---
title: 相對性原理與洛倫茲變換
description: 探討參考系的概念和古典力學中廣泛使用的伽利略變換座標變換。此外,簡要介紹麥克斯韋方程式和邁克爾遜-莫雷實驗作為洛倫茲變換的背景,並推導洛倫茲變換矩陣。
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **相對性原理**: 在等速運動的不同參考系中,所有物理定律應該是相同的原理
{: .prompt-info }

> **洛倫茲因子 $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **洛倫茲變換**
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

> **逆洛倫茲變換**
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

## 參考系與相對性原理
### 參考系 (frame of reference)
- **參考系(frame of reference)**: 物體運動意味著其位置相對於其他物體發生變化,由於所有運動都是相對的,因此為了描述運動,必須設定一個參考系作為基準。
- **慣性參考系(inertial frames of reference)**: 符合牛頓(Newton)第一運動定律("物體所受的合力為0時,其運動狀態保持不變")的系統。相對於一個慣性系以等速度運動的任何參考系都是慣性參考系。

### 相對性原理 (Principle of Relativity)
這是物理學的主要概念之一和基本前提,即在等速運動的不同參考系中,所有物理定律應該是相同的原理。如果相對運動的觀察者之間的物理定律不同,那麼可以利用這種差異來設定一個絕對參考系,從而確定誰是靜止的,誰是運動的。然而,根據相對性原理,這種區別是不存在的,因此對整個宇宙而言,不存在絕對參考系或絕對運動,所有慣性參考系都是等價的。

## 伽利略變換的局限性
### 伽利略變換 (Galilean transformation)
假設存在兩個慣性系 $S$ 和 $S^{\prime}$, $S^{\prime}$ 相對於 $S$ 以恆定速度 $\vec{v}$ 沿 $+x$ 方向運動,同一事件在 $S$ 中被觀察到發生在時刻 $t$ 的座標 $(x, y, z)$,而在 $S^{\prime}$ 中被觀察到發生在時刻 $t^{\prime}$ 的座標 $(x^{\prime}, y^{\prime}, z^{\prime})$。

此時, $S^{\prime}$ 中測量的運動 $x$ 方向值將比 $S$ 中測量的值大 $S^{\prime}$ 相對於 $S$ 在 $x$ 方向移動的距離 $\vec{v}t$,因此

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

而在 $y$ 和 $z$ 方向上沒有相對運動,所以

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

直觀上,我們可以假設

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

從式 ($\ref{eqn:galilean_transform_x}$) 到 ($\ref{eqn:galilean_transform_t}$) 這樣的不同慣性系之間的座標變換在物理學中被稱為**伽利略變換(Galilean transformation)**,這在日常情況下大多是正確的,簡單而直觀。然而,如後所述,這與麥克斯韋方程式相矛盾。

### 麥克斯韋方程式
19世紀後期,麥克斯韋(Maxwell)擴展了法拉第(Faraday)、安培(Ampere)等其他科學家提出的想法和先前的研究結果,揭示了電和磁實際上是同一種力,並推導出描述電磁場的以下四個方程式。

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: 通過任意閉合曲面的電通量等於內部的淨電荷量(高斯定律).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: 不存在磁單極(磁荷).}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: 磁場的變化產生電場(法拉第定律).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: 電場的變化和電流產生磁場.(安培-麥克斯韋定律)}
\end{gather*}$$

麥克斯韋方程式成功解釋了之前所有已知的電和磁現象,預測了電磁波的存在,並推導出真空中電磁波的速度 $c$ 是不變的常數,成為電磁學的核心公式。

### 伽利略變換與麥克斯韋方程式之間的矛盾
使用伽利略變換的牛頓力學已經作為物理學的基礎超過200年,而麥克斯韋方程式如上所述是描述電和磁現象的核心方程式。然而,這兩者之間存在以下矛盾:

- 根據相對性原理,麥克斯韋方程式也應該在所有慣性系中具有相同的形式,但是當我們將在一個慣性系中測量的值通過伽利略變換轉換為在另一個慣性系中測量的值時,麥克斯韋方程式會呈現出非常不同的形式。
- 從麥克斯韋方程式可以計算出光速 $c$ 的大小,且這是一個不變的常數,但根據牛頓力學和伽利略變換,光速 $c$ 在不同的慣性系中會被測量為不同的值。

因此,麥克斯韋方程式和伽利略變換是不相容的,至少需要修改其中之一。這成為後面將要討論的**洛倫茲變換(Lorentz transformation)**的出現背景。

## 以太(aether)理論與邁克爾遜-莫雷實驗
另一方面,19世紀的物理學認為光也像水波或聲波等其他波動一樣,是通過一種假想的介質*以太(aether)*傳播的,並努力發現這種以太的存在。

根據以太理論,即使宇宙空間是真空,也充滿了以太,因此由於地球以約30km/s的速度相對於太陽運動,會形成穿過地球的以太風。  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *圖片來源*
> - 作者: 維基媒體用戶 [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - 授權: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

為了驗證這個假設,1887年邁克爾遜(Michelson)與莫雷(Morley)合作,使用下面的干涉儀進行了*邁克爾遜-莫雷實驗(Michelson-Morley Experiment)*。  
![邁克爾遜-莫雷干涉儀](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *圖片來源*
> - 作者: Albert Abraham Michelson with Edward Morley
> - 授權: public domain

在這個實驗中,光線通過半鏡分成兩束,分別在干涉儀的兩個垂直臂上來回行進約11米,然後在中間點相遇,此時根據兩束光的相位差,會出現增強干涉或抵消干涉的條紋。根據以太理論,由於相對於以太的速度不同,光速應該有差異,因此這個相位差也會改變,應該能觀察到干涉條紋的變化。然而,實際上並沒有觀察到干涉條紋的變化。為了解釋這個實驗結果,有多種嘗試,其中菲茨傑拉德(FitzGerald)和洛倫茲(Lorentz)提出了當物體<u>相對於以太運動時</u>長度會收縮的*洛倫茲-菲茨傑拉德收縮(Lorentz–FitzGerald contraction)*或*長度收縮(length contraction)*,這導致了洛倫茲變換的產生。

> 洛倫茲當時相信以太的存在,並認為長度收縮是由相對於以太的運動引起的。後來愛因斯坦(Einstein)通過*特殊相對論(Theory of Special Relativity)*解釋了洛倫茲變換的真正物理意義,用時空的概念而不是以太來解釋長度收縮,並且後來證明以太是不存在的。
{: .prompt-info }

## 洛倫茲變換 (Lorentz transformation)
### 洛倫茲變換的推導
在前面討論的伽利略變換(式 [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$])的相同情況下,假設 $x$ 和 $x^{\prime}$ 之間不與麥克斯韋方程式矛盾的正確變換關係如下:

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

這裡 $\gamma$ 與 $x$ 和 $t$ 無關,但可能是 $\vec{v}$ 的函數。我們可以這樣假設的原因如下:

- 為了使 $S$ 中發生的事件與 $S^{\prime}$ 中發生的事件一一對應, $x$ 和 $x^{\prime}$ 應該是線性關係。
- 已知伽利略變換在日常情況下的力學中是正確的,所以應該能近似為式 ($\ref{eqn:galilean_transform_x}$)。
- 形式應盡可能簡單。

物理公式在參考系 $S$ 和 $S^{\prime}$ 中應該具有相同的形式,所以要用 $x^{\prime}$ 和 $t$ 表示 $x$ 時,只需改變 $\vec{v}$ 的符號(相對運動的方向),而兩個參考系之間除了 $\vec{v}$ 的符號外沒有任何區別,所以 $\gamma$ 應該相同。

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

與伽利略變換一樣,垂直於 $\vec{v}$ 方向的分量 $y$ 和 $y^{\prime}$, 以及 $z$ 和 $z^{\prime}$ 沒有理由不同,所以我們設:

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

現在將式 ($\ref{eqn:lorentz_transform_x}$) 代入 ($\ref{eqn:lorentz_transform_x_inverse}$),得到:

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

對 $t^{\prime}$ 進行整理,得到:

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

此外,為了不與麥克斯韋方程式矛盾,兩個參考系中的光速都應該是 $c$,我們可以利用這一點來求解 $\gamma$。假設 $t=0$ 時兩個參考系的原點在同一位置,這個初始條件意味著 $t^\prime = 0$。現在考慮 $t=t^\prime=0$ 時在 $S$ 和 $S^\prime$ 的共同原點有一個閃光,每個參考系的觀察者測量這個光的速度的情況。在這種情況下,在參考系 $S$ 中:

$$ x = ct \label{eqn:ct_S}\tag{9}$$

在參考系 $S^\prime$ 中:

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

使用式 ($\ref{eqn:lorentz_transform_x}$) 和 ($\ref{eqn:lorentz_transform_t}$) 替換上式中的 $x$ 和 $t$,得到:

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

對 $x$ 進行求解:

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

但是根據前面的式 ($\ref{eqn:ct_S}$), $x=ct$,所以:

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

因此:

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

將這個 $\vec{v}$ 的 $\gamma$ 表達式代入式 ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), ($\ref{eqn:lorentz_transform_t}$),我們最終得到從參考系 $S$ 到 $S^\prime$ 的變換式。

### 洛倫茲變換的變換矩陣

我們最終得到的變換式如下:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

這些式子就是**洛倫茲變換(Lorentz transformation)**。如果我們令 $\vec{\beta}=\vec{v}/c$,可以用矩陣表示如下:

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

洛倫茲(Lorentz)證明,使用這個變換式時,所有慣性參考系中的電磁基本公式都以相同的形式成立。此外,我們也可以看到,當速度 $v$ 相對於光速 $c$ 非常小時, $\gamma \to 1$,因此可以近似為伽利略變換。

### 逆洛倫茲變換 (inverse Lorentz transformation)
有時,將靜止系 $S$ 中的測量轉換為運動系 $S^\prime$ 中的測量不如反過來將運動系 $S^\prime$ 中的測量轉換為 $S$ 中的測量更方便。
在這種情況下,我們可以使用**逆洛倫茲變換(inverse Lorentz transformation)**。  
求 ($\ref{lorentz_transform_matrix}$) 的逆矩陣,我們得到以下逆洛倫茲變換矩陣:

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

這等同於將式 ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) 中帶有撇號和不帶撇號的物理量互換,並將 $v$ 替換為 $-v$(即將 $\beta$ 替換為 $-\beta$)。

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
