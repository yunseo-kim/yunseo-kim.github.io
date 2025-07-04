---
title: Principio de relatividad y transformación de Lorentz
description: Exploramos el concepto de sistemas de referencia y la transformación de Galileo ampliamente utilizada en la mecánica clásica. También examinamos brevemente las ecuaciones de Maxwell y el experimento de Michelson-Morley que sirvieron como antecedentes para la aparición de la transformación de Lorentz, y derivamos la matriz de transformación de Lorentz.
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Principio de relatividad**: El principio de que todas las leyes físicas deben ser idénticas en diferentes sistemas de referencia que se mueven a velocidad constante entre sí
{: .prompt-info }

> **Factor de Lorentz $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **Transformación de Lorentz**
>
> $$ \begin{pmatrix}
> \vec{x}^\prime \\ ct^\prime
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & -\gamma\vec{\beta} \\
> -\gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}. $$
>
> - $ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $
> - $ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $
{: .prompt-info }

> **Transformación inversa de Lorentz**
>
> $$ \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & \gamma\vec{\beta} \\
> \gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x^\prime} \\ ct^\prime
> \end{pmatrix}. $$
>
> - $ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime $
> - $ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} $
{: .prompt-info }

## Sistemas de referencia y principio de relatividad
### Sistema de referencia (frame of reference)
- **Sistema de referencia (frame of reference)**: Cuando decimos que un objeto se mueve, significa que su posición cambia relativamente respecto a otros objetos. Como todo movimiento es relativo, para describir cualquier movimiento es necesario establecer un sistema de referencia.
- **Sistema de referencia inercial (inertial frames of reference)**: Un sistema donde se cumple la primera ley de Newton ("El estado de movimiento de un objeto permanece invariable mientras la fuerza neta que actúa sobre él sea cero"). Cualquier sistema de referencia que se mueve a velocidad constante respecto a un sistema inercial también es un sistema inercial.

### Principio de relatividad (Principle of Relativity)
Es uno de los conceptos fundamentales y premisas básicas de la física, que establece que todas las leyes físicas deben ser idénticas en diferentes sistemas de referencia que se mueven a velocidad constante entre sí. Si las leyes físicas fueran diferentes para observadores en movimiento relativo, estas diferencias podrían utilizarse para establecer un sistema de referencia absoluto y determinar quién está en reposo y quién en movimiento. Sin embargo, según el principio de relatividad, tal distinción no existe, por lo que no hay un sistema de referencia absoluto ni movimiento absoluto en el universo, y todos los sistemas inerciales son equivalentes.

## Limitaciones de la transformación de Galileo
### Transformación de Galileo (Galilean transformation)
Supongamos que existen dos sistemas inerciales $S$ y $S^{\prime}$, donde $S^{\prime}$ se mueve respecto a $S$ con una velocidad constante $\vec{v}$ en la dirección $+x$. Un mismo evento es observado en $S$ en las coordenadas $(x, y, z)$ en el tiempo $t$, y en $S^{\prime}$ en las coordenadas $(x^{\prime}, y^{\prime}, z^{\prime})$ en el tiempo $t^{\prime}$.

En este caso, el valor del movimiento en la dirección $x$ medido en $S^{\prime}$ será menor que el medido en $S$ por la distancia que $S^{\prime}$ se ha movido respecto a $S$ en la dirección $x$, que es $\vec{v}t$, por lo tanto:

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

Y como no hay movimiento relativo en las direcciones $y$ y $z$:

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

Intuitivamente, podemos asumir que:

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

Esta transformación de coordenadas entre diferentes sistemas inerciales, representada por las ecuaciones ($\ref{eqn:galilean_transform_x}$) a ($\ref{eqn:galilean_transform_t}$), se conoce como **transformación de Galileo (Galilean transformation)**. Es simple e intuitiva, y funciona bien en la mayoría de las situaciones cotidianas. Sin embargo, como veremos más adelante, contradice las ecuaciones de Maxwell.

### Ecuaciones de Maxwell
A finales del siglo 11800, Maxwell (Maxwell) amplió las ideas y resultados de investigaciones previas propuestas por científicos como Faraday (Faraday) y Ampere (Ampere), revelando que la electricidad y el magnetismo son en realidad una sola fuerza, y derivó las siguientes cuatro ecuaciones que describen el campo electromagnético:

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: El flujo eléctrico a través de cualquier superficie cerrada es igual a la carga neta en su interior (ley de Gauss).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: No existen monopolos magnéticos (cargas magnéticas).}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: Un campo magnético variable crea un campo eléctrico (ley de Faraday).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: Un campo eléctrico variable y una corriente crean un campo magnético (ley de Ampere-Maxwell).}
\end{gather*}$$

Las ecuaciones de Maxwell explicaban con éxito todos los fenómenos eléctricos y magnéticos conocidos hasta entonces, predijeron la existencia de ondas electromagnéticas y derivaron que la velocidad de las ondas electromagnéticas en el vacío, $c$, es una constante invariable, convirtiéndose en las fórmulas fundamentales del electromagnetismo.

### Contradicción entre la transformación de Galileo y las ecuaciones de Maxwell
La mecánica newtoniana, que utiliza la transformación de Galileo, ha sido la base de la física durante más de 200 años, y las ecuaciones de Maxwell son, como se mencionó, ecuaciones fundamentales que describen los fenómenos eléctricos y magnéticos. Sin embargo, existe una contradicción entre ambas:

- Según el principio de relatividad, se esperaría que las ecuaciones de Maxwell también tuvieran la misma forma en todos los sistemas inerciales, pero al aplicar la transformación de Galileo para convertir mediciones de un sistema inercial a otro, las ecuaciones de Maxwell adquieren una forma muy diferente.
- A partir de las ecuaciones de Maxwell se puede calcular la magnitud de la velocidad de la luz $c$, que es una constante invariable, pero según la mecánica newtoniana y la transformación de Galileo, la velocidad de la luz $c$ se mediría de manera diferente en distintos sistemas inerciales.

Por lo tanto, las ecuaciones de Maxwell y la transformación de Galileo son incompatibles, y al menos una de ellas debía ser modificada. Esto sirvió como antecedente para la aparición de la **transformación de Lorentz (Lorentz transformation)** que se discutirá más adelante.

## Teoría del éter (aether) y experimento de Michelson-Morley
En la física del siglo 11800, se creía que la luz, al igual que otras ondas como las ondas superficiales o el sonido, se propagaba a través de un medio hipotético llamado *éter (aether)*, y se hicieron esfuerzos para descubrir su existencia.

Según la teoría del éter, el espacio, aunque fuera vacío, estaría lleno de éter, por lo que el movimiento orbital de la Tierra a aproximadamente 30 km/s respecto al Sol formaría un "viento de éter" que atravesaría la Tierra.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Para verificar esta hipótesis, en el año 11887 del [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), Michelson (Michelson) colaboró con Morley (Morley) para realizar el *experimento de Michelson-Morley (Michelson-Morley Experiment)* utilizando el interferómetro mostrado a continuación:  
![Interferómetro de Michelson-Morley](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Fuente de la imagen*
> - Autor: Albert Abraham Michelson with Edward Morley
> - Licencia: dominio público

En este experimento, el rayo de luz se divide en dos al pasar por un semiespejo, luego cada rayo recorre ida y vuelta los dos brazos perpendiculares del interferómetro, recorriendo aproximadamente 11 metros en total, y se encuentran en el punto medio, donde según la diferencia de fase entre los dos rayos, se producen patrones de interferencia constructiva o destructiva. Según la teoría del éter, la velocidad de la luz debería variar dependiendo de la velocidad relativa respecto al éter, lo que provocaría cambios en esta diferencia de fase y, por tanto, en los patrones de interferencia. Sin embargo, no se observó ningún cambio en los patrones de interferencia. Para explicar este resultado experimental, se hicieron varios intentos, entre los cuales FitzGerald (FitzGerald) y Lorentz (Lorentz) propusieron la *contracción de Lorentz-FitzGerald (Lorentz–FitzGerald contraction)* o *contracción de longitud (length contraction)*, que sugería que un objeto se contrae en longitud cuando <u>se mueve relativamente respecto al éter</u>, lo que condujo a la transformación de Lorentz.

> En ese momento, Lorentz creía en la existencia del éter y pensaba que la contracción de longitud ocurría debido al movimiento relativo respecto al éter. Posteriormente, Einstein (Einstein) interpretó el verdadero significado físico de la transformación de Lorentz con su *Teoría de la Relatividad Especial (Theory of Special Relativity)*, explicando la contracción de longitud en términos del concepto de espacio-tiempo en lugar del éter, y también se descubrió que el éter no existe.
{: .prompt-info }

## Transformación de Lorentz (Lorentz transformation)
### Derivación de la transformación de Lorentz
En la misma situación que vimos con la transformación de Galileo (ecuaciones [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]), supongamos que la relación de transformación correcta entre $x$ y $x^{\prime}$ que no contradice las ecuaciones de Maxwell es:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Donde $\gamma$ puede ser una función de $\vec{v}$ pero no depende de $x$ ni de $t$. Podemos hacer esta suposición por las siguientes razones:

- Para que exista una correspondencia uno a uno entre los eventos en $S$ y $S^{\prime}$, $x$ y $x^{\prime}$ deben tener una relación lineal.
- Como sabemos que la transformación de Galileo es correcta en situaciones mecánicas cotidianas, debe ser posible aproximarla mediante la ecuación ($\ref{eqn:galilean_transform_x}$).
- Debe tener una forma lo más simple posible.

Como las fórmulas físicas deben tener la misma forma en los sistemas de referencia $S$ y $S^{\prime}$, para expresar $x$ en términos de $x^{\prime}$ y $t$, solo hay que cambiar el signo de $\vec{v}$ (la dirección del movimiento relativo), y como no debe haber diferencia entre los dos sistemas de referencia excepto por el signo de $\vec{v}$, $\gamma$ debe ser el mismo:

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Al igual que en la transformación de Galileo, no hay razón para que las componentes perpendiculares a la dirección de $\vec{v}$, es decir, $y$ y $y^{\prime}$, así como $z$ y $z^{\prime}$, sean diferentes, por lo que:

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Ahora, sustituyendo la ecuación ($\ref{eqn:lorentz_transform_x}$) en ($\ref{eqn:lorentz_transform_x_inverse}$):

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

Despejando $t^{\prime}$:

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Además, para no contradecir las ecuaciones de Maxwell, la velocidad de la luz debe ser la misma ($c$) en ambos sistemas de referencia, lo que nos permite determinar $\gamma$. Si en $t=0$ los orígenes de ambos sistemas coinciden, entonces por esta condición inicial, $t^\prime = 0$. Ahora, imaginemos que en $t=t^\prime=0$ hay un destello de luz en el origen común de $S$ y $S^\prime$, y los observadores en cada sistema miden la velocidad de esta luz. En el sistema $S$:

$$ x = ct \label{eqn:ct_S}\tag{9}$$

Y en el sistema $S^\prime$:

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Sustituyendo $x$ y $t$ en estas ecuaciones usando ($\ref{eqn:lorentz_transform_x}$) y ($\ref{eqn:lorentz_transform_t}$):

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Resolviendo para $x$:

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Pero según la ecuación ($\ref{eqn:ct_S}$), $x=ct$, por lo que:

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

Por lo tanto:

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Sustituyendo esta expresión de $\gamma$ en función de $\vec{v}$ en las ecuaciones ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$) y ($\ref{eqn:lorentz_transform_t}$), obtenemos las ecuaciones finales de transformación del sistema $S$ al sistema $S^\prime$.

### Matriz de transformación de Lorentz

Las ecuaciones de transformación finales que obtuvimos son:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

Estas ecuaciones constituyen la **transformación de Lorentz (Lorentz transformation)**. Si definimos $\vec{\beta}=\vec{v}/c$, podemos expresarlas en forma matricial como:

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
\end{pmatrix}. \label{lorentz_transform_matrix}\tag{16}$$

Lorentz (Lorentz) demostró que utilizando esta transformación, las fórmulas fundamentales del electromagnetismo mantienen la misma forma en todos los sistemas de referencia inerciales. También podemos verificar que cuando la velocidad $v$ es muy pequeña comparada con la velocidad de la luz $c$, $\gamma \to 1$, por lo que la transformación se aproxima a la transformación de Galileo.

### Transformación inversa de Lorentz (inverse Lorentz transformation)
A veces es más conveniente transformar las mediciones del sistema en movimiento $S^\prime$ a las del sistema en reposo $S$, en lugar de hacerlo al revés.
En estos casos, podemos usar la **transformación inversa de Lorentz (inverse Lorentz transformation)**.  
Calculando la matriz inversa de ($\ref{lorentz_transform_matrix}$), obtenemos la siguiente matriz de transformación inversa de Lorentz:

$$ \begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & 0 & 0 & \gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix}. \tag{17}
$$

Esto equivale a intercambiar las cantidades físicas con prima y sin prima en las ecuaciones ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) y reemplazar $v$ por $-v$ (es decir, $\beta$ por $-\beta$).

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
