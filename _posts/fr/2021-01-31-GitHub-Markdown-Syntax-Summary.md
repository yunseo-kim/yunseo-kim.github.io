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
Cet article a été rédigé en se référant aux documents officiels de GitHub [Maîtriser Markdown](https://guides.github.com/features/mastering-markdown/) et [Syntaxe de base pour l'écriture et le formatage](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Qu'est-ce que Markdown
> **Markdown** est un langage de balisage léger basé sur du texte brut. Il est utilisé pour créer des documents formatés en texte brut et se caractérise par une syntaxe plus simple et plus facile que les langages de balisage ordinaires. Il est largement utilisé pour les fichiers README distribués avec les logiciels d'application et les publications en ligne car il peut être facilement converti en documents formatés tels que HTML et Rich Text Format (RTF).
>> John Gruber a créé le langage Markdown en 2004 avec une collaboration significative d'Aaron Swartz sur la syntaxe, dans le but de permettre aux gens d'écrire en utilisant un format de texte brut facile à lire et à écrire, avec la possibilité optionnelle de le convertir en XHTML (ou HTML) structurellement valide.

-[Wikipédia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Syntaxe Markdown
Comme il n'existe pas de norme établie pour Markdown, la syntaxe détaillée peut varier légèrement selon l'utilisation. La syntaxe Markdown résumée ici est basée sur [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Saut de ligne, séparation de paragraphe
Dans Markdown, une seule touche Entrée n'est pas reconnue comme un saut de ligne.
~~~
Première phrase.
Deuxième phrase.
Troisième phrase.
~~~
Première phrase.
Deuxième phrase.
Troisième phrase.

Le saut de ligne s'applique lorsque vous entrez deux espaces consécutifs ou plus.
~~~
Première phrase.  
Deuxième phrase.  
Troisième phrase.
~~~
Première phrase.  
Deuxième phrase.  
Troisième phrase.

Les paragraphes sont séparés par une ligne vide (deux touches Entrée).
~~~
Un paragraphe.

Un autre paragraphe.
~~~
Un paragraphe.

Un autre paragraphe.

### 2.2. En-têtes
Il y a 6 niveaux au total.
```
# Ceci est un H1
## Ceci est un H2
### Ceci est un H3
#### Ceci est un H4
##### Ceci est un H5
###### Ceci est un H6
```
# Ceci est un H1
## Ceci est un H2
### Ceci est un H3
#### Ceci est un H4
##### Ceci est un H5
###### Ceci est un H6

### 2.3. Accentuation
```
*Ce texte est en italique*
_Ceci est aussi en italique_

**Ce texte est en gras**
__Ce texte est aussi en gras__

~~Ce texte était une erreur~~

_Vous **pouvez** les combiner_

***Tout ce texte est important***
```
*Ce texte est en italique*  
_Ceci est aussi en italique_

**Ce texte est en gras**  
__Ce texte est aussi en gras__

~~Ce texte était une erreur~~

_Vous **pouvez** les combiner_

***Tout ce texte est important***

### 2.4. Citation de texte
On utilise \>.
```
> Ceci est une première citation.
>> Ceci est une deuxième citation.
>>> Ceci est une troisième citation.
```
> Ceci est une première citation.
>> Ceci est une deuxième citation.
>>> Ceci est une troisième citation.

### 2.5. Citation de code
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

On peut également activer la coloration syntaxique en spécifiant le langage de programmation.
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

On peut également utiliser des liens relatifs pointant vers d'autres fichiers du dépôt. L'utilisation est la même que dans le terminal.
```
[README](../README.md)
```

### 2.7. Liste non ordonnée
On utilise \- ou \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Liste ordonnée
On utilise des chiffres.
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
1. Premier élément de liste
   - Premier élément de liste imbriquée
     - Deuxième élément de liste imbriquée
```
1. Premier élément de liste
   - Premier élément de liste imbriquée
     - Deuxième élément de liste imbriquée

### 2.10. Liste de tâches
Pour créer une liste de tâches, ajoutez \[ ] devant chaque élément.
Pour marquer une tâche comme terminée, utilisez \[x].
```
- [x] Terminer mes modifications
- [ ] Pousser mes commits vers GitHub
- [ ] Ouvrir une pull request
```
- [x] Terminer mes modifications
- [ ] Pousser mes commits vers GitHub
- [ ] Ouvrir une pull request

### 2.11. Insertion d'image
```
Méthode : ![(Optionnel)Description de l'image](url){(Optionnel)Options supplémentaires}
![Logo GitHub](/images/logo.png)
![Logo GitHub](/images/logo.png){: .align-center}
![Logo GitHub](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Création de tableau
On peut créer un tableau en utilisant | et -.
Il faut laisser une ligne vide avant le tableau pour qu'il s'affiche correctement.
Il faut utiliser au moins trois - pour que le tableau soit correctement reconnu.
```

| Aligné à gauche | Centré | Aligné à droite |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Aligné à gauche | Centré | Aligné à droite |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |