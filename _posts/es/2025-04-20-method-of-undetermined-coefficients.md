---
title: "Método de coeficientes indeterminados"
description: "Exploremos el método de coeficientes indeterminados, una técnica de resolución útil y frecuentemente utilizada en ingeniería para sistemas oscilatorios, modelos de circuitos RLC eléctricos, etc., que permite resolver de manera simple problemas de valor inicial para EDOs lineales no homogéneas de coeficientes constantes con formas específicas."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Aplicación del método de coeficientes indeterminados**:
>   - **Coeficientes constantes $a$ y $b$** y
>   - Entrada $r(x)$ compuesta por funciones exponenciales, potencias de $x$, $\cos$ o $\sin$, o sumas y productos de tales funciones
>   - Ecuación diferencial ordinaria lineal $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Reglas de selección para el método de coeficientes indeterminados**  
>   - **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, selecciona $y_p$ de la misma fila y determina los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regla de modificación**: Si el término seleccionado para $y_p$ resulta ser una solución de la ecuación diferencial homogénea $y^{\prime\prime} + ay^{\prime} + by = 0$ correspondiente a la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$), multiplica este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la ecuación diferencial homogénea).  
>   - **(c) Regla de suma**: Si $r(x)$ es una suma de funciones en la primera columna de la tabla, selecciona como $y_p$ la suma de las funciones correspondientes en la segunda columna.
>
> | Término de $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerrequisitos
- [EDOs Lineales Homogéneas de Segundo Orden](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)
- [Wronskiano, existencia y unicidad de soluciones](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [EDOs Lineales No Homogéneas de Segundo Orden](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Espacios vectoriales, generación lineal (álgebra lineal)

## Método de coeficientes indeterminados
Consideremos la ecuación diferencial ordinaria lineal no homogénea de segundo orden

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

donde $r(x) \not\equiv 0$, y la ecuación diferencial homogénea correspondiente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Como vimos anteriormente en [EDOs Lineales No Homogéneas de Segundo Orden](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver el problema de valor inicial de la ecuación diferencial lineal no homogénea ($\ref{eqn:nonhomogeneous_linear_ode}$), necesitamos resolver la ecuación diferencial homogénea ($\ref{eqn:homogeneous_linear_ode}$) para obtener $y_h$, luego encontrar una solución particular $y_p$ de la ecuación ($\ref{eqn:nonhomogeneous_linear_ode}$) para obtener la solución general

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Entonces, ¿cómo podemos encontrar $y_p$? El método general para encontrar $y_p$ es el **método de variación de parámetros**, pero en ciertos casos se puede aplicar el **método de coeficientes indeterminados**, que es mucho más simple. Especialmente, es un método frecuentemente utilizado en ingeniería ya que se puede aplicar a sistemas oscilatorios y modelos de circuitos RLC eléctricos.

El método de coeficientes indeterminados es adecuado para ecuaciones diferenciales lineales con **coeficientes constantes $a$ y $b$**, donde la entrada $r(x)$ está compuesta por funciones exponenciales, potencias de $x$, $\cos$ o $\sin$, o sumas y productos de tales funciones

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

La clave del método de coeficientes indeterminados es que tales formas de $r(x)$ tienen derivadas de forma similar a sí mismas. Para aplicar el método de coeficientes indeterminados, seleccionamos $y_p$ de forma similar a $r(x)$ pero con coeficientes desconocidos que se determinan sustituyendo $y_p$ y sus derivadas en la ecuación diferencial dada. Las reglas para seleccionar $y_p$ apropiado para formas de $r(x)$ prácticamente importantes en ingeniería son las siguientes.

> **Reglas de selección para el método de coeficientes indeterminados**  
> **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$) es una de las funciones en la primera columna de la tabla, selecciona $y_p$ de la misma fila y determina los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regla de modificación**: Si el término seleccionado para $y_p$ resulta ser una solución de la ecuación diferencial homogénea $y^{\prime\prime} + ay^{\prime} + by = 0$ correspondiente a la ecuación ($\ref{eqn:linear_ode_with_constant_coefficients}$), multiplica este término por $x$ (o por $x^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la ecuación diferencial homogénea).  
> **(c) Regla de suma**: Si $r(x)$ es una suma de funciones en la primera columna de la tabla, selecciona como $y_p$ la suma de las funciones correspondientes en la segunda columna.
>
> | Término de $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método no solo es conveniente sino que también tiene la ventaja de ser autocorrectivo. Si seleccionamos $y_p$ incorrectamente o seleccionamos muy pocos términos, llegaremos a una contradicción, y si seleccionamos demasiados términos, los coeficientes de los términos innecesarios se vuelven $0$ y obtenemos el resultado correcto. Incluso si algo sale mal al aplicar el método de coeficientes indeterminados, nos daremos cuenta naturalmente durante el proceso de resolución, por lo que si seleccionamos un $y_p$ razonablemente apropiado según las reglas de selección anteriores, podemos intentarlo sin preocupación.

### Demostración de la regla de suma
Consideremos la ecuación diferencial lineal no homogénea

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

donde $r(x) = r_1(x) + r_2(x)$. Ahora supongamos que las siguientes dos ecuaciones con el mismo lado izquierdo pero con entradas $r_1$ y $r_2$ respectivamente

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

tienen ${y_p}\_1$ y ${y_p}\_2$ como soluciones respectivamente. Si denotamos el lado izquierdo de la ecuación dada como $L[y]$, entonces por la linealidad de $L[y]$, para $y\_p = {y_p}\_1 + {y_p}\_2$ se cumple lo siguiente, por lo que la regla de suma es válida.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Ejemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Según la regla básica (a), ponemos $y_p = Ce^{\gamma x}$ y lo sustituimos en la ecuación dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Caso donde $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar el coeficiente indeterminado $C$ y obtener $y_p$ como sigue:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Caso donde $\gamma^2 + a\gamma + b = 0$
En este caso debemos aplicar la regla de modificación (b). Primero, usando $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, encontremos las raíces de la ecuación característica de la ecuación diferencial homogénea $y^{\prime\prime} + ay^{\prime} + by = 0$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

De esto obtenemos la base de la ecuación diferencial homogénea

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Caso donde $\gamma \neq -a-\gamma$
Como $Ce^{\gamma x}$ que seleccionamos para $y_p$ es una solución de la ecuación diferencial homogénea correspondiente a la ecuación dada pero no es una raíz doble, según la regla de modificación (b) multiplicamos este término por $x$ y ponemos $y_p = Cxe^{\gamma x}$.

Ahora sustituyendo el $y_p$ modificado en la ecuación dada $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Caso donde $\gamma = -a-\gamma$
En este caso, $Ce^{\gamma x}$ que seleccionamos para $y_p$ es una raíz doble de la ecuación diferencial homogénea correspondiente a la ecuación dada, por lo que según la regla de modificación (b) multiplicamos este término por $x^2$ y ponemos $y_p = Cx^2 e^{\gamma x}$.

Ahora sustituyendo el $y_p$ modificado en la ecuación dada $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extensión del método de coeficientes indeterminados: $r(x)$ en forma de productos de funciones
Consideremos la ecuación diferencial lineal no homogénea

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

donde $r(x) = k x^n e^{\alpha x}\cos(\omega x)$. Si $r(x)$ se puede expresar como una función exponencial $e^{\alpha x}$, una potencia de $x$ como $x^m$, $\cos{\omega x}$ o $\sin{\omega x}$ (aquí asumimos $\cos$ sin pérdida de generalidad), o sumas y productos de tales funciones (es decir, se puede expresar como sumas y productos de las funciones en la primera columna de la tabla anterior), demostraremos que existe una solución $y_p$ de la ecuación que es una suma y producto de las funciones en la segunda columna de la misma tabla.

> Para una demostración rigurosa, se utilizan algunas partes de álgebra lineal, que están marcadas con \*. Se puede omitir estas partes marcadas con \* y leer solo el resto para una comprensión general sin problemas.
{: .prompt-tip }

### Definición del espacio vectorial $V$\*
Para $r(x)$ de la forma

$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

podemos tomar el espacio vectorial $V$ tal que $r(x) \in V$ como sigue:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Formas de las derivadas de funciones exponenciales, polinomiales y trigonométricas
Las formas de las derivadas de las funciones básicas presentadas en la primera columna de la tabla anterior son las siguientes:
- Función exponencial: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Función polinomial: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Funciones trigonométricas: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Las derivadas obtenidas al diferenciar estas funciones también se expresan como <u>sumas de funciones del mismo tipo</u>.

Por lo tanto, cuando las funciones $f$ y $g$ son las funciones anteriores o sumas de ellas, aplicando la regla del producto a $r(x) = f(x)g(x)$ obtenemos

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

donde $f$, $f^{\prime}$, $f^{\prime\prime}$ y $g$, $g^{\prime}$, $g^{\prime\prime}$ se pueden escribir todas como sumas o múltiplos constantes de funciones exponenciales, polinomiales y trigonométricas. Por lo tanto, $r^{\prime}(x) = (fg)^{\prime}$ y $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ también se pueden expresar como sumas y productos de estas funciones, al igual que $r(x)$.

### Invariancia del espacio vectorial $V$ bajo la operación de diferenciación $D$ y la transformación lineal $L$\*
Es decir, no solo $r(x)$ sino también $r^{\prime}(x)$ y $r^{\prime\prime}(x)$ son combinaciones lineales de términos de la forma $x^k e^{\alpha x}\cos(\omega x)$ y términos de la forma $x^k e^{\alpha x}\sin(\omega x)$, por lo que

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Expresando esto más generalmente introduciendo el operador de diferenciación $D$ para todos los elementos del espacio vectorial $V$ definido anteriormente, no limitándose a $r(x)$, *el espacio vectorial $V$ está cerrado bajo la operación de diferenciación $D$*. Por lo tanto, si denotamos el lado izquierdo de la ecuación dada $y^{\prime\prime} + ay^{\prime} + by$ como $L[y]$, entonces *$V$ es invariante bajo $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Como $r(x) \in V$ y $V$ es invariante bajo $L$, existe otro elemento $y_p$ de $V$ que satisface $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Por lo tanto, si seleccionamos apropiadamente $y_p$ para que sea la suma de todos los posibles términos de forma de producto usando coeficientes indeterminados $A_0, A_1, \dots, A_n$ y $K$, $M$ como sigue, podemos determinar los coeficientes indeterminados sustituyendo $y_p$ (o $xy_p$, $x^2y_p$) y sus derivadas en la ecuación dada según las reglas básica (a) y de modificación (b). Aquí, $n$ se puede determinar según el grado de $r(x)$ con respecto a $x$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Si la entrada dada $r(x)$ incluye varios valores diferentes de $\alpha_i$ y $\omega_j$, también se debe seleccionar $y_p$ para incluir todos los posibles términos de la forma $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ y $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ para cada valor de $\alpha_i$ y $\omega_j$.  
> La ventaja del método de coeficientes indeterminados es su simplicidad, por lo que si el ansatz se vuelve demasiado complejo y esta ventaja se desvanece, podría ser mejor aplicar el método de variación de parámetros que trataremos más adelante.
{: .prompt-warning }

## Extensión del método de coeficientes indeterminados: Ecuación de Euler-Cauchy
No solo para [EDOs lineales homogéneas de segundo orden con coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), sino también para la [ecuación de Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

se puede utilizar el método de coeficientes indeterminados.

### Sustitución de variables
[Sustituyendo $x = e^t$ para transformar en una EDO lineal homogénea de segundo orden con coeficientes constantes](/posts/euler-cauchy-equation/#transformación-a-edo-lineal-homogénea-de-segundo-orden-con-coeficientes-constantes) obtenemos

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

por lo que la ecuación de Euler-Cauchy se puede transformar en la siguiente ecuación diferencial homogénea con coeficientes constantes en $t$, como vimos anteriormente:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Ahora podemos aplicar el [método de coeficientes indeterminados que examinamos anteriormente](#método-de-coeficientes-indeterminados) de la misma manera a la ecuación ($\ref{eqn:substituted}$) para resolver con respecto a $t$, y finalmente obtener la solución con respecto a $x$ usando $t = \ln x$.

### Caso donde $r(x)$ es una potencia de $x$, logaritmo natural, o sumas y productos de tales funciones
Especialmente cuando la entrada $r(x)$ está compuesta por potencias de $x$, logaritmo natural, o sumas y productos de tales funciones, se puede seleccionar directamente un $y_p$ apropiado según las siguientes reglas de selección para ecuaciones de Euler-Cauchy.

> **Reglas de selección para el método de coeficientes indeterminados: Para ecuaciones de Euler-Cauchy**  
> **(a) Regla básica**: Si $r(x)$ en la ecuación ($\ref{eqn:euler_cauchy}$) es una de las funciones en la primera columna de la tabla, selecciona $y_p$ de la misma fila y determina los coeficientes indeterminados sustituyendo $y_p$ y sus derivadas en la ecuación ($\ref{eqn:euler_cauchy}$).  
> **(b) Regla de modificación**: Si el término seleccionado para $y_p$ resulta ser una solución de la ecuación diferencial homogénea $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ correspondiente a la ecuación ($\ref{eqn:euler_cauchy}$), multiplica este término por $\ln{x}$ (o por $(\ln{x})^2$ si esta solución corresponde a una raíz doble de la ecuación característica de la ecuación diferencial homogénea).  
> **(c) Regla de suma**: Si $r(x)$ es una suma de funciones en la primera columna de la tabla, selecciona como $y_p$ la suma de las funciones correspondientes en la segunda columna.
>
> | Término de $r(x)$ | Selección para $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

De esta manera se puede encontrar el mismo $y_p$ que se obtiene mediante [sustitución de variables](#sustitución-de-variables) de forma más rápida y conveniente para formas de entrada $r(x)$ prácticamente importantes. Se pueden derivar estas reglas de selección para ecuaciones de Euler-Cauchy sustituyendo $\ln{x}$ en lugar de $x$ en las [reglas de selección originales](#método-de-coeficientes-indeterminados).
