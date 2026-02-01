---
title: Prawa ruchu Newtona
description: Omówienie praw ruchu Newtona i znaczenia trzech zasad, definicji masy bezwładnej i grawitacyjnej oraz zasady równoważności, kluczowej nie tylko w mechanice klasycznej, ale też w ogólnej teorii względności.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Prawa ruchu Newtona**
> 1. O ile nie działa siła zewnętrzna, ciało pozostaje w spoczynku albo porusza się ruchem jednostajnym prostoliniowym.
> 2. Szybkość zmian pędu ciała w czasie jest równa sile działającej na to ciało.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Gdy dwa ciała oddziałują na siebie siłami, siły te mają jednakową wartość i przeciwny zwrot.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Zasada równoważności (principle of equivalence)**
> - masa bezwładna: masa, która — dla zadanej siły — wyznacza przyspieszenie ciała
> - masa grawitacyjna: masa, która wyznacza oddziaływanie grawitacyjne między danym ciałem a innym ciałem
> - obecnie wiadomo, że masa bezwładna i grawitacyjna są jednoznacznie zgodne z dokładnością rzędu $10^{-12}$
> - twierdzenie, że masa bezwładna i masa grawitacyjna są dokładnie równe, nazywa się **zasadą równoważności**
{: .prompt-info }

## Prawa ruchu Newtona
Prawa ruchu Newtona to trzy zasady ogłoszone przez Isaaca Newtona (Issac Newton) w roku 11687 [kalendarza holoceńskiego](https://en.wikipedia.org/wiki/Holocene_calendar) w dziele *Philosophiæ Naturalis Principia Mathematica* (matematyczne zasady filozofii przyrody, w skrócie „*Principia*”); stanowią one fundament mechaniki newtonowskiej (Newtonian mechanics).

1. O ile nie działa siła zewnętrzna, ciało pozostaje w spoczynku albo porusza się ruchem jednostajnym prostoliniowym.
2. Szybkość zmian pędu ciała w czasie jest równa sile działającej na to ciało.
3. Gdy dwa ciała oddziałują na siebie siłami, siły te mają jednakową wartość i przeciwny zwrot.

### Pierwsze prawo Newtona
> I. O ile nie działa siła zewnętrzna, ciało pozostaje w spoczynku albo porusza się ruchem jednostajnym prostoliniowym.

Ciało, na które nie działa siła zewnętrzna, nazywa się **ciałem swobodnym (free body)** albo **cząstką swobodną (free particle)**.
Należy jednak zauważyć, że samo pierwsze prawo dostarcza jedynie jakościowego pojęcia siły.

### Drugie prawo Newtona
> II. Szybkość zmian pędu ciała w czasie jest równa sile działającej na to ciało.

Newton zdefiniował **pęd (momentum)** jako iloczyn masy i prędkości

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

Z tego drugie prawo Newtona można zapisać następująco:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Pierwsze i drugie prawo Newtona — wbrew nazwie — są w istocie bliższe „definicji” siły niż „prawu”. Można też zauważyć, że definicja siły zależy od definicji „masy”.

### Trzecie prawo Newtona
> III. Gdy dwa ciała oddziałują na siebie siłami, siły te mają jednakową wartość i przeciwny zwrot.

Jest to prawo fizyczne znane również jako „zasada akcji i reakcji” i ma zastosowanie w przypadku, gdy siła wywierana przez jedno ciało na drugie jest skierowana wzdłuż prostej łączącej dwa punkty przyłożenia. Tego typu siłę nazywa się **siłą centralną (central force)**; trzecie prawo zachodzi niezależnie od tego, czy siła centralna jest przyciągająca, czy odpychająca. Przykładami sił centralnych są grawitacja lub siła elektrostatyczna między dwoma spoczywającymi ciałami, a także siła sprężystości. Z kolei siły między poruszającymi się ładunkami, grawitacja między poruszającymi się ciałami itp., czyli siły zależne od prędkości dwóch oddziałujących obiektów, należą do sił niecentralnych — w takich przypadkach nie da się zastosować trzeciego prawa.

Uwzględniając omówioną wcześniej definicję masy, trzecie prawo można przeformułować następująco:

> III$^\prime$. Jeżeli dwa ciała tworzą idealny układ izolowany, to ich przyspieszenia mają przeciwne zwroty, a stosunek ich wartości bezwzględnych jest równy odwrotnemu stosunkowi mas tych ciał.

Z trzeciego prawa Newtona wynika

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

a podstawiając do tego drugie prawo ($\ref{eqn:2nd_law}$), otrzymujemy

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Stąd widać, że w izolowanym oddziaływaniu dwóch cząstek pęd jest zachowany.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Ponadto w równaniu ($\ref{eqn:3rd-1_law}$) mamy $\vec{p}=m\vec{v}$, a masa $m$ jest stała, zatem

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

co prowadzi do

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Trzecie prawo Newtona opisuje sytuację, w której dwa ciała tworzą układ izolowany, jednak w praktyce zrealizowanie tak idealnych warunków jest niemożliwe — dlatego twierdzenie Newtona w ramach trzeciego prawa można uznać za dość zuchwałe. Mimo że wniosek ten został wyprowadzony z ograniczonych obserwacji, dzięki głębokiej intuicji fizycznej Newtona mechanika newtonowska przez niemal 300 lat utrzymywała mocną pozycję i nie wykazywała błędów w weryfikacjach eksperymentalnych. Dopiero w latach 11900. stały się możliwe na tyle precyzyjne pomiary, by wykazać różnice między przewidywaniami teorii Newtona a rzeczywistością — co doprowadziło do narodzin teorii względności i mechaniki kwantowej.

## Masa bezwładna i masa grawitacyjna
Jednym ze sposobów wyznaczania masy ciała jest użycie narzędzia takiego jak waga szalkowa i porównanie ciężaru badanego obiektu ze wzorcem. Metoda ta wykorzystuje fakt, że ciężar ciała w polu grawitacyjnym jest równy wartości siły grawitacji działającej na to ciało; w tym przypadku drugie prawo $\vec{F}=m\vec{a}$ przyjmuje postać $\vec{W}=m\vec{g}$. Metoda ta opiera się na podstawowym założeniu, że masa $m$ zdefiniowana w III$^\prime$ jest równa masie $m$ występującej w równaniu grawitacji. Te dwie masy nazywa się odpowiednio **masą bezwładną (inertial mass)** i **masą grawitacyjną (gravitational mass)** i definiuje następująco:

- masa bezwładna: masa, która — dla zadanej siły — wyznacza przyspieszenie ciała
- masa grawitacyjna: masa, która wyznacza oddziaływanie grawitacyjne między danym ciałem a innym ciałem

Choć jest to opowieść wymyślona później i niezwiązana bezpośrednio z Galileuszem (Galileo Galilei), eksperyment myślowy zrzucania ciał z wieży w Pizie był pierwszym, który sugerował, że masa bezwładna i masa grawitacyjna mogą być równe. Newton również próbował wykazać brak różnic między tymi masami, mierząc okresy wahadeł o tej samej długości, lecz o różnych masach ciężarków; jednak ze względu na prymitywną metodę i niewystarczającą dokładność nie udało mu się tego jednoznacznie potwierdzić.

Później, pod koniec lat 11800., węgierski fizyk Eötvös Loránd Ágoston przeprowadził eksperyment Eötvösa, aby precyzyjnie zmierzyć różnicę między masą bezwładną a grawitacyjną, i potwierdził ich równość z dość dużą dokładnością (błąd nie większy niż 1 na 20 milionów).

W jeszcze nowszych eksperymentach, przeprowadzanych m.in. przez Roberta Henry’ego Dicke’a (Robert Henry Dicke), dokładność tę dodatkowo poprawiono; obecnie wiadomo, że masa bezwładna i masa grawitacyjna są jednoznacznie zgodne w granicach błędu rzędu $10^{-12}$. Wynik ten ma ogromne znaczenie w ogólnej teorii względności, a twierdzenie, że masa bezwładna i masa grawitacyjna są dokładnie równe, nazywa się **zasadą równoważności (principle of equivalence)**.
