---
title: "使用 NVIDIA Container Toolkit 與 Docker/Podman 建立深度學習開發環境（1）- 安裝 NVIDIA Container Toolkit 與容器引擎"
description: "本系列說明如何在本機以 NVIDIA Container Toolkit 建置容器化深度學習開發環境，並設定 SSH 與 JupyterLab 以便作為遠端伺服器使用。本文為第一篇，介紹 NVIDIA Container Toolkit 與 Docker/Podman 容器引擎的安裝流程。"
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## 概述

本系列將介紹安裝 NVIDIA Container Toolkit 與 Docker 或 Podman，並以 Docker Hub 的 [nvidia/cuda 儲存庫](https://hub.docker.com/r/nvidia/cuda)所提供的 CUDA 與 cuDNN 映像檔為基礎撰寫 Dockerfile，建置深度學習開發環境的流程。為了讓有需要的人能自由取用，我會透過 GitHub 與 Docker Hub 分享經上述流程完成的 [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) 與 [映像檔](https://hub.docker.com/r/yunseokim/dl-env/tags)，並額外提供作為遠端伺服器使用所需的 SSH 與 JupyterLab 設定指南。  
本系列預計由 3 篇文章組成，而你正在閱讀的是系列的第 1 篇。
- 第 1 篇：NVIDIA Container Toolkit & 容器引擎安裝（本文）
- [第 2 篇：為 GPU 使用配置容器執行階段、撰寫 Dockerfile 與建置容器映像檔](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 第 3 篇（預計上傳）

本文以 x86_64 Linux 環境、且系統安裝支援 CUDA 的 NVIDIA 顯示卡為前提進行；除 Ubuntu 與 Fedora 之外的發行版我未親自測試，因此部分細節可能略有差異。  
（12026.1.6. 修訂）

### 開發環境組成

- 主機作業系統與架構：x86_64，Linux 環境（Ubuntu 22.04/24.04 LTS、RHEL/Centos、Fedora、openSUSE/SLES 15.x 等）
- 要建置的技術堆疊（語言與函式庫）
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/)（選用，與 NumPy/SciPy 相容的 GPU 加速陣列函式庫）
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/)（選用，用 GPU 加速器在幾乎零程式碼修改下加速 pandas）
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/)（選用，以少量程式碼搭配最佳化圖表函式庫，快速視覺化並篩選大型資料集）
  - [DALI](https://developer.nvidia.com/DALI)（選用，以 GPU 實作的高效能資料載入器/迭代器替代方案）
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/)（選用，基於 GPU 加速的 n 維影像處理與 I/O，作為 scikit-image 的替代方案）
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/)（選用，以與 scikit-learn API 高度相似的 API 在 GPU 上執行機器學習演算法）
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/)（選用，針對近似最近鄰與分群等進行最佳化的向量搜尋加速工具組）
  - [RAFT](https://docs.rapids.ai/api/raft/stable/)（選用，CUDA 加速基礎元件，供其他 RAPIDS 函式庫使用）
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/)（選用，GPU 加速圖分析函式庫，並提供對 NetworkX 的零程式碼修改加速器）
  - [tqdm](https://tqdm.github.io/)

  > 可依情況與個人偏好，考慮用 [Polars](https://pola.rs/) DataFrame 函式庫取代 pandas。它以 Rust 撰寫；雖然在超大規模資料處理時可能不如 cuDF + pandas 組合，但相較於原生 pandas 套件仍有相當亮眼的效能表現（[參考基準測試](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/)），且提供更偏向 Query 的語法。依官方 [Polars 部落格](https://pola.rs/posts/polars-on-gpu/)與 [cuDF 文件](https://docs.rapids.ai/api/cudf/stable/cudf_polars/)所述，Polars 與 NVIDIA RAPIDS 團隊正合作提供基於 cuDF 的 GPU 加速引擎（開放 Beta），並持續快速開發中。
  {: .prompt-tip }

  > 若你在猶豫要用 Docker CE 還是 Podman，[後文的比較表](#3-容器引擎安裝)可能會有幫助。
  {: .prompt-tip }

### 與先前撰寫的機器學習開發環境指南比較表

本部落格先前已有一篇[機器學習開發環境建置指南](/posts/Setting-up-a-Machine-Learning-Development-Environment)，但由於變更點不少，因此重新撰寫本文。差異如下表所示。

| 差異項目 | 舊文（12021 版本） | 本文（12024 撰寫，12026 修訂版） |
| --- | --- | --- |
| Linux 發行版 | 以 Ubuntu 為基準 | 除 Ubuntu 外，也可套用於 Fedora/RHEL/Centos、<br>Debian、openSUSE/SLES 等 |
| 建置方式 | 直接安裝於主機系統<br>以 venv 建立 Python 虛擬環境 | 使用 [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br>的 Docker 容器化環境<br>使用 uv 管理 Python 虛擬環境與套件 |
| NVIDIA 顯示驅動安裝 | O | O |
| 主機系統直接安裝<br>CUDA 與 cuDNN | O（使用 Apt 套件管理器） | X（使用 [Docker Hub 上 NVIDIA 提供的預先安裝映像檔](https://hub.docker.com/r/nvidia/cuda)，無需手動處理） |
| 可攜性 | 每次移轉到其他系統時<br>都需重新建置開發環境 | 基於 Docker，可用既有 Dockerfile <br>需要時隨時建置新映像檔，或輕鬆移植<br>既有映像檔（不含額外 volume/網路設定） |
| 使用 cuDNN 以外的<br>GPU 加速函式庫 | X | 導入 [CuPy](https://cupy.dev/)、[RAPIDS](https://rapids.ai/)、[DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook 介面 | Jupyter Notebook（classic） | JupyterLab（Next-Generation） |
| SSH 伺服器設定 | 未另外說明 | 包含基礎 SSH 伺服器設定 |

## 0. 事前確認事項

- [NVIDIA Container Toolkit 可用於支援 Apt、Yum 或 Dnf、Zypper 套件管理器的 Linux 發行版。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html)可在連結頁面確認支援的 Linux 發行版清單。雖然官方支援表未特別列出 Fedora，但 Fedora 同樣是 Red Hat Linux 系（與 RHEL 類似），因此一般可無痛使用。若你不熟悉 Linux、也不確定該選哪個發行版，使用 Ubuntu LTS 版通常最穩妥：包含非開源的專有驅動也較容易自動安裝，對初學者相對友善；使用者眾多，也使得大部分技術文件以 Ubuntu 為基準撰寫。
  - 你正在使用的系統架構與 Linux 發行版版本，可在終端機執行 `uname -m && cat /etc/*release` 確認。
- 需先確認系統顯示卡是否支援你打算使用的 CUDA 與 cuDNN 版本。
  - 目前電腦安裝的 GPU 型號可在終端機執行 `lspci | grep -i nvidia` 確認。
  - 在 <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> 中，依 cuDNN 版本查看其 **支援的 NVIDIA 顯示驅動版本**、所需的 **CUDA Compute Capability** 條件，以及 **支援的 NVIDIA 硬體**清單。
  - 到 <https://developer.nvidia.com/cuda-gpus> 的 GPU 清單找到你的型號後，確認其 **Compute Capability** 數值；該數值需滿足前述 **CUDA Compute Capability** 條件，才能正常使用 CUDA 與 cuDNN。

> 若你打算新購深度學習用顯示卡，以下文章對 GPU 選型整理得很好，且作者會不定期更新。  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> 若你也需要整體硬體配置指南，同一位作者撰寫的 [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)也非常有價值。
{: .prompt-tip }

若上述條件皆已滿足，就開始建置工作環境吧。

## 1. 安裝 NVIDIA 顯示驅動程式

首先必須在主機系統安裝 NVIDIA 顯示驅動。你可以從 [NVIDIA 驅動下載頁](https://www.nvidia.com/drivers/)下載 .run 安裝器來安裝，但就版本管理與維護而言，建議盡量使用系統的套件管理器安裝。請參考 <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> 官方文件，依你的系統環境安裝合適的顯示驅動。

### 專有模組 vs 開源模組（Proprietary module vs Open-source module）

NVIDIA Linux 驅動由多個核心模組組成；自 515 版驅動與之後的版本起，NVIDIA 提供兩種型態的驅動核心模組。

- Proprietary：NVIDIA 以往提供的專有（閉源）驅動。
- Open-source：以 MIT/GPLv2 雙授權提供的開源驅動，並透過 <https://github.com/NVIDIA/open-gpu-kernel-modules> 公開原始碼。

Proprietary 驅動提供給 Maxwell 架構到 Blackwell 之前架構的 GPU，並預計自 Blackwell 架構起停止支援。  
相對地，Open-source 驅動支援 Turing 及之後的架構。

[NVIDIA 建議在可行的情況下使用開源核心模組。](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
你可透過[此連結](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus)確認正在使用的 GPU 是否與開源驅動相容。

本文將以安裝開源驅動為前提進行說明。

### Debian & Ubuntu

Ubuntu 或 Debian 可在終端機輸入以下指令安裝：
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

以 Fedora 40 為基準，本文介紹透過 [RPM Fusion](https://rpmfusion.org/RPM%20Fusion)下載並安裝預先建置好的套件。

#### 1-Fedora-1. 設定 RPM Fusion 儲存庫

請參考 [RPM Fusion 官方指南](https://rpmfusion.org/Configuration)。  
在終端機執行以下指令：

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> 在較舊的 DNF（Fedora 40 與更早版本）中，第二行用來啟用 openh264 函式庫儲存庫的指令如下：
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> 但自 DNF 5（Fedora 41+）起，需改用
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> 因此本文已同步更新內容。
{: .prompt-info }

#### 1-Fedora-2. 安裝 akmod-nvidia 套件

請參考 [RPM Fusion 的 NVIDIA 驅動安裝指南](https://rpmfusion.org/Howto/NVIDIA)安裝 akmod-nvidia 套件。

```bash
sudo dnf update  # 此步若有內核更新，請先以最新內核重開機後再繼續
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> 同樣地，在較舊的 DNF（Fedora 40 與更早版本）中，第三行用於避免 autoremove 時刪除 NVIDIA 驅動的指令如下：
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> 但自 DNF 5（Fedora 41+）起需改用
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> 本文亦已反映此變更。
{: .prompt-info }

> 另外，過去 RPM Fusion 對 [NVIDIA 開源核心模組](#專有模組-vs-開源模組proprietary-module-vs-open-source-module)採取較消極立場，且在未特別指定時會預設提供 Proprietary 驅動。不過依據 [RPM Fusion 近期（12025 年 12 月）更新的指引](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open)，對於「重疊支援」硬體（Turing 到 Blackwell 之前架構）現在會自動選擇並提供更合適的版本，因此使用者不需要再手動挑選。對於 Turing 之前的舊架構、或 Blackwell 及更新架構，原本就只有單一選擇，故沒有變更。
> 因此已確認並移除先前透過 `/etc/rpm/macros.nvidia-kmod` 指定使用開源核心模組的內容。
>
> 此外，對於 `akmod-nvidia-open` 套件，除非你需要自行套用下游（downstream）變更到 kernel space 驅動，否則建議不要使用。
>
> 以上也已納入本文更新。
{: .prompt-info }

#### 1-Fedora-3. 在啟用安全開機（Secure Boot）時，為讓驅動正常載入而註冊金鑰  

> 只要依照下述流程增加一些額外步驟，就能在維持安全開機的前提下正常使用 NVIDIA 顯示驅動；若停用安全開機，系統安全性會顯著降低，因此不建議關閉。至少在進入 12020 年代之後，一般很少有必要停用安全開機。
{: .prompt-danger }

先安裝以下工具：

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

接著執行下列指令產生金鑰：

```bash
sudo kmodgenca -a
```

接下來需要把剛產生的金鑰註冊到 UEFI 韌體的 MOK：

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

執行後會要求輸入註冊金鑰用的密碼。稍後會重開機完成註冊流程；這個密碼是一次性使用，請輸入你能短時間記住的內容。

然後執行以下指令重開機：

```bash
systemctl reboot
```

系統開機時會自動跳出 MOK 管理畫面。選擇「Enroll MOK」，接著依序選「Continue」「Yes」後會要求輸入剛才設定的密碼。輸入完成後即完成金鑰註冊。最後輸入 reboot 再次重開機後，NVIDIA 驅動就會正常載入。

### 確認 NVIDIA 驅動是否安裝成功

在終端機執行以下指令可確認目前載入的 NVIDIA 核心模組：

```bash
cat /proc/driver/nvidia/version
```

若輸出類似以下內容，表示安裝成功：

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

此外，Linux 陣營在許多情況下預設採用的開源顯示驅動（nouveau 核心模組）在安裝 NVIDIA 驅動後應被停用；若未停用可能造成問題。安裝 NVIDIA 驅動並重開機後，執行以下指令不應輸出任何內容才算正常：

```bash
lsmod |grep nouveau
```

## 2. 安裝 NVIDIA Container Toolkit

接著安裝 [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)。請參考 [NVIDIA Container Toolkit 官方安裝指南](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)進行安裝；另外 Fedora 在安裝流程上有注意事項，請先把本節內容看完再動手。

### 使用 Apt（Ubuntu、Debian 等）

#### 2-Apt-1. 設定下載套件用的儲存庫

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. 更新套件清單

```bash
sudo apt update
```

#### 2-Apt-3. 安裝套件

```bash
sudo apt install nvidia-container-toolkit
```

### 使用 Yum 或 Dnf（Fedora、RHEL、Centos 等）

> 以 Fedora 40 實測時，和 Ubuntu 不同，`nvidia-smi` 指令與 `nvidia-persistenced` 套件並未預設包含於 NVIDIA 顯示驅動中，因此需要另外安裝 `xorg-x11-drv-nvidia-cuda` 套件。我未在 RHEL 與 Centos 親自測試，但其系統組成與 Fedora 相當接近；若依下列指南操作仍有問題，可嘗試同樣做法，或許會有幫助。
{: .prompt-warning }

> 在 Fedora 40 依上述方式安裝 `xorg-x11-drv-nvidia-cuda` 後，執行樣本工作負載測試，在我的系統上可正常運作。若仍因 SELinux 等因素造成問題，Fedora AI-ML 團隊提供的 [Fedora 專用 nvidia-container-toolkit 套件與指南](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/)也可能有幫助。
{: .prompt-tip }

#### 2-Dnf-1. 設定下載套件用的儲存庫

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

### 使用 Zypper（openSUSE、SLES）

#### 2-Zypper-1. 設定下載套件用的儲存庫

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. 安裝套件

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. 容器引擎安裝

接著安裝容器引擎：Docker CE 或 Podman。可依使用情境與偏好二選一安裝，並參考 [Docker 官方文件](https://docs.docker.com/engine/install/)與 [Podman 官方文件](https://podman.io/docs/installation)。

下表整理 Docker 與 Podman 的主要差異與優缺點。

| 比較項目 | Docker | Podman |
| --- | --- | --- |
| 架構 | Client-Server 模型，基於守護行程（daemon） | 無守護行程（daemonless）架構 |
| 安全性 | 預設依賴以 root 權限執行的 daemon，<br>存在潛在安全風險<br>（自 12020 年發表的 20.10 版起支援無根<br>模式（rootless），但需額外設定） | 不依賴 daemon，未特別指定時<br>預設以無根（rootless）方式運作，<br>並受 SELinux 保護 |
| 資源使用量 | 因 daemon 架構特性需常駐背景程序，<br>一般資源消耗較多 | 一般資源間接成本（overhead）較低 |
| 容器啟動時間 | 相對較慢 | 由於架構精簡，最多可快約 50%<br> |
| 生態系與文件 | 生態系與社群支援廣，<br>相關文件豐富 | 生態系相對較小，文件也相對較少 |
| 網路 | 使用 Docker Bridge Network | 使用 CNI（Container Network Interface）<br>外掛 |
| Kubernetes YAML<br>原生支援 | X（需轉換） | O |

參考資料：
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker 歷史較久，也長期在業界享有事實上的標準地位，因此最大的優勢在於生態系龐大且相關文件豐富。  
Podman 則由 Red Hat 於較近年開發，天生採無守護行程（daemonless）、無根（rootless）導向的進階架構，因此在安全性、系統資源使用量、容器啟動時間等面向具備多項優勢。此外，Docker 若 daemon 出問題導致停止，所有容器可能一併停止；而 Podman 的容器彼此完全獨立，單一容器故障不會影響其他容器，這也是 Podman 的強項之一。

最重要的是依自身條件選擇合適工具；但若你是初學者，以 Podman 作為起點可能是個不錯的選擇。儘管相較 Docker 生態系仍較小，但憑藉上述優勢正快速成長、差距也在縮小；並且在 Dockerfile 語法、Docker 映像檔、CLI（命令列介面）等許多方面與既有 Docker 相容。若你並非已在既有系統中大量採用 Docker，導致轉向 Podman 會有高昂切換成本，那麼一開始就採用 Podman 通常更合理。

### Podman

多數主流 Linux 發行版的系統預設儲存庫皆提供 Podman，可直接安裝。

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

#### 確認是否設定成功

在終端機執行：

```bash
podman run --rm hello-world
```

若輸出如下訊息即成功：

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

> 以 12025-12-18T00:43:00+09:00 時點，podman 版本 5.7.1、[passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`、Fedora 43 環境實測時，執行上述 hello-world、或在執行容器/建置映像檔時，會出現下列錯誤：
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> 即使我目前不使用 IPv6、且處於 IPv4 網路環境，容器網路設定階段的 pasta（包含於 passt 函式庫）仍會嘗試設定 IPv6 routing，因而導致此問題。經確認，在執行容器或[後文的映像檔建置步驟](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-建立docker映像檔並運行容器)中，若如下明確指定 `--net=pasta:-4` 強制使用 IPv4，則不會出現問題：
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> 查詢後發現有[先前已回報的相同症狀 issue](https://github.com/containers/podman/issues/22824)。該 issue 稱已在 [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/) 修正；但考量到觀察到的症狀一致、且同樣是在使用 Proton VPN 時發生等多項相似點，我推測可能是類似問題再次出現。
{: .prompt-warning }

### Docker CE

#### Ubuntu

##### 3-Ubuntu-1. 移除舊版或非官方套件以避免衝突

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. 設定儲存庫

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

##### 3-Ubuntu-4. 建立 `Docker` 群組並加入使用者

若要讓非 root 使用者不必 `sudo` 也能管理 Docker，可建立 `Docker` 群組並把需要使用 Docker 的帳號加入該群組。在終端機執行：

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

之後登出再登入即可套用變更。Ubuntu 或 Debian 一般不需額外操作，系統開機時 Docker 服務會自動啟動。

#### Fedora

##### 3-Fedora-1. 移除舊版或非官方套件以避免衝突

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

##### 3-Fedora-2. 設定儲存庫

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. 安裝套件

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

安裝過程會提示是否信任/匯入 GPG key。若 GPG key 與 `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35` 一致，輸入 y 允許即可。  
> 若 GPG key 不一致，可能遭遇供應鏈攻擊而下載到偽造套件，應立即停止安裝。
{: .prompt-danger }

##### 3-Fedora-4. 啟動 Docker daemon

此時 Docker 已安裝但尚未執行，可用以下指令啟動：

```bash
sudo systemctl start docker
```

若要讓系統開機時自動啟動 Docker 服務，執行：

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. 將使用者加入 `Docker` 群組

若要讓非 root 使用者能管理 Docker，需將該使用者加入 `Docker` 群組。Fedora 在前述安裝流程中會自動建立 `Docker` 群組，因此只需加入使用者即可：

```bash
sudo usermod -aG docker $USER
```

之後登出再登入即可套用變更。

#### 確認是否設定成功

在終端機執行：

```bash
docker run hello-world
```

若輸出如下訊息即成功：

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
續篇請見：[第 2 篇](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
