---
title: Wie man Posts automatisch mit der Claude 3.5 Sonnet API übersetzt (2) - Erstellung und Anwendung von Automatisierungsskripten
description: >-
  Dieser Beitrag behandelt den Prozess der Gestaltung von Prompts für die mehrsprachige Übersetzung von Markdown-Textdateien und die Automatisierung der Aufgabe mit Python unter Verwendung des von Anthropic erhaltenen API-Schlüssels und der erstellten Prompts. Dies ist der zweite Beitrag in der Serie und stellt die API-Bereitstellung und -Integration sowie die Erstellung von Python-Skripten vor.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Einführung
Kürzlich habe ich die Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blogbeiträgen eingeführt. In dieser Serie werden die Gründe für die Wahl der Claude 3.5 Sonnet API, die Methoden des Prompt-Designs und die Implementierung der API-Integration sowie Automatisierung durch Python-Skripte behandelt.  
Die Serie besteht aus zwei Artikeln, und dieser Artikel ist der zweite Teil der Serie.
- Teil 1: [Vorstellung des Claude 3.5 Sonnet Modells, Auswahlgründe und Prompt Engineering](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Teil 2: Erstellung und Implementierung von Python-Automatisierungsskripten mit der API (dieser Artikel)

## Bevor wir beginnen
Dieser Artikel ist eine Fortsetzung von [Teil 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1). Falls Sie diesen noch nicht gelesen haben, empfehle ich, zuerst den vorherigen Artikel zu lesen.

## Claude API Integration
### Claude API-Schlüssel erhalten

> Hier wird erklärt, wie man einen neuen Claude API-Schlüssel erhält. Wenn Sie bereits einen API-Schlüssel haben, können Sie diesen Schritt überspringen.
{: .prompt-tip }

Besuchen Sie <https://console.anthropic.com> und melden Sie sich an. Falls Sie noch kein Konto haben, müssen Sie sich zunächst registrieren. Nach der Anmeldung sehen Sie das folgende Dashboard.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Klicken Sie auf der Seite auf die Schaltfläche 'Get API keys', um den folgenden Bildschirm zu sehen.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Da ich bereits einen Schlüssel erstellt habe, wird ein Schlüssel mit dem Namen `yunseo-secret-key` angezeigt. Wenn Sie gerade erst ein Konto erstellt haben und noch keinen API-Schlüssel besitzen, werden Sie wahrscheinlich keine vorhandenen Schlüssel sehen. Klicken Sie oben rechts auf die Schaltfläche 'Create Key', um einen neuen Schlüssel zu erstellen.

> Nach der Schlüsselerstellung wird Ihr API-Schlüssel angezeigt. Da dieser Schlüssel später nicht mehr eingesehen werden kann, müssen Sie ihn unbedingt an einem sicheren Ort separat aufbewahren.
{: .prompt-warning }

### (Empfohlen) Claude API-Schlüssel in Umgebungsvariablen registrieren
Um die Claude API in Python- oder Shell-Skripten zu verwenden, muss der API-Schlüssel geladen werden. Man könnte den API-Schlüssel direkt im Skript speichern, aber diese Methode ist nicht geeignet, wenn das Skript auf GitHub hochgeladen oder anderweitig mit anderen geteilt werden soll. Auch wenn Sie nicht vorhaben, das Skript zu teilen, besteht das Risiko, dass bei unbeabsichtigtem Durchsickern des Skripts auch der API-Schlüssel kompromittiert wird. Daher wird empfohlen, den API-Schlüssel in den Umgebungsvariablen des eigenen Systems zu registrieren und ihn im Skript aus diesen Variablen zu laden. Im Folgenden wird die Methode zur Registrierung des API-Schlüssels in Systemumgebungsvariablen für UNIX-Systeme vorgestellt. Für Windows konsultieren Sie bitte andere Online-Ressourcen.

1. Öffnen Sie im Terminal je nach verwendeter Shell `nano ~/.bashrc` oder `nano ~/.zshrc`.
2. Fügen Sie `export ANTHROPIC_API_KEY='your-api-key-here'` zum Dateiinhalt hinzu. Ersetzen Sie 'your-api-key-here' durch Ihren API-Schlüssel und beachten Sie, dass er von Anführungszeichen umschlossen sein muss.
3. Speichern Sie die Änderungen und beenden Sie den Editor.
4. Führen Sie im Terminal `source ~/.bashrc` oder `source ~/.zshrc` aus, um die Änderungen zu übernehmen.

### Erforderliche Python-Pakete installieren
Wenn das anthropic-Paket in Ihrer Python-Umgebung noch nicht installiert ist, installieren Sie es mit folgendem Befehl:
```bash
pip3 install anthropic
```
Außerdem werden die folgenden Pakete für das später vorgestellte Übersetzungsskript benötigt. Installieren oder aktualisieren Sie sie mit diesem Befehl:
```bash
pip3 install -U argparse tqdm
```

### Python-Skripte erstellen
Das hier vorgestellte Übersetzungsskript besteht aus drei Python-Skriptdateien und einer CSV-Datei.

- `compare_hash.py`: Berechnet SHA256-Hash-Werte der koreanischen Originalbeiträge im Verzeichnis `_posts/ko`{: .filepath} und vergleicht sie mit den bestehenden Hash-Werten in der `hash.csv`-Datei, um eine Liste der geänderten oder neu hinzugefügten Dateien zurückzugeben
- `hash.csv`: CSV-Datei mit den SHA256-Hash-Werten der bestehenden Beitragsdateien
- `prompt.py`: Empfängt filepath, source_lang, target_lang Werte und lädt den Claude API-Schlüssel aus den Systemumgebungsvariablen. Ruft die API auf und verwendet den zuvor erstellten Prompt als Systemprompt und den Inhalt des zu übersetzenden Beitrags aus 'filepath' als Benutzerprompt. Empfängt dann die Antwort (Übersetzungsergebnis) vom Claude 3.5 Sonnet Modell und speichert sie als Textdatei unter `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath}
- `translate_changes.py`: Enthält die String-Variable source_lang und die Liste 'target_langs', ruft die Funktion `changed_files()` aus `compare_hash.py` auf und erhält die Liste changed_files zurück. Wenn es geänderte Dateien gibt, führt eine Doppelschleife über alle Dateien in der changed_files Liste und alle Elemente in der target_langs Liste aus und ruft dabei die Funktion `translate(filepath, source_lang, target_lang)` aus `prompt.py` auf, um die Übersetzung durchzuführen.

Der vollständige Inhalt der Skriptdateien kann auch im GitHub-Repository [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) eingesehen werden.

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
Da die Datei den zuvor erstellten Prompt enthält und daher recht lang ist, wird sie durch einen Link zur Quelldatei im GitHub-Repository ersetzt.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In der `prompt.py`-Datei unter dem obigen Link ist `max_tokens` eine Variable, die die maximale Ausgabelänge unabhängig von der Context-Window-Größe festlegt. Während die Context-Window-Größe bei der Claude API-Nutzung 200k Token (etwa 680.000 Zeichen) beträgt, hat jedes Modell eine festgelegte maximale Ausgabe-Token-Anzahl. Es wird empfohlen, diese vor der API-Nutzung in der [offiziellen Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/about-claude/models) zu überprüfen. Die bisherigen Claude 3-Modelle konnten maximal 4096 Token ausgeben, was bei den meisten Blogbeiträgen ausreichte. Bei einigen längeren Beiträgen mit über 8000 koreanischen Zeichen wurde die 4096-Token-Grenze jedoch in manchen Zielsprachen überschritten, wodurch der hintere Teil der Übersetzung abgeschnitten wurde. Claude 3.5 Sonnet verdoppelt die maximale Ausgabe-Token-Anzahl auf 8192, wodurch solche Probleme praktisch nicht mehr auftreten. In der `prompt.py` im obigen GitHub-Repository ist `max_tokens=8192` entsprechend eingestellt.
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

### Verwendung der Python-Skripte
Für Jekyll-Blogs erstellen Sie im Verzeichnis `/_posts`{: .filepath} Unterverzeichnisse nach [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) Sprachcodes wie `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Platzieren Sie die oben vorgestellten Python-Skripte und die CSV-Datei im Verzeichnis `/tools`{: .filepath} und führen Sie dort im Terminal folgenden Befehl aus:

```bash
python3 translate_changes.py
```

Das Skript wird ausgeführt und zeigt folgende Bildschirme:  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Praxiserfahrung
Wie oben beschrieben, nutze ich die automatische Beitragsübersetzung mit der Claude 3.5 API seit etwa zwei Monaten für diesen Blog. In den meisten Fällen liefert sie ohne zusätzlichen menschlichen Eingriff Übersetzungen von hervorragender Qualität. Nach der mehrsprachigen Veröffentlichung der Beiträge konnte ich tatsächlich organischen Suchverkehr aus Ländern außerhalb Koreas wie Brasilien, Kanada, den USA und Frankreich feststellen. Neben dem Blogverkehr gibt es auch zusätzliche Vorteile für das Lernen des Autors selbst: Da Claude sehr flüssige englische Texte erstellt, kann ich beim Überprüfen der Beiträge vor dem Push in das GitHub Pages Repository sehen, wie bestimmte Begriffe oder Ausdrücke aus meinem koreanischen Original auf natürliche Weise auf Englisch ausgedrückt werden. Auch wenn dies allein nicht für umfassendes Englischlernen ausreicht, ist es für einen Ingenieurstudenten aus einem nicht-englischsprachigen Land wie Korea durchaus vorteilhaft, ohne zusätzlichen Aufwand regelmäßig natürliche englische Ausdrücke und Fachbegriffe anhand des eigenen, vertrauten Texts zu lernen.
