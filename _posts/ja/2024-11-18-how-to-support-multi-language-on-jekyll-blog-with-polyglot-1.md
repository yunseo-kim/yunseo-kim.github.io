---
title: "PolyglotでJekyllブログの多言語対応を実現する方法 (1) - Polyglotプラグインの適用 & htmlヘッダー及びsitemapの修正"
description: "'jekyll-theme-chirpy'ベースのJekyllブログにPolyglotプラグインを適用して多言語対応を実装した過程を紹介する。この投稿は該当シリーズの最初の記事として、Polyglotプラグインを適用し、htmlヘッダーとsitemapを修正する部分を扱う。"
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## 概要
12024年7月初旬、Jekyll基盤でGitHub Pagesを通じてホスティング中の本ブログに[Polyglot](https://github.com/untra/polyglot)プラグインを適用して多言語対応実装を追加した。
このシリーズはChirpyテーマにPolyglotプラグインを適用する過程で発生したバグとその解決過程、そしてSEOを考慮したhtmlヘッダーとsitemap.xmlの作成法を共有する。
シリーズは3つの記事で構成されており、読んでいるこの記事は該当シリーズの最初の記事である。
- 1編：Polyglotプラグインの適用 & htmlヘッダー及びsitemapの修正（本文）
- 2編：[言語選択ボタンの実装 & レイアウト言語の現地化](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- 3編：[Chirpyテーマビルド失敗及び検索機能エラーのトラブルシューティング](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> 元々は全2編で構成していたが、その後数回にわたって内容を補強したことにより分量が大幅に増加したため、3編に改編した。
{: .prompt-info }

## 要求条件
- [x] ビルドした結果物（ウェブページ）を言語別パス（例：`/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）で区分して提供できなければならない。
- [x] 多言語対応に追加的に要する時間と労力を可能な限り最小化するため、作成した原本マークダウンファイルのYAML front matterに'lang'及び'permalink'タグを一々指定しなくても、ビルド時に該当ファイルが位置するローカルパス（例：`/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）に応じて自動的に言語を認識できなければならない。
- [x] サイト内各ページのヘッダー部分は適切なContent-Languageメタタグとhreflang代替タグ、canonical linkを含んで多言語検索のためのGoogle SEOガイドラインを満たさなければならない。
- [x] サイト内で各言語バージョン別ページリンクを漏れなく`sitemap.xml`{: .filepath}で提供できなければならず、`sitemap.xml`{: .filepath}自体は重複なくルートパスに一つだけ存在しなければならない。
- [x] [Chirpyテーマ](https://github.com/cotes2020/jekyll-theme-chirpy)で提供するすべての機能は各言語ページで正常動作しなければならず、そうでなければ正常動作するよう修正しなければならない。
  - [x] 'Recently Updated'、'Trending Tags'機能の正常動作
  - [x] GitHub Actionsを利用したビルド過程でエラーが発生しないこと
  - [x] ブログ右上の投稿検索機能の正常動作

## Polyglotプラグインの適用
Jekyllは多言語ブログを基本サポートしないため、上記の要求事項を満たす多言語ブログ実装のためには外部プラグインを活用しなければならない。検索してみると[Polyglot](https://github.com/untra/polyglot)が多言語ウェブサイト実装用途で多く使われており、上記要求事項をほぼ満たすことができるため、該当プラグインを採択した。

### プラグインのインストール
私はBundlerを使用中なので`Gemfile`に次の内容を追加した。

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

その後ターミナルで`bundle update`を実行すると自動的にインストールが完了する。

もしBundlerを使用しない場合、ターミナルで`gem install jekyll-polyglot`コマンドでgemを直接インストールした後、`_config.yml`{: .filepath}に次のようにプラグインを追加することもできる。

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 設定構成
次に`_config.yml`{: .filepath}ファイルを開いて下記内容を追加する。

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`：サポートしたい言語リスト
- `default_lang`：基本fallback言語
- `exclude_from_localization`：言語ローカライゼーション対象から除外するルートファイル/フォルダパス文字列正規表現指定
- `parallel_localization`：ビルド過程で多言語処理を並列化するかどうかを指定するboolean値
- `lang_from_path`：boolean値で、'true'に設定すると投稿マークダウンファイル内にYAML front matterで'lang'属性を別途明示しなくても、該当マークダウンファイルのパス文字列が言語コードを含んでいればこれを自動的に認識して使用する

> [Sitemapプロトコル公式文書](https://www.sitemaps.org/protocol.html#location)では次のように明示している。
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> これを遵守するためには同一内容の`sitemap.xml`{: .filepath}ファイルが言語別に作られず、ルートディレクトリに一つだけ存在するよう'exclude_from_localization'リストに追加して、下記の間違った例のようにならないようにしなければならない。
>
> 間違った例（各ファイルの内容は言語別に異ならず、すべて同一）：
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> （12025.01.14. アップデート）[上述した内容をREADMEに補強して提出したPull Request](https://github.com/untra/polyglot/pull/230)が受け入れられたことにより、今では[Polyglot公式文書](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation)でも同じ案内を確認できる。
{: .prompt-tip }

> 'parallel_localization'を'true'に指定するとビルド時間が相当短縮される利点があるが、12024年7月時点基準で本ブログに対して該当機能を有効化した時、ページ右側サイドバーの'Recently Updated'と'Trending Tags'部分のリンクタイトルが正常に処理されず他の言語と混在するバグがあった。まだ安定化が不十分なようなので、サイトに適用するなら事前に正常動作するかテストを経る必要がある。また[Windowsを使用する場合にも該当機能がサポートされないため無効化しなければならない](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

また[Jekyll 4.0では次のようにCSS sourcemaps生成を無効化しなければならない](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 投稿作成時の注意事項
多言語投稿作成時に注意すべき点は次の通りである。
- 適切な言語コード指定：ファイルパス（例：`/_posts/ko/example-post.md`{: .filepath}）またはYAML front matterの'lang'属性（例：`lang: ko`）を利用して適切なISO言語コードを指定してあげなければならない。[Chrome開発者文書](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)の例を参考にする。

> ただし、[Chrome開発者文書](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)では地域コードを'pt_BR'のような形式で表記しているが、実際には'pt-BR'のように_の代わりに-を使用しなければ、後でhtmlヘッダーにhreflang代替タグを追加する時に正常動作する。
{: .prompt-tip }

- ファイルパスと名前は一貫していなければならない。

詳細事項はGitHub [untra/polyglotリポジトリのREADME](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)を参考してほしい。

## htmlヘッダー及びsitemapの修正
今度はSEOのためにブログ内各ページのhtmlヘッダーにContent-Languageメタタグとhreflang代替タグを挿入し、標準URL（canonical URL）を適切に指定しなければならない。

### htmlヘッダー
12024.11.時点で最新バージョンである1.8.1リリース基準で、Polyglotはページヘッダー部分で{% raw %}`{% I18n_Headers %}`{% endraw %} Liquidタグ呼び出し時に上記作業を自動的に実行してくれる機能がある。
しかしこれは該当ページに'permalink'属性タグを明示して指定したことを想定しており、そうでない場合は正常動作しない。

したがって私は[ChirpyテーマのHead.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)を持ってきた後、下記のように直接内容を追加した。
[Polyglot公式ブログのSEO Recipesページ](https://polyglot.untra.io/seo/)を参考にして作業したが、私の使用環境及び要求条件に合わせて`page.permalink`の代わりに`page.url`属性を使用するよう修正した。

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">
  
  {% if site.default_lang -%}
  <link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />
  {%- endif -%}
  {% for lang in site.languages -%}
    {% if lang == site.default_lang -%}
      {%- continue -%}
    {%- endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {%- endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

（12025.07.29. 追加）またChirpyテーマは[Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag)プラグインを基本内蔵しているが、Jekyll SEO Tagが自動生成する`og:locale`、`og:url` [Open Graph](https://ogp.me/)メタデータ属性及び[標準URL（canonical URL）](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)（`rel="canonical"` `link`要素）がサイト基本言語（`site.lang`、`site.default_lang`）基準なので追加的な処理が必要であることを確認した。  
したがって{% raw %}`{{ seo_tags }}`{% endraw %}の前に次の構文を追加した。

{% raw %}
```liquid
(前略)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(中略)...

  {%- capture old_og_locale -%}
    <meta property="og:locale" content="{{site.lang}}" />
  {%- endcapture -%}
  {%- capture new_og_locale -%}
    <meta property="og:locale" content="{{site.active_lang}}" />
    {% for lang in site.languages -%}
      {%- if lang == site.active_lang -%}
        {%- continue -%}
      {%- endif %}
    <meta property="og:locale:alternate" content="{{lang}}" />
    {%- endfor %}
  {%- endcapture -%}
  {% assign seo_tags = seo_tags | replace: old_og_locale, new_og_locale %}
  
  {% unless site.active_lang == site.default_lang -%}
    {%- capture old_canonical_link -%}
      <link rel="canonical" href="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture old_og_url -%}
      <meta property="og:url" content="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_canonical_link -%}
      <link rel="canonical" href="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_og_url -%}
      <meta property="og:url" content="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {% assign seo_tags = seo_tags | replace: old_canonical_link, new_canonical_link %}
    {% assign seo_tags = seo_tags | replace: old_og_url, new_og_url %}
  {%- endunless %}

  {{ seo_tags }}

  ...(後略)
```
{: file='/_includes/head.html'}
{% endraw %}

> [Google開発者文書](https://developers.google.com/search/docs/crawling-indexing/canonicalization)によると、一つのページに複数の言語バージョンがある時は主要コンテンツの言語が同じ場合、すなわちヘッダー、フッター、その他重要でないテキストのみ翻訳されており本文が同一の場合にのみ重複と見なす。したがって今このブログのように本文テキストを複数言語で提供する場合には、各言語バージョンすべて重複ではない独立的なページとして見なすので、言語によって異なる標準URLを指定しなければならない。  
> 例えば今このページの日本語バージョンの場合、標準URLは"{{site.url}}{{page.url}}"ではなく"{{site.url}}/ja{{page.url}}"である。
{: .prompt-tip }

### sitemap
別途テンプレートを指定しない場合、Jekyllでビルド時に自動生成するsitemapは多言語ページを正常サポートしないため、ルートディレクトリに`sitemap.xml`{: .filepath}ファイルを生成し、次のように内容を入力する。

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages -%}

  {% for node in site.pages %}
    {%- comment -%}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{%- endcomment -%}
    {%- comment -%}<!-- Exclude redirects from sitemap -->{%- endcomment -%}
    {%- if node.redirect.to -%}
      {%- continue -%}
    {%- endif -%}
    {%- unless site.exclude_from_localization contains node.path -%}
      {%- comment -%}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{%- endcomment -%}
      {% if node.layout %}
        <url>
          <loc>
            {%- if lang == site.default_lang -%}
              {{ node.url | absolute_url }}
            {%- else -%}
              {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
            {%- endif -%}
          </loc>
          {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {% endif -%}
          {% if site.default_lang -%}
          <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
          {%- endif -%}
          {% for lang in site.languages -%}
            {% if lang == site.default_lang -%}
              {%- continue -%}
            {%- endif %}
          <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
          {%- endfor %}
        </url>
      {% endif %}
    {%- elsif site.default_lang -%}
        <url>
          <loc>{{ node.url | absolute_url }}</loc>
      {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {% endif -%}
        </url>
    {%- endunless -%}
  {% endfor %}

  {%- comment -%}<!-- This loops through all site collections including posts -->{%- endcomment -%}
  {% for collection in site.collections %}
    {% for node in site[collection.label] %}
      <url>
        <loc>
          {%- if lang == site.default_lang -%}
            {{ node.url | absolute_url }}
          {%- else -%}
            {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
          {%- endif -%}
        </loc>
        {% if node.last_modified_at and node.last_modified_at != node.date -%}
        <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- elsif node.date -%}
        <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- endif %}
        {% if site.default_lang -%}
        <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
        {%- endif -%}
        {% for lang in site.languages -%}
          {% if lang == site.default_lang -%}
            {%- continue -%}
          {%- endif %}
        <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
        {%- endfor %}
      </url>
    {% endfor %}
  {% endfor %}

{%- endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## Further Reading
[Part 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)に続く
