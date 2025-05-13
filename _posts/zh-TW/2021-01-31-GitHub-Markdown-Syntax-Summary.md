---
title: GitHub Markdown 語法整理
description: 了解什麼是 Markdown，並根據 GitHub Flavored Markdown 標準整理了主要的 Markdown 語法，以用於 GitHub Pages 部落格託管。
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
為了使用 GitHub Pages，有必要了解 **markdown** 語法。
本文參考了 GitHub 官方文件的 [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) 和 [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 撰寫而成。

## 1. 什麼是 Markdown
> **Markdown** 是一種輕量級的標記語言，基於純文本。它用於撰寫具有格式的文檔，其特點是相比一般的標記語言，語法更簡單易懂。由於可以輕鬆轉換為 HTML 和富文本（RTF）等格式文檔，因此常用於隨應用軟件分發的 README 文件或在線帖子等。  
> 約翰·格魯伯（John Gruber）在[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12004年與亞倫·斯沃茨（Aaron Swartz）在語法方面進行了重要合作，創造了 Markdown 語言。其目標是讓人們能夠使用易讀易寫的純文本格式進行寫作，同時可選擇性地轉換為結構上有效的 XHTML（或 HTML）。

-[維基百科，Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown 語法
由於 Markdown 沒有固定的標準，因此不同使用場景下的細節語法可能略有不同。這裡整理的 Markdown 語法是基於 [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) 標準。

### 2.1. 換行、段落分隔
在 Markdown 中，單次按下 Enter 鍵不會被識別為換行。
~~~
第一句話。
第二句話。
第三句話。
~~~
第一句話。
第二句話。
第三句話。

要換行，需要連續輸入兩個以上的空格。
~~~
第一句話。  
第二句話。  
第三句話。
~~~
第一句話。  
第二句話。  
第三句話。

段落與段落之間用空行（連按兩次 Enter 鍵）來分隔。
~~~
一個段落。

另一個段落。
~~~
一個段落。

另一個段落。

### 2.2. 標題（Headers）
共有 6 個等級。
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
原則上，H1 標籤在一個頁面中應該只出現一次，所以通常在撰寫文章或文檔時很少直接使用。

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

### 2.4. 文字引用
使用 \>。
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. 代碼引用
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

也可以指定程式語言以啟用語法高亮顯示。
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

也可以使用相對路徑連結指向儲存庫中的其他文件。使用方法與終端機中相同。
```
[README](../README.md)
```

### 2.7. 無序列表
使用 \- 或 \*。
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. 有序列表
使用數字。
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. 巢狀列表
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. 待辦事項列表
要創建待辦事項列表，在每個項目前加上 \[ ]。
要標記已完成的事項，使用 \[x]。
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
方法：![(可選)圖片描述](url){(可選)額外選項}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. 創建表格
使用 | 和 - 來創建表格。
表格前需要留一個空行才能正確顯示。
至少需要使用 3 個以上的 - 才能被正確識別。
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
