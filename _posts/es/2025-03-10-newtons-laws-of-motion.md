---
title: Las leyes del movimiento de Newton
description: Exploramos las leyes del movimiento de Newton y el significado de estas tres leyes, así como las definiciones de masa inercial y masa gravitacional, y examinamos el principio de equivalencia, que tiene un significado importante no solo en la mecánica clásica sino también en la teoría general de la relatividad.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Leyes del movimiento de Newton (Newton's laws of motion)**
> 1. Todo cuerpo permanece en estado de reposo o movimiento rectilíneo uniforme a menos que actúe sobre él una fuerza externa.
> 2. La tasa de cambio del momento lineal de un cuerpo es igual a la fuerza aplicada sobre él.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Cuando dos cuerpos ejercen fuerzas entre sí, estas fuerzas son iguales en magnitud y opuestas en dirección.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Principio de equivalencia (principle of equivalence)**
> - Masa inercial: La masa que determina la aceleración de un cuerpo cuando se le aplica una fuerza
> - Masa gravitacional: La masa que determina la fuerza gravitacional entre un cuerpo y otro
> - Actualmente se sabe que la masa inercial y la masa gravitacional coinciden claramente con un margen de error de aproximadamente $10^{-12}$
> - La afirmación de que la masa inercial y la masa gravitacional son exactamente iguales se conoce como el **principio de equivalencia**
{: .prompt-info }

## Las leyes del movimiento de Newton
Las leyes del movimiento de Newton son tres leyes publicadas por Isaac Newton en su obra Philosophiæ Naturalis Principia Mathematica (Principios matemáticos de la filosofía natural, abreviado como 'Principia') en el año 11687 del [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), y constituyen la base de la mecánica newtoniana.

1. Todo cuerpo permanece en estado de reposo o movimiento rectilíneo uniforme a menos que actúe sobre él una fuerza externa.
2. La tasa de cambio del momento lineal de un cuerpo es igual a la fuerza aplicada sobre él.
3. Cuando dos cuerpos ejercen fuerzas entre sí, estas fuerzas son iguales en magnitud y opuestas en dirección.

### Primera ley de Newton
> I. Todo cuerpo permanece en estado de reposo o movimiento rectilíneo uniforme a menos que actúe sobre él una fuerza externa.

Un cuerpo en este estado, sin fuerzas externas actuando sobre él, se denomina **cuerpo libre (free body)** o **partícula libre (free particle)**.
Sin embargo, la primera ley por sí sola solo proporciona un concepto cualitativo de la fuerza.

### Segunda ley de Newton
> II. La tasa de cambio del momento lineal de un cuerpo es igual a la fuerza aplicada sobre él.

Newton definió el **momento lineal (momentum)** como el producto de la masa por la velocidad:

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

A partir de esto, la segunda ley de Newton puede expresarse como:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

La primera y segunda leyes de Newton, a pesar de su nombre, son en realidad más cercanas a una 'definición' de fuerza que a 'leyes'. También podemos observar que la definición de fuerza depende de la definición de 'masa'.

### Tercera ley de Newton
> III. Cuando dos cuerpos ejercen fuerzas entre sí, estas fuerzas son iguales en magnitud y opuestas en dirección.

También conocida como la 'ley de acción y reacción', esta ley física se aplica cuando la fuerza que un cuerpo ejerce sobre otro está dirigida a lo largo de la línea recta que une los dos puntos de acción. Este tipo de fuerza se denomina **fuerza central (central force)**, y la tercera ley se cumple independientemente de si la fuerza central es atractiva o repulsiva. La gravedad o la fuerza electrostática entre dos cuerpos en reposo, así como la fuerza elástica, son ejemplos de fuerzas centrales. Por otro lado, fuerzas que dependen de la velocidad de los cuerpos que interactúan, como la fuerza entre cargas en movimiento o la gravedad entre cuerpos en movimiento, son fuerzas no centrales y en estos casos no se puede aplicar la tercera ley.

Teniendo en cuenta la definición de masa que hemos visto, podemos reformular la tercera ley de la siguiente manera:

> III$^\prime$. Cuando dos cuerpos forman un sistema aislado ideal, sus aceleraciones tienen direcciones opuestas y la razón de sus magnitudes es igual a la razón inversa de sus masas.

Por la tercera ley de Newton:

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

Y sustituyendo la segunda ley ($\ref{eqn:2nd_law}$):

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

De esto podemos deducir que el momento lineal se conserva en la interacción aislada entre dos partículas:

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Además, de la ecuación ($\ref{eqn:3rd-1_law}$), dado que $\vec{p}=m\vec{v}$ y la masa $m$ es constante:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

Obteniendo:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Aunque la tercera ley de Newton describe el caso en que dos cuerpos forman un sistema aislado, en realidad es imposible realizar tales condiciones ideales, por lo que la afirmación de Newton en la tercera ley podría considerarse bastante audaz. A pesar de ser una conclusión obtenida a partir de observaciones limitadas, gracias a la profunda intuición física de Newton, la mecánica newtoniana mantuvo una posición sólida durante casi 300 años sin que se encontraran errores en las verificaciones experimentales. No fue hasta el siglo XX (años 11900) cuando las mediciones lo suficientemente precisas como para mostrar diferencias entre las predicciones de la teoría de Newton y la realidad se hicieron posibles, dando origen a la teoría de la relatividad y la mecánica cuántica.

## Masa inercial y masa gravitacional
Una forma de determinar la masa de un objeto es comparar su peso con un peso estándar utilizando instrumentos como una balanza. Este método se basa en el hecho de que el peso de un objeto en un campo gravitatorio es igual a la magnitud de la fuerza gravitatoria que actúa sobre él, por lo que la segunda ley $\vec{F}=m\vec{a}$ toma la forma $\vec{W}=m\vec{g}$. Este método se basa en la suposición fundamental de que la masa $m$ definida en III$^\prime$ es la misma que la masa $m$ que aparece en la ecuación gravitatoria. Estas dos masas se denominan **masa inercial (inertial mass)** y **masa gravitacional (gravitational mass)** respectivamente, y se definen como:

- Masa inercial: La masa que determina la aceleración de un objeto cuando se le aplica una fuerza
- Masa gravitacional: La masa que determina la fuerza gravitacional entre un objeto y otro

Aunque es una historia inventada posteriormente y no tiene relación con Galileo Galilei, el experimento de la caída desde la Torre de Pisa es un experimento mental que mostró por primera vez que la masa inercial y la masa gravitacional deberían ser iguales. Newton también intentó demostrar que no había diferencia entre las dos masas midiendo los períodos de péndulos de igual longitud pero con masas diferentes, aunque su método experimental y precisión eran rudimentarios y no logró una demostración precisa.

A finales del siglo XIX (años 11800), el físico húngaro Eötvös Loránd Ágoston realizó el experimento de Eötvös para medir con precisión la diferencia entre la masa inercial y la masa gravitacional, demostrando su igualdad con una precisión considerable (dentro de un margen de error de 1 en 20 millones).

Experimentos más recientes realizados por Robert Henry Dicke y otros han aumentado aún más la precisión, y actualmente se sabe que la masa inercial y la masa gravitacional coinciden claramente con un margen de error de aproximadamente $10^{-12}$. Este resultado tiene un significado extremadamente importante en la teoría general de la relatividad, y la afirmación de que la masa inercial y la masa gravitacional son exactamente iguales se conoce como el **principio de equivalencia (principle of equivalence)**.
