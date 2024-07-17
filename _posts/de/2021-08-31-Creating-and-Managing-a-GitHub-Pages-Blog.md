---
title: "Erstellen und Verwalten eines GitHub Pages Blogs"
description: >-
  Erfahren Sie mehr über die Eigenschaften und Unterschiede von statischen und dynamischen Webseiten, statischen Website-Generatoren und hosten Sie einen Jekyll-Blog auf GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
---

Seit Anfang 2021 hoste ich meinen Blog mit Jekyll auf GitHub Pages. Da ich den Installationsprozess beim Aufbau des Blogs nicht richtig dokumentiert hatte, gab es bei der späteren Wartung einige Schwierigkeiten. Deshalb habe ich mich entschlossen, den Installationsprozess und die Wartungsmethoden zumindest kurz zusammenzufassen.  
~~Tatsächlich liegt es hauptsächlich daran, dass ich mich mit dem Hosting statischer Websites noch nicht so gut auskenne.~~
(Inhalt aktualisiert im Juni 2024)

## 1. Statische Site-Generatoren & Web-Hosting
### 1-1. Statische Webseiten vs. Dynamische Webseiten
#### Statische Webseiten (Static Web Pages)
- Webseiten, die auf dem Server gespeicherte Daten unverändert an den Benutzer übermitteln
- Der Webserver liefert dem Benutzer die vorher gespeicherte Seite entsprechend seiner Anfrage
- Benutzer sehen die gleiche Webseite, solange die auf dem Server gespeicherten Daten nicht geändert werden
- Da nur die angeforderte Datei übertragen werden muss, ist keine zusätzliche Verarbeitung erforderlich, was in der Regel zu schnelleren Antwortzeiten führt
- Bestehen nur aus einfachen Dateien, sodass nur ein Webserver eingerichtet werden muss, was die Einrichtungskosten niedrig hält
- Zeigen nur gespeicherte Informationen an, daher sind die Dienste begrenzt
- Hinzufügen, Ändern und Löschen von Daten muss manuell vom Administrator durchgeführt werden
- Struktur ist für Suchmaschinen leichter zu crawlen, was für die Suchmaschinenoptimierung (SEO) relativ vorteilhaft ist

#### Dynamische Webseiten (Dynamic Web Pages)
- Webseiten, die auf dem Server gespeicherte Daten durch Skripte verarbeiten und übermitteln
- Der Webserver interpretiert die Benutzeranfrage, verarbeitet die Daten und liefert die generierte Webseite
- Benutzer sehen Webseiten, die sich je nach Situation, Zeit und Anfrage ändern
- Antworten sind relativ langsamer, da Skripte zur Bereitstellung der Webseite verarbeitet werden müssen
- Zusätzliche Kosten entstehen bei der Einrichtung, da neben dem Webserver auch ein Anwendungsserver benötigt wird
- Ermöglichen vielfältige Dienste durch dynamische Bereitstellung verschiedener Informationskombinationen
- Je nach Webseitenstruktur können Benutzer Daten direkt im Browser hinzufügen, ändern und löschen

### 1-2. Statische Website-Generatoren (SSG, Static Site Generator)
- Tools, die statische Webseiten basierend auf Rohdaten (meist Markdown-Textdateien) und vordefinierten Templates generieren
- Automatisieren den Prozess des Erstellens und Bereitstellens von Webseiten, ohne dass einzelne HTML-Seiten manuell geschrieben werden müssen
- Beispiele: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Kostenloser Hosting-Service für statische Webseiten von GitHub
- Ermöglicht das Hosten einer persönlichen Hauptwebseite pro Konto und unbegrenzt viele projektbezogene Dokumentationsseiten pro Repository
- Nach Erstellung eines Repositories mit dem Namen '{username}.github.io' können gebaute HTML-Seiten direkt gepusht oder GitHub Actions für den Build- und Bereitstellungsprozess genutzt werden
- Bei Besitz einer eigenen Domain kann diese in den Einstellungen verknüpft werden, um anstelle der Standard-Domain '{username}.github.io' eine andere Domainadresse zu verwenden

## 2. Auswahl des SSG und Themes

### 2-1. Gründe für die Wahl von Jekyll
Es gibt verschiedene SSGs wie Jekyll, Hugo, Gatsby, aber ich habe mich für Jekyll entschieden. Die Kriterien bei der Auswahl und die Gründe für Jekyll waren:
- Minimierung unnötiger Fehlersuche und Fokussierung auf das Schreiben und Betreiben des Blogs?
  - Jekyll ist der offiziell unterstützte statische Website-Generator für GitHub Pages. Obwohl auch andere SSGs wie Hugo oder Gatsby auf GitHub Pages gehostet werden können oder sogar andere Hosting-Dienste wie Netlify genutzt werden könnten, ist für den Betrieb eines persönlichen Blogs dieser Größenordnung die technische Umsetzung, Buildgeschwindigkeit und Leistung nicht so entscheidend. Daher erschien es sinnvoll, etwas zu wählen, das einfacher zu warten ist und mehr Dokumentation zur Verfügung hat.
  - Jekyll hat auch die längste Entwicklungszeit im Vergleich zu Konkurrenten wie Hugo oder Gatsby. Entsprechend ist die Dokumentation gut und es gibt deutlich mehr Ressourcen, auf die man bei Problemen zurückgreifen kann.
- Vielfalt an verfügbaren Themes und Plugins?
  - Auch wenn man einen SSG verwendet und nicht direkt HTML schreibt, ist es zeitaufwändig und unnötig, alle Templates selbst zu erstellen. Es gibt viele hervorragende Themes online, die man nutzen kann.
  - Da ich hauptsächlich C oder Python verwende und mit Ruby (Jekyll) oder Go (Hugo) nicht vertraut bin, wollte ich bestehende Themes und Plugins intensiv nutzen.
  - Bei Jekyll fand ich schnell ein ansprechendes Theme, während Hugo und Gatsby vergleichsweise weniger geeignete Themes für persönliche Blogs zu haben schienen. Dies hängt wahrscheinlich mit der oben erwähnten Kompatibilität zu GitHub Pages und der längeren Entwicklungszeit zusammen.

### 2-2. Theme-Auswahl
#### Minimal Mistakes (Januar 2021 - April 2022)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo-Seite: <https://mmistakes.github.io/minimal-mistakes/>
- Theme, das ich etwa 1 Jahr und 3 Monate nach der ersten Blogerstellung verwendete
- Unterstützung für Kommentarfunktionen über Disqus, Discourse, utterances etc.
- Unterstützung für Kategorie- und Tag-Klassifizierung
- Integrierte Unterstützung für Google Analytics
- Auswahl vordefinierter Skins möglich
- Obwohl ich später zum Chirpy-Theme wechselte, das ein ansprechenderes Design hat, war es für einen technischen Blog durchaus brauchbar mit seinem schlichten, wenn auch nicht besonders schönen Design.

#### Chirpy Jekyll Theme (seit April 2022)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo-Seite: <https://chirpy.cotes.page/>
- Theme, das ich seit April 2022 bis heute verwende
- Unterstützung für Mehrfachkategorien und Tags
- Integrierte Unterstützung für LaTeX-Formeln basierend auf MathJax
- Integrierte Unterstützung für Diagramme basierend auf Mermaid
- Unterstützung für Kommentarfunktionen über Disqus, Giscus etc.
- Unterstützung für Google Analytics, GoatCounter
- Unterstützung für helles und dunkles Theme
- Zum Zeitpunkt des Themenwechsels mussten MathJax und Mermaid beim Minimal Mistakes Theme noch manuell hinzugefügt werden, während das Chirpy Theme diese standardmäßig unterstützt. Auch wenn die Anpassung nicht besonders aufwändig war, ist dies ein kleiner Vorteil.
- Vor allem ist das Design ansprechend. Während Minimal Mistakes zwar ordentlich, aber eher für offizielle technische Dokumentationen oder Portfolio-Seiten geeignet scheint, kann sich das Chirpy Theme durchaus mit kommerziellen Blog-Plattformen wie Tistory, Medium oder velog messen.

## 3. GitHub Repository erstellen, bauen und bereitstellen
Basierend auf dem aktuell (Juni 2024) verwendeten Chirpy Jekyll Theme, unter der Annahme, dass Git bereits installiert ist.  
Siehe [offizielle Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) und [offizielle Chirpy Jekyll Theme-Seite](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Ruby & Jekyll installieren
Installieren Sie Ruby und Jekyll gemäß der [offiziellen Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) entsprechend Ihrem Betriebssystem.

### 3-2. GitHub Repository erstellen
Die [offizielle Chirpy Jekyll Theme-Seite](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) stellt zwei Methoden vor:
1. Kerndateien über das "jekyll-theme-chirpy" Gem importieren und restliche Ressourcen aus der [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) Vorlage beziehen
  - Vorteil: Einfachere Anwendung von Versions-Upgrades.
  - Nachteil: Eingeschränkte Anpassungsmöglichkeiten.
2. Das [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) Repository für den eigenen Blog forken
  - Vorteil: Volle Kontrolle über alle Dateien ermöglicht freie Anpassungen, auch über die vom Theme unterstützten Funktionen hinaus.
  - Nachteil: Für Versions-Upgrades muss der [neueste Upstream-Tag des Originalrepositorys](https://github.com/cotes2020/jekyll-theme-chirpy/tags) gemergt werden, was zu Konflikten mit eigenen Anpassungen führen kann, die manuell gelöst werden müssen.

Ich habe mich für Methode 1 entschieden. Das Chirpy Theme ist bereits sehr ausgereift, sodass die meisten Nutzer wenig Anpassungsbedarf haben. Zudem wird es bis 2024 aktiv weiterentwickelt, weshalb die Vorteile regelmäßiger Updates die Nachteile eingeschränkter Anpassungsmöglichkeiten überwiegen, sofern keine umfangreichen Modifikationen geplant sind. Die offizielle Anleitung des Chirpy Themes empfiehlt ebenfalls Methode 1 für die meisten Nutzer.

### 3-3. Haupteinstellungen
Passen Sie die notwendigen Einstellungen in den Dateien `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} und `_data/share.yml`{: .filepath} im Stammverzeichnis an. Die Kommentare sind hilfreich und die Einstellungen intuitiv, sodass die Anpassung problemlos möglich ist. Externe Arbeiten sind hauptsächlich für die Einbindung von Google Search Console (Authentifizierungscode) und Webmaster-Tools wie Google Analytics oder GoatCounter erforderlich. Diese Prozesse sind jedoch relativ unkompliziert und nicht Kernthema dieses Beitrags, daher werden sie hier nicht detailliert behandelt.

### 3-4. Lokaler Build
Obwohl nicht zwingend erforderlich, möchten Sie vielleicht vor der Veröffentlichung neuer Beiträge oder Änderungen prüfen, ob diese korrekt angezeigt werden. Öffnen Sie dazu ein Terminal im Stammverzeichnis Ihres lokalen Repositories und führen Sie folgenden Befehl aus:
```console
$ bundle exec jekyll s
```
Nach einigen Sekunden ist die Seite lokal gebaut und unter <http://127.0.0.1:4000> einsehbar.

### 3-5. Bereitstellung
Es gibt zwei Möglichkeiten:
1. Nutzung von GitHub Actions (bei Hosting auf GitHub Pages)
  - Bei Verwendung des GitHub Free Plans muss das Repository öffentlich sein
  - Wählen Sie auf der GitHub-Webseite im Repository den Tab *Settings*, klicken Sie in der linken Navigationsleiste auf *Code and automation > Pages* und wählen Sie im Abschnitt **Source** die Option **GitHub Actions**
  - Nach der Einrichtung wird der *Build and Deploy* Workflow bei jedem neuen Commit automatisch ausgeführt
2. Manueller Build und Bereitstellung (bei Nutzung anderer Hosting-Dienste oder Self-Hosting)
  - Führen Sie folgenden Befehl aus, um die Seite manuell zu bauen:
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Laden Sie die Ergebnisse aus dem `_site` Verzeichnis auf Ihren Server hoch

## 4. Beiträge verfassen
Die [Anleitung zum Verfassen von Beiträgen](https://chirpy.cotes.page/posts/write-a-new-post/) des Chirpy Themes dokumentiert ausführlich die Methoden und verfügbaren Optionen. Hier werden die wichtigsten Punkte zusammengefasst, die bei jedem Beitrag zu beachten sind.

### Markdown-Datei erstellen
- Namensformat: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Speicherort: `_posts`{: .filepath} Verzeichnis

### Front Matter verfassen
Am Anfang der Markdown-Datei muss ein entsprechendes Front Matter eingefügt werden:
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]     # TAG names should always be lowercase
---
```
- **title**: Beitragstitel
- **description**: Zusammenfassung. Wenn nicht angegeben, wird automatisch ein Teil des Haupttextes verwendet. Für SEO wird empfohlen, den description Meta-Tag selbst zu verfassen. Idealerweise 135-160 Zeichen für lateinische Schrift, 80-110 Zeichen für Hangul.
- **date**: Genaues Erstellungsdatum und -zeit mit Zeitzone (optional, bei Auslassung wird die Information aus dem Dateinamen automatisch verwendet)
- **categories**: Kategorisierung des Beitrags
- **tags**: Tags für den Beit