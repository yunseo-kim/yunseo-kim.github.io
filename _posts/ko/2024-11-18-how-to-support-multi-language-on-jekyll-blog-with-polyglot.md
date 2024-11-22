---
title: Polyglot으로 Jekyll 블로그에서 다국어 지원하는 방법 (1) - Chirpy 테마에 Polyglot 적용 & 트러블슈팅
description: >-
  'jekyll-theme-chirpy' 기반의 Jekyll 블로그에 Polyglot 플러그인을 적용하여 다국어 지원을 구현한 과정을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
- RegExp
---
## 들어가며
약 4달 전인 2024년 7월 초, Jekyll 기반으로 Github Pages를 통해 호스팅 중인 본 블로그에 Polyglot 플러그인을 적용하여 다국어 지원 구현을 추가하였다.
이 글에서는 Polyglot 플러그인을 적용하는 과정에서 발생한 버그와 그 해결 과정, 그리고 SEO를 고려한 html 헤더와 sitemap.xml 작성법을 공유한다.

## 요구사항
- 빌드한 결과물(웹페이지)을 언어별 경로(ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath})로 구분하여 제공할 수 있어야 한다.
- 다국어 지원에 추가적으로 소요되는 시간과 노력을 가능한 최소화하기 위해, 작성한 원본 마크다운 파일의 YAML front matter에 'lang' 및 'permalink' 태그를 일일이 지정해 주지 않아도 빌드 시 해당 파일이 위치한 로컬 경로(ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath})에 따라 자동으로 언어를 인식할 수 있어야 한다.
- 사이트 내 각 페이지의 헤더 부분은 적절한 Content-Language 메타 태그와 hreflang 대체 태그를 포함하여 구글 다국어 검색을 위한 SEO 가이드라인을 충족해야 한다.
- 사이트 내에서 각 언어를 지원하는 모든 페이지 링크를 누락 없이 `sitemap.xml`에서 제공할 수 있어야 하며, `sitemap.xml` 자체는 중복 없이 루트 경로에 하나만 존재하여야 한다.

## Polyglot 플러그인 적용
Jekyll은 다국어 블로그를 기본 지원하지 않으므로, 위의 요구사항을 만족하는 다국어 블로그 구현을 위해서는 외부 플러그인을 활용해야 한다. 검색해보니 [Polyglot](https://github.com/untra/polyglot)이 다국어 웹사이트 구현 용도로 많이 쓰이며, 위 요구사항들을 모두 만족시킬 수 있어 해당 플러그인을 채택하였다.

### 플러그인 설치
나는 Bundler를 사용 중이므로 `Gemfile`에 다음 내용을 추가하였다.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

이후 터미널에서 `bundle update`를 실행하면 자동으로 설치가 완료된다.

만약 Bundler를 사용하지 않을 경우, 터미널에서 `gem install jekyll-polyglot` 명령으로 gem을 직접 설치한 후 `_config.yml`에 다음과 같이 플러그인을 추가할 수도 있다.

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### 설정 구성
다음으로 `_config.yml` 파일을 열고 아래 내용을 추가한다.

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
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

> 'parallel_localization'을 'true'로 지정하면 빌드 시간이 상당히 단축되는 장점이 있으나, 2024년 7월 시점 기준으로 본 블로그에 대해 해당 기능을 활성화했을 때 페이지 오른쪽 사이드바의 'Recently Updated'와 'Trending Tags' 부분 링크 제목이 정상적으로 처리되지 않고 다른 언어와 뒤섞이는 버그가 있었다. 아직 안정화가 덜 된 것 같으니 사이트에 적용하려면 미리 정상 작동하는지 테스트를 거칠 필요가 있다.
{: .prompt-warning }

### 포스트 작성 시 유의사항
다국어 포스트 작성 시 유의해야 할 점은 다음과 같다.
- 적절한 언어 코드 지정: 파일 경로(ex. `/_posts/ko/example-post.md`{: .filepath}) 또는 YAML front matter의 'lang' 속성(ex. `lang: ko`)을 이용하여 적절한 ISO 언어 코드를 지정해 주어야 한다. [Chrome 개발자 문서](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)의 예시를 참고한다.

> 단, [Chrome 개발자 문서](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales)에서는 지역코드를 'pt_BR'과 같은 형식으로 표기하고 있으나 실제로는 'pt-BR'과 같이 _ 대신 -를 사용하여야 추후 html 헤더에 hreflang 대체 태그를 추가할 때 정상 작동한다.

- 파일 경로와 이름은 일관적이어야 한다.

자세한 사항은 GitHub [untra/polyglot 리포지터리의 README](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it)를 참고하기 바란다.

## 트러블슈팅 ('relative_url_regex': target of repeat operator is not specified)
앞선 단계까지 진행한 후에 `bundle exec jekyll serve` 명령을 실행하여 빌드 테스트를 하였더니, `'relative_url_regex': target of repeat operator is not specified`라는 에러가 발생하며 빌드에 실패하였다.

```shell
...(전략)
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

...(후략)
```

비슷한 이슈가 보고된 적 있는지 검색해본 결과, Polyglot 리포지터리에 [정확히 동일한 이슈](https://github.com/untra/polyglot/issues/204)가 이미 등록되어 있었으며 해결책 또한 존재했다.

본 블로그에 적용 중인 [Chirpy 테마의 `_config.yml`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml) 파일 중에는 다음과 같은 구문이 존재한다.

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

문제의 원인은 [Polyglot의 `site.rb`](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb) 파일에 포함된 다음 두 함수의 정규식 구문이 위의 `"*.gem"`, `"*.gemspec"`, `"*.config.js"`과 같이 와일드카드를 포함하는 글로빙(globbing) 패턴을 정상적으로 처리하지 못하는 데 있다.

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

이 문제를 해결하는 방법은 두 가지이다.

### 1. Polyglot을 포크(fork)한 뒤 문제가 되는 부분을 수정하여 사용
이 글을 작성하는 시점(2024.11.) 기준으로 [Jekyll 공식 문서](https://jekyllrb.com/docs/configuration/options/#global-configuration)에서는 `exclude` 설정이 글로빙(globbing) 패턴 활용을 지원한다고 명시하고 있다.

>"This configuration option supports Ruby's File.fnmatch filename globbing patterns to match multiple entries to exclude."

즉, 문제의 원인은 Chirpy 테마가 아니라 Polyglot의 `relative_url_regex()`, `absolute_url_regex()` 두 함수에 있으므로 이를 문제가 발생하지 않게끔 수정해 주는 것이 근본적인 해결책이다.

Polyglot에서 해당 버그는 아직 해결되지 않은 상태이므로, [이 블로그 포스트](https://hionpu.com/posts/github_blog_4#4-polyglot-%EC%9D%98%EC%A1%B4%EC%84%B1-%EB%AC%B8%EC%A0%9C)와 [앞선 GitHub 이슈에 달린 답변](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322)을 참고하여 Polyglot 리포지터리를 포크(fork)한 뒤에 문제가 되는 부분을 다음과 같이 수정하여 원본 Polyglot 대신 사용하면 된다.

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

### 2. Chirpy 테마의 `_config.yml` 설정 파일에서 글로빙(globbing) 패턴을 정확한 파일명으로 대체
사실 정석적이고 이상적인 방법은 위의 패치가 Polyglot 메인스트림에 반영되는 것이다. 그러나 그 전까지는 포크한 버전을 대신 사용하여야 하는데, 이 경우 Polyglot 업스트림이 버전업될 때마다 해당 업데이트를 놓치지 않고 반영하며 따라가기가 번거롭기 때문에 나는 다른 방법을 사용하였다.

[Chirpy 테마 리포지터리]()에서 프로젝트 루트 경로에 위치하는 파일 중 `"*.gem"`, `"*.gemspec"`, `"*.config.js"` 패턴에 대응하는 파일을 확인해 보면 어차피 아래의 3개밖에 없다.
- `jekyll-theme-chirpy.gemspec`
- `purgecss.config.js`
- `rollup.config.js`

따라서 `_config.yml` 파일의 `exclude` 구문에서 글로빙(globbing) 패턴을 삭제하고 아래와 같이 바꿔 적어 주면 Polyglot이 문제 없이 처리할 수 있게 된다.

```yml
exclude: # https://github.com/untra/polyglot/issues/204 이슈 참고하여 수정.
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```

https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7#diff-ecec67b0e1d7e17a83587c6d27b6baaaa133f42482b07bd3685c77f34b62d883