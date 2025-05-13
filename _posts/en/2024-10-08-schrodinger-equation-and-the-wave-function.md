---
title: Schrödinger Equation and Wave Function
description: We examine the basic form of the Schrödinger equation, which holds a similar position in quantum mechanics as Newton's laws of motion in classical mechanics. We also explore the statistical interpretation of the physical meaning of wave functions obtained as solutions to the Schrödinger equation, perspectives on quantum indeterminacy, and the physical meaning of measurement in the Copenhagen interpretation (collapse of the wave function).
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
mermaid: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - (Time-dependent) Schrödinger equation: 
>
> $$ i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi $$
>
> - Statistical interpretation of the wave function $\Psi(x,t)$ (Born interpretation): The square of the absolute value of the wave function $\|\Psi(x,t)\|^2$ is the **probability density function** of finding the particle at position $x$ at time $t$.
> - Normalization of the wave function:
>   - $\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx = 1$
>   - If $\Psi(x,t)$ is a solution to the Schrödinger equation, then for any complex constant $A$, $A\Psi(x,t)$ is also a solution, and determining the constant $A$ to satisfy the above equation is called normalization
>   - **Non-normalizable solutions** cannot represent particles and are not valid wave functions; only **square-integrable** solutions are physically possible states
>   - A wave function normalized at one point in time remains normalized as time passes, even as $\Psi$ changes
> - Probability current:
>   - $J(x,t) \equiv \cfrac{i\hbar}{2m}\left(\Psi\cfrac{\partial \Psi^\*}{\partial x}-\Psi^\*\cfrac{\partial \Psi}{\partial x}\right)$
>   - The flow rate (probability per unit time) of the probability of finding a particle passing through point $x$
>   - If $P_{ab}(t)$ is the probability of finding a particle in the region $a<x<b$ at time $t$, then $\cfrac{dP_{ab}}{dt} = J(a,t) - J(b,t)$
{: .prompt-info }

## Prerequisites
- Continuous probability distribution and probability density

## Schrödinger Equation
Let's consider a particle with mass $m$ moving along the $x$-axis under a given force $F(x,t)$.

In classical mechanics, the main goal is to determine the position of the particle $x(t)$ at any time by applying Newton's equation of motion $F=ma$. This process can be roughly represented by the following diagram:

```mermaid
flowchart TD
	conditions["Given conditions"] -- F=ma --> x["Position x(t)"]
	x --> quantities["Physical quantities to be determined"]
```

In quantum mechanics, the same problem is approached in a very different way. The quantum mechanical approach is to solve the following **Schrödinger equation** to find the particle's **wave function** $\Psi(x,t)$.

$$ \begin{gather*}
i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}\\
\text{(} i=\sqrt{-1}\text{, } \hbar=\frac{h}{2\pi}=1.054573\times10^{-34}\text{, } h\text{: Planck constant, } V(x)\text{: potential energy)}
\end{gather*} $$

![Complex plot of a wave function that satisfies the nonrelativistic Schrödinger equation with V = 0(free particle)](https://upload.wikimedia.org/wikipedia/commons/b/b7/Wavepacket-a2k4-en.gif?20210105144724)
> *Image source*
> - Author: Wikimedia user Xcodexif
> - License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

```mermaid
flowchart TD
	conditions["Given conditions Ψ(x,0)"] -- "Schrödinger's Equation" --> x["Wave function Ψ(x,t)"]
	x --> quantities["PD of physical quantities"]
```

## Statistical Interpretation of the Wave Function $\Psi(x,t)$ (Born Interpretation)
While a particle in classical mechanics is located at a single point, the wave function representing a particle's state in quantum mechanics is a function of $x$ at a given $t$, meaning it is spread out in space. How should we interpret this physical meaning?

According to Born's **statistical interpretation**, the square of the absolute value of the wave function $\|\Psi(x,t)\|^2$ is the probability density function of finding the particle at position $x$ at time $t$. Although the wave function $\Psi$ itself is complex, $\|\Psi\|^2=\Psi^\*\Psi$ ($\Psi^\*$ is the complex conjugate of $\Psi$) is a real number greater than or equal to 0, making this interpretation possible. This can be expressed as:

$$ \int_a^b |\Psi(x,t)|^2 dx = \text{Probability of finding the particle between }a\text{ and }b\text{ at time }t. \tag{2}$$

This statistical interpretation implies that quantum mechanics inherently contains a kind of **indeterminacy**. Even if we know everything about the particle (the wave function), we can only know the probability distribution of possible outcomes, not determine a specific value.

Since this was difficult to accept intuitively, questions naturally arose about whether this indeterminacy was due to some flaw in quantum mechanics or an essential characteristic of nature.

## Perspectives on Quantum Indeterminacy
Suppose we measure the position of a particle and find that it is at point $C$. Where was the particle just before the measurement?

### Realist Position

> "God does not play dice."  
> *by Albert Einstein*

The particle was at $C$ all along. This is also the perspective of Einstein and Schrödinger. However, from this viewpoint, quantum mechanics is an incomplete theory because while the particle was actually at exactly $C$, the limitations of the theory only allow us to know the particle's position as a probability distribution until measurement. According to this perspective, indeterminacy is not an essential property of nature but a limitation of quantum mechanics, and there must be some hidden variables in addition to $\Psi$ that need to be known to perfectly describe the particle.

> Schrödinger was once a teaching assistant under Einstein, who was his mentor, and continued to interact with Einstein afterward. It is likely that Schrödinger's realist and deterministic stance was influenced by Einstein.
{: .prompt-info }

### Orthodox Position

> "Stop telling God what to do with his dice."  
> *by Niels Bohr, In answer to Einstein's earlier quote*
>
> "Observations not only disturb what is to be measured, they produce it"  
> ...  
> "We compel to assume a definite position."  
> *by Pascual Jordan*

Until just before measurement, the particle exists only in the form of a probability distribution and is not located anywhere; it is only when the act of measurement is performed that the particle appears at a specific location. This interpretation is called the **Copenhagen interpretation**, proposed by Bohr and Heisenberg at the University of Copenhagen.

> Interestingly, similar to the relationship between Einstein and Schrödinger, Heisenberg was also a student of Bohr.
{: .prompt-info }

### Agnostic Position

> "One should no more rack one's brain about the problem of whether something one cannot know anything about exists all the same, than about the ancient question of how many angels are able to sit on the point of a needle."  
> *by Wolfgang Pauli*

This position refuses to answer. Whatever claim is made about the state of a particle before measurement, if the only way to verify that claim is through measurement, then it is no longer "before measurement" - so what's the point? It's merely metaphysics, debating something that is fundamentally untestable and unknowable.

### Today's Consensus
In 11964 of the [Holocene calendar](https://en.wikipedia.org/wiki/Holocene_calendar), John Bell proved that there is an observable difference depending on whether a particle exists at an exact position before or after measurement, thus excluding the agnostic position. Subsequent experiments have made the Copenhagen interpretation mainstream. Therefore, unless otherwise specified, discussions about quantum mechanics generally assume this Copenhagen interpretation.

> There are still other interpretations that might be correct besides the Copenhagen interpretation, such as nonlocal hidden variable theories or the many worlds interpretation.
{: .prompt-info }

## Measurement and Collapse of the Wave Function
A particle does not have an exact position until it is measured, and only through measurement does it acquire a specific position $C$ (though, as we'll discuss in another post, even this position has some margin of error due to Heisenberg's uncertainty principle). However, if an additional measurement is made immediately after the first measurement, the same result will always be obtained, rather than different values with each measurement. This is explained as follows:

At the moment of the first measurement, the wave function of the subject changes dramatically, forming a narrow and sharp $\|\Psi(x,t)\|^2$ graph concentrated around point $C$. This is called the **collapse** of the wave function to point $C$ due to measurement.

Thus, physical processes can be divided into two distinct types:
- Ordinary processes where the wave function changes slowly according to the Schrödinger equation
- Measurement processes where $\Psi$ collapses suddenly and discontinuously

> A wave function that has collapsed due to measurement will spread out spatially again over time according to the Schrödinger equation. Therefore, to reproduce the same measurement result, the second measurement must be performed immediately.
{: .prompt-tip }

## Normalization of the Wave Function
Since the square of the absolute value of the wave function $\|\Psi(x,t)\|^2$ is the probability density of finding the particle at position $x$ at time $t$, integrating $\|\Psi\|^2$ over all $x$ should equal 1.

$$ \int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1. \label{eqn:wavefunction_norm}\tag{3} $$

From equation ($\ref{eqn:schrodinger_eqn}$), if $\Psi(x,t)$ is a solution, then for any complex constant $A$, $A\Psi(x,t)$ is also a solution. Therefore, $A$ must be determined to satisfy equation ($\ref{eqn:wavefunction_norm}$), and this process is called normalization of the wave function. Some solutions to the Schrödinger equation diverge to infinity when integrated, in which case there is no constant $A$ that satisfies equation ($\ref{eqn:wavefunction_norm}$). The same applies to the trivial solution $\Psi=0$. These **non-normalizable solutions** cannot represent particles and are not valid wave functions. Physically possible states correspond to **square-integrable** solutions of the Schrödinger equation.

Another important property of the Schrödinger equation is that <u>a wave function normalized at one point in time remains normalized ($\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1$) as time passes, even as $\Psi$ changes</u>. If the wave function had to be normalized with a different value of $A$ at each point in time, $A$ would be a function of time $t$ rather than a constant, making it impossible to find solutions to the Schrödinger equation. However, due to this property, the value of $A$ normalized at the initial condition ($t=0$) is preserved regardless of time $t$.

### Proof

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \int_{-\infty}^{\infty} \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx. \label{eqn:norm_proof_1}\tag{4} $$

> The result of integrating $\|\Psi\|^2$ with respect to $x$ is a function of $t$ only, so we use the total derivative ($d/dt$) on the left side, but $\|\Psi\|^2$ itself is a function of two variables $x$ and $t$, so we use the partial derivative ($\partial/\partial t$) on the right side.
{: .prompt-tip }

The above equation can be rewritten according to the product rule of differentiation as follows:

$$ \frac{\partial}{\partial t}|\Psi|^2 = \frac{\partial}{\partial t}(\Psi^*\Psi) = \Psi^*\frac{\partial \Psi}{\partial t} + \frac{\partial \Psi^*}{\partial t}\Psi. \label{eqn:norm_proof_2}\tag{5}$$

Multiplying both sides of the Schrödinger equation ($\ref{eqn:schrodinger_eqn}$) by $-\cfrac{i}{\hbar}$, we get:

$$ \frac{\partial \Psi}{\partial t} = \frac{i\hbar}{2m}\frac{\partial^2 \Psi}{\partial x^2}-\frac{i}{\hbar}V\Psi \label{eqn:norm_proof_3}\tag{6}$$

Taking the complex conjugate of $\cfrac{\partial \Psi}{\partial t}$ from the above equation:

$$ \frac{\partial \Psi^*}{\partial t} = -\frac{i\hbar}{2m}\frac{\partial^2 \Psi^*}{\partial x^2}+\frac{i}{\hbar}V\Psi^* \label{eqn:norm_proof_4}\tag{7}$$

Now, substituting ($\ref{eqn:norm_proof_3}$) and ($\ref{eqn:norm_proof_4}$) into equation ($\ref{eqn:norm_proof_2}$):

$$\begin{align*}
\frac{\partial}{\partial t}|\Psi|^2 &= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right) \\
&= \frac{\partial}{\partial x}\left[\frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right) \right] 
\end{align*} \label{eqn:norm_proof_5}\tag{8}$$

Substituting this into the right side of equation ($\ref{eqn:norm_proof_1}$):

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|_{-\infty}^{\infty}. \label{eqn:norm_proof_6}\tag{9} $$

For a wave function to be normalized and physically valid, $\Psi(x,t)$ must converge to $0$ as $x$ approaches $\pm\infty$. Therefore:

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 0 \label{eqn:norm_proof_fin}\tag{10} $$

Thus, $\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx$ is a constant independent of time.

$$ \therefore \text{If }\Psi\text{ is normalized at one point in time }t\text{, it remains normalized for all other times }t. \blacksquare $$

## Probability Current
Now, let's define $P_{ab}(t)$ as the probability of finding a particle in the region $a<x<b$ at time $t$. Then:

$$ P_{ab}(t) = \int_a^b |\Psi(x,t)|^2 dx \tag{11}$$

and,

$$ \begin{align*}
\frac{dP_{ab}}{dt} &= \frac{d}{dt}\int_a^b |\Psi(x,t)|^2 dx \\
&= \int_a^b \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx \quad \text{(See equation }\ref{eqn:norm_proof_1}\text{)}\\
&= \int_a^b \left(\frac{\partial \Psi^*}{\partial t}\Psi + \Psi^*\frac{\partial \Psi}{\partial t} \right)dx \quad \text{(See equation }\ref{eqn:norm_proof_2}\text{)} \\
&= \frac{i\hbar}{2m}\int_a^b \left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right)dx \\
&= \frac{i\hbar}{2m}\int_a^b\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \quad \text{(See equations }\ref{eqn:norm_proof_3},\ref{eqn:norm_proof_4},\ref{eqn:norm_proof_5}\text{)}\\
&= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial \Psi}{\partial x}-\frac{\partial \Psi^*}{\partial x}\Psi \right)\Bigg|^b_a \\
&= \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x} \right)\Bigg|^a_b
\end{align*} $$

Here, if we define:

$$ J(x,t) \equiv \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x}\right) \label{eqn:probability_current}\tag{12}$$

then,

$$ \frac{dP_{ab}}{dt} = J(a,t) - J(b,t) \label{eqn:probability_over_time}\tag{13}$$

$J(x,t)$ defined by equation ($\ref{eqn:probability_current}$) is called the **probability current**, and it represents the flow rate* of the probability of finding a particle passing through point $x$ (i.e., probability per unit time). From equation ($\ref{eqn:probability_over_time}$), if the probability current flowing in at one end $J(a,t)$ is greater than the probability current flowing out at the other end $J(b,t)$ at a specific time $t$, then $P_{ab}$ increases, and vice versa.

> *Think of it as the flow rate from fluid mechanics, where the mass or volume of fluid is replaced by probability.
{: .prompt-info }
