---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인
description: >-
  마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic으로부터 발급받은 API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## 들어가며
최근에 블로그 포스트의 다국어 번역을 위해 Anthropic의 Claude 3.5 Sonnet API를 도입하였다. 이에 이 시리즈에서는 도입 과정에서 Claude 3.5 Sonnet API를 선택한 이유와 프롬프트 디자인 방법, 그리고 Python 스크립트를 통한 API 연동 및 자동화 구현 방법을 다루고자 한다.  
시리즈는 2개의 글로 이루어져 있으며, 읽고 있는 이 글은 해당 시리즈의 첫 번째 글이다.
- 1편: Claude 3.5 Sonnet 모델 소개 및 선정 이유, 프롬프트 엔지니어링 (본문)
- 2편: [API를 활용한 Python 자동화 스크립트 작성 및 적용](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## About Claude 3.5 Sonnet
Claude 3 시리즈 모델은 모델 크기에 따라 Haiku, Sonnet, 그리고 Opus 버전이 제공된다.  
![Claude 3 모델 티어 구분](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 이미지 출처: [Anthropic Claude API 공식 웹페이지](https://www.anthropic.com/api)

그리고 한국 시각으로 2024년 6월 21일, Anthropic에서 최신 언어모델인 [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)를 공개하였다. Anthropic의 발표에 의하면 기존의 Claude 3 Sonnet와 동일한 비용과 속도로 Claude 3 Opus를 능가하는 추론 성능을 보인다고 하며, 대체로 작문과 언어 추론, 다국어 이해 및 번역 분야에서 경쟁 모델인 GPT-4 대비 강점을 보인다는 평이 지배적이다.  
![Claude 3.5 Sonnet 소개 이미지](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet 성능 벤치마크 결과](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 이미지 출처: [Anthropic 홈페이지](https://www.anthropic.com/news/claude-3-5-sonnet)

(2024.10.31. 추가) 2024년 10월 22일, Anthropic에서 Claude 3.5 Sonnet의 업그레이드 버전 API("claude-3-5-sonnet-20241022")와 Claude 3.5 Haiku를 발표하였다. 다만 [후술할 문제](#게으름-피우기-방지-20241031-할로윈-패치)로 인해 아직은 본 블로그에는 기존의 "claude-3-5-sonnet-20240620" API를 적용하고 있다.

## 포스트 번역을 위해 Claude 3.5를 도입한 이유
굳이 Claude 3.5나 GPT-4와 같은 언어모델이 아니더라도 구글 번역이나 DeepL과 같은 기존의 상용 번역 API가 존재한다. 그럼에도 번역 목적으로 LLM을 사용하기로 결정한 이유는 다른 상용 번역 서비스와 달리 사용자가 프롬프트 디자인을 통해 모델에게 글의 작성 목적이나 주요 주제 등 본문 외에도 추가적인 맥락 정보나 요구사항을 제공할 수 있고, 모델은 이에 맞추어 문맥을 고려한 번역을 제공할 수 있기 때문이다. DeepL이나 구글 번역도 대체로 뛰어난 번역 품질을 보이는 편이지만, 글의 주제나 전체적인 맥락을 잘 파악하지 못하는 한계 때문에 일상적인 회화가 아닌 전문적인 주제의 긴 글을 번역하도록 요청했을 때는 상대적으로 번역 결과물이 부자연스러운 경우가 있었다. 특히나 Claude는 상술하였듯 경쟁 모델인 GPT-4 대비 작문, 언어 추론, 다국어 이해 및 번역 분야에서는 상대적으로 더 뛰어나다는 평이 많으며 직접 간단히 테스트해 보았을 때도 GPT-4o보다 좀 더 매끄러운 번역 품질을 보였기에, 이 블로그에 기재하는 공학 관련 글들을 여러 언어로 번역하는 작업에 적합하다고 판단하였다.

## 프롬프트 디자인
### 뭔가를 요청할 때의 기본 원칙
언어모델로부터 목적에 부합하는 만족스러운 결과물을 얻기 위해서는 그에 맞는 적절한 프롬프트를 제공해야 한다. 프롬프트 디자인이라고 하면 뭔가 막막하게 느껴질 수 있지만, 사실 '뭔가를 잘 요청하는 방법'이란 상대방이 언어모델이든 사람이든 크게 다르지 않으므로 이와 같은 관점에서 접근하면 별로 어렵지 않다. 육하원칙에 따라 현 상황 및 요청사항을 명확히 설명하고, 필요하다면 몇 가지 구체적인 예시를 덧붙이는 것도 좋다. 프롬프트 디자인에 관한 수많은 팁과 기법들이 존재하지만, 대부분은 후술할 기본 원칙에서 파생되는 것들이다.

#### 전체적인 어조
고압적인 명령조보다는 정중하게 요청하는 어조로 프롬프트를 작성하고 입력하였을 때 언어모델이 보다 높은 품질의 응답을 출력한다는 보고가 많이 있다. 보통 사회에서 다른 사람에게 뭔가 요청할 때도 전자보다는 후자와 같은 말투로 요청했을 때 상대방이 더 성의 있게 부탁한 작업을 수행할 확률이 높아지는데, 언어모델도 이와 같은 사람들의 응답 패턴을 학습하여 모방하는 것으로 보인다.

#### 역할 부여 및 상황 설명(누가, 왜)
제일 먼저 Claude 3.5에게 *'기술 분야 전문 번역가(professional technical translator)'* 라는 역할을 부여하고, *"주로 수학이나 물리학, 데이터 과학에 관한 글을 기고하는 공학 블로거"* 라는 사용자에 관한 맥락 정보를 제공하였다.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### 큰 틀에서의 요청사항 전달(무엇을)
다음으로, 사용자로부터 제공된 마크다운 형식의 글을 {source_lang}에서 {target_lang}으로 형식을 유지하면서 번역하도록 요청하였다. 

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Claude API 호출 시, 프롬프트의 {source_lang}과 {target_lang} 자리에는 Python 스크립트의 f-string 기능을 통해 번역 출발언어와 도착언어 변수가 각각 들어간다.
{: .prompt-info }

#### 요구사항 구체화 및 예시(어떻게)
간단한 작업이라면 앞선 단계까지만 해도 충분히 원하는 결과를 얻는 경우도 있지만, 복잡한 작업을 요구하는 경우에는 추가적인 설명이 필요할 수 있다. 

요구 조건이 복잡하고 여러 가지일 경우, 각각의 사항을 풀어 서술하는 것보다 두괄적으로 목록화하여 전달하면 가독성이 향상되고 읽는 입장(인간이든 언어모델이든)에서 이해하기 쉽다. 또한 필요하다면 예시도 같이 제공하는 것이 도움이 된다.
이 경우에는 다음과 같은 조건들을 추가하였다.

##### YAML front matter의 처리
Jekyll 블로그에 업로드하기 위해 markdown으로 작성한 포스트의 첫 부분에 위치한 YAML front matter에는 'title'과 'description', 'categories', 그리고 'tags' 정보를 기록한다. 가령, 이 글의 YAML front matter는 다음과 같다.

```yaml
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: \>-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

그런데 포스트를 번역할 때 제목(title)과 설명(description) 태그는 다국어로 번역해야 하나, 포스트 URL의 일관성을 위해서는 카테고리(categories)와 태그(tags) 이름은 번역하지 않고 영문 그대로 놔두는 것이 유지관리에 용이하다. 따라서 아래와 같은 지시를 내려서 'title'과 'description' 이외의 태그는 번역하지 않도록 하였다. Claude가 YAML front matter에 관한 정보는 이미 학습하여 알고 있을 것이므로, 이 정도만 설명해도 대부분의 경우 충분하다.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> "under any circumstances, regardless of the language you are translating to"라는 문구를 덧붙여 **예외 없이** YAML front matter의 다른 태그들은 함부로 수정하지 않도록 강조하였다.
{: .prompt-tip }

##### 제공된 원문이 출발언어가 아닌 다른 언어를 포함하는 경우의 처리
한국어로 원문을 작성할 때, 어떤 개념의 정의를 처음 소개하거나 몇몇 전문용어를 사용하는 경우 '*중성자 감쇠 (Neutron Attenuation)*'와 같이 괄호 안에 영문 표현을 같이 기재하는 경우가 종종 있다. 이러한 표현을 번역하는 경우 어떨 땐 괄호를 살리고, 또 어떨 땐 괄호 안에 기재된 영문을 누락하는 등 번역 방식이 일관되지 않은 문제가 있어 아래와 같은 세부 지침을 정하였다.
- 전문용어의 경우,
  - 일본어와 같이 로마자 기반이 아닌 언어로 번역할 때는 '번역 표현(영어 표현)'의 형식을 유지한다.
  - 스페인어, 포르투갈어, 프랑스어와 같은 로마자 기반의 언어로 번역할 때에는 '번역 표현' 단독 표기와 '번역 표현(영어 표현)' 병행 표기를 둘 다 허용하며, Claude가 둘 중 더 적절한 것을 자율적으로 선택하도록 한다.
- 고유명사의 경우, 어떠한 형태로든 원문 철자가 번역 결과물에도 보존되어야 한다.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
  2. it may be a proper noun such as a person's name or a place name. \n\
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
      You can choose whichever you think is more appropriate.</example>\n\
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### 다른 포스트로 연결되는 링크의 처리
몇몇 포스트는 다른 포스트로 연결되는 링크를 포함하는데, 테스트 단계에서 이에 관한 지침을 별도로 제시하지 않았을 때 URL의 경로 부분까지 번역해야 하는 대상으로 해석해서 바꾸는 바람에 내부 링크가 깨지는 문제가 자주 발생하였다. 해당 문제는 프롬프트에 이 구절을 추가하여 해결하였다.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### 번역 결과물만을 응답으로 출력할 것
마지막으로, 응답 시 다른 말을 덧붙이지 않고 오직 번역 결과물만을 출력하도록 다음 문장을 제시한다.

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
“Here is the translation of the text provided, preserving the markdown format:” or something of that nature!!</important>
```

### 추가적인 프롬프트 디자인 기법
다만, 인간에게 작업을 요청할 때와 달리 언어모델의 경우에 특별히 적용되는 추가적인 기법들도 존재한다.
이에 관해서는 웹상에 여러 유용한 자료들이 많지만, 범용적으로 유용하게 활용할 수 있는 몇 가지 대표적인 팁을 정리해 보자면 다음과 같다.  
[Anthropic 공식 문서의 프롬프트 엔지니어링 가이드](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)를 주로 참고하였다.

#### XML 태그를 활용하여 구조화
사실 이는 지금껏 앞에서 이미 사용해 오고 있었다. 여러 맥락과 지시사항, 형식, 예시들을 포함하는 복잡한 프롬프트의 경우 `<instructions>`, `<example>`, `<format>` 등의 XML 태그를 적절히 활용하면 언어모델이 프롬프트를 정확히 해석하고 높은 품질의 의도에 맞는 출력을 내놓는 데 큰 도움이 된다. [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub 리포지터리에 프롬프트 작성 시 유용한 XML 태그들이 잘 정리되어 있으니 참고해보는 것을 추천한다.

#### 단계별 추론 (CoT, chain of thinking) 기법
수학 문제 풀이나 복잡한 문서 작성과 같이 상당한 수준의 추론을 필요로 하는 작업의 경우에, 언어모델이 문제를 단계별로 나누어 생각하도록 유도하면 성능을 크게 끌어올릴 수 있다. 다만 이 경우 응답 지연 시간이 길어질 수 있으며, 모든 작업에 대해 항상 이러한 기법이 유용한 것은 아니므로 주의한다. 

#### 프롬프트 체이닝 (prompt chaining) 기법
복잡한 작업을 수행해야 하는 경우 단일 프롬프트로는 대응에 한계가 있을 수 있다. 이 경우 처음부터 전체 작업 흐름을 여러 단계로 나눠서 단계별로 그에 특화된 프롬프트를 제시하고 앞 단계에서 얻은 응답을 그 다음 단계의 입력으로 전달하는 방식을 사용하는 것도 고려해 볼 수 있다. 이러한 기법을 프롬프트 체이닝(prompt chaining)이라고 한다.

#### 응답 첫 부분 미리 채워 놓기
프롬프트를 입력할 때, 응답할 내용의 첫 부분을 미리 제시하고 그 뒤에 이어질 답변을 작성하도록 함으로써 불필요한 인삿말 등의 서두를 건너뛰게 하거나, XML, JSON과 같은 특정 형식으로 응답하게끔 강제할 수 있다. [Claude API의 경우 호출 시에 `User` 메시지뿐만 아니라 `Assistant` 메시지를 함께 제출하면 이 기법을 사용할 수 있다.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### 게으름 피우기 방지 (2024.10.31. 할로윈 패치)
이 글을 처음 작성한 이후 중간에 한두 차례 약간의 프롬프트 개선 및 지시사항 구체화를 추가로 거치긴 했지만, 어쨌든 4달간 본 자동화 시스템을 적용하면서 별다른 큰 문제는 없었다.

그런데 한국 시각으로 2024.10.31. 저녁 6시경부터, 새로 작성한 포스트의 번역 작업을 맡겼을 때 포스트의 첫 'TL;DR' 부분만을 번역한 후 번역을 임의로 중단하는 이상현상이 지속 발생하였다.

해당 문제의 예상 원인 및 해결 방법에 대해 [별도의 포스트](/posts/does-ai-hate-to-work-on-halloween)로 다루었으니, 해당 글을 참고하기 바란다.

### 완성한 프롬프트
위의 단계를 거친 프롬프트 디자인 결과물은 다음과 같다.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role> The customer's request is as follows:\n\n \
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task> \
In the provided markdown format text, \n\
  - <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
  - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
    1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
    2. it may be a proper noun such as a person's name or a place name. \n\
    After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
    <if>it is the first case, and the target language is not a Roman alphabet-based language, \
    please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
      - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
      - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
    <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
      - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
        You can choose whichever you think is more appropriate.</example>\n\
      - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
        French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
    <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
      - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
        In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
        redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
    </condition>\n\n\
  - <condition><if>the provided text contains links in markdown format, \
    please translate the link text and the fragment part of the URL into {target_lang}, \
    but keep the path part of the URL intact.</if> \n\
    - <example> the German translation of '[중성자 상호작용과 반응단면적]\
      (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
      would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
      #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
“Here is the translation of the text provided, preserving the markdown format:” or something of that nature!!</important>
```

## Further Reading
Continued in [Part 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
