---
title: NVIDIA Container Toolkit과 Docker로 딥러닝 개발환경 구축하기 (2) - GPU 활용을 위한 컨테이너 런타임 구성,
  Dockerfile 작성 및 Docker 이미지 빌드
description: 이 시리즈는 로컬에 NVIDIA Container Toolkit과 Docker 기반의 딥러닝 개발환경을 구축하고, 원격 서버로
  활용할 수 있도록 SSH 및 Jupyter Lab을 설정하는 방법을 다룬다. 이 포스트는 해당 시리즈의 첫 번째 글로, NVIDIA Container
  Toolkit의 설치 방법을 소개한다.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## 개요
이 시리즈에서는 NVIDIA Container Toolkit과 Docker를 설치하고, Docker Hub의 [nvidia/cuda 리포지터리](https://hub.docker.com/r/nvidia/cuda)에서 제공하는 CUDA 및 cuDNN 이미지를 기반으로 Dockerfile을 작성하여 딥러닝 개발환경을 구축하는 과정을 다룬다. 필요한 분들은 자유롭게 가져다 사용할 수 있도록 이 과정을 거쳐 완성한 [Dockerfile](https://github.com/yunseo-kim/dl-env-docker)과 [이미지](https://hub.docker.com/r/yunseokim/dl-env/tags)를 GitHub와 Docker Hub를 통해 공유하며, 추가적으로 원격 서버로 활용하기 위한 SSH 및 Jupyter Lab 설정 가이드를 제공한다.  
시리즈는 3개의 글로 이루어질 예정이며, 읽고 있는 이 글은 해당 시리즈의 두 번째 글이다.
- [1편: NVIDIA Container Toolkit & Docker Engine 설치](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- 2편: GPU 활용을 위한 컨테이너 런타임 구성, Dockerfile 작성 및 Docker 이미지 빌드 (본문)
- 3편 (업로드 예정)

x86_64 리눅스 환경에서 CUDA를 지원하는 NVIDIA 그래픽카드를 장착한 시스템이라고 전제하고 진행하며, Ubuntu 또는 Fedora 이외의 배포판에서는 직접 테스트해 보지 않았기에 몇몇 세부적인 부분은 약간 차이가 있을 수 있다.

## 시작하기 전에
이 글은 [1편](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)에서 이어지는 글이므로, 만약 아직 읽지 않았다면 우선 이전 글부터 읽고 오는 것을 권장한다.

## 4. 컨테이너 런타임 구성
### 4-1. `nvidia-ctk` 명령 실행
```bash
sudo nvidia-ctk runtime configure --runtime=docker
```
위 명령은 Docker가 NVIDIA Container Runtime을 활용할 수 있도록 `/etc/docker/daemon.json`{: .filepath} 파일을 수정한다.

### 4-2. Docker 데몬 재시작
변경한 설정을 적용하기 위해 Docker 데몬을 재시작한다.
```bash
sudo systemctl restart docker
```

### 4-3. 정상적으로 구성되었는지 확인
샘플 CUDA 컨테이너를 실행해본다.
```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
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
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)이 글의 작성 시점인 2024년 8월 말을 기준으로, PyTorch 최신 버전인 2.4.0 버전은 CUDA 12.4를 지원한다. 따라서 여기서는 [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore)이미지를 사용한다. [PyTorch 홈페이지](https://pytorch.org/get-started/locally/)에서 PyTorch 최신 버전 및 지원하는 CUDA 버전을 확인할 수 있다.

완성된 Dockerfile의 소스는 [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub 리포지터리에 공개해 두었다. 아래에 해당 Dockerfile을 작성한 과정을 단계별로 설명한다.

### 5-1. base 이미지 지정
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. 기본 유틸리티 및 Python prerequisites 설치
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

### 5-3. 시스템 시간대 설정 (이 글에서는 'Asia/Seoul'로 진행)
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. 원격 접속을 위한 SSH 서버 설정  
보안을 위해 SSH 원격 접속 시 패스워드로는 root 계정 로그인이 불가능하도록 설정한다.
```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```
컨테이너 시작 시 SSH 서비스가 자동으로 시작되도록 구성한다.
```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```
SSH 접속 시 사용할 'remote'라는 이름의 non-root 사용자를 생성한다.
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

> 이 Dockerfile을 이용하여 Docker 이미지를 빌드할 때 별도로 옵션을 지정하지 않을 시, 'remote' 사용자의 계정 패스워드 초기값은 000000이다. 이는 보안상 매우 취약하니 Docker 이미지 빌드 시 `--build-arg` 옵션을 이용하여 계정 로그인 패스워드를 따로 지정하거나, 혹은 컨테이너를 처음 실행한 뒤 즉시 설정을 변경해 주도록 하자. 보안을 위해서는 SSH 접속 시 패스워드 로그인을 비활성화하고 별도의 키 파일을 통해서만 로그인이 가능하도록 추후 설정하는 것이 바람직하며, Yubikey와 같은 하드웨어 키까지 활용한다면 이상적이다.
> SSH 서버 구성에 관해서는 이 시리즈의 다음 편에서 어느 정도 다룰 예정이며, 더 자세히 알고 싶다면 다음 목록에 있는 문서들을 참고하면 좋다.
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. setuptools, pip 설치 및 PATH 환경변수 등록
```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. 개발환경에서 사용할 머신러닝 및 딥러닝 패키지 설치
```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
Cupy, cuDF, cuML, 그리고 DALI를 사용하려면 다음 내용도 Dockerfile에 추가한다.
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. 컨테이너 시작 시 JupyterLab 실행 설정
```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
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
빌드를 완료했다면, 다음 명령으로 일회용 컨테이너를 실행하여 잘 동작하는지 확인한다.
```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```
터미널에서 위 명령을 입력하면 앞서 빌드한 `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` 이미지로부터 `test-container`라는 이름의 컨테이너를 실행한 뒤 호스트 시스템의 88번 포트를 해당 컨테이너의 8888번 포트로 연결한다. 앞선 단계에서 Docker 이미지가 정상적으로 빌드되었고 컨테이너가 문제 없이 시작되었다면, `test-container` 컨테이너 안에서 JupyterLab이 기본값인 `http:127.0.0.1:8888` 주소로 실행 중일 것이다. 따라서 Docker Engine이 동작하는 호스트 시스템에서 브라우저를 열고 <http://127.0.0.1:88>로 접속했을 때, 컨테이너 내부의 `http://127.0.0.1:8888` 주소로 연결되어 아래와 같은 화면이 표시되어야 한다.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (optional) Docker Hub에 Push하기
앞선 과정을 거쳐 만든 개발환경 이미지를 필요할 때 언제든 Pull하여 활용하려면 빌드한 이미지를 Docker Hub에 Push해 두는 것이 좋다.  

> Docker Hub에 자신의 이미지를 Push하려면 본인의 Docker 계정이 필요하므로, 만약 아직 없다면 <https://app.docker.com/signup>에서 회원가입을 먼저 완료한다.
{: .prompt-tip }

우선 아래 명령으로 Docker Hub에 로그인한다.
```bash
docker login
```
이제 다음과 같은 형식의 명령을 실행하여 이미지 태그를 생성한다.
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```
마지막으로, 아래 명령을 실행하여 해당 이미지를 Docker Hub에 Push한다.
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
<https://hub.docker.com/>에서 아래와 같이 잘 Push되었음을 확인할 수 있다.  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

앞선 과정을 거쳐 완성한 이미지는 Docker Hub의 [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) 공개 리포지터리에 공개해 두었으며, 누구든 자유롭게 사용할 수 있다.
