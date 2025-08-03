---
title: "使用Polyglot在Jekyll部落格實現多語言支援 (1) - Polyglot外掛程式應用 & html標頭及sitemap修改"
description: "介紹在基於'jekyll-theme-chirpy'的Jekyll部落格中應用Polyglot外掛實現多語言支援的過程。此為系列第一篇文章，主要探討 Polyglot 外掛的應用、HTML 標頭與 sitemap 的修改方法。"
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## 概要
12024 年 7 月初，我為這個透過 Github Pages 託管、基於 Jekyll 的部落格，應用了 [Polyglot](https://github.com/untra/polyglot) 外掛，新增了多語言支援功能。
本系列文章將分享在 Chirpy 主題上應用 Polyglot 外掛時遇到的錯誤及其解決過程，以及考量到 SEO 的 HTML 標頭和 sitemap.xml 的撰寫方法。
此系列共有三篇文章，您正在閱讀的是第一篇。
- 第1篇：Polyglot外掛程式應用 & html標頭及sitemap修改 (本文)
- 第2篇：[實現語言選擇按鈕 & 版面配置語言本地化](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- 第3篇：[Chirpy主題構建失敗及搜尋功能錯誤故障排除](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> 原本此系列為兩篇文章，但經過數次內容補充後，篇幅大幅增加，因此改為三篇文章。
{: .prompt-info }

## 需求條件
- [x] 構建的結果（網頁）應按語言路徑（例如 `/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）分類提供。
- [x] 為了盡量減少多語言支援所需的額外時間和精力，不必在原始markdown文件的YAML front matter中逐一指定'lang'和'permalink'標籤，而是在構建時根據文件所在的本地路徑（例如 `/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）自動識別語言。
- [x] 網站中每個頁面的標頭部分應包含適當的Content-Language元標籤、hreflang替代標籤和canonical連結，以滿足Google多語言搜尋的SEO指南。
- [x] 網站中每個語言版本的頁面連結應完整地在`sitemap.xml`{: .filepath}中提供，而`sitemap.xml`{: .filepath}本身應只存在於根路徑中，不得重複。
- [x] [Chirpy主題](https://github.com/cotes2020/jekyll-theme-chirpy)提供的所有功能應在各語言頁面中正常運作，如果不正常，則需進行修改使其正常運作。
  - [x] 'Recently Updated'、'Trending Tags'功能正常運作
  - [x] 使用GitHub Actions構建過程中不出現錯誤
  - [x] 部落格右上角的文章搜尋功能正常運作

## 應用 Polyglot 外掛
Jekyll 預設不支援多語言部落格，因此要實現滿足上述需求的多語言部落格，必須使用外部外掛。經過搜尋，我發現 [Polyglot](https://github.com/untra/polyglot) 在實現多語言網站方面被廣泛使用，且能滿足大部分需求，因此我選擇了這個外掛。

### 安裝外掛
我正在使用 Bundler，所以在 `Gemfile` 中加入了以下內容。

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

之後在終端機中執行 `bundle update`，就會自動完成安裝。

如果不使用 Bundler，也可以在終端機中透過 `gem install jekyll-polyglot` 指令直接安裝 gem，然後在 `_config.yml`{: .filepath} 中加入此外掛，如下所示。

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 設定組態
接下來，打開 `_config.yml`{: .filepath} 檔案並加入以下內容。

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: 想要支援的語言列表
- `default_lang`: 預設的備用語言
- `exclude_from_localization`: 指定要從本地化對象中排除的根目錄檔案/資料夾路徑字串正規表示式
- `parallel_localization`: 一個布林值，指定在建置過程中是否要並行處理多語言
- `lang_from_path`: 一個布林值，設為 'true' 時，即使文章的 Markdown 檔案內未透過 YAML front matter 明確指定 'lang' 屬性，只要該 Markdown 檔案的路徑字串包含語言代碼，就會自動識別並使用

> [Sitemap 協定官方文件](https://www.sitemaps.org/protocol.html#location)中明確指出：
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> 為了遵守此規定，應將 `sitemap.xml`{: .filepath} 加入 'exclude_from_localization' 列表中，以確保不會為每種語言生成內容相同的 `sitemap.xml`{: .filepath} 檔案，而是只有一個位於根目錄下的檔案。這樣可以避免出現以下錯誤範例的情況。
>
> 錯誤範例（每個檔案的內容並非因語言而異，而是完全相同）：
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (12025.01.14. 更新) [我將上述內容補充至 README 並提交的 Pull Request](https://github.com/untra/polyglot/pull/230) 已被接受，現在您也可以在 [Polyglot 官方文件](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation)中找到相同的說明。
{: .prompt-tip }

> 將 'parallel_localization' 設為 'true' 的優點是能大幅縮短建置時間，但截至 12024 年 7 月，當我在本部落格啟用此功能時，頁面右側邊欄的 'Recently Updated' 和 'Trending Tags' 部分的連結標題無法正常處理，會與其他語言混雜在一起。此功能似乎尚未完全穩定，若要在網站上應用，需要事先測試是否能正常運作。此外，[Windows 使用者也應停用此功能，因為它不被支援](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

此外，[在 Jekyll 4.0 中，需要停用 CSS sourcemaps 的生成](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 撰寫文章時的注意事項
撰寫多語言文章時，應注意以下幾點：
- 指定適當的語言代碼：需透過檔案路徑（例如 `/_posts/ko/example-post.md`{: .filepath}）或 YAML front matter 的 'lang' 屬性（例如 `lang: ko`）來指定適當的 ISO 語言代碼。可參考 [Chrome 開發者文件](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)中的範例。

> 不過，[Chrome 開發者文件](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)中將地區代碼標示為 'pt_BR' 這樣的格式，但實際上應使用 '-' 而非 '_'，如 'pt-BR'，這樣在之後於 HTML 標頭中加入 hreflang 替代標籤時才能正常運作。
{: .prompt-tip }

- 檔案路徑和名稱應保持一致。

詳細資訊請參考 GitHub [untra/polyglot 儲存庫的 README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)。

## 修改 HTML 標頭與 sitemap
現在，為了 SEO，我們需要在部落格內各頁面的 HTML 標頭中插入 Content-Language 元標籤和 hreflang 替代標籤，並適當指定標準網址 (canonical URL)。

### HTML 標頭
截至 12024 年 11 月的最新版本 1.8.1，Polyglot 提供了在頁面標頭部分呼叫 {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid 標籤時自動執行上述操作的功能。
然而，此功能的前提是該頁面已透過 'permalink' 屬性標籤明確指定了永久連結，否則將無法正常運作。

因此，我取用了 [Chirpy 主題的 head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) 並直接加入了以下內容。
我參考了 [Polyglot 官方部落格的 SEO Recipes 頁面](https://polyglot.untra.io/seo/)進行操作，但為了符合我的使用環境和需求，我修改為使用 `page.url` 屬性而非 `page.permalink`。

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

(12025.07.29. 新增) 此外，我發現 Chirpy 主題預設內建了 [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag) 外掛，而 Jekyll SEO Tag 自動生成的 `og:locale`、`og:url` [Open Graph](https://ogp.me/) 元資料屬性以及[標準網址 (canonical URL)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)（`rel="canonical"` `link` 元素）是基於網站的預設語言（`site.lang`, `site.default_lang`），因此需要額外處理。
於是我在 {% raw %}`{{ seo_tags }}`{% endraw %} 前面加入了以下語法。

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

> 根據 [Google 開發者文件](https://developers.google.com/search/docs/crawling-indexing/canonicalization)，當一個頁面有多個語言版本時，只有在主要內容的語言相同，也就是只有頁首、頁尾或其他非重要文字被翻譯，而主體內容相同的情況下，才會被視為重複。因此，像本部落格這樣提供多種語言的主體文字時，每個語言版本都被視為獨立的頁面，而非重複頁面，所以應根據語言指定不同的標準網址。
> 例如，本頁面的韓文版本，其標準網址並非 "{{site.url}}{{page.url}}"，而是 "{{site.url}}/ko{{page.url}}"。
{: .prompt-tip }

### sitemap
若不另外指定範本，Jekyll 在建置時自動生成的 sitemap 不支援多語言頁面，因此需在根目錄下建立 `sitemap.xml`{: .filepath} 檔案，並輸入以下內容。

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

## 延伸閱讀
續見[第 2 部分](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
