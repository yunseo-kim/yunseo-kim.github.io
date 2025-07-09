---
title: "EDO Lineal Homogénea de 2º Orden con Coeficientes Constantes"
description: "Se examina la forma de la solución general de una EDO lineal homogénea con coeficientes constantes para cada caso, según el signo del discriminante de la ecuación característica."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - EDO lineal homogénea de segundo orden con coeficientes constantes: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Ecuación característica**: $\lambda^2 + a\lambda + b = 0$
> - Dependiendo del signo del discriminante $a^2 - 4b$ de la ecuación característica, la forma de la solución general se puede dividir en tres casos, como se muestra en la tabla:
>
> | Caso | Raíces de la ecuación característica | Base de soluciones de la EDO | Solución general de la EDO |
> | :---: | :---: | :---: | :---: |
> | I | Dos raíces reales distintas<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Una raíz real doble<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Raíces complejas conjugadas<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prerrequisitos
- [Ecuación de Bernoulli](/posts/Bernoulli-Equation/)
- [EDOs Lineales Homogéneas de Segundo Orden](/posts/homogeneous-linear-odes-of-second-order/)
- Fórmula de Euler

## Ecuación Característica
Consideremos la EDO lineal homogénea de segundo orden con coeficientes constantes $a$ y $b$

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Este tipo de ecuación tiene aplicaciones importantes en las vibraciones mecánicas y eléctricas.

Anteriormente, en el artículo sobre la [Ecuación de Bernoulli](/posts/Bernoulli-Equation/), obtuvimos la solución general de la ecuación logística. Según ese resultado, la solución de la EDO lineal de primer orden con coeficiente constante $k$

$$ y^\prime + ky = 0 $$

es la función exponencial $y = ce^{-kx}$. (el caso donde $A=-k$ y $B=0$ en la ecuación (4) de dicho artículo)

Por lo tanto, para la ecuación ($\ref{eqn:ode_with_constant_coefficients}$), que tiene una forma similar, podemos intentar primero una solución de la forma

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Por supuesto, esto es solo una conjetura, y no hay garantía de que la solución general realmente tenga esta forma. Sin embargo, si logramos encontrar dos soluciones linealmente independientes, sin importar cuáles sean, podemos obtener la solución general mediante el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición), como vimos en el artículo sobre [EDOs Lineales Homogéneas de Segundo Orden](/posts/homogeneous-linear-odes-of-second-order/#base-y-solución-general).  
> Como veremos en breve, también hay casos en los que necesitamos encontrar [una solución de forma diferente](#ii-una-raíz-real-doble-lambda--cfraca2).
{: .prompt-info }

Sustituyendo la ecuación ($\ref{eqn:general_sol}$) y sus derivadas

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

en la ecuación ($\ref{eqn:ode_with_constant_coefficients}$), obtenemos

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Por lo tanto, si $\lambda$ es una raíz de la **ecuación característica**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

entonces la función exponencial ($\ref{eqn:general_sol}$) es una solución de la EDO ($\ref{eqn:ode_with_constant_coefficients}$). Resolviendo la ecuación cuadrática ($\ref{eqn:characteristic_eqn}$), obtenemos las raíces

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

y de esto se deduce que las dos funciones

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

son soluciones de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$).

> Los términos **ecuación característica** y **ecuación auxiliar** a menudo se usan indistintamente; significan exactamente lo mismo. Se puede usar cualquiera de los dos.
{: .prompt-tip }

Ahora, podemos dividir el problema en tres casos según el signo del discriminante $a^2 - 4b$ de la ecuación característica ($\ref{eqn:characteristic_eqn}$).
- $a^2 - 4b > 0$: Dos raíces reales distintas
- $a^2 - 4b = 0$: Una raíz real doble
- $a^2 - 4b < 0$: Raíces complejas conjugadas

## Forma de la Solución General según el Signo del Discriminante
### I. Dos raíces reales distintas $\lambda_1$ y $\lambda_2$
En este caso, una base de soluciones para la ecuación ($\ref{eqn:ode_with_constant_coefficients}$) en cualquier intervalo es

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

y la solución general correspondiente es

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Una raíz real doble $\lambda = -\cfrac{a}{2}$
Si $a^2 - 4b = 0$, la ecuación cuadrática ($\ref{eqn:characteristic_eqn}$) tiene solo una raíz, $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$. Por lo tanto, la única solución de la forma $y = e^{\lambda x}$ que obtenemos es

$$ y_1 = e^{-(a/2)x} $$

Para obtener una base, necesitamos encontrar una segunda solución $y_2$ que sea linealmente independiente de $y_1$. 

En esta situación, podemos utilizar el método de [reducción de orden](/posts/homogeneous-linear-odes-of-second-order/#reducción-de-orden) que vimos anteriormente. Si establecemos la segunda solución que buscamos como $y_2=uy_1$ y sustituimos

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

en la ecuación ($\ref{eqn:ode_with_constant_coefficients}$), obtenemos

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Agrupando los términos por $u^{\prime\prime}$, $u^\prime$ y $u$, y reorganizando, obtenemos

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Aquí, como $y_1$ es una solución de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$), la expresión en el último paréntesis es $0$. Además, como

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

la expresión en el primer paréntesis también es $0$. Por lo tanto, solo queda $u^{\prime\prime}y_1 = 0$, de lo cual se deduce que $u^{\prime\prime}=0$. Integrando dos veces, obtenemos $u = c_1x + c_2$. Como las constantes de integración $c_1$ y $c_2$ pueden ser cualquier valor, podemos simplemente elegir $c_1=1$ y $c_2=0$ para establecer $u=x$. Entonces, $y_2 = uy_1 = xy_1$. Como $y_1$ y $y_2$ son linealmente independientes, forman una base. Por lo tanto, cuando la ecuación característica ($\ref{eqn:characteristic_eqn}$) tiene una raíz doble, una base de soluciones para la ecuación ($\ref{eqn:ode_with_constant_coefficients}$) en cualquier intervalo es

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

y la solución general correspondiente es

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Raíces complejas conjugadas $-\cfrac{1}{2}a + i\omega$ y $-\cfrac{1}{2}a - i\omega$
En este caso, $a^2 - 4b < 0$. Usando $\sqrt{-1} = i$, la ecuación ($\ref{eqn:lambdas}$) nos da

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

donde definimos el número real $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Con $\omega$ definido como arriba, las raíces de la ecuación característica ($\ref{eqn:characteristic_eqn}$) son las raíces complejas conjugadas $\lambda = -\cfrac{1}{2}a \pm i\omega$. Esto nos da dos soluciones complejas para la ecuación ($\ref{eqn:ode_with_constant_coefficients}$)

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Sin embargo, en este caso también podemos obtener una base de soluciones reales de la siguiente manera.

A partir de la fórmula de Euler

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

y la ecuación obtenida al sustituir $-t$ por $t$ en la fórmula anterior

$$ e^{-it} = \cos t - i\sin t $$

podemos sumar y restar las dos ecuaciones para obtener lo siguiente.

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

La función exponencial compleja $e^z$ para una variable compleja $z = r + it$ con parte real $r$ y parte imaginaria $it$ se puede definir utilizando las funciones reales $e^r$, $\cos t$ y $\sin t$ de la siguiente manera.

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Aquí, si establecemos $r=-\cfrac{1}{2}ax$ y $t=\omega x$, podemos escribir:

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición), la suma y los múltiplos constantes de estas soluciones complejas también son soluciones. Por lo tanto, sumando las dos ecuaciones y multiplicando ambos lados por $\cfrac{1}{2}$, podemos obtener la primera solución real $y_1$ de la siguiente manera.

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Del mismo modo, restando la segunda ecuación de la primera y multiplicando ambos lados por $\cfrac{1}{2i}$, podemos obtener la segunda solución real $y_2$.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Dado que $\cfrac{y_1}{y_2} = \cot{\omega x}$, que no es una constante, $y_1$ y $y_2$ son linealmente independientes en cualquier intervalo y, por lo tanto, forman una base de soluciones reales para la ecuación ($\ref{eqn:ode_with_constant_coefficients}$). A partir de esto, obtenemos la solución general

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ son constantes arbitrarias)} \label{eqn:general_sol_3}\tag{13}$$


