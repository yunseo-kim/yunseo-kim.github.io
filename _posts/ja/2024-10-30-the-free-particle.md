---
title: 自由粒子（The Free Particle）
description: ポテンシャルV(x)=0の自由粒子の場合、変数分離した解を規格化できないという事実とその意味を探り、 一般解に対する位置-運動量の不確定性関係を定性的に示し、Ψ(x,t)の位相速度と群速度を求めて物理的に解釈する。
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - 自由粒子：$V(x)=0$、境界条件なし（任意のエネルギー）
> - 変数分離した解 $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$は二乗積分すると無限大に発散するため規格化できず、これは以下を示唆する
>   - 自由粒子は定常状態で存在できない
>   - 自由粒子はエネルギーを正確な一つの値として定義できない（エネルギーの不確定性が存在）
> - それにもかかわらず、時間依存のシュレーディンガー方程式の一般解は変数分離した解の線形結合であるため、変数分離した解は依然として数学的には重要な意味を持つ。ただし、この場合制限条件がないため、一般解は不連続変数$n$に対する和($\sum$)ではなく連続変数$k$に対する積分($\int$)の形をとる。
> - シュレーディンガー方程式の一般解：
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{ここで }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - 位置の不確定性と運動量の不確定性の関係：
>   - 位置の不確定性が小さくなると運動量の不確定性は大きくなり、逆に運動量の不確定性が小さくなると位置の不確定性が大きくなる
>   - つまり、量子力学的に自由粒子の位置と運動量を同時に正確に知ることは不可能
> - 波動関数 $\Psi(x,t)$の位相速度と群速度：
>   - 位相速度：$v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - 群速度：$v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - 群速度の物理的意味と古典力学との比較：
>   - 物理的に群速度はその粒子の運動速度を意味する
>   - $\phi(k)$がある値 $k_0$ 付近で非常に鋭い形状だと仮定すると（運動量の不確定性が十分に小さい時）、
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Prerequisites
- オイラーの公式
- フーリエ変換（Fourier transform）＆プランシェレルの定理（Plancherel's theorem）
- [シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/)
- [時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/)
- [1次元無限井戸型ポテンシャル](/posts/the-infinite-square-well/)

## モデル設定
最も単純な場合である自由粒子（$V(x)=0$）を考えよう。古典的にはこれは単に等速度運動に過ぎないが、量子力学ではこの問題はより興味深い。  
自由粒子に対する[時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/)は

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

すなわち

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{、ここで }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

である。[ここまではポテンシャルが$0$の無限井戸型ポテンシャルの内部と同じである](/posts/the-infinite-square-well/#モデルおよび境界条件の設定)。ただし今回は一般解を次の指数関数の形で書こう。

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$と $C\cos{kx}+D\sin{kx}$は同じ$x$の関数を書く同等の方法である。オイラーの公式 $e^{ix}=\cos{x}+i\sin{x}$により
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> つまり、$C=A+B$、$D=i(A-B)$とすると
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> 逆に$A$と$B$を$C$と$D$で表すと$A=\cfrac{C-iD}{2}$、$B=\cfrac{C+iD}{2}$である。
>
> 量子力学では$V=0$の時、指数関数は動く波を表し、自由粒子を扱う際に最も便利である。一方、正弦と余弦関数は定在波を表すのに適しており、無限井戸型ポテンシャルの場合に自然に現れる。
{: .prompt-info }

無限井戸型ポテンシャルとは異なり、今回は$k$と$E$を制限する境界条件がない。つまり自由粒子は任意の正のエネルギーを持つことができる。

## 変数分離した解と位相速度
$\psi(x)$に時間依存性 $e^{-iEt/\hbar}$をつけると

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

を得る。

このように特別な形 $(x\pm vt)$に依存する$x$と$t$の任意の関数は、形が変わらず速度$v$で$\mp x$方向に動く波を表す。したがって式 ($\ref{eqn:Psi_seperated_solution}$)の第1項は右に動く波を表し、第2項は同じ波長と進行速度を持ち振幅だけが異なる波が左に動くことを表す。これらは$k$の前の符号だけが異なるので

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

と書くことができ、この時$k$の符号による波の進行方向は次のようになる。

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{右に移動}, \\
k<0 \Rightarrow & \text{左に移動}.
\end{cases} \tag{6}$$

自由粒子の「定常状態」は明らかに進行する波で*、その波長は $\lambda = 2\pi/\|k\|$であり、ド・ブロイの式（de Broglie formula）により

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

の運動量を持つ。

> *「定常状態」なのに進行する波というのは物理的には当然矛盾である。理由はすぐに出てくる。
{: .prompt-info }

またこの波の速度は次のようになる。

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

（ここで$\omega$は$t$の前の係数 $\cfrac{\hbar k^2}{2m}$である。）

しかし、この波動関数は二乗積分すると無限大に発散するため規格化できない。

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

つまり、<u>自由粒子の場合、変数分離した解は物理的に可能な状態ではない。</u>自由粒子は[定常状態](/posts/time-independent-schrodinger-equation/#1-定常状態stationary-statesである)で存在できず、[ある特定のエネルギー値](/posts/time-independent-schrodinger-equation/#2-ある範囲を持つ確率分布ではなく一つの明確な全エネルギー値eを持つ状態である)を持つこともできない。実際、直感的に考えても両端に境界条件が全くないのに定在波が形成されるほうが不自然である。

## 時間依存のシュレーディンガー方程式の一般解 $\Psi(x,t)$ を求める
それにもかかわらず、この変数分離した解は依然として重要な意味を持つ。物理的な解釈とは別に、[時間依存のシュレーディンガー方程式の一般解は変数分離した解の線形結合](/posts/time-independent-schrodinger-equation/#3-時間依存シュレーディンガー方程式の一般解は変数分離解の線形結合である)という数学的な意味を持つからである。ただし、この場合制限条件がないため、一般解は不連続変数$n$に対する和($\sum$)ではなく連続変数$k$に対する積分($\int$)の形をとる。

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> ここでは $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$が['時間に依存しないシュレーディンガー方程式'の記事の式(21)](/posts/time-independent-schrodinger-equation/#3-時間依存シュレーディンガー方程式の一般解は変数分離解の線形結合である)での$c_n$と同じ役割を果たす。
{: .prompt-info }

この波動関数は適切な$\phi(k)$に対して規格化できるが、必ず$k$の領域がなければならず、したがってエネルギーと速度の範囲を持つ。これを**波束（wave packet）**という。

> 正弦関数は空間的に無限に広がっているため規格化できない。しかし、このような波を複数重ね合わせると干渉により局所化され、規格化できるようになる。
{: .prompt-info }

## プランシェレルの定理（Plancherel theorem）を用いた $\phi(k)$ の導出

今や$\Psi(x,t)$の形（式[$\ref{eqn:Psi_general_solution}$]）がわかっているので、初期波動関数

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

を満たす$\phi(k)$を決定するだけでよい。これはフーリエ解析（Fourier analysis）の典型的な問題で、**プランシェレルの定理（Plancherel's theorem）**で答えを得ることができる。

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$を$f(x)$の**フーリエ変換（Fourier transform）**といい、$f(x)$は$F(k)$の**逆フーリエ変換（inverse Fourier transform）**という。両者の違いは指数の符号だけであることが式($\ref{eqn:plancherel_theorem}$)から容易に確認できる。もちろん、積分が存在する関数のみが許容されるという制限条件が存在する。

> $f(x)$が存在するための必要十分条件は $\int_{-\infty}^{\infty}\|f(x)\|^2dx$が有限でなければならないということである。この場合 $\int_{-\infty}^{\infty}\|F(k)\|^2dk$も有限であり、
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> である。人によっては式($\ref{eqn:plancherel_theorem}$)ではなく上の式をプランシェレルの定理（Plancherel's theorem）と呼ぶこともある（[ウィキペディア](https://en.wikipedia.org/wiki/Plancherel_theorem)でもこのように記述されている）。
{: .prompt-info }

今回の場合、$\Psi(x,0)$が規格化されなければならないという物理的な条件により、必ず積分が存在する。したがって、自由粒子に対する量子力学的解は式($\ref{eqn:Psi_general_solution}$)であり、ここで

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

である。

> ただし、実際には式($\ref{eqn:Psi_general_solution}$)の積分を解析的に解くことができる場合はほとんどない。通常はコンピュータで数値解析を用いて値を求める。
{: .prompt-tip }

## 波束の群速度の計算と物理的解釈

本質的に波束は$\phi$により振幅が決定される多数の正弦関数の重ね合わせである。つまり、波束を形成する「包絡線（envelope）」の中に「さざ波（ripples）」がある。

![A wave packet with the group velocity larger(5x) than phase velocity](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/wave_packet.gif)
> *画像ライセンスおよび原作出典の告知*
> - 画像生成ソースコード（gnuplot）：[yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/wave_packet.plt)
> - ライセンス：[Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualization/blob/main/LICENSE)
> - 原作者：[Ph.D. Youjun Hu](https://github.com/youjunhu)
> - 原ライセンス告知：[MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

物理的に粒子の速度に相当するのは、先ほど式($\ref{eqn:phase_velocity}$)で求めた個々のさざ波の速度（**位相速度、phase velocity**）ではなく、外側の包絡線の速度（**群速度、group velocity**）である。

### 位置の不確定性と運動量の不確定性の関係
式($\ref{eqn:Psi_at_t_0}$)の被積分項 $\int\phi(k)e^{ikx}dk$と、式($\ref{eqn:phi}$)の被積分項 $\int\Psi(x,0)e^{-ikx}dx$ 部分だけを別に取り出して位置の不確定性と運動量の不確定性の間の関係を見てみよう。

#### 位置の不確定性が小さい場合
位置空間で$\Psi$がある値$x_0$周辺の非常に狭い領域 $[x_0-\delta, x_0+\delta]$に分布し、それ以外の領域ではほぼ0の形状である場合（<u>位置の不確定性が小さい場合</u>）、$e^{-ikx} \approx e^{-ikx_0}$で$x$についてほぼ定数なので

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{eqn. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

である。定積分項は$p$について定数なので、前の$e^{-ipx_0/\hbar}$項により$\phi$は運動量空間で$p$に対する正弦波の形を取り、つまり広い運動量区間に分布する（<u>運動量の不確定性が大きい</u>）。

#### 運動量の不確定性が小さい場合
同様に運動量空間で$\phi$がある値$p_0$周辺の非常に狭い領域 $[p_0-\delta, p_0+\delta]$に分布し、それ以外の領域ではほぼ0の形状である場合（<u>運動量の不確定性が小さい場合</u>）、式($\ref{eqn:de_broglie_formula}$)により $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$で$p$についてほぼ定数であり、$dk=\frac{1}{\hbar}dp$なので

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

である。前の$e^{ip_0x/\hbar}$項により$\Psi$は位置空間で$x$に対する正弦波の形を取り、つまり広い位置区間に分布する（<u>位置の不確定性が大きい</u>）。

#### 結論
位置の不確定性が小さくなると運動量の不確定性は大きくなり、逆に運動量の不確定性が小さくなると位置の不確定性が大きくなる。したがって、量子力学的に自由粒子の位置と運動量を同時に正確に知ることは不可能である。

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *画像出典*
> - 作者：英語版ウィキペディアユーザー [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - ライセンス：public domain

> 実際、不確定性原理（uncertainty principle）により、これは自由粒子だけでなくすべての場合に適用される。不確定性原理については後日別の記事で扱うことにする。
{: .prompt-info }

### 波束の群速度
式($\ref{eqn:Psi_general_solution}$)の一般解を式($\ref{eqn:phase_velocity}$)と同様に $\omega \equiv \cfrac{\hbar k^2}{2m}$で書き直すと

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

となる。

> $\omega = \cfrac{\hbar k^2}{2m}$のように$\omega$を$k$の関数として表した式を**分散関係（dispersion relation）**という。以下の内容は分散関係に関係なく、すべての波束に対して一般的に適用される。
{: .prompt-info }

ここで$\phi(k)$が適切な値$k_0$付近で非常に鋭い形状だと仮定しよう。（$k$に対して広く広がっていても構わないが、このような波束の形状は非常に速く歪み、別の形に変わる。異なる$k$に対する成分はそれぞれ異なる速度で動くため、よく定義された速度を持つ全体の「群れ」という意味を失う。つまり、<u>運動量の不確定性が大きくなる。</u>）  
積分される関数は$k_0$付近を除いて無視できるので、この点付近で関数$\omega(k)$をテイラー展開でき、一次項まで書くと

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

を得る。ここで$s=k-k_0$と置換して$k_0$を中心に積分すると

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

前にある項 $e^{i(k_0x-\omega_0t)}$は速度 $\omega_0/k_0$で動く正弦波（「さざ波」）を意味し、この正弦波の振幅を決定する積分項（「包絡線」）は $e^{is(x-\omega_0^\prime t)}$ 部分により速度 $\omega_0^\prime$で動く。したがって $k=k_0$での位相速度は

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

で式($\ref{eqn:phase_velocity}$)での値と同じであることを再確認でき、群速度は

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

で位相速度の2倍になる。

## 古典力学との比較

巨視的なスケールで古典力学が成り立つことを知っているので、量子力学を通じて得た結果は量子論的な不確定性が十分に小さい時に古典力学での計算結果に近似できるはずである。今扱っている自由粒子の場合、先ほど仮定したように$\phi(k)$が適切な値$k_0$付近で非常に鋭い形状である時（つまり、<u>運動量の不確定性が十分に小さい時</u>）、量子力学で粒子の速度に相当する群速度$v_\text{group}$が同じ$k$とそれに伴うエネルギー値$E$に対して古典力学で求めた粒子の速度$v_\text{classical}$と等しくなるはずである。

先ほど求めた群速度（式[$\ref{eqn:group_velocity}$]）に式($\ref{eqn:t_independent_schrodinger_eqn}$)の $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$を代入すると

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

となり、古典力学で運動エネルギー$E$を持つ自由粒子の速度は同様に

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

である。したがって $v_\text{quantum}=v_\text{classical}$となるので、量子力学を適用して得た結果が物理的に妥当な解であることが確認できる。
