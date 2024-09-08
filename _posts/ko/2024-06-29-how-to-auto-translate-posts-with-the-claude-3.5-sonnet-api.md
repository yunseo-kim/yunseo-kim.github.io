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
## 들어가며
최근에 블로그 포스트의 다국어 번역을 위해 Anthropic의 Claude 3.5 Sonnet API를 도입하였다. 이에 도입 과정에서 Claude 3.5 Sonnet API를 선택한 이유와 프롬프트 디자인 방법, 그리고 Python 스크립트를 통한 API 연동 및 자동화 구현 방법을 다루고자 한다.

## About Claude 3.5 Sonnet
Claude 3 시리즈 모델은 모델 크기에 따라 Haiku, Sonnet, 그리고 Opus 버전이 제공된다.  
![Claude 3 모델 티어 구분](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> 이미지 출처: [Anthropic Claude API 공식 웹페이지](https://www.anthropic.com/api)

그리고 한국 시각으로 2024년 6월 21일, Anthropic에서 최신 언어모델인 [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)를 공개하였다. Anthropic의 발표에 의하면 기존의 Claude 3 Sonnet와 동일한 비용과 속도로 Claude 3 Opus를 능가하는 추론 성능을 보인다고 하며, 대체로 작문과 언어 추론, 다국어 이해 및 번역 분야에서 경쟁 모델인 GPT-4 대비 강점을 보인다는 평이 지배적이다.  
![Claude 3.5 Sonnet 소개 이미지](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet 성능 벤치마크 결과](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> 이미지 출처: [Anthropic 홈페이지](https://www.anthropic.com/news/claude-3-5-sonnet)

## 포스트 번역을 위해 Claude 3.5를 도입한 이유
굳이 Claude 3.5나 GPT-4와 같은 언어모델이 아니더라도 구글 번역이나 DeepL과 같은 기존의 상용 번역 API가 존재한다. 그럼에도 번역 목적으로 LLM을 사용하기로 결정한 이유는 다른 상용 번역 서비스와 달리 사용자가 프롬프트 디자인을 통해 모델에게 글의 작성 목적이나 주요 주제 등 본문 외에도 추가적인 맥락 정보나 요구사항을 제공할 수 있고, 모델은 이에 맞추어 문맥을 고려한 번역을 제공할 수 있기 때문이다. DeepL이나 구글 번역도 대체로 뛰어난 번역 품질을 보이는 편이지만, 글의 주제나 전체적인 맥락을 잘 파악하지 못하는 한계 때문에 일상적인 회화가 아닌 전문적인 주제의 긴 글을 번역하도록 요청했을 때는 상대적으로 번역 결과물이 부자연스러운 경우가 있었다. 특히나 Claude는 상술하였듯 경쟁 모델인 GPT-4 대비 작문, 언어 추론, 다국어 이해 및 번역 분야에서 상대적으로 더 뛰어나다는 평이 많기에, 이 블로그에 기재하는 공학 관련 글들을 여러 언어로 번역하는 작업에 적합하다고 판단하였다.

## 프롬프트 디자인
### 프롬프트 디자인의 기본 원칙
언어모델로부터 목적에 부합하는 만족스러운 결과물을 얻기 위해서는 그에 맞는 적절한 프롬프트를 제공해야 한다. 프롬프트 디자인이라고 하면 뭔가 막막하게 느껴질 수 있지만, 사실 '뭔가를 잘 요청하는 방법'이란 상대방이 언어모델이든 사람이든 크게 다르지 않으므로 이와 같은 관점에서 접근하면 별로 어렵지 않다. 육하원칙에 따라 현 상황 및 요청사항을 명확히 설명하고, 필요하다면 몇 가지 구체적인 예시를 덧붙이는 것도 좋다. 프롬프트 디자인에 관한 수많은 팁과 기법들이 존재하지만, 대부분은 상술한 기본 원칙에서 파생되는 것들이다.

### 역할 부여 및 상황 설명(누가, 왜)
제일 먼저 Claude 3.5에게 *'기술 분야 전문 번역가(professional technical translator)'* 라는 역할을 부여하고, *"주로 수학이나 물리학, 데이터 과학에 관한 글을 기고하는 공학 블로거"* 라는 사용자에 관한 맥락 정보를 제공하였다.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### 큰 틀에서의 요청사항 전달(무엇을)
다음으로, 사용자로부터 제공된 마크다운 형식의 글을 {source_lang}에서 {target_lang}으로 형식을 유지하면서 번역하도록 요청하였다. 
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Claude API 호출 시, 프롬프트의 {source_lang}과 {target_lang} 자리에는 Python 스크립트의 f-string 기능을 통해 번역 출발언어와 도착언어 변수가 각각 들어간다.
{: .prompt-info }

### 요구사항 구체화 및 예시(어떻게)
간단한 작업이라면 앞선 단계까지만 해도 충분히 원하는 결과를 얻는 경우도 있지만, 복잡한 작업을 요구하는 경우에는 추가적인 설명이 필요할 수 있다. 이 경우에는 다음과 같은 조건을 추가하였다.

#### YAML front matter의 처리
Jekyll 블로그에 업로드하기 위해 markdown으로 작성한 포스트의 첫 부분에 위치한 YAML front matter에는 'title'과 'description', 'categories', 그리고 'tags' 정보를 기록한다. 가령, 이 글의 YAML front matter는 다음과 같다.

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

그런데 포스트를 번역할 때 제목(title)과 설명(description) 태그는 다국어로 번역해야 하나, 포스트 URL의 일관성을 위해서는 카테고리(categories)와 태그(tags) 이름은 번역하지 않고 영문 그대로 놔두는 것이 유지관리에 용이하다. 따라서 아래와 같은 지시를 내려서 'title'과 'description' 이외의 태그는 번역하지 않도록 하였다. Claude가 YAML front matter에 관한 정보는 이미 학습하여 알고 있을 것이므로, 이 정도만 설명해도 대부분의 경우 충분하다.
> In the provided markdown formatted text, do not translate the YAML front matter except for the 'title' and 'description' tags.

#### 제공된 원문이 출발언어가 아닌 다른 언어를 포함하는 경우의 처리
한국어로 원문을 작성할 때, 어떤 개념의 정의를 처음 소개하거나 몇몇 전문용어를 사용하는 경우 '*중성자 감쇠 (Neutron Attenuation)*'와 같이 괄호 안에 영문 표현을 같이 기재하는 경우가 종종 있다. 이러한 표현을 번역하는 경우 어떨 땐 괄호를 살리고, 또 어떨 땐 괄호 안에 기재된 영문을 누락하는 등 번역 방식이 일관되지 않은 문제가 있어 아래 문장을 프롬프트에 추가하였다.
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### 다른 포스트로 연결되는 링크의 처리
몇몇 포스트는 다른 포스트로 연결되는 링크를 포함하는데, URL의 경로 부분까지 번역해야 하는 대상으로 해석해서 바꾸는 바람에 내부 링크가 깨지는 문제가 자주 발생하였다. 해당 문제는 프롬프트에 이 문장을 추가하여 해결하였다.
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### 번역 결과물만을 응답으로 출력할 것
마지막으로, 응답 시 다른 말을 덧붙이지 않고 오직 번역 결과물만을 출력하도록 다음 문장을 제시한다.
> The output should only contain the translated text.

### 완성한 프롬프트
위의 단계를 거친 프롬프트 디자인 결과물은 다음과 같다.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.

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
