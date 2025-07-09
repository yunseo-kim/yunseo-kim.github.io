---
title: "Homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten"
description: "Wir untersuchen die Form der allgemeinen Lösung einer homogenen linearen DGL mit konstanten Koeffizienten, abhängig vom Vorzeichen der Diskriminante der charakteristischen Gleichung."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Charakteristische Gleichung**: $\lambda^2 + a\lambda + b = 0$
> - Je nach Vorzeichen der Diskriminante $a^2 - 4b$ der charakteristischen Gleichung kann die Form der allgemeinen Lösung in drei Fälle unterteilt werden, wie in der Tabelle gezeigt:
>
> | Fall | Lösungen der charakteristischen Gleichung | Basis der Lösungen der DGL | Allgemeine Lösung der DGL |
> | :---: | :---: | :---: | :---: |
> | I | Zwei verschiedene reelle Wurzeln<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Reelle doppelte Wurzel<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Konjugiert komplexe Wurzeln<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Voraussetzungen
- [Bernoulli-Gleichung](/posts/Bernoulli-Equation/)
- [Homogene lineare DGL zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- Euler'sche Formel

## Charakteristische Gleichung
Betrachten wir eine homogene lineare Differentialgleichung zweiter Ordnung mit konstanten Koeffizienten $a$ und $b$:

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Diese Art von Gleichung hat wichtige Anwendungen bei mechanischen und elektrischen Schwingungen.

Im Beitrag zur [Bernoulli-Gleichung](/posts/Bernoulli-Equation/) haben wir bereits die allgemeine Lösung der logistischen Gleichung hergeleitet. Demnach ist die Lösung der linearen DGL erster Ordnung mit konstantem Koeffizienten $k$

$$ y^\prime + ky = 0 $$

die Exponentialfunktion $y = ce^{-kx}$ (für den Fall $A=-k$, $B=0$ in Gleichung (4) des entsprechenden Beitrags).

Daher können wir für die ähnlich geformte Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) zunächst einen Lösungsansatz der Form

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

versuchen.

> Natürlich ist dies nur eine Vermutung, und es gibt keine Garantie, dass die allgemeine Lösung tatsächlich diese Form hat. Aber wenn wir erst einmal zwei linear unabhängige Lösungen gefunden haben, können wir, wie im Beitrag über [homogene lineare DGL zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/#basis-und-allgemeine-lösung) gezeigt, die allgemeine Lösung mithilfe des [Superpositionsprinzips](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) finden.  
> Wie wir gleich sehen werden, gibt es auch Fälle, in denen wir eine [Lösung anderer Form finden müssen](#ii-reelle-doppelte-wurzel-lambda--cfraca2).
{: .prompt-info }

Setzen wir Gleichung ($\ref{eqn:general_sol}$) und ihre Ableitungen

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

in Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) ein, erhalten wir

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Wenn $\lambda$ also eine Lösung der **charakteristischen Gleichung**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

ist, dann ist die Exponentialfunktion ($\ref{eqn:general_sol}$) eine Lösung der Differentialgleichung ($\ref{eqn:ode_with_constant_coefficients}$). Die Lösungen der quadratischen Gleichung ($\ref{eqn:characteristic_eqn}$) sind

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

und daraus ergeben sich die beiden Funktionen

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

als Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$).

> Die Begriffe **charakteristische Gleichung** und **Hilfsgleichung (auxiliary equation)** werden oft synonym verwendet; sie bedeuten genau dasselbe. Man kann beide Begriffe verwenden.
{: .prompt-tip }

Nun können wir je nach Vorzeichen der Diskriminante $a^2 - 4b$ der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) drei Fälle unterscheiden:
- $a^2 - 4b > 0$: Zwei verschiedene reelle Wurzeln
- $a^2 - 4b = 0$: Reelle doppelte Wurzel
- $a^2 - 4b < 0$: Konjugiert komplexe Wurzeln

## Form der allgemeinen Lösung je nach Vorzeichen der Diskriminante der charakteristischen Gleichung
### I. Zwei verschiedene reelle Wurzeln $\lambda_1$ und $\lambda_2$
In diesem Fall ist die Basis der Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) auf einem beliebigen Intervall

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

und die entsprechende allgemeine Lösung ist

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Reelle doppelte Wurzel $\lambda = -\cfrac{a}{2}$
Im Fall $a^2 - 4b = 0$ hat die quadratische Gleichung ($\ref{eqn:characteristic_eqn}$) nur eine einzige Lösung $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$. Daher gibt es nur eine Lösung der Form $y = e^{\lambda x}$, die wir daraus erhalten können, nämlich

$$ y_1 = e^{-(a/2)x} $$

Um eine Basis zu erhalten, müssen wir eine zweite, von $y_1$ linear unabhängige Lösung $y_2$ finden.

Hierfür können wir das bereits besprochene [Reduktionsverfahren](/posts/homogeneous-linear-odes-of-second-order/#reduktionsverfahren-reduction-of-order) anwenden. Wir setzen die gesuchte zweite Lösung als $y_2=uy_1$ an und setzen

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

in die Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) ein, was zu

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

führt. Wenn wir die Terme nach $u^{\prime\prime}$, $u^\prime$ und $u$ gruppieren und ordnen, erhalten wir

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Da $y_1$ eine Lösung der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) ist, ist der Ausdruck in der letzten Klammer gleich $0$. Da

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

ist, ist auch der Ausdruck in der ersten Klammer gleich $0$. Somit bleibt nur $u^{\prime\prime}y_1 = 0$ übrig, woraus $u^{\prime\prime}=0$ folgt. Zweimalige Integration ergibt $u = c_1x + c_2$. Da die Integrationskonstanten $c_1$ und $c_2$ beliebige Werte annehmen können, können wir einfach $c_1=1$ und $c_2=0$ wählen, was zu $u=x$ führt. Dann ist $y_2 = uy_1 = xy_1$, und da $y_1$ und $y_2$ linear unabhängig sind, bilden sie eine Basis. Daher ist im Fall einer doppelten Wurzel der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) die Basis der Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$) auf einem beliebigen Intervall

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

und die entsprechende allgemeine Lösung ist

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Konjugiert komplexe Wurzeln $-\cfrac{1}{2}a + i\omega$ und $-\cfrac{1}{2}a - i\omega$
In diesem Fall ist $a^2 - 4b < 0$ und mit $\sqrt{-1} = i$ ergibt sich aus Gleichung ($\ref{eqn:lambdas}$)

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

Hier definieren wir die reelle Zahl $\omega = \sqrt{b-\cfrac{1}{4}a^2}$.

Wenn wir $\omega$ wie oben definieren, sind die Lösungen der charakteristischen Gleichung ($\ref{eqn:characteristic_eqn}$) die konjugiert komplexen Wurzeln $\lambda = -\cfrac{1}{2}a \pm i\omega$, und wir erhalten die entsprechenden zwei komplexen Lösungen der Gleichung ($\ref{eqn:ode_with_constant_coefficients}$)

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Auch in diesem Fall können wir jedoch eine Basis aus reellen (nicht-imaginären) Lösungen wie folgt erhalten.

Aus der Euler'schen Formel

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

und der durch Einsetzen von $-t$ für $t$ gewonnenen Gleichung

$$ e^{-it} = \cos t - i\sin t $$

erhalten wir durch Addition und Subtraktion der beiden Gleichungen:

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

Die komplexe Exponentialfunktion $e^z$ einer komplexen Variablen $z = r + it$ mit Realteil $r$ und Imaginärteil $it$ kann mit den reellen Funktionen $e^r$, $\cos t$ und $\sin t$ wie folgt definiert werden:

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Wenn wir hier $r=-\cfrac{1}{2}ax$ und $t=\omega x$ setzen, können wir schreiben:

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) sind auch die Summe und skalare Vielfache dieser komplexen Lösungen wieder Lösungen. Indem wir die beiden Gleichungen addieren und beide Seiten mit $\cfrac{1}{2}$ multiplizieren, erhalten wir die erste reelle Lösung $y_1$ wie folgt:

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Auf die gleiche Weise können wir die zweite reelle Lösung $y_2$ erhalten, indem wir die zweite Gleichung von der ersten subtrahieren und beide Seiten mit $\cfrac{1}{2i}$ multiplizieren.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Da $\cfrac{y_1}{y_2} = \cot{\omega x}$ keine Konstante ist, sind $y_1$ und $y_2$ auf jedem Intervall linear unabhängig und bilden somit eine Basis aus reellen Lösungen für die Gleichung ($\ref{eqn:ode_with_constant_coefficients}$). Daraus erhalten wir die allgemeine Lösung

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ sind beliebige Konstanten)} \label{eqn:general_sol_3}\tag{13}$$


