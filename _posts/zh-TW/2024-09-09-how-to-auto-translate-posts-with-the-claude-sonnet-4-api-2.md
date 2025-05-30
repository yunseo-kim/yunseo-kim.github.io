---
title: 使用 Claude Sonnet 4 API 自動翻譯文章的方法 (2) - 自動化腳本撰寫及應用
description: "設計用於 Markdown 文字檔案多語言翻譯的提示詞，並運用從 Anthropic 取得的 API 金鑰和撰寫的提示詞，透過 Python 自動化作業流程。本文是該系列的第二篇文章，介紹 API 發放及整合與 Python 腳本撰寫方法。"
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## 前言
自 12024 年 6 月導入 Anthropic 的 Claude 3.5 Sonnet API 用於部落格文章的多語言翻譯以來，經過數次提示詞及自動化腳本改進，以及模型版本升級，在將近一年的期間內滿意地運用該翻譯系統。因此在這個系列中，將探討導入過程中選擇 Claude Sonnet 模型的原因、提示詞設計方法，以及透過 Python 腳本進行 API 整合及自動化實作的方法。  
系列共由 2 篇文章組成，您正在閱讀的這篇是該系列的第二篇文章。
- 第 1 篇：[Claude Sonnet 模型介紹及選定理由、提示詞工程](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- 第 2 篇：運用 API 撰寫 Python 自動化腳本及應用（本文）

## 開始之前
本文是接續[第 1 篇](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)的文章，因此如果尚未閱讀，建議先閱讀前一篇文章。

## 完成的系統提示詞
經過前述[第 1 篇介紹的過程](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#提示詞設計)完成的提示詞設計結果如下。

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

## Claude API 整合
### Claude API 金鑰發放

> 這裡說明如何新發放 Claude API 金鑰。如果已經有可使用的 API 金鑰，可以跳過這個步驟。
{: .prompt-tip }

前往 <https://console.anthropic.com> 並登入。如果尚未有帳號，需要先進行會員註冊。登入後會看到如下的儀表板畫面。  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

在該畫面點擊 'Get API keys' 按鈕，可以看到如下畫面。  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) 我已經有建立好的金鑰，所以顯示名為 `yunseo-secret-key` 的金鑰，但如果是剛建立帳號且尚未發放 API 金鑰的狀態，應該沒有持有的金鑰。點擊右上角的 'Create Key' 按鈕即可發放新金鑰。

> 完成金鑰發放後，畫面會顯示您的 API 金鑰，該金鑰之後無法再次確認，因此務必記錄在安全的地方。
{: .prompt-warning }

### （建議）在環境變數中註冊 Claude API 金鑰
要在 Python 或 Shell 腳本中使用 Claude API，需要載入 API 金鑰。雖然可以直接在腳本中記錄 API 金鑰，但如果是需要上傳到 GitHub 等或以其他方式與他人分享的腳本，就無法使用這種方法。此外，即使沒有分享腳本檔案的打算，也可能因意外失誤導致腳本檔案外洩，如果腳本檔案中記錄了 API 金鑰，就有 API 金鑰一併外洩的風險。因此建議將 API 金鑰註冊在只有本人使用的系統環境變數中，在腳本中載入該環境變數的方式使用。以下以 UNIX 系統為基準，介紹在系統環境變數中註冊 API 金鑰的方法。Windows 的情況請參考網路上的其他文章。

1. 在終端機中根據您使用的 shell 類型，輸入 `nano ~/.bashrc` 或 `nano ~/.zshrc` 執行編輯器。
2. 在該檔案內容中新增 `export ANTHROPIC_API_KEY='your-api-key-here'`。將 'your-api-key-here' 部分替換為您的 API 金鑰，注意必須用 ' 包圍。
3. 儲存變更並退出編輯器。
4. 在終端機中執行 `source ~/.bashrc` 或 `source ~/.zshrc` 以套用變更。

### 安裝必要的 Python 套件
如果您使用的 Python 環境中尚未安裝 anthropic 套件，請使用以下命令安裝。
```bash
pip3 install anthropic
```
此外，以下套件也是後面介紹的文章翻譯腳本所需要的，請使用以下命令安裝或更新。
```bash
pip3 install -U argparse tqdm
```

### 撰寫 Python 腳本
本文介紹的文章翻譯腳本由以下 3 個 Python 腳本檔案和 1 個 CSV 檔案組成。

- `compare_hash.py`{: .filepath}：計算 `_posts/ko`{: .filepath} 目錄中韓文原文文章的 SHA256 雜湊值，與 `hash.csv`{: .filepath} 檔案中記錄的既有雜湊值比較，回傳變更或新增檔案名稱的清單
- `hash.csv`{: .filepath}：記錄既有文章檔案 SHA256 雜湊值的 CSV 檔案
- `prompt.py`{: .filepath}：接收 filepath、source_lang、target_lang 值，從系統環境變數載入 Claude API 金鑰值後呼叫 API，以系統提示詞提交前述撰寫的提示詞，以使用者提示詞提交 'filepath' 中要翻譯文章的內容。之後從 Claude Sonnet 4 模型接收回應（翻譯結果），輸出為 `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath} 路徑的文字檔案
- `translate_changes.py`{: .filepath}：擁有 source_lang 字串變數和 'target_langs' 清單變數，呼叫 `compare_hash.py`{: .filepath} 中的 `changed_files()` 函數回傳 changed_files 清單變數。如果有變更的檔案，對 changed_files 清單中的所有檔案和 target_langs 清單中的所有元素執行雙重迴圈，在該迴圈中呼叫 `prompt.py`{: .filepath} 中的 `translate(filepath, source_lang, target_lang)` 函數執行翻譯作業。

完成的腳本檔案內容也可以在 GitHub 的 [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) 儲存庫中確認。

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
由於包含前述撰寫的提示詞內容，檔案內容較長，因此以 GitHub 儲存庫中原始檔案的連結代替。  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> 上述連結中的 `prompt.py`{: .filepath} 檔案中，`max_tokens` 是與 Context window 大小無關，指定最大輸出長度的變數。使用 Claude API 時，一次可輸入的 Context window 大小為 200k 個 token（約 68 萬字的分量），但與此無關，各模型支援的最大輸出 token 數是固定的，建議在使用 API 前先在 [Anthropic 官方文件](https://docs.anthropic.com/en/docs/about-claude/models)中確認。既有的 Claude 3 系列模型最多可輸出 4096 個 token，以這個部落格的文章實驗時，韓文約 8000 字以上較長分量的文章，在某些輸出語言中會超過 4096 個 token，導致翻譯文後半部被截斷的問題。Claude 3.5 Sonnet 的最大輸出 token 數增加到 2 倍的 8192，因此通常不會因超過最大輸出 token 數而產生問題，從 Claude 3.7 開始更支援更長的輸出。上述 GitHub 儲存庫的 `prompt.py`{: .filepath} 中設定為 `max_tokens=16384`。
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
    # 要排除的檔案模式
    excluded_patterns = [
        '.DS_Store',  # macOS 系統檔案
        '~',          # 暫存檔案
        '.tmp',       # 暫存檔案
        '.temp',      # 暫存檔案
        '.bak',       # 備份檔案
        '.swp',       # vim 暫存檔案
        '.swo'        # vim 暫存檔案
    ]
    
    # 如果檔案名稱包含任一排除模式則回傳 False
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
    # 過濾暫存檔案
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    # 外部迴圈：變更檔案進度
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # 內部迴圈：各檔案的語言別翻譯進度
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### Python 腳本使用方法
以 Jekyll 部落格為基準，在 `/_posts`{: .filepath} 目錄中按 [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) 語言代碼設置 `/_posts/ko`{: .filepath}、`/_posts/en`{: .filepath}、`/_posts/pt-BR`{: .filepath} 等子目錄。然後在 `/_posts/ko`{: .filepath} 目錄中放置韓文原文（或在 Python 腳本中根據需要修改 `source_lang` 變數後，在對應目錄中放置該語言的原文），在 `/tools`{: .filepath} 目錄中放置上述介紹的 Python 腳本和 `hash.csv`{: .filepath} 檔案，然後在該位置開啟終端機並執行以下命令。

```bash
python3 translate_changes.py
```

腳本執行後會輸出如下畫面。  
![執行腳本截圖 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![執行腳本截圖 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

## 實際使用心得
如前所述，自 12024 年 6 月底在這個部落格導入使用 Claude Sonnet API 的文章自動翻譯後，持續改進並使用中。大部分情況下無需額外人工介入即可獲得自然的翻譯文，上傳多語言翻譯文章後，確實有來自巴西、加拿大、美國、法國、日本等韓國以外地區的 Organic Search 流量大量流入。而且查看錄製的 session 時，透過翻譯版本流入的訪客中，停留數分鐘到數十分鐘以上的情況也不少，考慮到網頁內容明顯使用機器翻譯的尷尬文章時，通常會按返回鍵離開或尋找英文版本，這表示翻譯版本的品質即使以母語使用者的標準來看也不會太尷尬。此外，除了部落格流量流入外，對於撰寫文章的我本人的學習方面也有附加優點，由於 Claude 以英文為基準撰寫相當流暢的文章，在 Commit & Push 文章到 GitHub Pages 儲存庫前的檢視過程中，可以確認我撰寫的韓文原文中特定術語或表達在英文中如何表達才自然。雖然僅憑這點無法說是充分的英語學習，但對於像韓國這樣的非英語圈國家的工科大學生來說，能夠以最熟悉的我親自撰寫的文章為例文，無需額外努力就能經常接觸日常表達以及學術表達或術語的自然英文表達，這也是相當大的優點。
