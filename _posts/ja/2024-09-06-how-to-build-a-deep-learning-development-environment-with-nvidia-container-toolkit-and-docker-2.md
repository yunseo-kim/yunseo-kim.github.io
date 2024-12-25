---
title: NVIDIA Container ToolkitとDockerでディープラーニング開発環境を構築する (2) - GPUを活用するためのコンテナランタイムの構成、Dockerfileの作成およびDockerイメージのビルド
description: このシリーズでは、ローカルにNVIDIA Container ToolkitとDockerベースのディープラーニング開発環境を構築し、リモートサーバーとして活用できるようにSSHおよびJupyter
  Labを設定する方法を扱います。この投稿は、そのシリーズの2番目の記事で、GPUを活用するためのコンテナランタイムの構成、Dockerfileの作成、およびDockerイメージのビルド方法を紹介します。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## 概要
このシリーズでは、NVIDIA Container ToolkitとDockerをインストールし、Docker Hubの[nvidia/cudaリポジトリ](https://hub.docker.com/r/nvidia/cuda)が提供するCUDAおよびcuDNNイメージをベースにDockerfileを作成してディープラーニング開発環境を構築するプロセスを扱います。必要な方が自由に使用できるように、このプロセスを経て完成した[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)と[イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags)をGitHubとDocker Hubを通じて共有し、さらにリモートサーバーとして活用するためのSSHおよびJupyter Lab設定ガイドを提供します。  
シリーズは3つの記事で構成される予定で、この記事はそのシリーズの2番目の記事です。
- [第1回：NVIDIA Container Toolkit & Docker Engineのインストール](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 第2回：GPUを活用するためのコンテナランタイムの構成、Dockerfileの作成およびDockerイメージのビルド（本文）
- 第3回（アップロード予定）

x86_64 Linux環境でCUDAをサポートするNVIDIAグラフィックカードを搭載したシステムを前提に進めます。UbuntuまたはFedora以外のディストリビューションでは直接テストしていないため、いくつかの細部は若干異なる可能性があります。

## 始める前に
この記事は[第1回](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)に続く記事なので、まだ読んでいない場合は、まず前の記事から読むことをお勧めします。

## 4. コンテナランタイムの構成
### 4-1. `nvidia-ctk`コマンドの実行
```bash
sudo nvidia-ctk runtime configure --runtime=docker
```
上記のコマンドは、DockerがNVIDIA Container Runtimeを利用できるように`/etc/docker/daemon.json`{: .filepath}ファイルを修正します。

### 4-2. Dockerデーモンの再起動
変更した設定を適用するためにDockerデーモンを再起動します。
```bash
sudo systemctl restart docker
```

### 4-3. 正常に構成されたかの確認
サンプルCUDAコンテナを実行してみます。
```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
おおよそ以下のような画面が表示されれば成功です。

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

## 5. Dockerfileの作成
Docker Hubの[nvidia/cudaリポジトリ](https://hub.docker.com/r/nvidia/cuda)が提供するCUDAおよびcuDNNイメージをベースにして、開発環境として使用するDockerfileを作成します。

- 必要とするCUDAおよびcuDNNのバージョン、Linuxディストリビューションの種類およびバージョンなどを考慮して使用するイメージを決定する必要があります。
- ![PyTorch 2.4.0がサポートするCUDAバージョン](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)この記事の作成時点である2024年8月末を基準に、PyTorch最新バージョンである2.4.0バージョンはCUDA 12.4をサポートしています。したがって、ここでは[12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)イメージを使用します。[PyTorchホームページ](https://pytorch.org/get-started/locally/)でPyTorch最新バージョンおよびサポートするCUDAバージョンを確認できます。

完成したDockerfileのソースは[yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHubリポジトリに公開しています。以下に、そのDockerfileを作成したプロセスを段階的に説明します。

### 5-1. ベースイメージの指定
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. 基本ユーティリティおよびPython prerequisitesのインストール
```Dockerfile
RUN apt-get update -y && apt-get install -y --no-install-recommends\
    apt-utils \
    ssh \
    curl \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*
```

### 5-3. システムタイムゾーンの設定（この記事では'Asia/Seoul'で進行）
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. リモートアクセスのためのSSHサーバー設定  
セキュリティのため、SSHリモートアクセス時にパスワードでrootアカウントログインができないように設定します。
```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```
コンテナ起動時にSSHサービスが自動的に開始されるように構成します。
```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```
SSH接続時に使用する'remote'という名前のnon-rootユーザーを作成します。
```Dockerfile
# Create a non-root user and switch to it
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
RUN useradd --create-home --password $USER_PASSWORD $USER_NAME
ENV HOME=/home/$USER_NAME
USER $USER_NAME
WORKDIR $HOME
# Re-run ssh when the container restarts.
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
# Create a workspace directory to locate jupyter notebooks and .py files
RUN mkdir -p $HOME/workspace
```

> このDockerfileを使用してDockerイメージをビルドする際、別途オプションを指定しない場合、'remote'ユーザーのアカウントパスワードの初期値は000000です。これはセキュリティ上非常に脆弱なので、Dockerイメージビルド時に`--build-arg`オプションを使用してアカウントログインパスワードを別途指定するか、またはコンテナを初めて実行した後、すぐに設定を変更するようにしましょう。セキュリティのためには、SSH接続時にパスワードログインを無効にし、別途のキーファイルを通じてのみログインが可能になるように後で設定することが望ましく、Yubikeyなどのハードウェアキーまで活用すれば理想的です。
> SSHサーバーの構成については、このシリーズの次回で多少扱う予定ですが、より詳しく知りたい場合は、次のリストにある文書を参考にするとよいでしょう。
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. setuptools、pipのインストールおよびPATH環境変数の登録
```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. 開発環境で使用する機械学習およびディープラーニングパッケージのインストール
```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
Cupy、cuDF、cuML、そしてDALIを使用する場合は、次の内容もDockerfileに追加します。
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. コンテナ起動時のJupyterLab実行設定
```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
```

## 6. Dockerイメージのビルドおよびコンテナの実行
### 6-1. イメージのビルド
Dockerfileが位置するディレクトリでターミナルを開き、以下のコマンドを実行します。
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> \<password\>の部分にSSH接続時に使用するログインパスワードを入力します。
{: .prompt-info }

### 6-2. サンプルワークロードの実行
ビルドが完了したら、次のコマンドで使い捨てコンテナを実行して正常に動作するか確認します。
```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```
ターミナルで上記のコマンドを入力すると、先ほどビルドした`dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04`イメージから`test-container`という名前のコンテナを実行し、ホストシステムの88番ポートを該当コンテナの8888番ポートに接続します。前の段階でDockerイメージが正常にビルドされ、コンテナが問題なく起動された場合、`test-container`コンテナ内でJupyterLabがデフォルト値である`http:127.0.0.1:8888`アドレスで実行中のはずです。したがって、Docker Engineが動作しているホストシステムでブラウザを開き、<http://127.0.0.1:88>にアクセスした時、コンテナ内部の`http://127.0.0.1:8888`アドレスに接続され、以下のような画面が表示されるはずです。

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (オプション) Docker Hubへのプッシュ
前述のプロセスを経て作成した開発環境イメージを必要な時にいつでもPullして活用するには、ビルドしたイメージをDocker Hubにプッシュしておくのが良いでしょう。

> Docker Hubに自分のイメージをプッシュするには自分のDockerアカウントが必要なので、まだない場合は<https://app.docker.com/signup>で会員登録を先に完了してください。
{: .prompt-tip }

まず、以下のコマンドでDocker Hubにログインします。
```bash
docker login
```
次に、以下のような形式のコマンドを実行してイメージタグを生成します。
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```
最後に、以下のコマンドを実行して該当イメージをDocker Hubにプッシュします。
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
<https://hub.docker.com/>で以下のようにうまくプッシュされたことを確認できます。  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

前述のプロセスを経て完成したイメージはDocker Hubの[yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags)公開リポジトリに公開しており、誰でも自由に使用できます。
