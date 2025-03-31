---
title: 如何在 Jekyll 部落格中使用 Polyglot 支援多語言 (1) - 套用 Polyglot 外掛程式 & 實作 hreflang alt 標籤、sitemap 和語言選擇按鈕
description: '介紹在基於 ''jekyll-theme-chirpy'' 的 Jekyll 部落格中套用 Polyglot 外掛程式來實現多語言支援的過程。這篇文章是該系列的第一篇,涵蓋了套用 Polyglot 外掛程式並修改 html 標頭和 sitemap 的部分。'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## 概述
大約 4 個月前,也就是[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 12024 年 7 月初,我在這個基於 Jekyll 並透過 Github Pages 託管的部落格中套用了 [Polyglot](https://github.com/untra/polyglot) 外掛程式來實現多語言支援。
這個系列將分享在 Chirpy 主題中套用 Polyglot 外掛程式的過程中遇到的錯誤及其解決方法,以及考慮 SEO 的 html 標頭和 sitemap.xml 的撰寫方法。
這個系列由兩篇文章組成,您正在閱讀的是該系列的第一篇。
- 第一篇:套用 Polyglot 外掛程式 & 實作 hreflang alt 標籤、sitemap 和語言選擇按鈕 (本文)
- 第二篇:[Chirpy 主題建置失敗和搜尋功能錯誤的疑難排解](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## 需求
- [x] 必須能夠按語言路徑(例如 `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath})區分並提供建置結果(網頁)。
- [x] 為了盡可能減少多語言支援所需的額外時間和精力,即使不在原始 Markdown 檔案的 YAML front matter 中逐一指定 'lang' 和 'permalink' 標籤,也應能在建置時根據該檔案所在的本地路徑(例如 `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath})自動識別語言。
- [x] 網站內每個頁面的標頭部分應包含適當的 Content-Language 元標籤和 hreflang 替代標籤,以滿足 Google 多語言搜尋的 SEO 指南。
- [x] 必須能在 `sitemap.xml`{: .filepath} 中提供網站內支援每種語言的所有頁面連結,且不遺漏,而 `sitemap.xml`{: .filepath} 本身應只存在於根路徑中,不得重複。
- [x] [Chirpy 主題](https://github.com/cotes2020/jekyll-theme-chirpy)提供的所有功能都必須在各語言頁面中正常運作,如果不正常,則必須修正使其正常運作。
  - [x] 'Recently Updated', 'Trending Tags' 功能正常運作
  - [x] 使用 GitHub Actions 的建置過程中不會出現錯誤
  - [x] 部落格右上角的文章搜尋功能正常運作

## 套用 Polyglot 外掛程式
由於 Jekyll 不原生支援多語言部落格,為了滿足上述需求實現多語言部落格,需要使用外部外掛程式。經過搜尋,發現 [Polyglot](https://github.com/untra/polyglot) 被廣泛用於多語言網站實現,且能滿足大部分上述需求,因此採用了該外掛程式。

### 安裝外掛程式
我正在使用 Bundler,所以在 `Gemfile` 中添加了以下內容:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

之後在終端機中執行 `bundle update`,就會自動完成安裝。

如果不使用 Bundler,也可以在終端機中使用 `gem install jekyll-polyglot` 命令直接安裝 gem,然後在 `_config.yml`{: .filepath} 中添加外掛程式,如下所示:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 配置設定
接下來,打開 `_config.yml`{: .filepath} 檔案並添加以下內容:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages:想要支援的語言列表
- default_lang:預設的 fallback 語言
- exclude_from_localization:指定要從本地化中排除的根檔案/資料夾路徑字串正則表達式
- parallel_localization:布林值,指定是否在建置過程中並行處理多語言
- lang_from_path:布林值,設為 'true' 時,即使在文章 Markdown 檔案內的 YAML front matter 中沒有明確指定 'lang' 屬性,只要該 Markdown 檔案的路徑字串包含語言代碼,就會自動識別並使用

> [Sitemap 協議官方文件](https://www.sitemaps.org/protocol.html#location)中明確指出:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> 為了遵守這一規定,應該將 'sitemap' 添加到 'exclude_from_localization' 列表中,確保相同內容的 `sitemap.xml`{: .filepath} 檔案不會為每種語言生成,而只在根目錄中存在一個,避免出現以下錯誤示例:
>
> 錯誤示例(每個檔案的內容在不同語言間並無差異,都是相同的):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (12025.01.14. 更新) [提交上述內容補充到 README 的 Pull Request](https://github.com/untra/polyglot/pull/230) 已被接受,現在在 [Polyglot 官方文件](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation)中也可以看到相同的說明。
{: .prompt-tip }

> 將 'parallel_localization' 設為 'true' 可以大幅縮短建置時間,但在 12024 年 7 月時,對本部落格啟用該功能時,頁面右側側邊欄的 'Recently Updated' 和 'Trending Tags' 部分的連結標題無法正常處理,出現與其他語言混雜的錯誤。看來還不夠穩定,如果要應用到網站上,需要先進行測試確認是否正常運作。此外,[Windows 用戶也不支援該功能,因此需要停用](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility)。
{: .prompt-warning }

此外,[在 Jekyll 4.0 中,需要如下停用 CSS sourcemaps 的生成](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 撰寫文章時的注意事項
撰寫多語言文章時需要注意以下幾點:
- 指定適當的語言代碼:必須使用檔案路徑(例如 `/_posts/ko/example-post.md`{: .filepath})或 YAML front matter 中的 'lang' 屬性(例如 `lang: ko`)來指定適當的 ISO 語言代碼。參考 [Chrome 開發者文件](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)中的示例。

> 但是,請注意,[Chrome 開發者文件](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)中使用 'pt_BR' 這樣的格式來表示地區代碼,但實際上應該使用 'pt-BR' 這樣的格式,即用 - 代替 _,這樣在之後添加 html 標頭的 hreflang 替代標籤時才能正常運作。

- 檔案路徑和名稱應保持一致。

詳細資訊請參考 GitHub [untra/polyglot 儲存庫的 README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)。

## 修改 html 標頭和 sitemap
現在,為了 SEO,我們需要在部落格內每個頁面的 html 標頭中插入 Content-Language 元標籤和 hreflang 替代標籤。

### html 標頭
在 12024.11. 時的最新版本 1.8.1 發布版中,Polyglot 在頁面標頭部分呼叫 {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid 標籤時,會自動執行上述操作。
然而,這假設該頁面已明確指定了 'permalink' 屬性標籤,如果沒有指定,則無法正常運作。

因此,我從 [Chirpy 主題的 head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) 中取得內容後,直接添加了以下內容:
參考了 [Polyglot 官方部落格的 SEO Recipes 頁面](https://polyglot.untra.io/seo/),但修改為在 `page.permalink` 不存在時使用 `page.url` 屬性代替。

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
由於 Jekyll 在建置時自動生成的 sitemap 不能正確支援多語言頁面,因此在根目錄創建 `sitemap.xml`{: .filepath} 檔案,並輸入以下內容:

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
(12025.02.05. 更新) 將語言選擇按鈕改進為下拉列表形式。  
創建 `_includes/lang-selector.html`{: .filepath} 檔案,並輸入以下內容:

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

此外,創建 `assets/css/lang-selector.css`{: .filepath} 檔案,並輸入以下內容:

```css
/**
 * 語言選擇器樣式
 * 
 * 定義側邊欄中語言選擇下拉選單的樣式。
 * 支援主題的深色模式,並針對移動環境進行了優化。
 */

/* 語言選擇器容器 */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* 下拉選單容器 */
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
    
    /* 字體和顏色 */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* 形狀和互動 */
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

/* Firefox 瀏覽器適配 */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE 瀏覽器適配 */
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
        padding: 0.75rem 2rem 0.75rem 1rem;  /* 更大的觸摸區域 */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* 移動端更寬的選擇區域 */
    }
}
```
{: file='assets/css/lang-selector.css'}

接下來,在 [Chirpy 主題的 `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) 中,"sidebar-bottom" 類別正前方添加以下三行,使 Jekyll 在頁面建置時載入先前編寫的 `_includes/lang-selector.html`{: .filepath} 的內容:

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
繼續閱讀 [第二部分](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
