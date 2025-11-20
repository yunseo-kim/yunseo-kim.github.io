---
title: 使用NVIDIA Container Toolkit與Docker/Podman建立深度學習開發環境 (1) - NVIDIA Container Toolkit
  & 容器引擎安裝
description: 本系列介紹如何使用NVIDIA Container Toolkit在本地建立容器化的深度學習開發環境，並設置SSH和Jupyter
  Lab以便能夠作為遠端伺服器使用。這篇文章是系列的第一部分，介紹NVIDIA Container Toolkit和容器引擎的安裝方法。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---
## 概述
本系列將介紹如何安裝NVIDIA Container Toolkit和Docker或Podman，並基於Docker Hub的[nvidia/cuda儲存庫](https://hub.docker.com/r/nvidia/cuda)提供的CUDA和cuDNN映像檔來編寫Dockerfile，建立深度學習開發環境。為了讓有需要的人能夠自由使用，我將通過這個過程完成的[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)和[映像檔](https://hub.docker.com/r/yunseokim/dl-env/tags)分享在GitHub和Docker Hub上，並額外提供將其用作遠端伺服器的SSH和Jupyter Lab設定指南。  
本系列預計包含三篇文章，您正在閱讀的是系列的第一篇。
- 第1篇：安裝NVIDIA Container Toolkit和容器引擎（本文）
- [第2篇：GPU利用的容器運行時配置、Dockerfile編寫及容器映像檔建立](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 第3篇（即將上傳）

本文假設在x86_64 Linux環境中使用支援CUDA的NVIDIA顯示卡系統，並且主要在Ubuntu或Fedora上進行測試，其他發行版可能在某些細節上有所不同。  
（12025.02.18. 內容更新）

### 開發環境配置
- 主機作業系統和架構：x86_64，Linux環境（Ubuntu 18.04/20.04/22.04 LTS、RHEL/Centos、Fedora、openSUSE/SLES 15.x等）
- 要建立的技術堆疊（語言和函式庫）
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE / Podman
  - CUDA 12.4
  - cuDNN
  - OpenSSH
  - tmux
  - JupyterLab
  - NumPy & SciPy
  - CuPy（可選，用於GPU加速計算的NumPy/SciPy兼容陣列函式庫）
  - pandas
  - cuDF（可選，無需修改代碼即可使用GPU加速pandas）
  - Matplotlib & Seaborn
  - DALI（可選，使用GPU的高性能數據加載器和數據迭代器替代方案）
  - scikit-learn
  - cuML（可選，在GPU上執行機器學習算法，API與scikit-learn非常相似）
  - PyTorch
  - tqdm

  > 根據情況和個人偏好，可以考慮使用[Polars](https://pola.rs/)DataFrame函式庫代替pandas。它是用Rust編寫的，[在處理大量數據時雖然比不上cuDF + pandas組合，但與純pandas相比性能卓越](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/)，並提供更專注於查詢的語法。根據[Polars官方部落格](https://pola.rs/posts/polars-on-gpu/)，他們正與NVIDIA RAPIDS團隊合作，計劃在不久的將來支援與cuDF的整合。
  {: .prompt-tip }

  > 如果您在考慮使用Docker CE還是Podman，[後文的比較表](#3-容器引擎安裝)可能會有所幫助。
  {: .prompt-tip }

### 與先前發布的機器學習開發環境建立指南的比較
[本部落格先前發布的機器學習開發環境建立指南](/posts/Setting-up-a-Machine-Learning-Development-Environment)大部分內容仍然有效，但有一些變更，因此我撰寫了這篇新文章。主要差異如下表所示：

| 差異點 | 舊文章（12021版本） | 本文（12024版本） |
| --- | --- | --- |
| Linux發行版 | 以Ubuntu為基準 | 除Ubuntu外，也適用於Fedora/RHEL/Centos、<br>Debian、openSUSE/SLES等 |
| 開發環境建立方式 | 使用venv的Python虛擬環境 | 使用[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)的<br>Docker容器環境 |
| NVIDIA顯示驅動安裝 | O | O |
| 在主機系統上<br>直接安裝CUDA和cuDNN | O（使用Apt套件管理器） | X（使用[Docker Hub上NVIDIA提供的預安裝映像檔](https://hub.docker.com/r/nvidia/cuda)，<br>無需直接操作） |
| 可移植性 | 每次更換系統都需要<br>重新建立開發環境 | 基於Docker，可以使用已製作的Dockerfile<br>隨時建立新映像檔，或輕鬆移植現有映像檔<br>（不包括額外的卷或網絡設定） |
| 除cuDNN外的<br>其他GPU加速函式庫 | X | 引入[CuPy](https://cupy.dev/)、[cuDF](https://docs.rapids.ai/api/cudf/stable/)、<br>[cuML](https://docs.rapids.ai/api/cuml/stable/)、[DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook介面 | Jupyter Notebook（經典版） | JupyterLab（下一代版本） |
| SSH伺服器設定 | 未涵蓋 | 第3篇將包含基本SSH伺服器設定 |

如果您想使用venv等Python虛擬環境而非Docker，[舊文章](/posts/Setting-up-a-Machine-Learning-Development-Environment)仍然有效，建議參考該文。

## 0. 前置檢查事項
- [NVIDIA Container Toolkit可在支援Apt、Yum或Dnf、Zypper套件管理器的Linux發行版上使用。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html)您可以在連結頁面查看支援的Linux發行版列表。雖然官方支援表中未特別列出，但Fedora作為基於Red Hat Linux的發行版，也可以正常使用。如果您不熟悉Linux環境且不確定應該使用哪個發行版，Ubuntu LTS版本是最穩妥的選擇。它會自動安裝非開源的專有驅動程式，對初學者相對友好，且由於用戶眾多，大多數技術文檔都以Ubuntu為基準編寫。
  - 您可以在終端機中執行`uname -m && cat /etc/*release`命令來檢查您的系統架構和Linux發行版版本。
- 首先需要確認系統中的顯示卡是否支援您想使用的CUDA和cuDNN版本。
  - 您可以在終端機中執行`lspci | grep -i nvidia`命令來檢查當前電腦安裝的GPU型號。
  - 在<https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>頁面可以查看各cuDNN版本**支援的NVIDIA顯示驅動版本**、要求的**CUDA Compute Capability**條件，以及**支援的NVIDIA硬體**列表。
  - 在<https://developer.nvidia.com/cuda-gpus>的GPU列表中找到您的型號，然後檢查其**Compute Capability**數值。這個數值必須滿足前面確認的**CUDA Compute Capability**條件，才能正常使用CUDA和cuDNN。

> 如果您計劃購買新的深度學習用顯示卡，以下文章很好地總結了GPU選擇標準。作者持續更新這篇文章。  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> 同一作者撰寫的[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)也非常有用。
{: .prompt-tip }

如果您滿足上述所有條件，就可以開始建立工作環境了。

## 1. 安裝NVIDIA顯示驅動
首先需要在主機系統上安裝NVIDIA顯示驅動。您可以從[NVIDIA驅動下載頁面](https://www.nvidia.com/drivers/)下載.run安裝程式，但從維護和版本管理角度來看，最好使用系統的套件管理器進行安裝。請參考<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>官方文檔，根據您的系統環境安裝適合的顯示驅動。

### 專有模組 vs 開源模組
NVIDIA Linux驅動由幾個核心模組組成，從版本515驅動及之後的版本開始，NVIDIA提供兩種類型的驅動核心模組：

- 專有（Proprietary）：NVIDIA一直提供的專有軟體驅動。
- 開源（Open-source）：以MIT/GPLv2雙授權提供的開源驅動。源代碼通過<https://github.com/NVIDIA/open-gpu-kernel-modules>公開。

專有驅動支援從Maxwell架構到Blackwell之前的架構設計的GPU，並將在Blackwell架構後停止支援。
而開源驅動支援Turing及之後的架構。

[NVIDIA建議盡可能使用開源核心模組。](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
您可以在[此連結](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus)檢查您的GPU是否與開源驅動兼容。

本文假設安裝開源驅動進行說明。

### Debian & Ubuntu
對於Ubuntu或Debian，在終端機中輸入以下命令進行安裝：
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
以Fedora 40為例，介紹使用[RPM Fusion](https://rpmfusion.org/RPM%20Fusion)提供的預編譯套件的安裝方法。

#### 1-Fedora-1. 配置RPM Fusion儲存庫  
參考[RPM Fusion官方指南](https://rpmfusion.org/Configuration)進行。  
在終端機中執行以下命令：
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. 安裝akmod-nvidia-open套件  
參考[RPM Fusion提供的NVIDIA驅動安裝指南](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open)，
啟用rpmfusion-nonfree-tainted儲存庫，然後安裝akmod-nvidia-open套件：
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark user akmod-nvidia-open
```

> 在DNF舊版本（Fedora 40及更早版本）中，為了在執行最後一行的autoremove時防止NVIDIA驅動被刪除，應使用以下命令：
>
> ```bash
> sudo dnf mark install akmod-nvidia-open
> ```
>
> 但從DNF 5（Fedora 41+）開始，必須改為輸入下列指令：
>
> ```bash
> sudo dnf mark user akmod-nvidia-open
> ```
>
> 本文內容已依此更新。
{: .prompt-tip }

#### 1-Fedora-3. 安全啟動（Secure Boot）時驅動正常載入的金鑰註冊  

> 只需完成下面說明的額外步驟，就能在啟用安全啟動的情況下正常使用NVIDIA顯示驅動。禁用安全啟動會使系統安全性大幅降低，因此不建議禁用。至少在進入12020年代後，幾乎沒有理由禁用安全啟動。
{: .prompt-danger }

首先安裝以下工具：
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

接著，執行以下命令生成金鑰：
```bash
sudo kmodgenca -a
```
現在需要將生成的金鑰註冊到UEFI韌體的MOK中：
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
執行此命令後，系統會要求輸入金鑰註冊密碼。稍後需要重新啟動完成金鑰註冊程序，這是一次性密碼，請輸入您能記住的密碼。

現在執行以下命令重新啟動系統：
```bash
systemctl reboot
```
系統啟動時會自動出現MOK管理視窗。選擇"Enroll MOK"，然後依次選擇"Continue"和"Yes"，接著會出現要求輸入密碼的視窗。輸入剛才設定的密碼後，金鑰註冊程序就完成了。輸入reboot再次重新啟動，NVIDIA驅動就會正常載入。

### 確認NVIDIA驅動安裝
在終端機中執行以下命令，檢查當前載入的NVIDIA核心模組：
```bash
cat /proc/driver/nvidia/version
```
如果輸出類似以下訊息，則表示安裝成功：
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. 安裝NVIDIA Container Toolkit
現在需要安裝[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)。參考[NVIDIA Container Toolkit官方安裝指南](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)進行安裝，但Fedora用戶請注意安裝過程中的特殊事項，請在開始前閱讀完本節內容。

### 使用Apt的情況（Ubuntu、Debian等）
#### 2-Apt-1. 配置下載套件的儲存庫
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. 更新套件列表
```bash
sudo apt update
```

#### 2-Apt-3. 安裝套件
```bash
sudo apt install nvidia-container-toolkit
```

### 使用Yum或Dnf的情況（Fedora、RHEL、Centos等）
> 在Fedora 40測試時，與Ubuntu不同，`nvidia-smi`命令和`nvidia-persistenced`套件並未包含在NVIDIA顯示驅動中，需要額外安裝`xorg-x11-drv-nvidia-cuda`套件。雖然未在RHEL和Centos上直接測試，但由於它們與Fedora系統配置非常相似，如果按照下面的指南操作時遇到問題，嘗試相同的方法可能會有所幫助。
{: .prompt-warning }

> 在Fedora 40上按照上述方法安裝`xorg-x11-drv-nvidia-cuda`並運行測試工作負載時，在筆者的系統上正常運作。如果由於SELinux等原因仍然出現問題，Fedora的AI-ML小組提供的[Fedora專用nvidia-container-toolkit套件和指南](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/)可能會有所幫助。
{: .prompt-tip }

#### 2-Dnf-1. 配置下載套件的儲存庫
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. 安裝套件
```bash
sudo dnf install nvidia-container-toolkit
```
或
```bash
sudo yum install nvidia-container-toolkit
```

### 使用Zypper的情況（openSUSE、SLES）
#### 2-Zypper-1. 配置下載套件的儲存庫
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. 安裝套件
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. 容器引擎安裝
接下來安裝Docker CE或Podman作為容器引擎。根據您的使用環境和偏好選擇其中一個進行安裝，可參考[Docker官方文檔](https://docs.docker.com/engine/install/)和[Podman官方文檔](https://podman.io/docs/installation)。

下表總結了Docker和Podman的主要差異和優缺點：

| 比較項目 | Docker | Podman |
| --- | --- | --- |
| 架構 | 客戶端-伺服器模型，基於守護進程(daemon) | 無守護進程(daemonless)結構 |
| 安全性 | 依賴於預設以root權限運行的守護進程，<br>存在潛在安全風險（12020年發布的20.10版本<br>開始支援無根模式，但需要額外設定） | 不依賴守護進程，除非特別指定，<br>預設以無根模式運行，並受SELinux保護 |
| 資源使用量 | 由於守護進程架構特性，背景進程<br>持續運行，通常消耗更多資源 | 通常有更少的資源開銷(overhead) |
| 容器啟動時間 | 相對較慢 | 簡化的架構使其執行速度<br>最多快50% |
| 生態系統和文檔 | 廣泛的生態系統和社區支持，<br>豐富的相關文檔 | 相對較小的生態系統和相關文檔 |
| 網絡 | 使用Docker Bridge Network | 使用CNI(Container Network Interface)<br>插件 |
| Kubernetes YAML<br>原生支持 | X（需要轉換） | O |

參考資料：
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker歷史更悠久，在業界已成為事實上的標準，因此擁有廣泛的生態系統和豐富的相關文檔，這是其最大優勢。  
Podman由Red Hat相對較近期開發，從設計之初就追求無守護進程(daemonless)、無根(rootless)的先進架構，在安全性、系統資源使用量和容器啟動時間等多方面具有優勢。與Docker相比，當守護進程出現問題導致所有容器一起崩潰不同，Podman中每個容器完全獨立，特定容器的崩潰不會影響其他容器，這也是Podman的強項。

根據各自的條件選擇適合的工具最為重要。對於初次接觸的個人用戶，從Podman開始可能是個不錯的選擇。雖然相對Docker生態系統規模較小，但憑藉上述諸多優勢，Podman正在快速成長並縮小差距。由於在Dockerfile語法、Docker映像檔、CLI（命令行界面）等多方面與Docker兼容，對個人或小型組織來說應該不會造成太大問題。

### Podman
大多數主要Linux發行版的系統基本儲存庫都支援Podman，因此安裝非常簡單。

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

### Docker CE
#### Ubuntu
##### 3-Ubuntu-1. 移除舊版本或非官方套件以防止套件衝突
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. 配置儲存庫
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

##### 3-Ubuntu-3. 安裝套件
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. 創建`Docker`群組並註冊用戶
要讓非root用戶無需`sudo`即可管理Docker，可以創建`Docker`群組並註冊需要使用Docker的用戶。在終端機中執行以下命令：
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
之後登出再重新登入，變更的設定就會生效。對於Ubuntu或Debian，系統啟動時Docker服務會自動運行，無需額外操作。

#### Fedora
##### 3-Fedora-1. 移除舊版本或非官方套件以防止套件衝突
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

##### 3-Fedora-2. 配置儲存庫
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. 安裝套件
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
安裝過程中會詢問是否批准GPG金鑰。如果GPG金鑰與`060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`一致，輸入y批准即可。  
> 如果GPG金鑰不一致，可能是下載了被供應鏈攻擊偽造的套件，應該中止安裝。
{: .prompt-danger }

##### 3-Fedora-4. 啟動Docker守護進程
現在Docker已安裝但尚未運行，執行以下命令啟動Docker：
```bash
sudo systemctl start docker
```
要使Docker服務在系統啟動時自動運行，執行以下命令：
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. 將用戶註冊到`Docker`群組
要讓非root用戶能夠管理Docker，需要將用戶註冊到`Docker`群組。在Fedora中，前面的套件安裝過程已自動創建`Docker`群組，只需註冊用戶即可：
```bash
sudo usermod -aG docker $USER
```
之後登出再重新登入，變更的設定就會生效。

#### 確認設定是否正確
在終端機中執行以下命令：
```bash
docker run hello-world
```
如果輸出類似以下訊息，則表示成功：

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
