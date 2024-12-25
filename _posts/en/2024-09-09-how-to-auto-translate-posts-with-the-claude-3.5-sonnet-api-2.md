---
title: How to Auto-translate Posts with Claude 3.5 Sonnet API (2) - Writing and Applying
  Automation Scripts
description: This post covers designing prompts for multilingual translation of markdown
  text files, and the process of automating the task using Python by applying the
  API key obtained from Anthropic and the created prompts. As the second article in
  the series, it introduces the methods for API issuance, integration, and Python
  script writing.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introduction
I recently adopted Anthropic's Claude 3.5 Sonnet API for multilingual translation of blog posts. In this series, I will cover the reasons for choosing the Claude 3.5 Sonnet API, prompt design methods, and how to implement API integration and automation through Python scripts.  
The series consists of 2 posts, and this post you're reading is the second one in the series.
- Part 1: [Introduction to Claude 3.5 Sonnet Model, Selection Rationale, and Prompt Engineering](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Part 2: Writing and Applying Python Automation Scripts with API (Current Post)

## Before Starting
This post is a continuation of [Part 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), so if you haven't read it yet, I recommend reading the previous post first.

## Claude API Integration
### Getting Claude API Key

> This section explains how to get a new Claude API key. If you already have an API key to use, you can skip this step.
{: .prompt-tip }

Visit <https://console.anthropic.com> and log in. If you don't have an account yet, you'll need to sign up first. After logging in, you'll see a dashboard screen like below.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Click the 'Get API keys' button on that screen, and you'll see a screen like this.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) I already have a key created, so a key named `yunseo-secret-key` is displayed, but if you've just created your account and haven't gotten an API key yet, you probably won't have any keys. You can get a new key by clicking the 'Create Key' button in the top right.

> When you complete the key issuance, your API key will be displayed on the screen. Since this key cannot be checked again later, make sure to record it separately in a safe place.
{: .prompt-warning }

### (Recommended) Registering Claude API Key as Environment Variable
To use the Claude API in Python or Shell scripts, you need to load the API key. While you can record the API key in the script itself, this method can't be used if you need to share the script with others through GitHub or other means. Also, even if you didn't plan to share the script file, there's a risk that the API key could be leaked along with the script file if the script file is accidentally exposed. Therefore, it's recommended to register the API key as an environment variable on your personal system and use it in scripts by loading that environment variable. Below, I'll introduce how to register an API key as a system environment variable based on UNIX systems. For Windows, please refer to other articles on the web.

1. In the terminal, run `nano ~/.bashrc` or `nano ~/.zshrc` depending on your shell type to launch the editor.
2. Add `export ANTHROPIC_API_KEY='your-api-key-here'` to the file content. Replace 'your-api-key-here' with your actual API key, and note that it must be wrapped in single quotes.
3. Save the changes and exit the editor.
4. Run `source ~/.bashrc` or `source ~/.zshrc` in the terminal to apply the changes.

### Installing Required Python Packages
If the anthropic package is not installed in your Python environment, install it with the following command:
```bash
pip3 install anthropic
```
Also, the following packages are needed to use the post translation script introduced later, so install or update them with this command:
```bash
pip3 install -U argparse tqdm
```

### Writing Python Scripts
The post translation script introduced in this article consists of 3 Python script files and 1 CSV file.

- `compare_hash.py`: Calculates SHA256 hash values of Korean original posts in the `_posts/ko`{: .filepath} directory and compares them with existing hash values recorded in the `hash.csv` file to return a list of changed or newly added filenames
- `hash.csv`: CSV file recording SHA256 hash values of existing post files
- `prompt.py`: Receives filepath, source_lang, target_lang values and loads Claude API key value from system environment variables, then calls API with previously written prompt as system prompt and content of post to be translated at 'filepath' as user prompt. Then receives response (translation result) from Claude 3.5 Sonnet model and outputs it as a text file at `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath} path
- `translate_changes.py`: Has source_lang string variable and 'target_langs' list variable, calls `changed_files()` function in `compare_hash.py` to return changed_files list variable. If there are changed files, executes nested loop for all files in changed_files list and all elements in target_langs list, and calls `translate(filepath, source_lang, target_lang)` function in `prompt.py` within that loop to perform translation.

The completed script files can also be found in the [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) repository on GitHub.

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
    # Sort the file hashes by filename (the dictionary keys)
    sorted_file_hashes = dict(sorted(file_hashes.items()))

    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for file_path, hash_value in sorted_file_hashes.items():
            writer.writerow([file_path, hash_value])

def changed_files():
    posts_dir = '../_posts/ko/'
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

    changed_files = changed_files()
    if changed_files:
        print("Changed files:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("No files have changed.")

    os.chdir(initial_wd)
```

#### prompt.py
Due to the length of the file content including the previously written prompt, I'll replace it with a link to the source file in the GitHub repository.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In the `prompt.py` file at the above link, `max_tokens` is a variable that specifies the maximum output length separately from the Context window size. While the Context window size that can be input at once when using the Claude API is 200k tokens (about 680,000 characters), separately from that, each model has a set maximum output token count, so it's recommended to check the [Anthropic official documentation](https://docs.anthropic.com/en/docs/about-claude/models) before using the API. Previous Claude 3 series models could output up to 4096 tokens, and while this wasn't a problem for most posts on this blog based on experiments, for some longer posts with roughly more than 8000 Korean characters, there was an issue where the latter part of the translation was cut off in some output languages as it exceeded 4096 tokens. In the case of Claude 3.5 Sonnet, the maximum output token count has doubled to 8192, so there were rarely any problems exceeding this maximum output token count, and in the `prompt.py` of the above GitHub repository, it's set to `max_tokens=8192`.
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
    initial_wd = os.getcwd()
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

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
    
    os.chdir(initial_wd)
```

### How to Use Python Scripts
For Jekyll blogs, create subdirectories by [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) language codes like `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath} inside the `/_posts`{: .filepath} directory where posts are located. Then, place the Python scripts and CSV file introduced above in the `/tools`{: .filepath} directory, open a terminal at that location, and run the following command:

```bash
python3 translate_changes.py
```

The script will run and display a screen like this:  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## User Experience
As mentioned above, I've been using automatic post translation with Claude 3.5 API on this blog for about 2 months. In most cases, high-quality translations can be obtained without additional human intervention, and after translating and posting in multiple languages, I've confirmed actual organic search traffic inflow from regions outside Korea such as Brazil, Canada, the United States, and France. Additionally, there were additional advantages in terms of learning for the writer beyond blog traffic inflow. Since Claude writes quite smooth English text, during the review process before pushing posts to the GitHub Pages repository, there's an opportunity to see how certain terms or expressions from my Korean original text can be naturally expressed in English. While this alone may not be sufficient for complete English learning, for an engineering undergraduate student in non-English speaking regions like Korea, it seems quite advantageous to frequently encounter natural English expressions for both everyday and academic terms and expressions, using my own familiar writing as example sentences, without any additional effort.
