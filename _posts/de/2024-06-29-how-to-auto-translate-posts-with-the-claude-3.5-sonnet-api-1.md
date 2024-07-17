---
title: Wie man Posts mit der Claude 3.5 Sonnet API automatisch übersetzt (1)
description: >-
  Eine kurze Einführung in das kürzlich veröffentlichte Claude 3.5 Sonnet-Modell, den Prozess der Prompt-Gestaltung für die mehrsprachige Übersetzung von Blog-Beiträgen und die Präsentation des fertigen Prompts.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Einleitung
Kürzlich habe ich die Claude 3.5 Sonnet API von Anthropic für die mehrsprachige Übersetzung von Blog-Beiträgen eingeführt. In diesem Zusammenhang möchte ich die Gründe für die Wahl der Claude 3.5 Sonnet API, die Methode der Prompt-Gestaltung sowie die Implementierung der API-Integration und Automatisierung durch Python-Skripte erläutern. Da der Inhalt, den ich behandeln möchte, recht umfangreich ist, wird dies nicht ein einzelner Beitrag, sondern eine Serie sein, und dies ist der erste Beitrag der Serie.

## Über Claude 3.5 Sonnet
Die Claude 3-Serie-Modelle werden je nach Modellgröße in den Versionen Haiku, Sonnet und Opus angeboten.  
![Claude 3 Modell-Tier-Unterscheidung](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Bildquelle: [Offizielle Webseite der Anthropic Claude API](https://www.anthropic.com/api)

Am 21. Juni 2024 (koreanische Zeit) veröffentlichte Anthropic das neueste Sprachmodell [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Laut Anthropics Ankündigung übertrifft es die Inferenzleistung von Claude 3 Opus bei gleichen Kosten und Geschwindigkeit wie das bestehende Claude 3 Sonnet. Es wird allgemein als dem Konkurrenzmodell GPT-4 in den Bereichen Komposition, sprachliches Schlussfolgern, mehrsprachiges Verständnis und Übersetzung überlegen angesehen.  
![Claude 3.5 Sonnet Einführungsbild](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Claude 3.5 Sonnet Leistungs-Benchmark-Ergebnisse](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Bildquelle: [Anthropic Homepage](https://www.anthropic.com/news/claude-3-5-sonnet)

## Gründe für die Einführung von Claude 3.5 zur Beitragsübersetzung
Es gibt bereits kommerzielle Übersetzungs-APIs wie Google Translate oder DeepL, die keine Sprachmodelle wie Claude 3.5 oder GPT-4 benötigen. Der Grund, warum ich mich dennoch für die Verwendung eines LLM für Übersetzungszwecke entschieden habe, liegt darin, dass der Benutzer im Gegensatz zu anderen kommerziellen Übersetzungsdiensten durch Prompt-Design dem Modell zusätzliche Kontextinformationen oder Anforderungen wie den Schreibzweck oder die Hauptthemen des Textes bereitstellen kann, und das Modell kann entsprechend eine kontextbezogene Übersetzung liefern. Obwohl DeepL und Google Translate im Allgemeinen eine hervorragende Übersetzungsqualität bieten, neigen sie aufgrund ihrer Einschränkungen bei der Erfassung des Themas und des Gesamtkontexts des Textes dazu, relativ unnatürliche Übersetzungsergebnisse zu liefern, wenn sie gebeten werden, lange Texte zu fachlichen Themen anstelle von alltäglichen Gesprächen zu übersetzen. Insbesondere Claude wird, wie bereits erwähnt, im Vergleich zum Konkurrenzmodell GPT-4 als relativ überlegen in den Bereichen Komposition, sprachliches Schlussfolgern, mehrsprachiges Verständnis und Übersetzung angesehen, weshalb ich es für geeignet hielt, die technischen Artikel in diesem Blog in mehrere Sprachen zu übersetzen.

## Prompt-Design
### Grundprinzipien des Prompt-Designs
Um zufriedenstellende Ergebnisse von einem Sprachmodell zu erhalten, die dem Zweck entsprechen, muss ein angemessener Prompt bereitgestellt werden. Obwohl Prompt-Design zunächst überwältigend erscheinen mag, unterscheidet sich die Methode, "etwas gut anzufordern", nicht wesentlich, ob der Gegenüber ein Sprachmodell oder ein Mensch ist. Aus dieser Perspektive betrachtet, ist es nicht besonders schwierig. Es ist gut, die aktuelle Situation und die Anforderungen nach den sechs W-Fragen (Wer, Was, Wann, Wo, Wie, Warum) klar zu erklären und bei Bedarf einige konkrete Beispiele hinzuzufügen. Es gibt zahlreiche Tipps und Techniken für Prompt-Design, aber die meisten leiten sich von den oben genannten Grundprinzipien ab.

### Rollenzuweisung und Situationsbeschreibung (Wer, Warum)
Zuerst wurde Claude 3.5 die Rolle eines *"professionellen technischen Übersetzers"* zugewiesen und Kontextinformationen über den Benutzer als *"einen technischen Blogger, der hauptsächlich über Mathematik, Physik und Datenwissenschaft schreibt"* bereitgestellt.
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Übermittlung der allgemeinen Anforderungen (Was)
Als Nächstes wurde angefordert, den vom Benutzer bereitgestellten Text im Markdown-Format von {source_lang} nach {target_lang} zu übersetzen, während das Format beibehalten wird.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Bei der Ausführung der Claude API werden die Platzhalter {source_lang} und {target_lang} im Prompt durch die Variablen für die Ausgangs- und Zielsprache mithilfe der f-string-Funktion des Python-Skripts ersetzt.
{: .prompt-info }

### Konkretisierung der Anforderungen und Beispiele (Wie)
Bis zu diesem Schritt kann es ausreichen, um die gewünschten Ergebnisse zu erzielen, aber bei komplexeren Aufgaben können zusätzliche Erklärungen erforderlich sein. In diesem Fall wurden die folgenden Bedingungen hinzugefügt.

#### Umgang mit Quelltext, der andere Sprachen als die Ausgangssprache enthält
Beim Verfassen des Originaltextes auf Koreanisch kommt es häufig vor, dass bei der ersten Einführung eines Konzepts oder bei der Verwendung einiger Fachbegriffe der englische Ausdruck in Klammern angegeben wird, wie bei '*중성자 감쇠 (Neutron Attenuation)*'. Bei der Übersetzung solcher Ausdrücke gab es Probleme mit der Inkonsistenz der Übersetzungsmethode, manchmal wurden die Klammern beibehalten und manchmal der englische Text in den Klammern weggelassen. Um dies zu adressieren, wurde der folgende Satz zum Prompt hinzugefügt.
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Behandlung von Links zu anderen Beiträgen
Einige Beiträge enthalten Links zu anderen Beiträgen, und es trat häufig das Problem auf, dass interne Links unterbrochen wurden, weil der Pfadteil der URL als zu übersetzender Teil interpretiert und geändert wurde. Dieses Problem wurde durch Hinzufügen des folgenden Satzes zum Prompt gelöst.
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Ausgabe nur des Übersetzungsergebnisses als Antwort
Schließlich wird der folgende Satz präsentiert, um sicherzustellen, dass bei der Antwort nur das Übersetzungsergebnis ausgegeben wird, ohne zusätzliche Kommentare hinzuzufügen.
> The output should only contain the translated text.

### Fertiger Prompt
Das Ergebnis des Prompt-Designs nach den obigen Schritten lautet wie folgt:
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.