---
title: 如何使用Polyglot在Jekyll部落格中支援多語言 (1) - 應用Polyglot外掛程式 & 實作hreflang alt標籤、sitemap和語言選擇按鈕
description: '介紹在基於''jekyll-theme-chirpy''的Jekyll部落格中應用Polyglot外掛程式來實現多語言支援的過程。這篇文章是該系列的第一篇，涵蓋了應用Polyglot外掛程式並修改html標頭和sitemap的部分。'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## 概述
大約4個月前的2024年7月初，我在這個通過Github Pages託管的Jekyll基礎部落格上應用了[Polyglot](https://github.com/untra/polyglot)外掛程式來實現多語言支援。
這個系列分享了在Chirpy主題上應用Polyglot外掛程式的過程中遇到的錯誤及其解決方法，以及考慮SEO的html標頭和sitemap.xml的編寫方法。
該系列由兩篇文章組成，您正在閱讀的是該系列的第一篇。
- 第1部分：應用Polyglot外掛程式 & 實作hreflang alt標籤、sitemap和語言選擇按鈕（本文）
- 第2部分：[Chirpy主題構建失敗和搜索功能錯誤故障排除](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## 需求
- [x] 必須能夠按語言路徑（例如 `/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）區分並提供構建結果（網頁）。
- [x] 為了盡可能減少多語言支援所需的額外時間和精力，即使不在原始markdown文件的YAML front matter中指定'lang'和'permalink'標籤，也應能在構建時根據該文件所在的本地路徑（例如 `/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）自動識別語言。
- [x] 網站內每個頁面的標頭部分必須包含適當的Content-Language元標籤和hreflang替代標籤，以滿足Google多語言搜索的SEO指南。
- [x] 必須能夠在 `sitemap.xml`{: .filepath} 中提供網站內支援每種語言的所有頁面鏈接，且不遺漏，而 `sitemap.xml`{: .filepath} 本身必須只存在於根路徑中，且不重複。
- [x] [Chirpy主題](https://github.com/cotes2020/jekyll-theme-chirpy)提供的所有功能必須在每種語言頁面上正常運作，如果不正常，則必須進行修改使其正常運作。
  - [x] 'Recently Updated'、'Trending Tags'功能正常運作
  - [x] 使用GitHub Actions的構建過程中不會出現錯誤
  - [x] 部落格右上角的文章搜索功能正常運作

## 應用Polyglot外掛程式
由於Jekyll不原生支援多語言部落格，為了滿足上述需求實現多語言部落格，需要使用外部外掛程式。經過搜索，發現[Polyglot](https://github.com/untra/polyglot)被廣泛用於多語言網站實現，並且能滿足大部分上述需求，因此採用了該外掛程式。

### 安裝外掛程式
我正在使用Bundler，所以在 `Gemfile` 中添加了以下內容：

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

之後在終端中執行 `bundle update`，就會自動完成安裝。

如果不使用Bundler，也可以在終端中使用 `gem install jekyll-polyglot` 命令直接安裝gem，然後在 `_config.yml`{: .filepath} 中添加外掛程式，如下所示：

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 配置設置
接下來，打開 `_config.yml`{: .filepath} 文件並添加以下內容：

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages：希望支援的語言列表
- default_lang：默認fallback語言
- exclude_from_localization：指定要從本地化中排除的根文件/文件夾路徑字符串正則表達式
- parallel_localization：布爾值，指定是否在構建過程中並行處理多語言
- lang_from_path：布爾值，設置為'true'時，即使在文章markdown文件內的YAML front matter中沒有明確指定'lang'屬性，如果該markdown文件的路徑字符串包含語言代碼，也會自動識別並使用

> [Sitemap協議官方文檔](https://www.sitemaps.org/protocol.html#location)中明確指出：
>
>> "Sitemap文件的位置決定了可以包含在該Sitemap中的URL集合。位於http://example.com/catalog/sitemap.xml的Sitemap文件可以包含任何以http://example.com/catalog/開頭的URL，但不能包含以http://example.com/images/開頭的URL。"
>
>> "強烈建議您將Sitemap放在Web伺服器的根目錄中。"
>
> 為了遵守這一點，應該將'sitemap'添加到'exclude_from_localization'列表中，確保相同內容的 `sitemap.xml`{: .filepath} 文件不會按語言生成多個，而只在根目錄中存在一個，避免出現以下錯誤示例。
>
> 錯誤示例（每個文件的內容在不同語言間都是相同的）：
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
{: .prompt-tip }

> 將'parallel_localization'設置為'true'可以顯著縮短構建時間，但截至2024年7月，當對本部落格啟用此功能時，頁面右側側邊欄的'Recently Updated'和'Trending Tags'部分的鏈接標題無法正常處理，出現與其他語言混雜的錯誤。這似乎還不夠穩定，如果要應用到網站上，需要事先測試是否正常運作。此外，[如果使用Windows，該功能也不支援，因此需要停用](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

此外，[在Jekyll 4.0中，需要按以下方式停用CSS sourcemaps生成](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)：

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 撰寫文章時的注意事項
撰寫多語言文章時需要注意以下幾點：
- 指定適當的語言代碼：必須使用文件路徑（例如 `/_posts/ko/example-post.md`{: .filepath}）或YAML front matter中的'lang'屬性（例如 `lang: ko`）來指定適當的ISO語言代碼。參考[Chrome開發者文檔](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)中的示例。

> 但是，雖然[Chrome開發者文檔](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)中將地區代碼表示為'pt_BR'這樣的格式，實際上應該使用'pt-BR'這樣的格式，用 - 代替 _，這樣在後續添加html標頭的hreflang替代標籤時才能正常運作。

- 文件路徑和名稱應保持一致。

詳細信息請參考GitHub [untra/polyglot倉庫的README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)。

## 修改html標頭和sitemap
現在，為了SEO，我們需要在部落格內每個頁面的html標頭中插入Content-Language元標籤和hreflang替代標籤。

### html標頭
截至2024年11月的最新版本1.8.1發布，Polyglot在頁面標頭部分調用 {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid標籤時，有自動執行上述操作的功能。
然而，這假設該頁面已明確指定了'permalink'屬性標籤，如果沒有指定，則無法正常運作。

因此，我從[Chirpy主題的head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)中獲取內容後，直接添加了以下內容。
參考了[Polyglot官方部落格的SEO Recipes頁面](https://polyglot.untra.io/seo/)進行工作，但修改為在 `page.permalink` 不存在時使用 `page.url` 屬性代替。
此外，參考[Google Search Central官方文檔](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault)，將網站默認語言頁面的hreflang屬性值指定為 `x-default` 而不是 `site.default_lang`，以便在訪問者的偏好語言不在網站支援的語言列表中或無法識別訪問者的偏好語言時，將該頁面鏈接識別為fallback。

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
由於Jekyll在構建時自動生成的sitemap不正確支援多語言頁面，因此在根目錄中創建 `sitemap.xml`{: .filepath} 文件，並輸入以下內容：

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

## 在側邊欄添加語言選擇按鈕
創建 `_includes/lang-selector.html`{: .filepath} 文件，並輸入以下內容：

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

然後，在[Chirpy主題的 `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) 的"sidebar-bottom"類部分添加以下三行，以便Jekyll在構建頁面時加載先前創建的 `_includes/lang-selector.html`{: .filepath} 的內容：

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## 進一步閱讀
繼續閱讀[第2部分](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
