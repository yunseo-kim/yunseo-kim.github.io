---
title: How to Support Multiple Languages on Jekyll Blog with Polyglot (2) - Troubleshooting Chirpy Theme Build Failure and Search Function Errors
description: >-
  This post introduces the process of implementing multilingual support by applying the Polyglot plugin to a Jekyll blog based on 'jekyll-theme-chirpy'.
  This is the second post in the series, covering the identification and resolution of errors that occurred when applying Polyglot to the Chirpy theme.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
mermaid: true
---
## Overview
About 4 months ago, in early July 2024, I added multilingual support to this blog, which is hosted via GitHub Pages based on Jekyll, by applying the [Polyglot](https://github.com/untra/polyglot) plugin.
This series shares the bugs encountered during the process of applying the Polyglot plugin to the Chirpy theme, their resolution process, and how to write HTML headers and sitemap.xml considering SEO.
The series consists of 2 posts, and this post you're reading is the second one in the series.
- Part 1: [Applying Polyglot Plugin & Implementing hreflang alt Tags, Sitemap, and Language Selection Button](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Part 2: Troubleshooting Chirpy Theme Build Failure and Search Function Errors (This post)

## Requirements
- [x] The built result (web pages) should be provided in language-specific paths (e.g., `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] To minimize additional time and effort required for multilingual support, the language should be automatically recognized based on the local path (e.g., `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) of the original markdown file during build, without having to specify 'lang' and 'permalink' tags in the YAML front matter of each file.
- [x] The header of each page on the site should include appropriate Content-Language meta tags and hreflang alternate tags to meet Google's multilingual search SEO guidelines.
- [x] All page links supporting each language on the site should be provided in `sitemap.xml`{: .filepath} without omission, and `sitemap.xml`{: .filepath} itself should exist only once in the root path without duplication.
- [x] All functions provided by the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy) should work normally on each language page, and if not, they should be modified to work properly.
  - [x] 'Recently Updated', 'Trending Tags' functions working normally
  - [x] No errors occurring during the build process using GitHub Actions
  - [x] Post search function in the upper right corner of the blog working normally

## Before We Start
This post is a continuation of [Part 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1), so if you haven't read it yet, it's recommended to read the previous post first.

## Troubleshooting ('relative_url_regex': target of repeat operator is not specified)
After proceeding with the previous steps, when I ran the `bundle exec jekyll serve` command to test the build, it failed with the error `'relative_url_regex': target of repeat operator is not specified`.

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

The [Chirpy theme's `_config.yml`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml) file that this blog is using contains the following statement:

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

The cause of the problem lies in the fact that the regular expression statements in the following two functions included in Polyglot's [`site.rb`{: .filepath}](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb) file cannot properly handle globbing patterns that include wildcards like `"*.gem"`, `"*.gemspec"`, `"*.config.js"` above.

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

In other words, the cause of the problem is not in the Chirpy theme but in the `relative_url_regex()` and `absolute_url_regex()` functions of Polyglot, so modifying them to prevent the problem from occurring is the fundamental solution.

Since this bug has not yet been resolved in Polyglot, you can fork the Polyglot repository and use it instead of the original Polyglot by modifying the problematic parts as follows, referring to [this blog post](https://hionpu.com/posts/github_blog_4#4-polyglot-%EC%9D%98%EC%A1%B4%EC%84%B1-%EB%AC%B8%EC%A0%9C) and [the answer to the previous GitHub issue](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322).

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

### 2. Replace globbing patterns with exact file names in the '_config.yml' configuration file of the Chirpy theme
In fact, the proper and ideal method would be for the above patch to be reflected in the Polyglot mainstream. However, until then, a forked version must be used instead, which can be cumbersome to keep up with and reflect updates every time the Polyglot upstream is versioned up. Therefore, I used a different method.

If you check the files located in the project root path in the [Chirpy theme repository](https://github.com/cotes2020/jekyll-theme-chirpy) that correspond to the `"*.gem"`, `"*.gemspec"`, `"*.config.js"` patterns, there are only 3 of them anyway:
- `jekyll-theme-chirpy.gemspec`{: .filepath}
- `purgecss.config.js`{: .filepath}
- `rollup.config.js`{: .filepath}

Therefore, if you delete the globbing patterns in the `exclude` statement of the `_config.yml`{: .filepath} file and replace them as follows, Polyglot can process them without any problems.

```yml
exclude: # Modified referring to the issue https://github.com/untra/polyglot/issues/204.
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```
{: file='_config.yml'}

## Modifying the Search Function
When I proceeded up to the previous steps, almost all site functions worked satisfactorily as intended. However, I later discovered that the search bar located in the upper right corner of the page applying the Chirpy theme could not index pages in languages other than `site.default_lang` (English in the case of this blog), and when searching in languages other than English, it output English pages as search results.

To understand the cause, let's look at what files are involved in the search function and where the problem occurs.

### '_layouts/default.html'
If you check the [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) file that forms the framework for all pages in the blog, you can see that it loads the contents of `search-results.html`{: .filepath} and `search-loader.html`{: .filepath} inside the `<body>` element.

{% raw %}
```liquid
  <body>
    {% include sidebar.html lang=lang %}

    <div id="main-wrapper" class="d-flex justify-content-center">
      <div class="container d-flex flex-column px-xxl-5">
        
        (...omitted...)

        {% include_cached search-results.html lang=lang %}
      </div>

      <aside aria-label="Scroll to Top">
        <button id="back-to-top" type="button" class="btn btn-lg btn-box-shadow">
          <i class="fas fa-angle-up"></i>
        </button>
      </aside>
    </div>

    (...omitted...)

    {% include_cached search-loader.html lang=lang %}
  </body>
```
{: file='_layouts/default.html'}
{% endraw %}

### '_includes/search-result.html'
[`_includes/search-result.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/search-results.html) constructs the `search-results` container to store search results for the keyword when a search term is entered in the search box.

{% raw %}
```html
<!-- The Search results -->

<div id="search-result-wrapper" class="d-flex justify-content-center d-none">
  <div class="col-11 content">
    <div id="search-hints">
      {% include_cached trending-tags.html %}
    </div>
    <div id="search-results" class="d-flex flex-wrap justify-content-center text-muted mt-3"></div>
  </div>
</div>
```
{: file='_includes/search-result.html'}
{% endraw %}

### '_includes/search-loader.html'
[`_includes/search-loader.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/search-loader.html) is the core part that implements the search based on the [Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search) library. It can be seen that it operates on the Client-Side by executing JavaScript in the visitor's browser to find parts that match the input keyword among the contents of the [`search.json`{: .filepath}](#assetsjsdatasearchjson) index file and return the corresponding post link as an `<article>` element.

{% raw %}
```js
{% capture result_elem %}
  <article class="px-1 px-sm-2 px-lg-4 px-xl-0">
    <header>
      <h2><a href="{url}">{title}</a></h2>
      <div class="post-meta d-flex flex-column flex-sm-row text-muted mt-1 mb-1">
        {categories}
        {tags}
      </div>
    </header>
    <p>{snippet}</p>
  </article>
{% endcapture %}

{% capture not_found %}<p class="mt-5">{{ site.data.locales[include.lang].search.no_results }}</p>{% endcapture %}

<script>
  {% comment %} Note: dependent library will be loaded in `js-selector.html` {% endcomment %}
  document.addEventListener('DOMContentLoaded', () => {
    SimpleJekyllSearch({
      searchInput: document.getElementById('search-input'),
      resultsContainer: document.getElementById('search-results'),
      json: '{{ '/assets/js/data/search.json' | relative_url }}',
      searchResultTemplate: '{{ result_elem | strip_newlines }}',
      noResultsText: '{{ not_found }}',
      templateMiddleware: function(prop, value, template) {
        if (prop === 'categories') {
          if (value === '') {
            return `${value}`;
          } else {
            return `<div class="me-sm-4"><i class="far fa-folder fa-fw"></i>${value}</div>`;
          }
        }

        if (prop === 'tags') {
          if (value === '') {
            return `${value}`;
          } else {
            return `<div><i class="fa fa-tag fa-fw"></i>${value}</div>`;
          }
        }
      }
    });
  });
</script>
```
{: file='_includes/search-loader.html'}
{% endraw %}

### '/assets/js/data/search.json'
{% raw %}
```liquid
---
layout: compress
swcache: true
---

[
  {% for post in site.posts %}
  {
    "title": {{ post.title | jsonify }},
    "url": {{ post.url | relative_url | jsonify }},
    "categories": {{ post.categories | join: ', ' | jsonify }},
    "tags": {{ post.tags | join: ', ' | jsonify }},
    "date": "{{ post.date }}",
    {% include no-linenos.html content=post.content %}
    {% assign _content = content | strip_html | strip_newlines %}
    "snippet": {{ _content | truncate: 200 | jsonify }},
    "content": {{ _content | jsonify }}
  }{% unless forloop.last %},{% endunless %}
  {% endfor %}
]
```
{: file='/assets/js/data/search.json'}
{% endraw %}

It defines a JSON file containing the title, URL, category and tag information, creation date, the first 200 characters snippet of the content, and the full content of all posts on the site using Jekyll's Liquid syntax.

### Search Function Operation Structure and Problem Identification
In summary, when hosting the Chirpy theme on GitHub Pages, the search function operates in the following process:

```mermaid
stateDiagram
  state "Changes" as CH
  state "Build start" as BLD
  state "Create search.json" as IDX
  state "Static Website" as DEP
  state "In Test" as TST
  state "Search Loader" as SCH
  state "Results" as R
    
  [*] --> CH: Make Changes
  CH --> BLD: Commit & Push origin
  BLD --> IDX: jekyll build
  IDX --> TST: Build Complete
  TST --> CH: Error Detected
  TST --> DEP: Deploy
  DEP --> SCH: Search Input
  SCH --> R: Return Results
  R --> [*]
```

Here, I confirmed that `search.json`{: .filepath} is created for each language by Polyglot as follows:
- `/assets/js/data/search.json`{: .filepath}
- `/ko/assets/js/data/search.json`{: .filepath}
- `/es/assets/js/data/search.json`{: .filepath}
- `/pt-BR/assets/js/data/search.json`{: .filepath}
- `/ja/assets/js/data/search.json`{: .filepath}
- `/fr/assets/js/data/search.json`{: .filepath}
- `/de/assets/js/data/search.json`{: .filepath}

Therefore, the problematic part is the "Search Loader". The problem of pages in languages other than English not being searched occurs because `_includes/search-loader.html`{: .filepath} statically loads only the English index file (`/assets/js/data/search.json`{: .filepath}) regardless of the language of the page currently being visited.

> - However, unlike markdown or html format files, for JSON files, the Polyglot wrapper works for Jekyll-provided variables such as `post.title`, `post.content`, etc., but it seems that the [Relativized Local Urls](https://github.com/untra/polyglot?tab=readme-ov-file#relativized-local-urls) feature does not work.
> - Similarly, I confirmed during the testing process that within the JSON file template, it's not possible to access the [{% raw %}`{{ site.default_lang }}`, `{{ site.active_lang }}`{% endraw %} liquid tags additionally provided by Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#features) other than the variables provided by Jekyll by default.
>
> Therefore, while values such as `title`, `snippet`, `content` in the index file are generated differently for each language, the `url` value returns the default path without considering the language, and appropriate handling for this needs to be added to the "Search Loader" part.
{: .prompt-warning }

### Problem Resolution
To solve this, you need to modify the contents of `_includes/search-loader.html`{: .filepath} as follows:

{% raw %}
```
{% capture result_elem %}
  <article class="px-1 px-sm-2 px-lg-4 px-xl-0">
    <header>
      {% if site.active_lang != site.default_lang %}
      <h2><a {% static_href %}href="/{{ site.active_lang }}{url}"{% endstatic_href %}>{title}</a></h2>
      {% else %}
      <h2><a href="{url}">{title}</a></h2>
      {% endif %}

(...omitted...)

<script>
  {% comment %} Note: dependent library will be loaded in `js-selector.html` {% endcomment %}
  document.addEventListener('DOMContentLoaded', () => {
    {% assign search_path = '/assets/js/data/search.json' %}
    {% if site.active_lang != site.default_lang %}
      {% assign search_path = '/' | append: site.active_lang | append: search_path %}
    {% endif %}
    
    SimpleJekyllSearch({
      searchInput: document.getElementById('search-input'),
      resultsContainer: document.getElementById('search-results'),
      json: '{{ search_path | relative_url }}',
      searchResultTemplate: '{{ result_elem | strip_newlines }}',

(...omitted)
```
{: file='_includes/search-loader.html'}
{% endraw %}

- I modified the liquid syntax in the {% raw %}`{% capture result_elem %}`{% endraw %} part to add the {% raw %}`"/{{ site.active_lang }}"`{% endraw %} prefix in front of the post URL loaded from the JSON file when `site.active_lang` (current page language) and `site.default_lang` (site default language) are not the same.
- In the same way, I modified the `<script>` part to designate the default path (`/assets/js/data/search.json`{: .filepath}) if the current page language and the site default language are the same during the build process, and the path corresponding to that language (e.g., `/ko/assets/js/data/search.json`{: .filepath}) if they are different, as `search_path`.

After modifying as above and rebuilding the website, I confirmed that the search results are displayed correctly for each language.

> Since `{url}` is where the URL value read from the JSON file will be inserted later, not a URL itself, Polyglot does not recognize it as a target for localization, so it needs to be handled directly according to the language. The problem is that {% raw %}`"/{{ site.active_lang }}{url}"`{% endraw %}, which has been processed in this way, is recognized as a URL, and although localization has already been completed, Polyglot doesn't know that and tries to perform localization redundantly (e.g., `"/ko/ko/posts/example-post"`{: .filepath}). To prevent this, I specified the [{% raw %}`{% static_href %}`{% endraw %} tag](https://github.com/untra/polyglot?tab=readme-ov-file#disabling-url-relativizing).
{: .prompt-tip }
