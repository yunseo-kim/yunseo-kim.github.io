---
title: Solution of First-Order Linear Ordinary Differential Equations
description: Let's explore the method of solving first-order linear ordinary differential
  equations.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## First-Order Linear Ordinary Differential Equation
If a first-order ordinary differential equation can be algebraically brought to the form

$$ y'+p(x)y=r(x) \tag{1} $$

it is called **linear**, otherwise it is called **nonlinear**.

The form in equation (1) is called the **standard form** of a first-order linear ordinary differential equation. If the first term of a given first-order linear ordinary differential equation is $f(x)y'$, we can obtain the standard form by dividing both sides of the equation by $f(x)$.

In engineering, $r(x)$ is often called the **input**, and $y(x)$ is called the **output** or the **response** to the input (and initial conditions).

## Homogeneous Linear Ordinary Differential Equation
Let's say $J$ is some interval $a<x<b$ where we want to solve equation (1). If $r(x)\equiv 0$ for the interval $J$ in equation (1), then

$$ y'+p(x)y=0 \tag{2}$$

and this is called **homogeneous**. In this case, we can use the [method of separation of variables](/posts/Separation-of-Variables/).

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

When $c=0$, we get the **trivial solution** $y(x)=0$.

## Nonhomogeneous Linear Ordinary Differential Equation
If $r(x)\not\equiv 0$ in the interval $J$, it is called **nonhomogeneous**. It is known that the nonhomogeneous linear ordinary differential equation (1) has an integrating factor that depends only on $x$. This integrating factor $F(x)$ can be found using equation (11) from the [method of finding integrating factors](/posts/Exact-Differential-Equation-and-Integrating-Factor/#method-for-finding-integrating-factors), or it can be found directly as follows.

Multiplying equation (1) by $F(x)$, we get

$$ Fy'+pFy=rF \tag{1*} $$

If

$$ pF=F' $$

then the left side of equation (1*) becomes the derivative $(Fy)'=F'y+Fy'$. Separating variables in $pF=F'$, we get $dF/F=p\ dx$, and integrating with $h=\int p\ dx$, we have

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

Substituting this into equation (1*), we get

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

Integrating, we get

$$ e^hy=\int e^hr\ dx + c $$
and dividing by $e^h$, we obtain the desired solution formula.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

Here, the integration constant in $h$ does not matter.

In equation (4), the only value that depends on the given initial condition is $c$, so if we write equation (4) as the sum of two terms

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

we can see that:

$$ \text{Total output}=\text{Response to input }r+\text{Response to initial condition} \tag{5} $$

## Example: RL Circuit
Suppose an RL circuit consists of a battery with electromotive force $E=48\textrm{V}$, a resistor with $R=11\mathrm{\Omega}$, and an inductor with $L=0.1\text{H}$, and the initial current is 0. Construct the model of this RL circuit and solve the resulting ordinary differential equation for the current $I(t)$.
> **Ohm's law**  
> The current $I$ in the circuit causes a voltage drop $RI$ across the resistor.
{: .prompt-info }

> **Faraday's law of electromagnetic induction**  
> The current $I$ in the circuit causes a voltage drop $LI'=L\ dI/dt$ across the inductor.
{: .prompt-info }

> **Kirchhoff's Voltage Law (KVL)**  
> The electromotive force applied to a closed circuit is equal to the sum of the voltage drops across all other elements in the circuit.
{: .prompt-info }

### Solution
According to the above laws, the model of the RL circuit is $LI'+RI=E(t)$, and in standard form:

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

We can solve this linear ordinary differential equation using equation (4) with $x=t, y=I, p=R/L, h=(R/L)t$.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

Here, $R/L=11/0.1=110$ and $E(t)=48$, so

$$ I=\frac{48}{11}+ce^{-110t} $$

From the initial condition $I(0)=0$, we get $I(0)=E/R+c=0$, $c=-E/R$. From this, we can find the following particular solution:

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
