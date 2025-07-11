---
title: "常係數二階齊次線性常微分方程式"
description: "根據特徵方程式判別式的正負號，探討常係數齊次線性常微分方程式的通解在各種情況下所呈現的形式。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 常係數二階齊次線性常微分方程式：$y^{\prime\prime} + ay^{\prime} + by = 0$
> - **特徵方程式(characteristic equation)**：$\lambda^2 + a\lambda + b = 0$
> - 根據特徵方程式的判別式 $a^2 - 4b$ 的正負號，通解的形式可分為下表三種情況：
>
> | 情況 | 特徵方程式的根 | 常微分方程式的解的基底 | 常微分方程式的通解 |
> | :---: | :---: | :---: | :---: |
> | I | 相異實根<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | 實重根<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | 共軛複數根<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## 先備知識
- [白努利方程式(Bernoulli Equation)](/posts/Bernoulli-Equation/)
- [二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- 歐拉公式

## 特徵方程式 (characteristic equation)
我們來探討係數 $a$ 與 $b$ 為常數的二階齊次線性常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

這種形式的方程式在機械、電學振盪中有重要的應用。

先前在[白努利方程式(Bernoulli Equation)](/posts/Bernoulli-Equation/)中，我們曾求過羅吉斯方程式的通解。根據該文，具有常數係數 $k$ 的一階線性常微分方程式

$$ y^\prime + ky = 0 $$

的解是指數函數 $y = ce^{-kx}$。（在該篇文章的方程式 (4) 中，$A=-k$，$B=0$ 的情況）

因此，對於形式相似的方程式 ($\ref{eqn:ode_with_constant_coefficients}$)，我們也可以先嘗試

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

形式的解。

> 當然，這純屬猜測，完全無法保證通解必定是這種形式。但無論如何，只要能先找到兩個線性獨立的解，就可以像在[二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-of-second-order/#基底與通解)一文中所探討的，根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)求出通解。  
> 稍後將會看到，也有[需要求取其他形式解的情況](#ii-實重根-lambda--cfraca2)。
{: .prompt-info }

將方程式 ($\ref{eqn:general_sol}$) 及其導數

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

代入方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 中，可得

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

因此，若 $\lambda$ 是**特徵方程式(characteristic equation)**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

的根，則指數函數 ($\ref{eqn:general_sol}$) 就是常微分方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 的解。求解二次方程式 ($\ref{eqn:characteristic_eqn}$) 的根，可得

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

由此可知，兩個函數

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

是方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 的解。

> **特徵方程式(characteristic equation)** 與 **輔助方程式(auxiliary equation)** 這兩個術語經常混用，但它們的意義完全相同。使用哪個稱呼都無妨。
{: .prompt-tip }

現在，根據特徵方程式 ($\ref{eqn:characteristic_eqn}$) 的判別式 $a^2 - 4b$ 的正負號，可將情況分為三種。
- $a^2 - 4b > 0$: 相異實根
- $a^2 - 4b = 0$: 實重根
- $a^2 - 4b < 0$: 共軛複數根

## 根據特徵方程式判別式的正負號決定通解的形式
### I. 相異實根 $\lambda_1$ 與 $\lambda_2$
在這種情況下，方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 在任意區間上的解的基底為

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

其對應的通解為

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

### II. 實重根 $\lambda = -\cfrac{a}{2}$
當 $a^2 - 4b = 0$ 時，二次方程式 ($\ref{eqn:characteristic_eqn}$) 只有一個根 $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$，因此能得到的 $y = e^{\lambda x}$ 形式的解只有一個：

$$ y_1 = e^{-(a/2)x} $$

為了得到基底，必須找出與 $y_1$ 線性獨立的第二個不同形式的解 $y_2$。

在這種情況下，可以利用先前探討過的[降階法](/posts/homogeneous-linear-odes-of-second-order/#降階法-reduction-of-order)。將欲求的第二個解設為 $y_2=uy_1$，並將

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

代入方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 中，可得

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

將 $u^{\prime\prime}$、$u^\prime$、$u$ 的各項分別整理後，可得

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

在此，因為 $y_1$ 是方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 的解，所以最後一個括號內的式子為 $0$。又因為

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

所以第一個括號內的式子也為 $0$。因此只剩下 $u^{\prime\prime}y_1 = 0$，由此可得 $u^{\prime\prime}=0$。積分兩次可得 $u = c_1x + c_2$。積分常數 $c_1$ 和 $c_2$ 可以是任何值，因此我們可以簡單地選擇 $c_1=1$、$c_2=0$，令 $u=x$。如此一來，$y_2 = uy_1 = xy_1$。由於 $y_1$ 和 $y_2$ 線性獨立，它們構成了一組基底。因此，當特徵方程式 ($\ref{eqn:characteristic_eqn}$) 有重根時，方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 在任意區間上的解的基底為

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

其對應的通解為

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

### III. 共軛複數根 $-\cfrac{1}{2}a + i\omega$ 與 $-\cfrac{1}{2}a - i\omega$
在這種情況下，$a^2 - 4b < 0$ 且 $\sqrt{-1} = i$，因此從方程式 ($\ref{eqn:lambdas}$) 可得

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

在此，我們定義實數 $\sqrt{b-\cfrac{1}{4}a^2} = \omega$。

如上定義 $\omega$ 後，特徵方程式 ($\ref{eqn:characteristic_eqn}$) 的根為共軛複數根 $\lambda = -\cfrac{1}{2}a \pm i\omega$，其對應的方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 的兩個複數解為

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

不過，在這種情況下，我們仍然可以得到一組由實數解構成的基底，如下所示。

歐拉公式(Euler formula)

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

以及將上式中的 $t$ 替換為 $-t$ 所得到的

$$ e^{-it} = \cos t - i\sin t $$

將這兩個方程式相加及相減，可得：

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

具有實部 $r$ 和虛部 $it$ 的複變數 $z = r + it$ 的複指數函數 $e^z$，可以使用實函數 $e^r$、$\cos t$ 和 $\sin t$ 定義如下：

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

在此，若令 $r=-\cfrac{1}{2}ax$，$t=\omega x$，則可寫成：

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，上述複數解的和與常數倍也同樣是解。因此，將兩個等式相加，並在兩邊同乘以 $\cfrac{1}{2}$，即可得到第一個實數解 $y_1$：

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

同理，將第一個等式減去第二個等式，並在兩邊同乘以 $\cfrac{1}{2i}$，即可得到第二個實數解 $y_2$。

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

由於 $\cfrac{y_1}{y_2} = \cot{\omega x}$ 不是常數，因此 $y_1$ 和 $y_2$ 在所有區間上皆為線性獨立，從而構成了方程式 ($\ref{eqn:ode_with_constant_coefficients}$) 的實數解基底。由此可得通解

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{為任意常數)} \label{eqn:general_sol_3}\tag{13}$$
