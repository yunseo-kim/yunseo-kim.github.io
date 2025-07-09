---
title: "Method of Undetermined Coefficients"
description: "Explore the method of undetermined coefficients, a powerful technique for solving specific nonhomogeneous linear ODEs with constant coefficients, widely used in engineering for models like vibrating systems and RLC circuits."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Method of Undetermined Coefficients** is applicable to:
>   - Linear ODEs $y^{\prime\prime} + ay^{\prime} + by = r(x)$
>   - with **constant coefficients $a$ and $b$**,
>   - and where the input $r(x)$ is an exponential function, a power of $x$, a cosine or sine, or sums and products of such functions.
> - **Choice Rules for the Method of Undetermined Coefficients**  
>   - **(a) Basic Rule**: If $r(x)$ in Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$) is one of the functions in the first column of the table, choose the corresponding $y_p$ from the same row and determine its undetermined coefficients by substituting $y_p$ and its derivatives into Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Modification Rule**: If a term in your choice for $y_p$ is a solution of the corresponding homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$, multiply this term by $x$ (or by $x^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
>   - **(c) Sum Rule**: If $r(x)$ is a sum of functions in the first column of the table, choose for $y_p$ the sum of the functions in the corresponding rows of the second column.
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
- Vector Spaces, Linear Span (Linear Algebra)

## Method of Undetermined Coefficients
Consider a second-order nonhomogeneous linear ordinary differential equation where $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

and its corresponding homogeneous ordinary differential equation

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

As we saw in [Nonhomogeneous Linear ODEs of Second Order](/posts/nonhomogeneous-linear-odes-of-second-order/), to solve an initial value problem for the nonhomogeneous linear ODE ($\ref{eqn:nonhomogeneous_linear_ode}$), we must first solve the homogeneous ODE ($\ref{eqn:homogeneous_linear_ode}$) to find $y_h$, then find a particular solution $y_p$ of Eq. ($\ref{eqn:nonhomogeneous_linear_ode}$) to obtain the general solution

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

So, how can we find $y_p$? A general method for finding $y_p$ is the **method of variation of parameters**, but in some cases, a much simpler method, the **method of undetermined coefficients**, can be applied. It is a frequently used method in engineering, especially as it can be applied to models of vibrating systems and RLC electrical circuits.

The method of undetermined coefficients is suitable for linear ODEs with **constant coefficients $a$ and $b$**, and where the input $r(x)$ is an exponential function, a power of $x$, a cosine or sine, or sums and products of such functions:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

The key to the method of undetermined coefficients is that an $r(x)$ of this form has derivatives that are similar in form to itself. To apply this method, we choose a $y_p$ that is similar in form to $r(x)$ but has unknown coefficients, which are determined by substituting $y_p$ and its derivatives into the given ODE. For forms of $r(x)$ that are practically important in engineering, the rules for choosing an appropriate $y_p$ are as follows.

> **Choice Rules for the Method of Undetermined Coefficients**  
> **(a) Basic Rule**: If $r(x)$ in Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$) is one of the functions in the first column of the table, choose the corresponding $y_p$ from the same row and determine its undetermined coefficients by substituting $y_p$ and its derivatives into Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Modification Rule**: If a term in your choice for $y_p$ is a solution of the corresponding homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$, multiply this term by $x$ (or by $x^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
> **(c) Sum Rule**: If $r(x)$ is a sum of functions in the first column of the table, choose for $y_p$ the sum of the functions in the corresponding rows of the second column.
>
> | Term in $r(x)$ | Choice for $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

This method has the advantage of being not only simple but also self-correcting. If you choose $y_p$ incorrectly or with too few terms, you will arrive at a contradiction. If you choose too many terms, the coefficients of the unnecessary terms will turn out to be $0$, leading to the correct result. Even if something goes wrong while applying the method, you will naturally notice it during the solution process. Therefore, as long as you choose a reasonably appropriate $y_p$ according to the choice rules above, you can try it without much hesitation.

### Proof of the Sum Rule
Consider a nonhomogeneous linear ODE of the form $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Now, let's assume that the following two equations, with the same left-hand side but with inputs $r_1$ and $r_2$, have particular solutions ${y_p}_1$ and ${y_p}_2$, respectively.

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

If we denote the left-hand side of the given equation as $L[y]$, then due to the linearity of $L[y]$, the sum rule holds because the following is satisfied for $y_p = {y_p}_1 + {y_p}_2$.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Example: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
According to the basic rule (a), we set $y_p = Ce^{\gamma x}$ and substitute it into the given equation $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Case where $\gamma^2 + a\gamma + b \neq 0$
We can determine the undetermined coefficient $C$ and find $y_p$ as follows.

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Case where $\gamma^2 + a\gamma + b = 0$
In this case, we must apply the modification rule (b). First, let's find the roots of the characteristic equation of the homogeneous ODE $y^{\prime\prime} + ay^{\prime} + by = 0$ by using the fact that $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

From this, we obtain the basis for the homogeneous ODE:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Case where $\gamma \neq -a-\gamma$
Since the chosen $y_p = Ce^{\gamma x}$ is a solution of the corresponding homogeneous ODE but not a double root, we multiply this term by $x$ according to the modification rule (b) and set $y_p = Cxe^{\gamma x}$.

Now, substituting the modified $y_p$ back into the given equation $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Case where $\gamma = -a-\gamma$
In this case, the chosen $y_p = Ce^{\gamma x}$ corresponds to a double root of the characteristic equation of the homogeneous ODE. Therefore, according to the modification rule (b), we multiply this term by $x^2$ and set $y_p = Cx^2 e^{\gamma x}$.

Now, substituting the modified $y_p$ back into the given equation $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extension of the Method: $r(x)$ as a Product of Functions
Consider a nonhomogeneous linear ODE where $r(x)$ is of the form $k x^n e^{\alpha x}\cos(\omega x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

If we assume $r(x)$ is a product of functions like an exponential function $e^{\alpha x}$, a power of $x$ like $x^m$, and a cosine or sine function like $\cos{\omega x}$ or $\sin{\omega x}$ (here we assume cosine without loss of generality), or a sum of such products (i.e., it can be expressed as a sum and product of functions from the first column of the previous table), we will show that a solution $y_p$ exists which is a sum and product of functions from the second column of the same table.

> For a rigorous proof, some parts are described using linear algebra and are marked with an asterisk (*). You can skip these parts and still get a general understanding.
{: .prompt-tip }

### Defining the Vector Space $V$*
For an $r(x)$ of the form
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

we can define a vector space $V$ such that $r(x) \in V$ as follows:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Derivative Forms of Exponential, Polynomial, and Trigonometric Functions
The derivative forms of the basic functions presented in the first column of the previous table are as follows.
- Exponential function: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Polynomial function: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Trigonometric functions: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

The derivatives obtained by differentiating these functions are also expressed as a <u>sum of the same kinds of functions</u>.

Therefore, if functions $f$ and $g$ are the functions above or their sums, applying the product rule to $r(x) = f(x)g(x)$ gives

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

and here, $f$, $f^{\prime}$, $f^{\prime\prime}$ and $g$, $g^{\prime}$, $g^{\prime\prime}$ can all be written as sums or constant multiples of exponential, polynomial, and trigonometric functions. Thus, $r^{\prime}(x) = (fg)^{\prime}$ and $r^{\prime\prime}(x) = (fg)^{\prime\prime}$, like $r(x)$, can also be expressed as sums and products of these functions.

### Invariance of $V$ under the Differential Operator $D$ and Linear Transformation $L$*
That is, not only $r(x)$ itself, but also $r^{\prime}(x)$ and $r^{\prime\prime}(x)$ are linear combinations of terms of the form $x^k e^{\alpha x}\cos(\omega x)$ and $x^k e^{\alpha x}\sin(\omega x)$, so

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Not limiting this to just $r(x)$, if we introduce the differential operator $D$ for all elements of the previously defined vector space $V$ to express this more generally, *the vector space $V$ is closed under the differentiation operation $D$*. Therefore, if we denote the left-hand side of the given equation, $y^{\prime\prime} + ay^{\prime} + by$, as $L[y]$, then *$V$ is invariant under $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Since $r(x) \in V$ and $V$ is invariant under $L$, there exists another element $y_p \in V$ that satisfies $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Therefore, if we choose an appropriate $y_p$ as a sum of all possible product terms using undetermined coefficients $A_0, A_1, \dots, A_n$ and $K, M$ as follows, we can determine the undetermined coefficients by substituting $y_p$ (or $xy_p$, $x^2y_p$) and its derivatives into the given equation, according to the basic rule (a) and the modification rule (b). Here, $n$ should be determined according to the degree of $x$ in $r(x)$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> If the given input $r(x)$ includes several different values of $\alpha_i$ and $\omega_j$, you must choose $y_p$ to include all possible terms of the form $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ and $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ for each $\alpha_i$ and $\omega_j$ value.  
> The advantage of the method of undetermined coefficients is its simplicity. If the ansatz becomes too complicated and this advantage is lost, it might be better to use the method of variation of parameters, which will be discussed later.
{: .prompt-warning }

## Extension of the Method: Euler-Cauchy Equation
The method of undetermined coefficients can be utilized not only for [homogeneous linear ODEs with constant coefficients](/posts/homogeneous-linear-odes-with-constant-coefficients/) but also for the [Euler-Cauchy equation](/posts/euler-cauchy-equation/):

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Change of Variables
By [substituting $x = e^t$ to transform it into a homogeneous linear ODE with constant coefficients](/posts/euler-cauchy-equation/#transformation-to-a-homogeneous-linear-ode-with-constant-coefficients), we get

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

which, as we have seen before, allows us to convert the Euler-Cauchy equation into the following homogeneous linear ODE with constant coefficients in terms of $t$.

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Now, we can apply the [previously discussed method of undetermined coefficients](#method-of-undetermined-coefficients) to Eq. ($\ref{eqn:substituted}$) to solve for $t$, and finally, use $t = \ln x$ to find the solution in terms of $x$.

### Case where $r(x)$ is a power of $x$, a natural logarithm, or a sum/product of such functions
In particular, if the input $r(x)$ consists of powers of $x$, natural logarithms, or sums and products of such functions, an appropriate $y_p$ can be chosen directly according to the following choice rules for the Euler-Cauchy equation.

> **Choice Rules for the Method of Undetermined Coefficients: For Euler-Cauchy Equations**  
> **(a) Basic Rule**: If $r(x)$ in Eq. ($\ref{eqn:euler_cauchy}$) is one of the functions in the first column of the table, choose the corresponding $y_p$ from the same row and determine its undetermined coefficients by substituting $y_p$ and its derivatives into Eq. ($\ref{eqn:euler_cauchy}$).  
> **(b) Modification Rule**: If a term in your choice for $y_p$ is a solution of the corresponding homogeneous ODE $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiply this term by $\ln{x}$ (or by $(\ln{x})^2$ if this solution corresponds to a double root of the characteristic equation of the homogeneous ODE).  
> **(c) Sum Rule**: If $r(x)$ is a sum of functions in the first column of the table, choose for $y_p$ the sum of the functions in the corresponding rows of the second column.
>
> | Term in $r(x)$ | Choice for $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

This way, for practically important forms of the input $r(x)$, we can find the same $y_p$ as obtained through the [change of variables](#change-of-variables) more quickly and easily. You can derive these choice rules for the Euler-Cauchy equation by substituting $\ln{x}$ for $x$ in the [original choice rules](#method-of-undetermined-coefficients) we looked at earlier.
