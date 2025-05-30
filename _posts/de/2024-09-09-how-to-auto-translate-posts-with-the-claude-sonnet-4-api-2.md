---
title: Automatische Übersetzung von Posts mit der Claude Sonnet 4 API (2) - Erstellung und Anwendung von Automatisierungsskripten
description: "Behandelt den Prozess der Gestaltung von Prompts für die mehrsprachige Übersetzung von Markdown-Textdateien und der Automatisierung der Arbeit mit Python unter Anwendung des von Anthropic ausgestellten API-Schlüssels und der erstellten Prompts. Dieser Post ist der zweite Artikel der entsprechenden Serie und stellt die API-Ausgabe und -Integration sowie die Methoden zur Erstellung von Python-Skripten vor."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Einführung
Seit der Einführung der Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blog-Posts im Juni 12024 betreibe ich das entsprechende Übersetzungssystem nach mehreren Verbesserungen der Prompts und Automatisierungsskripte sowie Modell-Upgrades über einen Zeitraum von fast einem Jahr zufriedenstellend. In dieser Serie möchte ich die Gründe für die Wahl des Claude Sonnet-Modells im Einführungsprozess, die Methoden des Prompt-Designs sowie die Implementierung der API-Integration und Automatisierung durch Python-Skripte behandeln.  
Die Serie besteht aus 2 Artikeln, und dieser Artikel, den Sie gerade lesen, ist der zweite Artikel der entsprechenden Serie.
- Teil 1: [Einführung des Claude Sonnet-Modells und Auswahlgründe, Prompt Engineering](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1)
- Teil 2: Erstellung und Anwendung von Python-Automatisierungsskripten mit der API (Haupttext)

## Bevor wir beginnen
Dieser Artikel ist eine Fortsetzung von [Teil 1](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1), daher wird empfohlen, zuerst den vorherigen Artikel zu lesen, falls Sie ihn noch nicht gelesen haben.

## Vollständiger System-Prompt
Das Ergebnis des Prompt-Designs nach dem [in Teil 1 vorgestellten Prozess](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-1/#prompt-design) ist wie folgt.

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

## Claude API-Integration
### Claude API-Schlüssel ausgeben

> Hier wird erklärt, wie man einen neuen Claude API-Schlüssel ausgibt. Wenn Sie bereits einen verwendbaren API-Schlüssel haben, können Sie diesen Schritt überspringen.
{: .prompt-tip }

Besuchen Sie <https://console.anthropic.com> und melden Sie sich an. Falls Sie noch kein Konto haben, müssen Sie sich zuerst registrieren. Nach der Anmeldung sehen Sie ein Dashboard wie unten gezeigt.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Anthropic_Console.png)

Klicken Sie auf dem entsprechenden Bildschirm auf die Schaltfläche 'Get API keys', dann sehen Sie den folgenden Bildschirm.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/api-keys.png) Da ich bereits einen erstellten Schlüssel habe, wird ein Schlüssel namens `yunseo-secret-key` angezeigt, aber wenn Sie gerade ein Konto erstellt haben und noch keinen API-Schlüssel ausgegeben haben, haben Sie wahrscheinlich noch keine Schlüssel. Klicken Sie auf die Schaltfläche 'Create Key' oben rechts, um einen neuen Schlüssel auszugeben.

> Nach Abschluss der Schlüsselausgabe wird Ihr API-Schlüssel auf dem Bildschirm angezeigt, aber dieser Schlüssel kann später nicht mehr eingesehen werden, daher müssen Sie ihn unbedingt an einem sicheren Ort separat notieren.
{: .prompt-warning }

### (Empfohlen) Claude API-Schlüssel in Umgebungsvariablen registrieren
Um die Claude API in Python- oder Shell-Skripten zu verwenden, muss der API-Schlüssel geladen werden. Es gibt zwar die Möglichkeit, den API-Schlüssel direkt im Skript zu notieren, aber wenn das Skript auf GitHub hochgeladen oder anderweitig mit anderen geteilt werden soll, ist diese Methode nicht verwendbar. Auch wenn Sie nicht vorhaben, das Skript zu teilen, besteht die Gefahr, dass die Skriptdatei durch unbeabsichtigte Fehler preisgegeben wird, und wenn der API-Schlüssel in der Skriptdatei notiert ist, kann es zu einem Unfall kommen, bei dem auch der API-Schlüssel preisgegeben wird. Daher wird empfohlen, den API-Schlüssel in den Umgebungsvariablen des Systems zu registrieren, das nur Sie verwenden, und im Skript diese Umgebungsvariable zu laden. Im Folgenden wird die Methode zur Registrierung des API-Schlüssels in den System-Umgebungsvariablen basierend auf UNIX-Systemen vorgestellt. Für Windows beziehen Sie sich bitte auf andere Artikel im Web.

1. Geben Sie im Terminal je nach verwendetem Shell-Typ `nano ~/.bashrc` oder `nano ~/.zshrc` ein, um den Editor zu starten.
2. Fügen Sie `export ANTHROPIC_API_KEY='your-api-key-here'` zum Inhalt der Datei hinzu. Ersetzen Sie 'your-api-key-here' durch Ihren API-Schlüssel und achten Sie darauf, ihn mit ' zu umschließen.
3. Speichern Sie die Änderungen und beenden Sie den Editor.
4. Führen Sie im Terminal `source ~/.bashrc` oder `source ~/.zshrc` aus, um die Änderungen zu übernehmen.

### Erforderliche Python-Pakete installieren
Falls das anthropic-Paket nicht in Ihrer Python-Umgebung installiert ist, installieren Sie es mit folgendem Befehl.
```bash
pip3 install anthropic
```
Außerdem sind die folgenden Pakete für das später vorgestellte Post-Übersetzungsskript erforderlich, installieren oder aktualisieren Sie sie mit folgendem Befehl.
```bash
pip3 install -U argparse tqdm
```

### Python-Skript schreiben
Das in diesem Artikel vorgestellte Post-Übersetzungsskript besteht aus den folgenden 3 Python-Skriptdateien und 1 CSV-Datei.

- `compare_hash.py`{: .filepath}: Berechnet die SHA256-Hash-Werte der koreanischen Originalpost-Dateien im `_posts/ko`{: .filepath}-Verzeichnis, vergleicht sie mit den in der `hash.csv`{: .filepath}-Datei aufgezeichneten bestehenden Hash-Werten und gibt eine Liste der geänderten oder neu hinzugefügten Dateinamen zurück
- `hash.csv`{: .filepath}: CSV-Datei, die die SHA256-Hash-Werte der bestehenden Post-Dateien aufzeichnet
- `prompt.py`{: .filepath}: Empfängt filepath-, source_lang- und target_lang-Werte, lädt den Claude API-Schlüsselwert aus den System-Umgebungsvariablen, ruft die API auf und übermittelt den zuvor erstellten Prompt als System-Prompt und den Inhalt des zu übersetzenden Posts unter 'filepath' als Benutzer-Prompt. Anschließend empfängt es die Antwort (Übersetzungsergebnis) vom Claude Sonnet 4-Modell und gibt sie als Textdatei unter dem Pfad `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath} aus
- `translate_changes.py`{: .filepath}: Enthält die source_lang-String-Variable und die 'target_langs'-Listenvariable, ruft die `changed_files()`-Funktion in `compare_hash.py`{: .filepath} auf und erhält die changed_files-Listenvariable zurück. Falls geänderte Dateien vorhanden sind, führt es eine doppelte Schleife für alle Dateien in der changed_files-Liste und alle Elemente in der target_langs-Liste aus und ruft innerhalb dieser Schleife die `translate(filepath, source_lang, target_lang)`-Funktion in `prompt.py`{: .filepath} auf, um die Übersetzungsarbeit durchzuführen.

Der Inhalt der vollständigen Skriptdateien kann auch im GitHub-Repository [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) eingesehen werden.

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
Da der Dateiinhalt aufgrund des zuvor erstellten Prompt-Inhalts ziemlich lang ist, wird er durch einen Link zur Quelldatei im GitHub-Repository ersetzt.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In der `prompt.py`{: .filepath}-Datei unter dem obigen Link ist `max_tokens` eine Variable, die unabhängig von der Context-Window-Größe die maximale Ausgabelänge festlegt. Bei der Verwendung der Claude API beträgt die Größe des Context-Windows, das auf einmal eingegeben werden kann, 200k Token (etwa 680.000 Zeichen), aber unabhängig davon ist die maximale Anzahl der Ausgabe-Token für jedes Modell festgelegt, daher wird empfohlen, dies vor der API-Nutzung in der [offiziellen Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/about-claude/models) zu überprüfen. Die bestehenden Claude 3-Serie-Modelle konnten maximal 4096 Token ausgeben, aber bei Tests mit den Artikeln dieses Blogs trat bei koreanischen Posts mit etwa 8000 oder mehr Zeichen in einigen Ausgabesprachen das Problem auf, dass 4096 Token überschritten wurden und der hintere Teil der Übersetzung abgeschnitten wurde. Bei Claude 3.5 Sonnet wurde die maximale Anzahl der Ausgabe-Token auf das Doppelte, nämlich 8192, erhöht, sodass es normalerweise keine Probleme durch Überschreitung dieser maximalen Ausgabe-Token-Anzahl gab, und ab Claude 3.7 wurde es so aktualisiert, dass es viel längere Ausgaben unterstützt. In der `prompt.py`{: .filepath} im obigen GitHub-Repository ist `max_tokens=16384` festgelegt.
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
    # Auszuschließende Dateimuster
    excluded_patterns = [
        '.DS_Store',  # macOS-Systemdatei
        '~',          # Temporäre Datei
        '.tmp',       # Temporäre Datei
        '.temp',      # Temporäre Datei
        '.bak',       # Backup-Datei
        '.swp',       # vim-Temporärdatei
        '.swo'        # vim-Temporärdatei
    ]
    
    # Gibt False zurück, wenn der Dateiname eines der Ausschlussmuster enthält
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
    # Temporäre Dateien filtern
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("No files have changed.")
    print("Changed files:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Translation start! ***")
    # Äußere Schleife: Fortschritt der geänderten Dateien
    for changed_file in tqdm(changed_files, desc="Files", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Innere Schleife: Fortschritt der sprachspezifischen Übersetzung für jede Datei
        for target_lang in tqdm(target_langs, desc="Languages", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nTranslation completed!")
    os.chdir(initial_wd)
```

### Verwendung der Python-Skripte
Basierend auf Jekyll-Blogs erstellen Sie Unterverzeichnisse nach [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php)-Sprachcodes wie `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath} im `/_posts`{: .filepath}-Verzeichnis. Platzieren Sie den koreanischen Originaltext im `/_posts/ko`{: .filepath}-Verzeichnis (oder modifizieren Sie die `source_lang`-Variable im Python-Skript entsprechend Ihren Bedürfnissen und platzieren Sie den Originaltext in der entsprechenden Sprache im entsprechenden Verzeichnis), platzieren Sie die oben vorgestellten Python-Skripte und die `hash.csv`{: .filepath}-Datei im `/tools`{: .filepath}-Verzeichnis, öffnen Sie dann das Terminal an diesem Ort und führen Sie den folgenden Befehl aus.

```bash
python3 translate_changes.py
```

Dann wird das Skript ausgeführt und ein Bildschirm wie unten gezeigt ausgegeben.  
![Screenshot der Skriptausführung 1](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-1.png)  
![Screenshot der Skriptausführung 2](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/translating-screen-2.png)

## Erfahrungen aus der praktischen Nutzung
Wie bereits erwähnt, habe ich die automatische Post-Übersetzung mit der Claude Sonnet API Ende Juni 12024 in diesem Blog eingeführt und nutze sie seitdem kontinuierlich mit Verbesserungen. In den meisten Fällen kann ich natürliche Übersetzungen erhalten, ohne dass zusätzliche menschliche Eingriffe erforderlich sind, und nach der Veröffentlichung von Posts in mehreren Sprachen konnte ich bestätigen, dass tatsächlich erheblicher Organic Search-Traffic aus Regionen außerhalb Koreas wie Brasilien, Kanada, USA, Frankreich und Japan über Suchmaschinen eingeht. Außerdem zeigen aufgezeichnete Sitzungen, dass Besucher, die über Übersetzungen eingehen, oft mehrere Minuten bis zu mehreren zehn Minuten oder länger verweilen. Normalerweise verlassen Besucher Webseiten, die offensichtlich maschinell übersetzt und unnatürlich wirken, schnell oder suchen lieber nach der englischen Version, was darauf hindeutet, dass die Qualität der Übersetzungen auch für Muttersprachler nicht besonders unnatürlich ist. Zusätzlich zum Blog-Traffic-Zuwachs gab es auch zusätzliche Vorteile für mein eigenes Lernen als Autor. Da Claude sehr flüssige englische Texte erstellt, hatte ich beim Überprüfungsprozess vor dem Commit & Push der Posts zum GitHub Pages-Repository die Gelegenheit zu sehen, wie bestimmte Begriffe oder Ausdrücke aus meinem koreanischen Originaltext natürlich ins Englische übersetzt werden. Obwohl dies allein nicht für ausreichendes Englischlernen reicht, ist es für Ingenieurstudenten in nicht-englischsprachigen Ländern wie Korea durchaus vorteilhaft, häufig natürliche englische Ausdrücke nicht nur für alltägliche, sondern auch für akademische Begriffe anhand der vertrautesten Texte - meiner eigenen Artikel - ohne zusätzlichen Aufwand kennenzulernen.
