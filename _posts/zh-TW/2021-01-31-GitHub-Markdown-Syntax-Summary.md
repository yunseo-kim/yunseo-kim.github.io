---
title: GitHub Markdown 語法整理
description: 本文將介紹 Markdown 是什麼，並以 GitHub Flavored Markdown 為基準，整理了用於 GitHub Pages 部落格託管的主要 Markdown 語法。
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

若要使用 GitHub Pages，需要先了解 **markdown** 語法。
本文參考 GitHub 官方文件的 [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) 和 [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 編寫而成。

## 1. 什麼是 Markdown
> **Markdown** 是一種基於純文字的輕量級標記語言。它被用來以純文字格式撰寫帶有格式的文件，其特點是語法比一般的標記語言更簡單易學。由於可以輕鬆轉換為 HTML 和富文本格式（RTF）等格式化文件，因此常被用於應用軟體附帶的 README 檔案或線上文章中。  
> 約翰·格魯伯（John Gruber）在[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12004 年，與亞倫·斯沃茨（Aaron Swartz）在語法方面進行了重要合作，共同創造了 Markdown 語言。其目標是讓使用者能以易於閱讀和編寫的純文字格式進行寫作，同時能夠選擇性地將其轉換為結構上有效的 XHTML（或 HTML）。

\- [維基百科，Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown 語法
Markdown 沒有統一的標準，因此詳細語法可能因使用情境而略有不同。這裡整理的 Markdown 語法是以 [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 為基準。

### 2.1. 換行與段落分隔
在 Markdown 中，按一次 Enter 鍵不會被視為換行。
~~~
第一句。
第二句。
第三句。
~~~
第一句。
第二句。
第三句。

若要換行，需在行末輸入兩個或以上的連續空格。
~~~
第一句。  
第二句。  
第三句。
~~~
第一句。  
第二句。  
第三句。

段落之間以一個空行（按兩次 Enter 鍵）來分隔。
~~~
這是一個段落。

這是另一個段落。
~~~
這是一個段落。

這是另一個段落。

### 2.2. 標題（Headers）
總共有六個層級。
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
H1 標籤原則上一頁只能有一個，因此在撰寫文章或文件時，通常很少會直接使用。

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

### 2.4. 引用文字
使用 > 符號。
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. 引用程式碼
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

也可以指定程式語言來啟用語法高亮顯示。
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

也可以使用指向儲存庫（repository）中其他檔案的相對路徑連結。使用方法與在終端機（terminal）中相同。
```
[README](../README.md)
```

### 2.7. 無序清單
使用 - 或 * 符號。
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

### 2.10. 任務清單
若要建立任務清單，請在每個項目前加上 \[ ]。
若要標示為已完成的項目，請使用 \[x]。
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. 附加圖片
```
語法：![（可選，建議填寫）圖片說明](url){（可選）附加選項}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. 建立表格
可以使用 | 和 - 來建立表格。
表格前必須留一個空行才能正常顯示。
至少需要使用三個以上的 - 才能被正常識別。
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
