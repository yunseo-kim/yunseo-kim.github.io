---
title: "Aufbau einer Deep Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und Docker (1) - Installation von NVIDIA Container Toolkit & Docker Engine"
description: >-
  Diese Serie behandelt den Aufbau einer lokalen Deep Learning-Entwicklungsumgebung basierend auf NVIDIA Container Toolkit und Docker sowie die Konfiguration von SSH und Jupyter Lab zur Nutzung als Remote-Server. Dieser Beitrag ist der erste Teil der Serie und stellt die Installationsmethode für das NVIDIA Container Toolkit vor.
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
---

## Überblick
In dieser Serie behandeln wir die Installation von NVIDIA Container Toolkit und Docker sowie die Erstellung eines Dockerfiles basierend auf CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub, um eine Deep Learning-Entwicklungsumgebung aufzubauen. Für diejenigen, die es benötigen, teile ich das [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und [Image](https://hub.docker.com/r/yunseokim/dl-env/tags), die durch diesen Prozess erstellt wurden, über GitHub und Docker Hub, damit sie frei verwendet werden können. Zusätzlich biete ich eine Anleitung zur Konfiguration von SSH und Jupyter Lab für die Nutzung als Remote-Server.  
Die Serie wird aus drei Beiträgen bestehen, und dieser Beitrag, den Sie gerade lesen, ist der erste Teil der Serie.
- Teil 1: Installation von NVIDIA Container Toolkit & Docker Engine (dieser Beitrag)
- [Teil 2: Konfiguration der Container-Laufzeit für GPU-Nutzung, Erstellung des Dockerfiles und Erstellung des Docker-Images](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Teil 3 (geplant)

Wir gehen davon aus, dass Sie ein System mit einer NVIDIA-Grafikkarte haben, die CUDA in einer x86_64 Linux-Umgebung unterstützt. Einige Details können in anderen Distributionen als Ubuntu oder Fedora leicht abweichen, da ich sie nicht direkt getestet habe.

### Konfiguration der Entwicklungsumgebung
- Host-Betriebssystem und Architektur: x86_64, Linux-Umgebung (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x usw.)
- Aufzubauender Technologie-Stack (Sprachen und Bibliotheken)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE
  - CUDA 12.4
  - cuDNN
  - JupyterLab
  - NumPy & SciPy
  - CuPy (optional, NumPy/SciPy-kompatible Array-Bibliothek für GPU-beschleunigtes Computing mit Python)
  - pandas
  - cuDF (optional, zur Beschleunigung von pandas ohne Codeänderungen mit dem GPU-Beschleuniger)
  - Matplotlib & Seaborn
  - DALI (optional, leistungsstarke Alternative zu eingebauten Datenladern und Dateniteratoren mit GPU)
  - scikit-learn
  - cuML (optional, zur Ausführung von Machine Learning-Algorithmen auf GPUs mit einer API, die der scikit-learn API sehr ähnlich ist)
  - PyTorch
  - OpenSSH
  - tqdm

  > Je nach Situation und persönlicher Präferenz könnte man auch in Betracht ziehen, die [Polars](https://pola.rs/) DataFrame-Bibliothek anstelle von pandas zu verwenden. Sie ist in Rust geschrieben und [zeigt bei der Verarbeitung großer Datenmengen eine beeindruckende Leistung im Vergleich zum reinen pandas-Paket, auch wenn sie der Kombination aus cuDF + pandas unterlegen ist](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/). Sie bietet auch eine eher auf Abfragen spezialisierte Syntax. Laut dem [offiziellen Polars-Blog](https://pola.rs/posts/polars-on-gpu/) plant das Team in Zusammenarbeit mit dem NVIDIA RAPIDS-Team, in naher Zukunft auch die Integration mit cuDF zu unterstützen.
  {: .prompt-tip }

### Vergleichstabelle mit dem zuvor erstellten Leitfaden zur Einrichtung einer Machine Learning-Entwicklungsumgebung
Es gibt bereits einen [zuvor in diesem Blog veröffentlichten Leitfaden zur Einrichtung einer Machine Learning-Entwicklungsumgebung](/posts/Setting-up-a-Machine-Learning-Development-Environment), der größtenteils noch gültig ist. Aufgrund einiger Änderungen habe ich jedoch diesen neuen Beitrag verfasst. Die Unterschiede sind in der folgenden Tabelle zusammengefasst.

| Unterschied | Vorheriger Beitrag (Version 2021) | Dieser Beitrag (Version 2024) |
| --- | --- | --- |
| Linux-Distribution | Basierend auf Ubuntu | Anwendbar auf Ubuntu, Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES usw. |
| Methode zum Aufbau der Entwicklungsumgebung | Python-Virtuelle Umgebung mit venv | Docker-Container-basierte Umgebung mit<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Installation des NVIDIA-Grafiktreibers | Ja | Ja |
| Direkte Installation von CUDA und cuDNN<br> auf dem Hostsystem | Ja (mit Apt-Paketmanager) | Nein (Verwendung von vorinstallierten Images<br> von NVIDIA auf Docker Hub, keine direkte Arbeit erforderlich) |
| Portabilität | Entwicklungsumgebung muss bei jedem<br> Systemwechsel neu aufgebaut werden | Docker-basiert, einfache Portierung durch Erstellung<br> neuer Images mit dem erstellten Dockerfile oder<br> Verwendung bestehender Images (außer zusätzlicher<br> Volumes oder Netzwerkeinstellungen) |
| Nutzung zusätzlicher GPU-<br>Beschleunigungsbibliotheken neben cuDNN | Nein | Einführung von [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook-Oberfläche | Jupyter Notebook (klassisch) | JupyterLab (Next-Generation) |
| SSH-Server-Konfiguration | Nicht behandelt | Grundlegende SSH-Server-Konfiguration in Teil 3 enthalten |

Wenn Sie eine Python-virtuelle Umgebung wie venv anstelle von Docker verwenden möchten, ist der [vorherige Beitrag](/posts/Setting-up-a-Machine-Learning-Development-Environment) immer noch gültig und kann als Referenz dienen.

## 0. Voraussetzungen
- [NVIDIA Container Toolkit ist in Linux-Distributionen verfügbar, die die Paketmanager Apt, Yum oder Dnf, Zypper unterstützen.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Auf der verlinkten Seite finden Sie eine Liste der unterstützten Linux-Distributionen. Obwohl es nicht explizit in der offiziellen Unterstützungstabelle aufgeführt ist, funktioniert Fedora ebenfalls problemlos, da es auf Red Hat Linux basiert. Wenn Sie mit Linux nicht vertraut sind und nicht wissen, welche Distribution Sie verwenden sollten, ist die Ubuntu LTS-Version am unkompliziertesten. Proprietäre Treiber werden automatisch installiert, was es für Anfänger relativ einfach zu bedienen macht, und aufgrund der großen Benutzerbasis sind die meisten technischen Dokumente für Ubuntu geschrieben.
  - Sie können die Architektur und Version Ihrer Linux-Distribution im Terminal mit dem Befehl `uname -m && cat /etc/*release` überprüfen.
- Überprüfen Sie zunächst, ob die in Ihrem System installierte Grafikkarte die CUDA- und cuDNN-Version unterstützt, die Sie verwenden möchten.
  - Sie können den Namen des in Ihrem Computer installierten GPU-Modells im Terminal mit dem Befehl `lspci | grep -i nvidia` überprüfen.
  - Auf der Seite <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> finden Sie für jede cuDNN-Version die **unterstützten NVIDIA-Grafiktreiberversionen**, die erforderliche **CUDA Compute Capability** und eine Liste der **unterstützten NVIDIA-Hardware**.
  - Suchen Sie auf <https://developer.nvidia.com/cuda-gpus> nach dem entsprechenden Modellnamen und überprüfen Sie den **Compute Capability**-Wert. Dieser Wert muss die zuvor überprüfte **CUDA Compute Capability**-Anforderung erfüllen, um CUDA und cuDNN problemlos nutzen zu können.

> Wenn Sie planen, eine neue Grafikkarte für Deep Learning-Aufgaben zu kaufen, sind die GPU-Auswahlkriterien in folgendem Artikel gut zusammengefasst. Der Autor aktualisiert den Artikel kontinuierlich.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> Ein weiterer sehr informativer Artikel desselben Autors ist [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/).
{: .prompt-tip }

Wenn Sie alle oben genannten Anforderungen erfüllen, können wir mit dem Aufbau der Arbeitsumgebung beginnen.

## 1. Installation des NVIDIA-Grafiktreibers
Zunächst müssen wir den NVIDIA-Grafiktreiber auf dem Hostsystem installieren. Sie können den .run-Installer von der [NVIDIA-Treiberdownloadseite](https://www.nvidia.com/drivers/) herunterladen und verwenden, aber es ist aus Gründen der Versionsverwaltung und Wartung besser, den Paketmanager Ihres Systems zu nutzen. Beziehen Sie sich auf die offizielle Dokumentation <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>, um den für Ihre Systemumgebung geeigneten Grafiktreiber zu installieren.

### Proprietäres Modul vs Open-Source-Modul
Der NVIDIA Linux-Treiber besteht aus mehreren Kernelmodulen, und ab Treiberversion 515 und späteren Versionen bietet NVIDIA zwei Arten von Treiber-Kernelmodulen an.

- Proprietär: Der exklusive Softwaretreiber, den NVIDIA bisher angeboten hat.
- Open-Source: Ein Open-Source-Treiber, der unter der MIT/GPLv2-Doppellizenz bereitgestellt wird. Der Quellcode ist über <https://github.com/NVIDIA/open-gpu-kernel-modules> verfügbar.

Der proprietäre Treiber wird für GPUs bereitgestellt, die auf Architekturen von Maxwell bis vor Blackwell basieren, und wird ab der Blackwell-Architektur eingestellt.
Der Open-Source-Treiber hingegen unterstützt Turing und spätere Architekturen.

[NVIDIA empfiehlt die Verwendung des Open-Source-Kernelmoduls, wenn möglich.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
Sie können [hier](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus) überprüfen, ob Ihre GPU mit dem Open-Source-Treiber kompatibel ist.

In diesem Artikel gehen wir davon aus, dass wir den Open-Source-Treiber installieren.

### Debian & Ubuntu
Für Ubuntu oder Debian geben Sie die folgenden Befehle im Terminal ein, um den Treiber zu installieren:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Basierend auf Fedora 40 stellen wir eine Methode vor, um das vorkompilierte Paket von [RPM Fusion](https://rpmfusion.org/RPM%20Fusion) herunterzuladen und zu installieren.

#### 1-Fedora-1. Konfiguration des RPM Fusion-Repositorys  
Wir folgen dem [offiziellen RPM Fusion-Leitfaden](https://rpmfusion.org/Configuration).  
Führen Sie den folgenden Befehl im Terminal aus:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Installation des akmod-nvidia-open-Pakets  
Unter Bezugnahme auf den [NVIDIA-Treiberinstallationsleitfaden von RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), 
aktivieren Sie das rpmfusion-nonfree-tainted-Repository und installieren Sie dann das akmod-nvidia-open-Paket.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Registrierung des Schlüssels für das korrekte Laden des Treibers bei aktiviertem Secure Boot  

> Mit dem unten beschriebenen zusätzlichen Verfahren können Sie den NVIDIA-Grafiktreiber normal verwenden, während Secure Boot aktiviert bleibt. Es wird empfohlen, Secure Boot nicht zu deaktivieren, da dies die Sicherheit des Systems erheblich beeinträchtigen würde. Zumindest seit Beginn der 2020er Jahre gibt es kaum noch Gründe, Secure Boot zu deaktivieren.
{: .prompt-danger }

Installieren Sie zunächst die folgenden Tools:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Führen Sie dann den folgenden Befehl aus, um einen Schlüssel zu generieren:
```bash
sudo kmodgenca -a
```
Jetzt müssen wir den generierten Schlüssel im MOK der UEFI-Firmware registrieren.
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Wenn Sie diesen Befehl ausführen, werden Sie aufgefordert, ein Passwort für die Schlüsselregistrierung einzugeben. Wir werden in Kürze neu starten, um den Schlüsselregistrierungsprozess abzuschließen, also geben Sie ein Einmalpasswort ein, das Sie sich merken können.

Führen Sie nun den folgenden Befehl aus, um das System neu zu starten:
```bash
systemctl reboot
```
Während des Systemstarts wird automatisch das MOK-Verwaltungsfenster angezeigt. Wählen Sie "Enroll MOK", dann nacheinander "Continue" und "Yes". Es erscheint ein Fenster, das das zuvor eingerichtete Passwort abfragt. Geben Sie das Passwort ein, das Sie vorhin festgelegt haben, und der Schlüsselregistrierungsprozess ist abgeschlossen. Geben Sie nun reboot ein, um erneut neu zu starten, und der NVIDIA-Treiber sollte normal geladen werden.

### Überprüfung der NVIDIA-Treiberinstallation
Sie können das aktuell geladene NVIDIA-Kernelmodul überprüfen, indem Sie den folgenden Befehl im Terminal ausführen:
```bash
cat /proc/driver/nvidia/version
```
Wenn eine Meldung ähnlich der folgenden angezeigt wird, wurde die Installation erfolgreich durchgeführt:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Installation des NVIDIA Container Toolkit
Jetzt müssen wir das [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) installieren. Folgen Sie dem [offiziellen Installationsleitfaden für das NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), aber beachten Sie für Fedora die Hinweise in diesem Abschnitt, bevor Sie fortfahren.

### Für Apt-Benutzer (Ubuntu, Debian usw.)
#### 2-Apt-1. Konfiguration des Repositorys für den Paketdownload
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
> Bei Tests auf Fedora 40 stellte sich heraus, dass im Gegensatz zu Ubuntu der Befehl `nvidia-smi` und das Paket `nvidia-persistenced` nicht standardmäßig im NVIDIA-Grafiktreiber enthalten waren, sodass das Paket `xorg-x11-drv-nvidia-cuda` zusätzlich installiert werden musste. Ich habe es nicht direkt auf RHEL und Centos getestet, aber da die Systemkonfiguration sehr ähnlich zu Fedora ist, könnte es hilfreich sein, die gleiche Methode zu versuchen, falls Probleme auftreten, wenn Sie nach dieser Anleitung vorgehen.
{: .prompt-warning }

> Nach der Installation von `xorg-x11-drv-nvidia-cuda` wie oben beschrieben und dem Ausführen einer Beispiel-Workload funktionierte es auf meinem Fedora 40-System normal. Falls aufgrund von SELinux oder anderen Gründen immer noch Probleme auftreten, könnte das [Fedora-spezifische nvidia-container-toolkit-Paket und der Leitfaden](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) der Fedora AI-ML-Gruppe hilfreich sein.
{: .prompt-tip }

#### 2-Dnf-1. Konfiguration des Repositorys für den Paketdownload
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
#### 2-Zypper-1. Konfiguration des Repositorys für den Paketdownload
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Paketinstallation
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installation der Docker Engine
Als Nächstes installieren wir die Docker Engine. Folgen Sie der [offiziellen Docker-Dokumentation](https://docs.docker.com/engine/install/) für die Installation.

### Für Ubuntu
#### 3-Ubuntu-1. Entfernen älterer oder inoffizieller Pakete zur Vermeidung von Konflikten
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

#### 3-Ubuntu-2. Repository-Konfiguration
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

#### 3-Ubuntu-3. Paketinstallation
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 3-Ubuntu-4. Erstellung der `Docker`-Gruppe und Hinzufügen des Benutzers  
Um Nicht-Root-Benutzern die Verwaltung von Docker ohne `sudo` zu ermöglichen, erstellen Sie eine `Docker`-Gruppe und fügen Sie den Benutzer hinzu, der Docker verwenden möchte. Führen Sie die folgenden Befehle im Terminal aus:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Melden Sie sich anschließend ab und wieder an, damit die geänderten Einstellungen wirksam werden. Für Ubuntu oder Debian wird der Docker-Dienst bei jedem Systemstart automatisch ohne weitere Aktionen gestartet.

### Für Fedora
#### 3-Fedora-1. Entfernen älterer oder inoffizieller Pakete zur Vermeidung von Konflikten
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

#### 3-Fedora-2. Repository-Konfiguration
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

#### 3-Fedora-3. Paketinstallation  
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Während der Paketinstallation werden Sie gefragt, ob Sie den GPG-Schlüssel akzeptieren möchten. Wenn der GPG-Schlüssel mit `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35` übereinstimmt, geben Sie y ein, um ihn zu akzeptieren.  
> Falls der GPG-Schlüssel nicht übereinstimmt, könnte es sich um ein gefälschtes Paket handeln, das durch einen Supply-Chain-Angriff heruntergeladen wurde. In diesem Fall sollten Sie die Installation abbrechen.
{: .prompt-danger }

#### 3-Fedora-4. Starten des Docker-Daemons  
Docker ist jetzt installiert, aber noch nicht gestartet. Sie können Docker mit folgendem Befehl starten:
```bash
sudo systemctl start docker
```
Um den Docker-Dienst beim Systemstart automatisch zu starten, führen Sie die folgenden Befehle aus:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

#### 3-Fedora-5. Hinzufügen des Benutzers zur `Docker`-Gruppe  
Um Nicht-Root-Benutzern die Verwaltung von Docker zu ermöglichen, fügen Sie den Benutzer, der Docker verwenden möchte, zur `Docker`-Gruppe hinzu. Bei Fedora wird die `Docker`-Gruppe während der vorherigen Paketinstallation automatisch erstellt, sodass Sie nur den Benutzer hinzufügen müssen.
```bash
sudo usermod -aG docker $USER
```
Melden Sie sich anschließend ab und wieder an, damit die geänderten Einstellungen wirksam werden.

### Überprüfung der korrekten Einrichtung  
Führen Sie den folgenden Befehl im Terminal aus:
```bash
docker run hello-world
```
Wenn eine Meldung wie die folgende angezeigt wird, war die Installation erfolgreich:

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
