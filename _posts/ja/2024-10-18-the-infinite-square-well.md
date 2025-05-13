---
title: 1次元無限井戸(The 1D Infinite Square Well)
description: 量子力学の基本概念をよく示す簡単かつ重要な代表的問題、1次元無限井戸問題を考察する。この理想的な状況で粒子のn番目の定常状態ψ(x)とエネルギーEを求め、ψ(x)が持つ重要な4つの数学的性質を学ぶ。そしてこれらから一般解Ψ(x,t)を導出する。
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 1次元無限井戸問題: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{その他の場合}
>   \end{cases}$$
> - 境界条件: $ \psi(0) = \psi(a) = 0 $
> - $n$番目の定常状態のエネルギー準位: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - 井戸内での時間に依存しないシュレーディンガー方程式の解:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - 各定常状態$\psi_n$の物理的解釈: 
>   - 長さ$a$の弦に現れる定在波の形
>   - **基底状態(ground state)**: 最も低いエネルギーを持つ定常状態$\psi_1$
>   - **励起状態(exited states)**: $n^2$に比例してエネルギーが増加する残りの$n\geq 2$の状態
> - $\psi_n$の重要な4つの数学的性質:
>   1. ポテンシャル$V(x)$が対称性を持つ場合、井戸の中心に対して偶関数、奇関数が交互に現れる
>   2. エネルギーが大きくなるにつれ、各連続した状態は**節(node)**が1つずつ増加する
>   3. **直交正規性(orthonomality)**を持つ
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. **完全性(completeness)**を持つ
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - シュレーディンガー方程式の一般解(定常状態の線形結合):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{ここで係数 }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Prerequisites
- 連続確率分布と確率密度
- 直交性と正規化(線形代数学)
- フーリエ級数と完全性(線形代数学)
- [シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/)
- [エーレンフェストの定理](/posts/ehrenfest-theorem/)
- [時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/)

## 与えられたポテンシャル条件
ポテンシャルが

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{その他の場合}
\end{cases} \tag{1}$$

とすると、このポテンシャル内の粒子は範囲$0<x<a$内では自由粒子であり、両端($x=0$と$x=a$)では無限の力が作用して脱出できない。古典的なモデルでは、これを前後に完全弾性衝突を繰り返し、非保存力が作用しない無限往復運動として解釈する。このようなポテンシャルは極めて人為的で単純だが、むしろそれゆえに今後量子力学を学ぶ際に他の物理的状況を考察する際の有用な参考例となり得るため、注意深く確認する必要がある。

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *画像出典*
> - 作者: ウィキメディア・ユーザー [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - ライセンス: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## モデルおよび境界条件の設定
井戸の外側では粒子を見つける確率が$0$なので$\psi(x)=0$である。井戸内では$V(x)=0$なので[時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/)は

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

であり、つまり

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ ここで } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

の形で書くことができる。

> ここで$E\geq 0$と仮定する。
{: .prompt-info }

これは古典的な**単純調和振動子(simple harmonic oscillator)**を記述する式であり、一般解は

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

である。ここで$A$と$B$は任意の定数であり、問題状況に合った特殊解を求める際には典型的にこの定数は問題で与えられた**境界条件**によって決定される。<u>$\psi(x)$の場合、通常は$\psi$と$d\psi/dx$がともに連続であることが境界条件となるが、ポテンシャルが無限大になる場所では$\psi$のみが連続である。</u>

## 時間に依存しないシュレーディンガー方程式の解を求める

$\psi(x)$が連続なので

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

となり、井戸の外側の解と接続しなければならない。式($\ref{eqn:psi_general_solution}$)で$x=0$のとき

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

なので、($\ref{eqn:boundary_conditions}$)を代入すると$B=0$でなければならない。

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

すると$\psi(a)=A\sin{ka}$なので、式($\ref{eqn:boundary_conditions}$)の$\psi(a)=0$を満たすためには$A=0$(自明解)か$\sin{ka}=0$である。したがって

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

である。ここでも同様に$k=0$は自明解であり、$\psi(x)=0$となって規格化できないため、この問題で求めたい解ではない。また$\sin(-\theta)=-\sin(\theta)$なので負の符号は式($\ref{eqn:psi_without_B}$)の$A$に吸収させることができるため、$ka>0$の場合のみを考慮しても一般性を失わない。そのため$k$について可能な解は

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

である。

すると$\psi_n=A\sin{k_n x}$で$\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$なので、式($\ref{eqn:t_independent_schrodinger_eqn}$)に代入すると可能な$E$値は次のようになる。

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

古典的な場合とは非常に対照的に、無限井戸内の量子粒子は任意のエネルギーを持つことができず、許容された値のうちの1つを持たなければならない。

> 時間に依存しないシュレーディンガー方程式の解に適用される境界条件によってエネルギーが量子化される。
{: .prompt-info }

ここで$\psi$を規格化して$A$を求めることができる。

> 本来は$\Psi(x,t)$を規格化するものだが、[時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/#1-定常状態stationary-statesである)の式(11)によりこれは$\psi(x)$を規格化することに相当する。
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

これは厳密には$A$の大きさのみを決定するが、$A$の位相は何の物理的意味も持たないので、単に正の実数の平方根を$A$として使用しても構わない。したがって井戸内での解は

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

である。

## 各定常状態$\psi_n$の物理的解釈
式($\ref{eqn:psi_n}$)のように時間に依存しないシュレーディンガー方程式から各エネルギー準位$n$に対する無限個の解を求めた。これらのうち最初の数個を図で描くと以下の画像のようになる。

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *画像出典*
> - 作者: ウィキメディア・ユーザー [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - ライセンス: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

これらの状態は長さ$a$の弦に現れる定在波の形を示し、最も低いエネルギーを持つ$\psi_1$を**基底状態(ground state)**と呼び、$n^2$に比例してエネルギーが増加する残りの$n\geq 2$の状態を**励起状態(excited states)**と呼ぶ。

## $\psi_n$の重要な4つの数学的性質
すべての関数$\psi_n(x)$は以下の重要な4つの性質を持つ。これら4つの性質は非常に強力であり、無限井戸に限定されない。最初の性質はポテンシャル自体が対称性を持つ関数であれば常に成立し、2番目、3番目、4番目の性質はポテンシャルの形に関係なく現れる一般的な性質である。

### 1. 井戸の中心に対して偶関数、奇関数が交互に現れる。
正の整数$n$に対して$\psi_{2n-1}$は偶関数、$\psi_{2n}$は奇関数である。

### 2. エネルギーが大きくなるにつれ、各連続した状態は節が1つずつ増加する。
正の整数$n$に対して$\psi_n$は$(n-1)$個の**節(node)**を持つ。

### 3. この状態は直交性(orthogonality)を持つ。

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

という意味で互いに**直交(orthogonal)**する。

> 今考えている無限井戸の場合、$\psi$は実数なので$\psi_m$の複素共役($^*$)を取らなくても良いが、そうでない場合のために常に付ける習慣をつけるのが良い。
{: .prompt-tip }

#### 証明
$m\neq n$のとき、

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

$m=n$のときは規格化によりこの積分は$1$となり、**クロネッカーのデルタ(Kronecker delta)** $\delta_{mn}$を使うと直交性と規格化を

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

の1つの表現として一緒に表すこともできる。このとき$\psi$は**直交正規化(orthonormal)**されているという。

### 4. これらの関数は完全性(completeness)を持つ。
任意の他の関数$f(x)$を線形結合

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

で書くことができるという意味でこれらの関数は**完全(complete)**である。式($\ref{eqn:fourier_series}$)は$f(x)$の**フーリエ級数(Fourier series)**であり、任意の関数をこのように展開できることを**ディリクレの定理(Dirichlet's theorem)**と呼ぶ。

## フーリエの方法(Fourier's trick)を用いた係数$c_n$の導出
$f(x)$が与えられたとき、上記の完全性(completeness)と直交正規性(orthonormality)を利用すると**フーリエの方法(Fourier's trick)**と呼ばれる次の方法で係数$c_n$を求めることができる。式($\ref{eqn:fourier_series}$)の両辺に$\psi_m(x)^*$をかけて積分すると、式($\ref{eqn:orthonomality}$)と($\ref{eqn:kronecker_delta}$)により

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

を得る。

> クロネッカーのデルタにより和の中で$n=m$の項以外のすべての項が消えることに注目する。
{: .prompt-info }

したがって$f(x)$を展開する際の$n$次の係数は

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

である。

## 時間依存シュレーディンガー方程式の一般解$\Psi(x,t)$の導出
無限井戸の各定常状態は['時間に依存しないシュレーディンガー方程式'投稿の式(10)](/posts/time-independent-schrodinger-equation/#1-定常状態stationary-statesである)と先ほど求めた式($\ref{eqn:psi_n}$)により

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

である。また[時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/#3-時間依存シュレーディンガー方程式の一般解は変数分離解の線形結合である)でシュレーディンガー方程式の一般解を定常状態の線形結合として表現できることを先に見た。したがって

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

と書くことができる。ここで次の条件を満たす係数$c_n$を見つけ出せばよい。

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

先ほど見た$\psi$の完全性により上を満たす$c_n$が常に存在し、式($\ref{eqn:coefficients_n}$)の$f(x)$に$\Psi(x,0)$を代入して求めることができる。

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

初期条件として$\Psi(x,0)$が与えられれば式($\ref{eqn:calc_of_cn}$)を用いて展開係数$c_n$を求め、これを式($\ref{eqn:general_solution}$)に代入して$\Psi(x,t)$を求める。そしてその後は[エーレンフェストの定理](/posts/ehrenfest-theorem/)の過程に従って関心のある任意の物理量を計算することができる。この方法は無限井戸だけでなく任意のポテンシャルに適用でき、ただ$\psi$関数の形と許容されるエネルギー準位に関する式が変わるだけである。

## エネルギー保存($\langle H \rangle=\sum\|c_n\|^2E_n$)の導出
$\psi(x)$の直交正規性(式[$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$])を用いて先ほど[時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/#エネルギー保存)で簡単に見たエネルギー保存を導出しよう。$c_n$は時間に依存しないので$t=0$の場合について成り立つことを示せば十分である。

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

また

$$ \hat{H}\psi_n = E_n\psi_n $$

なので次を得る。

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
