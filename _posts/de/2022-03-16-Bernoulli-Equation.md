---
title: "Bernoulli-Gleichung (Bernoulli Equation)"
description: >-
  Wir untersuchen die Bernoulli-Gleichung und die Lösungsmethode für die logistische Gleichung, eine spezielle Form der Bernoulli-Gleichung.
categories: [Mathematik, Differentialgleichung]
tags: [ODE, Differentialgleichungen erster Ordnung]
math: true
---

## Bernoulli-Gleichung (Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ ist eine beliebige reelle Zahl)}  \tag{1} $$

Die Bernoulli-Gleichung (1) ist linear, wenn $a=0$ oder $a=1$, und in allen anderen Fällen nichtlinear. Sie kann jedoch durch den folgenden Prozess in eine lineare Form umgewandelt werden.

Setzen wir

$$ u(x)=[y(x)]^{1-a} $$

und differenzieren dies. Wenn wir dann $y'$ aus Gleichung (1) einsetzen, erhalten wir

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

In der rechten Seite ist $y^{1-a}=u$, also erhalten wir die folgende lineare Differentialgleichung erster Ordnung:

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Beispiel: Logistische Gleichung (Logistic Equation)
Lösen Sie die logistische Gleichung (eine spezielle Form der Bernoulli-Gleichung):

$$ y'=Ay-By^2 \tag{3} $$

### Lösung
Wenn wir Gleichung (3) in die Form von Gleichung (1) umschreiben, erhalten wir

$$ y'-Ay=-By^2 $$

Hier ist $a=2$, also ist $u=y^{1-a}=y^{-1}$. Wenn wir dieses u differenzieren und $y'$ aus Gleichung (3) einsetzen, erhalten wir

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

Der letzte Term ist $-Ay^{-1}=-Au$, also erhalten wir die folgende lineare Differentialgleichung erster Ordnung:

$$ u'+Au=B $$

Gemäß der Lösungsformel für [inhomogene lineare Differentialgleichungen erster Ordnung](/posts/Solution-of-First-Order-Linear-ODE/#inhomogene-lineare-differentialgleichung) können wir die folgende allgemeine Lösung finden:

$$ u=ce^{-At}+B/A $$

Da $u=1/y$, erhalten wir daraus die allgemeine Lösung für Gleichung (3):

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$