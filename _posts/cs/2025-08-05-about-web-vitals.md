---
title: Webové metriky výkonnosti (Web Vitals)
description: "Shrnutí Web Vitals a kritérií měření/hodnocení v Lighthouse a vysvětlení, co jednotlivé metriky výkonu znamenají."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Faktory určující webový výkon
Při optimalizaci webového výkonu lze faktory, které výkon určují, ve velkém rozdělit na dvě kategorie: výkon načítání a výkon vykreslování.

### Výkon načítání HTML
- Čas od okamžiku, kdy je přes síť poprvé odeslán požadavek na webovou stránku na server, do okamžiku, kdy je stažen HTML dokument a prohlížeč začne renderovat
- Určuje, jak rychle se stránka začne zobrazovat
- Optimalizace pomocí: minimalizace přesměrování, cachování HTML odpovědí, komprese zdrojů, vhodné využití CDN apod.

### Výkon vykreslování
- Čas, který prohlížeč potřebuje k vykreslení obrazovky, kterou uživatel vidí, a k tomu, aby byla interaktivní
- Určuje, jak plynule a rychle se obraz vykresluje
- Optimalizace pomocí: odstranění zbytečného CSS a JS, prevence zpožděného načítání fontů a miniatur, přesunutí náročných výpočtů do samostatného Web Workeru pro minimalizaci blokování hlavního vlákna, optimalizace animací apod.

## Webové metriky výkonnosti (Web Vitals)
Text vychází z [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) od Googlu a z [dokumentace pro vývojáře Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Pokud k tomu není zvláštní důvod, je lepší neusilovat o zlepšení jen jedné metriky, ale mířit na celkové zlepšení a hlavně identifikovat, která část cílové stránky tvoří výkonnostní úzké hrdlo. Pokud navíc máte statistiky z reálných uživatelských dat, je vhodné se místo špičkových nebo průměrných hodnot zaměřit spíše na hodnoty zhruba na úrovni Q1 (spodní kvartil) a ověřit, že i v těchto případech splňujete cíle—pak teprve dále zlepšovat.

### Klíčové metriky webového výkonu (Core Web Vitals)
Jak bude zmíněno dále, metrik webového výkonu (Web Vitals) existuje více. Google však považuje za obzvlášť důležité následující tři metriky, které úzce souvisí s uživatelským zážitkem a lze je měřit v reálném prostředí (nikoli jen v laboratorních podmínkách). Říká jim [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Protože Google promítá Core Web Vitals cílového webu i do pořadí výsledků svého vyhledávače, měli by je provozovatelé webů pečlivě sledovat i z hlediska SEO.
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): odráží *výkon načítání*, musí být do 2,5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): odráží *odezvu*, musí být ≤ 200 ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): odráží *vizuální stabilitu*, je nutné držet ≤ 0,1

Core Web Vitals jsou primárně určeny pro měření v reálném prostředí, ale kromě INP lze zbylé dvě metriky měřit i v laboratorním prostředí, např. pomocí Chrome DevTools nebo Lighthouse. INP vyžaduje skutečné uživatelské vstupy, a proto jej v laboratorních podmínkách měřit nelze; v takových případech lze místo toho použít [TBT](#tbt-total-blocking-time), který s INP velmi silně koreluje a je mu podobný, a také platí, že [typicky zlepšení TBT vede i ke zlepšení INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Váhy metrik ve skóre výkonu Lighthouse 10
[Skóre výkonu Lighthouse se počítá jako vážený průměr skóre jednotlivých metrik a používá váhy z následující tabulky](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Metrika | Váha |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Měří čas od požadavku na stránku do vykreslení prvního obsahu DOM
- Za DOM obsah se považují obrázky na stránce, prvky `<canvas>` jiné než bílé, SVG apod.; obsah uvnitř `iframe` se nezohledňuje

> Jedním z faktorů, který má na FCP obzvlášť velký vliv, je doba načítání fontů; dokumentace pro vývojáře Chrome doporučuje pro optimalizaci v této oblasti nahlédnout do [souvisejícího článku](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Kritéria hodnocení v Lighthouse
Podle [dokumentace pro vývojáře Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) jsou hodnoticí kritéria Lighthouse následující:

| Barevná úroveň | Mobilní FCP (s) | Desktop FCP (s) |
| --- | --- | --- |
| Zelená (rychlé) | 0-1.8 | 0-0.9 |
| Oranžová (střední) | 1.8-3 | 0.9-1.6 |
| Červená (pomalé) | > 3 | > 1.6 |

### LCP (Largest Contentful Paint)
- Měří čas do vykreslení největšího prvku (obrázek, textový blok, video apod.) v rámci viditelné oblasti (viewport) při prvním otevření stránky
- Čím větší plochu prvek na obrazovce zabírá, tím spíše jej uživatel bude vnímat jako hlavní obsah
- Pokud je LCP obrázek, lze dobu rozdělit do čtyř podúseků; je důležité určit, kde vzniká úzké hrdlo
  1. Time to first byte (TTFB): čas od začátku načítání stránky do přijetí prvního bajtu odpovědi HTML dokumentu
  2. Zpoždění načtení (Load delay): rozdíl mezi okamžikem, kdy prohlížeč začne načítat LCP zdroj, a TTFB
  3. Doba načítání (Load time): čas potřebný k načtení samotného LCP zdroje
  4. Zpoždění vykreslení (Render delay): čas od dokončení načtení LCP zdroje do úplného vykreslení LCP prvku

#### Kritéria hodnocení v Lighthouse
Podle [dokumentace pro vývojáře Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}) jsou hodnoticí kritéria Lighthouse následující:

| Barevná úroveň | Mobilní LCP (s) | Desktop LCP (s) |
| --- | --- | --- |
| Zelená (rychlé) | 0-2.5 | 0-1.2 |
| Oranžová (střední) | 2.5-4 | 1.2-2.4 |
| Červená (pomalé) | > 4 | > 2.4 |

### TBT (Total Blocking Time)
- Měří celkový čas, po který webová stránka nedokáže reagovat na uživatelské vstupy, jako je kliknutí myší, dotyk na obrazovce nebo zadávání z klávesnice
- Z úloh mezi FCP a [TTI (okamžik, kdy se stránka stává interaktivní, Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* se za [dlouhé úlohy](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) považují ty, které běží ≥ 50 ms; u každé takové úlohy se část přesahující 50 ms nazývá *blocking portion* (blokující část) a součet všech blokujících částí je definován jako TBT

> \* Samotné TTI je příliš citlivé na odlehlé hodnoty síťových odpovědí i na dlouhé úlohy, má nízkou konzistenci a vysokou variabilitu; proto bylo [od Lighthouse 10 z hodnocených metrik odstraněno](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Nejběžnější příčinou dlouhých úloh bývá zbytečné nebo neefektivní načítání, parsování a spouštění JavaScriptu; [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) pomáhá zmenšit velikost JS payloadu tak, aby se jednotlivé části daly spustit do 50 ms, a v případě potřeby lze uvažovat i o oddělení do samostatného service workeru a běhu ve více vláknech mimo hlavní vlákno—takové kroky doporučují [dokumentace pro vývojáře Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) i [web.dev od Googlu](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Kritéria hodnocení v Lighthouse
Podle [dokumentace pro vývojáře Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) jsou hodnoticí kritéria Lighthouse následující:

| Barevná úroveň | Mobilní TBT (ms) | Desktop TBT (ms) |
| --- | --- | --- |
| Zelená (rychlé) | 0-200 | 0-150 |
| Oranžová (střední) | 200-600 | 150-350 |
| Červená (pomalé) | > 600 | > 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Příklad náhlé změny rozvržení" autoplay=true loop=true %}
> Zdroj videa: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Je cítit hluboký vztek z pohybu kurzoru~~

- Neočekávané změny rozvržení zhoršují UX různými způsoby: text se náhle posune a uživatel ztratí místo, kde četl, nebo omylem klikne na odkaz či tlačítko apod.
- Konkrétní způsob výpočtu skóre CLS je popsán na [web.dev od Googlu](https://web.dev/articles/cls)
- Jak je vidět na obrázku níže, cílem by měla být hodnota ≤ 0,1

![What is a good CLS score?](https://web.dev/static/articles/cls/image/good-cls-values.svg){: width="640" height="480" }
> Zdroj obrázku: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Měří, jak rychle se během načítání stránky obsah vizuálně zobrazuje
- Lighthouse nahrává proces načítání stránky v prohlížeči jako video, analyzuje jej, vypočítá průběh mezi snímky a následně pomocí [modulu Speedline pro Node.js](https://github.com/paulirish/speedline) vypočte skóre SI

> Jakákoli opatření vedoucí ke zrychlení načítání stránky—včetně těch, která byla zmíněna při shrnutí [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) a [TBT](#tbt-total-blocking-time)—se obvykle pozitivně projeví i ve skóre SI. Jde o metrikou výkonu, která spíše než jeden konkrétní krok reprezentuje celkový proces načítání do určité míry.
{: .prompt-tip }

#### Kritéria hodnocení v Lighthouse
Podle [dokumentace pro vývojáře Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}) jsou hodnoticí kritéria Lighthouse následující:

| Barevná úroveň | Mobilní SI (s) | Desktop SI (s) |
| --- | --- | --- |
| Zelená (rychlé) | 0-3.4 | 0-1.3 |
| Oranžová (střední) | 3.4-5.8 | 1.3-2.3 |
| Červená (pomalé) | > 5.8 | > 2.3 |
