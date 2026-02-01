---
title: "Jak automaticky překládat posty pomocí Claude Sonnet 4 API (2) – psaní a nasazení automatizačního skriptu"
description: "Navrhneme prompt pro vícejazyčný překlad Markdown souborů a ukážeme automatizaci v Pythonu: napojení Anthropic/Gemini API, získání klíčů a použití skriptů pro překlad postů."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2/
---

## Úvod
Od doby, kdy jsem v červnu 12024 zavedl pro vícejazyčný překlad blogových postů Anthropic Claude 3.5 Sonnet API, jsem přes několik iterací vylepšování promptů a automatizačních skriptů a také přes upgrady verzí modelů tento překladový systém provozoval spokojeně téměř rok. V této sérii proto chci pokrýt důvody, proč jsem při zavádění zvolil model Claude Sonnet a později přidal Gemini 2.5 Pro, jak navrhovat prompty, a jak v Pythonu implementovat napojení na API a automatizaci.  
Série se skládá ze 2 článků a tento, který právě čtete, je druhý.
- 1. díl: [Představení modelů Claude Sonnet/Gemini 2.5 a důvody volby, prompt engineering](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- 2. díl: Psaní a nasazení Python automatizačního skriptu s využitím API (tento článek)

## Než začnete
Protože tento článek navazuje na [1. díl](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), pokud jste jej ještě nečetli, doporučuji nejdřív přečíst předchozí část.

## Hotový systémový prompt
Výsledek návrhu promptu, dokončený procesem popsaným [v 1. díle](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#navrh-promptu), vypadá následovně.

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

> U [nově přidané funkce inkrementálního překladu](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#120250704) používám mírně odlišný systémový prompt. Je tam hodně překryvu, takže jej sem nepíšu; pokud je potřeba, podívejte se přímo do souboru [`prompt.py`{: .filepath } v GitHub repozitáři](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py).
{: .prompt-tip }

## Napojení na API
### Vydání API klíče

> Tady vysvětluji, jak si nově vydat Anthropic nebo Gemini API klíč. Pokud už klíč máte, tuto část můžete přeskočit.
{: .prompt-tip }

#### Anthropic Claude
Přejděte na <https://console.anthropic.com> a přihlaste se do Anthropic Console účtu. Pokud účet ještě nemáte, musíte se nejdřív zaregistrovat. Po přihlášení by se měla zobrazit dashboard stránka jako níže.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

Na této obrazovce klikněte na tlačítko „Get API keys“ a uvidíte stránku jako následující.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) Protože už mám vytvořený klíč, zobrazuje se mi klíč pojmenovaný `yunseo-secret-key`. Pokud jste účet právě založili a ještě jste API klíč nevydali, nejspíš tam žádný klíč mít nebudete. Vpravo nahoře klikněte na „Create Key“ a vydejte nový klíč.

> Po dokončení vydání se na obrazovce zobrazí váš API klíč, ale později už jej nebude možné znovu zobrazit, takže si jej určitě bezpečně uložte někam stranou.
{: .prompt-warning }

#### Google Gemini
Gemini API lze spravovat v Google AI Studio. Přejděte na <https://aistudio.google.com/apikey> a přihlaste se Google účtem; zobrazí se dashboard jako níže.  
![Google AI Studio Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/get-api-key-google-ai-studio.png)

Na této obrazovce klikněte na „API 키 만들기“ a postupujte podle průvodce. Pokud vytvoříte Google Cloud projekt a přidružený platební účet a propojíte je, budete připraveni API klíč používat. Oproti Anthropic API je postup trochu složitější, ale nemělo by to být nic zásadního.

> Na rozdíl od Anthropic Console můžete u Google kdykoli svůj API klíč znovu zobrazit na dashboardu. ~~I když, i kdyby vám někdo vykradl Anthropic Console účet, dokud ochráníte samotný API klíč, dá se škoda omezit; ale když vám vykradou Google účet, budete mít mnohem naléhavější problémy než jen Gemini API klíč~~  
> Takže není nutné si klíč zvlášť zapisovat; místo toho si dobře zabezpečte svůj Google účet.
{: .prompt-tip }

### (Doporučeno) Uložení API klíče do proměnných prostředí
Aby šlo v Pythonu nebo shell skriptech používat Claude API, je potřeba API klíč načíst. Klíč lze sice natvrdo zapsat do skriptu, ale to je nepoužitelné, pokud skript chcete nahrát na GitHub nebo jej jakkoli sdílet. Navíc i když skript sdílet neplánujete, může dojít k nechtěnému úniku souboru; a pokud je v něm klíč, hrozí únik i klíče. Proto doporučuji uložit API klíč do proměnných prostředí v systému, který používáte, a ve skriptu načítat právě tyto proměnné. Níže je postup pro UNIX systémy; pro Windows si prosím najděte jiný návod na webu.

1. V terminálu podle použitého shellu spusťte editor příkazem `nano ~/.bashrc` nebo `nano ~/.zshrc`.
2. Pokud používáte Anthropic API, přidejte do souboru `export ANTHROPIC_API_KEY=your-api-key-here`. Část `your-api-key-here` nahraďte svým klíčem. Pokud používáte Gemini API, stejným způsobem přidejte `export GEMINI_API_KEY=your-api-key-here`.
3. Uložte změny a editor ukončete.
4. V terminálu spusťte `source ~/.bashrc` nebo `source ~/.zshrc`, aby se změny projevily.

### Instalace potřebných Python balíčků
Pokud v používaném Python prostředí nemáte nainstalované API knihovny, nainstalujte je následujícími příkazy.

#### Anthropic Claude
```bash
pip3 install anthropic
```

#### Google Gemini
```bash
pip3 install google-genai
```

#### Společné
Následující balíčky jsou také potřeba pro překladový skript, který popíšu níže, takže je nainstalujte nebo aktualizujte:
```bash
pip3 install -U argparse tqdm
```

### Psaní Python skriptu
Překladový systém popsaný v tomto článku je složen ze 3 Python skriptů a 1 CSV souboru.

- `compare_hash.py`{: .filepath}: spočítá SHA256 hash hodnoty korejských originálních postů v adresáři `_posts/ko`{: .filepath}, porovná je s existujícími hash hodnotami z `hash.csv`{: .filepath} a vrátí seznam názvů souborů, které se změnily nebo byly nově přidány
- `hash.csv`{: .filepath}: CSV soubor s uloženými SHA256 hash hodnotami existujících postů
- `prompt.py`{: .filepath}: přijme hodnoty filepath, source_lang, target_lang, načte z proměnných prostředí Claude API klíč, zavolá API, jako systémový prompt použije dříve vytvořený prompt a jako uživatelský prompt odešle obsah překladu z `filepath`. Následně přijme odpověď (překlad) z modelu Claude Sonnet 4 a uloží ji jako textový soubor do cesty `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath}: obsahuje řetězcovou proměnnou source_lang a list target_langs, zavolá funkci `changed_files()` ze `compare_hash.py`{: .filepath} a získá list changed_files. Pokud existují změněné soubory, provede dvojitou smyčku přes všechny soubory v changed_files i všechny jazyky v target_langs a uvnitř volá `translate(filepath, source_lang, target_lang)` z `prompt.py`{: .filepath}, čímž spustí překlad.

Hotové skripty lze také najít v GitHub repozitáři [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
Protože tento soubor obsahuje i plné znění dříve vytvořeného promptu a je tedy poměrně dlouhý, nahradím jej odkazem na zdroják v GitHub repozitáři.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> V souboru `prompt.py`{: .filepath} na odkazu výše je `max_tokens` proměnná, která (nezávisle na velikosti context window) určuje maximální délku výstupu. Při použití Claude API lze v jednom požadavku poslat context window o velikosti 200k tokenů (cca 680 tisíc znaků), ale zvlášť pro každý model existuje limit maximálního počtu výstupních tokenů; před použitím API doporučuji ověřit v [oficiální dokumentaci Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) podporované limity. Starší modely řady Claude 3 uměly vypsat maximálně 4096 tokenů; při testování na článcích tohoto blogu se u delších postů (zhruba 8000+ korejských znaků) u některých cílových jazyků objevoval problém, že překlad přesáhl 4096 tokenů a konec byl uříznut. U Claude 3.5 Sonnet se limit výstupu zdvojnásobil na 8192 tokenů, takže to obvykle problém nebyl, a od Claude 3.7 se podpora prodlouženého výstupu ještě výrazně zlepšila. V `prompt.py`{: .filepath} v uvedeném GitHub repozitáři je nastaveno `max_tokens=16384`.
{: .prompt-tip }

> U Gemini je maximální výstupní délka už dlouho relativně štědrá; u Gemini 2.5 Pro lze vypsat až 65536 tokenů, takže v praxi jen zřídka narazíte na limit. Podle [oficiální dokumentace Gemini API](https://ai.google.dev/gemini-api/docs/models#token-size) odpovídá 1 token u Gemini (pro angličtinu) zhruba 4 znakům a 100 tokenů je přibližně 60–80 anglických slov.
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

### Jak Python skripty používat
V rámci Jekyll blogu si pod adresář `/_posts`{: .filepath} udělejte podadresáře podle jazykových kódů [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php), např. `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath} atd. Do `/_posts/ko`{: .filepath} uložte korejský originál (nebo upravte ve skriptu proměnnou `source_lang` podle potřeby a uložte originál do odpovídajícího adresáře) a do `/tools`{: .filepath} uložte výše uvedené Python skripty a soubor `hash.csv`{: .filepath}. Poté v daném umístění otevřete terminál a spusťte:

```bash
python3 translate_changes.py
```

Po spuštění by se mělo v terminálu zobrazit něco jako následující.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

Pokud nezadáte žádnou volbu, poběží výchozí režim plného překladu. Pokud přidáte volbu `--incremental`, můžete použít inkrementální překlad.

```bash
python3 translate_changes.py --incremental
```

## Praktické zkušenosti
Jak jsem zmínil výše, automatický překlad postů pomocí Claude Sonnet API jsem na tomto blogu zavedl koncem června 12024 a od té doby jej průběžně vylepšuji a používám. Ve většině případů není potřeba další lidský zásah a výsledkem je přirozeně působící překlad. Po publikaci vícejazyčných verzí jsem navíc ověřil, že reálně začal přitékat poměrně výrazný organic search traffic z oblastí mimo Koreu, například z Brazílie, Kanady, USA, Francie nebo Japonska. Když se podívám na nahrané session záznamy, není neobvyklé, že návštěvníci, kteří přijdou přes přeloženou verzi, na stránce stráví několik minut až desítky minut. Vzhledem k tomu, že u očividně „strojově přeložených“ a kostrbatých textů lidé často stránku hned zavřou nebo si raději najdou anglickou verzi, to naznačuje, že kvalita překladu nepůsobí výrazně nepřirozeně ani z pohledu rodilých mluvčích.

Kromě přínosu v podobě návštěvnosti má tento systém i vedlejší výhodu z hlediska mého vlastního učení. LLM jako Claude nebo Gemini umí (zejména v angličtině) psát velmi plynule, takže při kontrole před Commit & Push do GitHub Pages repozitáře mám příležitost vidět, jaké anglické formulace jsou pro konkrétní korejské výrazy a obraty přirozené. Samozřejmě je to samo o sobě málo na to tvrdit, že jde o „dostatečné“ studium angličtiny, ale možnost často a bez extra úsilí narážet na přirozené akademické obraty a terminologii — navíc na příkladech textů, které jsem napsal já sám a znám je nejlépe — je pro studenta technického oboru v zemi mimo anglofonní prostředí (jako je Korea) docela znatelná výhoda.
