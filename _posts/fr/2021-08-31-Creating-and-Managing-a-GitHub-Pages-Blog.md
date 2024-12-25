---
title: "Créer et gérer un blog GitHub Pages"
description: >-
  Découvrons les caractéristiques et les différences entre les pages web statiques et dynamiques, les générateurs de sites statiques, et hébergeons un blog Jekyll sur GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---

J'ai commencé à héberger un blog sur GitHub Pages en utilisant Jekyll au début de 2021. Cependant, comme je n'avais pas correctement documenté le processus d'installation à l'époque, j'ai rencontré quelques difficultés lors de la maintenance ultérieure. J'ai donc décidé de résumer brièvement le processus d'installation et les méthodes de maintenance.

(+ Mise à jour du contenu en décembre 2024)

## 1. Générateur de site statique & hébergement web
### 1-1. Page web statique vs page web dynamique
#### Page web statique (Static Web Page)
- Une page web qui transmet directement à l'utilisateur les données stockées sur le serveur
- Le serveur web transmet une page préalablement stockée correspondant à la requête de l'utilisateur
- L'utilisateur voit la même page web à moins que les données stockées sur le serveur ne soient modifiées
- Généralement, la réponse est rapide car seul le fichier correspondant à la requête doit être transmis, sans nécessiter de travail supplémentaire
- Comme elle n'est composée que de simples fichiers, seul un serveur web est nécessaire, ce qui rend les coûts de mise en place peu élevés
- Le service est limité car il ne montre que les informations stockées
- L'ajout, la modification et la suppression des données doivent être effectués manuellement par l'administrateur
- Structure relativement plus favorable à l'optimisation pour les moteurs de recherche (SEO) car facile à crawler pour les moteurs de recherche

#### Page web dynamique (Dynamic Web Page)
- Une page web qui traite les données stockées sur le serveur avec des scripts avant de les transmettre
- Le serveur web interprète la requête de l'utilisateur, traite les données, puis transmet la page web générée
- L'utilisateur voit des pages web qui varient selon la situation, l'heure, la requête, etc.
- La réponse est relativement lente car le script doit être traité pour transmettre la page web
- Des coûts supplémentaires sont encourus lors de la mise en place car un serveur d'applications est nécessaire en plus du serveur web
- Divers services sont possibles car elle peut fournir dynamiquement une combinaison d'informations variées
- Selon la structure de la page web, l'utilisateur peut ajouter, modifier et supprimer des données depuis le navigateur
- 
### 1-2. Générateur de site statique (SSG, Static Site Generator)
- Un outil qui génère des pages web statiques basées sur des données brutes (généralement des fichiers texte au format markdown) et des modèles prédéfinis
- Automatise le processus de construction et de déploiement de pages web en écrivant des articles en markdown, sans avoir à écrire directement des pages HTML individuelles
- ex) Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Un service d'hébergement de pages web statiques gratuit fourni par GitHub
- Permet d'héberger une page web personnelle représentative par compte, et de créer et héberger un nombre illimité de pages de documentation de projet par dépôt
- Après avoir créé un dépôt nommé selon le format '{username}.github.io' correspondant à votre nom d'utilisateur GitHub, vous pouvez soit pousser directement les pages HTML construites dans ce dépôt, soit utiliser GitHub Actions pour effectuer la construction et le déploiement
- Si vous possédez votre propre domaine, vous pouvez le connecter dans les paramètres pour utiliser une adresse de domaine différente au lieu du domaine par défaut au format '{username}.github.io'

## 2. Choix du SSG et du thème à utiliser

### 2-1. Raisons du choix de Jekyll
Il existe plusieurs SSG comme Jekyll, Hugo, Gatsby, etc., mais j'ai décidé d'utiliser Jekyll. Voici les critères que j'ai pris en compte lors du choix du SSG et les raisons pour lesquelles j'ai choisi Jekyll :
- Peut-on minimiser les essais et erreurs inutiles et se concentrer sur l'écriture d'articles et la gestion du blog ?
  - Jekyll est le générateur de site web statique officiellement supporté par GitHub Pages. Bien sûr, d'autres SSG comme Hugo, Gatsby, etc. peuvent être hébergés sur GitHub Pages, et il y a aussi l'option d'utiliser un service d'hébergement complètement différent comme Netlify, mais en réalité, pour gérer un blog personnel de cette taille, le SSG utilisé pour la construction et la vitesse de construction, les performances, etc. ne sont pas vraiment importants, donc j'ai pensé qu'il serait préférable d'avoir quelque chose de plus simple à maintenir et avec plus de documentation de référence.
  - De plus, Jekyll a la plus longue période de développement par rapport à ses concurrents comme Hugo et Gatsby. Cela signifie qu'il est bien documenté et qu'il y a une quantité écrasante de ressources à consulter en cas de problème.
- Y a-t-il une variété de thèmes et de plugins disponibles ?
  - Même si on n'écrit pas directement le HTML en utilisant un SSG, créer soi-même divers modèles est fastidieux, prend beaucoup de temps et n'est pas vraiment nécessaire. Il y a déjà de nombreux thèmes excellents disponibles en ligne, il suffit d'en adopter un qui vous plaît et de l'utiliser.
  - De plus, comme j'utilise principalement C ou Python, je ne connais pas bien Ruby pour Jekyll ou Go pour Hugo, donc je voulais utiliser activement les thèmes et plugins existants.
  - J'ai pu rapidement trouver un thème qui me plaisait pour Jekyll, alors que pour Hugo ou Gatsby, il ne semblait pas y avoir autant de thèmes adaptés à un blog personnel. Comme mentionné précédemment, la compatibilité avec GitHub Pages, largement utilisé par les développeurs pour l'hébergement de blogs personnels, et la période de développement semblent avoir eu un impact significatif ici aussi.

### 2-2. Choix du thème
#### Minimal Mistakes (janvier 2021 - avril 2022)
- Dépôt GitHub : <https://github.com/mmistakes/minimal-mistakes>
- Page de démonstration : <https://mmistakes.github.io/minimal-mistakes/>
- Thème que j'ai utilisé pendant environ 1 an et 3 mois après avoir créé mon blog pour la première fois
- Prise en charge des commentaires via Disqus, Discourse, utterances, etc.
- Prise en charge des fonctions de classification par catégories et tags
- Prise en charge native de Google Analytics
- Possibilité de choisir parmi des skins prédéfinis
- Bien que j'aie ensuite découvert le thème Chirpy qui avait un design plus élégant et qui me plaisait davantage, compte tenu du fait qu'il s'agit d'un blog d'ingénieur, je pense que c'était un design suffisamment épuré pour être utilisé confortablement, même s'il n'était pas particulièrement joli.

#### Chirpy Jekyll Theme (avril 2022 - présent)
- Dépôt GitHub : <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Page de démonstration : <https://chirpy.cotes.page/>
- Thème que j'utilise depuis que j'ai changé le thème de mon blog en avril 2022
- Prise en charge de la classification multi-catégories et des tags
- Prise en charge native de l'expression des formules mathématiques en syntaxe LaTeX basée sur MathJax
- Prise en charge native des fonctions de diagramme basées sur Mermaid
- Prise en charge des commentaires via Disqus, Giscus, etc.
- Prise en charge de Google Analytics, GoatCounter
- Prise en charge des thèmes clair et sombre
- Au moment du changement de thème, MathJax et Mermaid n'étaient pas nativement pris en charge par le thème Minimal Mistakes et devaient être ajoutés par personnalisation, mais le thème Chirpy les prend en charge nativement. Bien que la personnalisation ne soit pas grand-chose, c'est quand même un petit avantage.
- Surtout, le design est joli. Le thème Minimal Mistakes est épuré mais a une certaine rigidité qui semble plus adaptée à une documentation technique officielle de projet ou à une page de portfolio qu'à un blog, tandis que le thème Chirpy a l'avantage d'avoir un design qui ne fait pas pâle figure même comparé aux plateformes de blogs commerciales comme Tistory, Medium, velog, etc.

## 3. Création du dépôt GitHub, construction et déploiement
Je décris ici sur la base du Chirpy Jekyll Theme actuellement utilisé (juin 2024), en supposant que Git est déjà installé.  
Référence à [Guide d'installation officiel de Jekyll](https://jekyllrb.com/docs/installation/) et [Page officielle du Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Installation de Ruby & Jekyll
Installez Ruby et Jekyll selon votre environnement de système d'exploitation en suivant le [Guide d'installation officiel de Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Création du dépôt GitHub
La [page officielle du Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) présente les deux méthodes suivantes :
1. Méthode utilisant le gem "jekyll-theme-chirpy" pour importer les fichiers principaux et le reste des ressources à partir du modèle [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Avantage : Facilité d'application des mises à niveau de version, comme nous le verrons plus tard.
  - Inconvénient : La personnalisation est limitée.
2. Méthode de fork du dépôt [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) comme dépôt de votre propre blog
  - Avantage : Comme vous gérez directement tous les fichiers dans le dépôt, vous pouvez personnaliser librement même les fonctionnalités non prises en charge par le thème en modifiant directement le code.
  - Inconvénient : Pour appliquer une mise à niveau de version, vous devez fusionner [le dernier tag upstream du dépôt original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), ce qui peut parfois entrer en conflit avec le code que vous avez personnalisé. Dans ce cas, vous devez résoudre ce conflit vous-même.

J'ai choisi la méthode 1. Dans le cas du thème Chirpy, il est déjà très complet, donc pour la plupart des utilisateurs, il n'y a pas grand-chose à personnaliser, et comme le développement et l'amélioration des fonctionnalités sont encore très actifs jusqu'en 2024, les avantages de suivre l'upstream original en temps voulu l'emportent sur les avantages d'appliquer sa propre personnalisation, à moins de faire des modifications majeures. Le guide officiel du thème Chirpy recommande également la méthode 1 pour la plupart des utilisateurs.

### 3-3. Configurations principales
Appliquez les configurations nécessaires dans les fichiers `_config.yml`{: .filepath} du répertoire racine et `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. Les commentaires sont bien écrits et les configurations sont intuitives, donc vous pouvez les appliquer sans difficulté particulière. Les seules configurations qui nécessitent un travail séparé à l'extérieur sont l'enregistrement du code d'authentification pour l'intégration de Google Search Console et l'intégration d'outils de webmaster comme Google Analytics ou GoatCounter, mais ce n'est pas vraiment une procédure compliquée et ce n'est pas le sujet principal que je veux aborder dans cet article, donc je vais omettre une description détaillée.

### 3-4. Construction locale
Ce n'est pas une étape obligatoire, mais vous pourriez vouloir vérifier à l'avance si quelque chose que vous avez écrit ou modifié sur le site s'affichera correctement sur le web. Dans ce cas, ouvrez un terminal dans le répertoire racine du dépôt local et exécutez la commande suivante :
```console
$ bundle exec jekyll s
```
Après quelques secondes d'attente, le site sera construit localement et vous pourrez voir le résultat à l'adresse <http://127.0.0.1:4000>.

### 3-5. Déploiement
Il y a deux méthodes :
1. Utilisation de GitHub Actions (en cas d'hébergement sur GitHub Pages)
  - Si vous utilisez le plan GitHub Free, vous devez garder le dépôt public
  - Sur la page web GitHub, sélectionnez l'onglet *Settings* du dépôt, puis cliquez sur *Code and automation > Pages* dans la barre de navigation de gauche et sélectionnez l'option **GitHub Actions** dans la section **Source**
  - Une fois la configuration terminée, le workflow *Build and Deploy* s'exécutera automatiquement à chaque nouveau commit poussé
2. Construction et déploiement manuels (en cas d'utilisation d'un autre service d'hébergement ou d'auto-hébergement)
  - Exécutez la commande suivante pour construire le site manuellement
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Téléchargez le résultat de la construction dans le répertoire `_site` sur le serveur

## 4. Rédaction d'articles
Le [guide de rédaction d'articles](https://chirpy.cotes.page/posts/write-a-new-post/) du thème Chirpy documente bien la méthode de rédaction d'articles et les options disponibles. Il offre diverses fonctionnalités en plus de celles décrites dans cet article, et contient des informations utiles à consulter si nécessaire. Ici, nous résumons les points principaux à garder à l'esprit à chaque fois que vous publiez un article.

### Création du fichier markdown
- Format du nom : `YYYY-MM-DD-TITLE.md`{: .filepath}
- Emplacement : répertoire `_posts`{: .filepath}

### Rédaction du Front Matter
Au début du fichier markdown, vous devez rédiger correctement le Front Matter.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title** : Titre de l'article
- **description** : Résumé. Si non écrit, une partie du début du contenu principal sera automatiquement utilisée, mais il est recommandé d'écrire directement la balise meta description pour l'optimisation des moteurs de recherche (SEO). Une longueur d'environ 135 à 160 caractères en alphabet romain, ou 80 à 110 caractères en caractères non-latins est appropriée.
- **date** : Date et heure exactes de rédaction de l'article et fuseau horaire (facultatif, si omis, la date de création ou de modification du fichier sera automatiquement reconnue et utilisée)
- **categories** : Classification des catégories de l'article
- **tags** : Classification des tags à appliquer à l'article
- **image** : Insertion d'une image d'aperçu en haut de l'article
  - **path** : Chemin du fichier image
  - **alt** : Texte alternatif (facultatif)
- **toc** : Utilisation de la fonction de table des matières dans la barre latérale droite, la valeur par défaut est `true`
- **comments** : Utilisé pour spécifier explicitement l'utilisation des commentaires pour un article individuel, indépendamment des paramètres par défaut du site
- **math** : Activation de la fonction d'expression mathématique basée sur [MathJax](https://www.mathjax.org/) intégré, désactivée par défaut (`false`) pour les performances de la page
- **mermaid** : Activation de la fonction de diagramme basée sur [Mermaid](https://github.com/mermaid-js/mermaid) intégré, désactivée par défaut (`false`)

## 5. Mise à niveau

Je décris en supposant que la méthode 1 a été choisie dans [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-création-du-dépôt-github). Si vous avez choisi la méthode 2, comme mentionné précédemment, vous devez fusionner manuellement le dernier tag upstream.

1. Modifiez `Gemfile`{: .filepath} pour spécifier la nouvelle version du gem "jekyll-theme-chirpy".
2. Dans le cas d'une mise à niveau majeure, les fichiers principaux non inclus dans le gem "jekyll-theme-chirpy" et les options de configuration peuvent également avoir changé. Dans ce cas, vous devez vérifier les changements avec l'API GitHub ci-dessous et les refléter manuellement.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
