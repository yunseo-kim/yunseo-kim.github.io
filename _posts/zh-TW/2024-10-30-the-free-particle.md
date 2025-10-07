---
title: 自由粒子(The Free Particle)
description: 探討V(x)=0的自由粒子情況下，變數分離解無法歸一化的事實及其意義，定性地展示一般解的位置-動量不確定性關係，並求出Ψ(x,t)的相速度和群速度進行物理解釋。
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 自由粒子：$V(x)=0$，無邊界條件（任意能量）
> - 變數分離解 $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ 在平方積分時發散至無窮大，因此無法歸一化，這意味著：
>   - 自由粒子無法以穩態存在
>   - 自由粒子無法定義為一個確切的能量值（存在能量不確定性）
> - 儘管如此，由於時間相依薛丁格方程的一般解是變數分離解的線性組合，變數分離解在數學上仍具重要意義。但此情況下由於無限制條件，一般解不是對離散變數 $n$ 的求和（$\sum$），而是對連續變數 $k$ 的積分（$\int$）形式。
> - 薛丁格方程的一般解：
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{其中 }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - 位置不確定性與動量不確定性的關係：
>   - 位置不確定性減小時動量不確定性增大，反之動量不確定性減小時位置不確定性增大
>   - 即量子力學上無法同時精確知道自由粒子的位置和動量
> - 波函數 $\Psi(x,t)$ 的相速度和群速度：
>   - 相速度：$v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - 群速度：$v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - 群速度的物理意義及與古典力學的比較：
>   - 物理上群速度即為該粒子的運動速率
>   - 當 $\phi(k)$ 在某值 $k_0$ 附近呈非常尖銳形態時（動量不確定性足夠小時），
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## 先備知識
- 歐拉公式
- 傅立葉變換(Fourier transform) & 普朗歇雷爾定理(Plancherel's theorem)
- [薛丁格方程和波函數](/posts/schrodinger-equation-and-the-wave-function/)
- [時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/)
- [一維無限方井](/posts/the-infinite-square-well/)

## 模型設定
讓我們考察最簡單的情況——自由粒子（$V(x)=0$）。在古典力學中這只是等速運動，但在量子力學中這個問題更加有趣。  
自由粒子的[時間無關薛丁格方程](/posts/time-independent-schrodinger-equation/)為

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

即

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{，其中 }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[這與勢能為 $0$ 的無限方井內部相同](/posts/the-infinite-square-well/#模型和邊界條件設置)。不過這次讓我們將一般解寫成以下指數函數形式。

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ 與 $C\cos{kx}+D\sin{kx}$ 是表示相同 $x$ 函數的等價方法。根據歐拉公式 $e^{ix}=\cos{x}+i\sin{x}$
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> 即設 $C=A+B$，$D=i(A-B)$ 則 
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> 反之用 $C$ 和 $D$ 表示 $A$ 和 $B$ 則為 $A=\cfrac{C-iD}{2}$，$B=\cfrac{C+iD}{2}$。
>
> 在量子力學中當 $V=0$ 時指數函數表示移動波，在處理自由粒子時最為方便。而正弦和餘弦函數易於表示駐波，在無限方井情況下自然出現。
{: .prompt-info }

與無限方井不同，這次沒有限制 $k$ 和 $E$ 的邊界條件。即自由粒子可以擁有任意正能量。 

## 變數分離解與相速度
在 $\psi(x)$ 上加上時間依賴性 $e^{-iEt/\hbar}$ 得到

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

這種依賴於特殊形式 $(x\pm vt)$ 的 $x$ 和 $t$ 的任意函數，表示形狀不變且以速率 $v$ 向 $\mp x$ 方向移動的波。因此式 ($\ref{eqn:Psi_seperated_solution}$) 的第一項表示向右移動的波，第二項表示具有相同波長和傳播速率但振幅不同的波向左移動。它們只是 $k$ 前的符號不同，所以可以寫成

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

此時根據 $k$ 的符號，波的傳播方向如下。

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{向右移動}, \\
k<0 \Rightarrow & \text{向左移動}.
\end{cases} \tag{6}$$

自由粒子的「穩態」明顯是傳播波*，其波長為 $\lambda = 2\pi/\|k\|$，根據德布羅意公式(de Broglie formula)具有

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

的動量。

> *「穩態」卻是傳播波在物理上當然是矛盾的。原因很快就會說明。
{: .prompt-info }

此外這個波的速率如下。

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

（這裡 $\omega$ 是 $t$ 前的係數 $\cfrac{\hbar k^2}{2m}$。）

然而，這個波函數在平方積分時發散至無窮大，因此無法歸一化。

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

即，<u>自由粒子的變數分離解在物理上不是可能的狀態。</u>自由粒子無法以[穩態](/posts/time-independent-schrodinger-equation/#1-它們是穩態stationary-states)存在，也無法擁有[某個特定的能量值](/posts/time-independent-schrodinger-equation/#2-它們具有一個明確的總能量值-e而不是一個機率分布範圍)。事實上直觀地想，兩端完全沒有邊界條件卻形成駐波才更奇怪。

## 求解時間相依薛丁格方程的一般解 $\Psi(x,t)$
儘管如此，這個變數分離解仍具有重要意義，因為除了物理解釋外，[時間相依薛丁格方程的一般解是變數分離解的線性組合](/posts/time-independent-schrodinger-equation/#3-時間相依薛丁格方程式的一般解是變數分離解的線性組合)這一數學意義仍然成立。不過此情況下由於沒有限制條件，一般解不是對離散變數 $n$ 的求和（$\sum$），而是對連續變數 $k$ 的積分（$\int$）形式。

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> 這裡 $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ 起到與[「時間無關薛丁格方程」文章式 (21)](/posts/time-independent-schrodinger-equation/#3-時間相依薛丁格方程式的一般解是變數分離解的線性組合) 中 $c_n$ 相同的作用。
{: .prompt-info }

這個波函數對於適當的 $\phi(k)$ 可以歸一化，但必須有 $k$ 的範圍，因此具有能量和速率的範圍。這被稱為**波包(wave packet)**。

> 正弦函數在空間上無限擴展因此無法歸一化。但將多個這樣的波疊加時，由於干涉會局域化並可以歸一化。
{: .prompt-info }

## 利用普朗歇雷爾定理(Plancherel theorem)求 $\phi(k)$

現在我們知道了 $\Psi(x,t)$ 的形式（式 [$\ref{eqn:Psi_general_solution}$]），只需確定滿足初始波函數

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

的 $\phi(k)$ 即可。這是傅立葉分析(Fourier analysis)的典型問題，可以用**普朗歇雷爾定理(Plancherel's theorem)**得到答案。

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$ 稱為 $f(x)$ 的**傅立葉變換(Fourier transform)**，$f(x)$ 是 $F(k)$ 的**逆傅立葉變換(inverse Fourier transform)**。從式 ($\ref{eqn:plancherel_theorem}$) 可以輕易確認兩者的差異只在於指數的符號。當然存在積分必須存在的限制條件。

> $f(x)$ 存在的充要條件是 $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ 必須有限。此時 $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ 也有限，且 
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> 有些人將上式而非式 ($\ref{eqn:plancherel_theorem}$) 稱為普朗歇雷爾定理(Plancherel's theorem)（[維基百科](https://en.wikipedia.org/wiki/Plancherel_theorem)也是如此描述）。
{: .prompt-info }

在目前這種情況下，由於 $\Psi(x,0)$ 必須歸一化這一物理條件，積分必然存在。因此自由粒子的量子力學解為式 ($\ref{eqn:Psi_general_solution}$)，其中

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> 不過實際上能解析求解式 ($\ref{eqn:Psi_general_solution}$) 積分的情況幾乎沒有。通常使用電腦數值分析求值。
{: .prompt-tip }

## 波包的群速度計算及物理解釋

本質上波包是由 $\phi$ 決定振幅的無數正弦函數的疊加。即波包由「包絡線(envelope)」內的「漣漪(ripples)」組成。

![A wave packet with the group velocity larger(5x) than phase velocity](/physics-visualizations/figs/wave_packet.webp)
> *圖片授權及原作來源聲明*
> - 圖片生成原始碼(Python3)：[yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/wave_packet.py)
> - 圖片生成原始碼(gnuplot)：[yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/wave_packet.plt)
> - 授權：[Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)
> - 原作者：[Ph.D. Youjun Hu](https://github.com/youjunhu)
> - 原授權聲明：[MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

物理上對應粒子速度的不是前面式 ($\ref{eqn:phase_velocity}$) 求得的個別漣漪速度（**相速度，phase velocity**），而是外側包絡線的速度（**群速度，group velocity**）。

### 位置不確定性與動量不確定性的關係
讓我們單獨考慮式 ($\ref{eqn:Psi_at_t_0}$) 的被積函數 $\int\phi(k)e^{ikx}dk$ 和式 ($\ref{eqn:phi}$) 的被積函數 $\int\Psi(x,0)e^{-ikx}dx$ 部分，來看位置不確定性與動量不確定性之間的關係。

#### 位置不確定性小時
當位置空間中 $\Psi$ 分布在某值 $x_0$ 周圍的非常窄區域 $[x_0-\delta, x_0+\delta]$，在該區域外接近 0 時（<u>位置不確定性小時</u>），$e^{-ikx} \approx e^{-ikx_0}$ 對 $x$ 幾乎為常數，所以

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{式 }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

定積分項對 $p$ 為常數，所以由前面的 $e^{-ipx_0/\hbar}$ 項使 $\phi$ 在動量空間中對 $p$ 呈正弦波形態，即分布在寬動量區間（<u>動量不確定性大</u>）。

#### 動量不確定性小時
同樣，當動量空間中 $\phi$ 分布在某值 $p_0$ 周圍的非常窄區域 $[p_0-\delta, p_0+\delta]$，在該區域外接近 0 時（<u>動量不確定性小時</u>），根據式 ($\ref{eqn:de_broglie_formula}$)，$e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ 對 $p$ 幾乎為常數，且 $dk=\frac{1}{\hbar}dp$，所以

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

由前面的 $e^{ip_0x/\hbar}$ 項使 $\Psi$ 在位置空間中對 $x$ 呈正弦波形態，即分布在寬位置區間（<u>位置不確定性大</u>）。

#### 結論
位置不確定性減小時動量不確定性增大，反之動量不確定性減小時位置不確定性增大。因此量子力學上無法同時精確知道自由粒子的位置和動量。

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *圖片來源*
> - 作者：英文維基百科用戶 [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - 授權：public domain

> 事實上，根據不確定性原理(uncertainty principle)，這不僅適用於自由粒子，而是適用於所有情況。不確定性原理將在後續單獨文章中討論。
{: .prompt-info }

### 波包的群速度
將式 ($\ref{eqn:Psi_general_solution}$) 的一般解如式 ($\ref{eqn:phase_velocity}$) 中一樣用 $\omega \equiv \cfrac{\hbar k^2}{2m}$ 重寫為

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> 像 $\omega = \cfrac{\hbar k^2}{2m}$ 這樣將 $\omega$ 表示為 $k$ 函數的式子稱為**色散關係(dispersion relation)**。後述內容不論色散關係如何，都普遍適用於所有波包。
{: .prompt-info }

現在假設 $\phi(k)$ 在適當值 $k_0$ 附近呈非常尖銳形態。（$k$ 分布較寬也可以，但這種波包形態會很快變形為其他形態。不同 $k$ 的成分各自以不同速率移動，因此失去具有明確定義速度的整體「群」的意義。即<u>動量不確定性增大。</u>）  
被積函數除了 $k_0$ 附近外可以忽略，所以可以在此點附近對函數 $\omega(k)$ 進行泰勒展開，只取到一次項得到

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

現在以 $s=k-k_0$ 替換，以 $k_0$ 為中心積分得到

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

前面的項 $e^{i(k_0x-\omega_0t)}$ 表示以速率 $\omega_0/k_0$ 移動的正弦波（「漣漪」），決定此正弦波振幅的積分項（「包絡線」）由 $e^{is(x-\omega_0^\prime t)}$ 部分以速率 $\omega_0^\prime$ 移動。因此 $k=k_0$ 時的相速度為

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

再次確認與式 ($\ref{eqn:phase_velocity}$) 的值相同，群速度為

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

為相速度的 2 倍。

## 與古典力學的比較

我們知道在宏觀尺度下古典力學成立，所以通過量子力學得到的結果在量子論不確定性足夠小時應該能近似為古典力學的計算結果。對於目前處理的自由粒子情況，如前面假設的 $\phi(k)$ 在適當值 $k_0$ 附近呈非常尖銳形態時（即<u>動量不確定性足夠小時</u>），量子力學中對應粒子速率的群速度 $v_\text{group}$ 應該與古典力學中對相同 $k$ 及相應能量值 $E$ 求得的粒子速率 $v_\text{classical}$ 相同。

將式 ($\ref{eqn:t_independent_schrodinger_eqn}$) 的 $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ 代入剛求得的群速度（式 [$\ref{eqn:group_velocity}$]）得到

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

古典力學中具有動能 $E$ 的自由粒子速率同樣為

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

因此 $v_\text{quantum}=v_\text{classical}$，可以確認應用量子力學得到的結果是物理上合理的解。
