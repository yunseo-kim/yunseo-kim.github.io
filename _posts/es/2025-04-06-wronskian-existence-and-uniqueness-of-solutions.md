---
title: "El Wronskiano, Existencia y Unicidad de Soluciones"
description: "Se analiza el teorema de existencia y unicidad para problemas de valor inicial de EDOs lineales homogéneas de segundo orden con coeficientes variables continuos. Se introduce el Wronskiano como criterio para la dependencia o independencia lineal de las soluciones, y se demuestra que estas ecuaciones siempre poseen una solución general que abarca todas las soluciones posibles."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Para una ecuación diferencial ordinaria lineal homogénea de segundo orden con coeficientes variables continuos $p$ y $q$ en un intervalo $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> y las condiciones iniciales
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> se cumplen los siguientes cuatro teoremas.
> 1. **Teorema de Existencia y Unicidad para Problemas de Valor Inicial**: El problema de valor inicial compuesto por la ecuación y las condiciones iniciales dadas tiene una solución única $y(x)$ en el intervalo $I$.
> 2. **Criterio de Dependencia/Independencia Lineal de Soluciones usando el Wronskiano**: Para dos soluciones $y_1$ y $y_2$ de la ecuación, si existe un $x_0$ en el intervalo $I$ donde el valor del **Wronskiano** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ es $0$, entonces las dos soluciones son linealmente dependientes. Además, si existe un $x_1$ en el intervalo $I$ donde $W\neq 0$, las dos soluciones son linealmente independientes.
> 3. **Existencia de la Solución General**: La ecuación dada tiene una solución general en el intervalo $I$.
> 4. **Inexistencia de Soluciones Singulares**: Esta solución general incluye todas las soluciones de la ecuación (es decir, no existen soluciones singulares).
{: .prompt-info }

## Prerrequisitos
- [Solución de EDOs Lineales de Primer Orden](/posts/Solution-of-First-Order-Linear-ODE/)
- [EDOs Lineales Homogéneas de Segundo Orden (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs Lineales Homogéneas de Segundo Orden con Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matriz inversa, matriz singular y determinante

## EDOs Lineales Homogéneas con Coeficientes Variables Continuos
Anteriormente, hemos examinado la solución general de las [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) y la [ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/).
En este artículo, extenderemos la discusión a un caso más general para investigar la existencia y la forma de la solución general de una EDO lineal homogénea de segundo orden con **coeficientes variables** continuos arbitrarios $p$ y $q$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Además, también examinaremos la unicidad del [problema de valor inicial](/posts/homogeneous-linear-odes-of-second-order/#problema-de-valor-inicial-y-condiciones-iniciales) compuesto por la EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y las dos siguientes condiciones iniciales

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Para anticipar la conclusión, el punto clave de lo que se trata aquí es que una EDO <u>lineal</u> con coeficientes continuos no tiene *soluciones singulares* (soluciones que no se pueden obtener de la solución general).

## Teorema de Existencia y Unicidad para Problemas de Valor Inicial
> **Teorema de Existencia y Unicidad para Problemas de Valor Inicial**  
> Si $p(x)$ y $q(x)$ son funciones continuas en algún intervalo abierto $I$, y $x_0$ está en $I$, entonces el problema de valor inicial compuesto por las ecuaciones ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y ($\ref{eqn:initial_conditions}$) tiene una solución única $y(x)$ en el intervalo $I$.
{: .prompt-info }

La demostración de la existencia no se abordará aquí; solo examinaremos la demostración de la unicidad. Generalmente, demostrar la unicidad es más sencillo que demostrar la existencia.  
Si no le interesa la demostración, puede saltarse esta parte e ir directamente a [Dependencia e Independencia Lineal de las Soluciones](#dependencia-e-independencia-lineal-de-las-soluciones).

### Demostración de la Unicidad
Supongamos que el problema de valor inicial compuesto por la EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y las condiciones iniciales ($\ref{eqn:initial_conditions}$) tiene dos soluciones $y_1(x)$ y $y_2(x)$ en el intervalo $I$. La diferencia de estas dos soluciones

$$ y(x) = y_1(x) - y_2(x) $$

si podemos demostrar que es idénticamente cero en el intervalo $I$, esto implica que $y_1 \equiv y_2$ en el intervalo $I$, lo que significa la unicidad de la solución.

Dado que la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) es una EDO lineal homogénea, $y$, que es una combinación lineal de $y_1$ y $y_2$, es una solución de la ecuación en $I$. Como $y_1$ y $y_2$ satisfacen las mismas condiciones iniciales ($\ref{eqn:initial_conditions}$), $y$ satisface la condición

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Ahora consideremos la función

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

y su derivada

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

De la EDO, obtenemos

$$ y^{\prime\prime} = -py^{\prime} - qy $$

y sustituyendo esto en la ecuación para $z^{\prime}$, obtenemos

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Ahora, como $y$ y $y^{\prime}$ son reales,

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

De esto y de la definición de $z$, obtenemos dos desigualdades

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

De estas dos desigualdades, podemos ver que $\|2yy^{\prime}\|\leq z$, y por lo tanto, para el último término de la ecuación ($\ref{eqn:z_prime}$), se cumple la siguiente desigualdad.

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Usando este resultado junto con $-p \leq \|p\|$, y aplicando la ecuación ($\ref{eqn:inequalities}$a) al término $2yy^{\prime}$ de la ecuación ($\ref{eqn:z_prime}$), obtenemos

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Como ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, de esto obtenemos

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

y si definimos la función entre paréntesis como $h = 1 + 2\|p\| + \|q\|$, entonces

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

Del mismo modo, de las ecuaciones ($\ref{eqn:z_prime}$) y ($\ref{eqn:inequalities}$), obtenemos

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Estas dos desigualdades ($\ref{eqn:inequality_6a}$), ($\ref{eqn:inequality_6b}$) son equivalentes a la siguiente desigualdad

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

y el [factor integrante](/posts/Solution-of-First-Order-Linear-ODE/#ecuación-diferencial-ordinaria-lineal-no-homogénea) para el lado izquierdo de las dos ecuaciones es

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{y} \qquad F_2 = e^{\int h(x)\ dx} $$

Como $h$ es continua, la integral indefinida $\int h(x)\ dx$ existe, y como $F_1$ y $F_2$ son positivos, de la ecuación ($\ref{eqn:inequalities_7}$) obtenemos

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Esto significa que $F_1 z$ no es creciente y $F_2 z$ no es decreciente en el intervalo $I$. Por la ecuación ($\ref{eqn:initial_conditions_*}$), $z(x_0) = 0$, por lo que

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finalmente, dividiendo ambos lados de la desigualdad por los números positivos $F_1$ y $F_2$, podemos demostrar la unicidad de la solución de la siguiente manera.

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dependencia e Independencia Lineal de las Soluciones
Recordemos brevemente lo que cubrimos en [EDOs Lineales Homogéneas de Segundo Orden](/posts/homogeneous-linear-odes-of-second-order/#base-y-solución-general). La solución general en un intervalo abierto $I$ se construye a partir de una **base** $(y_1, y_2)$ en $I$, es decir, un par de soluciones linealmente independientes. Aquí, que $y_1$ y $y_2$ sean **linealmente independientes** en el intervalo $I$ significa que para todo $x$ en el intervalo, se cumple lo siguiente:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ y }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Si lo anterior no se cumple, y existe al menos un $k_1$ o $k_2$ no nulo tal que $k_1y_1(x) + k_2y_2(x) = 0$, entonces $y_1$ y $y_2$ son **linealmente dependientes** en el intervalo $I$. En este caso, para todo $x$ en el intervalo $I$,

$$ \text{(a) } y_1 = ky_2 \quad \text{o} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

de modo que $y_1$ y $y_2$ son proporcionales.

Ahora, examinemos el siguiente criterio para la dependencia/independencia lineal de las soluciones.

> **Criterio de Dependencia/Independencia Lineal de Soluciones usando el Wronskiano**  
> **i.** Si la EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene coeficientes continuos $p(x)$ y $q(x)$ en un intervalo abierto $I$, entonces una condición necesaria y suficiente para que dos soluciones $y_1$ y $y_2$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) sean linealmente dependientes en el intervalo $I$ es que el *determinante de Wronski* de estas soluciones, abreviado como **Wronskiano**, que es el siguiente determinante
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> sea cero en algún $x_0$ del intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ y } y_2 \text{ son linealmente dependientes} $$
>
> **ii.** Si $W=0$ en un punto $x=x_0$ del intervalo $I$, entonces $W=0$ para todo $x$ en el intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> En otras palabras, si existe un $x_1$ en el intervalo $I$ tal que $W\neq 0$, entonces en ese intervalo $I$, $y_1$ y $y_2$ son linealmente independientes.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ y } y_2 \text{ son linealmente independientes}
> \end{align*}$$
>
{: .prompt-info }

> El Wronskiano fue introducido por primera vez por el matemático polaco Józef Maria Hoene-Wroński, y recibió su nombre actual en 11882 EH, después de su muerte, por el matemático escocés Sir Thomas Muir.
{: .prompt-tip }

### Demostración
#### i. (a)
Supongamos que $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$. Entonces, la ecuación ($\ref{eqn:linearly_dependent}$a) o ($\ref{eqn:linearly_dependent}$b) se cumple en el intervalo $I$. Si se cumple la ecuación ($\ref{eqn:linearly_dependent}$a), entonces

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

y de manera similar, si se cumple la ecuación ($\ref{eqn:linearly_dependent}$b),

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

por lo que podemos confirmar que el Wronskiano $W(y_1, y_2)=0$ <u>para todo $x$ en el intervalo $I$</u>.

#### i. (b)
A la inversa, supongamos que $W(y_1, y_2)=0$ para algún $x = x_0$. Demostraremos que $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$. Consideremos el sistema de ecuaciones lineales para las incógnitas $k_1$, $k_2$

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Esto se puede expresar en forma de ecuación vectorial como:

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

y el determinante de esta matriz es precisamente $W(y_1(x_0), y_2(x_0))$. Como $\det(A) = W=0$, $A$ es una **matriz singular** que no tiene **matriz inversa**, y por lo tanto, el sistema de ecuaciones ($\ref{eqn:linear_system}$) tiene una solución no trivial $(c_1, c_2)$ además del vector nulo $(0,0)$, donde al menos uno de $k_1$ y $k_2$ no es cero. Ahora, introduzcamos la función

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Dado que la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) es lineal homogénea, por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición), esta función es una solución de ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$. De la ecuación ($\ref{eqn:linear_system}$), podemos ver que esta solución satisface las condiciones iniciales $y(x_0)=0$, $y^{\prime}(x_0)=0$.

Por otro lado, existe la solución trivial $y^\* \equiv 0$ que satisface las mismas condiciones iniciales $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Dado que los coeficientes $p$ y $q$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) son continuos, la unicidad de la solución está garantizada por el [Teorema de Existencia y Unicidad para Problemas de Valor Inicial](#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial), y por lo tanto, $y \equiv y^\*$. Es decir, en el intervalo $I$,

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Dado que al menos uno de $c_1$ y $c_2$ no es cero, no se satisface ($\ref{eqn:linearly_independent}$), lo que significa que $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$.

#### ii.
Si $W(x_0)=0$ en algún punto $x_0$ del intervalo $I$, entonces por [i.(b)](#i-b), $y_1$ y $y_2$ son linealmente dependientes en el intervalo $I$, y entonces por [i.(a)](#i-a), $W\equiv 0$. Por lo tanto, si existe al menos un $x_1$ en el intervalo $I$ tal que $W(x_1)\neq 0$, entonces $y_1$ y $y_2$ son linealmente independientes. $\blacksquare$

## La Solución General Incluye Todas las Soluciones
### Existencia de la Solución General
> Si $p(x)$ y $q(x)$ son continuos en un intervalo abierto $I$, entonces la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución general en el intervalo $I$.
{: .prompt-info }

#### Demostración
Por el [Teorema de Existencia y Unicidad para Problemas de Valor Inicial](#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial), la EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución $y_1(x)$ que satisface las condiciones iniciales en el intervalo $I$

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

y una solución $y_2(x)$ que satisface las condiciones iniciales en el intervalo $I$

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

El Wronskiano de estas dos soluciones en $x=x_0$ tiene un valor no nulo

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

por lo que, por el [Criterio de Dependencia/Independencia Lineal de Soluciones usando el Wronskiano](#dependencia-e-independencia-lineal-de-las-soluciones), $y_1$ y $y_2$ son linealmente independientes en el intervalo $I$. Por lo tanto, estas dos soluciones forman una base de soluciones para la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$, y una solución general $y = c_1y_1 + c_2y_2$ con constantes arbitrarias $c_1, c_2$ debe existir en el intervalo $I$. $\blacksquare$

### Inexistencia de Soluciones Singulares
> Si la EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene coeficientes continuos $p(x)$ y $q(x)$ en algún intervalo abierto $I$, entonces toda solución $y=Y(x)$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$ es de la forma
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> donde $y_1, y_2$ son una base de soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$ y $C_1, C_2$ son constantes apropiadas.  
> Es decir, la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no tiene **soluciones singulares**, que son soluciones que no se pueden obtener de la solución general.
{: .prompt-info }

#### Demostración
Sea $y=Y(x)$ cualquier solución de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$. Ahora, por el [teorema de existencia de la solución general](#existencia-de-la-solución-general), la EDO ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución general en el intervalo $I$

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Ahora debemos demostrar que para cualquier $Y(x)$, existen constantes $c_1, c_2$ tales que $y(x)=Y(x)$ en el intervalo $I$. Primero demostremos que podemos encontrar valores de $c_1, c_2$ tales que $y(x_0)=Y(x_0)$ y $y^{\prime}(x_0)=Y^{\prime}(x_0)$ para un $x_0$ arbitrario en el intervalo $I$. De la ecuación ($\ref{eqn:general_solution}$), obtenemos

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

Dado que $y_1$ y $y_2$ forman una base, el determinante de la matriz de coeficientes, $W(y_1(x_0), y_2(x_0))\neq 0$, y por lo tanto, la ecuación ($\ref{eqn:vector_equation_2}$) se puede resolver para $c_1$ y $c_2$. Llamemos a la solución $(c_1, c_2) = (C_1, C_2)$. Sustituyendo esto en la ecuación ($\ref{eqn:general_solution}$), obtenemos la siguiente solución particular.

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Como $C_1, C_2$ son la solución de la ecuación ($\ref{eqn:vector_equation_2}$),

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Por la unicidad del [Teorema de Existencia y Unicidad para Problemas de Valor Inicial](#teorema-de-existencia-y-unicidad-para-problemas-de-valor-inicial), $y^\* \equiv Y$ para todo $x$ en el intervalo $I$. $\blacksquare$
