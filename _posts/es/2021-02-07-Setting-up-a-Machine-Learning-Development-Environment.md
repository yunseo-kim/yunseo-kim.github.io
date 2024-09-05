---
title: "Configuración del entorno de desarrollo para aprendizaje automático"
description: >-
  Este artículo trata sobre cómo configurar un entorno de desarrollo para estudiar aprendizaje automático en una máquina local. Todo el contenido está escrito basado en Ubuntu 20.04 LTS con una tarjeta gráfica NVIDIA Geforce RTX 3070.
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
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

### Tabla comparativa con la nueva guía de configuración del entorno de desarrollo para aprendizaje automático
Aunque han pasado unos 3 años y medio desde que se subió al blog, el contenido de este artículo sigue siendo válido en general, excepto por algunos detalles específicos como las versiones de los paquetes y el lanzamiento del controlador de código abierto de NVIDIA. Sin embargo, al comprar una nueva PC en el verano de 2024 y configurar el entorno de desarrollo, hubo algunos cambios, por lo que escribí una [nueva guía de configuración del entorno de desarrollo](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/). Las diferencias se muestran en la siguiente tabla:

| Diferencia | Este artículo (versión 2021) | Nuevo artículo (versión 2024) |
| --- | --- | --- |
| Distribución Linux | Basado en Ubuntu | Aplicable a Ubuntu, Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Método de configuración del entorno | Entorno virtual de Python usando venv | Entorno basado en contenedores Docker<br> usando [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalación del controlador gráfico NVIDIA | Sí | Sí |
| Instalación directa de CUDA y cuDNN<br> en el sistema host | Sí (usando el gestor de paquetes Apt) | No (se usa una imagen preinstalada proporcionada<br> por NVIDIA en [Docker Hub](https://hub.docker.com/r/nvidia/cuda),<br> por lo que no es necesario hacerlo manualmente) |
| Portabilidad | Se debe reconstruir el entorno de desarrollo<br> cada vez que se migra a otro sistema | Basado en Docker, por lo que se puede construir<br> fácilmente una nueva imagen con el Dockerfile<br> creado cuando sea necesario, o portar fácilmente<br> una imagen existente (excluyendo configuraciones<br> adicionales de volumen o red) |
| Uso de bibliotecas de aceleración GPU<br> adicionales además de cuDNN | No | Introducción de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interfaz de Jupyter Notebook | Jupyter Notebook (clásico) | JupyterLab (Next-Generation) |
| Configuración del servidor SSH | No se trata | Incluye configuración básica del servidor SSH en la parte 3 |

Si deseas utilizar un entorno virtual de Python como venv en lugar de Docker, este artículo original sigue siendo válido, así que puedes continuar leyéndolo. Si quieres disfrutar de las ventajas de adoptar contenedores Docker, como una alta portabilidad, o si planeas usar otra distribución Linux además de Ubuntu, como Fedora, o si estás usando un entorno con tarjeta gráfica NVIDIA y quieres utilizar bibliotecas de aceleración GPU adicionales como CuPy, cuDF, cuML, DALI, o si deseas acceder remotamente mediante configuraciones SSH y JupyterLab, te recomiendo consultar también la [nueva guía](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1/).

## 0. Requisitos previos
- Se recomienda usar Linux para estudiar aprendizaje automático. Aunque es posible en Windows, puede haber muchas pérdidas de tiempo en varios aspectos menores. Lo más conveniente es usar la última versión LTS de Ubuntu. Es conveniente porque los controladores propietarios también se instalan automáticamente, y como hay muchos usuarios, la mayoría de la documentación técnica está escrita basada en Ubuntu.
- Generalmente, Python viene preinstalado en la mayoría de las distribuciones Linux, incluido Ubuntu. Sin embargo, si Python no está instalado, debes instalarlo antes de seguir este artículo.
  - Puedes verificar la versión actual de Python instalada con el siguiente comando:
  ```
  $ python3 --version
  ```
  - Si vas a usar TensorFlow 2 o PyTorch, debes verificar las versiones de Python compatibles. En el momento de escribir este artículo, [las versiones de Python compatibles con la última versión de PyTorch](https://pytorch.org/get-started/locally/#linux-python) son 3.6-3.8, y [las versiones de Python compatibles con la última versión de TensorFlow 2](https://www.tensorflow.org/install) son 3.5-3.8.  
  En este artículo, usamos Python 3.8.
- Si planeas estudiar aprendizaje automático en una máquina local, es bueno tener al menos una GPU. Aunque el preprocesamiento de datos es posible con CPU, la diferencia en la velocidad de entrenamiento entre CPU y GPU es abrumadora a medida que aumenta el tamaño del modelo (especialmente en el caso del aprendizaje profundo).
  - Para el aprendizaje automático, la opción de fabricante de GPU es prácticamente una: debes usar productos NVIDIA. NVIDIA es una empresa que ha invertido mucho en el campo del aprendizaje automático, y casi todos los frameworks de aprendizaje automático utilizan la biblioteca CUDA de NVIDIA.
  - Si planeas usar GPU para aprendizaje automático, primero debes verificar si el modelo de tarjeta gráfica que planeas usar es compatible con CUDA. Puedes verificar el nombre del modelo de GPU instalado en tu computadora actual con el comando `uname -m && cat /etc/*release` en la terminal. Busca el nombre del modelo correspondiente en la lista de GPU en el [enlace](https://developer.nvidia.com/cuda-gpus) y verifica el valor de **Compute Capability**. Este valor debe ser al menos 3.5 para poder usar CUDA.
  - Los criterios de selección de GPU están bien resumidos en el siguiente artículo. El autor actualiza continuamente el artículo.  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) escrito por la misma persona también es muy útil. La conclusión del artículo anterior es la siguiente:
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

Si cumples con todos los requisitos mencionados anteriormente, comencemos a configurar el entorno de trabajo.

## 1. Creación del directorio de trabajo
Abre la terminal y modifica el archivo .bashrc para registrar la variable de entorno (el comando está después del prompt $).  
Primero, abre el editor nano con el siguiente comando (puedes usar vim u otro editor si lo prefieres):
```
$ nano ~/.bashrc
```
Agrega el siguiente contenido en la última línea. Puedes cambiar el contenido entre comillas dobles a otra ruta si lo deseas.  
```export ML_PATH="$HOME/ml"```

Presiona Ctrl+O para guardar y luego Ctrl+X para salir.

Ahora ejecuta el siguiente comando para aplicar la variable de entorno:
```
$ source ~/.bashrc
```
Crea el directorio:
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
Si aparece algo así, significa que pip no está instalado en tu sistema. Instálalo usando el gestor de paquetes del sistema (aquí apt) (si aparece un número de versión, significa que ya está instalado, así que omite este comando):
```
$ sudo apt install python3-pip
```
Ahora pip está instalado en tu sistema. 

## 3. Creación de un entorno virtual independiente (recomendado)
Para crear un entorno virtual (para evitar conflictos con las versiones de bibliotecas de otros proyectos), instala venv:
```
$ sudo apt install python3-venv
```
Luego, crea un entorno Python independiente de la siguiente manera. Esto se hace para evitar conflictos entre las versiones de bibliotecas necesarias para cada proyecto, así que debes crear un nuevo entorno virtual cada vez que inicies un nuevo proyecto para establecer un entorno independiente.
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(nombre del entorno)
```
Para activar este entorno virtual, abre una terminal y ingresa el siguiente comando:
```
$ cd $ML_PATH
$ source ./(nombre del entorno)/bin/activate
```
Después de activar el entorno virtual, actualiza pip dentro del entorno virtual:
```
(env) $ pip install -U pip
```
Para desactivar el entorno virtual más tarde, usa el comando ```deactivate```. Cuando el entorno está activado, cualquier paquete que instales con el comando pip se instalará en este entorno independiente y Python usará estos paquetes.

## 3′. (Si no creas un entorno virtual) Actualización de la versión de pip
Al instalar pip en el sistema, se descarga e instala un archivo binario del servidor espejo de la distribución (aquí Ubuntu), pero este archivo binario generalmente no es la última versión debido a actualizaciones lentas (en mi caso, se instaló la versión 20.3.4). Para usar la última versión de pip, ejecuta el siguiente comando para instalar (o actualizar si ya está instalado) pip en el *directorio home del usuario*:  
```
$ python3 -m pip install -U pip

Collecting pip
(omitido)
Successfully installed pip-21.0.1
```
Puedes ver que pip se ha instalado en la versión 21.0.1, que es la última en el momento de escribir este artículo. En este punto, el pip instalado en el directorio home del usuario no es reconocido automáticamente por el sistema, por lo que debes registrarlo como una variable de entorno PATH para que el sistema lo reconozca y use. 

Abre nuevamente el archivo .bashrc con un editor:
```
$ nano ~/.bashrc
```
Esta vez, busca la línea que comienza con ```export PATH=```. Si no hay una ruta escrita después de eso, simplemente agrega el contenido como lo hiciste en el [paso 1](#1-creación-del-directorio-de-trabajo). Si hay otras rutas registradas existentes, agrega el contenido al final usando dos puntos:  
```export PATH="$HOME/.local/bin"```  
```export PATH="(ruta existente):$HOME/.local/bin"```

[Actualizar el pip del sistema de una manera diferente al gestor de paquetes del sistema puede causar problemas debido a conflictos de versiones](https://github.com/pypa/pip/issues/5599). Por eso instalamos pip por separado en el directorio home del usuario. Por la misma razón, es mejor usar el comando ```python3 -m pip``` en lugar del comando ```pip``` para usar pip cuando no estés dentro de un entorno virtual.

## 4. Instalación de paquetes para aprendizaje automático (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)
Instala todos los paquetes necesarios y otros paquetes conectados como dependencias con el siguiente comando pip.  
En mi caso, uso el comando ```pip``` porque estoy usando venv, pero si no estás usando venv, se recomienda usar el comando ```python3 -m pip``` en su lugar, como se mencionó anteriormente.
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(omitido)
```
Si usaste venv, registra un kernel en Jupyter y dale un nombre:
```
(env) $ python3 -m ipykernel install --user --name=(nombre del kernel)
```
A partir de ahora, para ejecutar Jupyter, usa el siguiente comando:
```
(env) $ jupyter notebook
```

## 5. Instalación de CUDA & cuDNN
### 5-1. Verificación de las versiones necesarias de CUDA & cuDNN
Verifica las versiones de CUDA compatibles en la [documentación oficial de PyTorch](https://pytorch.org/get-started/locally/).  
![Verificación de la versión de CUDA compatible con PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
Basado en PyTorch versión 1.7.1, las versiones de CUDA compatibles son 9.2, 10.1, 10.2, 11.0. Para las GPU NVIDIA serie 30, se requiere CUDA 11, por lo que podemos ver que necesitamos la versión 11.0.

También verifica las versiones de CUDA necesarias en la [documentación oficial de TensorFlow 2](https://www.tensorflow.org/install/gpu).  
![Verificación de la versión de CUDA compatible con TensorFlow 2](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
Basado en TensorFlow versión 2.4.0, confirmamos que necesitamos CUDA versión 11.0 y cuDNN versión 8.0.

En mi caso, verifiqué las versiones de CUDA compatibles con ambos paquetes porque a veces uso PyTorch y otras veces TensorFlow 2. Debes verificar los requisitos del paquete que necesites y ajustarte a ellos.

### 5-2. Instalación de CUDA
Accede al [Archivo de CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive) y selecciona la versión que verificaste anteriormente. En este artículo, seleccionamos [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
Ahora selecciona la plataforma y el tipo de instalador correspondientes, y sigue las instrucciones que aparecen en la pantalla. En este punto, [es preferible usar el gestor de paquetes del sistema para el instalador](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). Mi método preferido es deb (network).  
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
Si tienes buen ojo, habrás notado que la última línea es ligeramente diferente de las instrucciones que aparecen en la imagen. En la instalación de red, si solo ingresas cuda como se muestra en la imagen, se instalará la versión más reciente, 11.2, lo cual no es lo que queremos. Puedes ver varias opciones de metapaquetes en la [Guía de instalación de CUDA 11.0 para Linux](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#package-manager-metas). Aquí, modificamos la última línea para instalar específicamente el paquete CUDA Toolkit versión 11.0 y permitir que el paquete de controladores se actualice automáticamente.

### 5-3. Instalación de cuDNN
Instala cuDNN de la siguiente manera:
```
$ sudo apt install libcudnn8=8.0.5.39-1+cuda11.0
$ sudo apt install libcudnn8-dev=8.0.5.39-1+cuda11.0
```
## 6. Instalación de PyTorch
Si creaste un entorno virtual en el paso 3, procede con el entorno virtual que planeas usar activado. Si no necesitas PyTorch, omite este paso.  
Accede a la [página de inicio de PyTorch](https://pytorch.org/get-started/locally/) y selecciona la compilación de PyTorch a instalar (Stable), el sistema operativo (Linux), el paquete (Pip), el lenguaje (Python) y CUDA (11.0), luego sigue las instrucciones que aparecen en la pantalla.  
![Instalación de PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)
```
(env) $ pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
Para verificar si has instalado PyTorch correctamente, ejecuta el siguiente comando después de iniciar el intérprete de Python. Si se devuelve un tensor, has tenido éxito.
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
Si no necesitas TensorFlow, ignora este paso.  
Si instalaste PyTorch en un entorno virtual en el paso 6, desactiva ese entorno virtual, vuelve a los pasos 3 y 4 para crear y activar un nuevo entorno virtual, y luego procede. Si omitiste el paso 6, simplemente continúa.  
Instala TensorFlow de la siguiente manera:
```
(env2) $ pip install --upgrade tensorflow
```
Para verificar si has instalado TensorFlow correctamente, ejecuta el siguiente comando. Si muestra el nombre de la GPU y devuelve un tensor, has tenido éxito.
```
(env2) $ python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

2021-02-07 22:45:51.390640: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
(omitido)
2021-02-07 22:45:54.592749: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1406] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6878 MB memory) -> physical GPU (device: 0, name: GeForce RTX 3070, pci bus id: 0000:01:00.0, compute capability: 8.6)
tf.Tensor(526.1059, shape=(), dtype=float32)
```
