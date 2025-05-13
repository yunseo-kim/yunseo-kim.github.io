---
title: 未定係數法
description: 特定形式的常係數非齊次線性常微分方程的初值問題可以簡單地解決，這種在工程中對振動系統、RLC電路模型等常用的解法稱為未定係數法。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **未定係數法**的適用對象:
>   - **具有常數係數 $a$ 和 $b$**，且
>   - 輸入 $r(x)$ 由指數函數、$x$ 的冪次、$\cos$ 或 $\sin$，或這些函數的和與積組成的
>   - 線性常微分方程 $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **未定係數法的選擇規則**  
>   - **(a) 基本規則(basic rule)**: 在式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 中，若 $r(x)$ 是表格第一列中的某個函數，則選擇同一行的 $y_p$，並通過將 $y_p$ 及其導數代入式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 來確定未定係數。  
>   - **(b) 變形規則(modification rule)**: 如果選擇的 $y_p$ 項是式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 對應的齊次常微分方程 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的解，則在此項上乘以 $x$（或如果此解對應於齊次常微分方程特徵方程的重根，則乘以 $x^2$）。  
>   - **(c) 和規則(sum rule)**: 如果 $r(x)$ 是表格第一列中函數的和，則選擇第二列中對應行的函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [具有常係數的二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [歐拉-柯西方程](/posts/euler-cauchy-equation/)
- [布朗斯基行列式(Wronskian)、解的存在與唯一性](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [二階非齊次線性常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)
- 向量空間、線性生成(線性代數)

## 未定係數法
考慮 $r(x) \not\equiv 0$ 的二階非齊次線性常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

以及與此非齊次常微分方程對應的齊次常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

根據[二階非齊次線性常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)中所述，要解決非齊次線性常微分方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的初值問題，我們需要先解齊次常微分方程 ($\ref{eqn:homogeneous_linear_ode}$) 得到 $y_h$，然後找到方程 ($\ref{eqn:nonhomogeneous_linear_ode}$) 的一個解 $y_p$，從而得到通解

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

那麼如何找到 $y_p$ 呢？找到 $y_p$ 的一般方法是**參數變換法(method of variation of parameters)**，但在某些情況下，可以應用更簡單的**未定係數法(method of undetermined coefficients)**。這種方法在工程中特別常用，因為它可以應用於振動系統和RLC電路模型。

未定係數法適用於**具有常數係數 $a$ 和 $b$**，且輸入 $r(x)$ 由指數函數、$x$ 的冪次、$\cos$ 或 $\sin$，或這些函數的和與積組成的線性常微分方程

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

這種形式的 $r(x)$ 具有與自身相似形式的導數，這是未定係數法的核心。為了應用未定係數法，我們選擇一個與 $r(x)$ 形式相似但具有未知係數的 $y_p$，然後通過將 $y_p$ 及其導數代入給定的常微分方程來確定這些未知係數。工程上實用且重要的 $r(x)$ 形式的選擇規則如下：

> **未定係數法的選擇規則**  
> **(a) 基本規則(basic rule)**: 在式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 中，若 $r(x)$ 是表格第一列中的某個函數，則選擇同一行的 $y_p$，並通過將 $y_p$ 及其導數代入式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 來確定未定係數。  
> **(b) 變形規則(modification rule)**: 如果選擇的 $y_p$ 項是式 ($\ref{eqn:linear_ode_with_constant_coefficients}$) 對應的齊次常微分方程 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的解，則在此項上乘以 $x$（或如果此解對應於齊次常微分方程特徵方程的重根，則乘以 $x^2$）。  
> **(c) 和規則(sum rule)**: 如果 $r(x)$ 是表格第一列中函數的和，則選擇第二列中對應行的函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

這種方法不僅簡便，還具有自我校正性。如果選擇了錯誤的 $y_p$ 或選擇了太少的項，會導致矛盾；如果選擇了太多的項，不必要項的係數會變為 $0$，仍能得到正確結果。即使在應用未定係數法時出現問題，也能在解題過程中自然發現，因此只要按照上述選擇規則選擇了合適的 $y_p$，就可以放心嘗試。

### 和規則的證明
考慮形如 $r(x) = r_1(x) + r_2(x)$ 的非齊次線性常微分方程

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

現在考慮具有相同左側但輸入分別為 $r_1$ 和 $r_2$ 的兩個方程

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

假設這兩個方程分別有解 ${y_p}_1$ 和 ${y_p}_2$。將給定方程的左側表示為 $L[y]$，則由於 $L[y]$ 的線性性質，對於 $y_p = {y_p}_1 + {y_p}_2$，我們有

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

因此和規則成立。

## 例題：$y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
根據基本規則 (a)，我們設 $y_p = Ce^{\gamma x}$ 並代入給定方程 $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$，得到

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### 當 $\gamma^2 + a\gamma + b \neq 0$ 時
我們可以確定未定係數 $C$ 並求解 $y_p$ 如下：

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### 當 $\gamma^2 + a\gamma + b = 0$ 時
在這種情況下，我們需要應用變形規則 (b)。首先，利用 $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$，求解對應的齊次常微分方程 $y^{\prime\prime} + ay^{\prime} + by = 0$ 的特徵方程的根。

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

由此得到齊次常微分方程的基底

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### 當 $\gamma \neq -a-\gamma$ 時
由於我們選擇的 $y_p = Ce^{\gamma x}$ 是對應齊次常微分方程的非重根解，根據變形規則 (b)，我們在此項上乘以 $x$，得到 $y_p = Cxe^{\gamma x}$。

將修改後的 $y_p$ 代入給定方程 $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$，得到

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### 當 $\gamma = -a-\gamma$ 時
在這種情況下，由於 $y_p = Ce^{\gamma x}$ 是對應齊次常微分方程的重根解，根據變形規則 (b)，我們在此項上乘以 $x^2$，得到 $y_p = Cx^2 e^{\gamma x}$。

將修改後的 $y_p$ 代入給定方程 $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$，得到

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## 未定係數法的擴展：函數乘積形式的 $r(x)$
考慮 $r(x) = k x^n e^{\alpha x}\cos(\omega x)$ 形式的非齊次線性常微分方程

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

如果 $r(x)$ 可以表示為指數函數 $e^{\alpha x}$、$x$ 的冪次 $x^m$、$\cos{\omega x}$ 或 $\sin{\omega x}$（這裡假設為 $\cos$，不失一般性），或這些函數的和與積，那麼我們將證明存在一個解 $y_p$，它也是表格第二列中函數的和與積。

> 為了嚴謹的證明，我使用了線性代數，這些部分用 \* 標記。跳過這些部分仍能大致理解。
{: .prompt-tip }

### 向量空間 $V$ 的定義\*
對於形如
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

的 $r(x)$，我們可以定義一個向量空間 $V$，使得 $r(x) \in V$：

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### 指數函數、多項式函數、三角函數的導數形式
表格第一列中基本函數的導數形式如下：
- 指數函數：$\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- 多項式函數：$\cfrac{d}{dx}x^m = mx^{m-1}$
- 三角函數：$\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

這些函數的導數仍然可以表示為<u>相同類型函數的和</u>。

因此，若函數 $f$ 和 $g$ 是上述函數或它們的和，則對於 $r(x) = f(x)g(x)$，應用乘積求導法則得到

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

其中 $f$、$f^{\prime}$、$f^{\prime\prime}$ 和 $g$、$g^{\prime}$、$g^{\prime\prime}$ 都可以表示為指數函數、多項式函數、三角函數的和或常數倍。因此 $r^{\prime}(x) = (fg)^{\prime}$ 和 $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ 也可以表示為這些函數的和與積。

### $V$ 對微分算子 $D$ 和線性變換 $L$ 的不變性\*
即，不僅 $r(x)$ 本身，而且 $r^{\prime}(x)$ 和 $r^{\prime\prime}(x)$ 也是 $x^k e^{\alpha x}\cos(\omega x)$ 形式項和 $x^k e^{\alpha x}\sin(\omega x)$ 形式項的線性組合，因此

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

不限於 $r(x)$，對於前面定義的向量空間 $V$ 中的所有元素，引入微分算子 $D$，更一般地表示為*向量空間 $V$ 對微分算子 $D$ 是封閉的*。因此，如果將給定方程的左側表示為 $y^{\prime\prime} + ay^{\prime} + by = L[y]$，則*$V$ 對 $L$ 是不變的*。

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

由於 $r(x) \in V$ 且 $V$ 對 $L$ 不變，因此存在 $V$ 中的另一個元素 $y_p$ 滿足 $L[y_p] = r$。

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
因此，我們可以選擇一個包含所有可能乘積項的和的 $y_p$，使用未定係數 $A_0, A_1, \dots, A_n$ 和 $K$、$M$ 如下：

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

其中 $n$ 根據 $r(x)$ 中 $x$ 的次數確定。然後，根據基本規則 (a) 和變形規則 (b)，將 $y_p$（或 $xy_p$、$x^2y_p$）及其導數代入給定方程來確定未定係數。

$\blacksquare$

> 如果給定的輸入 $r(x)$ 包含不同的 $\alpha_i$ 和 $\omega_j$ 值，則需要為每個 $\alpha_i$ 和 $\omega_j$ 值選擇包含所有可能的 $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ 和 $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ 形式項的 $y_p$。  
> 未定係數法的優點是簡便，如果假設解（ansatz）變得過於複雜而失去這一優勢，可能更適合使用後續將討論的參數變換法。
{: .prompt-warning }

## 未定係數法的擴展：歐拉-柯西方程
除了[具有常係數的二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)外，未定係數法也可用於[歐拉-柯西方程](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### 變數替換
通過[將 $x = e^t$ 替換為具有常係數的二階齊次線性常微分方程](/posts/euler-cauchy-equation/#轉換為具有常係數的二階齊次線性常微分方程)，我們有

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

這樣可以將歐拉-柯西方程轉換為關於 $t$ 的常係數齊次線性常微分方程：

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

現在可以對方程 ($\ref{eqn:substituted}$) 應用[前面討論的未定係數法](#未定係數法)，然後利用 $t = \ln x$ 將解轉換回關於 $x$ 的形式。

### 當 $r(x)$ 是 $x$ 的冪次、自然對數或這些函數的和與積時
特別是當輸入 $r(x)$ 是 $x$ 的冪次、自然對數或這些函數的和與積時，可以按照以下歐拉-柯西方程用選擇規則直接選擇適當的 $y_p$：

> **未定係數法的選擇規則：歐拉-柯西方程用**  
> **(a) 基本規則(basic rule)**: 在式 ($\ref{eqn:euler_cauchy}$) 中，若 $r(x)$ 是表格第一列中的某個函數，則選擇同一行的 $y_p$，並通過將 $y_p$ 及其導數代入式 ($\ref{eqn:euler_cauchy}$) 來確定未定係數。  
> **(b) 變形規則(modification rule)**: 如果選擇的 $y_p$ 項是式 ($\ref{eqn:euler_cauchy}$) 對應的齊次常微分方程 $x^2y^{\prime\prime} + axy^{\prime} + by = 0$ 的解，則在此項上乘以 $\ln{x}$（或如果此解對應於齊次常微分方程的特徵方程的重根，則乘以 $(\ln{x})^2$）。  
> **(c) 和規則(sum rule)**: 如果 $r(x)$ 是表格第一列中函數的和，則選擇第二列中對應行的函數的和作為 $y_p$。
>
> | $r(x)$ 的項 | $y_p(x)$ 的選擇 |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

這樣可以更快更簡便地找到與[變數替換](#變數替換)方法相同的 $y_p$。將[原始選擇規則](#未定係數法)中的 $x$ 替換為 $\ln{x}$ 可以導出這個歐拉-柯西方程用選擇規則。
