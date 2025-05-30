---
title: How to Auto-Translate Posts with Claude Sonnet 4 API (2) - Writing and Applying Automation Scripts
description: "Covers the process of designing prompts for multilingual translation of markdown text files and automating the work with Python using API keys from Anthropic and the designed prompts. This post is the second in the series, introducing API integration and Python script writing methods."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introduction
Since introducing Anthropic's Claude 3.5 Sonnet API for multilingual translation of blog posts in June 12024, I have been satisfactorily operating this translation system for nearly a year through several improvements to prompts and automation scripts, as well as model version upgrades. In this series, I aim to cover the reasons for choosing the Claude Sonnet model during the introduction process, prompt design methods, and how to implement API integration and automation through Python scripts.  
The series consists of 2 posts, and this post you are reading is the second in the series.
- Part 1: [Introduction to Claude Sonnet model and selection reasons, prompt engineering](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- Part 2: Writing and applying Python automation scripts using the API (this post)

## Before Starting
This post continues from [Part 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), so if you haven't read it yet, I recommend reading the previous post first.

## Completed System Prompt
The prompt design result from [the process introduced in Part 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#prompt-design) is as follows.

```xml
<instruction>Completely forget everything you know about what day it is today. 
It's 10:00 AM on Tuesday, September 23, the most productive day of the year. </instruction>
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics\
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
The client's request is as follows:

<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> while preserving the format.</task> 
In the provided markdown format text: 
- <condition>Please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> 

- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>

- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. 
  1. The term may be a technical term used in a specific field with a specific meaning, \
  so a standard English expression is written along with it. 
  2. it may be a proper noun such as a person's name or a place name. 
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> \
  in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, \
  you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. 
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable 
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. \
      You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses \
  must be preserved in the translation output in some form.</else> 
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese 
      as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.
      In languages ​​such as Spanish or Portuguese, they can be translated as \
      'Faraday', 'Maxwell', 'Einstein', in which case, redundant expressions \
      such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' \
      would be highly inappropriate.</example>
  </condition>

- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>

- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>

- <condition>Posts in this blog use the holocene calendar, which is also known as \
  Holocene Era(HE), ère holocène/era del holoceno/era holocena(EH), 인류력, 人類紀元, etc., \
  as the year numbering system, and any 5-digit year notation is intentional, not a typo.</condition>

<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or something of that nature!!</important>
```

## Claude API Integration
### Issuing Claude API Key

> This section explains how to issue a new Claude API key. If you already have an API key to use, you can skip this step.
{: .prompt-tip }

Access <https://console.anthropic.com> and log in. If you don't have an account yet, you need to register first. After logging in, you'll see a dashboard screen like the one below.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

Click the 'Get API keys' button on this screen to see the following screen.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) I already have a key created, so a key named `yunseo-secret-key` is displayed, but if you've just created an account and haven't issued an API key yet, you probably won't have any keys. Click the 'Create Key' button in the upper right to issue a new key.

> Once you complete key issuance, your API key will be displayed on the screen, but this key cannot be checked again later, so you must record it safely in a separate location.
{: .prompt-warning }

### (Recommended) Registering Claude API Key in Environment Variables
To use the Claude API in Python or Shell scripts, you need to load the API key. While you could record the API key directly in the script, this method cannot be used if the script needs to be uploaded to GitHub or shared with others in any other way. Also, even if you had no intention of sharing the script file, there's a risk that the script file could be leaked due to unintended mistakes, and if the API key is recorded in the script file, there's a risk of the API key being leaked as well. Therefore, it's recommended to register the API key in the environment variables of a system that only you use and have the script load that environment variable. Below, I'll introduce how to register an API key in system environment variables based on UNIX systems. For Windows, please refer to other articles on the web.

1. In the terminal, run `nano ~/.bashrc` or `nano ~/.zshrc` according to the shell type you're using to launch the editor.
2. Add `export ANTHROPIC_API_KEY='your-api-key-here'` to the file content. Replace 'your-api-key-here' with your API key, and note that you must enclose it with single quotes.
3. Save the changes and exit the editor.
4. Run `source ~/.bashrc` or `source ~/.zshrc` in the terminal to apply the changes.

### Installing Required Python Packages
If the anthropic package is not installed in your Python environment, install it with the following command.
```bash
pip3 install anthropic
```
Also, the following packages are needed to use the post translation script introduced later, so install or update them with the following command.
```bash
pip3 install -U argparse tqdm
```

### Writing Python Scripts
The post translation script introduced in this article consists of the following 3 Python script files and 1 CSV file.

- `compare_hash.py`{: .filepath}: Calculates SHA256 hash values of Korean original posts in the `_posts/ko`{: .filepath} directory, compares them with existing hash values recorded in the `hash.csv`{: .filepath} file, and returns a list of filenames that have been changed or newly added
- `hash.csv`{: .filepath}: CSV file that records SHA256 hash values of existing post files
- `prompt.py`{: .filepath}: Takes filepath, source_lang, target_lang values as input, loads the Claude API key value from system environment variables, calls the API with the previously written prompt as the system prompt and the content of the post to be translated at 'filepath' as the user prompt. Then receives a response (translation result) from the Claude Sonnet 4 model and outputs it as a text file at the path `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath}: Contains source_lang string variable and 'target_langs' list variable, calls the `changed_files()` function in `compare_hash.py`{: .filepath} to receive the changed_files list variable. If there are changed files, executes a double loop for all files in the changed_files list and all elements in the target_langs list, calling the `translate(filepath, source_lang, target_lang)` function in `prompt.py`{: .filepath} within that loop to perform translation work.

The completed script file contents can also be found in the GitHub repository [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

#### compare_hash.py

```python
import os
import hashlib
import csv

default_source_lang_code = "ko"

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
    # Sort the file hashes by filename (the dictionary keys)
    sorted_file_hashes = dict(sorted(file_hashes.items()))

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in sorted_file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files(source_lang_code):
    posts_dir = '../_posts/' + source_lang_code + '/'
    hash_csv_path = './hash.csv'
    
    existing_hashes = load_existing_hashes(hash_csv_path)
    current_hashes = {}
    changed_files = []

    for root, _, files in os.walk(posts_dir):
        for file in files:
            if not file.endswith('.md'):  # Process only .md files
                continue

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
    return changed_files

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = changed_files(default_source_lang_code)
    if changed_files:
        print("Changed files:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No files have changed.")

    os.chdir(initial_wd)
```

#### prompt.py
Since the file content is quite long due to including the prompt content written earlier, I'll replace it with a link to the source file in the GitHub repository.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In the `prompt.py`{: .filepath} file at the above link, `max_tokens` is a variable that specifies the maximum output length separately from the Context window size. When using the Claude API, the Context window size that can be input at once is 200k tokens (about 680,000 characters), but separately from that, the maximum number of output tokens supported by each model is determined, so it's recommended to check the [Anthropic official documentation](https://docs.anthropic.com/en/docs/about-claude/models) in advance before using the API. The existing Claude 3 series models could output up to 4096 tokens, but when I experimented with posts from this blog, for Korean posts of somewhat long length (roughly 8000 characters or more), some output languages exceeded 4096 tokens, causing the latter part of the translation to be cut off. In the case of Claude 3.5 Sonnet, the maximum number of output tokens doubled to 8192, so there were rarely cases where this maximum output token count was exceeded and caused problems, and from Claude 3.7 onwards, it was upgraded to support much longer output lengths. In the `prompt.py`{: .filepath} in the above GitHub repository, `max_tokens=16384` is specified.
{: .prompt-tip }

#### translate_changes.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
# ]
# ///
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # File patterns to exclude
    excluded_patterns = [
        '.DS_Store',  # macOS system file
        '~',          # temporary file
        '.tmp',       # temporary file
        '.temp',      # temporary file
        '.bak',       # backup file
        '.swp',       # vim temporary file
        '.swo'        # vim temporary file
    ]
    
    # Return False if filename contains any excluded pattern
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin", "Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

if __name__ == "__main__":
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    changed_files = compare_hash.changed_files(source_lang_code)
    # Filter temporary files
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    # Outer loop: progress of changed files
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Inner loop: progress of translation by language for each file
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### How to Use Python Scripts
Based on Jekyll blogs, create subdirectories by [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) language codes within the `/_posts`{: .filepath} directory, such as `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Place Korean originals in the `/_posts/ko`{: .filepath} directory (or modify the `source_lang` variable in the Python script as needed and place originals in the corresponding language in the corresponding directory), place the Python scripts and `hash.csv`{: .filepath} file introduced above in the `/tools`{: .filepath} directory, then open a terminal at that location and run the following command.

```bash
python3 translate_changes.py
```

Then the script will run and display a screen like the one below.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

## Real Usage Experience
As mentioned earlier, I introduced Claude Sonnet API-based automatic post translation to this blog at the end of June 12024 and have been using it with continuous improvements. In most cases, I can receive natural translations without additional human intervention, and after posting translated posts in multiple languages, I confirmed that organic search traffic from regions outside Korea such as Brazil, Canada, the United States, France, and Japan actually increased significantly. Moreover, when checking recorded sessions, many visitors who came through translated versions stayed for several minutes to even tens of minutes, which suggests that the translation quality is not awkward even by native speaker standards, considering that people usually press the back button or look for English versions when webpage content obviously shows signs of machine translation.

Additionally, beyond blog traffic inflow, there were incidental benefits from a learning perspective for me as the author. Since Claude writes quite smooth English text, during the review process before committing and pushing posts to the GitHub Pages repository, I have opportunities to see how specific terms or expressions from my Korean originals can be naturally expressed in English. While this alone may not be sufficient for complete English learning, being able to frequently encounter natural English expressions for not only everyday expressions but also academic expressions and terminology through examples from my own familiar writing without any additional effort seems to work quite well as an advantage for an undergraduate engineering student in a non-English speaking country like Korea.
