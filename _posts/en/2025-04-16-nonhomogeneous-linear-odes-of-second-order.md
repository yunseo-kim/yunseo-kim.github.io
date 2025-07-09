---
title: "Nonhomogeneous Linear ODEs of Second Order"
description: "Explore the structure of the general solution for second-order nonhomogeneous linear ODEs in relation to their homogeneous counterparts. This post proves the existence of a general solution and the non-existence of singular solutions."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **General solution** of a second-order nonhomogeneous linear ODE $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: The general solution of the homogeneous ODE $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, which is $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: A particular solution of the given nonhomogeneous ODE
> - The response term $y_p$ is determined solely by the input $r(x)$. For the same nonhomogeneous ODE, $y_p$ does not change even if the initial conditions change. The difference between two particular solutions of a nonhomogeneous ODE is a solution of the corresponding homogeneous ODE.
> - **Existence of a general solution**: If the coefficients $p(x)$, $q(x)$, and the input function $r(x)$ of a nonhomogeneous ODE are continuous, a general solution always exists.
> - **Non-existence of singular solutions**: The general solution includes all solutions of the equation (i.e., no singular solutions exist).
{: .prompt-info }

## Prerequisites
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [The Wronskian, Existence and Uniqueness of Solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## General and Particular Solutions of Second-Order Nonhomogeneous Linear ODEs
Consider the second-order nonhomogeneous linear ordinary differential equation

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

where $r(x) \not\equiv 0$. The **general solution** of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on an open interval $I$ is the sum of the general solution $y_h = c_1y_1 + c_2y_2$ of the corresponding homogeneous ODE

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

and a particular solution $y_p$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$), in the form

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Furthermore, a **particular solution** of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on the interval $I$ is a solution obtained from equation ($\ref{eqn:general_sol}$) by assigning specific values to the arbitrary constants $c_1$ and $c_2$ in $y_h$.

In other words, adding an input $r(x)$, which depends only on the independent variable $x$, to the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) adds a corresponding term $y_p$ to the response. This added response term $y_p$ is determined solely by the input $r(x)$, regardless of the initial conditions. As we will see later, if we take the difference between any two solutions $y_1$ and $y_2$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) (i.e., the difference between particular solutions for two different sets of initial conditions), the term $y_p$, which is independent of the initial conditions, cancels out, leaving only the difference between ${y_h}_1$ and ${y_h}_2$. By the [Superposition Principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle), this difference is a solution of equation ($\ref{eqn:homogeneous_linear_ode}$).

## Relationship Between Solutions of Nonhomogeneous and Corresponding Homogeneous ODEs
> **Theorem 1: Relationship Between Solutions of Nonhomogeneous ODE ($\ref{eqn:nonhomogeneous_linear_ode}$) and Homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$)**  
> **(a)** The sum of a solution $y$ of the nonhomogeneous ODE ($\ref{eqn:nonhomogeneous_linear_ode}$) and a solution $\tilde{y}$ of the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) on some open interval $I$ is a solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on $I$. In particular, equation ($\ref{eqn:general_sol}$) is a solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on $I$.  
> **(b)** The difference between two solutions of the nonhomogeneous ODE ($\ref{eqn:nonhomogeneous_linear_ode}$) on an interval $I$ is a solution of the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) on $I$.
{: .prompt-info }

### Proof
#### (a)
Let's denote the left-hand side of equations ($\ref{eqn:nonhomogeneous_linear_ode}$) and ($\ref{eqn:homogeneous_linear_ode}$) as $L[y]$. Then, for any solution $y$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) and any solution $\tilde{y}$ of equation ($\ref{eqn:homogeneous_linear_ode}$) on interval $I$, the following holds:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
For any two solutions $y$ and $y^\*$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$, the following holds:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## The General Solution of a Nonhomogeneous ODE Includes All Solutions
For a homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$), [we know that the general solution includes all solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/#the-general-solution-includes-all-solutions). Let's show that the same holds for the nonhomogeneous ODE ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Theorem 2: The General Solution of a Nonhomogeneous ODE Includes All Solutions**  
> If the coefficients $p(x)$, $q(x)$, and the input function $r(x)$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) are continuous on some open interval $I$, then every solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on $I$ can be obtained from the general solution ($\ref{eqn:general_sol}$) of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on $I$ by assigning suitable values to the arbitrary constants $c_1$ and $c_2$ in $y_h$.
{: .prompt-info }

### Proof
Let $y^\*$ be any solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on $I$, and let $x_0$ be any $x$ in the interval $I$. By the [theorem on the Existence of a General Solution for homogeneous ODEs with continuous variable coefficients](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-of-a-general-solution), $y_h = c_1y_1 + c_2y_2$ exists. Also, by the **method of variation of parameters**, which we will discuss later, $y_p$ also exists. Therefore, the general solution ($\ref{eqn:general_sol}$) of the nonhomogeneous ODE ($\ref{eqn:nonhomogeneous_linear_ode}$) exists on the interval $I$. Now, by Theorem [1(b)](#relationship-between-solutions-of-nonhomogeneous-and-corresponding-homogeneous-odes) which we proved earlier, $Y = y^\* - y_p$ is a solution of the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) on interval $I$, and at $x_0$,

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

According to the [Existence and Uniqueness Theorem for Initial Value Problems](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-and-uniqueness-theorem-for-initial-value-problems), for the initial conditions above, there exists a unique particular solution $Y$ of the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) on interval $I$, which can be obtained by assigning suitable values to $c_1$ and $c_2$ in $y_h$. Since $y^\* = Y + y_p$, we have shown that any particular solution $y^\*$ of the nonhomogeneous ODE ($\ref{eqn:nonhomogeneous_linear_ode}$) can be obtained from the general solution ($\ref{eqn:general_sol}$). $\blacksquare$
