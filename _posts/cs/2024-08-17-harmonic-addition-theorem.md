---
title: Skládání goniometrických funkcí (Harmonic Addition Theorem)
description: Pro součet goniometrických funkcí tvaru f(θ) = a cos θ + b sin θ ukážeme, jak jej převést na jedinou funkci r sin(θ+α) nebo r cos(θ−β).
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Harmonic Addition Theorem]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Skládání goniometrických funkcí (Harmonic Addition Theorem)**
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \sin(\theta+\alpha) $$
>
> $$ (kde\ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}) $$
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \cos(\theta-\beta) $$
>
> $$ (kde\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}) $$
{: .prompt-info }

## Prerequisites
- [Sčítací vzorce goniometrických funkcí](/posts/trigonometric-addition-formulas)

## Skládání goniometrických funkcí (Harmonic Addition Theorem)
Pro funkci $f(\theta)$, která má tvar součtu goniometrických funkcí jako $f(\theta) = a \cos \theta + b \sin \theta$, vždy existují reálná čísla $\alpha$, $\beta$ taková, že platí
$f(\theta)=\sqrt{a^2+b^2} \sin(\theta+\alpha) = \sqrt{a^2+b^2} \cos(\theta-\beta)$.

![Geometric Derivation of the Harmonic Addition Theorem](/assets/img/trigonometry/harmonic-addition.png)

Jak je na obrázku, vezměme na souřadnicové rovině bod $P(a,b)$ a označme $\alpha$ velikost úhlu, který svírá úsečka $\overline{OP}$ s kladným směrem osy $x$.

$$ \overline{OP} = \sqrt{a^2+b^2} $$

a

$$ \cos \alpha = \frac{a}{\sqrt{a^{2} + b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2} + b^{2}}} \tag{1} $$

Potom

$$ \begin{align*}
a \sin \theta + b \cos \theta &= \sqrt{a^{2}+b^{2}} \left(\frac{a}{\sqrt{a^{2}+b^{2}}}\sin \theta + \frac{b}{\sqrt{a^{2}+b^{2}}}\cos \theta \right) \\
&= \sqrt{a^{2}+b^{2}}(\cos \alpha \sin \theta + \sin \alpha \cos \theta) \\
&= \sqrt{a^{2}+b^{2}} \sin(\theta + \alpha). \tag{2}
\end{align*} $$

Stejným způsobem vezměme bod $P^{\prime}(b,a)$ a označme $\beta$ velikost úhlu, který svírá úsečka $\overline{OP^{\prime}}$ s kladným směrem osy $x$. Dostaneme

$$ a \sin \theta + b \cos \theta = \sqrt{a^{2}+b^{2}}\cos(\theta-\beta). \tag{3} $$

$$ kde,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}. $$

Tímto způsobem se převod goniometrické funkce tvaru $a \sin \theta + b \sin \theta$ na tvar $r\sin(\theta+\alpha)$ nebo $r\cos(\theta-\beta)$ nazývá skládání goniometrických funkcí (Harmonic Addition).

## Příklad
Je dána funkce $f(\theta)=-\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right)$. Určete na intervalu $[0, 2\pi]$ její maximum a minimum.

### 1. Převod na tvar $a\sin\theta + b\cos\theta$
Pomocí [sčítacích vzorců goniometrických funkcí](/posts/trigonometric-addition-formulas) upravíme daný výraz:

$$ \begin{align*}
f(\theta) &= -\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right) \\
&= -\sqrt{3}\sin \theta + \left( \cos\theta \cos\frac{\pi}{3} + \sin\theta \sin\frac{\pi}{3} \right) \\
&= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta .
\end{align*} $$

### 2. Převod na tvar $r\sin(\theta+\alpha)$
Položíme-li $a=-\frac{\sqrt{3}}{2}$, $b=\frac{1}{2}$, pak

$$ r = \sqrt{a^2+b^2} = \sqrt{\frac{3}{4}+\frac{1}{4}} = 1 $$

Dále: pro $0 \leq \alpha<2\pi$ existuje právě jedna reálná hodnota $\alpha$ taková, že $\cos\alpha = a$ a $\sin\alpha = b$. Z hodnot goniometrických funkcí pro speciální úhly plyne, že $\alpha = \frac{5}{6}\pi$.

Proto po převedení dané funkce $f(\theta)$ do tvaru $r\sin(\theta+\alpha)$ dostaneme:

$$ f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right). $$

### 3. Určení maxima a minima na daném intervalu
![Graph of the given function](/assets/img/trigonometry/harmonic-addition-ex-graph.png)

Funkce $f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right)$ je periodická s periodou $2\pi$ a na daném intervalu nabývá maxima $1$ a minima $-1$.

$$ \therefore M=1,\ m=-1$$
