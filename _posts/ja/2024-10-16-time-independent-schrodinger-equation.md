---
title: "時間に依存しないシュレーディンガー方程式(Time-independent Schrödinger Equation)"
description: >-
  シュレーディンガー方程式の元の形（時間依存シュレーディンガー方程式）Ψ(x,t)に変数分離法を適用して
  時間に依存しないシュレーディンガー方程式ψ(x)を導出し、
  このように得られた変数分離解が数学的、物理的に持つ意味と重要性を理解する。
  そして変数分離解の線形結合によってシュレーディンガー方程式の一般解を求める方法を検討する。
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
---

## TL;DR
> - 変数分離解: $ \Psi(x,t) = \psi(x)\phi(t)$
> - 時間依存性("wiggle factor"): $ \phi(t) = e^{-iEt/\hbar} $
> - ハミルトニアン(Hamiltonian)演算子: $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - 時間に依存しないシュレーディンガー方程式: $ \hat H\psi = E\psi $
> - 変数分離解が持つ物理的、数学的意味と重要性:
>   1. 定常状態(stationary states)
>   2. 明確な全エネルギー値$E$を持つ
>   3. シュレーディンガー方程式の一般解は変数分離解の線形結合
> - 時間依存シュレーディンガー方程式の一般解: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Prerequisites
- 連続確率分布と確率密度
- [シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/)
- [エーレンフェストの定理](/posts/ehrenfest-theorem/)
- [変数分離法](/posts/Separation-of-Variables/)

## 変数分離法を用いた導出
[エーレンフェストの定理に関する投稿](/posts/ehrenfest-theorem/)で波動関数$\Psi$を用いて知りたい様々な物理量をどのように計算するかを見てきました。そうすると重要なのはその波動関数$\Psi(x,t)$をどのように得るかということですが、通常は与えられたポテンシャル$V(x,t)$に対して位置$x$と時間$t$に関する偏微分方程式である[シュレーディンガー方程式](/posts/schrodinger-equation-and-the-wave-function/)を解く必要があります。

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

もしポテンシャル$V$が時間$t$に依存しない場合、上記のシュレーディンガー方程式を[変数分離法](/posts/Separation-of-Variables/)を用いて解くことができます。次のように$x$のみの関数$\psi$と$t$のみの関数$\phi$の積の形で表される解を考えてみましょう。

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

一見するとこれは非常に限定的な表現で、全体の解の小さな部分集合しか求められないように見えますが、実際にはこのように得られた解が重要な意味を持つだけでなく、これらの分離可能な解を特定の方法で足し合わせることで一般解を求めることができます。

分離可能な解に対して

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

が成り立つので、これを式($\ref{eqn:schrodinger_eqn}$)に代入するとシュレーディンガー方程式を次のように書くことができます。

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

両辺を$\psi\phi$で割ると、左辺は$t$のみの関数で右辺は$x$のみの関数である

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

を得ます。この式が解を持つためには両辺が定数でなければなりません。もしそうでなければ、変数$t$と$x$のうち一方を一定に保ちながら他方のみを変化させたとき、上式の片側だけが変わってしまい、等式がもはや成り立たなくなるからです。したがって、左辺を分離定数$E$とおくことができます。

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

すると次の2つの常微分方程式を得ますが、一つは

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

で時間$t$に関する部分であり、もう一つは

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

で空間$x$に関する部分です。

$t$に関する常微分方程式($\ref{eqn:ode_t}$)は簡単に解くことができます。本来この方程式の一般解は$ce^{-iEt/\hbar}$ですが、どうせ関心があるのは$\phi$自体よりも積$\psi\phi$なので、定数$c$は$\psi$に含めることができます。すると

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

を得ます。

$x$に関する常微分方程式($\ref{eqn:t_independent_schrodinger_eqn}$)を**時間に依存しないシュレーディンガー方程式(time-independent Schrödinger equation)**と呼びます。ポテンシャル$V(x)$を知っていなければこの式を解くことはできません。

## 物理的、数学的意味
先ほど変数分離法を用いて時間$t$のみの関数$\phi(t)$と時間に依存しないシュレーディンガー方程式($\ref{eqn:t_independent_schrodinger_eqn}$)を得ました。元の**時間依存シュレーディンガー方程式(time-dependant Schrödinger equation)**($\ref{eqn:schrodinger_eqn}$)のほとんどの解は$\psi(x)\phi(t)$の形で表すことはできませんが、それにもかかわらず時間に依存しないシュレーディンガー方程式の形が重要である理由は、その解が持つ次の3つの性質によるものです。

### 1. 定常状態(stationary states)である。
波動関数

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

自体は$t$に依存しますが、確率密度

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

は時間依存性が相殺されて時間に依存せず一定です。

> 規格化可能な解に対しては、分離定数$E$は実数でなければなりません。
>
> 式($\ref{eqn:separation_of_variables}$)の$E$を複素数$E_0+i\Gamma$($E_0$、$\Gamma$は実数)とすると
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> となりますが、先ほど[シュレーディンガー方程式と波動関数](/posts/schrodinger-equation-and-the-wave-function/#波動関数の規格化normalization)で見たように$\int_{-\infty}^{\infty}\|\Psi\|^2dx$は時間に依存しない定数でなければならないので$\Gamma=0$です。$\blacksquare$
{: .prompt-info }

任意の物理量の期待値を計算する際にも同じことが起こり、[エーレンフェストの定理](/posts/ehrenfest-theorem/)の式(8)は

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

となるので、すべての期待値は時間に対して定数です。特に$\langle x \rangle$が定数なので、$\langle p \rangle=0$です。

### 2. ある範囲を持つ確率分布ではなく、一つの明確な全エネルギー値$E$を持つ状態である。
古典力学では全エネルギー（運動エネルギーとポテンシャルエネルギー）を**ハミルトニアン(Hamiltonian)**と呼び、

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

と定義しますが、したがって$p$を$-i\hbar(\partial/\partial x)$に置き換えると、量子力学におけるハミルトニアン(Hamiltonian)演算子には

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

が対応します。したがって、時間に依存しないシュレーディンガー方程式($\ref{eqn:t_independent_schrodinger_eqn}$)は

$$ \hat H \psi = E\psi \tag{15}$$

と書くことができ、ハミルトニアンの期待値は次のようになります。

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

また、

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

が成り立つので

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

であり、したがってハミルトニアン$H$の分散は

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

です。つまり、変数分離解は全エネルギーを測定したとき、常に一定の値$E$として測定されます。

### 3. 時間依存シュレーディンガー方程式の一般解は変数分離解の線形結合である。

時間に依存しないシュレーディンガー方程式($\ref{eqn:t_independent_schrodinger_eqn}$)は無限に多くの解$[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$を持ちます。これを\{$\psi_n(x)$\}とします。これらそれぞれに対して分離定数$E_1,E_2,E_3,\dots=$\{$E_n$\}が存在するので、それぞれの**可能なエネルギー準位**に対応する波動関数があります。

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

時間依存シュレーディンガー方程式($\ref{eqn:schrodinger_eqn}$)は任意の二つの解を線形結合しても解になるという性質があるので、一旦変数分離解を見つければすぐにより一般的な形の解である

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

を得ることができます。すべての時間依存シュレーディンガー方程式の解を上の形で書くことができ、あとは問題で与えられた初期条件を満たすように適切な定数$c_1, c_2, \dots$を求めて知りたい特殊解を見つけるだけです。つまり、一旦時間に依存しないシュレーディンガー方程式を解くことができれば、その後時間依存シュレーディンガー方程式の一般解を求めることは簡単にできます。

> 変数分離された解
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> はすべての確率と期待値が時間に依存しない定常状態ですが、式($\ref{eqn:general_solution}$)の一般解はこのような性質を持たないことに注意してください。
{: .prompt-warning }

## エネルギー保存
一般解($\ref{eqn:general_solution}$)において係数\{$c_n$\}の絶対値の二乗$\|c_n\|^2$は物理的にその状態($\Psi$)を持つ粒子のエネルギーを測定したとき$E_n$値が出る確率を意味します。したがって、この確率の和は

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

で1になるはずであり、ハミルトニアンの期待値は

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

です。ここで各定常状態のエネルギー準位$E_n$と係数\{$c_n$\}が時間に依存しないので、特定のエネルギー$E_n$が測定される確率やハミルトニアン$H$の期待値も時間に依存せず一定の値を持ちます。
