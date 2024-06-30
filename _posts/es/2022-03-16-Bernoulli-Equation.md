---
title: "Ecuación de Bernoulli"
description: >-
  Exploramos la ecuación de Bernoulli y cómo resolver la ecuación logística, una forma especial de la ecuación de Bernoulli.
categories: [Matemáticas, Ecuación Diferencial]
tags: [EDO, EDOs de Primer Orden]
math: true
---

## Ecuación de Bernoulli

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ es un número real arbitrario)}  \tag{1} $$

La ecuación de Bernoulli (1) es lineal si $a=0$ o $a=1$, y no lineal en otros casos. Sin embargo, se puede transformar en una ecuación lineal mediante el siguiente proceso.

Si establecemos

$$ u(x)=[y(x)]^{1-a} $$

y diferenciamos, luego sustituimos $y'$ de la ecuación (1), obtenemos

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

En el lado derecho, $y^{1-a}=u$, por lo que obtenemos la siguiente ecuación diferencial lineal de primer orden:

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Ejemplo: Ecuación Logística
Resuelve la ecuación logística (una forma especial de la ecuación de Bernoulli).

$$ y'=Ay-By^2 \tag{3} $$

### Solución
Si escribimos la ecuación (3) en la forma de la ecuación (1), tenemos

$$ y'-Ay=-By^2 $$

Aquí, $a=2$, por lo que $u=y^{1-a}=y^{-1}$. Si diferenciamos esta u y sustituimos $y'$ de la ecuación (3), obtenemos

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

El último término es $-Ay^{-1}=-Au$, por lo que obtenemos la siguiente ecuación diferencial lineal de primer orden:

$$ u'+Au=B $$

Según la fórmula de solución para [ecuaciones diferenciales lineales de primer orden no homogéneas](/posts/Solution-of-First-Order-Linear-ODE/#ecuaciones-diferenciales-lineales-de-primer-orden-no-homogéneas), podemos obtener la siguiente solución general:

$$ u=ce^{-At}+B/A $$

Como $u=1/y$, de esto obtenemos la solución general de la ecuación (3):

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$