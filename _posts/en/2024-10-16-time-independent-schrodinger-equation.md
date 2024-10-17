---
title: "Time-independent Schrödinger Equation"
description: >-
  We derive the time-independent Schrödinger equation ψ(x) by applying the separation of variables method
  to the original form of the Schrödinger equation (time-dependent Schrödinger equation) Ψ(x,t).
  We explore the mathematical and physical significance and importance of the separated solution obtained this way.
  We also examine the method of obtaining the general solution of the Schrödinger equation
  as a linear combination of separated solutions.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
---

## TL;DR
> - Separated solution: $ \Psi(x,t) = \psi(x)\phi(t)$
> - Time dependence ("wiggle factor"): $ \phi(t) = e^{-iEt/\hbar} $
> - Hamiltonian operator: $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - Time-independent Schrödinger equation: $ \hat H\psi = E\psi $
> - Physical and mathematical significance and importance of the separated solution:
>   1. Stationary states
>   2. Has a definite total energy value $E$
>   3. The general solution of the Schrödinger equation is a linear combination of separated solutions
> - General solution of the time-dependent Schrödinger equation: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Prerequisites
- Continuous probability distribution and probability density
- [Schrödinger Equation and Wave Function](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfest Theorem](/posts/ehrenfest-theorem/)
- [Separation of Variables](/posts/Separation-of-Variables/)

## Derivation Using Separation of Variables
In the [post about Ehrenfest's theorem](/posts/ehrenfest-theorem/), we looked at how to calculate various physical quantities using the wave function $\Psi$. The important question then is how to obtain this wave function $\Psi(x,t)$. Usually, for a given potential $V(x,t)$, we need to solve the [Schrödinger equation](/posts/schrodinger-equation-and-the-wave-function/), which is a partial differential equation in position $x$ and time $t$.

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

If the potential $V$ is independent of time $t$, we can solve the above Schrödinger equation using the [separation of variables method](/posts/Separation-of-Variables/). Let's consider a solution expressed as the product of a function $\psi$ of $x$ only and a function $\phi$ of $t$ only:

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

At first glance, this may seem like an unreasonably restrictive expression that can only find a small subset of the entire solution. However, the solution obtained this way not only has important meanings but can also be used to find the general solution by adding these separable solutions in a specific way.

For the separable solution,

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

Substituting these into equation ($\ref{eqn:schrodinger_eqn}$), we can write the Schrödinger equation as:

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

Dividing both sides by $\psi\phi$, we get:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

where the left side is a function of $t$ only and the right side is a function of $x$ only.

For this equation to have a solution, both sides must be equal to a constant. If not, when one variable ($t$ or $x$) is kept constant and the other is changed, only one side of the equation would change, making the equality no longer true. Therefore, we can set the left side to a separation constant $E$:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

This gives us two ordinary differential equations. One is for the time part:

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

and the other is for the spatial part:

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

The ordinary differential equation for $t$ ($\ref{eqn:ode_t}$) can be easily solved. The general solution to this equation is $ce^{-iEt/\hbar}$, but since we're more interested in the product $\psi\phi$ rather than $\phi$ itself, we can include the constant $c$ in $\psi$. This gives us:

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

The ordinary differential equation for $x$ ($\ref{eqn:t_independent_schrodinger_eqn}$) is called the **time-independent Schrödinger equation**. This equation can only be solved if we know the potential $V(x)$.

## Physical and Mathematical Significance
We have derived the function $\phi(t)$ of time $t$ only and the time-independent Schrödinger equation ($\ref{eqn:t_independent_schrodinger_eqn}$) using the separation of variables method. Although most solutions of the original **time-dependent Schrödinger equation** ($\ref{eqn:schrodinger_eqn}$) cannot be expressed in the form of $\psi(x)\phi(t)$, the time-independent Schrödinger equation form is important because of the following three properties of its solutions.

### 1. They are stationary states.
While the wave function itself

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

depends on $t$, the probability density

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

is constant over time as the time dependence cancels out.

> For normalizable solutions, the separation constant $E$ must be real.
>
> If we set $E$ in equation ($\ref{eqn:separation_of_variables}$) as a complex number $E_0+i\Gamma$ (where $E_0$ and $\Gamma$ are real),
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> As we saw earlier in [Schrödinger Equation and Wave Function](/posts/schrodinger-equation-and-the-wave-function/#normalization-of-the-wave-function), $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ should be a time-independent constant, so $\Gamma=0$. $\blacksquare$
{: .prompt-info }

The same thing happens when calculating the expectation value of any physical quantity, so equation (8) from [Ehrenfest's theorem](/posts/ehrenfest-theorem/) becomes:

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

Therefore, all expectation values are constant with respect to time. In particular, since $\langle x \rangle$ is constant, $\langle p \rangle=0$.

### 2. They have a definite total energy value $E$, not a probability distribution over a range.
In classical mechanics, the total energy (kinetic energy plus potential energy) is called the **Hamiltonian** and is defined as:

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

Therefore, if we replace $p$ with $-i\hbar(\partial/\partial x)$, the corresponding Hamiltonian operator in quantum mechanics is:

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

Thus, the time-independent Schrödinger equation ($\ref{eqn:t_independent_schrodinger_eqn}$) can be written as:

$$ \hat H \psi = E\psi \tag{15}$$

and the expectation value of the Hamiltonian is:

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

Also,

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

so

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

Therefore, the variance of the Hamiltonian $H$ is:

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

In other words, when the total energy is measured for the separated solution, it always measures a constant value $E$.

### 3. The general solution of the time-dependent Schrödinger equation is a linear combination of separated solutions.

The time-independent Schrödinger equation ($\ref{eqn:t_independent_schrodinger_eqn}$) has infinitely many solutions $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$. Let's call this set \{$\psi_n(x)$\}. For each of these, there exists a separation constant $E_1,E_2,E_3,\dots=$\{$E_n$\}, so for each **possible energy level**, there is a corresponding wave function.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

The time-dependent Schrödinger equation ($\ref{eqn:schrodinger_eqn}$) has the property that a linear combination of any two solutions is also a solution. Therefore, once we find the separated solutions, we can immediately obtain a more general form of solution:

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

All solutions of the time-dependent Schrödinger equation can be written in this form, and the remaining task is to find the appropriate constants $c_1, c_2, \dots$ to satisfy the initial conditions given in the problem and find the particular solution we're looking for. In other words, if we can solve the time-independent Schrödinger equation, we can then easily find the general solution of the time-dependent Schrödinger equation.

> Note that while the separated solution 
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> is a stationary state where all probabilities and expectation values are independent of time, the general solution in equation ($\ref{eqn:general_solution}$) does not have this property.
{: .prompt-warning }

## Energy Conservation
In the general solution ($\ref{eqn:general_solution}$), the square of the absolute value of the coefficients \{$c_n$\}, $\|c_n\|^2$, physically represents the probability of measuring the energy value $E_n$ when measuring the energy of a particle in the given state ($\Psi$). Therefore, the sum of these probabilities should be:

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

and the expectation value of the Hamiltonian is:

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

Here, since both the energy levels $E_n$ of each stationary state and the coefficients \{$c_n$\} are independent of time, the probability of measuring a specific energy $E_n$ and the expectation value of the Hamiltonian $H$ also remain constant, independent of time.
