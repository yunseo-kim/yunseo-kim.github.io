---
title: Euler-Cauchy-Gleichung
description: Wir untersuchen, wie die allgemeine Lösung der Euler-Cauchy-Gleichung je nach Vorzeichen der Diskriminante der charakteristischen Gleichung verschiedene Formen annimmt.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Euler-Cauchy-Gleichung: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Hilfsgleichung (auxiliary equation)**: $m^2 + (a-1)m + b = 0$
> - Je nach Vorzeichen der Diskriminante der Hilfsgleichung $(1-a)^2 - 4b$ kann die allgemeine Lösung in drei Fälle unterteilt werden, wie in der Tabelle dargestellt
>
> | Fall | Lösungen der Hilfsgleichung | Basis der Lösungen der Euler-Cauchy-Gleichung | Allgemeine Lösung der Euler-Cauchy-Gleichung |
> | :---: | :---: | :---: | :---: |
> | I | Verschiedene reelle Wurzeln<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Reelle doppelte Wurzel<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Konjugiert komplexe Wurzeln<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Voraussetzungen
- [Homogene lineare gewöhnliche Differentialgleichungen zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogene lineare gewöhnliche Differentialgleichungen mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Eulersche Formel

## Hilfsgleichung (auxiliary equation)
Die **Euler-Cauchy-Gleichung** ist eine Differentialgleichung der Form

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

mit den Konstanten $a$ und $b$ und der unbekannten Funktion $y(x)$. Wenn wir in Gleichung ($\ref{eqn:euler_cauchy_eqn}$)

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

einsetzen, erhalten wir

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

also

$$ [m(m-1) + am + b]x^m = 0 $$

Daraus ergibt sich die Hilfsgleichung

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

und die notwendige und hinreichende Bedingung dafür, dass $y=x^m$ eine Lösung der Euler-Cauchy-Gleichung ($\ref{eqn:euler_cauchy_eqn}$) ist, besteht darin, dass $m$ eine Lösung der Hilfsgleichung ($\ref{eqn:auxiliary_eqn}$) ist.

Die Lösungen der quadratischen Gleichung ($\ref{eqn:auxiliary_eqn}$) sind

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

und daraus folgt, dass die beiden Funktionen

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

Lösungen der Gleichung ($\ref{eqn:euler_cauchy_eqn}$) sind.

Wie bei [homogenen linearen gewöhnlichen Differentialgleichungen mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/) können wir je nach Vorzeichen der Diskriminante $(1-a)^2 - 4b$ der Hilfsgleichung ($\ref{eqn:auxiliary_eqn}$) drei Fälle unterscheiden:
- $(1-a)^2 - 4b > 0$: Zwei verschiedene reelle Wurzeln
- $(1-a)^2 - 4b = 0$: Eine reelle Doppelwurzel
- $(1-a)^2 - 4b < 0$: Konjugiert komplexe Wurzeln

## Form der allgemeinen Lösung je nach Vorzeichen der Diskriminante der Hilfsgleichung
### I. Zwei verschiedene reelle Wurzeln $m_1$ und $m_2$
In diesem Fall bilden

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

eine Basis der Lösungen der Gleichung ($\ref{eqn:euler_cauchy_eqn}$) in jedem Intervall, und die allgemeine Lösung lautet

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Reelle Doppelwurzel $m = \cfrac{1-a}{2}$
Wenn $(1-a)^2 - 4b = 0$, also $b=\cfrac{(1-a)^2}{4}$, hat die quadratische Gleichung ($\ref{eqn:auxiliary_eqn}$) nur eine Lösung $m = m_1 = m_2 = \cfrac{1-a}{2}$, und daraus ergibt sich eine Lösung der Form $y = x^m$:

$$ y_1 = x^{(1-a)/2} $$

Die Euler-Cauchy-Gleichung ($\ref{eqn:euler_cauchy_eqn}$) nimmt dann die Form

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

an. Wir suchen nun eine zweite linear unabhängige Lösung $y_2$ mit Hilfe der [Methode der Ordnungsreduktion](/posts/homogeneous-linear-odes-of-second-order/#ordnungsreduktion).

Wir setzen $y_2=uy_1$ und erhalten

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Da $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$, haben wir

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

und durch Integration erhalten wir $u = \ln x$.

Somit ist $y_2 = uy_1 = y_1 \ln x$, und $y_1$ und $y_2$ sind linear unabhängig, da ihr Quotient keine Konstante ist. Die allgemeine Lösung mit der Basis $y_1$ und $y_2$ lautet

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Konjugiert komplexe Wurzeln
In diesem Fall sind die Lösungen der Hilfsgleichung ($\ref{eqn:auxiliary_eqn}$) $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, und die entsprechenden komplexen Lösungen der Gleichung ($\ref{eqn:euler_cauchy_eqn}$) können mit Hilfe von $x=e^{\ln x}$ wie folgt geschrieben werden:

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Mit $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ und der Eulerschen Formel $e^{it} = \cos{t} + i\sin{t}$ erhalten wir

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

Daraus ergeben sich die beiden reellen Lösungen

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Da ihr Quotient $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ keine Konstante ist, sind diese beiden Lösungen linear unabhängig und bilden daher nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) eine Basis der Lösungen der Euler-Cauchy-Gleichung ($\ref{eqn:euler_cauchy_eqn}$). Daraus ergibt sich die allgemeine reelle Lösung:

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Allerdings ist der Fall, in dem die Hilfsgleichung der Euler-Cauchy-Gleichung konjugiert komplexe Wurzeln hat, von geringerer praktischer Bedeutung.
