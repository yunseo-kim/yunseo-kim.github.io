---
title: Wskaźniki wydajności WWW (Web Vitals)
description: "Porządkuję Web Vitals oraz kryteria pomiaru i oceny w Lighthouse, a także wyjaśniam, co oznacza każdy z kluczowych wskaźników wydajności."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Czynniki decydujące o wydajności WWW
Przy optymalizacji wydajności WWW czynniki, które ją determinują, można w dużym uproszczeniu podzielić na dwie kategorie: wydajność ładowania oraz wydajność renderowania.

### Wydajność ładowania HTML
- Czas od pierwszego żądania strony WWW do serwera przez sieć, przez pobranie dokumentu HTML, aż do momentu, w którym przeglądarka rozpocznie renderowanie
- Decyduje o tym, jak szybko strona zaczyna się wyświetlać
- Optymalizacja m.in. przez: minimalizację przekierowań, cache’owanie odpowiedzi HTML, kompresję zasobów, odpowiednie wykorzystanie CDN

### Wydajność renderowania
- Czas, jaki przeglądarka potrzebuje, aby narysować ekran widoczny dla użytkownika i umożliwić interakcję
- Decyduje o tym, jak płynnie i szybko renderowany jest widok
- Optymalizacja m.in. przez: usunięcie zbędnych CSS i JS, zapobieganie opóźnionemu ładowaniu fontów i miniaturek, przeniesienie ciężkich obliczeń do osobnego Web Worker w celu minimalizacji zajętości wątku głównego, optymalizację animacji

## Wskaźniki wydajności WWW (Web Vitals)
Opis opiera się na [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) Google oraz [dokumentacji Chrome dla deweloperów](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Jeśli nie ma ku temu szczególnego powodu, lepiej nie skupiać się wyłącznie na jednym wskaźniku, lecz dążyć do poprawy całościowej. Kluczowe jest też ustalenie, które elementy na optymalizowanej stronie stanowią wąskie gardło wydajności. Ponadto, jeśli dostępne są statystyki oparte na danych rzeczywistych użytkowników, zamiast koncentrować się na wartościach z czołówki lub średniej, warto patrzeć na wartości z dolnego kwartyla (około Q1) i sprawdzać, czy także w tym przypadku spełniane są założone cele — oraz odpowiednio wprowadzać usprawnienia.

### Kluczowe wskaźniki internetowe (Core Web Vitals)
Jak jeszcze za chwilę omówię, Web Vitals obejmują różne wskaźniki. Spośród nich Google uznaje za szczególnie istotne te trzy, które są mocno powiązane z doświadczeniem użytkownika i mogą być mierzone w środowisku rzeczywistym (a nie tylko laboratoryjnym). Nazywa je [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Ponieważ Google uwzględnia Core Web Vitals także w rankingu wyników wyszukiwania, z perspektywy właściciela serwisu warto uważnie śledzić te wskaźniki również pod kątem SEO.
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): odzwierciedla *wydajność ładowania*, powinno wynosić ≤ 2,5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): odzwierciedla *responsywność*, powinno wynosić ≤ 200 ms
- [Cummulative Layout Shift (CLS)](#cls-cumulative-layout-shift): odzwierciedla *stabilność wizualną*, należy utrzymywać ≤ 0,1

Core Web Vitals są zasadniczo przeznaczone do pomiaru w środowisku rzeczywistym, ale dwa z nich (z wyjątkiem INP) da się zmierzyć także w środowisku laboratoryjnym, np. w Chrome DevTools lub Lighthouse. INP wymaga rzeczywistych interakcji użytkownika, więc w labie nie da się go zmierzyć; w takich przypadkach można posiłkować się wskaźnikiem [TBT](#tbt-total-blocking-time), który jest z INP silnie skorelowany i podobny interpretacyjnie. Zazwyczaj [poprawa TBT poprawia też INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Wagi punktacji wydajności w Lighthouse 10
[Wynik wydajności w Lighthouse jest liczony jako średnia ważona punktów poszczególnych metryk, zgodnie z wagami z poniższej tabeli](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Metryka | Waga |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Mierzy czas od żądania strony do wyrenderowania pierwszej treści DOM
- Za treść DOM uznaje m.in. obrazy na stronie, elementy `<canvas>` (inne niż białe), SVG itd.; nie uwzględnia treści wewnątrz `iframe`

> Jednym z czynników szczególnie istotnie wpływających na FCP jest czas ładowania fontów; w kwestii optymalizacji Chrome zaleca zapoznanie się z [powiązanym wpisem](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) w [dokumentacji Chrome dla deweloperów](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Kryteria oceny Lighthouse
Zgodnie z [dokumentacją Chrome dla deweloperów](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), kryteria oceny w Lighthouse są następujące.

| Kolor oceny | FCP na mobile (s) | FCP na desktopie (s) |
| --- | --- | --- |
| Zielony (szybko) | 0-1.8 | 0-0.9 |
| Pomarańczowy (średnio) | 1.8-3 | 0.9-1.6 |
| Czerwony (wolno) | > 3 | > 1.6 |

### LCP (Largest Contentful Paint)
- Przy pierwszym otwarciu strony, licząc względem widocznego obszaru ekranu (viewport), mierzy czas do wyrenderowania największego elementu w tym obszarze (obraz, blok tekstu, wideo itd.)
- Im większa powierzchnia zajmowana na ekranie, tym większe prawdopodobieństwo, że użytkownik będzie to postrzegał jako główną treść
- Jeśli LCP dotyczy obrazu, czas ten można podzielić na 4 podetapy; ważne jest zidentyfikowanie, w którym miejscu powstaje wąskie gardło
  1. Time to first byte (TTFB): czas od rozpoczęcia ładowania strony do otrzymania pierwszego bajtu odpowiedzi dokumentu HTML
  2. Opóźnienie ładowania (Load delay): różnica między momentem, gdy przeglądarka zaczyna ładować zasób LCP, a TTFB
  3. Czas ładowania (Load time): czas potrzebny na załadowanie samego zasobu LCP
  4. Opóźnienie renderowania (Render delay): czas od zakończenia ładowania zasobu LCP do pełnego wyrenderowania elementu LCP

#### Kryteria oceny Lighthouse
Zgodnie z [dokumentacją Chrome dla deweloperów](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), kryteria oceny w Lighthouse są następujące.

| Kolor oceny | LCP na mobile (s) | LCP na desktopie (s) |
| --- | --- | --- |
| Zielony (szybko) | 0-2.5 | 0-1.2 |
| Pomarańczowy (średnio) | 2.5-4 | 1.2-2.4 |
| Czerwony (wolno) | > 4 | > 2.4 |

### TBT (Total Blocking Time)
- Mierzy łączny czas, w którym strona nie jest w stanie reagować na wejście użytkownika (np. kliknięcie myszą, dotyk ekranu, wpisywanie z klawiatury)
- Spośród zadań pomiędzy FCP a [TTI (moment rozpoczęcia interakcji, Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\* za *długie zadania* uznaje się te, które wykonywały się ≥ 50 ms. Dla każdego takiego zadania część czasu przekraczająca 50 ms jest nazywana *częścią blokującą (blocking portion)*, a suma wszystkich części blokujących jest definiowana jako TBT

> \* Samo TTI jest nadmiernie wrażliwe na wartości odstające odpowiedzi sieciowych oraz na długie zadania, przez co ma niską spójność i wysoką zmienność; dlatego [od Lighthouse 10 zostało wyłączone z kryteriów oceny wydajności](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Najczęstszą przyczyną długich zadań są zwykle zbędne lub nieefektywne ładowanie, parsowanie i wykonywanie JavaScript. [Dokumentacja Chrome dla deweloperów](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) oraz [web.dev Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) zalecają zastosowanie [podziału kodu (code splitting)](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) w celu zmniejszenia rozmiaru payloadu JS tak, aby każdy fragment dało się wykonać w czasie ≤ 50 ms; a jeśli to potrzebne — rozważyć przeniesienie pracy poza wątek główny, np. do osobnego service worker, aby wykonywać ją wielowątkowo.
{: .prompt-tip }

#### Kryteria oceny Lighthouse
Zgodnie z [dokumentacją Chrome dla deweloperów](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), kryteria oceny w Lighthouse są następujące.

| Kolor oceny | TBT na mobile (ms) | TBT na desktopie (ms) |
| --- | --- | --- |
| Zielony (szybko) | 0-200 | 0-150 |
| Pomarańczowy (średnio) | 200-600 | 150-350 |
| Czerwony (wolno) | > 600 | > 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Przykład nagłej zmiany układu (layoutu)" autoplay=true loop=true %}
> Źródło wideo: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~W ruchu kursora czuć głęboką wściekłość~~

- Nieoczekiwane zmiany układu psują UX na wiele sposobów: tekst nagle „ucieka”, przez co tracisz miejsce czytania, albo przypadkowo klikasz link czy przycisk
- Szczegółowy sposób wyliczania CLS jest opisany na [web.dev Google](https://web.dev/articles/cls)
- Jak widać na poniższym obrazie, celem powinno być ≤ 0,1

![What is a good CLS score?](https://web.dev/static/articles/cls/image/good-cls-values.svg){: width="640" height="480" }
> Źródło obrazu: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Mierzy, jak szybko treść jest wizualnie wyświetlana podczas ładowania strony
- Lighthouse nagrywa wideo z procesu ładowania strony w przeglądarce, analizuje je i oblicza postęp między klatkami, a następnie wyznacza wynik SI z użyciem [modułu Speedline dla Node.js](https://github.com/paulirish/speedline)

> Wszystko, co poprawia szybkość ładowania strony — w tym działania omawiane wcześniej przy [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) i [TBT](#tbt-total-blocking-time) — wpływa pozytywnie także na SI. To wskaźnik, który nie tyle reprezentuje jeden etap ładowania, ile w pewnym stopniu odzwierciedla cały proces.
{: .prompt-tip }

#### Kryteria oceny Lighthouse
Zgodnie z [dokumentacją Chrome dla deweloperów](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), kryteria oceny w Lighthouse są następujące.

| Kolor oceny | SI na mobile (s) | SI na desktopie (s) |
| --- | --- | --- |
| Zielony (szybko) | 0-3.4 | 0-1.3 |
| Pomarańczowy (średnio) | 3.4-5.8 | 1.3-2.3 |
| Czerwony (wolno) | > 5.8 | > 2.3 |
