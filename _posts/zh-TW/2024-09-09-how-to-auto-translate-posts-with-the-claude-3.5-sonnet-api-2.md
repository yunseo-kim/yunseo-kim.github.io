---
title: 如何使用Claude 3.5 Sonnet API自動翻譯文章 (2) - 編寫和應用自動化腳本
description: 本文介紹如何設計用於翻譯Markdown文本文件的多語言提示詞,以及如何使用從Anthropic獲得的API密鑰和設計的提示詞,通過Python實現工作自動化的過程。這是該系列的第二篇文章,介紹了API的獲取和集成以及Python腳本的編寫方法。
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## 前言
最近,我引入了Anthropic的Claude 3.5 Sonnet API來實現博客文章的多語言翻譯。在這個系列中,我將介紹選擇Claude 3.5 Sonnet API的原因、提示詞設計方法,以及如何通過Python腳本實現API集成和自動化。  
該系列由兩篇文章組成,您正在閱讀的是該系列的第二篇文章。
- 第1部分:[Claude 3.5 Sonnet模型介紹和選擇原因,提示詞工程](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- 第2部分:使用API編寫和應用Python自動化腳本(本文)

## 開始之前
本文是[第1部分](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)的延續,如果您還沒有閱讀,建議先閱讀前一篇文章。

## Claude API集成
### 獲取Claude API密鑰

> 這裡介紹如何獲取新的Claude API密鑰。如果您已經有可用的API密鑰,可以跳過這一步。
{: .prompt-tip }

訪問<https://console.anthropic.com>並登錄。如果您還沒有帳戶,需要先註冊。登錄後,您將看到如下所示的儀表板畫面。  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

在該畫面上點擊"Get API keys"按鈕,您將看到如下畫面。  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) 我已經創建了一個名為`yunseo-secret-key`的密鑰,所以它顯示在這裡,但如果您是第一次創建帳戶並且還沒有獲取API密鑰,可能不會看到任何密鑰。點擊右上角的"Create Key"按鈕來獲取新的密鑰。

> 完成密鑰獲取後,畫面上會顯示您的API密鑰,但之後將無法再次查看該密鑰,因此務必將其安全地記錄在別處。
{: .prompt-warning }

### (建議) 將Claude API密鑰註冊為環境變量
要在Python或Shell腳本中使用Claude API,需要加載API密鑰。雖然可以直接在腳本中記錄API密鑰,但如果需要上傳到GitHub或以其他方式與他人共享腳本,就不能使用這種方法。此外,即使沒有計劃共享腳本文件,也可能因意外錯誤導致腳本文件洩露,如果腳本文件中記錄了API密鑰,就有可能發生API密鑰一同洩露的事故。因此,建議將API密鑰註冊為僅供個人使用的系統環境變量,然後在腳本中加載該環境變量。以下介紹在UNIX系統中將API密鑰註冊為系統環境變量的方法。對於Windows系統,請參考網上的其他文章。

1. 在終端中,根據您使用的shell類型,輸入`nano ~/.bashrc`或`nano ~/.zshrc`來啟動編輯器。
2. 在文件內容中添加`export ANTHROPIC_API_KEY='your-api-key-here'`。將'your-api-key-here'替換為您的API密鑰,注意必須用單引號將其括起來。
3. 保存更改並退出編輯器。
4. 在終端中執行`source ~/.bashrc`或`source ~/.zshrc`以應用更改。

### 安裝所需的Python包
如果您的Python環境中尚未安裝anthropic包,請使用以下命令安裝:
```bash
pip3 install anthropic
```
此外,以下包也是後面介紹的文章翻譯腳本所需的,請使用以下命令安裝或更新:
```bash
pip3 install -U argparse tqdm
```

### 編寫Python腳本
本文介紹的文章翻譯腳本由以下3個Python腳本文件和1個CSV文件組成:

- `compare_hash.py`: 計算`_posts/ko`{: .filepath}目錄中韓語原文文章的SHA256哈希值,然後與`hash.csv`文件中記錄的現有哈希值進行比較,返回已更改或新添加的文件名列表
- `hash.csv`: 記錄現有文章文件SHA256哈希值的CSV文件
- `prompt.py`: 接收filepath、source_lang、target_lang值,從系統環境變量中加載Claude API密鑰值,然後調用API,將之前編寫的提示詞作為系統提示詞,將"filepath"中要翻譯的文章內容作為用戶提示詞提交。然後從Claude 3.5 Sonnet模型接收響應(翻譯結果),並將其作為文本文件輸出到`'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}路徑
- `translate_changes.py`: 包含source_lang字符串變量和'target_langs'列表變量,調用`compare_hash.py`中的`changed_files()`函數以返回changed_files列表變量。如果有更改的文件,則對changed_files列表中的所有文件和target_langs列表中的所有元素執行雙重循環,在該循環中調用`prompt.py`中的`translate(filepath, source_lang, target_lang)`函數執行翻譯任務。

完成的腳本文件內容也可以在GitHub的[yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools)存儲庫中查看。

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
由於包含之前編寫的提示詞內容,文件內容較長,因此用GitHub存儲庫中的源文件鏈接代替。  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> 上述鏈接中的`prompt.py`文件中的`max_tokens`是一個變量,用於指定最大輸出長度,與上下文窗口大小無關。使用Claude API時,一次可以輸入的上下文窗口大小為200k令牌(約68萬字左右),但每個模型支持的最大輸出令牌數是單獨指定的,因此建議在使用API之前先查看[Anthropic官方文檔](https://docs.anthropic.com/en/docs/about-claude/models)。以前的Claude 3系列模型最多可以輸出4096個令牌,根據對這個博客文章的實驗,大多數文章沒有問題,但對於一些較長的文章(韓文約8000字以上),在某些輸出語言中超過了4096個令牌,導致翻譯文本後部分被截斷的問題。Claude 3.5 Sonnet的最大輸出令牌數增加到了8192,是之前的兩倍,因此基本上不會出現超過這個最大輸出令牌數而導致問題的情況,上面GitHub存儲庫中的`prompt.py`也指定了`max_tokens=8192`。
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

### Python腳本使用方法
對於Jekyll博客,在包含文章的`/_posts`{: .filepath}目錄中,按照[ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php)語言代碼創建子目錄,如`/_posts/ko`{: .filepath}、`/_posts/en`{: .filepath}、`/_posts/pt-BR`{: .filepath}等。然後將上面介紹的Python腳本和CSV文件放在`/tools`{: .filepath}目錄中,在該位置打開終端並執行以下命令:

```bash
python3 translate_changes.py
```

腳本執行後,將顯示如下畫面:  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## 實際使用體驗
如上所述,我已經在這個博客上引入並使用了Claude 3.5 API進行文章自動翻譯約2個月。在大多數情況下,無需人工額外干預就能獲得高質量的翻譯文本。將文章翻譯成多種語言並發布後,我確實觀察到來自巴西、加拿大、美國、法國等韓國以外地區的通過搜索產生的自然搜索流量。除了增加博客流量外,對於文章作者本人的學習方面也有額外的好處。由於Claude能夠生成相當流暢的英文文章,在將文章推送到GitHub Pages存儲庫之前進行審核時,我可以了解如何用英語自然地表達我在韓語原文中使用的特定術語或表達。雖然僅憑這一點還不足以進行充分的英語學習,但對於像我這樣的非英語國家的工程學院本科生來說,能夠經常接觸到學術表達和術語的自然英文表達,而且是以我最熟悉的自己寫的文章為例子,無需額外努力就能獲得這樣的機會,這似乎也是一個相當大的優勢。
