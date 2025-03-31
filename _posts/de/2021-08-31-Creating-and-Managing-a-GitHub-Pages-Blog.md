---
title: GitHub Pages Blog erstellen und verwalten
description: Erfahren Sie mehr über die Eigenschaften und Unterschiede von statischen und dynamischen Webseiten sowie über statische Website-Generatoren und hosten Sie einen Jekyll-Blog auf GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---
Seit Anfang des [Holozän-Kalenders](https://en.wikipedia.org/wiki/Holocene_calendar) 12021 habe ich begonnen, einen Blog mit Jekyll auf GitHub Pages zu hosten. Da ich den Installationsprozess beim Aufbau des Blogs nicht richtig dokumentiert hatte, gab es später bei der Wartung einige Schwierigkeiten. Deshalb habe ich beschlossen, den Installationsprozess und die Wartungsmethoden zumindest kurz zusammenzufassen.

(+ 12024.12 Inhalt aktualisiert)

## 1. Statischer Site-Generator & Web-Hosting
### 1-1. Statische Webseite vs. Dynamische Webseite
#### Statische Webseite (Static Web Page)
- Eine Webseite, die auf dem Server gespeicherte Daten unverändert an den Benutzer überträgt
- Der Webserver liefert eine vorher gespeicherte Seite entsprechend der Benutzeranfrage
- Benutzer sehen die gleiche Webseite, solange die auf dem Server gespeicherten Daten nicht geändert werden
- Da nur die angeforderte Datei übertragen werden muss, ist keine zusätzliche Verarbeitung erforderlich, was in der Regel zu schnelleren Antwortzeiten führt
- Besteht nur aus einfachen Dateien, sodass nur ein Webserver eingerichtet werden muss, was die Einrichtungskosten niedrig hält
- Zeigt nur gespeicherte Informationen an, daher sind die Dienste begrenzt
- Hinzufügen, Ändern und Löschen von Daten muss manuell vom Administrator durchgeführt werden
- Struktur ist für Suchmaschinen leichter zu crawlen, was relativ vorteilhaft für die Suchmaschinenoptimierung (SEO) ist

#### Dynamische Webseite (Dynamic Web Page)
- Eine Webseite, die auf dem Server gespeicherte Daten durch Skripte verarbeitet und überträgt
- Der Webserver interpretiert die Benutzeranfrage, verarbeitet die Daten und liefert dann die generierte Webseite
- Benutzer sehen Webseiten, die sich je nach Situation, Zeit und Anfrage ändern
- Relativ langsamere Antwortzeiten, da Skripte zur Bereitstellung der Webseite verarbeitet werden müssen
- Zusätzliche Kosten bei der Einrichtung, da neben dem Webserver auch ein Anwendungsserver erforderlich ist
- Ermöglicht vielfältige Dienste durch dynamische Bereitstellung verschiedener Informationskombinationen
- Je nach Webseitenstruktur können Benutzer Daten direkt im Browser hinzufügen, ändern und löschen

### 1-2. Statischer Site-Generator (SSG, Static Site Generator)
- Ein Werkzeug, das statische Webseiten basierend auf Rohdaten (meist Textdateien im Markdown-Format) und vordefinierten Vorlagen generiert
- Automatisiert den Prozess des Erstellens und Bereitstellens von Webseiten, ohne dass einzelne HTML-Seiten manuell geschrieben werden müssen
- Beispiele: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Ein kostenloser Hosting-Service für statische Webseiten, angeboten von GitHub
- Ermöglicht das Hosten einer persönlichen Hauptwebseite pro Konto und unbegrenzt viele projektbezogene Dokumentationsseiten pro Repository
- Nach Erstellung eines Repositories mit dem Namen '{username}.github.io' entsprechend dem eigenen GitHub-Benutzernamen können gebaute HTML-Seiten direkt gepusht oder GitHub Actions für den Build- und Bereitstellungsprozess genutzt werden
- Bei Besitz einer eigenen Domain kann diese in den Einstellungen verknüpft werden, um anstelle der Standard-Domain '{username}.github.io' eine andere Domainadresse zu verwenden

## 2. Auswahl des zu verwendenden SSG und Themes

### 2-1. Gründe für die Wahl von Jekyll
Es gibt verschiedene SSGs wie Jekyll, Hugo, Gatsby usw., aber ich habe mich für Jekyll entschieden. Die Kriterien, die ich bei der Auswahl des SSG berücksichtigt habe, und die Gründe für die Wahl von Jekyll sind wie folgt:
- Kann unnötige Versuch-und-Irrtum-Phasen minimiert und der Fokus auf das Schreiben von Beiträgen und den Betrieb des Blogs gelegt werden?
  - Jekyll ist der offiziell unterstützte statische Website-Generator für GitHub Pages. Natürlich können auch andere SSGs wie Hugo, Gatsby usw. auf GitHub Pages gehostet werden, und es besteht auch die Option, ganz andere Hosting-Dienste wie Netlify zu nutzen. Aber für den Betrieb eines persönlichen Blogs dieser Größenordnung ist es technisch gesehen nicht wirklich wichtig, mit welchem SSG er aufgebaut wurde oder wie die Build-Geschwindigkeit und Leistung sind. Daher habe ich mich für die Option entschieden, die einfacher zu warten ist und für die es mehr Referenzdokumente gibt.
  - Jekyll hat auch die längste Entwicklungszeit im Vergleich zu Konkurrenten wie Hugo und Gatsby. Dementsprechend ist die Dokumentation gut und es gibt eine überwältigende Menge an Referenzmaterial, auf das man bei Problemen zurückgreifen kann.
- Gibt es eine Vielfalt an verfügbaren Themes und Plugins?
  - Auch wenn man keinen SSG verwendet und HTML direkt schreibt, ist es umständlich und zeitaufwendig, alle Vorlagen selbst zu erstellen, und es ist auch nicht wirklich notwendig. Es gibt bereits viele hervorragende Themes im Web, die man einfach auswählen und nutzen kann.
  - Da ich ursprünglich hauptsächlich C oder Python verwendet habe und mit Ruby von Jekyll oder Go von Hugo nicht so vertraut bin, wollte ich umso mehr die bereits entwickelten Themes und Plugins aktiv nutzen.
  - Bei Jekyll konnte ich schnell ein Theme finden, das mir auf den ersten Blick gefiel, während es bei Hugo oder Gatsby relativ weniger Themes gab, die für den Zweck eines persönlichen Blogs geeignet waren. Wie bereits erwähnt, scheinen die Kompatibilität mit GitHub Pages, die von vielen Entwicklern für das Hosten persönlicher Blogs genutzt wird, und die Entwicklungszeit hier einen großen Einfluss gehabt zu haben.

### 2-2. Theme-Auswahl
#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo-Seite: <https://mmistakes.github.io/minimal-mistakes/>
- Theme, das ich etwa 1 Jahr und 3 Monate lang nach der ersten Erstellung des Blogs verwendet habe
- Unterstützung für Kommentarfunktionen über Disqus, Discourse, utterances usw.
- Unterstützung für Kategorie- und Tag-Klassifizierungsfunktionen
- Grundlegende Unterstützung für Google Analytics
- Auswahl vordefinierter Skins möglich
- Obwohl ich später das Chirpy-Theme entdeckt und gewechselt habe, das ein eleganteres und ansprechenderes Design hat, war es angesichts der Tatsache, dass es sich um einen technischen Blog handelt, zwar nicht hübsch, aber durchaus brauchbar mit seinem einigermaßen sauberen Design.

#### Chirpy Jekyll Theme (12022.04 - Gegenwart)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo-Seite: <https://chirpy.cotes.page/>
- Theme, das ich seit dem Wechsel im April 12022 bis heute verwende
- Unterstützung für Mehrfachkategorien-Klassifizierung und Tag-Funktionen
- Grundlegende Unterstützung für mathematische Ausdrücke in LaTex-Syntax basierend auf MathJax
- Grundlegende Unterstützung für Diagrammfunktionen basierend auf Mermaid
- Unterstützung für Kommentarfunktionen über Disqus, Giscus usw.
- Unterstützung für Google Analytics, GoatCounter
- Unterstützung für helles und dunkles Theme
- Zum Zeitpunkt des Theme-Wechsels wurden MathJax oder Mermaid vom Minimal Mistakes Theme nicht nativ unterstützt und mussten durch eigene Anpassungen hinzugefügt werden, während das Chirpy Theme diese von Haus aus unterstützt. Obwohl die Anpassungen nicht besonders kompliziert waren, ist dies dennoch ein kleiner Vorteil.
- Vor allem ist das Design schön. Während das Minimal Mistakes Theme zwar sauber ist, hat es eine gewisse Steifheit, die eher für offizielle technische Dokumentationen von Projekten oder Portfolio-Seiten geeignet scheint. Das Chirpy Theme hingegen hat den Vorteil eines Designs, das sich im Vergleich zu kommerziellen Blog-Plattformen wie Tistory, Medium oder velog nicht zu verstecken braucht.

## 3. GitHub Repository erstellen, bauen und bereitstellen
Dies wird basierend auf dem aktuell (12024.06) verwendeten Chirpy Jekyll Theme beschrieben, unter der Annahme, dass Git bereits installiert ist.  
Siehe [offizielle Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) und [offizielle Chirpy Jekyll Theme-Seite](https://github.com/cotes2020/jekyll-theme-chirpy/wiki) für Referenzen.

### 3-1. Ruby & Jekyll installieren
Installieren Sie Ruby und Jekyll gemäß der [offiziellen Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) entsprechend Ihrer Betriebssystemumgebung.

### 3-2. GitHub Repository erstellen
Die [offizielle Chirpy Jekyll Theme-Seite](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) stellt die folgenden zwei Methoden vor:
1. Methode, bei der die Kerndateien über das "jekyll-theme-chirpy" Gem importiert und die restlichen Ressourcen aus der [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) Vorlage bezogen werden
  - Vorteil: Wie später erläutert, ist die Anwendung von Versions-Upgrades einfach.
  - Nachteil: Anpassungen sind eingeschränkt.
2. Methode, bei der das [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) Repository als eigenes Blog-Repository geforkt wird
  - Vorteil: Da alle Dateien direkt im Repository verwaltet werden, können auch Funktionen, die vom Theme nicht unterstützt werden, durch direkte Codeänderungen frei angepasst werden.
  - Nachteil: Um ein Versions-Upgrade anzuwenden, muss der [neueste Upstream-Tag des Original-Repositories](https://github.com/cotes2020/jekyll-theme-chirpy/tags) gemergt werden, was je nach Fall zu Konflikten mit selbst angepasstem Code führen kann. In diesem Fall müssen diese Konflikte manuell gelöst werden.

Ich habe mich für Methode 1 entschieden. Da das Chirpy Theme grundsätzlich eine hohe Vollständigkeit aufweist, gibt es für die meisten Benutzer nicht viel anzupassen. Zudem ist die Entwicklung und Funktionsverbesserung bis 12024 sehr aktiv, sodass die Vorteile des rechtzeitigen Folgens des Original-Upstreams die Vorteile direkter Anpassungen überwiegen, es sei denn, man plant umfangreiche Modifikationen. Auch der offizielle Leitfaden des Chirpy Themes empfiehlt Methode 1 für die meisten Benutzer.

### 3-3. Haupteinstellungen
Nehmen Sie die erforderlichen Einstellungen in den Dateien `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} und `_data/share.yml`{: .filepath} im Stammverzeichnis vor. Die Kommentare sind gut geschrieben und die Einstellungen sind intuitiv, sodass sie ohne besondere Schwierigkeiten angewendet werden können. Die einzigen Einstellungen, die separate externe Arbeiten erfordern, sind die Registrierung des Authentifizierungscodes für die Integration mit Google Search Console und die Verknüpfung von Webmaster-Tools wie Google Analytics oder GoatCounter. Aber auch diese Verfahren sind nicht wirklich kompliziert und da sie nicht das Kernthema dieses Artikels sind, wird auf eine detaillierte Beschreibung verzichtet.

### 3-4. Lokal bauen
Dies ist kein obligatorischer Schritt, aber man möchte vielleicht vorher überprüfen, ob neue Beiträge oder Änderungen an der Website korrekt im Web angezeigt werden. In diesem Fall öffnen Sie ein Terminal im Stammverzeichnis des lokalen Repositories und führen Sie den folgenden Befehl aus:
```console
$ bundle exec jekyll s
```
Nach einigen Sekunden wird die Website lokal gebaut und das Ergebnis kann unter der Adresse <http://127.0.0.1:4000> überprüft werden.

### 3-5. Bereitstellen
Es gibt zwei Methoden:
1. Nutzung von GitHub Actions (bei Hosting auf GitHub Pages)
  - Bei Verwendung des GitHub Free Plans muss das Repository öffentlich bleiben
  - Wählen Sie auf der GitHub-Webseite den *Settings* Tab des Repositories, klicken Sie dann in der linken Navigationsleiste auf *Code and automation > Pages* und wählen Sie im Abschnitt **Source** die Option **GitHub Actions**
  - Nach Abschluss der Einrichtung wird der *Build and Deploy* Workflow bei jedem neuen Commit-Push automatisch ausgeführt
2. Direkter Build und Bereitstellung (bei Nutzung anderer Hosting-Dienste oder Self-Hosting)
  - Führen Sie den folgenden Befehl aus, um die Website direkt zu bauen
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Laden Sie die Build-Ergebnisse aus dem `_site` Verzeichnis auf den Server hoch

## 4. Beiträge verfassen
Der [Leitfaden zum Verfassen von Beiträgen](https://chirpy.cotes.page/posts/write-a-new-post/) des Chirpy Themes dokumentiert gut die Methoden zum Verfassen von Beiträgen und die verfügbaren Optionen. Es bietet viele Funktionen über das hier Beschriebene hinaus, und es enthält nützliche Informationen zum Nachschlagen. Bei Bedarf sollte man die offizielle Dokumentation konsultieren. Hier werden die wichtigsten Punkte zusammengefasst, die bei jedem Beitrag zu beachten sind.

### Markdown-Datei erstellen
- Namensformat: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Ort: `_posts`{: .filepath} Verzeichnis

### Front Matter schreiben
Am Anfang der Markdown-Datei muss ein angemessenes Front Matter geschrieben werden.
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
- **description**: Zusammenfassung. Wenn nicht angegeben, wird automatisch ein Teil des Haupttextes verwendet, aber für die Suchmaschinenoptimierung (SEO) wird empfohlen, den description Meta-Tag angemessen selbst zu schreiben. Eine Länge von etwa 135-160 Zeichen für lateinische Schrift oder 80-110 Zeichen für CJK-Schrift ist angemessen.
- **date**: Genaues Erstellungsdatum und -zeit des Beitrags sowie Zeitzone (optional, bei Auslassung wird automatisch das Erstellungs- oder Änderungsdatum der Datei verwendet)
- **categories**: Kategorisierung des Beitrags
- **tags**: Tags für den Beitrag
- **image**: Einfügen eines Vorschaubildes am Anfang des Beitrags
  - **path**: Pfad zur Bilddatei
  - **alt**: Alternativer Text (optional)
- **toc**: Verwendung der Inhaltsverzeichnisfunktion in der rechten Seitenleiste, Standardwert ist `true`
- **comments**: Zur expliziten Angabe der Kommentarfunktion für einzelne Beiträge, unabhängig von den Standardeinstellungen der Website
- **math**: Aktivierung der eingebauten Formeldarstellungsfunktion basierend auf [MathJax](https://www.mathjax.org/), Standardwert ist aus Leistungsgründen deaktiviert (`false`)
- **mermaid**: Aktivierung der eingebauten Diagrammdarstellungsfunktion basierend auf [Mermaid](https://github.com/mermaid-js/mermaid), Standardwert ist deaktiviert (`false`)

## 5. Upgrade

Dies wird unter der Annahme beschrieben, dass Methode 1 aus [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-github-repository-erstellen) gewählt wurde. Bei Wahl von Methode 2 muss, wie erwähnt, der neueste Upstream-Tag manuell gemergt werden.

1. Bearbeiten Sie `Gemfile`{: .filepath}, um die Version des "jekyll-theme-chirpy" Gems neu festzulegen.
2. Bei Major-Upgrades könnten sich auch Kerndateien und Konfigurationsoptionen geändert haben, die nicht im "jekyll-theme-chirpy" Gem enthalten sind. In diesem Fall müssen die Änderungen über die folgende GitHub API überprüft und manuell übernommen werden:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<ältere_version>...<neuere_version>
  ```
