---
title: NVIDIA Container Toolkit und Docker/Podman für den Aufbau einer Deep-Learning-Entwicklungsumgebung (2) - Container-Runtime-Konfiguration für GPU-Nutzung, Dockerfile-Erstellung und Container-Image-Build
description: Diese Serie behandelt die Einrichtung einer containerisierten Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und deren Konfiguration als Remote-Server mit SSH und Jupyter Lab. Dieser Beitrag ist der zweite Teil der Serie und befasst sich mit der Erstellung eines Dockerfiles und dem Bauen eines Container-Images.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Übersicht
In dieser Serie behandeln wir die Installation von NVIDIA Container Toolkit und Docker oder Podman sowie die Erstellung eines Dockerfiles basierend auf CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub, um eine Deep-Learning-Entwicklungsumgebung aufzubauen. Für alle, die diese Umgebung nutzen möchten, stelle ich das fertige [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und [Image](https://hub.docker.com/r/yunseokim/dl-env/tags) auf GitHub und Docker Hub zur Verfügung, zusammen mit einer Anleitung zur Konfiguration von SSH und Jupyter Lab für die Nutzung als Remote-Server.  
Die Serie besteht aus 3 Teilen, und dieser Beitrag ist der zweite Teil.
- [Teil 1: Installation von NVIDIA Container Toolkit & Container-Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Teil 2: Container-Runtime-Konfiguration für GPU-Nutzung, Dockerfile-Erstellung und Container-Image-Build (dieser Beitrag)
- Teil 3 (geplant)

Wir gehen von einer x86_64-Linux-Umgebung mit einer CUDA-fähigen NVIDIA-Grafikkarte aus. Obwohl ich die Anleitung hauptsächlich für Ubuntu und Fedora getestet habe, können bei anderen Distributionen einige Details abweichen.  
(Aktualisiert am 18.02.12025)

> **Fehlerkorrektur**  
> In der ursprünglichen Version dieses Beitrags vom August 12024 gab es einige Fehler im Abschnitt [Dockerfile-Erstellung](#5-dockerfile-erstellung) und im daraus erstellten Image. Die Probleme waren:
> - Bei der Erstellung des remote-Kontos wurde das Passwort nicht korrekt gesetzt; eigentlich sollte man sich mit dem Passwort "000000" anmelden können, was aber nicht funktionierte
> - Der SSH-Daemon wurde beim Containerstart nicht automatisch gestartet
>
> Diese Probleme wurden kürzlich erkannt und am 16. Februar 12025 um 2 Uhr morgens (UTC+9) wurden die fehlerhaften Dockerfiles und Docker-Images im [GitHub-Repository](https://github.com/yunseo-kim/dl-env-docker) und auf [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) durch korrigierte Versionen ersetzt.  
> Wenn Sie das Dockerfile oder Docker-Image vor diesem Zeitpunkt heruntergeladen haben, aktualisieren Sie bitte auf die korrigierte Version.  
> Ich entschuldige mich bei allen, die durch die fehlerhaften Inhalte Probleme hatten.
{: .prompt-info }

## Bevor wir beginnen
Dieser Beitrag ist die Fortsetzung von [Teil 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1). Falls Sie diesen noch nicht gelesen haben, empfehle ich, zuerst dort zu beginnen.

## 4. Container-Runtime-Konfiguration
### Bei Verwendung von Podman
[Konfiguration mit CDI (Container Device Interface)](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Führen Sie den folgenden Befehl aus, um die CDI-Spezifikationsdatei im Verzeichnis `/etc/cdi`{: .filepath} zu erstellen:
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> Wenn Sie Ihre Grafikkarte wechseln oder die CUDA-Treiberkonfiguration ändern (einschließlich Versionsupgrades), müssen Sie die CDI-Spezifikationsdatei neu erstellen.
{: .prompt-warning }

> Die Verwendung des NVIDIA Container Runtime Hooks zusammen mit CDI kann zu Konflikten führen. Falls die Datei `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existiert, sollten Sie diese entweder löschen oder darauf achten, Container nicht mit gesetzter `NVIDIA_VISIBLE_DEVICES`-Umgebungsvariable auszuführen.
{: .prompt-warning }

### Bei Verwendung von Docker
Wir erklären die Konfiguration für den [Rootless-Modus](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Container-Runtime-Konfiguration mit `nvidia-ctk`
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
Dieser Befehl modifiziert die Datei `/etc/docker/daemon.json`{: .filepath}, damit Docker die NVIDIA Container Runtime nutzen kann.

#### 4-Docker-2. Docker-Daemon neustarten
Starten Sie den Docker-Daemon neu, um die Änderungen zu übernehmen:
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Konfiguration der Datei `/etc/nvidia-container-runtime/config.toml`{: .filepath} mit `sudo nvidia-ctk`
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Überprüfung der Konfiguration
Testen Sie die Konfiguration mit einem CUDA-Beispielcontainer.

Bei Verwendung von Podman:
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Bei Verwendung von Docker:
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Wenn eine Ausgabe ähnlich der folgenden erscheint, war die Konfiguration erfolgreich:

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

## 5. Dockerfile-Erstellung
Wir erstellen ein Dockerfile basierend auf den CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub.

- Berücksichtigen Sie die benötigten CUDA- und cuDNN-Versionen sowie die Linux-Distribution und -Version bei der Auswahl des Basis-Images.
- ![Von PyTorch 2.4.0 unterstützte CUDA-Version](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)Zum Zeitpunkt der Erstellung dieses Beitrags (Ende August 12024) unterstützt die neueste PyTorch-Version 2.4.0 CUDA 12.4. Daher verwenden wir hier das [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)-Image. Die neueste PyTorch-Version und die unterstützten CUDA-Versionen können auf der [PyTorch-Website](https://pytorch.org/get-started/locally/) überprüft werden.

Der vollständige Quellcode des Dockerfiles ist im GitHub-Repository [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) verfügbar. Im Folgenden erläutere ich den schrittweisen Aufbau dieses Dockerfiles.

### 5-1. Basis-Image festlegen
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Grundlegende Dienstprogramme und Python-Voraussetzungen installieren
```Dockerfile
# Install basic utilities and Python-related packages, gosu, and SSH server
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    apt-utils \
    curl \
    gosu \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip \
    ssh \
    tmux \
    && rm -rf /var/lib/apt/lists/* \
# verify that the binary works
    && gosu nobody true
```

### 5-3. Systemzeitzone einstellen (hier 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. SSH-Server für Fernzugriff einrichten  
Aus Sicherheitsgründen deaktivieren wir den Root-Login über SSH:
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Wir erstellen einen Nicht-Root-Benutzer namens 'remote' für SSH-Zugriffe:
```Dockerfile
# Create remote user (password can be passed to --build-arg at build time)
#
# This default password is very weak. Make sure to change it to your own unique
# password string!
#
# This Dockerfile assumes that the built image will only be used by yourself or
# a small group of trusted insiders, and if you need to distribute the image
# without exposing sensitive information, using --build-arg is dangerous.
# See the official Docker documentation.
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
ARG HOME_DIR="/home/$USER_NAME"
RUN useradd --create-home --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && echo "$USER_NAME:$USER_PASSWORD" | chpasswd
```

> Wenn Sie beim Bauen des Docker-Images keine speziellen Optionen angeben, ist das anfängliche Passwort für den 'remote'-Benutzer 000000. Dies ist aus Sicherheitsgründen sehr schwach, daher sollten Sie beim Bauen des Images die Option `--build-arg` verwenden, um ein eigenes Passwort festzulegen, oder das Passwort sofort nach dem ersten Start des Containers ändern. Für bessere Sicherheit sollten Sie die Passwort-Authentifizierung für SSH deaktivieren und stattdessen Schlüsseldateien für die Anmeldung verwenden. Idealerweise könnten Sie auch Hardware-Schlüssel wie Yubikey einsetzen.
> Die SSH-Server-Konfiguration wird im nächsten Teil dieser Serie behandelt. Für weitere Informationen können Sie die folgenden Ressourcen konsultieren:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> Dieses Dockerfile geht davon aus, dass das gebaute Image nur von Ihnen selbst oder einer kleinen Gruppe vertrauenswürdiger Personen verwendet wird. Wenn Sie das Image extern verteilen müssen, ist die Verwendung von `--build-arg` für Passwörter gefährlich und Sie sollten andere Methoden verwenden. Siehe [diese Dokumentation](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/) für weitere Informationen.
{: .prompt-danger }

### 5-5. Setuptools, pip installieren und PATH-Umgebungsvariable registrieren
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. Machine Learning- und Deep Learning-Pakete für die Entwicklungsumgebung installieren
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Wenn Sie Cupy, cuDF, cuML und DALI verwenden möchten, fügen Sie Folgendes zum Dockerfile hinzu:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Arbeitsverzeichnis erstellen
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Ports öffnen und `ENTRYPOINT` für den Containerstart konfigurieren
Wir öffnen die Ports 22 und 8888 für SSH und Jupyter Lab.  
Da für den automatischen Start des SSH-Daemons beim Containerstart Root-Rechte erforderlich sind, verwenden wir folgende Methode:
1. Der Container startet als Root-Benutzer
2. Direkt nach dem Start wird das Skript `/entrypoint.sh`{: .filepath} ausgeführt
3. Dieses Skript startet den SSH-Dienst und wechselt dann mit [`gosu`](https://github.com/tianon/gosu) zum remote-Benutzer
4. Wenn beim Containerstart kein spezieller Befehl angegeben wird, wird standardmäßig Jupyter Lab als remote-Benutzer (ohne Root-Rechte) gestartet

> Die Verwendung von `sudo` oder `su` in Docker- oder Podman-Containern wird generell nicht empfohlen. Wenn Root-Rechte benötigt werden, ist es besser, den Container als Root zu starten, die erforderlichen Aufgaben auszuführen und dann mit [`gosu`](https://github.com/tianon/gosu) zu einem Nicht-Root-Benutzer zu wechseln. Die Gründe dafür sind in den folgenden Ressourcen ausführlich erklärt:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Fügen Sie zunächst den folgenden Inhalt am Ende des Dockerfiles hinzu:
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Erstellen Sie dann im selben Verzeichnis wie das Dockerfile eine Datei namens `entrypoint.sh`{: .filepath} mit folgendem Inhalt:
```sh
#!/bin/bash
set -e

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

## 6. Docker-Image bauen und Container ausführen
### 6-1. Image bauen
Öffnen Sie ein Terminal im Verzeichnis mit dem Dockerfile und führen Sie folgenden Befehl aus:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Ersetzen Sie \<password\> durch das Passwort, das Sie für SSH-Logins verwenden möchten.
{: .prompt-info }

### 6-2. Test-Workload ausführen
Nach dem Build können Sie einen temporären Container starten, um zu überprüfen, ob alles funktioniert.

Für Podman:
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Für Docker:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Dieser Befehl startet einen Container namens `test-container` aus dem zuvor erstellten Image `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` und verbindet Port 22 des Host-Systems mit Port 22 des Containers sowie Port 88 des Hosts mit Port 8888 des Containers. Wenn das Docker-Image korrekt gebaut wurde und der Container erfolgreich gestartet ist, sollte JupyterLab im Container unter der Standardadresse `http:127.0.0.1:8888` laufen. Öffnen Sie einen Browser auf dem Host-System und navigieren Sie zu <http://127.0.0.1:88>, um auf JupyterLab zuzugreifen. Sie sollten einen Bildschirm ähnlich dem folgenden sehen:

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Öffnen Sie ein Terminal auf dem Host-System und führen Sie den Befehl `ssh remote@127.0.0.1` aus, um sich per SSH beim remote-Konto im Container anzumelden.  
Bei der ersten Anmeldung erhalten Sie eine Warnung, dass der Host-Schlüssel unbekannt ist. Geben Sie "yes" ein, um fortzufahren.  
Geben Sie dann das Passwort ein (wenn Sie es beim Image-Build nicht geändert haben, ist es standardmäßig "000000").
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {Fingerabdruck (jeder Schlüssel hat einen eindeutigen Wert)}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '127.0.0.1' (ED25519) to the list of known hosts.
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
Wenn Sie eine ähnliche Ausgabe sehen, war die SSH-Anmeldung erfolgreich. Geben Sie `exit` ein, um die Verbindung zu beenden.

### 6-3. (optional) Push auf Docker Hub
Um das erstellte Entwicklungsumgebungs-Image jederzeit nutzen zu können, ist es sinnvoll, es auf Docker Hub zu pushen.

> Um Ihr Image auf Docker Hub zu pushen, benötigen Sie ein Docker-Konto. Falls Sie noch keines haben, registrieren Sie sich unter <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Bei Docker Hub anmelden
##### Für Podman:
```bash
podman login docker.io
```

##### Für Docker:
```bash
docker login
```

#### 6-3-2. Image-Tag setzen
Ersetzen Sie `<dockerhub_username>`, `<repository_name>` und (optional) `:TAG` durch Ihre eigenen Werte.  
z.B. "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### Für Podman:
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Für Docker:
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Image pushen
Führen Sie abschließend den folgenden Befehl aus, um das Image auf Docker Hub zu pushen:

##### Für Podman:
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Für Docker:
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Sie können auf <https://hub.docker.com/> überprüfen, ob der Push erfolgreich war:  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

Das fertige Image ist im öffentlichen Repository [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) auf Docker Hub verfügbar und kann von jedem frei genutzt werden.

Um das Image zu pullen, ersetzen Sie einfach `push` durch `pull` in den oben genannten Befehlen.
