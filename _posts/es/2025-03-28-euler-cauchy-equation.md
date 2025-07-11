---
title: "Ecuación de Euler-Cauchy"
description: "Se examina la forma que toma la solución general de la ecuación de Euler-Cauchy en cada caso, según el signo del discriminante de la ecuación auxiliar."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Ecuación de Euler-Cauchy: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Ecuación auxiliar**: $m^2 + (a-1)m + b = 0$
> - Según el signo del discriminante $(1-a)^2 - 4b$ de la ecuación auxiliar, la forma de la solución general se puede dividir en tres casos como se muestra en la tabla
>
> | Caso | Raíces de la ecuación auxiliar | Base de soluciones de la ecuación de Euler-Cauchy | Solución general de la ecuación de Euler-Cauchy |
> | :---: | :---: | :---: | :---: |
> | I | Raíces reales distintas<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Raíz real doble<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Raíces complejas conjugadas<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerrequisitos
- [EDOs Lineales Homogéneas de Segundo Orden](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Fórmula de Euler

## Ecuación auxiliar
La **ecuación de Euler-Cauchy** es una ecuación diferencial ordinaria de la forma

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

con constantes dadas $a$ y $b$, y función incógnita $y(x)$. Sustituyendo en la ecuación ($\ref{eqn:euler_cauchy_eqn}$)

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

obtenemos

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

es decir

$$ [m(m-1) + am + b]x^m = 0 $$

De esto obtenemos la ecuación auxiliar

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

y la condición necesaria y suficiente para que $y=x^m$ sea solución de la ecuación de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) es que $m$ sea solución de la ecuación auxiliar ($\ref{eqn:auxiliary_eqn}$).

Resolviendo la ecuación cuadrática ($\ref{eqn:auxiliary_eqn}$) obtenemos

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

y de esto, las dos funciones

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

son soluciones de la ecuación ($\ref{eqn:euler_cauchy_eqn}$).

Al igual que en las [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), podemos dividir en tres casos según el signo del discriminante $(1-a)^2 - 4b$ de la ecuación auxiliar ($\ref{eqn:auxiliary_eqn}$).
- $(1-a)^2 - 4b > 0$: dos raíces reales distintas
- $(1-a)^2 - 4b = 0$: raíz real doble
- $(1-a)^2 - 4b < 0$: raíces complejas conjugadas

## Forma de la solución general según el signo del discriminante de la ecuación auxiliar
### I. Dos raíces reales distintas $m_1$ y $m_2$
En este caso, la base de soluciones de la ecuación ($\ref{eqn:euler_cauchy_eqn}$) en cualquier intervalo es

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

y la solución general correspondiente es

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Raíz real doble $m = \cfrac{1-a}{2}$
Cuando $(1-a)^2 - 4b = 0$, es decir, $b=\cfrac{(1-a)^2}{4}$, la ecuación cuadrática ($\ref{eqn:auxiliary_eqn}$) tiene una sola solución $m = m_1 = m_2 = \cfrac{1-a}{2}$, por lo que la única solución de la forma $y = x^m$ que podemos obtener es

$$ y_1 = x^{(1-a)/2} $$

y la ecuación de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) toma la forma

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Ahora encontremos otra solución $y_2$ linealmente independiente usando [reducción de orden](/posts/homogeneous-linear-odes-of-second-order/#reducción-de-orden).

Poniendo la segunda solución que buscamos como $y_2=uy_1$, obtenemos

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Como $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

e integrando obtenemos $u = \ln x$.

Por lo tanto, $y_2 = uy_1 = y_1 \ln x$, y como $y_1$ y $y_2$ tienen un cociente que no es constante, son linealmente independientes. La solución general correspondiente a la base $y_1$ y $y_2$ es

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Raíces complejas conjugadas
En este caso, las soluciones de la ecuación auxiliar ($\ref{eqn:auxiliary_eqn}$) son $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, y las dos soluciones complejas correspondientes de la ecuación ($\ref{eqn:euler_cauchy_eqn}$) se pueden escribir usando $x=e^{\ln x}$ como sigue:

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Poniendo $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ y usando la fórmula de Euler $e^{it} = \cos{t} + i\sin{t}$, obtenemos

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

y de esto obtenemos las siguientes dos soluciones reales

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Como el cociente de estas soluciones, $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$, no es constante, las dos soluciones anteriores son linealmente independientes y por tanto forman una base de la ecuación de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición). De esto obtenemos la siguiente solución general real:

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Sin embargo, el caso en que la ecuación auxiliar de la ecuación de Euler-Cauchy tiene raíces complejas conjugadas no tiene gran importancia práctica.

## Transformación a EDO lineal homogénea de segundo orden con coeficientes constantes
La ecuación de Euler-Cauchy se puede transformar en una [EDO lineal homogénea de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) mediante sustitución de variables.

Sustituyendo $x = e^t$, obtenemos

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

por lo que la ecuación de Euler-Cauchy ($\ref{eqn:euler_cauchy_eqn}$) se convierte en la siguiente EDO lineal homogénea con coeficientes constantes en $t$:

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

Resolviendo la ecuación ($\ref{eqn:substituted}$) con respecto a $t$ aplicando el método de [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), y luego transformando la solución obtenida de nuevo a una solución con respecto a $x$ usando $t = \ln{x}$, obtenemos [el mismo resultado que examinamos anteriormente](#forma-de-la-solución-general-según-el-signo-del-discriminante-de-la-ecuación-auxiliar).
