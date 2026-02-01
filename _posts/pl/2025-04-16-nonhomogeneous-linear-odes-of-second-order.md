---
title: "Niejednorodne liniowe równania różniczkowe zwyczajne drugiego rzędu (Nonhomogeneous Linear ODEs of Second Order)"
description: "Omawiamy postać rozwiązania ogólnego niejednorodnych liniowych równań różniczkowych II rzędu i jego związek z rozwiązaniem równania jednorodnego; pokazujemy istnienie rozwiązania ogólnego oraz brak rozwiązań osobliwych."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Rozwiązanie ogólne** niejednorodnego liniowego równania różniczkowego zwyczajnego II rzędu $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: rozwiązanie ogólne równania jednorodnego $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, tj. $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: rozwiązanie szczególne danego równania niejednorodnego
> - Składnik odpowiedzi $y_p$ jest wyznaczany wyłącznie przez wejście $r(x)$; dla tego samego równania niejednorodnego $y_p$ nie zmienia się nawet przy innych warunkach początkowych. Różnica dwóch rozwiązań szczególnych równania niejednorodnego jest rozwiązaniem odpowiadającego mu równania jednorodnego.
> - **Istnienie rozwiązania ogólnego**: jeżeli współczynniki $p(x)$, $q(x)$ oraz funkcja wejściowa $r(x)$ są ciągłe, to rozwiązanie ogólne zawsze istnieje
> - **Brak rozwiązań osobliwych**: rozwiązanie ogólne obejmuje wszystkie rozwiązania równania (tzn. rozwiązanie osobliwe nie istnieje)
{: .prompt-info }

## Wymagania wstępne
- [Jednorodne liniowe równania różniczkowe zwyczajne drugiego rzędu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskian, istnienie i jednoznaczność rozwiązań](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Rozwiązanie ogólne i rozwiązanie szczególne niejednorodnego liniowego RÓZ II rzędu
Rozważmy niejednorodne liniowe równanie różniczkowe zwyczajne II rzędu

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

gdzie $r(x) \not\equiv 0$. Na otwartym przedziale $I$ **rozwiązanie ogólne** równania ($\ref{eqn:nonhomogeneous_linear_ode}$) ma postać sumy rozwiązania ogólnego odpowiadającego mu równania jednorodnego

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

tj. $y_h = c_1y_1 + c_2y_2$, oraz rozwiązania szczególnego $y_p$ równania ($\ref{eqn:nonhomogeneous_linear_ode}$):

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Ponadto na przedziale $I$ **rozwiązaniem szczególnym** równania ($\ref{eqn:nonhomogeneous_linear_ode}$) jest rozwiązanie otrzymane z ($\ref{eqn:general_sol}$) przez nadanie konkretnych wartości dowolnym stałym $c_1$ i $c_2$ w $y_h$.

Innymi słowy: jeśli do jednorodnego równania różniczkowego ($\ref{eqn:homogeneous_linear_ode}$) dodamy wejście $r(x)$ zależne wyłącznie od zmiennej niezależnej $x$, to w odpowiedzi pojawi się odpowiadający mu składnik $y_p$. Ten dodatkowy składnik odpowiedzi $y_p$ jest wyznaczany niezależnie od warunków początkowych — wyłącznie przez wejście $r(x)$. Jak zobaczymy dalej, gdy odejmiemy od siebie dowolne dwa rozwiązania $y_1$ i $y_2$ równania ($\ref{eqn:nonhomogeneous_linear_ode}$) (tj. różnicę dwóch rozwiązań szczególnych odpowiadających dwóm różnym warunkom początkowym), część $y_p$ — niezależna od warunków początkowych — znika i pozostaje jedynie różnica ${y_h}_1$ i ${y_h}_2$, która na mocy [zasady superpozycji](/posts/homogeneous-linear-odes-of-second-order/#zasada-superpozycji) jest rozwiązaniem równania ($\ref{eqn:homogeneous_linear_ode}$).

## Związek między rozwiązaniami równania niejednorodnego a rozwiązaniami odpowiadającego mu równania jednorodnego
> **Twierdzenie 1: związek między rozwiązaniami równania niejednorodnego ($\ref{eqn:nonhomogeneous_linear_ode}$) i rozwiązaniami równania jednorodnego ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Na pewnym otwartym przedziale $I$ suma rozwiązania $y$ równania niejednorodnego ($\ref{eqn:nonhomogeneous_linear_ode}$) i rozwiązania $\tilde{y}$ równania jednorodnego ($\ref{eqn:homogeneous_linear_ode}$) jest na przedziale $I$ rozwiązaniem równania ($\ref{eqn:nonhomogeneous_linear_ode}$). W szczególności wzór ($\ref{eqn:general_sol}$) jest na przedziale $I$ rozwiązaniem równania ($\ref{eqn:nonhomogeneous_linear_ode}$).  
> **(b)** Na przedziale $I$ różnica dwóch rozwiązań równania niejednorodnego ($\ref{eqn:nonhomogeneous_linear_ode}$) jest na przedziale $I$ rozwiązaniem równania jednorodnego ($\ref{eqn:homogeneous_linear_ode}$).
{: .prompt-info }

### Dowód
#### (a)
Oznaczmy lewą stronę równań ($\ref{eqn:nonhomogeneous_linear_ode}$) i ($\ref{eqn:homogeneous_linear_ode}$) przez $L[y]$. Wtedy dla dowolnego rozwiązania $y$ równania ($\ref{eqn:nonhomogeneous_linear_ode}$) oraz dowolnego rozwiązania $\tilde{y}$ równania ($\ref{eqn:homogeneous_linear_ode}$) na przedziale $I$ zachodzi

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Dla dowolnych dwóch rozwiązań $y$ i $y^\*$ równania ($\ref{eqn:nonhomogeneous_linear_ode}$) na przedziale $I$ zachodzi

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## Rozwiązanie ogólne równania niejednorodnego obejmuje wszystkie rozwiązania
Dla równania jednorodnego ($\ref{eqn:homogeneous_linear_ode}$) [wiemy, że rozwiązanie ogólne obejmuje wszystkie rozwiązania](/posts/wronskian-existence-and-uniqueness-of-solutions/#ogolne-rozwiazanie-zawiera-wszystkie-rozwiazania). Pokażmy, że dla równania niejednorodnego ($\ref{eqn:nonhomogeneous_linear_ode}$) zachodzi to samo.

> **Twierdzenie 2: rozwiązanie ogólne równania niejednorodnego obejmuje wszystkie rozwiązania**  
> Jeżeli współczynniki $p(x)$, $q(x)$ oraz funkcja wejściowa $r(x)$ równania ($\ref{eqn:nonhomogeneous_linear_ode}$) są ciągłe na pewnym otwartym przedziale $I$, to każde rozwiązanie równania ($\ref{eqn:nonhomogeneous_linear_ode}$) na przedziale $I$ można otrzymać z rozwiązania ogólnego ($\ref{eqn:general_sol}$) przez odpowiedni dobór wartości stałych $c_1$ i $c_2$ w $y_h$.
{: .prompt-info }

### Dowód
Niech $y^\*$ będzie pewnym rozwiązaniem równania ($\ref{eqn:nonhomogeneous_linear_ode}$) na $I$, a $x_0$ — pewnym punktem $x$ należącym do $I$. Na mocy [twierdzenia o istnieniu rozwiązania ogólnego dla jednorodnego RÓZ o ciągłych współczynnikach zmiennych](/posts/wronskian-existence-and-uniqueness-of-solutions/#istnienie-rozwiazania-ogolnego) istnieje $y_h = c_1y_1 + c_2y_2$, a ponadto (jak omówimy później) na mocy **metody wariacji parametrów (method of variation of parameters)** istnieje także $y_p$, więc rozwiązanie ogólne ($\ref{eqn:general_sol}$) równania ($\ref{eqn:nonhomogeneous_linear_ode}$) na przedziale $I$ istnieje. Teraz, na mocy udowodnionego wcześniej twierdzenia [1(b)](#zwiazek-miedzy-rozwiazaniami-rownania-niejednorodnego-a-rozwiazaniami-odpowiadajacego-mu-rownania-jednorodnego), funkcja $Y = y^\* - y_p$ jest na przedziale $I$ rozwiązaniem jednorodnego równania ($\ref{eqn:homogeneous_linear_ode}$), a w punkcie $x_0$ mamy

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Z [twierdzenia o istnieniu i jednoznaczności rozwiązania zadania początkowego](/posts/wronskian-existence-and-uniqueness-of-solutions/#twierdzenie-o-istnieniu-i-jednoznacznosci-rozwiazania-zadania-poczatkowego) wynika, że na przedziale $I$ dla powyższych warunków początkowych istnieje dokładnie jedno rozwiązanie szczególne $Y$ jednorodnego równania ($\ref{eqn:homogeneous_linear_ode}$), które można otrzymać przez odpowiedni dobór $c_1$, $c_2$ w $y_h$. Ponieważ $y^\* = Y + y_p$, pokazaliśmy, że dowolne rozwiązanie szczególne $y^\*$ równania niejednorodnego ($\ref{eqn:nonhomogeneous_linear_ode}$) można otrzymać z rozwiązania ogólnego ($\ref{eqn:general_sol}$). $\blacksquare$
