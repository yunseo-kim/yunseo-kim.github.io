---
title: GitHubのマークダウン文法まとめ
description: Markdownとは何かを理解し、GitHub Pagesブログホスティングのために、GitHub Flavored Markdownを基準に主要なMarkdown文法をまとめました。
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
GitHub Pagesを活用するには、**markdown**文法について知る必要があります。
GitHub公式ドキュメントの[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)と[Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)を参考に作成しました。

## 1. マークダウンとは
> **マークダウン（markdown）**は、一般的なテキストベースの軽量マークアップ言語です。一般的なテキストで書式付きの文書を作成するのに使用され、一般的なマークアップ言語に比べて文法が簡単で簡潔なのが特徴です。HTMLやリッチテキスト（RTF）などの書式付き文書に簡単に変換できるため、アプリケーションソフトウェアと一緒に配布されるREADMEファイルやオンライン投稿などによく使用されます。  
> ジョン・グルーバーは[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar)12004年に、文法面でアーロン・シュワルツと重要な協力を通じてマークダウン言語を作成しました。人々が読みやすく書きやすいプレーンテキストフォーマットを使用して書くことができ、構造的に有効なXHTML（またはHTML）に選択的に変換できるようにすることが目標です。

-[ウィキペディア、マークダウン](https://en.wikipedia.org/wiki/Markdown)

## 2. マークダウン文法
マークダウンには定められた標準がないため、詳細な文法は使用場所によって少しずつ異なる場合があります。ここでまとめたマークダウン文法は[GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)基準です。

### 2.1. 改行、段落の区切り
マークダウンではエンターキー1回は改行として認識されません。
~~~
1つ目の文。
2つ目の文。
3つ目の文。
~~~
1つ目の文。
2つ目の文。
3つ目の文。

改行は、連続して2つ以上のスペースを入力すると適用されます。
~~~
1つ目の文。  
2つ目の文。  
3つ目の文。
~~~
1つ目の文。  
2つ目の文。  
3つ目の文。

段落と段落の間は空行（エンターキー2回）で区切ります。
~~~
1つの段落。

別の段落。
~~~
1つの段落。

別の段落。

### 2.2. 見出し（Headers）
全部で6段階あります。
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
H1タグは原則として1ページに1つだけあるべきなので、通常、投稿や文書作成時に直接使うことはあまりありません。

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

### 2.4. テキストの引用
\>を使用します。
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. コードの引用
\```または\~~~を使用します。
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

プログラミング言語を指定して、構文強調表示を有効にすることもできます。
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

### 2.6. リンク
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

リポジトリ内の他のファイルを指す相対パスリンクも使用できます。使用方法はターミナルでの場合と同じです。
```
[README](../README.md)
```

### 2.7. 非順序リスト
\-や\*を使用します。
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. 順序リスト
数字を使用します。
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. ネストされたリスト
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. タスクリスト
タスクリストを作成するには、各項目の前に\[ ]を追加します。
完了したタスクを表示するには\[x]を使用します。
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. 画像の添付
```
方法: ![(オプション)画像の説明](url){(オプション)追加オプション}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. 表の作成
|と-を使用して表を作成できます。
表の前に1行空けておく必要があります。
少なくとも3つ以上の-を使用する必要があります。
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
