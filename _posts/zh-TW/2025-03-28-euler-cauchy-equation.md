---
title: "歐拉-柯西方程式"
description: "本文將根據輔助方程式判別式的正負號，探討在不同情況下，歐拉-柯西方程式的通解會呈現何種形式。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 歐拉-柯西方程式：$x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **輔助方程式(auxiliary equation)**：$m^2 + (a-1)m + b = 0$
> - 根據輔助方程式的判別式 $(1-a)^2 - 4b$ 的正負號，通解的形式可分為下表三種情況：
>
> | 情況 | 輔助方程式的解 | 歐拉-柯西方程式的解的基底 | 歐拉-柯西方程式的通解 |
> | :---: | :---: | :---: | :---: |
> | I | 相異實根<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | 實重根<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | 共軛複數根<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## 先備知識
- [二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [常係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- 歐拉公式

## 輔助方程式 (auxiliary equation)
**歐拉-柯西方程式(Euler-Cauchy equation)** 是指具有給定常數 $a$ 和 $b$ 以及未知函數 $y(x)$ 的

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

形式的常微分方程式。將

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

代入方程式 ($\ref{eqn:euler_cauchy_eqn}$)

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

即

$$ [m(m-1) + am + b]x^m = 0 $$

由此可得輔助方程式

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

，而 $y=x^m$ 為歐拉-柯西方程式 ($\ref{eqn:euler_cauchy_eqn}$) 的解的充分必要條件是，$m$ 為輔助方程式 ($\ref{eqn:auxiliary_eqn}$) 的解。

求解二次方程式 ($\ref{eqn:auxiliary_eqn}$) 可得

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

，由此可知，兩個函數

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

是方程式 ($\ref{eqn:euler_cauchy_eqn}$) 的解。

如同在[常係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)中一樣，根據輔助方程式 ($\ref{eqn:auxiliary_eqn}$) 的判別式 $(1-a)^2 - 4b$ 的正負號，可將情況分為三種。
- $(1-a)^2 - 4b > 0$：相異實根
- $(1-a)^2 - 4b = 0$：實重根
- $(1-a)^2 - 4b < 0$：共軛複數根

## 根據輔助方程式判別式的正負號決定通解形式
### I. 相異實根 $m_1$ 與 $m_2$
在這種情況下，方程式 ($\ref{eqn:euler_cauchy_eqn}$) 在任意區間上的解的基底為

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

，其對應的通解為

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

。

### II. 實重根 $m = \cfrac{1-a}{2}$
在 $(1-a)^2 - 4b = 0$，即 $b=\cfrac{(1-a)^2}{4}$ 的情況下，二次方程式 ($\ref{eqn:auxiliary_eqn}$) 只有一個解 $m = m_1 = m_2 = \cfrac{1-a}{2}$，因此可得一個 $y = x^m$ 形式的解

$$ y_1 = x^{(1-a)/2} $$

，而歐拉-柯西方程式 ($\ref{eqn:euler_cauchy_eqn}$) 則變為

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

的形式。現在，我們利用[降階法](/posts/homogeneous-linear-odes-of-second-order/#降階法-reduction-of-order)來求另一個線性獨立的解 $y_2$。

若將欲求的第二個解設為 $y_2=uy_1$，可得

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

。

因為 $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$，所以

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

，積分後可得 $u = \ln x$。

因此 $y_2 = uy_1 = y_1 \ln x$，且因為 $y_1$ 和 $y_2$ 的商不為常數，所以它們是線性獨立的。對應於基底 $y_1$ 和 $y_2$ 的通解為

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

。

### III. 共軛複數根
在這種情況下，輔助方程式 ($\ref{eqn:auxiliary_eqn}$) 的解為 $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$，其對應的方程式 ($\ref{eqn:euler_cauchy_eqn}$) 的兩個複數解可利用 $x=e^{\ln x}$ 寫成如下形式：

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

令 $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ 並利用歐拉公式 $e^{it} = \cos{t} + i\sin{t}$，可知

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

，由此可得以下兩個實數解

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

。

由於這兩個解的商 $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$ 不為常數，因此它們是線性獨立的，故根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，它們構成了歐拉-柯西方程式 ($\ref{eqn:euler_cauchy_eqn}$) 的基底。由此可得以下的實數通解：

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

不過，在歐拉-柯西方程式中，輔助方程式為共軛複數根的情況，其實際重要性並不高。

## 轉換為常係數二階齊次線性常微分方程式
歐拉-柯西方程式可透過變數變換，轉換為[常係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)。

若以 $x = e^t$ 進行變換，則

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

，歐拉-柯西方程式 ($\ref{eqn:euler_cauchy_eqn}$) 將轉變為如下關於 $t$ 的常係數齊次線性常微分方程式：

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

將方程式 ($\ref{eqn:substituted}$) 應用[常係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)的解法對 $t$ 求解，然後利用 $t = \ln{x}$ 將得到的解轉換回關於 $x$ 的解，即可得到與[前述結果](#根據輔助方程式判別式的正負號決定通解形式)相同的結果。
