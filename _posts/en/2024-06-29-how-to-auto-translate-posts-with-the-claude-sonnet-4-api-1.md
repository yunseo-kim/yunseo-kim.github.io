---
title: How to Auto-Translate Posts with Claude Sonnet 4 API (1) - Prompt Design
description: "Covers the process of designing prompts for multilingual translation of markdown text files and automating the work with Python using API keys from Anthropic and the designed prompts. This post is the first in the series, introducing prompt design methods and processes."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---

## Introduction
Since introducing Anthropic's Claude 3.5 Sonnet API for multilingual translation of blog posts in June 12024, I have been satisfactorily operating this translation system for nearly a year through several improvements to prompts and automation scripts, as well as model version upgrades. In this series, I aim to cover the reasons for choosing the Claude Sonnet model during the introduction process, prompt design methods, and how to implement API integration and automation through Python scripts.  
The series consists of 2 posts, and this post you are reading is the first in the series.
- Part 1: Introduction to Claude Sonnet model and selection reasons, prompt engineering (this post)
- Part 2: [Writing and applying Python automation scripts using the API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## About Claude Sonnet
Claude series models are provided in Haiku, Sonnet, and Opus versions according to model size.  
![Claude 3 model tier classification](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> Image source: [Anthropic Claude API official webpage](https://www.anthropic.com/api)

> (Added 12025.05.29.)  
> The image was captured a year ago, so the token pricing is based on the old Claude 3 version, but the Haiku, Sonnet, Opus classification by model size is still valid. As of the end of May 12025, the pricing for each model provided by Anthropic is as follows.
>
> | Model | Base Input <br>Tokens | 5m Cache <br>Writes | 1h Cache <br>Writes | Cache Hits &<br> Refreshes | Output <br>Tokens |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | Claude Opus 4 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Sonnet 4 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.7 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.5 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Haiku 3.5 | $0.80 / MTok | $1 / MTok | $1.6 / MTok | $0.08 / MTok | $4 / MTok |
> | Claude Opus 3 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Haiku 3 | $0.25 / MTok | $0.30 / MTok | $0.50 / MTok | $0.03 / MTok | $1.25 / MTok |
>
> Source: [Anthropic developer docs](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

And the language model [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) released by Anthropic on June 21, 12024 (Korean time) shows reasoning performance that surpasses Claude 3 Opus at the same cost and speed as the existing Claude 3 Sonnet, and is generally evaluated to have strengths over the competing model GPT-4 in writing, language reasoning, multilingual understanding, and translation.  
![Claude 3.5 Sonnet introduction image](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet performance benchmark results](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> Image source: [Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## Why I Introduced Claude 3.5 for Post Translation
Even without language models like Claude 3.5 or GPT-4, existing commercial translation APIs like Google Translate or DeepL exist. Nevertheless, the reason I decided to use LLM for translation purposes is that unlike other commercial translation services, users can provide additional context information or requirements beyond the main text, such as the writing purpose or main topics of the text through prompt design, and the model can provide contextually appropriate translations accordingly.

While DeepL and Google Translate generally show excellent translation quality, they have limitations in that they cannot well grasp the topic or overall context of the text and cannot convey complex requirements separately. This causes problems when requesting translation of long texts on professional topics rather than everyday conversation, where the translation results are relatively unnatural and it's difficult to output exactly in the required specific format (markdown, YAML frontmatter, etc.).

In particular, as mentioned above, Claude was evaluated to be relatively superior to the competing model GPT-4 in writing, language reasoning, multilingual understanding, and translation, and when I briefly tested it myself, it showed smoother translation quality than GPT-4. Therefore, when considering introduction in June 12024, I judged it suitable for translating engineering-related articles posted on this blog into multiple languages.

## Model Adoption History and Current Status
### 12024.07.01.
As summarized in [a separate post](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/), [I completed the initial work of applying the Polyglot plugin and modifying `_config.yml`{: .filepath}, html headers, and sitemap accordingly.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Subsequently, [I adopted the Claude 3.5 Sonnet model for translation purposes and applied it after completing the initial implementation and verification of the API integration Python script covered in this series.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
On October 22, 12024, Anthropic announced an upgraded version of Claude 3.5 Sonnet API ("claude-3-5-sonnet-20241022") and Claude 3.5 Haiku. However, due to [a problem described later](#preventing-laziness-120241031-halloween-patch), this blog still applies the existing "claude-3-5-sonnet-20240620" API.

### 12025.04.02.
[Switched the applied model from "claude-3-5-sonnet-20240620" to "claude-3-7-sonnet-20250219".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[Switched the applied model from "claude-3-7-sonnet-20250219" to "claude-sonnet-4-20250514".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Claude 4 performance benchmark results](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> Image source: [Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

While there may be differences depending on usage conditions, generally since the Claude 3.7 Sonnet model was released, there's little disagreement that Claude is the most powerful model for coding. Anthropic is also actively promoting superior coding performance compared to competing models from OpenAI, Google, etc. as a major strength of their models, targeting developers as their main customer base. In this Claude Opus 4 and Claude Sonnet 4 announcement, they continue this trend by emphasizing coding performance and targeting developers.

Of course, looking at the published benchmark results, improvements have been made across all areas beyond coding, and for the translation work covered in this post, performance improvements in multilingual Q&A (MMMLU) and mathematical problem-solving (AIME 2025) sections are expected to be particularly effective. From brief testing, I confirmed that Claude Sonnet 4's translation results are superior to the previous model Claude 3.7 Sonnet in terms of natural expression, professionalism, and consistency in terminology usage.

> At this point, at least for translating technically-oriented Korean texts like those covered in this blog into multiple languages, I think Claude models are still the best. However, Google's Gemini models have been noticeably improving recently, and in May this year, they even released the Gemini 2.5 model, though it's still in Preview stage.  
> When comparing Gemini 2.0 Flash model with Claude 3.7 Sonnet and Claude Sonnet 4 models, I judged Claude's translation performance to be superior, but Gemini's multilingual performance is also quite excellent, and its mathematical and physics problem-solving and description abilities are actually better than even Claude Opus 4 in Gemini 2.5 Preview 05-06. So I can't guarantee what it will be like when that model is officially released and compared again.  
> Considering the somewhat cheaper API fees compared to Claude, Gemini has much better price competitiveness, so even with somewhat comparable performance, Gemini could be a reasonable alternative. Since Gemini 2.5 is still in Preview stage, I judge it too early to apply to actual automation and am not considering it for now, but I plan to test it when the stable version is released.
{: .prompt-tip }

## Prompt Design
### Basic Principles When Requesting Something
To get satisfactory results that meet your purpose from a language model, you need to provide appropriate prompts. Prompt design might seem daunting, but actually 'how to request something well' isn't very different whether the counterpart is a language model or a person, so approaching it from this perspective isn't too difficult. Clearly explain the current situation and requests according to the five W's and one H, and if necessary, add some specific examples. There are numerous tips and techniques for prompt design, but most are derived from the basic principles described below.

#### Overall Tone
There are many reports that when prompts are written and input in a polite requesting tone rather than a commanding tone, language models output higher quality responses. Usually in society, when requesting something from others, politely asking rather than commanding increases the probability that the other person will perform the requested task more sincerely, and language models seem to learn and imitate such human response patterns.

#### Role Assignment and Context Explanation (Who, Why)
First, I assigned Claude 4 the role of *'professional technical translator'* and provided context information about the user as *"an engineering blogger who writes mainly about math, physics, and data science"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Conveying Overall Request (What)
Next, I requested translation of the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> When calling the Claude API, the {source_lang} and {target_lang} placeholders in the prompt are replaced with the source and target language variables through Python's f-string functionality.
{: .prompt-info }

#### Specifying Requirements and Examples (How)
For simple tasks, the previous steps might be sufficient to get desired results, but for complex tasks, additional explanation may be needed.

When requirements are complex and numerous, listing them systematically rather than describing each item in detail improves readability and makes it easier to understand for the reader (whether human or language model). Also, providing examples when necessary is helpful.
In this case, I added the following conditions:

##### YAML Front Matter Processing
The YAML front matter located at the beginning of posts written in markdown for uploading to Jekyll blogs records 'title', 'description', 'categories', and 'tags' information. For example, the YAML front matter of this current post is as follows:

```yaml
---
title: How to Auto-Translate Posts with Claude Sonnet 4 API (1) - Prompt Design
description: >-
  Covers the process of designing prompts for multilingual translation of markdown text files 
  and automating the work with Python using API keys from Anthropic and the designed prompts. 
  This post is the first in the series, introducing prompt design methods and processes.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

However, when translating posts, while the title and description tags should be translated into multiple languages, for URL consistency, it's better for maintenance to leave category and tag names in English without translation. Therefore, I gave the following instruction to not translate tags other than 'title' and 'description'. Since Claude would already know about YAML front matter from its training, this level of explanation is usually sufficient.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> I added the phrase "under any circumstances, regardless of the language you are translating to" to emphasize **without exception** not to arbitrarily modify other tags in the YAML front matter.
{: .prompt-tip }

(Updated 12025.04.02.)  
Also, I instructed to write the description tag content in appropriate length considering SEO as follows:

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Handling Cases Where the Provided Original Text Contains Languages Other Than the Source Language
When writing original text in Korean, when first introducing the definition of a concept or using certain technical terms, I often include English expressions in parentheses like '*neutron attenuation (Neutron Attenuation)*'. When translating such expressions, there was a problem of inconsistent translation methods - sometimes keeping the parentheses and sometimes omitting the English in parentheses. So I established the following detailed guidelines:
- For technical terms,
  - When translating to non-Roman alphabet languages like Japanese, maintain the format 'translated expression (English expression)'.
  - When translating to Roman alphabet-based languages like Spanish, Portuguese, French, allow both 'translated expression' alone and 'translated expression (English expression)' together, letting Claude autonomously choose the more appropriate one.
- For proper nouns, the original spelling must be preserved in the translation result in some form.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases.
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it.
  2. it may be a proper noun such as a person's name or a place name.
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language,
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'.
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Handling Links to Other Posts
Some posts contain links to other posts, and during the testing phase, when no separate guidelines were provided for this, it often interpreted the URL path part as something that should be translated and changed it, causing internal links to break. This problem was solved by adding this clause to the prompt:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(Updated 12025.04.06.)  
While providing the above guidelines significantly reduces the frequency of broken links by correctly handling the path parts of links during translation, for links containing fragment identifiers, there was still a fundamental limitation where the language model had to roughly guess and fill in the fragment identifier part without knowing the content of the target post. To solve this fundamental problem, I improved the Python script and prompt to provide context information about other posts linked to in the `<reference_context>` XML tag of the user prompt and handle link translation according to that context. After applying this update, most link breaking problems could be prevented, and for closely connected series posts, it became possible to expect more consistent translation across multiple posts.

The following guideline is presented in the system prompt:
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

And the `<reference_context>` part of the user prompt is composed of the following format and content, provided additionally after the content of the main text to be translated:
```xml
<reference_context>
The following are contents of posts linked with hash fragments in the original post. 
Use these for context when translating links and references:

<referenced_post path="{post_1_path}" hash="{hash_fragment_1}">
{post_content}
</referenced_post>

<referenced_post path="{post__2_path}" hash="{hash_fragment_2}">
{post_content}
</referenced_post>

...

</reference_context>
```

> For how this was specifically implemented, refer to [Part 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) of this series and the [Python script](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) content in the GitHub repository.
{: .prompt-tip }

##### Output Only Translation Results as Response
Finally, I present the following sentence to output only the translation results without adding other words in the response:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Additional Prompt Design Techniques
However, unlike when requesting work from humans, there are additional techniques that apply specifically to language models.
While there are many useful resources on the web about this, here are some representative tips that can be universally useful:  
I mainly referenced [Anthropic's official prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Structuring Using XML Tags
Actually, this has been used throughout the previous sections. For complex prompts containing multiple contexts, instructions, formats, and examples, appropriately using XML tags like `<instructions>`, `<example>`, `<format>` helps language models accurately interpret prompts and produce high-quality outputs that meet intentions. The [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub repository has useful XML tags for prompt writing well organized, so I recommend checking it out.

#### Chain of Thinking (CoT) Technique
For tasks requiring significant reasoning like mathematical problem solving or complex document writing, inducing language models to think about problems step by step can greatly improve performance. However, this may increase response latency, and such techniques are not always useful for all tasks, so be careful.

#### Prompt Chaining Technique
When complex tasks need to be performed, there may be limitations in handling them with a single prompt. In this case, you can consider dividing the entire workflow into multiple steps from the beginning, presenting prompts specialized for each step, and passing responses from previous steps as input to the next step. This technique is called prompt chaining.

#### Prefilling Response Beginnings
When inputting prompts, by presenting the beginning part of the response content in advance and having it write the answer that follows, you can skip unnecessary greetings and other preambles, or force responses in specific formats like XML or JSON. [For Claude API, this technique can be used by submitting both `User` and `Assistant` messages together when calling.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Preventing Laziness (12024.10.31. Halloween Patch)
After initially writing this post, I went through one or two additional prompt improvements and instruction specifications, but anyway, there were no major problems while applying this automation system for 4 months.

However, starting around 6 PM Korean time on 12024.10.31., when I assigned translation work for newly written posts, an abnormal phenomenon persisted where it would only translate the first 'TL;DR' part of the post and then arbitrarily stop translation.

I covered the suspected causes and solutions for this problem in [a separate post](/posts/does-ai-hate-to-work-on-halloween), so please refer to that post.

### Completed System Prompt
The prompt design result from the above steps can be found in [the next part](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2).

## Further Reading
Continued in [Part 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
