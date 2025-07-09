---
title: "二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)"
description: "本文將探討二階線性常微分方程式的定義與特性，並深入理解在齊次線性常微分方程式中成立的重要定理——疊加原理，以及其衍生的基底(basis)概念。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 二階線性常微分方程式的**標準型(standard form)**: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **係數(coefficients)**: 函數 $p$, $q$
>   - **輸入(input)**: $r(x)$
>   - **輸出(output)** 或 **響應(response)**: $y(x)$
> - 齊次與非齊次
>   - **齊次(homogeneous)**: 以標準型表示時，$r(x)\equiv0$ 的情況
>   - **非齊次(nonhomogeneous)**: 以標準型表示時，$r(x)\not\equiv 0$ 的情況
> - **疊加原理(superposition principle)**: 對於<u>齊次</u>線性常微分方程式 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$，在開放區間 $I$ 上的任意兩個解的線性組合，同樣也是該方程式的解。也就是說，給定齊次線性常微分方程式的任意解之和與常數倍，也同樣是該方程式的解。
> - **基底(basis)** 或 **基礎系統(fundamental system)**: 在區間 $I$ 上，線性獨立的齊次線性常微分方程式的一對解 $(y_1, y_2)$
> - **降階法(reduction of order)**: 對於二階齊次常微分方程式，若能找到其中一個解，便可透過解一階常微分方程式，找出與此解線性獨立的第二個解，即基底。此方法稱為降階法。
> - 降階法的應用: 一般的二階常微分方程式 $F(x, y, y^\prime, y^{\prime\prime})=0$，無論是線性或非線性，在下列情況下皆可利用降階法降為一階：
>   - 方程式中未明確出現 $y$ 的情況
>   - 方程式中未明確出現 $x$ 的情況
>   - 方程式為齊次線性，且已知一個解的情況
{: .prompt-info }

## 先備知識
- [模型化（Modeling）的基本概念](/posts/Basic-Concepts-of-Modeling/)
- [變數分離法 (Separation of Variables)](/posts/Separation-of-Variables/)
- [一階線性常微分方程式的解法](/posts/Solution-of-First-Order-Linear-ODE/)

## 二階線性常微分方程式
若一個二階常微分方程式可寫成

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

的形式，則稱其為**線性(linear)**，否則稱為**非線性(nonlinear)**。

當 $p$、$q$、$r$ 為關於 $x$ 的任意函數時，此方程式對 $y$ 及其導數是線性的。

像方程式 ($\ref{eqn:standard_form}$) 這樣的形式稱為二階線性常微分方程式的**標準型(standard form)**。若給定的二階線性常微分方程式首項為 $f(x)y^{\prime\prime}$，可將方程式兩邊同除以 $f(x)$ 來得到標準型。

函數 $p$、$q$ 稱為**係數(coefficients)**，$r(x)$ 稱為**輸入(input)**，$y(x)$ 則稱為**輸出(output)** 或對輸入與初始條件的**響應(response)**。

### 齊次二階線性常微分方程式
假設我們要求解方程式 ($\ref{eqn:standard_form}$) 的區間為 $a<x<b$，記為 $J$。若在區間 $J$ 上 $r(x)\equiv 0$，則方程式為

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

此種情況稱為**齊次(homogeneous)**。

## 非齊次線性常微分方程式
在區間 $J$ 上 $r(x)\not\equiv 0$ 的情況，稱為**非齊次(nonhomogeneous)**。

## 疊加原理

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{為任意常數)}\tag{3}$$

此形式的函數稱為 $y_1$ 與 $y_2$ 的**線性組合(linear combination)**。

此時，下列定理成立：

> **疊加原理(superposition principle)**  
> 對於齊次線性常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)，在開放區間 $I$ 上的任意兩個解的線性組合，同樣也是方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解。也就是說，給定齊次線性常微分方程式的任意解之和與常數倍，也同樣是該方程式的解。
{: .prompt-info }

### 證明
令 $y_1$ 與 $y_2$ 為在區間 $I$ 上方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解。將 $y=c_1y_1+c_2y_2$ 代入方程式 ($\ref{eqn:homogeneous_linear_ode}$) 中：

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

結果為恆等式。因此，$y$ 在區間 $I$ 上是方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解。 $\blacksquare$

> 請注意，疊加原理僅適用於齊次線性常微分方程式，對於非齊次線性常微分方程式或非線性常微分方程式則不成立。
{: .prompt-warning }

## 基底與通解
### 回顧一階常微分方程式的主要概念
如同先前在 [模型化（Modeling）的基本概念](/posts/Basic-Concepts-of-Modeling/) 中所探討的，一階常微分方程式的初始值問題 (Initial Value Problem) 由一個常微分方程式和一個初始條件 (initial condition) $y(x_0)=y_0$ 組成。初始條件是用來決定給定常微分方程式通解中的任意常數 $c$，如此決定的解稱為特解。現在，我們將這些概念擴展到二階常微分方程式。

### 初始值問題與初始條件
對於二階齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的**初始值問題(initial value problem)**，是由給定的常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 和兩個**初始條件(initial conditions)**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

所組成。這些條件是用來決定常微分方程式的**通解(general solution)**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

中的兩個任意常數 $c_1$ 和 $c_2$。

### 線性獨立與線性相依
在此，我們先來了解線性獨立與線性相依的概念。為了在後面定義基底，有必要先理解這個概念。
若兩個函數 $y_1$ 和 $y_2$ 在其定義區間 $I$ 的所有點上滿足

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{且 }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

則稱這兩個函數 $y_1$ 和 $y_2$ 在區間 $I$ 上為**線性獨立(linearly independent)**。反之，則稱 $y_1$ 和 $y_2$ 為**線性相依(linearly dependent)**。

如果 $y_1$ 和 $y_2$ 是線性相依（即命題 ($\ref{eqn:linearly_independent}$) 不成立），則因為 $k_1 \neq 0$ 或 $k_2 \neq 0$，可以將方程式 ($\ref{eqn:linearly_independent}$) 的兩邊同除，寫成

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{或} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

的形式，由此可知 $y_1$ 和 $y_2$ 成比例。

### 基底、通解與特解
回到正題，要使方程式 ($\ref{eqn:general_sol}$) 成為通解，$y_1$ 和 $y_2$ 必須是方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解，同時在區間 $I$ 上不成比例且線性獨立 (linearly independent)。滿足這些條件，在區間 $I$ 上線性獨立的方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的一對解 (pair) $(y_1, y_2)$，稱為方程式 ($\ref{eqn:homogeneous_linear_ode}$) 在區間 $I$ 上的解的**基底(basis)** 或 **基礎系統(fundamental system)**。

利用初始條件來決定通解 ($\ref{eqn:general_sol}$) 的兩個常數 $c_1$ 和 $c_2$，可以得到一個通過點 $(x_0, K_0)$ 且在該點的切線斜率為 $K_1$ 的唯一解。此解稱為常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的**特解(particular solution)**。

若方程式 ($\ref{eqn:homogeneous_linear_ode}$) 在開放區間 $I$ 上連續，則其必有通解，且此通解包含所有可能的特解。也就是說，在這種情況下，方程式 ($\ref{eqn:homogeneous_linear_ode}$) 不會存在無法從通解中得到的奇異解 (singular solution)。

## 降階法 (reduction of order)
對於二階齊次常微分方程式，若能找到其中一個解，便可透過解一階常微分方程式，找出與此解線性獨立的第二個解，即基底。此方法稱為**降階法(reduction of order)**。

對於<u>首項為 $y^{\prime\prime}$ 而非 $f(x)y^{\prime\prime}$ 的標準型</u>二階齊次常微分方程式

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

，假設我們已知在開放區間 $I$ 上此方程式的一個解 $y_1$。

現在，我們設定欲求的第二個解為 $y_2 = uy_1$，並將

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

代入方程式中，可得

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

將 $u^{\prime\prime}$、$u^{\prime}$、$u$ 的各項分別整理後，可得

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

。然而，因為 $y_1$ 是給定方程式的解，最後一個括號內的式子等於 $0$，所以 $u$ 項消失，只剩下一個關於 $u^{\prime}$ 和 $u^{\prime\prime}$ 的常微分方程式。將此剩餘的常微分方程式兩邊同除以 $y_1$，並令 $u^{\prime}=U$、$u^{\prime\prime}=U^{\prime}$，即可得到以下的一階常微分方程式。

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

使用[變數分離法](/posts/Separation-of-Variables/)並積分可得

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

，兩邊取指數函數，最終可得

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

。前面我們設定 $U=u^{\prime}$，因此 $u=\int U dx$，故欲求的第二個解 $y_2$ 為

$$ y_2 = uy_1 = y_1 \int U dx $$

。因為 $\cfrac{y_2}{y_1} = u = \int U dx$ 在 $U>0$ 的情況下不為常數，所以 $y_1$ 和 $y_2$ 構成了解的基底。

### 降階法的應用
一般的二階常微分方程式 $F(x, y, y^\prime, y^{\prime\prime})=0$，無論是線性或非線性，只要滿足以下任一條件：$y$ 未明確出現、$x$ 未明確出現，或如前述為齊次線性且已知一解，即可利用降階法將其降為一階。

#### 方程式中未明確出現 $y$ 的情況
在 $F(x, y^\prime, y^{\prime\prime})=0$ 中，令 $z=y^{\prime}$，即可將其降為關於 $z$ 的一階常微分方程式 $F(x, z, z^{\prime})$。

#### 方程式中未明確出現 $x$ 的情況
在 $F(y, y^\prime, y^{\prime\prime})=0$ 中，令 $z=y^{\prime}$，則 $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$。因此，可將其降為一個以 $y$ 取代自變數 $x$、關於 $z$ 的一階常微分方程式 $F(y,z,z^\prime)$。
