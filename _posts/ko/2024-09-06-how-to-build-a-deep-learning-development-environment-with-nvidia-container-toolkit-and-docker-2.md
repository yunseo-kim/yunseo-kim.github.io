---
title: "NVIDIA Container Toolkit과 Docker/Podman으로 딥러닝 개발환경 구축하기 (2) - GPU 활용을 위한 컨테이너 런타임 구성, Dockerfile 작성 및 컨테이너 이미지 빌드"
description: "이 시리즈는 로컬에 NVIDIA Container Toolkit으로 컨테이너 기반의 딥러닝 개발환경을 구축하고, 원격 서버로 활용할 수 있도록 SSH 및 JupyterLab을 설정하는 방법을 다룬다. 이 포스트는 해당 시리즈의 두 번째 글로, Dockerfile을 작성하고 컨테이너 이미지를 빌드하는 과정을 다룬다."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## 개요

이 시리즈에서는 NVIDIA Container Toolkit과 Docker 또는 Podman을 설치하고, Docker Hub의 [nvidia/cuda 리포지터리](https://hub.docker.com/r/nvidia/cuda)에서 제공하는 CUDA 및 cuDNN 이미지를 기반으로 Dockerfile을 작성하여 딥러닝 개발환경을 구축하는 과정을 다룬다. 필요한 분들은 자유롭게 가져다 사용할 수 있도록 이 과정을 거쳐 완성한 [Dockerfile](https://github.com/yunseo-kim/dl-env-docker)과 [이미지](https://hub.docker.com/r/yunseokim/dl-env/tags)를 GitHub와 Docker Hub를 통해 공유하며, 추가적으로 원격 서버로 활용하기 위한 SSH 및 JupyterLab 설정 가이드를 제공한다.  
시리즈는 3개의 글로 이루어질 예정이며, 읽고 있는 이 글은 해당 시리즈의 두 번째 글이다.
- [1편: NVIDIA Container Toolkit & 컨테이너 엔진 설치](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 2편: GPU 활용을 위한 컨테이너 런타임 구성, Dockerfile 작성 및 컨테이너 이미지 빌드 (본문)
- 3편 (업로드 예정)

x86_64 리눅스 환경에서 CUDA를 지원하는 NVIDIA 그래픽카드를 장착한 시스템이라고 전제하고 진행하며, Ubuntu 또는 Fedora 이외의 배포판에서는 직접 테스트해 보지 않았기에 몇몇 세부적인 부분은 약간 차이가 있을 수 있다.  
(12026.1.6. 개정)

> **오류 정정 안내**
>
> 12024년 8월에 업로드한 이 글의 초본에서 [Dockerfile 작성](#5-dockerfile-작성) 부분의 서술 및 해당 Dockerfile로부터 빌드한 이미지에 일부 오류가 있었습니다. 문제가 있던 부분은 다음과 같습니다.
> - remote 계정 생성 부분에서 비밀번호를 설정하는 부분이 잘못되었으며, "000000"을 초기 패스워드로 입력하여 로그인할 수 있다고 서술하였으나 실제로는 그렇지 않았음 (12025.12.19 추가: 이제는 초기 패스워드가 "000000"이 아니므로 [아래 본문 내용](#5-4-원격-접속을-위한-ssh-서버-설정)을 꼭 확인할 것)
> - 컨테이너 시작 시 SSH 데몬이 자동 실행되지 않음
>
> 위 문제점들을 12025년 2월에 들어 인지하였으며, 한국 시간(UTC+9) 기준 12025년 2월 16일 오전 2시경 문제가 있던 Dockerfile과 Docker 이미지들을 문제를 해결한 파일들로 [GitHub 리포지터리](https://github.com/yunseo-kim/dl-env-docker)와 [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags)에 교체해 두었습니다.  
> 해당 일시 이전에 Dockerfile 또는 Docker 이미지를 Pull하였다면 수정한 버전으로 교체하시기 바랍니다.  
> 기존에 이 글을 참고하신 분들 중 잘못된 내용으로 혼란을 겪었던 분들이 계시다면 사과드립니다.
{: .prompt-info }

## 시작하기 전에

이 글은 [1편](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)에서 이어지는 글이므로, 만약 아직 읽지 않았다면 우선 이전 글부터 읽고 오는 것을 권장한다.

## 4. 컨테이너 런타임 구성

### Podman을 사용하는 경우

[CDI(Container Device Interface)를 활용하여 구성한다.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> 구 버전에서는 NVIDIA Container Toolkit 최초 설치 시, 그리고 이후 그래픽카드 장치 또는 드라이버 구성을 변경(버전 업그레이드 포함)할 때마다 매번 CDI 규격 파일을 수동으로 새로 생성해야 했다.
>
> 그러나 NVIDIA Container Toolkit `v1.18.0`부터는, `nvidia-cdi-refresh` systemd 서비스를 통해 다음의 경우 `/var/run/cdi/nvidia.yaml` CDI 규격 파일을 자동으로 생성하고 업데이트한다.
> - NVIDIA Container Toolkit 설치 혹은 업그레이드 시
> - NVIDIA GPU 드라이버 설치 혹은 업그레이드 시
> - 시스템 재부팅 시
>
> 따라서, 예전과 달리 이제는 따로 뭔가를 해 줘야 할 필요가 없다. 이를 반영하여 본문 내용을 수정하였다.
>
> 단, GPU 드라이버의 제거 또는 MIG 기기 재구성 시에는 `nvidia-cdi-refresh`가 대응하지 못하므로 수동으로 `nvidia-cdi-refresh.service`를 재시작해 CDI 규격 재생성을 유도해야 한다.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> NVIDIA Container Runtime hook를 CDI와 함께 사용하면 충돌할 수 있으므로, 만약 `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath}이 존재한다면 해당 파일을 삭제하거나 혹은 `NVIDIA_VISIBLE_DEVICES` 환경변수가 설정된 상태로 컨테이너를 실행하지 않도록 주의한다.
{: .prompt-warning }

### Docker를 사용하는 경우

[루트리스(rootless) 모드](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode) 기준으로 설명한다.

#### 4-Docker-1. `nvidia-ctk` 명령으로 컨테이너 런타임 설정 구성

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

위 명령은 Docker가 NVIDIA Container Runtime을 활용할 수 있도록 `/etc/docker/daemon.json`{: .filepath} 파일을 수정한다.

#### 4-Docker-2. Docker 데몬 재시작

변경한 설정을 적용하기 위해 Docker 데몬을 재시작한다.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. `sudo nvidia-ctk` 명령으로 `/etc/nvidia-container-runtime/config.toml`{: .filepath} 설정 파일 구성

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### 정상적으로 구성되었는지 확인

샘플 CUDA 컨테이너를 실행해본다.

Podman을 사용하는 경우 다음 명령을 실행한다.

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Docker를 사용하는 경우 다음 명령을 실행한다.

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

대략 아래와 유사한 화면이 표시되면 성공이다.

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

## 5. Dockerfile 작성

Docker Hub의 [nvidia/cuda 리포지터리](https://hub.docker.com/r/nvidia/cuda)에서 제공하는 CUDA 및 cuDNN 이미지를 기반으로 하여 개발환경으로 사용할 Dockerfile을 작성한다.

- 필요로 하는 CUDA 및 cuDNN 버전, 리눅스 배포판 종류 및 버전 등을 고려하여 사용할 이미지를 결정해야 한다. 
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  이 글의 작성 시점인 12024년 8월 말을 기준으로, PyTorch 최신 버전인 2.4.0 버전은 CUDA 12.4를 지원한다. 따라서 여기서는 [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)이미지를 사용한다. [PyTorch 홈페이지](https://pytorch.org/get-started/locally/)에서 PyTorch 최신 버전 및 지원하는 CUDA 버전을 확인할 수 있다.

완성된 Dockerfile의 소스는 [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub 리포지터리에 공개해 두었다. 아래에 해당 Dockerfile을 작성한 과정을 단계별로 설명한다.

> (+ 12026.1.6. 개정)  
> PyTorch 2.9.1과 CUDA 12.8 / 13.0을 지원하는 Dockerfile 및 이미지들을 동일한 GitHub 리포지터리 및 [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) Docker Hub 공개 리포지터리에 추가하였다. 본문의 내용도 PyTorch 2.9.1, CUDA 13.0에 맞춰 갱신하였다.
>
> 또한 scikit-image와 XGBoost, 그리고 RAPIDS 생태계 내 cuGraph, cuxfilter, cuCIM, RAFT, cuVS 라이브러리를 이미지 안에 포함시켰고, 기존 `amd64` 아키텍처에 더하여 `arm64` 지원을 추가하였다.
{: .prompt-info }

### 5-1. base 이미지 지정

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. 시스템 시간대 설정 (이 글에서는 'Asia/Seoul'로 진행)

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> [이 글](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22)의 내용을 주로 참고하였다.
{: .prompt-tip }

### 5-3. 기본 시스템 유틸리티 설치

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

### 5-4. 원격 접속을 위한 SSH 서버 설정

보안을 위해 SSH 원격 접속 시 root 계정 로그인이 불가능하도록 설정한다.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

SSH 접속 시 사용할 'remote'라는 이름의 non-root 사용자를 생성한다.

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

> 빌드 인수(`ARG`)나 환경 변수(`ENV`)의 내용은 빌드한 이미지에 그대로 노출되므로, [패스워드나 API 키와 같은 민감 정보를 지정할 때는 다른 방법을 사용해야 한다](https://docs.docker.com/build/building/secrets/). 여기서는 [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts)를 사용하였다.
{: .prompt-danger }

> [후술하겠지만](#6-1-이미지-빌드), 이 Dockerfile을 이용하여 이미지를 빌드할 때는 `DL_ENV_PASSWD` 환경변수를 통해 사용자 계정 패스워드로 사용할 문자열을 지정해 주어야 한다. [Docker Hub 배포 이미지](https://hub.docker.com/r/yunseokim/dl-env/tags)의 경우 계정 패스워드 초기값은 `satisfied-flip-remake`이며, 이 공개된 기본 패스워드를 그대로 사용하면 보안상 매우 취약하니 컨테이너를 처음 실행한 뒤 즉시 설정을 변경해 주도록 하자. 또한 보안을 위해서는 SSH 접속 시 패스워드 로그인을 비활성화하고 별도의 키 파일을 통해서만 로그인이 가능하도록 추후 설정하는 것이 바람직하며, Yubikey와 같은 하드웨어 키까지 활용한다면 이상적이다.
>
> SSH 서버 구성에 관해서는 이 시리즈의 다음 편에서 어느 정도 다룰 예정이며, 더 자세히 알고 싶다면 다음 목록에 있는 문서들을 참고하면 좋다.
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. uv 설치 및 환경변수 등록

> **[PEP 668](https://peps.python.org/pep-0668/)에 따른 [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) 스펙 반영 및 uv 도입 (12026.1.6. 개정)**
>
> 과거 이 글에서는 별도의 가상 환경(`venv`)을 생성하지 않고 컨테이너 이미지 안에서 곧바로 `pip`를 통한 패키지 설치를 진행하도록 Dockerfile을 작성하였다. 그렇게 한 이유는, 단일 목적의 컨테이너 이미지 안에서는 시스템 소프트웨어가 깨질 위험성이 낮고 설령 문제가 발생하더라도 이미지를 이용해 새로운 컨테이너를 생성하면 그만이기에 별도로 가상 환경을 생성할 필요성이 낮다는 판단 때문이었다. 이러한 점은 [PEP 668](https://peps.python.org/pep-0668/#use-cases)에서도 다음과 같이 부분적으로 인정한 바 있다.
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> 그러나, 이처럼 단일 목적 컨테이너 이미지 안에서라 할지라도 `pip`와 같은 파이썬 패키지 관리자를 통한 설치는 가상환경 안에서만 수행함으로써 운영체제 패키지 매니저 등을 통해 외부적으로 관리되는(externally managed) 패키지들과는 엄격히 구분하는 것이 표준으로 확립되었다. 이에 가상 환경을 생성 후 그 안에서 필요한 패키지들을 설치하도록 본문 내용을 개정, [PEP 668](https://peps.python.org/pep-0668/)과 그에 따른 [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) 스펙을 준수하고 파이썬 생태계 표준을 따르도록 하였다.
>
> 파이썬에서 가상 환경 생성 및 관리를 위해 공식 지원하는 표준 라이브러리는 [12021년 초에 작성한 다른 글에서도 한 차례 소개하였듯](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended) `venv`이다. 그러나 [Astral](https://astral.sh/)에서 Rust로 개발한 고성능 파이썬 패키지 및 프로젝트 관리자, [`uv`](https://docs.astral.sh/uv/)가 12024년에 처음 공개된 이후 다음과 같은 여러 큰 장점들 덕에 빠른 속도로 파이썬 생태계에서 새로운 사실상의 표준으로 자리 잡았다.
> - [`pip` 대비 압도적인 의존성 해결 및 패키지 설치 속도(10-100배)](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
> - 뛰어난 사용 편의성
> - [우수한 기존 `pip` 및 `venv`와의 호환성](https://docs.astral.sh/uv/pip/)
>
> 특히 여기서 다루는 PyTorch, RAPIDS 같은 머신러닝 분야 패키지들은 의존 패키지 수가 많고 대체로 대용량인 편이라 이러한 `uv`의 장점이 십분 발휘된다. 게다가 [`uv`는 캐시를 적극적이고 효율적으로 활용하기 때문에](https://docs.astral.sh/uv/concepts/cache/), 지금처럼 [컨테이너 이미지를 빌드할 때 cache mount를 적절히 활용해 주면 해당 장점을 극대화하여 빌드 시간을 크게 줄일 수 있다](https://docs.astral.sh/uv/guides/integration/docker/#caching). 따라서 여기서도 가상 환경 생성 및 관리, 그리고 패키지 설치 용도로 `uv`를 도입하겠다. `uv`의 ["Using uv in Docker" 공식 문서](https://docs.astral.sh/uv/guides/integration/docker/) 내용을 주로 참고하여 작업하였다.
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

> **`UV_CACHE_DIR`을 기본값인 `"$HOME_DIR/.cache/uv"` 대신 홈 디렉터리 밖 별도의 경로(`"/tmp/uv-cache"`)로 지정한 이유**
>
> 원래 `useradd --create-home`을 통해 사용자를 추가하면 해당 사용자는 자기 홈 디렉터리의 소유권을 갖고 있어야 정상이고, 여기서도 그러하다.
> 그러나 Podman에서 이미지 빌드 시, 앞쪽 레이어에서 정상적으로 소유권을 이전하였어도 뒤쪽 레이어에서 캐시 등을 마운트할 경우 그 상위 디렉터리의 소유권 메타데이터가 기본값(root 소유)으로 재설정되는 버그가 있음을 발견하였다. 관련하여 검색 결과, [약 3주 전쯤에 동일한 현상에 대해 다른 사용자가 보고한 이슈](https://github.com/containers/podman/issues/27777)를 발견하였으나 해당 이슈에 대해 아직 아무런 답변은 달리지 않은 상황이다. 내가 경험한 상황에 대한 자세한 정보는 [해당 이슈에 대하여 추가 코멘트로 달아 두었다](https://github.com/containers/podman/issues/27777#issuecomment-3712237296).
>
> 이에 소유권이 root로 재설정되더라도 문제가 되지 않도록, 빌드 단계에서는 `UV_CACHE_DIR`을 `$HOME_DIR`과 별개의 경로인 `"/tmp/uv-cache"`로 지정하였다. 어차피 이 캐시는 빌드 결과물인 최종 이미지에는 포함되지 않으므로 경로를 적절히 변경해도 상관없다.
{: .prompt-tip }

### 5-6. Python 설치, 가상환경 생성, setuptools & pip 설치

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

### 5-7. 개발환경에서 사용할 머신러닝 및 딥러닝 패키지 설치

#### 5-7-1. 공통 패키지들

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & CUDA 전용 GPU 가속 라이브러리

##### PyTorch만 설치할 경우

PyTorch만 설치하려면 다음 내용을 Dockerfile에 추가한다.

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & Cupy & RAPIDS & DALI

PyTorch뿐만 아니라 Cupy와 RAPIDS(cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS), 그리고 DALI를 사용하려면 다음 내용을 Dockerfile에 추가한다.

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

> 이때 PyTorch와 RAPIDS 패키지들이 몇몇 의존 라이브러리들(cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE)을 공유하는데, 따로따로 설치할 경우 서로 요구하는 버전이 달라 앞서 설치한 버전이 나중에 설치하는 버전으로 덮어씌워지면서 의존성 충돌이 발생할 우려가 커진다. 따라서 이들 패키지를 설치할 때는 설치 명령을 하나의 `uv pip install` 명령으로 통합하여 의존성 해결사(resolver)가 모든 제약 조건을 동시에 고려하도록 하고, PyTorch가 요구하는 버전을 우선순위로 둔다.
{: .prompt-tip }

### 5-8. 작업공간으로 사용할 디렉터리 생성

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. 포트 개방 및 컨테이너 시작 시 실행할 `ENTRYPOINT` 설정
SSH와 Jupyter Lab 접속을 위해 22, 8888 포트를 개방한다.  
또한 컨테이너 시작 시 SSH 데몬을 자동 실행하기 위해서는 루트 권한이 필요하므로 다음의 방법을 사용할 것이다.
1. 컨테이너 시작 시 root 계정으로 로그인된 상태
2. 컨테이너 시작 직후 `/entrypoint.sh`{: .filepath} 스크립트를 실행
3. 해당 스크립트에서 SSH 서비스를 시작한 후 [`gosu`](https://github.com/tianon/gosu)를 사용하여 remote 계정으로 전환
4. 컨테이너 실행 시 별도로 지정한 명령이 없다면 기본값으로 Jupyter Lab을 remote 계정(non-root 권한)으로 실행

> 일반적으로 Docker나 Podman 컨테이너 안에서의 `sudo` 또는 `su` 사용은 권장되지 않으며, 루트 권한이 필요할 경우 여기서 설명하는 것과 같이 일단 root 계정으로 컨테이너를 시작하고 루트 권한이 필요한 작업들을 수행한 후에 [`gosu`](https://github.com/tianon/gosu)를 사용하여 non-root 사용자로 전환하는 것이 좋다. 이렇게 해야 하는 이유는 아래의 자료들에 자세히 설명되어 있으므로 필요할 경우 참고하면 도움이 될 것이다.
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

우선 Dockerfile의 마지막 부분에 다음 내용을 입력한다.

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

다음으로, 작성한 Dockerfile과 동일한 경로에 `entrypoint.sh`{: .filepath}라는 이름으로 스크립트 파일을 생성하고 내용은 아래와 같이 작성한다.

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

> 일반적으로 docker exec나 CMD로 실행된 프로세스는 Docker의 ENV를 그대로 상속받지만, SSH로 접속한 세션은 Docker의 환경 변수를 자동으로 상속받지 못하는 경우가 많다. SSH는 로그인 시 새로운 쉘 세션을 생성하기 때문이다.
>
> 이를 해결하고 SSH 접속 시에도 `$WORK_DIR`과 같이 사전에 정의해 둔 환경 변수들에 접근 가능하도록 하려면, 컨테이너 실행 시 ssh 서비스를 시작하기 이전에 `printenv | grep _ >> /etc/environment` 같은 식으로 환경변수들을 미리 `/etc/environment`{: .filepath }에 덤프해 주는 것이 필요하다.
>
> 관련하여 다음 링크의 글들을 참고하면 도움이 된다.
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. OCI 이미지 빌드 및 컨테이너 실행

### 6-1. 이미지 빌드

Dockerfile이 위치한 디렉터리에서 터미널을 열고, `DL_ENV_PASSWD` 환경변수를 지정한다.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> \<your_own_password\> 자리에 SSH 접속 시 사용할 로그인 패스워드를 입력하면 된다.
{: .prompt-info }

이제 **해당 터미널 창을 닫지 말고**, 동일한 창에서 이어서 아래 명령을 실행, 빌드를 진행한다.

#### Podman의 경우

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> Podman 기준으로, 배포를 염두에 두고 본인이 사용 중인 기기의 플랫폼(운영체제/아키텍처)뿐만 아니라 base 이미지가 지원하는 모든 플랫폼에 대해 이미지를 빌드하려면 다음과 같이 [`--all-platforms` 옵션](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms)을 지정하고, [`--tag`나 `-t` 대신 `--manifest` 옵션을 대신 사용하면 된다](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant).
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> Docker의 경우 여기에 따로 정리하진 않았으니, 필요하다면 [Docker 공식 문서](https://docs.docker.com/build/building/multi-platform/)를 참고하도록 한다.
{: .prompt-tip }

#### Docker의 경우

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. 샘플 워크로드 실행

빌드를 완료했다면 일회용 컨테이너를 실행하여 잘 동작하는지 확인한다.

Podman의 경우 다음 명령을 실행한다.

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Docker의 경우 다음 명령을 실행한다.
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

터미널에서 위 명령을 입력하면 앞서 빌드한 `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04` 이미지로부터 `test-container`라는 이름의 컨테이너를 실행한 뒤 호스트 시스템의 2222번 포트와 해당 컨테이너의 22번 포트, 호스트 시스템의 8888번 포트와 컨테이너의 8888번 포트를 각각 연결한다. 앞선 단계에서 이미지가 정상적으로 빌드되었고 컨테이너가 문제 없이 시작되었다면, `test-container` 컨테이너 안에서 JupyterLab이 기본값인 `http:127.0.0.1:8888` 주소로 실행 중일 것이다. 따라서 Podman이나 Docker가 동작하는 호스트 시스템에서 브라우저를 열고 <http://127.0.0.1:8888>로 접속했을 때, 컨테이너 내부의 `http://127.0.0.1:8888` 주소로 연결되어 아래와 같은 화면이 표시되어야 한다.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

호스트 시스템에서 터미널을 열고 `ssh remote@127.0.0.1 -p 2222` 명령을 실행하여 컨테이너 내부에서 실행 중인 우분투 시스템의 remote 계정으로 원격 로그인해 보자.  
처음 로그인할 때는 접속 대상의 암호키에 관한 정보가 없으며 인증이 불가능하다는 경고가 출력되고, 계속 연결할 것인지 묻는데 "yes"를 입력하여 계속 진행하면 된다.  
이후 로그인을 위해 앞서 빌드 시 지정했던 패스워드(혹은 [Docker Hub 배포 이미지](https://hub.docker.com/r/yunseokim/dl-env/tags)를 pull하여 처음 로그인하는 경우라면, 초기 패스워드 `satisfied-flip-remake`)를 입력한다.

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {핑거프린트(각 키마다 제각기 다른 고유한 값을 가진다)}.
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
대략 위와 유사하게 출력된다면 SSH를 통한 원격 로그인에 성공한 것이다. 접속을 종료할 때는 `exit` 명령을 입력하면 된다.

### 6-3. (optional) Docker Hub에 Push하기

앞선 과정을 거쳐 만든 개발환경 이미지를 필요할 때 언제든 Pull하여 활용하려면 빌드한 이미지를 Docker Hub에 Push해 두는 것이 좋다.  

> Docker Hub에 자신의 이미지를 Push하려면 본인의 Docker 계정이 필요하므로, 만약 아직 없다면 <https://app.docker.com/signup>에서 회원가입을 먼저 완료한다.
{: .prompt-tip }

#### 6-3-1. Docker Hub 로그인

##### Podman의 경우

```bash
podman login docker.io
```

##### Docker의 경우

```bash
docker login
```

#### 6-3-2. 이미지 태그 지정

`<dockerhub_username>`과 `<repository_name>`, (선택)`:TAG` 부분에는 본인에게 해당하는 내용을 채워넣으면 된다.  
e.g. "yunseokim", "dl-env", "rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04"

> 앞서 본인이 사용 중인 기기의 플랫폼(운영체제/아키텍처)뿐만 아니라 base 이미지가 지원하는 모든 플랫폼에 대해 이미지를 빌드했고, 이 manifest 리스트 내지 이미지 인덱스를 일괄 Push하려는 경우라면 이 단계는 건너뛰고 [이미지 Push](#6-3-3-이미지-push) 단계로 곧바로 이동하여 거기에 작성해 둔 방법을 따른다.
{: .prompt-tip }

##### Podman의 경우

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Docker의 경우

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. 이미지 Push

마지막으로, 아래 명령을 실행하여 해당 이미지를 Docker Hub에 Push한다.

##### Podman의 경우

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> Podman 기준으로, 여러 플랫폼에 대응하는 각각의 이미지를 manifest 리스트 또는 이미지 인덱스로 묶어 한꺼번에 Push하려면 다음과 같이 [`podman manifest push` 명령](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls)을 사용한다.
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

##### Docker의 경우

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

<https://hub.docker.com/>에서 아래와 같이 잘 Push되었음을 확인할 수 있다.

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

앞선 과정을 거쳐 완성한 이미지는 Docker Hub의 [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) 공개 리포지터리에 공개해 두었으며, 누구든 자유롭게 사용할 수 있다.

이미지를 Pull하기 위해서는 앞서 Push할 때 사용한 명령어에서 `push` 부분만 `pull`로 바꿔서 실행해 주면 된다.
