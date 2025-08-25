---
title: 웹 성능 지표 (Web Vitals)
description: 웹 성능 지표(Web Vitals)와 Lighthouse 측정 및 평가 기준을 정리하고, 각 성능 지표가 무엇을 의미하는지 알아본다.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## 웹 성능을 결정하는 요소
웹 성능 최적화 시 고려해야 할 웹 성능을 결정하는 요소는 크게는 로딩 성능, 렌더링 성능의 두 가지로 분류할 수 있다.

### HTML 로딩 성능
- 네트워크를 통해 서버에 최초로 웹페이지를 요청한 후, HTML 문서를 받아 와 브라우저가 렌더링을 시작할 때까지의 시간
- 얼마나 빨리 페이지가 표시되기 시작하는가를 결정
- 리다이렉트 최소화, HTML 응답 캐싱, 리소스 압축, 적절한 CDN 활용 등의 방법으로 최적화

### 렌더링 성능
- 브라우저가 사용자가 보는 화면을 그리고 상호작용 가능하게끔 하는 데 걸리는 시간
- 얼마나 부드럽고 빠르게 화면이 그려지는가를 결정
- 불필요한 CSS 및 JS 제거, 폰트 및 썸네일 지연 로딩 방지, 무거운 연산은 별도의 Web Worker로 분리하여 메인 쓰레드 점유 최소화, 애니메이션 최적화 등의 방법으로 최적화

## 웹 성능 지표 (Web Vitals)
구글의 [web.dev](https://web.dev/performance?hl={{ site.active_lang }})와 [Chrome 개발자 문서](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }})를 기준으로 서술한다. 특별한 이유가 있는 게 아니라면 어느 한 성능 지표에만 집중하기보다는 전체적인 개선을 목표로 하는 것이 좋으며, 최적화하고자 하는 웹페이지에서 어떤 부분이 성능에 병목으로 작용하는지 파악하는 것이 중요하다. 또한 실제 사용자 데이터 통계가 있는 경우, 상위권이나 평균에 해당하는 값보다는 Q1 정도의 하위권 값에 주목하여 그 경우에도 목표 기준을 달성하는지 확인하고 개선하는 것이 좋다.

### 주요 웹 성능 지표 (Core Web Vitals)
잠시 후 다루겠지만 웹 성능 지표(Web Vitals)에는 여러 가지가 있다. 그러나 그 중에서도 특히 사용자 경험에 밀접한 연관이 있고, 모의 환경이 아닌 실제 환경에서 측정이 가능한 다음 3가지 지표를 구글에서는 특히 중요하게 간주하며, 이를 [주요 웹 성능 지표(Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals)라고 한다. 구글은 자사 검색엔진의 검색 결과 순서에도 대상 사이트의 주요 웹 성능 지표를 반영하기 때문에 사이트 운영자 입장에서도 이들 지표는 검색엔진 최적화(SEO)의 측면에서 유의 깊게 살펴야 한다.
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): *로딩 성능* 반영, 2.5초 이내여야 함
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): *응답성* 반영, 200ms 이하여야 함
- [Cummulative Layout Shift (CLS)](#cls-cumulative-layout-shift): *시각적 안정성* 반영, 0.1 이하로 유지해야 함

주요 웹 성능 지표는 기본적으로 실제 환경에서 측정하기 위한 것이지만, INP를 제외한 나머지 둘은 Chrome 개발자 도구나 Lighthouse와 같은 모의 환경에서도 측정할 수 있다. INP의 경우에는 실제 사용자 입력이 주어져야 측정 가능하므로 모의 환경에서는 측정할 수 없으나, 이런 경우 [TBT](#tbt-total-blocking-time)가 INP와 매우 상관관계가 높고 유사한 성능 지표이므로 대신 참고할 수 있으며 [보통은 TBT를 개선하면 INP도 함께 개선된다](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Lighthouse 10의 성능 점수 가중치
[Lighthouse의 성능 점수는 각 측정항목 점수의 가중 평균으로 계산하며, 이때 다음 표의 가중치를 따른다](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| 측정항목 | 가중치 |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- 페이지 요청 후 첫 DOM 콘텐츠를 렌더링하는 데까지의 소요 시간을 측정
- 페이지 내 이미지, 흰색이 아닌 `<canvas>` 요소, SVG 등을 DOM 콘텐츠로 간주하며, `iframe` 내 콘텐츠는 고려하지 않음

> FCP에 특히 중요하게 영향을 미치는 요소 중 하나는 글꼴 로딩 시간으로, 이에 관한 최적화는 [관련 포스트](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }})를 참고해 볼 것을 [Chrome 개발자 문서](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})에서는 권고하고 있다.
{: .prompt-tip }

#### Lighthouse 평가 기준
[Chrome 개발자 문서](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }})에 따르면, Lighthouse의 평가 기준은 다음 표와 같다.

| 색상 등급 | 모바일 FCP (초) | 데스크탑 FCP (초) |
| --- | --- | --- |
| 녹색 (빠름) | 0-1.8 | 0-0.9 |
| 주황색 (중간) | 1.8-3 | 0.9-1.6 |
| 빨간색 (느림) | 3 초과 | 1.6 초과 |

### LCP (Largest Contentful Paint)
- 웹페이지를 처음 열었을 때 제일 먼저 화면에 보이는 표시 영역(viewport)을 기준으로, 해당 영역 내에서 가장 크게 표시되는 요소(이미지, 텍스트 블록, 영상 등)를 렌더링하기까지의 소요 시간을 측정
- 화면상에서 차지하는 면적이 넓을수록 사용자 입장에서 주요 콘텐츠로 체감할 가능성이 높을 것임
- LCP가 이미지일 경우, 소요 시간을 4개의 하위 구간으로 나눌 수 있으며 이 중 병목이 발생하는 부분이 어디인지를 파악하는 것이 중요함
  1. Time to first byte (TTFB): 페이지 로드 시작 시점부터 HTML 문서 응답의 첫 바이트를 수신한 시점까지의 시간
  2. 로드 지연(Load delay): 브라우저가 LCP 리소스를 로드하기 시작한 시점과 TTTB 사이의 차
  3. 로드 시간(Load time): LCP 리소스 자체를 로드하는 데 걸린 시간
  4. 렌더링 지연(Render delay): LCP 리소스 로드를 완료한 시점부터 LCP 요소를 완전히 렌더링 완료할 때까지의 시간

#### Lighthouse 평가 기준
[Chrome 개발자 문서](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }})에 따르면, Lighthouse의 평가 기준은 다음 표와 같다.

| 색상 등급 | 모바일 FCP (초) | 데스크탑 FCP (초) |
| --- | --- | --- |
| 녹색 (빠름) | 0-2.5 | 0-1.2 |
| 주황색 (중간) | 2.5-4 | 1.2-2.4 |
| 빨간색 (느림) | 4 초과 | 2.4 초과 |

### TBT (Total Blocking Time)
- 웹페이지가 마우스 클릭, 화면 터치, 키보드 입력과 같은 사용자 입력에 반응하지 못하는 총 시간을 측정
- FCP와 [TTI(상호작용 시작 시점, Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* 사이의 작업들 중 50ms 이상 실행된 작업들을 [긴 작업](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }})으로 간주, 이러한 긴 작업들 각각에 소요된 시간에서 50ms를 뺀 초과분을 *차단 부분(blocking portion)*이라 하고 모든 차단 부분들의 합계를 TBT로 정의함

> \* TTI 자체는 네트워크 응답 이상치와 긴 작업들에 지나치게 민감하여 일관성이 낮고 높은 변동성을 가지며, 이에 따라 [Lighthouse 10부터는 성능 평가 항목에서 제외하였다](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> 일반적으로 긴 작업을 유발하는 가장 흔한 원인은 불필요하거나 비효율적인 자바스크립트 로딩, 파싱 및 실행이며, [코드 분할](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }})을 통해 각각이 50ms 이내에 실행 가능하도록 자바스크립트 페이로드 크기를 줄이고 필요하다면 메인 쓰레드가 아닌 별도의 서비스 worker로 분리하여 멀티쓰레드로 실행하는 것을 고려하라고 [Chrome 개발자 문서](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})와 [구글의 web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }})는 권고하고 있다.
{: .prompt-tip }

#### Lighthouse 평가 기준
[Chrome 개발자 문서](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }})에 따르면, Lighthouse의 평가 기준은 다음 표와 같다.

| 색상 등급 | 모바일 FCP (밀리초) | 데스크탑 FCP (밀리초) |
| --- | --- | --- |
| 녹색 (빠름) | 0-200 | 0-150 |
| 주황색 (중간) | 200-600 | 150-350 |
| 빨간색 (느림) | 600 초과 | 350 초과 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="갑작스러운 레이아웃 변경의 예시" autoplay=true loop=true %}
> 영상 출처: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~커서 움직임에서 깊은 분노가 느껴진다~~

- 예기치 않은 레이아웃 변경은 텍스트가 갑자기 이동하여 읽던 위치를 놓치거나, 링크 혹은 버튼을 잘못 클릭하게 하는 등 여러 방식으로 사용자 경험을 저해함
- CLS 점수를 산정하는 구체적인 방식은 [구글의 web.dev](https://web.dev/articles/cls)에 기술되어 있음
- 아래 이미지에서 확인할 수 있듯, 0.1 이하를 목표로 해야 함

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> 이미지 출처: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- 페이지를 로드하는 동안 콘텐츠가 얼마나 빨리 시각적으로 표시되는지를 측정
- Lighthouse는 브라우저에서 페이지를 로드하는 과정을 영상으로 녹화하고, 해당 영상을 분석하여 프레임 간의 진행을 계산한 뒤 [Speedline Node.js 모듈](https://github.com/paulirish/speedline)을 사용하여 SI 점수를 산정함

> 앞서 [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint), [TBT](#tbt-total-blocking-time)에 대해 정리하면서 언급했던 것들을 비롯해, 페이지 로딩 속도를 개선하는 조치라면 무엇이든 SI 점수에도 긍정적으로 작용한다. 페이지 로딩의 어느 한 과정만 대표하기보다는 전체 로딩 과정을 일정 수준 반영하는 성능 지표라고 볼 수 있다.
{: .prompt-tip }

#### Lighthouse 평가 기준
[Chrome 개발자 문서](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }})에 따르면, Lighthouse의 평가 기준은 다음 표와 같다.

| 색상 등급 | 모바일 SI (초) | 데스크탑 SI (초) |
| --- | --- | --- |
| 녹색 (빠름) | 0-3.4 | 0-1.3 |
| 주황색 (중간) | 3.4-5.8 | 1.3-2.3 |
| 빨간색 (느림) | 5.8 초과 | 2.3 초과 |
