---
title: "Wronskiano, Existencia y Unicidad de Soluciones"
description: "Para EDOs lineales homogéneas de segundo orden con coeficientes variables continuos arbitrarios, se estudian el teorema de existencia y unicidad de soluciones del problema de valor inicial, el método de discriminación de dependencia/independencia lineal de soluciones usando el Wronskiano, y se demuestra que tales ecuaciones siempre tienen una solución general que incluye todas las soluciones de la ecuación."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> Para la ecuación diferencial ordinaria lineal homogénea de segundo orden con coeficientes variables arbitrarios $p$ y $q$ continuos en el intervalo $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> y las condiciones iniciales
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> se cumplen los siguientes 4 teoremas:
> 1. **Teorema de existencia y unicidad de soluciones del problema de valor inicial**: El problema de valor inicial constituido por la ecuación dada y las condiciones iniciales tiene una solución única $y(x)$ en el intervalo $I$.
> 2. **Discriminación de dependencia/independencia lineal de soluciones usando el Wronskiano**: Para dos soluciones $y_1$ e $y_2$ de la ecuación, si existe un $x_0$ en el intervalo $I$ donde el **Wronskiano** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ se hace $0$, entonces las dos soluciones son linealmente dependientes. Además, si existe un $x_1$ en el intervalo $I$ donde $W\neq 0$, entonces las dos soluciones son linealmente independientes.
> 3. **Existencia de la solución general**: La ecuación dada tiene una solución general en el intervalo $I$.
> 4. **No existencia de soluciones singulares**: Esta solución general incluye todas las soluciones de la ecuación (es decir, no existen soluciones singulares).
{: .prompt-info }

## Prerrequisitos
- [Solución de EDOs lineales de primer orden](/posts/Solution-of-First-Order-Linear-ODE/)
- [EDOs lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)
- Matriz inversa y matriz singular, determinante

## EDOs homogéneas con coeficientes variables continuos arbitrarios
Anteriormente estudiamos las soluciones generales de [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/) y la [ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/).
En este artículo, extenderemos la discusión a un caso más general, estudiando la existencia y forma de la solución general de la ecuación diferencial ordinaria lineal homogénea de segundo orden con **coeficientes variables** continuos arbitrarios $p$ y $q$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

Además, también estudiaremos la unicidad del [problema de valor inicial](/posts/homogeneous-linear-odes-of-second-order/#problema-de-valor-inicial-y-condiciones-iniciales) constituido por la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y las siguientes dos condiciones iniciales

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

Adelantando la conclusión, el núcleo del contenido que trataremos aquí es que las ecuaciones diferenciales ordinarias <u>lineales</u> con coeficientes continuos no tienen *soluciones singulares* (soluciones que no se pueden obtener de la solución general).

## Teorema de existencia y unicidad de soluciones del problema de valor inicial
> **Teorema de existencia y unicidad de soluciones del problema de valor inicial**  
> Si $p(x)$ y $q(x)$ son funciones continuas en algún intervalo abierto $I$, y $x_0$ está dentro del intervalo $I$, entonces el problema de valor inicial constituido por las ecuaciones ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y ($\ref{eqn:initial_conditions}$) tiene una solución única $y(x)$ en el intervalo $I$.
{: .prompt-info }

No trataremos la demostración de la existencia aquí, solo veremos la demostración de la unicidad. Generalmente, demostrar la unicidad es más simple que demostrar la existencia.  
Si no te interesa la demostración, puedes saltar esta parte y pasar a [Dependencia e independencia lineal de soluciones](#dependencia-e-independencia-lineal-de-soluciones).

### Demostración de la unicidad
Supongamos que el problema de valor inicial constituido por la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) y las condiciones iniciales ($\ref{eqn:initial_conditions}$) tiene dos soluciones $y_1(x)$ e $y_2(x)$ en el intervalo $I$. Si podemos mostrar que la diferencia de estas dos soluciones

$$ y(x) = y_1(x) - y_2(x) $$

es idénticamente $0$ en el intervalo $I$, esto significa que $y_1 \equiv y_2$ en el intervalo $I$, lo que implica la unicidad de la solución.

Como la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) es una ecuación diferencial lineal homogénea, la combinación lineal $y$ de $y_1$ e $y_2$ se convierte en una solución de la ecuación en $I$. Como $y_1$ e $y_2$ satisfacen las mismas condiciones iniciales ($\ref{eqn:initial_conditions}$), $y$ satisface las condiciones

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Ahora consideremos la función

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

y su derivada

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

De la ecuación diferencial obtenemos

$$ y^{\prime\prime} = -py^{\prime} - qy $$

y sustituyendo esto en la expresión para $z^{\prime}$ obtenemos

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Ahora, como $y$ e $y^{\prime}$ son reales, tenemos

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

De esto y la definición de $z$ obtenemos las dos desigualdades

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

De estas dos desigualdades podemos ver que $\|2yy^{\prime}\|\leq z$, por lo que para el último término de la ecuación ($\ref{eqn:z_prime}$) se cumple la siguiente desigualdad:

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Usando este resultado junto con $-p \leq \|p\|$, y aplicando la ecuación ($\ref{eqn:inequalities}$a) al término $2yy^{\prime}$ de la ecuación ($\ref{eqn:z_prime}$), obtenemos

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Como ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, de esto obtenemos

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

Poniendo la función entre paréntesis como $h = 1 + 2\|p\| + \|q\|$, tenemos

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

De la misma manera, de las ecuaciones ($\ref{eqn:z_prime}$) y ($\ref{eqn:inequalities}$) obtenemos

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

Estas dos desigualdades ($\ref{eqn:inequality_6a}$), ($\ref{eqn:inequality_6b}$) son equivalentes a las siguientes desigualdades

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

y los [factores integrantes](/posts/Solution-of-First-Order-Linear-ODE/#ecuación-diferencial-lineal-no-homogénea) para los lados izquierdos de estas dos ecuaciones son

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{y} \qquad F_2 = e^{\int h(x)\ dx} $$

Como $h$ es continua, la integral indefinida $\int h(x)\ dx$ existe, y como $F_1$ y $F_2$ son positivos, de la ecuación ($\ref{eqn:inequalities_7}$) obtenemos

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

Esto significa que $F_1 z$ no aumenta en el intervalo $I$ y $F_2 z$ no disminuye. Por la ecuación ($\ref{eqn:initial_conditions_\*}$), $z(x_0) = 0$, por lo que

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finalmente, dividiendo ambos lados de las desigualdades por los números positivos $F_1$ y $F_2$, podemos demostrar la unicidad de la solución de la siguiente manera:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Dependencia e independencia lineal de soluciones
Recordemos brevemente el contenido tratado en [EDOs lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/#base-y-solución-general). La solución general en un intervalo abierto $I$ se construye a partir de una **base** $y_1$, $y_2$, es decir, un par de soluciones linealmente independientes en $I$. Aquí, que $y_1$ e $y_2$ sean **linealmente independientes** en el intervalo $I$ significa que satisfacen lo siguiente para todos los $x$ en el intervalo:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ y }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

Si no se satisface lo anterior y existe al menos un $k_1$, $k_2$ no nulo tal que $k_1y_1(x) + k_2y_2(x) = 0$, entonces $y_1$ e $y_2$ son **linealmente dependientes** en el intervalo $I$. En este caso, para todos los $x$ en el intervalo $I$ se cumple

$$ \text{(a) } y_1 = ky_2 \quad \text{o} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

por lo que $y_1$ e $y_2$ son proporcionales.

Ahora estudiemos el siguiente método de discriminación de independencia/dependencia lineal de soluciones.

> **Discriminación de dependencia/independencia lineal de soluciones usando el Wronskiano**  
> **i.** Si la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene coeficientes $p(x)$ y $q(x)$ continuos en el intervalo abierto $I$, entonces la condición necesaria y suficiente para que dos soluciones $y_1$ e $y_2$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$ sean linealmente dependientes es que el *determinante de Wronski* de estas soluciones, abreviado como **Wronskiano**
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> se haga $0$ en algún $x_0$ dentro del intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ e } y_2 \text{ son linealmente dependientes} $$
>
> **ii.** Si $W=0$ en un punto $x=x_0$ dentro del intervalo $I$, entonces $W=0$ en todos los $x$ dentro del intervalo $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> En otras palabras, si existe un $x_1$ en el intervalo $I$ donde $W\neq 0$, entonces $y_1$, $y_2$ son linealmente independientes en ese intervalo $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ e } y_2 \text{ son linealmente independientes}
> \end{align*}$$
>
{: .prompt-info }

> El Wronskiano fue introducido por primera vez por el matemático polaco Józef Maria Hoene-Wroński, y recibió su nombre actual en 11882 EH por el matemático escocés Thomas Muir.
{: .prompt-tip }

### Demostración
#### i. (a)
Supongamos que $y_1$ e $y_2$ son linealmente dependientes en el intervalo $I$. Entonces se cumple la ecuación ($\ref{eqn:linearly_dependent}$a) o ($\ref{eqn:linearly_dependent}$b) en el intervalo $I$. Si se cumple la ecuación ($\ref{eqn:linearly_dependent}$a), entonces

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

y de manera similar, si se cumple la ecuación ($\ref{eqn:linearly_dependent}$b), también

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

por lo que podemos confirmar que el Wronskiano $W(y_1, y_2)=0$ <u>para todos los $x$ en el intervalo $I$</u>.

#### i. (b)
Inversamente, cuando $W(y_1, y_2)=0$ para algún $x = x_0$, mostraremos que $y_1$ e $y_2$ se vuelven linealmente dependientes en el intervalo $I$. Consideremos el sistema de ecuaciones lineales en las incógnitas $k_1$, $k_2$

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

Esto se puede expresar en forma de ecuación vectorial como sigue:

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

y el determinante de esta matriz es precisamente $W(y_1(x_0), y_2(x_0))$. Como $\det(A) = W=0$, $A$ es una **matriz singular** que no tiene **matriz inversa**, por lo que el sistema de ecuaciones ($\ref{eqn:linear_system}$) tiene una solución $(c_1, c_2)$ distinta del vector cero $(0,0)$ donde al menos uno de $c_1$ y $c_2$ no es $0$. Ahora introduzcamos la función 

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Como la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) es lineal homogénea, por el [principio de superposición](/posts/homogeneous-linear-odes-of-second-order/#principio-de-superposición) esta función es una solución de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$. Del sistema de ecuaciones ($\ref{eqn:linear_system}$) podemos ver que esta solución satisface las condiciones iniciales $y(x_0)=0$, $y^{\prime}(x_0)=0$.

Por otro lado, existe la solución trivial $y^* \equiv 0$ que satisface las mismas condiciones iniciales $y^*(x_0)=0$, ${y^*}^{\prime}(x_0)=0$. Como los coeficientes $p$ y $q$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) son continuos, por el [teorema de existencia y unicidad de soluciones del problema de valor inicial](#teorema-de-existencia-y-unicidad-de-soluciones-del-problema-de-valor-inicial) se garantiza la unicidad de la solución, por lo que $y \equiv y^*$. Es decir, en el intervalo $I$

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Como al menos uno de $c_1$ y $c_2$ no es $0$, no se satisface ($\ref{eqn:linearly_independent}$), lo que significa que $y_1$, $y_2$ son linealmente dependientes en el intervalo $I$.

#### ii.
Si $W(x_0)=0$ en algún punto $x_0$ dentro del intervalo $I$, entonces por [i.(b)](#i-b) $y_1$, $y_2$ son linealmente dependientes en el intervalo $I$, y entonces por [i.(a)](#i-a) $W\equiv 0$. Por lo tanto, si existe al menos un $x_1$ en el intervalo $I$ tal que $W(x_1)\neq 0$, entonces $y_1$ e $y_2$ son linealmente independientes. $\blacksquare$

## La solución general incluye todas las soluciones
### Existencia de la solución general
> Si $p(x)$ y $q(x)$ son continuas en el intervalo abierto $I$, entonces la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución general en el intervalo $I$.
{: .prompt-info }

#### Demostración
Por el [teorema de existencia y unicidad de soluciones del problema de valor inicial](#teorema-de-existencia-y-unicidad-de-soluciones-del-problema-de-valor-inicial), la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución $y_1(x)$ en el intervalo $I$ que satisface las condiciones iniciales

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

y una solución $y_2(x)$ en el intervalo $I$ que satisface las condiciones iniciales

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

El Wronskiano de estas dos soluciones tiene un valor no nulo en $x=x_0$

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

por lo que, por la [discriminación de dependencia/independencia lineal de soluciones usando el Wronskiano](#dependencia-e-independencia-lineal-de-soluciones), $y_1$ e $y_2$ son linealmente independientes en el intervalo $I$. Por lo tanto, estas dos soluciones forman una base de soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$, y necesariamente existe una solución general $y = c_1y_1 + c_2y_2$ con constantes arbitrarias $c_1$, $c_2$ en el intervalo $I$. $\blacksquare$

### No existencia de soluciones singulares
> Si la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene coeficientes $p(x)$ y $q(x)$ continuos en algún intervalo abierto $I$, entonces todas las soluciones $y=Y(x)$ de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$ tienen la forma
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> donde $y_1$, $y_2$ son una base de soluciones de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$ y $C_1$, $C_2$ son constantes apropiadas.  
> Es decir, la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) no tiene **soluciones singulares** que no se puedan obtener de la solución general.
{: .prompt-info }

#### Demostración
Sea $y=Y(x)$ alguna solución de la ecuación ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) en el intervalo $I$. Ahora, por el [teorema de existencia de la solución general](#existencia-de-la-solución-general), la ecuación diferencial ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) tiene una solución general

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

en el intervalo $I$. Ahora debemos mostrar que para cualquier $Y(x)$ existen constantes $c_1$, $c_2$ tales que $y(x)=Y(x)$ en el intervalo $I$. Primero mostremos que podemos encontrar los valores de $c_1$, $c_2$ tales que $y(x_0)=Y(x_0)$ e $y^{\prime}(x_0)=Y^{\prime}(x_0)$ para cualquier $x_0$ en el intervalo $I$. De la ecuación ($\ref{eqn:general_solution}$) obtenemos

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

Como $y_1$ e $y_2$ son una base, el determinante de la matriz de coeficientes $W(y_1(x_0), y_2(x_0))\neq 0$, por lo que la ecuación ($\ref{eqn:vector_equation_2}$) se puede resolver para $c_1$ y $c_2$. Sea $(c_1, c_2) = (C_1, C_2)$ la solución. Sustituyendo esto en la ecuación ($\ref{eqn:general_solution}$) obtenemos la siguiente solución particular:

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Como $C_1$, $C_2$ son la solución de la ecuación ($\ref{eqn:vector_equation_2}$),

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

Por la unicidad del [teorema de existencia y unicidad de soluciones del problema de valor inicial](#teorema-de-existencia-y-unicidad-de-soluciones-del-problema-de-valor-inicial), $y^* \equiv Y$ para todos los $x$ en el intervalo $I$. $\blacksquare$
