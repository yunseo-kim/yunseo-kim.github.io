---
title: NVIDIA Container ToolkitとDocker/Podmanでディープラーニング開発環境を構築する (1) - NVIDIA Container Toolkit
  & コンテナエンジンのインストール
description: このシリーズではローカルにNVIDIA Container Toolkitでコンテナベースのディープラーニング開発環境を構築し、リモートサーバーとして
  活用できるようにSSHおよびJupyter Labを設定する方法を扱います。この投稿はシリーズの最初の記事で、NVIDIA Container
  Toolkitとコンテナエンジンのインストール方法を紹介します。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---
## 概要
このシリーズではNVIDIA Container ToolkitとDockerまたはPodmanをインストールし、Docker Hubの[nvidia/cudaリポジトリ](https://hub.docker.com/r/nvidia/cuda)から提供されるCUDAおよびcuDNNイメージをベースにDockerfileを作成してディープラーニング開発環境を構築するプロセスを扱います。必要な方が自由に利用できるように、このプロセスを経て完成した[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)と[イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags)をGitHubとDocker Hubを通じて共有し、さらにリモートサーバーとして活用するためのSSHおよびJupyter Lab設定ガイドを提供します。  
シリーズは3つの記事で構成される予定で、現在読んでいるこの記事はそのシリーズの最初の記事です。
- 第1回：NVIDIA Container Toolkit & コンテナエンジンのインストール（本文）
- [第2回：GPU活用のためのコンテナランタイム構成、Dockerfileの作成およびコンテナイメージのビルド](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 第3回（アップロード予定）

x86_64 Linuxの環境でCUDAをサポートするNVIDIAグラフィックカードを搭載したシステムを前提として進めます。UbuntuやFedora以外のディストリビューションでは直接テストしていないため、いくつかの詳細な部分で若干の違いがあるかもしれません。  
（12025.02.18. 内容更新）

### 開発環境構成
- ホストOS・アーキテクチャ：x86_64、Linux環境（Ubuntu 18.04/20.04/22.04 LTS、RHEL/Centos、Fedora、openSUSE/SLES 15.xなど）
- 構築する技術スタック（言語およびライブラリ）
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE / Podman
  - CUDA 12.4
  - cuDNN
  - OpenSSH
  - tmux
  - JupyterLab
  - NumPy & SciPy
  - CuPy (optional, NumPy/SciPy-compatible Array Library for GPU-accelerated Computing with Python)
  - pandas
  - cuDF (optional, to accelerate pandas with zero code changes with the GPU accelerator)
  - Matplotlib & Seaborn
  - DALI (optional, high-performance alternative to built-in data loaders and data iterators using GPU)
  - scikit-learn
  - cuML (optional, to execute machine learning algorithms on GPUs with an API that closely follows the scikit-learn API)
  - PyTorch
  - tqdm

  > 状況によって、また個人の好みによって、pandasの代わりに[Polars](https://pola.rs/) DataFrameライブラリを使用することも検討できます。Rustで書かれており、[大量データ処理時にはcuDF + pandas組み合わせには劣りますが、純正pandasパッケージと比較するとかなり優れたパフォーマンスを示し](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/)、クエリにより特化した文法を提供します。[Polars公式ブログ](https://pola.rs/posts/polars-on-gpu/)によると、NVIDIA RAPIDSチームと協力して近い将来cuDFとの連携もサポートする予定だとのことです。
  {: .prompt-tip }

  > Docker CEとPodmanのどちらを使用するか迷っている場合は、[後述の比較表](#3-コンテナエンジンのインストール)が参考になるでしょう。
  {: .prompt-tip }

### 以前に作成した機械学習開発環境構築ガイドとの比較表
[以前このブログにアップロードした機械学習開発環境構築ガイド](/posts/Setting-up-a-Machine-Learning-Development-Environment)が既に存在し、ほとんどは依然として有効ですが、いくつかの変更点があるため、この投稿を新たに作成しました。変更点は以下の表の通りです。

| 相違点 | 既存の記事（12021版） | 本文（12024版） |
| --- | --- | --- |
| Linuxディストリビューション | Ubuntuベース | Ubuntu以外にもFedora/RHEL/Centos、<br> Debian、openSUSE/SLESなどでも適用可能 |
| 開発環境構築方式 | venvを利用したPython仮想環境 | [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)を利用した<br> Dockerコンテナベース環境 |
| NVIDIAグラフィックドライバのインストール | O | O |
| ホストシステムに<br>CUDAおよびcuDNNを直接インストール | O（Aptパッケージマネージャ使用） | X（[Docker HubでNVIDIAが提供する事前インストール<br>イメージ](https://hub.docker.com/r/nvidia/cuda)を使用するため直接作業不要）
| 移植性 | 別のシステムに移行するたびに<br>開発環境を新たに構築する必要がある | Dockerベースのため、作成しておいたDockerfileで<br>必要な時に新しいイメージをビルドしたり、<br>既存に使用していたイメージ（追加ボリュームや<br>ネットワーク設定を除く）を簡単に移植可能 |
| cuDNN以外の追加的な<br>GPU加速ライブラリの活用 | X | [CuPy](https://cupy.dev/)、[cuDF](https://docs.rapids.ai/api/cudf/stable/)、[cuML](https://docs.rapids.ai/api/cuml/stable/)、[DALI](https://developer.nvidia.com/DALI)導入 |
| Jupyter Notebookインターフェース | Jupyter Notebook（classic） | JupyterLab（Next-Generation） |
| SSHサーバー設定 | 特に扱わない | 第3回で基本的なSSHサーバー設定構成を含む |

Dockerではなくvenvなどのpython仮想環境を活用したい場合は、[既存の記事](/posts/Setting-up-a-Machine-Learning-Development-Environment)も依然として有効なので、そちらを参考にすることをお勧めします。

## 0. 事前確認事項
- [NVIDIA Container ToolkitはApt、YumまたはDnf、ZypperパッケージマネージャをサポートするLinuxディストリビューションで使用可能です。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html)リンク先のページでサポートされているLinuxディストリビューションのリストを確認できます。公式サポート表には別途記載されていませんが、FedoraもRHELと同じRed Hat Linuxベースなので問題なく使用できます。Linux環境に慣れておらず、どのディストリビューションを使用すべきかよくわからない場合は、Ubuntu LTSバージョンを使用するのが最も無難です。オープンソースではない独占的なドライバも自動インストールされるため初心者が使用するにも比較的便利で、ユーザー数が多いため、ほとんどの技術文書がUbuntuを基準に作成されています。
  - 使用中のシステムアーキテクチャとLinuxディストリビューションのバージョンは、ターミナルで`uname -m && cat /etc/*release`コマンドで確認できます。
- システムに搭載されているグラフィックカードが使用しようとするCUDAおよびcuDNNバージョンをサポートするモデルかどうかを確認する必要があります。
  - 現在のコンピュータに搭載されているGPUモデル名は、ターミナルで`lspci | grep -i nvidia`コマンドで確認できます。
  - <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>ページでcuDNNバージョン別に**サポートするNVIDIAグラフィックドライババージョン**および要求される**CUDA Compute Capability**条件、そして**サポートするNVIDIAハードウェア**リストを確認しましょう。
  - <https://developer.nvidia.com/cuda-gpus>にあるGPUリストから該当するモデル名を見つけ、**Compute Capability**数値を確認しましょう。この数値が先ほど確認した**CUDA Compute Capability**条件を満たしていれば、CUDAおよびcuDNNを問題なく使用できます。

> ディープラーニング作業用グラフィックカードを新たに購入予定なら、GPU選定基準は次の記事によくまとめられています。筆者が継続的に更新している記事です。  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> 同じ方が書いた[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)という記事も非常に有益です。
{: .prompt-tip }

上記で言及したすべての事項を満たしていれば、作業環境の構築を始めましょう。

## 1. NVIDIAグラフィックドライバのインストール
まずNVIDIAグラフィックドライバをホストシステムにインストールする必要があります。[NVIDIAドライバダウンロードページ](https://www.nvidia.com/drivers/)から.runインストーラをダウンロードして利用しても良いですが、できれば自分のシステムのパッケージマネージャを活用してインストールする方が、バージョン管理およびメンテナンス面で良いでしょう。<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>公式ドキュメントを参考にして、自分のシステム環境に合ったグラフィックドライバをインストールします。

### Proprietary module vs Open-source module
NVIDIA Linuxドライバはいくつかのカーネルモジュールで構成されており、バージョン515ドライバおよびそれ以降のリリースからNVIDIAでは2種類のドライバカーネルモジュールを提供しています。

- Proprietary：NVIDIAが従来提供してきた独占的ソフトウェアドライバ。
- Open-source：MIT/GPLv2デュアルライセンスで提供されるオープンソースドライバ。<https://github.com/NVIDIA/open-gpu-kernel-modules>を通じてソースコードを公開。

Proprietaryドライバは、MaxwellアーキテクチャからBlackwell以前のアーキテクチャに基づいて設計されたGPUに対して提供され、Blackwellアーキテクチャからはサポートが終了する予定です。
一方、Open-sourceドライバはTuringおよびそれ以降のアーキテクチャに対してサポートされます。

[NVIDIAでは可能であればオープンソースカーネルモジュールを使用することを推奨しています。](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
使用中のGPUがオープンソースドライバと互換性があるかどうかは[このリンク](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus)で確認できます。

この記事ではオープンソースドライバをインストールすると仮定して説明します。

### Debian & Ubuntu
UbuntuまたはDebianの場合、ターミナルで次のコマンドを入力してインストールします。
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Fedora 40を基準に、[RPM Fusion](https://rpmfusion.org/RPM%20Fusion)から提供される事前ビルドされたパッケージをダウンロードしてインストールする方法を紹介します。

#### 1-Fedora-1. RPM Fusionリポジトリの構成  
[RPM Fusion公式ガイド](https://rpmfusion.org/Configuration)を参考に進めます。  
ターミナルで次のコマンドを実行します。
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. akmod-nvidia-openパッケージのインストール  
[RPM Fusionが提供するNVIDIAドライバインストールガイド](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open)を参考に、
rpmfusion-nonfree-taintedリポジトリを有効化した後、akmod-nvidia-openパッケージをインストールします。
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark user akmod-nvidia-open
```

> DNF 旧バージョン（Fedora 40 およびそれ以前）では、最後の行の autoremove 時に NVIDIA ドライバーが削除されるのを防ぐためのコマンドは次のとおりだった。
>
> ```bash
> sudo dnf mark install akmod-nvidia-open
> ```
>
> しかし DNF 5（Fedora 41+）からは、上記のコマンドの代わりに
>
> ```bash
> sudo dnf mark user akmod-nvidia-open
> ```
>
> を入力する必要があり、これを反映して本文の内容を更新しておいた。
{: .prompt-tip }

#### 1-Fedora-3. セキュアブート（Secure Boot）時にドライバが正常にロードされるためのキー登録  

> 以下で説明する少しの追加手順を踏めば、正常にセキュアブート機能を利用しながらNVIDIAグラフィックドライバを使用できます。セキュアブートを無効にするとシステムのセキュリティがかなり脆弱になるため、無効にしないことをお勧めします。少なくとも12020年代に入ってからは、よほどのことがない限りセキュアブートを解除する理由はありません。
{: .prompt-danger }

まず次のツールをインストールします。
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

次に、以下のコマンドを実行してキーを生成します。
```bash
sudo kmodgenca -a
```
今度はUEFIファームウェアのMOKに生成したキーを登録する必要があります。
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
上記コマンドを実行すると、キー登録のためのパスワードを入力するよう表示されます。しばらく後にキー登録手続き完了のために再起動しますが、その時に使用する使い捨てパスワードなので、適当に覚えられるものを入力してください。

次のコマンドを実行してシステムを再起動します。
```bash
systemctl reboot
```
システムが起動する際に自動的にMOK管理画面が表示されます。「Enroll MOK」を選択した後、「Continue」、「Yes」を続けて選択すると、先ほど設定したパスワードを要求する画面が表示されます。先ほど設定したパスワードを入力すると、キー登録手続きが完了します。今度は「reboot」と入力して再起動すると、正常にNVIDIAドライバがロードされるはずです。

### NVIDIAドライバのインストール確認
ターミナルで次のコマンドを実行して、現在ロードされているNVIDIAカーネルモジュールを確認できます。
```bash
cat /proc/driver/nvidia/version
```
以下のような形式のメッセージが出力されれば正常にインストールされています。
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. NVIDIA Container Toolkitのインストール
次に[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)をインストールする必要があります。[NVIDIA Container Toolkit公式インストールガイド](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)を参考にしてインストールを進めますが、Fedoraの場合はインストール過程で注意事項があるため、このセクションの内容を最後まで確認してから進めてください。

### Aptを使用する場合（Ubuntu、Debianなど）
#### 2-Apt-1. パッケージダウンロードのためのリポジトリ構成
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
> Fedora 40でテストした際、Ubuntuとは異なり、`nvidia-smi`コマンドおよび`nvidia-persistenced`パッケージがNVIDIAグラフィックドライバに標準で含まれておらず、`xorg-x11-drv-nvidia-cuda`パッケージを追加インストールする必要がありました。RHELおよびCentosでは直接テストしていませんが、Fedoraとシステム構成が非常に似ているため、もし以下のガイドに従って進めた際に問題が発生した場合は、同じ方法を試してみると役立つかもしれません。
{: .prompt-warning }

> Fedora 40で上記の方法で`xorg-x11-drv-nvidia-cuda`をインストールし、サンプルワークロードを実行してテストした際、筆者のシステムでは正常に動作しました。もしSELinuxなどの理由でまだ問題が発生する場合は、FedoraのAI-MLグループが提供する[Fedora専用nvidia-container-toolkitパッケージおよびガイド](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/)が役立つかもしれません。
{: .prompt-tip }

#### 2-Dnf-1. パッケージダウンロードのためのリポジトリ構成
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
#### 2-Zypper-1. パッケージダウンロードのためのリポジトリ構成
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. パッケージのインストール
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. コンテナエンジンのインストール
次にコンテナエンジンとしてDocker CEまたはPodmanをインストールします。使用環境と好みに合わせて、どちらか一方を選択してインストールすれば良く、[Docker公式ドキュメント](https://docs.docker.com/engine/install/)と[Podman公式ドキュメント](https://podman.io/docs/installation)を参考にします。

次の表はDockerとPodmanの主な違いと長所・短所をまとめたものです。

| 比較項目 | Docker | Podman |
| --- | --- | --- |
| アーキテクチャ | クライアント-サーバーモデル、デーモン（daemon）ベース | デーモンレス（daemonless）構造 |
| セキュリティ | 基本的にroot権限で実行されるデーモンに<br>依存するため潜在的なセキュリティ上のリスクが存在<br>（12020年発表のバージョン20.10からルートレス<br>モードをサポートするが、追加設定が必要） | デーモンに依存せず、別途指定しない限り<br>基本的にルートレスで動作し、<br>SELinuxで保護される |
| リソース使用量 | デーモンベース構造の特性上、バックグラウンドプロセスが<br>常時動作するため、一般的により多くの<br>リソースを使用 | 一般的により少ないリソースオーバーヘッド |
| コンテナ起動時間 | 比較的遅い | 簡素化されたアーキテクチャで最大50%程度<br>速く実行される |
| エコシステムとドキュメント化 | 広範なエコシステムとコミュニティサポート、<br>豊富な関連ドキュメント | 比較的小規模のエコシステムと関連ドキュメント |
| ネットワーキング | Docker Bridge Networkを使用 | CNI（Container Network Interface）<br>プラグインを使用 |
| Kubernetes YAML<br>ネイティブサポート | X（変換が必要） | O |

参考資料：
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Dockerはその歴史がより長く、業界で事実上の標準的地位を享受してきたため、幅広いエコシステムと豊富な関連ドキュメントが存在することが最大の利点です。  
PodmanはRed Hatによって比較的最近開発され、生まれながらにデーモンレス（daemonless）、ルートレス（rootless）を志向する発展した構造であるため、セキュリティ、システムリソース使用量およびコンテナ起動時間など様々な面で利点を持ちます。デーモンに問題が生じてダウンすると全てのコンテナが一緒にダウンするDockerとは異なり、各コンテナが完全に独立しているため特定のコンテナのダウンが他のコンテナに影響を与えないという点もPodmanの強みです。

それぞれの与えられた条件に合わせて使用するツールを選択することが何よりも重要であり、初めて入門する個人ユーザーであればPodmanから始めるのが良い選択かもしれません。Dockerに比べて相対的にエコシステムの規模が小さいとはいえ、上述した様々な利点のおかげで急速に成長しギャップを縮めており、Dockerfile構文やDockerイメージ、CLI（コマンドラインインターフェース）など多くの部分で既存のDockerと互換性があるため、個人や小規模団体の立場ではそれほど問題にならないでしょう。

### Podman
大多数の主要Linuxディストリビューションのシステム基本リポジトリでサポートされているため、簡単にインストールできます。

#### Ubuntuの場合
```bash
sudo apt install podman
```

#### Fedoraの場合
```bash
sudo dnf install podman
```

#### openSUSE
```bash
sudo zypper install podman
```

### Docker CE
#### Ubuntuの場合
##### 3-Ubuntu-1. パッケージ競合防止のための以前のバージョンや非公式パッケージの削除
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

##### 3-Ubuntu-4. `Docker`グループを作成してユーザーを登録する
non-rootユーザーも`sudo`なしでDockerを管理できるようにするには、`Docker`グループを作成した後、Dockerを利用したいユーザーを登録します。ターミナルで次のコマンドを実行します。
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
その後、ログアウトして再度ログインすると変更された設定が適用されます。UbuntuまたはDebianの場合、特別な作業なしでもシステム起動時ごとにDockerサービスが自動的に実行されます。

#### Fedoraの場合
##### 3-Fedora-1. パッケージ競合防止のための以前のバージョンや非公式パッケージの削除
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

##### 3-Fedora-2. リポジトリの
