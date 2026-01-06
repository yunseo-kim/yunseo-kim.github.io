---
title: "NVIDIA Container ToolkitとDocker/Podmanでディープラーニング開発環境を構築する (2) - GPU活用のためのコンテナランタイム構成、Dockerfile作成およびコンテナイメージのビルド"
description: "このシリーズでは、ローカルにNVIDIA Container Toolkitでコンテナベースのディープラーニング開発環境を構築し、リモートサーバとして使えるようにSSHとJupyterLabを設定する方法を解説する。本記事は第2回として、Dockerfileの作成とコンテナイメージのビルド手順を扱う。"
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## 概要

このシリーズでは、NVIDIA Container ToolkitとDockerまたはPodmanをインストールし、Docker Hubの [nvidia/cuda リポジトリ](https://hub.docker.com/r/nvidia/cuda) が提供するCUDAおよびcuDNNイメージをベースにDockerfileを作成して、ディープラーニング開発環境を構築する流れを扱う。必要な人が自由に使えるよう、この工程を経て完成させた [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) と [イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags) をGitHubとDocker Hubで共有し、加えてリモートサーバとして利用するためのSSHおよびJupyterLab設定ガイドも提供する。  
シリーズは全3本の予定で、読んでいるこの記事はその第2回である。
- [第1回: NVIDIA Container Toolkit & コンテナエンジンのインストール](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 第2回: GPU活用のためのコンテナランタイム構成、Dockerfile作成およびコンテナイメージのビルド（本文）
- 第3回（アップロード予定）

x86_64のLinux環境で、CUDAをサポートするNVIDIAグラフィックカードを搭載したシステムであることを前提に進める。UbuntuまたはFedora以外のディストリビューションでは直接テストしていないため、いくつかの細部は多少異なる可能性がある。  
（12026.1.6. 改訂）

> **誤りの訂正について**
>
> 12024年8月にアップロードした本記事の初稿では、[Dockerfile作成](#5-dockerfile-作成) の記述および当該Dockerfileからビルドしたイメージに一部誤りがあった。問題のあった箇所は次のとおり。
> - remoteアカウント作成部分のパスワード設定が誤っており、「000000」を初期パスワードとして入力すればログインできると記述したが、実際にはそうではなかった（12025.12.19 追記: 現在は初期パスワードが「000000」ではないため、必ず [下の本文](#5-4-リモート接続のためのsshサーバ設定) を確認すること）
> - コンテナ起動時にSSHデーモンが自動起動しない
>
> 上記の問題点を12025年2月に把握し、韓国時間(UTC+9)基準で12025年2月16日午前2時頃、問題のあったDockerfileとDockerイメージを、修正したファイルに置き換えて [GitHubリポジトリ](https://github.com/yunseo-kim/dl-env-docker) と [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) に差し替えておいた。  
> 当該時刻以前にDockerfileまたはDockerイメージをPullしている場合は、修正版に置き換えてほしい。  
> 既に本記事を参考にした方の中で、誤った内容により混乱を招いた方がいる場合はお詫びする。
{: .prompt-info }

## 始める前に

この記事は[第1回](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)の続きなので、まだ読んでいない場合は先に前の記事から読むことを推奨する。

## 4. コンテナランタイムの構成

### Podmanを使う場合

[CDI（Container Device Interface）を活用して構成する。](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> 旧バージョンでは、NVIDIA Container Toolkitの初回インストール時、およびその後にグラフィックカードデバイスやドライバ構成を変更（バージョンアップを含む）するたびに、毎回CDI仕様ファイルを手動で再生成する必要があった。
>
> しかしNVIDIA Container Toolkit `v1.18.0` からは、`nvidia-cdi-refresh` systemdサービスを通じて、以下の場合に `/var/run/cdi/nvidia.yaml` CDI仕様ファイルを自動生成・更新する。
> - NVIDIA Container Toolkitのインストールまたはアップグレード時
> - NVIDIA GPUドライバのインストールまたはアップグレード時
> - システム再起動時
>
> したがって、以前と違って今は特に何かを別途行う必要はない。これを反映して本文を修正した。
>
> ただし、GPUドライバの削除またはMIGデバイス再構成時には `nvidia-cdi-refresh` が対応できないため、手動で `nvidia-cdi-refresh.service` を再起動してCDI仕様の再生成を促す必要がある。
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> NVIDIA Container Runtime hookをCDIと併用すると衝突する可能性があるため、もし `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} が存在するなら当該ファイルを削除するか、あるいは `NVIDIA_VISIBLE_DEVICES` 環境変数を設定した状態でコンテナを起動しないよう注意する。
{: .prompt-warning }

### Dockerを使う場合

[ルートレス（rootless）モード](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode)を前提に説明する。

#### 4-Docker-1. `nvidia-ctk` コマンドでコンテナランタイム設定を構成

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

上のコマンドは、DockerがNVIDIA Container Runtimeを利用できるよう `/etc/docker/daemon.json`{: .filepath} ファイルを修正する。

#### 4-Docker-2. Dockerデーモンの再起動

変更した設定を適用するためDockerデーモンを再起動する。

```bash
systemctl --user restart docker
```

#### 4-Docker-3. `sudo nvidia-ctk` コマンドで `/etc/nvidia-container-runtime/config.toml`{: .filepath} 設定ファイルを構成

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### 正常に構成できたか確認

サンプルCUDAコンテナを実行してみる。

Podmanを使う場合は次のコマンドを実行する。

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Dockerを使う場合は次のコマンドを実行する。

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

概ね以下のような画面が表示されれば成功である。

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

## 5. Dockerfile作成

Docker Hubの [nvidia/cuda リポジトリ](https://hub.docker.com/r/nvidia/cuda) が提供するCUDAおよびcuDNNイメージをベースに、開発環境として使うDockerfileを作成する。

- 必要なCUDAおよびcuDNNのバージョン、Linuxディストリビューションの種類とバージョンなどを考慮して、使用するイメージを決める必要がある。 
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  本記事の執筆時点である12024年8月末を基準に、PyTorch最新の2.4.0はCUDA 12.4をサポートする。よってここでは [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) イメージを使用する。[PyTorch公式サイト](https://pytorch.org/get-started/locally/)でPyTorchの最新バージョンおよび対応CUDAバージョンを確認できる。

完成したDockerfileのソースは、[yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHubリポジトリで公開してある。以下では、そのDockerfileを作成した過程を段階的に説明する。

> (+ 12026.1.6. 改訂)  
> PyTorch 2.9.1とCUDA 12.8 / 13.0をサポートするDockerfileおよびイメージを、同じGitHubリポジトリと [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) Docker Hub公開リポジトリに追加した。本文内容もPyTorch 2.9.1、CUDA 13.0に合わせて更新した。
>
> また、scikit-imageとXGBoost、さらにRAPIDSエコシステム内のcuGraph、cuxfilter、cuCIM、RAFT、cuVSライブラリをイメージに含め、既存の `amd64` アーキテクチャに加えて `arm64` 対応も追加した。
{: .prompt-info }

### 5-1. baseイメージの指定

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. システムのタイムゾーン設定（本記事では「Asia/Seoul」で進める）

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> 主に[この記事](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22)を参考にした。
{: .prompt-tip }

### 5-3. 基本システムユーティリティのインストール

```Dockerfile
# Install basic utilities, gosu, and SSH server
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update -y && apt-get install -y --no-install-recommends \
        apt-utils \
        curl \
        gosu \
        openssh-server \
        ssh \
        tmux \
        tzdata \
# verify that the binary works
    && gosu nobody true
```

### 5-4. リモート接続のためのSSHサーバ設定

セキュリティのため、SSHリモート接続でrootアカウントによるログインをできないように設定する。

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

SSH接続に使用する「remote」という名前のnon-rootユーザを作成する。

```Dockerfile
# Create remote user
#
# The password must be pre-specified at build time with the `DL_ENV_PASSWD`
# environment variable.
ARG USER_NAME="remote"
ARG USER_UID=1001
ARG USER_GID=$USER_UID
ARG HOME_DIR="/home/$USER_NAME"
RUN --mount=type=secret,id=USER_PASSWORD \
    groupadd --gid $USER_GID $USER_NAME && \
    useradd --uid $USER_UID --gid $USER_GID --create-home \
        --home-dir $HOME_DIR --shell /bin/bash $USER_NAME \
    && awk -v user="$USER_NAME" '{print user ":" $0}' /run/secrets/USER_PASSWORD | chpasswd
```

> ビルド引数（`ARG`）や環境変数（`ENV`）の内容は、ビルドしたイメージにそのまま露出するため、[パスワードやAPIキーのような機密情報を指定する場合は別の方法を使うべきである](https://docs.docker.com/build/building/secrets/)。ここでは [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts) を使用した。
{: .prompt-danger }

> [後述するが](#6-1-イメージ-ビルド)、このDockerfileでイメージをビルドする際は `DL_ENV_PASSWD` 環境変数でユーザアカウントのパスワードとして使う文字列を指定する必要がある。[Docker Hub配布イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags) の場合、アカウントの初期パスワードは `satisfied-flip-remake` であり、この公開されたデフォルトパスワードをそのまま使うのはセキュリティ上非常に脆弱なので、コンテナ初回起動後ただちに設定を変更しよう。さらにセキュリティ面では、SSH接続時のパスワードログインを無効化し、鍵ファイルでのみログイン可能にするよう後で設定するのが望ましい。Yubikeyのようなハードウェアキーまで活用できれば理想的である。
>
> SSHサーバ構成については本シリーズの次回である程度扱う予定で、より詳しく知りたい場合は以下の文書も参考になる。
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. uvのインストールと環境変数の登録

> **[PEP 668](https://peps.python.org/pep-0668/)に基づく[Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/)仕様の反映とuv導入（12026.1.6. 改訂）**
>
> 以前の本記事では、別の仮想環境（`venv`）を作らず、コンテナイメージ内で直接 `pip` によるパッケージインストールを行うようDockerfileを書いていた。そうした理由は、単一目的のコンテナイメージ内ではシステムソフトウェアが壊れるリスクが低く、仮に問題が起きてもイメージから新しいコンテナを作り直せばよいので、わざわざ仮想環境を作る必要性が低いという判断によるものだった。この点は[PEP 668](https://peps.python.org/pep-0668/#use-cases)でも次のように部分的に認められている。
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> しかし、単一目的コンテナイメージ内であっても、`pip` のようなPythonパッケージマネージャによるインストールは仮想環境内でのみ行い、OSパッケージマネージャ等によって外部管理（externally managed）されるパッケージ群とは厳密に区別することが標準として確立された。これに合わせて、仮想環境を作成し、その中に必要パッケージを入れるよう本文を改訂し、[PEP 668](https://peps.python.org/pep-0668/)およびそれに基づく[Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/)仕様に準拠し、Pythonエコシステム標準に従うようにした。
>
> Pythonで仮想環境の作成・管理に公式対応する標準ライブラリは、[12021年初頭に書いた別記事でも一度紹介したとおり](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended) `venv` である。しかし [Astral](https://astral.sh/) がRustで開発した高性能なPythonパッケージ／プロジェクトマネージャ [`uv`](https://docs.astral.sh/uv/) が12024年に初公開されて以降、次のような大きな利点によりPythonエコシステムで急速に新たな事実上の標準として定着した。
> - [`pip`に比べ圧倒的な依存解決およびパッケージインストール速度（10〜100倍）](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
> - 優れた使い勝手
> - [既存の`pip`および`venv`との高い互換性](https://docs.astral.sh/uv/pip/)
>
> 特にここで扱うPyTorchやRAPIDSなどのML分野パッケージは依存関係が多く、概ね大容量であるため、`uv`の利点が最大限に活きる。加えて[`uv`はキャッシュを積極的かつ効率的に活用するため](https://docs.astral.sh/uv/concepts/cache/)、本記事のようにコンテナイメージビルド時にcache mountを適切に使えば、利点を最大化してビルド時間を大幅に短縮できる](https://docs.astral.sh/uv/guides/integration/docker/#caching)。そこでここでも、仮想環境の作成・管理およびパッケージインストール用途として`uv`を導入する。作業は主に`uv`の公式ドキュメント「["Using uv in Docker"](https://docs.astral.sh/uv/guides/integration/docker/)」を参考にした。
{: .prompt-info }

```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_UID:$USER_GID
WORKDIR $HOME_DIR

# Install uv by copying the binary from the official distroless image
COPY --from=ghcr.io/astral-sh/uv:0.9.21 /uv /uvx /bin/
ENV PATH="$HOME_DIR/.local/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ARG UV_CACHE_DIR="/tmp/uv-cache"
```

> **`UV_CACHE_DIR`をデフォルトの `"$HOME_DIR/.cache/uv"` ではなく、ホームディレクトリ外の別パス（`"/tmp/uv-cache"`）にした理由**
>
> 本来 `useradd --create-home` でユーザを追加すると、そのユーザが自分のホームディレクトリの所有権を持つのが正常であり、ここでもそうである。
> しかしPodmanでイメージをビルドする際、前段レイヤで正常に所有権を変更していても、後段レイヤでキャッシュ等をマウントすると、親ディレクトリの所有権メタデータがデフォルト値（root所有）に再設定されるバグがあることを発見した。調べたところ、[約3週間前に同様の現象を別ユーザが報告したIssue](https://github.com/containers/podman/issues/27777)が見つかったが、現時点ではまだ返信が付いていない。私が遭遇した状況の詳細は、[当該Issueに追加コメントとして書いておいた](https://github.com/containers/podman/issues/27777#issuecomment-3712237296)。
>
> そこで、所有権がrootに再設定されても問題にならないよう、ビルド段階では `UV_CACHE_DIR` を `$HOME_DIR` とは別のパスである `"/tmp/uv-cache"` に指定した。どうせこのキャッシュはビルド成果物である最終イメージには含まれないため、パスを適切に変えても差し支えない。
{: .prompt-tip }

### 5-6. Pythonのインストール、仮想環境作成、setuptools & pipのインストール

```Dockerfile
# Install the latest, managed Python executables
ARG UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv python install 3.13 --default

# Create a virtual environment
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv venv --python 3.13 --seed
# Use the virtual environment automatically
ENV VIRTUAL_ENV=$HOME_DIR/.venv
# Place entry points in the environment at the front of the path & .profile
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN echo "source $VIRTUAL_ENV/bin/activate" >> $HOME_DIR/.profile
# Allow pip to only run in a virtual environment; exit with an error otherwise
ENV PIP_REQUIRE_VENV=true

# Install setuptools
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install setuptools
```

### 5-7. 開発環境で使用する機械学習・深層学習パッケージのインストール

#### 5-7-1. 共通パッケージ

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & CUDA専用GPUアクセラレーションライブラリ

##### PyTorchのみをインストールする場合

PyTorchのみをインストールするなら、Dockerfileに次を追加する。

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & Cupy & RAPIDS & DALI

PyTorchに加えてCupyとRAPIDS（cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS）、さらにDALIを使うなら、Dockerfileに次を追加する。

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        --index-url https://download.pytorch.org/whl/cu130 \
        --extra-index-url=https://pypi.org/simple \
        --extra-index-url=https://pypi.nvidia.com \
        "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        cupy-cuda13x \
        "cudf-cu13==25.12.*" "dask-cudf-cu13==25.12.*" "cuml-cu13==25.12.*" \
        "cugraph-cu13==25.12.*" "nx-cugraph-cu13==25.12.*" "cuxfilter-cu13==25.12.*" \
        "cucim-cu13==25.12.*" "pylibraft-cu13==25.12.*" "raft-dask-cu13==25.12.*" \
        "cuvs-cu13==25.12.*" nvidia-dali-cuda130
```

> このときPyTorchとRAPIDSパッケージは、いくつかの依存ライブラリ（cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE）を共有している。別々にインストールすると要求バージョンが異なり、先に入れたものが後から入るバージョンで上書きされて依存関係の衝突が起きる懸念が大きくなる。よって、これらのパッケージはインストールコマンドを1つの `uv pip install` に統合し、依存解決器（resolver）がすべての制約を同時に考慮できるようにし、PyTorchが要求するバージョンを優先する。
{: .prompt-tip }

### 5-8. 作業スペースとして使うディレクトリの作成

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. ポート開放と、コンテナ起動時に実行する `ENTRYPOINT` の設定
SSHとJupyter Lab接続のために22、8888ポートを開放する。  
また、コンテナ起動時にSSHデーモンを自動起動するにはroot権限が必要なので、次の方法を使う。
1. コンテナ起動時はrootアカウントでログインした状態にする
2. コンテナ起動直後に `/entrypoint.sh`{: .filepath} スクリプトを実行する
3. スクリプト内でSSHサービスを起動した後、[`gosu`](https://github.com/tianon/gosu)を使ってremoteアカウントへ切り替える
4. コンテナ実行時に別途指定したコマンドがない場合、デフォルトとしてJupyter Labをremoteアカウント（non-root権限）で実行する

> 一般にDockerやPodmanコンテナ内での `sudo` や `su` の使用は推奨されず、root権限が必要な場合は、ここで説明するようにいったんrootアカウントでコンテナを起動してroot権限が必要な作業を済ませ、その後に [`gosu`](https://github.com/tianon/gosu) を使ってnon-rootユーザへ切り替えるのが良い。そうすべき理由は以下の資料に詳しく説明されているので、必要に応じて参考にするとよい。
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

まずDockerfileの末尾に次の内容を記述する。

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

次に、作成したDockerfileと同じパスに `entrypoint.sh`{: .filepath} という名前でスクリプトファイルを作成し、内容は以下のように書く。

```sh
#!/bin/bash
set -e

# Dump environment variables
printenv | grep _ >> /etc/environment

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

> 一般にdocker execやCMDで実行されたプロセスはDockerのENVをそのまま継承するが、SSHで接続したセッションはDockerの環境変数を自動的に継承できないことが多い。SSHはログイン時に新しいシェルセッションを生成するためである。
>
> これを解決し、SSH接続時にも `$WORK_DIR` のように事前定義した環境変数へアクセスできるようにするには、コンテナ実行時にsshサービスを起動する前に `printenv | grep _ >> /etc/environment` のように環境変数をあらかじめ `/etc/environment`{: .filepath } にダンプしておく必要がある。
>
> 関連して、以下のリンクの記事も参考になる。
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. OCIイメージのビルドとコンテナ実行

### 6-1. イメージ・ビルド

Dockerfileが置かれているディレクトリでターミナルを開き、`DL_ENV_PASSWD` 環境変数を指定する。

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> \<your_own_password\> の部分に、SSH接続時に使用するログインパスワードを入力すればよい。
{: .prompt-info }

ここからは **そのターミナルウィンドウを閉じずに**、同じウィンドウで続けて次のコマンドを実行し、ビルドを行う。

#### Podmanの場合

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> Podman基準で、配布も視野に入れて自分が使っているデバイスのプラットフォーム（OS/アーキテクチャ）だけでなく、baseイメージがサポートするすべてのプラットフォーム向けにイメージをビルドするには、次のように [`--all-platforms` オプション](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms) を指定し、さらに [`--tag` や `-t` の代わりに `--manifest` オプションを使えばよい](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant)。
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> Dockerの場合はここでは別途まとめないので、必要なら[Docker公式ドキュメント](https://docs.docker.com/build/building/multi-platform/)を参照してほしい。
{: .prompt-tip }

#### Dockerの場合

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. サンプルワークロードの実行

ビルドが完了したら、使い捨てコンテナを起動して正常動作するか確認する。

Podmanの場合は次のコマンドを実行する。

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Dockerの場合は次のコマンドを実行する。
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

ターミナルで上記コマンドを入力すると、先ほどビルドした `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04` イメージから `test-container` という名前のコンテナを起動し、ホスト側の2222番ポートと当該コンテナの22番ポート、ホスト側の8888番ポートとコンテナの8888番ポートをそれぞれ接続する。前段でイメージが正常にビルドされ、コンテナも問題なく起動しているなら、`test-container` 内でJupyterLabがデフォルトの `http:127.0.0.1:8888` アドレスで実行中のはずである。したがってPodmanまたはDockerが動作しているホスト側でブラウザを開き、<http://127.0.0.1:8888> にアクセスしたときに、コンテナ内部の `http://127.0.0.1:8888` へ接続され、次のような画面が表示されるはずだ。

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

ホスト側でターミナルを開き、`ssh remote@127.0.0.1 -p 2222` コマンドを実行して、コンテナ内部で動いているUbuntuシステムのremoteアカウントにリモートログインしてみよう。  
初回ログイン時は接続先のホスト鍵情報がなく認証できないという警告が出て、接続を続けるか尋ねられるので、「yes」を入力して続行すればよい。  
その後ログインのため、ビルド時に指定したパスワード（または [Docker Hub配布イメージ](https://hub.docker.com/r/yunseokim/dl-env/tags) をpullして初回ログインする場合は、初期パスワード `satisfied-flip-remake`）を入力する。

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {フィンガープリント(鍵ごとに固有の値を持つ)}.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:2222' (ED25519) to the list of known hosts.
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
概ね上のように出力されれば、SSHによるリモートログイン成功である。切断するには `exit` コマンドを入力すればよい。

### 6-3. (optional) Docker HubへPushする

上の手順で作成した開発環境イメージを、必要なときにいつでもPullして使えるようにするには、ビルドしたイメージをDocker HubへPushしておくのがよい。  

> Docker Hubへ自分のイメージをPushするにはDockerアカウントが必要なので、まだ持っていない場合は <https://app.docker.com/signup> で先に登録を完了する。
{: .prompt-tip }

#### 6-3-1. Docker Hubへログイン

##### Podmanの場合

```bash
podman login docker.io
```

##### Dockerの場合

```bash
docker login
```

#### 6-3-2. イメージタグの指定

`<dockerhub_username>`、`<repository_name>`、（任意）`:TAG` の部分は自分に該当する内容に置き換えればよい。  
e.g. "yunseokim", "dl-env", "rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04"

> 先ほど自分のデバイスのプラットフォーム（OS/アーキテクチャ）だけでなく、baseイメージがサポートする全プラットフォーム向けにイメージをビルドしており、このmanifestリスト（あるいはimage index）をまとめてPushしたい場合は、この段階を飛ばして [イメージPush](#6-3-3-イメージ-push) へ進み、そこに書いた方法に従う。
{: .prompt-tip }

##### Podmanの場合

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Dockerの場合

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. イメージPush

最後に、次のコマンドでDocker HubへPushする。

##### Podmanの場合

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> Podman基準で、複数プラットフォームに対応する各イメージをmanifestリストまたはimage indexとしてまとめてPushするには、次のように [`podman manifest push` コマンド](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls) を使う。
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> e.g.
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### Dockerの場合

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

<https://hub.docker.com/> で、以下のように正しくPushされたことを確認できる。

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

上の手順で完成させたイメージは、Docker Hubの [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) 公開リポジトリでも公開しており、誰でも自由に利用できる。

Pullするには、先ほどPushで使ったコマンドの `push` の部分だけを `pull` に変えて実行すればよい。
