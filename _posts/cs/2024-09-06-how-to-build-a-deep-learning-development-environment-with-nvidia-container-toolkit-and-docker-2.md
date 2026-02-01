---
title: "Vybudování vývojového prostředí pro deep learning pomocí NVIDIA Container Toolkit a Docker/Podman (2) – nastavení kontejnerového runtime pro využití GPU, psaní Dockerfile a sestavení kontejnerového obrazu"
description: "Tato série popisuje, jak lokálně vybudovat kontejnerové vývojové prostředí pro deep learning pomocí NVIDIA Container Toolkit a následně nastavit SSH a JupyterLab pro využití jako vzdálený server. Tento příspěvek je druhým dílem a věnuje se psaní Dockerfile a sestavení kontejnerového obrazu."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Přehled

V této sérii se věnuji instalaci NVIDIA Container Toolkit a Dockeru nebo Podmanu a procesu sestavení vývojového prostředí pro deep learning: na základě CUDA a cuDNN obrazů poskytovaných v repozitáři [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) na Docker Hubu napíšu Dockerfile. Aby si to kdokoli mohl snadno převzít a používat, sdílím [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) a [obrazy](https://hub.docker.com/r/yunseokim/dl-env/tags) vytvořené tímto postupem přes GitHub a Docker Hub a navíc poskytuji návod na nastavení SSH a JupyterLabu pro využití jako vzdálený server.  
Série bude mít 3 články a tento, který právě čtete, je druhý díl.
- [Díl 1: Instalace NVIDIA Container Toolkit & kontejnerového enginu](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Díl 2: Nastavení kontejnerového runtime pro využití GPU, psaní Dockerfile a sestavení kontejnerového obrazu (tento článek)
- Díl 3 (bude doplněno)

Předpokládám systém v prostředí x86_64 Linux s NVIDIA grafickou kartou podporující CUDA; jiné distribuce než Ubuntu nebo Fedora jsem netestoval, takže některé detaily se mohou mírně lišit.  
(Revize 12026.1.6.)

> **Oznámení o opravě chyb**
>
> V první verzi tohoto článku nahrané v srpnu 12024 byly chyby v části [Psaní Dockerfile](#5-psaní-dockerfile) a také v některých obrazech sestavených z daného Dockerfile. Problémové body byly následující:
> - V části vytváření účtu `remote` bylo chybně nastaveno heslo: bylo uvedeno, že se lze přihlásit s počátečním heslem „000000“, ale ve skutečnosti to neplatilo (doplněno 12025.12.19: nyní už počáteční heslo není „000000“, proto si určitě ověřte [text níže](#5-4-nastavení-ssh-serveru-pro-vzdálený-přístup))
> - Při startu kontejneru se automaticky nespouštěl SSH démon
>
> Tyto problémy jsem zaznamenal v únoru 12025 a přibližně 16. února 12025 kolem 02:00 (KST, UTC+9) jsem problematický Dockerfile i Docker obrazy nahradil opravenými verzemi v [repozitáři GitHub](https://github.com/yunseo-kim/dl-env-docker) a na [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> Pokud jste Dockerfile nebo Docker obraz stáhli (pull) před tímto časem, nahraďte jej opravenou verzí.  
> Pokud někomu chybné informace způsobily zmatek, omlouvám se.
{: .prompt-info }

## Než začnete

Tento článek navazuje na [díl 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1). Pokud jste jej ještě nečetli, doporučuji nejprve začít předchozím dílem.

## 4. Nastavení kontejnerového runtime

### Pokud používáte Podman

[Nastavení pomocí CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> Ve starších verzích bylo nutné po první instalaci NVIDIA Container Toolkit a následně po každé změně konfigurace GPU zařízení nebo ovladačů (včetně upgrade verze) pokaždé ručně znovu generovat soubor podle CDI specifikace.
>
> Od NVIDIA Container Toolkit `v1.18.0` se však soubor CDI specifikace `/var/run/cdi/nvidia.yaml` automaticky vytváří a aktualizuje službou systemd `nvidia-cdi-refresh` v těchto případech:
> - při instalaci nebo upgradu NVIDIA Container Toolkit
> - při instalaci nebo upgradu ovladače NVIDIA GPU
> - při restartu systému
>
> Na rozdíl od dřívějška už tedy obvykle není potřeba dělat nic navíc. Tomu jsem přizpůsobil i text článku.
>
> Pozor: při odebrání GPU ovladače nebo při rekonfiguraci zařízení MIG `nvidia-cdi-refresh` nemusí situaci pokrýt, takže je potřeba ručně restartovat `nvidia-cdi-refresh.service` a tím vynutit regeneraci CDI specifikace.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> Pokud se NVIDIA Container Runtime hook používá současně s CDI, může to vést ke konfliktům. Pokud tedy existuje `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath}, smažte jej, nebo dávejte pozor, abyste kontejner nespouštěli se současně nastavenou proměnnou prostředí `NVIDIA_VISIBLE_DEVICES`.
{: .prompt-warning }

### Pokud používáte Docker

Vysvětlení je psané pro [rootless režim](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Konfigurace kontejnerového runtime příkazem `nvidia-ctk`

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

Tento příkaz upraví soubor `/etc/docker/daemon.json`{: .filepath} tak, aby Docker mohl využívat NVIDIA Container Runtime.

#### 4-Docker-2. Restart Docker démona

Aby se změněná konfigurace projevila, restartujte Docker démona.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. Konfigurace souboru `/etc/nvidia-container-runtime/config.toml`{: .filepath} příkazem `sudo nvidia-ctk`

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Ověření, že je vše správně nastaveno

Spusťte ukázkový CUDA kontejner.

Pokud používáte Podman, spusťte:

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Pokud používáte Docker, spusťte:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

Pokud se zobrazí výstup přibližně podobný tomuto, je to v pořádku:

```bash
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 555.58.02              Driver Version: 555.58.02      CUDA Version: 12.5     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3090        Off |   00000000:01:00.0  On |                  N/A |
|  0%   46C    P8             29W /  350W |     460MiB /  24576MiB |      2%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

## 5. Psaní Dockerfile

Napíšeme Dockerfile pro vývojové prostředí na základě CUDA a cuDNN obrazů z repozitáře [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) na Docker Hubu.

- Je třeba zvolit obraz s ohledem na požadovanou verzi CUDA a cuDNN, typ a verzi linuxové distribuce apod.
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  K době psaní tohoto článku (konec srpna 12024) nejnovější PyTorch 2.4.0 podporuje CUDA 12.4. Proto zde používám obraz [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Nejnovější verzi PyTorch a podporovanou verzi CUDA lze ověřit na [webu PyTorch](https://pytorch.org/get-started/locally/).

Zdroj výsledného Dockerfile je zveřejněn v GitHub repozitáři [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Níže krok za krokem popisuji postup jeho tvorby.

> (+ revize 12026.1.6.)  
> Do stejného GitHub repozitáře a veřejného repozitáře Docker Hubu [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) jsem přidal i Dockerfile a obrazy podporující PyTorch 2.9.1 a CUDA 12.8 / 13.0. Obsah článku jsem aktualizoval pro PyTorch 2.9.1 a CUDA 13.0.
>
> Dále jsem do obrazu zahrnul scikit-image, XGBoost a v ekosystému RAPIDS knihovny cuGraph, cuxfilter, cuCIM, RAFT, cuVS a kromě architektury `amd64` jsem přidal i podporu `arm64`.
{: .prompt-info }

### 5-1. Určení base obrazu

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. Nastavení časové zóny systému (v článku použito „Asia/Seoul“)

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> Vycházel jsem hlavně z obsahu [tohoto článku](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22).
{: .prompt-tip }

### 5-3. Instalace základních systémových utilit

```Dockerfile
# Install basic utilities, gosu, and SSH server
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update -y && apt-get install -y --no-install-recommends \
        apt-utils \
        curl \
        gosu \
        openssh-server \
        ssh \
        tmux \
        tzdata \
# verify that the binary works
    && gosu nobody true
```

### 5-4. Nastavení SSH serveru pro vzdálený přístup

Z bezpečnostních důvodů zakážeme přihlášení na root účet přes SSH.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Vytvoříme non-root uživatele `remote`, který se bude používat pro SSH.

```Dockerfile
# Create remote user
#
# The password must be pre-specified at build time with the `DL_ENV_PASSWD`
# environment variable.
ARG USER_NAME="remote"
ARG USER_UID=1001
ARG USER_GID=$USER_UID
ARG HOME_DIR="/home/$USER_NAME"
RUN --mount=type=secret,id=USER_PASSWORD \
    groupadd --gid $USER_GID $USER_NAME && \
    useradd --uid $USER_UID --gid $USER_GID --create-home \
        --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && awk -v user="$USER_NAME" '{print user ":" $0}' /run/secrets/USER_PASSWORD | chpasswd
```

> Obsah build argumentů (`ARG`) i proměnných prostředí (`ENV`) je v sestaveném obrazu přímo viditelný, proto je při zadávání citlivých údajů, jako jsou hesla nebo API klíče, potřeba použít jiný postup](https://docs.docker.com/build/building/secrets/). Zde jsem použil [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts).
{: .prompt-danger }

> Jak bude uvedeno níže v části [Sestavení obrazu](#6-1-sestavení-obrazu), při sestavení obrazu z tohoto Dockerfile musíte zadat řetězec použitého hesla přes proměnnou prostředí `DL_ENV_PASSWD`. V případě [obrazů distribuovaných přes Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) je výchozí heslo účtu `satisfied-flip-remake`; ponechání tohoto veřejně známého hesla je z hlediska bezpečnosti velmi nebezpečné, proto po prvním spuštění kontejneru heslo ihned změňte. Pro vyšší bezpečnost je také vhodné později zakázat přihlašování heslem a povolit přihlašování pouze pomocí klíčů; ideální je využít i hardwarové klíče typu Yubikey.
>
> Konfiguraci SSH serveru proberu do určité míry v dalším díle série; pokud chcete jít více do hloubky, doporučuji následující dokumenty:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Instalace uv a registrace proměnných prostředí

> **Zohlednění PEP 668 a specifikace Externally Managed Environments a zavedení uv (revize 12026.1.6.)**
>
> Dříve jsem v tomto článku psal Dockerfile tak, aby se balíčky instalovaly pomocí `pip` přímo do kontejnerového obrazu bez vytváření samostatného virtuálního prostředí (`venv`). Důvodem bylo, že v „single-purpose“ kontejnerovém obrazu je riziko rozbití systémového softwaru menší a i kdyby k tomu došlo, obvykle stačí obraz znovu sestavit a spustit nový kontejner. Tento pohled PEP 668 částečně uznává i následujícím způsobem:
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> Přesto se jako standard ustálilo, že i v takových obrazech se instalace přes správce balíků jako `pip` provádí výhradně uvnitř virtuálního prostředí, aby byla striktně oddělena od balíků spravovaných „externě“ (externally managed) prostřednictvím systémového správce balíků apod. Proto jsem text aktualizoval tak, aby po vytvoření virtuálního prostředí proběhla instalace potřebných balíků uvnitř něj, a tím byl dodržen [PEP 668](https://peps.python.org/pep-0668/) i specifikace [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) a obecné standardy pythoního ekosystému.
>
> Oficiálně podporovaná standardní knihovna pro vytváření a správu virtuálních prostředí je `venv` (jak jsem mimochodem jednou zmiňoval i v [jiném článku z počátku 12021](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended)). Po vydání vysoce výkonného správce balíků a projektů v Pythonu, [`uv`](https://docs.astral.sh/uv/), vyvíjeného v Rustu firmou [Astral](https://astral.sh/) (poprvé zveřejněn v roce 12024), se však díky následujícím výhodám rychle stal de facto novým standardem:
> - [drtivě rychlejší řešení závislostí a instalace než `pip` (10–100×)](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
> - výborná použitelnost
> - [skvělá kompatibilita s existujícími `pip` a `venv`](https://docs.astral.sh/uv/pip/)
>
> Balíky z oblasti ML, jako PyTorch nebo RAPIDS, mívají mnoho závislostí a často jsou velké, takže výhody `uv` jsou zde obzvlášť výrazné. Navíc [`uv` agresivně a efektivně využívá cache](https://docs.astral.sh/uv/concepts/cache/), takže když při sestavení obrazu vhodně použijete cache mount, lze [zásadně zkrátit čas buildu](https://docs.astral.sh/uv/guides/integration/docker/#caching). Proto zde `uv` zavedu pro vytváření a správu virtuálního prostředí i pro instalaci balíků. Vycházel jsem hlavně z oficiální dokumentace [„Using uv in Docker“](https://docs.astral.sh/uv/guides/integration/docker/).
{: .prompt-info }

```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_UID:$USER_GID
WORKDIR $HOME_DIR

# Install uv by copying the binary from the official distroless image
COPY --from=ghcr.io/astral-sh/uv:0.9.21 /uv /uvx /bin/
ENV PATH="$HOME_DIR/.local/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ARG UV_CACHE_DIR="/tmp/uv-cache"
```

> **Proč je `UV_CACHE_DIR` nastaven na samostatnou cestu (`"/tmp/uv-cache"`) místo výchozí `"$HOME_DIR/.cache/uv"`**
>
> Při přidání uživatele pomocí `useradd --create-home` by měl tento uživatel standardně vlastnit svůj domovský adresář; zde tomu tak je.
> V Podmanu jsem však při buildu zjistil chybu: i když se v předchozích vrstvách vlastnictví nastaví správně, při připojení cache apod. v pozdější vrstvě se metadata vlastnictví nadřazeného adresáře resetují na výchozí (vlastník root). Při hledání jsem našel [issue nahlášené jiným uživatelem zhruba před 3 týdny](https://github.com/containers/podman/issues/27777), ale zatím bez odpovědi. Podrobnosti k situaci, kterou jsem zažil, jsem přidal jako [dodatečný komentář k tomuto issue](https://github.com/containers/podman/issues/27777#issuecomment-3712237296).
>
> Aby to nebyl problém ani v případě resetu vlastnictví na root, nastavil jsem v build fázi `UV_CACHE_DIR` mimo `$HOME_DIR`, konkrétně na `"/tmp/uv-cache"`. Tato cache se stejně do výsledného finálního obrazu nezahrnuje, takže změna cesty nevadí.
{: .prompt-tip }

### 5-6. Instalace Pythonu, vytvoření virtuálního prostředí, instalace setuptools & pip

```Dockerfile
# Install the latest, managed Python executables
ARG UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv python install 3.13 --default

# Create a virtual environment
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv venv --python 3.13 --seed
# Use the virtual environment automatically
ENV VIRTUAL_ENV=$HOME_DIR/.venv
# Place entry points in the environment at the front of the path & .profile
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN echo "source $VIRTUAL_ENV/bin/activate" >> $HOME_DIR/.profile
# Allow pip to only run in a virtual environment; exit with an error otherwise
ENV PIP_REQUIRE_VENV=true

# Install setuptools
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install setuptools
```

### 5-7. Instalace balíků pro ML/DL používaných ve vývojovém prostředí

#### 5-7-1. Společné balíky

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & GPU akcelerační knihovny specifické pro CUDA

##### Pokud instalujete pouze PyTorch

Pokud chcete instalovat jen PyTorch, přidejte do Dockerfile následující:

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & Cupy & RAPIDS & DALI

Pokud chcete používat nejen PyTorch, ale i Cupy, RAPIDS (cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS) a DALI, přidejte do Dockerfile následující:

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        --index-url https://download.pytorch.org/whl/cu130 \
        --extra-index-url=https://pypi.org/simple \
        --extra-index-url=https://pypi.nvidia.com \
        "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        cupy-cuda13x \
        "cudf-cu13==25.12.*" "dask-cudf-cu13==25.12.*" "cuml-cu13==25.12.*" \
        "cugraph-cu13==25.12.*" "nx-cugraph-cu13==25.12.*" "cuxfilter-cu13==25.12.*" \
        "cucim-cu13==25.12.*" "pylibraft-cu13==25.12.*" "raft-dask-cu13==25.12.*" \
        "cuvs-cu13==25.12.*" nvidia-dali-cuda130
```

> PyTorch a balíky RAPIDS sdílejí některé závislosti (cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE). Pokud by se instalovaly odděleně, je vysoké riziko konfliktu závislostí: verze požadovaná jedním balíkem může přepsat verzi nainstalovanou dříve a požadovanou druhým balíkem. Proto je vhodné tyto balíky instalovat jedním společným příkazem `uv pip install`, aby resolver zohlednil všechny podmínky současně, a aby se prioritně držely verze vyžadované PyTorchem.
{: .prompt-tip }

### 5-8. Vytvoření adresáře pro pracovní prostor

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. Otevření portů a nastavení `ENTRYPOINT` pro spuštění při startu kontejneru

Pro přístup přes SSH a Jupyter Lab otevřeme porty 22 a 8888.  
Dále: aby se při startu kontejneru automaticky spustil SSH démon, jsou potřeba root práva, proto použijeme tento postup:
1. kontejner se při startu spustí jako root
2. ihned po startu se spustí skript `/entrypoint.sh`{: .filepath}
3. skript spustí SSH službu a pak pomocí [`gosu`](https://github.com/tianon/gosu) přepne na účet `remote`
4. pokud při spuštění kontejneru není zadán žádný speciální příkaz, výchozí akce je spuštění JupyterLabu jako `remote` (non-root)

> Obecně se v Docker/Podman kontejnerech nedoporučuje používat `sudo` nebo `su`. Pokud potřebujete root práva, je vhodné postupovat jako zde: kontejner nejprve spustit jako root, udělat činnosti vyžadující root a poté přepnout na non-root uživatele pomocí [`gosu`](https://github.com/tianon/gosu). Důvody jsou podrobně vysvětlené v následujících materiálech:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Nejprve na konec Dockerfile přidejte:

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Poté ve stejném adresáři jako Dockerfile vytvořte soubor skriptu `entrypoint.sh`{: .filepath} s následujícím obsahem:

```sh
#!/bin/bash
set -e

# Dump environment variables
printenv | grep _ >> /etc/environment

# Run SSH daemon in the background
service ssh start

# Move to the workspace directory and run Jupyter Lab
cd "$WORK_DIR"
if [ $# -gt 0 ];then
    #su ${USER_NAME} -c "exec $@"
    exec gosu ${USER_NAME} $@
else
    #su ${USER_NAME} -c "exec jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}""
    exec gosu ${USER_NAME} jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}"
fi
```

> Obecně procesy spuštěné přes `docker exec` nebo `CMD` dědí Docker `ENV`, ale relace otevřené přes SSH často automaticky nezdědí proměnné prostředí z Dockeru, protože SSH při přihlášení vytváří novou shell relaci.
>
> Pokud to chcete obejít a zajistit, aby byly při SSH připojení dostupné i předem definované proměnné prostředí jako `$WORK_DIR`, je potřeba před spuštěním `ssh` služby při startu kontejneru proměnné „vypsat“ do `/etc/environment`{: .filepath } způsobem jako `printenv | grep _ >> /etc/environment`.
>
> K tématu mohou pomoci tyto odkazy:
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. Sestavení OCI obrazu a spuštění kontejneru

### 6-1. Sestavení obrazu

Otevřete terminál v adresáři, kde se nachází Dockerfile, a nastavte proměnnou prostředí `DL_ENV_PASSWD`.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> Do \<your_own_password\> zadejte přihlašovací heslo, které budete používat pro SSH.
{: .prompt-info }

Teď **toto okno terminálu nezavírejte** a ve stejném okně spusťte build.

#### Pro Podman

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> V Podmanu: pokud chcete kvůli distribuci sestavit obraz nejen pro platformu vlastního stroje (OS/architektura), ale pro všechny platformy podporované base obrazem, použijte [`--all-platforms` volbu](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms) a místo `--tag`/`-t` použijte [`--manifest`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant).
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> U Dockeru to zde zvlášť nerozepisuji; pokud to potřebujete, podívejte se do [oficiální dokumentace Dockeru](https://docs.docker.com/build/building/multi-platform/).
{: .prompt-tip }

#### Pro Docker

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. Spuštění ukázkové zátěže (workload)

Po dokončení buildu spusťte jednorázový kontejner a ověřte, že vše funguje.

Pro Podman:

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Pro Docker:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Po zadání výše uvedeného příkazu se z obrazu `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04` spustí kontejner pojmenovaný `test-container` a propojí se port 2222 na hostiteli s portem 22 v kontejneru a port 8888 na hostiteli s portem 8888 v kontejneru. Pokud se obraz správně sestavil a kontejner bez problémů naběhl, v kontejneru bude běžet JupyterLab na výchozí adrese `http:127.0.0.1:8888`. Proto když na hostitelském systému, kde běží Podman/Docker, otevřete prohlížeč a přejdete na <http://127.0.0.1:8888>, měli byste se připojit na `http://127.0.0.1:8888` uvnitř kontejneru a zobrazit obrazovku jako tato:

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Na hostitelském systému otevřete terminál a vyzkoušejte vzdálené přihlášení do účtu `remote` uvnitř kontejneru příkazem `ssh remote@127.0.0.1 -p 2222`.  
Při prvním přihlášení se zobrazí varování, že nemáte informace o klíči cílového stroje, a zeptá se, zda chcete pokračovat; zadejte „yes“.  
Poté pro přihlášení zadejte heslo, které jste nastavili při buildu (nebo pokud jste poprvé přihlášeni do obrazu staženého z [Docker Hub repozitáře](https://hub.docker.com/r/yunseokim/dl-env/tags), výchozí heslo `satisfied-flip-remake`).

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {otisk (unikátní hodnota, liší se pro každý klíč)}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:2222' (ED25519) to the list of known hosts.
remote@127.0.0.1's password: 
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 6.12.11-200.fc41.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

```

Pokud se výstup zhruba shoduje s tímto, vzdálené přihlášení přes SSH se podařilo. Pro ukončení spojení zadejte `exit`.

### 6-3. (volitelné) Push na Docker Hub

Pokud chcete vývojový obraz vytvořený výše kdykoli snadno stáhnout (pull) a používat, je dobré jej nahrát (push) na Docker Hub.  

> Abyste mohli pushovat vlastní obraz na Docker Hub, potřebujete Docker účet; pokud jej ještě nemáte, nejprve se zaregistrujte na <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Přihlášení na Docker Hub

##### Pro Podman

```bash
podman login docker.io
```

##### Pro Docker

```bash
docker login
```

#### 6-3-2. Tagování obrazu

Do `<dockerhub_username>`, `<repository_name>` a volitelného `:TAG` dosaďte vlastní hodnoty.  
Např. „yunseokim“, „dl-env“, „rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04“

> Pokud jste obraz sestavili nejen pro platformu vlastního stroje (OS/architektura), ale pro všechny platformy podporované base obrazem, a chcete hromadně pushnout manifest list / image index, tento krok přeskočte a přejděte rovnou na krok [Push obrazu](#6-3-3-push-obrazu) a postupujte podle uvedeného návodu.
{: .prompt-tip }

##### Pro Podman

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Pro Docker

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push obrazu

Nakonec spusťte následující příkaz a pushněte obraz na Docker Hub.

##### Pro Podman

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> V Podmanu: pokud chcete pushnout najednou více obrazů pro různé platformy svázaných do manifest listu / image indexu, použijte příkaz [`podman manifest push`](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls) takto:
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> Např.:
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### Pro Docker

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

Na <https://hub.docker.com/> pak uvidíte, že se obraz správně nahrál, například takto:

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

Obraz dokončený výše jsem zveřejnil v Docker Hub repozitáři [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags), kde jej může kdokoli volně používat.

Pro stažení (pull) obrazu stačí v příkazu použitém pro push změnit `push` na `pull` a příkaz spustit.
