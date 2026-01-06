---
title: "Mettre en place un environnement de développement pour le deep learning avec NVIDIA Container Toolkit et Docker/Podman (1) - Installation de NVIDIA Container Toolkit et du moteur de conteneur"
description: "Cette série explique comment mettre en place en local un environnement de développement deep learning basé sur des conteneurs avec NVIDIA Container Toolkit, puis configurer SSH et JupyterLab pour l’utiliser comme serveur distant. Ce premier billet présente l’installation de NVIDIA Container Toolkit et du moteur de conteneur."
categories: [AI & Data, Machine Learning]
tags: [Development Environment, Docker, CUDA, PyTorch]
image: /assets/img/technology.webp
---

## Aperçu

Dans cette série, nous abordons l’installation de NVIDIA Container Toolkit et de Docker ou Podman, puis le processus de création d’un environnement de développement pour le deep learning en écrivant un Dockerfile basé sur les images CUDA et cuDNN fournies par le dépôt [nvidia/cuda](https://hub.docker.com/r/nvidia/cuda) sur Docker Hub. Pour ceux qui en ont besoin, je partage via GitHub et Docker Hub le [Dockerfile](https://github.com/yunseo-kim/dl-env-docker) et l’[image](https://hub.docker.com/r/yunseokim/dl-env/tags) finalisés au terme de ce processus, et je fournis en plus un guide de configuration de SSH et JupyterLab afin de pouvoir l’utiliser comme serveur distant.  
La série devrait se composer de 3 articles, et celui que vous lisez est le premier.
- Partie 1 : Installation de NVIDIA Container Toolkit et du moteur de conteneur (cet article)
- [Partie 2 : Configuration du runtime de conteneur pour l’utilisation du GPU, rédaction du Dockerfile et construction de l’image de conteneur](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
- Partie 3 (à venir)

Je pars du principe qu’il s’agit d’un système Linux x86_64 équipé d’une carte graphique NVIDIA prenant en charge CUDA. Je n’ai pas testé directement sur des distributions autres qu’Ubuntu ou Fedora, donc certains détails peuvent différer légèrement.  
(Révision : 12026.1.6.)

### Composition de l’environnement de développement

- Système hôte et architecture : x86_64, environnement Linux (Ubuntu 22.04/24.04 LTS, RHEL/Centos, Fedora, openSUSE/SLES 15.x, etc.)
- Stack technique (langages et bibliothèques)
  - [Python 3](https://www.python.org/)
  - [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
  - [Docker Engine](https://docs.docker.com/engine/) / [Podman](https://podman.io/)
  - CUDA 12.4 / 12.8 / 13.0
  - cuDNN 9
  - [OpenSSH](https://www.openssh.com/)
  - [tmux](https://github.com/tmux/tmux/wiki)
  - [JupyterLab](https://jupyter.org/)
  - [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
  - [CuPy](https://cupy.dev/) (optionnel, bibliothèque de tableaux compatible NumPy/SciPy pour le calcul accéléré GPU en Python)
  - [pandas](https://pandas.pydata.org/)
  - [cuDF](https://docs.rapids.ai/api/cudf/stable/) (optionnel, pour accélérer pandas sans modification de code avec l’accélérateur GPU)
  - [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
  - [cuxfilter](https://docs.rapids.ai/api/cuxfilter/stable/) (optionnel, pour visualiser et filtrer rapidement de grands jeux de données en quelques lignes de code, avec des bibliothèques de graphiques de premier plan)
  - [DALI](https://developer.nvidia.com/DALI) (optionnel, alternative haute performance aux data loaders/iterators intégrés, utilisant le GPU)
  - [scikit-image](https://scikit-image.org/)
  - [cuCIM](https://docs.rapids.ai/api/cucim/stable/) (optionnel, alternative accélérée pour le traitement d’images n-dimensionnelles et l’I/O d’images, à scikit-image)
  - [scikit-learn](https://scikit-learn.org/)
  - [XGBoost](https://xgboost.ai/)
  - [cuML](https://docs.rapids.ai/api/cuml/stable/) (optionnel, pour exécuter des algorithmes de machine learning sur GPU via une API proche de celle de scikit-learn)
  - [cuVS](https://docs.rapids.ai/api/cuvs/stable/) (optionnel, algorithmes optimisés pour voisins les plus proches approchés et clustering, et autres outils essentiels pour la recherche vectorielle accélérée)
  - [RAFT](https://docs.rapids.ai/api/raft/stable/) (optionnel, primitives accélérées CUDA utilisées par d’autres bibliothèques RAPIDS)
  - [PyTorch](https://pytorch.org/)
  - [cuGraph](https://docs.rapids.ai/api/cugraph/stable/) (optionnel, bibliothèque d’analytique de graphes accélérée GPU incluant un accélérateur « zero code change » pour NetworkX)
  - [tqdm](https://tqdm.github.io/)

  > Selon le contexte et vos préférences, vous pouvez envisager d’utiliser la bibliothèque DataFrame [Polars](https://pola.rs/) à la place de pandas. Elle est écrite en Rust et, [même si elle est moins performante que la combinaison cuDF + pandas sur de très gros volumes de données, elle offre des performances très élevées comparée au package pandas « natif »](https://docs.rapids.ai/api/cudf/stable/cudf_pandas/benchmarks/). Elle propose également une syntaxe davantage orientée requêtes. D’après le [blog officiel de Polars](https://pola.rs/posts/polars-on-gpu/) et la [documentation cuDF](https://docs.rapids.ai/api/cudf/stable/cudf_polars/), Polars et l’équipe NVIDIA RAPIDS collaborent pour fournir en bêta ouverte un moteur d’accélération GPU basé sur cuDF, et le développement progresse rapidement.
  {: .prompt-tip }

  > Si vous hésitez entre Docker CE et Podman, le [tableau comparatif ci-dessous](#3-installation-du-moteur-de-conteneur) peut vous aider.
  {: .prompt-tip }

### Tableau comparatif avec un guide précédent d’environnement ML

Il existe déjà un [guide d’environnement de développement machine learning publié auparavant sur ce blog](/posts/Setting-up-a-Machine-Learning-Development-Environment), mais j’ai rédigé ce billet en raison de nombreux changements. Les différences sont résumées dans le tableau ci-dessous.

| Différence | Ancien article (version 12021) | Cet article (rédigé en 12024, révisé en 12026) |
| --- | --- | --- |
| Distribution Linux | Basé sur Ubuntu | Applicable aussi à Fedora/RHEL/Centos,<br> Debian, openSUSE/SLES, etc. |
| Méthode de mise en place | Installation directe sur l’hôte<br>environnement virtuel Python via venv | Environnement basé sur des conteneurs Docker<br>via [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)<br> env virtuel Python et gestion de paquets via uv |
| Installation du pilote graphique NVIDIA | O | O |
| Installation directe de <br>CUDA et cuDNN sur l’hôte | O (via le gestionnaire de paquets Apt) | X (on utilise des [images préinstallées fournies par NVIDIA sur Docker Hub](https://hub.docker.com/r/nvidia/cuda), donc pas besoin d’installation manuelle) |
| Portabilité | À chaque migration vers un autre système,<br> il faut reconstruire l’environnement | Basé sur Docker : à partir du Dockerfile,<br> on peut reconstruire une nouvelle image au besoin,<br> ou migrer facilement une image existante (hors volumes/paramètres réseau additionnels) |
| Utilisation de bibliothèques <br>GPU au-delà de cuDNN | X | Introduction de [CuPy](https://cupy.dev/), [RAPIDS](https://rapids.ai/), [DALI](https://developer.nvidia.com/DALI) |
| Interface Jupyter Notebook | Jupyter Notebook (classic) | JupyterLab (Next-Generation) |
| Configuration du serveur SSH | Non abordé séparément | Inclut une configuration de base du serveur SSH |

## 0. Vérifications préalables

- [NVIDIA Container Toolkit peut être utilisé sur des distributions Linux prenant en charge les gestionnaires de paquets Apt, Yum/Dnf ou Zypper.](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/supported-platforms.html) La page liée liste les distributions prises en charge. Fedora n’est pas explicitement indiqué dans le tableau de support officiel, mais comme il s’agit aussi d’une distribution basée sur Red Hat Linux comme RHEL, vous pouvez l’utiliser sans problème. Si vous n’êtes pas à l’aise avec Linux et ne savez pas quelle distribution choisir, utiliser une version Ubuntu LTS est le choix le plus « sûr ». Les pilotes propriétaires (non open source) s’installent aussi automatiquement, c’est relativement pratique pour les débutants, et la plupart des documents techniques sont rédigés en prenant Ubuntu comme référence, car la base d’utilisateurs est grande.
  - Vous pouvez vérifier l’architecture et la version de la distribution Linux depuis un terminal avec `uname -m && cat /etc/*release`.
- Vous devez d’abord vérifier que la carte graphique installée sur le système prend en charge les versions de CUDA et cuDNN que vous souhaitez utiliser.
  - Le modèle de GPU installé sur votre machine peut être vérifié depuis un terminal avec `lspci | grep -i nvidia`.
  - Sur <https://docs.nvidia.com/deeplearning/cudnn/latest/reference/support-matrix.html>, vérifiez, pour chaque version de cuDNN, la **version de pilote graphique NVIDIA prise en charge** ainsi que les exigences de **CUDA Compute Capability**, et la liste du **matériel NVIDIA pris en charge**.
  - Trouvez votre modèle de GPU dans la liste <https://developer.nvidia.com/cuda-gpus>, puis vérifiez la valeur de **Compute Capability**. Elle doit satisfaire la contrainte de **CUDA Compute Capability** vérifiée précédemment pour pouvoir utiliser CUDA et cuDNN sans problème.

> Si vous prévoyez d’acheter une nouvelle carte graphique pour le deep learning, les critères de choix sont bien résumés dans l’article suivant, mis à jour de manière irrégulière par son auteur.  
> - [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)
>
> Et si vous avez besoin d’un guide plus global sur la configuration matérielle, l’article [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) du même auteur est également très instructif.
{: .prompt-tip }

Si vous remplissez toutes les conditions ci-dessus, vous pouvez commencer la mise en place de l’environnement.

## 1. Installer le pilote graphique NVIDIA

Vous devez d’abord installer le pilote graphique NVIDIA sur le système hôte. Vous pouvez télécharger et utiliser l’installateur `.run` depuis la [page de téléchargement des pilotes NVIDIA](https://www.nvidia.com/drivers/), mais il est préférable, dans la mesure du possible, d’utiliser le gestionnaire de paquets de votre système : c’est meilleur pour la gestion des versions et la maintenance. Référez-vous à la documentation officielle <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#driver-installation> et installez le pilote adapté à votre environnement.

### Module propriétaire vs module open source

Le pilote NVIDIA pour Linux se compose de plusieurs modules du noyau. À partir du pilote version 515 et des versions ultérieures, NVIDIA fournit deux types de modules noyau pour le pilote.

- Propriétaire : le pilote logiciel propriétaire fourni historiquement par NVIDIA.
- Open source : pilote open source distribué sous double licence MIT/GPLv2. Le code source est publié via <https://github.com/NVIDIA/open-gpu-kernel-modules>.

Le pilote propriétaire est fourni pour les GPU conçus sur des architectures allant de Maxwell jusqu’à avant Blackwell ; à partir de l’architecture Blackwell, il devrait être abandonné.  
À l’inverse, le pilote open source est pris en charge pour Turing et les architectures ultérieures.

[NVIDIA recommande, si possible, d’utiliser les modules noyau open source.](https://us.download.nvidia.com/XFree86/Linux-x86_64/560.35.03/README/kernel_open.html)  
Vous pouvez vérifier si votre GPU est compatible avec le pilote open source via [ce lien](https://github.com/NVIDIA/open-gpu-kernel-modules?tab=readme-ov-file#compatible-gpus).

Dans cet article, j’explique en supposant l’installation du pilote open source.

### Debian & Ubuntu

Dans le cas d’Ubuntu ou Debian, saisissez les commandes suivantes dans un terminal.
```bash
sudo apt update
sudo apt install nvidia-open
```

### Fedora

Sur Fedora 40, je présente la méthode consistant à télécharger et installer les paquets précompilés fournis par [RPM Fusion](https://rpmfusion.org/RPM%20Fusion).

#### 1-Fedora-1. Configurer le dépôt RPM Fusion

Suivez le [guide officiel RPM Fusion](https://rpmfusion.org/Configuration).  
Exécutez les commandes suivantes dans un terminal.

```bash
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
```

> Avec les anciennes versions de DNF (Fedora 40 et versions antérieures), la ligne de commande pour activer le dépôt de la bibliothèque openh264 à la deuxième ligne était la suivante :
>
> ```bash
> sudo dnf config-manager --enable fedora-cisco-openh264
> ```
>
> Cependant, à partir de DNF 5 (Fedora 41+), il faut saisir, à la place :
>
> ```bash
> sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1
> ```
>
> J’ai mis à jour le contenu de l’article en conséquence.
{: .prompt-info }

#### 1-Fedora-2. Installer le paquet akmod-nvidia

En vous référant au [guide d’installation du pilote NVIDIA fourni par RPM Fusion](https://rpmfusion.org/Howto/NVIDIA), installez le paquet `akmod-nvidia`.

```bash
sudo dnf update  # à cette étape, s’il y a eu une mise à jour du noyau, redémarrez sur le noyau le plus récent puis reprenez
sudo dnf install akmod-nvidia
sudo dnf mark user akmod-nvidia
```

> De même, avec les anciennes versions de DNF (Fedora 40 et versions antérieures), la ligne de commande de la troisième ligne pour empêcher la suppression du pilote NVIDIA lors d’un `autoremove` était la suivante :
>
> ```bash
> sudo dnf mark install akmod-nvidia
> ```
>
> Cependant, à partir de DNF 5 (Fedora 41+), il faut saisir, à la place :
>
> ```bash
> sudo dnf mark user akmod-nvidia
> ```
>
> J’ai mis à jour le contenu de l’article en conséquence.
{: .prompt-info }

> Par ailleurs, RPM Fusion a historiquement eu une position plutôt négative vis-à-vis des [modules noyau open source NVIDIA](#module-proprietaire-vs-module-open-source) et, sauf indication contraire, fournissait par défaut le pilote propriétaire. Cependant, selon des [directives RPM Fusion récemment modifiées (décembre 12025)](https://rpmfusion.org/Howto/NVIDIA?highlight=%28%5CbCategoryHowto%5Cb%29#Kernel_Open), pour le matériel « à double support » (architectures de Turing à avant Blackwell), ils sélectionneront désormais automatiquement la meilleure des deux options. Il n’est donc plus nécessaire de choisir manuellement une version. Pour les anciennes architectures antérieures à Turing, ou pour Blackwell et les architectures ultérieures, il n’y avait de toute façon qu’une seule option, donc aucun changement.
> En conséquence, j’ai confirmé que le passage expliquant la spécification de l’option d’utilisation des modules noyau open source via `/etc/rpm/macros.nvidia-kmod` avait été supprimé.
>
> De plus, pour le paquet `akmod-nvidia-open`, il est indiqué de ne pas l’utiliser sauf si vous devez appliquer vous-même des modifications downstream au pilote kernel-space.
>
> Ces points ont également été nouvellement pris en compte dans cet article.
{: .prompt-info }

#### 1-Fedora-3. Enregistrer une clé pour le chargement correct du pilote avec Secure Boot

> Une petite procédure additionnelle suffit pour utiliser normalement les pilotes graphiques NVIDIA tout en conservant Secure Boot. Désactiver Secure Boot rend le système nettement plus vulnérable, donc je recommande de ne pas le désactiver. Depuis l’entrée dans les années 12020, il est rare d’avoir une bonne raison de le faire.
{: .prompt-danger }

Installez d’abord les outils suivants.

```bash
sudo dnf install kmodtool akmods mokutil openssl
```

Ensuite, exécutez la commande ci-dessous pour générer une clé.

```bash
sudo kmodgenca -a
```

Vous devez maintenant enregistrer la clé générée dans le MOK du firmware UEFI.

```bash
sudo mokutil --import /etc/pki/akmods/certs/public_key.der
```

Après cette commande, il vous sera demandé de saisir un mot de passe pour l’enregistrement de la clé. Vous allez redémarrer dans un instant pour finaliser la procédure ; saisissez donc un mot de passe à usage unique que vous pourrez retenir.

Redémarrez ensuite le système avec la commande suivante.

```bash
systemctl reboot
```

Au démarrage, l’écran de gestion MOK s’affichera automatiquement. Sélectionnez « Enroll MOK », puis « Continue » et « Yes ». Une fenêtre vous demandera alors le mot de passe que vous venez de définir. Après saisie, la procédure d’enregistrement de la clé se termine. Tapez ensuite « reboot » pour redémarrer : le pilote NVIDIA devrait alors se charger correctement.

### Vérifier l’installation du pilote NVIDIA

Dans un terminal, vous pouvez vérifier le module noyau NVIDIA actuellement chargé avec la commande suivante.

```bash
cat /proc/driver/nvidia/version
```

Si un message similaire au suivant s’affiche, l’installation est réussie.

```bash
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  555.58.02  Release Build  (dvs-builder@U16-I3-B03-4-3)  Tue Jun 25 01:26:03 UTC 2024
GCC version:  gcc version 14.2.1 20240801 (Red Hat 14.2.1-1) (GCC) 
```

De plus, dans l’écosystème Linux, le module noyau `nouveau`, pilote graphique open source souvent utilisé par défaut, doit être désactivé après l’installation du pilote NVIDIA ; sinon, il peut causer des problèmes. Après installation du pilote NVIDIA et redémarrage, la commande suivante ne doit rien afficher.

```bash
lsmod |grep nouveau
```

## 2. Installer NVIDIA Container Toolkit

Vous devez maintenant installer [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). Suivez le [guide d’installation officiel NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html). Notez toutefois qu’il existe des points d’attention spécifiques à Fedora : lisez cette section jusqu’au bout avant de procéder.

### Cas d’Apt (Ubuntu, Debian, etc.)

#### 2-Apt-1. Configurer le dépôt pour télécharger les paquets

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### 2-Apt-2. Mettre à jour la liste des paquets

```bash
sudo apt update
```

#### 2-Apt-3. Installer le paquet

```bash
sudo apt install nvidia-container-toolkit
```

### Cas de Yum/Dnf (Fedora, RHEL, Centos, etc.)

> Lors de tests sur Fedora 40, contrairement à Ubuntu, les commandes `nvidia-smi` et le paquet `nvidia-persistenced` n’étaient pas inclus par défaut dans le pilote graphique NVIDIA : il a fallu installer en plus le paquet `xorg-x11-drv-nvidia-cuda`. Je n’ai pas testé directement sur RHEL/Centos, mais la configuration système est très proche de Fedora ; si vous rencontrez un problème en suivant le guide ci-dessous, tenter la même approche peut aider.
{: .prompt-warning }

> Sur Fedora 40, après avoir installé `xorg-x11-drv-nvidia-cuda` comme ci-dessus et exécuté une charge de travail d’exemple pour tester, cela fonctionnait correctement sur mon système. Si des problèmes persistent (par exemple à cause de SELinux), le [paquet nvidia-container-toolkit et le guide spécifiques à Fedora fournis par le groupe AI-ML de Fedora](https://copr.fedorainfracloud.org/coprs/g/ai-ml/nvidia-container-toolkit/) peuvent également être utiles.
{: .prompt-tip }

#### 2-Dnf-1. Configurer le dépôt pour télécharger les paquets

```bash
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

#### 2-Dnf-2. Installer le paquet

```bash
sudo dnf install nvidia-container-toolkit
```

Ou

```bash
sudo yum install nvidia-container-toolkit
```

### Cas de Zypper (openSUSE, SLES)

#### 2-Zypper-1. Configurer le dépôt pour télécharger les paquets

```bash
sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo
```

#### 2-Zypper-2. Installer le paquet

```bash
sudo zypper --gpg-auto-import-keys install nvidia-container-toolkit
```

## 3. Installation du moteur de conteneur

Ensuite, installez Docker CE ou Podman comme moteur de conteneur. Choisissez l’un des deux selon votre environnement et vos préférences, en vous référant à la [documentation officielle Docker](https://docs.docker.com/engine/install/) et à la [documentation officielle Podman](https://podman.io/docs/installation).

Le tableau suivant résume les principales différences, avantages et inconvénients entre Docker et Podman.

| Élément de comparaison | Docker | Podman |
| --- | --- | --- |
| Architecture | Modèle client-serveur, basé sur un démon (daemon) | Architecture sans démon (daemonless) |
| Sécurité | Dépend d’un démon exécuté par défaut avec les<br> droits root, ce qui présente des risques potentiels<br>(depuis la version 20.10 annoncée en 12020, support du<br> mode rootless, mais configuration supplémentaire requise) | Ne dépend pas d’un démon ; sauf configuration spécifique,<br> fonctionne en rootless par défaut, et bénéficie de la protection SELinux |
| Consommation de ressources | Du fait de l’architecture à démon, un processus<br> de fond tourne en permanence ; en général davantage<br> de ressources consommées | En général, moins de surcoût (overhead) |
| Temps de démarrage des conteneurs | Relativement plus lent | Architecture simplifiée, jusqu’à ~50% plus rapide |
| Écosystème et documentation | Écosystème étendu, soutien de la communauté,<br> documentation abondante | Écosystème plus restreint, moins de documentation |
| Réseau | Docker Bridge Network | Plugins CNI (Container Network Interface) |
| Support natif du YAML Kubernetes | X (conversion nécessaire) | O |

Références :
- <https://www.redhat.com/en/topics/containers/what-is-podman>
- <https://www.datacamp.com/blog/docker-vs-podman>
- <https://apidog.com/blog/docker-vs-podman/>
- <https://www.privacyguides.org/articles/2022/04/22/linux-application-sandboxing/#securing-linux-containers>

Docker existe depuis plus longtemps et a longtemps occupé une position de standard de facto dans l’industrie : son principal avantage est donc un écosystème très large et une documentation riche.  
Podman a été développé plus récemment par Red Hat ; sa conception vise nativement le daemonless et le rootless, ce qui lui confère des avantages en matière de sécurité, de consommation de ressources système et de temps de démarrage des conteneurs. Contrairement à Docker (où la panne du démon peut faire tomber tous les conteneurs), les conteneurs Podman sont totalement indépendants : la défaillance d’un conteneur n’affecte pas les autres.

Il est essentiel de choisir l’outil qui correspond le mieux à votre contexte. Toutefois, pour un débutant, commencer avec Podman semble être un bon choix. Certes, l’écosystème est plus petit que celui de Docker, mais il grandit rapidement grâce aux avantages évoqués et réduit l’écart. De plus, Podman est compatible avec de nombreux aspects de Docker, notamment la syntaxe Dockerfile, les images Docker et la CLI (interface en ligne de commande). Sauf raison particulière (par exemple, un système à grande échelle déjà construit autour de Docker et où adopter Podman imposerait un coût de transition important), il est rationnel d’adopter Podman dès le départ.

### Podman

Podman est disponible dans les dépôts système par défaut de la plupart des principales distributions Linux, et peut donc être installé simplement.

#### Sur Ubuntu

```bash
sudo apt install podman
```

#### Sur Fedora

```bash
sudo dnf install podman
```

#### Sur openSUSE

```bash
sudo zypper install podman
```

#### Vérifier que tout est correctement configuré

Essayez la commande suivante dans un terminal.

```bash
podman run --rm hello-world
```

Si un message semblable à celui-ci s’affiche, c’est réussi.

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

> Lors de tests au 12025-12-18T00:43:00+09:00, avec podman 5.7.1, [passt](https://passt.top/passt/about/) `20251215.gb40f5cd-1.fc43.x86_64` et fedora 43, l’erreur suivante s’est produite lors de l’exécution de conteneurs (y compris `hello-world`) ou lors de la construction d’images :
>
> ```bash
> Error: pasta failed with exit code 1:
> Couldn't set IPv6 route(s) in guest: Operation not supported
> ```
>
> Je n’utilise pas IPv6 et je suis dans un environnement réseau IPv4, mais il semble que l’étape de configuration réseau du conteneur tente de configurer un routage IPv6 via pasta (inclus dans la bibliothèque passt), ce qui déclenche le problème. J’ai confirmé que le fait de spécifier explicitement l’option `--net=pasta:-4` pour forcer l’usage d’IPv4, comme ci-dessous, évite le problème, aussi bien pour l’exécution de conteneurs que pour [l’étape de construction d’image évoquée plus loin](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2/#6-construction-de-limage-docker-et-execution-du-conteneur).
>
> ```bash
> podman run --net=pasta:-4 --rm hello-world
> ```
>
> En cherchant, j’ai trouvé [un issue déjà ouvert auparavant avec les mêmes symptômes](https://github.com/containers/podman/issues/22824). Cet issue indique que le problème a été corrigé dans [2024_06_24.1ee2eca](https://archives.passt.top/passt-user/20240624210651.61ce77af@elisabeth/), mais étant donné la similarité des symptômes observés (notamment le fait que cela se produise en utilisant Proton VPN), je soupçonne une réapparition d’un problème similaire.
{: .prompt-warning }

### Docker CE

#### Sur Ubuntu

##### 3-Ubuntu-1. Supprimer les anciennes versions ou paquets non officiels pour éviter les conflits

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-Ubuntu-2. Configurer le dépôt

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

##### 3-Ubuntu-3. Installer les paquets

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

##### 3-Ubuntu-4. Créer le groupe `Docker` et y inscrire l’utilisateur

Pour permettre à un utilisateur non-root de gérer Docker sans `sudo`, créez le groupe `Docker`, puis ajoutez l’utilisateur concerné. Exécutez les commandes suivantes dans un terminal.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Déconnectez-vous puis reconnectez-vous pour appliquer les modifications. Sur Ubuntu ou Debian, Docker démarre automatiquement à chaque démarrage du système sans configuration supplémentaire.

#### Sur Fedora

##### 3-Fedora-1. Supprimer les anciennes versions ou paquets non officiels pour éviter les conflits

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

##### 3-Fedora-2. Configurer le dépôt

```bash
sudo dnf install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

##### 3-Fedora-3. Installer les paquets

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Pendant l’installation, un message demandera d’approuver la clé GPG. Si la clé GPG correspond à `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`, saisissez `y` pour approuver.  
> Si la clé GPG ne correspond pas, il est possible que vous ayez téléchargé un paquet falsifié via une attaque de la chaîne d’approvisionnement ; vous devez alors interrompre l’installation.
{: .prompt-danger }

##### 3-Fedora-4. Démarrer le démon Docker

Docker est maintenant installé, mais il n’est pas encore lancé. Exécutez la commande suivante pour démarrer Docker.

```bash
sudo systemctl start docker
```

Pour démarrer automatiquement le service Docker au boot, exécutez :

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

##### 3-Fedora-5. Inscrire l’utilisateur dans le groupe `Docker`

Pour permettre à un utilisateur non-root de gérer Docker, ajoutez l’utilisateur au groupe `Docker`. Sur Fedora, le groupe `Docker` est créé automatiquement lors de l’installation des paquets, il suffit donc d’ajouter l’utilisateur.

```bash
sudo usermod -aG docker $USER
```

Déconnectez-vous puis reconnectez-vous pour appliquer les modifications.

#### Vérifier que tout est correctement configuré

Essayez la commande suivante dans un terminal.

```bash
docker run hello-world
```

Si un message semblable à celui-ci s’affiche, c’est réussi.

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
Suite dans [Partie 2](/posts/how-to-build-a-deep-learning-development-environment-with-nvidia-container-toolkit-and-docker-2)
