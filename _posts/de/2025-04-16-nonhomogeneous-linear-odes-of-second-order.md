---
title: Inhomogene lineare Differentialgleichungen zweiter Ordnung
description: Untersuchung der Struktur und Eigenschaften inhomogener linearer Differentialgleichungen zweiter Ordnung, einschließlich der allgemeinen Lösungsmethodik und des Beweises, dass die allgemeine Lösung alle möglichen Lösungen umfasst.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Die **allgemeine Lösung** einer inhomogenen linearen Differentialgleichung zweiter Ordnung $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: allgemeine Lösung der homogenen Differentialgleichung $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ in der Form $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: partikuläre Lösung der inhomogenen Differentialgleichung
> - Der Antwortterm $y_p$ wird nur durch die Eingabe $r(x)$ bestimmt und ändert sich nicht bei unterschiedlichen Anfangsbedingungen für dieselbe inhomogene Differentialgleichung. Die Differenz zweier partikulärer Lösungen der inhomogenen Differentialgleichung ist eine Lösung der entsprechenden homogenen Differentialgleichung.
> - **Existenz der allgemeinen Lösung**: Wenn die Koeffizienten $p(x)$, $q(x)$ und die Eingabefunktion $r(x)$ stetig sind, existiert immer eine allgemeine Lösung
> - **Nichtexistenz singulärer Lösungen**: Die allgemeine Lösung umfasst alle Lösungen der Differentialgleichung (d.h., es gibt keine singulären Lösungen)
{: .prompt-info }

## Voraussetzungen
- [Homogene lineare Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskian, Existenz und Eindeutigkeit der Lösungen](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Allgemeine Lösung und partikuläre Lösung inhomogener linearer Differentialgleichungen zweiter Ordnung
Betrachten wir die inhomogene lineare Differentialgleichung zweiter Ordnung

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

wobei $r(x) \not\equiv 0$. Die **allgemeine Lösung** dieser inhomogenen Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf einem offenen Intervall $I$ hat die Form

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

wobei $y_h = c_1y_1 + c_2y_2$ die allgemeine Lösung der entsprechenden homogenen Differentialgleichung

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

ist und $y_p$ eine partikuläre Lösung der inhomogenen Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) darstellt. Eine **partikuläre Lösung** der Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ erhält man, indem man den Konstanten $c_1$ und $c_2$ in $y_h$ bestimmte Werte zuweist und diese in Gleichung ($\ref{eqn:general_sol}$) einsetzt.

Das bedeutet, wenn wir zur homogenen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) eine nur von der unabhängigen Variable $x$ abhängige Eingabe $r(x)$ hinzufügen, wird ein entsprechender Term $y_p$ zur Antwort hinzugefügt. Dieser zusätzliche Antwortterm $y_p$ wird unabhängig von den Anfangsbedingungen ausschließlich durch die Eingabe $r(x)$ bestimmt. Wie wir später sehen werden, ergibt die Differenz zweier beliebiger Lösungen $y_1$ und $y_2$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) (d.h. die Differenz zweier partikulärer Lösungen mit unterschiedlichen Anfangsbedingungen) nach Eliminierung des von den Anfangsbedingungen unabhängigen Terms $y_p$ die Differenz zwischen ${y_h}_1$ und ${y_h}_2$, die gemäß dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) eine Lösung der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) ist.

## Beziehung zwischen den Lösungen der inhomogenen Differentialgleichung und der entsprechenden homogenen Differentialgleichung
> **Satz 1: Beziehung zwischen den Lösungen der inhomogenen Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) und der homogenen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** Wenn $y$ eine Lösung der inhomogenen Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) und $\tilde{y}$ eine Lösung der homogenen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) auf einem offenen Intervall $I$ ist, dann ist die Summe $y + \tilde{y}$ eine Lösung der Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$. Insbesondere ist die Funktion ($\ref{eqn:general_sol}$) eine Lösung der Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$.  
> **(b)** Die Differenz zweier Lösungen der inhomogenen Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ ist eine Lösung der homogenen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$.
{: .prompt-info }

### Beweis
#### (a)
Bezeichnen wir die linke Seite der Gleichungen ($\ref{eqn:nonhomogeneous_linear_ode}$) und ($\ref{eqn:homogeneous_linear_ode}$) mit $L[y]$. Dann gilt für jede Lösung $y$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) und jede Lösung $\tilde{y}$ der Gleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Für zwei beliebige Lösungen $y$ und $y^\*$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ gilt:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## Die allgemeine Lösung umfasst alle Lösungen
Für homogene lineare Differentialgleichungen ($\ref{eqn:homogeneous_linear_ode}$) wissen wir bereits, dass die [allgemeine Lösung alle Lösungen umfasst](/posts/wronskian-existence-and-uniqueness-of-solutions/#die-allgemeine-lösung-umfasst-alle-lösungen). Wir zeigen nun, dass dies auch für inhomogene lineare Differentialgleichungen ($\ref{eqn:nonhomogeneous_linear_ode}$) gilt.

> **Satz 2: Die allgemeine Lösung der inhomogenen Differentialgleichung umfasst alle Lösungen**  
> Wenn die Koeffizienten $p(x)$, $q(x)$ und die Eingabefunktion $r(x)$ auf einem offenen Intervall $I$ stetig sind, dann kann jede Lösung der Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ durch geeignete Wahl der Konstanten $c_1$ und $c_2$ in der allgemeinen Lösung ($\ref{eqn:general_sol}$) dargestellt werden.
{: .prompt-info }

### Beweis
Sei $y^\*$ eine beliebige Lösung der Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ und $x_0$ ein Punkt in diesem Intervall. Nach dem [Existenzsatz für die allgemeine Lösung homogener linearer Differentialgleichungen](/posts/wronskian-existence-and-uniqueness-of-solutions/#existenz-der-allgemeinen-lösung) existiert die allgemeine Lösung $y_h = c_1y_1 + c_2y_2$, und durch die später zu behandelnde **Methode der Variation der Parameter** existiert auch $y_p$, sodass die allgemeine Lösung ($\ref{eqn:general_sol}$) der Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) auf dem Intervall $I$ existiert. Nach dem zuvor bewiesenen Satz [1(b)](#beziehung-zwischen-den-lösungen-der-inhomogenen-differentialgleichung-und-der-entsprechenden-homogenen-differentialgleichung) ist $Y = y^\* - y_p$ eine Lösung der homogenen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) auf dem Intervall $I$ mit

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Nach dem [Existenz- und Eindeutigkeitssatz für Anfangswertprobleme](/posts/wronskian-existence-and-uniqueness-of-solutions/#existenz--und-eindeutigkeitssatz-für-anfangswertprobleme) existiert auf dem Intervall $I$ eine eindeutige Lösung $Y$ der homogenen Differentialgleichung ($\ref{eqn:homogeneous_linear_ode}$) mit diesen Anfangsbedingungen, die durch geeignete Wahl der Konstanten $c_1$ und $c_2$ in $y_h$ dargestellt werden kann. Da $y^\* = Y + y_p$ gilt, kann jede partikuläre Lösung $y^\*$ der inhomogenen Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) aus der allgemeinen Lösung ($\ref{eqn:general_sol}$) abgeleitet werden. $\blacksquare$
