---
title: "使用 NVIDIA Container Toolkit 與 Docker/Podman 建置深度學習開發環境（2）- 用於 GPU 的容器執行時設定、撰寫 Dockerfile 與建置容器映像"
description: "本系列介紹如何在本機使用 NVIDIA Container Toolkit 建置容器化深度學習開發環境，並設定 SSH 與 JupyterLab 以便作為遠端伺服器使用。本文為系列第 2 篇，說明 Dockerfile 撰寫與容器映像建置流程。"
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## 概要

本系列將介紹安裝 NVIDIA Container Toolkit 與 Docker 或 Podman，並以 Docker Hub 的 [nvidia/cuda 儲存庫](https://hub.docker.com/r/nvidia/cuda)所提供的 CUDA 與 cuDNN 映像為基底撰寫 Dockerfile，以建置深度學習開發環境的流程。為了讓有需要的人能自由取用，我也會透過 GitHub 與 Docker Hub 分享經此流程完成的 [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) 與 [映像](https://hub.docker.com/r/yunseokim/dl-env/tags)，並另外提供可作為遠端伺服器使用的 SSH 與 JupyterLab 設定指南。  
本系列預計由 3 篇文章構成，而你正在閱讀的這篇是第 2 篇。
- [第 1 篇：安裝 NVIDIA Container Toolkit & 容器引擎](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 第 2 篇：用於 GPU 的容器執行時設定、撰寫 Dockerfile 與建置容器映像（本文）
- 第 3 篇（預計上傳）

本文以 x86_64 Linux 環境、並假設系統配備支援 CUDA 的 NVIDIA 顯示卡為前提進行；由於除了 Ubuntu 或 Fedora 以外的發行版我並未親自測試，部分細節可能會略有差異。  
（12026.1.6. 修訂）

> **錯誤更正說明**
>
> 在 12024 年 8 月上傳的本文初稿中，[撰寫 Dockerfile](#5-dockerfile-撰寫) 章節的敘述以及由該 Dockerfile 建置的映像存在部分錯誤。問題如下：
> - 建立 remote 帳號時設定密碼的部分有誤，文中描述可用「000000」作為初始密碼登入，但實際上並非如此（12025.12.19 補充：目前初始密碼也已不再是「000000」，務必確認[下方本文內容](#5-4-為了遠端連線的-ssh-伺服器設定)）
> - 容器啟動時 SSH daemon 不會自動啟動
>
> 我在 12025 年 2 月才意識到上述問題，並已於韓國時間（UTC+9）12025 年 2 月 16 日凌晨 2 點左右，將有問題的 Dockerfile 與 Docker 映像在 [GitHub 儲存庫](https://github.com/yunseo-kim/dl-env-docker)與 [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags)替換為已修正的版本。  
> 若你在該時間點之前 Pull 過 Dockerfile 或 Docker 映像，請更換為修正版。  
> 若先前參考本文的讀者因錯誤內容而造成困擾，在此致歉。
{: .prompt-info }

## 開始之前

本文是承接[第 1 篇](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)的續篇；若尚未閱讀，建議先讀完前一篇再回來。

## 4. 容器執行時（runtime）設定

### 使用 Podman 的情況

[透過 CDI(Container Device Interface) 來設定。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> 在舊版本中，NVIDIA Container Toolkit 初次安裝時，以及之後每次變更顯示卡裝置或驅動程式設定（包含版本升級）時，都必須手動重新產生 CDI 規格檔。
>
> 但自 NVIDIA Container Toolkit `v1.18.0` 起，會透過 `nvidia-cdi-refresh` systemd 服務，在下列情況自動建立並更新 `/var/run/cdi/nvidia.yaml` CDI 規格檔：
> - 安裝或升級 NVIDIA Container Toolkit 時
> - 安裝或升級 NVIDIA GPU 驅動程式時
> - 系統重新開機時
>
> 因此如今不同於以往，不再需要另外做什麼；我也已反映此變更而修訂本文內容。
>
> 但若是移除 GPU 驅動或重新配置 MIG 裝置，`nvidia-cdi-refresh` 無法處理，必須手動重新啟動 `nvidia-cdi-refresh.service` 以觸發 CDI 規格重新產生。
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> 若將 NVIDIA Container Runtime hook 與 CDI 一起使用可能會產生衝突，因此若存在 `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath}，請刪除該檔案，或注意不要在設定了 `NVIDIA_VISIBLE_DEVICES` 環境變數的狀態下執行容器。
{: .prompt-warning }

### 使用 Docker 的情況

以[無 root(rootless) 模式](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode)為基準進行說明。

#### 4-Docker-1. 使用 `nvidia-ctk` 指令設定容器 runtime

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

上述指令會修改 `/etc/docker/daemon.json`{: .filepath}，使 Docker 能使用 NVIDIA Container Runtime。

#### 4-Docker-2. 重新啟動 Docker daemon

為了套用變更後的設定，重新啟動 Docker daemon。

```bash
systemctl --user restart docker
```

#### 4-Docker-3. 使用 `sudo nvidia-ctk` 設定 `/etc/nvidia-container-runtime/config.toml`{: .filepath}

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### 確認是否設定成功

嘗試執行範例 CUDA 容器。

若使用 Podman，執行以下指令：

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

若使用 Docker，執行以下指令：

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

若顯示出大致如下的畫面，即表示成功。

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

## 5. Dockerfile 撰寫

以 Docker Hub 的 [nvidia/cuda 儲存庫](https://hub.docker.com/r/nvidia/cuda)所提供的 CUDA 與 cuDNN 映像為基底，撰寫將作為開發環境的 Dockerfile。

- 必須綜合考量所需的 CUDA 與 cuDNN 版本、Linux 發行版類型與版本等，來決定要使用的映像。 
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  以本文撰寫當時（12024 年 8 月下旬）為準，PyTorch 最新版 2.4.0 支援 CUDA 12.4。因此此處使用 [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) 映像。[PyTorch 官網](https://pytorch.org/get-started/locally/)可確認 PyTorch 最新版本與支援的 CUDA 版本。

完整 Dockerfile 原始碼已公開於 [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub 儲存庫。以下將分步說明撰寫該 Dockerfile 的過程。

> （+ 12026.1.6. 修訂）  
> 我已在同一個 GitHub 儲存庫與 [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) Docker Hub 公開儲存庫中，新增支援 PyTorch 2.9.1 與 CUDA 12.8 / 13.0 的 Dockerfile 與映像；本文內容也已依 PyTorch 2.9.1、CUDA 13.0 更新。
>
> 另外也將 scikit-image、XGBoost，以及 RAPIDS 生態系中的 cuGraph、cuxfilter、cuCIM、RAFT、cuVS 函式庫納入映像，並在既有 `amd64` 架構之外新增 `arm64` 支援。
{: .prompt-info }

### 5-1. 指定 base 映像

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. 設定系統時區（本文以 'Asia/Seoul' 為例）

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> 主要參考了[這篇文章](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22)的內容。
{: .prompt-tip }

### 5-3. 安裝基本系統工具

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

### 5-4. 為了遠端連線的 SSH 伺服器設定

為了安全起見，設定成 SSH 遠端連線時不可用 root 帳號登入。

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

建立一個用於 SSH 連線、名為 'remote' 的 non-root 使用者。

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

> 建置參數（`ARG`）或環境變數（`ENV`）的內容會原封不動暴露在建置後的映像中，因此在指定密碼或 API key 等敏感資訊時，[必須使用其他方法](https://docs.docker.com/build/building/secrets/)。此處使用了 [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts)。
{: .prompt-danger }

> 如後文所述（[#6-1-映像建置](#6-1-映像建置)），使用這份 Dockerfile 建置映像時，必須透過 `DL_ENV_PASSWD` 環境變數指定要作為使用者帳號密碼的字串。[Docker Hub 發佈映像](https://hub.docker.com/r/yunseokim/dl-env/tags)的帳號初始密碼為 `satisfied-flip-remake`；若直接沿用此公開的預設密碼，安全性將非常脆弱，因此請在第一次啟動容器後立即變更設定。此外，從安全角度來看，後續最好停用 SSH 的密碼登入，改為僅允許透過獨立的金鑰檔登入；若再搭配 Yubikey 之類的硬體金鑰則更理想。
>
> 關於 SSH 伺服器的設定，本系列下一篇會稍微提到；若想更深入了解，可參考以下文件：
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. 安裝 uv 並註冊環境變數

> **依 [PEP 668](https://peps.python.org/pep-0668/)反映 [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) 規格並導入 uv（12026.1.6. 修訂）**
>
> 過去本文的 Dockerfile 是在不建立獨立虛擬環境（`venv`）的情況下，直接在容器映像內用 `pip` 安裝套件。當時這麼做的理由是：在單一用途的容器映像中，系統軟體被破壞的風險較低；就算真的出問題，也只要用映像重建新的容器即可，因此我判斷不一定需要另外建立虛擬環境。[PEP 668](https://peps.python.org/pep-0668/#use-cases)也在某種程度上認同此點，如下所述：
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> 然而，即便是在單一用途的容器映像中，透過 `pip` 等 Python 套件管理器進行安裝也已被確立為標準：必須只在虛擬環境內執行，並且嚴格與透過作業系統套件管理器等外部方式管理的（externally managed）套件區隔開來。基於此，我修訂本文內容：先建立虛擬環境，再在其中安裝所需套件，以遵循 [PEP 668](https://peps.python.org/pep-0668/)及其對應的 [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) 規格，符合 Python 生態系的標準作法。
>
> Python 官方支援的虛擬環境建立與管理標準函式庫是 `venv`；我也曾在 12021 年初撰寫的另一篇文章中介紹過一次（https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended）。不過，自從 [Astral](https://astral.sh/) 以 Rust 開發的高效能 Python 套件/專案管理器 [`uv`](https://docs.astral.sh/uv/)於 12024 年首次公開後，因下列顯著優勢而快速成為 Python 生態系新的事實標準：
> - 相較 [`pip` 具壓倒性的依賴解析與套件安裝速度（10-100 倍）](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
> - 使用體驗優秀
> - [與既有 `pip` 與 `venv` 具高度相容性](https://docs.astral.sh/uv/pip/)
>
> 尤其本文所用的 PyTorch、RAPIDS 等機器學習套件，依賴套件多且多半容量很大，`uv` 的優勢能充分發揮。再加上 [`uv` 會積極且有效地使用快取](https://docs.astral.sh/uv/concepts/cache/)，如同本文一樣在建置容器映像時適當使用 cache mount，就能進一步放大優勢、大幅縮短建置時間（https://docs.astral.sh/uv/guides/integration/docker/#caching）。因此本文也將導入 `uv` 來建立/管理虛擬環境並安裝套件；操作主要參考 `uv` 的官方文件〈["Using uv in Docker"](https://docs.astral.sh/uv/guides/integration/docker/)〉。
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

> **將 `UV_CACHE_DIR` 從預設值 `"$HOME_DIR/.cache/uv"` 改為家目錄外的路徑（`"/tmp/uv-cache"`）的原因**
>
> 一般來說，用 `useradd --create-home` 新增使用者後，該使用者理應擁有自己家目錄的所有權；本文也是如此。
> 但我發現使用 Podman 建置映像時，即使在前面的 layer 已正常移交所有權，在後面的 layer 只要掛載 cache 等，其上層目錄的所有權中繼資料會被重設成預設值（root 所有）的 bug。搜尋後我發現約 3 週前已有其他使用者回報同樣現象的 issue（https://github.com/containers/podman/issues/27777），但該 issue 目前仍未收到任何回覆。我也已在該 issue 留下補充評論，描述我遇到的狀況細節（https://github.com/containers/podman/issues/27777#issuecomment-3712237296）。
>
> 因此，為了即使所有權被重設為 root 也不會造成問題，在建置階段將 `UV_CACHE_DIR` 設為與 `$HOME_DIR` 不同的 `"/tmp/uv-cache"`。反正此快取不會被包含在最終映像中，因此調整路徑也無妨。
{: .prompt-tip }

### 5-6. 安裝 Python、建立虛擬環境、安裝 setuptools & pip

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

### 5-7. 安裝開發環境要用的機器學習與深度學習套件

#### 5-7-1. 共通套件

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & CUDA 專用 GPU 加速函式庫

##### 只安裝 PyTorch 的情況

若只要安裝 PyTorch，則在 Dockerfile 中加入以下內容。

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & Cupy & RAPIDS & DALI

若除了 PyTorch 之外，還要使用 Cupy、RAPIDS(cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS)，以及 DALI，則在 Dockerfile 中加入以下內容。

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

> 此時 PyTorch 與 RAPIDS 套件會共用部分依賴函式庫（cuBLAS、NVRTC、cuFFT、cuRAND、cuSOLVER、cuSPARSE）。若分開安裝，彼此要求的版本可能不同，容易出現先安裝的版本被後安裝的版本覆寫而導致依賴衝突的風險。因此在安裝這些套件時，建議將安裝指令整合為一個 `uv pip install`，讓依賴解析器（resolver）能同時考量所有限制條件，並以 PyTorch 要求的版本為優先。
{: .prompt-tip }

### 5-8. 建立作為工作空間的目錄

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. 開放連接埠並設定容器啟動時要執行的 `ENTRYPOINT`
為了 SSH 與 Jupyter Lab 連線，開放 22、8888 連接埠。  
此外，若要在容器啟動時自動執行 SSH daemon，需要 root 權限，因此將採用以下方法：
1. 容器啟動時以 root 帳號登入
2. 容器啟動後立刻執行 `/entrypoint.sh`{: .filepath} 腳本
3. 在該腳本啟動 SSH 服務後，使用 [`gosu`](https://github.com/tianon/gosu)切換到 remote 帳號
4. 若執行容器時未額外指定指令，則預設以 remote 帳號（non-root 權限）啟動 Jupyter Lab

> 一般不建議在 Docker 或 Podman 容器中使用 `sudo` 或 `su`；若確實需要 root 權限，如本文所述，最佳做法是先以 root 帳號啟動容器、完成需要 root 權限的工作後，再使用 [`gosu`](https://github.com/tianon/gosu)切換成 non-root 使用者。原因可參考以下資料的詳細說明（有需要時再看即可）：
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

先在 Dockerfile 最後加入以下內容。

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

接著，在與 Dockerfile 相同的路徑下建立名為 `entrypoint.sh`{: .filepath} 的腳本檔，內容如下：

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

> 一般而言，透過 docker exec 或 CMD 執行的程序會原樣繼承 Docker 的 ENV；但透過 SSH 登入的 session 往往無法自動繼承 Docker 的環境變數，因為 SSH 登入時會建立新的 shell session。
>
> 若要解決此問題，並讓 SSH 連線時也能存取 `$WORK_DIR` 等預先定義的環境變數，需要在容器啟動、且 ssh 服務啟動之前，先用 `printenv | grep _ >> /etc/environment` 之類的方式把環境變數預先 dump 到 `/etc/environment`{: .filepath }。
>
> 相關內容可參考以下連結，會很有幫助：
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. 建置 OCI 映像並執行容器

### 6-1. 映像建置

在 Dockerfile 所在的目錄打開終端機，並設定 `DL_ENV_PASSWD` 環境變數。

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> 在 \<your_own_password\> 的位置輸入 SSH 連線登入時要使用的密碼即可。
{: .prompt-info }

接著**不要關閉此終端機視窗**，在同一個視窗中繼續執行以下指令進行建置。

#### Podman 的情況

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> 以 Podman 為例，若考慮發佈用途，想不只針對自己裝置的平台（作業系統/架構），也針對 base 映像支援的所有平台建置映像，則可如下加上 [`--all-platforms` 選項](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms)，並且[用 `--manifest` 取代 `--tag` 或 `-t`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant)。
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> Docker 的部分我在此不另行整理；若有需要請參考 [Docker 官方文件](https://docs.docker.com/build/building/multi-platform/)。
{: .prompt-tip }

#### Docker 的情況

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. 執行範例工作負載

建置完成後，先啟動一次性容器以確認是否正常運作。

Podman 的情況，執行以下指令：

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Docker 的情況，執行以下指令：
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

在終端機輸入上述指令後，會從先前建置的 `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04` 映像啟動名為 `test-container` 的容器，並將主機的 2222 連接埠與容器的 22 連接埠、主機的 8888 連接埠與容器的 8888 連接埠分別對應連接。若前述步驟中映像建置成功且容器能正常啟動，則 `test-container` 容器內的 JupyterLab 會以預設值 `http:127.0.0.1:8888` 位址運行。因此在執行 Podman 或 Docker 的主機系統上打開瀏覽器並連到 <http://127.0.0.1:8888> 時，應會連進容器內的 `http://127.0.0.1:8888`，並顯示如下畫面。

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

在主機系統上打開終端機，執行 `ssh remote@127.0.0.1 -p 2222`，嘗試以容器內 Ubuntu 系統的 remote 帳號進行遠端登入。  
第一次登入時，因為尚未有連線目標的主機金鑰資訊而無法驗證，會輸出警告並詢問是否要繼續連線；輸入 "yes" 繼續即可。  
之後會要求輸入登入密碼：也就是先前建置時指定的密碼（或者若是 Pull [Docker Hub 發佈映像](https://hub.docker.com/r/yunseokim/dl-env/tags)並首次登入，則輸入初始密碼 `satisfied-flip-remake`）。

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {指紋（每把金鑰都有各自不同的唯一值）}.
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

若輸出大致如上，即代表已成功透過 SSH 遠端登入。要結束連線時輸入 `exit` 即可。

### 6-3.（optional）Push 到 Docker Hub

若希望將前述流程製作出的開發環境映像在需要時隨時 Pull 來使用，建議把建置好的映像 Push 到 Docker Hub。  

> 要將自己的映像 Push 到 Docker Hub 需要 Docker 帳號；若尚未有帳號，請先到 <https://app.docker.com/signup>完成註冊。
{: .prompt-tip }

#### 6-3-1. 登入 Docker Hub

##### Podman 的情況

```bash
podman login docker.io
```

##### Docker 的情況

```bash
docker login
```

#### 6-3-2. 設定映像 tag

請在 `<dockerhub_username>`、`<repository_name>`、（選擇性）`:TAG` 位置填入你自己的資訊。  
例如："yunseokim"、"dl-env"、"rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04"

> 若你先前已不只針對自己裝置的平台（作業系統/架構），也針對 base 映像支援的所有平台建置映像，且想要把該 manifest list／image index 一次 Push 上去，那麼可略過此步驟，直接前往[映像 Push](#6-3-3-映像-push)並依那裡的方式操作。
{: .prompt-tip }

##### Podman 的情況

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Docker 的情況

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. 映像 Push

最後，執行以下指令將映像 Push 到 Docker Hub。

##### Podman 的情況

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> 以 Podman 為例，若要把多平台對應的各個映像以 manifest list 或 image index 的方式打包後一次 Push，可使用 [`podman manifest push` 指令](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls)，如下所示。
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> 例如：
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### Docker 的情況

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

在 <https://hub.docker.com/> 可以確認已成功 Push，如下圖所示。

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

我已將經上述流程完成的映像公開在 Docker Hub 的 [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) 公開儲存庫中，任何人都可自由使用。

要 Pull 該映像時，只要把先前 Push 用的指令中的 `push` 改成 `pull` 再執行即可。
