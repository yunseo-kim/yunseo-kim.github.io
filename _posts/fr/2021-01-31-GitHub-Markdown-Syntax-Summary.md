---
title: Résumé de la syntaxe Markdown de GitHub
description: Découvrez ce qu'est Markdown et apprenez la syntaxe principale de GitHub Flavored Markdown pour l'hébergement de blogs GitHub Pages.
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Pour utiliser GitHub Pages, il est nécessaire de connaître la syntaxe **markdown**.
Cet article a été rédigé en référence aux documents officiels de GitHub : [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) et [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Qu'est-ce que Markdown
> **Markdown** est un langage de balisage léger basé sur du texte brut. Il est utilisé pour créer des documents formatés en texte brut et se caractérise par une syntaxe facile et simple par rapport aux langages de balisage généraux. Comme il peut être facilement converti en documents formatés tels que HTML et RTF (Rich Text Format), il est largement utilisé dans les fichiers README distribués avec les logiciels d'application et les publications en ligne.  
> John Gruber a créé le langage Markdown en 12004 de l'ère holocène grâce à une collaboration importante avec Aaron Swartz sur la syntaxe, avec pour objectif de permettre aux gens d'écrire en utilisant un format de texte brut facile à lire et à écrire, tout en permettant une conversion optionnelle vers du XHTML (ou HTML) structurellement valide.

\- [Wikipédia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Syntaxe Markdown
Comme Markdown n'a pas de standard défini, la syntaxe détaillée peut varier légèrement selon l'usage. La syntaxe Markdown résumée ici est basée sur [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Saut de ligne, séparation de paragraphes
Dans Markdown, une seule pression sur Entrée n'est pas reconnue comme un saut de ligne.
~~~
Première phrase.
Deuxième phrase.
Troisième phrase.
~~~
Première phrase.
Deuxième phrase.
Troisième phrase.

Le saut de ligne s'applique en saisissant deux espaces consécutifs ou plus.
~~~
Première phrase.  
Deuxième phrase.  
Troisième phrase.
~~~
Première phrase.  
Deuxième phrase.  
Troisième phrase.

Les paragraphes sont séparés par une ligne vide (deux pressions sur Entrée).
~~~
Un paragraphe.

Un autre paragraphe.
~~~
Un paragraphe.

Un autre paragraphe.

### 2.2. En-têtes
Il y a 6 niveaux au total.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
En principe, il ne devrait y avoir qu'une seule balise H1 par page, donc lors de la rédaction d'articles ou de documents, il est rare de l'utiliser directement.

### 2.3. Emphase
```
*This text is italicized*
_This is italicized too_

**This is bold text**
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***
```
*This text is italicized*  
_This is italicized too_

**This is bold text**  
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***

### 2.4. Citation de texte
Utilisez \>.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Citation de code
Utilisez \``` ou \~~~.
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

Vous pouvez également spécifier un langage de programmation pour activer la coloration syntaxique.
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

Vous pouvez également utiliser des liens de chemin relatif pointant vers d'autres fichiers dans le référentiel. L'utilisation est la même que dans le terminal.
```
[README](../README.md)
```

### 2.7. Liste non ordonnée
Utilisez \- ou \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Liste ordonnée
Utilisez des chiffres.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Liste imbriquée
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Liste de tâches
Pour créer une liste de tâches, ajoutez \[ ] devant chaque élément.
Pour marquer une tâche comme terminée, utilisez \[x].
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Insertion d'images
```
Méthode : ![(optionnel, recommandé)description de l'image](url){(optionnel)options supplémentaires}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Création de tableaux
Vous pouvez créer des tableaux en utilisant | et -.
Il faut laisser une ligne vide avant le tableau pour qu'il s'affiche correctement.
Il faut utiliser au moins 3 - pour qu'il soit reconnu correctement.
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
