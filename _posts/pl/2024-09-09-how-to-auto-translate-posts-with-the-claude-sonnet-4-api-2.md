---
title: "Jak automatycznie tłumaczyć posty za pomocą API Claude Sonnet 4 (2) — pisanie i wdrożenie skryptu automatyzacji"
description: "Projekt promptu do wielojęzycznych tłumaczeń plików Markdown oraz automatyzacja w Pythonie: użycie kluczy API Anthropic/Gemini, integracja i uruchamianie skryptów tłumaczących posty (część 2 serii)."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2/
---

## Wprowadzenie
Po wdrożeniu w czerwcu 12024 roku API Claude 3.5 Sonnet od Anthropic do wielojęzycznego tłumaczenia wpisów na blogu, przez kilkanaście kolejnych miesięcy satysfakcjonująco utrzymuję ten system, przechodząc przez wiele iteracji usprawnień promptów i skryptów automatyzacji oraz aktualizacji wersji modeli. W tej serii chcę omówić powody wyboru modeli Claude Sonnet oraz późniejszego dodania Gemini 2.5 Pro, metody projektowania promptów, a także sposób integracji z API i implementacji automatyzacji w Pythonie.  
Seria składa się z dwóch wpisów, a tekst, który czytasz, jest drugim z nich.
- Część 1: [Wprowadzenie do modeli Claude Sonnet/Gemini 2.5 i powody wyboru, prompt engineering](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- Część 2: Pisanie i wdrożenie skryptu automatyzacji w Pythonie z użyciem API (ten wpis)

## Zanim zaczniesz
Ten wpis jest kontynuacją [części 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), więc jeśli jeszcze jej nie czytałeś(-aś), polecam najpierw zacząć od poprzedniego wpisu.

## Ukończony prompt systemowy
Efektem projektu promptu, ukończonego w procesie opisanym [w części 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#projektowanie-promptu), jest następujący rezultat.

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

> W przypadku [nowo dodanej funkcji tłumaczenia przyrostowego](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#120250704) używam nieco innego promptu systemowego. Wiele fragmentów się powtarza, więc nie będę go tutaj przepisywać; w razie potrzeby sprawdź bezpośrednio zawartość pliku [repozytorium GitHub `prompt.py`{: .filepath }](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py).
{: .prompt-tip }

## Integracja z API
### Wydanie klucza API

> Tutaj opisuję, jak uzyskać nowy klucz API Anthropic lub Gemini. Jeśli masz już klucz, którego będziesz używać, możesz pominąć ten krok.
{: .prompt-tip }

#### Anthropic Claude
Wejdź na <https://console.anthropic.com> i zaloguj się do Anthropic Console. Jeśli nie masz jeszcze konta, najpierw musisz się zarejestrować. Po zalogowaniu zobaczysz panel (dashboard) podobny do poniższego.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

Na tym ekranie kliknij przycisk „Get API keys”, a zobaczysz ekran podobny do poniższego.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) Ponieważ mam już utworzony klucz, widnieje tu klucz o nazwie `yunseo-secret-key`. Jeśli dopiero co założyłeś(-aś) konto i jeszcze nie wygenerowałeś(-aś) klucza API, prawdopodobnie nie będziesz mieć żadnego klucza na liście. Kliknij przycisk „Create Key” w prawym górnym rogu, aby utworzyć nowy klucz.

> Po zakończeniu generowania klucza na ekranie zostanie wyświetlony Twój klucz API, ale nie da się go potem ponownie podejrzeć — koniecznie zapisz go w bezpiecznym miejscu.
{: .prompt-warning }

#### Google Gemini
Gemini API można zarządzać w Google AI Studio. Wejdź na <https://aistudio.google.com/apikey> i zaloguj się kontem Google — zobaczysz panel jak poniżej.  
![Google AI Studio Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/get-api-key-google-ai-studio.png)

Kliknij przycisk „API 키 만들기” i postępuj zgodnie z instrukcją. Po utworzeniu i podpięciu projektu Google Cloud oraz konta rozliczeniowego klucz API będzie gotowy do użycia. Procedura jest nieco bardziej złożona niż w przypadku Anthropic API, ale nadal nie powinna sprawić większych trudności.

> W przeciwieństwie do Anthropic Console, tutaj możesz w dowolnym momencie podejrzeć swoje klucze API w panelu. ~~Zresztą nawet jeśli ktoś przejmie konto Anthropic Console, da się ograniczyć szkody, o ile sam klucz API pozostanie bezpieczny; natomiast gdy ktoś przejmie konto Google, to Gemini API key jest najmniejszym z Twoich problemów~~  
> Dlatego nie musisz osobno zapisywać klucza API — zamiast tego dbaj o bezpieczeństwo konta Google.
{: .prompt-tip }

### (Zalecane) Dodanie klucza API do zmiennych środowiskowych
Aby używać Claude API w Pythonie lub skryptach shellowych, trzeba wczytać klucz API. Można go zahardkodować w samym skrypcie, ale jeśli skrypt ma trafić na GitHub lub być udostępniany innym w jakiejkolwiek formie, to takie podejście odpada. Nawet jeśli nie planujesz udostępniać skryptu, plik może wyciec przez przypadek — a wtedy wycieknie również klucz API. Dlatego zalecam zapisanie klucza API w zmiennych środowiskowych systemu, z którego korzystasz, i wczytywanie go w skrypcie. Poniżej pokazuję sposób dla systemów UNIX. W przypadku Windows odsyłam do innych materiałów w sieci.

1. W terminalu uruchom edytor, zależnie od używanej powłoki: `nano ~/.bashrc` albo `nano ~/.zshrc`.
2. Jeśli używasz Anthropic API, dopisz `export ANTHROPIC_API_KEY=your-api-key-here`. W miejscu `your-api-key-here` wstaw swój klucz. Jeśli używasz Gemini API, analogicznie dopisz `export GEMINI_API_KEY=your-api-key-here`.
3. Zapisz zmiany i zamknij edytor.
4. W terminalu uruchom `source ~/.bashrc` albo `source ~/.zshrc`, aby zastosować zmiany.

### Instalacja wymaganych pakietów Pythona
Jeśli w Twoim środowisku Pythona nie ma jeszcze bibliotek API, zainstaluj je poleceniami:

#### Anthropic Claude
```bash
pip3 install anthropic
```

#### Google Gemini
```bash
pip3 install google-genai
```

#### Wspólne
Ponadto do skryptu tłumaczącego posty, który opisuję dalej, będą potrzebne też poniższe pakiety — zainstaluj je lub zaktualizuj:
```bash
pip3 install -U argparse tqdm
```

### Pisanie skryptów w Pythonie
Skrypt tłumaczący posty opisany w tym wpisie składa się z 3 plików Python i 1 pliku CSV:

- `compare_hash.py`{: .filepath}: oblicza hashe SHA256 dla koreańskich postów źródłowych w katalogu `_posts/ko`{: .filepath}, porównuje je z dotychczasowymi hashami zapisanymi w `hash.csv`{: .filepath} i zwraca listę nazw plików, które zmieniły się lub zostały dodane
- `hash.csv`{: .filepath}: plik CSV z dotychczasowymi hashami SHA256 dla istniejących postów
- `prompt.py`{: .filepath}: przyjmuje filepath, source_lang, target_lang, wczytuje klucz Claude API ze zmiennych środowiskowych, wywołuje API; jako prompt systemowy przekazuje wcześniej zaprojektowany prompt, a jako prompt użytkownika — treść posta do tłumaczenia z `filepath`. Następnie odbiera odpowiedź (wynik tłumaczenia) od modelu Claude Sonnet 4 i zapisuje ją do pliku tekstowego w ścieżce `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`{: .filepath}: zawiera zmienną string `source_lang` oraz listę `target_langs`. Wywołuje funkcję `changed_files()` z `compare_hash.py`{: .filepath}, otrzymując listę `changed_files`. Jeśli są zmienione pliki, wykonuje podwójną pętlę po wszystkich plikach z `changed_files` oraz po wszystkich językach z `target_langs`, i w tej pętli wywołuje `translate(filepath, source_lang, target_lang)` z `prompt.py`{: .filepath}, aby uruchomić tłumaczenie.

Zawartość gotowych skryptów można też sprawdzić w repozytorium GitHub: [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools).

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
Ponieważ plik zawiera także treść wcześniej przygotowanego promptu i przez to jest dość długi, zamiast wklejać go tutaj, podaję link do kodu w repozytorium GitHub.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> W pliku `prompt.py`{: .filepath} z linku powyżej `max_tokens` to zmienna określająca maksymalną długość wyjścia niezależnie od rozmiaru context window. W Claude API można jednorazowo podać context window o rozmiarze 200k tokenów (ok. 680 tys. znaków), ale niezależnie od tego każdy model ma własny limit maksymalnej liczby tokenów wyjściowych — przed użyciem API warto to sprawdzić w [oficjalnej dokumentacji Anthropic](https://docs.anthropic.com/en/docs/about-claude/models). Starsze modele z serii Claude 3 pozwalały na maksymalnie 4096 tokenów wyjścia; w moich testach na wpisach z tego bloga, przy dłuższych postach (w przybliżeniu powyżej ~8000 znaków po koreańsku) w niektórych językach wynik tłumaczenia przekraczał 4096 tokenów i końcówka była ucinana. W Claude 3.5 Sonnet limit wyjścia wzrósł 2× do 8192, więc w praktyce rzadko było to problemem; od Claude 3.7 wspierane są jeszcze dłuższe wyjścia. W `prompt.py`{: .filepath} w tym repozytorium ustawiono `max_tokens=16384`.
{: .prompt-tip }

> W przypadku Gemini maksymalna liczba tokenów wyjściowych od dawna jest dość duża; dla Gemini 2.5 Pro można wygenerować do 65536 tokenów, więc w praktyce trudno ten limit przekroczyć. Zgodnie z [oficjalną dokumentacją Gemini API](https://ai.google.dev/gemini-api/docs/models#token-size), w modelach Gemini 1 token to (dla języka angielskiego) ~4 znaki, a 100 tokenów to ok. 60–80 słów.
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

### Jak używać skryptów w Pythonie
W przypadku bloga opartego o Jekyll, wewnątrz katalogu `/_posts`{: .filepath} tworzę podkatalogi wg kodów języków [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php), np. `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Następnie w `/_posts/ko`{: .filepath} umieszczam koreański oryginał (albo — po odpowiedniej modyfikacji zmiennej `source_lang` w skrypcie — umieszczam oryginały w katalogu odpowiadającym wybranemu językowi). Do katalogu `/tools`{: .filepath} wkładam powyższe skrypty oraz plik `hash.csv`{: .filepath}, po czym w tym miejscu uruchamiam terminal i wykonuję:

```bash
python3 translate_changes.py
```

Wtedy skrypt się uruchomi i zobaczysz na wyjściu ekran podobny do poniższego.  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

Jeśli nie podasz żadnych opcji, domyślnie działa tryb tłumaczenia pełnego (full translation). Jeśli podasz `--incremental`, możesz użyć funkcji tłumaczenia przyrostowego.

```bash
python3 translate_changes.py --incremental
```

## Doświadczenia z użycia w praktyce
Jak wspomniałem wcześniej, pod koniec czerwca 12024 roku wdrożyłem na tym blogu automatyczne tłumaczenie postów z użyciem Claude Sonnet API i od tamtej pory korzystam z niego, stale je usprawniając. W większości przypadków można uzyskać naturalne tłumaczenia bez dodatkowej ingerencji człowieka; po opublikowaniu wielojęzycznych wersji wpisów faktycznie potwierdziłem istotny napływ ruchu Organic Search z regionów poza Koreą — m.in. z Brazylii, Kanady, USA, Francji czy Japonii. Co więcej, analiza nagranych sesji pokazuje, że część użytkowników, którzy trafili na tłumaczone wersje, potrafi spędzać na stronie od kilku minut do nawet kilkudziesięciu. Biorąc pod uwagę, że przy topornych tłumaczeniach maszynowych użytkownicy zwykle szybko wychodzą lub szukają wersji angielskiej, sugeruje to, że jakość tłumaczeń nie jest rażąco nienaturalna nawet z perspektywy native speakerów.

Poza samym ruchem na blogu zauważyłem też dodatkową korzyść z perspektywy mojej nauki: LLM-y takie jak Claude czy Gemini potrafią pisać bardzo płynnie po angielsku, więc w trakcie przeglądu przed Commit & Push do repozytorium GitHub Pages mam okazję sprawdzić, jak naturalnie oddać po angielsku konkretne koreańskie sformułowania, terminy czy zwroty użyte w oryginale. Oczywiście to nie wystarcza, by mówić o „wystarczającej” nauce angielskiego wyłącznie w ten sposób, ale możliwość częstego kontaktu — bez dodatkowego wysiłku — z naturalnymi angielskimi odpowiednikami zarówno codziennych, jak i akademickich wyrażeń (na podstawie tekstów, które sam napisałem i najlepiej znam) wydaje się być całkiem realną zaletą dla studenta kierunków inżynierskich w kraju nieanglojęzycznym, takim jak Korea.
