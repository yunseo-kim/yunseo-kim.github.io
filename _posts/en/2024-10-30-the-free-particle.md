---
title: "The Free Particle"
description: >-
  We explore the fact that the separated variable solution for a free particle with V(x)=0 cannot be normalized and what this implies,
  qualitatively show the position-momentum uncertainty relation for the general solution, and calculate and physically interpret the phase velocity and group velocity of Ψ(x,t).
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
---

## TL;DR
> - Free particle: $V(x)=0$, no boundary conditions (arbitrary energy)
> - The separated variable solution $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ diverges to infinity when squared and integrated, so it cannot be normalized, implying:
>   - Free particles cannot exist in stationary states
>   - Free particles cannot have a precisely defined single energy value (energy uncertainty exists)
> - Nevertheless, the general solution of the time-dependent Schrödinger equation is a linear combination of separated variable solutions, so the separated variable solutions still have mathematical significance. However, in this case, as there are no constraints, the general solution is in the form of an integral ($\int$) over the continuous variable $k$, not a sum ($\sum$) over the discrete variable $n$.
> - General solution of the Schrödinger equation:
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{where }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - Relationship between position uncertainty and momentum uncertainty:
>   - As position uncertainty decreases, momentum uncertainty increases, and vice versa
>   - In other words, quantum mechanically, it is impossible to know both the position and momentum of a free particle precisely at the same time
> - Phase velocity and group velocity of the wave function $\Psi(x,t)$:
>   - Phase velocity: $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - Group velocity: $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - Physical meaning of group velocity and comparison with classical mechanics:
>   - Physically, the group velocity represents the particle's speed of motion
>   - Assuming $\phi(k)$ is very sharp around some value $k_0$ (when momentum uncertainty is sufficiently small), 
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Prerequisites
- Euler's formula
- Fourier transform & Plancherel's theorem
- [Schrödinger Equation and the Wave Function](/posts/schrodinger-equation-and-the-wave-function/)
- [Time-Independent Schrödinger Equation](/posts/time-independent-schrodinger-equation/)
- [The Infinite Square Well](/posts/the-infinite-square-well/)

## Model Setup
Let's consider the simplest case of a free particle ($V(x)=0$). Classically, this is just uniform motion, but in quantum mechanics, this problem is more interesting.  
The [time-independent Schrödinger equation](/posts/time-independent-schrodinger-equation/) for a free particle is

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

i.e.,

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, where }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[Up to this point, it's the same as the interior of an infinite square well with $V=0$](/posts/the-infinite-square-well/#model-and-boundary-condition-setup). However, this time, let's write the general solution in the form of exponential functions:

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ and $C\cos{kx}+D\sin{kx}$ are equivalent ways of writing the same function of $x$. By Euler's formula $e^{ix}=\cos{x}+i\sin{x}$,
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> That is, if we set $C=A+B$, $D=i(A-B)$, then 
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> Conversely, expressing $A$ and $B$ in terms of $C$ and $D$, we get $A=\cfrac{C-iD}{2}$, $B=\cfrac{C+iD}{2}$.
>
> In quantum mechanics, when $V=0$, exponential functions represent moving waves and are most convenient when dealing with free particles. On the other hand, sine and cosine functions are useful for representing standing waves and naturally appear in the case of the infinite square well.
{: .prompt-info }

Unlike the infinite square well, there are no boundary conditions restricting $k$ and $E$ this time. In other words, a free particle can have any positive energy.

## Separated Variable Solution and Phase Velocity
Adding the time dependence $e^{-iEt/\hbar}$ to $\psi(x)$, we get

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

Any function of $x$ and $t$ that depends on a special form $(x\pm vt)$ represents a wave moving in the $\mp x$ direction with speed $v$, without changing its shape. Therefore, the first term in equation ($\ref{eqn:Psi_seperated_solution}$) represents a wave moving to the right, and the second term represents a wave with the same wavelength and propagation speed but different amplitude moving to the left. Since they only differ in the sign before $k$, we can write

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

where the direction of wave propagation according to the sign of $k$ is as follows:

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{moving to the right}, \\
k<0 \Rightarrow & \text{moving to the left}.
\end{cases} \tag{6}$$

The 'stationary state' of a free particle is clearly a propagating wave*, with wavelength $\lambda = 2\pi/\|k\|$ and momentum

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

according to the de Broglie formula.

> *It's obviously contradictory physically to be a 'stationary state' yet a propagating wave. The reason will soon become clear.
{: .prompt-info }

Also, the speed of this wave is as follows:

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(Here, $\omega$ is the coefficient $\cfrac{\hbar k^2}{2m}$ in front of $t$.)

However, this wave function cannot be normalized as it diverges to infinity when squared and integrated:

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

In other words, <u>for a free particle, the separated variable solution is not a physically possible state.</u> Free particles cannot exist in [stationary states](/posts/time-independent-schrodinger-equation/#1-they-are-stationary-states) and cannot have [a specific energy value](/posts/time-independent-schrodinger-equation/#2-they-have-a-definite-total-energy-value-e-not-a-probability-distribution-over-a-range). In fact, intuitively, it would be stranger if standing waves formed without any boundary conditions at both ends.

## Finding the General Solution $\Psi(x,t)$ of the Time-Dependent Schrödinger Equation
Nevertheless, this separated variable solution still holds important meaning because, apart from physical interpretation, it has mathematical significance as [the general solution of the time-dependent Schrödinger equation is a linear combination of separated variable solutions](/posts/time-independent-schrodinger-equation/#3-the-general-solution-of-the-time-dependent-schrödinger-equation-is-a-linear-combination-of-separated-solutions). However, in this case, as there are no constraints, the general solution takes the form of an integral ($\int$) over the continuous variable $k$, rather than a sum ($\sum$) over the discrete variable $n$.

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> Here, $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ plays the same role as $c_n$ in [equation (21) of the 'Time-Independent Schrödinger Equation' post](/posts/time-independent-schrodinger-equation/#3-the-general-solution-of-the-time-dependent-schrödinger-equation-is-a-linear-combination-of-separated-solutions).
{: .prompt-info }

This wave function can be normalized for appropriate $\phi(k)$, but it must have a range of $k$, and thus a range of energies and velocities. This is called a **wave packet**.

> A sine function cannot be normalized as it is spatially infinitely spread. However, when multiple such waves are superposed, they become localized due to interference and can be normalized.
{: .prompt-info }

## Finding $\phi(k)$ Using Plancherel's Theorem

Now that we know the form of $\Psi(x,t)$ (equation [$\ref{eqn:Psi_general_solution}$]), we just need to determine $\phi(k)$ that satisfies the initial wave function

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

This is a typical problem in Fourier analysis, and we can find the answer using **Plancherel's theorem**.

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$ is called the **Fourier transform** of $f(x)$, and $f(x)$ is called the **inverse Fourier transform** of $F(k)$. As can be easily seen from equation ($\ref{eqn:plancherel_theorem}$), the only difference between the two is the sign in the exponent. Of course, there is a restriction that only functions for which the integral exists are allowed.

> The necessary and sufficient condition for $f(x)$ to exist is that $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ must be finite. In this case, $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ is also finite, and 
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> Some people refer to this equation, rather than equation ($\ref{eqn:plancherel_theorem}$), as Plancherel's theorem ([Wikipedia](https://en.wikipedia.org/wiki/Plancherel_theorem) also describes it this way).
{: .prompt-info }

In this case, the integral must exist due to the physical condition that $\Psi(x,0)$ must be normalized. Therefore, the quantum mechanical solution for a free particle is equation ($\ref{eqn:Psi_general_solution}$), where

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> However, in practice, there are very few cases where the integral in equation ($\ref{eqn:Psi_general_solution}$) can be solved analytically. Usually, numerical analysis using computers is used to calculate the values.
{: .prompt-tip }

## Calculation and Physical Interpretation of the Group Velocity of Wave Packets

Essentially, a wave packet is a superposition of numerous sine functions with amplitudes determined by $\phi$. In other words, there are 'ripples' within an 'envelope' that forms the wave packet.

![A wave packet with the group velocity larger(5x) than phase velocity](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/wave_packet.gif)
> *Image License and Original Source Notice*
> - Image generation source code (gnuplot): [yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/wave_packet.plt)
> - License: [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualization/blob/main/LICENSE)
> - Original author: [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - Original license notice: [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

Physically, what corresponds to the particle's velocity is not the velocity of individual ripples (**phase velocity**) calculated in equation ($\ref{eqn:phase_velocity}$), but the velocity of the outer envelope (**group velocity**).

### Relationship Between Position Uncertainty and Momentum Uncertainty
Let's examine the relationship between position uncertainty and momentum uncertainty by focusing on the integrand parts $\int\phi(k)e^{ikx}dk$ from equation ($\ref{eqn:Psi_at_t_0}$) and $\int\Psi(x,0)e^{-ikx}dx$ from equation ($\ref{eqn:phi}$).

#### When Position Uncertainty is Small
When $\Psi$ is distributed in a very narrow region $[x_0-\delta, x_0+\delta]$ around some value $x_0$ in position space and is close to 0 outside this region (<u>when position uncertainty is small</u>), $e^{-ikx} \approx e^{-ikx_0}$ is almost constant with respect to $x$, so

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{eqn. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

The definite integral term is constant with respect to $p$, so due to the $e^{-ipx_0/\hbar}$ term in front, $\phi$ takes the form of a sine wave with respect to $p$ in momentum space, meaning it is distributed over a wide range of momentum (<u>momentum uncertainty is large</u>).

#### When Momentum Uncertainty is Small
Similarly, when $\phi$ is distributed in a very narrow region $[p_0-\delta, p_0+\delta]$ around some value $p_0$ in momentum space and is close to 0 outside this region (<u>when momentum uncertainty is small</u>), by equation ($\ref{eqn:de_broglie_formula}$), $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ is almost constant with respect to $p$ and $dk=\frac{1}{\hbar}dp$, so

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

Due to the $e^{ip_0x/\hbar}$ term in front, $\Psi$ takes the form of a sine wave with respect to $x$ in position space, meaning it is distributed over a wide range of position (<u>position uncertainty is large</u>).

#### Conclusion
As position uncertainty decreases, momentum uncertainty increases, and vice versa. Therefore, quantum mechanically, it is impossible to know both the position and momentum of a free particle precisely at the same time.

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *Image Source*
> - Author: English Wikipedia user [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - License: public domain

> In fact, due to the uncertainty principle, this applies not only to free particles but to all cases. We will cover the uncertainty principle in a separate post later.
{: .prompt-info }

### Group Velocity of Wave Packets
Rewriting the general solution in equation ($\ref{eqn:Psi_general_solution}$) with $\omega \equiv \cfrac{\hbar k^2}{2m}$ as in equation ($\ref{eqn:phase_velocity}$), we get

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> An equation expressing $\omega$ as a function of $k$, such as $\omega = \cfrac{\hbar k^2}{2m}$, is called a **dispersion relation**. The following content applies generally to all wave packets regardless of the dispersion relation.
{: .prompt-info }

Now, let's assume that $\phi(k)$ has a very sharp shape around some appropriate value $k_0$. (It's okay if it's widely spread in $k$, but such a wave packet shape quickly distorts and changes into a different form. As components with different $k$ move at different speeds, it loses the meaning of a well-defined 'group' velocity. In other words, <u>the uncertainty in momentum increases.</u>)  
Since the integrand can be ignored except near $k_0$, we can Taylor expand the function $\omega(k)$ around this point, and writing up to the first-order term, we get

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

Now, substituting $s=k-k_0$ and integrating centered around $k_0$, we get

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

The term $e^{i(k_0x-\omega_0t)}$ in front represents a sine wave ('ripple') moving at speed $\omega_0/k_0$, and the integral term ('envelope') that determines the amplitude of this sine wave moves at speed $\omega_0^\prime$ due to the $e^{is(x-\omega_0^\prime t)}$ part. Therefore, the phase velocity at $k=k_0$ is

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

which confirms again that it's the same as the value in equation ($\ref{eqn:phase_velocity}$), and the group velocity is

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

which is twice the phase velocity.

## Comparison with Classical Mechanics

Knowing that classical mechanics holds at macroscopic scales, the results obtained through quantum mechanics should approximate the calculations from classical mechanics when quantum uncertainties are sufficiently small. In the case of the free particle we're dealing with now, when $\phi(k)$ has a very sharp shape around an appropriate value $k_0$ as assumed earlier (i.e., <u>when momentum uncertainty is sufficiently small</u>), the group velocity $v_\text{group}$, which corresponds to the particle's speed in quantum mechanics, should be equal to the particle's speed $v_\text{classical}$ calculated in classical mechanics for the same $k$ and corresponding energy value $E$.

Substituting $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ from equation ($\ref{eqn:t_independent_schrodinger_eqn}$) into the group velocity we just found (equation [$\ref{eqn:group_velocity}$]), we get

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

and the speed of a free particle with kinetic energy $E$ in classical mechanics is likewise

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

Therefore, since $v_\text{quantum}=v_\text{classical}$, we can confirm that the result obtained by applying quantum mechanics is a physically valid solution.
