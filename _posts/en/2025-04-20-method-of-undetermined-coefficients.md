---
title: Method of Undetermined Coefficients
description: Learn about the method of undetermined coefficients, a technique for solving certain types of constant-coefficient nonhomogeneous linear ODEs commonly used in engineering for vibration systems and RLC circuit models.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - The **method of undetermined coefficients** applies to:
>   - Linear ODEs with **constant coefficients $a$ and $b$**
>   - Where input $r(x)$ consists of exponential functions, powers of $x$, $\cos$ or $\sin$, or sums and products of such functions
>   - $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Selection rules for the method of undetermined coefficients**  
>   - **(a) Basic rule**: If $r(x)$ in equation ($\ref{eqn:linear_ode_with_constant_coefficients}$) is one of the functions in the first column of the table, select $y_p$ from the same row in the second column, and determine the undetermined coefficients by substituting $y_p$ and its derivatives into equation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Modification rule**: If the term selected for $y_p$ is a solution of the corresponding homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$, multiply this term by $x$ (or by $x^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
>   - **(c) Sum rule**: If $r(x)$ is a sum of functions from the first column of the table, select $y_p$ as the sum of the corresponding functions from the second column.
>
> | Term in $r(x)$ | Choice for $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [Homogeneous Linear ODEs of Second Order](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogeneous Linear ODEs with Constant Coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Euler-Cauchy Equation](/posts/euler-cauchy-equation/)
- [Wronskian, Existence and Uniqueness of Solutions](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Nonhomogeneous Linear ODEs of Second Order](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Vector spaces, linear span (linear algebra)

## Method of Undetermined Coefficients
Consider a second-order nonhomogeneous linear ODE with $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

and the corresponding homogeneous ODE

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

As we saw in [Nonhomogeneous Linear ODEs of Second Order](/posts/nonhomogeneous-linear-odes-of-second-order/), to solve an initial value problem for the nonhomogeneous linear ODE ($\ref{eqn:nonhomogeneous_linear_ode}$), we need to find $y_h$ by solving the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) and then find a particular solution $y_p$ of equation ($\ref{eqn:nonhomogeneous_linear_ode}$) to obtain the general solution

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

So how do we find $y_p$? The general method for finding $y_p$ is the **method of variation of parameters**, but in some cases, we can apply the much simpler **method of undetermined coefficients**. This method is particularly useful in engineering for vibration systems and RLC circuit models.

The method of undetermined coefficients is suitable for **linear ODEs with constant coefficients $a$ and $b$** where the input $r(x)$ consists of exponential functions, powers of $x$, $\cos$ or $\sin$, or sums and products of such functions:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

The key insight of the method is that such forms of $r(x)$ have derivatives that are similar in form to themselves. To apply the method, we select $y_p$ that is similar in form to $r(x)$ but with undetermined coefficients that are determined by substituting $y_p$ and its derivatives into the given ODE. The rules for selecting an appropriate $y_p$ for practically important forms of $r(x)$ in engineering are as follows:

> **Selection rules for the method of undetermined coefficients**  
> **(a) Basic rule**: If $r(x)$ in equation ($\ref{eqn:linear_ode_with_constant_coefficients}$) is one of the functions in the first column of the table, select $y_p$ from the same row in the second column, and determine the undetermined coefficients by substituting $y_p$ and its derivatives into equation ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Modification rule**: If the term selected for $y_p$ is a solution of the corresponding homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$, multiply this term by $x$ (or by $x^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
> **(c) Sum rule**: If $r(x)$ is a sum of functions from the first column of the table, select $y_p$ as the sum of the corresponding functions from the second column.
>
> | Term in $r(x)$ | Choice for $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

This method has the advantage of being not only simple but also self-correcting. If you select $y_p$ incorrectly or choose too few terms, you'll reach a contradiction; if you choose too many terms, the coefficients of unnecessary terms will become zero, yielding the correct result. Even if something goes wrong when applying the method, you'll naturally notice it during the solution process, so you can confidently try with a reasonably appropriate $y_p$ following the selection rules above.

### Proof of the Sum Rule
Consider a nonhomogeneous linear ODE of the form $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Now consider two equations with the same left-hand side but with inputs $r_1$ and $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Suppose these equations have solutions ${y_p}_1$ and ${y_p}_2$, respectively. Denoting the left-hand side as $L[y]$, by the linearity of $L[y]$, for $y_p = {y_p}_1 + {y_p}_2$, we have:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Example: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
According to the basic rule (a), we set $y_p = Ce^{\gamma x}$ and substitute it into the given equation $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Case: $\gamma^2 + a\gamma + b \neq 0$
We can determine the undetermined coefficient $C$ and find $y_p$ as follows:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Case: $\gamma^2 + a\gamma + b = 0$
In this case, we need to apply the modification rule (b). First, using $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, let's find the roots of the characteristic equation of the homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

This gives us the basis for the homogeneous ODE:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Subcase: $\gamma \neq -a-\gamma$
Since the term $Ce^{\gamma x}$ we selected for $y_p$ is a solution of the corresponding homogeneous ODE but not a double root, according to the modification rule (b), we multiply it by $x$ to get $y_p = Cxe^{\gamma x}$.

Now we substitute this modified $y_p$ back into the given equation $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Subcase: $\gamma = -a-\gamma$
In this case, the term $Ce^{\gamma x}$ we selected for $y_p$ corresponds to a double root of the characteristic equation of the homogeneous ODE. According to the modification rule (b), we multiply it by $x^2$ to get $y_p = Cx^2 e^{\gamma x}$.

Now we substitute this modified $y_p$ back into the given equation $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extension of the Method: $r(x)$ as Products of Functions
Consider a nonhomogeneous linear ODE with $r(x) = k x^n e^{\alpha x}\cos(\omega x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

If $r(x)$ can be expressed as a sum and product of functions from the first column of the table (i.e., exponential functions, powers of $x$, $\cos$ or $\sin$), then there exists a solution $y_p$ that is a sum and product of functions from the second column of the table.

> For a rigorous proof, I'll use linear algebra, with sections marked with \* that can be skipped without losing the general understanding.
{: .prompt-tip }

### Definition of Vector Space $V$\*
For $r(x)$ of the form:
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

We can define a vector space $V$ such that $r(x) \in V$:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Derivatives of Basic Functions
The derivatives of the basic functions from the first column of the table are:
- Exponential function: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Polynomial function: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Trigonometric function: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

The derivatives of these functions can be expressed as <u>sums of the same types of functions</u>.

Therefore, if functions $f$ and $g$ are sums of these functions, for $r(x) = f(x)g(x)$, using the product rule:

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

where $f$, $f^{\prime}$, $f^{\prime\prime}$ and $g$, $g^{\prime}$, $g^{\prime\prime}$ can all be written as sums or constant multiples of exponential, polynomial, and trigonometric functions. Thus, $r^{\prime}(x) = (fg)^{\prime}$ and $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ can also be expressed as sums and products of these functions, just like $r(x)$.

### Invariance of $V$ Under Differential Operator $D$ and Linear Transformation $L$\*
Not only $r(x)$ itself, but also $r^{\prime}(x)$ and $r^{\prime\prime}(x)$ are linear combinations of terms of the form $x^k e^{\alpha x}\cos(\omega x)$ and $x^k e^{\alpha x}\sin(\omega x)$, so:

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

More generally, introducing the differential operator $D$ for all elements of the vector space $V$, *the vector space $V$ is closed under the differential operation $D$*. Therefore, if we denote the left-hand side of the given equation $y^{\prime\prime} + ay^{\prime} + by$ as $L[y]$, then *$V$ is invariant under $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Since $r(x) \in V$ and $V$ is invariant under $L$, there exists another element $y_p$ of $V$ such that $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Therefore, we can select an appropriate $y_p$ using undetermined coefficients $A_0, A_1, \dots, A_n$ and $K$, $M$ as a sum of all possible product terms:

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

According to the basic rule (a) and modification rule (b), we can determine the undetermined coefficients by substituting $y_p$ (or $xy_p$, $x^2y_p$) and its derivatives into the given equation. The degree $n$ is determined by the degree of $x$ in $r(x)$.

$\blacksquare$

> If the given input $r(x)$ contains different values of $\alpha_i$ and $\omega_j$, you should select $y_p$ to include all possible terms of the form $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ and $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ for each $\alpha_i$ and $\omega_j$.  
> The advantage of the method of undetermined coefficients is its simplicity, so if the ansatz becomes too complicated and this advantage is lost, it might be better to apply the method of variation of parameters instead.
{: .prompt-warning }

## Extension to Euler-Cauchy Equations
The method of undetermined coefficients can also be applied to [Euler-Cauchy equations](/posts/euler-cauchy-equation/):

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Change of Variables
As we saw in [transforming Euler-Cauchy equations to constant coefficient ODEs](/posts/euler-cauchy-equation/#transformation-to-homogeneous-linear-odes-with-constant-coefficients), with the substitution $x = e^t$:

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

The Euler-Cauchy equation can be transformed into a constant coefficient ODE:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

We can apply the [method of undetermined coefficients](#method-of-undetermined-coefficients) to equation ($\ref{eqn:substituted}$) to solve for $t$, and then use $t = \ln x$ to obtain the solution in terms of $x$.

### For $r(x)$ as Powers of $x$, Natural Logarithms, or Sums and Products of Such Functions
Particularly when the input $r(x)$ consists of powers of $x$, natural logarithms, or sums and products of such functions, we can directly select an appropriate $y_p$ using the following selection rules for Euler-Cauchy equations:

> **Selection rules for the method of undetermined coefficients: For Euler-Cauchy equations**  
> **(a) Basic rule**: If $r(x)$ in equation ($\ref{eqn:euler_cauchy}$) is one of the functions in the first column of the table, select $y_p$ from the corresponding row in the second column, and determine the undetermined coefficients by substituting $y_p$ and its derivatives into equation ($\ref{eqn:euler_cauchy}$).  
> **(b) Modification rule**: If the term selected for $y_p$ is a solution of the corresponding homogeneous ODE $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiply this term by $\ln{x}$ (or by $(\ln{x})^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
> **(c) Sum rule**: If $r(x)$ is a sum of functions from the first column of the table, select $y_p$ as the sum of the corresponding functions from the second column.
>
> | Term in $r(x)$ | Choice for $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

This allows us to find $y_p$ more quickly and easily for practically important forms of input $r(x)$, equivalent to what we would obtain through [change of variables](#change-of-variables). These selection rules for Euler-Cauchy equations can be derived from the [original selection rules](#method-of-undetermined-coefficients) by replacing $x$ with $\ln{x}$.
