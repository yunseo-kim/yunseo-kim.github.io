---
title: "El pozo cuadrado infinito unidimensional"
description: >-
  Examinamos el problema del pozo cuadrado infinito unidimensional, un ejemplo simple pero importante que ilustra bien los conceptos básicos de la mecánica cuántica. En esta situación ideal, encontramos el n-ésimo estado estacionario ψ(x) y la energía E de la partícula, y exploramos 4 importantes propiedades matemáticas de ψ(x). A partir de esto, obtenemos la solución general Ψ(x,t).
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
---

## TL;DR
> - Problema del pozo cuadrado infinito unidimensional: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{en otros casos}
>   \end{cases}$$
> - Condiciones de contorno: $ \psi(0) = \psi(a) = 0 $
> - Nivel de energía del n-ésimo estado estacionario: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Solución de la ecuación de Schrödinger independiente del tiempo dentro del pozo:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Interpretación física de cada estado estacionario $\psi_n$: 
>   - Forma de onda estacionaria en una cuerda de longitud $a$
>   - **Estado fundamental**: estado estacionario $\psi_1$ con la energía más baja
>   - **Estados excitados**: estados restantes con $n\geq 2$ cuya energía aumenta proporcionalmente a $n^2$
> - 4 importantes propiedades matemáticas de $\psi_n$:
>   1. Si el potencial $V(x)$ tiene simetría, las funciones pares e impares aparecen alternadamente respecto al centro del pozo
>   2. A medida que aumenta la energía, cada estado consecutivo tiene un **nodo** más
>   3. Posee **ortonormalidad**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. Posee **completitud**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Solución general de la ecuación de Schrödinger (combinación lineal de estados estacionarios):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{donde el coeficiente }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Prerrequisitos
- Distribución de probabilidad continua y densidad de probabilidad
- Ortogonalidad y normalización (álgebra lineal)
- Series de Fourier y completitud (álgebra lineal)
- [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Teorema de Ehrenfest](/posts/ehrenfest-theorem/)
- [Ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/)

## Condición de potencial dada
Si el potencial es

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{en otros casos}
\end{cases} \tag{1}$$

entonces la partícula dentro de este potencial es una partícula libre en el rango $0<x<a$ y no puede escapar debido a una fuerza infinita que actúa en ambos extremos ($x=0$ y $x=a$). En un modelo clásico, esto se interpreta como un movimiento de ida y vuelta infinito sin fuerzas no conservativas, repitiendo colisiones perfectamente elásticas hacia adelante y hacia atrás. Aunque este potencial es extremadamente artificial y simple, precisamente por eso puede ser un caso de referencia útil al examinar otras situaciones físicas mientras se estudia la mecánica cuántica, por lo que es necesario examinarlo cuidadosamente.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Configuración del modelo y condiciones de contorno
Fuera del pozo, la probabilidad de encontrar la partícula es $0$, por lo que $\psi(x)=0$. Dentro del pozo, $V(x)=0$, por lo que la [ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/) es

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

es decir,

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ donde } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

> Aquí se asume que $E\geq 0$.
{: .prompt-info }

Esta es la ecuación que describe un **oscilador armónico simple** clásico, y la solución general es

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

donde $A$ y $B$ son constantes arbitrarias que típicamente se determinan por las **condiciones de contorno** dadas en el problema al buscar una solución particular. <u>En el caso de $\psi(x)$, normalmente la condición de contorno es que tanto $\psi$ como $d\psi/dx$ sean continuas, pero donde el potencial se vuelve infinito, solo $\psi$ es continua.</u>

## Encontrar la solución de la ecuación de Schrödinger independiente del tiempo

Como $\psi(x)$ es continua,

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

debe conectarse con la solución fuera del pozo. En la ecuación ($\ref{eqn:psi_general_solution}$), cuando $x=0$

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

por lo tanto, sustituyendo ($\ref{eqn:boundary_conditions}$), $B$ debe ser $0$.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Entonces, como $\psi(a)=A\sin{ka}$, para satisfacer $\psi(a)=0$ de la ecuación ($\ref{eqn:boundary_conditions}$), $A=0$ (solución trivial) o $\sin{ka}=0$. Por lo tanto,

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Aquí también, $k=0$ es una solución trivial y resulta en $\psi(x)=0$, que no se puede normalizar, por lo que no es la solución que buscamos en este problema. Además, como $\sin(-\theta)=-\sin(\theta)$, el signo negativo puede ser absorbido en $A$ en la ecuación ($\ref{eqn:psi_without_B}$), por lo que considerar solo el caso $ka>0$ no pierde generalidad. Por lo tanto, las posibles soluciones para $k$ son

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Entonces $\psi_n=A\sin{k_n x}$ y $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, por lo que sustituyendo en la ecuación ($\ref{eqn:t_independent_schrodinger_eqn}$), los posibles valores de $E$ son:

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

En marcado contraste con el caso clásico, una partícula cuántica en un pozo cuadrado infinito no puede tener cualquier energía, sino que debe tener uno de los valores permitidos.

> La energía se cuantiza debido a las condiciones de contorno aplicadas a la solución de la ecuación de Schrödinger independiente del tiempo.
{: .prompt-info }

Ahora podemos encontrar $A$ normalizando $\psi$.

> Originalmente, se normaliza $\Psi(x,t)$, pero según la ecuación (11) de la [ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/#1-son-estados-estacionarios), esto equivale a normalizar $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

Esto determina estrictamente solo la magnitud de $A$, pero como la fase de $A$ no tiene ningún significado físico, podemos usar simplemente la raíz cuadrada real positiva como $A$. Por lo tanto, la solución dentro del pozo es

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Interpretación física de cada estado estacionario $\psi_n$
Como en la ecuación ($\ref{eqn:psi_n}$), hemos encontrado infinitas soluciones de la ecuación de Schrödinger independiente del tiempo para cada nivel de energía $n$. Si dibujamos los primeros pocos de estos en un gráfico, se verían como la siguiente imagen.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Estos estados toman la forma de ondas estacionarias en una cuerda de longitud $a$, y $\psi_1$, que tiene la energía más baja, se llama **estado fundamental**, mientras que los estados restantes con $n\geq 2$, cuya energía aumenta proporcionalmente a $n^2$, se llaman **estados excitados**.

## 4 importantes propiedades matemáticas de $\psi_n$
Todas las funciones $\psi_n(x)$ tienen las siguientes 4 importantes propiedades. Estas cuatro propiedades son muy poderosas y no se limitan solo al pozo cuadrado infinito. La primera propiedad siempre se cumple si el potencial mismo es una función con simetría, y la segunda, tercera y cuarta propiedades son propiedades generales que aparecen independientemente de la forma del potencial.

### 1. Las funciones pares e impares aparecen alternadamente con respecto al centro del pozo.
Para enteros positivos $n$, $\psi_{2n-1}$ es una función par y $\psi_{2n}$ es una función impar.

### 2. A medida que aumenta la energía, cada estado consecutivo tiene un nodo más.
Para enteros positivos $n$, $\psi_n$ tiene $(n-1)$ **nodos**.

### 3. Estos estados poseen ortogonalidad.

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

En este sentido, son **ortogonales** entre sí.

> En el caso del pozo cuadrado infinito que estamos examinando ahora, $\psi$ es real, por lo que no es necesario tomar el conjugado complejo ($^*$) de $\psi_m$, pero es bueno acostumbrarse a incluirlo siempre para casos en los que no sea así.
{: .prompt-tip }

#### Demostración
Cuando $m\neq n$,

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

Cuando $m=n$, esta integral es $1$ debido a la normalización, y usando la **delta de Kronecker** $\delta_{mn}$, la ortogonalidad y la normalización se pueden expresar juntas como

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

En este caso, se dice que $\psi$ está **ortonormalizada**.

### 4. Estas funciones poseen completitud.
En el sentido de que cualquier otra función $f(x)$ se puede escribir como una combinación lineal

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

estas funciones son **completas**. La ecuación ($\ref{eqn:fourier_series}$) es la **serie de Fourier** de $f(x)$, y el hecho de que cualquier función se pueda expandir de esta manera se llama **teorema de Dirichlet**.

## Cálculo de los coeficientes $c_n$ usando el truco de Fourier
Cuando se da $f(x)$, se pueden encontrar los coeficientes $c_n$ usando el siguiente método llamado **truco de Fourier**, utilizando la completitud y la ortonormalidad mencionadas anteriormente. Multiplicando ambos lados de la ecuación ($\ref{eqn:fourier_series}$) por $\psi_m(x)^*$ e integrando, por las ecuaciones ($\ref{eqn:orthonomality}$) y ($\ref{eqn:kronecker_delta}$),

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Nótese que debido a la delta de Kronecker, todos los términos en la suma excepto el término $n=m$ desaparecen.
{: .prompt_info }

Por lo tanto, el coeficiente n-ésimo al expandir $f(x)$ es

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Encontrar la solución general $\Psi(x,t)$ de la ecuación de Schrödinger dependiente del tiempo
Cada estado estacionario del pozo cuadrado infinito, según la ecuación (10) del post ['Ecuación de Schrödinger independiente del tiempo'](/posts/time-independent-schrodinger-equation/#1-son-estados-estacionarios) y la ecuación ($\ref{eqn:psi_n}$) que encontramos anteriormente, es

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

Además, en la [ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/#3-la-solución-general-de-la-ecuación-de-schrödinger-dependiente-del-tiempo-es-una-combinación-lineal-de-soluciones-separadas), vimos anteriormente que la solución general de la ecuación de Schrödinger se puede expresar como una combinación lineal de estados estacionarios. Por lo tanto, podemos escribir

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

Ahora solo necesitamos encontrar los coeficientes $c_n$ que satisfacen la siguiente condición:

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

Por la completitud de $\psi$ que examinamos anteriormente, siempre existen $c_n$ que satisfacen lo anterior, y se pueden encontrar sustituyendo $\Psi(x,0)$ por $f(x)$ en la ecuación ($\ref{eqn:coefficients_n}$).

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

Si se da $\Psi(x,0)$ como condición inicial, se pueden encontrar los coeficientes de expansión $c_n$ usando la ecuación ($\ref{eqn:calc_of_cn}$), y luego sustituirlos en la ecuación ($\ref{eqn:general_solution}$) para encontrar $\Psi(x,t)$. Después de eso, se puede calcular cualquier cantidad física de interés siguiendo el proceso del [teorema de Ehrenfest](/posts/ehrenfest-theorem/). Este método se puede aplicar no solo al pozo cuadrado infinito sino también a cualquier potencial, solo cambiando la forma de las funciones $\psi$ y la ecuación para los niveles de energía permitidos.

## Derivación de la conservación de la energía ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Derivemos la conservación de la energía que examinamos brevemente en la [ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/#conservación-de-la-energía) utilizando la ortonormalidad de $\psi(x)$ (ecuaciones [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]). Como $c_n$ es independiente del tiempo, es suficiente demostrar que es cierto para el caso $t=0$.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

Además, como

$$ \hat{H}\psi_n = E_n\psi_n $$

obtenemos lo siguiente:

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
