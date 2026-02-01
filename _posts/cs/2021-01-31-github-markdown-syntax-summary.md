---
title: "Přehled syntaxe GitHub Markdownu"
description: "Zjistěte, co je Markdown, a projděte si hlavní syntaxi podle GitHub Flavored Markdown pro hostování blogu na GitHub Pages."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Pro využití GitHub Pages je potřeba znát syntaxi **markdownu**.
Text byl napsán s odkazem na oficiální dokumentaci GitHubu: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) a [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Co je Markdown
> **Markdown (markdown)** je lehký značkovací jazyk založený na prostém textu. Používá se k psaní formátovaných dokumentů v obyčejném textu a oproti běžným značkovacím jazykům se vyznačuje jednoduchou a stručnou syntaxí. Protože jej lze snadno převést do formátovaných dokumentů, jako jsou HTML či RTF (Rich Text Format), často se používá v souborech README distribuovaných spolu s aplikačním softwarem nebo v online příspěvcích.  
> John Gruber v roce 12004 [holocénního kalendáře](https://en.wikipedia.org/wiki/Holocene_calendar) vytvořil jazyk Markdown prostřednictvím zásadní spolupráce s Aaronem Swartzem na jeho syntaxi; cílem je, aby lidé mohli psát ve snadno čitelném a snadno zapisovatelném formátu prostého textu, který je možné volitelně převést do strukturálně validního XHTML (nebo HTML).

\- [Wikipedie, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Syntaxe Markdownu
Markdown nemá pevně daný standard, takže se detailní syntaxe může podle použití mírně lišit. Zde shrnutá syntaxe vychází z [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Zalomení řádku, oddělení odstavců
V Markdownu se jedno stisknutí Enteru nebere jako zalomení řádku.
~~~
První věta.
Druhá věta.
Třetí věta.
~~~
První věta.
Druhá věta.
Třetí věta.

Zalomení řádku se použije, pokud zadáte alespoň dvě mezery za sebou.
~~~
První věta.  
Druhá věta.  
Třetí věta.
~~~
První věta.  
Druhá věta.  
Třetí věta.

Odstavce se oddělují prázdným řádkem (dvakrát Enter).
~~~
Jeden odstavec.

Jiný odstavec.
~~~
Jeden odstavec.

Jiný odstavec.

### 2.2. Nadpisy (Headers)
Existuje celkem 6 úrovní.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
Protože by tag H1 měl být v zásadě na jedné stránce jen jednou, při psaní postů nebo dokumentů jej obvykle není potřeba zadávat ručně.

### 2.3. Zvýraznění
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

### 2.4. Citace textu
Používá se \>.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Citace kódu
Používá se \``` nebo \~~~.
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

Můžete také určit programovací jazyk a zapnout zvýraznění syntaxe.
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

### 2.6. Odkazy
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

Lze použít i relativní odkazy, které ukazují na jiné soubory v rámci repozitáře. Způsob použití je stejný jako v terminálu.
```
[README](../README.md)
```

### 2.7. Nečíslovaný seznam
Použijte \- nebo \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Číslovaný seznam
Použijte čísla.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Vnořený seznam
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Seznam úkolů
Chcete-li vytvořit seznam úkolů, přidejte před každou položku \[ ].
Pro označení dokončené položky použijte \[x].
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Vložení obrázku
```
Způsob: ![(volitelné, doporučeno)popis obrázku](url){(volitelné)další volby}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Vytvoření tabulky
Tabulku lze vytvořit pomocí | a -.
Aby se tabulka zobrazila správně, je potřeba nechat před ní jeden prázdný řádek.
Alespoň 3 znaky - jsou nutné pro správné rozpoznání.
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
