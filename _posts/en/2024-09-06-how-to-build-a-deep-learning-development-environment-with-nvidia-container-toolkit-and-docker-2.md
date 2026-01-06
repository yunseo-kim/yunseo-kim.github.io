---
title: "Building a Deep Learning Development Environment with NVIDIA Container Toolkit and Docker/Podman (2) - Configuring the Container Runtime for GPU Usage, Writing a Dockerfile, and Building a Container Image"
description: "This series covers setting up a container-based deep learning environment locally with NVIDIA Container Toolkit, then configuring SSH and JupyterLab so it can be used as a remote server. Part 2 walks through writing a Dockerfile and building the container image."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Overview

In this series, we install NVIDIA Container Toolkit and Docker or Podman, then write a Dockerfile based on the CUDA and cuDNN images provided in Docker Hub’s [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda) to build a deep learning development environment. To make it easy for anyone who needs it to reuse, I’m sharing both the resulting [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) and the built [images](https://hub.docker.com/r/yunseokim/dl-env/tags) via GitHub and Docker Hub, and additionally provide a guide for configuring SSH and JupyterLab for use as a remote server.  
The series is planned to consist of three posts, and the post you are reading now is the second one.
- [Part 1: Installing NVIDIA Container Toolkit & a Container Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Part 2: Configuring the container runtime for GPU usage, writing a Dockerfile, and building a container image (this post)
- Part 3 (to be uploaded)

This post assumes an x86_64 Linux environment with an NVIDIA GPU that supports CUDA. Since I have not personally tested distributions other than Ubuntu or Fedora, some details may differ slightly on other distros.  
(Revised: 12026.1.6.)

> **Errata Notice**
>
> In the initial draft of this post uploaded in August 12024, there were some errors in the description of the [Dockerfile writing](#5-writing-the-dockerfile) section and in parts of the image built from that Dockerfile. The issues were as follows:
> - In the section where the `remote` account is created, the password-setting portion was incorrect. I stated that you could log in by entering `"000000"` as the initial password, but in reality this was not the case (Added 12025.12.19: now the initial password is *not* `"000000"`, so be sure to check [the relevant section below](#5-4-configuring-an-ssh-server-for-remote-access).)
> - The SSH daemon did not start automatically when the container started
>
> I became aware of these issues in February 12025, and around 2:00 AM on February 16, 12025 (KST, UTC+9) I replaced the problematic Dockerfile and Docker images with fixed versions in the [GitHub repository](https://github.com/yunseo-kim/dl-env-docker) and on [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> If you pulled the Dockerfile or Docker image before that time, please replace it with the corrected version.  
> I apologize to anyone who may have been confused by the incorrect information in the earlier version of this post.
{: .prompt-info }

## Before you begin

This post continues from [Part 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), so if you haven’t read it yet, I recommend reading the previous post first.

## 4. Configuring the container runtime

### If you use Podman

[Configure it using CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> In older versions, you had to manually regenerate the CDI spec file every time: once when NVIDIA Container Toolkit was first installed, and then again whenever you changed the GPU device or driver configuration (including version upgrades).
>
> However, starting with NVIDIA Container Toolkit `v1.18.0`, the `nvidia-cdi-refresh` systemd service automatically generates and updates the CDI spec file at `/var/run/cdi/nvidia.yaml` in the following cases:
> - When NVIDIA Container Toolkit is installed or upgraded
> - When the NVIDIA GPU driver is installed or upgraded
> - When the system reboots
>
> Therefore, unlike before, you no longer need to do anything separately. I updated the body of this post to reflect that.
>
> Note, however, that `nvidia-cdi-refresh` cannot handle driver removal or MIG device reconfiguration, so in those cases you must restart `nvidia-cdi-refresh.service` manually to trigger CDI spec regeneration.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> Using the NVIDIA Container Runtime hook together with CDI can cause conflicts. So if `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} exists, delete that file, or be careful not to run containers with the `NVIDIA_VISIBLE_DEVICES` environment variable set.
{: .prompt-warning }

### If you use Docker

This section explains things assuming [rootless mode](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configure the container runtime with the `nvidia-ctk` command

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

The command above modifies the `/etc/docker/daemon.json`{: .filepath} file so Docker can use the NVIDIA Container Runtime.

#### 4-Docker-2. Restart the Docker daemon

Restart the Docker daemon to apply the changed configuration.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configure `/etc/nvidia-container-runtime/config.toml`{: .filepath} with `sudo nvidia-ctk`

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Verify that it’s configured correctly

Run a sample CUDA container.

For Podman, run:

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

For Docker, run:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

If you see output roughly similar to the following, it worked.

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

## 5. Writing the Dockerfile

Write a Dockerfile for use as a development environment, based on the CUDA and cuDNN images provided in Docker Hub’s [nvidia/cuda repository](https://hub.docker.com/r/nvidia/cuda).

- You need to decide which image to use, considering the required CUDA and cuDNN versions, Linux distribution, and version.
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  As of late August 12024, when this post was written, the latest version of PyTorch (2.4.0) supports CUDA 12.4. So here we use the [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore) image. You can check the latest PyTorch version and its supported CUDA versions on the [PyTorch website](https://pytorch.org/get-started/locally/).

The source for the completed Dockerfile is 공개해 두었다 in the [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker) GitHub repository. Below, I explain the process of writing that Dockerfile step by step.

> (+ Revised: 12026.1.6.)  
> I added Dockerfiles and images that support PyTorch 2.9.1 and CUDA 12.8 / 13.0 to the same GitHub repository and to the public [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) Docker Hub repository. I also updated the body of this post to match PyTorch 2.9.1 and CUDA 13.0.
>
> I also included scikit-image, XGBoost, and within the RAPIDS ecosystem the libraries cuGraph, cuxfilter, cuCIM, RAFT, and cuVS in the image, and added `arm64` support in addition to the existing `amd64` architecture.
{: .prompt-info }

### 5-1. Specify the base image

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. Configure the system time zone (this post uses 'Asia/Seoul')

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> I mainly referred to [this post](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22).
{: .prompt-tip }

### 5-3. Install basic system utilities

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

### 5-4. Configure an SSH server for remote access

For security, configure SSH so that logging in as the root account via remote SSH is not allowed.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Create a non-root user named `remote` to use for SSH login.

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

> Since the contents of build arguments (`ARG`) or environment variables (`ENV`) are 그대로 exposed in the built image, [you should use another method when specifying sensitive information such as passwords or API keys](https://docs.docker.com/build/building/secrets/). Here, I used [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts).
{: .prompt-danger }

> As I’ll mention later](#6-1-building-the-image), when building an image using this Dockerfile, you must specify the string to use as the user account password via the `DL_ENV_PASSWD` environment variable. For the [images distributed on Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags), the initial password is `satisfied-flip-remake`. Using this publicly known default password as-is is extremely insecure, so be sure to change it immediately after running the container for the first time. For better security, it’s advisable to later disable password-based SSH logins and allow logins only via a separate key file, and ideally also use a hardware key such as a Yubikey.
>
> I plan to cover SSH server configuration to some extent in the next post in this series; if you want more detail, the documents below are good references:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Install uv and register environment variables

> **Reflecting PEP 668 “Externally Managed Environments” and introducing uv (Revised: 12026.1.6.)**
>
> In the past, this post wrote the Dockerfile so that packages would be installed directly inside the container image using `pip` without creating a separate virtual environment (`venv`). The reasoning was that in a single-purpose container image, the risk of breaking system software is relatively low, and even if something breaks you can simply create a new container from the image—so it didn’t seem necessary to create a separate virtual environment. This point is also partially acknowledged in [PEP 668](https://peps.python.org/pep-0668/#use-cases) as follows:
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> However, even in a single-purpose container image, it has become the established standard to install via a Python package manager like `pip` only inside a virtual environment, strictly separating those installs from externally managed packages (e.g., those managed via the OS package manager). Accordingly, I revised the content so that a virtual environment is created first and the required packages are installed within it—thereby complying with [PEP 668](https://peps.python.org/pep-0668/) and the associated [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) spec and following Python ecosystem standards.
>
> In Python, the officially supported standard-library tool for creating and managing virtual environments is `venv`, as I once introduced in [another post I wrote in early 12021](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended). However, after Astral](https://astral.sh/) released `uv`, a high-performance Python package and project manager written in Rust, in 12024, it quickly became a new de facto standard in the Python ecosystem thanks to major advantages like:
> - [Dramatically faster dependency resolution and package installation than `pip` (10–100×)](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
> - Excellent usability
> - [Great compatibility with existing `pip` and `venv`](https://docs.astral.sh/uv/pip/)
>
> In particular, machine learning packages like PyTorch and RAPIDS handled here have many dependencies and tend to be large, so `uv`’s advantages really shine. Moreover, [because `uv` uses its cache aggressively and efficiently](https://docs.astral.sh/uv/concepts/cache/), when building container images like this, [using cache mounts appropriately can maximize those benefits and significantly reduce build time](https://docs.astral.sh/uv/guides/integration/docker/#caching). So here I’ll adopt `uv` for creating and managing the virtual environment and for installing packages. I mainly followed the official ["Using uv in Docker" documentation](https://docs.astral.sh/uv/guides/integration/docker/).
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

> **Why set `UV_CACHE_DIR` to a separate path (`"/tmp/uv-cache"`) instead of the default `"$HOME_DIR/.cache/uv"`**
>
> Normally, when you add a user with `useradd --create-home`, that user should own their home directory—and that is the case here as well.
> However, when building images with Podman, I found a bug where, even if ownership was correctly transferred in earlier layers, mounting caches and the like in later layers can reset the ownership metadata of the parent directory back to the default (owned by root). While searching, I found [an issue reported by another user about the same phenomenon about three weeks ago](https://github.com/containers/podman/issues/27777), but as of now there has been no response on that issue. I also added additional comments with details about what I experienced [in that issue thread](https://github.com/containers/podman/issues/27777#issuecomment-3712237296).
>
> So, to avoid problems even if ownership gets reset to root, during the build stage I set `UV_CACHE_DIR` to a path separate from `$HOME_DIR`, namely `"/tmp/uv-cache"`. Since this cache is not included in the final image artifact anyway, it’s fine to change the path like this.
{: .prompt-tip }

### 5-6. Install Python, create a virtual environment, install setuptools & pip

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

### 5-7. Install machine learning and deep learning packages for the dev environment

#### 5-7-1. Common packages

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & CUDA-specific GPU acceleration libraries

##### If you only install PyTorch

To install only PyTorch, add the following to the Dockerfile.

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & Cupy & RAPIDS & DALI

If you want to use not only PyTorch but also Cupy and RAPIDS (cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS), as well as DALI, add the following to the Dockerfile.

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

> In this case, PyTorch and RAPIDS packages share some dependency libraries (cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE). If you install them separately, they may require different versions, and a version installed earlier can be overwritten by a later one—making dependency conflicts much more likely. Therefore, when installing these packages, it’s best to combine them into a single `uv pip install` command so the resolver considers all constraints at once, while giving priority to the versions required by PyTorch.
{: .prompt-tip }

### 5-8. Create a directory to use as a workspace

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. Expose ports and configure the `ENTRYPOINT` to run when the container starts

Expose ports 22 and 8888 for SSH and JupyterLab access.  
Also, since automatically starting the SSH daemon when the container starts requires root privileges, we’ll use the following approach:
1. Start the container as the root account
2. Immediately run the `/entrypoint.sh`{: .filepath} script right after the container starts
3. In that script, start the SSH service, then switch to the `remote` account using [`gosu`](https://github.com/tianon/gosu)
4. If no command is explicitly specified when running the container, run JupyterLab as the default command under the `remote` (non-root) account

> In general, using `sudo` or `su` inside Docker/Podman containers is not recommended. If you need root privileges, it’s better to start the container as root, perform the root-required tasks, and then switch to a non-root user via a tool like [`gosu`](https://github.com/tianon/gosu) as described here. The reasons are explained in detail in the materials below, which may be helpful if you need them:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

First, add the following at the end of the Dockerfile.

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Next, in the same directory as your Dockerfile, create a script file named `entrypoint.sh`{: .filepath} with the following contents.

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

> In general, processes run via `docker exec` or CMD inherit Docker’s ENV values 그대로, but sessions connected via SSH often do not automatically inherit Docker’s environment variables. This is because SSH creates a new shell session on login.
>
> To address this and ensure that even SSH sessions can access predefined environment variables like `$WORK_DIR`, you need to dump those variables into `/etc/environment`{: .filepath } before starting the ssh service when the container runs—e.g., `printenv | grep _ >> /etc/environment`.
>
> The following links may be helpful:
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. Building an OCI image and running a container

### 6-1. Building the image

Open a terminal in the directory where the Dockerfile is located, and set the `DL_ENV_PASSWD` environment variable.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> Replace \<your_own_password\> with the login password you want to use for SSH access.
{: .prompt-info }

Now, **do not close that terminal window**, and continue in the same window by running the command below to build the image.

#### For Podman

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> With Podman, if you want to build the image not only for the platform (OS/architecture) of your current device but for all platforms supported by the base image (with distribution in mind), you can specify the [`--all-platforms` option](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms), and [use `--manifest` instead of `--tag` or `-t`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant).
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> I didn’t separately organize the Docker equivalent here; if you need it, refer to the [official Docker documentation](https://docs.docker.com/build/building/multi-platform/).
{: .prompt-tip }

#### For Docker

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. Run a sample workload

After the build completes, run a disposable container to verify everything works.

For Podman, run:

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

For Docker, run:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

When you run the command above, it starts a container named `test-container` from the `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04` image you built earlier, and maps port 2222 on the host to port 22 in the container, and port 8888 on the host to port 8888 in the container. If the image was built correctly and the container started without issues, JupyterLab should be running inside the `test-container` container at its default address `http:127.0.0.1:8888`. Therefore, if you open a browser on the host system where Podman or Docker is running and go to <http://127.0.0.1:8888>, it should connect through to the container’s `http://127.0.0.1:8888` address and display a screen like the following.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

On the host system, open a terminal and try remotely logging in as the `remote` user of the Ubuntu system running inside the container by running `ssh remote@127.0.0.1 -p 2222`.  
On the first login, you won’t have information about the target’s host key and it can’t be authenticated, so you’ll see a warning and be asked whether to continue connecting—type `"yes"` to proceed.  
Then, for login, enter the password you specified at build time (or, if you pulled the [Docker Hub distributed image](https://hub.docker.com/r/yunseokim/dl-env/tags) and are logging in for the first time, the initial password `satisfied-flip-remake`).

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {fingerprint (a unique value that differs for each key)}.
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

If you see output roughly like the above, you’ve successfully logged in remotely via SSH. To end the session, type `exit`.

### 6-3. (optional) Push to Docker Hub

If you want to be able to pull and use the development environment image you created in the previous steps anytime you need, it’s a good idea to push the built image to Docker Hub.  

> To push your own image to Docker Hub, you need a Docker account. If you don’t have one yet, sign up first at <https://app.docker.com/signup>.
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

#### 6-3-2. Tag the image

Fill in `<dockerhub_username>`, `<repository_name>`, and optionally `:TAG` with values appropriate for you.  
e.g. `"yunseokim"`, `"dl-env"`, `"rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04"`

> If you built the image not only for your device’s platform (OS/architecture) but also for all platforms supported by the base image, and you intend to push the entire manifest list/image index at once, skip this step and jump directly to the [image push](#6-3-3-pushing-the-image) step and follow the method written there.
{: .prompt-tip }

##### For Podman

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### For Docker

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Pushing the image

Finally, run the command below to push the image to Docker Hub.

##### For Podman

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> With Podman, if you want to push multiple platform-specific images bundled together as a manifest list or image index, use the [`podman manifest push` command](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls) as follows:
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

##### For Docker

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

On <https://hub.docker.com/>, you can confirm that it was pushed successfully as shown below.

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

The image completed through the steps above is published in the public Docker Hub repository [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags), and anyone is free to use it.

To pull the image, just replace `push` with `pull` in the command you used when pushing.
