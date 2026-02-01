---
title: "Jak automatycznie tłumaczyć posty za pomocą Claude Sonnet 4 API (1) — projektowanie promptu"
description: "Projektuję prompt do wielojęzycznego tłumaczenia plików Markdown i pokazuję, jak zautomatyzować proces w Pythonie, wykorzystując klucze API Anthropic/Gemini oraz przygotowany prompt. Pierwszy wpis serii: metody i proces projektowania promptu."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1/
---

## Wprowadzenie
Odkąd w czerwcu 12024 roku wdrożyłem API Claude 3.5 Sonnet od Anthropic do wielojęzycznego tłumaczenia postów na blogu, przeszedłem przez kilka iteracji usprawnień promptów i skryptów automatyzacji oraz aktualizacje wersji modeli — i od blisko roku z satysfakcją używam tego systemu tłumaczeń. W tej serii chcę omówić: dlaczego w procesie wdrożenia wybrałem model Claude Sonnet, czemu później dodatkowo wdrożyłem Gemini 2.5 Pro, jak projektować prompt oraz jak zrealizować integrację z API i automatyzację przy użyciu skryptu Pythona.  
Seria składa się z dwóch wpisów, a czytany właśnie tekst jest jej pierwszą częścią.
- Część 1: Omówienie modeli Claude Sonnet/Gemini 2.5 i powody wyboru, inżynieria promptów (ten wpis)
- Część 2: [Napisanie i zastosowanie skryptu automatyzacji w Pythonie z użyciem API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## O Claude Sonnet
Modele z serii Claude są dostępne w wersjach Haiku, Sonnet oraz Opus — w zależności od rozmiaru modelu.  
![Podział tierów modeli Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> Źródło obrazu: [oficjalna strona Anthropic Claude API](https://www.anthropic.com/api)

> (Dodano 12025.05.29.)  
> To zrzut sprzed roku, więc stawki za token widnieją dla starszej wersji Claude 3, jednak podział na Haiku/Sonnet/Opus według rozmiaru modelu nadal jest aktualny. Na koniec maja 12025 roku cennik modeli udostępnianych przez Anthropic wygląda następująco:
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
> Źródło: [Anthropic developer docs](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

Następnie, 21 czerwca 12024 roku (czasu koreańskiego), Anthropic ogłosiło model językowy [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Przy tych samych kosztach i prędkości co dotychczasowy Claude 3 Sonnet, oferuje on możliwości rozumowania przewyższające Claude 3 Opus; powszechna jest też opinia, że w obszarach takich jak pisanie, rozumowanie językowe, rozumienie wielojęzyczne i tłumaczenie ma przewagę nad konkurencyjnym GPT-4.  
![Grafika przedstawiająca Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Wyniki benchmarków Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> Źródło obrazów: [Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## Dlaczego wdrożyłem Claude 3.5 do tłumaczenia postów
Nawet bez modeli językowych takich jak Claude 3.5 czy GPT-4 istnieją komercyjne API tłumaczeń, np. Google Translate lub DeepL. Mimo to zdecydowałem się użyć LLM do tłumaczeń, ponieważ — w odróżnieniu od innych usług — użytkownik może poprzez projektowanie promptu przekazać modelowi dodatkowy kontekst i wymagania wykraczające poza samą treść: cel tekstu, główne tematy itd. Model potrafi wtedy dostarczyć tłumaczenie uwzględniające kontekst.

DeepL i Google Translate zazwyczaj oferują bardzo dobrą jakość, ale mają ograniczenia: nie zawsze dobrze chwytają temat i ogólny kontekst długiego tekstu, a także nie pozwalają łatwo przekazać złożonych wymagań. Z tego powodu, gdy poprosi się je o tłumaczenie długiego, specjalistycznego tekstu (a nie codziennej rozmowy), rezultat bywa względnie nienaturalny; ponadto trudno wymusić, by wynik był dokładnie w wymaganym formacie (Markdown, YAML front matter itd.).

Zwłaszcza że Claude — jak wspomniałem — był często oceniany jako lepszy od GPT-4 w pisaniu, rozumowaniu językowym oraz rozumieniu i tłumaczeniach wielojęzycznych; w krótkich testach również dawał mi gładsze tłumaczenia niż GPT-4. Dlatego w czerwcu 12024 roku, gdy rozważałem wdrożenie, uznałem go za odpowiedni do tłumaczenia na wiele języków inżynierskich tekstów publikowanych na tym blogu.

## Historia aktualizacji
### 12024.07.01.
Jak podsumowałem w [osobnym wpisie](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/), ukończyłem wstępne prace: zastosowałem wtyczkę [Polyglot], dostosowałem `_config.yml`{: .filepath}, nagłówek HTML oraz sitemap.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Następnie, po wybraniu modelu Claude 3.5 Sonnet do tłumaczeń oraz po wstępnej implementacji i weryfikacji skryptu Pythona do integracji z API (opisywanego w tej serii), wdrożyłem go na blogu.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
22 października 12024 roku Anthropic ogłosiło zaktualizowaną wersję API Claude 3.5 Sonnet (`"claude-3-5-sonnet-20241022"`) oraz Claude 3.5 Haiku. Jednak ze względu na [omówiony dalej problem](#zapobieganie-lenistwu-latka-halloweenowa-120241031) na blogu nadal stosuję starsze API `"claude-3-5-sonnet-20240620"`.

### 12025.04.02.
[Zmieniono używany model z `"claude-3-5-sonnet-20240620"` na `"claude-3-7-sonnet-20250219"`.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[Zmieniono używany model z `"claude-3-7-sonnet-20250219"` na `"claude-sonnet-4-20250514"`.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Wyniki benchmarków wydajności Claude 4](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> Źródło obrazu: [Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

Warunki użycia mogą powodować różnice, ale zasadniczo od czasu pojawienia się Claude 3.7 Sonnet panuje dość powszechna zgoda, że w programowaniu Claude jest najsilniejszym modelem. Anthropic również aktywnie podkreśla przewagę swoich modeli w kodowaniu względem konkurencji (OpenAI, Google itd.). Przy ogłoszeniu Claude Opus 4 i Claude Sonnet 4 także zaakcentowano wydajność w kodowaniu i kontynuowano strategię celowania w deweloperów jako kluczową grupę klientów.

Oczywiście, z opublikowanych benchmarków wynika, że poprawy objęły również obszary inne niż kodowanie; w przypadku tłumaczeń omawianych w tym wpisie szczególnie istotny może być wzrost jakości w wielojęzycznym QA (MMMLU) oraz w rozwiązywaniu zadań matematycznych (AIME 2025). W krótkich testach potwierdziłem, że w porównaniu z Claude 3.7 Sonnet wyniki tłumaczeń Claude Sonnet 4 są lepsze pod względem naturalności sformułowań, profesjonalnego tonu oraz spójności terminologii.

> Na ten moment uważam, że przynajmniej do tłumaczenia technicznych tekstów pisanych po koreańsku — takich jak na tym blogu — modele Claude nadal są najlepsze. Jednocześnie w ostatnim czasie wyniki modeli Gemini od Google wyraźnie się poprawiają; w maju tego roku, choć nadal w fazie Preview, udostępniono też Gemini 2.5.  
> Porównując Gemini 2.0 Flash z Claude 3.7 Sonnet i Claude Sonnet 4, uznałem, że Claude tłumaczy lepiej, ale Gemini również ma bardzo mocne możliwości wielojęzyczne. Co więcej, mimo fazy Preview, Gemini 2.5 Preview 05-06 w matematyce, rozwiązywaniu zadań z fizyki i w umiejętności opisu wypada wręcz lepiej niż Claude Opus 4 — więc trudno z góry przesądzić, jak wypadnie porównanie po pełnym wydaniu.  
> Skoro do pewnego limitu można korzystać z [darmowego poziomu (Free Tier)](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits), a także biorąc pod uwagę, że nawet w płatnym poziomie (Paid Tier) Gemini ma tańsze stawki API niż Claude, przewaga cenowa Gemini jest ogromna. Dlatego nawet przy zbliżonej jakości Gemini może być rozsądną alternatywą. Ponieważ Gemini 2.5 wciąż jest w Preview, uznałem, że jest za wcześnie na wdrożenie w automatyzacji; gdy ukaże się wersja stabilna, planuję testy.
{: .prompt-tip }

### 12025.07.04.
- [Dodano funkcję tłumaczenia przyrostowego](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/978032f52c7d85ecb6b213233d5404d844402965)
- Rozdzielenie używanego modelu zależnie od języka docelowego ([Commit 3890c82](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3890c820c1f3df34f8e4686b8903ca4ee770ba15), [Commit fe0fc63](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/fe0fc63ae4e2764f3dfe24ff259b4477f120b9ed))
  - przy tłumaczeniu na angielski, tajwański chiński i niemiecki: użycie `"gemini-2.5-pro"`
  - przy tłumaczeniu na japoński, hiszpański, portugalski i francuski: nadal użycie dotychczasowego `"claude-sonnet-4-20250514"`
- Rozważano podniesienie wartości `temperature` z `0.0` do `0.2`, ale ostatecznie przywrócono ustawienie pierwotne

4 lipca 12025 roku modele Gemini 2.5 Pro oraz Gemini 2.5 Flash wreszcie wyszły z fazy Preview i zostały oficjalnie wydane. Choć liczba testowych przykładów była ograniczona, moje prywatne testy sugerowały, że nawet Gemini 2.5 Flash potrafi czasem wypadać naturalniej w tłumaczeniu na angielski niż dotychczasowy Claude Sonnet 4. Biorąc pod uwagę, że koszt na token wyjściowy w płatnym poziomie jest dla Gemini 2.5 Pro i Flash odpowiednio 1,5× oraz 6× niższy niż dla Claude Sonnet 4, to w lipcu 12025 — przynajmniej dla angielskiego — jest to w praktyce najbardziej konkurencyjny model cenowo-jakościowo. Jednak w przypadku Gemini 2.5 Flash, być może z uwagi na ograniczenia mniejszego modelu, choć wynik ogólnie bywa bardzo dobry, czasem pojawiały się problemy takie jak psucie formatu dokumentu Markdown czy wewnętrznych linków, co czyni go nieodpowiednim do złożonych zadań tłumaczenia i przetwarzania dokumentów. Ponadto, choć dla angielskiego Gemini 2.5 Pro wyraźnie dominuje, to w przypadku **większości postów po portugalsku (pt-BR)** oraz części postów po hiszpańsku model sprawiał wrażenie, jakby „męczył się” z zadaniem — prawdopodobnie z powodu mniejszej ilości danych treningowych. Analiza błędów pokazała, że w większości wynikały one z mylenia podobnych znaków, np. `í` i `i`, `ó` i `o`, `ç` i `c`, `ã` i `a`. Dla francuskiego nie obserwowałem tego typu błędów, ale zdarzało się, że zdania były zbyt rozwlekłe, przez co czytelność była gorsza niż w Claude Sonnet 4.

Nie znam dobrze języków innych niż angielski, więc trudno o szczegółowe i precyzyjne porównanie, ale z grubsza jakościowo wyglądało to tak:
- angielski, niemiecki, tajwański chiński: lepsze Gemini
- japoński, francuski, hiszpański, portugalski: lepsze Claude

Dodałem też do skryptu tłumaczeń funkcję tłumaczenia przyrostowego (Incremental Translation). Staram się starannie weryfikować tekst podczas pisania, ale mimo to zdarza mi się po publikacji zauważyć literówki lub drobne błędy, albo wpaść na pomysł, co jeszcze dopisać/poprawić. W takich sytuacjach zmieniony fragment jest niewielki, ale dotychczasowy skrypt musiał tłumaczyć i wypisywać cały tekst od początku do końca, co było nieefektywne kosztowo pod kątem użycia API. Dlatego zintegrowałem go z gitem: wykonuję porównanie wersji koreańskiego oryginału, wyciągam zmienione fragmenty w formacie diff, a następnie podaję je w prompcie wraz z pełnym poprzednim tłumaczeniem. Model zwraca diff-patch dla tłumaczenia, dzięki czemu można selektywnie zastosować tylko potrzebne poprawki. Ponieważ koszt tokenów wejściowych jest dużo niższy niż wyjściowych, można oczekiwać istotnych oszczędności; w konsekwencji, nawet przy drobnych zmianach w poście, będę mógł bez obaw uruchamiać automatyczny skrypt tłumaczeń zamiast ręcznie edytować każdą wersję językową.

Z kolei `temperature` to parametr określający, jaką losowość dodać w procesie generowania odpowiedzi: przy wyborze kolejnego słowa (tokena) model w pewnym stopniu „losuje” w oparciu o rozkład prawdopodobieństwa. Jest to nieujemna liczba rzeczywista (\*jak wspomnę dalej, zwykle w zakresie $[0,1]$ lub $[0,2]$): im bliżej 0, tym odpowiedzi są bardziej deterministyczne i spójne; im wyżej, tym bardziej zróżnicowane i kreatywne.  
Celem tłumaczenia jest możliwie dokładne i konsekwentne przekazanie znaczenia i tonu oryginału w innym języku, a nie kreatywne tworzenie nowych treści, więc aby zapewnić poprawność, spójność i przewidywalność, należy używać niskiej wartości `temperature`. Jednak ustawienie `temperature` na `0.0` powoduje, że model zawsze wybiera najbardziej prawdopodobne tokeny, co w niektórych przypadkach może prowadzić do zbyt dosłownego tłumaczenia lub do nienaturalnych, sztywnych zdań. Rozważałem więc lekkie podniesienie `temperature` do `0.2`, aby uniknąć nadmiernej „sztywności” i dodać odrobinę elastyczności — ale okazało się, że drastycznie spada dokładność obsługi złożonych linków zawierających fragmenty (fragment identifier), więc zrezygnowałem z tego.

> \* W praktyce najczęściej używany zakres `temperature` to 0–1; w Anthropic API dopuszczalny zakres również wynosi $[0,1]$. OpenAI API oraz Gemini API pozwalają na szerszy zakres $[0,2]$, ale rozszerzenie zakresu do $[0,2]$ nie oznacza, że skala „podwaja się” — znaczenie $T=1$ jest takie samo jak w modelach używających zakresu $[0,1]$. 
>
> Wewnętrznie, podczas generowania wyjścia, model działa jak pewna funkcja, która na podstawie promptu i dotychczas wygenerowanych tokenów zwraca rozkład prawdopodobieństwa kolejnego tokena; wynik losowania z tego rozkładu staje się następnym tokenem w odpowiedzi. Wartość bazowa odpowiadająca użyciu rozkładu „bez zmian” to $T=1$. Gdy $T<1$, rozkład staje się węższy i bardziej „ostry”, przez co model wybiera bardziej konsekwentnie głównie najbardziej prawdopodobne słowa; natomiast gdy $T>1$, rozkład się spłaszcza i sztucznie rośnie prawdopodobieństwo słów mało prawdopodobnych, które normalnie byłyby prawie nigdy nie wybierane.
>
> W obszarze $T>1$ jakość i przewidywalność odpowiedzi mogą się pogarszać (np. pojawiają się tokeny niepasujące do kontekstu, zdania niegramatyczne lub nielogiczne). W większości zadań — szczególnie w środowisku produkcyjnym — zaleca się trzymanie `temperature` w zakresie $[0,1]$. Wartości powyżej 1 można eksperymentalnie stosować do burzy mózgów czy wsparcia twórczego (np. szkic scenariusza), ale rośnie wtedy ryzyko halucynacji i błędów gramatycznych/logicznych, więc lepiej zakładać udział człowieka i weryfikację, a nie pełną automatyzację.
>
> Więcej szczegółów o `temperature` w modelach językowych można znaleźć w poniższych materiałach:
> - [Tamanna, *Understanding LLM Temperature* (2025).](https://medium.com/@tam.tamanna18/understanding-llm-temperature-7d838277a7d9)
> - [Tickr Data, *The Impact of Temperature on LLM Performance* (2023).](https://www.tickr.com/blog/posts/impact-of-temperature-on-llms/)
> - [Anik Das, *Temperature in Prompt Engineering* (2025).](https://peerlist.io/anikdas/articles/temperature-in-prompt-engineering)
> - [Peeperkorn et al., *Is Temperature the Creativity Parameter of LLMs?*, arXiv:2405.00492 (2024).](https://arxiv.org/abs/2405.00492)
> - [Colt Steele, *Understanding OpenAI’s Temperature Parameter* (2023).](https://www.coltsteele.com/tips/understanding-openai-s-temperature-parameter)
> - [Damon Garn, *Understanding the role of temperature settings in AI output*, TechTarget (2025).](https://www.techtarget.com/searchenterpriseai/tip/Understanding-the-role-of-temperature-settings-in-AI-output)
{: .prompt-info }

## Projektowanie promptu
### Podstawowe zasady, gdy o coś prosisz
Aby uzyskać od modelu językowego satysfakcjonujący wynik zgodny z celem, trzeba dostarczyć odpowiedni prompt. „Projektowanie promptu” może brzmieć onieśmielająco, ale w gruncie rzeczy „jak dobrze poprosić o coś” nie różni się aż tak bardzo — niezależnie od tego, czy prosisz model językowy, czy człowieka. Jeśli podejdziesz do tego z tej perspektywy, nie jest to szczególnie trudne. Warto jasno opisać sytuację i wymagania zgodnie z zasadą 5W1H (kto, co, kiedy, gdzie, dlaczego, jak), a jeśli trzeba — dodać kilka konkretnych przykładów. Istnieje mnóstwo porad i technik dotyczących promptów, ale większość z nich wynika z tych podstawowych zasad.

#### Ogólny ton
Często raportuje się, że gdy prompt jest napisany w uprzejmym, proszącym tonie, a nie w rozkazującym i wyniosłym, model językowy generuje odpowiedzi wyższej jakości. W społeczeństwie też zwykle jest tak, że gdy prosisz kogoś uprzejmie zamiast wydawać polecenia, rośnie szansa, że druga strona wykona zadanie staranniej — wygląda na to, że modele językowe uczą się i naśladują podobne wzorce.

#### Nadanie roli i opis sytuacji (kto, dlaczego)
Najpierw nadałem rolę *„profesjonalnego tłumacza technicznego (professional technical translator)”* oraz podałem kontekst o użytkowniku jako *„inżynierskim blogerze, który publikuje głównie o matematyce, fizyce i data science”*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Przekazanie wymagań w dużym zarysie (co)
Następnie poprosiłem, aby tekst dostarczony w formacie markdown został przetłumaczony z {source_lang} na {target_lang} z zachowaniem formatu.

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Podczas wywołania Claude API, w miejsce {source_lang} i {target_lang} w prompcie, poprzez mechanizm f-string w Pythonie, wstawiane są odpowiednio zmienne języka źródłowego i docelowego tłumaczenia.
{: .prompt-info }

#### Doprecyzowanie wymagań i przykłady (jak)
Przy prostych zadaniach czasem wystarczą wcześniejsze kroki, aby uzyskać pożądany wynik, ale przy złożonych wymaganiach może być potrzebne dodatkowe objaśnienie.

Gdy warunków jest dużo i są złożone, zamiast opisywać je rozwlekle, lepiej przekazać je w formie listy (w stylu „najpierw wniosek, potem szczegóły”) — zwiększa to czytelność i ułatwia zrozumienie (zarówno człowiekowi, jak i modelowi). Pomaga też dołączenie przykładów.
W tym przypadku dodałem następujące warunki.

##### Obsługa YAML front matter
Aby wrzucić post na bloga w Jekyllu, na początku pliku markdown znajduje się YAML front matter, gdzie zapisuje się informacje takie jak `title`, `description`, `categories` oraz `tags`. Dla przykładu YAML front matter tego wpisu wygląda tak:

```yaml
---
title: "Claude Sonnet 4 API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인"
description: "마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic/Gemini API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

Przy tłumaczeniu posta tagi `title` i `description` trzeba przetłumaczyć na dany język, ale aby zachować spójność URL-i, wygodniej jest nie tłumaczyć nazw kategorii (`categories`) i tagów (`tags`) i pozostawić je po angielsku — ułatwia to utrzymanie. Dlatego dodałem instrukcję, aby nie tłumaczyć tagów innych niż `title` i `description`. Ponieważ model najpewniej już „wie”, czym jest YAML front matter, zazwyczaj takie wyjaśnienie jest wystarczające.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> Dodałem frazę „under any circumstances, regardless of the language you are translating to”, aby podkreślić, że **bez wyjątków** nie wolno samowolnie modyfikować innych tagów w YAML front matter.
{: .prompt-tip }

(Aktualizacja 12025.04.02.)  
Dodatkowo poleciłem, by treść tagu `description` miała odpowiednią długość z uwzględnieniem SEO:

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Gdy oryginał zawiera języki inne niż język źródłowy
Pisząc po koreańsku, gdy po raz pierwszy wprowadzam definicję pojęcia albo używam pewnych terminów specjalistycznych, często zapisuję również angielską nazwę w nawiasie, np. *„중성자 감쇠 (Neutron Attenuation)”*. Przy tłumaczeniu takie elementy bywały obsługiwane niespójnie — czasem nawias zostawał, czasem angielski zapis w nawiasie był pomijany. Ustaliłem więc poniższe reguły:
- w przypadku terminów technicznych:
  - przy tłumaczeniu na języki nienależące do rodziny alfabetu łacińskiego (np. japoński) zachowujemy format `tłumaczenie(angielski)`;
  - przy tłumaczeniu na języki oparte na alfabecie łacińskim (np. hiszpański, portugalski, francuski) dopuszczamy zarówno zapis samego tłumaczenia, jak i zapis `tłumaczenie(angielski)` — model może wybrać lepszy wariant;
- w przypadku nazw własnych: oryginalna pisownia z nawiasu musi w jakiejś formie pozostać w tłumaczeniu.

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

##### Obsługa linków prowadzących do innych postów
Niektóre posty zawierają linki do innych postów. Na etapie testów, gdy nie podałem osobnych wytycznych, model często interpretował, że należy tłumaczyć także część ścieżki URL — przez co wewnętrzne linki się psuły. Ten problem rozwiązałem, dodając do promptu następujące zdanie.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(Aktualizacja 12025.04.06.)  
Po dodaniu tej instrukcji modele zaczęły poprawnie obsługiwać część ścieżki URL, więc liczba zepsutych linków wyraźnie spadła. Jednak w przypadku linków zawierających fragmenty (fragment identifier) pozostaje ograniczenie: bez znajomości treści docelowego wpisu model nadal musi „zgadywać” fragment. W związku z tym nie da się tego całkowicie rozwiązać wyłącznie instrukcją. Dlatego ulepszyłem skrypt Pythona i prompt: dołączam w prompcie kontekst innych postów, do których prowadzą linki z fragmentami, umieszczając pełną treść tych postów w tagu XML `<reference_context>` w prompcie użytkownika. Po wdrożeniu tej aktualizacji udało się w większości zapobiec problemom z linkami; w przypadku mocno powiązanych wpisów serii można też oczekiwać bardziej spójnych tłumaczeń na przestrzeni wielu postów.

W systemowym prompcie podaję następującą instrukcję:
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

A część `<reference_context>` w prompcie użytkownika ma następujący format i zawartość — jest dołączana na końcu, po treści tłumaczonego wpisu.
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

> Szczegóły implementacji znajdziesz w [części 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) tej serii oraz w pliku [Python script](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) w repozytorium GitHub.
{: .prompt-tip }

##### Wypisywanie w odpowiedzi wyłącznie przetłumaczonego tekstu
Na koniec dodałem polecenie, by w odpowiedzi nie dopisywać żadnych komentarzy, tylko zwrócić wyłącznie wynik tłumaczenia.

```xml
<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or "```markdown" or something of that nature!!</important>
```

### Dodatkowe techniki projektowania promptów
W odróżnieniu od proszenia człowieka, w przypadku modeli językowych istnieją też techniki specyficzne dla LLM.

W sieci jest wiele przydatnych materiałów na ten temat, ale jeśli zebrać kilka reprezentatywnych porad, które sprawdzają się dość uniwersalnie, to wygląda to następująco.  
Głównie opierałem się na [przewodniku prompt engineering w oficjalnej dokumentacji Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Strukturyzacja z użyciem tagów XML
W praktyce robiłem to już wcześniej. Gdy prompt jest złożony i zawiera wiele kontekstów, instrukcji, formatów i przykładów, zastosowanie tagów XML takich jak `<instructions>`, `<example>`, `<format>` pomaga modelowi poprawnie zinterpretować prompt i wygenerować wysokiej jakości wynik zgodny z intencją. W repozytorium GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) jest dobrze zebrana lista użytecznych tagów XML do promptów — polecam zajrzeć.

#### Rozumowanie etapami (CoT, Chain-of-Thought)
W zadaniach wymagających istotnego poziomu rozumowania (np. rozwiązywanie zadań matematycznych lub pisanie złożonych dokumentów) można znacząco poprawić wyniki, skłaniając model do myślenia etapami. Trzeba jednak uważać: może to zwiększać opóźnienie odpowiedzi, a poza tym nie jest to technika, która zawsze pomaga w każdym typie zadania.

#### Prompt chaining
Przy bardzo złożonych zadaniach pojedynczy prompt może nie wystarczyć. Wtedy warto rozważyć podzielenie całego przepływu pracy na etapy, przygotowanie promptu dopasowanego do każdego etapu oraz przekazywanie odpowiedzi z etapu poprzedniego jako wejścia do kolejnego. Takie podejście nazywa się prompt chaining.

#### Wypełnianie z góry początku odpowiedzi
Podczas podawania promptu można z góry wpisać początek odpowiedzi, a następnie poprosić model o jej kontynuację. Pozwala to pominąć zbędne wstępy typu „Dzień dobry” lub wymusić konkretny format wyjścia (np. XML, JSON). [W przypadku Anthropic API można użyć tej techniki, wysyłając przy wywołaniu nie tylko wiadomość `User`, ale również wiadomość `Assistant`.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Zapobieganie „lenistwu” (łatka halloweenowa 12024.10.31.) {#zapobieganie-lenistwu-latka-halloweenowa-120241031}
Po napisaniu tego wpisu wprowadziłem po drodze 1–2 drobne usprawnienia promptu i doprecyzowania instrukcji, ale przez cztery miesiące działania systemu automatyzacji nie było większych problemów.

Jednak 31 października 12024 roku około 18:00 (czasu koreańskiego), gdy zleciłem tłumaczenie nowo napisanego posta, zaczęła regularnie występować anomalia: model tłumaczył jedynie początkową sekcję „TL;DR”, po czym samowolnie przerywał tłumaczenie.

Przewidywaną przyczynę i sposób rozwiązania omówiłem w [osobnym poście](/posts/does-ai-hate-to-work-on-halloween) — proszę tam zajrzeć.

### Finalny systemowy prompt
Końcowy rezultat projektowania promptu po przejściu powyższych kroków możesz zobaczyć w [następnej części](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2).

## Dalsza lektura
Ciąg dalszy w [Części 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
