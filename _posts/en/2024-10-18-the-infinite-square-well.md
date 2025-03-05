---
title: The 1D Infinite Square Well
description: We examine the simple yet important representative problem of the 1D
  infinite square well, which well illustrates the basic concepts of quantum mechanics.
  We find the nth stationary state ψ(x) and energy E of a particle in this ideal situation,
  and learn four important mathematical properties of ψ(x). From this, we derive the
  general solution Ψ(x,t).
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - 1D Infinite Square Well Problem: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{otherwise}
>   \end{cases}$$
> - Boundary conditions: $ \psi(0) = \psi(a) = 0 $
> - Energy levels of the nth stationary state: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Solution of the time-independent Schrödinger equation inside the well:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Physical interpretation of each stationary state $\psi_n$: 
>   - Form of standing waves on a string of length $a$
>   - **Ground state**: The stationary state $\psi_1$ with the lowest energy
>   - **Excited states**: The remaining states with $n\geq 2$ where energy increases proportionally to $n^2$
> - Four important mathematical properties of $\psi_n$:
>   1. If the potential $V(x)$ has symmetry, even and odd functions appear alternately about the center of the well
>   2. As energy increases, each consecutive state increases by one **node**
>   3. Possesses **orthonormality**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. Possesses **completeness**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - General solution of the Schrödinger equation (linear combination of stationary states):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{where the coefficient }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Prerequisites
- Continuous probability distribution and probability density
- Orthogonality and normalization (Linear Algebra)
- Fourier series and completeness (Linear Algebra)
- [Schrödinger Equation and the Wave Function](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfest Theorem](/posts/ehrenfest-theorem/)
- [Time-Independent Schrödinger Equation](/posts/time-independent-schrodinger-equation/)

## Given Potential Condition
If the potential is

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{otherwise}
\end{cases} \tag{1}$$

then a particle in this potential is a free particle within the range $0<x<a$ and experiences an infinite force at both ends ($x=0$ and $x=a$), preventing escape. In a classical model, this is interpreted as an infinite back-and-forth motion with perfectly elastic collisions at both ends, without any non-conservative forces acting. Although this potential is highly artificial and simple, it can serve as a useful reference case when studying other physical situations in quantum mechanics, so it needs to be carefully examined.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Image source*
> - Author: Wikimedia user [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Model and Boundary Condition Setup
Outside the well, the probability of finding the particle is $0$, so $\psi(x)=0$. Inside the well, $V(x)=0$, so the [time-independent Schrödinger equation](/posts/time-independent-schrodinger-equation/) is

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

that is,

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ where } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

> Here, we assume $E\geq 0$.
{: .prompt-info }

This is the equation describing a classical **simple harmonic oscillator**, and its general solution is

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

Here, $A$ and $B$ are arbitrary constants, and when finding a specific solution that fits the problem situation, these constants are typically determined by the **boundary conditions** given in the problem. <u>For $\psi(x)$, the boundary conditions are usually that both $\psi$ and $d\psi/dx$ are continuous, but where the potential becomes infinite, only $\psi$ is continuous.</u>

## Solving the Time-Independent Schrödinger Equation

Since $\psi(x)$ is continuous,

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

must connect with the solution outside the well. From equation ($\ref{eqn:psi_general_solution}$), when $x=0$,

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

so, substituting ($\ref{eqn:boundary_conditions}$), we must have $B=0$.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Then, $\psi(a)=A\sin{ka}$, so to satisfy $\psi(a)=0$ from equation ($\ref{eqn:boundary_conditions}$), either $A=0$ (trivial solution) or $\sin{ka}=0$. Therefore,

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Here too, $k=0$ is a trivial solution, and since it results in $\psi(x)=0$, which cannot be normalized, it is not the solution we are looking for in this problem. Also, since $\sin(-\theta)=-\sin(\theta)$, the negative sign can be absorbed into $A$ in equation ($\ref{eqn:psi_without_B}$), so considering only the case where $ka>0$ does not lose generality. Therefore, the possible solutions for $k$ are

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Then, $\psi_n=A\sin{k_n x}$ and $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, so substituting into equation ($\ref{eqn:t_independent_schrodinger_eqn}$), the possible $E$ values are as follows:

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

In stark contrast to the classical case, a quantum particle in an infinite square well cannot have arbitrary energy but must have one of the allowed values.

> Energy is quantized by the boundary conditions applied to the solution of the time-independent Schrödinger equation.
{: .prompt-info }

Now we can find $A$ by normalizing $\psi$.

> Originally, we normalize $\Psi(x,t)$, but according to equation (11) in [Time-Independent Schrödinger Equation](/posts/time-independent-schrodinger-equation/#1-they-are-stationary-states), this corresponds to normalizing $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

This strictly determines only the magnitude of $A$, but since the phase of $A$ has no physical meaning, we can just use the positive real square root as $A$. Therefore, the solution inside the well is

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Physical Interpretation of Each Stationary State $\psi_n$
As in equation ($\ref{eqn:psi_n}$), we have found an infinite number of solutions for each energy level $n$ from the time-independent Schrödinger equation. If we draw the first few of these in a graph, it looks like the image below.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Image source*
> - Author: Wikimedia user [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

These states take the form of standing waves on a string of length $a$, with $\psi_1$ having the lowest energy called the **ground state**, and the remaining states with $n\geq 2$ where energy increases proportionally to $n^2$ called **excited states**.

## Four Important Mathematical Properties of $\psi_n$
All functions $\psi_n(x)$ have the following four important properties. These four properties are very powerful and are not limited to the infinite square well. The first property always holds if the potential itself is a function with symmetry, and the second, third, and fourth properties are general properties that appear regardless of the shape of the potential.

### 1. Even and odd functions appear alternately about the center of the well.
For positive integers $n$, $\psi_{2n-1}$ is an even function, and $\psi_{2n}$ is an odd function.

### 2. As energy increases, each consecutive state increases by one node.
For positive integers $n$, $\psi_n$ has $(n-1)$ **nodes**.

### 3. These states possess orthogonality.

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

In this sense, they are **orthogonal** to each other.

> In the case of the infinite square well we are looking at now, $\psi$ is real, so we don't need to take the complex conjugate ($^*$) of $\psi_m$, but it's good to get into the habit of always attaching it for cases where it's not.
{: .prompt-tip }

#### Proof
When $m\neq n$,

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

When $m=n$, this integral becomes 1 due to normalization, and using the **Kronecker delta** $\delta_{mn}$, we can express orthogonality and normalization together as

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

In this case, $\psi$ is said to be **orthonormal**.

### 4. These functions possess completeness.
In the sense that any other function $f(x)$ can be written as a linear combination

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

these functions are **complete**. Equation ($\ref{eqn:fourier_series}$) is the **Fourier series** of $f(x)$, and the fact that any function can be expanded in this way is called **Dirichlet's theorem**.

## Finding Coefficients $c_n$ Using Fourier's Trick
When $f(x)$ is given, we can find the coefficients $c_n$ using the following method called **Fourier's trick**, utilizing the completeness and orthonormality of $\psi(x)$. Multiply both sides of equation ($\ref{eqn:fourier_series}$) by $\psi_m(x)^*$ and integrate, then by equations ($\ref{eqn:orthonomality}$) and ($\ref{eqn:kronecker_delta}$),

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Note that all terms in the sum except for $n=m$ disappear due to the Kronecker delta.
{: .prompt-info }

Therefore, the $n$-th coefficient when expanding $f(x)$ is

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Finding the General Solution $\Psi(x,t)$ of the Time-Dependent Schrödinger Equation
Each stationary state of the infinite square well is, according to equation (10) in the ['Time-Independent Schrödinger Equation' post](/posts/time-independent-schrodinger-equation/#1-they-are-stationary-states) and equation ($\ref{eqn:psi_n}$) we found earlier,

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

Also, as we saw earlier in the [Time-Independent Schrödinger Equation](/posts/time-independent-schrodinger-equation/#3-the-general-solution-of-the-time-dependent-schrödinger-equation-is-a-linear-combination-of-separated-solutions), the general solution of the Schrödinger equation can be expressed as a linear combination of stationary states. Therefore,

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

Now we just need to find the coefficients $c_n$ that satisfy the following condition:

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

By the completeness of $\psi$ we examined earlier, $c_n$ that satisfies the above always exists, and can be found by substituting $\Psi(x,0)$ for $f(x)$ in equation ($\ref{eqn:coefficients_n}$).

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

If $\Psi(x,0)$ is given as an initial condition, use equation ($\ref{eqn:calc_of_cn}$) to find the expansion coefficients $c_n$, and substitute these into equation ($\ref{eqn:general_solution}$) to find $\Psi(x,t)$. Then, according to the process of the [Ehrenfest theorem](/posts/ehrenfest-theorem/), any physical quantity of interest can be calculated. This method can be applied not only to the infinite square well but also to arbitrary potentials, with only the form of the $\psi$ function and the equation for allowed energy levels changing.

## Derivation of Energy Conservation ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Let's derive the energy conservation that we briefly looked at earlier in the [Time-Independent Schrödinger Equation](/posts/time-independent-schrodinger-equation/#energy-conservation) using the orthonormality of $\psi(x)$ (equations [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]). Since $c_n$ is independent of time, it's sufficient to prove it for the case when $t=0$.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

Also, since

$$ \hat{H}\psi_n = E_n\psi_n $$

we get the following:

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
