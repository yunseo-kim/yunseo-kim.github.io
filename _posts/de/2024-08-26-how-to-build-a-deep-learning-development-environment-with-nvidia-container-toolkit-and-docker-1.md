---
title: "Deep-Learning-Entwicklungsumgebung mit NVIDIA Container Toolkit und Docker/Podman aufbauen (1) – Installation von NVIDIA Container Toolkit & Container-Engine"
description: "Diese Serie zeigt, wie man lokal mit NVIDIA Container Toolkit eine containerbasierte Deep-Learning-Umgebung aufsetzt und sie mit SSH sowie JupyterLab als Remote-Server nutzbar macht. Teil 1 behandelt die Installation des NVIDIA Container Toolkits und der Container-Engine."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Übersicht

In dieser Serie behandeln wir die Installation von NVIDIA Container Toolkit und Docker oder Podman sowie den Prozess, eine Deep-Learning-Entwicklungsumgebung aufzubauen, indem wir auf Basis der von Docker Hub im [nvidia/cuda-Repository](https://hub.docker.com/r/nvidia/cuda) bereitgestellten CUDA- und cuDNN-Images ein Dockerfile erstellen. Damit Interessierte das Ergebnis frei übernehmen können, teile ich das durch diesen Prozess fertiggestellte [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) und [Image](https://hub.docker.com/r/yunseokim/dl-env/tags) über GitHub und Docker Hub und stelle zusätzlich eine Anleitung zur Einrichtung von SSH und JupyterLab für die Nutzung als Remote-Server bereit.  
Die Serie wird aus 3 Beiträgen bestehen; der Beitrag, den Sie gerade lesen, ist der erste Teil.
- Teil 1: Installation von NVIDIA Container Toolkit & Container-Engine (dieser Beitrag)
- [Teil 2: Container-Runtime-Konfiguration für GPU-Nutzung, Dockerfile-Erstellung und Container-Image-Build](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Teil 3 (geplant)

Wir gehen von einem x86_64-Linux-System mit einer CUDA-fähigen NVIDIA-Grafikkarte aus. Auf Distributionen außer Ubuntu oder Fedora habe ich es nicht direkt getestet; daher können einige Details leicht abweichen.  
(Überarbeitet am 12026.1.6.)

### Zusammensetzung der Entwicklungsumgebung

- Host-Betriebssystem und Architektur: x86_64, Linux (Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x usw.)
- Tech-Stack (Sprachen & Libraries), der eingerichtet werden soll
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/) (optional, NumPy/SciPy-compatible Array Library for GPU-accelerated Computing with Python)
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/) (optional, to accelerate pandas with zero code changes with the GPU accelerator)
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/) (optional, to quickly visualize and filter through large datasets, with a few lines of code, using best in class charting libraries)
  - [DALI](https://developer.nvidia.com/DALI) (optional, a high-performance alternative to built-in data loaders and data iterators using GPU)
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/) (optional, an accelerated n-dimensional image processing and image I/O alternative to scikit-image)
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/) (optional, to execute machine learning algorithms on GPUs with an API that closely follows the scikit-learn API)
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/) (optional, optimized algorithms for approximate nearest neighbors and clustering, along with many other essential tools for accelerated vector search)
  - [RAFT](https://docs.rapids.ai/api/raft/stable/) (optional, CUDA accelerated primitives which is used by other RAPIDS libraries)
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/) (optional, a GPU-accelerated graph analytics library which includes a zero-code-change accelerator for NetworkX)
  - [tqdm](https://tqdm.github.io/)

  > Je nach Situation und persönlicher Präferenz kann man auch erwägen, statt pandas die DataFrame-Library [Polars](https://pola.rs/) zu verwenden. Sie ist in Rust geschrieben und zeigt [bei der Verarbeitung großer Datenmengen zwar gegenüber der Kombination cuDF + pandas das Nachsehen, ist aber im Vergleich zum reinen pandas-Paket dennoch sehr leistungsstark](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/) und bietet eine stärker auf Queries spezialisierte Syntax. Laut dem offiziellen [Polars-Blog](https://pola.rs/posts/polars-on-gpu/) und der [cuDF-Dokumentation](https://docs.rapids.ai/api/cudf/stable/cudf_polars/) unterstützen Polars und das NVIDIA-RAPIDS-Team in Zusammenarbeit eine cuDF-basierte GPU-Beschleunigungs-Engine als Open Beta und treiben die Entwicklung zügig voran.
  {: .prompt-tip }

  > Falls Sie überlegen, ob Sie Docker CE oder Podman verwenden sollen, kann die [weiter unten stehende Vergleichstabelle](#3-installation-der-container-engine) hilfreich sein.
  {: .prompt-tip }

### Vergleichstabelle mit einer früheren ML-Entwicklungsumgebungs-Anleitung

Es gibt bereits einen [früheren Leitfaden zum Aufbau einer Machine-Learning-Entwicklungsumgebung](/posts/Setting-up-a-Machine-Learning-Development-Environment), der auf diesem Blog veröffentlicht wurde. Da es jedoch mehrere Änderungen gibt, habe ich diesen Beitrag neu verfasst. Die Unterschiede sind in der folgenden Tabelle zusammengefasst.

| Unterschied | Alter Beitrag (Version 12021) | Dieser Beitrag (geschrieben 12024, überarbeitete Version 12026) |
| --- | --- | --- |
| Linux-Distribution | Fokus auf Ubuntu | Neben Ubuntu auch anwendbar auf Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES usw. |
| Vorgehen beim Aufbau | Direkte Installation auf dem Host<br>Python-Virtualenv mit venv | Containerbasierte Umgebung mit [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br>Python-Virtualenv & Paketverwaltung mit uv |
| Installation des NVIDIA-Grafiktreibers | O | O |
| Direkte Installation von <br>CUDA und cuDNN auf dem Host | O (Apt-Paketmanager) | X (da vorinstallierte Images von NVIDIA auf dem<br>[Docker Hub](https://hub.docker.com/r/nvidia/cuda) verwendet werden, ist keine manuelle Installation nötig) |
| Portabilität | Beim Umzug auf ein anderes System muss die<br>Umgebung neu aufgebaut werden | Docker-basiert: Mit dem vorbereiteten Dockerfile kann man<br>bei Bedarf neue Images bauen oder bestehende Images<br>(abgesehen von zusätzlichen Volumes/Netzwerkeinstellungen)<br>leicht übertragen |
| Nutzung zusätzlicher <br>GPU-beschleunigter Libraries (außer cuDNN) | X | Einführung von [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter-Notebook-Interface | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH-Server-Konfiguration | Nicht behandelt | Enthält eine grundlegende SSH-Server-Konfiguration |

## 0. Vorab-Checks

- [NVIDIA Container Toolkit kann auf Linux-Distributionen verwendet werden, die die Paketmanager Apt, Yum oder Dnf sowie Zypper unterstützen.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Auf der verlinkten Seite können Sie die Liste der unterstützten Distributionen prüfen. Fedora ist zwar in der offiziellen Support-Tabelle nicht gesondert aufgeführt, basiert jedoch wie RHEL auf Red Hat Linux und ist daher problemlos nutzbar. Wenn Sie mit Linux nicht vertraut sind und unsicher sind, welche Distribution Sie wählen sollen, ist Ubuntu LTS in der Regel die sicherste Wahl: Auch proprietäre Treiber lassen sich automatisch installieren, was für Einsteiger relativ bequem ist, und wegen der großen Nutzerbasis sind die meisten technischen Dokumentationen auf Ubuntu ausgerichtet.
  - Die Architektur und die Version Ihrer Linux-Distribution können Sie im Terminal mit `uname -m && cat /etc/*release` prüfen.
- Prüfen Sie zunächst, ob die im System verbaute Grafikkarte die CUDA- und cuDNN-Versionen unterstützt, die Sie verwenden möchten.
  - Das GPU-Modell lässt sich im Terminal mit `lspci | grep -i nvidia` prüfen.
  - Auf <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> können Sie je cuDNN-Version die **unterstützte NVIDIA-Treiberversion** und die erforderliche **CUDA Compute Capability** sowie die **unterstützte NVIDIA-Hardware** nachschlagen.
  - Suchen Sie auf <https://developer.nvidia.com/cuda-gpus> Ihr Modell und prüfen Sie den **Compute-Capability**-Wert. Dieser muss die zuvor geprüfte **CUDA Compute Capability**-Anforderung erfüllen, damit CUDA und cuDNN ohne Probleme nutzbar sind.

> Wenn Sie eine neue Grafikkarte speziell für Deep-Learning-Workloads kaufen möchten, sind die Kriterien zur GPU-Auswahl im folgenden Beitrag sehr gut zusammengefasst. Der Autor aktualisiert den Artikel unregelmäßig.  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> Wenn Sie nicht nur eine GPU-, sondern eine umfassende Hardware-Konfigurations-Anleitung benötigen, ist auch der Beitrag [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) desselben Autors sehr hilfreich.
{: .prompt-tip }

Wenn alle oben genannten Punkte erfüllt sind, beginnen wir mit der Einrichtung der Arbeitsumgebung.

## 1. Installation des NVIDIA-Grafiktreibers

Zuerst muss der NVIDIA-Grafiktreiber auf dem Host-System installiert werden. Man kann den `.run`-Installer von der [NVIDIA-Treiber-Downloadseite](https://www.nvidia.com/drivers/) herunterladen und verwenden; empfehlenswerter ist jedoch, den Treiber über den Paketmanager des Systems zu installieren, da das in Bezug auf Versionsmanagement und Wartbarkeit vorteilhaft ist. Installieren Sie den passenden Treiber für Ihre Umgebung anhand der offiziellen Dokumentation: <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>.

### Proprietäres Modul vs. Open-Source-Modul

Der NVIDIA-Linux-Treiber besteht aus mehreren Kernel-Modulen. Seit dem Treiber 515 und späteren Releases stellt NVIDIA zwei Typen von Treiber-Kernel-Modulen bereit.

- Proprietary: Der proprietäre Treiber, den NVIDIA bisher bereitgestellt hat.
- Open-source: Ein Open-Source-Treiber unter Dual-Lizenz MIT/GPLv2. Der Quellcode ist unter <https://github.com/NVIDIA/open-gpu-kernel-modules> veröffentlicht.

Der Proprietary-Treiber wird für GPUs bereitgestellt, die auf Architekturen von Maxwell bis vor Blackwell basieren; ab der Blackwell-Architektur soll die Unterstützung eingestellt werden.  
Der Open-Source-Treiber hingegen wird für Turing und spätere Architekturen unterstützt.

[NVIDIA empfiehlt, wenn möglich, die Open-Source-Kernel-Module zu verwenden.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
Ob Ihre GPU mit dem Open-Source-Treiber kompatibel ist, können Sie über [diesen Link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus) prüfen.

In diesem Beitrag wird davon ausgegangen, dass der Open-Source-Treiber installiert wird.

### Debian & Ubuntu

Unter Ubuntu oder Debian installieren Sie ihn, indem Sie im Terminal die folgenden Befehle ausführen.
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Ausgehend von Fedora 40 stelle ich die Methode vor, vorgebaute Pakete aus [RPM Fusion](https://rpmfusion.org/RPM%20Fusion) herunterzuladen und zu installieren.

#### 1-Fedora-1. RPM-Fusion-Repository einrichten

Gehen Sie nach der [offiziellen RPM-Fusion-Anleitung](https://rpmfusion.org/Configuration) vor.  
Führen Sie im Terminal folgende Befehle aus.

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> In älteren DNF-Versionen (Fedora 40 und früher) sah die Kommandozeile zur Aktivierung des openh264-Repositorys in der zweiten Zeile wie folgt aus:
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> Seit DNF 5 (Fedora 41+) muss man stattdessen
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> verwenden; entsprechend wurde der Beitrag aktualisiert.
{: .prompt-info }

#### 1-Fedora-2. Paket `akmod-nvidia` installieren

Orientieren Sie sich an der [NVIDIA-Treiber-Installationsanleitung von RPM Fusion](https://rpmfusion.org/Howto/NVIDIA) und installieren Sie `akmod-nvidia`.

```bash
sudo dnf update  # Falls es in diesem Schritt ein Kernel-Update gab: in den neuesten Kernel rebooten und dann fortfahren
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> Ebenso war in älteren DNF-Versionen (Fedora 40 und früher) die Kommandozeile in der dritten Zeile zum Verhindern der NVIDIA-Treiber-Entfernung bei autoremove wie folgt:
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> Seit DNF 5 (Fedora 41+) muss man stattdessen
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> verwenden; entsprechend wurde der Beitrag aktualisiert.
{: .prompt-info }

> RPM Fusion hatte in der Vergangenheit eine kritische Haltung gegenüber den [NVIDIA Open-Source-Kernel-Modulen](#proprietaeres-modul-vs-open-source-modul) und lieferte standardmäßig den Proprietary-Treiber aus, sofern man nichts explizit angab. Laut den [kürzlich (Dezember 12025) geänderten Richtlinien von RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open) wird bei Hardware mit doppelter Unterstützung (Architekturen von Turing bis vor Blackwell) nun automatisch die bessere Variante ausgewählt; man müsse daher nicht mehr selbst entscheiden. Für ältere Architekturen vor Turing sowie für Blackwell und neuere Architekturen gab es ohnehin jeweils nur eine Option, sodass es dort keine Änderungen gibt.
> Entsprechend wurde bestätigt, dass Inhalte zur Festlegung der Open-Source-Kernel-Module über `/etc/rpm/macros.nvidia-kmod` entfernt wurden.
>
> Außerdem heißt es, man solle das Paket `akmod-nvidia-open` nur dann verwenden, wenn man Downstream-Änderungen am Kernel-Space-Treiber direkt anwenden muss.
>
> Diese Punkte wurden ebenfalls neu in den Beitrag aufgenommen.
{: .prompt-info }

#### 1-Fedora-3. Secure Boot: Schlüssel registrieren, damit der Treiber korrekt lädt  

> Mit den unten beschriebenen zusätzlichen Schritten kann man Secure Boot weiterhin nutzen und zugleich den NVIDIA-Grafiktreiber verwenden. Da das Deaktivieren von Secure Boot die Systemsicherheit deutlich schwächen kann, wird empfohlen, es nicht auszuschalten. Spätestens seit den 12020ern gibt es in den meisten Fällen kaum noch Gründe, Secure Boot zu deaktivieren.
{: .prompt-danger }

Installieren Sie zunächst die folgenden Tools.

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Erzeugen Sie anschließend mit dem folgenden Befehl einen Schlüssel.

```bash
sudo kmodgenca -a
```

Nun müssen Sie den erzeugten Schlüssel im MOK der UEFI-Firmware registrieren.

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

Nach Ausführung dieses Befehls werden Sie zur Eingabe eines Passworts für die Schlüsselregistrierung aufgefordert. In Kürze werden Sie neu booten müssen, um den Vorgang abzuschließen; das Passwort ist ein Einmalpasswort für diesen Schritt – geben Sie also etwas ein, das Sie kurz behalten können.

Starten Sie jetzt das System mit dem folgenden Befehl neu.

```bash
systemctl reboot
```

Beim Booten erscheint automatisch das MOK-Management-Fenster. Wählen Sie „Enroll MOK“, dann nacheinander „Continue“ und „Yes“. Danach wird ein Fenster angezeigt, das das zuvor gesetzte Passwort verlangt. Nach Eingabe ist die Schlüsselregistrierung abgeschlossen. Geben Sie nun „reboot“ ein, um erneut zu booten; danach sollte der NVIDIA-Treiber korrekt geladen werden.

### Überprüfen der NVIDIA-Treiberinstallation

Mit folgendem Befehl können Sie im Terminal prüfen, welches NVIDIA-Kernel-Modul aktuell geladen ist.

```bash
cat /proc/driver/nvidia/version
```

Wenn eine Ausgabe ähnlich der folgenden erscheint, ist die Installation erfolgreich.

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

Außerdem sollte unter Linux der oft standardmäßig verwendete Open-Source-Grafiktreiber bzw. das Kernel-Modul `nouveau` nach der Installation des NVIDIA-Treibers deaktiviert sein; andernfalls kann es Probleme verursachen. Nach Installation und Reboot sollte der folgende Befehl keine Ausgabe liefern.

```bash
lsmod |grep nouveau
```

## 2. Installation von NVIDIA Container Toolkit

Als Nächstes installieren Sie das [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Folgen Sie dabei der [offiziellen Installationsanleitung](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html). Für Fedora gibt es während der Installation Hinweise zu beachten – lesen Sie daher diesen Abschnitt vollständig, bevor Sie fortfahren.

### Bei Verwendung von Apt (Ubuntu, Debian usw.)

#### 2-Apt-1. Repository für den Paketdownload einrichten

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Paketliste aktualisieren

```bash
sudo apt update
```

#### 2-Apt-3. Paket installieren

```bash
sudo apt install nvidia-container-toolkit
```

### Bei Verwendung von Yum oder Dnf (Fedora, RHEL, Centos usw.)

> Als ich es unter Fedora 40 getestet habe, waren – anders als unter Ubuntu – der Befehl `nvidia-smi` sowie das Paket `nvidia-persistenced` nicht standardmäßig im NVIDIA-Grafiktreiber enthalten, sodass zusätzlich das Paket `xorg-x11-drv-nvidia-cuda` installiert werden musste. RHEL und Centos habe ich nicht direkt getestet; da die Systemkonfiguration aber Fedora sehr ähnlich ist, kann es hilfreich sein, dieselbe Vorgehensweise zu probieren, falls mit der folgenden Anleitung Probleme auftreten.
{: .prompt-warning }

> Unter Fedora 40 hat es bei mir nach Installation von `xorg-x11-drv-nvidia-cuda` und Test mit einem Sample-Workload korrekt funktioniert. Falls dennoch Probleme auftreten (z.B. wegen SELinux), kann das [Fedora-spezifische Paket und die Anleitung der Fedora AI-ML Group](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) hilfreich sein.
{: .prompt-tip }

#### 2-Dnf-1. Repository für den Paketdownload einrichten

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Paket installieren

```bash
sudo dnf install nvidia-container-toolkit
```

oder

```bash
sudo yum install nvidia-container-toolkit
```

### Bei Verwendung von Zypper (openSUSE, SLES)

#### 2-Zypper-1. Repository für den Paketdownload einrichten

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Paket installieren

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installation der Container-Engine

Als Nächstes installieren Sie als Container-Engine Docker CE oder Podman. Wählen Sie je nach Umgebung und Präferenz eine der beiden Optionen und orientieren Sie sich an der [Docker-Dokumentation](https://docs.docker.com/engine/install/) bzw. der [Podman-Dokumentation](https://podman.io/docs/installation).

Die folgende Tabelle fasst die wichtigsten Unterschiede sowie Vor- und Nachteile von Docker und Podman zusammen.

| Vergleichspunkt | Docker | Podman |
| --- | --- | --- |
| Architektur | Client-Server-Modell, daemon-basiert | Daemonlos (daemonless) |
| Sicherheit | Abhängig von einem Daemon, der standardmäßig mit<br>Root-Rechten läuft → potenzielles Sicherheitsrisiko<br>(Rootless-Modus seit Version 20.10, angekündigt in 12020,<br>aber zusätzliche Konfiguration nötig) | Kein Daemon; sofern nicht anders konfiguriert,<br>standardmäßig rootless und durch SELinux geschützt |
| Ressourcenverbrauch | Durch den daemon-basierten Aufbau läuft ein Background-Prozess<br>ständig, daher i.d.R. höherer Ressourcenverbrauch | In der Regel geringerer Overhead |
| Container-Startzeit | Relativ langsam | Durch vereinfachte Architektur bis zu ca. 50%<br>schnellere Ausführung |
| Ökosystem & Dokumentation | Sehr großes Ökosystem und Community-Support,<br>umfangreiche Dokumentation | Vergleichsweise kleineres Ökosystem und weniger Dokumentation |
| Networking | Docker Bridge Network | CNI (Container Network Interface)-Plugins |
| Native Unterstützung von<br>Kubernetes-YAML | X (Konvertierung nötig) | O |

Referenzen:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker hat eine längere Historie und gilt in der Industrie lange Zeit de facto als Standard, weshalb ein breites Ökosystem und sehr viel Dokumentation der größte Vorteil sind.  
Podman hingegen wurde сравнително kürzlich von Red Hat entwickelt und verfolgt von Grund auf einen daemonlosen und rootlosen Ansatz. Dadurch hat es Vorteile in Bezug auf Sicherheit, Systemressourcenverbrauch und Container-Startzeit. Ein weiterer Pluspunkt: Während bei Docker bei Problemen mit dem Daemon alle Container gemeinsam ausfallen können, sind Podman-Container vollständig unabhängig, sodass ein Ausfall eines Containers andere nicht beeinflusst.

Am wichtigsten ist es, je nach den eigenen Rahmenbedingungen das passende Tool zu wählen. Für Einsteiger scheint Podman jedoch eine gute Wahl zu sein. Zwar ist das Ökosystem im Vergleich zu Docker kleiner, doch dank der genannten Vorteile wächst es schnell und schließt die Lücke. Zudem ist es in vielen Bereichen mit Docker kompatibel, etwa bei Dockerfile-Syntax, Docker-Images und der CLI (Command Line Interface). Wenn es keinen zwingenden Grund gibt (z.B. weil bereits ein großes Docker-basiertes System existiert und ein Wechsel hohe Umstellungskosten verursacht), ist es sinnvoll, von Anfang an Podman zu wählen.

### Podman

Da es in den System-Repositories der meisten großen Linux-Distributionen verfügbar ist, lässt es sich einfach installieren.

#### Ubuntu

```bash
sudo apt install podman
```

#### Fedora

```bash
sudo dnf install podman
```

#### openSUSE

```bash
sudo zypper install podman
```

#### Prüfen, ob alles korrekt eingerichtet ist

Führen Sie im Terminal den folgenden Befehl aus.

```bash
podman run --rm hello-world
```

Wenn eine Ausgabe wie die folgende erscheint, ist es erfolgreich.

```bash
!... Hello Podman World ...!

         .--"--.           
       / -     - \         
      / (O)   (O) \        
   ~~~| -=(,Y,)=- |         
    .---. /`  \   |~~      
 ~/  o  o \~~~~.----. ~~   
  | =(X)= |~  / (O (O) \   
   ~~~~~~~  ~| =(Y_)=-  |   
  ~~~~    ~~~|   U      |~~ 

Project:   https://github.com/containers/podman
Website:   https://podman.io
Desktop:   https://podman-desktop.io
Documents: https://docs.podman.io
YouTube:   https://youtube.com/@Podman
X/Twitter: @Podman_io
Mastodon:  @Podman_io@fosstodon.org
```

> Als ich am 12025-12-18T00:43:00+09:00 mit Podman 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64` und Fedora 43 getestet habe, trat beim Ausführen von Containern oder beim Image-Build (einschließlich des obigen hello-world) der folgende Fehler auf:
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> Obwohl ich IPv6 nicht nutze und mich in einer IPv4-Netzwerkumgebung befinde, scheint dies dadurch ausgelöst zu werden, dass pasta (enthalten in der passt-Library) in der Container-Netzwerkkonfiguration IPv6-Routing versucht. Beim Container-Start bzw. in dem [später beschriebenen Image-Build-Schritt](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-docker-image-bauen-und-container-ausfuehren) konnte ich das Problem beheben, indem ich explizit `--net=pasta:-4` setze, um IPv4 zu erzwingen:
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> Bei der Recherche bin ich auf ein [bereits früher gemeldetes Issue mit denselben Symptomen](https://github.com/containers/podman/issues/22824) gestoßen. Dort heißt es, es sei in [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/) behoben worden. Da die beobachteten Symptome identisch sind und es u.a. ebenfalls in Verbindung mit Proton VPN auftrat, vermute ich, dass ein ähnliches Problem erneut aufgetreten sein könnte.
{: .prompt-warning }

### Docker CE

#### Ubuntu

##### 3-Ubuntu-1. Alte oder inoffizielle Pakete entfernen (Konfliktvermeidung)

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Repository einrichten

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

##### 3-Ubuntu-3. Pakete installieren

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Gruppe `Docker` erstellen und Benutzer hinzufügen

Damit auch ein non-root Benutzer Docker ohne `sudo` verwalten kann, erstellen Sie die Gruppe `Docker` und fügen den gewünschten Benutzer hinzu. Führen Sie im Terminal Folgendes aus.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Melden Sie sich anschließend ab und wieder an, damit die Änderungen wirksam werden. Unter Ubuntu oder Debian startet der Docker-Service in der Regel automatisch bei jedem Systemstart, ohne dass weitere Schritte nötig sind.

#### Fedora

##### 3-Fedora-1. Alte oder inoffizielle Pakete entfernen (Konfliktvermeidung)

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

##### 3-Fedora-2. Repository einrichten

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Pakete installieren

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Während der Installation werden Sie gefragt, ob Sie den GPG-Key akzeptieren möchten. Wenn der Key mit `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35` übereinstimmt, geben Sie `y` ein, um zu bestätigen.  
> Falls der GPG-Key nicht übereinstimmt, könnten die Pakete durch einen Supply-Chain-Angriff manipuliert worden sein; in diesem Fall sollte die Installation abgebrochen werden.
{: .prompt-danger }

##### 3-Fedora-4. Docker-Daemon starten

Docker ist jetzt installiert, aber noch nicht gestartet. Mit folgendem Befehl starten Sie Docker.

```bash
sudo systemctl start docker
```

Damit der Docker-Service bei jedem Systemstart automatisch läuft:

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Benutzer zur Gruppe `Docker` hinzufügen

Damit auch ein non-root Benutzer Docker verwalten kann, fügen Sie ihn zur Gruppe `Docker` hinzu. Unter Fedora wird die Gruppe `Docker` im Installationsprozess automatisch erstellt, daher müssen Sie nur den Benutzer registrieren.

```bash
sudo usermod -aG docker $USER
```

Melden Sie sich anschließend ab und wieder an, damit die Änderungen wirksam werden.

#### Prüfen, ob alles korrekt eingerichtet ist

Führen Sie im Terminal den folgenden Befehl aus.

```bash
docker run hello-world
```

Wenn eine Ausgabe wie die folgende erscheint, ist es erfolgreich.

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

## Weiterführendes
Fortsetzung in [Teil 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
