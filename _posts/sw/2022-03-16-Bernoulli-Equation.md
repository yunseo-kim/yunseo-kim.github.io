---
title: "Mlinganyo wa Bernoulli (Bernoulli Equation)"
description: "Jifunze mlinganyo wa Bernoulli na mbinu ya kutatua mlinganyo wa logistic, aina maalum ya mlinganyo huo."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Mlinganyo wa Bernoulli (Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ ni namba halisi yoyote)}  \tag{1} $$

Mlinganyo wa Bernoulli (1) huwa wa mstari ikiwa $a=0$ au $a=1$, na huwa usio wa mstari katika hali nyingine. Hata hivyo, unaweza kubadilishwa kuwa wa mstari kupitia mchakato ufuatao.

$$ u(x)=[y(x)]^{1-a} $$

Tukiweka hivyo, kisha tukitofautisha na kubadilisha $y'$ kutoka kwenye mlinganyo (1), tunapata

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

Kwa kuwa $y^{1-a}=u$ katika upande wa kulia, tunapata mlinganyo ufuatao wa tofauti wa kawaida wa mstari.

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Mfano: Mlinganyo wa Logistic (Logistic Equation)

Tatua mlinganyo wa logistic (aina maalum ya mlinganyo wa Bernoulli).

$$ y'=Ay-By^2 \tag{3} $$

### Suluhisho

Tukiandika mlinganyo (3) katika umbo la mlinganyo (1), tunapata

$$ y'-Ay=-By^2 $$

Hapa $a=2$, kwa hiyo $u=y^{1-a}=y^{-1}$. Tukitofautisha $u$ hii na kubadilisha $y'$ kutoka kwenye mlinganyo (3), tunapata

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

Kwa kuwa neno la mwisho ni $-Ay^{-1}=-Au$, tunapata mlinganyo ufuatao wa tofauti wa kawaida wa mstari.

$$ u'+Au=B $$

Kwa kutumia fomula ya suluhisho ya [mlinganyo wa tofauti wa kawaida wa mstari usio homojeni](/posts/Solution-of-First-Order-Linear-ODE/#mlinganyo-wa-tofauti-wa-kawaida-wa-mstari-usio-homojeni), tunaweza kupata suluhisho la jumla lifuatalo.

$$ u=ce^{-At}+B/A $$

Kwa kuwa $u=1/y$, kutokana na hili tunapata suluhisho la jumla la mlinganyo (3)

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$


