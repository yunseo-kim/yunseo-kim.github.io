---
title: Wie man mit Polyglot mehrsprachige Unterstützung für einen Jekyll-Blog implementiert
description: >-
  Dieser Beitrag beschreibt den Prozess der Implementierung mehrsprachiger Unterstützung für einen Jekyll-Blog basierend auf dem 'jekyll-theme-chirpy' Theme unter Verwendung des Polyglot-Plugins.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
- RegExp
---
## Einleitung
Vor etwa 4 Monaten, Anfang Juli 2024, habe ich das [Polyglot](https://github.com/untra/polyglot)-Plugin implementiert, um mehrsprachige Unterstützung für diesen Jekyll-basierten Blog hinzuzufügen, der über Github Pages gehostet wird.
In diesem Beitrag teile ich die Bugs, die während der Anwendung des Polyglot-Plugins auf das Chirpy-Theme auftraten, deren Lösungsprozesse, sowie Methoden zum Schreiben von HTML-Headern und sitemap.xml unter Berücksichtigung der SEO.

## Anforderungen
- [x] Die gebauten Ergebnisse (Webseiten) sollten unter sprachspezifischen Pfaden (z.B. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}) bereitgestellt werden können.
- [x] Um den zusätzlichen Zeit- und Arbeitsaufwand für die mehrsprachige Unterstützung zu minimieren, sollte es möglich sein, die Sprache automatisch anhand des lokalen Pfads (z.B. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) zu erkennen, ohne dass 'lang' und 'permalink' Tags im YAML-Frontmatter der originalen Markdown-Dateien manuell spezifiziert werden müssen.
- [x] Der Header-Bereich jeder Seite der Website sollte angemessene Content-Language Meta-Tags und hreflang Alternate-Tags enthalten, um die SEO-Richtlinien für die mehrsprachige Google-Suche zu erfüllen.
- [x] Es sollte möglich sein, Links zu allen Seiten, die jede Sprache unterstützen, ohne Auslassungen in der `sitemap.xml` bereitzustellen, und die `sitemap.xml` selbst sollte nur einmal im Root-Verzeichnis ohne Duplikate existieren.
- [ ] Alle vom [Chirpy-Theme](https://github.com/cotes2020/jekyll-theme-chirpy) bereitgestellten Funktionen sollten auf jeder Sprachseite normal funktionieren, andernfalls sollten sie entsprechend angepasst werden.
  - [x] Normale Funktion von Features wie 'Recently Updated', 'Trending Tags' usw.
  - [x] Keine falsch positiven (False Positive) Warnungen bei der Überprüfung interner Links während des Build-Prozesses mit GitHub Actions
  - [ ] Normale Funktion der Beitragssuche in der oberen rechten Ecke des Blogs

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

Anschließend wird durch Ausführen von `bundle update` im Terminal die Installation automatisch abgeschlossen.

Wenn Sie Bundler nicht verwenden, können Sie das Gem auch direkt mit dem Befehl `gem install jekyll-polyglot` im Terminal installieren und dann das Plugin wie folgt zu `_config.yml` hinzufügen:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Konfiguration
Als Nächstes öffnen Sie die Datei `_config.yml` und fügen Sie Folgendes hinzu:

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
- parallel_localization: Boolean-Wert, der angibt, ob die mehrsprachige Verarbeitung während des Build-Prozesses parallelisiert werden soll
- lang_from_path: Boolean-Wert; wenn auf 'true' gesetzt, wird die Sprache automatisch aus dem Pfadstring der Markdown-Datei erkannt, wenn dieser einen Sprachcode enthält, ohne dass das 'lang'-Attribut im YAML-Frontmatter der Markdown-Datei explizit angegeben werden muss

> Das [offizielle Dokument des Sitemap-Protokolls](https://www.sitemaps.org/protocol.html#location) besagt Folgendes:
>
>> "Der Standort einer Sitemap-Datei bestimmt die Menge der URLs, die in dieser Sitemap enthalten sein können. Eine Sitemap-Datei, die sich unter http://example.com/catalog/sitemap.xml befindet, kann alle URLs enthalten, die mit http://example.com/catalog/ beginnen, aber keine URLs, die mit http://example.com/images/ beginnen."
>
>> "Es wird dringend empfohlen, Ihre Sitemap im Stammverzeichnis Ihres Webservers zu platzieren."
>
> Um dies einzuhalten, sollte 'sitemap.xml' zur Liste 'exclude_from_localization' hinzugefügt werden, damit nicht mehrere `sitemap.xml`-Dateien mit identischem Inhalt für jede Sprache erstellt werden, sondern nur eine einzige im Root-Verzeichnis existiert. So wird vermieden, dass es wie in diesem falschen Beispiel aussieht:
>
> Falsches Beispiel (der Inhalt jeder Datei ist für alle Sprachen identisch):
> - https://www.yunseo.kim/sitemap.xml
> - https://www.yunseo.kim/ko/sitemap.xml
> - https://www.yunseo.kim/es/sitemap.xml
> - https://www.yunseo.kim/pt-BR/sitemap.xml
> - https://www.yunseo.kim/ja/sitemap.xml
> - https://www.yunseo.kim/fr/sitemap.xml
> - https://www.yunseo.kim/de/sitemap.xml
{: .prompt-tip }

> Wenn 'parallel_localization' auf 'true' gesetzt wird, kann die Build-Zeit erheblich verkürzt werden. Allerdings gab es zum Zeitpunkt Juli 2024 einen Bug, bei dem die Links in den Abschnitten 'Recently Updated' und 'Trending Tags' in der rechten Seitenleiste dieses Blogs nicht korrekt verarbeitet wurden und mit anderen Sprachen vermischt waren, wenn diese Funktion aktiviert war. Es scheint noch nicht vollständig stabilisiert zu sein, daher sollte vor der Anwendung auf einer Website getestet werden, ob es ordnungsgemäß funktioniert. Außerdem [wird diese Funktion unter Windows nicht unterstützt und sollte deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Außerdem [muss in Jekyll 4.0 die Generierung von CSS-Sourcemaps wie folgt deaktiviert werden](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 werden SCSS-Sourcemaps aufgrund der Funktionsweise von Polyglot nicht korrekt generiert
```
{: file='_config.yml'}

### Zu beachten beim Schreiben von Beiträgen
Beim Schreiben mehrsprachiger Beiträge sollten folgende Punkte beachtet werden:
- Korrekte Sprachcode-Zuweisung: Der entsprechende ISO-Sprachcode sollte entweder über den Dateipfad (z.B. `/_posts/ko/example-post.md`{: .filepath}) oder über das 'lang'-Attribut im YAML-Frontmatter (z.B. `lang: ko`) zugewiesen werden. Siehe Beispiele in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Beachten Sie jedoch, dass in der [Chrome-Entwicklerdokumentation](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) Regionscodes im Format 'pt_BR' angegeben sind, aber tatsächlich 'pt-BR' mit einem Bindestrich anstelle eines Unterstrichs verwendet werden sollte, damit später hreflang Alternate-Tags korrekt zum HTML-Header hinzugefügt werden können.

- Dateipfade und -namen sollten konsistent sein.

Weitere Details finden Sie in der README des [untra/polyglot GitHub-Repositories](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Fehlerbehebung ('relative_url_regex': target of repeat operator is not specified)
Nach Abschluss der vorherigen Schritte führte ich den Befehl `bundle exec jekyll serve` aus, um einen Build-Test durchzuführen. Dabei trat der Fehler `'relative_url_regex': target of repeat operator is not specified` auf, und der Build schlug fehl.

```shell
...(Vorheriges ausgelassen)
                    ------------------------------------------------
      Jekyll 4.3.4   Please append `--trace` to the `serve` command 
                     for any additional information or backtrace. 
                    ------------------------------------------------
/Users/yunseo/.gem/ruby/3.2.2/gems/jekyll-polyglot-1.8.1/lib/jekyll/polyglot/
patches/jekyll/site.rb:234:in `relative_url_regex': target of repeat operator 
is not specified: /href="?\/((?:(?!*.gem)(?!*.gemspec)(?!tools)(?!README.md)(
?!LICENSE)(?!*.config.js)(?!rollup.config.js)(?!package*.json)(?!.sass-cache)
(?!.jekyll-cache)(?!gemfiles)(?!Gemfile)(?!Gemfile.lock)(?!node_modules)(?!ve
ndor\/bundle\/)(?!vendor\/cache\/)(?!vendor\/gems\/)(?!vendor\/ruby\/)(?!en\/
)(?!ko\/)(?!es\/)(?!pt-BR\/)(?!ja\/)(?!fr\/)(?!de\/)[^,'"\s\/?.]+\.?)*(?:\/[^
\]\[)("'\s]*)?)"/ (RegexpError)

...(Nachfolgendes ausgelassen)
```

Nach einer Suche nach ähnlichen gemeldeten Problemen fand ich [genau dasselbe Problem](https://github.com/untra/polyglot/issues/204) bereits im Polyglot-Repository registriert, zusammen mit einer Lösung.

Die `_config.yml`-Datei des [Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml), das in diesem Blog verwendet wird, enthält den folgenden Abschnitt:

```yml
exclude:
  - "*.gem"
  - "*.gemspec"
  - docs
  - tools
  - README.md
  - LICENSE
  - "*.config.js"
  - package*.json
```
{: file='_config.yml'}

Die Ursache des Problems liegt in den regulären Ausdrücken der folgenden beiden Funktionen in der [site.rb-Datei von Polyglot](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb), die Globbing-Muster mit Wildcards wie `"*.gem"`, `"*.gemspec"`, `"*.config.js"` nicht korrekt verarbeiten können.

{% raw %}
```ruby
    # ein regulärer Ausdruck, der relative URLs in einem HTML-Dokument abgleicht
    # passt auf href="baseurl/foo/bar-baz" href="/foo/bar-baz" und ähnliche
    # vermeidet das Abgleichen ausgeschlossener Dateien. prepare stellt sicher,
    # dass alle @exclude-Verzeichnisse einen abschließenden Schrägstrich haben.
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    # ein regulärer Ausdruck, der absolute URLs in einem HTML-Dokument abgleicht
    # passt auf href="http://baseurl/foo/bar-baz" und ähnliche
    # vermeidet das Abgleichen ausgeschlossener Dateien. prepare stellt sicher,
    # dass alle @exclude-Verzeichnisse einen abschließenden Schrägstrich haben.
    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(polyglot root path)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

Es gibt zwei Möglichkeiten, dieses Problem zu lösen:

### 1. Forken Sie Polyglot, modifizieren Sie den problematischen Teil und verwenden Sie es
Zum Zeitpunkt dieses Beitrags (November 2024) gibt die [offizielle Jekyll-Dokumentation](https://jekyllrb.com/docs/configuration/options/#global-configuration) an, dass die `exclude`-Konfiguration die Verwendung von Globbing-Mustern unterstützt.

>"Diese Konfigurationsoption unterstützt Rubys File.fnmatch Dateinamen-Globbing-Muster, um mehrere Einträge zum Ausschließen abzugleichen."

Das bedeutet, dass die Ursache des Problems nicht im Chirpy-Theme liegt, sondern in den beiden Funktionen `relative_url_regex()` und `absolute_url_regex()` von Polyglot. Die grundlegende Lösung besteht darin, diese so zu modifizieren, dass das Problem nicht mehr auftritt.

Da dieser Bug in Polyglot noch nicht behoben wurde, können Sie Polyglot forken und den problematischen Teil wie folgt modifizieren, basierend auf [diesem Blogbeitrag](https://hionpu.com/en/posts/github_blog_4#4-polyglot-dependency-issue) und [dieser Antwort im vorherigen GitHub-Issue](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322), und dann anstelle des Original-Polyglot verwenden:

{% raw %}
```ruby
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(polyglot root path)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

### 2. Ersetzen Sie die Globbing-Muster in der _config.yml-Datei des Chirpy-Themes durch genaue Dateinamen
Eigentlich wäre die ideale und korrekte Methode, dass der obige Patch in den Hauptzweig von Polyglot aufgenommen wird. Bis dahin müsste man jedoch eine geforkte Version verwenden, was umständlich sein kann, da man bei jedem Upstream-Update von Polyglot diese Änderungen nicht verpassen und nachziehen muss. Daher habe ich mich für eine andere Methode entschieden.

Wenn man die Dateien im Wurzelverzeichnis des [Chirpy-Theme-Repositories](https://github.com/cotes2020/jekyll-theme-chirpy) überprüft, die den Mustern `"*.gem"`, `"*.gemspec"`, `"*.config.js"` entsprechen, stellt man fest, dass es ohnehin nur die folgenden 3 gibt:
- `jekyll-theme-chirpy.gemspec`
- `purgecss.config.js`
- `rollup.config.js`

Daher kann man die Globbing-Muster im `exclude`-Abschnitt der `_config.yml`-Datei löschen und wie folgt ersetzen, damit Polyglot sie problemlos verarbeiten kann:

```yml
exclude: # Modifiziert unter Berücksichtigung des Issues https://github.com/untra/polyglot/issues/204.
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```

## Änderung des HTML-Headers und der Sitemap
Nun müssen für SEO-Zwecke Content-Language Meta-Tags und hreflang Alternate-Tags in den HTML-Header jeder Seite des Blogs eingefügt werden.

### HTML-Header
Ab Version 1.8.1, der neuesten Version zum Zeitpunkt November 2024, bietet Polyglot eine Funktion, die diese Aufgabe automatisch ausführt, wenn der Liquid-Tag {% raw %}`{% I18n_Headers %}`{% endraw %} im Header-Bereich der Seite aufgerufen wird.
Dies setzt jedoch voraus, dass das 'permalink'-Attribut-Tag für die Seite explizit angegeben wurde, andernfalls funktioniert es nicht ordnungsgemäß.

Daher habe ich [head.html des Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) übernommen und den Inhalt wie folgt direkt hinzugefügt.
Ich habe mich an der [SEO Recipes-Seite des offiziellen Polyglot-Blogs](https://polyglot.untra.io/seo/) orientiert, aber modifiziert, um die `page.url`-Eigenschaft zu verwenden, wenn `page.permalink` nicht vorhanden ist.
Außerdem habe ich basierend auf der [offiziellen Google Search Central-Dokumentation](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault) `x-default` anstelle von `site.default_lang` als hreflang-Attributwert für die Standardsprachseite der Website festgelegt, damit dieser Seitenlink als Fallback erkannt wird, wenn die bevorzugte Sprache des Besuchers nicht in der Liste der unterstützten Sprachen der Website enthalten ist oder wenn die bevorzugte Sprache des Besuchers nicht erkannt werden kann.

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
Da die von Jekyll beim Bauen automatisch generierte Sitemap mehrsprachige Seiten nicht korrekt unterstützt, erstellen Sie eine `sitemap.xml`-Datei im Root-Verzeichnis und fügen Sie den folgenden Inhalt ein:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- sehr einfache Überprüfung, ob die Seite in der Ausschlussliste ist - das bedeutet, dass ausgeschlossene Seiten überhaupt nicht in der Sitemap erscheinen, schreiben Sie bei Bedarf Ausnahmen -->{% endcomment %}
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

## Hinzufügen einer Sprachauswahl-Schaltfläche zur Seitenleiste
Ich habe eine Datei `_includes/lang-selector.html` erstellt und den folgenden Inhalt eingefügt:

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

Anschließend habe ich die folgenden drei Zeilen zum "sidebar-bottom"-Klassenabschnitt in [_includes/sidebar.html des Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) hinzugefügt, damit Jekyll den Inhalt von `_includes/lang-selector.html` beim Seitenbau lädt:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Problem bei der Verwendung der Suchfunktion: Mehrsprachige Seiten werden nicht korrekt indiziert
Nach Abschluss der vorherigen Schritte funktionierten fast alle Funktionen der Website wie beabsichtigt zufriedenstellend. Allerdings stellte ich später fest, dass die Suchleiste in der oberen rechten Ecke der Seite mit dem Chirpy-Theme Seiten in anderen Sprachen als `site.default_lang` (in diesem Fall Englisch) nicht indizierte und bei der Suche in anderen Sprachen als Englisch englische Seiten als Suchergebnisse ausgab.

Dies liegt daran, dass die [Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search) JavaScript-Bibliothek, die vom Chirpy-Theme verwendet wird, für die Indizierung auf die von Jekyll bereitgestellte `site.posts`-Variable angewiesen ist und daher mehrsprachige Seiten, die mit Polyglot erstellt wurden, außer der Standardsprache nicht erkennt.

Die einfache Struktur von Simple-Jekyll-Search, die die Indizierung mit einer einzigen Liquid-Vorlage namens [`search.json`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/assets/js/data/search.json) durchführt und nur auf von Jekyll standardmäßig bereitgestellte Variablen angewiesen ist, ist einerseits ein Vorteil, erweist sich in diesem Fall jedoch als entscheidender Nachteil und Einschränkung und ist daher für die Anwendung in diesem Blog ungeeignet. Solange Jekyll keine native Unterstützung für mehrsprachige Seiten bietet und Polyglot keine Alternative zur `site.posts`-Variable bereitstellt, kann Simple-Jekyll-Search die für diesen Blog erforderliche Indizierung mehrsprachiger Seiten nicht ordnungsgemäß durchführen. Daher ist es notwendig, eine Alternative zu Simple-Jekyll-Search zu finden und zu implementieren, was als Folgeprojekt und Thema für einen zukünftigen Beitrag verbleibt.
