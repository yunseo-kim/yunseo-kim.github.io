---
title: "調和振動子（The Harmonic Oscillator）の代数的解法"
description: >-
  量子力学における調和振動子のシュレーディンガー方程式を立て、その方程式の代数的な解法を学ぶ。
  交換子と正準交換関係および梯子演算子から任意の定常状態の波動関数とエネルギー準位を求める。
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder Operators]
math: true
---

## TL;DR
> - 振幅が十分に小さければ、どのような振動も単純調和振動（simple harmonic oscillation）で近似できるため、単純調和振動は物理学で重要な意味を持つ
> - 調和振動子: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **交換子（commutator）**:
>   - 二つの演算子がどれだけ交換（commute）されないかを表す二項演算
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **正準交換関係（canonical commutation relation）**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **梯子演算子（ladder operators）**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$を**昇降演算子（raising operator）**、$\hat{a}\_-$を**降下演算子（lowering operator）**と呼ぶ
>   - 任意の定常状態に対してエネルギー準位を上げたり下げたりできるため、時間に依存しないシュレーディンガー方程式の一つの解を見つければ他の解もすべて見つけることができる
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - $n$番目の定常状態の波動関数とエネルギー準位:
>   - 基底状態（$0$番目の定常状態）:
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$番目の定常状態:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$は$\hat{a}\_\pm$の**エルミート共役（hermitian conjugate）**であり**随伴演算子（adjoint operator）**である
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - これから以下の性質を導くことができる:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - $\hat{x}$と$\hat{p}$の累乗を含む物理量の期待値計算方法:
>   1. 梯子演算子の定義を用いて$\hat{x}$と$\hat{p}$を昇降演算子と降下演算子で表現
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. 期待値を求めたい物理量を上の$\hat{x}$と$\hat{p}$の式を用いて表現
>   3. $\left(\hat{a}\_\pm \right)^m$は$\psi\_{n\pm m}$に比例するので$\psi_n$とは直交して$0$になることを利用
>   4. 梯子演算子の性質を用いて積分計算
{: .prompt-info }

## Prerequisites
- [変数分離法](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/)
- [エーレンフェストの定理](/posts/ehrenfest-theorem/)
- [時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/)
- [1次元無限井戸型ポテンシャル](/posts/the-infinite-square-well/)
- エルミート共役（hermitian conjugate）、随伴演算子（adjoint operator）

## モデル設定
### 古典力学における調和振動子
古典的な調和振動子の代表的な例は、質量$m$がばね定数$k$のばねに吊るされている場合の運動（摩擦は無視する）である。
この運動は**フックの法則（Hooke's law）**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

に従う。この式の解は

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

であり、ここで

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

は振動の角振動数である。位置$x$に対するポテンシャルエネルギーは

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

の放物線の形である。

現実には完全な調和振動子は存在しない。今例として挙げたばねの場合でも、ばねを過度に引っ張ると弾性限界を超えて切れたり永久変形が発生し、実際にその点に達する前にすでにフックの法則を正確には従わなくなる。それにもかかわらず物理学で調和振動子が重要な理由は、任意のポテンシャルも極小値（local minimum）付近では放物線の形で近似できるからである。任意のポテンシャル$V(x)$を極小点付近でテイラー展開すると

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

を得る。ここで$V(x)$に任意の定数を加えても力には全く影響を与えないので、ここから$V(x_0)$を引き、$x_0$が極小点なので$V^\prime(x_0)=0$であることを利用し、$(x-x_0)$が十分に小さいという仮定の下で高次項を無視すると

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

を得る\*。これは点$x_0$付近で有効ばね定数$k=V^{\prime\prime}(x_0)$の調和振動子の運動と一致する。つまり、振幅が十分に小さければ、どのような振動も単純調和振動（simple harmonic oscillation）で近似できる。

> \* $V(x)$が$x_0$で極小値を持つと仮定したので、ここで$V^{\prime\prime}(x_0) \geq 0$である。非常にまれに$V^{\prime\prime}(x_0)=0$の場合があり、このような運動は単純調和振動で近似できない。
{: .prompt-info }

### 量子力学における調和振動子
量子力学的調和振動子問題はポテンシャル

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

に対するシュレーディンガー方程式を解くことである。調和振動子に対する[時間に依存しないシュレーディンガー方程式](/posts/time-independent-schrodinger-equation/)は

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

である。

この問題を解くには全く異なる二つのアプローチがある。一つは**べき級数（power series method）**を用いた解析的な方法（analytic method）であり、もう一つは**梯子演算子（ladder operators）**を用いた代数的な方法（algebraic method）である。代数的な方法がより速く簡単だが、べき級数を用いた解析的な解法も学ぶ必要がある。ここでは代数的な解法を扱い、解析的な解法は[この記事](/posts/analytic-solution-of-the-harmonic-oscillator/)を参照してほしい。

## 交換子と正準交換関係
式（$\ref{eqn:t_independent_schrodinger_eqn}$）を運動量演算子$\hat{p}\equiv -i\hbar \cfrac{d}{dx}$を活用して次のように書くことができる。

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

ここでハミルトニアン（Hamiltonian）

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

を因数分解しよう。

もし$p$と$x$が数（numbers）であれば

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

のように簡単に因数分解できるが、ここで$\hat{p}$と$\hat{x}$は演算子であり、演算子に対しては一般的に**交換法則（commutative property）**が成り立たないため（$\hat{p}\hat{x}\neq \hat{x}\hat{p}$）、そう簡単ではない。しかし、とにかく基準点にはなるので、まずは次の量を見てみることから始めよう。

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

上で定義した演算子$\hat{a_\pm}$に対して、$\hat{a}\_-\hat{a}\_+$は

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

である。ここで$(\hat{x}\hat{p}-\hat{p}\hat{x})$項を$\hat{x}$と$\hat{p}$の**交換子（commutator）**と呼び、二つの演算子がどれだけ交換（commute）されないかを表す。一般的に演算子$\hat{A}$と$\hat{B}$の交換子を角括弧を使って次のように表す。

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

この表記法を用いると式（$\ref{eqn:a_m_times_a_p_without_commutator}$）を次のように書き直すことができる。

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

ここで$\hat{x}$と$\hat{p}$の交換子を求める必要がある。

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

であり、試験関数$f(x)$を取り除くと次を得る。

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

これを**正準交換関係（canonical commutation relation）**と呼ぶ。

## 梯子演算子（ladder operators）
正準交換関係により式（$\ref{eqn:a_m_times_a_p}$）は

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

つまり

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

である。ここで$\hat{a_-}$と$\hat{a_+}$の順序が重要で、$\hat{a_+}$を左に置くと

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

となり

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

を満たす。この場合ハミルトニアンは

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

とも書ける。したがって時間に依存しないシュレーディンガー方程式（$\hat{H}\psi=E\psi$）を$\hat{a}_\pm$で表現すると

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

である（複号同順）。

ここで次の重要な性質を見出すことができる。

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> 証明:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> 同様に、
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

したがって、時間に依存しないシュレーディンガー方程式の一つの解を見つけることができれば、他の解をすべて見つけることができる。任意の定常状態に対してエネルギー準位を上げたり下げたりできるため、$\hat{a}\_\pm$を**梯子演算子（ladder operators）**と呼び、$\hat{a}\_+$は**昇降演算子（raising operator）**であり、$\hat{a}\_-$は**降下演算子（lowering operator）**である。

## 調和振動子の定常状態
### 定常状態$\psi_n$とエネルギー準位$E_n$
降下演算子を続けて適用すると、いつかは$0$より小さいエネルギー状態を得ることになり、このような状態は物理的に存在し得ない。数学的には$\psi$がシュレーディンガー方程式の解であれば$\hat{a}_-\psi$もシュレーディンガー方程式の解であるが、この新しい解が常に規格化される（つまり物理的に可能な状態である）という保証はない。降下演算子を続けて適用していくと、最終的には自明解$\psi=0$を得る。

したがって調和振動子の定常状態$\psi$に対して、

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

を満たす（より低いエネルギー準位が存在しない）「最も低い段階」$\psi_0$が存在する。この$\psi_0$は

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

を満たすので、

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

である。これは[分離可能な常微分方程式](/posts/Separation-of-Variables/)なので、次のように簡単に解くことができる。

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

またこの関数は次のように規格化できる。

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

ここで$A^2 = \sqrt{m\omega / \pi\hbar}$なので

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

である。ここでこの解を先ほど求めたシュレーディンガー方程式（$\ref{eqn:schrodinger_eqn_with_ladder}$）に代入し、$\hat{a}_-\psi_0$であることを利用すると次を得る。

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

この**基底状態（ground state）**から始めて昇降演算子を続けて適用すると、昇降演算子が一回作用するごとにエネルギーが$\hbar\omega$ずつ増加する励起状態（excited states）を得ることができる。

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

ここで$A_n$は規格化定数である。このように基底状態を見出した後に昇降演算子を適用して調和振動子のすべての定常状態と許容されるエネルギー準位を決定することができる。

### 規格化
規格化定数も代数的に求めることができる。我々は$\hat{a}\_{\pm}\psi_n$が$\psi\_{n\pm 1}$に比例することを知っているので、

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

と書くことができる。

ここで任意の定積分可能な関数$f(x)$と$g(x)$に対して次が成り立つことに注目しよう。

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$は$\hat{a}\_\pm$の**エルミート共役（hermitian conjugate）**であり**随伴演算子（adjoint operator）**である。

> **証明:**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

したがって、$f=\hat{a}_\pm \psi_n$、$g=\psi_n$とおくと

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

が成り立つ。そうすると式（$\ref{eqn:schrodinger_eqn_with_ladder}$）と（$\ref{eqn:psi_n_and_E_n}$）から

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

となるので、式（$\ref{eqn:norm_const}$）と（$\ref{eqn:norm_const_2}$）から次を得る。

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

そしてここで$\psi_n$と$\psi_{n\pm1}$はすべて規格化されているので$\|c_n\|^2=n+1,\ \|d_n\|^2=n$となり、したがって

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

となる。これから規格化された任意の定常状態$\psi_n$を次のように求めることができる。

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

つまり、式（$\ref{eqn:psi_n_and_E_n}$）において規格化定数$A_n=\cfrac{1}{\sqrt{n!}}$である。

### 定常状態の直交性
[1次元無限井戸型ポテンシャル](/posts/the-infinite-square-well/#3-%E3%81%93%E3%81%AE%E7%8A%B6%E6%85%8B%E3%81%AF%E7%9B%B4%E4%BA%A4%E6%80%A7orthogonality%E3%82%92%E6%8C%81%E3%81%A4)の場合と同様に、調和振動子の定常状態は直交する。

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### 証明
先ほど示した式（$\ref{eqn:hermitian_conjugate}$）と（$\ref{eqn:norm_const_2}$）、（$\ref{eqn:norm_const_3}$）を使用して証明できる。式（$\ref{eqn:hermitian_conjugate}$）で$f=\hat{a}_-\psi_m,\ g=\psi_n$とおくと

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

となることを利用する。

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

直交性を利用すると、[1次元無限井戸型ポテンシャルの式（19）で行ったように](/posts/the-infinite-square-well/#%E6%99%82%E9%96%93%E4%BE%9D%E5%AD%98%E3%82%B7%E3%83%A5%E3%83%AC%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%AC%E3%83%BC%E6%96%B9%E7%A8%8B%E5%BC%8F%E3%81%AE%E4%B8%80%E8%88%AC%E8%A7%A3psixt%E3%81%AE%E5%B0%8E%E5%87%BA)$\Psi(x,0)$を定常状態の線形結合$\sum c_n\psi_n(x)$として展開するとき、その係数$c_n$を[フーリエ法](/posts/the-infinite-square-well/#%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E3%81%AE%E6%96%B9%E6%B3%95fouriers-trick%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E4%BF%82%E6%95%B0c_n%E3%81%AE%E5%B0%8E%E5%87%BA)で求めることができる。

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

ここでも同様に$\|c_n\|^2$はエネルギーを測定して$E_n$値を得る確率である。

## 任意の定常状態$\psi_n$におけるポテンシャルエネルギーの期待値$\langle V \rangle$
$\langle V \rangle$を求めるためには、次の積分を計算する必要がある。

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

$\hat{x}$と$\hat{p}$の累乗を含むこのような形の積分を計算する際には、以下の方法が有用である。

まず式（$\ref{eqn:ladder_operators}$）のラダー演算子の定義を用いて$\hat{x}$と$\hat{p}$を生成演算子と消滅演算子で表す。

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

次に期待値を求めたい物理量を上の$\hat{x}$と$\hat{p}$の式を用いて表す。ここでは$x^2$に関心があるので、

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

のように表すことができる。これから次を得る。

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

そしてここで$\left(\hat{a}\_\pm \right)^2$は$\psi\_{n\pm2}$に比例するので$\psi\_n$とは直交し、したがって$\left(\hat{a}\_+ \right)^2$と$\left(\hat{a}\_- \right)^2$のこの二つの項は$0$になる。最後に式（$\ref{eqn:norm_const_2}$）を用いて残りの二つの項を計算すると

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

を得る。式（$\ref{eqn:psi_n_and_E_n}$）を参照すると、ポテンシャルエネルギーの期待値は全エネルギーのちょうど半分であることがわかり、残りの半分は当然運動エネルギー$T$である。これは調和振動子の固有の特性である。
