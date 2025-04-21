---
title: Method of Undetermined Coefficients
description: Let's explore the method of undetermined coefficients, a useful technique frequently applied in engineering for vibration systems and RLC circuit models that can simply solve initial value problems for certain types of constant-coefficient nonhomogeneous linear ordinary differential equations.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Method of Undetermined Coefficients** applies to:
>   - Linear ODEs with **constant coefficients $a$ and $b$**
>   - Where input $r(x)$ consists of exponential functions, powers of $x$, $\cos$ or $\sin$, or sums and products of such functions
>   - In the form $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Selection Rules for the Method of Undetermined Coefficients**  
>   - **(a) Basic rule**: If $r(x)$ in equation ($\ref{eqn:linear_ode_with_constant_coefficients}$) is one of the functions in the first column of the table, select $y_p$ from the same row in the second column, and determine the undetermined coefficients by substituting $y_p$ and its derivatives into equation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Modification rule**: If the term chosen for $y_p$ is a solution of the corresponding homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$, multiply this term by $x$ (or by $x^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
>   - **(c) Sum rule**: If $r(x)$ is a sum of functions from the first column of the table, select $y_p$ as the sum of the corresponding functions from the second column.
>
> | Term in $r(x)$ | Selection for $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskian, Existence and Uniqueness of Solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Nonhomogeneous Linear ODEs of Second Order](/posts/nonhomogeneous-linear-odes-of-second-order/)

## Method of Undetermined Coefficients
Consider a second-order nonhomogeneous linear ODE with $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

and the corresponding homogeneous ODE

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

As we saw in [Nonhomogeneous Linear ODEs of Second Order](/posts/nonhomogeneous-linear-odes-of-second-order/), to solve an initial value problem for the nonhomogeneous linear ODE ($\ref{eqn:nonhomogeneous_linear_ode}$), we need to find $y_h$ by solving the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) and then find a particular solution $y_p$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) to obtain the general solution

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

So how do we find $y_p$? The general method for finding $y_p$ is the **method of variation of parameters**, but in some cases, the much simpler **method of undetermined coefficients** can be applied. This method is particularly useful in engineering for vibration systems and RLC circuit models.

The method of undetermined coefficients is suitable for linear ODEs with **constant coefficients $a$ and $b$** where the input $r(x)$ consists of exponential functions, powers of $x$, $\cos$ or $\sin$, or sums and products of such functions:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

The key to the method of undetermined coefficients is that such forms of $r(x)$ have derivatives that are similar in form to themselves. To apply the method, we select a $y_p$ that is similar in form to $r(x)$ but with undetermined coefficients that are determined by substituting $y_p$ and its derivatives into the given ODE. The rules for selecting an appropriate $y_p$ for practically important forms of $r(x)$ in engineering are as follows:

> **Selection Rules for the Method of Undetermined Coefficients**  
> **(a) Basic rule**: If $r(x)$ in equation ($\ref{eqn:linear_ode_with_constant_coefficients}$) is one of the functions in the first column of the table, select $y_p$ from the same row in the second column, and determine the undetermined coefficients by substituting $y_p$ and its derivatives into equation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Modification rule**: If the term chosen for $y_p$ is a solution of the corresponding homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$, multiply this term by $x$ (or by $x^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
> **(c) Sum rule**: If $r(x)$ is a sum of functions from the first column of the table, select $y_p$ as the sum of the corresponding functions from the second column.
>
> | Term in $r(x)$ | Selection for $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

This method is not only convenient but also has a self-correcting property. If you select $y_p$ incorrectly or choose too few terms, you'll reach a contradiction; if you choose too many terms, the coefficients of unnecessary terms will become 0, still yielding the correct result. Even if something goes wrong when applying the method, you'll naturally notice it during the solution process, so you can confidently try with a reasonably appropriate $y_p$ according to the selection rules above.

### Proof of the Sum Rule
Consider a nonhomogeneous linear ODE of the form $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

Now consider the following two equations with the same left-hand side but with inputs $r_1$ and $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

Suppose these equations have solutions ${y_p}_1$ and ${y_p}_2$ respectively. If we denote the left-hand side of the equation as $L[y]$, then by the linearity of $L[y]$, for $y_p = {y_p}_1 + {y_p}_2$, we have:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

This proves the sum rule.

### Example: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
According to the basic rule (a), we set $y_p = Ce^{\gamma x}$ and substitute it into the given equation $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### Case: $\gamma^2 + a\gamma + b \neq 0$
We can determine the undetermined coefficient $C$ and find $y_p$ as follows:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### Case: $\gamma^2 + a\gamma + b = 0$
In this case, we need to apply the modification rule (b). First, using $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, let's find the roots of the characteristic equation of the homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

From this, we obtain the basis for the homogeneous ODE:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

##### Subcase: $\gamma \neq -a-\gamma$
Since the term $Ce^{\gamma x}$ we selected for $y_p$ is a solution of the corresponding homogeneous ODE but not a double root, according to the modification rule (b), we multiply this term by $x$ to get $y_p = Cxe^{\gamma x}$.

Now we substitute this modified $y_p$ into the given equation $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### Subcase: $\gamma = -a-\gamma$
In this case, the term $Ce^{\gamma x}$ we selected for $y_p$ corresponds to a double root of the characteristic equation of the homogeneous ODE. According to the modification rule (b), we multiply this term by $x^2$ to get $y_p = Cx^2 e^{\gamma x}$.

Now we substitute this modified $y_p$ into the given equation $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
