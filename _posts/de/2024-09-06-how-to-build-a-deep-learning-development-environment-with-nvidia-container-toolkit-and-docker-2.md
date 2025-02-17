---
title: Aufbau einer Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und Docker/Podman (2) - Container-Runtime-Konfiguration für GPU-Nutzung, Erstellung eines Dockerfiles und Aufbau eines Container-Images
description: Diese Serie behandelt den Aufbau einer containerisierten Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit auf dem lokalen System und die Konfiguration von SSH und Jupyter Lab zur Nutzung als Remote-Server. Dieser Beitrag ist der zweite Teil der Serie und befasst sich mit dem Prozess der Erstellung eines Dockerfiles und dem Aufbau eines Container-Images.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---

## Überblick
In dieser Serie behandeln wir die Installation von NVIDIA Container Toolkit und Docker oder Podman sowie die Erstellung eines Dockerfiles basierend auf CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub, um eine Deep-Learning-Entwicklungsumgebung aufzubauen. Für diejenigen, die es benötigen, teile ich das [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und [Image](https://hub.docker.com/r/yunseokim/dl-env/tags), die durch diesen Prozess erstellt wurden, über GitHub und Docker Hub, damit sie frei verwendet werden können. Zusätzlich biete ich eine Anleitung zur Konfiguration von SSH und Jupyter Lab für die Nutzung als Remote-Server.  
Die Serie wird aus 3 Beiträgen bestehen, und dieser Beitrag, den Sie gerade lesen, ist der zweite Teil der Serie.
- [Teil 1: Installation von NVIDIA Container Toolkit & Container Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Teil 2: Container-Runtime-Konfiguration für GPU-Nutzung, Erstellung eines Dockerfiles und Aufbau eines Container-Images (dieser Beitrag)
- Teil 3 (geplant)

Wir gehen davon aus, dass Sie in einer x86_64 Linux-Umgebung mit einer NVIDIA-Grafikkarte arbeiten, die CUDA unterstützt. Bitte beachten Sie, dass einige spezifische Details bei anderen Distributionen als Ubuntu oder Fedora leicht abweichen können, da ich sie nicht direkt getestet habe.  
(Inhalt aktualisiert am 18.02.2025)

> **Fehlerkorrektur-Hinweis**  
> In der ursprünglichen Version dieses Beitrags, die im August 2024 hochgeladen wurde, gab es einige Fehler im Abschnitt [Erstellung des Dockerfiles](#5-erstellung-des-dockerfiles) und in dem daraus erstellten Image. Die problematischen Bereiche waren:
> - Bei der Erstellung des remote-Kontos war die Passworteinstellung fehlerhaft, und es war nicht möglich, sich mit dem Passwort "000000" anzumelden, wie es eigentlich vorgesehen war
> - Der SSH-Daemon wurde beim Containerstart nicht automatisch gestartet
>
> Diese Probleme wurden kürzlich erkannt, und am 16. Februar 2025 um etwa 2 Uhr morgens koreanischer Zeit (UTC+9) wurden die fehlerhaften Dockerfiles und Docker-Images im [GitHub-Repository](https://github.com/yunseo-kim/dl-env-docker) und auf [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) durch korrigierte Versionen ersetzt.  
> Wenn Sie das Dockerfile oder Docker-Image vor diesem Zeitpunkt heruntergeladen haben, ersetzen Sie es bitte durch die aktualisierte Version.  
> Ich entschuldige mich bei allen, die aufgrund der fehlerhaften Informationen Verwirrung erlebt haben.
{: .prompt-info }

## Bevor Sie beginnen
Dieser Beitrag ist eine Fortsetzung von [Teil 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1). Wenn Sie ihn noch nicht gelesen haben, empfehle ich, zuerst den vorherigen Beitrag zu lesen.

## 4. Konfiguration der Container-Runtime
### Wenn Sie Podman verwenden
[Konfigurieren Sie mit CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Führen Sie den folgenden Befehl aus, um die CDI-Spezifikationsdatei im Verzeichnis `/etc/cdi`{: .filepath} zu erstellen.
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> Wenn Sie die Grafikkarte wechseln oder die CUDA-Treiberkonfiguration ändern (einschließlich Versionsupgrades), müssen Sie die CDI-Spezifikationsdatei neu erstellen.
{: .prompt-warning }

> Die Verwendung des NVIDIA Container Runtime Hooks zusammen mit CDI kann zu Konflikten führen. Wenn `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existiert, löschen Sie diese Datei oder achten Sie darauf, den Container nicht mit der Umgebungsvariable `NVIDIA_VISIBLE_DEVICES` auszuführen.
{: .prompt-warning }

### Wenn Sie Docker verwenden
Wir erklären basierend auf dem [rootless Modus](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Konfiguration der Container-Runtime mit dem `nvidia-ctk` Befehl
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
Dieser Befehl modifiziert die Datei `/etc/docker/daemon.json`{: .filepath}, damit Docker die NVIDIA Container Runtime nutzen kann.

#### 4-Docker-2. Neustart des Docker-Daemons
Starten Sie den Docker-Daemon neu, um die geänderten Einstellungen anzuwenden.
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Konfiguration der Datei `/etc/nvidia-container-runtime/config.toml`{: .filepath} mit dem `sudo nvidia-ctk` Befehl
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Überprüfung der korrekten Konfiguration
Führen Sie einen Beispiel-CUDA-Container aus.

Wenn Sie Podman verwenden, führen Sie den folgenden Befehl aus:
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Wenn Sie Docker verwenden, führen Sie den folgenden Befehl aus:
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Wenn eine Ausgabe ähnlich der folgenden angezeigt wird, war es erfolgreich.

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

## 5. Erstellung des Dockerfiles
Wir erstellen ein Dockerfile für die Entwicklungsumgebung basierend auf den CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub.

- Sie müssen das zu verwendende Image basierend auf den benötigten CUDA- und cuDNN-Versionen, der Art und Version der Linux-Distribution usw. auswählen. 
- ![Von PyTorch 2.4.0 unterstützte CUDA-Version](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)Zum Zeitpunkt des Schreibens dieses Beitrags Ende August 2024 unterstützt die neueste Version von PyTorch, Version 2.4.0, CUDA 12.4. Daher verwenden wir hier das [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) Image. Sie können die neueste Version von PyTorch und die unterstützte CUDA-Version auf der [PyTorch-Website](https://pytorch.org/get-started/locally/) überprüfen.

Der Quellcode des fertigen Dockerfiles ist im GitHub-Repository [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) veröffentlicht. Im Folgenden wird der Prozess der Erstellung dieses Dockerfiles Schritt für Schritt erklärt.

### 5-1. Festlegung des Basis-Images
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Installation grundlegender Dienstprogramme und Python-Voraussetzungen
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

### 5-3. Einstellung der Systemzeitzone (in diesem Beitrag verwenden wir 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. SSH-Server-Konfiguration für Fernzugriff  
Aus Sicherheitsgründen konfigurieren wir den SSH-Server so, dass keine Root-Anmeldung bei der Fernverbindung möglich ist.
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Wir erstellen einen Nicht-Root-Benutzer namens 'remote' für die SSH-Verbindung.
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

> Wenn Sie beim Erstellen des Docker-Images mit diesem Dockerfile keine separate Option angeben, ist der anfängliche Kontopasswort für den Benutzer 'remote' 000000. Dies ist aus Sicherheitsgründen sehr schwach, daher sollten Sie entweder die Option `--build-arg` beim Erstellen des Docker-Images verwenden, um ein separates Anmeldepasswort festzulegen, oder die Einstellungen sofort nach der ersten Ausführung des Containers ändern. Für die Sicherheit ist es ratsam, die Passwortanmeldung für SSH-Verbindungen zu deaktivieren und nur die Anmeldung über eine separate Schlüsseldatei zu ermöglichen. Idealerweise könnte auch ein Hardware-Schlüssel wie Yubikey verwendet werden.
> Die SSH-Server-Konfiguration wird im nächsten Teil dieser Serie etwas ausführlicher behandelt. Wenn Sie mehr darüber erfahren möchten, können Sie die folgenden Dokumente konsultieren:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> Außerdem geht dieses Dockerfile davon aus, dass das erstellte Image nur von Ihnen selbst oder einer kleinen Gruppe vertrauenswürdiger Insider verwendet wird. Wenn Sie das erstellte Image extern verteilen müssen, ist die Passworteinstellung über `--build-arg` gefährlich und Sie sollten eine andere Methode verwenden. Bitte beachten Sie [dieses Dokument](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/).
{: .prompt-danger }

### 5-5. Installation von setuptools, pip und Registrierung der PATH-Umgebungsvariable
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. Installation von Machine Learning- und Deep Learning-Paketen für die Entwicklungsumgebung
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

### 5-7. Erstellung eines Verzeichnisses als Arbeitsbereich
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Öffnen von Ports und Einstellung des `ENTRYPOINT` für die Containerausführung
Wir öffnen die Ports 22 und 8888 für SSH und Jupyter Lab-Zugriff.  
Um den SSH-Daemon beim Containerstart automatisch auszuführen, benötigen wir Root-Rechte. Daher verwenden wir die folgende Methode:
1. Beim Containerstart als Root-Konto angemeldet
2. Ausführung des `/entrypoint.sh`{: .filepath} Skripts direkt nach dem Containerstart
3. In diesem Skript starten wir den SSH-Dienst und wechseln dann mit [`gosu`](https://github.com/tianon/gosu) zum remote-Konto
4. Wenn beim Containerstart kein separater Befehl angegeben wurde, wird standardmäßig Jupyter Lab als remote-Konto (ohne Root-Rechte) ausgeführt

> Im Allgemeinen wird die Verwendung von `sudo` oder `su` in Docker- oder Podman-Containern nicht empfohlen. Wenn Root-Rechte benötigt werden, ist es besser, den Container zunächst als Root-Konto zu starten, die erforderlichen Root-Aufgaben auszuführen und dann mit [`gosu`](https://github.com/tianon/gosu) zu einem Nicht-Root-Benutzer zu wechseln, wie hier beschrieben. Die Gründe dafür sind in den folgenden Ressourcen ausführlich erklärt, die bei Bedarf hilfreich sein können:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Fügen Sie zunächst den folgenden Inhalt am Ende des Dockerfiles ein:
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Erstellen Sie als Nächstes eine Skriptdatei namens `entrypoint.sh`{: .filepath} im selben Verzeichnis wie das erstellte Dockerfile und füllen Sie sie mit folgendem Inhalt:
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

## 6. Erstellung des Docker-Images und Ausführung des Containers
### 6-1. Image-Erstellung
Öffnen Sie ein Terminal im Verzeichnis, in dem sich das Dockerfile befindet, und führen Sie den folgenden Befehl aus:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Ersetzen Sie <password> durch das Anmeldepasswort, das Sie für die SSH-Verbindung verwenden möchten.
{: .prompt-info }

### 6-2. Ausführung einer Beispiel-Workload
Nach Abschluss des Builds führen Sie einen Einweg-Container aus, um zu überprüfen, ob alles ordnungsgemäß funktioniert.

Für Podman führen Sie den folgenden Befehl aus:
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Für Docker führen Sie den folgenden Befehl aus:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Wenn Sie diesen Befehl im Terminal eingeben, wird ein Container namens `test-container` aus dem zuvor erstellten `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` Image gestartet und die Ports 22 und 8888 des Containers werden mit den Ports 22 und 88 des Hostsystems verbunden. Wenn das Docker-Image im vorherigen Schritt erfolgreich erstellt wurde und der Container problemlos gestartet wurde, sollte JupyterLab im `test-container` Container unter der Standardadresse `http:127.0.0.1:8888` laufen. Daher sollten Sie, wenn Sie einen Browser auf dem Hostsystem öffnen, auf dem die Docker Engine läuft, und <http://127.0.0.1:88> aufrufen, mit der Adresse `http://127.0.0.1:8888` im Container verbunden werden und einen Bildschirm wie den folgenden sehen:

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Öffnen Sie ein Terminal auf dem Hostsystem und führen Sie den Befehl `ssh remote@127.0.0.1` aus, um sich remote beim Ubuntu-System im Container als remote-Konto anzumelden.  
Bei der ersten Anmeldung erhalten Sie eine Warnung, dass keine Informationen über den Schlüssel des Verbindungsziels vorliegen und eine Authentifizierung nicht möglich ist. Sie werden gefragt, ob Sie die Verbindung fortsetzen möchten. Geben Sie "yes" ein, um fortzufahren.  
Geben Sie dann das Passwort ein (wenn Sie es beim Erstellen des Images nicht geändert haben, sollte es der Standardwert "000000" sein).
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {Fingerabdruck (jeder Schlüssel hat einen einzigartigen Wert)}.
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
Wenn Sie eine ähnliche Ausgabe wie oben sehen, war die Remote-Anmeldung über SSH erfolgreich. Um die Verbindung zu beenden, geben Sie den Befehl `exit` ein.

### 6-3. (optional) Push auf Docker Hub
Um das erstellte Entwicklungsumgebungs-Image jederzeit bei Bedarf pullen und nutzen zu können, ist es ratsam, das erstellte Image auf Docker Hub zu pushen.  

> Um Ihr eigenes Image auf Docker Hub zu pushen, benötigen Sie ein Docker-Konto. Falls Sie noch keines haben, registrieren Sie sich zuerst unter <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Anmeldung bei Docker Hub
##### Für Podman
```bash
podman login docker.io
```

##### Für Docker
```bash
docker login
```

#### 6-3-2. Image-Tag setzen
Ersetzen Sie <dockerhub_username>, <repository_name> und (optional) :TAG durch Ihre entsprechenden Informationen.  
z.B. "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### Für Podman
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Für Docker
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Image pushen
Führen Sie abschließend den folgenden Befehl aus, um das Image auf Docker Hub zu pushen.

##### Für Podman
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Für Docker
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Sie können auf <https://hub.docker.com/> überprüfen, ob der Push erfolgreich war, wie unten gezeigt:  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

Das durch diesen Prozess erstellte Image wurde im öffentlichen Repository [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) auf Docker Hub veröffentlicht und kann von jedem frei genutzt werden.

Um das Image zu pullen, ändern Sie einfach den Teil `push` im zuvor verwendeten Push-Befehl in `pull`.
