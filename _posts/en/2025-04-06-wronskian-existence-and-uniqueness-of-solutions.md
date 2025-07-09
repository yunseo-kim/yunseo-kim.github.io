---
title: "The Wronskian, Existence and Uniqueness of Solutions"
description: "Explore the existence and uniqueness of solutions for second-order homogeneous linear ODEs with continuous variable coefficients. Learn to use the Wronskian to test for linear independence and see why these equations always have a general solution that encompasses all possible solutions."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> For a second-order homogeneous linear ordinary differential equation with continuous variable coefficients $p$ and $q$ on an interval $I$
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> and initial conditions
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> the following four theorems hold.
> 1. **Existence and Uniqueness Theorem for Initial Value Problems**: The initial value problem consisting of the given equation and initial conditions has a unique solution $y(x)$ on the interval $I$.
> 2. **Test for Linear Dependence/Independence using the Wronskian**: For two solutions $y_1$ and $y_2$ of the equation, if there exists an $x_0$ in the interval $I$ where the **Wronskian** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ is $0$, then the two solutions are linearly dependent. Furthermore, if there exists an $x_1$ in the interval $I$ where $W\neq 0$, then the two solutions are linearly independent.
> 3. **Existence of a General Solution**: The given equation has a general solution on the interval $I$.
> 4. **Nonexistence of Singular Solutions**: This general solution includes all solutions of the equation (i.e., no singular solutions exist).
{: .prompt-info }

## Prerequisites
- [Solution of First-Order Linear ODEs](/posts/Solution-of-First-Order-Linear-ODE/)
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogeneous Linear ODEs with Constant Coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Euler-Cauchy Equation](/posts/euler-cauchy-equation/)
- Inverse Matrix, Singular Matrix, and Determinant

## Homogeneous Linear ODEs with Continuous Variable Coefficients
Previously, we examined the general solutions of [Homogeneous Linear ODEs with Constant Coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/) and the [Euler-Cauchy Equation](/posts/euler-cauchy-equation/).
In this article, we extend the discussion to a more general case: a second-order homogeneous linear ordinary differential equation with arbitrary continuous **variable coefficients** $p$ and $q$.

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

We will investigate the existence and form of the general solution for this equation. Additionally, we will explore the uniqueness of the solution to the [Initial Value Problem](/posts/homogeneous-linear-odes-of-second-order/#initial-value-problem-and-initial-conditions) composed of the ODE ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) and the following two initial conditions:

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

To state the conclusion upfront, the core of this discussion is that a <u>linear</u> ordinary differential equation with continuous coefficients does not have a *singular solution* (a solution that cannot be obtained from the general solution).

## Existence and Uniqueness Theorem for Initial Value Problems
> **Existence and Uniqueness Theorem for Initial Value Problems**  
> If $p(x)$ and $q(x)$ are continuous functions on some open interval $I$, and $x_0$ is in $I$, then the initial value problem consisting of Eqs. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) and ($\ref{eqn:initial_conditions}$) has a unique solution $y(x)$ on the interval $I$.
{: .prompt-info }

The proof of existence will not be covered here; we will only look at the proof of uniqueness. Proving uniqueness is typically simpler than proving existence.  
If you are not interested in the proof, you may skip this section and proceed to [Linear Dependence and Independence of Solutions](#linear-dependence-and-independence-of-solutions).

### Proof of Uniqueness
Let's assume that the initial value problem consisting of the ODE ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) and initial conditions ($\ref{eqn:initial_conditions}$) has two solutions, $y_1(x)$ and $y_2(x)$, on the interval $I$. If we can show that their difference

$$ y(x) = y_1(x) - y_2(x) $$

is identically zero on the interval $I$, this implies that $y_1 \equiv y_2$ on $I$, which means the solution is unique.

Since Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) is a homogeneous linear ODE, the linear combination $y$ of $y_1$ and $y_2$ is also a solution to the equation on $I$. Since $y_1$ and $y_2$ satisfy the same initial conditions ($\ref{eqn:initial_conditions}$), $y$ satisfies the conditions

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

Now, consider the function

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

and its derivative

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

From the ODE, we have

$$ y^{\prime\prime} = -py^{\prime} - qy $$

Substituting this into the expression for $z^{\prime}$ gives

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

Now, since $y$ and $y^{\prime}$ are real,

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

From this and the definition of $z$, we can derive two inequalities:

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

From these two inequalities, we know that $|2yy^{\prime}|\leq z$. Thus, for the last term in Eq. ($\ref{eqn:z_prime}$), the following inequality holds:

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

Using this result, along with $-p \leq |p|$, and applying inequality ($\ref{eqn:inequalities}$a) to the term $2yy^{\prime}$ in Eq. ($\ref{eqn:z_prime}$), we get

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

Since ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$, this leads to

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

Letting the function in the parenthesis be $h = 1 + 2|p| + |q|$, we have

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

In the same way, from Eqs. ($\ref{eqn:z_prime}$) and ($\ref{eqn:inequalities}$), we get

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

These two inequalities, ($\ref{eqn:inequality_6a}$) and ($\ref{eqn:inequality_6b}$), are equivalent to the following inequalities:

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

The [integrating factors](/posts/Solution-of-First-Order-Linear-ODE/#nonhomogeneous-linear-ordinary-differential-equations) for the left-hand sides of these two expressions are

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{and} \qquad F_2 = e^{\int h(x)\ dx} $$

Since $h$ is continuous, the indefinite integral $\int h(x)\ dx$ exists. As $F_1$ and $F_2$ are positive, from ($\ref{eqn:inequalities_7}$) we obtain

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

This means that on the interval $I$, $F_1 z$ is non-increasing and $F_2 z$ is non-decreasing. By Eq. ($\ref{eqn:initial_conditions_*}$), we have $z(x_0) = 0$, so

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

Finally, dividing both sides of the inequalities by the positive functions $F_1$ and $F_2$, we can show the uniqueness of the solution as follows:

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## Linear Dependence and Independence of Solutions
Let's briefly recall what we covered in [Second-Order Homogeneous Linear ODEs](/posts/homogeneous-linear-odes-of-second-order/#basis-and-general-solution). The general solution on an open interval $I$ is constructed from a **basis** $y_1$, $y_2$ on $I$, which is a pair of linearly independent solutions. Here, $y_1$ and $y_2$ being **linearly independent** on an interval $I$ means that for all $x$ in the interval, the following holds:

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{ and }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

If the above is not satisfied, and $k_1y_1(x) + k_2y_2(x) = 0$ holds for at least one non-zero $k_1$ or $k_2$, then $y_1$ and $y_2$ are **linearly dependent** on the interval $I$. In this case, for all $x$ in the interval $I$,

$$ \text{(a) } y_1 = ky_2 \quad \text{or} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

which means $y_1$ and $y_2$ are proportional.

Now let's look at the following test for linear independence/dependence of solutions.

> **Test for Linear Dependence/Independence using the Wronskian**  
> **i.** If the ODE ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has continuous coefficients $p(x)$ and $q(x)$ on an open interval $I$, then a necessary and sufficient condition for two solutions $y_1$ and $y_2$ of Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) to be linearly dependent on $I$ is that their *Wronski determinant*, or simply **Wronskian**, which is the following determinant,
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> is zero at some $x_0$ in the interval $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{ and } y_2 \text{ are linearly dependent} $$
>
> **ii.** If $W=0$ at a point $x=x_0$ in the interval $I$, then $W=0$ for all $x$ in the interval $I$.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> In other words, if there exists an $x_1$ in the interval $I$ such that $W\neq 0$, then $y_1$ and $y_2$ are linearly independent on that interval $I$.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{ and } y_2 \text{ are linearly independent}
> \end{align*}$$
>
{: .prompt-info }

> The Wronskian was first introduced by the Polish mathematician Józef Maria Hoene-Wroński and was named after him posthumously in 11882 HE by the Scottish mathematician Sir Thomas Muir.
{: .prompt-tip }

### Proof
#### i. (a)
Let $y_1$ and $y_2$ be linearly dependent on the interval $I$. Then, either Eq. ($\ref{eqn:linearly_dependent}$a) or ($\ref{eqn:linearly_dependent}$b) holds on $I$. If Eq. ($\ref{eqn:linearly_dependent}$a) holds, then

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2y_2^{\prime} - y_2(ky_2^{\prime}) = 0 $$

Similarly, if Eq. ($\ref{eqn:linearly_dependent}$b) holds, then

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1(ly_1^{\prime}) - ly_1y_1^{\prime} = 0 $$

Thus, we can confirm that the Wronskian $W(y_1, y_2)=0$ <u>for all $x$ in the interval $I$</u>.

#### i. (b)
Conversely, suppose that $W(y_1, y_2)=0$ for some $x = x_0$. We will show that $y_1$ and $y_2$ are linearly dependent on the interval $I$. Consider the system of linear equations for the unknowns $k_1$, $k_2$:

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

This can be expressed in the form of a vector equation:

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

The coefficient matrix of this vector equation is

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

and the determinant of this matrix is $W(y_1(x_0), y_2(x_0))$. Since $\det(A) = W=0$, $A$ is a **singular matrix** that does not have an **inverse matrix**. Therefore, the system of equations ($\ref{eqn:linear_system}$) has a non-trivial solution $(c_1, c_2)$ other than the zero vector $(0,0)$, where at least one of $k_1$ and $k_2$ is not zero. Now, let's introduce the function

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

Since Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) is homogeneous and linear, by the [Superposition Principle](/posts/homogeneous-linear-odes-of-second-order/#superposition-principle), this function is a solution of ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on the interval $I$. From Eq. ($\ref{eqn:linear_system}$), we can see that this solution satisfies the initial conditions $y(x_0)=0$, $y^{\prime}(x_0)=0$.

Meanwhile, there exists a trivial solution $y^\* \equiv 0$ that satisfies the same initial conditions $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$. Since the coefficients $p$ and $q$ of Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) are continuous, the uniqueness of the solution is guaranteed by the [Existence and Uniqueness Theorem for Initial Value Problems](#existence-and-uniqueness-theorem-for-initial-value-problems). Therefore, $y \equiv y^\*$. That is, on the interval $I$,

$$ c_1y_1 + c_2y_2 \equiv 0 $$

Since at least one of $c_1$ and $c_2$ is not zero, this does not satisfy ($\ref{eqn:linearly_independent}$), which means that $y_1$ and $y_2$ are linearly dependent on the interval $I$.

#### ii.
If $W(x_0)=0$ at some point $x_0$ in the interval $I$, then by [i.(b)](#i-b), $y_1$ and $y_2$ are linearly dependent on the interval $I$. Then, by [i.(a)](#i-a), $W\equiv 0$. Therefore, if there is even one point $x_1$ in the interval $I$ where $W(x_1)\neq 0$, then $y_1$ and $y_2$ are linearly independent. $\blacksquare$

## The General Solution Includes All Solutions
### Existence of a General Solution
> If $p(x)$ and $q(x)$ are continuous on an open interval $I$, then the equation ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has a general solution on the interval $I$.
{: .prompt-info }

#### Proof
By the [Existence and Uniqueness Theorem for Initial Value Problems](#existence-and-uniqueness-theorem-for-initial-value-problems), the ODE ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has a solution $y_1(x)$ on the interval $I$ that satisfies the initial conditions

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

and a solution $y_2(x)$ on the interval $I$ that satisfies the initial conditions

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

The Wronskian of these two solutions at $x=x_0$ has a non-zero value:

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

Therefore, by the [Test for Linear Dependence/Independence using the Wronskian](#linear-dependence-and-independence-of-solutions), $y_1$ and $y_2$ are linearly independent on the interval $I$. Thus, these two solutions form a basis of solutions for Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on the interval $I$, and a general solution $y = c_1y_1 + c_2y_2$ with arbitrary constants $c_1$, $c_2$ must exist on the interval $I$. $\blacksquare$

### Nonexistence of Singular Solutions
> If the ODE ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has continuous coefficients $p(x)$ and $q(x)$ on some open interval $I$, then every solution $y=Y(x)$ of Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on the interval $I$ is of the form
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> where $y_1$, $y_2$ form a basis of solutions for Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on the interval $I$, and $C_1$, $C_2$ are suitable constants.  
> That is, Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) does not have a **singular solution**, which is a solution that cannot be obtained from the general solution.
{: .prompt-info }

#### Proof
Let $y=Y(x)$ be any solution of Eq. ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) on the interval $I$. Now, by the [Existence of a General Solution theorem](#existence-of-a-general-solution), the ODE ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) has a general solution on the interval $I$:

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

Now we must show that for any $Y(x)$, there exist constants $c_1$, $c_2$ such that $y(x)=Y(x)$ on the interval $I$. Let's first show that we can find values for $c_1$, $c_2$ such that for an arbitrary $x_0$ in $I$, we have $y(x_0)=Y(x_0)$ and $y^{\prime}(x_0)=Y^{\prime}(x_0)$. From Eq. ($\ref{eqn:general_solution}$), we get

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

Since $y_1$ and $y_2$ form a basis, the determinant of the coefficient matrix, which is the Wronskian $W(y_1(x_0), y_2(x_0))$, is non-zero. Therefore, Eq. ($\ref{eqn:vector_equation_2}$) can be solved for $c_1$ and $c_2$. Let the solution be $(c_1, c_2) = (C_1, C_2)$. Substituting this into Eq. ($\ref{eqn:general_solution}$) gives the following particular solution:

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

Since $C_1$, $C_2$ are the solution to Eq. ($\ref{eqn:vector_equation_2}$),

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

By the uniqueness part of the [Existence and Uniqueness Theorem for Initial Value Problems](#existence-and-uniqueness-theorem-for-initial-value-problems), we have $y^\* \equiv Y$ for all $x$ in the interval $I$. $\blacksquare$
