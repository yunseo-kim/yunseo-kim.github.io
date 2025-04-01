---
title: Wie man mit Polyglot mehrsprachige Unterstützung in einem Jekyll-Blog implementiert (1) - Anwendung des Polyglot-Plugins & Implementierung von hreflang-Alt-Tags, Sitemap und Sprachauswahl-Button
description: 'Dieser Beitrag stellt vor, wie ein mehrsprachiger Blog mit dem Polyglot-Plugin auf einem Jekyll-Blog basierend auf "jekyll-theme-chirpy" implementiert wurde. Dies ist der erste Teil der Serie und behandelt die Anwendung des Polyglot-Plugins sowie die Anpassung des HTML-Headers und der Sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## Übersicht
Vor etwa 4 Monaten, Anfang Juli 12024 im [Holozän-Kalender](https://en.wikipedia.org/wiki/Holocene_calendar), habe ich das [Polyglot](https://github.com/untra/polyglot)-Plugin auf meinem Jekyll-basierten Blog, der über GitHub Pages gehostet wird, implementiert, um mehrsprachige Unterstützung hinzuzufügen.
Diese Serie teilt den Prozess der Implementierung des Polyglot-Plugins im Chirpy-Theme, die dabei aufgetretenen Bugs und deren Lösungen sowie die Erstellung von HTML-Headern und sitemap.xml unter Berücksichtigung von SEO.
Die Serie besteht aus zwei Artikeln, und dieser Artikel ist der erste Teil.
- Teil 1: Anwendung des Polyglot-Plugins & Implementierung von hreflang-Alt-Tags, Sitemap und Sprachauswahl-Button (dieser Artikel)
- Teil 2: [Fehlerbehebung bei Build-Fehlern und Suchfunktionsproblemen im Chirpy-Theme](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Anforderungen
- [x] Die gebauten Ergebnisse (Webseiten) sollten nach Sprachpfaden (z.B. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}) getrennt bereitgestellt werden.
- [x] Um den zusätzlichen Zeit- und Arbeitsaufwand für die mehrsprachige Unterstützung zu minimieren, sollte das System die Sprache automatisch anhand des lokalen Pfads (z.B. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) erkennen können, ohne dass 'lang' und 'permalink' Tags im YAML-Frontmatter jeder Markdown-Datei manuell angegeben werden müssen.
- [x] Der Header-Bereich jeder Seite sollte geeignete Content-Language-Meta-Tags und hreflang-Alternativ-Tags enthalten, um die SEO-Richtlinien für die Google-Mehrsprachensuche zu erfüllen.
- [x] Alle Links zu mehrsprachigen Seiten sollten vollständig in der `sitemap.xml`{: .filepath} aufgeführt sein, und die `sitemap.xml`{: .filepath} selbst sollte nur einmal im Root-Verzeichnis existieren, ohne Duplikate.
- [x] Alle Funktionen des [Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy) sollten auf jeder Sprachseite normal funktionieren, andernfalls müssen sie entsprechend angepasst werden.
  - [x] 'Recently Updated', 'Trending Tags' Funktionen arbeiten normal
  - [x] Keine Fehler während des Build-Prozesses mit GitHub Actions
  - [x] Die Suchfunktion in der oberen rechten Ecke des Blogs funktioniert normal

## Anwendung des Polyglot-Plugins
Da Jekyll keine mehrsprachigen Blogs standardmäßig unterstützt, müssen wir ein externes Plugin verwenden, um die oben genannten Anforderungen zu erfüllen. Nach einiger Recherche stellte ich fest, dass [Polyglot](https://github.com/untra/polyglot) häufig für mehrsprachige Websites verwendet wird und die meisten unserer Anforderungen erfüllen kann, daher habe ich dieses Plugin gewählt.

### Plugin-Installation
Da ich Bundler verwende, habe ich Folgendes zu meiner `Gemfile` hinzugefügt:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Danach führt man im Terminal `bundle update` aus, und die Installation wird automatisch abgeschlossen.

Wenn Sie Bundler nicht verwenden, können Sie das Gem direkt mit dem Befehl `gem install jekyll-polyglot` im Terminal installieren und dann das Plugin in `_config.yml`{: .filepath} wie folgt hinzufügen:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfiguration
Als nächstes öffnen Sie die Datei `_config.yml`{: .filepath} und fügen Folgendes hinzu:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Liste der unterstützten Sprachen
- default_lang: Standard-Fallback-Sprache
- exclude_from_localization: Regex-Strings für Root-Dateien/Ordnerpfade, die von der Lokalisierung ausgeschlossen werden sollen
- parallel_localization: Boolean-Wert, der angibt, ob die mehrsprachige Verarbeitung während des Build-Prozesses parallelisiert werden soll
- lang_from_path: Boolean-Wert, der bei 'true' die Sprache automatisch aus dem Dateipfad erkennt, ohne dass ein 'lang'-Attribut im YAML-Frontmatter angegeben werden muss

> Das [offizielle Dokument zum Sitemap-Protokoll](https://www.sitemaps.org/protocol.html#location) besagt:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Um dies einzuhalten, sollte die `sitemap.xml`{: .filepath} Datei nicht für jede Sprache erstellt werden, sondern nur einmal im Root-Verzeichnis existieren. Fügen Sie sie daher zur 'exclude_from_localization'-Liste hinzu, um zu vermeiden, dass sie wie im folgenden falschen Beispiel mehrfach erstellt wird.
>
> Falsches Beispiel (alle Dateien haben denselben Inhalt):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Update 14.01.12025) [Ein Pull Request mit den oben genannten Informationen](https://github.com/untra/polyglot/pull/230) wurde akzeptiert, und diese Anleitung ist jetzt auch in der [offiziellen Polyglot-Dokumentation](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation) verfügbar.
{: .prompt-tip }

> Wenn Sie 'parallel_localization' auf 'true' setzen, kann die Build-Zeit erheblich verkürzt werden, aber Stand Juli 12024 gab es einen Bug, bei dem die Titel der Links in den Bereichen 'Recently Updated' und 'Trending Tags' in der rechten Seitenleiste nicht korrekt verarbeitet wurden und mit anderen Sprachen vermischt wurden. Es scheint noch nicht vollständig stabilisiert zu sein, daher sollten Sie vor der Anwendung auf Ihrer Website testen, ob es ordnungsgemäß funktioniert. Außerdem [wird diese Funktion unter Windows nicht unterstützt und sollte deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Außerdem müssen Sie [in Jekyll 4.0 die Generierung von CSS-Sourcemaps wie folgt deaktivieren](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Hinweise zum Schreiben von Beiträgen
Beim Schreiben mehrsprachiger Beiträge sollten Sie Folgendes beachten:
- Korrekte Sprachcode-Angabe: Verwenden Sie entweder den Dateipfad (z.B. `/_posts/ko/example-post.md`{: .filepath}) oder das 'lang'-Attribut im YAML-Frontmatter (z.B. `lang: ko`), um den entsprechenden ISO-Sprachcode anzugeben. Siehe Beispiele in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Obwohl die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) Regionscodes im Format 'pt_BR' angibt, sollten Sie tatsächlich '-' statt '_' verwenden (also 'pt-BR'), damit die hreflang-Alternativ-Tags im HTML-Header später korrekt funktionieren.

- Dateipfade und -namen sollten konsistent sein.

Weitere Details finden Sie in der [README des GitHub untra/polyglot-Repositories](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Anpassung von HTML-Header und Sitemap
Jetzt müssen wir für SEO-Zwecke Content-Language-Meta-Tags und hreflang-Alternativ-Tags in den HTML-Header jeder Seite einfügen.

### HTML-Header
In der neuesten Version 1.8.1 (Stand November 12024) bietet Polyglot die Funktion, diese Aufgabe automatisch auszuführen, wenn der Liquid-Tag {% raw %}`{% I18n_Headers %}`{% endraw %} im Seitenkopf aufgerufen wird.
Diese Funktion setzt jedoch voraus, dass die Seite ein 'permalink'-Attribut hat, und funktioniert andernfalls nicht korrekt.

Daher habe ich [head.html aus dem Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) übernommen und den folgenden Inhalt direkt hinzugefügt.
Ich habe mich an der [SEO Recipes-Seite des offiziellen Polyglot-Blogs](https://polyglot.untra.io/seo/) orientiert, aber die Implementierung so angepasst, dass sie `page.url` verwendet, wenn `page.permalink` nicht verfügbar ist.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### Sitemap
Da die von Jekyll automatisch generierte Sitemap mehrsprachige Seiten nicht korrekt unterstützt, erstellen wir eine `sitemap.xml`{: .filepath} Datei im Root-Verzeichnis mit folgendem Inhalt:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- This loops through all site collections including posts -->{% endcomment %}
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
(Update 05.02.12025) Der Sprachauswahl-Button wurde zu einem Dropdown-Menü verbessert.  
Erstellen Sie eine Datei `_includes/lang-selector.html`{: .filepath} mit folgendem Inhalt:

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
{: file='_includes/lang-selector.html'}
{% endraw %}

Erstellen Sie außerdem eine Datei `assets/css/lang-selector.css`{: .filepath} mit folgendem Inhalt:

```css
/**
 * Sprachauswahl-Stil
 * 
 * Definiert den Stil für das Sprachauswahl-Dropdown in der Seitenleiste.
 * Unterstützt den Dark Mode des Themes und ist für mobile Umgebungen optimiert.
 */

/* Sprachauswahl-Container */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Dropdown-Container */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Auswahlelement */
.lang-select {
    /* Grundstil */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Schrift und Farbe */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Form und Interaktion */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Pfeil-Icon hinzufügen */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Flaggen-Emoji-Stil */
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

/* Hover-Zustand */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* Fokus-Zustand */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Firefox-Browser-Anpassung */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* IE-Browser-Anpassung */
.lang-select::-ms-expand {
    display: none;
}

/* Dark-Mode-Anpassung */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Mobile Optimierung */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Größerer Touch-Bereich */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Breiterer Auswahlbereich auf Mobilgeräten */
    }
}
```
{: file='assets/css/lang-selector.css'}

Fügen Sie dann in [`_includes/sidebar.html`{: .filepath} des Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) direkt vor der "sidebar-bottom"-Klasse die folgenden drei Zeilen hinzu, damit Jekyll den Inhalt von `_includes/lang-selector.html`{: .filepath} beim Seitenbau lädt:

{% raw %}
```liquid
  (Anfang)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(Ende)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
