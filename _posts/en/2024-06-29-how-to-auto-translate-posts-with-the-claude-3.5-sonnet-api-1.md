---
title: How to Auto-Translate Posts with Claude 3.5 Sonnet API (1) - Prompt Design
description: This post covers designing prompts for multilingual translation of markdown text files, and automating the process using Python with an API key from Anthropic and the created prompt. This is the first post in the series, introducing prompt design methods and processes.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introduction
I recently adopted Anthropic's Claude 3.5 Sonnet API for multilingual translation of blog posts. In this series, I will discuss the reasons for choosing Claude 3.5 Sonnet API, prompt design methods, and how to implement API integration and automation using Python scripts.
The series consists of two posts, and this is the first post in the series.
- Part 1: Introduction to Claude 3.5 Sonnet model and selection rationale, prompt engineering (current post)
- Part 2: [Writing and applying Python automation scripts using the API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## About Claude 3.5 Sonnet
The Claude 3 series models are available in Haiku, Sonnet, and Opus versions, depending on the model size.
![Claude 3 model tier distinction](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)
> Image source: [Anthropic Claude API official webpage](https://www.anthropic.com/api)

And on June 21, 12024 [Human Era](https://en.wikipedia.org/wiki/Holocene_calendar) (Korean time), Anthropic released their latest language model, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). According to Anthropic's announcement, it shows inference performance surpassing Claude 3 Opus at the same cost and speed as the existing Claude 3 Sonnet, and it is generally considered to have advantages over its competitor model, GPT-4, in writing, language reasoning, multilingual understanding, and translation.
![Claude 3.5 Sonnet introduction image](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)
![Claude 3.5 Sonnet performance benchmark results](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)
> Image source: [Anthropic homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

(Added on Oct 31, 12024) On October 22, 12024, Anthropic announced an upgraded version of the Claude 3.5 Sonnet API ("claude-3-5-sonnet-20241022") and Claude 3.5 Haiku. However, due to [the problem mentioned later](#preventing-laziness-12024-10-31-halloween-patch), this blog is still using the existing "claude-3-5-sonnet-20240620" API.

## Why I Adopted Claude 3.5 for Post Translation
Even without language models like Claude 3.5 or GPT-4, there are existing commercial translation APIs such as Google Translate or DeepL. Nevertheless, I decided to use an LLM for translation purposes because, unlike other commercial translation services, users can provide additional contextual information or requirements beyond the main text through prompt design, such as the purpose of writing or main topics, and the model can provide context-aware translations accordingly. Although DeepL and Google Translate generally show excellent translation quality, they have limitations in not fully grasping the subject or overall context of the text, resulting in relatively unnatural translation results when asked to translate long texts on specialized topics rather than everyday conversations. Especially, as mentioned earlier, Claude is reported to be relatively superior to its competitor model GPT-4 in writing, language reasoning, multilingual understanding, and translation fields, and when I briefly tested it myself, it showed smoother translation quality than GPT-4o. Therefore, I judged it suitable for translating engineering-related articles posted on this blog into multiple languages.

## Prompt Design
### Basic Principles When Making Requests
To obtain satisfactory results that meet the purpose from a language model, an appropriate prompt must be provided. Prompt design might seem daunting, but in fact, 'how to make good requests' is not much different whether the recipient is a language model or a human, so it's not that difficult if approached from this perspective. It's good to clearly explain the current situation and requests according to the 5W1H principle, and if necessary, add a few specific examples. There are numerous tips and techniques for prompt design, but most are derived from the basic principles described below.

#### Overall Tone
There are many reports that language models produce higher quality responses when prompts are written and input in a polite requesting tone rather than an authoritative commanding tone. Usually, in society, when asking someone to do something, the probability of the other person performing the requested task more sincerely is higher when politely requested rather than authoritatively commanded. It seems that language models learn and imitate this response pattern of people.

#### Role Assignment and Situation Explanation (Who, Why)
First, I assigned Claude 3.5 the role of a *'professional technical translator'* and provided contextual information about the user as *"an engineering blogger who mainly writes about mathematics, physics, or data science."*

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

> When calling the Claude API, the {source_lang} and {target_lang} in the prompt are replaced with the source language and target language variables, respectively, through the f-string feature of the Python script.
{: .prompt-info }

#### Specifying Requirements and Examples (How)
For simple tasks, the previous steps might be sufficient to get the desired results, but for complex tasks, additional explanations may be needed.

When requirements are complex and numerous, it's more readable and easier to understand (whether for humans or language models) to list them in a top-down manner rather than describing each item in detail. Also, providing examples if necessary can be helpful.
In this case, the following conditions were added:

##### Handling YAML Front Matter
The YAML front matter located at the beginning of posts written in markdown for uploading to Jekyll blogs records 'title', 'description', 'categories', and 'tags' information. For example, the YAML front matter for this post is as follows:

```yaml
---
title: How to Auto-Translate Posts with Claude 3.5 Sonnet API
description: >-
  This post briefly introduces the recently released Claude 3.5 Sonnet model, shares the process of designing prompts for multilingual translation of blog posts, and the resulting prompt. It also introduces how to write and use Python translation automation scripts using the API key issued by Anthropic and the previously created prompt.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

However, when translating posts, while the title and description tags need to be translated into multiple languages, it's more convenient for maintenance to leave the category and tag names in English without translation for consistency in post URLs. Therefore, the following instruction was added to ensure that tags other than 'title' and 'description' are not translated:

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> The phrase "under any circumstances, regardless of the language you are translating to" was added to emphasize that other tags in the YAML front matter should not be modified **without exception**.
{: .prompt-tip }

##### Handling Cases Where the Provided Original Text Includes Languages Other Than the Source Language
When writing the original text in Korean, there are often cases where English expressions are included in parentheses when introducing the definition of a concept or using certain technical terms, such as '*중성자 감쇠 (Neutron Attenuation)*'. When translating such expressions, there were issues with inconsistent translation methods, sometimes preserving the parentheses and other times omitting the English in parentheses. To address this, the following detailed guidelines were established:
- For technical terms,
  - When translating into languages not based on the Roman alphabet, such as Japanese, maintain the format 'translated expression(English expression)'.
  - When translating into Roman alphabet-based languages like Spanish, Portuguese, or French, both 'translated expression' alone and 'translated expression(English expression)' are allowed, and Claude is allowed to autonomously choose whichever is more appropriate.
- For proper nouns, the original spelling must be preserved in some form in the translation output.

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
Some posts include links to other posts, and during the testing phase, when no separate guidelines were provided for this, there was a frequent problem of internal links breaking because the path part of the URL was interpreted as something that needed to be translated. This issue was resolved by adding the following phrase to the prompt:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Outputting Only the Translation Results as a Response
Finally, the following sentence is presented to output only the translation results without adding any other words in the response:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Additional Prompt Design Techniques
However, there are additional techniques that apply specifically to language models, unlike when requesting tasks from humans.
There are many useful resources on the web about this, but here are some representative tips that can be universally useful:
The [prompt engineering guide in the official Anthropic documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) was mainly referenced.

#### Structuring Using XML Tags
In fact, this has already been used throughout the previous sections. For complex prompts that include various contexts, instructions, formats, and examples, appropriate use of XML tags such as `<instructions>`, `<example>`, `<format>` can greatly help the language model accurately interpret the prompt and produce high-quality, intended outputs. The [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub repository has a well-organized list of useful XML tags for writing prompts, so I recommend referring to it.

#### Chain of Thinking (CoT) Technique
For tasks that require a considerable level of reasoning, such as solving math problems or creating complex documents, guiding the language model to think about the problem step by step can greatly improve performance. However, this may lead to longer response times, and it's important to note that this technique is not always useful for all tasks.

#### Prompt Chaining Technique
When performing complex tasks, there may be limitations in responding with a single prompt. In this case, it's worth considering dividing the entire workflow into multiple steps from the beginning, presenting prompts specialized for each step, and passing the response obtained from the previous step as input to the next step. This technique is called prompt chaining.

#### Prefilling the Beginning of the Response
When inputting a prompt, you can force the model to skip unnecessary greetings or introductions, or force it to respond in a specific format such as XML or JSON, by presenting the first part of the response content in advance and asking it to continue writing the answer after that. [In the case of the Claude API, this technique can be used by submitting an `Assistant` message along with the `User` message when calling.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Preventing Laziness (October 31, 12024 Halloween Patch)
Although I made a couple of minor prompt improvements and specification clarifications after initially writing this post, there were no major issues while applying this automation system for four months.

However, from around 6 PM Korean time on October 31, 12024, when tasked with translating newly written posts, a persistent anomaly occurred where only the first 'TL;DR' part of the post was translated before arbitrarily stopping the translation.

The suspected cause of this issue and its solution are discussed in [a separate post](/posts/does-ai-hate-to-work-on-halloween), so please refer to that post.

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
