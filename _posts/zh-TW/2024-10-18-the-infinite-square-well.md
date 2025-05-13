---
title: 一維無限方井(The 1D Infinite Square Well)
description: 探討量子力學基本概念的簡單而重要的代表性問題 - 一維無限方井問題。在這種理想情況下，我們求解粒子的第n個定態波函數ψ(x)和能量E，並了解ψ(x)的四個重要數學性質。最後，我們從中得出一般解Ψ(x,t)。
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 一維無限方井問題：
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{其他情況}
>   \end{cases}$$
> - 邊界條件：$ \psi(0) = \psi(a) = 0 $
> - 第$n$個定態的能量級別：$E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - 井內時間無關薛丁格方程的解：
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - 每個定態$\psi_n$的物理解釋：
>   - 長度為$a$的弦上出現的駐波形式
>   - **基態(ground state)**：具有最低能量的定態$\psi_1$
>   - **激發態(exited states)**：能量隨$n^2$成比例增加的其餘$n\geq 2$狀態
> - $\psi_n$的四個重要數學性質：
>   1. 如果勢能$V(x)$具有對稱性，則偶函數和奇函數會交替出現在井的中心
>   2. 隨著能量增加，每個連續狀態的**節點(node)**數量增加一個
>   3. 具有**正交歸一性(orthonomality)**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. 具有**完備性(completeness)**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - 薛丁格方程的一般解（定態的線性組合）：
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{其中係數 }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## 先備知識
- 連續機率分布和機率密度
- 正交性和歸一化（線性代數）
- 傅立葉級數和完備性（線性代數）
- [薛丁格方程和波函數](/posts/schrodinger-equation-and-the-wave-function/)
- [埃倫費斯特定理](/posts/ehrenfest-theorem/)
- [時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/)

## 給定的勢能條件
當勢能為

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{其他情況}
\end{cases} \tag{1}$$

時，這個勢能中的粒子在範圍$0<x<a$內是自由粒子，而在兩端（$x=0$和$x=a$）受到無限大的力而無法逃脫。在經典模型中，這被解釋為前後完全彈性碰撞的無限往復運動，且沒有非保守力作用。儘管這種勢能是極為人為和簡單的，但正因如此，它可以成為在後續學習量子力學時探討其他物理情況的有用參考案例，因此需要仔細檢查。

![無限勢井](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *圖片來源*
> - 作者：維基媒體用戶 [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - 授權：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## 模型和邊界條件設置
在井外，找到粒子的機率為$0$，因此$\psi(x)=0$。在井內，$V(x)=0$，所以[時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/)為

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

即

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ 其中 } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

的形式。

> 這裡假設$E\geq 0$。
{: .prompt-info }

這是描述經典**簡諧振盪器(simple harmonic oscillator)**的方程，其一般解為

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

其中$A$和$B$是任意常數，在求解特定問題的特解時，這些常數通常由問題給定的**邊界條件**決定。<u>對於$\psi(x)$，通常$\psi$和$d\psi/dx$都是連續的作為邊界條件，但在勢能為無窮大的地方，只有$\psi$是連續的。</u>

## 求解時間無關薛丁格方程

由於$\psi(x)$是連續的，所以

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

必須與井外的解連接。在式 ($\ref{eqn:psi_general_solution}$) 中，當$x=0$時

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

因此，代入 ($\ref{eqn:boundary_conditions}$) 得$B=0$。

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

那麼$\psi(a)=A\sin{ka}$，為了滿足式 ($\ref{eqn:boundary_conditions}$) 中的$\psi(a)=0$，要麼$A=0$（平凡解），要麼$\sin{ka}=0$。因此

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

這裡同樣，$k=0$是平凡解，會導致$\psi(x)=0$，無法歸一化，因此不是我們在這個問題中尋找的解。此外，由於$\sin(-\theta)=-\sin(\theta)$，負號可以被吸收到式 ($\ref{eqn:psi_without_B}$) 的$A$中，所以只考慮$ka>0$的情況也不會失去一般性。因此，$k$的可能解為

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

那麼$\psi_n=A\sin{k_n x}$且$\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$，將其代入式 ($\ref{eqn:t_independent_schrodinger_eqn}$)，可得到可能的$E$值如下：

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

與經典情況形成鮮明對比的是，無限方井中的量子粒子不能擁有任意能量，而必須擁有允許值中的一個。

> 能量的量子化是由時間無關薛丁格方程解的邊界條件所決定的。
{: .prompt-info }

現在我們可以通過歸一化$\psi$來求得$A$。

> 原本應該是歸一化$\Psi(x,t)$，但根據[時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/#1-它們是穩態stationary-states)的式 (11)，這等同於歸一化$\psi(x)$。
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

嚴格來說，這只決定了$A$的大小，但$A$的相位沒有任何物理意義，所以我們可以直接使用正實數平方根作為$A$。因此，井內的解為

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## 每個定態$\psi_n$的物理解釋
如式 ($\ref{eqn:psi_n}$) 所示，我們從時間無關薛丁格方程得到了每個能量級別$n$對應的無限多個解。其中前幾個解的圖形如下圖所示。

![最低四個量子態的初始波函數](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *圖片來源*
> - 作者：維基媒體用戶 [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - 授權：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

這些狀態呈現出長度為$a$的弦上的駐波形式，能量最低的$\psi_1$被稱為**基態(ground state)**，而能量隨$n^2$成比例增加的其餘$n\geq 2$狀態被稱為**激發態(exited states)**。

## $\psi_n$的四個重要數學性質
所有函數$\psi_n(x)$都具有以下四個重要性質。這四個性質非常強大，且不僅限於無限方井。第一個性質在勢能函數本身具有對稱性時總是成立，而第二、三、四個性質是不依賴勢能形狀的一般性質。

### 1. 偶函數和奇函數交替出現在井的中心。
對於正整數$n$，$\psi_{2n-1}$是偶函數，$\psi_{2n}$是奇函數。

### 2. 隨著能量增加，每個連續狀態的節點數量增加一個。
對於正整數$n$，$\psi_n$有$(n-1)$個**節點(node)**。

### 3. 這些狀態具有正交性(orthogonality)。

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

意味著它們是相互**正交(orthogonal)**的。

> 在我們現在討論的無限方井情況下，$\psi$是實數，所以不需要取$\psi_m$的共軛複數($^*$)，但為了適應其他情況，養成總是加上它的習慣是好的。
{: .prompt-tip }

#### 證明
當$m\neq n$時，

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

當$m=n$時，由於歸一化，這個積分等於$1$。使用**克羅內克函數(Kronecker delta)** $\delta_{mn}$，我們可以將正交性和歸一化一起表示為

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

這時我們說$\psi$是**正交歸一化(orthonormal)**的。

### 4. 這些函數具有完備性(completeness)。
任意其他函數$f(x)$可以表示為線性組合

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

這意味著這些函數是**完備(complete)**的。式 ($\ref{eqn:fourier_series}$) 是$f(x)$的**傅立葉級數(Fourier series)**，任意函數都可以這樣展開的定理被稱為**狄利克雷定理(Dirichlet's theorem)**。

## 使用傅立葉方法(Fourier's trick)求係數$c_n$
當給定$f(x)$時，我們可以利用上述的完備性(completeness)和正交歸一性(orthonormality)，使用所謂的**傅立葉方法(Fourier's trick)**來求係數$c_n$。將式 ($\ref{eqn:fourier_series}$) 兩邊乘以$\psi_m(x)^*$並積分，根據式 ($\ref{eqn:orthonomality}$) 和 ($\ref{eqn:kronecker_delta}$)，我們得到

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> 注意到由於克羅內克函數的作用，和式中除了$n=m$的項外，其他所有項都消失了。
{: .prompt-info }

因此，展開$f(x)$時的$n$階係數為

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## 求解時間相依薛丁格方程的一般解$\Psi(x,t)$
無限方井的每個定態根據['時間無關薛丁格方程'文章中的式 (10)](/posts/time-independent-schrodinger-equation/#1-它們是穩態stationary-states) 和我們先前得到的式 ($\ref{eqn:psi_n}$) 可以表示為

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

此外，我們在[時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/#3-時間相依薛丁格方程式的一般解是變數分離解的線性組合)中看到，薛丁格方程的一般解可以表示為定態的線性組合。因此，

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

現在我們只需要找到滿足以下條件的係數$c_n$：

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

根據我們先前討論的$\psi$的完備性，總是存在滿足上述條件的$c_n$，我們可以將$\Psi(x,0)$代入式 ($\ref{eqn:coefficients_n}$) 中的$f(x)$來求解：

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

當給定初始條件$\Psi(x,0)$時，我們使用式 ($\ref{eqn:calc_of_cn}$) 求解展開係數$c_n$，然後將其代入式 ($\ref{eqn:general_solution}$) 中求得$\Psi(x,t)$。之後，我們可以按照[埃倫費斯特定理](/posts/ehrenfest-theorem/)的過程計算任何我們感興趣的物理量。這種方法不僅適用於無限方井，還可以應用於任意勢能，只是$\psi$函數的形式和允許的能量級別的表達式會有所不同。

## 推導能量守恆($\langle H \rangle=\sum\|c_n\|^2E_n$)
利用$\psi(x)$的正交歸一性（式 [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]），我們來推導先前在[時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/#能量守恆)中簡略提到的能量守恆。由於$c_n$與時間無關，我們只需證明$t=0$時的情況即可。

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

此外，

$$ \hat{H}\psi_n = E_n\psi_n $$

因此我們得到：

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
