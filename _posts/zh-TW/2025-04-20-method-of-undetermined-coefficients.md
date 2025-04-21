---
title: 未定係數法
description: 讓我們來了解未定係數法，這是一種在工程中常用於解決振動系統、RLC電路模型等問題的方法，它可以簡單地解決特定形式的常係數非齊次線性常微分方程的初值問題。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **未定係數法**的適用對象：
>   - 具有**常數係數 $a$ 和 $b$**，且
>   - 輸入 $r(x)$ 由指數函數、$x$ 的冪次、$\cos$ 或 $\sin$，或這些函數的和與積組成的
>   - 線性常微分方程 $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **未定係數法的選擇規則**  
>   - **(a) 基本規則(basic rule)**：在方程 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 中，如果 $r(x)$ 是表格第一列中的某個函數，則選擇同一行的 $y_p$，並通過將 $y_p$ 及其導數代入方程 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 來確定未定係數。  
>   - **(b) 修正規則(modification rule)**：如果選擇的 $y_p$ 項是方程 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 對應的齊次常微分方程 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的解，則將該項乘以 $x$（或者如果該解對應於齊次常微分方程特徵方程的重根，則乘以 $x^2$）。  
>   - **(c) 和規則(sum rule)**：如果 $r(x)$ 是表格第一列中函數的和，則選擇第二列中對應行的函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [二階齊次線性常微分方程 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [朗斯基行列式(Wronskian)、解的存在與唯一性](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [二階非齊次線性常微分方程 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)

## 未定係數法
考慮 $r(x) \not\equiv 0$ 的二階非齊次線性常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

以及與此非齊次常微分方程對應的齊次常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

根據我們在[二階非齊次線性常微分方程 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)中所學，要解決非齊次線性常微分方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的初值問題，我們需要先解齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 得到 $y_h$，然後找到方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的一個特解 $y_p$，從而得到通解

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

那麼，如何找到 $y_p$ 呢？找到 $y_p$ 的一般方法是**參數變換法(method of variation of parameters)**，但在某些情況下，可以應用更簡單的**未定係數法(method of undetermined coefficients)**。特別是，這種方法適用於振動系統和RLC電路模型，因此在工程中經常使用。

未定係數法適用於具有**常數係數 $a$ 和 $b$**，且輸入 $r(x)$ 由指數函數、$x$ 的冪次、$\cos$ 或 $\sin$，或這些函數的和與積組成的線性常微分方程

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

這種形式的 $r(x)$ 具有與自身相似形式的導數，這是未定係數法的核心。為了應用未定係數法，我們選擇一個與 $r(x)$ 形式相似的 $y_p$，但其中包含未知係數，這些係數通過將 $y_p$ 及其導數代入給定的常微分方程來確定。對於工程中實際重要的 $r(x)$ 形式，選擇適當 $y_p$ 的規則如下：

> **未定係數法的選擇規則**  
> **(a) 基本規則(basic rule)**：在方程 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 中，如果 $r(x)$ 是表格第一列中的某個函數，則選擇同一行的 $y_p$，並通過將 $y_p$ 及其導數代入方程 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 來確定未定係數。  
> **(b) 修正規則(modification rule)**：如果選擇的 $y_p$ 項是方程 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 對應的齊次常微分方程 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的解，則將該項乘以 $x$（或者如果該解對應於齊次常微分方程特徵方程的重根，則乘以 $x^2$）。  
> **(c) 和規則(sum rule)**：如果 $r(x)$ 是表格第一列中函數的和，則選擇第二列中對應行的函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

這種方法不僅簡便，而且具有自校正性。如果選擇了錯誤的 $y_p$ 或選擇了太少的項，會導致矛盾；如果選擇了太多的項，不必要項的係數會變為 $0$，仍能得到正確的結果。即使在應用未定係數法時出現錯誤，也會在解題過程中自然發現，因此，只要按照上述選擇規則選擇了適當的 $y_p$，就可以放心嘗試。

### 和規則的證明
考慮形如 $r(x) = r_1(x) + r_2(x)$ 的非齊次線性常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

現在考慮具有相同左邊，但輸入分別為 $r_1$ 和 $r_2$ 的兩個方程

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

假設這兩個方程分別有解 ${y_p}_1$ 和 ${y_p}_2$。將給定方程的左邊表示為 $L[y]$，則由 $L[y]$ 的線性性質，對於 $y_p = {y_p}_1 + {y_p}_2$，有

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

因此和規則成立。

### 例題：$y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
根據基本規則 (a)，設 $y_p = Ce^{\gamma x}$ 並代入給定方程 $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$，得

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### 當 $\gamma^2 + a\gamma + b \neq 0$ 時
可以如下確定未定係數 $C$ 並求解 $y_p$：

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### 當 $\gamma^2 + a\gamma + b = 0$ 時
這種情況下需要應用修正規則 (b)。首先利用 $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ 求解齊次常微分方程 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的特徵方程的根。

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

由此得到齊次常微分方程的基

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

##### 當 $\gamma \neq -a-\gamma$ 時
由於我們選擇的 $y_p = Ce^{\gamma x}$ 是給定方程對應的齊次常微分方程的非重根解，根據修正規則 (b)，將此項乘以 $x$，得 $y_p = Cxe^{\gamma x}$。

現在將修正後的 $y_p$ 代入給定方程 $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$，得

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### 當 $\gamma = -a-\gamma$ 時
這種情況下，我們選擇的 $y_p = Ce^{\gamma x}$ 是給定方程對應的齊次常微分方程的重根解，根據修正規則 (b)，將此項乘以 $x^2$，得 $y_p = Cx^2 e^{\gamma x}$。

現在將修正後的 $y_p$ 代入給定方程 $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$，得

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
