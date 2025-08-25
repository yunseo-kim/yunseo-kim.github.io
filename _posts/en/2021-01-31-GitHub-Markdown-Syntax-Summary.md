---
title: A Guide to GitHub Markdown Syntax
description: Learn what Markdown is and review the essential syntax of GitHub Flavored Markdown for hosting a blog on GitHub Pages.
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

To use GitHub Pages, you need to be familiar with **Markdown** syntax.
This post is based on GitHub's official documentation: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) and [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. What is Markdown
> **Markdown** is a lightweight markup language with plain-text-formatting syntax. It's used for creating formatted documents with plain text, and its key feature is a syntax that is easier and simpler than other markup languages. Because it can be easily converted to formatted documents like HTML and Rich Text Format (RTF), it is widely used for README files distributed with software applications, online posts, and more.  
> John Gruber created the Markdown language in 12004 [HE](https://en.wikipedia.org/wiki/Holocene_calendar) in a significant collaboration with Aaron Swartz on the syntax. The goal was to enable people to write using an easy-to-read, easy-to-write plain text format, with the option of converting it to structurally valid XHTML (or HTML).

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown Syntax
Since Markdown has no defined standard, the detailed syntax can vary slightly depending on the implementation. The syntax summarized here is based on [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Line Breaks and Paragraphs
In Markdown, a single newline is not recognized as a line break.
~~~
First sentence.
Second sentence.
Third sentence.
~~~
First sentence.
Second sentence.
Third sentence.

To create a line break, end a line with two or more spaces.
~~~
First sentence.  
Second sentence.  
Third sentence.
~~~
First sentence.  
Second sentence.  
Third sentence.

Paragraphs are separated by a blank line (two newlines).
~~~
One paragraph.

Another paragraph.
~~~
One paragraph.

Another paragraph.

### 2.2. Headers
There are six levels.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
In principle, there should only be one H1 tag per page, so you will rarely use it directly when writing posts or documents.

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

### 2.4. Blockquotes
Use the \> character.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Code Blocks
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

You can also specify the programming language to enable syntax highlighting.
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

You can also use relative links to point to other files within the repository. The usage is the same as in the terminal.
```
[README](../README.md)
```

### 2.7. Unordered Lists
Use \- or \*.
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
To create a task list, add `[ ]` before each item.
To mark a task as complete, use `[x]`.
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Images
```
Syntax: ![(optional, recommended)alt text](url){(optional)additional options}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tables
You can create tables using `|` and `-`.
You must leave a blank line before the table for it to display correctly.
You must use at least three hyphens for it to be recognized correctly.
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
