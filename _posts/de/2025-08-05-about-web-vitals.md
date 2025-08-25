---
title: Web-Leistungsindikatoren (Web Vitals)
description: Eine Zusammenfassung der Web-Leistungsindikatoren (Web Vitals) und der Mess- und Bewertungskriterien von Lighthouse. Erfahren Sie, was die einzelnen Leistungsindikatoren bedeuten.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Faktoren, die die Web-Performance bestimmen
Die Faktoren, die bei der Optimierung der Web-Performance berücksichtigt werden müssen, lassen sich grob in zwei Kategorien einteilen: Ladeleistung und Rendering-Leistung.

### HTML-Ladeleistung
- Die Zeit von der ersten Anfrage einer Webseite an den Server über das Netzwerk bis zum Empfang des HTML-Dokuments und dem Beginn des Renderings durch den Browser.
- Bestimmt, wie schnell die Seite zu sehen ist.
- Optimierung durch Minimierung von Weiterleitungen, Caching von HTML-Antworten, Komprimierung von Ressourcen und angemessene Nutzung von CDNs.

### Rendering-Leistung
- Die Zeit, die der Browser benötigt, um den für den Benutzer sichtbaren Bildschirm zu zeichnen und interaktiv zu machen.
- Bestimmt, wie flüssig und schnell der Bildschirm gezeichnet wird.
- Optimierung durch Entfernen von unnötigem CSS und JS, Vermeiden von verzögertem Laden von Schriftarten und Thumbnails, Auslagern rechenintensiver Operationen in separate Web Worker zur Minimierung der Hauptthread-Auslastung und Optimierung von Animationen.

## Web-Leistungsindikatoren (Web Vitals)
Dieser Artikel basiert auf den Informationen von Googles [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) und der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Sofern kein besonderer Grund vorliegt, ist es besser, eine allgemeine Verbesserung anzustreben, anstatt sich nur auf einen einzelnen Leistungsindikator zu konzentrieren. Es ist wichtig zu identifizieren, welche Teile der zu optimierenden Webseite als Leistungsengpass fungieren. Wenn Statistiken von echten Nutzern verfügbar sind, ist es außerdem ratsam, sich nicht auf die Spitzen- oder Durchschnittswerte zu konzentrieren, sondern auf die Werte im unteren Bereich (etwa das erste Quartil, Q1), um zu überprüfen und zu verbessern, ob auch in diesen Fällen die Zielkriterien erreicht werden.

### Core Web Vitals (Wichtige Web-Leistungsindikatoren)
Wie wir gleich sehen werden, gibt es verschiedene Web-Leistungsindikatoren (Web Vitals). Google betrachtet jedoch die folgenden drei Metriken als besonders wichtig, da sie eng mit der Benutzererfahrung zusammenhängen und in realen Umgebungen (nicht nur in simulierten) gemessen werden können. Diese werden als [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals) bezeichnet. Da Google die Core Web Vitals einer Website in das Ranking seiner Suchergebnisse einbezieht, müssen Website-Betreiber diese Indikatoren auch im Hinblick auf die Suchmaschinenoptimierung (SEO) sorgfältig beachten.
- [Largest Contentful Paint (LCP)](#lcp-largest-contentful-paint): Spiegelt die *Ladeleistung* wider, sollte unter 2,5 Sekunden liegen.
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): Spiegelt die *Reaktionsfähigkeit* wider, sollte unter 200 ms liegen.
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): Spiegelt die *visuelle Stabilität* wider, sollte unter 0,1 gehalten werden.

Die Core Web Vitals sind grundsätzlich für die Messung in realen Umgebungen gedacht, aber mit Ausnahme von INP können die beiden anderen auch in simulierten Umgebungen wie den Chrome-Entwicklertools oder Lighthouse gemessen werden. Da INP eine tatsächliche Benutzereingabe zur Messung erfordert, kann es nicht in einer simulierten Umgebung gemessen werden. In solchen Fällen kann jedoch [TBT](#tbt-total-blocking-time) als Referenz herangezogen werden, da es eine sehr hohe Korrelation mit INP aufweist und ein ähnlicher Leistungsindikator ist. [Normalerweise verbessert sich mit der Optimierung von TBT auch der INP-Wert](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Gewichtung der Leistungsbewertung in Lighthouse 10
[Die Leistungsbewertung von Lighthouse wird als gewichteter Durchschnitt der Punktzahlen der einzelnen Metriken berechnet, wobei die Gewichtungen in der folgenden Tabelle gelten](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Metrik | Gewichtung |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Misst die Zeit, die vom Anfordern der Seite bis zum Rendern des ersten DOM-Inhalts benötigt wird.
- Als DOM-Inhalt gelten Bilder, nicht-weiße `<canvas>`-Elemente, SVGs usw. auf der Seite. Inhalte innerhalb eines `iframe` werden nicht berücksichtigt.

> Einer der Faktoren, die den FCP besonders stark beeinflussen, ist die Ladezeit von Schriftarten. Die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) empfiehlt, für Optimierungen in diesem Bereich den [entsprechenden Beitrag](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) zu konsultieren.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) sind die Bewertungskriterien von Lighthouse wie folgt:

| Farbbewertung | Mobiler FCP (Sekunden) | Desktop-FCP (Sekunden) |
| --- | --- | --- |
| Grün (schnell) | 0-1,8 | 0-0,9 |
| Orange (moderat) | 1,8-3 | 0,9-1,6 |
| Rot (langsam) | Über 3 | Über 1,6 |

### LCP (Largest Contentful Paint)
- Misst die Zeit, die benötigt wird, um das größte Element (Bild, Textblock, Video usw.) innerhalb des sichtbaren Bereichs (Viewport) zu rendern, wenn eine Webseite zum ersten Mal geladen wird.
- Je größer der Bereich ist, den ein Element auf dem Bildschirm einnimmt, desto wahrscheinlicher ist es, dass der Benutzer es als Hauptinhalt wahrnimmt.
- Wenn das LCP-Element ein Bild ist, kann die benötigte Zeit in vier Teilintervalle unterteilt werden. Es ist wichtig zu identifizieren, in welchem dieser Abschnitte der Engpass auftritt:
  1. Time to First Byte (TTFB): Die Zeit vom Beginn des Seitenladevorgangs bis zum Empfang des ersten Bytes der HTML-Dokumentantwort.
  2. Ladeverzögerung (Load delay): Die Differenz zwischen dem Zeitpunkt, zu dem der Browser mit dem Laden der LCP-Ressource beginnt, und dem TTFB.
  3. Ladezeit (Load time): Die Zeit, die zum Laden der LCP-Ressource selbst benötigt wird.
  4. Rendering-Verzögerung (Render delay): Die Zeit vom Abschluss des Ladens der LCP-Ressource bis zur vollständigen Darstellung des LCP-Elements.

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}) sind die Bewertungskriterien von Lighthouse wie folgt:

| Farbbewertung | Mobiler LCP (Sekunden) | Desktop-LCP (Sekunden) |
| --- | --- | --- |
| Grün (schnell) | 0-2,5 | 0-1,2 |
| Orange (moderat) | 2,5-4 | 1,2-2,4 |
| Rot (langsam) | Über 4 | Über 2,4 |

### TBT (Total Blocking Time)
- Misst die Gesamtzeit, in der eine Webseite nicht auf Benutzereingaben wie Mausklicks, Bildschirmberührungen oder Tastatureingaben reagieren kann.
- Zwischen FCP und [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})* werden Aufgaben, die länger als 50 ms dauern, als [lange Aufgaben (long tasks)](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) betrachtet. Der Teil jeder langen Aufgabe, der 50 ms überschreitet, wird als *blockierender Anteil (blocking portion)* bezeichnet. TBT ist die Summe aller dieser blockierenden Anteile.

> \* TTI selbst reagiert übermäßig empfindlich auf Ausreißer bei Netzwerkantworten und langen Aufgaben, was zu geringer Konsistenz und hoher Variabilität führt. Daher wurde es [ab Lighthouse 10 aus den Leistungsbewertungsmetriken entfernt](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Die häufigste Ursache für lange Aufgaben ist das unnötige oder ineffiziente Laden, Parsen und Ausführen von JavaScript. Die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) und [Googles web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) empfehlen, die Größe der JavaScript-Payloads durch [Code-Splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) zu reduzieren, sodass jeder Teil in weniger als 50 ms ausgeführt werden kann. Bei Bedarf sollte die Ausführung in einen separaten Service Worker ausgelagert werden, um den Hauptthread zu entlasten und Multithreading zu nutzen.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) sind die Bewertungskriterien von Lighthouse wie folgt:

| Farbbewertung | Mobiler TBT (Millisekunden) | Desktop-TBT (Millisekunden) |
| --- | --- | --- |
| Grün (schnell) | 0-200 | 0-150 |
| Orange (moderat) | 200-600 | 150-350 |
| Rot (langsam) | Über 600 | Über 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Beispiel für eine plötzliche Layoutverschiebung" autoplay=true loop=true %}
> Videoquelle: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Man spürt die tiefe Wut in der Cursorbewegung~~

- Unerwartete Layoutverschiebungen beeinträchtigen die Benutzererfahrung auf verschiedene Weise, z. B. indem Text plötzlich verschoben wird und man die Leseposition verliert oder versehentlich auf den falschen Link oder Button klickt.
- Die genaue Methode zur Berechnung des CLS-Scores ist auf [Googles web.dev](https://web.dev/articles/cls) beschrieben.
- Wie in der folgenden Abbildung zu sehen ist, sollte ein Wert von 0,1 oder weniger angestrebt werden.

![Was ist ein guter CLS-Wert?](/assets/img/about-web-vitals/good-cls-values.svg)
> Bildquelle: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Misst, wie schnell Inhalte während des Ladevorgangs einer Seite visuell angezeigt werden.
- Lighthouse zeichnet den Ladevorgang der Seite im Browser als Video auf, analysiert dieses Video, um den Fortschritt zwischen den einzelnen Frames zu berechnen, und ermittelt dann den SI-Score mithilfe des [Speedline Node.js-Moduls](https://github.com/paulirish/speedline).

> Alle Maßnahmen zur Verbesserung der Seitenladegeschwindigkeit, einschließlich der bereits bei [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) und [TBT](#tbt-total-blocking-time) erwähnten, wirken sich positiv auf den SI-Score aus. Man kann ihn als einen Leistungsindikator betrachten, der nicht nur einen einzelnen Teil des Ladevorgangs repräsentiert, sondern den gesamten Prozess bis zu einem gewissen Grad widerspiegelt.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}) sind die Bewertungskriterien von Lighthouse wie folgt:

| Farbbewertung | Mobiler SI (Sekunden) | Desktop-SI (Sekunden) |
| --- | --- | --- |
| Grün (schnell) | 0-3,4 | 0-1,3 |
| Orange (moderat) | 3,4-5,8 | 1,3-2,3 |
| Rot (langsam) | Über 5,8 | Über 2,3 |
