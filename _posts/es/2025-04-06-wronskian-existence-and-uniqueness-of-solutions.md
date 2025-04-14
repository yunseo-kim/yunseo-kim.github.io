---
title: Wronskiano, existencia y unicidad de soluciones
description: Para ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden con coeficientes variables continuos, estudiamos los teoremas de existencia y unicidad de soluciones para problemas de valor inicial, el método del Wronskiano para determinar la dependencia/independencia lineal de soluciones, y demostramos que estas ecuaciones siempre tienen una solución general que incluye todas las soluciones posibles.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> Para un intervalo $I$ donde los coeficientes variables $p$ y $q$ son continuos, consideremos la ecuación diferencial ordinaria lineal homogénea de segundo orden
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> y las condiciones iniciales
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> Se cumplen los siguientes cuatro teoremas:
> 1. **Teorema de existencia y unicidad para problemas de valor inicial**: El problema de valor inicial formado por la ecuación dada y las condiciones iniciales tiene una única solución $y(x)$ en el intervalo $I$.
> 2. **Determinación de dependencia/independencia lineal mediante el Wronskiano**: Para dos soluciones $y_1$ y $y_2$ de la ecuación, si existe un punto $x_0$ en el intervalo $I$ donde el **Wronskiano** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ es igual a $0$, entonces las soluciones son linealmente dependientes. Además, si existe un punto $x_1$ en $I$ donde $W\neq 0$, entonces las soluciones son linealmente independientes.
> 3. **Existencia de la solución general**: La ecuación dada tiene una solución general en el intervalo $I$.
> 4. **Inexistencia de soluciones singulares**: Esta solución general incluye todas las soluciones de la ecuación (es decir, no existen soluciones singulares).
{: .prompt-info }

## Prerrequisitos
- [Solución de ecuaciones diferenciales ordinarias lineales de primer orden](/posts/Solution-of-First-Order-Linear-ODE/)
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matrices inversas y singulares, determinantes

## Ecuaciones diferenciales ordinarias lineales homogéneas con coeficientes variables continuos
Anteriormente estudiamos la [solución general de ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) y la [ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/).
En este artículo, extenderemos nuestra discusión a un caso más general, examinando la existencia y forma de la solución general de ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden con **coeficientes variables** $p$ y $q$ continuos:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Además, estudiaremos la unicidad del [problema de valor inicial](/posts/homogeneous-linear-odes-of-second-order/#problema-de-valor-inicial-y-condiciones-iniciales) formado por la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y las siguientes dos condiciones iniciales:

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Anticipando la conclusión, el punto clave de este artículo es que las ecuaciones diferenciales <u>lineales</u> con coeficientes continuos no tienen *soluciones singulares* (soluciones que no pueden obtenerse de la solución general).

## Teorema de existencia y unicidad para problemas de valor inicial
> **Teorema de existencia y unicidad para problemas de valor inicial**  
> Si $p(x)$ y $q(x)$ son funciones continuas en algún intervalo abierto $I$, y $x_0$ está en el intervalo $I$, entonces el problema de valor inicial formado por las ecuaciones ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y ($\ref{eqn:initial_conditions}$) tiene una única solución $y(x)$ en el intervalo $I$.
{: .prompt-info }

No abordaremos aquí la demostración de la existencia, y nos centraremos solo en la demostración de la unicidad, que suele ser más sencilla.  
Si no estás interesado en la demostración, puedes pasar directamente a la sección [Dependencia e independencia lineal de soluciones](#dependencia-e-independencia-lineal-de-soluciones).

### Demostración de la unicidad
Supongamos que el problema de valor inicial formado por la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y las condiciones iniciales ($\ref{eqn:initial_conditions}$) tiene dos soluciones $y_1(x)$ y $y_2(x)$ en el intervalo $I$. Si podemos demostrar que la diferencia entre estas dos soluciones

$$ y(x) = y_1(x) - y_2(x) $$

es idénticamente igual a $0$ en el intervalo $I$, entonces $y_1 \equiv y_2$ en $I$, lo que demostraría la unicidad de la solución.

Como la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) es una ecuación diferencial lineal homogénea, la combinación lineal $y$ de $y_1$ y $y_2$ también es una solución en $I$. Dado que $y_1$ y $y_2$ satisfacen las mismas condiciones iniciales ($\ref{eqn:initial_conditions}$), $y$ satisface las condiciones

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_1(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Consideremos ahora la función

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

y su derivada

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

De la ecuación diferencial, obtenemos

$$ y^{\prime\prime} = -py^{\prime} - qy $$

Sustituyendo esto en la expresión de $z^{\prime}$, tenemos

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Como $y$ y $y^{\prime}$ son números reales, tenemos que

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

De esto y de la definición de $z$, obtenemos las dos desigualdades

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

De estas dos desigualdades, podemos deducir que $\|2yy^{\prime}\|\leq z$, y por lo tanto, para el último término de la ecuación ($\ref{eqn:z_prime}$), se cumple la siguiente desigualdad:

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Usando este resultado junto con el hecho de que $-p \leq \|p\|$, y aplicando la desigualdad ($\ref{eqn:inequalities}$a) al término $2yy^{\prime}$ en la ecuación ($\ref{eqn:z_prime}$), obtenemos

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Como ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, esto nos lleva a

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

Si definimos la función dentro del paréntesis como $h = 1 + 2\|p\| + \|q\|$, tenemos

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

De manera similar, usando las ecuaciones ($\ref{eqn:z_prime}$) y ($\ref{eqn:inequalities}$), obtenemos

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Estas dos desigualdades ($\ref{eqn:inequality_6a}$) y ($\ref{eqn:inequality_6b}$) son equivalentes a

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

Los [factores integrantes](/posts/Solution-of-First-Order-Linear-ODE/#ecuación-diferencial-lineal-no-homogénea) para los lados izquierdos de estas dos ecuaciones son

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{y} \qquad F_2 = e^{\int h(x)\ dx} $$

Como $h$ es continua, la integral indefinida $\int h(x)\ dx$ existe, y como $F_1$ y $F_2$ son positivos, de las ecuaciones ($\ref{eqn:inequalities_7}$) obtenemos

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Esto significa que $F_1 z$ no es creciente y $F_2 z$ no es decreciente en el intervalo $I$. Como $z(x_0) = 0$ según las ecuaciones ($\ref{eqn:initial_conditions_*}$), tenemos

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finalmente, dividiendo ambos lados de las desigualdades por los valores positivos $F_1$ y $F_2$, podemos demostrar la unicidad de la solución:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dependencia e independencia lineal de soluciones
Recordemos brevemente lo que vimos en [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/#base-y-solución-general). La solución general en un intervalo abierto $I$ se construye a partir de una **base** $y_1$, $y_2$, es decir, un par de soluciones linealmente independientes. Dos soluciones $y_1$ y $y_2$ son **linealmente independientes** en el intervalo $I$ si para todo $x$ en el intervalo:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ y }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Si esta condición no se cumple, y existe al menos un par de valores $k_1$, $k_2$ no ambos cero tales que $k_1y_1(x) + k_2y_2(x) = 0$, entonces $y_1$ y $y_2$ son **linealmente dependientes** en el intervalo $I$. En este caso, para todo $x$ en el intervalo $I$:

$$ \text{(a) } y_1 = ky_2 \quad \text{o} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

es decir, $y_1$ y $y_2$ son proporcionales.

Ahora, veamos el siguiente método para determinar la dependencia o independencia lineal de soluciones:

> **Determinación de dependencia/independencia lineal mediante el Wronskiano**  
> **i.** Si la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene coeficientes $p(x)$ y $q(x)$ continuos en un intervalo abierto $I$, entonces una condición necesaria y suficiente para que dos soluciones $y_1$ y $y_2$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$ sean linealmente dependientes es que el *determinante wronskiano*, o simplemente **Wronskiano**
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> sea igual a $0$ en algún punto $x_0$ del intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ y } y_2 \text{ son linealmente dependientes} $$
>
> **ii.** Si el Wronskiano $W=0$ en un punto $x=x_0$ del intervalo $I$, entonces $W=0$ para todo $x$ en el intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> En otras palabras, si existe un punto $x_1$ en el intervalo $I$ donde $W\neq 0$, entonces $y_1$ y $y_2$ son linealmente independientes en $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ y } y_2 \text{ son linealmente independientes}
> \end{align*}$$
>
{: .prompt-info }

> El Wronskiano fue introducido por el matemático polaco Józef Maria Hoene-Wroński, y recibió su nombre actual en 11882 EH por el matemático escocés Thomas Muir.
{: .prompt-tip }

### Demostración
#### i. (a)
Supongamos que $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$. Entonces, en el intervalo $I$, se cumple la ecuación ($\ref{eqn:linearly_dependent}$a) o ($\ref{eqn:linearly_dependent}$b). Si se cumple la ecuación ($\ref{eqn:linearly_dependent}$a), entonces

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

De manera similar, si se cumple la ecuación ($\ref{eqn:linearly_dependent}$b), entonces

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Por lo tanto, podemos confirmar que el Wronskiano $W(y_1, y_2)=0$ para <u>todo $x$ en el intervalo $I$</u>.

#### i. (b)
Inversamente, supongamos que $W(y_1, y_2)=0$ en algún punto $x = x_0$. Demostraremos que $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$. Consideremos el sistema de ecuaciones lineales con incógnitas $k_1$ y $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Esto puede expresarse como la siguiente ecuación vectorial:

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

La matriz de coeficientes de esta ecuación vectorial es

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

y su determinante es precisamente $W(y_1(x_0), y_2(x_0))$. Como $\det(A) = W=0$, $A$ es una **matriz singular** (sin inversa), y por lo tanto, el sistema de ecuaciones ($\ref{eqn:linear_system}$) tiene una solución no trivial $(c_1, c_2)$ donde al menos uno de $c_1$ o $c_2$ no es cero. Definamos ahora la función

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Como la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) es lineal homogénea, por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición), esta función es una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$. De la ecuación ($\ref{eqn:linear_system}$), podemos ver que esta solución satisface las condiciones iniciales $y(x_0)=0$ y $y^{\prime}(x_0)=0$.

Por otro lado, existe la solución trivial $y^\* \equiv 0$ que también satisface las mismas condiciones iniciales $y^\*(x_0)=0$ y ${y^\*}^{\prime}(x_0)=0$. Como los coeficientes $p$ y $q$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) son continuos, el [Teorema de existencia y unicidad para problemas de valor inicial](#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial) garantiza la unicidad de la solución, por lo que $y \equiv y^\*$. Es decir, en el intervalo $I$:

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Como al menos uno de $c_1$ o $c_2$ no es cero, no se cumple la condición ($\ref{eqn:linearly_independent}$), lo que significa que $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$.

#### ii.
Si el Wronskiano $W(x_0)=0$ en algún punto $x_0$ del intervalo $I$, entonces por [i.(b)](#i-b), $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$, y por [i.(a)](#i-a), $W\equiv 0$ en todo el intervalo. Por lo tanto, si existe un punto $x_1$ en el intervalo $I$ donde $W(x_1)\neq 0$, entonces $y_1$ y $y_2$ son linealmente independientes. $\blacksquare$

## La solución general incluye todas las soluciones
### Existencia de la solución general
> Si $p(x)$ y $q(x)$ son continuos en un intervalo abierto $I$, entonces la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución general en el intervalo $I$.
{: .prompt-info }

#### Demostración
Por el [Teorema de existencia y unicidad para problemas de valor inicial](#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial), la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución $y_1(x)$ en el intervalo $I$ que satisface las condiciones iniciales

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

y una solución $y_2(x)$ en el intervalo $I$ que satisface las condiciones iniciales

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

El Wronskiano de estas dos soluciones en $x=x_0$ es un valor no nulo:

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Por lo tanto, según la [Determinación de dependencia/independencia lineal mediante el Wronskiano](#dependencia-e-independencia-lineal-de-soluciones), $y_1$ y $y_2$ son linealmente independientes en el intervalo $I$. Estas dos soluciones forman una base de soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$, y por lo tanto, existe una solución general $y = c_1y_1 + c_2y_2$ con constantes arbitrarias $c_1$ y $c_2$ en el intervalo $I$. $\blacksquare$

### Inexistencia de soluciones singulares
> Si la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene coeficientes $p(x)$ y $q(x)$ continuos en un intervalo abierto $I$, entonces toda solución $y=Y(x)$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$ puede expresarse como
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> donde $y_1$ y $y_2$ forman una base de soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$, y $C_1$ y $C_2$ son constantes apropiadas.  
> Es decir, la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no tiene **soluciones singulares** (soluciones que no pueden obtenerse de la solución general).
{: .prompt-info }

#### Demostración
Sea $y=Y(x)$ cualquier solución de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$. Por el [teorema de existencia de la solución general](#existencia-de-la-solución-general), la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución general

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

en el intervalo $I$. Debemos demostrar que para cualquier $Y(x)$ dado, existen constantes $c_1$ y $c_2$ tales que $y(x)=Y(x)$ en el intervalo $I$. Primero, encontremos valores de $c_1$ y $c_2$ tales que $y(x_0)=Y(x_0)$ y $y^{\prime}(x_0)=Y^{\prime}(x_0)$ para cualquier $x_0$ elegido en el intervalo $I$. De la ecuación ($\ref{eqn:general_solution}$), obtenemos

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

Como $y_1$ y $y_2$ forman una base, el determinante de la matriz de coeficientes, $W(y_1(x_0), y_2(x_0))\neq 0$, por lo que la ecuación ($\ref{eqn:vector_equation_2}$) tiene una solución única para $c_1$ y $c_2$. Llamemos a esta solución $(c_1, c_2) = (C_1, C_2)$. Sustituyendo estos valores en la ecuación ($\ref{eqn:general_solution}$), obtenemos la solución particular:

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Como $(C_1, C_2)$ es la solución de la ecuación ($\ref{eqn:vector_equation_2}$), tenemos

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Por la unicidad garantizada por el [Teorema de existencia y unicidad para problemas de valor inicial](#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial), $y^* \equiv Y$ en todo el intervalo $I$. $\blacksquare$
