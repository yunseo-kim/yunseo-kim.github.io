---
title: "Construyendo un entorno de desarrollo de aprendizaje profundo con NVIDIA Container Toolkit y Docker (1) - Instalación de NVIDIA Container Toolkit y Docker Engine"
description: >-
  Esta serie cubre cómo configurar un entorno de desarrollo de aprendizaje profundo basado en NVIDIA Container Toolkit y Docker localmente, y cómo configurar SSH y Jupyter Lab para utilizarlo como servidor remoto. Esta publicación es la primera de la serie e introduce cómo instalar NVIDIA Container Toolkit.
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
---

## Resumen
Esta serie cubre el proceso de instalación de NVIDIA Container Toolkit y Docker, y la creación de un entorno de desarrollo de aprendizaje profundo escribiendo un Dockerfile basado en imágenes CUDA y cuDNN proporcionadas por el [repositorio nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) en Docker Hub. Para aquellos que lo necesiten, compartimos el [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) y la [imagen](https://hub.docker.com/r/yunseokim/dl-env/tags) completados a través de este proceso en GitHub y Docker Hub para que puedan usarse libremente, y adicionalmente proporcionamos una guía de configuración de SSH y Jupyter Lab para su uso como servidor remoto.  
La serie constará de 3 publicaciones, y esta es la primera de ellas.
- Parte 1: Instalación de NVIDIA Container Toolkit y Docker Engine (este artículo)
- [Parte 2: Configuración del tiempo de ejecución del contenedor para utilizar GPU, escritura de Dockerfile y construcción de imagen Docker](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Parte 3 (próximamente)

Asumimos un sistema con una tarjeta gráfica NVIDIA compatible con CUDA en un entorno Linux x86_64, y aunque algunos detalles específicos pueden variar ligeramente en distribuciones distintas a Ubuntu o Fedora, ya que no se han probado directamente.

### Configuración del entorno de desarrollo
- Sistema operativo y arquitectura del host: Entorno Linux x86_64 (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Pila tecnológica a construir (lenguajes y bibliotecas)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE
  - CUDA 12.4
  - cuDNN
  - JupyterLab
  - NumPy & SciPy
  - CuPy (opcional, biblioteca de matrices compatible con NumPy/SciPy para computación acelerada por GPU con Python)
  - pandas
  - cuDF (opcional, para acelerar pandas con cambios de código cero con el acelerador GPU)
  - Matplotlib & Seaborn
  - DALI (opcional, alternativa de alto rendimiento a los cargadores de datos e iteradores de datos integrados usando GPU)
  - scikit-learn
  - cuML (opcional, para ejecutar algoritmos de aprendizaje automático en GPUs con una API que sigue de cerca la API de scikit-learn)
  - PyTorch
  - OpenSSH
  - tqdm

  > Dependiendo de la situación y las preferencias personales, se puede considerar usar la biblioteca DataFrame [Polars](https://pola.rs/) en lugar de pandas. Está escrita en Rust y [muestra un rendimiento considerablemente mejor en comparación con el paquete pandas puro al procesar grandes volúmenes de datos, aunque no supera a la combinación cuDF + pandas](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), y proporciona una sintaxis más especializada para consultas. Según el [blog oficial de Polars](https://pola.rs/posts/polars-on-gpu/), planean soportar la integración con cuDF en un futuro cercano en colaboración con el equipo de NVIDIA RAPIDS.
  {: .prompt-tip }

### Tabla comparativa con la guía anterior de configuración del entorno de desarrollo de aprendizaje automático
Ya existe [una guía de configuración del entorno de desarrollo de aprendizaje automático que subí previamente a este blog](/posts/Setting-up-a-Machine-Learning-Development-Environment) que sigue siendo válida en su mayoría, pero hay algunos cambios, por lo que escribí esta nueva publicación. Las diferencias se resumen en la siguiente tabla.

| Diferencia | Publicación anterior (versión 2021) | Este artículo (versión 2024) |
| --- | --- | --- |
| Distribución Linux | Basado en Ubuntu | Aplicable a Ubuntu, Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Método de construcción del entorno de desarrollo | Entorno virtual de Python usando venv | Entorno basado en contenedores Docker usando<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalación del controlador gráfico NVIDIA | O | O |
| Instalación directa de CUDA y cuDNN en el sistema host | O (usando el gestor de paquetes Apt) | X (No es necesario hacerlo directamente ya que se usa<br> una imagen preinstalada proporcionada por NVIDIA en [Docker Hub](https://hub.docker.com/r/nvidia/cuda)) |
| Portabilidad | Se debe reconstruir el entorno de desarrollo<br> cada vez que se migra a otro sistema | Basado en Docker, por lo que se puede construir fácilmente<br> una nueva imagen con el Dockerfile creado cuando sea necesario<br> o portar fácilmente la imagen existente (excluyendo<br> configuraciones adicionales de volumen o red) |
| Uso de bibliotecas de aceleración GPU adicionales además de cuDNN | X | Introducción de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interfaz de Jupyter Notebook | Jupyter Notebook (clásico) | JupyterLab (nueva generación) |
| Configuración del servidor SSH | No se trata | Incluye configuración básica del servidor SSH en la parte 3 |

Si prefieres usar un entorno virtual de Python como venv en lugar de Docker, te recomiendo consultar [la publicación anterior](/posts/Setting-up-a-Machine-Learning-Development-Environment) que sigue siendo válida.

## 0. Requisitos previos
- [NVIDIA Container Toolkit está disponible en distribuciones Linux que soportan los gestores de paquetes Apt, Yum o Dnf, Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Puedes verificar la lista de distribuciones Linux soportadas en la página enlazada, y aunque no está listada oficialmente, Fedora también se puede usar sin problemas ya que está basada en Red Hat Linux como RHEL. Si no estás familiarizado con Linux y no sabes qué distribución usar, Ubuntu LTS es la opción más segura. Es relativamente conveniente para principiantes ya que los controladores propietarios se instalan automáticamente, y como tiene muchos usuarios, la mayoría de la documentación técnica está escrita para Ubuntu.
  - Puedes verificar la arquitectura de tu sistema y la versión de la distribución Linux ejecutando el comando `uname -m && cat /etc/*release` en la terminal.
- Primero debes verificar si la tarjeta gráfica instalada en tu sistema es compatible con las versiones de CUDA y cuDNN que planeas usar.
  - Puedes verificar el modelo de GPU instalado en tu computadora ejecutando el comando `lspci | grep -i nvidia` en la terminal.
  - En la página <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, verifica la **versión del controlador NVIDIA soportada** por versión de cuDNN, los requisitos de **CUDA Compute Capability**, y la lista de **hardware NVIDIA soportado**.
  - Encuentra el modelo correspondiente en la lista de GPUs en <https://developer.nvidia.com/cuda-gpus> y verifica el valor de **Compute Capability**. Este valor debe cumplir con los requisitos de **CUDA Compute Capability** verificados anteriormente para poder usar CUDA y cuDNN sin problemas.

> Si planeas comprar una nueva tarjeta gráfica para tareas de aprendizaje profundo, los criterios de selección de GPU están bien resumidos en el siguiente artículo. El autor actualiza continuamente este artículo.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) del mismo autor también es muy útil.
{: .prompt-tip }

Si cumples con todos los requisitos mencionados anteriormente, comencemos a configurar el entorno de trabajo.

## 1. Instalación del controlador gráfico NVIDIA
Primero, debes instalar el controlador gráfico NVIDIA en el sistema host. Puedes descargar e usar el instalador .run de la [página de descarga de controladores NVIDIA](https://www.nvidia.com/drivers/), pero es preferible usar el gestor de paquetes de tu sistema para la instalación, ya que es mejor para la gestión de versiones y el mantenimiento. Consulta la documentación oficial <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> e instala el controlador gráfico adecuado para tu entorno de sistema.

### Módulo propietario vs Módulo de código abierto
El controlador NVIDIA para Linux consta de varios módulos del kernel, y a partir del controlador versión 515 y posteriores, NVIDIA proporciona dos tipos de módulos del kernel del controlador.

- Propietario: El controlador de software propietario que NVIDIA ha proporcionado tradicionalmente.
- Código abierto: Controlador de código abierto proporcionado bajo licencia dual MIT/GPLv2. El código fuente se publica a través de <https://github.com/NVIDIA/open-gpu-kernel-modules>.

El controlador propietario se proporciona para GPUs basadas en arquitecturas desde Maxwell hasta antes de Blackwell, y se discontinuará a partir de la arquitectura Blackwell.
Por otro lado, el controlador de código abierto es compatible con arquitecturas Turing y posteriores.

[NVIDIA recomienda usar el módulo del kernel de código abierto cuando sea posible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
Puedes verificar si tu GPU es compatible con el controlador de código abierto en [este enlace](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

En este artículo, asumiremos que estamos instalando el controlador de código abierto.

### Debian y Ubuntu
Para Ubuntu o Debian, ingresa los siguientes comandos en la terminal para instalar:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Basado en Fedora 40, introduciremos el método de descarga e instalación del paquete precompilado proporcionado por [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuración del repositorio RPM Fusion  
Sigue la [guía oficial de RPM Fusion](https://rpmfusion.org/Configuration).  
Ejecuta el siguiente comando en la terminal:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Instalación del paquete akmod-nvidia-open  
Consulta la [guía de instalación del controlador NVIDIA proporcionada por RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open),
activa el repositorio rpmfusion-nonfree-tainted y luego instala el paquete akmod-nvidia-open.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Registro de clave para la carga normal del controlador con el arranque seguro (Secure Boot) activado  

> Siguiendo el procedimiento adicional que se explica a continuación, puedes usar normalmente el controlador gráfico NVIDIA mientras utilizas la función de arranque seguro, y se recomienda no desactivarlo ya que la seguridad del sistema se vuelve bastante vulnerable cuando se desactiva el arranque seguro. Al menos desde la década de 2020, no hay razón para desactivar el arranque seguro en la mayoría de los casos.
{: .prompt-danger }

Primero, instala las siguientes herramientas:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Luego, ejecuta el siguiente comando para generar una clave:
```bash
sudo kmodgenca -a
```
Ahora debes registrar la clave generada en el MOK del firmware UEFI.
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Cuando ejecutes el comando anterior, se te pedirá que ingreses una contraseña para registrar la clave. En un momento reiniciaremos para completar el proceso de registro de la clave, así que ingresa una contraseña de un solo uso que puedas recordar fácilmente.

Ahora ejecuta el siguiente comando para reiniciar el sistema:
```bash
systemctl reboot
```
Cuando el sistema arranque, aparecerá automáticamente la ventana de gestión de MOK. Selecciona "Enroll MOK", luego selecciona "Continue" y "Yes" sucesivamente, y aparecerá una ventana solicitando la contraseña que configuraste hace un momento. Ingresa la contraseña que configuraste anteriormente y se completará el proceso de registro de la clave. Ahora ingresa reboot para reiniciar nuevamente y el controlador NVIDIA se cargará normalmente.

### Verificación de la instalación del controlador NVIDIA
Puedes verificar el módulo del kernel NVIDIA actualmente cargado ejecutando el siguiente comando en la terminal:
```bash
cat /proc/driver/nvidia/version
```
Si se muestra un mensaje similar al siguiente, la instalación se ha realizado correctamente:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Instalación de NVIDIA Container Toolkit
Ahora debemos instalar [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Sigue la instalación consultando la [guía oficial de instalación de NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), pero ten en cuenta que hay consideraciones especiales para Fedora durante el proceso de instalación, así que revisa todo el contenido de esta sección antes de proceder.

### Para usuarios de Apt (Ubuntu, Debian, etc.)
#### 2-Apt-1. Configuración del repositorio para la descarga de paquetes
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Actualización de la lista de paquetes
```bash
sudo apt update
```

#### 2-Apt-3. Instalación del paquete
```bash
sudo apt install nvidia-container-toolkit
```

### Para usuarios de Yum o Dnf (Fedora, RHEL, Centos, etc.)
> Al probar en Fedora 40, a diferencia de Ubuntu, el comando `nvidia-smi` y el paquete `nvidia-persistenced` no estaban incluidos por defecto en el controlador gráfico NVIDIA, por lo que fue necesario instalar adicionalmente el paquete `xorg-x11-drv-nvidia-cuda`. No he probado directamente en RHEL y Centos, pero como la configuración del sistema es muy similar a Fedora, si tienes problemas siguiendo la guía a continuación, intentar el mismo método podría ser útil.
{: .prompt-warning }

> Después de instalar `xorg-x11-drv-nvidia-cuda` como se describió anteriormente y ejecutar una carga de trabajo de muestra para probar en Fedora 40, funcionó normalmente en mi sistema. Si aún tienes problemas debido a SELinux u otras razones, el [paquete nvidia-container-toolkit específico para Fedora y la guía](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) proporcionados por el grupo AI-ML de Fedora podrían ser útiles.
{: .prompt-tip }

#### 2-Dnf-1. Configuración del repositorio para la descarga de paquetes
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Instalación del paquete
```bash
sudo dnf install nvidia-container-toolkit
```
o
```bash
sudo yum install nvidia-container-toolkit
```

### Para usuarios de Zypper (openSUSE, SLES)
#### 2-Zypper-1. Configuración del repositorio para la descarga de paquetes
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalación del paquete
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalación de Docker Engine
A continuación, instalamos Docker Engine. Sigue la instalación consultando la [documentación oficial de Docker](https://docs.docker.com/engine/install/).

### Para Ubuntu
#### 3-Ubuntu-1. Eliminación de versiones anteriores o paquetes no oficiales para evitar conflictos de paquetes
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

#### 3-Ubuntu-2. Configuración del repositorio
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

#### 3-Ubuntu-3. Instalación del paquete
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 3-Ubuntu-4. Creación del grupo `Docker` y registro de usuarios  
Para permitir que los usuarios no root gestionen Docker sin `sudo`, puedes crear un grupo `Docker` y registrar a los usuarios que deseen usar Docker. Ejecuta los siguientes comandos en la terminal:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Después de cerrar sesión y volver a iniciar sesión, se aplicará la configuración modificada. En el caso de Ubuntu o Debian, el servicio Docker se ejecutará automáticamente en cada arranque del sistema sin necesidad de trabajo adicional.

### Para Fedora
#### 3-Fedora-1. Eliminación de versiones anteriores o paquetes no oficiales para evitar conflictos de paquetes
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

#### 3-Fedora-2. Configuración del repositorio
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

#### 3-Fedora-3. Instalación del paquete  
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Durante el proceso de instalación del paquete, aparecerá una notificación preguntando si deseas aprobar la clave GPG. Si la clave GPG coincide con `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, ingresa y para aprobarla.  
> Si la clave GPG no coincide, podrías haber descargado un paquete falsificado debido a un ataque a la cadena de suministro, por lo que debes detener la instalación.
{: .prompt-danger }

#### 3-Fedora-4. Inicio del demonio Docker  
Ahora Docker está instalado pero no en ejecución, así que puedes iniciar Docker ingresando el siguiente comando:
```bash
sudo systemctl start docker
```
Para que el servicio Docker se ejecute automáticamente al arrancar el sistema, ejecuta los siguientes comandos:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

#### 3-Fedora-5. Registro de usuarios en el grupo `Docker`  
Para permitir que los usuarios no root gestionen Docker, registra a los usuarios que deseen usar Docker en el grupo `Docker`. En el caso de Fedora, el grupo `Docker` se crea automáticamente durante el proceso de instalación del paquete anterior, así que solo necesitas registrar al usuario.
```bash
sudo usermod -aG docker $USER
```
Después de cerrar sesión y volver a iniciar sesión, se aplicará la configuración modificada.

### Verificación de la configuración correcta  
Ejecuta el siguiente comando en la terminal:
```bash
docker run hello-world
```
Si se muestra un mensaje como el siguiente, has tenido éxito:

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

## Lectura adicional
Continúa en la [Parte 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
