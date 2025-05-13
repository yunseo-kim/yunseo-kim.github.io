---
title: 伯努利方程式(Bernoulli Equation)
description: 探討伯努利方程式及其特殊形式邏輯斯方程式的解法。
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## 伯努利方程式(Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{為任意實數)}  \tag{1} $$

伯努利方程式 (1) 在 $a=0$ 或 $a=1$ 時是線性的，其他情況則為非線性。然而，我們可以通過以下步驟將其轉換為線性方程式。

令 $$ u(x)=[y(x)]^{1-a} $$

對其進行微分，然後將式 (1) 中的 $y'$ 代入，得到：

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

在右邊，$y^{1-a}=u$，因此我們得到以下線性常微分方程：

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## 例題：邏輯斯方程式(Logistic Equation)
求解邏輯斯方程式（伯努利方程式的特殊形式）：

$$ y'=Ay-By^2 \tag{3} $$

### 解法
將式 (3) 改寫成式 (1) 的形式：

$$ y'-Ay=-By^2 $$

這裡 $a=2$，所以 $u=y^{1-a}=y^{-1}$。對這個 u 進行微分，並將式 (3) 中的 $y'$ 代入：

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

最後一項是 $-Ay^{-1}=-Au$，因此我們得到以下線性常微分方程：

$$ u'+Au=B $$

根據[非齊次線性常微分方程](/posts/Solution-of-First-Order-Linear-ODE/#非齊次線性常微分方程)的解法公式，我們可以得到以下通解：

$$ u=ce^{-At}+B/A $$

由於 $u=1/y$，因此我們可以得到式 (3) 的通解：

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$
