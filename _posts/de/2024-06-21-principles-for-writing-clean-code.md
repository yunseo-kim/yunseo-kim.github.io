---
title: Prinzipien für das Schreiben von gutem Code
description: "Warum guter, wartbarer Code wichtig ist – und welche Prinzipien helfen: KISS, DRY, Modularisierung, Standardbibliothek, klare Namen, Normalisierung, Trennung von Logik und Daten."
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## Warum es wichtig ist, guten Code zu schreiben
Wenn man sich nur darauf konzentriert, für die aktuelle Implementierung schnell Code herunterzuschreiben, können sich [Technische Schulden](/posts/Technical-debt/) bis zu einem unbeherrschbaren Niveau aufblähen und später die Wartung erschweren. Deshalb ist es bei Entwicklungsprojekten ohne Frage wichtig, von Anfang an gut lesbaren und wartbaren Code zu schreiben.

Bei Problemlösen (PS, Problem Solving) oder Programmierwettbewerben (CP, Competitive Programming) wird der verwendete Code nach Abschluss der Lösung bzw. des Wettbewerbs meist nicht wiederverwendet. Insbesondere bei CP gibt es Zeitlimits, weshalb manche sagen, schnelles Implementieren sei wichtiger als „guter“ Code. Um diese Frage zu beantworten, sollte man sich klarmachen, warum man PS/CP betreibt und in welche Richtung man sich entwickeln will.

Meiner Meinung nach kann man – abgesehen vom allgemeinen Fördern der Problemlösekompetenz und mit Fokus auf das Programmieren – durch PS/CP Folgendes lernen:
- Innerhalb gegebener Laufzeit- und Speicherlimits kann man verschiedene Algorithmen und Datenstrukturen verwenden und verinnerlichen; dadurch bekommt man auch in realen Projekten ein Gespür dafür, welche Algorithmen und Datenstrukturen in bestimmten Situationen geeignet sind.
- Nach dem Einreichen erhält man sofort objektives Feedback zu Richtig/Falsch, Laufzeit und Speicherverbrauch; so kann man üben, fehlerfreien Code schnell und routiniert zu schreiben.
- Man kann Code von Könnern studieren, den eigenen Code damit vergleichen und Verbesserungen finden.
- Im Vergleich zu realen Projekten schreibt man wiederholt kleineren Code mit ähnlicher Funktionalität und kann (insbesondere beim Solo-Üben von PS) ohne Deadlines auf Details achten und üben, knappen und guten Code zu schreiben.

Natürlich kann man PS/CP auch rein als Hobby betreiben. Wenn man PS/CP jedoch nutzt, um Programmierfähigkeiten zu trainieren, ist auch der letzte Punkt – „Übung im Schreiben guten Codes“ – ein großer Vorteil, nicht weniger als die drei zuvor genannten. Guter Code entsteht nicht von allein, sondern will durch wiederholte Praxis stetig eingeübt werden. Außerdem sind komplexer, schwer lesbarer Code und das Debuggen schwierig; selbst für einen selbst ist es damit schwerer, auf Anhieb korrekt zu implementieren. Verliert man dann Zeit in ineffizientem Debuggen, wird die Implementierung am Ende oft gar nicht so schnell. Zwischen PS/CP und der Berufspraxis gibt es zwar große Unterschiede, aber deshalb das Schreiben guten Codes völlig zu ignorieren und nur auf schnelle Umsetzung zu setzen, wäre aus den genannten Gründen eine Verkehrung von Zweck und Mittel. Ich persönlich finde, auch in PS/CP sollte man knappen und effizienten Code schreiben.

> 12024.12 Kommentar hinzugefügt:  
> Betrachtet man die derzeitige Entwicklung, bleiben der Aufbau von Grundlagen in Algorithmen und Datenstrukturen sowie das Trainieren der Problemlösefähigkeit weiterhin sinnvoll. In der Phase, in der man das in lauffähigen Code gießt, sollte man aber nicht darauf beharren, alles selbst zu tippen: Es ist m. E. klüger, GitHub Copilot, Cursor, Windsurf u. a. AI-Tools aktiv zu nutzen, Zeit zu sparen und die gewonnene Zeit in andere Arbeit oder Lernen zu investieren. Wer PS/CP für allgemeine Problemlösekompetenz oder als Hobby macht, soll sich davon natürlich nicht abhalten lassen. Aber nur zum Üben des Codens Zeit und Mühe in PS/CP zu stecken, hat inzwischen ein deutlich schlechteres Kosten-Nutzen-Verhältnis. Selbst in Entwicklerjobs dürfte – zumindest als Einstellungstest – die Bedeutung klassischer Codetests spürbar sinken.
{: .prompt-warning }

## Prinzipien für das Schreiben von gutem Code
Ob Code für Wettbewerbe oder für die Praxis: Die Kriterien für „guten Code“ unterscheiden sich kaum. In diesem Beitrag gehe ich auf die wichtigsten allgemeinen Prinzipien ein. Für PS/CP kann es zur schnellen Umsetzung relativ zur Praxis Kompromisse geben; solche Fälle erwähne ich ausdrücklich.

### Einfachen, schlanken Code schreiben
> "KISS(Keep It Simple, Stupid)"

- Je kürzer und schlanker der Code, desto geringer das Risiko von Tippfehlern oder trivialen Bugs, und desto einfacher das Debuggen.
- Möglichst so schreiben, dass sich der Code auch ohne separate Kommentare leicht erschließt; wirklich nur, wenn nötig, Kommentare zur Detailerklärung ergänzen. Besser die Struktur selbst einfach halten, statt auf Kommentare zu bauen.
- Falls Kommentare nötig sind, klar und knapp formulieren.
- Funktionen sollten höchstens drei Parameter entgegennehmen; sind mehr nötig, diese nach Möglichkeit in einem Objekt bündeln.
- Eine tiefe Verschachtelung von Bedingungen verschlechtert die Lesbarkeit. Man sollte daher die Verschachtelungstiefe möglichst gering halten.  
  z. B. ist der folgende Stil mit Guard Clauses leserlicher als der obige:  

  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if user:
          token = await user_service.get_token(user)
  
          if token :
              if token.purpose == 'reset':
                  return True
      return False
  ```
  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if not user:
          return False
    
      token = await user_service.get_token(user)
  
      if not token or token.purpose != 'reset':
          return False
    
    return True
  ```
- In PS/CP geht man teils noch weiter und nutzt Tricks wie C/C++-Makros, um Code kürzer und schneller schreibbar zu machen. Unter Zeitdruck eines Wettbewerbs kann das nützlich sein, aber es ist eine PS/CP-spezifische Methode; im Allgemeinen sollte man Makros in C++ vermeiden.  
  z. B.:  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Code modularisieren
> "DRY(Don't Repeat Yourself)"

- Wiederholte Codeabschnitte in Funktionen oder Klassen kapseln und wiederverwenden.
- Durch Modularisierung steigt die Lesbarkeit, und bei Änderungen muss man nur die zentrale Funktion/Klasse anpassen – die Wartung wird leichter.
- Idealerweise erfüllt eine Funktion nur eine einzige Aufgabe (Single Responsibility). Bei PS/CP ist der Code jedoch meist kleinskalig und auf spezifische, einfache Aufgaben ausgerichtet; Wiederverwendung ist begrenzt und die Zeit knapp, sodass man die Prinzipien nicht so strikt wie in der Praxis einhalten kann.

### Standardbibliothek nutzen
> "Don't reinvent the wheel"

- In der Lernphase für Algorithmen/Datenstrukturen ist es sinnvoll, etwa Queues, Stacks oder Sortieralgorithmen selbst zu implementieren, um die Prinzipien zu verstehen. Abseits dessen sollte man die Standardbibliothek aktiv nutzen.
- Standardbibliotheken sind vielfach genutzt, gut erprobt und in der Regel performant – effizienter als Eigenimplementierungen.
- Durch Nutzung bestehender Bibliotheken spart man sich redundante Implementierungen und Zeit; in der Zusammenarbeit können Teammitglieder den Code zudem leichter verstehen.

### Konsistente und klare Benennung verwenden
> "Follow standard conventions"

- Unmissverständliche Variablen- und Funktionsnamen verwenden.
- Jede Sprache hat übliche Namenskonventionen; die in der Standardbibliothek der jeweiligen Sprache verwendeten Konventionen kennen und für Klassen, Funktionen, Variablen etc. konsequent anwenden.
- So benennen, dass klar wird, welche Aufgabe Variablen, Funktionen und Klassen erfüllen; bei booleschen (boolean) Werten sollte erkennbar sein, unter welcher Bedingung sie wahr (True) sind.

### Alle Daten normalisiert speichern
- Alle Daten in ein einheitliches Format normalisieren und so verarbeiten.
- Hat derselbe Inhalt mehrere Formate, drohen schwer auffindbare, subtile Bugs, z. B. leicht abweichende String-Darstellungen oder unterschiedliche Hash-Werte.
- Beim Speichern/Verarbeiten von Daten wie Zeitzonen oder Strings möglichst unmittelbar nach Eingabe/Berechnung in ein Standardformat wie UTC oder UTF-8 konvertieren. Entweder schon im Konstruktor der repräsentierenden Klasse normalisieren oder direkt in der Eingabefunktion.

### Code-Logik und Daten trennen
- Daten, die nichts mit der Code-Logik zu tun haben, nicht direkt in Bedingungen einbetten, sondern in eine separate Tabelle auslagern.  
  z. B. ist die folgende Schreibweise besser als die obige:

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ~~~c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ~~~
