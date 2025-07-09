---
title: "Inhomogene lineare DGL zweiter Ordnung"
description: "Untersuchung der allgemeinen Lösung einer inhomogenen linearen DGL zweiter Ordnung, ihrer Beziehung zur homogenen Lösung, sowie der Existenz der allgemeinen und Nichtexistenz singulärer Lösungen."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Allgemeine Lösung** der inhomogenen linearen DGL zweiter Ordnung $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: allgemeine Lösung der homogenen GDGL $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: eine partikuläre Lösung der inhomogenen GDGL
> - Der Antwortterm $y_p$ wird nur durch die Eingabe $r(x)$ bestimmt und ändert sich nicht mit unterschiedlichen Anfangsbedingungen für dieselbe inhomogene GDGL. Die Differenz zweier partikulärer Lösungen der inhomogenen GDGL ist eine Lösung der zugehörigen homogenen GDGL.
> - **Existenz der allgemeinen Lösung**: Wenn die Koeffizienten $p(x)$, $q(x)$ und die Eingabefunktion $r(x)$ der inhomogenen GDGL stetig sind, existiert immer eine allgemeine Lösung.
> - **Nichtexistenz singulärer Lösungen**: Die allgemeine Lösung umfasst alle Lösungen der Gleichung (d.h. es existieren keine singulären Lösungen).
{: .prompt-info }

## Voraussetzungen
- [Homogene lineare DGL zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronski-Determinante, Existenz und Eindeutigkeit von Lösungen](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Allgemeine und partikuläre Lösung einer inhomogenen linearen DGL zweiter Ordnung
Betrachten wir die inhomogene lineare DGL zweiter Ordnung

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

Hierbei ist $r(x) \not\equiv 0$. Die **allgemeine Lösung** der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf einem offenen Intervall $I$ ist die Summe aus der allgemeinen Lösung $y_h = c_1y_1 + c_2y_2$ der zugehörigen homogenen GDGL

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

und einer partikulären Lösung $y_p$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) in der Form

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Eine **partikuläre Lösung** der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ ist eine Lösung, die man aus der allgemeinen Lösung ($\ref{eqn:general_sol}$) erhält, indem man den beliebigen Konstanten $c_1$ und $c_2$ in $y_h$ bestimmte Werte zuweist.

Das heißt, wenn zur homogenen GDGL ($\ref{eqn:homogeneous_linear_ode}$) eine nur von der unabhängigen Variablen $x$ abhängige Eingabe $r(x)$ hinzugefügt wird, wird der Antwort ein entsprechender Term $y_p$ hinzugefügt. Dieser zusätzliche Antwortterm $y_p$ wird ausschließlich durch die Eingabe $r(x)$ bestimmt und ist unabhängig von den Anfangsbedingungen. Wie wir später sehen werden, ist die Differenz zweier beliebiger Lösungen $y_1$ und $y_2$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) (d.h. die Differenz zweier partikulärer Lösungen für unterschiedliche Anfangsbedingungen) so, dass der von den Anfangsbedingungen unabhängige Teil $y_p$ sich aufhebt und nur die Differenz zwischen ${y_h}_1$ und ${y_h}_2$ übrig bleibt. Diese Differenz ist nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) eine Lösung der Gleichung ($\ref{eqn:homogeneous_linear_ode}$).

## Beziehung zwischen den Lösungen der inhomogenen und der zugehörigen homogenen GDGL
> **Satz 1: Beziehung zwischen den Lösungen der inhomogenen GDGL ($\ref{eqn:nonhomogeneous_linear_ode}$) und der homogenen GDGL ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Die Summe einer Lösung $y$ der inhomogenen GDGL ($\ref{eqn:nonhomogeneous_linear_ode}$) und einer Lösung $\tilde{y}$ der homogenen GDGL ($\ref{eqn:homogeneous_linear_ode}$) auf einem offenen Intervall $I$ ist eine Lösung der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$. Insbesondere ist die Gleichung ($\ref{eqn:general_sol}$) eine Lösung der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$.  
> **(b)** Die Differenz zweier Lösungen der inhomogenen GDGL ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ ist eine Lösung der homogenen GDGL ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$.
{: .prompt-info }

### Beweis
#### (a)
Bezeichnen wir die linke Seite der Gleichungen ($\ref{eqn:nonhomogeneous_linear_ode}$) und ($\ref{eqn:homogeneous_linear_ode}$) mit $L[y]$. Dann gilt für eine beliebige Lösung $y$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) und eine beliebige Lösung $\tilde{y}$ der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Für zwei beliebige Lösungen $y$ und $y^\*$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ gilt:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## Die allgemeine Lösung der inhomogenen GDGL umfasst alle Lösungen
Für die homogene GDGL ($\ref{eqn:homogeneous_linear_ode}$) wissen wir bereits, dass [die allgemeine Lösung alle Lösungen umfasst](/posts/wronskian-existence-and-uniqueness-of-solutions/#die-allgemeine-lösung-umfasst-alle-lösungen). Zeigen wir nun, dass dasselbe auch für die inhomogene GDGL ($\ref{eqn:nonhomogeneous_linear_ode}$) gilt.

> **Satz 2: Die allgemeine Lösung der inhomogenen GDGL umfasst alle Lösungen**  
> Wenn die Koeffizienten $p(x)$, $q(x)$ und die Eingabefunktion $r(x)$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf einem offenen Intervall $I$ stetig sind, dann kann jede Lösung der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ durch geeignete Wahl der beliebigen Konstanten $c_1$ und $c_2$ in $y_h$ der allgemeinen Lösung ($\ref{eqn:general_sol}$) der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ erhalten werden.
{: .prompt-info }

### Beweis
Sei $y^\*$ eine beliebige Lösung der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf $I$ und sei $x_0$ ein beliebiger Punkt im Intervall $I$. Nach dem [Satz über die Existenz einer allgemeinen Lösung](/posts/wronskian-existence-and-uniqueness-of-solutions/#existenz-einer-allgemeinen-lösung) existiert $y_h = c_1y_1 + c_2y_2$, und durch die später zu besprechende **Methode der Variation der Konstanten** existiert auch $y_p$, sodass die allgemeine Lösung ($\ref{eqn:general_sol}$) der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ existiert. Nach dem zuvor bewiesenen Satz [1(b)](#beziehung-zwischen-den-lösungen-der-inhomogenen-und-der-zugehörigen-homogenen-gdgl) ist $Y = y^\* - y_p$ eine Lösung der homogenen GDGL ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$, und bei $x_0$ gilt:

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Gemäß dem [Existenz- und Eindeutigkeitssatz für Anfangswertprobleme](/posts/wronskian-existence-and-uniqueness-of-solutions/#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) existiert auf dem Intervall $I$ eine eindeutige partikuläre Lösung $Y$ der homogenen GDGL ($\ref{eqn:homogeneous_linear_ode}$), die durch geeignete Wahl von $c_1$ und $c_2$ in $y_h$ für die obigen Anfangsbedingungen erhalten werden kann. Da $y^\* = Y + y_p$ ist, haben wir gezeigt, dass jede beliebige partikuläre Lösung $y^\*$ der inhomogenen GDGL ($\ref{eqn:nonhomogeneous_linear_ode}$) aus der allgemeinen Lösung ($\ref{eqn:general_sol}$) abgeleitet werden kann. $\blacksquare$
