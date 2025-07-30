---
title: How to Support Multiple Languages on a Jekyll Blog with Polyglot (1) - Applying the Polyglot Plugin & Implementing hreflang alt Tags, Sitemap, and a Language Selector Button
description: 'This post introduces the process of implementing multi-language support on a Jekyll blog based on the ''jekyll-theme-chirpy'' by applying the Polyglot plugin. This is the first part of the series, covering the application of the Polyglot plugin and modifications to the HTML header and sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---
## Overview
About four months ago, in early July 12024, I added multi-language support to this blog, which is hosted on GitHub Pages with Jekyll, by applying the [Polyglot](https://github.com/untra/polyglot) plugin.
This series shares the bugs encountered while applying the Polyglot plugin to the Chirpy theme, their solutions, and how to write the HTML header and sitemap.xml with SEO in mind.
The series consists of two posts, and the one you are reading is the first.
- Part 1: Applying the Polyglot Plugin & Implementing hreflang alt Tags, Sitemap, and a Language Selector Button (This Post)
- Part 2: [Troubleshooting Chirpy Theme Build Failures and Search Function Errors](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requirements
- [x] The built result (web pages) must be served under language-specific paths (e.g., `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] To minimize the additional time and effort for multi-language support, the build process should automatically recognize the language based on the local file path (e.g., `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) without needing to manually specify 'lang' and 'permalink' tags in the YAML front matter of each Markdown file.
- [x] The header of each page on the site must meet Google's SEO guidelines for multilingual search by including appropriate Content-Language meta tags, hreflang alternate tags, and canonical links.
- [x] The site must provide all language-specific page links in a single `sitemap.xml`{: .filepath} file without omissions, and this `sitemap.xml`{: .filepath} file must exist only at the root path without duplication.
- [x] All features provided by the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy) must function correctly on each language page. If not, they must be modified to work properly.
  - [x] 'Recently Updated' and 'Trending Tags' features work correctly.
  - [x] No errors during the build process using GitHub Actions.
  - [x] The post search function in the top-right corner of the blog works correctly.

## Applying the Polyglot Plugin
Jekyll does not natively support multilingual blogs, so an external plugin is needed to meet the requirements above. After some research, I found that [Polyglot](https://github.com/untra/polyglot) is widely used for creating multilingual websites and could satisfy most of my requirements, so I chose to use it.

### Plugin Installation
Since I'm using Bundler, I added the following to my `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Then, running `bundle update` in the terminal completes the installation automatically.

If you are not using Bundler, you can install the gem directly with the command `gem install jekyll-polyglot` in the terminal and then add the plugin to `_config.yml`{: .filepath} as follows:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration
Next, open the `_config.yml`{: .filepath} file and add the following content.

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: A list of languages you want to support.
- default_lang: The default fallback language.
- exclude_from_localization: Specifies a regex string for root files/folders to exclude from localization.
- parallel_localization: A boolean value that specifies whether to parallelize multilingual processing during the build process.
- lang_from_path: A boolean value. If set to 'true', it automatically recognizes and uses the language code from the path string of a post's Markdown file, even if the 'lang' attribute is not specified in the YAML front matter.

> The [official Sitemap protocol documentation](https://www.sitemaps.org/protocol.html#location) states the following:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> To comply with this, you must add `sitemap.xml`{: .filepath} to the 'exclude_from_localization' list to ensure that only one `sitemap.xml`{: .filepath} file exists in the root directory, instead of having identical files created for each language, as shown in the incorrect example below.
>
> Incorrect example (the content of each file is identical):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Updated 12025.01.14.) As my [Pull Request to add the above information to the README](https://github.com/untra/polyglot/pull/230) was merged, you can now find the same guidance in the [official Polyglot documentation](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Setting 'parallel_localization' to 'true' has the advantage of significantly reducing build time. However, as of July 12024, enabling this feature on my blog caused a bug where the link titles in the 'Recently Updated' and 'Trending Tags' sections of the right sidebar were not processed correctly and got mixed up with other languages. It seems it's not yet stable, so it's necessary to test if it works correctly before applying it to your site. Also, [this feature is not supported on Windows and must be disabled](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Also, [for Jekyll 4.0, you must disable CSS sourcemaps as follows](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Notes on Writing Posts
Here are some points to keep in mind when writing multilingual posts:
- Specify appropriate language codes: You must specify the correct ISO language code using either the file path (e.g., `/_posts/ko/example-post.md`{: .filepath}) or the 'lang' attribute in the YAML front matter (e.g., `lang: ko`). Refer to the examples in the [Chrome Developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Although the [Chrome Developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) uses formats like 'pt_BR' for locale codes, you should actually use a hyphen instead of an underscore, like 'pt-BR', for the hreflang alternate tags in the HTML header to work correctly later.
{: .prompt-tip }

- File paths and names must be consistent.

For more details, please refer to the [README of the untra/polyglot repository on GitHub](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modifying the HTML Header and Sitemap
Now, for SEO purposes, we need to insert Content-Language meta tags and hreflang alternate tags into the HTML header of each page on the blog, and properly specify the canonical URL.

### HTML Header
As of the latest version 1.8.1 release in November 12024, Polyglot has a feature that automatically performs the above tasks when the {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid tag is called in the page header.
However, this assumes that the 'permalink' attribute tag is explicitly specified for the page, and it does not work correctly otherwise.

Therefore, I took [Chirpy theme's head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) and added the content myself as shown below.
I referred to the [SEO Recipes page on the official Polyglot blog](https://polyglot.untra.io/seo/), but modified it to use the `page.url` attribute instead of `page.permalink` to fit my environment and requirements.

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

(Added 12025.07.29.) Additionally, I found that the Chirpy theme includes the [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag) plugin by default. The `og:locale`, `og:url` [Open Graph](https://ogp.me/) metadata attributes and the [canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (`rel="canonical"` `link` element) automatically generated by Jekyll SEO Tag are based on the site's default language (`site.lang`, `site.default_lang`), which required additional processing.
Therefore, I added the following code before {% raw %}`{{ seo_tags }}`{% endraw %}.

{% raw %}
```liquid
(omitted)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(omitted)...

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

  ...(omitted)
```
{: file='/_includes/head.html'}
{% endraw %}

> According to the [Google Developer documentation](https://developers.google.com/search/docs/crawling-indexing/canonicalization), when a page has multiple language versions, it is considered duplicate only if the language of the main content is the same, meaning only the header, footer, and other non-critical text are translated while the body remains identical. Therefore, in cases like this blog where the main text is provided in multiple languages, each language version is considered an independent page, not a duplicate. Thus, different canonical URLs must be specified for each language.
> For example, for the Korean version of this page, the canonical URL is "{{site.url}}/ko{{page.url}}", not "{{site.url}}{{page.url}}".
{: .prompt-tip }

### sitemap
If a template is not specified, the sitemap automatically generated by Jekyll during the build does not properly support multilingual pages. Therefore, create a `sitemap.xml`{: .filepath} file in the root directory and enter the following content.

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

## Adding a Language Selector Button to the Sidebar
(Updated 12025.02.05.) The language selector button has been improved to a dropdown list format.
Create the file `_includes/lang-selector.html`{: .filepath} and enter the following content.

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

Also, create the file `assets/css/lang-selector.css`{: .filepath} and enter the following content.

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

/* Mobile environment optimization */
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

Next, in the Chirpy theme's `_includes/sidebar.html`{: .filepath} file ([link](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html)), add the following three lines just before the "sidebar-bottom" class to have Jekyll include the content of `_includes/lang-selector.html`{: .filepath} during the page build.

{% raw %}
```liquid
  (omitted)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(omitted)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Further Reading
Continued in [Part 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
