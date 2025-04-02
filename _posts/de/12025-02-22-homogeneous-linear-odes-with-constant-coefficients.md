---
title: Lineare homogene Differentialgleichungen zweiter Ordnung mit konstanten Koeffizienten
description: Wir betrachten, wie die allgemeine Lösung einer linearen homogenen Differentialgleichung mit konstanten Koeffizienten je nach Vorzeichen der Diskriminante der charakteristischen Gleichung aussieht.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Lineare homogene Differentialgleichung zweiter Ordnung mit konstanten Koeffizienten: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Charakteristische Gleichung**: $\lambda^2 + a\lambda + b = 0$
> - Je nach Vorzeichen der Diskriminante $a^2 - 4b$ der charakteristischen Gleichung kann die allgemeine Lösung in drei Fälle unterteilt werden, wie in der Tabelle dargestellt
>
> | Fall | Lösungen der charakteristischen Gleichung | Basis der Lösungen der DGL | Allgemeine Lösung der DGL |
> | :---: | :---: | :---: | :---: |
> | I | Zwei verschiedene reelle Wurzeln<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Reelle Doppelwurzel<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Konjugiert komplexe Wurzeln<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$ <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Voraussetzungen
- [Bernoulli-Gleichung(Bernoulli Equation)](/posts/Bernoulli-Equation/)
- [Homogene lineare Differentialgleichungen zweiter Ordnung (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- Eulersche Formel

## Charakteristische Gleichung
Betrachten wir die lineare homogene Differentialgleichung zweiter Ordnung mit konstanten Koeffizienten $a$ und $b$

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Diese Art von Gleichung findet wichtige Anwendungen in mechanischen und elektrischen Schwingungen.

Wie wir zuvor in der [Bernoulli-Gleichung(Bernoulli Equation)](/posts/Bernoulli-Equation/) bei der Lösung der logistischen Gleichung gesehen haben, ist die Lösung einer linearen Differentialgleichung erster Ordnung mit konstantem Koeffizienten $k$

$$ y^\prime + ky = 0 $$

die Exponentialfunktion $y = ce^{-kx}$. (Dies entspricht dem Fall $A=-k$, $B=0$ in Gleichung (4) des genannten Beitrags)

Daher können wir für die ähnlich geformte Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) zunächst einen Lösungsansatz der Form

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

versuchen.

> Natürlich ist dies nur eine Vermutung, und es gibt keine Garantie, dass die allgemeine Lösung tatsächlich diese Form haben wird. Aber wenn wir irgendwie zwei linear unabhängige Lösungen finden können, können wir, wie wir in [Homogene lineare Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/#basis-und-allgemeine-lösung) gesehen haben, aufgrund des [Superpositionsprinzips](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) die allgemeine Lösung konstruieren.  
> Wie wir gleich sehen werden, gibt es auch [Fälle, in denen wir eine andere Form der Lösung finden müssen](#ii-reelle-doppelwurzel-lambda---cfraca2).
{: .prompt-info }

Wenn wir Gleichung ($\ref{eqn:general_sol}$) und ihre Ableitungen

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

in Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) einsetzen, erhalten wir

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Daher ist die Exponentialfunktion ($\ref{eqn:general_sol}$) eine Lösung der Differentialgleichung ($\ref{eqn:ode_with_constant_coefficients}$), wenn $\lambda$ eine Lösung der **charakteristischen Gleichung**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

ist. Die Lösungen dieser quadratischen Gleichung ($\ref{eqn:characteristic_eqn}$) sind

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a + \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

und daraus folgt, dass die beiden Funktionen

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) sind.

Nun können wir je nach Vorzeichen der Diskriminante $a^2 - 4b$ der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) drei Fälle unterscheiden:
- $a^2 - 4b > 0$: Zwei verschiedene reelle Wurzeln
- $a^2 - 4b = 0$: Reelle Doppelwurzel
- $a^2 - 4b < 0$: Konjugiert komplexe Wurzeln

## Form der allgemeinen Lösung je nach Vorzeichen der Diskriminante der charakteristischen Gleichung
### I. Zwei verschiedene reelle Wurzeln $\lambda_1$ und $\lambda_2$
In diesem Fall bilden

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

eine Basis der Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) in jedem Intervall, und die entsprechende allgemeine Lösung lautet

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Reelle Doppelwurzel $\lambda = -\cfrac{a}{2}$
Wenn $a^2 - 4b = 0$, hat die quadratische Gleichung ($\ref{eqn:characteristic_eqn}$) nur eine Lösung $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, und daher erhalten wir nur eine Lösung der Form $y = e^{\lambda x}$, nämlich

$$ y_1 = e^{-(a/2)x} $$

Um eine Basis zu erhalten, müssen wir eine zweite Lösung $y_2$ finden, die unabhängig von $y_1$ ist.

In dieser Situation können wir die zuvor besprochene [Ordnungsreduktion](/posts/homogeneous-linear-odes-of-second-order/#ordnungsreduktion) anwenden. Wir setzen die gesuchte zweite Lösung als $y_2=uy_1$ an und erhalten

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Wenn wir dies in Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) einsetzen, erhalten wir

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Nach Umordnung der Terme mit $u^{\prime\prime}$, $u^\prime$ und $u$ erhalten wir

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Da $y_1$ eine Lösung der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) ist, ist der Ausdruck in der letzten Klammer gleich 0, und da

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

ist auch der Ausdruck in der ersten Klammer gleich 0. Somit bleibt nur $u^{\prime\prime}y_1 = 0$ übrig, woraus folgt, dass $u^{\prime\prime}=0$. Zweimalige Integration ergibt $u = c_1x + c_2$, wobei die Integrationskonstanten $c_1$ und $c_2$ beliebige Werte annehmen können. Wir können einfach $c_1=1$ und $c_2=0$ wählen, sodass $u=x$. Dann wird $y_2 = uy_1 = xy_1$, und da $y_1$ und $y_2$ linear unabhängig sind, bilden sie eine Basis. Daher ist im Fall einer Doppelwurzel der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) die Basis der Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) in jedem Intervall

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

und die entsprechende allgemeine Lösung lautet

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Konjugiert komplexe Wurzeln $-\cfrac{1}{2}a + i\omega$ und $-\cfrac{1}{2}a - i\omega$
In diesem Fall ist $a^2 - 4b < 0$ und $\sqrt{-1} = i$, sodass aus Gleichung ($\ref{eqn:lambdas}$)

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

folgt. Definieren wir hier die reelle Zahl $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Mit dieser Definition von $\omega$ werden die Lösungen der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) zu den konjugiert komplexen Wurzeln $\lambda = -\cfrac{1}{2}a \pm i\omega$, und wir erhalten die entsprechenden zwei komplexen Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$)

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Allerdings können wir auch in diesem Fall eine Basis reeller Lösungen wie folgt erhalten.

Mit der Eulerschen Formel

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

und der daraus durch Einsetzen von $-t$ für $t$ erhaltenen Gleichung

$$ e^{-it} = \cos t - i\sin t $$

erhalten wir durch Addition und Subtraktion dieser beiden Gleichungen

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

Die komplexe Exponentialfunktion $e^z$ einer komplexen Variable $z = r + it$ mit Realteil $r$ und Imaginärteil $it$ kann unter Verwendung der reellen Funktionen $e^r$, $\cos t$ und $\sin t$ wie folgt definiert werden:

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + \sin t) \label{eqn:complex_exp}\tag{10}$$

Wenn wir hier $r=-\cfrac{1}{2}ax$ und $t=\omega x$ setzen, können wir schreiben:

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) sind auch die Summe und das konstante Vielfache dieser komplexen Lösungen Lösungen. Daher können wir die erste reelle Lösung $y_1$ erhalten, indem wir die beiden Gleichungen addieren und beide Seiten mit $\cfrac{1}{2}$ multiplizieren:

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Auf ähnliche Weise können wir die zweite reelle Lösung $y_2$ erhalten, indem wir die zweite Gleichung von der ersten subtrahieren und beide Seiten mit $\cfrac{1}{2i}$ multiplizieren:

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Da $\cfrac{y_1}{y_2} = \cot{\omega x}$ keine Konstante ist, sind $y_1$ und $y_2$ in jedem Intervall linear unabhängig und bilden daher eine Basis der reellen Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$). Daraus erhalten wir die allgemeine Lösung

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ sind beliebige Konstanten)} \label{eqn:general_sol_3}\tag{13}$$
