---
title: Homogene lineare Differentialgleichungen zweiter Ordnung
description: Wir untersuchen die Definition und Eigenschaften linearer Differentialgleichungen zweiter Ordnung und verstehen insbesondere das wichtige Theorem des Superpositionsprinzips und das daraus resultierende Konzept der Basis für homogene lineare Differentialgleichungen.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Standardform** einer linearen Differentialgleichung zweiter Ordnung: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Koeffizienten**: Funktionen $p$, $q$
>   - **Eingabe**: $r(x)$
>   - **Ausgabe** oder **Antwort**: $y(x)$
> - Homogen und inhomogen
>   - **Homogen**: Wenn in der Standardform $r(x)\equiv0$
>   - **Inhomogen**: Wenn in der Standardform $r(x)\not\equiv 0$
> - **Superpositionsprinzip**: Für eine <u>homogene</u> lineare Differentialgleichung $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ ist jede Linearkombination zweier beliebiger Lösungen auf einem offenen Intervall $I$ ebenfalls eine Lösung der gegebenen Gleichung. Das heißt, die Summe und das Vielfache beliebiger Lösungen der gegebenen homogenen linearen Differentialgleichung sind ebenfalls Lösungen dieser Gleichung.
> - **Basis** oder **Fundamentalsystem**: Ein Paar $(y_1, y_2)$ linear unabhängiger Lösungen der homogenen linearen Differentialgleichung auf dem Intervall $I$
> - **Ordnungsreduktion**: Wenn eine Lösung einer homogenen linearen Differentialgleichung zweiter Ordnung gefunden werden kann, kann eine zweite, linear unabhängige Lösung, also eine Basis, durch Lösen einer Differentialgleichung erster Ordnung gefunden werden. Diese Methode wird als Ordnungsreduktion bezeichnet.
> - Anwendung der Ordnungsreduktion: Eine allgemeine Differentialgleichung zweiter Ordnung $F(x, y, y^\prime, y^{\prime\prime})=0$, ob linear oder nichtlinear, kann in folgenden Fällen mittels Ordnungsreduktion auf eine Gleichung erster Ordnung reduziert werden:
>   - Wenn $y$ nicht explizit auftritt
>   - Wenn $x$ nicht explizit auftritt
>   - Wenn sie homogen linear ist und eine Lösung bereits bekannt ist
{: .prompt-info }

## Voraussetzungen
- [Grundkonzepte der Modellierung](/posts/Basic-Concepts-of-Modeling/)
- [Trennung der Variablen](/posts/Separation-of-Variables/)
- [Lösung linearer Differentialgleichungen erster Ordnung](/posts/Solution-of-First-Order-Linear-ODE/)

## Lineare Differentialgleichungen zweiter Ordnung
Eine Differentialgleichung zweiter Ordnung wird als **linear** bezeichnet, wenn sie in der Form

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

geschrieben werden kann, andernfalls wird sie als **nichtlinear** bezeichnet.

Wenn $p$, $q$ und $r$ Funktionen von $x$ sind, ist diese Gleichung linear in $y$ und seinen Ableitungen.

Die Form in Gleichung ($\ref{eqn:standard_form}$) wird als **Standardform** einer linearen Differentialgleichung zweiter Ordnung bezeichnet. Wenn der erste Term einer gegebenen linearen Differentialgleichung zweiter Ordnung $f(x)y^{\prime\prime}$ ist, kann die Standardform durch Division beider Seiten der Gleichung durch $f(x)$ erhalten werden.

Die Funktionen $p$ und $q$ werden als **Koeffizienten**, $r(x)$ als **Eingabe** und $y(x)$ als **Ausgabe** oder **Antwort** auf die Eingabe und die Anfangsbedingungen bezeichnet.

### Homogene lineare Differentialgleichungen zweiter Ordnung
Sei $J$ das Intervall $a<x<b$, in dem wir Gleichung ($\ref{eqn:standard_form}$) lösen wollen. Wenn in Gleichung ($\ref{eqn:standard_form}$) $r(x)\equiv 0$ für das Intervall $J$ gilt, haben wir

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

und dies wird als **homogen** bezeichnet.

## Inhomogene lineare Differentialgleichungen
Wenn $r(x)\not\equiv 0$ im Intervall $J$, wird die Gleichung als **inhomogen** bezeichnet.

## Superpositionsprinzip

Eine Funktion der Form

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ sind beliebige Konstanten)}\tag{3}$$

wird als **Linearkombination** von $y_1$ und $y_2$ bezeichnet.

Dabei gilt Folgendes:

> **Superpositionsprinzip**  
> Für die homogene lineare Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) ist jede Linearkombination zweier beliebiger Lösungen auf einem offenen Intervall $I$ ebenfalls eine Lösung von Gleichung ($\ref{eqn:homogeneous_linear_ode}$). Das heißt, die Summe und das Vielfache beliebiger Lösungen der gegebenen homogenen linearen Differentialgleichung sind ebenfalls Lösungen dieser Gleichung.
{: .prompt-info }

### Beweis
Seien $y_1$ und $y_2$ Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$. Wenn wir $y=c_1y_1+c_2y_2$ in Gleichung ($\ref{eqn:homogeneous_linear_ode}$) einsetzen, erhalten wir

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

was eine Identität ist. Daher ist $y$ eine Lösung der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$. $\blacksquare$

> Es ist zu beachten, dass das Superpositionsprinzip nur für homogene lineare Differentialgleichungen gilt und nicht für inhomogene lineare oder nichtlineare Differentialgleichungen.
{: .prompt-warning }

## Basis und allgemeine Lösung
### Wiederholung wichtiger Konzepte aus Differentialgleichungen erster Ordnung
Wie wir zuvor in [Grundkonzepte der Modellierung](/posts/Basic-Concepts-of-Modeling/) gesehen haben, besteht ein Anfangswertproblem (Initial Value Problem) für eine Differentialgleichung erster Ordnung aus der Differentialgleichung und einer Anfangsbedingung (initial condition) $y(x_0)=y_0$. Die Anfangsbedingung wird benötigt, um die willkürliche Konstante $c$ in der allgemeinen Lösung der gegebenen Differentialgleichung zu bestimmen, und die so bestimmte Lösung wird als spezielle Lösung bezeichnet. Lassen Sie uns nun diese Konzepte auf Differentialgleichungen zweiter Ordnung erweitern.

### Anfangswertproblem und Anfangsbedingungen
Ein **Anfangswertproblem** für die homogene lineare Differentialgleichung zweiter Ordnung ($\ref{eqn:homogeneous_linear_ode}$) besteht aus der gegebenen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) und zwei **Anfangsbedingungen**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Diese Bedingungen werden benötigt, um die zwei willkürlichen Konstanten $c_1$ und $c_2$ in der **allgemeinen Lösung** der Differentialgleichung zu bestimmen

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Lineare Unabhängigkeit und lineare Abhängigkeit
Lassen Sie uns kurz das Konzept der linearen Unabhängigkeit und Abhängigkeit betrachten. Dies ist notwendig, um später die Basis zu definieren.  
Zwei Funktionen $y_1$ und $y_2$ sind **linear unabhängig** auf einem Intervall $I$, wenn für alle Punkte in $I$ gilt:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ und }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

Andernfalls sind $y_1$ und $y_2$ **linear abhängig**.

Wenn $y_1$ und $y_2$ linear abhängig sind (d.h. wenn die Aussage ($\ref{eqn:linearly_independent}$) nicht wahr ist), können wir durch Division beider Seiten der Gleichung in ($\ref{eqn:linearly_independent}$) durch $k_1 \neq 0$ oder $k_2 \neq 0$ schreiben:

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{oder} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

was zeigt, dass $y_1$ und $y_2$ proportional zueinander sind.

### Basis, allgemeine Lösung, spezielle Lösung
Um zur allgemeinen Lösung ($\ref{eqn:general_sol}$) zurückzukehren: Damit dies eine allgemeine Lösung ist, müssen $y_1$ und $y_2$ Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) sein und gleichzeitig auf dem Intervall $I$ nicht proportional zueinander und linear unabhängig sein. Ein Paar $(y_1, y_2)$ von Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode}$), das diese Bedingungen erfüllt und auf dem Intervall $I$ linear unabhängig ist, wird als **Basis** oder **Fundamentalsystem** der Lösungen von Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$ bezeichnet.

Durch Verwendung der Anfangsbedingungen zur Bestimmung der beiden Konstanten $c_1$ und $c_2$ in der allgemeinen Lösung ($\ref{eqn:general_sol}$) erhalten wir eine eindeutige Lösung, die durch den Punkt $(x_0, K_0)$ geht und an diesem Punkt eine Tangentensteigung von $K_1$ hat. Dies wird als **spezielle Lösung** der Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) bezeichnet.

Wenn Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf einem offenen Intervall $I$ stetig ist, hat sie immer eine allgemeine Lösung, und diese allgemeine Lösung umfasst alle möglichen speziellen Lösungen. Das bedeutet, in diesem Fall hat Gleichung ($\ref{eqn:homogeneous_linear_ode}$) keine singuläre Lösung, die nicht aus der allgemeinen Lösung abgeleitet werden kann.

## Ordnungsreduktion
Wenn für eine homogene lineare Differentialgleichung zweiter Ordnung eine Lösung gefunden werden kann, kann eine zweite, linear unabhängige Lösung, also eine Basis, durch Lösen einer Differentialgleichung erster Ordnung wie folgt gefunden werden. Diese Methode wird als **Ordnungsreduktion** bezeichnet.

Betrachten wir die homogene lineare Differentialgleichung zweiter Ordnung in Standardform (d.h. <u>mit $y^{\prime\prime}$ statt $f(x)y^{\prime\prime}$</u>)

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

und nehmen wir an, dass wir eine Lösung $y_1$ dieser Gleichung auf einem offenen Intervall $I$ kennen.

Wir setzen nun die zweite gesuchte Lösung als $y_2 = uy_1$ an und erhalten:

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Wenn wir dies in die Gleichung einsetzen, erhalten wir:

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Wenn wir die Terme mit $u^{\prime\prime}$, $u^{\prime}$ und $u$ gruppieren und umordnen, erhalten wir:

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Da $y_1$ eine Lösung der gegebenen Gleichung ist, verschwindet der Ausdruck in der letzten Klammer, und wir erhalten eine Differentialgleichung für $u^{\prime}$ und $u^{\prime\prime}$. Wenn wir beide Seiten dieser verbleibenden Differentialgleichung durch $y_1$ teilen und $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$ setzen, erhalten wir die folgende Differentialgleichung erster Ordnung:

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Durch [Trennung der Variablen](/posts/Separation-of-Variables/) und Integration erhalten wir:

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

Durch Anwendung der Exponentialfunktion auf beide Seiten erhalten wir schließlich:

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Da wir zuvor $U=u^{\prime}$ gesetzt haben, gilt $u=\int U dx$, und die gesuchte zweite Lösung $y_2$ ist:

$$ y_2 = uy_1 = y_1 \int U dx $$

Da $\cfrac{y_2}{y_1} = u = \int U dx$ keine Konstante sein kann, solange $U>0$ ist, bilden $y_1$ und $y_2$ eine Basis der Lösungen.

### Anwendung der Ordnungsreduktion
Eine allgemeine Differentialgleichung zweiter Ordnung $F(x, y, y^\prime, y^{\prime\prime})=0$, ob linear oder nichtlinear, kann mittels Ordnungsreduktion auf eine Gleichung erster Ordnung reduziert werden, wenn $y$ nicht explizit auftritt, wenn $x$ nicht explizit auftritt, oder wenn sie homogen linear ist und eine Lösung bereits bekannt ist, wie wir zuvor gesehen haben.

#### Wenn $y$ nicht explizit auftritt
In $F(x, y^\prime, y^{\prime\prime})=0$ können wir $z=y^{\prime}$ setzen und erhalten eine Differentialgleichung erster Ordnung $F(x, z, z^{\prime})$ für $z$.

#### Wenn $x$ nicht explizit auftritt
In $F(y, y^\prime, y^{\prime\prime})=0$ können wir $z=y^{\prime}$ setzen. Da $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$, erhalten wir eine Differentialgleichung erster Ordnung $F(y,z,z^\prime)$ für $z$, wobei $y$ die Rolle der unabhängigen Variable $x$ übernimmt.
