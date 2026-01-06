---
title: "NVIDIA Container Toolkit과 Docker/Podman으로 딥러닝 개발환경 구축하기 (1) - NVIDIA Container Toolkit & 컨테이너 엔진 설치"
description: "이 시리즈는 로컬에 NVIDIA Container Toolkit으로 컨테이너 기반의 딥러닝 개발환경을 구축하고, 원격 서버로 활용할 수 있도록 SSH 및 JupyterLab을 설정하는 방법을 다룬다. 이 포스트는 해당 시리즈의 첫 번째 글로, NVIDIA Container Toolkit과 컨테이너 엔진의 설치 방법을 소개한다."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## 개요

이 시리즈에서는 NVIDIA Container Toolkit과 Docker 또는 Podman을 설치하고, Docker Hub의 [nvidia/cuda 리포지터리](https://hub.docker.com/r/nvidia/cuda)에서 제공하는 CUDA 및 cuDNN 이미지를 기반으로 Dockerfile을 작성하여 딥러닝 개발환경을 구축하는 과정을 다룬다. 필요한 분들은 자유롭게 가져다 사용할 수 있도록 이 과정을 거쳐 완성한 [Dockerfile](https://github.com/yunseo-kim/dl-env-docker)과 [이미지](https://hub.docker.com/r/yunseokim/dl-env/tags)를 GitHub와 Docker Hub를 통해 공유하며, 추가적으로 원격 서버로 활용하기 위한 SSH 및 JupyterLab 설정 가이드를 제공한다.  
시리즈는 3개의 글로 이루어질 예정이며, 읽고 있는 이 글은 해당 시리즈의 첫 번째 글이다.
- 1편: NVIDIA Container Toolkit & 컨테이너 엔진 설치 (본문)
- [2편: GPU 활용을 위한 컨테이너 런타임 구성, Dockerfile 작성 및 컨테이너 이미지 빌드](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- 3편 (업로드 예정)

x86_64 리눅스 환경에서 CUDA를 지원하는 NVIDIA 그래픽카드를 장착한 시스템이라고 전제하고 진행하며, Ubuntu 또는 Fedora 이외의 배포판에서는 직접 테스트해 보지 않았기에 몇몇 세부적인 부분은 약간 차이가 있을 수 있다.  
(12026.1.6. 개정)

### 개발환경 구성

- 호스트 운영체제 및 아키텍처: x86_64, 리눅스 환경(Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x 등)
- 구축할 기술 스택(언어 및 라이브러리)
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/) (optional, NumPy/SciPy-compatible Array Library for GPU-accelerated Computing with Python)
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/) (optional, to accelerate pandas with zero code changes with the GPU accelerator)
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/) (optional, to quickly visualize and filter through large datasets, with a few lines of code, using best in class charting libraries)
  - [DALI](https://developer.nvidia.com/DALI) (optional, a high-performance alternative to built-in data loaders and data iterators using GPU)
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/) (optional, an accelerated n-dimensional image processing and image I/O alternative to scikit-image)
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/) (optional, to execute machine learning algorithms on GPUs with an API that closely follows the scikit-learn API)
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/) (optional, optimized algorithms for approximate nearest neighbors and clustering, along with many other essential tools for accelerated vector search)
  - [RAFT](https://docs.rapids.ai/api/raft/stable/) (optional, CUDA accelerated primitives which is used by other RAPIDS libraries)
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/) (optional, a GPU-accelerated graph analytics library which includes a zero-code-change accelerator for NetworkX)
  - [tqdm](https://tqdm.github.io/)

  > 상황에 따라, 그리고 본인의 선호에 따라, pandas 대신 [Polars](https://pola.rs/) DataFrame 라이브러리를 대신 사용하는 것도 고려해 볼 수 있다. Rust로 작성되었고, [대용량 데이터 처리 시 cuDF + pandas 조합에는 밀리지만 순정 pandas 패키지와 비교했을 때는 상당히 뛰어난 퍼포먼스를 보이며](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), Query에 보다 특화된 문법을 제공한다. 공식 [Polars 블로그](https://pola.rs/posts/polars-on-gpu/)와 [cuDF 문서](https://docs.rapids.ai/api/cudf/stable/cudf_polars/)에 따르면 Polars와 NVIDIA RAPIDS 팀이 협력하여 cuDF 기반 GPU 가속 엔진을 오픈 베타로 지원하고 있으며, 빠르게 개발을 진행 중이라고 한다.
  {: .prompt-tip }

  > Docker CE와 Podman 중 무엇을 사용할지 고민이라면 [후술한 비교 표](#3-컨테이너-엔진-설치)가 도움이 될 수 있다.
  {: .prompt-tip }

### 이전에 작성한 머신러닝 개발환경 구축 가이드와의 비교표

[기존에 이 블로그에 업로드했던 머신러닝 개발환경 구축 가이드](/posts/Setting-up-a-Machine-Learning-Development-Environment)가 이미 존재하지만, 여러 변경점이 있어 새로 이 포스트를 작성하였다. 달라진 점들은 아래 표와 같다.

| 차이점 | 기존 글 (12021 버전) | 본문 (12024 작성, 12026 개정 버전) |
| --- | --- | --- |
| 리눅스 배포판 | Ubuntu 기준 | Ubuntu 외에도 Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES 등에서 적용 가능 |
| 개발환경 구축 방식 | 호스트 시스템에 직접 설치<br>venv를 이용한 파이썬 가상환경 | [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)을 이용한<br> Docker 컨테이너 기반 환경<br> uv를 이용한 파이썬 가상환경 및 패키지 관리 |
| NVIDIA 그래픽 드라이버 설치 | O | O |
| 호스트 시스템에 <br>CUDA 및 cuDNN 직접 설치 | O (Apt 패키지 매니저 사용) | X ([Docker Hub에서 NVIDIA가 제공하는 사전 설치<br> 이미지](https://hub.docker.com/r/nvidia/cuda)를 사용하므로 직접 작업할 필요 없음)
| 이식성 | 다른 시스템으로 이전할 때마다<br> 개발환경을 새로 구축해야 함 | Docker 기반이므로, 제작해 둔 Dockerfile로 <br>필요할 때마다 새로운 이미지를 빌드하거나 <br>기존에 사용하던 이미지(추가 볼륨이나 네트워크<br> 설정 제외)를 쉽게 이식 가능 |
| cuDNN 외 추가적인 <br>GPU 가속 라이브러리 활용 | X | [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), [DALI](https://developer.nvidia.com/DALI) 도입 |
| Jupyter Notebook 인터페이스 | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH 서버 설정 | 따로 다루지 않음 | 기초적인 SSH 서버 설정 구성을 포함 |

## 0. 사전 확인사항

- [NVIDIA Container Toolkit은 Apt, Yum 또는 Dnf, Zypper 패키지 매니저를 지원하는 리눅스 배포판에서 사용 가능하다.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) 링크된 페이지에서 지원하는 리눅스 배포판 목록을 확인할 수 있으며, 공식 지원표에는 따로 기재되어 있지 않지만 Fedora 역시 RHEL과 같은 Red Hat Linux 기반이므로 문제 없이 사용 가능하다. 본인이 리눅스 환경에 익숙하지 않고 어떤 배포판을 사용해야 할지 잘 모르겠다면 우분투 LTS 버전을 사용하는 것이 제일 무난하다. 오픈소스가 아닌 독점 드라이버들도 자동 설치되어 초심자가 사용하기에도 비교적 편리하며, 사용자 수가 많기 때문에 대부분의 기술 문서가 우분투 기준으로 작성되어 있다.
  - 본인이 사용 중인 시스템 아키텍처 및 리눅스 배포판 버전은 터미널에서 `uname -m && cat /etc/*release` 명령으로 확인 가능하다.
- 시스템에 장착된 그래픽카드가 사용하려는 CUDA 및 cuDNN 버전을 지원하는 모델인지 우선 확인해야 한다.
  - 현재 컴퓨터에 장착된 GPU 모델명은 터미널에서 `lspci | grep -i nvidia` 명령으로 확인 가능하다.
  - <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> 페이지에서 cuDNN 버전별로 **지원하는 NVIDIA 그래픽 드라이버 버전** 및 요구하는 **CUDA Compute Capability** 조건, 그리고 **지원하는 NVIDIA 하드웨어** 목록을 확인하자.
  - <https://developer.nvidia.com/cuda-gpus>에 있는 GPU 목록에서 해당하는 모델명을 찾은 뒤, **Compute Capability** 수치를 확인하자. 이 수치가 앞서 확인한 **CUDA Compute Capability** 조건을 충족해야 CUDA 및 cuDNN을 문제 없이 사용 가능하다.

> 딥러닝 작업용 그래픽카드를 새로 구매할 예정이라면, GPU 선정 기준은 다음 글에 잘 정리되어 있다. 글쓴이가 비정기적으로 업데이트하고 있는 글이다.  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> GPU뿐만 아니라 전반적인 하드웨어 구성 가이드가 필요하다면, 같은 분이 작성한 [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)이라는 글도 매우 유익하다.
{: .prompt-tip }

위에서 언급한 모든 사항들을 충족하였다면 작업환경 구성을 시작하자.

## 1. NVIDIA 그래픽 드라이버 설치

우선 NVIDIA 그래픽 드라이버를 호스트 시스템에 설치해야 한다. [NVIDIA 드라이버 다운로드 페이지](https://www.nvidia.com/drivers/)에서 .run 인스톨러를 다운로드하여 이용해도 되지만, 가급적이면 본인 시스템의 패키지 매니저를 활용하여 설치하는 것이 버전 관리 및 유지보수 측면에서 좋다. <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> 공식 문서를 참고하여 본인의 시스템 환경에 맞는 그래픽 드라이버를 설치한다. 

### Proprietary module vs Open-source module

NVIDIA 리눅스 드라이버는 몇 가지 커널 모듈들로 구성되며, 버전 515 드라이버 및 그 이후 릴리즈부터 NVIDIA에서는 두 가지 유형의 드라이버 커널 모듈을 제공하고 있다.

- Proprietary: NVIDIA가 기존에 제공해 왔던 독점 소프트웨어 드라이버.
- Open-source: MIT/GPLv2 이중 라이선스로 제공되는 오픈 소스 드라이버. <https://github.com/NVIDIA/open-gpu-kernel-modules>를 통해 소스코드를 공개함.

Proprietary 드라이버는 Maxwell 아키텍처부터 Blackwell 이전까지의 아키텍처 기반으로 설계된 GPU들에 대해 제공되며, Blackwell 아키텍처부터는 지원 중단될 예정이다.
반면 Open-source 드라이버는 Turing 및 그 이후의 아키텍처에 대해 지원된다.

[NVIDIA에서는 가능하다면 오픈소스 커널 모듈을 사용할 것을 권장하고 있다.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
사용 중인 GPU가 오픈소스 드라이버와 호환되는지는 [이 링크](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus)에서 확인 가능하다.

이 글에서는 오픈소스 드라이버를 설치한다고 가정하고 설명한다.

### Debian & Ubuntu

Ubuntu 또는 Debian의 경우 터미널에서 다음 명령어를 입력하여 설치한다.
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Fedora 40 기준으로, [RPM Fusion](https://rpmfusion.org/RPM%20Fusion)에서 제공하는 사전 빌드된 패키지를 다운로드하여 설치하는 방법을 소개한다.

#### 1-Fedora-1. RPM Fusion 리포지터리 구성

[RPM Fusion 공식 가이드](https://rpmfusion.org/Configuration)를 참고하여 진행한다.  
터미널에서 다음 명령을 실행한다.

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> DNF 구 버전(Fedora 40 및 그 이전 버전)에서는 둘째 줄의 openh264 라이브러리 저장소 활성화를 위한 명령줄이 다음과 같았다.
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> 그러나 DNF 5(Fedora 41+)에서부터는 위 명령줄 대신
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> 을 대신 입력해야 하며, 이를 반영해 본문 내용을 갱신하였다.
{: .prompt-info }

#### 1-Fedora-2. akmod-nvidia 패키지 설치

[RPM Fusion에서 제공하는 NVIDIA 드라이버 설치 가이드](https://rpmfusion.org/Howto/NVIDIA)를 참고하여, akmod-nvidia 패키지를 설치한다.

```bash
sudo dnf update  # 이 단계에서 만약 커널 업데이트가 있었다면, 최신 커널로 재부팅하고 나서 마저 진행한다
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> 마찬가지로, DNF 구 버전(Fedora 40 및 그 이전 버전)에서는 셋째 줄의 autoremove 시 NVIDIA 드라이버 삭제 방지를 위한 명령줄이 다음과 같았다.
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> 그러나 DNF 5(Fedora 41+)에서부터는 위 명령줄 대신
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> 을 대신 입력해야 하며, 이를 반영해 본문 내용을 갱신하였다.
{: .prompt-info }

> 한편, 과거 RPM Fusion은 [NVIDIA 오픈소스 커널 모듈](#proprietary-module-vs-open-source-module)에 대해 부정적인 입장을 보여 왔고 별도로 지정하지 않는 한 Proprietary 드라이버를 기본 제공했다. 그러나 [최근(12025년 12월) 변경된 RPM Fusion 측 지침](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open)에 따르면 이제 중복 지원 하드웨어(Turing부터 Blackwell 이전까지의 아키텍처)에 대해서 둘 중 더 나은 버전을 자동으로 선택해 제공할 것이며, 따라서 어떤 버전을 사용할지 직접 고를 필요가 없다고 한다. Turing 이전의 구형 아키텍처나, Blackwell 및 그 이후의 최신 아키텍처에 대해서는 원래부터 선택지가 하나뿐이었으므로 변경사항이 없다.
> 이에 따라 `/etc/rpm/macros.nvidia-kmod`를 통한 오픈소스 커널 모듈 사용 옵션 지정에 관한 내용이 삭제된 것을 확인하였다.
>
> 또한 `akmod-nvidia-open` 패키지의 경우, 커널 스페이스 드라이버에 다운스트림 변경사항을 직접 적용해야 하는 경우가 아니면 사용하지 말라고 한다.
>
> 위 사항들 역시 본문 내용에 새로 반영하였다.
{: .prompt-info }

#### 1-Fedora-3. 보안 부팅(Secure Boot) 시 드라이버 정상 로드를 위한 키 등록  

> 아래에서 설명하는 약간의 추가 절차만 거치면 정상적으로 보안 부팅 기능을 이용하면서 NVIDIA 그래픽 드라이버를 사용할 수 있으며, 보안 부팅 비활성화 시 시스템의 보안이 상당히 취약해지므로 해제하지 않는 것을 권한다. 적어도 12020년대에 접어든 이후로는 어지간해서는 보안 부팅을 해제할 이유가 없다.
{: .prompt-danger }

우선 다음 툴들을 설치한다.

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

다음으로, 아래 명령을 실행하여 키를 생성한다.

```bash
sudo kmodgenca -a
```

이제 UEFI펌웨어의 MOK에 생성한 키를 등록해야 한다.

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

위 명령을 실행하면 키 등록을 위한 패스워드를 입력하라고 뜰 것이다. 잠시 뒤에 키 등록 절차 완료를 위해 재부팅을 할 건데, 그때 사용할 일회용 패스워드이니 적당히 기억할 수 있는 것으로 입력한다.

이제 다음 명령을 실행하여 시스템을 재부팅한다.

```bash
systemctl reboot
```

시스템이 부팅되면서 자동으로 MOK 관리 창이 뜰 것이다. "Enroll MOK"를 선택한 뒤에 "Continue", "Yes"를 연달아 선택하면 좀 전에 설정한 패스워드를 요구하는 창이 뜬다. 앞서 설정했던 패스워드를 입력하고 나면 키 등록 절차가 완료된다. 이제 reboot를 입력하여 다시 부팅하면 정상적으로 NVIDIA 드라이버가 로드될 것이다.

### NVIDIA 드라이버 설치 확인

터미널에서 다음 명령을 실행하여 현재 로드된 NVIDIA 커널 모듈을 확인할 수 있다.

```bash
cat /proc/driver/nvidia/version
```

아래와 비슷한 형태의 메시지가 출력된다면 정상적으로 설치한 것이다.

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

또한 리눅스 진영에서 많은 경우 기본 채택하고 있는 오픈소스 그래픽 드라이버, nouveau 커널 모듈은 NVIDIA 드라이버 설치 후에는 비활성화되어야 하며 그렇지 않을 경우 문제를 야기할 수 있다. NVIDIA 드라이버를 설치하고 재부팅한 이후에는 다음 명령 실행 시 아무 내용도 출력되지 않아야 정상이다.

```bash
lsmod |grep nouveau
```

## 2. NVIDIA Container Toolkit 설치

이제 [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)을 설치해야 한다. [NVIDIA Container Toolkit 공식 설치 가이드](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)를 참고하여 설치를 진행하되, Fedora의 경우 설치 과정에서 유의사항이 있으므로 이 섹션의 내용을 끝까지 확인한 뒤 진행하기 바란다.

### Apt를 사용하는 경우 (Ubuntu, Debian 등)

#### 2-Apt-1. 패키지 다운로드를 위한 리포지터리 구성

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. 패키지 리스트 업데이트

```bash
sudo apt update
```

#### 2-Apt-3. 패키지 설치

```bash
sudo apt install nvidia-container-toolkit
```

### Yum 또는 Dnf를 사용하는 경우 (Fedora, RHEL, Centos 등)

> Fedora 40에서 테스트했을 때, Ubuntu에서와 달리 `nvidia-smi` 명령 및 `nvidia-persistenced` 패키지가 NVIDIA 그래픽 드라이버에 기본 포함되어 있지 않아 `xorg-x11-drv-nvidia-cuda` 패키지를 추가 설치해야 했다. RHEL 및 Centos에서는 직접 테스트해 보지 않았으나, Fedora와 시스템 구성이 매우 비슷한 편이므로 만약 아래 가이드대로 진행했을 때 문제가 발생한다면 같은 방법을 시도해 보는 것이 도움이 될 수도 있다.
{: .prompt-warning }

> Fedora 40에서 위 방법대로 `xorg-x11-drv-nvidia-cuda`를 설치하고 샘플 워크로드를 실행하여 테스트했을 때 내 시스템에서는 정상 동작하였다. 만약 SELinux 등의 이유로 여전히 문제가 발생한다면, Fedora의 AI-ML 그룹에서 제공하는 [Fedora 전용 nvidia-container-toolkit 패키지 및 가이드](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/)가 도움이 될 수도 있다.
{: .prompt-tip }

#### 2-Dnf-1. 패키지 다운로드를 위한 리포지터리 구성

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. 패키지 설치

```bash
sudo dnf install nvidia-container-toolkit
```

또는

```bash
sudo yum install nvidia-container-toolkit
```

### Zypper를 사용하는 경우 (openSUSE, SLES)

#### 2-Zypper-1. 패키지 다운로드를 위한 리포지터리 구성

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. 패키지 설치

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. 컨테이너 엔진 설치

다음으로는 컨테이너 엔진으로 Docker CE 또는 Podman을 설치한다. 사용 환경과 선호에 맞게 둘 중 하나를 선택하여 설치하면 되며, [Docker 공식 문서](https://docs.docker.com/engine/install/)와 [Podman 공식 문서](https://podman.io/docs/installation)를 참고한다.

다음 표는 Docker와 Podman의 주요 차이점 및 장단점을 정리한 것이다.

| 비교항목 | Docker | Podman |
| --- | --- | --- |
| 아키텍처 | 클라이언트-서버 모델, 데몬(daemon) 기반 | 데몬리스(daemonless) 구조 |
| 보안 | 기본적으로 root 권한으로 실행되는 데몬에 <br>의존하므로 잠재적인 보안상의 위험 존재<br>(12020년 발표된 버전 20.10부터 루트리스 <br>모드를 지원하나, 추가적인 설정 필요) | 데몬에 의존하지 않아 별도로 지정하지 않는 <br>한 기본적으로 루트리스로 작동하며,<br> SELinux로 보호받음 |
| 자원 사용량 | 데몬 기반 구조의 특성상 백그라운드 프로세스가<br> 상시 동작하므로, 일반적으로 더 많은 양의<br> 자원 사용 | 일반적으로 더 적은 자원 간접비용(overhead) |
| 컨테이너 시작 시간 | 상대적으로 느림 | 간소화된 아키텍처로 최대 50% 정도<br> 더 빠르게 실행됨 |
| 생태계 및 문서화 | 광범위한 생태계와 커뮤니티 지원,<br> 풍부한 관련 문서 | 상대적으로 소규모의 생태계와 관련 문서 |
| 네트워킹 | Docker Bridge Network 사용 | CNI(Container Network Interface)<br> 플러그인 사용 |
| Kubernetes YAML<br> 네이티브 지원 | X(변환 필요) | O |

참고 자료:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker는 그 역사가 더 오래되었으며 업계에서 사실상의 표준 지위를 누려 왔으므로 폭넓은 생태계와 풍부한 관련 문서가 존재한다는 것이 가장 큰 장점이다.  
Podman은 Red Hat에 의해 비교적 최근에 개발되었으며, 태생적으로 데몬리스(daemonless), 루트리스(rootless)를 지향하는 발전된 구조이기에 보안, 시스템 자원 사용량 및 컨테이너 시동 시간 등 여러 측면에서 장점을 지닌다. 데몬에 문제가 생겨 다운되면 모든 컨테이너들이 함께 다운되는 Docker와 달리, 각 컨테이너가 완전히 독립적이라 특정 컨테이너의 다운이 다른 컨테이너에 영향을 미치지 않는다는 점도 Podman의 강점이다.

각자의 주어진 여건에 맞추어 사용할 도구를 선택하는 것이 무엇보다 중요하나, 처음 입문하는 사용자라면 Podman으로 시작하는 것이 좋은 선택일 듯 싶다. Docker에 비해 상대적으로 생태계 규모가 작다고 하나 상술한 여러 장점들 덕에 빠른 속도로 성장하며 격차를 좁히고 있고, Dockerfile 문법이나 Docker 이미지, CLI(명령줄 인터페이스) 등 많은 부분에서 기존의 Docker와 호환된다. 기존에 이미 Docker 기반으로 대규모 시스템을 구축해 두어서 Podman을 채택하려면 큰 전환비용이 든다거나 하는 사유가 없다면, 처음부터 Podman을 채택하는 것이 합리적이다.

### Podman

대다수의 주요 리눅스 배포판의 시스템 기본 리포지터리에서 지원하므로 간단히 설치할 수 있다.

#### Ubuntu의 경우

```bash
sudo apt install podman
```

#### Fedora의 경우

```bash
sudo dnf install podman
```

#### openSUSE의 경우

```bash
sudo zypper install podman
```

#### 정상적으로 설정되었는지 확인

터미널에서 다음 명령을 실행해본다.

```bash
podman run --rm hello-world
```

아래와 같은 메시지가 출력되면 성공이다.

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

> 12025-12-18T00:43:00+09:00 시점에 podman 버전 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`, fedora 43 환경 기준으로 테스트했을 때, 위의 hello-world를 비롯하여 컨테이너 실행 또는 이미지 빌드 시 다음 에러가 발생하였다.
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> 현재 나는 IPv6는 사용하지 않으며 IPv4 네트워크 환경에 있음에도 불구하고, 컨테이너 네트워크 구성 단계에서 pasta(passt 라이브러리에 포함됨)가 IPv6 라우팅을 시도하여 발생하는 문제로 보인다. 컨테이너 실행이나 [후술할 이미지 빌드 단계](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-building-docker-image-and-running-container)에서 아래와 같이 `--net=pasta:-4` 옵션을 명시적으로 지정하여 IPv4를 사용하도록 하면 문제가 발생하지 않는 것을 확인하였다.
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> 찾아보니 [동일한 증상으로 이전에 등록된 이슈](https://github.com/containers/podman/issues/22824)가 존재했다. 해당 이슈는 [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/)에서 수정되었다고 하나, 관찰된 증상이 동일한 점, Proton VPN 사용 중 발생한 문제라는 점 등 많은 부분이 매우 유사하여 아마도 비슷한 이슈가 재발한 것이 아닐까 추측하고 있다.
{: .prompt-warning }

### Docker CE

#### Ubuntu의 경우

##### 3-Ubuntu-1. 패키지 충돌 방지를 위한 이전 버전 혹은 비공식 패키지 제거

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. 리포지터리 구성

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

##### 3-Ubuntu-3. 패키지 설치

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. `Docker` 그룹 생성하고 사용자 등록하기

non-root 사용자도 `sudo` 없이 Docker를 관리할 수 있게 하려면, `Docker` 그룹을 생성한 뒤 Docker를 이용하고자 하는 사용자를 등록하면 된다. 터미널에서 다음 명령을 실행한다.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

이후 로그아웃했다가 다시 로그인하면 변경된 설정이 적용된다. Ubuntu 또는 Debian의 경우, 별다른 작업 없이도 시스템 부팅 시마다 Docker 서비스가 자동으로 실행된다.

#### Fedora의 경우

##### 3-Fedora-1. 패키지 충돌 방지를 위한 이전 버전 혹은 비공식 패키지 제거

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

##### 3-Fedora-2. 리포지터리 구성

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. 패키지 설치

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

패키지 설치 과정에서 GPG 키를 승인할 것인지 알림이 뜰 것이다. GPG 키가 `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`과 일치한다면, y를 입력하여 승인하면 된다.  
> 만약 GPG 키가 일치하지 않을 경우, 공급망 공격에 의해 위조된 패키지를 다운로드한 것일 수 있으므로 설치를 중단해야 한다.
{: .prompt-danger }

##### 3-Fedora-4. Docker 데몬 시작

이제 Docker가 설치되었지만 실행되지 않은 상태이므로, 다음 명령어를 입력하여 Docker를 실행할 수 있다.

```bash
sudo systemctl start docker
```

시스템 부팅 시 Docker 서비스가 자동으로 실행되도록 하려면 다음 명령을 실행한다.

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. `Docker` 그룹에 사용자 등록하기

non-root 사용자도 Docker를 관리할 수 있도록 하려면 `Docker` 그룹에 Docker를 이용하고자 하는 사용자를 등록한다. Fedora의 경우 앞선 패키지 설치 과정에서 `Docker` 그룹을 자동으로 생성하므로, 사용자 등록만 진행하면 된다.

```bash
sudo usermod -aG docker $USER
```

이후 로그아웃했다가 다시 로그인하면 변경된 설정이 적용된다.

#### 정상적으로 설정되었는지 확인

터미널에서 다음 명령을 실행해본다.

```bash
docker run hello-world
```

아래와 같은 메시지가 출력되면 성공이다.

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
Continued in [Part 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
