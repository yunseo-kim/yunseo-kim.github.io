---
title: "使用Polyglot在Jekyll部落格實現多語言支援 (2) - 實現語言選擇按鈕 & 版面配置語言本地化"
description: "介紹在基於'jekyll-theme-chirpy'的Jekyll部落格中，應用Polyglot外掛實現多語言支援的過程。此為系列第二篇文章，主要探討如何實現語言選擇按鈕及將版面配置語言本地化。"
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## 概要
12024年7月初，我為這個透過 Github Pages 託管、基於 Jekyll 的部落格，應用了 [Polyglot](https://github.com/untra/polyglot) 外掛，新增了多語言支援功能。
本系列文章將分享在 Chirpy 主題上應用 Polyglot 外掛時遇到的錯誤及其解決過程，以及考量到 SEO 的 HTML 標頭和 sitemap.xml 的撰寫方法。
此系列共有三篇文章，您正在閱讀的是第二篇。
- 第1篇：[Polyglot外掛程式應用 & html標頭及sitemap修改](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- 第2篇：實現語言選擇按鈕 & 版面配置語言本地化 (本文)
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

## 開始之前
本文接續[第1篇](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)，若您尚未閱讀，建議先從前一篇文章開始。

## 在側邊欄新增語言選擇按鈕
> (12025.02.05. 更新) 已將語言選擇按鈕改良為下拉式選單形式。
{: .prompt-info }

我建立了 `_includes/lang-selector.html`{: .filepath} 檔案，並輸入以下內容。

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="選擇語言">
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

此外，我建立了 `assets/css/lang-selector.css`{: .filepath} 檔案，並輸入以下內容。

```css
/**
 * 語言選擇器樣式
 * 
 * 定義位於側邊欄的語言選擇下拉選單的樣式。
 * 支援主題的暗黑模式，並在行動裝置環境下進行了最佳化。
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
    
    /* 字體與顏色 */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* 外觀與互動 */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* 新增箭頭圖示 */
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

/* 焦點狀態 */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Firefox 瀏覽器相容 */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE 瀏覽器相容 */
.lang-select::-ms-expand {
    display: none;
}

/* 暗黑模式相容 */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* 行動裝置環境最佳化 */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* 更大的觸控區域 */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* 在行動裝置上更寬的選擇區域 */
    }
}
```
{: file='assets/css/lang-selector.css'}

接著，我在 [Chirpy 主題的 `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) 中，於 `sidebar-bottom` class 的正前方加入了以下三行 `lang-selector-wrapper` class，讓 Jekyll 在建置頁面時能載入先前編寫的 `_includes/lang-selector.html`{: .filepath} 內容。

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

## (12025.07.31. 新增功能) 版面配置語言本地化
原本只對頁面標題和內容等正文部分進行了語言本地化，而左側邊欄的標籤名稱、網站頂部、底部及右側面板等版面配置語言則固定為網站預設的英文。個人認為這樣已經足夠，所以沒有感到進行額外工作的強烈需求。然而，最近在處理[上述 Open Graph 元資料屬性及標準網址 (canonical URL) 的修補](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#html-標頭)時，發現只需稍作修改，就能非常簡單地實現版面配置語言的本地化。如果需要大規模繁瑣的程式碼修改，那又是另一回事，但這是一個[不到10分鐘的簡單工作](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb)，所以就順便加上了。

### 新增語系檔
[Chirpy 主題本身支援的語言範圍就相當廣泛](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales)，只是沒有提供同時在網站各頁面提供多語言版本並讓使用者選擇切換的功能。因此，只需從 Chirpy 主題提供的語系檔中選擇性地下載所需檔案，並在必要時適當修改檔名即可。語系檔的檔名必須與先前在[設定組態](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#設定組態)階段於 `_config.yml`{: .filepath} 檔案中定義的 `languages` 列表中的項目一致。

> 事實上，正如稍後會提到的，`_data`{: .filepath} 目錄下的檔案即使不直接新增，也會透過 [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy) 預設提供。
>
> 不過，就我的情況而言，由於以下原因，直接使用 Chirpy 主題提供的語系檔有些不便，需要進行一些修改：
> - Chirpy 主題預設提供的語系檔名格式為 `ko-KR`、`ja-JP`，包含了地區代碼，與本站使用的格式（`ko`、`ja` 等）不符。
> - 授權聲明文字需要從預設的 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 修改為符合本部落格的 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。
> - 作為韓國人，我認為[韓語](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml)和[日語](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml)語系檔中有些部分顯得不自然，或不適合本部落格，因此我個人進行了一些修改。
> - 基於下述的種種原因，我不太喜歡西元紀年法，並且在這個部落格中採用了[人類紀元(Holocene calendar)](https://en.wikipedia.org/wiki/Holocene_calendar)作為日期表示格式，因此需要相應地修改語系檔。
>   - 它根本上帶有特定宗教的濃厚色彩，且偏向西方世界。
>     - 我不否認耶穌是偉大的聖人，也尊重該宗教的立場。如果西元紀年法像佛教的佛滅紀元一樣只在該宗教內部使用，那完全沒有問題。但事實並非如此，這才是我提出問題的原因。除了耶穌，還有孔子、釋迦牟尼、蘇格拉底等許多其他聖人。對於非宗教人士、其他宗教的信徒，以及歐洲以外的其他文化圈來說，為什麼全世界通用的紀年法元年非得是耶穌的誕生年不可？
>     - 而且，那個「元年」是否真的是耶穌的誕生年？事實上，公認的說法是耶穌在此之前幾年就已誕生。
>   - 這是在「0」的概念出現前設計的紀年法，因此西元前1年(-1)的下一年就是西元1年(1)，這使得年份計算不夠直觀。
>   - 將人類進入新石器時代和農業社會後，到耶穌誕生前的一萬年歷史，即使只考慮文字發明後的3000-4000年，都籠統地稱為「西元前」，這在世界史，特別是古代史方面，會引發認知上的扭曲。
> 
> 因此，我在這裡將語系檔直接新增到 `_data/locales`{: .filepath} 目錄下，並進行了適當的修改後才應用。
> 如果您沒有上述情況，並且打算直接使用 Chirpy 主題預設提供的語系檔，可以跳過此步驟。
{: .prompt-tip }

### 與 Polyglot 整合
現在，只需對以下兩個檔案進行少量修改，即可與 Polyglot 順利整合。

> 如果您在建立儲存庫時不是直接 fork 主題儲存庫，而是使用了 [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended)，那麼您的網站儲存庫中可能沒有對應的檔案。這是因為這些檔案即使不直接新增，也會透過 [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy) 預設提供。在這種情況下，您可以先從 [Chirpy 主題儲存庫](https://github.com/cotes2020/jekyll-theme-chirpy)下載對應的原始檔案，放置到您儲存庫中的相同位置，然後再進行修改。Jekyll 在建置網站時，如果儲存庫中已存在同名檔案，會優先使用它，而不是 [外部 gem (jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy) 提供的檔案。
{: .prompt-tip }

#### '\_includes/lang.html'
如下所示，在 [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) 檔案中間加入兩行程式碼，讓頁面在未透過 YAML front matter 明確指定 `lang` 變數的情況下，優先識別 [Polyglot 的 `site.active_lang` 變數](https://github.com/untra/polyglot?tab=readme-ov-file#features)，其次才是 `_config.yml`{: .filepath} 中定義的網站預設語言 (`site.lang`) 或英語 (`'en'`)。該檔案在建置時會被套用 Chirpy 主題的網站中所有頁面 ([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) 共同呼叫以宣告 `lang` 變數，並利用此處宣告的 `lang` 變數來執行版面配置語言的本地化。

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

`lang` 變數宣告的優先順序：
- 修改前：
  1. `page.lang` (在單一頁面的 YAML front matter 中定義時)
  2. `site.lang` (在 `_config.yml`{: .filepath} 中定義時)
  3. `'en'`
- 修改後：
  1. `page.lang` (在單一頁面的 YAML front matter 中定義時)
  2. **`site.active_lang`** (應用 Polyglot 時)
  3. `site.lang` (在 `_config.yml`{: .filepath} 中定義時)
  4. `'en'`

#### '\_layouts/default.html'
同樣地，修改 [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) 檔案的內容，以正確地為 HTML 文件的最上層元素 `<html>` 標籤指定 `lang` 屬性。

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

`<html>` 標籤 `lang` 屬性指定的優先順序：
- 修改前：
  1. `page.lang` (在單一頁面的 YAML front matter 中定義時)
  2. `site.alt_lang` (在 `_config.yml`{: .filepath} 中定義時)
  3. `site.lang` (在 `_config.yml`{: .filepath} 中定義時)
  4. `unknown` (空字串, `lang=""`)
- 修改後：
  1. `page.lang` (在單一頁面的 YAML front matter 中定義時)
  2. **`site.active_lang`** (應用 Polyglot 時)
  3. `site.alt_lang` (在 `_config.yml`{: .filepath} 中定義時)
  4. `site.lang` (在 `_config.yml`{: .filepath} 中定義時)
  5. `unknown` (空字串, `lang=""`)

> 不建議將網頁語言 (`lang` 屬性) 設為 `unknown`，應盡可能指定一個適當的值。如您所見，`_config.yml`{: .filepath} 中的 `lang` 屬性值會作為備用選項，因此無論是否使用 Polyglot，都最好將此值妥善定義，正常情況下通常也已經定義好了。若像本文一樣應用了 Polyglot 或類似的 i18n 外掛，將其設定為與 [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#設定組態) 相同的值會是個不錯的選擇。
{: .prompt-tip }

## 延伸閱讀
續見[第 3 部分](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
