---
title: シュレーディンガー方程式と波動関数
description: 量子力学において古典力学のニュートンの運動法則に相当するシュレーディンガー方程式の基本形を見ていきます。 また、シュレーディンガー方程式の解として得られる波動関数の物理的意味に関する統計的解釈と量子力学的不確定性に関する視点、そしてコペンハーゲン解釈における測定行為の物理的意味（波動関数の崩壊）について学びます。
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
mermaid: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - (時間依存)シュレーディンガー方程式：
>
> $$ i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi $$
>
> - 波動関数 $\Psi(x,t)$ の統計的解釈（ボルンの解釈）：波動関数の絶対値の二乗 $\|\Psi(x,t)\|^2$ は時刻 $t$、位置 $x$ で粒子を見つける**確率密度関数**である。
> - 波動関数の規格化：
>   - $\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx = 1$
>   - $\Psi(x,t)$ がシュレーディンガー方程式の解であれば、任意の複素数定数 $A$ に対して $A\Psi(x,t)$ も同様に解であり、このとき上式を満たすように定数 $A$ を決定することを規格化（normalization）という
>   - **規格化できない解（non-normalizable solutions）**は粒子を表すことができないため有効な波動関数ではなく、**二乗可積分（square-integrable）**な解のみが物理的に可能な状態である
>   - ある時点で規格化された波動関数は、時間が経過して $\Psi$ が変化しても、継続して規格化された状態を維持する
> - 確率流：
>   - $J(x,t) \equiv \cfrac{i\hbar}{2m}\left(\Psi\cfrac{\partial \Psi^\*}{\partial x}-\Psi^\*\cfrac{\partial \Psi}{\partial x}\right)$
>   - 粒子を見つける確率が点 $x$ を通過して流れる流量（単位時間あたりの確率）
>   - 時刻 $t$、領域 $a<x<b$ で粒子を見つける確率を $P_{ab}(t)$ とすると $\cfrac{dP_{ab}}{dt} = J(a,t) - J(b,t)$
{: .prompt-info }

## Prerequisites
- 連続確率分布と確率密度

## シュレーディンガー方程式（Schrödinger equation）
質量 $m$ の粒子が与えられた力 $F(x,t)$ を受けながら $x$ 軸上で動く状況を考えてみましょう。

古典力学では主な目標は、ニュートンの運動方程式 $F=ma$ を適用して任意の時間における粒子の位置 $x(t)$ を決定することです。このプロセスは大まかに次のようなダイアグラムで表現できます。

```mermaid
flowchart TD
	conditions["与えられた条件"] -- F=ma --> x["位置 x(t)"]
	x --> quantities["求めたい物理量"]
```

量子力学では同じ問題を非常に異なる方法でアプローチします。量子力学のアプローチは、次の**シュレーディンガー方程式（Schrödinger equation）**を解いて粒子の**波動関数** $\Psi(x,t)$ を求めることです。

$$ \begin{gather*}
i\hbar\frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}\\
\text{(} i=\sqrt{-1}\text{, } \hbar=\frac{h}{2\pi}=1.054573\times10^{-34}\text{, } h\text{：プランク定数, } V(x)\text{：ポテンシャルエネルギー)}
\end{gather*} $$

![Complex plot of a wave function that satisfies the nonrelativistic Schrödinger equation with V = 0(free particle)](https://upload.wikimedia.org/wikipedia/commons/b/b7/Wavepacket-a2k4-en.gif?20210105144724)
> *画像出典*
> - 作者：ウィキメディアユーザー Xcodexif
> - ライセンス：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

```mermaid
flowchart TD
	conditions["与えられた条件、通常 Ψ(x,0)"] -- "シュレーディンガー方程式" --> x["波動関数 Ψ(x,t)"]
	x --> quantities["求めたい物理量の確率分布"]
```

## 波動関数 $\Psi(x,t)$ の統計的解釈（ボルンの解釈）
古典力学における粒子は一点に位置するのに対し、量子力学で粒子の状態を表す波動関数は与えられた $t$ における $x$ の関数であり、つまり空間に広がっています。これの物理的意味をどのように解釈すべきでしょうか？

ボルン（Born）の**統計的解釈**によれば、波動関数の絶対値の二乗 $\|\Psi(x,t)\|^2$ は時刻 $t$、位置 $x$ で粒子を見つける確率密度関数です。波動関数 $\Psi$ 自体は複素数ですが、$\|\Psi\|^2=\Psi^*\Psi$（$\Psi^*$ は $\Psi$ の複素共役）は0以上の実数であるため、このような解釈が成り立ちます。つまり、次のように表現できます。

$$ \int_a^b |\Psi(x,t)|^2 dx = \text{時刻 }t\text{において }a\text{と }b\text{ の間で粒子を見つけられる確率}. \tag{2}$$

このような統計的解釈は、量子力学が一種の**不確定性（indeterminacy）**を内包することを意味します。粒子に関するすべて（波動関数）を知っていても、可能な結果の確率分布しか知ることができず、特定の値を決定することはできません。

これは直感的に受け入れがたいものだったため、自然とこのような不確定性が量子力学の何らかの欠点によるものなのか、それとも本質的な自然の特性なのかについての疑問が提起されました。

## 量子力学的不確定性（quantum indeterminacy）を見る視点
ある粒子の位置を測定して、この粒子が点 $C$ にあることがわかったとします。では、測定する直前に粒子はどこにあったのでしょうか？

### 実在論的（realist）立場

> "神はサイコロを振らない。" ("God does not play dice.")  
> *by アルベルト・アインシュタイン*

粒子はもともと $C$ にあった。これはアインシュタイン（Einstein）とシュレーディンガー（Schrödinger）の視点でもあります。しかし、このような視点から見ると、実際には粒子が正確に $C$ にあったのに理論の限界で測定前まで粒子の位置を確率分布でしか知ることができないため、量子力学は不完全な理論ということになります。つまり、この視点によれば、不確定性は本質的な自然の性質ではなく量子力学の限界によるものであり、$\Psi$ 以外の何らかの隠れた変数が追加的に存在し、これまで知らなければ粒子を完全に記述できないということになります。

> シュレーディンガー（Schrödinger）はアインシュタイン（Einstein）の弟子として一時期その下で助手として働いたこともあり、その後もアインシュタインと交流を続けました。シュレーディンガーの実在論的かつ決定論的な立場もその影響である可能性が高いです。
{: .prompt-info }

### 正統的（orthodox）立場

> "神がサイコロで何をしようと気にするな。" ("Stop telling God what to do with his dice.")  
> *by ニールス・ボーア、アインシュタインの先の引用への返答として*
>
> "観測は測定対象に干渉するだけでなく、作り出す" ("Observations not only disturb what is to be measured, they produce it")  
> ...  
> "我々が特定の位置を持つように強制しているのだ。" ("We compel to assume a definite position.")  
> *by パスクアル・ヨルダン*

測定直前まで粒子は確率分布の形でのみ存在し、どこにもなく、測定行為をしたときに初めて粒子がある一つの位置に現れます。このような解釈を**コペンハーゲン解釈**と呼び、コペンハーゲン大学でボーア（Bohr）とハイゼンベルク（Heisenberg）を中心に提案された解釈です。

> 面白いのは、アインシュタインとシュレーディンガーの関係と同様に、ハイゼンベルク（Heisenberg）もまたボーア（Bohr）の弟子だということです。
{: .prompt-info }

### 不可知論的（agnostic）立場

> "針の先にはどれだけ多くの天使が座れるかという古い質問のように、何も全く知ることができない何かがそれでも存在するかどうか考えて頭を悩ます必要はない。" ("One should no more rack one's brain about the problem of whether something one cannot know anything about exists all the same, than about the ancient question of how many angels are able to sit on the point of a needle.")  
> *by ヴォルフガング・パウリ*

回答を拒否します。測定する前の粒子の状態について何を主張しても、その主張が正しいかどうかを確認する唯一の方法が測定だとすれば、それはもはや「測定以前」ではなくなってしまうのに、どんな意味があるでしょうか？本質的に試すことができず、知ることができない何かについて議論することは形而上学に過ぎません。

### 今日の通念
1964年にジョン・ベル（John Bell）が測定の前後を問わず粒子が正確な位置に存在するかどうかによって観測可能な差があることを証明したことで、まず不可知論的立場は排除され、その後の実験を通じてコペンハーゲン解釈が主流となりました。したがって、特別な言及がない限り、通常量子力学について扱う際はこのようなコペンハーゲン解釈を前提とします。

> 非局所的隠れ変数理論（nonlocal hidden variable theories）や多世界解釈（many worlds interpretation）のような、コペンハーゲン解釈以外の正しい可能性のある他の解釈も依然として存在します。
{: .prompt-info }

## 測定と波動関数の崩壊
粒子は測定以前まで正確な位置を持っておらず、測定を通じて初めて $C$ という特定の位置（後で別の記事で扱いますが、実際にはハイゼンベルクの不確定性原理により、この位置も完全に正確な値ではなく、若干の誤差範囲を持ちます）を持つようになります。ただし、この最初の測定を行った直後にすぐに追加測定を行った場合、測定するたびに異なる値を得るのではなく、必ず同じ結果を得ます。これは次のように説明されます。

最初の測定を行う瞬間、測定対象の波動関数が激しく変化して点 $C$ 付近に集中した狭く尖った形の $\|\Psi(x,t)\|^2$ グラフを形成します。これを波動関数が測定によって点 $C$ に**崩壊（collapse）**したと言います。

つまり、物理過程は異なる二種類に分けることができます。
- シュレーディンガー方程式によって波動関数がゆっくりと変化する一般的な（ordinary）過程
- $\Psi$ が突然かつ不連続に崩壊する測定（measurement）過程

> 測定によって崩壊した波動関数は時間が経つとシュレーディンガー方程式に従って再び空間的に広がっていきます。したがって、同じ測定結果を再現するには二回目の測定をすぐに行う必要があります。
{: .prompt-tip }

## 波動関数の規格化（Normalization）
波動関数の絶対値の二乗 $\|\Psi(x,t)\|^2$ は時刻 $t$、位置 $x$ で粒子を見つける確率密度であるため、すべての $x$ について $\|\Psi\|^2$ を積分すると1になるはずです。

$$ \int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1. \label{eqn:wavefunction_norm}\tag{3} $$

式 ($\ref{eqn:schrodinger_eqn}$) において $\Psi(x,t)$ が解であれば、任意の複素数定数 $A$ に対して $A\Psi(x,t)$ も解であることがわかります。したがって、式 ($\ref{eqn:wavefunction_norm}$) を満たすようにこの $A$ を決定する必要があり、このプロセスを波動関数の規格化（normalization）と呼びます。シュレーディンガー方程式のいくつかの解は積分すると無限大に発散し、この場合、式 ($\ref{eqn:wavefunction_norm}$) を満たす定数 $A$ は存在しません。自明解（trivial solution）$\Psi=0$ の場合も同様です。このような**規格化できない解（non-normalizable solutions）**は粒子を表すことができないため、有効な波動関数ではありません。物理的に可能な状態は、シュレーディンガー方程式の**二乗可積分（square-integrable）**な解に対応します。

また、シュレーディンガー方程式の重要な性質は、<u>ある時点で規格化された波動関数は、時間が経過して $\Psi$ が変化しても、継続して規格化された状態（$\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1$）を維持する</u>ということです。波動関数を毎時点で異なる $A$ 値で規格化しなければならないとすれば、$A$ は定数ではなく時間 $t$ の関数となるため、もはやシュレーディンガー方程式の解を求めることができなくなりますが、この性質により初期条件（$t=0$）で規格化した $A$ 値は時間 $t$ に関係なく継続して保存されます。

### 証明

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \int_{-\infty}^{\infty} \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx. \label{eqn:norm_proof_1}\tag{4} $$

> $\|\Psi\|^2$ を $x$ について積分した結果は $t$ のみの関数であるため、左辺では全微分（$d/dt$）を使いますが、$\|\Psi\|^2$ 自体は $x$ と $t$ の二変数関数であるため、右辺では偏微分（$\partial/\partial t$）を使います。
{: .prompt-tip }

上式を積の微分規則に従って次のように書き換えることができます。

$$ \frac{\partial}{\partial t}|\Psi|^2 = \frac{\partial}{\partial t}(\Psi^*\Psi) = \Psi^*\frac{\partial \Psi}{\partial t} + \frac{\partial \Psi^*}{\partial t}\Psi. \label{eqn:norm_proof_2}\tag{5}$$

式 ($\ref{eqn:schrodinger_eqn}$) のシュレーディンガー方程式の両辺に $-\cfrac{i}{\hbar}$ をかけると

$$ \frac{\partial \Psi}{\partial t} = \frac{i\hbar}{2m}\frac{\partial^2 \Psi}{\partial x^2}-\frac{i}{\hbar}V\Psi \label{eqn:norm_proof_3}\tag{6}$$

と書くことができ、上式で $\cfrac{\partial \Psi}{\partial t}$ の複素共役を取ると

$$ \frac{\partial \Psi^*}{\partial t} = -\frac{i\hbar}{2m}\frac{\partial^2 \Psi^*}{\partial x^2}+\frac{i}{\hbar}V\Psi^* \label{eqn:norm_proof_4}\tag{7}$$

を得ます。ここで式 ($\ref{eqn:norm_proof_2}$) に ($\ref{eqn:norm_proof_3}$) と ($\ref{eqn:norm_proof_4}$) を代入すると

$$\begin{align*}
\frac{\partial}{\partial t}|\Psi|^2 &= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right) \\
&= \frac{\partial}{\partial x}\left[\frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right) \right] 
\end{align*} \label{eqn:norm_proof_5}\tag{8}$$

となり、これを最初の式 ($\ref{eqn:norm_proof_1}$) の右辺に代入すると

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|_{-\infty}^{\infty}. \label{eqn:norm_proof_6}\tag{9} $$

しかし、波動関数が規格化されて物理的に有効であるためには、$x$ が $\pm\infty$ に向かうとき $\Psi(x,t)$ は $0$ に収束しなければなりません。したがって

$$ \frac{d}{dt}\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 0 \label{eqn:norm_proof_fin}\tag{10} $$

となり、$\int_{-\infty}^{\infty} \|\Psi(x,t)\|^2 dx$ は時間に無関係な定数です。

$$ \therefore \Psi \text{がある時点 }t\text{で規格化されていれば、他のすべての時点 }t\text{についても規格化されている。} \blacksquare $$

## 確率流（probability current）
今度は時刻 $t$、領域 $a<x<b$ で粒子を見つける確率を $P_{ab}(t)$ としましょう。すると

$$ P_{ab}(t) = \int_a^b |\Psi(x,t)|^2 dx \tag{11}$$

となり、

$$ \begin{align*}
\frac{dP_{ab}}{dt} &= \frac{d}{dt}\int_a^b |\Psi(x,t)|^2 dx \\
&= \int_a^b \frac{\partial}{\partial t}|\Psi(x,t)|^2 dx \quad \text{(}\because\text{式 }\ref{eqn:norm_proof_1}\text{ 参照)}\\
&= \int_a^b \left(\frac{\partial \Psi^*}{\partial t}\Psi + \Psi^*\frac{\partial \Psi}{\partial t} \right)dx \quad \text{(}\because\text{式 }\ref{eqn:norm_proof_2}\text{ 参照)} \\
&= \frac{i\hbar}{2m}\int_a^b \left(\Psi^*\frac{\partial^2\Psi}{\partial x^2}-\frac{\partial^2\Psi^*}{\partial x^2}\Psi\right)dx \\
&= \frac{i\hbar}{2m}\int_a^b\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \quad \text{(}\because\text{式 }\ref{eqn:norm_proof_3},\ref{eqn:norm_proof_4},\ref{eqn:norm_proof_5}\text{ 参照)}\\
&= \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial \Psi}{\partial x}-\frac{\partial \Psi^*}{\partial x}\Psi \right)\Bigg|^b_a \\
&= \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x} \right)\Bigg|^a_b
\end{align*} $$

です。ここで

$$ J(x,t) \equiv \frac{i\hbar}{2m}\left(\Psi\frac{\partial \Psi^*}{\partial x}-\Psi^*\frac{\partial \Psi}{\partial x}\right) \label{eqn:probability_current}\tag{12}$$

とおくと、

$$ \frac{dP_{ab}}{dt} = J(a,t) - J(b,t) \label{eqn:probability_over_time}\tag{13}$$

となります。

式 ($\ref{eqn:probability_current}$) のように定義した $J(x,t)$ を**確率流（probability current）**と呼び、粒子を見つける確率が点 $x$ を通過して流れる流量\*（つまり、単位時間あたりの確率）を意味します。式 ($\ref{eqn:probability_over_time}$) において、特定の時刻 $t$ に一方の端から流れ込む確率流 $J(a,t)$ が他方から流れ出る確率流 $J(b,t)$ より大きければ $P_{ab}$ は増加し、逆の場合には減少します。

> *流体力学の流量（flow rate）で流体の質量または体積がここでは確率に置き換わったと考えればよいです。
{: .prompt-info }
