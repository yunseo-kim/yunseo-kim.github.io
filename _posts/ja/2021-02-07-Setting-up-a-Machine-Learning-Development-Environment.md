---
title: "機械学習開発環境の構築"
description: >-
  この記事では、ローカルマシンで機械学習を学ぶための最初のステップとなる開発環境の構築方法について説明します。すべての内容は、Ubuntu 20.04 LTS上でNVIDIA Geforce RTX 3070グラフィックカードを基準に作成しています。
categories:
  - Data Science
tags:
  - Machine Learning
  - Deep Learning
toc: true
toc_sticky: true
---

## 概要
この記事では、ローカルマシンで機械学習を学ぶための最初のステップとなる開発環境の構築方法について説明します。すべての内容は、Ubuntu 20.04 LTS上でNVIDIA Geforce RTX 3070グラフィックカードを基準に作成しています。

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
  - ディープラーニングフレームワーク（各環境につき1つだけ選択してインストールすることを推奨）
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

## 0. 事前確認事項
- 機械学習の学習にはLinuxの使用を推奨します。Windowsでも可能ですが、様々な細かい部分で時間の無駄が多く発生する可能性があります。Ubuntuの最新LTSバージョンを使用するのが最も無難です。オープンソースではない独占的なドライバーも自動的にインストールされるため便利で、ユーザー数が多いため、ほとんどの技術文書がUbuntuを基準に作成されています。
- 一般的に、UbuntuをはじめとするほとんどのLinuxディストリビューションにはPythonがデフォルトでインストールされています。しかし、もしPythonがインストールされていない場合は、この記事に従う前にPythonをまずインストールする必要があります。
  - 現在インストールされているPythonのバージョンは、次のコマンドで確認できます。
  ```
  $ python3 --version
  ```
  - TensorFlow2またはPyTorchを使用する予定であれば、互換性のあるPythonバージョンを確認する必要があります。この記事の執筆時点で、[PyTorch最新バージョンがサポートするPythonバージョン](https://pytorch.org/get-started/locally/#linux-python)は3.6-3.8、[TensorFlow2最新バージョンがサポートするPythonバージョン](https://www.tensorflow.org/install)は3.5-3.8です。  
  この記事ではPython 3.8バージョンを使用します。
- ローカルマシンで機械学習を学ぶ計画であれば、GPUを1つ以上準備することをお勧めします。データの前処理程度はCPUでも可能ですが、モデルの学習段階では、モデルの規模が大きくなるほどCPUとGPUの学習速度の差は圧倒的です（特にディープラーニングの場合がそうです）。
  - 機械学習のためであれば、GPU製造メーカーの選択肢は実質的に1つしかありません。NVIDIA製品を使用する必要があります。NVIDIAは機械学習分野に相当多くの投資をしてきた会社であり、ほぼすべての機械学習フレームワークでNVIDIAのCUDAライブラリを利用しています。
  - 機械学習用にGPUを使用する予定であれば、使用しようとするグラフィックカードがCUDA使用可能なモデルかどうかを先に確認する必要があります。現在のコンピュータに搭載されているGPUのモデル名は、ターミナルで```nvidia-smi```コマンドで確認できます。[リンク](https://developer.nvidia.com/cuda-gpus)にあるGPUリストから該当するモデル名を見つけた後、**Compute Capability**の数値を確認しましょう。この数値が少なくとも3.5以上でなければCUDAを使用できません。
  - GPUの選定基準は次の記事によくまとめられています。著者が継続的に更新している記事です。  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  同じ方が書いた[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)という記事も非常に有益です。参考までに、上記の記事の結論は以下の通りです。
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

上記で言及したすべての事項を満たしていれば、作業環境の構築を始めましょう。

## 1. 作業ディレクトリの作成
ターミナルを開き、.bashrcファイルを修正して環境変数を登録します（$プロンプトの後がコマンドです）。  
まず、次のコマンドを使用してnanoエディタを開きます（vimやその他のエディタでも構いません）。
```
$ nano ~/.bashrc
```
最後の行に次の内容を追加します。二重引用符内の内容は、希望すれば別のパスに変更しても構いません。  
```export ML_PATH="$HOME/ml"```

Ctrl+Oを押して保存した後、Ctrl+Xで抜け出します。

次に、以下のコマンドを実行して環境変数を適用します。
```
$ source ~/.bashrc
```
ディレクトリを作成します。
```
$ mkdir -p $ML_PATH
```

## 2. pipパッケージマネージャのインストール
機械学習に必要なPythonパッケージをインストールする方法はいくつかあります。Anacondaのような科学用Python配布版を使用しても良いですし（Windows OSの場合は推奨される方法）、Pythonの自体のパッケージングツールであるpipを使用することもできます。ここでは、LinuxやmacOSのbashシェルでpipコマンドを使用します。

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
その後、独立したPython環境を次のように作成します。このようにする理由は、プロジェクトごとに必要なライブラリのバージョンが異なり、衝突を防ぐためです。新しいプロジェクトを開始するたびに新しい仮想環境を作成して独立した環境を構築すれば良いです。
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
後で仮想環境を無効にするには、```deactivate```コマンドを使用します。環境を有効にした状態では、pipコマンドでインストールするどのパッケージも、この独立した環境にインストールされ、Pythonはこのパッケージを使用します。

## 3′. （仮想環境を作成しない場合）pipバージョンのアップグレード
システムにpipをインストールする際、ディストリビューション（ここではUbuntu）のミラーサーバーにあるバイナリファイルをダウンロードしてインストールしますが、このバイナリファイルは一般的に更新が遅れており、最新バージョンではない場合が多いです（筆者の場合、20.3.4バージョンがインストールされました）。最新バージョンのpipを使用するために、次のコマンドを実行して*ユーザーのホームディレクトリ*にpipをインストール（または既にインストールされている場合はアップグレード）します。  
```
$ python3 -m pip install -U pip

Collecting pip
（中略）
Successfully installed pip-21.0.1
```
pipがこの記事を作成した時点での最新版である21.0.1バージョンでインストールされたことが確認できます。この時、ユーザーのホームディレクトリにインストールしたpipはシステムが自動的に認識しないため、システムが認識して使用できるようにPATH環境変数に登録する必要があります。

再び.bashrcファイルをエディタで開きます。
```
$ nano ~/.bashrc
```
今度は```export PATH=```で始まる行を探します。もしその後に書かれたパスがない場合は、[1段階](#1-作業ディレクトリの作成)で行ったように内容を追加するだけで良いです。既に登録された他のパスがある場合は、コロンを使用してその後ろに内容を追加します。  
```export PATH="$HOME/.local/bin"```  
```export PATH="(既存のパス):$HOME/.local/bin"```

[システムのpipをシステムパッケージマネージャ以外の方法でアップグレードすると、バージョンの衝突により問題が発生する可能性があります](https://github.com/pypa/pip/issues/5599)。そのため、```sudo```を使用せずにユーザーのホームディレクトリにpipをインストールするのです。同じ理由で、仮想環境内でない限り、```pip```コマンドの代わりに```python3 -m pip```コマンドを使用してpipを使用することをお勧めします。

## 4. 機械学習用パッケージ（jupyter、matplotlib、numpy、pandas、scipy、scikit-learn）のインストール
次のpipコマンドで必要なパッケージと依存関係で連結された他のパッケージをすべてインストールします。  
venvを使用しない場合は管理者権限が必要です。  
また、筆者の場合はvenvを使用しているため、単に```pip```コマンドを使用しましたが、venvを使用しない場合は、前述のように```python3 -m pip```コマンドを代わりに使用することをお勧めします。
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
（後略）
```
venvを使用した場合は、Jupyterにカーネルを登録し、名前を付けます。
```
(env) $ python3 -m ipykernel install --user --name=(カーネル名)
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

[T