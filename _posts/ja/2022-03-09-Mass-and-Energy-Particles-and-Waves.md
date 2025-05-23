---
title: 質量とエネルギー、粒子と波動
description: 相対性理論の質量-エネルギー等価原理を探求し、運動する電子のエネルギーを相対論的効果を考慮して計算してみよう。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## 質量-エネルギー等価原理
質量とエネルギーは互いに同一であり、相互に変換することができる。

$$ E=mc^2 $$

ここで$c$は光の速度 $2.9979 \times 10^{10}\ \text{cm/sec}$である。

## 電子ボルト(Electron Volt, eV)
*電子ボルト(electron volt, eV)*：1個の電子が1Vの電圧を通過するときに得る運動エネルギー

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## 運動する物体の質量とエネルギー
相対性理論によれば、観測者の立場から運動する物体の質量は相対的に増加し、運動する物体の速さと質量に関する式は次のように定義される。

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$：静止質量、$v$：速さ

粒子の*総エネルギー(total energy)*は*静止質量エネルギー(rest-mass energy)*と*運動エネルギー(kinetic energy)*の和であるため、次が成り立つ。

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

特に$v\ll c$の場合、$\cfrac{v^2}{c^2} = \epsilon$とおき、$\epsilon = 0$付近でテイラー展開して（つまり、マクローリン展開して）近似すると

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

となり、古典力学での運動エネルギーの公式と同じになる。実質的に、$v\leq 0.2c$または$E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$の場合、$v\ll c$とみなしてこの近似式を使用しても（つまり、相対性理論による効果を無視しても）十分に正確な値が得られる。

### 電子
電子の静止質量エネルギー$E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$であるため、電子の運動エネルギーが$0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$を超える場合、相対論的運動エネルギー公式を適用する必要がある。原子核工学で扱う電子のエネルギーは多くの場合10keVより大きいため、ほとんどの場合式(2)を適用する必要がある。

### 中性子
中性子の静止質量エネルギーはおよそ1000MeVに達するため、$0.02E_{rest}=20\text{MeV}$である。原子核工学で中性子の運動エネルギーが20MeVを超える状況を扱うことはまれであるため、通常、中性子の運動エネルギー計算には式(3)を用いる。

### 光子
式(2)、(3)は静止質量が0でない場合に有効であるため、静止質量が0である光子には適用できない。光子の総エネルギーは以下の式で求める。

$$ E = h\nu \tag{4} $$

$h$：プランク定数($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$)、$\nu$：電磁波の振動数

## 物質波
自然界のすべての物質は粒子であると同時に波動である。つまり、すべての粒子はそれに相応する波長（*ドブロイ波長、de Broglie wavelength*）を持つ。このとき波長$\lambda$は運動量$p$とプランク定数$h$の関数である。

$$ \lambda = \frac {h}{p} \tag{5}$$

また、運動量$p$は次の式で定義される。

$$ p = mv \tag{6} $$

### 相対論的効果を無視する場合（例：中性子）
運動エネルギー$E=1/2 mv^2$であるため、式(6)をエネルギーの関数として表現すると次のようになる。

$$ p=\sqrt{2mE} \tag{7} $$

これを式(5)に代入すると、粒子の波長は

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

となる。原子核工学では中性子のドブロイ波長を求めるときに上記の式を適用する。中性子の静止質量を代入すると次のように表現される。

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

ここで$\lambda$の単位はcmであり、$E$はeVで表現された中性子の運動エネルギーである。

### 相対論的効果を考慮する場合（例：電子）
前述の相対性理論の式を直接解いて運動量$p$を計算する。

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{rest}}} \tag{10}$$

するとドブロイ波長は次のようになる。

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{rest}}}} \tag{11} $$

### 静止質量が0の粒子（例：光子）
静止質量が0の粒子の運動量は式(6)で求めることができないため、

$$ p=\frac {E}{c} \tag{12} $$

と表現する。式(12)を式(5)に代入すると

$$ \lambda = \frac {hc}{E} \tag{13}$$

となる。ここに$h$と$c$の値を代入すると、最終的に波長に関する式は

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

となる。ここで$\lambda$の単位はm、$E$の単位はeVである。
