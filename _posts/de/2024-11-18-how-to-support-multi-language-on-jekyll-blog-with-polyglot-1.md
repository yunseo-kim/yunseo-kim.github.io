---
title: "Mehrsprachige Unterstützung für einen Jekyll-Blog mit Polyglot (1) - Anwendung des Polyglot-Plugins & Anpassung von HTML-Header und Sitemap"
description: "Eine Anleitung zur Implementierung mehrsprachiger Unterstützung in einem Jekyll-Blog mit dem 'jekyll-theme-chirpy'-Theme durch das Polyglot-Plugin. Dieser erste Teil der Serie behandelt die Anwendung des Polyglot-Plugins und die Anpassung des HTML-Headers und der Sitemap."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## Übersicht
Anfang Juli 12024, habe ich meinem auf Jekyll basierenden und über Github Pages gehosteten Blog mit dem [Polyglot](https://github.com/untra/polyglot)-Plugin eine mehrsprachige Unterstützung hinzugefügt.
Diese Serie teilt den Prozess der Behebung von Fehlern, die bei der Anwendung des Polyglot-Plugins auf das Chirpy-Theme auftraten, sowie Anleitungen zur Erstellung von HTML-Headern und sitemap.xml unter Berücksichtigung von SEO.
Die Serie besteht aus drei Beiträgen, und dieser hier ist der erste Teil.
- Teil 1: Anwendung des Polyglot-Plugins & Anpassung von HTML-Header und Sitemap (Dieser Beitrag)
- Teil 2: [Implementierung des Sprachauswahl-Buttons & Lokalisierung der Layout-Sprache](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- Teil 3: [Fehlerbehebung bei Build-Fehlern und Suchfunktionsproblemen im Chirpy-Theme](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> Ursprünglich bestand die Serie aus zwei Teilen, wurde aber nach mehreren inhaltlichen Erweiterungen, die den Umfang erheblich vergrößerten, auf drei Teile umstrukturiert.
{: .prompt-info }

## Anforderungen
- [x] Die erstellten Ergebnisse (Webseiten) müssen nach Sprachen in separaten Pfaden (z.B. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}) bereitgestellt werden können.
- [x] Um den zusätzlichen Zeit- und Arbeitsaufwand für die Mehrsprachigkeit zu minimieren, muss das System die Sprache automatisch anhand des lokalen Dateipfads (z.B. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) erkennen, ohne dass für jede Markdown-Datei manuell 'lang'- und 'permalink'-Tags im YAML-Frontmatter festgelegt werden müssen.
- [x] Der Header jeder Seite der Website muss die Google-SEO-Richtlinien für die mehrsprachige Suche erfüllen, indem er entsprechende Content-Language-Meta-Tags, hreflang-Alternate-Tags und Canonical-Links enthält.
- [x] Alle Sprachversionen der Seiten müssen lückenlos in einer `sitemap.xml`{: .filepath}-Datei bereitgestellt werden. Diese `sitemap.xml`{: .filepath} muss ohne Duplikate nur im Stammverzeichnis vorhanden sein.
- [x] Alle vom [Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy) bereitgestellten Funktionen müssen auf jeder Sprachseite korrekt funktionieren. Andernfalls müssen sie entsprechend angepasst werden.
  - [x] Die Funktionen 'Kürzlich aktualisiert' und 'Trend-Tags' müssen normal funktionieren.
  - [x] Der Build-Prozess mit GitHub Actions muss fehlerfrei ablaufen.
  - [x] Die Beitragssuche oben rechts im Blog muss korrekt funktionieren.

## Anwendung des Polyglot-Plugins
Da Jekyll von Haus aus keine mehrsprachigen Blogs unterstützt, ist die Verwendung eines externen Plugins erforderlich, um die oben genannten Anforderungen zu erfüllen. Nach einiger Recherche habe ich mich für [Polyglot](https://github.com/untra/polyglot) entschieden, da es für die Erstellung mehrsprachiger Websites weit verbreitet ist und die meisten meiner Anforderungen erfüllt.

### Plugin-Installation
Da ich Bundler verwende, habe ich Folgendes zu meiner `Gemfile` hinzugefügt.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Anschließend wird es durch Ausführen von `bundle update` im Terminal automatisch installiert.

Wenn Sie Bundler nicht verwenden, können Sie das Gem auch direkt mit dem Befehl `gem install jekyll-polyglot` im Terminal installieren und das Plugin dann wie folgt in Ihrer `_config.yml`{: .filepath} hinzufügen.

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfiguration
Öffnen Sie als Nächstes die Datei `_config.yml`{: .filepath} und fügen Sie den folgenden Inhalt hinzu.

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: Liste der zu unterstützenden Sprachen
- `default_lang`: Standard-Fallback-Sprache
- `exclude_from_localization`: Gibt einen regulären Ausdruck für Pfadzeichenfolgen von Stammdateien/-ordnern an, die von der Lokalisierung ausgeschlossen werden sollen
- `parallel_localization`: Ein boolescher Wert, der angibt, ob die mehrsprachige Verarbeitung während des Build-Prozesses parallelisiert werden soll
- `lang_from_path`: Ein boolescher Wert. Bei 'true' wird die Sprache automatisch aus dem Pfad der Markdown-Datei erkannt, wenn die Pfadzeichenfolge einen Sprachcode enthält, auch wenn das 'lang'-Attribut nicht explizit im YAML-Frontmatter angegeben ist.

> Die [offizielle Dokumentation des Sitemap-Protokolls](https://www.sitemaps.org/protocol.html#location) besagt Folgendes:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Um dies zu befolgen, muss die `sitemap.xml`{: .filepath}-Datei zur Liste 'exclude_from_localization' hinzugefügt werden, damit nicht für jede Sprache eine identische `sitemap.xml`{: .filepath}-Datei erstellt wird und nur eine einzige im Stammverzeichnis existiert. Dies verhindert das folgende falsche Beispiel.
>
> Falsches Beispiel (der Inhalt jeder Datei ist identisch):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Update 14.01.12025) Ein [Pull Request, der die README um die oben genannten Inhalte ergänzt](https://github.com/untra/polyglot/pull/230), wurde angenommen. Daher ist diese Anleitung nun auch in der [offiziellen Polyglot-Dokumentation](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation) zu finden.
{: .prompt-tip }

> Das Setzen von 'parallel_localization' auf 'true' hat den Vorteil, die Build-Zeit erheblich zu verkürzen. Als ich diese Funktion jedoch im Juli 12024 für meinen Blog aktivierte, trat ein Fehler auf, bei dem die Link-Titel in den Abschnitten 'Kürzlich aktualisiert' und 'Trend-Tags' in der rechten Seitenleiste nicht korrekt verarbeitet wurden und mit anderen Sprachen vermischt waren. Es scheint, dass die Funktion noch nicht stabil ist, daher ist es notwendig, vor der Anwendung auf Ihrer Website zu testen, ob sie ordnungsgemäß funktioniert. Außerdem [wird diese Funktion unter Windows nicht unterstützt und sollte daher deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
>
> (Update 09.12025) Im Sommer 12025 habe ich die Funktion 'parallel_localization' auf Basis dieses Blogs erneut getestet; sie funktionierte ohne Probleme einwandfrei. Daher ist sie derzeit aktiviert, was die Build-Zeit deutlich verkürzt hat.
{: .prompt-warning }

Außerdem [muss bei Jekyll 4.0 die Erstellung von CSS-Sourcemaps wie folgt deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Hinweise zum Verfassen von Beiträgen
Beim Verfassen mehrsprachiger Beiträge ist Folgendes zu beachten:
- Angemessenen Sprachcode festlegen: Sie müssen einen geeigneten ISO-Sprachcode entweder über den Dateipfad (z.B. `/_posts/ko/example-post.md`{: .filepath}) oder das 'lang'-Attribut im YAML-Frontmatter (z.B. `lang: ko`) festlegen. Beispiele finden Sie in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Obwohl die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) Regionalcodes im Format 'pt_BR' angibt, muss in der Praxis 'pt-BR' mit einem Bindestrich anstelle eines Unterstrichs verwendet werden, damit die hreflang-Alternate-Tags später im HTML-Header korrekt funktionieren.
{: .prompt-tip }

- Dateipfade und -namen müssen konsistent sein.

Weitere Details finden Sie im [README des untra/polyglot-Repositorys auf GitHub](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Anpassung von HTML-Header und Sitemap
Nun müssen wir für SEO-Zwecke den HTML-Header jeder Seite des Blogs um Content-Language-Meta-Tags und hreflang-Alternate-Tags erweitern und die kanonische URL (canonical URL) korrekt festlegen.

### HTML-Header
Zum Zeitpunkt des Releases 1.8.1 im November 12024 bietet Polyglot eine Funktion, die diese Aufgaben automatisch erledigt, wenn der Liquid-Tag {% raw %}`{% I18n_Headers %}`{% endraw %} im Header-Bereich der Seite aufgerufen wird.
Dies setzt jedoch voraus, dass für die betreffende Seite ein 'permalink'-Attribut explizit angegeben wurde, andernfalls funktioniert es nicht korrekt.

Daher habe ich die [head.html des Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) übernommen und den folgenden Inhalt manuell hinzugefügt.
Ich habe mich an der [SEO-Recipes-Seite des offiziellen Polyglot-Blogs](https://polyglot.untra.io/seo/) orientiert, aber die Verwendung von `page.url` anstelle von `page.permalink` an meine Nutzungsumgebung und Anforderungen angepasst.

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

(Hinzugefügt am 29.07.12025) Des Weiteren ist im Chirpy-Theme standardmäßig das [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag)-Plugin integriert. Ich habe festgestellt, dass die von Jekyll SEO Tag automatisch generierten [Open Graph](https://ogp.me/)-Metadaten-Attribute `og:locale` und `og:url` sowie die [kanonische URL (canonical URL)](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)(das `link`-Element mit `rel="canonical"`) auf der Standardsprache der Website (`site.lang`, `site.default_lang`) basieren und daher eine zusätzliche Verarbeitung erfordern.
Daher habe ich vor {% raw %}`{{ seo_tags }}`{% endraw %} den folgenden Code hinzugefügt.

{% raw %}
```liquid
(vorheriger Teil)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(mittlerer Teil)...

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

  ...(nachfolgender Teil)
```
{: file='/_includes/head.html'}
{% endraw %}

> Laut der [Google-Entwicklerdokumentation](https://developers.google.com/search/docs/crawling-indexing/canonicalization) werden mehrere Sprachversionen einer Seite nur dann als Duplikate betrachtet, wenn die Sprache des Hauptinhalts dieselbe ist, d.h. nur Kopfzeile, Fußzeile und andere unwichtige Texte übersetzt sind, der Haupttext aber identisch ist. Da dieser Blog den Haupttext in mehreren Sprachen anbietet, werden die einzelnen Sprachversionen als unabhängige Seiten und nicht als Duplikate betrachtet. Daher muss für jede Sprache eine andere kanonische URL angegeben werden.
> Beispielsweise ist die kanonische URL für die deutsche Version dieser Seite nicht „{{site.url}}{{page.url}}“, sondern „{{site.url}}/de{{page.url}}“.
{: .prompt-tip }

### sitemap
Wenn keine Vorlage angegeben wird, unterstützt die von Jekyll beim Build automatisch generierte Sitemap mehrsprachige Seiten nicht korrekt. Erstellen Sie daher eine `sitemap.xml`{: .filepath}-Datei im Stammverzeichnis und geben Sie den folgenden Inhalt ein.

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

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
