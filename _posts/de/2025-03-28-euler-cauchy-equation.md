---
title: "Die Euler-Cauchy-Gleichung"
description: "Untersuchung der allgemeinen Lösung der Euler-Cauchy-Gleichung basierend auf dem Vorzeichen der Diskriminante der charakteristischen Gleichung. Die drei Fälle werden behandelt."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Euler-Cauchy-Gleichung: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Charakteristische Gleichung**: $m^2 + (a-1)m + b = 0$
> - Je nach Vorzeichen der Diskriminante der charakteristischen Gleichung, $(1-a)^2 - 4b$, kann die Form der allgemeinen Lösung wie in der Tabelle in drei Fälle unterteilt werden:
>
> | Fall | Lösungen der charakteristischen Gleichung | Basis der Lösungen der Euler-Cauchy-Gleichung | Allgemeine Lösung der Euler-Cauchy-Gleichung |
> | :---: | :---: | :---: | :---: |
> | I | Zwei verschiedene reelle Wurzeln<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Reelle doppelte Wurzel<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Konjugiert komplexe Wurzeln<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Voraussetzungen
- [Homogene lineare DGL zweiter Ordnung](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Eulersche Formel

## Die charakteristische Gleichung
Die **Euler-Cauchy-Gleichung** ist eine gewöhnliche Differentialgleichung der Form

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

mit gegebenen Konstanten $a$ und $b$ und einer unbekannten Funktion $y(x)$. Setzt man

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

in die Gleichung ($\ref{eqn:euler_cauchy_eqn}$) ein, erhält man

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

also

$$ [m(m-1) + am + b]x^m = 0 $$

Daraus ergibt sich die charakteristische Gleichung

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

und die notwendige und hinreichende Bedingung dafür, dass $y=x^m$ eine Lösung der Euler-Cauchy-Gleichung ($\ref{eqn:euler_cauchy_eqn}$) ist, ist, dass $m$ eine Lösung der charakteristischen Gleichung ($\ref{eqn:auxiliary_eqn}$) ist.

Die Lösungen der quadratischen Gleichung ($\ref{eqn:auxiliary_eqn}$) sind

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

und daraus folgt, dass die beiden Funktionen

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

Lösungen der Gleichung ($\ref{eqn:euler_cauchy_eqn}$) sind.

Analog zum Fall der [homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/) können wir je nach Vorzeichen der Diskriminante $(1-a)^2 - 4b$ der charakteristischen Gleichung ($\ref{eqn:auxiliary_eqn}$) drei Fälle unterscheiden.
- $(1-a)^2 - 4b > 0$: Zwei verschiedene reelle Wurzeln
- $(1-a)^2 - 4b = 0$: Reelle doppelte Wurzel
- $(1-a)^2 - 4b < 0$: Konjugiert komplexe Wurzeln

## Form der allgemeinen Lösung je nach Vorzeichen der Diskriminante
### I. Zwei verschiedene reelle Wurzeln $m_1$ und $m_2$
In diesem Fall ist die Basis der Lösungen der Gleichung ($\ref{eqn:euler_cauchy_eqn}$) auf einem beliebigen Intervall

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

und die entsprechende allgemeine Lösung ist

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Reelle doppelte Wurzel $m = \cfrac{1-a}{2}$
Im Fall, dass $(1-a)^2 - 4b = 0$, also $b=\cfrac{(1-a)^2}{4}$, hat die quadratische Gleichung ($\ref{eqn:auxiliary_eqn}$) nur eine einzige Lösung $m = m_1 = m_2 = \cfrac{1-a}{2}$, und somit ist eine Lösung der Form $y = x^m$, die wir daraus erhalten,

$$ y_1 = x^{(1-a)/2} $$

und die Euler-Cauchy-Gleichung ($\ref{eqn:euler_cauchy_eqn}$) nimmt die Form

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

an. Nun finden wir eine weitere, linear unabhängige Lösung $y_2$ mit dem [Reduktionsverfahren](/posts/homogeneous-linear-odes-of-second-order/#reduktionsverfahren-reduction-of-order).

Wenn wir die gesuchte zweite Lösung als $y_2=uy_1$ ansetzen, erhalten wir

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Da $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$ ist,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

und durch Integration erhält man $u = \ln x$.

Daher ist $y_2 = uy_1 = y_1 \ln x$, und da ihr Quotient keine Konstante ist, sind $y_1$ und $y_2$ linear unabhängig. Die der Basis $y_1$ und $y_2$ entsprechende allgemeine Lösung ist

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Konjugiert komplexe Wurzeln
In diesem Fall sind die Lösungen der charakteristischen Gleichung ($\ref{eqn:auxiliary_eqn}$) $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, und die entsprechenden beiden komplexen Lösungen der Gleichung ($\ref{eqn:euler_cauchy_eqn}$) können unter Verwendung von $x=e^{\ln x}$ wie folgt geschrieben werden.

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Setzt man $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ und verwendet die Eulersche Formel $e^{it} = \cos{t} + i\sin{t}$, so sieht man, dass

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

und daraus erhält man die folgenden beiden reellen Lösungen

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Da ihr Quotient $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ keine Konstante ist, sind die beiden obigen Lösungen linear unabhängig und bilden daher nach dem [Superpositionsprinzip](/posts/homogeneous-linear-odes-of-second-order/#superpositionsprinzip) eine Basis für die Euler-Cauchy-Gleichung ($\ref{eqn:euler_cauchy_eqn}$). Daraus erhalten wir die folgende reelle allgemeine Lösung.

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Allerdings ist der Fall, dass die charakteristische Gleichung der Euler-Cauchy-Gleichung konjugiert komplexe Wurzeln hat, von geringerer praktischer Bedeutung.

## Transformation in eine homogene lineare GDGL mit konstanten Koeffizienten
Die Euler-Cauchy-Gleichung kann durch eine Variablensubstitution in eine [homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/) umgewandelt werden.

Durch die Substitution $x = e^t$ erhält man

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

wodurch die Euler-Cauchy-Gleichung ($\ref{eqn:euler_cauchy_eqn}$) in die folgende homogene lineare GDGL mit konstanten Koeffizienten bezüglich $t$ umgewandelt wird.

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

Löst man die Gleichung ($\ref{eqn:substituted}$) für $t$ mit der Methode für [homogene lineare DGL zweiter Ordnung mit konstanten Koeffizienten](/posts/homogeneous-linear-odes-with-constant-coefficients/) und transformiert die so erhaltene Lösung unter Verwendung von $t = \ln{x}$ zurück in eine Lösung für $x$, erhält man [die gleichen Ergebnisse wie zuvor](#form-der-allgemeinen-lösung-je-nach-vorzeichen-der-diskriminante).
