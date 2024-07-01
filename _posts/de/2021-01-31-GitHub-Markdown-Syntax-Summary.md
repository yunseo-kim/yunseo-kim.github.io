---
title: "Zusammenfassung der GitHub Markdown-Syntax"
description: >-
  Wir erfahren, was Markdown ist, und fassen die wichtigsten Markdown-Syntaxregeln basierend auf GitHub Flavored Markdown für das Hosting von GitHub Pages-Blogs zusammen.
categories:
  - Blogging
tags:
  - Jekyll
toc: true
toc_sticky: true
---

Für die Nutzung von GitHub Pages ist es notwendig, die **Markdown**-Syntax zu kennen.
Dieser Beitrag wurde unter Bezugnahme auf die offiziellen GitHub-Dokumente [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) und [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) verfasst.

## 1. Was ist Markdown?
> **Markdown** ist eine leichtgewichtige Auszeichnungssprache auf Basis von Klartext. Sie wird verwendet, um formatierte Dokumente mit normalem Text zu erstellen und zeichnet sich durch eine einfachere und unkompliziertere Syntax im Vergleich zu herkömmlichen Auszeichnungssprachen aus. Da sie leicht in HTML und Rich Text Format (RTF) umgewandelt werden kann, wird sie häufig für README-Dateien, die mit Anwendungssoftware verteilt werden, oder für Online-Beiträge verwendet.
>> John Gruber entwickelte die Markdown-Sprache im Jahr 2004 in bedeutender Zusammenarbeit mit Aaron Swartz in Bezug auf die Syntax. Das Ziel war es, Menschen zu ermöglichen, ein leicht lesbares und schreibbares Klartext-Format zu verwenden, das optional in strukturell gültiges XHTML (oder HTML) umgewandelt werden kann.

-[Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown-Syntax
Da es keinen festgelegten Standard für Markdown gibt, können sich die detaillierten Syntaxregeln je nach Anwendung leicht unterscheiden. Die hier zusammengefasste Markdown-Syntax basiert auf [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Zeilenumbruch, Absatztrennung
In Markdown wird ein einmaliges Drücken der Eingabetaste nicht als Zeilenumbruch erkannt.
~~~
Erster Satz.
Zweiter Satz.
Dritter Satz.
~~~
Erster Satz.
Zweiter Satz.
Dritter Satz.

Ein Zeilenumbruch wird angewendet, wenn zwei oder mehr aufeinanderfolgende Leerzeichen eingegeben werden.
~~~
Erster Satz.  
Zweiter Satz.  
Dritter Satz.
~~~
Erster Satz.  
Zweiter Satz.  
Dritter Satz.

Absätze werden durch eine Leerzeile (zweimaliges Drücken der Eingabetaste) getrennt.
~~~
Ein Absatz.

Ein anderer Absatz.
~~~
Ein Absatz.

Ein anderer Absatz.

### 2.2. Überschriften (Headers)
Es gibt insgesamt 6 Ebenen.
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

### 2.3. Hervorhebung
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

### 2.4. Textzitate
Verwenden Sie \>.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Codezitate
Verwenden Sie \``` oder \~~~.
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

Sie können auch eine Programmiersprache angeben, um die Syntaxhervorhebung zu aktivieren.
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

### 2.6. Links
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

Sie können auch relative Pfad-Links verwenden, die auf andere Dateien im Repository verweisen. Die Verwendung ist die gleiche wie im Terminal.
```
[README](../README.md)
```

### 2.7. Ungeordnete Liste
Verwenden Sie \- oder \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Geordnete Liste
Verwenden Sie Zahlen.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Verschachtelte Liste
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Aufgabenliste
Um eine Aufgabenliste zu erstellen, fügen Sie \[ ] vor jedem Element hinzu.
Um eine erledigte Aufgabe anzuzeigen, verwenden Sie \[x].
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Bilder einfügen
```
Methode: ![(Optional)Bildbeschreibung](url){(Optional)Zusatzoptionen}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tabellen erstellen
Verwenden Sie | und -, um Tabellen zu erstellen.
Lassen Sie eine Leerzeile vor der Tabelle, damit sie korrekt angezeigt wird.
Verwenden Sie mindestens drei -, damit sie korrekt erkannt wird.
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