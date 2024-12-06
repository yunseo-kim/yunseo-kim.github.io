---
title: "Solución analítica del oscilador armónico (The Harmonic Oscillator)"
description: >-
  Establecemos la ecuación de Schrödinger para el oscilador armónico en mecánica cuántica y examinamos su solución analítica.
  Resolvemos la ecuación introduciendo la variable adimensional 𝜉 y expresamos cualquier estado estacionario normalizado utilizando polinomios de Hermite.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hermite Polynomials]
math: true
---

## TL;DR
> - Cualquier oscilación puede aproximarse a una oscilación armónica simple si la amplitud es lo suficientemente pequeña, lo que hace que la oscilación armónica simple sea importante en física
> - Oscilador armónico: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - Introducción de la variable adimensional $\xi$ y la energía $K$ expresada en unidades de $\cfrac{1}{2}\hbar\omega$:
>   - $\xi \equiv \sqrt{\cfrac{m\omega}{\hbar}}x$
>   - $K \equiv \cfrac{2E}{\hbar\omega}$
>   - $ \cfrac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi $
> - Cuando $\|\xi\|^2 \to \infty$, la solución asintótica físicamente permitida es $\psi(\xi) \to Ae^{-\xi^2/2}$, por lo tanto,
>
> $$ \begin{gather*}
> \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(donde }\lim_{\xi\to\infty}h(\xi)=A\text{)}, \\
> \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0
> \end{gather*} $$
>
> - Si expresamos la solución de esta ecuación en forma de serie $ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j$,
>
> $$ a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j $$
>
> - Para que esta solución sea normalizable, la serie $\sum a_j$ debe ser finita, es decir, debe existir un valor 'máximo' de $j$, $n\in \mathbb{N}$, tal que $a_j=0$ para $j>n$, por lo tanto
>   - $ K = 2n + 1 $
>   - $ E_n = \left(n+\cfrac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots $
> - En general, $h_n(\xi)$ es un polinomio de grado $n$ en $\xi$, y el resto, excluyendo el coeficiente inicial ($a_0$ o $a_1$), se denomina **polinomio de Hermite (Hermite polynomials)** $H_n(\xi)$
>
> $$ h_n(\xi) = 
> \begin{cases}
> a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
> a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
> \end{cases} $$
>
> - Estado estacionario normalizado del oscilador armónico:
>
> $$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2} $$
>
> - Características del oscilador cuántico
>   - Las funciones propias alternan entre funciones pares e impares
>   - Existe una probabilidad no nula de encontrar la partícula en regiones clásicamente prohibidas (más allá de la amplitud clásica para una $E$ dada)
>   - Para todos los estados estacionarios con $n$ impar, la probabilidad de encontrar la partícula en el centro es $0$
>   - A medida que $n$ aumenta, el oscilador cuántico se asemeja más al oscilador clásico
{: .prompt-info }

## Prerequisites
- [Método de separación de variables](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Teorema de Ehrenfest](/posts/ehrenfest-theorem/)
- [Ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/)
- [Pozo cuadrado infinito unidimensional](/posts/the-infinite-square-well/)
- [Solución algebraica del oscilador armónico](/posts/algebraic-solution-of-the-harmonic-oscillator/)

## Configuración del modelo
Para una descripción del oscilador armónico en mecánica clásica y la importancia del problema del oscilador armónico, consulte el [artículo anterior](/posts/algebraic-solution-of-the-harmonic-oscillator/).

### El oscilador armónico en mecánica cuántica
El problema del oscilador armónico cuántico consiste en resolver la ecuación de Schrödinger para el potencial

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{1}$$

La [ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/) para el oscilador armónico es

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

Hay dos enfoques completamente diferentes para resolver este problema. Uno es el método analítico utilizando **series de potencias**, y el otro es el método algebraico utilizando **operadores de escalera**. Aunque el método algebraico es más rápido y simple, también es necesario estudiar la solución analítica utilizando series de potencias. [Anteriormente hemos tratado el método de solución algebraica](/posts/algebraic-solution-of-the-harmonic-oscillator/), y aquí trataremos el método de solución analítica.

## Transformación de la ecuación de Schrödinger
Introduciendo la variable adimensional

$$ \xi \equiv \sqrt{\frac{m\omega}{\hbar}}x \label{eqn:xi}\tag{3}$$

podemos simplificar la ecuación de Schrödinger independiente del tiempo ($\ref{eqn:t_independent_schrodinger_eqn}$) de la siguiente manera:

$$ \frac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi. \label{eqn:schrodinger_eqn_with_xi}\tag{4}$$

Aquí, $K$ es la energía expresada en unidades de $\cfrac{1}{2}\hbar\omega$.

$$ K \equiv \frac{2E}{\hbar\omega}. \label{eqn:K}\tag{5}$$

Ahora debemos resolver esta ecuación reescrita ($\ref{eqn:schrodinger_eqn_with_xi}$). Primero, para valores muy grandes de $\xi$ (es decir, para valores muy grandes de $x$), $\xi^2 \gg K$, por lo que

$$ \frac{d^2\psi}{d\xi^2} \approx \xi^2\psi \label{eqn:schrodinger_eqn_approx}\tag{6}$$

y la solución aproximada a esto es

$$ \psi(\xi) \approx Ae^{-\xi^2/2} + Be^{\xi^2/2} \label{eqn:psi_approx}\tag{7}$$

Sin embargo, el término $B$ diverge cuando $\|x\|\to \infty$ y no se puede normalizar, por lo que la solución asintótica físicamente permitida es

$$ \psi(\xi) \to Ae^{-\xi^2/2} \label{eqn:psi_asymp}\tag{8}$$

Ahora, separemos la parte exponencial y escribamos

$$ \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(donde }\lim_{\xi\to\infty}h(\xi)=A\text{)} \label{eqn:psi_and_h}\tag{9}$$

> Aunque usamos un método aproximado en el proceso de derivación para encontrar la forma de la solución asintótica para descubrir el término exponencial $e^{-\xi^2/2}$, la ecuación ($\ref{eqn:psi_and_h}$) obtenida a través de esto no es una ecuación aproximada, sino una ecuación exacta. Esta separación de la forma asintótica es el primer paso estándar cuando se resuelve una ecuación diferencial en forma de serie de potencias.
{: .prompt-info }

Diferenciando la ecuación ($\ref{eqn:psi_and_h}$) para obtener $\cfrac{d\psi}{d\xi}$ y $\cfrac{d^2\psi}{d\xi^2}$,

$$ \begin{gather*}
\frac{d\psi}{d\xi} = \left(\frac{dh}{d\xi}-\xi h \right)e^{-\xi^2/2}, \\
\frac{d^2\psi}{d\xi^2} = \left(\frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(\xi^2-1)h \right)e^{-\xi^2/2}
\end{gather*} $$

por lo que la ecuación de Schrödinger ($\ref{eqn:schrodinger_eqn_with_xi}$) se convierte ahora en

$$ \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0 \label{eqn:schrodinger_eqn_with_h}\tag{10}$$

## Expansión en serie de potencias
Según el teorema de Taylor, cualquier función que varíe suavemente se puede expresar como una serie de potencias, así que busquemos la solución de la ecuación ($\ref{eqn:schrodinger_eqn_with_h}$) en forma de serie de $\xi$:

$$ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j \label{eqn:h_series_exp}\tag{11}$$

Diferenciando cada término de esta serie, obtenemos las siguientes dos ecuaciones:

$$ \begin{gather*}
\frac{dh}{d\xi} = a_1 + 2a_2\xi + 3a_3\xi^2 + \cdots = \sum_{j=0}^{\infty}ja_j\xi^{j-1}, \\
\frac{d^2 h}{d\xi^2} = 2a_2 + 2\cdot3a_3\xi + 3\cdot4a_4\xi^2 + \cdots = \sum_{j=0}^{\infty} (j+1)(j+2)a_{j+2}\xi^j.
\end{gather*} $$

Sustituyendo estas dos ecuaciones de vuelta en la ecuación de Schrödinger (ecuación [$\ref{eqn:schrodinger_eqn_with_h}$]), obtenemos:

$$ \sum_{j=0}^{\infty}[(j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j]\xi^j = 0. \label{eqn:schrodinger_eqn_power_series}\tag{12}$$

Por la unicidad de la expansión en serie de potencias, el coeficiente de cada potencia de $\xi$ debe ser cero, por lo que

$$ (j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j = 0 $$

$$ \therefore a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j. \label{eqn:recursion_formula}\tag{13}$$

Esta **fórmula de recurrencia** es equivalente a la ecuación de Schrödinger. Dados dos constantes arbitrarias $a_0$ y $a_1$, se pueden determinar los coeficientes de todos los términos de la solución $h(\xi)$.

Sin embargo, no siempre es posible normalizar la solución obtenida de esta manera. Si la serie $\sum a_j$ es una serie infinita (si $\lim_{j\to\infty} a_j\neq0$), para $j$ muy grandes, la fórmula de recurrencia anterior se aproxima a

$$ a_{j+2} \approx \frac{2}{j}a_j $$

y la solución aproximada a esto es

$$ a_j \approx \frac{C}{(j/2)!} \quad \text{(}C\text{ es una constante arbitraria)}$$

En este caso, para valores grandes de $\xi$ donde los términos de orden superior se vuelven dominantes,

$$ h(\xi) \approx C\sum\frac{1}{(j/2)!}\xi^j \approx C\sum\frac{1}{j!}\xi^{2j} \approx Ce^{\xi^2} $$

y si $h(\xi)$ toma esta forma $Ce^{\xi^2}$, $\psi(\xi)$ en la ecuación ($\ref{eqn:psi_and_h}$) toma la forma $Ce^{\xi^2/2}$, que diverge cuando $\xi \to \infty$. Esto corresponde a la solución no normalizable con $A=0, B\neq0$ en la ecuación ($\ref{eqn:psi_approx}$).

Por lo tanto, la serie $\sum a_j$ debe ser finita. Debe existir un valor 'máximo' de $j$, $n\in \mathbb{N}$, tal que $a_j=0$ para $j>n$, y para que esto suceda, debe ser $a_{n+2}=0$ para $a_n$ no nulo, por lo que de la ecuación ($\ref{eqn:recursion_formula}$)

$$ K = 2n + 1 $$

Sustituyendo esto en la ecuación ($\ref{eqn:K}$), obtenemos las energías físicamente permitidas

$$ E_n = \left(n+\frac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots \label{eqn:E_n}\tag{14}$$

Con esto, hemos obtenido la misma condición de cuantización de energía que en la ecuación (21) de la [solución algebraica del oscilador armónico](/posts/algebraic-solution-of-the-harmonic-oscillator/#estados-estacionarios-psi_n-y-niveles-de-energía-e_n) utilizando un método completamente diferente.

## Polinomios de Hermite (Hermite polynomials) $H_n(\xi)$ y estados estacionarios $\psi_n(x)$
### Polinomios de Hermite $H_n$
En general, $h_n(\xi)$ es un polinomio de grado $n$ en $\xi$, y contiene solo términos pares si $n$ es par, y solo términos impares si $n$ es impar. El resto, excluyendo el coeficiente inicial ($a_0$ o $a_1$), se denomina **polinomio de Hermite (Hermite polynomial)** $H_n(\xi)$.

$$ h_n(\xi) = 
\begin{cases}
a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
\end{cases} $$

Tradicionalmente, los coeficientes se eligen arbitrariamente de modo que el coeficiente del término de mayor grado en $H_n$ sea $2^n$.

A continuación se muestran los primeros polinomios de Hermite:

$$ \begin{align*}
H_0 &= 1 \\
H_1 &= 2\xi \\
H_2 &= 4\xi^2 - 2 \\
H_3 &= 8\xi^3 - 12\xi \\
H_4 &= 16\xi^4 - 48\xi^2 + 12 \\
H_5 &= 32\xi^5 - 160\xi^3 + 120\xi \\
&\qquad\vdots
\end{align*} $$

### Estados estacionarios $\psi_n(x)$
Los estados estacionarios normalizados para el oscilador armónico son:

$$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2}. $$

Esto coincide con el resultado obtenido en la [solución algebraica del oscilador armónico](/posts/algebraic-solution-of-the-harmonic-oscillator/#normalización) (ecuación [27]).

La siguiente imagen muestra los estados estacionarios $\psi_n(x)$ y las densidades de probabilidad $\|\psi_n(x)\|^2$ para los primeros 8 valores de $n$. Se puede observar que las funciones propias del oscilador cuántico alternan entre funciones pares e impares.

![Representaciones de la función de onda para los primeros ocho autoestados ligados, n = 0 a 7. El eje horizontal muestra la posición x.](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Licencia: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)

![Densidades de probabilidad correspondientes.](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Licencia: Dominio Público

El oscilador cuántico es bastante diferente del oscilador clásico correspondiente, no solo en que la energía está cuantizada, sino también en que la distribución de probabilidad de la posición $x$ muestra características peculiares.
- Existe una probabilidad no nula de encontrar la partícula en regiones clásicamente prohibidas (más allá de la amplitud clásica para una $E$ dada)
- Para todos los estados estacionarios con $n$ impar, la probabilidad de encontrar la partícula en el centro es 0

A medida que $n$ aumenta, el oscilador cuántico se asemeja más al oscilador clásico. La siguiente imagen muestra la distribución de probabilidad clásica de la posición $x$ (línea punteada) y el estado cuántico $\|\psi_{30}\|^2$ para $n=30$ (línea sólida). Si se suavizan las partes irregulares, los dos gráficos muestran una forma aproximadamente coincidente.

![Distribuciones de probabilidad cuántica (sólida) y clásica (punteada) del estado excitado n = 30 del oscilador armónico cuántico. Las líneas verticales punteadas representan los puntos de retorno clásicos.](https://upload.wikimedia.org/wikipedia/commons/6/69/QHOn30pdf.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia [AkanoToE](https://commons.wikimedia.org/wiki/User:AkanoToE)
> - Licencia: Dominio Público

### Visualización interactiva de las distribuciones de probabilidad del oscilador cuántico
La siguiente es una visualización reactiva basada en Plotly.js que he creado personalmente. Puedes ajustar el valor de $n$ con el deslizador para ver la forma de la distribución de probabilidad clásica y $\|\psi_n\|^2$ en función de la posición $x$.

{% include quantum-harmonic-oscillator.html %}

> - Visualización original: [Repositorio yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/quantum-harmonic-oscillator.html)
> - Licencia: [Ver aquí](https://github.com/yunseo-kim/physics-visualization?tab=readme-ov-file#license)

Además, si tienes Python instalado en tu computadora y un entorno con las bibliotecas Numpy, Plotly y Dash instaladas, también puedes ejecutar el script Python [`/src/quantum_oscillator.py`{: .filepath}](https://github.com/yunseo-kim/physics-visualization/blob/main/src/quantum_oscillator.py) en el mismo repositorio para ver los resultados.
