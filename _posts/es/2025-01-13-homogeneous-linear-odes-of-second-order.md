---
title: Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden
description: Exploramos la definición y características de las ecuaciones diferenciales ordinarias lineales de segundo orden, enfocándonos en el principio de superposición y el concepto de base para ecuaciones homogéneas.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Forma estándar** de una ecuación diferencial ordinaria lineal de segundo orden: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coeficientes**: funciones $p$, $q$
>   - **Entrada**: $r(x)$
>   - **Salida** o **respuesta**: $y(x)$
> - Homogénea y no homogénea
>   - **Homogénea**: cuando $r(x)\equiv0$ en la forma estándar
>   - **No homogénea**: cuando $r(x)\not\equiv 0$ en la forma estándar
> - **Principio de superposición**: Para una ecuación diferencial ordinaria lineal homogénea $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, cualquier combinación lineal de dos soluciones en un intervalo abierto $I$ es también una solución de la ecuación dada. Es decir, la suma y el producto por una constante de cualquier solución de la ecuación diferencial ordinaria lineal homogénea dada también son soluciones de dicha ecuación.
> - **Base** o **sistema fundamental**: Un par de soluciones $(y_1, y_2)$ linealmente independientes en el intervalo $I$ de la ecuación diferencial ordinaria lineal homogénea
> - **Reducción de orden**: Si se puede encontrar una solución para una ecuación diferencial ordinaria homogénea de segundo orden, se puede encontrar una segunda solución linealmente independiente, es decir, una base, resolviendo una ecuación diferencial de primer orden
> - Aplicaciones de la reducción de orden: Una ecuación diferencial de segundo orden general $F(x, y, y^\prime, y^{\prime\prime})=0$, ya sea lineal o no lineal, puede reducirse a primer orden utilizando la reducción de orden en los siguientes casos:
>   - Cuando $y$ no aparece explícitamente
>   - Cuando $x$ no aparece explícitamente
>   - Cuando es lineal homogénea y ya se conoce una solución
{: .prompt-info }

## Prerrequisitos
- [Conceptos básicos de modelado](/posts/Basic-Concepts-of-Modeling/)
- [Separación de variables](/posts/Separation-of-Variables/)
- [Solución de ecuaciones diferenciales ordinarias lineales de primer orden](/posts/Solution-of-First-Order-Linear-ODE/)

## Ecuaciones diferenciales ordinarias lineales de segundo orden
Una ecuación diferencial de segundo orden es **lineal** si se puede escribir en la forma

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

y **no lineal** en caso contrario.

Cuando $p$, $q$, $r$ son funciones de $x$, esta ecuación es lineal en $y$ y sus derivadas.

La forma ($\ref{eqn:standard_form}$) se conoce como la **forma estándar** de una ecuación diferencial ordinaria lineal de segundo orden. Si el primer término de una ecuación diferencial ordinaria lineal de segundo orden dada es $f(x)y^{\prime\prime}$, se puede obtener la forma estándar dividiendo ambos lados de la ecuación por $f(x)$.

Las funciones $p$, $q$ se denominan **coeficientes**, $r(x)$ se llama **entrada**, y $y(x)$ es la **salida** o **respuesta** a la entrada y las condiciones iniciales.

### Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden
Sea $J$ el intervalo $a<x<b$ donde queremos resolver la ecuación ($\ref{eqn:standard_form}$). Si $r(x)\equiv 0$ en $J$ en la ecuación ($\ref{eqn:standard_form}$), tenemos

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

y se dice que es **homogénea**.

## Ecuaciones diferenciales ordinarias lineales no homogéneas
Si $r(x)\not\equiv 0$ en el intervalo $J$, se dice que es **no homogénea**.

## Principio de superposición

Una función de la forma

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ son constantes arbitrarias)}\tag{3}$$

se llama **combinación lineal** de $y_1$ y $y_2$.

En este caso, se cumple lo siguiente:

> **Principio de superposición**
> Para una ecuación diferencial ordinaria lineal homogénea ($\ref{eqn:homogeneous_linear_ode}$), cualquier combinación lineal de dos soluciones en un intervalo abierto $I$ es también una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode}$). Es decir, la suma y el producto por una constante de cualquier solución de la ecuación diferencial ordinaria lineal homogénea dada también son soluciones de dicha ecuación.
{: .prompt-info }

### Demostración
Supongamos que $y_1$ y $y_2$ son soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$. Sustituyendo $y=c_1y_1+c_2y_2$ en la ecuación ($\ref{eqn:homogeneous_linear_ode}$):

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

se obtiene una identidad. Por lo tanto, $y$ es una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$. $\blacksquare$

> Hay que tener en cuenta que el principio de superposición solo se aplica a ecuaciones diferenciales ordinarias lineales homogéneas, y no se cumple para ecuaciones diferenciales ordinarias lineales no homogéneas o no lineales.
{: .prompt-warning }

## Base y solución general
### Repaso de conceptos clave de ecuaciones diferenciales de primer orden
Como vimos anteriormente en [Conceptos básicos de modelado](/posts/Basic-Concepts-of-Modeling/), un problema de valor inicial para una ecuación diferencial de primer orden consiste en la ecuación diferencial y una condición inicial $y(x_0)=y_0$. La condición inicial es necesaria para determinar la constante arbitraria $c$ en la solución general de la ecuación diferencial dada, y la solución así determinada se llama solución particular. Ahora extendamos estos conceptos a ecuaciones diferenciales de segundo orden.

### Problema de valor inicial y condiciones iniciales
Un **problema de valor inicial** para la ecuación diferencial ordinaria lineal homogénea de segundo orden ($\ref{eqn:homogeneous_linear_ode}$) consiste en la ecuación diferencial dada ($\ref{eqn:homogeneous_linear_ode}$) y dos **condiciones iniciales**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Estas condiciones son necesarias para determinar las dos constantes arbitrarias $c_1$ y $c_2$ en la **solución general** de la ecuación diferencial

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Independencia lineal y dependencia lineal
Aquí, revisemos brevemente los conceptos de independencia lineal y dependencia lineal. Es necesario entender esto para definir la base más adelante.  
Si para dos funciones $y_1$ y $y_2$ definidas en un intervalo $I$, se cumple que

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ y }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

para todos los puntos del intervalo $I$, entonces se dice que estas dos funciones $y_1$ y $y_2$ son **linealmente independientes** en el intervalo $I$. En caso contrario, se dice que $y_1$ y $y_2$ son **linealmente dependientes**.

Si $y_1$ y $y_2$ son linealmente dependientes (es decir, si la proposición ($\ref{eqn:linearly_independent}$) no es verdadera), podemos dividir ambos lados de la ecuación en ($\ref{eqn:linearly_independent}$) por $k_1 \neq 0$ o $k_2 \neq 0$ para obtener

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{o} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

lo que muestra que $y_1$ y $y_2$ son proporcionales.

### Base, solución general, solución particular
Volviendo al tema, para que ($\ref{eqn:general_sol}$) sea la solución general, $y_1$ y $y_2$ deben ser soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) y al mismo tiempo ser linealmente independientes (no proporcionales entre sí) en el intervalo $I$. Un par $(y_1, y_2)$ de soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) que son linealmente independientes en el intervalo $I$ y satisfacen estas condiciones se llama **base** o **sistema fundamental** de soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$.

Al utilizar las condiciones iniciales para determinar las dos constantes $c_1$ y $c_2$ en la solución general ($\ref{eqn:general_sol}$), obtenemos una única solución que pasa por el punto $(x_0, K_0)$ y tiene una pendiente de tangente $K_1$ en ese punto. Esta se llama **solución particular** de la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode}$).

Si la ecuación ($\ref{eqn:homogeneous_linear_ode}$) es continua en un intervalo abierto $I$, siempre tiene una solución general, y esta solución general incluye todas las posibles soluciones particulares. Es decir, en este caso, la ecuación ($\ref{eqn:homogeneous_linear_ode}$) no tiene soluciones singulares que no se puedan obtener de la solución general.

## Reducción de orden
Si podemos encontrar una solución para una ecuación diferencial ordinaria homogénea de segundo orden, podemos encontrar una segunda solución linealmente independiente, es decir, una base, resolviendo una ecuación diferencial de primer orden de la siguiente manera. Este método se llama **reducción de orden**.

Consideremos una ecuación diferencial ordinaria lineal homogénea de segundo orden en forma estándar <u>con $y^{\prime\prime}$ en lugar de $f(x)y^{\prime\prime}$</u>:

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

Supongamos que conocemos una solución $y_1$ de esta ecuación en un intervalo abierto $I$.

Ahora, pongamos la segunda solución que buscamos como $y_2 = uy_1$, y

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Sustituyendo en la ecuación, obtenemos

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Agrupando los términos con $u^{\prime\prime}$, $u^{\prime}$, $u$, obtenemos

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Sin embargo, como $y_1$ es una solución de la ecuación dada, la expresión entre paréntesis del último término es 0, por lo que el término con $u$ desaparece, quedando una ecuación diferencial en $u^{\prime}$ y $u^{\prime\prime}$. Dividiendo ambos lados de esta ecuación diferencial restante por $y_1$ y poniendo $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$, obtenemos la siguiente ecuación diferencial de primer orden:

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

[Separando variables](/posts/Separation-of-Variables/) e integrando, obtenemos

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

y tomando la exponencial en ambos lados, finalmente obtenemos

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Como habíamos puesto $U=u^{\prime}$, tenemos que $u=\int U dx$, por lo que la segunda solución $y_2$ que buscábamos es

$$ y_2 = uy_1 = y_1 \int U dx $$

Como $\cfrac{y_2}{y_1} = u = \int U dx$ no puede ser constante mientras $U>0$, $y_1$ y $y_2$ forman una base de soluciones.

### Aplicaciones de la reducción de orden
Una ecuación diferencial de segundo orden general $F(x, y, y^\prime, y^{\prime\prime})=0$, ya sea lineal o no lineal, puede reducirse a primer orden utilizando la reducción de orden cuando $y$ no aparece explícitamente, cuando $x$ no aparece explícitamente, o como vimos antes, cuando es lineal homogénea y ya se conoce una solución.

#### Cuando $y$ no aparece explícitamente
En $F(x, y^\prime, y^{\prime\prime})=0$, poniendo $z=y^{\prime}$, se puede reducir a una ecuación diferencial de primer orden en $z$: $F(x, z, z^{\prime})$.

#### Cuando $x$ no aparece explícitamente
En $F(y, y^\prime, y^{\prime\prime})=0$, poniendo $z=y^{\prime}$, tenemos $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$, por lo que se puede reducir a una ecuación diferencial de primer orden en $z$ donde $y$ juega el papel de la variable independiente $x$: $F(y,z,z^\prime)$.
