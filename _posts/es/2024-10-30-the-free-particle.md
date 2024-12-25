---
title: La partícula libre
description: Exploramos el hecho de que la solución separable para una partícula libre
  con V(x)=0 no se puede normalizar y lo que esto significa, demostramos cualitativamente
  la relación de incertidumbre posición-momento para la solución general, y calculamos
  e interpretamos físicamente la velocidad de fase y de grupo de Ψ(x,t).
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Partícula libre: $V(x)=0$, sin condiciones de contorno (energía arbitraria)
> - La solución separable $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ diverge al infinito cuando se integra el cuadrado, por lo que no se puede normalizar, lo que implica:
>   - Una partícula libre no puede existir en un estado estacionario
>   - Una partícula libre no puede tener un valor de energía definido con precisión (existe incertidumbre en la energía)
> - Sin embargo, la solución general de la ecuación de Schrödinger dependiente del tiempo sigue siendo una combinación lineal de soluciones separables, por lo que estas siguen teniendo importancia matemática. En este caso, al no haber condiciones restrictivas, la solución general toma la forma de una integral ($\int$) sobre la variable continua $k$, en lugar de una suma ($\sum$) sobre una variable discreta $n$.
> - Solución general de la ecuación de Schrödinger:
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{donde }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - Relación entre la incertidumbre en posición y en momento:
>   - Si la incertidumbre en posición disminuye, la incertidumbre en momento aumenta, y viceversa
>   - Es decir, cuánticamente es imposible conocer simultáneamente con precisión la posición y el momento de una partícula libre
> - Velocidad de fase y de grupo de la función de onda $\Psi(x,t)$:
>   - Velocidad de fase: $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - Velocidad de grupo: $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - Significado físico de la velocidad de grupo y comparación con la mecánica clásica:
>   - Físicamente, la velocidad de grupo representa la velocidad de movimiento de la partícula
>   - Asumiendo que $\phi(k)$ tiene una forma muy aguda alrededor de algún valor $k_0$ (cuando la incertidumbre en el momento es suficientemente pequeña), 
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Prerrequisitos
- Fórmula de Euler
- Transformada de Fourier & Teorema de Plancherel
- [Ecuación de Schrödinger y función de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/)
- [Pozo cuadrado infinito unidimensional](/posts/the-infinite-square-well/)

## Configuración del modelo
Consideremos el caso más simple de una partícula libre ($V(x)=0$). Clásicamente, esto es simplemente un movimiento a velocidad constante, pero en mecánica cuántica este problema es más interesante.  
La [ecuación de Schrödinger independiente del tiempo](/posts/time-independent-schrodinger-equation/) para una partícula libre es

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

es decir

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, donde }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[Hasta aquí es igual que el interior del pozo cuadrado infinito con potencial $0$](/posts/the-infinite-square-well/#configuración-del-modelo-y-condiciones-de-contorno). Sin embargo, esta vez escribamos la solución general en forma de función exponencial:

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ y $C\cos{kx}+D\sin{kx}$ son formas equivalentes de escribir la misma función de $x$. Por la fórmula de Euler $e^{ix}=\cos{x}+i\sin{x}$,
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> Es decir, si tomamos $C=A+B$, $D=i(A-B)$, entonces 
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> A la inversa, expresando $A$ y $B$ en términos de $C$ y $D$, tenemos $A=\cfrac{C-iD}{2}$, $B=\cfrac{C+iD}{2}$.
>
> En mecánica cuántica, cuando $V=0$, la función exponencial representa una onda en movimiento y es la más conveniente para tratar partículas libres. Por otro lado, las funciones seno y coseno son útiles para representar ondas estacionarias y aparecen naturalmente en el caso del pozo cuadrado infinito.
{: .prompt-info }

A diferencia del pozo cuadrado infinito, esta vez no hay condiciones de contorno que restrinjan $k$ y $E$. Es decir, una partícula libre puede tener cualquier energía positiva.

## Solución separable y velocidad de fase
Si añadimos la dependencia temporal $e^{-iEt/\hbar}$ a $\psi(x)$, obtenemos

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

Cualquier función de $x$ y $t$ que dependa de una forma especial $(x\pm vt)$ representa una onda que se mueve en la dirección $\mp x$ con velocidad $v$ sin cambiar de forma. Por lo tanto, el primer término de la ecuación ($\ref{eqn:Psi_seperated_solution}$) representa una onda que se mueve hacia la derecha, y el segundo término representa una onda con la misma longitud de onda y velocidad de propagación, pero con amplitud diferente, moviéndose hacia la izquierda. Como solo difieren en el signo delante de $k$, podemos escribir

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

donde la dirección de propagación de la onda según el signo de $k$ es:

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{se mueve hacia la derecha}, \\
k<0 \Rightarrow & \text{se mueve hacia la izquierda}.
\end{cases} \tag{6}$$

El 'estado estacionario' de una partícula libre es claramente una onda en movimiento*, con longitud de onda $\lambda = 2\pi/\|k\|$ y, según la fórmula de de Broglie,

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

de momento.

> *Que un 'estado estacionario' sea una onda en movimiento es, por supuesto, físicamente contradictorio. La razón se verá pronto.
{: .prompt-info }

Además, la velocidad de esta onda es:

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(Aquí, $\omega$ es el coeficiente delante de $t$, $\cfrac{\hbar k^2}{2m}$.)

Sin embargo, esta función de onda no se puede normalizar porque diverge al infinito cuando se integra su cuadrado.

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

Es decir, <u>en el caso de una partícula libre, la solución separable no es un estado físicamente posible.</u> Una partícula libre no puede existir en un [estado estacionario](/posts/time-independent-schrodinger-equation/#1-son-estados-estacionarios), ni puede tener [un valor de energía específico](/posts/time-independent-schrodinger-equation/#2-es-un-estado-con-un-valor-de-energía-total-e-bien-definido-no-una-distribución-de-probabilidad-con-un-rango). De hecho, intuitivamente, sería más extraño que se formara una onda estacionaria sin condiciones de contorno en absoluto en los extremos.

## Obtención de la solución general $\Psi(x,t)$ de la ecuación de Schrödinger dependiente del tiempo
A pesar de esto, esta solución separable sigue teniendo un significado importante, porque independientemente de la interpretación física, [la solución general de la ecuación de Schrödinger dependiente del tiempo es una combinación lineal de soluciones separables](/posts/time-independent-schrodinger-equation/#3-la-solución-general-de-la-ecuación-de-schrödinger-dependiente-del-tiempo-es-una-combinación-lineal-de-soluciones-separadas), lo que le da un significado matemático. Sin embargo, en este caso, como no hay condiciones restrictivas, la solución general toma la forma de una integral ($\int$) sobre la variable continua $k$, en lugar de una suma ($\sum$) sobre una variable discreta $n$.

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> Aquí, $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ juega el mismo papel que $c_n$ en [la ecuación (21) del post 'Ecuación de Schrödinger independiente del tiempo'](/posts/time-independent-schrodinger-equation/#3-la-solución-general-de-la-ecuación-de-schrödinger-dependiente-del-tiempo-es-una-combinación-lineal-de-soluciones-separadas).
{: .prompt-info }

Esta función de onda se puede normalizar para un $\phi(k)$ apropiado, pero debe tener un rango de $k$ y, por lo tanto, un rango de energías y velocidades. Esto se llama un **paquete de ondas (wave packet)**.

> Una función seno está espacialmente extendida infinitamente y no se puede normalizar. Sin embargo, si superponemos varias de estas ondas, se localizan por interferencia y se pueden normalizar.
{: .prompt-info }

## Obtención de $\phi(k)$ utilizando el teorema de Plancherel

Ahora que conocemos la forma de $\Psi(x,t)$ (ecuación [$\ref{eqn:Psi_general_solution}$]), solo necesitamos determinar $\phi(k)$ que satisfaga la función de onda inicial

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

Este es un problema típico de análisis de Fourier, y podemos obtener la respuesta mediante el **teorema de Plancherel**.

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$ se llama la **transformada de Fourier** de $f(x)$, y $f(x)$ es la **transformada inversa de Fourier** de $F(k)$. Como se puede ver fácilmente en la ecuación ($\ref{eqn:plancherel_theorem}$), la única diferencia entre ambas es el signo en el exponente. Por supuesto, existe la condición restrictiva de que solo se permiten funciones para las que existe la integral.

> La condición necesaria y suficiente para que $f(x)$ exista es que $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ sea finita. En este caso, $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ también es finita, y 
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> Algunas personas se refieren a esta ecuación como el teorema de Plancherel, en lugar de la ecuación ($\ref{eqn:plancherel_theorem}$) (esto es lo que se describe en [Wikipedia](https://en.wikipedia.org/wiki/Plancherel_theorem)).
{: .prompt-info }

En este caso, la integral siempre existe debido a la condición física de que $\Psi(x,0)$ debe estar normalizada. Por lo tanto, la solución cuántica para una partícula libre es la ecuación ($\ref{eqn:Psi_general_solution}$), donde

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> Sin embargo, en la práctica, casi nunca es posible resolver analíticamente la integral en la ecuación ($\ref{eqn:Psi_general_solution}$). Normalmente, se utilizan métodos de análisis numérico por computadora para obtener los valores.
{: .prompt-tip }

## Cálculo de la velocidad de grupo del paquete de ondas e interpretación física

Esencialmente, un paquete de ondas es una superposición de numerosas funciones seno cuyas amplitudes están determinadas por $\phi$. Es decir, hay 'ondulaciones (ripples)' dentro de una 'envolvente (envelope)' que forma el paquete de ondas.

![A wave packet with the group velocity larger(5x) than phase velocity](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/wave_packet.gif)
> *Aviso de licencia y fuente original de la imagen*
> - Código fuente para la generación de la imagen (gnuplot): [yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/wave_packet.plt)
> - Licencia: [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualization/blob/main/LICENSE)
> - Autor original: [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - Aviso de licencia original: [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

Físicamente, lo que corresponde a la velocidad de la partícula no es la velocidad de las ondulaciones individuales (**velocidad de fase, phase velocity**) calculada anteriormente en la ecuación ($\ref{eqn:phase_velocity}$), sino la velocidad de la envolvente exterior (**velocidad de grupo, group velocity**).

### Relación entre la incertidumbre en posición y en momento
Examinemos la relación entre la incertidumbre en posición y en momento considerando solo la parte del integrando $\int\phi(k)e^{ikx}dk$ de la ecuación ($\ref{eqn:Psi_at_t_0}$) y la parte del integrando $\int\Psi(x,0)e^{-ikx}dx$ de la ecuación ($\ref{eqn:phi}$).

#### Cuando la incertidumbre en posición es pequeña
Cuando $\Psi$ en el espacio de posición tiene una distribución muy estrecha alrededor de algún valor $x_0$ en el intervalo $[x_0-\delta, x_0+\delta]$ y es cercana a cero fuera de esta región (<u>cuando la incertidumbre en posición es pequeña</u>), $e^{-ikx} \approx e^{-ikx_0}$ es casi constante respecto a $x$, por lo que

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{ec. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

El término de la integral definida es constante respecto a $p$, por lo que debido al término $e^{-ipx_0/\hbar}$ anterior, $\phi$ tendrá una forma de onda sinusoidal respecto a $p$ en el espacio de momento, es decir, se distribuirá en un amplio rango de momentos (<u>la incertidumbre en el momento es grande</u>).

#### Cuando la incertidumbre en momento es pequeña
De manera similar, cuando $\phi$ en el espacio de momento tiene una distribución muy estrecha alrededor de algún valor $p_0$ en el intervalo $[p_0-\delta, p_0+\delta]$ y es cercana a cero fuera de esta región (<u>cuando la incertidumbre en momento es pequeña</u>), por la ecuación ($\ref{eqn:de_broglie_formula}$), $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ es casi constante respecto a $p$ y $dk=\frac{1}{\hbar}dp$, por lo que

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

Debido al término $e^{ip_0x/\hbar}$ anterior, $\Psi$ tendrá una forma de onda sinusoidal respecto a $x$ en el espacio de posición, es decir, se distribuirá en un amplio rango de posiciones (<u>la incertidumbre en la posición es grande</u>).

#### Conclusión
Si la incertidumbre en posición disminuye, la incertidumbre en momento aumenta, y viceversa. Por lo tanto, cuánticamente es imposible conocer simultáneamente con precisión la posición y el momento de una partícula libre.

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *Fuente de la imagen*
> - Autor: Usuario de Wikipedia en inglés [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - Licencia: dominio público

> De hecho, debido al principio de incertidumbre (uncertainty principle), esto se aplica no solo a las partículas libres, sino a todos los casos. El principio de incertidumbre se tratará en un post separado en el futuro.
{: .prompt-info }

### Velocidad de grupo del paquete de ondas
Si reescribimos la solución general de la ecuación ($\ref{eqn:Psi_general_solution}$) como en la ecuación ($\ref{eqn:phase_velocity}$) con $\omega \equiv \cfrac{\hbar k^2}{2m}$, obtenemos

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> Una ecuación que expresa $\omega$ como función de $k$, como $\omega = \cfrac{\hbar k^2}{2m}$, se llama **relación de dispersión (dispersion relation)**. El contenido que sigue se aplica generalmente a todos los paquetes de ondas, independientemente de la relación de dispersión.
{: .prompt-info }

Ahora supongamos que $\phi(k)$ tiene una forma muy aguda alrededor de algún valor apropiado $k_0$. (Está bien si se extiende ampliamente en $k$, pero tal forma de paquete de ondas se distorsiona muy rápidamente y cambia a una forma diferente. Esto se debe a que los componentes para diferentes $k$ se mueven a diferentes velocidades, perdiendo el significado de un 'grupo' total bien definido con una velocidad. Es decir, <u>la incertidumbre en el momento aumenta.</u>)  
La función que se integra es despreciable excepto cerca de $k_0$, por lo que podemos expandir la función $\omega(k)$ en serie de Taylor alrededor de este punto, y si escribimos solo hasta el término de primer orden, obtenemos

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

Ahora, sustituyendo $s=k-k_0$ e integrando alrededor de $k_0$,

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

El término anterior $e^{i(k_0x-\omega_0t)}$ representa una onda sinusoidal ('ondulaciones') que se mueve a una velocidad $\omega_0/k_0$, y el término integral que determina la amplitud de esta onda sinusoidal ('envolvente') se mueve a una velocidad $\omega_0^\prime$ debido a la parte $e^{is(x-\omega_0^\prime t)}$. Por lo tanto, la velocidad de fase en $k=k_0$ es

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

que es el mismo valor que en la ecuación ($\ref{eqn:phase_velocity}$), y la velocidad de grupo es

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

que es el doble de la velocidad de fase.

## Comparación con la mecánica clásica

Sabiendo que la mecánica clásica se cumple a escala macroscópica, los resultados obtenidos a través de la mecánica cuántica deberían aproximarse a los resultados calculados en la mecánica clásica cuando la incertidumbre cuántica es suficientemente pequeña. En el caso de la partícula libre que estamos tratando ahora, cuando $\phi(k)$ tiene una forma muy aguda alrededor de un valor apropiado $k_0$ (es decir, <u>cuando la incertidumbre en el momento es suficientemente pequeña</u>), la velocidad de grupo $v_\text{group}$, que corresponde a la velocidad de la partícula en mecánica cuántica, debería ser igual a la velocidad de la partícula $v_\text{classical}$ calculada en mecánica clásica para el mismo valor de $k$ y la energía $E$ correspondiente.

Si sustituimos $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ de la ecuación ($\ref{eqn:t_independent_schrodinger_eqn}$) en la velocidad de grupo que acabamos de calcular (ecuación [$\ref{eqn:group_velocity}$]), obtenemos

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

y la velocidad de una partícula libre con energía cinética $E$ en mecánica clásica es igualmente

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

Por lo tanto, como $v_\text{quantum}=v_\text{classical}$, podemos confirmar que el resultado obtenido aplicando la mecánica cuántica es una solución físicamente válida.
