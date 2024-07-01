---
title: "Prinzipien für das Schreiben guten Codes"
description: >-
  Wir untersuchen die Notwendigkeit, guten Code zu schreiben, und die wichtigsten allgemeinen Prinzipien für das Schreiben guten Codes.
categories:
  - Programming
tags:
  - Coding
  - PS/CP
---
## Die Notwendigkeit, guten Code zu schreiben
Wenn man sich nur darauf konzentriert, schnell Code für die sofortige Implementierung zu schreiben, kann die [technische Schuld](/posts/Technical-debt/) auf ein nicht mehr zu bewältigendes Niveau anwachsen und später zu Wartungsproblemen führen. Daher ist es bei der Durchführung von Entwicklungsprojekten unbestreitbar wichtig, von Anfang an lesbaren und leicht zu wartenden guten Code zu schreiben.

Bei der Problemlösung (PS, Problem Solving) oder bei Programmierwettbewerben (CP, Competitive Programming) wird der zur Problemlösung verwendete Code normalerweise nach Abschluss der Problemlösung oder des Wettbewerbs nicht wiederverwendet. Insbesondere bei CP gibt es Zeitbeschränkungen, sodass man argumentieren könnte, dass eine schnelle Implementierung wichtiger ist als das Schreiben von gutem Code. Um diese Frage zu beantworten, muss man darüber nachdenken, warum man PS/CP betreibt und welche Richtung man verfolgt.

Meiner persönlichen Meinung nach kann man durch PS/CP Folgendes lernen:
- Man kann verschiedene Algorithmen und Datenstrukturen innerhalb der gegebenen Laufzeit- und Speicherbeschränkungen anwenden und erlernen. Dadurch kann man ein Gefühl dafür entwickeln, welche Algorithmen und Datenstrukturen in bestimmten Situationen bei realen Projekten am besten geeignet sind.
- Nachdem man Code geschrieben und eingereicht hat, erhält man sofort objektives Feedback über die Richtigkeit/Unrichtigkeit, Laufzeit und Speichernutzung. Dies ermöglicht es, ohne Lücken zu üben, genauen Code schnell und kompetent zu schreiben.
- Man kann den Code von anderen erfahrenen Programmierern sehen und mit dem eigenen Code vergleichen, um Verbesserungsmöglichkeiten zu finden.
- Im Vergleich zu realen Entwicklungsprojekten schreibt man wiederholt Code kleineren Umfangs mit ähnlicher Funktionalität. Dadurch kann man (besonders wenn man alleine PS übt) üben, prägnanten und guten Code zu schreiben, ohne von Fristen eingeschränkt zu sein und sich auf Details konzentrieren.

Es gibt natürlich Fälle, in denen PS/CP einfach als Hobby betrieben wird, aber für diejenigen wie mich, die PS/CP indirekt zur Verbesserung ihrer Programmierfähigkeiten nutzen, ist der letzte Punkt "Üben, guten Code zu schreiben" genauso wichtig wie die ersten drei. Das Schreiben von gutem Code ist nichts, was von Anfang an natürlich kommt, sondern etwas, das durch wiederholtes Üben kontinuierlich verbessert werden muss. Außerdem ist komplexer und schwer lesbarer Code schwierig zu debuggen und selbst für den Autor nicht einfach, auf Anhieb korrekt zu schreiben. Wenn man zu viel Zeit mit ineffizientem Debugging verbringt, kann es passieren, dass man am Ende nicht einmal besonders schnell implementiert. Obwohl PS/CP sich natürlich stark von der realen Arbeitswelt unterscheidet, ist es aus den genannten Gründen meiner Meinung nach kontraproduktiv, das Schreiben von gutem Code völlig zu vernachlässigen und sich nur auf die sofortige Implementierung zu konzentrieren. Daher versuche ich persönlich, auch bei PS/CP prägnanten und effizienten Code zu schreiben.

## Prinzipien für das Schreiben guten Codes
Ob es sich um Code handelt, der in einem Wettbewerb geschrieben wird, oder um Code, der in der Praxis geschrieben wird, die Kriterien für guten Code unterscheiden sich nicht wesentlich. In diesem Artikel werden die wichtigsten allgemeinen Prinzipien für das Schreiben guten Codes behandelt. Allerdings kann es bei PS/CP für eine schnelle Implementierung Kompromisse geben, die im Vergleich zur Praxis relativ sind. In solchen Fällen wird dies im Artikel gesondert erwähnt.

### Schreiben von prägnanten Code
> "KISS (Keep It Simple, Stupid)"
- Je kürzer und prägnanter der Code ist, desto geringer ist natürlich die Gefahr von Tippfehlern oder einfachen Bugs, und das Debugging wird erleichtert.
- Schreiben Sie den Code so, dass er möglichst ohne zusätzliche Kommentare leicht zu interpretieren ist, und fügen Sie nur bei wirklicher Notwendigkeit Kommentare für detaillierte Erklärungen hinzu. Es ist besser, die Codestruktur selbst prägnant zu halten, als sich auf Kommentare zu verlassen.
- Wenn Kommentare geschrieben werden, sollten sie klar und prägnant sein.
- Die Anzahl der an eine Funktion übergebenen Argumente sollte auf höchstens drei begrenzt werden. Wenn mehr Argumente zusammen übergeben werden müssen, sollten sie zu einem Objekt zusammengefasst werden.
- Wenn die Tiefe (depth) von Bedingungsanweisungen doppelt oder dreifach wird, beeinträchtigt dies die Lesbarkeit. Daher sollte die Erhöhung der Tiefe von Bedingungsanweisungen möglichst vermieden werden.
  z.B. Der untenstehende Code, der die Guard Clause verwendet, ist in Bezug auf die Lesbarkeit vorteilhafter als der obere Code.

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
- Bei PS/CP wird jedoch manchmal der Trick verwendet, Makros in C/C++ zu verwenden, um die Codelänge weiter zu reduzieren und schneller zu schreiben. Dies kann in zeitkritischen Wettbewerben nützlich sein, ist aber nur für PS/CP geeignet. Im Allgemeinen sollte die Verwendung von Makros in C++ vermieden werden.
  z.B.

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Code-Modularisierung
> "DRY (Don't Repeat Yourself)"
- Wenn derselbe Code wiederholt verwendet wird, trennen Sie diesen Teil in Funktionen oder Klassen zur Wiederverwendung.
- Durch aktive Wiederverwendung von Code durch Modularisierung wird die Lesbarkeit verbessert, und wenn später Codeänderungen erforderlich sind, muss nur die entsprechende Funktion oder Klasse einmal geändert werden, was die Wartung erleichtert.
- Prinzipiell ist es ideal, wenn eine Funktion nicht mehr als eine Aufgabe erfüllt und nur eine Funktionalität hat. Allerdings ist der Code, der in PS/CP geschrieben wird, meist ein kleines Programm mit einfacher Funktionalität, sodass die Wiederverwendung begrenzt ist und aufgrund der Zeitbeschränkung die Prinzipien nicht so streng wie in der Praxis befolgt werden können.

### Nutzung von Standardbibliotheken
> "Don't reinvent the wheel"
- Während es in der Lernphase von Algorithmen und Datenstrukturen nützlich ist, Datenstrukturen wie Queues und Stacks sowie Sortieralgorithmen selbst zu implementieren, um die Prinzipien zu verstehen, ist es ansonsten besser, Standardbibliotheken aktiv zu nutzen.
- Standardbibliotheken wurden bereits unzählige Male verwendet und getestet und sind gut optimiert, sodass sie effizienter sind als eine eigene Implementierung.
- Da man vorhandene Bibliotheken verwenden kann, muss man keine Zeit damit verschwenden, unnötigerweise Code mit identischer Funktionalität selbst zu implementieren, und bei der Zusammenarbeit ist es für andere Teammitglieder einfacher, den geschriebenen Code zu verstehen.

### Verwendung einer konsistenten und klaren Namenskonvention
> "Follow standard conventions"
- Verwenden Sie eindeutige Variablen- und Funktionsnamen.
- Normalerweise gibt es für jede Programmiersprache eine passende Namenskonvention. Lernen Sie die Namenskonvention, die in der Standardbibliothek der verwendeten Sprache verwendet wird, und wenden Sie sie konsistent bei der Deklaration von Klassen, Funktionen, Variablen usw. an.
- Benennen Sie so, dass klar wird, welche Funktion jede Variable, Funktion und Klasse hat, und bei booleschen Typen, unter welchen Bedingungen sie True zurückgeben.

### Normalisierung aller Daten bei der Speicherung
- Verarbeiten Sie alle Daten in einem einheitlichen, normalisierten Format.
- Wenn dieselben Daten mehr als ein Format haben, können subtile Bugs auftreten, die schwer zu erkennen sind, wie leicht unterschiedliche String-Darstellungen oder unterschiedliche Hash-Werte.
- Bei der Speicherung und Verarbeitung von Daten wie Zeitzonen und Strings sollten diese sofort nach dem Empfang oder der Berechnung in ein einheitliches Standardformat wie UTC oder UTF-8-Kodierung konvertiert werden. Es ist am besten, die Normalisierung entweder im Konstruktor der Klasse, die diese Daten repräsentiert, oder sofort in der Funktion, die die Daten empfängt, durchzuführen.

### Trennung von Logik und Daten im Code
- Daten, die nichts mit der Logik des Codes zu tun haben, sollten nicht direkt in Bedingungsanweisungen eingefügt, sondern in separate Tabellen ausgelagert werden.
  z.B. Es ist besser, den Code wie unten zu schreiben als wie oben.

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