---
title: "EDO lineal homogénea de segundo orden con coeficientes constantes"
description: "Se examina cómo la forma de la solución general de una ecuación diferencial ordinaria lineal homogénea con coeficientes constantes varía según el signo del discriminante de la ecuación característica en cada caso."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - EDO lineal homogénea de segundo orden con coeficientes constantes: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Ecuación característica**: $\lambda^2 + a\lambda + b = 0$
> - Según el signo del discriminante $a^2 - 4b$ de la ecuación característica, la forma de la solución general se puede dividir en tres casos como se muestra en la tabla
>
> | Caso | Raíces de la ecuación característica | Base de soluciones de la EDO | Solución general de la EDO |
> | :---: | :---: | :---: | :---: |
> | I | Raíces reales distintas<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Raíz real doble<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Raíces complejas conjugadas<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prerrequisitos
- [Ecuación de Bernoulli](/posts/Bernoulli-Equation/)
- [EDOs lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- Fórmula de Euler

## Ecuación característica
Consideremos la EDO lineal homogénea de segundo orden donde los coeficientes $a$ y $b$ son constantes

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

Este tipo de ecuación tiene importantes aplicaciones en vibraciones mecánicas y eléctricas.

Anteriormente, en la [Ecuación de Bernoulli](/posts/Bernoulli-Equation/), obtuvimos la solución general de la ecuación logística, y según eso, la EDO lineal de primer orden con coeficiente constante $k$

$$ y^\prime + ky = 0 $$

tiene como solución la función exponencial $y = ce^{-kx}$. (Caso donde $A=-k$, $B=0$ en la ecuación (4) de ese artículo)

Por lo tanto, para la ecuación ($\ref{eqn:ode_with_constant_coefficients}$) de forma similar, podemos intentar primero una solución de la forma

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Por supuesto, esto es solo una conjetura, y no hay garantía alguna de que la solución general tenga realmente esta forma. Sin embargo, si logramos encontrar dos soluciones linealmente independientes, como vimos en [EDOs lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/#base-y-solución-general), podemos obtener la solución general mediante el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición).  
> Como veremos en breve, [también hay casos donde debemos encontrar soluciones de otra forma](#ii-raíz-real-doble-lambda---cfraca2).
{: .prompt-info }

Sustituyendo la ecuación ($\ref{eqn:general_sol}$) y sus derivadas

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

en la ecuación ($\ref{eqn:ode_with_constant_coefficients}$), obtenemos

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Por lo tanto, si $\lambda$ es una solución de la **ecuación característica**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

entonces la función exponencial ($\ref{eqn:general_sol}$) es una solución de la EDO ($\ref{eqn:ode_with_constant_coefficients}$). Resolviendo la ecuación cuadrática ($\ref{eqn:characteristic_eqn}$), obtenemos

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

y de esto, las dos funciones

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

se convierten en soluciones de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$).

> Los términos **ecuación característica** y **ecuación auxiliar** se usan frecuentemente de manera intercambiable, y ambos tienen exactamente el mismo significado. Se puede usar cualquiera de los dos términos.
{: .prompt-tip }

Ahora, podemos dividir en tres casos según el signo del discriminante $a^2 - 4b$ de la ecuación característica ($\ref{eqn:characteristic_eqn}$).
- $a^2 - 4b > 0$: dos raíces reales distintas
- $a^2 - 4b = 0$: raíz real doble
- $a^2 - 4b < 0$: raíces complejas conjugadas

## Forma de la solución general según el signo del discriminante de la ecuación característica
### I. Dos raíces reales distintas $\lambda_1$ y $\lambda_2$
En este caso, la base de soluciones de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$) en cualquier intervalo es

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

y la solución general correspondiente es

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Raíz real doble $\lambda = -\cfrac{a}{2}$
Cuando $a^2 - 4b = 0$, la ecuación cuadrática ($\ref{eqn:characteristic_eqn}$) tiene solo una solución $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$, por lo que solo podemos obtener una solución de la forma $y = e^{\lambda x}$:

$$ y_1 = e^{-(a/2)x} $$

Para obtener una base, necesitamos encontrar una segunda solución $y_2$ independiente de $y_1$. 

En esta situación, podemos utilizar la [reducción de orden](/posts/homogeneous-linear-odes-of-second-order/#reducción-de-orden) que estudiamos anteriormente. Poniendo la segunda solución que buscamos como $y_2=uy_1$, y

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Sustituyendo en la ecuación ($\ref{eqn:ode_with_constant_coefficients}$), obtenemos

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Agrupando los términos de $u^{\prime\prime}$, $u^\prime$, $u$, obtenemos

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Aquí, como $y_1$ es una solución de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$), la expresión en el último paréntesis es $0$, y

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

por lo que la expresión en el primer paréntesis también es $0$. Por lo tanto, solo queda $u^{\prime\prime}y_1 = 0$, de donde $u^{\prime\prime}=0$. Integrando dos veces, obtenemos $u = c_1x + c_2$, y como las constantes de integración $c_1$ y $c_2$ pueden tomar cualquier valor, podemos simplemente elegir $c_1=1$, $c_2=0$ para poner $u=x$. Entonces $y_2 = uy_1 = xy_1$, y como $y_1$ y $y_2$ son linealmente independientes, forman una base. Por lo tanto, cuando la ecuación característica ($\ref{eqn:characteristic_eqn}$) tiene una raíz doble, la base de soluciones de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$) en cualquier intervalo es

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

y la solución general correspondiente es

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Raíces complejas conjugadas $-\cfrac{1}{2}a + i\omega$ y $-\cfrac{1}{2}a - i\omega$
En este caso, $a^2 - 4b < 0$ y $\sqrt{-1} = i$, por lo que en la ecuación ($\ref{eqn:lambdas}$)

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

y aquí definamos el número real $\sqrt{b-\cfrac{1}{4}a^2} = \omega$.

Con $\omega$ definido de esta manera, las soluciones de la ecuación característica ($\ref{eqn:characteristic_eqn}$) son las raíces complejas conjugadas $\lambda = -\cfrac{1}{2}a \pm i\omega$, y las dos soluciones complejas correspondientes de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$) son

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

Sin embargo, también en este caso podemos obtener una base de soluciones reales de la siguiente manera.

La fórmula de Euler

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

y sustituyendo $-t$ en lugar de $t$ en la ecuación anterior para obtener

$$ e^{-it} = \cos t - i\sin t $$

Sumando y restando estas dos ecuaciones, obtenemos lo siguiente.

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

La función exponencial compleja $e^z$ de una variable compleja $z = r + it$ con parte real $r$ y parte imaginaria $it$ se puede definir usando las funciones reales $e^r$, $\cos t$ y $\sin t$ de la siguiente manera.

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Aquí, poniendo $r=-\cfrac{1}{2}ax$, $t=\omega x$, podemos escribir lo siguiente.

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

Por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición), las sumas y productos por constantes de las soluciones complejas anteriores también son soluciones. Por lo tanto, sumando las dos ecuaciones y multiplicando ambos lados por $\cfrac{1}{2}$, podemos obtener la primera solución real $y_1$ de la siguiente manera.

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

De la misma manera, restando la segunda ecuación de la primera y multiplicando ambos lados por $\cfrac{1}{2i}$, podemos obtener la segunda solución real $y_2$.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Como $\cfrac{y_1}{y_2} = \cot{\omega x}$ y esto no es una constante, $y_1$ y $y_2$ son linealmente independientes en todos los intervalos y por lo tanto forman una base de soluciones reales de la ecuación ($\ref{eqn:ode_with_constant_coefficients}$). De esto obtenemos la solución general

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{ son constantes arbitrarias)} \label{eqn:general_sol_3}\tag{13}$$
