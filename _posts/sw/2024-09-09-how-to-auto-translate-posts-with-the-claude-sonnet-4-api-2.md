---
title: "Jinsi ya Kutafsiri Machapisho Kiotomatiki kwa Claude Sonnet 4 API (2) - Kuandika na Kutumia Skripti ya Otomatiki"
description: "Makala hii inaeleza jinsi ya kubuni prompt kwa tafsiri ya lugha nyingi ya faili za maandishi ya Markdown, na jinsi ya kuendesha kazi hiyo kiotomatiki kwa Python kwa kutumia funguo za API za Anthropic/Gemini pamoja na prompt uliyoandika. Hii ni sehemu ya pili ya mfululizo huu, ikitambulisha utoaji na uunganishaji wa API pamoja na uandishi wa skripti ya Python."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2/
---

## Utangulizi
Baada ya kuanzisha Anthropic Claude 3.5 Sonnet API mnamo Juni 12024 kwa ajili ya tafsiri ya lugha nyingi ya machapisho ya blogu, nimekuwa nikiendesha mfumo huo wa tafsiri kwa kuridhika kwa karibu mwaka mmoja kupitia maboresho kadhaa ya prompt na skripti za otomatiki, pamoja na masasisho ya matoleo ya modeli. Kwa hivyo, katika mfululizo huu ningependa kueleza sababu za kuchagua modeli ya Claude Sonnet wakati wa kuanzisha mfumo huo na baadaye kuongeza Gemini 2.5 Pro, pamoja na mbinu ya kubuni prompt, na jinsi ya kutekeleza uunganishaji wa API na otomatiki kwa kutumia skripti ya Python.  
Mfululizo huu una makala 2, na unayosoma sasa ni ya pili.
- Sehemu ya 1: [Utangulizi wa modeli za Claude Sonnet/Gemini 2.5 na sababu za kuzichagua, uhandisi wa prompt](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- Sehemu ya 2: Kuandika na kutumia skripti ya otomatiki ya Python kwa kutumia API (makala hii)

## Kabla ya Kuanza
Kwa kuwa makala hii inaendelea kutoka [Sehemu ya 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), ikiwa bado hujaisoma, ninapendekeza uanze na makala iliyotangulia.

## System Prompt Iliyokamilishwa
Matokeo ya muundo wa prompt yaliyokamilika kupitia [mchakato ulioelezwa katika Sehemu ya 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#ubunifu-wa-prompt) ni kama ifuatavyo.

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
or "```markdown" or something of that nature!!</important>
```

> Kwa upande wa [kipengele kipya cha tafsiri ya nyongeza](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#120250704), system prompt tofauti kidogo hutumika. Kwa kuwa kuna sehemu nyingi zinazofanana, sitaandika hapa; ikiwa unahitaji, tafadhali angalia moja kwa moja yaliyomo ndani ya [`prompt.py`{: .filepath } katika hazina ya GitHub](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py).
{: .prompt-tip }

## Uunganishaji wa API
### Kutoa API Key

> Hapa nitaeleza jinsi ya kutoa API key mpya ya Anthropic au Gemini. Ikiwa tayari unayo API key utakayotumia, unaweza kuruka hatua hii.
{: .prompt-tip }

#### Anthropic Claude
Nenda kwenye <https://console.anthropic.com> na uingie kwa akaunti yako ya Anthropic Console. Ikiwa bado huna akaunti ya Anthropic Console, utahitaji kujisajili kwanza. Ukishaingia, utaona dashibodi kama ilivyo hapa chini.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

Ukibofya kitufe cha 'Get API keys' kwenye skrini hiyo, utaona ukurasa kama huu ufuatao.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) Kwa kuwa mimi tayari nina key niliyounda mapema, key yenye jina `yunseo-secret-key` inaonekana. Ikiwa umetengeneza akaunti kwa mara ya kwanza na bado hujatoa API key, huenda usiwe na key yoyote. Bofya kitufe cha 'Create Key' kilicho juu kulia ili kutoa key mpya.

> Ukishamaliza kutoa key, API key yako itaonyeshwa kwenye skrini, lakini hutaweza kuiona tena baadaye, hivyo lazima uiandike na kuihifadhi mahali salama.
{: .prompt-warning }

#### Google Gemini
Gemini API inaweza kusimamiwa katika Google AI Studio. Nenda kwenye <https://aistudio.google.com/apikey> na uingie kwa akaunti yako ya Google; kisha dashibodi kama hii itaonyeshwa.  
![Google AI Studio Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/get-api-key-google-ai-studio.png)

Kutoka hapo, bofya kitufe cha 'API 키 만들기' na fuata maelekezo. Ukisha tengeneza na kuunganisha mradi wa Google Cloud pamoja na akaunti ya malipo ya kutumia, utakuwa tayari kutumia API key. Ingawa utaratibu huu ni mgumu kidogo kuliko Anthropic API, kwa ujumla haupaswi kuwa wa shida kubwa.

> Tofauti na Anthropic Console, unaweza kuona API key zako wakati wowote kwenye dashibodi. ~~Kwa kweli, hata kama akaunti ya Anthropic Console ingevamiwa, mradi API key iko salama madhara yangeweza kupunguzwa; lakini akaunti ya Google ikivamiwa, Gemini API key haitakuwa hata tatizo la pekee la haraka~~  
> Kwa hiyo hakuna haja ya kuiandika API key kando, lakini badala yake hakikisha usalama wa akaunti yako ya Google unadumishwa vizuri.
{: .prompt-tip }

### (Inapendekezwa) Kusajili API key katika environment variables
Ili kutumia Claude API katika Python au Shell script, unahitaji kupakia API key. Kuna njia ya kui-hardcode API key ndani ya skripti yenyewe, lakini njia hiyo haiwezekani ikiwa ni skripti unayotaka kupakia GitHub au kushiriki na watu wengine kwa namna yoyote ile. Aidha, hata kama hukukusudia kushiriki faili ya skripti, inaweza kuvuja kwa bahati mbaya; na ikiwa API key imeandikwa ndani ya skripti, basi pia kuna hatari ya API key kuvuja pamoja nayo. Kwa hiyo inapendekezwa usajili API key katika environment variable ya mfumo wako binafsi, kisha skripti yako ivute environment variable hiyo inapohitajika. Hapa chini nitaeleza jinsi ya kusajili API key katika system environment variables kwa mifumo ya UNIX. Kwa Windows, tafadhali rejea makala nyingine mtandaoni.

1. Kwenye terminal, andika `nano ~/.bashrc` au `nano ~/.zshrc` kulingana na aina ya shell unayotumia ili kufungua mhariri.
2. Ukiwa unatumia Anthropic API, ongeza `export ANTHROPIC_API_KEY=your-api-key-here` kwenye faili husika. Badili sehemu ya 'your-api-key-here' kwa API key yako mwenyewe. Kwa Gemini API, ongeza `export GEMINI_API_KEY=your-api-key-here` kwa njia hiyo hiyo.
3. Hifadhi mabadiliko na ufunge mhariri.
4. Endesha `source ~/.bashrc` au `source ~/.zshrc` kwenye terminal ili kutumia mabadiliko hayo.

### Kusakinisha Python packages zinazohitajika
Ikiwa maktaba ya API haijasakinishwa katika mazingira yako ya Python, sakinisha kwa amri zifuatazo.

#### Anthropic Claude
```bash
pip3 install anthropic
```

#### Google Gemini
```bash
pip3 install google-genai
```

#### Za Pamoja
Zaidi ya hayo, packages zifuatazo pia zinahitajika ili kutumia skripti ya kutafsiri machapisho itakayoelezwa baadaye, kwa hiyo zisakinishe au zisasishwe kwa amri hii.
```bash
pip3 install -U argparse tqdm
```

### Kuandika Skripti ya Python
Skripti ya kutafsiri machapisho itakayowasilishwa katika makala hii ina faili 3 za skripti za Python na faili 1 ya CSV kama ifuatavyo.

- `compare_hash.py`{: .filepath}: Hukokotoa hash za SHA256 za machapisho ya Kikorea ndani ya saraka ya `_posts/ko`{: .filepath}, kisha huzilinganisha na hash zilizopo kwenye faili ya `hash.csv`{: .filepath} na kurudisha orodha ya majina ya faili yaliyobadilishwa au kuongezwa upya
- `hash.csv`{: .filepath}: Faili ya CSV inayohifadhi hash za SHA256 za faili za machapisho yaliyopo
- `prompt.py`{: .filepath}: Hupokea filepath, source_lang, na target_lang, kisha hupakia API key ya Claude kutoka kwenye system environment variable, huita API, na hutumia prompt uliotayarisha awali kama system prompt na yaliyomo kwenye chapisho la kutafsiri lililo kwenye 'filepath' kama user prompt. Baadaye hupokea majibu (matokeo ya tafsiri) kutoka kwa modeli ya Claude Sonnet 4 na kuyaandika kama faili ya maandishi kwenye njia ya `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath}: Ina string variable ya source_lang na list variable ya 'target_langs', kisha huita kazi ya `changed_files()` ndani ya `compare_hash.py`{: .filepath} na kupata list variable ya changed_files. Ikiwa kuna faili zilizobadilika, huendesha nested loop juu ya faili zote ndani ya changed_files na vipengele vyote ndani ya target_langs, na ndani ya loop hiyo huita kazi ya `translate(filepath, source_lang, target_lang)` ndani ya `prompt.py`{: .filepath} ili kutekeleza tafsiri.

Unaweza pia kuona yaliyomo ya faili hizi za skripti zilizokamilika katika hazina ya GitHub ya [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
Kwa kuwa faili hii pia inajumuisha yaliyomo ya prompt niliyoandika hapo awali, ni ndefu kidogo, kwa hiyo nitaibadilisha kwa kiungo cha faili ya source kilicho kwenye hazina ya GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> Katika faili ya `prompt.py`{: .filepath} kwenye kiungo hicho hapo juu, `max_tokens` ni kigezo kinachobainisha urefu wa juu wa matokeo ya kutoka, tofauti na ukubwa wa context window. Kwa kutumia Claude API, context window inayoweza kuingizwa kwa mkupuo mmoja ni tokeni 200k (takribani herufi 680,000), lakini tofauti na hilo, kila modeli ina kikomo chake cha juu cha output tokens, kwa hiyo ninapendekeza ukihakiki mapema katika [nyaraka rasmi za Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) kabla ya kutumia API. Modeli za awali za mfululizo wa Claude 3 ziliweza kutoa hadi tokeni 4096, lakini nilipojaribu kwa machapisho ya blogu hii, kwa makala ndefu za Kikorea zenye takribani zaidi ya herufi 8000, kulikuwa na tatizo katika baadhi ya lugha za matokeo ambapo tafsiri ilikatika mwishoni kwa sababu ilizidi tokeni 4096. Kwa Claude 3.5 Sonnet, idadi ya juu ya output tokens iliongezwa mara mbili hadi 8192, kwa hiyo kwa kawaida tatizo hilo halikutokea, na kuanzia Claude 3.7 modeli hiyo iliboreshwa zaidi ili kusaidia matokeo marefu zaidi. Katika `prompt.py`{: .filepath} ya hazina hiyo ya GitHub, `max_tokens=16384` imewekwa.
{: .prompt-tip }

> Kwa upande wa Gemini, tangu zamani imekuwa na kiwango kikubwa cha juu cha output tokens; kwa Gemini 2.5 Pro, inaweza kutoa hadi tokeni 65536, hivyo kwa kawaida hakuna uwezekano mkubwa wa kuzidi kikomo hicho. Kulingana na [nyaraka rasmi za Gemini API](https://ai.google.dev/gemini-api/docs/models#token-size), tokeni 1 katika modeli za Gemini ni takribani herufi 4 za Kiingereza, na tokeni 100 ni karibu maneno 60-80 ya Kiingereza.
{: .prompt-tip }

#### translate_changes.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "tqdm",
#     "argparse",
# ]
# ///
import sys
import os
import subprocess
from tqdm import tqdm
import compare_hash
import prompt

def is_valid_file(filename):
    # 제외할 파일 패턴들
    excluded_patterns = [
        '.DS_Store',  # macOS 시스템 파일
        '~',          # 임시 파일
        '.tmp',       # 임시 파일
        '.temp',      # 임시 파일
        '.bak',       # 백업 파일
        '.swp',       # vim 임시 파일
        '.swo'        # vim 임시 파일
    ]
    
    # 파일명이 제외 패턴 중 하나라도 포함하면 False 반환
    return not any(pattern in filename for pattern in excluded_patterns)

posts_dir = '../_posts/'
source_lang = "Korean"
target_langs = ["English", "Japanese", "Taiwanese Mandarin", "Spanish", "Brazilian Portuguese", "French", "German"]
source_lang_code = "ko"
target_lang_codes = ["en", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]

def get_git_diff(filepath):
    """Get the diff of the file using git"""
    try:
        # Get the diff of the file
        result = subprocess.run(
            ['git', 'diff', '--unified=0', '--no-color', '--', filepath],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Error getting git diff: {e}")
        return None

def translate_incremental(filepath, source_lang, target_lang, model):
    """Translate only the changed parts of a file using git diff"""
    # Get the git diff
    diff_output = get_git_diff(filepath)
    # print(f"Diff output: {diff_output}")
    if not diff_output:
        print(f"No changes detected or error getting diff for {filepath}")
        return
    
    # Call the translation function with the diff
    prompt.translate_with_diff(filepath, source_lang, target_lang, diff_output, model)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Translate markdown files with optional incremental updates')
    parser.add_argument('--incremental', action='store_true', 
                       help='Only translate changed parts of files using git diff')
    args, _ = parser.parse_known_args()
    
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
    
    # Outer loop: Progress through changed files
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        
        # Inner loop: Progress through target languages
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            model = "gemini-2.5-pro" if target_lang in ["English", "Taiwanese Mandarin", "German"] else "claude-sonnet-4-20250514"
            if args.incremental:
                translate_incremental(filepath, source_lang, target_lang, model)
            else:
                prompt.translate(filepath, source_lang, target_lang, model)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### Jinsi ya Kutumia Skripti ya Python
Kwa blogu ya Jekyll, ndani ya saraka ya `/_posts`{: .filepath}, weka saraka ndogo kwa kila msimbo wa lugha wa [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php), kama vile `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, na `/_posts/pt-BR`{: .filepath}. Kisha weka maandishi asilia ya Kikorea katika saraka ya `/_posts/ko`{: .filepath} (au, baada ya kurekebisha variable ya `source_lang` katika skripti ya Python kulingana na mahitaji yako, weka maandishi asilia ya lugha hiyo katika saraka inayolingana), na weka skripti za Python zilizoelezwa hapo juu pamoja na faili ya `hash.csv`{: .filepath} ndani ya saraka ya `/tools`{: .filepath}. Baada ya hapo, fungua terminal katika eneo hilo na endesha amri ifuatayo.

```bash
python3 translate_changes.py
```

Basi skripti itaendeshwa na utaona skrini kama hizi hapa chini.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

Usipobainisha option yoyote, itafanya kazi katika hali ya chaguomsingi ya tafsiri kamili, na ukibainisha option ya `--incremental`, unaweza kutumia kipengele cha tafsiri ya nyongeza.

```bash
python3 translate_changes.py --incremental
```

## Uzoefu wa Matumizi Halisi
Kama nilivyotaja awali, niliingiza tafsiri ya kiotomatiki ya machapisho kwa kutumia Claude Sonnet API kwenye blogu hii mwishoni mwa Juni 12024, na tangu hapo nimekuwa nikiitumia huku nikiiboresha kila mara. Mara nyingi, ninaweza kupata tafsiri za asili na laini bila kuhitaji uingiliaji wa ziada wa binadamu. Baada ya kuchapisha tafsiri za lugha nyingi za machapisho, nilithibitisha kuwa trafik ya Organic Search kutoka maeneo ya nje ya Korea kama vile Brazil, Kanada, Marekani, Ufaransa, na Japani iliingia kwa kiwango kikubwa. Zaidi ya hayo, nikikagua session zilizorekodiwa, si nadra kuona wageni waliokuja kupitia tafsiri hizo wakibaki kwa dakika kadhaa hadi makumi ya dakika. Kwa kawaida, ikiwa maudhui ya ukurasa wa wavuti yanaonekana wazi kuwa tafsiri ya mashine iliyo ngumu na isiyo ya asili, watu hufunga ukurasa au kutafuta toleo la Kiingereza badala yake; kwa hivyo hali hii inadokeza kwamba ubora wa tafsiri hizi hauonekani kuwa wa ajabu sana hata kwa viwango vya wasemaji asilia. Pia kulikuwa na faida ya ziada si tu kwa upande wa kuleta trafik kwenye blogu, bali pia kwa upande wa kujifunza kwangu binafsi kama mwandishi. Kwa kuwa LLM kama Claude au Gemini zinaweza kuandika maandishi ya Kiingereza kwa ulaini mkubwa, wakati wa kuyapitia kabla ya kufanya Commit & Push ya chapisho kwenye hazina ya GitHub Pages, ninapata fursa ya kuona ni kwa namna gani istilahi au misemo fulani niliyoandika katika maandishi asilia ya Kikorea inaweza kusemwa kwa Kiingereza kwa asili zaidi. Ingawa haitoshi kusema kuwa hili peke yake ni mafunzo kamili ya Kiingereza, ukweli kwamba naweza kukutana mara kwa mara, bila juhudi ya ziada, na mifano ya misemo ya asili ya Kiingereza si tu ya mazungumzo ya kila siku bali pia ya kitaaluma na ya istilahi, nikitumia kama mifano maandishi niliyoyaandika mwenyewe na ninayoyafahamu kuliko maandishi mengine yoyote, unaonekana kuwa faida kubwa kwa mwanafunzi wa shahada ya kwanza wa uhandisi katika nchi isiyo ya ulimwengu wa Kiingereza kama Korea.
