---
title: Technische Schuld (Technical debt)
description: Lasst uns das Konzept der technischen Schuld, die Gründe für ihr Entstehen
  und Möglichkeiten zu ihrer Minimierung betrachten.
categories: [Programming]
tags: [Coding]
image: /assets/img/technology.jpg
---
## Technische Schuld (Technical debt)
Technische Schuld: Der Preis, den man später zahlen muss, wenn man in der Entwicklung Abkürzungen wählt, um unmittelbare Anforderungen zu erfüllen und das aktuelle Projekt schneller abzuschließen.

Ähnlich wie man durch die Aufnahme von finanziellen Schulden schnell in dringende Bereiche investieren kann, aber dann unter finanziellem Druck steht und Kapital plus Zinsen zurückzahlen muss, führt die schnelle Entwicklung zur Lösung aktueller Anforderungen - auch wenn sie etwas unsauber ist - zu komplexerem und redundantem Code, was die spätere Implementierung oder Erweiterung neuer Funktionen erschwert.

Es ist nicht unbedingt schlecht, technische Schulden in Kauf zu nehmen, um neue Funktionen schnell zu implementieren, ähnlich wie Unternehmen durch Schulden mehr Investitionen rechtzeitig tätigen können, um neue Produkte zu entwickeln und Marktanteile zu gewinnen, oder wie Einzelpersonen durch Kredite Häuser kaufen können. Es ist jedoch wünschenswert, die Anhäufung technischer Schulden zu reduzieren und sie auf einem beherrschbaren Niveau zu halten.

## Gründe für das Entstehen technischer Schulden
Selbst wenn die Fähigkeiten der Entwickler ausreichend sind, entstehen technische Schulden unvermeidlich im Prozess der Softwareentwicklung und können nicht vollständig verhindert werden.
Wenn ein Dienst sich weiterentwickelt und der ursprünglich entworfene Code an seine Grenzen stößt, kann es notwendig sein, das bestehende Design zu ändern, selbst wenn der Code ursprünglich gut lesbar und funktional war.
Auch wenn sich die Technologie selbst weiterentwickelt und früher gängige Bibliotheken/Frameworks nicht mehr häufig verwendet werden, kann man sich entscheiden, den technologischen Stack auf andere Bibliotheken/Frameworks umzustellen, und in diesem Fall wird der zuvor geschriebene Code zu einer Art technischer Schuld.

Darüber hinaus können technische Schulden aus folgenden Gründen entstehen:
- Wenn das während des Projekts Entworfene nicht rechtzeitig dokumentiert wird, sodass andere Personen oder man selbst nach einiger Zeit Schwierigkeiten haben, den Code zu interpretieren
- Wenn nicht mehr verwendete Variablen oder Datenbankeinträge nicht entfernt werden
- Wenn wiederholte Aufgaben (Deployment/Build usw.) nicht automatisiert werden, was jedes Mal zusätzliche Zeit und Aufwand erfordert
- Dringende Spezifikationsänderungen

## Methoden zur Minimierung technischer Schulden
### Festlegung von Konventionen zwischen Entwicklern
- Wenn man nicht alleine entwickelt, ist eine Einigung über die zu verwendende Sprache oder den technologischen Stack, die Verzeichnisstruktur des Projekts, den Entwicklungsstil usw. für eine reibungslose Zusammenarbeit erforderlich
- Es muss entschieden werden, bis zu welchem Punkt die Methoden vereinheitlicht werden und ab wann sie der individuellen Autonomie überlassen werden
- Es ist notwendig, durch Code-Reviews gegenseitig die Entwicklungsstile zu überprüfen und Meinungen auszutauschen

### Schreiben von sauberem Code (Clean Code) & Refactoring
- Wenn der bestehende Code unordentlich ist und die Entwicklung behindert, können technische Schulden durch Refactoring, das die Codestruktur sauber verändert, beglichen werden
- Natürlich wird die Schwierigkeit des Refactorings umso höher, je unordentlicher der bestehende Code ist (Spaghetti-Code)
- Man sollte von Anfang an bestrebt sein, gut lesbaren und leicht zu wartenden Code zu schreiben
