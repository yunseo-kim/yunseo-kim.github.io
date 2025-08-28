---
title: "GitHub Markdown 語法整理"
description: "介紹什麼是 Markdown，並依 GitHub Flavored Markdown 彙整 GitHub Pages 部落格常用的 Markdown 語法與範例。"
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

要善用 GitHub Pages，需要了解 **Markdown** 語法。
本文參考 GitHub 官方文件的 [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) 與 [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 撰寫。

## 1. 什麼是 Markdown
> **Markdown（markdown）**是一種以純文字為基礎的輕量級標記語言。它用純文字就能撰寫具備格式的文件，和一般標記語言相比，語法更簡單易學。由於能輕易轉換成 HTML 與豐富文字格式（RTF）等格式化文件，因此廣泛用於隨應用程式一同發布的 README 檔案與線上貼文等。  
> 約翰‧格魯伯（John Gruber）在[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12004 年，與亞倫‧斯沃茨（Aaron Swartz）在語法面進行重要協作，建立了 Markdown 語言；其目標是讓人們以易讀易寫的純文字格式撰寫內容，並可選擇性地轉換為結構上有效的 XHTML（或 HTML）。

\- [維基百科，Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown 語法
Markdown 沒有統一標準，因此細節語法會因使用場景而異。這裡整理的 Markdown 語法以 [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 為準。

### 2.1. 换行與段落分隔
在 Markdown 中，單按一次 Enter 並不會被視為換行。
~~~
第一句。
第二句。
第三句。
~~~
第一句。
第二句。
第三句。

若要換行，可在行尾連續輸入至少兩個空白。
~~~
第一句。  
第二句。  
第三句。
~~~
第一句。  
第二句。  
第三句。

段落與段落之間以空白行（按兩次 Enter）分隔。
~~~
一個段落。

另一個段落。
~~~
一個段落。

另一個段落。

### 2.2. 標題（Headers）
共有 6 個層級。
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
原則上每頁只能有一個 H1，因此在撰寫文章或文件時通常不直接使用。

### 2.3. 強調
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

### 2.4. 區塊引用
使用 \>。
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. 程式碼引用
使用 \``` 或 \~~~。
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

也可以指定程式語言以啟用語法高亮。
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

### 2.6. 連結
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

也可以使用相對路徑連結到版本庫中的其他檔案，寫法與終端機相同。
```
[README](../README.md)
```

### 2.7. 無序清單
使用 - 或 *。
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. 有序清單
使用數字。
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. 巢狀清單
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. 待辦清單
要建立待辦清單，在各項目前加上 \[ ]。  
要標示已完成則使用 \[x]。
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. 插入圖片
```
寫法：![(可選，建議) 圖片說明](url){(可選) 其他選項}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. 建立表格
可用 | 與 - 建立表格。  
表格前須留一個空行才能正確顯示。  
每欄至少需 3 個連續的 - 才能被正確解析。
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
