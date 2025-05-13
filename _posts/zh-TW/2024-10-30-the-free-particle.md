---
title: 自由粒子（The Free Particle）
description: 探討V(x)=0的自由粒子情況下，變數分離解無法規範化的事實及其意義，定性地展示一般解的位置-動量不確定性關係，並計算Ψ(x,t)的相速度和群速度，進行物理解釋。
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 自由粒子：$V(x)=0$，無邊界條件（任意能量）
> - 變數分離解 $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ 平方積分時發散至無窮大，因此無法規範化，這暗示：
>   - 自由粒子無法以定態存在
>   - 自由粒子無法定義為一個精確的能量值（存在能量不確定性）
> - 儘管如此，時間相依薛丁格方程的一般解仍是變數分離解的線性組合，因此變數分離解在數學上仍具重要意義。但在這種情況下，由於沒有限制條件，一般解不是對不連續變數 $n$ 的和（$\sum$），而是對連續變數 $k$ 的積分（$\int$）形式。
> - 薛丁格方程的一般解：
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{其中 }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - 位置不確定性和動量不確定性的關係：
>   - 位置不確定性減小時，動量不確定性增大，反之亦然
>   - 即在量子力學上，無法同時精確知道自由粒子的位置和動量
> - 波函數 $\Psi(x,t)$ 的相速度和群速度：
>   - 相速度：$v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - 群速度：$v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - 群速度的物理意義及與經典力學的比較：
>   - 物理上，群速度即代表該粒子的運動速度
>   - 假設 $\phi(k)$ 在某值 $k_0$ 附近呈現非常尖銳的形狀時（動量不確定性足夠小時），
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## 先備知識
- 歐拉公式
- 傅立葉變換（Fourier transform）& 普朗歇雷爾定理（Plancherel's theorem）
- [薛丁格方程和波函數](/posts/schrodinger-equation-and-the-wave-function/)
- [時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/)
- [一維無限方井](/posts/the-infinite-square-well/)

## 模型設定
讓我們來看最簡單的情況，即自由粒子（$V(x)=0$）。在經典物理中，這只是等速運動，但在量子力學中，這個問題變得更加有趣。
自由粒子的[時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/)為

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

即

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{，其中 }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[到這裡為止，與勢能為 $0$ 的無限方井內部相同](/posts/the-infinite-square-well/#模型和邊界條件設置)。不過這次我們將一般解寫成以下指數函數形式：

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ 和 $C\cos{kx}+D\sin{kx}$ 是表示同一 $x$ 函數的等價方法。根據歐拉公式 $e^{ix}=\cos{x}+i\sin{x}$，我們有
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> 即，如果我們令 $C=A+B$，$D=i(A-B)$，則
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> 反之，用 $C$ 和 $D$ 表示 $A$ 和 $B$，則 $A=\cfrac{C-iD}{2}$，$B=\cfrac{C+iD}{2}$。
>
> 在量子力學中，當 $V=0$ 時，指數函數表示移動的波，在處理自由粒子時最為方便。相反，正弦和餘弦函數適合表示駐波，在無限方井的情況下自然出現。
{: .prompt-info }

與無限方井不同，這次沒有限制 $k$ 和 $E$ 的邊界條件。也就是說，自由粒子可以具有任意正能量。

## 變數分離解和相速度
將時間依賴性 $e^{-iEt/\hbar}$ 加到 $\psi(x)$ 上，我們得到

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

任何依賴於特定形式 $(x\pm vt)$ 的 $x$ 和 $t$ 的函數，都表示一個以速度 $v$ 向 $\mp x$ 方向移動且形狀不變的波。因此，式 ($\ref{eqn:Psi_seperated_solution}$) 的第一項表示向右移動的波，第二項表示具有相同波長和傳播速度但振幅不同的向左移動的波。它們只在 $k$ 前的符號上有所不同，所以我們可以寫成

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

這時，根據 $k$ 的符號，波的傳播方向如下：

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{向右移動}, \\
k<0 \Rightarrow & \text{向左移動}.
\end{cases} \tag{6}$$

自由粒子的「定態」顯然是進行波*，其波長為 $\lambda = 2\pi/\|k\|$，根據德布羅意公式（de Broglie formula），其動量為

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

> *「定態」卻是進行波，這在物理上當然是矛盾的。原因很快就會說明。
{: .prompt-info }

此外，這個波的速度如下：

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

（這裡的 $\omega$ 是 $t$ 前的係數 $\cfrac{\hbar k^2}{2m}$。）

然而，這個波函數在平方積分時會發散到無窮大，因此無法規範化。

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

也就是說，<u>在自由粒子的情況下，變數分離解在物理上不是可能的狀態。</u>自由粒子無法以[定態](/posts/time-independent-schrodinger-equation/#1-它們是穩態stationary-states)存在，也無法具有[某個特定的能量值](/posts/time-independent-schrodinger-equation/#2-它們具有一個明確的總能量值-e而不是一個機率分布範圍)。事實上，直觀地想，在兩端完全沒有邊界條件的情況下形成駐波才更奇怪。

## 求解時間相依薛丁格方程的一般解 $\Psi(x,t)$
儘管如此，這個變數分離解仍然具有重要意義，因為除了物理解釋之外，[時間相依薛丁格方程的一般解是變數分離解的線性組合](/posts/time-independent-schrodinger-equation/#3-時間相依薛丁格方程式的一般解是變數分離解的線性組合)這一數學意義仍然成立。只是在這種情況下，由於沒有限制條件，一般解不是對不連續變數 $n$ 的和（$\sum$），而是對連續變數 $k$ 的積分（$\int$）形式。

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> 這裡，$\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ 扮演了與['時間無關薛丁格方程'文章中式 (21)](/posts/time-independent-schrodinger-equation/#3-時間相依薛丁格方程式的一般解是變數分離解的線性組合) 中 $c_n$ 相同的角色。
{: .prompt-info }

這個波函數對於適當的 $\phi(k)$ 可以被規範化，但必須有 $k$ 的範圍，因此也有能量和速度的範圍。這被稱為**波包（wave packet）**。

> 正弦函數在空間上無限延伸，因此無法規範化。然而，如果我們疊加多個這樣的波，它們會因干涉而局部化，從而可以規範化。
{: .prompt-info }

## 使用普朗歇雷爾定理（Plancherel theorem）求解 $\phi(k)$

現在我們知道了 $\Psi(x,t)$ 的形式（式 [$\ref{eqn:Psi_general_solution}$]），只需要確定滿足初始波函數

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

的 $\phi(k)$ 即可。這是傅立葉分析（Fourier analysis）的典型問題，可以用**普朗歇雷爾定理（Plancherel's theorem）**來解答。

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

我們稱 $F(k)$ 為 $f(x)$ 的**傅立葉變換（Fourier transform）**，而 $f(x)$ 是 $F(k)$ 的**逆傅立葉變換（inverse Fourier transform）**。從式 ($\ref{eqn:plancherel_theorem}$) 可以輕易看出，兩者的差異僅在於指數的符號。當然，這裡有一個限制條件，即只有積分存在的函數才被允許。

> $f(x)$ 存在的必要充分條件是 $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ 必須是有限的。在這種情況下，$\int_{-\infty}^{\infty}\|F(k)\|^2dk$ 也是有限的，且
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> 有些人將這個式子，而不是式 ($\ref{eqn:plancherel_theorem}$)，稱為普朗歇雷爾定理（Plancherel's theorem）（[維基百科](https://en.wikipedia.org/wiki/Plancherel_theorem)也是這樣描述的）。
{: .prompt-info }

在這個情況下，由於 $\Psi(x,0)$ 必須被規範化的物理條件，積分必定存在。因此，自由粒子的量子力學解是式 ($\ref{eqn:Psi_general_solution}$)，其中

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> 然而，實際上能夠解析地求解式 ($\ref{eqn:Psi_general_solution}$) 的積分的情況幾乎不存在。通常我們會使用電腦進行數值分析來求值。
{: .prompt-tip }

## 計算波包的群速度及其物理解釋

本質上，波包是由 $\phi$ 決定振幅的眾多正弦函數的疊加。也就是說，波包由形成「包絡線（envelope）」的「漣漪（ripples）」組成。

![群速度大於相速度（5倍）的波包](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/wave_packet.gif)
> *圖片授權及原作出處聲明*
> - 圖片生成源代碼（gnuplot）：[yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/wave_packet.plt)
> - 授權：[Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualization/blob/main/LICENSE)
> - 原作者：[Ph.D. Youjun Hu](https://github.com/youjunhu)
> - 原授權聲明：[MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

從物理角度來看，對應於粒子速度的不是前面式 ($\ref{eqn:phase_velocity}$) 中計算的個別漣漪的速度（**相速度，phase velocity**），而是外部包絡線的速度（**群速度，group velocity**）。

### 位置不確定性和動量不確定性的關係
讓我們單獨考慮式 ($\ref{eqn:Psi_at_t_0}$) 中的被積分項 $\int\phi(k)e^{ikx}dk$ 和式 ($\ref{eqn:phi}$) 中的被積分項 $\int\Psi(x,0)e^{-ikx}dx$，來探討位置不確定性和動量不確定性之間的關係。

#### 當位置不確定性小時
在位置空間中，當 $\Psi$ 分布在某個值 $x_0$ 附近的非常窄的區域 $[x_0-\delta, x_0+\delta]$，而在其他區域接近 0 時（<u>位置不確定性小時</u>），$e^{-ikx} \approx e^{-ikx_0}$ 對 $x$ 幾乎是常數，因此

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{式 }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

定積分項對 $p$ 是常數，因此前面的 $e^{-ipx_0/\hbar}$ 項使得 $\phi$ 在動量空間中對 $p$ 呈現正弦波形式，即分布在寬廣的動量區間（<u>動量不確定性大</u>）。

#### 當動量不確定性小時
同樣地，在動量空間中，當 $\phi$ 分布在某個值 $p_0$ 附近的非常窄的區域 $[p_0-\delta, p_0+\delta]$，而在其他區域接近 0 時（<u>動量不確定性小時</u>），根據式 ($\ref{eqn:de_broglie_formula}$)，$e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ 對 $p$ 幾乎是常數，且 $dk=\frac{1}{\hbar}dp$，因此

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

前面的 $e^{ip_0x/\hbar}$ 項使得 $\Psi$ 在位置空間中對 $x$ 呈現正弦波形式，即分布在寬廣的位置區間（<u>位置不確定性大</u>）。

#### 結論
位置不確定性減小時，動量不確定性增大，反之亦然。因此，在量子力學上，無法同時精確知道自由粒子的位置和動量。

![量子力學行進波函數](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *圖片來源*
> - 作者：英文維基百科用戶 [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - 授權：公有領域

> 事實上，根據不確定性原理（uncertainty principle），這不僅適用於自由粒子，而是適用於所有情況。我們將在未來的文章中詳細討論不確定性原理。
{: .prompt-info }

### 波包的群速度
將式 ($\ref{eqn:Psi_general_solution}$) 的一般解用與式 ($\ref{eqn:phase_velocity}$) 相同的 $\omega \equiv \cfrac{\hbar k^2}{2m}$ 重新寫為

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> 像 $\omega = \cfrac{\hbar k^2}{2m}$ 這樣將 $\omega$ 表示為 $k$ 的函數的式子稱為**色散關係（dispersion relation）**。以下內容不依賴於色散關係，適用於所有波包。
{: .prompt-info }

現在假設 $\phi(k)$ 在適當的值 $k_0$ 附近呈現非常尖銳的形狀。（雖然對 $k$ 廣泛分布也可以，但這種波包的形狀會很快變形並轉變為其他形狀。這是因為不同 $k$ 的成分以不同的速度移動，失去了整體「群」具有明確速度的意義。換句話說，<u>動量的不確定性增大。</u>）
被積分的函數除了 $k_0$ 附近可以忽略不計，因此我們可以在這一點附近對函數 $\omega(k)$ 進行泰勒展開，只取到一階項：

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

現在用 $s=k-k_0$ 替換，以 $k_0$ 為中心積分：

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

前面的項 $e^{i(k_0x-\omega_0t)}$ 表示以速度 $\omega_0/k_0$ 移動的正弦波（「漣漪」），而決定這個正弦波振幅的積分項（「包絡線」）由於 $e^{is(x-\omega_0^\prime t)}$ 部分以速度 $\omega_0^\prime$ 移動。因此，在 $k=k_0$ 處的相速度為

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

這與式 ($\ref{eqn:phase_velocity}$) 中的值相同，而群速度為

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

是相速度的兩倍。

## 與經典力學的比較

我們知道在宏觀尺度上經典力學成立，因此通過量子力學得到的結果在量子不確定性足夠小時應該近似於經典力學的計算結果。在我們現在討論的自由粒子情況下，如前面假設的那樣，當 $\phi(k)$ 在適當的值 $k_0$ 附近呈現非常尖銳的形狀時（即<u>動量不確定性足夠小時</u>），量子力學中對應於粒子速度的群速度 $v_\text{group}$ 應該與相同 $k$ 和相應能量值 $E$ 下經典力學計算的粒子速度 $v_\text{classical}$ 相同。

將剛剛得到的群速度（式 [$\ref{eqn:group_velocity}$]）代入式 ($\ref{eqn:t_independent_schrodinger_eqn}$) 中的 $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$，我們得到

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

而在經典力學中，具有動能 $E$ 的自由粒子的速度同樣為

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

因此，$v_\text{quantum}=v_\text{classical}$，這證實了我們通過應用量子力學得到的結果在物理上是合理的解。
