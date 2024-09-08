---
title: Claude 3.5 Sonnet APIでポストを自動翻訳する方法
description: >-
  最近公開されたClaude 3.5 Sonnetモデルを簡単に紹介し、このブログポストの多言語翻訳作業に適用するためのプロンプトをデザインした過程と完成したプロンプトの結果を共有します。
  そして、Anthropicから発行されたAPIキーと先ほど作成したプロンプトを適用して、Pythonで翻訳自動化スクリプトを作成し活用する方法を紹介します。
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## はじめに
最近、ブログポストの多言語翻訳のためにAnthropicのClaude 3.5 Sonnet APIを導入しました。ここでは、導入過程でClaude 3.5 Sonnet APIを選択した理由とプロンプトのデザイン方法、そしてPythonスクリプトを通じたAPI連携と自動化の実装方法を扱います。

## Claude 3.5 Sonnetについて
Claude 3シリーズモデルは、モデルサイズに応じてHaiku、Sonnet、そしてOpusバージョンが提供されています。  
![Claude 3モデルティア区分](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 画像出典: [Anthropic Claude API公式ウェブページ](https://www.anthropic.com/api)

そして韓国時間2024年6月21日、Anthropicが最新の言語モデルである[Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)を公開しました。Anthropicの発表によると、既存のClaude 3 Sonnetと同じコストと速度でClaude 3 Opusを上回る推論性能を示すとのことで、概して作文と言語推論、多言語理解および翻訳分野で競合モデルであるGPT-4に比べて強みを持つという評価が支配的です。  
![Claude 3.5 Sonnet紹介画像](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet性能ベンチマーク結果](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 画像出典: [Anthropicホームページ](https://www.anthropic.com/news/claude-3-5-sonnet)

## ポスト翻訳のためにClaude 3.5を導入した理由
あえてClaude 3.5やGPT-4のような言語モデルでなくても、Google翻訳やDeepLのような既存の商用翻訳APIが存在します。それにもかかわらず、翻訳目的でLLMを使用することにした理由は、他の商用翻訳サービスとは異なり、ユーザーがプロンプトデザインを通じてモデルに文章の作成目的や主要テーマなど本文以外にも追加的な文脈情報や要求事項を提供でき、モデルはそれに合わせて文脈を考慮した翻訳を提供できるからです。DeepLやGoogle翻訳も概ね優れた翻訳品質を示す傾向がありますが、文章のテーマや全体的な文脈をよく把握できない限界のため、日常的な会話ではなく専門的なテーマの長い文章を翻訳するよう要求した場合は、相対的に翻訳結果が不自然な場合がありました。特にClaudeは上述したように、競合モデルであるGPT-4に比べて作文、言語推論、多言語理解および翻訳分野で相対的により優れているという評価が多いため、このブログに記載する工学関連の文章を複数の言語に翻訳する作業に適していると判断しました。

## プロンプトデザイン
### プロンプトデザインの基本原則
言語モデルから目的に合った満足のいく結果物を得るためには、それに合った適切なプロンプトを提供する必要があります。プロンプトデザインというと何か漠然と感じられるかもしれませんが、実際には「何かをうまく要求する方法」という点で、相手が言語モデルであれ人間であれ大きく変わりません。このような観点からアプローチすれば、それほど難しくありません。5W1Hに従って現状況および要請事項を明確に説明し、必要であれば具体的な例をいくつか添えるのも良いでしょう。プロンプトデザインに関する数多くのヒントやテクニックが存在しますが、ほとんどは上述した基本原則から派生したものです。

### 役割付与および状況説明（誰が、なぜ）
まず最初にClaude 3.5に*「技術分野の専門翻訳者(professional technical translator)」*という役割を与え、*「主に数学や物理学、データサイエンスに関する文章を寄稿する工学ブロガー」*というユーザーに関する文脈情報を提供しました。
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### 大枠での要請事項伝達（何を）
次に、ユーザーから提供されたマークダウン形式の文章を{source_lang}から{target_lang}に形式を維持しながら翻訳するよう要請しました。 
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Claude API呼び出し時、プロンプトの{source_lang}と{target_lang}の位置には、PythonスクリプトのF文字列機能を通じて翻訳元言語と目標言語変数がそれぞれ入ります。
{: .prompt-info }

### 要求事項の具体化および例示（どのように）
簡単な作業であれば前の段階までで十分に望む結果を得られる場合もありますが、複雑な作業を要求する場合には追加の説明が必要な場合があります。この場合は、以下のような条件を追加しました。

#### YAML front matterの処理
Jekyllブログにアップロードするためにmarkdownで作成したポストの冒頭に位置するYAML front matterには、'title'と'description'、'categories'、そして'tags'情報を記録します。例えば、この文章のYAML front matterは次のようになっています。

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

しかし、ポストを翻訳する際にタイトル(title)と説明(description)タグは多言語に翻訳する必要がありますが、ポストURLの一貫性のためにはカテゴリー(categories)とタグ(tags)名は翻訳せずに英文のままにしておくのがメンテナンスに有利です。したがって、以下のような指示を出して'title'と'description'以外のタグは翻訳しないようにしました。ClaudeはYAML front matterに関する情報をすでに学習して知っているはずなので、この程度の説明でほとんどの場合十分です。
> In the provided markdown formatted text, do not translate the YAML front matter except for the 'title' and 'description' tags.

#### 提供された原文が出発言語以外の言語を含む場合の処理
韓国語で原文を作成する際、ある概念の定義を初めて紹介したり、いくつかの専門用語を使用する場合に、*'중성자 감쇠 (Neutron Attenuation)'*のように括弧内に英語表現を一緒に記載することがよくあります。このような表現を翻訳する場合、ある時は括弧を残し、またある時は括弧内に記載された英文を省略するなど、翻訳方式が一貫していない問題があったため、以下の文をプロンプトに追加しました。
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### 他のポストにリンクする場合の処理
いくつかのポストは他のポストへのリンクを含んでいますが、URLのパス部分まで翻訳すべき対象として解釈して変更してしまい、内部リンクが壊れる問題がよく発生しました。この問題はプロンプトにこの文を追加して解決しました。
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### 翻訳結果のみを応答として出力すること
最後に、応答時に他の言葉を付け加えず、翻訳結果のみを出力するよう次の文を提示します。
> The output should only contain the translated text.

### 完成したプロンプト
上記の段階を経たプロンプトデザインの結果物は次の通りです。
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.

## Claude API連携
### Claude APIキーの発行

> ここではClaude APIキーを新たに発行する方法を説明します。すでに使用するAPIキーを持っている場合は、この段階はスキップしても構いません。
{: .prompt-tip }

<https://console.anthropic.com>にアクセスしてログインします。まだアカウントがない場合は、まず会員登録を行う必要があります。ログインすると、以下のようなダッシュボード画面が表示されます。  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

該当画面で'Get API keys'ボタンをクリックすると、次のような画面が表示されます。  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) 私はすでに作成済みのキーがあるため、`yunseo-secret-key`という名前のキーが表示されていますが、アカウントを初めて作成してAPIキーをまだ発行していない状態であれば、おそらく保有しているキーはないはずです。右上の'Create Key'ボタンをクリックして新しいキーを発行すればよいです。

> キーの発行が完了すると画面に自分のAPIキーが表示されますが、該当キーは以後再確認できないため、必ず安全な場所に別途記録しておく必要があります。
{: .prompt-warning }

### （推奨）環境変数にClaude APIキーを登録
PythonやShellスクリプトでClaude APIを活用するには、APIキーを読み込む必要があります。スクリプト自体にAPIキーを記録する方法もありますが、GitHubなどにアップロードしたり、その他の方法で他の人々と共有する必要があるスクリプトであれば、この方法は使えません。またスクリプトファイルを共有する予定がなくても、意図しないミスでスクリプトファイルが流出する可能性があり、もしスクリプトファイルにAPIキーが記録されていれば、APIキーまで一緒に流出する事故が発生するリスクがあります。したがって、APIキーを自分だけが使用するシステムの環境変数に登録しておき、スクリプトではその環境変数を読み込む方式で活用することをお勧めします。以下では、UNIXシステムを基準にシステム環境変数にAPIキーを登録する方法を紹介します。Windowsの場合は、ウェブ上の他の記事を参照してください。

1. ターミナルで自分が使用しているシェルの種類に合わせて`nano ~/.bashrc`または`nano ~/.zshrc`を入力してエディタを実行します。
2. そのファイル内容に`export ANTHROPIC_API_KEY='your-api-key-here'`を追加します。'your-api-key-here'部分に自分のAPIキーを代わりに入れればよく、必ず'を使って囲む必要があることに注意してください。
3. 変更内容を保存してエディタを終了します。
4. ターミナルで`source ~/.bashrc`または`source ~/.zshrc`を実行して変更事項を反映します。

### 必要なPythonパッケージのインストール
自分が使用しているPython環境にanthropicパッケージがインストールされていない場合は、次のコマンドでインストールします。
```bash
pip3 install anthropic
```
また、以下のパッケージも後で紹介するポスト翻訳スクリプトを使用するには必要なので、次のコマンドでインストールまたはアップデートします。
```bash
pip3 install -U argparse tqdm
```

### Pythonスクリプトの作成
この記事で紹介するポスト翻訳スクリプトは、次の3つのPythonスクリプトファイルと1つのCSVファイルで構成されています。

- `compare_hash.py`: `_posts/ko`{: .filepath}ディレクトリ内にある韓国語原文ポストのSHA256ハッシュ値を計算した後、`hash.csv`ファイルに記録されている既存のハッシュ値と比較して変更または新たに追加されたファイル名のリストを返す
- `hash.csv`: 既存のポストファイルのSHA256ハッシュ値を記録したCSVファイル
- `prompt.py`: filepath、source_lang、target_lang値を入力として受け取り、システム環境変数からClaude APIキー値を読み込んだ後、APIを呼び出し、システムプロンプトとして先ほど作成したプロンプトを、ユーザープロンプトとして'filepath'にある翻訳するポストの内容を提出。その後、Claude 3.5 Sonnetモデルから応答（翻訳結果）を受け取り、`'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}パスにテキストファイルとして出力
- `translate_changes.py`: source_lang文字列変数と'target_langs'リスト変数を持ち、`compare_hash.py`内の`changed_files()`関数を呼び出してchanged_filesリスト変数を返してもらう。変更されたファイルがある場合、changed_filesリスト内のすべてのファイル、そしてtarget_langsリスト内のすべての要素に対する二重ループを実行し、該当ループ内で`prompt.py`内の`translate(filepath, source_lang, target_lang)`関数を呼び出して翻訳作業を実行するようにする。

完成したスクリプトファイルの内容は、GitHubの[yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools)リポジトリでも確認できます。

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
先ほど作成したプロンプトの内容まで含んでいるためファイルの内容が少し長いので、GitHubリポジトリにあるソースファイルのリンクで代替します。  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> 上記リンクにある`prompt.py`ファイルで`max_tokens`は、Context windowサイズとは別に最大出力長を指定する変数です。Claude API使用時に一度に入力できるContext windowのサイズは200kトークン（約68万文字程度の分量）ですが、それとは別に各モデルごとにサポートする最大出力トークン数が決まっているので、API活用前に[Anthropic公式ドキュメント](https://docs.anthropic.com/en/docs/about-claude/models)で事前に確認しておくことをお勧めします。既存のClaude 3シリーズモデルは最大4096トークンまで出力が可能でしたが、このブログの記事で実験してみた結果、大多数のポストでは問題ありませんでしたが、中には韓国語で約8000文字以上のやや長い分量のポストの場合、いくつかの出力言語で4096トークンを超えて翻訳文の後半部分が切れる問題が発生しました。Claude 3.5 Sonnetの場合、最大出力トークン数が2倍の8192に増えたため、よほどのことがない限りこの最大出力トークン数を超えて問題になることはなく、上記GitHubリポジトリの`prompt.py`でも`max_tokens=8192`と指定しています。
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

### Pythonスクリプトの使用方法
Jekyllブログを基準に、ポストが位置する`/_posts`{: .filepath}ディレクトリ内に[ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php)言語コード別に`/_posts/ko`{: .filepath}、`/_posts/en`{: .filepath}、`/_posts/pt-BR`{: .filepath}のようにサブディレクトリを置きます。そして`/tools`{: .filepath}ディレクトリに上で紹介したPythonスクリプトとCSVファイルを置いた後、その位置でターミナルを開き、以下のコマンドを実行します。

```bash
python3 translate_changes.py
```

そうすると、スクリプトが実行され、以下のような画面が表示されるはずです。  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## 実使用記
上述したようにClaude 3.5 APIを利用したポスト自動翻訳をこのブログに導入してから約2ヶ月ほど使用中です。ほとんどの場合、別途人が追加介入する必要なく優れた品質の翻訳文を提供してもらえ、ポストを多言語で翻訳してアップロードしてからブラジルやカナダ、アメリカ、フランスなど韓国以外の地域からの検索を通じたOrganic Searchトラフィックが実際に流入されていることを確認しました。また、ブログのトラフィック流入だけでなく、文章作成者本人の学習面でも付加的な利点がありました。Claudeが英文基準でかなり滑らかな文章を作成してくれるため、GitHub Pagesリポジトリにポストをプッシュする前にレビューする過程で、私が作成した韓国語原文の特定の用語や表現を英語ではどのように表現すれば自然なのかを確認する機会がありました。これだけで十分な英語学習ができるとは言い難いですが、日常的な表現だけでなく学術的な表現や用語に対する自然な英文表現を、どんな文章よりも馴染みのある自分が直接作成した文章を例文として、特別な追加的な努力なしに頻繁に接することができるというのも、韓国のような非英語圏地域国家の工学部学部生にはそれなりに利点として作用するように思います。
