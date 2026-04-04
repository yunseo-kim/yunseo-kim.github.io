---
title: Uundaji wa Jumla ya Kazi za Trigonometria (Harmonic Addition Theorem)
description: Kwa jumla ya kazi za trigonometria ya umbo la f(θ) = a cos θ + b sin θ, tunaangalia jinsi ya kupata kazi moja inayolingana nayo, yaani r sin(θ+α) au r cos(θ-β).
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Harmonic Addition Theorem]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Kwa Ufupi
> **Uundaji wa Jumla ya Kazi za Trigonometria (Harmonic Addition Theorem)**
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \sin(\theta+\alpha) $$
>
> $$ (ambapo,\ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}) $$
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \cos(\theta-\beta) $$
>
> $$ (ambapo,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}) $$
{: .prompt-info }

## Mahitaji ya Awali
- [Kanuni za Kuongeza za Trigonometria](/posts/trigonometric-addition-formulas)

## Uundaji wa Jumla ya Kazi za Trigonometria (Harmonic Addition Theorem)
Kwa kazi $f(\theta)$ iliyo katika umbo la jumla ya kazi za trigonometria kama $f(\theta) = a \cos \theta + b \sin \theta$, daima zipo nambari halisi $\alpha$, $\beta$ zinazotosheleza $f(\theta)=\sqrt{a^2+b^2} \sin(\theta+\alpha) = \sqrt{a^2+b^2} \cos(\theta-\beta)$.

![Utoaji wa Kijiometri wa Harmonic Addition Theorem](/assets/img/trigonometry/harmonic-addition.png)

Kama kwenye mchoro, tukichukua nukta $P(a,b)$ kwenye ndege ya uratibu, na tukisema ukubwa wa pembe inayoundwa na kipande cha mstari $\overline{OP}$ na mwelekeo chanya wa mhimili wa $x$ ni $\alpha$, basi

$$ \overline{OP} = \sqrt{a^2+b^2} $$

na

$$ \cos \alpha = \frac{a}{\sqrt{a^{2} + b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2} + b^{2}}} \tag{1} $$

ni kweli. Wakati huu,

$$ \begin{align*}
a \sin \theta + b \cos \theta &= \sqrt{a^{2}+b^{2}} \left(\frac{a}{\sqrt{a^{2}+b^{2}}}\sin \theta + \frac{b}{\sqrt{a^{2}+b^{2}}}\cos \theta \right) \\
&= \sqrt{a^{2}+b^{2}}(\cos \alpha \sin \theta + \sin \alpha \cos \theta) \\
&= \sqrt{a^{2}+b^{2}} \sin(\theta + \alpha). \tag{2}
\end{align*} $$

Kwa njia hiyo hiyo, tukichukua nukta $P^{\prime}(b,a)$ na tukisema ukubwa wa pembe inayoundwa na kipande cha mstari $\overline{OP^{\prime}}$ na mwelekeo chanya wa mhimili wa $x$ ni $\beta$, tunapata yafuatayo.

$$ a \sin \theta + b \cos \theta = \sqrt{a^{2}+b^{2}}\cos(\theta-\beta). \tag{3} $$

$$ Ambapo,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}. $$

Kwa namna hii, kubadilisha kazi ya trigonometria ya umbo la $a \sin \theta + b \sin \theta$ kuwa katika umbo la $r\sin(\theta+\alpha)$ au $r\cos(\theta-\beta)$ kunaitwa uundaji wa jumla ya kazi za trigonometria (Harmonic Addition).

## Mfano
Ikiwa kazi ni $f(\theta)=-\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right)$, tafuta thamani kubwa zaidi na thamani ndogo zaidi ya kazi $f(\theta)$ katika sehemu $[0, 2\pi]$.

### 1. Badilisha iwe katika umbo la $a\sin\theta + b\cos\theta$
Kwa kutumia [Kanuni za Kuongeza za Trigonometria](/posts/trigonometric-addition-formulas), tunaweza kubadilisha fomyula ya kazi tuliyopewa kama ifuatavyo:

$$ \begin{align*}
f(\theta) &= -\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right) \\
&= -\sqrt{3}\sin \theta + \left( \cos\theta \cos\frac{\pi}{3} + \sin\theta \sin\frac{\pi}{3} \right) \\
&= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta .
\end{align*} $$

### 2. Badilisha iwe katika umbo la $r\sin(\theta+\alpha)$
Tukiweka $a=-\frac{\sqrt{3}}{2}$, $b=\frac{1}{2}$, basi

$$ r = \sqrt{a^2+b^2} = \sqrt{\frac{3}{4}+\frac{1}{4}} = 1 $$

ndivyo ilivyo.

Pia, ipo thamani moja ya nambari halisi $\alpha$ inayotosheleza $0 \leq \alpha<2\pi$, $\cos\alpha = a$, na $\sin\alpha = b$. Kutokana na thamani za uwiano wa trigonometria kwa pembe maalumu, tunaweza kujua kuwa $\alpha = \frac{5}{6}\pi$. 

Kwa hiyo, tukibadilisha kazi tuliyopewa $f(\theta)$ kuwa katika umbo la $r\sin(\theta+\alpha)$, tunapata yafuatayo.

$$ f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right). $$

### 3. Tafuta thamani kubwa zaidi na ndogo zaidi katika sehemu iliyotolewa
![Grafu ya kazi iliyopewa](/assets/img/trigonometry/harmonic-addition-ex-graph.png)

Kazi $f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right)$ ni kazi ya kipindi yenye kipindi cha $2\pi$, na katika sehemu iliyotolewa ina thamani kubwa zaidi $1$ na thamani ndogo zaidi $-1$.

$$ \therefore M=1,\ m=-1$$
