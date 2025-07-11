---
title: "EDOs Lineales No Homogéneas de Segundo Orden (Nonhomogeneous Linear ODEs of Second Order)"
description: "Se examina la forma de la solución general de las EDOs lineales no homogéneas de segundo orden, centrándose en su relación con las soluciones de las ecuaciones diferenciales lineales homogéneas correspondientes, y se demuestra la existencia de la solución general y la no existencia de soluciones singulares."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Solución general** de la EDO lineal no homogénea de segundo orden $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: solución general de la EDO homogénea $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ → $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: solución particular de la EDO no homogénea correspondiente
> - El término de respuesta $y_p$ está determinado únicamente por la entrada $r(x)$, y para la misma EDO no homogénea, $y_p$ no cambia aunque cambien las condiciones iniciales. La diferencia entre dos soluciones particulares de la EDO no homogénea se convierte en una solución de la EDO homogénea correspondiente.
> - **Existencia de la solución general**: Si los coeficientes $p(x)$, $q(x)$ de la EDO no homogénea y la función de entrada $r(x)$ son continuas, siempre existe una solución general
> - **No existencia de soluciones singulares**: La solución general incluye todas las soluciones de la ecuación (es decir, no existen soluciones singulares)
{: .prompt-info }

## Prerrequisitos
- [EDOs lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskiano, existencia y unicidad de soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## Solución general y solución particular de EDOs lineales no homogéneas de segundo orden
Consideremos la EDO lineal no homogénea de segundo orden

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

donde $r(x) \not\equiv 0$. La **solución general** de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en un intervalo abierto $I$ tiene la forma de la suma de la solución general $y_h = c_1y_1 + c_2y_2$ de la EDO homogénea correspondiente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

y una solución particular $y_p$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$)

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Además, una **solución particular** de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ es una solución obtenida de la ecuación ($\ref{eqn:general_sol}$) asignando valores específicos a las constantes arbitrarias $c_1$ y $c_2$ de $y_h$.

Es decir, cuando se añade una entrada $r(x)$ que depende únicamente de la variable independiente $x$ a la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$), se añade un término correspondiente $y_p$ a la respuesta, y este término de respuesta añadido $y_p$ está determinado únicamente por la entrada $r(x)$, independientemente de las condiciones iniciales. Como veremos más adelante, si calculamos la diferencia entre dos soluciones arbitrarias $y_1$ e $y_2$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) (es decir, la diferencia entre las soluciones particulares respectivas para dos condiciones iniciales diferentes), la parte $y_p$ independiente de las condiciones iniciales se cancela, quedando solo la diferencia entre ${y_h}\_1$ e ${y_h}\_2$, que por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición) se convierte en una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode}$).

## Relación entre las soluciones de la EDO no homogénea y las soluciones de la EDO homogénea correspondiente
> **Teorema 1: Relación entre las soluciones de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) y las soluciones de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** La suma de una solución $y$ de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) y una solución $\tilde{y}$ de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) en algún intervalo abierto $I$ es una solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$. En particular, la ecuación ($\ref{eqn:general_sol}$) es una solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$.  
> **(b)** La diferencia entre dos soluciones de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ es una solución de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$.
{: .prompt-info }

### Demostración
#### (a)
Denotemos el lado izquierdo de las ecuaciones ($\ref{eqn:nonhomogeneous_linear_ode}$) y ($\ref{eqn:homogeneous_linear_ode}$) como $L[y]$. Entonces, para cualquier solución $y$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) y cualquier solución $\tilde{y}$ de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$, se satisface lo siguiente:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
Para dos soluciones arbitrarias $y$ e $y^\*$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$, se satisface lo siguiente:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## La solución general de la EDO no homogénea incluye todas las soluciones
Sabemos que [la solución general de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) incluye todas las soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/#no-existencia-de-soluciones-singulares). Demostremos que lo mismo se cumple para la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Teorema 2: La solución general de la EDO no homogénea incluye todas las soluciones**  
> Si los coeficientes $p(x)$, $q(x)$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) y la función de entrada $r(x)$ son continuas en algún intervalo abierto $I$, entonces todas las soluciones de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$ se pueden obtener asignando valores apropiados a las constantes arbitrarias $c_1$ y $c_2$ de $y_h$ en la solución general ($\ref{eqn:general_sol}$) de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$.
{: .prompt-info }

### Demostración
Sea $y^\*$ alguna solución de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en $I$, y sea $x_0$ algún $x$ dentro del intervalo $I$. Por el [teorema de existencia de la solución general para EDOs homogéneas con coeficientes variables continuos](/posts/wronskian-existence-and-uniqueness-of-solutions/#existencia-de-la-solución-general), existe $y_h = c_1y_1 + c_2y_2$, y por el **método de variación de parámetros** que estudiaremos más adelante, también existe $y_p$, por lo que existe la solución general ($\ref{eqn:general_sol}$) de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) en el intervalo $I$. Ahora, por el teorema [1(b)](#relación-entre-las-soluciones-de-la-edo-no-homogénea-y-las-soluciones-de-la-edo-homogénea-correspondiente) demostrado anteriormente, $Y = y^\* - y_p$ es una solución de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$, y en $x_0$

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

Por el [teorema de existencia y unicidad de soluciones del problema de valor inicial](/posts/wronskian-existence-and-uniqueness-of-solutions/#teorema-de-existencia-y-unicidad-de-soluciones-del-problema-de-valor-inicial), existe de manera única una solución particular $Y$ de la EDO homogénea ($\ref{eqn:homogeneous_linear_ode}$) que se puede obtener asignando valores apropiados a $c_1$, $c_2$ de $y_h$ para las condiciones iniciales anteriores en el intervalo $I$. Como $y^\* = Y + y_p$, hemos demostrado que cualquier solución particular $y^\*$ de la EDO no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$) se puede obtener de la solución general ($\ref{eqn:general_sol}$). $\blacksquare$
