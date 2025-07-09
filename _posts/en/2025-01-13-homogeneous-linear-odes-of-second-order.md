---
title: "Homogeneous Linear ODEs of Second Order"
description: "Learn the definition and properties of second-order linear ordinary differential equations, focusing on the superposition principle for homogeneous linear ODEs and the related concept of a basis."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Standard form** of a second-order linear ODE: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **Coefficients**: Functions $p$, $q$
>   - **Input**: $r(x)$
>   - **Output** or **response**: $y(x)$
> - Homogeneous and Nonhomogeneous
>   - **Homogeneous**: When $r(x)\equiv0$ in the standard form.
>   - **Nonhomogeneous**: When $r(x)\not\equiv 0$ in the standard form.
> - **Superposition principle**: For a <u>homogeneous</u> linear ODE $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$, any linear combination of two of its solutions on an open interval $I$ is also a solution of the given equation. That is, the sum and constant multiples of any solutions to the given homogeneous linear ODE are also solutions.
> - **Basis** or **fundamental system**: A pair of linearly independent solutions $(y_1, y_2)$ of a homogeneous linear ODE on an interval $I$.
> - **Reduction of order**: If one solution to a second-order homogeneous ODE is known, a second, linearly independent solution (i.e., a basis) can be found by solving a first-order ODE. This method is called reduction of order.
> - Applications of reduction of order: A general second-order ODE $F(x, y, y^\prime, y^{\prime\prime})=0$, whether linear or nonlinear, can be reduced to a first-order ODE using reduction of order in the following cases:
>   - $y$ does not appear explicitly.
>   - $x$ does not appear explicitly.
>   - The equation is homogeneous linear and one solution is already known.
{: .prompt-info }

## Prerequisites
- [Basic Concepts of Modeling](/posts/Basic-Concepts-of-Modeling/)
- [Separation of Variables](/posts/Separation-of-Variables/)
- [Solution of First-Order Linear ODEs](/posts/Solution-of-First-Order-Linear-ODE/)

## Second-Order Linear ODEs
A second-order ordinary differential equation is called **linear** if it can be written in the form

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

and **nonlinear** otherwise.

When $p$, $q$, and $r$ are functions of any $x$, this equation is linear with respect to $y$ and its derivatives.

The form of Eq. ($\ref{eqn:standard_form}$) is called the **standard form** of a second-order linear ODE. If the first term of a given second-order linear ODE is $f(x)y^{\prime\prime}$, we can obtain the standard form by dividing both sides of the equation by $f(x)$.

The functions $p$ and $q$ are called **coefficients**, $r(x)$ is the **input**, and $y(x)$ is the **output** or the **response** to the input and initial conditions.

### Homogeneous Second-Order Linear ODEs
Let $J$ be an interval $a<x<b$ where we want to solve Eq. ($\ref{eqn:standard_form}$). If $r(x)\equiv 0$ for the interval $J$ in Eq. ($\ref{eqn:standard_form}$), then

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

and this is called **homogeneous**.

## Nonhomogeneous Linear ODEs
If $r(x)\not\equiv 0$ in the interval $J$, the equation is called **nonhomogeneous**.

## Superposition Principle

A function of the form
$$ y = c_1y_1 + c_2y_2 \quad \text{(where }c_1, c_2\text{ are arbitrary constants)}\tag{3}$$
is called a **linear combination** of $y_1$ and $y_2$.

The following holds true.

> **Superposition principle**  
> For the homogeneous linear ODE ($\ref{eqn:homogeneous_linear_ode}$), any linear combination of two of its solutions on an open interval $I$ is also a solution of Eq. ($\ref{eqn:homogeneous_linear_ode}$). That is, the sum and constant multiples of any solutions to the given homogeneous linear ODE are also solutions.
{: .prompt-info }

### Proof
Let $y_1$ and $y_2$ be solutions of Eq. ($\ref{eqn:homogeneous_linear_ode}$) on an interval $I$. Substituting $y=c_1y_1+c_2y_2$ into Eq. ($\ref{eqn:homogeneous_linear_ode}$) gives

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

which becomes an identity. Therefore, $y$ is a solution of Eq. ($\ref{eqn:homogeneous_linear_ode}$) on the interval $I$. $\blacksquare$

> Note that the superposition principle holds only for homogeneous linear ODEs and not for nonhomogeneous linear or nonlinear ODEs.
{: .prompt-warning }

## Basis and General Solution
### Review of Key Concepts from First-Order ODEs
As we saw previously in [Basic Concepts of Modeling](/posts/Basic-Concepts-of-Modeling/), an Initial Value Problem for a first-order ODE consists of the ODE and an initial condition $y(x_0)=y_0$. The initial condition is necessary to determine the arbitrary constant $c$ in the general solution of the given ODE, and the resulting solution is called a particular solution. Let's now extend these concepts to second-order ODEs.

### Initial Value Problem and Initial Conditions
An **initial value problem** for the second-order homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) consists of the given ODE ($\ref{eqn:homogeneous_linear_ode}$) and two **initial conditions**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

These conditions are needed to determine the two arbitrary constants $c_1$ and $c_2$ in the **general solution** of the ODE

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

### Linear Independence and Dependence
Let's briefly discuss the concepts of linear independence and dependence. This is necessary to define a basis later.  
Two functions $y_1$ and $y_2$ are said to be **linearly independent** on an interval $I$ where they are defined if for all points in $I$,

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ and }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

Otherwise, $y_1$ and $y_2$ are said to be **linearly dependent**.

If $y_1$ and $y_2$ are linearly dependent (i.e., statement ($\ref{eqn:linearly_independent}$) is not true), then with $k_1 \neq 0$ or $k_2 \neq 0$, we can divide both sides of the equation in ($\ref{eqn:linearly_independent}$) to write

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{or} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

which shows that $y_1$ and $y_2$ are proportional.

### Basis, General Solution, and Particular Solution
Returning to our discussion, for Eq. ($\ref{eqn:general_sol}$) to be a general solution, $y_1$ and $y_2$ must be solutions to Eq. ($\ref{eqn:homogeneous_linear_ode}$) and also be linearly independent (not proportional to each other) on the interval $I$. A pair of solutions $(y_1, y_2)$ of Eq. ($\ref{eqn:homogeneous_linear_ode}$) that are linearly independent on an interval $I$ is called a **basis** or a **fundamental system** of solutions for Eq. ($\ref{eqn:homogeneous_linear_ode}$) on $I$.

By using the initial conditions to determine the two constants $c_1$ and $c_2$ in the general solution ($\ref{eqn:general_sol}$), we obtain a unique solution that passes through the point $(x_0, K_0)$ and has a slope of $K_1$ at that point. This is called a **particular solution** of the ODE ($\ref{eqn:homogeneous_linear_ode}$).

If Eq. ($\ref{eqn:homogeneous_linear_ode}$) is continuous on an open interval $I$, it is guaranteed to have a general solution, and this general solution includes all possible particular solutions. In this case, Eq. ($\ref{eqn:homogeneous_linear_ode}$) does not have a singular solution that cannot be obtained from the general solution.

## Reduction of Order
If we can find one solution to a second-order homogeneous ODE, we can find a second, linearly independent solution—that is, a basis—by solving a first-order ODE as follows. This method is called **reduction of order**.

For a second-order homogeneous ODE in <u>standard form with $y^{\prime\prime}$, not $f(x)y^{\prime\prime}$</u>,

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

let's assume we know one solution $y_1$ on an open interval $I$.

Now, let's set the second solution we are looking for as $y_2 = uy_1$, and substitute

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

into the equation to get

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

Grouping the terms by $u^{\prime\prime}$, $u^{\prime}$, and $u$ gives

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

However, since $y_1$ is a solution to the given equation, the expression in the last parenthesis is $0$. Thus, the term with $u$ disappears, leaving an ODE in terms of $u^{\prime}$ and $u^{\prime\prime}$. Dividing the remaining ODE by $y_1$ and setting $u^{\prime}=U$ and $u^{\prime\prime}=U^{\prime}$, we obtain the following first-order ODE.

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

Using [Separation of Variables](/posts/Separation-of-Variables/) and integrating,

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

and taking the exponential of both sides, we finally get

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

Since we set $U=u^{\prime}$, we have $u=\int U dx$. The second solution $y_2$ we are looking for is

$$ y_2 = uy_1 = y_1 \int U dx $$

Since $\cfrac{y_2}{y_1} = u = \int U dx$ cannot be a constant as long as $U>0$, $y_1$ and $y_2$ form a basis of solutions.

### Applications of Reduction of Order
A general second-order ODE $F(x, y, y^\prime, y^{\prime\prime})=0$, whether linear or nonlinear, can be reduced to a first-order ODE using reduction of order when $y$ does not appear explicitly, when $x$ does not appear explicitly, or, as seen before, when the equation is homogeneous linear and one solution is already known.

#### Case where $y$ does not appear explicitly
In $F(x, y^\prime, y^{\prime\prime})=0$, setting $z=y^{\prime}$ reduces the equation to a first-order ODE in $z$, $F(x, z, z^{\prime})$.

#### Case where $x$ does not appear explicitly
In $F(y, y^\prime, y^{\prime\prime})=0$, setting $z=y^{\prime}$ gives $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$. This reduces the equation to a first-order ODE in $z$, $F(y,z,z^\prime)$, where $y$ takes the role of the independent variable $x$.
