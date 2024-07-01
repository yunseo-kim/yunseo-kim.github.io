---
title: "Bernoulli Equation"
description: >-
  We explore the Bernoulli equation and its solution method, as well as the logistic equation, which is a special form of the Bernoulli equation.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
---

## Bernoulli Equation

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ is any real number)}  \tag{1} $$

The Bernoulli equation (1) is linear if $a=0$ or $a=1$, and nonlinear otherwise. However, it can be transformed into a linear equation through the following process.

Let $$ u(x)=[y(x)]^{1-a} $$

Differentiating this and substituting $y'$ from equation (1), we get

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

In the right-hand side, $y^{1-a}=u$, so we obtain the following linear first-order differential equation:

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Example: Logistic Equation
Solve the logistic equation (a special form of the Bernoulli equation).

$$ y'=Ay-By^2 \tag{3} $$

### Solution
Writing equation (3) in the form of equation (1):

$$ y'-Ay=-By^2 $$

Here, $a=2$, so $u=y^{1-a}=y^{-1}$. Differentiating this u and substituting $y'$ from equation (3):

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

The last term is $-Ay^{-1}=-Au$, so we obtain the following linear first-order differential equation:

$$ u'+Au=B $$

By the solution formula for [non-homogeneous linear first-order differential equations](/posts/Solution-of-First-Order-Linear-ODE/#nonhomogeneous-linear-ordinary-differential-equation), we can find the following general solution:

$$ u=ce^{-At}+B/A $$

Since $u=1/y$, we obtain the general solution of equation (3):

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$