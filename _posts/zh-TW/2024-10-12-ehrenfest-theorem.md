---
title: 埃倫費斯特定理（Ehrenfest theorem）
description: 探討在量子力學中如何從波函數計算位置和動量的期望值，並將其擴展到任意力學變量Q(x,p)的期望值計算公式。從中推導出埃倫費斯特定理（Ehrenfest
  theorem）。
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## 先備知識
- 連續機率分布和機率密度
- [薛丁格方程和波函數](/posts/schrodinger-equation-and-the-wave-function/)

## 從波函數計算期望值
### 位置 $x$ 的期望值
處於 $\Psi$ 狀態的粒子的位置 $x$ 的期望值（expectation value）為

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

對於處於相同狀態 $\Psi$ 的足夠多數量的粒子，分別測量它們的位置後取測量結果的平均值，就會得到通過上述公式計算的 $\langle x \rangle$。

> 請注意，這裡所說的期望值並非對同一粒子重複測量得到的平均值，而是對具有相同狀態的系統的**系綜（ensemble）**進行測量結果的平均值。如果對同一粒子在短時間間隔內進行多次重複測量，由於在第一次測量時[波函數會發生坍塌（collapse）](/posts/schrodinger-equation-and-the-wave-function/#測量與波函數坍縮)，因此在後續的測量中將會持續得到相同的值。
{: .prompt-warning }

### 動量 $p$ 的期望值
由於 $\Psi$ 依賴於時間，隨著時間的推移，$\langle x \rangle$ 將會變化。此時，根據[薛丁格方程和波函數](/posts/schrodinger-equation-and-the-wave-function/)中的公式（8）和上面的公式（$\ref{eqn:x_exp}$），以下關係成立：

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> 在從公式（$\ref{eqn:dx/dt_1}$）到（$\ref{eqn:dx/dt_2}$）的過程中，以及從（$\ref{eqn:dx/dt_2}$）到（$\ref{eqn:dx/dt_3}$）的過程中，兩次應用了分部積分，並且由於 $\lim_{x\rightarrow\pm\infty}\Psi=0$，因此捨棄了邊界項（boundary term）。
{: .prompt-tip }

因此，我們得到**動量**的期望值如下：

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### 任意物理量 $Q(x,p)$ 的期望值
我們可以將前面得到的 $\langle x \rangle$ 和 $\langle p \rangle$ 的表達式寫成以下形式：

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

算符 $\hat x \equiv x$ 表示位置，算符 $\hat p \equiv -i\hbar(\partial/\partial x)$ 表示動量。對於動量算符 $\hat p$，擴展到三維空間時可以定義為 $\hat p \equiv -i\hbar\nabla$。

所有的經典力學變量都可以用位置和動量表示，因此我們可以將其擴展到任意物理量的期望值。要計算任意量 $Q(x,p)$ 的期望值，只需將所有的 $p$ 替換為 $-i\hbar\nabla$，然後將得到的算符放在 $\Psi^*$ 和 $\Psi$ 之間進行積分即可。

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

例如，動能 $T=\cfrac{p^2}{2m}$，因此

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

通過公式（$\ref{eqn:Q_exp}$），我們可以計算處於狀態 $\Psi$ 的粒子的任意物理量的期望值。

## 埃倫費斯特定理（Ehrenfest theorem）
### 計算 $d\langle p \rangle/dt$
讓我們對公式（$\ref{eqn:p_op}$）的兩邊對時間 $t$ 進行微分，以求得動量期望值的時間微分 $\cfrac{d\langle p \rangle}{dt}$。

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> 將[薛丁格方程和波函數](/posts/schrodinger-equation-and-the-wave-function/)中的公式（6）和（7）代入公式（$\ref{eqn:dp/dt_1}$），可以得到公式（$\ref{eqn:dp/dt_2}$）。在從公式（$\ref{eqn:dp/dt_3}$）到（$\ref{eqn:dp/dt_4}$）的過程中，應用了分部積分，並且如前所述，由於 $\lim_{x\rightarrow\pm\infty}\Psi=0$，因此捨棄了邊界項（boundary term）。
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### 埃倫費斯特定理與牛頓運動第二定律的關係
我們之前得到的以下兩個公式被稱為埃倫費斯特定理（Ehrenfest theorem）：

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

埃倫費斯特定理與經典力學中勢能和保守力之間的關係式 $F=\cfrac{dp}{dt}=-\nabla V$ 有相當相似的形式。
將兩個公式並排比較如下：

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [埃倫費斯特定理]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [牛頓運動第二定律]}$$

將埃倫費斯特定理的第二個公式 $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$（公式 [$\ref{eqn:ehrenfest_theorem_2nd}$]）的右側在 $\langle x \rangle$ 附近對 $x$ 進行泰勒展開：

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

在這裡，如果 $x-\langle x \rangle$ 足夠小，我們可以忽略第一項以外的所有高階項，並近似為

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

換句話說，**如果某個粒子的波函數在空間上非常接近某一點並呈現尖銳的分布（$\|\Psi\|^2$ 對 $x$ 的離散度非常小），那麼埃倫費斯特定理可以近似為經典力學中的牛頓運動第二定律。** 在宏觀尺度上，我們可以忽略波函數在空間上的擴散程度，實際上將粒子的位置視為一個點，因此牛頓運動第二定律成立。然而，在微觀尺度上，我們無法忽略量子力學效應，因此牛頓運動第二定律不再適用，而必須使用埃倫費斯特定理。
