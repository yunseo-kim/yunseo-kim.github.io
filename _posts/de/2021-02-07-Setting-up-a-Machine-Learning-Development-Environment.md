---
title: Aufbau einer Entwicklungsumgebung für maschinelles Lernen
description: Dieser Artikel behandelt die Methode zum Aufbau einer Entwicklungsumgebung,
  die als erster Schritt zum Studium des maschinellen Lernens auf einem lokalen Rechner
  betrachtet werden kann. Der gesamte Inhalt wurde basierend auf Ubuntu 20.04 LTS
  mit einer NVIDIA GeForce RTX 3070 Grafikkarte geschrieben.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, CUDA, PyTorch, TensorFlow]
image: /assets/img/technology.jpg
---
## Überblick
Dieser Artikel behandelt die Methode zum Aufbau einer Entwicklungsumgebung, die als erster Schritt zum Studium des maschinellen Lernens auf einem lokalen Rechner betrachtet werden kann. Der gesamte Inhalt wurde basierend auf Ubuntu 20.04 LTS mit einer NVIDIA GeForce RTX 3070 Grafikkarte geschrieben.

- Aufzubauender Technologie-Stack
  - Ubuntu 20.04 LTS
  - Python 3.8
  - pip 21.0.1
  - jupyter
  - matplotlib
  - numpy
  - pandas
  - scipy
  - scikit-learn
  - CUDA 11.0.3
  - cuDNN 8.0.5
  - Deep Learning Framework (es wird empfohlen, nur eines pro Umgebung zu installieren)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

### Vergleichstabelle mit dem neu erstellten Leitfaden zum Aufbau einer Entwicklungsumgebung für maschinelles Lernen
Obwohl es etwa dreieinhalb Jahre her ist, seit dieser Artikel im Blog veröffentlicht wurde, ist der Inhalt dieses Artikels in großen Zügen immer noch gültig, abgesehen von einigen Details wie Paketversionen oder der Veröffentlichung des NVIDIA Open-Source-Treibers. Als ich jedoch im Sommer 2024 einen neuen PC kaufte und die Entwicklungsumgebung aufbaute, gab es einige Änderungen, weshalb ich [einen neuen Leitfaden zum Aufbau der Entwicklungsumgebung](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/) geschrieben habe. Die Unterschiede sind in der folgenden Tabelle aufgeführt.

| Unterschied | Dieser Artikel (Version 2021) | Neuer Artikel (Version 2024) |
| --- | --- | --- |
| Linux-Distribution | Basierend auf Ubuntu | Anwendbar auf Ubuntu sowie Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES usw. |
| Methode zum Aufbau der Entwicklungsumgebung | Python-Virtuelle Umgebung mit venv | Docker-Container-basierte Umgebung mit<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Installation des NVIDIA-Grafiktreibers | O | O |
| Direkte Installation von CUDA und cuDNN<br> auf dem Hostsystem | O (Verwendung des Apt-Paketmanagers) | X (Verwendung von vorinstallierten Images,<br> die von NVIDIA auf Docker Hub bereitgestellt werden,<br> daher keine direkte Arbeit erforderlich) |
| Portabilität | Entwicklungsumgebung muss bei jedem<br> Wechsel zu einem anderen System<br> neu aufgebaut werden | Docker-basiert, daher einfache Portierung<br> bestehender Images (außer zusätzlicher<br> Volumen- oder Netzwerkeinstellungen) oder<br> Erstellung neuer Images bei Bedarf mit<br> vorbereiteten Dockerfiles |
| Nutzung zusätzlicher GPU-Beschleunigungsbibliotheken<br> neben cuDNN | X | Einführung von [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook-Schnittstelle | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH-Server-Konfiguration | Nicht behandelt | Grundlegende SSH-Server-Konfiguration in Teil 3 enthalten |

Wenn Sie eine Python-virtuelle Umgebung wie venv anstelle von Docker verwenden möchten, ist dieser bestehende Artikel immer noch gültig und Sie können ihn weiterhin lesen. Wenn Sie die Vorteile der hohen Portabilität usw. von Docker-Containern nutzen möchten, oder wenn Sie planen, eine andere Linux-Distribution als Ubuntu wie Fedora zu verwenden, oder wenn Sie eine Umgebung mit einer NVIDIA-Grafikkarte verwenden und zusätzliche GPU-Beschleunigungsbibliotheken wie CuPy, cuDF, cuML, DALI usw. nutzen möchten, oder wenn Sie per Fernzugriff über SSH und JupyterLab-Konfiguration zugreifen möchten, empfehle ich Ihnen, auch den [neuen Leitfaden](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/) zu konsultieren.

## 0. Voraussetzungen
- Für das Studium des maschinellen Lernens wird die Verwendung von Linux empfohlen. Es ist zwar auch unter Windows möglich, aber es kann in vielen kleinen Bereichen zu Zeitverschwendung kommen. Am unkompliziertesten ist es, die neueste LTS-Version von Ubuntu zu verwenden. Nicht-Open-Source-Treiber werden automatisch installiert, was bequem ist, und aufgrund der großen Benutzerzahl sind die meisten technischen Dokumente für Ubuntu geschrieben.
- Im Allgemeinen ist Python in den meisten Linux-Distributionen, einschließlich Ubuntu, vorinstalliert. Wenn Python jedoch nicht installiert ist, müssen Sie es zuerst installieren, bevor Sie diesem Artikel folgen.
  - Sie können die aktuell installierte Python-Version mit dem folgenden Befehl überprüfen:
  ```
  $ python3 --version
  ```
  - Wenn Sie TensorFlow 2 oder PyTorch verwenden möchten, sollten Sie die kompatiblen Python-Versionen überprüfen. Zum Zeitpunkt des Schreibens dieses Artikels unterstützt [die neueste Version von PyTorch Python-Versionen](https://pytorch.org/get-started/locally/#linux-python) 3.6-3.8, und [die neueste Version von TensorFlow 2 unterstützt Python-Versionen](https://www.tensorflow.org/install) 3.5-3.8.  
  In diesem Artikel verwenden wir Python 3.8.
- Wenn Sie planen, maschinelles Lernen auf einem lokalen Rechner zu studieren, ist es ratsam, mindestens eine GPU vorzubereiten. Während die Datenvorverarbeitung auch mit der CPU möglich ist, ist der Unterschied in der Trainingsgeschwindigkeit zwischen CPU und GPU bei größeren Modellen in der Trainingsphase überwältigend (insbesondere im Fall des Deep Learning).
  - Für maschinelles Lernen gibt es praktisch nur eine Wahl für den GPU-Hersteller. Sie müssen ein NVIDIA-Produkt verwenden. NVIDIA ist ein Unternehmen, das erheblich in den Bereich des maschinellen Lernens investiert hat, und fast alle Frameworks für maschinelles Lernen verwenden die CUDA-Bibliothek von NVIDIA.
  - Wenn Sie planen, eine GPU für maschinelles Lernen zu verwenden, sollten Sie zuerst überprüfen, ob das Grafikkartenmodell, das Sie verwenden möchten, CUDA unterstützt. Sie können den Namen des GPU-Modells, das derzeit in Ihrem Computer installiert ist, im Terminal mit dem Befehl `uname -m && cat /etc/*release` überprüfen. Suchen Sie den entsprechenden Modellnamen in der GPU-Liste im [Link](https://developer.nvidia.com/cuda-gpus) und überprüfen Sie den Wert der **Compute Capability**. Dieser Wert sollte mindestens 3.5 betragen, damit CUDA verwendet werden kann.
  - Die Kriterien für die GPU-Auswahl sind in folgendem Artikel gut zusammengefasst. Der Autor aktualisiert den Artikel kontinuierlich.  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  Ein weiterer sehr informativer Artikel desselben Autors ist [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/). Die Schlussfolgerung des obigen Artikels lautet wie folgt:
    > Die RTX 3070 und RTX 3080 sind mächtige Karten, aber ihnen fehlt etwas Speicher. Für viele Aufgaben benötigen Sie jedoch nicht so viel Speicher.  
    > Die RTX 3070 ist perfekt, wenn Sie Deep Learning lernen möchten. Das liegt daran, dass die grundlegenden Fähigkeiten zum Training der meisten Architekturen erlernt werden können, indem man sie einfach etwas herunterskaliert oder etwas kleinere Eingangsbilder verwendet. Wenn ich Deep Learning erneut lernen würde, würde ich wahrscheinlich eine RTX 3070 oder sogar mehrere verwenden, wenn ich das Geld übrig hätte.
    > Die RTX 3080 ist derzeit bei weitem die kosteneffizienteste Karte und daher ideal für Prototyping. Für Prototyping möchten Sie den größten Speicher, der noch günstig ist. Mit Prototyping meine ich hier Prototyping in jedem Bereich: Forschung, kompetitives Kaggle, Hacken von Ideen/Modellen für ein Startup, Experimentieren mit Forschungscode. Für all diese Anwendungen ist die RTX 3080 die beste GPU.

Wenn Sie alle oben genannten Punkte erfüllt haben, lassen Sie uns mit dem Aufbau der Arbeitsumgebung beginnen.

## 1. Erstellung des Arbeitsverzeichnisses
Öffnen Sie ein Terminal und bearbeiten Sie die .bashrc-Datei, um die Umgebungsvariable zu registrieren (der Befehl folgt nach dem $-Prompt).  
Öffnen Sie zunächst den nano-Editor mit folgendem Befehl (vim oder ein anderer Editor ist auch in Ordnung):
```
$ nano ~/.bashrc
```
Fügen Sie am Ende der Datei Folgendes hinzu. Sie können den Inhalt in den Anführungszeichen nach Belieben in einen anderen Pfad ändern.  
```export ML_PATH="$HOME/ml"```

Drücken Sie Strg+O zum Speichern und dann Strg+X zum Beenden.

Führen Sie nun den folgenden Befehl aus, um die Umgebungsvariable anzuwenden:
```
$ source ~/.bashrc
```
Erstellen Sie das Verzeichnis:
```
$ mkdir -p $ML_PATH
```

## 2. Installation des pip-Paketmanagers
Es gibt mehrere Möglichkeiten, die für maschinelles Lernen erforderlichen Python-Pakete zu installieren. Sie können eine wissenschaftliche Python-Distribution wie Anaconda verwenden (empfohlen für Windows-Betriebssysteme) oder das integrierte Packaging-Tool von Python, pip, verwenden. Hier werden wir den pip-Befehl in der Bash-Shell unter Linux oder macOS verwenden.

Überprüfen Sie mit dem folgenden Befehl, ob pip auf Ihrem System installiert ist:
```
$ pip3 --version

Der Befehl 'pip3' wurde nicht gefunden, kann aber installiert werden mit:

sudo apt install python3-pip

```
Wenn Sie eine solche Ausgabe sehen, ist pip nicht auf Ihrem System installiert. Installieren Sie es mit dem Paketmanager Ihres Systems (hier apt) (wenn eine Versionsnummer angezeigt wird, ist es bereits installiert, überspringen Sie diesen Befehl):
```
$ sudo apt install python3-pip
```
Nun ist pip auf Ihrem System installiert.

## 3. Erstellung einer unabhängigen virtuellen Umgebung (empfohlen)
Um eine virtuelle Umgebung zu erstellen (um Konflikte mit Bibliotheksversionen anderer Projekte zu vermeiden), installieren Sie venv:
```
$ sudo apt install python3-venv
```
Erstellen Sie dann eine unabhängige Python-Umgebung wie folgt. Der Grund dafür ist, Konflikte zwischen den für jedes Projekt erforderlichen Bibliotheksversionen zu vermeiden. Sie sollten also bei jedem Start eines neuen Projekts eine neue virtuelle Umgebung erstellen, um eine unabhängige Umgebung aufzubauen.
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(Umgebungsname)
```
Um diese virtuelle Umgebung zu aktivieren, öffnen Sie ein Terminal und geben Sie den folgenden Befehl ein:
```
$ cd $ML_PATH
$ source ./(Umgebungsname)/bin/activate
```
Aktualisieren Sie pip in der virtuellen Umgebung, nachdem Sie sie aktiviert haben:
```
(env) $ pip install -U pip
```
Um die virtuelle Umgebung später zu deaktivieren, verwenden Sie den Befehl `deactivate`. Wenn die Umgebung aktiviert ist, wird jedes Paket, das Sie mit dem pip-Befehl installieren, in dieser unabhängigen Umgebung installiert, und Python wird dieses Paket verwenden.

## 3′. (Wenn keine virtuelle Umgebung erstellt wird) Aktualisierung der pip-Version
Bei der Installation von pip auf dem System wird eine Binärdatei vom Mirror-Server der Distribution (hier Ubuntu) heruntergeladen und installiert. Diese Binärdatei ist in der Regel nicht die neueste Version, da die Updates oft verzögert sind (in meinem Fall wurde Version 20.3.4 installiert). Um die neueste Version von pip zu verwenden, führen Sie den folgenden Befehl aus, um pip im *Benutzer-Heimatverzeichnis* zu installieren (oder zu aktualisieren, falls es bereits installiert ist):  
```
$ python3 -m pip install -U pip

Collecting pip
(gekürzt)
Successfully installed pip-21.0.1
```
Sie können sehen, dass pip auf Version 21.0.1 installiert wurde, die zum Zeitpunkt des Schreibens dieses Artikels die neueste ist. Da das im Benutzer-Heimatverzeichnis installierte pip vom System nicht automatisch erkannt wird, müssen Sie es als PATH-Umgebungsvariable registrieren, damit das System es erkennen und verwenden kann.

Öffnen Sie erneut die .bashrc-Datei mit einem Editor:
```
$ nano ~/.bashrc
```
Suchen Sie diesmal nach der Zeile, die mit `export PATH=` beginnt. Wenn es keinen Pfad dahinter gibt, fügen Sie einfach den Inhalt hinzu, wie Sie es in [Schritt 1](#1-erstellung-des-arbeitsverzeichnisses) getan haben. Wenn es bereits andere registrierte Pfade gibt, fügen Sie den Inhalt mit einem Doppelpunkt dahinter hinzu.  
```export PATH="$HOME/.local/bin"```  
```export PATH="(bestehender Pfad):$HOME/.local/bin"```

[Wenn Sie das System-pip auf eine andere Weise als den System-Paketmanager aktualisieren, können Probleme aufgrund von Versionskonflikten auftreten](https://github.com/pypa/pip/issues/5599). Deshalb installieren wir pip separat im Benutzer-Heimatverzeichnis. Aus dem gleichen Grund ist es ratsam, den Befehl `python3 -m pip` anstelle von `pip` zu verwenden, wenn Sie pip außerhalb einer virtuellen Umgebung verwenden.

## 4. Installation von Paketen für maschinelles Lernen (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)
Installieren Sie alle erforderlichen Pakete und ihre Abhängigkeiten mit dem folgenden pip-Befehl.  
In meinem Fall verwende ich venv, daher verwende ich einfach den `pip`-Befehl. Wenn Sie venv nicht verwenden, empfehle ich, wie bereits erwähnt, stattdessen den Befehl `python3 -m pip` zu verwenden.
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(gekürzt)
```
Wenn Sie venv verwendet haben, registrieren Sie den Kernel in Jupyter und geben Sie ihm einen Namen:
```
(env) $ python3 -m ipykernel install --user --name=(Kernelname)
```
Ab jetzt können Sie Jupyter mit folgendem Befehl starten:
```
(env) $ jupyter notebook
```

## 5. Installation von CUDA & cuDNN
### 5-1. Überprüfung der erforderlichen CUDA & cuDNN Versionen
Überprüfen Sie die unterstützten CUDA-Versionen in der [offiziellen PyTorch-Dokumentation](https://pytorch.org/get-started/locally/).  
![Überprüfung der kompatiblen CUDA-Version für PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
Basierend auf PyTorch Version 1.7.1 sind die unterstützten CUDA-Versionen 9.2, 10.1, 10.2, 11.0. Für NVIDIA 30-Serie GPUs ist CUDA 11 erforderlich, daher wissen wir, dass Version 11.0 benötigt wird.

Überprüfen Sie auch die erforderliche CUDA-Version in der [offiziellen TensorFlow 2-Dokumentation](https://www.tensorflow.org/install/gpu).  
![Überprüfung der kompatiblen CUDA-Version für TensorFlow 2](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
Basierend auf TensorFlow Version 2.4.0 haben wir festgestellt, dass CUDA Version 11.0 und cuDNN Version 8.0 erforderlich sind.

In meinem Fall überprüfe ich die CUDA-Versionen, die mit beiden Paketen kompatibel sind, da ich je nach Situation entweder PyTorch oder TensorFlow 2 verwende. Sie sollten die Anforderungen des Pakets überprüfen, das Sie benötigen, und sich danach richten.

### 5-2. Installation von CUDA
Gehen Sie zum [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) und wählen Sie die Version aus, die Sie zuvor überprüft haben. In diesem Artikel wählen wir [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
Wählen Sie nun die entsprechende Plattform und den Installertyp aus und folgen Sie den Anweisungen auf dem Bildschirm. [Es wird empfohlen, wenn möglich den Systempaketmanager für den Installer zu verwenden](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). Meine bevorzugte Methode ist deb (network).  
![Auswahl der CUDA-Plattform](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)  
![Installation von CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)  

Führen Sie die folgenden Befehle aus, um CUDA zu installieren:
```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```
Wenn Sie aufmerksam sind, werden Sie bemerkt haben, dass die letzte Zeile leicht von den Anweisungen im Bild abweicht. Bei der Netzwerkinstallation würde die Eingabe von cuda allein, wie im Bild gezeigt, die neueste Version 11.2 installieren, was nicht das ist, was wir wollen. Sie können verschiedene Meta-Paket-Optionen im [CUDA 11.0 Linux-Installationsleitfaden](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas) einsehen. Hier haben wir die letzte Zeile modifiziert, um das CUDA Toolkit-Paket in Version 11.0 zu installieren und das Treiberpaket automatisch aktualisieren zu lassen.

### 5-3. Installation von cuDNN
Installieren Sie cuDNN wie folgt:
```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```
## 6. Installation von PyTorch
Wenn Sie in Schritt 3 eine virtuelle Umgebung erstellt haben, fahren Sie mit aktivierter virtueller Umgebung fort. Überspringen Sie diesen Schritt, wenn Sie PyTorch nicht benötigen.  
Gehen Sie zur [PyTorch-Website](https://pytorch.org/get-started/locally/), wählen Sie den zu installierenden PyTorch-Build (Stable), das Betriebssystem (Linux), das Paket (Pip), die Sprache (Python) und CUDA (11.0) aus und folgen Sie den Anweisungen auf dem Bildschirm.  
![Installation von PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)
```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
Um zu überprüfen, ob PyTorch korrekt installiert wurde, starten Sie den Python-Interpreter und führen Sie die folgenden Befehle aus. Wenn ein Tensor zurückgegeben wird, war die Installation erfolgreich.
```
(env) $ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> x = torch.rand(5, 3)
>>> print(x)"
tensor([[0.8187, 0.5925, 0.2768],
        [0.9884, 0.8298, 0.8553],
        [0.6350, 0.7243, 0.2323],
        [0.9205, 0.9239, 0.9065],
        [0.2424, 0.1018, 0.3426]])
```
Um zu überprüfen, ob der GPU-Treiber und CUDA aktiviert und verfügbar sind, führen Sie den folgenden Befehl aus:
```
>>> torch.cuda.is_available()
True
```

## 7. Installation von TensorFlow 2
Ignorieren Sie diesen Schritt, wenn Sie TensorFlow nicht benötigen.  
Wenn Sie PyTorch in Schritt 6 in einer virtuellen Umgebung installiert haben, deaktivieren Sie diese Umgebung, gehen Sie zurück zu den Schritten 3 und 4, erstellen und aktivieren Sie eine neue virtuelle Umgebung und fahren Sie dann fort. Wenn Sie Schritt 6 übersprungen haben, fahren Sie einfach fort.  
Installieren Sie TensorFlow wie folgt:
```
(env2) $ pip install --upgrade tensorflow
```
Um zu überprüfen, ob TensorFlow korrekt installiert wurde, führen Sie den folgenden Befehl aus. Wenn der GPU-Name angezeigt wird und ein Tensor zurückgegeben wird, war die Installation erfolgreich.
```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
(gekürzt)
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```
