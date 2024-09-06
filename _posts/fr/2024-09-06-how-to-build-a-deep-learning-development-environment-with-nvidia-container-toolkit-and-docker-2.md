---
title: "Construire un environnement de développement pour l'apprentissage profond avec NVIDIA Container Toolkit et Docker (2) - Configuration du runtime de conteneur pour l'utilisation du GPU, rédaction du Dockerfile et construction de l'image Docker"
description: >-
  Cette série traite de la mise en place d'un environnement de développement pour l'apprentissage profond basé sur NVIDIA Container Toolkit et Docker en local, et de la configuration de SSH et Jupyter Lab pour l'utiliser comme serveur distant. Ce post est le deuxième article de la série, qui présente la méthode de configuration du runtime de conteneur pour l'utilisation du GPU, la rédaction du Dockerfile et la construction de l'image Docker.
categories:
  - Data Science
  - Machine Learning
  - Deep Learning
tags:
  - Development Environment
---

## Aperçu
Dans cette série, nous abordons le processus d'installation de NVIDIA Container Toolkit et Docker, et de construction d'un environnement de développement pour l'apprentissage profond en écrivant un Dockerfile basé sur les images CUDA et cuDNN fournies par le [dépôt nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub. Pour ceux qui en ont besoin, nous partageons le [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) et l'[image](https://hub.docker.com/r/yunseokim/dl-env/tags) complétés à travers ce processus via GitHub et Docker Hub pour une utilisation libre, et fournissons en plus un guide de configuration SSH et Jupyter Lab pour une utilisation comme serveur distant.  
La série se composera de 3 articles, et cet article que vous lisez est le deuxième de la série.
- [Partie 1 : Installation de NVIDIA Container Toolkit & Docker Engine](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1)
- Partie 2 : Configuration du runtime de conteneur pour l'utilisation du GPU, rédaction du Dockerfile et construction de l'image Docker (cet article)
- Partie 3 (à venir)

Nous procédons en supposant un système équipé d'une carte graphique NVIDIA prenant en charge CUDA dans un environnement Linux x86_64, et comme nous n'avons pas testé directement sur des distributions autres qu'Ubuntu ou Fedora, il peut y avoir de légères différences dans certains détails spécifiques.

## Avant de commencer
Cet article fait suite à la [Partie 1](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-1), donc si vous ne l'avez pas encore lue, il est recommandé de commencer par l'article précédent.

## 4. Configuration du runtime de conteneur
### 4-1. Exécution de la commande `nvidia-ctk`
```bash
sudo nvidia-ctk runtime configure --runtime=docker
```
Cette commande modifie le fichier `/etc/docker/daemon.json`{: .filepath} pour permettre à Docker d'utiliser le NVIDIA Container Runtime.

### 4-2. Redémarrage du démon Docker
Redémarrez le démon Docker pour appliquer les modifications de configuration.
```bash
sudo systemctl restart docker
```

### 4-3. Vérification de la configuration correcte
Exécutez un conteneur CUDA d'exemple.
```bash
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
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
Nous écrivons un Dockerfile à utiliser comme environnement de développement basé sur les images CUDA et cuDNN fournies par le [dépôt nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub.

- Il faut décider de l'image à utiliser en tenant compte des versions CUDA et cuDNN nécessaires, du type et de la version de distribution Linux, etc. 
- ![Version CUDA prise en charge par PyTorch 2.4.0](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/PyTorch_CUDA_version.png)Au moment de la rédaction de cet article, fin août 2024, la dernière version de PyTorch, la version 2.4.0, prend en charge CUDA 12.4. Par conséquent, nous utilisons ici l'image [12.4.1-cudnn-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/12.4.1-cudnn-devel-ubuntu22.04/images/sha256-0a434eff1826693c1e2a669b20062f9995e73ed3456cdb70416d7ba9c1e3d1f5?context=explore). Vous pouvez vérifier la dernière version de PyTorch et la version CUDA prise en charge sur le [site web de PyTorch](https://pytorch.org/get-started/locally/).

Le code source du Dockerfile complet est disponible publiquement dans le dépôt GitHub [yunseo-kim/dl-env-docker](https://github.com/yunseo-kim/dl-env-docker). Ci-dessous, nous expliquons étape par étape le processus de rédaction de ce Dockerfile.

### 5-1. Spécification de l'image de base
```Dockerfile
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04
```

### 5-2. Installation des utilitaires de base et des prérequis Python
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

### 5-3. Configuration du fuseau horaire du système (dans cet article, nous procédons avec 'Asia/Seoul')
```Dockerfile
# Set up time zone
ARG TZ="Asia/Seoul"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

### 5-4. Configuration du serveur SSH pour l'accès à distance  
Pour des raisons de sécurité, configurez de manière à ce que la connexion au compte root ne soit pas possible par mot de passe lors de la connexion SSH à distance.
```Dockerfile
# Disable root access via password
RUN echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config
```
Configurez pour que le service SSH démarre automatiquement au démarrage du conteneur.
```Dockerfile
RUN echo "sudo service ssh start > /dev/null" >> $HOME/.bashrc
```
Créez un utilisateur non-root nommé 'remote' à utiliser lors de la connexion SSH.
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

> Si aucune option n'est spécifiée lors de la construction de l'image Docker à l'aide de ce Dockerfile, la valeur initiale du mot de passe du compte utilisateur 'remote' est 000000. Ceci est très vulnérable en termes de sécurité, donc lors de la construction de l'image Docker, utilisez l'option `--build-arg` pour spécifier séparément le mot de passe de connexion au compte, ou changez immédiatement les paramètres après avoir exécuté le conteneur pour la première fois. Pour la sécurité, il est souhaitable de désactiver ultérieurement la connexion par mot de passe lors de la connexion SSH et de configurer pour que la connexion ne soit possible que via un fichier de clé séparé, et il serait idéal d'utiliser également une clé matérielle comme Yubikey.
> La configuration du serveur SSH sera abordée dans une certaine mesure dans la prochaine partie de cette série, et si vous voulez en savoir plus, vous pouvez consulter les documents de la liste suivante.
> - <https://help.ubuntu.com/community/SSH/OpenSSH/Configuring>
> - <https://documentation.ubuntu.com/server/how-to/security/openssh-server/>
> - <https://hostman.com/tutorials/how-to-install-and-configure-ssh-on-an-ubuntu-server/>
> - <https://developers.yubico.com/SSH/>
{: .prompt-danger }

### 5-5. Installation de setuptools, pip et enregistrement de la variable d'environnement PATH
```Dockerfile
RUN python3 -m pip install -U setuptools pip
ENV PATH="$HOME/.local/bin:$PATH"
```

### 5-6. Installation des packages d'apprentissage automatique et d'apprentissage profond à utiliser dans l'environnement de développement
```Dockerfile
RUN python3 -m pip install -U jupyterlab numpy scipy pandas matplotlib seaborn[stats] scikit-learn tqdm
RUN python3 -m pip install -U torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
Si vous voulez utiliser Cupy, cuDF, cuML et DALI, ajoutez également le contenu suivant au Dockerfile.
```Dockerfile
RUN python3 -m pip install -U cupy-cuda12x
RUN python3 -m pip install -U --extra-index-url=https://pypi.nvidia.com cudf-cu12==24.8.* cuml-cu12==24.8.* nvidia-dali-cuda120
```

### 5-7. Configuration pour exécuter JupyterLab au démarrage du conteneur
```Dockerfile
CMD cd $HOME/workspace && \
    jupyter lab --no-browser --autoreload --ip=0.0.0.0 --notebook-dir="$HOME/workspace"
```

## 6. Construction de l'image Docker et exécution du conteneur
### 6-1. Construction de l'image
Ouvrez un terminal dans le répertoire où se trouve le Dockerfile et exécutez la commande suivante.
```bash
docker build -t dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04 -f ./Dockerfile . \
--build-arg USER_PASSWORD=<password>
```
> À la place de \<password\>, entrez le mot de passe de connexion à utiliser lors de la connexion SSH.
{: .prompt-info }

### 6-2. Exécution d'une charge de travail d'exemple
Une fois la construction terminée, vérifiez si cela fonctionne bien en exécutant un conteneur jetable avec la commande suivante.
```bash
docker run -itd --rm --name test-container \
--gpus all -p 88:8888 \
dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04
```
Lorsque vous entrez la commande ci-dessus dans le terminal, elle exécute un conteneur nommé `test-container` à partir de l'image `dl-env:cuda12.4.1-cudnn9.1.0-ubuntu22.04` précédemment construite, puis connecte le port 88 du système hôte au port 8888 de ce conteneur. Si l'image Docker a été correctement construite à l'étape précédente et que le conteneur a démarré sans problème, JupyterLab devrait être en cours d'exécution à l'adresse par défaut `http:127.0.0.1:8888` dans le conteneur `test-container`. Par conséquent, lorsque vous ouvrez un navigateur sur le système hôte où fonctionne le Docker Engine et accédez à <http://127.0.0.1:88>, il devrait se connecter à l'adresse `http://127.0.0.1:8888` à l'intérieur du conteneur et afficher un écran comme ci-dessous.

![Capture d'écran de l'interface JupyterLab](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/Jupyter_Server.png)

### 6-3. (optionnel) Push vers Docker Hub
Pour pouvoir utiliser l'image de l'environnement de développement créée à travers le processus précédent en la tirant (Pull) à tout moment lorsque nécessaire, il est bon de la pousser (Push) sur Docker Hub.  

> Pour pousser votre propre image sur Docker Hub, vous avez besoin de votre propre compte Docker, donc si vous n'en avez pas encore, complétez d'abord l'inscription sur <https://app.docker.com/signup>.
{: .prompt-tip }

Tout d'abord, connectez-vous à Docker Hub avec la commande suivante.
```bash
docker login
```
Maintenant, exécutez une commande au format suivant pour créer un tag d'image.
```bash
docker tag IMAGE_ID <dockerhub_username>/<repository_name>[:TAG]
```
Enfin, exécutez la commande suivante pour pousser cette image sur Docker Hub.
```bash
docker push <dockerhub_username>/<repository_name>[:TAG]
```
Vous pouvez vérifier sur <https://hub.docker.com/> que le Push a bien été effectué comme ci-dessous.  
![Capture d'écran de Docker Hub](/assets/img/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker/yunseokim_dl-env-docker-hub.png)

L'image complétée à travers le processus précédent a été rendue publique dans le dépôt public [yunseokim/dl-env](https://hub.docker.com/r/yunseokim/dl-env/tags) sur Docker Hub, et peut être utilisée librement par quiconque.
