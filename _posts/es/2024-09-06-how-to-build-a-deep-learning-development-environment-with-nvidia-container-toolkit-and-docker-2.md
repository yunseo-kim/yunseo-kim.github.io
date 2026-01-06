---
title: "Construir un entorno de desarrollo de deep learning con NVIDIA Container Toolkit y Docker/Podman (2): configuración del runtime de contenedores para usar la GPU, creación del Dockerfile y build de la imagen"
description: "La serie explica cómo montar en local un entorno de deep learning basado en contenedores con NVIDIA Container Toolkit y habilitar su uso como servidor remoto mediante SSH y JupyterLab. Este segundo post cubre la creación del Dockerfile y el proceso de build de la imagen."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Resumen

En esta serie se cubre el proceso de instalar NVIDIA Container Toolkit y Docker o Podman, y de construir un entorno de desarrollo de deep learning escribiendo un Dockerfile basado en las imágenes de CUDA y cuDNN que ofrece el [repositorio nvidia/cuda de Docker Hub](https://hub.docker.com/r/nvidia/cuda). Para que cualquiera pueda reutilizarlo libremente, comparto el [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) y la [imagen](https://hub.docker.com/r/yunseokim/dl-env/tags) resultantes a través de GitHub y Docker Hub, y adicionalmente ofrezco una guía para configurar SSH y JupyterLab con el fin de usarlo como servidor remoto.  
La serie constará de 3 entradas, y esta que estás leyendo es la segunda.
- [Parte 1: instalación de NVIDIA Container Toolkit y del motor de contenedores](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Parte 2: configuración del runtime de contenedores para usar la GPU, creación del Dockerfile y build de la imagen (este post)
- Parte 3 (pendiente de publicación)

Se asume un sistema x86_64 con Linux y una GPU NVIDIA compatible con CUDA; no he probado directamente distribuciones distintas de Ubuntu o Fedora, así que algunos detalles podrían variar ligeramente.  
(12026.1.6. revisado)

> **Aviso de corrección de errores**
>
> En el borrador inicial de este post, publicado en agosto de 12024, había algunos errores en la sección de [creación del Dockerfile](#5-creación-del-dockerfile) y en parte de la imagen construida a partir de dicho Dockerfile. Los puntos problemáticos eran los siguientes:
> - En la parte de creación de la cuenta `remote`, el paso de establecer contraseña era incorrecto: se indicaba que se podía iniciar sesión usando "000000" como contraseña inicial, pero en realidad no era así (añadido el 12025.12.19: ahora la contraseña inicial ya no es "000000", así que asegúrate de revisar [el contenido de abajo](#5-4-configuración-del-servidor-ssh-para-acceso-remoto)).
> - Al arrancar el contenedor, el daemon de SSH no se iniciaba automáticamente.
>
> Identifiqué estos problemas en febrero de 12025 y, en horario de Corea (UTC+9), alrededor de las 2:00 a. m. del 16 de febrero de 12025, reemplacé en el [repositorio de GitHub](https://github.com/yunseo-kim/dl-env-docker) y en [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) el Dockerfile y las imágenes con versiones corregidas.  
> Si hiciste pull del Dockerfile o de la imagen antes de ese momento, sustitúyelos por la versión corregida.  
> Pido disculpas a quienes se hayan confundido por el contenido incorrecto.
{: .prompt-info }

## Antes de empezar

Este post continúa desde la [Parte 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1); si aún no la has leído, se recomienda hacerlo primero.

## 4. Configuración del runtime de contenedores

### Si usas Podman

[Se configura utilizando CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> En versiones antiguas, al instalar por primera vez NVIDIA Container Toolkit, y también cada vez que se cambiaba la configuración (incluida la actualización de versión) del dispositivo GPU o del driver, había que regenerar manualmente el fichero de especificación CDI.
>
> Sin embargo, desde NVIDIA Container Toolkit `v1.18.0`, mediante el servicio systemd `nvidia-cdi-refresh`, el fichero de especificación CDI `/var/run/cdi/nvidia.yaml` se genera y actualiza automáticamente en los siguientes casos:
> - al instalar o actualizar NVIDIA Container Toolkit
> - al instalar o actualizar el driver de NVIDIA GPU
> - al reiniciar el sistema
>
> Por tanto, a diferencia de antes, ya no hace falta hacer nada manualmente. He actualizado el contenido del post para reflejarlo.
>
> No obstante, si se elimina el driver de GPU o se reconfigura un dispositivo MIG, `nvidia-cdi-refresh` no lo gestiona; en ese caso hay que reiniciar manualmente `nvidia-cdi-refresh.service` para forzar la regeneración de la especificación CDI.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> Usar el hook de NVIDIA Container Runtime junto con CDI puede causar conflictos; si existe `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath}, elimina ese archivo o asegúrate de no ejecutar contenedores con la variable de entorno `NVIDIA_VISIBLE_DEVICES` configurada.
{: .prompt-warning }

### Si usas Docker

Se explica tomando como referencia el [modo rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configurar el runtime de contenedores con el comando `nvidia-ctk`

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

El comando anterior modifica el archivo `/etc/docker/daemon.json`{: .filepath} para que Docker pueda usar NVIDIA Container Runtime.

#### 4-Docker-2. Reiniciar el daemon de Docker

Reinicia el daemon de Docker para aplicar los cambios.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configurar el archivo `/etc/nvidia-container-runtime/config.toml`{: .filepath} con `sudo nvidia-ctk`

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Verificar que se configuró correctamente

Ejecuta un contenedor CUDA de ejemplo.

Si usas Podman, ejecuta:

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Si usas Docker, ejecuta:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

Si aparece una pantalla similar a la siguiente, es que ha funcionado.

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

## 5. Creación del Dockerfile

Se escribe un Dockerfile para usarlo como entorno de desarrollo, basado en las imágenes de CUDA y cuDNN que ofrece el [repositorio nvidia/cuda de Docker Hub](https://hub.docker.com/r/nvidia/cuda).

- Debes decidir qué imagen usar teniendo en cuenta la versión de CUDA/cuDNN necesaria, la distribución Linux, su versión, etc.
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  A finales de agosto de 12024, cuando se escribió este post, la versión más reciente de PyTorch era 2.4.0 y soportaba CUDA 12.4. Por ello aquí se usa la imagen [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). En la [web de PyTorch](https://pytorch.org/get-started/locally/) puedes comprobar la versión más reciente y la versión de CUDA soportada.

El código fuente del Dockerfile final se ha publicado en el repositorio de GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). A continuación explico paso a paso el proceso para escribirlo.

> (+ 12026.1.6. revisado)  
> Añadí Dockerfiles e imágenes que soportan PyTorch 2.9.1 y CUDA 12.8 / 13.0 en el mismo repositorio de GitHub y en el repositorio público de Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags). El contenido del post también se actualizó para encajar con PyTorch 2.9.1 y CUDA 13.0.
>
> Además, incluí scikit-image y XGBoost, y dentro del ecosistema RAPIDS incluí las librerías cuGraph, cuxfilter, cuCIM, RAFT y cuVS, y agregué soporte `arm64` además del `amd64` existente.
{: .prompt-info }

### 5-1. Especificar la imagen base

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. Configurar la zona horaria del sistema (en este post, 'Asia/Seoul')

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> Me basé principalmente en el contenido de [este artículo](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22).
{: .prompt-tip }

### 5-3. Instalar utilidades básicas del sistema

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

### 5-4. Configuración del servidor SSH para acceso remoto

Por seguridad, configura SSH para que no sea posible iniciar sesión remota como root.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Crea un usuario no root llamado `remote` que se usará para conectarse por SSH.

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

> El contenido de los argumentos de build (`ARG`) o de variables de entorno (`ENV`) queda expuesto tal cual en la imagen construida, así que al especificar información sensible como [contraseñas o claves API hay que usar otros métodos](https://docs.docker.com/build/building/secrets/). Aquí se usó [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts).
{: .prompt-danger }

> Como se explicará [más adelante](#6-1-build-de-la-imagen), al construir una imagen usando este Dockerfile debes indicar, mediante la variable de entorno `DL_ENV_PASSWD`, la cadena que se usará como contraseña de la cuenta de usuario. En el caso de la [imagen distribuida en Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags), la contraseña inicial de la cuenta es `satisfied-flip-remake`; usar esta contraseña pública por defecto tal cual es extremadamente inseguro, así que cambia la configuración inmediatamente después de ejecutar el contenedor por primera vez. Además, por seguridad es recomendable deshabilitar el login por contraseña en SSH y configurar que el acceso solo sea posible mediante un archivo de clave; idealmente, también puedes usar una llave hardware como Yubikey.
>
> Sobre la configuración del servidor SSH, planeo cubrirlo parcialmente en la siguiente entrada de esta serie; si quieres más detalle, consulta los siguientes documentos:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Instalar uv y registrar variables de entorno

> **Reflejar PEP 668 y adoptar uv para Externally Managed Environments (12026.1.6. revisado)**
>
> En el pasado, este post proponía escribir el Dockerfile de manera que se instalaran paquetes con `pip` directamente dentro de la imagen del contenedor sin crear un entorno virtual (`venv`). La razón era que, dentro de una imagen de contenedor de propósito único, el riesgo de romper el software del sistema es menor y, incluso si ocurre algún problema, basta con recrear un contenedor desde la imagen, por lo que parecía menos necesario crear un entorno virtual. Este punto también se reconoce parcialmente en [PEP 668](https://peps.python.org/pep-0668/#use-cases) de la siguiente forma.
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> Sin embargo, incluso en una imagen de contenedor de propósito único, se ha establecido como estándar instalar mediante gestores como `pip` únicamente dentro de un entorno virtual, separando estrictamente los paquetes gestionados externamente (externally managed) mediante el gestor de paquetes del sistema operativo, etc. En consecuencia, he revisado el contenido para crear un entorno virtual e instalar dentro de él los paquetes necesarios, cumpliendo [PEP 668](https://peps.python.org/pep-0668/) y la especificación de [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) y alineándome con el estándar del ecosistema Python.
>
> La librería estándar oficialmente soportada para crear y gestionar entornos virtuales en Python es `venv`, como ya presenté una vez en [otro post escrito a principios de 12021](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended). No obstante, desde que [Astral](https://astral.sh/) publicó en 12024 un gestor de paquetes y proyectos Python de alto rendimiento desarrollado en Rust, [`uv`](https://docs.astral.sh/uv/), este se ha convertido rápidamente en un nuevo estándar de facto en el ecosistema Python por varias ventajas importantes:
> - Velocidad de resolución de dependencias e instalación de paquetes abrumadoramente superior frente a [`pip` (10–100×)](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md)
> - Excelente facilidad de uso
> - [Muy buena compatibilidad con `pip` y `venv`](https://docs.astral.sh/uv/pip/)
>
> En particular, los paquetes de ML como PyTorch o RAPIDS que se tratan aquí tienen muchas dependencias y suelen ser grandes, por lo que estas ventajas de `uv` se aprovechan al máximo. Además, como [`uv` usa la caché de forma activa y eficiente](https://docs.astral.sh/uv/concepts/cache/), si durante el build de la imagen se utilizan adecuadamente los cache mounts como aquí, [se puede maximizar esa ventaja y reducir mucho el tiempo de build](https://docs.astral.sh/uv/guides/integration/docker/#caching). Por ello, aquí también adoptaré `uv` para crear/gestionar entornos virtuales e instalar paquetes. Me basé principalmente en la documentación oficial ["Using uv in Docker"](https://docs.astral.sh/uv/guides/integration/docker/).
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

> **Por qué se define `UV_CACHE_DIR` en `"/tmp/uv-cache"` en lugar del valor por defecto `"$HOME_DIR/.cache/uv"`**
>
> Normalmente, si se añade un usuario con `useradd --create-home`, ese usuario debe tener la propiedad de su propio directorio home, y aquí también es así.
> Sin embargo, al hacer build de una imagen con Podman, descubrí un bug por el cual, aunque en capas anteriores se haya cambiado correctamente la propiedad, al montar cachés (etc.) en capas posteriores, los metadatos de propiedad del directorio padre se restablecen al valor por defecto (propiedad de root). Buscando, encontré un [issue reportado por otro usuario sobre el mismo fenómeno hace unas ~3 semanas](https://github.com/containers/podman/issues/27777), pero todavía no hay respuesta. Dejé información detallada de mi caso en [un comentario adicional de ese issue](https://github.com/containers/podman/issues/27777#issuecomment-3712237296).
>
> Por ello, para que no sea un problema aunque la propiedad se restablezca a root, en la fase de build fijé `UV_CACHE_DIR` a una ruta distinta de `$HOME_DIR`, `"/tmp/uv-cache"`. De todos modos, esta caché no se incluye en la imagen final resultante, así que no importa cambiar la ruta adecuadamente.
{: .prompt-tip }

### 5-6. Instalar Python, crear entorno virtual, instalar setuptools y pip

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

### 5-7. Instalar paquetes de ML/DL para el entorno de desarrollo

#### 5-7-1. Paquetes comunes

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch y librerías de aceleración GPU específicas de CUDA

##### Si solo vas a instalar PyTorch

Si solo quieres instalar PyTorch, añade lo siguiente al Dockerfile.

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch + CuPy + RAPIDS + DALI

Si además de PyTorch quieres usar CuPy, RAPIDS (cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS) y DALI, añade lo siguiente al Dockerfile.

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

> En este caso, los paquetes de PyTorch y RAPIDS comparten algunas librerías de dependencias (cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE); si se instalan por separado, aumenta mucho el riesgo de que las versiones requeridas difieran y de que una instalación posterior sobrescriba lo anterior provocando conflictos de dependencias. Por eso, al instalar estos paquetes conviene unificarlo en un único comando `uv pip install`, para que el resolvedor considere todas las restricciones a la vez y se prioricen las versiones requeridas por PyTorch.
{: .prompt-tip }

### 5-8. Crear el directorio que se usará como espacio de trabajo

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. Abrir puertos y configurar el `ENTRYPOINT` que se ejecutará al iniciar el contenedor
Para acceder por SSH y Jupyter Lab se abren los puertos 22 y 8888.  
Además, para arrancar automáticamente el daemon de SSH al iniciar el contenedor se necesitan privilegios root, así que se usará el siguiente enfoque:
1. Iniciar el contenedor estando logueado como root
2. Ejecutar el script `/entrypoint.sh`{: .filepath} justo después de iniciar el contenedor
3. En ese script, arrancar el servicio SSH y luego cambiar al usuario `remote` usando [`gosu`](https://github.com/tianon/gosu)
4. Si al ejecutar el contenedor no se especifica un comando aparte, por defecto ejecutar Jupyter Lab como `remote` (sin privilegios root)

> En general no se recomienda usar `sudo` o `su` dentro de contenedores Docker/Podman; cuando se necesita privilegio root, es mejor iniciar el contenedor como root, realizar las tareas que lo requieran y después cambiar a un usuario no root con [`gosu`](https://github.com/tianon/gosu) tal como se describe aquí. Las razones están explicadas en detalle en los materiales siguientes:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Primero, en la parte final del Dockerfile, añade lo siguiente.

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Después, en la misma ruta donde está el Dockerfile, crea un script llamado `entrypoint.sh`{: .filepath} con el contenido siguiente.

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

> En general, los procesos ejecutados con `docker exec` o con `CMD` heredan tal cual el `ENV` de Docker, pero las sesiones que entran por SSH a menudo no heredan automáticamente las variables de entorno de Docker. Esto se debe a que SSH crea una nueva sesión de shell al iniciar sesión.
>
> Para resolverlo y permitir que también por SSH se pueda acceder a variables de entorno definidas previamente como `$WORK_DIR`, es necesario volcar antes esas variables en `/etc/environment`{: .filepath} con algo como `printenv | grep _ >> /etc/environment` antes de arrancar el servicio SSH al ejecutar el contenedor.
>
> Pueden ser útiles estos enlaces:
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. Build de la imagen OCI y ejecución del contenedor

### 6-1. Build de la imagen

Abre un terminal en el directorio donde está el Dockerfile y define la variable de entorno `DL_ENV_PASSWD`.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> Sustituye \<your_own_password\> por la contraseña de login que usarás al conectarte por SSH.
{: .prompt-info }

Ahora, **sin cerrar esa ventana del terminal**, ejecuta en la misma ventana los comandos de abajo para realizar el build.

#### En Podman

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> En Podman, si de cara a distribución quieres construir la imagen no solo para la plataforma (SO/arquitectura) de tu equipo sino para todas las plataformas soportadas por la imagen base, especifica la [opción `--all-platforms`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms) y usa `--manifest` en lugar de [`--tag` o `-t`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant), así:
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> En el caso de Docker no lo organizo aquí aparte; si lo necesitas, consulta la [documentación oficial de Docker](https://docs.docker.com/build/building/multi-platform/).
{: .prompt-tip }

#### En Docker

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. Ejecutar una carga de trabajo de ejemplo

Cuando termines el build, ejecuta un contenedor desechable para comprobar que funciona.

En Podman:

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

En Docker:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Al introducir el comando anterior en la terminal, se ejecuta un contenedor llamado `test-container` a partir de la imagen `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04`, y se conectan el puerto 2222 del host con el puerto 22 del contenedor, y el puerto 8888 del host con el puerto 8888 del contenedor. Si en los pasos anteriores la imagen se construyó correctamente y el contenedor arrancó sin problemas, dentro del contenedor JupyterLab estará ejecutándose en la dirección por defecto `http:127.0.0.1:8888`. Por tanto, si en el host donde corre Podman/Docker abres el navegador y entras a <http://127.0.0.1:8888>, se conectará a `http://127.0.0.1:8888` dentro del contenedor y debería mostrarse una pantalla como la siguiente.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

En el host, abre un terminal y ejecuta `ssh remote@127.0.0.1 -p 2222` para probar el login remoto con la cuenta `remote` del Ubuntu dentro del contenedor.  
La primera vez no tendrás información sobre la clave del host y aparecerá una advertencia diciendo que no se puede autenticar; te preguntará si quieres continuar, y puedes escribir "yes" para seguir.  
Después, para iniciar sesión, introduce la contraseña que definiste durante el build (o si has hecho pull de la [imagen distribuida en Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) y es tu primer login, la contraseña inicial `satisfied-flip-remake`).

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {huella digital (cada clave tiene un valor único diferente)}.
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

Si aparece algo similar a lo anterior, el login remoto por SSH habrá sido exitoso. Para salir, ejecuta `exit`.

### 6-3. (opcional) Push a Docker Hub

Para poder hacer pull y reutilizar la imagen del entorno de desarrollo en cualquier momento, es buena idea subir (push) la imagen construida a Docker Hub.  

> Para hacer push de tu imagen a Docker Hub necesitas una cuenta de Docker; si aún no la tienes, completa el registro primero en <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Login en Docker Hub

##### En Podman

```bash
podman login docker.io
```

##### En Docker

```bash
docker login
```

#### 6-3-2. Etiquetar la imagen

En `<dockerhub_username>`, `<repository_name>` y (opcional) `:TAG`, rellena con tus valores.  
Por ejemplo: "yunseokim", "dl-env", "rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04"

> Si antes construiste la imagen no solo para la plataforma (SO/arquitectura) de tu equipo, sino también para todas las plataformas soportadas por la imagen base, y quieres hacer push del manifest list o del image index de una sola vez, omite este paso y pasa directamente a [Push de la imagen](#6-3-3-push-de-la-imagen), siguiendo el método indicado allí.
{: .prompt-tip }

##### En Podman

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### En Docker

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push de la imagen

Por último, ejecuta el siguiente comando para hacer push de la imagen a Docker Hub.

##### En Podman

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> En Podman, para hacer push de una vez de las imágenes para múltiples plataformas empaquetadas en un manifest list o image index, usa el comando [`podman manifest push`](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls) como sigue:
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> Por ejemplo:
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### En Docker

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

En <https://hub.docker.com/> podrás verificar que se subió correctamente, como en el ejemplo siguiente.

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

La imagen final construida con el proceso anterior se ha publicado en el repositorio público de Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags), y cualquiera puede usarla libremente.

Para hacer pull de la imagen, basta con cambiar `push` por `pull` en el comando que usaste para subirla.
