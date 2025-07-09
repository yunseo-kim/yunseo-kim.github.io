---
title: "Die Methode der unbestimmten Koeffizienten"
description: "Die Methode der unbestimmten Koeffizienten vereinfacht die Lösung von Anfangswertproblemen für bestimmte inhomogene lineare DGLs mit konstanten Koeffizienten. Sie ist besonders nützlich in der Technik für Modelle wie Schwingungssysteme oder RLC-Schaltkreise."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Anwendungsbereich der Methode der unbestimmten Koeffizienten**:
>   - Lineare gewöhnliche Differentialgleichungen der Form $y^{\prime\prime} + ay^{\prime} + by = r(x)$
>   - mit **konstanten Koeffizienten $a$ und $b$**,
>   - und einer Inhomogenität $r(x)$, die aus Exponentialfunktionen, Potenzen von $x$, $\cos$ oder $\sin$ oder Summen und Produkten solcher Funktionen besteht.
> - **Ansatzregeln für die Methode der unbestimmten Koeffizienten**  
>   - **(a) Grundregel**: Wenn $r(x)$ in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) einer der Funktionen in der ersten Spalte der Tabelle entspricht, wählen Sie den Ansatz $y_p$ aus derselben Zeile und bestimmen Sie die unbestimmten Koeffizienten, indem Sie $y_p$ und seine Ableitungen in die Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) einsetzen.  
>   - **(b) Modifikationsregel**: Wenn ein Term im gewählten Ansatz für $y_p$ eine Lösung der zugehörigen homogenen DGL $y^{\prime\prime} + ay^{\prime} + by = 0$ ist, multiplizieren Sie diesen Term mit $x$ (oder mit $x^2$, falls diese Lösung einer doppelten Wurzel der charakteristischen Gleichung der homogenen DGL entspricht).  
>   - **(c) Summenregel**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wählen Sie für $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Ansatz für $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Voraussetzungen
- [Homogene lineare DGL zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Die Euler-Cauchy-Gleichung](/posts/euler-cauchy-equation/)
- [Wronski-Determinante, Existenz und Eindeutigkeit von Lösungen](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Inhomogene lineare DGL zweiter Ordnung](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Vektorräume, Lineare Hülle (Lineare Algebra)

## Die Methode der unbestimmten Koeffizienten
Betrachten wir eine inhomogene lineare Differentialgleichung zweiter Ordnung mit $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

und die zugehörige homogene Differentialgleichung

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Wie wir im Beitrag über [inhomogene lineare DGL zweiter Ordnung](/posts/nonhomogeneous-linear-odes-of-second-order/) gesehen haben, müssen wir zur Lösung eines Anfangswertproblems für die inhomogene lineare DGL ($\ref{eqn:nonhomogeneous_linear_ode}$) zunächst die homogene DGL ($\ref{eqn:homogeneous_linear_ode}$) lösen, um $y_h$ zu finden, und dann eine spezielle Lösung $y_p$ der Gleichung ($\ref{eqn:nonhomogeneous_linear_ode}$) finden, um die allgemeine Lösung

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

zu erhalten. Wie findet man also $y_p$? Eine allgemeine Methode zur Bestimmung von $y_p$ ist die **Methode der Variation der Konstanten**, aber in bestimmten Fällen kann die viel einfachere **Methode der unbestimmten Koeffizienten** angewendet werden. Insbesondere ist sie eine in der Technik häufig verwendete Methode, da sie auf Schwingungssysteme und RLC-Schaltkreis-Modelle anwendbar ist.

Die Methode der unbestimmten Koeffizienten eignet sich für lineare Differentialgleichungen mit **konstanten Koeffizienten $a$ und $b$** und einer Inhomogenität $r(x)$, die aus Exponentialfunktionen, Potenzen von $x$, $\cos$ oder $\sin$ oder Summen und Produkten solcher Funktionen besteht:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

Der Kern der Methode der unbestimmten Koeffizienten liegt darin, dass solche Funktionen $r(x)$ Ableitungen haben, die ihnen selbst ähneln. Um die Methode anzuwenden, wählt man einen Ansatz für $y_p$, der eine ähnliche Form wie $r(x)$ hat, aber unbestimmte Koeffizienten enthält, die durch Einsetzen von $y_p$ und seinen Ableitungen in die gegebene Differentialgleichung bestimmt werden. Die Regeln für die Wahl eines geeigneten Ansatzes für $y_p$ für praktisch wichtige Formen von $r(x)$ in der Technik lauten wie folgt.

> **Ansatzregeln für die Methode der unbestimmten Koeffizienten**  
> **(a) Grundregel**: Wenn $r(x)$ in Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) einer der Funktionen in der ersten Spalte der Tabelle entspricht, wählen Sie den Ansatz $y_p$ aus derselben Zeile und bestimmen Sie die unbestimmten Koeffizienten, indem Sie $y_p$ und seine Ableitungen in die Gleichung ($\ref{eqn:linear_ode_with_constant_coefficients}$) einsetzen.  
> **(b) Modifikationsregel**: Wenn ein Term im gewählten Ansatz für $y_p$ eine Lösung der zugehörigen homogenen DGL $y^{\prime\prime} + ay^{\prime} + by = 0$ ist, multiplizieren Sie diesen Term mit $x$ (oder mit $x^2$, falls diese Lösung einer doppelten Wurzel der charakteristischen Gleichung der homogenen DGL entspricht).  
> **(c) Summenregel**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wählen Sie für $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Ansatz für $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Diese Methode ist nicht nur einfach, sondern auch selbstkorrigierend. Wenn man einen falschen Ansatz für $y_p$ wählt oder zu wenige Terme verwendet, führt dies zu einem Widerspruch. Wählt man zu viele Terme, werden die Koeffizienten der überflüssigen Terme zu $0$, was zum richtigen Ergebnis führt. Selbst wenn bei der Anwendung der Methode etwas schief geht, wird man es im Laufe der Lösung bemerken. Solange man also einen einigermaßen vernünftigen Ansatz für $y_p$ gemäß den obigen Regeln wählt, kann man es ohne Bedenken versuchen.

### Beweis der Summenregel
Betrachten wir eine inhomogene lineare Differentialgleichung der Form $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Nehmen wir nun an, die folgenden beiden Gleichungen mit derselben linken Seite und den Inhomogenitäten $r_1$ bzw. $r_2$

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

haben die partikulären Lösungen ${y_p}_1$ bzw. ${y_p}_2$. Bezeichnen wir die linke Seite der gegebenen Gleichung mit $L[y]$, so gilt aufgrund der Linearität von $L[y]$ für $y_p = {y_p}_1 + {y_p}_2$ die folgende Beziehung, womit die Summenregel bewiesen ist.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Beispiel: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Nach der Grundregel (a) setzen wir $y_p = Ce^{\gamma x}$ in die gegebene Gleichung $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$ ein:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Fall $\gamma^2 + a\gamma + b \neq 0$
Wir können den unbestimmten Koeffizienten $C$ bestimmen und $y_p$ wie folgt finden:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Fall $\gamma^2 + a\gamma + b = 0$
In diesem Fall müssen wir die Modifikationsregel (b) anwenden. Zuerst bestimmen wir die Wurzeln der charakteristischen Gleichung der homogenen DGL $y^{\prime\prime} + ay^{\prime} + by = 0$, indem wir $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ verwenden.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Daraus erhalten wir die Basis der homogenen DGL:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Fall $\gamma \neq -a-\gamma$
Da der gewählte Ansatz $y_p = Ce^{\gamma x}$ eine einfache (nicht doppelte) Wurzel der charakteristischen Gleichung der zugehörigen homogenen DGL ist, multiplizieren wir diesen Term gemäß der Modifikationsregel (b) mit $x$ und setzen $y_p = Cxe^{\gamma x}$.

Setzen wir nun den modifizierten Ansatz $y_p$ wieder in die gegebene Gleichung $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ ein:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Fall $\gamma = -a-\gamma$
In diesem Fall ist der gewählte Ansatz $y_p = Ce^{\gamma x}$ eine doppelte Wurzel der charakteristischen Gleichung der zugehörigen homogenen DGL. Gemäß der Modifikationsregel (b) multiplizieren wir diesen Term mit $x^2$ und setzen $y_p = Cx^2 e^{\gamma x}$.

Setzen wir nun den modifizierten Ansatz $y_p$ wieder in die gegebene Gleichung $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ ein:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Erweiterung der Methode: $r(x)$ als Produkt von Funktionen
Betrachten wir eine inhomogene lineare Differentialgleichung der Form $r(x) = k x^n e^{\alpha x}\cos(\omega x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Wir werden zeigen, dass wenn $r(x)$ ein Produkt oder eine Summe von Funktionen wie der Exponentialfunktion $e^{\alpha x}$, einer Potenz von $x$ ($x^m$) und $\cos{\omega x}$ oder $\sin{\omega x}$ ist (hier nehmen wir $\cos$ an, ohne an Allgemeinheit zu verlieren), also wenn $r(x)$ als Summe und Produkt von Funktionen aus der ersten Spalte der obigen Tabelle ausgedrückt werden kann, eine Lösung $y_p$ der Gleichung existiert, die eine Summe und ein Produkt von Funktionen aus der zweiten Spalte derselben Tabelle ist.

> Für einen rigorosen Beweis werden Teile mit Konzepten aus der linearen Algebra beschrieben, die mit einem \* markiert sind. Sie können diese Abschnitte überspringen und trotzdem ein grundlegendes Verständnis erlangen.
{: .prompt-tip }

### Definition des Vektorraums $V$*
Für ein $r(x)$ der Form
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

können wir einen Vektorraum $V$ so definieren, dass $r(x) \in V$:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Ableitungsformen von Exponential-, Polynom- und trigonometrischen Funktionen
Die Ableitungsformen der Grundfunktionen aus der ersten Spalte der obigen Tabelle sind wie folgt:
- Exponentialfunktion: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Polynomfunktion: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Trigonometrische Funktionen: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Die durch Differenzieren dieser Funktionen erhaltenen Ableitungen werden ebenfalls als <u>Summe von Funktionen desselben Typs</u> ausgedrückt.

Wenn also die Funktionen $f$ und $g$ die oben genannten Funktionen oder deren Summen sind, ergibt die Anwendung der Produktregel auf $r(x) = f(x)g(x)$:

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

Hier können $f$, $f^{\prime}$, $f^{\prime\prime}$ und $g$, $g^{\prime}$, $g^{\prime\prime}$ alle als Summen oder skalare Vielfache von Exponential-, Polynom- und trigonometrischen Funktionen geschrieben werden. Daher können auch $r^{\prime}(x) = (fg)^{\prime}$ und $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ wie $r(x)$ als Summe und Produkt dieser Funktionen ausgedrückt werden.

### Invarianz von $V$ unter dem Differenzialoperator $D$ und der linearen Transformation $L$*
Das bedeutet, nicht nur $r(x)$ selbst, sondern auch $r^{\prime}(x)$ und $r^{\prime\prime}(x)$ sind Linearkombinationen von Termen der Form $x^k e^{\alpha x}\cos(\omega x)$ und $x^k e^{\alpha x}\sin(\omega x)$.

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Wenn wir dies nicht auf $r(x)$ beschränken, sondern allgemeiner für alle Elemente des zuvor definierten Vektorraums $V$ unter Verwendung des Differenzialoperators $D$ ausdrücken, ist *der Vektorraum $V$ unter dem Differenzialoperator $D$ abgeschlossen*. Bezeichnen wir die linke Seite der gegebenen Gleichung $y^{\prime\prime} + ay^{\prime} + by$ mit $L[y]$, so ist *$V$ invariant unter $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Da $r(x) \in V$ und $V$ invariant unter $L$ ist, existiert ein weiteres Element $y_p \in V$, das $L[y_p] = r$ erfüllt.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Daher, wenn wir einen geeigneten Ansatz für $y_p$ als Summe aller möglichen Produktterme mit unbestimmten Koeffizienten $A_0, A_1, \dots, A_n$ und $K, M$ wie folgt wählen, können wir die unbestimmten Koeffizienten bestimmen, indem wir $y_p$ (oder $xy_p$, $x^2y_p$) und seine Ableitungen gemäß der Grundregel (a) und der Modifikationsregel (b) in die gegebene Gleichung einsetzen. Dabei wird $n$ entsprechend dem Grad von $x$ in $r(x)$ bestimmt.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Wenn die gegebene Inhomogenität $r(x)$ verschiedene Werte für $\alpha_i$ und $\omega_j$ enthält, muss der Ansatz für $y_p$ so gewählt werden, dass er alle möglichen Terme der Form $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ und $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ für jeden Wert von $\alpha_i$ und $\omega_j$ enthält.  
> Der Vorteil der Methode der unbestimmten Koeffizienten liegt in ihrer Einfachheit. Wenn der Ansatz zu kompliziert wird und dieser Vorteil verloren geht, ist es möglicherweise besser, die später zu behandelnde Methode der Variation der Konstanten anzuwenden.
{: .prompt-warning }

## Erweiterung der Methode: Die Euler-Cauchy-Gleichung
Die Methode der unbestimmten Koeffizienten kann nicht nur auf [homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/), sondern auch auf die [Euler-Cauchy-Gleichung](/posts/euler-cauchy-equation/) angewendet werden:

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Variablensubstitution
Durch die [Transformation in eine homogene lineare DGL mit konstanten Koeffizienten durch Substitution von $x = e^t$](/posts/euler-cauchy-equation/#transformation-in-eine-homogene-lineare-gdgl-mit-konstanten-koeffizienten) mit

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

kann die Euler-Cauchy-Gleichung, wie wir bereits gesehen haben, in die folgende homogene lineare DGL mit konstanten Koeffizienten bezüglich $t$ umgewandelt werden:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Nun können wir die [zuvor besprochene Methode der unbestimmten Koeffizienten](#die-methode-der-unbestimmten-koeffizienten) auf die Gleichung ($\ref{eqn:substituted}$) anwenden, um sie für $t$ zu lösen, und schließlich die Lösung für $x$ finden, indem wir $t = \ln x$ verwenden.

### Fall, in dem $r(x)$ aus Potenzen von $x$, natürlichen Logarithmen oder Summen und Produkten solcher Funktionen besteht
Insbesondere wenn die Inhomogenität $r(x)$ aus Potenzen von $x$, natürlichen Logarithmen oder Summen und Produkten solcher Funktionen besteht, kann ein geeigneter Ansatz für $y_p$ direkt gemäß den folgenden Ansatzregeln für die Euler-Cauchy-Gleichung gewählt werden.

> **Ansatzregeln für die Methode der unbestimmten Koeffizienten: Euler-Cauchy-Gleichung**  
> **(a) Grundregel**: Wenn $r(x)$ in Gleichung ($\ref{eqn:euler_cauchy}$) einer der Funktionen in der ersten Spalte der Tabelle entspricht, wählen Sie den Ansatz $y_p$ aus derselben Zeile und bestimmen Sie die unbestimmten Koeffizienten, indem Sie $y_p$ und seine Ableitungen in die Gleichung ($\ref{eqn:euler_cauchy}$) einsetzen.  
> **(b) Modifikationsregel**: Wenn ein Term im gewählten Ansatz für $y_p$ eine Lösung der zugehörigen homogenen DGL $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ ist, multiplizieren Sie diesen Term mit $\ln{x}$ (oder mit $(\ln{x})^2$, falls diese Lösung einer doppelten Wurzel der charakteristischen Gleichung der homogenen DGL entspricht).  
> **(c) Summenregel**: Wenn $r(x)$ eine Summe von Funktionen aus der ersten Spalte der Tabelle ist, wählen Sie für $y_p$ die Summe der entsprechenden Funktionen aus der zweiten Spalte.
>
> | Term in $r(x)$ | Ansatz für $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Auf diese Weise kann für praktisch wichtige Formen der Inhomogenität $r(x)$ ein Ansatz für $y_p$ gefunden werden, der mit dem durch die [Variablensubstitution](#variablensubstitution) erhaltenen identisch ist, jedoch schneller und einfacher. Man kann diese Ansatzregeln für die Euler-Cauchy-Gleichung ableiten, indem man in den [ursprünglichen Ansatzregeln](#die-methode-der-unbestimmten-koeffizienten) $x$ durch $\ln{x}$ ersetzt.
