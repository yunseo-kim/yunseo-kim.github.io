---
title: Automatische Übersetzung von Posts mit der Claude Sonnet 4 API (1) - Prompt-Design
description: "Behandelt den Prozess der Gestaltung von Prompts für die mehrsprachige Übersetzung von Markdown-Textdateien und der Automatisierung der Arbeit mit Python unter Anwendung des von Anthropic ausgestellten API-Schlüssels und der erstellten Prompts. Dieser Post ist der erste Artikel der entsprechenden Serie und stellt die Methoden und Prozesse des Prompt-Designs vor."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---

## Einführung
Seit der Einführung der Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blog-Posts im Juni 12024 betreibe ich das entsprechende Übersetzungssystem nach mehreren Verbesserungen der Prompts und Automatisierungsskripte sowie Modell-Upgrades über einen Zeitraum von fast einem Jahr zufriedenstellend. In dieser Serie möchte ich die Gründe für die Wahl des Claude Sonnet-Modells im Einführungsprozess, die Methoden des Prompt-Designs sowie die Implementierung der API-Integration und Automatisierung durch Python-Skripte behandeln.  
Die Serie besteht aus 2 Artikeln, und dieser Artikel, den Sie gerade lesen, ist der erste Artikel der entsprechenden Serie.
- Teil 1: Einführung des Claude Sonnet-Modells und Auswahlgründe, Prompt Engineering (Haupttext)
- Teil 2: [Erstellung und Anwendung von Python-Automatisierungsskripten mit der API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## Über Claude Sonnet
Die Claude-Serie-Modelle werden je nach Modellgröße in den Versionen Haiku, Sonnet und Opus angeboten.  
![Claude 3 Modell-Tier-Unterscheidung](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> Bildquelle: [Anthropic Claude API offizielle Webseite](https://www.anthropic.com/api)

> (12025.05.29. Ergänzung)  
> Das Bild wurde vor einem Jahr aufgenommen, daher sind die Token-Preise basierend auf der alten Version Claude 3 angegeben, aber die Unterscheidung nach Modellgröße in Haiku, Sonnet, Opus ist noch gültig. Stand Ende Mai 12025 ist die Preisgestaltung für jedes von Anthropic angebotene Modell wie folgt.
>
> | Model | Base Input <br>Tokens | 5m Cache <br>Writes | 1h Cache <br>Writes | Cache Hits &<br> Refreshes | Output <br>Tokens |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | Claude Opus 4 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Sonnet 4 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.7 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.5 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Haiku 3.5 | $0.80 / MTok | $1 / MTok | $1.6 / MTok | $0.08 / MTok | $4 / MTok |
> | Claude Opus 3 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Haiku 3 | $0.25 / MTok | $0.30 / MTok | $0.50 / MTok | $0.03 / MTok | $1.25 / MTok |
>
> Quelle: [Anthropic developer docs](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

Und das am 21. Juni 12024 koreanischer Zeit von Anthropic veröffentlichte Sprachmodell [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) zeigt bei gleichen Kosten und Geschwindigkeit wie das bisherige Claude 3 Sonnet eine Inferenzleistung, die Claude 3 Opus übertrifft, und wird allgemein als überlegen gegenüber dem Konkurrenzmodell GPT-4 in den Bereichen Schreiben, Sprachlogik, mehrsprachiges Verständnis und Übersetzung bewertet.  
![Claude 3.5 Sonnet Einführungsbild](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet Leistungs-Benchmark-Ergebnisse](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> Bildquelle: [Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## Gründe für die Einführung von Claude 3.5 für die Post-Übersetzung
Auch ohne Sprachmodelle wie Claude 3.5 oder GPT-4 gibt es bereits bestehende kommerzielle Übersetzungs-APIs wie Google Translate oder DeepL. Dennoch entschied ich mich für die Verwendung von LLM für Übersetzungszwecke, weil Benutzer im Gegensatz zu anderen kommerziellen Übersetzungsdiensten durch Prompt-Design dem Modell zusätzliche Kontextinformationen oder Anforderungen wie den Schreibzweck oder das Hauptthema des Textes neben dem Haupttext bereitstellen können, und das Modell kann entsprechend kontextbewusste Übersetzungen liefern.

Obwohl DeepL oder Google Translate im Allgemeinen auch ausgezeichnete Übersetzungsqualität zeigen, haben sie aufgrund der Begrenzung, dass sie das Thema oder den Gesamtkontext des Textes nicht gut erfassen können und keine komplexen Anforderungen separat übermittelt werden können, das Problem, dass die Übersetzungsergebnisse relativ unnatürlich sein können, wenn sie gebeten werden, lange Texte zu professionellen Themen zu übersetzen, die nicht alltägliche Konversation sind, und es ist schwierig, genau in dem benötigten spezifischen Format (Markdown, YAML frontmatter usw.) auszugeben.

Insbesondere Claude wurde, wie oben erwähnt, oft als relativ überlegen gegenüber dem Konkurrenzmodell GPT-4 in den Bereichen Schreiben, Sprachlogik, mehrsprachiges Verständnis und Übersetzung bewertet, und als ich es direkt einfach testete, zeigte es auch eine etwas glattere Übersetzungsqualität als GPT-4, weshalb ich es im Juni 12024, als ich die Einführung in Betracht zog, als geeignet für die Übersetzung der in diesem Blog veröffentlichten ingenieursbezogenen Artikel in mehrere Sprachen beurteilte.

## Modell-Adoptionshistorie und aktueller Status
### 12024.07.01.
Wie in [einem separaten Artikel](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/) zusammengefasst, [wurde die anfängliche Arbeit der Anwendung des Polyglot-Plugins und der entsprechenden Modifikation von `_config.yml`{: .filepath}, HTML-Header und Sitemap abgeschlossen.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Anschließend [wurde das Claude 3.5 Sonnet-Modell für Übersetzungszwecke adoptiert und nach der anfänglichen Implementierung und Verifizierung des in dieser Serie behandelten API-integrierten Python-Skripts angewendet.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
Am 22. Oktober 12024 kündigte Anthropic die Upgrade-Version der Claude 3.5 Sonnet API ("claude-3-5-sonnet-20241022") und Claude 3.5 Haiku an. Aufgrund des [später beschriebenen Problems](#faulheit-verhindern-120241031-halloween-patch) wird jedoch noch die bestehende "claude-3-5-sonnet-20240620" API in diesem Blog angewendet.

### 12025.04.02.
[Das angewendete Modell wurde von "claude-3-5-sonnet-20240620" auf "claude-3-7-sonnet-20250219" umgestellt.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[Das angewendete Modell wurde von "claude-3-7-sonnet-20250219" auf "claude-sonnet-4-20250514" umgestellt.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Claude 4 Leistungs-Benchmark-Ergebnisse](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> Bildquelle: [Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

Je nach Nutzungsbedingungen kann es Unterschiede geben, aber im Allgemeinen herrscht seit dem Erscheinen des Claude 3.7 Sonnet-Modells die Meinung vor, dass Claude das stärkste Modell für das Programmieren ist. Anthropic selbst bewirbt aktiv die überlegene Programmierleistung gegenüber Konkurrenzmodellen von OpenAI oder Google als Hauptstärke ihrer eigenen Modelle. Auch bei der diesmaligen Ankündigung von Claude Opus 4 und Claude Sonnet 4 kann man bestätigen, dass sie die Programmierleistung betonen und die Entwickler als Hauptzielgruppe anvisieren.

Natürlich zeigen die veröffentlichten Benchmark-Ergebnisse, dass auch in anderen Bereichen als dem Programmieren insgesamt Verbesserungen erzielt wurden, und für die in diesem Artikel behandelte Übersetzungsarbeit dürften insbesondere die Leistungsverbesserungen in den Bereichen mehrsprachige Frage-Antwort (MMMLU) oder mathematische Problemlösung (AIME 2025) besonders wirksam sein. Bei direkten einfachen Tests konnte ich bestätigen, dass die Übersetzungsergebnisse von Claude Sonnet 4 gegenüber dem vorherigen Modell Claude 3.7 Sonnet in Bezug auf Natürlichkeit der Ausdrucksweise, Fachlichkeit und Konsistenz der Terminologie überlegen sind.

> Zum jetzigen Zeitpunkt denke ich, dass Claude-Modelle zumindest für die Übersetzung von technisch orientierten, auf Koreanisch verfassten Texten wie denen in diesem Blog in mehrere Sprachen immer noch am besten sind. Allerdings hat sich die Leistung von Googles Gemini-Modell in letzter Zeit merklich verbessert, und im Mai dieses Jahres wurde sogar das Gemini 2.5-Modell veröffentlicht, wenn auch noch im Preview-Stadium.  
> Beim Vergleich der Modelle Gemini 2.0 Flash, Claude 3.7 Sonnet und Claude Sonnet 4 beurteilte ich Claudes Übersetzungsleistung als überlegen, aber Geminis mehrsprachige Leistung ist ebenfalls ziemlich ausgezeichnet, und die Fähigkeiten zur Lösung und Beschreibung von Mathematik- und Physikproblemen sind bei Gemini 2.5 Preview 05-06 sogar besser als bei Claude Opus 4, sodass ich nicht garantieren kann, wie es sein wird, wenn dieses Modell offiziell veröffentlicht wird und erneut verglichen wird.  
> Angesichts der im Vergleich zu Claude etwas günstigeren API-Gebühren ist Geminis Preiskonkurrenzfähigkeit überlegen, sodass Gemini eine vernünftige Alternative werden könnte, wenn nur eine einigermaßen gleichwertige Leistung erzielt wird. Da Gemini 2.5 noch im Preview-Stadium ist, halte ich es für zu früh, es für die tatsächliche Automatisierung anzuwenden, und berücksichtige es derzeit nicht, aber ich plane, es zu testen, wenn die offizielle Version in Zukunft veröffentlicht wird.
{: .prompt-tip }

## Prompt-Design
### Grundprinzipien beim Anfordern von etwas
Um von einem Sprachmodell zufriedenstellende Ergebnisse zu erhalten, die dem Zweck entsprechen, muss man entsprechende angemessene Prompts bereitstellen. Prompt-Design mag überwältigend erscheinen, aber tatsächlich unterscheidet sich die "Methode, etwas gut anzufordern" nicht wesentlich, ob der Gegenüber ein Sprachmodell oder ein Mensch ist, sodass es nicht besonders schwierig ist, wenn man es aus dieser Perspektive angeht. Es ist gut, die aktuelle Situation und Anforderungen nach den sechs W-Fragen klar zu erklären und bei Bedarf einige konkrete Beispiele hinzuzufügen. Es gibt unzählige Tipps und Techniken zum Prompt-Design, aber die meisten leiten sich von den nachfolgend beschriebenen Grundprinzipien ab.

#### Gesamtton
Es gibt viele Berichte, dass Sprachmodelle qualitativ hochwertigere Antworten ausgeben, wenn Prompts in einem höflich bittenden Ton anstatt in einem autoritären Befehlston verfasst und eingegeben werden. Normalerweise ist auch in der Gesellschaft die Wahrscheinlichkeit höher, dass der Gegenüber eine Aufgabe gewissenhafter ausführt, wenn man höflich bittet anstatt autoritär zu befehlen, und Sprachmodelle scheinen solche Antwortmuster von Menschen zu lernen und nachzuahmen.

#### Rollenzuweisung und Situationserklärung (wer, warum)
Zuerst wurde Claude 4 die Rolle eines *'professionellen technischen Übersetzers (professional technical translator)'* zugewiesen und Kontextinformationen über den Benutzer als *"Ingenieursblogger, der hauptsächlich Artikel über Mathematik, Physik und Datenwissenschaft schreibt"* bereitgestellt.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Übermittlung der Anforderungen im großen Rahmen (was)
Als nächstes wurde darum gebeten, den vom Benutzer bereitgestellten Text im Markdown-Format von {source_lang} nach {target_lang} zu übersetzen, während das Format beibehalten wird.

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Beim Aufruf der Claude API werden die Plätze {source_lang} und {target_lang} im Prompt durch die f-string-Funktion des Python-Skripts mit den Variablen für Ausgangs- und Zielsprache der Übersetzung ersetzt.
{: .prompt-info }

#### Konkretisierung der Anforderungen und Beispiele (wie)
Bei einfachen Aufgaben können die vorherigen Schritte ausreichen, um die gewünschten Ergebnisse zu erzielen, aber bei komplexen Aufgaben können zusätzliche Erklärungen erforderlich sein.

Wenn die Anforderungen komplex und vielfältig sind, verbessert sich die Lesbarkeit und das Verständnis (sowohl für Menschen als auch für Sprachmodelle), wenn man jeden Punkt in einer Liste aufführt, anstatt sie ausführlich zu beschreiben. Außerdem ist es hilfreich, bei Bedarf auch Beispiele bereitzustellen.
In diesem Fall wurden folgende Bedingungen hinzugefügt.

##### Behandlung des YAML front matter
Im YAML front matter am Anfang von für Jekyll-Blogs geschriebenen Markdown-Posts werden Informationen zu 'title', 'description', 'categories' und 'tags' aufgezeichnet. Zum Beispiel ist das YAML front matter dieses Artikels wie folgt.

```yaml
---
title: Claude Sonnet 4 API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인
description: >-
  마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic으로부터 발급받은
  API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 
  이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

Beim Übersetzen von Posts müssen jedoch die Titel- (title) und Beschreibungs- (description) Tags in mehrere Sprachen übersetzt werden, aber für die Konsistenz der Post-URLs ist es für die Wartung vorteilhaft, die Kategorie- (categories) und Tag- (tags) Namen nicht zu übersetzen und auf Englisch zu belassen. Daher wurde die folgende Anweisung gegeben, um andere Tags außer 'title' und 'description' nicht zu übersetzen. Da Claude bereits Informationen über YAML front matter gelernt haben und kennen wird, reicht diese Erklärung in den meisten Fällen aus.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> Der Zusatz "under any circumstances, regardless of the language you are translating to" betont **ausnahmslos**, dass andere Tags des YAML front matter nicht willkürlich geändert werden sollen.
{: .prompt-tip }

(12025.04.02. Update)  
Außerdem wurde angewiesen, den Inhalt des description-Tags unter SEO-Gesichtspunkten in angemessener Länge zu verfassen.

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Behandlung von Fällen, in denen der bereitgestellte Originaltext andere Sprachen als die Ausgangssprache enthält
Beim Verfassen von Originaltexten auf Koreanisch gibt es oft Fälle, in denen beim ersten Vorstellen der Definition eines Konzepts oder bei der Verwendung einiger Fachbegriffe englische Ausdrücke in Klammern wie '*중성자 감쇠 (Neutron Attenuation)*' hinzugefügt werden. Bei der Übersetzung solcher Ausdrücke gab es das Problem inkonsistenter Übersetzungsmethoden, manchmal wurden die Klammern beibehalten, manchmal wurde das in den Klammern angegebene Englisch weggelassen, weshalb folgende detaillierte Richtlinien festgelegt wurden.
- Bei Fachbegriff:
  - Bei der Übersetzung in nicht-römische Sprachen wie Japanisch wird das Format 'Übersetzungsausdruck(englischer Ausdruck)' beibehalten.
  - Bei der Übersetzung in römische Sprachen wie Spanisch, Portugiesisch, Französisch sind sowohl die alleinige Angabe 'Übersetzungsausdruck' als auch die kombinierte Angabe 'Übersetzungsausdruck(englischer Ausdruck)' erlaubt, und Claude kann autonom das geeignetere auswählen.
- Bei Eigennamen muss die ursprüngliche Schreibweise in irgendeiner Form im Übersetzungsergebnis erhalten bleiben.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases.
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it.
  2. it may be a proper noun such as a person's name or a place name.
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language,
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'.
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Behandlung von Links zu anderen Posts
Einige Posts enthalten Links zu anderen Posts, aber in der Testphase, als keine separaten Richtlinien dazu bereitgestellt wurden, interpretierte das System oft auch den Pfadteil der URL als zu übersetzenden Gegenstand und änderte ihn, wodurch interne Links häufig brachen. Dieses Problem wurde durch Hinzufügung dieses Satzes zum Prompt gelöst.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(12025.04.06. Update)  
Wenn die obigen Richtlinien bereitgestellt werden, wird der Pfadteil von Links bei der Übersetzung korrekt behandelt, wodurch die Häufigkeit von Link-Brüchen erheblich reduziert wird. Bei Links mit Fragment-Identifiern besteht jedoch immer noch die Begrenzung, dass das Sprachmodell den Fragment-Identifer-Teil grob schätzen und ausfüllen muss, es sei denn, es kennt den Inhalt des verlinkten Zielartikels, wodurch eine grundlegende Problemlösung unmöglich war. Daher wurden das Python-Skript und der Prompt verbessert, um Kontextinformationen über andere verlinkte Posts im `<reference_context>` XML-Tag des Benutzer-Prompts bereitzustellen und die Link-Übersetzung entsprechend diesem Kontext zu behandeln. Nach Anwendung dieses Updates konnte das Problem der Link-Brüche größtenteils verhindert werden, und bei eng verbundenen Serien-Artikeln kann auch der Effekt einer konsistenteren Übersetzung über mehrere Posts hinweg erwartet werden.

Im System-Prompt wird folgende Richtlinie präsentiert.
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

Und der `<reference_context>`-Teil des Benutzer-Prompts ist in folgendem Format und Inhalt zusammengestellt und wird zusätzlich nach dem Inhalt des zu übersetzenden Haupttexts bereitgestellt.
```xml
<reference_context>
The following are contents of posts linked with hash fragments in the original post. 
Use these for context when translating links and references:

<referenced_post path="{post_1_path}" hash="{hash_fragment_1}">
{post_content}
</referenced_post>

<referenced_post path="{post__2_path}" hash="{hash_fragment_2}">
{post_content}
</referenced_post>

...

</reference_context>
```

> Wie dies konkret implementiert wurde, siehe [Teil 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) dieser Serie und den Inhalt des [Python-Skripts](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) im GitHub-Repository.
{: .prompt-tip }

##### Nur Übersetzungsergebnisse als Antwort ausgeben
Schließlich wird folgender Satz präsentiert, um bei der Antwort keine anderen Worte hinzuzufügen und nur die Übersetzungsergebnisse auszugeben.

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Zusätzliche Prompt-Design-Techniken
Im Gegensatz zu Arbeitsanfragen an Menschen gibt es jedoch auch zusätzliche Techniken, die speziell für Sprachmodelle gelten.
Obwohl es viele nützliche Materialien dazu im Web gibt, sind hier einige repräsentative Tipps zusammengefasst, die universell nützlich angewendet werden können.  
Hauptsächlich wurde der [Prompt Engineering Guide der offiziellen Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) als Referenz verwendet.

#### Strukturierung mit XML-Tags
Tatsächlich wurde dies bereits die ganze Zeit verwendet. Bei komplexen Prompts, die verschiedene Kontexte, Anweisungen, Formate und Beispiele enthalten, hilft die angemessene Verwendung von XML-Tags wie `<instructions>`, `<example>`, `<format>` dem Sprachmodell dabei, den Prompt genau zu interpretieren und qualitativ hochwertige Ausgaben zu produzieren, die der Absicht entsprechen. Im GitHub-Repository [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) sind nützliche XML-Tags für das Schreiben von Prompts gut zusammengefasst, daher wird empfohlen, diese als Referenz zu verwenden.

#### Schrittweise Argumentation (CoT, chain of thinking) Technik
Bei Aufgaben, die ein erhebliches Maß an Argumentation erfordern, wie das Lösen mathematischer Probleme oder das Verfassen komplexer Dokumente, kann die Leistung erheblich gesteigert werden, wenn man das Sprachmodell dazu anleitet, das Problem schrittweise zu durchdenken. In diesem Fall kann sich jedoch die Antwortlatenz verlängern, und diese Technik ist nicht immer für alle Aufgaben nützlich, daher ist Vorsicht geboten.

#### Prompt-Chaining-Technik
Bei komplexen Aufgaben kann ein einzelner Prompt an seine Grenzen stoßen. In diesem Fall kann man erwägen, den gesamten Arbeitsablauf von Anfang an in mehrere Schritte zu unterteilen, für jeden Schritt spezialisierte Prompts zu präsentieren und die Antwort aus dem vorherigen Schritt als Eingabe für den nächsten Schritt zu übertragen. Diese Technik wird Prompt-Chaining genannt.

#### Vorab-Ausfüllen des Antwortanfangs
Beim Eingeben von Prompts kann man den ersten Teil des zu antwortenden Inhalts vorab präsentieren und die Fortsetzung der Antwort schreiben lassen, wodurch unnötige Begrüßungen und andere Einleitungen übersprungen oder Antworten in bestimmten Formaten wie XML oder JSON erzwungen werden können. [Bei der Claude API kann diese Technik verwendet werden, indem beim Aufruf nicht nur `User`-Nachrichten, sondern auch `Assistant`-Nachrichten zusammen übermittelt werden.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Faulheit verhindern (12024.10.31. Halloween-Patch)
Nach der ersten Erstellung dieses Artikels gab es zwischenzeitlich ein- oder zweimal zusätzliche Prompt-Verbesserungen und Konkretisierungen von Anweisungen, aber jedenfalls gab es 4 Monate lang bei der Anwendung dieses Automatisierungssystems keine größeren Probleme.

Aber ab etwa 18:00 Uhr koreanischer Zeit am 12024.10.31. trat kontinuierlich das seltsame Phänomen auf, dass bei der Übersetzungsarbeit für neu geschriebene Posts nur der erste 'TL;DR'-Teil des Posts übersetzt und die Übersetzung willkürlich abgebrochen wurde.

Die vermuteten Ursachen und Lösungsmethoden für dieses Problem wurden in [einem separaten Post](/posts/does-ai-hate-to-work-on-halloween) behandelt, bitte beziehen Sie sich auf diesen Artikel.

### Vollständiger System-Prompt
Das Ergebnis des Prompt-Designs nach den obigen Schritten kann im [nächsten Teil](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) eingesehen werden.

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
