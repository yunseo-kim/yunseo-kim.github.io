---
title: Lineare homogene Differentialgleichungen zweiter Ordnung mit konstanten Koeffizienten
description: Wir untersuchen, wie die allgemeine Lösung einer homogenen linearen Differentialgleichung zweiter Ordnung mit konstanten Koeffizienten je nach Vorzeichen der Diskriminante der charakteristischen Gleichung aussieht.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Homogene lineare Differentialgleichung zweiter Ordnung mit konstanten Koeffizienten: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Charakteristische Gleichung**: $\lambda^2 + a\lambda + b = 0$
> - Je nach Vorzeichen der Diskriminante $a^2 - 4b$ der charakteristischen Gleichung kann die allgemeine Lösung in drei Fälle eingeteilt werden, wie in der Tabelle dargestellt
>
> | Fall | Lösungen der charakteristischen Gleichung | Basis der Lösungen | Allgemeine Lösung |
> | :---: | :---: | :---: | :---: |
> | I | Verschiedene reelle Wurzeln<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Reelle Doppelwurzel<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Konjugiert komplexe Wurzeln<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Voraussetzungen
- [Bernoulli-Gleichung](/posts/Bernoulli-Equation/)
- [Homogene lineare Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- Eulersche Formel

## Charakteristische Gleichung
Betrachten wir eine homogene lineare Differentialgleichung zweiter Ordnung mit konstanten Koeffizienten $a$ und $b$:

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Diese Art von Gleichung findet wichtige Anwendungen bei mechanischen und elektrischen Schwingungen.

Wie wir bereits bei der [Bernoulli-Gleichung](/posts/Bernoulli-Equation/) gesehen haben, ist die Lösung einer linearen Differentialgleichung erster Ordnung mit konstantem Koeffizienten $k$:

$$ y^\prime + ky = 0 $$

die Exponentialfunktion $y = ce^{-kx}$. (Dies entspricht dem Fall $A=-k$, $B=0$ in Gleichung (4) des verlinkten Beitrags)

Daher können wir für die ähnlich strukturierte Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) zunächst einen Lösungsansatz der Form

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

versuchen.

> Dies ist natürlich nur eine Vermutung, und es gibt keine Garantie, dass die allgemeine Lösung tatsächlich diese Form hat. Aber wenn wir zwei linear unabhängige Lösungen finden können, können wir nach dem [Superpositionsprinzips](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip), wie wir bei [homogenen linearen Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/#basis-und-allgemeine-lösung) gesehen haben, die allgemeine Lösung konstruieren.  
> Wie wir später sehen werden, gibt es [Fälle, in denen wir andere Lösungsformen finden müssen](#ii-reelle-doppelwurzel-lambda---cfraca2).
{: .prompt-info }

Wenn wir den Ansatz ($\ref{eqn:general_sol}$) und seine Ableitungen

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

in Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) einsetzen, erhalten wir:

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Daraus folgt, dass die Exponentialfunktion ($\ref{eqn:general_sol}$) eine Lösung der Differentialgleichung ($\ref{eqn:ode_with_constant_coefficients}$) ist, wenn $\lambda$ eine Lösung der **charakteristischen Gleichung**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

ist. Die Lösungen dieser quadratischen Gleichung ($\ref{eqn:characteristic_eqn}$) sind:

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

Damit sind die beiden Funktionen

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$).

> Die Begriffe **charakteristische Gleichung** und **Hilfsgleichung** werden oft synonym verwendet und bedeuten dasselbe. Beide Bezeichnungen sind korrekt.
{: .prompt-tip }

Je nach Vorzeichen der Diskriminante $a^2 - 4b$ der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) können wir drei Fälle unterscheiden:
- $a^2 - 4b > 0$: Zwei verschiedene reelle Wurzeln
- $a^2 - 4b = 0$: Eine reelle Doppelwurzel
- $a^2 - 4b < 0$: Konjugiert komplexe Wurzeln

## Allgemeine Lösungsformen je nach Diskriminante
### I. Verschiedene reelle Wurzeln $\lambda_1$ und $\lambda_2$
In diesem Fall bilden die Funktionen

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

eine Basis der Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) in jedem Intervall, und die allgemeine Lösung lautet:

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Reelle Doppelwurzel $\lambda = -\cfrac{a}{2}$
Wenn $a^2 - 4b = 0$, hat die quadratische Gleichung ($\ref{eqn:characteristic_eqn}$) nur eine Lösung $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, und wir erhalten nur eine Lösung der Form $y = e^{\lambda x}$:

$$ y_1 = e^{-(a/2)x} $$

Um eine Basis zu erhalten, müssen wir eine zweite, von $y_1$ linear unabhängige Lösung $y_2$ finden.

In dieser Situation können wir die Methode der [Ordnungsreduktion](/posts/homogeneous-linear-odes-of-second-order/#ordnungsreduktion) anwenden. Wir setzen $y_2=uy_1$ und berechnen:

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Wenn wir diese Ausdrücke in Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) einsetzen, erhalten wir:

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Nach Umordnung der Terme mit $u^{\prime\prime}$, $u^\prime$ und $u$ ergibt sich:

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Da $y_1$ eine Lösung der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) ist, ist der Ausdruck in der letzten Klammer gleich 0. Außerdem gilt:

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

Somit ist auch der Ausdruck in der ersten Klammer gleich 0. Es bleibt nur $u^{\prime\prime}y_1 = 0$, woraus $u^{\prime\prime}=0$ folgt. Durch zweimalige Integration erhalten wir $u = c_1x + c_2$. Da die Integrationskonstanten $c_1$ und $c_2$ beliebig sein können, können wir einfach $c_1=1$ und $c_2=0$ wählen, also $u=x$. Damit wird $y_2 = uy_1 = xy_1$, und $y_1$ und $y_2$ sind linear unabhängig und bilden eine Basis. Die Basis der Lösungen für den Fall einer Doppelwurzel ist also:

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

und die entsprechende allgemeine Lösung lautet:

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Konjugiert komplexe Wurzeln $-\cfrac{1}{2}a + i\omega$ und $-\cfrac{1}{2}a - i\omega$
In diesem Fall ist $a^2 - 4b < 0$ und mit $\sqrt{-1} = i$ können wir aus Gleichung ($\ref{eqn:lambdas}$) ableiten:

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

Definieren wir die reelle Zahl $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Mit dieser Definition von $\omega$ sind die Lösungen der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) die konjugiert komplexen Wurzeln $\lambda = -\cfrac{1}{2}a \pm i\omega$, und die entsprechenden komplexen Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) sind:

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Wir können jedoch auch reelle Basislösungen erhalten.

Mit der Eulerschen Formel

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

und der daraus abgeleiteten Gleichung für $-t$:

$$ e^{-it} = \cos t - i\sin t $$

erhalten wir durch Addition und Subtraktion:

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

Die komplexe Exponentialfunktion $e^z$ für eine komplexe Variable $z = r + it$ mit Realteil $r$ und Imaginärteil $it$ kann mit den reellen Funktionen $e^r$, $\cos t$ und $\sin t$ wie folgt definiert werden:

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Wenn wir $r=-\cfrac{1}{2}ax$ und $t=\omega x$ setzen, können wir schreiben:

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) sind auch Linearkombinationen dieser komplexen Lösungen wieder Lösungen. Durch Addition der beiden Gleichungen und Multiplikation mit $\cfrac{1}{2}$ erhalten wir die erste reelle Lösung $y_1$:

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Auf ähnliche Weise erhalten wir durch Subtraktion der zweiten Gleichung von der ersten und Multiplikation mit $\cfrac{1}{2i}$ die zweite reelle Lösung $y_2$:

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Da $\cfrac{y_1}{y_2} = \cot{\omega x}$ keine Konstante ist, sind $y_1$ und $y_2$ in jedem Intervall linear unabhängig und bilden somit eine Basis der reellen Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$). Die allgemeine Lösung lautet daher:

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(wobei }A,\, B\text{ beliebige Konstanten sind)} \label{eqn:general_sol_3}\tag{13}$$
