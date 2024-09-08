---
title: Wie man Beiträge mit der Claude 3.5 Sonnet API automatisch übersetzt
description: >-
  Dieser Beitrag stellt kurz das kürzlich veröffentlichte Claude 3.5 Sonnet Modell vor und teilt den Prozess des Prompt-Designs sowie das fertige Prompt für die mehrsprachige Übersetzung von Blogbeiträgen. Außerdem wird erklärt, wie man mit einem von Anthropic erhaltenen API-Schlüssel und dem zuvor erstellten Prompt ein Python-Skript zur Automatisierung der Übersetzung schreibt und verwendet.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Einleitung
Kürzlich habe ich die Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blogbeiträgen eingeführt. In diesem Beitrag möchte ich die Gründe für die Wahl der Claude 3.5 Sonnet API, die Methode des Prompt-Designs und die Implementierung der Automatisierung durch API-Integration und Python-Skripte erläutern.

## Über Claude 3.5 Sonnet
Die Claude 3 Modellreihe wird je nach Modellgröße in den Versionen Haiku, Sonnet und Opus angeboten.  
![Unterscheidung der Claude 3 Modell-Tiers](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Bildquelle: [Offizielle Webseite der Anthropic Claude API](https://www.anthropic.com/api)

Am 21. Juni 2024 (koreanische Zeit) veröffentlichte Anthropic das neueste Sprachmodell [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Laut Anthropics Ankündigung übertrifft es die Inferenzleistung von Claude 3 Opus bei gleichen Kosten und Geschwindigkeit wie das bestehende Claude 3 Sonnet. Es wird allgemein als dem Konkurrenzmodell GPT-4 in den Bereichen Texterstellung, sprachliches Schlussfolgern, mehrsprachiges Verständnis und Übersetzung überlegen angesehen.  
![Einführungsbild von Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Leistungs-Benchmark-Ergebnisse von Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Bildquelle: [Anthropic Homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

## Gründe für die Einführung von Claude 3.5 zur Beitragsübersetzung
Es gibt bereits kommerzielle Übersetzungs-APIs wie Google Translate oder DeepL, die keine großen Sprachmodelle wie Claude 3.5 oder GPT-4 verwenden. Dennoch habe ich mich für die Verwendung eines LLM zu Übersetzungszwecken entschieden, weil der Benutzer im Gegensatz zu anderen kommerziellen Übersetzungsdiensten durch Prompt-Design dem Modell zusätzliche Kontextinformationen oder Anforderungen wie den Schreibzweck oder die Hauptthemen des Textes neben dem eigentlichen Inhalt zur Verfügung stellen kann, und das Modell die Übersetzung entsprechend kontextbezogen anpassen kann. Obwohl DeepL und Google Translate im Allgemeinen eine hervorragende Übersetzungsqualität bieten, neigen sie aufgrund ihrer Einschränkungen beim Erfassen des Themas und des Gesamtkontexts dazu, relativ unnatürliche Ergebnisse zu liefern, wenn sie gebeten werden, lange Texte zu fachspezifischen Themen anstelle von alltäglichen Gesprächen zu übersetzen. Insbesondere Claude wird, wie bereits erwähnt, in den Bereichen Texterstellung, sprachliches Schlussfolgern, mehrsprachiges Verständnis und Übersetzung als dem Konkurrenzmodell GPT-4 relativ überlegen eingeschätzt, weshalb ich es für geeignet hielt, die technischen Artikel in diesem Blog in mehrere Sprachen zu übersetzen.

## Prompt-Design
### Grundprinzipien des Prompt-Designs
Um zufriedenstellende Ergebnisse von einem Sprachmodell zu erhalten, die dem Zweck entsprechen, muss ein angemessener Prompt bereitgestellt werden. Prompt-Design mag zunächst überwältigend erscheinen, aber tatsächlich unterscheidet sich die "Methode, etwas gut anzufordern" nicht wesentlich, ob der Gegenüber ein Sprachmodell oder ein Mensch ist. Wenn man es aus dieser Perspektive betrachtet, ist es nicht besonders schwierig. Es ist gut, die aktuelle Situation und die Anforderungen nach den sechs W-Fragen (Wer, Was, Wann, Wo, Wie, Warum) klar zu erklären und bei Bedarf einige konkrete Beispiele hinzuzufügen. Es gibt zahlreiche Tipps und Techniken für das Prompt-Design, aber die meisten leiten sich von diesem Grundprinzip ab.

### Rollenzuweisung und Situationsbeschreibung (Wer, Warum)
Zuerst wies ich Claude 3.5 die Rolle eines "professionellen technischen Übersetzers" zu und gab Kontextinformationen über den Benutzer als "einen Technik-Blogger, der hauptsächlich über Mathematik, Physik und Datenwissenschaft schreibt".
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Übermittlung der allgemeinen Anforderungen (Was)
Als Nächstes bat ich darum, den vom Benutzer bereitgestellten Text im Markdown-Format von {source_lang} nach {target_lang} zu übersetzen, während das Format beibehalten wird. 
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Bei der Ausführung der Claude API werden die Platzhalter {source_lang} und {target_lang} im Prompt durch die Variablen für die Ausgangs- und Zielsprache mithilfe der f-string-Funktion des Python-Skripts ersetzt.
{: .prompt-info }

### Konkretisierung der Anforderungen und Beispiele (Wie)
Bei einfachen Aufgaben kann es ausreichen, nur bis zum vorherigen Schritt zu gehen, um die gewünschten Ergebnisse zu erhalten. Bei komplexeren Aufgaben können jedoch zusätzliche Erklärungen erforderlich sein. In diesem Fall wurden die folgenden Bedingungen hinzugefügt.

#### Behandlung des YAML Front Matter
Der YAML Front Matter am Anfang eines in Markdown geschriebenen Beitrags für einen Jekyll-Blog enthält Informationen zu 'title', 'description', 'categories' und 'tags'. Zum Beispiel sieht der YAML Front Matter dieses Beitrags wie folgt aus:

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

Bei der Übersetzung eines Beitrags sollten die Tags 'title' und 'description' in mehrere Sprachen übersetzt werden, aber für die Konsistenz der Beitrags-URLs ist es für die Wartung einfacher, die Namen der Kategorien (categories) und Tags (tags) unübersetzt auf Englisch zu belassen. Daher wurde folgende Anweisung gegeben, um nur 'title' und 'description' zu übersetzen:
> In the provided markdown formatted text, do not translate the YAML front matter except for the 'title' and 'description' tags.

#### Behandlung von Texten, die andere Sprachen als die Ausgangssprache enthalten
Beim Schreiben des Originaltexts auf Koreanisch kommt es oft vor, dass bei der Einführung einer Konzeptdefinition oder bei der Verwendung bestimmter Fachbegriffe der englische Ausdruck in Klammern hinzugefügt wird, wie bei '*중성자 감쇠 (Neutron Attenuation)*'. Bei der Übersetzung solcher Ausdrücke gab es Probleme mit der Inkonsistenz der Übersetzungsmethode, manchmal wurden die Klammern beibehalten, manchmal der englische Text in den Klammern weggelassen. Um dieses Problem zu lösen, wurde der folgende Satz zum Prompt hinzugefügt:
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Behandlung von Links zu anderen Beiträgen
Einige Beiträge enthalten Links zu anderen Beiträgen, und es gab häufig Probleme, bei denen interne Links unterbrochen wurden, weil der Pfadteil der URL als zu übersetzender Teil interpretiert und geändert wurde. Dieses Problem wurde gelöst, indem der folgende Satz zum Prompt hinzugefügt wurde:
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Nur das Übersetzungsergebnis als Antwort ausgeben
Schließlich wird der folgende Satz präsentiert, um sicherzustellen, dass bei der Antwort nur das Übersetzungsergebnis ausgegeben wird, ohne zusätzliche Kommentare:
> The output should only contain the translated text.

### Fertiger Prompt
Das Ergebnis des Prompt-Designs nach den obigen Schritten sieht wie folgt aus:
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.

## Claude API Integration
### Erhalt eines Claude API-Schlüssels

> Hier wird erklärt, wie man einen neuen Claude API-Schlüssel erhält. Wenn Sie bereits einen API-Schlüssel haben, den Sie verwenden können, können Sie diesen Schritt überspringen.
{: .prompt-tip }

Besuchen Sie <https://console.anthropic.com> und melden Sie sich an. Wenn Sie noch kein Konto haben, müssen Sie sich zuerst registrieren. Nach der Anmeldung sollten Sie einen Dashboard-Bildschirm wie den folgenden sehen:  
![Anthropic Console Dashboard](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Anthropic_Console.png)

Wenn Sie auf diesem Bildschirm auf die Schaltfläche 'Get API keys' klicken, sehen Sie den folgenden Bildschirm:  
![API Keys](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/api-keys.png) Da ich bereits einen Schlüssel erstellt habe, wird ein Schlüssel mit dem Namen `yunseo-secret-key` angezeigt. Wenn Sie gerade ein Konto erstellt haben und noch keinen API-Schlüssel erhalten haben, haben Sie wahrscheinlich noch keinen Schlüssel. Sie können einen neuen Schlüssel erhalten, indem Sie auf die Schaltfläche 'Create Key' oben rechts klicken.

> Nachdem Sie den Schlüssel erhalten haben, wird Ihr API-Schlüssel auf dem Bildschirm angezeigt. Da dieser Schlüssel später nicht mehr eingesehen werden kann, müssen Sie ihn unbedingt an einem sicheren Ort separat notieren.
{: .prompt-warning }

### (Empfohlen) Registrierung des Claude API-Schlüssels als Umgebungsvariable
Um die Claude API in Python- oder Shell-Skripten zu verwenden, muss der API-Schlüssel abgerufen werden. Es ist möglich, den API-Schlüssel direkt im Skript zu speichern, aber wenn das Skript auf GitHub oder auf andere Weise mit anderen geteilt werden muss, ist diese Methode nicht anwendbar. Selbst wenn Sie nicht vorhaben, die Skriptdatei zu teilen, besteht die Gefahr, dass bei einem unbeabsichtigten Leck der Skriptdatei auch der API-Schlüssel mit preisgegeben wird, wenn er in der Skriptdatei gespeichert ist. Daher wird empfohlen, den API-Schlüssel als Umgebungsvariable in einem System zu registrieren, das nur Sie verwenden, und ihn dann im Skript aus dieser Umgebungsvariable abzurufen. Im Folgenden wird die Methode zur Registrierung des API-Schlüssels als Systemumgebungsvariable für UNIX-Systeme vorgestellt. Für Windows sollten Sie andere Anleitungen im Web konsultieren.

1. Öffnen Sie im Terminal einen Editor, indem Sie je nach verwendeter Shell `nano ~/.bashrc` oder `nano ~/.zshrc` eingeben.
2. Fügen Sie `export ANTHROPIC_API_KEY='your-api-key-here'` zum Inhalt der Datei hinzu. Ersetzen Sie 'your-api-key-here' durch Ihren eigenen API-Schlüssel und achten Sie darauf, ihn mit einfachen Anführungszeichen zu umschließen.
3. Speichern Sie die Änderungen und beenden Sie den Editor.
4. Führen Sie im Terminal `source ~/.bashrc` oder `source ~/.zshrc` aus, um die Änderungen zu übernehmen.

### Installation der erforderlichen Python-Pakete
Wenn das anthropic-Paket in Ihrer Python-Umgebung nicht installiert ist, installieren Sie es mit dem folgenden Befehl:
```bash
pip3 install anthropic
```
Außerdem werden die folgenden Pakete benötigt, um das später vorgestellte Skript zur Beitragsübersetzung zu verwenden. Installieren oder aktualisieren Sie sie mit dem folgenden Befehl:
```bash
pip3 install -U argparse tqdm
```

### Erstellung des Python-Skripts
Das in diesem Beitrag vorgestellte Skript zur Beitragsübersetzung besteht aus drei Python-Skriptdateien und einer CSV-Datei:

- `compare_hash.py`: Berechnet die SHA256-Hash-Werte der koreanischen Originalbeiträge im Verzeichnis `_posts/ko`{: .filepath}, vergleicht sie mit den bestehenden Hash-Werten in der Datei `hash.csv` und gibt eine Liste der geänderten oder neu hinzugefügten Dateinamen zurück.
- `hash.csv`: Eine CSV-Datei, die die SHA256-Hash-Werte der bestehenden Beitragsdateien enthält.
- `prompt.py`: Nimmt filepath, source_lang, target_lang als Eingabe, ruft den Claude API-Schlüssel aus der Systemumgebungsvariable ab, ruft die API auf und verwendet den zuvor erstellten Prompt als Systemprompt und den Inhalt des zu übersetzenden Beitrags in 'filepath' als Benutzerprompt. Anschließend erhält es die Antwort (das Übersetzungsergebnis) vom Claude 3.5 Sonnet-Modell und gibt es als Textdatei im Pfad `'../_posts/' + language_code[target_lang] + '/' + filename`{: .filepath} aus.
- `translate_changes.py`: Enthält die String-Variable source_lang und die Liste target_langs, ruft die Funktion `changed_files()` aus `compare_hash.py` auf, um die Liste changed_files zurückzugeben. Wenn es geänderte Dateien gibt, führt es eine doppelte Schleife über alle Dateien in der Liste changed_files und alle Elemente in der Liste target_langs aus und ruft innerhalb dieser Schleife die Funktion `translate(filepath, source_lang, target_lang)` aus `prompt.py` auf, um die Übersetzung durchzuführen.

Der Inhalt der fertigen Skriptdateien kann auch im GitHub-Repository [yunseo-kim/yunseo-kim.github.io](https://github.com/yunseo-kim/yunseo-kim.github.io/tree/main/tools) eingesehen werden.

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
Da diese Datei den zuvor erstellten Prompt-Inhalt enthält und daher etwas länger ist, wird sie durch einen Link zur Quelldatei im GitHub-Repository ersetzt.  
<https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py>

> In der `prompt.py`-Datei unter dem obigen Link ist `max_tokens` eine Variable, die die maximale Ausgabelänge unabhängig von der Größe des Kontextfensters festlegt. Bei der Verwendung der Claude API beträgt die Größe des Kontextfensters, das auf einmal eingegeben werden kann, 200k Token (etwa 680.000 Zeichen), aber unabhängig davon ist für jedes Modell eine maximale Ausgabe-Token-Anzahl festgelegt. Es wird empfohlen, dies vor der API-Nutzung in der [offiziellen Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/about-claude/models) zu überprüfen. Die bisherigen Claude 3-Serienmodelle konnten maximal 4096 Token ausgeben, was bei Tests mit den Beiträgen dieses Blogs für die meisten Beiträge kein Problem darstellte. Bei einigen längeren Beiträgen mit mehr als etwa 8000 koreanischen Zeichen trat jedoch in einigen Ausgabesprachen das Problem auf, dass der hintere Teil der Übersetzung abgeschnitten wurde, weil die 4096 Token überschritten wurden. Bei Claude 3.5 Sonnet wurde die maximale Ausgabe-Token-Anzahl auf das Doppelte, 8192, erhöht, sodass es kaum Probleme mit der Überschreitung dieser maximalen Ausgabe-Token-Anzahl gab. In der `prompt.py`-Datei im obigen GitHub-Repository wurde `max_tokens=8192` festgelegt.
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

### Verwendung des Python-Skripts
Für einen Jekyll-Blog legen Sie innerhalb des Verzeichnisses `/_posts`{: .filepath}, in dem sich die Beiträge befinden, Unterverzeichnisse nach [ISO 639-1](https://www.loc.gov/standards/iso639-2/php/code_list.php) Sprachcodes an, wie `/_posts/ko`{: .filepath}, `/_posts/en`{: .filepath}, `/_posts/pt-BR`{: .filepath}. Platzieren Sie dann die oben vorgestellten Python-Skripte und die CSV-Datei im Verzeichnis `/tools`{: .filepath}, öffnen Sie ein Terminal an diesem Ort und führen Sie den folgenden Befehl aus:

```bash
python3 translate_changes.py
```

Das Skript wird ausgeführt und Sie sollten einen Bildschirm wie den folgenden sehen:  
![Screenshot of running script 1](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-1.png)  
![Screenshot of running script 2](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/translating-screen-2.png)

## Erfahrungsbericht
Wie oben beschrieben, verwende ich die automatische Beitragsübersetzung mit der Claude 3.5 API seit etwa zwei Monaten für diesen Blog. In den meisten Fällen liefert sie Übersetzungen von hervorragender Qualität, ohne dass ein zusätzlicher menschlicher Eingriff erforderlich ist. Ich konnte feststellen, dass nach der mehrsprachigen Übersetzung und Veröffentlichung von Beiträgen tatsächlich organischer Suchverkehr aus Regionen außerhalb Koreas, wie Brasilien, Kanada, den USA und Frankreich, generiert wurde. Neben dem Blogverkehr gab es auch zusätzliche Vorteile für das Lernen des Autors selbst. Da Claude sehr flüssige Texte auf Englisch erstellt, bietet sich beim Überprüfen der Beiträge vor dem Push in das GitHub Pages Repository die Gelegenheit, zu sehen, wie bestimmte Begriffe oder Ausdrücke aus dem koreanischen Original auf natürliche Weise auf Englisch ausgedrückt werden können. Obwohl dies allein nicht für ein umfassendes Englischlernen ausreicht, scheint es für einen Ingenieurstudenten aus einem nicht-englischsprachigen Land wie Korea durchaus vorteilhaft zu sein, regelmäßig und ohne zusätzlichen Aufwand natürliche englische Ausdrücke nicht nur für alltägliche, sondern auch für akademische Ausdrücke und Begriffe anhand des vertrautesten Textes - des selbst geschriebenen - zu sehen.
