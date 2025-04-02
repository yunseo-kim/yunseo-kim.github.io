---
title: Wie man Posts mit der Claude 3.5 Sonnet API automatisch übersetzt (1) - Prompt-Design
description: Dieser Beitrag behandelt das Design von Prompts für die mehrsprachige Übersetzung von Markdown-Textdateien und die Automatisierung des Prozesses mit Python unter Verwendung eines API-Schlüssels von Anthropic. Dies ist der erste Teil der Serie, der die Methoden und den Prozess des Prompt-Designs vorstellt.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Einleitung
Kürzlich habe ich die Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung meiner Blogbeiträge eingeführt. In dieser Serie möchte ich die Gründe für die Wahl der Claude 3.5 Sonnet API, die Methoden des Prompt-Designs sowie die Implementierung der API-Integration und Automatisierung mit Python-Skripten erläutern.  
Die Serie besteht aus zwei Beiträgen, und dieser Artikel ist der erste Teil.
- Teil 1: Einführung in das Claude 3.5 Sonnet-Modell und Gründe für die Auswahl, Prompt Engineering (dieser Beitrag)
- Teil 2: [Erstellung und Anwendung von Python-Automatisierungsskripten mit der API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Über Claude 3.5 Sonnet
Die Claude 3-Modellreihe wird je nach Modellgröße in den Versionen Haiku, Sonnet und Opus angeboten.  
![Claude 3 Modell-Tier-Unterscheidung](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Bildquelle: [Anthropic Claude API offizielle Webseite](https://www.anthropic.com/api)

Am 21. Juni 12024 nach dem [Holozän-Kalender](https://en.wikipedia.org/wiki/Holocene_calendar) (koreanische Zeit) veröffentlichte Anthropic sein neuestes Sprachmodell [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Laut Anthropic bietet es zu den gleichen Kosten und mit der gleichen Geschwindigkeit wie Claude 3 Sonnet eine Schlussfolgerungsleistung, die Claude 3 Opus übertrifft. Es gilt allgemein als dem Konkurrenzmodell GPT-4 in Bereichen wie Textkomposition, sprachlichem Denken, mehrsprachigem Verständnis und Übersetzung überlegen.  
![Claude 3.5 Sonnet Einführungsbild](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet Leistungs-Benchmark-Ergebnisse](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Bildquelle: [Anthropic Homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

(Ergänzung vom 31.10.12024) Am 22. Oktober 12024 kündigte Anthropic eine aktualisierte Version der Claude 3.5 Sonnet API ("claude-3-5-sonnet-20241022") und Claude 3.5 Haiku an. Aufgrund des [später beschriebenen Problems](#verhinderung-von-faulheit-halloween-patch-vom-31102024) verwende ich in diesem Blog jedoch noch die ursprüngliche "claude-3-5-sonnet-20240620" API.

## Warum ich Claude 3.5 für die Übersetzung von Beiträgen eingeführt habe
Es gibt bereits kommerzielle Übersetzungs-APIs wie Google Translate oder DeepL, die keine großen Sprachmodelle wie Claude 3.5 oder GPT-4 benötigen. Der Grund, warum ich mich dennoch für ein LLM zur Übersetzung entschieden habe, liegt darin, dass man im Gegensatz zu anderen kommerziellen Übersetzungsdiensten durch Prompt-Design dem Modell zusätzliche Kontextinformationen oder Anforderungen wie den Schreibzweck oder die Hauptthemen des Textes mitteilen kann, und das Modell kann entsprechend eine kontextbezogene Übersetzung liefern. Obwohl DeepL und Google Translate im Allgemeinen eine hervorragende Übersetzungsqualität bieten, können ihre Ergebnisse bei längeren Texten zu fachlichen Themen aufgrund der begrenzten Erfassung des Themas oder des Gesamtkontexts relativ unnatürlich wirken. Wie bereits erwähnt, gilt Claude im Vergleich zum Konkurrenzmodell GPT-4 als überlegen in den Bereichen Textkomposition, sprachliches Denken, mehrsprachiges Verständnis und Übersetzung. Bei einem einfachen Test lieferte es im Vergleich zu GPT-4o flüssigere Übersetzungen, weshalb ich es für die Übersetzung der technischen Beiträge in diesem Blog in verschiedene Sprachen als geeignet erachte.

## Prompt-Design
### Grundprinzipien für Anfragen
Um zufriedenstellende Ergebnisse von einem Sprachmodell zu erhalten, muss man einen geeigneten Prompt bereitstellen. Prompt-Design mag zunächst überwältigend erscheinen, aber im Grunde unterscheidet sich "wie man etwas gut anfragt" nicht wesentlich, ob der Empfänger ein Sprachmodell oder ein Mensch ist. Es ist hilfreich, die aktuelle Situation und die Anforderungen nach den sechs W-Fragen klar zu erklären und bei Bedarf einige konkrete Beispiele hinzuzufügen. Es gibt viele Tipps und Techniken für das Prompt-Design, aber die meisten leiten sich von den folgenden Grundprinzipien ab.

#### Allgemeiner Tonfall
Es gibt viele Berichte, dass Sprachmodelle qualitativ hochwertigere Antworten liefern, wenn Prompts in einem höflichen, bittenden Ton statt in einem befehlenden Ton formuliert werden. Auch im sozialen Umgang ist es wahrscheinlicher, dass jemand eine Aufgabe gewissenhafter erledigt, wenn man höflich darum bittet, statt barsch zu befehlen. Sprachmodelle scheinen dieses menschliche Antwortmuster zu lernen und nachzuahmen.

#### Rollenzuweisung und Situationsbeschreibung (Wer, Warum)
Zunächst habe ich Claude 3.5 die Rolle eines *"professionellen technischen Übersetzers"* zugewiesen und Kontextinformationen über den Benutzer als *"Technik-Blogger, der hauptsächlich über Mathematik, Physik und Datenwissenschaft schreibt"* bereitgestellt.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Übermittlung der allgemeinen Anforderungen (Was)
Als Nächstes bat ich darum, den vom Benutzer bereitgestellten Markdown-Text von {source_lang} nach {target_lang} zu übersetzen und dabei das Format beizubehalten.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Bei Claude API-Aufrufen werden die Platzhalter {source_lang} und {target_lang} im Prompt durch die Ausgangs- und Zielsprachvariablen über die f-string-Funktion des Python-Skripts ersetzt.
{: .prompt-info }

#### Konkretisierung der Anforderungen und Beispiele (Wie)
Bei einfachen Aufgaben können die vorherigen Schritte ausreichen, um die gewünschten Ergebnisse zu erzielen, aber bei komplexeren Aufgaben können zusätzliche Erklärungen erforderlich sein.

Wenn die Anforderungen komplex und vielfältig sind, verbessert eine strukturierte Auflistung die Lesbarkeit und erleichtert das Verständnis (sowohl für Menschen als auch für Sprachmodelle). Bei Bedarf ist es auch hilfreich, Beispiele bereitzustellen.
In diesem Fall habe ich die folgenden Bedingungen hinzugefügt:

##### Behandlung des YAML Front Matter
Am Anfang eines in Markdown verfassten Posts für einen Jekyll-Blog befindet sich ein YAML Front Matter mit Informationen zu 'title', 'description', 'categories' und 'tags'. Das YAML Front Matter dieses Beitrags sieht beispielsweise so aus:

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

Bei der Übersetzung eines Beitrags sollten der Titel (title) und die Beschreibung (description) in verschiedene Sprachen übersetzt werden, aber für die Konsistenz der Post-URLs ist es vorteilhaft, die Kategorien (categories) und Tags (tags) unverändert auf Englisch zu belassen. Daher habe ich die folgende Anweisung hinzugefügt, um sicherzustellen, dass nur 'title' und 'description' übersetzt werden:

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Ich habe die Phrase "under any circumstances, regardless of the language you are translating to" hinzugefügt, um zu betonen, dass **ohne Ausnahme** keine anderen Tags im YAML Front Matter geändert werden sollten.
{: .prompt-tip }

##### Umgang mit Texten in anderen Sprachen als der Ausgangssprache
Beim Verfassen von Texten auf Koreanisch werden bei der Einführung von Konzepten oder Fachbegriffen oft englische Ausdrücke in Klammern hinzugefügt, wie bei '*중성자 감쇠 (Neutron Attenuation)*'. Bei der Übersetzung solcher Ausdrücke gab es Inkonsistenzen, manchmal wurden die Klammern beibehalten, manchmal der englische Ausdruck weggelassen. Daher habe ich die folgenden detaillierten Richtlinien festgelegt:
- Für Fachbegriffe:
  - Bei Übersetzungen in nicht-romanische Sprachen wie Japanisch das Format 'Übersetzter Ausdruck(Englischer Ausdruck)' beibehalten.
  - Bei Übersetzungen in romanische Sprachen wie Spanisch, Portugiesisch oder Französisch sind sowohl 'Übersetzter Ausdruck' allein als auch 'Übersetzter Ausdruck(Englischer Ausdruck)' zulässig, wobei Claude die angemessenere Option selbst wählen kann.
- Für Eigennamen muss die Originalschreibweise in irgendeiner Form in der Übersetzung erhalten bleiben.

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

##### Behandlung von Links zu anderen Beiträgen
Einige Beiträge enthalten Links zu anderen Beiträgen. In der Testphase, als keine spezifischen Anweisungen dazu gegeben wurden, interpretierte das Modell oft den Pfadteil der URL als zu übersetzenden Text, was zu defekten internen Links führte. Dieses Problem wurde durch Hinzufügen der folgenden Anweisung gelöst:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Nur Übersetzungsergebnisse ausgeben
Schließlich habe ich angewiesen, dass die Antwort nur die Übersetzungsergebnisse ohne zusätzlichen Text enthalten soll:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Zusätzliche Prompt-Design-Techniken
Im Gegensatz zu Anfragen an Menschen gibt es bei Sprachmodellen einige zusätzliche Techniken, die speziell anwendbar sind.
Es gibt viele nützliche Ressourcen dazu im Internet, aber hier sind einige allgemein nützliche Tipps, die ich zusammengefasst habe.  
Ich habe hauptsächlich den [Prompt-Engineering-Leitfaden in der offiziellen Anthropic-Dokumentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) als Referenz verwendet.

#### Strukturierung mit XML-Tags
Diese Technik habe ich bereits durchgehend verwendet. Bei komplexen Prompts mit verschiedenen Kontexten, Anweisungen, Formaten und Beispielen kann die angemessene Verwendung von XML-Tags wie `<instructions>`, `<example>`, `<format>` dem Sprachmodell helfen, den Prompt genau zu interpretieren und qualitativ hochwertige, beabsichtigte Ausgaben zu liefern. Das GitHub-Repository [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) enthält eine gute Zusammenstellung nützlicher XML-Tags für das Prompt-Writing.

#### Chain-of-Thought (CoT) Technik
Für Aufgaben, die erhebliches Denken erfordern, wie mathematische Problemlösung oder komplexe Dokumentenerstellung, kann die Leistung des Sprachmodells deutlich verbessert werden, indem es dazu angeregt wird, das Problem in Schritten zu durchdenken. Diese Technik kann jedoch zu längeren Antwortzeiten führen und ist nicht für alle Aufgaben gleichermaßen nützlich.

#### Prompt-Chaining-Technik
Bei komplexen Aufgaben kann ein einzelner Prompt an seine Grenzen stoßen. In solchen Fällen kann es sinnvoll sein, den gesamten Arbeitsablauf von Anfang an in mehrere Schritte zu unterteilen, für jeden Schritt einen spezialisierten Prompt zu erstellen und die Antwort aus einem Schritt als Eingabe für den nächsten zu verwenden. Diese Technik wird als Prompt-Chaining bezeichnet.

#### Vorfüllen des Antwortanfangs
Beim Eingeben eines Prompts kann man den Anfang der erwarteten Antwort vorgeben und das Modell bitten, von dort aus weiterzuschreiben. Dies kann unnötige Einleitungen vermeiden oder das Modell zwingen, in einem bestimmten Format wie XML oder JSON zu antworten. [Bei der Claude API kann diese Technik angewendet werden, indem man bei einem API-Aufruf sowohl eine `User`-Nachricht als auch eine `Assistant`-Nachricht übermittelt.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Verhinderung von Faulheit (Halloween-Patch vom 31.10.2024)
Obwohl ich nach dem ersten Schreiben dieses Artikels ein- oder zweimal geringfügige Prompt-Verbesserungen und Präzisierungen der Anweisungen vorgenommen habe, lief das Automatisierungssystem vier Monate lang ohne größere Probleme.

Doch am 31.10.12024 gegen 18 Uhr koreanischer Zeit trat ein seltsames Phänomen auf: Bei der Übersetzung neuer Beiträge übersetzte das System nur den ersten "TL;DR"-Teil des Beitrags und brach dann willkürlich ab.

Die vermuteten Ursachen und Lösungen für dieses Problem habe ich in einem [separaten Beitrag](/posts/does-ai-hate-to-work-on-halloween) behandelt, auf den ich hier verweise.

### Der fertige Prompt
Das Ergebnis des oben beschriebenen Prompt-Design-Prozesses ist wie folgt:

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
