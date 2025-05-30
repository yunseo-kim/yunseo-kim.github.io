---
title: 二階非齊次線性常微分方程（Nonhomogeneous Linear ODEs of Second Order）
description: 了解二階非齊次線性常微分方程的一般解結構、特解與齊次方程解的關係，以及解的存在性與唯一性。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 二階非齊次線性常微分方程 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$ 的**一般解**:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: 齊次常微分方程 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ 的一般解 $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: 該非齊次常微分方程的特解
> - 響應項 $y_p$ 僅由輸入 $r(x)$ 決定，對於相同的非齊次常微分方程，即使初始條件不同，$y_p$ 也不會改變。非齊次常微分方程的兩個特解之差是對應齊次常微分方程的解。
> - **一般解的存在**: 若非齊次常微分方程的係數 $p(x)$、$q(x)$ 和輸入函數 $r(x)$ 連續，則一般解必定存在
> - **奇異解的不存在**: 一般解包含方程的所有解（即不存在奇異解）
{: .prompt-info }

## Prerequisites
- [二階齊次線性常微分方程（Homogeneous Linear ODEs of Second Order）](/posts/homogeneous-linear-odes-of-second-order/)
- [朗斯基行列式（Wronskian）、解的存在與唯一性](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## 二階非齊次線性常微分方程的一般解與特解
考慮二階非齊次線性常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

其中 $r(x) \not\equiv 0$。在開區間 $I$ 上，方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的**一般解**是由對應齊次常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

的一般解 $y_h = c_1y_1 + c_2y_2$ 與方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的特解 $y_p$ 的和

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

所組成。此外，區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的**特解**是通過為 $y_h$ 中的任意常數 $c_1$ 和 $c_2$ 指定特定值，從式 ($\ref{eqn:general_sol}$) 得到的解。

也就是說，當我們在齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 中加入僅依賴於自變量 $x$ 的輸入 $r(x)$ 時，會在響應中添加對應項 $y_p$，而這個額外的響應項 $y_p$ 與初始條件無關，僅由輸入 $r(x)$ 決定。如後文所示，若計算方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意兩個解 $y_1$ 和 $y_2$ 之差（即計算兩個不同初始條件下各自特解的差），則與初始條件無關的 $y_p$ 部分會被消除，只剩下 ${y_h}_1$ 和 ${y_h}_2$ 之差，而這根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)是方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解。

## 非齊次常微分方程的解與對應齊次常微分方程解的關係
> **定理 1: 非齊次常微分方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解與齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解的關係**  
> **(a)** 在某開區間 $I$ 上，非齊次常微分方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解 $y$ 與齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解 $\tilde{y}$ 之和是區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解。特別地，式 ($\ref{eqn:general_sol}$) 是區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的解。  
> **(b)** 區間 $I$ 上非齊次常微分方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的兩個解之差是區間 $I$ 上齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解。
{: .prompt-info }

### 證明
#### (a)
將方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 和 ($\ref{eqn:homogeneous_linear_ode}$) 的左側表示為 $L[y]$。則對於區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意解 $y$ 和方程 ($\ref{eqn:homogeneous_linear_ode}$) 的任意解 $\tilde{y}$，有：

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
對於區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意兩個解 $y$ 和 $y^\*$，有：

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## 非齊次常微分方程的一般解包含所有解
我們已知對於齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$)，[一般解包含所有解](/posts/wronskian-existence-and-uniqueness-of-solutions/#通解包含所有解)。現在我們來證明對於非齊次常微分方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 也成立相同的結論。

> **定理 2: 非齊次常微分方程的一般解包含所有解**  
> 若方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的係數 $p(x)$、$q(x)$ 和輸入函數 $r(x)$ 在某開區間 $I$ 上連續，則區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的所有解都可以通過為區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的一般解 ($\ref{eqn:general_sol}$) 中 $y_h$ 的任意常數 $c_1$ 和 $c_2$ 指定適當值來獲得。
{: .prompt-info }

### 證明
設 $y^\*$ 是區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的某個解，$x_0$ 是區間 $I$ 內的某點。根據[連續變數係數齊次常微分方程一般解存在定理](/posts/wronskian-existence-and-uniqueness-of-solutions/#通解的存在)，$y_h = c_1y_1 + c_2y_2$ 存在，而且通過後續將介紹的**參數變換法（method of variation of parameters）**，$y_p$ 也存在，因此區間 $I$ 上方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的一般解 ($\ref{eqn:general_sol}$) 存在。現在根據前面證明的定理 [1(b)](#非齊次常微分方程的解與對應齊次常微分方程解的關係)，$Y = y^\* - y_p$ 是區間 $I$ 上齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 的解，且在 $x_0$ 處有

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

根據[初值問題解的存在性與唯一性定理](/posts/wronskian-existence-and-uniqueness-of-solutions/#初值問題解的存在性與唯一性定理)，在區間 $I$ 上存在唯一的齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 特解 $Y$，可通過為 $y_h$ 中的 $c_1$、$c_2$ 指定適當值獲得，滿足上述初始條件。由於 $y^\* = Y + y_p$，我們已證明非齊次常微分方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的任意特解 $y^\*$ 可從一般解 ($\ref{eqn:general_sol}$) 獲得。$\blacksquare$
