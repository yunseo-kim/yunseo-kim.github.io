---
title: How to Support Multiple Languages on Jekyll Blog with Polyglot (1) - Applying Polyglot Plugin & Implementing hreflang alt Tags, Sitemap, and Language Selection Button
description: 'This post introduces the process of implementing multilingual support by applying the Polyglot plugin to a Jekyll blog based on ''jekyll-theme-chirpy''. This is the first post in the series, covering the application of the Polyglot plugin and modifications to HTML headers and sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---
## Overview
About 4 months ago, in early July of the [Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar) 12024, I added multilingual support to this Jekyll-based blog hosted on Github Pages by applying the [Polyglot](https://github.com/untra/polyglot) plugin.
This series shares the bugs encountered during the process of applying the Polyglot plugin to the Chirpy theme, their solutions, and how to write HTML headers and sitemap.xml with SEO in mind.
The series consists of two posts, and this is the first post in the series.
- Part 1: Applying Polyglot Plugin & Implementing hreflang alt Tags, Sitemap, and Language Selection Button (this post)
- Part 2: [Troubleshooting Chirpy Theme Build Failures and Search Function Errors](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requirements
- [x] The built result (web pages) should be provided with language-specific paths (e.g., `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] To minimize the additional time and effort required for multilingual support, the system should automatically recognize the language based on the local path (e.g., `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) without having to specify 'lang' and 'permalink' tags in the YAML front matter of each original markdown file.
- [x] The header section of each page on the site should include appropriate Content-Language meta tags and hreflang alternate tags to meet Google's multilingual search SEO guidelines.
- [x] The `sitemap.xml`{: .filepath} should provide links to all pages supporting each language without omissions, and the `sitemap.xml`{: .filepath} itself should exist only once in the root path without duplication.
- [x] All features provided by the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy) should work normally on each language page, and if not, they should be modified to work properly.
  - [x] 'Recently Updated', 'Trending Tags' features working normally
  - [x] No errors during the build process using GitHub Actions
  - [x] Blog post search function in the upper right corner working normally

## Applying the Polyglot Plugin
Since Jekyll does not natively support multilingual blogs, an external plugin must be used to implement a multilingual blog that meets the above requirements. After searching, I found that [Polyglot](https://github.com/untra/polyglot) is widely used for multilingual website implementation and can satisfy most of the requirements, so I adopted this plugin.

### Plugin Installation
Since I'm using Bundler, I added the following to my `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Then running `bundle update` in the terminal will automatically complete the installation.

If you're not using Bundler, you can directly install the gem with the command `gem install jekyll-polyglot` in the terminal, and then add the plugin to `_config.yml`{: .filepath} as follows:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration
Next, open the `_config.yml`{: .filepath} file and add the following content:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: List of languages you want to support
- default_lang: Default fallback language
- exclude_from_localization: String regex specifying root files/folder paths to exclude from localization
- parallel_localization: Boolean value specifying whether to parallelize multilingual processing during build
- lang_from_path: Boolean value, when set to 'true', automatically recognizes and uses the language code if the path string of the markdown file contains it, even without explicitly specifying the 'lang' attribute in the YAML front matter

> The [official Sitemap protocol documentation](https://www.sitemaps.org/protocol.html#location) states:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> To comply with this, you should add 'sitemap' to the 'exclude_from_localization' list to ensure that only one `sitemap.xml`{: .filepath} file exists in the root directory, rather than being created for each language, as in the incorrect example below.
>
> Incorrect example (all files have identical content, not different by language):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Updated 12025.01.14.) As [the Pull Request I submitted with the above content reinforced in the README](https://github.com/untra/polyglot/pull/230) has been accepted, the same guidance can now be found in the [official Polyglot documentation](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Setting 'parallel_localization' to 'true' can significantly reduce build time, but as of July 12024, when this feature was activated for this blog, there was a bug where the link titles in the 'Recently Updated' and 'Trending Tags' sections in the right sidebar were not processed correctly and were mixed with other languages. It seems not fully stabilized yet, so it's necessary to test if it works properly before applying it to your site. Also, [this feature is not supported on Windows, so it should be disabled](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Also, [in Jekyll 4.0, you need to disable CSS sourcemaps generation as follows](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Considerations When Writing Posts
When writing multilingual posts, keep the following in mind:
- Proper language code designation: You should specify the appropriate ISO language code either through the file path (e.g., `/_posts/ko/example-post.md`{: .filepath}) or the 'lang' attribute in the YAML front matter (e.g., `lang: ko`). Refer to examples in the [Chrome developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> However, while the [Chrome developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) formats region codes as 'pt_BR', you should actually use 'pt-BR' with a hyphen instead of an underscore for proper functioning when adding hreflang alternate tags to the HTML header later.

- File paths and names should be consistent.

For more details, refer to the GitHub [untra/polyglot repository README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modifying HTML Headers and Sitemap
Now we need to insert Content-Language meta tags and hreflang alternate tags into the HTML headers of each page on the blog for SEO.

### HTML Headers
As of November 12024, in the latest version 1.8.1 release, Polyglot has a feature that automatically performs the above tasks when the {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid tag is called in the page header section.
However, this assumes that the 'permalink' attribute tag has been explicitly specified for that page, and it will not work properly otherwise.

Therefore, I took [Chirpy theme's head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) and directly added the following content, referencing [Polyglot's official blog SEO Recipes page](https://polyglot.untra.io/seo/), but modified it to use the `page.url` attribute instead when `page.permalink` is not available:

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

### Sitemap
Since the sitemap automatically generated by Jekyll during build does not properly support multilingual pages, create a `sitemap.xml`{: .filepath} file in the root directory and enter the following content:

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

## Adding Language Selection Button to Sidebar
(Updated 12025.02.05.) The language selection button has been improved to a dropdown list format.  
Create a `_includes/lang-selector.html`{: .filepath} file and enter the following content:

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

Also, create a `assets/css/lang-selector.css`{: .filepath} file and enter the following content:

```css
/**
 * Language Selector Styles
 * 
 * Defines styles for the language selection dropdown located in the sidebar.
 * Supports the theme's dark mode and is optimized for mobile environments.
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
    
    /* Font and colors */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Shape and interaction */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Add arrow icon */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Flag emoji styles */
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

/* Firefox browser support */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE browser support */
.lang-select::-ms-expand {
    display: none;
}

/* Dark mode support */
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

Next, add the following three lines just before the "sidebar-bottom" class in [Chirpy theme's `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) to load the content of `_includes/lang-selector.html`{: .filepath} when Jekyll builds the page:

{% raw %}
```liquid
  (beginning)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(end)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Further Reading
Continued in [Part 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
