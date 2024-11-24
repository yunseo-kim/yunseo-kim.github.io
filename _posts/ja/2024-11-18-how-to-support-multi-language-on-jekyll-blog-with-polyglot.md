---
title: Polyglotを使用してJekyllブログで多言語サポートを実装する方法
description: >-
  'jekyll-theme-chirpy'ベースのJekyllブログにPolyglotプラグインを適用して多言語サポートを実装したプロセスを紹介します。
categories:
- Blogging
tags:
- Jekyll
- Polyglot
- RegExp
---
## はじめに
約4ヶ月前の2024年7月初め、JekyllベースでGithub Pagesを通じてホスティング中の本ブログに[Polyglot](https://github.com/untra/polyglot)プラグインを適用して多言語サポートの実装を追加しました。
この記事では、ChirpyテーマにPolyglotプラグインを適用する過程で発生したバグとその解決過程、そしてSEOを考慮したhtmlヘッダーとsitemap.xmlの作成方法を共有します。

## 要件
- [x] ビルドした結果物（ウェブページ）を言語別のパス（例：`/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）で区別して提供できること。
- [x] 多言語サポートに追加的に必要な時間と労力を可能な限り最小化するため、作成したオリジナルのマークダウンファイルのYAML front matterに'lang'および'permalink'タグを一つ一つ指定しなくても、ビルド時にそのファイルが位置するローカルパス（例：`/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）に応じて自動的に言語を認識できること。
- [x] サイト内の各ページのヘッダー部分は、適切なContent-Languageメタタグとhreflang代替タグを含め、Googleの多言語検索のためのSEOガイドラインを満たすこと。
- [x] サイト内で各言語をサポートするすべてのページリンクを漏れなく`sitemap.xml`で提供できること、また`sitemap.xml`自体は重複なくルートパスに1つだけ存在すること。
- [ ] [Chirpyテーマ](https://github.com/cotes2020/jekyll-theme-chirpy)で提供されるすべての機能が各言語ページで正常に動作すること。そうでない場合は正常に動作するように修正すること。
  - [x] 'Recently Updated'、'Trending Tags'などの機能が正常に動作すること
  - [x] GitHub Actionsを利用したビルド過程でサイト内部リンクのエラー検証時、偽陽性（False Positive）警告が発生しないこと
  - [ ] ブログ右上の投稿検索機能が正常に動作すること

## Polyglotプラグインの適用
Jekyllは多言語ブログを基本サポートしていないため、上記の要件を満たす多言語ブログの実装には外部プラグインを活用する必要があります。検索してみると[Polyglot](https://github.com/untra/polyglot)が多言語ウェブサイト実装用途でよく使われており、上記の要件のほとんどを満たすことができるため、このプラグインを採用しました。

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
次に`_config.yml`ファイルを開き、以下の内容を追加します。

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: サポートしたい言語リスト
- default_lang: デフォルトのフォールバック言語
- exclude_from_localization: ローカライゼーション対象から除外するルートファイル/フォルダパス文字列の正規表現指定
- parallel_localization: ビルド過程で多言語処理を並列化するかどうかを指定するブール値
- lang_from_path: ブール値で、'true'に設定すると投稿マークダウンファイル内にYAML front matterで'lang'属性を別途明示しなくても、該当マークダウンファイルのパス文字列が言語コードを含む場合、これを自動的に認識して使用する

> [Sitemapプロトコル公式ドキュメント](https://www.sitemaps.org/protocol.html#location)では次のように明記されています。
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> これを遵守するためには、同一内容の`sitemap.xml`ファイルが言語別に作成されずにルートディレクトリに1つだけ存在するように'exclude_from_localization'リストに追加して、以下の誤った例のようにならないようにする必要があります。
>
> 誤った例（各ファイルの内容は言語別に異なるわけではなく、すべて同じ）：
> - https://www.yunseo.kim/sitemap.xml
> - https://www.yunseo.kim/ko/sitemap.xml
> - https://www.yunseo.kim/es/sitemap.xml
> - https://www.yunseo.kim/pt-BR/sitemap.xml
> - https://www.yunseo.kim/ja/sitemap.xml
> - https://www.yunseo.kim/fr/sitemap.xml
> - https://www.yunseo.kim/de/sitemap.xml
{: .prompt-tip }

> 'parallel_localization'を'true'に指定するとビルド時間がかなり短縮されるメリットがありますが、2024年7月時点で本ブログに対して該当機能を有効にした際、ページ右側のサイドバーの'Recently Updated'と'Trending Tags'部分のリンクタイトルが正常に処理されず、他の言語と混ざってしまうバグがありました。まだ安定化が不十分なようですので、サイトに適用する前にあらかじめ正常に動作するかテストを行う必要があります。また、[Windowsを使用する場合も該当機能がサポートされないため、無効化する必要があります](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

また、[Jekyll 4.0では次のようにCSSソースマップの生成を無効化する必要があります](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 投稿作成時の注意点
多言語投稿作成時に注意すべき点は次の通りです。
- 適切な言語コードの指定：ファイルパス（例：`/_posts/ko/example-post.md`{: .filepath}）またはYAML front matterの'lang'属性（例：`lang: ko`）を利用して適切なISO言語コードを指定する必要があります。[Chrome開発者ドキュメント](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)の例を参考にしてください。

> ただし、[Chrome開発者ドキュメント](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)では地域コードを'pt_BR'のような形式で表記していますが、実際には'pt-BR'のように_の代わりに-を使用しなければ、後にhtmlヘッダーにhreflang代替タグを追加する際に正常に動作しません。

- ファイルパスと名前は一貫性がなければなりません。

詳細については、GitHub [untra/polyglotリポジトリのREADME](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)を参照してください。

## トラブルシューティング（'relative_url_regex': target of repeat operator is not specified）
前段階まで進めた後、`bundle exec jekyll serve`コマンドを実行してビルドテストを行ったところ、`'relative_url_regex': target of repeat operator is not specified`というエラーが発生し、ビルドに失敗しました。

```shell
...(前略)
                    ------------------------------------------------
      Jekyll 4.3.4   Please append `--trace` to the `serve` command 
                     for any additional information or backtrace. 
                    ------------------------------------------------
/Users/yunseo/.gem/ruby/3.2.2/gems/jekyll-polyglot-1.8.1/lib/jekyll/polyglot/
patches/jekyll/site.rb:234:in `relative_url_regex': target of repeat operator 
is not specified: /href="?\/((?:(?!*.gem)(?!*.gemspec)(?!tools)(?!README.md)(
?!LICENSE)(?!*.config.js)(?!rollup.config.js)(?!package*.json)(?!.sass-cache)
(?!.jekyll-cache)(?!gemfiles)(?!Gemfile)(?!Gemfile.lock)(?!node_modules)(?!ve
ndor\/bundle\/)(?!vendor\/cache\/)(?!vendor\/gems\/)(?!vendor\/ruby\/)(?!en\/
)(?!ko\/)(?!es\/)(?!pt-BR\/)(?!ja\/)(?!fr\/)(?!de\/)[^,'"\s\/?.]+\.?)*(?:\/[^
\]\[)("'\s]*)?)"/ (RegexpError)

...(後略)
```

同様の問題が報告されたことがあるか検索した結果、Polyglotリポジトリに[全く同じ問題](https://github.com/untra/polyglot/issues/204)が既に登録されており、解決策も存在しました。

本ブログに適用中の[Chirpyテーマの`_config.yml`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml)ファイルには次のような構文が存在します。

```yml
exclude:
  - "*.gem"
  - "*.gemspec"
  - docs
  - tools
  - README.md
  - LICENSE
  - "*.config.js"
  - package*.json
```
{: file='_config.yml'}

問題の原因は[Polyglotの`site.rb`](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb)ファイルに含まれる次の2つの関数の正規表現構文が、上記の`"*.gem"`、`"*.gemspec"`、`"*.config.js"`のようにワイルドカードを含むグロビング（globbing）パターンを正常に処理できないことにあります。

{% raw %}
```ruby
    # a regex that matches relative urls in a html document
    # matches href="baseurl/foo/bar-baz" href="/foo/bar-baz" and others like it
    # avoids matching excluded files.  prepare makes sure
    # that all @exclude dirs have a trailing slash.
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    # a regex that matches absolute urls in a html document
    # matches href="http://baseurl/foo/bar-baz" and others like it
    # avoids matching excluded files.  prepare makes sure
    # that all @exclude dirs have a trailing slash.
    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(polyglot root path)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

この問題を解決する方法は2つあります。

### 1. Polyglotをフォーク（fork）した後、問題となる部分を修正して使用
この記事を書いている時点（2024.11.）基準で[Jekyll公式ドキュメント](https://jekyllrb.com/docs/configuration/options/#global-configuration)では、`exclude`設定がグロビング（globbing）パターンの活用をサポートすると明記しています。

>"This configuration option supports Ruby's File.fnmatch filename globbing patterns to match multiple entries to exclude."

つまり、問題の原因はChirpyテーマではなく、Polyglotの`relative_url_regex()`、`absolute_url_regex()`の2つの関数にあるため、これらを問題が発生しないように修正することが根本的な解決策です。

Polyglotでは該当バグはまだ解決されていない状態なので、[このブログ投稿](https://hionpu.com/en/posts/github_blog_4#4-polyglot-dependency-issue)と[前述のGitHubイシューに付いた回答](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322)を参考にして、Polyglotリポジトリをフォーク（fork）した後、問題となる部分を次のように修正して元のPolyglotの代わりに使用すればよいです。

{% raw %}
```ruby
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(polyglot root path)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

### 2. Chirpyテーマの`_config.yml`設定ファイルでグロビング（globbing）パターンを正確なファイル名に置き換える
実際、正攻法で理想的な方法は上記のパッチがPolyglotのメインストリームに反映されることです。しかし、それまではフォークしたバージョンを代わりに使用しなければなりませんが、この場合、Polyglotのアップストリームがバージョンアップするたびにその更新を見逃さずに反映しながらフォローするのが面倒なため、私は別の方法を使用しました。

[Chirpyテーマリポジトリ](https://github.com/cotes2020/jekyll-theme-chirpy)でプロジェクトのルートパスに位置するファイルのうち、`"*.gem"`、`"*.gemspec"`、`"*.config.js"`パターンに対応するファイルを確認してみると、どうせ以下の3つしかありません。
- `jekyll-theme-chirpy.gemspec`
- `purgecss.config.js`
- `rollup.config.js`

したがって、`_config.yml`ファイルの`exclude`構文からグロビング（globbing）パターンを削除し、以下のように書き換えれば、Polyglotが問題なく処理できるようになります。

```yml
exclude: # https://github.com/untra/polyglot/issues/204 イシューを参考に修正。
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```

## htmlヘッダーおよびsitemapの修正
次に、SEOのためにブログ内の各ページのhtmlヘッダーにContent-Languageメタタグとhreflang代替タグを挿入する必要があります。

### htmlヘッダー
2024.11.基準の最新バージョンである1.8.1リリース基準で、Polyglotはページヘッダー部分で{% raw %}`{% I18n_Headers %}`{% endraw %}Liquidタグ呼び出し時に上記の作業を自動的に行う機能があります。
しかし、これは該当ページに'permalink'属性タグを明示して指定したことを前提としており、そうでない場合は正常に動作しません。

したがって、私は[Chirpyテーマの`head.html`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)を持ってきた後、以下のように直接内容を追加しました。
[Polyglot公式ブログのSEO Recipesページ](https://polyglot.untra.io/seo/)を参考に作業しましたが、`page.permalink`がない場合は`page.url`属性を代わりに使用するように修正しました。
また、[Google Search Central公式ドキュメント](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault)を参考にして、サイトのデフォルト言語ページに対するhreflang属性値として`site.default_lang`の代わりに`x-default`を指定することで、サイトがサポートする言語リストに訪問者の好みの言語がない場合や、訪問者の好みの言語を認識できない場合のフォールバックとして該当ページリンクを認識するようにしました。

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

### sitemap
Jekyllでビルド時に自動生成するsitemapは多言語ページを正常にサポートしないため、ルートディレクトリに`sitemap.xml`ファイルを作成し、次のように内容を入力します。

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
`_includes/lang-selector.html`ファイルを作成し、次のように内容を入力しました。

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

次に、[Chirpyテーマの`_includes/sidebar.html`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html)の"sidebar-bottom"クラス部分に次の3行を追加して、先ほど作成した`_includes/lang-selector.html`の内容をJekyllがページビルド時に読み込むようにしました。

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## 検索機能使用時に多言語ページを正常にインデックスできない問題
前段階まで進めた時点でほとんどのサイト機能が意図した通り満足に動作しました。しかし、Chirpyテーマを適用したページ右上に位置する検索バーが`site.default_lang`（本ブログの場合は英語）以外の言語で書かれたページをインデックスできず、英語以外の他の言語で検索した場合も検索結果として英語ページを出力するという問題があることを後で発見しました。

これは、Chirpyテーマで活用している[Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search)JavaScriptライブラリがJekyllで提供する`site.posts`変数に依存してインデックスを行うため、Polyglotを使用してビルドしたデフォルト言語以外の多言語ページを認識できずに発生する問題です。

[`search.json`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/assets/js/data/search.json)という単一のliquidテンプレートでJekyllが基本提供する変数のみに依存してインデックスを行うSimple-Jekyll-Searchの単純な構造は長所でもありますが、今回の場合は致命的な短所であり限界として作用し、したがって本ブログに適用するには不適切です。JekyllがMultilingual Pagesを基本サポートせず、Polyglotが`site.posts`を代替できる何か別の変数をサポートしない限り、Simple-Jekyll-Searchは本ブログで要求する多言語ページのインデックスを適切に行うことができないと判断します。そのため、Simple-Jekyll-Searchを代替できる代案を探索して適用する必要があり、これは後続の課題であり投稿テーマとして残しておきます。
