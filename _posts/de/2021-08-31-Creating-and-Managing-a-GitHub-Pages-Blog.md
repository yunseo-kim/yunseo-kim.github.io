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

## 1. Statische Website-Generatoren & Web-Hosting
### 1-1. Statische Webseiten vs Dynamische Webseiten
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
- Tools, die statische Webseiten basierend auf Rohdaten (meist Markdown-Textdateien) und vordefinierten Vorlagen generieren
- Automatisieren den Prozess des Erstellens und Bereitstellens von Webseiten, ohne dass einzelne HTML-Seiten manuell geschrieben werden müssen
- Beispiele: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Kostenloser Hosting-Service für statische Webseiten von GitHub
- Ermöglicht das Hosten einer persönlichen Hauptwebseite pro Konto und unbegrenzt viele projektbezogene Dokumentationsseiten pro Repository
- Nach Erstellung eines Repositories mit dem Namen '{username}.github.io' entsprechend dem GitHub-Benutzernamen können gebaute HTML-Seiten direkt gepusht oder GitHub Actions für den Build- und Bereitstellungsprozess genutzt werden
- Bei Besitz einer eigenen Domain kann diese in den Einstellungen verknüpft werden, um anstelle der Standard-Domain '{username}.github.io' eine andere Domainadresse zu verwenden

## 2. Auswahl des SSG und Themes

### Gründe für die Wahl von Jekyll
Es gibt verschiedene SSGs wie Jekyll, Hugo, Gatsby, aber ich habe mich für Jekyll entschieden. Die Kriterien, die ich bei der Auswahl des SSG berücksichtigt habe, und die Gründe für die Wahl von Jekyll sind wie folgt:
- Kann unnötige Versuch-und-Irrtum-Prozesse minimiert und der Fokus auf das Schreiben und Betreiben des Blogs gelegt werden?
  - Jekyll ist der offiziell von GitHub Pages unterstützte statische Website-Generator. Natürlich können auch andere SSGs wie Hugo oder Gatsby auf GitHub Pages gehostet werden, und es gibt auch die Option, ganz andere Hosting-Dienste wie Netlify zu nutzen. Aber für einen persönlichen Blog dieser Größenordnung ist es technisch gesehen nicht wirklich wichtig, mit welchem SSG er aufgebaut wurde oder wie schnell der Build-Prozess ist. Daher habe ich mich für die Option entschieden, die einfacher zu warten ist und für die es mehr Referenzdokumente gibt.
  - Jekyll hat auch die längste Entwicklungszeit im Vergleich zu Konkurrenten wie Hugo und Gatsby. Dementsprechend ist die Dokumentation gut und es gibt deutlich mehr Ressourcen, auf die man bei Problemen zurückgreifen kann.
- Gibt es eine Vielfalt an verfügbaren Themes und Plugins?
  - Auch wenn man einen SSG verwendet und nicht direkt HTML schreibt, ist es zeitaufwändig und unnötig, alle Templates selbst zu erstellen. Es gibt viele hervorragende Themes, die online verfügbar sind, und man kann einfach eines auswählen und verwenden, das einem gefällt.
  - Da ich hauptsächlich C oder Python verwende und mit Ruby (Jekyll) oder Go (Hugo) nicht vertraut bin, wollte ich bestehende Themes und Plugins aktiv nutzen.
  - Bei Jekyll konnte ich schnell ein Theme finden, das mir auf den ersten Blick gefiel, während es bei Hugo oder Gatsby vergleichsweise weniger Themes gab, die für persönliche Blogs geeignet schienen. Dies scheint stark von der Kompatibilität mit GitHub Pages, das von vielen Entwicklern für persönliche Blogs genutzt wird, und der längeren Entwicklungszeit beeinflusst zu sein.

### Theme-Auswahl
#### Minimal Mistakes (Januar 2021 - April 2022)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo-Seite: <https://mmistakes.github.io/minimal-mistakes/>
- Theme, das ich etwa 1 Jahr und 3 Monate lang nach der ersten Erstellung des Blogs verwendet habe
- Unterstützung für Kommentarfunktionen über Disqus, Discourse, utterances etc.
- Unterstützung für Kategorie- und Tag-Klassifizierung
- Integrierte Unterstützung für Google Analytics
- Auswahl vordefinierter Skins möglich
- Obwohl ich später zum Chirpy-Theme wechselte, das ein attraktiveres Design hat, war es für einen technischen Blog durchaus angemessen mit seinem schlichten, wenn auch nicht besonders schönen Design.

### Chirpy Jekyll Theme (seit April 2022)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo-Seite: <https://chirpy.cotes.page/>
- Theme, das ich seit April 2022 bis heute verwende
- Unterstützung für Mehrfachkategorien-Klassifizierung und Tags
- Integrierte Unterstützung für mathematische Ausdrücke mit LaTex-Syntax basierend auf MathJax
- Integrierte Unterstützung für Diagramme basierend auf Mermaid
- Unterstützung für Kommentarfunktionen über Disqus, Giscus etc.
- Unterstützung für Google Analytics, GoatCounter
- Unterstützung für helles und dunkles Theme
- Zum Zeitpunkt des Theme-Wechsels mussten MathJax oder Mermaid beim Minimal Mistakes Theme noch manuell durch Anpassungen hinzugefügt werden, während das Chirpy Theme diese Funktionen standardmäßig unterstützt. Auch wenn die Anpassungen nicht besonders kompliziert waren, ist dies ein kleiner Vorteil.
- Vor allem ist das Design schön. Während das Minimal Mistakes Theme zwar ordentlich ist, aber eine gewisse Steifheit hat, die eher für offizielle technische Dokumentationen oder Portfolio-Seiten geeignet scheint, ist der Vorteil des Chirpy Themes sein Design, das sich auch im Vergleich zu kommerziellen Blog-Plattformen wie Tistory, Medium oder velog sehen lassen kann.

## 3. GitHub Repository erstellen, bauen und bereitstellen
Die folgenden Anweisungen basieren auf dem aktuell (Juni 2024) verwendeten Chirpy Jekyll Theme und setzen voraus, dass Git bereits installiert ist.  
Siehe [offizielle Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) und [offizielle Chirpy Jekyll Theme-Seite](https://github.com/cotes2020/jekyll-theme-chirpy/wiki) für weitere Informationen.

### 3-1. Ruby & Jekyll installieren
Installieren Sie Ruby und Jekyll gemäß der [offiziellen Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) entsprechend Ihrem Betriebssystem.

### 3-2. GitHub Repository erstellen
Die [offizielle Chirpy Jekyll Theme-Seite](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) stellt zwei Methoden vor:
1. Kerndateien über das "jekyll-theme-chirpy" Gem importieren und die restlichen Ressourcen aus der [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) Vorlage beziehen
  - Vorteil: Einfachere Anwendung von Versions-Upgrades, wie später erläutert.
  - Nachteil: Eingeschränkte Anpassungsmöglichkeiten.
2. Das [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) Repository für Ihren Blog forken
  - Vorteil: Volle Kontrolle über alle Dateien im Repository ermöglicht freie Anpassungen, auch für Funktionen, die vom Theme nicht standardmäßig unterstützt werden.
  - Nachteil: Für Versions-Upgrades muss der [neueste Upstream-Tag des Original-Repositories](https://github.com/cotes2020/jekyll-theme-chirpy/tags) gemerged werden, was zu Konflikten mit eigenen Anpassungen führen kann, die manuell gelöst werden müssen.

Ich habe mich für Methode 1 entschieden. Das Chirpy Theme ist bereits sehr ausgereift, sodass die meisten Benutzer wenig Anpassungsbedarf haben. Zudem wird es Stand 2024 noch aktiv weiterentwickelt, weshalb die Vorteile des zeitnahen Folgens des Original-Upstreams die Vorteile eigener Anpassungen für die meisten Nutzer überwiegen. Der offizielle Leitfaden des Chirpy Themes empfiehlt ebenfalls Methode 1 für die meisten Benutzer.

### 3-3. Haupteinstellungen
Nehmen Sie die erforderlichen Einstellungen in den Dateien `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} und `_data/share.yml`{: .filepath} im Stammverzeichnis vor. Die Kommentare sind gut und die Einstellungen intuitiv, sodass sie ohne Schwierigkeiten angewendet werden können. Einstellungen, die externe Arbeiten erfordern, umfassen die Registrierung des Authentifizierungscodes für die Google Search Console-Integration und die Einbindung von Webmaster-Tools wie Google Analytics oder GoatCounter. Diese Verfahren sind jedoch nicht besonders komplex und nicht das Kernthema dieses Beitrags, daher werden detaillierte Erläuterungen ausgelassen.

### 3-4. Lokal bauen
Dies ist kein obligatorischer Schritt, aber Sie möchten vielleicht vorab überprüfen, ob neue Beiträge oder Änderungen an der Website korrekt im Web angezeigt werden. Öffnen Sie dazu ein Terminal im Stammverzeichnis des lokalen Repositories und führen Sie den folgenden Befehl aus:
```console
$ bundle exec jekyll s
```
Nach einigen Sekunden wird die Website lokal gebaut und das Ergebnis kann unter <http://127.0.0.1:4000> eingesehen werden.

### 3-5. Bereitstellen
Es gibt zwei Methoden:
1. Nutzung von GitHub Actions (bei Hosting auf GitHub Pages)
  - Bei Verwendung des GitHub Free Plans muss das Repository öffentlich bleiben
  - Wählen Sie auf der GitHub-Webseite den *Settings*-Tab des Repositories, klicken Sie in der linken Navigationsleiste auf *Code and automation > Pages* und wählen Sie im Abschnitt **Source** die Option **GitHub Actions**
  - Nach der Einrichtung wird der *Build and Deploy* Workflow bei jedem neuen Commit automatisch ausgeführt
2. Manueller Build und Bereitstellung (bei Nutzung anderer Hosting-Dienste oder Self-Hosting)
  - Führen Sie den folgenden Befehl aus, um die Website manuell zu bauen:
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Laden Sie die Build-Ergebnisse aus dem `_site`-Verzeichnis auf Ihren Server hoch

## 4. Beiträge verfassen
Der [Leitfaden zum Verfassen von Beiträgen](https://chirpy.cotes.page/posts/write-a-new-post/) des Chirpy Themes dokumentiert gut, wie Beiträge verfasst werden und welche Optionen verfügbar sind. Neben den hier beschriebenen Punkten bietet er verschiedene Funktionen, die nützliche Referenzen darstellen. Hier werden die wichtigsten Punkte zusammengefasst, die bei jedem Beitrag zu beachten sind.

### Markdown-Datei erstellen
- Namensformat: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Speicherort: `_posts`{: .filepath} Verzeichnis

### Front Matter verfassen
Am Anfang der Markdown-Datei muss ein entsprechendes Front Matter erstellt werden.
```YAML
---
title: