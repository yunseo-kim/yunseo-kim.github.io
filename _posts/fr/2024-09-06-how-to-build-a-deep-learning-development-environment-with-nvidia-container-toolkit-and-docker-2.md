---
title: Construire un environnement de développement pour le deep learning avec NVIDIA Container Toolkit et Docker/Podman (2) - Configuration du runtime de conteneur pour l'utilisation du GPU, rédaction du Dockerfile et construction de l'image de conteneur
description: Cette série traite de la mise en place d'un environnement de développement pour le deep learning basé sur des conteneurs avec NVIDIA Container Toolkit en local, et de la configuration de SSH et Jupyter Lab pour l'utiliser comme serveur distant. Ce billet est le deuxième de la série et couvre le processus de rédaction d'un Dockerfile et de construction d'une image de conteneur.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Aperçu
Dans cette série, nous abordons le processus d'installation de NVIDIA Container Toolkit et Docker ou Podman, et la création d'un environnement de développement pour le deep learning en écrivant un Dockerfile basé sur les images CUDA et cuDNN fournies par le [dépôt nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub. Pour ceux qui en ont besoin, je partage le [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) et [l'image](https://hub.docker.com/r/yunseokim/dl-env/tags) complétés via GitHub et Docker Hub, ainsi qu'un guide de configuration SSH et Jupyter Lab pour l'utilisation comme serveur distant.  
La série se composera de 3 articles, et celui-ci est le deuxième de la série.
- [Partie 1: Installation de NVIDIA Container Toolkit et du moteur de conteneur](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Partie 2: Configuration du runtime de conteneur pour l'utilisation du GPU, rédaction du Dockerfile et construction de l'image de conteneur (cet article)
- Partie 3 (à venir)

Je suppose que vous utilisez un système Linux x86_64 avec une carte graphique NVIDIA compatible CUDA. Bien que j'ai principalement testé sur Ubuntu et Fedora, certains détails peuvent varier légèrement sur d'autres distributions.  
(Mis à jour le 18.02.12025)

> **Avis de correction d'erreur**  
> Dans la version initiale de cet article publiée en août 12024 du [calendrier holocène](https://en.wikipedia.org/wiki/Holocene_calendar), il y avait quelques erreurs dans la section [Rédaction du Dockerfile](#5-rédaction-du-dockerfile) et dans l'image construite à partir de ce Dockerfile. Les problèmes étaient les suivants:
> - La partie concernant la création du compte remote avait un problème dans la configuration du mot de passe, et il n'était pas possible de se connecter avec le mot de passe "000000" comme prévu
> - Le démon SSH ne démarrait pas automatiquement au lancement du conteneur
>
> J'ai récemment pris conscience de ces problèmes et, vers 2h du matin le 16 février 12025 (UTC+9), j'ai remplacé le Dockerfile problématique et les images Docker par des versions corrigées sur le [dépôt GitHub](https://github.com/yunseo-kim/dl-env-docker) et [Docker Hub](https://hub.docker.com/r/yunseokim/dl-env/tags).  
> Si vous avez téléchargé le Dockerfile ou l'image Docker avant cette date, veuillez les remplacer par les versions corrigées.  
> Je présente mes excuses à tous ceux qui ont pu être confrontés à des difficultés en raison de ces erreurs.
{: .prompt-info }

## Avant de commencer
Cet article fait suite à la [première partie](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), donc si vous ne l'avez pas encore lue, je vous recommande de la lire d'abord.

## 4. Configuration du runtime de conteneur
### Si vous utilisez Podman
[Configurez en utilisant CDI (Container Device Interface).](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html)

Exécutez la commande suivante pour générer le fichier de spécification CDI dans le répertoire `/etc/cdi`{: .filepath}:
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
> Si vous changez de carte graphique ou modifiez la configuration du pilote CUDA (y compris les mises à niveau de version), vous devrez régénérer le fichier de spécification CDI.
{: .prompt-warning }

> L'utilisation du hook NVIDIA Container Runtime avec CDI peut provoquer des conflits. Si le fichier `/usr/share/containers/oci/hooks.d/oci-nvidia-hook.json`{: .filepath} existe, supprimez-le ou évitez d'exécuter des conteneurs avec la variable d'environnement `NVIDIA_VISIBLE_DEVICES` définie.
{: .prompt-warning }

### Si vous utilisez Docker
Les explications sont basées sur le [mode rootless](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#rootless-mode).

#### 4-Docker-1. Configurer le runtime de conteneur avec la commande `nvidia-ctk`
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
```
Cette commande modifie le fichier `/etc/docker/daemon.json`{: .filepath} pour permettre à Docker d'utiliser NVIDIA Container Runtime.

#### 4-Docker-2. Redémarrer le démon Docker
Redémarrez le démon Docker pour appliquer les modifications:
```bash
systemctl --user restart docker
```

#### 4-Docker-3. Configurer le fichier `/etc/nvidia-container-runtime/config.toml`{: .filepath} avec la commande `sudo nvidia-ctk`
```bash
sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```

### Vérifier que tout est correctement configuré
Exécutez un conteneur CUDA d'exemple.

Si vous utilisez Podman:
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi
```

Si vous utilisez Docker:
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```
Si vous voyez un affichage similaire à celui ci-dessous, c'est un succès:

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
Nous allons créer un Dockerfile pour notre environnement de développement basé sur les images CUDA et cuDNN fournies par le [dépôt nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub.

- Vous devez choisir une image en fonction des versions de CUDA et cuDNN dont vous avez besoin, ainsi que du type et de la version de distribution Linux. 
- ![Version CUDA supportée par PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)À la date de rédaction de cet article (fin août 12024), la dernière version de PyTorch (2.4.0) prend en charge CUDA 12.4. Par conséquent, nous utiliserons l'image [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Vous pouvez vérifier la dernière version de PyTorch et les versions CUDA prises en charge sur le [site web de PyTorch](https://pytorch.org/get-started/locally/).

Le Dockerfile complet est disponible dans le dépôt GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Voici une explication étape par étape de sa création.

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

### 5-3. Configurer le fuseau horaire (dans cet article, 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"  # If necessary, replace it with a value that works for you.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 5-4. Configurer le serveur SSH pour l'accès à distance  
Pour des raisons de sécurité, configurez SSH pour empêcher la connexion en tant que root:
```Dockerfile
# Set up SSH server
RUN mkdir /var/run/sshd
RUN echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
```

Créez un utilisateur non-root nommé 'remote' pour les connexions SSH:
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

> Lors de la construction de l'image Docker avec ce Dockerfile, si aucune option n'est spécifiée, le mot de passe initial du compte 'remote' sera 000000. C'est très vulnérable sur le plan de la sécurité, donc utilisez l'option `--build-arg` lors de la construction pour spécifier un mot de passe différent, ou changez-le immédiatement après le premier démarrage du conteneur. Pour une meilleure sécurité, il est recommandé de désactiver la connexion par mot de passe SSH et de n'autoriser que la connexion via des fichiers de clés, voire d'utiliser une clé matérielle comme Yubikey.
> La configuration du serveur SSH sera abordée dans la prochaine partie de cette série. Pour plus de détails, consultez les documents suivants:
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

> De plus, ce Dockerfile suppose que l'image construite ne sera utilisée que par vous-même ou un petit groupe de personnes de confiance. Si vous devez distribuer l'image à l'extérieur, l'utilisation de `--build-arg` pour définir des mots de passe est dangereuse et d'autres méthodes devraient être utilisées. Consultez [ce document](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/) pour plus d'informations.
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

### 5-6. Installer les packages de machine learning et deep learning
```Dockerfile
RUN python3 -m pip install -U \
        jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm \
    && python3 -m pip install -U torch torchvision torchaudio \
        --index-url https://download.pytorch.org/whl/cu124
```
Si vous souhaitez utiliser Cupy, cuDF, cuML et DALI, ajoutez également ceci au Dockerfile:
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x \
    && python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com \
        cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Créer un répertoire de travail
```Dockerfile
# Create a workspace directory to locate jupyter notebooks and .py files
ENV WORK_DIR="$HOME_DIR/workspace"
RUN mkdir -p $WORK_DIR
```

### 5-8. Exposer les ports et configurer l'`ENTRYPOINT` à exécuter au démarrage du conteneur
Exposez les ports 22 et 8888 pour SSH et Jupyter Lab.  
Pour exécuter automatiquement le démon SSH au démarrage du conteneur, nous avons besoin des privilèges root, donc nous utiliserons l'approche suivante:
1. Le conteneur démarre en tant que root
2. Le script `/entrypoint.sh`{: .filepath} s'exécute juste après le démarrage
3. Ce script démarre le service SSH puis utilise [`gosu`](https://github.com/tianon/gosu) pour passer au compte remote
4. Si aucune commande n'est spécifiée lors du lancement du conteneur, Jupyter Lab démarre par défaut avec le compte remote (privilèges non-root)

> En général, l'utilisation de `sudo` ou `su` dans les conteneurs Docker ou Podman n'est pas recommandée. Si des privilèges root sont nécessaires, il est préférable de démarrer le conteneur en tant que root, d'effectuer les tâches nécessitant ces privilèges, puis de passer à un utilisateur non-root avec [`gosu`](https://github.com/tianon/gosu). Les raisons sont expliquées en détail dans les ressources suivantes:
> - <https://docs.docker.com/build/building/best-practices/#user>
> - <https://www.sobyte.net/post/2023-01/docker-gosu-su-exec/>
> - <https://www.baeldung.com/linux/docker-image-container-switch-user>
> - <https://docsaid.org/en/blog/gosu-usage/>
{: .prompt-tip }

D'abord, ajoutez ce qui suit à la fin de votre Dockerfile:
```Dockerfile
# Expose SSH and Jupyter Lab ports
EXPOSE 22 8888

# Switch to root
USER root

# Copy the entry point script and grant permission to run it
COPY --chmod=755 entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

Ensuite, créez un fichier script nommé `entrypoint.sh`{: .filepath} dans le même répertoire que votre Dockerfile avec le contenu suivant:
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
Ouvrez un terminal dans le répertoire contenant votre Dockerfile et exécutez:
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> Remplacez \<password\> par le mot de passe que vous souhaitez utiliser pour la connexion SSH.
{: .prompt-info }

### 6-2. Exécution d'une charge de travail d'exemple
Une fois la construction terminée, exécutez un conteneur jetable pour vérifier que tout fonctionne correctement.

Pour Podman:
```bash
podman run -itd --rm --name test-container --device nvidia.com/gpu=all \
--security-opt=label=disable -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Pour Docker:
```bash
docker run -itd --rm --name test-container \
--gpus all -p 22:22 -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```

Cette commande exécute un conteneur nommé `test-container` à partir de l'image `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` que vous venez de construire, en mappant le port 22 du conteneur au port 22 de l'hôte et le port 8888 du conteneur au port 88 de l'hôte. Si l'image Docker a été correctement construite et que le conteneur a démarré sans problème, JupyterLab devrait s'exécuter à l'adresse `http:127.0.0.1:8888` à l'intérieur du conteneur. Vous devriez donc pouvoir ouvrir un navigateur sur le système hôte et accéder à <http://127.0.0.1:88>, qui se connectera à l'adresse `http://127.0.0.1:8888` à l'intérieur du conteneur, affichant un écran similaire à celui-ci:

![Capture d'écran de l'interface JupyterLab](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

Ouvrez un terminal sur le système hôte et exécutez la commande `ssh remote@127.0.0.1` pour vous connecter à distance au compte remote du système Ubuntu exécuté dans le conteneur.  
Lors de la première connexion, vous recevrez un avertissement indiquant que l'authenticité de l'hôte ne peut pas être établie et on vous demandera si vous souhaitez continuer la connexion. Tapez "yes" pour continuer.  
Ensuite, entrez le mot de passe (si vous ne l'avez pas changé lors de la construction de l'image, ce sera la valeur par défaut "000000").
```bash
$ ssh remote@127.0.0.1
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ED25519 key fingerprint is {empreinte digitale (chaque clé a une valeur unique)}.
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
Si vous voyez un affichage similaire, vous avez réussi à vous connecter via SSH. Pour terminer la session, tapez la commande `exit`.

### 6-3. (facultatif) Pousser l'image vers Docker Hub
Pour pouvoir utiliser votre image d'environnement de développement à tout moment en la récupérant, il est bon de la pousser vers Docker Hub.

> Pour pousser votre image vers Docker Hub, vous avez besoin d'un compte Docker. Si vous n'en avez pas encore, inscrivez-vous d'abord sur <https://app.docker.com/signup>.
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

#### 6-3-2. Attribution d'un tag à l'image
Remplacez `<dockerhub_username>`, `<repository_name>` et (optionnel) `:TAG` par vos propres informations.  
Par exemple: "yunseokim", "dl-env", "rapids-cuda12.4.1-cudnn9.1.0-ubuntu22.04"

##### Pour Podman
```bash
podman tag IMAGE_ID docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Pour Docker
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```

#### 6-3-3. Pousser l'image
Enfin, exécutez la commande suivante pour pousser l'image vers Docker Hub:

##### Pour Podman
```bash
podman push docker.io/<dockerhub_username>/<repository_name>[:TAG]
```

##### Pour Docker
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Vous pouvez vérifier que l'image a bien été poussée sur <https://hub.docker.com/>, comme illustré ci-dessous:  
![Capture d'écran Docker Hub](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

L'image complétée à travers ce processus est disponible publiquement dans le dépôt [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) sur Docker Hub, et peut être utilisée librement par quiconque.

Pour récupérer l'image, il suffit de remplacer `push` par `pull` dans la commande utilisée précédemment pour la pousser.
