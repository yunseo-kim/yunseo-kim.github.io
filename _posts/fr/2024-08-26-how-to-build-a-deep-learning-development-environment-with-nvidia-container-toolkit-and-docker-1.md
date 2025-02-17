---
title: Construire un environnement de développement pour l'apprentissage profond avec NVIDIA Container Toolkit et Docker/Podman (1) - Installation de NVIDIA Container Toolkit et du moteur de conteneurs
description: Cette série traite de la mise en place d'un environnement de développement pour l'apprentissage profond basé sur des conteneurs en utilisant NVIDIA Container Toolkit localement, et de la configuration de SSH et Jupyter Lab pour l'utiliser comme serveur distant. Ce post est le premier article de la série, introduisant les méthodes d'installation de NVIDIA Container Toolkit et du moteur de conteneurs.
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.jpg
---
## Aperçu
Cette série couvre le processus d'installation de NVIDIA Container Toolkit et Docker ou Podman, et la création d'un environnement de développement pour l'apprentissage profond en écrivant un Dockerfile basé sur les images CUDA et cuDNN fournies par le [référentiel nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub. Pour ceux qui en ont besoin, le [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) et [l'image](https://hub.docker.com/r/yunseokim/dl-env/tags) complétés à travers ce processus sont partagés via GitHub et Docker Hub pour une utilisation libre, et un guide de configuration SSH et Jupyter Lab est également fourni pour une utilisation comme serveur distant.  
La série sera composée de 3 articles, et celui que vous lisez est le premier article de cette série.
- Partie 1 : Installation de NVIDIA Container Toolkit et du moteur de conteneurs (cet article)
- [Partie 2 : Configuration du runtime de conteneur pour l'utilisation du GPU, écriture du Dockerfile et construction de l'image de conteneur](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Partie 3 (à venir)

Nous supposons un système équipé d'une carte graphique NVIDIA prenant en charge CUDA dans un environnement Linux x86_64, et bien que certains détails puissent légèrement différer pour les distributions autres qu'Ubuntu ou Fedora, car ils n'ont pas été directement testés.  
(Mise à jour du contenu le 18.02.2025)

### Configuration de l'environnement de développement
- Système d'exploitation hôte et architecture : Environnement Linux x86_64 (Ubuntu 18.04/20.04/22.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
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
  - CuPy (optionnel, bibliothèque de tableaux compatible NumPy/SciPy pour le calcul accéléré par GPU avec Python)
  - pandas
  - cuDF (optionnel, pour accélérer pandas sans changement de code avec l'accélérateur GPU)
  - Matplotlib & Seaborn
  - DALI (optionnel, alternative haute performance aux chargeurs de données et itérateurs de données intégrés utilisant le GPU)
  - scikit-learn
  - cuML (optionnel, pour exécuter des algorithmes d'apprentissage automatique sur GPU avec une API qui suit de près l'API scikit-learn)
  - PyTorch
  - tqdm

  > Selon la situation et vos préférences personnelles, vous pouvez envisager d'utiliser la bibliothèque DataFrame [Polars](https://pola.rs/) au lieu de pandas. Écrite en Rust, elle offre des performances nettement supérieures à celles du package pandas pur [bien qu'elle soit dépassée par la combinaison cuDF + pandas lors du traitement de grands volumes de données](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/), et fournit une syntaxe plus spécialisée pour les requêtes. Selon [le blog officiel de Polars](https://pola.rs/posts/polars-on-gpu/), ils prévoient également de prendre en charge l'intégration avec cuDF dans un avenir proche en collaboration avec l'équipe NVIDIA RAPIDS.
  {: .prompt-tip }

  > Si vous hésitez entre Docker CE et Podman, [le tableau comparatif mentionné plus loin](#3-installation-du-moteur-de-conteneurs) pourrait vous être utile.
  {: .prompt-tip }

### Tableau comparatif avec le guide précédent de configuration d'environnement d'apprentissage automatique
Il existe déjà [un guide de configuration d'environnement d'apprentissage automatique précédemment publié sur ce blog](/posts/Setting-up-a-Machine-Learning-Development-Environment) qui reste en grande partie valide, mais il y a eu quelques changements, d'où la rédaction de ce nouveau post. Les différences sont résumées dans le tableau ci-dessous.

| Différence | Article précédent (version 2021) | Cet article (version 2024) |
| --- | --- | --- |
| Distribution Linux | Basé sur Ubuntu | Applicable à Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. en plus d'Ubuntu |
| Méthode de construction<br> de l'environnement | Environnement virtuel Python<br> utilisant venv | Environnement basé sur des conteneurs Docker<br> utilisant [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) |
| Installation du pilote<br> graphique NVIDIA | O | O |
| Installation directe de CUDA<br> et cuDNN sur le système hôte | O (utilisation du gestionnaire<br> de paquets Apt) | X (Utilisation d'images pré-installées fournies par<br> NVIDIA sur [Docker Hub](https://hub.docker.com/r/nvidia/cuda), donc pas besoin de travail direct) |
| Portabilité | Nécessité de reconstruire<br> l'environnement de développement<br> à chaque transfert vers un<br> autre système | Basé sur Docker, donc possibilité de construire<br> facilement une nouvelle image avec le Dockerfile<br> créé au besoin ou de porter facilement l'image<br> existante (à l'exception des volumes<br> supplémentaires ou des configurations réseau) |
| Utilisation de bibliothèques<br> d'accélération GPU<br> supplémentaires en plus<br> de cuDNN | X | Introduction de [CuPy](https://cupy.dev/), [cuDF](https://docs.rapids.ai/api/cudf/stable/), [cuML](https://docs.rapids.ai/api/cuml/stable/), [DALI](https://developer.nvidia.com/DALI) |
| Interface Jupyter Notebook | Jupyter Notebook (classique) | JupyterLab (nouvelle génération) |
| Configuration du serveur SSH | Non traité séparément | Inclut la configuration de base du serveur SSH<br> dans la partie 3 |

Si vous souhaitez utiliser un environnement virtuel Python comme venv plutôt que Docker, [l'article précédent](/posts/Setting-up-a-Machine-Learning-Development-Environment) est toujours valable, donc je recommande de s'y référer.

## 0. Vérifications préalables
- [NVIDIA Container Toolkit peut être utilisé sur les distributions Linux prenant en charge les gestionnaires de paquets Apt, Yum ou Dnf, Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) Vous pouvez vérifier la liste des distributions Linux prises en charge sur la page liée, et bien que Fedora ne soit pas spécifiquement mentionné dans le tableau de support officiel, il peut être utilisé sans problème car il est basé sur Red Hat Linux comme RHEL. Si vous n'êtes pas familier avec l'environnement Linux et ne savez pas quelle distribution utiliser, la version LTS d'Ubuntu est la plus sûre. Elle est relativement facile à utiliser pour les débutants car les pilotes propriétaires sont également installés automatiquement, et la plupart des documents techniques sont rédigés sur la base d'Ubuntu en raison du grand nombre d'utilisateurs.
  - Vous pouvez vérifier l'architecture de votre système et la version de la distribution Linux que vous utilisez avec la commande `uname -m && cat /etc/*release` dans le terminal.
- Vous devez d'abord vérifier si la carte graphique installée dans votre système prend en charge les versions de CUDA et cuDNN que vous souhaitez utiliser.
  - Vous pouvez vérifier le nom du modèle GPU installé dans votre ordinateur actuel avec la commande `lspci | grep -i nvidia` dans le terminal.
  - Sur la page <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, vérifiez la **version du pilote graphique NVIDIA prise en charge** par version de cuDNN, les conditions requises de **CUDA Compute Capability**, et la liste du **matériel NVIDIA pris en charge**.
  - Trouvez le nom du modèle correspondant dans la liste des GPU sur <https://developer.nvidia.com/cuda-gpus>, puis vérifiez la valeur **Compute Capability**. Cette valeur doit satisfaire les conditions de **CUDA Compute Capability** vérifiées précédemment pour pouvoir utiliser CUDA et cuDNN sans problème.

> Si vous prévoyez d'acheter une nouvelle carte graphique pour les tâches d'apprentissage profond, les critères de sélection du GPU sont bien résumés dans l'article suivant. L'auteur met continuellement à jour cet article.  
> [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)  
> L'article [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) écrit par la même personne est également très instructif.
{: .prompt-tip }

Si vous remplissez toutes les conditions mentionnées ci-dessus, commençons à construire l'environnement de travail.

## 1. Installation du pilote graphique NVIDIA
Tout d'abord, vous devez installer le pilote graphique NVIDIA sur le système hôte. Vous pouvez télécharger et utiliser l'installateur .run depuis la [page de téléchargement des pilotes NVIDIA](https://www.nvidia.com/drivers/), mais il est préférable d'utiliser le gestionnaire de paquets de votre système pour l'installation, ce qui est meilleur en termes de gestion des versions et de maintenance. Référez-vous à la documentation officielle <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> pour installer le pilote graphique adapté à votre environnement système.

### Module propriétaire vs Module open-source
Le pilote Linux NVIDIA est composé de plusieurs modules noyau, et à partir du pilote version 515 et des versions ultérieures, NVIDIA fournit deux types de modules noyau pour les pilotes.

- Propriétaire : Le pilote logiciel propriétaire que NVIDIA a fourni jusqu'à présent.
- Open-source : Pilote open-source fourni sous double licence MIT/GPLv2. Le code source est publié via <https://github.com/NVIDIA/open-gpu-kernel-modules>.

Le pilote propriétaire est fourni pour les GPU basés sur les architectures de Maxwell à Blackwell, et sera abandonné à partir de l'architecture Blackwell.
En revanche, le pilote open-source est pris en charge pour les architectures Turing et ultérieures.

[NVIDIA recommande d'utiliser le module noyau open-source si possible.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html) 
Vous pouvez vérifier si votre GPU est compatible avec le pilote open-source sur [ce lien](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

Dans cet article, nous supposons que nous installons le pilote open-source.

### Debian & Ubuntu
Pour Ubuntu ou Debian, entrez les commandes suivantes dans le terminal pour l'installation :
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora
Basé sur Fedora 40, nous présentons la méthode d'installation en téléchargeant et installant le package pré-construit fourni par [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configuration du référentiel RPM Fusion  
Référez-vous au [guide officiel de RPM Fusion](https://rpmfusion.org/Configuration) pour procéder.  
Exécutez la commande suivante dans le terminal :
```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

#### 1-Fedora-2. Installation du package akmod-nvidia-open  
En vous référant au [guide d'installation du pilote NVIDIA fourni par RPM Fusion](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), 
activez le référentiel rpmfusion-nonfree-tainted, puis installez le package akmod-nvidia-open.
```bash
sudo dnf update --refresh
sudo dnf install rpmfusion-nonfree-release-tainted
sudo dnf install akmod-nvidia-open
sudo dnf mark install akmod-nvidia-open
```

#### 1-Fedora-3. Enregistrement de la clé pour le chargement normal du pilote lors du démarrage sécurisé (Secure Boot)  

> En suivant la procédure supplémentaire expliquée ci-dessous, vous pouvez utiliser normalement le pilote graphique NVIDIA tout en profitant de la fonction de démarrage sécurisé, et il est recommandé de ne pas la désactiver car la sécurité du système devient considérablement vulnérable lorsque le démarrage sécurisé est désactivé. Au moins depuis les années 2020, il n'y a pratiquement aucune raison de désactiver le démarrage sécurisé.
{: .prompt-danger }

Tout d'abord, installez les outils suivants :
```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Ensuite, exécutez la commande suivante pour générer une clé :
```bash
sudo kmodgenca -a
```
Maintenant, vous devez enregistrer la clé générée dans le MOK du firmware UEFI.
```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```
Lorsque vous exécutez cette commande, il vous sera demandé d'entrer un mot de passe pour l'enregistrement de la clé. C'est un mot de passe à usage unique que vous utiliserez pour terminer la procédure d'enregistrement de la clé lors du redémarrage dans un instant, alors entrez quelque chose dont vous pouvez vous souvenir facilement.

Maintenant, exécutez la commande suivante pour redémarrer le système :
```bash
systemctl reboot
```
Pendant le démarrage du système, la fenêtre de gestion MOK apparaîtra automatiquement. Sélectionnez "Enroll MOK", puis sélectionnez successivement "Continue" et "Yes", et une fenêtre demandant le mot de passe que vous avez défini précédemment apparaîtra. Une fois que vous aurez entré le mot de passe que vous avez défini précédemment, la procédure d'enregistrement de la clé sera terminée. Maintenant, entrez reboot pour redémarrer et le pilote NVIDIA devrait se charger normalement.

### Vérification de l'installation du pilote NVIDIA
Vous pouvez vérifier le module noyau NVIDIA actuellement chargé en exécutant la commande suivante dans le terminal :
```bash
cat /proc/driver/nvidia/version
```
Si un message similaire à celui ci-dessous s'affiche, l'installation est réussie :
```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

## 2. Installation de NVIDIA Container Toolkit
Maintenant, vous devez installer [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Suivez l'installation en vous référant au [guide d'installation officiel de NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html), mais pour Fedora, il y a des points à noter lors de l'installation, donc veuillez vérifier le contenu de cette section jusqu'à la fin avant de procéder.

### Pour ceux qui utilisent Apt (Ubuntu, Debian, etc.)
#### 2-Apt-1. Configuration du référentiel pour le téléchargement des paquets
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

### Pour ceux qui utilisent Yum ou Dnf (Fedora, RHEL, Centos, etc.)
> Lors des tests sur Fedora 40, contrairement à Ubuntu, la commande `nvidia-smi` et le paquet `nvidia-persistenced` n'étaient pas inclus par défaut dans le pilote graphique NVIDIA, donc il fallait installer le paquet `xorg-x11-drv-nvidia-cuda` en plus. Je n'ai pas testé directement sur RHEL et Centos, mais comme leur configuration système est très similaire à celle de Fedora, si vous rencontrez des problèmes en suivant le guide ci-dessous, essayer la même méthode pourrait être utile.
{: .prompt-warning }

> Sur Fedora 40, après avoir installé `xorg-x11-drv-nvidia-cuda` comme indiqué ci-dessus et exécuté une charge de travail d'exemple pour tester, cela fonctionnait normalement sur mon système. Si vous rencontrez toujours des problèmes, peut-être en raison de SELinux ou autre, le [paquet nvidia-container-toolkit spécifique à Fedora et le guide fourni par le groupe AI-ML de Fedora](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) pourraient être utiles.
{: .prompt-tip }

#### 2-Dnf-1. Configuration du référentiel pour le téléchargement des paquets
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

### Pour ceux qui utilisent Zypper (openSUSE, SLES)
#### 2-Zypper-1. Configuration du référentiel pour le téléchargement des paquets
```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Installation du paquet
```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installation du moteur de conteneurs
Ensuite, installez Docker CE ou Podman comme moteur de conteneurs. Vous pouvez choisir l'un des deux en fonction de votre environnement d'utilisation et de vos préférences, en vous référant à la [documentation officielle de Docker](https://docs.docker.com/engine/install/) et à la [documentation officielle de Podman](https://podman.io/docs/installation).

Le tableau suivant résume les principales différences et les avantages et inconvénients de Docker et Podman.

| Élément de comparaison | Docker | Podman |
| --- | --- | --- |
| Architecture | Modèle client-serveur, basé sur un démon | Structure sans démon (daemonless) |
| Sécurité | Risque potentiel de sécurité dû à la dépendance<br> à un démon s'exécutant par défaut avec les<br> privilèges root (Le mode rootless est pris en<br> charge depuis la version 20.10 publiée en 2020,<br> mais nécessite une configuration supplémentaire) | Fonctionne par défaut en mode rootless sans<br> dépendre d'un démon, sauf indication contraire,<br> et est protégé par SELinux |
| Utilisation des ressources | En raison de la nature de l'architecture basée<br> sur un démon, un processus d'arrière-plan<br> fonctionne en permanence, utilisant<br> généralement plus de ressources | Généralement moins de frais généraux de ressources |
| Temps de démarrage<br> des conteneurs | Relativement lent | Jusqu'à 50% plus rapide grâce à une<br> architecture simplifiée |
| Écosystème et<br> documentation | Vaste écosystème et support communautaire,<br> documentation abondante | Écosystème et documentation relativement<br> plus petits |
| Mise en réseau | Utilise Docker Bridge Network | Utilise les plugins CNI (Container Network Interface) |
| Prise en charge native<br> de Kubernetes YAML | X (nécessite une conversion) | O |

Références :
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker a une histoire plus longue et a joui d'un statut de facto standard dans l'industrie, donc son plus grand avantage est l'existence d'un vaste écosystème et d'une documentation abondante.  
Podman a été développé relativement récemment par Red Hat, et en raison de sa structure avancée visant intrinsèquement le sans démon (daemonless) et le sans root (rootless), il présente des avantages à plusieurs égards, notamment en termes de sécurité, d'utilisation des ressources système et de temps de démarrage des conteneurs. Un autre avantage de Podman est que, contrairement à Docker où tous les conteneurs tombent en panne si le démon rencontre un problème, chaque conteneur est complètement indépendant, donc la panne d'un conteneur spécifique n'affecte pas les autres conteneurs.

Il est surtout important de choisir l'outil qui convient à vos conditions données, et pour un utilisateur individuel qui débute, commencer avec Podman pourrait être un bon choix. Bien que son écosystème soit relativement plus petit que celui de Docker, il comble rapidement l'écart grâce à ses nombreux avantages mentionnés ci-dessus, et comme il est compatible avec Docker dans de nombreux aspects tels que la syntaxe Dockerfile, les images Docker et l'interface en ligne de commande (CLI), cela ne devrait pas poser trop de problèmes pour les individus ou les petits groupes.

### Podman
Il peut être installé simplement car il est pris en charge dans les référentiels système par défaut de la plupart des principales distributions Linux.

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
##### 3-Ubuntu-1. Suppression des versions antérieures ou des paquets non officiels pour éviter les conflits de paquets
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configuration du référentiel
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
Pour permettre aux utilisateurs non-root de gérer Docker sans `sudo`, vous pouvez créer un groupe `Docker` puis y ajouter les utilisateurs qui souhaitent utiliser Docker. Exécutez les commandes suivantes dans le terminal :
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
Après cela, déconnectez-vous puis reconnectez-vous pour que les changements soient appliqués. Pour Ubuntu ou Debian, le service Docker démarre automatiquement à chaque démarrage du système sans aucune action supplémentaire.

#### Pour Fedora
##### 3-Fedora-1. Suppression des versions antérieures ou des paquets non officiels pour éviter les conflits de paquets
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

##### 3-Fedora-2. Configuration du référentiel
```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Installation des paquets
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Pendant le processus d'installation des paquets, une notification vous demandera si vous souhaitez approuver la clé GPG. Si la clé GPG correspond à `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, entrez y pour l'approuver.  
> Si la clé GPG ne correspond pas, vous pourriez avoir téléchargé un paquet contrefait suite à une attaque de la chaîne d'approvisionnement, et vous devez arrêter l'installation.
{: .prompt-danger }

##### 3-Fedora-4. Démarrage du démon Docker
Docker est maintenant installé mais pas en cours d'exécution, vous pouvez donc lancer Docker en entrant la commande suivante :
```bash
sudo systemctl start docker
```
Pour que le service Docker démarre automatiquement au démarrage du système, exécutez les commandes suivantes :
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Ajout de l'utilisateur au groupe `Docker`
Pour permettre aux utilisateurs non-root de gérer Docker, ajoutez les utilisateurs qui souhaitent utiliser Docker au groupe `Docker`. Dans le cas de Fedora, le groupe `Docker` est automatiquement créé lors du processus d'installation des paquets précédent, il suffit donc d'ajouter l'utilisateur.
```bash
sudo usermod -aG docker $USER
```
Après cela, déconnectez-vous puis reconnectez-vous pour que les changements soient appliqués.

#### Vérification que la configuration est correcte
Essayez d'exécuter la commande suivante dans le terminal :
```bash
docker run hello-world
```
Si un message similaire à celui ci-dessous s'affiche, c'est un succès.

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
