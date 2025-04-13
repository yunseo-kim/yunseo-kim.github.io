---
title: 二階齊次線性常微分方程（Homogeneous Linear ODEs of Second Order）
description: 了解二階線性常微分方程的定義和特徵，特別是在齊次線性常微分方程中成立的重要定理——疊加原理，以及由此產生的基底（basis）概念。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - 二階線性常微分方程的**標準形式**：$y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **係數（coefficients）**：函數 $p$、$q$
>   - **輸入（input）**：$r(x)$
>   - **輸出（output）**或**響應（response）**：$y(x)$
> - 齊次和非齊次
>   - **齊次（homogeneous）**：當以標準形式表示時，$r(x)\equiv0$的情況
>   - **非齊次（nonhomogeneous）**：當以標準形式表示時，$r(x)\not\equiv 0$的情況
> - **疊加原理（superposition principle）**：對於<u>齊次</u>線性常微分方程 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$，在開區間 $I$ 中任意兩個解的線性組合同樣是給定方程的解。也就是說，給定齊次線性常微分方程的任意解的和與常數倍同樣是該方程的解。
> - **基底（basis）**或**基本系統（fundamental system）**：在區間 $I$ 中線性獨立的齊次線性常微分方程解的對 $(y_1, y_2)$
> - **降階法（reduction of order）**：對於二階齊次常微分方程，如果能找到一個解，則可以通過解一階常微分方程來找到與這個解線性獨立的第二個解，即基底，這種方法稱為降階法
> - 降階法的應用：一般的二階常微分方程 $F(x, y, y^\prime, y^{\prime\prime})=0$，無論是線性還是非線性，在以下情況下都可以使用降階法降為一階：
>   - $y$ 沒有明確出現的情況
>   - $x$ 沒有明確出現的情況
>   - 齊次線性且已知一個解的情況
{: .prompt-info }

## Prerequisites
- [建模（Modeling）基本概念](/posts/Basic-Concepts-of-Modeling/)
- [分離變數法（Separation of Variables）](/posts/Separation-of-Variables/)
- [一階線性常微分方程的解法](/posts/Solution-of-First-Order-Linear-ODE/)

## 二階線性常微分方程
如果二階常微分方程可以寫成

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

的形式，則稱為**線性（linear）**，否則稱為**非線性（nonlinear）**。

當 $p$、$q$、$r$ 是關於 $x$ 的任意函數時，這個方程對 $y$ 及其導數是線性的。

式 ($\ref{eqn:standard_form}$) 這種形式稱為二階線性常微分方程的**標準形式（standard form）**。如果給定的二階線性常微分方程的第一項是 $f(x)y^{\prime\prime}$，則可以將方程兩邊除以 $f(x)$ 得到標準形式。

函數 $p$、$q$ 稱為**係數（coefficients）**，$r(x)$ 稱為**輸入（input）**，$y(x)$ 稱為**輸出（output）**或對輸入和初始條件的**響應（response）**。

### 齊次二階線性常微分方程
假設我們要解的式 ($\ref{eqn:standard_form}$) 的區間 $a<x<b$ 為 $J$。如果在式 ($\ref{eqn:standard_form}$) 中，對區間 $J$ 有 $r(x)\equiv 0$，則

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

這種情況稱為**齊次（homogeneous）**。

## 非齊次線性常微分方程
在區間 $J$ 中，如果 $r(x)\not\equiv 0$，則稱為**非齊次（nonhomogeneous）**。

## 疊加原理

$$ y = c_1y_1 + c_2y_2 \quad \text{（}c_1, c_2\text{為任意常數）}\tag{3}$$

這種形式的函數稱為 $y_1$ 和 $y_2$ 的**線性組合（linear combination）**。

此時，以下原理成立：

> **疊加原理（superposition principle）**  
> 對於齊次線性常微分方程 ($\ref{eqn:homogeneous_linear_ode}$)，在開區間 $I$ 中任意兩個解的線性組合同樣是式 ($\ref{eqn:homogeneous_linear_ode}$) 的解。也就是說，給定齊次線性常微分方程的任意解的和與常數倍同樣是該方程的解。
{: .prompt-info }

### 證明
假設 $y_1$ 和 $y_2$ 是區間 $I$ 中方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解。將 $y=c_1y_1+c_2y_2$ 代入式 ($\ref{eqn:homogeneous_linear_ode}$)，得到

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

這是一個恆等式。因此，$y$ 是區間 $I$ 中方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解。$\blacksquare$

> 請注意，疊加原理只適用於齊次線性常微分方程，不適用於非齊次線性常微分方程或非線性常微分方程。
{: .prompt-warning }

## 基底和通解
### 回顧一階常微分方程的主要概念
如我們在[建模（Modeling）基本概念](/posts/Basic-Concepts-of-Modeling/)中所見，一階常微分方程的初值問題（Initial Value Problem）由常微分方程和初始條件（initial condition）$y(x_0)=y_0$ 組成。初始條件用於確定給定常微分方程通解中的任意常數 $c$，由此確定的解稱為特解。現在讓我們將這些概念擴展到二階常微分方程。

### 初值問題和初始條件
二階齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 的**初值問題（initial value problem）**由給定的常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 和兩個**初始條件（initial conditions）**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

組成。這些條件用於確定常微分方程**通解（general solution）**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

中的兩個任意常數 $c_1$ 和 $c_2$。

### 線性獨立和線性相依
在這裡，讓我們簡單了解一下線性獨立和線性相依的概念。為了後面定義基底，我們需要理解這一點。  
如果兩個函數 $y_1$ 和 $y_2$ 在定義區間 $I$ 的所有點上滿足

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{且 }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

則稱這兩個函數 $y_1$ 和 $y_2$ 在區間 $I$ 上**線性獨立（linearly independent）**，否則稱 $y_1$ 和 $y_2$ **線性相依（linearly dependent）**。

如果 $y_1$ 和 $y_2$ 線性相依（即命題 ($\ref{eqn:linearly_independent}$) 不成立），則可以將 ($\ref{eqn:linearly_independent}$) 方程兩邊除以 $k_1 \neq 0$ 或 $k_2 \neq 0$，得到

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{或} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

這表明 $y_1$ 和 $y_2$ 成比例。

### 基底、通解、特解
回到主題，為了使式 ($\ref{eqn:general_sol}$) 成為通解，$y_1$ 和 $y_2$ 必須是方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解，同時在區間 $I$ 上不成比例且線性獨立（linearly independent）。滿足這些條件的、在區間 $I$ 上線性獨立的方程 ($\ref{eqn:homogeneous_linear_ode}$) 解的對（pair）$(y_1, y_2)$ 稱為式 ($\ref{eqn:homogeneous_linear_ode}$) 在區間 $I$ 上的解的**基底（basis）**或**基本系統（fundamental system）**。

通過使用初始條件來確定通解 ($\ref{eqn:general_sol}$) 中的兩個常數 $c_1$ 和 $c_2$，我們可以得到一個唯一的解，該解通過點 $(x_0, K_0)$ 並在該點的切線斜率為 $K_1$。這稱為常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 的**特解（particular solution）**。

如果式 ($\ref{eqn:homogeneous_linear_ode}$) 在開區間 $I$ 上連續，則它必定有通解，且這個通解包含所有可能的特解。也就是說，在這種情況下，方程 ($\ref{eqn:homogeneous_linear_ode}$) 不會有無法從通解得到的奇解（singular solution）。

## 降階法（reduction of order）
對於二階齊次常微分方程，如果能找到一個解，則可以通過解以下一階常微分方程來找到與這個解線性獨立的第二個解，即基底。這種方法稱為**降階法（reduction of order）**。

對於<u>不是 $f(x)y^{\prime\prime}$ 而是 $y^{\prime\prime}$ 的標準形式</u>的二階齊次常微分方程

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

假設我們在開區間 $I$ 中已知這個方程的一個解 $y_1$。

現在，我們將要尋找的第二個解設為 $y_2 = uy_1$，並得到

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

將這些代入方程，得到

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

將 $u^{\prime\prime}$、$u^{\prime}$、$u$ 各項分別收集並整理，得到

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

由於 $y_1$ 是給定方程的解，最後括號內的式子為 $0$，因此 $u$ 項消失，剩下關於 $u^{\prime}$ 和 $u^{\prime\prime}$ 的常微分方程。將這個剩餘的常微分方程兩邊除以 $y_1$，並令 $u^{\prime}=U$、$u^{\prime\prime}=U^{\prime}$，得到以下一階常微分方程：

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

[分離變數](/posts/Separation-of-Variables/)並積分，得到

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

兩邊取指數函數，最終得到

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

由於之前設 $U=u^{\prime}$，所以 $u=\int U dx$，因此我們要找的第二個解 $y_2$ 為

$$ y_2 = uy_1 = y_1 \int U dx $$

只要 $U>0$，$\cfrac{y_2}{y_1} = u = \int U dx$ 就不可能是常數，因此 $y_1$ 和 $y_2$ 構成解的基底。

### 降階法的應用
一般的二階常微分方程 $F(x, y, y^\prime, y^{\prime\prime})=0$，無論是線性還是非線性，在 $y$ 沒有明確出現、$x$ 沒有明確出現，或者如前所述是齊次線性且已知一個解的情況下，都可以使用降階法降為一階。

#### 當 $y$ 沒有明確出現時
對於 $F(x, y^\prime, y^{\prime\prime})=0$，令 $z=y^{\prime}$，可以降為關於 $z$ 的一階常微分方程 $F(x, z, z^{\prime})$。

#### 當 $x$ 沒有明確出現時
對於 $F(y, y^\prime, y^{\prime\prime})=0$，令 $z=y^{\prime}$，則 $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$，因此可以降為關於 $z$ 的一階常微分方程 $F(y,z,z^\prime)$，其中 $y$ 代替了獨立變數 $x$ 的角色。
