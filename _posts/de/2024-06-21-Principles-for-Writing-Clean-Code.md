---
title: Prinzipien für das Schreiben guten Codes
description: Wir untersuchen die Notwendigkeit, guten Code zu schreiben, und die wichtigsten
  allgemeinen Prinzipien für die Erstellung von gutem Code.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.jpg
---
## Die Notwendigkeit, guten Code zu schreiben
Wenn man sich nur darauf konzentriert, schnell Code für die sofortige Implementierung zu schreiben, kann die [technische Schuld](/posts/Technical-debt/#technische-schuld-technical-debt) auf ein unkontrollierbares Niveau anwachsen und später zu Wartungsproblemen führen. Daher ist es bei der Durchführung von Entwicklungsprojekten unbestreitbar wichtig, von Anfang an lesbaren und wartbaren guten Code zu schreiben.

Bei Problemlösung (PS, Problem Solving) oder Wettbewerbsprogrammierung (CP, Competitive Programming) wird der zur Problemlösung verwendete Code normalerweise nach Abschluss der Aufgabe oder des Wettbewerbs nicht wiederverwendet. Insbesondere bei CP gibt es oft Zeitbeschränkungen, sodass man argumentieren könnte, dass eine schnelle Implementierung wichtiger sei als das Schreiben von gutem Code. Um diese Frage zu beantworten, muss man darüber nachdenken, warum man PS/CP betreibt und welche Richtung man verfolgt.

Meiner Meinung nach kann man durch PS/CP Folgendes lernen:
- Man kann verschiedene Algorithmen und Datenstrukturen innerhalb der gegebenen Laufzeit- und Speicherbeschränkungen anwenden und erlernen. Dies hilft dabei, ein Gefühl dafür zu entwickeln, welche Algorithmen und Datenstrukturen in bestimmten Situationen bei realen Projekten am besten geeignet sind.
- Nach dem Schreiben und Einreichen des Codes erhält man sofort objektives Feedback zur Korrektheit, Laufzeit und Speichernutzung. Dies ermöglicht es, präzisen Code schnell und kompetent zu schreiben, ohne etwas zu übersehen.
- Man kann den Code von erfahrenen Programmierern betrachten, ihn mit dem eigenen vergleichen und Verbesserungsmöglichkeiten finden.
- Im Vergleich zu realen Entwicklungsprojekten schreibt man wiederholt Code mit ähnlicher Funktionalität in kleinerem Umfang. Dies ermöglicht es (besonders beim alleinigen PS-Üben), ohne Zeitdruck auf Details zu achten und das Schreiben von prägnanten und guten Code zu üben.

Obwohl es Fälle gibt, in denen PS/CP einfach als Hobby betrieben wird, ist der letzte Punkt "Üben, guten Code zu schreiben" ein ebenso großer Vorteil wie die ersten drei, wenn man PS/CP indirekt zur Verbesserung der Programmierfähigkeiten nutzt. Das Schreiben von gutem Code ist keine natürliche Fähigkeit, sondern erfordert kontinuierliche Übung und Verfeinerung. Zudem ist komplexer und schwer lesbarer Code schwierig zu debuggen und selbst für den Autor nicht einfach, auf Anhieb korrekt zu schreiben. Ineffizientes Debugging kann viel Zeit in Anspruch nehmen, sodass die Implementierung letztendlich nicht so schnell erfolgt. Obwohl PS/CP sich natürlich stark von der Praxis unterscheidet, ist es aus den genannten Gründen meiner Meinung nach kontraproduktiv, das Schreiben von gutem Code völlig zu vernachlässigen und sich nur auf die sofortige Implementierung zu konzentrieren. Daher denke ich, dass es auch bei PS/CP vorteilhaft ist, prägnanten und effizienten Code zu schreiben.

> Kommentar hinzugefügt im Dezember 2024:  
> Angesichts der aktuellen Entwicklungen scheint es, dass, sofern man nicht Informatik studiert und die Entwicklung selbst zum Beruf macht, es für diejenigen, die Programmierung als Mittel für numerische Analyse oder Auswertung von Versuchsdaten nutzen wollen, sinnvoller sein könnte, KI-Tools wie GitHub Copilot, Cursor oder Windsurf aktiv zu nutzen, um Zeit zu sparen und diese gewonnene Zeit für andere Studien zu verwenden. Wenn man PS/CP als Hobby betreibt, wird niemand etwas dagegen haben, aber Zeit und Mühe in PS/CP zu investieren, um das Codeschreiben zu üben, scheint jetzt im Verhältnis von Aufwand zu Nutzen nicht mehr so effizient zu sein. Selbst für Entwicklerberufe erwarte ich, dass die Bedeutung von Coding-Tests als Einstellungsprüfung wahrscheinlich deutlich abnehmen wird.
{: .prompt-warning }

## Prinzipien für das Schreiben guten Codes
Ob es sich um Code handelt, der in Wettbewerben geschrieben wird, oder um Code, der in der Praxis geschrieben wird, die Kriterien für guten Code unterscheiden sich nicht wesentlich. In diesem Artikel werden die wichtigsten allgemeinen Prinzipien für das Schreiben von gutem Code behandelt. Bei PS/CP kann es jedoch Kompromisse geben, um eine schnelle Implementierung zu ermöglichen, die im Vergleich zur Praxis relativ sind. Solche Fälle werden im Artikel gesondert erwähnt.

### Schreiben von prägnanten Code
> "KISS (Keep It Simple, Stupid)"

- Je kürzer und prägnanter der Code ist, desto geringer ist natürlich die Gefahr von Tippfehlern oder einfachen Bugs, und das Debugging wird erleichtert.
- Der Code sollte möglichst so geschrieben werden, dass er ohne zusätzliche Kommentare leicht zu interpretieren ist. Kommentare sollten nur hinzugefügt werden, wenn sie wirklich notwendig sind. Es ist besser, die Codestruktur selbst übersichtlich zu halten, als sich auf Kommentare zu verlassen.
- Wenn Kommentare geschrieben werden, sollten sie klar und prägnant sein.
- Die Anzahl der an eine Funktion übergebenen Argumente sollte auf höchstens drei begrenzt werden. Wenn mehr Argumente zusammen übergeben werden müssen, sollten sie zu einem Objekt zusammengefasst werden.
- Tiefe Verschachtelungen von Bedingungen (doppelt, dreifach) beeinträchtigen die Lesbarkeit, daher sollte eine Zunahme der Tiefe von Bedingungen möglichst vermieden werden.
  z.B. Der untere Code, der die Guard Clause Idiom verwendet, ist in Bezug auf die Lesbarkeit vorteilhafter als der obere Code.

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
- Bei PS/CP wird jedoch manchmal der Trick verwendet, Makros in C/C++ zu nutzen, um die Codelänge weiter zu reduzieren und schneller zu schreiben. Dies kann in zeitkritischen Wettbewerben nützlich sein, sollte aber nur für PS/CP verwendet werden. Im Allgemeinen sollte die Verwendung von Makros in C++ vermieden werden.
  z.B.

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Code-Modularisierung
> "DRY (Don't Repeat Yourself)"

- Wenn derselbe Code wiederholt verwendet wird, sollte dieser Teil in Funktionen oder Klassen aufgeteilt und wiederverwendet werden.
- Durch aktive Wiederverwendung von Code durch Modularisierung verbessert sich die Lesbarkeit, und wenn später Codeänderungen erforderlich sind, muss nur die entsprechende Funktion oder Klasse einmal geändert werden, was die Wartung erleichtert.
- Prinzipiell ist es ideal, wenn eine Funktion nicht mehr als eine Aufgabe erfüllt und nur eine Funktionalität hat. Allerdings ist der Code, der in PS/CP geschrieben wird, meist ein kleines Programm mit einfacher Funktionalität, sodass die Wiederverwendung begrenzt ist. Aufgrund der Zeitbeschränkungen kann es schwierig sein, die Prinzipien so streng wie in der Praxis zu befolgen.

### Nutzung von Standardbibliotheken
> "Don't reinvent the wheel"

- Während es in der Lernphase von Algorithmen und Datenstrukturen nützlich sein kann, Datenstrukturen wie Queues und Stacks oder Sortieralgorithmen selbst zu implementieren, um die Prinzipien zu verstehen, ist es ansonsten besser, Standardbibliotheken aktiv zu nutzen.
- Standardbibliotheken wurden bereits unzählige Male verwendet und verifiziert und sind gut optimiert, was sie effizienter macht als eine eigene Implementierung.
- Da man vorhandene Bibliotheken verwenden kann, muss man keine Zeit damit verschwenden, dieselbe Funktionalität unnötigerweise selbst zu implementieren. Zudem ist es für andere Teammitglieder bei der Zusammenarbeit einfacher, den geschriebenen Code zu verstehen.

### Verwendung konsistenter und klarer Benennungskonventionen
> "Follow standard conventions"

- Verwendung eindeutiger Variablen- und Funktionsnamen.
- Normalerweise gibt es für jede Programmiersprache passende Benennungskonventionen. Es ist ratsam, sich mit den in der Standardbibliothek der verwendeten Sprache genutzten Konventionen vertraut zu machen und diese konsistent bei der Deklaration von Klassen, Funktionen und Variablen anzuwenden.
- Die Benennung sollte klar die Funktion jeder Variable, Funktion und Klasse widerspiegeln. Bei booleschen Typen sollte deutlich werden, unter welchen Bedingungen sie True zurückgeben.

### Normalisierung aller Daten bei der Speicherung
- Alle Daten sollten in einem einheitlichen, normalisierten Format verarbeitet werden.
- Wenn dieselben Daten in mehr als einem Format vorliegen, können subtile, schwer zu findende Bugs auftreten, wie leicht abweichende String-Darstellungen oder unterschiedliche Hash-Werte.
- Bei der Speicherung und Verarbeitung von Daten wie Zeitzonen oder Strings sollten diese sofort nach der Eingabe oder Berechnung in ein einheitliches Standardformat wie UTC oder UTF-8-Kodierung konvertiert werden. Es ist ratsam, die Normalisierung entweder im Konstruktor der Klasse, die die Daten repräsentiert, oder direkt in der Funktion, die die Daten entgegennimmt, durchzuführen.

### Trennung von Code-Logik und Daten
- Daten, die nicht mit der Logik des Codes zusammenhängen, sollten nicht direkt in Bedingungsanweisungen eingefügt, sondern in separate Tabellen ausgelagert werden.
  z.B. Es ist besser, den Code wie im unteren Beispiel zu schreiben, anstatt wie im oberen.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ```c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ```
