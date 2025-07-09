---
title: "Homogeneous Linear ODEs of Second Order with Constant Coefficients"
description: "Explore how the general solution of a second-order homogeneous linear ODE with constant coefficients changes based on the roots of its characteristic equation."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Second-order homogeneous linear ODE with constant coefficients: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **Characteristic equation**: $\lambda^2 + a\lambda + b = 0$
> - Depending on the sign of the discriminant $a^2 - 4b$ of the characteristic equation, the form of the general solution can be divided into three cases as shown in the table:
>
> | Case | Roots of Characteristic Equation | Basis of the ODE's Solution | General Solution of the ODE |
> | :---: | :---: | :---: | :---: |
> | I | Distinct real roots<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | Real double root<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | Complex conjugate roots<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [Bernoulli Equation](/posts/Bernoulli-Equation/)
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- Euler's formula

## Characteristic Equation
Let's consider a second-order homogeneous linear ordinary differential equation with constant coefficients $a$ and $b$:

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

This type of equation has important applications in mechanical and electrical vibrations.

We have previously found the general solution of the logistic equation in [Bernoulli Equation](/posts/Bernoulli-Equation/), and according to it, the solution to the first-order linear ODE with a constant coefficient $k$,

$$ y^\prime + ky = 0 $$

is the exponential function $y = ce^{-kx}$ (the case where $A=-k$ and $B=0$ in equation (4) of that post).

Therefore, for a similarly shaped equation like ($\ref{eqn:ode_with_constant_coefficients}$), we can first try a solution of the form

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

> Of course, this is merely a guess, and there is no guarantee that the general solution will actually have this form. However, if we can find any two linearly independent solutions, we can obtain the general solution by the [superposition principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle), as we saw in [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/#basis-and-general-solution).  
> As we will see shortly, [there are also cases where we need to find a different form of solution](#ii-real-double-root-lambda---cfraca2).
{: .prompt-info }

Substituting Eq. ($\ref{eqn:general_sol}$) and its derivatives

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

into Eq. ($\ref{eqn:ode_with_constant_coefficients}$) gives

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

Therefore, if $\lambda$ is a root of the **characteristic equation**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

then the exponential function ($\ref{eqn:general_sol}$) is a solution to the ordinary differential equation ($\ref{eqn:ode_with_constant_coefficients}$). Solving the quadratic equation ($\ref{eqn:characteristic_eqn}$) gives

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

and from this, the two functions

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

become solutions to equation ($\ref{eqn:ode_with_constant_coefficients}$).

> The terms **characteristic equation** and **auxiliary equation** are often used interchangeably; they mean exactly the same thing. You can use either term.
{: .prompt-tip }

Now, we can divide the problem into three cases depending on the sign of the discriminant $a^2 - 4b$ of the characteristic equation ($\ref{eqn:characteristic_eqn}$).
- $a^2 - 4b > 0$: Distinct real roots
- $a^2 - 4b = 0$: Real double root
- $a^2 - 4b < 0$: Complex conjugate roots

## Form of the General Solution based on the Sign of the Discriminant
### I. Distinct Real Roots $\lambda_1$ and $\lambda_2$
In this case, a basis of solutions for equation ($\ref{eqn:ode_with_constant_coefficients}$) on any interval is

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

and the corresponding general solution is

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. Real Double Root $\lambda = -\cfrac{a}{2}$
If $a^2 - 4b = 0$, the quadratic equation ($\ref{eqn:characteristic_eqn}$) yields only one root $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$. Therefore, the only solution of the form $y = e^{\lambda x}$ we can obtain is

$$ y_1 = e^{-(a/2)x} $$

To obtain a basis, we need to find a second solution $y_2$ that is linearly independent of $y_1$.

In this situation, we can use [reduction of order](/posts/homogeneous-linear-odes-of-second-order/#reduction-of-order), which we have discussed before. We set the second solution we are looking for as $y_2=uy_1$, and substitute

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

into equation ($\ref{eqn:ode_with_constant_coefficients}$) to get

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

Grouping the terms by $u^{\prime\prime}$, $u^\prime$, and $u$ gives

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

Here, since $y_1$ is a solution to equation ($\ref{eqn:ode_with_constant_coefficients}$), the expression in the last parenthesis is $0$. Also, since

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

the expression in the first parenthesis is also $0$. Thus, only $u^{\prime\prime}y_1 = 0$ remains, which implies $u^{\prime\prime}=0$. Integrating twice gives $u = c_1x + c_2$. Since the integration constants $c_1$ and $c_2$ can be any value, we can simply choose $c_1=1$ and $c_2=0$ to set $u=x$. Then we have $y_2 = uy_1 = xy_1$. Since $y_1$ and $y_2$ are linearly independent, they form a basis. Therefore, when the characteristic equation ($\ref{eqn:characteristic_eqn}$) has a double root, a basis of solutions for equation ($\ref{eqn:ode_with_constant_coefficients}$) on any interval is

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

and the corresponding general solution is

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. Complex Conjugate Roots $-\cfrac{1}{2}a + i\omega$ and $-\cfrac{1}{2}a - i\omega$
In this case, $a^2 - 4b < 0$, and since $\sqrt{-1} = i$, from Eq. ($\ref{eqn:lambdas}$) we have

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

Here, let's define the real number $\omega = \sqrt{b-\cfrac{1}{4}a^2}$.

With $\omega$ defined as above, the roots of the characteristic equation ($\ref{eqn:characteristic_eqn}$) are the complex conjugate roots $\lambda = -\cfrac{1}{2}a \pm i\omega$. The corresponding two complex solutions to equation ($\ref{eqn:ode_with_constant_coefficients}$) are

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

However, in this case, we can obtain a basis of real solutions as follows.

From Euler's formula

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

and by substituting $-t$ for $t$ in the above equation to get

$$ e^{-it} = \cos t - i\sin t $$

we can add and subtract these two equations to obtain:

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

The complex exponential function $e^z$ of a complex variable $z = r + it$ with real part $r$ and imaginary part $it$ can be defined using the real functions $e^r$, $\cos t$, and $\sin t$ as follows.

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

Here, setting $r=-\cfrac{1}{2}ax$ and $t=\omega x$, we can write:

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

By the [superposition principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle), the sum and constant multiples of these complex solutions are also solutions. Therefore, by adding the two equations side by side and multiplying both sides by $\cfrac{1}{2}$, we can obtain the first real solution $y_1$ as follows.

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

Similarly, by subtracting the second equation from the first and multiplying both sides by $\cfrac{1}{2i}$, we can obtain the second real solution $y_2$.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

Since $\cfrac{y_1}{y_2} = \cot{\omega x}$ is not a constant, $y_1$ and $y_2$ are linearly independent on any interval and thus form a basis of real solutions for equation ($\ref{eqn:ode_with_constant_coefficients}$). From this, we obtain the general solution

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(where }A,\, B\text{ are arbitrary constants)} \label{eqn:general_sol_3}\tag{13}$$
