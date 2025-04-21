---
title: Método de coeficientes indeterminados
description: Exploremos el método de coeficientes indeterminados, una técnica útil en ingeniería para resolver problemas de valor inicial en ecuaciones diferenciales lineales no homogéneas con coeficientes constantes, aplicable a sistemas vibratorios y circuitos RLC.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Método de coeficientes indeterminados** se aplica a:
>   - Ecuaciones diferenciales lineales con **coeficientes constantes $a$ y $b$**
>   - Donde la entrada $r(x)$ consiste en funciones exponenciales, potencias de $x$, $\cos$ o $\sin$, o combinaciones de estas
>   - Ecuación diferencial lineal $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Reglas de selección para el método de coeficientes indeterminados**  
>   - **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, seleccione $y_p$ de la misma fila y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regla de modificación**: Si el término seleccionado para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica).  
>   - **(c) Regla de suma**: Si $r(x)$ es una suma de funciones de la primera columna de la tabla, seleccione para $y_p$ la suma de las funciones correspondientes de la segunda columna.
>
> | Término de $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerrequisitos
- [Ecuaciones diferenciales ordinarias lineales homogéneas de segundo orden](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskiano, existencia y unicidad de soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Ecuaciones diferenciales ordinarias lineales no homogéneas de segundo orden](/posts/nonhomogeneous-linear-odes-of-second-order/)

## Método de coeficientes indeterminados
Consideremos una ecuación diferencial ordinaria lineal no homogénea de segundo orden con $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

y la ecuación diferencial homogénea correspondiente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Según lo que vimos anteriormente en [Ecuaciones diferenciales ordinarias lineales no homogéneas de segundo orden](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver un problema de valor inicial para la ecuación diferencial lineal no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$), debemos encontrar $y_h$ resolviendo la ecuación diferencial homogénea ($\ref{eqn:homogeneous_linear_ode}$) y luego encontrar una solución particular $y_p$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) para obtener la solución general

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Entonces, ¿cómo encontramos $y_p$? El método general para encontrar $y_p$ es el **método de variación de parámetros**, pero en ciertos casos podemos aplicar el **método de coeficientes indeterminados**, que es mucho más simple. Este método es particularmente útil en ingeniería para sistemas vibratorios y modelos de circuitos eléctricos RLC.

El método de coeficientes indeterminados es adecuado para ecuaciones diferenciales lineales con **coeficientes constantes $a$ y $b$**, donde la entrada $r(x)$ consiste en funciones exponenciales, potencias de $x$, $\cos$ o $\sin$, o combinaciones de estas:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

La clave del método de coeficientes indeterminados es que estas formas de $r(x)$ tienen derivadas de forma similar a sí mismas. Para aplicar el método, seleccionamos un $y_p$ de forma similar a $r(x)$, pero con coeficientes indeterminados que se determinarán sustituyendo en la ecuación diferencial dada. Las reglas para seleccionar un $y_p$ apropiado para formas de $r(x)$ importantes en ingeniería son las siguientes:

> **Reglas de selección para el método de coeficientes indeterminados**  
> **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, seleccione $y_p$ de la misma fila y determine los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regla de modificación**: Si el término seleccionado para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica).  
> **(c) Regla de suma**: Si $r(x)$ es una suma de funciones de la primera columna de la tabla, seleccione para $y_p$ la suma de las funciones correspondientes de la segunda columna.
>
> | Término de $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método no solo es conveniente sino que también tiene la ventaja de ser autocorrectivo. Si seleccionamos incorrectamente $y_p$ o elegimos muy pocos términos, llegaremos a una contradicción; si elegimos demasiados términos, los coeficientes de los términos innecesarios resultarán ser cero, dando el resultado correcto. Incluso si algo sale mal al aplicar el método, lo notaremos naturalmente durante el proceso de resolución, por lo que podemos intentarlo sin preocupaciones siguiendo las reglas de selección anteriores.

### Demostración de la regla de suma
Consideremos una ecuación diferencial lineal no homogénea de la forma $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

Ahora, consideremos las dos ecuaciones con el mismo lado izquierdo pero con entradas $r_1$ y $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

Supongamos que estas ecuaciones tienen soluciones ${y_p}_1$ y ${y_p}_2$ respectivamente. Si denotamos el lado izquierdo de la ecuación como $L[y]$, entonces por la linealidad de $L[y]$, para $y_p = {y_p}_1 + {y_p}_2$ tenemos:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

### Ejemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Según la regla básica (a), ponemos $y_p = Ce^{\gamma x}$ y sustituimos en la ecuación dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### Caso donde $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar el coeficiente indeterminado $C$ y encontrar $y_p$ como sigue:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### Caso donde $\gamma^2 + a\gamma + b = 0$
En este caso, debemos aplicar la regla de modificación (b). Primero, usando que $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, encontremos las raíces de la ecuación característica de la ecuación diferencial homogénea $y^{\prime\prime} + ay^{\prime} + by = 0$:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

De esto obtenemos la base de la ecuación diferencial homogénea:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

##### Caso donde $\gamma \neq -a-\gamma$
Como el $Ce^{\gamma x}$ que seleccionamos para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente pero no una raíz doble, según la regla de modificación (b), multiplicamos este término por $x$ para obtener $y_p = Cxe^{\gamma x}$.

Ahora sustituimos este $y_p$ modificado en la ecuación dada $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### Caso donde $\gamma = -a-\gamma$
En este caso, como el $Ce^{\gamma x}$ que seleccionamos para $y_p$ corresponde a una raíz doble de la ecuación característica, según la regla de modificación (b), multiplicamos este término por $x^2$ para obtener $y_p = Cx^2 e^{\gamma x}$.

Ahora sustituimos este $y_p$ modificado en la ecuación dada $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
