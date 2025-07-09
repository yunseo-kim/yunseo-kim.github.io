---
title: "待定係數法"
description: "本文將探討待定係數法。這是一種在工程學中，針對振動系統、RLC 電路模型等，能簡便地解決特定形式之常係數非齊次線性常微分方程式初值問題的實用解法。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **待定係數法**的適用對象：
>   - 具有**常數係數 $a$ 和 $b$**
>   - 且輸入項 $r(x)$ 由指數函數、$x$ 的冪次、$\cos$ 或 $\sin$，或這些函數的和與積所組成
>   - 的線性常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **待定係數法的選擇規則**  
>   - **(a) 基本規則(basic rule)**：若方程式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 中的 $r(x)$ 是下表第一欄中的任一函數，則選擇同一列的 $y_p$。將 $y_p$ 及其導數代入方程式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 以確定待定係數。  
>   - **(b) 修正規則(modification rule)**：若所選的 $y_p$ 項是方程式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 對應的齊次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的解，則將該項乘以 $x$（若該解對應於齊次常微分方程式特徵方程式的重根，則乘以 $x^2$）。  
>   - **(c) 疊加規則(sum rule)**：若 $r(x)$ 是下表第一欄中函數的和，則選擇第二欄對應列中函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## 先備知識
- [二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [常係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [歐拉-柯西方程式](/posts/euler-cauchy-equation/)
- [朗斯基行列式(Wronskian)，解的存在性與唯一性](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [二階非齊次線性常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)
- 向量空間、線性生成 (線性代數)

## 待定係數法
考慮 $r(x) \not\equiv 0$ 的二階非齊次線性常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

以及與此非齊次常微分方程式對應的齊次常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

。

根據先前在 [二階非齊次線性常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/) 中的探討，為了解決非齊次線性常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的初值問題，我們需要先解齊次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$) 求得 $y_h$，然後找到方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的一個特解 $y_p$，從而得到通解

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

。那麼，$y_p$ 該如何尋找呢？尋找 $y_p$ 的一般方法是**參數變異法(method of variation of parameters)**，但在某些情況下，可以應用更為簡單的**待定係數法(method of undetermined coefficients)**。此方法特別適用於振動系統和 RLC 電路模型，因此在工程學中被頻繁使用。

待定係數法適用於具有**常數係數 $a$ 和 $b$**，且輸入項 $r(x)$ 由指數函數、$x$ 的冪次、$\cos$ 或 $\sin$，或這些函數的和與積所組成的線性常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

。這類 $r(x)$ 的導數形式與其自身相似，這是待定係數法的核心思想。應用此方法時，我們選擇一個與 $r(x)$ 形式相似的 $y_p$，但其係數是待定的，這些係數可以通過將 $y_p$ 及其導數代入給定的常微分方程式來確定。對於在工程學中具有實際重要性的 $r(x)$ 形式，選擇適當 $y_p$ 的規則如下。

> **待定係數法的選擇規則**  
> **(a) 基本規則(basic rule)**：若方程式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 中的 $r(x)$ 是下表第一欄中的任一函數，則選擇同一列的 $y_p$。將 $y_p$ 及其導數代入方程式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 以確定待定係數。  
> **(b) 修正規則(modification rule)**：若所選的 $y_p$ 項是方程式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 對應的齊次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的解，則將該項乘以 $x$（若該解對應於齊次常微分方程式特徵方程式的重根，則乘以 $x^2$）。  
> **(c) 疊加規則(sum rule)**：若 $r(x)$ 是下表第一欄中函數的和，則選擇第二欄對應列中函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

此方法不僅簡便，還具有自我校正的優點。如果錯誤地選擇了 $y_p$ 或選擇了過少的項，將會導致矛盾；如果選擇了過多的項，不必要的項的係數將變為 $0$，最終仍能得到正確的結果。即使在應用待定係數法時出現錯誤，也能在解題過程中自然地發現，因此只要根據上述選擇規則選擇一個大致適當的 $y_p$，便可以放心地嘗試。

### 疊加規則的證明
考慮 $r(x) = r_1(x) + r_2(x)$ 形式的非齊次線性常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

。現在，考慮以下兩個具有相同左側但輸入項分別為 $r_1$ 和 $r_2$ 的方程式

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

，並假設它們的解分別為 ${y_p}_1$ 和 ${y_p}_2$。若將給定方程式的左側記為 $L[y]$，根據 $L[y]$ 的線性性質，對於 $y_p = {y_p}_1 + {y_p}_2$，滿足以下關係，因此疊加規則成立。

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## 範例：$y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
根據基本規則 (a)，設 $y_p = Ce^{\gamma x}$ 並代入給定方程式 $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$：

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### $\gamma^2 + a\gamma + b \neq 0$ 的情況
可以如下確定待定係數 $C$ 並求得 $y_p$。

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### $\gamma^2 + a\gamma + b = 0$ 的情況
在這種情況下，必須應用修正規則 (b)。首先，利用 $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ 來求齊次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的特徵方程式的根。

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

由此得到齊次常微分方程式的基底

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

。

#### $\gamma \neq -a-\gamma$ 的情況
所選的 $y_p = Ce^{\gamma x}$ 是對應齊次常微分方程式的非重根解，因此根據修正規則 (b)，將此項乘以 $x$，設 $y_p = Cxe^{\gamma x}$。

現在，將修正後的 $y_p$ 重新代入給定方程式 $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$：

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### $\gamma = -a-\gamma$ 的情況
在這種情況下，所選的 $y_p = Ce^{\gamma x}$ 是對應齊次常微分方程式的重根解，因此根據修正規則 (b)，將此項乘以 $x^2$，設 $y_p = Cx^2 e^{\gamma x}$。

現在，將修正後的 $y_p$ 重新代入給定方程式 $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$：

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## 待定係數法的擴展：$r(x)$ 為函數乘積形式
考慮 $r(x) = k x^n e^{\alpha x}\cos(\omega x)$ 形式的非齊次線性常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

。若 $r(x)$ 是指數函數 $e^{\alpha x}$、$x$ 的冪次 $x^m$、$\cos{\omega x}$ 或 $\sin{\omega x}$（此處假設為 $\cos$，不失一般性），或這些函數的和與積（即，可以用前述表格第一欄中函數的和與積來表示），我們將證明存在一個方程式的解 $y_p$，它也是同一表格第二欄中函數的和與積。

> 為求嚴謹證明，部分內容使用線性代數進行描述，並以 * 標示。跳過這些部分，只閱讀其餘內容，亦不影響對大致概念的理解。
{: .prompt-tip }

### 定義向量空間 $V$*
對於 $r(x)$

$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

，我們可以定義一個向量空間 $V$，使得 $r(x) \in V$：

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### 指數函數、多項式函數、三角函數的導數形式
前述表格第一欄中基本函數的導數形式如下：
- 指數函數：$\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- 多項式函數：$\cfrac{d}{dx}x^m = mx^{m-1}$
- 三角函數：$\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

對這些函數求導得到的導數，同樣可以表示為<u>同類函數的和</u>。

因此，若函數 $f$ 和 $g$ 是上述函數或其和，對 $r(x) = f(x)g(x)$ 應用乘法法則：

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

其中 $f$, $f^{\prime}$, $f^{\prime\prime}$ 和 $g$, $g^{\prime}$, $g^{\prime\prime}$ 都可以寫成指數函數、多項式函數、三角函數的和或常數倍的形式。因此，$r^{\prime}(x) = (fg)^{\prime}$ 和 $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ 也與 $r(x)$ 一樣，可以表示為這些函數的和與積。

### $V$ 對於微分運算 $D$ 與線性變換 $L$ 的不變性*
也就是說，不僅 $r(x)$ 本身，其導數 $r^{\prime}(x)$ 和 $r^{\prime\prime}(x)$ 也都是 $x^k e^{\alpha x}\cos(\omega x)$ 形式項和 $x^k e^{\alpha x}\sin(\omega x)$ 形式項的線性組合，因此

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

不限於 $r(x)$，若對先前定義的向量空間 $V$ 的所有元素引入微分算子 $D$，可以更一般地表示為，*向量空間 $V$ 在微分運算 $D$ 下是封閉的*。因此，若將給定方程式的左側 $y^{\prime\prime} + ay^{\prime} + by$ 記為 $L[y]$，則 *$V$ 在 $L$ 下是不變的(invariant)*。

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

因為 $r(x) \in V$ 且 $V$ 在 $L$ 下不變，所以存在 $V$ 的另一個元素 $y_p$ 滿足 $L[y_p] = r$。

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
因此，若使用待定係數 $A_0, A_1, \dots, A_n$ 和 $K, M$ 選擇一個適當的 $y_p$，使其成為所有可能的乘積項之和，如下所示，便可根據基本規則 (a) 和修正規則 (b)，將 $y_p$（或 $xy_p$, $x^2y_p$）及其導數代入給定方程式以確定待定係數。此處的 $n$ 根據 $r(x)$ 中 $x$ 的次數來決定。

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> 若給定的輸入項 $r(x)$ 包含多個不同的 $\alpha_i$ 和 $\omega_j$ 值，則選擇 $y_p$ 時必須確保涵蓋所有可能的 $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ 和 $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ 形式的項。  
> 待定係數法的優點在於簡便，因此若假設解(ansatz)變得過於複雜，使其優點黯然失色，那麼採用之後將會介紹的參數變異法可能會是更好的選擇。
{: .prompt-warning }

## 待定係數法的擴展：歐拉-柯西方程式
不僅是[常係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)，待定係數法也可以應用於[歐拉-柯西方程式](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

。

### 變數變換
透過[以 $x = e^t$ 進行變換，轉換為常係數二階齊次線性常微分方程式](/posts/euler-cauchy-equation/#轉換為常係數二階齊次線性常微分方程式)，可得

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

，我們之前已經知道，歐拉-柯西方程式可以轉換為以下關於 $t$ 的常係數齊次線性常微分方程式。

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

現在，對方程式 ($\ref{eqn:substituted}$) 同樣應用[前面探討的待定係數法](#待定係數法)對 $t$ 求解，最後利用 $t = \ln x$ 將解轉換回關於 $x$ 的解即可。

### $r(x)$ 為 $x$ 的冪次、自然對數或這些函數的和與積的情況
特別是當輸入項 $r(x)$ 由 $x$ 的冪次、自然對數或這些函數的和與積組成時，可以根據以下歐拉-柯西方程式專用的選擇規則，直接選擇適當的 $y_p$。

> **待定係數法的選擇規則：歐拉-柯西方程式專用**  
> **(a) 基本規則(basic rule)**：若方程式 ($\ref{eqn:euler_cauchy}$) 中的 $r(x)$ 是下表第一欄中的任一函數，則選擇同一列的 $y_p$。將 $y_p$ 及其導數代入方程式 ($\ref{eqn:euler_cauchy}$) 以確定待定係數。  
> **(b) 修正規則(modification rule)**：若所選的 $y_p$ 項是方程式 ($\ref{eqn:euler_cauchy}$) 對應的齊次常微分方程式 $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ 的解，則將該項乘以 $\ln{x}$（若該解對應於齊次常微分方程式特徵方程式的重根，則乘以 $(\ln{x})^2$）。  
> **(c) 疊加規則(sum rule)**：若 $r(x)$ 是下表第一欄中函數的和，則選擇第二欄對應列中函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

這樣，對於具有實際重要性的輸入項 $r(x)$，可以比透過[變數變換](#變數變換)更快、更簡便地找到與之相同的 $y_p$。將先前探討的[原始選擇規則](#待定係數法)中的 $x$ 替換為 $\ln{x}$，即可推導出此歐拉-柯西方程式專用的選擇規則。
