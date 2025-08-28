---
title: "Polyglot으로 Jekyll 블로그에서 다국어 지원하는 방법 (2) - 언어 선택 버튼 구현 & 레이아웃 언어 현지화"
description: "'jekyll-theme-chirpy' 기반의 Jekyll 블로그에 Polyglot 플러그인을 적용하여 다국어 지원을 구현한 과정을 소개한다. 이 포스트는 해당 시리즈의 첫 번째 글로, Polyglot 플러그인을 적용하고 html 헤더와 sitemap을 수정하는 부분을 다룬다."
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## 개요
12024년 7월 초, Jekyll 기반으로 Github Pages를 통해 호스팅 중인 본 블로그에 [Polyglot](https://github.com/untra/polyglot) 플러그인을 적용하여 다국어 지원 구현을 추가하였다.
이 시리즈는 Chirpy 테마에 Polyglot 플러그인을 적용하는 과정에서 발생한 버그와 그 해결 과정, 그리고 SEO를 고려한 html 헤더와 sitemap.xml 작성법을 공유한다.
시리즈는 3개의 글로 이루어져 있으며, 읽고 있는 이 글은 해당 시리즈의 두 번째 글이다.
- 1편: [Polyglot 플러그인 적용 & html 헤더 및 sitemap 수정](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- 2편: 언어 선택 버튼 구현 & 레이아웃 언어 현지화 (본문)
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

## 시작하기 전에
이 글은 [1편](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)에서 이어지는 글이므로, 만약 아직 읽지 않았다면 우선 이전 글부터 읽고 오는 것을 권장한다.

## 사이드바에 언어 선택 버튼 추가
> (12025.02.05. 업데이트) 언어 선택 버튼을 드롭다운 리스트 형식으로 개선하였다.
{: .prompt-info }

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
{: file='\_includes/lang-selector.html'}
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

그 다음, [Chirpy 테마의 `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) 중 `sidebar-bottom` 클래스 바로 앞에 다음과 같이 `lang-selector-wrapper` 클래스 세 줄을 추가하여 앞서 작성한 `_includes/lang-selector.html`{: .filepath}의 내용을 Jekyll이 페이지 빌드 시에 불러오도록 하였다.

{% raw %}
```liquid
  (전략)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(후략)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (12025.07.31. 기능 추가) 레이아웃 언어 현지화
기존에는 페이지 제목과 내용 등 본문 컨텐츠에만 언어 현지화를 적용하였으며, 왼쪽 사이드바의 탭 이름이나 사이트 상하단 및 우측 패널 등의 레이아웃 언어는 사이트 기본값인 영어로 고정하였다. 개인적으로는 그 정도로도 충분했기 때문에 추가로 작업할 필요성을 크게 느끼지 못해서였으나, 최근에 [상술한 Open Graph 메타데이터 속성 및 표준 URL(canonical URL) 패치](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#html-헤더)를 작업하는 과정에서 레이아웃 언어 현지화가 약간의 수정만으로도 매우 간단히 가능함을 발견하였다. 대규모의 번거로운 코드 수정 작업이 필요하다면 모르겠으나, [채 10분도 안 걸리는 간단한 작업](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb)이었으므로 겸사겸사 추가 적용하였다.

### 로케일 추가
사이트 내 각 페이지에 대해 여러 언어 버전을 동시에 제공하고, 사용자 선택에 따라 버전 간에 전환하는 기능이 없을 뿐 [Chirpy 테마가 지원하는 언어 범위 자체는 원래도 꽤나 넓은 편이다](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales). 따라서 Chirpy 테마가 제공하는 로케일 파일들 중 필요한 것들을 선택적으로 다운로드하여 추가하고, 필요할 경우 파일 이름만 적절히 수정해 주면 된다. 로케일 파일 이름은 앞서 [설정 구성](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#설정-구성) 단계에서 `_config.yml`{: .filepath} 파일 내에 정의한 `languages` 리스트 내 항목과 일치하여야 한다.

> 사실 바로 뒤에서도 언급하겠지만, `_data`{: .filepath} 디렉터리의 파일들은 직접 추가하지 않아도 [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy)을 통해 기본 제공되기는 한다.
>
> 다만 나의 경우에는 다음과 같은 이유들로 인해 Chirpy 테마가 제공하는 로케일을 그대로 사용하기 곤란하여 따로 몇 가지 수정이 필요했다.
> - Chirpy 테마가 기본 제공하는 로케일 파일들의 이름 형식이 `ko-KR`, `ja-JP`와 같이 지역 코드를 포함하고 있어 지금 이 사이트에 사용 중인 형식(`ko`, `ja` 등)과 일치하지 않음
> - 라이선스 안내 문구를 기본값인 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)이 아니라 이 블로그의 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)에 맞게 수정 필요
> - [한국어](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml)나 [일본어](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) 로케일은 한국인인 내가 보기에 좀 어색하거나 지금 이 블로그에는 맞지 않아 개인적으로 고친 부분들이 존재함
> - 아래에 서술해 둔 바와 같이 이래저래 이유가 있어서 서력기원을 별로 좋아하지 않으며, 지금 이 블로그에만큼은 날짜 표기 형식으로 [인류력](https://en.wikipedia.org/wiki/Holocene_calendar)을 채택하고 있기에 로케일을 그에 맞게 수정해야 했음
>   - 근본적으로 특정 종교의 종교적 색채가 강하고 서구권 편향적임
>     - 예수가 위대한 성인이란 점은 부정하지 않으며, 해당 종교의 입장도 존중하기에 불교의 불멸기원처럼 서력기원도 그 종교 내부적으로만 쓰겠다고 한다면야 전혀 문제 될 것 없겠으나, 그게 아니니까 문제를 제기하는 것임. 공자, 석가모니, 소크라테스 등등 그 말고도 다른 성인들은 많았는데, 비종교인이나 다른 종교를 믿는 사람들, 그리고 유럽 이외의 타 문화권 입장에서 전 세계가 쓰는 기년법의 원년이 굳이 예수의 탄생 연도여야 하는 이유가 무엇인가?
>     - 그리고 그 '원년'이 진짜 예수 탄생 연도는 맞냐고 하면, 사실 그것도 아니고 그보다 몇 년 전에 탄생했다는 게 정설임
>   - '0'의 개념이 등장하기 전 고안된 기년법이라 기원전 1년(-1) 다음 해가 곧바로 서기 1년(1)이란 점에서 연도 계산이 직관적이지 않음
>   - 인류의 신석기 시대 및 농경 사회 진입 이후 예수 탄쟁 전까지의 10000년, 문자 발명 이후만 고려하더라도 3000-4000년에 달하는 역사를 '기원전'으로 퉁치는데, 이 때문에 세계사, 특히 고대사에 있어 인지적인 왜곡을 유발함
> 
> 그렇기 때문에 여기서는 `_data/locales`{: .filepath} 디렉터리에 로케일 파일들을 직접 추가 후 적당히 수정하여 적용한 것이다.  
> 따라서 해당사항이 없고, Chirpy 테마가 기본 제공하는 로케일을 수정 없이 그대로 적용하겠다면 이 단계는 건너뛰어도 된다.
{: .prompt-tip }

### Polyglot과 통합
이제 다음의 두 파일만 약간씩 수정하면 Polyglot과 매끄럽게 통합할 수 있다.

> 처음에 리포지터리를 생성할 때 테마 리포지터리를 직접 포크하지 않고 [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended)를 사용한 경우라면 해당하는 파일이 본인 사이트의 리포지터리에는 없을 수도 있다. 직접 추가하지 않아도 [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy)을 통해 기본 제공되는 파일들이기 때문인데, 그럴 경우에는 [Chirpy 테마 리포지터리](https://github.com/cotes2020/jekyll-theme-chirpy)에서 해당하는 파일 원본을 먼저 다운로드하여 본인의 리포지터리 내 동일 위치에 놓은 뒤 작업하면 된다. Jekyll이 사이트를 빌드할 때 리포지터리 내에 동일한 이름의 파일이 이미 있을 경우 [외부 gem(jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy)에서 제공하는 파일보다 우선적으로 적용한다.
{: .prompt-tip }

#### '\_includes/lang.html'
아래와 같이 [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) 파일 중간에 코드 두 줄을 추가하여, 페이지의 YAML front matter에 따로 `lang` 변수를 명시하여 지정하지 않은 경우 `_config.yml`{: .filepath}에 정의된 사이트 기본 언어(`site.lang`)나 영어(`'en'`)보다 [Polyglot의 `site.active_lang` 변수](https://github.com/untra/polyglot?tab=readme-ov-file#features)를 우선적으로 인식하도록 한다. 해당 파일은 Chirpy 테마를 적용한 사이트 내의 모든 페이지([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html))에서 빌드 시 `lang` 변수 선언을 위해 공통적으로 호출하는 파일로, 여기서 선언하는 `lang` 변수를 이용하여 레이아웃 언어 현지화를 실행한다.

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

`lang` 변수 선언 시 우선순위:
- 수정 전:
  1. `page.lang`(개별 페이지의 YAML front matter 내에 정의된 경우)
  2. `site.lang`(`_config.yml`{: .filepath}에 정의된 경우)
  3. `'en'`
- 수정 후:
  1. `page.lang`(개별 페이지의 YAML front matter 내에 정의된 경우)
  2. **`site.active_lang`**(Polyglot을 적용 중인 경우)
  3. `site.lang`(`_config.yml`{: .filepath}에 정의된 경우)
  4. `'en'`

#### '\_layouts/default.html'
마찬가지로 [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) 파일의 내용을 수정하여, HTML 문서 최상위 요소인 `<html>` 태그에 `lang` 속성을 올바르게 지정하도록 한다.

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

`<html>` 태그 `lang` 속성 지정 시 우선순위:
- 수정 전:
  1. `page.lang`(개별 페이지의 YAML front matter 내에 정의된 경우)
  2. `site.alt_lang`(`_config.yml`{: .filepath}에 정의된 경우)
  3. `site.lang`(`_config.yml`{: .filepath}에 정의된 경우)
  4. `unknown`(빈 문자열, `lang=""`)
- 수정 후:
  1. `page.lang`(개별 페이지의 YAML front matter 내에 정의된 경우)
  2. **`site.active_lang`**(Polyglot을 적용 중인 경우)
  3. `site.alt_lang`(`_config.yml`{: .filepath}에 정의된 경우)
  4. `site.lang`(`_config.yml`{: .filepath}에 정의된 경우)
  5. `unknown`(빈 문자열, `lang=""`)

> 웹 페이지 언어(`lang` 속성)를 지정하지 않고 `unknown`으로 두는 것은 권장하지 않으며, 가능한 한 적절한 값으로 지정해 두어야 한다. 보다시피 `_config.yml`{: .filepath} 내의 `lang` 속성 값을 fallback으로 사용하기 때문에, Polyglot을 사용하든 사용하지 않든 이 값은 반드시 적절히 정의해 두는 것이 좋으며 정상적인 경우라면 보통은 이미 정의되어 있을 것이다. 이 글에서 다루는 것과 같이 Polyglot 혹은 그와 유사한 i18n 플러그인을 적용한 경우라면 [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#설정-구성)과 동일한 값으로 지정하는 것이 무난할 것이다.
{: .prompt-tip }

## Further Reading
Continued in [Part 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
