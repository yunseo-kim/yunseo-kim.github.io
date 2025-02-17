---
title: NVIDIA Container ToolkitとDocker/Podmanでディープラーニング開発環境を構築する (2) - GPU活用のためのコンテナランタイム構成、Dockerfileの作成とコンテナイメージのビルド
description: このシリーズでは、ローカルにNVIDIA Container Toolkitでコンテナベースのディープラーニング開発環境を構築し、リモートサーバーとして活用できるようSSHとJupyter Labを設定する方法を扱います。この投稿はシリーズの2番目の記事で、Dockerfileを作成しコンテナイメージをビルドするプロセスを扱います。
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## 概要
このシリーズでは、NVIDIA Container ToolkitとDockerまたはPodmanをインストールし、Docker Hubの[nvidia/cudaリポジトリ](https://hub.docker.com/r/nvidia/cuda)が提供するCUDAおよびcuDNNイメージをベースにDockerfileを作成してディープラーニング開発環境を構築するプロセスを扱います。必要な方が自由に使用できるよう、このプロセスを経て完成した[Dockerfile](https://github.com/yunseo-kim/dl-env-docker)と[イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags)をGitHubとDocker Hubを通じて共有し、さらにリモートサーバーとして活用するためのSSHおよびJupyter Lab設定ガイドを提供します。  
シリーズは3つの記事で構成される予定で、この記事はそのシリーズの2番目の記事です。
- [第1回：NVIDIA Container Toolkit & コンテナエンジンのインストール](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 第2回：GPU活用のためのコンテナランタイム構成、Dockerfileの作成とコンテナイメージのビルド（本文）
- 第3回（アップロード予定）

x86_64 Linux環境でCUDAをサポートするNVIDIAグラフィックカードを搭載したシステムを前提に進めます。UbuntuまたはFedora以外のディストリビューションでは直接テストしていないため、いくつかの細部は若干異なる可能性があります。  
（2025.02.18. 内容更新）

> **エラー修正のお知らせ**  
> 2024年8月にアップロードしたこの記事の初稿で[Dockerfileの作成](#5-dockerfileの作成)部分の記述および該当Dockerfileからビルドしたイメージに一部エラーがありました。問題があった部分は以下の通りです：
> - remoteアカウント作成部分でパスワードを設定する部分が間違っており、本来なら"000000"をパスワードとして入力してログインできるはずですが、そうなっていませんでした
> - コンテナ起動時にSSHデーモンが自動実行されません
>
> 上記の問題点を最近認識し、韓国時間（UTC+9）基準2025年2月16日午前2時頃、問題があったDockerfileとDockerイメージを問題を解決したファイルに[GitHubリポジトリ](https://github.com/yunseo-kim/dl-env-docker)と[Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags)で置き換えました。  
> 該当日時以前にDockerfileまたはDockerイメージをPullした場合は、修正されたバージョンに置き換えてください。  
> 既にこの記事を参考にされた方々の中で、誤った内容で混乱を経験された方がいらっしゃれば申し訳ありません。
{: .prompt-info }

## 始める前に
この記事は[第1回](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)からの続きですので、まだ読んでいない場合は、まず前の記事から読むことをお勧めします。

## 4. コンテナランタイムの構成
### Podmanを使用する場合
[CDI（Container Device Interface）を活用して構成します。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

次のコマンドを実行してCDI仕様ファイルを `/etc/cdi`{: .filepath} ディレクトリに生成します。
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> グラフィックカードデバイスを変更したり、CUDAドライバー構成を変更（バージョンアップグレードを含む）する場合、CDI仕様ファイルを新たに生成する必要があります。
{: .prompt-warning }

> NVIDIA Container Runtime hookをCDIと一緒に使用すると衝突する可能性があるため、もし `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} が存在する場合は、該当ファイルを削除するか、または `NVIDIA_VISIBLE_DEVICES` 環境変数が設定された状態でコンテナを実行しないよう注意してください。
{: .prompt-warning }

### Dockerを使用する場合
[ルートレス（rootless）モード](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode)を基準に説明します。

#### 4-Docker-1. `nvidia-ctk` コマンドでコンテナランタイム設定を構成
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
上記のコマンドは、DockerがNVIDIA Container Runtimeを活用できるように `/etc/docker/daemon.json`{: .filepath} ファイルを修正します。

#### 4-Docker-2. Dockerデーモンの再起動
変更した設定を適用するためにDockerデーモンを再起動します。
```bash
systemctl --user restart docker
```

#### 4-Docker-3. `sudo nvidia-ctk` コマンドで `/etc/nvidia-container-runtime/config.toml`{: .filepath} 設定ファイルを構成
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### 正常に構成されたか確認
サンプルCUDAコンテナを実行してみます。

Podmanを使用する場合は次のコマンドを実行します。
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Dockerを使用する場合は次のコマンドを実行します。
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
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

- 必要とするCUDAおよびcuDNNバージョン、Linuxディストリビューションの種類およびバージョンなどを考慮して使用するイメージを決定する必要があります。
- ![PyTorch 2.4.0がサポートするCUDAバージョン](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)この記事の作成時点である2024年8月末を基準に、PyTorch最新バージョンである2.4.0バージョンはCUDA 12.4をサポートしています。したがって、ここでは[12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)イメージを使用します。[PyTorchホームページ](https://pytorch.org/get-started/locally/)でPyTorch最新バージョンおよびサポートするCUDAバージョンを確認できます。

完成したDockerfileのソースは[yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHubリポジトリに公開しています。以下に該当Dockerfileを作成したプロセスを段階的に説明します。

### 5-1. ベースイメージの指定
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. 基本ユーティリティおよびPython prerequisitesのインストール
```Dockerfile
# Install basic utilities and Python-related packages, gosu, and SSH server
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    apt-utils \
    curl \
    gosu \
    openssh-server \
    python3 \
    python-is-python3 \
    python3-pip \
    ssh \
    tmux \
    && rm -rf /var/lib/apt/lists/* \
# verify that the binary works
    && gosu nobody true
```

### 5-3. システムタイムゾーンの設定（この記事では'Asia/Seoul'で進行）
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. リモートアクセスのためのSSHサーバー設定  
セキュリティのため、SSHリモートアクセス時にrootアカウントログインが不可能になるよう設定します。
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

SSHアクセス時に使用する'remote'という名前のnon-rootユーザーを作成します。
```Dockerfile
# Create remote user (password can be passed to --build-arg at build time)
#
# This default password is very weak. Make sure to change it to your own unique
# password string!
#
# This Dockerfile assumes that the built image will only be used by yourself or
# a small group of trusted insiders, and if you need to distribute the image
# without exposing sensitive information, using --build-arg is dangerous.
# See the official Docker documentation.
ARG USER_NAME="remote"
ARG USER_PASSWORD="000000"
ARG HOME_DIR="/home/$USER_NAME"
RUN useradd --create-home --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && echo "$USER_NAME:$USER_PASSWORD" | chpasswd
```

> このDockerfileを利用してDockerイメージをビルドする際、別途オプションを指定しない場合、'remote'ユーザーのアカウントパスワードの初期値は000000です。これはセキュリティ上非常に脆弱なので、Dockerイメージビルド時に `--build-arg` オプションを利用してアカウントログインパスワードを別途指定するか、またはコンテナを初めて実行した後、直ちに設定を変更するようにしましょう。セキュリティのためには、SSHアクセス時にパスワードログインを無効化し、別途のキーファイルを通じてのみログインが可能になるよう後で設定することが望ましく、Yubikeyなどのハードウェアキーまで活用すれば理想的です。
> SSHサーバー構成については、このシリーズの次回で多少扱う予定ですが、より詳しく知りたい場合は、次のリストにある文書を参考にするとよいでしょう。
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> また、このDockerfileはビルドしたイメージを個人または信頼できる少数の内部者のみが使用することを想定しており、もしビルドしたイメージを外部に配布する必要がある場合、`--build-arg`を通じたパスワード設定は危険なので、他の方法を使用する必要があります。[この文書](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/)を参考にしてください。
{: .prompt-danger }

### 5-5. setuptools、pipのインストールおよびPATH環境変数の登録
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. 開発環境で使用する機械学習およびディープラーニングパッケージのインストール
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Cupy、cuDF、cuML、そしてDALIを使用する場合は、次の内容もDockerfileに追加します。
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. 作業スペースとして使用するディレクトリの作成
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. ポートの開放およびコンテナ起動時に実行する `ENTRYPOINT` の設定
SSHとJupyter Labアクセスのために22、8888ポートを開放します。  
また、コンテナ起動時にSSHデーモンを自動実行するにはroot権限が必要なので、次の方法を使用します。
1. コンテナ起動時にrootアカウントでログインされた状態
2. コンテナ起動直後に `/entrypoint.sh`{: .filepath} スクリプトを実行
3. 該当スクリプトでSSHサービスを開始した後、[`gosu`](https://github.com/tianon/gosu)を使用してremoteアカウントに切り替え
4. コンテナ実行時に別途指定したコマンドがない場合、デフォルト値としてJupyter Labをremoteアカウント（non-root権限）で実行

> 一般的に、DockerやPodmanコンテナ内での `sudo` または `su` の使用は推奨されず、root権限が必要な場合は、ここで説明しているように、まずrootアカウントでコンテナを起動し、root権限が必要な作業を実行した後に[`gosu`](https://github.com/tianon/gosu)を使用してnon-rootユーザーに切り替えることが良いです。このようにする理由は、以下の資料に詳しく説明されているので、必要な場合は参考にすると役立つでしょう。
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

まず、Dockerfileの最後の部分に次の内容を入力します。
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

次に、作成したDockerfileと同じパスに `entrypoint.sh`{: .filepath} という名前でスクリプトファイルを作成し、内容は以下のように作成します。
```sh
#!/bin/bash
set -e

# Run SSH daemon in the background
service ssh start

# Move to the workspace directory and run Jupyter Lab
cd "$WORK_DIR"
if [ $# -gt 0 ];then
    #su ${USER_NAME} -c "exec $@"
    exec gosu ${USER_NAME} $@
else
    #su ${USER_NAME} -c "exec jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}""
    exec gosu ${USER_NAME} jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="${WORK_DIR}"
fi
```

## 6. Dockerイメージのビルドとコンテナの実行
### 6-1. イメージのビルド
Dockerfileが位置するディレクトリでターミナルを開き、以下のコマンドを実行します。
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> \<password\> の部分にSSHアクセス時に使用するログインパスワードを入力すれば良いです。
{: .prompt-info }

### 6-2. サンプルワークロードの実行
ビルドを完了したら、使い捨てコンテナを実行して正常に動作するか確認します。

Podmanの場合は次のコマンドを実行します。
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Dockerの場合は次のコマンドを実行します。
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

ターミナルで上記のコマンドを入力すると、先ほどビルドした `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` イメージから `test-container` という名前のコンテナを実行した後、ホストシステムの22番ポートと該当コンテナの22番ポート、ホストシステムの88番ポートとコンテナの8888番ポートをそれぞれ接続します。前の段階でDockerイメージが正常にビルドされ、コンテナが問題なく起動された場合、`test-container` コンテナ内でJupyterLabがデフォルト値である `http:127.0.0.1:8888` アドレスで実行中のはずです。したがって、Docker Engineが動作しているホストシステムでブラウザを開き、<http://127.0.0.1:88>にアクセスした時、コンテナ内部の `http://127.0.0.1:8888` アドレスに接続され、以下のような画面が表示されるはずです。

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

ホストシステムでターミナルを開き、`ssh remote@127.0.0.1` コマンドを実行して、コンテナ内部で実行中のUbuntuシステムのremoteアカウントにリモートログインしてみましょう。  
初めてログインする際は、接続対象の暗号キーに関する情報がなく、認証が不可能だという警告が出力され、接続を続行するかどうか尋ねられますが、"yes"を入力して続行すれば良いです。  
その後、ログインのためにパスワード（イメージビルド時に別途変更していなければデフォルト値である"000000"のはずです）を入力します。
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {フィンガープリント（各キーごとに異なる固有の値を持つ）}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '127.0.0.1' (ED25519) to the list of known hosts.
remote@127.0.0.1's password: 
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 6.12.11-200.fc41.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

```
おおよそ上記のように出力されれば、SSHを通じたリモートログインに成功したことになります。接続を終了する際は `exit` コマンドを入力すれば良いです。

### 6-3. （オプション）Docker Hubにプッシュする
前述のプロセスを経て作成した開発環境イメージを必要な時にいつでもPullして活用するには、ビルドしたイメージをDocker Hubにプッシュしておくのが良いでしょう。

> Docker Hubに自分のイメージをプッシュするには自分のDockerアカウントが必要なので、まだない場合は<https://app.docker.com/signup>で会員登録を先に完了してください。
{: .prompt-tip }

#### 6-3-1. Docker Hubにログイン
##### Podmanの場合
```bash
podman login docker.io
```

##### Dockerの場合
```bash
docker login
```

#### 6-3-2. イメージタグの指定
`<dockerhub_username>`と`<repository_name>`、（オプション）`:TAG`部分には自分に該当する内容を入力すれば良いです。  
例：「yunseokim」、「dl-env」、「rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04」

##### Podmanの場合
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Dockerの場合
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. イメージのプッシュ
最後に、以下のコマンドを実行して該当イメージをDocker Hubにプッシュします。

##### Podmanの場合
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Dockerの場合
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
<https://hub.docker.com/>で以下のように正常にプッシュされたことを確認できます。  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

前述のプロセスを経て完成したイメージはDocker Hubの[yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags)公開リポジトリに公開しており、誰でも自由に使用できます。

イメージをPullするには、先ほどプッシュする際に使用したコマンドで `push` 部分だけ `pull` に変えて実行すれば良いです。
