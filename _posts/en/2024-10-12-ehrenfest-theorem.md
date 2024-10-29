---
title: "Ehrenfest Theorem"
description: >-
  Learn how to calculate the expectation values of position and momentum from the wave function in quantum mechanics,
  and extend this to the calculation formula for the expectation value of any mechanical variable Q(x,p).
  Then, derive the Ehrenfest theorem from this.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
---

## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Prerequisites
- Continuous probability distribution and probability density
- [Schrödinger equation and wave function](/posts/schrodinger-equation-and-the-wave-function/)

## Calculating Expectation Values from Wave Function
### Expectation Value of Position $x$
The expectation value of position $x$ for a particle in state $\Psi$ is

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

If we measure the position of a sufficiently large number of particles in the same state $\Psi$ and take the average of the measurement results, we obtain $\langle x \rangle$ calculated through the above equation.

> Note that the expectation value mentioned here is not the average obtained by repeatedly measuring one particle, but the average of measurement results for an **ensemble** of systems with the same state. If the same particle is measured repeatedly at short time intervals, the [wave function collapses](/posts/schrodinger-equation-and-the-wave-function/#measurement-and-collapse-of-the-wave-function) at the first measurement, so subsequent measurements will continue to yield the same value.
{: .prompt-warning }

### Expectation Value of Momentum $p$
As $\Psi$ depends on time, $\langle x \rangle$ will change over time. At this point, according to equation (8) in [Schrödinger equation and wave function](/posts/schrodinger-equation-and-the-wave-function/) and equation ($\ref{eqn:x_exp}$) above, the following holds:

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> In the process from equation ($\ref{eqn:dx/dt_1}$) to ($\ref{eqn:dx/dt_2}$) and from ($\ref{eqn:dx/dt_2}$) to ($\ref{eqn:dx/dt_3}$), integration by parts was applied twice, and since $\lim_{x\rightarrow\pm\infty}\Psi=0$, the boundary terms were discarded.
{: .prompt-tip }

Therefore, we obtain the expectation value of **momentum** as follows:

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Expectation Value for Any Physical Quantity $Q(x,p)$
The expressions for $\langle x \rangle$ and $\langle p \rangle$ obtained earlier can be written in the following form:

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

The operator $\hat x \equiv x$ represents position, and the operator $\hat p \equiv -i\hbar(\partial/\partial x)$ represents momentum. For the momentum operator $\hat p$, when extended to three-dimensional space, it can be defined as $\hat p \equiv -i\hbar\nabla$.

Since all classical mechanical variables can be expressed in terms of position and momentum, this can be extended to the expectation value of any physical quantity. To calculate the expectation value of any quantity $Q(x,p)$, replace all $p$ with $-i\hbar\nabla$, and integrate the resulting operator placed between $\Psi^*$ and $\Psi$.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

For example, since kinetic energy $T=\cfrac{p^2}{2m}$,

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

Using equation ($\ref{eqn:Q_exp}$), we can calculate the expectation value of any physical quantity for a particle in state $\Psi$.

## Ehrenfest Theorem
### Calculation of $d\langle p \rangle/dt$
Let's differentiate both sides of equation ($\ref{eqn:p_op}$) with respect to time $t$ to find the time derivative of the expectation value of momentum, $\cfrac{d\langle p \rangle}{dt}$.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> Equation ($\ref{eqn:dp/dt_2}$) can be obtained by substituting equations (6) and (7) from [Schrödinger equation and wave function](/posts/schrodinger-equation-and-the-wave-function/) into equation ($\ref{eqn:dp/dt_1}$). In the process from equation ($\ref{eqn:dp/dt_3}$) to ($\ref{eqn:dp/dt_4}$), integration by parts was applied, and as before, since $\lim_{x\rightarrow\pm\infty}\Psi=0$, the boundary terms were discarded.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Relationship between Ehrenfest Theorem and Newton's Second Law of Motion
The following two equations obtained earlier are called the Ehrenfest theorem:

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

The Ehrenfest theorem has a form quite similar to the relationship between potential energy and conservative force in classical mechanics, $F=\cfrac{dp}{dt}=-\nabla V$.  
Comparing the two equations side by side:

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newton's Second Law of Motion]}$$

If we Taylor expand the right-hand side of the second equation of the Ehrenfest theorem $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (equation [$\ref{eqn:ehrenfest_theorem_2nd}$]) around $\langle x \rangle$ with respect to $x$:

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

If $x-\langle x \rangle$ is sufficiently small, we can ignore all higher-order terms except the first term and approximate:

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

In other words, **if a particle's wave function is spatially distributed very close to a single point (if the dispersion of $\|\Psi\|^2$ with respect to $x$ is very small), the Ehrenfest theorem can be approximated to Newton's Second Law of Motion in classical mechanics.** On a macroscopic scale, we can essentially regard the particle's position as a single point, ignoring the spatial spread of the wave function, so Newton's Second Law of Motion holds. However, on a microscopic scale, quantum mechanical effects cannot be ignored, so Newton's Second Law of Motion no longer holds, and the Ehrenfest theorem must be used.
