---
title: Wie man mit Polyglot mehrsprachige Unterstützung für einen Jekyll-Blog implementiert (1) - Anwendung des Polyglot-Plugins & Implementierung von hreflang alt-Tags, Sitemap und Sprachauswahl-Button
description: 'Dieser Beitrag beschreibt den Prozess der Implementierung mehrsprachiger Unterstützung für einen Jekyll-Blog basierend auf dem ''jekyll-theme-chirpy'' Theme unter Verwendung des Polyglot-Plugins. Dies ist der erste Teil der Serie und behandelt die Anwendung des Polyglot-Plugins sowie die Modifikation des HTML-Headers und der Sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## Überblick
Vor etwa 4 Monaten, Anfang Juli 2024, habe ich die mehrsprachige Unterstützung für diesen Jekyll-basierten Blog, der über Github Pages gehostet wird, durch die Implementierung des [Polyglot](https://github.com/untra/polyglot)-Plugins hinzugefügt.
Diese Serie teilt die Erfahrungen mit Bugs, die während der Anwendung des Polyglot-Plugins auf das Chirpy-Theme auftraten, deren Lösungsprozesse, sowie Methoden zum Schreiben von HTML-Headern und sitemap.xml unter Berücksichtigung der SEO.
Die Serie besteht aus zwei Artikeln, und dieser Artikel, den Sie gerade lesen, ist der erste Teil der Serie.
- Teil 1: Anwendung des Polyglot-Plugins & Implementierung von hreflang alt-Tags, Sitemap und Sprachauswahl-Button (dieser Artikel)
- Teil 2: [Fehlerbehebung bei Build-Fehlern des Chirpy-Themes und Suchfunktionsproblemen](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Anforderungen
- [x] Das gebaute Ergebnis (Webseite) sollte nach sprachspezifischen Pfaden (z.B. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}) unterschieden und bereitgestellt werden können.
- [x] Um den zusätzlichen Zeit- und Arbeitsaufwand für die mehrsprachige Unterstützung zu minimieren, sollte die Sprache automatisch anhand des lokalen Pfads (z.B. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) der ursprünglichen Markdown-Datei beim Build erkannt werden können, ohne dass 'lang' und 'permalink' Tags im YAML-Frontmatter der Datei manuell spezifiziert werden müssen.
- [x] Der Header-Bereich jeder Seite der Website sollte angemessene Content-Language Meta-Tags und hreflang Alternate-Tags enthalten, um die SEO-Richtlinien für die Google-Mehrsprachensuche zu erfüllen.
- [x] Die `sitemap.xml`{: .filepath} sollte alle Links zu den Seiten in jeder unterstützten Sprache auf der Website ohne Auslassungen bereitstellen können, und die `sitemap.xml`{: .filepath} selbst sollte nur einmal im Root-Verzeichnis ohne Duplikate existieren.
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

Anschließend wird die Installation automatisch abgeschlossen, wenn Sie `bundle update` im Terminal ausführen.

Wenn Sie Bundler nicht verwenden, können Sie das Gem auch direkt mit dem Befehl `gem install jekyll-polyglot` im Terminal installieren und dann das Plugin wie folgt zu `_config.yml`{: .filepath} hinzufügen:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfiguration
Als Nächstes öffnen Sie die Datei `_config.yml`{: .filepath} und fügen Sie Folgendes hinzu:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
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
- lang_from_path: Boolescher Wert; wenn auf 'true' gesetzt, wird die Sprache automatisch aus dem Pfadstring der Markdown-Datei erkannt und verwendet, wenn dieser einen Sprachcode enthält, ohne dass das 'lang'-Attribut explizit im YAML-Frontmatter des Beitrags angegeben werden muss

> Das [offizielle Dokument zum Sitemap-Protokoll](https://www.sitemaps.org/protocol.html#location) besagt Folgendes:
>
>> "Der Standort einer Sitemap-Datei bestimmt die Menge der URLs, die in dieser Sitemap enthalten sein können. Eine Sitemap-Datei, die sich unter http://example.com/catalog/sitemap.xml befindet, kann alle URLs enthalten, die mit http://example.com/catalog/ beginnen, aber keine URLs, die mit http://example.com/images/ beginnen."
>
>> "Es wird dringend empfohlen, Ihre Sitemap im Stammverzeichnis Ihres Webservers zu platzieren."
>
> Um dies einzuhalten, sollte 'sitemap.xml'{: .filepath} zur Liste 'exclude_from_localization' hinzugefügt werden, damit nicht für jede Sprache eine separate `sitemap.xml`{: .filepath}-Datei mit identischem Inhalt erstellt wird, sondern nur eine einzige im Stammverzeichnis existiert. So wird vermieden, dass es wie im folgenden falschen Beispiel aussieht.
>
> Falsches Beispiel (der Inhalt jeder Datei ist für alle Sprachen identisch):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Update vom 14.01.2025) Nachdem [ein Pull Request mit den oben genannten Inhalten zur Ergänzung des README akzeptiert wurde](https://github.com/untra/polyglot/pull/230), kann man nun die gleiche Anleitung auch in der [offiziellen Polyglot-Dokumentation](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation) finden.
{: .prompt-tip }

> Wenn 'parallel_localization' auf 'true' gesetzt wird, kann die Build-Zeit erheblich verkürzt werden, aber zum Zeitpunkt Juli 2024 gab es für diesen Blog einen Bug, bei dem die Linktitel im 'Recently Updated' und 'Trending Tags' Bereich der rechten Seitenleiste nicht korrekt verarbeitet wurden und mit anderen Sprachen vermischt waren, wenn diese Funktion aktiviert war. Es scheint noch nicht vollständig stabilisiert zu sein, daher sollte vor der Anwendung auf die Website getestet werden, ob es normal funktioniert. Außerdem [wird diese Funktion unter Windows nicht unterstützt und sollte daher deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Außerdem [muss in Jekyll 4.0 die Generierung von CSS-Sourcemaps wie folgt deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Zu beachtende Punkte beim Verfassen von Beiträgen
Beim Verfassen mehrsprachiger Beiträge sollten folgende Punkte beachtet werden:
- Korrekte Sprachcode-Zuweisung: Der entsprechende ISO-Sprachcode sollte entweder über den Dateipfad (z.B. `/_posts/ko/example-post.md`{: .filepath}) oder über das 'lang'-Attribut im YAML-Frontmatter (z.B. `lang: ko`) zugewiesen werden. Siehe Beispiele in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Allerdings verwendet die [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) das Format 'pt_BR' für Regionscodes, aber tatsächlich sollte '-' anstelle von '_' verwendet werden, also 'pt-BR', damit es später beim Hinzufügen von hreflang-Alternate-Tags zum HTML-Header korrekt funktioniert.

- Dateipfade und -namen sollten konsistent sein.

Weitere Details finden Sie im README des GitHub-Repositories [untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Änderung des HTML-Headers und der Sitemap
Nun müssen für SEO-Zwecke Content-Language Meta-Tags und hreflang Alternate-Tags in den HTML-Header jeder Seite des Blogs eingefügt werden.

### HTML-Header
In der neuesten Version 1.8.1 (Stand November 2024) bietet Polyglot eine Funktion, die diese Aufgabe automatisch erledigt, wenn der Liquid-Tag {% raw %}`{% I18n_Headers %}`{% endraw %} im Header-Bereich der Seite aufgerufen wird.
Dies setzt jedoch voraus, dass für die betreffende Seite ein 'permalink'-Attribut-Tag explizit angegeben wurde, andernfalls funktioniert es nicht ordnungsgemäß.

Daher habe ich [head.html aus dem Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) übernommen und dann den Inhalt wie folgt direkt ergänzt.
Ich habe mich an der [SEO Recipes-Seite des offiziellen Polyglot-Blogs](https://polyglot.untra.io/seo/) orientiert, aber modifiziert, um das `page.url`-Attribut zu verwenden, wenn `page.permalink` nicht vorhanden ist.

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
Da die von Jekyll beim Build automatisch generierte Sitemap mehrsprachige Seiten nicht korrekt unterstützt, erstellen Sie eine `sitemap.xml`{: .filepath}-Datei im Stammverzeichnis und fügen Sie folgenden Inhalt ein:

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
            {% comment %}<!-- Annahme, dass wenn kein Layout zugewiesen ist, die Seite nicht in die Sitemap aufgenommen wird, Sie möchten dies möglicherweise ändern -->{% endcomment %}
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
(Update vom 05.02.2025) Der Sprachauswahl-Button wurde zu einem Dropdown-Listenformat verbessert.  
Erstellen Sie eine Datei `_includes/lang-selector.html`{: .filepath} und fügen Sie folgenden Inhalt ein:

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Sprache auswählen">
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

Erstellen Sie außerdem eine Datei `assets/css/lang-selector.css`{: .filepath} und fügen Sie folgenden Inhalt ein:

```css
/**
 * Sprachauswahl-Stil
 * 
 * Definiert den Stil für die Sprachauswahl-Dropdown in der Seitenleiste.
 * Unterstützt den Dunkelmodus des Themes und ist für mobile Umgebungen optimiert.
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

/* Auswahl-Eingabeelement */
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

/* Dunkelmodus-Anpassung */
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

Fügen Sie als Nächstes die folgenden drei Zeilen direkt vor der Klasse "sidebar-bottom" in [Chirpy's `_includes/sidebar.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) ein, damit Jekyll den Inhalt von `_includes/lang-selector.html`{: .filepath} beim Seitenbau lädt:

{% raw %}
```liquid
  (Vorheriger Teil)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(Nachfolgender Teil)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Weiterführende Lektüre
Fortsetzung in [Teil 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
