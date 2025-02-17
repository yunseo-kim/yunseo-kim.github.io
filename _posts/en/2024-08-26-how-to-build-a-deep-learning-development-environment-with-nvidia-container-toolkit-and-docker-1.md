---
title: Building a Deep Learning Development Environment with NVIDIA Container Toolkit and Docker/Podman (1) - Installing NVIDIA Container Toolkit & Container Engine
description: This series covers setting up a container-based deep learning development environment locally using NVIDIA Container Toolkit, and configuring SSH and Jupyter Lab for remote server use. This post, the first in the series, introduces the installation methods for NVIDIA Container Toolkit and container engines.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Overview
This series covers the process of installing NVIDIA Container Toolkit and Docker or Podman, writing a Dockerfile based on CUDA and cuDNN images provided by the [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda) on Docker Hub, and building a deep learning development environment. For those who need it, I share the [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) and [image](https://hub.docker.com/r/yunseokim/dl-env/tags) completed through this process on GitHub and Docker Hub for free use, and additionally provide a guide for SSH and Jupyter Lab setup for remote server use.  
The series will consist of 3 posts, and this post you're reading is the first in the series.
- Part 1: Installing NVIDIA Container Toolkit & Container Engine (This post)
- [Part 2: Configuring Container Runtime for GPU Utilization, Writing Dockerfile and Building Container Image](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Part 3 (Upcoming)

We proceed assuming an x86_64 Linux environment with an NVIDIA graphics card supporting CUDA installed, and while some specific details may differ slightly for distributions other than Ubuntu or Fedora, as I haven't directly tested them.  
(Content updated on 2025.02.18)

### Development Environment Configuration
- Host OS and Architecture: x86_64, Linux environment (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Technology stack to be built (languages and libraries)
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

  > Depending on the situation and personal preference, you might consider using the [Polars](https://pola.rs/) DataFrame library instead of pandas. Written in Rust, it [shows quite impressive performance compared to the vanilla pandas package, although it falls behind the cuDF + pandas combination when processing large-scale data](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), and provides a more query-specialized syntax. According to the [Polars official blog](https://pola.rs/posts/polars-on-gpu/), they plan to support integration with cuDF in the near future in collaboration with the NVIDIA RAPIDS team.
  {: .prompt-tip }

  > If you're unsure whether to use Docker CE or Podman, the [comparison table below](#3-installing-container-engine) might be helpful.
  {: .prompt-tip }

### Comparison with Previously Written Machine Learning Development Environment Setup Guide
There's already [a machine learning development environment setup guide uploaded to this blog](/posts/Setting-up-a-Machine-Learning-Development-Environment), which is still mostly valid, but there are some changes, so I wrote this new post. The differences are summarized in the table below.

| Difference | Previous Post (2021 Version) | This Post (2024 Version) |
| --- | --- | --- |
| Linux Distribution | Based on Ubuntu | Applicable to Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc., besides Ubuntu |
| Development Environment<br> Setup Method | Python virtual environment using venv | Docker container-based environment using<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| NVIDIA Graphics Driver Installation | O | O |
| Direct Installation of CUDA and<br> cuDNN on Host System | O (Using Apt package manager) | X (Using pre-installed images provided by NVIDIA<br> from Docker Hub, so no direct work needed) |
| Portability | Need to rebuild development environment<br> every time when moving to another system | Docker-based, so can easily build new images<br> with prepared Dockerfile or port existing images<br> (excluding additional volumes or network settings)<br> when needed |
| Utilization of Additional GPU<br> Acceleration Libraries besides cuDNN | X | Introduction of [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook Interface | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH Server Configuration | Not covered separately | Includes basic SSH server configuration setup in Part 3 |

If you want to use Python virtual environments like venv instead of Docker, the [previous post](/posts/Setting-up-a-Machine-Learning-Development-Environment) is still valid, so I recommend referring to that post.

## 0. Prerequisites
- [NVIDIA Container Toolkit is available on Linux distributions that support Apt, Yum or Dnf, Zypper package managers.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) You can check the list of supported Linux distributions on the linked page, and although not specifically listed in the official support table, Fedora can also be used without issues as it's based on Red Hat Linux like RHEL. If you're not familiar with Linux environments and aren't sure which distribution to use, using the Ubuntu LTS version is the most straightforward option. It's relatively convenient for beginners as non-open source proprietary drivers are automatically installed, and most technical documentation is written based on Ubuntu due to its large user base.
  - You can check your system architecture and Linux distribution version by running the `uname -m && cat /etc/*release` command in the terminal.
- First, you need to check if the graphics card installed in your system supports the CUDA and cuDNN versions you want to use.
  - You can check the GPU model name installed in your current computer with the `lspci | grep -i nvidia` command in the terminal.
  - On the <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> page, check the **supported NVIDIA graphics driver versions**, required **CUDA Compute Capability** conditions, and the list of **supported NVIDIA hardware** for each cuDNN version.
  - Find the corresponding model name in the GPU list at <https://developer.nvidia.com/cuda-gpus>, and check the **Compute Capability** value. This value must meet the **CUDA Compute Capability** condition checked earlier to use CUDA and cuDNN without issues.

> If you're planning to purchase a new graphics card for deep learning tasks, the following article summarizes the GPU selection criteria well. The author continuously updates this article.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> Another article by the same author, [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/), is also very informative.
{: .prompt-tip }

If all the above-mentioned conditions are met, let's start setting up the work environment.

## 1. Installing NVIDIA Graphics Driver
First, you need to install the NVIDIA graphics driver on your host system. You can download and use the .run installer from the [NVIDIA driver download page](https://www.nvidia.com/drivers/), but it's better to use your system's package manager for installation in terms of version management and maintenance. Refer to the official document <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> to install the graphics driver suitable for your system environment.

### Proprietary module vs Open-source module
NVIDIA Linux drivers consist of several kernel modules, and from driver version 515 and later releases, NVIDIA provides two types of driver kernel modules.

- Proprietary: The proprietary software driver that NVIDIA has been providing.
- Open-source: Open-source driver provided under MIT/GPLv2 dual license. Source code is publicly available through <https://github.com/NVIDIA/open-gpu-kernel-modules>.

Proprietary drivers are provided for GPUs based on architectures from Maxwell to pre-Blackwell, and will be discontinued from the Blackwell architecture.
On the other hand, open-source drivers are supported for Turing and later architectures.

[NVIDIA recommends using the open-source kernel module if possible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
You can check if your GPU is compatible with the open-source driver at [this link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

This guide assumes installing the open-source driver.

### Debian & Ubuntu
For Ubuntu or Debian, enter the following commands in the terminal to install:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Based on Fedora 40, we introduce the method of downloading and installing pre-built packages provided by [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuring RPM Fusion Repository  
Refer to the [RPM Fusion official guide](https://rpmfusion.org/Configuration) to proceed.  
Execute the following command in the terminal:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Installing akmod-nvidia-open Package  
Referring to the [NVIDIA driver installation guide provided by RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), 
activate the rpmfusion-nonfree-tainted repository and then install the akmod-nvidia-open package.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Registering Key for Normal Driver Loading during Secure Boot  

> By following the additional procedures explained below, you can normally use the NVIDIA graphics driver while using the secure boot function, and it is recommended not to disable secure boot as the system's security becomes quite vulnerable when it is disabled. At least since entering the 2020s, there's hardly any reason to disable secure boot.
{: .prompt-danger }

First, install the following tools:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Next, run the following command to generate a key:
```bash
sudo kmodgenca -a
```
Now you need to register the generated key in the MOK of the UEFI firmware.
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
When you run the above command, you will be prompted to enter a password for key registration. We're going to reboot soon to complete the key registration process, so enter something you can remember as it's a one-time password you'll use then.

Now run the following command to reboot the system:
```bash
systemctl reboot
```
As the system boots, the MOK management window will automatically appear. Select "Enroll MOK", then select "Continue" and "Yes" in succession, and a window will appear asking for the password you set earlier. Enter the password you set earlier, and the key registration process will be completed. Now if you enter reboot to boot again, the NVIDIA driver will be loaded normally.

### Verifying NVIDIA Driver Installation
You can check the currently loaded NVIDIA kernel module by running the following command in the terminal:
```bash
cat /proc/driver/nvidia/version
```
If a message similar to the following is output, it has been installed correctly:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Installing NVIDIA Container Toolkit
Now you need to install the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Proceed with the installation referring to the [NVIDIA Container Toolkit official installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), but for Fedora, there are some precautions during the installation process, so please check the contents of this section to the end before proceeding.

### For Apt users (Ubuntu, Debian, etc.)
#### 2-Apt-1. Configuring Repository for Package Download
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Updating Package List
```bash
sudo apt update
```

#### 2-Apt-3. Installing Package
```bash
sudo apt install nvidia-container-toolkit
```

### For Yum or Dnf users (Fedora, RHEL, Centos, etc.)
> When tested on Fedora 40, unlike Ubuntu, the `nvidia-smi` command and `nvidia-persistenced` package were not included by default in the NVIDIA graphics driver, so the `xorg-x11-drv-nvidia-cuda` package had to be additionally installed. I haven't directly tested on RHEL and Centos, but as their system configurations are very similar to Fedora, if you encounter issues when proceeding as per the guide below, trying the same method might be helpful.
{: .prompt-warning }

> When installing `xorg-x11-drv-nvidia-cuda` as above and running a sample workload to test on Fedora 40, it worked normally on the author's system. If you still encounter issues due to SELinux or other reasons, the [Fedora-specific nvidia-container-toolkit package and guide](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) provided by Fedora's AI-ML group might be helpful.
{: .prompt-tip }

#### 2-Dnf-1. Configuring Repository for Package Download
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Installing Package
```bash
sudo dnf install nvidia-container-toolkit
```
or
```bash
sudo yum install nvidia-container-toolkit
```

### For Zypper users (openSUSE, SLES)
#### 2-Zypper-1. Configuring Repository for Package Download
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Installing Package
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installing Container Engine
Next, install Docker CE or Podman as the container engine. You can choose and install one of the two according to your usage environment and preference, referring to the [Docker official documentation](https://docs.docker.com/engine/install/) and [Podman official documentation](https://podman.io/docs/installation).

The following table summarizes the main differences and pros and cons of Docker and Podman.

| Comparison Item | Docker | Podman |
| --- | --- | --- |
| Architecture | Client-server model, daemon-based | Daemonless structure |
| Security | Potential security risks due to reliance on<br> daemon running with root privileges by default<br>(Rootless mode supported from version 20.10<br> released in 2020, but requires additional setup) | Does not rely on daemon, operates rootless by<br> default unless specifically designated, and<br> protected by SELinux |
| Resource Usage | Generally uses more resources due to<br> background processes always running<br> in daemon-based structure | Generally less resource overhead |
| Container Start Time | Relatively slow | Up to 50% faster execution with<br> simplified architecture |
| Ecosystem and Documentation | Extensive ecosystem and community support,<br> abundant related documentation | Relatively smaller ecosystem and<br> related documentation |
| Networking | Uses Docker Bridge Network | Uses CNI (Container Network Interface) plugin |
| Kubernetes YAML<br> Native Support | X (Conversion needed) | O |

Reference materials:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker's biggest advantage is its extensive ecosystem and abundant related documentation due to its longer history and de facto standard status in the industry.  
Podman was developed relatively recently by Red Hat, and inherently aims for daemonless and rootless structure, thus having advantages in several aspects such as security, system resource usage, and container start time. Unlike Docker where all containers go down together when the daemon has a problem and goes down, each container in Podman is completely independent, so the downtime of a specific container does not affect other containers, which is also a strength of Podman.

It's most important to choose a tool that fits your given conditions, and for individual users just starting out, starting with Podman might be a good choice. Although its ecosystem is relatively smaller compared to Docker, it's rapidly growing and narrowing the gap thanks to the aforementioned advantages, and since it's compatible with Docker in many aspects such as Dockerfile syntax, Docker images, and CLI (Command Line Interface), it shouldn't be much of an issue for individuals or small groups.

### Podman
It can be easily installed as it's supported in the system default repositories of most major Linux distributions.

#### For Ubuntu
```bash
sudo apt install podman
```

#### For Fedora
```bash
sudo dnf install podman
```

#### For openSUSE
```bash
sudo zypper install podman
```

### Docker CE
#### For Ubuntu
##### 3-Ubuntu-1. Removing Previous Versions or Unofficial Packages to Prevent Package Conflicts
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configuring Repository
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

##### 3-Ubuntu-3. Installing Package
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Creating `Docker` Group and Registering User
To allow non-root users to manage Docker without `sudo`, you can create a `Docker` group and register users who want to use Docker. Run the following commands in the terminal:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
After logging out and logging back in, the changed settings will be applied. For Ubuntu or Debian, the Docker service automatically runs at system boot without any additional work.

#### For Fedora
##### 3-Fedora-1. Removing Previous Versions or Unofficial Packages to Prevent Package Conflicts
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

##### 3-Fedora-2. Configuring Repository
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Installing Package
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
During the package installation process, you will be asked whether to approve the GPG key. If the GPG key matches `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, enter y to approve.  
> If the GPG key does not match, you may have downloaded a forged package due to a supply chain attack, so you should stop the installation.
{: .prompt-danger }

##### 3-Fedora-4. Starting Docker Daemon
Now Docker is installed but not running, so you can start Docker by entering the following command:
```bash
sudo systemctl start docker
```
To have the Docker service run automatically at system boot, execute the following commands:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Registering User to `Docker` Group
To allow non-root users to manage Docker, register users who want to use Docker to the `Docker` group. In the case of Fedora, the `Docker` group is automatically created during the previous package installation process, so you only need to proceed with user registration.
```bash
sudo usermod -aG docker $USER
```
After logging out and logging back in, the changed settings will be applied.

#### Verifying Correct Setup
Try running the following command in the terminal:
```bash
docker run hello-world
```
If you see a message like the one below, it's successful:

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
