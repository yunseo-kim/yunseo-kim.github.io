---
title: Wie man Posts mit der Claude 3.5 Sonnet API automatisch übersetzt (2) - Erstellung und Anwendung von Automatisierungsskripten
description: Dieser Beitrag behandelt den Prozess des Entwerfens von Prompts für die mehrsprachige Übersetzung von Markdown-Textdateien und der Automatisierung der Aufgabe mit Python unter Verwendung eines von Anthropic ausgestellten API-Schlüssels und des erstellten Prompts. Dies ist der zweite Beitrag in der Serie und stellt die API-Ausstellung, Integration und Python-Skripterstellung vor.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
## Einleitung
Kürzlich habe ich die Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blogbeiträgen eingeführt. In dieser Serie möchte ich die Gründe für die Wahl der Claude 3.5 Sonnet API, die Methode des Prompt-Designs und die Implementierung der API-Integration und Automatisierung durch Python-Skripte erläutern.  
Die Serie besteht aus zwei Beiträgen, und dieser Beitrag, den Sie gerade lesen, ist der zweite Teil der Serie.
- Teil 1: [Einführung in das Claude 3.5 Sonnet-Modell und Gründe für die Auswahl, Prompt Engineering](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1)
- Teil 2: Erstellung und Anwendung von Python-Automatisierungsskripten mit der API (dieser Beitrag)

## Bevor wir beginnen
Dieser Beitrag ist eine Fortsetzung von [Teil 1](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1), daher empfehle ich, zuerst den vorherigen Beitrag zu lesen, falls Sie dies noch nicht getan haben.

## Claude API Integration
### Claude API-Schlüssel erhalten

> Hier wird erklärt, wie man einen neuen Claude API-Schlüssel erhält. Wenn Sie bereits einen API-Schlüssel haben, den Sie verwenden können, können Sie diesen Schritt überspringen.
{: .prompt-tip }

Melden Sie sich bei <https://console.anthropic.com> an. Wenn Sie noch kein Konto haben, müssen Sie sich zuerst registrieren. Nach der Anmeldung sollten Sie ein Dashboard-Bildschirm wie unten gezeigt sehen.  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Wenn Sie auf diesem Bildschirm auf die Schaltfläche 'Get API keys' klicken, sehen Sie den folgenden Bildschirm.  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Da ich bereits einen Schlüssel erstellt habe, wird ein Schlüssel mit dem Namen `yunseo-secret-key` angezeigt. Wenn Sie gerade erst ein Konto erstellt haben und noch keinen API-Schlüssel erhalten haben, haben Sie wahrscheinlich noch keine Schlüssel. Klicken Sie einfach auf die Schaltfläche 'Create Key' oben rechts, um einen neuen Schlüssel zu erhalten.

> Nachdem Sie den Schlüssel erhalten haben, wird Ihr API-Schlüssel auf dem Bildschirm angezeigt. Da dieser Schlüssel später nicht mehr eingesehen werden kann, stellen Sie sicher, dass Sie ihn an einem sicheren Ort separat notieren.
{: .prompt-warning }

### (Empfohlen) Registrierung des Claude API-Schlüssels als Umgebungsvariable
Um die Claude API in Python- oder Shell-Skripten zu verwenden, müssen Sie den API-Schlüssel abrufen. Obwohl es möglich ist, den API-Schlüssel direkt im Skript zu notieren, ist dies keine Option, wenn Sie das Skript auf GitHub hochladen oder auf andere Weise mit anderen teilen müssen. Selbst wenn Sie nicht vorhaben, die Skriptdatei zu teilen, besteht die Gefahr, dass der API-Schlüssel versehentlich zusammen mit der Skriptdatei preisgegeben wird, falls die Skriptdatei unbeabsichtigt durchsickert. Daher wird empfohlen, den API-Schlüssel als Umgebungsvariable in Ihrem persönlichen System zu registrieren und ihn dann im Skript aus dieser Umgebungsvariable abzurufen. Im Folgenden wird erklärt, wie man den API-Schlüssel als Systemumgebungsvariable für UNIX-Systeme registriert. Für Windows-Benutzer empfehle ich, andere Anleitungen im Internet zu konsultieren.

1. Öffnen Sie einen Terminal und führen Sie je nach verwendeter Shell `nano ~/.bashrc` oder `nano ~/.zshrc` aus, um den Editor zu starten.
2. Fügen Sie `export ANTHROPIC_API_KEY='your-api-key-here'` zum Inhalt der Datei hinzu. Ersetzen Sie 'your-api-key-here' durch Ihren tatsächlichen API-Schlüssel und achten Sie darauf, ihn mit einfachen Anführungszeichen zu umschließen.
3. Speichern Sie die Änderungen und beenden Sie den Editor.
4. Führen Sie `source ~/.bashrc` oder `source ~/.zshrc` im Terminal aus, um die Änderungen zu übernehmen.

### Installation der erforderlichen Python-Pakete
Wenn das anthropic-Paket in Ihrer Python-Umgebung noch nicht installiert ist, installieren Sie es mit folgendem Befehl:
```bash
pip3 install anthropic
```
Außerdem werden die folgenden Pakete für das später vorgestellte Skript zur Beitragsübersetzung benötigt. Installieren oder aktualisieren Sie sie mit folgendem Befehl:
```bash
pip3 install -U argparse tqdm
```

### Erstellung von Python-Skripten
Das in diesem Beitrag vorgestellte Skript zur Beitragsübersetzung besteht aus drei Python-Skriptdateien und einer CSV-Datei:

- `compare_hash.py`: Berechnet die SHA256-Hash-Werte der koreanischen Originalbeiträge im Verzeichnis `_posts/ko`{: .filepath}, vergleicht sie mit den bestehenden Hash-Werten in der Datei `hash.csv` und gibt eine Liste der geänderten oder neu hinzugefügten Dateinamen zurück.
- `hash.csv`: Eine CSV-Datei, die die SHA256-Hash-Werte der bestehenden Beitragsdateien enthält.
- `prompt.py`: Nimmt filepath, source_lang und target_lang als Eingabe, ruft den Claude API-Schlüssel aus der Systemumgebungsvariable ab, ruft die API auf und verwendet den zuvor erstellten Prompt als Systemprompt und den Inhalt des zu übersetzenden Beitrags aus 'filepath' als Benutzerprompt. Anschließend empfängt es die Antwort (das Übersetzungsergebnis) vom Claude 3.5 Sonnet-Modell und gibt sie als Textdatei im Pfad `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath} aus.
- `translate_changes.py`: Enthält die String-Variable source_lang und die Liste 'target_langs', ruft die Funktion `changed_files()` aus `compare_hash.py` auf, um die Liste changed_files zurückzugeben. Wenn es geänderte Dateien gibt, führt es eine doppelte Schleife über alle Dateien in der changed_files-Liste und alle Elemente in der target_langs-Liste aus und ruft innerhalb dieser Schleife die Funktion `translate(filepath, source_lang, target_lang)` aus `prompt.py` auf, um die Übersetzung durchzuführen.

Der Inhalt der fertigen Skriptdateien kann auch im GitHub-Repository [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) eingesehen werden.

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
    # Sortiere die Datei-Hashes nach Dateinamen (den Dictionary-Schlüsseln)
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
            if not file.endswith('.md'):  # Verarbeite nur .md-Dateien
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
        print("Geänderte Dateien:")
        for file in changed_files:
            print(f"- {file}")
    else:
        print("Keine Dateien wurden geändert.")

    os.chdir(initial_wd)
```

#### prompt.py
Da der Inhalt den zuvor erstellten Prompt enthält und daher etwas lang ist, wird er durch einen Link zur Quelldatei im GitHub-Repository ersetzt.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In der `prompt.py`-Datei unter dem obigen Link ist `max_tokens` eine Variable, die die maximale Ausgabelänge unabhängig von der Größe des Kontextfensters festlegt. Obwohl die Größe des Kontextfensters, das bei der Verwendung der Claude API auf einmal eingegeben werden kann, 200k Token beträgt (etwa 680.000 Zeichen), gibt es für jedes Modell eine festgelegte maximale Anzahl von Ausgabe-Tokens. Es wird empfohlen, dies vor der Verwendung der API in der [offiziellen Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/about-claude/models) zu überprüfen. Die bisherigen Claude 3-Serienmodelle konnten maximal 4096 Token ausgeben, was für die meisten Beiträge auf diesem Blog kein Problem darstellte. Bei einigen längeren Beiträgen mit mehr als etwa 8000 koreanischen Zeichen trat jedoch in einigen Ausgabesprachen das Problem auf, dass die 4096 Token überschritten wurden und der hintere Teil der Übersetzung abgeschnitten wurde. Bei Claude 3.5 Sonnet hat sich die maximale Anzahl der Ausgabe-Token auf 8192 verdoppelt, sodass es kaum noch Probleme mit der Überschreitung dieser maximalen Ausgabe-Token-Anzahl gab. In der `prompt.py` im obigen GitHub-Repository wurde `max_tokens=8192` festgelegt.
{: .prompt-tip }

#### translate_changes.py

```python
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
        '.swp',       # vim temporäre Datei
        '.swo'        # vim temporäre Datei
    ]
    
    # Gibt False zurück, wenn der Dateiname eines der Ausschlussmuster enthält
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
    # Filtern temporärer Dateien
    changed_files = [f for f in changed_files if is_valid_file(f)]
    
    if not changed_files:
        sys.exit("Keine Dateien wurden geändert.")
    print("Geänderte Dateien:")
    for file in changed_files:
        print(f"- {file}")

    print("")
    print("*** Übersetzung beginnt! ***")
    # Äußere Schleife: Fortschritt der geänderten Dateien
    for changed_file in tqdm(changed_files, desc="Dateien", position=0):
        filepath = os.path.join(posts_dir, source_lang_code, changed_file)
        # Innere Schleife: Übersetzungsfortschritt für jede Sprache pro Datei
        for target_lang in tqdm(target_langs, desc="Sprachen", position=1, leave=False):
            prompt.translate(filepath, source_lang, target_lang)
    
    print("\nÜbersetzung abgeschlossen!")
    os.chdir(initial_wd)
```

### Verwendung des Python-Skripts
Für einen Jekyll-Blog legen Sie innerhalb des `/_posts`{: .filepath}-Verzeichnisses, in dem sich die Beiträge befinden, Unterverzeichnisse für jede [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) Sprachcode an, wie `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Platzieren Sie dann die oben vorgestellten Python-Skripte und die CSV-Datei im `/tools`{: .filepath}-Verzeichnis, öffnen Sie ein Terminal an diesem Ort und führen Sie den folgenden Befehl aus:

```bash
python3 translate_changes.py
```

Das Skript wird ausgeführt und Sie sollten einen Bildschirm wie den folgenden sehen:  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Erfahrungsbericht
Wie oben beschrieben, verwende ich die automatische Beitragsübersetzung mit der Claude 3.5 API seit etwa zwei Monaten auf diesem Blog. In den meisten Fällen erhalte ich Übersetzungen von hervorragender Qualität, ohne dass ein zusätzlicher menschlicher Eingriff erforderlich ist. Nachdem ich die Beiträge in mehreren Sprachen übersetzt und veröffentlicht habe, konnte ich tatsächlich organischen Suchverkehr aus Regionen außerhalb Koreas wie Brasilien, Kanada, den USA und Frankreich beobachten. Neben dem Blogverkehr gab es auch zusätzliche Vorteile für das Lernen des Autors selbst. Da Claude sehr flüssige Texte auf Englisch erstellt, hatte ich beim Überprüfen der Beiträge vor dem Push in das GitHub Pages-Repository die Gelegenheit zu sehen, wie bestimmte Begriffe oder Ausdrücke aus meinem koreanischen Originaltext auf natürliche Weise auf Englisch ausgedrückt werden können. Obwohl dies allein nicht für ein umfassendes Englischstudium ausreicht, scheint es für einen Ingenieurstudenten aus einem nicht-englischsprachigen Land wie Korea durchaus vorteilhaft zu sein, regelmäßig und ohne zusätzlichen Aufwand natürliche englische Ausdrücke nicht nur für alltägliche, sondern auch für akademische Ausdrücke und Begriffe zu sehen, und das anhand eines Textes, der vertrauter ist als jeder andere - nämlich des selbst verfassten Textes.
