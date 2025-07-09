---
title: "Euler-Cauchy Equation"
description: "Explore the different forms of the general solution to the Euler-Cauchy equation based on the sign of the discriminant of its auxiliary equation."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Euler-Cauchy equation: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Auxiliary equation**: $m^2 + (a-1)m + b = 0$
> - The form of the general solution can be divided into three cases, as shown in the table, depending on the sign of the discriminant $(1-a)^2 - 4b$ of the auxiliary equation.
>
> | Case | Roots of Auxiliary Equation | Basis of Solutions for Euler-Cauchy Equation | General Solution of Euler-Cauchy Equation |
> | :---: | :---: | :---: | :---: |
> | I | Distinct real roots<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Real double root<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Complex conjugate roots<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerequisites
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogeneous Linear ODEs with Constant Coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Euler's Formula

## Auxiliary Equation
The **Euler-Cauchy equation** is an ordinary differential equation of the form

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

with given constants $a$ and $b$, and an unknown function $y(x)$. Substituting

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

into Eq. ($\ref{eqn:euler_cauchy_eqn}$) gives

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

which simplifies to

$$ [m(m-1) + am + b]x^m = 0 $$

From this, we obtain the auxiliary equation

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

and the necessary and sufficient condition for $y=x^m$ to be a solution of the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$) is that $m$ is a root of the auxiliary equation ($\ref{eqn:auxiliary_eqn}$).

Solving the quadratic equation ($\ref{eqn:auxiliary_eqn}$) gives the roots

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

and from this, the two functions

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

are solutions to equation ($\ref{eqn:euler_cauchy_eqn}$).

As with [Homogeneous Linear ODEs with Constant Coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/), we can divide this into three cases based on the sign of the discriminant $(1-a)^2 - 4b$ of the auxiliary equation ($\ref{eqn:auxiliary_eqn}$).
- $(1-a)^2 - 4b > 0$: Distinct real roots
- $(1-a)^2 - 4b = 0$: Real double root
- $(1-a)^2 - 4b < 0$: Complex conjugate roots

## Forms of the General Solution Based on the Sign of the Discriminant
### I. Distinct Real Roots $m_1$ and $m_2$
In this case, a basis of solutions for equation ($\ref{eqn:euler_cauchy_eqn}$) on any interval is

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

and the corresponding general solution is

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Real Double Root $m = \cfrac{1-a}{2}$
When $(1-a)^2 - 4b = 0$, i.e., $b=\cfrac{(1-a)^2}{4}$, the quadratic equation ($\ref{eqn:auxiliary_eqn}$) has only one root $m = m_1 = m_2 = \cfrac{1-a}{2}$. Therefore, the one solution of the form $y = x^m$ we can obtain is

$$ y_1 = x^{(1-a)/2} $$

and the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$) takes the form

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

Now, let's find another linearly independent solution $y_2$ using [reduction of order](/posts/homogeneous-linear-odes-of-second-order/#reduction-of-order).

If we set the second solution we are looking for as $y_2=uy_1$, we get

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Since $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

and integrating gives $u = \ln x$.

Therefore, $y_2 = uy_1 = y_1 \ln x$, and since their quotient is not a constant, $y_1$ and $y_2$ are linearly independent. The general solution corresponding to the basis $y_1$ and $y_2$ is

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Complex Conjugate Roots
In this case, the roots of the auxiliary equation ($\ref{eqn:auxiliary_eqn}$) are $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, and the corresponding two complex solutions of the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$) can be written as follows, using the fact that $x=e^{\ln x}$.

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

By setting $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ and using Euler's formula $e^{it} = \cos{t} + i\sin{t}$, we can see that

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

and from this, we obtain the following two real solutions

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Since their quotient $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ is not a constant, the two solutions above are linearly independent and thus form a basis for the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$) by the [superposition principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle). From this, we obtain the following real general solution.

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

However, the case where the auxiliary equation of an Euler-Cauchy equation has complex conjugate roots is not of great practical importance.

## Transformation to a Homogeneous Linear ODE with Constant Coefficients
The Euler-Cauchy equation can be transformed into a [homogeneous linear ODE with constant coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/) through a change of variables.

By substituting $x = e^t$, we get

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

and the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$) is transformed into the following homogeneous linear ODE with constant coefficients in terms of $t$.

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

If we solve equation ($\ref{eqn:substituted}$) for $t$ by applying the solution method for [homogeneous linear ODEs with constant coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/), and then transform the resulting solution back into a solution in terms of $x$ using $t = \ln{x}$, we obtain [the same results as seen before](#forms-of-the-general-solution-based-on-the-sign-of-the-discriminant).
