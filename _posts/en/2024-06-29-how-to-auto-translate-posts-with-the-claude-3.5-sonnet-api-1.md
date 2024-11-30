---
title: How to Auto-translate Posts with Claude 3.5 Sonnet API (1) - Prompt Design
description: >-
  This post covers the process of designing prompts for multilingual translation of markdown text files, and automating the task using Python with the API key obtained from Anthropic and the created prompts. This is the first post in the series, introducing the method and process of prompt design.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introduction
I recently adopted Anthropic's Claude 3.5 Sonnet API for multilingual translation of blog posts. In this series, I will discuss why I chose Claude 3.5 Sonnet API, how to design prompts, and how to implement automation through Python script integration with the API.  
The series consists of two posts, and this is the first post in the series.
- Part 1: Introduction to Claude 3.5 Sonnet model and selection rationale, prompt engineering (current post)
- Part 2: [Writing and implementing Python automation scripts using the API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## About Claude 3.5 Sonnet
The Claude 3 series models are available in Haiku, Sonnet, and Opus versions according to model size.  
![Claude 3 model tier classification](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Image source: [Anthropic Claude API official webpage](https://www.anthropic.com/api)

And on June 21, 2024 KST, Anthropic released their latest language model, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). According to Anthropic's announcement, it shows inference performance surpassing Claude 3 Opus at the same cost and speed as the existing Claude 3 Sonnet, and it is generally considered to have advantages over its competitor GPT-4 in writing, language reasoning, multilingual understanding, and translation.  
![Claude 3.5 Sonnet introduction image](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet performance benchmark results](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Image source: [Anthropic homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

(Added on Oct 31, 2024) On October 22, 2024, Anthropic announced an upgraded version API ("claude-3-5-sonnet-20241022") of Claude 3.5 Sonnet and Claude 3.5 Haiku. However, due to the [issue discussed later](#preventing-laziness-october-31-2024-halloween-patch), this blog is still using the existing "claude-3-5-sonnet-20240620" API.

## Why I Adopted Claude 3.5 for Post Translation
Even without language models like Claude 3.5 or GPT-4, there are existing commercial translation APIs like Google Translate or DeepL. Nevertheless, I decided to use an LLM for translation purposes because, unlike other commercial translation services, users can provide additional contextual information or requirements beyond the text through prompt design, such as the purpose of writing and main topics, and the model can provide context-aware translations accordingly. While DeepL and Google Translate generally show excellent translation quality, they have limitations in not fully understanding the subject matter and overall context, resulting in relatively unnatural translation results when asked to translate long texts on specialized topics rather than everyday conversation. In particular, as mentioned above, Claude is generally considered to be relatively superior to its competitor GPT-4 in writing, language reasoning, multilingual understanding and translation, and when I briefly tested it myself, it showed smoother translation quality than GPT-4, so I determined it was suitable for translating engineering-related articles posted on this blog into multiple languages.

## Prompt Design
### Basic Principles When Making Requests
To obtain satisfactory results that meet the purpose from a language model, appropriate prompts must be provided. While prompt design might seem daunting, in fact, 'how to make good requests' isn't much different whether the recipient is a language model or a human, so it's not that difficult when approached from this perspective. It's good to clearly explain the current situation and requests according to the 5W1H principle, and add some specific examples if needed. While there are many tips and techniques for prompt design, most are derived from the basic principles discussed below.

#### Overall Tone
There are many reports that language models output higher quality responses when prompts are written and input in a polite requesting tone rather than a commanding tone. Usually in society, when requesting something from others, the probability of the other person performing the requested task more sincerely increases when making the request in the latter tone rather than the former, and it seems that language models learn and imitate such human response patterns.

#### Role Assignment and Situation Explanation (Who, Why)
First, I assigned Claude 3.5 the role of a *'professional technical translator'* and provided contextual information about the user as an *"engineering blogger who mainly writes about mathematics, physics, and data science"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Conveying Overall Request (What)
Next, I requested to translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while maintaining the format.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> When calling the Claude API, the {source_lang} and {target_lang} placeholders in the prompt are filled with source and target language variables respectively through Python script's f-string functionality.
{: .prompt-info }

#### Requirements Specification and Examples (How)
For simple tasks, the previous steps might be sufficient to get the desired results, but for complex tasks requiring additional explanation may be needed.

When requirements are complex and numerous, listing them with topic sentences rather than fully describing each item improves readability and makes it easier to understand for readers (whether human or language model). Also, providing examples can be helpful if needed.
In this case, the following conditions were added:

##### Handling YAML Front Matter
The YAML front matter located at the beginning of posts written in markdown for uploading to Jekyll blogs records 'title', 'description', 'categories', and 'tags' information. For example, the YAML front matter for this post is as follows:

```yaml
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: >-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

While the title and description tags need to be translated into multiple languages when translating posts, for URL consistency, it's easier for maintenance to leave category and tag names untranslated in English. Therefore, I added the following instruction to prevent translation of tags other than 'title' and 'description':

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> The phrase "under any circumstances, regardless of the language you are translating to" was added to emphasize that other YAML front matter tags should **never** be modified.
{: .prompt-tip }

##### Handling When Provided Original Text Contains Languages Other Than Source Language
When writing original text in Korean, when introducing the definition of a concept or using certain technical terms, there are often cases where English expressions are included in parentheses, such as '*중성자 감쇠 (Neutron Attenuation)*'. When translating such expressions, there was an issue with inconsistent translation methods, sometimes preserving parentheses and other times omitting the English in parentheses, so the following detailed guidelines were established:
- For technical terms:
  - When translating into non-Roman alphabet-based languages like Japanese, maintain the format 'translated expression(English expression)'.
  - When translating into Roman alphabet-based languages like Spanish, Portuguese, or French, both 'translated expression' alone and 'translated expression(English expression)' are allowed, and Claude can autonomously choose whichever is more appropriate.
- For proper nouns, the original spelling must be preserved in the translation output in some form.

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

##### Handling Links to Other Posts
Some posts include links to other posts, and during the testing phase, when no separate guidelines were provided for this, there was a frequent problem of internal links breaking because the path part of the URL was interpreted as something that needed to be translated. This issue was resolved by adding this phrase to the prompt:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Output Translation Results Only
Finally, the following sentence is presented to output only the translation results without adding any other words in the response:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Additional Prompt Design Techniques
However, there are additional techniques that specifically apply to language models, unlike when requesting tasks from humans.
While there are many useful resources about this on the web, here are some representative tips that can be useful universally:  
Mainly referenced [Anthropic's official documentation on prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Structuring Using XML Tags
In fact, this has already been used throughout the previous sections. For complex prompts containing various contexts, instructions, formats, and examples, appropriate use of XML tags like `<instructions>`, `<example>`, `<format>` can greatly help language models accurately interpret prompts and produce high-quality outputs that match intentions. The [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub repository has a good compilation of useful XML tags for writing prompts, so it's recommended to refer to it.

#### Chain of Thinking (CoT) Technique
For tasks requiring significant reasoning, such as solving math problems or creating complex documents, performance can be greatly improved by guiding the language model to think about problems step by step. However, this may lead to longer response delays, and this technique is not always useful for all tasks, so caution is needed.

#### Prompt Chaining Technique
When performing complex tasks, there may be limitations in handling them with a single prompt. In this case, you can consider dividing the entire workflow into multiple steps from the beginning, presenting prompts specialized for each step, and passing the responses obtained from the previous step as input to the next step. This technique is called prompt chaining.

#### Prefilling Response Beginning
When inputting prompts, you can force skipping unnecessary greetings or responding in specific formats like XML or JSON by presenting the first part of the response content in advance and having it continue writing the answer after that. [In the case of Claude API, this technique can be used by submitting both `User` and `Assistant` messages when making API calls.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Preventing Laziness (October 31, 2024 Halloween Patch)
Although there were a couple of minor prompt improvements and specification clarifications after this post was first written, there were no major issues while applying this automation system for 4 months.

However, starting from around 6 PM KST on October 31, 2024, when tasked with translating newly written posts, a persistent anomaly occurred where only the first 'TL;DR' section of posts would be translated before arbitrarily stopping the translation.

The suspected cause of this issue and its solution are covered in [a separate post](/posts/does-ai-hate-to-work-on-halloween), so please refer to that post.

### Completed Prompt
The result of the prompt design through the above steps is as follows:

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
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

## Further Reading
Continued in [Part 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
