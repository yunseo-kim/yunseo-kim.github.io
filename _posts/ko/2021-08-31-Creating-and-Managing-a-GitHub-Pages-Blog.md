---
title: GitHub Pages 블로그 만들고 관리하기
description: 정적 웹 페이지와 동적 웹 페이지의 특징과 차이, 정적 웹 사이트 생성기(Static Site Generator)에 대해 알아보고
  Jekyll 블로그를 GitHub Pages에 호스팅해 보자.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
[인류력](https://en.wikipedia.org/wiki/Holocene_calendar) 12021년 초부터 Jekyll을 이용해서 GitHub Pages에 블로그를 호스팅하기 시작했다. 그런데 블로그 구축 당시에 설치 과정을 제대로 정리를 안 해 놨더니 추후 유지관리할 때 어려움이 좀 있어서, 간략하게나마 설치 과정과 유지관리 방법을 정리해 놓기로 했다.  

(+ 12024.12 내용 업데이트)

## 1. 정적 사이트 생성기 & 웹 호스팅
### 1-1. 정적 웹 페이지 vs 동적 웹 페이지
#### 정적 웹 페이지(Static Web Page)
- 서버에 저장한 데이터를 그대로 사용자에게 전달하는 웹 페이지
- 웹 서버에서 사용자 요청에 해당하는 미리 저장해 둔 페이지를 전달함
- 사용자는 서버에 저장한 데이터를 변경하지 않는 한 동일한 웹 페이지를 보게 됨
- 요청에 해당하는 파일만 전송하면 되므로 추가적인 작업이 불필요하여, 일반적으로 응답이 빠름
- 단순한 파일들로만 구성되어 있어 웹 서버만 구축하면 되므로 구축 비용이 저렴함
- 저장해 둔 정보만 보여주므로 서비스가 한정적임
- 데이터 추가, 수정, 삭제를 관리자가 수동으로 해야 함
- 검색 엔진 측에서 크롤링하기 용이한 구조로, 검색 엔진 최적화(SEO)에 상대적으로 더 유리

#### 동적 웹 페이지(Dynamic Web Page)
- 서버에 저장한 데이터를 스크립트로 가공처리하여 전달하는 웹 페이지
- 웹 서버에서 사용자의 요청을 해석하여 데이터를 가공한 후 생성한 웹 페이지를 전달함
- 사용자는 상황, 시간, 요청 등에 따라 달라지는 웹 페이지를 보게 됨
- 웹 페이지 전달을 위해 스크립트를 처리해야 하므로 상대적으로 응답이 느림
- 웹 서버 외에 어플리케이션 서버가 필요하기 때문에 구축 시 추가 비용이 발생함
- 다양한 정보를 조합하여 동적으로 제공하므로 다양한 서비스가 가능함
- 웹 페이지 구조에 따라 데이터 추가, 수정, 삭제를 사용자가 브라우저에서 할 수 있음

### 1-2. 정적 웹 사이트 생성기(SSG, Static Site Generator)
- raw 데이터(보통 markdown 형식의 텍스트 파일)와 사전 정의된 템플릿을 기반으로 정적 웹 페이지를 생성해 주는 도구
- 개별 HTML 페이지를 직접 작성할 필요 없이, 마크다운으로 포스트를 작성하면 웹페이지를 빌드하여 웹 상에 배포하는 과정을 자동화함
- ex) Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- GitHub에서 무료로 제공하는 정적 웹 페이지 호스팅 서비스
- 계정별로 1개의 개인 대표 웹 페이지를 호스팅할 수 있고, 무제한으로 리포지터리별 프로젝트 문서 페이지를 생성 및 호스팅할 수 있다.
- '{username}.github.io' 형식의 이름으로 본인의 GitHub username에 맞춰 리포지터리를 생성한 후에, 해당 리포지터리에 빌드한 HTML 페이지를 직접 Push하거나 혹은 GitHub Actions를 활용하여 빌드 및 배포를 수행할 수 있다.
- 소유하고 있는 도메인이 있다면 설정에서 연결하여 '{username}.github.io' 형식의 기본 도메인 대신 다른 도메인 주소를 사용할 수도 있다.

## 2. 사용할 SSG와 테마 선택

### 2-1. Jekyll을 선택한 이유
Jekyll, Hugo, Gatsby 등 여러 SSG가 존재하지만, Jekyll을 사용하기로 결정하였다. 사용할 SSG를 선택하는 과정에서 고려한 기준과, Jekyll을 선택한 이유는 다음과 같다.
- 불필요한 시행착오를 최소화하고 글 작성과 블로그 운영에 집중할 수 있는가?
  - Jekyll은 Github Pages에서 공식 지원하는 정적 웹 사이트 생성기이다. 물론 Hugo, Gatsby 등 다른 SSG들도 Github Pages에서 얼마든지 호스팅할 수 있고 Netlify 등 아예 다른 호스팅 서비스를 이용한다는 선택지도 있지만, 사실 이 정도 규모의 개인 블로그를 운영하는 데 있어서 기술적으로 어떤 SSG를 사용하여 구축했는지와 빌드 속도, 성능 등은 크게 중요하지 않으므로 그냥 조금이라도 더 유지보수가 간단하고 참고할 문서가 많은 것이 좋겠다고 판단했다.
  - Jekyll은 또한 Hugo, Gatsby 등 다른 경쟁자들에 비해 개발 기간이 제일 길다. 그만큼 관련 문서화가 잘 되어 있고, 실제로 문제가 생겼을 때 참고할 수 있는 자료의 양이 압도적으로 많다.
- 사용할 수 있는 테마와 플러그인이 다양한가?
  - 직접 HTML을 작성하는 게 아니라 SSG를 사용한다고 해도, 각종 템플릿을 직접 만들어 내는 것은 번거롭고 시간도 오래 걸리며 굳이 그럴 필요도 없다. 웹 상에 이미 공개되어 있는 훌륭한 테마들이 많으니, 마음에 드는 것을 채택해서 활용하면 된다.
  - 더군다나 나는 원래 C나 Python을 주로 활용하기 때문에, Jekyll의 Ruby나 Hugo의 Go 언어는 잘은 모르는 상황이라 더더욱 기존에 개발되어 있는 테마와 플러그인들을 적극적으로 활용하려고 했다.
  - Jekyll에는 한눈에 봐도 마음에 드는 테마를 금방 찾아낼 수 있었던 반면, Hugo나 Gatsby는 상대적으로 개인 블로그 목적으로 쓰기에 적합한 테마의 수가 그리 많지는 않았던 것 같다. 아무래도 상술한 것처럼 개발자들이 개인 블로그 호스팅을 위해 많이 사용하는 Github Pages와의 연동성, 그리고 개발 기간이 여기에도 영향을 크게 미친 것 같다.

### 2-2. 테마 선택
#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- 블로그를 처음 만들고 약 1년 3개월 동안 활용했던 테마
- Disqus, Discourse, utterances 등을 통한 댓글 기능 지원
- 카테고리와 태그 분류 기능 지원
- Google Analytics 기본 지원
- 사전 정의된 스킨 선택 가능
- 디자인이 더 유려하고 마음에 드는 Chirpy 테마를 이후에 발견하고 넘어가긴 했지만, 어차피 공돌이스러운 블로그라는 걸 감안하면 예쁘진 않아도 나름 깔끔한 디자인을 가지고 있어서 무난히 사용할 만 했던 것 같다.

#### Chirpy Jekyll Theme (12022.04 - 현재)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- 12022년 4월에 블로그 테마를 이전한 이후 지금까지 사용 중인 테마
- 다중 카테고리 분류, 태그 기능 지원
- MathJax 기반으로 LaTex 문법의 수식 표현을 기본 지원
- Mermaid 기반의 다이어그램 기능 기본 지원
- Disqus, Giscus 등을 통한 댓글 기능 지원
- Google Analytics, GoatCounter 지원
- 라이트 테마와 다크 테마 지원
- 테마 전환 시점 기준으로 MathJax나 Mermaid는 Minimal Mistakes 테마에서는 자체 지원하지 않아서 직접 커스터마이징으로 추가해 주어야 했는데, Chirpy 테마에서는 기본적으로 자체 지원한다. 물론 커스터마이징이라 해 봤자 별 거 없긴 하지만 그래도 소소한 이점이라 할 수 있다.
- 무엇보다, 디자인이 예쁘다. Minimal Mistakes 테마는 깔끔은 하지만 뭔가 블로그보단 프로젝트 공식 기술문서나 포트폴리오 페이지에 더 적합할 듯한 특유의 딱딱함이 있는데, Chirpy 테마는 티스토리나 미디엄, velog 등의 상용 블로그 플랫폼과 비교해도 별로 꿇리지 않는 디자인이 장점이다.

## 3. GitHub 리포지터리 생성, 빌드 및 배포하기
현재(12024.06) 사용 중인 Chirpy Jekyll Theme을 기준으로 기술하며, Git은 기본적으로 설치하였다고 가정하고 진행한다.  
[Jekyll 공식 설치 가이드](https://jekyllrb.com/docs/installation/)와 [Chirpy Jekyll Theme 공식 페이지](https://github.com/cotes2020/jekyll-theme-chirpy/wiki) 참고.

### 3-1. Ruby & Jekyll 설치하기
[Jekyll 공식 설치 가이드](https://jekyllrb.com/docs/installation/)에 따라 자신의 운영체제 환경에 맞추어 Ruby와 Jekyll을 설치한다.

### 3-2. GitHub 리포지터리 생성
[Chirpy Jekyll Theme 공식 페이지](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site)에서는 다음 두 가지 방법을 소개하고 있다.
1. "jekyll-theme-chirpy" gem으로 핵심 파일들을 불러오고 나머지 리소스를 [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) 템플릿으로부터 가져오는 방법
  - 장점: 후술하겠지만 버전 업그레이드 적용이 용이하다.
  - 단점: 커스터마이징이 제한된다.
2. [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 리포지터리를 본인 블로그의 리포지터리로 포크하는 방법
  - 장점: 모든 파일들을 리포지터리 안에서 직접 관리하므로 테마에서 지원하지 않는 기능도 직접 코드를 수정하여 자유롭게 커스터마이징할 수 있다.
  - 단점: 버전 업그레이드를 적용하려면 [원본 리포지터리의 최신 업스트림 태그](https://github.com/cotes2020/jekyll-theme-chirpy/tags)를 merge해야 하는데, 경우에 따라선 직접 커스터마이징한 코드가 업그레이드 버전의 코드와 충돌할 수 있다. 이 경우 해당 충돌을 직접 해결해야 한다.

나는 1번 방법을 채택하였다. Chirpy 테마의 경우 기본적으로 완성도가 높아서 대부분의 유저 입장에선 커스터마이징할 게 크게 없는 데다가, 12024년 현재까지도 상당히 활발하게 개발 및 기능 개선이 진행 중이라 어지간히 마개조를 할 게 아니라면 원본 업스트림을 제때 따라가는 것의 이점이 직접 커스터마이징을 적용하는 것의 이점을 상회한다. Chirpy 테마 공식 가이드에서도 대부분의 유저에게는 1번 방법을 권장하고 있다.

### 3-3. 주요 설정
루트 디렉터리의 `_config.yml`{: .filepath} 파일과 `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath} 파일에서 필요한 설정들을 적용한다. 주석이 잘 달려 있고 설정들이 직관적이라 별다른 어려움 없이 적용할 수 있다. 그나마 외부에서 별도의 작업이 필요한 설정으로 Google Search Console 연동을 위한 인증 코드 등록과 Google Analytics나 GoatCounter 등의 웹마스터 도구 연동 정도가 있는데, 이것도 사실 그리 복잡한 절차는 아니고 이 글에서 다루려는 핵심 주제는 아니기 때문에 자세한 서술은 생략한다.

### 3-4. 로컬에서 빌드하기
필수 절차는 아니지만, 새로운 포스트를 작성하거나 혹은 사이트에 뭔가 수정을 가했을 때 웹에서 정상적으로 표시될지 미리 확인하고 싶을 수 있다. 이럴 때는 로컬 리포지터리의 루트 디렉터리에서 터미널을 열고 아래 명령을 실행하면 된다.
```console
$ bundle exec jekyll s
```
몇 초 정도 기다리면 사이트가 로컬에서 빌드되어 <http://127.0.0.1:4000> 주소에서 결과물을 확인할 수 있다.

### 3-5. 배포하기
두 가지 방법이 있다.
1. GitHub Actions 활용 (GitHub Pages에서 호스팅하는 경우)
  - GitHub Free Plan을 사용 중이라면, 리포지터리를 public으로 유지해야 함
  - GitHub 웹페이지에서 리포지터리의 *Settings* 탭을 선택한 뒤, 왼쪽의 네비게이션 바에서 *Code and automation > Pages*를 클릭하고 **Source** 섹션에서 **GitHub Actions** 옵션을 선택
  - 설정 완료 후 새로운 커밋을 Push할 때마다 *Build and Deploy* 워크플로우를 자동 실행함
2. 직접 빌드하여 배포 (다른 호스팅 서비스를 활용하거나 셀프 호스팅하는 경우)
  - 아래 명령을 실행하여 직접 사이트 빌드
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - `_site` 디렉터리에 있는 빌드 결과물을 서버에 업로드

## 4. 포스트 작성
Chirpy 테마의 [포스트 작성 가이드](https://chirpy.cotes.page/posts/write-a-new-post/)에 포스트 작성 방법과 사용할 수 있는 옵션이 잘 문서화되어 있다. 이 글에서 서술하는 것 외에도 다양한 기능을 제공하고 있으며, 참고하면 좋은 내용들이니 필요하다면 공식 문서를 참고하도록 하자. 여기서는 매번 포스팅할 때마다 공통적으로 염두에 두어야 하는 주요 사항들을 정리해 둔다.

### 마크다운 파일 생성
- 이름 형식: `YYYY-MM-DD-TITLE.md`{: .filepath}
- 위치: `_posts`{: .filepath} 디렉터리

### Front Matter 작성
마크다운 파일의 첫 부분에는 Front Matter를 적절하게 작성해야 한다.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: 포스트 제목
- **description**: 요약문. 작성하지 않을 시 본문 내용의 앞부분 일부를 자동으로 가져다 사용하지만 검색엔진 최적화(SEO)를 위해서는 description 메타 태그를 직접 적절히 작성해 주는 것을 권장함. 로마자 기준 135~160자, 한글 기준 80~110자 정도 분량이 적절함.
- **date**: 정확한 포스트 작성 일시와 timezone(생략 가능, 생략 시 파일의 작성 날짜 또는 수정된 날짜 정보를 자동으로 인식해 사용)
- **categories**: 포스트의 카테고리 분류
- **tags**: 포스트에 적용할 태그 분류
- **image**: 포스트 상단에 미리보기 이미지 삽입
  - **path**: 이미지 파일 경로
  - **alt**: 대체 텍스트(생략 가능)
- **toc**: 오른쪽 사이드바의 목차 기능 사용 여부, 기본값은 `true`
- **comments**: 사이트 기본 설정과 별개로, 개별 포스트의 댓글 사용 여부를 명시적으로 지정하고 싶을 경우 사용
- **math**: 내장된 [MathJax](https://www.mathjax.org/) 기반 수식 표현 기능 활성화, 기본값은 페이지 성능을 위해 비활성화(`false`)
- **mermaid**: 내장된 [Mermaid](https://github.com/mermaid-js/mermaid) 기반 다이어그램 표현 기능 활성화, 기본값은 비활성화(`false`)

## 5. 업그레이드

[3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-github-리포지터리-생성)에서 1번 방법을 채택했다고 가정하고 서술한다. 2번 방법을 채택했다면 상술했듯 최신 업스트림 태그를 직접 merge해야 한다.

1. `Gemfile`{: .filepath}을 편집해서 "jekyll-theme-chirpy" gem의 버전을 새로 지정한다.
2. 메이저 업그레이드의 경우, "jekyll-theme-chirpy" gem에 포함되지 않은 핵심 파일들과 설정 옵션도 변경되었을 수 있다. 이때는 아래의 GitHub API로 변경사항을 확인한 후 직접 반영해 주어야 한다.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
