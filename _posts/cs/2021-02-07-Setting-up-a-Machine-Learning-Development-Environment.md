---
title: "Vybudování vývojového prostředí pro strojové učení"
description: "Tento článek popisuje, jak na lokálním počítači vybudovat vývojové prostředí pro studium strojového učení. Vše je psáno pro Ubuntu 20.04 LTS a GPU NVIDIA GeForce RTX 3070."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, CUDA, PyTorch, TensorFlow]
image: /assets/img/technology.webp
---

## Přehled

Tento článek se zabývá tím, jak vybudovat vývojové prostředí, které lze považovat za první krok ke studiu strojového učení na lokálním počítači. Veškerý obsah byl sepsán pro Ubuntu 20.04 LTS a grafickou kartu NVIDIA Geforce RTX 3070.

- Budovaný technologický stack
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
  - framework pro hluboké učení (doporučuje se zvolit a nainstalovat pouze jeden na každé prostředí)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

### Srovnávací tabulka s nově napsaným průvodcem pro vybudování ML vývojového prostředí

Přestože od nahrání na blog uběhly zhruba tři a půl roku, obsah tohoto článku je stále ve velkých rysech platný — až na několik detailů, jako jsou verze balíčků nebo vydání open-source driverů NVIDIA. V létě roku 12024 (podle [holocénního kalendáře](https://en.wikipedia.org/wiki/Holocene_calendar)) jsem si ale pořídil nový PC a při budování prostředí došlo k několika změnám, proto jsem sepsal [nový návod na vybudování vývojového prostředí](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/). Změny jsou v tabulce níže.

| Rozdíl | Tento článek (verze 12021) | Nový článek (verze 12024) |
| --- | --- | --- |
| Linuxová distribuce | Vychází z Ubuntu | Kromě Ubuntu použitelný i na Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES apod. |
| Způsob vybudování prostředí | Python virtuální prostředí pomocí venv | Prostředí na bázi Docker kontejnerů pomocí<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalace NVIDIA grafického ovladače | O | O |
| Přímá instalace <br>CUDA a cuDNN na hostitelský systém | O (použití správce balíčků apt) | X (používají se předpřipravené<br> image od NVIDIA na [Docker Hubu](https://hub.docker.com/r/nvidia/cuda), takže není nutný ruční zásah) |
| Přenositelnost | Při přesunu na jiný systém je nutné<br> prostředí znovu vybudovat | Díky Dockeru lze podle připraveného Dockerfile<br> kdykoli sestavit nový image, nebo snadno přenést<br> dříve používaný image (mimo dodatečné volumes či síťová<br> nastavení) |
| Využití dalších <br>GPU akceleračních knihoven mimo cuDNN | X | Zavedení [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Rozhraní Jupyter Notebook | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| Nastavení SSH serveru | Neřeší se samostatně | Ve 3. dílu zahrnuje základní konfiguraci SSH serveru |

Pokud chcete místo Dockeru používat Python virtuální prostředí typu venv, i tento původní článek je stále použitelný, takže můžete pokračovat ve čtení. Pokud chcete využít výhody Docker kontejnerů, jako je vysoká přenositelnost, plánujete používat jinou distribuci než Ubuntu (např. Fedora), máte prostředí s NVIDIA GPU a chcete používat další GPU akcelerační knihovny jako CuPy, cuDF, cuML, DALI, nebo se chcete připojovat vzdáleně přes SSH a JupyterLab, doporučuji nahlédnout i do [nového průvodce](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/).

## 0. Předběžná kontrola

- Pro studium strojového učení se doporučuje používat Linux. Ve Windows to sice jde také, ale v různých drobnostech může docházet k výrazným časovým ztrátám. Nejbezpečnější volbou je používat nejnovější Ubuntu LTS. Proprietární (ne open-source) ovladače se navíc instalují automaticky, což je pohodlné, a díky velkému počtu uživatelů je většina technické dokumentace psána právě pro Ubuntu.
- Obecně platí, že Ubuntu a většina linuxových distribucí má Python předinstalovaný. Pokud však Python nainstalovaný nemáte, před postupem podle tohoto článku jej nejprve nainstalujte.
  - Nainstalovanou verzi Pythonu lze ověřit následujícím příkazem:
    ```
    $ python3 --version
    ```
  - Pokud budete používat TensorFlow 2 nebo PyTorch, je nutné ověřit kompatibilní verzi Pythonu. K době psaní tohoto článku [nejnovější verze PyTorch podporuje Python](https://pytorch.org/get-started/locally/#linux-python) 3.6–3.8 a [nejnovější TensorFlow 2 podporuje Python](https://www.tensorflow.org/install) 3.5–3.8.  
  V tomto článku používám Python 3.8.
- Pokud plánujete studovat strojové učení na lokálním počítači, je vhodné mít k dispozici alespoň jednu GPU. Předzpracování dat se dá zvládnout i na CPU, ale ve fázi trénování modelu je s rostoucí velikostí modelu rozdíl v rychlosti mezi CPU a GPU drtivý (zejména u deep learningu).
  - Pro strojové učení je volba výrobce GPU prakticky jen jedna: je potřeba použít NVIDIA. NVIDIA do oblasti strojového učení dlouhodobě významně investuje a téměř všechny ML frameworky využívají knihovnu CUDA od NVIDIA.
  - Pokud chcete pro ML používat GPU, nejprve ověřte, že vaše grafická karta podporuje CUDA. Název modelu GPU v počítači lze zjistit v terminálu příkazem `uname -m && cat /etc/*release`. V seznamu GPU na tomto [odkazu](https://developer.nvidia.com/cuda-gpus) najděte svůj model a ověřte hodnotu **Compute Capability**. Aby bylo možné CUDA používat, musí být alespoň 3.5.
  - Kritéria pro výběr GPU jsou dobře shrnuta v následujícím článku, který autor průběžně aktualizuje:  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  Velmi přínosný je i článek [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/). Závěr prvního článku je následující:
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

Pokud splňujete všechny výše uvedené body, můžeme začít s budováním pracovního prostředí.

## 1. Vytvoření pracovního adresáře

Otevřete terminál a upravte soubor `.bashrc`, abyste zaregistrovali proměnnou prostředí (to, co následuje za promptem `$`, je příkaz).  
Nejprve otevřete editor nano následujícím příkazem (vim či jiný editor je také v pořádku).

```
$ nano ~/.bashrc
```

Na poslední řádek přidejte následující obsah. Cestu v uvozovkách můžete dle potřeby změnit.  
`export ML_PATH="$HOME/ml"`

Uložte pomocí Ctrl+O a ukončete Ctrl+X.

Nyní aplikujte proměnné prostředí následujícím příkazem.

```
$ source ~/.bashrc
```

Vytvořte adresář.

```
$ mkdir -p $ML_PATH
```

## 2. Instalace správce balíčků pip

Způsobů, jak nainstalovat Python balíčky potřebné pro strojové učení, je více. Můžete použít vědeckou Python distribuci jako Anaconda (doporučeno ve Windows), nebo použít samotný Python balíčkovací nástroj pip. Zde budeme používat příkaz pip v bash shellu na Linuxu nebo macOS.

Zkontrolujte, zda je v systému pip nainstalován:

```
$ pip3 --version

Příkaz „pip3“ nebyl nalezen, ale lze jej nainstalovat pomocí:

sudo apt install python3-pip

```

Pokud se zobrazí výše uvedené, pip v systému nainstalován není. Nainstalujte jej pomocí správce balíčků systému (zde apt) (pokud se zobrazí číslo verze, pip už nainstalovaný je a tento krok přeskočte).

```
$ sudo apt install python3-pip
```

Nyní je pip v systému nainstalován.

## 3. Vytvoření izolovaného virtuálního prostředí (doporučeno)

Pro vytvoření virtuálního prostředí (aby se předešlo konfliktům verzí knihoven mezi různými projekty) nainstalujte venv.

```
$ sudo apt install python3-venv
```

Poté vytvořte izolované Python prostředí následovně. Důvodem je to, že různé projekty vyžadují různé verze knihoven; proto je vhodné při zahájení každého nového projektu vytvořit nové virtuální prostředí.

```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(název prostředí)
```

Pro aktivaci virtuálního prostředí otevřete terminál a zadejte:

```
$ cd $ML_PATH
$ source ./(název prostředí)/bin/activate
```

Po aktivaci virtuálního prostředí upgradujte pip uvnitř prostředí:

```
(env) $ pip install -U pip
```

Později lze virtuální prostředí deaktivovat příkazem `deactivate`. Pokud je prostředí aktivní, jakýkoli balíček nainstalovaný přes pip se nainstaluje do tohoto izolovaného prostředí a Python jej bude používat.

## 3′. (Pokud virtuální prostředí nevytváříte) Upgrade verze pip

Při instalaci pip do systému se stáhne a nainstaluje binární soubor z mirror serverů distribuce (zde Ubuntu). Tyto binárky se obvykle aktualizují se zpožděním, takže často nejde o nejnovější verzi (v mém případě se nainstalovala verze 20.3.4). Chcete-li používat nejnovější pip, spusťte následující příkaz a nainstalujte (nebo upgradujte) pip do *domovského adresáře uživatele*.  

```
$ python3 -m pip install -U pip

Collecting pip
(…)
Successfully installed pip-21.0.1
```

Je vidět, že pip byl nainstalován ve verzi 21.0.1, která byla v době psaní článku nejnovější. Pip nainstalovaný do domovského adresáře ovšem systém automaticky nerozpozná, proto je potřeba přidat jej do proměnné prostředí PATH.

Znovu otevřete soubor `.bashrc` v editoru.

```
$ nano ~/.bashrc
```

Tentokrát najděte řádek začínající `export PATH=`. Pokud za ním není žádná cesta, stačí přidat obsah stejně jako v [kroku 1](#1-vytvoření-pracovního-adresáře). Pokud už jsou zaregistrovány jiné cesty, přidejte další pomocí dvojtečky.  
`export PATH="$HOME/.local/bin"`  
`export PATH="(stávající cesta):$HOME/.local/bin"`

[Pokud upgradujete systémový pip jinou metodou než přes systémového správce balíčků, může to způsobit problémy kvůli konfliktům verzí](https://github.com/pypa/pip/issues/5599). Proto se pip instaluje samostatně do domovského adresáře uživatele. Ze stejného důvodu je mimo virtuální prostředí vhodné používat místo příkazu `pip` raději `python3 -m pip`.

## 4. Instalace balíčků pro strojové učení (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)

Následujícím pip příkazem nainstalujte všechny potřebné balíčky i jejich závislosti.  
V mém případě používám venv, takže jsem použil přímo `pip`. Pokud ale venv nepoužíváte, jak bylo zmíněno výše, doporučuje se místo toho použít `python3 -m pip`.

```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(…)
```

Pokud používáte venv, zaregistrujte kernel do Jupyteru a nastavte název.

```
(env) $ python3 -m ipykernel install --user --name=(název kernelu)
```

Od této chvíle Jupyter spustíte následovně:

```
(env) $ jupyter notebook
```

## 5. Instalace CUDA & cuDNN

### 5-1. Ověření požadovaných verzí CUDA & cuDNN

V [oficiální dokumentaci PyTorch](https://pytorch.org/get-started/locally/) ověřte podporované verze CUDA.  
![Ověření kompatibilní verze CUDA pro PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
Pro PyTorch 1.7.1 jsou podporované verze CUDA 9.2, 10.1, 10.2 a 11.0. Pro GPU řady NVIDIA 30 je potřeba CUDA 11, takže vidíme, že je vyžadována verze 11.0.

V [oficiální dokumentaci TensorFlow 2](https://www.tensorflow.org/install/gpu) také ověřte požadované verze CUDA.  
![Ověření kompatibilní verze CUDA pro TensorFlow2](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
Pro TensorFlow 2.4.0 jsem ověřil, že je stejně potřeba CUDA 11.0 a cuDNN 8.0.

Já podle situace někdy používám PyTorch a jindy TensorFlow 2, proto jsem ověřil verze CUDA kompatibilní s oběma balíčky. Vy si ověřte požadavky balíčku, který potřebujete, a přizpůsobte se jim.

### 5-2. Instalace CUDA

Přejděte na [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive), vyberte verzi, kterou jste ověřili výše, a otevřete ji. V tomto článku vybereme [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
Nyní zvolte odpovídající platformu a typ instalátoru a postupujte podle instrukcí na obrazovce. V tomto bodě se [doporučuje používat pokud možno systémového správce balíčků](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). Moje preferovaná volba je deb (network).  
![Výběr platformy pro CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)  
![Instalace CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)  

Spusťte následující příkazy pro instalaci CUDA:

```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```

Pokud jste pozorní, všimnete si, že poslední řádek se mírně liší od instrukcí na obrázku. Při síťové instalaci, pokud zadáte pouze `cuda` podle obrázku, nainstaluje se nejnovější verze 11.2, což nechceme. V [instalační příručce CUDA 11.0 pro Linux](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas) si můžete prohlédnout různé volby meta balíčků. Zde jsem upravil poslední řádek tak, aby se nainstaloval CUDA Toolkit konkrétně ve verzi 11.0, zatímco balíček ovladačů se mohl automaticky aktualizovat.

### 5-3. Instalace cuDNN

Nainstalujte cuDNN následovně:

```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```

## 6. Instalace PyTorch

Pokud jste v kroku 3 vytvořili virtuální prostředí, pokračujte s aktivovaným prostředím. Pokud PyTorch nepotřebujete, tento krok přeskočte.  
Přejděte na [web PyTorch](https://pytorch.org/get-started/locally/), vyberte build (Stable), operační systém (Linux), balíček (Pip), jazyk (Python) a CUDA (11.0) a postupujte podle zobrazených instrukcí.  
![Instalace PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)

```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

Pro ověření správné instalace PyTorch spusťte Python interpret a proveďte následující příkazy. Pokud se vrátí tensor, instalace je úspěšná.

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

Pro ověření, že GPU ovladač a CUDA jsou aktivní a dostupné, spusťte:

```
>>> torch.cuda.is_available()
True
```

## 7. Instalace TensorFlow 2

Pokud TensorFlow nepotřebujete, tento krok ignorujte.  
Pokud jste v kroku 6 nainstalovali PyTorch do virtuálního prostředí, toto prostředí deaktivujte a vraťte se ke krokům 3 a 4: vytvořte nové virtuální prostředí, aktivujte jej a pokračujte. Pokud jste krok 6 přeskočili, pokračujte rovnou dál.  
TensorFlow nainstalujte takto:

```
(env2) $ pip install --upgrade tensorflow
```

Pro ověření správné instalace TensorFlow spusťte následující příkaz. Pokud se zobrazí název GPU a vrátí se tensor, je vše v pořádku.

```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
(중략)
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```
