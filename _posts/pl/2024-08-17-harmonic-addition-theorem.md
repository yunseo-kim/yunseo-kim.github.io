---
title: Złożenie funkcji trygonometrycznych (Harmonic Addition Theorem)
description: Dla sumy funkcji trygonometrycznych postaci f(θ) = a cos θ + b sin θ pokazujemy, jak wyznaczyć równoważną pojedynczą funkcję r sin(θ+α) lub r cos(θ−β).
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Harmonic Addition Theorem]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Złożenie funkcji trygonometrycznych (Harmonic Addition Theorem)**
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \sin(\theta+\alpha) $$
>
> $$ (gdzie,\ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}) $$
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \cos(\theta-\beta) $$
>
> $$ (gdzie,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}) $$
{: .prompt-info }

## Wymagania wstępne
- [Wzory na dodawanie funkcji trygonometrycznych](/posts/trigonometric-addition-formulas)

## Złożenie funkcji trygonometrycznych (Harmonic Addition Theorem)
Dla funkcji $f(\theta)$ będącej sumą funkcji trygonometrycznych, np. $f(\theta) = a \cos \theta + b \sin \theta$, zawsze istnieją liczby rzeczywiste $\alpha$, $\beta$ spełniające
$f(\theta)=\sqrt{a^2+b^2} \sin(\theta+\alpha) = \sqrt{a^2+b^2} \cos(\theta-\beta)$.

![Geometric Derivation of the Harmonic Addition Theorem](/assets/img/trigonometry/harmonic-addition.png)

Jak na rysunku: wybierzmy na płaszczyźnie współrzędnych punkt $P(a,b)$ i niech $\alpha$ oznacza miarę kąta między odcinkiem $\overline{OP}$ a dodatnim zwrotem osi $x$.

$$ \overline{OP} = \sqrt{a^2+b^2} $$

oraz

$$ \cos \alpha = \frac{a}{\sqrt{a^{2} + b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2} + b^{2}}} \tag{1} $$

Wówczas

$$ \begin{align*}
a \sin \theta + b \cos \theta &= \sqrt{a^{2}+b^{2}} \left(\frac{a}{\sqrt{a^{2}+b^{2}}}\sin \theta + \frac{b}{\sqrt{a^{2}+b^{2}}}\cos \theta \right) \\
&= \sqrt{a^{2}+b^{2}}(\cos \alpha \sin \theta + \sin \alpha \cos \theta) \\
&= \sqrt{a^{2}+b^{2}} \sin(\theta + \alpha). \tag{2}
\end{align*} $$

Analogicznie, biorąc punkt $P^{\prime}(b,a)$ i oznaczając przez $\beta$ miarę kąta między odcinkiem $\overline{OP^{\prime}}$ a dodatnim zwrotem osi $x$, otrzymujemy:

$$ a \sin \theta + b \cos \theta = \sqrt{a^{2}+b^{2}}\cos(\theta-\beta). \tag{3} $$

$$ \text{gdzie }\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}. $$

Takie przekształcanie funkcji trygonometrycznej postaci $a \sin \theta + b \sin \theta$ do postaci $r\sin(\theta+\alpha)$ lub $r\cos(\theta-\beta)$ nazywa się złożeniem funkcji trygonometrycznych (Harmonic Addition).

## Przykład
Dla funkcji $f(\theta)=-\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right)$ wyznacz wartość największą i najmniejszą funkcji $f(\theta)$ na przedziale $[0, 2\pi]$.

### 1. Sprowadzenie do postaci $a\sin\theta + b\cos\theta$
Korzystając z [wzorów na dodawanie funkcji trygonometrycznych](/posts/trigonometric-addition-formulas), przekształcamy dane wyrażenie:

$$ \begin{align*}
f(\theta) &= -\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right) \\
&= -\sqrt{3}\sin \theta + \left( \cos\theta \cos\frac{\pi}{3} + \sin\theta \sin\frac{\pi}{3} \right) \\
&= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta .
\end{align*} $$

### 2. Sprowadzenie do postaci $r\sin(\theta+\alpha)$
Niech $a=-\frac{\sqrt{3}}{2}$, $b=\frac{1}{2}$. Wtedy

$$ r = \sqrt{a^2+b^2} = \sqrt{\frac{3}{4}+\frac{1}{4}} = 1 $$

Ponadto istnieje dokładnie jedna liczba rzeczywista $\alpha$ taka, że $0 \leq \alpha<2\pi$ oraz $\cos\alpha = a$, $\sin\alpha = b$. Z wartości funkcji trygonometrycznych dla kątów szczególnych wynika, że $\alpha = \frac{5}{6}\pi$. 

Zatem przekształcenie danej funkcji $f(\theta)$ do postaci $r\sin(\theta+\alpha)$ ma postać:

$$ f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right). $$

### 3. Wyznaczenie wartości największej i najmniejszej na danym przedziale
![Graph of the given function](/assets/img/trigonometry/harmonic-addition-ex-graph.png)

Funkcja $f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right)$ jest funkcją okresową o okresie $2\pi$, a na danym przedziale osiąga wartość największą $1$ oraz wartość najmniejszą $-1$.

$$ \therefore M=1,\ m=-1$$
