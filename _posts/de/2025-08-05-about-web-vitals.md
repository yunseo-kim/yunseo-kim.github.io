---
title: Web-Leistungskennzahlen (Web Vitals)
description: Web Vitals und Lighthouse im Überblick: Definitionen, Messung, Bewertung (FCP, LCP, INP, TBT, CLS, SI) plus praktische Tipps zur Performance-Optimierung.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Faktoren, die die Web-Performance bestimmen
Bei der Optimierung der Web-Performance lassen sich die bestimmenden Faktoren grob in zwei Kategorien einteilen: Ladeleistung und Rendering-Leistung.

### HTML-Ladeleistung
- Zeitspanne vom erstmaligen Anfordern der Webseite über das Netzwerk bis zu dem Zeitpunkt, an dem der Browser mit dem Rendern beginnt
- Bestimmt, wie schnell die Seite sichtbar zu werden beginnt
- Optimierung durch Minimieren von Redirects, Caching der HTML-Antwort, Komprimierung von Ressourcen, geeignete Nutzung eines CDN etc.

### Rendering-Leistung
- Zeit, die der Browser benötigt, um die sichtbare Oberfläche zu zeichnen und Interaktionen zu ermöglichen
- Bestimmt, wie weich und schnell die Oberfläche aufgebaut wird
- Optimierung durch Entfernen unnötiger CSS- und JS-Ressourcen, Vermeiden verzögerten Ladens von Schriften und Thumbnails, Auslagern schwerer Berechnungen in separate Web Worker zur Minimierung der Hauptthread-Blockierung, Optimierung von Animationen etc.

## Web-Leistungskennzahlen (Web Vitals)
Die Darstellung folgt Googles [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) und der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Sofern kein besonderer Grund besteht, sollte man nicht nur eine einzelne Kennzahl isoliert optimieren, sondern die Gesamtverbesserung anstreben und identifizieren, wo auf der Zielseite echte Engpässe liegen. Liegen reale Nutzungsdaten vor, lohnt es sich zudem, den unteren Bereich (etwa Q1) statt nur Spitzen- oder Durchschnittswerte zu betrachten und sicherzustellen, dass auch dort die Zielwerte erreicht werden.

### Zentrale Web-Leistungskennzahlen (Core Web Vitals)
Es gibt verschiedene Web Vitals. Besonders wichtig sind jedoch drei Kennzahlen, die unmittelbar mit der Nutzererfahrung verknüpft sind und in realen Umgebungen (nicht nur im Labor) messbar sind. Google bezeichnet sie als [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Da Google diese Kennzahlen auch im Ranking seiner Suchmaschine berücksichtigt, sind sie für Seitenbetreiber aus SEO-Sicht besonders relevant.
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): spiegelt die Ladeleistung wider, sollte ≤ 2,5 s sein
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): spiegelt die Reaktionsfähigkeit wider, sollte ≤ 200 ms sein
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): spiegelt die visuelle Stabilität wider, sollte ≤ 0,1 bleiben

Core Web Vitals sind primär für Felddaten gedacht. Zwei davon (außer INP) lassen sich aber auch in Laborumgebungen wie den Chrome DevTools oder Lighthouse messen. INP erfordert echte Nutzereingaben und ist daher im Labor nicht messbar; in diesem Fall kann [TBT](#tbt-total-blocking-time) als stark korrelierte, ähnliche Kennzahl herangezogen werden, und [in der Regel verbessert sich INP mit, wenn man TBT verbessert](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Gewichtung der Performance-Punktzahl in Lighthouse 10
[Die Performance-Punktzahl von Lighthouse ist ein gewichteter Durchschnitt der Teilresultate; es gelten folgende Gewichte](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Messgröße | Gewicht |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Misst die Zeit bis zum Rendern der ersten DOM-Inhalte nach dem Seitenaufruf
- Als DOM-Inhalte gelten u. a. Bilder, nicht-weiße `<canvas>`-Elemente, SVG; Inhalte in `iframe`s werden nicht berücksichtigt

> Einer der besonders einflussreichen Faktoren für FCP ist die Schriftladedauer. Die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) empfiehlt Optimierungen nach dem [entsprechenden Beitrag](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbkategorie | Mobil-FCP (s) | Desktop-FCP (s) |
| --- | --- | --- |
| Grün (schnell) | 0–1,8 | 0–0,9 |
| Orange (mittel) | 1,8–3 | 0,9–1,6 |
| Rot (langsam) | über 3 | über 1,6 |

### LCP (Largest Contentful Paint)
- Misst die Zeit bis zum Rendern des größten Elements (Bild, Textblock, Video etc.) innerhalb des bei Seitenaufruf zunächst sichtbaren Anzeigebereichs (Viewport)
- Je größer die sichtbare Fläche eines Elements, desto eher wird es als Hauptinhalt wahrgenommen
- Ist der LCP ein Bild, lässt sich die Gesamtdauer in vier Teilabschnitte gliedern; wichtig ist, den Engpass zu identifizieren:
  1. Time to First Byte (TTFB): Zeit vom Start des Seitenladens bis zum Empfang des ersten Bytes der HTML-Antwort
  2. Ladeverzögerung (Load Delay): Differenz zwischen dem Zeitpunkt, zu dem der Browser mit dem Laden der LCP-Ressource beginnt, und dem TTFB
  3. Ladezeit (Load Time): Zeit zum Laden der LCP-Ressource selbst
  4. Render-Verzögerung (Render Delay): Zeit vom Ende des Ladens der LCP-Ressource bis zur vollständigen Darstellung des LCP-Elements

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbkategorie | Mobil-LCP (s) | Desktop-LCP (s) |
| --- | --- | --- |
| Grün (schnell) | 0–2,5 | 0–1,2 |
| Orange (mittel) | 2,5–4 | 1,2–2,4 |
| Rot (langsam) | über 4 | über 2,4 |

### TBT (Total Blocking Time)
- Misst die Gesamtzeit, in der die Seite nicht auf Nutzereingaben wie Mausklicks, Touches oder Tastatur reagiert
- Zwischen FCP und [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* werden Tasks mit Laufzeit ≥ 50 ms als [Long Tasks](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) gewertet; von der Laufzeit jeder Long Task wird die 50-ms-Schwelle abgezogen (Blocking-Anteil), und die Summe dieser Blocking-Anteile ist der TBT

> \* TTI ist sehr empfindlich gegenüber Ausreißern in Netzwerkantworten und Long Tasks, wodurch es inkonsistent und volatil ist; daher [entfiel TTI ab Lighthouse 10 als Bewertungsmetrik](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Häufigste Ursache für Long Tasks sind überflüssiges oder ineffizientes Laden, Parsen und Ausführen von JavaScript. Die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) und [Googles web.dev](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) empfehlen, per [Code-Splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) die JS-Payload so zu reduzieren, dass einzelne Aufgaben in ≤ 50 ms ausführbar sind, und bei Bedarf in einen separaten Worker (z. B. Web Worker) auszulagern, um den Hauptthread zu entlasten.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbkategorie | Mobil-TBT (ms) | Desktop-TBT (ms) |
| --- | --- | --- |
| Grün (schnell) | 0–200 | 0–150 |
| Orange (mittel) | 200–600 | 150–350 |
| Rot (langsam) | über 600 | über 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Beispiel für eine plötzliche Layout-Änderung" autoplay=true loop=true %}
> Videoquelle: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Man spürt tiefe Wut in der Cursor-Bewegung~~

- Unerwartete Layout-Verschiebungen beeinträchtigen die User Experience, z. B. durch wegspringenden Text oder Fehlklicks auf Links/Buttons
- Die genaue Berechnung des CLS-Scores ist auf [Googles web.dev](https://web.dev/articles/cls) beschrieben
- Wie in der folgenden Grafik zu sehen, sollte ein Wert ≤ 0,1 angestrebt werden

![Was ist ein guter CLS-Wert?](/assets/img/about-web-vitals/good-cls-values.svg)
> Bildquelle: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Misst, wie schnell während des Ladens der Seite Inhalte visuell erscheinen
- Lighthouse zeichnet den Ladevorgang als Video auf, analysiert die Frame-Fortschritte und berechnet daraus mittels des [Speedline-Node.js-Moduls](https://github.com/paulirish/speedline) den SI-Score

> Maßnahmen, die die Ladegeschwindigkeit verbessern — darunter die zuvor behandelten [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) und [TBT](#tbt-total-blocking-time) — wirken sich in der Regel auch positiv auf den SI aus. SI repräsentiert nicht nur einen einzelnen Schritt, sondern reflektiert den gesamten Ladeprozess in gewissem Maß.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
Laut der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbkategorie | Mobil-SI (s) | Desktop-SI (s) |
| --- | --- | --- |
| Grün (schnell) | 0–3,4 | 0–1,3 |
| Orange (mittel) | 3,4–5,8 | 1,3–2,3 |
| Rot (langsam) | über 5,8 | über 2,3 |
