---
title: Homogeneous Linear ODEs of Second Order
description: Learn about the definition and characteristics of second-order linear differential equations, and understand the important theorem of the superposition principle and the resulting concept of basis in homogeneous linear differential equations.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Standard form** of second-order linear differential equations: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coefficients**: functions $p$, $q$
>   - **Input**: $r(x)$
>   - **Output** or **response**: $y(x)$
> - Homogeneous and nonhomogeneous
>   - **Homogeneous**: When $r(x)\equiv0$ in standard form
>   - **Nonhomogeneous**: When $r(x)\not\equiv 0$ in standard form
> - **Superposition principle**: For a <u>homogeneous</u> linear differential equation $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, any linear combination of two solutions in an open interval $I$ is also a solution to the given equation. In other words, the sum and scalar multiple of any solutions to the given homogeneous linear differential equation are also solutions to that equation.
> - **Basis** or **fundamental system**: A pair of solutions $(y_1, y_2)$ to the homogeneous linear differential equation that are linearly independent in the interval $I$
> - **Reduction of order**: If one solution can be found for a second-order homogeneous differential equation, a second solution linearly independent of this solution, i.e., a basis, can be found by solving a first-order differential equation
> - Application of reduction of order: A general second-order differential equation $F(x, y, y^\prime, y^{\prime\prime})=0$, whether linear or nonlinear, can be reduced to first order using reduction of order in the following cases:
>   - When $y$ does not appear explicitly
>   - When $x$ does not appear explicitly
>   - When it is homogeneous linear and one solution is already known
{: .prompt-info }

## Prerequisites
- [Basic Concepts of Modeling](/posts/Basic-Concepts-of-Modeling/)
- [Separation of Variables](/posts/Separation-of-Variables/)
- [Solution of First Order Linear ODE](/posts/Solution-of-First-Order-Linear-ODE/)

## Second-Order Linear Differential Equations
A second-order differential equation is called **linear** if it can be written in the form

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

and **nonlinear** otherwise.

When $p$, $q$, and $r$ are functions of $x$, this equation is linear in $y$ and its derivatives.

The form in equation ($\ref{eqn:standard_form}$) is called the **standard form** of a second-order linear differential equation. If the first term of a given second-order linear differential equation is $f(x)y^{\prime\prime}$, we can obtain the standard form by dividing both sides of the equation by $f(x)$.

The functions $p$ and $q$ are called **coefficients**, $r(x)$ is called the **input**, and $y(x)$ is called the **output** or **response** to the input and initial conditions.

### Homogeneous Second-Order Linear Differential Equations
Let $J$ be the interval $a<x<b$ where we want to solve equation ($\ref{eqn:standard_form}$). If $r(x)\equiv 0$ in $J$ in equation ($\ref{eqn:standard_form}$), we have

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

and this is called **homogeneous**.

## Nonhomogeneous Linear Differential Equations
If $r(x)\not\equiv 0$ in the interval $J$, it is called **nonhomogeneous**.

## Superposition Principle

A function of the form

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{ are arbitrary constants)}\tag{3}$$

is called a **linear combination** of $y_1$ and $y_2$.

The following principle holds:

> **Superposition Principle**  
> For a homogeneous linear differential equation ($\ref{eqn:homogeneous_linear_ode}$), any linear combination of two solutions in an open interval $I$ is also a solution to equation ($\ref{eqn:homogeneous_linear_ode}$). In other words, the sum and scalar multiple of any solutions to the given homogeneous linear differential equation are also solutions to that equation.
{: .prompt-info }

### Proof
Let $y_1$ and $y_2$ be solutions to equation ($\ref{eqn:homogeneous_linear_ode}$) in the interval $I$. Substituting $y=c_1y_1+c_2y_2$ into equation ($\ref{eqn:homogeneous_linear_ode}$), we get

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

which is an identity. Therefore, $y$ is a solution to equation ($\ref{eqn:homogeneous_linear_ode}$) in the interval $I$. $\blacksquare$

> Note that the superposition principle only holds for homogeneous linear differential equations and does not apply to nonhomogeneous linear differential equations or nonlinear differential equations.
{: .prompt-warning }

## Basis and General Solution
### Recap of Key Concepts from First-Order Differential Equations
As we saw earlier in [Basic Concepts of Modeling](/posts/Basic-Concepts-of-Modeling/), an initial value problem for a first-order differential equation consists of the differential equation and an initial condition $y(x_0)=y_0$. The initial condition is necessary to determine the arbitrary constant $c$ in the general solution of the given differential equation, and the solution determined this way is called a particular solution. Let's now extend these concepts to second-order differential equations.

### Initial Value Problem and Initial Conditions
An **initial value problem** for a second-order homogeneous differential equation ($\ref{eqn:homogeneous_linear_ode}$) consists of the given differential equation ($\ref{eqn:homogeneous_linear_ode}$) and two **initial conditions**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

These conditions are necessary to determine the two arbitrary constants $c_1$ and $c_2$ in the **general solution** of the differential equation

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Linear Independence and Linear Dependence
Let's briefly look at the concepts of linear independence and linear dependence. We need to understand this to define the basis later.  
If for two functions $y_1$ and $y_2$ defined on an interval $I$,

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ and }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

holds for all points in $I$, then these two functions $y_1$ and $y_2$ are said to be **linearly independent** on the interval $I$. If not, $y_1$ and $y_2$ are said to be **linearly dependent**.

If $y_1$ and $y_2$ are linearly dependent (i.e., if proposition ($\ref{eqn:linearly_independent}$) is not true), we can divide both sides of the equation in ($\ref{eqn:linearly_independent}$) by $k_1 \neq 0$ or $k_2 \neq 0$ to get

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{or} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

which shows that $y_1$ and $y_2$ are proportional.

### Basis, General Solution, Particular Solution
Coming back, for equation ($\ref{eqn:general_sol}$) to be a general solution, $y_1$ and $y_2$ must be solutions to equation ($\ref{eqn:homogeneous_linear_ode}$) and at the same time be linearly independent (not proportional to each other) in the interval $I$. A pair of solutions $(y_1, y_2)$ to equation ($\ref{eqn:homogeneous_linear_ode}$) that satisfies these conditions and is linearly independent in the interval $I$ is called a **basis** or **fundamental system** of solutions to equation ($\ref{eqn:homogeneous_linear_ode}$) in the interval $I$.

By using the initial conditions to determine the two constants $c_1$ and $c_2$ in the general solution ($\ref{eqn:general_sol}$), we obtain a unique solution that passes through the point $(x_0, K_0)$ and has a slope of $K_1$ at that point. This is called a **particular solution** to the differential equation ($\ref{eqn:homogeneous_linear_ode}$).

If equation ($\ref{eqn:homogeneous_linear_ode}$) is continuous on an open interval $I$, it must have a general solution, and this general solution includes all possible particular solutions. In other words, in this case, equation ($\ref{eqn:homogeneous_linear_ode}$) does not have singular solutions that cannot be obtained from the general solution.

## Reduction of Order
If we can find one solution to a second-order homogeneous differential equation, we can find a second solution linearly independent of this solution, i.e., a basis, by solving a first-order differential equation as follows. This method is called **reduction of order**.

For a second-order homogeneous differential equation in standard form <u>with $y^{\prime\prime}$ instead of $f(x)y^{\prime\prime}$</u>

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

suppose we know one solution $y_1$ to this equation in an open interval $I$.

Now, let's set the second solution we're looking for as $y_2 = uy_1$, and

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

Substituting these into the equation, we get

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Grouping terms with $u^{\prime\prime}$, $u^{\prime}$, and $u$, we get

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

However, since $y_1$ is a solution to the given equation, the expression in the last parenthesis is 0, so the $u$ term disappears, leaving a differential equation in $u^{\prime}$ and $u^{\prime\prime}$. Dividing both sides of this remaining differential equation by $y_1$ and setting $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$, we get the following first-order differential equation:

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

[Separating variables](/posts/Separation-of-Variables/) and integrating, we get

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

Taking the exponential of both sides, we finally get

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Since we set $U=u^{\prime}$ earlier, $u=\int U dx$, so the second solution $y_2$ we're looking for is

$$ y_2 = uy_1 = y_1 \int U dx $$

As long as $U>0$, $\cfrac{y_2}{y_1} = u = \int U dx$ cannot be a constant, so $y_1$ and $y_2$ form a basis of solutions.

### Application of Reduction of Order
A general second-order differential equation $F(x, y, y^\prime, y^{\prime\prime})=0$, whether linear or nonlinear, can be reduced to first order using reduction of order when $y$ does not appear explicitly, when $x$ does not appear explicitly, or as we saw earlier, when it is homogeneous linear and one solution is already known.

#### When $y$ does not appear explicitly
In $F(x, y^\prime, y^{\prime\prime})=0$, if we set $z=y^{\prime}$, we can reduce it to a first-order differential equation $F(x, z, z^{\prime})$ in $z$.

#### When $x$ does not appear explicitly
In $F(y, y^\prime, y^{\prime\prime})=0$, if we set $z=y^{\prime}$, then $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$, so we can reduce it to a first-order differential equation $F(y,z,z^\prime)$ in $z$ where $y$ takes the role of the independent variable $x$.
