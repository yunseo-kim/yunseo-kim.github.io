---
title: GitHub Pages ブログの作成と運用
description: 静的/動的ウェブページの特徴と違い、静的サイトジェネレーター（Static Site Generator）の概要と選び方を整理し、Jekyll ブログを GitHub Pages で構築・ホスティングする手順を解説。
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

12021年の初めから Jekyll を使って GitHub Pages にブログをホスティングし始めた。しかし構築当時にインストール手順をきちんと整理しておかなかったため、後の保守でやや困ったので、簡単にでもインストール手順と運用方法をまとめておく。  

（+ 12024.12 内容更新）

## 1. 静的サイトジェネレーターとウェブホスティング
### 1-1. 静的ウェブページ vs 動的ウェブページ
#### 静的ウェブページ（Static Web Page）
- サーバに保存されたデータをそのまま利用者に返すページ
- ウェブサーバはリクエストに対応する事前保存済みページを返す
- 利用者はサーバ上のデータが変更されない限り同一のページを見る
- 要求されたファイルだけ送ればよいので追加処理が不要で、一般に応答が速い
- 単純なファイル群で構成され、ウェブサーバだけ用意すればよいので構築コストが低い
- 保存済みの情報だけを表示するため提供できる機能が限られる
- データの追加・修正・削除を管理者が手動で行う必要がある
- クローリングしやすい構造で、検索エンジン最適化（SEO）に相対的に有利

#### 動的ウェブページ（Dynamic Web Page）
- サーバに保存したデータをスクリプトで加工して返すページ
- ウェブサーバがリクエストを解釈し、データを加工して生成したページを返す
- 利用者は状況・時間・要求に応じて変化するページを見る
- 返却前にスクリプト処理が必要なため相対的に応答が遅い
- ウェブサーバに加えてアプリケーションサーバが必要で、構築時に追加コストが発生
- 多様な情報を組み合わせて動的に提供できるため多様なサービスが可能
- ページ構造によっては、利用者がブラウザ上でデータの追加・修正・削除を行える

### 1-2. 静的サイトジェネレーター（SSG, Static Site Generator）
- 生データ（通常は Markdown 形式のテキスト）と定義済みテンプレートから静的ウェブページを生成するツール
- 個別に HTML を書かずとも、Markdown で記事を書けばビルドと配信を自動化できる
- 例）Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- GitHub が無料提供する静的ウェブページのホスティングサービス
- アカウントごとに1つの個人サイトをホストでき、リポジトリ単位のプロジェクトドキュメントサイトは無制限に作成・ホスト可能
- '{username}.github.io' という名前で自分の GitHub ユーザー名に合わせてリポジトリを作成し、そのリポジトリにビルド済み HTML を直接 Push するか、GitHub Actions を使ってビルドとデプロイを実行できる
- 所有ドメインがあれば設定で関連付け、デフォルトの '{username}.github.io' ではない独自ドメインを使うことも可能

## 2. 使用する SSG とテーマの選定

### 2-1. Jekyll を選んだ理由
Jekyll、Hugo、Gatsby など複数の SSG があるが、Jekyll を使うことにした。選定基準と採用理由は次のとおり。
- 無用な試行錯誤を減らし、執筆と運営に集中できるか？
  - Jekyll は GitHub Pages で公式サポートされる静的サイトジェネレーターである。もちろん Hugo や Gatsby など他の SSG でも GitHub Pages 上でホストできるし、Netlify など別ホスティングを使う選択肢もある。しかしこの規模の個人ブログでは、どの SSG を使うか・ビルド速度や性能がどうかはそれほど重要ではない。そこで、より保守が簡単で参照ドキュメントが多いものがよいと判断した。
  - また Jekyll は Hugo や Gatsby に比べ開発の歴史が長い。その分ドキュメントが充実しており、実際に問題が起きた際に参照できる資料が圧倒的に多い。
- 利用できるテーマとプラグインが多いか？
  - SSG を使うとしても、各種テンプレートを一から作るのは手間で時間もかかり、そこまでの必要もない。すでに公開されている優れたテーマが多いので、気に入ったものを採用すればよい。
  - そもそも自分は C や Python を主に使っており、Jekyll の Ruby や Hugo の Go 言語には明るくない。したがって既存のテーマやプラグインを積極的に活用したかった。
  - Jekyll は一目で気に入るテーマがすぐ見つかった一方、Hugo や Gatsby は個人ブログ用途に適したテーマ数が相対的に多くはない印象だった。先述のとおり、開発者が個人ブログのホスティングに多用する GitHub Pages との親和性や、開発期間の長さがここにも効いているのだろう。

### 2-2. テーマ選定
#### Minimal Mistakes（12021.01 - 12022.04）
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- ブログ開設から約1年3か月使っていたテーマ
- Disqus、Discourse、utterances によるコメント機能対応
- カテゴリとタグの分類機能
- Google Analytics を標準サポート
- 定義済みのスキンを選択可能
- のちにデザインがより好みの Chirpy テーマを見つけて乗り換えたが、工学系っぽいブログという点を踏まえると、たとえ可愛げはなくても十分に整ったデザインで無難に使えたと思う。

#### Chirpy Jekyll Theme（12022.04 - 現在）
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- 12022年4月に移行して以来、現在も使用中のテーマ
- 複数カテゴリ、タグ機能に対応
- MathJax ベースで LaTeX 記法の数式を標準サポート
- Mermaid ベースのダイアグラム機能を標準サポート
- Disqus、Giscus などによるコメント機能に対応
- Google Analytics、GoatCounter に対応
- ライト/ダークテーマに対応
- 乗り換え時点では、MathJax や Mermaid は Minimal Mistakes テーマでは自前サポートがなく、カスタマイズで追加する必要があったが、Chirpy では標準サポートされている。たいした手間ではないにせよ、ちょっとした利点ではある。
- 何よりデザインが美しい。Minimal Mistakes はきれいではあるものの、ブログというよりプロジェクトの公式ドキュメントやポートフォリオ向けの堅さがあり、Chirpy は Tistory や Medium、velog などの商用ブログプラットフォームと比べても見劣りしないのが強み。

## 3. GitHub リポジトリの作成、ビルドとデプロイ
現在（12024.06）使用中の Chirpy Jekyll Theme を前提に記す。Git はインストール済みと仮定する。  
[Jekyll 公式インストールガイド](https://jekyllrb.com/docs/installation/) と [Chirpy Jekyll Theme 公式ページ](https://github.com/cotes2020/jekyll-theme-chirpy/wiki) を参照。

### 3-1. Ruby と Jekyll のインストール
[Jekyll 公式インストールガイド](https://jekyllrb.com/docs/installation/)に従い、OS 環境に合わせて Ruby と Jekyll をインストールする。

### 3-2. GitHub リポジトリの作成
[Chirpy Jekyll Theme 公式ページ](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site)では次の2つの方法が紹介されている。
1. "jekyll-theme-chirpy" gem でコアファイルを取り込み、残りのリソースを [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) テンプレートから持ってくる方法
  - 長所：後述のとおり、バージョンアップの適用が容易。
  - 短所：大規模にカスタマイズする場合はかえって不便なことがある。
2. [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) リポジトリを自分のブログのリポジトリとしてフォークする方法
  - 長所：すべてのファイルをリポジトリ内で直接管理できるため、テーマ非対応の機能をコード修正で追加するなどのカスタマイズがしやすい。
  - 短所：バージョンアップを適用するには[元リポジトリの最新アップストリームタグ](https://github.com/cotes2020/jekyll-theme-chirpy/tags)をマージする必要があり、場合によっては独自カスタマイズとアップグレード版のコードが衝突する。衝突した場合は自力で解消する必要がある。

私は1番の方法を採用した。Chirpy テーマは基本的に完成度が高く、多くのユーザにとって大きなカスタマイズは不要なうえ、12024年現在も活発に開発・改善が続いている。よほどの大改造をしない限り、元のアップストリームに随時追従する利点が、独自カスタマイズの利点を上回る。公式ガイドでも大半のユーザには1番の方法が推奨されている。

### 3-3. 主な設定
ルートディレクトリの `_config.yml`{: .filepath} と `_data/contact.yml`{: .filepath}、`_data/share.yml`{: .filepath} で必要な設定を行う。コメントが丁寧で直感的な設定が多く、特に難しくはない。外部作業がいるものとしては Google Search Console 連携のための認証コード登録や、Google Analytics / GoatCounter などのウェブマスターツール連携があるが、手順自体は複雑ではないし、本稿の主題でもないため詳細は割愛する。

### 3-4. ローカルビルド
必須ではないが、新規ポストやサイトの修正がウェブ上で正しく表示されるか事前に確認したいことがある。その場合はローカルリポジトリのルートでターミナルを開き、次を実行する。
```console
$ bundle exec jekyll s
```
しばらく待つとローカルでビルドされ、<http://127.0.0.1:4000> で結果を確認できる。

### 3-5. デプロイ
方法は2つ。
1. GitHub Actions を活用（GitHub Pages でホスティングする場合）
  - GitHub Free プランを使っている場合、リポジトリは public にする必要がある
  - GitHub のウェブ UI でリポジトリの「Settings」タブを開き、左のナビゲーションで「Code and automation > Pages」をクリックし、**Source** セクションで **GitHub Actions** を選択
  - 設定完了後は、新しいコミットを Push するたびに「Build and Deploy」ワークフローが自動実行される
2. 自前でビルドして配布（他ホスティングやセルフホスティングの場合）
  - 次を実行してサイトを手動ビルド
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - `_site` ディレクトリのビルド成果物をサーバへアップロード

## 4. ポスト作成
Chirpy テーマの[ポスト作成ガイド](https://chirpy.cotes.page/posts/write-a-new-post/)に、作成手順や利用可能なオプションがよく整理されている。本稿で触れていない機能も多数あるので、必要に応じて公式ドキュメントを参照してほしい。また GitHub Flavored Markdown の基本構文は以前に[別記事](/posts/github-markdown-syntax-summary/)でまとめてある。ここでは投稿時に共通して意識すべき要点を記す。

### Markdown ファイルの作成
- 名前形式: `YYYY-MM-DD-TITLE.md`{: .filepath}
- 置き場所: `_posts`{: .filepath} ディレクトリ

### Front Matter の記述
Markdown ファイルの冒頭に Front Matter を適切に記述する。
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: ポストのタイトル
- **description**: 要約。未記入の場合は本文冒頭の一部が自動で使われるが、検索エンジン最適化（SEO）のため自分で適切に書くことを推奨。ローマ字基準で135〜160文字、日本語は80〜110文字程度が目安。
- **date**: 正確な作成日時とタイムゾーン（省略可。省略時はファイルの作成日や更新日を自動取得）
- **categories**: カテゴリ分類
- **tags**: タグ分類
- **image**: 記事上部のプレビュー画像
  - **path**: 画像ファイルのパス
  - **alt**: 代替テキスト（省略可）
- **toc**: 右サイドバーの目次機能の有無。デフォルトは `true`
- **comments**: サイト既定とは別に、記事単位でコメント可否を明示したい場合に使用
- **math**: 内蔵の [MathJax](https://www.mathjax.org/) ベースの数式表示を有効化。ページ性能のためデフォルトは無効（`false`）
- **mermaid**: 内蔵の [Mermaid](https://github.com/mermaid-js/mermaid) ベースのダイアグラム表示を有効化。デフォルトは無効（`false`）

## 5. アップグレード

[3-2](#3-2-github-リポジトリ-作成)で1番の方法を採用した前提で述べる。2番の方法なら、前述のとおり最新のアップストリームタグを自分でマージする。

1. `Gemfile`{: .filepath} を編集し、"jekyll-theme-chirpy" gem のバージョンを新しいものに指定する。
2. メジャーアップグレードの場合は、"jekyll-theme-chirpy" gem に含まれないコアファイルや設定オプションも変更されている可能性がある。その場合は下記の GitHub の比較 URL で差分を確認し、手動で反映する。
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
