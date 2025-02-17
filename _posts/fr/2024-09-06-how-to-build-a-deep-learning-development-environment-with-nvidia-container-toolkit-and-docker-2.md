---
title: Construire un environnement de développement pour l'apprentissage profond avec NVIDIA Container Toolkit et Docker/Podman (2) - Configuration du runtime de conteneur pour l'utilisation du GPU, rédaction du Dockerfile et construction de l'image de conteneur
description: Cette série couvre la mise en place d'un environnement de développement pour l'apprentissage profond basé sur des conteneurs en utilisant NVIDIA Container Toolkit localement, et la configuration de SSH et Jupyter Lab pour l'utiliser comme serveur distant. Ce billet est le deuxième de la série et traite du processus de rédaction du Dockerfile et de construction de l'image de conteneur.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Aperçu
Cette série couvre l'installation de NVIDIA Container Toolkit et Docker ou Podman, et le processus de construction d'un environnement de développement pour l'apprentissage profond en écrivant un Dockerfile basé sur les images CUDA et cuDNN fournies par le [dépôt nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub. Le [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) et [l'image](https://hub.docker.com/r/yunseokim/dl-env/tags) complétés à travers ce processus sont partagés via GitHub et Docker Hub pour que ceux qui en ont besoin puissent les utiliser librement, et un guide de configuration SSH et Jupyter Lab est également fourni pour une utilisation comme serveur distant.  
La série se composera de 3 articles, et celui-ci est le deuxième de la série.
- [Partie 1 : Installation de NVIDIA Container Toolkit & du moteur de conteneur](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Partie 2 : Configuration du runtime de conteneur pour l'utilisation du GPU, rédaction du Dockerfile et construction de l'image de conteneur (cet article)
- Partie 3 (à venir)

Nous supposons un environnement Linux x86_64 avec une carte graphique NVIDIA prenant en charge CUDA, et bien que certains détails puissent différer légèrement pour les distributions autres qu'Ubuntu ou Fedora, car ils n'ont pas été testés directement.  
(Mise à jour du contenu le 18.02.2025)

> **Avis de correction d'erreur**  
> Dans la version initiale de cet article publiée en août 2024, il y avait quelques erreurs dans la section [Rédaction du Dockerfile](#5-rédaction-du-dockerfile) et dans l'image construite à partir de ce Dockerfile. Les problèmes étaient les suivants :
> - La partie de création du compte remote où le mot de passe était défini était incorrecte, et il n'était pas possible de se connecter avec le mot de passe "000000" comme prévu initialement
> - Le démon SSH ne démarrait pas automatiquement au lancement du conteneur
>
> Ces problèmes ont été récemment identifiés, et vers 2h du matin (UTC+9) le 16 février 2025, le Dockerfile et les images Docker problématiques ont été remplacés par des fichiers corrigés sur le [dépôt GitHub](https://github.com/yunseo-kim/dl-env-docker) et [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> Si vous avez récupéré le Dockerfile ou l'image Docker avant cette date, veuillez les remplacer par la version corrigée.  
> Nous nous excusons auprès de ceux qui auraient pu être confus par le contenu erroné parmi ceux qui se sont référés à cet article précédemment.
{: .prompt-info }

## Avant de commencer
Cet article fait suite à la [partie 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), donc si vous ne l'avez pas encore lue, il est recommandé de commencer par là.

## 4. Configuration du runtime de conteneur
### Si vous utilisez Podman
[Configurez en utilisant CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Exécutez la commande suivante pour générer le fichier de spécification CDI dans le répertoire `/etc/cdi`{: .filepath} :
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> Si vous changez de carte graphique ou modifiez la configuration du pilote CUDA (y compris la mise à niveau de version), vous devez régénérer le fichier de spécification CDI.
{: .prompt-warning }

> L'utilisation du hook NVIDIA Container Runtime avec CDI peut causer des conflits, donc si `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existe, supprimez ce fichier ou évitez d'exécuter des conteneurs avec la variable d'environnement `NVIDIA_VISIBLE_DEVICES` définie.
{: .prompt-warning }

### Si vous utilisez Docker
Nous expliquons sur la base du [mode rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configurer le runtime de conteneur avec la commande `nvidia-ctk`
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
Cette commande modifie le fichier `/etc/docker/daemon.json`{: .filepath} pour permettre à Docker d'utiliser le NVIDIA Container Runtime.

#### 4-Docker-2. Redémarrer le démon Docker
Redémarrez le démon Docker pour appliquer les modifications de configuration.
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configurer le fichier de configuration `/etc/nvidia-container-runtime/config.toml`{: .filepath} avec la commande `sudo nvidia-ctk`
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Vérifier que la configuration est correcte
Exécutez un conteneur CUDA d'exemple.

Si vous utilisez Podman, exécutez la commande suivante :
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Si vous utilisez Docker, exécutez la commande suivante :
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Si un écran similaire à celui ci-dessous s'affiche, c'est un succès.

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
Nous allons écrire un Dockerfile pour l'environnement de développement basé sur les images CUDA et cuDNN fournies par le [dépôt nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub.

- Vous devez choisir l'image à utiliser en tenant compte de la version CUDA et cuDNN requise, du type et de la version de distribution Linux, etc. 
- ![Version CUDA prise en charge par PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)Au moment de la rédaction de cet article fin août 2024, la dernière version de PyTorch, 2.4.0, prend en charge CUDA 12.4. Nous utiliserons donc ici l'image [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Vous pouvez vérifier la dernière version de PyTorch et la version CUDA prise en charge sur le [site web de PyTorch](https://pytorch.org/get-started/locally/).

Le code source du Dockerfile complet est disponible dans le dépôt GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Ci-dessous, nous expliquons étape par étape le processus de rédaction de ce Dockerfile.

### 5-1. Spécifier l'image de base
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Installer les utilitaires de base et les prérequis Python
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

### 5-3. Configurer le fuseau horaire du système (nous utilisons 'Asia/Seoul' dans cet article)
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. Configurer le serveur SSH pour l'accès à distance  
Pour des raisons de sécurité, configurez de manière à ce que la connexion au compte root soit impossible lors de l'accès SSH à distance.
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Créez un utilisateur non-root nommé 'remote' à utiliser pour la connexion SSH.
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

> Lors de la construction de l'image Docker à l'aide de ce Dockerfile, si aucune option n'est spécifiée séparément, la valeur initiale du mot de passe du compte 'remote' est 000000. Ceci est très vulnérable en termes de sécurité, donc lors de la construction de l'image Docker, utilisez l'option `--build-arg` pour spécifier séparément le mot de passe de connexion au compte, ou modifiez immédiatement les paramètres après avoir exécuté le conteneur pour la première fois. Pour la sécurité, il est souhaitable de désactiver la connexion par mot de passe lors de la connexion SSH et de configurer ultérieurement pour que la connexion ne soit possible que via un fichier de clé séparé, et l'utilisation d'une clé matérielle comme Yubikey serait idéale.
> La configuration du serveur SSH sera abordée dans une certaine mesure dans la prochaine partie de cette série, et si vous voulez en savoir plus, vous pouvez consulter les documents suivants :
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> De plus, ce Dockerfile suppose que l'image construite ne sera utilisée que par vous-même ou un petit groupe d'initiés de confiance, et si vous devez distribuer l'image construite à l'extérieur, l'utilisation de `--build-arg` pour définir le mot de passe est dangereuse et une autre méthode doit être utilisée. Veuillez vous référer à [ce document](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/).
{: .prompt-danger }

### 5-5. Installer setuptools, pip et enregistrer la variable d'environnement PATH
```Dockerfile
# Switch to remote user
ENV USER_NAME="$USER_NAME"
USER $USER_NAME
WORKDIR $HOME_DIR

# Install pip and ml/dl related packages
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME_DIR/.local/bin:$PATH"
```

### 5-6. Installer les packages d'apprentissage automatique et d'apprentissage profond à utiliser dans l'environnement de développement
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Si vous voulez utiliser Cupy, cuDF, cuML et DALI, ajoutez également le contenu suivant au Dockerfile :
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Créer un répertoire à utiliser comme espace de travail
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Ouvrir les ports et configurer l'`ENTRYPOINT` à exécuter au démarrage du conteneur
Ouvrez les ports 22 et 8888 pour l'accès SSH et Jupyter Lab.  
De plus, pour exécuter automatiquement le démon SSH au démarrage du conteneur, les privilèges root sont nécessaires, donc nous utiliserons la méthode suivante :
1. État connecté en tant que compte root au démarrage du conteneur
2. Exécution du script `/entrypoint.sh`{: .filepath} immédiatement après le démarrage du conteneur
3. Démarrage du service SSH dans ce script, puis passage au compte remote en utilisant [`gosu`](https://github.com/tianon/gosu)
4. Si aucune commande n'est spécifiée séparément lors de l'exécution du conteneur, exécution de Jupyter Lab par défaut avec le compte remote (privilèges non-root)

> En général, l'utilisation de `sudo` ou `su` à l'intérieur d'un conteneur Docker ou Podman n'est pas recommandée, et si des privilèges root sont nécessaires, il est préférable de démarrer le conteneur en tant que compte root comme expliqué ici, d'effectuer les tâches nécessitant des privilèges root, puis de passer à un utilisateur non-root en utilisant [`gosu`](https://github.com/tianon/gosu). Les raisons pour lesquelles cela doit être fait sont expliquées en détail dans les ressources ci-dessous, qui peuvent être utiles si nécessaire.
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

Tout d'abord, entrez le contenu suivant dans la dernière partie du Dockerfile :
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Ensuite, créez un fichier de script nommé `entrypoint.sh`{: .filepath} dans le même chemin que le Dockerfile que vous avez écrit, et écrivez le contenu comme suit :
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

## 6. Construction de l'image Docker et exécution du conteneur
### 6-1. Construction de l'image
Ouvrez un terminal dans le répertoire où se trouve le Dockerfile et exécutez la commande suivante :
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> À la place de \<password\>, entrez le mot de passe de connexion à utiliser lors de l'accès SSH.
{: .prompt-info }

### 6-2. Exécution d'une charge de travail d'exemple
Une fois la construction terminée, exécutez un conteneur jetable pour vérifier qu'il fonctionne correctement.

Pour Podman, exécutez la commande suivante :
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Pour Docker, exécutez la commande suivante :
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Lorsque vous entrez la commande ci-dessus dans le terminal, elle exécute un conteneur nommé `test-container` à partir de l'image `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` précédemment construite, puis connecte le port 22 du système hôte au port 22 de ce conteneur, et le port 88 du système hôte au port 8888 du conteneur. Si l'image Docker a été correctement construite à l'étape précédente et que le conteneur a démarré sans problème, JupyterLab devrait être en cours d'exécution à l'adresse par défaut `http:127.0.0.1:8888` à l'intérieur du conteneur `test-container`. Par conséquent, lorsque vous ouvrez un navigateur sur le système hôte où le moteur Docker fonctionne et accédez à <http://127.0.0.1:88>, il devrait se connecter à l'adresse `http://127.0.0.1:8888` à l'intérieur du conteneur et afficher un écran similaire à celui ci-dessous.

![Capture d'écran de l'interface JupyterLab](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Ouvrez un terminal sur le système hôte et exécutez la commande `ssh remote@127.0.0.1` pour vous connecter à distance au compte remote du système Ubuntu en cours d'exécution à l'intérieur du conteneur.  
Lors de la première connexion, un avertissement s'affichera indiquant qu'il n'y a pas d'informations sur la clé de chiffrement de la cible de connexion et que l'authentification est impossible, et il vous sera demandé si vous souhaitez continuer la connexion. Entrez "yes" pour continuer.  
Ensuite, entrez le mot de passe pour vous connecter (s'il n'a pas été modifié lors de la construction de l'image, ce sera la valeur par défaut "000000").
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {empreinte digitale (chaque clé a une valeur unique différente)}.
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
Si l'affichage est à peu près similaire à ce qui précède, la connexion à distance via SSH a réussi. Pour terminer la connexion, entrez la commande `exit`.

### 6-3. (optionnel) Push vers Docker Hub
Pour pouvoir utiliser l'image d'environnement de développement créée à travers le processus précédent à tout moment en la récupérant lorsque nécessaire, il est bon de la pousser sur Docker Hub.  

> Pour pousser votre propre image sur Docker Hub, vous avez besoin de votre propre compte Docker, donc si vous n'en avez pas encore, inscrivez-vous d'abord sur <https://app.docker.com/signup>.
{: .prompt-tip }

#### 6-3-1. Connexion à Docker Hub
##### Pour Podman
```bash
podman login docker.io
```

##### Pour Docker
```bash
docker login
```

#### 6-3-2. Étiquetage de l'image
Remplacez `<dockerhub_username>`, `<repository_name>`, et (optionnel) `:TAG` par vos propres informations.  
Par exemple : "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### Pour Podman
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Pour Docker
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Push de l'image
Enfin, exécutez la commande suivante pour pousser l'image sur Docker Hub.

##### Pour Podman
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Pour Docker
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Vous pouvez vérifier que le push a bien été effectué sur <https://hub.docker.com/> comme ci-dessous.  
![Capture d'écran de Docker Hub](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

L'image complétée à travers le processus précédent a été rendue publique dans le dépôt public [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) sur Docker Hub, et peut être utilisée librement par quiconque.

Pour récupérer l'image, il suffit de changer la partie `push` en `pull` dans la commande utilisée précédemment pour le push.
