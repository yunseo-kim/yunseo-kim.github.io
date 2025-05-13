---
title: Euler-Cauchy Equation
description: Examine how the general solution of the Euler-Cauchy equation takes different forms depending on the sign of the discriminant of the auxiliary equation.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Euler-Cauchy equation: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **Auxiliary equation**: $m^2 + (a-1)m + b = 0$
> - The general solution takes different forms depending on the sign of the discriminant $(1-a)^2 - 4b$ of the auxiliary equation, as shown in the table
>
> | Case | Roots of auxiliary equation | Basis for Euler-Cauchy equation | General solution |
> | :---: | :---: | :---: | :---: |
> | I | Distinct real roots<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | Real double root<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | Complex conjugate roots<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerequisites
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogeneous Linear ODEs with Constant Coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- Euler's formula

## Auxiliary Equation
The **Euler-Cauchy equation** is a differential equation with constants $a$ and $b$ and unknown function $y(x)$ in the form:

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0. \label{eqn:euler_cauchy_eqn}\tag{1} $$

Substituting 

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

into equation ($\ref{eqn:euler_cauchy_eqn}$), we get

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

which simplifies to

$$ [m(m-1) + am + b]x^m = 0 $$

This gives us the auxiliary equation

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

For $y=x^m$ to be a solution of the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$), $m$ must be a root of the auxiliary equation ($\ref{eqn:auxiliary_eqn}$).

The roots of this quadratic equation are

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

Thus, the functions

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

are solutions to equation ($\ref{eqn:euler_cauchy_eqn}$).

As with [homogeneous linear ODEs with constant coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/), we can classify the solutions into three cases based on the discriminant $(1-a)^2 - 4b$ of the auxiliary equation ($\ref{eqn:auxiliary_eqn}$):
- $(1-a)^2 - 4b > 0$: Two distinct real roots
- $(1-a)^2 - 4b = 0$: One real double root
- $(1-a)^2 - 4b < 0$: Complex conjugate roots

## General Solutions Based on the Discriminant
### I. Two Distinct Real Roots $m_1$ and $m_2$
In this case, the basis for equation ($\ref{eqn:euler_cauchy_eqn}$) is

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

and the general solution is

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. Real Double Root $m = \cfrac{1-a}{2}$
When $(1-a)^2 - 4b = 0$, i.e., $b=\cfrac{(1-a)^2}{4}$, the auxiliary equation ($\ref{eqn:auxiliary_eqn}$) has a single root $m = m_1 = m_2 = \cfrac{1-a}{2}$. This gives us one solution

$$ y_1 = x^{(1-a)/2} $$

and the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$) becomes

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

To find another linearly independent solution, we use the [reduction of order](/posts/homogeneous-linear-odes-of-second-order/#reduction-of-order) method.

Setting $y_2=uy_1$, we get

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

Since $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

Integrating, we get $u = \ln x$.

Therefore, $y_2 = uy_1 = y_1 \ln x$, and since the ratio $\frac{y_2}{y_1} = \ln x$ is not constant, $y_1$ and $y_2$ are linearly independent. The general solution is

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. Complex Conjugate Roots
In this case, the roots of the auxiliary equation ($\ref{eqn:auxiliary_eqn}$) are $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$, and the corresponding complex solutions to equation ($\ref{eqn:euler_cauchy_eqn}$) can be written as follows, using $x=e^{\ln x}$:

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

Setting $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ and using Euler's formula $e^{it} = \cos{t} + i\sin{t}$, we get

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

From these, we can derive two real solutions:

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

Since their ratio $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ is not constant, these solutions are linearly independent and form a basis. By the [superposition principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle), the general solution is:

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

Note that the case of complex conjugate roots in Euler-Cauchy equations is of less practical importance.

## Transformation to Homogeneous Linear ODEs with Constant Coefficients
The Euler-Cauchy equation can be transformed into a homogeneous linear ODE with constant coefficients through a change of variables.

With the substitution $x = e^t$, we have:

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

This transforms the Euler-Cauchy equation ($\ref{eqn:euler_cauchy_eqn}$) into:

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

We can solve equation ($\ref{eqn:substituted}$) using methods for [homogeneous linear ODEs with constant coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/), and then substitute $t = \ln{x}$ to obtain the solution in terms of $x$. This approach yields the same results as [discussed above](#general-solutions-based-on-the-discriminant).
