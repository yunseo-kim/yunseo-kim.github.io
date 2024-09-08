---
title: How to Auto-Translate Posts with the Claude 3.5 Sonnet API
description: >-
  This post briefly introduces the recently released Claude 3.5 Sonnet model, shares the process of designing prompts to apply it to multilingual translation of blog posts, and presents the resulting prompts.
  It also introduces how to write and utilize a Python script for translation automation using the API key issued by Anthropic and the previously written prompts.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introduction
Recently, I introduced the Claude 3.5 Sonnet API from Anthropic for multilingual translation of blog posts. In this post, I will discuss the reasons for choosing the Claude 3.5 Sonnet API, the method of prompt design, and how to implement API integration and automation through Python scripts.

## About Claude 3.5 Sonnet
The Claude 3 series models are provided in Haiku, Sonnet, and Opus versions according to model size.  
![Claude 3 model tier distinction](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Image source: [Anthropic Claude API official webpage](https://www.anthropic.com/api)

And on June 21, 2024, Korean time, Anthropic released their latest language model, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). According to Anthropic's announcement, it shows inference performance surpassing Claude 3 Opus at the same cost and speed as the existing Claude 3 Sonnet, and it is generally considered to have advantages over its competitor model GPT-4 in the fields of writing, language reasoning, multilingual understanding, and translation.  
![Claude 3.5 Sonnet introduction image](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet performance benchmark results](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Image source: [Anthropic homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

## Reasons for Introducing Claude 3.5 for Post Translation
Even without language models like Claude 3.5 or GPT-4, there are existing commercial translation APIs such as Google Translate or DeepL. Nevertheless, the reason for deciding to use an LLM for translation purposes is that unlike other commercial translation services, users can provide additional contextual information or requirements beyond the main text through prompt design, such as the purpose of writing or main topics, and the model can provide translations considering the context accordingly. Although DeepL and Google Translate generally show excellent translation quality, due to the limitation of not being able to grasp the subject or overall context of the text well, when asked to translate long texts on specialized topics rather than everyday conversations, the translation results were relatively unnatural in some cases. Especially since Claude is said to be relatively superior to its competitor model GPT-4 in the fields of writing, language reasoning, multilingual understanding, and translation as mentioned above, I judged it to be suitable for the task of translating engineering-related articles posted on this blog into multiple languages.

## Prompt Design
### Basic Principles of Prompt Design
To obtain satisfactory results that meet the purpose from a language model, an appropriate prompt must be provided accordingly. Prompt design may seem daunting, but in fact, 'how to request something well' is not much different whether the other party is a language model or a person, so it's not that difficult if approached from this perspective. It's good to clearly explain the current situation and requirements according to the 5W1H principle, and if necessary, add a few specific examples. There are numerous tips and techniques for prompt design, but most are derived from the basic principles mentioned above.

### Role Assignment and Situation Explanation (Who, Why)
First, I assigned Claude 3.5 the role of a *'professional technical translator'* and provided context information about the user as *"an engineering blogger who mainly writes about math, physics, and data science"*.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Conveying Overall Request (What)
Next, I requested to translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while maintaining the format.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> When calling the Claude API, the {source_lang} and {target_lang} in the prompt are replaced with the source language and target language variables respectively through the f-string feature of the Python script.
{: .prompt-info }

### Specifying Requirements and Examples (How)
For simple tasks, the previous steps might be sufficient to get the desired results, but for complex tasks, additional explanations may be needed. In this case, the following conditions were added.

#### Handling YAML Front Matter
The YAML front matter located at the beginning of posts written in markdown for uploading to Jekyll blogs records 'title', 'description', 'categories', and 'tags' information. For example, the YAML front matter for this post is as follows:

```YAML
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

However, when translating posts, while the title and description tags need to be translated into multiple languages, it's more convenient for maintenance to leave the category and tag names in English without translation for consistency in post URLs. Therefore, the following instruction was given to ensure that tags other than 'title' and 'description' are not translated. Since Claude is likely to have already learned about YAML front matter, this level of explanation should be sufficient in most cases.
> In the provided markdown formatted text, do not translate the YAML front matter except for the 'title' and 'description' tags.

#### Handling Cases Where the Provided Original Text Contains Languages Other Than the Source Language
When writing the original text in Korean, when introducing the definition of a concept for the first time or using some technical terms, it's often the case to include the English expression in parentheses, such as '*중성자 감쇠 (Neutron Attenuation)*'. When translating such expressions, there were issues with inconsistent translation methods, sometimes preserving the parentheses and sometimes omitting the English written in parentheses, so the following sentence was added to the prompt.
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Handling Links to Other Posts
Some posts include links to other posts, and there was often a problem where the path part of the URL was interpreted as something that needed to be translated, causing internal links to break. This problem was solved by adding this sentence to the prompt.
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Output Only the Translation Result as a Response
Finally, the following sentence is presented to output only the translation result without adding any other words when responding.
> The output should only contain the translated text.

### Completed Prompt
The result of the prompt design through the above steps is as follows:
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.

## Claude API Integration
### Issuing Claude API Key

> This section explains how to issue a new Claude API key. If you already have an API key to use, you can skip this step.
{: .prompt-tip }

Go to <https://console.anthropic.com> and log in. If you don't have an account yet, you need to sign up first. After logging in, you will see a dashboard screen like the one below.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Clicking the 'Get API keys' button on this screen will show you the following screen.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) I already have a key created, so a key named `yunseo-secret-key` is displayed, but if you've just created an account and haven't issued an API key yet, you probably don't have any keys. You can issue a new key by clicking the 'Create Key' button in the top right.

> When you complete the key issuance, your API key will be displayed on the screen, but this key cannot be checked again later, so be sure to record it separately in a safe place.
{: .prompt-warning }

### (Recommended) Registering Claude API Key in Environment Variables
To use the Claude API in Python or Shell scripts, you need to load the API key. While you can record the API key in the script itself, this method can't be used if you need to upload the script to GitHub or share it with others in other ways. Also, even if you didn't intend to share the script file, there's a risk that the API key could be leaked along with the script file if it's recorded in the script file in case of an unintended mistake leading to the script file being leaked. Therefore, it's recommended to register the API key in the environment variables of the system that only you use, and then load that environment variable in the script. Below, I introduce how to register the API key in system environment variables based on UNIX systems. For Windows, please refer to other articles on the web.

1. In the terminal, run `nano ~/.bashrc` or `nano ~/.zshrc` depending on the type of shell you use to launch the editor.
2. Add `export ANTHROPIC_API_KEY='your-api-key-here'` to the contents of that file. Replace 'your-api-key-here' with your actual API key, and note that it must be wrapped with single quotes.
3. Save the changes and exit the editor.
4. Run `source ~/.bashrc` or `source ~/.zshrc` in the terminal to apply the changes.

### Installing Necessary Python Packages
If the anthropic package is not installed in your Python environment, install it with the following command.
```bash
pip3 install anthropic
```
Also, the following packages are needed to use the post translation script introduced later, so install or update them with the following command.
```bash
pip3 install -U argparse tqdm
```

### Writing Python Scripts
The post translation script introduced in this article consists of 3 Python script files and 1 CSV file.

- `compare_hash.py`: Calculates the SHA256 hash values of the Korean original posts in the `_posts/ko`{: .filepath} directory, compares them with the existing hash values recorded in the `hash.csv` file, and returns a list of file names that have been changed or newly added
- `hash.csv`: A CSV file recording the SHA256 hash values of existing post files
- `prompt.py`: Receives filepath, source_lang, target_lang values, loads the Claude API key value from system environment variables, then calls the API and submits the prompt we wrote earlier as the system prompt and the content of the post to be translated at 'filepath' as the user prompt. Then receives the response (translation result) from the Claude 3.5 Sonnet model and outputs it as a text file at the path `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`: Contains a source_lang string variable and a 'target_langs' list variable, calls the `changed_files()` function in `compare_hash.py` to return the changed_files list variable. If there are changed files, it runs a double loop for all files in the changed_files list and all elements in the target_langs list, and within that loop, calls the `translate(filepath, source_lang, target_lang)` function in `prompt.py` to perform the translation task.

The contents of the completed script files can also be found in the [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) repository on GitHub.

#### compare_hash.py

```python
import os
import hashlib
import csv

def compute_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def load_existing_hashes(csv_path):
    existing_hashes = {}
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 2:
                    existing_hashes[row[0]] = row[1]
    return existing_hashes

def update_hash_csv(csv_path, file_hashes):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files():
    posts_dir = '../_posts/ko/'
    hash_csv_path = './hash.csv'
    
    existing_hashes = load_existing_hashes(hash_csv_path)
    current_hashes = {}
    changed_files = []

    for root, _, files in os.walk(posts_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=posts_dir)
            
            current_hash = compute_file_hash(file_path)
            current_hashes[relative_path] = current_hash
            
            if relative_path in existing_hashes:
                if current_hash != existing_hashes[relative_path]:
                    changed_files.append(relative_path)
            else:
                changed_files.append(relative_path)

    update_hash_csv(hash_csv_path, current_hashes)

    if __name__ == "__main__":
        if changed_files:
            print("Changed files:")
            for file in changed_files:
                print(f"- {file}")
        else:
            print("No files have changed.")

    return changed_files
```

#### prompt.py
As it includes the content of the prompt we wrote earlier and the file content is quite long, I'm replacing it with a link to the source file in the GitHub repository.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In the `prompt.py` file at the above link, `max_tokens` is a variable that specifies the maximum output length separately from the Context window size. When using the Claude API, the size of the Context window that can be input at once is 200k tokens (about 680,000 characters), but separately from that, each model has a set maximum number of output tokens, so it's recommended to check the [Anthropic official documentation](https://docs.anthropic.com/en/docs/about-claude/models) before using the API. The existing Claude 3 series models could output up to a maximum of 4096 tokens, and while this wasn't a problem for most posts when experimenting with this blog's articles, for some longer posts with roughly more than 8000 characters in Korean, there was an issue where the back part of the translation was cut off in some output languages as it exceeded 4096 tokens. In the case of Claude 3.5 Sonnet, the maximum number of output tokens has doubled to 8192, so there were no problems exceeding this maximum number of output tokens in most cases, and in the `prompt.py` of the above GitHub repository, it's set to `max_tokens=8192`.
{: .prompt-tip }

#### translate_changes.py

```python
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

posts_dir = '../_posts/ko/'
source_lang = "Korean"
target_langs = ["English", "Spanish", "Brazilian Portuguese", "Japanese", "French", "German"]

if __name__ == "__main__":
    changed_files = compare_hash.changed_files()
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")

    for file in changed_files:
        print(f"- {file}")
    print("")
    print("*** Translation start! ***")

    for changed_file in changed_files:
        print(f"- Translating {changed_file}")
        filepath = os.path.join(posts_dir, changed_file)
        for target_lang in tqdm(target_langs):
            prompt.translate(filepath, source_lang, target_lang)
```

### How to Use the Python Script
Based on the Jekyll blog, create subdirectories for each [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) language code inside the `/_posts`{: .filepath} directory where the posts are located, such as `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Then, place the Python scripts and CSV file introduced above in the `/tools`{: .filepath} directory, open a terminal at that location, and run the following command.

```bash
python3 translate_changes.py
```

Then the script will run and a screen like the one below will be displayed.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Actual Usage Experience
As described above, I've been using the automatic post translation using the Claude 3.5 API on this blog for about 2 months since its introduction. In most cases, high-quality translations can be obtained without the need for additional human intervention, and after translating and posting in multiple languages, I've confirmed that Organic Search traffic through searches from regions outside of Korea, such as Brazil, Canada, the United States, and France, is actually incoming. In addition to the blog's traffic inflow, there were additional advantages in terms of learning for the writer of the article. Since Claude writes quite smooth text based on English, in the process of reviewing before pushing posts to the GitHub Pages repository, there's an opportunity to check how certain terms or expressions in the Korean original text I wrote can be naturally expressed in English. While this alone may not be sufficient for comprehensive English learning, it seems to be quite advantageous for an undergraduate engineering student in a non-English speaking country like Korea to frequently encounter natural English expressions for not only everyday expressions but also academic expressions and terms, using the text I wrote myself, which is more familiar than any other text, as an example sentence without any additional effort.
