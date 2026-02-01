---
title: "Jak dodać obsługę wielu języków na blogu Jekyll z Polyglot (2) — implementacja przycisku wyboru języka i lokalizacja języka układu"
description: "Jak wdrożyć Polyglot w blogu Jekyll opartym o „jekyll-theme-chirpy”: część 2. Implementacja przycisku wyboru języka i lokalizacja języka układu."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Przegląd
Na początku lipca 12024 roku dodałem do tego bloga (opartego na Jekyll i hostowanego przez GitHub Pages) obsługę wielu języków, wdrażając wtyczkę [Polyglot](https://github.com/untra/polyglot).
W tej serii dzielę się błędami, które pojawiły się podczas integracji Polyglot z motywem Chirpy, sposobem ich rozwiązania, a także metodą przygotowania nagłówków HTML i pliku sitemap.xml z uwzględnieniem SEO.
Seria składa się z 3 wpisów, a czytany teraz tekst to część druga.
- Część 1: [Wdrożenie wtyczki Polyglot oraz modyfikacja nagłówka HTML i sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Część 2: Implementacja przycisku wyboru języka i lokalizacja języka układu (ten wpis)
- Część 3: [Rozwiązywanie problemów: nieudany build motywu Chirpy oraz błędy funkcji wyszukiwania](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> Początkowo planowałem całość jako 2 części, jednak później kilkukrotnie uzupełniałem treść, przez co znacząco wzrosła objętość i ostatecznie przebudowałem serię do 3 części.
{: .prompt-info }

## Wymagania
- [x] Wynik builda (strony WWW) musi dać się serwować z rozróżnieniem na ścieżki per język (np. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Aby możliwie zminimalizować dodatkowy czas i nakład pracy związany z wielojęzycznością, podczas builda język ma być wykrywany automatycznie na podstawie lokalnej ścieżki pliku (np. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) — bez konieczności ręcznego dodawania tagów `lang` i `permalink` w YAML front matter w każdym pliku źródłowym Markdown.
- [x] Nagłówek każdej strony w serwisie musi spełniać wytyczne Google SEO dla wyszukiwania wielojęzycznego: odpowiedni meta tag Content-Language, tagi alternatywne hreflang oraz link canonical.
- [x] Linki do stron dla każdej wersji językowej muszą być kompletne w `sitemap.xml`{: .filepath}, a sam `sitemap.xml`{: .filepath} nie może się duplikować — ma istnieć wyłącznie jeden, w katalogu głównym (root).
- [x] Wszystkie funkcje dostarczane przez [motyw Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) muszą działać poprawnie na stronach w każdym języku; jeśli nie — trzeba je zmodyfikować, aby działały.
  - [x] Poprawne działanie „Recently Updated” i „Trending Tags”
  - [x] Brak błędów w procesie builda z użyciem GitHub Actions
  - [x] Poprawne działanie wyszukiwania postów w prawym górnym rogu bloga

## Zanim zaczniesz
Ten wpis jest kontynuacją [Części 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1), więc jeśli jeszcze jej nie czytałeś(-aś), polecam najpierw przeczytać poprzedni tekst.

## Dodanie przycisku wyboru języka do paska bocznego
> (Aktualizacja 12025.02.05.) Ulepszyłem(-am) przycisk wyboru języka do postaci listy rozwijanej (dropdown).
{: .prompt-info }

Utworzyłem(-am) plik `_includes/lang-selector.html`{: .filepath} i wpisałem(-am) poniższą treść.

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Select Language">
    {%- for lang in site.languages -%}
        <option value="{% if lang == site.default_lang %}{{ page.url }}{% else %}/{{ lang }}{{ page.url }}{% endif %}"
                {% if lang == site.active_lang %}selected{% endif %}>
            {% case lang %}
            {% when 'ko' %}🇰🇷 한국어
            {% when 'en' %}🇺🇸 English
            {% when 'ja' %}🇯🇵 日本語
            {% when 'zh-TW' %}🇹🇼 正體中文
            {% when 'es' %}🇪🇸 Español
            {% when 'pt-BR' %}🇧🇷 Português
            {% when 'fr' %}🇫🇷 Français
            {% when 'de' %}🇩🇪 Deutsch
            {% else %}{{ lang }}
            {% endcase %}
        </option>
    {%- endfor -%}
    </select>
</div>

<script>
function changeLang(url) {
    window.location.href = url;
}
</script>
```
{: file='\_includes/lang-selector.html'}
{% endraw %}

Dodatkowo utworzyłem(-am) plik `assets/css/lang-selector.css`{: .filepath} i wpisałem(-am) poniższą treść.

```css
/**
 * Style selektora języka
 * 
 * Definiuje wygląd rozwijanego selektora języka w pasku bocznym.
 * Wspiera tryb ciemny motywu i jest zoptymalizowany pod urządzenia mobilne.
 */

/* Kontener selektora języka */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Kontener dropdown */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Element wejściowy wyboru */
.lang-select {
    /* Styl bazowy */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Czcionka i kolory */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Kształt i interakcja */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Dodanie ikony strzałki */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Styl emoji flag */
.lang-select option {
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
    padding: 0.35rem;
    font-size: 1rem;
}

.lang-flag {
    display: inline-block;
    margin-right: 0.5rem;
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
}

/* Stan hover */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* Stan focus */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Obsługa przeglądarki Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Obsługa przeglądarki IE */
.lang-select::-ms-expand {
    display: none;
}

/* Obsługa trybu ciemnego */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Optymalizacja dla urządzeń mobilnych */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* większy obszar dotyku */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* szerszy obszar wyboru na mobile */
    }
}
```
{: file='assets/css/lang-selector.css'}

Następnie, w pliku [Chirpy `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html), dodałem(-am) trzy linie z klasą `lang-selector-wrapper` bezpośrednio przed klasą `sidebar-bottom`, aby Jekyll w trakcie builda wczytywał treść wcześniej przygotowanego `_includes/lang-selector.html`{: .filepath}.

{% raw %}
```liquid
  (전략)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(후략)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (12025.07.31. dodanie funkcji) Lokalizacja języka układu
Wcześniej lokalizację językową stosowałem(-am) wyłącznie do treści głównej (np. tytułu strony i zawartości wpisu), natomiast język elementów układu — takich jak nazwy zakładek w lewym pasku bocznym, stopka/górna belka strony czy prawy panel — był na stałe ustawiony na domyślny język serwisu, czyli angielski. Osobiście uważałem(-am), że to w zupełności wystarcza, więc nie odczuwałem(-am) potrzeby dalszych prac.  
Jednak w trakcie przygotowywania [wspomnianej wyżej łatki dla właściwości metadanych Open Graph oraz standardowego URL (canonical URL)](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#nagłówek-html) zauważyłem(-am), że lokalizacja języka układu jest zaskakująco prosta i wymaga tylko drobnych poprawek. Gdyby wymagało to dużej, uciążliwej refaktoryzacji — pewnie bym tego nie robił(-a), ale ponieważ była to [prosta zmiana, zajmująca nawet nie 10 minut](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb), przy okazji wdrożyłem(-am) ją również.

### Dodanie plików locale
Chirpy nie oferuje co prawda funkcji równoległego dostarczania wielu wersji językowych tej samej strony i przełączania się między nimi w zależności od wyboru użytkownika, ale [sam zakres języków wspieranych przez motyw Chirpy jest od początku całkiem szeroki](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales). Wystarczy więc selektywnie pobrać potrzebne pliki locale i dodać je do projektu, a jeśli trzeba — odpowiednio zmienić nazwę pliku. Nazwy plików locale muszą zgadzać się z elementami listy `languages` zdefiniowanej wcześniej w pliku `_config.yml`{: .filepath} na etapie [Konfiguracja](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#konfiguracja).

> W praktyce (o czym wspomnę jeszcze za chwilę) plików w katalogu `_data`{: .filepath} nie trzeba dodawać ręcznie — są one dostarczane domyślnie przez [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy).
>
> W moim przypadku jednak nie mogłem(-am) użyć tych plików „as is” i potrzebowałem(-am) kilku poprawek z następujących powodów:
> - Domyślne nazwy plików locale w Chirpy zawierają kod regionu, np. `ko-KR`, `ja-JP`, co nie pasuje do formatu używanego na tej stronie (`ko`, `ja` itd.).
> - Trzeba było dopasować komunikat licencyjny: zamiast domyślnego [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) do [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) używanego na tym blogu.
> - Pliki locale dla [koreańskiego](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) i [japońskiego](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) były (z mojej perspektywy) nieco nienaturalne lub nie pasowały do tego bloga, więc miejscami poprawiłem(-am) je ręcznie.
> - Jak opisałem(-am) poniżej, z różnych powodów nie przepadam za erą chrześcijańską i na tym blogu przyjąłem(-am) [kalendarz holoceński](https://en.wikipedia.org/wiki/Holocene_calendar) jako format zapisu dat, więc pliki locale trzeba było dopasować pod to.
>   - System jest z natury mocno nacechowany religijnie i zachodniocentryczny.
>     - Nie neguję, że Jezus jest wielką postacią, i szanuję perspektywę tej religii — gdyby era chrześcijańska była używana wyłącznie wewnątrz tej religii, jak np. buddyjska era Nirwany, nie byłoby problemu. Problem polega na tym, że nie jest. Jest wielu innych wielkich nauczycieli (Konfucjusz, Budda, Sokrates itd.), więc dlaczego z perspektywy osób niereligijnych, wyznawców innych religii oraz kultur spoza Europy „rok 1” globalnego systemu datowania ma koniecznie odpowiadać narodzinom Jezusa?
>     - Co więcej, nawet jeśli zapytać, czy ten „rok 1” faktycznie odpowiada historycznemu rokowi narodzin Jezusa, to odpowiedź brzmi: według konsensusu raczej nie — urodził się kilka lat wcześniej.
>   - Jest to system wymyślony przed upowszechnieniem koncepcji „0”, więc po 1 roku p.n.e. (-1) następuje od razu 1 rok n.e. (1), co jest nieintuicyjne w obliczeniach na latach.
>   - Około 10 000 lat historii ludzkości (od wejścia w neolit i społeczeństwa rolnicze do czasu narodzin Jezusa), a nawet 3000–4000 lat po wynalezieniu pisma, wrzuca się zbiorczo do kategorii „p.n.e.”, co wywołuje zniekształcenia poznawcze w historii świata, zwłaszcza starożytnej.
>
> Dlatego w tym przypadku dodałem(-am) pliki locale bezpośrednio do katalogu `_data/locales`{: .filepath} i dostosowałem(-am) je ręcznie.  
> Jeśli u Ciebie te problemy nie występują i chcesz użyć domyślnych plików locale Chirpy bez modyfikacji, możesz pominąć ten krok.
{: .prompt-tip }

### Integracja z Polyglot
Teraz wystarczy lekko zmodyfikować tylko dwa pliki, aby uzyskać płynną integrację z Polyglot.

> Jeśli podczas tworzenia repozytorium nie forkowałeś(-aś) repozytorium motywu bezpośrednio, tylko użyłeś(-aś) [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended), to w Twoim repozytorium może nie być tych plików. Wynika to z tego, że są one dostarczane domyślnie przez [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy). W takim przypadku pobierz najpierw oryginalne pliki z [repozytorium motywu Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) i umieść je w tym samym miejscu w swoim repozytorium, a dopiero potem wprowadź zmiany.  
> Podczas builda, jeśli w repozytorium istnieje plik o tej samej nazwie, Jekyll użyje go z priorytetem względem pliku dostarczanego przez [zewnętrzny gem (jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy).
{: .prompt-tip }

#### '\_includes/lang.html'
Jak poniżej, dodałem(-am) dwie linie kodu w środku pliku [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html), tak aby — jeśli w YAML front matter strony nie ustawiono jawnie zmiennej `lang` — priorytetowo używać [zmiennej `site.active_lang` z Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#features), a nie domyślnego języka serwisu z `_config.yml`{: .filepath} (`site.lang`) ani angielskiego (`'en'`).  
Ten plik jest wspólnie wywoływany podczas builda przez wszystkie strony w serwisie opartym o Chirpy (z poziomu [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) w celu deklaracji zmiennej `lang` — a właśnie ta zmienna steruje lokalizacją języka układu.

{% raw %}
```diff
@@ -1,10 +1,12 @@
 {% comment %}
   Detect appearance language and return it through variable "lang"
 {% endcomment %}
 {% if site.data.locales[page.lang] %}
   {% assign lang = page.lang %}
+{% elsif site.data.locales[site.active_lang] %}
+  {% assign lang = site.active_lang %}
 {% elsif site.data.locales[site.lang] %}
   {% assign lang = site.lang %}
 {% else %}
   {% assign lang = 'en' %}
 {% endif %}
```
{: file='\_includes/lang.html'}
{% endraw %}

Priorytety przy deklaracji zmiennej `lang`:
- Przed modyfikacją:
  1. `page.lang` (jeśli zdefiniowano w YAML front matter danej strony)
  2. `site.lang` (jeśli zdefiniowano w `_config.yml`{: .filepath})
  3. `'en'`
- Po modyfikacji:
  1. `page.lang` (jeśli zdefiniowano w YAML front matter danej strony)
  2. **`site.active_lang`** (jeśli używasz Polyglot)
  3. `site.lang` (jeśli zdefiniowano w `_config.yml`{: .filepath})
  4. `'en'`

#### '\_layouts/default.html'
Podobnie zmodyfikowałem(-am) plik [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html), aby poprawnie ustawić atrybut `lang` w tagu `<html>`, czyli w najwyższym elemencie dokumentu HTML.

{% raw %}
```diff
@@ -1,19 +1,19 @@
 ---
 layout: compress
 ---
 
 <!doctype html>
 
 {% include origin-type.html %}
 
 {% include lang.html %}
 
 {% if site.theme_mode %}
   {% capture prefer_mode %}data-mode="{{ site.theme_mode }}"{% endcapture %}
 {% endif %}
 
 <!-- `site.alt_lang` can specify a language different from the UI -->
-<html lang="{{ page.lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
+<html lang="{{ page.lang | default: site.active_lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
   {% include head.html %}
```
{: file='\_layouts/default.html'}
{% endraw %}

Priorytety przy ustawianiu atrybutu `lang` w tagu `<html>`:
- Przed modyfikacją:
  1. `page.lang` (jeśli zdefiniowano w YAML front matter danej strony)
  2. `site.alt_lang` (jeśli zdefiniowano w `_config.yml`{: .filepath})
  3. `site.lang` (jeśli zdefiniowano w `_config.yml`{: .filepath})
  4. `unknown` (pusty string, `lang=""`)
- Po modyfikacji:
  1. `page.lang` (jeśli zdefiniowano w YAML front matter danej strony)
  2. **`site.active_lang`** (jeśli używasz Polyglot)
  3. `site.alt_lang` (jeśli zdefiniowano w `_config.yml`{: .filepath})
  4. `site.lang` (jeśli zdefiniowano w `_config.yml`{: .filepath})
  5. `unknown` (pusty string, `lang=""`)

> Pozostawienie języka strony (`lang`) jako `unknown` nie jest zalecane — najlepiej ustawić możliwie poprawną wartość. Jak widać, jako fallback używana jest wartość `lang` z `_config.yml`{: .filepath}, więc niezależnie od tego, czy korzystasz z Polyglot, warto ten parametr poprawnie zdefiniować (w typowym przypadku i tak jest już ustawiony).  
> Jeśli wdrażasz Polyglot lub podobną wtyczkę i18n, rozsądnie jest ustawić go na tę samą wartość co [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#konfiguracja).
{: .prompt-tip }

## Dalsza lektura
Ciąg dalszy w [Części 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
