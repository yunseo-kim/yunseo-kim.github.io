---
title: How to Automatically Translate Posts with Claude 3.5 Sonnet API (1)
description: >-
  Briefly introduce the recently released Claude 3.5 Sonnet model, and share the process of designing prompts to apply it to multilingual translation of blog posts, along with the completed prompt results.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introduction
Recently, I introduced the Claude 3.5 Sonnet API from Anthropic for multilingual translation of blog posts. In this regard, I would like to cover the reasons for choosing the Claude 3.5 Sonnet API, the method of prompt design, and the implementation of API integration and automation through Python scripts. As the content I want to cover is quite extensive, it will be a series rather than a single post, and this is the first post in the series.

## About Claude 3.5 Sonnet
The Claude 3 series models are provided in Haiku, Sonnet, and Opus versions according to model size.  
![Claude 3 model tier distinction](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Image source: [Anthropic Claude API official webpage](https://www.anthropic.com/api)

And on June 21, 2024, Korean time, Anthropic released their latest language model, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). According to Anthropic's announcement, it shows inference performance surpassing Claude 3 Opus at the same cost and speed as the existing Claude 3 Sonnet, and it is generally considered to have advantages over its competitor model GPT-4 in the fields of writing, language reasoning, multilingual understanding, and translation.  
![Claude 3.5 Sonnet introduction image](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet performance benchmark results](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Image source: [Anthropic homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

## Reasons for Introducing Claude 3.5 for Post Translation
Even without language models like Claude 3.5 or GPT-4, there are existing commercial translation APIs such as Google Translate or DeepL. Nevertheless, the reason for deciding to use LLM for translation purposes is that unlike other commercial translation services, users can provide additional contextual information or requirements beyond the main text, such as the purpose of writing or main topics, through prompt design, and the model can provide context-aware translations accordingly. Although DeepL and Google Translate generally show excellent translation quality, due to the limitation of not fully grasping the subject or overall context of the text, when asked to translate long texts on specialized topics rather than everyday conversations, the translation results were relatively unnatural in some cases. Especially since Claude is said to be relatively superior to its competitor model GPT-4 in the fields of writing, language reasoning, multilingual understanding, and translation as mentioned above, I judged it to be suitable for the task of translating engineering-related articles posted on this blog into multiple languages.

## Prompt Design
### Basic Principles of Prompt Design
To obtain satisfactory results that meet the purpose from a language model, an appropriate prompt must be provided accordingly. While prompt design may seem daunting, in fact, the method of 'asking for something well' is not much different whether the other party is a language model or a person, so it's not that difficult if approached from this perspective. It's good to clearly explain the current situation and requirements according to the 5W1H principle, and if necessary, add a few specific examples. There are numerous tips and techniques for prompt design, but most are derived from the basic principles mentioned above.

### Role Assignment and Situation Explanation (Who, Why)
First, I assigned Claude 3.5 the role of a 'professional technical translator' and provided contextual information about the user as "an engineering blogger who mainly writes about math, physics, and data science."
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Conveying Overall Request (What)
Next, I requested to translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> When calling the Claude API, the {source_lang} and {target_lang} in the prompt are replaced with the source language and target language variables respectively through the f-string feature of the Python script.
{: .prompt-info }

### Specifying Requirements and Examples (How)
While the previous steps might be sufficient to get the desired results in some cases, additional explanations may be needed for complex tasks. In this case, the following conditions were added:

#### Handling when the provided original text includes languages other than the source language
When writing the original text in Korean, when introducing the definition of a concept for the first time or using some technical terms, it's often written with the English expression in parentheses, like '중성자 감쇠 (Neutron Attenuation)'. When translating such expressions, there was a problem of inconsistent translation methods, sometimes preserving the parentheses and sometimes omitting the English in parentheses, so the following sentence was added to the prompt.
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Handling links to other posts
Some posts include links to other posts, and there was a frequent problem of internal links breaking because the path part of the URL was interpreted as something to be translated and changed. This problem was solved by adding this sentence to the prompt.
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Output only the translation result as a response
Finally, the following sentence is presented to output only the translation result without adding any other words when responding.
> The output should only contain the translated text.

### Completed Prompt
The result of the prompt design through the above steps is as follows:
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.
