---
title: GitHub マークダウン記法まとめ
description: "マークダウン（markdown）の概要を説明し、GitHub Pagesのブログ運用に向けて、GitHub フレーバード・マークダウン（GitHub Flavored Markdown）を基準に主要な記法を整理します。"
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

GitHub Pagesを活用するには、**マークダウン（markdown）**記法について知っておく必要がある。
GitHub公式ドキュメントの[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)と[Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)を参考に作成した。

## 1. マークダウンとは
> **マークダウン（markdown）**は、プレーンテキストベースの軽量マークアップ言語である。プレーンテキストで書式付き文書を作成するために用いられ、一般的なマークアップ言語に比べて文法が簡潔であるのが特徴。HTMLやリッチテキスト（RTF）などの書式文書へ容易に変換できるため、アプリケーションに同梱されるREADMEファイルやオンライン投稿などに広く用いられている。  
> ジョン・グルーバー（John Gruber）は人類紀元（https://en.wikipedia.org/wiki/Holocene_calendar）12004年に、文法面でアーロン・スワーツ（Aaron Swartz）と重要な協働を通じてマークダウン言語を作成した。人間が読み書きしやすいプレーンテキストのフォーマットで記述でき、かつ構造的に妥当なXHTML（または HTML）へ選択的に変換できることを目標としている。

\- [ウィキペディア、マークダウン](https://en.wikipedia.org/wiki/Markdown)

## 2. マークダウン記法
マークダウンには定まった標準がないため、詳細な文法は利用先によって多少異なりうる。ここでまとめる記法は[GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)を基準とする。

### 2.1. 改行と段落区切り
マークダウンでは、Enterキー1回は改行として認識されない。
~~~
第一の文。
第二の文。
第三の文。
~~~
第一の文。
第二の文。
第三の文。

改行はスペースを連続で2つ以上入力すると適用される。
~~~
第一の文。  
第二の文。  
第三の文。
~~~
第一の文。  
第二の文。  
第三の文。

段落同士は空行（Enterキー2回）で区切る。
~~~
ひとつの段落。

別の段落。
~~~
ひとつの段落。

別の段落。

### 2.2. 見出し（Headers）
全部で6段階がある。
```
# これはH1です
## これはH2です
### これはH3です
#### これはH4です
##### これはH5です
###### これはH6です
```
H1タグは原則として1ページに1つだけにすべきなので、記事や文書を書く際に直接使う機会は多くない。

### 2.3. 強調
```
*このテキストはイタリック体です*
_これもイタリック体です_

**これは太字です**
__これも太字です__

~~これは誤りのテキストでした~~

_組み合わせることも **できます**_

***このテキスト全体が重要です***
```
*このテキストはイタリック体です*  
_これもイタリック体です_

**これは太字です**  
__これも太字です__

~~これは誤りのテキストでした~~

_組み合わせることも **できます**_

***このテキスト全体が重要です***

### 2.4. テキスト引用
\> を用いる。
```
> これは第1レベルのブロック引用です。
>> これは第2レベルのブロック引用です。
>>> これは第3レベルのブロック引用です。
```
> これは第1レベルのブロック引用です。
>> これは第2レベルのブロック引用です。
>>> これは第3レベルのブロック引用です。

### 2.5. コード引用
\``` または \~~~ を用いる。
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

プログラミング言語を指定してシンタックスハイライトを有効にできる。
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

リポジトリ内の別ファイルを指す相対パスのリンクも使える。使い方はターミナルと同様。
```
[README](../README.md)
```

### 2.7. 非順序リスト
\- または \* を用いる。
```
- ジョージ・ワシントン(George Washington)
- ジョン・アダムズ(John Adams)
- トーマス・ジェファーソン(Thomas Jefferson)
```
- ジョージ・ワシントン(George Washington)
- ジョン・アダムズ(John Adams)
- トーマス・ジェファーソン(Thomas Jefferson)

### 2.8. 番号付きリスト
数字を用いる。
```
1. ジェームズ・マディソン(James Madison)
2. ジェームズ・モンロー(James Monroe)
3. ジョン・クィンシー・アダムズ(John Quincy Adams)
```
1. ジェームズ・マディソン(James Madison)
2. ジェームズ・モンロー(James Monroe)
3. ジョン・クィンシー・アダムズ(John Quincy Adams)

### 2.9. ネストされたリスト
```
1. 最初のリスト項目
   - 最初のネストされた項目
     - 2番目のネストされた項目
```
1. 最初のリスト項目
   - 最初のネストされた項目
     - 2番目のネストされた項目

### 2.10. タスクリスト
タスクリストを作るには各項目の先頭に \[ ] を付ける。
完了した項目は \[x] を用いる。
```
- [x] 変更を完了する
- [ ] コミットをGitHubにプッシュする
- [ ] プルリクエストを作成する
```
- [x] 変更を完了する
- [ ] コミットをGitHubにプッシュする
- [ ] プルリクエストを作成する

### 2.11. 画像の挿入
```
方法: ![(任意・推奨)画像の説明](url){（任意）追加オプション}
![GitHub ロゴ(GitHub Logo)](/images/logo.png)
![GitHub ロゴ(GitHub Logo)](/images/logo.png){: .align-center}
![GitHub ロゴ(GitHub Logo)](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. 表の作成
| と - を使って表を作成できる。
表の前に1行空けると正しく表示される。
少なくとも3つ以上の - を使う必要がある。
```
 
| 左寄せ | 中央寄せ | 右寄せ |
| :---   |  :---:   |   ---: |
| git status | git status | git status |
| git diff   | git diff   | git diff   |
```

| 左寄せ | 中央寄せ | 右寄せ |
| :---   |  :---:   |   ---: |
| git status | git status | git status |
| git diff   | git diff   | git diff   |
