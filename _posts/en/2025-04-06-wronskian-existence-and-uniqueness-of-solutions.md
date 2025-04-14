---
title: Wronskian, Existence and Uniqueness of Solutions
description: For a second-order homogeneous linear differential equation with arbitrary continuous variable coefficients, we explore the existence and uniqueness theorem for initial value problems, the Wronskian method for determining linear dependence/independence of solutions, and prove that such equations always have general solutions that include all possible solutions.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> For a second-order homogeneous linear differential equation with arbitrary continuous variable coefficients $p$ and $q$ on an interval $I$:
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> and initial conditions
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> the following four theorems hold:
> 1. **Existence and Uniqueness Theorem for Initial Value Problems**: The initial value problem consisting of the given equation and initial conditions has a unique solution $y(x)$ on interval $I$.
> 2. **Determining Linear Dependence/Independence Using the Wronskian**: For two solutions $y_1$ and $y_2$ of the equation, if there exists an $x_0$ in interval $I$ where the **Wronskian** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ equals zero, then the two solutions are linearly dependent. Furthermore, if there exists an $x_1$ in interval $I$ where $W\neq 0$, then the two solutions are linearly independent.
> 3. **Existence of General Solution**: The given equation has a general solution on interval $I$.
> 4. **Non-existence of Singular Solutions**: This general solution includes all solutions of the equation (i.e., singular solutions do not exist).
{: .prompt-info }

## Prerequisites
- [Solution of First-Order Linear ODE](/posts/Solution-of-First-Order-Linear-ODE/)
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogeneous Linear ODEs with Constant Coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Euler-Cauchy Equation](/posts/euler-cauchy-equation/)
- Inverse matrices and singular matrices, determinants

## Homogeneous Linear Differential Equations with Arbitrary Continuous Variable Coefficients
Previously, we explored the general solutions of [homogeneous linear ODEs with constant coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/) and [Euler-Cauchy equations](/posts/euler-cauchy-equation/).
In this post, we extend our discussion to the more general case of second-order homogeneous linear differential equations with arbitrary continuous **variable coefficients** $p$ and $q$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

We will examine the existence and form of general solutions to this equation. Additionally, we will investigate the uniqueness of the [initial value problem](/posts/homogeneous-linear-odes-of-second-order/#initial-value-problem-and-initial-conditions) consisting of differential equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) and the following two initial conditions:

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

To preview our conclusion, the key insight is that <u>linear</u> differential equations with continuous coefficients do not possess *singular solutions* (solutions that cannot be derived from the general solution).

## Existence and Uniqueness Theorem for Initial Value Problems
> **Existence and Uniqueness Theorem for Initial Value Problems**  
> If $p(x)$ and $q(x)$ are continuous functions on some open interval $I$, and $x_0$ is a point in interval $I$, then the initial value problem consisting of equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) and conditions ($\ref{eqn:initial_conditions}$) has a unique solution $y(x)$ on interval $I$.
{: .prompt-info }

We will only address the proof of uniqueness here, as proving existence is typically more complex.  
If you're not interested in the proof, you can skip to the [Linear Dependence and Linear Independence of Solutions](#linear-dependence-and-linear-independence-of-solutions) section.

### Proof of Uniqueness
Assume that the initial value problem consisting of differential equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) and initial conditions ($\ref{eqn:initial_conditions}$) has two solutions $y_1(x)$ and $y_2(x)$ on interval $I$. We need to show that their difference

$$ y(x) = y_1(x) - y_2(x) $$

is identically zero on interval $I$, which would imply that $y_1 \equiv y_2$ on interval $I$, proving uniqueness.

Since equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) is a homogeneous linear differential equation, the linear combination $y$ of $y_1$ and $y_2$ is also a solution on interval $I$. Since $y_1$ and $y_2$ satisfy the same initial conditions ($\ref{eqn:initial_conditions}$), $y$ satisfies the conditions

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Now consider the function

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

and its derivative

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

From the differential equation, we have

$$ y^{\prime\prime} = -py^{\prime} - qy $$

Substituting this into the expression for $z^{\prime}$, we get

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Since $y$ and $y^{\prime}$ are real numbers, we have

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

From this and the definition of $z$, we obtain two inequalities:

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

These inequalities imply that $\|2yy^{\prime}\|\leq z$, and therefore for the last term in equation ($\ref{eqn:z_prime}$), we have:

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Using this result along with $-p \leq \|p\|$ and applying inequality ($\ref{eqn:inequalities}$a) to the term $2yy^{\prime}$ in equation ($\ref{eqn:z_prime}$), we get:

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Since ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, we obtain:

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

If we denote the function in parentheses as $h = 1 + 2\|p\| + \|q\|$, we have:

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

Similarly, from equations ($\ref{eqn:z_prime}$) and ($\ref{eqn:inequalities}$), we get:

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

These two inequalities ($\ref{eqn:inequality_6a}$) and ($\ref{eqn:inequality_6b}$) are equivalent to:

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

The [integrating factors](/posts/Solution-of-First-Order-Linear-ODE/#nonhomogeneous-linear-ordinary-differential-equation) for the left sides of these inequalities are:

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{and} \qquad F_2 = e^{\int h(x)\ dx} $$

Since $h$ is continuous, the indefinite integral $\int h(x)\ dx$ exists, and since $F_1$ and $F_2$ are positive, from inequalities ($\ref{eqn:inequalities_7}$) we get:

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

This means that $F_1 z$ is non-increasing and $F_2 z$ is non-decreasing on interval $I$. From equation ($\ref{eqn:initial_conditions_*}$), we know that $z(x_0) = 0$, so:

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finally, dividing these inequalities by the positive values $F_1$ and $F_2$, we can prove uniqueness:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Linear Dependence and Linear Independence of Solutions
Let's recall what we discussed in [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/#basis-and-general-solution). The general solution on an open interval $I$ is constructed from a **basis** $y_1$, $y_2$ - a pair of linearly independent solutions on $I$. Two functions $y_1$ and $y_2$ are **linearly independent** on interval $I$ if for all $x$ in the interval:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ and }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

If this condition is not satisfied, and there exist non-zero constants $k_1$, $k_2$ such that $k_1y_1(x) + k_2y_2(x) = 0$, then $y_1$ and $y_2$ are **linearly dependent** on interval $I$. In this case, for all $x$ in interval $I$:

$$ \text{(a) } y_1 = ky_2 \quad \text{or} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

meaning that $y_1$ and $y_2$ are proportional.

Now let's examine the method for determining linear dependence/independence of solutions:

> **Determining Linear Dependence/Independence Using the Wronskian**  
> **i.** If differential equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has continuous coefficients $p(x)$ and $q(x)$ on an open interval $I$, then a necessary and sufficient condition for two solutions $y_1$ and $y_2$ of equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) to be linearly dependent is that their *Wronski determinant*, or **Wronskian**
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> equals zero at some point $x_0$ in interval $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ and } y_2 \text{ are linearly dependent} $$
>
> **ii.** If the Wronskian $W=0$ at one point $x=x_0$ in interval $I$, then $W=0$ at all points in interval $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> In other words, if there exists a point $x_1$ in interval $I$ where $W\neq 0$, then $y_1$ and $y_2$ are linearly independent on interval $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_1)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ and } y_2 \text{ are linearly independent}
> \end{align*}$$
>
{: .prompt-info }

> The Wronskian was first introduced by the Polish mathematician Józef Maria Hoene-Wroński, and was named after him by the Scottish mathematician Sir Thomas Muir in 11882 HE, after Wroński's death.
{: .prompt-tip }

### Proof
#### i. (a)
Suppose $y_1$ and $y_2$ are linearly dependent on interval $I$. Then either equation ($\ref{eqn:linearly_dependent}$a) or ($\ref{eqn:linearly_dependent}$b) holds on interval $I$. If equation ($\ref{eqn:linearly_dependent}$a) holds, then:

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

Similarly, if equation ($\ref{eqn:linearly_dependent}$b) holds:

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

Thus, we've shown that the Wronskian $W(y_1, y_2)=0$ for <u>all $x$ in interval $I$</u>.

#### i. (b)
Conversely, suppose that $W(y_1, y_2)=0$ at some point $x = x_0$. We'll show that $y_1$ and $y_2$ are linearly dependent on interval $I$. Consider the system of linear equations in unknowns $k_1$, $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

This can be expressed as the vector equation:

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

The coefficient matrix is:

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

and its determinant is $W(y_1(x_0), y_2(x_0))$. Since $\det(A) = W=0$, $A$ is a **singular matrix** without an **inverse matrix**, so the system of equations ($\ref{eqn:linear_system}$) has a non-trivial solution $(c_1, c_2)$ where at least one of $c_1$ or $c_2$ is non-zero. Now consider the function:

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Since equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) is homogeneous and linear, by the [superposition principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle), this function is a solution to equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on interval $I$. From equation ($\ref{eqn:linear_system}$), this solution satisfies the initial conditions $y(x_0)=0$, $y^{\prime}(x_0)=0$.

However, the trivial solution $y^\* \equiv 0$ also satisfies the same initial conditions $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Since the coefficients $p$ and $q$ in equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) are continuous, the [Existence and Uniqueness Theorem for Initial Value Problems](#existence-and-uniqueness-theorem-for-initial-value-problems) guarantees that the solution is unique, so $y \equiv y^\*$. This means that on interval $I$:

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Since at least one of $c_1$ or $c_2$ is non-zero, condition ($\ref{eqn:linearly_independent}$) is not satisfied, which means that $y_1$ and $y_2$ are linearly dependent on interval $I$.

#### ii.
If the Wronskian $W(x_0)=0$ at some point $x_0$ in interval $I$, then by [i.(b)](#i-b), $y_1$ and $y_2$ are linearly dependent on interval $I$, and by [i.(a)](#i-a), $W\equiv 0$ on interval $I$. Therefore, if there exists a point $x_1$ in interval $I$ where $W(x_1)\neq 0$, then $y_1$ and $y_2$ must be linearly independent. $\blacksquare$

## The General Solution Includes All Solutions
### Existence of General Solution
> If $p(x)$ and $q(x)$ are continuous on an open interval $I$, then differential equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has a general solution on interval $I$.
{: .prompt-info }

#### Proof
By the [Existence and Uniqueness Theorem for Initial Value Problems](#existence-and-uniqueness-theorem-for-initial-value-problems), differential equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has a solution $y_1(x)$ on interval $I$ satisfying the initial conditions:

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

and a solution $y_2(x)$ on interval $I$ satisfying the initial conditions:

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

The Wronskian of these two solutions at $x=x_0$ is non-zero:

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

By the [Wronskian method for determining linear dependence/independence](#linear-dependence-and-linear-independence-of-solutions), $y_1$ and $y_2$ are linearly independent on interval $I$. Therefore, these two solutions form a basis for the solutions of equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on interval $I$, and the general solution $y = c_1y_1 + c_2y_2$ with arbitrary constants $c_1$, $c_2$ exists on interval $I$. $\blacksquare$

### Non-existence of Singular Solutions
> If differential equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has continuous coefficients $p(x)$ and $q(x)$ on an open interval $I$, then every solution $y=Y(x)$ of equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on interval $I$ has the form:
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> where $y_1$, $y_2$ form a basis for the solutions of equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on interval $I$, and $C_1$, $C_2$ are appropriate constants.  
> In other words, equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) does not have **singular solutions** (solutions that cannot be obtained from the general solution).
{: .prompt-info }

#### Proof
Let $y=Y(x)$ be any solution of equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on interval $I$. By the [Existence of General Solution theorem](#existence-of-general-solution), equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has a general solution on interval $I$:

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

We need to show that for any $Y(x)$, there exist constants $c_1$, $c_2$ such that $y(x)=Y(x)$ on interval $I$. First, let's show that we can find values of $c_1$, $c_2$ such that $y(x_0)=Y(x_0)$ and $y^{\prime}(x_0)=Y^{\prime}(x_0)$ for any chosen $x_0$ in interval $I$. From equation ($\ref{eqn:general_solution}$), we have:

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

Since $y_1$ and $y_2$ form a basis, the determinant of the coefficient matrix, $W(y_1(x_0), y_2(x_0))\neq 0$, so equation ($\ref{eqn:vector_equation_2}$) can be solved for $c_1$ and $c_2$. Let's call the solution $(c_1, c_2) = (C_1, C_2)$. Substituting these values into equation ($\ref{eqn:general_solution}$), we get the particular solution:

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Since $C_1$ and $C_2$ satisfy equation ($\ref{eqn:vector_equation_2}$):

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

By the uniqueness part of the [Existence and Uniqueness Theorem](#existence-and-uniqueness-theorem-for-initial-value-problems), $y^* \equiv Y$ on interval $I$. $\blacksquare$
