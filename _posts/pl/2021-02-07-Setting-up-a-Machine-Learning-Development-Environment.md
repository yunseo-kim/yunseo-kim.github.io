---
title: "Jak skonfigurować środowisko deweloperskie do uczenia maszynowego"
description: "W tym wpisie omawiam, jak skonfigurować środowisko do nauki uczenia maszynowego na komputerze lokalnym. Wszystko opisano dla Ubuntu 20.04 LTS oraz karty NVIDIA GeForce RTX 3070."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, CUDA, PyTorch, TensorFlow]
image: /assets/img/technology.webp
---

## Przegląd

W tym wpisie omawiam, jak skonfigurować środowisko deweloperskie, które można uznać za pierwszy krok w nauce uczenia maszynowego na komputerze lokalnym. Całość została przygotowana na Ubuntu 20.04 LTS, z założeniem użycia karty graficznej NVIDIA Geforce RTX 3070.

- Stos technologiczny, który skonfigurujemy
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
  - Framework do deep learningu (zalecane: w każdym środowisku instalować tylko jeden)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

### Tabela porównawcza z nowo napisaną instrukcją konfiguracji środowiska ML

Choć od publikacji tego wpisu na blogu minęło około 3,5 roku, jego treść nadal jest w dużej mierze aktualna — poza kilkoma szczegółami, takimi jak wersje pakietów czy ogłoszenia dotyczące otwartoźródłowych sterowników NVIDIA. Jednak latem [kalendarza holoceńskiego](https://en.wikipedia.org/wiki/Holocene_calendar) (rok 12024) kupiłem nowy komputer i konfigurując środowisko, wprowadziłem kilka zmian, dlatego napisałem [nowy przewodnik konfiguracji środowiska](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/). Różnice przedstawia poniższa tabela.

| Różnica | Ten wpis (wersja 12021) | Nowy wpis (wersja 12024) |
| --- | --- | --- |
| Dystrybucja Linuksa | w oparciu o Ubuntu | poza Ubuntu także Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES itd. |
| Sposób budowy środowiska | pythonowe środowisko wirtualne z użyciem venv | środowisko oparte o kontenery Docker<br> z użyciem [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalacja sterownika NVIDIA | O | O |
| Bezpośrednia instalacja <br>CUDA i cuDNN na hoście | O (z użyciem menedżera pakietów apt) | X (korzystamy z gotowych obrazów<br> dostarczanych przez NVIDIA na [Docker Hub](https://hub.docker.com/r/nvidia/cuda), więc nie trzeba robić tego ręcznie) |
| Przenośność | przy przenoszeniu na inny system<br> trzeba odtworzyć środowisko od zera | dzięki Dockerowi można łatwo przenosić: <br> w razie potrzeby budować nowe obrazy z Dockerfile <br> albo przenosić dotychczas używany obraz (z wyłączeniem dodatkowych wolumenów i ustawień sieci) |
| Dodatkowe biblioteki <br>akceleracji GPU poza cuDNN | X | wdrożenie: [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interfejs Jupyter Notebook | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| Konfiguracja serwera SSH | nie omawiana osobno | w części 3 uwzględniono podstawową konfigurację serwera SSH |

Jeśli zamiast Dockera chcesz korzystać z pythonowych środowisk wirtualnych typu venv, ten wpis również nadal jest aktualny, więc możesz czytać dalej. Jeżeli natomiast chcesz skorzystać z zalet kontenerów Docker (np. wysoka przenośność), planujesz używać dystrybucji innej niż Ubuntu (np. Fedora), korzystasz z karty NVIDIA i chcesz wykorzystywać dodatkowe biblioteki akceleracji GPU (CuPy, cuDF, cuML, DALI itd.), albo chcesz łączyć się zdalnie przez SSH i skonfigurować JupyterLab, to warto zajrzeć także do [nowego przewodnika](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/).

## 0. Wymagania wstępne / rzeczy do sprawdzenia

- Do nauki uczenia maszynowego zalecam korzystanie z Linuksa. Na Windowsie też się da, ale na wielu drobnych rzeczach łatwo stracić czas. Najbezpieczniejszym wyborem jest najnowsze wydanie Ubuntu LTS. Wygodne jest to, że nawet niewolne (własnościowe) sterowniki mogą zostać zainstalowane automatycznie, a dzięki dużej liczbie użytkowników większość dokumentacji technicznej jest pisana pod Ubuntu.
- Zwykle Python jest preinstalowany w Ubuntu i większości dystrybucji Linuksa. Jeśli jednak nie jest zainstalowany, przed kontynuowaniem tego wpisu trzeba go najpierw zainstalować.
  - Aktualnie zainstalowaną wersję Pythona można sprawdzić poleceniem:
    ```
    $ python3 --version
    ```
  - Jeśli planujesz używać TensorFlow 2 albo PyTorch, musisz sprawdzić kompatybilne wersje Pythona. Na moment pisania tego wpisu [najnowsza wersja PyTorch wspiera Pythona 3.6–3.8](https://pytorch.org/get-started/locally/#linux-python), a [najnowsza wersja TensorFlow 2 wspiera Pythona 3.5–3.8](https://www.tensorflow.org/install).  
  W tym wpisie używam Pythona 3.8.
- Jeśli planujesz uczyć ML na komputerze lokalnym, dobrze jest mieć co najmniej jeden GPU. Wstępne przetwarzanie danych da się zrobić na CPU, ale na etapie trenowania modeli — im większy model, tym różnica prędkości trenowania między CPU i GPU jest miażdżąca (szczególnie w deep learningu).
  - W praktyce wybór producenta GPU do ML jest zasadniczo jeden: trzeba używać NVIDIA. NVIDIA od dawna mocno inwestuje w ML, a prawie wszystkie frameworki ML korzystają z bibliotek CUDA.
  - Jeśli chcesz używać GPU do ML, najpierw sprawdź, czy dana karta obsługuje CUDA. Nazwę modelu GPU zainstalowanego w komputerze można sprawdzić w terminalu poleceniem `uname -m && cat /etc/*release`. Następnie znajdź swój model na liście GPU pod [tym linkiem](https://developer.nvidia.com/cuda-gpus) i sprawdź wartość **Compute Capability**. Musi wynosić co najmniej 3.5, aby możliwe było używanie CUDA.
  - Kryteria doboru GPU są dobrze zebrane w poniższym wpisie (autor regularnie go aktualizuje):  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  Bardzo przydatny jest też jego tekst [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/). Dla porządku: wnioski z powyższego wpisu są następujące.
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

Jeśli spełniłeś wszystkie powyższe warunki, zaczynajmy konfigurację środowiska.

## 1. Utworzenie katalogu roboczego

Otwórz terminal i zmodyfikuj plik `.bashrc`, aby zarejestrować zmienną środowiskową (po znaku `$` znajduje się polecenie).  
Najpierw otwórz edytor nano (vim lub inny edytor też jest OK).

```
$ nano ~/.bashrc
```

Na końcu pliku dodaj następującą treść. Jeśli chcesz, możesz zmienić ścieżkę wewnątrz cudzysłowu.  
`export ML_PATH="$HOME/ml"`

Wciśnij Ctrl+O, aby zapisać, a następnie Ctrl+X, aby wyjść.

Teraz wykonaj poniższe polecenie, aby zastosować zmiany w zmiennych środowiskowych.

```
$ source ~/.bashrc
```

Utwórz katalog.

```
$ mkdir -p $ML_PATH
```

## 2. Instalacja menedżera pakietów pip

Istnieje kilka sposobów instalacji pakietów Pythona potrzebnych do ML. Możesz użyć naukowej dystrybucji Pythona, takiej jak Anaconda (zalecane w przypadku Windowsa), albo skorzystać z pip — narzędzia do pakietowania Pythona. Tutaj będziemy używać polecenia pip w powłoce bash na Linuksie lub macOS.

Sprawdź, czy pip jest zainstalowany, poleceniem:

```
$ pip3 --version

Nie można odnaleźć polecenia 'pip3', ale można je zainstalować przez:

sudo apt install python3-pip

```

Jeśli widzisz taki komunikat, to pip nie jest zainstalowany. Zainstaluj go przez menedżer pakietów systemu (tutaj: apt). (Jeśli wyświetliła się wersja, pip jest już zainstalowany — wtedy ten krok pomiń.)

```
$ sudo apt install python3-pip
```

Teraz pip jest już zainstalowany w systemie.

## 3. Utworzenie niezależnego środowiska wirtualnego (zalecane)

Aby stworzyć środowisko wirtualne (żeby uniknąć konfliktów wersji bibliotek między różnymi projektami), zainstaluj venv.

```
$ sudo apt install python3-venv
```

Następnie utwórz niezależne środowisko Pythona w następujący sposób. Robi się to po to, by uniknąć konfliktów: różne projekty mogą wymagać różnych wersji bibliotek. W praktyce oznacza to, że dla każdego nowego projektu tworzysz nowe środowisko wirtualne.

```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(nazwa środowiska)
```

Aby aktywować środowisko wirtualne, otwórz terminal i wpisz:

```
$ cd $ML_PATH
$ source ./(nazwa środowiska)/bin/activate
```

Po aktywacji zaktualizuj pip wewnątrz środowiska.

```
(env) $ pip install -U pip
```

Później, aby zdezaktywować środowisko, użyj polecenia `deactivate`. Gdy środowisko jest aktywne, każdy pakiet instalowany poleceniem pip trafia do tego izolowanego środowiska, a Python będzie z niego korzystał.

## 3′. (Jeśli nie tworzysz środowiska wirtualnego) aktualizacja wersji pip

Gdy instalujesz pip w systemie, dystrybucja (tu: Ubuntu) pobiera i instaluje binaria z serwerów mirror — te pliki binarne zwykle są aktualizowane z opóźnieniem, więc często nie jest to najnowsza wersja (u autora była to 20.3.4). Aby używać najnowszego pip, wykonaj poniższe polecenie, instalując (lub aktualizując) pip w *katalogu domowym użytkownika*.  

```
$ python3 -m pip install -U pip

Collecting pip
(…)
Successfully installed pip-21.0.1
```

Widać, że pip został zainstalowany w wersji 21.0.1, która w momencie pisania była najnowsza. Ponieważ pip zainstalowany w katalogu domowym nie jest automatycznie wykrywany przez system, trzeba dodać go do zmiennej PATH.

Ponownie otwórz `.bashrc` w edytorze.

```
$ nano ~/.bashrc
```

Tym razem znajdź linię zaczynającą się od `export PATH=`. Jeśli po niej nie ma żadnych ścieżek, dodaj wpis tak jak w [kroku 1](#1-utworzenie-katalogu-roboczego). Jeśli są już inne ścieżki, dopisz nową po dwukropku.  
`export PATH="$HOME/.local/bin"`  
`export PATH="(istniejąca ścieżka):$HOME/.local/bin"`

[Jeśli zaktualizujesz systemowego pip inną metodą niż przez systemowy menedżer pakietów, mogą wystąpić problemy z konfliktami wersji](https://github.com/pypa/pip/issues/5599). Dlatego instalujemy pip osobno w katalogu domowym użytkownika. Z tego samego powodu, jeśli nie jesteś w środowisku wirtualnym, zamiast polecenia `pip` lepiej używać `python3 -m pip`.

## 4. Instalacja pakietów do ML (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)

Poniższym poleceniem pip zainstaluj wymagane pakiety oraz wszystkie zależności.  
U autora, ponieważ używa venv, wystarcza polecenie `pip`. Jeśli jednak nie używasz venv, to — jak wspomniano — zalecane jest użycie `python3 -m pip`.

```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(…)
```

Jeśli używasz venv, zarejestruj kernel w Jupyter i nadaj mu nazwę.

```
(env) $ python3 -m ipykernel install --user --name=(nazwa kernela)
```

Od teraz, aby uruchomić Jupyter, użyj:

```
(env) $ jupyter notebook
```

## 5. Instalacja CUDA i cuDNN

### 5-1. Sprawdzenie wymaganych wersji CUDA i cuDNN

Sprawdź w [oficjalnej dokumentacji PyTorch](https://pytorch.org/get-started/locally/), jakie wersje CUDA są wspierane.  
![Sprawdzenie kompatybilnej wersji CUDA dla PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
Dla PyTorch 1.7.1 wspierane są CUDA: 9.2, 10.1, 10.2 oraz 11.0. Ponieważ karty z serii NVIDIA 30 wymagają CUDA 11, widać, że potrzebujemy wersji 11.0.

Sprawdź też wymagane wersje CUDA w [oficjalnej dokumentacji TensorFlow 2](https://www.tensorflow.org/install/gpu).  
![Sprawdzenie kompatybilnej wersji CUDA dla TensorFlow 2](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
Dla TensorFlow 2.4.0 również potrzebna jest CUDA 11.0, a cuDNN w wersji 8.0.

Autor czasem używa PyTorch, a czasem TensorFlow 2, więc sprawdził kompatybilne wersje CUDA dla obu pakietów. Ty po prostu dobierz wersje zgodnie z wymaganiami tego, czego potrzebujesz.

### 5-2. Instalacja CUDA

Wejdź na stronę [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive), wybierz wcześniej ustaloną wersję i przejdź dalej. W tym wpisie wybieramy [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
Teraz wybierz odpowiednią platformę i typ instalatora, a następnie wykonuj instrukcje z ekranu. W tym miejscu [w przypadku instalatora zaleca się w miarę możliwości użycie systemowego menedżera pakietów](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). Preferowana przez autora metoda to deb (network).  
![Wybór platformy CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)  
![Instalacja CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)  

Wykonaj poniższe polecenia, aby zainstalować CUDA.

```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```

Jeśli jesteś spostrzegawczy, zauważysz, że ostatnia linia trochę różni się od instrukcji widocznej na obrazku. W instalacji sieciowej, jeśli wpiszesz `cuda` dokładnie jak na obrazku, zainstaluje się najnowsza wersja (11.2), a tego nie chcemy. W [przewodniku instalacji CUDA 11.0 dla Linuksa](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas) można sprawdzić różne opcje metapakietów. Tutaj zmodyfikowałem ostatnią linię tak, aby przypiąć CUDA Toolkit do wersji 11.0, a pakiety sterownika pozostawić do automatycznych aktualizacji.

### 5-3. Instalacja cuDNN

Zainstaluj cuDNN w następujący sposób.

```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```

## 6. Instalacja PyTorch

Jeśli w kroku 3 utworzyłeś środowisko wirtualne, wykonuj ten krok przy aktywnym środowisku. Jeśli PyTorch nie jest potrzebny, możesz pominąć ten krok.  
Wejdź na stronę [PyTorch](https://pytorch.org/get-started/locally/) i wybierz: build PyTorch (Stable), system (Linux), pakiet (Pip), język (Python) oraz CUDA (11.0), a następnie wykonuj instrukcje z ekranu.  
![Instalacja PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)

```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

Aby zweryfikować poprawność instalacji, uruchom interpreter Pythona i wykonaj poniższe polecenia. Jeśli zwróci tensor, wszystko działa.

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

Aby sprawdzić, czy sterownik GPU i CUDA są aktywne oraz dostępne, wykonaj:

```
>>> torch.cuda.is_available()
True
```

## 7. Instalacja TensorFlow 2

Jeśli TensorFlow nie jest potrzebny, możesz pominąć ten krok.  
Jeżeli w kroku 6 zainstalowałeś PyTorch w środowisku wirtualnym, to to środowisko zdezaktywuj, wróć do kroków 3 i 4, utwórz nowe środowisko wirtualne, aktywuj je i dopiero wtedy kontynuuj. Jeśli pominąłeś krok 6, możesz po prostu kontynuować.  
Zainstaluj TensorFlow następująco:

```
(env2) $ pip install --upgrade tensorflow
```

Aby zweryfikować poprawność instalacji TensorFlow, wykonaj poniższe polecenie. Jeśli wyświetli nazwę GPU i zwróci tensor, wszystko działa.

```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
(…)
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```
