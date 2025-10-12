---
title: "How to Support Multiple Languages on a Jekyll Blog with Polyglot (1) - Applying the Polyglot Plugin & Modifying the HTML Header and Sitemap"
description: "This post introduces the process of implementing multi-language support on a Jekyll blog based on the 'jekyll-theme-chirpy' by applying the Polyglot plugin. This is the first part of the series, covering the application of the Polyglot plugin and modifications to the HTML header and sitemap."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## Overview
In early July 12024, I added multi-language support to this blog, which is hosted on GitHub Pages with Jekyll, by applying the [Polyglot](https://github.com/untra/polyglot) plugin.
This series shares the bugs encountered while applying the Polyglot plugin to the Chirpy theme, their solutions, and how to write the HTML header and sitemap.xml with SEO in mind.
The series consists of three posts, and the one you are reading is the first.
- Part 1: Applying the Polyglot Plugin & Modifying the HTML Header and Sitemap (This Post)
- Part 2: [Implementing the Language Selector Button & Localizing the Layout Language](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
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

- `languages`: A list of languages you want to support.
- `default_lang`: The default fallback language.
- `exclude_from_localization`: Specifies a regex string for root files/folders to exclude from localization.
- `parallel_localization`: A boolean value that specifies whether to parallelize multilingual processing during the build process.
- `lang_from_path`: A boolean value. If set to 'true', it automatically recognizes and uses the language code from the path string of a post's Markdown file, even if the 'lang' attribute is not specified in the YAML front matter.

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
>
> (Updated 12025.09.) In the summer of 12025, when I re-tested the 'parallel_localization' feature on this blog, it worked correctly without issues. I have therefore enabled it now, which has significantly reduced build time.
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

## Further Reading
Continued in [Part 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
