---
title: "Cómo construir un entorno de desarrollo de deep learning con NVIDIA Container Toolkit y Docker/Podman (1) - Instalación de NVIDIA Container Toolkit y del motor de contenedores"
description: "Esta serie explica cómo montar localmente un entorno de deep learning basado en contenedores con NVIDIA Container Toolkit y cómo configurarlo para uso remoto con SSH y JupyterLab. En esta primera entrega se cubre la instalación de NVIDIA Container Toolkit y del motor de contenedores."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Descripción general

En esta serie cubrimos el proceso de instalar NVIDIA Container Toolkit y Docker o Podman, y construir un entorno de desarrollo de deep learning escribiendo un Dockerfile basado en imágenes CUDA y cuDNN proporcionadas por el repositorio [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) en Docker Hub. Para que cualquiera pueda reutilizarlo libremente, comparto el [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) y la [imagen](https://hub.docker.com/r/yunseokim/dl-env/tags) finalizados tras este proceso a través de GitHub y Docker Hub, y adicionalmente proporciono una guía de configuración de SSH y JupyterLab para usarlo como servidor remoto.  
La serie constará de 3 artículos, y este que estás leyendo es el primero.
- Parte 1: Instalación de NVIDIA Container Toolkit y del motor de contenedores (este artículo)
- [Parte 2: Configuración del runtime de contenedor para usar la GPU, escritura de Dockerfile y construcción de la imagen de contenedor](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Parte 3 (próximamente)

Procederemos asumiendo un sistema Linux x86_64 con una tarjeta gráfica NVIDIA que soporte CUDA, y como no he probado personalmente distribuciones distintas de Ubuntu o Fedora, algunos detalles específicos pueden variar ligeramente.  
(Revisado el 12026.1.6.)

### Configuración del entorno de desarrollo

- Sistema operativo host y arquitectura: x86_64, entorno Linux (Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Stack tecnológico a construir (lenguajes y librerías)
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/) (opcional, librería de arrays compatible con NumPy/SciPy para cómputo acelerado por GPU con Python)
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/) (opcional, para acelerar pandas con cambios de código cero mediante el acelerador GPU)
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/) (opcional, para visualizar y filtrar rápidamente datasets grandes con unas pocas líneas de código, usando librerías de gráficos de primer nivel)
  - [DALI](https://developer.nvidia.com/DALI) (opcional, alternativa de alto rendimiento a los data loaders e iteradores integrados usando GPU)
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/) (opcional, alternativa acelerada para procesamiento de imágenes n-dimensional e I/O de imágenes frente a scikit-image)
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/) (opcional, para ejecutar algoritmos de ML en GPUs con una API muy cercana a la de scikit-learn)
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/) (opcional, algoritmos optimizados para vecinos más cercanos aproximados y clustering, junto con muchas otras herramientas esenciales para búsqueda vectorial acelerada)
  - [RAFT](https://docs.rapids.ai/api/raft/stable/) (opcional, primitivas aceleradas por CUDA usadas por otras librerías RAPIDS)
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/) (opcional, librería de analítica de grafos acelerada por GPU que incluye un acelerador de cambios de código cero para NetworkX)
  - [tqdm](https://tqdm.github.io/)

  > Dependiendo de la situación y de tus preferencias, también puedes considerar usar la librería DataFrame [Polars](https://pola.rs/) en lugar de pandas. Está escrita en Rust y, aunque en el procesamiento de grandes volúmenes de datos queda por detrás de la combinación cuDF + pandas, [en comparación con el paquete pandas “puro” muestra un rendimiento bastante superior](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), y ofrece una sintaxis más orientada a consultas. Según el [blog oficial de Polars](https://pola.rs/posts/polars-on-gpu/) y la [documentación de cuDF](https://docs.rapids.ai/api/cudf/stable/cudf_polars/), Polars y el equipo de NVIDIA RAPIDS colaboran para ofrecer en beta abierta un motor de aceleración por GPU basado en cuDF, y el desarrollo avanza rápidamente.
  {: .prompt-tip }

  > Si estás dudando entre usar Docker CE o Podman, la [tabla comparativa mencionada más adelante](#3-instalación-del-motor-de-contenedores) puede serte útil.
  {: .prompt-tip }

### Tabla comparativa con una guía anterior de configuración de entorno de ML que escribí

Ya existe una [guía de configuración de entorno de desarrollo de machine learning que publiqué anteriormente en este blog](/posts/Setting-up-a-Machine-Learning-Development-Environment), pero como ha habido varios cambios, he escrito este nuevo post. Las diferencias se resumen en la tabla siguiente.

| Diferencia | Artículo anterior (versión 12021) | Este artículo (escrito en 12024, versión revisada 12026) |
| --- | --- | --- |
| Distribución Linux | Basado en Ubuntu | Además de Ubuntu, aplicable a Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Método de construcción del entorno | Instalación directa en el sistema host<br>Entorno virtual de Python con venv | Entorno basado en contenedores Docker<br> mediante [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br> Entorno virtual y gestión de paquetes de Python con uv |
| Instalación del driver gráfico NVIDIA | O | O |
| Instalación directa de <br>CUDA y cuDNN en el host | O (usando el gestor de paquetes Apt) | X (como se usan [imágenes preinstaladas<br> proporcionadas por NVIDIA en Docker Hub](https://hub.docker.com/r/nvidia/cuda), no hace falta hacerlo manualmente) |
| Portabilidad | Cada vez que se migra a otro sistema<br> hay que reconstruir el entorno | Al estar basado en Docker, con el Dockerfile <br>preparado puedes construir nuevas imágenes cuando <br>lo necesites, o migrar fácilmente la imagen que <br>ya usabas (excluyendo volúmenes adicionales o<br> configuración de red) |
| Uso de librerías adicionales <br>de aceleración GPU además de cuDNN | X | Se incorporan [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), [DALI](https://developer.nvidia.com/DALI) |
| Interfaz de Jupyter Notebook | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| Configuración del servidor SSH | No se trata | Incluye configuración básica del servidor SSH |

## 0. Verificaciones previas

- [NVIDIA Container Toolkit puede usarse en distribuciones Linux que soporten los gestores de paquetes Apt, Yum o Dnf, y Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) En la página enlazada puedes consultar la lista de distribuciones soportadas; aunque Fedora no aparece explícitamente en la tabla de soporte oficial, al ser una distro basada en Red Hat Linux como RHEL, se puede utilizar sin problemas. Si no estás familiarizado con Linux y no sabes qué distribución usar, la opción más segura suele ser Ubuntu LTS. También instala automáticamente drivers propietarios (no open source), lo que suele ser más cómodo para principiantes, y como hay muchos usuarios, la mayoría de documentación técnica está escrita tomando Ubuntu como referencia.
  - Puedes comprobar la arquitectura del sistema y la versión de la distribución Linux en la terminal con `uname -m && cat /etc/*release`.
- Primero debes comprobar si la GPU instalada en el sistema es un modelo que soporte las versiones de CUDA y cuDNN que quieres usar.
  - Puedes ver el modelo de la GPU instalada en tu equipo con `lspci | grep -i nvidia` en la terminal.
  - En <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> revisa por versión de cuDNN: la **versión del driver NVIDIA soportada**, los requisitos de **CUDA Compute Capability**, y la lista de **hardware NVIDIA soportado**.
  - En <https://developer.nvidia.com/cuda-gpus> busca tu modelo de GPU y comprueba el valor de **Compute Capability**. Ese valor debe cumplir el requisito de **CUDA Compute Capability** que verificaste antes para poder usar CUDA y cuDNN sin problemas.

> Si planeas comprar una GPU nueva para deep learning, los criterios de selección están bien resumidos en el siguiente artículo, que el autor actualiza de forma irregular.  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> Si además necesitas una guía de configuración de hardware más general, también es muy útil el artículo del mismo autor: [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/).
{: .prompt-tip }

Si cumples todos los puntos anteriores, empecemos con la configuración del entorno de trabajo.

## 1. Instalación del driver gráfico NVIDIA

Primero debes instalar el driver gráfico NVIDIA en el sistema host. Puedes descargar y usar el instalador `.run` desde la [página de descarga de drivers de NVIDIA](https://www.nvidia.com/drivers/), pero siempre que sea posible es mejor instalarlo usando el gestor de paquetes del sistema por motivos de control de versiones y mantenimiento. Consulta la documentación oficial <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> e instala el driver que corresponda a tu entorno.

### Módulo propietario vs módulo de código abierto

El driver de NVIDIA para Linux se compone de varios módulos del kernel, y desde el driver versión 515 y lanzamientos posteriores, NVIDIA ofrece dos tipos de módulos de kernel para el driver.

- Propietario: el driver de software propietario que NVIDIA ha proporcionado tradicionalmente.
- Código abierto: driver open source bajo doble licencia MIT/GPLv2. El código fuente se publica en <https://github.com/NVIDIA/open-gpu-kernel-modules>.

El driver propietario se ofrece para GPUs diseñadas con arquitecturas desde Maxwell hasta antes de Blackwell, y a partir de la arquitectura Blackwell se prevé que se descontinúe.  
En cambio, el driver de código abierto se soporta para Turing y arquitecturas posteriores.

[NVIDIA recomienda usar los módulos de kernel open source si es posible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
Puedes comprobar si tu GPU es compatible con el driver open source en [este enlace](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

En este artículo se asume que instalaremos el driver de código abierto.

### Debian & Ubuntu

En el caso de Ubuntu o Debian, instala ejecutando los siguientes comandos en la terminal:
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Tomando Fedora 40 como referencia, presento un método para descargar e instalar paquetes precompilados proporcionados por [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuración del repositorio RPM Fusion

Sigue la [guía oficial de RPM Fusion](https://rpmfusion.org/Configuration).  
Ejecuta lo siguiente en la terminal.

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> En versiones antiguas de DNF (Fedora 40 y anteriores), la línea de comandos de la segunda línea para habilitar el repositorio de la librería openh264 era la siguiente:
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> Sin embargo, desde DNF 5 (Fedora 41+), en lugar de ese comando hay que introducir:
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> y he actualizado el contenido del artículo para reflejarlo.
{: .prompt-info }

#### 1-Fedora-2. Instalar el paquete akmod-nvidia

Siguiendo la [guía de instalación del driver NVIDIA proporcionada por RPM Fusion](https://rpmfusion.org/Howto/NVIDIA), instala el paquete akmod-nvidia.

```bash
sudo dnf update  # si en este paso hubo una actualización del kernel, reinicia con el kernel más reciente y luego continúa
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> De igual modo, en versiones antiguas de DNF (Fedora 40 y anteriores), la línea de comandos de la tercera línea para evitar que el driver NVIDIA se eliminase en un autoremove era:
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> Sin embargo, desde DNF 5 (Fedora 41+), en lugar de ese comando hay que introducir:
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> y he actualizado el contenido del artículo para reflejarlo.
{: .prompt-info }

> Por otro lado, en el pasado RPM Fusion había mostrado una postura negativa respecto a los [módulos de kernel NVIDIA open source](#módulo-propietario-vs-módulo-de-código-abierto), y salvo que se indicara lo contrario, proporcionaba por defecto el driver propietario. Sin embargo, según las [directrices de RPM Fusion modificadas recientemente (diciembre de 12025)](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), ahora para hardware con soporte duplicado (arquitecturas desde Turing hasta antes de Blackwell) seleccionará automáticamente la mejor opción entre ambas, por lo que no es necesario elegir manualmente. Para arquitecturas antiguas anteriores a Turing, o para arquitecturas más recientes Blackwell y posteriores, desde el principio solo existía una opción, por lo que no hay cambios.
> En consecuencia, se ha eliminado el contenido relativo a especificar la opción de usar el módulo de kernel open source mediante `/etc/rpm/macros.nvidia-kmod`.
>
> Además, en el caso del paquete `akmod-nvidia-open`, indican que no debe usarse salvo que necesites aplicar tú mismo cambios downstream al driver en espacio de kernel.
>
> Estos puntos también se han reflejado recientemente en el contenido del artículo.
{: .prompt-info }

#### 1-Fedora-3. Registro de clave para que el driver se cargue correctamente con Secure Boot habilitado  

> Si sigues el procedimiento adicional (ligero) que se describe a continuación, podrás usar el driver gráfico NVIDIA manteniendo Secure Boot habilitado. Desactivar Secure Boot debilita considerablemente la seguridad del sistema, por lo que recomiendo no hacerlo. Al menos desde que entramos en la década de 12020, rara vez hay un motivo para desactivar Secure Boot.
{: .prompt-danger }

Primero instala las siguientes herramientas.

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

A continuación, ejecuta el siguiente comando para generar una clave.

```bash
sudo kmodgenca -a
```

Ahora debes registrar en el MOK del firmware UEFI la clave generada.

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

Al ejecutar el comando, te pedirá que introduzcas una contraseña para registrar la clave. En breve reiniciaremos para completar el procedimiento; es una contraseña de un solo uso para ese reinicio, así que introduce algo que puedas recordar razonablemente.

Ahora ejecuta el siguiente comando para reiniciar el sistema.

```bash
systemctl reboot
```

Durante el arranque aparecerá automáticamente la pantalla de gestión de MOK. Selecciona “Enroll MOK” y luego “Continue” y “Yes”; a continuación aparecerá una pantalla solicitando la contraseña que configuraste antes. Al introducirla, se completa el registro de la clave. Después, introduce “reboot” para reiniciar de nuevo y el driver NVIDIA debería cargarse correctamente.

### Verificar la instalación del driver NVIDIA

En la terminal puedes ejecutar el siguiente comando para comprobar el módulo del kernel NVIDIA cargado actualmente.

```bash
cat /proc/driver/nvidia/version
```

Si aparece un mensaje similar al siguiente, la instalación fue correcta.

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

Además, en Linux a menudo se usa por defecto el driver gráfico open source *nouveau* como módulo del kernel; después de instalar el driver NVIDIA debe quedar deshabilitado, y si no lo está puede causar problemas. Tras instalar el driver NVIDIA y reiniciar, el siguiente comando no debería mostrar ninguna salida.

```bash
lsmod |grep nouveau
```

## 2. Instalación de NVIDIA Container Toolkit

Ahora debes instalar [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Sigue la [guía oficial de instalación de NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), pero en el caso de Fedora hay consideraciones a tener en cuenta durante la instalación, así que revisa el contenido de esta sección hasta el final antes de continuar.

### Si usas Apt (Ubuntu, Debian, etc.)

#### 2-Apt-1. Configurar el repositorio para descargar paquetes

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Actualizar la lista de paquetes

```bash
sudo apt update
```

#### 2-Apt-3. Instalar el paquete

```bash
sudo apt install nvidia-container-toolkit
```

### Si usas Yum o Dnf (Fedora, RHEL, Centos, etc.)

> Al probar en Fedora 40, a diferencia de Ubuntu, los comandos `nvidia-smi` y el paquete `nvidia-persistenced` no venían incluidos por defecto con el driver gráfico NVIDIA, por lo que fue necesario instalar adicionalmente el paquete `xorg-x11-drv-nvidia-cuda`. No lo he probado directamente en RHEL ni Centos, pero como la configuración del sistema es muy similar a Fedora, si al seguir la guía de abajo aparece algún problema, probar el mismo método podría ayudar.
{: .prompt-warning }

> En Fedora 40, tras instalar `xorg-x11-drv-nvidia-cuda` como se indicó arriba y probar ejecutando un workload de ejemplo, en mi sistema funcionó correctamente. Si aun así se producen problemas por motivos como SELinux, el paquete y guía específicos para Fedora proporcionados por el grupo AI-ML de Fedora —[nvidia-container-toolkit para Fedora](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/)— podrían ser de ayuda.
{: .prompt-tip }

#### 2-Dnf-1. Configurar el repositorio para descargar paquetes

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Instalar el paquete

```bash
sudo dnf install nvidia-container-toolkit
```

o bien

```bash
sudo yum install nvidia-container-toolkit
```

### Si usas Zypper (openSUSE, SLES)

#### 2-Zypper-1. Configurar el repositorio para descargar paquetes

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Instalar el paquete

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Instalación del motor de contenedores

A continuación, instala Docker CE o Podman como motor de contenedores. Puedes elegir uno u otro según tu entorno y preferencias; consulta la [documentación oficial de Docker](https://docs.docker.com/engine/install/) y la [documentación oficial de Podman](https://podman.io/docs/installation).

La siguiente tabla resume las principales diferencias, ventajas y desventajas de Docker y Podman.

| Elemento de comparación | Docker | Podman |
| --- | --- | --- |
| Arquitectura | Modelo cliente-servidor, basado en demonio (daemon) | Estructura sin demonio (daemonless) |
| Seguridad | Depende de un demonio que por defecto se ejecuta <br>con permisos root, por lo que existe un riesgo potencial<br>de seguridad<br>(desde la versión 20.10 publicada en 12020 soporta modo <br>rootless, pero requiere configuración adicional) | Al no depender de un demonio, salvo que se indique lo <br>contrario, funciona por defecto en modo rootless y<br> está protegido por SELinux |
| Uso de recursos | Por la naturaleza de la arquitectura basada en demonio,<br> un proceso en segundo plano se mantiene siempre activo,<br> por lo que normalmente consume más recursos | En general, menor overhead de recursos |
| Tiempo de arranque del contenedor | Relativamente más lento | Gracias a una arquitectura más simple, puede ejecutarse<br> hasta ~50% más rápido |
| Ecosistema y documentación | Ecosistema y soporte comunitario amplios,<br> abundante documentación relacionada | Ecosistema y documentación relativamente más reducidos |
| Networking | Usa Docker Bridge Network | Usa plugins CNI (Container Network Interface) |
| Soporte nativo de YAML<br> de Kubernetes | X (requiere conversión) | O |

Referencias:
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker tiene más historia y durante mucho tiempo ha disfrutado de un estatus de estándar de facto en la industria, por lo que su mayor ventaja es contar con un ecosistema amplio y mucha documentación relacionada.  
Podman fue desarrollado por Red Hat relativamente más recientemente; por su diseño, apuesta desde el origen por ser daemonless y rootless, y por ello ofrece ventajas en múltiples aspectos como seguridad, consumo de recursos del sistema y tiempo de arranque de contenedores. A diferencia de Docker —donde si el demonio falla y cae, caen todos los contenedores—, en Podman cada contenedor es completamente independiente, así que la caída de un contenedor no afecta a los demás; este también es un punto fuerte de Podman.

Lo más importante es elegir la herramienta que mejor se ajuste a tus condiciones, pero si estás empezando, parece una buena opción comenzar con Podman. Aunque su ecosistema es más pequeño que el de Docker, está creciendo rápido gracias a las ventajas descritas, y reduce la brecha; además, es compatible en muchos aspectos con Docker existente (sintaxis de Dockerfile, imágenes Docker, CLI, etc.). Salvo que ya tengas un sistema grande construido sobre Docker y adoptar Podman implique un coste de migración alto, es razonable optar por Podman desde el inicio.

### Podman

Como la mayoría de distribuciones Linux principales lo incluyen en sus repositorios por defecto, se puede instalar de forma sencilla.

#### En Ubuntu

```bash
sudo apt install podman
```

#### En Fedora

```bash
sudo dnf install podman
```

#### En openSUSE

```bash
sudo zypper install podman
```

#### Verificar que está configurado correctamente

Ejecuta el siguiente comando en la terminal.

```bash
podman run --rm hello-world
```

Si aparece un mensaje como el siguiente, es un éxito.

```bash
!... Hello Podman World ...!

         .--"--.           
       / -     - \         
      / (O)   (O) \        
   ~~~| -=(,Y,)=- |         
    .---. /`  \   |~~      
 ~/  o  o \~~~~.----. ~~   
  | =(X)= |~  / (O (O) \   
   ~~~~~~~  ~| =(Y_)=-  |   
  ~~~~    ~~~|   U      |~~ 

Project:   https://github.com/containers/podman
Website:   https://podman.io
Desktop:   https://podman-desktop.io
Documents: https://docs.podman.io
YouTube:   https://youtube.com/@Podman
X/Twitter: @Podman_io
Mastodon:  @Podman_io@fosstodon.org
```

> En el momento 12025-12-18T00:43:00+09:00, al probar con podman 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64`, en un entorno Fedora 43, al ejecutar hello-world o al ejecutar contenedores / construir imágenes apareció el siguiente error:
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> Aunque actualmente no uso IPv6 y estoy en una red IPv4, parece que durante la fase de configuración de red del contenedor, pasta (incluido en la librería passt) intenta establecer routing IPv6 y eso causa el problema. Verifiqué que si se especifica explícitamente `--net=pasta:-4` para forzar IPv4 como se muestra abajo, el problema no ocurre al ejecutar contenedores o en la [fase de construcción de imagen que se tratará más adelante](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-construir-la-imagen-docker-y-ejecutar-el-contenedor).
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> Buscando, encontré que existía [un issue registrado anteriormente con el mismo síntoma](https://github.com/containers/podman/issues/22824). En ese issue se menciona que se corrigió en [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/), pero dado que el síntoma observado es idéntico y que ocurrió al usar Proton VPN, entre otras similitudes, sospecho que quizá un problema parecido haya reaparecido.
{: .prompt-warning }

### Docker CE

#### En Ubuntu

##### 3-Ubuntu-1. Eliminar versiones anteriores o paquetes no oficiales para evitar conflictos

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configurar el repositorio

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

##### 3-Ubuntu-3. Instalar los paquetes

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Crear el grupo `Docker` y registrar al usuario

Si quieres que los usuarios non-root puedan gestionar Docker sin `sudo`, crea el grupo `Docker` y registra en él al usuario que vaya a usar Docker. Ejecuta lo siguiente en la terminal.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Después, cierra sesión y vuelve a iniciarla para que se apliquen los cambios. En Ubuntu o Debian, el servicio Docker se ejecuta automáticamente en cada arranque del sistema sin necesidad de acciones adicionales.

#### En Fedora

##### 3-Fedora-1. Eliminar versiones anteriores o paquetes no oficiales para evitar conflictos

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

##### 3-Fedora-2. Configurar el repositorio

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Instalar los paquetes

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Durante la instalación se te pedirá que apruebes la clave GPG. Si coincide con `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, introduce `y` para aprobarla.  
> Si la clave GPG no coincide, es posible que se haya descargado un paquete falsificado debido a un ataque a la cadena de suministro, por lo que debes detener la instalación.
{: .prompt-danger }

##### 3-Fedora-4. Iniciar el demonio de Docker

Ahora Docker está instalado pero no se está ejecutando, así que puedes iniciarlo con el siguiente comando.

```bash
sudo systemctl start docker
```

Si quieres que el servicio Docker se ejecute automáticamente al arrancar el sistema, ejecuta lo siguiente.

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Registrar al usuario en el grupo `Docker`

Para que un usuario non-root pueda gestionar Docker, registra al usuario en el grupo `Docker`. En Fedora, el grupo `Docker` se crea automáticamente durante el proceso de instalación anterior, así que solo necesitas registrar al usuario.

```bash
sudo usermod -aG docker $USER
```

Después, cierra sesión y vuelve a iniciarla para que se apliquen los cambios.

#### Verificar que está configurado correctamente

Ejecuta el siguiente comando en la terminal.

```bash
docker run hello-world
```

Si aparece un mensaje como el siguiente, es un éxito.

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
Continuación en la [Parte 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
