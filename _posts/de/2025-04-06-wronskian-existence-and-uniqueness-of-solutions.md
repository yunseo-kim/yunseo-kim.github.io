---
title: Wronskian, Existenz und Eindeutigkeit der Lösung
description: Für eine homogene lineare Differentialgleichung zweiter Ordnung mit beliebigen stetigen Koeffizienten untersuchen wir den Existenz- und Eindeutigkeitssatz für Anfangswertprobleme, die Methode zur Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels Wronskian sowie den Beweis, dass solche Gleichungen stets eine allgemeine Lösung besitzen, die alle möglichen Lösungen umfasst.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> Für eine homogene lineare Differentialgleichung zweiter Ordnung mit beliebigen stetigen Koeffizienten $p$ und $q$ auf einem Intervall $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> und die Anfangsbedingungen
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> gelten die folgenden vier Sätze:
> 1. **Existenz- und Eindeutigkeitssatz für Anfangswertprobleme**: Das durch die gegebene Differentialgleichung und die Anfangsbedingungen definierte Anfangswertproblem besitzt auf dem Intervall $I$ eine eindeutige Lösung $y(x)$.
> 2. **Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels Wronskian**: Für zwei Lösungen $y_1$ und $y_2$ der Differentialgleichung gilt: Wenn es einen Punkt $x_0$ im Intervall $I$ gibt, an dem der **Wronskian** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ den Wert $0$ annimmt, dann sind die beiden Lösungen linear abhängig. Wenn es einen Punkt $x_1$ im Intervall $I$ gibt, an dem $W\neq 0$ gilt, dann sind die beiden Lösungen linear unabhängig.
> 3. **Existenz der allgemeinen Lösung**: Die gegebene Differentialgleichung besitzt auf dem Intervall $I$ eine allgemeine Lösung.
> 4. **Nichtexistenz singulärer Lösungen**: Diese allgemeine Lösung umfasst alle Lösungen der Differentialgleichung (d.h., es gibt keine singulären Lösungen).
{: .prompt-info }

## Voraussetzungen
- [Lösung linearer Differentialgleichungen erster Ordnung](/posts/Solution-of-First-Order-Linear-ODE/)
- [Homogene lineare Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogene lineare Differentialgleichungen zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Euler-Cauchy-Gleichung](/posts/euler-cauchy-equation/)
- Inverse Matrix und singuläre Matrix, Determinante

## Homogene lineare Differentialgleichungen mit beliebigen stetigen Koeffizienten
In früheren Beiträgen haben wir die allgemeinen Lösungen für [homogene lineare Differentialgleichungen zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/) und [Euler-Cauchy-Gleichungen](/posts/euler-cauchy-equation/) untersucht.
In diesem Beitrag erweitern wir unsere Betrachtung auf den allgemeineren Fall einer homogenen linearen Differentialgleichung zweiter Ordnung mit beliebigen stetigen **variablen Koeffizienten** $p$ und $q$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Wir untersuchen die Existenz und Form der allgemeinen Lösung dieser Differentialgleichung. Zusätzlich betrachten wir die Eindeutigkeit des [Anfangswertproblems](/posts/homogeneous-linear-odes-of-second-order/#anfangswertproblem-und-anfangsbedingungen), das durch die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) und die folgenden Anfangsbedingungen definiert ist:

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Vorwegnehmend sei gesagt, dass der Kernpunkt unserer Betrachtung darin liegt, dass <u>lineare</u> Differentialgleichungen mit stetigen Koeffizienten keine *singulären Lösungen* (Lösungen, die nicht aus der allgemeinen Lösung abgeleitet werden können) besitzen.

## Existenz- und Eindeutigkeitssatz für Anfangswertprobleme
> **Existenz- und Eindeutigkeitssatz für Anfangswertprobleme**  
> Wenn $p(x)$ und $q(x)$ auf einem offenen Intervall $I$ stetige Funktionen sind und $x_0$ ein Punkt in diesem Intervall ist, dann besitzt das durch die Gleichungen ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) und ($\ref{eqn:initial_conditions}$) definierte Anfangswertproblem auf dem Intervall $I$ eine eindeutige Lösung $y(x)$.
{: .prompt-info }

Auf den Beweis der Existenz werden wir hier nicht eingehen, sondern nur den Beweis der Eindeutigkeit betrachten. In der Regel ist der Beweis der Eindeutigkeit einfacher als der Beweis der Existenz.  
Wenn Sie am Beweis nicht interessiert sind, können Sie diesen Abschnitt überspringen und direkt zu [Lineare Abhängigkeit und Unabhängigkeit von Lösungen](#lineare-abhängigkeit-und-unabhängigkeit-von-lösungen) übergehen.

### Beweis der Eindeutigkeit
Angenommen, das durch die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) und die Anfangsbedingungen ($\ref{eqn:initial_conditions}$) definierte Anfangswertproblem besitzt zwei Lösungen $y_1(x)$ und $y_2(x)$ auf dem Intervall $I$. Wenn wir zeigen können, dass die Differenz

$$ y(x) = y_1(x) - y_2(x) $$

auf dem Intervall $I$ identisch gleich $0$ ist, dann bedeutet dies, dass $y_1 \equiv y_2$ auf $I$ gilt, was die Eindeutigkeit der Lösung beweist.

Da die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) homogen und linear ist, ist die Linearkombination $y$ von $y_1$ und $y_2$ ebenfalls eine Lösung auf $I$. Da $y_1$ und $y_2$ dieselben Anfangsbedingungen ($\ref{eqn:initial_conditions}$) erfüllen, erfüllt $y$ die Bedingungen

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_1(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Betrachten wir nun die Funktion

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

und ihre Ableitung

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

Aus der Differentialgleichung erhalten wir

$$ y^{\prime\prime} = -py^{\prime} - qy $$

und wenn wir dies in die Gleichung für $z^{\prime}$ einsetzen, erhalten wir

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Da $y$ und $y^{\prime}$ reell sind, gilt

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

Aus dieser Ungleichung und der Definition von $z$ erhalten wir die beiden Ungleichungen

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

Aus diesen beiden Ungleichungen folgt, dass $\|2yy^{\prime}\|\leq z$ gilt, und somit gilt für den letzten Term in Gleichung ($\ref{eqn:z_prime}$) die folgende Ungleichung:

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Mit diesem Ergebnis und der Tatsache, dass $-p \leq \|p\|$ gilt, sowie unter Anwendung von Ungleichung ($\ref{eqn:inequalities}$a) auf den Term $2yy^{\prime}$ in Gleichung ($\ref{eqn:z_prime}$), erhalten wir

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Da ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$ gilt, folgt daraus

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

Wenn wir die Funktion in der Klammer als $h = 1 + 2\|p\| + \|q\|$ definieren, erhalten wir

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

Auf ähnliche Weise erhalten wir aus den Gleichungen ($\ref{eqn:z_prime}$) und ($\ref{eqn:inequalities}$)

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Diese beiden Ungleichungen ($\ref{eqn:inequality_6a}$) und ($\ref{eqn:inequality_6b}$) sind äquivalent zu den folgenden Ungleichungen

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

Die [Integrationsfaktoren](/posts/Solution-of-First-Order-Linear-ODE/#inhomogene-lineare-differentialgleichung) für die linken Seiten dieser beiden Ungleichungen sind

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{und} \qquad F_2 = e^{\int h(x)\ dx} $$

Da $h$ stetig ist, existiert das unbestimmte Integral $\int h(x)\ dx$, und da $F_1$ und $F_2$ positiv sind, folgt aus den Ungleichungen ($\ref{eqn:inequalities_7}$)

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Dies bedeutet, dass $F_1 z$ auf dem Intervall $I$ nicht zunimmt und $F_2 z$ nicht abnimmt. Da nach Gleichung ($\ref{eqn:initial_conditions_*}$) $z(x_0) = 0$ gilt, haben wir

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Wenn wir schließlich beide Seiten der Ungleichungen durch die positiven Werte $F_1$ und $F_2$ dividieren, können wir die Eindeutigkeit der Lösung wie folgt zeigen:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Lineare Abhängigkeit und Unabhängigkeit von Lösungen
Erinnern wir uns kurz an die Inhalte aus dem Beitrag über [homogene lineare Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/#basis-und-allgemeine-lösung). Die allgemeine Lösung auf einem offenen Intervall $I$ wird aus einer **Basis** $y_1$, $y_2$ auf $I$ gebildet, also aus einem Paar linear unabhängiger Lösungen. Dabei bedeutet **linear unabhängig**, dass für alle $x$ im Intervall $I$ gilt:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ und }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Wenn diese Bedingung nicht erfüllt ist und es mindestens ein Paar von Werten $k_1$, $k_2$ gibt, die nicht beide $0$ sind, für die $k_1y_1(x) + k_2y_2(x) = 0$ gilt, dann sind $y_1$ und $y_2$ auf dem Intervall $I$ **linear abhängig**. In diesem Fall gilt für alle $x$ im Intervall $I$

$$ \text{(a) } y_1 = ky_2 \quad \text{oder} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

d.h., $y_1$ und $y_2$ sind proportional zueinander.

Betrachten wir nun die folgende Methode zur Bestimmung der linearen Abhängigkeit bzw. Unabhängigkeit von Lösungen:

> **Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels Wronskian**  
> **i.** Wenn die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf einem offenen Intervall $I$ stetige Koeffizienten $p(x)$ und $q(x)$ besitzt, dann ist eine notwendige und hinreichende Bedingung dafür, dass zwei Lösungen $y_1$ und $y_2$ der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ linear abhängig sind, dass die *Wronski-Determinante*, kurz **Wronskian** genannt,
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> an irgendeinem Punkt $x_0$ im Intervall $I$ den Wert $0$ annimmt.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ und } y_2 \text{ sind linear abhängig} $$
>
> **ii.** Wenn der Wronskian an einem Punkt $x=x_0$ im Intervall $I$ den Wert $0$ annimmt, dann ist er für alle $x$ im Intervall $I$ gleich $0$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> Mit anderen Worten: Wenn es einen Punkt $x_1$ im Intervall $I$ gibt, an dem $W\neq 0$ gilt, dann sind $y_1$ und $y_2$ auf diesem Intervall $I$ linear unabhängig.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ und } y_2 \text{ sind linear unabhängig}
> \end{align*}$$
>
{: .prompt-info }

> Der Wronskian wurde vom polnischen Mathematiker Józef Maria Hoene-Wroński eingeführt und erhielt seinen heutigen Namen im Jahr 11882 HE durch den schottischen Mathematiker Sir Thomas Muir, nach Wrońskis Tod.
{: .prompt-tip }

### Beweis
#### i. (a)
Angenommen, $y_1$ und $y_2$ sind auf dem Intervall $I$ linear abhängig. Dann gilt auf dem Intervall $I$ entweder Gleichung ($\ref{eqn:linearly_dependent}$a) oder ($\ref{eqn:linearly_dependent}$b). Wenn Gleichung ($\ref{eqn:linearly_dependent}$a) gilt, dann haben wir

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

und ebenso, wenn Gleichung ($\ref{eqn:linearly_dependent}$b) gilt, dann haben wir

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Somit ist der Wronskian $W(y_1, y_2)=0$ <u>für alle $x$ im Intervall $I$</u>.

#### i. (b)
Umgekehrt werden wir zeigen, dass wenn $W(y_1, y_2)=0$ an einem Punkt $x = x_0$ gilt, dann sind $y_1$ und $y_2$ auf dem Intervall $I$ linear abhängig. Betrachten wir das lineare Gleichungssystem für die Unbekannten $k_1$ und $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Dies kann als folgende Vektorgleichung dargestellt werden:

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

Die Koeffizientenmatrix dieser Vektorgleichung ist

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

und die Determinante dieser Matrix ist gerade $W(y_1(x_0), y_2(x_0))$. Da $\det(A) = W=0$ ist, ist $A$ eine **singuläre Matrix** ohne **Inverse**, und daher besitzt das Gleichungssystem ($\ref{eqn:linear_system}$) eine nichttriviale Lösung $(c_1, c_2)$, bei der mindestens einer der Werte $c_1$ und $c_2$ nicht $0$ ist. Betrachten wir nun die Funktion

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Da die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) homogen und linear ist, ist diese Funktion nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) eine Lösung der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$. Aus Gleichung ($\ref{eqn:linear_system}$) folgt, dass diese Lösung die Anfangsbedingungen $y(x_0)=0$ und $y^{\prime}(x_0)=0$ erfüllt.

Andererseits existiert die triviale Lösung $y^* \equiv 0$, die dieselben Anfangsbedingungen $y^*(x_0)=0$ und ${y^*}^{\prime}(x_0)=0$ erfüllt. Da die Koeffizienten $p$ und $q$ der Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) stetig sind, garantiert der [Existenz- und Eindeutigkeitssatz für Anfangswertprobleme](#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) die Eindeutigkeit der Lösung, und daher gilt $y \equiv y^*$. Das bedeutet, dass auf dem Intervall $I$

$$ c_1y_1 + c_2y_2 \equiv 0 $$

gilt. Da mindestens einer der Werte $c_1$ und $c_2$ nicht $0$ ist, ist die Bedingung ($\ref{eqn:linearly_independent}$) nicht erfüllt, was bedeutet, dass $y_1$ und $y_2$ auf dem Intervall $I$ linear abhängig sind.

#### ii.
Wenn der Wronskian an einem Punkt $x_0$ im Intervall $I$ den Wert $0$ annimmt, dann sind nach [i.(b)](#i-b) $y_1$ und $y_2$ auf dem Intervall $I$ linear abhängig, und nach [i.(a)](#i-a) gilt dann $W\equiv 0$. Daher gilt: Wenn es einen Punkt $x_1$ im Intervall $I$ gibt, an dem $W(x_1)\neq 0$ gilt, dann sind $y_1$ und $y_2$ linear unabhängig. $\blacksquare$

## Die allgemeine Lösung umfasst alle Lösungen
### Existenz der allgemeinen Lösung
> Wenn $p(x)$ und $q(x)$ auf einem offenen Intervall $I$ stetig sind, dann besitzt die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ eine allgemeine Lösung.
{: .prompt-info }

#### Beweis
Nach dem [Existenz- und Eindeutigkeitssatz für Anfangswertprobleme](#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) besitzt die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ eine Lösung $y_1(x)$, die die Anfangsbedingungen

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

erfüllt, und eine Lösung $y_2(x)$, die die Anfangsbedingungen

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

erfüllt. Der Wronskian dieser beiden Lösungen hat am Punkt $x=x_0$ den von Null verschiedenen Wert

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Daher sind nach der [Methode zur Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels Wronskian](#lineare-abhängigkeit-und-unabhängigkeit-von-lösungen) $y_1$ und $y_2$ auf dem Intervall $I$ linear unabhängig. Somit bilden diese beiden Lösungen eine Basis für die Lösungen der Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$, und die allgemeine Lösung $y = c_1y_1 + c_2y_2$ mit beliebigen Konstanten $c_1$ und $c_2$ existiert auf dem Intervall $I$. $\blacksquare$

### Nichtexistenz singulärer Lösungen
> Wenn die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf einem offenen Intervall $I$ stetige Koeffizienten $p(x)$ und $q(x)$ besitzt, dann lässt sich jede Lösung $y=Y(x)$ der Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ in der Form
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> darstellen, wobei $y_1$ und $y_2$ eine Basis für die Lösungen der Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ bilden und $C_1$ und $C_2$ geeignete Konstanten sind.  
> Das bedeutet, dass die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) keine **singulären Lösungen** besitzt, also keine Lösungen, die nicht aus der allgemeinen Lösung abgeleitet werden können.
{: .prompt-info }

#### Beweis
Sei $y=Y(x)$ eine beliebige Lösung der Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$. Nach dem [Existenzsatz für die allgemeine Lösung](#existenz-der-allgemeinen-lösung) besitzt die Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ die allgemeine Lösung

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Wir müssen nun zeigen, dass für jede Funktion $Y(x)$ Konstanten $c_1$ und $c_2$ existieren, so dass $y(x)=Y(x)$ auf dem Intervall $I$ gilt. Zunächst zeigen wir, dass wir für einen beliebigen Punkt $x_0$ im Intervall $I$ Werte für $c_1$ und $c_2$ finden können, so dass $y(x_0)=Y(x_0)$ und $y^{\prime}(x_0)=Y^{\prime}(x_0)$ gilt. Aus Gleichung ($\ref{eqn:general_solution}$) erhalten wir

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

Da $y_1$ und $y_2$ eine Basis bilden, ist die Determinante der Koeffizientenmatrix, also $W(y_1(x_0), y_2(x_0))$, von Null verschieden, und daher kann die Gleichung ($\ref{eqn:vector_equation_2}$) nach $c_1$ und $c_2$ aufgelöst werden. Sei $(c_1, c_2) = (C_1, C_2)$ die Lösung. Wenn wir diese Werte in Gleichung ($\ref{eqn:general_solution}$) einsetzen, erhalten wir die spezielle Lösung

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Da $C_1$ und $C_2$ die Gleichung ($\ref{eqn:vector_equation_2}$) erfüllen, gilt

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Nach der Eindeutigkeit des [Existenz- und Eindeutigkeitssatzes für Anfangswertprobleme](#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) gilt $y^* \equiv Y$ auf dem gesamten Intervall $I$. $\blacksquare$
