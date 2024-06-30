---
title: "GitHub Markdown Syntax Summary"
description: >-
  Learn what Markdown is and summarize the main Markdown syntax based on GitHub Flavored Markdown for GitHub Pages blog hosting.
categories:
  - Blogging
tags:
  - Jekyll
toc: true
toc_sticky: true
---

To utilize GitHub Pages, it's necessary to understand **markdown** syntax.
This summary is based on GitHub's official documents [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) and [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. What is Markdown
> **Markdown** is a lightweight markup language based on plain text. It is used to write formatted documents in plain text, and is characterized by its easy and simple syntax compared to general markup languages. It is widely used in README files distributed with application software or online posts because it can be easily converted to formatted documents such as HTML and Rich Text Format (RTF).
>> John Gruber created the Markdown language in 2004 through significant collaboration with Aaron Swartz on grammar, with the goal of enabling people to write using an easy-to-read and easy-to-write plain text format while allowing optional conversion to structurally valid XHTML (or HTML).

-[Wikipedia, Markdown](https://ko.wikipedia.org/wiki/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4)

## 2. Markdown Syntax
Since Markdown doesn't have a set standard, detailed syntax may vary slightly depending on where it's used. The Markdown syntax summarized here is based on [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Line Breaks, Paragraph Separation
In Markdown, a single press of the enter key is not recognized as a line break.
~~~
First sentence.
Second sentence.
Third sentence.
~~~
First sentence.
Second sentence.
Third sentence.

A line break is applied by entering two or more consecutive spaces.
~~~
First sentence.  
Second sentence.  
Third sentence.
~~~
First sentence.  
Second sentence.  
Third sentence.

Paragraphs are separated by a blank line (pressing enter twice).
~~~
One paragraph.

Another paragraph.
~~~
One paragraph.

Another paragraph.

### 2.2. Headers
There are six levels in total.
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

### 2.3. Emphasis
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

### 2.4. Text Quoting
Use >.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Code Quoting
Use \``` or \~~~.
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

You can also activate syntax highlighting by specifying a programming language.
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

You can also use relative path links to other files within the repository. The usage is the same as in the terminal.
```
[README](../README.md)
```

### 2.7. Unordered Lists
Use - or *.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Ordered Lists
Use numbers.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Nested Lists
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Task Lists
To create a task list, add [ ] before each item.
To mark a task as complete, use [x].
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Image Attachment
```
Method: ![(Optional)Image description](url){(Optional)Additional options}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Table Creation
You can create tables using | and -.
Leave a blank line before the table for it to display correctly.
Use at least three - for it to be recognized correctly.
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