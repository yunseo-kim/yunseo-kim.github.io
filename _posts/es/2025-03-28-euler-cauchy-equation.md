---
title: Ecuación de Euler-Cauchy
description: Examinamos cómo la forma de la solución general de la ecuación de Euler-Cauchy varía según el signo del discriminante de la ecuación auxiliar.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - Ecuación de Euler-Cauchy: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Ecuación auxiliar**: $m^2 + (a-1)m + b = 0$
> - Según el signo del discriminante de la ecuación auxiliar $(1-a)^2 - 4b$, la forma de la solución general se puede clasificar en tres casos como se muestra en la tabla
>
> | Caso | Soluciones de la ecuación auxiliar | Base de soluciones de la ecuación de Euler-Cauchy | Solución general de la ecuación de Euler-Cauchy |
> | :---: | :---: | :---: | :---: |
> | I | Raíces reales distintas<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Raíz real doble<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Raíces complejas conjugadas<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerequisites
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Fórmula de Euler

## Ecuación auxiliar
La **ecuación de Euler-Cauchy** es una ecuación diferencial ordinaria de la forma

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

donde $a$ y $b$ son constantes dadas y $y(x)$ es la función desconocida. Si sustituimos en la ecuación ($\ref{eqn:euler_cauchy_eqn}$)

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

obtenemos

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

es decir

$$ [m(m-1) + am + b]x^m = 0 $$

De aquí obtenemos la ecuación auxiliar

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

y la condición necesaria y suficiente para que $y=x^m$ sea una solución de la ecuación de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) es que $m$ sea una solución de la ecuación auxiliar ($\ref{eqn:auxiliary_eqn}$).

Resolviendo la ecuación cuadrática ($\ref{eqn:auxiliary_eqn}$), obtenemos

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

y de aquí, las dos funciones

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

son soluciones de la ecuación ($\ref{eqn:euler_cauchy_eqn}$).

Al igual que en [ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), podemos dividir los casos en tres según el signo del discriminante $(1-a)^2 - 4b$ de la ecuación auxiliar ($\ref{eqn:auxiliary_eqn}$):
- $(1-a)^2 - 4b > 0$: dos raíces reales distintas
- $(1-a)^2 - 4b = 0$: una raíz real doble
- $(1-a)^2 - 4b < 0$: raíces complejas conjugadas

## Forma de la solución general según el signo del discriminante de la ecuación auxiliar
### I. Dos raíces reales distintas $m_1$ y $m_2$
En este caso, la base de soluciones de la ecuación ($\ref{eqn:euler_cauchy_eqn}$) en cualquier intervalo es

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

y la solución general correspondiente es

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Raíz real doble $m = \cfrac{1-a}{2}$
Cuando $(1-a)^2 - 4b = 0$, es decir, $b=\cfrac{(1-a)^2}{4}$, la ecuación cuadrática ($\ref{eqn:auxiliary_eqn}$) tiene una única solución $m = m_1 = m_2 = \cfrac{1-a}{2}$, y por lo tanto, la única solución de la forma $y = x^m$ que podemos obtener es

$$ y_1 = x^{(1-a)/2} $$

y la ecuación de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) toma la forma

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Ahora, encontremos otra solución linealmente independiente $y_2$ utilizando el [método de reducción de orden](/posts/homogeneous-linear-odes-of-second-order/#reducción-de-orden).

Si ponemos la segunda solución buscada como $y_2=uy_1$, obtenemos

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Como $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$, tenemos

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

y al integrar obtenemos $u = \ln x$.

Por lo tanto, $y_2 = uy_1 = y_1 \ln x$, y $y_1$ y $y_2$ son linealmente independientes ya que su cociente no es constante. La solución general correspondiente a la base $y_1$ y $y_2$ es

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Raíces complejas conjugadas
En este caso, las soluciones de la ecuación auxiliar ($\ref{eqn:auxiliary_eqn}$) son $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, y las dos soluciones complejas correspondientes de la ecuación ($\ref{eqn:euler_cauchy_eqn}$) se pueden escribir, utilizando que $x=e^{\ln x}$, como:

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Si ponemos $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ y utilizamos la fórmula de Euler $e^{it} = \cos{t} + i\sin{t}$, obtenemos

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

y de aquí obtenemos las dos soluciones reales

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Como su cociente $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ no es constante, estas dos soluciones son linealmente independientes y, por lo tanto, por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición), forman una base para las soluciones de la ecuación de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$). De aquí obtenemos la siguiente solución general real:

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Sin embargo, el caso en que la ecuación auxiliar de la ecuación de Euler-Cauchy tiene raíces complejas conjugadas no tiene tanta importancia práctica.
