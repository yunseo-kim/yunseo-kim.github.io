---
title: Créer et gérer un blog GitHub Pages
description: Découvrons les caractéristiques et différences entre pages web statiques et dynamiques, les générateurs de sites statiques, et hébergeons un blog Jekyll sur GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---
J'ai commencé à héberger un blog sur GitHub Pages en utilisant Jekyll au début de l'année 12021 de [l'ère holocène](https://en.wikipedia.org/wiki/Holocene_calendar). Cependant, n'ayant pas correctement documenté le processus d'installation à l'époque, j'ai rencontré quelques difficultés lors de la maintenance ultérieure. J'ai donc décidé de résumer brièvement le processus d'installation et les méthodes de maintenance.

(+ Mise à jour 12024.12)

## 1. Générateur de site statique & hébergement web
### 1-1. Pages web statiques vs pages web dynamiques
#### Pages web statiques
- Pages web qui transmettent directement aux utilisateurs les données stockées sur le serveur
- Le serveur web transmet la page préalablement stockée correspondant à la demande de l'utilisateur
- Les utilisateurs voient la même page web à moins que les données stockées sur le serveur ne soient modifiées
- La réponse est généralement rapide car seul le fichier correspondant à la demande doit être transmis, sans traitement supplémentaire
- Composées uniquement de fichiers simples, elles ne nécessitent qu'un serveur web, ce qui rend leur mise en place peu coûteuse
- Les services sont limités car elles ne montrent que les informations stockées
- L'ajout, la modification et la suppression de données doivent être effectués manuellement par l'administrateur
- Structure favorable au référencement (SEO) car facile à explorer par les moteurs de recherche

#### Pages web dynamiques
- Pages web qui traitent les données stockées sur le serveur via des scripts avant de les transmettre
- Le serveur web interprète la demande de l'utilisateur, traite les données puis transmet la page web générée
- Les utilisateurs voient des pages web qui varient selon la situation, l'heure, la demande, etc.
- La réponse est relativement lente car les scripts doivent être traités avant la transmission
- Nécessitent un serveur d'applications en plus du serveur web, ce qui entraîne des coûts supplémentaires
- Permettent divers services en combinant dynamiquement différentes informations
- Selon la structure de la page web, les utilisateurs peuvent ajouter, modifier et supprimer des données depuis leur navigateur

### 1-2. Générateurs de sites statiques (SSG)
- Outils qui génèrent des pages web statiques à partir de données brutes (généralement des fichiers texte au format markdown) et de modèles prédéfinis
- Automatisent le processus de création et de déploiement de pages web sans avoir à écrire directement chaque page HTML
- Exemples : Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Service d'hébergement gratuit de pages web statiques fourni par GitHub
- Permet d'héberger une page web personnelle par compte et un nombre illimité de pages de documentation de projet par dépôt
- Après avoir créé un dépôt nommé '{username}.github.io' correspondant à votre nom d'utilisateur GitHub, vous pouvez soit pousser directement les pages HTML construites, soit utiliser GitHub Actions pour la construction et le déploiement
- Si vous possédez un domaine, vous pouvez le connecter dans les paramètres pour utiliser une adresse de domaine personnalisée au lieu du domaine par défaut '{username}.github.io'

## 2. Choix du SSG et du thème

### 2-1. Pourquoi Jekyll
Bien qu'il existe plusieurs SSG comme Jekyll, Hugo, Gatsby, j'ai choisi Jekyll. Voici les critères considérés et les raisons de ce choix :
- Est-il possible de minimiser les essais inutiles et de se concentrer sur la rédaction et la gestion du blog ?
  - Jekyll est le générateur de sites statiques officiellement pris en charge par GitHub Pages. Bien que d'autres SSG comme Hugo ou Gatsby puissent également être hébergés sur GitHub Pages, et qu'il existe d'autres services d'hébergement comme Netlify, pour un blog personnel de cette taille, le choix technique du SSG, la vitesse de construction et les performances ne sont pas vraiment importants. J'ai donc préféré opter pour une solution plus simple à maintenir et mieux documentée.
  - Jekyll existe depuis plus longtemps que ses concurrents comme Hugo ou Gatsby. La documentation est donc plus complète et il y a beaucoup plus de ressources disponibles en cas de problème.
- Y a-t-il une variété de thèmes et de plugins disponibles ?
  - Même en utilisant un SSG, créer ses propres modèles est fastidieux et chronophage, et ce n'est pas vraiment nécessaire. Il existe déjà d'excellents thèmes disponibles en ligne qu'on peut adopter et utiliser.
  - De plus, comme j'utilise principalement C et Python, je ne connais pas bien Ruby (Jekyll) ou Go (Hugo), donc je voulais utiliser activement les thèmes et plugins existants.
  - J'ai rapidement trouvé un thème qui me plaisait pour Jekyll, alors que Hugo et Gatsby semblaient avoir relativement moins de thèmes adaptés à un blog personnel. La compatibilité avec GitHub Pages, très utilisé par les développeurs pour l'hébergement de blogs personnels, et la longue période de développement ont probablement eu un impact significatif ici aussi.

### 2-2. Choix du thème
#### Minimal Mistakes (12021.01 - 12022.04)
- Dépôt GitHub : <https://github.com/mmistakes/minimal-mistakes>
- Page de démonstration : <https://mmistakes.github.io/minimal-mistakes/>
- Thème que j'ai utilisé pendant environ 1 an et 3 mois après la création de mon blog
- Prise en charge des commentaires via Disqus, Discourse, utterances, etc.
- Fonctionnalités de classification par catégories et tags
- Prise en charge native de Google Analytics
- Possibilité de choisir parmi des skins prédéfinis
- Bien que j'aie ensuite découvert et adopté le thème Chirpy au design plus élégant, Minimal Mistakes offre un design assez épuré qui convenait bien à un blog technique.

#### Chirpy Jekyll Theme (12022.04 - présent)
- Dépôt GitHub : <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Page de démonstration : <https://chirpy.cotes.page/>
- Thème que j'utilise depuis avril 12022
- Prise en charge de la classification multi-catégories et des tags
- Prise en charge native des formules mathématiques avec syntaxe LaTeX via MathJax
- Prise en charge native des diagrammes basés sur Mermaid
- Prise en charge des commentaires via Disqus, Giscus, etc.
- Prise en charge de Google Analytics, GoatCounter
- Thèmes clair et sombre disponibles
- Au moment du changement de thème, MathJax et Mermaid n'étaient pas nativement pris en charge par Minimal Mistakes et nécessitaient une personnalisation, alors que Chirpy les intègre nativement.
- Surtout, le design est élégant. Minimal Mistakes est épuré mais a une certaine rigidité qui conviendrait mieux à une documentation technique officielle ou à un portfolio, tandis que Chirpy offre un design qui n'a rien à envier aux plateformes de blogs commerciales comme Tistory, Medium ou velog.

## 3. Création du dépôt GitHub, construction et déploiement
Je décris ici le processus basé sur le thème Chirpy Jekyll actuellement utilisé (12024.06), en supposant que Git est déjà installé.  
Référez-vous au [guide d'installation officiel de Jekyll](https://jekyllrb.com/docs/installation/) et à la [page officielle du thème Chirpy Jekyll](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Installation de Ruby & Jekyll
Installez Ruby et Jekyll selon votre système d'exploitation en suivant le [guide d'installation officiel de Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Création du dépôt GitHub
La [page officielle du thème Chirpy Jekyll](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) présente deux méthodes :
1. Utiliser la gemme "jekyll-theme-chirpy" pour les fichiers principaux et le modèle [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) pour les autres ressources
  - Avantage : Facilité de mise à niveau des versions.
  - Inconvénient : Personnalisation limitée.
2. Forker le dépôt [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) pour votre blog
  - Avantage : Liberté totale de personnalisation en modifiant directement le code.
  - Inconvénient : Pour mettre à niveau, il faut fusionner le [dernier tag upstream du dépôt original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), ce qui peut créer des conflits avec vos personnalisations.

J'ai choisi la méthode 1. Le thème Chirpy est déjà très complet et la plupart des utilisateurs n'ont pas besoin de personnalisations majeures. De plus, comme le développement et l'amélioration des fonctionnalités sont toujours très actifs en 12024, les avantages de suivre l'upstream original l'emportent sur ceux de la personnalisation directe. Le guide officiel du thème Chirpy recommande également la méthode 1 pour la majorité des utilisateurs.

### 3-3. Configuration principale
Appliquez les paramètres nécessaires dans les fichiers `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} et `_data/share.yml`{: .filepath} à la racine du répertoire. Les commentaires sont bien rédigés et les paramètres sont intuitifs, donc faciles à appliquer. Les configurations qui nécessitent des actions externes incluent l'enregistrement du code d'authentification pour Google Search Console et l'intégration d'outils comme Google Analytics ou GoatCounter, mais ces procédures ne sont pas très complexes et ne sont pas le sujet principal de cet article.

### 3-4. Construction locale
Bien que ce ne soit pas obligatoire, vous pourriez vouloir vérifier à quoi ressemblera votre site après avoir écrit un nouveau post ou effectué des modifications. Pour cela, ouvrez un terminal dans le répertoire racine de votre dépôt local et exécutez :
```console
$ bundle exec jekyll s
```
Après quelques secondes, le site sera construit localement et vous pourrez voir le résultat à l'adresse <http://127.0.0.1:4000>.

### 3-5. Déploiement
Deux méthodes sont possibles :
1. Utiliser GitHub Actions (pour l'hébergement sur GitHub Pages)
  - Si vous utilisez GitHub Free Plan, le dépôt doit rester public
  - Sur la page GitHub de votre dépôt, allez dans l'onglet *Settings*, puis dans la barre de navigation gauche, cliquez sur *Code and automation > Pages* et sélectionnez l'option **GitHub Actions** dans la section **Source**
  - Une fois configuré, le workflow *Build and Deploy* s'exécutera automatiquement à chaque nouveau commit poussé
2. Construction manuelle et déploiement (pour d'autres services d'hébergement ou auto-hébergement)
  - Exécutez la commande suivante pour construire le site
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Téléchargez le résultat de la construction situé dans le répertoire `_site` sur votre serveur

## 4. Rédaction d'articles
Le [guide de rédaction d'articles](https://chirpy.cotes.page/posts/write-a-new-post/) du thème Chirpy documente bien les méthodes et options disponibles. Il offre diverses fonctionnalités au-delà de ce qui est décrit ici, donc référez-vous à la documentation officielle si nécessaire. Voici les points essentiels à garder à l'esprit pour chaque publication.

### Création du fichier markdown
- Format du nom : `YYYY-MM-DD-TITLE.md`{: .filepath}
- Emplacement : répertoire `_posts`{: .filepath}

### Rédaction du Front Matter
La première partie du fichier markdown doit contenir un Front Matter correctement rédigé.
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
- **description** : Résumé. Si non spécifié, une partie du contenu sera automatiquement utilisée, mais il est recommandé de rédiger manuellement cette balise meta pour l'optimisation des moteurs de recherche (SEO). Une longueur de 135 à 160 caractères en alphabet latin ou 80 à 110 caractères en coréen est appropriée.
- **date** : Date et heure exactes de rédaction avec fuseau horaire (facultatif, si omis, la date de création ou de modification du fichier sera automatiquement utilisée)
- **categories** : Classification par catégories de l'article
- **tags** : Classification par tags de l'article
- **image** : Insertion d'une image d'aperçu en haut de l'article
  - **path** : Chemin du fichier image
  - **alt** : Texte alternatif (facultatif)
- **toc** : Utilisation de la table des matières dans la barre latérale droite, valeur par défaut `true`
- **comments** : Pour spécifier explicitement l'utilisation des commentaires pour un article individuel, indépendamment des paramètres par défaut du site
- **math** : Activation de la fonction d'expression mathématique basée sur [MathJax](https://www.mathjax.org/), désactivée par défaut (`false`) pour les performances
- **mermaid** : Activation de la fonction de diagramme basée sur [Mermaid](https://github.com/mermaid-js/mermaid), désactivée par défaut (`false`)

## 5. Mise à niveau

Je décris ici le processus en supposant que vous avez choisi la méthode 1 dans la section [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-création-du-dépôt-github). Si vous avez choisi la méthode 2, vous devrez fusionner manuellement le dernier tag upstream.

1. Modifiez le fichier `Gemfile`{: .filepath} pour spécifier la nouvelle version de la gemme "jekyll-theme-chirpy".
2. Pour les mises à niveau majeures, les fichiers essentiels non inclus dans la gemme "jekyll-theme-chirpy" et les options de configuration peuvent également avoir changé. Dans ce cas, vérifiez les modifications avec l'API GitHub ci-dessous et appliquez-les manuellement.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
