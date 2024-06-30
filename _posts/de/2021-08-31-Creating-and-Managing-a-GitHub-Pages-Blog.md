---
title: "GitHub Pages Blog erstellen und verwalten"
description: >-
  Lernen Sie die Eigenschaften und Unterschiede von statischen und dynamischen Webseiten sowie statische Website-Generatoren kennen und hosten Sie einen Jekyll-Blog auf GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
---

Anfang 2021 begann ich, einen Blog mit Jekyll auf GitHub Pages zu hosten. Da ich den Installationsprozess beim Aufbau des Blogs nicht richtig dokumentiert hatte, gab es später bei der Wartung einige Schwierigkeiten. Deshalb habe ich mich entschlossen, den Installationsprozess und die Wartungsmethoden zumindest kurz zusammenzufassen.  
~~Tatsächlich liegt es hauptsächlich daran, dass ich mich mit dem Hosting statischer Websites noch nicht so gut auskenne.~~
(Inhalt aktualisiert im Juni 2024)

## 1. Statische Website-Generatoren & Web-Hosting
### 1-1. Statische vs. Dynamische Webseiten
#### Statische Webseiten
- Webseiten, die auf dem Server gespeicherte Daten unverändert an den Benutzer übermitteln
- Der Webserver liefert vorgefertigte Seiten entsprechend der Benutzeranfrage
- Benutzer sehen die gleiche Webseite, solange die auf dem Server gespeicherten Daten nicht geändert werden
- Generell schnelle Antwortzeiten, da nur die angeforderte Datei übertragen werden muss
- Kostengünstig in der Einrichtung, da nur ein Webserver benötigt wird
- Begrenzte Servicemöglichkeiten, da nur gespeicherte Informationen angezeigt werden
- Manuelle Verwaltung von Datenergänzungen, -änderungen und -löschungen durch den Administrator
- Tendenziell vorteilhafter für Suchmaschinenoptimierung (SEO) aufgrund der einfacheren Struktur für Crawler

#### Dynamische Webseiten
- Webseiten, die auf dem Server gespeicherte Daten durch Skripte verarbeiten und übermitteln
- Der Webserver interpretiert die Benutzeranfrage, verarbeitet die Daten und liefert die generierte Webseite
- Benutzer sehen je nach Situation, Zeit und Anfrage unterschiedliche Webseiten
- Relativ langsamere Antwortzeiten aufgrund der Skriptverarbeitung vor der Seitenauslieferung
- Höhere Einrichtungskosten, da neben dem Webserver auch ein Anwendungsserver benötigt wird
- Vielfältige Servicemöglichkeiten durch dynamische Kombination verschiedener Informationen
- Benutzer können je nach Webseitenstruktur Daten direkt im Browser hinzufügen, ändern oder löschen

### 1-2. Statische Website-Generatoren (SSG, Static Site Generator)
- Tools zur Erstellung statischer Webseiten basierend auf Rohdaten (meist Markdown-Textdateien) und vordefinierten Templates
- Automatisieren den Prozess der Webseitenerstellung und -veröffentlichung ohne manuelle HTML-Kodierung
- Beispiele: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Kostenloser Hosting-Service für statische Webseiten von GitHub
- Ermöglicht eine persönliche Hauptwebseite pro Konto und unbegrenzte projektbezogene Dokumentationsseiten pro Repository
- Erstellung eines Repositories mit dem Namen '{username}.github.io' entsprechend dem GitHub-Benutzernamen
- Direkte Push-Möglichkeit von gebauten HTML-Seiten oder Nutzung von GitHub Actions für Build und Deployment
- Option zur Verwendung einer eigenen Domain anstelle der Standard-Domain '{username}.github.io'

## 2. Auswahl des SSG und Themes

### Gründe für die Wahl von Jekyll
Bei der Auswahl des SSG wurden folgende Kriterien berücksichtigt:
- Minimierung unnötiger Fehlersuche und Fokussierung auf Schreiben und Blogbetrieb?
  - Jekyll ist der offiziell unterstützte statische Website-Generator für GitHub Pages
  - Längste Entwicklungszeit unter den Konkurrenten, daher umfangreiche Dokumentation und Ressourcen
- Vielfalt an verfügbaren Themes und Plugins?
  - Große Auswahl an geeigneten Themes für persönliche Blogs
  - Umfangreiche Plugins für zusätzliche Funktionalitäten

### Theme-Auswahl
#### Minimal Mistakes (Januar 2021 - April 2022)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo-Seite: <https://mmistakes.github.io/minimal-mistakes/>
- Verwendet für etwa 1 Jahr und 3 Monate
- Unterstützung für Kommentarfunktionen (Disqus, Discourse, utterances)
- Kategorie- und Tag-Funktionalität
- Integrierte Google Analytics-Unterstützung
- Auswahl vordefinierter Skins

### Chirpy Jekyll Theme (seit April 2022)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo-Seite: <https://chirpy.cotes.page/>
- Aktuell verwendetes Theme seit April 2022
- Unterstützung für Mehrfachkategorien und Tags
- Integrierte LaTex-Formeldarstellung mit MathJax
- Integrierte Diagrammfunktion basierend auf Mermaid
- Kommentarfunktionen (Disqus, Giscus)
- Google Analytics und GoatCounter-Unterstützung
- Helles und dunkles Theme
- Ästhetisch ansprechendes Design, vergleichbar mit kommerziellen Blog-Plattformen

## 3. GitHub Repository erstellen, bauen und deployen
Basierend auf dem aktuell (Juni 2024) verwendeten Chirpy Jekyll Theme. Es wird vorausgesetzt, dass Git bereits installiert ist.

### 3-1. Ruby & Jekyll installieren
Folgen Sie der [offiziellen Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) entsprechend Ihrem Betriebssystem.

### 3-2. GitHub Repository erstellen
Die [offizielle Chirpy Jekyll Theme-Seite](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) bietet zwei Methoden:
1. Verwendung des "jekyll-theme-chirpy" Gems und des [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) Templates
2. Forken des [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) Repositories

Ich habe Methode 1 gewählt aufgrund der einfacheren Versionsaktualisierung und der hohen Grundfunktionalität des Chirpy-Themes.

### 3-3. Hauptkonfigurationen
Passen Sie die Einstellungen in `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} und `_data/share.yml`{: .filepath} an.

### 3-4. Lokaler Build
Führen Sie im Root-Verzeichnis des lokalen Repositories folgenden Befehl aus:
```console
$ bundle exec jekyll s
```
Die Ergebnisse können unter <http://127.0.0.1:4000> eingesehen werden.

### 3-5. Deployment
Zwei Möglichkeiten:
1. Nutzung von GitHub Actions (für GitHub Pages Hosting)
2. Manueller Build und Upload (für andere Hosting-Dienste oder Self-Hosting)

## 4. Beiträge verfassen
Detaillierte Anweisungen finden Sie im [Beitragsschreib-Leitfaden](https://chirpy.cotes.page/posts/write-a-new-post/) des Chirpy-Themes.

### Markdown-Datei erstellen
- Namensformat: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Speicherort: `_posts`{: .filepath} Verzeichnis

### Front Matter verfassen
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]     # TAG-Namen sollten immer kleingeschrieben sein
---
```

## 5. Upgrade

Für Methode 1 aus Abschnitt 3-2:

1. Aktualisieren Sie die Version des "jekyll-theme-chirpy" Gems in der `Gemfile`{: .filepath}.
2. Bei Major-Upgrades überprüfen Sie Änderungen an Kerndateien und Konfigurationsoptionen mit der GitHub API:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<ältere_version>...<neuere_version>
  ```