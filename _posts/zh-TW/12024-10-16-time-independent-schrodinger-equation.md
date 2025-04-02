---
title: 與時間無關的薛丁格方程式(Time-independent Schrödinger Equation)
description: 將薛丁格方程式的原始形式(時間相依薛丁格方程式) Ψ(x,t)應用變數分離法,推導出與時間無關的薛丁格方程式 ψ(x),並探討這種變數分離解在數學和物理上的意義和重要性。同時,我們還將研究如何通過變數分離解的線性組合來求得薛丁格方程式的一般解。
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - 變數分離解: $ \Psi(x,t) = \psi(x)\phi(t)$
> - 時間依賴性("wiggle factor"): $ \phi(t) = e^{-iEt/\hbar} $
> - 哈密頓算子(Hamiltonian): $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - 與時間無關的薛丁格方程式: $ \hat H\psi = E\psi $
> - 變數分離解的物理和數學意義及重要性:
>   1. 穩態(stationary states)
>   2. 具有明確的總能量值 $E$
>   3. 薛丁格方程式的一般解是變數分離解的線性組合
> - 時間相依薛丁格方程式的一般解: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Prerequisites
- 連續機率分布和機率密度
- [薛丁格方程式和波函數](/posts/schrodinger-equation-and-the-wave-function/)
- [埃倫費斯特定理](/posts/ehrenfest-theorem/)
- [變數分離法](/posts/Separation-of-Variables/)

## 使用變數分離法的推導
在[關於埃倫費斯特定理的文章](/posts/ehrenfest-theorem/)中,我們探討了如何使用波函數 $\Psi$ 來計算各種物理量。那麼,重要的是如何獲得這個波函數 $\Psi(x,t)$。通常,我們需要對給定的勢能 $V(x,t)$ 求解關於位置 $x$ 和時間 $t$ 的偏微分方程,即[薛丁格方程式](/posts/schrodinger-equation-and-the-wave-function/)。

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

如果勢能 $V$ 與時間 $t$ 無關,我們可以使用[變數分離法](/posts/Separation-of-Variables/)來解上述薛丁格方程式。讓我們考慮以下形式的解,它是只依賴於 $x$ 的函數 $\psi$ 和只依賴於 $t$ 的函數 $\phi$ 的乘積:

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

乍看之下,這似乎是一個非常受限的表達方式,可能只能求得整體解的一小部分。但事實上,這種解不僅具有重要意義,而且我們還可以通過特定方式將這些可分離的解相加來得到一般解。

對於可分離的解,我們有

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

將這些代入方程 ($\ref{eqn:schrodinger_eqn}$),我們可以將薛丁格方程式寫成:

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

兩邊除以 $\psi\phi$,我們得到左邊只是 $t$ 的函數,右邊只是 $x$ 的函數:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

為了使這個方程有解,兩邊必須等於一個常數。否則,如果我們保持變量 $t$ 和 $x$ 中的一個不變,而改變另一個,方程的一邊會改變而另一邊不變,等式就不再成立。因此,我們可以將左邊設為分離常數 $E$:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

這樣我們就得到了兩個常微分方程,一個是關於時間 $t$ 的:

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

另一個是關於空間 $x$ 的:

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

關於 $t$ 的常微分方程 ($\ref{eqn:ode_t}$) 很容易解。這個方程的一般解是 $ce^{-iEt/\hbar}$,但由於我們關心的是乘積 $\psi\phi$ 而不是 $\phi$ 本身,所以常數 $c$ 可以包含在 $\psi$ 中。因此我們得到:

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

關於 $x$ 的常微分方程 ($\ref{eqn:t_independent_schrodinger_eqn}$) 被稱為**與時間無關的薛丁格方程式(time-independent Schrödinger equation)**。要解這個方程,我們需要知道勢能 $V(x)$。

## 物理和數學意義
我們剛才使用變數分離法得到了只依賴於時間 $t$ 的函數 $\phi(t)$ 和與時間無關的薛丁格方程式 ($\ref{eqn:t_independent_schrodinger_eqn}$)。雖然原始的**時間相依薛丁格方程式(time-dependant Schrödinger equation)** ($\ref{eqn:schrodinger_eqn}$) 的大多數解不能表示為 $\psi(x)\phi(t)$ 的形式,但與時間無關的薛丁格方程式形式之所以重要,是因為其解具有以下三個特性:

### 1. 它們是穩態(stationary states)。
波函數

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

本身依賴於 $t$,但機率密度

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

中的時間依賴性被抵消,因此與時間無關。

> 對於可規範化的解,分離常數 $E$ 必須是實數。
>
> 如果我們將式 ($\ref{eqn:separation_of_variables}$) 中的 $E$ 設為複數 $E_0+i\Gamma$（$E_0$, $\Gamma$ 為實數）,則
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> 但如我們在[薛丁格方程式和波函數](/posts/schrodinger-equation-and-the-wave-function/#波函數的規範化normalization)中所討論的,
> $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ 應該是與時間無關的常數,因此 $\Gamma=0$。$\blacksquare$
{: .prompt-info }

在計算任何物理量的期望值時也會發生同樣的情況,[埃倫費斯特定理](/posts/ehrenfest-theorem/)中的式 (8) 變為

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

因此所有期望值都是時間的常數。特別地,由於 $\langle x \rangle$ 是常數,所以 $\langle p \rangle=0$。

### 2. 它們具有一個明確的總能量值 $E$,而不是一個機率分布範圍。
在經典力學中,總能量（動能加上勢能）被稱為**哈密頓量(Hamiltonian)**,定義為

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

因此,將 $p$ 替換為 $-i\hbar(\partial/\partial x)$,我們得到量子力學中的哈密頓算子(Hamiltonian operator):

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

因此,與時間無關的薛丁格方程式 ($\ref{eqn:t_independent_schrodinger_eqn}$) 可以寫成

$$ \hat H \psi = E\psi \tag{15}$$

哈密頓量的期望值為:

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

此外,

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

成立,因此

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

因此,哈密頓量 $H$ 的方差為

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

這意味著,當測量變數分離解的總能量時,總是得到固定值 $E$。

### 3. 時間相依薛丁格方程式的一般解是變數分離解的線性組合。

與時間無關的薛丁格方程式 ($\ref{eqn:t_independent_schrodinger_eqn}$) 有無限多個解 $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$。我們將它們表示為 \{$\psi_n(x)$\}。對於每一個解,都存在一個對應的分離常數 $E_1,E_2,E_3,\dots=$\{$E_n$\},因此對於每個**可能的能量級別**,都有一個對應的波函數。

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

時間相依薛丁格方程式 ($\ref{eqn:schrodinger_eqn}$) 具有這樣的性質:任意兩個解的線性組合也是一個解。因此,一旦我們找到變數分離解,我們就可以立即得到更一般形式的解:

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

所有時間相依薛丁格方程式的解都可以寫成上述形式,現在剩下的工作就是找到適當的常數 $c_1, c_2, \dots$ 以滿足問題中給定的初始條件,從而得到我們想要的特解。換句話說,只要我們能夠解出與時間無關的薛丁格方程式,接下來求解時間相依薛丁格方程式的一般解就變得相對簡單。

> 變數分離解 
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> 的所有機率和期望值都與時間無關,是穩態,但式 ($\ref{eqn:general_solution}$) 中的一般解並不具有這種性質。
{: .prompt-warning }

## 能量守恆
在一般解 ($\ref{eqn:general_solution}$) 中,係數 \{$c_n$\} 的絕對值平方 $\|c_n\|^2$ 在物理上表示當測量處於該狀態($\Psi$)的粒子的能量時,得到 $E_n$ 值的機率。因此,這些機率的總和應該為 1:

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

哈密頓量的期望值為:

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

在這裡,每個穩態的能量級別 $E_n$ 和係數 \{$c_n$\} 都與時間無關,因此測量到特定能量 $E_n$ 的機率以及哈密頓量 $H$ 的期望值都是與時間無關的常數。
