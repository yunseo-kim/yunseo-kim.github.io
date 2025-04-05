---
title: 具有常數係數的二階齊次線性常微分方程
description: 根據特徵方程的判別式符號，探討各種情況下常數係數齊次線性常微分方程的一般解形式。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - 具有常數係數的二階齊次線性常微分方程：$y^{\prime\prime} + ay^{\prime} + by = 0$
> - **特徵方程(characteristic equation)**：$\lambda^2 + a\lambda + b = 0$
> - 根據特徵方程的判別式 $a^2 - 4b$ 的符號，一般解的形式可分為三種情況，如下表所示
>
> | 情況 | 特徵方程的解 | 常微分方程解的基底 | 常微分方程的一般解 |
> | :---: | :---: | :---: | :---: |
> | I | 兩個不同實根<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | 實重根<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | 共軛複根<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [伯努利方程(Bernoulli Equation)](/posts/Bernoulli-Equation/)
- [二階齊次線性常微分方程 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- 歐拉公式

## 特徵方程 (characteristic equation)
讓我們考慮係數 $a$ 和 $b$ 為常數的二階齊次線性常微分方程

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

這種形式的方程在機械和電氣振盪中有重要的應用。

在之前的[伯努利方程(Bernoulli Equation)](/posts/Bernoulli-Equation/)中，我們求解了邏輯斯方程的一般解，根據那篇文章，具有常數係數 $k$ 的一階線性常微分方程

$$ y^\prime + ky = 0 $$

的解是指數函數 $y = ce^{-kx}$。（在該文章的方程(4)中，當 $A=-k$, $B=0$ 時）

因此，對於類似形式的方程($\ref{eqn:ode_with_constant_coefficients}$)，我們可以先嘗試

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

形式的解。

> 當然，這只是一個猜測，並不能保證一般解真的是這種形式。但是，只要我們能找到兩個線性獨立的解，根據[二階齊次線性常微分方程](/posts/homogeneous-linear-odes-of-second-order/#基底通解特解)中討論的[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，我們就能求出一般解。  
> 稍後我們會看到，在某些情況下[需要尋找其他形式的解](#ii-實重根-lambda---cfraca2)。
{: .prompt-info }

將式($\ref{eqn:general_sol}$)及其導數

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

代入方程($\ref{eqn:ode_with_constant_coefficients}$)，得到

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

因此，如果 $\lambda$ 是**特徵方程(characteristic equation)**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

的解，那麼指數函數($\ref{eqn:general_sol}$)就是常微分方程($\ref{eqn:ode_with_constant_coefficients}$)的解。求解二次方程($\ref{eqn:characteristic_eqn}$)，得到

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

因此，兩個函數

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

是方程($\ref{eqn:ode_with_constant_coefficients}$)的解。

> **特徵方程(characteristic equation)**和**輔助方程(auxiliary equation)**這兩個術語經常被混用，它們完全是同一個意思。使用哪一個術語都可以。
{: .prompt-tip }

現在，根據特徵方程($\ref{eqn:characteristic_eqn}$)的判別式 $a^2 - 4b$ 的符號，我們可以將情況分為三種：
- $a^2 - 4b > 0$：兩個不同的實根
- $a^2 - 4b = 0$：實重根
- $a^2 - 4b < 0$：共軛複根

## 根據特徵方程判別式符號的一般解形式
### I. 兩個不同實根 $\lambda_1$ 和 $\lambda_2$
在這種情況下，方程($\ref{eqn:ode_with_constant_coefficients}$)在任意區間上的解的基底是

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

因此，一般解為

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. 實重根 $\lambda = -\cfrac{a}{2}$
當 $a^2 - 4b = 0$ 時，二次方程($\ref{eqn:characteristic_eqn}$)只有一個解 $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$，因此我們只能得到一個形如 $y = e^{\lambda x}$ 的解

$$ y_1 = e^{-(a/2)x} $$

為了找到基底，我們需要找到與 $y_1$ 線性獨立的第二個解 $y_2$。

在這種情況下，我們可以使用之前學過的[降階法](/posts/homogeneous-linear-odes-of-second-order/#降階法reduction-of-order)。假設第二個解的形式為 $y_2=uy_1$，則

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

將這些代入方程($\ref{eqn:ode_with_constant_coefficients}$)，得到

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

整理 $u^{\prime\prime}$, $u^\prime$, $u$ 各項，得到

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

由於 $y_1$ 是方程($\ref{eqn:ode_with_constant_coefficients}$)的解，最後一個括號內的表達式為 $0$，且

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

所以第一個括號內的表達式也為 $0$。因此只剩下 $u^{\prime\prime}y_1 = 0$，從而 $u^{\prime\prime}=0$。積分兩次得到 $u = c_1x + c_2$，其中積分常數 $c_1$ 和 $c_2$ 可以是任意值，所以我們可以簡單地選擇 $c_1=1$, $c_2=0$，即 $u=x$。這樣 $y_2 = uy_1 = xy_1$，且 $y_1$ 和 $y_2$ 線性獨立，因此它們構成基底。所以，當特徵方程($\ref{eqn:characteristic_eqn}$)有重根時，方程($\ref{eqn:ode_with_constant_coefficients}$)在任意區間上的解的基底是

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

對應的一般解為

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. 共軛複根 $-\cfrac{1}{2}a + i\omega$ 和 $-\cfrac{1}{2}a - i\omega$
在這種情況下，$a^2 - 4b < 0$ 且 $\sqrt{-1} = i$，所以從式($\ref{eqn:lambdas}$)得到

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

定義實數 $\sqrt{b-\cfrac{1}{4}a^2} = \omega$。

有了這個定義，特徵方程($\ref{eqn:characteristic_eqn}$)的解是共軛複根 $\lambda = -\cfrac{1}{2}a \pm i\omega$，對應的方程($\ref{eqn:ode_with_constant_coefficients}$)的兩個複解為

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

但在這種情況下，我們也可以得到實數解的基底，方法如下。

利用歐拉公式(Euler formula)

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

以及將 $t$ 替換為 $-t$ 得到的

$$ e^{-it} = \cos t - i\sin t $$

將這兩個式子相加和相減，得到

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

對於具有實部 $r$ 和虛部 $it$ 的複變數 $z = r + it$，複指數函數 $e^z$ 可以用實函數 $e^r$, $\cos t$ 和 $\sin t$ 定義如下：

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

令 $r=-\cfrac{1}{2}ax$, $t=\omega x$，則可以寫成

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，上述複解的和與常數倍也是解。因此，將兩個等式相加並乘以 $\cfrac{1}{2}$，得到第一個實數解 $y_1$：

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

同樣，從第一個等式減去第二個等式並乘以 $\cfrac{1}{2i}$，得到第二個實數解 $y_2$：

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

由於 $\cfrac{y_1}{y_2} = \cot{\omega x}$ 不是常數，所以 $y_1$ 和 $y_2$ 在所有區間上線性獨立，因此構成方程($\ref{eqn:ode_with_constant_coefficients}$)實數解的基底。由此得到一般解

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{為任意常數)} \label{eqn:general_sol_3}\tag{13}$$
