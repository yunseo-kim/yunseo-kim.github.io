---
title: Método de coeficientes indeterminados
description: Exploremos el método de coeficientes indeterminados, una técnica que permite resolver fácilmente problemas de valor inicial para ciertos tipos de ecuaciones diferenciales ordinarias lineales no homogéneas con coeficientes constantes, muy útil en ingeniería para sistemas vibratorios y circuitos RLC.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - El **método de coeficientes indeterminados** se aplica a:
>   - Ecuaciones diferenciales ordinarias lineales no homogéneas con **coeficientes constantes $a$ y $b$**
>   - Donde la entrada $r(x)$ consiste en funciones exponenciales, potencias de $x$, $\cos$ o $\sin$, o sumas y productos de estas funciones
>   - $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Reglas de selección para el método de coeficientes indeterminados**  
>   - **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, seleccione $y_p$ de la misma fila en la segunda columna y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regla de modificación**: Si el término seleccionado para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la ecuación diferencial homogénea).  
>   - **(c) Regla de suma**: Si $r(x)$ es una suma de funciones de la primera columna de la tabla, seleccione para $y_p$ la suma de las funciones correspondientes de la segunda columna.
>
> | Término en $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)
- [Wronskiano, existencia y unicidad de soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Ecuaciones diferenciales ordinarias lineales no homogéneas de segundo orden](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Espacios vectoriales, generación lineal (álgebra lineal)

## Método de coeficientes indeterminados
Consideremos una ecuación diferencial ordinaria lineal no homogénea de segundo orden con $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

y la ecuación diferencial homogénea correspondiente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Según lo que vimos en [Ecuaciones diferenciales ordinarias lineales no homogéneas de segundo orden](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver un problema de valor inicial para la ecuación diferencial no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$), debemos encontrar $y_h$ resolviendo la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$) y luego encontrar una solución particular $y_p$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) para obtener la solución general

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

¿Cómo encontramos $y_p$? El método general para encontrar $y_p$ es el **método de variación de parámetros**, pero en ciertos casos podemos aplicar el **método de coeficientes indeterminados**, que es mucho más simple. Este método es particularmente útil en ingeniería para sistemas vibratorios y modelos de circuitos RLC.

El método de coeficientes indeterminados es adecuado para ecuaciones diferenciales lineales con **coeficientes constantes $a$ y $b$** donde la entrada $r(x)$ consiste en funciones exponenciales, potencias de $x$, $\cos$ o $\sin$, o sumas y productos de estas funciones:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

La clave del método de coeficientes indeterminados es que este tipo de funciones $r(x)$ tienen derivadas de forma similar a ellas mismas. Para aplicar el método, seleccionamos un $y_p$ de forma similar a $r(x)$, pero con coeficientes indeterminados que se determinan sustituyendo $y_p$ y sus derivadas en la ecuación dada. Las reglas para seleccionar un $y_p$ adecuado para formas de $r(x)$ de importancia práctica en ingeniería son las siguientes:

> **Reglas de selección para el método de coeficientes indeterminados**  
> **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, seleccione $y_p$ de la misma fila en la segunda columna y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regla de modificación**: Si el término seleccionado para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la ecuación diferencial homogénea).  
> **(c) Regla de suma**: Si $r(x)$ es una suma de funciones de la primera columna de la tabla, seleccione para $y_p$ la suma de las funciones correspondientes de la segunda columna.
>
> | Término en $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método tiene la ventaja de ser autocorrectivo. Si seleccionamos incorrectamente $y_p$ o elegimos muy pocos términos, llegaremos a una contradicción; si elegimos demasiados términos, los coeficientes de los términos innecesarios resultarán ser cero, dando el resultado correcto. Incluso si algo sale mal al aplicar el método, lo notaremos durante el proceso de resolución, por lo que podemos intentarlo sin preocupaciones siguiendo las reglas de selección.

### Demostración de la regla de suma
Consideremos una ecuación diferencial lineal no homogénea de la forma

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Ahora consideremos las dos ecuaciones con el mismo lado izquierdo pero con entradas $r_1$ y $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Supongamos que estas ecuaciones tienen soluciones ${y_p}_1$ y ${y_p}_2$ respectivamente. Si denotamos el lado izquierdo de la ecuación como $L[y]$, entonces por la linealidad de $L[y]$, para $y_p = {y_p}_1 + {y_p}_2$ tenemos:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Ejemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Según la regla básica (a), ponemos $y_p = Ce^{\gamma x}$ y sustituimos en la ecuación dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Caso $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar el coeficiente indeterminado $C$ y encontrar $y_p$ como sigue:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Caso $\gamma^2 + a\gamma + b = 0$
En este caso debemos aplicar la regla de modificación (b). Primero, usando que $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, encontramos las raíces de la ecuación característica de la ecuación diferencial homogénea $y^{\prime\prime} + ay^{\prime} + by = 0$:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

De aquí obtenemos la base de la ecuación diferencial homogénea:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Caso $\gamma \neq -a-\gamma$
Como el término $Ce^{\gamma x}$ que seleccionamos para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente pero no corresponde a una raíz doble, según la regla de modificación (b) debemos multiplicarlo por $x$, obteniendo $y_p = Cxe^{\gamma x}$.

Ahora sustituimos este $y_p$ en la ecuación dada $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Caso $\gamma = -a-\gamma$
En este caso, el término $Ce^{\gamma x}$ que seleccionamos para $y_p$ corresponde a una raíz doble de la ecuación característica, por lo que según la regla de modificación (b) debemos multiplicarlo por $x^2$, obteniendo $y_p = Cx^2 e^{\gamma x}$.

Sustituimos este $y_p$ en la ecuación dada $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extensión del método de coeficientes indeterminados: $r(x)$ como producto de funciones
Consideremos una ecuación diferencial lineal no homogénea con

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

donde $r(x) = k x^n e^{\alpha x}\cos(\omega x)$ es un producto de funciones exponenciales, potencias de $x$ y funciones trigonométricas. Demostraremos que existe una solución $y_p$ que es también un producto de las funciones correspondientes de la segunda columna de la tabla.

> Para la demostración rigurosa se utiliza álgebra lineal, y estas partes están marcadas con \*. Puedes saltarte estas secciones y aún entender la idea general.
{: .prompt-tip }

### Definición del espacio vectorial $V$\*
Para $r(x)$ de la forma

$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

podemos definir un espacio vectorial $V$ tal que $r(x) \in V$:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forma de las derivadas de funciones exponenciales, polinómicas y trigonométricas
Las derivadas de las funciones básicas de la primera columna de la tabla son:
- Función exponencial: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Función polinómica: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Función trigonométrica: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Las derivadas de estas funciones se pueden expresar como <u>sumas de funciones del mismo tipo</u>.

Por tanto, si $f$ y $g$ son funciones de este tipo o sumas de ellas, y $r(x) = f(x)g(x)$, aplicando la regla del producto:

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

donde $f$, $f^{\prime}$, $f^{\prime\prime}$ y $g$, $g^{\prime}$, $g^{\prime\prime}$ pueden expresarse como sumas o múltiplos constantes de funciones exponenciales, polinómicas y trigonométricas. Por lo tanto, $r^{\prime}(x) = (fg)^{\prime}$ y $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ también pueden expresarse como sumas y productos de estas funciones.

### Invariancia del espacio vectorial $V$ bajo el operador diferencial $D$ y la transformación lineal $L$\*
Es decir, no solo $r(x)$ sino también $r^{\prime}(x)$ y $r^{\prime\prime}(x)$ son combinaciones lineales de términos de la forma $x^k e^{\alpha x}\cos(\omega x)$ y $x^k e^{\alpha x}\sin(\omega x)$, por lo que:

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Más generalmente, introduciendo el operador diferencial $D$ para todos los elementos del espacio vectorial $V$ definido anteriormente, podemos decir que *el espacio vectorial $V$ está cerrado bajo la operación de diferenciación $D$*. Por lo tanto, si denotamos el lado izquierdo de la ecuación $y^{\prime\prime} + ay^{\prime} + by$ como $L[y]$, entonces *$V$ es invariante bajo $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Como $r(x) \in V$ y $V$ es invariante bajo $L$, existe otro elemento $y_p \in V$ tal que $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Por lo tanto, podemos seleccionar un $y_p$ apropiado con coeficientes indeterminados $A_0, A_1, \dots, A_n$, $K$ y $M$ de la siguiente forma, que incluye la suma de todos los posibles términos producto:

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

Siguiendo las reglas básica (a) y de modificación (b), podemos determinar los coeficientes indeterminados sustituyendo $y_p$ (o $xy_p$, $x^2y_p$ según corresponda) y sus derivadas en la ecuación dada. El valor de $n$ se determina según el grado de $x$ en $r(x)$.

$\blacksquare$

> Si la entrada dada $r(x)$ incluye varios valores diferentes de $\alpha_i$ y $\omega_j$, debemos seleccionar un $y_p$ que incluya todos los posibles términos de la forma $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ y $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ para cada valor de $\alpha_i$ y $\omega_j$.  
> La ventaja del método de coeficientes indeterminados es su simplicidad, pero si el ansatz se vuelve demasiado complicado, puede ser mejor aplicar el método de variación de parámetros que veremos más adelante.
{: .prompt-warning }

## Extensión del método de coeficientes indeterminados: ecuación de Euler-Cauchy
El método de coeficientes indeterminados también puede aplicarse a la [ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Cambio de variable
[Mediante la sustitución $x = e^t$ podemos transformar la ecuación de Euler-Cauchy en una ecuación diferencial ordinaria lineal homogénea de segundo orden con coeficientes constantes](/posts/euler-cauchy-equation/#transformación-a-ecuación-diferencial-ordinaria-lineal-homogénea-de-segundo-orden-con-coeficientes-constantes):

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

Con esto, la ecuación de Euler-Cauchy se transforma en:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Podemos aplicar el [método de coeficientes indeterminados](#método-de-coeficientes-indeterminados) a la ecuación ($\ref{eqn:substituted}$) para resolverla en términos de $t$, y luego sustituir $t = \ln x$ para obtener la solución en términos de $x$.

### Caso donde $r(x)$ consiste en potencias de $x$, logaritmos naturales, o sumas y productos de estas funciones
Especialmente cuando la entrada $r(x)$ consiste en potencias de $x$, logaritmos naturales, o sumas y productos de estas funciones, podemos seleccionar directamente un $y_p$ adecuado siguiendo estas reglas para ecuaciones de Euler-Cauchy:

> **Reglas de selección para el método de coeficientes indeterminados: versión para ecuaciones de Euler-Cauchy**  
> **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:euler_cauchy}$) es una de las funciones en la primera columna de la tabla, seleccione $y_p$ de la misma fila en la segunda columna y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:euler_cauchy}$).  
> **(b) Regla de modificación**: Si el término seleccionado para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiplique este término por $\ln{x}$ (o por $(\ln{x})^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la ecuación diferencial homogénea).  
> **(c) Regla de suma**: Si $r(x)$ es una suma de funciones de la primera columna de la tabla, seleccione para $y_p$ la suma de las funciones correspondientes de la segunda columna.
>
> | Término en $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Esto nos permite encontrar $y_p$ de manera más rápida y sencilla para formas de entrada $r(x)$ de importancia práctica, obteniendo el mismo resultado que con el [cambio de variable](#cambio-de-variable). Estas reglas para ecuaciones de Euler-Cauchy pueden derivarse de las [reglas originales](#método-de-coeficientes-indeterminados) sustituyendo $\ln{x}$ en lugar de $x$.
