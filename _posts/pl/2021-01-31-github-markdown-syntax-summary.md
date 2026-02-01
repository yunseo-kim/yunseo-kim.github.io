---
title: "Podsumowanie składni Markdown na GitHubie"
description: "Czym jest Markdown i jak, w kontekście hostowania bloga na GitHub Pages, korzystać z GitHub Flavored Markdown — najważniejsze zasady i składnia."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Aby wykorzystać GitHub Pages, trzeba znać składnię **markdown**.
Tekst powstał na podstawie oficjalnej dokumentacji GitHub: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) oraz [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Czym jest Markdown
> **Markdown (markdown)** to lekki język znaczników oparty na zwykłym tekście. Służy do tworzenia sformatowanych dokumentów w postaci zwykłego tekstu; w porównaniu z typowymi językami znaczników cechuje się prostą i łatwą składnią. Ponieważ można go łatwo konwertować do dokumentów sformatowanych, takich jak HTML czy Rich Text Format (RTF), jest często używany w plikach README dystrybuowanych wraz z oprogramowaniem oraz w publikacjach online.  
> John Gruber stworzył język Markdown w roku 12004 [kalendarza holoceńskiego](https://en.wikipedia.org/wiki/Holocene_calendar), we współpracy z Aaronem Swartzem w zakresie składni; celem było umożliwienie ludziom pisania w łatwym do czytania i łatwym do tworzenia formacie plain text, z opcjonalną konwersją do strukturalnie poprawnego XHTML (lub HTML).

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Składnia Markdown
Markdown nie ma jednego ustalonego standardu, dlatego szczegółowa składnia może się nieco różnić w zależności od zastosowania. Składnia zebrana tutaj opiera się na [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Łamanie linii, podział na akapity
W Markdown pojedyncze naciśnięcie Enter nie jest traktowane jako złamanie linii.
~~~
Pierwsze zdanie.
Drugie zdanie.
Trzecie zdanie.
~~~
Pierwsze zdanie.
Drugie zdanie.
Trzecie zdanie.

Złamanie linii uzyskuje się, wpisując co najmniej dwie spacje z rzędu.
~~~
Pierwsze zdanie.  
Drugie zdanie.  
Trzecie zdanie.
~~~
Pierwsze zdanie.  
Drugie zdanie.  
Trzecie zdanie.

Akapity rozdziela się pustą linią (dwa razy Enter).
~~~
Jeden akapit.

Inny akapit.
~~~
Jeden akapit.

Inny akapit.

### 2.2. Nagłówki (Headers)
Łącznie jest 6 poziomów.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
Ponieważ tag H1 zasadniczo powinien występować na stronie tylko raz, zwykle przy pisaniu posta lub dokumentu rzadko używa się go bezpośrednio.

### 2.3. Wyróżnienia
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

### 2.4. Cytowanie tekstu
Używa się \>.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Cytowanie kodu
Używa się \``` lub \~~~.
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

Można też wskazać język programowania, aby włączyć podświetlanie składni.
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

### 2.6. Linki
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

Można też używać linków względnych wskazujących na inne pliki w repozytorium. Sposób użycia jest taki sam jak w terminalu.
```
[README](../README.md)
```

### 2.7. Lista nieuporządkowana
Używa się \- lub \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Lista uporządkowana
Używa się numerów.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Lista zagnieżdżona
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Lista zadań (to-do)
Aby utworzyć listę zadań, dodaj \[ ] przed każdym elementem.
Aby oznaczyć zadanie jako wykonane, użyj \[x].
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Wstawianie obrazów
```
Metoda: ![(opcjonalnie, zalecane)opis obrazu](url){(opcjonalnie)opcje dodatkowe}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tworzenie tabel
Tabele można tworzyć za pomocą | oraz -.
Przed tabelą należy zostawić jedną pustą linię, aby wyświetlała się poprawnie.
Aby składnia została poprawnie rozpoznana, trzeba użyć co najmniej 3 znaków -.
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
