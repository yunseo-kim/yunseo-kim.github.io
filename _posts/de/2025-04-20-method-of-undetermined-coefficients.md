---
title: Methode der unbestimmten Koeffizienten
description: Lernen wir die Methode der unbestimmten Koeffizienten kennen, eine nützliche Lösungsmethode in der Ingenieurwissenschaft für Schwingungssysteme und RLC-Schaltkreise, die Anfangswertprobleme bestimmter linearer Differentialgleichungen mit konstanten Koeffizienten vereinfacht.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Anwendungsbereich der Methode der unbestimmten Koeffizienten**:
>   - Lineare Differentialgleichungen mit **konstanten Koeffizienten $a$ und $b$**
>   - Eingangsfunktion $r(x)$ besteht aus Exponentialfunktionen, Potenzen von $x$, $\cos$ oder $\sin$, oder Summen und Produkten dieser Funktionen
>   - Lineare Differentialgleichung der Form $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Auswahlregeln für die Methode der unbestimmten Koeffizienten**  
>   - **(a) Grundregel (basic rule)**: Wenn $r(x)$ in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) eine der Funktionen in der ersten Spalte der Tabelle ist, wähle $y_p$ aus derselben Zeile und bestimme die unbestimmten Koeffizienten durch Einsetzen von $y_p$ und seinen Ableitungen in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Modifikationsregel (modification rule)**: Wenn der für $y_p$ gewählte Term eine Lösung der homogenen Differentialgleichung $y^{\prime\prime} + ay^{\prime} + by = 0$ ist, multipliziere diesen Term mit $x$ (oder mit $x^2$, falls dieser Term einer Doppelwurzel der charakteristischen Gleichung entspricht).  
>   - **(c) Summenregel (sum rule)**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wähle als $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Wahl für $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Voraussetzungen
- [Homogene lineare Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronski-Determinante, Existenz und Eindeutigkeit von Lösungen](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Inhomogene lineare Differentialgleichungen zweiter Ordnung](/posts/nonhomogeneous-linear-odes-of-second-order/)

## Methode der unbestimmten Koeffizienten
Betrachten wir eine inhomogene lineare Differentialgleichung zweiter Ordnung mit $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

und die entsprechende homogene Differentialgleichung

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Wie wir bereits in [Inhomogene lineare Differentialgleichungen zweiter Ordnung](/posts/nonhomogeneous-linear-odes-of-second-order/) gesehen haben, müssen wir zur Lösung eines Anfangswertproblems für die inhomogene Differentialgleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) zunächst die homogene Gleichung ($\ref{eqn:homogeneous_linear_ode}$) lösen, um $y_h$ zu finden, und dann eine partikuläre Lösung $y_p$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) bestimmen, um die allgemeine Lösung

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

zu erhalten. Wie finden wir nun $y_p$? Die allgemeine Methode zur Bestimmung von $y_p$ ist die **Methode der Variation der Parameter (method of variation of parameters)**, aber in bestimmten Fällen kann die viel einfachere **Methode der unbestimmten Koeffizienten (method of undetermined coefficients)** angewendet werden. Diese Methode ist besonders in der Ingenieurwissenschaft für Schwingungssysteme und RLC-Schaltkreise nützlich.

Die Methode der unbestimmten Koeffizienten eignet sich für lineare Differentialgleichungen mit **konstanten Koeffizienten $a$ und $b$**, bei denen die Eingangsfunktion $r(x)$ aus Exponentialfunktionen, Potenzen von $x$, $\cos$ oder $\sin$, oder Summen und Produkten dieser Funktionen besteht:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

Der Kerngedanke dieser Methode ist, dass solche Formen von $r(x)$ Ableitungen haben, die ihrer eigenen Form ähnlich sind. Um die Methode anzuwenden, wählt man für $y_p$ eine Form, die $r(x)$ ähnelt, aber unbestimmte Koeffizienten enthält, die durch Einsetzen in die gegebene Differentialgleichung bestimmt werden. Die Regeln zur Auswahl eines geeigneten $y_p$ für praktisch wichtige Formen von $r(x)$ in der Ingenieurwissenschaft sind wie folgt:

> **Auswahlregeln für die Methode der unbestimmten Koeffizienten**  
> **(a) Grundregel (basic rule)**: Wenn $r(x)$ in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) eine der Funktionen in der ersten Spalte der Tabelle ist, wähle $y_p$ aus derselben Zeile und bestimme die unbestimmten Koeffizienten durch Einsetzen von $y_p$ und seinen Ableitungen in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Modifikationsregel (modification rule)**: Wenn der für $y_p$ gewählte Term eine Lösung der homogenen Differentialgleichung $y^{\prime\prime} + ay^{\prime} + by = 0$ ist, multipliziere diesen Term mit $x$ (oder mit $x^2$, falls dieser Term einer Doppelwurzel der charakteristischen Gleichung entspricht).  
> **(c) Summenregel (sum rule)**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wähle als $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Wahl für $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Diese Methode ist nicht nur einfach, sondern hat auch den Vorteil der Selbstkorrektur. Wenn man $y_p$ falsch wählt oder zu wenige Terme auswählt, führt dies zu Widersprüchen; wählt man zu viele Terme, werden die Koeffizienten der unnötigen Terme zu Null, und man erhält trotzdem das richtige Ergebnis. Selbst wenn bei der Anwendung der Methode etwas schiefgeht, wird man es im Lösungsprozess bemerken, sodass man getrost einen Versuch wagen kann, solange man $y_p$ gemäß den obigen Regeln einigermaßen passend gewählt hat.

### Beweis der Summenregel
Betrachten wir eine inhomogene lineare Differentialgleichung der Form $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

Nun betrachten wir zwei Gleichungen mit derselben linken Seite, aber mit $r_1$ bzw. $r_2$ als Eingangsfunktionen:

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

Angenommen, diese haben jeweils ${y_p}_1$ und ${y_p}_2$ als Lösungen. Wenn wir die linke Seite der Gleichung als $L[y]$ bezeichnen, dann gilt aufgrund der Linearität von $L[y]$ für $y_p = {y_p}_1 + {y_p}_2$:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

### Beispiel: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Gemäß der Grundregel (a) setzen wir $y_p = Ce^{\gamma x}$ und substituieren in die gegebene Gleichung $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### Fall: $\gamma^2 + a\gamma + b \neq 0$
In diesem Fall können wir den unbestimmten Koeffizienten $C$ wie folgt bestimmen und $y_p$ finden:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### Fall: $\gamma^2 + a\gamma + b = 0$
In diesem Fall müssen wir die Modifikationsregel (b) anwenden. Zunächst nutzen wir $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, um die Wurzeln der charakteristischen Gleichung der homogenen Differentialgleichung $y^{\prime\prime} + ay^{\prime} + by = 0$ zu finden:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Daraus erhalten wir die Basis der homogenen Differentialgleichung:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

##### Fall: $\gamma \neq -a-\gamma$
Da der für $y_p$ gewählte Term $Ce^{\gamma x}$ eine Lösung der homogenen Differentialgleichung ist, aber keine Doppelwurzel, multiplizieren wir gemäß der Modifikationsregel (b) diesen Term mit $x$ und setzen $y_p = Cxe^{\gamma x}$.

Nun setzen wir das modifizierte $y_p$ in die gegebene Gleichung $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ ein:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### Fall: $\gamma = -a-\gamma$
In diesem Fall ist der für $y_p$ gewählte Term $Ce^{\gamma x}$ eine Lösung der homogenen Differentialgleichung, die einer Doppelwurzel entspricht. Gemäß der Modifikationsregel (b) multiplizieren wir diesen Term mit $x^2$ und setzen $y_p = Cx^2 e^{\gamma x}$.

Nun setzen wir das modifizierte $y_p$ in die gegebene Gleichung $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ ein:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
