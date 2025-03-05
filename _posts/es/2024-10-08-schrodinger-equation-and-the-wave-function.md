---
title: La ecuación de Schrödinger y la función de onda
description: Examinamos la forma básica de la ecuación de Schrödinger, que tiene una
  posición similar a las leyes del movimiento de Newton en la mecánica clásica dentro
  de la mecánica cuántica. También exploramos la interpretación estadística del significado
  físico de la función de onda obtenida como solución de la ecuación de Schrödinger,
  las perspectivas sobre la indeterminación cuántica y el significado físico del acto
  de medición en la interpretación de Copenhague (colapso de la función de onda).
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
mermaid: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Ecuación de Schrödinger (dependiente del tiempo): 
>
> $$ i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi $$
>
> - Interpretación estadística de la función de onda $\Psi(x,t)$ (interpretación de Born): El cuadrado del valor absoluto de la función de onda $\|\Psi(x,t)\|^2$ es la **función de densidad de probabilidad** de encontrar la partícula en la posición $x$ en el tiempo $t$.
> - Normalización de la función de onda:
>   - $\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx = 1$
>   - Si $\Psi(x,t)$ es una solución de la ecuación de Schrödinger, entonces $A\Psi(x,t)$ también es una solución para cualquier constante compleja $A$, y determinar la constante $A$ para satisfacer la ecuación anterior se llama normalización
>   - Las **soluciones no normalizables** no pueden representar partículas y no son funciones de onda válidas, solo las soluciones **de cuadrado integrable** son físicamente posibles
>   - Una función de onda normalizada en un punto en el tiempo permanece normalizada a medida que pasa el tiempo, incluso cuando $\Psi$ cambia
> - Corriente de probabilidad:
>   - $J(x,t) \equiv \cfrac{i\hbar}{2m}\left(\Psi\cfrac{\partial \Psi^\*}{\partial x}-\Psi^\*\cfrac{\partial \Psi}{\partial x}\right)$
>   - El flujo de probabilidad (probabilidad por unidad de tiempo) que pasa por el punto $x$
>   - Si $P_{ab}(t)$ es la probabilidad de encontrar la partícula en la región $a<x<b$ en el tiempo $t$, entonces $\cfrac{dP_{ab}}{dt} = J(a,t) - J(b,t)$
{: .prompt-info }

## Prerrequisitos
- Distribución de probabilidad continua y densidad de probabilidad

## Ecuación de Schrödinger (Schrödinger equation)
Consideremos una partícula de masa $m$ moviéndose a lo largo del eje $x$ bajo una fuerza dada $F(x,t)$.

En la mecánica clásica, el objetivo principal es aplicar la ecuación de movimiento de Newton $F=ma$ para determinar la posición $x(t)$ de la partícula en cualquier momento. Este proceso se puede representar aproximadamente con el siguiente diagrama:

```mermaid
flowchart TD
	conditions["Condiciones dadas"] -- F=ma --> x["Posición x(t)"]
	x --> quantities["Cantidades físicas"]
```

En la mecánica cuántica, se aborda el mismo problema de una manera muy diferente. El enfoque de la mecánica cuántica es resolver la siguiente **ecuación de Schrödinger** para obtener la **función de onda** $\Psi(x,t)$ de la partícula:

$$ \begin{gather*}
i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}\\
\text{(} i=\sqrt{-1}\text{, } \hbar=\frac{h}{2\pi}=1.054573\times10^{-34}\text{, } h\text{: constante de Planck, } V(x)\text{: energía potencial)}
\end{gather*} $$

![Gráfico complejo de una función de onda que satisface la ecuación de Schrödinger no relativista con V = 0 (partícula libre)](https://upload.wikimedia.org/wikipedia/commons/b/b7/Wavepacket-a2k4-en.gif?20210105144724)
> *Fuente de la imagen*
> - Autor: Usuario de Wikimedia Xcodexif
> - Licencia: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

```mermaid
flowchart TD
	conditions["Condiciones dadas Ψ(x,0)"] -- "Ecuación de Schrödinger" --> x["Función de onda Ψ(x,t)"]
	x --> quantities["PD de las cantidades físicas"]
```

## Interpretación estadística de la función de onda $\Psi(x,t)$ (Interpretación de Born)
Mientras que en la mecánica clásica una partícula se localiza en un punto, en la mecánica cuántica la función de onda que representa el estado de la partícula es una función de $x$ para un $t$ dado, es decir, está extendida en el espacio. ¿Cómo debemos interpretar el significado físico de esto?

Según la **interpretación estadística** de Born, el cuadrado del valor absoluto de la función de onda $\|\Psi(x,t)\|^2$ es la función de densidad de probabilidad de encontrar la partícula en la posición $x$ en el tiempo $t$. Aunque la función de onda $\Psi$ en sí es un número complejo, $\|\Psi\|^2=\Psi^\*\Psi$ ($\Psi^\*$ es el conjugado complejo de $\Psi$) es un número real no negativo, lo que permite esta interpretación. Es decir, se puede expresar de la siguiente manera:

$$ \int_a^b |\Psi(x,t)|^2 dx = \text{Probabilidad de encontrar la partícula entre }a\text{ y }b\text{ en el tiempo }t. \tag{2}$$

Esta interpretación estadística implica que la mecánica cuántica conlleva una cierta **indeterminación**. Incluso si se conoce todo sobre la partícula (la función de onda), solo se puede conocer la distribución de probabilidad de los posibles resultados, no se puede determinar un valor específico.

Esto era difícil de aceptar intuitivamente, por lo que naturalmente surgieron preguntas sobre si esta indeterminación se debía a algún defecto de la mecánica cuántica o si era una característica esencial de la naturaleza.

## Perspectivas sobre la indeterminación cuántica (quantum indeterminacy)
Supongamos que medimos la posición de una partícula y descubrimos que está en el punto $C$. Entonces, ¿dónde estaba la partícula justo antes de la medición?

### Posición realista (realist)

> "Dios no juega a los dados." ("God does not play dice.")  
> *por Albert Einstein*

La partícula estaba originalmente en $C$. Esta es también la perspectiva de Einstein y Schrödinger. Sin embargo, desde este punto de vista, dado que la partícula estaba realmente exactamente en $C$, pero debido a las limitaciones de la teoría solo podemos conocer la distribución de probabilidad de la posición de la partícula hasta el momento de la medición, la mecánica cuántica es una teoría incompleta. Es decir, según este punto de vista, la indeterminación no es una característica esencial de la naturaleza, sino el resultado de las limitaciones de la mecánica cuántica, y debe haber algunas variables ocultas adicionales además de $\Psi$ que deben conocerse para describir completamente la partícula.

> Schrödinger fue alumno de Einstein y trabajó como su asistente durante un tiempo, y luego continuó intercambiando ideas con Einstein. Es probable que su posición realista y determinista también fuera influenciada por esto.
{: .prompt-info }

### Posición ortodoxa (orthodox)

> "Deja de decirle a Dios qué hacer con sus dados." ("Stop telling God what to do with his dice.")  
> *por Niels Bohr, en respuesta a la cita anterior de Einstein*
>
> "Las observaciones no solo perturban lo que se va a medir, sino que lo producen" ("Observations not only disturb what is to be measured, they produce it")  
> ...  
> "Nosotros obligamos a asumir una posición definida." ("We compel to assume a definite position.")  
> *por Pascual Jordan*

Hasta justo antes de la medición, la partícula solo existe en forma de distribución de probabilidad y no está en ningún lugar específico, y solo cuando se realiza el acto de medición la partícula aparece en una posición específica. Esta interpretación se llama **interpretación de Copenhague**, y fue propuesta por Bohr y Heisenberg en la Universidad de Copenhague.

> Lo interesante es que, de manera similar a la relación entre Einstein y Schrödinger, Heisenberg también fue alumno de Bohr.
{: .prompt-info }

### Posición agnóstica (agnostic)

> "No hay necesidad de romperse la cabeza sobre el problema de si algo de lo que no se puede saber nada existe de todos modos, al igual que sobre la antigua pregunta de cuántos ángeles pueden sentarse en la punta de una aguja." ("One should no more rack one's brain about the problem of whether something one cannot know anything about exists all the same, than about the ancient question of how many angels are able to sit on the point of a needle.")  
> *por Wolfgang Pauli*

Se niega a responder. Cualquier afirmación que se haga sobre el estado de la partícula antes de la medición, si la única forma de verificar si esa afirmación es correcta es mediante la medición, entonces ya no es "antes de la medición", ¿qué sentido tiene? Es simplemente metafísica discutir sobre algo que es fundamentalmente imposible de probar y conocer.

### Consenso actual
En 1964, John Bell demostró que hay una diferencia observable dependiendo de si la partícula existe en una posición exacta o no, ya sea antes o después de la medición, lo que excluyó la posición agnóstica, y posteriormente, a través de experimentos, la interpretación de Copenhague se convirtió en la corriente principal. Por lo tanto, a menos que se indique lo contrario, generalmente se asume esta interpretación de Copenhague cuando se trata de mecánica cuántica.

> Todavía existen otras interpretaciones que podrían ser correctas además de la interpretación de Copenhague, como las teorías de variables ocultas no locales (nonlocal hidden variable theories) o la interpretación de muchos mundos (many worlds interpretation).
{: .prompt-info }

## Medición y colapso de la función de onda
La partícula no tiene una posición exacta hasta justo antes de la medición, y solo a través de la medición adquiere una posición específica $C$ (de hecho, debido al principio de incertidumbre de Heisenberg, que trataremos en otro artículo más adelante, incluso esta posición no es un valor perfectamente exacto, sino que tiene un pequeño margen de error). Sin embargo, si se realiza una medición adicional inmediatamente después de esta primera medición, no se obtienen resultados diferentes cada vez que se mide, sino que siempre se obtiene el mismo resultado. Esto se explica de la siguiente manera:

En el momento en que se realiza la primera medición, la función de onda del objeto medido cambia drásticamente, formando un gráfico de $\|\Psi(x,t)\|^2$ estrecho y puntiagudo concentrado alrededor del punto $C$. Esto se denomina **colapso (collapse)** de la función de onda al punto $C$ debido a la medición.

Es decir, los procesos físicos se pueden dividir en dos tipos distintos:
- Procesos ordinarios en los que la función de onda cambia lentamente según la ecuación de Schrödinger
- Procesos de medición en los que $\Psi$ colapsa repentina y discontinuamente

> La función de onda que ha colapsado debido a la medición se vuelve a extender espacialmente con el tiempo según la ecuación de Schrödinger. Por lo tanto, para reproducir el mismo resultado de medición, la segunda medición debe realizarse inmediatamente.
{: .prompt-tip }

## Normalización de la función de onda
Como el cuadrado del valor absoluto de la función de onda $\|\Psi(x,t)\|^2$ es la densidad de probabilidad de encontrar la partícula en la posición $x$ en el tiempo $t$, la integral de $\|\Psi\|^2$ sobre todos los $x$ debe ser igual a 1.

$$ \int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1. \label{eqn:wavefunction_norm}\tag{3} $$

En la ecuación ($\ref{eqn:schrodinger_eqn}$), si $\Psi(x,t)$ es una solución, entonces $A\Psi(x,t)$ también es una solución para cualquier constante compleja $A$. Por lo tanto, se debe determinar esta $A$ para satisfacer la ecuación ($\ref{eqn:wavefunction_norm}$), y este proceso se llama normalización de la función de onda. Algunas soluciones de la ecuación de Schrödinger divergen a infinito cuando se integran, y en este caso no existe una constante $A$ que satisfaga la ecuación ($\ref{eqn:wavefunction_norm}$). Lo mismo ocurre con la solución trivial $\Psi=0$. Estas **soluciones no normalizables** no pueden representar partículas y no son funciones de onda válidas. Los estados físicamente posibles corresponden a soluciones **de cuadrado integrable** de la ecuación de Schrödinger.

Además, una propiedad importante de la ecuación de Schrödinger es que <u>una función de onda normalizada en un punto en el tiempo permanece normalizada ($\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1$) a medida que pasa el tiempo, incluso cuando $\Psi$ cambia</u>. Si tuviéramos que normalizar la función de onda con un valor $A$ diferente en cada punto en el tiempo, $A$ ya no sería una constante sino una función del tiempo $t$, lo que haría imposible encontrar soluciones a la ecuación de Schrödinger, pero debido a esta propiedad, el valor $A$ normalizado en la condición inicial ($t=0$) se conserva independientemente del tiempo $t$.

### Demostración

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \int_{-\infty}^{\infty} \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx. \label{eqn:norm_proof_1}\tag{4} $$

> El resultado de integrar $\|\Psi\|^2$ con respecto a $x$ es una función solo de $t$, por lo que usamos la derivada total ($d/dt$) en el lado izquierdo, pero $\|\Psi\|^2$ en sí es una función de dos variables $x$ y $t$, por lo que usamos la derivada parcial ($\partial/\partial t$) en el lado derecho.
{: .prompt-tip }

La ecuación anterior se puede reescribir según la regla de derivación del producto como:

$$ \frac{\partial}{\partial t}|\Psi|^2 = \frac{\partial}{\partial t}(\Psi^*\Psi) = \Psi^*\frac{\partial \Psi}{\partial t} + \frac{\partial \Psi^*}{\partial t}\Psi. \label{eqn:norm_proof_2}\tag{5}$$

Si multiplicamos ambos lados de la ecuación de Schrödinger ($\ref{eqn:schrodinger_eqn}$) por $-\cfrac{i}{\hbar}$, obtenemos:

$$ \frac{\partial \Psi}{\partial t} = \frac{i\hbar}{2m}\frac{\partial^2 \Psi}{\partial x^2}-\frac{i}{\hbar}V\Psi \label{eqn:norm_proof_3}\tag{6}$$

y tomando el conjugado complejo de $\cfrac{\partial \Psi}{\partial t}$ en la ecuación anterior:

$$ \frac{\partial \Psi^*}{\partial t} = -\frac{i\hbar}{2m}\frac{\partial^2 \Psi^*}{\partial x^2}+\frac{i}{\hbar}V\Psi^* \label{eqn:norm_proof_4}\tag{7}$$

Ahora, sustituyendo ($\ref{eqn:norm_proof_3}$) y ($\ref{eqn:norm_proof_4}$) en ($\ref{eqn:norm_proof_2}$):

$$\begin{align*}
\frac{\partial}{\partial t}|\Psi|^2 &= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right) \\
&= \frac{\partial}{\partial x}\left[\frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right) \right] 
\end{align*} \label{eqn:norm_proof_5}\tag{8}$$

y sustituyendo esto en el lado derecho de la ecuación inicial ($\ref{eqn:norm_proof_1}$):

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|_{-\infty}^{\infty}. \label{eqn:norm_proof_6}\tag{9} $$

Sin embargo, para que la función de onda esté normalizada y sea físicamente válida, $\Psi(x,t)$ debe converger a $0$ cuando $x$ tiende a $\pm\infty$. Por lo tanto:

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 0 \label{eqn:norm_proof_fin}\tag{10} $$

lo que significa que $\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx$ es una constante independiente del tiempo.

$$ \therefore \text{Si }\Psi\text{ está normalizada en un punto en el tiempo }t\text{, permanece normalizada para todos los demás puntos en el tiempo }t. \blacksquare $$

## Corriente de probabilidad (probability current)
Ahora, llamemos $P_{ab}(t)$ a la probabilidad de encontrar la partícula en la región $a<x<b$ en el tiempo $t$. Entonces:

$$ P_{ab}(t) = \int_a^b |\Psi(x,t)|^2 dx \tag{11}$$

y,

$$ \begin{align*}
\frac{dP_{ab}}{dt} &= \frac{d}{dt}\int_a^b |\Psi(x,t)|^2 dx \\
&= \int_a^b \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx \quad \text{(Ver ecuación }\ref{eqn:norm_proof_1}\text{)}\\
&= \int_a^b \left(\frac{\partial \Psi^*}{\partial t}\Psi + \Psi^*\frac{\partial \Psi}{\partial t} \right)dx \quad \text{(Ver ecuación }\ref{eqn:norm_proof_2}\text{)} \\
&= \frac{i\hbar}{2m}\int_a^b \left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right)dx \\
&= \frac{i\hbar}{2m}\int_a^b\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \quad \text{(Ver ecuaciones }\ref{eqn:norm_proof_3},\ref{eqn:norm_proof_4},\ref{eqn:norm_proof_5}\text{)}\\
&= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial \Psi}{\partial x}-\frac{\partial \Psi^*}{\partial x}\Psi \right)\Bigg|^b_a \\
&= \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x} \right)\Bigg|^a_b
\end{align*} $$

Aquí, si definimos:

$$ J(x,t) \equiv \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x}\right) \label{eqn:probability_current}\tag{12}$$

entonces,

$$ \frac{dP_{ab}}{dt} = J(a,t) - J(b,t) \label{eqn:probability_over_time}\tag{13}$$

$J(x,t)$, definido en la ecuación ($\ref{eqn:probability_current}$), se llama **corriente de probabilidad** y representa el flujo de probabilidad* (es decir, la probabilidad por unidad de tiempo) que pasa por el punto $x$. En la ecuación ($\ref{eqn:probability_over_time}$), si la corriente de probabilidad $J(a,t)$ que fluye hacia un extremo en un momento dado $t$ es mayor que la corriente de probabilidad $J(b,t)$ que fluye hacia el otro extremo, $P_{ab}$ aumenta, y en el caso contrario, disminuye.

> *En la mecánica de fluidos, el flujo (flow rate) de masa o volumen del fluido se ha reemplazado aquí por la probabilidad.
{: .prompt-info }
