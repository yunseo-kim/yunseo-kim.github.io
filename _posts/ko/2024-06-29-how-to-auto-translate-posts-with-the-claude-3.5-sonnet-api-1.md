---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법 (1)
description: >-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## 들어가며
최근에 블로그 포스트의 다국어 번역을 위해 Anthropic의 Claude 3.5 Sonnet API를 도입하였다. 이에 도입 과정에서 Claude 3.5 Sonnet API를 선택한 이유와 프롬프트 디자인 방법, 그리고 Python 스크립트를 통한 API 연동 및 자동화 구현 방법을 다루고자 한다. 글에서 다루고자 하는 내용이 꽤 방대한 관계로 하나의 포스트가 아닌 시리즈가 될 예정이며, 이 글은 시리즈의 첫 번째 글이다.

## About Claude 3.5 Sonnet
Claude 3 시리즈 모델은 모델 크기에 따라 Haiku, Sonnet, 그리고 Opus 버전이 제공된다.  
![Claude 3 모델 티어 구분](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 이미지 출처: [Anthropic Claude API 공식 웹페이지](https://www.anthropic.com/api)

그리고 한국 시각으로 2024년 6월 21일, Anthropic에서 최신 언어모델인 [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)를 공개하였다. Anthropic의 발표에 의하면 기존의 Claude 3 Sonnet와 동일한 비용과 속도로 Claude 3 Opus를 능가하는 추론 성능을 보인다고 하며, 대체로 작문과 언어 추론, 다국어 이해 및 번역 분야에서 경쟁 모델인 GPT-4 대비 강점을 보인다는 평이 지배적이다.  
![Claude 3.5 Sonnet 소개 이미지](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet 성능 벤치마크 결과](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 이미지 출처: [Anthropic 홈페이지](https://www.anthropic.com/news/claude-3-5-sonnet)

## 포스트 번역을 위해 Claude 3.5를 도입한 이유
굳이 Claude 3.5나 GPT-4와 같은 언어모델이 아니더라도 구글 번역이나 DeepL과 같은 기존의 상용 번역 API가 존재한다. 그럼에도 번역 목적으로 LLM을 사용하기로 결정한 이유는 다른 상용 번역 서비스와 달리 사용자가 프롬프트 디자인을 통해 모델에게 글의 작성 목적이나 주요 주제 등 본문 외에도 추가적인 맥락 정보나 요구사항을 제공할 수 있고, 모델은 이에 맞추어 문맥을 고려한 번역을 제공할 수 있기 때문이다. DeepL이나 구글 번역도 대체로 뛰어난 번역 품질을 보이는 편이지만, 글의 주제나 전체적인 맥락을 잘 파악하지 못하는 한계 때문에 일상적인 회화가 아닌 전문적인 주제의 긴 글을 번역하도록 요청했을 때는 상대적으로 번역 결과물이 부자연스러운 경우가 있었다. 특히나 Claude는 상술하였듯 경쟁 모델인 GPT-4 대비 작문, 언어 추론, 다국어 이해 및 번역 분야에서 상대적으로 더 뛰어나다는 평이 많기에, 이 블로그에 기재하는 공학 관련 글들을 여러 언어로 번역하는 작업에 적합하다고 판단하였다.

## 프롬프트 디자인
### 프롬프트 디자인의 기본 원칙
언어모델로부터 목적에 부합하는 만족스러운 결과물을 얻기 위해서는 그에 맞는 적절한 프롬프트를 제공해야 한다. 프롬프트 디자인이라고 하면 뭔가 막막하게 느껴질 수 있지만, 사실 '뭔가를 잘 요청하는 방법'이란 상대방이 언어모델이든 사람이든 크게 다르지 않으므로 이와 같은 관점에서 접근하면 별로 어렵지 않다. 육하원칙에 따라 현 상황 및 요청사항을 명확히 설명하고, 필요하다면 몇 가지 구체적인 예시를 덧붙이는 것도 좋다. 프롬프트 디자인에 관한 수많은 팁과 기법들이 존재하지만, 대부분은 상술한 기본 원칙에서 파생되는 것들이다.

### 역할 부여 및 상황 설명(누가, 왜)
제일 먼저 Claude 3.5에게 *'기술 분야 전문 번역가(professional technical translator)'* 라는 역할을 부여하고, *"주로 수학이나 물리학, 데이터 과학에 관한 글을 기고하는 공학 블로거"* 라는 사용자에 관한 맥락 정보를 제공하였다.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### 큰 틀에서의 요청사항 전달(무엇을)
다음으로, 사용자로부터 제공된 마크다운 형식의 글을 {source_lang}에서 {target_lang}으로 형식을 유지하면서 번역하도록 요청하였다. 
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Claude API 호출 시, 프롬프트의 {source_lang}과 {target_lang} 자리에는 Python 스크립트의 f-string 기능을 통해 번역 출발언어와 도착언어 변수가 각각 들어간다.
{: .prompt-info }

### 요구사항 구체화 및 예시(어떻게)
앞선 단계까지만 해도 충분히 원하는 결과를 얻는 경우도 있지만, 복잡한 작업을 요구하는 경우에는 추가적인 설명이 필요할 수 있다. 이 경우에는 다음과 같은 조건을 추가하였다.

#### 제공된 원문이 출발언어가 아닌 다른 언어를 포함하는 경우의 처리
한국어로 원문을 작성할 때, 어떤 개념의 정의를 처음 소개하거나 몇몇 전문용어를 사용하는 경우 '*중성자 감쇠 (Neutron Attenuation)*'와 같이 괄호 안에 영문 표현을 같이 기재하는 경우가 종종 있다. 이러한 표현을 번역하는 경우 어떨 땐 괄호를 살리고, 또 어떨 땐 괄호 안에 기재된 영문을 누락하는 등 번역 방식이 일관되지 않은 문제가 있어 아래 문장을 프롬프트에 추가하였다.
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### 다른 포스트로 연결되는 링크의 처리
몇몇 포스트는 다른 포스트로 연결되는 링크를 포함하는데, URL의 경로 부분까지 번역해야 하는 대상으로 해석해서 바꾸는 바람에 내부 링크가 깨지는 문제가 자주 발생하였다. 해당 문제는 프롬프트에 이 문장을 추가하여 해결하였다.
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### 번역 결과물만을 응답으로 출력할 것
마지막으로, 응답 시 다른 말을 덧붙이지 않고 오직 번역 결과물만을 출력하도록 다음 문장을 제시한다.
> The output should only contain the translated text.

### 완성한 프롬프트
위의 단계를 거친 프롬프트 디자인 결과물은 다음과 같다.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.