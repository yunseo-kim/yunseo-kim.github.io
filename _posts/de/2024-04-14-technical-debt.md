---
title: Technische Schuld (Technical Debt)
description: "Technische Schuld verständlich erklärt: Entstehungsgründe und praxiserprobte Methoden, um sie in Softwareprojekten zu vermeiden, zu reduzieren und nachhaltig zu beherrschen."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Technische Schuld
> **Technische Schuld (Technical Debt)**  
> Die künftigen Kosten, die entstehen, wenn man im Entwicklungsprozess Abkürzungen nimmt, um aktuelle Anforderungen schneller zu erfüllen und ein Projekt rascher abzuschließen
{: .prompt-info }

So wie man, wenn man finanzielle Schulden eingeht, zwar schnell in dringend benötigte Bereiche investieren kann, dafür aber finanziellen Druck hat und Zins und Tilgung leisten muss, führt auch das schnelle Vorantreiben der Entwicklung, um akute Anforderungen zu erfüllen – selbst wenn der Code dabei etwas unsauber wird – dazu, dass der Code komplexer und redundanter wird und spätere Implementierungen oder Erweiterungen erschwert.

Wie Unternehmen über Fremdkapital rechtzeitig mehr investieren, um neue Produkte zu entwickeln und Marktanteile zu gewinnen, oder Privatpersonen über Kredite ein Haus finanzieren, ist auch das bewusste Eingehen technischer Schuld, um Funktionen schnell auszuliefern, nicht per se schlecht. Entscheidend ist, den Aufbau technischer Schuld zu begrenzen und sie in einem tragbaren Rahmen aktiv zu managen.

## Warum technische Schuld entsteht
Selbst bei hoher Kompetenz der Entwickler entsteht im Verlauf der Entwicklung zwangsläufig technische Schuld; sie vollständig zu vermeiden ist unmöglich.
Wenn ein Dienst wächst und die ursprüngliche Architektur an Grenzen stößt, muss selbst gut lesbarer und zuverlässig funktionierender Code möglicherweise umgebaut werden.
Mit dem Fortschritt der Technologien geraten einst dominierende Bibliotheken und Frameworks aus der Mode; entscheidet man sich dann für einen Wechsel des Tech-Stacks, wird der bestehende Code ebenfalls zu einer Form technischer Schuld.

Darüber hinaus kann technische Schuld aus folgenden Gründen entstehen.
- Fehlende, zeitnahe Dokumentation des Designs: Andere – oder man selbst nach einiger Zeit – tun sich schwer, den Code zu verstehen
- Nicht entfernte, obsolet gewordene Variablen oder Datenbankfelder
- Nicht automatisierte Routineaufgaben (z. B. Deployment/Build), die jedes Mal zusätzliche Zeit und Aufwand kosten
- Dringende, kurzfristige Spezifikationsänderungen

## Wie man technische Schuld minimiert
### Konventionen im Team festlegen
- Wenn man nicht allein entwickelt: Einigungen über Sprache/Tech-Stack, Projektstruktur (Verzeichnisse) und Coding-Stil für reibungslose Zusammenarbeit
- Festlegen, was standardisiert wird und wo individuelle Freiheit beginnt
- Code-Reviews nutzen, um Stilfragen abzugleichen und Feedback auszutauschen

### Clean Code schreiben & Refactoring
- Ist bestehender Code hinderlich, kann man technische Schuld durch Refactoring abbauen und die Struktur bereinigen
- Je stärker der Altcode Spaghetti-Code ist, desto schwieriger das Refactoring; im Extremfall verwirft man ihn und entwickelt von Grund auf neu
- Idealerweise von Beginn an auf gute Lesbarkeit und Wartbarkeit achten
