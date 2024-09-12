---
title: "Principio de relatividad y transformación de Lorentz"
description: >-
  Exploramos el concepto de sistemas de referencia y la transformación de Galileo ampliamente utilizada en la mecánica clásica. También examinamos brevemente las ecuaciones de Maxwell y el experimento de Michelson-Morley que sirvieron de base para la aparición de la transformación de Lorentz, y derivamos la matriz de transformación de Lorentz.
categories: [Engineering Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
---

## Sistemas de referencia y principio de relatividad
### Sistema de referencia (frame of reference)
- **Sistema de referencia (frame of reference)**: Decir que un objeto se mueve significa que su posición cambia relativamente respecto a otros objetos. Como todo movimiento es relativo, para describir un movimiento es necesario establecer un sistema de referencia que sirva de base.
- **Sistema de referencia inercial (inertial frames of reference)**: Un sistema en el que se cumple la primera ley del movimiento de Newton ("El estado de movimiento de un objeto permanece invariable mientras la fuerza neta que actúa sobre él sea cero"). Cualquier sistema de referencia que se mueva a velocidad constante respecto a un sistema inercial es también un sistema de referencia inercial.

### Principio de relatividad (Principle of Relativity)
Uno de los conceptos principales y premisas básicas de la física, que establece que todas las leyes físicas deben ser las mismas en diferentes sistemas de referencia que se mueven a velocidad constante entre sí. Si los observadores en movimiento relativo experimentaran leyes físicas diferentes, esta diferencia podría utilizarse para establecer un sistema de referencia absoluto y determinar quién está en reposo y quién en movimiento. Sin embargo, según el principio de relatividad, tal distinción no existe, por lo que no hay un sistema de referencia absoluto o movimiento absoluto para todo el universo, y todos los sistemas de referencia inerciales son equivalentes.

## Limitaciones de la transformación de Galileo
### Transformación de Galileo (Galilean transformation)
Supongamos que existen dos sistemas inerciales $S$ y $S^{\prime}$, donde $S^{\prime}$ se mueve con una velocidad constante $\vec{v}$ en la dirección $+x$ respecto a $S$, y un mismo evento es observado en $S$ en las coordenadas $(x, y, z)$ en el tiempo $t$, y en $S^{\prime}$ en las coordenadas $(x^{\prime}, y^{\prime}, z^{\prime})$ en el tiempo $t^{\prime}$.

En este caso, el valor del movimiento en la dirección $x$ medido en $S^{\prime}$ será mayor que el medido en $S$ por la distancia que $S^{\prime}$ se ha movido respecto a $S$ en la dirección $x$, que es $\vec{v}t$, por lo tanto:

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

Y como no hay movimiento relativo en las direcciones $y$ y $z$:

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

Intuitivamente, podemos asumir que:

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

Esta transformación de coordenadas entre sistemas inerciales diferentes, desde la ecuación ($\ref{eqn:galilean_transform_x}$) hasta la ($\ref{eqn:galilean_transform_t}$), utilizada clásicamente en física, se denomina **transformación de Galileo (Galilean transformation)**. Es simple e intuitiva y funciona bien en la mayoría de las situaciones cotidianas. Sin embargo, como se mencionará más adelante, entra en contradicción con las ecuaciones de Maxwell.

### Ecuaciones de Maxwell
A finales del siglo XIX, Maxwell (Maxwell) amplió las ideas y resultados de investigaciones previas propuestas por otros científicos como Faraday (Faraday) y Ampère (Ampere), revelando que la electricidad y el magnetismo son en realidad una sola fuerza, y derivó las siguientes cuatro ecuaciones que describen el campo electromagnético:

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: El flujo eléctrico a través de cualquier superficie cerrada es igual a la carga neta en su interior (Ley de Gauss).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: No existen monopolos magnéticos.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: Un campo magnético variable crea un campo eléctrico (Ley de Faraday).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: Las corrientes eléctricas y los campos eléctricos variables crean campos magnéticos (Ley de Ampère-Maxwell).}
\end{gather*}$$

Las ecuaciones de Maxwell explicaban con éxito todos los fenómenos eléctricos y magnéticos conocidos hasta entonces, predijeron la existencia de ondas electromagnéticas y también derivaron que la velocidad de las ondas electromagnéticas en el vacío, $c$, es una constante invariable, convirtiéndose así en las fórmulas fundamentales del electromagnetismo.

### Contradicción entre la transformación de Galileo y las ecuaciones de Maxwell
La mecánica newtoniana, que utiliza la transformación de Galileo, ha sido la base de la física durante más de 200 años, y las ecuaciones de Maxwell son, como se mencionó anteriormente, las ecuaciones fundamentales que describen los fenómenos eléctricos y magnéticos. Sin embargo, existe una contradicción entre ambas:

- Según el principio de relatividad, se espera que las ecuaciones de Maxwell también tengan la misma forma en todos los sistemas inerciales, pero al aplicar la transformación de Galileo para convertir los valores medidos en un sistema inercial a los valores medidos en otro sistema inercial, las ecuaciones de Maxwell toman una forma muy diferente.
- Aunque la magnitud de la velocidad de la luz $c$ se puede calcular a partir de las ecuaciones de Maxwell y es una constante invariable, según la mecánica newtoniana y la transformación de Galileo, la velocidad de la luz $c$ se mide de manera diferente en diferentes sistemas inerciales.

Por lo tanto, las ecuaciones de Maxwell y la transformación de Galileo son incompatibles entre sí, y al menos una de ellas debía ser modificada. Esto se convirtió en el trasfondo para la aparición de la **transformación de Lorentz (Lorentz transformation)** que se mencionará más adelante.

## Teoría del éter (aether) y experimento de Michelson-Morley
Por otro lado, en la física del siglo XIX se creía que la luz, al igual que otras ondas como las ondas superficiales o las ondas sonoras, se transmitía a través de un medio hipotético llamado *éter (aether)*, y se hicieron esfuerzos para descubrir la existencia de este éter.

Según la teoría del éter, incluso si el espacio exterior estuviera vacío, estaría lleno de éter, por lo que se pensaba que la órbita de la Tierra, que se mueve a una velocidad de aproximadamente 30 km/s respecto al Sol, formaría un viento de éter que atravesaría la Tierra.
![Viento de éter](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Para verificar esta hipótesis, en 1887 Michelson (Michelson) colaboró con Morley (Morley) para realizar el *experimento de Michelson-Morley (Michelson-Morley Experiment)* utilizando el interferómetro que se muestra a continuación.  
![Interferómetro de Michelson-Morley](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Fuente de la imagen*
> - Autor: Albert Abraham Michelson con Edward Morley
> - Licencia: dominio público

En este experimento, el rayo de luz se divide en dos al pasar por un espejo semitransparente, luego cada rayo viaja de ida y vuelta por los dos brazos perpendiculares del interferómetro, recorriendo un total de unos 11 m, y se encuentran en el punto medio, donde se producen patrones de interferencia constructiva o destructiva según la diferencia de fase entre los dos rayos. Según la teoría del éter, la velocidad de la luz debería variar dependiendo de la velocidad relativa al éter, por lo que se esperaba observar un cambio en estos patrones de interferencia, pero en realidad no se pudo observar ningún cambio. Hubo varios intentos de explicar estos resultados experimentales, entre los cuales FitzGerald (FitzGerald) y Lorentz (Lorentz) propusieron la *contracción de Lorentz-FitzGerald (Lorentz–FitzGerald contraction)* o *contracción de longitud (length contraction)*, que sugiere que la longitud de un objeto se contrae cuando <u>se mueve relativamente al éter</u>, lo que lleva a la transformación de Lorentz.

> En ese momento, Lorentz creía en la existencia del éter y pensaba que la contracción de longitud ocurría debido al movimiento relativo al éter. Más tarde, Einstein (Einstein) interpretó el verdadero significado físico de la transformación de Lorentz con su *Teoría de la Relatividad Especial (Theory of Special Relativity)*, explicando la contracción de longitud en términos del concepto de espacio-tiempo en lugar del éter, y también se descubrió posteriormente que el éter no existe.
{: .prompt-info }

## Transformación de Lorentz (Lorentz transformation)
### Derivación de la transformación de Lorentz
En la misma situación que en la transformación de Galileo (ecuaciones [$\ref{eqn:galilean_transform_x}$]~[$\ref{eqn:galilean_transform_t}$]), supongamos que la relación de transformación correcta entre $x$ y $x^{\prime}$ que no contradice las ecuaciones de Maxwell es la siguiente:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Aquí, $\gamma$ no depende de $x$ y $t$, pero puede ser una función de $\vec{v}$. Las razones para hacer esta suposición son las siguientes:

- Para que haya una correspondencia uno a uno entre los eventos en $S$ y $S^{\prime}$, $x$ y $x^{\prime}$ deben tener una relación lineal.
- Como se sabe que la transformación de Galileo es correcta en la mecánica de situaciones cotidianas, debe poder aproximarse a la ecuación ($\ref{eqn:galilean_transform_x}$).
- Debe tener una forma lo más simple posible.

Como las fórmulas físicas deben tener la misma forma en los sistemas de referencia $S$ y $S^{\prime}$, para expresar $x$ en términos de $x^{\prime}$ y $t$, solo se necesita cambiar el signo de $\vec{v}$ (la dirección del movimiento relativo), y como no debe haber ninguna diferencia entre los dos sistemas de referencia excepto por el signo de $\vec{v}$, $\gamma$ debe ser el mismo.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Al igual que en la transformación de Galileo, no hay razón para que las componentes perpendiculares a la dirección de $\vec{v}$, es decir, $y$ y $y^{\prime}$, y $z$ y $z^{\prime}$, sean diferentes, por lo que:

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Ahora, si sustituimos la ecuación ($\ref{eqn:lorentz_transform_x}$) en ($\ref{eqn:lorentz_transform_x_inverse}$):

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

Por lo tanto, despejando $t^{\prime}$:

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Además, para no contradecir las ecuaciones de Maxwell, la velocidad de la luz debe ser $c$ en ambos sistemas de referencia, lo que nos permite determinar $\gamma$. Si los orígenes de los dos sistemas de referencia estaban en el mismo lugar cuando $t=0$, entonces por esta condición inicial, $t^\prime = 0$. Ahora imaginemos que hubo un destello de luz en el origen común de $S$ y $S^\prime$ cuando $t=t^\prime=0$, y que los observadores en cada sistema de referencia miden la velocidad de esta luz. En este caso, en el sistema de referencia $S$:

$$ x = ct \label{eqn:ct_S}\tag{9}$$

y en el sistema de referencia $S^\prime$:

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Sustituyendo $x$ y $t$ en la ecuación anterior usando las ecuaciones ($\ref{eqn:lorentz_transform_x}$) y ($\ref{eqn:lorentz_transform_t}$):

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Resolviendo esta ecuación para $x$:

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Sin embargo, como vimos en la ecuación ($\ref{eqn:ct_S}$), $x=ct$, por lo tanto:

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

Y por lo tanto:

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Sustituyendo esta expresión de $\gamma$ en función de $\vec{v}$ en las ecuaciones ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), ($\ref{eqn:lorentz_transform_t}$), obtenemos finalmente las ecuaciones de transformación del sistema de referencia $S$ al $S^\prime$.

### Matriz de transformación de Lorentz

Las ecuaciones de transformación que finalmente obtuvimos son las siguientes:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} $$
- $$ y^\prime = y $$
- $$ z^\prime = z $$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} $$

Estas ecuaciones son la **transformación de Lorentz (Lorentz transformation)**. Si definimos $\vec{\beta}=\vec{v}/c$, podemos expresarlas en forma matricial de la siguiente manera:

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}.$$

Lorentz (Lorentz) demostró que al usar estas ecuaciones de transformación, las fórmulas básicas del electromagnetismo se mantienen en la misma forma en todos los sistemas de referencia inerciales. Además, podemos ver que cuando la velocidad $v$ es muy pequeña en comparación con la velocidad de la luz $c$, $\gamma \to 1$, por lo que se puede aproximar a la transformación de Galileo.

Si generalizamos para el caso en que la velocidad relativa de $S^\prime$ respecto al sistema de referencia inercial $S$ es $\vec{v}=v_x\hat{i}+v_y\hat{j}+v_z\hat{k}$, $\vec{\beta}=\vec{v}/c$, y los vectores de posición medidos en los dos sistemas de referencia son $\vec{x}=x_1\hat{i}+x_2\hat{j}+x_3\hat{k}$ y $\vec{x^\prime}=x_1^\prime\hat{i}+x_2^\prime\hat{j}+x_3^\prime\hat{k}$ respectivamente, la transformación de Lorentz se puede escribir como:

- $$ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $$
- $$ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $$

O bien:

$$ \begin{pmatrix}
\vec{x}^\prime \\ ct^\prime
\end{pmatrix}
= \begin{pmatrix}
\gamma & -\gamma\vec{\beta} \\
-\gamma\vec{\beta} & \gamma
\end{pmatrix}
\begin{pmatrix}
\vec{x} \\ ct
\end{pmatrix}.
$$
