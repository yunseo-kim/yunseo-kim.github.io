---
title: "GitHub Markdown-Syntax Zusammenfassung"
description: >-
  Wir erklären, was Markdown ist und fassen die wichtigsten Markdown-Syntaxregeln basierend auf GitHub Flavored Markdown für das Hosting von GitHub Pages Blogs zusammen.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---

Für die Nutzung von GitHub Pages ist es notwendig, die **Markdown**-Syntax zu kennen.
Dieser Beitrag wurde unter Bezugnahme auf die offiziellen GitHub-Dokumente [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) und [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) verfasst.

## 1. Was ist Markdown?
> **Markdown** ist eine leichtgewichtige Auszeichnungssprache, die auf normalem Text basiert. Sie wird verwendet, um formatierte Dokumente mit normalem Text zu erstellen und zeichnet sich durch eine einfachere und unkompliziertere Syntax im Vergleich zu herkömmlichen Auszeichnungssprachen aus. Da sie leicht in HTML und Rich Text Format (RTF) umgewandelt werden kann, wird sie häufig für README-Dateien, die mit Anwendungssoftware verteilt werden, oder für Online-Beiträge verwendet.
>> John Gruber entwickelte die Markdown-Sprache im Jahr 2004 in bedeutender Zusammenarbeit mit Aaron Swartz in Bezug auf die Syntax. Das Ziel war es, Menschen die Möglichkeit zu geben, in einem leicht lesbaren und schreibbaren Klartext-Format zu schreiben, das optional in strukturell gültiges XHTML (oder HTML) umgewandelt werden kann.

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
# Dies ist eine H1
## Dies ist eine H2
### Dies ist eine H3
#### Dies ist eine H4
##### Dies ist eine H5
###### Dies ist eine H6
```
Das H1-Tag sollte prinzipiell nur einmal pro Seite verwendet werden, daher wird es beim Verfassen von Beiträgen oder Dokumenten normalerweise nicht direkt verwendet.

### 2.3. Hervorhebung
```
*Dieser Text ist kursiv*
_Dieser Text ist auch kursiv_

**Dieser Text ist fett**
__Dieser Text ist auch fett__

~~Dieser Text war ein Fehler~~

_Du **kannst** sie kombinieren_

***Dieser gesamte Text ist wichtig***
```
*Dieser Text ist kursiv*  
_Dieser Text ist auch kursiv_

**Dieser Text ist fett**  
__Dieser Text ist auch fett__

~~Dieser Text war ein Fehler~~

_Du **kannst** sie kombinieren_

***Dieser gesamte Text ist wichtig***

### 2.4. Textzitate
Man verwendet \>.
```
> Dies ist ein erstes Blockzitat.
>> Dies ist ein zweites Blockzitat.
>>> Dies ist ein drittes Blockzitat.
```
> Dies ist ein erstes Blockzitat.
>> Dies ist ein zweites Blockzitat.
>>> Dies ist ein drittes Blockzitat.

### 2.5. Code-Zitate
Man verwendet \``` oder \~~~.
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

Man kann auch eine Programmiersprache angeben, um die Syntaxhervorhebung zu aktivieren.
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

Man kann auch relative Pfad-Links verwenden, die auf andere Dateien im Repository verweisen. Die Verwendung ist die gleiche wie im Terminal.
```
[README](../README.md)
```

### 2.7. Ungeordnete Liste
Man verwendet \- oder \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Geordnete Liste
Man verwendet Zahlen.
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
1. Erster Listenpunkt
   - Erster verschachtelter Listenpunkt
     - Zweiter verschachtelter Listenpunkt
```
1. Erster Listenpunkt
   - Erster verschachtelter Listenpunkt
     - Zweiter verschachtelter Listenpunkt

### 2.10. Aufgabenliste
Um eine Aufgabenliste zu erstellen, fügt man \[ ] vor jedem Element hinzu.
Um eine erledigte Aufgabe anzuzeigen, verwendet man \[x].
```
- [x] Meine Änderungen abschließen
- [ ] Meine Commits auf GitHub pushen
- [ ] Einen Pull Request öffnen
```
- [x] Meine Änderungen abschließen
- [ ] Meine Commits auf GitHub pushen
- [ ] Einen Pull Request öffnen

### 2.11. Bilder einfügen
```
Methode: ![(Optional)Bildbeschreibung](url){(Optional)Zusatzoptionen}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tabellen erstellen
Man kann Tabellen mit | und - erstellen.
Es muss eine leere Zeile vor der Tabelle gelassen werden, damit sie korrekt angezeigt wird.
Es müssen mindestens drei - verwendet werden, damit sie korrekt erkannt wird.
```

| Linksbündig | Zentriert | Rechtsbündig |
| :---        |   :---:   |         ---: |
| git status  | git status| git status   |
| git diff    | git diff  | git diff     |
```

| Linksbündig | Zentriert | Rechtsbündig |
| :---        |   :---:   |         ---: |
| git status  | git status| git status   |
| git diff    | git diff  | git diff     |
