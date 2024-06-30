---
title: "ベルヌーイ方程式(Bernoulli Equation)"
description: >-
  ベルヌーイ方程式と、ベルヌーイ方程式の特殊な形であるロジスティック方程式の解法を学ぶ。
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
---

## ベルヌーイ方程式(Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{は任意の実数)}  \tag{1} $$

ベルヌーイ方程式 (1)は $a=0$ または $a=1$の場合は線形であり、それ以外の場合は非線形である。しかし、以下の過程を経て線形に変換することができる。

$$ u(x)=[y(x)]^{1-a} $$

とおき、微分した後、式 (1)から $y'$を代入すると

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

を得る。右辺で $y^{1-a}=u$であるため、次の線形常微分方程式を得る。

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## 例題：ロジスティック方程式(Logistic Equation)
ロジスティック方程式（ベルヌーイ方程式の特殊な形）を解け。

$$ y'=Ay-By^2 \tag{3} $$

### 解法
式 (3)を式 (1)の形で書くと

$$ y'-Ay=-By^2 $$

となる。$a=2$なので $u=y^{1-a}=y^{-1}$である。この uを微分し、式 (3)から $y'$を代入すると

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

となる。最後の項は $-Ay^{-1}=-Au$なので、次の線形常微分方程式を得る。

$$ u'+Au=B $$

[非斉次線形常微分方程式](/posts/Solution-of-First-Order-Linear-ODE/#非斉次線形常微分方程式)の解の公式により、次の一般解を求めることができる。

$$ u=ce^{-At}+B/A $$

$u=1/y$なので、これから式 (3)の一般解

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$

を得る。