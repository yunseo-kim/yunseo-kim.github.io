---
title: Polyglotを使用してJekyllブログで多言語サポートを実装する方法 (1) - Polyglotプラグインの適用 & hreflang altタグ、サイトマップ、言語選択ボタンの実装
description: >-
  'jekyll-theme-chirpy'ベースのJekyllブログにPolyglotプラグインを適用して多言語サポートを実装したプロセスを紹介します。
  この投稿はシリーズの最初の記事で、Polyglotプラグインの適用とHTMLヘッダー、サイトマップの修正部分を扱います。
categories:
- Blogging
tags:
- Jekyll
- Polyglot
---
## 概要
約4ヶ月前の2024年7月初め、Jekyll基盤でGithub Pagesを通じてホスティングしているこのブログに[Polyglot](https://github.com/untra/polyglot)プラグインを適用して多言語サポートの実装を追加しました。
このシリーズでは、ChirpyテーマにPolyglotプラグインを適用する過程で発生したバグとその解決過程、そしてSEOを考慮したHTMLヘッダーとsitemap.xmlの作成方法を共有します。
シリーズは2つの記事で構成されており、この記事はそのシリーズの最初の記事です。
- 第1回：Polyglotプラグインの適用 & hreflang altタグ、サイトマップ、言語選択ボタンの実装（本文）
- 第2回：[Chirpyテーマのビルド失敗と検索機能エラーのトラブルシューティング](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## 要件
- [x] ビルドした結果物（ウェブページ）を言語別のパス（例：`/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）で区別して提供できること。
- [x] 多言語サポートに追加的に必要な時間と労力を可能な限り最小化するために、作成した原本のマークダウンファイルのYAML front matterに'lang'および'permalink'タグを一つ一つ指定しなくても、ビルド時に該当ファイルが位置するローカルパス（例：`/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）に応じて自動的に言語を認識できること。
- [x] サイト内の各ページのヘッダー部分は適切なContent-Languageメタタグとhreflang代替タグを含み、Googleの多言語検索のためのSEOガイドラインを満たすこと。
- [x] サイト内で各言語をサポートするすべてのページリンクを漏れなく`sitemap.xml`で提供できること、また`sitemap.xml`自体は重複なくルートパスに1つだけ存在すること。
- [x] [Chirpyテーマ](https://github.com/cotes2020/jekyll-theme-chirpy)で提供されるすべての機能が各言語ページで正常に動作すること。そうでない場合は正常に動作するように修正すること。
  - [x] 'Recently Updated'、'Trending Tags'機能が正常に動作すること
  - [x] GitHub Actionsを使用したビルドプロセスでエラーが発生しないこと
  - [x] ブログ右上の投稿検索機能が正常に動作すること

## Polyglotプラグインの適用
Jekyllは多言語ブログを基本的にサポートしていないため、上記の要件を満たす多言語ブログの実装には外部プラグインを活用する必要があります。検索してみると、[Polyglot](https://github.com/untra/polyglot)が多言語ウェブサイト実装用途で多く使用されており、上記の要件のほとんどを満たすことができるため、このプラグインを採用しました。

### プラグインのインストール
私はBundlerを使用しているため、`Gemfile`に次の内容を追加しました。

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

その後、ターミナルで`bundle update`を実行すると自動的にインストールが完了します。

Bundlerを使用しない場合は、ターミナルで`gem install jekyll-polyglot`コマンドでgemを直接インストールした後、`_config.yml`に次のようにプラグインを追加することもできます。

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 設定の構成
次に、`_config.yml`ファイルを開き、以下の内容を追加します。

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: サポートしたい言語のリスト
- default_lang: デフォルトのフォールバック言語
- exclude_from_localization: ローカライゼーション対象から除外するルートファイル/フォルダパス文字列の正規表現指定
- parallel_localization: ビルドプロセスで多言語処理を並列化するかどうかを指定するブール値
- lang_from_path: ブール値で、'true'に設定すると、投稿マークダウンファイル内にYAML front matterで'lang'属性を別途明示しなくても、該当マークダウンファイルのパス文字列が言語コードを含んでいれば、これを自動的に認識して使用する

> [サイトマッププロトコルの公式ドキュメント](https://www.sitemaps.org/protocol.html#location)では、次のように明記されています。
>
>> "サイトマップファイルの場所は、そのサイトマップに含めることができるURLのセットを決定します。http://example.com/catalog/sitemap.xmlにあるサイトマップファイルは、http://example.com/catalog/で始まる任意のURLを含めることができますが、http://example.com/images/で始まるURLは含めることができません。"
>
>> "サイトマップをウェブサーバーのルートディレクトリに配置することを強く推奨します。"
>
> これを遵守するためには、同じ内容の`sitemap.xml`ファイルが言語別に作成されず、ルートディレクトリに1つだけ存在するように'exclude_from_localization'リストに追加して、以下の誤った例のようにならないようにする必要があります。
>
> 誤った例（各ファイルの内容は言語別に異なるものではなく、すべて同じ）：
> - /sitemap.xml
> - /ko/sitemap.xml
> - /es/sitemap.xml
> - /pt-BR/sitemap.xml
> - /ja/sitemap.xml
> - /fr/sitemap.xml
> - /de/sitemap.xml
{: .prompt-tip }

> 'parallel_localization'を'true'に指定するとビルド時間が大幅に短縮されるメリットがありますが、2024年7月時点で、このブログに対してこの機能を有効にした場合、ページ右側のサイドバーの'Recently Updated'と'Trending Tags'部分のリンクタイトルが正常に処理されず、他の言語と混ざってしまうバグがありました。まだ安定化が不十分なようですので、サイトに適用する前に事前にテストを行う必要があります。また、[Windowsを使用する場合もこの機能がサポートされていないため、無効化する必要があります](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

また、[Jekyll 4.0では以下のようにCSSソースマップの生成を無効化する必要があります](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 投稿作成時の注意点
多言語投稿作成時に注意すべき点は以下の通りです。
- 適切な言語コードの指定：ファイルパス（例：`/_posts/ko/example-post.md`{: .filepath}）またはYAML front matterの'lang'属性（例：`lang: ko`）を使用して、適切なISO言語コードを指定する必要があります。[Chrome開発者ドキュメント](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)の例を参考にしてください。

> ただし、[Chrome開発者ドキュメント](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)では地域コードを'pt_BR'のような形式で表記していますが、実際には'pt-BR'のように_の代わりに-を使用する必要があります。これは後でHTMLヘッダーにhreflang代替タグを追加する際に正常に動作するためです。

- ファイルパスと名前は一貫性がある必要があります。

詳細については、GitHub [untra/polyglotリポジトリのREADME](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)を参照してください。

## HTMLヘッダーとサイトマップの修正
次に、SEOのためにブログ内の各ページのHTMLヘッダーにContent-Languageメタタグとhreflang代替タグを挿入する必要があります。

### HTMLヘッダー
2024年11月時点の最新バージョンである1.8.1リリース基準で、Polyglotはページヘッダー部分で{% raw %}`{% I18n_Headers %}`{% endraw %} Liquidタグを呼び出す際に上記の作業を自動的に行う機能があります。
しかし、これはそのページに'permalink'属性タグを明示的に指定していることを前提としており、そうでない場合は正常に動作しません。

したがって、私は[ChirpyテーマのHead.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)を取得した後、以下のように直接内容を追加しました。
[Polyglot公式ブログのSEO Recipesページ](https://polyglot.untra.io/seo/)を参考に作業しましたが、`page.permalink`がない場合は`page.url`属性を代わりに使用するように修正しました。
また、[Google Search Central公式ドキュメント](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault)を参考に、サイトのデフォルト言語ページに対するhreflang属性値として`site.default_lang`の代わりに`x-default`を指定することで、サイトがサポートする言語リストに訪問者の優先言語がない場合や訪問者の優先言語を認識できない場合のフォールバックとして該当ページリンクを認識するようにしました。

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="x-default" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### サイトマップ
Jekyllでビルド時に自動生成されるサイトマップは多言語ページを正常にサポートしないため、ルートディレクトリに`sitemap.xml`ファイルを作成し、以下のように内容を入力します。

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- This loops through all site collections including posts -->{% endcomment %}
    {% for collection in site.collections %}
        {% for node in site[collection.label] %}
            <url>
                <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
            </url>
        {% endfor %}
    {% endfor %}

{% endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## サイドバーに言語選択ボタンを追加
`_includes/lang-selector.html`ファイルを作成し、以下のように内容を入力しました。

{% raw %}
```liquid
<p>
{%- for lang in site.languages -%}
  {%- if lang == site.default_lang -%}
<a ferh="{{ page.url }}" style="display:inline-block; white-space:nowrap;">
    {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- else -%}
<a href="/{{ lang }}{{ page.url }}" style="display:inline-block; white-space:nowrap;">
  {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- endif -%}
{%- endfor -%}
</p>
```
{: file='_includes/lang-selector.html'}
{% endraw %}

次に、[Chirpyテーマの`_includes/sidebar.html`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html)の"sidebar-bottom"クラス部分に以下の3行を追加して、先ほど作成した`_includes/lang-selector.html`の内容をJekyllがページビルド時に読み込むようにしました。

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## さらなる読み物
[パート2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)に続きます
