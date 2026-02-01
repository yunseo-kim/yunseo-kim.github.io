---
title: "Wronskian, istnienie i jednoznaczność rozwiązań"
description: "Dla jednorodnego liniowego RÓZ 2. rzędu z ciągłymi współczynnikami zmiennymi omawiamy twierdzenie o istnieniu i jednoznaczności oraz kryterium zależności/niezależności liniowej z użyciem Wronskianu."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Dla jednorodnego liniowego równania różniczkowego zwyczajnego 2. rzędu z dowolnymi ciągłymi współczynnikami zmiennymi $p$ i $q$ na przedziale $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> oraz warunków początkowych
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> zachodzą następujące 4 twierdzenia.
> 1. **Twierdzenie o istnieniu i jednoznaczności rozwiązania zagadnienia początkowego**: zagadnienie początkowe złożone z danego równania i warunków początkowych ma na przedziale $I$ jedyne rozwiązanie $y(x)$.
> 2. **Rozstrzyganie zależności/niezależności liniowej rozwiązań za pomocą Wronskianu**: dla dwóch rozwiązań $y_1$ i $y_2$ tego równania, jeśli istnieje $x_0$ na przedziale $I$ takie, że wartość **Wronskianu** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ jest równa $0$, to rozwiązania są liniowo zależne. Ponadto, jeśli istnieje $x_1$ na $I$ takie, że $W\neq 0$, to rozwiązania są liniowo niezależne.
> 3. **Istnienie rozwiązania ogólnego**: dane równanie ma na przedziale $I$ rozwiązanie ogólne.
> 4. **Brak rozwiązań osobliwych**: to rozwiązanie ogólne obejmuje wszystkie rozwiązania równania (tzn. nie istnieją rozwiązania osobliwe).
{: .prompt-info }

## Prerequisites
- [Rozwiązywanie liniowych równań różniczkowych zwyczajnych 1. rzędu](/posts/Solution-of-First-Order-Linear-ODE/)
- [Jednorodne liniowe równania różniczkowe zwyczajne drugiego rzędu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Jednorodne liniowe RÓZ 2. rzędu ze stałymi współczynnikami](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Równanie Eulera–Cauchy’ego](/posts/euler-cauchy-equation/)
- macierz odwrotna i macierz osobliwa, wyznacznik

## Jednorodne liniowe równanie różniczkowe zwyczajne z dowolnymi ciągłymi współczynnikami zmiennymi
Wcześniej poznaliśmy rozwiązania ogólne dla [jednorodnych liniowych RÓZ 2. rzędu ze stałymi współczynnikami](/posts/homogeneous-linear-odes-with-constant-coefficients/) oraz [równania Eulera–Cauchy’ego](/posts/euler-cauchy-equation/).
W tym wpisie rozszerzymy rozważania na bardziej ogólny przypadek: jednorodne liniowe RÓZ 2. rzędu z dowolnymi ciągłymi **współczynnikami zmiennymi (variable coefficient)** $p$ i $q$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

i omówimy istnienie oraz postać jego rozwiązania ogólnego. Dodatkowo zbadamy też jednoznaczność [zagadnienia początkowego](/posts/homogeneous-linear-odes-of-second-order/#zagadnienie-poczatkowe-i-warunki-poczatkowe) złożonego z równania różniczkowego ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) i następujących dwóch warunków początkowych

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Mówiąc od razu, sednem jest fakt, że <u>liniowe</u> RÓZ o ciągłych współczynnikach nie mają *rozwiązań osobliwych (singular solution)* (tj. rozwiązań, których nie da się uzyskać z rozwiązania ogólnego).

## Twierdzenie o istnieniu i jednoznaczności rozwiązania zagadnienia początkowego
> **Twierdzenie o istnieniu i jednoznaczności rozwiązania zagadnienia początkowego (Existence and Uniqueness Theorem for Initial Value Problems)**  
> Jeśli $p(x)$ i $q(x)$ są funkcjami ciągłymi na pewnym otwartym przedziale $I$, a $x_0$ należy do $I$, to zagadnienie początkowe złożone z równań ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) oraz ($\ref{eqn:initial_conditions}$) ma na $I$ jedyne rozwiązanie $y(x)$.
{: .prompt-info }

Dowodu istnienia tutaj nie omawiamy; przyjrzymy się wyłącznie dowodowi jednoznaczności. Zwykle udowodnienie jednoznaczności jest prostsze niż udowodnienie istnienia.  
Jeśli dowód Cię nie interesuje, możesz pominąć tę część i przejść do [zależności i niezależności liniowej rozwiązań](#zaleznosc-i-niezaleznosc-liniowa-rozwiazan).

### Dowód jednoznaczności
Załóżmy, że zagadnienie początkowe złożone z równania ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) i warunków ($\ref{eqn:initial_conditions}$) ma na przedziale $I$ dwa rozwiązania: $y_1(x)$ oraz $y_2(x)$. Jeśli pokażemy, że ich różnica

$$ y(x) = y_1(x) - y_2(x) $$

jest identycznie równa $0$ na $I$, to będzie to oznaczało, że $y_1 \equiv y_2$ na $I$, czyli że rozwiązanie jest jednoznaczne.

Ponieważ równanie ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) jest jednorodnym liniowym RÓZ, funkcja $y$ będąca kombinacją liniową $y_1$ i $y_2$ także jest rozwiązaniem na $I$. Ponieważ $y_1$ i $y_2$ spełniają te same warunki początkowe ($\ref{eqn:initial_conditions}$), $y$ spełnia

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Rozważmy teraz funkcję

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

oraz jej pochodną

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

Z równania różniczkowego mamy

$$ y^{\prime\prime} = -py^{\prime} - qy $$

a po podstawieniu do wyrażenia na $z^{\prime}$ otrzymujemy

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Ponieważ $y$ i $y^{\prime}$ są rzeczywiste,

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

Stąd oraz z definicji $z$ wynikają dwie nierówności

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

Z nich dostajemy $\|2yy^{\prime}\|\leq z$, a więc dla ostatniego wyrazu w ($\ref{eqn:z_prime}$) zachodzi

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Korzystając z tego oraz z faktu, że $-p \leq \|p\|$, i stosując ($\ref{eqn:inequalities}$a) do wyrazu $2yy^{\prime}$ w ($\ref{eqn:z_prime}$), otrzymujemy

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Ponieważ ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, stąd

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

Wprowadzając $h = 1 + 2\|p\| + \|q\|$, dostajemy

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

Analogicznie, z ($\ref{eqn:z_prime}$) i ($\ref{eqn:inequalities}$) wynika

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Nierówności ($\ref{eqn:inequality_6a}$) i ($\ref{eqn:inequality_6b}$) są równoważne

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

a *czynnikami całkującymi* dla lewych stron (por. [czynnik całkujący](/posts/Solution-of-First-Order-Linear-ODE/#niejednorodne-liniowe-rownania-rozniczkowe-zwyczajne)) są

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{oraz} \qquad F_2 = e^{\int h(x)\ dx} $$

Ponieważ $h$ jest ciągła, całka nieoznaczona $\int h(x)\ dx$ istnieje. Ponadto $F_1$ i $F_2$ są dodatnie, więc z ($\ref{eqn:inequalities_7}$) mamy

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

To oznacza, że na $I$ funkcja $F_1 z$ nie rośnie, a $F_2 z$ nie maleje. Ponieważ z ($\ref{eqn:initial_conditions_*}$) wynika $z(x_0) = 0$, otrzymujemy

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Na koniec dzielimy obie strony nierówności przez dodatnie $F_1$ i $F_2$, co daje jednoznaczność:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Zależność i niezależność liniowa rozwiązań
Przypomnijmy na chwilę treści z wpisu o [jednorodnych liniowych RÓZ 2. rzędu](/posts/homogeneous-linear-odes-of-second-order/#baza-i-rozwiazanie-ogolne). Rozwiązanie ogólne na otwartym przedziale $I$ buduje się z pary rozwiązań liniowo niezależnych $y_1$, $y_2$, czyli z **bazy (basis)** na $I$. To, że $y_1$ i $y_2$ są **liniowo niezależne (linearly independent)** na $I$, oznacza, że dla każdego $x$ z przedziału zachodzi

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ i }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Jeśli powyższe nie zachodzi, tzn. istnieją współczynniki $k_1$, $k_2$ niezerowe (co najmniej jeden z nich) takie, że $k_1y_1(x) + k_2y_2(x) = 0$, to $y_1$ i $y_2$ są **liniowo zależne (linearly dependent)** na $I$. Wówczas dla każdego $x$ z $I$ mamy

$$ \text{(a) } y_1 = ky_2 \quad \text{lub} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

czyli $y_1$ i $y_2$ są proporcjonalne.

Poznajmy teraz kryterium rozstrzygania zależności/niezależności liniowej.

> **Rozstrzyganie zależności/niezależności liniowej rozwiązań za pomocą Wronskianu**  
> **i.** Jeśli równanie różniczkowe ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) ma na otwartym przedziale $I$ ciągłe współczynniki $p(x)$ i $q(x)$, to warunkiem koniecznym i wystarczającym na to, aby dwa rozwiązania $y_1$ i $y_2$ równania ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) były liniowo zależne na $I$, jest to, by *wyznacznik Wrońskiego (Wronski determinant)*, w skrócie **Wronskian**, tj.
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> zerował się w pewnym punkcie $x_0$ z przedziału $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ i } y_2 \text{ są liniowo zależne} $$
>
> **ii.** Jeśli w jednym punkcie $x=x_0$ z przedziału $I$ zachodzi $W=0$, to w całym $I$ zachodzi $W=0$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> Innymi słowy, jeżeli istnieje $x_1 \in I$ takie, że $W\neq 0$, to na całym $I$ rozwiązania $y_1$, $y_2$ są liniowo niezależne.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_1)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ i } y_2 \text{ są liniowo niezależne}
> \end{align*}$$
>
{: .prompt-info }

> Wronskian został po raz pierwszy wprowadzony przez polskiego matematyka Józefa Marię Hoene-Wrońskiego, a obecną nazwę nadano mu pośmiertnie w 11882 HE przez szkockiego matematyka Sir Thomasa Muira.
{: .prompt-tip }

### Dowód
#### i. (a)
Niech $y_1$ i $y_2$ będą liniowo zależne na $I$. Wtedy na $I$ zachodzi ($\ref{eqn:linearly_dependent}$a) lub ($\ref{eqn:linearly_dependent}$b). Jeśli zachodzi ($\ref{eqn:linearly_dependent}$a), to

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

a analogicznie, gdy zachodzi ($\ref{eqn:linearly_dependent}$b), mamy

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Zatem widzimy, że <u>dla każdego $x$ z przedziału $I$</u> zachodzi $W(y_1, y_2)=0$.

#### i. (b)
Odwrotnie, załóżmy, że dla pewnego $x = x_0$ zachodzi $W(y_1, y_2)=0$. Pokażemy, że wtedy $y_1$ i $y_2$ są liniowo zależne na $I$. Rozważmy układ równań liniowych ze względu na niewiadome $k_1$, $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Można go zapisać w postaci równania wektorowego:

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

Macierzą współczynników jest

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

a jej wyznacznik jest równy $W(y_1(x_0), y_2(x_0))$. Ponieważ $\det(A) = W=0$, macierz $A$ jest **macierzą osobliwą (singular matrix)**, czyli nie ma **macierzy odwrotnej (inverse matrix)**. Zatem układ ($\ref{eqn:linear_system}$) ma rozwiązanie inne niż wektor zerowy $(0,0)$: istnieje rozwiązanie $(c_1, c_2)$, gdzie przynajmniej jedna z liczb $c_1$, $c_2$ nie jest równa $0$. Wprowadźmy teraz funkcję

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Ponieważ równanie ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) jest jednorodne liniowe, to na mocy [zasady superpozycji](/posts/homogeneous-linear-odes-of-second-order/#zasada-superpozycji) funkcja ta jest rozwiązaniem ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na $I$. Z ($\ref{eqn:linear_system}$) wynika, że spełnia warunki początkowe $y(x_0)=0$ oraz $y^{\prime}(x_0)=0$.

Z drugiej strony istnieje rozwiązanie trywialne $y^\* \equiv 0$, które spełnia te same warunki początkowe $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Ponieważ współczynniki $p$ i $q$ są ciągłe, z [twierdzenia o istnieniu i jednoznaczności zagadnienia początkowego](#twierdzenie-o-istnieniu-i-jednoznacznosci-rozwiazania-zagadnienia-poczatkowego) wynika jednoznaczność rozwiązania, a więc $y \equiv y^\*$. Innymi słowy, na $I$

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Ponieważ przynajmniej jedno z $c_1$, $c_2$ jest niezerowe, warunek ($\ref{eqn:linearly_independent}$) nie jest spełniony. Zatem $y_1$ i $y_2$ są liniowo zależne na $I$.

#### ii.
Jeśli w pewnym punkcie $x_0 \in I$ zachodzi $W(x_0)=0$, to z [i.(b)](#i-b) wynika, że $y_1$, $y_2$ są liniowo zależne na $I$, a wtedy z [i.(a)](#i-a) dostajemy $W\equiv 0$. Zatem jeśli istnieje choć jeden punkt $x_1 \in I$ taki, że $W(x_1)\neq 0$, to $y_1$ i $y_2$ są liniowo niezależne. $\blacksquare$

## Rozwiązanie ogólne obejmuje wszystkie rozwiązania
### Istnienie rozwiązania ogólnego
> Jeśli $p(x)$ i $q(x)$ są ciągłe na otwartym przedziale $I$, to równanie ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) ma na $I$ rozwiązanie ogólne.
{: .prompt-info }

#### Dowód
Na mocy [twierdzenia o istnieniu i jednoznaczności zagadnienia początkowego](#twierdzenie-o-istnieniu-i-jednoznacznosci-rozwiazania-zagadnienia-poczatkowego), równanie ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) ma na $I$ rozwiązanie $y_1(x)$ spełniające warunki początkowe

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

oraz rozwiązanie $y_2(x)$ spełniające na $I$ warunki

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

Wronskian tych dwóch rozwiązań w punkcie $x=x_0$ ma wartość niezerową:

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Zatem na mocy kryterium [zależności i niezależności liniowej rozwiązań](#zaleznosc-i-niezaleznosc-liniowa-rozwiazan) $y_1$ i $y_2$ są liniowo niezależne na $I$. W konsekwencji tworzą bazę rozwiązań równania ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na $I$, a więc rozwiązanie ogólne postaci $y = c_1y_1 + c_2y_2$ (dla dowolnych stałych $c_1$, $c_2$) istnieje na $I$. $\blacksquare$

### Brak rozwiązań osobliwych
> Jeśli równanie ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) ma na pewnym otwartym przedziale $I$ ciągłe współczynniki $p(x)$ i $q(x)$, to każde jego rozwiązanie $y=Y(x)$ na $I$ ma postać
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> gdzie $y_1$, $y_2$ tworzą bazę rozwiązań równania ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na $I$, a $C_1$, $C_2$ są pewnymi stałymi.  
> To znaczy, równanie ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) nie ma **rozwiązań osobliwych (singular solution)**, których nie dałoby się uzyskać z rozwiązania ogólnego.
{: .prompt-info }

#### Dowód
Niech $y=Y(x)$ będzie dowolnym rozwiązaniem równania ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) na $I$. Z [twierdzenia o istnieniu rozwiązania ogólnego](#istnienie-rozwiazania-ogolnego) wiemy, że równanie ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) ma na $I$ rozwiązanie ogólne

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Musimy wykazać, że dla dowolnego $Y(x)$ istnieją stałe $c_1$, $c_2$ takie, że na $I$ zachodzi $y(x)=Y(x)$. Najpierw pokażmy, że dla dowolnie wybranego $x_0 \in I$ da się dobrać $c_1$, $c_2$ tak, aby $y(x_0)=Y(x_0)$ oraz $y^{\prime}(x_0)=Y^{\prime}(x_0)$. Z ($\ref{eqn:general_solution}$) wynika

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

Ponieważ $y_1$ i $y_2$ tworzą bazę, wyznacznik macierzy współczynników, tj. $W(y_1(x_0), y_2(x_0))\neq 0$, a więc układ ($\ref{eqn:vector_equation_2}$) można rozwiązać względem $c_1$ i $c_2$. Oznaczmy rozwiązanie przez $(c_1, c_2) = (C_1, C_2)$. Po podstawieniu do ($\ref{eqn:general_solution}$) dostajemy rozwiązanie szczególne

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Ponieważ $C_1$, $C_2$ spełniają ($\ref{eqn:vector_equation_2}$),

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Z jednoznaczności w [twierdzeniu o istnieniu i jednoznaczności zagadnienia początkowego](#twierdzenie-o-istnieniu-i-jednoznacznosci-rozwiazania-zagadnienia-poczatkowego) wynika, że dla każdego $x \in I$ zachodzi $y^\* \equiv Y$. $\blacksquare$
