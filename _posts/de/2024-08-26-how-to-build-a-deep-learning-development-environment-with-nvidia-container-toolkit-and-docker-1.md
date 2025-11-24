---
title: NVIDIA Container Toolkit und Docker/Podman zur Einrichtung einer Deep-Learning-Entwicklungsumgebung (1) - Installation von NVIDIA Container Toolkit & Container-Engine
description: Diese Serie behandelt die Einrichtung einer containerisierten Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und die Konfiguration von SSH und Jupyter Lab für die Nutzung als Remote-Server. Dieser Beitrag ist der erste Teil der Serie und stellt die Installation des NVIDIA Container Toolkit und der Container-Engine vor.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---
## Übersicht
In dieser Serie behandeln wir die Installation von NVIDIA Container Toolkit und Docker oder Podman, sowie die Erstellung einer Dockerfile basierend auf CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub, um eine Deep-Learning-Entwicklungsumgebung aufzubauen. Für alle, die diese Umgebung nutzen möchten, stelle ich die fertige [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und [Images](https://hub.docker.com/r/yunseokim/dl-env/tags) über GitHub und Docker Hub zur Verfügung. Zusätzlich biete ich eine Anleitung zur Konfiguration von SSH und Jupyter Lab für die Nutzung als Remote-Server.  
Die Serie wird aus drei Artikeln bestehen, und dieser Artikel ist der erste Teil.
- Teil 1: Installation von NVIDIA Container Toolkit & Container-Engine (dieser Artikel)
- [Teil 2: Container-Runtime-Konfiguration für GPU-Nutzung, Dockerfile-Erstellung und Container-Image-Build](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Teil 3 (geplant)

Ich gehe davon aus, dass Sie eine x86_64 Linux-Umgebung mit einer CUDA-fähigen NVIDIA-Grafikkarte verwenden. Obwohl ich die Anleitung nicht auf allen Distributionen außer Ubuntu und Fedora getestet habe, könnten einige Details leicht abweichen.  
(Aktualisiert am 18.02.12025)

### Umgebungskonfiguration
- Host-Betriebssystem und Architektur: x86_64, Linux-Umgebung (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x usw.)
- Aufzubauender Technologie-Stack (Sprachen und Bibliotheken)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE / Podman
  - CUDA 12.4
  - cuDNN
  - OpenSSH
  - tmux
  - JupyterLab
  - NumPy & SciPy
  - CuPy (optional, NumPy/SciPy-kompatible Array-Bibliothek für GPU-beschleunigtes Computing mit Python)
  - pandas
  - cuDF (optional, zur Beschleunigung von pandas mit GPU-Unterstützung ohne Codeänderungen)
  - Matplotlib & Seaborn
  - DALI (optional, leistungsstarke Alternative zu eingebauten Datenladern und Dateniteratoren mit GPU-Unterstützung)
  - scikit-learn
  - cuML (optional, zur Ausführung von Machine-Learning-Algorithmen auf GPUs mit einer API, die der scikit-learn API ähnelt)
  - PyTorch
  - tqdm

  > Je nach Situation und persönlicher Präferenz könnte man auch die [Polars](https://pola.rs/) DataFrame-Bibliothek anstelle von pandas in Betracht ziehen. Sie ist in Rust geschrieben und [zeigt bei der Verarbeitung großer Datenmengen zwar nicht die Leistung der cuDF + pandas-Kombination, übertrifft aber das reine pandas-Paket deutlich](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/) und bietet eine stärker auf Abfragen spezialisierte Syntax. Laut [offiziellem Polars-Blog](https://pola.rs/posts/polars-on-gpu/) arbeitet das Team mit NVIDIA RAPIDS zusammen, um in naher Zukunft auch die Integration mit cuDF zu unterstützen.
  {: .prompt-tip }

  > Wenn Sie zwischen Docker CE und Podman schwanken, könnte die [unten aufgeführte Vergleichstabelle](#3-installation-der-container-engine) hilfreich sein.
  {: .prompt-tip }

### Vergleichstabelle mit dem früheren Leitfaden zur Einrichtung einer Machine-Learning-Entwicklungsumgebung
Es gibt bereits einen [früheren Leitfaden zur Einrichtung einer Machine-Learning-Entwicklungsumgebung](/posts/Setting-up-a-Machine-Learning-Development-Environment) in diesem Blog, der größtenteils noch gültig ist. Aufgrund einiger Änderungen habe ich jedoch diesen neuen Beitrag verfasst. Die Unterschiede sind in der folgenden Tabelle zusammengefasst.

| Unterschied | Früherer Artikel (Version 12021) | Dieser Artikel (Version 12024) |
| --- | --- | --- |
| Linux-Distribution | Basierend auf Ubuntu | Anwendbar auf Ubuntu, Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES usw. |
| Methode zur Einrichtung der Entwicklungsumgebung | Python-Virtualenv mit venv | Containerbasierte Umgebung mit<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Installation des NVIDIA-Grafiktreibers | Ja | Ja |
| Direkte Installation von CUDA und cuDNN<br> auf dem Host-System | Ja (mit Apt-Paketmanager) | Nein (Verwendung von vorinstallierten Images<br> aus dem [Docker Hub von NVIDIA](https://hub.docker.com/r/nvidia/cuda),<br> keine direkte Installation erforderlich) |
| Portabilität | Bei jedem Systemwechsel muss die<br> Entwicklungsumgebung neu eingerichtet werden | Docker-basiert, daher einfache Portierung durch<br> Erstellung neuer Images mit der vorhandenen<br> Dockerfile oder Verwendung bestehender Images<br> (ohne zusätzliche Volumes oder Netzwerkeinstellungen) |
| Nutzung zusätzlicher GPU-<br>Beschleunigungsbibliotheken<br> neben cuDNN | Nein | Einführung von [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/),<br> [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook-Oberfläche | Jupyter Notebook (klassisch) | JupyterLab (Next-Generation) |
| SSH-Server-Konfiguration | Nicht behandelt | Grundlegende SSH-Server-Konfiguration<br> in Teil 3 enthalten |

Wenn Sie lieber eine Python-Virtualenv wie venv anstelle von Docker verwenden möchten, ist der [frühere Artikel](/posts/Setting-up-a-Machine-Learning-Development-Environment) nach wie vor gültig und kann als Referenz dienen.

## 0. Voraussetzungen
- [NVIDIA Container Toolkit ist auf Linux-Distributionen verfügbar, die Apt, Yum oder Dnf, Zypper Paketmanager unterstützen.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Auf der verlinkten Seite finden Sie eine Liste der unterstützten Linux-Distributionen. Obwohl Fedora nicht explizit in der offiziellen Unterstützungstabelle aufgeführt ist, funktioniert es problemlos, da es auf Red Hat Linux basiert. Wenn Sie mit Linux nicht vertraut sind und nicht wissen, welche Distribution Sie verwenden sollten, ist Ubuntu LTS eine gute Wahl. Es installiert automatisch proprietäre Treiber, was es für Anfänger relativ benutzerfreundlich macht, und die meisten technischen Dokumente sind für Ubuntu geschrieben, da es viele Benutzer hat.
  - Sie können Ihre Systemarchitektur und Linux-Distribution mit dem Befehl `uname -m && cat /etc/*release` im Terminal überprüfen.
- Stellen Sie sicher, dass Ihre Grafikkarte die CUDA- und cuDNN-Version unterstützt, die Sie verwenden möchten.
  - Den Namen Ihres GPU-Modells können Sie mit dem Befehl `lspci | grep -i nvidia` im Terminal überprüfen.
  - Auf <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> finden Sie die **unterstützten NVIDIA-Grafiktreiberversionen**, die erforderliche **CUDA Compute Capability** und die Liste der **unterstützten NVIDIA-Hardware** für jede cuDNN-Version.
  - Suchen Sie Ihr Modell in der GPU-Liste auf <https://developer.nvidia.com/cuda-gpus> und überprüfen Sie die **Compute Capability**. Dieser Wert muss die zuvor überprüfte **CUDA Compute Capability**-Anforderung erfüllen, um CUDA und cuDNN problemlos nutzen zu können.

> Wenn Sie eine neue Grafikkarte für Deep-Learning-Aufgaben kaufen möchten, sind die Auswahlkriterien im folgenden Artikel gut zusammengefasst. Der Autor aktualisiert den Artikel regelmäßig.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> Der Artikel [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) vom selben Autor ist ebenfalls sehr informativ.
{: .prompt-tip }

Wenn Sie alle oben genannten Anforderungen erfüllen, können wir mit der Einrichtung der Arbeitsumgebung beginnen.

## 1. Installation des NVIDIA-Grafiktreibers
Zunächst müssen Sie den NVIDIA-Grafiktreiber auf Ihrem Host-System installieren. Sie können den .run-Installer von der [NVIDIA-Treiberdownloadseite](https://www.nvidia.com/drivers/) herunterladen, aber es ist besser, den Paketmanager Ihres Systems zu verwenden, da dies die Versionsverwaltung und Wartung erleichtert. Folgen Sie der [offiziellen Dokumentation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation), um den für Ihre Systemumgebung geeigneten Grafiktreiber zu installieren.

### Proprietäres Modul vs. Open-Source-Modul
Der NVIDIA-Linux-Treiber besteht aus mehreren Kernelmodulen. Ab Treiberversion 515 bietet NVIDIA zwei Arten von Treiber-Kernelmodulen an:

- Proprietär: Der traditionelle proprietäre Softwaretreiber von NVIDIA.
- Open-Source: Ein Open-Source-Treiber unter MIT/GPLv2-Doppellizenz. Der Quellcode ist unter <https://github.com/NVIDIA/open-gpu-kernel-modules> verfügbar.

Der proprietäre Treiber wird für GPUs von der Maxwell-Architektur bis vor Blackwell angeboten und wird ab der Blackwell-Architektur nicht mehr unterstützt.
Der Open-Source-Treiber unterstützt dagegen die Turing-Architektur und neuere.

[NVIDIA empfiehlt die Verwendung des Open-Source-Kernelmoduls, wenn möglich.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
Sie können [hier](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus) überprüfen, ob Ihre GPU mit dem Open-Source-Treiber kompatibel ist.

In diesem Artikel gehen wir davon aus, dass wir den Open-Source-Treiber installieren.

### Debian & Ubuntu
Für Ubuntu oder Debian geben Sie die folgenden Befehle im Terminal ein:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Für Fedora 40 stellen wir die Installation über vorgefertigte Pakete von [RPM Fusion](https://rpmfusion.org/RPM%20Fusion) vor.

#### 1-Fedora-1. Konfiguration des RPM Fusion-Repositorys  
Folgen Sie dem [offiziellen RPM Fusion-Leitfaden](https://rpmfusion.org/Configuration).  
Führen Sie den folgenden Befehl im Terminal aus:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Installation des akmod-nvidia-open-Pakets  
Folgen Sie dem [NVIDIA-Treiberinstallationsleitfaden von RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open),
aktivieren Sie das rpmfusion-nonfree-tainted-Repository und installieren Sie dann das akmod-nvidia-open-Paket:
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark user akmod-nvidia-open
```

> In älteren DNF-Versionen (Fedora 40 und früher) lautete die Befehlszeile in der letzten Zeile, um zu verhindern, dass der NVIDIA-Treiber bei `autoremove` entfernt wird, wie folgt:
>
> ```bash
> sudo dnf mark install akmod-nvidia-open
> ```
>
> Ab DNF 5 (Fedora 41+) muss stattdessen der folgende Befehl verwendet werden:
>
> ```bash
> sudo dnf mark user akmod-nvidia-open
> ```
>
> Dies wurde im obigen Text bereits entsprechend aktualisiert.
{: .prompt-tip }

#### 1-Fedora-3. Schlüsselregistrierung für korrektes Laden des Treibers bei aktiviertem Secure Boot  

> Mit dem unten beschriebenen zusätzlichen Verfahren können Sie den NVIDIA-Grafiktreiber normal verwenden, während Secure Boot aktiviert bleibt. Es wird dringend empfohlen, Secure Boot nicht zu deaktivieren, da dies die Sicherheit Ihres Systems erheblich beeinträchtigen würde. Zumindest seit den 12020er Jahren gibt es kaum noch Gründe, Secure Boot zu deaktivieren.
{: .prompt-danger }

Installieren Sie zunächst die folgenden Tools:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Führen Sie dann den folgenden Befehl aus, um einen Schlüssel zu generieren:
```bash
sudo kmodgenca -a
```
Jetzt müssen Sie den generierten Schlüssel im MOK (Machine Owner Key) der UEFI-Firmware registrieren:
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Bei der Ausführung dieses Befehls werden Sie aufgefordert, ein Passwort für die Schlüsselregistrierung einzugeben. Dies ist ein Einmalpasswort, das Sie bei einem bevorstehenden Neustart zur Abschließung des Registrierungsvorgangs benötigen werden.

Starten Sie nun das System neu:
```bash
systemctl reboot
```
Während des Bootvorgangs wird automatisch der MOK-Manager angezeigt. Wählen Sie "Enroll MOK", dann "Continue" und "Yes". Sie werden nach dem zuvor festgelegten Passwort gefragt. Nach Eingabe des Passworts ist die Schlüsselregistrierung abgeschlossen. Geben Sie "reboot" ein, um neu zu starten, und der NVIDIA-Treiber sollte normal geladen werden.

### Überprüfung der NVIDIA-Treiberinstallation
Führen Sie den folgenden Befehl im Terminal aus, um das aktuell geladene NVIDIA-Kernelmodul zu überprüfen:
```bash
cat /proc/driver/nvidia/version
```
Wenn eine Ausgabe ähnlich der folgenden erscheint, wurde der Treiber erfolgreich installiert:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Installation des NVIDIA Container Toolkit
Jetzt müssen wir das [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) installieren. Folgen Sie dem [offiziellen Installationsleitfaden für NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), aber beachten Sie bei Fedora die Hinweise am Ende dieses Abschnitts.

### Für Apt-Benutzer (Ubuntu, Debian usw.)
#### 2-Apt-1. Repository-Konfiguration für Paketdownloads
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Aktualisierung der Paketliste
```bash
sudo apt update
```

#### 2-Apt-3. Paketinstallation
```bash
sudo apt install nvidia-container-toolkit
```

### Für Yum- oder Dnf-Benutzer (Fedora, RHEL, Centos usw.)
> Bei Tests mit Fedora 40 stellte ich fest, dass im Gegensatz zu Ubuntu der Befehl `nvidia-smi` und das Paket `nvidia-persistenced` nicht standardmäßig im NVIDIA-Grafiktreiber enthalten waren, sodass das Paket `xorg-x11-drv-nvidia-cuda` zusätzlich installiert werden musste. Ich habe RHEL und Centos nicht direkt getestet, aber da sie Fedora sehr ähnlich sind, könnte dieser Ansatz auch dort hilfreich sein, falls Probleme auftreten.
{: .prompt-warning }

> Bei Tests auf Fedora 40 mit der Installation von `xorg-x11-drv-nvidia-cuda` wie beschrieben funktionierte die Testarbeitsbelastung auf meinem System normal. Falls aufgrund von SELinux oder anderen Gründen weiterhin Probleme auftreten, könnte das [Fedora-spezifische nvidia-container-toolkit-Paket und der Leitfaden](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) der Fedora AI-ML-Gruppe hilfreich sein.
{: .prompt-tip }

#### 2-Dnf-1. Repository-Konfiguration für Paketdownloads
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Paketinstallation
```bash
sudo dnf install nvidia-container-toolkit
```
oder
```bash
sudo yum install nvidia-container-toolkit
```

### Für Zypper-Benutzer (openSUSE, SLES)
#### 2-Zypper-1. Repository-Konfiguration für Paketdownloads
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Paketinstallation
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installation der Container-Engine
Als Nächstes installieren wir Docker CE oder Podman als Container-Engine. Wählen Sie je nach Umgebung und Präferenz eine der beiden Optionen und folgen Sie der [offiziellen Docker-Dokumentation](https://docs.docker.com/engine/install/) oder der [offiziellen Podman-Dokumentation](https://podman.io/docs/installation).

Die folgende Tabelle fasst die wichtigsten Unterschiede und Vor- und Nachteile von Docker und Podman zusammen:

| Vergleichskriterium | Docker | Podman |
| --- | --- | --- |
| Architektur | Client-Server-Modell, Daemon-basiert | Daemonless-Struktur |
| Sicherheit | Potenzielles Sicherheitsrisiko durch<br> Abhängigkeit von einem Daemon mit Root-Rechten<br>(Rootless-Modus ab Version 20.10 von 12020<br> verfügbar, erfordert aber zusätzliche Konfiguration) | Keine Abhängigkeit von einem Daemon,<br> standardmäßig rootless, durch SELinux geschützt |
| Ressourcenverbrauch | Höherer Ressourcenverbrauch durch<br> ständig laufende Hintergrundprozesse | Generell geringerer Overhead |
| Container-Startzeit | Relativ langsam | Bis zu 50% schneller durch<br> vereinfachte Architektur |
| Ökosystem und Dokumentation | Umfangreiches Ökosystem und<br> Community-Unterstützung, reichhaltige Dokumentation | Vergleichsweise kleineres Ökosystem<br> und weniger Dokumentation |
| Netzwerk | Verwendet Docker Bridge Network | Verwendet CNI (Container Network Interface)<br> Plugins |
| Native Unterstützung für<br> Kubernetes YAML | Nein (Konvertierung erforderlich) | Ja |

Quellen:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker hat eine längere Geschichte und gilt als De-facto-Standard in der Branche, was zu einem umfangreichen Ökosystem und reichhaltiger Dokumentation geführt hat - sein größter Vorteil.  
Podman wurde relativ kürzlich von Red Hat entwickelt und verfolgt von Grund auf einen daemonlosen, rootlosen Ansatz, was Vorteile in Bezug auf Sicherheit, Systemressourcenverbrauch und Container-Startzeit bietet. Ein weiterer Vorteil von Podman ist, dass Container vollständig unabhängig sind - wenn bei Docker der Daemon abstürzt, stürzen alle Container ab, während bei Podman der Absturz eines Containers keine Auswirkungen auf andere hat.

Die Wahl des richtigen Tools hängt von Ihren spezifischen Anforderungen ab. Für Einsteiger könnte Podman eine gute Wahl sein. Obwohl das Ökosystem im Vergleich zu Docker kleiner ist, wächst es aufgrund der genannten Vorteile schnell. Podman ist in vielen Bereichen mit Docker kompatibel, einschließlich Dockerfile-Syntax, Docker-Images und CLI, was für Einzelpersonen oder kleine Gruppen kein großes Problem darstellen sollte.

### Podman
Podman ist in den Standard-Repositories der meisten großen Linux-Distributionen verfügbar und kann einfach installiert werden.

#### Für Ubuntu
```bash
sudo apt install podman
```

#### Für Fedora
```bash
sudo dnf install podman
```

#### Für openSUSE
```bash
sudo zypper install podman
```

### Docker CE
#### Für Ubuntu
##### 3-Ubuntu-1. Entfernung älterer oder inoffizieller Pakete zur Vermeidung von Konflikten
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Repository-Konfiguration
```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```

##### 3-Ubuntu-3. Paketinstallation
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Erstellung der Docker-Gruppe und Hinzufügen von Benutzern
Damit auch Nicht-Root-Benutzer Docker ohne `sudo` verwenden können, erstellen Sie eine `Docker`-Gruppe und fügen Sie die entsprechenden Benutzer hinzu:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Melden Sie sich ab und wieder an, damit die Änderungen wirksam werden. Bei Ubuntu oder Debian startet der Docker-Dienst automatisch beim Systemstart.

#### Für Fedora
##### 3-Fedora-1. Entfernung älterer oder inoffizieller Pakete zur Vermeidung von Konflikten
```bash
sudo dnf remove docker \
                docker-client \
                docker-client-latest \
                docker-common \
                docker-latest \
                docker-latest-logrotate \
                docker-logrotate \
                docker-selinux \
                docker-engine-selinux \
                docker-engine
```

##### 3-Fedora-2. Repository-Konfiguration
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Paketinstallation
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Während der Installation werden Sie gefragt, ob Sie den GPG-Schlüssel akzeptieren möchten. Wenn der GPG-Schlüssel mit `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35` übereinstimmt, geben Sie y ein, um zu bestätigen.  
> Falls der GPG-Schlüssel nicht übereinstimmt, könnte es sich um ein gefälschtes Paket durch einen Supply-Chain-Angriff handeln. In diesem Fall sollten Sie die Installation abbrechen.
{: .prompt-danger }

##### 3-Fedora-4. Starten des Docker-Daemons
Docker ist jetzt installiert, aber noch nicht gestartet. Starten Sie Docker mit:
```bash
sudo systemctl start docker
```
Um Docker beim Systemstart automatisch zu starten, führen Sie aus:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Hinzufügen von Benutzern zur Docker-Gruppe
Damit Nicht-Root-Benutzer Docker verwalten können, fügen Sie sie der Docker-Gruppe hinzu. Bei Fedora wird die Docker-Gruppe während der Paketinstallation automatisch erstellt:
```bash
sudo usermod -aG docker $USER
```
Melden Sie sich ab und wieder an, damit die Änderungen wirksam werden.

#### Überprüfung der korrekten Einrichtung
Führen Sie im Terminal den folgenden Befehl aus:
```bash
docker run hello-world
```
Wenn eine Ausgabe wie die folgende erscheint, war die Installation erfolgreich:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
