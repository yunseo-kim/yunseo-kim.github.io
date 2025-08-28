---
title: "Résumé de la syntaxe Markdown GitHub"
description: "Qu’est-ce que Markdown ? Guide concis des principales syntaxes selon GitHub Flavored Markdown (GFM) pour écrire et publier un blog avec GitHub Pages."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Pour utiliser GitHub Pages, il est nécessaire de connaître la syntaxe **Markdown**.
Ce billet s’appuie sur la documentation officielle de GitHub, notamment [Maîtriser Markdown](https://guides.github.com/features/mastering-markdown/) et [Syntaxe d’écriture et de mise en forme de base](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Qu’est-ce que Markdown ?
> **Markdown** est un langage de balisage léger basé sur du texte brut. Il sert à rédiger des documents mis en forme à partir de texte simple et se caractérise par une syntaxe plus facile et plus concise que celle des langages de balisage classiques. Il se convertit aisément en documents formatés comme HTML ou RTF, et est donc largement utilisé pour les fichiers README distribués avec les logiciels ou pour les publications en ligne.  
> John Gruber a créé le langage Markdown en 12004 de l’[ère holocène](https://en.wikipedia.org/wiki/Holocene_calendar), en collaboration étroite sur la syntaxe avec Aaron Swartz, avec pour objectif de permettre d’écrire dans un format texte lisible et facile à saisir tout en offrant une conversion optionnelle vers du XHTML (ou HTML) structurellement valide.

\- [Wikipédia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Syntaxe Markdown
Markdown n’étant pas standardisé, les détails de la syntaxe peuvent varier selon l’environnement. La présente synthèse suit la référence [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Saut de ligne, séparation de paragraphes
Dans Markdown, appuyer une seule fois sur Entrée n’est pas interprété comme un saut de ligne.
~~~
첫째 문장.
둘째 문장.
셋째 문장.
~~~
첫째 문장.
둘째 문장.
셋째 문장.

Un saut de ligne s’obtient en ajoutant au moins deux espaces consécutifs en fin de ligne.
~~~
첫째 문장.  
둘째 문장.  
셋째 문장.
~~~
첫째 문장.  
둘째 문장.  
셋째 문장.

On sépare les paragraphes par une ligne vide (deux fois Entrée).
~~~
하나의 문단.

다른 문단.
~~~
하나의 문단.

다른 문단.

### 2.2. Titres (headers)
Il existe 6 niveaux.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
Le niveau H1 ne devrait en principe apparaître qu’une seule fois par page ; on l’emploie donc rarement directement dans un article ou un document.

### 2.3. Emphase
```
*Ce texte est en italique*
_Ceci est en italique aussi_

**Ceci est en gras**
__Ceci est en gras aussi__

~~Ceci était un texte erroné~~

_Vous **pouvez** les combiner_

***Tout ce texte est important***
```
*Ce texte est en italique*  
_Ceci est en italique aussi_

**Ceci est en gras**  
__Ceci est en gras aussi__

~~Ceci était un texte erroné~~

_Vous **pouvez** les combiner_

***Tout ce texte est important***

### 2.4. Citations (blockquote)
On utilise \>.
```
> Ceci est une première citation.
>> Ceci est une deuxième citation.
>>> Ceci est une troisième citation.
```
> Ceci est une première citation.
>> Ceci est une deuxième citation.
>>> Ceci est une troisième citation.

### 2.5. Blocs de code
On utilise \``` ou \~~~.
~~~
```
git status
git add
git commit
```
~~~
```
git status
git add
git commit
```

On peut préciser le langage pour activer la coloration syntaxique.
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

### 2.6. Liens
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

Vous pouvez aussi utiliser des liens relatifs pointant vers d’autres fichiers du dépôt. La syntaxe est la même qu’au terminal.
```
[README](../README.md)
```

### 2.7. Listes non ordonnées
On utilise \- ou \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Listes ordonnées
On utilise des chiffres.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Listes imbriquées
```
1. Premier élément de liste
   - Premier élément imbriqué
     - Deuxième élément imbriqué
```
1. Premier élément de liste
   - Premier élément imbriqué
     - Deuxième élément imbriqué

### 2.10. Listes de tâches
Pour créer une liste de tâches, ajoutez \[ ] devant chaque élément.
Pour marquer une tâche terminée, utilisez \[x].
```
- [x] Terminer mes modifications
- [ ] Pousser mes commits sur GitHub
- [ ] Ouvrir une pull request
```
- [x] Terminer mes modifications
- [ ] Pousser mes commits sur GitHub
- [ ] Ouvrir une pull request

### 2.11. Insertion d’images
```
Méthode : ![(optionnel, recommandé) description de l’image](url){(optionnel) options supplémentaires}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Création de tableaux
On peut créer des tableaux avec | et -.  
Laissez une ligne vide avant le tableau pour un affichage correct.  
Utilisez au moins 3 traits d’union pour une reconnaissance correcte.
```
 
| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
