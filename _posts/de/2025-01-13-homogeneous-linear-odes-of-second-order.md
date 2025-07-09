---
title: "Homogene lineare DGL zweiter Ordnung"
description: "Einführung in die Definition und Eigenschaften linearer Differentialgleichungen zweiter Ordnung. Verstehen des Superpositionsprinzips für homogene Gleichungen und des Konzepts einer Basis."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Standardform** einer linearen DGL 2. Ordnung: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Koeffizienten**: Funktionen $p$, $q$
>   - **Eingabe (Input)**: $r(x)$
>   - **Ausgabe (Output)** oder **Antwort (Response)**: $y(x)$
> - Homogen und Inhomogen
>   - **Homogen**: Wenn in der Standardform $r(x)\equiv0$ gilt.
>   - **Inhomogen**: Wenn in der Standardform $r(x)\not\equiv 0$ gilt.
> - **Superpositionsprinzip**: Für eine <u>homogene</u> lineare DGL $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ ist jede Linearkombination von zwei beliebigen Lösungen auf einem offenen Intervall $I$ ebenfalls eine Lösung der gegebenen Gleichung. Das heißt, die Summe und das skalare Vielfache von beliebigen Lösungen der gegebenen homogenen linearen DGL sind ebenfalls Lösungen dieser Gleichung.
> - **Basis** oder **Fundamentalsystem**: Ein Paar $(y_1, y_2)$ von linear unabhängigen Lösungen einer homogenen linearen DGL auf einem Intervall $I$.
> - **Reduktionsverfahren (reduction of order)**: Wenn eine Lösung einer homogenen DGL 2. Ordnung bekannt ist, kann eine zweite, linear unabhängige Lösung (also eine Basis) durch Lösen einer DGL 1. Ordnung gefunden werden. Dieses Verfahren wird als Reduktionsverfahren bezeichnet.
> - Anwendung des Reduktionsverfahrens: Eine allgemeine DGL 2. Ordnung $F(x, y, y^\prime, y^{\prime\prime})=0$, ob linear oder nichtlinear, kann in den folgenden Fällen mittels Reduktionsverfahren auf eine DGL 1. Ordnung reduziert werden:
>   - Wenn $y$ nicht explizit vorkommt.
>   - Wenn $x$ nicht explizit vorkommt.
>   - Wenn die Gleichung linear homogen ist und eine Lösung bereits bekannt ist.
{: .prompt-info }

## Voraussetzungen
- [Grundkonzepte der Modellierung](/posts/Basic-Concepts-of-Modeling/)
- [Trennung der Variablen](/posts/Separation-of-Variables/)
- [Lösung linearer DGL erster Ordnung](/posts/Solution-of-First-Order-Linear-ODE/)

## Lineare Differentialgleichungen zweiter Ordnung
Eine Differentialgleichung zweiter Ordnung heißt **linear**, wenn sie in der Form

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

geschrieben werden kann, andernfalls heißt sie **nichtlinear**.

Wenn $p$, $q$ und $r$ Funktionen von $x$ sind, ist diese Gleichung linear in $y$ und seinen Ableitungen.

Die Form der Gleichung ($\ref{eqn:standard_form}$) wird als **Standardform** einer linearen DGL zweiter Ordnung bezeichnet. Falls der erste Term einer gegebenen linearen DGL zweiter Ordnung $f(x)y^{\prime\prime}$ ist, kann man die Standardform erhalten, indem man beide Seiten der Gleichung durch $f(x)$ teilt.

Die Funktionen $p$ und $q$ werden als **Koeffizienten**, $r(x)$ als **Eingabe (Input)** und $y(x)$ als **Ausgabe (Output)** oder **Antwort (Response)** auf die Eingabe und die Anfangsbedingungen bezeichnet.

### Homogene lineare DGL zweiter Ordnung
Sei $J$ ein Intervall $a<x<b$, auf dem wir die Gleichung ($\ref{eqn:standard_form}$) lösen wollen. Wenn für das Intervall $J$ gilt, dass $r(x)\equiv 0$ ist, dann haben wir

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

und diese Gleichung wird als **homogen** bezeichnet.

## Inhomogene lineare Differentialgleichungen
Wenn auf dem Intervall $J$ gilt, dass $r(x)\not\equiv 0$, wird die Gleichung als **inhomogen** bezeichnet.

## Superpositionsprinzip

Eine Funktion der Form

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ sind beliebige Konstanten)}\tag{3}$$

wird als **Linearkombination** von $y_1$ und $y_2$ bezeichnet.

Dabei gilt Folgendes:

> **Superpositionsprinzip**  
> Für die homogene lineare Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) ist jede Linearkombination von zwei beliebigen Lösungen auf einem offenen Intervall $I$ ebenfalls eine Lösung der Gleichung ($\ref{eqn:homogeneous_linear_ode}$). Das heißt, die Summe und das skalare Vielfache von beliebigen Lösungen der gegebenen homogenen linearen DGL sind ebenfalls Lösungen dieser Gleichung.
{: .prompt-info }

### Beweis
Seien $y_1$ und $y_2$ Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$. Setzen wir $y=c_1y_1+c_2y_2$ in die Gleichung ($\ref{eqn:homogeneous_linear_ode}$) ein, erhalten wir

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

was eine Identität ergibt. Daher ist $y$ eine Lösung der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$. $\blacksquare$

> Beachten Sie, dass das Superpositionsprinzip nur für homogene lineare Differentialgleichungen gilt und nicht für inhomogene lineare oder nichtlineare Differentialgleichungen.
{: .prompt-warning }

## Basis und allgemeine Lösung
### Wiederholung der Hauptkonzepte von DGLs erster Ordnung
Wie bereits im Beitrag über [Grundkonzepte der Modellierung](/posts/Basic-Concepts-of-Modeling/) erläutert, besteht ein Anfangswertproblem für eine Differentialgleichung erster Ordnung aus der DGL selbst und einer Anfangsbedingung $y(x_0)=y_0$. Die Anfangsbedingung ist notwendig, um die beliebige Konstante $c$ in der allgemeinen Lösung der DGL zu bestimmen. Die so bestimmte Lösung wird als partikuläre Lösung bezeichnet. Erweitern wir nun diese Konzepte auf Differentialgleichungen zweiter Ordnung.

### Anfangswertproblem und Anfangsbedingungen
Ein **Anfangswertproblem** für eine homogene DGL zweiter Ordnung ($\ref{eqn:homogeneous_linear_ode}$) besteht aus der gegebenen DGL ($\ref{eqn:homogeneous_linear_ode}$) und zwei **Anfangsbedingungen**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Diese Bedingungen sind erforderlich, um die beiden beliebigen Konstanten $c_1$ und $c_2$ in der **allgemeinen Lösung**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

der DGL zu bestimmen.

### Lineare Unabhängigkeit und Abhängigkeit
Lassen Sie uns hier kurz die Konzepte der linearen Unabhängigkeit und Abhängigkeit betrachten. Dies ist notwendig, um später den Begriff der Basis zu definieren.  
Zwei auf einem Intervall $I$ definierte Funktionen $y_1$ und $y_2$ heißen auf diesem Intervall **linear unabhängig**, wenn für alle Punkte in $I$ gilt:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ und }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

Andernfalls heißen $y_1$ und $y_2$ **linear abhängig**.

Wenn $y_1$ und $y_2$ linear abhängig sind (d.h., die Aussage ($\ref{eqn:linearly_independent}$) ist nicht wahr), dann gilt $k_1 \neq 0$ oder $k_2 \neq 0$. Man kann dann beide Seiten der Gleichung in ($\ref{eqn:linearly_independent}$) teilen, um

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{oder} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

zu schreiben, was zeigt, dass $y_1$ und $y_2$ proportional zueinander sind.

### Basis, allgemeine Lösung, partikuläre Lösung
Zurück zum Thema: Damit Gleichung ($\ref{eqn:general_sol}$) eine allgemeine Lösung ist, müssen $y_1$ und $y_2$ Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) sein und gleichzeitig auf dem Intervall $I$ nicht proportional, also linear unabhängig sein. Ein Paar $(y_1, y_2)$ von Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode}$), das diese Bedingung der linearen Unabhängigkeit auf dem Intervall $I$ erfüllt, wird als **Basis** oder **Fundamentalsystem** der Lösungen der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$ bezeichnet.

Durch die Verwendung der Anfangsbedingungen zur Bestimmung der beiden Konstanten $c_1$ und $c_2$ in der allgemeinen Lösung ($\ref{eqn:general_sol}$) erhält man eine eindeutige Lösung, die durch den Punkt $(x_0, K_0)$ geht und an diesem Punkt die Steigung $K_1$ hat. Diese wird als **partikuläre Lösung** der DGL ($\ref{eqn:homogeneous_linear_ode}$) bezeichnet.

Wenn die Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf einem offenen Intervall $I$ stetig ist, besitzt sie notwendigerweise eine allgemeine Lösung, die alle möglichen partikulären Lösungen umfasst. Das bedeutet, in diesem Fall hat die Gleichung ($\ref{eqn:homogeneous_linear_ode}$) keine singulären Lösungen, die nicht aus der allgemeinen Lösung abgeleitet werden können.

## Reduktionsverfahren (reduction of order)
Wenn man eine Lösung einer homogenen DGL zweiter Ordnung finden kann, kann man eine zweite, linear unabhängige Lösung – also eine Basis – finden, indem man eine DGL erster Ordnung löst. Dieses Verfahren wird als **Reduktionsverfahren (reduction of order)** bezeichnet.

Betrachten wir eine homogene DGL zweiter Ordnung <u>in Standardform mit $y^{\prime\prime}$ anstelle von $f(x)y^{\prime\prime}$</u>

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

und nehmen wir an, wir kennen eine Lösung $y_1$ dieser Gleichung auf einem offenen Intervall $I$.

Setzen wir nun die gesuchte zweite Lösung als $y_2 = uy_1$ an und

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

setzen dies in die Gleichung ein, erhalten wir

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Wenn wir die Terme nach $u^{\prime\prime}$, $u^{\prime}$ und $u$ gruppieren und ordnen, erhalten wir

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Da $y_1$ jedoch eine Lösung der gegebenen Gleichung ist, ist der Ausdruck in der letzten Klammer gleich 0. Daher verschwindet der Term mit $u$, und es bleibt eine DGL für $u^{\prime}$ und $u^{\prime\prime}$ übrig. Wenn wir beide Seiten dieser verbleibenden DGL durch $y_1$ teilen und $u^{\prime}=U$ sowie $u^{\prime\prime}=U^{\prime}$ setzen, erhalten wir die folgende DGL erster Ordnung.

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Durch [Trennung der Variablen](/posts/Separation-of-Variables/) und Integration erhalten wir

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

und wenn wir auf beiden Seiten die Exponentialfunktion anwenden, erhalten wir schließlich

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Da wir zuvor $U=u^{\prime}$ gesetzt haben, ist $u=\int U dx$, und die gesuchte zweite Lösung $y_2$ ist

$$ y_2 = uy_1 = y_1 \int U dx $$

Da $\cfrac{y_2}{y_1} = u = \int U dx$ keine Konstante sein kann, solange $U>0$ ist, bilden $y_1$ und $y_2$ eine Basis von Lösungen.

### Anwendung des Reduktionsverfahrens
Eine allgemeine DGL zweiter Ordnung $F(x, y, y^\prime, y^{\prime\prime})=0$, ob linear oder nichtlinear, kann mittels Reduktionsverfahren auf eine DGL erster Ordnung reduziert werden, wenn $y$ nicht explizit vorkommt, wenn $x$ nicht explizit vorkommt, oder, wie bereits gesehen, wenn die Gleichung linear homogen ist und eine Lösung bereits bekannt ist.

#### Fall, in dem y nicht explizit vorkommt
In $F(x, y^\prime, y^{\prime\prime})=0$ setzen wir $z=y^{\prime}$. Dies führt zu einer DGL erster Ordnung für $z$, nämlich $F(x, z, z^{\prime})$.

#### Fall, in dem x nicht explizit vorkommt
In $F(y, y^\prime, y^{\prime\prime})=0$ setzen wir $z=y^{\prime}$. Dann ist $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$. Dies führt zu einer DGL erster Ordnung für $z$, $F(y,z,z^\prime)$, in der $y$ die Rolle der unabhängigen Variable $x$ übernimmt.
