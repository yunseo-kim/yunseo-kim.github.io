---
title: 核反應與結合能
description: 探討核反應的表達式和Q值(Q-value)的定義,以及質量虧損(mass defect)和結合能(binding energy)的概念。
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.png
---
## 核反應 (Nuclear Reaction)
### 核反應中的基本定律
*核反應(nuclear reaction)*：兩個不同的原子核相互碰撞,或原子核與核子碰撞,產生兩個或更多新的核粒子或伽馬射線的反應

如果兩個原子核 $a$、$b$ 反應產生原子核或伽馬射線 $c$、$d$,這個反應可以表示如下:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

核反應中遵循以下四個基本定律:

- *核子數守恆定律(conservation of nucleon)*：反應前後總核子數相同。核子的種類可以改變,因此質子和中子的數量各自不一定保持不變。
- *電荷量守恆定律(conservation of charge)*：反應前後粒子的總電荷量相同。
- *動量守恆定律(conservation of momentum)*：反應前後粒子的總動量相同。
- *能量守恆定律(conservation of energy)*：<u>包括靜止質量能量在內的</u>總能量在反應前後相同。

### 放熱反應(exothermic reaction) & 吸熱反應(endothermic reaction)
在式 ($\ref{nuclear_reaction}$) 的核反應中,反應前的總能量是 $a$ 和 $b$ 的靜止質量能量與動能之和,反應後的總能量是 $c$ 和 $d$ 的靜止質量能量與動能之和。因此,根據能量守恆定律,以下等式成立:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

整理上式可得:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

也就是說,核反應前後動能的差異等於核反應前後靜止質量的差異。
我們將上式右邊稱為核反應的 *Q值(Q-value)*,定義如下:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

Q值總是以MeV為單位表示,由於1 amu質量的靜止質量能量通常為931MeV,因此Q值也可以寫成:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *放熱反應(exothermic reaction)*：$Q>0$ 的核反應,部分質量轉換為動能,反應後動能增加
- *吸熱反應(endothermic reaction)*：$Q<0$ 的核反應,部分動能轉換為質量,反應後動能減少

| 核反應類型 | Q值 | 反應前後質量變化 | 反應前後動能變化 |
| :---: | :---: | :---: | :---: |
| 放熱反應 | $Q>0$ | $\Delta m<0$ (減少) | $\Delta E>0$ (增加) |
| 吸熱反應 | $Q<0$ | $\Delta m>0$ (增加) | $\Delta E<0$ (減少) |

### 核反應的簡略表示
式 ($\ref{nuclear_reaction}$) 的核反應可以簡略表示如下:

$$ a(b, c)d $$

這表示 $a$ 被 $b$ 入射,放出 $c$ 並轉變為 $d$ 的核反應。

#### 例如:
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## 結合能 (Binding Energy)
### 質量虧損 (Mass Defect)
所有原子核的質量都略小於構成該核的中子和質子質量之和。這個差異稱為*質量虧損(mass defect)*。

如果將原子核的質量表示為 $M_A$,則任意原子核的質量虧損 $\Delta$ 可以按以下方式計算:

$$ \Delta = ZM_p + NM_n - M_A. $$

將質量虧損 $\Delta$ 轉換為能量單位,就是將任意原子核分裂成其組成核子所需的能量。由於這是將核子束縛在一起的能量,因此稱為*結合能(binding energy)*。反過來說,當A個核子形成原子核時,能量水平會降低 $\Delta$,因此在核反應過程中會向周圍釋放相應的能量。

### 每核子平均結合能
原子核的總結合能隨質量數 $A$ 的增加而增加,但其斜率並不恆定。  
![不同中子數的每核子平均結合能](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
從上圖可以看出,每核子平均結合能 $\Delta/A$ 在低質量數時急劇增加,但在 $A\geq56$ 的重原子核中則緩慢下降。

### 核反應的Q值與結合能的關係
在式 ($\ref{nuclear_reaction}$) 的核反應中,核 $a$ 的結合能為

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

因此,核 $a$ 的質量為

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

同樣地,對於核 $b$、$c$、$d$,我們有

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

假設

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

將上述式子代入式 ($\ref{Q_value}$),我們得到

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

這意味著當兩個較不穩定的核通過某種核反應過程結合形成更穩定的核時,總是會釋放能量。

### 核融合(Nuclear Fusion)和核分裂(Nuclear Fission)
以結合能為 $2.23\text{MeV}$ 的氘和結合能為 $8.48\text{MeV}$ 的氚結合,生成結合能為 $28.3\text{MeV}$ 的 $^4\text{He}$ 並釋放一個中子的核反應為例:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

反應前後結合能差異相當於 $28.3-(2.23+8.48)=17.6\text{MeV}$ 的能量(每核子 $3.52\text{MeV}$)以氦原子核和中子的動能形式釋放。

像式 ($\ref{nuclear_fusion}$) 這樣,兩個質量數較小的輕原子核結合形成比反應前質量數更大的重原子核的反應稱為*核融合(nuclear fusion)*。這是太陽和所有恆星的能量來源,也許有朝一日人類能直接將其作為動力源使用。

另一方面,以結合能約為 $1780\text{MeV}$ 的 $^{235}\text{U}$ 吸收中子後分裂成結合能為 $783\text{MeV}$ 的 $^{92}\text{Kr}$ 和約 $1170\text{MeV}$ 的 $^{141}\text{Ba}$,並釋放3個中子的核反應為例:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

反應前後結合能差異相當於 $783+1170-1780=173\text{MeV}$ 的能量(每核子 $0.733\text{MeV}$)被釋放。

像式 ($\ref{nuclear_fission}$) 這樣,重原子核分裂成較輕原子核的反應稱為*核分裂(nuclear fission)*。自艾森豪威爾第34任美國總統的"和平利用原子能(Atoms for Peace)"演說和蘇聯的奧布寧斯克核電站以來,核分裂已被廣泛用作電力來源。
