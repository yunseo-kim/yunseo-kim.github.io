---
title: "Configuración del entorno de desarrollo para aprendizaje automático"
description: >-
  Este artículo trata sobre cómo configurar un entorno de desarrollo para estudiar aprendizaje automático en una máquina local. Todo el contenido está escrito basado en Ubuntu 20.04 LTS con una tarjeta gráfica NVIDIA Geforce RTX 3070.
categories:
  - Data Science
tags:
  - Machine Learning
  - Deep Learning
toc: true
toc_sticky: true
---

## Resumen
Este artículo trata sobre cómo configurar un entorno de desarrollo para estudiar aprendizaje automático en una máquina local. Todo el contenido está escrito basado en Ubuntu 20.04 LTS con una tarjeta gráfica NVIDIA Geforce RTX 3070.

- Pila tecnológica a configurar
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
  - Frameworks de aprendizaje profundo (se recomienda instalar solo uno por entorno)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

## 0. Requisitos previos
- Se recomienda usar Linux para estudiar aprendizaje automático. Aunque es posible en Windows, puede haber muchas pérdidas de tiempo en varios detalles menores. La versión LTS más reciente de Ubuntu es la más conveniente. Los controladores propietarios se instalan automáticamente, lo que es conveniente, y como tiene muchos usuarios, la mayoría de la documentación técnica está escrita para Ubuntu.
- Por lo general, Python viene preinstalado en la mayoría de las distribuciones de Linux, incluido Ubuntu. Sin embargo, si Python no está instalado, debes instalarlo antes de seguir este artículo.
  - Puedes verificar la versión actual de Python instalada con el siguiente comando:
  ```
  $ python3 --version
  ```
  - Si planeas usar TensorFlow 2 o PyTorch, debes verificar las versiones de Python compatibles. En el momento de escribir este artículo, [la última versión de PyTorch es compatible con Python 3.6-3.8](https://pytorch.org/get-started/locally/#linux-python), y [la última versión de TensorFlow 2 es compatible con Python 3.5-3.8](https://www.tensorflow.org/install).  
  En este artículo, usaremos Python 3.8.
- Si planeas estudiar aprendizaje automático en una máquina local, es recomendable tener al menos una GPU. Aunque el preprocesamiento de datos se puede hacer con CPU, la diferencia en la velocidad de entrenamiento entre CPU y GPU se vuelve abrumadora a medida que aumenta el tamaño del modelo durante la fase de entrenamiento (especialmente en el caso del aprendizaje profundo).
  - Para el aprendizaje automático, realmente solo hay una opción de fabricante de GPU. Debes usar productos NVIDIA. NVIDIA ha invertido mucho en el campo del aprendizaje automático, y casi todos los frameworks de aprendizaje automático utilizan la biblioteca CUDA de NVIDIA.
  - Si planeas usar una GPU para aprendizaje automático, primero debes verificar si el modelo de tarjeta gráfica que planeas usar es compatible con CUDA. Puedes verificar el nombre del modelo de GPU instalado actualmente en tu computadora con el comando ```nvidia-smi``` en la terminal. Busca el nombre del modelo correspondiente en la lista de GPU en [este enlace](https://developer.nvidia.com/cuda-gpus) y verifica el valor de **Compute Capability**. Este valor debe ser al menos 3.5 para poder usar CUDA.
  - Los criterios para seleccionar una GPU están bien resumidos en el siguiente artículo. El autor actualiza continuamente este artículo.  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) escrito por la misma persona también es muy útil. Por cierto, la conclusión del artículo anterior es la siguiente:
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

Si cumples con todos los requisitos mencionados anteriormente, comencemos a configurar el entorno de trabajo.

## 1. Creación del directorio de trabajo
Abre una terminal y modifica el archivo .bashrc para registrar variables de entorno (el comando está después del prompt $).  
Primero, usa el siguiente comando para abrir el editor nano (vim u otro editor también está bien).
```
$ nano ~/.bashrc
```
Agrega el siguiente contenido en la última línea. Puedes cambiar el contenido entre comillas dobles a otra ruta si lo deseas.  
```export ML_PATH="$HOME/ml"```

Presiona Ctrl+O para guardar y luego Ctrl+X para salir.

Ahora ejecuta el siguiente comando para aplicar la variable de entorno.
```
$ source ~/.bashrc
```
Crea el directorio.
```
$ mkdir -p $ML_PATH
```

## 2. Instalación del gestor de paquetes pip
Hay varias formas de instalar los paquetes de Python necesarios para el aprendizaje automático. Puedes usar una distribución de Python científico como Anaconda (método recomendado para el sistema operativo Windows), o puedes usar pip, la herramienta de empaquetado propia de Python. Aquí usaremos el comando pip en el shell bash de Linux o macOS.

Verifica si pip está instalado en tu sistema con el siguiente comando:
```
$ pip3 --version

No se pudo encontrar el comando 'pip3'. Sin embargo, se puede instalar con:

sudo apt install python3-pip

```
Si aparece algo como lo anterior, significa que pip no está instalado en tu sistema. Instálalo usando el gestor de paquetes del sistema (aquí apt) (si aparece un número de versión, significa que ya está instalado, así que omite este comando).
```
$ sudo apt install python3-pip
```
Ahora pip está instalado en tu sistema.

## 3. Creación de un entorno virtual independiente (recomendado)
Para crear un entorno virtual (para evitar conflictos con versiones de bibliotecas de otros proyectos), instala venv.
```
$ sudo apt install python3-venv
```
Luego, crea un entorno Python independiente de la siguiente manera. Esto se hace para evitar conflictos entre las versiones de bibliotecas necesarias para cada proyecto, por lo que debes crear un nuevo entorno virtual cada vez que inicies un nuevo proyecto para establecer un entorno independiente.
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(nombre del entorno)
```
Para activar este entorno virtual, abre una terminal y ingresa el siguiente comando:
```
$ cd $ML_PATH
$ source ./(nombre del entorno)/bin/activate
```
Después de activar el entorno virtual, actualiza pip dentro del entorno virtual.
```
(env) $ pip install -U pip
```
Para desactivar el entorno virtual más tarde, usa el comando ```deactivate```. Cuando el entorno está activado, cualquier paquete que instales con el comando pip se instalará en este entorno independiente y Python usará estos paquetes.

## 3′. (Si no creas un entorno virtual) Actualización de la versión de pip
Cuando instalas pip en el sistema, se descarga e instala un archivo binario del servidor espejo de la distribución (en este caso, Ubuntu), pero este archivo binario generalmente no es la versión más reciente debido a actualizaciones lentas (en mi caso, se instaló la versión 20.3.4). Para usar la versión más reciente de pip, ejecuta el siguiente comando para instalar (o actualizar si ya está instalado) pip en el *directorio home del usuario*.  
```
$ python3 -m pip install -U pip

Collecting pip
(omitido)
Successfully installed pip-21.0.1
```
Puedes ver que pip se ha instalado en la versión 21.0.1, que es la más reciente en el momento de escribir este artículo. En este punto, pip instalado en el directorio home del usuario no es reconocido automáticamente por el sistema, por lo que debes registrarlo como una variable de entorno PATH para que el sistema lo reconozca y use.

Abre nuevamente el archivo .bashrc con un editor.
```
$ nano ~/.bashrc
```
Esta vez, busca la línea que comienza con ```export PATH=```. Si no hay una ruta escrita después de esto, simplemente agrega el contenido como lo hicimos en el [paso 1](#1-creación-del-directorio-de-trabajo). Si ya hay otras rutas registradas, agrega el contenido después usando dos puntos.  
```export PATH="$HOME/.local/bin"```  
```export PATH="(ruta existente):$HOME/.local/bin"```

[Actualizar pip del sistema de una manera diferente al gestor de paquetes del sistema puede causar problemas debido a conflictos de versiones](https://github.com/pypa/pip/issues/5599). Por eso instalamos pip en el directorio home del usuario sin usar ```sudo```. Por la misma razón, es mejor usar el comando ```python3 -m pip``` en lugar del comando ```pip``` para usar pip cuando no estás dentro de un entorno virtual.

## 4. Instalación de paquetes para aprendizaje automático (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)
Instala todos los paquetes necesarios y otros paquetes conectados por dependencias con el siguiente comando pip.  
Si no usas venv, necesitarás permisos de administrador.  
Además, en mi caso, uso el comando ```pip``` porque estoy usando venv, pero si no estás usando venv, se recomienda usar el comando ```python3 -m pip``` en su lugar, como se mencionó anteriormente.
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(omitido)
```
Si usaste venv, registra un kernel en Jupyter y dale un nombre.
```
(env) $ python3 -m ipykernel install --user --name=(nombre del kernel)
```
A partir de ahora, puedes ejecutar Jupyter con el siguiente comando:
```
(env) $ jupyter notebook
```

## 5. Instalación de CUDA y cuDNN
### 5-1. Verificación de las versiones necesarias de CUDA y cuDNN

Verifica las versiones de CUDA compatibles en la [documentación oficial de PyTorch](https://pytorch.org/get-started/locally/).

![Verificación de versiones de CUDA compatibles con PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)

Para PyTorch versión 1.7.1, las versiones de CUDA compatibles son 9.2, 10.1, 10.2 y 11.0. Para las GPU NVIDIA serie 30, se requiere CUDA 11, por lo que sabemos que necesitamos la versión 11.0.

También verifica las versiones de CUDA necesarias en la [documentación oficial de TensorFlow 2](https://www.tensorflow.org/install/gpu).

![Verificación de versiones de CUDA compatibles con TensorFlow 2](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)

Para TensorFlow versión 2.4.0, se requiere CUDA 11.0 y cuDNN 8.0.

El autor verificó las versiones de CUDA compatibles con ambos paquetes porque a veces usa PyTorch y otras veces TensorFlow 2. Debes verificar los requisitos del paquete que necesites y ajustarte a ellos.

### 5-2. Instalación de CUDA

Accede al [Archivo de CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) y selecciona la versión que verificaste anteriormente. En este artículo, seleccionamos [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).

![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)

Ahora selecciona la plataforma y el tipo de instalador correspondientes, y sigue las instrucciones que aparecen en la pantalla. En este caso, [es preferible usar el gestor de paquetes del sistema](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). El autor prefiere el método deb (network).

![Selección de plataforma CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-2.png)
![Instalación de CUDA](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-3.png)

Ejecuta los siguientes comandos para instalar CUDA:

```
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
$ sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
$ sudo apt update
$ sudo apt install cuda-toolkit-11-0 cuda-drivers
```

Si eres observador, habrás notado que la última línea es ligeramente diferente a las instrucciones mostradas en la imagen. En la instalación por red, si solo se ingresa cuda como se muestra en la imagen, se instalará la versión más reciente (11.2), lo cual no es lo que queremos. Puedes ver varias opciones de metapaquetes en la [Guía de instalación de CUDA 11.0 para Linux](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas). Aquí, modificamos la última línea para instalar específicamente el paquete CUDA Toolkit versión 11.0 y permitir que el paquete de controladores se actualice automáticamente.

### 5-3. Instalación de cuDNN

Instala cuDNN con los siguientes comandos:

```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```

## 6. Instalación de PyTorch

Si creaste un entorno virtual en el paso 3, asegúrate de activarlo antes de continuar. Si no necesitas PyTorch, puedes omitir este paso.

Accede a la [página de PyTorch](https://pytorch.org/get-started/locally/), selecciona la versión de PyTorch (Stable), el sistema operativo (Linux), el paquete (Pip), el lenguaje (Python) y CUDA (11.0), y sigue las instrucciones que aparecen en la pantalla.

![Instalación de PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)

```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```

Para verificar si PyTorch se instaló correctamente, ejecuta el intérprete de Python y prueba los siguientes comandos. Si se devuelve un tensor, la instalación fue exitosa.

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

Para verificar si el controlador de GPU y CUDA están activados y disponibles, ejecuta el siguiente comando:

```
>>> torch.cuda.is_available()
True
```

## 7. Instalación de TensorFlow 2

Si instalaste PyTorch en un entorno virtual en el paso 6, desactiva ese entorno y vuelve a los pasos 3 y 4 para crear y activar un nuevo entorno virtual antes de continuar. Si omitiste el paso 6, simplemente continúa.

Instala TensorFlow con el siguiente comando:

```
(env2) $ pip install --upgrade tensorflow
```

Para verificar si TensorFlow se instaló correctamente, ejecuta el siguiente comando. Si muestra el nombre de la GPU y devuelve un tensor, la instalación fue exitosa.

```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
(omitido)
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```
