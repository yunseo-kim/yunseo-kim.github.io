---
title: "二階非齊次線性常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)"
description: "本文將探討二階非齊次線性常微分方程式的通解形式，著重於其與對應的齊次線性常微分方程式解之間的關係，並證明通解的存在性與奇異解的不存在性。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 二階非齊次線性常微分方程式 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$ 的**通解(general solution)**：
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$：對應的齊次常微分方程式 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ 的通解 $y_h = c_1y_1 + c_2y_2$
>   - $y_p$：該非齊次常微分方程式的特解(particular solution)
> - 響應項 $y_p$ 僅由輸入 $r(x)$ 決定，對於相同的非齊次常微分方程式，即使初始條件不同，$y_p$ 也不會改變。非齊次常微分方程式的兩個特解之差，會是對應的齊次常微分方程式的解。
> - **通解的存在性**：若非齊次常微分方程式的係數 $p(x)$、$q(x)$ 與輸入函數 $r(x)$ 連續，則其通解必定存在。
> - **奇異解的不存在**：通解包含方程式的所有解（即不存在奇異解）。
{: .prompt-info }

## 先備知識
- [二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [朗斯基行列式(Wronskian)，解的存在性與唯一性](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## 二階非齊次線性常微分方程式的通解與特解
考慮二階非齊次線性常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

，其中 $r(x) \not\equiv 0$。在開放區間 $I$ 上，方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的**通解(general solution)**，是由此非齊次常微分方程式對應的齊次常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

的通解 $y_h = c_1y_1 + c_2y_2$ 與方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的特解 $y_p$ 的和

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

所構成。此外，在區間 $I$ 上，方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的**特解(particular solution)**，是透過為 $y_h$ 的任意常數 $c_1$ 和 $c_2$ 指定特定值，從方程式 ($\ref{eqn:general_sol}$) 得到的解。

也就是說，若在齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 中加入僅依賴於自變數 $x$ 的輸入 $r(x)$，則其響應中會增加一個對應的項 $y_p$，而這個增加的響應項 $y_p$ 僅由輸入 $r(x)$ 決定，與初始條件無關。我們稍後將會看到，若求方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意兩個解 $y_1$ 和 $y_2$ 的差（即，求對應於兩個不同初始條件的特解之差），與初始條件無關的 $y_p$ 部分會被消去，只剩下 ${y_h}_1$ 和 ${y_h}_2$ 的差，而根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，此差值亦為方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解。

## 非齊次常微分方程式的解與其對應的齊次常微分方程式解之間的關係
> **定理 1：非齊次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解與齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解之間的關係**  
> **(a)** 在某個開放區間 $I$ 上，非齊次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解 $y$ 與齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解 $\tilde{y}$ 的和，同樣是區間 $I$ 上方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解。特別地，方程式 ($\ref{eqn:general_sol}$) 是區間 $I$ 上方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解。  
> **(b)** 在區間 $I$ 上，非齊次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的兩個解之差，是區間 $I$ 上齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解。
{: .prompt-info }

### 證明
#### (a)
將方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 與 ($\ref{eqn:homogeneous_linear_ode}$) 的左式記為 $L[y]$。那麼，在區間 $I$ 上，對於方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意解 $y$ 與方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的任意解 $\tilde{y}$，下列關係成立。

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
在區間 $I$ 上，對於方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意兩個解 $y$ 與 $y^\*$，下列關係成立。

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## 非齊次常微分方程式的通解包含所有解
對於齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)，我們[已知其通解包含所有解](/posts/wronskian-existence-and-uniqueness-of-solutions/#通解包含所有解)。現在我們來證明，對於非齊次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)，同樣的結論也成立。

> **定理 2：非齊次常微分方程式的通解包含所有解**  
> 若方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的係數 $p(x)$、$q(x)$ 與輸入函數 $r(x)$ 在某個開放區間 $I$ 上連續，則在區間 $I$ 上，方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的所有解，都可以透過為方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的通解 ($\ref{eqn:general_sol}$) 中的 $y_h$ 的任意常數 $c_1$ 和 $c_2$ 指定適當的值來得到。
{: .prompt-info }

### 證明
令 $y^\*$ 為在 $I$ 上方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的某個解，並令 $x_0$ 為區間 $I$ 內的某個 $x$。根據[具有連續變數係數的齊次常微分方程式的通解存在性定理](/posts/wronskian-existence-and-uniqueness-of-solutions/#通解的存在性)，$y_h = c_1y_1 + c_2y_2$ 存在；此外，根據我們稍後將探討的**參數變換法(method of variation of parameters)**，$y_p$ 也存在，因此在區間 $I$ 上，方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的通解 ($\ref{eqn:general_sol}$) 存在。現在，根據前面證明的定理 [1(b)](#非齊次常微分方程式的解與其對應的齊次常微分方程式解之間的關係)，$Y = y^\* - y_p$ 是在區間 $I$ 上齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 的解，且在 $x_0$ 處滿足

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

。根據[初始值問題解的存在性與唯一性定理](/posts/wronskian-existence-and-uniqueness-of-solutions/#初始值問題解的存在性與唯一性定理)，在區間 $I$ 上，對於上述初始條件，存在一個唯一的特解 $Y$，此解可透過為 $y_h$ 的 $c_1$、$c_2$ 指定適當的值來得到。由於 $y^\* = Y + y_p$，我們證明了非齊次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意特解 $y^\*$ 都可以從通解 ($\ref{eqn:general_sol}$) 中得到。 $\blacksquare$
