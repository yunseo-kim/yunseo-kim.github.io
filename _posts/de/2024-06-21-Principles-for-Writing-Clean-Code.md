---
title: Prinzipien für das Schreiben guten Codes
description: Die Notwendigkeit, guten Code zu schreiben, und die allgemeinen Hauptprinzipien für das Schreiben guten Codes.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
---
## Die Notwendigkeit, guten Code zu schreiben
Wenn man sich nur darauf konzentriert, schnell Code zu schreiben, um eine unmittelbare Implementierung zu erreichen, kann die [technische Schuld](/posts/Technical-debt/) auf ein nicht mehr beherrschbares Niveau anwachsen und später zu Wartungsproblemen führen. Daher ist es bei der Durchführung von Entwicklungsprojekten unbestreitbar wichtig, von Anfang an lesbaren und wartungsfreundlichen Code zu schreiben.

Bei der algorithmischen Problemlösung (PS, Problem Solving) oder bei Programmierwettbewerben (CP, Competitive Programming) wird der Code, der zur Problemlösung verwendet wird, normalerweise nach Abschluss des Problems oder Wettbewerbs nicht wiederverwendet. Besonders bei CP gibt es Zeitbeschränkungen, weshalb manche argumentieren, dass eine schnelle Implementierung wichtiger sei als guter Code. Um diese Frage zu beantworten, muss man überlegen, warum man PS/CP betreibt und welche Richtung man verfolgt.

Meiner Meinung nach kann man durch PS/CP Folgendes lernen:
- Man kann verschiedene Algorithmen und Datenstrukturen innerhalb der gegebenen Laufzeit- und Speicherbeschränkungen anwenden und beherrschen, wodurch man ein Gefühl dafür bekommt, welche Algorithmen und Datenstrukturen in bestimmten Situationen bei realen Projekten verwendet werden sollten
- Nach dem Schreiben und Einreichen des Codes erhält man sofort objektives Feedback über Richtigkeit/Fehler, Laufzeit und Speicherverbrauch, sodass man üben kann, präzisen Code schnell und kompetent ohne Lücken zu schreiben
- Man kann den Code von anderen Experten betrachten, mit dem eigenen vergleichen und Verbesserungsmöglichkeiten finden
- Im Vergleich zu realen Entwicklungsprojekten schreibt man wiederholt Code kleineren Umfangs mit ähnlicher Funktionalität, sodass man (besonders wenn man alleine PS übt) ohne Zeitdruck auf Details achten und üben kann, prägnanten und guten Code zu schreiben

Obwohl manche PS/CP einfach als Hobby betreiben, ist der letzte Punkt "Übung im Schreiben guten Codes" für diejenigen, die PS/CP indirekt zur Verbesserung ihrer Programmierfähigkeiten nutzen, genauso wichtig wie die ersten drei Punkte. Guten Code zu schreiben ist keine natürliche Fähigkeit, sondern erfordert kontinuierliche Übung. Außerdem ist komplexer und schwer lesbarer Code schwieriger zu debuggen und selbst für den Autor nicht leicht auf Anhieb korrekt zu schreiben. Wenn man Zeit mit ineffizientem Debugging verbringt, führt das oft nicht zu einer schnelleren Implementierung. Obwohl PS/CP sich natürlich stark von der Berufspraxis unterscheidet, ist es aus den genannten Gründen meiner Meinung nach auch bei PS/CP besser, prägnanten und effizienten Code zu schreiben, anstatt sich nur auf die unmittelbare Implementierung zu konzentrieren.

> 12024.12 Kommentar hinzugefügt:  
> Nach der aktuellen Stimmung zu urteilen, scheint es, dass man, wenn man nicht Informatik studiert und Entwicklung als Beruf betreibt, sondern Programmierung als Mittel für numerische Analyse oder experimentelle Datenauswertung nutzen möchte, besser daran täte, KI-Tools wie GitHub Copilot, Cursor oder Windsurf aktiv zu nutzen, um Zeit zu sparen und diese für andere Studien zu verwenden. Wenn man PS/CP als Hobby genießt, wird niemand etwas dagegen haben, aber Zeit und Mühe in PS/CP zum Üben des Codeschreibens zu investieren, scheint jetzt ein schlechtes Kosten-Nutzen-Verhältnis zu haben. Selbst für Entwicklungsberufe erwarte ich, dass die Bedeutung von Coding-Tests als Einstellungsprüfung wahrscheinlich deutlich abnehmen wird.
{: .prompt-warning }

## Prinzipien für das Schreiben guten Codes
Ob es sich um Code für Wettbewerbe oder für die Praxis handelt, die Kriterien für guten Code unterscheiden sich nicht wesentlich. In diesem Artikel werden die allgemeinen Hauptprinzipien für das Schreiben guten Codes behandelt. Bei PS/CP kann es jedoch für eine schnelle Implementierung Kompromisse geben, die im Vergleich zur Berufspraxis gemacht werden - solche Fälle werden im Text gesondert erwähnt.

### Prägnanten Code schreiben
> "KISS (Keep It Simple, Stupid)"

- Je kürzer und prägnanter der Code ist, desto geringer ist natürlich das Risiko von Tippfehlern oder einfachen Bugs, und das Debugging wird erleichtert
- Der Code sollte möglichst ohne zusätzliche Kommentare leicht zu interpretieren sein, und Kommentare sollten nur bei wirklichem Bedarf für Detailerklärungen hinzugefügt werden. Es ist besser, sich auf eine klare Codestruktur zu konzentrieren als auf Kommentare
- Wenn Kommentare geschrieben werden, sollten sie klar und prägnant sein
- Eine Funktion sollte nicht mehr als drei Parameter haben; wenn mehr Parameter zusammen übergeben werden müssen, sollten sie zu einem Objekt zusammengefasst werden
- Tiefe Verschachtelungen von Bedingungen (doppelt, dreifach) beeinträchtigen die Lesbarkeit, daher sollte die Tiefe von Bedingungen möglichst vermieden werden.
  z.B. Der untere Code mit Guard Clauses ist lesbarer als der obere:

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
- Bei PS/CP werden manchmal C/C++-Makros verwendet, um den Code noch kürzer zu machen und schneller zu schreiben. Dies kann in zeitkritischen Wettbewerben nützlich sein, ist aber nur für PS/CP geeignet - im Allgemeinen sollte die Verwendung von Makros in C++ vermieden werden.
  z.B.:

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Code-Modularisierung
> "DRY (Don't Repeat Yourself)"

- Wenn derselbe Code wiederholt verwendet wird, sollte dieser Teil in Funktionen oder Klassen aufgeteilt und wiederverwendet werden
- Durch Modularisierung und aktive Wiederverwendung von Code verbessert sich die Lesbarkeit, und bei späteren Codeänderungen muss nur die entsprechende Funktion oder Klasse einmal geändert werden, was die Wartung erleichtert
- Grundsätzlich sollte eine Funktion idealerweise nur eine Aufgabe erfüllen und nicht mehrere Dinge tun. Bei PS/CP ist der Code jedoch meist klein und führt einfache Funktionen aus, sodass die Wiederverwendbarkeit begrenzt ist und die Zeitbeschränkungen es schwierig machen, die Prinzipien so streng wie in der Praxis zu befolgen.

### Nutzung von Standardbibliotheken
> "Don't reinvent the wheel"

- Beim Erlernen von Algorithmen und Datenstrukturen ist es nützlich, Datenstrukturen wie Queues und Stacks oder Sortieralgorithmen selbst zu implementieren, um die Prinzipien zu verstehen. Ansonsten ist es jedoch besser, Standardbibliotheken aktiv zu nutzen
- Standardbibliotheken wurden bereits unzählige Male verwendet und getestet und sind gut optimiert, was sie effizienter macht als eigene Implementierungen
- Die Verwendung vorhandener Bibliotheken spart Zeit, die sonst für die Implementierung identischer Funktionalitäten verschwendet würde, und macht den Code für Teammitglieder bei der Zusammenarbeit leichter verständlich

### Konsistente und klare Namenskonventionen
> "Follow standard conventions"

- Verwendung eindeutiger Variablen- und Funktionsnamen
- Jede Programmiersprache hat ihre eigenen Namenskonventionen. Man sollte die Konventionen der Standardbibliothek der verwendeten Sprache kennen und bei der Deklaration von Klassen, Funktionen und Variablen konsequent anwenden
- Die Namen von Variablen, Funktionen und Klassen sollten klar ihre Funktionalität zeigen, und bei booleschen Typen sollte deutlich sein, unter welchen Bedingungen sie True zurückgeben

### Alle Daten normalisiert speichern
- Alle Daten sollten in einem einheitlichen Format normalisiert und verarbeitet werden
- Wenn dieselben Daten in mehr als einem Format vorliegen, können subtile Bugs auftreten, wie leicht unterschiedliche Zeichendarstellungen oder unterschiedliche Hash-Werte
- Bei der Speicherung und Verarbeitung von Daten wie Zeitzonen oder Strings sollten diese sofort nach Erhalt oder Berechnung in ein Standardformat wie UTC oder UTF-8-Kodierung konvertiert werden. Die Normalisierung sollte entweder im Konstruktor der Datenklasse oder direkt in der Funktion erfolgen, die die Daten empfängt.

### Trennung von Code-Logik und Daten
- Daten, die nichts mit der Code-Logik zu tun haben, sollten nicht direkt in Bedingungen eingebettet, sondern in separate Tabellen ausgelagert werden.
  z.B. Der untere Code ist besser als der obere:

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
