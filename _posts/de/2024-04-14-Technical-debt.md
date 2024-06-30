---
title: "Technische Schuld (Technical debt)"
description: >-
  Lasst uns das Konzept der technischen Schuld, die Gründe für ihr Entstehen und Methoden zu ihrer Minimierung untersuchen.
categories: [Programming]
tags: [Coding]
---

## Technische Schuld (Technical debt)
Technische Schuld: Der Preis, der später gezahlt werden muss, wenn man Abkürzungen wählt, um ein Projekt schneller abzuschließen und unmittelbare Anforderungen zu erfüllen.

Ähnlich wie bei finanziellen Schulden, bei denen man Geld leiht, um schnell in dringende Bereiche zu investieren, aber dann unter finanziellem Druck steht und Zinsen zusätzlich zum Hauptbetrag zurückzahlen muss, führt die schnelle Entwicklung zur Lösung aktueller Anforderungen, auch wenn sie etwas unsauber ist, zu komplexerem und redundantem Code, was die spätere Implementierung oder Erweiterung neuer Funktionen erschwert.

Es ist nicht unbedingt schlecht, technische Schulden in Kauf zu nehmen, um neue Funktionen schnell zu implementieren, ähnlich wie Unternehmen durch Schulden mehr Investitionen rechtzeitig tätigen, um neue Produkte zu entwickeln und Marktanteile zu erhöhen, oder wie Einzelpersonen durch Kredite Häuser kaufen. Es ist jedoch wünschenswert, die Anhäufung technischer Schulden zu reduzieren und sie auf einem beherrschbaren Niveau zu halten.

## Gründe für das Entstehen technischer Schulden
Selbst wenn die Fähigkeiten der Entwickler ausreichend sind, entstehen technische Schulden unvermeidlich im Prozess der Softwareentwicklung und können nicht vollständig verhindert werden.
Wenn ein Dienst sich weiterentwickelt und der ursprünglich entworfene Code an seine Grenzen stößt, kann es notwendig sein, das ursprüngliche Design zu ändern, selbst wenn der Code ursprünglich gut lesbar und funktional war.
Auch wenn sich die Technologie selbst weiterentwickelt und früher gängige Bibliotheken/Frameworks nicht mehr häufig verwendet werden, kann man sich entscheiden, den technologischen Stack auf andere Bibliotheken/Frameworks umzustellen, und in diesem Fall wird der zuvor geschriebene Code zu einer Art technischer Schuld.

Darüber hinaus können technische Schulden aus folgenden Gründen entstehen:
- Wenn das Design während des Projekts nicht rechtzeitig dokumentiert wird, was zu Schwierigkeiten bei der Interpretation des Codes durch andere oder sogar durch sich selbst nach einiger Zeit führt
- Wenn nicht mehr verwendete Variablen oder Datenbankeinträge nicht entfernt werden
- Wenn wiederholte Aufgaben (Deployment/Build usw.) nicht automatisiert werden, was jedes Mal zusätzliche Zeit und Aufwand erfordert
- Dringende Spezifikationsänderungen

## Methoden zur Minimierung technischer Schulden
### Festlegung von Konventionen zwischen Entwicklern
- Wenn nicht allein entwickelt wird, ist eine Einigung über die zu verwendende Sprache oder den technologischen Stack, die Projektverzeichnisstruktur, den Entwicklungsstil usw. für eine reibungslose Zusammenarbeit erforderlich
- Es muss entschieden werden, bis zu welchem Punkt die Methoden vereinheitlicht werden und ab wann sie der individuellen Autonomie überlassen werden
- Es ist notwendig, durch Code-Reviews gegenseitig die Entwicklungsstile zu überprüfen und Meinungen auszutauschen

### Schreiben von sauberem Code (Clean Code) & Refactoring
- Wenn der bestehende Code unordentlich ist und die Entwicklung behindert, können technische Schulden durch Refactoring, das die Codestruktur bereinigt, abgebaut werden
- Natürlich steigt der Schwierigkeitsgrad des Refactorings, je unordentlicher der bestehende Code ist
- Es sollte von Anfang an angestrebt werden, gut lesbaren und leicht wartbaren Code zu schreiben