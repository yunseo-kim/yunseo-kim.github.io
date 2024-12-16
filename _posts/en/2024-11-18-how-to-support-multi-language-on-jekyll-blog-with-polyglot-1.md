---
title: How to Support Multiple Languages on a Jekyll Blog with Polyglot (1) - Applying Polyglot Plugin & Implementing hreflang alt Tags, Sitemap, and Language Selection Button
description: >-
  This post introduces the process of implementing multilingual support on a Jekyll blog based on 'jekyll-theme-chirpy' using the Polyglot plugin.
  As the first in the series, this post covers applying the Polyglot plugin and modifying the HTML header and sitemap.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
---
## Overview
About 4 months ago, in early July 2024, I added multilingual support to this Jekyll-based blog hosted on Github Pages by applying the [Polyglot](https://github.com/untra/polyglot) plugin.
This series shares the bugs encountered during the process of applying the Polyglot plugin to the Chirpy theme, their solutions, and how to write HTML headers and sitemap.xml considering SEO.
The series consists of two posts, and this is the first post of the series.
- Part 1: Applying Polyglot Plugin & Implementing hreflang alt Tags, Sitemap, and Language Selection Button (This post)
- Part 2: [Troubleshooting Chirpy Theme Build Failure and Search Function Errors](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requirements
- [x] The built result (web pages) should be provided in language-specific paths (e.g., `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] To minimize additional time and effort required for multilingual support, the language should be automatically recognized based on the local path (e.g., `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) of the original markdown file during build, without having to specify 'lang' and 'permalink' tags in the YAML front matter of each file.
- [x] The header part of each page on the site should include appropriate Content-Language meta tags and hreflang alternate tags to meet Google's multilingual search SEO guidelines.
- [x] The `sitemap.xml`{: .filepath} should provide links to all pages supporting each language on the site without omission, and the `sitemap.xml`{: .filepath} itself should exist only once in the root path without duplication.
- [x] All functions provided by the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy) should work normally on each language page, and if not, they should be modified to work properly.
  - [x] 'Recently Updated', 'Trending Tags' functions working normally
  - [x] No errors occurring during the build process using GitHub Actions
  - [x] Post search function in the upper right corner of the blog working normally

## Applying the Polyglot Plugin
Since Jekyll does not natively support multilingual blogs, an external plugin must be used to implement a multilingual blog that meets the above requirements. After searching, I found that [Polyglot](https://github.com/untra/polyglot) is widely used for multilingual website implementation and can satisfy most of the above requirements, so I adopted this plugin.

### Installing the Plugin
As I use Bundler, I added the following content to the `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Then, running `bundle update` in the terminal will automatically complete the installation.

If you're not using Bundler, you can directly install the gem by running `gem install jekyll-polyglot` in the terminal, and then add the plugin to `_config.yml`{: .filepath} as follows:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration
Next, open the `_config.yml`{: .filepath} file and add the following content:

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: List of languages you want to support
- default_lang: Default fallback language
- exclude_from_localization: Specify regular expressions for root file/folder paths to exclude from localization
- parallel_localization: Boolean value specifying whether to parallelize multilingual processing during the build process
- lang_from_path: Boolean value, if set to 'true', it automatically recognizes and uses the language code if the path string of the markdown file includes it, without needing to explicitly specify the 'lang' attribute in the YAML front matter of the post markdown file

> The [official Sitemap protocol documentation](https://www.sitemaps.org/protocol.html#location) states:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> To comply with this, you should add 'sitemap.xml' to the 'exclude_from_localization' list to ensure that only one `sitemap.xml`{: .filepath} file exists in the root directory, rather than creating separate ones for each language, as shown in the incorrect example below.
>
> Incorrect example (the content of each file is identical, not different for each language):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
{: .prompt-tip }

> Setting 'parallel_localization' to 'true' can significantly reduce build time, but as of July 2024, when this feature was activated for this blog, there was a bug where the link titles in the 'Recently Updated' and 'Trending Tags' sections of the right sidebar were not processed correctly and mixed with other languages. It seems not fully stabilized yet, so it's necessary to test if it works properly before applying it to your site. Also, [this feature is not supported on Windows, so it should be deactivated](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Also, [in Jekyll 4.0, you need to disable CSS sourcemap generation as follows](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Points to Note When Writing Posts
When writing multilingual posts, keep the following in mind:
- Proper language code designation: You should specify the appropriate ISO language code using either the file path (e.g., `/_posts/ko/example-post.md`{: .filepath}) or the 'lang' attribute in the YAML front matter (e.g., `lang: ko`). Refer to the examples in the [Chrome developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> However, while the [Chrome developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) uses the format 'pt_BR' for region codes, you should actually use 'pt-BR' with a hyphen instead of an underscore for it to work properly when adding hreflang alternate tags to the HTML header later.

- File paths and names should be consistent.

For more details, please refer to the README of the GitHub [untra/polyglot repository](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modifying HTML Header and Sitemap
Now, for SEO purposes, we need to insert Content-Language meta tags and hreflang alternate tags in the HTML header of each page on the blog.

### HTML Header
As of the latest version 1.8.1 release in November 2024, Polyglot has a feature that automatically performs the above task when the {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid tag is called in the page header section.
However, this assumes that the 'permalink' attribute tag has been explicitly specified for that page, and it does not work properly otherwise.

Therefore, I imported [Chirpy theme's head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) and directly added the following content.
I referred to the [SEO Recipes page of the official Polyglot blog](https://polyglot.untra.io/seo/) but modified it to use the `page.url` attribute instead if `page.permalink` is not available.
Also, referring to the [Google Search Central official documentation](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault), I specified `x-default` instead of `site.default_lang` as the hreflang attribute value for the site's default language page, so that the link to that page is recognized as a fallback when the visitor's preferred language is not in the list of languages supported by the site or when the visitor's preferred language cannot be recognized.

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
Create a `_includes/lang-selector.html`{: .filepath} file and enter the following content:

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

Then, add the following three lines to the "sidebar-bottom" class section of [Chirpy theme's `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) to make Jekyll load the content of `_includes/lang-selector.html`{: .filepath} during page build:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Further Reading
Continued in [Part 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)