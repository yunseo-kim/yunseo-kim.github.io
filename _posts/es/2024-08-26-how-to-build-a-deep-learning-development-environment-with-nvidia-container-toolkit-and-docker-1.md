---
title: Configuración de un entorno de desarrollo de aprendizaje profundo con NVIDIA Container Toolkit y Docker/Podman (1) - Instalación de NVIDIA Container Toolkit y motor de contenedores
description: Esta serie aborda cómo configurar un entorno de desarrollo de aprendizaje profundo basado en contenedores con NVIDIA Container Toolkit localmente, y cómo configurar SSH y Jupyter Lab para utilizarlo como servidor remoto. Esta publicación es la primera de la serie e introduce los métodos de instalación de NVIDIA Container Toolkit y el motor de contenedores.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---
## Descripción general
En esta serie, cubrimos el proceso de instalación de NVIDIA Container Toolkit y Docker o Podman, y la creación de un entorno de desarrollo de deep learning escribiendo un Dockerfile basado en imágenes CUDA y cuDNN proporcionadas por el [repositorio nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) en Docker Hub. Comparto el [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) y la [imagen](https://hub.docker.com/r/yunseokim/dl-env/tags) completados a través de GitHub y Docker Hub para que cualquiera pueda usarlos libremente, y además proporciono una guía para configurar SSH y Jupyter Lab para su uso como servidor remoto.  
La serie constará de 3 artículos, y este que estás leyendo es el primero de ellos.
- Parte 1: Instalación de NVIDIA Container Toolkit y motor de contenedores (este artículo)
- [Parte 2: Configuración del runtime de contenedores para utilizar GPU, escritura de Dockerfile y construcción de imagen de contenedor](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Parte 3 (próximamente)

Procederemos asumiendo un sistema Linux x86_64 con una tarjeta gráfica NVIDIA que soporte CUDA, y aunque no he probado personalmente distribuciones distintas a Ubuntu o Fedora, algunos detalles específicos pueden variar ligeramente.  
(Actualizado el 18.02.12025)

### Configuración del entorno de desarrollo
- Sistema operativo host y arquitectura: x86_64, entorno Linux (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Stack tecnológico a construir (lenguajes y bibliotecas)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE / Podman
  - CUDA 12.4
  - cuDNN
  - OpenSSH
  - tmux
  - JupyterLab
  - NumPy & SciPy
  - CuPy (opcional, biblioteca de arrays compatible con NumPy/SciPy para computación acelerada por GPU con Python)
  - pandas
  - cuDF (opcional, para acelerar pandas con cambios de código cero mediante el acelerador GPU)
  - Matplotlib & Seaborn
  - DALI (opcional, alternativa de alto rendimiento a los cargadores de datos e iteradores integrados utilizando GPU)
  - scikit-learn
  - cuML (opcional, para ejecutar algoritmos de aprendizaje automático en GPUs con una API que sigue de cerca la API de scikit-learn)
  - PyTorch
  - tqdm

  > Dependiendo de la situación y preferencias personales, se podría considerar usar la biblioteca DataFrame [Polars](https://pola.rs/) en lugar de pandas. Está escrita en Rust y [aunque su rendimiento es inferior a la combinación cuDF + pandas para procesamiento de grandes volúmenes de datos, supera significativamente al paquete pandas original](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), y proporciona una sintaxis más especializada para consultas. Según el [blog oficial de Polars](https://pola.rs/posts/polars-on-gpu/), están colaborando con el equipo NVIDIA RAPIDS para soportar la integración con cuDF en un futuro próximo.
  {: .prompt-tip }

  > Si estás indeciso entre Docker CE y Podman, la [tabla comparativa que se presenta más adelante](#3-instalación-del-motor-de-contenedores) puede ser útil.
  {: .prompt-tip }

### Tabla comparativa con la guía anterior de configuración de entorno de desarrollo para aprendizaje automático
Ya existe [una guía anterior de configuración de entorno de desarrollo para aprendizaje automático en este blog](/posts/Setting-up-a-Machine-Learning-Development-Environment) que sigue siendo mayormente válida, pero hay algunos cambios que motivaron la creación de esta nueva publicación. Las diferencias se resumen en la siguiente tabla:

| Diferencia | Artículo anterior (versión 12021) | Este artículo (versión 12024) |
| --- | --- | --- |
| Distribución Linux | Basado en Ubuntu | Aplicable a Ubuntu y también Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Método de configuración<br>del entorno de desarrollo | Entorno virtual Python usando venv | Entorno basado en contenedores Docker<br>usando [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Instalación del controlador<br>gráfico NVIDIA | Sí | Sí |
| Instalación directa de CUDA<br>y cuDNN en el sistema host | Sí (usando el gestor de paquetes Apt) | No (se usan [imágenes preinstaladas proporcionadas<br>por NVIDIA en Docker Hub](https://hub.docker.com/r/nvidia/cuda),<br>por lo que no es necesario instalarlos directamente) |
| Portabilidad | Necesidad de reconstruir el entorno<br>de desarrollo cada vez que se migra<br>a otro sistema | Al estar basado en Docker, se puede construir<br>fácilmente una nueva imagen con el Dockerfile<br>creado o migrar la imagen existente<br>(excluyendo volúmenes adicionales o<br>configuraciones de red) |
| Uso de bibliotecas adicionales<br>de aceleración GPU<br>además de cuDNN | No | Incorporación de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interfaz de Jupyter Notebook | Jupyter Notebook (clásico) | JupyterLab (nueva generación) |
| Configuración del servidor SSH | No se aborda | Incluye configuración básica del servidor SSH<br>en la parte 3 |

Si prefieres utilizar entornos virtuales de Python como venv en lugar de Docker, el [artículo anterior](/posts/Setting-up-a-Machine-Learning-Development-Environment) sigue siendo válido y se recomienda consultarlo.

## 0. Requisitos previos
- [NVIDIA Container Toolkit está disponible para distribuciones Linux que soporten los gestores de paquetes Apt, Yum o Dnf, y Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Puedes verificar la lista de distribuciones Linux soportadas en el enlace proporcionado. Aunque no aparece específicamente en la tabla de soporte oficial, Fedora también es compatible ya que está basado en Red Hat Linux como RHEL. Si no estás familiarizado con Linux y no sabes qué distribución usar, Ubuntu LTS es la opción más segura. Es relativamente conveniente para principiantes ya que los controladores propietarios se instalan automáticamente, y debido a su gran base de usuarios, la mayoría de la documentación técnica está escrita para Ubuntu.
  - Puedes verificar la arquitectura de tu sistema y la versión de la distribución Linux con el comando `uname -m && cat /etc/*release` en la terminal.
- Primero debes verificar si la tarjeta gráfica instalada en tu sistema es compatible con las versiones de CUDA y cuDNN que planeas usar.
  - Puedes verificar el modelo de GPU instalado en tu computadora con el comando `lspci | grep -i nvidia` en la terminal.
  - En la página <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> puedes verificar las **versiones de controladores NVIDIA compatibles**, los requisitos de **CUDA Compute Capability** y la lista de **hardware NVIDIA soportado** para cada versión de cuDNN.
  - Encuentra tu modelo de GPU en la lista de <https://developer.nvidia.com/cuda-gpus> y verifica su valor de **Compute Capability**. Este valor debe cumplir con los requisitos de **CUDA Compute Capability** verificados anteriormente para usar CUDA y cuDNN sin problemas.

> Si planeas comprar una nueva tarjeta gráfica para tareas de aprendizaje profundo, los criterios de selección de GPU están bien resumidos en el siguiente artículo, que el autor actualiza constantemente:  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> Otro artículo muy útil del mismo autor es [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/).
{: .prompt-tip }

Si cumples con todos los requisitos mencionados anteriormente, comencemos con la configuración del entorno de trabajo.

## 1. Instalación del controlador gráfico NVIDIA
Primero, debes instalar el controlador gráfico NVIDIA en tu sistema host. Puedes descargar e instalar el instalador .run desde la [página de descarga de controladores NVIDIA](https://www.nvidia.com/drivers/), pero es preferible utilizar el gestor de paquetes de tu sistema para facilitar la gestión de versiones y el mantenimiento. Consulta la documentación oficial <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> y sigue las instrucciones según tu entorno de sistema.

### Módulo propietario vs Módulo de código abierto
Los controladores Linux de NVIDIA consisten en varios módulos del kernel, y a partir de la versión 515 y posteriores, NVIDIA proporciona dos tipos de módulos de controladores para el kernel:

- Propietario: El controlador de software propietario que NVIDIA ha proporcionado tradicionalmente.
- Código abierto: Controlador de código abierto con licencia dual MIT/GPLv2. El código fuente está disponible en <https://github.com/NVIDIA/open-gpu-kernel-modules>.

El controlador propietario está disponible para GPUs basadas en arquitecturas desde Maxwell hasta antes de Blackwell, y se discontinuará para la arquitectura Blackwell en adelante.
Por otro lado, el controlador de código abierto es compatible con arquitecturas Turing y posteriores.

[NVIDIA recomienda usar el módulo de kernel de código abierto cuando sea posible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
Puedes verificar si tu GPU es compatible con el controlador de código abierto en [este enlace](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

En este artículo, explicaremos asumiendo que instalarás el controlador de código abierto.

### Debian y Ubuntu
Para Ubuntu o Debian, instala el controlador ingresando los siguientes comandos en la terminal:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Para Fedora 40, presentamos el método de instalación utilizando paquetes precompilados proporcionados por [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuración del repositorio RPM Fusion  
Siguiendo la [guía oficial de RPM Fusion](https://rpmfusion.org/Configuration), ejecuta el siguiente comando en la terminal:
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Instalación del paquete akmod-nvidia-open  
Siguiendo la [guía de instalación de controladores NVIDIA de RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), activa el repositorio rpmfusion-nonfree-tainted y luego instala el paquete akmod-nvidia-open:
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark user akmod-nvidia-open
```

> En las versiones antiguas de DNF (Fedora 40 y anteriores), la línea de comandos para evitar que se eliminaran los controladores NVIDIA al ejecutar autoremove en la última línea era la siguiente.
>
> ```bash
> sudo dnf mark install akmod-nvidia-open
> ```
>
> Sin embargo, a partir de DNF 5 (Fedora 41+) debes introducir
>
> ```bash
> sudo dnf mark user akmod-nvidia-open
> ```
>
> en lugar de la línea anterior, y he actualizado el contenido principal para reflejarlo.
{: .prompt-tip }

#### 1-Fedora-3. Registro de clave para cargar correctamente el controlador con Secure Boot activado  

> Con solo seguir el procedimiento adicional que se explica a continuación, podrás utilizar normalmente el controlador gráfico NVIDIA manteniendo la función de arranque seguro, y se recomienda encarecidamente no desactivarla ya que la seguridad del sistema se vuelve considerablemente vulnerable. Al menos desde la década de 12020 en adelante, rara vez hay razón para desactivar el arranque seguro.
{: .prompt-danger }

Primero, instala las siguientes herramientas:
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Luego, ejecuta el siguiente comando para generar una clave:
```bash
sudo kmodgenca -a
```
Ahora debes registrar la clave generada en el MOK del firmware UEFI:
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Al ejecutar este comando, se te pedirá que ingreses una contraseña para el registro de la clave. Esta será una contraseña de un solo uso que utilizarás cuando reinicies, así que ingresa algo que puedas recordar fácilmente.

Ahora reinicia el sistema con el siguiente comando:
```bash
systemctl reboot
```
Durante el arranque del sistema, aparecerá automáticamente la ventana de gestión MOK. Selecciona "Enroll MOK", luego "Continue" y "Yes" consecutivamente, y aparecerá una ventana solicitando la contraseña que configuraste anteriormente. Después de ingresar la contraseña, se completará el procedimiento de registro de la clave. Ahora ingresa reboot para reiniciar nuevamente y el controlador NVIDIA se cargará normalmente.

### Verificación de la instalación del controlador NVIDIA
Puedes verificar el módulo del kernel NVIDIA actualmente cargado ejecutando el siguiente comando en la terminal:
```bash
cat /proc/driver/nvidia/version
```
Si ves un mensaje similar al siguiente, la instalación se ha realizado correctamente:
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Instalación de NVIDIA Container Toolkit
Ahora debemos instalar [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Sigue la [guía oficial de instalación de NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), pero ten en cuenta que para Fedora hay consideraciones especiales, así que revisa completamente esta sección antes de proceder.

### Para sistemas que usan Apt (Ubuntu, Debian, etc.)
#### 2-Apt-1. Configuración del repositorio para descargar paquetes
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

### Para sistemas que usan Yum o Dnf (Fedora, RHEL, Centos, etc.)
> Al probar en Fedora 40, a diferencia de Ubuntu, el comando `nvidia-smi` y el paquete `nvidia-persistenced` no estaban incluidos por defecto en el controlador gráfico NVIDIA, por lo que fue necesario instalar adicionalmente el paquete `xorg-x11-drv-nvidia-cuda`. No he probado directamente en RHEL y Centos, pero como su configuración de sistema es muy similar a Fedora, si experimentas problemas siguiendo esta guía, intentar el mismo método podría ser útil.
{: .prompt-warning }

> Al instalar `xorg-x11-drv-nvidia-cuda` como se indica arriba y ejecutar cargas de trabajo de prueba en Fedora 40, funcionó correctamente en mi sistema. Si sigues experimentando problemas, posiblemente debido a SELinux u otras razones, el [paquete nvidia-container-toolkit específico para Fedora y la guía proporcionada por el grupo AI-ML de Fedora](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) podrían ser útiles.
{: .prompt-tip }

#### 2-Dnf-1. Configuración del repositorio para descargar paquetes
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

### Para sistemas que usan Zypper (openSUSE, SLES)
#### 2-Zypper-1. Configuración del repositorio para descargar paquetes
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalación del paquete
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalación del motor de contenedores
A continuación, instala Docker CE o Podman como motor de contenedores. Puedes elegir uno de los dos según tu entorno y preferencias, consultando la [documentación oficial de Docker](https://docs.docker.com/engine/install/) y la [documentación oficial de Podman](https://podman.io/docs/installation).

La siguiente tabla resume las principales diferencias y ventajas/desventajas entre Docker y Podman:

| Criterio | Docker | Podman |
| --- | --- | --- |
| Arquitectura | Modelo cliente-servidor, basado en daemon | Estructura sin daemon (daemonless) |
| Seguridad | Potencial riesgo de seguridad al depender de<br>un daemon que se ejecuta con privilegios root<br>(desde la versión 20.10 lanzada en 12020<br>soporta modo rootless, pero requiere<br>configuración adicional) | No depende de daemon y opera en modo<br>rootless por defecto a menos que se<br>especifique lo contrario, protegido por SELinux |
| Uso de recursos | Mayor consumo de recursos debido a procesos<br>en segundo plano que operan constantemente<br>por su estructura basada en daemon | Generalmente menor sobrecarga (overhead)<br>de recursos |
| Tiempo de inicio<br>de contenedores | Relativamente más lento | Hasta 50% más rápido gracias a su<br>arquitectura simplificada |
| Ecosistema y<br>documentación | Amplio ecosistema y soporte comunitario,<br>abundante documentación relacionada | Ecosistema y documentación relativamente<br>más reducidos |
| Redes | Usa Docker Bridge Network | Usa plugins CNI (Container Network Interface) |
| Soporte nativo para<br>YAML de Kubernetes | No (requiere conversión) | Sí |

Referencias:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

La mayor ventaja de Docker es su amplio ecosistema y abundante documentación, ya que tiene una historia más larga y ha disfrutado de un estatus de estándar de facto en la industria.  
Podman fue desarrollado más recientemente por Red Hat y, al estar diseñado desde su origen con un enfoque daemonless y rootless, ofrece ventajas en términos de seguridad, uso de recursos del sistema y tiempo de inicio de contenedores. Otra fortaleza de Podman es que cada contenedor es completamente independiente, por lo que si un contenedor falla, no afecta a los demás, a diferencia de Docker donde si el daemon tiene problemas, todos los contenedores se caen.

Es importante elegir la herramienta que mejor se adapte a tus circunstancias, y para usuarios individuales que están comenzando, Podman podría ser una buena elección. Aunque su ecosistema es relativamente más pequeño que el de Docker, está creciendo rápidamente gracias a sus múltiples ventajas, y es compatible con la sintaxis de Dockerfile, imágenes Docker y CLI (interfaz de línea de comandos), lo que no debería ser un problema para individuos o pequeños grupos.

### Podman
Se puede instalar fácilmente ya que está disponible en los repositorios base de la mayoría de las principales distribuciones Linux.

#### Para Ubuntu
```bash
sudo apt install podman
```

#### Para Fedora
```bash
sudo dnf install podman
```

#### Para openSUSE
```bash
sudo zypper install podman
```

### Docker CE
#### Para Ubuntu
##### 3-Ubuntu-1. Eliminación de versiones anteriores o paquetes no oficiales para evitar conflictos
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configuración del repositorio
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

##### 3-Ubuntu-3. Instalación de paquetes
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Creación del grupo `Docker` y registro de usuario
Para permitir que usuarios sin privilegios root gestionen Docker sin usar `sudo`, crea un grupo `Docker` y registra a los usuarios que deseen utilizar Docker. Ejecuta los siguientes comandos en la terminal:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Después de cerrar sesión y volver a iniciarla, la configuración modificada se aplicará. En Ubuntu o Debian, el servicio Docker se ejecutará automáticamente cada vez que se inicie el sistema sin necesidad de configuración adicional.

#### Para Fedora
##### 3-Fedora-1. Eliminación de versiones anteriores o paquetes no oficiales para evitar conflictos
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

##### 3-Fedora-2. Configuración del repositorio
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Instalación de paquetes
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Durante la instalación del paquete, aparecerá una notificación preguntando si deseas aprobar la clave GPG. Si la clave GPG coincide con `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, ingresa y para aprobarla.  
> Si la clave GPG no coincide, podrías estar descargando un paquete falsificado debido a un ataque a la cadena de suministro, y deberías detener la instalación.
{: .prompt-danger }

##### 3-Fedora-4. Inicio del daemon Docker
Ahora Docker está instalado pero no en ejecución, así que puedes iniciarlo con el siguiente comando:
```bash
sudo systemctl start docker
```
Para que el servicio Docker se ejecute automáticamente al iniciar el sistema, ejecuta los siguientes comandos:
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Registro de usuario en el grupo `Docker`
Para permitir que usuarios sin privilegios root gestionen Docker, registra a los usuarios que deseen utilizar Docker en el grupo `Docker`. En Fedora, el grupo `Docker` se crea automáticamente durante la instalación del paquete, así que solo necesitas registrar al usuario:
```bash
sudo usermod -aG docker $USER
```
Después de cerrar sesión y volver a iniciarla, la configuración modificada se aplicará.

#### Verificación de la configuración correcta
Ejecuta el siguiente comando en la terminal:
```bash
docker run hello-world
```
Si ves un mensaje como el siguiente, la instalación ha sido exitosa:

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

## Lecturas adicionales
Continúa en la [Parte 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
