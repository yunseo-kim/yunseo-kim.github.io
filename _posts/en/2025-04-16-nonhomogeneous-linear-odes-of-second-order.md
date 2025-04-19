---
title: Nonhomogeneous Linear ODEs of Second Order
description: Understanding the general solution of second-order nonhomogeneous linear differential equations, including the relationship between homogeneous and nonhomogeneous solutions, existence theorems, and the absence of singular solutions.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - The **general solution** of a second-order nonhomogeneous linear differential equation $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: general solution of the homogeneous equation $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, where $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: particular solution of the nonhomogeneous equation
> - The response term $y_p$ is determined solely by the input $r(x)$, and remains unchanged for the same nonhomogeneous equation regardless of initial conditions. The difference between two particular solutions of a nonhomogeneous equation is a solution of the corresponding homogeneous equation.
> - **Existence of general solution**: A general solution always exists when the coefficients $p(x)$, $q(x)$ and the input function $r(x)$ are continuous
> - **Non-existence of singular solutions**: The general solution includes all solutions of the equation (i.e., singular solutions do not exist)
{: .prompt-info }

## Prerequisites
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskian, Existence and Uniqueness of Solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## General Solution and Particular Solution of Second-Order Nonhomogeneous Linear Differential Equations
Consider the second-order nonhomogeneous linear differential equation

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

where $r(x) \not\equiv 0$. The **general solution** of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on an open interval $I$ is the sum of the general solution $y_h = c_1y_1 + c_2y_2$ of the corresponding homogeneous differential equation

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

and a particular solution $y_p$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$):

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

A **particular solution** of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$ is obtained by assigning specific values to the arbitrary constants $c_1$ and $c_2$ in $y_h$ in equation ($\ref{eqn:general_sol}$).

In other words, when we add an input $r(x)$ that depends only on the independent variable $x$ to the homogeneous differential equation ($\ref{eqn:homogeneous_linear_ode}$), a corresponding term $y_p$ is added to the response, and this additional response term $y_p$ is determined solely by the input $r(x)$, independent of the initial conditions. As we will see later, if we take the difference between any two solutions $y_1$ and $y_2$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) (i.e., the difference between particular solutions for two different initial conditions), the $y_p$ term that is independent of initial conditions cancels out, leaving only the difference between ${y_h}_1$ and ${y_h}_2$, which by the [superposition principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle) is a solution to equation ($\ref{eqn:homogeneous_linear_ode}$).

## Relationship Between Solutions of Nonhomogeneous and Homogeneous Differential Equations
> **Theorem 1: Relationship Between Solutions of Nonhomogeneous and Homogeneous Differential Equations**  
> **(a)** The sum of any solution $y$ of the nonhomogeneous differential equation ($\ref{eqn:nonhomogeneous_linear_ode}$) and any solution $\tilde{y}$ of the homogeneous differential equation ($\ref{eqn:homogeneous_linear_ode}$) on an open interval $I$ is a solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$. In particular, equation ($\ref{eqn:general_sol}$) is a solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$.  
> **(b)** The difference between any two solutions of the nonhomogeneous differential equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$ is a solution of the homogeneous differential equation ($\ref{eqn:homogeneous_linear_ode}$) on interval $I$.
{: .prompt-info }

### Proof
#### (a)
Let's denote the left side of equations ($\ref{eqn:nonhomogeneous_linear_ode}$) and ($\ref{eqn:homogeneous_linear_ode}$) as $L[y]$. Then for any solution $y$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) and any solution $\tilde{y}$ of equation ($\ref{eqn:homogeneous_linear_ode}$) on interval $I$, we have:

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
For any two solutions $y$ and $y^\*$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$, we have:

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## The General Solution Includes All Solutions
We know that for homogeneous differential equation ($\ref{eqn:homogeneous_linear_ode}$), [the general solution includes all solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/#the-general-solution-includes-all-solutions). Let's show that the same holds for nonhomogeneous differential equation ($\ref{eqn:nonhomogeneous_linear_ode}$).

> **Theorem 2: The General Solution of a Nonhomogeneous Differential Equation Includes All Solutions**  
> If the coefficients $p(x)$, $q(x)$ and the input function $r(x)$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) are continuous on an open interval $I$, then any solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$ can be obtained from the general solution ($\ref{eqn:general_sol}$) by assigning appropriate values to the arbitrary constants $c_1$ and $c_2$ in $y_h$.
{: .prompt-info }

### Proof
Let $y^\*$ be any solution of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) on interval $I$, and let $x_0$ be any point in interval $I$. By the [existence theorem for general solutions of homogeneous equations with continuous coefficients](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-of-general-solution), $y_h = c_1y_1 + c_2y_2$ exists, and by the **method of variation of parameters** (which we will explore later), $y_p$ also exists, so the general solution ($\ref{eqn:general_sol}$) of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) exists on interval $I$. Now, by Theorem [1(b)](#relationship-between-solutions-of-nonhomogeneous-and-homogeneous-differential-equations), $Y = y^\* - y_p$ is a solution of the homogeneous differential equation ($\ref{eqn:homogeneous_linear_ode}$) on interval $I$, and at $x_0$:

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

By the [existence and uniqueness theorem for initial value problems](/posts/wronskian-existence-and-uniqueness-of-solutions/#existence-and-uniqueness-theorem-for-initial-value-problems), there exists a unique solution $Y$ of the homogeneous differential equation ($\ref{eqn:homogeneous_linear_ode}$) on interval $I$ satisfying these initial conditions, which can be obtained by assigning appropriate values to $c_1$ and $c_2$ in $y_h$. Since $y^\* = Y + y_p$, we have shown that any particular solution $y^\*$ of the nonhomogeneous differential equation ($\ref{eqn:nonhomogeneous_linear_ode}$) can be obtained from the general solution ($\ref{eqn:general_sol}$). $\blacksquare$
