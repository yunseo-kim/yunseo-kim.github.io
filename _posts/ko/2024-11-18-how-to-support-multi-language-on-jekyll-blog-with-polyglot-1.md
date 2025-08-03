---
title: "Polyglot으로 Jekyll 블로그에서 다국어 지원하는 방법 (1) - Polyglot 플러그인 적용 & html 헤더 및 sitemap 수정"
description: "'jekyll-theme-chirpy' 기반의 Jekyll 블로그에 Polyglot 플러그인을 적용하여 다국어 지원을 구현한 과정을 소개한다. 이 포스트는 해당 시리즈의 첫 번째 글로, Polyglot 플러그인을 적용하고 html 헤더와 sitemap을 수정하는 부분을 다룬다."
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## 개요
12024년 7월 초, Jekyll 기반으로 Github Pages를 통해 호스팅 중인 본 블로그에 [Polyglot](https://github.com/untra/polyglot) 플러그인을 적용하여 다국어 지원 구현을 추가하였다.
이 시리즈는 Chirpy 테마에 Polyglot 플러그인을 적용하는 과정에서 발생한 버그와 그 해결 과정, 그리고 SEO를 고려한 html 헤더와 sitemap.xml 작성법을 공유한다.
시리즈는 3개의 글로 이루어져 있으며, 읽고 있는 이 글은 해당 시리즈의 첫 번째 글이다.
- 1편: Polyglot 플러그인 적용 & html 헤더 및 sitemap 수정 (본문)
- 2편: [언어 선택 버튼 구현 & 레이아웃 언어 현지화](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- 3편: [Chirpy 테마 빌드 실패 및 검색 기능 오류 트러블슈팅](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> 원래는 총 2편으로 구성하였으나, 이후 몇 차례에 걸쳐 내용을 보강함에 따라 분량이 크게 늘어나 3편으로 개편하였다.
{: .prompt-info }

## 요구조건
- [x] 빌드한 결과물(웹페이지)을 언어별 경로(ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath})로 구분하여 제공할 수 있어야 한다.
- [x] 다국어 지원에 추가적으로 소요되는 시간과 노력을 가능한 최소화하기 위해, 작성한 원본 마크다운 파일의 YAML front matter에 'lang' 및 'permalink' 태그를 일일이 지정해 주지 않아도 빌드 시 해당 파일이 위치한 로컬 경로(ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath})에 따라 자동으로 언어를 인식할 수 있어야 한다.
- [x] 사이트 내 각 페이지의 헤더 부분은 적절한 Content-Language 메타 태그와 hreflang 대체 태그, canonical 링크를 포함하여 다국어 검색을 위한 Google SEO 가이드라인을 충족해야 한다.
- [x] 사이트 내에서 각 언어 버전별 페이지 링크를 누락 없이 `sitemap.xml`{: .filepath}로 제공할 수 있어야 하며, `sitemap.xml`{: .filepath} 자체는 중복 없이 루트 경로에 하나만 존재하여야 한다.
- [x] [Chirpy 테마](https://github.com/cotes2020/jekyll-theme-chirpy)에서 제공하는 모든 기능은 각 언어 페이지에서 정상 작동해야 하며, 그렇지 않다면 정상 작동하게끔 수정해야 한다.
  - [x] 'Recently Updated', 'Trending Tags' 기능 정상 작동
  - [x] GitHub Actions를 이용한 빌드 과정에서 에러가 발생하지 않을 것
  - [x] 블로그 우상단 포스트 검색 기능 정상 작동

## Polyglot 플러그인 적용
Jekyll은 다국어 블로그를 기본 지원하지 않으므로, 위의 요구사항을 만족하는 다국어 블로그 구현을 위해서는 외부 플러그인을 활용해야 한다. 검색해보니 [Polyglot](https://github.com/untra/polyglot)이 다국어 웹사이트 구현 용도로 많이 쓰이며, 위 요구사항들을 대부분 만족시킬 수 있어 해당 플러그인을 채택하였다.

### 플러그인 설치
나는 Bundler를 사용 중이므로 `Gemfile`에 다음 내용을 추가하였다.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

이후 터미널에서 `bundle update`를 실행하면 자동으로 설치가 완료된다.

만약 Bundler를 사용하지 않을 경우, 터미널에서 `gem install jekyll-polyglot` 명령으로 gem을 직접 설치한 후 `_config.yml`{: .filepath}에 다음과 같이 플러그인을 추가할 수도 있다.

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 설정 구성
다음으로 `_config.yml`{: .filepath} 파일을 열고 아래 내용을 추가한다.

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: 지원하고자 하는 언어 리스트
- `default_lang`: 기본 fallback 언어
- `exclude_from_localization`: 언어 현지화 대상에서 제외할 루트 파일/폴더 경로 문자열 정규식 지정
- `parallel_localization`: 빌드 과정에서 다국어 처리를 병렬화할지 여부를 지정하는 boolean 값
- `lang_from_path`: boolean 값으로, 'true'로 설정하면 포스트 마크다운 파일 내에 YAML front matter로 'lang' 속성을 별도 명시하지 않더라도 해당 마크다운 파일의 경로 문자열이 언어 코드를 포함한다면 이를 자동으로 인식하여 사용함

> [Sitemap 프로토콜 공식 문서](https://www.sitemaps.org/protocol.html#location)에서는 다음과 같이 명시하고 있다.
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> 이를 준수하기 위해서는 동일한 내용의 `sitemap.xml`{: .filepath} 파일이 언어별로 만들어지지 않고 루트 디렉터리에 단 하나만 존재하도록 'exclude_from_localization' 리스트에 추가하여, 아래의 잘못된 예시처럼 되지 않도록 해야 한다.
>
> 잘못된 예시(각 파일의 내용은 언어별로 다르지 않고 모두 동일):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (12025.01.14. 업데이트) [상술한 내용을 README에 보강하여 제출한 Pull Request](https://github.com/untra/polyglot/pull/230)가 받아들여짐에 따라, 이제 [Polyglot 공식 문서](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation)에서도 동일한 안내를 확인할 수 있다.
{: .prompt-tip }

> 'parallel_localization'을 'true'로 지정하면 빌드 시간이 상당히 단축되는 장점이 있으나, 12024년 7월 시점 기준으로 본 블로그에 대해 해당 기능을 활성화했을 때 페이지 오른쪽 사이드바의 'Recently Updated'와 'Trending Tags' 부분 링크 제목이 정상적으로 처리되지 않고 다른 언어와 뒤섞이는 버그가 있었다. 아직 안정화가 덜 된 것 같으니 사이트에 적용하려면 미리 정상 작동하는지 테스트를 거칠 필요가 있다. 또한 [Windows를 사용하는 경우에도 해당 기능이 지원되지 않으므로 비활성화해야 한다](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

또한 [Jekyll 4.0에서는 다음과 같이 CSS sourcemaps 생성을 비활성화해야 한다](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### 포스트 작성 시 유의사항
다국어 포스트 작성 시 유의해야 할 점은 다음과 같다.
- 적절한 언어 코드 지정: 파일 경로(ex. `/_posts/ko/example-post.md`{: .filepath}) 또는 YAML front matter의 'lang' 속성(ex. `lang: ko`)을 이용하여 적절한 ISO 언어 코드를 지정해 주어야 한다. [Chrome 개발자 문서](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)의 예시를 참고한다.

> 단, [Chrome 개발자 문서](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)에서는 지역코드를 'pt_BR'과 같은 형식으로 표기하고 있으나 실제로는 'pt-BR'과 같이 _ 대신 -를 사용하여야 추후 html 헤더에 hreflang 대체 태그를 추가할 때 정상 작동한다.
{: .prompt-tip }

- 파일 경로와 이름은 일관적이어야 한다.

자세한 사항은 GitHub [untra/polyglot 리포지터리의 README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)를 참고하기 바란다.

## html 헤더 및 sitemap 수정
이제 SEO를 위해 블로그 내 각 페이지의 html 헤더에 Content-Language 메타 태그와 hreflang 대체 태그를 삽입하고, 표준 URL(canonical URL)을 적절히 지정해야 한다.

### html 헤더
12024.11. 시점에서 최신 버전인 1.8.1 릴리즈 기준으로, Polyglot은 페이지 헤더 부분에서 {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid 태그 호출 시 위 작업을 자동으로 수행해 주는 기능이 있다.
그러나 이는 해당 페이지에 'permalink' 속성 태그를 명시하여 지정했음을 상정하고 있으며, 그렇지 않을 경우 정상 동작하지 않는다.

따라서 나는 [Chirpy 테마의 head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)을 가져온 뒤에 아래와 같이 직접 내용을 추가하였다.
[Polyglot 공식 블로그의 SEO Recipes 페이지](https://polyglot.untra.io/seo/)를 참고하여 작업하였으나, 내 사용 환경 및 요구조건에 맞게 `page.permalink` 대신 `page.url` 속성을 사용하도록 수정하였다.

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

(12025.07.29. 추가) 또한 Chirpy 테마는 [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag) 플러그인을 기본 내장하고 있는데, Jekyll SEO Tag가 자동 생성하는 `og:locale`, `og:url` [Open Graph](https://ogp.me/) 메타데이터 속성 및 [표준 URL(canonical URL)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)(`rel="canonical"` `link` 요소)이 사이트 기본 언어(`site.lang`, `site.default_lang`) 기준이라 추가적인 처리가 필요함을 확인하였다.  
따라서 {% raw %}`{{ seo_tags }}`{% endraw %} 앞에 다음 구문을 추가하였다.

{% raw %}
```liquid
(전략)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(중략)...

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

  ...(후략)
```
{: file='/_includes/head.html'}
{% endraw %}

> [구글 개발자 문서](https://developers.google.com/search/docs/crawling-indexing/canonicalization)에 따르면 한 페이지에 여러 언어 버전이 있을 때는 주요 콘텐츠의 언어가 같은 경우, 즉 머리글, 바닥글, 기타 중요하지 않은 텍스트만 번역되어 있고 본문이 동일한 경우에만 중복으로 간주한다. 따라서 지금 이 블로그와 같이 본문 텍스트를 여러 언어로 제공하는 경우에는 각 언어 버전들 모두 중복이 아닌 독립적인 페이지들로 간주하므로, 언어에 따라 다른 표준 URL을 지정해야 한다.  
> 가령 지금 이 페이지의 한국어 버전의 경우, 표준 URL은 "{{site.url}}{{page.url}}"이 아니라 "{{site.url}}/ko{{page.url}}"이다.
{: .prompt-tip }

### sitemap
별도로 템플릿을 지정하지 않을 경우 Jekyll에서 빌드 시 자동 생성하는 sitemap은 다국어 페이지를 정상 지원하지 않으므로, 루트 디렉터리에 `sitemap.xml`{: .filepath} 파일을 생성하고 다음과 같이 내용을 입력한다.

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
