---
title: Web-Performance-Kennzahlen (Web Vitals)
description: "Überblick über Web Vitals und die Lighthouse-Mess- und Bewertungskriterien: Bedeutung der einzelnen Leistungskennzahlen, wie sie gemessen werden und wie man sie optimiert."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Faktoren, die die Web-Performance bestimmen
Bei der Optimierung der Web-Performance lassen sich die entscheidenden Faktoren grob in zwei Kategorien einteilen: *Ladeleistung* und *Renderingleistung*.

### HTML-Ladeleistung
- Zeitspanne vom ersten Seitenaufruf über das Netzwerk bis zu dem Moment, in dem der Browser mit dem Rendern beginnt
- Bestimmt, wie schnell die Seite sichtbar zu werden beginnt
- Optimierung durch Minimierung von Redirects, Caching der HTML-Antwort, Komprimierung von Ressourcen, passenden CDN-Einsatz u. a.

### Renderingleistung
- Zeit, die der Browser benötigt, um das sichtbare UI zu zeichnen und interaktiv zu machen
- Bestimmt, wie flüssig und schnell der Bildschirm aufgebaut wird
- Optimierung durch Entfernen unnötigen CSS und JS, Vermeiden verzögerten Ladens von Schriftarten und Thumbnails, Auslagern rechenintensiver Aufgaben in einen separaten Web Worker zur Entlastung des Main Threads, Optimierung von Animationen u. a.

## Web-Performance-Kennzahlen (Web Vitals)
Die Beschreibung folgt den Leitlinien von [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) und der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Ohne besonderen Grund sollte man sich nicht auf eine einzige Metrik fixieren, sondern eine ganzheitliche Verbesserung anstreben und identifizieren, wo die Engpässe der zu optimierenden Seite liegen. Liegen reale Nutzungsdaten vor, empfiehlt es sich zudem, weniger auf Durchschnitts- oder Spitzenwerte zu schauen, sondern eher auf das untere Quartil (Q1), um sicherzustellen, dass auch in diesen Fällen die Zielwerte erreicht werden.

### Zentrale Web-Performance-Kennzahlen (Core Web Vitals)
Es gibt mehrere Web-Performance-Kennzahlen (Web Vitals). Unter ihnen betrachtet Google die folgenden drei, die besonders eng mit der User Experience verknüpft sind und in realen Umgebungen (nicht nur im Labor) messbar sind, als besonders wichtig – die [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Da Google diese Kennzahlen auch in die Reihenfolge der Suchergebnisse seiner Suchmaschine einfließen lässt, sollten Website-Betreiber sie auch im Hinblick auf Suchmaschinenoptimierung (SEO) sorgfältig beobachten.
- [Largest Contentful Paint (LCP)](#lcp-largest-contentful-paint): spiegelt die *Ladeleistung* wider, Zielwert ≤ 2,5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): spiegelt die *Reaktionsfähigkeit* wider, Zielwert ≤ 200 ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): spiegelt die *visuelle Stabilität* wider, Zielwert ≤ 0,1

Core Web Vitals sind grundsätzlich für Messungen in realen Umgebungen konzipiert. Zwei davon (außer INP) lassen sich aber auch in Laborumgebungen wie den Chrome DevTools oder Lighthouse messen. INP erfordert reale Nutzereingaben und kann deshalb nicht im Labor gemessen werden; in solchen Fällen kann [TBT](#tbt-total-blocking-time) als nahe korrelierende, ähnliche Metrik herangezogen werden – [in der Regel verbessert sich INP, wenn man TBT verbessert](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Gewichtung der Leistungsbewertung in Lighthouse 10
[Die Lighthouse-Leistungsbewertung ist ein gewogener Durchschnitt der Teilmetriken; die folgenden Gewichte werden verwendet](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Messwert | Gewichtung |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Misst die Zeit bis zur ersten Darstellung eines DOM-Inhalts nach dem Seitenaufruf
- Als DOM-Inhalt gelten Bilder, nicht-weiße `<canvas>`-Elemente, SVG usw.; Inhalte in `iframe`s werden nicht berücksichtigt

> Einer der Faktoren mit besonders großem Einfluss auf FCP ist die Schriftladezeit. Für entsprechende Optimierungen empfiehlt die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) den [zugehörigen Beitrag](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) als Einstieg.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
[Laut der Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbstufe | FCP mobil (s) | FCP Desktop (s) |
| --- | --- | --- |
| Grün (schnell) | 0–1,8 | 0–0,9 |
| Orange (mittel) | 1,8–3 | 0,9–1,6 |
| Rot (langsam) | > 3 | > 1,6 |

### LCP (Largest Contentful Paint)
- Misst die Zeit bis zur Darstellung des größten Elements (Bild, Textblock, Video usw.) innerhalb des anfänglich sichtbaren Bereichs (Viewport), wenn eine Seite erstmals geöffnet wird
- Je größer die sichtbare Fläche eines Elements ist, desto eher wird es vom Nutzer als Hauptinhalt wahrgenommen
- Ist der LCP ein Bild, lässt sich die Dauer in vier Teilabschnitte gliedern. Wichtig ist zu ermitteln, wo der Engpass liegt:
  1. Time to First Byte (TTFB): Zeit vom Ladebeginn der Seite bis zum Eintreffen des ersten Bytes der HTML-Antwort
  2. Ladeverzögerung (Load Delay): Differenz zwischen dem Start der LCP-Ressourcenanforderung durch den Browser und dem TTFB
  3. Ladezeit (Load Time): Zeit zum Laden der LCP-Ressource selbst
  4. Renderverzögerung (Render Delay): Zeit vom Abschluss des Ladens der LCP-Ressource bis zur vollständigen Darstellung des LCP-Elements

#### Lighthouse-Bewertungskriterien
[Laut der Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbstufe | LCP mobil (s) | LCP Desktop (s) |
| --- | --- | --- |
| Grün (schnell) | 0–2,5 | 0–1,2 |
| Orange (mittel) | 2,5–4 | 1,2–2,4 |
| Rot (langsam) | > 4 | > 2,4 |

### TBT (Total Blocking Time)
- Misst die gesamte Zeit, in der eine Seite nicht auf Nutzereingaben wie Mausklicks, Touches oder Tastatureingaben reagieren kann
- Zwischen FCP und [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* werden alle Tasks, die ≥ 50 ms dauern, als [Long Tasks](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) betrachtet. Von der Dauer jeder langen Aufgabe wird der Anteil oberhalb von 50 ms als *Blockierungsanteil (blocking portion)* bezeichnet; die Summe aller Blockierungsanteile ist der TBT.

> \* TTI reagiert übermäßig empfindlich auf Ausreißer bei Netzwerkantworten und auf lange Aufgaben, ist daher inkonsistent und stark variabel; entsprechend [wurde TTI seit Lighthouse 10 aus der Leistungsbewertung entfernt](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Häufigste Ursache langer Aufgaben sind unnötiges oder ineffizientes Laden, Parsen und Ausführen von JavaScript. Die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) und [web.dev von Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) empfehlen, durch [Code-Splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) die JS-Payload so zu reduzieren, dass einzelne Blöcke in ≤ 50 ms ausführbar sind, und bei Bedarf Arbeit vom Main Thread in einen separaten Service Worker auszulagern, um sie multithreaded auszuführen.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
[Laut der Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbstufe | TBT mobil (ms) | TBT Desktop (ms) |
| --- | --- | --- |
| Grün (schnell) | 0–200 | 0–150 |
| Orange (mittel) | 200–600 | 150–350 |
| Rot (langsam) | > 600 | > 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Beispiel für eine plötzliche Layoutänderung" autoplay=true loop=true %}
> Videoquelle: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~In der Bewegung des Cursors spürt man tiefe Wut.~~

- Unerwartete Layoutverschiebungen verschlechtern die User Experience auf vielfältige Weise: Text springt und man verliert die Leseposition, Links/Buttons werden versehentlich geklickt usw.
- Die genaue Berechnung des CLS-Scores ist auf [web.dev](https://web.dev/articles/cls) beschrieben.
- Wie in der folgenden Grafik ersichtlich, sollte der Zielwert ≤ 0,1 sein.

![Was ist ein guter CLS-Wert?](/assets/img/about-web-vitals/good-cls-values.svg)
> Bildquelle: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Misst, wie schnell während des Ladens einer Seite Inhalte sichtbar werden
- Lighthouse zeichnet den Ladevorgang als Video auf, analysiert die Fortschritte zwischen den Frames und berechnet daraus mithilfe des [Speedline-Node.js-Moduls](https://github.com/paulirish/speedline) den SI-Score

> Maßnahmen zur Beschleunigung des Seitenladens – einschließlich dessen, was wir bei [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) und [TBT](#tbt-total-blocking-time) besprochen haben – wirken sich in der Regel auch positiv auf den SI aus. Der SI ist weniger Repräsentant eines einzelnen Teilschritts als vielmehr eine Metrik, die den gesamten Ladeprozess in gewissem Maß abbildet.
{: .prompt-tip }

#### Lighthouse-Bewertungskriterien
[Laut der Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}) gelten folgende Schwellen:

| Farbstufe | SI mobil (s) | SI Desktop (s) |
| --- | --- | --- |
| Grün (schnell) | 0–3,4 | 0–1,3 |
| Orange (mittel) | 3,4–5,8 | 1,3–2,3 |
| Rot (langsam) | > 5,8 | > 2,3 |
