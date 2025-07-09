---
title: Ecuación de Bernoulli (Bernoulli Equation)
description: Exploramos la ecuación de Bernoulli y cómo resolver la ecuación logística,
  una forma especial de la ecuación de Bernoulli.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Ecuación de Bernoulli (Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ es un número real arbitrario)}  \tag{1} $$

La ecuación de Bernoulli (1) es lineal si $a=0$ o $a=1$, y no lineal en otros casos. Sin embargo, se puede transformar en una ecuación lineal mediante el siguiente proceso.

Sea $$ u(x)=[y(x)]^{1-a} $$

Diferenciando y sustituyendo $y'$ de la ecuación (1), obtenemos:

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

En el lado derecho, $y^{1-a}=u$, por lo que obtenemos la siguiente ecuación diferencial lineal de primer orden:

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Ejemplo: Ecuación Logística (Logistic Equation)
Resuelve la ecuación logística (una forma especial de la ecuación de Bernoulli).

$$ y'=Ay-By^2 \tag{3} $$

### Solución
Escribiendo la ecuación (3) en la forma de la ecuación (1):

$$ y'-Ay=-By^2 $$

Aquí, $a=2$, por lo que $u=y^{1-a}=y^{-1}$. Diferenciando esta u y sustituyendo $y'$ de la ecuación (3):

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

El último término es $-Ay^{-1}=-Au$, por lo que obtenemos la siguiente ecuación diferencial lineal de primer orden:

$$ u'+Au=B $$

Según la fórmula de solución para [ecuaciones diferenciales lineales de primer orden no homogéneas](/posts/Solution-of-First-Order-Linear-ODE/#ecuación-diferencial-ordinaria-lineal-no-homogénea), podemos obtener la siguiente solución general:

$$ u=ce^{-At}+B/A $$

Como $u=1/y$, de esto obtenemos la solución general de la ecuación (3):

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$
