---
title: Niezależne od czasu równanie Schrödingera (Time-independent Schrödinger Equation)
description: Stosując rozdzielenie zmiennych do pierwotnej postaci równania Schrödingera (zależnej od czasu) dla Ψ(x,t), wyprowadzamy niezależne od czasu równanie dla ψ(x) oraz omawiamy sens i znaczenie otrzymanych rozwiązań — matematyczne i fizyczne. Pokazujemy też, jak z superpozycji tych rozwiązań zbudować rozwiązanie ogólne.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Rozwiązanie po rozdzieleniu zmiennych: $ \Psi(x,t) = \psi(x)\phi(t)$
> - Zależność czasowa („wiggle factor”): $ \phi(t) = e^{-iEt/\hbar} $
> - Operator hamiltonianu (Hamiltonian): $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - Niezależne od czasu równanie Schrödingera: $ \hat H\psi = E\psi $
> - Znaczenie fizyczne i matematyczne rozwiązań z rozdzieleniem zmiennych:
>   1. stany stacjonarne (stationary states)
>   2. mają jednoznaczną wartość energii całkowitej $E$
>   3. rozwiązanie ogólne równania Schrödingera jest liniową kombinacją rozwiązań po rozdzieleniu zmiennych
> - Rozwiązanie ogólne zależnego od czasu równania Schrödingera: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Wymagania wstępne
- ciągłe rozkłady prawdopodobieństwa i gęstość prawdopodobieństwa
- [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/)
- [Twierdzenie Ehrenfesta](/posts/ehrenfest-theorem/)
- [Metoda rozdzielania zmiennych](/posts/Separation-of-Variables/)

## Wyprowadzenie z użyciem metody rozdzielania zmiennych
W [poście o twierdzeniu Ehrenfesta](/posts/ehrenfest-theorem/) omówiliśmy, jak za pomocą funkcji falowej $\Psi$ obliczać różne interesujące nas wielkości fizyczne. Kluczowe jest więc pytanie: jak znaleźć tę funkcję falową $\Psi(x,t)$? Zwykle należy rozwiązać — dla danego potencjału $V(x,t)$ — równanie cząstkowe względem położenia $x$ i czasu $t$, czyli [równanie Schrödingera](/posts/schrodinger-equation-and-the-wave-function/).

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

Jeśli potencjał $V$ nie zależy od czasu $t$, powyższe równanie Schrödingera można rozwiązać metodą [rozdzielania zmiennych](/posts/Separation-of-Variables/). Rozważmy rozwiązanie w postaci iloczynu funkcji zależnej wyłącznie od $x$ (oznaczmy ją $\psi$) oraz funkcji zależnej wyłącznie od $t$ (oznaczmy ją $\phi$):

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

Na pierwszy rzut oka jest to podejście absurdalnie ograniczające i może się wydawać, że pozwala znaleźć jedynie mały podzbiór wszystkich rozwiązań. W rzeczywistości jednak nie tylko ma ono istotne znaczenie, ale też z takich rozdzielalnych rozwiązań można — poprzez odpowiednie ich sumowanie — skonstruować rozwiązanie ogólne.

Dla rozwiązania rozdzielalnego zachodzi

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

więc po podstawieniu do równania ($\ref{eqn:schrodinger_eqn}$) dostajemy

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

Dzieląc obie strony przez $\psi\phi$, otrzymujemy zależność, w której lewa strona jest funkcją wyłącznie $t$, a prawa — wyłącznie $x$:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

Aby to równanie miało rozwiązanie, obie strony muszą być stałe; gdyby tak nie było, to przy utrzymaniu jednej ze zmiennych ($t$ lub $x$) na stałym poziomie i zmianie drugiej, zmieniałaby się tylko jedna strona równania, przez co równość przestałaby zachodzić. Zatem lewą stronę możemy przyrównać do stałej separacji $E$:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

Wówczas dostajemy dwa równania różniczkowe zwyczajne: pierwsze, dotyczące czasu $t$,

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

oraz drugie, dotyczące przestrzeni $x$,

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

Równanie ($\ref{eqn:ode_t}$) łatwo rozwiązać. Co prawda jego rozwiązanie ogólne ma postać $ce^{-iEt/\hbar}$, ale ponieważ interesuje nas iloczyn $\psi\phi$, stałą $c$ można włączyć do $\psi$. Otrzymujemy więc

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

Równanie dla $x$, tj. ($\ref{eqn:t_independent_schrodinger_eqn}$), nazywa się **niezależnym od czasu równaniem Schrödingera (time-independent Schrödinger equation)**. Aby je rozwiązać, trzeba znać potencjał $V(x)$.

## Znaczenie fizyczne i matematyczne
Metodą rozdzielania zmiennych otrzymaliśmy funkcję zależną wyłącznie od czasu $\phi(t)$ oraz niezależne od czasu równanie Schrödingera ($\ref{eqn:t_independent_schrodinger_eqn}$). Chociaż większości rozwiązań pierwotnego **zależnego od czasu równania Schrödingera (time-dependant Schrödinger equation)** ($\ref{eqn:schrodinger_eqn}$) nie da się zapisać w postaci $\psi(x)\phi(t)$, to jednak postać niezależna od czasu jest szczególnie ważna, ponieważ jej rozwiązania mają trzy następujące własności.

### 1. Są to stany stacjonarne (stationary states).
Funkcja falowa

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

zależy od $t$, ale gęstość prawdopodobieństwa

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

ma zależność czasową, która się redukuje, i pozostaje stała w czasie.

> Dla rozwiązań, które da się znormalizować, stała separacji $E$ musi być rzeczywista.
>
> Jeśli w ($\ref{eqn:separation_of_variables}$) przyjmiemy $E$ jako liczbę zespoloną $E_0+i\Gamma$ (gdzie $E_0$, $\Gamma$ są rzeczywiste), to
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> Jak omówiono wcześniej w tekście [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/#normalizacja-funkcji-falowej-normalization), $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ musi być stałą niezależną od czasu, więc $\Gamma=0$. $\blacksquare$
{: .prompt-info }

To samo dzieje się przy obliczaniu wartości oczekiwanych dowolnych wielkości fizycznych: wzór (8) z [twierdzenia Ehrenfesta](/posts/ehrenfest-theorem/) przyjmuje postać

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

a więc wszystkie wartości oczekiwane są stałe w czasie. W szczególności $\langle x \rangle$ jest stałe, zatem $\langle p \rangle=0$.

### 2. Jest to stan o jednoznacznej energii całkowitej $E$, a nie rozkład prawdopodobieństwa na pewnym przedziale.
W mechanice klasycznej energię całkowitą (sumę energii kinetycznej i potencjalnej) nazywa się **hamiltonianem (Hamiltonian)** i definiuje jako

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

Zatem po podstawieniu $p\to -i\hbar(\partial/\partial x)$ odpowiadający jej w mechanice kwantowej operator hamiltonianu (Hamiltonian) ma postać

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

W konsekwencji niezależne od czasu równanie Schrödingera ($\ref{eqn:t_independent_schrodinger_eqn}$) można zapisać jako

$$ \hat H \psi = E\psi \tag{15}$$

a wartość oczekiwana hamiltonianu wynosi

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

Ponadto zachodzi

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

więc

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

a zatem wariancja hamiltonianu $H$ to

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

Innymi słowy: dla rozwiązania po rozdzieleniu zmiennych, przy pomiarze energii całkowitej zawsze otrzymujemy tę samą wartość $E$.

### 3. Rozwiązanie ogólne zależnego od czasu równania Schrödingera jest liniową kombinacją rozwiązań po rozdzieleniu zmiennych.

Niezależne od czasu równanie Schrödingera ($\ref{eqn:t_independent_schrodinger_eqn}$) ma nieskończenie wiele rozwiązań $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$. Oznaczmy je jako \{$\psi_n(x)$\}. Ponieważ dla każdego z nich istnieje stała separacji $E_1,E_2,E_3,\dots=$\{$E_n$\}, to dla każdego **dopuszczalnego poziomu energii** istnieje odpowiadająca mu funkcja falowa.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

Zależne od czasu równanie Schrödingera ($\ref{eqn:schrodinger_eqn}$) ma własność liniowości: liniowa kombinacja dowolnych dwóch rozwiązań jest również rozwiązaniem. Dlatego po znalezieniu rozwiązań rozdzielalnych natychmiast otrzymujemy bardziej ogólne rozwiązanie postaci

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

Każde rozwiązanie zależnego od czasu równania Schrödingera można zapisać w powyższej postaci; pozostaje jedynie dobrać stałe $c_1, c_2, \dots$ tak, aby spełniały warunek początkowy zadany w problemie, i w ten sposób znaleźć interesujące nas rozwiązanie szczególne. Innymi słowy: gdy tylko potrafimy rozwiązać niezależne od czasu równanie Schrödingera, skonstruowanie rozwiązania ogólnego równania zależnego od czasu staje się proste.

> Rozwiązanie po rozdzieleniu zmiennych
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> jest stanem stacjonarnym, w którym wszystkie prawdopodobieństwa i wartości oczekiwane są niezależne od czasu; należy jednak pamiętać, że rozwiązanie ogólne ($\ref{eqn:general_solution}$) tej własności nie ma.
{: .prompt-warning }

## Zasada zachowania energii
W rozwiązaniu ogólnym ($\ref{eqn:general_solution}$) kwadrat modułu współczynników \{$c_n$\}, tj. $\|c_n\|^2$, ma interpretację fizyczną: oznacza prawdopodobieństwo otrzymania wartości $E_n$ przy pomiarze energii cząstki w stanie ($\Psi$). Zatem suma tych prawdopodobieństw musi wynosić 1:

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

a wartość oczekiwana hamiltonianu to

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

Ponieważ poziomy energii $E_n$ poszczególnych stanów stacjonarnych oraz współczynniki \{$c_n$\} nie zależą od czasu, zarówno prawdopodobieństwo zmierzenia danej energii $E_n$, jak i wartość oczekiwana hamiltonianu $H$, również pozostają stałe w czasie.
