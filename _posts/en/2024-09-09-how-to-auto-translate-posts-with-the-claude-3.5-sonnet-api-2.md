---
title: How to Auto-Translate Posts with Claude 3.5 Sonnet API (2) - Writing and Applying Automation Scripts
description: This post covers designing prompts for multilingual translation of markdown text files, and automating the process using Python with the API key obtained from Anthropic and the created prompts. This is the second post in the series, introducing API issuance, integration, and Python script writing methods.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Introduction
I recently adopted Anthropic's Claude 3.5 Sonnet API for multilingual translation of blog posts. In this series, I'll cover why I chose Claude 3.5 Sonnet API, how to design effective prompts, and how to implement automation through Python scripts and API integration.   
The series consists of 2 posts, and this post you're reading is the second one in the series.
- Part 1: [Introduction to Claude 3.5 Sonnet Model, Reasons for Selection, and Prompt Engineering](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Part 2: Writing and Applying Python Automation Scripts Using the API (This post)

## Before We Begin
This post is a continuation of [Part 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), so if you haven't read it yet, I recommend reading the previous post first.

## Claude API Integration
### Obtaining a Claude API Key

> This section explains how to obtain a new Claude API key. If you already have an API key to use, you can skip this step.
{: .prompt-tip }

Go to <https://console.anthropic.com> and log in. If you don't have an account yet, you'll need to sign up first. After logging in, you'll see a dashboard screen like the one below.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Click the 'Get API keys' button on this screen, and you'll see the following screen.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) I already have a key created, so a key named `yunseo-secret-key` is displayed, but if you've just created your account and haven't obtained an API key yet, you probably won't have any keys. Click the 'Create Key' button in the upper right to obtain a new key.

> When you complete the key issuance, your API key will be displayed on the screen. Since this key cannot be viewed again later, make sure to record it separately in a safe place.
{: .prompt-warning }

### (Recommended) Registering the Claude API Key as an Environment Variable
To use the Claude API in Python or Shell scripts, you need to load the API key. While you could record the API key in the script itself, this method isn't suitable if you need to upload the script to GitHub or share it with others in any other way. Even if you didn't intend to share the script file, there's a risk that the API key could be leaked along with the script file if it's accidentally exposed. Therefore, it's recommended to register the API key as an environment variable on your personal system and load that environment variable in the script. Below, I'll introduce how to register the API key as a system environment variable based on UNIX systems. For Windows, please refer to other articles on the web.

1. In the terminal, run `nano ~/.bashrc` or `nano ~/.zshrc` depending on your shell type to open the editor.
2. Add `export ANTHROPIC_API_KEY='your-api-key-here'` to the file content. Replace 'your-api-key-here' with your actual API key, and make sure to enclose it in single quotes.
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
The post translation script introduced in this article consists of three Python script files and one CSV file:

- `compare_hash.py`: Calculates the SHA256 hash values of the Korean original posts in the `_posts/ko`{: .filepath} directory, compares them with the existing hash values recorded in the `hash.csv` file, and returns a list of file names that have been changed or newly added
- `hash.csv`: A CSV file recording the SHA256 hash values of existing post files
- `prompt.py`: Receives filepath, source_lang, target_lang values, loads the Claude API key value from system environment variables, calls the API with the prompt we wrote earlier as the system prompt and the content of the post to be translated in 'filepath' as the user prompt. Then receives the response (translation result) from the Claude 3.5 Sonnet model and outputs it as a text file to the path `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`: Contains a source_lang string variable and a 'target_langs' list variable, calls the `changed_files()` function in `compare_hash.py` to return the changed_files list variable. If there are changed files, it executes a double loop for all files in the changed_files list and all elements in the target_langs list, calling the `translate(filepath, source_lang, target_lang)` function in `prompt.py` within this loop to perform the translation task.

The contents of the completed script files can also be found in the [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) repository on GitHub.

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
As it includes the content of the prompt we wrote earlier and the file content is quite long, I'll replace it with a link to the source file in the GitHub repository.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In the `prompt.py` file at the above link, `max_tokens` is a variable that specifies the maximum output length, separate from the Context window size. When using the Claude API, you can input up to 200k tokens (about 680,000 characters) in the Context window at once, but separately, each model has a set maximum output token count. It's recommended to check this in advance in the [Anthropic official documentation](https://docs.anthropic.com/en/docs/about-claude/models) before using the API. The existing Claude 3 series models could output up to 4096 tokens, which was not a problem for most posts in this blog based on experiments, but for some longer posts with more than about 8000 Korean characters, there was an issue where the latter part of the translation was cut off in some output languages due to exceeding 4096 tokens. In the case of Claude 3.5 Sonnet, the maximum output token count has doubled to 8192, so there were no problems exceeding this maximum output token count in most cases, and `max_tokens=8192` is specified in the `prompt.py` file in the above GitHub repository.
{: .prompt-tip }

#### translate_changes.py

```python
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # Patterns to exclude
    excluded_patterns = [
        '.DS_Store',  # macOS system file
        '~',          # Temporary file
        '.tmp',       # Temporary file
        '.temp',      # Temporary file
        '.bak',       # Backup file
        '.swp',       # vim temporary file
        '.swo'        # vim temporary file
    ]
    
    # Return False if the filename includes any of the excluded patterns
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin","Spanish", "Brazilian Portuguese", "French", "German"]
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
    # Outer loop: Progress of changed files
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Inner loop: Progress of translation for each language per file
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### How to Use the Python Scripts
For Jekyll blogs, create subdirectories for each [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) language code inside the `/_posts`{: .filepath} directory where posts are located, such as `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Then, place the Python scripts and CSV file introduced above in the `/tools`{: .filepath} directory, open a terminal at that location, and run the following command:

```bash
python3 translate_changes.py
```

The script will run and display a screen like the one below.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Real-world Usage Experience
As mentioned above, I've been using the automatic post translation with Claude 3.5 API on this blog for about 2 months. In most cases, it provides high-quality translations without the need for additional human intervention, and after translating and posting in multiple languages, I've confirmed actual organic search traffic from regions outside of Korea, such as Brazil, Canada, the United States, and France. In addition to blog traffic, there were additional advantages in terms of learning for the writer. Since Claude produces quite smooth English writing, during the review process before pushing posts to the GitHub Pages repository, I have the opportunity to see how certain terms or expressions I wrote in Korean can be naturally expressed in English. While this alone may not be sufficient for comprehensive English learning, it seems to be quite advantageous for an undergraduate engineering student in a non-English speaking country like Korea to frequently encounter natural English expressions for not only everyday phrases but also academic expressions and terms, using the most familiar text - the one I wrote myself - as an example, without any additional effort.
