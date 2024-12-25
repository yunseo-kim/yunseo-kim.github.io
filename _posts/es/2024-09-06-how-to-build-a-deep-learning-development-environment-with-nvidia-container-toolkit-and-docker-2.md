---
title: Configuración del entorno de desarrollo de aprendizaje profundo con NVIDIA
  Container Toolkit y Docker (2) - Configuración del tiempo de ejecución del contenedor
  para utilizar la GPU, escritura del Dockerfile y construcción de la imagen Docker
description: Esta serie cubre cómo configurar un entorno de desarrollo de aprendizaje
  profundo basado en NVIDIA Container Toolkit y Docker localmente, y cómo configurar
  SSH y Jupyter Lab para utilizarlo como servidor remoto. Esta publicación es la primera
  de la serie e introduce cómo instalar NVIDIA Container Toolkit.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Resumen
En esta serie, cubriremos el proceso de instalación de NVIDIA Container Toolkit y Docker, y la creación de un entorno de desarrollo de aprendizaje profundo escribiendo un Dockerfile basado en las imágenes CUDA y cuDNN proporcionadas por el [repositorio nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) en Docker Hub. Para aquellos que lo necesiten, compartimos el [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) y la [imagen](https://hub.docker.com/r/yunseokim/dl-env/tags) completados a través de este proceso en GitHub y Docker Hub para que puedan usarlos libremente, y además proporcionamos una guía de configuración de SSH y Jupyter Lab para utilizarlo como servidor remoto.  
La serie constará de tres publicaciones, y esta es la segunda de ellas.
- [Parte 1: Instalación de NVIDIA Container Toolkit y Docker Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Parte 2: Configuración del tiempo de ejecución del contenedor para utilizar la GPU, escritura del Dockerfile y construcción de la imagen Docker (este artículo)
- Parte 3 (próximamente)

Procedemos asumiendo un sistema Linux x86_64 con una tarjeta gráfica NVIDIA compatible con CUDA, y aunque no hemos probado directamente en distribuciones distintas a Ubuntu o Fedora, puede haber algunas diferencias menores en algunos detalles específicos.

## Antes de empezar
Este artículo es una continuación de la [Parte 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), así que si aún no la has leído, se recomienda leerla primero.

## 4. Configuración del tiempo de ejecución del contenedor
### 4-1. Ejecutar el comando `nvidia-ctk`
```bash
sudo nvidia-ctk runtime configure --runtime=docker
```
Este comando modifica el archivo `/etc/docker/daemon.json`{: .filepath} para permitir que Docker utilice el NVIDIA Container Runtime.

### 4-2. Reiniciar el demonio Docker
Reiniciamos el demonio Docker para aplicar los cambios de configuración.
```bash
sudo systemctl restart docker
```

### 4-3. Verificar que se ha configurado correctamente
Ejecutamos un contenedor CUDA de muestra.
```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Si se muestra una pantalla similar a la siguiente, ha sido exitoso.

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

## 5. Escritura del Dockerfile
Escribimos un Dockerfile para usar como entorno de desarrollo basado en las imágenes CUDA y cuDNN proporcionadas por el [repositorio nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) en Docker Hub.

- Debemos decidir qué imagen usar considerando las versiones de CUDA y cuDNN necesarias, el tipo y versión de la distribución Linux, etc. 
- ![Versión de CUDA soportada por PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)A partir de finales de agosto de 2024, cuando se escribió este artículo, la versión más reciente de PyTorch, 2.4.0, soporta CUDA 12.4. Por lo tanto, aquí usaremos la imagen [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Puedes verificar la versión más reciente de PyTorch y la versión de CUDA soportada en la [página web de PyTorch](https://pytorch.org/get-started/locally/).

El código fuente del Dockerfile completado está disponible públicamente en el repositorio de GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). A continuación, explicamos paso a paso el proceso de escritura de este Dockerfile.

### 5-1. Especificar la imagen base
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Instalar utilidades básicas y prerrequisitos de Python
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

### 5-3. Configurar la zona horaria del sistema (en este artículo, procedemos con 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. Configurar el servidor SSH para acceso remoto  
Configuramos para que no sea posible iniciar sesión en la cuenta root con contraseña durante el acceso remoto SSH por razones de seguridad.
```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```
Configuramos para que el servicio SSH se inicie automáticamente al iniciar el contenedor.
```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```
Creamos un usuario no root llamado 'remote' para usar al conectarse por SSH.
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

> Si no se especifica una opción por separado al construir la imagen Docker usando este Dockerfile, el valor inicial de la contraseña de la cuenta del usuario 'remote' es 000000. Esto es muy vulnerable en términos de seguridad, así que asegúrate de especificar una contraseña de inicio de sesión de cuenta por separado usando la opción `--build-arg` al construir la imagen Docker, o cambiar la configuración inmediatamente después de ejecutar el contenedor por primera vez. Para mayor seguridad, es deseable deshabilitar el inicio de sesión con contraseña al conectarse por SSH y configurarlo posteriormente para que solo sea posible iniciar sesión a través de un archivo de clave separado, e idealmente, utilizar una clave de hardware como Yubikey.
> La configuración del servidor SSH se tratará hasta cierto punto en la próxima parte de esta serie, y si quieres saber más, puedes consultar los documentos en la siguiente lista.
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Instalar setuptools, pip y registrar la variable de entorno PATH
```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. Instalar paquetes de aprendizaje automático y aprendizaje profundo para usar en el entorno de desarrollo
```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
Si quieres usar Cupy, cuDF, cuML y DALI, agrega también lo siguiente al Dockerfile:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Configurar la ejecución de JupyterLab al iniciar el contenedor
```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
```

## 6. Construcción de la imagen Docker y ejecución del contenedor
### 6-1. Construcción de la imagen
Abre una terminal en el directorio donde se encuentra el Dockerfile y ejecuta el siguiente comando:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> En el lugar de \<password\>, ingresa la contraseña de inicio de sesión que usarás para la conexión SSH.
{: .prompt-info }

### 6-2. Ejecutar una carga de trabajo de muestra
Una vez completada la construcción, verifica si funciona correctamente ejecutando un contenedor desechable con el siguiente comando:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```
Al ingresar este comando en la terminal, se ejecutará un contenedor llamado `test-container` a partir de la imagen `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` que construimos anteriormente, y conectará el puerto 88 del sistema host al puerto 8888 de ese contenedor. Si la imagen Docker se construyó correctamente en el paso anterior y el contenedor se inició sin problemas, JupyterLab debería estar ejecutándose en la dirección predeterminada `http:127.0.0.1:8888` dentro del contenedor `test-container`. Por lo tanto, al abrir un navegador en el sistema host donde se ejecuta Docker Engine y acceder a <http://127.0.0.1:88>, debería conectarse a la dirección `http://127.0.0.1:8888` dentro del contenedor y mostrar una pantalla como la siguiente:

![Captura de pantalla de la interfaz de JupyterLab](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (opcional) Subir a Docker Hub
Para poder utilizar la imagen del entorno de desarrollo que creamos a través del proceso anterior en cualquier momento que sea necesario, es bueno subirla a Docker Hub.  

> Para subir tu propia imagen a Docker Hub, necesitas tu propia cuenta de Docker, así que si aún no tienes una, primero completa el registro en <https://app.docker.com/signup>.
{: .prompt-tip }

Primero, inicia sesión en Docker Hub con el siguiente comando:
```bash
docker login
```
Ahora, ejecuta un comando con el siguiente formato para crear una etiqueta de imagen:
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```
Finalmente, ejecuta el siguiente comando para subir la imagen a Docker Hub:
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Puedes confirmar que se ha subido correctamente en <https://hub.docker.com/> como se muestra a continuación:  
![Captura de pantalla de Docker Hub](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

La imagen completada a través del proceso anterior está disponible públicamente en el repositorio público [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) en Docker Hub, y cualquiera puede usarla libremente.
