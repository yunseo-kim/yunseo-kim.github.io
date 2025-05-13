---
title: How to Auto-Translate Posts with Claude 3.5 Sonnet API (1) - Prompt Design
description: This post covers designing prompts for multilingual translation of markdown text files, and automating the process with Python using an API key from Anthropic and the designed prompt. This is the first post in the series, introducing prompt design methods and processes.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introduction
I recently adopted Anthropic's Claude 3.5 Sonnet API for multilingual translation of blog posts. In this series, I'll cover why I chose Claude 3.5 Sonnet API, how to design effective prompts, and how to implement automation through Python scripts and API integration.  
The series consists of two posts, and this is the first one.
- Part 1: Introduction to Claude 3.5 Sonnet model, Reasons for Selection, and Prompt Engineering (this post)
- Part 2: [Writing and Applying Python Automation Scripts Using the API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## About Claude 3.5 Sonnet
The Claude 3 series models are available in Haiku, Sonnet, and Opus versions, based on model size.  
![Claude 3 model tier classification](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Image source: [Anthropic Claude API official webpage](https://www.anthropic.com/api)

On June 21, 12024 ([Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar)) Korean time, Anthropic released their latest language model, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). According to Anthropic, it delivers reasoning performance that surpasses Claude 3 Opus at the same cost and speed as Claude 3 Sonnet, and is generally considered to have advantages over its competitor GPT-4 in writing, language reasoning, multilingual understanding, and translation.  
![Claude 3.5 Sonnet introduction image](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet performance benchmark results](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Image source: [Anthropic homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

(Added 12024.10.31.) On October 22, 12024, Anthropic announced an upgraded version of Claude 3.5 Sonnet API ("claude-3-5-sonnet-20241022") and Claude 3.5 Haiku. However, due to the [issue described later](#preventing-laziness-120241031-halloween-patch), this blog is still using the original "claude-3-5-sonnet-20240620" API.

## Why I Adopted Claude 3.5 for Post Translation
Even without language models like Claude 3.5 or GPT-4, there are existing commercial translation APIs like Google Translate or DeepL. I decided to use an LLM for translation because, unlike other commercial translation services, users can provide additional contextual information or requirements through prompt design, such as the purpose of the writing or main topics, and the model can provide context-aware translations accordingly. While DeepL and Google Translate generally provide excellent translation quality, they have limitations in understanding the subject or overall context of the text, which can result in relatively unnatural translations when asked to translate long texts on specialized topics. As mentioned earlier, Claude is reportedly superior to its competitor GPT-4 in writing, language reasoning, multilingual understanding, and translation, and in my simple tests, it showed smoother translation quality than GPT-4o, making it suitable for translating engineering-related posts on this blog into multiple languages.

## Prompt Design
### Basic Principles for Making Requests
To get satisfactory results from a language model that meet your purpose, you need to provide an appropriate prompt. Prompt design might seem daunting, but the principles of "how to make good requests" aren't that different whether you're asking a language model or a person. Approaching it from this perspective makes it less difficult. Clearly explain the current situation and requirements according to the 5W1H method, and add specific examples if necessary. While there are numerous tips and techniques for prompt design, most derive from the basic principles described below.

#### Overall Tone
Many reports suggest that language models produce higher quality responses when prompts are written in a polite, requesting tone rather than a commanding one. In normal social interactions, people are more likely to perform tasks diligently when asked politely rather than commanded imperiously. Language models seem to mimic this human response pattern through their training.

#### Role Assignment and Context Explanation (Who, Why)
First, I assigned Claude 3.5 the role of a *'professional technical translator'* and provided contextual information about the user as an *"engineering blogger who mainly writes about mathematics, physics, and data science."*

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Communicating the Overall Request (What)
Next, I requested that the markdown-formatted text provided by the user be translated from {source_lang} to {target_lang} while preserving the format.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> When calling the Claude API, the {source_lang} and {target_lang} placeholders in the prompt are replaced with the source and target language variables through Python's f-string functionality.
{: .prompt-info }

#### Specifying Requirements and Examples (How)
For simple tasks, the previous steps might be sufficient to get the desired results, but complex tasks may require additional explanation.

When requirements are complex and numerous, listing them in a top-down approach improves readability and makes them easier to understand (for both humans and language models) compared to describing each item in detail. Providing examples can also be helpful.
In this case, I added the following conditions:

##### Handling YAML Front Matter
The YAML front matter at the beginning of a markdown post for a Jekyll blog contains 'title', 'description', 'categories', and 'tags' information. For example, the YAML front matter for this post is:

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

When translating posts, the title and description tags should be translated into multiple languages, but for URL consistency, category and tag names should remain in English for easier maintenance. I added the following instruction to ensure that only 'title' and 'description' are translated:

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> I emphasized that the other tags in the YAML front matter should not be modified **under any circumstances** by adding the phrase "under any circumstances, regardless of the language you are translating to."
{: .prompt-tip }

##### Handling Content in Languages Other Than the Source Language
When writing original content in Korean, I often include English expressions in parentheses when introducing concept definitions or using technical terms, such as '*중성자 감쇠 (Neutron Attenuation)*'. When translating such expressions, there were inconsistencies in whether to keep the parentheses or omit the English in parentheses, so I established the following detailed guidelines:
- For technical terms:
  - When translating to non-Roman alphabet-based languages like Japanese, maintain the 'translated expression(English expression)' format.
  - When translating to Roman alphabet-based languages like Spanish, Portuguese, or French, both 'translated expression' alone and 'translated expression(English expression)' are acceptable, allowing Claude to autonomously choose the more appropriate option.
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
Some posts include links to other posts, and during testing, without specific guidelines, the model often interpreted the path part of URLs as something to be translated, breaking internal links. I resolved this issue by adding this clause to the prompt:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Outputting Only Translation Results
Finally, I instructed the model to output only the translation results without any additional text:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Additional Prompt Design Techniques
Unlike when requesting tasks from humans, there are additional techniques that apply specifically to language models.
While there are many useful resources on this topic online, here are some generally useful tips:  
I mainly referenced [Anthropic's official prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Structuring with XML Tags
I've already been using this technique throughout. For complex prompts containing various contexts, instructions, formats, and examples, appropriate use of XML tags like `<instructions>`, `<example>`, and `<format>` helps the language model interpret the prompt accurately and produce high-quality, intended outputs. The [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub repository has a good collection of useful XML tags for prompt writing.

#### Chain of Thought (CoT) Technique
For tasks requiring significant reasoning, such as solving math problems or creating complex documents, guiding the language model to break down the problem into steps can greatly improve performance. However, this may increase response time, and this technique isn't always useful for all tasks.

#### Prompt Chaining Technique
For complex tasks, a single prompt might be limiting. In such cases, consider dividing the entire workflow into multiple stages, providing specialized prompts for each stage, and using the response from one stage as input for the next. This technique is called prompt chaining.

#### Prefilling the Beginning of the Response
When inputting a prompt, you can provide the beginning of the response and have the model continue from there, allowing you to skip unnecessary greetings or force responses in specific formats like XML or JSON. [With the Claude API, you can use this technique by submitting an `Assistant` message along with the `User` message when making the API call.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Preventing Laziness (12024.10.31. Halloween Patch)
After initially writing this post, I made a few minor prompt improvements and clarifications, but the automation system worked without major issues for four months.

However, starting around 6 PM Korean time on 12024.10.31, when I assigned translation tasks for newly written posts, the model consistently exhibited abnormal behavior - translating only the first 'TL;DR' section of the post before arbitrarily stopping the translation.

I've covered the suspected causes and solutions for this issue in [a separate post](/posts/does-ai-hate-to-work-on-halloween), so please refer to that post for details.

### The Completed Prompt
The result of the prompt design process described above is as follows:

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
