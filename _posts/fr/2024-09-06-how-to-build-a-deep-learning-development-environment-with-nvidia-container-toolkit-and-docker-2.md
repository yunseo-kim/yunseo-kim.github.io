---
title: "Mettre en place un environnement de développement deep learning avec NVIDIA Container Toolkit et Docker/Podman (2) — Configuration du runtime pour exploiter le GPU, rédaction du Dockerfile et build de l’image"
description: "Série : créer un environnement deep learning en conteneur avec NVIDIA Container Toolkit, puis activer un usage distant via SSH et JupyterLab. Partie 2 : écrire le Dockerfile et construire l’image."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Vue d’ensemble

Cette série explique comment installer NVIDIA Container Toolkit et Docker ou Podman, puis construire un environnement de développement deep learning en rédigeant un Dockerfile à partir des images CUDA et cuDNN fournies par le dépôt [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub. Pour que chacun puisse réutiliser facilement le résultat, je partage via GitHub et Docker Hub le [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) et l’[image](https://hub.docker.com/r/yunseokim/dl-env/tags) finalisés en suivant ce processus, et je fournis en plus un guide de configuration SSH et JupyterLab pour une utilisation comme serveur distant.  
La série comportera 3 articles, et celui que vous lisez est le deuxième.
- [Partie 1 : Installation de NVIDIA Container Toolkit & du moteur de conteneurs](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Partie 2 : Configuration du runtime pour exploiter le GPU, rédaction du Dockerfile et build de l’image (cet article)
- Partie 3 (à venir)

On part du principe qu’il s’agit d’un système x86_64 sous Linux équipé d’une carte graphique NVIDIA compatible CUDA. Je n’ai pas testé directement sur des distributions autres qu’Ubuntu ou Fedora ; certains détails peuvent donc légèrement différer.  
(12026.1.6. révision)

> **Avis de correction d’erreurs**
>
> Dans le brouillon initial de cet article, publié en août 12024, il y avait des erreurs dans la section [Rédaction du Dockerfile](#5-rédaction-du-dockerfile) ainsi que dans certaines parties de l’image construite à partir de ce Dockerfile. Les problèmes étaient les suivants :
> - Dans la partie création du compte `remote`, l’étape de définition du mot de passe était incorrecte : j’indiquais qu’on pouvait se connecter en saisissant `"000000"` comme mot de passe initial, mais ce n’était pas le cas (ajout 12025.12.19 : désormais, le mot de passe initial n’est plus `"000000"` ; veuillez impérativement vérifier le [contenu ci-dessous](#5-4-configuration-du-serveur-ssh-pour-laccès-à-distance))
> - Au démarrage du conteneur, le démon SSH ne se lançait pas automatiquement
>
> J’ai pris connaissance de ces problèmes en février 12025 et, vers 2 h du matin le 16 février 12025 (heure de Corée, UTC+9), j’ai remplacé sur le [dépôt GitHub](https://github.com/yunseo-kim/dl-env-docker) et sur [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags) le Dockerfile et les images Docker concernés par des versions corrigées.  
> Si vous avez *pull* le Dockerfile ou une image Docker avant cette date, veuillez les remplacer par la version corrigée.  
> Si certains lecteurs ont été perturbés par ces informations erronées, je vous présente mes excuses.
{: .prompt-info }

## Avant de commencer

Cet article fait suite à la [partie 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1). Si vous ne l’avez pas encore lue, il est recommandé de commencer par l’article précédent.

## 4. Configuration du runtime de conteneur

### Si vous utilisez Podman

[Configurer via CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

> Avec les anciennes versions, lors de la première installation de NVIDIA Container Toolkit, puis à chaque modification de la carte GPU ou de la configuration du pilote (y compris une mise à niveau de version), il fallait régénérer manuellement à chaque fois le fichier de spécification CDI.
>
> Toutefois, à partir de NVIDIA Container Toolkit `v1.18.0`, le service systemd `nvidia-cdi-refresh` génère et met à jour automatiquement le fichier de spécification CDI `/var/run/cdi/nvidia.yaml` dans les cas suivants :
> - Installation ou mise à niveau de NVIDIA Container Toolkit
> - Installation ou mise à niveau du pilote NVIDIA GPU
> - Redémarrage du système
>
> Par conséquent, contrairement à avant, il n’y a plus rien à faire manuellement. J’ai modifié le corps de l’article pour refléter cela.
>
> En revanche, lors de la suppression du pilote GPU ou de la reconfiguration d’un périphérique MIG, `nvidia-cdi-refresh` ne sait pas réagir : il faut alors redémarrer manuellement `nvidia-cdi-refresh.service` afin de forcer la régénération de la spécification CDI.
> 
> ```bash
> sudo systemctl restart nvidia-cdi-refresh.service
> ```
{: .prompt-info }

> L’utilisation conjointe du hook NVIDIA Container Runtime avec CDI peut provoquer des conflits. Ainsi, si `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existe, supprimez ce fichier ou veillez à ne pas exécuter de conteneur avec la variable d’environnement `NVIDIA_VISIBLE_DEVICES` définie.
{: .prompt-warning }

### Si vous utilisez Docker

Explications basées sur le mode [rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configurer le runtime via la commande `nvidia-ctk`

```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```

La commande ci-dessus modifie le fichier `/etc/docker/daemon.json`{: .filepath} afin que Docker puisse utiliser NVIDIA Container Runtime.

#### 4-Docker-2. Redémarrer le démon Docker

Redémarrez le démon Docker pour appliquer la configuration modifiée.

```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configurer le fichier `/etc/nvidia-container-runtime/config.toml`{: .filepath} via `sudo nvidia-ctk`

```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Vérifier que la configuration fonctionne

Essayez d’exécuter un conteneur CUDA d’exemple.

Avec Podman, exécutez :

```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Avec Docker, exécutez :

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

Si un écran similaire à celui ci-dessous s’affiche, c’est réussi.

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

## 5. Rédaction du Dockerfile

Rédigez un Dockerfile destiné à servir d’environnement de développement, en vous basant sur les images CUDA et cuDNN fournies par le dépôt [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub.

- Il faut choisir l’image à utiliser en tenant compte de la version CUDA/cuDNN nécessaire, de la distribution Linux et de sa version, etc. 
- ![CUDA version supported by PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)  
  À la date de rédaction (fin août 12024), la dernière version de PyTorch (2.4.0) prend en charge CUDA 12.4. Ici, on utilise donc l’image [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Vous pouvez vérifier la version la plus récente de PyTorch et les versions CUDA supportées sur le [site officiel PyTorch](https://pytorch.org/get-started/locally/).

Le code source du Dockerfile final est publié dans le dépôt GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Ci-dessous, j’explique étape par étape le processus de rédaction de ce Dockerfile.

> (+ 12026.1.6. révision)  
> J’ai ajouté, dans le même dépôt GitHub ainsi que dans le dépôt public Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags), des Dockerfiles et des images prenant en charge PyTorch 2.9.1 et CUDA 12.8 / 13.0. Le contenu de l’article a également été mis à jour pour correspondre à PyTorch 2.9.1 et CUDA 13.0.
>
> J’ai aussi inclus scikit-image, XGBoost, ainsi que des bibliothèques de l’écosystème RAPIDS (cuGraph, cuxfilter, cuCIM, RAFT, cuVS) dans l’image, et ajouté le support `arm64` en plus de l’architecture `amd64`.
{: .prompt-info }

### 5-1. Définir l’image de base

```Dockerfile
FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04
```

### 5-2. Configurer le fuseau horaire système (ici : « Asia/Seoul »)

```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
ENV TZ="$TZ"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone
```

> Je me suis principalement appuyé sur le contenu de [cet article](https://dev.to/bitecode/set-timezone-in-your-docker-image-d22).
{: .prompt-tip }

### 5-3. Installer les utilitaires système de base

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

### 5-4. Configuration du serveur SSH pour l’accès à distance

Pour des raisons de sécurité, configurez SSH de sorte qu’il soit impossible de se connecter à distance avec le compte root.

```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Créez un utilisateur non-root nommé `remote` qui servira pour les connexions SSH.

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

> Le contenu des arguments de build (`ARG`) ou des variables d’environnement (`ENV`) est exposé tel quel dans l’image construite ; il faut donc [utiliser une autre méthode pour fournir des informations sensibles comme un mot de passe ou une clé API](https://docs.docker.com/build/building/secrets/). Ici, j’utilise des [Secret mounts](https://docs.docker.com/build/building/secrets/#secret-mounts).
{: .prompt-danger }

> Comme on le verra [plus loin](#6-1-build-de-limage), lors du build de l’image avec ce Dockerfile, vous devez fournir via la variable d’environnement `DL_ENV_PASSWD` la chaîne à utiliser comme mot de passe du compte utilisateur. Pour l’[image distribuée sur Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags), le mot de passe initial est `satisfied-flip-remake`. Utiliser tel quel ce mot de passe par défaut public est *très* risqué : après le premier démarrage du conteneur, modifiez immédiatement ce réglage. Par ailleurs, pour des raisons de sécurité, il est préférable de désactiver l’authentification par mot de passe pour SSH et d’autoriser uniquement la connexion via une clé, et idéalement d’exploiter aussi une clé matérielle comme Yubikey.
>
> La configuration d’un serveur SSH sera abordée en partie dans le prochain article de cette série. Pour aller plus loin, vous pouvez consulter :
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Installer uv et enregistrer les variables d’environnement

> **Prise en compte de la spécification [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) selon [PEP 668](https://peps.python.org/pep-0668/) et adoption de uv (12026.1.6. révision)**
>
> Par le passé, cet article proposait un Dockerfile qui installait directement les paquets via `pip` à l’intérieur de l’image, sans créer de virtualenv (`venv`). La raison était que, dans une image de conteneur à objectif unique, le risque de casser le logiciel système est faible et, même en cas de problème, il suffit de recréer un conteneur à partir de l’image ; il n’y avait donc pas forcément besoin d’un environnement virtuel. Ce point est d’ailleurs partiellement reconnu dans [PEP 668](https://peps.python.org/pep-0668/#use-cases), comme suit.
>> 5. A distro Python when used in a single-application container image (e.g., a Docker container). In this use case, the risk of breaking system software is lower, since generally only a single application runs in the container, and the impact is lower, since you can rebuild the container and you don’t have to struggle to recover a running machine.
>
> Cependant, même dans un conteneur à objectif unique, la norme s’est établie : l’installation via un gestionnaire de paquets Python comme `pip` doit être effectuée uniquement dans un environnement virtuel, afin de séparer strictement les paquets gérés « en externe » (externally managed) par le gestionnaire de paquets de l’OS. J’ai donc révisé le contenu pour créer un environnement virtuel et y installer les paquets nécessaires, afin de respecter [PEP 668](https://peps.python.org/pep-0668/) et la spécification [Externally Managed Environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/), conformément aux standards de l’écosystème Python.
>
> La bibliothèque standard officiellement supportée pour créer et gérer des environnements virtuels est `venv`, comme je l’avais déjà présenté une fois dans un [autre article écrit début 12021](https://www.yunseo.kim/posts/Setting-up-a-Machine-Learning-Development-Environment/#3-creating-an-independent-virtual-environment-recommended). Toutefois, depuis la première publication en 12024 de [`uv`](https://docs.astral.sh/uv/), un gestionnaire Python de paquets et de projets hautes performances développé en Rust par [Astral](https://astral.sh/), celui-ci s’est imposé très rapidement comme nouveau standard de facto grâce, notamment, aux avantages suivants :
> - Une résolution des dépendances et une installation des paquets nettement plus rapides que `pip` (10 à 100×) : <https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md>
> - Une excellente ergonomie
> - Une [très bonne compatibilité avec `pip` et `venv`](https://docs.astral.sh/uv/pip/)
>
> En particulier, les paquets ML comme PyTorch ou RAPIDS abordés ici ont beaucoup de dépendances et sont souvent volumineux : les atouts de `uv` y sont donc pleinement exploités. De plus, [`uv` utilise le cache de façon agressive et efficace](https://docs.astral.sh/uv/concepts/cache/) ; en exploitant correctement les cache mounts lors du build d’image, [on peut réduire fortement le temps de build](https://docs.astral.sh/uv/guides/integration/docker/#caching). C’est pourquoi j’introduis ici `uv` pour la création/gestion de l’environnement virtuel et l’installation des paquets. Je me suis principalement appuyé sur la documentation officielle ["Using uv in Docker"](https://docs.astral.sh/uv/guides/integration/docker/).
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

> **Pourquoi définir `UV_CACHE_DIR` sur `"/tmp/uv-cache"` au lieu de la valeur par défaut `"$HOME_DIR/.cache/uv"` ?**
>
> Normalement, lorsqu’on ajoute un utilisateur via `useradd --create-home`, cet utilisateur doit posséder son répertoire home ; c’est aussi le cas ici.
> Toutefois, lors d’un build d’image avec Podman, j’ai constaté un bug : même si la propriété est correctement transférée dans les couches précédentes, le fait de monter un cache (ou similaire) dans des couches ultérieures peut réinitialiser les métadonnées de propriété du répertoire parent vers la valeur par défaut (propriété root). En cherchant, j’ai trouvé un ticket ouvert il y a environ 3 semaines rapportant le même phénomène : <https://github.com/containers/podman/issues/27777>, mais sans réponse à ce jour. J’ai ajouté en commentaire des détails sur mon cas : <https://github.com/containers/podman/issues/27777#issuecomment-3712237296>.
>
> Pour éviter tout problème même si la propriété est réinitialisée à root, j’ai défini `UV_CACHE_DIR` sur un chemin distinct de `$HOME_DIR`, à savoir `"/tmp/uv-cache"`, pendant l’étape de build. De toute façon, ce cache n’est pas inclus dans l’image finale, donc changer le chemin n’a pas d’impact.
{: .prompt-tip }

### 5-6. Installer Python, créer un environnement virtuel, installer setuptools & pip

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

### 5-7. Installer les paquets ML/DL à utiliser dans l’environnement de développement

#### 5-7-1. Paquets communs

```Dockerfile
# Install ml/dl related packages
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn scikit-image xgboost tqdm
```

#### 5-7-2. PyTorch & bibliothèques d’accélération GPU spécifiques à CUDA

##### Installer uniquement PyTorch

Pour n’installer que PyTorch, ajoutez ceci au Dockerfile.

```Dockerfile
RUN --mount=type=cache,target=$UV_CACHE_DIR,uid=$USER_UID,gid=$USER_GID \
    uv pip install -U "torch~=2.9.1" "torchvision~=0.24.1" "torchaudio~=2.9.1" \
        --index-url https://download.pytorch.org/whl/cu130
```

##### PyTorch & Cupy & RAPIDS & DALI

Pour utiliser non seulement PyTorch, mais aussi Cupy, RAPIDS (cuDF, cuML, cuGraph, cuxfilter, cuCIM, RAFT, cuVS) et DALI, ajoutez ceci au Dockerfile.

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

> PyTorch et les paquets RAPIDS partagent certaines bibliothèques dépendantes (cuBLAS, NVRTC, cuFFT, cuRAND, cuSOLVER, cuSPARSE). Si on installe séparément, il est probable que les versions requises divergent ; la version installée en premier peut être écrasée par la suivante, entraînant des conflits de dépendances. Il est donc préférable de regrouper l’installation en une seule commande `uv pip install`, afin que le resolver prenne en compte toutes les contraintes simultanément, en donnant la priorité aux versions requises par PyTorch.
{: .prompt-tip }

### 5-8. Créer un répertoire de travail (workspace)

```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
ENV UV_CACHE_DIR="$HOME_DIR/.cache/uv"
ENV UV_PYTHON_CACHE_DIR="$UV_CACHE_DIR/python"
```

### 5-9. Ouvrir les ports et configurer l’`ENTRYPOINT` à exécuter au démarrage du conteneur

Pour l’accès via SSH et Jupyter Lab, ouvrez les ports 22 et 8888.  
De plus, comme le lancement automatique du démon SSH au démarrage du conteneur nécessite les droits root, on utilisera la méthode suivante :
1. Démarrer le conteneur en étant connecté en tant que root
2. Juste après le démarrage, exécuter le script `/entrypoint.sh`{: .filepath}
3. Dans ce script, démarrer le service SSH puis basculer vers le compte `remote` via [`gosu`](https://github.com/tianon/gosu)
4. Si aucun ordre n’est fourni lors de l’exécution du conteneur, lancer par défaut Jupyter Lab en tant que `remote` (droits non-root)

> En général, l’usage de `sudo` ou `su` à l’intérieur d’un conteneur Docker/Podman n’est pas recommandé. Si des privilèges root sont nécessaires, il vaut mieux démarrer le conteneur en tant que root, exécuter les tâches qui nécessitent root, puis basculer vers un utilisateur non-root avec [`gosu`](https://github.com/tianon/gosu), comme décrit ici. Les raisons sont détaillées dans les ressources suivantes :
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

D’abord, ajoutez ce qui suit à la fin du Dockerfile.

```Dockerfile
# Switch to root
USER root

# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Ensuite, dans le même répertoire que le Dockerfile, créez un fichier script nommé `entrypoint.sh`{: .filepath} et écrivez-le comme suit.

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

> En général, un processus lancé via `docker exec` ou `CMD` hérite tel quel des variables `ENV` de Docker. En revanche, une session ouverte via SSH n’hérite souvent pas automatiquement des variables d’environnement du conteneur, car SSH crée une nouvelle session de shell à la connexion.
>
> Pour résoudre cela et permettre l’accès (via SSH) aux variables prédéfinies comme `$WORK_DIR`, il faut « dumper » les variables dans `/etc/environment`{: .filepath } avant de démarrer le service SSH lors de l’exécution du conteneur, par exemple avec `printenv | grep _ >> /etc/environment`.
>
> Les liens suivants peuvent aider :
> - <https://stackoverflow.com/questions/34630571/docker-env-variables-not-set-while-log-via-shell>
> - <https://github.com/moby/moby/issues/2569>

## 6. Build d’image OCI et exécution du conteneur

### 6-1. Build de l’image

Ouvrez un terminal dans le répertoire où se trouve le Dockerfile et définissez la variable d’environnement `DL_ENV_PASSWD`.

```bash
export DL_ENV_PASSWD="<your_own_password>"
```

> Remplacez \<your_own_password\> par le mot de passe de connexion à utiliser pour SSH.
{: .prompt-info }

Ensuite, **ne fermez pas cette fenêtre de terminal**, et exécutez la commande ci-dessous dans la même session pour lancer le build.

#### Cas de Podman

```bash
podman build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 -f ./Dockerfile \
--security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

> Avec Podman, si vous souhaitez construire l’image non seulement pour la plateforme (OS/architecture) de votre machine, mais pour toutes les plateformes supportées par l’image de base (en vue de la distribution), utilisez l’option [`--all-platforms`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#all-platforms) et remplacez `--tag`/`-t` par l’option [`--manifest`](https://docs.podman.io/en/stable/markdown/podman-build.1.html#platform-os-arch-variant), comme suit :
>
> ```bash
> podman build --all-platforms --manifest dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> -f ./Dockerfile --security-opt=label=disable --secret=id=USER_PASSWORD,env=DL_ENV_PASSWD .
> ```
>
> Je ne détaille pas ici l’équivalent côté Docker ; si nécessaire, référez-vous à la [documentation officielle Docker](https://docs.docker.com/build/building/multi-platform/).
{: .prompt-tip }

#### Cas de Docker

```bash
docker build -t dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
-f ./Dockerfile --secret id=USER_PASSWORD,env=DL_ENV_PASSWD .
```

### 6-2. Exécuter une charge de travail (workload) d’exemple

Une fois le build terminé, exécutez un conteneur jetable pour vérifier que tout fonctionne.

Avec Podman :

```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

Avec Docker :
```bash
docker run -itd --rm --name test-container \
--gpus all -p 2222:22 -p 8888:8888 \
dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04
```

En saisissant ces commandes, vous lancez un conteneur nommé `test-container` depuis l’image `dl-env:cuda13.0.2-cudnn9.14.0-ubuntu24.04`, puis vous mappez le port 2222 de l’hôte vers le port 22 du conteneur, et le port 8888 de l’hôte vers le port 8888 du conteneur. Si l’image a été correctement construite et que le conteneur a démarré sans erreur, JupyterLab doit tourner dans le conteneur sur l’adresse par défaut `http:127.0.0.1:8888`. Ainsi, si vous ouvrez un navigateur sur la machine hôte et accédez à <http://127.0.0.1:8888>, vous serez redirigé vers `http://127.0.0.1:8888` à l’intérieur du conteneur, et l’écran suivant doit apparaître.

![JupyterLab Interface Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Sur l’hôte, ouvrez un terminal et exécutez `ssh remote@127.0.0.1 -p 2222` pour tenter une connexion distante sur le compte `remote` du système Ubuntu à l’intérieur du conteneur.  
Lors de la première connexion, vous n’avez aucune information sur la clé de l’hôte et un avertissement indique que l’authenticité ne peut pas être vérifiée ; on vous demande si vous souhaitez continuer : saisissez `yes` pour poursuivre.  
Ensuite, pour vous authentifier, saisissez le mot de passe défini lors du build (ou, si vous vous connectez pour la première fois après avoir *pull* l’[image distribuée sur Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags), le mot de passe initial `satisfied-flip-remake`).

```bash
$ ssh remote@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ED25519 key fingerprint is {핑거프린트(각 키마다 제각기 다른 고유한 값을 가진다)}.
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

Si l’affichage est globalement similaire à l’exemple ci-dessus, la connexion SSH distante a réussi. Pour terminer la session, tapez `exit`.

### 6-3. (optionnel) Push sur Docker Hub

Pour pouvoir *pull* et réutiliser l’image d’environnement de développement quand vous en avez besoin, il est conseillé de la *push* sur Docker Hub.  

> Pour *push* votre image sur Docker Hub, il vous faut un compte Docker. Si vous n’en avez pas encore, inscrivez-vous sur <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Connexion à Docker Hub

##### Cas de Podman

```bash
podman login docker.io
```

##### Cas de Docker

```bash
docker login
```

#### 6-3-2. Taguer l’image

Remplissez `<dockerhub_username>`, `<repository_name>` et (optionnel) `:TAG` avec vos propres valeurs.  
Ex. : `"yunseokim"`, `"dl-env"`, `"rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04"`

> Si vous avez construit l’image non seulement pour la plateforme de votre machine (OS/architecture) mais aussi pour toutes les plateformes supportées par l’image de base, et que vous voulez *push* en bloc la liste de manifest (ou index d’images), sautez cette étape et passez directement à l’étape [Push de l’image](#6-3-3-push-de-limage).
{: .prompt-tip }

##### Cas de Podman

```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Cas de Docker

```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push de l’image

Enfin, exécutez la commande ci-dessous pour *push* l’image sur Docker Hub.

##### Cas de Podman

```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

> Avec Podman, pour *push* en une seule fois, sous forme de liste de manifest ou d’index d’images, l’ensemble des images correspondant à plusieurs plateformes, utilisez [`podman manifest push`](https://docs.podman.io/en/stable/markdown/podman-manifest-push.1.htmls) comme suit :
>
> ```bash
> podman manifest push --all REPOSITORY:MANIFEST_TAG \
> docker.io/<dockerhub_username>/<repository_name>[:TAG]
> ```
>
> Ex. :
>
> ```bash
> podman manifest push --all dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04 \
> docker.io/yunseokim/dl-env:rapids-cuda13.0.2-cudnn9.14.0-ubuntu24.04
> ```
>
{: .prompt-tip }

##### Cas de Docker

```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```

Vous pouvez vérifier sur <https://hub.docker.com/> que le *push* a bien réussi, comme ci-dessous.

![Docker Hub Screenshot](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

L’image finalisée via les étapes ci-dessus est publiée dans le dépôt public Docker Hub [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags), et tout le monde peut l’utiliser librement.

Pour *pull* l’image, reprenez la commande utilisée pour le *push* et remplacez simplement `push` par `pull`.
