---
title: 使用NVIDIA Container Toolkit和Docker建立深度學習開發環境 (1) - 安裝NVIDIA Container Toolkit
  和Docker Engine
description: 本系列介紹如何在本地建立基於NVIDIA Container Toolkit和Docker的深度學習開發環境,並設置SSH和Jupyter
  Lab以便遠程使用。這是系列的第一篇文章,介紹NVIDIA Container Toolkit的安裝方法。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## 概述
本系列將介紹安裝NVIDIA Container Toolkit和Docker,並基於Docker Hub的[nvidia/cuda倉庫](https://hub.docker.com/r/nvidia/cuda)提供的CUDA和cuDNN映像編寫Dockerfile來建立深度學習開發環境的過程。為了方便需要的人自由使用,我們將通過這個過程完成的[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)和[映像](https://hub.docker.com/r/yunseokim/dl-env/tags)分享在GitHub和Docker Hub上,並額外提供用於遠程服務器的SSH和Jupyter Lab設置指南。  
該系列將包含3篇文章,您正在閱讀的是該系列的第一篇。
- 第1篇:安裝NVIDIA Container Toolkit和Docker Engine(本文)
- [第2篇:配置用於GPU利用的容器運行時,編寫Dockerfile和構建Docker映像](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 第3篇(計劃上傳)

我們假設在x86_64 Linux環境中使用支持CUDA的NVIDIA顯卡系統,並進行操作。除Ubuntu或Fedora以外的發行版,由於未親自測試,某些細節可能略有不同。

### 開發環境配置
- 主機操作系統和架構:x86_64,Linux環境(Ubuntu 18.04/20.04/22.04 LTS、RHEL/Centos、Fedora、openSUSE/SLES 15.x等)
- 要構建的技術棧(語言和庫)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE
  - CUDA 12.4
  - cuDNN
  - JupyterLab
  - NumPy & SciPy
  - CuPy (可選,用於GPU加速計算的NumPy/SciPy兼容數組庫)
  - pandas
  - cuDF (可選,無需代碼更改即可使用GPU加速器加速pandas)
  - Matplotlib & Seaborn
  - DALI (可選,使用GPU的高性能內置數據加載器和數據迭代器替代方案)
  - scikit-learn
  - cuML (可選,在GPU上執行機器學習算法,API與scikit-learn API非常相似)
  - PyTorch
  - OpenSSH
  - tqdm

  > 根據情況和個人偏好,可以考慮使用[Polars](https://pola.rs/) DataFrame庫代替pandas。它是用Rust編寫的,[在處理大量數據時性能不如cuDF + pandas組合,但與純pandas包相比性能相當出色](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/),並提供更專門的查詢語法。根據[Polars官方博客](https://pola.rs/posts/polars-on-gpu/),他們正在與NVIDIA RAPIDS團隊合作,計劃在不久的將來支持與cuDF的集成。
  {: .prompt-tip }

### 與之前撰寫的機器學習開發環境設置指南的比較表
[之前在這個博客上傳的機器學習開發環境設置指南](/posts/Setting-up-a-Machine-Learning-Development-Environment)仍然大部分有效,但有一些變化,所以我重新寫了這篇文章。變化如下表所示:

| 差異 | 舊文章 (2021版) | 本文 (2024版) |
| --- | --- | --- |
| Linux發行版 | 以Ubuntu為基準 | 除Ubuntu外,也適用於Fedora/RHEL/Centos、<br>Debian、openSUSE/SLES等 |
| 開發環境構建方式 | 使用venv的Python虛擬環境 | 基於[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)的<br>Docker容器環境 |
| NVIDIA顯卡驅動安裝 | O | O |
| 在主機系統上直接安裝<br>CUDA和cuDNN | O (使用Apt包管理器) | X (使用[Docker Hub上NVIDIA提供的預安裝映像](https://hub.docker.com/r/nvidia/cuda),<br>因此無需直接操作)
| 可移植性 | 每次遷移到其他系統時<br>都需要重新構建開發環境 | 基於Docker,因此可以使用製作好的Dockerfile<br>在需要時構建新映像,或輕鬆移植現有映像<br>(除額外卷或網絡設置外) |
| 使用cuDNN以外的<br>額外GPU加速庫 | X | 引入[CuPy](https://cupy.dev/)、[cuDF](https://docs.rapids.ai/api/cudf/stable/)、[cuML](https://docs.rapids.ai/api/cuml/stable/)、[DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook界面 | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH服務器設置 | 未單獨介紹 | 第3篇將包括基本的SSH服務器設置配置 |

如果想使用venv等Python虛擬環境而不是Docker,[舊文章](/posts/Setting-up-a-Machine-Learning-Development-Environment)仍然有效,建議參考該文章。

## 0. 預檢事項
- [NVIDIA Container Toolkit可在支持Apt、Yum或Dnf、Zypper包管理器的Linux發行版上使用。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html)可以在鏈接的頁面查看支持的Linux發行版列表,雖然官方支持表中未單獨列出,但Fedora作為基於Red Hat Linux的發行版也可以正常使用。如果您不熟悉Linux環境且不確定應該使用哪個發行版,使用Ubuntu LTS版本是最穩妥的選擇。它會自動安裝非開源的專有驅動程序,相對容易上手,而且由於用戶數量眾多,大多數技術文檔都是以Ubuntu為基準編寫的。
  - 可以在終端中使用`uname -m && cat /etc/*release`命令檢查您正在使用的系統架構和Linux發行版版本。
- 首先要確認系統中安裝的顯卡是否支持您想使用的CUDA和cuDNN版本。
  - 可以在終端中使用`lspci | grep -i nvidia`命令檢查當前計算機安裝的GPU型號。
  - 在<https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>頁面可以查看每個cuDNN版本**支持的NVIDIA顯卡驅動版本**、要求的**CUDA Compute Capability**條件,以及**支持的NVIDIA硬件**列表。
  - 在<https://developer.nvidia.com/cuda-gpus>的GPU列表中找到相應的型號,然後檢查**Compute Capability**數值。這個數值必須滿足前面確認的**CUDA Compute Capability**條件,才能正常使用CUDA和cuDNN。

> 如果計劃購買新的深度學習用顯卡,以下文章很好地總結了GPU選擇標準。作者持續更新這篇文章。  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> 同一作者撰寫的[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)也非常有用。
{: .prompt-tip }

如果滿足上述所有條件,讓我們開始構建工作環境。

## 1. 安裝NVIDIA顯卡驅動
首先需要在主機系統上安裝NVIDIA顯卡驅動。可以從[NVIDIA驅動下載頁面](https://www.nvidia.com/drivers/)下載.run安裝程序使用,但最好使用系統的包管理器進行安裝,這樣在版本管理和維護方面更好。參考<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>官方文檔,安裝適合您系統環境的顯卡驅動。

### 專有模塊 vs 開源模塊
NVIDIA Linux驅動由幾個內核模塊組成,從515版驅動及之後的發布版本開始,NVIDIA提供兩種類型的驅動內核模塊。

- 專有:NVIDIA一直提供的專有軟件驅動。
- 開源:以MIT/GPLv2雙重許可提供的開源驅動。通過<https://github.com/NVIDIA/open-gpu-kernel-modules>公開源代碼。

專有驅動提供對從Maxwell架構到Blackwell之前的架構設計的GPU的支持,並將在Blackwell架構後停止支持。
相反,開源驅動支持Turing及之後的架構。

[NVIDIA建議盡可能使用開源內核模塊。](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
可以在[此鏈接](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus)檢查您使用的GPU是否與開源驅動兼容。

本文假設安裝開源驅動進行說明。

### Debian & Ubuntu
對於Ubuntu或Debian,在終端中輸入以下命令進行安裝:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
以Fedora 40為例,介紹從[RPM Fusion](https://rpmfusion.org/RPM%20Fusion)下載預構建包進行安裝的方法。

#### 1-Fedora-1. 配置RPM Fusion倉庫  
參考[RPM Fusion官方指南](https://rpmfusion.org/Configuration)進行操作。  
在終端中執行以下命令:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. 安裝akmod-nvidia-open包  
參考[RPM Fusion提供的NVIDIA驅動安裝指南](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open),
啟用rpmfusion-nonfree-tainted倉庫,然後安裝akmod-nvidia-open包。
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. 安全啟動(Secure Boot)時註冊密鑰以正常加載驅動  

> 只需按照下面說明的簡單額外步驟,就可以正常使用安全啟動功能並使用NVIDIA顯卡驅動。禁用安全啟動會使系統安全性大大降低,因此建議不要禁用。至少在2020年代之後,幾乎沒有理由禁用安全啟動。
{: .prompt-danger }

首先安裝以下工具:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

接下來,執行以下命令生成密鑰:
```bash
sudo kmodgenca -a
```
現在需要在UEFI固件的MOK中註冊生成的密鑰。
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
執行上述命令後,會提示輸入密鑰註冊密碼。稍後將重啟以完成密鑰註冊程序,這是一次性密碼,請輸入一個您能記住的密碼。

現在執行以下命令重啟系統:
```bash
systemctl reboot
```
系統啟動時會自動出現MOK管理窗口。選擇"Enroll MOK",然後連續選擇"Continue"、"Yes",會出現要求剛才設置的密碼的窗口。輸入之前設置的密碼後,密鑰註冊程序就完成了。現在輸入reboot再次重啟,NVIDIA驅動就會正常加載。

### 確認NVIDIA驅動安裝
在終端中執行以下命令可以檢查當前加載的NVIDIA內核模塊:
```bash
cat /proc/driver/nvidia/version
```
如果輸出類似以下消息,則表示安裝正常:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. 安裝NVIDIA Container Toolkit
現在需要安裝[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)。參考[NVIDIA Container Toolkit官方安裝指南](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)進行安裝,但對於Fedora,安裝過程中有注意事項,請在開始之前仔細閱讀本節內容。

### 使用Apt的情況 (Ubuntu、Debian等)
#### 2-Apt-1. 配置用於下載包的倉庫
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. 更新包列表
```bash
sudo apt update
```

#### 2-Apt-3. 安裝包
```bash
sudo apt install nvidia-container-toolkit
```

### 使用Yum或Dnf的情況 (Fedora、RHEL、Centos等)
> 在Fedora 40上測試時,與Ubuntu不同,`nvidia-smi`命令和`nvidia-persistenced`包不包含在NVIDIA顯卡驅動中,需要額外安裝`xorg-x11-drv-nvidia-cuda`包。雖然沒有直接在RHEL和Centos上測試,但由於它們的系統配置與Fedora非常相似,如果按照以下指南操作時出現問題,嘗試相同的方法可能會有幫助。
{: .prompt-warning }

> 在Fedora 40上按照上述方法安裝`xorg-x11-drv-nvidia-cuda`並運行示例工作負載進行測試時,在作者的系統上正常運行。如果由於SELinux等原因仍然出現問題,Fedora的AI-ML組提供的[Fedora專用nvidia-container-toolkit包和指南](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/)可能會有幫助。
{: .prompt-tip }

#### 2-Dnf-1. 配置用於下載包的倉庫
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. 安裝包
```bash
sudo dnf install nvidia-container-toolkit
```
或
```bash
sudo yum install nvidia-container-toolkit
```

### 使用Zypper的情況 (openSUSE、SLES)
#### 2-Zypper-1. 配置用於下載包的倉庫
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. 安裝包
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. 安裝Docker Engine
接下來安裝Docker Engine。參考[Docker官方文檔](https://docs.docker.com/engine/install/)進行安裝。

### Ubuntu的情況
#### 3-Ubuntu-1. 移除舊版本或非官方包以防止包衝突
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

#### 3-Ubuntu-2. 配置倉庫
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

#### 3-Ubuntu-3. 安裝包
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 3-Ubuntu-4. 創建`Docker`組並註冊用戶  
要讓非root用戶無需`sudo`即可管理Docker,可以創建`Docker`組,然後將想使用Docker的用戶註冊到該組。在終端中執行以下命令:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
之後註銷並重新登錄,修改的設置就會生效。對於Ubuntu或Debian,無需額外操作,Docker服務會在每次系統啟動時自動運行。

### Fedora的情況
#### 3-Fedora-1. 移除舊版本或非官方包以防止包衝突
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

#### 3-Fedora-2. 配置倉庫
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

#### 3-Fedora-3. 安裝包  
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
在包安裝過程中,會出現是否批准GPG密鑰的提示。如果GPG密鑰與`060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`一致,輸入y批准即可。  
> 如果GPG密鑰不一致,可能是下載了被供應鏈攻擊偽造的包,應該中止安裝。
{: .prompt-danger }

#### 3-Fedora-4. 啟動Docker守護進程  
現在Docker已安裝但未運行,可以輸入以下命令啟動Docker:
```bash
sudo systemctl start docker
```
要使Docker服務在系統啟動時自動運行,執行以下命令:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

#### 3-Fedora-5. 將用戶註冊到`Docker`組  
要讓非root用戶也能管理Docker,將想使用Docker的用戶註冊到`Docker`組。對於Fedora,在之前的包安裝過程中已自動創建了`Docker`組,因此只需進行用戶註冊。
```bash
sudo usermod -aG docker $USER
```
之後註銷並重新登錄,修改的設置就會生效。

### 確認是否正確設置  
在終端中執行以下命令:
```bash
docker run hello-world
```
如果輸出以下消息,則表示成功:

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

## 延伸閱讀
繼續閱讀[第2部分](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
