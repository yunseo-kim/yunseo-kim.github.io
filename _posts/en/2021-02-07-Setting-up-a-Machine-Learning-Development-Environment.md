---
title: "Setting Up a Machine Learning Development Environment"
description: >-
  This article covers how to set up a development environment, which can be considered the first step in studying machine learning on a local machine. All content is based on Ubuntu 20.04 LTS with an NVIDIA GeForce RTX 3070 graphics card.
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
toc: true
toc_sticky: true
---

## Overview
This article covers how to set up a development environment, which can be considered the first step in studying machine learning on a local machine. All content is based on Ubuntu 20.04 LTS with an NVIDIA GeForce RTX 3070 graphics card.

- Technology stack to be built
  - Ubuntu 20.04 LTS
  - Python 3.8
  - pip 21.0.1
  - jupyter
  - matplotlib
  - numpy
  - pandas
  - scipy
  - scikit-learn
  - CUDA 11.0.3
  - cuDNN 8.0.5
  - Deep learning framework (it is recommended to install only one per environment)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

## 0. Prerequisites
- Linux is recommended for studying machine learning. While it's possible on Windows, there can be a lot of time wasted on various minor issues. Using the latest LTS version of Ubuntu is the most straightforward option. It's convenient as non-open source proprietary drivers are automatically installed, and most technical documentation is written based on Ubuntu due to its large user base.
- Generally, Python comes pre-installed on Ubuntu and most Linux distributions. However, if Python is not installed, you should install it before following this guide.
  - You can check the currently installed Python version with the following command:
  ```
  $ python3 --version
  ```
  - If you're planning to use TensorFlow 2 or PyTorch, you should check the compatible Python versions. As of writing this article, [the latest version of PyTorch supports Python versions](https://pytorch.org/get-started/locally/#linux-python) 3.6-3.8, and [the latest version of TensorFlow 2 supports Python versions](https://www.tensorflow.org/install) 3.5-3.8.  
  This article uses Python 3.8.
- If you plan to study machine learning on a local machine, it's good to have at least one GPU. While data preprocessing can be done with a CPU, as the model size increases, the learning speed difference between CPU and GPU becomes overwhelming (especially in the case of deep learning).
  - For machine learning, there's essentially only one choice for GPU manufacturer. You need to use NVIDIA products. NVIDIA has invested significantly in the field of machine learning, and almost all machine learning frameworks use NVIDIA's CUDA library.
  - If you plan to use a GPU for machine learning, you should first check if the graphics card you want to use is a model that supports CUDA. You can check the GPU model name of your current computer by using the `uname -m && cat /etc/*release` command in the terminal. Find the corresponding model name in the GPU list at [this link](https://developer.nvidia.com/cuda-gpus), and check the **Compute Capability** value. This value should be at least 3.5 for CUDA to be usable.
  - The criteria for selecting a GPU are well summarized in the following article. The author continues to update this article.  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  Another article by the same person, [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/), is also very informative. For reference, the conclusion of the above article is as follows:
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

If you meet all the requirements mentioned above, let's start setting up the work environment.

## 1. Creating a Work Directory
Open a terminal and modify the .bashrc file to register environment variables (the command follows the $ prompt).  
First, open the nano editor with the following command (vim or any other editor is fine too).
```
$ nano ~/.bashrc
```
Add the following content to the last line. You can change the path inside the double quotes if you want.  
```export ML_PATH="$HOME/ml"```

Press Ctrl+O to save, then Ctrl+X to exit.

Now run the following command to apply the environment variable.
```
$ source ~/.bashrc
```
Create the directory.
```
$ mkdir -p $ML_PATH
```

## 2. Installing pip Package Manager
There are several ways to install the Python packages needed for machine learning. You can use a scientific Python distribution like Anaconda (recommended for Windows operating systems), or you can use pip, Python's own packaging tool. Here, we will use the pip command in the bash shell of Linux or macOS.

Check if pip is installed on your system with the following command:
```
$ pip3 --version

Command 'pip3' not found, but can be installed with:

sudo apt install python3-pip

```
If it appears like this, pip is not installed on your system. Install it using the system's package manager (apt in this case) (if a version number appears, it's already installed, so skip this command).
```
$ sudo apt install python3-pip
```
Now pip is installed on your system.

## 3. Creating an Independent Virtual Environment (Recommended)
To create a virtual environment (to avoid conflicts with library versions of other projects), install venv.
```
$ sudo apt install python3-venv
```
Then create an independent Python environment as follows. The reason for doing this is to prevent conflicts between different library versions needed for each project, so you should create a new virtual environment for each new project to build an independent environment.
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(environment name)
```
To activate this virtual environment, open a terminal and enter the following command:
```
$ cd $ML_PATH
$ source ./(environment name)/bin/activate
```
After activating the virtual environment, upgrade pip inside the virtual environment.
```
(env) $ pip install -U pip
```
To deactivate the virtual environment later, use the ```deactivate``` command. When the environment is activated, any packages you install using the pip command will be installed in this isolated environment, and Python will use these packages.

## 3′. (If not creating a virtual environment) Upgrading pip version
When installing pip on the system, it downloads and installs a binary file from the distribution's (Ubuntu in this case) mirror server, but this binary file is often not the latest version as updates are generally slow (in the author's case, version 20.3.4 was installed). To use the latest version of pip, run the following command to install (or upgrade if already installed) pip in *the user's home directory*.  
```
$ python3 -m pip install -U pip

Collecting pip
(omitted)
Successfully installed pip-21.0.1
```
You can see that pip has been installed as version 21.0.1, which is the latest as of writing this article. At this point, the pip installed in the user's home directory is not automatically recognized by the system, so it needs to be registered as a PATH environment variable to be recognized and used by the system.

Open the .bashrc file with an editor again.
```
$ nano ~/.bashrc
```
This time, find the line starting with ```export PATH=```. If there's no path written after it, just add the content as we did in [Step 1](#1-creating-a-work-directory). If there are other paths already registered, add the content after them using a colon.  
```export PATH="$HOME/.local/bin"```  
```export PATH="(existing path):$HOME/.local/bin"```

[Upgrading system pip by methods other than the system package manager can cause problems due to version conflicts](https://github.com/pypa/pip/issues/5599). That's why we install pip separately in the user's home directory. For the same reason, it's better to use the ```python3 -m pip``` command instead of the ```pip``` command to use pip when not in a virtual environment.

## 4. Installing Machine Learning Packages (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)
Install all necessary packages and their dependencies with the following pip command.  
In my case, I used the ```pip``` command as is because I'm using venv, but if you're not using venv, it's recommended to use the ```python3 -m pip``` command instead, as mentioned earlier.
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(omitted)
```
If you used venv, register a kernel to Jupyter and name it.
```
(env) $ python3 -m ipykernel install --user --name=(kernel name)
```
From now on, you can use the following command to run Jupyter:
```
(env) $ jupyter notebook
```

## 5. Installing CUDA & cuDNN
### 5-1. Checking Required CUDA & cuDNN Versions
Check the supported CUDA versions in the [PyTorch official documentation](https://pytorch.org/get-started/locally/).  
![Check PyTorch Compatible CUDA Version](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
Based on PyTorch version 1.7.1, the supported CUDA versions are 9.2, 10.1, 10.2, 11.0. For NVIDIA 30 series GPUs, CUDA 11 is required, so we know that version 11.0 is needed.

Also check the required CUDA version in the [TensorFlow 2 official documentation](https://www.tensorflow.org/install/gpu).  
![Check TensorFlow2 Compatible CUDA Version](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
Based on TensorFlow 2.4.0 version, we confirmed that CUDA 11.0 and cuDNN 8.0 versions are required.

In my case, I checked the CUDA versions compatible with both packages because I sometimes use PyTorch and sometimes TensorFlow 2. You should check the requirements of the package you need and match accordingly.

### 5-2. Installing CUDA
Go to [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive) and select the version you confirmed earlier. In this article, we select [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
Now select the corresponding platform and installer type, and follow the instructions that appear on the screen. At this point, [it's better to use the system package manager for the installer if possible](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). My preferred method is deb (network).  
![Select CUDA Platform](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)  
![Install CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)  

Run the following commands to install CUDA.
```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```
If you have a keen eye, you might have noticed that the last line is slightly different from the instructions shown in the image. In the network installation, if you enter cuda as shown in the image, the latest version 11.2 will be installed, which is not what we want. You can see various meta-package options in the [CUDA 11.0 Linux Installation Guide](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas). Here, we modified the last line to specify the installation of CUDA Toolkit package as version 11.0 and allow the driver package to be automatically upgraded.

### 5-3. Installing cuDNN
Install cuDNN as follows:
```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```
## 6. Installing PyTorch
If you created a virtual environment in step 3, proceed with the virtual environment you want to use activated. If you don't need PyTorch, skip this step.  
Go to the [PyTorch homepage](https://pytorch.org/get-started/locally/), select the PyTorch build (Stable), operating system (Linux), package (Pip), language (Python), CUDA (11.0) you want to install, and follow the instructions that appear on the screen.  
![Install PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)
```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
To verify that PyTorch is installed correctly, run the following command after running the Python interpreter. If a tensor is returned, it's successful.
```
(env) $ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> x = torch.rand(5, 3)
>>> print(x)"
tensor([[0.8187, 0.5925, 0.2768],
        [0.9884, 0.8298, 0.8553],
        [0.6350, 0.7243, 0.2323],
        [0.9205, 0.9239, 0.9065],
        [0.2424, 0.1018, 0.3426]])
```
To check if the GPU driver and CUDA are activated and available, run the following command:
```
>>> torch.cuda.is_available()
True
```

## 7. Installing TensorFlow 2
If you don't need TensorFlow, you can ignore this step.  
If you installed PyTorch in a virtual environment in step 6, deactivate that virtual environment, go back to steps 3 and 4 to create and activate a new virtual environment, then proceed. If you skipped step 6, just proceed as is.  
Install TensorFlow as follows:
```
(env2) $ pip install --upgrade tensorflow
```
To verify that TensorFlow is installed correctly, run the following command. If it displays the GPU name and returns a tensor, it's successful.
```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
(omitted)
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```
