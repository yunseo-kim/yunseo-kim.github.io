---
title: Wie man Posts automatisch mit der Claude 3.5 Sonnet API übersetzt (1) - Prompt-Design
description: Dieser Beitrag behandelt den Prozess des Designs von Prompts für die
  mehrsprachige Übersetzung von Markdown-Textdateien und die Automatisierung der Arbeit
  mit Python unter Verwendung eines von Anthropic ausgestellten API-Schlüssels und
  des erstellten Prompts. Dies ist der erste Beitrag in der Serie und stellt die Methoden
  und Prozesse des Prompt-Designs vor.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Einführung
Kürzlich habe ich die Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blog-Posts eingeführt. In dieser Serie werde ich die Gründe für die Wahl der Claude 3.5 Sonnet API, die Methoden des Prompt-Designs sowie die Implementierung der API-Integration und Automatisierung mittels Python-Skript erläutern.  
Die Serie besteht aus zwei Artikeln, und dieser Artikel ist der erste Teil der Serie.
- Teil 1: Einführung des Claude 3.5 Sonnet Modells und Auswahlgründe, Prompt Engineering (dieser Artikel)
- Teil 2: [Erstellung und Anwendung des Python-Automatisierungsskripts mit der API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Über Claude 3.5 Sonnet
Die Claude 3 Serienmodelle werden je nach Modellgröße in den Versionen Haiku, Sonnet und Opus angeboten.  
![Claude 3 Modell-Tier-Unterscheidung](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Bildquelle: [Anthropic Claude API offizielle Webseite](https://www.anthropic.com/api)

Am 21. Juni 2024 (koreanische Zeit) veröffentlichte Anthropic das neueste Sprachmodell [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Laut Anthropics Ankündigung übertrifft es die Schlussfolgerungsleistung von Claude 3 Opus bei gleichen Kosten und Geschwindigkeit wie Claude 3 Sonnet. Es wird allgemein als dem Konkurrenzmodell GPT-4 überlegen in den Bereichen Textkomposition, sprachliche Schlussfolgerung, mehrsprachiges Verständnis und Übersetzung angesehen.  
![Claude 3.5 Sonnet Einführungsbild](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet Leistungs-Benchmark-Ergebnisse](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Bildquelle: [Anthropic Homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

(Ergänzung vom 31.10.2024) Am 22. Oktober 2024 kündigte Anthropic eine Upgrade-Version der Claude 3.5 Sonnet API ("claude-3-5-sonnet-20241022") und Claude 3.5 Haiku an. Aufgrund des [später beschriebenen Problems](#verhinderung-von-faulheit-halloween-patch-31102024) wird in diesem Blog jedoch noch die bestehende "claude-3-5-sonnet-20240620" API verwendet.

## Gründe für die Einführung von Claude 3.5 für Post-Übersetzungen
Es gibt bereits kommerzielle Übersetzungs-APIs wie Google Translate oder DeepL, auch ohne Sprachmodelle wie Claude 3.5 oder GPT-4. Der Grund, warum ich mich dennoch für ein LLM zu Übersetzungszwecken entschieden habe, liegt darin, dass man im Gegensatz zu anderen kommerziellen Übersetzungsdiensten durch Prompt-Design dem Modell zusätzliche Kontextinformationen oder Anforderungen wie den Schreibzweck oder die Hauptthemen des Textes bereitstellen kann, und das Modell kann die Übersetzung entsprechend kontextbezogen durchführen. DeepL und Google Translate liefern zwar im Allgemeinen auch hervorragende Übersetzungsqualität, aber aufgrund der Einschränkung, dass sie das Thema und den Gesamtkontext nicht gut erfassen können, sind die Übersetzungsergebnisse bei längeren Texten zu fachlichen Themen im Vergleich relativ unnatürlich. Insbesondere Claude wird im Vergleich zum Konkurrenzmodell GPT-4 in den Bereichen Textkomposition, sprachliche Schlussfolgerung, mehrsprachiges Verständnis und Übersetzung als relativ überlegen eingeschätzt, und auch bei einem einfachen Test zeigte es eine flüssigere Übersetzungsqualität als GPT-4. Daher hielt ich es für geeignet für die Übersetzung der technischen Artikel in diesem Blog in verschiedene Sprachen.

## Prompt-Design
### Grundprinzipien beim Stellen von Anfragen
Um zufriedenstellende, zweckdienliche Ergebnisse von einem Sprachmodell zu erhalten, muss man einen angemessenen Prompt bereitstellen. Prompt-Design mag zunächst einschüchternd erscheinen, aber tatsächlich unterscheidet sich "die Art, wie man etwas gut anfragt" nicht wesentlich, ob der Gegenüber ein Sprachmodell oder ein Mensch ist. Wenn man es aus dieser Perspektive betrachtet, ist es gar nicht so schwierig. Es ist hilfreich, die aktuelle Situation und Anforderungen nach den W-Fragen klar zu erklären und bei Bedarf einige konkrete Beispiele hinzuzufügen. Es gibt viele Tipps und Techniken für Prompt-Design, aber die meisten leiten sich von den nachfolgend beschriebenen Grundprinzipien ab.

#### Allgemeiner Tonfall
Es gibt viele Berichte, dass Sprachmodelle qualitativ hochwertigere Antworten liefern, wenn Prompts in einem höflich anfragenden Ton statt in einem befehlenden Ton formuliert werden. Auch im gesellschaftlichen Umgang ist die Wahrscheinlichkeit höher, dass jemand eine Aufgabe gewissenhafter ausführt, wenn man ihn höflich darum bittet, statt zu befehlen. Sprachmodelle scheinen dieses menschliche Antwortmuster gelernt zu haben und zu imitieren.

#### Rollenzuweisung und Situationsbeschreibung (Wer, Warum)
Zunächst wurde Claude 3.5 die Rolle eines "professionellen technischen Übersetzers" zugewiesen und Kontextinformationen über den Benutzer als "Technik-Blogger, der hauptsächlich über Mathematik, Physik und Data Science schreibt" bereitgestellt.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Übermittlung der grundlegenden Anforderungen (Was)
Als Nächstes wurde angefordert, den vom Benutzer bereitgestellten Markdown-formatierten Text von {source_lang} nach {target_lang} unter Beibehaltung des Formats zu übersetzen.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Bei Claude API-Aufrufen werden die Platzhalter {source_lang} und {target_lang} im Prompt durch die Ausgangs- und Zielsprachvariablen mittels der f-string-Funktion des Python-Skripts ersetzt.
{: .prompt-info }

#### Konkretisierung der Anforderungen und Beispiele (Wie)
Bei einfachen Aufgaben können die vorherigen Schritte ausreichen, um das gewünschte Ergebnis zu erhalten, aber bei komplexeren Aufgaben können zusätzliche Erklärungen erforderlich sein.

Wenn die Anforderungen komplex und vielfältig sind, ist es übersichtlicher und verständlicher für den Leser (sei es Mensch oder Sprachmodell), sie in Form einer Liste zu präsentieren, anstatt sie ausführlich zu beschreiben. Auch die Bereitstellung von Beispielen kann hilfreich sein.
In diesem Fall wurden folgende Bedingungen hinzugefügt:

##### Behandlung des YAML Front Matter
Der YAML Front Matter am Anfang eines in Markdown geschriebenen Posts für einen Jekyll-Blog enthält Informationen zu 'title', 'description', 'categories' und 'tags'. Zum Beispiel sieht der YAML Front Matter dieses Artikels wie folgt aus:

```yaml
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: \>-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

Bei der Übersetzung des Posts müssen zwar Titel (title) und Beschreibung (description) in verschiedene Sprachen übersetzt werden, aber für die Konsistenz der Post-URLs ist es für die Wartung vorteilhaft, die Kategorie- (categories) und Tag-Namen (tags) unverändert in Englisch zu belassen. Daher wurde folgende Anweisung hinzugefügt, um sicherzustellen, dass außer 'title' und 'description' keine Tags übersetzt werden. Da Claude bereits Informationen über YAML Front Matter gelernt hat, sollte diese Erklärung in den meisten Fällen ausreichen.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Die Phrase "under any circumstances, regardless of the language you are translating to" wurde hinzugefügt, um zu betonen, dass **ausnahmslos** keine anderen Tags im YAML Front Matter modifiziert werden sollen.
{: .prompt-tip }

##### Behandlung von Texten in anderen Sprachen als der Ausgangssprache
Beim Schreiben des Originaltexts auf Koreanisch wird oft bei der ersten Einführung eines Konzepts oder bei der Verwendung bestimmter Fachbegriffe der englische Ausdruck in Klammern beigefügt, wie zum Beispiel '*중성자 감쇠 (Neutron Attenuation)*'. Für die Übersetzung solcher Ausdrücke wurden folgende detaillierte Richtlinien festgelegt, da es Inkonsistenzen gab, bei denen manchmal die Klammern beibehalten und manchmal der englische Ausdruck in Klammern weggelassen wurde:
- Bei Fachbegriffen:
  - Bei der Übersetzung in nicht-romanische Sprachen wie Japanisch wird das Format 'Übersetzung(englischer Ausdruck)' beibehalten.
  - Bei der Übersetzung in romanische Sprachen wie Spanisch, Portugiesisch oder Französisch sind sowohl die alleinige Angabe der 'Übersetzung' als auch die kombinierte Angabe 'Übersetzung(englischer Ausdruck)' zulässig, wobei Claude selbstständig die angemessenere Option wählen kann.
- Bei Eigennamen muss die Originalschreibweise in irgendeiner Form in der Übersetzung erhalten bleiben.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
  2. it may be a proper noun such as a person's name or a place name. \n\
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
      You can choose whichever you think is more appropriate.</example>\n\
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Behandlung von Links zu anderen Posts
Einige Posts enthalten Links zu anderen Posts. In der Testphase trat häufig das Problem auf, dass interne Links unterbrochen wurden, weil das Modell ohne spezifische Anweisungen auch den Pfadteil der URL als zu übersetzenden Text interpretierte. Dieses Problem wurde durch Hinzufügen der folgenden Anweisung gelöst:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Nur Übersetzungsergebnisse als Antwort ausgeben
Schließlich wurde der folgende Satz hinzugefügt, um sicherzustellen, dass nur die Übersetzungsergebnisse ohne zusätzliche Kommentare ausgegeben werden:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Zusätzliche Prompt-Design-Techniken
Im Gegensatz zu Anfragen an Menschen gibt es bei Sprachmodellen zusätzliche spezifische Techniken.
Es gibt viele nützliche Ressourcen dazu im Internet, aber hier sind einige der wichtigsten allgemein anwendbaren Tipps zusammengefasst.  
Diese basieren hauptsächlich auf dem [Prompt Engineering Guide in der offiziellen Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Strukturierung durch XML-Tags
Tatsächlich wurde dies bereits in den vorherigen Abschnitten verwendet. Bei komplexen Prompts mit verschiedenen Kontexten, Anweisungen, Formaten und Beispielen kann die angemessene Verwendung von XML-Tags wie `<instructions>`, `<example>`, `<format>` dem Sprachmodell helfen, den Prompt genau zu interpretieren und qualitativ hochwertige, beabsichtigte Ausgaben zu erzeugen. Das [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub-Repository enthält eine gute Zusammenstellung nützlicher XML-Tags für das Prompt-Writing.

#### Chain of Thinking (CoT) Technik
Bei Aufgaben, die erhebliches Denken erfordern, wie mathematische Problemlösung oder komplexe Dokumentenerstellung, kann die Leistung deutlich verbessert werden, wenn das Sprachmodell dazu angeleitet wird, das Problem in Schritte zu unterteilen. Allerdings kann dies zu längeren Antwortzeiten führen und ist nicht für alle Aufgaben gleichermaßen nützlich.

#### Prompt Chaining Technik
Bei komplexen Aufgaben können einzelne Prompts an ihre Grenzen stoßen. In solchen Fällen kann es sinnvoll sein, den gesamten Arbeitsablauf von Anfang an in mehrere Schritte zu unterteilen, für jeden Schritt spezifische Prompts zu erstellen und die Antworten aus vorherigen Schritten als Eingabe für den nächsten Schritt zu verwenden. Diese Technik wird als Prompt Chaining bezeichnet.

#### Vorausfüllen des Antwortanfangs
Beim Eingeben eines Prompts kann man den Anfang der erwarteten Antwort vorgeben und das Modell auffordern, die Antwort fortzusetzen. Dies kann unnötige Begrüßungsfloskeln vermeiden oder das Modell zwingen, in einem bestimmten Format wie XML oder JSON zu antworten. [Bei der Claude API kann diese Technik verwendet werden, indem man bei einem API-Aufruf neben der `User`-Nachricht auch eine `Assistant`-Nachricht übermittelt.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Verhinderung von Faulheit (Halloween-Patch 31.10.2024)
Seit der ersten Erstellung dieses Artikels gab es ein oder zwei kleinere Prompt-Verbesserungen und Präzisierungen der Anweisungen, aber das automatisierte System lief vier Monate lang ohne größere Probleme.

Allerdings trat ab etwa 18 Uhr koreanischer Zeit am 31.10.2024 kontinuierlich die Anomalie auf, dass bei der Übersetzung neuer Posts nur der erste "TL;DR"-Teil übersetzt und die Übersetzung dann willkürlich abgebrochen wurde.

Die vermuteten Ursachen und Lösungen für dieses Problem werden in einem [separaten Post](/posts/does-ai-hate-to-work-on-halloween) behandelt, bitte lesen Sie diesen Artikel für weitere Details.

### Der fertige Prompt
Das Ergebnis des oben beschriebenen Prompt-Designs sieht wie folgt aus:

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role> The customer's request is as follows:\n\n \
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task> \
In the provided markdown format text, \n\
  - <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
  - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
    1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
    2. it may be a proper noun such as a person's name or a place name. \n\
    After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
    <if>it is the first case, and the target language is not a Roman alphabet-based language, \
    please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
      - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
      - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
    <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
      - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
        You can choose whichever you think is more appropriate.</example>\n\
      - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
        French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
    <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
      - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
        In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
        redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
    </condition>\n\n\
  - <condition><if>the provided text contains links in markdown format, \
    please translate the link text and the fragment part of the URL into {target_lang}, \
    but keep the path part of the URL intact.</if> \n\
    - <example> the German translation of '[중성자 상호작용과 반응단면적]\
      (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
      would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
      #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
