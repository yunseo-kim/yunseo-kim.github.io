---
title: Wie man Posts mit der Claude 3.5 Sonnet API automatisch übersetzt (1) - Prompt-Design
description: Dieser Beitrag behandelt das Design von Prompts für die mehrsprachige Übersetzung von Markdown-Textdateien sowie den Prozess der Automatisierung der Arbeit mit Python unter Verwendung eines von Anthropic erhaltenen API-Schlüssels und des erstellten Prompts. Dies ist der erste Beitrag der Serie und stellt die Methoden und den Prozess des Prompt-Designs vor.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Einleitung
Kürzlich habe ich die Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blog-Beiträgen eingeführt. In dieser Serie werde ich die Gründe für die Wahl der Claude 3.5 Sonnet API, die Methoden des Prompt-Designs sowie die Implementierung der API-Integration und Automatisierung mittels Python-Skripten erläutern.  
Die Serie besteht aus zwei Beiträgen, und dieser Artikel, den Sie gerade lesen, ist der erste Teil der Serie.
- Teil 1: Vorstellung des Claude 3.5 Sonnet-Modells und Gründe für seine Auswahl, Prompt-Engineering (dieser Beitrag)
- Teil 2: [Erstellung und Anwendung eines Python-Automatisierungsskripts unter Verwendung der API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Über Claude 3.5 Sonnet
Die Claude 3-Serie bietet je nach Modellgröße die Versionen Haiku, Sonnet und Opus.  
![Claude 3 Modell-Tier-Unterscheidung](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Bildquelle: [Offizielle Webseite der Anthropic Claude API](https://www.anthropic.com/api)

Am 21. Juni 12024 nach koreanischer Zeit (im [Holozän-Kalender](https://de.wikipedia.org/wiki/Holoz%C3%A4n-Kalender)) veröffentlichte Anthropic das neueste Sprachmodell [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Laut Anthropics Ankündigung übertrifft es die Inferenzleistung von Claude 3 Opus bei gleichen Kosten und Geschwindigkeit wie Claude 3 Sonnet. Es wird allgemein als dem Konkurrenzmodell GPT-4 in Bereichen wie Textkomposition, sprachliches Schlussfolgern, mehrsprachiges Verständnis und Übersetzung überlegen angesehen.  
![Claude 3.5 Sonnet Einführungsbild](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet Leistungs-Benchmark-Ergebnisse](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Bildquelle: [Anthropic Homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

(Ergänzung vom 31.10.12024) Am 22. Oktober 12024 kündigte Anthropic eine aktualisierte Version der Claude 3.5 Sonnet API ("claude-3-5-sonnet-20241022") und Claude 3.5 Haiku an. Aufgrund des [später erwähnten Problems](#verhinderung-von-faulheit-halloween-patch-vom-31102024) wird in diesem Blog jedoch noch die bestehende "claude-3-5-sonnet-20240620" API verwendet.

## Gründe für die Einführung von Claude 3.5 zur Beitragsübersetzung
Es gibt bereits kommerzielle Übersetzungs-APIs wie Google Translate oder DeepL, die nicht unbedingt Sprachmodelle wie Claude 3.5 oder GPT-4 erfordern. Der Grund, warum ich mich dennoch für die Verwendung eines LLM zu Übersetzungszwecken entschieden habe, liegt darin, dass der Benutzer im Gegensatz zu anderen kommerziellen Übersetzungsdiensten durch Prompt-Design dem Modell zusätzliche Kontextinformationen oder Anforderungen wie den Schreibzweck oder die Hauptthemen des Textes bereitstellen kann. Das Modell kann dann eine kontextbezogene Übersetzung liefern, die diesen Informationen entspricht. Obwohl DeepL und Google Translate im Allgemeinen eine hervorragende Übersetzungsqualität bieten, neigen sie aufgrund ihrer Grenzen beim Verständnis des Themas oder des Gesamtkontexts eines Textes dazu, bei der Übersetzung längerer Texte zu fachspezifischen Themen, die über alltägliche Konversation hinausgehen, relativ unnatürliche Ergebnisse zu liefern. Insbesondere Claude wird im Vergleich zum Konkurrenzmodell GPT-4 in den Bereichen Textkomposition, sprachliches Schlussfolgern, mehrsprachiges Verständnis und Übersetzung als überlegen angesehen. Bei einem einfachen Test zeigte es auch eine flüssigere Übersetzungsqualität als GPT-4o. Daher hielt ich es für geeignet, die technischen Beiträge in diesem Blog in verschiedene Sprachen zu übersetzen.

## Prompt-Design
### Grundprinzipien beim Stellen von Anfragen
Um zufriedenstellende Ergebnisse von einem Sprachmodell zu erhalten, die dem Zweck entsprechen, muss ein angemessener Prompt bereitgestellt werden. Prompt-Design mag zunächst überwältigend erscheinen, aber tatsächlich unterscheidet sich die "Methode, etwas gut anzufragen" nicht wesentlich, ob der Empfänger ein Sprachmodell oder ein Mensch ist. Aus dieser Perspektive betrachtet, ist es nicht besonders schwierig. Es ist hilfreich, die aktuelle Situation und die Anforderungen nach den sechs W-Fragen (Wer, Was, Wann, Wo, Wie, Warum) klar zu erklären und bei Bedarf einige konkrete Beispiele hinzuzufügen. Es gibt zahlreiche Tipps und Techniken für das Prompt-Design, aber die meisten leiten sich von den im Folgenden beschriebenen Grundprinzipien ab.

#### Allgemeiner Ton
Es wird häufig berichtet, dass Sprachmodelle qualitativ hochwertigere Antworten liefern, wenn Prompts in einem höflich anfragenden Ton formuliert werden, anstatt in einem befehlenden Ton. Auch in der Gesellschaft ist es wahrscheinlicher, dass jemand eine Aufgabe gewissenhafter ausführt, wenn man ihn mit dem ersteren statt dem letzteren Tonfall bittet. Es scheint, dass Sprachmodelle dieses menschliche Antwortmuster gelernt haben und nachahmen.

#### Rollenzuweisung und Situationsbeschreibung (Wer, Warum)
Zuerst wurde Claude 3.5 die Rolle eines *"professionellen technischen Übersetzers (professional technical translator)"* zugewiesen und Kontextinformationen über den Benutzer als *"Ingenieur-Blogger, der hauptsächlich über Mathematik, Physik und Datenwissenschaft schreibt"* bereitgestellt.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Übermittlung der allgemeinen Anforderungen (Was)
Als Nächstes wurde darum gebeten, den vom Benutzer bereitgestellten Text im Markdown-Format von {source_lang} nach {target_lang} zu übersetzen, während das Format beibehalten wird.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Bei der Ausführung der Claude API werden die Platzhalter {source_lang} und {target_lang} im Prompt durch die Variablen für die Ausgangs- und Zielsprache mithilfe der f-string-Funktion des Python-Skripts ersetzt.
{: .prompt-info }

#### Konkretisierung der Anforderungen und Beispiele (Wie)
Bei einfachen Aufgaben können die vorherigen Schritte ausreichen, um die gewünschten Ergebnisse zu erzielen. Bei komplexeren Aufgaben können jedoch zusätzliche Erklärungen erforderlich sein.

Wenn die Anforderungen komplex und vielfältig sind, ist es besser, sie in einer Liste zusammenzufassen, anstatt jede einzeln auszuführen. Dies verbessert die Lesbarkeit und macht es für den Leser (sei es Mensch oder Sprachmodell) leichter zu verstehen. Bei Bedarf kann es auch hilfreich sein, Beispiele bereitzustellen.
In diesem Fall wurden die folgenden Bedingungen hinzugefügt:

##### Behandlung des YAML Front Matter
Das YAML Front Matter am Anfang eines in Markdown verfassten Beitrags für einen Jekyll-Blog enthält Informationen zu 'title', 'description', 'categories' und 'tags'. Das YAML Front Matter dieses Beitrags sieht beispielsweise wie folgt aus:

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

Bei der Übersetzung eines Beitrags müssen die Tags für Titel (title) und Beschreibung (description) in mehrere Sprachen übersetzt werden. Für die Konsistenz der Beitrags-URLs ist es jedoch vorteilhaft für die Wartung, die Namen der Kategorien (categories) und Tags (tags) unverändert auf Englisch zu belassen. Daher wurde die folgende Anweisung hinzugefügt, um sicherzustellen, dass nur 'title' und 'description' übersetzt werden:

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Der Zusatz "under any circumstances, regardless of the language you are translating to" betont, dass die anderen Tags im YAML Front Matter **ohne Ausnahme** nicht verändert werden sollen.
{: .prompt-tip }

##### Umgang mit Teilen des Originaltexts, die nicht in der Ausgangssprache verfasst sind
Beim Verfassen des Originaltexts auf Koreanisch ist es üblich, bei der ersten Einführung eines Konzepts oder bei der Verwendung bestimmter Fachbegriffe den englischen Ausdruck in Klammern hinzuzufügen, wie bei *'중성자 감쇠 (Neutron Attenuation)'*. Bei der Übersetzung solcher Ausdrücke gab es Inkonsistenzen, manchmal wurden die Klammern beibehalten, manchmal der englische Ausdruck in Klammern weggelassen. Um dieses Problem zu lösen, wurden die folgenden detaillierten Anweisungen festgelegt:
- Für Fachbegriffe:
  - Bei der Übersetzung in Sprachen, die nicht auf dem römischen Alphabet basieren, wie Japanisch, soll das Format 'übersetzte Ausdrucksweise(englische Ausdrucksweise)' beibehalten werden.
  - Bei der Übersetzung in Sprachen, die auf dem römischen Alphabet basieren, wie Spanisch, Portugiesisch oder Französisch, sind sowohl die alleinige Angabe der 'übersetzten Ausdrucksweise' als auch die kombinierte Angabe 'übersetzte Ausdrucksweise(englische Ausdrucksweise)' zulässig. Claude soll selbstständig entscheiden, welche der beiden Optionen angemessener ist.
- Für Eigennamen muss die ursprüngliche Schreibweise in irgendeiner Form im Übersetzungsergebnis erhalten bleiben.

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
Einige Beiträge enthalten Links zu anderen Beiträgen. In der Testphase, als keine spezifischen Anweisungen dazu gegeben wurden, interpretierte das Modell oft, dass auch der Pfadteil der URL übersetzt werden sollte, was zu gebrochenen internen Links führte. Dieses Problem wurde durch Hinzufügen des folgenden Satzes zum Prompt gelöst:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Ausgabe nur des Übersetzungsergebnisses als Antwort
Schließlich wird der folgende Satz hinzugefügt, um sicherzustellen, dass bei der Antwort nur das Übersetzungsergebnis ausgegeben wird, ohne zusätzliche Kommentare:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Zusätzliche Prompt-Design-Techniken
Im Gegensatz zu Anfragen an Menschen gibt es bei Sprachmodellen einige zusätzliche Techniken, die speziell angewendet werden können.
Es gibt viele nützliche Ressourcen zu diesem Thema im Internet, aber hier sind einige der repräsentativsten Tipps, die allgemein nützlich sein können:  
Der [offizielle Leitfaden zum Prompt-Engineering von Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) wurde hauptsächlich als Referenz verwendet.

#### Strukturierung mit XML-Tags
Tatsächlich wurde dies bereits in den vorherigen Abschnitten verwendet. Bei komplexen Prompts, die verschiedene Kontexte, Anweisungen, Formate und Beispiele enthalten, kann die angemessene Verwendung von XML-Tags wie `<instructions>`, `<example>`, `<format>` usw. dem Sprachmodell helfen, den Prompt genau zu interpretieren und qualitativ hochwertige, beabsichtigte Ausgaben zu produzieren. Das [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) GitHub-Repository enthält eine gute Zusammenstellung nützlicher XML-Tags für das Verfassen von Prompts, die als Referenz empfohlen wird.

#### Chain-of-Thought (CoT) Technik
Bei Aufgaben, die ein erhebliches Maß an Schlussfolgerung erfordern, wie das Lösen mathematischer Probleme oder das Verfassen komplexer Dokumente, kann die Leistung des Sprachmodells deutlich verbessert werden, indem es dazu angeregt wird, das Problem schrittweise zu durchdenken. Allerdings kann dies zu längeren Antwortzeiten führen, und diese Technik ist nicht für alle Aufgaben gleichermaßen nützlich, was zu beachten ist.

#### Prompt-Chaining-Technik
Bei der Durchführung komplexer Aufgaben kann ein einzelner Prompt möglicherweise an seine Grenzen stoßen. In solchen Fällen kann es sinnvoll sein, den gesamten Arbeitsablauf von Anfang an in mehrere Schritte zu unterteilen, für jeden Schritt einen spezifischen Prompt zu erstellen und die Antwort aus dem vorherigen Schritt als Eingabe für den nächsten Schritt zu verwenden. Diese Technik wird als Prompt-Chaining bezeichnet.

#### Vorfüllen des Anfangs der Antwort
Beim Eingeben des Prompts kann man den Anfang des zu antwortenden Inhalts vorgeben und das Modell auffordern, die Antwort daran anzuschließen. Dies kann dazu dienen, unnötige Einleitungen wie Begrüßungen zu überspringen oder eine Antwort in einem bestimmten Format wie XML oder JSON zu erzwingen. [Bei der Claude API kann diese Technik angewendet werden, indem man bei der Ausführung nicht nur die `User`-Nachricht, sondern auch eine `Assistant`-Nachricht mitsendet.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Verhinderung von Faulheit (Halloween-Patch vom 31.10.2024)
Obwohl seit dem ersten Verfassen dieses Artikels ein- oder zweimal geringfügige Verbesserungen des Prompts und Konkretisierungen der Anweisungen vorgenommen wurden, gab es in den vier Monaten der Anwendung dieses Automatisierungssystems keine größeren Probleme.

Allerdings trat ab etwa 18 Uhr koreanischer Zeit am 31.10.12024 bei der Übersetzung neu erstellter Beiträge kontinuierlich die Anomalie auf, dass nur der erste 'TL;DR'-Teil des Beitrags übersetzt und die Übersetzung dann willkürlich abgebrochen wurde.

Die vermuteten Ursachen für dieses Problem und mögliche Lösungsansätze werden in einem [separaten Beitrag](/posts/does-ai-hate-to-work-on-halloween) behandelt, auf den hier verwiesen wird.

### Der fertige Prompt
Das Ergebnis des oben beschriebenen Prompt-Design-Prozesses sieht wie folgt aus:

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
