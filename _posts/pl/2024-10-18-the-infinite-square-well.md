---
title: 1-wymiarowa nieskończona studnia potencjału (The 1D Infinite Square Well)
description: Prosty, ale kluczowy problem mechaniki kwantowej: 1D nieskończona studnia. Wyznaczamy n-ty stan stacjonarny ψ(x) i energię E, omawiamy 4 własności ψ(x) oraz konstruujemy rozwiązanie ogólne Ψ(x,t).
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Problem 1D nieskończonej studni:
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{w przeciwnym razie}
>   \end{cases}$$
> - Warunki brzegowe: $ \psi(0) = \psi(a) = 0 $
> - Poziomy energii $n$-tego stanu stacjonarnego: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Rozwiązanie równania Schrödingera niezależnego od czasu wewnątrz studni:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Interpretacja fizyczna poszczególnych stanów stacjonarnych $\psi_n$:
>   - postać fali stojącej na strunie o długości $a$
>   - **stan podstawowy (ground state)**: stan stacjonarny $\psi_1$ o najniższej energii
>   - **stany wzbudzone (excited states)**: pozostałe stany dla $n\geq 2$, których energia rośnie proporcjonalnie do $n^2$
> - 4 ważne własności matematyczne $\psi_n$:
>   1. jeśli potencjał $V(x)$ ma symetrię, to względem środka studni na przemian pojawiają się funkcje parzyste i nieparzyste
>   2. im większa energia, tym każdy kolejny stan ma o jeden więcej **węzeł (node)**
>   3. spełniają **ortonormalność (orthonormality)**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases}
>      \end{gather*} $$
>
>   4. spełniają **zupełność (completeness)**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Rozwiązanie ogólne równania Schrödingera (kombinacja liniowa stanów stacjonarnych):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{gdzie współczynniki }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Wymagania wstępne
- ciągłe rozkłady prawdopodobieństwa i gęstość prawdopodobieństwa
- ortogonalność i normalizacja (algebra liniowa)
- szeregi Fouriera i zupełność (algebra liniowa)
- [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/)
- [Twierdzenie Ehrenfesta](/posts/ehrenfest-theorem/)
- [Równanie Schrödingera niezależne od czasu](/posts/time-independent-schrodinger-equation/)

## Zadany potencjał
Jeśli potencjał jest równy

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{w przeciwnym razie}
\end{cases} \tag{1}$$

to cząstka wewnątrz tego potencjału jest w zakresie $0<x<a$ cząstką swobodną, natomiast na obu końcach ($x=0$ oraz $x=a$) działa na nią nieskończenie wielka siła, przez co nie może uciec. W klasycznym modelu interpretuje się to jako ruch tam i z powrotem z doskonale sprężystymi zderzeniami, bez udziału sił niezachowawczych — czyli nieskończony ruch wahadłowy. Choć taki potencjał jest skrajnie sztuczny i uproszczony, właśnie dlatego może stanowić użyteczny punkt odniesienia przy analizie innych sytuacji fizycznych w dalszej nauce mechaniki kwantowej, więc warto go uważnie prześledzić.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Model i warunki brzegowe
Poza studnią prawdopodobieństwo znalezienia cząstki wynosi $0$, więc $\psi(x)=0$. Wewnątrz studni $V(x)=0$, zatem [równanie Schrödingera niezależne od czasu](/posts/time-independent-schrodinger-equation/) ma postać

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

czyli

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ gdzie } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

> Przyjmujemy tu założenie $E\geq 0$.
{: .prompt-info }

Jest to równanie opisujące klasyczny **oscylator harmoniczny (simple harmonic oscillator)**, a rozwiązanie ogólne ma postać

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

gdzie $A$ i $B$ są dowolnymi stałymi. Przy wyznaczaniu rozwiązania szczególnego odpowiadającego sytuacji z zadania stałe te są typowo wyznaczane z **warunków brzegowych**. <u>W przypadku $\psi(x)$ zwykle warunkiem brzegowym jest ciągłość zarówno $\psi$, jak i $d\psi/dx$, jednak w punktach, gdzie potencjał staje się nieskończony, ciągła jest tylko $\psi$.</u>

## Wyznaczenie rozwiązania równania Schrödingera niezależnego od czasu

Ponieważ $\psi(x)$ jest ciągła, musi zachodzić

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

aby rozwiązanie dało się połączyć z rozwiązaniem na zewnątrz studni. W równaniu ($\ref{eqn:psi_general_solution}$) dla $x=0$ mamy

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

zatem po podstawieniu ($\ref{eqn:boundary_conditions}$) musi być $B=0$.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Wtedy $\psi(a)=A\sin{ka}$, więc aby spełnić $\psi(a)=0$ z ($\ref{eqn:boundary_conditions}$), trzeba mieć albo $A=0$ (rozwiązanie trywialne), albo $\sin{ka}=0$. Stąd

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Podobnie, $k=0$ daje rozwiązanie trywialne $\psi(x)=0$, którego nie da się znormalizować, więc nie jest to rozwiązanie, którego szukamy. Ponadto, ponieważ $\sin(-\theta)=-\sin(\theta)$, znak minus można wchłonąć w stałą $A$ z równania ($\ref{eqn:psi_without_B}$). Dlatego bez straty ogólności można rozważać wyłącznie przypadek $ka>0$. Zatem dopuszczalne wartości $k$ to

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Wówczas $\psi_n=A\sin{k_n x}$ oraz $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, więc po podstawieniu do ($\ref{eqn:t_independent_schrodinger_eqn}$) otrzymujemy możliwe wartości $E$:

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

W ostrym kontraście do przypadku klasycznego, cząstka kwantowa w nieskończonej studni kwadratowej nie może mieć dowolnej energii — musi przyjmować jedną z dozwolonych wartości.

> Energia ulega skwantowaniu wskutek warunków brzegowych nałożonych na rozwiązanie równania Schrödingera niezależnego od czasu.
{: .prompt-info }

Teraz możemy znormalizować $\psi$ i wyznaczyć $A$.

> Formalnie normalizuje się $\Psi(x,t)$, ale na mocy równania (11) z posta [Równanie Schrödingera niezależne od czasu](/posts/time-independent-schrodinger-equation/#1-stany-stacjonarne-stationary-states) jest to równoważne normalizacji $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

Ściśle rzecz biorąc wyznacza to tylko moduł $A$, ale faza $A$ nie ma żadnego znaczenia fizycznego, więc można po prostu przyjąć dodatni rzeczywisty pierwiastek jako $A$. Zatem rozwiązanie wewnątrz studni ma postać

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Interpretacja fizyczna poszczególnych stanów stacjonarnych $\psi_n$
Jak w ($\ref{eqn:psi_n}$), z równania Schrödingera niezależnego od czasu otrzymaliśmy nieskończenie wiele rozwiązań odpowiadających kolejnym poziomom energii $n$. Jeśli narysujemy kilka pierwszych z nich, otrzymamy wykresy jak na poniższym rysunku.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Stany te mają postać fali stojącej na strunie o długości $a$. Stan $\psi_1$ o najniższej energii nazywa się **stanem podstawowym (ground state)**, a pozostałe stany dla $n\geq 2$, których energia rośnie proporcjonalnie do $n^2$, nazywa się **stanami wzbudzonymi (excited states)**.

## 4 ważne własności matematyczne $\psi_n$
Wszystkie funkcje $\psi_n(x)$ mają następujące cztery istotne własności. Są one bardzo silne i nie ograniczają się wyłącznie do nieskończonej studni kwadratowej. Pierwsza własność zachodzi zawsze, gdy sam potencjał jest funkcją o symetrii, natomiast druga, trzecia i czwarta są własnościami ogólnymi, występującymi niezależnie od kształtu potencjału.

### 1. Względem środka studni na przemian pojawiają się funkcje parzyste i nieparzyste.
Dla dodatniej liczby całkowitej $n$ funkcja $\psi_{2n-1}$ jest parzysta, a $\psi_{2n}$ jest nieparzysta.

### 2. Im większa energia, tym każdy kolejny stan ma o jeden więcej węzłów.
Dla dodatniej liczby całkowitej $n$ funkcja $\psi_n$ ma $(n-1)$ **węzłów (node)**.

### 3. Te stany mają ortogonalność (orthogonality).

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

czyli są wzajemnie **ortogonalne (orthogonal)**.

> W rozważanej nieskończonej studni kwadratowej $\psi$ jest rzeczywista, więc nie trzeba brać sprzężenia zespolonego ($^*$) dla $\psi_m$, ale warto wyrobić w sobie nawyk zawsze je zapisywać na wypadek ogólniejszych sytuacji.
{: .prompt-tip }

#### Dowód
Dla $m\neq n$:

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

Dla $m=n$ całka ta wynosi $1$ na mocy normalizacji, a używając **delty Kroneckera (Kronecker delta)** $\delta_{mn}$ można jednocześnie zapisać ortogonalność i normalizację jako

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

Wtedy mówi się, że $\psi$ jest **ortonormalna (orthonormal)**.

### 4. Te funkcje mają zupełność (completeness).
W sensie, że dowolną inną funkcję $f(x)$ można zapisać jako kombinację liniową

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

funkcje te są **zupełne (complete)**. Równanie ($\ref{eqn:fourier_series}$) jest **szeregiem Fouriera (Fourier series)** funkcji $f(x)$, a fakt, że dowolną funkcję można w ten sposób rozwinąć, nazywa się **twierdzeniem Dirichleta (Dirichlet's theorem)**.

## Wyznaczenie współczynników $c_n$ metodą Fouriera (Fourier's trick)
Gdy dana jest funkcja $f(x)$, to korzystając z powyższej zupełności (completeness) i ortonormalności (orthonormality) można wyznaczyć współczynniki $c_n$ następującą metodą, znaną jako **metoda Fouriera (Fourier's trick)**. Mnożąc obustronnie ($\ref{eqn:fourier_series}$) przez $\psi_m(x)^*$ i całkując, na mocy ($\ref{eqn:orthonomality}$) oraz ($\ref{eqn:kronecker_delta}$) otrzymujemy

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Zwróć uwagę, że dzięki delcie Kroneckera w sumie znikają wszystkie wyrazy poza tym z $n=m$.
{: .prompt-info }

Zatem przy rozwinięciu $f(x)$ współczynnik rzędu $n$ wynosi

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Wyznaczenie rozwiązania ogólnego $\Psi(x,t)$ równania Schrödingera zależnego od czasu
Każdy stan stacjonarny nieskończonej studni kwadratowej, na mocy [równania (10) z posta „Równanie Schrödingera niezależne od czasu”](/posts/time-independent-schrodinger-equation/#1-stany-stacjonarne-stationary-states) oraz wcześniej otrzymanego ($\ref{eqn:psi_n}$), ma postać

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

Ponadto w [Równaniu Schrödingera niezależnym od czasu](/posts/time-independent-schrodinger-equation/#3-ogolne-rozwiazanie-rownania-schrodingera-zaleznego-od-czasu-jest-kombinacja-liniowa-rozwiazan-z-metody-rozdzielenia-zmiennych) widzieliśmy, że rozwiązanie ogólne równania Schrödingera można wyrazić jako kombinację liniową stanów stacjonarnych. Zatem

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

Pozostaje jedynie znaleźć współczynniki $c_n$ spełniające warunek

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

Dzięki zupełności $\psi$ współczynniki $c_n$ spełniające powyższe równanie zawsze istnieją i można je wyznaczyć podstawiając $\Psi(x,0)$ za $f(x)$ w ($\ref{eqn:coefficients_n}$):

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

Gdy zadany jest warunek początkowy $\Psi(x,0)$, korzystamy z ($\ref{eqn:calc_of_cn}$), aby znaleźć współczynniki rozwinięcia $c_n$, a następnie podstawiamy je do ($\ref{eqn:general_solution}$), otrzymując $\Psi(x,t)$. Potem, zgodnie z procedurą z posta o [twierdzeniu Ehrenfesta](/posts/ehrenfest-theorem/), można obliczyć dowolną interesującą wielkość fizyczną. Metoda ta działa nie tylko dla nieskończonej studni kwadratowej, ale dla dowolnego potencjału — zmienia się jedynie postać funkcji $\psi$ oraz wzory na dozwolone poziomy energii.

## Wyprowadzenie zasady zachowania energii ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Korzystając z ortonormalności $\psi(x)$ (równania [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]) wyprowadźmy zachowanie energii, które krótko omawialiśmy wcześniej w poście [Równanie Schrödingera niezależne od czasu](/posts/time-independent-schrodinger-equation/#zachowanie-energii). Ponieważ $c_n$ nie zależą od czasu, wystarczy wykazać to dla $t=0$.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

Ponadto, ponieważ

$$ \hat{H}\psi_n = E_n\psi_n $$

otrzymujemy

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
