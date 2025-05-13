---
title: GitHub Pages Blog erstellen und verwalten
description: Erfahre mehr über die Eigenschaften und Unterschiede zwischen statischen und dynamischen Webseiten, Static Site Generators und wie du einen Jekyll-Blog auf GitHub Pages hosten kannst.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
Seit Anfang des Jahres 12021 der [Holozän-Zeitrechnung](https://en.wikipedia.org/wiki/Holocene_calendar) habe ich begonnen, einen Blog mit Jekyll auf GitHub Pages zu hosten. Da ich den Installationsprozess damals nicht richtig dokumentiert hatte, gab es später bei der Wartung einige Schwierigkeiten. Deshalb habe ich mich entschlossen, den Installationsprozess und die Wartungsmethoden zumindest kurz zusammenzufassen.

(+ 12024.12 Inhaltsupdate)

## 1. Static Site Generator & Webhosting
### 1-1. Statische vs. Dynamische Webseiten
#### Statische Webseiten (Static Web Pages)
- Webseiten, die auf dem Server gespeicherte Daten unverändert an den Benutzer übermitteln
- Der Webserver liefert die vorher gespeicherte Seite entsprechend der Benutzeranfrage
- Benutzer sehen immer die gleiche Webseite, solange die auf dem Server gespeicherten Daten nicht geändert werden
- Da nur die angeforderte Datei übertragen werden muss, sind keine zusätzlichen Verarbeitungen nötig, was in der Regel zu schnelleren Antwortzeiten führt
- Bestehen nur aus einfachen Dateien, daher ist nur ein Webserver erforderlich, was die Einrichtungskosten niedrig hält
- Bieten begrenzte Dienste, da nur gespeicherte Informationen angezeigt werden können
- Daten müssen manuell vom Administrator hinzugefügt, bearbeitet oder gelöscht werden
- Leichter von Suchmaschinen zu crawlen, was für die Suchmaschinenoptimierung (SEO) vorteilhaft ist

#### Dynamische Webseiten (Dynamic Web Pages)
- Webseiten, die auf dem Server gespeicherte Daten durch Skripte verarbeiten und dann übermitteln
- Der Webserver interpretiert die Benutzeranfrage, verarbeitet die Daten und liefert die generierte Webseite
- Benutzer sehen je nach Situation, Zeit, Anfrage usw. unterschiedliche Webseiten
- Antworten sind relativ langsamer, da Skripte zur Erstellung der Webseite verarbeitet werden müssen
- Neben dem Webserver wird ein Anwendungsserver benötigt, was zu höheren Einrichtungskosten führt
- Ermöglichen vielfältige Dienste durch dynamische Kombination verschiedener Informationen
- Je nach Struktur der Webseite können Benutzer Daten direkt im Browser hinzufügen, bearbeiten oder löschen

### 1-2. Static Site Generator (SSG)
- Tools, die statische Webseiten aus Rohdaten (meist Markdown-Textdateien) und vordefinierten Templates erstellen
- Automatisieren den Prozess der Erstellung und Veröffentlichung von Webseiten, ohne dass einzelne HTML-Seiten manuell geschrieben werden müssen
- Beispiele: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Kostenloser Hosting-Service für statische Webseiten von GitHub
- Pro Konto kann eine persönliche Hauptwebseite gehostet werden, sowie unbegrenzt viele projektbezogene Dokumentationsseiten
- Nach Erstellung eines Repositories mit dem Namen '{username}.github.io' entsprechend deinem GitHub-Benutzernamen kannst du entweder direkt erstellte HTML-Seiten pushen oder GitHub Actions für Build und Deployment nutzen
- Bei Besitz einer eigenen Domain kann diese in den Einstellungen verknüpft werden, um anstelle der Standard-Domain '{username}.github.io' eine andere Domainadresse zu verwenden

## 2. Auswahl des SSG und Themes

### 2-1. Warum Jekyll?
Es gibt verschiedene SSGs wie Jekyll, Hugo, Gatsby usw., aber ich habe mich für Jekyll entschieden. Die Kriterien für meine Entscheidung waren:
- Minimierung unnötiger Fehlersuche, um mich auf das Schreiben und Bloggen konzentrieren zu können
  - Jekyll ist der offiziell von GitHub Pages unterstützte Static Site Generator. Natürlich können auch andere SSGs wie Hugo oder Gatsby auf GitHub Pages gehostet werden, oder man könnte andere Hosting-Dienste wie Netlify nutzen. Aber für einen persönlichen Blog dieser Größe ist es technisch nicht so wichtig, welcher SSG verwendet wird. Daher entschied ich mich für die einfachere Wartung und die größere Menge an Referenzdokumenten.
  - Jekyll hat auch die längste Entwicklungszeit im Vergleich zu Konkurrenten wie Hugo und Gatsby. Dadurch ist es besser dokumentiert und es gibt deutlich mehr Ressourcen, auf die man bei Problemen zurückgreifen kann.
- Vielfalt an verfügbaren Themes und Plugins
  - Selbst wenn man einen SSG verwendet, ist es mühsam und zeitaufwändig, alle Templates selbst zu erstellen, und es ist auch nicht notwendig. Es gibt viele hervorragende Themes im Web, die man einfach übernehmen kann.
  - Da ich hauptsächlich C und Python verwende und mit Ruby (Jekyll) oder Go (Hugo) nicht so vertraut bin, wollte ich bestehende Themes und Plugins intensiv nutzen.
  - Bei Jekyll fand ich schnell ein Theme, das mir gefiel, während Hugo und Gatsby vergleichsweise weniger Themes hatten, die für persönliche Blogs geeignet waren. Dies liegt wahrscheinlich an der bereits erwähnten Kompatibilität mit GitHub Pages und der längeren Entwicklungszeit.

### 2-2. Theme-Auswahl
#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- Theme, das ich für etwa 1 Jahr und 3 Monate nach der ersten Erstellung meines Blogs verwendet habe
- Unterstützung für Kommentarfunktionen über Disqus, Discourse, utterances usw.
- Unterstützung für Kategorien- und Tag-Klassifizierung
- Integrierte Google Analytics-Unterstützung
- Auswahl vordefinierter Skins
- Obwohl ich später zum Chirpy-Theme wechselte, das ein eleganteres Design hat, war Minimal Mistakes mit seinem schlichten Design durchaus brauchbar für einen technisch orientierten Blog.

#### Chirpy Jekyll Theme (12022.04 - heute)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- Theme, das ich seit April 12022 bis heute verwende
- Unterstützung für Mehrfachkategorien und Tags
- Integrierte Unterstützung für mathematische Formeln mit LaTex-Syntax basierend auf MathJax
- Integrierte Diagrammfunktionen basierend auf Mermaid
- Unterstützung für Kommentarfunktionen über Disqus, Giscus usw.
- Unterstützung für Google Analytics, GoatCounter
- Unterstützung für helles und dunkles Theme
- Zum Zeitpunkt des Wechsels bot Minimal Mistakes keine native Unterstützung für MathJax oder Mermaid, was manuelle Anpassungen erforderte. Chirpy unterstützt diese Funktionen standardmäßig.
- Vor allem ist das Design ansprechend. Während Minimal Mistakes zwar ordentlich ist, aber eine gewisse Steifheit aufweist, die eher zu offiziellen Projektdokumentationen oder Portfolio-Seiten passt, kann das Chirpy-Theme mit kommerziellen Blog-Plattformen wie Tistory, Medium oder velog mithalten.

## 3. GitHub Repository erstellen, bauen und deployen
Die folgenden Anweisungen beziehen sich auf das aktuell (12024.06) verwendete Chirpy Jekyll Theme und setzen voraus, dass Git bereits installiert ist.  
Siehe [Jekyll offizielle Installationsanleitung](https://jekyllrb.com/docs/installation/) und [Chirpy Jekyll Theme offizielle Seite](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Ruby & Jekyll installieren
Installiere Ruby und Jekyll gemäß der [offiziellen Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) entsprechend deinem Betriebssystem.

### 3-2. GitHub Repository erstellen
Die [offizielle Chirpy Jekyll Theme-Seite](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) stellt zwei Methoden vor:
1. Verwenden des "jekyll-theme-chirpy" Gems für Kerndateien und Beziehen der restlichen Ressourcen aus der [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) Vorlage
  - Vorteil: Einfacheres Upgrade auf neuere Versionen
  - Nachteil: Eingeschränkte Anpassungsmöglichkeiten
2. Forken des [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) Repositories als eigenes Blog-Repository
  - Vorteil: Vollständige Kontrolle über alle Dateien, ermöglicht freie Anpassungen auch für nicht standardmäßig unterstützte Funktionen
  - Nachteil: Für Upgrades muss der [neueste Upstream-Tag des Original-Repositories](https://github.com/cotes2020/jekyll-theme-chirpy/tags) gemerged werden, was zu Konflikten mit eigenen Anpassungen führen kann, die manuell gelöst werden müssen

Ich habe mich für Methode 1 entschieden. Das Chirpy-Theme ist bereits sehr ausgereift, sodass die meisten Benutzer kaum Anpassungen benötigen. Zudem wird es auch im Jahr 12024 noch aktiv weiterentwickelt, weshalb die Vorteile des regelmäßigen Folgens des Original-Upstreams die Vorteile eigener Anpassungen überwiegen, sofern man keine umfangreichen Änderungen plant. Auch der offizielle Leitfaden des Chirpy-Themes empfiehlt den meisten Benutzern Methode 1.

### 3-3. Hauptkonfiguration
Passe die notwendigen Einstellungen in den Dateien `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} und `_data/share.yml`{: .filepath} im Stammverzeichnis an. Die Dateien sind gut kommentiert und die Einstellungen intuitiv. Externe Konfigurationen wie die Einrichtung von Google Search Console oder Google Analytics/GoatCounter sind ebenfalls recht einfach, werden hier aber nicht im Detail behandelt, da sie nicht zum Kernthema dieses Beitrags gehören.

### 3-4. Lokaler Build
Dies ist kein notwendiger Schritt, aber nützlich, um zu überprüfen, wie neue Beiträge oder Änderungen im Web aussehen werden. Öffne ein Terminal im Stammverzeichnis des lokalen Repositories und führe folgenden Befehl aus:
```console
$ bundle exec jekyll s
```
Nach einigen Sekunden wird die Seite lokal gebaut und kann unter <http://127.0.0.1:4000> angesehen werden.

### 3-5. Deployment
Es gibt zwei Methoden:
1. Nutzung von GitHub Actions (für Hosting auf GitHub Pages)
  - Bei Verwendung des GitHub Free Plans muss das Repository öffentlich sein
  - Gehe auf der GitHub-Webseite zum *Settings*-Tab des Repositories, wähle im linken Navigationsmenü *Code and automation > Pages* und wähle im **Source**-Abschnitt die Option **GitHub Actions**
  - Nach der Einrichtung wird der *Build and Deploy*-Workflow automatisch bei jedem neuen Push ausgeführt
2. Manueller Build und Deployment (für andere Hosting-Dienste oder Self-Hosting)
  - Führe folgenden Befehl aus, um die Seite zu bauen:
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Lade die Ergebnisse aus dem `_site`-Verzeichnis auf deinen Server hoch

## 4. Beiträge verfassen
Der [Leitfaden zum Verfassen von Beiträgen](https://chirpy.cotes.page/posts/write-a-new-post/) des Chirpy-Themes dokumentiert ausführlich, wie Beiträge erstellt werden und welche Optionen verfügbar sind. Hier werden die wichtigsten Punkte zusammengefasst, die bei jedem Beitrag zu beachten sind.

### Markdown-Datei erstellen
- Namensformat: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Speicherort: `_posts`{: .filepath}-Verzeichnis

### Front Matter erstellen
Am Anfang jeder Markdown-Datei muss ein Front Matter-Abschnitt stehen:
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: Titel des Beitrags
- **description**: Zusammenfassung. Wenn nicht angegeben, wird automatisch ein Teil des Haupttextes verwendet. Für SEO wird empfohlen, diesen Meta-Tag selbst zu verfassen. Idealerweise 135-160 Zeichen für lateinische Schrift, 80-110 Zeichen für Hangul.
- **date**: Genaues Erstellungsdatum und Zeitzone (optional, bei Weglassen wird das Erstellungs- oder Änderungsdatum der Datei verwendet)
- **categories**: Kategorien des Beitrags
- **tags**: Tags für den Beitrag
- **image**: Vorschaubild am Anfang des Beitrags
  - **path**: Pfad zur Bilddatei
  - **alt**: Alternativer Text (optional)
- **toc**: Aktivierung des Inhaltsverzeichnisses in der rechten Seitenleiste, Standardwert ist `true`
- **comments**: Explizite Festlegung der Kommentarfunktion für einzelne Beiträge, unabhängig von der Standardeinstellung
- **math**: Aktivierung der integrierten [MathJax](https://www.mathjax.org/)-basierten Formeldarstellung, standardmäßig deaktiviert (`false`) für bessere Seitenleistung
- **mermaid**: Aktivierung der integrierten [Mermaid](https://github.com/mermaid-js/mermaid)-basierten Diagrammdarstellung, standardmäßig deaktiviert (`false`)

## 5. Upgrade

Hier wird angenommen, dass Methode 1 aus [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-github-repository-erstellen) gewählt wurde. Bei Methode 2 müsste der neueste Upstream-Tag manuell gemerged werden.

1. Bearbeite die `Gemfile`{: .filepath}, um die Version des "jekyll-theme-chirpy" Gems zu aktualisieren.
2. Bei Major-Upgrades können sich auch Kerndateien und Konfigurationsoptionen ändern, die nicht im "jekyll-theme-chirpy" Gem enthalten sind. Prüfe in diesem Fall die Änderungen mit der folgenden GitHub API und wende sie manuell an:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
