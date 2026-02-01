---
title: Tworzenie i zarządzanie blogiem na GitHub Pages
description: Poznaj różnice między stronami statycznymi i dynamicznymi oraz SSG. Zobacz, jak zbudować blog Jekyll i hostować go na GitHub Pages.
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

Na początku 12021 roku zacząłem hostować bloga na GitHub Pages, używając Jekylla. Problem w tym, że podczas budowy bloga nie uporządkowałem porządnie procesu instalacji, więc później pojawiły się pewne trudności przy utrzymaniu. Dlatego postanowiłem choćby skrótowo spisać proces instalacji i sposób dalszego utrzymania.  

(+ aktualizacja treści 12024.12)

## 1. Generator stron statycznych & hosting WWW
### 1-1. Statyczna strona WWW vs dynamiczna strona WWW
#### Statyczna strona WWW (Static Web Page)
- strona WWW, która przekazuje użytkownikowi dane zapisane na serwerze w niezmienionej postaci
- serwer WWW dostarcza wcześniej zapisany plik strony odpowiadający żądaniu użytkownika
- dopóki użytkownik nie zmieni danych zapisanych na serwerze, będzie widzieć tę samą stronę
- ponieważ wystarczy wysłać tylko plik odpowiadający żądaniu, nie są potrzebne dodatkowe operacje; zwykle odpowiedź jest szybka
- składa się wyłącznie z prostych plików, więc wystarczy postawić serwer WWW — niskie koszty wdrożenia
- pokazuje tylko zapisane informacje, więc zakres usługi jest ograniczony
- dodawanie, modyfikowanie i usuwanie danych administrator wykonuje ręcznie
- struktura ułatwia crawling po stronie wyszukiwarek, więc jest relatywnie korzystna pod kątem optymalizacji dla wyszukiwarek (SEO)

#### Dynamiczna strona WWW (Dynamic Web Page)
- strona WWW, która przetwarza dane zapisane na serwerze za pomocą skryptów i dopiero tak je dostarcza
- serwer WWW interpretuje żądanie użytkownika, przetwarza dane i przekazuje wygenerowaną stronę
- użytkownik widzi stronę zmieniającą się zależnie od sytuacji, czasu, żądania itd.
- do dostarczenia strony trzeba wykonać skrypty, więc odpowiedź jest relatywnie wolniejsza
- oprócz serwera WWW potrzebny jest serwer aplikacyjny, co generuje dodatkowe koszty przy wdrożeniu
- dzięki dynamicznemu łączeniu informacji możliwe jest oferowanie różnorodnych usług
- zależnie od struktury strony użytkownik może dodawać, modyfikować i usuwać dane w przeglądarce

### 1-2. Generator statycznych stron WWW (SSG, Static Site Generator)
- narzędzie, które na podstawie surowych danych (zwykle plików tekstowych w formacie Markdown) oraz zdefiniowanych szablonów generuje statyczne strony WWW
- zamiast ręcznie pisać osobne strony HTML, automatyzuje proces: piszesz post w Markdown, a system buduje stronę i publikuje ją w sieci
- np. Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- darmowa usługa hostingu statycznych stron WWW oferowana przez GitHub
- na jedno konto można hostować 1 osobistą stronę główną, a dodatkowo można bez limitu tworzyć i hostować strony dokumentacji projektów dla poszczególnych repozytoriów
- po utworzeniu repozytorium dopasowanego do własnej nazwy użytkownika GitHub w formacie `{username}.github.io` można bezpośrednio wypchnąć (Push) zbudowane strony HTML do tego repozytorium albo użyć GitHub Actions do budowania i wdrażania
- jeśli masz własną domenę, możesz podpiąć ją w ustawieniach i używać innego adresu niż domyślna domena `{username}.github.io`

## 2. Wybór SSG i motywu

### 2-1. Dlaczego wybrałem Jekylla
Istnieje wiele SSG, takich jak Jekyll, Hugo czy Gatsby, ale zdecydowałem się na Jekylla. Kryteria, które brałem pod uwagę przy wyborze SSG, oraz powody wyboru Jekylla są następujące:
- czy da się zminimalizować zbędne próby i błędy oraz skupić na pisaniu i prowadzeniu bloga?
  - Jekyll jest oficjalnie wspieranym generatorem stron statycznych na GitHub Pages. Oczywiście inne SSG, takie jak Hugo czy Gatsby, też można bez problemu hostować na GitHub Pages, a alternatywą jest skorzystanie z innego hostingu, np. Netlify. Jednak przy blogu osobistym tej skali technicznie nie jest aż tak ważne, jakim SSG to zbudowano oraz jaka jest prędkość builda czy wydajność — uznałem więc, że lepiej wybrać coś, co będzie choć trochę prostsze w utrzymaniu i ma dużo materiałów referencyjnych.
  - Jekyll ma też najdłuższy czas rozwoju w porównaniu z konkurentami jak Hugo czy Gatsby. Dzięki temu dokumentacja jest bardzo dobra, a gdy pojawi się problem, ilość dostępnych materiałów pomocniczych jest przytłaczająco duża.
- czy dostępnych jest wiele motywów i wtyczek?
  - nawet jeśli używa się SSG zamiast ręcznie pisać HTML, tworzenie własnych szablonów jest uciążliwe i czasochłonne, a często nie ma sensu. W sieci jest wiele świetnych gotowych motywów — wystarczy wybrać i użyć.
  - dodatkowo, ponieważ na co dzień używam głównie C i Pythona, Ruby (Jekyll) i Go (Hugo) nie są dla mnie tak naturalne, więc tym bardziej chciałem aktywnie wykorzystywać istniejące motywy i wtyczki.
  - w Jekyllu szybko znalazłem motyw, który od razu mi się spodobał, natomiast w Hugo czy Gatsby liczba motywów sensownych pod blog osobisty wydawała mi się mniejsza. Prawdopodobnie duże znaczenie miała tu — jak wyżej — integracja z GitHub Pages (popularnym do hostowania blogów) oraz dłuższy czas rozwoju ekosystemu.

### 2-2. Wybór motywu
#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- motyw używany przez ok. 1 rok i 3 miesiące od momentu założenia bloga
- obsługa komentarzy przez Disqus, Discourse, utterances itd.
- obsługa kategoryzacji i tagów
- wbudowane wsparcie dla Google Analytics
- możliwość wyboru predefiniowanych skórek (skinów)
- później znalazłem ładniejszy i bardziej odpowiadający mi motyw Chirpy i przeszedłem na niego, ale biorąc pod uwagę „inżynierski” charakter bloga: nawet jeśli nie był szczególnie piękny, miał dość czysty design i dało się go sensownie używać.

#### Chirpy Jekyll Theme (12022.04 - obecnie)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- motyw używany od migracji w kwietniu 12022 do teraz
- obsługa wielopoziomowych kategorii i tagów
- domyślne wsparcie dla zapisu wzorów w LaTeX na bazie MathJax
- domyślne wsparcie dla diagramów na bazie Mermaid
- obsługa komentarzy przez Disqus, Giscus itd.
- wsparcie dla Google Analytics, GoatCounter
- wsparcie dla motywu jasnego i ciemnego
- w momencie zmiany motywu MathJax i Mermaid nie były natywnie wspierane w Minimal Mistakes, więc trzeba je było dodać samodzielnie poprzez customizację; w Chirpy są wspierane domyślnie. Oczywiście to nie jest jakaś wielka przeróbka, ale jednak drobna zaleta.
- przede wszystkim: jest ładny. Minimal Mistakes jest czysty, ale ma pewną „sztywność” bardziej pasującą do oficjalnej dokumentacji projektu lub portfolio niż do bloga. Chirpy ma tę zaletę, że wyglądem wcale nie ustępuje komercyjnym platformom blogowym typu Tistory, Medium czy velog.

## 3. Utworzenie repozytorium GitHub, build i wdrożenie
Opis bazuje na używanym obecnie (12024.06) Chirpy Jekyll Theme; zakładam, że Git jest już zainstalowany.  
Warto zajrzeć do: [oficjalny poradnik instalacji Jekyll](https://jekyllrb.com/docs/installation/) oraz [oficjalna strona Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalacja Ruby i Jekyll
Zgodnie z [oficjalnym poradnikiem instalacji Jekyll](https://jekyllrb.com/docs/installation/) zainstaluj Ruby i Jekyll odpowiednio do swojego systemu operacyjnego.

### 3-2. Utworzenie repozytorium GitHub
Na [oficjalnej stronie Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) opisane są dwie metody:
1. wczytanie plików rdzenia przez gem „jekyll-theme-chirpy”, a resztę zasobów pobranie z szablonu [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - zaleta: jak opiszę niżej, łatwo stosować aktualizacje wersji
  - wada: przy dużej customizacji może być wręcz niewygodne
2. zforkowanie repozytorium [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) jako repozytorium własnego bloga
  - zaleta: zarządzasz wszystkimi plikami bezpośrednio w repozytorium, więc łatwo modyfikować kod i dodawać funkcje nieobsługiwane przez motyw
  - wada: aby zastosować aktualizację wersji, trzeba zmergować [najnowszy upstream tag z oryginalnego repozytorium](https://github.com/cotes2020/jekyll-theme-chirpy/tags); w zależności od przypadku kod, który sam zmodyfikowałeś, może wejść w konflikt z nową wersją. Wtedy trzeba samodzielnie rozwiązać konflikty.

Wybrałem metodę 1. W przypadku motywu Chirpy jakość bazowa jest wysoka, więc z perspektywy większości użytkowników nie ma wielu rzeczy do customizacji. Do tego, nawet w 12024 roku rozwój i ulepszanie funkcji nadal jest dość aktywne, więc o ile nie planujesz dużych i „rzeźniczych” przeróbek, korzyści z nadążania za upstreamem na czas przewyższają korzyści z ciężkiej customizacji. Oficjalny przewodnik Chirpy również rekomenduje metodę 1 większości użytkowników.

### 3-3. Kluczowe ustawienia
W pliku `_config.yml`{: .filepath} w katalogu głównym oraz w plikach `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath} zastosuj potrzebne ustawienia. Komentarze są dobrze napisane, a konfiguracja jest intuicyjna, więc da się to zrobić bez większych problemów. W zasadzie jedyne ustawienia wymagające działań na zewnątrz to rejestracja kodu weryfikacyjnego do integracji z Google Search Console oraz integracja z narzędziami webmastera typu Google Analytics czy GoatCounter. To też nie jest szczególnie złożone, a nie jest głównym tematem tego wpisu, więc pominę szczegółowy opis.

### 3-4. Build lokalny
Nie jest to krok obowiązkowy, ale gdy napiszesz nowy post lub wprowadzisz jakieś zmiany w serwisie, możesz chcieć sprawdzić wcześniej, czy wszystko poprawnie się wyświetla. W takiej sytuacji otwórz terminal w katalogu głównym lokalnego repozytorium i uruchom:
```console
$ bundle exec jekyll s
```
Po chwili strona zbuduje się lokalnie i możesz sprawdzić wynik pod adresem <http://127.0.0.1:4000>.

### 3-5. Wdrażanie
Są dwie metody.
1. Wykorzystanie GitHub Actions (gdy hostujesz na GitHub Pages)
  - jeśli używasz GitHub Free Plan, repozytorium musi pozostać publiczne
  - na stronie repozytorium na GitHub wybierz zakładkę *Settings*, następnie w lewym pasku nawigacji kliknij *Code and automation > Pages* i w sekcji **Source** wybierz opcję **GitHub Actions**
  - po zakończeniu konfiguracji, przy każdym Push nowego commita automatycznie uruchomi się workflow *Build and Deploy*
2. Ręczny build i wdrożenie (gdy korzystasz z innego hostingu lub hostujesz samodzielnie)
  - uruchom poniższe polecenie, aby samodzielnie zbudować stronę
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - wgraj na serwer wynik builda znajdujący się w katalogu `_site`

## 4. Pisanie postów
W [przewodniku pisania postów](https://chirpy.cotes.page/posts/write-a-new-post/) dla motywu Chirpy dobrze udokumentowano sposób tworzenia wpisów i dostępne opcje. Poza tym, co opisuję w tym tekście, motyw oferuje też wiele dodatkowych funkcji — jeśli potrzeba, warto zajrzeć do dokumentacji. Podstawową składnię GitHub Flavored Markdown zebrałem wcześniej w [osobnym wpisie](/posts/github-markdown-syntax-summary/). Tutaj podsumowuję kluczowe rzeczy, o których warto pamiętać przy każdym publikowaniu.

### Tworzenie pliku Markdown
- format nazwy: `YYYY-MM-DD-TITLE.md`{: .filepath}
- lokalizacja: katalog `_posts`{: .filepath}

### Pisanie Front Matter
Na początku pliku Markdown należy poprawnie przygotować Front Matter.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: tytuł posta
- **description**: streszczenie. Jeśli go nie podasz, automatycznie zostanie użyty początkowy fragment treści, ale ze względu na optymalizację dla wyszukiwarek (SEO) zaleca się ręcznie wpisać sensowny meta tag description. Odpowiednia długość to ok. 135–160 znaków w alfabecie łacińskim oraz ok. 80–110 znaków w hangulu.
- **date**: dokładna data i godzina publikacji oraz strefa czasowa (opcjonalnie; jeśli pominięte, automatycznie wykorzystywana jest data utworzenia lub modyfikacji pliku)
- **categories**: kategoryzacja posta
- **tags**: tagi przypisane do posta
- **image**: wstawienie obrazka podglądowego na górze posta
  - **path**: ścieżka do pliku obrazu
  - **alt**: tekst alternatywny (opcjonalnie)
- **toc**: czy włączyć spis treści w prawym pasku bocznym; domyślnie `true`
- **comments**: jeśli chcesz jawnie ustawić dla konkretnego posta włączenie/wyłączenie komentarzy niezależnie od globalnej konfiguracji
- **math**: włączenie wbudowanej obsługi wzorów na bazie [MathJax](https://www.mathjax.org/); domyślnie wyłączone (`false`) dla wydajności
- **mermaid**: włączenie wbudowanej obsługi diagramów na bazie [Mermaid](https://github.com/mermaid-js/mermaid); domyślnie wyłączone (`false`)

## 5. Aktualizacje (upgrade)

Opis zakłada, że w [3-2](#3-2-utworzenie-repozytorium-github) wybrano metodę 1. Jeśli wybrałeś metodę 2, jak wspomniałem, musisz ręcznie zmergować najnowszy upstream tag.

1. Edytuj `Gemfile`{: .filepath} i ustaw nową wersję gema „jekyll-theme-chirpy”.
2. W przypadku aktualizacji major możliwe, że zmieniły się także pliki rdzenia i opcje konfiguracyjne, które nie są częścią gema „jekyll-theme-chirpy”. Wtedy sprawdź zmiany przez poniższe API GitHuba i zastosuj je ręcznie.
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
