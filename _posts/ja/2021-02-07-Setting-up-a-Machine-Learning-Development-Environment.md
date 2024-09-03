---
title: "機械学習開発環境の構築"
description: >-
  この記事では、ローカルマシンで機械学習を学ぶための最初のステップとなる開発環境の構築方法について説明します。すべての内容は、Ubuntu 20.04 LTS上でNVIDIA Geforce RTX 3070グラフィックカードを基準に作成されています。
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
toc: true
toc_sticky: true
---

## 概要
この記事では、ローカルマシンで機械学習を学ぶための最初のステップとなる開発環境の構築方法について説明します。すべての内容は、Ubuntu 20.04 LTS上でNVIDIA Geforce RTX 3070グラフィックカードを基準に作成されています。

- 構築する技術スタック
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
  - ディープラーニングフレームワーク（各環境につき1つのみ選択してインストールすることを推奨）
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

## 0. 事前確認事項
- 機械学習の学習にはLinuxの使用を推奨します。Windowsでも可能ですが、様々な細かい部分で時間の無駄が多く発生する可能性があります。Ubuntuの最新LTSバージョンを使用するのが最も無難です。オープンソースではない独占的なドライバーも自動的にインストールされるため便利で、ユーザー数が多いため、ほとんどの技術文書がUbuntuを基準に作成されています。
- 一般的に、UbuntuをはじめとするほとんどのLinuxディストリビューションにはPythonがデフォルトでインストールされています。しかし、もしPythonがインストールされていない場合は、この記事に従う前にPythonをまずインストールする必要があります。
  - 現在インストールされているPythonのバージョンは次のコマンドで確認できます。
  ```
  $ python3 --version
  ```
  - TensorFlow2またはPyTorchを使用する予定であれば、互換性のあるPythonバージョンを確認する必要があります。この記事の執筆時点で、[PyTorch最新バージョンがサポートするPythonバージョン](https://pytorch.org/get-started/locally/#linux-python)は3.6-3.8、[TensorFlow2最新バージョンがサポートするPythonバージョン](https://www.tensorflow.org/install)は3.5-3.8です。  
  この記事ではPython 3.8バージョンを使用します。
- ローカルマシンで機械学習を学ぶ計画であれば、GPUを1つ以上準備することをお勧めします。データの前処理程度はCPUでも可能ですが、モデルの学習段階では、モデルの規模が大きくなるほどCPUとGPUの学習速度の差は圧倒的です（特にディープラーニングの場合がそうです）。
  - 機械学習のためであれば、GPU製造元の選択肢は実質的に1つしかありません。NVIDIA製品を利用する必要があります。NVIDIAは機械学習分野に相当多くの投資をしてきた会社であり、ほぼすべての機械学習フレームワークでNVIDIAのCUDAライブラリを利用しています。
  - 機械学習用にGPUを使用する予定であれば、使用しようとするグラフィックカードがCUDA使用可能なモデルかどうかを先に確認する必要があります。現在のコンピュータに搭載されているGPUモデル名は、ターミナルで`uname -m && cat /etc/*release`コマンドで確認できます。[リンク](https://developer.nvidia.com/cuda-gpus)にあるGPUリストで該当するモデル名を見つけた後、**Compute Capability**の数値を確認してください。この数値が少なくとも3.5以上でなければCUDAを使用できません。
  - GPUの選定基準は次の記事によくまとめられています。著者が継続的に更新している記事です。  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  同じ方が書いた[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)という記事も非常に有益です。参考までに、上記の記事の結論は以下の通りです。
    > RTX 3070とRTX 3080は強力なカードですが、メモリが少し不足しています。しかし、多くのタスクでは、そのような量のメモリは必要ありません。  
    > RTX 3070は、ディープラーニングを学びたい場合に最適です。これは、ほとんどのアーキテクチャのトレーニングの基本的なスキルを、単に少しスケールダウンしたり、少し小さな入力画像を使用したりすることで学ぶことができるからです。もし私がディープラーニングを再び学ぶとしたら、おそらく1枚のRTX 3070、あるいは余裕があれば複数枚を選ぶでしょう。
    > RTX 3080は現在、最もコスト効率の高いカードであり、プロトタイピングに理想的です。プロトタイピングには、まだ安価な最大のメモリが欲しいところです。ここでプロトタイピングとは、あらゆる分野でのプロトタイピングを意味します：研究、競争的なKaggle、スタートアップのためのアイデア/モデルのハッキング、研究コードの実験などです。これらすべてのアプリケーションに対して、RTX 3080が最高のGPUです。

上記で言及したすべての事項を満たしていれば、作業環境の構築を開始しましょう。

## 1. 作業ディレクトリの作成
ターミナルを開き、.bashrcファイルを修正して環境変数を登録します（$プロンプトの後がコマンドです）。  
まず、次のコマンドを使用してnanoエディタを開きます（vimやその他のエディタでも構いません）。
```
$ nano ~/.bashrc
```
最後の行に次の内容を追加します。二重引用符内の内容は、希望すれば別のパスに変更しても構いません。  
```export ML_PATH="$HOME/ml"```

Ctrl+Oを押して保存し、Ctrl+Xで終了します。

次に、以下のコマンドを実行して環境変数を適用します。
```
$ source ~/.bashrc
```
ディレクトリを作成します。
```
$ mkdir -p $ML_PATH
```

## 2. pipパッケージマネージャのインストール
機械学習に必要なPythonパッケージをインストールする方法はいくつかあります。Anacondaのような科学的Python配布版を使用してもよいですし（Windows OSの場合は推奨される方法）、Pythonの自体のパッケージングツールであるpipを使用することもできます。ここでは、LinuxやmacOSのbashシェルでpipコマンドを使用します。

システムにpipがインストールされているかどうかを次のコマンドで確認します。
```
$ pip3 --version

コマンド 'pip3' が見つかりません。ただし、以下の方法でインストールできます：

sudo apt install python3-pip

```
上記のように表示される場合、システムにpipがインストールされていません。システムのパッケージマネージャ（ここではapt）を使用してインストールします（もしバージョン名が表示される場合は、すでにインストールされているので、このコマンドはスキップします）。
```
$ sudo apt install python3-pip
```
これでシステムにpipがインストールされました。

## 3. 独立した仮想環境の作成（推奨）
仮想環境（他のプロジェクトのライブラリバージョンとの衝突を避けるため）を作成するには、venvをインストールします。
```
$ sudo apt install python3-venv
```
その後、独立したPython環境を次のように作成します。これを行う理由は、プロジェクトごとに必要なライブラリのバージョンが異なり、衝突を防ぐためです。新しいプロジェクトを開始するたびに新しい仮想環境を作成して独立した環境を構築すればよいです。
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(環境名)
```
この仮想環境を有効にするには、ターミナルを開いて次のコマンドを入力します。
```
$ cd $ML_PATH
$ source ./(環境名)/bin/activate
```
仮想環境を有効にした後、仮想環境内のpipをアップグレードします。
```
(env) $ pip install -U pip
```
後で仮想環境を無効にするには、```deactivate```コマンドを使用します。環境を有効にした状態では、pipコマンドでインストールするパッケージはすべてこの独立した環境にインストールされ、Pythonはこのパッケージを使用します。

## 3′. （仮想環境を作成しない場合）pipバージョンのアップグレード
システムにpipをインストールする際、ディストリビューション（ここではUbuntu）のミラーサーバーにあるバイナリファイルをダウンロードしてインストールしますが、このバイナリファイルは一般的に更新が遅れており、最新バージョンでない場合が多いです（筆者の場合、20.3.4バージョンがインストールされました）。最新バージョンのpipを使用するために、次のコマンドを実行して*ユーザーのホームディレクトリ*にpipをインストール（または既にインストールされている場合はアップグレード）します。  
```
$ python3 -m pip install -U pip

Collecting pip
（中略）
Successfully installed pip-21.0.1
```
pipがこの記事を作成した時点での最新バージョンである21.0.1にインストールされたことが確認できます。この時、ユーザーのホームディレクトリにインストールしたpipはシステムが自動的に認識できないため、システムが認識して使用できるようにPATH環境変数として登録する必要があります。

再び.bashrcファイルをエディタで開きます。
```
$ nano ~/.bashrc
```
今度は```export PATH=```で始まる行を探します。もしその後に記述されたパスがない場合は、[1段階](#1-作業ディレクトリの作成)で行ったように内容を追加するだけです。既に登録された他のパスがある場合は、コロンを使用してその後ろに内容を追加します。  
```export PATH="$HOME/.local/bin"```  
```export PATH="（既存のパス）:$HOME/.local/bin"```

[システムのpipをシステムパッケージマネージャ以外の方法でアップグレードすると、バージョンの衝突により問題が発生する可能性があります](https://github.com/pypa/pip/issues/5599)。そのため、ユーザーのホームディレクトリに別途pipをインストールするのです。同じ理由で、仮想環境内でない限り、```pip```コマンドの代わりに```python3 -m pip```コマンドを使用してpipを使用することをお勧めします。

## 4. 機械学習用パッケージ（jupyter、matplotlib、numpy、pandas、scipy、scikit-learn）のインストール
次のpipコマンドで必要なパッケージと依存関係で連結された他のパッケージをすべてインストールします。  
筆者の場合、venvを使用しているため単に```pip```コマンドを使用しましたが、venvを使用しない場合は前述のように```python3 -m pip```コマンドを代わりに使用することをお勧めします。
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
（後略）
```
venvを使用した場合は、Jupyterにカーネルを登録し、名前を付けます。
```
(env) $ python3 -m ipykernel install --user --name=（カーネル名）
```
これからJupyterを実行するには、次のコマンドを使用します。
```
(env) $ jupyter notebook
```

## 5. CUDA & cuDNNのインストール
### 5-1. 必要なCUDA & cuDNNバージョンの確認
[PyTorch公式ドキュメント](https://pytorch.org/get-started/locally/)でサポートされているCUDAバージョンを確認します。  
![PyTorch互換CUDAバージョンの確認](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
PyTorch 1.7.1バージョンを基準に、サポートされているCUDAバージョンは9.2、10.1、10.2、11.0です。NVIDIA 30シリーズGPUの場合、CUDA 11が必要なため、11.0バージョンが必要であることがわかります。

[TensorFlow2公式ドキュメント](https://www.tensorflow.org/install/gpu)でも必要なCUDAバージョンを確認します。  
![TensorFlow2互換CUDAバージョンの確認](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
TensorFlow 2.4.0バージョンを基準に、CUDAも同様に11.0バージョン、cuDNNは8.0バージョンが必要であることを確認しました。

筆者の場合、場合によってはPyTorchを使用する時も、TensorFlow2を使用する時もあるため、両方のパッケージと互換性のあるCUDAバージョンを確認しました。自分が必要なパッケージの要件を確認し、それに合わせればよいです。

### 5-2. CUDAのインストール
[CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive)にアクセスし、前で確認したバージョンを選択して進みます。この記事では[CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive)を選択して進みます。  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
次に、該当するプラットフォームとインストーラーの種類を選択し、画面に表示される指示に従います。この時、[インストーラーの場合、可能な限りシステムパッケージマネージャーを利用することをお勧めします](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method)。筆者が好む方法はdeb (network)です。  
![CUDAプラットフォームの選択](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)  
![CUDAのインストール](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)  

以下のコマンドを実行してCUDAをインストールします。
```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```
目が良ければ、最後の行が画像に表示された指示と少し異なることに気づいたかもしれません。ネットワークインストールで画像に表示されたようにcudaだけを入力すると、最新バージョンである11.2バージョンがインストールされますが、これは私たちが望むものではありません。[CUDA 11.0 Linux インストールガイド](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas)で様々なメタパッケージオプションを確認できます。ここでは、CUDA Toolkitパッケージを11.0バージョンで指定インストールし、ドライバーパッケージは自動アップグレードされるようにするために最後の行を修正しました。

### 5-3. cuDNNのインストール
次のようにcuDNNをインストールします。
```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```
## 6. PyTorchのインストール
先ほど3段階で仮想環境を作成した場合は、使用する仮想環境を有効にした状態で進めます。PyTorchが必要ない場合は、この段階はスキップします。  
[PyTorchホームページ](https://pytorch.org/get-started/locally/)にアクセスし、インストールするPyTorchビルド（Stable）、オペレーティングシステム（Linux）、パッケージ（Pip）、言語（Python）、CUDA（11.0）を選択し、画面に表示される指示に従います。  
![PyTorchのインストール](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)
```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
PyTorchを正しくインストールしたかを検証するために、Pythonインタープリタを実行した後、次のコマンドを実行してみます。テンソルが返されれば成功です。
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
GPUドライバーとCUDAが有効化されており、使用可能かどうかを確認するために次のコマンドを実行してみます。
```
>>> torch.cuda.is_available()
True
```

## 7. TensorFlow 2のインストール
TensorFlowが必要ない場合は、この段階は無視してください。  
6段階でPyTorchを仮想環境にインストールした場合は、その仮想環境を無効にした後、3、4段階に戻って新しい仮想環境を作成し、有効にしてから進めます。6段階をスキップした場合は、そのまま進めてください。  
次のようにTensorFlowをインストールします。
```
(env2) $ pip install --upgrade tensorflow
```
TensorFlowを正しくインストールしたかを検証するために、次のコマンドを実行してみます。GPU名を表示し、テンソルを返せば成功です。
```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
（中略）
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```