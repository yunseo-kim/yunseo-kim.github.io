---
title: エーレンフェストの定理(Ehrenfest theorem)
description: 量子力学において波動関数から位置と運動量の期待値を求める方法を学び、 これを任意の力学的変数Q(x,p)に対する期待値の計算式に拡張する。
  そしてこれからエーレンフェストの定理(Ehrenfest theorem)を導出する。
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## 前提知識
- 連続確率分布と確率密度
- [シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/)

## 波動関数からの期待値計算
### 位置 $x$ の期待値
$\Psi$ 状態にある粒子に対する位置 $x$ の期待値(expectation value)は

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

である。同じ状態 $\Psi$ にある十分多数の粒子に対してそれぞれ位置を測定した後、測定結果の平均を取ると、上の式を通じて計算した $\langle x \rangle$ を得る。

> ここで言う期待値とは、1つの粒子を繰り返し測定して得た平均値ではなく、同じ状態を持つ系の**アンサンブル(ensemble)**に対する測定結果の平均であることに注意する。もし同じ粒子を短い時間間隔で何度も繰り返し測定すると、最初の測定で[波動関数が崩壊(collapse)](/posts/schrodinger-equation-and-the-wave-function/#測定と波動関数の崩壊)するため、その後の測定では常に同じ値のみを得ることになる。
{: .prompt-warning }

### 運動量 $p$ の期待値
$\Psi$ が時間に依存するため、時間が経つにつれて $\langle x \rangle$ は変化するだろう。このとき[シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/)の式(8)と上の式($\ref{eqn:x_exp}$)により、次が成り立つ。

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> 式($\ref{eqn:dx/dt_1}$)から($\ref{eqn:dx/dt_2}$)への過程と($\ref{eqn:dx/dt_2}$)から($\ref{eqn:dx/dt_3}$)への過程で2回部分積分を適用し、$\lim_{x\rightarrow\pm\infty}\Psi=0$であるため境界項(boundary term)を捨てた。
{: .prompt-tip }

したがって**運動量**の期待値を次のように得る。

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### 任意の物理量 $Q(x,p)$ に対する期待値
前で求めた $\langle x \rangle$ と $\langle p \rangle$ の表現式を次の形で書くことができる。

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

演算子 $\hat x \equiv x$ は位置を表し、演算子 $\hat p \equiv -i\hbar(\partial/\partial x)$ は運動量を表す。運動量演算子 $\hat p$ の場合、3次元空間に拡張すると $\hat p \equiv -i\hbar\nabla$ と定義できる。

すべての古典力学的変数は位置と運動量で表すことができるため、これを任意の物理量に対する期待値に拡張できる。任意の量 $Q(x,p)$ に対する期待値を計算するには、すべての $p$ を $-i\hbar\nabla$ に置き換え、このようにして得られた演算子を $\Psi^*$ と $\Psi$ の間に入れて積分すればよい。

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

例えば、運動エネルギー $T=\cfrac{p^2}{2m}$ であるため

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

である。

式($\ref{eqn:Q_exp}$)を通じて状態 $\Psi$ にある粒子に対する任意の物理量の期待値を計算することができる。

## エーレンフェストの定理 (Ehrenfest theorem)
### $d\langle p \rangle/dt$ の計算
式($\ref{eqn:p_op}$)の両辺を時間 $t$ に対して微分して運動量の期待値の時間微分 $\cfrac{d\langle p \rangle}{dt}$ を求めよう。

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> 式($\ref{eqn:dp/dt_1}$)に[シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/)の式(6)と(7)を代入して式($\ref{eqn:dp/dt_2}$)を得ることができる。式($\ref{eqn:dp/dt_3}$)から($\ref{eqn:dp/dt_4}$)への過程では部分積分を適用し、前と同様に $\lim_{x\rightarrow\pm\infty}\Psi=0$ であるため境界項(boundary term)を捨てた。
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### エーレンフェストの定理とニュートンの運動第2法則との関係
先ほど得た次の2つの式をエーレンフェストの定理(Ehrenfest theorem)という。

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

エーレンフェストの定理は古典力学におけるポテンシャルエネルギーと保存力の間の関係式 $F=\cfrac{dp}{dt}=-\nabla V$ とかなり類似した形を持つ。
2つの式を並べて比較してみると以下のようになる。

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newton's Second Law of Motion]}$$

エーレンフェストの定理の2番目の式 $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$(式[$\ref{eqn:ehrenfest_theorem_2nd}$])の右辺を $\langle x \rangle$ 付近で $x$ についてテイラー展開すると

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

である。ここでもし $x-\langle x \rangle$ が十分に小さければ、最初の項以外のすべての高次項を無視して

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

と近似できる。

つまり、**ある粒子の波動関数が空間的にある一点に非常に近く分布する鋭い形状を持つ場合($\|\Psi\|^2$ の $x$ に対する散布度が非常に小さい場合)、エーレンフェストの定理を古典力学のニュートンの運動第2法則で近似できる。** 巨視的なスケールでは波動関数が空間的に広がった程度を無視し、粒子の位置を事実上1点とみなすことができるためニュートンの運動第2法則が成り立つが、微視的なスケールでは量子力学的効果を無視できないためニュートンの運動第2法則はもはや成り立たず、エーレンフェストの定理を活用しなければならない。
