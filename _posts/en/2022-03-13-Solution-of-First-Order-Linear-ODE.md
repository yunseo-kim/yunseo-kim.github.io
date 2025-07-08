---
title: Solution of First-Order Linear ODEs
description: Learn how to solve first-order linear ordinary differential equations using the integrating factor method, with a practical example of an RL circuit.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## First-Order Linear Ordinary Differential Equations
A first-order ordinary differential equation is called **linear** if it can be written algebraically in the form

$$ y'+p(x)y=r(x) \tag{1} $$

and **nonlinear** otherwise.

The form of equation (1) is called the **standard form** of a first-order linear ODE. If the first term of a given first-order linear ODE is $f(x)y'$, we can obtain the standard form by dividing both sides of the equation by $f(x)$.

In engineering, $r(x)$ is often called the **input**, and $y(x)$ is called the **output** or the **response** to the input (and initial conditions).

## Homogeneous Linear Ordinary Differential Equations
Let $J$ be an interval $a<x<b$ where we want to solve equation (1). If $r(x)\equiv 0$ for the interval $J$ in equation (1), we have

$$ y'+p(x)y=0 \tag{2}$$

and this is called **homogeneous**. In this case, we can use the [Separation of Variables](/posts/Separation-of-Variables/) method.

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

If $c=0$, we get the **trivial solution** $y(x)=0$.

## Nonhomogeneous Linear Ordinary Differential Equations
If $r(x)\not\equiv 0$ in the interval $J$, it is called **nonhomogeneous**. It is known that the nonhomogeneous linear ODE (1) has an integrating factor that depends only on $x$. This integrating factor $F(x)$ can be found using equation (11) from the [Method for Finding Integrating Factors](/posts/Exact-Differential-Equation-and-Integrating-Factor/#method-for-finding-integrating-factors), or it can be derived directly as follows.

Multiplying equation (1) by $F(x)$ gives

$$ Fy'+pFy=rF \tag{1*} $$

If

$$ pF=F' $$

then the left side of equation (1*) becomes the derivative $(Fy)'=F'y+Fy'$. Separating variables in $pF=F'$ gives $dF/F=p\ dx$. Integrating and letting $h=\int p\ dx$, we have

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Substituting this into equation (1*):

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrating this gives

$$ e^hy=\int e^hr\ dx + c $$
and dividing by $e^h$ gives the desired solution formula.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Here, the constant of integration in $h$ does not matter.

Since the only value in equation (4) that depends on the given initial condition is $c$, if we write equation (4) as the sum of two terms

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

we can see the following:

$$ \text{Total Output} = \text{Response to Input } r + \text{Response to Initial Condition} \tag{5} $$

## Example: RL Circuit
An $RL$ circuit consists of a battery with an electromotive force (EMF) of $E=48\textrm{V}$, a resistor with $R=11\mathrm{\Omega}$, and an inductor with $L=0.1\text{H}$. Assume the initial current is zero. Find the model for this $RL$ circuit and solve the resulting ordinary differential equation for the current $I(t)$.
> **Ohm's Law**  
> The current $I$ in the circuit causes a voltage drop of $RI$ across the resistor.
{: .prompt-info }

> **Faraday's Law of Electromagnetic Induction**  
> The current $I$ in the circuit causes a voltage drop of $LI'=L\ dI/dt$ across the inductor.
{: .prompt-info }

> **Kirchhoff's Voltage Law (KVL)**  
> The electromotive force applied to a closed circuit is equal to the sum of the voltage drops across all other elements in the circuit.
{: .prompt-info }

### Solution
According to the laws above, the model for the $RL$ circuit is $LI'+RI=E(t)$, and in standard form, it is:

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

We can solve this linear ODE by setting $x=t, y=I, p=R/L, h=(R/L)t$ in equation (4).

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Here, since $R/L=11/0.1=110$ and $E(t)=48$,

$$ I=\frac{48}{11}+ce^{-110t} $$

From the initial condition $I(0)=0$, we get $I(0)=E/R+c=0$, so $c=-E/R$. From this, we can find the particular solution:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
