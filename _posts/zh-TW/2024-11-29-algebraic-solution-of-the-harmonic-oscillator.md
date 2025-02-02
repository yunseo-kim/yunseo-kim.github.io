---
title: 諧振子（The Harmonic Oscillator）的代數解法
description: 建立量子力學中諧振子的薛丁格方程式，並探討該方程式的代數解法。從交換子、正則交換關係和階梯算符推導出任意定態的波函數和能量本徵值。
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---

## TL;DR
> - 如果振幅足夠小，任何振動都可以近似為簡諧振動（simple harmonic oscillation），因此簡諧振動在物理學中具有重要意義
> - 諧振子：$V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **交換子（commutator）**：
>   - 表示兩個算符之間不可交換程度的二元運算
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **正則交換關係（canonical commutation relation）**：$\left[\hat{x},\hat{p}\right] = i\hbar$
> - **階梯算符（ladder operators）**：
>   - $\hat{a}\_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$稱為**升階算符（raising operator）**，$\hat{a}\_-$稱為**降階算符（lowering operator）**
>   - 可以對任意定態提高或降低能量本徵值，因此只要找到時間無關薛丁格方程的一個解，就可以找到所有其他解
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - 第n個定態的波函數和能量本徵值：
>   - 基態（第0個定態）：
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - 第n個定態：
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$是$\hat{a}\_\pm$的**厄米共軛（hermitian conjugate）**和**伴隨算符（adjoint operator）**
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - 由此可以推導出以下性質：
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - 計算包含$\hat{x}$和$\hat{p}$冪次的物理量期望值的方法：
>   1. 利用階梯算符的定義將$\hat{x}$和$\hat{p}$表示為升階算符和降階算符
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. 使用上述$\hat{x}$和$\hat{p}$的表達式來表示要計算期望值的物理量
>   3. 利用$\left(\hat{a}\_\pm \right)^m$與$\psi\_{n\pm m}$成正比，因此與$\psi_n$正交而為$0$
>   4. 利用階梯算符的性質進行積分計算
{: .prompt-info }

## 先備知識
- [分離變數法](https://www.yunseo.kim/posts/Separation-of-Variables/)
- [薛丁格方程式和波函數](/posts/schrodinger-equation-and-the-wave-function/)
- [埃倫費斯特定理](/posts/ehrenfest-theorem/)
- [時間無關薛丁格方程式](/posts/time-independent-schrodinger-equation/)
- [一維無限方井](/posts/the-infinite-square-well/)
- 厄米共軛（hermitian conjugate）、伴隨算符（adjoint operator）

## 模型設定
### 經典力學中的諧振子
經典諧振子的典型例子是質量為$m$的物體懸掛在彈性係數為$k$的彈簧上的運動（忽略摩擦）。
這種運動遵循**胡克定律（Hooke's law）**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

這個方程的解是

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

其中

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

是振動的角頻率。位置$x$的勢能是

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

呈拋物線形狀。

在現實中，完美的諧振子是不存在的。即使是我們剛剛舉例的彈簧，如果過度拉伸，也會超過彈性極限而斷裂或產生永久變形，事實上，在達到那個點之前，它就已經不能精確地遵循胡克定律了。儘管如此，諧振子在物理學中仍然很重要，因為任何任意的勢能在極小值（local minimum）附近都可以近似為拋物線形狀。將任意勢能$V(x)$在極小點附近進行泰勒展開：

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

現在，由於給$V(x)$加上任意常數對力沒有任何影響，所以我們可以從中減去$V(x_0)$，並且由於$x_0$是極小點，所以$V^\prime(x_0)=0$，在假設$(x-x_0)$足夠小的情況下忽略高階項，我們得到：

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

這與有效彈性係數$k=V^{\prime\prime}(x_0)$的諧振子在點$x_0$附近的運動一致\*。換句話說，如果振幅足夠小，任何振動都可以近似為簡諧振動（simple harmonic oscillation）。

> \* 假設$V(x)$在$x_0$處有極小值，因此這裡$V^{\prime\prime}(x_0) \geq 0$。極少數情況下$V^{\prime\prime}(x_0)=0$，這種運動不能近似為簡諧振動。
{: .prompt-info }

### 量子力學中的諧振子
量子力學諧振子問題是解決勢能為

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

的薛丁格方程。諧振子的[時間無關薛丁格方程式](/posts/time-independent-schrodinger-equation/)是

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

解決這個問題有兩種完全不同的方法。一種是使用**冪級數（power series method）**的解析方法（analytic method），另一種是使用**階梯算符（ladder operators）**的代數方法（algebraic method）。代數方法更快更簡單，但學習解析解法也是必要的。這裡我們將討論代數解法，解析解法請參考[這篇文章](/posts/analytic-solution-of-the-harmonic-oscillator/)。

## 交換子和正則交換關係
利用動量算符$\hat{p}\equiv -i\hbar \cfrac{d}{dx}$，我們可以將方程（$\ref{eqn:t_independent_schrodinger_eqn}$）寫成：

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

現在讓我們因式分解哈密頓算符（Hamiltonian）

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

如果$p$和$x$是數字，我們可以簡單地因式分解為

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

但是這裡$\hat{p}$和$\hat{x}$是算符，對算符來說通常不滿足**交換律（commutative property）**（$\hat{p}\hat{x}\neq \hat{x}\hat{p}$），所以沒有那麼簡單。但無論如何，這可以作為一個起點，所以讓我們從考慮以下量開始：

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

對於我們剛定義的算符$\hat{a}\_\pm$，$\hat{a}\_-\hat{a}\_+$是

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

這裡$(\hat{x}\hat{p}-\hat{p}\hat{x})$項被稱為$\hat{x}$和$\hat{p}$的**交換子（commutator）**，它表示兩個算符不能交換的程度。一般來說，算符$\hat{A}$和$\hat{B}$的交換子用方括號表示如下：

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

使用這種表示法，我們可以將方程（$\ref{eqn:a_m_times_a_p_without_commutator}$）重寫為：

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

現在我們需要找出$\hat{x}$和$\hat{p}$的交換子。

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

去掉試驗函數$f(x)$，我們得到：

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

這被稱為**正則交換關係（canonical commutation relation）**。

## 階梯算符（ladder operators）
根據正則交換關係，方程（$\ref{eqn:a_m_times_a_p}$）變為

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

即

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

這裡$\hat{a}\_-$和$\hat{a}\_+$的順序很重要，如果把$\hat{a}\_+$放在左邊，我們得到

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

並且滿足

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

在這種情況下，哈密頓算符也可以寫成

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

因此，用$\hat{a}_\pm$表示的時間無關薛丁格方程（$\hat{H}\psi=E\psi$）是

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

（上下符號同順）。

現在我們可以得到以下重要性質：

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> 證明：
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> 同樣地，
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

因此，如果我們能找到時間無關薛丁格方程的一個解，我們就能找到所有其他解。由於我們可以對任意定態提高或降低能量本徵值，所以$\hat{a}\_\pm$被稱為**階梯算符（ladder operators）**，其中$\hat{a}\_+$是**升階算符（raising operator）**，$\hat{a}\_-$是**降階算符（lowering operator）**。

## 諧振子的定態
### 定態 $\psi_n$ 和能量級 $E_n$
如果持續應用降階算符，最終會得到能量小於 $0$ 的狀態，而這種狀態在物理上是不可能存在的。從數學上來說，如果 $\psi$ 是薛丁格方程的解，那麼 $\hat{a}_-\psi$ 也是薛丁格方程的解，但這個新解並不保證總是能被規範化（即不保證是物理上可能的狀態）。持續應用降階算符，最終會得到平凡解 $\psi=0$。

因此，對於諧振子的定態 $\psi$，存在一個「最低階」$\psi_0$，滿足：

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

這個 $\psi_0$ 不存在更低的能量級。它滿足：

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

因此，

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

這是一個[可分離的常微分方程](/posts/Separation-of-Variables/)，可以輕易解得：

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

此外，這個函數可以如下規範化：

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

這裡 $A^2 = \sqrt{m\omega / \pi\hbar}$，所以

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

現在將這個解代入先前得到的薛丁格方程（$\ref{eqn:schrodinger_eqn_with_ladder}$），並利用 $\hat{a}_-\psi_0=0$，我們得到：

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

從這個**基態（ground state）**開始，持續應用升階算符，每應用一次升階算符，能量就增加 $\hbar\omega$，我們就可以得到激發態（excited states）。

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

這裡 $A_n$ 是規範化常數。這樣，我們可以先找出基態，然後應用升階算符來決定諧振子的所有定態和允許的能量級。

### 規範化
規範化常數也可以用代數方法求得。我們知道 $\hat{a}\_{\pm}\psi_n$ 與 $\psi\_{n\pm 1}$ 成正比，所以可以寫成：

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

現在注意到對於任何可積函數 $f(x)$ 和 $g(x)$，以下關係成立：

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ 是 $\hat{a}\_\pm$ 的**厄米共軛（hermitian conjugate）**和**伴隨算符（adjoint operator）**。

> **證明：**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

因此，令 $f=\hat{a}_\pm \psi_n$，$g=\psi_n$，我們得到：

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

那麼從方程（$\ref{eqn:schrodinger_eqn_with_ladder}$）和（$\ref{eqn:psi_n_and_E_n}$）可得：

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

從方程（$\ref{eqn:norm_const}$）和（$\ref{eqn:norm_const_2}$），我們得到：

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

由於 $\psi_n$ 和 $\psi_{n\pm1}$ 都是規範化的，所以 $\|c_n\|^2=n+1,\ \|d_n\|^2=n$，因此：

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

從這裡，我們可以得到任意規範化的定態 $\psi_n$：

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

也就是說，在方程（$\ref{eqn:psi_n_and_E_n}$）中，規範化常數 $A_n=\cfrac{1}{\sqrt{n!}}$。

### 定態的正交性
和[一維無限方井](/posts/the-infinite-square-well/#3-這些狀態具有正交性orthogonality)一樣，諧振子的定態也是正交的。

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### 證明
我們可以使用先前證明的方程（$\ref{eqn:hermitian_conjugate}$）、（$\ref{eqn:norm_const_2}$）和（$\ref{eqn:norm_const_3}$）來證明這一點。在方程（$\ref{eqn:hermitian_conjugate}$）中，令 $f=\hat{a}_-\psi_m,\ g=\psi_n$，我們得到：

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

利用這個關係：

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

利用正交性，就像[一維無限方井的方程（19）中所做的那樣](/posts/the-infinite-square-well/#求解時間相依薛丁格方程的一般解psixt)，當我們將 $\Psi(x,0)$ 展開為定態的線性組合 $\sum c_n\psi_n(x)$ 時，可以使用[傅立葉方法](/posts/the-infinite-square-well/#使用傅立葉方法fouriers-trick求係數c_n)來求係數 $c_n$。

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

這裡同樣，$\|c_n\|^2$ 是測量能量得到 $E_n$ 值的概率。

## 任意定態 $\psi_n$ 中勢能的期望值 $\langle V \rangle$
為了求 $\langle V \rangle$，我們需要計算以下積分：

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

在計算包含 $\hat{x}$ 和 $\hat{p}$ 的冪次的這種形式的積分時，以下方法非常有用。

首先，利用方程（$\ref{eqn:ladder_operators}$）中階梯算符的定義，將 $\hat{x}$ 和 $\hat{p}$ 表示為升階算符和降階算符：

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

現在，使用上面的 $\hat{x}$ 和 $\hat{p}$ 的表達式來表示我們想要求期望值的物理量。這裡我們關心的是 $x^2$，所以：

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

從這裡我們得到：

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

這裡，$\left(\hat{a}\_{\pm} \right)^2$ 與 $\psi\_{n\pm2}$ 成正比，因此與 $\psi\_n$ 正交，所以 $\left(\hat{a}\_+ \right)^2$ 和 $\left(\hat{a}\_- \right)^2$ 這兩項為 $0$。最後，利用方程（$\ref{eqn:norm_const_2}$）計算剩下的兩項，我們得到：

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

參考方程（$\ref{eqn:psi_n_and_E_n}$），我們可以看到勢能的期望值正好是總能量的一半，剩下的一半當然是動能 $T$。這是諧振子的固有特性。
