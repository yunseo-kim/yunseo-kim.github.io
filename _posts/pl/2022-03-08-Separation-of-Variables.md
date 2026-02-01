---
title: "Metoda rozdzielania zmiennych (Separation of Variables)"
description: "Poznaj metodę rozdzielania zmiennych i kilka powiązanych przykładów zastosowań."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Metoda rozdzielania zmiennych (Separation of Variables)

**Równanie rozdzielalne (separable equation)**: równanie, które poprzez przekształcenia algebraiczne da się sprowadzić do postaci $g(y)y'=f(x)$.

Jeśli scałkujemy obie strony równania rozdzielalnego $g(y)y'=f(x)$ względem $x$, to otrzymamy

$$ \int g(y)y'dx = \int f(x)dx + c $$

a ponieważ $y'dx=dy$, mamy

$$ \int g(y)dy = \int f(x)dx + c $$

czyli można rozdzielić wyrażenie zależne od $x$ i wyrażenie zależne od $y$ na prawą i lewą stronę. Jeżeli $f$ i $g$ są funkcjami ciągłymi, to obliczając powyższe całki, można otrzymać rozwiązanie ogólne danego równania różniczkowego. Taki sposób rozwiązywania nazywa się **metodą rozdzielania zmiennych (separation of variables)**.

## Przykład modelowania: datowanie radiowęglowe (Radiocarbon Dating)

Ötzi (Oetzi) to neolityczna mumia znaleziona w Alpach Ötztalskich (Oetztal) w roku 11991 [kalendarza holoceńskiego](https://en.wikipedia.org/wiki/Holocene_calendar). Jeśli stosunek węgla-14 do węgla-12 w tej mumii wynosi 52,5% wartości dla żywego organizmu, to mniej więcej kiedy Ötzi żył i zmarł?
> W atmosferze oraz w żywych organizmach stosunek węgla-14 do węgla-12 jest stały. Gdy organizm umiera, wchłanianie węgla-14 przez oddychanie i odżywianie ustaje, ale rozpad węgla-14 nadal zachodzi, więc udział węgla promieniotwórczego maleje. Dlatego porównując udział węgla promieniotwórczego w skamieniałości z jego udziałem w atmosferze, można oszacować wiek skamieniałości. Okres półtrwania węgla-14 wynosi 5715 lat.
{: .prompt-info }

### Rozwiązanie

Rozdzielmy zmienne w równaniu różniczkowym zwyczajnym $y'=ky$ i scałkujmy:

$$\frac {dy}{y}=k dt$$

$$ \log |y|=kt+c $$

$$ y=y_{0}e^{kt}\ (y_0=e^c) $$

Aby wyznaczyć stałą $k$, użyjemy okresu półtrwania $H=5715$.

$$ y_{0}e^{kH}=0.5y_0 $$

$$e^{kH}=0.5$$

$$ k=\frac {\log 0.5}{H}=-\frac {0.693}{5715}=-0.0001213. $$

Na koniec, aby znaleźć czas śmierci Ötziego (Oetzi) $t$, podstawiamy stosunek 52,5%:

$$ e^{kt}=e^{-.0.0001213t}=0.525$$

$$ t=\frac {\log 0.525}{-0.0001213}=5312.$$

$$ \therefore \text{około 5310 lat temu, przypuszczalnie zmarł około roku 6680 kalendarza holoceńskiego}. $$

## Przykład modelowania: problem mieszania

Na początku w zbiorniku znajduje się 1000 L wody, w której rozpuszczono 10 kg soli. Solanka wpływa z prędkością 10 L/min i zawiera 0,2 kg soli na litr. Mieszanina w zbiorniku jest dobrze mieszana i pozostaje jednorodna, a solanka wypływa z prędkością 10 L/min. Wyznacz ilość soli $y(t)$ w zbiorniku w chwili $t$.

### 1. Ustalenie modelu

$$ y'=\text{rate in} - \text{rate out}. $$

Dopływ soli wynosi 2 kg/min. Odpływ solanki na minutę stanowi 0,01 całkowitej objętości solanki, więc odpływ soli wynosi $0.01 y(t)$ na minutę. Zatem model jest równaniem różniczkowym zwyczajnym

$$y'=2-0.01y=-0.01(y-200) $$

### 2. Rozwiązanie modelu

Ułożone równanie jest rozdzielalne. Rozdzielmy zmienne, scałkujmy, a następnie przejdźmy do funkcji wykładniczej po obu stronach.

$$ \frac {dy}{y-200}=-0.01 dt $$

$$ \log |y-200| = -0.01t+c^* $$

$$ y-200=ce^{-0.01t}. $$

Początkowo w zbiorniku jest 10 kg soli, więc warunek początkowy to $y(0)=10$. Podstawiając $y=10,\ t=0$ do powyższego wzoru, otrzymujemy $10-200=ce^0=c$, zatem $c=-190$.

$$ \therefore y(t)=200-190e^{-0.01t} $$

Czyli w danej sytuacji ilość soli w zbiorniku zbiega wykładniczo do 200 kg.

## Przykład modelowania: prawo stygnięcia Newtona (Newton's Law of Cooling)

Zimą temperatura w ciągu dnia w pewnym budynku biurowym jest utrzymywana na poziomie 20℃. Ogrzewanie wyłącza się o 22:00 i włącza ponownie o 6:00. Pewnego dnia o 2:00 w nocy temperatura wewnątrz budynku wynosiła 17,4℃. Na zewnątrz o 22:00 było 10℃, a o 6:00 spadło do 4℃. Jaka była temperatura wewnątrz budynku o 6:00, gdy ogrzewanie się włączało?
> **Prawo stygnięcia Newtona (Newton's law of cooling)**  
> Szybkość zmiany temperatury $T$ pewnego ciała w czasie jest proporcjonalna do różnicy temperatury między ciałem a jego otoczeniem.
{: .prompt-info }

### 1. Ustalenie modelu

Niech $T(t)$ oznacza temperaturę wewnątrz budynku, a $T_A$ — temperaturę na zewnątrz. Wówczas z prawa stygnięcia Newtona mamy

$$ \frac {dT}{dt}=k(T-T_A) $$

### 2. Rozwiązanie ogólne

Wiemy jedynie, że $T_A$ zmienia się między 10℃ a 4℃, ale nie znamy dokładnej wartości, więc nie da się rozwiązać wcześniej ułożonego równania. W takiej sytuacji pomocne bywa *uproszczenie sytuacji do łatwiejszego problemu i próba rozwiązania*. Średnia z dwóch znanych wartości wynosi 7℃, więc załóżmy, że nieznana funkcja $T_A$ jest stała i równa $T_A=7$. Nawet jeśli to przybliżenie nie jest dokładne, można oczekiwać uzyskania przybliżonej wartości temperatury wewnątrz budynku $T$ o 6:00.

Dla stałej $T_A=7$ wcześniej ułożone równanie jest rozdzielalne. Rozdzielając zmienne, całkując i przechodząc do funkcji wykładniczej, otrzymujemy rozwiązanie ogólne.

$$ \frac {dT}{T-7}=k dt $$

$$ \log |T-7|=kt+c^* $$

$$ T(t)=7+ce^{kt} \quad(c=e^{c^*}).$$

### 3. Rozwiązanie szczególne

Wybieramy 22:00 jako $t=0$, więc warunek początkowy to $T(0)=20$. Oznaczmy otrzymane rozwiązanie szczególne przez $T_p$. Podstawiając:

$$ T(0)=7+ce^0=20 $$

$$ c=20-7=13 $$

$$ T_p(t)=7+13e^{kt}. $$

### 4. Wyznaczenie $k$

O 2:00 w nocy temperatura wewnątrz budynku wynosiła 17,4℃, więc $T(4)=17.4$. Wyznaczając algebraicznie $k$ i podstawiając do $T_p(t)$:

$$ T_p(4)=7+13e^{4k}=17.4 $$

$$ e^{4k}=0.8 $$

$$ k=\frac {1}{4} \log 0.8=-0.056 $$

$$ T_p(t)=7+13e^{-0.056t}. $$

### 5. Odpowiedź i interpretacja

Ponieważ 6:00 odpowiada $t=8$, mamy

$$ T_p(8)=7+13e^{-0.056\cdot8}=15.3\text{[℃]}. $$

## Przykład modelowania: twierdzenie Torricellego (Torricelli's Theorem)

Zbiornik ma średnicę 2 m, otwór ma średnicę 1 cm, a początkowa wysokość wody przy otwarciu otworu wynosi 2,25 m. Wyznacz wysokość wody w zbiorniku w dowolnej chwili oraz czas, po jakim zbiornik się opróżni.
> **Twierdzenie Torricellego (Torricelli's theorem)**  
> Prędkość wypływu wody pod wpływem grawitacji wynosi
>
> $$ v(t)=0.600\sqrt{2gh(t)}. $$
>
> $h(t)$: wysokość słupa wody nad otworem w chwili $t$  
> $g=980\text{cm/s²}$: przyspieszenie grawitacyjne na powierzchni Ziemi
{: .prompt-info }

### 1. Ustalenie modelu

Objętość wypływu $\Delta V$ w krótkim czasie $\Delta t$ wynosi

$$ \Delta V = Av\Delta t \qquad (A: \text{pole przekroju otworu})$$

Musi ona być równa zmianie objętości wody w zbiorniku $\Delta V^*$. Ponadto

$$ \Delta V^* = -B\Delta h \qquad (B: \text{pole przekroju zbiornika}) $$

gdzie $\Delta h(>0)$ jest spadkiem wysokości wody $h(t)$. Zrównując $\Delta V$ i $\Delta V^*$, otrzymujemy

$$ -B\Delta h = Av\Delta t $$

Teraz, korzystając z twierdzenia Torricellego, wyrażamy $v$, a następnie przechodzimy z $\Delta t$ do granicy dążącej do zera, uzyskując model opisany równaniem różniczkowym zwyczajnym pierwszego rzędu:

$$ \frac {\Delta h}{\Delta t} = -\frac {A}{B}v = -\frac{A}{B}0.600\sqrt{2gh(t)} $$

$$ \frac {dh}{dt} = \lim_{t\to0}\frac {\Delta h}{\Delta t} = -26.56\frac {A}{B}\sqrt{h}. $$

### 2. Rozwiązanie ogólne

To równanie jest rozdzielalne. Rozdzielając zmienne i całkując, dostajemy

$$ \frac {dh}{\sqrt{h}} = -26.56\frac{A}{B}dt $$

$$ 2\sqrt{h} = c^* - 26.56\frac{A}{B}t $$

Dzieląc obie strony przez 2 i podnosząc do kwadratu, otrzymujemy $h=(c-13.28At/B)^2$. Podstawiając $13.28A/B=13.28 \cdot 0.5^2 \pi /100^2 \pi = 0.000332$, uzyskujemy rozwiązanie ogólne

$$ h(t)=(c-0.000332t)^2 $$

### 3. Rozwiązanie szczególne

Warunek początkowy to $h(0)=225\text{cm}$. Podstawiając $t=0$ i $h=225$, z rozwiązania ogólnego otrzymujemy $c^2=225, c=15.00$, a zatem rozwiązanie szczególne

$$ h_p(t)=(15.00-0.000332t)^2 $$

### 4. Czas opróżnienia zbiornika

$$ t = 15.00/0.000332 = 45181 \text{[s]} = 12.6 \text{[h]}. $$

## Sprowadzenie do postaci rozdzielalnej (separable form)

Zdarza się, że równanie różniczkowe zwyczajne, które nie jest rozdzielalne, można uczynić rozdzielalnym poprzez wprowadzenie nowej niewiadomej funkcji zależnej od $y$.

$$ y'=f\left(\frac {y}{x}\right). $$

Rozwiązując takie równanie, podstawmy $y/x=u$. Wtedy

$$ y=ux,\quad y'=u'x+u $$

Zatem po podstawieniu do $y'=f(y/x)$ otrzymujemy $u'x=f(u)-u$. Jeżeli $f(u)-u\neq0$, to

$$ \frac {du}{f(u)-u}=\frac {dx}{x} $$

co daje postać rozdzieloną.
