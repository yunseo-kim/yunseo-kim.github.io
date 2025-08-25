---
title: Zusammenfassung der GitHub Markdown-Syntax
description: Was ist Markdown? Eine Zusammenfassung der wichtigsten GitHub Flavored Markdown-Syntax für das Hosten von Blogs mit GitHub Pages.
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Um GitHub Pages zu nutzen, ist es notwendig, die **Markdown**-Syntax zu kennen.
Dieser Beitrag wurde unter Bezugnahme auf die offiziellen GitHub-Dokumente [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) und [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) verfasst.

## 1. Was ist Markdown?
> **Markdown** ist eine leichtgewichtige Auszeichnungssprache, die auf reinem Text basiert. Sie wird verwendet, um formatierte Dokumente mit einfachem Text zu erstellen, und zeichnet sich durch eine einfachere und unkompliziertere Syntax im Vergleich zu herkömmlichen Auszeichnungssprachen aus. Da sie leicht in formatierte Dokumente wie HTML und Rich-Text-Format (RTF) umgewandelt werden kann, wird sie häufig für README-Dateien, die mit Anwendungssoftware verteilt werden, oder für Online-Beiträge verwendet.  
> John Gruber hat im Jahr 12004 des [Holozän-Kalenders](https://en.wikipedia.org/wiki/Holocene_calendar) in bedeutender Zusammenarbeit mit Aaron Swartz bezüglich der Syntax die Sprache Markdown entwickelt. Das Ziel war es, den Menschen zu ermöglichen, in einem leicht les- und schreibbaren reinen Textformat zu schreiben, das optional in strukturell gültiges XHTML (oder HTML) umgewandelt werden kann.

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown-Syntax
Da es keinen festgelegten Standard für Markdown gibt, kann die detaillierte Syntax je nach Anwendungsfall leicht variieren. Die hier zusammengefasste Markdown-Syntax basiert auf [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Zeilenumbrüche und Absätze
In Markdown wird ein einfacher Zeilenumbruch (einmaliges Drücken der Eingabetaste) nicht als Zeilenumbruch interpretiert.
~~~
Erster Satz.
Zweiter Satz.
Dritter Satz.
~~~
Erster Satz.
Zweiter Satz.
Dritter Satz.

Ein Zeilenumbruch wird durch die Eingabe von zwei oder mehr Leerzeichen am Ende einer Zeile erzeugt.
~~~
Erster Satz.  
Zweiter Satz.  
Dritter Satz.
~~~
Erster Satz.  
Zweiter Satz.  
Dritter Satz.

Absätze werden durch eine Leerzeile (zweimaliges Drücken der Eingabetaste) voneinander getrennt.
~~~
Ein Absatz.

Ein anderer Absatz.
~~~
Ein Absatz.

Ein anderer Absatz.

### 2.2. Überschriften (Headers)
Es gibt insgesamt sechs Ebenen.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
Das H1-Tag sollte prinzipiell nur einmal pro Seite verwendet werden, daher wird es beim Verfassen von Beiträgen oder Dokumenten selten direkt geschrieben.

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

### 2.4. Zitate
Wird mit \> erstellt.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Code-Blöcke
Wird mit \``` oder \~~~ erstellt.
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

Man kann auch die Programmiersprache angeben, um die Syntaxhervorhebung zu aktivieren.
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

Es können auch relative Links verwendet werden, die auf andere Dateien im Repository verweisen. Die Verwendung ist die gleiche wie im Terminal.
```
[README](../README.md)
```

### 2.7. Ungeordnete Listen
Wird mit \- oder \* erstellt.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Geordnete Listen
Wird mit Zahlen erstellt.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Verschachtelte Listen
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Aufgabenlisten
Um eine Aufgabenliste zu erstellen, fügen Sie \[ ] vor jeden Punkt hinzu.
Um eine erledigte Aufgabe zu markieren, verwenden Sie \[x].
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
Syntax: ![(optional, empfohlen)Bildbeschreibung](URL){(optional)Zusatzoptionen}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tabellen erstellen
Tabellen können mit | und - erstellt werden.
Vor der Tabelle muss eine Leerzeile stehen, damit sie korrekt angezeigt wird.
Es müssen mindestens drei - verwendet werden, damit sie korrekt erkannt wird.
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
