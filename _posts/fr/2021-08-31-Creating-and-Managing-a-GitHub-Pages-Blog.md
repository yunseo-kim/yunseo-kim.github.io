---
title: "Créer et gérer un blog GitHub Pages"
description: >-
  Découvrons les caractéristiques et les différences entre les pages web statiques et dynamiques, les générateurs de sites statiques, et hébergeons un blog Jekyll sur GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
---

J'ai commencé à héberger un blog sur GitHub Pages en utilisant Jekyll au début de 2021. Cependant, comme je n'avais pas correctement documenté le processus d'installation à l'époque, j'ai rencontré quelques difficultés lors de la maintenance ultérieure. J'ai donc décidé de résumer brièvement le processus d'installation et les méthodes de maintenance.  
~~En réalité, c'est surtout parce que je ne suis pas encore très familier avec l'hébergement de sites statiques.~~
(Mise à jour du contenu en juin 2024)

## 1. Générateur de sites statiques & hébergement web
### 1-1. Pages web statiques vs pages web dynamiques
#### Pages web statiques
- Pages web qui transmettent les données stockées sur le serveur directement à l'utilisateur
- Le serveur web transmet la page préalablement stockée correspondant à la demande de l'utilisateur
- Les utilisateurs voient la même page web à moins que les données stockées sur le serveur ne soient modifiées
- Généralement, la réponse est rapide car seul le fichier correspondant à la demande doit être transmis, sans nécessiter de traitement supplémentaire
- Comme elles ne sont composées que de fichiers simples, seul un serveur web est nécessaire, ce qui rend les coûts de mise en place peu élevés
- Le service est limité car seules les informations stockées sont affichées
- L'ajout, la modification et la suppression des données doivent être effectués manuellement par l'administrateur
- Structure facile à crawler pour les moteurs de recherche, relativement plus avantageuse pour l'optimisation des moteurs de recherche (SEO)

#### Pages web dynamiques
- Pages web qui traitent les données stockées sur le serveur avec des scripts avant de les transmettre
- Le serveur web interprète la demande de l'utilisateur, traite les données, puis transmet la page web générée
- Les utilisateurs voient des pages web qui varient selon la situation, l'heure, la demande, etc.
- La réponse est relativement lente car le script doit être traité pour transmettre la page web
- Des coûts supplémentaires sont encourus lors de la mise en place car un serveur d'application est nécessaire en plus du serveur web
- Divers services sont possibles car des informations variées peuvent être combinées et fournies dynamiquement
- Selon la structure de la page web, les utilisateurs peuvent ajouter, modifier et supprimer des données directement depuis le navigateur

### 1-2. Générateur de sites statiques (SSG, Static Site Generator)
- Outil qui génère des pages web statiques basées sur des données brutes (généralement des fichiers texte au format markdown) et des modèles prédéfinis
- Automatise le processus de construction et de déploiement de pages web en écrivant des articles en markdown, sans avoir à écrire directement des pages HTML individuelles
- ex) Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Service d'hébergement de pages web statiques gratuit fourni par GitHub
- Permet d'héberger une page web personnelle représentative par compte, et de créer et héberger un nombre illimité de pages de documentation de projet par dépôt
- Après avoir créé un dépôt nommé selon le format '{username}.github.io' correspondant à votre nom d'utilisateur GitHub, vous pouvez soit pousser directement les pages HTML construites vers ce dépôt, soit utiliser GitHub Actions pour effectuer la construction et le déploiement
- Si vous possédez votre propre domaine, vous pouvez le connecter dans les paramètres pour utiliser une adresse de domaine différente au lieu du domaine par défaut au format '{username}.github.io'

## 2. Choix du SSG et du thème à utiliser

### Raisons du choix de Jekyll
Il existe plusieurs SSG comme Jekyll, Hugo, Gatsby, etc., mais j'ai décidé d'utiliser Jekyll. Voici les critères que j'ai pris en compte lors du choix du SSG et les raisons pour lesquelles j'ai choisi Jekyll :
- Est-il possible de minimiser les essais et erreurs inutiles et de se concentrer sur l'écriture et la gestion du blog ?
  - Jekyll est le générateur de sites web statiques officiellement pris en charge par Github Pages. Bien sûr, d'autres SSG comme Hugo, Gatsby, etc. peuvent également être hébergés sur Github Pages, et il existe également l'option d'utiliser un service d'hébergement complètement différent comme Netlify, mais en réalité, pour gérer un blog personnel de cette taille, le SSG utilisé pour la construction et la vitesse de construction, les performances, etc. ne sont pas vraiment importants, donc j'ai pensé qu'il serait préférable d'opter pour quelque chose de plus simple à maintenir et avec plus de documentation de référence.
  - De plus, Jekyll a la plus longue période de développement par rapport à ses concurrents comme Hugo et Gatsby. Cela signifie que la documentation est bien faite et qu'il y a une quantité écrasante de ressources à consulter en cas de problème.
- Y a-t-il une variété de thèmes et de plugins disponibles ?
  - Même si on n'écrit pas directement le HTML en utilisant un SSG, créer soi-même divers modèles est fastidieux, prend beaucoup de temps, et ce n'est pas vraiment nécessaire. Il y a déjà de nombreux thèmes excellents disponibles en ligne, il suffit d'en adopter un qui vous plaît et de l'utiliser.
  - De plus, comme j'utilise principalement C ou Python, je ne connais pas bien Ruby pour Jekyll ou Go pour Hugo, donc j'ai voulu utiliser activement les thèmes et plugins existants.
  - Avec Jekyll, j'ai pu rapidement trouver un thème qui me plaisait au premier coup d'œil, alors qu'avec Hugo ou Gatsby, il ne semblait pas y avoir autant de thèmes adaptés à un blog personnel. Comme mentionné précédemment, la compatibilité avec Github Pages, que de nombreux développeurs utilisent pour héberger leurs blogs personnels, et la période de développement semblent avoir eu un impact important ici aussi.

### Choix du thème
#### Minimal Mistakes (janvier 2021 - avril 2022)
- Dépôt Github : <https://github.com/mmistakes/minimal-mistakes>
- Page de démonstration : <https://mmistakes.github.io/minimal-mistakes/>
- Thème que j'ai utilisé pendant environ 1 an et 3 mois après avoir créé mon blog
- Prise en charge des commentaires via Disqus, Discourse, utterances, etc.
- Prise en charge des fonctions de catégorisation et de balisage
- Prise en charge native de Google Analytics
- Possibilité de choisir parmi des skins prédéfinis
- Bien que j'aie ensuite découvert le thème Chirpy qui a un design plus élégant et qui me plaît davantage, en tenant compte du fait qu'il s'agit d'un blog d'ingénierie, je pense que c'était un thème assez correct à utiliser avec un design épuré, même s'il n'était pas particulièrement joli.

### Thème Chirpy Jekyll (depuis avril 2022)
- Dépôt Github : <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Page de démonstration : <https://chirpy.cotes.page/>
- Thème que j'utilise depuis que j'ai changé le thème de mon blog en avril 2022
- Prise en charge de la classification multi-catégories et des fonctions de balisage
- Prise en charge native de l'expression des équations en syntaxe LaTeX basée sur MathJax
- Prise en charge native des fonctions de diagramme basées sur Mermaid
- Prise en charge des commentaires via Disqus, Giscus, etc.
- Prise en charge de Google Analytics, GoatCounter
- Prise en charge des thèmes clair et sombre
- Au moment du changement de thème, MathJax et Mermaid n'étaient pas pris en charge nativement par le thème Minimal Mistakes et devaient être ajoutés par personnalisation, mais le thème Chirpy les prend en charge nativement. Bien sûr, la personnalisation n'était pas grand-chose, mais c'est quand même un petit avantage.
- Surtout, le design est joli. Le thème Minimal Mistakes est épuré mais a une certaine rigidité qui semble plus adaptée à une documentation technique officielle de projet ou à une page de portfolio qu'à un blog, tandis que le thème Chirpy a l'avantage d'avoir un design qui ne fait pas pâle figure même comparé aux plateformes de blogs commerciales comme Tistory, Medium, velog, etc.

## 3. Création du dépôt GitHub, construction et déploiement
Je décris ici le processus basé sur le thème Chirpy Jekyll que j'utilise actuellement (juin 2024), en supposant que Git est déjà installé.  
Référez-vous au [guide d'installation officiel de Jekyll](https://jekyllrb.com/docs/installation/) et à la [page officielle du thème Chirpy Jekyll](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Installation de Ruby & Jekyll
Installez Ruby et Jekyll selon votre environnement de système d'exploitation en suivant le [guide d'installation officiel de Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Création du dépôt GitHub
La [page officielle du thème Chirpy Jekyll](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) présente les deux méthodes suivantes :
1. Méthode utilisant le gem "jekyll-theme-chirpy" pour importer les fichiers principaux et le reste des ressources à partir du modèle [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Avantage : Facilité d'application des mises à niveau de version, comme nous le verrons plus tard.
  - Inconvénient : La personnalisation est limitée.
2. Méthode de fork du dépôt [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) pour en faire le dépôt de votre propre blog
  - Avantage : Comme vous gérez directement tous les fichiers dans le dépôt, vous pouvez personnaliser librement même les fonctionnalités non prises en charge par le thème en modifiant directement le code.
  - Inconvénient : Pour appliquer une mise à niveau de version, vous devez fusionner [le dernier tag upstream du dépôt original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), ce qui peut parfois entrer en conflit avec le code que vous avez personnalisé. Dans ce cas, vous devez résoudre ces conflits manuellement.

J'ai choisi la méthode 1. Dans le cas du thème Chirpy, il est déjà très complet, donc pour la plupart des utilisateurs, il n'y a pas grand-chose à personnaliser, et comme il est encore activement développé et amélioré jusqu'en 2024, les avantages de suivre l'upstream original en temps voulu l'emportent sur les avantages d'appliquer sa propre personnalisation, à moins de vouloir vraiment modifier en profondeur. Le guide officiel du thème Chirpy recommande également la méthode 1 pour la plupart des utilisateurs.

### 3-3. Configurations principales
Appliquez les configurations nécessaires dans les fichiers `_config.yml`{: .filepath} du répertoire racine et `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. Les commentaires sont bien écrits et les configurations sont intuitives, donc vous pouvez les appliquer sans difficulté particulière. Les seules configurations qui nécessitent un travail séparé à l'extérieur sont l'enregistrement du code d'authentification pour l'intégration de Google Search Console et l'intégration d'outils de webmaster comme Google Analytics ou GoatCounter, mais ce n'est pas vraiment une procédure compliquée et ce n'est pas le sujet principal de cet article, donc je vais omettre les détails.

### 3-4. Construction locale
Ce n'est pas une étape obligatoire, mais vous pourriez vouloir vérifier à l'avance si un nouveau post que vous avez écrit ou une modification que vous avez apportée au site s'affichera correctement sur le web. Dans ce cas, ouvrez un terminal dans le répertoire racine du dépôt local et exécutez la commande suivante :
```console
$ bundle exec jekyll s
```
Après quelques secondes d'attente, le site sera construit localement et vous pourrez voir le résultat à l'adresse <http://127.0.0.1:4000>.

### 3-5. Déploiement
Il y a deux méthodes :
1. Utilisation de GitHub Actions (dans le cas d'un hébergement sur GitHub Pages)
  - Si vous utilisez le plan GitHub Free, vous devez garder le dépôt public
  - Sur la page web GitHub, sélectionnez l'onglet *Settings* du dépôt, puis cliquez sur *Code and automation > Pages* dans la barre de navigation de gauche et sélectionnez l'option **GitHub Actions** dans la section **Source**
  - Une fois la configuration terminée, le workflow *Build and Deploy* s'exécutera automatiquement à chaque nouveau commit poussé
2. Construction et déploiement manuels (dans le cas de l'utilisation d'un autre service d'hébergement ou d'un auto-hébergement)
  - Exécutez la commande suivante pour construire le site manuellement
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Téléchargez le résultat de la construction dans le répertoire `_site` sur le serveur

## 4. Rédaction de posts
Le [guide de rédaction de posts](https://chirpy.cotes.page/posts/write-a-new-post/) du thème Chirpy documente bien la méthode de rédaction des posts et les options disponibles. Il fournit diverses fonctionnalités en plus de celles décrites dans cet article, et c'est un contenu utile à consulter si nécessaire. Ici, nous résumons les points principaux à garder à l'esprit à chaque fois que vous postez.

### Création du fichier markdown
- Format du nom : `YYYY-MM-DD-TITLE.md`{: .filepath}
- Emplacement : répertoire `_posts`{: .filepath}

### Rédaction du Front Matter
Vous devez rédiger correctement le Front Matter au début du fichier markdown.
```YAML
