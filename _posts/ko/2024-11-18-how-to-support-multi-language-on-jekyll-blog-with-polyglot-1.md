---
title: Polyglot으로 Jekyll 블로그에서 다국어 지원하는 방법 (1) - Polyglot 플러그인 적용 & hreflang alt 태그
  및 sitemap, 언어 선택 버튼 구현
description: '''jekyll-theme-chirpy'' 기반의 Jekyll 블로그에 Polyglot 플러그인을 적용하여 다국어 지원을
  구현한 과정을 소개한다. 이 포스트는 해당 시리즈의 첫 번째 글로, Polyglot 플러그인을 적용하고 html 헤더와 sitemap을 수정하는
  부분을 다룬다.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## 개요
약 4달 전인 2024년 7월 초, Jekyll 기반으로 Github Pages를 통해 호스팅 중인 본 블로그에 [Polyglot](https://github.com/untra/polyglot) 플러그인을 적용하여 다국어 지원 구현을 추가하였다.
이 시리즈는 Chirpy 테마에 Polyglot 플러그인을 적용하는 과정에서 발생한 버그와 그 해결 과정, 그리고 SEO를 고려한 html 헤더와 sitemap.xml 작성법을 공유한다.
시리즈는 2개의 글로 이루어져 있으며, 읽고 있는 이 글은 해당 시리즈의 첫 번째 글이다.
- 1편: Polyglot 플러그인 적용 & hreflang alt 태그 및 sitemap, 언어 선택 버튼 구현 (본문)
- 2편: [Chirpy 테마 빌드 실패 및 검색 기능 오류 트러블슈팅](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## 요구사항
- [x] 빌드한 결과물(웹페이지)을 언어별 경로(ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath})로 구분하여 제공할 수 있어야 한다.
- [x] 다국어 지원에 추가적으로 소요되는 시간과 노력을 가능한 최소화하기 위해, 작성한 원본 마크다운 파일의 YAML front matter에 'lang' 및 'permalink' 태그를 일일이 지정해 주지 않아도 빌드 시 해당 파일이 위치한 로컬 경로(ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath})에 따라 자동으로 언어를 인식할 수 있어야 한다.
- [x] 사이트 내 각 페이지의 헤더 부분은 적절한 Content-Language 메타 태그와 hreflang 대체 태그를 포함하여 구글 다국어 검색을 위한 SEO 가이드라인을 충족해야 한다.
- [x] 사이트 내에서 각 언어를 지원하는 모든 페이지 링크를 누락 없이 `sitemap.xml`{: .filepath}에서 제공할 수 있어야 하며, `sitemap.xml`{: .filepath} 자체는 중복 없이 루트 경로에 하나만 존재하여야 한다.
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
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: 지원하고자 하는 언어 리스트
- default_lang: 기본 fallback 언어
- exclude_from_localization: 지역화 대상에서 제외할 루트 파일/폴더 경로 문자열 정규식 지정
- parallel_localization: 빌드 과정에서 다국어 처리를 병렬화할지 여부를 지정하는 boolean 값
- lang_from_path: boolean 값으로, 'true'로 설정하면 포스트 마크다운 파일 내에 YAML front matter로 'lang' 속성을 별도 명시하지 않더라도 해당 마크다운 파일의 경로 문자열이 언어 코드를 포함한다면 이를 자동으로 인식하여 사용함

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
> (2025.01.14. 업데이트) [상술한 내용을 README에 보강하여 제출한 Pull Request](https://github.com/untra/polyglot/pull/230)가 받아들여짐에 따라, 이제 [Polyglot 공식 문서](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation)에서도 동일한 안내를 확인할 수 있다.
{: .prompt-tip }

> 'parallel_localization'을 'true'로 지정하면 빌드 시간이 상당히 단축되는 장점이 있으나, 2024년 7월 시점 기준으로 본 블로그에 대해 해당 기능을 활성화했을 때 페이지 오른쪽 사이드바의 'Recently Updated'와 'Trending Tags' 부분 링크 제목이 정상적으로 처리되지 않고 다른 언어와 뒤섞이는 버그가 있었다. 아직 안정화가 덜 된 것 같으니 사이트에 적용하려면 미리 정상 작동하는지 테스트를 거칠 필요가 있다. 또한 [Windows를 사용하는 경우에도 해당 기능이 지원되지 않으므로 비활성화해야 한다](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
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

- 파일 경로와 이름은 일관적이어야 한다.

자세한 사항은 GitHub [untra/polyglot 리포지터리의 README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)를 참고하기 바란다.

## html 헤더 및 sitemap 수정
이제 SEO를 위해 블로그 내 각 페이지의 html 헤더에 Content-Language 메타 태그와 hreflang 대체 태그를 삽입해야 한다.

### html 헤더
2024.11. 기준 최신 버전인 1.8.1 릴리즈 기준, Polyglot은 페이지 헤더 부분에서 {% raw %}`{% I18n_Headers %}`{% endraw %} Liquid 태그 호출 시 위 작업을 자동으로 수행해 주는 기능이 있다.
그러나 이는 해당 페이지에 'permalink' 속성 태그를 명시하여 지정했음을 상정하고 있으며, 그렇지 않을 경우 정상 동작하지 않는다.

따라서 나는 [Chirpy 테마의 head.html](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html)을 가져온 뒤에 아래와 같이 직접 내용을 추가하였다.
[Polyglot 공식 블로그의 SEO Recipes 페이지](https://polyglot.untra.io/seo/)를 참고하여 작업하였으나, `page.permalink`가 없을 경우 `page.url` 속성을 대신 사용하도록 수정하였다.

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
Jekyll에서 빌드 시 자동 생성하는 sitemap은 다국어 페이지를 정상 지원하지 않으므로, 루트 디렉터리에 `sitemap.xml`{: .filepath} 파일을 생성하고 다음과 같이 내용을 입력한다.

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

## 사이드바에 언어 선택 버튼 추가
(2025.02.05. 업데이트) 언어 선택 버튼을 드롭다운 리스트 형식으로 개선하였다.  
`_includes/lang-selector.html`{: .filepath} 파일을 생성하고 다음과 같이 내용을 입력하였다.

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

또한 `assets/css/lang-selector.css`{: .filepath} 파일을 생성하고 다음과 같이 내용을 입력하였다.

```css
/**
 * 언어 선택기 스타일
 * 
 * 사이드바에 위치한 언어 선택 드롭다운의 스타일을 정의합니다.
 * 테마의 다크 모드를 지원하며, 모바일 환경에서도 최적화되어 있습니다.
 */

/* 언어 선택기 컨테이너 */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* 드롭다운 컨테이너 */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* 선택 입력 요소 */
.lang-select {
    /* 기본 스타일 */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* 폰트 및 색상 */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* 모양 및 상호작용 */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* 화살표 아이콘 추가 */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* 국기 이모지 스타일 */
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

/* 호버 상태 */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* 포커스 상태 */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Firefox 브라우저 대응 */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE 브라우저 대응 */
.lang-select::-ms-expand {
    display: none;
}

/* 다크 모드 대응 */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* 모바일 환경 최적화 */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* 더 큰 터치 영역 */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* 모바일에서 더 넓은 선택 영역 */
    }
}
```
{: file='assets/css/lang-selector.css'}

그 다음, [Chirpy 테마의 `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) 중 "sidebar-bottom" 클래스 바로 앞에 다음과 같이 세 줄을 추가하여 앞서 작성한 `_includes/lang-selector.html`{: .filepath}의 내용을 Jekyll이 페이지 빌드 시에 불러오도록 하였다.

{% raw %}
```liquid
  (전략)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(후략)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Further Reading
Continued in [Part 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
