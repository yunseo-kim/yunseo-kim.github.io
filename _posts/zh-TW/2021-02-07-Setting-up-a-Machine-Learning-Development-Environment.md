---
title: 建立機器學習開發環境
description: 本文介紹如何在本地機器上建立機器學習學習的第一步 - 開發環境。所有內容都是基於Ubuntu 20.04 LTS和NVIDIA GeForce RTX 3070顯卡編寫的。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, CUDA, PyTorch, TensorFlow]
image: /assets/img/technology.jpg
---

## 概述

本文介紹如何在本地機器上建立機器學習學習的第一步 - 開發環境。所有內容都是基於Ubuntu 20.04 LTS和NVIDIA GeForce RTX 3070顯卡編寫的。

- 要建立的技術堆疊
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
  - 深度學習框架(建議每個環境只選擇安裝一個)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

### 與新撰寫的機器學習開發環境建置指南的比較表

雖然距離在部落格上傳已經過了約3年半,但這篇文章的內容除了套件版本或NVIDIA開源驅動程式發布等一些細節外,在大框架上仍然有效。然而,在2024年夏天購買新電腦並建置開發環境時,有一些變更,因此我撰寫了[新的開發環境建置指南](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/)。變更的部分如下表所示:

| 差異點 | 本文 (2021版本) | 新文章 (2024版本) |
| --- | --- | --- |
| Linux發行版 | 以Ubuntu為基準 | 除了Ubuntu外,也適用於Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES等 |
| 開發環境建置方式 | 使用venv的Python虛擬環境 | 使用[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)的<br> Docker容器基礎環境 |
| NVIDIA顯卡驅動安裝 | O | O |
| 在主機系統上直接安裝<br>CUDA和cuDNN | O (使用Apt套件管理器) | X (使用[Docker Hub上NVIDIA提供的預安裝映像檔](https://hub.docker.com/r/nvidia/cuda),<br>因此無需直接操作)
| 可移植性 | 每次轉移到其他系統時<br>都需要重新建置開發環境 | 基於Docker,因此可以使用製作好的Dockerfile<br>在需要時建立新映像檔,或輕鬆移植<br>現有使用的映像檔(除了額外的卷或網路設定) |
| 除cuDNN外的其他<br>GPU加速庫使用 | X | 引入[CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook介面 | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH伺服器設定 | 未特別提及 | 在第3部分包含基本的SSH伺服器設定配置 |

如果想使用venv等Python虛擬環境而非Docker,這篇原本撰寫的文章仍然有效,可以繼續閱讀。如果想享受Docker容器導入的高可移植性等優點,或計劃使用Ubuntu以外的其他Linux發行版如Fedora等,或使用NVIDIA顯卡環境並想利用CuPy、cuDF、cuML、DALI等額外的GPU加速庫,或想通過SSH和JupyterLab設定進行遠端訪問,也建議參考[新指南](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/)。

## 0. 事前確認事項

- 建議使用Linux來學習機器學習。雖然在Windows上也可以,但在許多細節方面可能會浪費很多時間。使用Ubuntu最新的LTS版本是最穩妥的選擇。非開源的專有驅動程式也會自動安裝,很方便,而且由於使用者數量多,大多數技術文件都是以Ubuntu為基準編寫的。
- 一般來說,Ubuntu和大多數Linux發行版都預裝了Python。但如果沒有安裝Python,在按照本文操作之前,需要先安裝Python。
  - 可以用以下命令確認當前安裝的Python版本:
  ```
  $ python3 --version
  ```
  - 如果要使用TensorFlow 2或PyTorch,需要確認兼容的Python版本。以本文撰寫時為基準,[PyTorch最新版本支援的Python版本](https://pytorch.org/get-started/locally/#linux-python)是3.6-3.8,[TensorFlow 2最新版本支援的Python版本](https://www.tensorflow.org/install)是3.5-3.8。  
  本文使用Python 3.8版本。
- 如果計劃在本地機器上學習機器學習,最好準備至少一個GPU。雖然數據預處理等工作用CPU也可以,但在模型訓練階段,隨著模型規模的增大,CPU和GPU的訓練速度差異會變得非常顯著(特別是深度學習的情況)。
  - 對於機器學習來說,GPU製造商的選擇實際上只有一個。必須使用NVIDIA的產品。NVIDIA是在機器學習領域投資非常多的公司,幾乎所有機器學習框架都使用NVIDIA的CUDA庫。
  - 如果計劃將GPU用於機器學習,首先要確認要使用的顯卡型號是否支援CUDA。可以在終端機中使用`uname -m && cat /etc/*release`命令確認當前電腦安裝的GPU型號。在[連結](https://developer.nvidia.com/cuda-gpus)中的GPU列表中找到相應的型號,然後確認**Compute Capability**數值。這個數值至少要3.5以上才能使用CUDA。
  - GPU選擇標準在以下文章中有很好的整理。作者持續更新這篇文章。  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  同一位作者撰寫的[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)這篇文章也非常有用。參考上述文章的結論如下:
    > RTX 3070和RTX 3080是強大的顯卡,但它們的記憶體稍微不足。然而,對於許多任務來說,你並不需要那麼多記憶體。  
    > RTX 3070對於學習深度學習來說是完美的。這是因為大多數架構的基本訓練技能可以通過稍微縮小規模或使用稍小的輸入圖像來學習。如果我再次學習深度學習,我可能會選擇一張RTX 3070,如果有多餘的錢,甚至可能選擇多張。
    > RTX 3080目前是最具成本效益的顯卡,因此非常適合原型設計。對於原型設計,你想要最大的記憶體,但仍然要便宜。這裡的原型設計指的是任何領域的原型設計:研究、競爭性Kaggle、為創業公司構思/建模、實驗研究代碼。對於所有這些應用,RTX 3080是最佳的GPU。

如果滿足了上述所有條件,就可以開始建置工作環境了。

## 1. 創建工作目錄

打開終端機,修改.bashrc文件以註冊環境變數($提示符後面是命令)。  
首先使用以下命令打開nano編輯器(使用vim或其他編輯器也可以)。
```
$ nano ~/.bashrc
```
在最後一行添加以下內容。雙引號內的內容可以根據需要更改為其他路徑。  
```export ML_PATH="$HOME/ml"```

按Ctrl+O保存,然後按Ctrl+X退出。

現在執行以下命令以應用環境變數。
```
$ source ~/.bashrc
```
創建目錄。
```
$ mkdir -p $ML_PATH
```

## 2. 安裝pip套件管理器

安裝機器學習所需的Python套件有多種方法。可以使用像Anaconda這樣的科學Python發行版(對Windows操作系統來說是推薦的方法),也可以使用Python自身的打包工具pip。這裡我們將在Linux或macOS的bash shell中使用pip命令。

使用以下命令檢查系統是否已安裝pip。
```
$ pip3 --version

找不到命令 'pip3'。但可以通過以下方式安裝:

sudo apt install python3-pip

```
如果出現上述情況,則表示系統未安裝pip。使用系統的套件管理器(這裡是apt)安裝(如果顯示版本號,則表示已安裝,可以跳過此命令)。
```
$ sudo apt install python3-pip
```
現在系統已安裝pip。

## 3. 創建獨立的虛擬環境(建議)

要創建虛擬環境(為了避免與其他專案的庫版本衝突),需要安裝venv。
```
$ sudo apt install python3-venv
```
然後按以下方式創建獨立的Python環境。這樣做的原因是為了防止每個專案所需的庫版本不同而發生衝突,因此每次開始新專案時都應該創建新的虛擬環境以建立獨立的環境。
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(環境名稱)
```
要啟動這個虛擬環境,打開終端機並輸入以下命令:
```
$ cd $ML_PATH
$ source ./(環境名稱)/bin/activate
```
啟動虛擬環境後,升級虛擬環境中的pip。
```
(env) $ pip install -U pip
```
之後要停用虛擬環境,使用```deactivate```命令。在環境啟動狀態下,使用pip命令安裝的任何套件都會安裝到這個獨立的環境中,Python會使用這些套件。

## 3′. (不創建虛擬環境的情況) 升級pip版本

在系統上安裝pip時,會下載發行版(這裡是Ubuntu)鏡像伺服器上的二進制文件並安裝,這個二進制文件通常更新較慢,可能不是最新版本(作者的情況是安裝了20.3.4版本)。要使用最新版本的pip,執行以下命令在*使用者的主目錄*安裝pip(或者如果已經安裝,則升級):  
```
$ python3 -m pip install -U pip

Collecting pip
(中略)
Successfully installed pip-21.0.1
```
可以看到pip已安裝到本文撰寫時的最新版本21.0.1。此時,安裝在使用者主目錄的pip系統無法自動識別,因此需要將其註冊為PATH環境變數,使系統能夠識別和使用。

再次用編輯器打開.bashrc文件。
```
$ nano ~/.bashrc
```
這次找到以```export PATH=```開頭的行。如果後面沒有寫任何路徑,就像[第1步](#1-創建工作目錄)那樣直接添加內容。如果已經註冊了其他路徑,使用冒號在後面添加內容。  
```export PATH="$HOME/.local/bin"```  
```export PATH="(現有路徑):$HOME/.local/bin"```

[如果使用系統套件管理器以外的方法升級系統pip,可能會因版本衝突而出現問題](https://github.com/pypa/pip/issues/5599)。這就是為什麼要在使用者的主目錄單獨安裝pip的原因。出於同樣的原因,除非在虛擬環境中,否則建議使用```python3 -m pip```命令而不是```pip```命令來使用pip。

## 4. 安裝機器學習用套件(jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)

使用以下pip命令安裝所需的套件和相關依賴套件。  
作者使用venv,所以直接使用```pip```命令,但如果不使用venv,如前所述,建議使用```python3 -m pip```命令代替。
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(後略)
```
如果使用了venv,為Jupyter註冊核心並命名。
```
(env) $ python3 -m ipykernel install --user --name=(核心名稱)
```
從現在開始,要執行Jupyter,使用以下命令:
```
(env) $ jupyter notebook
```

## 5. 安裝CUDA & cuDNN

### 5-1. 確認所需的CUDA & cuDNN版本

在[PyTorch官方文件](https://pytorch.org/get-started/locally/)中確認支援的CUDA版本。  
![確認PyTorch兼容的CUDA版本](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
以PyTorch 1.7.1版本為基準,支援的CUDA版本是9.2、10.1、10.2、11.0。NVIDIA 30系列GPU需要CUDA 11,所以我們知道需要11.0版本。

在[TensorFlow 2官方文件](https://www.tensorflow.org/install/gpu)中也確認所需的CUDA版本。  
![確認TensorFlow 2兼容的CUDA版本](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
以TensorFlow 2.4.0版本為基準,同樣需要CUDA 11.0版本,cuDNN需要8.0版本。

作者有時使用PyTorch,有時使用TensorFlow 2,所以確認了兩個套件都兼容的CUDA版本。根據自己需要的套件的要求進行確認即可。

### 5-2. 安裝CUDA

訪問[CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive),然後選擇前面確認的版本進入。本文選擇進入[CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive)。  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
現在選擇相應的平台和安裝程式類型,然後按照螢幕上顯示的指示操作。此時,[建議盡可能使用系統套件管理器安裝](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method)。作者偏好的方法是deb (network)。  
![選擇CUDA平台](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)  
![安裝CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)  

執行以下命令安裝CUDA。
```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```
如果你眼尖的話,會發現最後一行與圖片中顯示的指示略有不同。在網絡安裝中,如果按照圖片中的指示只輸入cuda,會安裝最新的11.2版本,這不是我們想要的。在[CUDA 11.0 Linux安裝指南](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas)中可以查看多個元套件選項。這裡我們修改了最後一行,以指定安裝11.0版本的CUDA Toolkit套件,並讓驅動程式套件自動升級。

### 5-3. 安裝cuDNN

按以下方式安裝cuDNN。
```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```

## 6. 安裝PyTorch

如果在第3步創建了虛擬環境,請在啟動要使用的虛擬環境的狀態下進行。如果不需要PyTorch,可以跳過這一步。  
訪問[PyTorch首頁](https://pytorch.org/get-started/locally/),選擇要安裝的PyTorch構建(Stable)、操作系統(Linux)、套件(Pip)、語言(Python)、CUDA(11.0),然後按照螢幕上顯示的指示操作。  
![安裝PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)
```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
要驗證是否正確安裝了PyTorch,執行Python解釋器後運行以下命令。如果返回張量,則表示成功。
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
要確認GPU驅動程式和CUDA是否已啟用並可用,執行以下命令:
```
>>> torch.cuda.is_available()
True
```

## 7. 安裝TensorFlow 2

如果不需要TensorFlow,可以忽略這一步。  
如果在第6步將PyTorch安裝到虛擬環境中,請停用該虛擬環境,然後回到第3、4步創建並啟動新的虛擬環境後再繼續。如果跳過了第6步,就直接繼續進行。  
按以下方式安裝TensorFlow:
```
(env2) $ pip install --upgrade tensorflow
```
要驗證是否正確安裝了TensorFlow,執行以下命令。如果顯示GPU名稱並返回張量,則表示成功。
```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
(中略)
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```
