---
title: "Jednorodne liniowe równania różniczkowe zwyczajne drugiego rzędu (Homogeneous Linear ODEs of Second Order)"
description: "Poznaj definicję i cechy liniowych równań różniczkowych zwyczajnych 2. rzędu; omówimy zasadę superpozycji dla równań jednorodnych oraz wynikające z niej pojęcie bazy (basis)."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Postać standardowa** 2. rzędu liniowego równania różniczkowego zwyczajnego: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **współczynniki (coefficients)**: funkcje $p$, $q$
>   - **wejście (input)**: $r(x)$
>   - **wyjście (output)** lub **odpowiedź (response)**: $y(x)$
> - Jednorodne i niejednorodne
>   - **jednorodne (homogeneous)**: w postaci standardowej $r(x)\equiv0$
>   - **niejednorodne (nonhomogeneous)**: w postaci standardowej $r(x)\not\equiv 0$
> - **zasada superpozycji (superposition principle)**: dla <u>jednorodnego</u> liniowego RÓZ $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ dowolna kombinacja liniowa dwóch rozwiązań na otwartym przedziale $I$ również jest rozwiązaniem. Innymi słowy, suma dowolnych rozwiązań danego jednorodnego liniowego RÓZ oraz ich mnożenie przez stałą także daje rozwiązanie tego równania.
> - **baza (basis)** lub **układ fundamentalny (fundamental system)**: para $(y_1, y_2)$ rozwiązań jednorodnego liniowego RÓZ liniowo niezależnych na przedziale $I$
> - **redukcja rzędu (reduction of order)**: dla jednorodnego RÓZ 2. rzędu, jeśli potrafimy znaleźć jedno rozwiązanie, to drugie rozwiązanie liniowo niezależne (czyli bazę) można wyznaczyć, rozwiązując RÓZ 1. rzędu; metodę tę nazywa się redukcją rzędu
> - Zastosowania redukcji rzędu: ogólne RÓZ 2. rzędu $F(x, y, y^\prime, y^{\prime\prime})=0$ (liniowe lub nieliniowe) można w następujących przypadkach sprowadzić do równania 1. rzędu:
>   - gdy $y$ nie występuje jawnie
>   - gdy $x$ nie występuje jawnie
>   - gdy jest jednorodne liniowe i znamy już jedno rozwiązanie
{: .prompt-info }

## Prerequisites
- [Podstawowe pojęcia modelowania (Modeling)](/posts/Basic-Concepts-of-Modeling/)
- [Metoda rozdzielania zmiennych (Separation of Variables)](/posts/Separation-of-Variables/)
- [Rozwiązywanie liniowych równań różniczkowych zwyczajnych 1. rzędu](/posts/Solution-of-First-Order-Linear-ODE/)

## Liniowe równania różniczkowe zwyczajne 2. rzędu
Równanie różniczkowe zwyczajne 2. rzędu

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

nazywa się **liniowym (linear)**, jeśli można je zapisać w tej postaci; w przeciwnym razie jest **nieliniowe (nonlinear)**.

Gdy $p$, $q$, $r$ są funkcjami zmiennej $x$, równanie to jest liniowe względem $y$ oraz jego pochodnych.

Postać jak w ($\ref{eqn:standard_form}$) nazywa się **postacią standardową (standard form)** liniowego RÓZ 2. rzędu. Jeśli pierwszy wyraz danego liniowego RÓZ 2. rzędu ma postać $f(x)y^{\prime\prime}$, to dzieląc obie strony równania przez $f(x)$, można otrzymać postać standardową.

Funkcje $p$, $q$ nazywa się **współczynnikami (coefficients)**, $r(x)$ — **wejściem (input)**, a $y(x)$ — **wyjściem (output)** lub **odpowiedzią (response)** na wejście i warunki początkowe.

### Jednorodne liniowe równania różniczkowe zwyczajne 2. rzędu
Niech $J$ oznacza pewien przedział $a<x<b$, na którym chcemy rozwiązać ($\ref{eqn:standard_form}$). Jeśli w ($\ref{eqn:standard_form}$) na przedziale $J$ zachodzi $r(x)\equiv 0$, to

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

i takie równanie nazywa się **jednorodnym (homogeneous)**.

## Niejednorodne liniowe równania różniczkowe zwyczajne
Jeśli na przedziale $J$ zachodzi $r(x)\not\equiv 0$, to równanie nazywa się **niejednorodnym (nonhomogeneous)**.

## Zasada superpozycji

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ są dowolnymi stałymi)}\tag{3}$$

Funkcję tej postaci nazywa się **kombinacją liniową (linear combination)** funkcji $y_1$ i $y_2$.

Wtedy zachodzi następujące twierdzenie.

> **zasada superpozycji (superposition principle)**  
> Dla jednorodnego liniowego RÓZ ($\ref{eqn:homogeneous_linear_ode}$) dowolna kombinacja liniowa dwóch rozwiązań na otwartym przedziale $I$ jest również rozwiązaniem równania ($\ref{eqn:homogeneous_linear_ode}$). Innymi słowy, suma dowolnych rozwiązań danego jednorodnego liniowego RÓZ oraz ich mnożenie przez stałą także daje rozwiązanie tego równania.
{: .prompt-info }

### Dowód
Niech $y_1$ oraz $y_2$ będą rozwiązaniami równania ($\ref{eqn:homogeneous_linear_ode}$) na przedziale $I$. Podstawiając $y=c_1y_1+c_2y_2$ do ($\ref{eqn:homogeneous_linear_ode}$), otrzymujemy

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

co jest tożsamością. Zatem $y$ jest rozwiązaniem równania ($\ref{eqn:homogeneous_linear_ode}$) na przedziale $I$. $\blacksquare$

> Należy zauważyć, że zasada superpozycji zachodzi wyłącznie dla jednorodnych liniowych równań różniczkowych zwyczajnych; nie jest spełniona dla liniowych równań niejednorodnych ani dla równań nieliniowych.
{: .prompt-warning }

## Baza i rozwiązanie ogólne
### Przypomnienie kluczowych pojęć z równań 1. rzędu
Jak widzieliśmy wcześniej w [Podstawowe pojęcia modelowania (Modeling)](/posts/Basic-Concepts-of-Modeling/), zagadnienie początkowe (Initial Value Problem) dla RÓZ 1. rzędu składa się z równania różniczkowego oraz warunku początkowego (initial condition) $y(x_0)=y_0$. Warunek początkowy jest potrzebny do wyznaczenia dowolnej stałej $c$ w rozwiązaniu ogólnym danego równania, a tak wyznaczone rozwiązanie nazywa się rozwiązaniem szczególnym. Rozszerzmy teraz te pojęcia na równania 2. rzędu.

### Zagadnienie początkowe i warunki początkowe
**Zagadnienie początkowe (initial value problem)** dla jednorodnego RÓZ 2. rzędu ($\ref{eqn:homogeneous_linear_ode}$) składa się z danego równania różniczkowego ($\ref{eqn:homogeneous_linear_ode}$) oraz dwóch **warunków początkowych (initial conditions)**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Warunki te są potrzebne do wyznaczenia dwóch dowolnych stałych $c_1$ oraz $c_2$ w **rozwiązaniu ogólnym (general solution)**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Niezależność i zależność liniowa
Na chwilę przyjrzyjmy się pojęciom niezależności i zależności liniowej. Aby zdefiniować bazę, potrzebujemy je rozumieć.  
Jeżeli dla dwóch funkcji $y_1$ i $y_2$ zdefiniowanych na przedziale $I$, w każdym punkcie tego przedziału zachodzi

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ i }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

to mówimy, że $y_1$ i $y_2$ są **liniowo niezależne (linearly independent)** na przedziale $I$. W przeciwnym razie są **liniowo zależne (linearly dependent)**.

Jeśli $y_1$ oraz $y_2$ są liniowo zależne (tj. gdy zdanie ($\ref{eqn:linearly_independent}$) nie jest prawdziwe), to można podzielić obie strony równania w ($\ref{eqn:linearly_independent}$) przez $k_1 \neq 0$ lub $k_2 \neq 0$ i zapisać

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{lub} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

co pokazuje, że $y_1$ i $y_2$ są proporcjonalne.

### Baza, rozwiązanie ogólne, rozwiązanie szczególne
Wracając: aby ($\ref{eqn:general_sol}$) było rozwiązaniem ogólnym, $y_1$ i $y_2$ muszą być rozwiązaniami równania ($\ref{eqn:homogeneous_linear_ode}$) oraz jednocześnie nie mogą być proporcjonalne na przedziale $I$, tzn. muszą być liniowo niezależne (linearly independent). Parę $(y_1, y_2)$ rozwiązań równania ($\ref{eqn:homogeneous_linear_ode}$), liniowo niezależnych na przedziale $I$, nazywa się na przedziale $I$ **bazą (basis)** lub **układem fundamentalnym (fundamental system)** rozwiązań równania ($\ref{eqn:homogeneous_linear_ode}$).

Wykorzystując warunki początkowe, wyznaczamy dwie stałe $c_1$ oraz $c_2$ w rozwiązaniu ogólnym ($\ref{eqn:general_sol}$), otrzymując jedyne rozwiązanie przechodzące przez punkt $(x_0, K_0)$ i o nachyleniu stycznej w tym punkcie równym $K_1$. Rozwiązanie to nazywa się **rozwiązaniem szczególnym (particular solution)** równania ($\ref{eqn:homogeneous_linear_ode}$).

Jeśli ($\ref{eqn:homogeneous_linear_ode}$) jest ciągłe na otwartym przedziale $I$, to ma koniecznie rozwiązanie ogólne, które obejmuje wszystkie możliwe rozwiązania szczególne. Innymi słowy, w tym przypadku równanie ($\ref{eqn:homogeneous_linear_ode}$) nie ma rozwiązań osobliwych (singular solution), których nie dałoby się otrzymać z rozwiązania ogólnego.

## Redukcja rzędu (reduction of order)
Dla jednorodnego RÓZ 2. rzędu, jeśli potrafimy znaleźć jedno rozwiązanie, to drugie rozwiązanie liniowo niezależne od niego, czyli bazę, można wyznaczyć w następujący sposób przez rozwiązanie RÓZ 1. rzędu. Metodę tę nazywa się **redukcją rzędu (reduction of order)**.

<u>Dla jednorodnego liniowego RÓZ 2. rzędu w postaci standardowej</u>, tj. z $y^{\prime\prime}$ (a nie $f(x)y^{\prime\prime}$),

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

załóżmy, że znamy jedno rozwiązanie $y_1$ na otwartym przedziale $I$.

Niech szukane drugie rozwiązanie ma postać $y_2 = uy_1$. Wówczas

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Po podstawieniu do równania otrzymujemy

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Grupując wyrazy przy $u^{\prime\prime}$, $u^{\prime}$ i $u$, dostajemy

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Ponieważ $y_1$ jest rozwiązaniem danego równania, wyrażenie w ostatnim nawiasie wynosi $0$, więc wyraz z $u$ znika i zostaje równanie różniczkowe względem $u^{\prime}$ oraz $u^{\prime\prime}$. Dzieląc obie strony przez $y_1$ oraz podstawiając $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$, otrzymujemy równanie 1. rzędu

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Stosując [rozdzielanie zmiennych](/posts/Separation-of-Variables/) i całkując, dostajemy

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

a po podniesieniu obu stron do wykładnika otrzymujemy ostatecznie

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Ponieważ wcześniej przyjęliśmy $U=u^{\prime}$, mamy $u=\int U dx$, a zatem drugie rozwiązanie $y_2$ wynosi

$$ y_2 = uy_1 = y_1 \int U dx $$

Ponieważ $\cfrac{y_2}{y_1} = u = \int U dx$ nie może być stałą (o ile $U>0$), $y_1$ oraz $y_2$ tworzą bazę rozwiązań.

### Zastosowania redukcji rzędu
Ogólne RÓZ 2. rzędu $F(x, y, y^\prime, y^{\prime\prime})=0$ — niezależnie od tego, czy jest liniowe czy nieliniowe — można sprowadzić do równania 1. rzędu metodą redukcji rzędu, gdy $y$ nie występuje jawnie, gdy $x$ nie występuje jawnie albo (jak wyżej) gdy jest to równanie jednorodne liniowe i znamy już jedno rozwiązanie.

#### Gdy $y$ nie występuje jawnie
Jeśli w $F(x, y^\prime, y^{\prime\prime})=0$ podstawimy $z=y^{\prime}$, to możemy sprowadzić problem do RÓZ 1. rzędu względem $z$: $F(x, z, z^{\prime})$.

#### Gdy $x$ nie występuje jawnie
Jeśli w $F(y, y^\prime, y^{\prime\prime})=0$ podstawimy $z=y^{\prime}$, to

$y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$,

więc możemy sprowadzić problem do RÓZ 1. rzędu względem $z$, w którym $y$ pełni rolę zmiennej niezależnej zamiast $x$: $F(y,z,z^\prime)$.
