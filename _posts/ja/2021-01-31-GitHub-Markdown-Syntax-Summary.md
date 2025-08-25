---
title: GitHub マークダウン文法整理
description: Markdownとは何かを学び、GitHub Pagesブログホスティングのために、GitHub Flavored Markdown基準で主要なMarkdown文法を整理しました。
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

GitHub Pagesの活用のためには**markdown**文法について知る必要がある。
GitHub公式ドキュメントの[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)と[Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)を参考にして作成した。

## 1. マークダウンとは
> **マークダウン（markdown）**は一般テキストベースの軽量マークアップ言語である。一般テキストで書式のある文書を作成するのに使用され、一般的なマークアップ言語に比べて文法が簡単で単純なのが特徴である。HTMLやリッチテキスト（RTF）などの書式文書に簡単に変換されるため、アプリケーションソフトウェアと一緒に配布されるREADMEファイルやオンライン投稿などに多く使用される。  
> ジョン・グルーバーは[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar)12004年に文法面でアーロン・スワーツと重要な協業を通じてマークダウン言語を作り、人々が読みやすく書きやすいプレーンテキストフォーマットを使用して書くことができながら、構造的に有効なXHTML（またはHTML）に選択的変換が可能にすることが目標である。

\- [ウィキペディア、マークダウン](https://en.wikipedia.org/wiki/Markdown)

## 2. マークダウン文法
マークダウンは決まった標準がないため、詳細文法は使用先ごとに少しずつ異なる場合がある。ここで整理したマークダウン文法は[GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)基準である。

### 2.1. 改行、段落区分
マークダウンではエンターキー一回は改行として認識しない。
~~~
最初の文。
二番目の文。
三番目の文。
~~~
最初の文。
二番目の文。
三番目の文。

改行は空白を連続して二つ以上入力すると適用される。
~~~
最初の文。  
二番目の文。  
三番目の文。
~~~
最初の文。  
二番目の文。  
三番目の文。

段落と段落の間は空行（エンターキー二回）で区分する。
~~~
一つの段落。

別の段落。
~~~
一つの段落。

別の段落。

### 2.2. 見出し（Headers）
全部で6段階がある。
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
H1タグは原則的に一つのページに一つだけあるべきなので、通常投稿や文書作成時には直接使うことはあまりない。

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

### 2.4. テキスト引用
\>を利用する。
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. コード引用
\``` または \~~~を利用する。
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

プログラミング言語を指定して文法ハイライト表示を有効にすることもできる。
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

リポジトリ内の他のファイルを指す相対パスリンクも使用できる。使用法はターミナルでと同じである。
```
[README](../README.md)
```

### 2.7. 順序なしリスト
\-や\*を利用する。
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. 順序付きリスト
数字を利用する。
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. ネストしたリスト
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. タスクリスト
タスクリストを作るには各項目の前に\[ ]を追加する。
完了したタスクを表示するには\[x]を利用する。
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. 画像添付
```
方法: ![(選択、推奨)画像説明](url){(選択)追加オプション}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. 表作成
|と-を利用して表を作成できる。
表の前に一行空けておく必要がある。
少なくとも3つ以上の-を使用しなければ正常に認識される。
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
