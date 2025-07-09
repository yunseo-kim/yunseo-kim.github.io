---
title: "EDOs Lineales no Homogéneas de Segundo Orden (Nonhomogeneous Linear ODEs of Second Order)"
description: "Se analiza la forma de la solución general de una EDO lineal no homogénea de segundo orden, su relación con la solución de la EDO homogénea correspondiente, y se demuestra la existencia de la solución general y la inexistencia de soluciones singulares."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Solución general** de una EDO lineal no homogénea de segundo orden $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: solución general $y_h = c_1y_1 + c_2y_2$ de la EDO homogénea $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$
>   - $y_p$: solución particular de la EDO no homogénea correspondiente
> - El término de respuesta $y_p$ está determinado únicamente por la entrada $r(x)$, y para la misma EDO no homogénea, $y_p$ no cambia aunque cambien las condiciones iniciales. La diferencia entre dos soluciones particulares de una EDO no homogénea es una solución de la EDO homogénea correspondiente.
> - **Existencia de la solución general**: Si los coeficientes $p(x)$, $q(x)$ y la función de entrada $r(x)$ de la EDO no homogénea son continuos, siempre existe una solución general.
> - **Inexistencia de soluciones singulares**: La solución general incluye todas las soluciones de la ecuación (es decir, no existen soluciones singulares).
{: .prompt-info }

## Prerrequisitos
- [EDOs Lineales Homogéneas de Segundo Orden (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [El Wronskiano, Existencia y Unicidad de Soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solución General y Particular de EDOs Lineales no Homogéneas de Segundo Orden
Consideremos la EDO lineal no homogénea de segundo orden

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

donde $r(x) \not\equiv 0$. En un intervalo abierto $I$, la **solución general** de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) es la suma de la solución general $y_h = c_1y_1 + c_2y_2$ de la EDO homogénea correspondiente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

y una solución particular $y_p$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$), con la forma

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Además, una **solución particular** de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ es una solución que se obtiene de la ecuación ($\ref{eqn:general_sol}$) asignando valores específicos a las constantes arbitrarias $c_1$ y $c_2$ de $y_h$.

Es decir, si a la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) se le añade una entrada $r(x)$ que depende solo de la variable independiente $x$, se añade un término correspondiente $y_p$ a la respuesta. Este término de respuesta añadido $y_p$ está determinado únicamente por la entrada $r(x)$, independientemente de las condiciones iniciales. Como veremos más adelante, si calculamos la diferencia entre dos soluciones cualesquiera $y_1$ y $y_2$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) (es decir, la diferencia entre dos soluciones particulares para dos condiciones iniciales diferentes), la parte $y_p$, que es independiente de las condiciones iniciales, se cancela, dejando solo la diferencia entre ${y_h}_1$ y ${y_h}_2$. Por el [Principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposicion), esta diferencia es una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode}$).

## Relación entre las soluciones de la EDO no homogénea y las de la EDO homogénea correspondiente
> **Teorema 1: Relación entre las soluciones de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) y las de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** La suma de una solución $y$ de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) y una solución $\tilde{y}$ de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) en un intervalo abierto $I$ es una solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$. En particular, la ecuación ($\ref{eqn:general_sol}$) es una solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$.  
> **(b)** La diferencia de dos soluciones de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) en un intervalo $I$ es una solución de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$.
{: .prompt-info }

### Demostración
#### (a)
Denotemos el lado izquierdo de las ecuaciones ($\ref{eqn:nonhomogeneous_linear_ode}$) y ($\ref{eqn:homogeneous_linear_ode}$) como $L[y]$. Entonces, para cualquier solución $y$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) y cualquier solución $\tilde{y}$ de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$, se cumple lo siguiente.

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Para dos soluciones cualesquiera $y$ y $y^\*$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$, se cumple lo siguiente.

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## La solución general de una EDO no homogénea incluye todas las soluciones
Para la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$), [sabemos que la solución general incluye todas las soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/#la-solucion-general-incluye-todas-las-soluciones). Demostremos que lo mismo se cumple para la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Teorema 2: La solución general de una EDO no homogénea incluye todas las soluciones**  
> Si los coeficientes $p(x)$, $q(x)$ y la función de entrada $r(x)$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) son continuos en un intervalo abierto $I$, entonces toda solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ puede obtenerse de la solución general ($\ref{eqn:general_sol}$) de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ asignando valores apropiados a las constantes arbitrarias $c_1$ y $c_2$ de $y_h$.
{: .prompt-info }

### Demostración
Sea $y^\*$ una solución cualquiera de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en $I$, y sea $x_0$ un punto cualquiera en el intervalo $I$. Por el [teorema de existencia de la solución general para EDOs homogéneas con coeficientes variables continuos](/posts/wronskian-existence-and-uniqueness-of-solutions/#existencia-de-la-solucion-general), existe $y_h = c_1y_1 + c_2y_2$, y por el **método de variación de parámetros**, que veremos más adelante, $y_p$ también existe, por lo que la solución general ($\ref{eqn:general_sol}$) de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) existe en el intervalo $I$. Ahora, por el Teorema [1(b)](#relación-entre-las-soluciones-de-la-edo-no-homogénea-y-las-de-la-edo-homogénea-correspondiente) que demostramos anteriormente, $Y = y^\* - y_p$ es una solución de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$, y en $x_0$

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

es cierto. Según el [Teorema de Existencia y Unicidad para Problemas de Valor Inicial](/posts/wronskian-existence-and-uniqueness-of-solutions/#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial), existe una única solución particular $Y$ de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) que se puede obtener asignando valores apropiados a $c_1$ y $c_2$ de $y_h$ para las condiciones iniciales anteriores en el intervalo $I$. Como $y^\* = Y + y_p$, hemos demostrado que cualquier solución particular $y^\*$ de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) puede obtenerse de la solución general ($\ref{eqn:general_sol}$). $\blacksquare$
