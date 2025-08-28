---
title: "Mehrsprachige Unterstützung für einen Jekyll-Blog mit Polyglot (2) - Implementierung eines Sprachauswahl-Buttons & Lokalisierung der Layout-Sprache"
description: "Anleitung zur Implementierung eines Sprachauswahl-Buttons und zur Lokalisierung der Layout-Sprache in einem Jekyll-Blog mit dem Polyglot-Plugin. Dieser zweite Teil der Serie behandelt die Anpassung der Benutzeroberfläche für eine mehrsprachige Website auf Basis des 'jekyll-theme-chirpy'."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Übersicht
Anfang Juli 12024 habe ich meinem auf Jekyll basierenden und über Github Pages gehosteten Blog mit dem [Polyglot](https://github.com/untra/polyglot)-Plugin eine mehrsprachige Unterstützung hinzugefügt.
Diese Serie teilt den Prozess der Behebung von Fehlern, die bei der Anwendung des Polyglot-Plugins auf das Chirpy-Theme auftraten, sowie Anleitungen zur Erstellung von HTML-Headern und sitemap.xml unter Berücksichtigung von SEO.
Die Serie besteht aus drei Beiträgen, und dieser hier ist der zweite Teil.
- Teil 1: [Anwendung des Polyglot-Plugins & Anpassung von HTML-Header und Sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Teil 2: Implementierung des Sprachauswahl-Buttons & Lokalisierung der Layout-Sprache (Dieser Beitrag)
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

## Bevor wir beginnen
Dieser Beitrag ist die Fortsetzung von [Teil 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1). Wenn Sie diesen noch nicht gelesen haben, empfehle ich Ihnen, zuerst den vorherigen Beitrag zu lesen.

## Sprachauswahl-Button zur Seitenleiste hinzufügen
> (Update 05.02.12025) Der Sprachauswahl-Button wurde zu einer Dropdown-Liste verbessert.
{: .prompt-info }

Ich habe die Datei `_includes/lang-selector.html`{: .filepath} erstellt und den folgenden Inhalt eingegeben.

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
{: file='\_includes/lang-selector.html'}
{% endraw %}

Zudem habe ich die Datei `assets/css/lang-selector.css`{: .filepath} erstellt und den folgenden Inhalt eingegeben.

```css
/**
 * Stile für den Sprachwähler
 * 
 * Definiert die Stile für das Sprachauswahl-Dropdown in der Seitenleiste.
 * Unterstützt den Dunkelmodus des Themes und ist für mobile Umgebungen optimiert.
 */

/* Container für den Sprachwähler */
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
    /* Grundstile */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Schriftart und Farbe */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Aussehen und Interaktion */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Pfeilsymbol hinzufügen */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Stil für Flaggen-Emojis */
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

/* Anpassung für Firefox-Browser */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Anpassung für IE-Browser */
.lang-select::-ms-expand {
    display: none;
}

/* Anpassung für Dunkelmodus */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Optimierung für mobile Umgebungen */
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

Anschließend habe ich in der Datei [`_includes/sidebar.html`{: .filepath} des Chirpy-Themes](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) direkt vor der Klasse `sidebar-bottom` die folgenden drei Zeilen für die Klasse `lang-selector-wrapper` hinzugefügt, damit Jekyll den Inhalt der zuvor erstellten `_includes/lang-selector.html`{: .filepath} beim Erstellen der Seite lädt.

{% raw %}
```liquid
  (Anfang)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(Ende)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (Hinzugefügt am 31.07.12025) Lokalisierung der Layout-Sprache
Bisher wurde die Sprachlokalisierung nur auf den Hauptinhalt wie Seitentitel und Text angewendet, während die Layout-Sprache für Elemente wie die Tabs in der linken Seitenleiste, den oberen und unteren Bereich der Website sowie das rechte Panel auf dem Standardwert Englisch belassen wurde. Persönlich war das für mich ausreichend, weshalb ich keine große Notwendigkeit für weitere Anpassungen sah. Kürzlich entdeckte ich jedoch bei der Arbeit an [dem oben erwähnten Patch für Open-Graph-Metadaten-Attribute und die kanonische URL (canonical URL)](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#html-header), dass die Lokalisierung der Layout-Sprache mit nur geringfügigen Änderungen sehr einfach umzusetzen ist. Da es sich um [eine einfache Aufgabe, die weniger als 10 Minuten dauert](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb) handelte und keine umfangreichen und mühsamen Code-Änderungen erforderte, habe ich sie bei dieser Gelegenheit zusätzlich implementiert.

### Hinzufügen von Lokalen
Das [Chirpy-Theme unterstützt von Haus aus eine recht breite Palette von Sprachen](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales), auch wenn es keine Funktion bietet, um mehrere Sprachversionen für jede Seite gleichzeitig bereitzustellen und zwischen ihnen zu wechseln. Daher kann man die benötigten Lokalisierungsdateien aus dem Chirpy-Theme selektiv herunterladen, hinzufügen und bei Bedarf die Dateinamen entsprechend anpassen. Die Namen der Lokalisierungsdateien müssen mit den Einträgen in der `languages`-Liste übereinstimmen, die zuvor in der Phase der [Konfiguration](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#konfiguration) in der Datei `_config.yml`{: .filepath} definiert wurden.

> Wie gleich erwähnt wird, werden die Dateien im Verzeichnis `_data`{: .filepath} standardmäßig über das [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy) bereitgestellt, auch wenn man sie nicht manuell hinzufügt.
>
> In meinem Fall war es jedoch aus folgenden Gründen schwierig, die vom Chirpy-Theme bereitgestellten Lokalen unverändert zu verwenden, weshalb einige Anpassungen erforderlich waren:
> - Das Namensformat der vom Chirpy-Theme bereitgestellten Lokalisierungsdateien enthält regionale Codes wie `ko-KR` oder `ja-JP`, was nicht mit dem auf dieser Website verwendeten Format (`ko`, `ja` usw.) übereinstimmt.
> - Der Lizenzhinweis musste vom Standardwert [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) auf die für diesen Blog geltende [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) geändert werden.
> - Als Koreaner fand ich einige Formulierungen in den [koreanischen](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) und [japanischen](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) Lokalen etwas unnatürlich oder für diesen Blog unpassend, weshalb ich sie persönlich angepasst habe.
> - Aus den unten beschriebenen Gründen mag ich die christliche Zeitrechnung nicht besonders und habe für diesen Blog das Datumsformat auf die [Holozän-Zeitrechnung](https://en.wikipedia.org/wiki/Holocene_calendar) umgestellt, was eine Anpassung der Lokalen erforderte.
>   - Sie ist fundamental von einer bestimmten Religion geprägt und westlich-zentriert.
>     - Ich bestreite nicht, dass Jesus ein großer Heiliger war, und ich respektiere die Haltung dieser Religion. Wenn die christliche Zeitrechnung, ähnlich wie die buddhistische Zeitrechnung, nur intern von dieser Religion verwendet würde, gäbe es kein Problem. Da dies aber nicht der Fall ist, werfe ich die Frage auf. Es gab viele andere große Persönlichkeiten wie Konfuzius, Buddha, Sokrates usw. Warum sollte aus der Sicht von Nicht-Religiösen, Anhängern anderer Religionen und Kulturen außerhalb Europas das erste Jahr der weltweit verwendeten Zeitrechnung ausgerechnet das Geburtsjahr von Jesus sein?
>     - Und wenn man fragt, ob dieses 'erste Jahr' tatsächlich das Geburtsjahr von Jesus ist, ist die etablierte Ansicht, dass er tatsächlich einige Jahre früher geboren wurde.
>   - Da diese Zeitrechnung vor der Einführung des Konzepts der 'Null' entwickelt wurde, ist die Jahresberechnung nicht intuitiv, da auf das Jahr 1 v. Chr. (-1) direkt das Jahr 1 n. Chr. (1) folgt.
>   - Die 10.000 Jahre Geschichte seit dem Beginn des Neolithikums und der Agrargesellschaft bis vor der Geburt Jesu – oder selbst die 3000-4000 Jahre seit der Erfindung der Schrift – werden pauschal als 'vor Christus' bezeichnet, was zu einer kognitiven Verzerrung der Weltgeschichte, insbesondere der alten Geschichte, führt.
> 
> Aus diesen Gründen habe ich die Lokalisierungsdateien im Verzeichnis `_data/locales`{: .filepath} manuell hinzugefügt und entsprechend angepasst.  
> Wenn dies auf Sie nicht zutrifft und Sie die vom Chirpy-Theme bereitgestellten Lokalen ohne Änderungen verwenden möchten, können Sie diesen Schritt überspringen.
{: .prompt-tip }

### Integration mit Polyglot
Nun können wir durch geringfügige Änderungen an den folgenden zwei Dateien eine nahtlose Integration mit Polyglot erreichen.

> Wenn Sie Ihr Repository ursprünglich mit dem [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended) erstellt haben und nicht durch direktes Forken des Theme-Repositorys, sind die entsprechenden Dateien möglicherweise nicht in Ihrem Repository vorhanden. Das liegt daran, dass sie standardmäßig über das [jekyll-theme-chirpy gem](https://rubygems.org/gems/jekyll-theme-chirpy) bereitgestellt werden. In diesem Fall laden Sie einfach die Originaldateien aus dem [Chirpy-Theme-Repository](https://github.com/cotes2020/jekyll-theme-chirpy) herunter, platzieren sie an der gleichen Stelle in Ihrem Repository und nehmen dann die Änderungen vor. Wenn Jekyll die Website erstellt, werden Dateien in Ihrem Repository gegenüber denen aus externen Gems (wie jekyll-theme-chirpy) bevorzugt, sofern sie den gleichen Namen haben.
{: .prompt-tip }

#### '\_includes/lang.html'
Durch Hinzufügen von zwei Codezeilen in der Mitte der Datei [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) wird sichergestellt, dass [die Variable `site.active_lang` von Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#features) Vorrang vor der Standardsprache der Website (`site.lang`) oder Englisch (`'en'`) hat, die in `_config.yml`{: .filepath} definiert sind, falls in der YAML-Frontmatter einer Seite keine `lang`-Variable explizit angegeben ist. Diese Datei wird von allen Seiten der Website, die das Chirpy-Theme verwenden ([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)), beim Build-Prozess aufgerufen, um die `lang`-Variable zu deklarieren. Diese `lang`-Variable wird dann für die Lokalisierung der Layout-Sprache verwendet.

{% raw %}
```diff
@@ -1,10 +1,12 @@
 {% comment %}
-  Detect appearance language and return it through variable "lang"
+  Erkennt die Anzeigesprache und gibt sie über die Variable "lang" zurück
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

Priorität bei der Deklaration der `lang`-Variable:
- Vor der Änderung:
  1. `page.lang` (Wenn im YAML-Frontmatter der einzelnen Seite definiert)
  2. `site.lang` (Wenn in `_config.yml`{: .filepath} definiert)
  3. `'en'`
- Nach der Änderung:
  1. `page.lang` (Wenn im YAML-Frontmatter der einzelnen Seite definiert)
  2. **`site.active_lang`** (Wenn Polyglot angewendet wird)
  3. `site.lang` (Wenn in `_config.yml`{: .filepath} definiert)
  4. `'en'`

#### '\_layouts/default.html'
Ebenso wird der Inhalt der Datei [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) geändert, um sicherzustellen, dass dem obersten HTML-Element, dem `<html>`-Tag, das `lang`-Attribut korrekt zugewiesen wird.

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
 
-<!-- `site.alt_lang` can specify a language different from the UI -->
-<html lang="{{ page.lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
+<!-- `site.alt_lang` kann eine andere Sprache als die der Benutzeroberfläche festlegen -->
+<html lang="{{ page.lang | default: site.active_lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
   {% include head.html %}
```
{: file='\_layouts/default.html'}
{% endraw %}

Priorität bei der Zuweisung des `lang`-Attributs für das `<html>`-Tag:
- Vor der Änderung:
  1. `page.lang` (Wenn im YAML-Frontmatter der einzelnen Seite definiert)
  2. `site.alt_lang` (Wenn in `_config.yml`{: .filepath} definiert)
  3. `site.lang` (Wenn in `_config.yml`{: .filepath} definiert)
  4. `unknown` (leere Zeichenkette, `lang=""`)
- Nach der Änderung:
  1. `page.lang` (Wenn im YAML-Frontmatter der einzelnen Seite definiert)
  2. **`site.active_lang`** (Wenn Polyglot angewendet wird)
  3. `site.alt_lang` (Wenn in `_config.yml`{: .filepath} definiert)
  4. `site.lang` (Wenn in `_config.yml`{: .filepath} definiert)
  5. `unknown` (leere Zeichenkette, `lang=""`)

> Es wird nicht empfohlen, die Sprache einer Webseite (`lang`-Attribut) nicht anzugeben und auf `unknown` zu belassen. Es sollte nach Möglichkeit ein geeigneter Wert festgelegt werden. Wie Sie sehen, wird der Wert des `lang`-Attributs in `_config.yml`{: .filepath} als Fallback verwendet. Daher ist es ratsam, diesen Wert immer korrekt zu definieren, unabhängig davon, ob Sie Polyglot verwenden oder nicht. In der Regel sollte er bereits definiert sein. Wenn Sie, wie in diesem Beitrag beschrieben, Polyglot oder ein ähnliches i18n-Plugin verwenden, ist es sinnvoll, denselben Wert wie für [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#konfiguration) festzulegen.
{: .prompt-tip }

## Weiterführende Lektüre
Fortsetzung in [Teil 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
