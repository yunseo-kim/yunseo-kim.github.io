---
title: 使用NVIDIA Container Toolkit和Docker建立深度學習開發環境 (2) - 配置GPU容器運行時、編寫Dockerfile和構建Docker映像
description: 本系列介紹如何在本地使用NVIDIA Container Toolkit和Docker建立深度學習開發環境,並設置SSH和Jupyter Lab以便遠程使用。這篇文章是該系列的第二篇,介紹如何配置GPU容器運行時、編寫Dockerfile和構建Docker映像。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---

## 概述

本系列將介紹安裝NVIDIA Container Toolkit和Docker,並基於Docker Hub的[nvidia/cuda倉庫](https://hub.docker.com/r/nvidia/cuda)提供的CUDA和cuDNN映像編寫Dockerfile來構建深度學習開發環境的過程。為了方便需要的人自由使用,我將通過這個過程完成的[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)和[映像](https://hub.docker.com/r/yunseokim/dl-env/tags)分享在GitHub和Docker Hub上,並額外提供用於遠程服務器的SSH和Jupyter Lab設置指南。
該系列將由3篇文章組成,您正在閱讀的這篇是該系列的第二篇。
- [第1篇:安裝NVIDIA Container Toolkit和Docker Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 第2篇:配置GPU容器運行時、編寫Dockerfile和構建Docker映像(本文)
- 第3篇(計劃上傳)

我們假設在x86_64 Linux環境中使用支持CUDA的NVIDIA顯卡系統進行,由於我沒有在Ubuntu或Fedora以外的發行版上直接測試過,某些細節可能會略有不同。

## 開始之前

這篇文章是[第1篇](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)的延續,如果您還沒有閱讀,建議先閱讀前一篇文章。

## 4. 配置容器運行時

### 4-1. 執行`nvidia-ctk`命令

```bash
sudo nvidia-ctk runtime configure --runtime=docker
```

上述命令修改`/etc/docker/daemon.json`{: .filepath}文件,使Docker能夠利用NVIDIA Container Runtime。

### 4-2. 重啟Docker守護進程

重啟Docker守護進程以應用更改的設置。

```bash
sudo systemctl restart docker
```

### 4-3. 確認是否正確配置

運行示例CUDA容器進行測試。

```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

如果顯示類似以下的畫面,則表示成功。

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

## 5. 編寫Dockerfile

基於Docker Hub的[nvidia/cuda倉庫](https://hub.docker.com/r/nvidia/cuda)提供的CUDA和cuDNN映像,編寫用作開發環境的Dockerfile。

- 需要考慮所需的CUDA和cuDNN版本、Linux發行版類型和版本等來決定使用哪個映像。
- ![PyTorch 2.4.0支持的CUDA版本](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)截至本文撰寫時間2024年8月底,PyTorch最新版本2.4.0支持CUDA 12.4。因此,這裡我們使用[12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)映像。您可以在[PyTorch官網](https://pytorch.org/get-started/locally/)查看PyTorch最新版本及其支持的CUDA版本。

完成的Dockerfile源碼已公開在[yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub倉庫中。以下逐步說明編寫該Dockerfile的過程。

### 5-1. 指定基礎映像

```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. 安裝基本工具和Python先決條件

```Dockerfile
RUN apt-get update -y && apt-get install -y --no-install-recommends\
    apt-utils \
    ssh \
    curl \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*
```

### 5-3. 設置系統時區(本文以'Asia/Taipei'為例)

```Dockerfile
# Set up time zone
ARG TZ="Asia/Taipei"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. 配置SSH服務器以進行遠程訪問

為了安全起見,設置SSH遠程訪問時禁止使用密碼登錄root帳戶。

```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```

配置容器啟動時自動啟動SSH服務。

```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```

創建一個名為'remote'的非root用戶用於SSH連接。

```Dockerfile
# Create a non-root user and switch to it
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
RUN useradd --create-home --password $USER_PASSWORD $USER_NAME
ENV HOME=/home/$USER_NAME
USER $USER_NAME
WORKDIR $HOME
# Re-run ssh when the container restarts.
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
# Create a workspace directory to locate jupyter notebooks and .py files
RUN mkdir -p $HOME/workspace
```

> 使用此Dockerfile構建Docker映像時,如果不指定其他選項,'remote'用戶的初始帳戶密碼為000000。這在安全性上非常脆弱,因此在構建Docker映像時請使用`--build-arg`選項指定帳戶登錄密碼,或者在首次運行容器後立即更改設置。為了安全起見,最好禁用SSH連接時的密碼登錄,只允許通過單獨的密鑰文件登錄,如果再使用Yubikey等硬件密鑰則更理想。
> 關於SSH服務器配置,將在本系列的下一篇中進行一些介紹,如果想了解更多細節,可以參考以下文檔列表:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. 安裝setuptools、pip並註冊PATH環境變量

```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. 安裝開發環境中使用的機器學習和深度學習套件

```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

如果要使用Cupy、cuDF、cuML和DALI,還需要在Dockerfile中添加以下內容:

```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. 設置容器啟動時運行JupyterLab

```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
```

## 6. 構建Docker映像和運行容器

### 6-1. 構建映像

在Dockerfile所在目錄中打開終端,執行以下命令:

```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```

> 在<password>處輸入SSH連接時要使用的登錄密碼。
{: .prompt-info }

### 6-2. 運行示例工作負載

完成構建後,使用以下命令運行一次性容器以檢查是否正常運行:

```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

在終端中輸入上述命令後,將從之前構建的`dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04`映像運行名為`test-container`的容器,並將主機系統的88端口連接到該容器的8888端口。如果前面步驟中Docker映像正確構建並且容器順利啟動,`test-container`容器內部應該正在默認地址`http:127.0.0.1:8888`上運行JupyterLab。因此,在運行Docker Engine的主機系統上打開瀏覽器並訪問<http://127.0.0.1:88>時,應該連接到容器內部的`http://127.0.0.1:8888`地址,並顯示如下畫面:

![JupyterLab界面截圖](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (可選) 推送到Docker Hub

如果想隨時Pull並使用通過上述過程創建的開發環境映像,最好將構建的映像推送到Docker Hub。

> 要將自己的映像推送到Docker Hub,需要有自己的Docker帳戶,如果還沒有,請先在<https://app.docker.com/signup>完成註冊。
{: .prompt-tip }

首先,使用以下命令登錄Docker Hub:

```bash
docker login
```

現在,執行以下格式的命令創建映像標籤:

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

最後,執行以下命令將該映像推送到Docker Hub:

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

您可以在<https://hub.docker.com/>上確認是否成功推送,如下圖所示:
![Docker Hub截圖](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

通過上述過程完成的映像已公開在Docker Hub的[yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags)公共倉庫中,任何人都可以自由使用。
