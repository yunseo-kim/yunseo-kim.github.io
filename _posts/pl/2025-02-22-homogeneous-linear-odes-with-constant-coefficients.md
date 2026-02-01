---
title: "Jednorodne liniowe równanie różniczkowe zwyczajne 2. rzędu o stałych współczynnikach"
description: "Zobacz, jak znak wyróżnika równania charakterystycznego wpływa na postać rozwiązania ogólnego jednorodnego liniowego RÓZ 2. rzędu o stałych współczynnikach."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Jednorodne liniowe RÓZ 2. rzędu o stałych współczynnikach: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Równanie charakterystyczne (characteristic equation)**: $\lambda^2 + a\lambda + b = 0$
> - W zależności od znaku wyróżnika równania charakterystycznego $a^2 - 4b$ postać rozwiązania ogólnego można podzielić na trzy przypadki (jak w tabeli)
>
> | Przypadek | Rozwiązania równania charakterystycznego | Baza rozwiązań RÓZ | Rozwiązanie ogólne RÓZ |
> | :---: | :---: | :---: | :---: |
> | I | Dwa różne pierwiastki rzeczywiste<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Podwójny pierwiastek rzeczywisty<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Sprzężone pierwiastki zespolone<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Wymagania wstępne
- [Równanie Bernoulliego (Bernoulli Equation)](/posts/Bernoulli-Equation/)
- [Jednorodne liniowe równania różniczkowe zwyczajne drugiego rzędu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- wzór Eulera

## Równanie charakterystyczne (characteristic equation)
Rozważmy jednorodne liniowe równanie różniczkowe zwyczajne 2. rzędu o stałych współczynnikach $a$ i $b$

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Równania tej postaci mają istotne zastosowania m.in. w drganiach mechanicznych i elektrycznych.

Wcześniej, w poście [Równanie Bernoulliego (Bernoulli Equation)](/posts/Bernoulli-Equation/), wyznaczyliśmy rozwiązanie ogólne równania logistycznego; wynika z tego, że rozwiązaniem jednorodnego liniowego RÓZ 1. rzędu o stałym współczynniku $k$

$$ y^\prime + ky = 0 $$

jest funkcja wykładnicza $y = ce^{-kx}$. (względem równania (4) z tamtego wpisu: przypadek $A=-k$, $B=0$)

Zatem dla równania o podobnej postaci, tj. ($\ref{eqn:ode_with_constant_coefficients}$), również możemy najpierw spróbować rozwiązania w postaci

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Oczywiście jest to jedynie hipoteza i nie ma żadnej gwarancji, że rozwiązanie ogólne rzeczywiście będzie miało taką postać. Jednak niezależnie od tego, wystarczy znaleźć dwa liniowo niezależne rozwiązania, a wtedy — jak widzieliśmy w poście [Jednorodne liniowe RÓZ 2. rzędu](/posts/homogeneous-linear-odes-of-second-order/#baza-i-rozwiazanie-ogolne) — na mocy [zasady superpozycji](/posts/homogeneous-linear-odes-of-second-order/#zasada-superpozycji) można otrzymać rozwiązanie ogólne.  
> Jak za chwilę zobaczymy, zdarzają się też sytuacje, w których trzeba szukać [rozwiązania innej postaci](#ii-podwojny-pierwiastek-rzeczywisty-lambda---cfraca2).
{: .prompt-info }

Podstawiając ($\ref{eqn:general_sol}$) oraz jego pochodne

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

do równania ($\ref{eqn:ode_with_constant_coefficients}$), otrzymujemy

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Zatem jeśli $\lambda$ jest rozwiązaniem **równania charakterystycznego (characteristic equation)**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

to funkcja wykładnicza ($\ref{eqn:general_sol}$) jest rozwiązaniem RÓZ ($\ref{eqn:ode_with_constant_coefficients}$). Rozwiązując równanie kwadratowe ($\ref{eqn:characteristic_eqn}$), dostajemy

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

a stąd dwie funkcje

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

są rozwiązaniami równania ($\ref{eqn:ode_with_constant_coefficients}$).

> Terminy **równanie charakterystyczne (characteristic equation)** oraz **równanie pomocnicze (auxiliary equation)** często są używane zamiennie, ale znaczą dokładnie to samo. Można stosować dowolne z tych określeń.
{: .prompt-tip }

Teraz, w zależności od znaku wyróżnika równania charakterystycznego ($\ref{eqn:characteristic_eqn}$), tj. $a^2 - 4b$, można rozważyć trzy przypadki:
- $a^2 - 4b > 0$: dwa różne pierwiastki rzeczywiste
- $a^2 - 4b = 0$: podwójny pierwiastek rzeczywisty
- $a^2 - 4b < 0$: sprzężone pierwiastki zespolone

## Postać rozwiązania ogólnego w zależności od znaku wyróżnika równania charakterystycznego
### I. Dwa różne pierwiastki rzeczywiste $\lambda_1$ i $\lambda_2$
W tym przypadku na dowolnym przedziale bazą rozwiązań równania ($\ref{eqn:ode_with_constant_coefficients}$) jest

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

a odpowiadające rozwiązanie ogólne ma postać

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Podwójny pierwiastek rzeczywisty $\lambda = -\cfrac{a}{2}$
Gdy $a^2 - 4b = 0$, równanie kwadratowe ($\ref{eqn:characteristic_eqn}$) ma tylko jedno rozwiązanie $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, a więc rozwiązanie postaci $y = e^{\lambda x}$ jest tylko jedno:

$$ y_1 = e^{-(a/2)x} $$

Aby otrzymać bazę, musimy znaleźć drugie rozwiązanie $y_2$ o innej postaci, liniowo niezależne od $y_1$.

W takiej sytuacji można wykorzystać poznaną wcześniej metodę [redukcji rzędu](/posts/homogeneous-linear-odes-of-second-order/#redukcja-rzedu-reduction-of-order). Przyjmijmy, że szukane drugie rozwiązanie ma postać $y_2=uy_1$. Wówczas

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Po podstawieniu do równania ($\ref{eqn:ode_with_constant_coefficients}$) otrzymujemy

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Grupując wyrazy przy $u^{\prime\prime}$, $u^\prime$, $u$, dostajemy

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Ponieważ $y_1$ jest rozwiązaniem równania ($\ref{eqn:ode_with_constant_coefficients}$), wyrażenie w ostatnim nawiasie wynosi $0$, a ponadto

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

więc także wyrażenie w pierwszym nawiasie jest równe $0$. Zostaje zatem tylko $u^{\prime\prime}y_1 = 0$, skąd $u^{\prime\prime}=0$. Całkując dwukrotnie, otrzymujemy $u = c_1x + c_2$. Ponieważ stałe całkowania $c_1$ i $c_2$ mogą być dowolne, możemy po prostu wybrać $c_1=1$, $c_2=0$ i przyjąć $u=x$. Wtedy $y_2 = uy_1 = xy_1$. Ponieważ $y_1$ i $y_2$ są liniowo niezależne, tworzą bazę. Zatem w przypadku, gdy równanie charakterystyczne ($\ref{eqn:characteristic_eqn}$) ma pierwiastek podwójny, bazą rozwiązań równania ($\ref{eqn:ode_with_constant_coefficients}$) na dowolnym przedziale jest

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

a odpowiadające rozwiązanie ogólne to

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Sprzężone pierwiastki zespolone $-\cfrac{1}{2}a + i\omega$ oraz $-\cfrac{1}{2}a - i\omega$
W tym przypadku $a^2 - 4b < 0$ i $\sqrt{-1} = i$, więc z ($\ref{eqn:lambdas}$) mamy

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

Zdefiniujmy teraz liczbę rzeczywistą $\omega$ przez $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Przy takiej definicji $\omega$ rozwiązaniami równania charakterystycznego ($\ref{eqn:characteristic_eqn}$) są sprzężone pierwiastki zespolone $\lambda = -\cfrac{1}{2}a \pm i\omega$, a odpowiadające im dwa zespolone rozwiązania równania ($\ref{eqn:ode_with_constant_coefficients}$) to

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Także w tym przypadku można jednak uzyskać bazę rozwiązań rzeczywistych (nieurojonych), jak poniżej.

Korzystając ze wzoru Eulera (Euler formula)

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

oraz z równania otrzymanego po podstawieniu $t \mapsto -t$,

$$ e^{-it} = \cos t - i\sin t $$

a następnie dodając i odejmując stronami te dwa równania, dostajemy

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

Dla liczby zespolonej $z = r + it$ (z częścią rzeczywistą $r$ i urojoną $it$) funkcję wykładniczą zespoloną $e^z$ można zdefiniować za pomocą funkcji rzeczywistych $e^r$, $\cos t$ i $\sin t$ następująco:

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Podstawiając $r=-\cfrac{1}{2}ax$, $t=\omega x$, możemy napisać

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Z [zasady superpozycji](/posts/homogeneous-linear-odes-of-second-order/#zasada-superpozycji) wynika, że suma tych rozwiązań zespolonych oraz ich mnożenie przez stałą także daje rozwiązanie. Dodając stronami oba równania i mnożąc obie strony przez $\cfrac{1}{2}$, otrzymujemy pierwsze rozwiązanie rzeczywiste $y_1$:

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Analogicznie, odejmując stronami drugie równanie od pierwszego i mnożąc obie strony przez $\cfrac{1}{2i}$, dostajemy drugie rozwiązanie rzeczywiste $y_2$:

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Ponieważ $\cfrac{y_1}{y_2} = \cot{\omega x}$ nie jest stałe, funkcje $y_1$ i $y_2$ są liniowo niezależne na każdym przedziale, a więc tworzą bazę rozwiązań rzeczywistych równania ($\ref{eqn:ode_with_constant_coefficients}$). Stąd otrzymujemy rozwiązanie ogólne

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ są dowolnymi stałymi)} \label{eqn:general_sol_3}\tag{13}$$
