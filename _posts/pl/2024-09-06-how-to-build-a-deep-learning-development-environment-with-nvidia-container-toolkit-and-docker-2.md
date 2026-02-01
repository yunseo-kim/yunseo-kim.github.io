---
title: "Budowa środowiska do deep learningu z NVIDIA Container Toolkit i Docker/Podman (2) — konfiguracja runtime’u kontenera dla GPU, pisanie Dockerfile i budowanie obrazu"
description: "Seria pokazuje, jak zbudować lokalne, kontenerowe środowisko deep learningu z NVIDIA Container Toolkit oraz skonfigurować SSH i JupyterLab do użycia jako serwer zdalny. Ten drugi wpis opisuje tworzenie Dockerfile i proces budowy obrazu."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Przegląd

W tej serii omawiam instalację NVIDIA Container Toolkit oraz Docker lub Podman, a następnie proces budowy środowiska do deep learningu poprzez napisanie Dockerfile na bazie obrazów CUDA i cuDNN dostępnych w repozytorium Docker Hub [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda). Aby każdy mógł swobodnie skorzystać z efektów, udostępniam przez GitHub i Docker Hub zarówno [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) ukończony po przejściu tych kroków, jak i [obrazy](https://hub.docker.com/r/yunseokim/dl-env/tags). Dodatkowo dostarczam przewodnik konfiguracji SSH i JupyterLab, aby móc wykorzystywać to jako serwer zdalny.  
Seria będzie składać się z 3 wpisów, a czytany teraz tekst jest drugim z nich.
- [Część 1: instalacja NVIDIA Container Toolkit i silnika kontenerów](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Część 2: konfiguracja runtime’u kontenera dla GPU, pisanie Dockerfile i budowanie obrazu (ten wpis)
- Część 3 (wkrótce)

Zakładam system x86_64 z kartą NVIDIA obsługującą CUDA w środowisku Linux; dystrybucji innych niż Ubuntu lub Fedora nie testowałem bezpośrednio, więc pewne szczegóły mogą się nieco różnić.  
(12026.1.6. rewizja)

> **Informacja o korekcie błędów**
>
> W szkicu tego wpisu opublikowanym w sierpniu 12024 r. występowały błędy w opisie sekcji [Pisanie Dockerfile](#5-dockerfile-작성) oraz w części obrazów zbudowanych z tego Dockerfile. Problem dotyczył następujących elementów:
> - w kroku tworzenia konta `remote` błędnie opisano ustawienie hasła — napisano, że można zalogować się używając „000000” jako hasła początkowego, co w rzeczywistości nie było prawdą (dodane 12025.12.19: obecnie hasło początkowe nie wynosi „000000”, więc koniecznie sprawdź [treść poniżej](#5-4-원격-접속을-위한-ssh-서버-설정))
> - przy starcie kontenera demon SSH nie uruchamiał się automatycznie
>
> Powyższe problemy zostały zauważone w lutym 12025 r. i około godz. 02:00 (czas koreański, UTC+9) 16 lutego 12025 r. podmieniłem problematyczny Dockerfile oraz obrazy Dockera na poprawione wersje w [repozytorium GitHub](https://github.com/yunseo-kim/dl-env-docker) oraz na [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> Jeśli pobrałeś Dockerfile lub obraz Dockera przed tym terminem, zamień je na wersję poprawioną.  
> Jeśli kogoś wprowadziły w błąd niepoprawne informacje z poprzedniej wersji, przepraszam.
{: .prompt-info }

## Zanim zaczniesz

Ten wpis jest kontynuacją [części 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), więc jeśli jeszcze jej nie czytałeś, zalecam najpierw zapoznać się z poprzednim tekstem.

## 4. Konfiguracja runtime’u kontenera

### Gdy używasz Podmana

[Konfiguracja z użyciem CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> W starszych wersjach przy pierwszej instalacji NVIDIA Container Toolkit, a także po każdej zmianie konfiguracji urządzeń GPU lub sterowników (w tym aktualizacji wersji), za każdym razem trzeba było ręcznie generować od nowa plik specyfikacji CDI.
>
> Jednak od NVIDIA Container Toolkit `v1.18.0` usługa systemd `nvidia-cdi-refresh` automatycznie generuje i aktualizuje plik specyfikacji CDI `/var/run/cdi/nvidia.yaml` w następujących przypadkach:
> - instalacja lub aktualizacja NVIDIA Container Toolkit
> - instalacja lub aktualizacja sterownika NVIDIA GPU
> - restart systemu
>
> W związku z tym, inaczej niż dawniej, nie trzeba już wykonywać dodatkowych kroków. Zmiany te uwzględniłem, aktualizując treść wpisu.
>
> Uwaga: przy usuwaniu sterownika GPU lub rekonfiguracji urządzeń MIG `nvidia-cdi-refresh` nie zareaguje, więc należy ręcznie zrestartować `nvidia-cdi-refresh.service`, aby wymusić ponowne wygenerowanie specyfikacji CDI.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> Jeśli użyjesz NVIDIA Container Runtime hook razem z CDI, może to powodować konflikt, więc jeśli istnieje plik `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath}, usuń go albo uważaj, by nie uruchamiać kontenera z ustawioną zmienną środowiskową `NVIDIA_VISIBLE_DEVICES`.
{: .prompt-warning }

### Gdy używasz Dockera

Opis dotyczy trybu [rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Konfiguracja runtime’u kontenera poleceniem `nvidia-ctk`

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

Powyższe polecenie modyfikuje plik `/etc/docker/daemon.json`{: .filepath} tak, aby Docker mógł korzystać z NVIDIA Container Runtime.

#### 4-Docker-2. Restart demona Dockera

Aby zastosować zmienioną konfigurację, zrestartuj demona Dockera.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. Konfiguracja `/etc/nvidia-container-runtime/config.toml`{: .filepath} poleceniem `sudo nvidia-ctk`

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Sprawdzenie, czy konfiguracja działa poprawnie

Uruchom przykładowy kontener CUDA.

Dla Podmana wykonaj:

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Dla Dockera wykonaj:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

Jeśli zobaczysz wynik podobny do poniższego, wszystko działa.

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

## 5. Pisanie Dockerfile

Napisz Dockerfile, który będzie bazował na obrazach CUDA i cuDNN dostarczanych w repozytorium Docker Hub [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda).

- Należy wybrać obraz, biorąc pod uwagę wymagane wersje CUDA i cuDNN oraz rodzaj i wersję dystrybucji Linuksa.
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  Według stanu na koniec sierpnia 12024 r., gdy powstawał ten tekst, najnowszy PyTorch 2.4.0 wspiera CUDA 12.4. Dlatego użyto tutaj obrazu [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Aktualne wersje PyTorch i wspierane wersje CUDA można sprawdzić na [stronie PyTorch](https://pytorch.org/get-started/locally/).

Źródło gotowego Dockerfile udostępniłem w repozytorium GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Poniżej krok po kroku opisuję proces jego tworzenia.

> (+ 12026.1.6. rewizja)  
> Dodałem Dockerfile oraz obrazy wspierające PyTorch 2.9.1 oraz CUDA 12.8 / 13.0 do tego samego repozytorium GitHub oraz publicznego repozytorium Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags). Treść wpisu również zaktualizowałem pod PyTorch 2.9.1 i CUDA 13.0.
>
> Ponadto uwzględniłem w obrazie scikit-image, XGBoost oraz biblioteki ekosystemu RAPIDS: cuGraph, cuxfilter, cuCIM, RAFT, cuVS, a także dodałem wsparcie `arm64` obok dotychczasowego `amd64`.
{: .prompt-info }

### 5-1. Wskazanie obrazu bazowego

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. Ustawienie strefy czasowej systemu (w tym wpisie: „Asia/Seoul”)

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> Korzystałem głównie z treści [tego wpisu](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22).
{: .prompt-tip }

### 5-3. Instalacja podstawowych narzędzi systemowych

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

### 5-4. Konfiguracja serwera SSH do zdalnego dostępu

Ze względów bezpieczeństwa skonfiguruj SSH tak, aby logowanie na konto root przez SSH było niemożliwe.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Utwórz użytkownika bez uprawnień roota o nazwie `remote`, który będzie używany do logowania przez SSH.

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

> Ponieważ zawartość argumentów budowania (`ARG`) i zmiennych środowiskowych (`ENV`) jest wprost ujawniana w zbudowanym obrazie, [do przekazywania danych wrażliwych, takich jak hasła czy klucze API, należy używać innego podejścia](https://docs.docker.com/build/building/secrets/). Tutaj użyto [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts).
{: .prompt-danger }

> Jak opiszę [później](#6-1-이미지-빌드), przy budowaniu obrazu z tego Dockerfile należy podać hasło konta użytkownika poprzez zmienną środowiskową `DL_ENV_PASSWD`. W przypadku obrazów dystrybuowanych na [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) hasło początkowe konta to `satisfied-flip-remake`. Pozostawienie tego publicznie znanego hasła bez zmian jest skrajnie niebezpieczne — po pierwszym uruchomieniu kontenera natychmiast je zmień. Z punktu widzenia bezpieczeństwa zalecane jest także wyłączenie logowania hasłem i skonfigurowanie logowania wyłącznie kluczem, a idealnie również użycie klucza sprzętowego (np. YubiKey).
>
> Konfigurację serwera SSH omówię w pewnym zakresie w kolejnej części serii; jeśli chcesz więcej szczegółów, warto zajrzeć do poniższych dokumentów:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Instalacja uv oraz rejestracja zmiennych środowiskowych

> **Uwzględnienie specyfikacji Externally Managed Environments zgodnie z [PEP 668](https://peps.python.org/pep-0668/) oraz wprowadzenie uv (12026.1.6. rewizja)**
>
> W przeszłości w tym wpisie tworzyłem Dockerfile tak, by instalować pakiety przez `pip` bezpośrednio w obrazie kontenera, bez tworzenia osobnego środowiska wirtualnego (`venv`). Wynikało to z założenia, że w obrazie kontenera o pojedynczym przeznaczeniu ryzyko „zepsucia” oprogramowania systemowego jest niewielkie, a nawet jeśli dojdzie do problemów, można po prostu zbudować nowy kontener. Tę perspektywę częściowo uznaje również [PEP 668](https://peps.python.org/pep-0668/#use-cases):
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> Jednak nawet w takim scenariuszu standardem stało się wykonywanie instalacji przez menedżera pakietów Pythona (np. `pip`) wyłącznie wewnątrz środowiska wirtualnego, z rygorystycznym rozdzieleniem od pakietów zarządzanych zewnętrznie (externally managed) przez menedżer pakietów systemu operacyjnego. W związku z tym zaktualizowałem treść tak, aby po utworzeniu środowiska wirtualnego instalować pakiety w jego ramach, zgodnie z [PEP 668](https://peps.python.org/pep-0668/) i specyfikacją [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/).
>
> Standardową biblioteką Pythona do tworzenia i zarządzania środowiskiem wirtualnym jest `venv`, co opisałem także w innym tekście napisanym na początku 12021 r.: <https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended>.
>
> Jednak po tym, jak [Astral](https://astral.sh/) opublikował w 12024 r. wydajnego menedżera pakietów i projektów w Pythonie, napisanego w Ruście — [`uv`](https://docs.astral.sh/uv/) — narzędzie to bardzo szybko stało się nowym de facto standardem dzięki m.in.:
> - zdecydowanie szybszemu rozwiązywaniu zależności i instalacji pakietów niż `pip` (10–100×): <https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md>
> - bardzo dobrej ergonomii użycia
> - świetnej kompatybilności z `pip` i `venv`: <https://docs.astral.sh/uv/pip/>
>
> W szczególności pakiety z obszaru ML, takie jak PyTorch czy RAPIDS, mają dużo zależności i często są duże, więc zalety `uv` są tu wyjątkowo odczuwalne. Dodatkowo [`uv` aktywnie i efektywnie korzysta z cache](https://docs.astral.sh/uv/concepts/cache/); przy odpowiednim użyciu cache mount podczas budowania obrazu można wyraźnie skrócić czas builda: <https://docs.astral.sh/uv/guides/integration/docker/#caching>. Dlatego także tutaj wprowadzę `uv` do tworzenia i zarządzania środowiskiem wirtualnym oraz instalowania pakietów. Opierałem się głównie na oficjalnym dokumencie: ["Using uv in Docker"](https://docs.astral.sh/uv/guides/integration/docker/).
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

> **Dlaczego ustawiono `UV_CACHE_DIR` na `"/tmp/uv-cache"` zamiast domyślnego `"$HOME_DIR/.cache/uv"`**
>
> Zwykle po dodaniu użytkownika przez `useradd --create-home` użytkownik powinien być właścicielem swojego katalogu domowego — i tak jest również tutaj.
> Jednak przy budowaniu obrazu w Podmanie odkryłem błąd: nawet jeśli we wcześniejszych warstwach poprawnie zmieniono właściciela, to przy montowaniu cache w późniejszych warstwach metadane własności katalogu nadrzędnego są resetowane do wartości domyślnej (własność roota). Znalazłem też zgłoszenie innego użytkownika sprzed ok. 3 tygodni opisujące ten sam problem: <https://github.com/containers/podman/issues/27777>, ale w chwili pisania nie było jeszcze odpowiedzi. Bardziej szczegółowy opis mojego przypadku dopisałem jako komentarz do tego zgłoszenia: <https://github.com/containers/podman/issues/27777#issuecomment-3712237296>.
>
> Aby uniknąć problemów nawet wtedy, gdy własność zostanie zresetowana do roota, na etapie builda ustawiam `UV_CACHE_DIR` poza `$HOME_DIR`, na `"/tmp/uv-cache"`. Ten cache i tak nie trafia do finalnego obrazu, więc zmiana ścieżki nie stanowi problemu.
{: .prompt-tip }

### 5-6. Instalacja Pythona, utworzenie środowiska wirtualnego, instalacja setuptools i pip

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

### 5-7. Instalacja pakietów ML/DL do środowiska deweloperskiego

#### 5-7-1. Pakiety wspólne

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch i biblioteki akceleracji GPU specyficzne dla CUDA

##### Jeśli instalujesz tylko PyTorch

Aby zainstalować tylko PyTorch, dodaj do Dockerfile:

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch + Cupy + RAPIDS + DALI

Jeśli oprócz PyTorch chcesz używać Cupy oraz RAPIDS (cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS), a także DALI, dodaj:

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

> W tym miejscu PyTorch i RAPIDS współdzielą pewne biblioteki zależności (cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE). Jeśli instalować je oddzielnie, rośnie ryzyko konfliktów zależności: wersje wymagane przez później instalowany pakiet mogą nadpisać te zainstalowane wcześniej. Dlatego instalację warto scalić w jedno polecenie `uv pip install`, aby resolver uwzględnił wszystkie ograniczenia naraz, a priorytet miały wersje wymagane przez PyTorch.
{: .prompt-tip }

### 5-8. Utworzenie katalogu roboczego

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. Otwarcie portów i ustawienie `ENTRYPOINT` uruchamianego przy starcie kontenera

Aby umożliwić dostęp przez SSH i Jupyter Lab, otwieramy porty 22 i 8888.  
Dodatkowo, aby demon SSH uruchamiał się automatycznie przy starcie kontenera, potrzebne są uprawnienia roota — zastosujemy więc następujące podejście:
1. kontener startuje zalogowany jako root
2. tuż po starcie uruchamiany jest skrypt `/entrypoint.sh`{: .filepath}
3. skrypt uruchamia usługę SSH, a następnie przełącza się na konto `remote` używając [`gosu`](https://github.com/tianon/gosu)
4. jeśli przy uruchamianiu kontenera nie podano osobnej komendy, domyślnie uruchamiany jest Jupyter Lab na koncie `remote` (bez uprawnień roota)

> Ogólnie w kontenerach Docker/Podman nie zaleca się używania `sudo` ani `su`. Jeśli potrzebujesz uprawnień roota, lepszym podejściem jest uruchomienie kontenera jako root, wykonanie niezbędnych czynności wymagających roota, a następnie przełączenie się na użytkownika bez roota poprzez [`gosu`](https://github.com/tianon/gosu). Dlaczego tak jest, szczegółowo wyjaśniają poniższe materiały:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Najpierw dodaj na końcu Dockerfile:

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Następnie w tym samym katalogu co Dockerfile utwórz plik skryptu o nazwie `entrypoint.sh`{: .filepath} i wklej poniższą treść:

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

> Zwykle proces uruchomiony przez `docker exec` lub CMD dziedziczy ENV z Dockera, natomiast sesja zestawiona przez SSH często nie dziedziczy automatycznie zmiennych środowiskowych Dockera. Dzieje się tak, ponieważ SSH przy logowaniu tworzy nową sesję powłoki.
>
> Aby to obejść i zapewnić dostęp do wcześniej zdefiniowanych zmiennych (np. `$WORK_DIR`) również po logowaniu przez SSH, trzeba przed uruchomieniem usługi ssh podczas startu kontenera „zrzucić” zmienne do `/etc/environment`{: .filepath}, np. `printenv | grep _ >> /etc/environment`.
>
> Pomocne mogą być poniższe linki:
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. Budowanie obrazu OCI i uruchamianie kontenera

### 6-1. Budowanie obrazu

Otwórz terminal w katalogu, w którym znajduje się Dockerfile, i ustaw zmienną środowiskową `DL_ENV_PASSWD`.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> W miejsce \<your_own_password\> wpisz hasło logowania, które ma być używane przy połączeniu przez SSH.
{: .prompt-info }

Teraz **nie zamykaj tego okna terminala** i w tym samym oknie uruchom poniższe polecenia, aby przeprowadzić build.

#### Dla Podmana

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> W Podmanie, jeśli chcesz zbudować obraz nie tylko dla platformy używanego urządzenia (OS/arch), ale dla wszystkich platform wspieranych przez obraz bazowy, możesz dodać opcję [`--all-platforms`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms) oraz zamiast `--tag`/`-t` użyć opcji [`--manifest`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant).
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> Dla Dockera nie porządkuję tego osobno w tym wpisie — w razie potrzeby zobacz: <https://docs.docker.com/build/building/multi-platform/>.
{: .prompt-tip }

#### Dla Dockera

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. Uruchomienie przykładowego workloadu

Po zakończeniu budowania uruchom jednorazowy kontener i sprawdź, czy wszystko działa.

Dla Podmana:

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Dla Dockera:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Po wpisaniu polecenia powyżej uruchomisz kontener o nazwie `test-container` z obrazu `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04`, a następnie zmapujesz port 2222 hosta na port 22 kontenera oraz port 8888 hosta na port 8888 kontenera. Jeśli obraz zbudował się poprawnie i kontener wystartował bez problemów, wewnątrz kontenera JupyterLab powinien działać pod domyślnym adresem `http:127.0.0.1:8888`. W związku z tym na hoście, na którym działa Podman lub Docker, otwórz przeglądarkę i wejdź na <http://127.0.0.1:8888>. Powinno to połączyć się z adresem `http://127.0.0.1:8888` wewnątrz kontenera i wyświetlić ekran podobny do poniższego.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Na hoście otwórz terminal i wykonaj `ssh remote@127.0.0.1 -p 2222`, aby spróbować zdalnie zalogować się do systemu Ubuntu działającego wewnątrz kontenera na konto `remote`.  
Przy pierwszym logowaniu nie masz informacji o kluczu hosta docelowego, więc pojawi się ostrzeżenie o braku możliwości weryfikacji — zostaniesz zapytany, czy kontynuować. Wpisz `yes`, aby przejść dalej.  
Następnie, aby się zalogować, wpisz hasło ustawione podczas budowania (albo, jeśli logujesz się po raz pierwszy do obrazu pobranego z [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags), hasło początkowe `satisfied-flip-remake`).

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {odcisk palca (unikalna wartość, inna dla każdego klucza)}.
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

Jeśli zobaczysz wynik z grubsza podobny do powyższego, logowanie zdalne przez SSH się powiodło. Aby zakończyć połączenie, wpisz `exit`.

### 6-3. (optional) Push na Docker Hub

Jeśli chcesz móc w dowolnym momencie pobierać (pull) i wykorzystywać obraz środowiska deweloperskiego utworzony powyższą metodą, warto wypchnąć (push) zbudowany obraz na Docker Hub.  

> Aby wykonać push własnego obrazu na Docker Hub, potrzebujesz konta Docker. Jeśli jeszcze go nie masz, zarejestruj się tutaj: <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Logowanie do Docker Hub

##### Dla Podmana

```bash
podman login docker.io
```

##### Dla Dockera

```bash
docker login
```

#### 6-3-2. Nadanie taga obrazowi

W miejscach `<dockerhub_username>`, `<repository_name>` oraz (opcjonalnie) `:TAG` wstaw odpowiednie dla siebie wartości.  
Np. „yunseokim”, „dl-env”, „rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04”.

> Jeśli wcześniej zbudowałeś obraz nie tylko dla platformy używanego urządzenia (OS/arch), ale dla wszystkich platform wspieranych przez obraz bazowy, i chcesz wypchnąć zbiorczo listę manifestów / indeks obrazów, pomiń ten krok i przejdź od razu do kroku [Push obrazu](#6-3-3-이미지-push), stosując metodę opisaną w tym miejscu.
{: .prompt-tip }

##### Dla Podmana

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Dla Dockera

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push obrazu

Na koniec wykonaj poniższe polecenie, aby wypchnąć obraz na Docker Hub.

##### Dla Podmana

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> W Podmanie, aby wypchnąć naraz obrazy dla wielu platform zebrane jako lista manifestów lub indeks obrazów, użyj polecenia [`podman manifest push`](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls):
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> Np.
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### Dla Dockera

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

Na <https://hub.docker.com/> możesz sprawdzić, czy obraz został poprawnie wypchnięty — powinieneś zobaczyć coś podobnego do poniższego.

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

Obraz ukończony powyższą metodą udostępniłem publicznie w repozytorium Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) — każdy może go swobodnie używać.

Aby pobrać (pull) obraz, wystarczy w poleceniu użytym do push zamienić `push` na `pull` i je wykonać.
