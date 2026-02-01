---
title: "Jak přidat vícejazyčnou podporu do Jekyll blogu pomocí Polyglot (1) – nasazení pluginu Polyglot a úprava HTML hlavičky a sitemap"
description: "Popisuji proces, jak jsem do Jekyll blogu na bázi 'jekyll-theme-chirpy' nasadil plugin Polyglot a zavedl vícejazyčnou podporu. 1. díl: nasazení Polyglot, úpravy HTML hlavičky a sitemap.xml s ohledem na SEO."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## Přehled
Začátkem července 12024 jsem na tento blog (hostovaný přes GitHub Pages a postavený na Jekyllu) nasadil plugin [Polyglot](https://github.com/untra/polyglot) a doplnil tak podporu více jazyků.  
V této sérii sdílím bugy, které se objevily při aplikaci Polyglot na téma Chirpy, jejich řešení a také způsob úprav HTML hlavičky a `sitemap.xml`{: .filepath} s ohledem na SEO.  
Série se skládá ze 3 článků a tento, který právě čtete, je její první díl.

- 1. díl: Nasazení pluginu Polyglot & úprava HTML hlavičky a sitemap (tento článek)
- 2. díl: [Implementace tlačítka pro výběr jazyka & lokalizace jazyka rozvržení](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- 3. díl: [Troubleshooting: selhání buildu tématu Chirpy a chyby ve vyhledávání](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> Původně byla série ve 2 dílech, ale jak jsem ji později v několika krocích doplňoval, výrazně narostl rozsah, a proto jsem ji přepracoval na 3 díly.
{: .prompt-info }

## Požadavky
- [x] Výstup buildu (webové stránky) musí být možné poskytovat rozlišeně podle jazyka pomocí cest (např. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Aby se minimalizoval dodatečný čas a práce spojené s vícejazyčností, nesmí být nutné u každého zdrojového Markdown souboru ručně nastavovat ve YAML front matter tagy `lang` a `permalink`. Při buildu se musí jazyk automaticky rozpoznat podle lokální cesty, kde soubor leží (např. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}).
- [x] Hlavička každé stránky na webu musí splňovat Google SEO doporučení pro vícejazyčné vyhledávání: správný meta tag `Content-Language`, alternátní tagy `hreflang` a canonical odkaz.
- [x] Odkazy na všechny jazykové verze stránek musí být bez vynechání uvedeny v `sitemap.xml`{: .filepath}; samotný `sitemap.xml`{: .filepath} musí existovat bez duplicit pouze jednou v kořenové cestě.
- [x] Všechny funkce, které poskytuje [téma Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy), musí fungovat korektně i na stránkách jednotlivých jazyků; pokud ne, musí se upravit tak, aby fungovaly.
  - [x] Správná funkce „Recently Updated“, „Trending Tags“
  - [x] Žádné chyby v procesu buildu přes GitHub Actions
  - [x] Správná funkce vyhledávání příspěvků vpravo nahoře

## Nasazení pluginu Polyglot
Jekyll vícejazyčný blog nativně nepodporuje, takže pro splnění výše uvedených požadavků je potřeba použít externí plugin. Při hledání se ukázalo, že [Polyglot](https://github.com/untra/polyglot) se často používá pro vícejazyčné weby a většinu uvedených požadavků dokáže splnit, proto jsem zvolil právě tento plugin.

### Instalace pluginu
Používám Bundler, takže jsem do `Gemfile` přidal následující:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Poté stačí v terminálu spustit `bundle update` a instalace se dokončí automaticky.

Pokud Bundler nepoužíváte, můžete gem nainstalovat přímo příkazem `gem install jekyll-polyglot` a následně doplnit plugin do `_config.yml`{: .filepath} takto:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfigurace
Dále otevřete `_config.yml`{: .filepath} a přidejte:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: seznam podporovaných jazyků
- `default_lang`: výchozí fallback jazyk
- `exclude_from_localization`: regulární výraz (řetězce) kořenových cest souborů/složek, které se nemají lokalizovat
- `parallel_localization`: boolean určující, zda se má vícejazyčné zpracování během buildu paralelizovat
- `lang_from_path`: boolean; při nastavení na `true` není nutné explicitně uvádět `lang` ve YAML front matter. Pokud cesta k Markdown souboru obsahuje kód jazyka, Polyglot jej automaticky rozpozná a použije

> [Oficiální dokumentace protokolu Sitemap](https://www.sitemaps.org/protocol.html#location) uvádí následující:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Abyste to splnili, je potřeba zajistit, aby se `sitemap.xml`{: .filepath} nevytvářel pro každý jazyk, ale existoval pouze jednou v kořenovém adresáři. Proto je nutné jej přidat do seznamu `exclude_from_localization`, aby nevznikla situace jako v následujícím chybném příkladu.
>
> Chybný příklad (obsah každého souboru je shodný, jen se duplicitně generuje):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Aktualizace 12025.01.14.) Jakmile byl přijat [Pull Request, kterým jsem výše uvedené doplnil do README](https://github.com/untra/polyglot/pull/230), lze stejné doporučení najít i v [oficiální dokumentaci Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Nastavení `parallel_localization` na `true` má výhodu výrazného zkrácení času buildu, ale v červenci 12024 se při jeho zapnutí na tomto blogu objevoval bug: názvy odkazů v pravém postranním panelu („Recently Updated“ a „Trending Tags“) se nezpracovávaly správně a míchaly se s jinými jazyky. Funkce tehdy zřejmě nebyla dostatečně stabilní, takže pokud ji chcete použít, je potřeba předem otestovat, že vše funguje správně. Navíc [ani při použití Windows není tato funkce podporována, takže ji je nutné vypnout](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
>
> (Aktualizace 12025.09) Když jsem v létě 12025 funkci `parallel_localization` znovu otestoval na tomto blogu, fungovala bez problémů. Aktuálně ji mám tedy zapnutou a díky tomu se čas buildu výrazně zkrátil.
{: .prompt-warning }

Dále je také potřeba [v Jekyll 4.0 vypnout generování CSS sourcemaps](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility) takto:

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Poznámky při psaní příspěvků
Při psaní vícejazyčných příspěvků je potřeba dávat pozor na následující:

- Správné určení kódu jazyka: pomocí cesty k souboru (např. `/_posts/ko/example-post.md`{: .filepath}) nebo přes atribut `lang` ve YAML front matter (např. `lang: ko`) musíte uvést správný ISO kód jazyka. Řiďte se příklady v [dokumentaci Chrome pro vývojáře](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Poznámka: [dokumentace Chrome pro vývojáře](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) zapisuje regionální kódy ve formátu `pt_BR`, ale ve skutečnosti je potřeba používat `pt-BR` (pomlčka místo podtržítka), aby to později správně fungovalo při přidání alternátních tagů `hreflang` do HTML hlavičky.
{: .prompt-tip }

- Cesty a názvy souborů musí být konzistentní.

Podrobnosti najdete v README repozitáře [untra/polyglot na GitHubu](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Úprava HTML hlavičky a sitemap
Nyní je kvůli SEO potřeba do HTML hlavičky každé stránky vložit meta tag `Content-Language`, alternátní tagy `hreflang` a vhodně nastavit standardní URL (canonical URL).

### HTML hlavička
K listopadu 12024 (release 1.8.1, tehdy nejnovější) má Polyglot funkci, která při zavolání Liquid tagu {% raw %}`{% I18n_Headers %}`{% endraw %} automaticky provede uvedené úpravy v části hlavičky stránky.  
Tato funkce ale předpokládá, že stránka má explicitně nastavený atribut `permalink`; pokud tomu tak není, nefunguje korektně.

Proto jsem vzal [head.html z tématu Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) a doplnil do něj ručně následující. Postup jsem odvodil z [Polyglot oficiálního blogu – stránka SEO Recipes](https://polyglot.untra.io/seo/), ale upravil jsem to pro své prostředí a požadavky tak, aby se místo `page.permalink` používal atribut `page.url`.

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

(Doplnění 12025.07.29.) Téma Chirpy má také v základu plugin [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag). Ověřil jsem, že metadata `og:locale` a `og:url` generovaná automaticky Jekyll SEO Tag (pro [Open Graph](https://ogp.me/)) a také [standardní URL (canonical URL)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (`rel="canonical"` element `link`) jsou generována podle výchozího jazyka webu (`site.lang`, `site.default_lang`), a je tedy potřeba to dodatečně upravit.  
Proto jsem před {% raw %}`{{ seo_tags }}`{% endraw %} vložil následující blok.

{% raw %}
```liquid
(ukázka)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(vynecháno)...

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

  ...(dále) 
```
{: file='/_includes/head.html'}
{% endraw %}

> Podle [dokumentace Google](https://developers.google.com/search/docs/crawling-indexing/canonicalization) se stránky považují za duplicitní pouze tehdy, pokud mají stejné hlavní části obsahu (tj. je přeložený jen nadpis, zápatí a další nepodstatné texty, ale tělo je stejné). Pokud tedy – jako u tohoto blogu – poskytujete obsah článku v různých jazycích, jednotlivé jazykové verze se nepovažují za duplicity, ale za samostatné stránky, a proto je potřeba nastavovat různou canonical URL podle jazyka.  
> Například u korejské verze této stránky není canonical URL `"{{site.url}}{{page.url}}"`, ale `"{{site.url}}/ko{{page.url}}"`.
{: .prompt-tip }

### Sitemap
Pokud neurčíte vlastní šablonu, sitemap, který Jekyll automaticky vygeneruje při buildu, vícejazyčné stránky správně nepodporuje. Proto v kořenovém adresáři vytvořte soubor `sitemap.xml`{: .filepath} a vložte do něj následující:

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

## Další čtení
Pokračování v [Dílu 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
