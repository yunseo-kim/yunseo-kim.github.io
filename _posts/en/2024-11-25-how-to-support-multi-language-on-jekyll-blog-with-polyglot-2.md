---
title: "How to Support Multiple Languages on a Jekyll Blog with Polyglot (2) - Implementing a Language Selector Button & Localizing the Layout Language"
description: "Part two of our series on implementing multi-language support for a Jekyll blog with the Polyglot plugin. Learn how to add a language selector button and localize the Chirpy theme's layout for a seamless user experience."
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Overview
In early July 12024, I added multi-language support to this blog, which is hosted on GitHub Pages with Jekyll, by applying the [Polyglot](https://github.com/untra/polyglot) plugin.
This series shares the bugs encountered while applying the Polyglot plugin to the Chirpy theme, their solutions, and how to write the HTML header and sitemap.xml with SEO in mind.
The series consists of three posts, and the one you are reading is the second.
- Part 1: [Applying the Polyglot Plugin & Modifying the HTML Header and Sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Part 2: Implementing the Language Selector Button & Localizing the Layout Language (This Post)
- Part 3: [Troubleshooting Chirpy Theme Build Failures and Search Function Errors](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> This series was originally planned as two parts. However, it has been expanded to three parts after significant content additions and revisions.
{: .prompt-info }

## Requirements
- [x] The built result (web pages) must be served under language-specific paths (e.g., `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] To minimize the additional time and effort for multi-language support, the build process should automatically recognize the language based on the local file path (e.g., `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) without needing to manually specify 'lang' and 'permalink' tags in the YAML front matter of each Markdown file.
- [x] The header of each page on the site must meet Google's SEO guidelines for multilingual search by including appropriate Content-Language meta tags, hreflang alternate tags, and canonical links.
- [x] The site must provide all language-specific page links in a single `sitemap.xml`{: .filepath} file without omissions, and this `sitemap.xml`{: .filepath} file must exist only at the root path without duplication.
- [x] All features provided by the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy) must function correctly on each language page. If not, they must be modified to work properly.
  - [x] 'Recently Updated' and 'Trending Tags' features work correctly.
  - [x] No errors during the build process using GitHub Actions.
  - [x] The post search function in the top-right corner of the blog works correctly.

## Before We Start
This post is a continuation of [Part 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1). If you haven't read it yet, I recommend reading the previous post first.

## Adding a Language Selector Button to the Sidebar
> (Updated 12025.02.05.) The language selector button has been improved to a dropdown list format.
{: .prompt-info }

I created the file `_includes/lang-selector.html`{: .filepath} and added the following content.

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Select Language">
    {%- for lang in site.languages -%}
        <option value="{% if lang == site.default_lang %}{{ page.url }}{% else %}/{{ lang }}{{ page.url }}{% endif %}"
                {% if lang == site.active_lang %}selected{% endif %}>
            {% case lang %}
            {% when 'ko' %}🇰🇷 Korean
            {% when 'en' %}🇺🇸 English
            {% when 'ja' %}🇯🇵 Japanese
            {% when 'zh-TW' %}🇹🇼 Traditional Chinese
            {% when 'es' %}🇪🇸 Spanish
            {% when 'pt-BR' %}🇧🇷 Portuguese
            {% when 'fr' %}🇫🇷 French
            {% when 'de' %}🇩🇪 German
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

I also created the file `assets/css/lang-selector.css`{: .filepath} and added the following content.

```css
/**
 * Language Selector Styles
 * 
 * Defines the styles for the language selection dropdown located in the sidebar.
 * It supports the theme's dark mode and is optimized for mobile environments.
 */

/* Language selector container */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Dropdown container */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Select input element */
.lang-select {
    /* Basic styles */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Font and color */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Appearance and interaction */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Add arrow icon */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Flag emoji style */
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

/* Hover state */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* Focus state */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Firefox browser compatibility */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE browser compatibility */
.lang-select::-ms-expand {
    display: none;
}

/* Dark mode compatibility */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Mobile optimization */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Larger touch area */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Wider selection area on mobile */
    }
}
```
{: file='assets/css/lang-selector.css'}

Next, in [Chirpy theme's `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html), I added the three lines for the `lang-selector-wrapper` class right before the `sidebar-bottom` class. This makes Jekyll load the content of the previously created `_includes/lang-selector.html`{: .filepath} during the page build.

{% raw %}
```liquid
  (omitted)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(omitted)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (Feature Added 12025.07.31.) Localizing the Layout Language
Previously, localization was only applied to the main content, such as page titles and body text, while the layout language for elements like the left sidebar tabs, site header/footer, and right panel remained fixed to the site's default (English). Personally, I felt this was sufficient and didn't see a strong need for further work. However, while working on the [recent patch for Open Graph metadata and canonical URLs](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#html-header), I discovered that localizing the layout language was surprisingly simple with just a few modifications. If it had required extensive and cumbersome code changes, I might have passed, but since it was a [simple task that took less than 10 minutes](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb), I decided to implement it as well.

### Adding Locales
Although the site doesn't provide multiple language versions of each page simultaneously for users to switch between, the [Chirpy theme itself supports a fairly wide range of languages](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales). Therefore, you can selectively download the necessary locale files provided by the Chirpy theme, add them, and, if needed, just modify the filenames appropriately. The locale filenames must match the items in the `languages` list defined in the `_config.yml`{: .filepath} file during the [Configuration](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuration) step.

> As I'll mention shortly, the files in the `_data`{: .filepath} directory are provided by default through the [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy), so you don't have to add them manually.
>
> However, in my case, I couldn't use the locales provided by the Chirpy theme as-is for the following reasons and needed to make a few modifications:
> - The filename format of the default locale files provided by the Chirpy theme includes region codes, like `ko-KR` and `ja-JP`, which doesn't match the format I use on this site (`ko`, `ja`, etc.).
> - The license notice needed to be changed from the default [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) to this blog's [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
> - As a native Korean speaker, some parts of the [Korean](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) and [Japanese](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) locales seemed awkward or unsuitable for this blog, so I personally corrected them.
> - For various reasons detailed below, I'm not a fan of the Common Era, and for this blog, I've adopted the [Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar) for date notation, which required modifying the locales accordingly.
>   - It is fundamentally tied to a specific religion and is Western-centric.
>     - I don't deny that Jesus was a great saint, and I respect the views of that religion. The issue arises because it's not just used internally. If it were used only within that religion, like the Buddhist calendar, there would be no problem. But that's not the case. There were many other great figures like Confucius, Gautama Buddha, and Socrates. From the perspective of non-religious people, followers of other religions, and non-European cultures, why must the epoch of the global calendar be the year of Jesus's birth?
>     - And if you ask whether that 'year one' is actually the year of Jesus's birth, the consensus is that he was actually born a few years earlier.
>   - As a calendar system devised before the concept of '0', the year following 1 BC (-1) is immediately 1 AD (1), which makes year calculations non-intuitive.
>   - It lumps the 10,000 years of human history from the Neolithic period and the advent of agriculture until before Jesus's birth—or at least the 3,000-4,000 years since the invention of writing—into the 'Before Christ' era, which causes cognitive distortion in understanding world history, especially ancient history.
> 
> For these reasons, I manually added and modified the locale files in the `_data/locales`{: .filepath} directory.  
> Therefore, if these issues don't apply to you and you plan to use the default Chirpy theme locales without modification, you can skip this step.
{: .prompt-tip }

### Integrating with Polyglot
Now, with minor modifications to the following two files, you can seamlessly integrate with Polyglot.

> If you used the [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended) to create your repository instead of forking the theme repository directly, the relevant files might not be in your site's repository. This is because they are provided by default through the [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy). In that case, you should first download the original files from the [Chirpy theme repository](https://github.com/cotes2020/jekyll-theme-chirpy), place them in the same location within your repository, and then proceed with the modifications. When Jekyll builds the site, it prioritizes files within your repository over those provided by an external gem (like [jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy)) if they have the same name.
{: .prompt-tip }

#### '\_includes/lang.html'
As shown below, add two lines of code to the middle of the [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) file. This ensures that if the `lang` variable is not explicitly specified in a page's YAML front matter, Polyglot's `site.active_lang` variable is prioritized over the site's default language (`site.lang`) defined in `_config.yml`{: .filepath} or English (`'en'`). This file is commonly called by all pages on a Chirpy-themed site (via [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) to declare the `lang` variable, which is then used to execute layout language localization.

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

Priority for `lang` variable declaration:
- Before modification:
  1. `page.lang` (if defined in the individual page's YAML front matter)
  2. `site.lang` (if defined in `_config.yml`{: .filepath})
  3. `'en'`
- After modification:
  1. `page.lang` (if defined in the individual page's YAML front matter)
  2. **`site.active_lang`** (if using Polyglot)
  3. `site.lang` (if defined in `_config.yml`{: .filepath})
  4. `'en'`

#### '\_layouts/default.html'
Similarly, modify the content of the [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) file to correctly assign the `lang` attribute to the top-level HTML element, `<html>`.

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

Priority for assigning the `<html>` tag's `lang` attribute:
- Before modification:
  1. `page.lang` (if defined in the individual page's YAML front matter)
  2. `site.alt_lang` (if defined in `_config.yml`{: .filepath})
  3. `site.lang` (if defined in `_config.yml`{: .filepath})
  4. `unknown` (empty string, `lang=""`)
- After modification:
  1. `page.lang` (if defined in the individual page's YAML front matter)
  2. **`site.active_lang`** (if using Polyglot)
  3. `site.alt_lang` (if defined in `_config.yml`{: .filepath})
  4. `site.lang` (if defined in `_config.yml`{: .filepath})
  5. `unknown` (empty string, `lang=""`)

> It is not recommended to leave the web page language (`lang` attribute) unspecified as `unknown`; it should be set to an appropriate value whenever possible. As you can see, the `lang` attribute value in `_config.yml`{: .filepath} is used as a fallback. Therefore, whether you use Polyglot or not, it is good practice to define this value properly, and in normal cases, it should already be defined. If you are applying Polyglot or a similar i18n plugin as discussed in this post, setting it to the same value as [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuration) would be a safe choice.
{: .prompt-tip }

## Further Reading
Continued in [Part 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
