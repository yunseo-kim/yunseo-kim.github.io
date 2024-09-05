---
title: "Aufbau einer Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und Docker (2) - Konfiguration der Container-Laufzeit für GPU-Nutzung, Erstellung von Dockerfile und Docker Image Build"
description: >-
  Diese Serie behandelt den Aufbau einer lokalen Deep-Learning-Entwicklungsumgebung basierend auf NVIDIA Container Toolkit und Docker sowie die Einrichtung von SSH und Jupyter Lab zur Nutzung als Remote-Server. Dieser Beitrag ist der zweite Teil der Serie und stellt die Methode zur Installation des NVIDIA Container Toolkit vor.
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
---

## Überblick
In dieser Serie behandeln wir die Installation von NVIDIA Container Toolkit und Docker sowie die Erstellung eines Dockerfiles basierend auf CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub, um eine Deep-Learning-Entwicklungsumgebung aufzubauen. Für diejenigen, die es benötigen, teile ich das [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und das [Image](https://hub.docker.com/r/yunseokim/dl-env/tags), die durch diesen Prozess erstellt wurden, über GitHub und Docker Hub, damit sie frei verwendet werden können. Zusätzlich biete ich eine Anleitung zur Einrichtung von SSH und Jupyter Lab für die Nutzung als Remote-Server.  
Die Serie wird aus drei Beiträgen bestehen, und dieser Beitrag, den Sie gerade lesen, ist der zweite Teil der Serie.
- [Teil 1: Installation von NVIDIA Container Toolkit & Docker Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Teil 2: Konfiguration der Container-Laufzeit für GPU-Nutzung, Erstellung von Dockerfile und Docker Image Build (dieser Beitrag)
- Teil 3 (geplant)

Wir gehen davon aus, dass Sie eine x86_64 Linux-Umgebung mit einer NVIDIA-Grafikkarte verwenden, die CUDA unterstützt. Einige Details können in anderen Distributionen als Ubuntu oder Fedora leicht abweichen, da ich sie nicht direkt getestet habe.

## Bevor wir beginnen
Dieser Beitrag ist eine Fortsetzung von [Teil 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1). Wenn Sie ihn noch nicht gelesen haben, empfehle ich, zuerst den vorherigen Beitrag zu lesen.

## 4. Konfiguration der Container-Laufzeit
### 4-1. Ausführen des `nvidia-ctk` Befehls
```bash
sudo nvidia-ctk runtime configure --runtime=docker
```
Dieser Befehl modifiziert die Datei `/etc/docker/daemon.json`{: .filepath}, damit Docker die NVIDIA Container Runtime nutzen kann.

### 4-2. Neustart des Docker-Daemons
Starten Sie den Docker-Daemon neu, um die geänderten Einstellungen zu übernehmen.
```bash
sudo systemctl restart docker
```

### 4-3. Überprüfung der korrekten Konfiguration
Führen Sie einen Beispiel-CUDA-Container aus.
```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Wenn eine Ausgabe ähnlich der folgenden erscheint, war die Konfiguration erfolgreich.

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
Wir erstellen ein Dockerfile für die Entwicklungsumgebung basierend auf CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub.

- Sie müssen das zu verwendende Image basierend auf den benötigten CUDA- und cuDNN-Versionen sowie der Art und Version der Linux-Distribution auswählen. 
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)Zum Zeitpunkt des Schreibens dieses Beitrags, Ende August 2024, unterstützt die neueste Version von PyTorch, Version 2.4.0, CUDA 12.4. Daher verwenden wir hier das [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) Image. Sie können die neueste Version von PyTorch und die unterstützte CUDA-Version auf der [PyTorch-Website](https://pytorch.org/get-started/locally/) überprüfen.

Der Quellcode des fertigen Dockerfiles ist im GitHub-Repository [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) öffentlich zugänglich. Im Folgenden wird der Prozess der Erstellung dieses Dockerfiles Schritt für Schritt erklärt.

### 5-1. Festlegung des Basis-Images
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Installation grundlegender Dienstprogramme und Python-Voraussetzungen
```Dockerfile
RUN apt-get update -y && apt-get install -y --no-install-recommends\
    apt-utils \
    ssh \
    curl \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*
```

### 5-3. Einstellung der Systemzeitzone (in diesem Beitrag verwenden wir 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. SSH-Server-Konfiguration für Fernzugriff  
Aus Sicherheitsgründen konfigurieren wir, dass der Root-Zugriff über SSH mit Passwort nicht möglich ist.
```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```
Wir konfigurieren, dass der SSH-Dienst beim Start des Containers automatisch gestartet wird.
```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```
Wir erstellen einen Nicht-Root-Benutzer namens 'remote' für SSH-Verbindungen.
```Dockerfile
# Create a non-root user and switch to it
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
RUN useradd --create-home --password $USER_PASSWORD $USER_NAME
ENV HOME=/home/$USER_NAME
USER $USER_NAME
WORKDIR $HOME
# Re-run ssh when the container restarts.
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
# Create a workspace directory to locate jupyter notebooks and .py files
RUN mkdir -p $HOME/workspace
```

> Wenn Sie dieses Dockerfile verwenden, um ein Docker-Image zu erstellen, ohne separate Optionen anzugeben, ist der anfängliche Kontopasswort für den Benutzer 'remote' 000000. Dies ist aus Sicherheitsgründen sehr anfällig, daher sollten Sie entweder die Option `--build-arg` beim Erstellen des Docker-Images verwenden, um ein separates Konto-Login-Passwort anzugeben, oder die Einstellungen sofort nach der ersten Ausführung des Containers ändern. Aus Sicherheitsgründen ist es ratsam, die Passwort-Anmeldung für SSH-Verbindungen zu deaktivieren und nur Anmeldungen über separate Schlüsseldateien zuzulassen. Idealerweise sollte auch ein Hardware-Schlüssel wie Yubikey verwendet werden.
> Die SSH-Server-Konfiguration wird im nächsten Teil dieser Serie etwas ausführlicher behandelt. Wenn Sie mehr darüber erfahren möchten, können Sie die folgenden Dokumente konsultieren:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Installation von setuptools, pip und Registrierung der PATH-Umgebungsvariable
```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. Installation von Machine Learning- und Deep Learning-Paketen für die Entwicklungsumgebung
```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
Wenn Sie Cupy, cuDF, cuML und DALI verwenden möchten, fügen Sie auch Folgendes zum Dockerfile hinzu:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Konfiguration zum Starten von JupyterLab beim Container-Start
```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
```

## 6. Docker Image Build und Container-Ausführung
### 6-1. Image Build
Öffnen Sie ein Terminal im Verzeichnis, in dem sich das Dockerfile befindet, und führen Sie den folgenden Befehl aus:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Ersetzen Sie \<password\> durch das Login-Passwort, das Sie für SSH-Verbindungen verwenden möchten.
{: .prompt-info }

### 6-2. Ausführung einer Beispiel-Workload
Nach Abschluss des Builds führen Sie den folgenden Befehl aus, um einen Einweg-Container zu starten und zu überprüfen, ob alles ordnungsgemäß funktioniert:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```
Wenn Sie diesen Befehl im Terminal eingeben, wird ein Container namens `test-container` aus dem zuvor erstellten Image `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` gestartet und der Port 88 des Host-Systems mit dem Port 8888 dieses Containers verbunden. Wenn das Docker-Image im vorherigen Schritt erfolgreich erstellt wurde und der Container problemlos gestartet wurde, sollte JupyterLab innerhalb des `test-container` Containers unter der Standardadresse `http:127.0.0.1:8888` laufen. Daher sollten Sie, wenn Sie einen Browser auf dem Host-System öffnen, auf dem die Docker Engine läuft, und <http://127.0.0.1:88> aufrufen, mit der internen Adresse `http://127.0.0.1:8888` des Containers verbunden werden und einen Bildschirm wie den folgenden sehen:

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (optional) Push auf Docker Hub
Um das erstellte Entwicklungsumgebungs-Image jederzeit bei Bedarf pullen und nutzen zu können, ist es ratsam, das gebaute Image auf Docker Hub zu pushen.  

> Um Ihr eigenes Image auf Docker Hub zu pushen, benötigen Sie ein Docker-Konto. Falls Sie noch keines haben, registrieren Sie sich zuerst unter <https://app.docker.com/signup>.
{: .prompt-tip }

Melden Sie sich zunächst mit folgendem Befehl bei Docker Hub an:
```bash
docker login
```
Erstellen Sie nun einen Image-Tag mit einem Befehl in folgendem Format:
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```
Führen Sie schließlich den folgenden Befehl aus, um das Image auf Docker Hub zu pushen:
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Sie können auf <https://hub.docker.com/> überprüfen, ob der Push erfolgreich war, wie unten gezeigt:  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

Das durch diesen Prozess erstellte Image ist im öffentlichen Repository [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) auf Docker Hub verfügbar und kann von jedem frei genutzt werden.
