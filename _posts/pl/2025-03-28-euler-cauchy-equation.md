---
title: "Równanie Eulera–Cauchy’ego"
description: "W zależności od znaku wyróżnika równania pomocniczego omawiamy, jaką postać przyjmuje rozwiązanie ogólne równania Eulera–Cauchy’ego w każdym z trzech przypadków."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Równanie Eulera–Cauchy’ego: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Równanie pomocnicze (auxiliary equation)**: $m^2 + (a-1)m + b = 0$
> - W zależności od znaku wyróżnika równania pomocniczego $(1-a)^2 - 4b$ postać rozwiązania ogólnego można podzielić na trzy przypadki, jak w tabeli
>
> | Przypadek | Rozwiązania równania pomocniczego | Baza rozwiązań równania Eulera–Cauchy’ego | Rozwiązanie ogólne równania Eulera–Cauchy’ego |
> | :---: | :---: | :---: | :---: |
> | I | dwa różne pierwiastki rzeczywiste<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | podwójny pierwiastek rzeczywisty<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | sprzężone pierwiastki zespolone<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Wymagania wstępne
- [Jednorodne liniowe równania różniczkowe zwyczajne drugiego rzędu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Jednorodne liniowe RÓZ 2. rzędu o stałych współczynnikach](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- wzór Eulera

## Równanie pomocnicze (auxiliary equation)
**Równanie Eulera–Cauchy’ego (Euler–Cauchy equation)** jest równaniem różniczkowym zwyczajnym postaci

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

z danymi stałymi $a$ i $b$ oraz niewiadomą funkcją $y(x)$.

Podstawiając do równania ($\ref{eqn:euler_cauchy_eqn}$)

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

otrzymujemy

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

czyli

$$ [m(m-1) + am + b]x^m = 0. $$

Stąd dostajemy równanie pomocnicze

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

a warunek konieczny i wystarczający na to, by $y=x^m$ było rozwiązaniem równania Eulera–Cauchy’ego ($\ref{eqn:euler_cauchy_eqn}$), jest taki, że $m$ jest pierwiastkiem równania pomocniczego ($\ref{eqn:auxiliary_eqn}$).

Rozwiązania równania kwadratowego ($\ref{eqn:auxiliary_eqn}$) wynoszą

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

i stąd dwie funkcje

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

są rozwiązaniami równania ($\ref{eqn:euler_cauchy_eqn}$).

Podobnie jak w poście [Jednorodne liniowe RÓZ 2. rzędu o stałych współczynnikach](/posts/homogeneous-linear-odes-with-constant-coefficients/), w zależności od znaku wyróżnika $(1-a)^2 - 4b$ równania pomocniczego ($\ref{eqn:auxiliary_eqn}$) można rozważyć trzy przypadki:
- $(1-a)^2 - 4b > 0$: dwa różne pierwiastki rzeczywiste
- $(1-a)^2 - 4b = 0$: podwójny pierwiastek rzeczywisty
- $(1-a)^2 - 4b < 0$: sprzężone pierwiastki zespolone

## Postać rozwiązania ogólnego zależnie od znaku wyróżnika równania pomocniczego
### I. Dwa różne pierwiastki rzeczywiste $m_1$ i $m_2$
W tym przypadku na dowolnym przedziale baza rozwiązań równania ($\ref{eqn:euler_cauchy_eqn}$) ma postać

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

a odpowiadające jej rozwiązanie ogólne to

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

.

### II. Podwójny pierwiastek rzeczywisty $m = \cfrac{1-a}{2}$
Gdy $(1-a)^2 - 4b = 0$, czyli $b=\cfrac{(1-a)^2}{4}$, równanie kwadratowe ($\ref{eqn:auxiliary_eqn}$) ma tylko jedno rozwiązanie $m = m_1 = m_2 = \cfrac{1-a}{2}$. Zatem jedyne rozwiązanie postaci $y = x^m$, jakie można stąd uzyskać, to

$$ y_1 = x^{(1-a)/2} $$

a równanie Eulera–Cauchy’ego ($\ref{eqn:euler_cauchy_eqn}$) przyjmuje postać

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Teraz wyznaczmy inne, liniowo niezależne rozwiązanie $y_2$, korzystając z metody [redukcji rzędu](/posts/homogeneous-linear-odes-of-second-order/#redukcja-rzedu-reduction-of-order).

Jeśli szukane drugie rozwiązanie zapiszemy jako $y_2=uy_1$, to otrzymujemy

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right). $$

Ponieważ $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$, mamy

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x}, $$

a po scałkowaniu dostajemy $u = \ln x$.

Zatem $y_2 = uy_1 = y_1 \ln x$, a ponieważ ich iloraz nie jest stały, $y_1$ i $y_2$ są liniowo niezależne. Rozwiązanie ogólne odpowiadające bazie $y_1$, $y_2$ wynosi

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

.

### III. Sprzężone pierwiastki zespolone
W tym przypadku rozwiązania równania pomocniczego ($\ref{eqn:auxiliary_eqn}$) mają postać $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$. Odpowiadające im dwa zespolone rozwiązania równania ($\ref{eqn:euler_cauchy_eqn}$) można, korzystając z faktu $x=e^{\ln x}$, zapisać następująco:

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Kładąc $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ i stosując wzór Eulera $e^{it} = \cos{t} + i\sin{t}$, otrzymujemy

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

a stąd dwa rozwiązania rzeczywiste

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

.

Ponieważ ich iloraz $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ nie jest stały, powyższe dwa rozwiązania są liniowo niezależne, a więc na mocy [zasady superpozycji](/posts/homogeneous-linear-odes-of-second-order/#zasada-superpozycji) tworzą bazę rozwiązań równania Eulera–Cauchy’ego ($\ref{eqn:euler_cauchy_eqn}$). Stąd dostajemy następujące rzeczywiste rozwiązanie ogólne:

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Należy jednak zauważyć, że przypadek sprzężonych pierwiastków zespolonych w równaniu Eulera–Cauchy’ego nie ma zwykle szczególnie dużego znaczenia praktycznego.

## Sprowadzenie do jednorodnego liniowego RÓZ 2. rzędu o stałych współczynnikach
Równanie Eulera–Cauchy’ego można przez podstawienie zmiennej sprowadzić do [jednorodnego liniowego RÓZ 2. rzędu o stałych współczynnikach](/posts/homogeneous-linear-odes-with-constant-coefficients/).

Podstawiając $x = e^t$, dostajemy

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right), $$

więc równanie Eulera–Cauchy’ego ($\ref{eqn:euler_cauchy_eqn}$) przechodzi w następujące jednorodne liniowe równanie różniczkowe zwyczajne o stałych współczynnikach względem $t$:

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

Rozwiązując równanie ($\ref{eqn:substituted}$) metodami dla [jednorodnych liniowych RÓZ 2. rzędu o stałych współczynnikach](/posts/homogeneous-linear-odes-with-constant-coefficients/) względem $t$, a następnie przechodząc z powrotem do zmiennej $x$, używając $t = \ln{x}$, otrzymamy [dokładnie ten sam wynik co wcześniej](#postac-rozwiazania-ogolnego-zaleznie-od-znaku-wyroznika-rownania-pomocniczego).
