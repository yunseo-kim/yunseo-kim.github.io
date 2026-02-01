---
title: Zasady pisania dobrego kodu
description: "O potrzebie pisania dobrego kodu oraz najważniejszych, ogólnych zasadach, które pomagają tworzyć kod czytelny i łatwy w utrzymaniu."
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## Potrzeba pisania dobrego kodu
Jeśli skupiać się wyłącznie na szybkim napisaniu kodu „na już”, pod [dług techniczny](/posts/Technical-debt/) może urosnąć do poziomu nie do udźwignięcia, a później pojawią się problemy z utrzymaniem. Dlatego podczas prowadzenia projektu developerskiego pisanie od początku czytelnego i łatwego w utrzymaniu dobrego kodu jest bezsprzecznie ważne.

W przypadku rozwiązywania zadań algorytmicznych (PS, Problem Solving) lub zawodów programistycznych (CP, Competitive Programming) często po zakończeniu zadania czy konkursu nie ma potrzeby ponownego użycia kodu, a zwłaszcza w CP, gdzie obowiązują limity czasu, można usłyszeć opinię, że ważniejsza jest szybka implementacja niż pisanie dobrego kodu. Aby odpowiedzieć na to pytanie, warto zastanowić się, po co w ogóle uprawiasz PS/CP i jaki kierunek chcesz obrać.

Moim zdaniem, jeśli poza ogólnym kształceniem umiejętności rozwiązywania problemów spojrzeć wyłącznie od strony programistycznej, to rzeczy, których można nauczyć się dzięki PS/CP, są następujące:
- W trakcie rozwiązywania problemów w zadanych ograniczeniach czasu i pamięci można wypróbować i opanować różne algorytmy oraz struktury danych; dzięki temu w realnych projektach łatwiej wyczuć, jakich algorytmów i struktur danych użyć w konkretnej sytuacji
- Po napisaniu i wysłaniu kodu natychmiast dostaje się obiektywny feedback: poprawne/niepoprawne, czas wykonania oraz zużycie pamięci — można więc ćwiczyć szybkie i sprawne pisanie *dokładnego* kodu bez pomijania szczegółów
- Można oglądać kod napisany przez innych zaawansowanych uczestników, porównywać z własnym i znajdować obszary do poprawy
- Ponieważ wielokrotnie pisze się relatywnie małe fragmenty kodu o podobnej funkcjonalności (w porównaniu z realnym projektem), da się ćwiczyć pisanie zwięzłego i dobrego kodu, zwracając uwagę na detale i (zwłaszcza gdy ćwiczysz PS samodzielnie) nie będąc przywiązanym do terminów

Oczywiście PS/CP można traktować po prostu jako hobby, ale jeśli robisz PS/CP po to, by podnieść umiejętności programistyczne, to ostatnia korzyść — „ćwiczenie pisania dobrego kodu” — jest równie duża jak poprzednie trzy. Pisanie dobrego kodu nie przychodzi naturalnie od razu; trzeba je systematycznie doskonalać przez powtarzalną praktykę. Co więcej, kod złożony i trudny w czytaniu ciężko się debuguje, a nawet Tobie samemu trudniej go napisać poprawnie za pierwszym razem — przez co łatwo tracić czas na nieefektywne debugowanie i finalnie wcale nie implementować tak szybko. PS/CP oczywiście różni się od realnej pracy, ale mimo to całkowite ignorowanie jakości kodu i skupianie się wyłącznie na doraźnej implementacji jest (z powodów powyżej) odwróceniem priorytetów. Dlatego osobiście uważam, że także w PS/CP warto pisać kod zwięzły i efektywny.

> Komentarz dodany 12024.12:  
> Patrząc na obecne trendy, budowanie zaplecza wiedzy do pisania wydajnych programów (algorytmy, struktury danych itp.) oraz rozwijanie umiejętności rozwiązywania problemów wciąż będzie mieć sens, ale na etapie przekuwania tego w działający kod nie warto już koniecznie upierać się, by wszystko pisać samodzielnie. Lepiej aktywnie korzystać z AI, takiej jak GitHub Copilot, Cursor czy Windsurf, oszczędzić czas i przeznaczyć go na inne zadania lub naukę. Oczywiście jeśli robisz PS/CP dla ogólnej umiejętności rozwiązywania problemów, do nauki algorytmów/struktur danych albo po prostu jako hobby — nie ma powodu, by Cię od tego odciągać. Natomiast wkładanie czasu i wysiłku w PS/CP wyłącznie po to, by ćwiczyć samo pisanie kodu, wydaje się dziś mieć znacznie niższy zwrot z inwestycji. Co więcej, nawet w zawodach stricte developerskich znaczenie testów programistycznych jako etapu rekrutacji prawdopodobnie zauważalnie spadnie w porównaniu z dotychczasowym.
{: .prompt-warning }

## Zasady pisania dobrego kodu
Niezależnie od tego, czy kod jest pisany na konkurs, czy w pracy, warunki, które pozwalają nazwać go „dobrym”, nie różnią się znacząco. W tym wpisie omawiam główne zasady, które ogólnie pomagają pisać dobry kod. Trzeba jednak pamiętać, że w PS/CP, dla szybkiej implementacji, czasem idzie się na większe kompromisy niż w praktyce zawodowej — takie przypadki zaznaczę osobno w tekście.

### Pisanie zwięzłego kodu
> "KISS(Keep It Simple, Stupid)"

- Im krótszy i bardziej zwięzły kod, tym mniejsze ryzyko literówek i prostych bugów oraz łatwiejsze debugowanie
- W miarę możliwości pisać tak, by kod dało się łatwo zrozumieć nawet bez osobnych komentarzy; komentarze dodawać tylko wtedy, gdy naprawdę są potrzebne, aby uzupełnić szczegółowe wyjaśnienia. Lepiej niż polegać na komentarzach, jest utrzymać prostą strukturę samego kodu.
- Jeśli piszesz komentarze, rób to jasno i zwięźle
- Liczbę argumentów przekazywanych do jednej funkcji ograniczać do 3; jeśli trzeba przekazać więcej, zgrupować je w jeden obiekt
- Gdy zagnieżdżenie warunków (depth) robi się podwójne lub potrójne, spada czytelność — dlatego należy unikać niepotrzebnego pogłębiania zagnieżdżenia.  
  ex) W porównaniu z kodem powyżej, kod poniżej wykorzystujący idiom *Guard Clause* jest korzystniejszy pod względem czytelności  

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
- Jednak w PS/CP czasem, idąc krok dalej, stosuje się „sztuczki” w postaci makr C/C++, żeby skrócić kod i pisać szybciej. Może to być przydatne w konkursach o dużej presji czasu, ale jest to metoda, która sprawdza się głównie w PS/CP; generalnie używania makr w C++ należy unikać.  
  ex)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularyzacja kodu
> "DRY(Don't Repeat Yourself)"

- Gdy ten sam kod jest używany wielokrotnie, wydzielić go do funkcji lub klasy i używać ponownie
- Aktywne ponowne wykorzystywanie kodu dzięki modularyzacji poprawia czytelność, a gdy później trzeba coś zmienić, wystarczy zmodyfikować daną funkcję lub klasę tylko raz — co ułatwia utrzymanie
- Zasadniczo idealnie jest, gdy jedna funkcja nie robi dwóch lub więcej rzeczy, tylko realizuje jedną odpowiedzialność. Jednak kod pisany w PS/CP to zwykle małe programy o prostych funkcjach, przez co możliwości ponownego użycia są ograniczone, a czas jest limitowany — więc może być trudno przestrzegać tych zasad tak rygorystycznie jak w pracy.

### Wykorzystywanie bibliotek standardowych
> "Don't reinvent the wheel"

- Na etapie nauki algorytmów i struktur danych przydatne jest samodzielne implementowanie struktur typu kolejka czy stos oraz algorytmów sortowania, by zrozumieć zasadę działania; poza tym lepiej aktywnie korzystać z bibliotek standardowych
- Biblioteki standardowe były używane i weryfikowane niezliczoną liczbę razy oraz są dobrze zoptymalizowane, więc zwykle są wydajniejsze niż własna implementacja od zera
- Skoro można użyć istniejącej biblioteki, nie ma sensu marnować czasu na ręczne pisanie kodu o tej samej funkcjonalności, a w pracy zespołowej innym członkom zespołu łatwiej jest zrozumieć taki kod

### Stosowanie spójnego i jednoznacznego nazewnictwa
> "Follow standard conventions"

- Używać niemających dwuznaczności nazw zmiennych i funkcji
- Dla większości języków programowania istnieją właściwe im konwencje nazewnictwa (naming convention) — warto poznać te stosowane w bibliotece standardowej danego języka i konsekwentnie je stosować przy deklarowaniu klas, funkcji, zmiennych itd.
- Nazywać tak, aby było jasne, co robi każda zmienna/funkcja/klasa, a w przypadku typu boolean — przy jakim warunku zwracane jest True

### Wszystkie dane przechowuj w postaci znormalizowanej
- Wszystkie dane należy przetwarzać poprzez normalizację do jednego, spójnego formatu
- Jeśli te same dane mogą występować w co najmniej dwóch formatach, mogą pojawić się trudne do wyłapania subtelne bugi (np. minimalnie różniące się reprezentacje tekstowe albo inne wartości hashy)
- Przy zapisie i przetwarzaniu danych takich jak strefy czasowe czy napisy, należy je konwertować do jednego standardowego formatu (np. UTC, kodowanie UTF-8) natychmiast po wczytaniu lub po wykonaniu obliczeń. Dobrą praktyką jest wykonywać normalizację od razu w konstruktorze klasy reprezentującej te dane albo bezpośrednio w funkcji, która je wczytuje.

### Rozdziel logikę kodu od danych
- Danych niezwiązanych z logiką kodu nie należy umieszczać bezpośrednio wewnątrz instrukcji warunkowych; należy je wydzielić do osobnej tabeli  
  ex) W porównaniu z kodem powyżej, zaleca się pisać jak w kodzie poniżej.

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
