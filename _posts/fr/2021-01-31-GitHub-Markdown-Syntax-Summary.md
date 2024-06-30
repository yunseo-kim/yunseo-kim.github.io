---
title: "Résumé de la syntaxe Markdown de GitHub"
description: >-
  Nous avons examiné ce qu'est Markdown et résumé les principales syntaxes Markdown basées sur GitHub Flavored Markdown pour l'hébergement de blogs GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
toc: true
toc_sticky: true
---

Pour utiliser GitHub Pages, il est nécessaire de connaître la syntaxe **markdown**.
Cet article a été rédigé en se référant aux documents officiels de GitHub [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) et [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Qu'est-ce que Markdown
> **Markdown** est un langage de balisage léger basé sur du texte brut. Il est utilisé pour créer des documents formatés en texte brut et se caractérise par une syntaxe plus simple et plus facile que les langages de balisage ordinaires. Il est largement utilisé pour les fichiers README distribués avec les logiciels d'application et les publications en ligne car il peut être facilement converti en documents formatés tels que HTML et Rich Text Format (RTF).
>> John Gruber a créé le langage Markdown en 2004 avec une collaboration significative d'Aaron Swartz sur la syntaxe, dans le but de permettre aux gens d'écrire en utilisant un format de texte brut facile à lire et à écrire, avec la possibilité optionnelle de le convertir en XHTML (ou HTML) structurellement valide.

-[Wikipédia, Markdown](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4)

## 2. Syntaxe Markdown
Comme il n'existe pas de norme établie pour Markdown, la syntaxe détaillée peut varier légèrement selon l'utilisation. La syntaxe Markdown résumée ici est basée sur [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Saut de ligne, séparation de paragraphe
Dans Markdown, appuyer une fois sur la touche Entrée n'est pas reconnu comme un saut de ligne.
~~~
Première phrase.
Deuxième phrase.
Troisième phrase.
~~~
Première phrase.
Deuxième phrase.
Troisième phrase.

Le saut de ligne est appliqué en entrant deux espaces consécutifs ou plus.
~~~
Première phrase.  
Deuxième phrase.  
Troisième phrase.
~~~
Première phrase.  
Deuxième phrase.  
Troisième phrase.

Les paragraphes sont séparés par une ligne vide (appuyer deux fois sur la touche Entrée).
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
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6

### 2.3. Accentuation
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

Vous pouvez également activer la mise en évidence de la syntaxe en spécifiant un langage de programmation.
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

Vous pouvez également utiliser des liens de chemin relatif pointant vers d'autres fichiers du dépôt. L'utilisation est la même que dans le terminal.
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

### 2.11. Insertion d'image
```
Méthode : ![(Optionnel)Description de l'image](url){(Optionnel)Options supplémentaires}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Création de tableau
Vous pouvez créer un tableau en utilisant | et -.
Laissez une ligne vide avant le tableau pour qu'il s'affiche correctement.
Utilisez au moins trois - pour que le tableau soit correctement reconnu.
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