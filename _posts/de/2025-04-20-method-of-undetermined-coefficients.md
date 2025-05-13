---
title: Methode der unbestimmten Koeffizienten
description: Lernen wir die Methode der unbestimmten Koeffizienten kennen, die eine einfache Lösung für Anfangswertprobleme bestimmter linearer inhomogener Differentialgleichungen mit konstanten Koeffizienten bietet und häufig in der Ingenieurwissenschaft für Schwingungssysteme und RLC-Stromkreise verwendet wird.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Methode der unbestimmten Koeffizienten** ist anwendbar auf:
>   - Lineare Differentialgleichungen mit **konstanten Koeffizienten $a$ und $b$**
>   - Eingangsfunktion $r(x)$ besteht aus Exponentialfunktionen, Potenzen von $x$, $\cos$ oder $\sin$, oder Summen und Produkten dieser Funktionen
>   - Form: $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Auswahlregeln für die Methode der unbestimmten Koeffizienten**  
>   - **(a) Grundregel (basic rule)**: Wenn $r(x)$ in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) eine der Funktionen in der ersten Spalte der Tabelle ist, wähle $y_p$ aus der entsprechenden Zeile der zweiten Spalte und bestimme die unbestimmten Koeffizienten durch Einsetzen von $y_p$ und seinen Ableitungen in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Modifikationsregel (modification rule)**: Wenn der für $y_p$ gewählte Term eine Lösung der homogenen Differentialgleichung $y^{\prime\prime} + ay^{\prime} + by = 0$ ist, multipliziere diesen Term mit $x$ (oder mit $x^2$, falls dieser Term einer Doppelwurzel der charakteristischen Gleichung der homogenen Differentialgleichung entspricht).  
>   - **(c) Summenregel (sum rule)**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wähle für $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Wahl für $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [Homogene lineare Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogene lineare Differentialgleichungen zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Euler-Cauchy-Gleichung](/posts/euler-cauchy-equation/)
- [Wronskian, Existenz und Eindeutigkeit von Lösungen](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Inhomogene lineare Differentialgleichungen zweiter Ordnung](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Vektorräume, lineare Erzeugung (Lineare Algebra)

## Methode der unbestimmten Koeffizienten
Betrachten wir eine inhomogene lineare Differentialgleichung zweiter Ordnung mit $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

und die entsprechende homogene Differentialgleichung

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Wie wir in [Inhomogene lineare Differentialgleichungen zweiter Ordnung](/posts/nonhomogeneous-linear-odes-of-second-order/) gesehen haben, müssen wir zur Lösung eines Anfangswertproblems für die inhomogene Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) zunächst die homogene Gleichung ($\ref{eqn:homogeneous_linear_ode}$) lösen, um $y_h$ zu finden, und dann eine partikuläre Lösung $y_p$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) bestimmen, um die allgemeine Lösung

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

zu erhalten. Wie finden wir aber $y_p$? Die allgemeine Methode zur Bestimmung von $y_p$ ist die **Methode der Variation der Parameter**, aber in bestimmten Fällen kann die viel einfachere **Methode der unbestimmten Koeffizienten** angewendet werden. Diese Methode wird besonders häufig in der Ingenieurwissenschaft für Schwingungssysteme und RLC-Stromkreise verwendet.

Die Methode der unbestimmten Koeffizienten eignet sich für lineare Differentialgleichungen mit **konstanten Koeffizienten $a$ und $b$**, bei denen die Eingangsfunktion $r(x)$ aus Exponentialfunktionen, Potenzen von $x$, $\cos$ oder $\sin$, oder Summen und Produkten dieser Funktionen besteht:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

Der Kerngedanke dieser Methode ist, dass solche Formen von $r(x)$ Ableitungen haben, die ähnlich zu ihnen selbst sind. Zur Anwendung der Methode wählt man ein $y_p$ mit ähnlicher Form wie $r(x)$, jedoch mit unbestimmten Koeffizienten, die durch Einsetzen in die gegebene Differentialgleichung bestimmt werden. Die Regeln zur Auswahl eines geeigneten $y_p$ für praktisch wichtige Formen von $r(x)$ sind wie folgt:

> **Auswahlregeln für die Methode der unbestimmten Koeffizienten**  
> **(a) Grundregel (basic rule)**: Wenn $r(x)$ in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) eine der Funktionen in der ersten Spalte der Tabelle ist, wähle $y_p$ aus der entsprechenden Zeile der zweiten Spalte und bestimme die unbestimmten Koeffizienten durch Einsetzen von $y_p$ und seinen Ableitungen in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Modifikationsregel (modification rule)**: Wenn der für $y_p$ gewählte Term eine Lösung der homogenen Differentialgleichung $y^{\prime\prime} + ay^{\prime} + by = 0$ ist, multipliziere diesen Term mit $x$ (oder mit $x^2$, falls dieser Term einer Doppelwurzel der charakteristischen Gleichung der homogenen Differentialgleichung entspricht).  
> **(c) Summenregel (sum rule)**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wähle für $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Wahl für $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Diese Methode hat den Vorteil, dass sie nicht nur einfach ist, sondern auch selbstkorrigierend. Wenn man $y_p$ falsch wählt oder zu wenige Terme auswählt, führt dies zu Widersprüchen; wählt man zu viele Terme, werden die Koeffizienten der unnötigen Terme zu Null, und man erhält trotzdem das richtige Ergebnis. Selbst wenn bei der Anwendung der Methode etwas schief geht, wird man es im Lösungsprozess bemerken, sodass man ohne Bedenken einen Versuch wagen kann, solange man den Auswahlregeln einigermaßen folgt.

### Beweis der Summenregel
Betrachten wir eine inhomogene lineare Differentialgleichung der Form

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Nun betrachten wir zwei Gleichungen mit derselben linken Seite, aber mit $r_1$ bzw. $r_2$ als Eingangsfunktionen:

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Angenommen, diese haben jeweils die Lösungen ${y_p}_1$ und ${y_p}_2$. Wenn wir die linke Seite mit $L[y]$ bezeichnen, dann gilt aufgrund der Linearität von $L[y]$ für $y_p = {y_p}_1 + {y_p}_2$:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Beispiel: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Nach der Grundregel (a) setzen wir $y_p = Ce^{\gamma x}$ und in die gegebene Gleichung $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$ ein:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Fall: $\gamma^2 + a\gamma + b \neq 0$
In diesem Fall können wir den unbestimmten Koeffizienten $C$ wie folgt bestimmen und $y_p$ finden:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Fall: $\gamma^2 + a\gamma + b = 0$
In diesem Fall müssen wir die Modifikationsregel (b) anwenden. Zunächst nutzen wir $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, um die Wurzeln der charakteristischen Gleichung der homogenen Differentialgleichung $y^{\prime\prime} + ay^{\prime} + by = 0$ zu finden:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Daraus erhalten wir die Basis der homogenen Differentialgleichung:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Fall: $\gamma \neq -a-\gamma$
Da der für $y_p$ gewählte Term $Ce^{\gamma x}$ eine Lösung der homogenen Differentialgleichung ist, aber keine Doppelwurzel der charakteristischen Gleichung, multiplizieren wir diesen Term gemäß der Modifikationsregel (b) mit $x$ und setzen $y_p = Cxe^{\gamma x}$.

Wenn wir dieses modifizierte $y_p$ in die gegebene Gleichung $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ einsetzen, erhalten wir:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Fall: $\gamma = -a-\gamma$
In diesem Fall ist der für $y_p$ gewählte Term $Ce^{\gamma x}$ eine Lösung der homogenen Differentialgleichung, die einer Doppelwurzel der charakteristischen Gleichung entspricht. Gemäß der Modifikationsregel (b) multiplizieren wir diesen Term mit $x^2$ und setzen $y_p = Cx^2 e^{\gamma x}$.

Wenn wir dieses modifizierte $y_p$ in die gegebene Gleichung $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ einsetzen, erhalten wir:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Erweiterung der Methode: $r(x)$ als Produkt von Funktionen
Betrachten wir eine inhomogene lineare Differentialgleichung der Form

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Wenn $r(x)$ ein Produkt aus Exponentialfunktion $e^{\alpha x}$, Potenz von $x$ ($x^m$), und $\cos{\omega x}$ oder $\sin{\omega x}$ ist (hier nehmen wir $\cos$ an, ohne Beschränkung der Allgemeinheit), dann können wir zeigen, dass eine Lösung $y_p$ existiert, die ein Produkt der entsprechenden Funktionen aus der zweiten Spalte der Tabelle ist.

> Teile des Beweises, die strenge mathematische Konzepte aus der linearen Algebra verwenden, sind mit \* gekennzeichnet. Diese Teile können übersprungen werden, ohne das grundlegende Verständnis zu beeinträchtigen.
{: .prompt-tip }

### Definition des Vektorraums $V$\*
Für $r(x)$ der Form
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

können wir einen Vektorraum $V$ definieren, für den $r(x) \in V$ gilt:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Form der Ableitungen von Exponential-, Polynom- und trigonometrischen Funktionen
Die Ableitungen der in der ersten Spalte der Tabelle aufgeführten Grundfunktionen haben folgende Formen:
- Exponentialfunktion: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Polynomfunktion: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Trigonometrische Funktion: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Die Ableitungen dieser Funktionen können wieder als <u>Summen von Funktionen derselben Art</u> ausgedrückt werden.

Wenn also $f$ und $g$ solche Funktionen oder Summen davon sind und $r(x) = f(x)g(x)$, dann gilt nach der Produktregel:

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

wobei $f$, $f^{\prime}$, $f^{\prime\prime}$ und $g$, $g^{\prime}$, $g^{\prime\prime}$ alle als Summen oder Vielfache von Exponential-, Polynom- und trigonometrischen Funktionen geschrieben werden können. Daher können auch $r^{\prime}(x) = (fg)^{\prime}$ und $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ als Summen und Produkte dieser Funktionen ausgedrückt werden.

### Invarianz von $V$ unter dem Differentialoperator $D$ und dem linearen Operator $L$\*
Das bedeutet, dass nicht nur $r(x)$ selbst, sondern auch $r^{\prime}(x)$ und $r^{\prime\prime}(x)$ lineare Kombinationen von Termen der Form $x^k e^{\alpha x}\cos(\omega x)$ und $x^k e^{\alpha x}\sin(\omega x)$ sind, also:

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Allgemeiner ausgedrückt, wenn wir den Differentialoperator $D$ für alle Elemente des Vektorraums $V$ einführen, dann ist *der Vektorraum $V$ abgeschlossen unter der Differentialoperation $D$*. Wenn wir die linke Seite der gegebenen Gleichung $y^{\prime\prime} + ay^{\prime} + by$ als $L[y]$ bezeichnen, dann ist *$V$ invariant unter $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Da $r(x) \in V$ und $V$ invariant unter $L$ ist, existiert ein weiteres Element $y_p \in V$, das $L[y_p] = r$ erfüllt.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Daher können wir ein geeignetes $y_p$ als Summe aller möglichen Produktterme mit unbestimmten Koeffizienten $A_0, A_1, \dots, A_n$ und $K$, $M$ wie folgt wählen:

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

Gemäß der Grundregel (a) und der Modifikationsregel (b) können wir dann $y_p$ (oder $xy_p$, $x^2y_p$) und seine Ableitungen in die gegebene Gleichung einsetzen, um die unbestimmten Koeffizienten zu bestimmen. Dabei wird $n$ entsprechend dem Grad von $x$ in $r(x)$ gewählt.

$\blacksquare$

> Wenn die gegebene Eingangsfunktion $r(x)$ verschiedene $\alpha_i$ und $\omega_j$ Werte enthält, muss $y_p$ so gewählt werden, dass es alle möglichen Terme der Form $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ und $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ für jeden Wert von $\alpha_i$ und $\omega_j$ enthält.  
> Der Vorteil der Methode der unbestimmten Koeffizienten liegt in ihrer Einfachheit. Wenn der Ansatz zu kompliziert wird und dieser Vorteil verloren geht, könnte es besser sein, stattdessen die Methode der Variation der Parameter anzuwenden.
{: .prompt-warning }

## Erweiterung der Methode: Euler-Cauchy-Gleichungen
Die Methode der unbestimmten Koeffizienten kann nicht nur auf [homogene lineare Differentialgleichungen zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/) angewendet werden, sondern auch auf [Euler-Cauchy-Gleichungen](/posts/euler-cauchy-equation/):

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Variablensubstitution
Durch die Substitution [$x = e^t$ kann die Gleichung in eine homogene lineare Differentialgleichung zweiter Ordnung mit konstanten Koeffizienten transformiert werden](/posts/euler-cauchy-equation/#transformation-in-eine-homogene-lineare-differentialgleichung-zweiter-ordnung-mit-konstanten-koeffizienten):

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

Dadurch wird die Euler-Cauchy-Gleichung zu einer Differentialgleichung mit konstanten Koeffizienten in $t$:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Wir können nun die [oben beschriebene Methode der unbestimmten Koeffizienten](#methode-der-unbestimmten-koeffizienten) auf Gleichung ($\ref{eqn:substituted}$) anwenden, um sie in Bezug auf $t$ zu lösen, und dann mit $t = \ln x$ zurück zu $x$ transformieren.

### Fall: $r(x)$ besteht aus Potenzen von $x$, natürlichen Logarithmen oder Summen und Produkten solcher Funktionen
Insbesondere wenn die Eingangsfunktion $r(x)$ aus Potenzen von $x$, natürlichen Logarithmen oder Summen und Produkten solcher Funktionen besteht, können wir direkt ein geeignetes $y_p$ gemäß den folgenden Auswahlregeln für Euler-Cauchy-Gleichungen wählen:

> **Auswahlregeln für die Methode der unbestimmten Koeffizienten: Für Euler-Cauchy-Gleichungen**  
> **(a) Grundregel (basic rule)**: Wenn $r(x)$ in Gleichung ($\ref{eqn:euler_cauchy}$) eine der Funktionen in der ersten Spalte der Tabelle ist, wähle $y_p$ aus der entsprechenden Zeile der zweiten Spalte und bestimme die unbestimmten Koeffizienten durch Einsetzen von $y_p$ und seinen Ableitungen in Gleichung ($\ref{eqn:euler_cauchy}$).  
> **(b) Modifikationsregel (modification rule)**: Wenn der für $y_p$ gewählte Term eine Lösung der homogenen Differentialgleichung $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ ist, multipliziere diesen Term mit $\ln{x}$ (oder mit $(\ln{x})^2$, falls dieser Term einer Doppelwurzel der charakteristischen Gleichung der homogenen Differentialgleichung entspricht).  
> **(c) Summenregel (sum rule)**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wähle für $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Wahl für $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Auf diese Weise können wir für praktisch wichtige Formen der Eingangsfunktion $r(x)$ schneller und einfacher ein geeignetes $y_p$ finden, das dem durch [Variablensubstitution](#variablensubstitution) erhaltenen entspricht. Diese Auswahlregeln für Euler-Cauchy-Gleichungen können aus den [ursprünglichen Auswahlregeln](#methode-der-unbestimmten-koeffizienten) abgeleitet werden, indem man $x$ durch $\ln{x}$ ersetzt.
