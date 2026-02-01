---
title: "Równanie Bernoulliego (Bernoulli Equation)"
description: "Omawiamy równanie Bernoulliego oraz metodę rozwiązywania jego szczególnego przypadku — równania logistycznego."
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Równanie Bernoulliego (Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ jest dowolną liczbą rzeczywistą)}  \tag{1} $$

Równanie Bernoulliego (1) jest liniowe dla $a=0$ lub $a=1$, a w pozostałych przypadkach jest nieliniowe. Można je jednak sprowadzić do postaci liniowej, wykonując poniższe kroki.

Niech

$$ u(x)=[y(x)]^{1-a} $$

a po zróżniczkowaniu i podstawieniu $y'$ z (1) otrzymujemy

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

Ponieważ w prawej stronie $y^{1-a}=u$, dostajemy następujące liniowe równanie różniczkowe zwyczajne:

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Przykład: równanie logistyczne (Logistic Equation)

Rozwiąż równanie logistyczne (szczególną postać równania Bernoulliego).

$$ y'=Ay-By^2 \tag{3} $$

### Rozwiązanie

Zapiszmy (3) w postaci (1):

$$ y'-Ay=-By^2 $$

Ponieważ $a=2$, mamy $u=y^{1-a}=y^{-1}$. Różniczkując $u$ i podstawiając $y'$ z (3), otrzymujemy

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

Ostatni wyraz to $-Ay^{-1}=-Au$, zatem dostajemy liniowe równanie różniczkowe zwyczajne

$$ u'+Au=B $$

Korzystając ze wzoru na rozwiązanie z wpisu [Niejednorodne liniowe równanie różniczkowe zwyczajne](/posts/Solution-of-First-Order-Linear-ODE/#niejednorodne-liniowe-rownanie-rozniczkowe-zwyczajne), możemy znaleźć następujące rozwiązanie ogólne:

$$ u=ce^{-At}+B/A $$

Ponieważ $u=1/y$, stąd rozwiązanie ogólne równania (3) wynosi

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$

je otrzymujemy.
