---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법 (2) - 자동화 스크립트 작성 및 적용
description: >-
  본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인하고, Anthropic으로부터 발급받은 API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 이 포스트는 해당 시리즈의 두 번째 글로, API 발급 및 연동과 Python 스크립트 작성 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## 들어가며
최근에 블로그 포스트의 다국어 번역을 위해 Anthropic의 Claude 3.5 Sonnet API를 도입하였다. 이에 이 시리즈에서는 도입 과정에서 Claude 3.5 Sonnet API를 선택한 이유와 프롬프트 디자인 방법, 그리고 Python 스크립트를 통한 API 연동 및 자동화 구현 방법을 다루고자 한다.  
시리즈는 2개의 글로 이루어져 있으며, 읽고 있는 이 글은 해당 시리즈의 두 번째 글이다.
- 1편: [Claude 3.5 Sonnet 모델 소개 및 선정 이유, 프롬프트 엔지니어링](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- 2편: API를 활용한 Python 자동화 스크립트 작성 및 적용 (본문)

## 시작하기 전에
이 글은 [1편](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)에서 이어지는 글이므로, 만약 아직 읽지 않았다면 우선 이전 글부터 읽고 오는 것을 권장한다.

## Claude API 연동
### Claude API 키 발급

> 여기서는 Claude API 키를 새로 발급받는 방법을 설명한다. 이미 사용할 API 키를 가지고 있다면 이 단계는 건너뛰어도 좋다.
{: .prompt-tip }

<https://console.anthropic.com>에 접속하여 로그인한다. 만약 아직 계정이 없다면 회원가입을 먼저 진행해야 한다. 로그인하면 아래와 같은 대시보드 화면이 뜰 것이다.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

해당 화면에서 'Get API keys' 버튼을 클릭하면 다음과 같은 화면을 볼 수 있다.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) 나는 이미 생성해 놓은 키가 있기 때문에 `yunseo-secret-key`라는 이름의 키가 표시되는데, 계정을 처음 만들고 나서 API 키를 아직 발급받지 않은 상태라면 아마 보유하고 있는 키가 없을 것이다. 오른쪽 위의 'Create Key' 버튼을 클릭하여 새로운 키를 발급받으면 된다.

> 키 발급을 완료하면 화면에 본인의 API 키가 표시되는데, 해당 키는 이후 다시 확인할 수 없으므로 반드시 안전한 곳에 따로 잘 기록해 두어야 한다.
{: .prompt-warning }

### (권장) 환경 변수에 Claude API 키 등록
Python이나 Shell 스크립트에서 Claude API를 활용하려면 API 키를 불러와야 한다. 스크립트 자체에 API 키를 기록하는 방법도 있지만, GitHub 등에 업로드하거나 그 이외의 방법으로 다른 사람들과 공유해야 하는 스크립트라면 이 방법은 쓸 수 없다. 또한 스크립트 파일을 공유할 생각이 없었더라도, 의도치 않은 실수로 스크립트 파일이 유출될 수 있는데 만약 스크립트 파일에 API 키가 기록되어 있다면 API 키까지 같이 유출되는 사고가 발생할 위험이 있다. 따라서 API 키를 본인만이 사용하는 시스템의 환경변수에 등록해 두고 스크립트에서는 해당 환경변수를 불러오는 방식으로 활용하는 것을 권장한다. 아래에서는 UNIX 시스템 기준으로 시스템 환경 변수에 API 키를 등록하는 방법을 소개한다. Windows의 경우 웹 상에 다른 글을 참고하기 바란다.

1. 터미널에서 본인이 사용하는 쉘 종류에 맞게 `nano ~/.bashrc` 또는 `nano ~/.zshrc`를 입력하여 편집기를 실행한다.
2. 해당 파일 내용에 `export ANTHROPIC_API_KEY='your-api-key-here'`를 추가한다. 'your-api-key-here' 부분에 본인의 API 키를 대신 넣으면 되며, 반드시 '를 이용하여 감싸 주어야 함에 유의한다.
3. 변경 내용을 저장하고 편집기를 종료한다.
4. 터미널에서 `source ~/.bashrc` 또는 `source ~/.zshrc`를 실행하여 변경사항을 반영한다.

### 필요한 Python 패키지 설치
본인이 사용하는 Python 환경에 anthropic 패키지가 설치되어 있지 않다면 다음 명령으로 설치한다.
```bash
pip3 install anthropic
```
또한 다음 패키지들도 뒤에서 소개할 포스트 번역 스크립트를 사용하려면 필요하니, 다음 명령으로 설치 또는 업데이트한다.
```bash
pip3 install -U argparse tqdm
```

### Python 스크립트 작성
이 글에서 소개할 포스트 번역 스크립트는 다음의 3개 Python 스크립트 파일과 1개의 CSV 파일로 구성되어 있다.

- `compare_hash.py`: `_posts/ko`{: .filepath} 디렉터리 안에 있는 한국어 원문 포스트들의 SHA256 해시 값을 계산한 뒤 `hash.csv` 파일에 기록되어 있는 기존 해시 값과 비교하여 변경 혹은 새롭게 추가된 파일명의 리스트를 반환
- `hash.csv`: 기존 포스트 파일들의 SHA256 해시 값을 기록한 CSV 파일
- `prompt.py`: filepath, source_lang, target_lang 값을 입력받고 시스템 환경 변수에서 Claude API 키 값을 불러온 뒤, API를 호출하고 시스템 프롬프트로는 앞서 작성했던 프롬프트를, 사용자 프롬프트로는 'filepath'에 있는 번역할 포스트의 내용을 제출. 이후 Claude 3.5 Sonnet 모델로부터 응답(번역 결과물)을 받아 `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath} 경로에 텍스트 파일로 출력
- `translate_changes.py`: source_lang 문자열 변수와 'target_langs' 리스트 변수를 가지고 있으며, `compare_hash.py` 안의 `changed_files()` 함수를 호출하여 changed_files 리스트 변수를 반환받음. 만약 변경된 파일이 있다면 changed_files 리스트 안의 모든 파일, 그리고 target_langs 리스트 안의 모든 요소에 대한 이중 반복문을 실행하며, 해당 반복문 안에서 `prompt.py` 안의 `translate(filepath, source_lang, target_lang)` 함수를 호출하여 번역 작업을 수행하도록 함.

완성한 스크립트 파일의 내용은 GitHub의 [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) 리포지터리에서도 확인할 수 있다.

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
앞서 작성했던 프롬프트의 내용까지 포함하고 있어 파일 내용이 좀 긴 관계로, GitHub 리포지터리에 있는 소스 파일의 링크로 대체한다.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> 위의 링크에 있는 `prompt.py` 파일에서 `max_tokens`는 Context window 크기와 별개로 최대 출력 길이를 지정하는 변수이다. Claude API 사용 시 한번에 입력할 수 있는 Context window의 크기는 200k 토큰(약 68만 글자 정도의 분량)이지만, 그와 별개로 각 모델별로 지원하는 최대 출력 토큰 수가 정해져 있으니 API 활용 전에 [Anthropic 공식 문서](https://docs.anthropic.com/en/docs/about-claude/models)에서 미리 확인해 보는 것을 권장한다. 기존의 Claude 3 시리즈 모델들은 최대 4096토큰까지 출력이 가능했는데, 이 블로그의 글로 실험해 본 결과 대다수의 포스트에서는 문제가 없긴 했으나 개중 한글로 대략 8000자 이상의 좀 긴 분량의 포스트의 경우 몇몇 출력 언어에서 4096토큰을 초과하여 번역문 뒷부분이 잘리는 문제가 발생하였다. Claude 3.5 Sonnet의 경우 최대 출력 토큰 수가 2배인 8192로 늘었기 때문에 어지간해서는 이 최대 출력 토큰 수를 초과하여 문제가 되는 경우는 없었으며, 위 GitHub 리포지터리의 `prompt.py`에서도 `max_tokens=8192`로 지정해 두었다.
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

### Python 스크립트 사용 방법
Jekyll 블로그 기준으로, 포스트가 위치한 `/_posts`{: .filepath} 디렉터리 안에 [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) 언어 코드별로 `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}과 같이 하위 디렉터리를 둔다. 그리고 `/tools`{: .filepath} 디렉터리에 위에서 소개한 Python 스크립트들과 CSV 파일을 둔 뒤, 해당 위치에서 터미널을 열고 아래 명령을 실행한다.

```bash
python3 translate_changes.py
```

그러면 스크립트가 실행되면서 아래와 같은 화면이 출력될 것이다.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## 실사용기
상술한 것과 같이 Claude 3.5 API를 이용한 포스트 자동 번역을 이 블로그에 도입하고 나서 약 2개월 정도 사용 중이다. 대부분의 경우에는 따로 사람이 추가 개입할 필요 없이 뛰어난 품질의 번역문을 제공받을 수 있으며, 포스트를 다국어로 번역하여 올리고 나서 브라질이나 캐나다, 미국, 프랑스 등 한국 이외의 지역에서의 검색을 통한 Organic Search 트래픽이 실제로 유입되는 것을 확인하였다. 또한 블로그의 트래픽 유입뿐만 아니라 글 작성자 본인의 학습 측면에서 부가적인 장점도 있었는데, Claude가 영문 기준으로 상당히 매끄러운 글을 작성해 주기 때문에 GitHub Pages 리포지터리에 포스트를 Push하기 전 검토하는 과정에서 내가 작성한 한국어 원문의 특정 용어나 표현을 영어로는 어떤 식으로 표현하면 자연스러운지 확인할 수 있는 기회가 있다. 오직 이것만으로 충분한 영어 학습이 된다고 말하기엔 부족하겠지만, 일상적인 표현뿐만 아니라 학술적인 표현이나 용어에 대한 자연스러운 영문 표현을, 그 어떤 글보다도 익숙한 내가 직접 작성한 글을 예문 삼아, 별다른 추가적인 노력 없이도 자주 접할 수 있다는 것 또한 한국과 같은 비 영미권 지역 국가의 공대 학부생에게는 제법 장점으로 작용하는 듯 싶다.
