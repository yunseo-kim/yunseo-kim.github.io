---
title: Polyglotを使ってJekyllブログで多言語サポートを実装する方法 (1) - Polyglotプラグインの適用 & hreflang altタグおよびsitemap、言語選択ボタンの実装
description: "'jekyll-theme-chirpy'ベースのJekyllブログにPolyglotプラグインを適用して多言語サポートを実装した過程を紹介します。この投稿はそのシリーズの最初の記事で、Polyglotプラグインを適用し、htmlヘッダーとsitemapを修正する部分を扱います。'"
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## 概要
約4ヶ月前の[人類暦](https://en.wikipedia.org/wiki/Holocene_calendar)12024年7月初め、JekyllベースでGithub Pagesを通じてホスティングしている本ブログに[Polyglot](https://github.com/untra/polyglot)プラグインを適用して多言語サポートの実装を追加しました。
このシリーズは、ChirpyテーマにPolyglotプラグインを適用する過程で発生したバグとその解決過程、そしてSEOを考慮したhtmlヘッダーとsitemap.xmlの作成方法を共有します。
シリーズは2つの記事で構成されており、この記事はそのシリーズの最初の記事です。
- 第1回：Polyglotプラグインの適用 & hreflang altタグおよびsitemap、言語選択ボタンの実装（本文）
- 第2回：[Chirpyテーマのビルド失敗および検索機能エラーのトラブルシューティング](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## 要件
- [x] ビルドした結果物（ウェブページ）を言語別のパス（例：`/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）で区別して提供できること。
- [x] 多言語サポートに追加的に必要な時間と労力を可能な限り最小化するために、作成した原本のマークダウンファイルのYAML front matterに'lang'および'permalink'タグを一々指定しなくても、ビルド時に該当ファイルが位置するローカルパス（例：`/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）に応じて自動的に言語を認識できること。
- [x] サイト内の各ページのヘッダー部分は適切なContent-Languageメタタグとhreflang代替タグを含み、Googleの多言語検索のためのSEOガイドラインを満たすこと。
- [x] サイト内で各言語をサポートするすべてのページリンクを漏れなく`sitemap.xml`{: .filepath}で提供できること、また`sitemap.xml`{: .filepath}自体は重複なくルートパスに1つだけ存在すること。
- [x] [Chirpyテーマ](https://github.com/cotes2020/jekyll-theme-chirpy)で提供されるすべての機能が各言語ページで正常に動作すること。そうでない場合は正常に動作するように修正すること。
  - [x] 'Recently Updated'、'Trending Tags'機能の正常動作
  - [x] GitHub Actionsを利用したビルドプロセスでエラーが発生しないこと
  - [x] ブログ右上の投稿検索機能の正常動作

## Polyglotプラグインの適用
Jekyllは多言語ブログを基本サポートしていないため、上記の要件を満たす多言語ブログ実装のためには外部プラグインを活用する必要があります。検索してみると[Polyglot](https://github.com/untra/polyglot)が多言語ウェブサイト実装用途でよく使われており、上記の要件のほとんどを満たすことができるため、このプラグインを採用しました。

### プラグインのインストール
私はBundlerを使用しているため、`Gemfile`に次の内容を追加しました。

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

その後、ターミナルで`bundle update`を実行すると自動的にインストールが完了します。

もしBundlerを使用しない場合、ターミナルで`gem install jekyll-polyglot`コマンドでgemを直接インストールした後、`_config.yml`{: .filepath}に次のようにプラグインを追加することもできます。

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 設定の構成
次に`_config.yml`{: .filepath}ファイルを開き、以下の内容を追加します。

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: サポートしたい言語リスト
- default_lang: デフォルトのフォールバック言語
- exclude_from_localization: ローカライゼーション対象から除外するルートファイル/フォルダパス文字列正規表現指定
- parallel_localization: ビルドプロセスで多言語処理を並列化するかどうかを指定するブール値
- lang_from_path: ブール値で、'true'に設定すると投稿マークダウンファイル内にYAML front matterで'lang'属性を別途明示しなくても、該当マークダウンファイルのパス文字列が言語コードを含んでいれば、これを自動的に認識して使用する

> [Sitemapプロトコル公式ドキュメント](https://www.sitemaps.org/protocol.html#location)では次のように明記されています。
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> これを遵守するためには、同じ内容の`sitemap.xml`{: .filepath}ファイルが言語別に作成されずにルートディレクトリに1つだけ存在するように'exclude_from_localization'リストに追加して、以下の誤った例のようにならないようにする必要があります。
>
> 誤った例（各ファイルの内容は言語別に異なるものではなく、すべて同じ）：
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> （12025.01.14. 更新）[上述の内容をREADMEに補強して提出したPull Request](https://github.com/untra/polyglot/pull/230)が受け入れられたため、現在は[Polyglot公式ドキュメント](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation)でも同じ案内を確認できます。
{: .prompt-tip }

> 'parallel_localization'を'true'に指定するとビルド時間がかなり短縮されるメリットがありますが、12024年7月時点で本ブログに対してこの機能を有効にした際、ページ右側のサイドバーの'Recently Updated'と'Trending Tags'部分のリンクタイトルが正常に処理されず、他の言語と混ざってしまうバグがありました。まだ安定化が不十分なようですので、サイトに適用する際は事前に正常動作するかテストを行う必要があります。また、[Windowsを使用する場合もこの機能がサポートされないため、無効化する必要があります](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

また、[Jekyll 4.0では次のようにCSSソースマップ生成を無効化する必要があります](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 投稿作成時の注意点
多言語投稿作成時に注意すべき点は次の通りです。
- 適切な言語コードの指定：ファイルパス（例：`/_posts/ko/example-post.md`{: .filepath}）またはYAML front matterの'lang'属性（例：`lang: ko`）を利用して適切なISO言語コードを指定する必要があります。[Chrome開発者ドキュメント](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)の例を参考にしてください。

> ただし、[Chrome開発者ドキュメント](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)では地域コードを'pt_BR'のような形式で表記していますが、実際には'pt-BR'のように_の代わりに-を使用する必要があります。これは後にHTMLヘッダーにhreflang代替タグを追加する際に正常に動作するためです。

- ファイルパスと名前は一貫性がある必要があります。

詳細については、GitHub [untra/polyglotリポジトリのREADME](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)を参照してください。

## HTMLヘッダーおよびsitemapの修正
次に、SEOのためにブログ内の各ページのHTMLヘッダーにContent-Languageメタタグとhreflang代替タグを挿入する必要があります。

### HTMLヘッダー
12024.11.時点で最新バージョンである1.8.1リリース基準で、Polyglotはページヘッダー部分で{% raw %}`{% I18n_Headers %}`{% endraw %} Liquidタグ呼び出し時に上記の作業を自動的に行う機能があります。
しかし、これは該当ページに'permalink'属性タグを明示的に指定したことを前提としており、そうでない場合は正常に動作しません。

したがって、私は[Chirpyテーマのhead.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)を取得した後、以下のように直接内容を追加しました。
[Polyglot公式ブログのSEO Recipesページ](https://polyglot.untra.io/seo/)を参考に作業しましたが、`page.permalink`がない場合は`page.url`属性を代わりに使用するように修正しました。

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### sitemap
Jekyllでビルド時に自動生成されるsitemapは多言語ページを正常にサポートしないため、ルートディレクトリに`sitemap.xml`{: .filepath}ファイルを作成し、次のように内容を入力します。

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
（12025.02.05. 更新）言語選択ボタンをドロップダウンリスト形式に改善しました。  
`_includes/lang-selector.html`{: .filepath}ファイルを作成し、次のように内容を入力しました。

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Select Language">
    {%- for lang in site.languages -%}
        <option value="{% if lang == site.default_lang %}{{ page.url }}{% else %}/{{ lang }}{{ page.url }}{% endif %}"
                {% if lang == site.active_lang %}selected{% endif %}>
            {% case lang %}
            {% when 'ko' %}🇰🇷 한국어
            {% when 'en' %}🇺🇸 English
            {% when 'ja' %}🇯🇵 日本語
            {% when 'zh-TW' %}🇹🇼 正體中文
            {% when 'es' %}🇪🇸 Español
            {% when 'pt-BR' %}🇧🇷 Português
            {% when 'fr' %}🇫🇷 Français
            {% when 'de' %}🇩🇪 Deutsch
            {% else %}{{ lang }}
            {% endcase %}
        </option>
    {%- endfor -%}
    </select>
</div>

<script>
function changeLang(url) {
    window.location.href = url;
}
</script>
```
{: file='_includes/lang-selector.html'}
{% endraw %}

また、`assets/css/lang-selector.css`{: .filepath}ファイルを作成し、次のように内容を入力しました。

```css
/**
 * 言語セレクタースタイル
 * 
 * サイドバーに位置する言語選択ドロップダウンのスタイルを定義します。
 * テーマのダークモードをサポートし、モバイル環境でも最適化されています。
 */

/* 言語セレクターコンテナ */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* ドロップダウンコンテナ */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* 選択入力要素 */
.lang-select {
    /* 基本スタイル */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* フォントと色 */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* 形状と相互作用 */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* 矢印アイコン追加 */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* 国旗絵文字スタイル */
.lang-select option {
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
    padding: 0.35rem;
    font-size: 1rem;
}

.lang-flag {
    display: inline-block;
    margin-right: 0.5rem;
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
}

/* ホバー状態 */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* フォーカス状態 */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Firefoxブラウザ対応 */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IEブラウザ対応 */
.lang-select::-ms-expand {
    display: none;
}

/* ダークモード対応 */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* モバイル環境最適化 */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* より大きなタッチ領域 */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* モバイルでより広い選択領域 */
    }
}
```
{: file='assets/css/lang-selector.css'}

次に、[Chirpyテーマの`_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html)の"sidebar-bottom"クラスの直前に次のように3行を追加して、先ほど作成した`_includes/lang-selector.html`{: .filepath}の内容をJekyllがページビルド時に読み込むようにしました。

{% raw %}
```liquid
  (前略)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(後略)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## さらなる読み物
[パート2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)に続きます
