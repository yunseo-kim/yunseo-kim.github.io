---
title: "NVIDIA Container ToolkitとDocker/Podmanでディープラーニング開発環境を構築する（1）- NVIDIA Container Toolkit & コンテナエンジンのインストール"
description: "このシリーズでは、ローカルにNVIDIA Container Toolkitを用いてコンテナベースのディープラーニング開発環境を構築し、リモートサーバーとして活用できるようSSHおよびJupyterLabを設定する方法を解説します。本記事は第1回として、NVIDIA Container Toolkitとコンテナエンジンのインストール手順を紹介します。"
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## 概要

このシリーズではNVIDIA Container ToolkitとDockerまたはPodmanをインストールし、Docker Hubの[nvidia/cudaリポジトリ](https://hub.docker.com/r/nvidia/cuda)で提供されるCUDAおよびcuDNNイメージをベースにDockerfileを作成して、ディープラーニング開発環境を構築する過程を扱う。必要な方が自由に利用できるよう、この過程を経て完成した[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)と[イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags)をGitHubとDocker Hubで共有し、加えてリモートサーバーとして活用するためのSSHおよびJupyterLab設定ガイドを提供する。  
シリーズは3本の記事で構成する予定で、いま読んでいる本記事はその第1回である。
- 第1回：NVIDIA Container Toolkit & コンテナエンジンのインストール（本文）
- [第2回：GPU活用のためのコンテナランタイム構成、Dockerfileの作成およびコンテナイメージのビルド](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 第3回（アップロード予定）

x86_64 Linux環境でCUDAをサポートするNVIDIAグラフィックカードを搭載したシステムであることを前提に進める。UbuntuまたはFedora以外のディストリビューションでは直接テストしていないため、いくつかの細部は多少異なる可能性がある。  
（12026.1.6. 改訂）

### 開発環境の構成

- ホストOSおよびアーキテクチャ：x86_64、Linux環境（Ubuntu 22.04/24.04 LTS、RHEL/Centos、Fedora、openSUSE/SLES 15.x など）
- 構築する技術スタック（言語・ライブラリ）
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/)（optional, NumPy/SciPy-compatible Array Library for GPU-accelerated Computing with Python）
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/)（optional, to accelerate pandas with zero code changes with the GPU accelerator）
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/)（optional, to quickly visualize and filter through large datasets, with a few lines of code, using best in class charting libraries）
  - [DALI](https://developer.nvidia.com/DALI)（optional, a high-performance alternative to built-in data loaders and data iterators using GPU）
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/)（optional, an accelerated n-dimensional image processing and image I/O alternative to scikit-image）
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/)（optional, to execute machine learning algorithms on GPUs with an API that closely follows the scikit-learn API）
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/)（optional, optimized algorithms for approximate nearest neighbors and clustering, along with many other essential tools for accelerated vector search）
  - [RAFT](https://docs.rapids.ai/api/raft/stable/)（optional, CUDA accelerated primitives which is used by other RAPIDS libraries）
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/)（optional, a GPU-accelerated graph analytics library which includes a zero-code-change accelerator for NetworkX）
  - [tqdm](https://tqdm.github.io/)

  > 状況や好みによっては、pandasの代わりに[Polars](https://pola.rs/)のDataFrameライブラリを使用することも検討できる。Rustで書かれており、[大規模データ処理ではcuDF + pandasの組み合わせには劣るものの、素のpandasパッケージと比べるとかなり優れた性能を示し](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/)、Queryにより特化した文法を提供する。公式の[Polarsブログ](https://pola.rs/posts/polars-on-gpu/)と[cuDFドキュメント](https://docs.rapids.ai/api/cudf/stable/cudf_polars/)によれば、PolarsとNVIDIA RAPIDSチームが協力してcuDFベースのGPU加速エンジンをオープンベータで提供しており、急速に開発が進んでいるという。
  {: .prompt-tip }

  > Docker CEとPodmanのどちらを使うか迷っているなら、[後述の比較表](#3-コンテナエンジンのインストール)が参考になる。
  {: .prompt-tip }

### 以前に作成した機械学習開発環境構築ガイドとの比較表

[以前このブログにアップロードした機械学習開発環境構築ガイド](/posts/Setting-up-a-Machine-Learning-Development-Environment)も存在するが、変更点が多いため新たに本記事を書いた。相違点は以下の表の通り。

| 相違点 | 既存記事（12021バージョン） | 本文（12024執筆、12026改訂バージョン） |
| --- | --- | --- |
| Linuxディストリビューション | Ubuntu基準 | Ubuntuに加えてFedora/RHEL/Centos,<br> Debian, openSUSE/SLESなどでも適用可能 |
| 開発環境の構築方式 | ホストシステムに直接インストール<br>venvを用いたPython仮想環境 | [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)を用いた<br> Dockerコンテナベースの環境<br> uvによるPython仮想環境およびパッケージ管理 |
| NVIDIAグラフィックドライバのインストール | O | O |
| ホストシステムに<br>CUDAおよびcuDNNを直接インストール | O（Aptパッケージマネージャ使用） | X（[Docker HubでNVIDIAが提供する事前インストール<br>イメージ](https://hub.docker.com/r/nvidia/cuda)を使うため、直接作業不要） |
| 移植性 | 別システムへ移行するたびに<br>開発環境を再構築する必要がある | Dockerベースのため、作成済みDockerfileから<br>必要に応じて新規イメージをビルドしたり、<br>既存イメージ（追加ボリュームやネットワーク<br>設定を除く）を容易に移植可能 |
| cuDNN以外の追加<br>GPU加速ライブラリ活用 | X | [CuPy](https://cupy.dev/)、[RAPIDS](https://rapids.ai/)、[DALI](https://developer.nvidia.com/DALI)を導入 |
| Jupyter Notebookインターフェース | Jupyter Notebook（classic） | JupyterLab（Next-Generation） |
| SSHサーバー設定 | 扱わない | 基本的なSSHサーバー設定構成を含む |

## 0. 事前確認事項

- [NVIDIA Container ToolkitはApt、YumまたはDnf、ZypperパッケージマネージャをサポートするLinuxディストリビューションで利用できる。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) リンク先ページで対応ディストリビューション一覧を確認できる。公式サポート表には明記されていないが、FedoraもRHELと同じRed Hat Linux系であるため問題なく利用可能だ。Linuxに不慣れでどのディストリビューションを使うべきか分からないなら、Ubuntu LTS版が無難である。オープンソースではないプロプライエタリドライバも自動インストールされ、初心者でも比較的使いやすい。また利用者が多いため、多くの技術文書がUbuntu基準で書かれている。
  - 使用中のシステムアーキテクチャおよびLinuxディストリビューションのバージョンは、ターミナルで`uname -m && cat /etc/*release`で確認できる。
- システムに搭載されたグラフィックカードが、使用予定のCUDAおよびcuDNNバージョンをサポートしているモデルかを先に確認する必要がある。
  - 現在のGPUモデル名はターミナルで`lspci | grep -i nvidia`により確認できる。
  - <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> で、cuDNNバージョンごとの**対応NVIDIAグラフィックドライババージョン**および要求される**CUDA Compute Capability**条件、そして**対応NVIDIAハードウェア**一覧を確認しよう。
  - <https://developer.nvidia.com/cuda-gpus> のGPU一覧から該当モデルを探し、**Compute Capability**の値を確認しよう。この値が先に確認した**CUDA Compute Capability**条件を満たす必要がある。満たしていればCUDAおよびcuDNNを問題なく利用できる。

> ディープラーニング作業用のグラフィックカードを新規購入する予定なら、GPU選定基準は次の記事にうまく整理されている。筆者が不定期に更新している記事である。  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> GPUだけでなく全体的なハードウェア構成ガイドが必要なら、同じ方が書いた[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)も非常に有益だ。
{: .prompt-tip }

上で言及したすべての条件を満たしたら、作業環境の構成を開始しよう。

## 1. NVIDIAグラフィックドライバのインストール

まずNVIDIAグラフィックドライバをホストシステムにインストールする必要がある。[NVIDIAドライバダウンロードページ](https://www.nvidia.com/drivers/)から`.run`インストーラをダウンロードして使ってもよいが、可能であればシステムのパッケージマネージャを用いてインストールするほうが、バージョン管理・保守の観点で望ましい。<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> の公式ドキュメントを参照し、システム環境に合ったグラフィックドライバをインストールする。

### プロプライエタリモジュール vs オープンソースモジュール

NVIDIAのLinuxドライバはいくつかのカーネルモジュールで構成される。バージョン515ドライバおよびそれ以降のリリースから、NVIDIAは2種類のドライバカーネルモジュールを提供している。

- Proprietary：従来NVIDIAが提供してきた独占ソフトウェアドライバ。
- Open-source：MIT/GPLv2のデュアルライセンスで提供されるオープンソースドライバ。<https://github.com/NVIDIA/open-gpu-kernel-modules> でソースコードを公開している。

ProprietaryドライバはMaxwellアーキテクチャからBlackwell以前までのアーキテクチャ向けに提供され、Blackwellアーキテクチャ以降ではサポート終了予定である。  
一方、Open-sourceドライバはTuringおよびそれ以降のアーキテクチャでサポートされる。

[NVIDIAは可能であればオープンソースのカーネルモジュールを使用することを推奨している。](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
利用中のGPUがオープンソースドライバと互換性があるかは、[このリンク](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus)で確認できる。

本記事ではオープンソースドライバをインストールする前提で説明する。

### Debian & Ubuntu

UbuntuまたはDebianの場合は、ターミナルで次のコマンドを入力してインストールする。
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Fedora 40を基準に、[RPM Fusion](https://rpmfusion.org/RPM%20Fusion)が提供する事前ビルド済みパッケージをダウンロードしてインストールする方法を紹介する。

#### 1-Fedora-1. RPM Fusionリポジトリの構成

[RPM Fusion公式ガイド](https://rpmfusion.org/Configuration)を参照して進める。  
ターミナルで次のコマンドを実行する。

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> DNF旧バージョン（Fedora 40およびそれ以前）では、2行目のopenh264ライブラリリポジトリを有効化するコマンドは次の形だった。
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> しかしDNF 5（Fedora 41+）からは上記の代わりに
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> を入力する必要があるため、それを反映して本文を更新した。
{: .prompt-info }

#### 1-Fedora-2. akmod-nvidiaパッケージのインストール

[RPM Fusionが提供するNVIDIAドライバインストールガイド](https://rpmfusion.org/Howto/NVIDIA)を参照し、akmod-nvidiaパッケージをインストールする。

```bash
sudo dnf update  # この段階でカーネル更新があった場合は、最新カーネルで再起動してから続行する
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> 同様に、DNF旧バージョン（Fedora 40およびそれ以前）では、3行目のautoremove時にNVIDIAドライバが削除されるのを防ぐコマンドは次の形だった。
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> しかしDNF 5（Fedora 41+）からは上記の代わりに
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> を入力する必要があるため、それを反映して本文を更新した。
{: .prompt-info }

> 一方、過去のRPM Fusionは[NVIDIAオープンソースカーネルモジュール](#プロプライエタリモジュール-vs-オープンソースモジュール)に対して否定的な立場を示してきて、特に指定しない限りProprietaryドライバをデフォルト提供していた。しかし[最近（12025年12月）変更されたRPM Fusion側の指針](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open)によれば、重複サポート対象ハードウェア（TuringからBlackwell以前までのアーキテクチャ）については、両者のうちより良いバージョンを自動選択して提供するようになったため、どちらを使うかを手動で選ぶ必要はないとのことだ。Turing以前の旧アーキテクチャや、Blackwellおよびそれ以降の新アーキテクチャについては、もともと選択肢が1つしかないため変更はない。
> これに伴い、`/etc/rpm/macros.nvidia-kmod`によるオープンソースカーネルモジュール使用オプション指定に関する内容が削除されたことを確認した。
>
> また`akmod-nvidia-open`パッケージについては、カーネル空間ドライバにダウンストリーム変更を直接適用する必要がある場合を除き、使用しないようにとのことだ。
>
> これらの点も本文に新たに反映した。
{: .prompt-info }

#### 1-Fedora-3. セキュアブート（Secure Boot）時にドライバを正常ロードするための鍵登録

> 以下で説明する多少の追加手順を踏めば、セキュアブート機能を有効にしたままNVIDIAグラフィックドライバを利用できる。セキュアブートを無効化するとシステムのセキュリティはかなり脆弱になるため、無効化しないことを推奨する。少なくとも12020年代に入って以降、よほどの事情がない限りセキュアブートを無効化する理由はない。
{: .prompt-danger }

まず次のツールをインストールする。

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

次に、以下のコマンドを実行して鍵を生成する。

```bash
sudo kmodgenca -a
```

続いて、UEFIファームウェアのMOKに生成した鍵を登録する必要がある。

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

上記コマンドを実行すると、鍵登録用パスワードの入力を求められるはずだ。しばらく後に鍵登録手続きを完了するため再起動するが、そのときに使うワンタイムパスワードなので、適度に覚えられるものを入力する。

次のコマンドでシステムを再起動する。

```bash
systemctl reboot
```

起動時に自動でMOK管理画面が表示される。「Enroll MOK」を選択し、「Continue」「Yes」を続けて選ぶと、先ほど設定したパスワードの入力を求める画面が出る。パスワードを入力すれば鍵登録手続きは完了する。あとはrebootを入力して再起動すれば、NVIDIAドライバが正常にロードされる。

### NVIDIAドライバのインストール確認

ターミナルで次のコマンドを実行すると、現在ロードされているNVIDIAカーネルモジュールを確認できる。

```bash
cat /proc/driver/nvidia/version
```

以下のような形式のメッセージが出力されれば正常にインストールできている。

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

また、Linux界隈で多くの場合にデフォルト採用されているオープンソースのグラフィックドライバであるnouveauカーネルモジュールは、NVIDIAドライバインストール後に無効化されている必要があり、そうでない場合は問題を引き起こすことがある。NVIDIAドライバをインストールして再起動した後は、次のコマンドを実行して何も出力されないことが正常である。

```bash
lsmod |grep nouveau
```

## 2. NVIDIA Container Toolkitのインストール

次に[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)をインストールする。[NVIDIA Container Toolkit公式インストールガイド](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)を参照して進めればよいが、Fedoraの場合はインストール過程で注意点があるため、このセクションの内容を最後まで確認してから進めてほしい。

### Aptを使用する場合（Ubuntu、Debianなど）

#### 2-Apt-1. パッケージダウンロード用リポジトリの構成

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. パッケージリストの更新

```bash
sudo apt update
```

#### 2-Apt-3. パッケージのインストール

```bash
sudo apt install nvidia-container-toolkit
```

### YumまたはDnfを使用する場合（Fedora、RHEL、Centosなど）

> Fedora 40でテストしたところ、Ubuntuとは異なり`nvidia-smi`コマンドおよび`nvidia-persistenced`パッケージがNVIDIAグラフィックドライバに標準では含まれていなかったため、`xorg-x11-drv-nvidia-cuda`パッケージを追加でインストールする必要があった。RHELおよびCentosでは直接テストしていないが、Fedoraとシステム構成がかなり近いため、以下のガイド通りに進めて問題が出た場合は同様の方法を試すことが助けになるかもしれない。
{: .prompt-warning }

> Fedora 40で上記の方法で`xorg-x11-drv-nvidia-cuda`をインストールし、サンプルワークロードを実行してテストしたところ、私の環境では正常動作した。もしSELinuxなどの理由で依然として問題が発生する場合は、FedoraのAI-MLグループが提供する[Fedora専用のnvidia-container-toolkitパッケージおよびガイド](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/)が役に立つ可能性がある。
{: .prompt-tip }

#### 2-Dnf-1. パッケージダウンロード用リポジトリの構成

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. パッケージのインストール

```bash
sudo dnf install nvidia-container-toolkit
```

または

```bash
sudo yum install nvidia-container-toolkit
```

### Zypperを使用する場合（openSUSE、SLES）

#### 2-Zypper-1. パッケージダウンロード用リポジトリの構成

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. パッケージのインストール

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. コンテナエンジンのインストール

次に、コンテナエンジンとしてDocker CEまたはPodmanをインストールする。利用環境と好みに合わせてどちらかを選んでインストールすればよい。[Docker公式ドキュメント](https://docs.docker.com/engine/install/)と[Podman公式ドキュメント](https://podman.io/docs/installation)を参照する。

以下の表はDockerとPodmanの主要な違いと長所・短所をまとめたものだ。

| 比較項目 | Docker | Podman |
| --- | --- | --- |
| アーキテクチャ | クライアント-サーバーモデル、デーモン（daemon）ベース | デーモンレス（daemonless）構造 |
| セキュリティ | 基本的にroot権限で動作するデーモンに<br>依存するため潜在的なセキュリティリスクがある<br>（12020年に公開されたバージョン20.10から<br>ルートレスモードをサポートするが追加設定が必要） | デーモンに依存しないため、別途指定しない<br>限り基本的にルートレスで動作し、<br>SELinuxにより保護される |
| リソース使用量 | デーモンベース構造の特性上、バックグラウンドプロセスが<br>常時動作するため、一般により多くの<br>リソースを使用 | 一般により少ないオーバーヘッド（overhead） |
| コンテナ起動時間 | 相対的に遅い | 簡素化されたアーキテクチャにより最大50%程度<br>高速に起動 |
| エコシステム・文書化 | 広範なエコシステムとコミュニティ支援、<br>豊富な関連ドキュメント | 相対的に小規模なエコシステムと関連ドキュメント |
| ネットワーキング | Docker Bridge Networkを使用 | CNI（Container Network Interface）<br>プラグインを使用 |
| Kubernetes YAML<br>ネイティブサポート | X（変換が必要） | O |

参考資料:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Dockerは歴史が長く、業界で事実上の標準的地位を享受してきたため、広いエコシステムと豊富な関連ドキュメントが存在する点が最大の利点だ。  
PodmanはRed Hatにより比較的最近開発され、設計段階からデーモンレス（daemonless）・ルートレス（rootless）を志向する先進的な構造であるため、セキュリティ、システム資源使用量、コンテナ起動時間など多方面で利点を持つ。デーモンに問題が生じて停止すると全コンテナがまとめて落ちるDockerと異なり、各コンテナが完全に独立しているため、特定コンテナの停止が他コンテナに影響しない点もPodmanの強みである。

各自の状況に合わせてツールを選ぶことが何より重要だが、入門者であればPodmanから始めるのが良い選択に思える。Dockerに比べてエコシステム規模は小さいものの、前述の利点により急速に成長して差を縮めており、Dockerfile文法やDockerイメージ、CLI（コマンドラインインターフェース）など多くの点で既存のDockerと互換性がある。既にDockerベースで大規模システムを構築済みで、Podman採用に大きな移行コストがかかる、といった事情がないなら、最初からPodmanを採用するのが合理的だ。

### Podman

主要なLinuxディストリビューションの多くで、システム標準リポジトリから提供されるため簡単にインストールできる。

#### Ubuntuの場合

```bash
sudo apt install podman
```

#### Fedoraの場合

```bash
sudo dnf install podman
```

#### openSUSEの場合

```bash
sudo zypper install podman
```

#### 正常に設定されているか確認

ターミナルで次のコマンドを実行してみる。

```bash
podman run --rm hello-world
```

以下のようなメッセージが出力されれば成功だ。

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

> 12025-12-18T00:43:00+09:00時点で、podmanバージョン5.7.1、[passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`、fedora 43環境を基準にテストしたところ、上記hello-worldを含め、コンテナ実行またはイメージビルド時に次のエラーが発生した。
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> 現在私はIPv6を使用しておらずIPv4ネットワーク環境にいるにもかかわらず、コンテナネットワーク構成段階でpasta（passtライブラリに含まれる）がIPv6ルーティングを試みることで発生する問題に見える。コンテナ実行や[後述のイメージビルド段階](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-dockerイメージのビルドとコンテナの実行)で、以下のように`--net=pasta:-4`オプションを明示してIPv4を使うようにすると問題が発生しないことを確認した。
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> 調べてみると、[同様の症状で以前に登録されたイシュー](https://github.com/containers/podman/issues/22824)が存在した。当該イシューは[2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/)で修正されたとあるが、観測された症状が同一である点、Proton VPN使用中に発生した問題である点など、多くの部分が非常によく似ているため、類似のイシューが再発したのではないかと推測している。
{: .prompt-warning }

### Docker CE

#### Ubuntuの場合

##### 3-Ubuntu-1. パッケージ競合防止のため旧版または非公式パッケージを削除

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. リポジトリの構成

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

##### 3-Ubuntu-3. パッケージのインストール

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. `Docker`グループを作成してユーザーを登録

non-rootユーザーでも`sudo`なしでDockerを管理できるようにするには、`Docker`グループを作成し、Dockerを利用するユーザーを登録すればよい。ターミナルで次のコマンドを実行する。

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

その後、ログアウトして再ログインすれば変更が適用される。UbuntuまたはDebianの場合、特に追加作業をしなくてもシステム起動時にDockerサービスが自動起動する。

#### Fedoraの場合

##### 3-Fedora-1. パッケージ競合防止のため旧版または非公式パッケージを削除

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

##### 3-Fedora-2. リポジトリの構成

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. パッケージのインストール

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

パッケージインストール中にGPGキーを承認するかの確認が出るはずだ。GPGキーが`060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`と一致するなら、yを入力して承認すればよい。  
> もしGPGキーが一致しない場合、サプライチェーン攻撃により偽造パッケージをダウンロードした可能性があるため、インストールを中止すべきである。
{: .prompt-danger }

##### 3-Fedora-4. Dockerデーモンの起動

Dockerのインストールは完了しているが未起動の状態なので、次のコマンドでDockerを起動できる。

```bash
sudo systemctl start docker
```

システム起動時にDockerサービスを自動起動させたい場合は、次を実行する。

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. `Docker`グループにユーザーを登録

non-rootユーザーでもDockerを管理できるようにするには、`Docker`グループにDockerを利用するユーザーを登録する。Fedoraの場合、前述のパッケージインストール時に`Docker`グループが自動作成されるため、ユーザー登録のみ行えばよい。

```bash
sudo usermod -aG docker $USER
```

その後ログアウトして再ログインすれば変更が適用される。

#### 正常に設定されているか確認

ターミナルで次のコマンドを実行してみる。

```bash
docker run hello-world
```

以下のようなメッセージが出力されれば成功だ。

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

## Further Reading
[第2回](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)に続く
