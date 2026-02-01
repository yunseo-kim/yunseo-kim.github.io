---
title: Dług techniczny (Technical debt)
description: "Poznaj pojęcie długu technicznego, przyczyny jego powstawania oraz sposoby minimalizowania go w procesie wytwarzania oprogramowania."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Dług techniczny
> **Dług techniczny (Technical debt)**  
> cena, którą trzeba będzie zapłacić w przyszłości, gdy w procesie rozwoju — aby natychmiast spełnić wymagania — wybiera się „drogę na skróty”, pozwalającą szybciej domknąć projekt tu i teraz
{: .prompt-info }

Tak jak w księgowości, zaciągając dług (debt) i pożyczając pieniądze, można szybko zainwestować tam, gdzie jest to potrzebne, ale później odczuwa się presję finansową i trzeba spłacić kapitał wraz z odsetkami, tak samo wytwarzając oprogramowanie: jeśli — aby rozwiązać bieżące wymagania — rozwija się je szybko, nawet jeśli jest to nieco „brudne”, kod staje się złożony i powielony, co w przyszłości utrudnia implementację nowych funkcji lub rozbudowę.

Podobnie jak firma może dzięki długowi w odpowiednim czasie zrealizować większe inwestycje, aby opracować nowy produkt i zwiększyć udział w rynku, a osoba prywatna może dzięki kredytowi kupić dom, tak też zaakceptowanie długu technicznego i szybka implementacja nowych funkcji nie jest z definicji czymś wyłącznie złym. Pożądane jest jednak ograniczanie narastania długu technicznego i zarządzanie nim na możliwym do udźwignięcia poziomie.

## Dlaczego powstaje dług techniczny
Nawet jeśli kompetencje programisty są wystarczające, w trakcie rozwoju oprogramowania dług techniczny powstaje nieuchronnie i nie da się go całkowicie wyeliminować u źródła.  
Gdy w miarę rozwoju usługi dotychczas zaprojektowany kod natrafia na swoje ograniczenia, może zajść potrzeba modyfikacji istniejącej architektury — nawet jeśli wcześniej był to kod czytelny i dobrze działający.  
Ponadto wraz z rozwojem technologii może się okazać, że biblioteki/frameworki, które kiedyś były standardem, przestają być używane; wtedy można zdecydować się na zmianę stosu technologicznego na inne biblioteki/frameworki — i również w takim przypadku wcześniej napisany kod staje się pewnego rodzaju długiem technicznym.

Oprócz tego dług techniczny może powstawać z następujących powodów:
- brak terminowej dokumentacji tego, co zostało zaprojektowane w trakcie projektu, przez co innym osobom — albo po czasie samemu sobie — trudno jest zinterpretować dany kod
- nieusuwanie zmiennych lub pól/pozycji w bazie danych, których już się nie używa
- nieautomatyzowanie czynności powtarzalnych (wdrożenie/budowanie itp.), co każdorazowo wymaga dodatkowego czasu i wysiłku
- pilna zmiana specyfikacji

## Jak minimalizować dług techniczny
### Ustalenie zasad (Convention) między programistami
- jeśli projekt nie jest realizowany w pojedynkę, dla sprawnej współpracy potrzebne są uzgodnienia dot. używanego języka lub stosu technologicznego, struktury katalogów projektu, stylu programowania itd.
- należy zdecydować, do jakiego stopnia ujednolicić sposób pracy, a od którego miejsca pozostawić swobodę jednostce
- potrzebne są code review, aby wzajemnie weryfikować styl pracy i wymieniać opinie

### Pisanie Clean Code i refaktoryzacja (Refactoring)
- jeśli istniejący kod jest „brudny” i przeszkadza w rozwoju, można spłacić dług techniczny poprzez refaktoryzację, czyli uporządkowanie struktury kodu
- oczywiście im bardziej istniejący kod jest „spaghetti code”, tym trudniejsza staje się refaktoryzacja; w skrajnych przypadkach rezygnuje się z refaktoryzacji, porzuca stary kod i tworzy rozwiązanie od zera
- w miarę możliwości warto od początku starać się pisać kod czytelny i łatwy w utrzymaniu
