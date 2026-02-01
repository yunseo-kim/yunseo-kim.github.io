---
title: "Budowa środowiska deweloperskiego do deep learningu z NVIDIA Container Toolkit oraz Docker/Podman (1) — instalacja NVIDIA Container Toolkit i silnika kontenerów"
description: "Seria pokazuje, jak zbudować lokalnie kontenerowe środowisko do deep learningu z NVIDIA Container Toolkit oraz skonfigurować SSH i JupyterLab, aby używać go jak zdalnego serwera. W tej części omawiam instalację NVIDIA Container Toolkit i silnika kontenerów."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Przegląd

W tej serii instalujemy NVIDIA Container Toolkit oraz Docker lub Podman, a następnie — bazując na obrazach CUDA i cuDNN z [repozytorium nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) na Docker Hub — piszemy Dockerfile i budujemy kontenerowe środowisko deweloperskie do deep learningu. Aby każdy mógł swobodnie skorzystać z gotowych efektów, udostępniam Dockerfile przygotowany w tym procesie ([Dockerfile](https://github.com/yunseo-kim/dl-env-docker)) oraz gotowe [obrazy](https://hub.docker.com/r/yunseokim/dl-env/tags) poprzez GitHub i Docker Hub; dodatkowo dostarczam przewodnik konfiguracji SSH i JupyterLab, aby używać środowiska jako zdalnego serwera.  
Seria będzie składać się z 3 wpisów, a czytany teraz tekst to część pierwsza.
- Część 1: NVIDIA Container Toolkit i instalacja silnika kontenerów (ten wpis)
- [Część 2: konfiguracja runtime’u kontenerów dla GPU, pisanie Dockerfile i budowanie obrazu kontenera](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Część 3 (w przygotowaniu)

Zakładam system x86_64 z Linuksem oraz kartą NVIDIA obsługującą CUDA; nie testowałem bezpośrednio dystrybucji innych niż Ubuntu i Fedora, więc niektóre detale mogą się nieznacznie różnić.  
(aktualizacja: 12026.1.6.)

### Skład środowiska

- System hosta i architektura: x86_64, Linux (Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x itd.)
- Stos technologiczny (języki i biblioteki)
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/) (opcjonalnie, biblioteka tablic kompatybilna z NumPy/SciPy do obliczeń akcelerowanych GPU w Pythonie)
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/) (opcjonalnie, aby przyspieszyć pandas na GPU bez zmian w kodzie)
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/) (opcjonalnie, szybka wizualizacja i filtrowanie dużych zbiorów danych kilkoma linijkami kodu, z użyciem wysokiej klasy bibliotek do wykresów)
  - [DALI](https://developer.nvidia.com/DALI) (opcjonalnie, wysokowydajna alternatywa dla wbudowanych data loaderów i iteratorów danych, wykorzystująca GPU)
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/) (opcjonalnie, akcelerowana GPU alternatywa dla scikit-image do n-wymiarowego przetwarzania obrazów i I/O)
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/) (opcjonalnie, uruchamianie algorytmów ML na GPU z API zbliżonym do scikit-learn)
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/) (opcjonalnie, zoptymalizowane algorytmy dla approximate nearest neighbors i klasteryzacji oraz inne narzędzia do przyspieszonego wyszukiwania wektorowego)
  - [RAFT](https://docs.rapids.ai/api/raft/stable/) (opcjonalnie, prymitywy akcelerowane CUDA, używane przez inne biblioteki RAPIDS)
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/) (opcjonalnie, biblioteka analityki grafów akcelerowana GPU, zawiera też akcelerator „zero code change” dla NetworkX)
  - [tqdm](https://tqdm.github.io/)

  > W zależności od sytuacji i własnych preferencji można rozważyć użycie biblioteki DataFrame [Polars](https://pola.rs/) zamiast pandas. Jest napisana w Rust; [w przetwarzaniu bardzo dużych danych ustępuje zestawowi cuDF + pandas, ale w porównaniu do „czystego” pakietu pandas często wypada znacząco lepiej wydajnościowo](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/) i oferuje składnię bardziej ukierunkowaną na zapytania (query). Zgodnie z oficjalnym [blogiem Polars](https://pola.rs/posts/polars-on-gpu/) oraz [dokumentacją cuDF](https://docs.rapids.ai/api/cudf/stable/cudf_polars/), Polars współpracuje z zespołem NVIDIA RAPIDS nad akceleracją GPU opartą o cuDF (otwarta beta) i prace szybko postępują.
  {: .prompt-tip }

  > Jeśli wahasz się między Docker CE a Podman, pomocna może być [tabela porównawcza poniżej](#3-instalacja-silnika-kontenerów).
  {: .prompt-tip }

### Tabela porównawcza z wcześniejszym poradnikiem budowy środowiska ML

Na blogu istnieje już [wcześniejszy poradnik budowy środowiska deweloperskiego do machine learningu](/posts/Setting-up-a-Machine-Learning-Development-Environment), ale ze względu na liczne zmiany przygotowałem nowy wpis. Różnice przedstawia poniższa tabela.

| Różnica | Poprzedni wpis (wersja 12021) | Ten wpis (napisany 12024, zaktualizowany 12026) |
| --- | --- | --- |
| Dystrybucja Linuksa | Ubuntu | Oprócz Ubuntu: Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES itd. |
| Sposób budowy środowiska | Instalacja bezpośrednio na hoście<br>wirtualne środowisko Pythona przez venv | Środowisko oparte o kontenery Docker<br>z użyciem [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br> wirtualne środowisko i zarządzanie pakietami przez uv |
| Instalacja sterownika graficznego NVIDIA | O | O |
| Bezpośrednia instalacja <br>CUDA i cuDNN na hoście | O (menedżer pakietów apt) | X (używamy gotowych, wstępnie zainstalowanych<br> obrazów od NVIDIA z [Docker Hub](https://hub.docker.com/r/nvidia/cuda), więc nie trzeba robić tego ręcznie) |
| Przenośność | Przy migracji na inny system trzeba<br> odtwarzać środowisko od zera | Dzięki Dockerowi: można w razie potrzeby<br> budować nowe obrazy z Dockerfile lub łatwo<br> przenosić dotychczas używany obraz<br>(z pominięciem dodatkowych wolumenów i ustawień sieci) |
| Dodatkowe <br>biblioteki GPU poza cuDNN | X | Wdrożenie: [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), [DALI](https://developer.nvidia.com/DALI) |
| Interfejs Jupyter Notebook | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| Konfiguracja serwera SSH | Nie omawiana | Zawiera podstawową konfigurację SSH |

## 0. Wstępne sprawdzenia

- [NVIDIA Container Toolkit można używać na dystrybucjach Linuksa wspierających menedżery pakietów Apt, Yum/Dnf lub Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Pod linkiem można sprawdzić listę wspieranych dystrybucji. Fedora nie jest osobno wyszczególniona w oficjalnej tabeli, ale jako że bazuje na Red Hat Linux (podobnie jak RHEL), działa bez problemu. Jeśli nie czujesz się pewnie w Linuksie i nie wiesz, którą dystrybucję wybrać, najbezpieczniejszym wyborem będzie Ubuntu LTS. Dodatkowo automatycznie instalowane są także zamknięte (proprietary) sterowniki, co bywa wygodne dla początkujących; a z racji dużej popularności większość dokumentacji technicznej jest pisana pod Ubuntu.
  - Architekturę systemu i wersję dystrybucji Linuksa można sprawdzić w terminalu poleceniem `uname -m && cat /etc/*release`.
- Najpierw trzeba upewnić się, że karta graficzna w systemie wspiera wersje CUDA i cuDNN, których chcesz używać.
  - Model GPU w komputerze można sprawdzić w terminalu poleceniem `lspci | grep -i nvidia`.
  - Na stronie <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> sprawdź dla danej wersji cuDNN: **wspierane wersje sterownika NVIDIA**, wymagane **CUDA Compute Capability**, oraz listę **wspieranego sprzętu NVIDIA**.
  - Na liście GPU pod adresem <https://developer.nvidia.com/cuda-gpus> znajdź swój model i sprawdź wartość **Compute Capability**. Musi ona spełniać wymaganie **CUDA Compute Capability** z poprzedniego kroku, aby CUDA i cuDNN działały bez problemu.

> Jeśli planujesz zakup nowej karty do deep learningu, kryteria doboru GPU są dobrze zebrane w następującym tekście (autor aktualizuje go nieregularnie).  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> Jeśli potrzebujesz również poradnika doboru całej konfiguracji sprzętowej, bardzo wartościowy jest też wpis tego samego autora: [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/).
{: .prompt-tip }

Jeśli spełniasz wszystkie powyższe warunki, przejdźmy do konfiguracji środowiska.

## 1. Instalacja sterownika graficznego NVIDIA

Najpierw należy zainstalować sterownik graficzny NVIDIA na hoście. Można pobrać i użyć instalatora `.run` ze strony [NVIDIA Driver Downloads](https://www.nvidia.com/drivers/), ale z punktu widzenia zarządzania wersjami i utrzymania zdecydowanie lepiej jest skorzystać z menedżera pakietów danej dystrybucji. Zainstaluj sterownik odpowiedni dla Twojego systemu, kierując się oficjalną dokumentacją: <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>. 

### Moduł proprietary vs moduł open-source

Sterownik NVIDIA dla Linuksa składa się z kilku modułów jądra; począwszy od sterownika w wersji 515 i kolejnych wydań NVIDIA dostarcza dwa typy modułów jądra:

- Proprietary: zamknięty sterownik, który NVIDIA dostarczała tradycyjnie.
- Open-source: sterownik open source na licencji dual MIT/GPLv2. Kod jest publiczny na <https://github.com/NVIDIA/open-gpu-kernel-modules>.

Sterownik proprietary jest dostarczany dla GPU projektowanych w oparciu o architektury od Maxwell do wersji sprzed Blackwell; od architektury Blackwell wsparcie ma zostać zakończone.  
Z kolei sterownik open-source wspiera architektury Turing i nowsze.

[NVIDIA zaleca używanie otwartoźródłowych modułów jądra, jeśli to możliwe.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
Kompatybilność Twojego GPU z otwartym sterownikiem można sprawdzić pod [tym linkiem](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

W tym wpisie zakładam instalację sterownika open-source.

### Debian i Ubuntu

W Ubuntu lub Debianie zainstaluj w terminalu:

```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Dla Fedora 40 opisuję instalację paczek prebuild z [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Konfiguracja repozytoriów RPM Fusion

Postępuj zgodnie z [oficjalnym przewodnikiem RPM Fusion](https://rpmfusion.org/Configuration).  
W terminalu uruchom:

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> W starszych wersjach DNF (Fedora 40 i wcześniejsze) druga linia — włączanie repozytorium biblioteki openh264 — wyglądała tak:
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> Jednak od DNF 5 (Fedora 41+) zamiast tego polecenia należy użyć:
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> i zgodnie z tym zaktualizowałem treść wpisu.
{: .prompt-info }

#### 1-Fedora-2. Instalacja pakietu akmod-nvidia

Kierując się [poradnikiem instalacji sterowników NVIDIA z RPM Fusion](https://rpmfusion.org/Howto/NVIDIA), zainstaluj pakiet akmod-nvidia.

```bash
sudo dnf update  # jeśli na tym etapie była aktualizacja jądra, zrestartuj do najnowszego kernela i dopiero kontynuuj
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> Podobnie, w starszych wersjach DNF (Fedora 40 i wcześniejsze) trzecia linia — zapobieganie usunięciu sterownika NVIDIA przez autoremove — wyglądała tak:
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> Jednak od DNF 5 (Fedora 41+) zamiast tego należy użyć:
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> i zgodnie z tym zaktualizowałem treść wpisu.
{: .prompt-info }

> Z kolei RPM Fusion historycznie prezentowało negatywne stanowisko wobec [otwartoźródłowych modułów jądra NVIDIA](#moduł-proprietary-vs-moduł-open-source) i domyślnie dostarczało sterowniki proprietary, o ile nie wskazano inaczej. Jednak zgodnie z [niedawnymi (grudzień 12025) wytycznymi RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), dla sprzętu wspieranego podwójnie (architektury od Turing do wersji sprzed Blackwell) system ma automatycznie wybierać lepszy wariant, więc nie trzeba już ręcznie decydować. Dla architektur sprzed Turing oraz dla Blackwell i nowszych i tak od początku była tylko jedna opcja, więc tu nic się nie zmienia.
> W związku z tym potwierdziłem, że usunięto opis ustawienia opcji wyboru modułu open-source przez `/etc/rpm/macros.nvidia-kmod`.
>
> Dodano też uwagę, że pakietu `akmod-nvidia-open` nie należy używać, o ile nie ma potrzeby samodzielnego nakładania downstreamowych zmian na sterownik w przestrzeni jądra.
>
> Te informacje również uwzględniłem w treści wpisu.
{: .prompt-info }

#### 1-Fedora-3. Rejestracja klucza, aby sterownik ładował się poprawnie przy Secure Boot

> Jeśli wykonasz poniższe dodatkowe kroki, możesz korzystać ze sterownika NVIDIA przy włączonym Secure Boot. Wyłączenie Secure Boot istotnie osłabia bezpieczeństwo systemu, więc zalecam go nie wyłączać. Przynajmniej w latach 12020+ rzadko jest sens wyłączać Secure Boot.
{: .prompt-danger }

Najpierw zainstaluj narzędzia:

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Następnie wygeneruj klucz:

```bash
sudo kmodgenca -a
```

Teraz trzeba zarejestrować wygenerowany klucz w MOK firmware’u UEFI:

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

Po uruchomieniu polecenia pojawi się prośba o hasło do rejestracji klucza. Za chwilę zrestartujesz system, aby dokończyć rejestrację — będzie to jednorazowe hasło użyte podczas procesu, więc ustaw takie, które zapamiętasz.

Zrestartuj system:

```bash
systemctl reboot
```

Podczas bootowania automatycznie pokaże się okno zarządzania MOK. Wybierz „Enroll MOK”, a następnie kolejno „Continue” i „Yes”; pojawi się ekran proszący o hasło — wpisz hasło ustawione przed chwilą. Po zakończeniu rejestracji wybierz reboot, aby uruchomić system ponownie; sterownik NVIDIA powinien załadować się poprawnie.

### Weryfikacja instalacji sterownika NVIDIA

W terminalu wykonaj:

```bash
cat /proc/driver/nvidia/version
```

Jeśli zobaczysz komunikat podobny do poniższego, instalacja przebiegła poprawnie.

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

Dodatkowo: w świecie Linuksa często domyślnie używa się otwartoźródłowego sterownika nouveau (moduł jądra). Po instalacji sterownika NVIDIA nouveau powinien zostać wyłączony — w przeciwnym razie może powodować problemy. Po instalacji sterownika NVIDIA i restarcie, poniższe polecenie nie powinno zwrócić żadnego wyniku:

```bash
lsmod |grep nouveau
```

## 2. Instalacja NVIDIA Container Toolkit

Teraz zainstaluj [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Postępuj według [oficjalnego przewodnika instalacji NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), ale w przypadku Fedory zwróć uwagę na dodatkowe uwagi — przeczytaj tę sekcję do końca, zanim zaczniesz.

### Dla Apt (Ubuntu, Debian itd.)

#### 2-Apt-1. Konfiguracja repozytorium do pobierania pakietów

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Aktualizacja listy pakietów

```bash
sudo apt update
```

#### 2-Apt-3. Instalacja pakietu

```bash
sudo apt install nvidia-container-toolkit
```

### Dla Yum/Dnf (Fedora, RHEL, Centos itd.)

> Podczas testów na Fedora 40 okazało się, że w przeciwieństwie do Ubuntu polecenie `nvidia-smi` oraz pakiet `nvidia-persistenced` nie są domyślnie częścią sterownika NVIDIA — musiałem doinstalować `xorg-x11-drv-nvidia-cuda`. Nie testowałem bezpośrednio na RHEL i Centos, ale konfiguracja systemu jest dość podobna do Fedory, więc jeśli po przejściu przez poniższy poradnik pojawią się problemy, warto spróbować tej samej metody.
{: .prompt-warning }

> Na Fedora 40 po instalacji `xorg-x11-drv-nvidia-cuda` i uruchomieniu przykładowego workloadu u mnie wszystko działało. Jeśli mimo to nadal pojawiają się problemy (np. przez SELinux), pomocny może być [dedykowany dla Fedory pakiet i przewodnik nvidia-container-toolkit od grupy Fedora AI-ML](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/).
{: .prompt-tip }

#### 2-Dnf-1. Konfiguracja repozytorium do pobierania pakietów

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Instalacja pakietu

```bash
sudo dnf install nvidia-container-toolkit
```

albo

```bash
sudo yum install nvidia-container-toolkit
```

### Dla Zypper (openSUSE, SLES)

#### 2-Zypper-1. Konfiguracja repozytorium do pobierania pakietów

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalacja pakietu

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalacja silnika kontenerów

Następnie zainstaluj jako silnik kontenerów Docker CE albo Podman. Wybierz jedno z nich zgodnie z warunkami i preferencjami; skorzystaj z [oficjalnej dokumentacji Docker](https://docs.docker.com/engine/install/) oraz [oficjalnej dokumentacji Podman](https://podman.io/docs/installation).

Poniższa tabela podsumowuje główne różnice i zalety/wady Dockera i Podmana.

| Kryterium | Docker | Podman |
| --- | --- | --- |
| Architektura | Model klient–serwer, oparty o demona (daemon) | Architektura bez demona (daemonless) |
| Bezpieczeństwo | Zależy od demona uruchamianego domyślnie z uprawnieniami root, co niesie potencjalne ryzyko<br>(od wersji 20.10 z 12020 wspiera tryb rootless, ale wymaga dodatkowej konfiguracji) | Bez zależności od demona; domyślnie działa rootless (o ile nie ustawisz inaczej),<br> chroniony przez SELinux |
| Zużycie zasobów | Ze względu na proces demona działający w tle<br> zwykle większe | Zwykle mniejszy narzut (overhead) |
| Czas startu kontenera | Relatywnie wolniejszy | Uproszczona architektura — uruchamianie nawet o ~50% szybsze |
| Ekosystem i dokumentacja | Bardzo szeroki ekosystem i wsparcie społeczności,<br> bogata dokumentacja | Mniejszy ekosystem i mniej materiałów |
| Sieć | Docker Bridge Network | Wtyczki CNI (Container Network Interface) |
| Natywne wsparcie<br>dla YAML Kubernetes | X (wymaga konwersji) | O |

Materiały:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker jest starszy i przez długi czas miał status de facto standardu, więc jego największą zaletą jest szeroki ekosystem i obfita dokumentacja.  
Podman został opracowany stosunkowo niedawno przez Red Hat; z założenia stawia na architekturę daemonless i rootless, dzięki czemu ma przewagi w bezpieczeństwie, zużyciu zasobów oraz czasie startu kontenerów. Kolejną mocną stroną Podmana jest to, że — w przeciwieństwie do Dockera — awaria demona nie „kładzie” wszystkich kontenerów naraz: każdy kontener działa w pełni niezależnie, więc awaria jednego nie wpływa na pozostałe.

Najważniejsze jest dobranie narzędzia do własnych warunków, ale dla osób zaczynających przygodę wydaje się, że dobrym wyborem będzie start od Podmana. Choć jego ekosystem jest mniejszy niż Dockera, dzięki opisanym zaletom szybko rośnie i zmniejsza dystans; jest też kompatybilny z wieloma elementami świata Dockera (składnia Dockerfile, obrazy, CLI). Jeśli nie masz powodu typu: „już mam zbudowany duży system oparty o Dockera i przejście na Podmana byłoby kosztowne”, to wybór Podmana od początku bywa najbardziej racjonalny.

### Podman

Wspierany w domyślnych repozytoriach większości głównych dystrybucji Linuksa, więc instalacja jest prosta.

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

#### Sprawdzenie, czy działa poprawnie

W terminalu uruchom:

```bash
podman run --rm hello-world
```

Jeśli zobaczysz poniższą wiadomość, to działa.

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

> Podczas testów (12025-12-18T00:43:00+09:00) w środowisku: podman 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`, Fedora 43 — przy uruchamianiu hello-world oraz przy uruchamianiu kontenerów lub budowie obrazów pojawiał się błąd:
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> Nie używam IPv6 i działam w sieci IPv4, a mimo to na etapie konfiguracji sieci kontenera pasta (w składzie biblioteki passt) próbuje ustawić routing IPv6, co wygląda na źródło problemu. Potwierdziłem, że jeśli przy uruchamianiu kontenera lub na etapie [później omawianego budowania obrazu](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-budowanie-obrazu-docker-i-uruchamianie-kontenera) jawnie wymuszę IPv4 przez opcję `--net=pasta:-4`, problem nie występuje:
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> Znalazłem też [wcześniej zgłoszony issue o identycznych objawach](https://github.com/containers/podman/issues/22824). W issue podano, że naprawa została wdrożona w [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/), ale ze względu na zbieżność symptomów oraz to, że problem występował przy użyciu Proton VPN, podejrzewam, że podobny błąd mógł powrócić.
{: .prompt-warning }

### Docker CE

#### Ubuntu

##### 3-Ubuntu-1. Usunięcie starych/nieoficjalnych pakietów, aby uniknąć konfliktów

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Konfiguracja repozytorium

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

##### 3-Ubuntu-3. Instalacja pakietów

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Utworzenie grupy `Docker` i dodanie użytkownika

Aby użytkownik non-root mógł zarządzać Dockerem bez `sudo`, utwórz grupę `Docker` i dodaj do niej użytkownika, który ma używać Dockera:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Następnie wyloguj się i zaloguj ponownie, aby zmiany weszły w życie. W Ubuntu i Debianie usługa Dockera zwykle startuje automatycznie przy bootowaniu bez dodatkowych kroków.

#### Fedora

##### 3-Fedora-1. Usunięcie starych/nieoficjalnych pakietów, aby uniknąć konfliktów

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

##### 3-Fedora-2. Konfiguracja repozytorium

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Instalacja pakietów

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

W trakcie instalacji pojawi się pytanie o zatwierdzenie klucza GPG. Jeśli klucz GPG jest zgodny z `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, wpisz `y`, aby zatwierdzić.  
> Jeśli klucz GPG się nie zgadza, może to oznaczać atak na łańcuch dostaw (supply chain) i pobranie podrobionego pakietu — należy przerwać instalację.
{: .prompt-danger }

##### 3-Fedora-4. Uruchomienie demona Dockera

Docker jest już zainstalowany, ale jeszcze nie działa; uruchom go:

```bash
sudo systemctl start docker
```

Aby usługa Dockera uruchamiała się automatycznie przy starcie systemu:

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Dodanie użytkownika do grupy `Docker`

Aby użytkownik non-root mógł zarządzać Dockerem, dodaj go do grupy `Docker`. Na Fedorze grupa `Docker` jest zwykle tworzona automatycznie podczas instalacji, więc wystarczy dodać użytkownika:

```bash
sudo usermod -aG docker $USER
```

Wyloguj się i zaloguj ponownie, aby zmiany zadziałały.

#### Sprawdzenie, czy działa poprawnie

W terminalu uruchom:

```bash
docker run hello-world
```

Jeśli pojawi się wiadomość jak poniżej, to działa.

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

## Dalsza lektura
Ciąg dalszy w: [Część 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
