---
title: "PolyglotでJekyllブログの多言語対応を実現する方法 (2) - 言語選択ボタンの実装 & レイアウト言語の現地化"
description: "'jekyll-theme-chirpy'ベースのJekyllブログにPolyglotプラグインを適用して多言語対応を実装した過程を紹介する。この投稿は該当シリーズの2番目の記事として、言語選択ボタンの実装とレイアウト言語の現地化部分を扱う。"
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## 概要
12024年7月初旬、Jekyll基盤でGitHub Pagesを通じてホスティング中の本ブログに[Polyglot](https://github.com/untra/polyglot)プラグインを適用して多言語対応実装を追加した。
このシリーズはChirpyテーマにPolyglotプラグインを適用する過程で発生したバグとその解決過程、そしてSEOを考慮したhtmlヘッダーとsitemap.xmlの作成法を共有する。
シリーズは3つの記事で構成されており、読んでいるこの記事は該当シリーズの2番目の記事である。
- 1編：[Polyglotプラグインの適用 & htmlヘッダー及びsitemapの修正](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- 2編：言語選択ボタンの実装 & レイアウト言語の現地化（本文）
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

## 始める前に
この記事は[1編](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)から続く記事なので、まだ読んでいない場合は先に前の記事から読むことを推奨する。

## サイドバーに言語選択ボタンを追加
> （12025.02.05. アップデート）言語選択ボタンをドロップダウンリスト形式に改善した。
{: .prompt-info }

`_includes/lang-selector.html`{: .filepath}ファイルを生成し、次のように内容を入力した。

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
{: file='\_includes/lang-selector.html'}
{% endraw %}

また`assets/css/lang-selector.css`{: .filepath}ファイルを生成し、次のように内容を入力した。

```css
/**
 * 言語選択器スタイル
 * 
 * サイドバーに位置する言語選択ドロップダウンのスタイルを定義します。
 * テーマのダークモードをサポートし、モバイル環境でも最適化されています。
 */

/* 言語選択器コンテナ */
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
    
    /* フォント及び色彩 */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* 形状及び相互作用 */
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

その後、[ChirpyテーマのChirpyテーマの`_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html)中の`sidebar-bottom`クラス直前に次のように`lang-selector-wrapper`クラス3行を追加して、先ほど作成した`_includes/lang-selector.html`{: .filepath}の内容をJekyllがページビルド時に読み込むようにした。

{% raw %}
```liquid
  (前略)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(後略)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## （12025.07.31. 機能追加）レイアウト言語の現地化
既存にはページタイトルと内容など本文コンテンツにのみ言語現地化を適用し、左側サイドバーのタブ名やサイト上下端及び右側パネルなどのレイアウト言語はサイト基本値である英語に固定していた。個人的にはその程度でも十分だったため、追加で作業する必要性をあまり感じなかったが、最近[上述したOpen Graphメタデータ属性及び標準URL（canonical URL）パッチ](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#htmlヘッダー)を作業する過程で、レイアウト言語現地化が少しの修正だけで非常に簡単に可能であることを発見した。大規模で面倒なコード修正作業が必要なら分からないが、[10分もかからない簡単な作業](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb)だったので、ついでに追加適用した。

### ロケールの追加
サイト内各ページに対して複数言語バージョンを同時に提供し、ユーザー選択に応じてバージョン間で切り替える機能がないだけで、[Chirpyテーマがサポートする言語範囲自体は元々もかなり広い方である](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales)。したがってChirpyテーマが提供するロケールファイルの中から必要なものを選択的にダウンロードして追加し、必要な場合はファイル名だけ適切に修正すればよい。ロケールファイル名は先ほど[設定構成](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#設定構成)段階で`_config.yml`{: .filepath}ファイル内に定義した`languages`リスト内項目と一致しなければならない。

> 実際すぐ後でも言及するが、`_data`{: .filepath}ディレクトリのファイルは直接追加しなくても[jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy)を通じて基本提供される。
>
> ただし私の場合には次のような理由でChirpyテーマが提供するロケールをそのまま使用するのが困難で、別途いくつかの修正が必要だった。
> - Chirpyテーマが基本提供するロケールファイルの名前形式が`ko-KR`、`ja-JP`のように地域コードを含んでおり、今このサイトに使用中の形式（`ko`、`ja`など）と一致しない
> - ライセンス案内文句を基本値である[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)ではなく、このブログの[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)に合わせて修正が必要
> - [韓国語](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml)や[日本語](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml)ロケールは韓国人である私が見るに少し不自然だったり、今このブログには合わないため個人的に修正した部分が存在する
> - 下に記述したように色々理由があって西暦紀元をあまり好まず、今このブログにだけは日付表記形式として[人類紀元（Holocene calendar）](https://en.wikipedia.org/wiki/Holocene_calendar)を採択しているため、ロケールをそれに合わせて修正する必要があった
>   - 根本的に特定宗教の宗教的色彩が強く西欧圏偏向的である
>     - イエスが偉大な聖人だという点は否定しないし、該当宗教の立場も尊重するため、仏教の仏滅紀元のように西暦紀元もその宗教内部的にのみ使うというなら全く問題ないが、そうではないから問題を提起するのである。孔子、釈迦、ソクラテスなどなど、その他にも多くの聖人がいたのに、非宗教人や他の宗教を信じる人々、そしてヨーロッパ以外の他文化圏の立場で全世界が使う紀年法の元年が굳이イエスの誕生年度である理由は何か？
>     - そしてその「元年」が本当にイエス誕生年度なのかと言えば、実際はそうでもなく、それより数年前に誕生したというのが定説である
>   - 「0」の概念が登場する前に考案された紀年法なので、紀元前1年（-1）の次の年がすぐに西暦1年（1）という点で年度計算が直感的でない
>   - 人類の新石器時代及び農耕社会進入以後、イエス誕生前までの10000年、文字発明以後のみ考慮しても3000-4000年に達する歴史を「紀元前」でまとめるが、このため世界史、特に古代史において認知的な歪曲を誘発する
> 
> そのためここでは`_data/locales`{: .filepath}ディレクトリにロケールファイルを直接追加後、適当に修正して適用したのである。  
> したがって該当事項がなく、Chirpyテーマが基本提供するロケールを修正なしでそのまま適用するなら、この段階は飛ばしても良い。
{: .prompt-tip }

### Polyglotとの統合
今度は次の2つのファイルだけ少しずつ修正すれば、Polyglotと滑らかに統合できる。

> 最初にリポジトリを生成する時、テーマリポジトリを直接フォークせずに[Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended)を使用した場合なら、該当するファイルが本人のサイトのリポジトリにはない可能性もある。直接追加しなくても[jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy)を通じて基本提供されるファイルだからだが、その場合には[Chirpyテーマリポジトリ](https://github.com/cotes2020/jekyll-theme-chirpy)から該当するファイル原本を先にダウンロードして本人のリポジトリ内同一位置に置いた後作業すればよい。Jekyllがサイトをビルドする時、リポジトリ内に同一名のファイルが既にある場合、[外部gem（jekyll-theme-chirpy）](https://rubygems.org/gems/jekyll-theme-chirpy)で提供するファイルより優先的に適用する。
{: .prompt-tip }

#### '\_includes/lang.html'
下記のように[`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html)ファイル中間にコード2行を追加して、ページのYAML front matterに別途`lang`変数を明示して指定しなかった場合、`_config.yml`{: .filepath}に定義されたサイト基本言語（`site.lang`）や英語（`'en'`）より[Polyglotの`site.active_lang`変数](https://github.com/untra/polyglot?tab=readme-ov-file#features)を優先的に認識するようにする。該当ファイルはChirpyテーマを適用したサイト内のすべてのページ（[`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)）でビルド時`lang`変数宣言のため共通的に呼び出すファイルで、ここで宣言する`lang`変数を利用してレイアウト言語現地化を実行する。

{% raw %}
```diff
@@ -1,10 +1,12 @@
 {% comment %}
   Detect appearance language and return it through variable "lang"
 {% endcomment %}
 {% if site.data.locales[page.lang] %}
   {% assign lang = page.lang %}
+{% elsif site.data.locales[site.active_lang] %}
+  {% assign lang = site.active_lang %}
 {% elsif site.data.locales[site.lang] %}
   {% assign lang = site.lang %}
 {% else %}
   {% assign lang = 'en' %}
 {% endif %}
```
{: file='\_includes/lang.html'}
{% endraw %}

`lang`変数宣言時の優先順位：
- 修正前：
  1. `page.lang`（個別ページのYAML front matter内に定義された場合）
  2. `site.lang`（`_config.yml`{: .filepath}に定義された場合）
  3. `'en'`
- 修正後：
  1. `page.lang`（個別ページのYAML front matter内に定義された場合）
  2. **`site.active_lang`**（Polyglotを適用中の場合）
  3. `site.lang`（`_config.yml`{: .filepath}に定義された場合）
  4. `'en'`

#### '\_layouts/default.html'
同様に[`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)ファイルの内容を修正して、HTML文書最上位要素である`<html>`タグに`lang`属性を正しく指定するようにする。

{% raw %}
```diff
@@ -1,19 +1,19 @@
 ---
 layout: compress
 ---
 
 <!doctype html>
 
 {% include origin-type.html %}
 
 {% include lang.html %}
 
 {% if site.theme_mode %}
   {% capture prefer_mode %}data-mode="{{ site.theme_mode }}"{% endcapture %}
 {% endif %}
 
 <!-- `site.alt_lang` can specify a language different from the UI -->
-<html lang="{{ page.lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
+<html lang="{{ page.lang | default: site.active_lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
   {% include head.html %}
```
{: file='\_layouts/default.html'}
{% endraw %}

`<html>`タグ`lang`属性指定時の優先順位：
- 修正前：
  1. `page.lang`（個別ページのYAML front matter内に定義された場合）
  2. `site.alt_lang`（`_config.yml`{: .filepath}に定義された場合）
  3. `site.lang`（`_config.yml`{: .filepath}に定義された場合）
  4. `unknown`（空文字列、`lang=""`）
- 修正後：
  1. `page.lang`（個別ページのYAML front matter内に定義された場合）
  2. **`site.active_lang`**（Polyglotを適用中の場合）
  3. `site.alt_lang`（`_config.yml`{: .filepath}に定義された場合）
  4. `site.lang`（`_config.yml`{: .filepath}に定義された場合）
  5. `unknown`（空文字列、`lang=""`）

> ウェブページ言語（`lang`属性）を指定せずに`unknown`にしておくことは推奨されず、可能な限り適切な値で指定しておくべきである。見ての通り`_config.yml`{: .filepath}内の`lang`属性値をfallbackとして使用するため、Polyglotを使用するかしないかに関わらず、この値は必ず適切に定義しておくのが良く、正常な場合なら通常は既に定義されているはずである。この記事で扱うようにPolyglotまたはそれと類似したi18nプラグインを適用した場合なら、[`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#設定構成)と同じ値で指定するのが無難だろう。
{: .prompt-tip }

## Further Reading
[Part 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)に続く
