---
title: Building a Deep Learning Development Environment with NVIDIA Container Toolkit and Docker/Podman (2) - Configuring Container Runtime for GPU Utilization, Writing Dockerfile and Building Container Image
description: This series covers setting up a container-based deep learning development environment locally using NVIDIA Container Toolkit, and configuring SSH and Jupyter Lab for remote server use. This post is the second in the series, covering the process of writing a Dockerfile and building a container image.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Overview
This series covers installing NVIDIA Container Toolkit and Docker or Podman, and building a deep learning development environment by writing a Dockerfile based on CUDA and cuDNN images provided by the [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda) on Docker Hub. For those who need it, I share the [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) and [image](https://hub.docker.com/r/yunseokim/dl-env/tags) completed through this process via GitHub and Docker Hub for free use, and additionally provide a guide for SSH and Jupyter Lab setup for remote server use.  
The series will consist of 3 posts, and this post you're reading is the second in the series.
- [Part 1: Installing NVIDIA Container Toolkit & Container Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Part 2: Configuring Container Runtime for GPU Utilization, Writing Dockerfile and Building Container Image (This post)
- Part 3 (To be uploaded)

We proceed assuming an x86_64 Linux environment with an NVIDIA graphics card supporting CUDA installed. Some specific details may differ slightly for distributions other than Ubuntu or Fedora, as I haven't directly tested them.  
(Content updated on 2025.02.18)

> **Error Correction Notice**  
> In the initial version of this post uploaded in August 2024, there were some errors in the description of the [Writing Dockerfile](#5-writing-dockerfile) section and in the image built from that Dockerfile. The problematic parts were as follows:
> - The password setting part in the remote account creation section was incorrect, and it was not possible to log in with "000000" as the password as originally intended
> - The SSH daemon did not automatically start when the container was launched
>
> I recently became aware of these issues and replaced the problematic Dockerfile and Docker images with files that resolved the issues in the [GitHub repository](https://github.com/yunseo-kim/dl-env-docker) and [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) around 2 AM on February 16, 2025 (UTC+9).  
> If you pulled the Dockerfile or Docker images before this time, please replace them with the updated versions.  
> I apologize to those who may have experienced confusion due to the incorrect information among those who previously referred to this post.
{: .prompt-info }

## Before We Begin
This post is a continuation of [Part 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), so if you haven't read it yet, it's recommended to read the previous post first.

## 4. Configuring Container Runtime
### If Using Podman
[Configure using CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Run the following command to generate CDI specification files in the `/etc/cdi`{: .filepath} directory.
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> When changing graphics card devices or modifying CUDA driver configurations (including version upgrades), you need to regenerate the CDI specification file.
{: .prompt-warning }

> Using NVIDIA Container Runtime hook with CDI can cause conflicts, so if `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} exists, delete that file or be careful not to run containers with the `NVIDIA_VISIBLE_DEVICES` environment variable set.
{: .prompt-warning }

### If Using Docker
Explanation based on [rootless mode](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configure Container Runtime Settings with `nvidia-ctk` Command
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
This command modifies the `/etc/docker/daemon.json`{: .filepath} file to allow Docker to utilize the NVIDIA Container Runtime.

#### 4-Docker-2. Restart Docker Daemon
Restart the Docker daemon to apply the changed settings.
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configure `/etc/nvidia-container-runtime/config.toml`{: .filepath} Settings File with `sudo nvidia-ctk` Command
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Verify Proper Configuration
Run a sample CUDA container.

If using Podman, execute the following command:
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

If using Docker, execute the following command:
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
If a screen similar to the one below is displayed, it's successful.

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
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)As of late August 2024, when this post is being written, PyTorch version 2.4.0, which is the latest version, supports CUDA 12.4. Therefore, we will use the [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) image here. You can check the latest version of PyTorch and the supported CUDA version on the [PyTorch homepage](https://pytorch.org/get-started/locally/).

The completed Dockerfile source is publicly available in the [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub repository. Below, I explain the process of writing this Dockerfile step by step.

### 5-1. Specify Base Image
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Install Basic Utilities and Python Prerequisites
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

### 5-3. Set System Time Zone (In this post, we proceed with 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. Set Up SSH Server for Remote Access  
Configure SSH to prevent root account login for security when remotely accessing.
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Create a non-root user named 'remote' to use for SSH access.
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

> When building a Docker image using this Dockerfile, if no separate options are specified, the initial value of the 'remote' user's account password is 000000. This is very vulnerable in terms of security, so when building the Docker image, use the `--build-arg` option to specify a separate account login password, or change the settings immediately after running the container for the first time. For security, it's desirable to disable password login when connecting via SSH and configure it to allow login only through a separate key file later, and it would be ideal to utilize hardware keys like Yubikey.
> SSH server configuration will be covered to some extent in the next part of this series, and if you want to know more details, you can refer to the documents in the following list:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> Also, this Dockerfile assumes that the built image will be used only by individuals or a small group of trusted insiders, and if you need to distribute the built image externally, setting passwords through `--build-arg` is dangerous and other methods should be used. Please refer to [this document](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/).
{: .prompt-danger }

### 5-5. Install setuptools, pip and Register PATH Environment Variable
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. Install Machine Learning and Deep Learning Packages to Use in the Development Environment
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
If you want to use Cupy, cuDF, cuML, and DALI, add the following content to the Dockerfile as well:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Create Directory to Use as Workspace
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Open Ports and Set `ENTRYPOINT` to Run When Container Starts
Open ports 22 and 8888 for SSH and Jupyter Lab access.  
Also, to automatically run the SSH daemon when the container starts, root privileges are needed, so we will use the following method:
1. Logged in as root account when container starts
2. Run `/entrypoint.sh`{: .filepath} script immediately after container starts
3. Start SSH service in that script and then switch to remote account using [`gosu`](https://github.com/tianon/gosu)
4. If no separate command is specified when running the container, run Jupyter Lab as remote account (non-root privileges) by default

> Generally, using `sudo` or `su` inside Docker or Podman containers is not recommended, and if root privileges are needed, it's better to start the container as root account, perform tasks that require root privileges, and then switch to a non-root user using [`gosu`](https://github.com/tianon/gosu) as explained here. The reasons for doing this are explained in detail in the materials below, which can be helpful if needed:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

First, enter the following content at the end of the Dockerfile:
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Next, create a script file named `entrypoint.sh`{: .filepath} in the same path as the written Dockerfile and write the content as follows:
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

## 6. Build Docker Image and Run Container
### 6-1. Build Image
Open a terminal in the directory where the Dockerfile is located and run the following command:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Enter the login password you want to use for SSH access in place of \<password\>.
{: .prompt-info }

### 6-2. Run Sample Workload
After completing the build, run a disposable container to check if it works well.

For Podman, run the following command:
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

For Docker, run the following command:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

When you enter the above command in the terminal, it will run a container named `test-container` from the previously built `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` image, and connect port 22 of the host system to port 22 of that container, and port 88 of the host system to port 8888 of the container. If the Docker image was built normally in the previous step and the container started without any problems, JupyterLab should be running inside the `test-container` container at the default address `http:127.0.0.1:8888`. Therefore, when you open a browser on the host system where the Docker Engine is running and access <http://127.0.0.1:88>, it should connect to the `http://127.0.0.1:8888` address inside the container and display a screen like the one below.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Let's open a terminal on the host system and run the `ssh remote@127.0.0.1` command to remotely log in to the remote account of the Ubuntu system running inside the container.  
When logging in for the first time, a warning will be displayed stating that there is no information about the encryption key of the connection target and authentication is not possible, and it will ask if you want to continue connecting. You can proceed by entering "yes".  
Then enter the password (if you didn't change it when building the image, it will be the default value "000000") to log in.
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {fingerprint (each key has its own unique value)}.
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
If it outputs something similar to the above, you have successfully logged in remotely via SSH. To end the connection, enter the `exit` command.

### 6-3. (optional) Push to Docker Hub
To be able to pull and utilize the development environment image you created through the previous process whenever needed, it's good to push the built image to Docker Hub.  

> To push your own image to Docker Hub, you need your own Docker account, so if you don't have one yet, complete the registration at <https://app.docker.com/signup> first.
{: .prompt-tip }

#### 6-3-1. Log in to Docker Hub
##### For Podman
```bash
podman login docker.io
```

##### For Docker
```bash
docker login
```

#### 6-3-2. Tag Image
Fill in the parts for `<dockerhub_username>`, `<repository_name>`, and (optional) `:TAG` with your own relevant information.  
e.g. "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### For Podman
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### For Docker
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push Image
Finally, run the command below to push the image to Docker Hub.

##### For Podman
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### For Docker
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
You can confirm that it has been pushed successfully as shown below at <https://hub.docker.com/>.  
![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

The image completed through the previous process has been made public in the [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) public repository on Docker Hub, and anyone can use it freely.

To pull the image, you just need to change the `push` part to `pull` in the command used earlier for pushing.
