---
title: So unterstützen Sie mehrere Sprachen in einem Jekyll-Blog mit Polyglot (1)
  - Anwendung des Polyglot-Plugins & Implementierung von hreflang alt-Tags, Sitemap
  und Sprachauswahl-Button
description: Dieser Beitrag beschreibt den Prozess der Implementierung mehrsprachiger
  Unterstützung in einem Jekyll-Blog basierend auf 'jekyll-theme-chirpy' unter Verwendung
  des Polyglot-Plugins. Als erster Teil der Serie behandelt dieser Beitrag die Anwendung
  des Polyglot-Plugins und die Änderung des HTML-Headers und der Sitemap.
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## Überblick
Vor etwa 4 Monaten, Anfang Juli 2024, habe ich das [Polyglot](https://github.com/untra/polyglot)-Plugin auf diesen Jekyll-basierten Blog angewendet, der über Github Pages gehostet wird, um mehrsprachige Unterstützung zu implementieren.
Diese Serie teilt den Prozess der Anwendung des Polyglot-Plugins auf das Chirpy-Theme, die aufgetretenen Bugs und deren Lösungen sowie Methoden zum Schreiben von HTML-Headern und sitemap.xml unter Berücksichtigung der SEO.
Die Serie besteht aus zwei Beiträgen, und dieser Beitrag ist der erste Teil der Serie.
- Teil 1: Anwendung des Polyglot-Plugins & Implementierung von hreflang alt-Tags, Sitemap und Sprachauswahl-Button (dieser Beitrag)
- Teil 2: [Fehlerbehebung bei Chirpy-Theme-Build-Fehlern und Suchfunktionsproblemen](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Anforderungen
- [x] Die gebauten Ergebnisse (Webseiten) sollten in sprachspezifischen Pfaden (z.B. `/posts/de/`{: .filepath}, `/posts/ja/`{: .filepath}) bereitgestellt werden können.
- [x] Um den zusätzlichen Zeit- und Arbeitsaufwand für die mehrsprachige Unterstützung zu minimieren, sollte die Sprache automatisch anhand des lokalen Pfads (z.B. `/_posts/de/`{: .filepath}, `/_posts/ja/`{: .filepath}) erkannt werden können, ohne dass 'lang' und 'permalink' Tags im YAML-Frontmatter der originalen Markdown-Dateien manuell angegeben werden müssen.
- [x] Der Header-Teil jeder Seite der Website sollte angemessene Content-Language Meta-Tags und hreflang-Alternativ-Tags enthalten, um die SEO-Richtlinien für die Google-Mehrsprachensuche zu erfüllen.
- [x] Die `sitemap.xml`{: .filepath} sollte alle Links zu den Seiten in jeder unterstützten Sprache ohne Auslassungen bereitstellen, und die `sitemap.xml`{: .filepath} selbst sollte nur einmal im Root-Verzeichnis ohne Duplikate existieren.
- [x] Alle vom [Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy) bereitgestellten Funktionen sollten auf jeder Sprachseite normal funktionieren, andernfalls müssen sie angepasst werden.
  - [x] 'Recently Updated', 'Trending Tags' Funktionen funktionieren normal
  - [x] Keine Fehler während des Build-Prozesses mit GitHub Actions
  - [x] Die Suchfunktion oben rechts im Blog funktioniert normal

## Anwendung des Polyglot-Plugins
Da Jekyll standardmäßig keine mehrsprachigen Blogs unterstützt, ist ein externes Plugin erforderlich, um einen mehrsprachigen Blog zu implementieren, der die obigen Anforderungen erfüllt. Nach einiger Recherche stellte sich heraus, dass [Polyglot](https://github.com/untra/polyglot) häufig für die Implementierung mehrsprachiger Websites verwendet wird und die meisten der obigen Anforderungen erfüllen kann, daher wurde dieses Plugin ausgewählt.

### Plugin-Installation
Da ich Bundler verwende, habe ich Folgendes zur `Gemfile` hinzugefügt:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Anschließend wird die Installation automatisch abgeschlossen, wenn Sie `bundle update` im Terminal ausführen.

Wenn Sie Bundler nicht verwenden, können Sie das Gem direkt mit dem Befehl `gem install jekyll-polyglot` im Terminal installieren und dann das Plugin wie folgt zu `_config.yml`{: .filepath} hinzufügen:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfiguration
Als Nächstes öffnen Sie die Datei `_config.yml`{: .filepath} und fügen Sie Folgendes hinzu:

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
- exclude_from_localization: Reguläre Ausdrücke für Datei-/Ordnerpfade im Stammverzeichnis, die von der Lokalisierung ausgeschlossen werden sollen
- parallel_localization: Boolescher Wert, der angibt, ob die mehrsprachige Verarbeitung während des Build-Prozesses parallelisiert werden soll
- lang_from_path: Boolescher Wert; wenn auf 'true' gesetzt, wird die Sprache automatisch aus dem Pfadstring der Markdown-Datei erkannt und verwendet, wenn dieser einen Sprachcode enthält, ohne dass das 'lang'-Attribut im YAML-Frontmatter der Beitragsdatei explizit angegeben werden muss

> Das [offizielle Dokument des Sitemap-Protokolls](https://www.sitemaps.org/protocol.html#location) besagt Folgendes:
>
>> "Der Standort einer Sitemap-Datei bestimmt die Menge der URLs, die in dieser Sitemap enthalten sein können. Eine Sitemap-Datei, die sich unter http://example.com/catalog/sitemap.xml befindet, kann alle URLs enthalten, die mit http://example.com/catalog/ beginnen, aber keine URLs, die mit http://example.com/images/ beginnen."
>
>> "Es wird dringend empfohlen, dass Sie Ihre Sitemap im Stammverzeichnis Ihres Webservers platzieren."
>
> Um dies einzuhalten, sollten Sie 'sitemap' zur Liste 'exclude_from_localization' hinzufügen, damit nicht mehrere `sitemap.xml`{: .filepath} Dateien mit identischem Inhalt für jede Sprache erstellt werden, sondern nur eine einzige im Stammverzeichnis existiert. Vermeiden Sie das folgende falsche Beispiel:
>
> Falsches Beispiel (der Inhalt jeder Datei ist für alle Sprachen identisch):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
{: .prompt-tip }

> Das Setzen von 'parallel_localization' auf 'true' kann die Build-Zeit erheblich verkürzen, aber Stand Juli 2024 gab es für diesen Blog einen Bug, bei dem die Linktitel in den Abschnitten 'Recently Updated' und 'Trending Tags' in der rechten Seitenleiste nicht korrekt verarbeitet wurden und mit anderen Sprachen vermischt waren, wenn diese Funktion aktiviert war. Es scheint noch nicht vollständig stabilisiert zu sein, daher sollten Sie vor der Anwendung auf Ihrer Website testen, ob es ordnungsgemäß funktioniert. Außerdem [muss diese Funktion deaktiviert werden, wenn Sie Windows verwenden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Außerdem [müssen Sie in Jekyll 4.0 die Generierung von CSS-Sourcemaps wie folgt deaktivieren](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Zu beachtende Punkte beim Schreiben von Beiträgen
Beim Schreiben mehrsprachiger Beiträge sind folgende Punkte zu beachten:
- Angemessene Sprachcode-Zuweisung: Der entsprechende ISO-Sprachcode sollte entweder über den Dateipfad (z.B. `/_posts/de/example-post.md`{: .filepath}) oder das 'lang'-Attribut im YAML-Frontmatter (z.B. `lang: de`) zugewiesen werden. Siehe Beispiele in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Beachten Sie jedoch, dass in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) Regionscodes im Format 'pt_BR' angegeben sind, aber tatsächlich sollte '_' durch '-' ersetzt werden, also 'pt-BR', damit später hreflang-Alternativ-Tags im HTML-Header korrekt funktionieren.

- Dateipfade und -namen sollten konsistent sein.

Weitere Details finden Sie in der README des GitHub [untra/polyglot Repositories](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Änderung des HTML-Headers und der Sitemap
Nun müssen wir für SEO-Zwecke Content-Language Meta-Tags und hreflang-Alternativ-Tags in den HTML-Header jeder Seite des Blogs einfügen.

### HTML-Header
In der neuesten Version 1.8.1 (Stand November 2024) bietet Polyglot eine Funktion, die diese Aufgabe automatisch erledigt, wenn der Liquid-Tag {% raw %}`{% I18n_Headers %}`{% endraw %} im Header-Bereich der Seite aufgerufen wird.
Dies setzt jedoch voraus, dass das 'permalink'-Attribut-Tag für die Seite explizit angegeben wurde, andernfalls funktioniert es nicht ordnungsgemäß.

Daher habe ich [head.html aus dem Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) übernommen und den folgenden Inhalt direkt hinzugefügt.
Ich habe mich an der [SEO Recipes-Seite des offiziellen Polyglot-Blogs](https://polyglot.untra.io/seo/) orientiert, aber modifiziert, um das `page.url`-Attribut zu verwenden, wenn `page.permalink` nicht vorhanden ist.
Außerdem habe ich unter Bezugnahme auf die [offizielle Google Search Central-Dokumentation](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault) den hreflang-Attributwert für die Standardsprachseite der Website auf `x-default` anstelle von `site.default_lang` gesetzt, damit dieser Seitenlink als Fallback erkannt wird, wenn die bevorzugte Sprache des Besuchers nicht in der Liste der von der Website unterstützten Sprachen enthalten ist oder wenn die bevorzugte Sprache des Besuchers nicht erkannt werden kann.

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
Da die von Jekyll beim Build automatisch generierte Sitemap mehrsprachige Seiten nicht korrekt unterstützt, erstellen Sie eine `sitemap.xml`{: .filepath} Datei im Stammverzeichnis und geben Sie den folgenden Inhalt ein:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- sehr oberflächliche Prüfung, ob die Seite in der Ausschlussliste enthalten ist - das bedeutet, dass ausgeschlossene Seiten überhaupt nicht in der Sitemap erscheinen, schreiben Sie bei Bedarf Ausnahmen -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- Annahme, dass die Seite nicht in die Sitemap aufgenommen wird, wenn kein Layout zugewiesen ist, Sie möchten dies möglicherweise ändern -->{% endcomment %}
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
Erstellen Sie eine Datei `_includes/lang-selector.html`{: .filepath} und geben Sie den folgenden Inhalt ein:

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

Fügen Sie dann die folgenden drei Zeilen zum "sidebar-bottom" Klassenabschnitt in [_includes/sidebar.html des Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) hinzu, damit Jekyll den Inhalt von `_includes/lang-selector.html`{: .filepath} beim Seitenbau lädt:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
