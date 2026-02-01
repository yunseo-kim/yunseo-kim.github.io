---
title: "Vybudování vývojového prostředí pro hluboké učení pomocí NVIDIA Container Toolkit a Dockeru/Podmanu (1) – Instalace NVIDIA Container Toolkit a kontejnerového enginu"
description: "Tato série popisuje, jak na lokálním stroji vytvořit kontejnerové vývojové prostředí pro deep learning pomocí NVIDIA Container Toolkit a jak jej připravit pro vzdálené použití přes SSH a JupyterLab. Tento první díl se zaměřuje na instalaci NVIDIA Container Toolkit a kontejnerového enginu."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Přehled

V této sérii nainstalujeme NVIDIA Container Toolkit a Docker nebo Podman a na základě obrazů CUDA a cuDNN poskytovaných v repozitáři [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) na Docker Hubu napíšeme Dockerfile, abychom vybudovali vývojové prostředí pro hluboké učení. Aby si to kdokoli mohl snadno převzít a použít, sdílím výsledný [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) a [obrazy](https://hub.docker.com/r/yunseokim/dl-env/tags) přes GitHub a Docker Hub a navíc poskytuji průvodce nastavením SSH a JupyterLabu pro využití jako vzdálený server.  
Série bude mít 3 články a tento, který právě čtete, je první díl.
- 1. díl: NVIDIA Container Toolkit & instalace kontejnerového enginu (tento článek)
- [2. díl: Nastavení kontejnerového runtime pro využití GPU, psaní Dockerfile a build kontejnerového obrazu](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 3. díl (bude nahráno)

Postup předpokládá systém s NVIDIA GPU podporující CUDA v prostředí x86_64 Linux. Na distribucích jiných než Ubuntu nebo Fedora jsem to netestoval, takže některé detaily se mohou mírně lišit.  
(revize 12026.1.6.)

### Složení vývojového prostředí

- Hostitelský OS a architektura: x86_64, Linux (Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x apod.)
- Budovaný technologický stack (jazyky a knihovny)
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

  > Podle situace a vlastních preferencí lze zvážit použití knihovny DataFrame [Polars](https://pola.rs/) místo pandas. Je napsaná v Rustu a [při zpracování velkých dat sice zaostává za kombinací cuDF + pandas, ale oproti „čistému“ balíčku pandas má velmi výrazně lepší výkon](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/) a nabízí syntaxi více zaměřenou na dotazy. Podle oficiálního [blogu Polars](https://pola.rs/posts/polars-on-gpu/) a [dokumentace cuDF](https://docs.rapids.ai/api/cudf/stable/cudf_polars/) tým Polars ve spolupráci s NVIDIA RAPIDS poskytuje GPU akcelerační engine na bázi cuDF v otevřené betě a rychle na něm pracuje.
  {: .prompt-tip }

  > Pokud váháte, zda použít Docker CE nebo Podman, může pomoci [srovnávací tabulka níže](#3-instalace-kontejnerového-enginu).
  {: .prompt-tip }

### Srovnání s dříve napsaným průvodcem pro vytvoření ML prostředí

V tomto blogu už existuje [původní průvodce vytvořením vývojového prostředí pro machine learning](/posts/Setting-up-a-Machine-Learning-Development-Environment), ale protože došlo k řadě změn, napsal jsem tento nový článek. Rozdíly shrnuje tabulka níže.

| Rozdíl | Původní článek (verze 12021) | Tento článek (napsáno 12024, revize 12026) |
| --- | --- | --- |
| Linux distribuce | Primárně Ubuntu | Kromě Ubuntu i Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES apod. |
| Způsob sestavení prostředí | Přímá instalace na hostiteli<br>Python virtuální prostředí přes venv | Kontejnerové prostředí na bázi Dockeru<br> pomocí [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br>Virtuální prostředí a správa balíčků přes uv |
| Instalace NVIDIA grafického ovladače | O | O |
| Přímá instalace <br>CUDA a cuDNN na hostitele | O (přes Apt) | X (používají se předinstalované<br> obrazy od NVIDIA na [Docker Hubu](https://hub.docker.com/r/nvidia/cuda), není potřeba nic ručně instalovat) |
| Přenositelnost | Při přesunu na jiný systém je nutné<br> znovu vybudovat celé prostředí | Protože jde o Docker, lze<br> kdykoli znovu buildit nový obraz z Dockerfile nebo<br> snadno přenést dříve používaný obraz<br>(kromě dodatečných volume či nastavení sítě) |
| Využití dalších <br>GPU akceleračních knihoven mimo cuDNN | X | Zavedení [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), [DALI](https://developer.nvidia.com/DALI) |
| Rozhraní Jupyter Notebooku | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| Nastavení SSH serveru | Není samostatně pokryto | Zahrnuje základní konfiguraci SSH serveru |

## 0. Předběžná kontrola

- [NVIDIA Container Toolkit lze používat na Linux distribucích podporujících balíčkové manažery Apt, Yum nebo Dnf, Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Na odkazované stránce lze ověřit seznam podporovaných distribucí. Ve oficiální tabulce není Fedora explicitně uvedena, ale protože je (stejně jako RHEL) postavená na Red Hat Linux základu, funguje bez problémů. Pokud nejste v Linuxu zběhlí a nejste si jistí, jakou distribuci zvolit, Ubuntu LTS je obvykle nejbezpečnější volba. Snadno se používá i pro začátečníky, protože se automaticky instalují i proprietární ovladače, a protože má velkou uživatelskou základnu, většina technické dokumentace je psána právě pro Ubuntu.
  - Architekturu systému a verzi Linux distribuce zjistíte v terminálu příkazem `uname -m && cat /etc/*release`.
- Nejdříve je potřeba ověřit, že GPU v systému podporuje verze CUDA a cuDNN, které chcete používat.
  - Model GPU nainstalované v počítači zjistíte v terminálu příkazem `lspci | grep -i nvidia`.
  - Na stránce <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> ověřte pro danou verzi cuDNN **podporovanou verzi NVIDIA ovladače** a požadovanou **CUDA Compute Capability** a také seznam **podporovaného NVIDIA hardwaru**.
  - Na <https://developer.nvidia.com/cuda-gpus> najděte svůj model GPU a ověřte hodnotu **Compute Capability**. Ta musí splňovat požadavek **CUDA Compute Capability** uvedený výše, aby CUDA i cuDNN fungovaly bez potíží.

> Pokud plánujete koupit novou GPU na deep learning, kritéria výběru jsou dobře shrnuta v následujícím článku (autor jej nepravidelně aktualizuje).  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> Pokud potřebujete i obecnější doporučení pro sestavu hardwaru, velmi užitečný je také článek [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) od stejného autora.
{: .prompt-tip }

Pokud splňujete všechny výše uvedené podmínky, můžeme začít sestavovat pracovní prostředí.

## 1. Instalace NVIDIA grafického ovladače

Nejprve je potřeba nainstalovat NVIDIA grafický ovladač na hostitelský systém. Můžete si stáhnout .run instalátor z [NVIDIA stránky pro stahování ovladačů](https://www.nvidia.com/drivers/), ale z hlediska správy verzí a údržby je lepší použít balíčkový manažer dané distribuce. S odkazem na oficiální dokumentaci <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> nainstalujte ovladač odpovídající vašemu prostředí.

### Proprietary modul vs Open-source modul

NVIDIA linuxový ovladač se skládá z několika kernelových modulů a od ovladače verze 515 (a novějších) NVIDIA poskytuje dva typy kernelových modulů ovladače:

- Proprietary: proprietární ovladač, který NVIDIA poskytovala tradičně.
- Open-source: open-source ovladač pod duální licencí MIT/GPLv2. Zdrojové kódy jsou zveřejněny na <https://github.com/NVIDIA/open-gpu-kernel-modules>.

Proprietary ovladač je poskytován pro GPU navržené na architekturách od Maxwell po období před Blackwell; od architektury Blackwell se jeho podpora plánuje ukončit.  
Naopak open-source ovladač je podporován pro architektury Turing a novější.

[NVIDIA doporučuje používat open-source kernelové moduly, pokud je to možné.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
Zda je vaše GPU kompatibilní s open-source ovladačem, ověříte na [tomto odkazu](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

V tomto článku budu předpokládat instalaci open-source ovladače.

### Debian & Ubuntu

V případě Ubuntu nebo Debianu nainstalujte v terminálu následujícími příkazy:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Pro Fedoru 40 ukážu instalaci předbuildovaných balíčků poskytovaných přes [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Nastavení RPM Fusion repozitářů

Postupujte podle [oficiálního průvodce RPM Fusion](https://rpmfusion.org/Configuration).  
V terminálu spusťte:

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> Ve starších verzích DNF (Fedora 40 a dříve) měl druhý řádek pro povolení repozitáře knihoven openh264 podobu:
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> Od DNF 5 (Fedora 41+) je však nutné místo toho použít:
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> a proto jsem text článku aktualizoval.
{: .prompt-info }

#### 1-Fedora-2. Instalace balíčku akmod-nvidia

Dle [instalačního návodu pro NVIDIA ovladač od RPM Fusion](https://rpmfusion.org/Howto/NVIDIA) nainstalujte balíček akmod-nvidia.

```bash
sudo dnf update  # pokud zde dojde k aktualizaci kernelu, nejprve rebootněte do nejnovějšího kernelu a pak pokračujte
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> Podobně ve starších verzích DNF (Fedora 40 a dříve) měl třetí řádek, který bránil odstranění ovladače při autoremove, podobu:
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> Od DNF 5 (Fedora 41+) je nutné místo toho použít:
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> což jsem v článku zohlednil.
{: .prompt-info }

> RPM Fusion v minulosti zastávalo vůči [NVIDIA open-source kernelovým modulům](#proprietary-modul-vs-open-source-modul) spíše negativní postoj a pokud jste nic neuvedli, poskytovalo ve výchozím nastavení proprietární ovladač. Podle [nedávno (prosinec 12025) změněných pokynů RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open) nyní pro hardware s duplicitní podporou (architektury od Turing po období před Blackwell) automaticky zvolí a poskytne lepší variantu, takže už není potřeba ručně vybírat. Pro starší architektury před Turingem a pro nejnovější architektury Blackwell a novější stejně vždy existovala jen jedna možnost, takže zde se nic nemění.
> Na základě toho jsem ověřil, že informace o volbě open-source modulů přes `/etc/rpm/macros.nvidia-kmod` byly odstraněny.
>
> Dále se uvádí, že balíček `akmod-nvidia-open` se nemá používat, pokud nepotřebujete přímo aplikovat downstream změny do kernel-space ovladače.
>
> Tyto body jsem také promítl do aktualizace textu.
{: .prompt-info }

#### 1-Fedora-3. Registrace klíče pro správné načtení ovladače při Secure Boot

> Po provedení níže popsaných doplňkových kroků lze Secure Boot běžně používat spolu s NVIDIA ovladačem. Vypnutí Secure Bootu výrazně oslabuje bezpečnost systému, proto jej nedoporučuji vypínat. Minimálně od začátku 12020s obvykle neexistuje dobrý důvod Secure Boot vypínat.
{: .prompt-danger }

Nejprve nainstalujte následující nástroje:

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Poté vytvořte klíč:

```bash
sudo kmodgenca -a
```

Nyní je potřeba zaregistrovat vytvořený klíč do MOK v UEFI firmwaru.

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

Po spuštění příkazu budete vyzváni k zadání hesla pro registraci klíče. Za chvíli budete rebootovat a toto jednorázové heslo budete potřebovat v průběhu registrace, takže zadejte něco, co si krátce zapamatujete.

Poté restartujte systém:

```bash
systemctl reboot
```

Během bootu se automaticky zobrazí okno správy MOK. Zvolte „Enroll MOK“, poté postupně „Continue“ a „Yes“; následně budete vyzváni k zadání hesla, které jste nastavili. Po zadání hesla bude registrace hotová. Poté zvolte reboot a po dalším startu by se měl NVIDIA ovladač načíst správně.

### Ověření instalace NVIDIA ovladače

V terminálu můžete ověřit aktuálně načtený NVIDIA kernelový modul:

```bash
cat /proc/driver/nvidia/version
```

Pokud se zobrazí zpráva podobná této, instalace je v pořádku:

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

Dále je potřeba, aby po instalaci NVIDIA ovladače byl vypnut open-source grafický ovladač `nouveau` (kernelový modul), který bývá v Linuxu často výchozí. Pokud by zůstal aktivní, může způsobovat problémy. Po instalaci ovladače a rebootu by následující příkaz neměl vypsat nic:

```bash
lsmod |grep nouveau
```

## 2. Instalace NVIDIA Container Toolkit

Nyní je potřeba nainstalovat [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Postupujte podle [oficiálního instalačního průvodce NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), ale v případě Fedory existují během instalace důležité poznámky — proto si nejdříve dočtěte tuto sekci až do konce a pak pokračujte.

### Pokud používáte Apt (Ubuntu, Debian apod.)

#### 2-Apt-1. Nastavení repozitáře pro stahování balíčků

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Aktualizace seznamu balíčků

```bash
sudo apt update
```

#### 2-Apt-3. Instalace balíčku

```bash
sudo apt install nvidia-container-toolkit
```

### Pokud používáte Yum nebo Dnf (Fedora, RHEL, Centos apod.)

> Při testování na Fedoře 40 jsem zjistil, že na rozdíl od Ubuntu nejsou příkaz `nvidia-smi` ani balíček `nvidia-persistenced` součástí základní instalace NVIDIA ovladače, takže bylo nutné doinstalovat balíček `xorg-x11-drv-nvidia-cuda`. RHEL ani Centos jsem přímo netestoval, ale protože mají se Fedorou velmi podobnou skladbu systému, pokud byste při postupu podle tohoto návodu narazili na problém, může pomoci zkusit stejný postup.
{: .prompt-warning }

> Na Fedoře 40 mi po instalaci `xorg-x11-drv-nvidia-cuda` a otestování na ukázkovém workloadu vše fungovalo. Pokud by přesto vznikaly potíže (např. kvůli SELinux), může pomoci [Fedora-specifický balíček a návod pro nvidia-container-toolkit](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) od Fedora AI-ML skupiny.
{: .prompt-tip }

#### 2-Dnf-1. Nastavení repozitáře pro stahování balíčků

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Instalace balíčku

```bash
sudo dnf install nvidia-container-toolkit
```

nebo

```bash
sudo yum install nvidia-container-toolkit
```

### Pokud používáte Zypper (openSUSE, SLES)

#### 2-Zypper-1. Nastavení repozitáře pro stahování balíčků

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalace balíčku

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalace kontejnerového enginu

Dále nainstalujte jako kontejnerový engine buď Docker CE, nebo Podman. Vyberte si podle svého prostředí a preferencí; postupujte podle [oficiální dokumentace Dockeru](https://docs.docker.com/engine/install/) a [oficiální dokumentace Podmanu](https://podman.io/docs/installation).

Následující tabulka shrnuje hlavní rozdíly, výhody a nevýhody Dockeru a Podmanu.

| Kritérium | Docker | Podman |
| --- | --- | --- |
| Architektura | Klient–server model, na bázi démona (daemon) | „Daemonless“ architektura |
| Bezpečnost | Spoléhá na démona běžícího ve výchozím stavu s root právy, <br>což představuje potenciální bezpečnostní riziko<br>(od verze 20.10 vydané v 12020 podporuje rootless<br>mód, ale vyžaduje dodatečné nastavení) | Bez závislosti na démonu; pokud nic neurčíte,<br> běží ve výchozím stavu rootless a je chráněn<br> SELinuxem |
| Spotřeba prostředků | Kvůli démonové architektuře běží v pozadí proces trvale,<br> typicky tedy spotřebovává více prostředků | Obvykle menší režie (overhead) |
| Čas startu kontejneru | Relativně pomalejší | Díky zjednodušené architektuře až o ~50 %<br> rychlejší spuštění |
| Ekosystém a dokumentace | Velmi rozsáhlý ekosystém a komunitní podpora,<br> bohatá dokumentace | Relativně menší ekosystém a méně dokumentace |
| Síťování | Docker Bridge Network | CNI (Container Network Interface)<br> pluginy |
| Nativní podpora Kubernetes YAML | X (vyžaduje převod) | O |

Zdroje:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker má delší historii a dlouho byl de facto průmyslovým standardem; největší výhodou je proto široký ekosystém a množství související dokumentace.  
Podman byl vyvinut relativně nedávno firmou Red Hat a díky své koncepci „daemonless“ a „rootless“ přináší výhody v oblasti bezpečnosti, spotřeby systémových prostředků i doby startu kontejnerů. Silnou stránkou Podmanu je i to, že na rozdíl od Dockeru (kde pád démona může shodit všechny kontejnery) jsou kontejnery plně nezávislé, takže pád jednoho kontejneru neovlivní ostatní.

Nejdůležitější je vybrat nástroj podle vlastních podmínek a potřeb, ale pro úplné začátečníky se jako dobrá volba jeví začít s Podmanem. I když je jeho ekosystém oproti Dockeru menší, díky výše uvedeným výhodám rychle roste a rozdíl se zmenšuje. Zároveň je v mnoha ohledech kompatibilní s Dockerem (Dockerfile syntaxe, Docker obrazy, CLI). Pokud už nemáte vybudovaný velký systém postavený na Dockeru, kde by přechod na Podman znamenal významné náklady, dává smysl zvolit Podman rovnou od začátku.

### Podman

Podman je v systémových repozitářích většiny hlavních Linux distribucí, takže jej lze nainstalovat jednoduše.

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

#### Ověření, že je vše nastaveno správně

V terminálu spusťte:

```bash
podman run --rm hello-world
```

Pokud se vypíše následující zpráva, je to v pořádku:

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

> Při testování v čase 12025-12-18T00:43:00+09:00 (podman 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`, Fedora 43) se při spuštění hello-world i při běhu kontejnerů nebo buildu obrazů objevila chyba:
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> Přestože IPv6 nepoužívám a jsem v IPv4 síti, při nastavování sítě kontejneru se zdá, že pasta (součást passt knihovny) zkouší nastavit IPv6 routování. Ověřil jsem, že při explicitním použití IPv4 přes volbu `--net=pasta:-4` problém nenastává — jak při spuštění kontejneru, tak i ve [fázi buildu obrazu popsané později](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-sestavení-oci-obrazu-a-spuštění-kontejneru).
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> Při hledání jsem našel [dříve nahlášený issue se stejnými příznaky](https://github.com/containers/podman/issues/22824). V issue se píše, že to bylo opraveno v [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/), ale vzhledem k tomu, že pozorované chování je stejné a také šlo o problém při použití Proton VPN, mám podezření, že se podobný issue znovu objevil.
{: .prompt-warning }

### Docker CE

#### Ubuntu

##### 3-Ubuntu-1. Odstranění starších nebo neoficiálních balíčků kvůli kolizím

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Nastavení repozitáře

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

##### 3-Ubuntu-3. Instalace balíčků

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Vytvoření skupiny `Docker` a přidání uživatele

Aby mohl Docker spravovat i non-root uživatel bez `sudo`, stačí vytvořit skupinu `Docker` a přidat do ní uživatele:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Poté se odhlaste a znovu přihlaste, aby se změny projevily. Na Ubuntu nebo Debianu se služba Docker obvykle spouští automaticky při bootu i bez dalších kroků.

#### Fedora

##### 3-Fedora-1. Odstranění starších nebo neoficiálních balíčků kvůli kolizím

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

##### 3-Fedora-2. Nastavení repozitáře

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Instalace balíčků

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Během instalace budete vyzváni k potvrzení GPG klíče. Pokud klíč odpovídá `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, potvrďte zadáním `y`.  
> Pokud se GPG klíč neshoduje, může jít o podvržený balíček stažený v rámci supply-chain útoku, a instalaci je nutné okamžitě přerušit.
{: .prompt-danger }

##### 3-Fedora-4. Spuštění Docker démona

Docker je nyní nainstalovaný, ale neběží. Spusťte jej:

```bash
sudo systemctl start docker
```

Chcete-li, aby se Docker spouštěl automaticky při bootu:

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Přidání uživatele do skupiny `Docker`

Aby mohl Docker spravovat i non-root uživatel, přidejte uživatele do skupiny `Docker`. Na Fedoře se skupina `Docker` vytvoří automaticky během instalace, takže stačí jen přidání uživatele:

```bash
sudo usermod -aG docker $USER
```

Poté se odhlaste a znovu přihlaste, aby se změny projevily.

#### Ověření, že je vše nastaveno správně

V terminálu spusťte:

```bash
docker run hello-world
```

Pokud se zobrazí zpráva jako níže, je to v pořádku:

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

## Další čtení
Pokračování v [dílu 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
