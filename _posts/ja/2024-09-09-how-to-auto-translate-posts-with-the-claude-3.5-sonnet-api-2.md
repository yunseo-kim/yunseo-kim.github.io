---
title: Claude 3.5 Sonnet APIでポストを自動翻訳する方法 (2) - 自動化スクリプトの作成と適用
description: マークダウンテキストファイルの多言語翻訳のためのプロンプトをデザインし、Anthropicから発行されたAPIキーと作成したプロンプトを適用してPythonで作業を自動化するプロセスを扱います。このポストはシリーズの2番目の記事で、API発行と連携、Pythonスクリプト作成方法を紹介する。
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## はじめに
最近、ブログポストの多言語翻訳のためにAnthropicのClaude 3.5 Sonnet APIを導入した。このシリーズでは、導入過程でClaude 3.5 Sonnet APIを選択した理由とプロンプトのデザイン方法、そしてPythonスクリプトを通じたAPI連携と自動化の実装方法を扱う。  
シリーズは2つの記事で構成されており、この記事はシリーズの2番目の記事である。
- 第1回: [Claude 3.5 Sonnetモデルの紹介と選定理由、プロンプトエンジニアリング](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- 第2回: APIを活用したPython自動化スクリプトの作成と適用（本文）

## 始める前に
この記事は[第1回](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)に続く記事なので、まだ読んでいない場合は、まず前の記事から読むことをお勧めする。

## Claude API連携
### Claude APIキーの発行

> ここではClaude APIキーを新たに発行する方法を説明する。すでに使用するAPIキーを持っている場合は、このステップをスキップしても良い。
{: .prompt-tip }

<https://console.anthropic.com>にアクセスしてログインする。まだアカウントがない場合は、まず会員登録を行う必要がある。ログインすると、以下のようなダッシュボード画面が表示される。  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

この画面で「Get API keys」ボタンをクリックすると、次のような画面が表示される。  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) 私はすでに作成済みのキーがあるため、`yunseo-secret-key`という名前のキーが表示されているが、アカウントを初めて作成してAPIキーをまだ発行していない状態であれば、おそらく保有しているキーはないはずだ。右上の「Create Key」ボタンをクリックして新しいキーを発行すれば良い。

> キーの発行が完了すると画面に自分のAPIキーが表示されるが、そのキーは後で再確認することができないため、必ず安全な場所に別途記録しておく必要がある。
{: .prompt-warning }

### （推奨）環境変数にClaude APIキーを登録
PythonやShellスクリプトでClaude APIを活用するには、APIキーを読み込む必要がある。スクリプト自体にAPIキーを記録する方法もあるが、GitHubなどにアップロードしたり、その他の方法で他の人々と共有する必要があるスクリプトの場合、この方法は使えない。また、スクリプトファイルを共有する予定がなくても、意図しないミスでスクリプトファイルが流出する可能性があり、もしスクリプトファイルにAPIキーが記録されていれば、APIキーまで一緒に流出する事故が発生するリスクがある。したがって、APIキーを自分だけが使用するシステムの環境変数に登録しておき、スクリプトではその環境変数を読み込む方式で活用することをお勧めする。以下では、UNIXシステムを基準にシステム環境変数にAPIキーを登録する方法を紹介する。Windowsの場合は、ウェブ上の他の記事を参照してほしい。

1. ターミナルで使用しているシェルの種類に合わせて `nano ~/.bashrc` または `nano ~/.zshrc` を入力してエディタを実行する。
2. そのファイルの内容に `export ANTHROPIC_API_KEY='your-api-key-here'` を追加する。'your-api-key-here'の部分に自分のAPIキーを代わりに入れれば良く、必ず'を使って囲む必要があることに注意する。
3. 変更内容を保存してエディタを終了する。
4. ターミナルで `source ~/.bashrc` または `source ~/.zshrc` を実行して変更事項を反映する。

### 必要なPythonパッケージのインストール
使用しているPython環境にanthropicパッケージがインストールされていない場合は、次のコマンドでインストールする。
```bash
pip3 install anthropic
```
また、以下のパッケージも後で紹介するポスト翻訳スクリプトを使用するには必要なので、次のコマンドでインストールまたはアップデートする。
```bash
pip3 install -U argparse tqdm
```

### Pythonスクリプトの作成
この記事で紹介するポスト翻訳スクリプトは、次の3つのPythonスクリプトファイルと1つのCSVファイルで構成されている。

- `compare_hash.py`: `_posts/ko`{: .filepath}ディレクトリ内にある韓国語原文ポストのSHA256ハッシュ値を計算した後、`hash.csv`ファイルに記録されている既存のハッシュ値と比較して変更または新たに追加されたファイル名のリストを返す
- `hash.csv`: 既存のポストファイルのSHA256ハッシュ値を記録したCSVファイル
- `prompt.py`: filepath、source_lang、target_lang値を入力として受け取り、システム環境変数からClaude APIキー値を読み込んだ後、APIを呼び出し、システムプロンプトとして先ほど作成したプロンプトを、ユーザープロンプトとして'filepath'にある翻訳するポストの内容を提出。その後、Claude 3.5 Sonnetモデルから応答（翻訳結果）を受け取り、`'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}パスにテキストファイルとして出力
- `translate_changes.py`: source_lang文字列変数と'target_langs'リスト変数を持ち、`compare_hash.py`内の`changed_files()`関数を呼び出してchanged_filesリスト変数を返してもらう。変更されたファイルがある場合、changed_filesリスト内のすべてのファイル、そしてtarget_langsリスト内のすべての要素に対する二重ループを実行し、そのループ内で`prompt.py`内の`translate(filepath, source_lang, target_lang)`関数を呼び出して翻訳作業を実行するようにする。

完成したスクリプトファイルの内容はGitHubの[yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools)リポジトリでも確認できる。

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
    # ファイルハッシュをファイル名（辞書のキー）でソート
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
            if not file.endswith('.md'):  # .mdファイルのみ処理
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
        print("変更されたファイル:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("変更されたファイルはありません。")

    os.chdir(initial_wd)
```

#### prompt.py
先ほど作成したプロンプトの内容まで含んでいるためファイルの内容が少し長いので、GitHubリポジトリにあるソースファイルのリンクで代替する。  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> 上のリンクにある`prompt.py`ファイルで`max_tokens`は、コンテキストウィンドウサイズとは別に最大出力長を指定する変数である。Claude API使用時に一度に入力できるコンテキストウィンドウのサイズは200kトークン（約68万文字程度の分量）だが、それとは別に各モデルごとにサポートする最大出力トークン数が決まっているので、API活用前に[Anthropic公式ドキュメント](https://docs.anthropic.com/en/docs/about-claude/models)で事前に確認しておくことをお勧めする。既存のClaude 3シリーズモデルは最大4096トークンまで出力が可能だったが、このブログの記事で実験してみた結果、大多数のポストでは問題なかったものの、中には韓国語で約8000文字以上のやや長い分量のポストの場合、いくつかの出力言語で4096トークンを超えて翻訳文の後半部分が切れる問題が発生した。Claude 3.5 Sonnetの場合、最大出力トークン数が2倍の8192に増えたため、よほどのことがない限りこの最大出力トークン数を超えて問題になることはなく、上記GitHubリポジトリの`prompt.py`でも`max_tokens=8192`と指定している。
{: .prompt-tip }

#### translate_changes.py

```python
import sys
import os
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # 除外するファイルパターン
    excluded_patterns = [
        '.DS_Store',  # macOSシステムファイル
        '~',          # 一時ファイル
        '.tmp',       # 一時ファイル
        '.temp',      # 一時ファイル
        '.bak',       # バックアップファイル
        '.swp',       # vim一時ファイル
        '.swo'        # vim一時ファイル
    ]
    
    # ファイル名が除外パターンのいずれかを含む場合はFalseを返す
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
    # 一時ファイルのフィルタリング
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("変更されたファイルはありません。")
    print("変更されたファイル:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** 翻訳開始！ ***")
    # 外部ループ：変更されたファイルの進捗状況
    for changed_file in tqdm(changed_files, desc="ファイル", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # 内部ループ：各ファイルの言語別翻訳進捗状況
        for target_lang in tqdm(target_langs, desc="言語", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\n翻訳完了！")
    os.chdir(initial_wd)
```

### Pythonスクリプトの使用方法
Jekyllブログを基準に、ポストが位置する`/_posts`{: .filepath}ディレクトリ内に[ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php)言語コード別に`/_posts/ko`{: .filepath}、`/_posts/en`{: .filepath}、`/_posts/pt-BR`{: .filepath}のようにサブディレクトリを置く。そして`/tools`{: .filepath}ディレクトリに上で紹介したPythonスクリプトとCSVファイルを置いた後、その位置でターミナルを開き、以下のコマンドを実行する。

```bash
python3 translate_changes.py
```

そうするとスクリプトが実行され、以下のような画面が表示される。  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## 実使用記
上述したようにClaude 3.5 APIを利用したポスト自動翻訳をこのブログに導入してから約2ヶ月ほど使用中である。ほとんどの場合、別途人が追加で介入する必要なく優れた品質の翻訳文を提供してもらえ、ポストを多言語で翻訳してアップロードしてからブラジルやカナダ、アメリカ、フランスなど韓国以外の地域からの検索を通じたOrganic Searchトラフィックが実際に流入されているのを確認した。また、ブログのトラフィック流入だけでなく、記事作成者本人の学習面でも付加的な利点があった。Claudeが英文基準でかなり滑らかな文章を作成してくれるため、GitHub Pagesリポジトリにポストをプッシュする前にレビューする過程で、自分が作成した韓国語原文の特定の用語や表現を英語ではどのように表現すると自然なのかを確認する機会がある。これだけで十分な英語学習ができるとは言い難いが、日常的な表現だけでなく学術的な表現や用語に対する自然な英語表現を、どんな文章よりも馴染みのある自分が直接作成した文章を例文として、特別な追加の努力なしに頻繁に接することができるというのも、韓国のような非英語圏地域の国の工学部学部生にとってはそれなりに利点として作用するように思える。
