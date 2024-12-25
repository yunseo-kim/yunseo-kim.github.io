---
title: Teorema de Ehrenfest
description: Exploramos cómo calcular los valores esperados de posición y momento
  a partir de la función de onda en mecánica cuántica, extendiendo esto a una fórmula
  para el valor esperado de cualquier variable mecánica Q(x,p). Luego derivamos el
  teorema de Ehrenfest a partir de estos resultados.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Prerrequisitos
- Distribución de probabilidad continua y densidad de probabilidad
- [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/)

## Cálculo de valores esperados a partir de la función de onda
### Valor esperado de la posición $x$
El valor esperado (expectation value) de la posición $x$ para una partícula en el estado $\Psi$ es

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

Si medimos la posición de un número suficientemente grande de partículas en el mismo estado $\Psi$ y promediamos los resultados de las mediciones, obtendremos $\langle x \rangle$ calculado mediante la ecuación anterior.

> Hay que tener en cuenta que el valor esperado del que hablamos aquí no es el promedio obtenido de mediciones repetidas en una sola partícula, sino el promedio de los resultados de mediciones en un **ensemble** de sistemas con el mismo estado. Si se realizan múltiples mediciones repetidas en la misma partícula en intervalos cortos de tiempo, la [función de onda colapsará (collapse)](/posts/schrodinger-equation-and-the-wave-function/#medición-y-colapso-de-la-función-de-onda) en la primera medición, por lo que las mediciones posteriores darán continuamente el mismo valor.
{: .prompt-warning }

### Valor esperado del momento $p$
Como $\Psi$ depende del tiempo, $\langle x \rangle$ cambiará con el tiempo. Entonces, según la ecuación (8) de [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/) y la ecuación ($\ref{eqn:x_exp}$) anterior, se cumple lo siguiente:

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> En el proceso de ($\ref{eqn:dx/dt_1}$) a ($\ref{eqn:dx/dt_2}$) y de ($\ref{eqn:dx/dt_2}$) a ($\ref{eqn:dx/dt_3}$), se aplicó la integración por partes dos veces, y se descartaron los términos de frontera (boundary terms) ya que $\lim_{x\rightarrow\pm\infty}\Psi=0$.
{: .prompt-tip }

Por lo tanto, obtenemos el valor esperado del **momento** de la siguiente manera:

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Valor esperado para una cantidad física arbitraria $Q(x,p)$
Las expresiones para $\langle x \rangle$ y $\langle p \rangle$ que obtuvimos anteriormente se pueden escribir de la siguiente forma:

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

El operador $\hat x \equiv x$ representa la posición, y el operador $\hat p \equiv -i\hbar(\partial/\partial x)$ representa el momento. En el caso del operador de momento $\hat p$, al extenderlo al espacio tridimensional, se puede definir como $\hat p \equiv -i\hbar\nabla$.

Como todas las variables de la mecánica clásica se pueden expresar en términos de posición y momento, esto se puede extender al valor esperado de cualquier cantidad física. Para calcular el valor esperado de una cantidad arbitraria $Q(x,p)$, se reemplaza toda $p$ por $-i\hbar\nabla$, y se integra el operador resultante entre $\Psi^*$ y $\Psi$.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

Por ejemplo, como la energía cinética es $T=\cfrac{p^2}{2m}$,

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

A través de la ecuación ($\ref{eqn:Q_exp}$), podemos calcular el valor esperado de cualquier cantidad física para una partícula en el estado $\Psi$.

## Teorema de Ehrenfest
### Cálculo de $d\langle p \rangle/dt$
Derivemos ambos lados de la ecuación ($\ref{eqn:p_op}$) con respecto al tiempo $t$ para obtener la derivada temporal del valor esperado del momento $\cfrac{d\langle p \rangle}{dt}$.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> Se puede obtener la ecuación ($\ref{eqn:dp/dt_2}$) sustituyendo las ecuaciones (6) y (7) de [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/) en la ecuación ($\ref{eqn:dp/dt_1}$). En el proceso de ($\ref{eqn:dp/dt_3}$) a ($\ref{eqn:dp/dt_4}$), se aplicó la integración por partes y, como antes, se descartaron los términos de frontera (boundary terms) ya que $\lim_{x\rightarrow\pm\infty}\Psi=0$.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Relación entre el teorema de Ehrenfest y la segunda ley del movimiento de Newton
Las siguientes dos ecuaciones que obtuvimos anteriormente se conocen como el teorema de Ehrenfest:

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

El teorema de Ehrenfest tiene una forma muy similar a la relación entre la energía potencial y la fuerza conservativa en la mecánica clásica, $F=\cfrac{dp}{dt}=-\nabla V$.  
Comparemos las dos ecuaciones lado a lado:

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Teorema de Ehrenfest]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Segunda ley del movimiento de Newton]}$$

Si expandimos en serie de Taylor el lado derecho de la segunda ecuación del teorema de Ehrenfest $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (ecuación [$\ref{eqn:ehrenfest_theorem_2nd}$]) alrededor de $\langle x \rangle$ con respecto a $x$, obtenemos:

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

Si $x-\langle x \rangle$ es lo suficientemente pequeño, podemos ignorar todos los términos de orden superior excepto el primero y aproximar:

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

Es decir, **si la función de onda de una partícula tiene una distribución espacial muy concentrada cerca de un punto (si la dispersión de $\|\Psi\|^2$ con respecto a $x$ es muy pequeña), el teorema de Ehrenfest se puede aproximar a la segunda ley del movimiento de Newton de la mecánica clásica.** A escala macroscópica, podemos ignorar la extensión espacial de la función de onda y considerar la posición de la partícula esencialmente como un punto, por lo que se cumple la segunda ley del movimiento de Newton. Sin embargo, a escala microscópica, los efectos cuánticos no se pueden ignorar, por lo que la segunda ley del movimiento de Newton ya no se cumple y debemos utilizar el teorema de Ehrenfest.
