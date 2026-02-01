---
title: "Jak dodać obsługę wielu języków na blogu Jekyll z Polyglot (1) — wdrożenie wtyczki Polyglot oraz modyfikacja nagłówka HTML i sitemap"
description: "Opis wdrożenia wtyczki Polyglot w blogu Jekyll opartym na „jekyll-theme-chirpy”, aby uruchomić wielojęzyczność. Część 1 serii: instalacja Polyglot oraz modyfikacje nagłówka HTML i pliku sitemap pod SEO."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## Przegląd
Na początku lipca 12024 roku dodałem do tego bloga (opartego na Jekyll i hostowanego przez GitHub Pages) obsługę wielu języków, wdrażając wtyczkę [Polyglot](https://github.com/untra/polyglot).
W tej serii dzielę się błędami, które pojawiły się podczas integracji Polyglot z motywem Chirpy, sposobem ich rozwiązania, a także metodą przygotowania nagłówków HTML i pliku sitemap.xml z uwzględnieniem SEO.
Seria składa się z 3 wpisów, a czytany teraz tekst to część pierwsza.
- Część 1: Wdrożenie wtyczki Polyglot oraz modyfikacja nagłówka HTML i sitemap (ten wpis)
- Część 2: [Implementacja przycisku wyboru języka i lokalizacja języka układu](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
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

## Wdrożenie wtyczki Polyglot
Jekyll nie wspiera wielojęzycznych blogów natywnie, więc aby zrealizować blog wielojęzyczny spełniający powyższe wymagania, trzeba użyć zewnętrznej wtyczki. Po rozeznaniu okazało się, że [Polyglot](https://github.com/untra/polyglot) jest często używany do budowy wielojęzycznych stron i może spełnić większość z powyższych wymagań, więc wybrałem tę wtyczkę.

### Instalacja wtyczki
Ponieważ używam Bundlera, dodałem do `Gemfile` poniższą treść.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Następnie wystarczy uruchomić w terminalu `bundle update`, a instalacja zakończy się automatycznie.

Jeśli nie używasz Bundlera, możesz zainstalować gema bezpośrednio poleceniem `gem install jekyll-polyglot`, a potem dodać wtyczkę w `_config.yml`{: .filepath} w następujący sposób:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfiguracja
Następnie otwórz plik `_config.yml`{: .filepath} i dodaj poniższe:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: lista języków, które mają być wspierane
- `default_lang`: domyślny język fallback
- `exclude_from_localization`: wyrażenia (regex) dla ścieżek plików/katalogów w root, które mają być wyłączone z lokalizacji językowej
- `parallel_localization`: wartość boolean określająca, czy przetwarzanie wielojęzyczne ma być równoległe podczas builda
- `lang_from_path`: wartość boolean; po ustawieniu na `true` Polyglot rozpozna i użyje kodu języka z ciągu ścieżki pliku Markdown (o ile ścieżka zawiera kod języka), nawet jeśli w YAML front matter nie podasz osobno właściwości `lang`

> [Oficjalna dokumentacja protokołu Sitemap](https://www.sitemaps.org/protocol.html#location) stwierdza:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Aby się do tego dostosować, trzeba dopilnować, żeby plik `sitemap.xml`{: .filepath} nie był generowany osobno dla każdego języka, tylko istniał dokładnie jeden w katalogu głównym. W tym celu dodaj `sitemap.xml`{: .filepath} do listy `exclude_from_localization`, aby nie doszło do sytuacji jak w poniższym błędnym przykładzie.
>
> Błędny przykład (zawartość każdego pliku nie różni się między językami — jest identyczna):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Aktualizacja 12025.01.14.) Ponieważ przyjęto mój [Pull Request, w którym uzupełniłem README o powyższe informacje](https://github.com/untra/polyglot/pull/230), teraz takie samo zalecenie można znaleźć także w [oficjalnej dokumentacji Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Ustawienie `parallel_localization` na `true` ma tę zaletę, że znacząco skraca czas builda, jednak według stanu na lipiec 12024, gdy włączyłem tę funkcję na tym blogu, występował błąd: tytuły linków w sekcjach „Recently Updated” i „Trending Tags” na prawym pasku bocznym nie były przetwarzane poprawnie i mieszały się między językami. Wygląda na to, że funkcja nie była jeszcze w pełni stabilna — przed użyciem na swojej stronie warto ją przetestować. Dodatkowo [jeśli używasz Windows, ta funkcja nie jest wspierana, więc trzeba ją wyłączyć](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
>
> (Aktualizacja 12025.09) Latem 12025 ponownie przetestowałem `parallel_localization` na tym blogu i wtedy działało poprawnie. W związku z tym obecnie mam tę funkcję włączoną, co istotnie skróciło czas builda.
{: .prompt-warning }

Dodatkowo, [w Jekyll 4.0 należy wyłączyć generowanie CSS sourcemaps w następujący sposób](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Uwagi przy pisaniu postów
Poniżej rzeczy, na które trzeba uważać, pisząc posty wielojęzyczne:
- Poprawne wskazanie kodu języka: należy podać właściwy kod ISO, korzystając ze ścieżki pliku (np. `/_posts/ko/example-post.md`{: .filepath}) albo z właściwości `lang` w YAML front matter (np. `lang: ko`). Warto oprzeć się na przykładach z [dokumentacji dla programistów Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Uwaga: w [dokumentacji deweloperskiej Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) kod regionu bywa zapisywany jako `pt_BR`, ale w praktyce trzeba użyć `pt-BR` (myślnik zamiast podkreślenia), aby później tagi alternatywne hreflang w nagłówku HTML działały poprawnie.
{: .prompt-tip }

- Ścieżki i nazwy plików powinny być spójne.

Szczegóły znajdziesz w README repozytorium GitHub: [untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modyfikacja nagłówka HTML i sitemap
Teraz, na potrzeby SEO, trzeba wstawić do nagłówka HTML każdej strony meta tag Content-Language, alternatywne tagi hreflang oraz poprawnie ustawić adres kanoniczny (canonical URL).

### Nagłówek HTML
Według stanu na 12024.11, w wersji 1.8.1 (wówczas najnowszej), Polyglot ma funkcję, która automatycznie wykonuje powyższe działania, gdy w nagłówku strony wywołasz tag Liquid {% raw %}`{% I18n_Headers %}`{% endraw %}.
Jednak funkcja ta zakłada, że dla danej strony jawnie ustawiono atrybut `permalink`; w przeciwnym razie nie działa poprawnie.

Dlatego skopiowałem [head.html z motywu Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) i samodzielnie dodałem poniższą treść.
Kierowałem się stroną [SEO Recipes na oficjalnym blogu Polyglot](https://polyglot.untra.io/seo/), ale dopasowałem implementację do mojego środowiska i wymagań — zamiast `page.permalink` użyłem właściwości `page.url`.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">
  
  {% if site.default_lang -%}
  <link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />
  {%- endif -%}
  {% for lang in site.languages -%}
    {% if lang == site.default_lang -%}
      {%- continue -%}
    {%- endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {%- endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

(Dodano 12025.07.29.) Motyw Chirpy domyślnie zawiera również wtyczkę [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag). Potwierdziłem jednak, że automatycznie generowane przez nią metadane [Open Graph](https://ogp.me/) `og:locale` i `og:url`, a także [adres kanoniczny (canonical URL)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (element `link` z `rel="canonical"`) są generowane względem podstawowego języka strony (`site.lang`, `site.default_lang`), więc potrzebna jest dodatkowa obróbka.  
W związku z tym dodałem następujący fragment przed {% raw %}`{{ seo_tags }}`{% endraw %}.

{% raw %}
```liquid
(전략)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(중략)...

  {%- capture old_og_locale -%}
    <meta property="og:locale" content="{{site.lang}}" />
  {%- endcapture -%}
  {%- capture new_og_locale -%}
    <meta property="og:locale" content="{{site.active_lang}}" />
    {% for lang in site.languages -%}
      {%- if lang == site.active_lang -%}
        {%- continue -%}
      {%- endif %}
    <meta property="og:locale:alternate" content="{{lang}}" />
    {%- endfor %}
  {%- endcapture -%}
  {% assign seo_tags = seo_tags | replace: old_og_locale, new_og_locale %}
  
  {% unless site.active_lang == site.default_lang -%}
    {%- capture old_canonical_link -%}
      <link rel="canonical" href="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture old_og_url -%}
      <meta property="og:url" content="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_canonical_link -%}
      <link rel="canonical" href="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_og_url -%}
      <meta property="og:url" content="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {% assign seo_tags = seo_tags | replace: old_canonical_link, new_canonical_link %}
    {% assign seo_tags = seo_tags | replace: old_og_url, new_og_url %}
  {%- endunless %}

  {{ seo_tags }}

  ...(후략)
```
{: file='/_includes/head.html'}
{% endraw %}

> Zgodnie z [dokumentacją dla deweloperów Google](https://developers.google.com/search/docs/crawling-indexing/canonicalization), gdy jedna strona ma wiele wersji językowych, Google uznaje je za duplikaty tylko wtedy, gdy język głównej treści jest taki sam — tzn. przetłumaczone są wyłącznie nagłówek, stopka i inne mało istotne fragmenty, a zasadnicza treść pozostaje identyczna. Dlatego w przypadku takiego bloga jak ten, gdzie treść wpisów jest dostępna w wielu językach, każdą wersję językową należy traktować jako osobną, nieduplikującą się stronę — i trzeba ustawić różne canonical URL zależnie od języka.  
> Na przykład dla koreańskiej wersji tej strony canonical URL to nie `"{{site.url}}{{page.url}}"`, lecz `"{{site.url}}/ko{{page.url}}"`.
{: .prompt-tip }

### Sitemap
Jeśli nie wskażesz osobnego szablonu, sitemap generowany automatycznie przez Jekyll podczas builda nie wspiera poprawnie stron wielojęzycznych. Dlatego utwórz w katalogu głównym plik `sitemap.xml`{: .filepath} i wprowadź następującą treść:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages -%}

  {% for node in site.pages %}
    {%- comment -%}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{%- endcomment -%}
    {%- comment -%}<!-- Exclude redirects from sitemap -->{%- endcomment -%}
    {%- if node.redirect.to -%}
      {%- continue -%}
    {%- endif -%}
    {%- unless site.exclude_from_localization contains node.path -%}
      {%- comment -%}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{%- endcomment -%}
      {% if node.layout %}
        <url>
          <loc>
            {%- if lang == site.default_lang -%}
              {{ node.url | absolute_url }}
            {%- else -%}
              {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
            {%- endif -%}
          </loc>
          {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {% endif -%}
          {% if site.default_lang -%}
          <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
          {%- endif -%}
          {% for lang in site.languages -%}
            {% if lang == site.default_lang -%}
              {%- continue -%}
            {%- endif %}
          <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
          {%- endfor %}
        </url>
      {% endif %}
    {%- elsif site.default_lang -%}
        <url>
          <loc>{{ node.url | absolute_url }}</loc>
      {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {% endif -%}
        </url>
    {%- endunless -%}
  {% endfor %}

  {%- comment -%}<!-- This loops through all site collections including posts -->{%- endcomment -%}
  {% for collection in site.collections %}
    {% for node in site[collection.label] %}
      <url>
        <loc>
          {%- if lang == site.default_lang -%}
            {{ node.url | absolute_url }}
          {%- else -%}
            {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
          {%- endif -%}
        </loc>
        {% if node.last_modified_at and node.last_modified_at != node.date -%}
        <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- elsif node.date -%}
        <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- endif %}
        {% if site.default_lang -%}
        <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
        {%- endif -%}
        {% for lang in site.languages -%}
          {% if lang == site.default_lang -%}
            {%- continue -%}
          {%- endif %}
        <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
        {%- endfor %}
      </url>
    {% endfor %}
  {% endfor %}

{%- endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## Dalsza lektura
Ciąg dalszy w [Części 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
