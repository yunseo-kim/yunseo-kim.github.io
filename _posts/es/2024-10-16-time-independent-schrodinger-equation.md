---
title: Ecuación de Schrödinger independiente del tiempo
description: Derivamos la ecuación de Schrödinger independiente del tiempo ψ(x) aplicando
  el método de separación de variables a la forma original de la ecuación de Schrödinger
  (dependiente del tiempo) Ψ(x,t). Exploramos el significado matemático y físico y
  la importancia de la solución separada obtenida. También examinamos cómo obtener
  la solución general de la ecuación de Schrödinger mediante la combinación lineal
  de soluciones separadas.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Solución separada: $ \Psi(x,t) = \psi(x)\phi(t)$
> - Dependencia temporal ("factor de oscilación"): $ \phi(t) = e^{-iEt/\hbar} $
> - Operador hamiltoniano: $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - Ecuación de Schrödinger independiente del tiempo: $ \hat H\psi = E\psi $
> - Significado físico y matemático e importancia de la solución separada:
>   1. Estados estacionarios
>   2. Tiene un valor de energía total $E$ bien definido
>   3. La solución general de la ecuación de Schrödinger es una combinación lineal de soluciones separadas
> - Solución general de la ecuación de Schrödinger dependiente del tiempo: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Prerequisites
- Distribuciones de probabilidad continua y densidad de probabilidad
- [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Teorema de Ehrenfest](/posts/ehrenfest-theorem/)
- [Método de separación de variables](/posts/Separation-of-Variables/)

## Derivación utilizando el método de separación de variables
En la publicación sobre [el teorema de Ehrenfest](/posts/ehrenfest-theorem/), vimos cómo calcular varias cantidades físicas utilizando la función de onda $\Psi$. Entonces, lo importante es cómo obtener esa función de onda $\Psi(x,t)$, y generalmente se debe resolver la [ecuación de Schrödinger](/posts/schrodinger-equation-and-the-wave-function/), que es una ecuación diferencial parcial en términos de la posición $x$ y el tiempo $t$ para un potencial dado $V(x,t)$.

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

Si el potencial $V$ es independiente del tiempo $t$, podemos resolver la ecuación de Schrödinger anterior utilizando el [método de separación de variables](/posts/Separation-of-Variables/). Consideremos una solución que se expresa como el producto de una función $\psi$ solo de $x$ y una función $\phi$ solo de $t$:

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

A primera vista, esto puede parecer una expresión excesivamente restrictiva y que solo podría obtener un pequeño subconjunto de la solución completa, pero de hecho, la solución obtenida de esta manera tiene un significado importante y podemos obtener la solución general sumando estas soluciones separables de una manera específica.

Para la solución separable,

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

se cumple, por lo que sustituyendo esto en la ecuación ($\ref{eqn:schrodinger_eqn}$), podemos escribir la ecuación de Schrödinger como:

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

Dividiendo ambos lados por $\psi\phi$, obtenemos

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

donde el lado izquierdo es una función solo de $t$ y el lado derecho es una función solo de $x$. Para que esta ecuación tenga solución, ambos lados deben ser constantes, porque si no lo fueran, al mantener constante una de las variables $t$ o $x$ y variar solo la otra, solo cambiaría un lado de la ecuación, haciendo que la igualdad ya no sea verdadera. Por lo tanto, podemos establecer el lado izquierdo igual a una constante de separación $E$.

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

Entonces obtenemos dos ecuaciones diferenciales ordinarias, una es 

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

que es la parte del tiempo $t$, y la otra es

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

que es la parte del espacio $x$.

La ecuación diferencial ordinaria ($\ref{eqn:ode_t}$) para $t$ se puede resolver fácilmente. Originalmente, la solución general de esta ecuación es $ce^{-iEt/\hbar}$, pero como lo que nos interesa es el producto $\psi\phi$ más que $\phi$ en sí mismo, podemos incluir la constante $c$ en $\psi$. Entonces obtenemos

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

La ecuación diferencial ordinaria ($\ref{eqn:t_independent_schrodinger_eqn}$) para $x$ se llama **ecuación de Schrödinger independiente del tiempo**. Esta ecuación solo se puede resolver si conocemos el potencial $V(x)$.

## Significado físico y matemático
Anteriormente, utilizando el método de separación de variables, obtuvimos la función $\phi(t)$ que depende solo del tiempo y la ecuación de Schrödinger independiente del tiempo ($\ref{eqn:t_independent_schrodinger_eqn}$). Aunque la mayoría de las soluciones de la **ecuación de Schrödinger dependiente del tiempo** original ($\ref{eqn:schrodinger_eqn}$) no se pueden expresar en la forma $\psi(x)\phi(t)$, la forma de la ecuación de Schrödinger independiente del tiempo sigue siendo importante debido a las siguientes tres propiedades que tiene su solución.

### 1. Son estados estacionarios.
Aunque la función de onda en sí misma

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

depende de $t$, la densidad de probabilidad

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

es constante e independiente del tiempo ya que la dependencia temporal se cancela.

> Para soluciones que se pueden normalizar, la constante de separación $E$ debe ser real.
>
> Si tomamos $E$ en la ecuación ($\ref{eqn:separation_of_variables}$) como un número complejo $E_0+i\Gamma$ (donde $E_0$ y $\Gamma$ son reales),
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> Como vimos anteriormente en [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/#normalización-de-la-función-de-onda), $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ debe ser una constante independiente del tiempo, por lo que $\Gamma=0$. $\blacksquare$
{: .prompt-info }

Lo mismo ocurre al calcular el valor esperado de cualquier cantidad física, por lo que la ecuación (8) del [teorema de Ehrenfest](/posts/ehrenfest-theorem/) se convierte en

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

y todos los valores esperados son constantes con respecto al tiempo. En particular, como $\langle x \rangle$ es constante, $\langle p \rangle=0$.

### 2. Es un estado con un valor de energía total $E$ bien definido, no una distribución de probabilidad con un rango.
En la mecánica clásica, la energía total (energía cinética y energía potencial) se llama **hamiltoniano** y se define como

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

Por lo tanto, si reemplazamos $p$ por $-i\hbar(\partial/\partial x)$, el operador hamiltoniano en mecánica cuántica corresponde a

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

Por lo tanto, la ecuación de Schrödinger independiente del tiempo ($\ref{eqn:t_independent_schrodinger_eqn}$) se puede escribir como

$$ \hat H \psi = E\psi \tag{15}$$

y el valor esperado del hamiltoniano es el siguiente:

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

Además, como

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

se cumple,

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

y por lo tanto, la varianza del hamiltoniano $H$ es

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

Es decir, la solución separada siempre mide un valor constante $E$ cuando se mide la energía total.

### 3. La solución general de la ecuación de Schrödinger dependiente del tiempo es una combinación lineal de soluciones separadas.

La ecuación de Schrödinger independiente del tiempo ($\ref{eqn:t_independent_schrodinger_eqn}$) tiene infinitas soluciones $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$. Llamemos a estas \{$\psi_n(x)$\}. Para cada una de ellas, existe una constante de separación $E_1,E_2,E_3,\dots=$\{$E_n$\}, por lo que hay una función de onda correspondiente para cada **nivel de energía posible**.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

La ecuación de Schrödinger dependiente del tiempo ($\ref{eqn:schrodinger_eqn}$) tiene la propiedad de que la combinación lineal de dos soluciones arbitrarias también es una solución, por lo que una vez que encontramos las soluciones separadas, inmediatamente podemos obtener una forma más general de solución:

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

Todas las soluciones de la ecuación de Schrödinger dependiente del tiempo se pueden escribir en esta forma, y ahora lo único que queda por hacer es encontrar las constantes apropiadas $c_1, c_2, \dots$ para satisfacer las condiciones iniciales dadas en el problema y encontrar la solución particular que estamos buscando. Es decir, una vez que podemos resolver la ecuación de Schrödinger independiente del tiempo, obtener la solución general de la ecuación de Schrödinger dependiente del tiempo es simple.

> La solución separada 
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> es un estado estacionario donde todas las probabilidades y valores esperados son independientes del tiempo, pero la solución general en la ecuación ($\ref{eqn:general_solution}$) no tiene esta propiedad.
{: .prompt-warning }

## Conservación de la energía
En la solución general ($\ref{eqn:general_solution}$), el cuadrado del valor absoluto de los coeficientes \{$c_n$\}, $\|c_n\|^2$, representa físicamente la probabilidad de medir el valor $E_n$ cuando se mide la energía de una partícula en ese estado ($\Psi$). Por lo tanto, la suma de estas probabilidades debe ser

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

igual a 1, y el valor esperado del hamiltoniano es

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

Aquí, como los niveles de energía $E_n$ de cada estado estacionario y los coeficientes \{$c_n$\} son independientes del tiempo, la probabilidad de medir una energía específica $E_n$ o el valor esperado del hamiltoniano $H$ también tienen un valor constante independiente del tiempo.
