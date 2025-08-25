---
title: GitHub-Pages-Blog erstellen und verwalten
description: Merkmale und Unterschiede statischer und dynamischer Webseiten; Überblick über Static Site Generatoren und ein Jekyll‑Blog, der auf GitHub Pages gehostet wird.
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

Seit Anfang 12021 hoste ich mit Jekyll einen Blog auf GitHub Pages. Da ich den Installationsprozess beim Aufsetzen nicht sauber dokumentiert hatte, war die spätere Wartung mühsam. Deshalb halte ich hier kurz Installation und Pflege fest.  

(+ Inhalt aktualisiert 12024.12)

## 1. Static-Site-Generator & Webhosting
### 1-1. Statische Webseiten vs. dynamische Webseiten
#### Statische Webseite (Static Web Page)
- Webseite, die auf dem Server gespeicherte Daten unverändert an die Nutzer ausliefert
- Der Webserver liefert eine vorab gespeicherte Seite passend zur Anfrage
- Nutzende sehen dieselbe Seite, solange die auf dem Server gespeicherten Daten unverändert bleiben
- Da nur die angeforderte Datei übertragen wird, sind keine zusätzlichen Verarbeitungsschritte nötig; die Antwort ist in der Regel schnell
- Besteht aus einfachen Dateien; ein Webserver genügt, daher geringe Einrichtungskosten
- Zeigt nur vorab gespeicherte Informationen; Funktionsumfang ist begrenzt
- Hinzufügen, Ändern und Löschen von Daten erfolgt meist manuell durch die Verwaltung
- Struktur ist für Crawler günstig; relativ vorteilhaft für Suchmaschinenoptimierung (SEO)

#### Dynamische Webseite (Dynamic Web Page)
- Webseite, die serverseitig Daten per Skript verarbeitet und ausliefert
- Der Webserver interpretiert die Anfrage, verarbeitet Daten und liefert die generierte Seite
- Inhalt variiert je nach Situation, Zeitpunkt und Anfrage
- Skriptausführung macht die Auslieferung relativ langsamer
- Zusätzlich zum Webserver ist ein Anwendungsserver erforderlich; es entstehen Mehrkosten
- Durch dynamische Kombination von Informationen sind vielfältige Dienste möglich
- Je nach Aufbau können Nutzende Daten im Browser hinzufügen, ändern oder löschen

### 1-2. Statischer Website‑Generator (SSG, Static Site Generator)
- Werkzeug, das aus Rohdaten (meist Markdown‑Textdateien) und vordefinierten Templates statische Seiten erzeugt
- Automatisiert das Bauen und Ausliefern: Beiträge in Markdown verfassen, den Rest übernimmt das System
- z. B. Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Kostenloser Hosting‑Dienst für statische Webseiten von GitHub
- Pro Konto lässt sich eine persönliche Hauptseite hosten; außerdem können unbegrenzt viele Repository‑basierte Projekt‑Dokuseiten erstellt und gehostet werden.
- Erstelle ein Repository mit dem Namen '{username}.github.io' passend zu deinem GitHub‑Nutzernamen und pushe die gebauten HTML‑Seiten dorthin oder nutze GitHub Actions zum Bauen und Deployen.
- Mit eigener Domain lässt sich in den Einstellungen die Standarddomain im Format '{username}.github.io' ersetzen.

## 2. SSG und Theme auswählen

### 2-1. Warum ich Jekyll gewählt habe
Es gibt mehrere SSGs wie Jekyll, Hugo, Gatsby; entschieden habe ich mich für Jekyll. Kriterien und Gründe:
- Minimiert es unnötige Fehlversuche, sodass ich mich aufs Schreiben und den Betrieb konzentrieren kann?
  - Jekyll wird von GitHub Pages offiziell unterstützt. Natürlich lassen sich auch Hugo, Gatsby etc. dort hosten, oder man nutzt andere Hoster wie Netlify. Für einen Blog dieser Größenordnung sind SSG‑Wahl, Build‑Tempo und Performance aber weniger entscheidend. Mir war wichtiger, dass Wartung einfach ist und es viele Referenzen gibt.
  - Jekyll wird länger entwickelt als viele Alternativen wie Hugo oder Gatsby. Entsprechend ist die Dokumentation reif und im Problemfall gibt es massenhaft Material.
- Gibt es viele Themes und Plugins?
  - Auch mit SSGs ist das Erstellen eigener Templates aufwendig und oft unnötig. Es gibt viele gute, frei verfügbare Themes – einfach eines wählen und nutzen.
  - Ich arbeite primär mit C und Python; mit Rubys bzw. Gos Ökosystem bin ich weniger vertraut. Umso mehr wollte ich vorhandene Themes und Plugins nutzen.
  - Für Jekyll fand ich schnell ein ansprechendes Theme. Bei Hugo oder Gatsby schienen mir für persönliche Blogs weniger passende Themes verfügbar zu sein – wohl auch wegen der starken Nutzung von GitHub Pages durch Entwickler und der längeren Entwicklungszeit von Jekyll.

### 2-2. Theme-Auswahl
#### Minimal Mistakes (12021.01 - 12022.04)
- GitHub-Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo-Seite: <https://mmistakes.github.io/minimal-mistakes/>
- Theme, das ich ab Blogstart ca. 1 Jahr und 3 Monate verwendet habe
- Kommentare via Disqus, Discourse, utterances
- Kategorien- und Tag‑Klassifizierung
- Google Analytics out of the box
- Auswahl vordefinierter Skins
- Später bin ich auf das optisch ansprechendere Chirpy‑Theme umgestiegen. Minimal Mistakes ist zwar nicht „hübsch“, aber für einen techniklastigen Blog sauber und gut nutzbar.

#### Chirpy Jekyll Theme (12022.04 - aktuell)
- GitHub-Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo-Seite: <https://chirpy.cotes.page/>
- Seit dem Theme‑Wechsel im 12022.04 im Einsatz
- Mehrfachkategorien und Tags
- Formelsatz mit LaTeX über MathJax
- Diagramme mit Mermaid
- Kommentare via Disqus, Giscus
- Unterstützung für Google Analytics und GoatCounter
- Helles und dunkles Theme
- Zum Zeitpunkt des Wechsels unterstützte Minimal Mistakes MathJax und Mermaid nicht nativ; man musste es selbst ergänzen. Chirpy bringt beides ab Werk mit – kein großer, aber doch ein spürbarer Vorteil.
- Vor allem: das Design ist schön. Minimal Mistakes wirkt eher wie für Projektdokumentation oder Portfolios, während Chirpy gegenüber Plattformen wie Tistory, Medium oder Velog optisch locker mithält.

## 3. GitHub-Repository anlegen, bauen und deployen
Im Folgenden (Stand 12024.06) anhand des Chirpy Jekyll Theme; Git gilt als installiert.  
Siehe auch den [offiziellen Jekyll‑Installationsleitfaden](https://jekyllrb.com/docs/installation/) und die [offizielle Seite des Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Ruby & Jekyll installieren
Installiere Ruby und Jekyll gemäß dem [offiziellen Jekyll‑Installationsleitfaden](https://jekyllrb.com/docs/installation/) für dein Betriebssystem.

### 3-2. GitHub-Repository erstellen
Die [offizielle Seite des Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) beschreibt zwei Wege:
1. Kernbestandteile via "jekyll-theme-chirpy" Gem beziehen und übrige Ressourcen aus dem [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) Template holen
  - Vorteil: Upgrades lassen sich, wie unten beschrieben, leicht einspielen.
  - Nachteil: Für sehr umfangreiches Customizing evtl. unhandlich.
2. Das Repository [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) forken und als eigenes Blog‑Repo nutzen
  - Vorteil: Alle Dateien liegen direkt im eigenen Repo; ideal, um Code anzupassen und nicht unterstützte Features zu ergänzen.
  - Nachteil: Für Upgrades müssen [aktuelle Upstream‑Tags des Original‑Repos](https://github.com/cotes2020/jekyll-theme-chirpy/tags) gemergt werden; eigene Anpassungen können mit Upgrades kollidieren und müssen dann manuell aufgelöst werden.

Ich habe Methode 1 gewählt. Chirpy ist schon „out of the box“ sehr ausgereift; für die meisten Nutzer gibt es wenig zu customizen. Zudem wird es (Stand 12024) sehr aktiv weiterentwickelt. Wenn man das Theme nicht gerade stark umbaut, überwiegen die Vorteile, dem Upstream zeitnah zu folgen. Auch die offizielle Anleitung empfiehlt Methode 1 für die meisten.

### 3-3. Wichtige Einstellungen
In der Root‑Directory die Dateien `_config.yml`{: .filepath} sowie `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath} anpassen. Die Optionen sind gut kommentiert und intuitiv. Externe Schritte betreffen u. a. die Verifizierung für die Google Search Console sowie die Einbindung von Google Analytics oder GoatCounter. Das ist nicht kompliziert und hier nicht das Kernthema, daher ohne Details.

### 3-4. Lokal bauen
Nicht zwingend, aber praktisch zum Prüfen neuer Beiträge oder Änderungen. Im Root des lokalen Repos ein Terminal öffnen und:
```console
$ bundle exec jekyll s
```
Nach kurzer Zeit ist die Site lokal gebaut und unter <http://127.0.0.1:4000> erreichbar.

### 3-5. Deployen
Es gibt zwei Wege:
1. Mit GitHub Actions (bei Hosting auf GitHub Pages)
  - Beim GitHub Free Plan muss das Repository public sein
  - In der GitHub‑Weboberfläche den Tab *Settings* des Repositories öffnen, links *Code and automation > Pages* wählen und im Abschnitt **Source** die Option **GitHub Actions** aktivieren
  - Nach der Einrichtung wird bei jedem Push der *Build and Deploy*‑Workflow automatisch ausgeführt
2. Manuell bauen und deployen (anderer Hoster oder Self‑Hosting)
  - Mit folgendem Befehl die Site bauen:
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Die Build‑Artefakte im Verzeichnis `_site` auf den Server hochladen

## 4. Beiträge schreiben
Die [Schreibanleitung des Chirpy‑Themes](https://chirpy.cotes.page/posts/write-a-new-post/) dokumentiert Vorgehen und Optionen sehr gut. Darüber hinaus gibt es viele weitere Features – bei Bedarf dort nachlesen. Die Grundsyntax von GitHub Flavored Markdown habe ich zuvor in einem [separaten Beitrag](/posts/github-markdown-syntax-summary/) zusammengefasst. Hier die wichtigsten Punkte, die bei jedem Post zu beachten sind.

### Markdown-Datei anlegen
- Namensschema: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Ort: Verzeichnis `_posts`{: .filepath}

### Front Matter schreiben
Am Anfang der Markdown‑Datei muss das Front Matter passend ausgefüllt werden.
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
- **title**: Beitragstitel
- **description**: Kurzfassung. Falls nicht gesetzt, wird ein Auszug aus dem Text verwendet; für SEO empfiehlt es sich, die description‑Meta‑Angabe selbst sinnvoll zu formulieren. Richtwert: 135–160 Zeichen in lateinischer Schrift, 80–110 Zeichen auf Koreanisch.
- **date**: Exakte Erstellungszeit und Zeitzone (optional; ohne Angabe werden Dateizeitstempel genutzt)
- **categories**: Kategorien des Beitrags
- **tags**: Tags des Beitrags
- **image**: Vorschaubild oben im Beitrag
  - **path**: Pfad zur Bilddatei
  - **alt**: Alternativtext (optional)
- **toc**: Inhaltsverzeichnis in der rechten Sidebar aktivieren; Standard ist `true`
- **comments**: Kommentare für den einzelnen Beitrag unabhängig von der Site‑Voreinstellung explizit steuern
- **math**: Formelsatz mit [MathJax](https://www.mathjax.org/) aktivieren; standardmäßig aus Performancegründen deaktiviert (`false`)
- **mermaid**: Diagramme mit [Mermaid](https://github.com/mermaid-js/mermaid) aktivieren; standardmäßig deaktiviert (`false`)

## 5. Upgrade

Es gilt die Annahme, dass in [3-2](#3-2-github-repository-erstellen) Methode 1 verwendet wurde. Bei Methode 2 müssen, wie oben erwähnt, die neuesten Upstream‑Tags manuell gemergt werden.

1. `Gemfile`{: .filepath} bearbeiten und die Version des "jekyll-theme-chirpy" Gems aktualisieren.
2. Bei einem Major‑Upgrade können Kerndateien und Optionen, die nicht Teil des "jekyll-theme-chirpy" Gems sind, geändert worden sein. Prüfe die Änderungen über die folgende GitHub‑Compare‑Ansicht und übernimm sie manuell:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
