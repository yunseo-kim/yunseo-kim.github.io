---
title: "EDOs Lineales Homogéneas de Segundo Orden (Homogeneous Linear ODEs of Second Order)"
description: "Se explora la definición y características de las ecuaciones diferenciales ordinarias (EDOs) lineales de segundo orden. Se analiza el principio de superposición, un teorema clave para las EDOs lineales homogéneas, y el concepto de base asociado."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Forma estándar** de una EDO lineal de segundo orden: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coeficientes**: funciones $p$, $q$
>   - **Entrada (input)**: $r(x)$
>   - **Salida (output)** o **respuesta (response)**: $y(x)$
> - Homogénea y no homogénea
>   - **Homogénea**: si $r(x)\equiv0$ en la forma estándar.
>   - **No homogénea**: si $r(x)\not\equiv 0$ en la forma estándar.
> - **Principio de superposición**: Para una EDO lineal <u>homogénea</u> $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, cualquier combinación lineal de dos soluciones en un intervalo abierto $I$ es también una solución de la ecuación. Es decir, la suma y el producto por una constante de soluciones de la EDO lineal homogénea dada también son soluciones.
> - **Base** o **sistema fundamental**: Un par de soluciones $(y_1, y_2)$ de una EDO lineal homogénea que son linealmente independientes en un intervalo $I$.
> - **Reducción de orden**: Si se conoce una solución de una EDO homogénea de segundo orden, se puede encontrar una segunda solución linealmente independiente (es decir, una base) resolviendo una EDO de primer orden. Este método se llama reducción de orden.
> - Aplicaciones de la reducción de orden: Una EDO general de segundo orden $F(x, y, y^\prime, y^{\prime\prime})=0$, ya sea lineal o no lineal, puede reducirse a una de primer orden mediante la reducción de orden en los siguientes casos:
>   - Cuando $y$ no aparece explícitamente.
>   - Cuando $x$ no aparece explícitamente.
>   - Cuando es lineal homogénea y ya se conoce una solución.
{: .prompt-info }

## Prerrequisitos
- [Conceptos Básicos de Modelado](/posts/Basic-Concepts-of-Modeling/)
- [Separación de Variables](/posts/Separation-of-Variables/)
- [Solución de EDOs Lineales de Primer Orden](/posts/Solution-of-First-Order-Linear-ODE/)

## EDOs Lineales de Segundo Orden
Una EDO de segundo orden se denomina **lineal** si se puede escribir en la forma

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

y **no lineal** en caso contrario.

Cuando $p$, $q$ y $r$ son funciones de $x$, la ecuación es lineal con respecto a $y$ y sus derivadas.

La forma de la ecuación ($\ref{eqn:standard_form}$) se conoce como la **forma estándar** de una EDO lineal de segundo orden. Si el primer término de una EDO lineal de segundo orden dada es $f(x)y^{\prime\prime}$, se puede obtener la forma estándar dividiendo ambos lados de la ecuación por $f(x)$.

Las funciones $p$ y $q$ se denominan **coeficientes**, $r(x)$ es la **entrada (input)**, y $y(x)$ es la **salida (output)** o la **respuesta (response)** a la entrada y las condiciones iniciales.

### EDOs Lineales Homogéneas de Segundo Orden
Sea $J$ un intervalo $a<x<b$ en el que queremos resolver la ecuación ($\ref{eqn:standard_form}$). Si $r(x)\equiv 0$ en el intervalo $J$, la ecuación se convierte en

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

y se denomina **homogénea**.

## EDOs Lineales No Homogéneas
Si $r(x)\not\equiv 0$ en el intervalo $J$, la ecuación se denomina **no homogénea**.

## Principio de Superposición

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ son constantes arbitrarias)}\tag{3}$$

Una función de esta forma se llama **combinación lineal** de $y_1$ y $y_2$.

En este caso, se cumple lo siguiente:

> **Principio de superposición**  
> Para la EDO lineal homogénea ($\ref{eqn:homogeneous_linear_ode}$), cualquier combinación lineal de dos soluciones en un intervalo abierto $I$ es también una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode}$). Es decir, la suma y el producto por una constante de cualesquiera soluciones de la EDO lineal homogénea dada también son soluciones de dicha ecuación.
{: .prompt-info }

### Demostración
Sean $y_1$ y $y_2$ soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$. Sustituyendo $y=c_1y_1+c_2y_2$ en la ecuación ($\ref{eqn:homogeneous_linear_ode}$), obtenemos:

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

lo que resulta en una identidad. Por lo tanto, $y$ es una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$. $\blacksquare$

> Es importante tener en cuenta que el principio de superposición solo se aplica a las EDOs lineales homogéneas y no es válido para las EDOs lineales no homogéneas ni para las EDOs no lineales.
{: .prompt-warning }

## Base y Solución General
### Repaso de Conceptos Clave de EDOs de Primer Orden
Como vimos anteriormente en [Conceptos Básicos de Modelado](/posts/Basic-Concepts-of-Modeling/), un problema de valor inicial (PVI) para una EDO de primer orden consiste en la EDO y una condición inicial $y(x_0)=y_0$. La condición inicial es necesaria para determinar la constante arbitraria $c$ en la solución general de la EDO, y la solución así determinada se llama solución particular. Ahora, extendamos estos conceptos a las EDOs de segundo orden.

### Problema de Valor Inicial y Condiciones Iniciales
Un **problema de valor inicial (PVI)** para una EDO homogénea de segundo orden ($\ref{eqn:homogeneous_linear_ode}$) consiste en la EDO dada ($\ref{eqn:homogeneous_linear_ode}$) y dos **condiciones iniciales**:

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

Estas condiciones son necesarias para determinar las dos constantes arbitrarias $c_1$ y $c_2$ en la **solución general** de la EDO:

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Independencia y Dependencia Lineal
Hagamos una pausa para revisar los conceptos de independencia y dependencia lineal. Es necesario entenderlos para definir una base más adelante.  
Si para todo $x$ en un intervalo $I$ donde dos funciones $y_1$ y $y_2$ están definidas, se cumple que

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ y }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

entonces las dos funciones $y_1$ y $y_2$ se denominan **linealmente independientes** en el intervalo $I$. De lo contrario, $y_1$ y $y_2$ se denominan **linealmente dependientes**.

Si $y_1$ y $y_2$ son linealmente dependientes (es decir, si la proposición ($\ref{eqn:linearly_independent}$) no es cierta), entonces con $k_1 \neq 0$ o $k_2 \neq 0$, podemos dividir ambos lados de la ecuación en ($\ref{eqn:linearly_independent}$) para escribir

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{o} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

lo que muestra que $y_1$ y $y_2$ son proporcionales.

### Base, Solución General y Solución Particular
Volviendo al tema, para que la ecuación ($\ref{eqn:general_sol}$) sea una solución general, $y_1$ y $y_2$ deben ser soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) y, al mismo tiempo, ser linealmente independientes (no proporcionales) en el intervalo $I$. Un par de soluciones $(y_1, y_2)$ de la ecuación ($\ref{eqn:homogeneous_linear_ode}$) que son linealmente independientes en el intervalo $I$ se denomina una **base** o un **sistema fundamental** de soluciones para la ecuación ($\ref{eqn:homogeneous_linear_ode}$) en el intervalo $I$.

Al utilizar las condiciones iniciales para determinar las dos constantes $c_1$ y $c_2$ de la solución general ($\ref{eqn:general_sol}$), obtenemos una única solución que pasa por el punto $(x_0, K_0)$ y tiene una pendiente de $K_1$ en ese punto. Esto se llama una **solución particular** de la EDO ($\ref{eqn:homogeneous_linear_ode}$).

Si la ecuación ($\ref{eqn:homogeneous_linear_ode}$) es continua en un intervalo abierto $I$, entonces tiene una solución general, y esta solución general incluye todas las soluciones particulares posibles. Es decir, en este caso, la ecuación ($\ref{eqn:homogeneous_linear_ode}$) no tiene soluciones singulares que no puedan obtenerse de la solución general.

## Reducción de Orden
Si se puede encontrar una solución para una EDO lineal homogénea de segundo orden, se puede encontrar una segunda solución linealmente independiente, es decir, una base, resolviendo una EDO de primer orden como se muestra a continuación. Este método se llama **reducción de orden**.

Consideremos una EDO lineal homogénea de segundo orden <u>en su forma estándar, con $y^{\prime\prime}$ en lugar de $f(x)y^{\prime\prime}$</u>

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

y supongamos que conocemos una solución $y_1$ de esta ecuación en un intervalo abierto $I$.

Ahora, busquemos una segunda solución de la forma $y_2 = uy_1$. Sustituyendo

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

en la ecuación, obtenemos

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Agrupando los términos por $u^{\prime\prime}$, $u^{\prime}$ y $u$, y reorganizando, obtenemos

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

Sin embargo, como $y_1$ es una solución de la ecuación dada, la expresión en el último paréntesis es $0$. Por lo tanto, el término con $u$ desaparece, dejando una EDO en términos de $u^{\prime}$ y $u^{\prime\prime}$. Dividiendo ambos lados de esta EDO restante por $y_1$ y haciendo $u^{\prime}=U$ y $u^{\prime\prime}=U^{\prime}$, obtenemos la siguiente EDO de primer orden:

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Separando las variables ([Separación de Variables](/posts/Separation-of-Variables/)) e integrando, obtenemos

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

y tomando la exponencial en ambos lados, finalmente obtenemos

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Como establecimos anteriormente $U=u^{\prime}$, tenemos $u=\int U dx$. Por lo tanto, la segunda solución $y_2$ que buscamos es

$$ y_2 = uy_1 = y_1 \int U dx $$

Dado que $\cfrac{y_2}{y_1} = u = \int U dx$ no puede ser una constante mientras $U>0$, $y_1$ y $y_2$ forman una base de soluciones.

### Aplicaciones de la Reducción de Orden
Una EDO general de segundo orden $F(x, y, y^\prime, y^{\prime\prime})=0$, ya sea lineal o no lineal, puede reducirse a una de primer orden mediante la reducción de orden cuando $y$ no aparece explícitamente, cuando $x$ no aparece explícitamente, o, como vimos antes, cuando es lineal homogénea y ya se conoce una solución.

#### Caso en que $y$ no aparece explícitamente
En $F(x, y^\prime, y^{\prime\prime})=0$, si hacemos $z=y^{\prime}$, la ecuación se puede reducir a una EDO de primer orden en $z$, $F(x, z, z^{\prime})=0$.

#### Caso en que $x$ no aparece explícitamente
En $F(y, y^\prime, y^{\prime\prime})=0$, si hacemos $z=y^{\prime}$, entonces $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = z\cfrac{dz}{dy}$. Por lo tanto, la ecuación se puede reducir a una EDO de primer orden en $z$ con respecto a $y$, $F\left(y, z, z\frac{dz}{dy}\right)=0$, donde $y$ actúa como la variable independiente.
