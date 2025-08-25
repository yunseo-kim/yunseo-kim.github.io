---
title: Créer et gérer un blog GitHub Pages
description: Différences entre pages web statiques et dynamiques, aperçu des générateurs de sites statiques, et tutoriel pour héberger un blog Jekyll sur GitHub Pages.
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

Je me suis mis à héberger mon blog sur GitHub Pages avec Jekyll depuis le début de 12021. Comme je n’avais pas correctement consigné la procédure d’installation lors de la mise en place, la maintenance s’est avérée un peu délicate par la suite. J’ai donc décidé de résumer ici, même brièvement, le processus d’installation et la façon de maintenir le site.  

(+ mise à jour du contenu 12024.12)

## 1. Générateurs de sites statiques et hébergement web
### 1-1. Pages web statiques vs pages web dynamiques
#### Page web statique
- Page web qui transmet à l’utilisateur les données stockées sur le serveur telles quelles
- Le serveur web renvoie une page préenregistrée correspondant à la requête de l’utilisateur
- L’utilisateur voit la même page tant que les données sur le serveur ne changent pas
- Comme il suffit d’envoyer le fichier demandé, aucune opération supplémentaire n’est nécessaire, la réponse est généralement rapide
- Composée de fichiers simples, elle ne requiert qu’un serveur web, ce qui réduit les coûts de mise en place
- Ne montrant que des informations préstockées, les services offerts sont limités
- L’ajout, la modification et la suppression de données doivent être effectués manuellement par l’administrateur
- Structure aisément explorée par les moteurs de recherche, donc relativement plus favorable au référencement (SEO)

#### Page web dynamique
- Page web qui transmet des données traitées par des scripts à partir des données stockées sur le serveur
- Le serveur web interprète la requête, traite les données puis renvoie une page web générée
- L’utilisateur voit des pages qui varient selon la situation, l’heure, la requête, etc.
- Le traitement de scripts pour générer la page induit une réponse relativement plus lente
- La présence d’un serveur d’applications, en plus du serveur web, engendre des coûts supplémentaires
- La combinaison dynamique de diverses informations permet une grande variété de services
- Selon la structure de la page, l’utilisateur peut ajouter, modifier ou supprimer des données directement dans le navigateur

### 1-2. Générateur de site statique (SSG)
- Outil qui génère des pages web statiques à partir de données brutes (généralement des fichiers texte au format Markdown) et de gabarits prédéfinis
- Inutile d’écrire chaque page HTML à la main : on rédige en Markdown et l’outil automatise la construction et le déploiement du site
- p. ex. : Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Service d’hébergement gratuit de pages web statiques proposé par GitHub
- Par compte, on peut héberger une page personnelle principale, et créer/héberger sans limite des pages de documentation par dépôt
- En créant un dépôt nommé selon le format “{username}.github.io”, on peut pousser directement les pages HTML construites, ou utiliser GitHub Actions pour la construction et le déploiement
- Si vous possédez un domaine, vous pouvez le lier dans les paramètres et utiliser son adresse à la place du domaine par défaut “{username}.github.io”

## 2. Choix du SSG et du thème

### 2-1. Pourquoi j’ai choisi Jekyll
Il existe plusieurs SSG comme Jekyll, Hugo, Gatsby, mais j’ai décidé d’utiliser Jekyll. Voici mes critères et les raisons de ce choix.
- Peut-on minimiser les essais/erreurs inutiles et se concentrer sur l’écriture et l’exploitation du blog ?
  - Jekyll est officiellement pris en charge par GitHub Pages. Certes, Hugo et Gatsby peuvent aussi être hébergés sur GitHub Pages, et des services comme Netlify sont des alternatives, mais pour un blog personnel de cette taille, le choix du SSG, la vitesse de build ou les performances importent peu. J’ai donc privilégié une solution facile à maintenir et bien documentée.
  - Jekyll a aussi un historique de développement plus long que Hugo ou Gatsby. La documentation est plus riche, et en cas de problème, la quantité de ressources disponibles est nettement supérieure.
- Les thèmes et plugins disponibles sont-ils variés ?
  - Même avec un SSG, créer tous les gabarits soi-même est fastidieux et prend du temps—sans réelle nécessité. Il existe déjà de très bons thèmes publics ; il suffit d’adopter celui qui convient.
  - J’utilise surtout C et Python, et je ne maîtrise pas très bien Ruby (Jekyll) ni Go (Hugo). Je voulais donc tirer parti des thèmes et plugins existants.
  - J’ai trouvé très vite un thème qui me plaisait chez Jekyll, alors que, pour Hugo ou Gatsby, les thèmes adaptés à un blog personnel semblaient moins nombreux. Comme dit plus haut, la bonne intégration avec GitHub Pages (souvent choisi pour les blogs de dev) et la maturité du projet jouent sans doute en faveur de Jekyll.

### 2-2. Choix du thème
#### Minimal Mistakes (12021.01 - 12022.04)
- Dépôt GitHub : <https://github.com/mmistakes/minimal-mistakes>
- Page de démonstration : <https://mmistakes.github.io/minimal-mistakes/>
- Thème utilisé pendant environ 1 an et 3 mois au lancement du blog
- Prise en charge des commentaires via Disqus, Discourse, utterances, etc.
- Prise en charge des catégories et des tags
- Prise en charge native de Google Analytics
- Skins prédéfinis sélectionnables
- J’ai ensuite découvert Chirpy, au design plus soigné et plus à mon goût. Même si Minimal Mistakes n’est pas le plus “joli”, pour un blog d’ingénieur, son design propre et sobre reste tout à fait convenable.

#### Thème Jekyll Chirpy (12022.04 - présent)
- Dépôt GitHub : <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Page de démonstration : <https://chirpy.cotes.page/>
- Thème que j’utilise depuis la migration en 12022.04
- Prise en charge des catégories multiples et des tags
- Prise en charge native des formules LaTeX via MathJax
- Prise en charge native des diagrammes via Mermaid
- Commentaires via Disqus, Giscus, etc.
- Prise en charge de Google Analytics et GoatCounter
- Thèmes clair et sombre
- Au moment de la migration, MathJax et Mermaid n’étaient pas pris en charge nativement par Minimal Mistakes, il fallait les ajouter en personnalisant. Chirpy les prend en charge d’emblée. Ce n’est pas une personnalisation difficile, mais c’est un petit plus.
- Surtout, le design est agréable. Minimal Mistakes est propre mais un peu rigide—plus adapté à une documentation de projet ou un portfolio. Chirpy, lui, n’a pas grand-chose à envier aux plateformes commerciales comme Tistory, Medium ou Velog.

## 3. Créer un dépôt GitHub, générer et déployer
Je décris ci-dessous en me basant sur le thème Chirpy Jekyll utilisé actuellement (12024.06), et en supposant Git déjà installé.  
Voir le [guide officiel d’installation de Jekyll](https://jekyllrb.com/docs/installation/) et la [page officielle du thème Jekyll Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Installer Ruby et Jekyll
Installez Ruby et Jekyll en fonction de votre système d’exploitation, conformément au [guide officiel d’installation de Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Création du dépôt GitHub
La [page officielle du thème Jekyll Chirpy](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) présente deux méthodes :
1. Utiliser la gem “jekyll-theme-chirpy” pour importer les fichiers cœur et tirer le reste des ressources du modèle [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Avantage : comme expliqué plus loin, l’application des mises à niveau est aisée.
  - Inconvénient : pour de très grosses personnalisations, cela peut être moins pratique.
2. Forker le dépôt [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) dans le dépôt de votre blog
  - Avantage : vous gérez tous les fichiers dans votre dépôt, ce qui facilite l’ajout de fonctionnalités non prises en charge en modifiant directement le code.
  - Inconvénient : pour appliquer une mise à niveau, il faut fusionner [la dernière balise upstream du dépôt original](https://github.com/cotes2020/jekyll-theme-chirpy/tags). Selon les cas, vos personnalisations peuvent entrer en conflit avec la nouvelle version ; il faudra alors résoudre ces conflits à la main.

J’ai opté pour la première méthode. Le thème Chirpy est très abouti et, pour la plupart des utilisateurs, il y a peu à personnaliser. En 12024, le projet est encore activement développé et amélioré, donc, sauf besoin de modifications lourdes, suivre rapidement l’upstream est plus avantageux que de multiplier les personnalisations locales. D’ailleurs, la documentation officielle recommande aussi la méthode 1 pour la majorité des utilisateurs.

### 3-3. Paramètres principaux
Appliquez les réglages nécessaires dans les fichiers `_config.yml`{: .filepath} à la racine, ainsi que `_data/contact.yml`{: .filepath} et `_data/share.yml`{: .filepath}. Les commentaires sont clairs et les paramètres intuitifs. Les seules opérations externes un peu distinctes sont l’ajout du code de vérification pour Google Search Console et l’intégration d’outils comme Google Analytics ou GoatCounter. Rien de très compliqué, et ce n’est pas le cœur de cet article, donc je n’entre pas dans les détails.

### 3-4. Construire en local
Ce n’est pas obligatoire, mais quand on ajoute un article ou qu’on modifie le site, on peut vouloir vérifier le rendu avant publication. Ouvrez un terminal à la racine du dépôt local et exécutez :
```console
$ bundle exec jekyll s
```
Après un court instant, le site est construit en local et consultable à l’adresse <http://127.0.0.1:4000>.

### 3-5. Déployer
Deux méthodes :
1. Utiliser GitHub Actions (si hébergé sur GitHub Pages)
  - Avec l’offre gratuite GitHub, le dépôt doit être public
  - Sur la page du dépôt GitHub, ouvrez l’onglet *Settings*, puis dans la barre de navigation de gauche, cliquez sur *Code and automation > Pages* et, dans la section **Source**, choisissez l’option **GitHub Actions**
  - Une fois configuré, le workflow *Build and Deploy* se lance automatiquement à chaque push
2. Construire et déployer soi-même (autre hébergeur ou auto‑hébergement)
  - Construire le site avec la commande suivante :
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Envoyer le résultat contenu dans le répertoire `_site` vers votre serveur

## 4. Rédiger des articles
Le [guide de rédaction d’un nouvel article](https://chirpy.cotes.page/posts/write-a-new-post/) du thème Chirpy est très bien documenté. Outre ce qui est décrit ici, de nombreuses options sont disponibles ; reportez-vous à la doc officielle si besoin. La syntaxe de base du GitHub Flavored Markdown est résumée dans un [article séparé](/posts/github-markdown-syntax-summary/). Ci-dessous, je récapitule les points à garder en tête à chaque publication.

### Créer le fichier Markdown
- Format du nom : `YYYY-MM-DD-TITLE.md`{: .filepath}
- Emplacement : répertoire `_posts`{: .filepath}

### Renseigner le Front Matter
Le fichier Markdown doit commencer par un Front Matter approprié.
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
  alt: texte alternatif de l’image
toc: true
comments: false
math: true
mermaid: true
---
```
- **title** : titre de l’article
- **description** : résumé. S’il n’est pas fourni, une portion du début du corps est utilisée automatiquement, mais pour le SEO il est recommandé de le rédiger explicitement. En alphabet latin, visez 135–160 caractères ; en coréen, 80–110 caractères.
- **date** : date et heure exactes de l’article, avec fuseau horaire (facultatif ; à défaut, la date de création ou de modification du fichier est détectée automatiquement)
- **categories** : catégorisation de l’article
- **tags** : tags appliqués à l’article
- **image** : image d’aperçu en haut de l’article
  - **path** : chemin de l’image
  - **alt** : texte alternatif (facultatif)
- **toc** : activer la table des matières dans la barre latérale droite ; `true` par défaut
- **comments** : permet d’activer/désactiver explicitement les commentaires pour l’article, indépendamment du réglage global du site
- **math** : activer l’affichage des formules via [MathJax](https://www.mathjax.org/) ; désactivé par défaut (`false`) pour préserver les performances
- **mermaid** : activer les diagrammes basés sur [Mermaid](https://github.com/mermaid-js/mermaid) ; désactivé par défaut (`false`)

## 5. Mise à niveau

En partant du principe que vous avez choisi la méthode 1 dans la [section 3-2](#3-2-création-du-dépôt-github). Si vous avez choisi la méthode 2, comme indiqué plus haut, il faudra fusionner la dernière balise upstream.

1. Modifiez le `Gemfile`{: .filepath} pour définir la nouvelle version de la gem “jekyll-theme-chirpy”.
2. Pour une mise à niveau majeure, des fichiers cœur non inclus dans la gem “jekyll-theme-chirpy” et des options de configuration peuvent aussi avoir changé. Dans ce cas, vérifiez les différences via l’API GitHub ci-dessous et appliquez-les manuellement.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
