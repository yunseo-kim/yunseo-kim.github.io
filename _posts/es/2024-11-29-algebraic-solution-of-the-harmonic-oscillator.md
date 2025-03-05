---
title: Solución algebraica del oscilador armónico (The Harmonic Oscillator)
description: Se establece la ecuación de Schrödinger para el oscilador armónico en
  mecánica cuántica y se examina su solución algebraica. Se obtienen las funciones
  de onda y los niveles de energía de cualquier estado estacionario a partir de los
  conmutadores, las relaciones de conmutación canónicas y los operadores escalera.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Cualquier oscilación puede aproximarse a una oscilación armónica simple si la amplitud es lo suficientemente pequeña, lo que hace que la oscilación armónica simple sea importante en física
> - Oscilador armónico: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Conmutador (commutator)**:
>   - Operación binaria que indica cuán mal conmutan dos operadores
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Relación de conmutación canónica (canonical commutation relation)**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Operadores escalera (ladder operators)**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ se llama **operador de subida (raising operator)**, $\hat{a}\_-$ se llama **operador de bajada (lowering operator)**
>   - Pueden subir o bajar los niveles de energía para cualquier estado estacionario, por lo que si se encuentra una solución de la ecuación de Schrödinger independiente del tiempo, se pueden encontrar todas las demás soluciones
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Función de onda y nivel de energía del $n$-ésimo estado estacionario:
>   - Estado fundamental ($0$-ésimo estado estacionario):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$-ésimo estado estacionario:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ es el **conjugado hermítico (hermitian conjugate)** y el **operador adjunto (adjoint operator)** de $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - De esto se pueden derivar las siguientes propiedades:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Método para calcular el valor esperado de cantidades físicas que incluyen potencias de $\hat{x}$ y $\hat{p}$:
>   1. Expresar $\hat{x}$ y $\hat{p}$ en términos de operadores de subida y bajada usando la definición de los operadores escalera
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. Expresar la cantidad física cuyo valor esperado se quiere calcular usando las expresiones de $\hat{x}$ y $\hat{p}$ anteriores
>   3. Utilizar el hecho de que $\left(\hat{a}\_\pm \right)^m$ es proporcional a $\psi\_{n\pm m}$ y por lo tanto ortogonal a $\psi\_n$, resultando en $0$
>   4. Calcular la integral usando las propiedades de los operadores escalera
{: .prompt-info }

## Prerequisites
- [Método de separación de variables](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Teorema de Ehrenfest](/posts/ehrenfest-theorem/)
- [Ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/)
- [Pozo cuadrado infinito unidimensional](/posts/the-infinite-square-well/)
- Conjugado hermítico (hermitian conjugate), operador adjunto (adjoint operator)

## Configuración del modelo
### Oscilador armónico en mecánica clásica
Un ejemplo típico de oscilador armónico clásico es el movimiento de una masa $m$ colgada de un resorte con constante $k$ (ignorando la fricción).
Este movimiento sigue la **ley de Hooke**:

$$ F = -kx = m\frac{d^2x}{dt^2} $$

La solución de esta ecuación es:

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

donde

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

es la frecuencia angular de la oscilación. La energía potencial en función de la posición $x$ tiene la forma parabólica:

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

En la realidad, no existen osciladores armónicos perfectos. Incluso en el caso del resorte que usamos como ejemplo, si se estira demasiado, excederá su límite elástico y se romperá o sufrirá una deformación permanente, y de hecho, incluso antes de llegar a ese punto, ya no seguirá exactamente la ley de Hooke. Sin embargo, la razón por la que el oscilador armónico es importante en física es que cualquier potencial arbitrario puede aproximarse a una forma parabólica cerca de su mínimo local. Si expandimos un potencial arbitrario $V(x)$ en serie de Taylor cerca de un mínimo:

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Ahora, como sumar una constante arbitraria a $V(x)$ no afecta en absoluto a la fuerza, podemos restar $V(x_0)$ aquí, y como $x_0$ es un mínimo, $V^\prime(x_0)=0$, y asumiendo que $(x-x_0)$ es lo suficientemente pequeño para ignorar los términos de orden superior, obtenemos:

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

Esto coincide con el movimiento de un oscilador armónico con una constante de resorte efectiva $k=V^{\prime\prime}(x_0)$ cerca del punto $x_0$\*. Es decir, cualquier oscilación puede aproximarse a una oscilación armónica simple si la amplitud es lo suficientemente pequeña.

> \* Como asumimos que $V(x)$ tiene un mínimo en $x_0$, aquí $V^{\prime\prime}(x_0) \geq 0$. En casos muy raros, puede ocurrir que $V^{\prime\prime}(x_0)=0$, y tal movimiento no puede aproximarse a una oscilación armónica simple.
{: .prompt-info }

### Oscilador armónico en mecánica cuántica
El problema del oscilador armónico cuántico consiste en resolver la ecuación de Schrödinger para el potencial:

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

La [ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/) para el oscilador armónico es:

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

Hay dos enfoques completamente diferentes para resolver este problema. Uno es el método analítico utilizando **series de potencias (power series method)**, y el otro es el método algebraico utilizando **operadores escalera (ladder operators)**. El método algebraico es más rápido y simple, pero también es necesario estudiar la solución analítica utilizando series de potencias. Aquí trataremos el método de solución algebraica, y para el método de solución analítica, consulta [este artículo](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Conmutadores y relación de conmutación canónica
La ecuación ($\ref{eqn:t_independent_schrodinger_eqn}$) se puede escribir utilizando el operador de momento $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$ de la siguiente manera:

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Ahora factorizemos el hamiltoniano (Hamiltonian):

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

Si $p$ y $x$ fueran números, podríamos factorizar simplemente como:

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

pero aquí $\hat{p}$ y $\hat{x}$ son operadores y generalmente no cumplen la **propiedad conmutativa (commutative property)** para operadores ($\hat{p}\hat{x}\neq \hat{x}\hat{p}$), así que no es tan simple. Sin embargo, puede servir como punto de partida, así que comencemos examinando la siguiente cantidad:

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

Para los operadores $\hat{a_\pm}$ definidos arriba, $\hat{a}\_-\hat{a}\_+$ es:

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Aquí, el término $(\hat{x}\hat{p}-\hat{p}\hat{x})$ se llama **conmutador (commutator)** de $\hat{x}$ y $\hat{p}$, e indica cuán mal conmutan los dos operadores. En general, el conmutador de los operadores $\hat{A}$ y $\hat{B}$ se denota usando corchetes de la siguiente manera:

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

Usando esta notación, la ecuación ($\ref{eqn:a_m_times_a_p_without_commutator}$) se puede reescribir como:

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Ahora necesitamos encontrar el conmutador de $\hat{x}$ y $\hat{p}$.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

y eliminando la función de prueba $f(x)$, obtenemos:

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

Esto se llama **relación de conmutación canónica (canonical commutation relation)**.

## Operadores escalera (ladder operators)
Debido a la relación de conmutación canónica, la ecuación ($\ref{eqn:a_m_times_a_p}$) se convierte en:

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

es decir,

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Aquí, el orden de $\hat{a}\_-$ y $\hat{a}\_+$ es importante; si ponemos $\hat{a}\_+$ a la izquierda, obtenemos:

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

y satisface:

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

En este caso, el hamiltoniano también se puede escribir como:

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Por lo tanto, si expresamos la ecuación de Schrödinger independiente del tiempo ($\hat{H}\psi=E\psi$) en términos de $\hat{a}_\pm$, obtenemos:

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(el signo superior e inferior van juntos).

Ahora podemos descubrir la siguiente propiedad importante:

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Demostración:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> De manera similar,
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Por lo tanto, si podemos encontrar una solución de la ecuación de Schrödinger independiente del tiempo, podemos encontrar todas las demás soluciones. Como podemos subir o bajar los niveles de energía para cualquier estado estacionario, $\hat{a}\_\pm$ se llaman **operadores escalera (ladder operators)**, donde $\hat{a}\_+$ es el **operador de subida (raising operator)** y $\hat{a}\_-$ es el **operador de bajada (lowering operator)**.

## Estados estacionarios del oscilador armónico
### Estados estacionarios $\psi_n$ y niveles de energía $E_n$
Si seguimos aplicando el operador de bajada, eventualmente obtendremos un estado de energía menor que 0, que no puede existir físicamente. Matemáticamente, si $\psi$ es una solución de la ecuación de Schrödinger, $\hat{a}_-\psi$ también es una solución de la ecuación de Schrödinger, pero no hay garantía de que esta nueva solución esté siempre normalizada (es decir, que sea un estado físicamente posible). Si seguimos aplicando el operador de bajada, eventualmente obtendremos la solución trivial $\psi=0$.

Por lo tanto, para los estados estacionarios $\psi$ del oscilador armónico, existe un "nivel más bajo" $\psi_0$ que satisface:

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

(no existe un nivel de energía más bajo). Este $\psi_0$ satisface:

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

por lo tanto,

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

Esta es una [ecuación diferencial ordinaria separable](/posts/Separation-of-Variables/), por lo que se puede resolver fácilmente de la siguiente manera:

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

Además, esta función se puede normalizar de la siguiente manera:

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Aquí, $A^2 = \sqrt{m\omega / \pi\hbar}$, por lo que:

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Ahora, si sustituimos esta solución en la ecuación de Schrödinger ($\ref{eqn:schrodinger_eqn_with_ladder}$) que obtuvimos anteriormente y usamos el hecho de que $\hat{a}_-\psi_0=0$, obtenemos:

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

Comenzando desde este **estado fundamental (ground state)** y aplicando repetidamente el operador de subida, podemos obtener estados excitados (excited states) donde la energía aumenta en $\hbar\omega$ cada vez que se aplica el operador de subida.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

Aquí, $A_n$ es la constante de normalización. De esta manera, después de encontrar el estado fundamental, podemos determinar todos los estados estacionarios y los niveles de energía permitidos del oscilador armónico aplicando el operador de subida.

### Normalización
La constante de normalización también se puede obtener algebraicamente. Sabemos que $\hat{a}\_{\pm}\psi\_n$ es proporcional a $\psi\_{n\pm 1}$, por lo que podemos escribir:

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Ahora, observemos que para cualquier función $f(x)$ y $g(x)$ integrable se cumple lo siguiente:

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ es el **conjugado hermítico (hermitian conjugate)** y el **operador adjunto (adjoint operator)** de $\hat{a}\_\pm$.

> **Demostración:**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

Por lo tanto, si tomamos $f=\hat{a}_\pm \psi_n$, $g=\psi_n$, obtenemos:

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Entonces, de las ecuaciones ($\ref{eqn:schrodinger_eqn_with_ladder}$) y ($\ref{eqn:psi_n_and_E_n}$):

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

De las ecuaciones ($\ref{eqn:norm_const}$) y ($\ref{eqn:norm_const_2}$), obtenemos:

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

Y como $\psi_n$ y $\psi_{n\pm1}$ están todos normalizados, $\|c_n\|^2=n+1,\ \|d_n\|^2=n$, por lo tanto:

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

A partir de esto, podemos obtener cualquier estado estacionario normalizado $\psi_n$ de la siguiente manera:

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

Es decir, en la ecuación ($\ref{eqn:psi_n_and_E_n}$), la constante de normalización es $A_n=\cfrac{1}{\sqrt{n!}}$.

### Ortogonalidad de los estados estacionarios
Al igual que en el [pozo cuadrado infinito unidimensional](/posts/the-infinite-square-well/#3-estos-estados-poseen-ortogonalidad), los estados estacionarios del oscilador armónico son ortogonales.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Demostración
Se puede demostrar utilizando las ecuaciones ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$) y ($\ref{eqn:norm_const_3}$) que mostramos anteriormente. En la ecuación ($\ref{eqn:hermitian_conjugate}$), tomamos $f=\hat{a}_-\psi_m,\ g=\psi_n$, y utilizamos el hecho de que

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

Utilizando la ortogonalidad, al igual que [hicimos en la ecuación (19) del pozo cuadrado infinito unidimensional](/posts/the-infinite-square-well/#encontrar-la-soluci%C3%B3n-general-psixt-de-la-ecuaci%C3%B3n-de-schr%C3%B6dinger-dependiente-del-tiempo), cuando expandimos $\Psi(x,0)$ como una combinación lineal de estados estacionarios $\sum c_n\psi_n(x)$, podemos obtener los coeficientes $c_n$ utilizando el [método de Fourier](/posts/the-infinite-square-well/#c%C3%A1lculo-de-los-coeficientes-c_n-usando-el-truco-de-fourier).

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Aquí también, $\|c_n\|^2$ es la probabilidad de obtener el valor $E_n$ al medir la energía.

## Valor esperado de la energía potencial $\langle V \rangle$ en cualquier estado estacionario $\psi_n$
Para obtener $\langle V \rangle$, necesitamos calcular la siguiente integral:

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

Al calcular integrales de esta forma que incluyen potencias de $\hat{x}$ y $\hat{p}$, el siguiente método es útil.

Primero, usando la definición de los operadores de escalera en la ecuación ($\ref{eqn:ladder_operators}$), expresamos $\hat{x}$ y $\hat{p}$ en términos de los operadores de subida y bajada.

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Ahora expresamos la cantidad física cuyo valor esperado queremos calcular utilizando las expresiones anteriores de $\hat{x}$ y $\hat{p}$. Aquí estamos interesados en $x^2$, por lo que podemos expresarlo como:

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

De esto obtenemos:

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

Y aquí, como $\left(\hat{a}\_\pm \right)^2$ es proporcional a $\psi\_{n\pm2}$, es ortogonal a $\psi\_n$, por lo que los términos $\left(\hat{a}\_+ \right)^2$ y $\left(\hat{a}\_- \right)^2$ se anulan. Finalmente, utilizando la ecuación ($\ref{eqn:norm_const_2}$) para calcular los dos términos restantes, obtenemos:

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

Refiriéndonos a la ecuación ($\ref{eqn:psi_n_and_E_n}$), podemos ver que el valor esperado de la energía potencial es exactamente la mitad de la energía total, y la otra mitad es, por supuesto, la energía cinética $T$. Esta es una característica única del oscilador armónico.
