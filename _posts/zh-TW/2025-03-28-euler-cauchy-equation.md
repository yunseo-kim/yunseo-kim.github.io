---
title: 歐拉-柯西方程
description: 根據輔助方程式的判別式符號，探討歐拉-柯西方程式的一般解在各種情況下呈現的形式。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 歐拉-柯西方程：$x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **輔助方程式(auxiliary equation)**：$m^2 + (a-1)m + b = 0$
> - 根據輔助方程式的判別式 $(1-a)^2 - 4b$ 的符號，一般解的形式可分為以下三種情況
>
> | 情況 | 輔助方程式的解 | 歐拉-柯西方程的解的基底 | 歐拉-柯西方程的一般解 |
> | :---: | :---: | :---: | :---: |
> | I | 不同實根<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | 實重根<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | 共軛複根<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerequisites
- [二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [具有常係數的二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- 歐拉公式

## 輔助方程 (auxiliary equation)
**歐拉-柯西方程(Euler-Cauchy equation)**是具有常數 $a$ 和 $b$，以及未知函數 $y(x)$ 的形式為

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

的常微分方程。將

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

代入式 ($\ref{eqn:euler_cauchy_eqn}$)，得到

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

即

$$ [m(m-1) + am + b]x^m = 0 $$

由此得到輔助方程

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

$y=x^m$ 成為歐拉-柯西方程 ($\ref{eqn:euler_cauchy_eqn}$) 解的充分必要條件是 $m$ 為輔助方程 ($\ref{eqn:auxiliary_eqn}$) 的解。

求解二次方程 ($\ref{eqn:auxiliary_eqn}$)，得到

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

因此，兩個函數

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

是方程 ($\ref{eqn:euler_cauchy_eqn}$) 的解。

與[具有常係數的二階齊次線性常微分方程](/posts/homogeneous-linear-odes-with-constant-coefficients/)類似，根據輔助方程 ($\ref{eqn:auxiliary_eqn}$) 的判別式 $(1-a)^2 - 4b$ 的符號，可分為三種情況：
- $(1-a)^2 - 4b > 0$：兩個不同的實根
- $(1-a)^2 - 4b = 0$：實重根
- $(1-a)^2 - 4b < 0$：共軛複根

## 根據輔助方程的判別式符號的一般解形式
### I. 兩個不同的實根 $m_1$ 和 $m_2$
在這種情況下，方程 ($\ref{eqn:euler_cauchy_eqn}$) 在任意區間上的解的基底為

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

相應的一般解為

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

### II. 實重根 $m = \cfrac{1-a}{2}$
當 $(1-a)^2 - 4b = 0$，即 $b=\cfrac{(1-a)^2}{4}$ 時，二次方程 ($\ref{eqn:auxiliary_eqn}$) 只有一個解 $m = m_1 = m_2 = \cfrac{1-a}{2}$，因此得到的 $y = x^m$ 形式的一個解為

$$ y_1 = x^{(1-a)/2} $$

而歐拉-柯西方程 ($\ref{eqn:euler_cauchy_eqn}$) 變為

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

現在使用[降階法](/posts/homogeneous-linear-odes-of-second-order/#降階法reduction-of-order)來找出線性獨立的另一個解 $y_2$。

設第二個解為 $y_2=uy_1$，則

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

由於 $\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$，所以

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

積分後得到 $u = \ln x$。

因此 $y_2 = uy_1 = y_1 \ln x$，且 $y_1$ 和 $y_2$ 線性獨立。基底 $y_1$ 和 $y_2$ 對應的一般解為

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

### III. 共軛複根
在這種情況下，輔助方程 ($\ref{eqn:auxiliary_eqn}$) 的解為 $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$，對應的方程 ($\ref{eqn:euler_cauchy_eqn}$) 的兩個複數解可以利用 $x=e^{\ln x}$ 寫為：

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

令 $t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$ 並使用歐拉公式 $e^{it} = \cos{t} + i\sin{t}$，得到

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

由此得到兩個實數解

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

這兩個解線性獨立，因此根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，歐拉-柯西方程 ($\ref{eqn:euler_cauchy_eqn}$) 的實數一般解為

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

不過，歐拉-柯西方程中輔助方程具有共軛複根的情況在實際應用中重要性較小。

## 轉換為具有常係數的二階齊次線性常微分方程
歐拉-柯西方程可以通過變數替換轉換為[具有常係數的二階齊次線性常微分方程](/posts/homogeneous-linear-odes-with-constant-coefficients/)。

令 $x = e^t$，則

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

歐拉-柯西方程 ($\ref{eqn:euler_cauchy_eqn}$) 轉換為關於 $t$ 的常係數齊次線性常微分方程：

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

使用[具有常係數的二階齊次線性常微分方程](/posts/homogeneous-linear-odes-with-constant-coefficients/)的解法求解方程 ($\ref{eqn:substituted}$)，然後利用 $t = \ln{x}$ 將解轉換回關於 $x$ 的形式，可以得到與[前面討論的結果](#根據輔助方程的判別式符號的一般解形式)相同的結果。
