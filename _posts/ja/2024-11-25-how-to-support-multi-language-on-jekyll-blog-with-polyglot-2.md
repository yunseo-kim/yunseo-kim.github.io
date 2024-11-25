---
title: Polyglotを使用してJekyllブログで多言語サポートを実装する方法 (2) - Chirpyテーマのビルド失敗と検索機能エラーのトラブルシューティング
description: >-
  'jekyll-theme-chirpy'ベースのJekyllブログにPolyglotプラグインを適用して多言語サポートを実装したプロセスを紹介します。
  この投稿はシリーズの2番目の記事で、Chirpyテーマにポリグロットを適用する際に発生したエラーの原因を特定し、解決する部分を扱います。
categories:
- Blogging
tags:
- Jekyll
- Polyglot
mermaid: true
---
## 概要
約4ヶ月前の2024年7月初め、Jekyll ベースでGithub Pagesを通じてホスティングしているこのブログに[Polyglot](https://github.com/untra/polyglot)プラグインを適用して多言語サポートの実装を追加しました。
このシリーズは、Chirpyテーマにポリグロットプラグインを適用するプロセスで発生したバグとその解決過程、そしてSEOを考慮したhtmlヘッダーとsitemap.xmlの作成方法を共有します。
シリーズは2つの記事で構成されており、この記事はそのシリーズの2番目の記事です。
- 第1回: [Polyglotプラグインの適用 & hreflang altタグおよびsitemap、言語選択ボタンの実装](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- 第2回: Chirpyテーマのビルド失敗と検索機能エラーのトラブルシューティング（本文）

## 要件
- [x] ビルドした結果（ウェブページ）を言語別のパス（例：`/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）で区別して提供できること。
- [x] 多言語サポートに追加的に必要な時間と労力を可能な限り最小化するために、作成した原本のマークダウンファイルのYAML front matterに'lang'および'permalink'タグを一つ一つ指定しなくても、ビルド時にそのファイルが位置するローカルパス（例：`/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）に応じて自動的に言語を認識できること。
- [x] サイト内の各ページのヘッダー部分は、適切なContent-Languageメタタグとhreflang代替タグを含み、Googleの多言語検索のためのSEOガイドラインを満たすこと。
- [x] サイト内で各言語をサポートするすべてのページリンクを漏れなく`sitemap.xml`で提供できること、また`sitemap.xml`自体は重複なくルートパスに1つだけ存在すること。
- [x] [Chirpyテーマ](https://github.com/cotes2020/jekyll-theme-chirpy)で提供されるすべての機能が各言語ページで正常に動作すること。そうでない場合は正常に動作するように修正すること。
  - [x] 'Recently Updated'、'Trending Tags'機能が正常に動作すること
  - [x] GitHub Actionsを使用したビルドプロセスでエラーが発生しないこと
  - [x] ブログ右上の投稿検索機能が正常に動作すること

## 始める前に
この記事は[第1回](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)からの続きですので、まだ読んでいない場合は、まず前の記事から読むことをお勧めします。

## トラブルシューティング（'relative_url_regex': target of repeat operator is not specified）
前のステップまで進めた後、`bundle exec jekyll serve`コマンドを実行してビルドテストを行ったところ、`'relative_url_regex': target of repeat operator is not specified`というエラーが発生し、ビルドに失敗しました。

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

同様の問題が報告されているか検索した結果、Polyglotリポジトリに[全く同じ問題](https://github.com/untra/polyglot/issues/204)が既に登録されており、解決策も存在していました。

このブログに適用中の[Chirpyテーマの`_config.yml`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml)ファイルには、次のような構文が存在します。

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

問題の原因は、[Polyglotの`site.rb`](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb)ファイルに含まれる次の2つの関数の正規表現構文が、上記の`"*.gem"`、`"*.gemspec"`、`"*.config.js"`のようなワイルドカードを含むグロビング（globbing）パターンを正常に処理できないことにあります。

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

### 1. Polyglotをフォーク（fork）した後、問題のある部分を修正して使用する
この記事を書いている時点（2024年11月）で、[Jekyll公式ドキュメント](https://jekyllrb.com/docs/configuration/options/#global-configuration)では、`exclude`設定がグロビング（globbing）パターンの使用をサポートすると明記しています。

>"This configuration option supports Ruby's File.fnmatch filename globbing patterns to match multiple entries to exclude."

つまり、問題の原因はChirpyテーマではなく、Polyglotの`relative_url_regex()`、`absolute_url_regex()`の2つの関数にあるため、これらを問題が発生しないように修正することが根本的な解決策です。

Polyglotでは該当のバグはまだ解決されていない状態なので、[このブログ投稿](https://hionpu.com/posts/github_blog_4#4-polyglot-%EC%9D%98%EC%A1%B4%EC%84%B1-%EB%AC%B8%EC%A0%9C)と[前述のGitHubイシューに付いた回答](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322)を参考に、Polyglotリポジトリをフォーク（fork）した後、問題のある部分を次のように修正して、元のPolyglotの代わりに使用すればよいです。

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
実際、正統的で理想的な方法は、上記のパッチがPolyglotのメインストリームに反映されることです。しかし、それまではフォークしたバージョンを代わりに使用しなければなりませんが、この場合、Polyglotのアップストリームがバージョンアップするたびにそのアップデートを見逃さずに反映しながらフォローするのが面倒なため、私は別の方法を使用しました。

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

## 検索機能の修正
前のステップまで進めた時点で、ほとんどすべてのサイト機能が意図したとおりに満足に動作していました。しかし、Chirpyテーマを適用したページの右上に位置する検索バーが`site.default_lang`（このブログの場合は英語）以外の言語のページをインデックスできず、英語以外の他の言語で検索した場合も検索結果として英語ページを出力するという問題があることを後で発見しました。

原因を把握するために、検索機能に関与するファイルが何で、そのうちどこで問題が発生しているのかを見てみましょう。

### '_layouts/default.html'
ブログ内のすべてのページの枠組みを構成する[`_layouts/default.html`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)ファイルを確認してみると、`<body>`要素内に`search-results.html`と`search-loader.html`の内容を読み込んでいることが確認できます。

{% raw %}
```liquid
  <body>
    {% include sidebar.html lang=lang %}

    <div id="main-wrapper" class="d-flex justify-content-center">
      <div class="container d-flex flex-column px-xxl-5">
        
        (...中略...)

        {% include_cached search-results.html lang=lang %}
      </div>

      <aside aria-label="Scroll to Top">
        <button id="back-to-top" type="button" class="btn btn-lg btn-box-shadow">
          <i class="fas fa-angle-up"></i>
        </button>
      </aside>
    </div>

    (...中略...)

    {% include_cached search-loader.html lang=lang %}
  </body>
```
{: file='_layouts/default.html'}
{% endraw %}

### '_includes/search-result.html'
[`_includes/search-result.html`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/search-results.html)は、検索ボックスにキーワードを入力した際にそのキーワードに対する検索結果を格納するための`search-results`コンテナを構成します。

{% raw %}
```html
<!-- The Search results -->

<div id="search-result-wrapper" class="d-flex justify-content-center d-none">
  <div class="col-11 content">
    <div id="search-hints">
      {% include_cached trending-tags.html %}
    </div>
    <div id="search-results" class="d-flex flex-wrap justify-content-center text-muted mt-3"></div>
  </div>
</div>
```
{: file='_includes/search-result.html'}
{% endraw %}

### '_includes/search-loader.html'
[`_includes/search-loader.html`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/search-loader.html)がまさに[Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search)ライブラリベースの検索を実装した核心的な部分で、これは[`search.json`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/assets/js/data/search.json)インデックスファイルの内容のうち入力キーワードと一致する部分を見つけて該当の投稿リンクを`<article>`要素として返すJavaScriptを訪問者のブラウザ上で実行することで、クライアントサイドで動作することがわかります。

{% raw %}
```js
{% capture result_elem %}
  <article class="px-1 px-sm-2 px-lg-4 px-xl-0">
    <header>
      <h2><a href="{url}">{title}</a></h2>
      <div class="post-meta d-flex flex-column flex-sm-row text-muted mt-1 mb-1">
        {categories}
        {tags}
      </div>
    </header>
    <p>{snippet}</p>
  </article>
{% endcapture %}

{% capture not_found %}<p class="mt-5">{{ site.data.locales[include.lang].search.no_results }}</p>{% endcapture %}

<script>
  {% comment %} Note: dependent library will be loaded in `js-selector.html` {% endcomment %}
  document.addEventListener('DOMContentLoaded', () => {
    SimpleJekyllSearch({
      searchInput: document.getElementById('search-input'),
      resultsContainer: document.getElementById('search-results'),
      json: '{{ '/assets/js/data/search.json' | relative_url }}',
      searchResultTemplate: '{{ result_elem | strip_newlines }}',
      noResultsText: '{{ not_found }}',
      templateMiddleware: function(prop, value, template) {
        if (prop === 'categories') {
          if (value === '') {
            return `${value}`;
          } else {
            return `<div class="me-sm-4"><i class="far fa-folder fa-fw"></i>${value}</div>`;
          }
        }

        if (prop === 'tags') {
          if (value === '') {
            return `${value}`;
          } else {
            return `<div><i class="fa fa-tag fa-fw"></i>${value}</div>`;
          }
        }
      }
    });
  });
</script>
```
{: file='_includes/search-loader.html'}
{% endraw %}

### 検索機能の動作構造および問題発生部分の把握
つまりまとめると、GitHub Pages上でChirpyテーマをホスティングする場合、検索機能は次のようなプロセスで動作します。

```mermaid
stateDiagram
  state "Changes" as CH
  state "Build start" as BLD
  state "Create search.json" as IDX
  state "Static Website" as DEP
  state "In Test" as TST
  state "Search Loader" as SCH
  state "Results" as R
    
  [*] --> CH: Make Changes
  CH --> BLD: Commit & Push origin
  BLD --> IDX: jekyll build
  IDX --> TST: Build Complete
  TST --> CH: Error Detected
  TST --> DEP: Deploy
  DEP --> SCH: Search Input
  SCH --> R: Return Results
  R --> [*]
```

ここで`search.json`はPolyglotによって次のように各言語ごとにうまく生成されていることを確認しました。
- /assets/js/data/search.json
- /ko/assets/js/data/search.json
- /es/assets/js/data/search.json
- /pt-BR/assets/js/data/search.json
- /ja/assets/js/data/search.json
- /fr/assets/js/data/search.json
- /de/assets/js/data/search.json

したがって、問題の原因となる部分は「Search Loader」です。英語以外の他の言語バージョンのページが検索されない問題は、`_includes/search-loader.html`で現在訪問中のページの言語に関係なく英語のインデックスファイル（`/assets/js/data/search.json`）のみを静的に読み込むために発生します。

### 問題解決
これを解決するには、`_includes/search-loader.html`の内容を次のように修正すればよいです。

{% raw %}
```js
(前略...)

<script>
  {% comment %} Note: dependent library will be loaded in `js-selector.html` {% endcomment %}
  document.addEventListener('DOMContentLoaded', () => {
    // 現在の言語を取得
    const lang = "{{site.active_lang}}";

    // 適切な検索JSONパスを構築
    const searchJsonPath = lang === "{{site.default_lang}}"
      ? '{{ "/assets/js/data/search.json" | relative_url }}'
      : `{{ "/" | relative_url }}${lang}/assets/js/data/search.json`;

    // Simple Jekyll Searchを初期化
    SimpleJekyllSearch({
      searchInput: document.getElementById('search-input'),
      resultsContainer: document.getElementById('search-results'),
      json: searchJsonPath, // 言語に基づく動的パスを使用
      searchResultTemplate: '{{ result_elem | strip_newlines }}',
      noResultsText: '{{ not_found }}',

(...後略)
```
{: file='_includes/search-loader.html'}
{% endraw %}

現在の言語（{% raw %}`{{site.active_lang}}`{% endraw %}）とサイトのデフォルト言語（{% raw %}`{{site.default_lang}}`{% endraw %}）を比較し、同じであればデフォルトパス（"/assets/js/data/search.json"）を、異なれば`${lang}/assets/js/data/search.json`を`searchJsonPath`として動的に読み込むようにJavaScriptコードを修正しました。上記のように修正した後、ウェブサイトを再ビルドすると、各言語に合わせて検索結果が正常に表示されることを確認しました。
