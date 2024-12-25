---
title: GitHub Pages Blog erstellen und verwalten
description: Erfahren Sie mehr über die Eigenschaften und Unterschiede von statischen
  und dynamischen Webseiten, statischen Website-Generatoren und hosten Sie einen Jekyll-Blog
  auf GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---
Seit Anfang 2021 hoste ich meinen Blog mit Jekyll auf GitHub Pages. Da ich den Installationsprozess beim Aufbau des Blogs nicht richtig dokumentiert hatte, gab es bei der späteren Wartung einige Schwierigkeiten. Deshalb habe ich mich entschlossen, den Installationsprozess und die Wartungsmethoden zumindest kurz zusammenzufassen.

(+ Aktualisierung Dezember 2024)

## 1. Statischer Site-Generator & Webhosting
### 1-1. Statische Webseiten vs. Dynamische Webseiten
#### Statische Webseiten (Static Web Pages)
- Webseiten, die auf dem Server gespeicherte Daten unverändert an den Benutzer übermitteln
- Der Webserver liefert eine vorher gespeicherte Seite entsprechend der Benutzeranfrage
- Benutzer sehen die gleiche Webseite, solange die auf dem Server gespeicherten Daten nicht geändert werden
- Da nur die angeforderte Datei übertragen werden muss, ist keine zusätzliche Verarbeitung erforderlich, was in der Regel zu schnelleren Antwortzeiten führt
- Bestehen nur aus einfachen Dateien, sodass nur ein Webserver eingerichtet werden muss, was die Einrichtungskosten niedrig hält
- Zeigen nur gespeicherte Informationen an, daher sind die Dienste begrenzt
- Hinzufügen, Ändern und Löschen von Daten muss manuell vom Administrator durchgeführt werden
- Struktur ist für Suchmaschinen leichter zu crawlen, was für die Suchmaschinenoptimierung (SEO) relativ vorteilhaft ist

#### Dynamische Webseiten (Dynamic Web Pages)
- Webseiten, die auf dem Server gespeicherte Daten durch Skripte verarbeiten und übermitteln
- Der Webserver interpretiert die Benutzeranfrage, verarbeitet die Daten und liefert dann die generierte Webseite
- Benutzer sehen Webseiten, die sich je nach Situation, Zeit und Anfrage ändern
- Relativ langsamere Antwortzeiten, da Skripte zur Bereitstellung der Webseite verarbeitet werden müssen
- Zusätzliche Kosten bei der Einrichtung, da neben dem Webserver auch ein Anwendungsserver erforderlich ist
- Ermöglichen vielfältige Dienste durch dynamische Bereitstellung verschiedener Informationskombinationen
- Je nach Webseitenstruktur können Benutzer Daten direkt im Browser hinzufügen, ändern und löschen

### 1-2. Statischer Site-Generator (SSG, Static Site Generator)
- Ein Werkzeug, das statische Webseiten basierend auf Rohdaten (meist Markdown-Textdateien) und vordefinierten Templates generiert
- Automatisiert den Prozess des Erstellens und Bereitstellens von Webseiten, ohne dass einzelne HTML-Seiten manuell geschrieben werden müssen
- Beispiele: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Ein kostenloser Hosting-Service für statische Webseiten, bereitgestellt von GitHub
- Ermöglicht das Hosten einer persönlichen Hauptwebseite pro Konto und unbegrenzt viele projektbezogene Dokumentationsseiten pro Repository
- Nach Erstellung eines Repositories mit dem Namen '{username}.github.io' entsprechend dem eigenen GitHub-Benutzernamen können gebaute HTML-Seiten direkt gepusht oder der Build- und Bereitstellungsprozess über GitHub Actions durchgeführt werden
- Bei Besitz einer eigenen Domain kann diese in den Einstellungen verknüpft werden, um anstelle der Standard-Domain '{username}.github.io' eine andere Domainadresse zu verwenden

## 2. Auswahl des SSG und Themes

### 2-1. Gründe für die Wahl von Jekyll
Es gibt verschiedene SSGs wie Jekyll, Hugo, Gatsby usw., aber ich habe mich für Jekyll entschieden. Die Kriterien, die ich bei der Auswahl des SSG berücksichtigt habe, und die Gründe für die Wahl von Jekyll sind wie folgt:
- Kann ich unnötige Versuch-und-Irrtum-Phasen minimieren und mich auf das Schreiben von Beiträgen und den Betrieb des Blogs konzentrieren?
  - Jekyll ist der offiziell unterstützte statische Website-Generator für GitHub Pages. Natürlich können auch andere SSGs wie Hugo, Gatsby usw. auf GitHub Pages gehostet werden, und es besteht auch die Option, einen ganz anderen Hosting-Service wie Netlify zu nutzen. Aber für den Betrieb eines persönlichen Blogs dieser Größenordnung ist es technisch gesehen nicht wirklich wichtig, mit welchem SSG er aufgebaut wurde oder wie schnell der Build-Prozess ist. Daher hielt ich es für besser, etwas zu wählen, das einfacher zu warten ist und für das es mehr Referenzdokumente gibt.
  - Jekyll hat auch die längste Entwicklungszeit im Vergleich zu Konkurrenten wie Hugo und Gatsby. Dementsprechend ist es gut dokumentiert, und es gibt eine überwältigende Menge an Referenzmaterial, wenn tatsächlich Probleme auftreten.
- Gibt es eine Vielfalt an verfügbaren Themes und Plugins?
  - Selbst wenn man keinen HTML-Code selbst schreibt, sondern einen SSG verwendet, ist es zeitaufwändig und unnötig, alle Templates selbst zu erstellen. Es gibt viele hervorragende Themes, die bereits im Web verfügbar sind, und man kann einfach eines auswählen und verwenden, das einem gefällt.
  - Da ich ursprünglich hauptsächlich C oder Python verwendet habe und mit Ruby (für Jekyll) oder Go (für Hugo) nicht so vertraut bin, wollte ich bestehende Themes und Plugins noch aktiver nutzen.
  - Bei Jekyll konnte ich schnell ein Theme finden, das mir auf den ersten Blick gefiel, während Hugo und Gatsby vergleichsweise weniger Themes hatten, die für den Zweck eines persönlichen Blogs geeignet schienen. Dies scheint stark von der oben erwähnten Kompatibilität mit GitHub Pages, das von Entwicklern häufig für persönliche Blog-Hosting genutzt wird, und der Entwicklungszeit beeinflusst zu sein.

### 2-2. Theme-Auswahl
#### Minimal Mistakes (Januar 2021 - April 2022)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo-Seite: <https://mmistakes.github.io/minimal-mistakes/>
- Theme, das ich etwa 1 Jahr und 3 Monate lang nach der ersten Erstellung meines Blogs verwendet habe
- Unterstützung für Kommentarfunktionen über Disqus, Discourse, utterances usw.
- Unterstützung für Kategorie- und Tag-Klassifizierung
- Integrierte Unterstützung für Google Analytics
- Auswahl vordefinierter Skins möglich
- Obwohl ich später zum Chirpy-Theme wechselte, das ein attraktiveres Design hat, war es angesichts der Tatsache, dass es sich um einen technischen Blog handelt, zwar nicht besonders schön, aber hatte ein recht sauberes Design, das gut zu verwenden war.

#### Chirpy Jekyll Theme (April 2022 - heute)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo-Seite: <https://chirpy.cotes.page/>
- Theme, das ich seit April 2022 bis heute verwende
- Unterstützung für Mehrfachkategorien-Klassifizierung und Tags
- Integrierte Unterstützung für mathematische Ausdrücke mit LaTex-Syntax basierend auf MathJax
- Integrierte Unterstützung für Diagrammfunktionen basierend auf Mermaid
- Unterstützung für Kommentarfunktionen über Disqus, Giscus usw.
- Unterstützung für Google Analytics, GoatCounter
- Unterstützung für helles und dunkles Theme
- Zum Zeitpunkt des Theme-Wechsels wurden MathJax oder Mermaid vom Minimal Mistakes Theme nicht nativ unterstützt und mussten durch eigene Anpassungen hinzugefügt werden. Das Chirpy Theme unterstützt diese Funktionen von Haus aus. Obwohl die Anpassungen nicht besonders kompliziert waren, ist dies dennoch ein kleiner Vorteil.
- Vor allem sieht das Design gut aus. Während das Minimal Mistakes Theme zwar sauber ist, hat es eine gewisse Steifheit, die eher für offizielle technische Dokumentationen oder Portfolio-Seiten geeignet scheint. Das Chirpy Theme hingegen hat den Vorteil eines Designs, das kommerziellen Blog-Plattformen wie Tistory, Medium oder velog in nichts nachsteht.

## 3. GitHub Repository erstellen, bauen und bereitstellen
Dies basiert auf dem aktuell (Juni 2024) verwendeten Chirpy Jekyll Theme und geht davon aus, dass Git bereits installiert ist.  
Siehe [offizielle Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) und [offizielle Chirpy Jekyll Theme-Seite](https://github.com/cotes2020/jekyll-theme-chirpy/wiki) für Referenzen.

### 3-1. Ruby & Jekyll installieren
Installieren Sie Ruby und Jekyll gemäß der [offiziellen Jekyll-Installationsanleitung](https://jekyllrb.com/docs/installation/) entsprechend Ihrer Betriebssystemumgebung.

### 3-2. GitHub Repository erstellen
Die [offizielle Chirpy Jekyll Theme-Seite](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) stellt zwei Methoden vor:
1. Kerndateien mit dem "jekyll-theme-chirpy" Gem importieren und die restlichen Ressourcen aus der [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) Vorlage beziehen
  - Vorteil: Einfache Anwendung von Versions-Upgrades, wie später erläutert.
  - Nachteil: Eingeschränkte Anpassungsmöglichkeiten.
2. Das [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) Repository für Ihren Blog forken
  - Vorteil: Alle Dateien werden direkt im Repository verwaltet, sodass auch nicht vom Theme unterstützte Funktionen durch direkte Codeänderungen frei angepasst werden können.
  - Nachteil: Um Versions-Upgrades anzuwenden, muss der [neueste Upstream-Tag des Originalrepositorys](https://github.com/cotes2020/jekyll-theme-chirpy/tags) gemergt werden, was zu Konflikten mit eigenen Anpassungen führen kann. In diesem Fall müssen diese Konflikte manuell gelöst werden.

Ich habe mich für Methode 1 entschieden. Das Chirpy Theme ist grundsätzlich sehr ausgereift, sodass die meisten Benutzer wenig Anpassungsbedarf haben. Zudem wird es bis 2024 sehr aktiv entwickelt und verbessert, sodass die Vorteile, dem Original-Upstream zu folgen, die Vorteile eigener Anpassungen überwiegen, es sei denn, man plant umfangreiche Modifikationen. Die offizielle Anleitung des Chirpy Themes empfiehlt Methode 1 für die meisten Benutzer.

### 3-3. Haupteinstellungen
Nehmen Sie die erforderlichen Einstellungen in den Dateien `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} und `_data/share.yml`{: .filepath} im Stammverzeichnis vor. Die Kommentare sind gut geschrieben und die Einstellungen sind intuitiv, sodass sie ohne besondere Schwierigkeiten angewendet werden können. Die einzigen Einstellungen, die externe Arbeiten erfordern, sind die Registrierung des Authentifizierungscodes für die Google Search Console-Integration und die Integration von Webmaster-Tools wie Google Analytics oder GoatCounter. Aber auch diese Verfahren sind nicht besonders kompliziert und nicht das Kernthema dieses Beitrags, daher wird auf eine detaillierte Beschreibung verzichtet.

### 3-4. Lokal bauen
Dies ist kein notwendiger Schritt, aber Sie möchten vielleicht vorher überprüfen, ob neue Beiträge oder Änderungen an der Website korrekt im Web angezeigt werden. In diesem Fall öffnen Sie ein Terminal im Stammverzeichnis des lokalen Repositories und führen Sie den folgenden Befehl aus:
```console
$ bundle exec jekyll s
```
Nach einigen Sekunden wird die Website lokal gebaut und das Ergebnis kann unter der Adresse <http://127.0.0.1:4000> überprüft werden.

### 3-5. Bereitstellen
Es gibt zwei Methoden:
1. Nutzung von GitHub Actions (bei Hosting auf GitHub Pages)
  - Bei Nutzung des GitHub Free Plans muss das Repository öffentlich bleiben
  - Wählen Sie auf der GitHub-Webseite den *Settings*-Tab des Repositories, klicken Sie dann in der linken Navigationsleiste auf *Code and automation > Pages* und wählen Sie im Abschnitt **Source** die Option **GitHub Actions**
  - Nach Abschluss der Einrichtung wird der *Build and Deploy*-Workflow bei jedem neuen Commit automatisch ausgeführt
2. Manueller Build und Bereitstellung (bei Nutzung anderer Hosting-Dienste oder Self-Hosting)
  - Führen Sie den folgenden Befehl aus, um die Website manuell zu bauen
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Laden Sie die Build-Ergebnisse aus dem `_site`-Verzeichnis auf den Server hoch

## 4. Beiträge verfassen
Der [Leitfaden zum Verfassen von Beiträgen](https://chirpy.cotes.page/posts/write-a-new-post/) des Chirpy Themes dokumentiert gut, wie man Beiträge verfasst und welche Optionen verfügbar sind. Das Theme bietet viele Funktionen über die hier beschriebenen hinaus, und es lohnt sich, die offizielle Dokumentation zu konsultieren, wenn nötig. Hier fassen wir die wichtigsten Punkte zusammen, die bei jedem Beitrag zu beachten sind.

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
- **description**: Zusammenfassung. Wenn nicht angegeben, wird automatisch ein Teil des Haupttextes verwendet, aber für die Suchmaschinenoptimierung (SEO) wird empfohlen, den description Meta-Tag angemessen selbst zu schreiben. Eine Länge von etwa 135-160 Zeichen für lateinische Schrift oder 80-110 Zeichen für CJK-Schriften ist angemessen.
- **date**: Genaues Erstellungsdatum und -zeit des Beitrags mit Zeitzone (optional, bei Auslassung wird automatisch das Erstellungs- oder Änderungsdatum der Datei verwendet)
- **categories**: Kategorisierung des Beitrags
- **tags**: Tags für den Beitrag
- **image**: Vorschaubild am Anfang des Beitrags einfügen
  - **path**: Pfad zur Bilddatei
  - **alt**: Alternativer Text (optional)
- **toc**: Verwendung der Inhaltsverzeichnisfunktion in der rechten Seitenleiste, Standardwert ist `true`
- **comments**: Explizite Angabe der Kommentarfunktion für einzelne Beiträge, unabhängig von den Standardeinstellungen der Website
- **math**: Aktivierung der integrierten Formeldarstellungsfunktion basierend auf [MathJax](https://www.mathjax.org/), Standardwert ist `false` für bessere Seitenleistung
- **mermaid**: Aktivierung der integrierten Diagrammdarstellungsfunktion basierend auf [Mermaid](https://github.com/mermaid-js/mermaid), Standardwert ist `false`

## 5. Upgrade

Dies geht davon aus, dass Methode 1 aus [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-github-repository-erstellen) gewählt wurde. Bei Wahl von Methode 2 muss, wie erwähnt, der neueste Upstream-Tag manuell gemergt werden.

1. Bearbeiten Sie die `Gemfile`{: .filepath}, um die neue Version des "jekyll-theme-chirpy" Gems anzugeben.
2. Bei Major-Upgrades können sich auch Kerndateien und Konfigurationsoptionen geändert haben, die nicht im "jekyll-theme-chirpy" Gem enthalten sind. In diesem Fall müssen Sie die Änderungen mit der folgenden GitHub API überprüfen und manuell anwenden:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<ältere_version>...<neuere_version>
  ```
