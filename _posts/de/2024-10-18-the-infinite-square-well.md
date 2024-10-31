---
title: "Der eindimensionale unendliche Potentialtopf"
description: >-
  Wir betrachten das einfache, aber wichtige Modellproblem des eindimensionalen unendlichen Potentialtopfs, das grundlegende Konzepte der Quantenmechanik gut veranschaulicht. Wir bestimmen die n-te stationäre Zustandsfunktion ψ(x) und Energie E des Teilchens in dieser idealen Situation, untersuchen vier wichtige mathematische Eigenschaften von ψ(x) und leiten daraus die allgemeine Lösung Ψ(x,t) ab.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
---

## TL;DR
> - Eindimensionaler unendlicher Potentialtopf: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{sonst}
>   \end{cases}$$
> - Randbedingungen: $ \psi(0) = \psi(a) = 0 $
> - Energieniveaus des n-ten stationären Zustands: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Lösung der zeitunabhängigen Schrödinger-Gleichung im Topf:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Physikalische Interpretation jedes stationären Zustands $\psi_n$: 
>   - Form einer stehenden Welle auf einer Saite der Länge $a$
>   - **Grundzustand**: Stationärer Zustand $\psi_1$ mit der niedrigsten Energie
>   - **Angeregte Zustände**: Übrige Zustände mit $n\geq 2$, deren Energie proportional zu $n^2$ zunimmt
> - Vier wichtige mathematische Eigenschaften von $\psi_n$:
>   1. Wenn das Potential $V(x)$ symmetrisch ist, wechseln sich gerade und ungerade Funktionen bezüglich der Topfmitte ab
>   2. Mit zunehmender Energie erhöht sich die Anzahl der **Knoten** in jedem aufeinanderfolgenden Zustand um eins
>   3. Besitzt **Orthonormalität**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. Besitzt **Vollständigkeit**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Allgemeine Lösung der Schrödinger-Gleichung (Linearkombination stationärer Zustände):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{wobei } c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Voraussetzungen
- Stetige Wahrscheinlichkeitsverteilungen und Wahrscheinlichkeitsdichte
- Orthogonalität und Normierung (Lineare Algebra)
- Fourier-Reihen und Vollständigkeit (Lineare Algebra)
- [Schrödinger-Gleichung und Wellenfunktion](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfest-Theorem](/posts/ehrenfest-theorem/)
- [Zeitunabhängige Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/)

## Gegebene Potentialbedingungen
Wenn das Potential

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{sonst}
\end{cases} \tag{1}$$

ist, verhält sich das Teilchen in diesem Potential im Bereich $0<x<a$ wie ein freies Teilchen und kann an beiden Enden ($x=0$ und $x=a$) aufgrund der unendlichen Kraft nicht entkommen. In einem klassischen Modell würde dies als unendliche Hin- und Herbewegung mit vollständig elastischen Stößen an beiden Enden interpretiert werden, ohne dass nicht-konservative Kräfte wirken. Obwohl dieses Potential höchst künstlich und einfach ist, kann es gerade deshalb als nützliche Referenz dienen, wenn wir später andere physikalische Situationen in der Quantenmechanik betrachten.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Bildquelle*
> - Autor: Wikimedia-Benutzer [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Modell und Randbedingungen Aufstellen
Außerhalb des Topfes ist die Wahrscheinlichkeit, das Teilchen zu finden, $0$, also $\psi(x)=0$. Innerhalb des Topfes ist $V(x)=0$, sodass die [zeitunabhängige Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/)

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

lautet, oder

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ wobei } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

geschrieben werden kann.

> Hier nehmen wir an, dass $E\geq 0$ ist.
{: .prompt-info }

Dies ist die Gleichung, die einen klassischen **harmonischen Oszillator** beschreibt, und die allgemeine Lösung ist

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

Hier sind $A$ und $B$ beliebige Konstanten, die typischerweise durch die **Randbedingungen** des Problems bestimmt werden, wenn man eine spezielle Lösung sucht. <u>Für $\psi(x)$ sind die Randbedingungen normalerweise, dass sowohl $\psi$ als auch $d\psi/dx$ stetig sind, aber an Stellen, wo das Potential unendlich wird, ist nur $\psi$ stetig.</u>

## Lösung der zeitunabhängigen Schrödinger-Gleichung

Da $\psi(x)$ stetig ist, muss

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

gelten, um mit der Lösung außerhalb des Topfes verbunden zu sein. Aus Gleichung ($\ref{eqn:psi_general_solution}$) folgt für $x=0$

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

Setzt man ($\ref{eqn:boundary_conditions}$) ein, muss $B=0$ sein.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Dann ist $\psi(a)=A\sin{ka}$, und um ($\ref{eqn:boundary_conditions}$) mit $\psi(a)=0$ zu erfüllen, muss entweder $A=0$ (triviale Lösung) oder $\sin{ka}=0$ sein. Daher

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Auch hier ist $k=0$ eine triviale Lösung, die zu $\psi(x)=0$ führt und nicht normierbar ist, also nicht die Lösung, die wir in diesem Problem suchen. Da $\sin(-\theta)=-\sin(\theta)$, können wir das negative Vorzeichen in $A$ in Gleichung ($\ref{eqn:psi_without_B}$) absorbieren, sodass wir ohne Verlust der Allgemeinheit nur $ka>0$ betrachten müssen. Daher sind die möglichen Lösungen für $k$

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Dann ist $\psi_n=A\sin{k_n x}$ und $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, sodass wir durch Einsetzen in Gleichung ($\ref{eqn:t_independent_schrodinger_eqn}$) die möglichen $E$-Werte erhalten:

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

Im starken Gegensatz zum klassischen Fall kann ein Quantenteilchen in einem unendlichen Potentialtopf nicht beliebige Energien haben, sondern muss einen der erlaubten Werte annehmen.

> Die Energie wird durch die Randbedingungen quantisiert, die auf die Lösungen der zeitunabhängigen Schrödinger-Gleichung angewendet werden.
{: .prompt-info }

Jetzt können wir $\psi$ normieren, um $A$ zu bestimmen.

> Eigentlich normieren wir $\Psi(x,t)$, aber aufgrund von Gleichung (11) in [Zeitunabhängige Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/#1-es-sind-stationäre-zustände) entspricht dies der Normierung von $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

Dies bestimmt streng genommen nur den Betrag von $A$, aber da die Phase von $A$ keine physikalische Bedeutung hat, können wir einfach die positive reelle Quadratwurzel als $A$ verwenden. Daher ist die Lösung innerhalb des Topfes

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Physikalische Interpretation der stationären Zustände $\psi_n$
Wie in Gleichung ($\ref{eqn:psi_n}$) gezeigt, haben wir unendlich viele Lösungen für jedes Energieniveau $n$ aus der zeitunabhängigen Schrödinger-Gleichung erhalten. Die ersten paar davon sind im folgenden Bild dargestellt.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Bildquelle*
> - Autor: Wikimedia-Benutzer [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - Lizenz: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Diese Zustände haben die Form von stehenden Wellen auf einer Saite der Länge $a$. $\psi_1$ mit der niedrigsten Energie wird als **Grundzustand** bezeichnet, während die übrigen Zustände mit $n\geq 2$, deren Energie proportional zu $n^2$ zunimmt, als **angeregte Zustände** bezeichnet werden.

## Vier wichtige mathematische Eigenschaften von $\psi_n$
Alle Funktionen $\psi_n(x)$ haben die folgenden vier wichtigen Eigenschaften. Diese vier Eigenschaften sind sehr mächtig und nicht auf den unendlichen Potentialtopf beschränkt. Die erste Eigenschaft gilt immer, wenn das Potential selbst eine symmetrische Funktion ist, während die zweite, dritte und vierte Eigenschaft allgemeine Eigenschaften sind, die unabhängig von der Form des Potentials auftreten.

### 1. Gerade und ungerade Funktionen wechseln sich bezüglich der Topfmitte ab.
Für positive ganze Zahlen $n$ ist $\psi_{2n-1}$ eine gerade Funktion und $\psi_{2n}$ eine ungerade Funktion.

### 2. Mit zunehmender Energie erhöht sich die Anzahl der Knoten in jedem aufeinanderfolgenden Zustand um eins.
Für positive ganze Zahlen $n$ hat $\psi_n$ $(n-1)$ **Knoten**.

### 3. Diese Zustände besitzen Orthogonalität.

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

In diesem Sinne sind sie **orthogonal** zueinander.

> Im Fall des unendlichen Potentialtopfs, den wir gerade betrachten, ist $\psi$ reell, sodass wir die komplexe Konjugation von $\psi_m$ ($^*$) nicht benötigen würden, aber es ist eine gute Angewohnheit, sie immer hinzuzufügen, für Fälle, in denen dies nicht zutrifft.
{: .prompt-tip }

#### Beweis
Für $m\neq n$,

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

Für $m=n$ ist dieses Integral aufgrund der Normierung 1, und wir können das **Kronecker-Delta** $\delta_{mn}$ verwenden, um Orthogonalität und Normierung in einem Ausdruck zusammenzufassen:

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

In diesem Fall sagt man, $\psi$ sei **orthonormal**.

### 4. Diese Funktionen besitzen Vollständigkeit.
Jede beliebige andere Funktion $f(x)$ kann als Linearkombination

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

geschrieben werden. In diesem Sinne sind diese Funktionen **vollständig**. Gleichung ($\ref{eqn:fourier_series}$) ist die **Fourier-Reihe** von $f(x)$, und die Tatsache, dass jede Funktion so entwickelt werden kann, wird als **Dirichletscher Satz** bezeichnet.

## Berechnung der Koeffizienten $c_n$ mit dem Fourier-Trick
Wenn $f(x)$ gegeben ist, können wir die Koeffizienten $c_n$ mit der als **Fourier-Trick** bekannten Methode berechnen, indem wir die Vollständigkeit und Orthonormalität von $\psi(x)$ ausnutzen. Wir müssen nur zeigen, dass es für $t=0$ gilt, da $c_n$ zeitunabhängig ist. Multiplizieren wir beide Seiten von Gleichung ($\ref{eqn:fourier_series}$) mit $\psi_m(x)^*$ und integrieren, erhalten wir aufgrund von Gleichungen ($\ref{eqn:orthonomality}$) und ($\ref{eqn:kronecker_delta}$):

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Beachten Sie, dass aufgrund des Kronecker-Deltas alle Terme in der Summe außer dem Term mit $n=m$ verschwinden.
{: .prompt-info }

Daher ist der Koeffizient n-ter Ordnung bei der Entwicklung von $f(x)$

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Berechnung der allgemeinen Lösung $\Psi(x,t)$ der zeitabhängigen Schrödinger-Gleichung
Jeder stationäre Zustand des unendlichen Potentialtopfs ist gemäß Gleichung (10) im Beitrag ['Zeitunabhängige Schrödinger-Gleichung'](/posts/time-independent-schrodinger-equation/#1-es-sind-stationäre-zustände) und der zuvor gefundenen Gleichung ($\ref{eqn:psi_n}$)

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

Wie wir in der [Zeitunabhängigen Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/#3-die-allgemeine-lösung-der-zeitabhängigen-schrödinger-gleichung-ist-eine-linearkombination-der-separierten-lösungen) gesehen haben, kann die allgemeine Lösung der Schrödinger-Gleichung als Linearkombination stationärer Zustände ausgedrückt werden. Daher können wir schreiben:

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

Jetzt müssen wir nur noch die Koeffizienten $c_n$ finden, die die folgende Bedingung erfüllen:

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

Aufgrund der Vollständigkeit von $\psi$ existieren immer $c_n$, die dies erfüllen, und wir können sie berechnen, indem wir $\Psi(x,0)$ für $f(x)$ in Gleichung ($\ref{eqn:coefficients_n}$) einsetzen.

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

Wenn $\Psi(x,0)$ als Anfangsbedingung gegeben ist, berechnen wir die Entwicklungskoeffizienten $c_n$ mit Gleichung ($\ref{eqn:calc_of_cn}$) und setzen diese in Gleichung ($\ref{eqn:general_solution}$) ein, um $\Psi(x,t)$ zu erhalten. Danach können wir beliebige physikalische Größen nach dem Verfahren des [Ehrenfest-Theorems](/posts/ehrenfest-theorem/) berechnen. Diese Methode kann nicht nur auf den unendlichen Potentialtopf, sondern auf beliebige Potentiale angewendet werden, wobei sich lediglich die Form der $\psi$-Funktionen und die Gleichung für die erlaubten Energieniveaus ändern.

## Herleitung der Energieerhaltung ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Leiten wir die Energieerhaltung her, die wir zuvor in der [Zeitunabhängigen Schrödinger-Gleichung](/posts/time-independent-schrodinger-equation/#energieerhaltung) kurz betrachtet haben, indem wir die Orthonormalität von $\psi(x)$ (Gleichungen [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]) verwenden. Da $c_n$ zeitunabhängig ist, müssen wir nur zeigen, dass es für $t=0$ gilt.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

Außerdem gilt

$$ \hat{H}\psi_n = E_n\psi_n $$

Daher erhalten wir:

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
