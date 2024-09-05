---
title: "Building a Deep Learning Development Environment with NVIDIA Container Toolkit and Docker (2) - Configuring Container Runtime for GPU Utilization, Writing Dockerfile and Building Docker Image"
description: >-
  This series covers how to set up a local deep learning development environment based on NVIDIA Container Toolkit and Docker, and configure SSH and Jupyter Lab for remote server use. This post is the second in the series, introducing how to configure the container runtime, write a Dockerfile, and build a Docker image.
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
---

## Overview
This series covers the process of installing NVIDIA Container Toolkit and Docker, and building a deep learning development environment by writing a Dockerfile based on CUDA and cuDNN images provided by the [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda) on Docker Hub. For those who need it, the [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) and [image](https://hub.docker.com/r/yunseokim/dl-env/tags) completed through this process are shared via GitHub and Docker Hub for free use, and additionally, a guide for SSH and Jupyter Lab setup for remote server use is provided.  
The series will consist of 3 posts, and this post you're reading is the second in the series.
- [Part 1: Installing NVIDIA Container Toolkit & Docker Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Part 2: Configuring Container Runtime for GPU Utilization, Writing Dockerfile and Building Docker Image (This post)
- Part 3 (To be uploaded)

We proceed assuming an x86_64 Linux environment with an NVIDIA graphics card supporting CUDA, and while some specific details may differ slightly for distributions other than Ubuntu or Fedora as they haven't been directly tested.

## Before We Begin
This post is a continuation from [Part 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), so if you haven't read it yet, it's recommended to read the previous post first.

## 4. Configuring Container Runtime
### 4-1. Execute `nvidia-ctk` command
```bash
sudo nvidia-ctk runtime configure --runtime=docker
```
This command modifies the `/etc/docker/daemon.json`{: .filepath} file to allow Docker to utilize the NVIDIA Container Runtime.

### 4-2. Restart Docker daemon
Restart the Docker daemon to apply the changed settings.
```bash
sudo systemctl restart docker
```

### 4-3. Verify proper configuration
Run a sample CUDA container.
```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
If you see a screen similar to the one below, it's successful.

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

## 5. Writing Dockerfile
Write a Dockerfile to be used as a development environment based on CUDA and cuDNN images provided by the [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda) on Docker Hub.

- You need to decide on the image to use considering the required CUDA and cuDNN versions, Linux distribution type and version, etc. 
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)As of late August 2024, when this post is being written, PyTorch version 2.4.0, which is the latest version, supports CUDA 12.4. Therefore, we'll use the [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) image here. You can check the latest PyTorch version and supported CUDA version on the [PyTorch homepage](https://pytorch.org/get-started/locally/).

The source of the completed Dockerfile has been made public in the [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub repository. Below, I explain the process of writing this Dockerfile step by step.

### 5-1. Specify base image
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Install basic utilities and Python prerequisites
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

### 5-3. Set system time zone (In this post, we proceed with 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. Configure SSH server for remote access  
For security, configure so that root account login is not possible with a password when connecting remotely via SSH.
```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```
Configure the SSH service to start automatically when the container starts.
```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```
Create a non-root user named 'remote' to use when connecting via SSH.
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

> When building a Docker image using this Dockerfile, if no separate option is specified, the initial password for the 'remote' user account is 000000. This is very vulnerable in terms of security, so when building the Docker image, use the `--build-arg` option to specify a separate account login password, or change the settings immediately after running the container for the first time. For security, it's desirable to disable password login when connecting via SSH and configure it to allow login only through a separate key file, and it would be ideal to utilize hardware keys like Yubikey.
> SSH server configuration will be covered to some extent in the next part of this series, and if you want to know more details, you can refer to the documents in the following list.
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Install setuptools, pip and register PATH environment variable
```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. Install machine learning and deep learning packages to use in the development environment
```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
If you want to use Cupy, cuDF, cuML, and DALI, add the following to the Dockerfile as well.
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Configure JupyterLab to run when the container starts
```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
```

## 6. Building Docker Image and Running Container
### 6-1. Build image
Open a terminal in the directory where the Dockerfile is located and run the following command.
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Enter the login password you want to use when connecting via SSH in place of \<password\>.
{: .prompt-info }

### 6-2. Run sample workload
Once the build is complete, run a disposable container with the following command to check if it works well.
```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```
When you enter the above command in the terminal, it runs a container named `test-container` from the previously built `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` image and connects port 88 of the host system to port 8888 of that container. If the Docker image was built correctly in the previous step and the container started without any problems, JupyterLab should be running at the default address `http:127.0.0.1:8888` inside the `test-container` container. Therefore, when you open a browser on the host system where the Docker Engine is running and access <http://127.0.0.1:88>, it should connect to the `http://127.0.0.1:8888` address inside the container and display a screen like the one below.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (optional) Push to Docker Hub
To be able to pull and utilize the development environment image created through the previous process whenever needed, it's good to push the built image to Docker Hub.  

> To push your own image to Docker Hub, you need your own Docker account, so if you don't have one yet, complete the registration at <https://app.docker.com/signup> first.
{: .prompt-tip }

First, log in to Docker Hub with the command below.
```bash
docker login
```
Now, run a command in the following format to create an image tag.
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```
Finally, run the command below to push the image to Docker Hub.
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
You can confirm that it has been pushed successfully as shown below at <https://hub.docker.com/>.  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

The image completed through the previous process has been made public in the [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) public repository on Docker Hub, and anyone can use it freely.
