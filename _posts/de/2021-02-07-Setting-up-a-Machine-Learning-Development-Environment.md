---
title: "Aufbau einer Entwicklungsumgebung für maschinelles Lernen"
description: >-
  Dieser Artikel behandelt die Methode zum Aufbau einer Entwicklungsumgebung, die als erster Schritt zum Studium des maschinellen Lernens auf einem lokalen Rechner betrachtet werden kann. Der gesamte Inhalt wurde basierend auf Ubuntu 20.04 LTS mit einer NVIDIA Geforce RTX 3070 Grafikkarte erstellt.
categories:
  - Data Science
tags:
  - Machine Learning
  - Deep Learning
toc: true
toc_sticky: true
---

## Überblick
Dieser Artikel behandelt die Methode zum Aufbau einer Entwicklungsumgebung, die als erster Schritt zum Studium des maschinellen Lernens auf einem lokalen Rechner betrachtet werden kann. Der gesamte Inhalt wurde basierend auf Ubuntu 20.04 LTS mit einer NVIDIA Geforce RTX 3070 Grafikkarte erstellt.

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

## 0. Voraussetzungen
- Für das Studium des maschinellen Lernens wird die Verwendung von Linux empfohlen. Es ist zwar auch unter Windows möglich, aber es kann in vielen kleinen Bereichen zu Zeitverschwendung kommen. Die neueste LTS-Version von Ubuntu zu verwenden ist am unkompliziertesten. Nicht-Open-Source-Treiber werden automatisch installiert, was bequem ist, und da es viele Benutzer gibt, sind die meisten technischen Dokumente auf Ubuntu-Basis geschrieben.
- Im Allgemeinen ist Python in den meisten Linux-Distributionen, einschließlich Ubuntu, standardmäßig installiert. Wenn Python jedoch nicht installiert ist, sollten Sie es zuerst installieren, bevor Sie diesem Artikel folgen.
  - Die aktuell installierte Python-Version kann mit folgendem Befehl überprüft werden:
  ```
  $ python3 --version
  ```
  - Wenn Sie TensorFlow 2 oder PyTorch verwenden möchten, sollten Sie die kompatiblen Python-Versionen überprüfen. Zum Zeitpunkt des Schreibens dieses Artikels unterstützt [die neueste Version von PyTorch Python-Versionen](https://pytorch.org/get-started/locally/#linux-python) 3.6-3.8, und [die neueste Version von TensorFlow 2 unterstützt Python-Versionen](https://www.tensorflow.org/install) 3.5-3.8.  
  In diesem Artikel verwenden wir Python 3.8.
- Wenn Sie planen, maschinelles Lernen auf einem lokalen Rechner zu studieren, ist es ratsam, mindestens eine GPU vorzubereiten. Datenvorverarbeitung ist zwar auch mit der CPU möglich, aber in der Modelltrainingsphase wird der Geschwindigkeitsunterschied zwischen CPU und GPU mit zunehmender Modellgröße überwältigend (insbesondere im Fall des Deep Learning).
  - Für maschinelles Lernen gibt es praktisch nur eine Wahl für GPU-Hersteller. Man muss NVIDIA-Produkte verwenden. NVIDIA ist ein Unternehmen, das erheblich in den Bereich des maschinellen Lernens investiert hat, und fast alle Frameworks für maschinelles Lernen verwenden NVIDIAs CUDA-Bibliothek.
  - Wenn Sie planen, eine GPU für maschinelles Lernen zu verwenden, sollten Sie zuerst überprüfen, ob das Grafikkartenmodell, das Sie verwenden möchten, CUDA-fähig ist. Der Name des aktuell im Computer installierten GPU-Modells kann im Terminal mit dem Befehl ```nvidia-smi``` überprüft werden. Finden Sie den entsprechenden Modellnamen in der GPU-Liste im [Link](https://developer.nvidia.com/cuda-gpus) und überprüfen Sie den Wert der **Compute Capability**. Dieser Wert muss mindestens 3.5 betragen, damit CUDA verwendet werden kann.
  - Die Kriterien für die GPU-Auswahl sind in folgendem Artikel gut zusammengefasst. Der Autor aktualisiert den Artikel kontinuierlich.  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  Ein weiterer Artikel desselben Autors, [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/), ist ebenfalls sehr informativ. Die Schlussfolgerung des obigen Artikels lautet übrigens wie folgt:
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

Wenn alle oben genannten Punkte erfüllt sind, beginnen wir mit dem Aufbau der Arbeitsumgebung.

## 1. Erstellung des Arbeitsverzeichnisses
Öffnen Sie ein Terminal und bearbeiten Sie die .bashrc-Datei, um die Umgebungsvariable zu registrieren (der Befehl folgt nach dem $-Prompt).  
Öffnen Sie zunächst den nano-Editor mit folgendem Befehl (vim oder ein anderer Editor ist auch in Ordnung):
```
$ nano ~/.bashrc
```
Fügen Sie am Ende der Zeile Folgendes hinzu. Der Inhalt in Anführungszeichen kann, wenn gewünscht, in einen anderen Pfad geändert werden.  
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
Es gibt mehrere Möglichkeiten, die für maschinelles Lernen erforderlichen Python-Pakete zu installieren. Sie können eine wissenschaftliche Python-Distribution wie Anaconda verwenden (empfohlen für Windows-Betriebssysteme) oder das integrierte Packaging-Tool von Python, pip, verwenden. Hier werden wir den pip-Befehl in der Bash-Shell von Linux oder macOS verwenden.

Überprüfen Sie mit folgendem Befehl, ob pip auf Ihrem System installiert ist:
```
$ pip3 --version

Der Befehl 'pip3' wurde nicht gefunden, kann aber wie folgt installiert werden:

sudo apt install python3-pip

```
Wenn es so aussieht, ist pip nicht auf Ihrem System installiert. Installieren Sie es mit dem Paketmanager Ihres Systems (hier apt) (wenn eine Versionsnummer angezeigt wird, ist es bereits installiert, überspringen Sie diesen Befehl):
```
$ sudo apt install python3-pip
```
Jetzt ist pip auf Ihrem System installiert.

## 3. Erstellung einer unabhängigen virtuellen Umgebung (empfohlen)
Um eine virtuelle Umgebung zu erstellen (um Konflikte mit Bibliotheksversionen anderer Projekte zu vermeiden), installieren Sie venv:
```
$ sudo apt install python3-venv
```
Erstellen Sie dann wie folgt eine unabhängige Python-Umgebung. Der Grund dafür ist, Konflikte zwischen den für jedes Projekt erforderlichen Bibliotheksversionen zu verhindern. Sie sollten also jedes Mal, wenn Sie ein neues Projekt beginnen, eine neue virtuelle Umgebung erstellen, um eine unabhängige Umgebung aufzubauen.
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(Umgebungsname)
```
Um diese virtuelle Umgebung zu aktivieren, öffnen Sie ein Terminal und geben Sie den folgenden Befehl ein:
```
$ cd $ML_PATH
$ source ./(Umgebungsname)/bin/activate
```
Aktualisieren Sie nach der Aktivierung der virtuellen Umgebung pip innerhalb der virtuellen Umgebung:
```
(env) $ pip install -U pip
```
Um die virtuelle Umgebung später zu deaktivieren, verwenden Sie den Befehl ```deactivate```. Wenn die Umgebung aktiviert ist, wird jedes Paket, das Sie mit dem pip-Befehl installieren, in dieser unabhängigen Umgebung installiert, und Python verwendet diese Pakete.

## 3′. (Wenn keine virtuelle Umgebung erstellt wird) Aktualisierung der pip-Version
Wenn Sie pip auf dem System installieren, wird eine Binärdatei vom Mirror-Server der Distribution (hier Ubuntu) heruntergeladen und installiert. Diese Binärdatei ist in der Regel nicht die neueste Version, da die Updates oft verzögert sind (in meinem Fall wurde Version 20.3.4 installiert). Um die neueste Version von pip zu verwenden, führen Sie den folgenden Befehl aus, um pip im *Benutzer-Heimverzeichnis* zu installieren (oder zu aktualisieren, falls es bereits installiert ist):  
```
$ python3 -m pip install -U pip

Collecting pip
(gekürzt)
Successfully installed pip-21.0.1
```
Sie können sehen, dass pip auf Version 21.0.1 installiert wurde, die zum Zeitpunkt des Schreibens dieses Artikels die neueste ist. Da das im Benutzer-Heimverzeichnis installierte pip vom System nicht automatisch erkannt wird, müssen Sie es als PATH-Umgebungsvariable registrieren, damit das System es erkennen und verwenden kann.

Öffnen Sie die .bashrc-Datei erneut mit einem Editor:
```
$ nano ~/.bashrc
```
Suchen Sie diesmal nach der Zeile, die mit ```export PATH=``` beginnt. Wenn es keinen Pfad dahinter gibt, fügen Sie einfach den Inhalt hinzu, wie Sie es in [Schritt 1](#1-erstellung-des-arbeitsverzeichnisses) getan haben. Wenn es bereits andere registrierte Pfade gibt, fügen Sie den Inhalt mit einem Doppelpunkt dahinter hinzu.  
```export PATH="$HOME/.local/bin"```  
```export PATH="(bestehender Pfad):$HOME/.local/bin"```

[Wenn Sie das System-pip auf eine andere Weise als den Systempaketmanager aktualisieren, können Probleme aufgrund von Versionskonflikten auftreten](https://github.com/pypa/pip/issues/5599). Deshalb installieren wir pip ohne ```sudo``` im Benutzer-Heimverzeichnis. Aus demselben Grund ist es ratsam, den Befehl ```python3 -m pip``` anstelle von ```pip``` zu verwenden, wenn Sie pip außerhalb einer virtuellen Umgebung verwenden.

## 4. Installation von Paketen für maschinelles Lernen (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)
Installieren Sie alle erforderlichen Pakete und ihre Abhängigkeiten mit dem folgenden pip-Befehl.  
Wenn Sie venv nicht verwenden, benötigen Sie Administratorrechte.  
In meinem Fall verwende ich venv, daher habe ich einfach den ```pip```-Befehl verwendet. Wenn Sie venv nicht verwenden, empfehle ich, wie bereits erwähnt, stattdessen den Befehl ```python3 -m pip``` zu verwenden.
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(gekürzt)
```
Wenn Sie venv verwendet haben, registrieren Sie den Kernel für Jupyter und geben Sie ihm einen Namen:
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

Ich habe die CUDA-Versionen überprüft, die sowohl mit PyTorch als auch mit TensorFlow 2 kompatibel sind, da ich je nach Situation beide Pakete verwende. Sie sollten die Anforderungen des Pakets überprüfen, das Sie benötigen, und sich danach richten.

### 5-2. Installation von CUDA
Gehen Sie zum [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) und wäh