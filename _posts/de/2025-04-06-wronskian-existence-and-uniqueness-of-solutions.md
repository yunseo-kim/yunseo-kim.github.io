---
title: "Wronski-Determinante, Existenz und Eindeutigkeit von Lösungen"
description: "Für eine homogene lineare DGL zweiter Ordnung mit stetigen, variablen Koeffizienten untersuchen wir den Existenz- und Eindeutigkeitssatz für Anfangswertprobleme und die Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels der Wronski-Determinante. Wir zeigen auch, dass solche Gleichungen immer eine allgemeine Lösung besitzen, die alle möglichen Lösungen umfasst."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Für eine homogene lineare gewöhnliche Differentialgleichung zweiter Ordnung mit stetigen, variablen Koeffizienten $p$ und $q$ auf einem Intervall $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> und den Anfangsbedingungen
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> gelten die folgenden vier Sätze.
> 1. **Existenz- und Eindeutigkeitssatz für Anfangswertprobleme**: Das durch die gegebene Gleichung und die Anfangsbedingungen definierte Anfangswertproblem hat eine eindeutige Lösung $y(x)$ auf dem Intervall $I$.
> 2. **Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels der Wronski-Determinante**: Für zwei Lösungen $y_1$ und $y_2$ der Gleichung sind diese linear abhängig, wenn es ein $x_0$ im Intervall $I$ gibt, für das die **Wronski-Determinante** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ gleich $0$ ist. Wenn es ein $x_1$ im Intervall $I$ gibt, für das $W\neq 0$ ist, sind die beiden Lösungen linear unabhängig.
> 3. **Existenz einer allgemeinen Lösung**: Die gegebene Gleichung besitzt eine allgemeine Lösung auf dem Intervall $I$.
> 4. **Nichtexistenz singulärer Lösungen**: Diese allgemeine Lösung umfasst alle Lösungen der Gleichung (d.h., es gibt keine singulären Lösungen).
{: .prompt-info }

## Voraussetzungen
- [Lösung linearer DGL erster Ordnung](/posts/Solution-of-First-Order-Linear-ODE/)
- [Homogene lineare DGL zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Euler-Cauchy-Gleichung](/posts/euler-cauchy-equation/)
- Inverse Matrizen, singuläre Matrizen und Determinanten

## Homogene lineare GDGL mit stetigen variablen Koeffizienten
Zuvor haben wir die allgemeine Lösung für [homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/) und die [Euler-Cauchy-Gleichung](/posts/euler-cauchy-equation/) untersucht.
In diesem Beitrag erweitern wir die Diskussion auf einen allgemeineren Fall und untersuchen die Existenz und Form der allgemeinen Lösung einer homogenen linearen gewöhnlichen Differentialgleichung zweiter Ordnung mit beliebigen stetigen **variablen Koeffizienten** $p$ und $q$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Darüber hinaus werden wir die Eindeutigkeit des [Anfangswertproblems](/posts/homogeneous-linear-odes-of-second-order/#anfangswertproblem-und-anfangsbedingungen) untersuchen, das aus der gewöhnlichen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) und den folgenden beiden Anfangsbedingungen besteht:

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Um es vorwegzunehmen: Der Kern des hier behandelten Themas ist, dass eine <u>lineare</u> gewöhnliche Differentialgleichung mit stetigen Koeffizienten keine *singuläre Lösung* (eine Lösung, die nicht aus der allgemeinen Lösung abgeleitet werden kann) besitzt.

## Existenz- und Eindeutigkeitssatz für Anfangswertprobleme
> **Existenz- und Eindeutigkeitssatz für Anfangswertprobleme**  
> Wenn $p(x)$ und $q(x)$ stetige Funktionen auf einem offenen Intervall $I$ sind und $x_0$ in diesem Intervall $I$ liegt, dann hat das durch die Gleichungen ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) und ($\ref{eqn:initial_conditions}$) definierte Anfangswertproblem eine eindeutige Lösung $y(x)$ auf dem Intervall $I$.
{: .prompt-info }

Der Beweis der Existenz wird hier nicht behandelt; wir werden uns nur den Beweis der Eindeutigkeit ansehen. In der Regel ist der Beweis der Eindeutigkeit einfacher als der Beweis der Existenz.  
Wenn Sie nicht am Beweis interessiert sind, können Sie diesen Abschnitt überspringen und zu [Lineare Abhängigkeit und Unabhängigkeit von Lösungen](#lineare-abhängigkeit-und-unabhängigkeit-von-lösungen) übergehen.

### Beweis der Eindeutigkeit
Nehmen wir an, das Anfangswertproblem, bestehend aus der gewöhnlichen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) und den Anfangsbedingungen ($\ref{eqn:initial_conditions}$), hat zwei Lösungen $y_1(x)$ und $y_2(x)$ auf dem Intervall $I$. Wenn wir zeigen können, dass die Differenz dieser beiden Lösungen

$$ y(x) = y_1(x) - y_2(x) $$

auf dem Intervall $I$ identisch null ist, bedeutet dies, dass $y_1 \equiv y_2$ auf dem Intervall $I$ gilt, was die Eindeutigkeit der Lösung beweist.

Da die Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) eine homogene lineare gewöhnliche Differentialgleichung ist, ist die Linearkombination $y$ von $y_1$ und $y_2$ ebenfalls eine Lösung der Gleichung auf $I$. Da $y_1$ und $y_2$ die gleichen Anfangsbedingungen ($\ref{eqn:initial_conditions}$) erfüllen, erfüllt $y$ die Bedingungen

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Betrachten wir nun die Funktion

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

und ihre Ableitung

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

Aus der gewöhnlichen Differentialgleichung erhalten wir

$$ y^{\prime\prime} = -py^{\prime} - qy $$

und setzen dies in die Gleichung für $z^{\prime}$ ein, um

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

zu erhalten. Da $y$ und $y^{\prime}$ reell sind, gilt

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

Daraus und aus der Definition von $z$ erhalten wir zwei Ungleichungen

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

Aus diesen beiden Ungleichungen können wir schließen, dass $|2yy^{\prime}|\leq z$. Dann gilt für den letzten Term in Gleichung ($\ref{eqn:z_prime}$) die folgende Ungleichung:

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Unter Verwendung dieses Ergebnisses und der Tatsache, dass $-p \leq |p|$, und durch Anwendung von Gleichung ($\ref{eqn:inequalities}$a) auf den Term $2yy^{\prime}$ in Gleichung ($\ref{eqn:z_prime}$) erhalten wir

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Da ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$ ist, ergibt sich daraus

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

und wenn wir die Funktion in der Klammer als $h = 1 + 2|p| + |q|$ setzen, haben wir

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

Auf die gleiche Weise erhalten wir aus den Gleichungen ($\ref{eqn:z_prime}$) und ($\ref{eqn:inequalities}$)

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Diese beiden Ungleichungen ($\ref{eqn:inequality_6a}$), ($\ref{eqn:inequality_6b}$) sind äquivalent zu den folgenden Ungleichungen

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

und die [integrierenden Faktoren](/posts/Solution-of-First-Order-Linear-ODE/#inhomogene-lineare-gewöhnliche-differentialgleichungen) für die linken Seiten der beiden Gleichungen sind

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{und} \qquad F_2 = e^{\int h(x)\ dx} $$

Da $h$ stetig ist, existiert das unbestimmte Integral $\int h(x)\ dx$, und da $F_1$ und $F_2$ positiv sind, erhalten wir aus Gleichung ($\ref{eqn:inequalities_7}$)

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Dies bedeutet, dass $F_1 z$ auf dem Intervall $I$ nicht zunimmt und $F_2 z$ nicht abnimmt. Gemäß Gleichung ($\ref{eqn:initial_conditions_*}$) ist $z(x_0) = 0$, also

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Schließlich können wir die Eindeutigkeit der Lösung zeigen, indem wir beide Seiten der Ungleichungen durch die positiven Zahlen $F_1$ und $F_2$ teilen:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Lineare Abhängigkeit und Unabhängigkeit von Lösungen
Erinnern wir uns kurz an den Inhalt des Beitrags über [lineare homogene DGL zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/#basis-und-allgemeine-lösung). Die allgemeine Lösung auf einem offenen Intervall $I$ wird aus einer **Basis** $y_1$, $y_2$ auf $I$ gebildet, d.h. aus einem Paar linear unabhängiger Lösungen. Dass $y_1$ und $y_2$ auf dem Intervall $I$ **linear unabhängig** sind, bedeutet, dass für alle $x$ im Intervall Folgendes gilt:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ und }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Wenn dies nicht erfüllt ist und $k_1y_1(x) + k_2y_2(x) = 0$ für mindestens ein nicht-null $k_1$ oder $k_2$ gilt, sind $y_1$ und $y_2$ auf dem Intervall $I$ **linear abhängig**. In diesem Fall gilt für alle $x$ im Intervall $I$

$$ \text{(a) } y_1 = ky_2 \quad \text{oder} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

sodass $y_1$ und $y_2$ proportional sind.

Betrachten wir nun das folgende Kriterium zur Bestimmung der linearen Unabhängigkeit/Abhängigkeit von Lösungen.

> **Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels der Wronski-Determinante**  
> **i.** Wenn die gewöhnliche Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf einem offenen Intervall $I$ stetige Koeffizienten $p(x)$ und $q(x)$ hat, dann ist die notwendige und hinreichende Bedingung dafür, dass zwei Lösungen $y_1$ und $y_2$ der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ linear abhängig sind, dass ihre *Wronski-Determinante*, kurz **Wronski-Determinante** genannt,
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> an einem Punkt $x_0$ im Intervall $I$ null wird.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ und } y_2 \text{ sind linear abhängig} $$
>
> **ii.** Wenn $W=0$ an einem Punkt $x=x_0$ im Intervall $I$ ist, dann ist $W=0$ für alle $x$ im Intervall $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> Mit anderen Worten, wenn es ein $x_1$ im Intervall $I$ gibt, für das $W\neq 0$ ist, dann sind $y_1$ und $y_2$ in diesem Intervall $I$ linear unabhängig.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ und } y_2 \text{ sind linear unabhängig}
> \end{align*}$$
>
{: .prompt-info }

> Die Wronski-Determinante wurde erstmals vom polnischen Mathematiker Józef Maria Hoene-Wroński eingeführt und nach seinem Tod im Jahr 11882 HE vom schottischen Mathematiker Sir Thomas Muir benannt.
{: .prompt-tip }

### Beweis
#### i. (a)
Nehmen wir an, $y_1$ und $y_2$ sind auf dem Intervall $I$ linear abhängig. Dann gilt auf dem Intervall $I$ entweder Gleichung ($\ref{eqn:linearly_dependent}$a) oder ($\ref{eqn:linearly_dependent}$b). Wenn Gleichung ($\ref{eqn:linearly_dependent}$a) gilt, dann ist

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2y_2^{\prime} - y_2(ky_2^{\prime}) = 0 $$

und ebenso, wenn Gleichung ($\ref{eqn:linearly_dependent}$b) gilt,

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1(ly_1^{\prime}) - ly_1y_1^{\prime} = 0 $$

Daher können wir bestätigen, dass die Wronski-Determinante $W(y_1, y_2)=0$ <u>für alle $x$ im Intervall $I$</u> ist.

#### i. (b)
Umgekehrt wollen wir zeigen, dass, wenn $W(y_1, y_2)=0$ für ein $x = x_0$ gilt, $y_1$ und $y_2$ auf dem Intervall $I$ linear abhängig sind. Betrachten wir das lineare Gleichungssystem für die Unbekannten $k_1$, $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Dies kann in Vektorform wie folgt ausgedrückt werden:

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

und die Determinante dieser Matrix ist $W(y_1(x_0), y_2(x_0))$. Da $\det(A) = W=0$ ist, ist $A$ eine **singuläre Matrix**, die keine **inverse Matrix** besitzt. Daher hat das Gleichungssystem ($\ref{eqn:linear_system}$) eine nichttriviale Lösung $(c_1, c_2)$, bei der mindestens einer der Werte $k_1$ und $k_2$ nicht null ist. Führen wir nun die Funktion

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

ein. Da die Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) linear und homogen ist, ist diese Funktion nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) eine Lösung von ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$. Aus Gleichung ($\ref{eqn:linear_system}$) wissen wir, dass diese Lösung die Anfangsbedingungen $y(x_0)=0$, $y^{\prime}(x_0)=0$ erfüllt.

Andererseits existiert die triviale Lösung $y^\* \equiv 0$, die die gleichen Anfangsbedingungen $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$ erfüllt. Da die Koeffizienten $p$ und $q$ der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) stetig sind, ist die Eindeutigkeit der Lösung durch den [Existenz- und Eindeutigkeitssatz für Anfangswertprobleme](#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) gewährleistet, und daher ist $y \equiv y^\*$. Das heißt, auf dem Intervall $I$ gilt

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Da mindestens einer der Werte $c_1$ und $c_2$ nicht null ist, ist ($\ref{eqn:linearly_independent}$) nicht erfüllt, was bedeutet, dass $y_1$ und $y_2$ auf dem Intervall $I$ linear abhängig sind.

#### ii.
Wenn an einem Punkt $x_0$ im Intervall $I$ $W(x_0)=0$ ist, dann sind $y_1$ und $y_2$ nach [i.(b)](#i-b) auf dem Intervall $I$ linear abhängig, und dann ist nach [i.(a)](#i-a) $W\equiv 0$. Daher, wenn es auch nur einen Punkt $x_1$ im Intervall $I$ gibt, an dem $W(x_1)\neq 0$ ist, sind $y_1$ und $y_2$ linear unabhängig. $\blacksquare$

## Die allgemeine Lösung umfasst alle Lösungen
### Existenz einer allgemeinen Lösung
> Wenn $p(x)$ und $q(x)$ auf einem offenen Intervall $I$ stetig sind, dann besitzt die Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) eine allgemeine Lösung auf dem Intervall $I$.
{: .prompt-info }

#### Beweis
Nach dem [Existenz- und Eindeutigkeitssatz für Anfangswertprobleme](#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) hat die gewöhnliche Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) eine Lösung $y_1(x)$, die die Anfangsbedingungen

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

auf dem Intervall $I$ erfüllt, und eine Lösung $y_2(x)$, die die Anfangsbedingungen

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

auf dem Intervall $I$ erfüllt. Die Wronski-Determinante dieser beiden Lösungen hat bei $x=x_0$ einen Wert ungleich null:

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Daher sind $y_1$ und $y_2$ nach dem Kriterium der [Bestimmung der linearen Abhängigkeit/Unabhängigkeit von Lösungen mittels der Wronski-Determinante](#lineare-abhängigkeit-und-unabhängigkeit-von-lösungen) auf dem Intervall $I$ linear unabhängig. Folglich bilden diese beiden Lösungen eine Basis für die Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$, und es existiert notwendigerweise eine allgemeine Lösung $y = c_1y_1 + c_2y_2$ mit beliebigen Konstanten $c_1$, $c_2$ auf dem Intervall $I$. $\blacksquare$

### Nichtexistenz singulärer Lösungen
> Wenn die gewöhnliche Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf einem offenen Intervall $I$ stetige Koeffizienten $p(x)$ und $q(x)$ hat, dann hat jede Lösung $y=Y(x)$ der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ die Form
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> wobei $y_1$, $y_2$ eine Basis von Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$ ist und $C_1$, $C_2$ geeignete Konstanten sind.  
> Das heißt, die Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) hat keine **singuläre Lösung**, die nicht aus der allgemeinen Lösung abgeleitet werden kann.
{: .prompt-info }

#### Beweis
Sei $y=Y(x)$ eine beliebige Lösung der Gleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) auf dem Intervall $I$. Nach dem [Satz über die Existenz einer allgemeinen Lösung](#existenz-einer-allgemeinen-lösung) hat die gewöhnliche Differentialgleichung ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) eine allgemeine Lösung auf dem Intervall $I$:

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Wir müssen nun zeigen, dass für jedes beliebige $Y(x)$ Konstanten $c_1$, $c_2$ existieren, sodass $y(x)=Y(x)$ auf dem Intervall $I$ gilt. Zeigen wir zunächst, dass wir Werte für $c_1$, $c_2$ finden können, sodass für ein beliebiges $x_0$ im Intervall $I$ gilt: $y(x_0)=Y(x_0)$ und $y^{\prime}(x_0)=Y^{\prime}(x_0)$. Aus Gleichung ($\ref{eqn:general_solution}$) erhalten wir

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

Da $y_1$ und $y_2$ eine Basis bilden, ist die Determinante der Koeffizientenmatrix, $W(y_1(x_0), y_2(x_0))$, ungleich null. Daher kann die Gleichung ($\ref{eqn:vector_equation_2}$) nach $c_1$ und $c_2$ aufgelöst werden. Nennen wir die Lösung $(c_1, c_2) = (C_1, C_2)$. Wenn wir dies in Gleichung ($\ref{eqn:general_solution}$) einsetzen, erhalten wir die folgende partikuläre Lösung:

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Da $C_1$, $C_2$ die Lösung von Gleichung ($\ref{eqn:vector_equation_2}$) sind, gilt

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Aufgrund der Eindeutigkeit aus dem [Existenz- und Eindeutigkeitssatz für Anfangswertprobleme](#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) gilt $y^\* \equiv Y$ für alle $x$ im Intervall $I$. $\blacksquare$
