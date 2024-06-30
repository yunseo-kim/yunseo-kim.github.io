---
title: "Configuration de l'environnement de développement pour le machine learning"
description: >-
  Cet article traite de la méthode de configuration de l'environnement de développement, qui peut être considérée comme la première étape pour étudier le machine learning sur une machine locale. Tout le contenu a été rédigé sur la base d'Ubuntu 20.04 LTS avec une carte graphique NVIDIA Geforce RTX 3070.
categories:
  - Data Science
tags:
  - Machine Learning
  - Deep Learning
toc: true
toc_sticky: true
---

## Aperçu
Cet article traite de la méthode de configuration de l'environnement de développement, qui peut être considérée comme la première étape pour étudier le machine learning sur une machine locale. Tout le contenu a été rédigé sur la base d'Ubuntu 20.04 LTS avec une carte graphique NVIDIA Geforce RTX 3070.

- Stack technologique à configurer
  - Ubuntu 20.04 LTS
  - Python 3.8
  - pip 21.0.1
  - jupyter
  - matplotlib
  - numpy
  - pandas
  - scipy
  - scikit-learn
  - CUDA 11.0.3
  - cuDNN 8.0.5
  - Frameworks de deep learning (il est recommandé de n'en installer qu'un seul par environnement)
    - PyTorch 1.7.1
    - TensorFlow 2.4.0

## 0. Vérifications préalables
- L'utilisation de Linux est recommandée pour l'étude du machine learning. Bien que ce soit possible sous Windows, cela peut entraîner une perte de temps sur de nombreux petits aspects. La version LTS la plus récente d'Ubuntu est la plus pratique. Les pilotes propriétaires non open source sont également installés automatiquement pour plus de commodité, et comme il y a beaucoup d'utilisateurs, la plupart des documents techniques sont rédigés sur la base d'Ubuntu.
- En général, Python est préinstallé sur la plupart des distributions Linux, y compris Ubuntu. Cependant, si Python n'est pas installé, vous devez d'abord l'installer avant de suivre cet article.
  - Vous pouvez vérifier la version actuelle de Python installée avec la commande suivante :
  ```
  $ python3 --version
  ```
  - Si vous prévoyez d'utiliser TensorFlow 2 ou PyTorch, vous devez vérifier les versions Python compatibles. Au moment de la rédaction de cet article, [les versions Python prises en charge par la dernière version de PyTorch](https://pytorch.org/get-started/locally/#linux-python) sont 3.6-3.8, et [les versions Python prises en charge par la dernière version de TensorFlow 2](https://www.tensorflow.org/install) sont 3.5-3.8.  
  Dans cet article, nous utilisons Python 3.8.
- Si vous prévoyez d'étudier le machine learning sur une machine locale, il est préférable de préparer au moins un GPU. Bien que le prétraitement des données soit possible avec un CPU, la différence de vitesse d'apprentissage entre CPU et GPU devient écrasante à mesure que la taille du modèle augmente (en particulier dans le cas du deep learning).
  - Pour le machine learning, il n'y a en réalité qu'un seul choix de fabricant de GPU. Vous devez utiliser un produit NVIDIA. NVIDIA est une entreprise qui a beaucoup investi dans le domaine du machine learning, et presque tous les frameworks de machine learning utilisent la bibliothèque CUDA de NVIDIA.
  - Si vous prévoyez d'utiliser un GPU pour le machine learning, vous devez d'abord vérifier si le modèle de carte graphique que vous souhaitez utiliser est compatible avec CUDA. Vous pouvez vérifier le nom du modèle GPU installé dans votre ordinateur avec la commande ```nvidia-smi``` dans le terminal. Trouvez le nom du modèle correspondant dans la liste des GPU sur le [lien](https://developer.nvidia.com/cuda-gpus), puis vérifiez la valeur **Compute Capability**. Cette valeur doit être d'au moins 3.5 pour pouvoir utiliser CUDA.
  - Les critères de sélection des GPU sont bien résumés dans l'article suivant. L'auteur met continuellement à jour cet article.  
  [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2020/09/07/which-gpu-for-deep-learning/)  
  L'article [A Full Hardware Guide to Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) écrit par la même personne est également très utile. Pour référence, la conclusion de l'article ci-dessus est la suivante :
    > The RTX 3070 and RTX 3080 are mighty cards, but they lack a bit of memory. For many tasks, however, you do not need that amount of memory.  
    > The RTX 3070 is perfect if you want to learn deep learning. This is so because the basic skills of training most architectures can be learned by just scaling them down a bit or using a bit smaller input images. If I would learn deep learning again, I would probably roll with one RTX 3070, or even multiple if I have the money to spare.
    > The RTX 3080 is currently by far the most cost-efficient card and thus ideal for prototyping. For prototyping, you want the largest memory, which is still cheap. With prototyping, I mean here prototyping in any area: Research, competitive Kaggle, hacking ideas/models for a startup, experimenting with research code. For all these applications, the RTX 3080 is the best GPU.

Si vous avez satisfait à toutes les conditions mentionnées ci-dessus, commençons la configuration de l'environnement de travail.

## 1. Création du répertoire de travail
Ouvrez un terminal et modifiez le fichier .bashrc pour enregistrer la variable d'environnement (la commande suit le prompt $).  
Tout d'abord, utilisez la commande suivante pour ouvrir l'éditeur nano (vim ou tout autre éditeur convient également).
```
$ nano ~/.bashrc
```
Ajoutez le contenu suivant à la dernière ligne. Vous pouvez changer le chemin entre guillemets si vous le souhaitez.  
```export ML_PATH="$HOME/ml"```

Appuyez sur Ctrl+O pour sauvegarder, puis sur Ctrl+X pour quitter.

Maintenant, exécutez la commande suivante pour appliquer la variable d'environnement.
```
$ source ~/.bashrc
```
Créez le répertoire.
```
$ mkdir -p $ML_PATH
```

## 2. Installation du gestionnaire de paquets pip
Il existe plusieurs façons d'installer les paquets Python nécessaires au machine learning. Vous pouvez utiliser une distribution Python scientifique comme Anaconda (méthode recommandée pour le système d'exploitation Windows), ou vous pouvez utiliser pip, l'outil de packaging natif de Python. Ici, nous utiliserons la commande pip dans le shell bash de Linux ou macOS.

Vérifiez si pip est installé sur votre système avec la commande suivante.
```
$ pip3 --version

Commande 'pip3' introuvable, mais peut être installée avec :

sudo apt install python3-pip

```
Si vous voyez cela, cela signifie que pip n'est pas installé sur votre système. Installez-le en utilisant le gestionnaire de paquets de votre système (ici apt) (si un numéro de version apparaît, cela signifie qu'il est déjà installé, donc vous pouvez sauter cette commande).
```
$ sudo apt install python3-pip
```
Pip est maintenant installé sur votre système.

## 3. Création d'un environnement virtuel indépendant (recommandé)
Pour créer un environnement virtuel (pour éviter les conflits de versions de bibliothèques avec d'autres projets), installez venv.
```
$ sudo apt install python3-venv
```
Ensuite, créez un environnement Python indépendant comme suit. La raison pour laquelle nous faisons cela est d'éviter les conflits dus aux différentes versions de bibliothèques nécessaires pour chaque projet, donc vous devez créer un nouvel environnement virtuel et construire un environnement indépendant chaque fois que vous commencez un nouveau projet.
```
$ cd $ML_PATH
$ python3 -m venv --system-site-packages ./(nom de l'environnement)
```
Pour activer cet environnement virtuel, ouvrez un terminal et entrez la commande suivante.
```
$ cd $ML_PATH
$ source ./(nom de l'environnement)/bin/activate
```
Après avoir activé l'environnement virtuel, mettez à jour pip dans l'environnement virtuel.
```
(env) $ pip install -U pip
```
Pour désactiver l'environnement virtuel plus tard, utilisez la commande ```deactivate```. Lorsque l'environnement est activé, tout paquet installé avec la commande pip sera installé dans cet environnement isolé et Python utilisera ces paquets.

## 3′. (Si vous ne créez pas d'environnement virtuel) Mise à jour de la version de pip
Lors de l'installation de pip sur le système, vous téléchargez et installez un fichier binaire du serveur miroir de la distribution (ici Ubuntu), mais ce fichier binaire est généralement en retard sur la mise à jour et n'est souvent pas la dernière version (dans mon cas, la version 20.3.4 a été installée). Pour utiliser la dernière version de pip, exécutez la commande suivante pour installer (ou mettre à jour si déjà installé) pip dans le *répertoire personnel de l'utilisateur*.  
```
$ python3 -m pip install -U pip

Collecting pip
(omis)
Successfully installed pip-21.0.1
```
Vous pouvez voir que pip a été installé dans la version 21.0.1, qui est la dernière version au moment de la rédaction de cet article. À ce moment, pip installé dans le répertoire personnel de l'utilisateur n'est pas automatiquement reconnu par le système, donc vous devez l'enregistrer comme variable d'environnement PATH pour que le système puisse le reconnaître et l'utiliser.

Ouvrez à nouveau le fichier .bashrc avec un éditeur.
```
$ nano ~/.bashrc
```
Cette fois, trouvez la ligne commençant par ```export PATH=```. S'il n'y a pas de chemin écrit après, ajoutez simplement le contenu comme vous l'avez fait à [l'étape 1](#1-création-du-répertoire-de-travail). S'il y a déjà d'autres chemins enregistrés, ajoutez le contenu à la fin en utilisant deux-points.  
```export PATH="$HOME/.local/bin"```  
```export PATH="(chemin existant):$HOME/.local/bin"```

[La mise à niveau de pip système par une méthode autre que le gestionnaire de paquets système peut causer des problèmes en raison de conflits de version](https://github.com/pypa/pip/issues/5599). C'est pourquoi nous installons pip dans le répertoire personnel de l'utilisateur sans utiliser ```sudo```. Pour la même raison, il est préférable d'utiliser la commande ```python3 -m pip``` au lieu de la commande ```pip``` pour utiliser pip, sauf dans un environnement virtuel.

## 4. Installation des paquets pour le machine learning (jupyter, matplotlib, numpy, pandas, scipy, scikit-learn)
Installez tous les paquets nécessaires et les autres paquets liés par dépendance avec la commande pip suivante.  
Les droits d'administrateur sont nécessaires si vous n'utilisez pas venv.  
De plus, dans mon cas, j'ai simplement utilisé la commande ```pip``` car j'utilise venv, mais si vous n'utilisez pas venv, il est recommandé d'utiliser la commande ```python3 -m pip``` à la place, comme mentionné précédemment.
```
(env) $ pip install -U jupyter matplotlib numpy pandas scipy scikit-learn

Collecting jupyter
  Downloading jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting matplotlib
(suite omise)
```
Si vous avez utilisé venv, enregistrez un noyau pour Jupyter et donnez-lui un nom.
```
(env) $ python3 -m ipykernel install --user --name=(nom du noyau)
```
Désormais, pour exécuter Jupyter, utilisez la commande suivante.
```
(env) $ jupyter notebook
```

## 5. Installation de CUDA & cuDNN
### 5-1. Vérification des versions CUDA & cuDNN nécessaires
Vérifiez les versions CUDA prises en charge dans la [documentation officielle de PyTorch](https://pytorch.org/get-started/locally/).  
![Vérification des versions CUDA compatibles avec PyTorch](/assets/img/머신러닝-개발환경-구축하기/PyTorch_Installation.png)  
Sur la base de PyTorch version 1.7.1, les versions CUDA prises en charge sont 9.2, 10.1, 10.2, 11.0. Pour les GPU NVIDIA série 30, CUDA 11 est nécessaire, donc nous savons que la version 11.0 est nécessaire.

Vérifiez également la version CUDA nécessaire dans la [documentation officielle de TensorFlow 2](https://www.tensorflow.org/install/gpu).  
![Vérification des versions CUDA compatibles avec TensorFlow 2](/assets/img/머신러닝-개발환경-구축하기/TensorFlow_GPU_support.png)  
Sur la base de TensorFlow version 2.4.0, nous avons confirmé que CUDA version 11.0 et cuDNN version 8.0 sont nécessaires.

Dans mon cas, j'utilise parfois PyTorch et parfois TensorFlow 2 selon les circonstances, donc j'ai vérifié les versions CUDA compatibles avec les deux paquets. Vous devez vérifier les exigences du paquet dont vous avez besoin et vous y conformer.

### 5-2. Installation de CUDA
Accédez à [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive), puis sélectionnez la version que vous avez vérifiée précédemment. Dans cet article, nous sélectionnons [CUDA Toolkit 11.0 Update1](https://developer.nvidia.com/cuda-11.0-update1-download-archive).  
![CUDA 11.0 Update 1](/assets/img/머신러닝-개발환경-구축하기/CUDA_installation-1.png)  
Maintenant, sélectionnez la plateforme et le type d'installateur correspondants, puis suivez les instructions qui apparaissent à l'écran. À ce moment, [il est préférable d'utiliser le gestionnaire de paquets système pour l'installateur si possible](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html#choose-installation-method). Ma méthode préférée est deb (network