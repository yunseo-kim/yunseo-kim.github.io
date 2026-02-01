---
title: "Bernoulliho rovnice (Bernoulli Equation)"
description: "Probereme Bernoulliho rovnici a postup řešení její speciální formy – logistické rovnice."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Bernoulliho rovnice (Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ je libovolné reálné číslo)}  \tag{1} $$

Bernoulliho rovnice (1) je lineární pro $a=0$ nebo $a=1$ a v ostatních případech je nelineární. Lze ji však následujícím postupem převést na lineární.

Položme

$$ u(x)=[y(x)]^{1-a} $$

a po zderivování a dosazení $y'$ z (1) dostaneme

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

Protože na pravé straně platí $y^{1-a}=u$, získáme následující lineární obyčejnou diferenciální rovnici

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Příklad: logistická rovnice (Logistic Equation)

Vyřešte logistickou rovnici (speciální tvar Bernoulliho rovnice).

$$ y'=Ay-By^2 \tag{3} $$

### Řešení

Rovnici (3) přepišme do tvaru (1):

$$ y'-Ay=-By^2 $$

Zde je $a=2$, tedy $u=y^{1-a}=y^{-1}$. Zderivujeme-li $u$ a dosadíme $y'$ z (3), dostaneme

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

Poslední člen je $-Ay^{-1}=-Au$, takže získáme následující lineární obyčejnou diferenciální rovnici:

$$ u'+Au=B $$

Podle vzorce pro řešení v článku [Nehomogenní lineární obyčejná diferenciální rovnice](/posts/Solution-of-First-Order-Linear-ODE/#nehomogenni-linearni-obycejna-diferencialni-rovnice) lze určit následující obecné řešení:

$$ u=ce^{-At}+B/A $$

Protože $u=1/y$, dostáváme z toho obecné řešení rovnice (3):

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$

Získali jsme tak řešení.
