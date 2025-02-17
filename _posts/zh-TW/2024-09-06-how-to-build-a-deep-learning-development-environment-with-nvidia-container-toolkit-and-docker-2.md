---
title: 使用NVIDIA Container Toolkit和Docker/Podman建立深度學習開發環境 (2) - 配置GPU容器運行時、編寫Dockerfile和構建容器映像
description: 本系列介紹如何在本地使用NVIDIA Container Toolkit建立基於容器的深度學習開發環境,並設置SSH和Jupyter Lab以便用作遠程服務器。這篇文章是該系列的第二篇,涵蓋了編寫Dockerfile和構建容器映像的過程。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---

## 概述

本系列介紹如何安裝NVIDIA Container Toolkit和Docker或Podman,並基於Docker Hub的[nvidia/cuda倉庫](https://hub.docker.com/r/nvidia/cuda)提供的CUDA和cuDNN映像編寫Dockerfile來構建深度學習開發環境。為了方便需要的人自由使用,我們通過GitHub和Docker Hub分享了這個過程中完成的[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)和[映像](https://hub.docker.com/r/yunseokim/dl-env/tags),並額外提供了用作遠程服務器的SSH和Jupyter Lab設置指南。
該系列將包含3篇文章,您正在閱讀的這篇是該系列的第二篇。

- [第1篇:安裝NVIDIA Container Toolkit和容器引擎](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 第2篇:配置GPU容器運行時、編寫Dockerfile和構建容器映像(本文)  
- 第3篇(計劃上傳)

我們假設在x86_64 Linux環境中使用支持CUDA的NVIDIA顯卡系統,並在Ubuntu或Fedora上進行。在其他發行版上可能會有一些細微的差異,因為我們沒有直接測試過。
(2025.02.18. 內容更新)

> **錯誤更正通知**  
> 在2024年8月上傳的這篇文章的初稿中,[編寫Dockerfile](#5-編寫dockerfile)部分的描述以及從該Dockerfile構建的映像中存在一些錯誤。問題部分如下:
> - 在創建remote帳戶部分,設置密碼的部分有誤,原本應該能夠使用"000000"作為密碼登錄,但實際上並不能
> - 容器啟動時SSH守護進程沒有自動運行
>
> 我們最近意識到了上述問題,並在韓國時間(UTC+9)2025年2月16日上午2點左右,將有問題的Dockerfile和Docker映像替換為解決問題的文件,上傳到了[GitHub倉庫](https://github.com/yunseo-kim/dl-env-docker)和[Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags)。
> 如果您在該時間之前Pull了Dockerfile或Docker映像,請替換為修改後的版本。
> 如果之前參考這篇文章的人因錯誤內容而感到困惑,我們深表歉意。
{: .prompt-info }

## 開始之前

這篇文章是[第1篇](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)的延續,如果您還沒有閱讀,建議先閱讀前一篇文章。

## 4. 配置容器運行時

### 使用Podman的情況

[使用CDI（Container Device Interface）進行配置。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

執行以下命令在`/etc/cdi`{: .filepath}目錄中生成CDI規範文件。

```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```

> 如果更換顯卡設備或更改CUDA驅動程序配置（包括版本升級）,需要重新生成CDI規範文件。
{: .prompt-warning }

> 將NVIDIA Container Runtime hook與CDI一起使用可能會發生衝突,因此如果存在`/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath},請刪除該文件或注意不要在設置了`NVIDIA_VISIBLE_DEVICES`環境變量的情況下運行容器。
{: .prompt-warning }

### 使用Docker的情況

以[無根（rootless）模式](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode)為例進行說明。

#### 4-Docker-1. 使用`nvidia-ctk`命令配置容器運行時設置

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

上述命令修改`/etc/docker/daemon.json`{: .filepath}文件,使Docker能夠利用NVIDIA Container Runtime。

#### 4-Docker-2. 重啟Docker守護進程

重啟Docker守護進程以應用更改的設置。

```bash
systemctl --user restart docker
```

#### 4-Docker-3. 使用`sudo nvidia-ctk`命令配置`/etc/nvidia-container-runtime/config.toml`{: .filepath}設置文件

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### 確認是否正確配置

運行示例CUDA容器進行測試。

使用Podman的情況下執行以下命令:

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

使用Docker的情況下執行以下命令:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

如果顯示類似以下的畫面,則表示成功:

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

- 需要考慮所需的CUDA和cuDNN版本、Linux發行版類型和版本等因素來決定使用哪個映像。
- ![PyTorch 2.4.0支持的CUDA版本](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)截至本文撰寫時間2024年8月底,PyTorch最新版本2.4.0支持CUDA 12.4。因此,這裡我們使用[12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)映像。您可以在[PyTorch官網](https://pytorch.org/get-started/locally/)查看PyTorch最新版本及其支持的CUDA版本。

完成的Dockerfile源碼已公開在[yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub倉庫中。以下逐步說明編寫該Dockerfile的過程。

### 5-1. 指定基礎映像

```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. 安裝基本工具和Python先決條件

```Dockerfile
# Install basic utilities and Python-related packages, gosu, and SSH server
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    apt-utils \
    curl \
    gosu \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip \
    ssh \
    tmux \
    && rm -rf /var/lib/apt/lists/* \
# verify that the binary works
    && gosu nobody true
```

### 5-3. 設置系統時區（本文以'Asia/Seoul'為例）

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. 設置SSH服務器以進行遠程訪問

為了安全起見,設置SSH遠程訪問時無法使用root帳戶登錄。

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

創建一個名為'remote'的非root用戶,用於SSH訪問。

```Dockerfile
# Create remote user (password can be passed to --build-arg at build time)
#
# This default password is very weak. Make sure to change it to your own unique
# password string!
#
# This Dockerfile assumes that the built image will only be used by yourself or
# a small group of trusted insiders, and if you need to distribute the image
# without exposing sensitive information, using --build-arg is dangerous.
# See the official Docker documentation.
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
ARG HOME_DIR="/home/$USER_NAME"
RUN useradd --create-home --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && echo "$USER_NAME:$USER_PASSWORD" | chpasswd
```

> 使用此Dockerfile構建Docker映像時,如果不指定其他選項,'remote'用戶的初始帳戶密碼為000000。這在安全性方面非常脆弱,因此在構建Docker映像時,請使用`--build-arg`選項單獨指定帳戶登錄密碼,或者在首次運行容器後立即更改設置。為了安全起見,最好在後續設置中禁用SSH訪問時的密碼登錄,只允許通過單獨的密鑰文件登錄,如果還能利用像Yubikey這樣的硬件密鑰,那就更理想了。
> 關於SSH服務器配置,我們將在本系列的下一篇中稍作介紹,如果想了解更多詳細信息,可以參考以下列表中的文檔:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> 此外,這個Dockerfile假設構建的映像只會由個人或少數可信的內部人員使用,如果需要將構建的映像分發給外部,通過`--build-arg`設置密碼是危險的,應該使用其他方法。請參考[這份文檔](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/)。
{: .prompt-danger }

### 5-5. 安裝setuptools、pip並註冊PATH環境變量

```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. 安裝開發環境中使用的機器學習和深度學習包

```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```

如果要使用Cupy、cuDF、cuML和DALI,還需要在Dockerfile中添加以下內容:

```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. 創建用作工作空間的目錄

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. 開放端口並設置容器啟動時執行的`ENTRYPOINT`

為了SSH和Jupyter Lab訪問,開放22和8888端口。
此外,由於在容器啟動時自動運行SSH守護進程需要root權限,我們將使用以下方法:
1. 容器啟動時以root帳戶登錄
2. 容器啟動後立即執行`/entrypoint.sh`{: .filepath}腳本
3. 該腳本啟動SSH服務後,使用[`gosu`](https://github.com/tianon/gosu)切換到remote帳戶
4. 如果運行容器時沒有單獨指定命令,則默認以remote帳戶（非root權限）運行Jupyter Lab

> 通常不建議在Docker或Podman容器內使用`sudo`或`su`,如果需要root權限,最好像這裡解釋的那樣,先以root帳戶啟動容器,執行需要root權限的任務後,使用[`gosu`](https://github.com/tianon/gosu)切換到非root用戶。以下資料詳細解釋了為什麼要這樣做,如有需要可以參考:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

首先,在Dockerfile的最後部分輸入以下內容:

```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

接下來,在與編寫的Dockerfile相同的路徑下創建一個名為`entrypoint.sh`{: .filepath}的腳本文件,內容如下:

```sh
#!/bin/bash
set -e

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

## 6. 構建Docker映像和運行容器

### 6-1. 構建映像

在Dockerfile所在的目錄中打開終端,執行以下命令:

```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```

> 在<password>處輸入SSH訪問時要使用的登錄密碼。
{: .prompt-info }

### 6-2. 運行示例工作負載

完成構建後,運行一次性容器以確認是否正常運行。

對於Podman,執行以下命令:

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

對於Docker,執行以下命令:

```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

在終端中輸入上述命令後,將從之前構建的`dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04`映像運行名為`test-container`的容器,並將主機系統的22端口與該容器的22端口,主機系統的88端口與容器的8888端口分別連接。如果在前面的步驟中Docker映像正常構建並且容器順利啟動,那麼`test-container`容器內部應該正在默認地址`http:127.0.0.1:8888`上運行JupyterLab。因此,在運行Docker Engine的主機系統上打開瀏覽器並訪問<http://127.0.0.1:88>時,應該連接到容器內部的`http://127.0.0.1:8888`地址,並顯示如下畫面:

![JupyterLab界面截圖](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

在主機系統上打開終端,執行`ssh remote@127.0.0.1`命令,嘗試遠程登錄到容器內部運行的Ubuntu系統的remote帳戶。
首次登錄時會出現警告,說明沒有連接目標的加密密鑰信息,無法進行認證,並詢問是否繼續連接,輸入"yes"繼續進行即可。
然後輸入登錄密碼（如果在構建映像時沒有特別更改,默認值應該是"000000"）。

```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {指紋（每個密鑰都有不同的唯一值）}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '127.0.0.1' (ED25519) to the list of known hosts.
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

如果顯示類似上述內容,則表示通過SSH成功遠程登錄。要結束連接,輸入`exit`命令即可。

### 6-3. (可選) 推送到Docker Hub

如果想隨時Pull並使用通過上述過程創建的開發環境映像,最好將構建的映像推送到Docker Hub。

> 要將自己的映像推送到Docker Hub,需要有自己的Docker帳戶,如果還沒有,請先在<https://app.docker.com/signup>完成註冊。
{: .prompt-tip }

#### 6-3-1. 登錄Docker Hub

##### 對於Podman

```bash
podman login docker.io
```

##### 對於Docker

```bash
docker login
```

#### 6-3-2. 指定映像標籤

在`<dockerhub_username>`、`<repository_name>`和(可選)`:TAG`部分填入您自己的相關內容。
例如："yunseokim"、"dl-env"、"rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### 對於Podman

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### 對於Docker

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. 推送映像

最後,執行以下命令將該映像推送到Docker Hub。

##### 對於Podman

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### 對於Docker

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

您可以在<https://hub.docker.com/>上確認是否成功推送,如下圖所示。
![Docker Hub截圖](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

通過上述過程完成的映像已公開在Docker Hub的[yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags)公共倉庫中,任何人都可以自由使用。

要Pull映像,只需將前面Push時使用的命令中的`push`部分改為`pull`即可。
