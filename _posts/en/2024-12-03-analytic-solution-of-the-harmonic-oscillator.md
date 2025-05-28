---
title: Analytical Solution of the Harmonic Oscillator
description: We set up the Schrödinger equation for the harmonic oscillator in quantum
  mechanics and explore its analytical solution method. We solve the equation by introducing
  the dimensionless variable 𝜉, and express any normalized stationary state using
  Hermite polynomials.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hermite Polynomials]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Any oscillation can be approximated as simple harmonic oscillation if the amplitude is sufficiently small, making simple harmonic oscillation significant in physics
> - Harmonic oscillator: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - Introduce dimensionless variable $\xi$ and energy $K$ expressed in units of $\cfrac{1}{2}\hbar\omega$:
>   - $\xi \equiv \sqrt{\cfrac{m\omega}{\hbar}}x$
>   - $K \equiv \cfrac{2E}{\hbar\omega}$
>   - $ \cfrac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi $
> - As $\|\xi\|^2 \to \infty$, the physically allowed asymptotic solution is $\psi(\xi) \to Ae^{-\xi^2/2}$, therefore,
>
> $$ \begin{gather*}
> \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(where }\lim_{\xi\to\infty}h(\xi)=A\text{)}, \\
> \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0
> \end{gather*} $$
>
> - Expressing the solution to the above equation in series form $ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j$,
>
> $$ a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j $$
>
> - For this solution to be normalizable, the series $\sum a_j$ must be finite, meaning there must exist a 'largest' $j$ value $n\in \mathbb{N}$ such that $a_j=0$ for $j>n$, thus
>   - $ K = 2n + 1 $
>   - $ E_n = \left(n+\cfrac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots $
> - Generally, $h_n(\xi)$ is an $n$-th degree polynomial in $\xi$, and the remainder excluding the leading coefficient ($a_0$ or $a_1$) is called the **Hermite polynomial** $H_n(\xi)$
>
> $$ h_n(\xi) = 
> \begin{cases}
> a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
> a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
> \end{cases} $$
>
> - Normalized stationary states of the harmonic oscillator:
>
> $$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2} $$
>
> - Characteristics of the quantum oscillator
>   - Even and odd eigenfunctions alternate
>   - Non-zero probability of finding the particle in classically forbidden regions (where $x$ is greater than the classical amplitude for a given $E$)
>   - Zero probability of finding the particle at the center for all odd $n$ stationary states
>   - As $n$ increases, it becomes more similar to a classical oscillator
{: .prompt-info }

## Prerequisites
- [Separation of Variables](https://www.yunseo.kim/posts/Separation-of-Variables/)
- [Schrödinger Equation and the Wave Function](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfest Theorem](/posts/ehrenfest-theorem/)
- [Time-Independent Schrödinger Equation](/posts/time-independent-schrodinger-equation/)
- [The Infinite Square Well](/posts/the-infinite-square-well/)
- [Algebraic Solution of the Harmonic Oscillator](/posts/algebraic-solution-of-the-harmonic-oscillator/)

## Model Setup
For the description of the harmonic oscillator in classical mechanics and the importance of the harmonic oscillator problem, refer to the [previous post](/posts/algebraic-solution-of-the-harmonic-oscillator/).

### Harmonic Oscillator in Quantum Mechanics
The quantum mechanical harmonic oscillator problem involves solving the Schrödinger equation for the potential

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{1}$$

The [time-independent Schrödinger equation](/posts/time-independent-schrodinger-equation/) for the harmonic oscillator is

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

There are two completely different approaches to solving this problem. One is the analytical method using **power series**, and the other is the algebraic method using **ladder operators**. While the algebraic method is faster and simpler, it's also necessary to study the analytical solution using power series. [We have previously covered the algebraic solution method](/posts/algebraic-solution-of-the-harmonic-oscillator/), and here we will discuss the analytical solution method.

## Transformation of the Schrödinger Equation
By introducing the dimensionless variable

$$ \xi \equiv \sqrt{\frac{m\omega}{\hbar}}x \label{eqn:xi}\tag{3}$$

we can simplify the time-independent Schrödinger equation ($\ref{eqn:t_independent_schrodinger_eqn}$) as follows:

$$ \frac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi. \label{eqn:schrodinger_eqn_with_xi}\tag{4}$$

Here, $K$ is the energy expressed in units of $\cfrac{1}{2}\hbar\omega$.

$$ K \equiv \frac{2E}{\hbar\omega}. \label{eqn:K}\tag{5}$$

Now we need to solve this rewritten equation ($\ref{eqn:schrodinger_eqn_with_xi}$). First, for very large $\xi$ (i.e., for very large $x$), $\xi^2 \gg K$, so

$$ \frac{d^2\psi}{d\xi^2} \approx \xi^2\psi \label{eqn:schrodinger_eqn_approx}\tag{6}$$

and an approximate solution to this is

$$ \psi(\xi) \approx Ae^{-\xi^2/2} + Be^{\xi^2/2} \label{eqn:psi_approx}\tag{7}$$

However, the $B$ term here diverges as $\|x\|\to \infty$ and cannot be normalized, so the physically allowed asymptotic solution is

$$ \psi(\xi) \to Ae^{-\xi^2/2} \label{eqn:psi_asymp}\tag{8}$$

Now, let's separate the exponential part and write

$$ \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(where }\lim_{\xi\to\infty}h(\xi)=A\text{)} \label{eqn:psi_and_h}\tag{9}$$

> We used an approximation method in the derivation process to find the form of the asymptotic solution to determine the exponential term $e^{-\xi^2/2}$, but the equation ($\ref{eqn:psi_and_h}$) obtained through this is not an approximate equation but an exact one. Separating the asymptotic form in this way is a standard first step when solving differential equations in power series form.
{: .prompt-info }

Differentiating equation ($\ref{eqn:psi_and_h}$) to find $\cfrac{d\psi}{d\xi}$ and $\cfrac{d^2\psi}{d\xi^2}$, we get

$$ \begin{gather*}
\frac{d\psi}{d\xi} = \left(\frac{dh}{d\xi}-\xi h \right)e^{-\xi^2/2}, \\
\frac{d^2\psi}{d\xi^2} = \left(\frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(\xi^2-1)h \right)e^{-\xi^2/2}
\end{gather*} $$

so the Schrödinger equation ($\ref{eqn:schrodinger_eqn_with_xi}$) now becomes

$$ \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0 \label{eqn:schrodinger_eqn_with_h}\tag{10}$$

## Power Series Expansion
By Taylor's theorem, any smoothly varying function can be expressed as a power series, so let's try to find the solution to equation ($\ref{eqn:schrodinger_eqn_with_h}$) in the form of a series in $\xi$:

$$ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j \label{eqn:h_series_exp}\tag{11}$$

Differentiating each term of this series gives us the following two equations:

$$ \begin{gather*}
\frac{dh}{d\xi} = a_1 + 2a_2\xi + 3a_3\xi^2 + \cdots = \sum_{j=0}^{\infty}ja_j\xi^{j-1}, \\
\frac{d^2 h}{d\xi^2} = 2a_2 + 2\cdot3a_3\xi + 3\cdot4a_4\xi^2 + \cdots = \sum_{j=0}^{\infty} (j+1)(j+2)a_{j+2}\xi^j.
\end{gather*} $$

Substituting these two equations back into the Schrödinger equation (equation [$\ref{eqn:schrodinger_eqn_with_h}$]), we get:

$$ \sum_{j=0}^{\infty}[(j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j]\xi^j = 0. \label{eqn:schrodinger_eqn_power_series}\tag{12}$$

By the uniqueness of power series expansion, the coefficient for each power of $\xi$ must be zero, so

$$ (j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j = 0 $$

$$ \therefore a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j. \label{eqn:recursion_formula}\tag{13}$$

This **recursion formula** is equivalent to the Schrödinger equation. Given two arbitrary constants $a_0$ and $a_1$, we can find the coefficients of all terms in the solution $h(\xi)$.

However, the solution obtained in this way cannot always be normalized. If the series $\sum a_j$ is an infinite series (if $\lim_{j\to\infty} a_j\neq0$), for very large $j$, the above recursion formula approximately becomes

$$ a_{j+2} \approx \frac{2}{j}a_j $$

and an approximate solution to this is

$$ a_j \approx \frac{C}{(j/2)!} \quad \text{(}C\text{ is an arbitrary constant)}$$

In this case, for large $\xi$ values where higher-order terms become dominant,

$$ h(\xi) \approx C\sum\frac{1}{(j/2)!}\xi^j \approx C\sum\frac{1}{j!}\xi^{2j} \approx Ce^{\xi^2} $$

and if $h(\xi)$ takes this $Ce^{\xi^2}$ form, $\psi(\xi)$ in equation ($\ref{eqn:psi_and_h}$) becomes $Ce^{\xi^2/2}$, which diverges as $\xi \to \infty$. This corresponds to the non-normalizable solution with $A=0, B\neq0$ in equation ($\ref{eqn:psi_approx}$).

Therefore, the series $\sum a_j$ must be finite. There must exist a 'largest' $j$ value $n\in \mathbb{N}$ such that $a_j=0$ for $j>n$, and for this to happen, $a_{n+2}=0$ must hold for non-zero $a_n$, so from equation ($\ref{eqn:recursion_formula}$)

$$ K = 2n + 1 $$

Substituting this into equation ($\ref{eqn:K}$), we obtain the physically allowed energies

$$ E_n = \left(n+\frac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots \label{eqn:E_n}\tag{14}$$

Thus, we have obtained the energy quantization condition identical to equation (21) in the [algebraic solution of the harmonic oscillator](/posts/algebraic-solution-of-the-harmonic-oscillator/#stationary-state-psi_n-and-energy-level-e_n) using a completely different method.

## Hermite Polynomials $H_n(\xi)$ and Stationary States $\psi_n(x)$
### Hermite Polynomials $H_n$
In general, $h_n(\xi)$ is an $n$-th degree polynomial in $\xi$, and it contains only even powers if $n$ is even, and only odd powers if $n$ is odd. The remainder, excluding the leading coefficient ($a_0$ or $a_1$), is called the **Hermite polynomial** $H_n(\xi)$.

$$ h_n(\xi) = 
\begin{cases}
a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
\end{cases} $$

Traditionally, the coefficient of the highest degree term in $H_n$ is arbitrarily set to be $2^n$.

Here are the first few Hermite polynomials:

$$ \begin{align*}
H_0 &= 1 \\
H_1 &= 2\xi \\
H_2 &= 4\xi^2 - 2 \\
H_3 &= 8\xi^3 - 12\xi \\
H_4 &= 16\xi^4 - 48\xi^2 + 12 \\
H_5 &= 32\xi^5 - 160\xi^3 + 120\xi \\
&\qquad\vdots
\end{align*} $$

### Stationary States $\psi_n(x)$
The normalized stationary states for the harmonic oscillator are as follows:

$$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2}. $$

This is consistent with the result (equation [27]) obtained in the [algebraic solution of the harmonic oscillator](/posts/algebraic-solution-of-the-harmonic-oscillator/#normalization).

The following image shows the stationary states $\psi_n(x)$ and probability densities $\|\psi_n(x)\|^2$ for the first 8 $n$ values. You can see that even and odd functions alternate as eigenfunctions of the quantum oscillator.

![Wavefunction representations for the first eight bound eigenstates, n = 0 to 7. The horizontal axis shows the position x.](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)
> *Image source*
> - Author: Wikimedia user [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)

![Corresponding probability densities.](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)
> *Image source*
> - Author: Wikimedia user [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - License: Public Domain

The quantum oscillator is quite different from its classical counterpart, not only in that the energy is quantized, but also in that the probability distribution of position $x$ shows peculiar characteristics.
- There is a non-zero probability of finding the particle in regions that are classically forbidden (where $x$ is greater than the classical amplitude for a given $E$)
- For all odd $n$ stationary states, the probability of finding the particle at the center is zero

As $n$ increases, the quantum oscillator becomes more similar to a classical oscillator. The image below shows the classical probability distribution of position $x$ (dashed line) and the quantum state $\|\psi_{30}\|^2$ (solid line) for $n=30$. If you smooth out the bumpy parts, the two graphs roughly coincide.

![Quantum (solid) and classical (dashed) probability distributions of the n = 30 excited state of the quantum harmonic oscillator. The vertical dashed lines represent the classical turning points.](https://upload.wikimedia.org/wikipedia/commons/6/69/QHOn30pdf.svg)
> *Image source*
> - Author: Wikimedia user [AkanoToE](https://commons.wikimedia.org/wiki/User:AkanoToE)
> - License: Public Domain

### Interactive Visualization of Quantum Oscillator Probability Distributions
The following is a responsive visualization based on Plotly.js that I created myself. You can adjust the $n$ value using the slider to check the classical probability distribution and the shape of $\|\psi_n\|^2$ with respect to position $x$.

<div class="plotly-iframe-container" style="position: relative; padding-bottom: 110%; overflow: hidden;">
    <iframe id="plotly-iframe"
            src="/physics-visualizations/quantum-harmonic-oscillator.html"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 120%; border: none;" 
            allow="fullscreen">
    </iframe>
</div>

> - Original visualization page: <{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html>
> - Source code: [yunseo-kim/physics-visualizations repository](https://github.com/yunseo-kim/physics-visualizations/blob/main/quantum-harmonic-oscillator.html)
> - License: [See here](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

Also, if you can use Python on your computer and have the Numpy, Plotly, and Dash libraries installed, you can run the [`/src/quantum_oscillator.py`{: .filepath}](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/quantum_oscillator.py) Python script in the same repository to see the results.
