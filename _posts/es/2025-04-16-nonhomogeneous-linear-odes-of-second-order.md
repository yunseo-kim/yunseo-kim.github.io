---
title: Ecuaciones diferenciales ordinarias lineales no homogéneas de segundo orden
description: Estudio de las ecuaciones diferenciales ordinarias lineales no homogéneas de segundo orden, su solución general como suma de la solución homogénea y una solución particular, y teoremas sobre la existencia y unicidad de soluciones.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Solución general** de una ecuación diferencial ordinaria lineal no homogénea de segundo orden $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: solución general de la ecuación homogénea $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, donde $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: solución particular de la ecuación no homogénea
> - El término de respuesta $y_p$ está determinado únicamente por la entrada $r(x)$ y no cambia con diferentes condiciones iniciales para la misma ecuación no homogénea. La diferencia entre dos soluciones particulares de la ecuación no homogénea es una solución de la ecuación homogénea correspondiente.
> - **Existencia de la solución general**: Si los coeficientes $p(x)$, $q(x)$ y la función de entrada $r(x)$ son continuos, siempre existe una solución general
> - **Inexistencia de soluciones singulares**: La solución general incluye todas las soluciones posibles (es decir, no existen soluciones singulares)
{: .prompt-info }

## Prerrequisitos
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskiano, existencia y unicidad de soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solución general y solución particular de ecuaciones diferenciales ordinarias lineales no homogéneas de segundo orden
Consideremos la ecuación diferencial ordinaria lineal no homogénea de segundo orden

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

donde $r(x) \not\equiv 0$. La **solución general** de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en un intervalo abierto $I$ es la suma de la solución general $y_h = c_1y_1 + c_2y_2$ de la ecuación homogénea correspondiente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

y una solución particular $y_p$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$):

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Una **solución particular** de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ se obtiene asignando valores específicos a las constantes arbitrarias $c_1$ y $c_2$ en $y_h$ de la ecuación ($\ref{eqn:general_sol}$).

En otras palabras, cuando añadimos una entrada $r(x)$ que solo depende de la variable independiente $x$ a la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$), se añade un término de respuesta correspondiente $y_p$ a la solución, y este término adicional $y_p$ está determinado únicamente por la entrada $r(x)$, independientemente de las condiciones iniciales. Como veremos más adelante, si calculamos la diferencia entre dos soluciones particulares $y_1$ e $y_2$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) (es decir, la diferencia entre soluciones para dos condiciones iniciales diferentes), el término $y_p$ independiente de las condiciones iniciales se cancela, dejando solo la diferencia entre ${y_h}_1$ y ${y_h}_2$, que por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición) es una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode}$).

## Relación entre las soluciones de la ecuación no homogénea y la ecuación homogénea correspondiente
> **Teorema 1: Relación entre las soluciones de la ecuación no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) y la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** La suma de cualquier solución $y$ de la ecuación no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) y cualquier solución $\tilde{y}$ de la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$) en un intervalo abierto $I$ es una solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$. En particular, la expresión ($\ref{eqn:general_sol}$) es una solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$.  
> **(b)** La diferencia entre dos soluciones cualesquiera de la ecuación no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ es una solución de la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$.
{: .prompt-info }

### Demostración
#### (a)
Denotemos el lado izquierdo de las ecuaciones ($\ref{eqn:nonhomogeneous_linear_ode}$) y ($\ref{eqn:homogeneous_linear_ode}$) como $L[y]$. Entonces, para cualquier solución $y$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) y cualquier solución $\tilde{y}$ de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$, tenemos:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Para dos soluciones cualesquiera $y$ e $y^\*$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$, tenemos:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## La solución general incluye todas las soluciones posibles
Sabemos que para la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$), [la solución general incluye todas las soluciones posibles](/posts/wronskian-existence-and-uniqueness-of-solutions/#la-solución-general-incluye-todas-las-soluciones). Demostremos que lo mismo se cumple para la ecuación no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Teorema 2: La solución general de la ecuación no homogénea incluye todas las soluciones posibles**  
> Si los coeficientes $p(x)$, $q(x)$ y la función de entrada $r(x)$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) son continuos en un intervalo abierto $I$, entonces cualquier solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ puede obtenerse asignando valores apropiados a las constantes arbitrarias $c_1$ y $c_2$ en $y_h$ de la solución general ($\ref{eqn:general_sol}$).
{: .prompt-info }

### Demostración
Sea $y^\*$ cualquier solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$, y sea $x_0$ cualquier punto en $I$. Por el [teorema de existencia de la solución general](/posts/wronskian-existence-and-uniqueness-of-solutions/#existencia-de-la-solución-general) para ecuaciones homogéneas con coeficientes continuos, existe $y_h = c_1y_1 + c_2y_2$, y por el método de variación de parámetros (que estudiaremos más adelante), también existe $y_p$, por lo que la solución general ($\ref{eqn:general_sol}$) de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) existe en el intervalo $I$. Ahora, por el teorema [1(b)](#relación-entre-las-soluciones-de-la-ecuación-no-homogénea-y-la-ecuación-homogénea-correspondiente) que acabamos de demostrar, $Y = y^\* - y_p$ es una solución de la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$, y en $x_0$:

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Por el [teorema de existencia y unicidad para problemas de valor inicial](/posts/wronskian-existence-and-uniqueness-of-solutions/#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial), existe una única solución particular $Y$ de la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$ que satisface estas condiciones iniciales, y esta solución puede obtenerse asignando valores apropiados a $c_1$ y $c_2$ en $y_h$. Como $y^\* = Y + y_p$, hemos demostrado que cualquier solución particular $y^\*$ de la ecuación no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) puede obtenerse a partir de la solución general ($\ref{eqn:general_sol}$). $\blacksquare$
