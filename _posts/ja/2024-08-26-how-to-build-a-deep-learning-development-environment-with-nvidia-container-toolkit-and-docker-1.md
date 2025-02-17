---
title: NVIDIA Container ToolkitとDocker/Podmanでディープラーニング開発環境を構築する (1) - NVIDIA Container Toolkit & コンテナエンジンのインストール
description: このシリーズでは、ローカルにNVIDIA Container Toolkitを使用してコンテナベースのディープラーニング開発環境を構築し、リモートサーバーとして活用できるようSSHおよびJupyter Labを設定する方法を扱います。この投稿はシリーズの最初の記事で、NVIDIA Container Toolkitとコンテナエンジンのインストール方法を紹介します。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---

## 概要

このシリーズでは、NVIDIA Container ToolkitとDockerまたはPodmanをインストールし、Docker Hubの[nvidia/cudaリポジトリ](https://hub.docker.com/r/nvidia/cuda)が提供するCUDAおよびcuDNNイメージをベースにDockerfileを作成してディープラーニング開発環境を構築するプロセスを扱います。必要な方が自由に使用できるよう、このプロセスを経て完成した[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)と[イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags)をGitHubとDocker Hubを通じて共有し、さらにリモートサーバーとして活用するためのSSHおよびJupyter Lab設定ガイドを提供します。  
シリーズは3つの記事で構成される予定で、この記事はそのシリーズの最初の記事です。
- 第1回：NVIDIA Container Toolkit & コンテナエンジンのインストール（本文）
- [第2回：GPUを活用するためのコンテナランタイムの構成、Dockerfileの作成およびコンテナイメージのビルド](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 第3回（アップロード予定）

x86_64 Linux環境でCUDAをサポートするNVIDIAグラフィックカードを搭載したシステムを前提として進めます。UbuntuまたはFedora以外のディストリビューションでは直接テストしていないため、いくつかの細かい部分で若干の違いがある可能性があります。  
（2025.02.18. 内容更新）

### 開発環境の構成
- ホストオペレーティングシステムとアーキテクチャ：x86_64、Linux環境（Ubuntu 18.04/20.04/22.04 LTS、RHEL/Centos、Fedora、openSUSE/SLES 15.xなど）
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
  - CuPy （オプション、GPUを使用したPythonでの高速計算のためのNumPy/SciPy互換配列ライブラリ）
  - pandas
  - cuDF （オプション、コードを変更せずにGPUアクセラレータでpandasを高速化）
  - Matplotlib & Seaborn
  - DALI （オプション、GPUを使用した高性能な組み込みデータローダーおよびデータイテレータの代替）
  - scikit-learn
  - cuML （オプション、scikit-learn APIに近いAPIを使用してGPU上で機械学習アルゴリズムを実行）
  - PyTorch
  - tqdm

  > 状況に応じて、また個人の好みに応じて、pandasの代わりに[Polars](https://pola.rs/) DataFrameライブラリを使用することも検討できます。Rustで書かれており、[大規模データ処理時にcuDF + pandasの組み合わせには及ばないものの、純粋なpandasパッケージと比較するとかなり優れたパフォーマンスを示し](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/)、クエリにより特化した文法を提供します。[Polars公式ブログ](https://pola.rs/posts/polars-on-gpu/)によると、NVIDIA RAPIDSチームと協力して近い将来cuDFとの連携もサポートする予定だそうです。
  {: .prompt-tip }

  > Docker CEとPodmanのどちらを使用するか迷っている場合は、[後述の比較表](#3-コンテナエンジンのインストール)が参考になるかもしれません。
  {: .prompt-tip }

### 以前に作成した機械学習開発環境構築ガイドとの比較表
[以前このブログにアップロードした機械学習開発環境構築ガイド](/posts/Setting-up-a-Machine-Learning-Development-Environment)がすでに存在し、ほとんどはまだ有効ですが、いくつかの変更点があるため、この投稿を新たに作成しました。変更点は以下の表の通りです。

| 相違点 | 既存の記事（2021年版） | 本文（2024年版） |
| --- | --- | --- |
| Linuxディストリビューション | Ubuntuベース | Ubuntu以外にもFedora/RHEL/Centos、<br>Debian、openSUSE/SLESなどにも適用可能 |
| 開発環境構築方法 | venvを使用したPython仮想環境 | [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)を使用した<br>Dockerコンテナベースの環境 |
| NVIDIAグラフィックドライバのインストール | O | O |
| ホストシステムへの<br>CUDAおよびcuDNNの直接インストール | O（Aptパッケージマネージャを使用） | X（[Docker HubでNVIDIAが提供する事前インストール<br>イメージ](https://hub.docker.com/r/nvidia/cuda)を使用するため、直接作業する必要なし）
| 移植性 | 他のシステムに移行するたびに<br>開発環境を新たに構築する必要がある | Dockerベースのため、作成しておいたDockerfileで<br>必要に応じて新しいイメージをビルドするか、<br>既存のイメージ（追加ボリュームやネットワーク<br>設定を除く）を簡単に移植可能 |
| cuDNN以外の追加的な<br>GPU加速ライブラリの活用 | X | [CuPy](https://cupy.dev/)、[cuDF](https://docs.rapids.ai/api/cudf/stable/)、[cuML](https://docs.rapids.ai/api/cuml/stable/)、[DALI](https://developer.nvidia.com/DALI)の導入 |
| Jupyter Notebookインターフェース | Jupyter Notebook（classic） | JupyterLab（Next-Generation） |
| SSHサーバー設定 | 別途扱わない | 第3回で基本的なSSHサーバー設定構成を含む |

Dockerではなくvenvなどのpython仮想環境を活用したい場合は、[既存の記事](/posts/Setting-up-a-Machine-Learning-Development-Environment)もまだ有効なので、その記事を参考にすることをお勧めします。

## 0. 事前確認事項
- [NVIDIA Container ToolkitはApt、YumまたはDnf、ZypperパッケージマネージャをサポートするLinuxディストリビューションで使用可能です。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html)リンクされたページでサポートされているLinuxディストリビューションのリストを確認できます。公式サポート表には別途記載されていませんが、FedoraもRHELと同じRed Hat Linuxベースなので問題なく使用可能です。Linuxに慣れていない方で、どのディストリビューションを使用すべきかよくわからない場合は、Ubuntu LTSバージョンを使用するのが最も無難です。オープンソースではない独占的なドライバも自動インストールされるため、初心者が使用するにも比較的便利で、ユーザー数が多いため、ほとんどの技術文書がUbuntuを基準に作成されています。
  - 使用中のシステムアーキテクチャとLinuxディストリビューションのバージョンは、ターミナルで`uname -m && cat /etc/*release`コマンドで確認できます。
- システムに搭載されているグラフィックカードが使用しようとするCUDAおよびcuDNNバージョンをサポートするモデルかどうかを先に確認する必要があります。
  - 現在のコンピュータに搭載されているGPUモデル名は、ターミナルで`lspci | grep -i nvidia`コマンドで確認できます。
  - <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>ページでcuDNNバージョン別の**サポートされるNVIDIAグラフィックドライババージョン**および要求される**CUDA Compute Capability**条件、そして**サポートされるNVIDIAハードウェア**リストを確認しましょう。
  - <https://developer.nvidia.com/cuda-gpus>にあるGPUリストで該当するモデル名を見つけ、**Compute Capability**数値を確認しましょう。この数値が先ほど確認した**CUDA Compute Capability**条件を満たしていれば、CUDAおよびcuDNNを問題なく使用できます。

> ディープラーニング作業用のグラフィックカードを新しく購入する予定なら、GPU選定基準は次の記事によくまとめられています。筆者が継続的に更新している記事です。  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> 同じ方が書いた[A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)という記事も非常に有益です。
{: .prompt-tip }

上記で言及したすべての事項を満たしていれば、作業環境の構築を始めましょう。

## 1. NVIDIAグラフィックドライバのインストール
まず、NVIDIAグラフィックドライバをホストシステムにインストールする必要があります。[NVIDIAドライバダウンロードページ](https://www.nvidia.com/drivers/)から.runインストーラーをダウンロードして利用しても構いませんが、できるだけ自分のシステムのパッケージマネージャを活用してインストールするのがバージョン管理とメンテナンス面で良いです。<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation>公式ドキュメントを参考に、自分のシステム環境に合ったグラフィックドライバをインストールします。

### プロプライエタリモジュール vs オープンソースモジュール
NVIDIA Linuxドライバはいくつかのカーネルモジュールで構成されており、バージョン515ドライバおよびそれ以降のリリースから、NVIDIAは2種類のドライバカーネルモジュールを提供しています。

- プロプライエタリ：NVIDIAが従来提供してきた独占ソフトウェアドライバ。
- オープンソース：MIT/GPLv2デュアルライセンスで提供されるオープンソースドライバ。<https://github.com/NVIDIA/open-gpu-kernel-modules>を通じてソースコードを公開しています。

プロプライエタリドライバはMaxwellアーキテクチャからBlackwell以前のアーキテクチャまでのGPUに対して提供され、Blackwellアーキテクチャからはサポートが終了する予定です。
一方、オープンソースドライバはTuringおよびそれ以降のアーキテクチャに対してサポートされます。

[NVIDIAは可能であればオープンソースカーネルモジュールを使用することを推奨しています。](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
使用中のGPUがオープンソースドライバと互換性があるかどうかは[このリンク](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus)で確認できます。

この記事ではオープンソースドライバをインストールすると仮定して説明します。

### Debian & Ubuntu
UbuntuまたはDebianの場合、ターミナルで次のコマンドを入力してインストールします。
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Fedora 40を基準に、[RPM Fusion](https://rpmfusion.org/RPM%20Fusion)が提供する事前ビルドされたパッケージをダウンロードしてインストールする方法を紹介します。

#### 1-Fedora-1. RPM Fusionリポジトリの構成  
[RPM Fusion公式ガイド](https://rpmfusion.org/Configuration)を参考に進めます。  
ターミナルで次のコマンドを実行します。
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. akmod-nvidia-openパッケージのインストール  
[RPM Fusionが提供するNVIDIAドライバインストールガイド](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open)を参考に、
rpmfusion-nonfree-taintedリポジトリを有効にした後、akmod-nvidia-openパッケージをインストールします。
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. セキュアブート（Secure Boot）時のドライバ正常ロードのためのキー登録  

> 以下で説明する若干の追加手順を踏めば、正常にセキュアブート機能を利用しながらNVIDIAグラフィックドライバを使用できます。セキュアブートを無効にするとシステムのセキュリティがかなり脆弱になるため、無効にしないことをお勧めします。少なくとも2020年代に入ってからは、よほどのことがない限りセキュアブートを解除する理由はありません。
{: .prompt-danger }

まず、次のツールをインストールします。
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

次に、以下のコマンドを実行してキーを生成します。
```bash
sudo kmodgenca -a
```
これでUEFIファームウェアのMOKに生成したキーを登録する必要があります。
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
上記のコマンドを実行すると、キー登録のためのパスワードを入力するよう表示されます。しばらく後にキー登録手順完了のために再起動しますが、その時に使用する一回限りのパスワードなので、適当に覚えられるものを入力します。

これで次のコマンドを実行してシステムを再起動します。
```bash
systemctl reboot
```
システムが起動する際に自動的にMOK管理ウィンドウが表示されます。"Enroll MOK"を選択した後、"Continue"、"Yes"を連続して選択すると、先ほど設定したパスワードを要求するウィンドウが表示されます。先ほど設定したパスワードを入力すると、キー登録手順が完了します。これでrebootを入力して再起動すると、正常にNVIDIAドライバがロードされるはずです。

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
次に[NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)をインストールする必要があります。[NVIDIA Container Toolkit公式インストールガイド](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)を参考にインストールを進めますが、Fedoraの場合はインストール過程で注意事項があるため、このセクションの内容を最後まで確認してから進めてください。

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
> Fedora 40でテストした際、Ubuntuとは異なり、`nvidia-smi`コマンドおよび`nvidia-persistenced`パッケージがNVIDIAグラフィックドライバにデフォルトで含まれていないため、`xorg-x11-drv-nvidia-cuda`パッケージを追加インストールする必要がありました。RHELおよびCentosでは直接テストしていませんが、Fedoraとシステム構成が非常に似ているため、もし以下のガイドに従って進めた際に問題が発生した場合は、同じ方法を試してみるのが役立つかもしれません。
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
次に、コンテナエンジンとしてDocker CEまたはPodmanをインストールします。使用環境と好みに合わせて、どちらか一方を選択してインストールすれば良く、[Docker公式ドキュメント](https://docs.docker.com/engine/install/)と[Podman公式ドキュメント](https://podman.io/docs/installation)を参照してください。

次の表は、DockerとPodmanの主な違いと長所短所をまとめたものです。

| 比較項目 | Docker | Podman |
| --- | --- | --- |
| アーキテクチャ | クライアント-サーバーモデル、デーモン（daemon）ベース | デーモンレス（daemonless）構造 |
| セキュリティ | 基本的にroot権限で実行されるデーモンに<br>依存するため、潜在的なセキュリティ上のリスクが存在<br>（2020年に発表されたバージョン20.10からルートレス<br>モードをサポートしていますが、追加の設定が必要） | デーモンに依存しないため、特に指定しない限り<br>基本的にルートレスで動作し、<br>SELinuxで保護される |
| リソース使用量 | デーモンベースの構造の特性上、バックグラウンドプロセスが<br>常時動作するため、一般的により多くの<br>リソースを使用 | 一般的により少ないリソースオーバーヘッド |
| コンテナ起動時間 | 比較的遅い | 簡素化されたアーキテクチャにより最大50%程度<br>速く実行される |
| エコシステムとドキュメント | 広範なエコシステムとコミュニティサポート、<br>豊富な関連ドキュメント | 比較的小規模のエコシステムと関連ドキュメント |
| ネットワーキング | Docker Bridge Networkを使用 | CNI（Container Network Interface）<br>プラグインを使用 |
| Kubernetes YAML<br>ネイティブサポート | X（変換が必要） | O |

参考資料：
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Dockerはその歴史がより長く、業界で事実上の標準的地位を享受してきたため、幅広いエコシステムと豊富な関連ドキュメントが存在することが最大の利点です。
Podmanは Red Hatによって比較的最近開発され、生まれながらにしてデーモンレス（daemonless）、ルートレス（rootless）を志向する発展した構造であるため、セキュリティ、システムリソース使用量およびコンテナ起動時間など様々な面で利点を持ちます。デーモンに問題が生じてダウンすると全てのコンテナが一緒にダウンするDockerとは異なり、各コンテナが完全に独立しているため特定のコンテナのダウンが他のコンテナに影響を与えないという点もPodmanの強みです。

それぞれの与えられた条件に合わせて使用するツールを選択することが何よりも重要であり、初めて入門する個人ユーザーであればPodmanで始めるのが良い選択かもしれません。Dockerに比べて相対的にエコシステムの規模が小さいと言われていますが、上述した様々な利点のおかげで急速に成長しており格差を縮めています。また、Dockerfile文法やDockerイメージ、CLI（コマンドラインインターフェース）など多くの部分で既存のDockerと互換性があるため、個人や小規模団体の立場ではそれほど問題にならないでしょう。

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
##### 3-Ubuntu-1. パッケージの競合を防ぐための以前のバージョンまたは非公式パッケージの削除
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. リポジトリの設定
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
non-rootユーザーも`sudo`なしでDockerを管理できるようにするには、`Docker`グループを作成した後、Dockerを使用したいユーザーを登録すれば良いです。ターミナルで次のコマンドを実行します。
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
その後、ログアウトしてから再度ログインすると、変更された設定が適用されます。UbuntuまたはDebianの場合、特別な作業なしでもシステム起動時ごとにDockerサービスが自動的に実行されます。

#### Fedoraの場合
##### 3-Fedora-1. パッケージの競合を防ぐための以前のバージョンまたは非公式パッケージの削除
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

##### 3-Fedora-2. リポジトリの設定
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. パッケージのインストール
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
パッケージのインストール過程でGPGキーを承認するかどうかの通知が表示されます。GPGキーが`060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`と一致する場合、yを入力して承認してください。
> GPGキーが一致しない場合、サプライチェーン攻撃によって偽造されたパッケージをダウンロードした可能性があるため、インストールを中止する必要があります。
{: .prompt-danger }

##### 3-Fedora-4. Dockerデーモンの起動
これでDockerがインストールされましたが、実行されていない状態です。次のコマンドを入力してDockerを実行できます。
```bash
sudo systemctl start docker
```
システム起動時にDockerサービスが自動的に実行されるようにするには、次のコマンドを実行します。
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. `Docker`グループにユーザーを登録する
non-rootユーザーもDockerを管理できるようにするには、`Docker`グループにDockerを使用したいユーザーを登録します。Fedoraの場合、先のパッケージインストール過程で`Docker`グループを自動的に作成するため、ユーザー登録のみ行えば良いです。
```bash
sudo usermod -aG docker $USER
```
その後、ログアウトしてから再度ログインすると、変更された設定が適用されます。

#### 正常に設定されたかどうかの確認
ターミナルで次のコマンドを実行してみます。
```bash
docker run hello-world
```
以下のようなメッセージが出力されれば成功です。

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

## さらなる読み物
[パート2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)に続きます
