---
title: "Harmonische Addition (Harmonic Addition Theorem)"
description: >-
  Wir untersuchen die Methode zur Bestimmung einer einzelnen trigonometrischen Funktion r sin(θ+α) oder r cos(θ-β), die einer Summe von trigonometrischen Funktionen der Form f(θ) = a cos θ + b sin θ entspricht.
categories: [Mathematics]
tags: [Trigonometrie]
math: true
---

## TL;DR
> **Harmonische Addition (Harmonic Addition Theorem)**
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \sin(\theta+\alpha) $$
>
> $$ (wobei\ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}) $$
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \cos(\theta-\beta) $$
>
> $$ (wobei\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}) $$
{: .prompt-info }

## Voraussetzungen
- [Additionstheoreme der Trigonometrie](/posts/trigonometric-addition-formulas)

## Harmonische Addition (Harmonic Addition Theorem)
Für eine Funktion f(θ) = a cos θ + b sin θ, die als Summe trigonometrischer Funktionen dargestellt ist, existieren immer reelle Zahlen α und β, die f(θ)=√(a²+b²) sin(θ+α) = √(a²+b²) cos(θ-β) erfüllen.

![Geometrische Herleitung des Harmonic Addition Theorems](/assets/img/trigonometry/harmonic-addition.png)

Wie in der Abbildung gezeigt, wählen wir den Punkt P(a,b) in der Koordinatenebene und bezeichnen den Winkel zwischen der Strecke OP und der positiven x-Achse als α. Dann gilt:

$$ \overline{OP} = \sqrt{a^2+b^2} $$

und

$$ \cos \alpha = \frac{a}{\sqrt{a^{2} + b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2} + b^{2}}} \tag{1} $$

In diesem Fall:

$$ \begin{align*}
a \sin \theta + b \cos \theta &= \sqrt{a^{2}+b^{2}} \left(\frac{a}{\sqrt{a^{2}+b^{2}}}\sin \theta + \frac{b}{\sqrt{a^{2}+b^{2}}}\cos \theta \right) \\
&= \sqrt{a^{2}+b^{2}}(\cos \alpha \sin \theta + \sin \alpha \cos \theta) \\
&= \sqrt{a^{2}+b^{2}} \sin(\theta + \alpha). \tag{2}
\end{align*} $$

Auf die gleiche Weise wählen wir den Punkt P'(b,a) und bezeichnen den Winkel zwischen der Strecke OP' und der positiven x-Achse als β. Dann erhalten wir:

$$ a \sin \theta + b \cos \theta = \sqrt{a^{2}+b^{2}}\cos(\theta-\beta). \tag{3} $$

$$ wobei\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}. $$

Diese Umformung einer trigonometrischen Funktion der Form a sin θ + b sin θ in die Form r sin(θ+α) oder r cos(θ-β) wird als harmonische Addition (Harmonic Addition) bezeichnet.

## Beispiel
Sei f(θ)=-√3 sin θ + cos(θ - π/3). Bestimmen Sie den Maximal- und Minimalwert der Funktion f(θ) im Intervall [0, 2π].

### 1. Umformung in die Form a sin θ + b cos θ
Unter Verwendung der [Additionstheoreme der Trigonometrie](/posts/trigonometric-addition-formulas) können wir die gegebene Funktion umformen:

$$ \begin{align*}
f(\theta) &= -\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right) \\
&= -\sqrt{3}\sin \theta + \left( \cos\theta \cos\frac{\pi}{3} + \sin\theta \sin\frac{\pi}{3} \right) \\
&= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta .
\end{align*} $$

### 2. Umformung in die Form r sin(θ+α)
Setzen wir a=-√3/2 und b=1/2, dann gilt:

$$ r = \sqrt{a^2+b^2} = \sqrt{\frac{3}{4}+\frac{1}{4}} = 1 $$

Außerdem existiert genau ein reeller Wert α mit 0 ≤ α < 2π, für den cos α = a und sin α = b gilt. Aus den trigonometrischen Werten für spezielle Winkel können wir schließen, dass α = 5π/6 ist.

Daher kann die gegebene Funktion f(θ) in die Form r sin(θ+α) umgeformt werden als:

$$ f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right). $$

### 3. Bestimmung des Maximal- und Minimalwerts im gegebenen Intervall
![Graph der gegebenen Funktion](/assets/img/trigonometry/harmonic-addition-ex-graph.png)

Die Funktion f(θ) = sin(θ + 5π/6) ist eine periodische Funktion mit der Periode 2π und hat im gegebenen Intervall den Maximalwert 1 und den Minimalwert -1.

$$ \therefore M=1,\ m=-1$$