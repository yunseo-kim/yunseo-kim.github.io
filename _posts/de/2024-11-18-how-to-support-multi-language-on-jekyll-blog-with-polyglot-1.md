---
title: Wie man mit Polyglot mehrsprachige Unterstützung für einen Jekyll-Blog implementiert (1) - Anwendung des Polyglot-Plugins & Implementierung von hreflang alt-Tags, Sitemap und Sprachauswahl-Button
description: >-
  Dieser Beitrag beschreibt den Prozess der Implementierung mehrsprachiger Unterstützung für einen Jekyll-Blog basierend auf dem 'jekyll-theme-chirpy' Theme unter Verwendung des Polyglot-Plugins.
  Als erster Teil der Serie behandelt dieser Post die Anwendung des Polyglot-Plugins und die Modifikation des HTML-Headers und der Sitemap.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
---
## Überblick
Vor etwa 4 Monaten, Anfang Juli 2024, habe ich meinem Jekyll-basierten Blog, der über Github Pages gehostet wird, mehrsprachige Unterstützung hinzugefügt, indem ich das [Polyglot](https://github.com/untra/polyglot)-Plugin implementiert habe.
Diese Serie teilt die Erfahrungen mit Bugs, die während der Anwendung des Polyglot-Plugins auf das Chirpy-Theme auftraten, deren Lösungen, sowie Methoden zum Schreiben von HTML-Headern und sitemap.xml unter Berücksichtigung der SEO.
Die Serie besteht aus zwei Beiträgen, und dieser Beitrag ist der erste Teil der Serie.
- Teil 1: Anwendung des Polyglot-Plugins & Implementierung von hreflang alt-Tags, Sitemap und Sprachauswahl-Button (dieser Beitrag)
- Teil 2: [Fehlerbehebung bei Build-Fehlern des Chirpy-Themes und Suchfunktionsproblemen](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Anforderungen
- [x] Das gebaute Ergebnis (Webseite) sollte in sprachspezifischen Pfaden (z.B. `/posts/de/`{: .filepath}, `/posts/ja/`{: .filepath}) bereitgestellt werden können.
- [x] Um den zusätzlichen Zeit- und Arbeitsaufwand für die mehrsprachige Unterstützung zu minimieren, sollte die Sprache beim Build automatisch anhand des lokalen Pfads der originalen Markdown-Datei (z.B. `/_posts/de/`{: .filepath}, `/_posts/ja/`{: .filepath}) erkannt werden, ohne dass 'lang' und 'permalink' Tags im YAML-Frontmatter der Markdown-Datei manuell spezifiziert werden müssen.
- [x] Der Header-Teil jeder Seite der Website sollte angemessene Content-Language Meta-Tags und hreflang Alternativ-Tags enthalten, um die SEO-Richtlinien für die Google-Mehrsprachensuche zu erfüllen.
- [x] Die `sitemap.xml` sollte alle Links zu den mehrsprachigen Seiten der Website ohne Auslassungen bereitstellen, und die `sitemap.xml` selbst sollte nur einmal im Root-Verzeichnis existieren, ohne Duplikate.
- [x] Alle vom [Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy) bereitgestellten Funktionen sollten auf jeder Sprachseite normal funktionieren, andernfalls müssen sie entsprechend angepasst werden.
  - [x] Normale Funktion von 'Recently Updated' und 'Trending Tags'
  - [x] Keine Fehler während des Build-Prozesses mit GitHub Actions
  - [x] Normale Funktion der Beitragssuche in der oberen rechten Ecke des Blogs

## Anwendung des Polyglot-Plugins
Da Jekyll standardmäßig keine mehrsprachigen Blogs unterstützt, ist die Verwendung eines externen Plugins erforderlich, um einen mehrsprachigen Blog zu implementieren, der die oben genannten Anforderungen erfüllt. Nach einiger Recherche stellte sich heraus, dass [Polyglot](https://github.com/untra/polyglot) häufig für die Implementierung mehrsprachiger Websites verwendet wird und die meisten der oben genannten Anforderungen erfüllen kann, weshalb ich mich für dieses Plugin entschieden habe.

### Plugin-Installation
Da ich Bundler verwende, habe ich Folgendes zur `Gemfile` hinzugefügt:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Anschließend wird die Installation automatisch abgeschlossen, wenn man `bundle update` im Terminal ausführt.

Wenn man Bundler nicht verwendet, kann man das Gem auch direkt mit dem Befehl `gem install jekyll-polyglot` im Terminal installieren und dann das Plugin wie folgt zu `_config.yml` hinzufügen:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfiguration
Als Nächstes öffnet man die Datei `_config.yml` und fügt Folgendes hinzu:

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Liste der zu unterstützenden Sprachen
- default_lang: Standard-Fallback-Sprache
- exclude_from_localization: Reguläre Ausdrücke für Root-Datei-/Ordnerpfade, die von der Lokalisierung ausgeschlossen werden sollen
- parallel_localization: Boolescher Wert, der angibt, ob die mehrsprachige Verarbeitung während des Build-Prozesses parallelisiert werden soll
- lang_from_path: Boolescher Wert; wenn auf 'true' gesetzt, wird die Sprache automatisch aus dem Pfadstring der Markdown-Datei erkannt, wenn dieser einen Sprachcode enthält, ohne dass das 'lang'-Attribut im YAML-Frontmatter der Markdown-Datei explizit angegeben werden muss

> Das [offizielle Dokument des Sitemap-Protokolls](https://www.sitemaps.org/protocol.html#location) besagt Folgendes:
>
>> "Der Standort einer Sitemap-Datei bestimmt die Menge der URLs, die in dieser Sitemap enthalten sein können. Eine Sitemap-Datei, die sich unter http://example.com/catalog/sitemap.xml befindet, kann alle URLs enthalten, die mit http://example.com/catalog/ beginnen, aber keine URLs, die mit http://example.com/images/ beginnen."
>
>> "Es wird dringend empfohlen, Ihre Sitemap im Stammverzeichnis Ihres Webservers zu platzieren."
>
> Um dies einzuhalten, sollte 'sitemap' zur Liste 'exclude_from_localization' hinzugefügt werden, damit nicht für jede Sprache eine separate `sitemap.xml`-Datei mit identischem Inhalt erstellt wird, sondern nur eine einzige im Stammverzeichnis existiert. So wird vermieden, dass es wie im folgenden falschen Beispiel aussieht.
>
> Falsches Beispiel (der Inhalt jeder Datei ist für alle Sprachen identisch):
> - /sitemap.xml
> - /ko/sitemap.xml
> - /es/sitemap.xml
> - /pt-BR/sitemap.xml
> - /ja/sitemap.xml
> - /fr/sitemap.xml
> - /de/sitemap.xml
{: .prompt-tip }

> Wenn 'parallel_localization' auf 'true' gesetzt wird, kann die Build-Zeit erheblich verkürzt werden. Allerdings gab es zum Stand Juli 2024 für diesen Blog einen Bug, bei dem die Linktitel im 'Recently Updated' und 'Trending Tags' Bereich der rechten Seitenleiste nicht korrekt verarbeitet wurden und sich mit anderen Sprachen vermischten, wenn diese Funktion aktiviert war. Es scheint noch nicht vollständig stabilisiert zu sein, daher sollte man vor der Anwendung auf der eigenen Seite testen, ob es ordnungsgemäß funktioniert. Außerdem [wird diese Funktion unter Windows nicht unterstützt und sollte daher deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Zusätzlich [muss in Jekyll 4.0 die Generierung von CSS-Sourcemaps wie folgt deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Zu beachtende Punkte beim Verfassen von Beiträgen
Beim Verfassen mehrsprachiger Beiträge sollte man Folgendes beachten:
- Korrekte Sprachcode-Zuweisung: Der entsprechende ISO-Sprachcode sollte entweder über den Dateipfad (z.B. `/_posts/de/example-post.md`{: .filepath}) oder über das 'lang'-Attribut im YAML-Frontmatter (z.B. `lang: de`) zugewiesen werden. Beispiele finden Sie in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Beachten Sie jedoch, dass in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) Regionscodes im Format 'pt_BR' angegeben werden, aber tatsächlich sollte '_' durch '-' ersetzt werden, also 'pt-BR', damit später die hreflang-Alternativ-Tags im HTML-Header korrekt funktionieren.

- Dateipfade und -namen sollten konsistent sein.

Weitere Details finden Sie in der [README des GitHub untra/polyglot Repositories](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modifikation des HTML-Headers und der Sitemap
Nun müssen für SEO-Zwecke Content-Language Meta-Tags und hreflang Alternativ-Tags in den HTML-Header jeder Seite des Blogs eingefügt werden.

### HTML-Header
In der neuesten Version 1.8.1 (Stand November 2024) bietet Polyglot eine Funktion, die diese Aufgabe automatisch erledigt, wenn der Liquid-Tag {% raw %}`{% I18n_Headers %}`{% endraw %} im Header-Bereich der Seite aufgerufen wird.
Dies setzt jedoch voraus, dass für die betreffende Seite ein 'permalink'-Attribut-Tag explizit angegeben wurde, andernfalls funktioniert es nicht ordnungsgemäß.

Daher habe ich [head.html aus dem Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) übernommen und den Inhalt wie folgt direkt ergänzt.
Ich habe mich an der [SEO Recipes Seite des offiziellen Polyglot-Blogs](https://polyglot.untra.io/seo/) orientiert, aber modifiziert, um `page.url` anstelle von `page.permalink` zu verwenden, wenn `page.permalink` nicht vorhanden ist.
Außerdem habe ich unter Bezugnahme auf die [offizielle Google Search Central Dokumentation](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault) `x-default` anstelle von `site.default_lang` als hreflang-Attributwert für die Standardsprachseite der Website festgelegt, damit dieser Seitenlink als Fallback erkannt wird, wenn die bevorzugte Sprache des Besuchers nicht in der Liste der unterstützten Sprachen der Website enthalten ist oder wenn die bevorzugte Sprache des Besuchers nicht erkannt werden kann.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="x-default" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### Sitemap
Da die von Jekyll beim Build automatisch generierte Sitemap mehrsprachige Seiten nicht korrekt unterstützt, erstellen Sie eine `sitemap.xml`-Datei im Root-Verzeichnis und fügen Sie folgenden Inhalt ein:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- sehr einfache Überprüfung, ob die Seite in der Ausschlussliste enthalten ist - das bedeutet, dass ausgeschlossene Seiten überhaupt nicht in der Sitemap erscheinen, schreiben Sie bei Bedarf Ausnahmen -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- Annahme: Wenn kein Layout zugewiesen ist, dann die Seite nicht in die Sitemap aufnehmen, Sie möchten dies möglicherweise ändern -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- Dies durchläuft alle Site-Sammlungen einschließlich Beiträge -->{% endcomment %}
    {% for collection in site.collections %}
        {% for node in site[collection.label] %}
            <url>
                <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
            </url>
        {% endfor %}
    {% endfor %}

{% endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## Hinzufügen eines Sprachauswahl-Buttons zur Seitenleiste
Erstellen Sie eine Datei `_includes/lang-selector.html` und fügen Sie folgenden Inhalt ein:

{% raw %}
```liquid
<p>
{%- for lang in site.languages -%}
  {%- if lang == site.default_lang -%}
<a ferh="{{ page.url }}" style="display:inline-block; white-space:nowrap;">
    {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- else -%}
<a href="/{{ lang }}{{ page.url }}" style="display:inline-block; white-space:nowrap;">
  {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- endif -%}
{%- endfor -%}
</p>
```
{: file='_includes/lang-selector.html'}
{% endraw %}

Fügen Sie dann die folgenden drei Zeilen zum "sidebar-bottom" Klassenbereich in [_includes/sidebar.html des Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) hinzu, damit Jekyll den Inhalt von `_includes/lang-selector.html` beim Seitenbau lädt:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
