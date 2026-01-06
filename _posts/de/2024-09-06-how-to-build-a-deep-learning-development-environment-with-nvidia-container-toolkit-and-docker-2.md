---
title: "Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und Docker/Podman einrichten (2) – Container-Runtime für GPU-Nutzung konfigurieren, Dockerfile schreiben und Container-Image bauen"
description: "Diese Serie zeigt, wie man lokal mit dem NVIDIA Container Toolkit eine containerbasierte Deep-Learning-Umgebung aufsetzt und sie via SSH und JupyterLab als Remote-Server nutzbar macht. Dieser zweite Teil behandelt das Schreiben eines Dockerfiles und den Build des Container-Images."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Überblick

In dieser Serie geht es darum, NVIDIA Container Toolkit sowie Docker oder Podman zu installieren und auf Basis der in der Docker-Hub-[nvidia/cuda-Registry](https://hub.docker.com/r/nvidia/cuda) bereitgestellten CUDA- und cuDNN-Images ein Dockerfile zu erstellen, um eine Deep-Learning-Entwicklungsumgebung aufzubauen. Damit Interessierte das Ergebnis frei wiederverwenden können, teile ich das im Verlauf erstellte [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und das fertige [Image](https://hub.docker.com/r/yunseokim/dl-env/tags) über GitHub bzw. Docker Hub und stelle zusätzlich eine Anleitung zur Konfiguration von SSH und JupyterLab bereit, um das Setup als Remote-Server zu nutzen.  
Die Serie wird aus drei Beiträgen bestehen; der Beitrag, den du gerade liest, ist der zweite Teil.
- [Teil 1: NVIDIA Container Toolkit & Container-Engine installieren](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Teil 2: Container-Runtime für GPU-Nutzung konfigurieren, Dockerfile schreiben und Container-Image bauen (dieser Beitrag)
- Teil 3 (geplant)

Ich gehe von einem x86_64-Linux-System mit einer NVIDIA-Grafikkarte aus, die CUDA unterstützt. Auf Distributionen außer Ubuntu oder Fedora habe ich es nicht direkt getestet; einzelne Details können daher leicht abweichen.  
(Überarbeitet am 12026.1.6.)

> **Hinweis zur Fehlerkorrektur**
>
> In der im August 12024 veröffentlichten ersten Fassung dieses Beitrags gab es im Abschnitt [Dockerfile schreiben](#5-dockerfile-schreiben) sowie in Teilen des daraus gebauten Images einige Fehler. Betroffen waren insbesondere:
> - Im Abschnitt zur Erstellung des remote-Accounts war das Setzen des Passworts falsch beschrieben. Ich hatte angegeben, man könne sich mit „000000“ als initialem Passwort anmelden – das stimmte in der Praxis nicht. (Ergänzung vom 12025.12.19: Inzwischen ist das Initialpasswort ohnehin nicht mehr „000000“; daher bitte unbedingt den [entsprechenden Abschnitt unten](#5-4-ssh-server-für-remote-zugriff-einrichten) prüfen.)
> - Beim Start des Containers wurde der SSH-Daemon nicht automatisch gestartet.
>
> Diese Probleme habe ich im Februar 12025 erkannt und die fehlerhaften Dockerfiles sowie Docker-Images am 16. Februar 12025 gegen ca. 02:00 Uhr (KST, UTC+9) durch korrigierte Versionen in der [GitHub-Repository](https://github.com/yunseo-kim/dl-env-docker) und auf [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) ersetzt.  
> Falls du vor diesem Zeitpunkt das Dockerfile oder ein Image gepullt hast, ersetze es bitte durch die korrigierte Version.  
> Falls durch die falschen Angaben Verwirrung entstanden ist, entschuldige ich mich.
{: .prompt-info }

## Bevor du anfängst

Da dieser Beitrag direkt an [Teil 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1) anschließt, empfehle ich, ihn zuerst zu lesen, falls du das noch nicht getan hast.

## 4. Container-Runtime konfigurieren

### Wenn du Podman verwendest

[Konfiguration über CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> In älteren Versionen musste man beim Erstinstallieren des NVIDIA Container Toolkits – und danach jedes Mal, wenn man GPU-Geräte oder die Treiberkonfiguration (inkl. Versionsupgrade) änderte – die CDI-Spezifikationsdatei manuell neu erzeugen.
>
> Seit NVIDIA Container Toolkit `v1.18.0` wird jedoch über den systemd-Service `nvidia-cdi-refresh` die CDI-Datei `/var/run/cdi/nvidia.yaml` automatisch erzeugt und aktualisiert, und zwar in folgenden Fällen:
> - bei Installation oder Upgrade des NVIDIA Container Toolkits
> - bei Installation oder Upgrade des NVIDIA GPU-Treibers
> - beim Systemneustart
>
> Damit muss man – anders als früher – in der Regel nichts mehr zusätzlich tun. Entsprechend habe ich den Inhalt dieses Beitrags angepasst.
>
> Hinweis: Beim Entfernen des GPU-Treibers oder bei einer MIG-Neukonfiguration kann `nvidia-cdi-refresh` nicht automatisch reagieren; dann muss man `nvidia-cdi-refresh.service` manuell neu starten, um eine CDI-Neugenerierung anzustoßen.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> Wenn man den NVIDIA Container Runtime hook zusammen mit CDI nutzt, kann es zu Konflikten kommen. Falls `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existiert, lösche diese Datei oder achte darauf, Container nicht mit gesetzter Umgebungsvariable `NVIDIA_VISIBLE_DEVICES` zu starten.
{: .prompt-warning }

### Wenn du Docker verwendest

Die folgenden Schritte sind für den [Rootless-Modus](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode) beschrieben.

#### 4-Docker-1. Container-Runtime-Konfiguration mit `nvidia-ctk`

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

Dieser Befehl passt die Datei `/etc/docker/daemon.json`{: .filepath} so an, dass Docker die NVIDIA Container Runtime verwenden kann.

#### 4-Docker-2. Docker-Daemon neu starten

Damit die geänderte Konfiguration wirksam wird, starte den Docker-Daemon neu.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. Konfigurationsdatei `/etc/nvidia-container-runtime/config.toml`{: .filepath} mit `sudo nvidia-ctk` anpassen

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Prüfen, ob alles korrekt eingerichtet ist

Starte einen Beispiel-CUDA-Container.

Für Podman:

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Für Docker:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

Wenn ungefähr eine Ausgabe wie die folgende erscheint, ist es erfolgreich.

```bash
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 555.58.02              Driver Version: 555.58.02      CUDA Version: 12.5     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3090        Off |   00000000:01:00.0  On |                  N/A |
|  0%   46C    P8             29W /  350W |     460MiB /  24576MiB |      2%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

## 5. Dockerfile schreiben

Wir schreiben ein Dockerfile für die Entwicklungsumgebung auf Basis der CUDA- und cuDNN-Images aus der Docker-Hub-[nvidia/cuda-Registry](https://hub.docker.com/r/nvidia/cuda).

- Dabei solltest du die benötigten CUDA- und cuDNN-Versionen sowie Distribution und Versionsstand von Linux berücksichtigen, um das passende Base-Image auszuwählen. 
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  Stand Ende August 12024 (Zeitpunkt der ursprünglichen Erstellung dieses Beitrags) unterstützt die damals aktuelle PyTorch-Version 2.4.0 CUDA 12.4. Daher wurde hier das Image [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) verwendet. Auf der [PyTorch-Website](https://pytorch.org/get-started/locally/) kannst du die aktuelle PyTorch-Version sowie die unterstützten CUDA-Versionen prüfen.

Den vollständigen Dockerfile-Source habe ich in der GitHub-Repository [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) veröffentlicht. Im Folgenden erkläre ich Schritt für Schritt, wie er erstellt wurde.

> (+ Überarbeitung am 12026.1.6.)  
> Dockerfiles und Images für PyTorch 2.9.1 mit Unterstützung für CUDA 12.8 / 13.0 habe ich ebenfalls in derselben GitHub-Repository sowie in der öffentlichen Docker-Hub-Repository [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) ergänzt. Den Inhalt dieses Beitrags habe ich entsprechend auf PyTorch 2.9.1 und CUDA 13.0 aktualisiert.
>
> Außerdem habe ich scikit-image, XGBoost sowie innerhalb des RAPIDS-Ökosystems die Bibliotheken cuGraph, cuxfilter, cuCIM, RAFT und cuVS ins Image aufgenommen und zusätzlich zur bisherigen `amd64`-Architektur auch `arm64`-Support ergänzt.
{: .prompt-info }

### 5-1. Base-Image festlegen

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. System-Zeitzone festlegen (hier: „Asia/Seoul“)

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> Ich habe mich dabei hauptsächlich an [diesem Artikel](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22) orientiert.
{: .prompt-tip }

### 5-3. Grundlegende System-Utilities installieren

```Dockerfile
# Install basic utilities, gosu, and SSH server
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update -y && apt-get install -y --no-install-recommends \
        apt-utils \
        curl \
        gosu \
        openssh-server \
        ssh \
        tmux \
        tzdata \
# verify that the binary works
    && gosu nobody true
```

### 5-4. SSH-Server für Remote-Zugriff einrichten

Aus Sicherheitsgründen konfigurieren wir SSH so, dass ein Login als root nicht möglich ist.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Für den SSH-Login erstellen wir einen Non-Root-User mit dem Namen „remote“.

```Dockerfile
# Create remote user
#
# The password must be pre-specified at build time with the `DL_ENV_PASSWD`
# environment variable.
ARG USER_NAME="remote"
ARG USER_UID=1001
ARG USER_GID=$USER_UID
ARG HOME_DIR="/home/$USER_NAME"
RUN --mount=type=secret,id=USER_PASSWORD \
    groupadd --gid $USER_GID $USER_NAME && \
    useradd --uid $USER_UID --gid $USER_GID --create-home \
        --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && awk -v user="$USER_NAME" '{print user ":" $0}' /run/secrets/USER_PASSWORD | chpasswd
```

> Inhalte von Build-Argumenten (`ARG`) oder Umgebungsvariablen (`ENV`) sind im gebauten Image direkt einsehbar. Deshalb sollte man [für Passwörter, API-Keys und andere sensitive Daten eine andere Methode verwenden](https://docs.docker.com/build/building/secrets/). Hier wird dafür [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts) genutzt.
{: .prompt-danger }

> Wie [später beschrieben](#6-1-image-bauen), musst du beim Build dieses Images über die Umgebungsvariable `DL_ENV_PASSWD` eine Zeichenkette für das User-Passwort setzen. Beim [auf Docker Hub veröffentlichten Image](https://hub.docker.com/r/yunseokim/dl-env/tags) lautet das Initialpasswort `satisfied-flip-remake`. Wenn du dieses öffentlich bekannte Default-Passwort unverändert nutzt, ist das sicherheitstechnisch äußerst riskant – ändere es daher direkt nach dem ersten Containerstart. Außerdem ist es aus Sicherheitsgründen sinnvoll, die Passwort-Anmeldung per SSH zu deaktivieren und nur noch Key-basierte Logins zu erlauben; idealerweise kombiniert man das sogar mit Hardware-Keys wie einem Yubikey.
>
> Auf die SSH-Server-Konfiguration gehe ich im nächsten Teil dieser Serie noch etwas ein. Für weitere Details sind die folgenden Dokumente hilfreich:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. uv installieren und Umgebungsvariablen setzen

> **Berücksichtigung von [PEP 668](https://peps.python.org/pep-0668/) (Externally Managed Environments) und Einführung von uv (Überarbeitung am 12026.1.6.)**
>
> In der Vergangenheit habe ich in diesem Beitrag ein Dockerfile beschrieben, das Python-Pakete im Container-Image direkt per `pip` installiert, ohne eine separate virtuelle Umgebung (`venv`) zu erstellen. Der Gedanke dahinter war, dass in einem Single-Purpose-Container die Gefahr, Systemsoftware „kaputtzuinstallieren“, geringer ist; selbst wenn etwas schiefläuft, kann man das Image einfach neu bauen und einen neuen Container erstellen. Das wird auch in [PEP 668](https://peps.python.org/pep-0668/#use-cases) teilweise anerkannt:
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> Dennoch hat sich als Standard etabliert, Installationen via Python-Paketmanager wie `pip` strikt auf virtuelle Umgebungen zu beschränken, um eine saubere Trennung zu extern verwalteten (externally managed) Paketen sicherzustellen, die z. B. über den OS-Paketmanager installiert werden. Entsprechend habe ich den Beitrag so überarbeitet, dass zunächst eine virtuelle Umgebung erstellt und die benötigten Pakete darin installiert werden – konform zu [PEP 668](https://peps.python.org/pep-0668/) und der zugehörigen Spezifikation [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/).
>
> Die offiziell unterstützte Standardbibliothek zur Erstellung und Verwaltung virtueller Umgebungen ist `venv`, wie ich auch schon in [einem anderen Beitrag (früh 12021)](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended) erwähnt habe. Seit jedoch [Astral](https://astral.sh/) den in Rust entwickelten, performanten Python-Paket- und Projektmanager [`uv`](https://docs.astral.sh/uv/) erstmals in 12024 veröffentlicht hat, hat er sich aufgrund wichtiger Vorteile schnell als de-facto-Standard etabliert:
> - im Vergleich zu `pip` massiv schnelleres Dependency-Resolving und Paketinstallation (10–100×) ([Benchmarks](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md))
> - sehr gute Bedienbarkeit
> - [sehr gute Kompatibilität zu `pip` und `venv`](https://docs.astral.sh/uv/pip/)
>
> Gerade bei ML-Paketen wie PyTorch oder RAPIDS, die viele und oft große Abhängigkeiten mitbringen, spielen diese Vorteile ihre Stärken aus. Zusätzlich nutzt [`uv` Caches aktiv und effizient](https://docs.astral.sh/uv/concepts/cache/); wenn man – wie hier – beim Image-Build Cache-Mounts sinnvoll einsetzt, lässt sich dadurch die Build-Zeit deutlich verkürzen ([Docker-Caching-Guide](https://docs.astral.sh/uv/guides/integration/docker/#caching)). Daher verwende ich hier `uv` sowohl für das Erstellen/Verwalten der venv als auch für die Paketinstallation. Ich habe mich dabei hauptsächlich an der offiziellen Doku ["Using uv in Docker"](https://docs.astral.sh/uv/guides/integration/docker/) orientiert.
{: .prompt-info }

```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_UID:$USER_GID
WORKDIR $HOME_DIR

# Install uv by copying the binary from the official distroless image
COPY --from=ghcr.io/astral-sh/uv:0.9.21 /uv /uvx /bin/
ENV PATH="$HOME_DIR/.local/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ARG UV_CACHE_DIR="/tmp/uv-cache"
```

> **Warum `UV_CACHE_DIR` nicht auf dem Default `"$HOME_DIR/.cache/uv"`, sondern außerhalb des Home-Verzeichnisses (`"/tmp/uv-cache"`) liegt**
>
> Normalerweise sollte ein User, der per `useradd --create-home` angelegt wurde, Eigentümer seines Home-Verzeichnisses sein – und das ist hier auch der Fall.
> Beim Image-Build mit Podman habe ich jedoch einen Bug festgestellt: Selbst wenn in früheren Layern die Ownership korrekt gesetzt wurde, kann beim späteren Mounten von Caches o. Ä. in nachfolgenden Layern die Ownership-Metadaten des übergeordneten Verzeichnisses auf den Default (root) zurückgesetzt werden. Bei der Suche dazu bin ich auf ein [Issue gestoßen, das ein anderer User ca. drei Wochen zuvor gemeldet hatte](https://github.com/containers/podman/issues/27777); bisher gibt es dort noch keine Antwort. Zusätzliche Details zu meinem Fall habe ich [als Kommentar in diesem Issue ergänzt](https://github.com/containers/podman/issues/27777#issuecomment-3712237296).
>
> Damit das Zurücksetzen auf root im Build nicht problematisch wird, setze ich im Build-Schritt `UV_CACHE_DIR` daher auf `"/tmp/uv-cache"` statt unter `$HOME_DIR`. Dieser Cache ist ohnehin nicht Bestandteil des finalen Images – daher ist die Pfadänderung unkritisch.
{: .prompt-tip }

### 5-6. Python installieren, virtuelle Umgebung erstellen, setuptools & pip installieren

```Dockerfile
# Install the latest, managed Python executables
ARG UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv python install 3.13 --default

# Create a virtual environment
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv venv --python 3.13 --seed
# Use the virtual environment automatically
ENV VIRTUAL_ENV=$HOME_DIR/.venv
# Place entry points in the environment at the front of the path & .profile
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN echo "source $VIRTUAL_ENV/bin/activate" >> $HOME_DIR/.profile
# Allow pip to only run in a virtual environment; exit with an error otherwise
ENV PIP_REQUIRE_VENV=true

# Install setuptools
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install setuptools
```

### 5-7. ML-/DL-Pakete für die Entwicklungsumgebung installieren

#### 5-7-1. Gemeinsame Pakete

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & CUDA-spezifische GPU-Beschleunigungsbibliotheken

##### Nur PyTorch installieren

Wenn du nur PyTorch installieren willst, füge Folgendes ins Dockerfile ein:

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & CuPy & RAPIDS & DALI

Wenn du zusätzlich zu PyTorch auch CuPy, RAPIDS (cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS) sowie DALI verwenden willst, füge Folgendes ins Dockerfile ein:

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        --index-url https://download.pytorch.org/whl/cu130 \
        --extra-index-url=https://pypi.org/simple \
        --extra-index-url=https://pypi.nvidia.com \
        "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        cupy-cuda13x \
        "cudf-cu13==25.12.*" "dask-cudf-cu13==25.12.*" "cuml-cu13==25.12.*" \
        "cugraph-cu13==25.12.*" "nx-cugraph-cu13==25.12.*" "cuxfilter-cu13==25.12.*" \
        "cucim-cu13==25.12.*" "pylibraft-cu13==25.12.*" "raft-dask-cu13==25.12.*" \
        "cuvs-cu13==25.12.*" nvidia-dali-cuda130
```

> PyTorch- und RAPIDS-Pakete teilen einige Abhängigkeitsbibliotheken (cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE). Installiert man sie getrennt, können sich die jeweils geforderten Versionen unterscheiden; dann überschreibt eine spätere Installation die zuvor installierte Version, was das Risiko für Dependency-Konflikte erhöht. Deshalb ist es sinnvoll, diese Pakete in einem einzigen `uv pip install`-Aufruf zu installieren, sodass der Resolver alle Constraints gleichzeitig berücksichtigen kann und dabei die von PyTorch geforderten Versionen priorisiert.
{: .prompt-tip }

### 5-8. Verzeichnis als Workspace anlegen

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. Ports öffnen und `ENTRYPOINT` für den Containerstart setzen

Für SSH und JupyterLab öffnen wir die Ports 22 und 8888.  
Damit beim Containerstart der SSH-Daemon automatisch gestartet werden kann, sind Root-Rechte nötig; daher verwenden wir folgenden Ansatz:
1. Container startet zunächst als root
2. Direkt nach dem Start wird das Skript `/entrypoint.sh`{: .filepath} ausgeführt
3. Das Skript startet den SSH-Service und wechselt anschließend mittels [`gosu`](https://github.com/tianon/gosu) zum remote-User
4. Wenn beim Containerstart kein separates Kommando angegeben wird, startet standardmäßig JupyterLab als remote-User (Non-Root)

> In Docker-/Podman-Containern wird die Verwendung von `sudo` oder `su` generell nicht empfohlen. Wenn Root-Rechte benötigt werden, ist es besser, wie hier beschrieben zunächst als root zu starten, root-pflichtige Aufgaben auszuführen und anschließend mit [`gosu`](https://github.com/tianon/gosu) zu einem Non-Root-User zu wechseln. Die Hintergründe werden in den folgenden Quellen ausführlich erläutert:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Trage zunächst am Ende des Dockerfiles Folgendes ein:

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Erstelle danach im selben Verzeichnis wie das Dockerfile eine Skriptdatei `entrypoint.sh`{: .filepath} mit folgendem Inhalt:

```sh
#!/bin/bash
set -e

# Dump environment variables
printenv | grep _ >> /etc/environment

# Run SSH daemon in the background
service ssh start

# Move to the workspace directory and run Jupyter Lab
cd "$WORK_DIR"
if [ $# -gt 0 ];then
    #su ${USER_NAME} -c "exec $@"
    exec gosu ${USER_NAME} $@
else
    #su ${USER_NAME} -c "exec jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}""
    exec gosu ${USER_NAME} jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}"
fi
```

> Üblicherweise erben Prozesse, die via `docker exec` oder `CMD` gestartet werden, die Docker-`ENV`-Variablen direkt. Bei Sessions, die per SSH aufgebaut werden, ist das jedoch oft nicht der Fall, weil SSH beim Login eine neue Shell-Session erzeugt.
>
> Um das zu lösen und auch in SSH-Sessions Zugriff auf vordefinierte Umgebungsvariablen wie `$WORK_DIR` zu haben, muss man die Umgebungsvariablen vor dem Start des SSH-Services in `/etc/environment`{: .filepath } dumpen, z. B. mit `printenv | grep _ >> /etc/environment`.
>
> Die folgenden Links sind dazu hilfreich:
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. OCI-Image bauen und Container ausführen

### 6-1. Image bauen

Öffne im Verzeichnis, in dem das Dockerfile liegt, ein Terminal und setze die Umgebungsvariable `DL_ENV_PASSWD`.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> Anstelle von \<your_own_password\> trägst du das Login-Passwort ein, das du beim SSH-Zugriff verwenden willst.
{: .prompt-info }

Jetzt **schließe dieses Terminalfenster nicht**, sondern führe im selben Fenster direkt anschließend den Build-Befehl aus.

#### Für Podman

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> Wenn du unter Podman nicht nur für die Plattform deines aktuellen Geräts (OS/Architektur), sondern für alle vom Base-Image unterstützten Plattformen bauen willst, nutze dafür wie folgt die Option [`--all-platforms`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms) und verwende statt `--tag`/`-t` die Option [`--manifest`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant).
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> Für Docker wird das hier nicht separat erläutert; falls du es brauchst, siehe die [offizielle Docker-Doku](https://docs.docker.com/build/building/multi-platform/).
{: .prompt-tip }

#### Für Docker

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. Beispiel-Workload ausführen

Nach erfolgreichem Build startest du zum Test einen temporären Container.

Für Podman:

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Für Docker:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Wenn du diese Befehle eingibst, wird aus dem zuvor gebauten Image `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04` ein Container namens `test-container` gestartet. Anschließend werden Port 2222 des Host-Systems mit Port 22 des Containers sowie Port 8888 des Hosts mit Port 8888 des Containers verbunden. Wenn der Build korrekt war und der Container ohne Probleme gestartet ist, läuft in `test-container` JupyterLab unter der Standardadresse `http:127.0.0.1:8888`. Öffne daher auf dem Host, auf dem Podman/Docker läuft, einen Browser und rufe <http://127.0.0.1:8888> auf; du solltest dann auf die interne Adresse `http://127.0.0.1:8888` im Container weitergeleitet werden und eine Oberfläche wie folgt sehen.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Öffne auf dem Host ein Terminal und teste den SSH-Login in den Container über `ssh remote@127.0.0.1 -p 2222`.  
Beim ersten Login erscheint eine Warnung, dass noch keine Information zum Host-Key vorliegt und die Authentizität nicht verifiziert werden kann; wenn du dann „yes“ eingibst, wird die Verbindung fortgesetzt.  
Gib anschließend zum Login das Passwort ein, das du beim Build gesetzt hast (oder – wenn du das [Docker-Hub-Image](https://hub.docker.com/r/yunseokim/dl-env/tags) gepullt hast und dich erstmals einloggst – das Initialpasswort `satisfied-flip-remake`).

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {Fingerabdruck (hat je Schlüssel einen jeweils eindeutigen Wert)}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:2222' (ED25519) to the list of known hosts.
remote@127.0.0.1's password: 
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 6.12.11-200.fc41.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

```

Wenn die Ausgabe ungefähr so aussieht, war der SSH-Login erfolgreich. Zum Beenden gibst du `exit` ein.

### 6-3. (optional) Auf Docker Hub pushen

Wenn du das erstellte Entwicklungsumgebungs-Image bei Bedarf jederzeit per Pull wiederverwenden willst, ist es sinnvoll, das gebaute Image auf Docker Hub zu pushen.  

> Um ein eigenes Image auf Docker Hub zu pushen, brauchst du einen Docker-Account. Falls du noch keinen hast, registriere dich zuerst unter <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Bei Docker Hub einloggen

##### Für Podman

```bash
podman login docker.io
```

##### Für Docker

```bash
docker login
```

#### 6-3-2. Image taggen

Fülle `<dockerhub_username>`, `<repository_name>` und (optional) `:TAG` mit deinen eigenen Werten aus.  
z. B. „yunseokim“, „dl-env“, „rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04“

> Falls du zuvor bereits ein Multi-Platform-Build (für alle vom Base-Image unterstützten Plattformen) erstellt hast und die gesamte Manifest-Liste bzw. den Image-Index auf einmal pushen willst, überspringe diesen Schritt und gehe direkt zu [Image pushen](#6-3-3-image-pushen), und folge dort der beschriebenen Methode.
{: .prompt-tip }

##### Für Podman

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Für Docker

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Image pushen

Zum Schluss pushst du das Image mit folgendem Befehl auf Docker Hub.

##### Für Podman

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> Unter Podman kannst du mehrere plattformspezifische Images als Manifest-Liste bzw. Image-Index gebündelt pushen, indem du den Befehl [`podman manifest push`](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls) wie folgt verwendest:
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> z. B.
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### Für Docker

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

Auf <https://hub.docker.com/> kannst du anschließend prüfen, ob es wie folgt erfolgreich gepusht wurde.

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

Das fertige Image aus diesem Prozess habe ich in der öffentlichen Docker-Hub-Repository [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) veröffentlicht; es kann von allen frei genutzt werden.

Um das Image zu pullen, ersetze im zuvor verwendeten Push-Befehl einfach `push` durch `pull` und führe ihn aus.
