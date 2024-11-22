---
title: How to Support Multiple Languages on a Jekyll Blog with Polyglot
description: >-
  Introducing the process of implementing multilingual support by applying the Polyglot plugin to a Jekyll blog based on 'jekyll-theme-chirpy'.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
- RegExp
---
## Introduction
About 4 months ago, in early July 2024, I added multilingual support to this Jekyll-based blog hosted on Github Pages by applying the [Polyglot](https://github.com/untra/polyglot) plugin.
In this post, I will share the bugs encountered during the process of applying the Polyglot plugin and their solutions, as well as how to write HTML headers and sitemap.xml considering SEO.

## Requirements
- [x] The build result (web pages) should be provided in language-specific paths (e.g., `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] To minimize the additional time and effort required for multilingual support, the language should be automatically recognized based on the local path (e.g., `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) where the original markdown file is located during the build process, without having to specify 'lang' and 'permalink' tags in the YAML front matter of each markdown file.
- [x] The header part of each page on the site should include appropriate Content-Language meta tags and hreflang alternate tags to meet Google's multilingual search SEO guidelines.
- [x] All page links supporting each language on the site should be provided in `sitemap.xml` without omission, and `sitemap.xml` itself should exist only once in the root path without duplication.
- [ ] All functions provided by the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy) should work normally on each language page, and if not, they should be modified to work properly.

## Applying the Polyglot Plugin
Since Jekyll does not natively support multilingual blogs, an external plugin must be used to implement a multilingual blog that meets the above requirements. After searching, I found that [Polyglot](https://github.com/untra/polyglot) is widely used for multilingual website implementation and can satisfy most of the above requirements, so I adopted this plugin.

### Installing the Plugin
Since I'm using Bundler, I added the following content to the `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Then, running `bundle update` in the terminal will automatically complete the installation.

If you're not using Bundler, you can directly install the gem with the `gem install jekyll-polyglot` command in the terminal, and then add the plugin to `_config.yml` as follows:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuration Setup
Next, open the `_config.yml` file and add the following content:

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
- exclude_from_localization: Specify string regex for root file/folder paths to exclude from localization
- parallel_localization: Boolean value specifying whether to parallelize multilingual processing during the build process
- lang_from_path: Boolean value, if set to 'true', it automatically recognizes and uses the language code if the path string of the markdown file includes it, even if the 'lang' attribute is not explicitly specified in the YAML front matter within the post markdown file

> The [official Sitemap protocol document](https://www.sitemaps.org/protocol.html#location) states the following:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> To comply with this, 'sitemap.xml' should be added to the 'exclude_from_localization' list to ensure that only one file with the same content exists in the root directory, not created for each language, to avoid incorrect examples like the following:
>
> Incorrect example (the content of each file is the same for all languages):
> - https://www.yunseo.kim/sitemap.xml
> - https://www.yunseo.kim/ko/sitemap.xml
> - https://www.yunseo.kim/es/sitemap.xml
> - https://www.yunseo.kim/pt-BR/sitemap.xml
> - https://www.yunseo.kim/ja/sitemap.xml
> - https://www.yunseo.kim/fr/sitemap.xml
> - https://www.yunseo.kim/de/sitemap.xml
{: .prompt-tip }

> Setting 'parallel_localization' to 'true' significantly reduces build time, but as of July 2024, when this feature was activated for this blog, there was a bug where the link titles in the 'Recently Updated' and 'Trending Tags' sections of the right sidebar were not processed correctly and mixed with other languages. It seems not fully stabilized yet, so it's necessary to test if it works properly before applying it to your site. Also, [this feature is not supported when using Windows, so it should be deactivated](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Also, [in Jekyll 4.0, CSS sourcemaps generation should be disabled as follows](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Points to Note When Writing Posts
When writing multilingual posts, the following points should be noted:
- Appropriate language code designation: The appropriate ISO language code should be specified using the file path (e.g., `/_posts/ko/example-post.md`{: .filepath}) or the 'lang' attribute in the YAML front matter (e.g., `lang: ko`). Refer to the examples in the [Chrome developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> However, while the [Chrome developer documentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) uses the format 'pt_BR' for region codes, in practice, you should use '-' instead of '_', like 'pt-BR', for it to work properly when adding hreflang alternate tags to the HTML header later.

- File paths and names should be consistent.

For more details, please refer to the README of the GitHub [untra/polyglot repository](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Troubleshooting ('relative_url_regex': target of repeat operator is not specified)
After completing the previous steps, when I ran the `bundle exec jekyll serve` command to test the build, it failed with the error `'relative_url_regex': target of repeat operator is not specified`.

```shell
...(omitted)
                    ------------------------------------------------
      Jekyll 4.3.4   Please append `--trace` to the `serve` command 
                     for any additional information or backtrace. 
                    ------------------------------------------------
/Users/yunseo/.gem/ruby/3.2.2/gems/jekyll-polyglot-1.8.1/lib/jekyll/polyglot/
patches/jekyll/site.rb:234:in `relative_url_regex': target of repeat operator 
is not specified: /href="?\/((?:(?!*.gem)(?!*.gemspec)(?!tools)(?!README.md)(
?!LICENSE)(?!*.config.js)(?!rollup.config.js)(?!package*.json)(?!.sass-cache)
(?!.jekyll-cache)(?!gemfiles)(?!Gemfile)(?!Gemfile.lock)(?!node_modules)(?!ve
ndor\/bundle\/)(?!vendor\/cache\/)(?!vendor\/gems\/)(?!vendor\/ruby\/)(?!en\/
)(?!ko\/)(?!es\/)(?!pt-BR\/)(?!ja\/)(?!fr\/)(?!de\/)[^,'"\s\/?.]+\.?)*(?:\/[^
\]\[)("'\s]*)?)"/ (RegexpError)

...(omitted)
```

After searching to see if a similar issue had been reported, I found that [exactly the same issue](https://github.com/untra/polyglot/issues/204) had already been registered in the Polyglot repository, and a solution existed as well.

The [`_config.yml` file of the Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml) that I'm applying to this blog contains the following clause:

```yml
exclude:
  - "*.gem"
  - "*.gemspec"
  - docs
  - tools
  - README.md
  - LICENSE
  - "*.config.js"
  - package*.json
```
{: file='_config.yml'}

The cause of the problem lies in the regex clauses of the following two functions included in [Polyglot's `site.rb`](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb) file, which cannot properly handle globbing patterns including wildcards like `"*.gem"`, `"*.gemspec"`, `"*.config.js"`.

{% raw %}
```ruby
    # a regex that matches relative urls in a html document
    # matches href="baseurl/foo/bar-baz" href="/foo/bar-baz" and others like it
    # avoids matching excluded files.  prepare makes sure
    # that all @exclude dirs have a trailing slash.
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    # a regex that matches absolute urls in a html document
    # matches href="http://baseurl/foo/bar-baz" and others like it
    # avoids matching excluded files.  prepare makes sure
    # that all @exclude dirs have a trailing slash.
    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(polyglot root path)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

There are two ways to solve this problem.

### 1. Fork Polyglot and use it after modifying the problematic parts
As of the time of writing this post (November 2024), the [Jekyll official documentation](https://jekyllrb.com/docs/configuration/options/#global-configuration) states that the `exclude` configuration supports the use of globbing patterns.

>"This configuration option supports Ruby's File.fnmatch filename globbing patterns to match multiple entries to exclude."

In other words, the root cause of the problem is not in the Chirpy theme but in the `relative_url_regex()` and `absolute_url_regex()` functions of Polyglot, so modifying them to prevent the problem is the fundamental solution.

Since this bug has not yet been resolved in Polyglot, you can fork the Polyglot repository and modify the problematic parts as follows, referring to [this blog post](https://hionpu.com/en/posts/github_blog_4#4-polyglot-dependency-issue) and [the answer to the previous GitHub issue](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322), and use it instead of the original Polyglot.

{% raw %}
```ruby
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(polyglot root path)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

### 2. Replace globbing patterns with exact filenames in the `_config.yml` configuration file of the Chirpy theme
In fact, the ideal and proper method would be for the above patch to be reflected in the Polyglot mainstream. However, until then, you would have to use the forked version instead, which can be cumbersome to keep up with and reflect updates every time the Polyglot upstream is updated. Therefore, I used a different method.

If you check the files located in the project root path in the [Chirpy theme repository](https://github.com/cotes2020/jekyll-theme-chirpy) that correspond to the `"*.gem"`, `"*.gemspec"`, `"*.config.js"` patterns, there are only 3 files anyway:
- `jekyll-theme-chirpy.gemspec`
- `purgecss.config.js`
- `rollup.config.js`

Therefore, if you delete the globbing patterns in the `exclude` clause of the `_config.yml` file and rewrite it as follows, Polyglot can process it without any problems.

```yml
exclude: # Modified referring to the https://github.com/untra/polyglot/issues/204 issue.
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```

## Modifying HTML Headers and Sitemap
Now, for SEO purposes, we need to insert Content-Language meta tags and hreflang alternate tags in the HTML headers of each page on the blog.

### HTML Headers
As of the latest version 1.8.1 release in November 2024, Polyglot has a feature that automatically performs the above task when the {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid tag is called in the page header section.
However, this assumes that the 'permalink' attribute tag has been explicitly specified for that page, and it does not work properly otherwise.

Therefore, I brought in [Chirpy theme's head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) and directly added the following content, referring to [Polyglot's official blog SEO Recipes page](https://polyglot.untra.io/seo/). However, I modified it to use the `page.url` attribute instead if `page.permalink` is not available.
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
Since the sitemap automatically generated by Jekyll during the build process does not properly support multilingual pages, create a `sitemap.xml` file in the root directory and enter the following content:

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
Create a `_includes/lang-selector.html` file and enter the following content:

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

Then, add the following three lines to the "sidebar-bottom" class part of [Chirpy theme's `_includes/sidebar.html`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) to make Jekyll load the content of `_includes/lang-selector.html` when building the page:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Issue with Search Function Not Properly Indexing Multilingual Pages
After completing the previous steps, almost all site functions worked satisfactorily as intended. However, I later discovered that the search bar located in the upper right corner of the page with the Chirpy theme applied could not index pages in languages other than `site.default_lang` (English in the case of this blog), and when searching in languages other than English, it output English pages as search results.

This problem occurs because the [Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search) JavaScript library used by the Chirpy theme relies on the `site.posts` variable provided by Jekyll to perform indexing, and thus fails to recognize multilingual pages built using Polyglot other than the default language.

The simple structure of Simple-Jekyll-Search, which performs indexing relying only on variables provided by Jekyll with a single liquid template called [`search.json`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/assets/js/data/search.json), is an advantage, but in this case, it acts as a critical disadvantage and limitation, making it unsuitable for application to this blog. Unless Jekyll natively supports multilingual pages and Polyglot provides some other variable that can replace `site.posts`, I believe Simple-Jekyll-Search cannot properly perform the multilingual page indexing required by this blog. Therefore, it is necessary to explore and apply alternatives that can replace Simple-Jekyll-Search, which I will leave as a follow-up task and topic for a future post.
