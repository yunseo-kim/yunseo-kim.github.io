---
title: "核反応と結合エネルギー"
description: >-
  核反応の表現式とQ値（Q-value）の定義、質量欠損（mass defect）と結合エネルギー（binding energy）の概念を学ぶ。
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
---

## 核反応（Nuclear Reaction）
### 核反応における基本法則
*核反応（nuclear reaction）*：2つの異なる原子核同士、または原子核と核子が衝突して2つ以上の新しい核粒子またはガンマ線を生成する反応

2つの原子核 $a$、$b$ が反応して生成物として原子核またはガンマ線 $c$、$d$ が生成されるとすると、この反応は以下のように表現される。

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

核反応では、以下の4つの基本法則が成り立つ。

- *核子数保存の法則（conservation of nucleon）*：総核子数は反応の前後で同じである。核子の種類は変わる可能性があるため、陽子と中性子がそれぞれ保存されるわけではない。
- *電荷量保存の法則（conservation of charge）*：粒子の電荷量の総和は反応の前後で同じである。
- *運動量保存の法則（conservation of momentum）*：粒子の運動量の総和は反応の前後で同じである。
- *エネルギー保存の法則（conservation of energy）*：<u>静止質量エネルギーを含む</u>総エネルギーは反応の前後で同じである。

### 発熱反応（exothermic reaction）＆吸熱反応（endothermic reaction）
式（$\ref{nuclear_reaction}$）の核反応において、反応前の総エネルギーは $a$ と $b$ の静止質量エネルギーと運動エネルギーの和であり、反応後の総エネルギーは $c$ と $d$ の静止質量エネルギーと運動エネルギーの和である。したがって、エネルギー保存の法則により、以下が成り立つ。

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

上の式を整理すると以下のようになる。

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

つまり、核反応の前後の運動エネルギーの差は、核反応の前後の静止質量の差と等しいことがわかる。
最後の式の右辺を核反応の*Q値（Q-value）*と呼び、以下のように定義する。

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

Q値は常にMeV単位で表され、1 amuの質量に対する静止質量エネルギーが通常931MeVであるため、Q値を以下のように書くこともできる。

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *発熱反応（exothermic reaction）*：$Q>0$の核反応、質量の一部が運動エネルギーに変換され、反応後の運動エネルギーが増加
- *吸熱反応（endothermic reaction）*：$Q<0$の核反応、運動エネルギーの一部が質量に変換され、反応後の運動エネルギーが減少

| 核反応の種類 | Q値 | 反応前後の質量変化 | 反応前後の運動エネルギー変化 |
| :---: | :---: | :---: | :---: |
| 発熱反応 | $Q>0$ | $\Delta m<0$ （減少） | $\Delta E>0$ （増加） |
| 吸熱反応 | $Q<0$ | $\Delta m>0$ （増加） | $\Delta E<0$ （減少） |

### 核反応の簡略表現
式（$\ref{nuclear_reaction}$）の核反応は以下のように簡略化して表現できる。

$$ a(b, c)d $$

これは $a$ に $b$ が入射して $c$ を放出し、$d$ に変換される核反応を意味する。

#### 例）
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## 結合エネルギー（Binding Energy）
### 質量欠損（Mass Defect）
すべての核の質量は、その核を構成する中性子および陽子の質量の和よりもわずかに小さい。この差を*質量欠損（mass defect）*と呼ぶ。

核の質量を $M_A$ とすると、任意の核の質量欠損 $\Delta$ は次のように計算できる。

$$ \Delta = ZM_p + NM_n - M_A. $$

質量欠損 $\Delta$ をエネルギー単位で表現すると、任意の核をその構成核子に分解するのに必要なエネルギーとなる。核子を束縛しているエネルギーという意味で、これを*結合エネルギー（binding energy）*と呼ぶ。逆に、A個の核子から原子核が生成される場合、結合エネルギー $\Delta$ だけエネルギー準位が下がるため、核反応過程でそれだけのエネルギーを周囲に放出する。

### 核子あたりの平均結合エネルギー
原子核の総結合エネルギーは質量数 $A$ が増加するにつれて増加するが、その傾きは一定ではない。  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
核子あたりの平均結合エネルギー $\Delta/A$ は低い質量数では急激に増加するが、$A\geq56$ の重い原子核では緩やかな傾きで減少することが上の画像で確認できる。

### 核反応のQ値と結合エネルギーの関係
式（$\ref{nuclear_reaction}$）の核反応において、$a$ 核の結合エネルギーは

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

であり、$a$ の質量は

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

となる。同様の方法で $b$、$c$、$d$ 核についても

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

である。

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

と見なし、上の式を式（$\ref{Q_value}$）に代入すると

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

となる。これは、ある核反応過程によって、より不安定な2つの核が結合してより安定な核が作られるときは、常にエネルギーが放出されることを意味する。

### 核融合（Nuclear Fusion）と核分裂（Nuclear Fission）
$2.23\text{MeV}$ の結合エネルギーを持つ重水素と $8.48\text{MeV}$ の結合エネルギーを持つ三重水素が結合して $28.3\text{MeV}$ の結合エネルギーを持つ $^4\text{He}$ を生成し、中性子1個を放出する核反応の場合

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

反応前後の結合エネルギーの差に相当する $28.3-(2.23+8.48)=17.6\text{MeV}$ のエネルギー（核子あたり $3.52\text{MeV}$）をヘリウム原子核と中性子の運動エネルギーの形で放出する。

式（$\ref{nuclear_fusion}$）のように、質量数が小さい2つの軽い原子核が結合して反応前よりも質量数が大きい重い原子核を形成する反応を*核融合（nuclear fusion）*という。これは太陽をはじめとするすべての恒星のエネルギー源であり、いつかは人類が直接動力源として利用する日が来るだろう。

一方、結合エネルギーが約 $1780\text{MeV}$ の $^{235}\text{U}$ が中性子を吸収した後、結合エネルギーが $783\text{MeV}$ の $^{92}\text{Kr}$ と約 $1170\text{MeV}$ の $^{141}\text{Ba}$ に分離され、3個の中性子を放出する核反応の場合

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

反応前後の結合エネルギーの差に相当する $783+1170-1780=173\text{MeV}$ のエネルギー（核子あたり $0.733\text{MeV}$）を放出する。

式（$\ref{nuclear_fission}$）のように、重い原子核が軽い原子核に分離する反応を*核分裂（nuclear fission）*といい、アイゼンハワー第34代アメリカ大統領の「平和のための原子力（Atoms for Peace）」演説とソ連のオブニンスク原子力発電所以来、電力源として広く活用されている。
