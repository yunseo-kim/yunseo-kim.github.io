---
title: 相対性原理とローレンツ変換
description: 基準系の概念と古典力学で広く使われてきた座標変換であるガリレイ変換について学ぶ。またローレンツ変換の登場背景となったマクスウェル方程式とマイケルソン-モーリー実験を簡単に見て、ローレンツ変換の変換行列を導出する。
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **相対性原理**: 等速度で運動する互いに異なる基準系に対して、すべての物理法則が同一でなければならないという原理
{: .prompt-info }

> **ローレンツ因子 $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **ローレンツ変換**
>
> $$ \begin{pmatrix}
> \vec{x}^\prime \\ ct^\prime
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & -\gamma\vec{\beta} \\
> -\gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}. $$
>
> - $ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $
> - $ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $
{: .prompt-info }

> **逆ローレンツ変換**
>
> $$ \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & \gamma\vec{\beta} \\
> \gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x^\prime} \\ ct^\prime
> \end{pmatrix}. $$
>
> - $ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime $
> - $ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} $
{: .prompt-info }

## 基準系と相対性原理
### 基準系 (frame of reference)
- **基準系(frame of reference)**: ある物体が動くということは、その位置が他の物体に対して相対的に変化するということであり、すべての運動は相対的であるため、ある運動を記述するためにはその基準となる基準系を設定する必要がある。
- **慣性基準系(inertial frames of reference)**: ニュートン(Newton)の運動第1法則（「物体に作用する正味の力が0である限り、物体の運動状態は不変である」）が成立する系。ある慣性系に対して等速度で動く任意の基準系は慣性基準系である。

### 相対性原理 (Principle of Relativity)
物理学の主要な概念の一つであり基本前提として、等速度で運動する互いに異なる基準系に対して、すべての物理法則が同一でなければならないという原理である。もし相対的に動く観測者たちに物理法則が互いに異なるならば、この差を利用して一つの絶対基準系を設定し、誰が静止していて誰が動いているかを知ることができるだろう。しかし相対性原理によれば、そのような区別はないため、全宇宙に対する絶対基準系または絶対運動は存在せず、すべての慣性基準系は同等である。

## ガリレイ変換の限界点
### ガリレイ変換 (Galilean transformation)
二つの慣性系$S$と$S^{\prime}$が存在し、$S^{\prime}$は$S$に対して$+x$方向の一定速度$\vec{v}$で動いており、同一の一つの事象を$S$では時刻$t$のとき座標$(x, y, z)$で起こったものとして、$S^{\prime}$では時刻$t^{\prime}$のとき座標$(x^{\prime}, y^{\prime}, z^{\prime})$で起こったものとして観察したとしよう。

このとき、$S^{\prime}$で測定した運動の$x$方向の値は$S$で測定した値より$S^{\prime}$が$S$に対して$x$方向に動いた距離である$\vec{v}t$だけ大きいはずなので

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

であり、$y$と$z$方向には相対的な運動がないので

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

であり、直感的に

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

であると仮定できる。上記の式($\ref{eqn:galilean_transform_x}$)から($\ref{eqn:galilean_transform_t}$)までのように物理学で古典的に使用してきた互いに異なる慣性系間の座標変換を**ガリレイ変換(Galilean transformation)**と呼び、これは日常的な状況でほとんど一致するため、シンプルかつ直感的である。しかし後述するように、これはマクスウェル方程式と矛盾する。

### マクスウェル方程式
ファラデー(Faraday)、アンペール(Ampere)などの他の科学者が提案したアイデアと先行研究結果を11800年代後半にマクスウェル(Maxwell)が拡張し、電気と磁気は実際に一つの力であることを明らかにし、電磁場を記述する次の4つの方程式を導出した。

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: 任意の閉曲面を通過する電気束は内部の正味電荷量と同じである（ガウスの法則）。}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: 磁気単極子（磁荷）は存在しない。}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: 磁場の変化は電場を作る（ファラデーの法則）。}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: 電場の変化と電流は磁場を作る（アンペール-マクスウェルの法則）。}
\end{gather*}$$

マクスウェル方程式はそれまで知られていた電気と磁気現象をすべて成功裏に説明でき、電磁波の存在を予測し、また真空中での電磁波の速さ$c$は不変の定数であることを導き出し、電磁気学の核心公式として位置づけられた。

### ガリレイ変換とマクスウェル方程式の間の矛盾
ガリレイ変換を活用するニュートン力学は200年以上物理学の基盤となってきており、マクスウェル方程式は上述したように電気と磁気現象を記述する核心方程式である。しかしこの二つの間には次のような矛盾が生じる。

- 相対性原理によればマクスウェル方程式もすべての慣性系で同じ形を持つことが期待されるが、ある慣性系で測定した値をガリレイ変換を適用して別の慣性系で測定した値に変換すると、マクスウェル方程式は非常に異なる形を持つことになる。
- マクスウェル方程式から光速$c$の大きさを計算でき、これは不変の定数であるが、ニュートン力学とガリレイ変換によれば光速$c$は慣性系によって異なって測定される。

したがって、マクスウェル方程式とガリレイ変換は互いに合わず、少なくともどちらか一方を修正する必要があった。これは後述する**ローレンツ変換(Lorentz transformation)**の登場背景となる。

## エーテル(aether)理論とマイケルソン-モーリー実験
一方、11800年代の物理学では、光も水面波や音波のような他の波と同様に*エーテル(aether)*という仮想の媒質によって伝達されると考えられており、このエーテルの存在を発見しようと努力した。

エーテル理論によれば、宇宙空間は真空であっても、エーテルで満たされているため、太陽に対して約30km/sの速さで運動する地球の公転によって、地球を横切るエーテル風が形成されると考えられた。  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *画像出典*
> - 作者: ウィキメディアユーザー [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - ライセンス: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

このような仮説を検証するために、[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar)11887年、マイケルソン(Michelson)はモーリー(Morley)と協力して、以下の干渉計を活用した*マイケルソン-モーリー実験(Michelson-Morley Experiment)*を行った。  
![マイケルソン-モーリー干渉計](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *画像出典*
> - 作者: Albert Abraham Michelson with Edward Morley
> - ライセンス: public domain

この実験では、光線は半透明鏡を通過する際に2つに分かれ、それぞれ干渉計の直交する二つの腕を往復しながら合計約11mほど進み、中間地点で出会い、このとき二つの光線の位相差によって強め合う干渉または弱め合う干渉模様が現れる。エーテル理論によれば、エーテルに対する相対速度によって光の速度に差が生じるため、この位相差も変化し、干渉模様の変化を観測できるはずだと期待されたが、実際には干渉模様の変化を観測することができなかった。このような実験結果を説明するためにいくつかの試みがあったが、その中でもフィッツジェラルド(FitzGerald)とローレンツ(Lorentz)は、ある物体が<u>エーテルに対して相対的に運動する場合</u>、長さが収縮するという*ローレンツ-フィッツジェラルド収縮(Lorentz–FitzGerald contraction)*または*長さの収縮(length contraction)*を提案し、これはローレンツ変換につながる。

> ローレンツはこの当時、エーテルが存在すると信じており、長さの収縮がエーテルに対する相対的運動によって起こると考えていた。その後、アインシュタイン(Einstein)が*特殊相対性理論(Theory of Special Relativity)*でローレンツ変換が持つ真の物理的意味を解釈することによって、エーテルではなく時空間の概念で長さの収縮を説明し、エーテルは存在しないということもその後明らかになる。
{: .prompt-info }

## ローレンツ変換 (Lorentz transformation)
### ローレンツ変換の導出
先に見たガリレイ変換（式[$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]）と同じ状況で、マクスウェル方程式と矛盾しない$x$と$x^{\prime}$の間の正しい変換関係が次のようであると仮定しよう。

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

ここで$\gamma$は$x$と$t$には無関係だが、$\vec{v}$の関数である可能性はある。このように仮定できる理由は次の通りである。

- $S$で起こる事象と$S^{\prime}$で起こる事象が一対一対応するためには、$x$と$x^{\prime}$は線形関係でなければならない。
- ガリレイ変換が日常的な状況の力学では正しいことが知られているので、式($\ref{eqn:galilean_transform_x}$)で近似できなければならない。
- できるだけ単純な形でなければならない。

物理公式は基準系$S$と$S^{\prime}$で同じ形でなければならないので、$x$を$x^{\prime}$と$t$で表すには$\vec{v}$の符号（相対運動の方向）だけを変えればよく、二つの基準系の間には$\vec{v}$の符号以外には何の違いもないはずなので、$\gamma$は同じでなければならない。

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

ガリレイ変換と同様に、$\vec{v}$の方向に垂直な成分である$y$と$y^{\prime}$、そして$z$と$z^{\prime}$は異なる理由がないので、

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

とする。ここで式($\ref{eqn:lorentz_transform_x}$)を($\ref{eqn:lorentz_transform_x_inverse}$)に代入すると

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

となるので、$t^{\prime}$について整理すると

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

が成立する。

またマクスウェル方程式と矛盾しないためには、二つの基準系での光速は$c$で同じでなければならないので、これを利用して$\gamma$を求めることができる。$t=0$のとき二つの基準系の原点が同じ場所にあったとすると、この初期条件により$t^\prime = 0$である。ここで$t=t^\prime=0$のとき$S$と$S^\prime$の共通原点で閃光があり、各基準系の観測者がこの光の速さを測定する状況を考えてみよう。この場合、基準系$S$では

$$ x = ct \label{eqn:ct_S}\tag{9}$$

であり、基準系$S^\prime$では

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

である。式($\ref{eqn:lorentz_transform_x}$)と($\ref{eqn:lorentz_transform_t}$)を用いて上式の$x$と$t$を置き換えると

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

となる。この式を$x$について解くと

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

となる。しかし先ほど式($\ref{eqn:ct_S}$)で$x=ct$であるので、

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

であり、したがって

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

である。この$\vec{v}$に対する$\gamma$の式を式($\ref{eqn:lorentz_transform_x}$)、($\ref{eqn:lorentz_transform_yz}$)、($\ref{eqn:lorentz_transform_t}$)に代入すると、最終的に基準系$S$から$S^\prime$への変換式が得られる。

### ローレンツ変換の変換行列

前に最終的に得られた変換式は次の通りである。

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

これらの式が**ローレンツ変換(Lorentz transformation)**である。$\vec{\beta}=\vec{v}/c$とすると、行列では以下のように表現できる。

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}. \label{lorentz_transform_matrix}\tag{16}$$

ローレンツ(Lorentz)はこの変換式を使用するとき、すべての慣性基準系で電磁気の基本公式が同じ形で成立することを示した。また速さ$v$が光速$c$に比べて非常に小さいときは$\gamma \to 1$となるので、ガリレイ変換で近似できることも確認できる。

### 逆ローレンツ変換 (inverse Lorentz transformation)
時には静止した系$S$での測定を動く系$S^\prime$での測定に変換するよりも、逆に動く系$S^\prime$での測定を$S$での測定に変換する方が便利な場合がある。
このような場合には**逆ローレンツ変換(inverse Lorentz transformation)**を使用できる。  
($\ref{lorentz_transform_matrix}$)の逆行列を求めると、次のような逆ローレンツ変換行列が得られる。

$$ \begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & 0 & 0 & \gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix}. \tag{17}
$$

これは式($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$)のプライムが付いた物理量と付いていない物理量を互いに入れ替え、$v$を$-v$に（つまり、$\beta$を$-\beta$に）置き換えたものと同じである。

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
