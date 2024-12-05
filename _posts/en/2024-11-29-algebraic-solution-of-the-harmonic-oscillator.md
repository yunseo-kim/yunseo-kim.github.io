---
title: "Algebraic Solution of the Harmonic Oscillator"
description: >-
  We set up the Schrödinger equation for the harmonic oscillator in quantum mechanics and explore its algebraic solution method.
  We derive the wave function and energy levels of any stationary state from commutators, canonical commutation relations, and ladder operators.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder Operators]
math: true
---

## TL;DR
> - Any oscillation can be approximated as simple harmonic oscillation if the amplitude is small enough, which makes simple harmonic oscillation significant in physics
> - Harmonic oscillator: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Commutator**:
>   - A binary operation that shows how well two operators do not commute
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Canonical commutation relation**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Ladder operators**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ is called the **raising operator**, and $\hat{a}\_-$ is called the **lowering operator**
>   - Can raise or lower the energy level for any stationary state, so if one solution of the time-independent Schrödinger equation is found, all other solutions can be found
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Wave function and energy level of the $n$-th stationary state:
>   - Ground state ($0$th stationary state):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$-th stationary state:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ is the **Hermitian conjugate** and **adjoint operator** of $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - From this, the following properties can be derived:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Method for calculating the expectation value of physical quantities including powers of $\hat{x}$ and $\hat{p}$:
>   1. Express $\hat{x}$ and $\hat{p}$ in terms of raising and lowering operators using the definition of ladder operators
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. Express the physical quantity for which you want to find the expectation value using the above expressions for $\hat{x}$ and $\hat{p}$
>   3. Use the fact that $\left(\hat{a}\_\pm \right)^m$ is proportional to $\psi\_{n\pm m}$ and thus orthogonal to $\psi_n$, becoming $0$
>   4. Calculate the integral using the properties of ladder operators
{: .prompt-info }

## Prerequisites
- [Separation of Variables](https://www.yunseo.kim/posts/Separation-of-Variables/)
- [Schrödinger Equation and the Wave Function](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfest Theorem](/posts/ehrenfest-theorem/)
- [Time-Independent Schrödinger Equation](/posts/time-independent-schrodinger-equation/)
- [The Infinite Square Well](/posts/the-infinite-square-well/)
- Hermitian conjugate, adjoint operator

## Model Setup
### Harmonic Oscillator in Classical Mechanics
A typical example of a classical harmonic oscillator is the motion of a mass $m$ attached to a spring with spring constant $k$ (ignoring friction).
This motion follows **Hooke's law**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

The solution to this equation is

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

where

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

is the angular frequency of the oscillation. The potential energy as a function of position $x$ is

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

which is in the form of a parabola.

In reality, a perfect harmonic oscillator does not exist. Even in the case of the spring we just used as an example, if you pull the spring too much, it will break or undergo permanent deformation beyond its elastic limit, and in fact, it will not follow Hooke's law exactly even before reaching that point. Nevertheless, the reason why harmonic oscillators are important in physics is that any arbitrary potential can be approximated as a parabola near its local minimum. If we Taylor expand an arbitrary potential $V(x)$ near its minimum point, we get

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Now, since adding an arbitrary constant to $V(x)$ has no effect on the force, we can subtract $V(x_0)$ here, and using the fact that $V^\prime(x_0)=0$ since $x_0$ is a minimum point, and neglecting higher-order terms assuming $(x-x_0)$ is sufficiently small, we get

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

This coincides with the motion of a harmonic oscillator with an effective spring constant $k=V^{\prime\prime}(x_0)$ near the point $x_0$. In other words, if the amplitude is sufficiently small, any oscillation can be approximated as simple harmonic oscillation.

> \* Since we assumed that $V(x)$ has a minimum at $x_0$, $V^{\prime\prime}(x_0) \geq 0$ here. In very rare cases, $V^{\prime\prime}(x_0)=0$, and such motion cannot be approximated as simple harmonic oscillation.
{: .prompt-info }

### Harmonic Oscillator in Quantum Mechanics
The quantum mechanical harmonic oscillator problem is to solve the Schrödinger equation for the potential

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

The [time-independent Schrödinger equation](/posts/time-independent-schrodinger-equation/) for the harmonic oscillator is

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

There are two completely different approaches to solving this problem. One is an analytical method using **power series**, and the other is an algebraic method using **ladder operators**. The algebraic method is faster and simpler, but it's also necessary to study the analytical solution using power series. Here, we will cover the algebraic solution method, and for the analytical solution method, please refer to [this article](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Commutators and Canonical Commutation Relations
We can rewrite equation ($\ref{eqn:t_independent_schrodinger_eqn}$) using the momentum operator $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$ as follows:

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Now let's factorize the Hamiltonian

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

If $p$ and $x$ were numbers, we could simply factorize as

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

but here, $\hat{p}$ and $\hat{x}$ are operators, and the **commutative property** generally doesn't hold for operators ($\hat{p}\hat{x}\neq \hat{x}\hat{p}$), so it's not that simple. However, it can still serve as a starting point, so let's begin by examining the following quantity:

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

For the operators $\hat{a\_\pm}$ defined above, $\hat{a}\_-\hat{a}\_+$ is

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Here, the term $(\hat{x}\hat{p}-\hat{p}\hat{x})$ is called the **commutator** of $\hat{x}$ and $\hat{p}$, and it indicates how poorly the two operators commute. In general, the commutator of operators $\hat{A}$ and $\hat{B}$ is denoted using square brackets as follows:

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

Using this notation, we can rewrite equation ($\ref{eqn:a_m_times_a_p_without_commutator}$) as:

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Now we need to find the commutator of $\hat{x}$ and $\hat{p}$.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

and removing the test function $f(x)$, we get:

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

This is called the **canonical commutation relation**.

## Ladder Operators
By the canonical commutation relation, equation ($\ref{eqn:a_m_times_a_p}$) becomes

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

i.e.,

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Here, the order of $\hat{a}\_-$ and $\hat{a}\_+$ is important. If we put $\hat{a}\_+$ on the left, we get

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

and it satisfies

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

In this case, the Hamiltonian can also be written as

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Therefore, if we express the time-independent Schrödinger equation ($\hat{H}\psi=E\psi$) using $\hat{a}\_\pm$, we get

$$ \hbar\omega \left(\hat{a}\_{\pm}\hat{a}\_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(upper/lower signs together).

Now we can derive the following important property:

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Proof:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> Similarly,
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Therefore, if we can find one solution to the time-independent Schrödinger equation, we can find all other solutions. Since we can raise or lower the energy level for any stationary state, $\hat{a}\_\pm$ are called **ladder operators**, where $\hat{a}\_+$ is the **raising operator** and $\hat{a}\_-$ is the **lowering operator**.

## Stationary States of the Harmonic Oscillator
### Stationary State $\psi_n$ and Energy Level $E_n$
If we keep applying the lowering operator, we will eventually reach an energy state lower than 0, which cannot exist physically. Mathematically, if $\psi$ is a solution to the Schrödinger equation, then $\hat{a}_-\psi$ is also a solution, but there's no guarantee that this new solution is always normalized (i.e., physically possible). If we keep applying the lowering operator, we will eventually reach the trivial solution $\psi=0$.

Therefore, for a stationary state $\psi$ of the harmonic oscillator, there exists a 'lowest level' $\psi_0$ that satisfies

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

(where no lower energy level exists). This $\psi_0$ satisfies

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

therefore,

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

This is a [separable ordinary differential equation](/posts/Separation-of-Variables/), so we can easily solve it as follows:

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

Also, this function can be normalized as follows:

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Here, $A^2 = \sqrt{m\omega / \pi\hbar}$, so

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Now, if we substitute this solution into the Schrödinger equation ($\ref{eqn:schrodinger_eqn_with_ladder}$) we found earlier, and use the fact that $\hat{a}_-\psi_0=0$, we get:

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

Starting from this **ground state**, we can obtain excited states by repeatedly applying the raising operator, where the energy increases by $\hbar\omega$ each time the raising operator is applied.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

Here, $A_n$ is the normalization constant. In this way, we can determine all stationary states and allowed energy levels of the harmonic oscillator by finding the ground state and then applying the raising operator.

### Normalization
The normalization constant can also be determined algebraically. We know that $\hat{a}\_{\pm}\psi_n$ is proportional to $\psi\_{n\pm 1}$, so we can write

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Now, note that for any integrable functions $f(x)$ and $g(x)$, the following holds:

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ is the **Hermitian conjugate** and **adjoint operator** of $\hat{a}\_\pm$.

> **Proof:**
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

Therefore, if we let $f=\hat{a}_\pm \psi_n$, $g=\psi_n$, we get

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Then, from equations ($\ref{eqn:schrodinger_eqn_with_ladder}$) and ($\ref{eqn:psi_n_and_E_n}$),

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

Therefore, from equations ($\ref{eqn:norm_const}$) and ($\ref{eqn:norm_const_2}$), we get:

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

And since $\psi_n$ and $\psi_{n\pm1}$ are all normalized, $\|c_n\|^2=n+1,\ \|d_n\|^2=n$, and therefore

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

From this, we can find any normalized stationary state $\psi_n$ as follows:

$$ \psi\_n = \frac{1}{\sqrt{n!}}\left(\hat{a}\_+ \right)^n \psi\_0. \tag{27}$$

In other words, in equation ($\ref{eqn:psi_n_and_E_n}$), the normalization constant $A_n=\cfrac{1}{\sqrt{n!}}$.

### Orthogonality of Stationary States
As in [The Infinite Square Well](/posts/the-infinite-square-well/#3-these-states-possess-orthogonality), the stationary states of the harmonic oscillator are orthogonal.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Proof
We can prove this using equations ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$), and ($\ref{eqn:norm_const_3}$) that we showed earlier. In equation ($\ref{eqn:hermitian_conjugate}$), let $f=\hat{a}_-\psi_m,\ g=\psi_n$, and use the fact that

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

Using orthogonality, as we did in [equation (19) of The Infinite Square Well](/posts/the-infinite-square-well/#finding-the-general-solution-psixt-of-the-time-dependent-schrödinger-equation), when expanding $\Psi(x,0)$ as a linear combination of stationary states $\sum c_n\psi_n(x)$, we can find the coefficient $c_n$ using the [Fourier method](/posts/the-infinite-square-well/#finding-coefficients-c_n-using-fouriers-trick).

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Here too, $\|c_n\|^2$ is the probability of obtaining the value $E_n$ when measuring energy.

## Expectation Value of Potential Energy $\langle V \rangle$ in Any Stationary State $\psi_n$
To find $\langle V \rangle$, we need to calculate the following integral:

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

When calculating integrals of this form that include powers of $\hat{x}$ and $\hat{p}$, the following method is useful.

First, use the definition of ladder operators in equation ($\ref{eqn:ladder_operators}$) to express $\hat{x}$ and $\hat{p}$ in terms of raising and lowering operators.

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Now express the physical quantity for which you want to calculate the expectation value using the above expressions for $\hat{x}$ and $\hat{p}$. Here, we're interested in $x^2$, so we can express it as:

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

From this, we get:

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

And here, since $\left(\hat{a}\_\pm \right)^2$ is proportional to $\psi\_{n\pm2}$, it's orthogonal to $\psi\_n$, so these two terms $\left(\hat{a}\_+ \right)^2$ and $\left(\hat{a}\_- \right)^2$ become 0. Finally, using equation ($\ref{eqn:norm_const_2}$) to calculate the remaining two terms:

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

Referring to equation ($\ref{eqn:psi_n_and_E_n}$), we can see that the expectation value of potential energy is exactly half of the total energy, and naturally, the other half is kinetic energy $T$. This is a characteristic property of the harmonic oscillator.
