---
title: Configuración de un entorno de desarrollo de aprendizaje profundo con NVIDIA Container Toolkit y Docker/Podman (2) - Configuración del runtime de contenedor para utilizar GPU, escritura de Dockerfile y construcción de imagen de contenedor
description: Esta serie cubre cómo configurar un entorno de desarrollo de deep learning basado en contenedores con NVIDIA Container Toolkit localmente, y cómo configurar SSH y Jupyter Lab para utilizarlo como servidor remoto. Esta publicación es la segunda de la serie y cubre el proceso de escribir un Dockerfile y construir una imagen de contenedor.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---
## Descripción general
En esta serie, cubrimos el proceso de instalación de NVIDIA Container Toolkit y Docker o Podman, y la creación de un entorno de desarrollo de deep learning escribiendo un Dockerfile basado en imágenes CUDA y cuDNN proporcionadas por el [repositorio nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) en Docker Hub. Comparto el [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) y la [imagen](https://hub.docker.com/r/yunseokim/dl-env/tags) completados a través de GitHub y Docker Hub para que cualquiera pueda usarlos libremente, y además proporciono una guía para configurar SSH y Jupyter Lab para su uso como servidor remoto.  
La serie constará de 3 artículos, y este que estás leyendo es el segundo de la serie.
- [Parte 1: Instalación de NVIDIA Container Toolkit y motor de contenedores](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Parte 2: Configuración del runtime de contenedor para utilizar GPU, escritura de Dockerfile y construcción de imagen de contenedor (este artículo)
- Parte 3 (próximamente)

Procederemos asumiendo un sistema Linux x86_64 con una tarjeta gráfica NVIDIA que soporte CUDA, y aunque no he probado personalmente distribuciones distintas a Ubuntu o Fedora, algunos detalles específicos pueden variar ligeramente.  
(Actualizado el 18.02.12025)

> **Aviso de corrección de errores**  
> En la versión inicial de este artículo subida en agosto del año [holocene](https://en.wikipedia.org/wiki/Holocene_calendar) 12024, había algunos errores en la sección [Escritura del Dockerfile](#5-escritura-del-dockerfile) y en la imagen construida a partir de dicho Dockerfile. Los problemas eran los siguientes:
> - La parte de creación de la cuenta remote donde se configura la contraseña era incorrecta, y aunque debería haber sido posible iniciar sesión con la contraseña "000000", no funcionaba
> - El demonio SSH no se iniciaba automáticamente al arrancar el contenedor
>
> Recientemente me di cuenta de estos problemas y alrededor de las 2 AM (UTC+9) del 16 de febrero de 12025, reemplacé el Dockerfile problemático y las imágenes Docker con archivos corregidos en el [repositorio GitHub](https://github.com/yunseo-kim/dl-env-docker) y [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> Si descargaste el Dockerfile o la imagen Docker antes de esa fecha, por favor actualízalos a la versión corregida.  
> Me disculpo con quienes hayan experimentado confusión debido a la información incorrecta.
{: .prompt-info }

## Antes de empezar
Este artículo es una continuación de la [Parte 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), así que si aún no la has leído, te recomiendo que la leas primero.

## 4. Configuración del runtime de contenedor
### Si usas Podman
[Configura utilizando CDI (Container Device Interface)](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Ejecuta el siguiente comando para generar el archivo de especificaciones CDI en el directorio `/etc/cdi`{: .filepath}:
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> Si cambias tu tarjeta gráfica o modificas la configuración del controlador CUDA (incluyendo actualizaciones de versión), deberás generar un nuevo archivo de especificaciones CDI.
{: .prompt-warning }

> El uso del hook de NVIDIA Container Runtime junto con CDI puede causar conflictos, así que si existe el archivo `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath}, elimínalo o ten cuidado de no ejecutar contenedores con la variable de entorno `NVIDIA_VISIBLE_DEVICES` configurada.
{: .prompt-warning }

### Si usas Docker
Explicaré basándome en el [modo rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configurar el runtime de contenedor con el comando `nvidia-ctk`
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
Este comando modifica el archivo `/etc/docker/daemon.json`{: .filepath} para permitir que Docker utilice NVIDIA Container Runtime.

#### 4-Docker-2. Reiniciar el demonio Docker
Reinicia el demonio Docker para aplicar los cambios:
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configurar el archivo `/etc/nvidia-container-runtime/config.toml`{: .filepath} con el comando `sudo nvidia-ctk`
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Verificar que todo esté configurado correctamente
Ejecuta un contenedor CUDA de prueba.

Si usas Podman, ejecuta:
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Si usas Docker, ejecuta:
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Si ves una salida similar a la siguiente, la configuración ha sido exitosa:

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
Escribiremos un Dockerfile para nuestro entorno de desarrollo basado en las imágenes CUDA y cuDNN proporcionadas por el [repositorio nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) en Docker Hub.

- Debes decidir qué imagen usar considerando las versiones de CUDA y cuDNN que necesitas, así como el tipo y versión de distribución Linux.
- ![Versión CUDA soportada por PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)A finales de agosto de 12024, cuando se escribió este artículo, la versión más reciente de PyTorch (2.4.0) soporta CUDA 12.4. Por lo tanto, usaremos la imagen [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Puedes verificar la versión más reciente de PyTorch y las versiones de CUDA compatibles en la [página web de PyTorch](https://pytorch.org/get-started/locally/).

El Dockerfile completo está disponible en el repositorio GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). A continuación, explicaré el proceso de creación paso a paso.

### 5-1. Especificar la imagen base
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Instalar utilidades básicas y prerrequisitos de Python
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

### 5-3. Configurar la zona horaria del sistema (en este artículo usamos 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. Configurar el servidor SSH para acceso remoto
Configuramos el servidor SSH para que no permita inicios de sesión como root por motivos de seguridad:
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Creamos un usuario no-root llamado 'remote' para las conexiones SSH:
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

> Si no especificas opciones adicionales al construir la imagen Docker con este Dockerfile, la contraseña inicial para el usuario 'remote' será 000000. Esto es extremadamente vulnerable desde el punto de vista de seguridad, así que deberías especificar una contraseña diferente usando la opción `--build-arg` al construir la imagen, o cambiar la configuración inmediatamente después de ejecutar el contenedor por primera vez. Para mayor seguridad, es recomendable desactivar el inicio de sesión por contraseña para SSH y permitir solo inicios de sesión mediante archivos de clave, e idealmente utilizar hardware como Yubikey.
> La configuración del servidor SSH se tratará en cierta medida en la próxima parte de esta serie, pero si quieres saber más, puedes consultar los siguientes documentos:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> Además, este Dockerfile asume que la imagen construida será utilizada solo por ti o por un pequeño grupo de personas de confianza. Si necesitas distribuir la imagen sin exponer información sensible, usar `--build-arg` para configurar contraseñas es peligroso. Consulta [este documento](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/) para más información.
{: .prompt-danger }

### 5-5. Instalar setuptools, pip y registrar la variable de entorno PATH
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. Instalar paquetes de machine learning y deep learning
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Si quieres usar Cupy, cuDF, cuML y DALI, añade lo siguiente al Dockerfile:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Crear un directorio para usar como espacio de trabajo
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Exponer puertos y configurar `ENTRYPOINT` para ejecutar al iniciar el contenedor
Exponemos los puertos 22 y 8888 para SSH y Jupyter Lab.  
Además, para ejecutar automáticamente el demonio SSH al iniciar el contenedor, necesitamos privilegios de root, así que usaremos el siguiente método:
1. Iniciar el contenedor como usuario root
2. Ejecutar el script `/entrypoint.sh`{: .filepath} inmediatamente después de iniciar el contenedor
3. En ese script, iniciar el servicio SSH y luego cambiar al usuario remote usando [`gosu`](https://github.com/tianon/gosu)
4. Si no se especifica ningún comando al ejecutar el contenedor, ejecutar Jupyter Lab como usuario remote (con privilegios no-root) por defecto

> Generalmente, no se recomienda usar `sudo` o `su` dentro de contenedores Docker o Podman. Si necesitas privilegios de root, es mejor iniciar el contenedor como root, realizar las tareas que requieren privilegios de root, y luego cambiar a un usuario no-root usando [`gosu`](https://github.com/tianon/gosu), como se explica aquí. Las razones para esto se explican detalladamente en los siguientes recursos:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Primero, añade lo siguiente al final del Dockerfile:
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Luego, crea un archivo de script llamado `entrypoint.sh`{: .filepath} en la misma ubicación que tu Dockerfile con el siguiente contenido:
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

## 6. Construir la imagen Docker y ejecutar el contenedor
### 6-1. Construir la imagen
Abre una terminal en el directorio donde se encuentra el Dockerfile y ejecuta:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Reemplaza \<password\> con la contraseña que quieres usar para iniciar sesión SSH.
{: .prompt-info }

### 6-2. Ejecutar una carga de trabajo de prueba
Una vez completada la construcción, ejecuta un contenedor desechable para verificar que todo funciona correctamente.

Si usas Podman, ejecuta:
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Si usas Docker, ejecuta:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Este comando ejecuta un contenedor llamado `test-container` a partir de la imagen `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` que acabamos de construir, y mapea el puerto 22 del host al puerto 22 del contenedor, y el puerto 88 del host al puerto 8888 del contenedor. Si la imagen Docker se construyó correctamente y el contenedor se inició sin problemas, JupyterLab debería estar ejecutándose en la dirección `http:127.0.0.1:8888` dentro del contenedor. Por lo tanto, al abrir un navegador en el sistema host donde se ejecuta Docker Engine y acceder a <http://127.0.0.1:88>, deberías conectarte a la dirección `http://127.0.0.1:8888` dentro del contenedor y ver una pantalla como esta:

![Captura de pantalla de la interfaz de JupyterLab](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Abre una terminal en el sistema host y ejecuta el comando `ssh remote@127.0.0.1` para iniciar sesión remotamente en la cuenta remote del sistema Ubuntu que se ejecuta dentro del contenedor.  
La primera vez que inicies sesión, aparecerá una advertencia indicando que no hay información sobre la clave de cifrado del destino y que la autenticación no es posible, y te preguntará si deseas continuar con la conexión. Ingresa "yes" para continuar.  
Luego, ingresa la contraseña para iniciar sesión (si no la cambiaste durante la construcción de la imagen, el valor predeterminado es "000000").
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {huella digital (cada clave tiene un valor único)}.
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
Si ves una salida similar a la anterior, has iniciado sesión correctamente a través de SSH. Para cerrar la sesión, ingresa el comando `exit`.

### 6-3. (opcional) Subir a Docker Hub
Si quieres poder utilizar la imagen de entorno de desarrollo que has creado en cualquier momento, es buena idea subirla a Docker Hub.

> Para subir tu imagen a Docker Hub, necesitas tener una cuenta de Docker. Si aún no tienes una, regístrate primero en <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Iniciar sesión en Docker Hub
##### Si usas Podman
```bash
podman login docker.io
```

##### Si usas Docker
```bash
docker login
```

#### 6-3-2. Etiquetar la imagen
Reemplaza `<dockerhub_username>`, `<repository_name>` y (opcional) `:TAG` con tus propios valores.  
Por ejemplo: "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### Si usas Podman
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Si usas Docker
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Subir la imagen
Finalmente, ejecuta el siguiente comando para subir la imagen a Docker Hub:

##### Si usas Podman
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Si usas Docker
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Puedes verificar que la imagen se ha subido correctamente en <https://hub.docker.com/>, como se muestra a continuación:  
![Captura de pantalla de Docker Hub](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

La imagen completada a través de este proceso está disponible públicamente en el repositorio [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) en Docker Hub, y cualquiera puede usarla libremente.

Para descargar la imagen, simplemente cambia `push` por `pull` en el comando que usaste para subirla.
