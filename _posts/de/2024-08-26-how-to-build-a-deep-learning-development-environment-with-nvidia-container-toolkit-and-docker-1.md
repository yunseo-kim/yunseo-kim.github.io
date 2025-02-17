---
title: Aufbau einer Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und Docker/Podman (1) - Installation von NVIDIA Container Toolkit & Container-Engine
description: Diese Serie behandelt den Aufbau einer containerbasierten Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit auf dem lokalen System sowie die Konfiguration von SSH und Jupyter Lab zur Nutzung als Remote-Server. Dieser Beitrag ist der erste Teil der Serie und stellt die Installationsmethoden für NVIDIA Container Toolkit und die Container-Engine vor.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Überblick
In dieser Serie behandeln wir die Installation von NVIDIA Container Toolkit und Docker oder Podman, das Schreiben eines Dockerfiles basierend auf CUDA- und cuDNN-Images aus dem [nvidia/cuda Repository](https://hub.docker.com/r/nvidia/cuda) auf Docker Hub, und den Aufbau einer Deep-Learning-Entwicklungsumgebung. Das [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und [Image](https://hub.docker.com/r/yunseokim/dl-env/tags), die durch diesen Prozess erstellt wurden, werden über GitHub und Docker Hub geteilt, damit sie von Interessierten frei genutzt werden können. Zusätzlich wird eine Anleitung zur Konfiguration von SSH und Jupyter Lab für die Nutzung als Remote-Server bereitgestellt.  
Die Serie wird aus drei Beiträgen bestehen, und dieser Beitrag ist der erste Teil der Serie.
- Teil 1: Installation von NVIDIA Container Toolkit & Container-Engine (dieser Beitrag)
- [Teil 2: Konfiguration der Container-Laufzeit für GPU-Nutzung, Erstellung des Dockerfiles und Erstellung des Container-Images](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Teil 3 (geplant)

Wir gehen davon aus, dass ein x86_64 Linux-System mit einer CUDA-fähigen NVIDIA-Grafikkarte verwendet wird. Obwohl nicht direkt getestet, können einige Details in anderen Distributionen als Ubuntu oder Fedora leicht abweichen.  
(Inhalt aktualisiert am 18.02.2025)

### Konfiguration der Entwicklungsumgebung
- Host-Betriebssystem und Architektur: x86_64, Linux-Umgebung (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x etc.)
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
  - cuDF (optional, zur Beschleunigung von pandas ohne Codeänderungen mit dem GPU-Beschleuniger)
  - Matplotlib & Seaborn
  - DALI (optional, hochperformante Alternative zu eingebauten Datenladern und Dateniteratoren mit GPU)
  - scikit-learn
  - cuML (optional, zur Ausführung von Machine-Learning-Algorithmen auf GPUs mit einer API, die der scikit-learn API sehr ähnlich ist)
  - PyTorch
  - tqdm

  > Je nach Situation und persönlicher Präferenz könnte man auch in Betracht ziehen, die [Polars](https://pola.rs/) DataFrame-Bibliothek anstelle von pandas zu verwenden. Sie ist in Rust geschrieben und [zeigt bei der Verarbeitung großer Datenmengen zwar eine geringere Leistung als die Kombination aus cuDF + pandas, übertrifft aber das reine pandas-Paket deutlich](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/). Zudem bietet sie eine auf Abfragen spezialisierte Syntax. Laut dem [offiziellen Polars-Blog](https://pola.rs/posts/polars-on-gpu/) plant das Team in Zusammenarbeit mit dem NVIDIA RAPIDS-Team, in naher Zukunft auch die Integration mit cuDF zu unterstützen.
  {: .prompt-tip }

  > Wenn Sie sich nicht sicher sind, ob Sie Docker CE oder Podman verwenden sollen, könnte die [später erwähnte Vergleichstabelle](#3-installation-der-container-engine) hilfreich sein.
  {: .prompt-tip }

### Vergleichstabelle mit dem zuvor erstellten Leitfaden zur Einrichtung einer Machine-Learning-Entwicklungsumgebung
Es existiert bereits ein [zuvor auf diesem Blog veröffentlichter Leitfaden zur Einrichtung einer Machine-Learning-Entwicklungsumgebung](/posts/Setting-up-a-Machine-Learning-Development-Environment), der größtenteils noch gültig ist. Aufgrund einiger Änderungen wurde jedoch dieser neue Beitrag verfasst. Die Unterschiede sind in der folgenden Tabelle zusammengefasst.

| Unterschied | Vorheriger Beitrag (Version 2021) | Dieser Beitrag (Version 2024) |
| --- | --- | --- |
| Linux-Distribution | Basierend auf Ubuntu | Anwendbar auf Ubuntu sowie Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES etc. |
| Methode zum Aufbau der Entwicklungsumgebung | Python-Virtuelle Umgebung mit venv | Container-basierte Umgebung mit<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Installation des NVIDIA-Grafiktreibers | Ja | Ja |
| Direkte Installation von CUDA und cuDNN<br> auf dem Host-System | Ja (mit Apt-Paketmanager) | Nein (Verwendung von vorinstallierten Images<br> von [NVIDIA auf Docker Hub](https://hub.docker.com/r/nvidia/cuda),<br> keine direkte Arbeit erforderlich) |
| Portabilität | Bei jedem Systemwechsel muss die<br> Entwicklungsumgebung neu aufgebaut werden | Docker-basiert, einfache Portierung durch<br> Erstellung neuer Images mit dem erstellten<br> Dockerfile oder einfache Übertragung<br> bestehender Images (außer zusätzlicher<br> Volumes oder Netzwerkeinstellungen) |
| Nutzung zusätzlicher GPU-<br>Beschleunigungsbibliotheken neben cuDNN | Nein | Einführung von [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook-Oberfläche | Jupyter Notebook (klassisch) | JupyterLab (Next-Generation) |
| SSH-Server-Konfiguration | Nicht behandelt | Teil 3 enthält grundlegende SSH-Server-<br>Konfigurationseinstellungen |

Wenn Sie lieber eine Python-virtuelle Umgebung wie venv anstelle von Docker verwenden möchten, ist der [vorherige Beitrag](/posts/Setting-up-a-Machine-Learning-Development-Environment) weiterhin gültig und kann als Referenz dienen.

## 0. Voraussetzungen
- [NVIDIA Container Toolkit ist in Linux-Distributionen verfügbar, die die Paketmanager Apt, Yum oder Dnf, Zypper unterstützen.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Auf der verlinkten Seite finden Sie eine Liste der unterstützten Linux-Distributionen. Obwohl nicht explizit in der offiziellen Unterstützungstabelle aufgeführt, funktioniert Fedora ebenfalls problemlos, da es auf Red Hat Linux basiert. Wenn Sie mit Linux nicht vertraut sind und nicht wissen, welche Distribution Sie verwenden sollten, ist die LTS-Version von Ubuntu die sicherste Wahl. Sie installiert automatisch proprietäre Treiber, was sie relativ benutzerfreundlich für Anfänger macht, und aufgrund der großen Benutzerbasis sind die meisten technischen Dokumente für Ubuntu verfasst.
  - Sie können die Architektur und Linux-Distribution Ihres Systems im Terminal mit dem Befehl `uname -m && cat /etc/*release` überprüfen.
- Zunächst sollten Sie überprüfen, ob die in Ihrem System installierte Grafikkarte die CUDA- und cuDNN-Version unterstützt, die Sie verwenden möchten.
  - Den Namen des in Ihrem Computer installierten GPU-Modells können Sie im Terminal mit dem Befehl `lspci | grep -i nvidia` überprüfen.
  - Auf der Seite <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> finden Sie eine Liste der **unterstützten NVIDIA-Grafiktreiber-Versionen**, die erforderliche **CUDA Compute Capability** und eine Liste der **unterstützten NVIDIA-Hardware** für jede cuDNN-Version.
  - Suchen Sie auf <https://developer.nvidia.com/cuda-gpus> nach dem entsprechenden Modellnamen und überprüfen Sie den Wert der **Compute Capability**. Dieser Wert muss die zuvor überprüfte **CUDA Compute Capability**-Bedingung erfüllen, damit CUDA und cuDNN problemlos verwendet werden können.

> Wenn Sie planen, eine neue Grafikkarte für Deep-Learning-Aufgaben zu kaufen, sind die Auswahlkriterien für GPUs in folgendem Artikel gut zusammengefasst. Der Autor aktualisiert den Artikel kontinuierlich.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> Ein weiterer sehr informativer Artikel desselben Autors ist [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/).
{: .prompt-tip }

Wenn alle oben genannten Bedingungen erfüllt sind, können wir mit dem Aufbau der Arbeitsumgebung beginnen.

## 1. Installation des NVIDIA-Grafiktreibers
Zunächst muss der NVIDIA-Grafiktreiber auf dem Host-System installiert werden. Sie können den .run-Installer von der [NVIDIA-Treiber-Download-Seite](https://www.nvidia.com/drivers/) herunterladen und verwenden, aber es ist aus Gründen der Versionsverwaltung und Wartung besser, den Paketmanager Ihres Systems zu nutzen. Beziehen Sie sich auf die offizielle Dokumentation unter <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>, um den für Ihre Systemumgebung geeigneten Grafiktreiber zu installieren.

### Proprietäres Modul vs Open-Source-Modul
Der NVIDIA Linux-Treiber besteht aus mehreren Kernelmodulen, und ab Treiberversion 515 bietet NVIDIA zwei Arten von Treiber-Kernelmodulen an:

- Proprietär: Der herkömmliche proprietäre Softwaretreiber, den NVIDIA bisher angeboten hat.
- Open-Source: Ein Open-Source-Treiber, der unter der MIT/GPLv2-Doppellizenz bereitgestellt wird. Der Quellcode ist unter <https://github.com/NVIDIA/open-gpu-kernel-modules> verfügbar.

Der proprietäre Treiber wird für GPUs basierend auf Architekturen von Maxwell bis vor Blackwell angeboten und wird ab der Blackwell-Architektur eingestellt.
Der Open-Source-Treiber hingegen wird für Architekturen ab Turing unterstützt.

[NVIDIA empfiehlt die Verwendung des Open-Source-Kernelmoduls, wenn möglich.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
Ob Ihre GPU mit dem Open-Source-Treiber kompatibel ist, können Sie [hier](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus) überprüfen.

In diesem Artikel gehen wir davon aus, dass der Open-Source-Treiber installiert wird.

### Debian & Ubuntu
Für Ubuntu oder Debian geben Sie die folgenden Befehle im Terminal ein, um den Treiber zu installieren:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Basierend auf Fedora 40 stellen wir eine Methode vor, um vorkompilierte Pakete von [RPM Fusion](https://rpmfusion.org/RPM%20Fusion) herunterzuladen und zu installieren.

#### 1-Fedora-1. Konfiguration des RPM Fusion-Repositorys  
Wir folgen der [offiziellen Anleitung von RPM Fusion](https://rpmfusion.org/Configuration).  
Führen Sie die folgenden Befehle im Terminal aus:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Installation des akmod-nvidia-open-Pakets  
Unter Bezugnahme auf die [NVIDIA-Treiberinstallationsanleitung von RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), 
aktivieren Sie das rpmfusion-nonfree-tainted-Repository und installieren Sie dann das akmod-nvidia-open-Paket.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Schlüsselregistrierung für korrektes Laden des Treibers bei aktiviertem Secure Boot  

> Mit dem unten beschriebenen zusätzlichen Verfahren können Sie den NVIDIA-Grafiktreiber normal verwenden, während Secure Boot aktiviert bleibt. Da die Deaktivierung von Secure Boot die Systemsicherheit erheblich beeinträchtigt, wird empfohlen, es nicht zu deaktivieren. Zumindest seit Beginn der 2020er Jahre gibt es kaum noch Gründe, Secure Boot zu deaktivieren.
{: .prompt-danger }

Installieren Sie zunächst die folgenden Tools:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Führen Sie dann den folgenden Befehl aus, um einen Schlüssel zu generieren:
```bash
sudo kmodgenca -a
```
Jetzt müssen Sie den generierten Schlüssel im MOK der UEFI-Firmware registrieren:
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Bei der Ausführung dieses Befehls werden Sie aufgefordert, ein Passwort für die Schlüsselregistrierung einzugeben. In Kürze werden Sie das System neu starten, um den Schlüsselregistrierungsprozess abzuschließen. Geben Sie ein Einmalpasswort ein, das Sie sich leicht merken können.

Führen Sie nun den folgenden Befehl aus, um das System neu zu starten:
```bash
systemctl reboot
```
Während des Systemstarts wird automatisch das MOK-Verwaltungsfenster erscheinen. Wählen Sie "Enroll MOK" und dann nacheinander "Continue" und "Yes". Es erscheint ein Fenster, das nach dem zuvor eingerichteten Passwort fragt. Geben Sie das Passwort ein, das Sie vorhin festgelegt haben, und der Schlüsselregistrierungsprozess wird abgeschlossen. Geben Sie nun reboot ein, um neu zu starten, und der NVIDIA-Treiber sollte normal geladen werden.

### Überprüfung der NVIDIA-Treiberinstallation
Sie können das aktuell geladene NVIDIA-Kernelmodul überprüfen, indem Sie den folgenden Befehl im Terminal ausführen:
```bash
cat /proc/driver/nvidia/version
```
Wenn eine Meldung ähnlich der folgenden ausgegeben wird, wurde die Installation erfolgreich durchgeführt:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Installation des NVIDIA Container Toolkit
Nun müssen wir das [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) installieren. Folgen Sie dem [offiziellen Installationsleitfaden des NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) für die Installation, aber beachten Sie für Fedora die Hinweise in diesem Abschnitt, bevor Sie fortfahren.

### Für Apt-Benutzer (Ubuntu, Debian etc.)
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

### Für Yum- oder Dnf-Benutzer (Fedora, RHEL, Centos etc.)
> Bei Tests auf Fedora 40 stellte sich heraus, dass im Gegensatz zu Ubuntu der Befehl `nvidia-smi` und das Paket `nvidia-persistenced` nicht standardmäßig im NVIDIA-Grafiktreiber enthalten waren, sodass das Paket `xorg-x11-drv-nvidia-cuda` zusätzlich installiert werden musste. Obwohl nicht direkt auf RHEL und Centos getestet, könnte aufgrund der sehr ähnlichen Systemkonfiguration zu Fedora die gleiche Methode hilfreich sein, falls Probleme auftreten sollten.
{: .prompt-warning }

> Nach der Installation von `xorg-x11-drv-nvidia-cuda` wie oben beschrieben und der Durchführung von Testarbeitslasten funktionierte alles normal auf dem System des Autors unter Fedora 40. Falls aufgrund von SELinux oder anderen Gründen weiterhin Probleme auftreten, könnte das [Fedora-spezifische nvidia-container-toolkit-Paket und die Anleitung](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) der Fedora AI-ML-Gruppe hilfreich sein.
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

## 3. Installation der Container-Engine
Als nächstes installieren wir Docker CE oder Podman als Container-Engine. Sie können eine der beiden basierend auf Ihrer Umgebung und Präferenz wählen. Beziehen Sie sich auf die [offizielle Docker-Dokumentation](https://docs.docker.com/engine/install/) und die [offizielle Podman-Dokumentation](https://podman.io/docs/installation).

Die folgende Tabelle fasst die Hauptunterschiede sowie Vor- und Nachteile von Docker und Podman zusammen:

| Vergleichspunkt | Docker | Podman |
| --- | --- | --- |
| Architektur | Client-Server-Modell, Daemon-basiert | Daemonless-Struktur |
| Sicherheit | Potenzielles Sicherheitsrisiko aufgrund der<br>Abhängigkeit von einem Daemon, der standardmäßig<br>mit Root-Rechten läuft (Rootless-Modus wird seit<br>Version 20.10 von 2020 unterstützt, erfordert<br>jedoch zusätzliche Konfiguration) | Läuft standardmäßig rootless, wenn nicht anders<br>angegeben, da es nicht von einem Daemon abhängt,<br>und wird durch SELinux geschützt |
| Ressourcenverbrauch | Generell höherer Ressourcenverbrauch aufgrund<br>des ständig laufenden Hintergrundprozesses<br>der Daemon-basierten Struktur | Generell geringerer Overhead |
| Container-Startzeit | Relativ langsamer | Bis zu 50% schnellere Ausführung dank<br>vereinfachter Architektur |
| Ökosystem und Dokumentation | Umfangreiches Ökosystem und Community-Support,<br>reichhaltige Dokumentation | Vergleichsweise kleineres Ökosystem und<br>weniger umfangreiche Dokumentation |
| Netzwerke | Verwendet Docker Bridge Network | Verwendet CNI (Container Network Interface)<br>Plugins |
| Native Unterstützung für<br>Kubernetes YAML | X (Konvertierung erforderlich) | O |

Referenzen:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker hat eine längere Geschichte und genießt de facto Standardstatus in der Branche, was sein größter Vorteil in Form eines breiten Ökosystems und umfangreicher Dokumentation ist.
Podman wurde relativ kürzlich von Red Hat entwickelt und strebt von Natur aus eine daemonless und rootless Struktur an, was in Bezug auf Sicherheit, Systemressourcennutzung und Container-Startzeit viele Vorteile bietet. Ein weiterer Vorteil von Podman ist, dass jeder Container vollständig unabhängig ist, sodass der Ausfall eines bestimmten Containers keine Auswirkungen auf andere Container hat, im Gegensatz zu Docker, wo alle Container ausfallen, wenn der Daemon Probleme hat und abstürzt.

Es ist am wichtigsten, das Werkzeug zu wählen, das zu den gegebenen Umständen passt. Für Einzelpersonen, die gerade erst anfangen, könnte Podman eine gute Wahl sein. Obwohl das Ökosystem im Vergleich zu Docker relativ klein ist, wächst es aufgrund der oben genannten Vorteile schnell und holt auf. Für Einzelpersonen oder kleine Gruppen sollte es kein großes Problem darstellen, da es in vielen Bereichen wie Dockerfile-Syntax, Docker-Images und CLI (Command Line Interface) mit dem bestehenden Docker kompatibel ist.

### Podman
Es kann einfach installiert werden, da es in den Standard-Systemrepositories der meisten großen Linux-Distributionen unterstützt wird.

#### Für Ubuntu
```bash
sudo apt install podman
```

#### Für Fedora
```bash
sudo dnf install podman
```

#### openSUSE
```bash
sudo zypper install podman
```

### Docker CE
#### Für Ubuntu
##### 3-Ubuntu-1. Entfernen älterer Versionen oder inoffizieller Pakete zur Vermeidung von Paketkonflikten
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

##### 3-Ubuntu-4. Erstellen der `Docker`-Gruppe und Hinzufügen von Benutzern
Um Nicht-Root-Benutzern die Verwaltung von Docker ohne `sudo` zu ermöglichen, erstellen Sie eine `Docker`-Gruppe und fügen Sie die Benutzer hinzu, die Docker verwenden möchten. Führen Sie die folgenden Befehle im Terminal aus:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Melden Sie sich anschließend ab und wieder an, damit die geänderten Einstellungen wirksam werden. Bei Ubuntu oder Debian wird der Docker-Dienst automatisch bei jedem Systemstart ohne zusätzliche Aktionen gestartet.

#### Für Fedora
##### 3-Fedora-1. Entfernen älterer Versionen oder inoffizieller Pakete zur Vermeidung von Paketkonflikten
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
Während der Paketinstallation werden Sie gefragt, ob Sie den GPG-Schlüssel akzeptieren möchten. Wenn der GPG-Schlüssel mit `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35` übereinstimmt, geben Sie y ein, um ihn zu akzeptieren.
> Falls der GPG-Schlüssel nicht übereinstimmt, sollten Sie die Installation abbrechen, da Sie möglicherweise ein gefälschtes Paket durch einen Supply-Chain-Angriff heruntergeladen haben.
{: .prompt-danger }

##### 3-Fedora-4. Starten des Docker-Daemons
Docker ist jetzt installiert, aber noch nicht gestartet. Sie können Docker mit folgendem Befehl starten:
```bash
sudo systemctl start docker
```
Um den Docker-Dienst beim Systemstart automatisch zu starten, führen Sie die folgenden Befehle aus:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Hinzufügen von Benutzern zur `Docker`-Gruppe
Um Nicht-Root-Benutzern die Verwaltung von Docker zu ermöglichen, fügen Sie die Benutzer, die Docker verwenden möchten, zur `Docker`-Gruppe hinzu. Bei Fedora wird die `Docker`-Gruppe während der vorherigen Paketinstallation automatisch erstellt, sodass Sie nur die Benutzer hinzufügen müssen.
```bash
sudo usermod -aG docker $USER
```
Melden Sie sich anschließend ab und wieder an, damit die geänderten Einstellungen wirksam werden.

#### Überprüfen der korrekten Einrichtung
Führen Sie den folgenden Befehl im Terminal aus:
```bash
docker run hello-world
```
Wenn die folgende Nachricht angezeigt wird, war die Installation erfolgreich:

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
