---
title: NVIDIA Container Toolkit과 Docker/Podman으로 딥러닝 개발환경 구축하기 (2) - GPU 활용을 위한 컨테이너 런타임 구성,
  Dockerfile 작성 및 컨테이너 이미지 빌드
description: 이 시리즈는 로컬에 NVIDIA Container Toolkit으로 컨테이너 기반의 딥러닝 개발환경을 구축하고, 원격 서버로
  활용할 수 있도록 SSH 및 Jupyter Lab을 설정하는 방법을 다룬다. 이 포스트는 해당 시리즈의 두 번째 글로, Dockerfile을 작성하고 컨테이너 이미지를 빌드하는 과정을 다룬다.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---
## 개요
이 시리즈에서는 NVIDIA Container Toolkit과 Docker 또는 Podman을 설치하고, Docker Hub의 [nvidia/cuda 리포지터리](https://hub.docker.com/r/nvidia/cuda)에서 제공하는 CUDA 및 cuDNN 이미지를 기반으로 Dockerfile을 작성하여 딥러닝 개발환경을 구축하는 과정을 다룬다. 필요한 분들은 자유롭게 가져다 사용할 수 있도록 이 과정을 거쳐 완성한 [Dockerfile](https://github.com/yunseo-kim/dl-env-docker)과 [이미지](https://hub.docker.com/r/yunseokim/dl-env/tags)를 GitHub와 Docker Hub를 통해 공유하며, 추가적으로 원격 서버로 활용하기 위한 SSH 및 Jupyter Lab 설정 가이드를 제공한다.  
시리즈는 3개의 글로 이루어질 예정이며, 읽고 있는 이 글은 해당 시리즈의 두 번째 글이다.
- [1편: NVIDIA Container Toolkit & 컨테이너 엔진 설치](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 2편: GPU 활용을 위한 컨테이너 런타임 구성, Dockerfile 작성 및 컨테이너 이미지 빌드 (본문)
- 3편 (업로드 예정)

x86_64 리눅스 환경에서 CUDA를 지원하는 NVIDIA 그래픽카드를 장착한 시스템이라고 전제하고 진행하며, Ubuntu 또는 Fedora 이외의 배포판에서는 직접 테스트해 보지 않았기에 몇몇 세부적인 부분은 약간 차이가 있을 수 있다.  
(12025.02.18. 내용 업데이트)

> **오류 정정 안내**  
> [인류력](https://en.wikipedia.org/wiki/Holocene_calendar) 12024년 8월에 업로드한 이 글의 초본에서 [Dockerfile 작성](#5-dockerfile-작성) 부분의 서술 및 해당 Dockerfile로부터 빌드한 이미지에 일부 오류가 있었습니다. 문제가 있던 부분은 다음과 같습니다.
> - remote 계정 생성 부분에서 비밀번호를 설정하는 부분이 잘못되었으며, 원래대로라면 "000000"을 패스워드로 입력하여 로그인할 수 있어야 하나 그렇지 않았음
> - 컨테이너 시작 시 SSH 데몬이 자동 실행되지 않음
>
> 위 문제점들을 최근 인지하였으며, 한국 시간(UTC+9) 기준 12025년 2월 16일 오전 2시경 문제가 있던 Dockerfile과 Docker 이미지들을 문제를 해결한 파일들로 [GitHub 리포지터리](https://github.com/yunseo-kim/dl-env-docker)와 [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags)에 교체해 두었습니다.  
> 해당 일시 이전에 Dockerfile 또는 Docker 이미지를 Pull하였다면 수정된 버전으로 교체하시기 바랍니다.  
> 기존에 이 글을 참고하신 분들 중 잘못된 내용으로 혼란을 겪었던 분들이 계시다면 사과드립니다.
{: .prompt-info }

## 시작하기 전에
이 글은 [1편](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)에서 이어지는 글이므로, 만약 아직 읽지 않았다면 우선 이전 글부터 읽고 오는 것을 권장한다.

## 4. 컨테이너 런타임 구성
### Podman을 사용하는 경우
[CDI(Container Device Interface)를 활용하여 구성한다.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

다음 명령을 실행하여 CDI 규격 파일을 `/etc/cdi`{: .filepath} 디렉터리에 생성한다.
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> 그래픽카드 장치를 바꾸거나 CUDA 드라이버 구성을 변경(버전 업그레이드 포함)하는 경우 CDI 규격 파일을 새로 생성해야 한다.
{: .prompt-warning }

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
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)이 글의 작성 시점인 12024년 8월 말을 기준으로, PyTorch 최신 버전인 2.4.0 버전은 CUDA 12.4를 지원한다. 따라서 여기서는 [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)이미지를 사용한다. [PyTorch 홈페이지](https://pytorch.org/get-started/locally/)에서 PyTorch 최신 버전 및 지원하는 CUDA 버전을 확인할 수 있다.

완성된 Dockerfile의 소스는 [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub 리포지터리에 공개해 두었다. 아래에 해당 Dockerfile을 작성한 과정을 단계별로 설명한다.

### 5-1. base 이미지 지정
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. 기본 유틸리티 및 Python prerequisites 설치
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

### 5-3. 시스템 시간대 설정 (이 글에서는 'Asia/Seoul'로 진행)
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
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

> 이 Dockerfile을 이용하여 Docker 이미지를 빌드할 때 별도로 옵션을 지정하지 않을 시, 'remote' 사용자의 계정 패스워드 초기값은 000000이다. 이는 보안상 매우 취약하니 Docker 이미지 빌드 시 `--build-arg` 옵션을 이용하여 계정 로그인 패스워드를 따로 지정하거나, 혹은 컨테이너를 처음 실행한 뒤 즉시 설정을 변경해 주도록 하자. 보안을 위해서는 SSH 접속 시 패스워드 로그인을 비활성화하고 별도의 키 파일을 통해서만 로그인이 가능하도록 추후 설정하는 것이 바람직하며, Yubikey와 같은 하드웨어 키까지 활용한다면 이상적이다.
> SSH 서버 구성에 관해서는 이 시리즈의 다음 편에서 어느 정도 다룰 예정이며, 더 자세히 알고 싶다면 다음 목록에 있는 문서들을 참고하면 좋다.
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> 또한 이 Dockerfile은 빌드한 이미지를 개인 혹은 신뢰할 수 있는 소수의 내부자들만 사용함을 상정하고 있으며, 만약 빌드한 이미지를 외부에 배포해야 한다면 `--build-arg`를 통한 패스워드 설정은 위험하므로 다른 방법을 사용해야 한다. [이 문서](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/)를 참고하기 바란다.
{: .prompt-danger }

### 5-5. setuptools, pip 설치 및 PATH 환경변수 등록
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. 개발환경에서 사용할 머신러닝 및 딥러닝 패키지 설치
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Cupy, cuDF, cuML, 그리고 DALI를 사용하려면 다음 내용도 Dockerfile에 추가한다.
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. 작업공간으로 사용할 디렉터리 생성
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. 포트 개방 및 컨테이너 시작 시 실행할 `ENTRYPOINT` 설정
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
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

다음으로, 작성한 Dockerfile과 동일한 경로에 `entrypoint.sh`{: .filepath}라는 이름으로 스크립트 파일을 생성하고 내용은 아래와 같이 작성한다.
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

## 6. Docker 이미지 빌드 및 컨테이너 실행
### 6-1. 이미지 빌드
Dockerfile이 위치한 디렉터리에서 터미널을 열고 아래 명령을 실행한다.
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> \<password\> 자리에 SSH 접속 시 사용할 로그인 패스워드를 입력하면 된다.
{: .prompt-info }

### 6-2. 샘플 워크로드 실행
빌드를 완료했다면 일회용 컨테이너를 실행하여 잘 동작하는지 확인한다.

Podman의 경우 다음 명령을 실행한다.
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Docker의 경우 다음 명령을 실행한다.
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

터미널에서 위 명령을 입력하면 앞서 빌드한 `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` 이미지로부터 `test-container`라는 이름의 컨테이너를 실행한 뒤 호스트 시스템의 22번 포트와 해당 컨테이너의 22번 포트, 호스트 시스템의 88번 포트와 컨테이너의 8888번 포트를 각각 연결한다. 앞선 단계에서 Docker 이미지가 정상적으로 빌드되었고 컨테이너가 문제 없이 시작되었다면, `test-container` 컨테이너 안에서 JupyterLab이 기본값인 `http:127.0.0.1:8888` 주소로 실행 중일 것이다. 따라서 Docker Engine이 동작하는 호스트 시스템에서 브라우저를 열고 <http://127.0.0.1:88>로 접속했을 때, 컨테이너 내부의 `http://127.0.0.1:8888` 주소로 연결되어 아래와 같은 화면이 표시되어야 한다.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

호스트 시스템에서 터미널을 열고 `ssh remote@127.0.0.1` 명령을 실행하여 컨테이너 내부에서 실행 중인 우분투 시스템의 remote 계정으로 원격 로그인해 보자.  
처음 로그인할 때는 접속 대상의 암호키에 관한 정보가 없으며 인증이 불가능하다는 경고가 출력되고, 계속 연결할 것인지 묻는데 "yes"를 입력하여 계속 진행하면 된다.  
이후 로그인을 위해 패스워드(이미지 빌드 시 따로 변경하지 않았다면 기본값인 "000000"일 것이다)를 입력한다.
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {핑거프린트(각 키마다 제각기 다른 고유한 값을 가진다)}.
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
e.g. "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

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

##### Docker의 경우
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
<https://hub.docker.com/>에서 아래와 같이 잘 Push되었음을 확인할 수 있다.  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

앞선 과정을 거쳐 완성한 이미지는 Docker Hub의 [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) 공개 리포지터리에 공개해 두었으며, 누구든 자유롭게 사용할 수 있다.

이미지를 Pull하기 위해서는 앞서 Push할 때 사용한 명령어에서 `push` 부분만 `pull`로 바꿔서 실행해 주면 된다.
