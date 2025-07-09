---
title: "Método de los coeficientes indeterminados"
description: "Exploramos el método de los coeficientes indeterminados, una técnica útil en ingeniería para resolver problemas de valor inicial en EDOs lineales no homogéneas con coeficientes constantes, aplicable a sistemas de vibración, circuitos RLC y más."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Aplicación del **método de los coeficientes indeterminados**:
>   - EDOs lineales $y^{\prime\prime} + ay^{\prime} + by = r(x)$
>   - con **coeficientes constantes $a$ y $b$**, y
>   - donde el término de entrada $r(x)$ es una función exponencial, una potencia de $x$, $\cos$ o $\sin$, o una suma o producto de estas funciones.
> - **Reglas de elección para el método de los coeficientes indeterminados**  
>   - **(a) Regla básica (basic rule)**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, elija $y_p$ de la misma fila y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regla de modificación (modification rule)**: Si un término en su elección para $y_p$ es una solución de la EDO homogénea correspondiente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la EDO homogénea).  
>   - **(c) Regla de la suma (sum rule)**: Si $r(x)$ es una suma de funciones listadas en la primera columna de la tabla, elija para $y_p$ la suma de las funciones en las filas correspondientes de la segunda columna.
>
> | Término en $r(x)$ | Elección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerrequisitos
- [EDOs Lineales Homogéneas de Segundo Orden](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs Lineales Homogéneas de Segundo Orden con Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)
- [Wronskiano, Existencia y Unicidad de Soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [EDOs Lineales No Homogéneas de Segundo Orden](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Espacio vectorial, combinación lineal (álgebra lineal)

## Método de los coeficientes indeterminados
Consideremos una ecuación diferencial ordinaria lineal no homogénea de segundo orden con $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

y la ecuación diferencial ordinaria homogénea correspondiente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Como vimos en [EDOs Lineales No Homogéneas de Segundo Orden](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver un problema de valor inicial para la ecuación lineal no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$), primero debemos resolver la ecuación homogénea ($\ref{eqn:homogeneous_linear_ode}$) para encontrar $y_h$, y luego encontrar una solución particular $y_p$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) para obtener la solución general

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Entonces, ¿cómo encontramos $y_p$? Un método general para encontrar $y_p$ es el **método de variación de parámetros**, pero en algunos casos, se puede aplicar un método mucho más simple: el **método de los coeficientes indeterminados**. Este método es particularmente útil en ingeniería, ya que se puede aplicar a sistemas de vibración y modelos de circuitos eléctricos RLC.

El método de los coeficientes indeterminados es adecuado para ecuaciones diferenciales ordinarias lineales con **coeficientes constantes $a$ y $b$**, y donde el término de entrada $r(x)$ es una función exponencial, una potencia de $x$, $\cos$ o $\sin$, o una suma o producto de tales funciones:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

La clave del método de los coeficientes indeterminados es que este tipo de $r(x)$ tiene derivadas de forma similar a la propia función. Para aplicar el método, elegimos una $y_p$ que tenga una forma similar a $r(x)$ pero con coeficientes desconocidos, que se determinan sustituyendo $y_p$ y sus derivadas en la ecuación diferencial dada. Las reglas para elegir una $y_p$ apropiada para formas de $r(x)$ de importancia práctica en ingeniería son las siguientes.

> **Reglas de elección para el método de los coeficientes indeterminados**  
> **(a) Regla básica (basic rule)**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, elija $y_p$ de la misma fila y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regla de modificación (modification rule)**: Si un término en su elección para $y_p$ es una solución de la EDO homogénea correspondiente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la EDO homogénea).  
> **(c) Regla de la suma (sum rule)**: Si $r(x)$ es una suma de funciones listadas en la primera columna de la tabla, elija para $y_p$ la suma de las funciones en las filas correspondientes de la segunda columna.
>
> | Término en $r(x)$ | Elección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método no solo es simple, sino que también tiene la ventaja de ser autocorrector. Si elige una $y_p$ incorrecta o con muy pocos términos, llegará a una contradicción. Si elige demasiados términos, los coeficientes de los términos innecesarios resultarán ser $0$, lo que aún conduce al resultado correcto. Dado que cualquier error en la aplicación del método de los coeficientes indeterminados se hace evidente naturalmente durante el proceso de solución, puede intentarlo sin dudarlo siempre que haya elegido una $y_p$ razonablemente apropiada de acuerdo con las reglas de elección anteriores.

### Demostración de la regla de la suma
Consideremos una ecuación diferencial ordinaria lineal no homogénea de la forma $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Ahora, consideremos las siguientes dos ecuaciones con el mismo lado izquierdo pero con entradas $r_1$ y $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Supongamos que tienen soluciones particulares ${y_p}_1$ y ${y_p}_2$, respectivamente. Si denotamos el lado izquierdo de la ecuación dada como $L[y]$, entonces por la linealidad de $L[y]$, para $y_p = {y_p}_1 + {y_p}_2$, se cumple lo siguiente, lo que demuestra la regla de la suma.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Ejemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Según la regla básica (a), establecemos $y_p = Ce^{\gamma x}$ y lo sustituimos en la ecuación dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Caso en que $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar el coeficiente indeterminado $C$ y encontrar $y_p$ de la siguiente manera:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Caso en que $\gamma^2 + a\gamma + b = 0$
En este caso, debemos aplicar la regla de modificación (b). Primero, encontremos las raíces de la ecuación característica de la EDO homogénea $y^{\prime\prime} + ay^{\prime} + by = 0$ usando el hecho de que $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

A partir de esto, obtenemos la base de la EDO homogénea:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Caso en que $\gamma \neq -a-\gamma$
Dado que la elección para $y_p$, $Ce^{\gamma x}$, es una solución pero no una raíz doble de la EDO homogénea correspondiente, multiplicamos este término por $x$ según la regla de modificación (b), estableciendo $y_p = Cxe^{\gamma x}$.

Ahora, sustituyendo esta $y_p$ modificada de nuevo en la ecuación dada $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Caso en que $\gamma = -a-\gamma$
En este caso, la elección para $y_p$, $Ce^{\gamma x}$, es una raíz doble de la EDO homogénea correspondiente, por lo que multiplicamos este término por $x^2$ según la regla de modificación (b), estableciendo $y_p = Cx^2 e^{\gamma x}$.

Ahora, sustituyendo esta $y_p$ modificada de nuevo en la ecuación dada $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extensión del método de los coeficientes indeterminados: $r(x)$ como producto de funciones
Consideremos una ecuación diferencial ordinaria lineal no homogénea de la forma $r(x) = k x^n e^{\alpha x}\cos(\omega x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Si $r(x)$ es un producto de una función exponencial $e^{\alpha x}$, una potencia de $x$ ($x^m$), y $\cos{\omega x}$ o $\sin{\omega x}$ (aquí asumimos $\cos$ sin pérdida de generalidad), o una suma de tales funciones (es decir, si puede expresarse como una suma y producto de las funciones en la primera columna de la tabla anterior), mostraremos que existe una solución de la ecuación, $y_p$, que es una suma y producto de las funciones en la segunda columna de la misma tabla.

> Algunas partes se describen utilizando álgebra lineal para una demostración rigurosa, y estas partes están marcadas con un \*. Puede omitir estas partes y aun así obtener una comprensión general.
{: .prompt-tip }

### Definición del espacio vectorial $V$*
Para un $r(x)$ tal que
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

podemos definir un espacio vectorial $V$ tal que $r(x) \in V$ de la siguiente manera:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forma de las derivadas de funciones exponenciales, polinómicas y trigonométricas
Las formas de las derivadas de las funciones básicas presentadas en la primera columna de la tabla anterior son las siguientes:
- Función exponencial: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Función polinómica: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Función trigonométrica: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

La derivada obtenida al diferenciar estas funciones también se expresa como una <u>suma del mismo tipo de funciones</u>.

Por lo tanto, si las funciones $f$ y $g$ son las funciones anteriores o sumas de ellas, aplicando la regla del producto a $r(x) = f(x)g(x)$:

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

Aquí, $f$, $f^{\prime}$, $f^{\prime\prime}$ y $g$, $g^{\prime}$, $g^{\prime\prime}$ pueden escribirse como sumas o múltiplos constantes de funciones exponenciales, polinómicas y trigonométricas. Por lo tanto, $r^{\prime}(x) = (fg)^{\prime}$ y $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ también pueden expresarse como sumas y productos de estas funciones, al igual que $r(x)$.

### Invariancia de $V$ bajo el operador de diferenciación $D$ y la transformación lineal $L$*
Es decir, no solo $r(x)$ mismo, sino también $r^{\prime}(x)$ y $r^{\prime\prime}(x)$ son combinaciones lineales de términos de la forma $x^k e^{\alpha x}\cos(\omega x)$ y $x^k e^{\alpha x}\sin(\omega x)$, por lo que

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Si no nos limitamos a $r(x)$ e introducimos el operador de diferenciación $D$ para todos los elementos del espacio vectorial $V$ definido anteriormente, podemos expresarlo de manera más general: *el espacio vectorial $V$ es cerrado bajo el operador de diferenciación $D$*. Por lo tanto, si denotamos el lado izquierdo de la ecuación dada $y^{\prime\prime} + ay^{\prime} + by$ como $L[y]$, entonces *$V$ es invariante bajo $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Dado que $r(x) \in V$ y $V$ es invariante bajo $L$, existe otro elemento $y_p$ en $V$ que satisface $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Por lo tanto, si elegimos una $y_p$ apropiada para que sea la suma de todos los términos de producto posibles, utilizando coeficientes indeterminados $A_0, A_1, \dots, A_n$ y $K, M$ de la siguiente manera, podemos determinar los coeficientes indeterminados sustituyendo $y_p$ (o $xy_p$, $x^2y_p$) y sus derivadas en la ecuación dada, de acuerdo con la regla básica (a) y la regla de modificación (b). Aquí, $n$ se puede determinar según el grado de $x$ en $r(x)$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Si la entrada dada $r(x)$ incluye varios valores diferentes de $\alpha_i$ y $\omega_j$, debe elegir $y_p$ para incluir exhaustivamente todos los términos posibles de la forma $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ y $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ para cada valor de $\alpha_i$ y $\omega_j$.  
> La ventaja del método de los coeficientes indeterminados es su simplicidad, por lo que si el ansatz se vuelve demasiado complejo y esta ventaja se desvanece, podría ser mejor aplicar el método de variación de parámetros, que se discutirá más adelante.
{: .prompt-warning }

## Extensión del método de los coeficientes indeterminados: Ecuación de Euler-Cauchy
Además de las [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), el método de los coeficientes indeterminados también se puede utilizar para la [ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Sustitución de variables
Hemos visto anteriormente que al [transformar a una EDO lineal homogénea de segundo orden con coeficientes constantes mediante la sustitución $x = e^t$](/posts/euler-cauchy-equation/#transformación-a-una-edo-lineal-homogénea-de-segundo-orden-con-coeficientes-constantes), tenemos

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

lo que permite transformar la ecuación de Euler-Cauchy en la siguiente EDO lineal homogénea con coeficientes constantes en términos de $t$:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Ahora, podemos aplicar el [método de los coeficientes indeterminados que hemos discutido anteriormente](#método-de-los-coeficientes-indeterminados) a la ecuación ($\ref{eqn:substituted}$) para resolverla en términos de $t$, y finalmente, usar $t = \ln x$ para encontrar la solución en términos de $x$.

### Caso en que $r(x)$ es una potencia de $x$, un logaritmo natural, o una suma o producto de estas funciones
En particular, si el término de entrada $r(x)$ consiste en potencias de $x$, logaritmos naturales, o sumas y productos de tales funciones, podemos elegir directamente una $y_p$ apropiada de acuerdo con las siguientes reglas de elección para la ecuación de Euler-Cauchy.

> **Reglas de elección para el método de los coeficientes indeterminados: para la ecuación de Euler-Cauchy**  
> **(a) Regla básica (basic rule)**: Si $r(x)$ en la ecuación ($\ref{eqn:euler_cauchy}$) es una de las funciones en la primera columna de la tabla, elija $y_p$ de la misma fila y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:euler_cauchy}$).  
> **(b) Regla de modificación (modification rule)**: Si un término en su elección para $y_p$ es una solución de la EDO homogénea correspondiente $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiplique este término por $\ln{x}$ (o por $(\ln{x})^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la EDO homogénea).  
> **(c) Regla de la suma (sum rule)**: Si $r(x)$ es una suma de funciones listadas en la primera columna de la tabla, elija para $y_p$ la suma de las funciones en las filas correspondientes de la segunda columna.
>
> | Término en $r(x)$ | Elección para $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

De esta manera, para formas de entrada $r(x)$ de importancia práctica, podemos encontrar la misma $y_p$ que se obtendría mediante la [sustitución de variables](#sustitución-de-variables) de una manera más rápida y sencilla. Podemos derivar estas reglas de elección para la ecuación de Euler-Cauchy sustituyendo $\ln{x}$ en lugar de $x$ en las [reglas de elección originales](#método-de-los-coeficientes-indeterminados) que vimos anteriormente.
