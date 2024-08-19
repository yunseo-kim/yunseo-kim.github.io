---
title: "Teorema de la Adición Armónica"
description: >-
  Exploramos cómo encontrar una función trigonométrica única correspondiente r sin(θ+α) o r cos(θ-β) para una suma de funciones trigonométricas de la forma f(θ) = a cos θ + b sin θ.
categories: [Matemáticas]
tags: [Trigonometría]
math: true
---

## TL;DR
> **Teorema de la Adición Armónica**
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \sin(\theta+\alpha) $$
>
> $$ (donde,\ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}) $$
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \cos(\theta-\beta) $$
>
> $$ (donde,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}) $$
{: .prompt-info }

## Prerrequisitos
- [Fórmulas de adición trigonométrica](/posts/trigonometric-addition-formulas)

## Teorema de la Adición Armónica
Para una función f(θ) = a cos θ + b sin θ que consiste en una suma de funciones trigonométricas, siempre existen números reales α y β que satisfacen f(θ)=√(a²+b²) sin(θ+α) = √(a²+b²) cos(θ-β).

![Derivación geométrica del Teorema de la Adición Armónica](/assets/img/trigonometry/harmonic-addition.png)

Como se muestra en la figura, si tomamos un punto P(a,b) en el plano de coordenadas y definimos α como el ángulo formado entre el segmento OP y la dirección positiva del eje x, entonces

$$ \overline{OP} = \sqrt{a^2+b^2} $$

y

$$ \cos \alpha = \frac{a}{\sqrt{a^{2} + b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2} + b^{2}}} \tag{1} $$

En este caso,

$$ \begin{align*}
a \sin \theta + b \cos \theta &= \sqrt{a^{2}+b^{2}} \left(\frac{a}{\sqrt{a^{2}+b^{2}}}\sin \theta + \frac{b}{\sqrt{a^{2}+b^{2}}}\cos \theta \right) \\
&= \sqrt{a^{2}+b^{2}}(\cos \alpha \sin \theta + \sin \alpha \cos \theta) \\
&= \sqrt{a^{2}+b^{2}} \sin(\theta + \alpha). \tag{2}
\end{align*} $$

De manera similar, si tomamos un punto P'(b,a) y definimos β como el ángulo formado entre el segmento OP y la dirección positiva del eje x, obtenemos:

$$ a \sin \theta + b \cos \theta = \sqrt{a^{2}+b^{2}}\cos(\theta-\beta). \tag{3} $$

$$ donde,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}. $$

La transformación de una función trigonométrica de la forma a sin θ + b sin θ en la forma r sin(θ+α) o r cos(θ-β) se conoce como Adición Armónica.

## Ejemplo
Dada la función f(θ)=-√3 sin θ + cos(θ - π/3), encuentra los valores máximo y mínimo de f(θ) en el intervalo [0, 2π].

### 1. Transformar a la forma a sin θ + b cos θ
Usando las [fórmulas de adición trigonométrica](/posts/trigonometric-addition-formulas), transformamos la función dada:

$$ \begin{align*}
f(\theta) &= -\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right) \\
&= -\sqrt{3}\sin \theta + \left( \cos\theta \cos\frac{\pi}{3} + \sin\theta \sin\frac{\pi}{3} \right) \\
&= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta .
\end{align*} $$

### 2. Transformar a la forma r sin(θ+α)
Tomando a=-√3/2 y b=1/2,

$$ r = \sqrt{a^2+b^2} = \sqrt{\frac{3}{4}+\frac{1}{4}} = 1 $$

Además, existe un único valor real α en el rango 0 ≤ α < 2π que satisface cos α = a y sin α = b. De los valores trigonométricos para ángulos especiales, podemos determinar que α = 5π/6.

Por lo tanto, la función dada f(θ) transformada a la forma r sin(θ+α) es:

$$ f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right). $$

### 3. Encontrar los valores máximo y mínimo en el intervalo dado
![Gráfica de la función dada](/assets/img/trigonometry/harmonic-addition-ex-graph.png)

La función f(θ) = sin(θ + 5π/6) es una función periódica con período 2π, y en el intervalo dado tiene un valor máximo de 1 y un valor mínimo de -1.

$$ \therefore M=1,\ m=-1$$