---
title: 質量與能量，粒子與波動
description: 探索相對論的質量-能量等價原理，並考慮相對論效應計算運動電子的能量。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## 質量-能量等價原理
質量與能量是相同的，並且可以相互轉換。

$$ E=mc^2 $$

其中 $c$ 是光速 $2.9979 \times 10^{10}\ \text{cm/sec}$。

## 電子伏特(Electron Volt, eV)
*電子伏特(electron volt, eV)*：一個電子通過1V電壓時獲得的動能

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## 運動物體的質量與能量
根據相對論，從觀察者的角度來看，運動物體的質量相對增加，運動物體的速度與質量的關係式如下：

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$：靜止質量，$v$：速度

粒子的*總能量(total energy)*是*靜止質量能量(rest-mass energy)*與*動能(kinetic energy)*的總和，因此成立以下關係：

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

特別是當 $v\ll c$ 時，令 $\cfrac{v^2}{c^2} = \epsilon$，在 $\epsilon = 0$ 附近進行泰勒展開（即麥克勞林展開）近似：

$$
\begin{align*}
E_{\text{kinetic}} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

這與經典力學中的動能公式相同。實際上，當 $v\leq 0.2c$ 或 $E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$ 時，可以視為 $v\ll c$，使用這個近似公式（即忽略相對論效應）仍能得到足夠準確的值。

### 電子
電子的靜止質量能量 $E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$，因此，當電子的動能超過 $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$ 時，必須應用相對論動能公式。在核工程中處理的電子能量在許多情況下大於10keV，所以大多數情況下必須應用公式(2)。

### 中子
中子的靜止質量能量約為1000MeV，因此 $0.02E_{rest}=20\text{MeV}$。在核工程中，處理中子動能超過20MeV的情況很少見，所以通常使用公式(3)計算中子的動能。

### 光子
公式(2)、(3)僅適用於靜止質量不為零的情況，因此不適用於靜止質量為零的光子。光子的總能量由以下公式計算：

$$ E = h\nu \tag{4} $$

$h$：普朗克常數($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$)，$\nu$：電磁波頻率

## 物質波
自然界中的所有物質既是粒子又是波動。也就是說，所有粒子都有相應的波長（*德布羅意波長，de Broglie wavelength*）。波長 $\lambda$ 是動量 $p$ 和普朗克常數 $h$ 的函數。

$$ \lambda = \frac {h}{p} \tag{5}$$

而動量 $p$ 由以下公式定義：

$$ p = mv \tag{6} $$

### 忽略相對論效應的情況（例如，中子）
動能 $E=1/2 mv^2$，因此將公式(6)表示為能量的函數：

$$ p=\sqrt{2mE} \tag{7} $$

將其代入公式(5)，粒子的波長為：

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

在核工程中，計算中子的德布羅意波長時使用上述公式。代入中子的靜止質量後，表示為：

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

其中 $\lambda$ 的單位是cm，$E$ 是以eV表示的中子動能。

### 考慮相對論效應的情況（例如，電子）
直接解前面的相對論公式來計算動量 $p$。

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{rest}}} \tag{10}$$

則德布羅意波長為：

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{rest}}}} \tag{11} $$

### 靜止質量為零的粒子（例如，光子）
靜止質量為零的粒子的動量不能用公式(6)計算，而是表示為：

$$ p=\frac {E}{c} \tag{12} $$

將公式(12)代入公式(5)：

$$ \lambda = \frac {hc}{E} \tag{13}$$

代入 $h$ 和 $c$ 的值，最終波長公式為：

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

其中 $\lambda$ 的單位是m，$E$ 的單位是eV。
