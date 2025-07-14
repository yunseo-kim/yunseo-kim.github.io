---
title: 使用Polyglot在Jekyll部落格實現多語言支援 (1) - 應用Polyglot外掛程式 & 實現hreflang alt標籤、sitemap及語言選擇按鈕
description: '介紹在基於''jekyll-theme-chirpy''的Jekyll部落格中應用Polyglot外掛程式實現多語言支援的過程。這篇文章是該系列的第一篇，涵蓋了應用Polyglot外掛程式並修改html標頭和sitemap的部分。'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---
## 概述
大約4個月前，也就是[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12024年7月初，我在基於Jekyll並通過Github Pages託管的本部落格中應用了[Polyglot](https://github.com/untra/polyglot)外掛程式來實現多語言支援。
這個系列將分享在Chirpy主題中應用Polyglot外掛程式的過程中遇到的錯誤及其解決方法，以及考慮SEO的html標頭和sitemap.xml的編寫方法。
本系列由兩篇文章組成，您正在閱讀的是該系列的第一篇。
- 第1篇：Polyglot外掛程式應用 & 實現hreflang alt標籤、sitemap及語言選擇按鈕（本文）
- 第2篇：[Chirpy主題構建失敗及搜尋功能錯誤故障排除](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## 需求
- [x] 構建的結果（網頁）應按語言路徑（例如 `/posts/ko/`{: .filepath}、`/posts/ja/`{: .filepath}）分類提供。
- [x] 為了盡量減少多語言支援所需的額外時間和精力，不必在原始markdown檔案的YAML front matter中逐一指定'lang'和'permalink'標籤，而是在構建時根據檔案所在的本地路徑（例如 `/_posts/ko/`{: .filepath}、`/_posts/ja/`{: .filepath}）自動識別語言。
- [x] 網站中每個頁面的標頭部分應包含適當的Content-Language元標籤和hreflang替代標籤，以滿足Google多語言搜尋的SEO指南。
- [x] 網站中支援每種語言的所有頁面連結應完整地在`sitemap.xml`{: .filepath}中提供，而`sitemap.xml`{: .filepath}本身應只存在於根路徑中，不得重複。
- [x] [Chirpy主題](https://github.com/cotes2020/jekyll-theme-chirpy)提供的所有功能應在各語言頁面中正常運作，如果不正常，則需進行修正。
  - [x] 'Recently Updated'、'Trending Tags'功能正常運作
  - [x] 使用GitHub Actions構建過程中不出現錯誤
  - [x] 部落格右上角的文章搜尋功能正常運作

## 應用Polyglot外掛程式
由於Jekyll不原生支援多語言部落格，為了滿足上述需求實現多語言部落格，需要使用外部外掛程式。經過搜尋，發現[Polyglot](https://github.com/untra/polyglot)被廣泛用於多語言網站實現，且能滿足大部分上述需求，因此採用了該外掛程式。

### 安裝外掛程式
我使用Bundler，所以在`Gemfile`中添加了以下內容：

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

然後在終端執行`bundle update`即可完成安裝。

如果不使用Bundler，也可以在終端執行`gem install jekyll-polyglot`命令直接安裝gem，然後在`_config.yml`{: .filepath}中添加以下外掛程式：

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 配置設定
接下來，打開`_config.yml`{: .filepath}檔案並添加以下內容：

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: 想要支援的語言列表
- default_lang: 預設fallback語言
- exclude_from_localization: 排除在本地化之外的根檔案/資料夾路徑字串正則表達式
- parallel_localization: 布林值，指定是否在構建過程中並行處理多語言
- lang_from_path: 布林值，設為'true'時，即使在文章markdown檔案中的YAML front matter中沒有明確指定'lang'屬性，只要該markdown檔案的路徑字串包含語言代碼，也會自動識別並使用

> [Sitemap協議官方文件](https://www.sitemaps.org/protocol.html#location)中明確指出：
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> 為了遵循這一規定，應確保相同內容的`sitemap.xml`{: .filepath}檔案不會按語言分別生成，而是只存在於根目錄中，因此需要將其添加到'exclude_from_localization'列表中，避免出現以下錯誤示例：
>
> 錯誤示例（每個檔案的內容相同，沒有語言差異）：
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> （12025.01.14. 更新）[提交的包含上述內容的Pull Request](https://github.com/untra/polyglot/pull/230)已被接受，現在在[Polyglot官方文件](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation)中也可以看到相同的指導。
{: .prompt-tip }

> 將'parallel_localization'設為'true'可以大幅縮短構建時間，但截至12024年7月，在本部落格啟用該功能時，頁面右側邊欄的'Recently Updated'和'Trending Tags'部分的連結標題無法正常處理，會與其他語言混雜。這似乎尚未完全穩定，因此在應用到網站前需要先測試其是否正常運作。此外，[Windows用戶也不支援此功能，需要將其停用](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

此外，[在Jekyll 4.0中，需要禁用CSS sourcemaps生成](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)：

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 撰寫文章時的注意事項
撰寫多語言文章時需注意以下幾點：
- 正確指定語言代碼：可以通過檔案路徑（例如 `/_posts/ko/example-post.md`{: .filepath}）或YAML front matter中的'lang'屬性（例如 `lang: ko`）來指定適當的ISO語言代碼。參考[Chrome開發者文件](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)的示例。

> 不過，[Chrome開發者文件](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)中將地區代碼表示為'pt_BR'這樣的格式，但實際上應使用'pt-BR'這樣的格式，即用-代替_，這樣在後續添加html標頭中的hreflang替代標籤時才能正常運作。

- 檔案路徑和名稱應保持一致。

詳細信息請參考GitHub [untra/polyglot儲存庫的README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)。

## 修改html標頭和sitemap
現在，為了SEO，我們需要在部落格中每個頁面的html標頭中插入Content-Language元標籤和hreflang替代標籤。

### html標頭
截至12024.11.的最新版本1.8.1，Polyglot在頁面標頭部分調用{% raw %}`{% I18n_Headers %}`{% endraw %} Liquid標籤時會自動執行上述操作。
但這假設該頁面已通過'permalink'屬性標籤明確指定，否則無法正常運作。

因此，我從[Chirpy主題的head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)中獲取代碼，然後直接添加了以下內容：
參考了[Polyglot官方部落格的SEO Recipes頁面](https://polyglot.untra.io/seo/)，但修改為在`page.permalink`不存在時使用`page.url`屬性代替。

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
Jekyll在構建時自動生成的sitemap不能正確支援多語言頁面，因此需要在根目錄創建`sitemap.xml`{: .filepath}檔案，並輸入以下內容：

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
（12025.02.05. 更新）已將語言選擇按鈕改進為下拉列表形式。  
創建`_includes/lang-selector.html`{: .filepath}檔案，並輸入以下內容：

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

同時創建`assets/css/lang-selector.css`{: .filepath}檔案，並輸入以下內容：

```css
/**
 * 語言選擇器樣式
 * 
 * 定義側邊欄中語言選擇下拉列表的樣式。
 * 支援主題的深色模式，並針對移動環境進行了優化。
 */

/* 語言選擇器容器 */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* 下拉列表容器 */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* 選擇輸入元素 */
.lang-select {
    /* 基本樣式 */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* 字體及顏色 */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* 形狀及互動 */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* 添加箭頭圖標 */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* 國旗表情符號樣式 */
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

/* 懸停狀態 */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* 聚焦狀態 */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Firefox瀏覽器適配 */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE瀏覽器適配 */
.lang-select::-ms-expand {
    display: none;
}

/* 深色模式適配 */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* 移動環境優化 */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* 更大的觸控區域 */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* 移動設備上更寬的選擇區域 */
    }
}
```
{: file='assets/css/lang-selector.css'}

接下來，在[Chirpy主題的`_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html)中"sidebar-bottom"類別前添加以下三行，使Jekyll在頁面構建時載入前面創建的`_includes/lang-selector.html`{: .filepath}內容：

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

## 延伸閱讀
繼續閱讀[第2部分](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
