---
title: Construire un environnement de développement pour le deep learning avec NVIDIA Container Toolkit et Docker/Podman (1) - Installation de NVIDIA Container Toolkit et du moteur de conteneurs
description: Cette série explique comment configurer un environnement de développement d'apprentissage profond basé sur des conteneurs avec NVIDIA Container Toolkit, et comment configurer SSH et Jupyter Lab pour l'utiliser comme serveur distant. Ce billet est le premier de la série et présente l'installation de NVIDIA Container Toolkit et du moteur de conteneurs.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Aperçu
Cette série couvre le processus d'installation de NVIDIA Container Toolkit et Docker ou Podman, et la création d'un environnement de développement d'apprentissage profond en écrivant un Dockerfile basé sur les images CUDA et cuDNN fournies par le [dépôt nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub. Je partage le [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) et [l'image](https://hub.docker.com/r/yunseokim/dl-env/tags) complétés via GitHub et Docker Hub pour que ceux qui en ont besoin puissent les utiliser librement, et je fournis également un guide de configuration SSH et Jupyter Lab pour l'utilisation comme serveur distant.  
La série se composera de 3 articles, et celui-ci est le premier de la série.
- Partie 1 : Installation de NVIDIA Container Toolkit et du moteur de conteneurs (cet article)
- [Partie 2 : Configuration du runtime de conteneur pour l'utilisation du GPU, rédaction du Dockerfile et construction de l'image de conteneur](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Partie 3 (à venir)

Je suppose que vous utilisez un système Linux x86_64 avec une carte graphique NVIDIA compatible CUDA, et bien que je n'aie pas testé personnellement sur des distributions autres qu'Ubuntu ou Fedora, certains détails peuvent légèrement différer.  
(Mis à jour le 18.02.12025)

### Configuration de l'environnement de développement
- Système d'exploitation hôte et architecture : x86_64, environnement Linux (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Pile technologique à construire (langages et bibliothèques)
  - Python 3
  - NVIDIA Container Toolkit
  - Docker CE / Podman
  - CUDA 12.4
  - cuDNN
  - OpenSSH
  - tmux
  - JupyterLab
  - NumPy & SciPy
  - CuPy (optionnel, bibliothèque de tableaux compatible NumPy/SciPy pour le calcul GPU accéléré avec Python)
  - pandas
  - cuDF (optionnel, pour accélérer pandas avec le GPU sans modification de code)
  - Matplotlib & Seaborn
  - DALI (optionnel, alternative haute performance aux chargeurs de données intégrés utilisant le GPU)
  - scikit-learn
  - cuML (optionnel, pour exécuter des algorithmes d'apprentissage automatique sur GPU avec une API similaire à scikit-learn)
  - PyTorch
  - tqdm

  > Selon votre situation et vos préférences, vous pourriez envisager d'utiliser la bibliothèque DataFrame [Polars](https://pola.rs/) au lieu de pandas. Écrite en Rust, elle [offre des performances nettement supérieures à pandas pur, bien qu'inférieures à la combinaison cuDF + pandas pour le traitement de grands volumes de données](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), et propose une syntaxe plus spécialisée pour les requêtes. Selon le [blog officiel de Polars](https://pola.rs/posts/polars-on-gpu/), ils prévoient de collaborer avec l'équipe NVIDIA RAPIDS pour prendre en charge l'intégration avec cuDF dans un avenir proche.
  {: .prompt-tip }

  > Si vous hésitez entre Docker CE et Podman, le [tableau comparatif ci-dessous](#3-installation-du-moteur-de-conteneurs) pourrait vous aider.
  {: .prompt-tip }

### Tableau comparatif avec le guide précédent de configuration d'environnement d'apprentissage automatique
Un [guide précédent de configuration d'environnement d'apprentissage automatique](/posts/Setting-up-a-Machine-Learning-Development-Environment) existe déjà sur ce blog et reste largement valide, mais j'ai créé ce nouveau billet pour refléter certains changements. Les différences sont résumées dans le tableau ci-dessous.

| Différence | Article précédent (version 12021) | Cet article (version 12024) |
| --- | --- | --- |
| Distribution Linux | Basé sur Ubuntu | Applicable à Ubuntu, Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Méthode de configuration | Environnement virtuel Python avec venv | Environnement basé sur conteneurs avec<br> [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Installation du pilote graphique NVIDIA | O | O |
| Installation directe de CUDA et cuDNN<br> sur le système hôte | O (utilisant le gestionnaire de paquets Apt) | X (utilisant des [images préinstallées fournies par NVIDIA<br> sur Docker Hub](https://hub.docker.com/r/nvidia/cuda), donc pas besoin d'installation directe) |
| Portabilité | Nécessite de reconstruire l'environnement<br> à chaque migration vers un nouveau système | Basé sur Docker, donc facile de construire une nouvelle<br> image avec le Dockerfile existant ou de porter<br> une image existante (hors volumes et<br> configurations réseau supplémentaires) |
| Utilisation de bibliothèques<br> d'accélération GPU<br> supplémentaires à cuDNN | X | Introduction de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interface Jupyter Notebook | Jupyter Notebook (classique) | JupyterLab (nouvelle génération) |
| Configuration du serveur SSH | Non traitée | Configuration de base du serveur SSH incluse dans la partie 3 |

Si vous préférez utiliser un environnement virtuel Python comme venv plutôt que Docker, l'[article précédent](/posts/Setting-up-a-Machine-Learning-Development-Environment) reste valide et peut être consulté.

## 0. Vérifications préalables
- [NVIDIA Container Toolkit est disponible sur les distributions Linux prenant en charge les gestionnaires de paquets Apt, Yum ou Dnf, Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Vous pouvez consulter la liste des distributions Linux prises en charge sur la page liée. Bien que non explicitement mentionné dans le tableau de support officiel, Fedora, étant basé sur Red Hat Linux comme RHEL, est également compatible. Si vous n'êtes pas familier avec Linux et ne savez pas quelle distribution choisir, Ubuntu LTS est généralement le choix le plus sûr. Il installe automatiquement les pilotes propriétaires, ce qui le rend relativement facile à utiliser pour les débutants, et sa large base d'utilisateurs signifie que la plupart de la documentation technique est écrite pour Ubuntu.
  - Vous pouvez vérifier l'architecture de votre système et la version de votre distribution Linux en exécutant `uname -m && cat /etc/*release` dans le terminal.
- Vérifiez d'abord que votre carte graphique prend en charge les versions CUDA et cuDNN que vous souhaitez utiliser.
  - Vous pouvez vérifier le modèle de GPU installé dans votre ordinateur en exécutant `lspci | grep -i nvidia` dans le terminal.
  - Consultez <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html> pour vérifier les **versions de pilotes NVIDIA prises en charge**, les exigences de **CUDA Compute Capability**, et la liste des **matériels NVIDIA pris en charge** pour chaque version de cuDNN.
  - Trouvez votre modèle de GPU dans la liste à <https://developer.nvidia.com/cuda-gpus> et vérifiez sa valeur de **Compute Capability**. Cette valeur doit répondre aux exigences de **CUDA Compute Capability** vérifiées précédemment pour utiliser CUDA et cuDNN sans problème.

> Si vous prévoyez d'acheter une nouvelle carte graphique pour l'apprentissage profond, les critères de sélection sont bien résumés dans l'article suivant, régulièrement mis à jour par l'auteur.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> L'article [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) du même auteur est également très instructif.
{: .prompt-tip }

Si vous remplissez toutes les conditions mentionnées ci-dessus, commençons à configurer l'environnement de travail.

## 1. Installation du pilote graphique NVIDIA
Tout d'abord, vous devez installer le pilote graphique NVIDIA sur votre système hôte. Vous pouvez télécharger et utiliser l'installateur .run depuis la [page de téléchargement des pilotes NVIDIA](https://www.nvidia.com/drivers/), mais il est préférable d'utiliser le gestionnaire de paquets de votre système pour faciliter la gestion des versions et la maintenance. Consultez la documentation officielle <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> et installez le pilote graphique adapté à votre environnement système.

### Module propriétaire vs module open-source
Les pilotes Linux NVIDIA sont composés de plusieurs modules noyau, et depuis la version 515 et les versions ultérieures, NVIDIA propose deux types de modules noyau pour les pilotes.

- Propriétaire : Le pilote logiciel propriétaire que NVIDIA a fourni traditionnellement.
- Open-source : Pilote open-source fourni sous double licence MIT/GPLv2. Le code source est disponible via <https://github.com/NVIDIA/open-gpu-kernel-modules>.

Le pilote propriétaire est fourni pour les GPU basés sur les architectures de Maxwell à pré-Blackwell, et sera abandonné à partir de l'architecture Blackwell.
En revanche, le pilote open-source est pris en charge pour les architectures Turing et ultérieures.

[NVIDIA recommande d'utiliser le module noyau open-source lorsque c'est possible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)
Vous pouvez vérifier si votre GPU est compatible avec le pilote open-source sur [ce lien](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

Dans cet article, nous supposons que vous installez le pilote open-source.

### Debian & Ubuntu
Pour Ubuntu ou Debian, entrez les commandes suivantes dans le terminal pour l'installation.
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Pour Fedora 40, nous présentons la méthode d'installation utilisant les paquets précompilés fournis par [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuration du dépôt RPM Fusion  
Suivez le [guide officiel de RPM Fusion](https://rpmfusion.org/Configuration).  
Exécutez la commande suivante dans le terminal.
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Installation du paquet akmod-nvidia-open  
En vous référant au [guide d'installation des pilotes NVIDIA de RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), 
activez le dépôt rpmfusion-nonfree-tainted puis installez le paquet akmod-nvidia-open.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Enregistrement de la clé pour le chargement normal du pilote avec Secure Boot  

> En suivant la procédure supplémentaire décrite ci-dessous, vous pouvez utiliser normalement le pilote graphique NVIDIA tout en conservant la fonction Secure Boot. La désactivation de Secure Boot rend votre système considérablement vulnérable, il est donc recommandé de ne pas le désactiver. Au moins depuis les années 12020, il n'y a généralement pas de raison de désactiver Secure Boot.
{: .prompt-danger }

Tout d'abord, installez les outils suivants.
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Ensuite, exécutez la commande suivante pour générer une clé.
```bash
sudo kmodgenca -a
```
Maintenant, vous devez enregistrer la clé générée dans le MOK du firmware UEFI.
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Lorsque vous exécutez cette commande, vous serez invité à entrer un mot de passe pour l'enregistrement de la clé. Vous allez redémarrer bientôt pour terminer la procédure d'enregistrement de la clé, alors entrez un mot de passe à usage unique que vous pourrez facilement mémoriser.

Maintenant, exécutez la commande suivante pour redémarrer le système.
```bash
systemctl reboot
```
Pendant le démarrage du système, la fenêtre de gestion MOK apparaîtra automatiquement. Sélectionnez "Enroll MOK", puis "Continue", puis "Yes", et une fenêtre vous demandera le mot de passe que vous avez défini précédemment. Après avoir entré le mot de passe, la procédure d'enregistrement de la clé sera terminée. Maintenant, entrez reboot pour redémarrer et le pilote NVIDIA se chargera normalement.

### Vérification de l'installation du pilote NVIDIA
Vous pouvez vérifier le module noyau NVIDIA actuellement chargé en exécutant la commande suivante dans le terminal.
```bash
cat /proc/driver/nvidia/version
```
Si un message similaire à celui ci-dessous s'affiche, l'installation est réussie.
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Installation de NVIDIA Container Toolkit
Maintenant, vous devez installer [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Suivez le [guide d'installation officiel de NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), mais pour Fedora, il y a des points à noter, alors veuillez lire cette section jusqu'à la fin avant de procéder.

### Pour les utilisateurs d'Apt (Ubuntu, Debian, etc.)
#### 2-Apt-1. Configuration du dépôt pour le téléchargement des paquets
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Mise à jour de la liste des paquets
```bash
sudo apt update
```

#### 2-Apt-3. Installation du paquet
```bash
sudo apt install nvidia-container-toolkit
```

### Pour les utilisateurs de Yum ou Dnf (Fedora, RHEL, Centos, etc.)
> Lors des tests sur Fedora 40, contrairement à Ubuntu, les commandes `nvidia-smi` et le paquet `nvidia-persistenced` n'étaient pas inclus par défaut dans le pilote graphique NVIDIA, nécessitant l'installation supplémentaire du paquet `xorg-x11-drv-nvidia-cuda`. Je n'ai pas testé directement sur RHEL et Centos, mais comme leur configuration système est très similaire à Fedora, si vous rencontrez des problèmes en suivant ce guide, essayer la même méthode pourrait être utile.
{: .prompt-warning }

> Sur Fedora 40, après avoir installé `xorg-x11-drv-nvidia-cuda` comme indiqué ci-dessus et testé avec une charge de travail exemple, tout fonctionnait normalement sur mon système. Si vous rencontrez toujours des problèmes, peut-être en raison de SELinux, le [paquet nvidia-container-toolkit spécifique à Fedora et le guide fourni par le groupe AI-ML de Fedora](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) pourraient être utiles.
{: .prompt-tip }

#### 2-Dnf-1. Configuration du dépôt pour le téléchargement des paquets
```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Installation du paquet
```bash
sudo dnf install nvidia-container-toolkit
```
ou
```bash
sudo yum install nvidia-container-toolkit
```

### Pour les utilisateurs de Zypper (openSUSE, SLES)
#### 2-Zypper-1. Configuration du dépôt pour le téléchargement des paquets
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Installation du paquet
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installation du moteur de conteneurs
Ensuite, installez Docker CE ou Podman comme moteur de conteneurs. Choisissez l'un des deux selon votre environnement et vos préférences, en vous référant à la [documentation officielle de Docker](https://docs.docker.com/engine/install/) et à la [documentation officielle de Podman](https://podman.io/docs/installation).

Le tableau suivant résume les principales différences et avantages/inconvénients de Docker et Podman.

| Critère | Docker | Podman |
| --- | --- | --- |
| Architecture | Modèle client-serveur, basé sur un démon | Structure sans démon (daemonless) |
| Sécurité | Dépend d'un démon exécuté par défaut avec<br> les privilèges root, présentant des risques<br> potentiels de sécurité (mode rootless supporté<br> depuis la version 20.10 de 12020, mais<br> nécessite une configuration supplémentaire) | Ne dépend pas d'un démon, fonctionne par<br> défaut en mode rootless sauf indication<br> contraire, et est protégé par SELinux |
| Utilisation des ressources | En raison de sa structure basée sur un démon,<br> des processus d'arrière-plan fonctionnent en<br> permanence, utilisant généralement plus<br> de ressources | Généralement moins de frais généraux<br> (overhead) de ressources |
| Temps de démarrage<br> des conteneurs | Relativement lent | Jusqu'à 50% plus rapide grâce à une<br> architecture simplifiée |
| Écosystème et<br> documentation | Vaste écosystème et support communautaire,<br> documentation abondante | Écosystème et documentation<br> relativement plus limités |
| Réseau | Utilise Docker Bridge Network | Utilise les plugins CNI<br> (Container Network Interface) |
| Support natif des<br> YAML Kubernetes | X (conversion nécessaire) | O |

Références :
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker a une histoire plus longue et a joui d'un statut de standard de facto dans l'industrie, son principal avantage étant son vaste écosystème et sa riche documentation.  
Podman a été développé relativement récemment par Red Hat, et avec sa structure avancée visant nativement le daemonless et le rootless, il présente des avantages en termes de sécurité, d'utilisation des ressources système et de temps de démarrage des conteneurs. Contrairement à Docker, où tous les conteneurs tombent en panne si le démon rencontre un problème, chaque conteneur Podman est complètement indépendant, ce qui signifie que la panne d'un conteneur n'affecte pas les autres.

Il est important de choisir l'outil qui convient le mieux à votre situation, et pour un utilisateur individuel débutant, Podman pourrait être un bon choix. Bien que son écosystème soit relativement plus petit que celui de Docker, il comble rapidement l'écart grâce à ses nombreux avantages, et comme il est compatible avec la syntaxe Dockerfile, les images Docker et l'interface CLI, ce ne devrait pas être un problème pour les individus ou les petits groupes.

### Podman
Il est facilement installable car il est pris en charge par les dépôts système par défaut de la plupart des principales distributions Linux.

#### Pour Ubuntu
```bash
sudo apt install podman
```

#### Pour Fedora
```bash
sudo dnf install podman
```

#### Pour openSUSE
```bash
sudo zypper install podman
```

### Docker CE
#### Pour Ubuntu
##### 3-Ubuntu-1. Suppression des versions précédentes ou des paquets non officiels pour éviter les conflits
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configuration du dépôt
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

##### 3-Ubuntu-3. Installation des paquets
```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Création du groupe `Docker` et ajout de l'utilisateur
Pour permettre aux utilisateurs non-root de gérer Docker sans `sudo`, créez un groupe `Docker` puis ajoutez-y les utilisateurs qui souhaitent utiliser Docker. Exécutez les commandes suivantes dans le terminal.
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Déconnectez-vous puis reconnectez-vous pour appliquer les changements. Sur Ubuntu ou Debian, le service Docker démarre automatiquement à chaque démarrage du système sans configuration supplémentaire.

#### Pour Fedora
##### 3-Fedora-1. Suppression des versions précédentes ou des paquets non officiels pour éviter les conflits
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

##### 3-Fedora-2. Configuration du dépôt
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Installation des paquets
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Pendant l'installation, vous serez invité à approuver une clé GPG. Si la clé GPG correspond à `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, entrez y pour approuver.  
> Si la clé GPG ne correspond pas, vous pourriez avoir téléchargé un paquet falsifié par une attaque de la chaîne d'approvisionnement et devriez interrompre l'installation.
{: .prompt-danger }

##### 3-Fedora-4. Démarrage du démon Docker
Docker est maintenant installé mais pas encore en cours d'exécution. Exécutez la commande suivante pour démarrer Docker.
```bash
sudo systemctl start docker
```
Pour que le service Docker démarre automatiquement au démarrage du système, exécutez les commandes suivantes.
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Ajout de l'utilisateur au groupe `Docker`
Pour permettre aux utilisateurs non-root de gérer Docker, ajoutez-les au groupe `Docker`. Sur Fedora, le groupe `Docker` est automatiquement créé lors de l'installation des paquets, donc vous n'avez qu'à ajouter l'utilisateur.
```bash
sudo usermod -aG docker $USER
```
Déconnectez-vous puis reconnectez-vous pour appliquer les changements.

#### Vérification de la configuration
Exécutez la commande suivante dans le terminal.
```bash
docker run hello-world
```
Si vous voyez un message similaire à celui ci-dessous, c'est un succès.

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

## Pour aller plus loin
Suite dans la [Partie 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
