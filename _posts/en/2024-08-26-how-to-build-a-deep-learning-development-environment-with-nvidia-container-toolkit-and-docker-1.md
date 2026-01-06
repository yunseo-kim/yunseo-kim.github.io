---
title: "Building a Deep Learning Development Environment with NVIDIA Container Toolkit and Docker/Podman (1) - Installing NVIDIA Container Toolkit & a Container Engine"
description: "Part 1 of a series on building a container-based deep learning environment with NVIDIA Container Toolkit and Docker/Podman, plus SSH and JupyterLab for remote use. This post covers installing the toolkit and the container engine."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Overview

In this series, we will install NVIDIA Container Toolkit and Docker or Podman, then build a deep learning development environment by writing a Dockerfile based on CUDA and cuDNN images provided by the [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda) on Docker Hub. For those who need it, I’m sharing the [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) and the resulting [image](https://hub.docker.com/r/yunseokim/dl-env/tags) via GitHub and Docker Hub, and I also provide an SSH and JupyterLab setup guide for using the environment as a remote server.  
This series is planned to consist of 3 posts, and the post you are reading is the first one.
- Part 1: Installing NVIDIA Container Toolkit & a Container Engine (this post)
- [Part 2: Configuring Container Runtime for GPU Utilization, Writing Dockerfile, and Building Container Images](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Part 3 (upcoming)

This guide assumes an x86_64 Linux environment with an NVIDIA graphics card that supports CUDA. Since I have not tested it directly on distributions other than Ubuntu or Fedora, some details may differ slightly.  
(Revised on 12026.1.6.)

### Development Environment Configuration

- Host OS & architecture: x86_64, Linux (Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Tech stack to be set up (languages & libraries)
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

  > Depending on the situation and your preferences, you may also consider using the [Polars](https://pola.rs/) DataFrame library instead of pandas. It’s written in Rust, and [while it falls short compared to the cuDF + pandas combination for large-scale data processing, it performs quite well compared to vanilla pandas packages](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), and provides syntax that is more specialized for queries. According to the official [Polars blog](https://pola.rs/posts/polars-on-gpu/) and the [cuDF documentation](https://docs.rapids.ai/api/cudf/stable/cudf_polars/), Polars and the NVIDIA RAPIDS team are collaborating to provide an open beta cuDF-based GPU acceleration engine, and development is progressing rapidly.
  {: .prompt-tip }

  > If you’re debating whether to use Docker CE or Podman, the [comparison table below](#3-installing-a-container-engine) may help.
  {: .prompt-tip }

### Comparison Table vs. My Previous Machine Learning Dev Environment Guide

A [machine learning development environment setup guide previously uploaded to this blog](/posts/Setting-up-a-Machine-Learning-Development-Environment) already exists, but I wrote this post anew due to several changes. The differences are summarized in the table below.

| Difference | Previous post (12021 version) | This post (written in 12024, revised in 12026) |
| --- | --- | --- |
| Linux distributions | Based on Ubuntu | Applicable not only to Ubuntu but also <br> Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Setup approach | Install directly on the host system<br>Python virtual env with venv | Docker container-based environment using<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br> Python virtual env & package management using uv |
| NVIDIA graphics driver installation | O | O |
| Install CUDA & cuDNN directly on the host system | O (using Apt package manager) | X (uses prebuilt images provided by NVIDIA on<br> [Docker Hub](https://hub.docker.com/r/nvidia/cuda), so no manual installation needed) |
| Portability | Must rebuild the dev environment<br>whenever migrating to another system | Since it’s Docker-based, you can<br> build new images as needed from a prepared Dockerfile, or<br> easily migrate an existing image (excluding extra volumes or network settings) |
| Using additional GPU-accelerated libraries beyond cuDNN | X | Introduces [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), and [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook interface | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH server setup | Not covered | Includes basic SSH server setup |

## 0. Prerequisites / Things to Check

- [NVIDIA Container Toolkit can be used on Linux distributions that support the Apt, Yum or Dnf, and Zypper package managers.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) You can check the list of supported Linux distributions on the linked page. Fedora is not explicitly listed in the official support table, but since it is also based on Red Hat Linux like RHEL, it works without issues. If you’re not familiar with Linux and aren’t sure which distribution to choose, Ubuntu LTS is generally the safest choice. Even proprietary (non-open-source) drivers can be installed automatically, making it relatively beginner-friendly, and since it has a large user base, most technical documentation is written with Ubuntu in mind.
  - You can check your system architecture and Linux distribution version in a terminal with `uname -m && cat /etc/*release`.
- First, verify that the GPU installed in your system supports the CUDA and cuDNN versions you intend to use.
  - You can check the GPU model installed in your computer in a terminal with `lspci | grep -i nvidia`.
  - On <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, check (by cuDNN version) the **supported NVIDIA graphics driver versions**, the required **CUDA Compute Capability** conditions, and the list of **supported NVIDIA hardware**.
  - Find your model in the GPU list at <https://developer.nvidia.com/cuda-gpus>, then check its **Compute Capability** value. This value must satisfy the **CUDA Compute Capability** requirement you checked above to use CUDA and cuDNN without issues.

> If you’re planning to buy a new GPU for deep learning workloads, the following post summarizes GPU selection criteria well. The author updates it intermittently.  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> If you also need a guide for overall hardware configuration (beyond just the GPU), the same author’s post [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) is also very useful.
{: .prompt-tip }

If you meet all of the requirements mentioned above, let’s start setting up the working environment.

## 1. Installing the NVIDIA Graphics Driver

First, you must install the NVIDIA graphics driver on the host system. You can download and use the `.run` installer from the [NVIDIA driver download page](https://www.nvidia.com/drivers/), but if possible, it’s better to install via your system’s package manager for easier version management and maintenance. Refer to the official documentation at <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> to install a graphics driver suitable for your system environment.

### Proprietary Module vs Open-Source Module

The NVIDIA Linux driver consists of several kernel modules, and starting with driver version 515 and later releases, NVIDIA provides two types of driver kernel modules.

- Proprietary: the proprietary software driver NVIDIA has traditionally provided.
- Open-source: an open-source driver provided under a dual MIT/GPLv2 license. The source code is available via <https://github.com/NVIDIA/open-gpu-kernel-modules>.

The proprietary driver is provided for GPUs based on architectures from Maxwell up to (but not including) Blackwell, and it is planned to be discontinued starting with the Blackwell architecture.  
In contrast, the open-source driver is supported for Turing and later architectures.

[NVIDIA recommends using the open-source kernel modules if possible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
You can check whether your GPU is compatible with the open-source driver at [this link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

In this post, I will assume you are installing the open-source driver.

### Debian & Ubuntu

For Ubuntu or Debian, run the following commands in a terminal:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Based on Fedora 40, this section introduces how to download and install prebuilt packages provided by [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configure RPM Fusion Repositories

Proceed by referring to the [RPM Fusion official guide](https://rpmfusion.org/Configuration).  
Run the following commands in a terminal.

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> In older versions of DNF (Fedora 40 and earlier), the command line to enable the openh264 library repository on the second line was:
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> However, starting from DNF 5 (Fedora 41+), you must use:
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> I updated the post accordingly.
{: .prompt-info }

#### 1-Fedora-2. Install the akmod-nvidia Package

Refer to the [NVIDIA driver installation guide provided by RPM Fusion](https://rpmfusion.org/Howto/NVIDIA), and install the akmod-nvidia package.

```bash
sudo dnf update  # If there was a kernel update at this step, reboot into the latest kernel and then continue
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> Likewise, in older versions of DNF (Fedora 40 and earlier), the command on the third line to prevent the NVIDIA driver from being removed by autoremove was:
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> However, starting from DNF 5 (Fedora 41+), you must use:
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> I updated the post accordingly.
{: .prompt-info }

> Meanwhile, RPM Fusion had historically taken a negative stance on the [NVIDIA open-source kernel modules](#proprietary-module-vs-open-source-module) and, unless explicitly specified, provided the proprietary driver by default. However, according to [recent RPM Fusion guideline changes (December 12025)](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), for overlap-supported hardware (architectures from Turing up to pre-Blackwell), they will now automatically select and provide the better option between the two, so you no longer need to choose manually. For older architectures prior to Turing, and for the newest architectures (Blackwell and later), there was only one option to begin with, so nothing changes there.
> Accordingly, I confirmed that the content about specifying the open-source kernel module option via `/etc/rpm/macros.nvidia-kmod` has been removed.
>
> Also, for the `akmod-nvidia-open` package, they advise not to use it unless you specifically need to apply downstream changes directly to the kernel-space driver.
>
> I incorporated these points into the post as well.
{: .prompt-info }

#### 1-Fedora-3. Register a Key so the Driver Loads Properly with Secure Boot Enabled  

> With just a small amount of additional work as described below, you can use the NVIDIA graphics driver while keeping Secure Boot enabled. Since disabling Secure Boot significantly weakens system security, I recommend not turning it off. At least since entering the 12020s, there’s rarely a good reason to disable Secure Boot.
{: .prompt-danger }

First, install the following tools.

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Next, generate a key by running the command below.

```bash
sudo kmodgenca -a
```

Now you need to enroll the generated key into the UEFI firmware’s MOK.

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

After running the command above, you will be prompted to enter a password for key enrollment. Shortly, you will reboot to complete the enrollment process; this password is a one-time password for that step, so enter something you can remember.

Now reboot the system with the following command.

```bash
systemctl reboot
```

During boot, the MOK management screen will appear automatically. Select “Enroll MOK”, then select “Continue” and “Yes” in sequence, and you’ll see a prompt asking for the password you set earlier. After entering it, key enrollment will be completed. Enter “reboot” to boot again, and the NVIDIA driver should load normally.

### Verify NVIDIA Driver Installation

In a terminal, you can check the currently loaded NVIDIA kernel module with the following command.

```bash
cat /proc/driver/nvidia/version
```

If you see output similar to the following, it has been installed correctly.

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

Also, in many Linux distributions, the open-source graphics driver `nouveau` kernel module is used by default. After installing the NVIDIA driver, `nouveau` should be disabled; otherwise it may cause issues. After installing the NVIDIA driver and rebooting, running the following command should produce no output.

```bash
lsmod |grep nouveau
```

## 2. Installing NVIDIA Container Toolkit

Next, you need to install [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Follow the [official NVIDIA Container Toolkit installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), but for Fedora, there are a few notes to be aware of—so read this entire section before proceeding.

### If Using Apt (Ubuntu, Debian, etc.)

#### 2-Apt-1. Configure the Repository for Package Downloads

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Update Package Lists

```bash
sudo apt update
```

#### 2-Apt-3. Install the Package

```bash
sudo apt install nvidia-container-toolkit
```

### If Using Yum or Dnf (Fedora, RHEL, Centos, etc.)

> When I tested on Fedora 40, unlike Ubuntu, the `nvidia-smi` command and the `nvidia-persistenced` package were not included in the NVIDIA graphics driver by default, so I had to additionally install the `xorg-x11-drv-nvidia-cuda` package. I haven’t tested directly on RHEL or Centos, but since their system configuration is quite similar to Fedora, if you run into issues when following the guide below, trying the same approach may help.
{: .prompt-warning }

> On my system, after installing `xorg-x11-drv-nvidia-cuda` on Fedora 40 as described above and testing by running the sample workload, everything worked normally. If issues still occur due to SELinux or other reasons, the [Fedora-specific nvidia-container-toolkit package and guide](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) provided by Fedora’s AI-ML group may also help.
{: .prompt-tip }

#### 2-Dnf-1. Configure the Repository for Package Downloads

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Install the Package

```bash
sudo dnf install nvidia-container-toolkit
```

Or:

```bash
sudo yum install nvidia-container-toolkit
```

### If Using Zypper (openSUSE, SLES)

#### 2-Zypper-1. Configure the Repository for Package Downloads

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Install the Package

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installing a Container Engine

Next, install either Docker CE or Podman as the container engine. Choose whichever fits your environment and preferences, and refer to the [official Docker documentation](https://docs.docker.com/engine/install/) and the [official Podman documentation](https://podman.io/docs/installation).

The table below summarizes key differences, pros, and cons between Docker and Podman.

| Comparison Item | Docker | Podman |
| --- | --- | --- |
| Architecture | Client-server model; daemon-based | Daemonless architecture |
| Security | Depends on a daemon that runs as root by default, <br> which poses potential security risks<br>(supports rootless mode since v20.10 released in 12020, but requires additional setup) | Does not depend on a daemon; operates rootless <br>by default unless specified otherwise,<br> protected by SELinux |
| Resource usage | Because a background process runs constantly <br> due to the daemon-based design, it generally uses more resources | Generally lower overhead |
| Container startup time | Relatively slower | Up to ~50% faster due to <br> simplified architecture |
| Ecosystem & documentation | Extensive ecosystem and community support,<br> abundant documentation | Relatively smaller ecosystem and less documentation |
| Networking | Uses Docker Bridge Network | Uses CNI (Container Network Interface) plugins |
| Native support for Kubernetes YAML | X (conversion required) | O |

References:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker has a longer history and has effectively held the de facto standard position in the industry, so its biggest advantage is the broad ecosystem and abundant documentation.  
Podman, developed more recently by Red Hat, has a more advanced architecture that is inherently daemonless and rootless, offering advantages in multiple areas such as security, system resource usage, and container startup time. Another strength of Podman is that, unlike Docker (where a daemon failure can bring down all containers together), each container is fully independent, so a failure of one container does not affect others.

Choosing the tool that best fits your circumstances is the most important thing, but if you’re a beginner, starting with Podman may be a good choice. While its ecosystem is smaller than Docker’s, it’s growing rapidly thanks to the advantages mentioned above, and it is compatible with Docker in many aspects, including Dockerfile syntax, Docker images, and the CLI (command-line interface). Unless you already have large-scale systems built around Docker and would incur high migration costs to adopt Podman, choosing Podman from the start is a reasonable approach.

### Podman

Since it is supported in the default repositories of most major Linux distributions, you can install it easily.

#### On Ubuntu

```bash
sudo apt install podman
```

#### On Fedora

```bash
sudo dnf install podman
```

#### On openSUSE

```bash
sudo zypper install podman
```

#### Verify it’s set up correctly

Run the following command in a terminal.

```bash
podman run --rm hello-world
```

If you see output like the following, it worked.

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

> When I tested on Fedora 43 with podman version 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`, at 12025-12-18T00:43:00+09:00, the following error occurred when running containers or building images, including the hello-world example above:
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> Even though I’m not using IPv6 and I’m on an IPv4 network, it seems that during container network setup, pasta (included in the passt library) attempts IPv6 routing and triggers this issue. I confirmed that explicitly specifying the `--net=pasta:-4` option to force IPv4, as shown below, avoids the problem both when running containers and during the [image build step described later](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-building-docker-image-and-running-container).
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> I found that a [previous issue with the same symptom](https://github.com/containers/podman/issues/22824) exists. That issue was said to be fixed in [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/), but given that the observed symptom is identical and that the issue occurred while using Proton VPN, among other similarities, I suspect a similar issue may have resurfaced.
{: .prompt-warning }

### Docker CE

#### On Ubuntu

##### 3-Ubuntu-1. Remove old versions or unofficial packages to prevent conflicts

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configure the repository

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

##### 3-Ubuntu-3. Install packages

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Create the `Docker` group and add your user

To allow a non-root user to manage Docker without `sudo`, create the `Docker` group and add the user who will use Docker. Run the following commands in a terminal.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Log out and log back in to apply the changes. On Ubuntu or Debian, Docker services will start automatically on each boot without additional steps.

#### On Fedora

##### 3-Fedora-1. Remove old versions or unofficial packages to prevent conflicts

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

##### 3-Fedora-2. Configure the repository

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Install packages

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

During installation, you will be prompted to approve the GPG key. If the GPG key matches `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, enter `y` to approve it.  
> If the GPG key does not match, it may indicate a supply-chain attack with tampered packages, so you must stop the installation.
{: .prompt-danger }

##### 3-Fedora-4. Start the Docker daemon

Docker is installed at this point but not running yet, so start it with the command below.

```bash
sudo systemctl start docker
```

To start Docker automatically at boot, run:

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Add your user to the `Docker` group

To allow a non-root user to manage Docker, add the user who will use Docker to the `Docker` group. On Fedora, the `Docker` group is automatically created during package installation, so you only need to add the user.

```bash
sudo usermod -aG docker $USER
```

Log out and log back in to apply the changes.

#### Verify it’s set up correctly

Run the following command in a terminal.

```bash
docker run hello-world
```

If you see output like the following, it worked.

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
