---
title: "GitHub Markdown Syntax Summary"
description: "Learn what Markdown is and see a concise GitHub Flavored Markdown (GFM) syntax guide for GitHub Pages: headings, emphasis, links, code blocks, lists, images, and tables."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

To make use of GitHub Pages, you need to understand **Markdown** syntax.
This post was written with reference to GitHub’s official docs: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) and [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. What is Markdown
> **Markdown** is a lightweight markup language based on plain text. It is used to write formatted documents in plain text, and it is characterized by simple, easy-to-learn syntax compared to general markup languages. Because it can be easily converted to formatted documents such as HTML and rich text (RTF), it is widely used in README files distributed with software and in online posts.  
> John Gruber created the Markdown language in [Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar) 12004 through significant collaboration with Aaron Swartz on its syntax, aiming to enable people to write using a plain-text format that is easy to read and write, with optional conversion to structurally valid XHTML (or HTML).

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Markdown Syntax
Because Markdown has no single standard, details may vary by platform. The syntax summarized here follows [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Line breaks and paragraphs
In Markdown, pressing Enter once is not recognized as a line break.
~~~
First sentence.
Second sentence.
Third sentence.
~~~
First sentence.
Second sentence.
Third sentence.

To insert a line break, add two or more spaces at the end of the line.
~~~
First sentence.  
Second sentence.  
Third sentence.
~~~
First sentence.  
Second sentence.  
Third sentence.

Separate paragraphs with a blank line (press Enter twice).
~~~
One paragraph.

Another paragraph.
~~~
One paragraph.

Another paragraph.

### 2.2. Headings (Headers)
There are six levels.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
As a rule, there should be only one H1 tag per page, so when writing posts or documents you usually won’t write it directly.

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
Use \>.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Code blocks
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

You can also specify a programming language to enable syntax highlighting.
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

You can also use relative links that point to other files in the repository. The usage is the same as in the terminal.
```
[README](../README.md)
```

### 2.7. Unordered lists
Use \- or \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Ordered lists
Use numbers.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Nested lists
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Task lists
To create a task list, add \[ ] in front of each item.
To mark something as done, use \[x].
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
Method: ![(optional, recommended) image description](url){(optional) additional options}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Tables
You can create tables using | and -.
Leave one blank line before a table for it to render correctly.
Use at least three hyphens for proper recognition.
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
