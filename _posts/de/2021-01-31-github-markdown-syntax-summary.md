---
title: GitHub Markdown: Syntax-Überblick
description: "Was ist Markdown? Überblick über die wichtigsten Syntaxelemente nach GitHub Flavored Markdown (GFM) – mit Tipps für GitHub Pages und Blog-Hosting."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Für die Nutzung von GitHub Pages sollte man die **Markdown**-Syntax kennen.
Dieser Beitrag orientiert sich an den offiziellen GitHub-Dokumenten [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) und [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Was ist Markdown?
> **Markdown** ist eine leichte Auszeichnungssprache auf Basis von Plaintext. Sie wird verwendet, um formatierte Dokumente mit einfachem Text zu verfassen; im Vergleich zu anderen Auszeichnungssprachen ist ihre Syntax besonders leicht und übersichtlich. Da sich Markdown einfach in formatierte Dokumente wie HTML und Rich Text (RTF) umwandeln lässt, wird es häufig für mit Software ausgelieferte README-Dateien und für Online-Beiträge verwendet.  
> John Gruber entwickelte im Jahr 12004 des [Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar) die Sprache Markdown in enger Zusammenarbeit mit Aaron Swartz in Bezug auf die Syntax, mit dem Ziel, dass Menschen in einem gut les- und schreibbaren Plaintext-Format schreiben und diesen bei Bedarf in strukturell valides XHTML (oder HTML) konvertieren können.

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown-Syntax
Markdown hat keinen verbindlichen Standard; Details können je nach Einsatzort variieren. Die hier zusammengefasste Syntax folgt dem Standard von [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Zeilenumbruch und Absätze
Ein einmaliges Drücken der Eingabetaste erzeugt keinen Zeilenumbruch.
~~~
Erster Satz.
Zweiter Satz.
Dritter Satz.
~~~
Erster Satz.
Zweiter Satz.
Dritter Satz.

Ein Zeilenumbruch wird erzeugt, indem am Zeilenende mindestens zwei Leerzeichen eingefügt werden.
~~~
Erster Satz.  
Zweiter Satz.  
Dritter Satz.
~~~
Erster Satz.  
Zweiter Satz.  
Dritter Satz.

Absätze werden durch eine Leerzeile (zweimal Enter) getrennt.
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
Ein H1-Tag sollte grundsätzlich nur einmal pro Seite vorkommen; beim Schreiben von Posts oder Dokumenten wird es daher in der Regel nicht direkt verwendet.

### 2.3. Hervorhebungen
```
*Dieser Text ist kursiv*
_Dies ist ebenfalls kursiv_

**Dies ist fett**
__Das ist auch fett__

~~Das war ein Fehler~~

_Man **kann** sie kombinieren_

***Dieser gesamte Text ist wichtig***
```
*Dieser Text ist kursiv*  
_Dies ist ebenfalls kursiv_

**Dies ist fett**  
__Das ist auch fett__

~~Das war ein Fehler~~

_Man **kann** sie kombinieren_

***Dieser gesamte Text ist wichtig***

### 2.4. Blockzitate
\> verwenden.
```
> Dies ist ein erstes Blockzitat.
>> Dies ist ein zweites Blockzitat.
>>> Dies ist ein drittes Blockzitat.
```
> Dies ist ein erstes Blockzitat.
>> Dies ist ein zweites Blockzitat.
>>> Dies ist ein drittes Blockzitat.

### 2.5. Codeblöcke
\``` oder \~~~ verwenden.
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

Sie können auch eine Programmiersprache angeben, um Syntaxhervorhebung zu aktivieren.
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

Sie können auch relative Links verwenden, die auf andere Dateien im Repository zeigen. Die Verwendung entspricht der im Terminal.
```
[README](../README.md)
```

### 2.7. Unsortierte Listen
\- oder \* verwenden.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Geordnete Listen
Zahlen verwenden.
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

### 2.10. Aufgabenliste
Fügen Sie vor jedem Element \[ ] hinzu, um eine Aufgabenliste zu erstellen.
Verwenden Sie \[x], um erledigte Aufgaben zu markieren.
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
Methode: ![(optional, empfohlen) Bildbeschreibung](url){(optional) Zusatzoptionen}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tabellen erstellen
Mit | und - können Tabellen erstellt werden.
Vor der Tabelle muss eine Leerzeile stehen, damit sie korrekt angezeigt wird.
Es müssen mindestens drei - verwendet werden, damit die Tabelle erkannt wird.
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
