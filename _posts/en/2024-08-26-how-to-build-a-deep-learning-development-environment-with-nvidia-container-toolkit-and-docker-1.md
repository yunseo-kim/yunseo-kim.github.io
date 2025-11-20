---
title: Building a Deep Learning Development Environment with NVIDIA Container Toolkit and Docker/Podman (1) - Installing NVIDIA Container Toolkit & Container Engine
description: This series covers setting up a container-based deep learning development environment using NVIDIA Container Toolkit, and configuring SSH and Jupyter Lab for remote server use. This post, the first in the series, introduces the installation of NVIDIA Container Toolkit and container engines.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---
## Overview
This series covers installing NVIDIA Container Toolkit with Docker or Podman, and building a deep learning development environment by writing a Dockerfile based on CUDA and cuDNN images provided by the [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda) on Docker Hub. For those who need it, I'm sharing the completed [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) and [image](https://hub.docker.com/r/yunseokim/dl-env/tags) through GitHub and Docker Hub, along with a guide for SSH and Jupyter Lab setup for remote server use.  
The series will consist of 3 posts, and this is the first post in the series.
- Part 1: Installing NVIDIA Container Toolkit & Container Engine (this post)
- [Part 2: Configuring Container Runtime for GPU Utilization, Writing Dockerfile and Building Container Image](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Part 3 (coming soon)

This guide assumes you're using an x86_64 Linux environment with an NVIDIA graphics card that supports CUDA. While I've primarily tested on Ubuntu and Fedora, there may be slight differences in some details for other distributions.  
(Updated on 12025.02.18)

### Development Environment Configuration
- Host OS and architecture: x86_64, Linux environment (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Technology stack to build (languages and libraries)
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

  > Depending on your situation and preferences, you might consider using the [Polars](https://pola.rs/) DataFrame library instead of pandas. Written in Rust, it [shows impressive performance compared to pure pandas (though not quite matching cuDF + pandas)](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), and provides query-specialized syntax. According to the [Polars official blog](https://pola.rs/posts/polars-on-gpu/), they're working with the NVIDIA RAPIDS team to support cuDF integration in the near future.
  {: .prompt-tip }

  > If you're undecided between Docker CE and Podman, the [comparison table below](#3-installing-container-engine) might help.
  {: .prompt-tip }

### Comparison with Previous Machine Learning Environment Setup Guide
I've previously uploaded a [machine learning development environment setup guide](/posts/Setting-up-a-Machine-Learning-Development-Environment) on this blog, which is still mostly valid, but there are some changes that prompted me to write this new post. The differences are summarized in the table below:

| Difference | Previous Post (12021 version) | This Post (12024 version) |
| --- | --- | --- |
| Linux Distribution | Ubuntu-based | Applicable to Ubuntu, Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Development Environment Setup Method | Python virtual environment using venv | Container-based environment using<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| NVIDIA Graphics Driver Installation | O | O |
| Direct Installation of CUDA and<br> cuDNN on Host System | O (Using Apt package manager) | X (Using pre-installed images provided by NVIDIA<br> from Docker Hub, so no direct work needed) |
| Portability | Need to rebuild development environment<br> when moving to another system | Docker-based, so you can easily build new images<br> with your prepared Dockerfile or port existing<br> images (excluding additional volumes or<br> network settings) |
| Additional GPU Acceleration<br> Libraries Beyond cuDNN | X | Introducing [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/),<br> [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Jupyter Notebook Interface | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| SSH Server Configuration | Not covered | Basic SSH server configuration included in Part 3 |

If you prefer using Python virtual environments like venv instead of Docker, the [previous post](/posts/Setting-up-a-Machine-Learning-Development-Environment) is still valid and recommended.

## 0. Prerequisites
- [NVIDIA Container Toolkit is available for Linux distributions that support Apt, Yum or Dnf, and Zypper package managers.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) You can check the list of supported Linux distributions at the linked page. Although not specifically listed in the official support table, Fedora also works fine as it's based on Red Hat Linux. If you're not familiar with Linux environments and aren't sure which distribution to use, Ubuntu LTS is a safe choice. It automatically installs proprietary drivers, making it relatively convenient for beginners, and most technical documentation is written with Ubuntu in mind due to its large user base.
  - You can check your system architecture and Linux distribution version by running `uname -m && cat /etc/*release` in the terminal.
- First, verify that your graphics card supports the CUDA and cuDNN versions you want to use.
  - You can check the GPU model installed in your computer by running `lspci | grep -i nvidia` in the terminal.
  - Check the <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> page to see the **supported NVIDIA graphics driver versions**, required **CUDA Compute Capability** conditions, and **supported NVIDIA hardware** list for each cuDNN version.
  - Find your model in the GPU list at <https://developer.nvidia.com/cuda-gpus> and check its **Compute Capability** value. This value must meet the **CUDA Compute Capability** requirements identified earlier to use CUDA and cuDNN without issues.

> If you're planning to purchase a new graphics card for deep learning work, the following article provides well-organized selection criteria. The author keeps this article updated regularly.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> Another article by the same author, [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/), is also very informative.
{: .prompt-tip }

Once you've confirmed all the requirements above, let's start building the environment.

## 1. Installing NVIDIA Graphics Driver
First, you need to install the NVIDIA graphics driver on your host system. You can download and use the .run installer from the [NVIDIA driver download page](https://www.nvidia.com/drivers/), but it's better to use your system's package manager for version management and maintenance. Refer to the official documentation at <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> to install the appropriate graphics driver for your system.

### Proprietary module vs Open-source module
NVIDIA Linux drivers consist of several kernel modules, and since driver version 515 and later releases, NVIDIA provides two types of driver kernel modules:

- Proprietary: The traditional proprietary software driver that NVIDIA has been providing.
- Open-source: An open-source driver provided under dual MIT/GPLv2 license. Source code is available at <https://github.com/NVIDIA/open-gpu-kernel-modules>.

The proprietary driver is provided for GPUs based on Maxwell architecture through pre-Blackwell architectures and will be discontinued for Blackwell architecture and beyond.
The open-source driver supports Turing and later architectures.

[NVIDIA recommends using the open-source kernel module when possible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
You can check if your GPU is compatible with the open-source driver at [this link](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

This guide assumes you're installing the open-source driver.

### Debian & Ubuntu
For Ubuntu or Debian, enter the following commands in the terminal to install:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
For Fedora 40, I'll introduce the method of downloading and installing pre-built packages provided by [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuring RPM Fusion Repository  
Refer to the [RPM Fusion official guide](https://rpmfusion.org/Configuration).  
Run the following command in the terminal:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Installing akmod-nvidia-open Package  
Referring to the [NVIDIA driver installation guide provided by RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), 
activate the rpmfusion-nonfree-tainted repository and then install the akmod-nvidia-open package:
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark user akmod-nvidia-open
```

> In older DNF versions (Fedora 40 and earlier), the command on the last line to prevent the NVIDIA driver from being removed by autoremove was as follows:
>
> ```bash
> sudo dnf mark install akmod-nvidia-open
> ```
>
> However, starting with DNF 5 (Fedora 41+), you must enter
>
> ```bash
> sudo dnf mark user akmod-nvidia-open
> ```
>
> instead of the above command. The main text has been updated to reflect this.
{: .prompt-tip }

#### 1-Fedora-3. Registering Keys for Driver Loading with Secure Boot Enabled  

> With just a few additional steps described below, you can use NVIDIA graphics drivers normally with Secure Boot enabled. Since disabling Secure Boot makes your system significantly more vulnerable, it's recommended not to disable it. There's rarely a reason to disable Secure Boot, at least since the 12020s.
{: .prompt-danger }

First, install the following tools:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Next, run the following command to generate keys:
```bash
sudo kmodgenca -a
```
Now you need to register the generated key in the UEFI firmware's MOK:
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
When you run this command, you'll be prompted to enter a password for key registration. This is a one-time password you'll use when rebooting to complete the key registration process, so enter something you can remember.

Now run the following command to reboot the system:
```bash
systemctl reboot
```
During boot, the MOK management screen will automatically appear. Select "Enroll MOK," then "Continue," then "Yes," and you'll be prompted for the password you set earlier. After entering the password, the key registration process will be completed. Now type reboot to restart, and the NVIDIA driver should load normally.

### Verifying NVIDIA Driver Installation
You can check the currently loaded NVIDIA kernel module by running the following command in the terminal:
```bash
cat /proc/driver/nvidia/version
```
If you see a message similar to the one below, the installation was successful:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Installing NVIDIA Container Toolkit
Now you need to install the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Refer to the [NVIDIA Container Toolkit official installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) for installation, but note that there are special considerations for Fedora, so please read this section completely before proceeding.

### For Apt Users (Ubuntu, Debian, etc.)
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

### For Yum or Dnf Users (Fedora, RHEL, Centos, etc.)
> When testing on Fedora 40, unlike Ubuntu, the `nvidia-smi` command and `nvidia-persistenced` package were not included in the NVIDIA graphics driver by default, so I had to install the `xorg-x11-drv-nvidia-cuda` package additionally. I haven't directly tested on RHEL and Centos, but since their system configurations are very similar to Fedora, if you encounter issues following the guide below, trying the same method might help.
{: .prompt-warning }

> When I installed `xorg-x11-drv-nvidia-cuda` as described above on Fedora 40 and ran a sample workload to test, it worked normally on my system. If you still encounter issues, perhaps due to SELinux, the [Fedora-specific nvidia-container-toolkit package and guide](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) provided by Fedora's AI-ML group might help.
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

### For Zypper Users (openSUSE, SLES)
#### 2-Zypper-1. Configuring Repository for Package Download
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Installing Package
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installing Container Engine
Next, install Docker CE or Podman as your container engine. Choose one based on your environment and preference, referring to the [Docker official documentation](https://docs.docker.com/engine/install/) and [Podman official documentation](https://podman.io/docs/installation).

The following table summarizes the key differences and pros/cons of Docker and Podman:

| Comparison | Docker | Podman |
| --- | --- | --- |
| Architecture | Client-server model, daemon-based | Daemonless structure |
| Security | Potential security risks due to reliance on<br> daemon running with root privileges by default<br>(Rootless mode supported since version 20.10<br> released in 12020, but requires additional setup) | Not dependent on daemon, operates rootless<br> by default unless specified otherwise,<br> protected by SELinux |
| Resource Usage | Generally uses more resources due to<br> background processes always running<br> in daemon-based architecture | Generally less resource overhead |
| Container Start Time | Relatively slower | Up to 50% faster execution due to<br> streamlined architecture |
| Ecosystem and Documentation | Extensive ecosystem and community support,<br> abundant documentation | Relatively smaller ecosystem and documentation |
| Networking | Uses Docker Bridge Network | Uses CNI (Container Network Interface) plugins |
| Kubernetes YAML<br> Native Support | X (requires conversion) | O |

References:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker's biggest advantage is its longer history and de facto standard status in the industry, resulting in a broad ecosystem and abundant documentation.  
Podman, developed more recently by Red Hat, has an inherently advanced structure aimed at being daemonless and rootless, giving it advantages in security, system resource usage, and container start time. Another strength of Podman is that each container is completely independent, so the failure of one container doesn't affect others, unlike Docker where all containers go down if the daemon has problems.

It's most important to choose the tool that fits your specific circumstances. For individual users just starting out, Podman might be a good choice. Although its ecosystem is relatively smaller compared to Docker, it's growing rapidly and closing the gap thanks to its many advantages. Since it's compatible with Docker in many aspects like Dockerfile syntax, Docker images, and CLI (command-line interface), this shouldn't be a significant issue for individuals or small organizations.

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

##### 3-Ubuntu-3. Installing Packages
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Creating `Docker` Group and Adding User
To allow non-root users to manage Docker without `sudo`, create a `Docker` group and add the user who wants to use Docker. Run the following commands in the terminal:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Log out and log back in for the changes to take effect. For Ubuntu or Debian, the Docker service will automatically start at system boot without any additional steps.

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

##### 3-Fedora-3. Installing Packages
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
During package installation, you'll be prompted to approve a GPG key. If the GPG key matches `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, enter y to approve.  
> If the GPG key doesn't match, you may have downloaded a forged package due to a supply chain attack, and should abort the installation.
{: .prompt-danger }

##### 3-Fedora-4. Starting Docker Daemon
Now Docker is installed but not running, so enter the following command to start Docker:
```bash
sudo systemctl start docker
```
To make the Docker service start automatically at system boot, run the following commands:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Adding User to `Docker` Group
To allow non-root users to manage Docker, add the user who wants to use Docker to the `Docker` group. For Fedora, the `Docker` group is automatically created during package installation, so you only need to add the user:
```bash
sudo usermod -aG docker $USER
```
Log out and log back in for the changes to take effect.

#### Verifying Proper Setup
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
