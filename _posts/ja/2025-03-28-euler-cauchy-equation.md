---
title: オイラー・コーシー方程式
description: 補助方程式の判別式の符号に応じて、オイラー・コーシー方程式の一般解がどのような形になるかを考察する。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - オイラー・コーシー方程式: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **補助方程式(auxiliary equation)**: $m^2 + (a-1)m + b = 0$
> - 補助方程式の判別式 $(1-a)^2 - 4b$の符号によって一般解の形を表のように三つの場合に分けることができる
>
> | 場合 | 補助方程式の解 | オイラー・コーシー方程式の解の基底 | オイラー・コーシー方程式の一般解 |
> | :---: | :---: | :---: | :---: |
> | I | 異なる実根<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | 実重根<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | 共役複素根<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerequisites
- [2階同次線形常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [定数係数を持つ2階同次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- オイラーの公式

## 補助方程式 (auxiliary equation)
**オイラー・コーシー方程式(Euler-Cauchy equation)**は、与えられた定数 $a$と $b$、そして未知関数 $y(x)$を持つ

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

形式の常微分方程式である。式 ($\ref{eqn:euler_cauchy_eqn}$)に

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

を代入すると

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

つまり

$$ [m(m-1) + am + b]x^m = 0 $$

を得る。これから補助方程式

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

を得る。$y=x^m$がオイラー・コーシー方程式 ($\ref{eqn:euler_cauchy_eqn}$)の解となるための必要十分条件は、$m$が補助方程式 ($\ref{eqn:auxiliary_eqn}$)の解となることである。

二次方程式 ($\ref{eqn:auxiliary_eqn}$)の解を求めると

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

となり、これから二つの関数

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

が方程式 ($\ref{eqn:euler_cauchy_eqn}$)の解となる。

[定数係数を持つ2階同次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)と同様に、補助方程式 ($\ref{eqn:auxiliary_eqn}$)の判別式 $(1-a)^2 - 4b$の符号によって場合を三つに分けることができる。
- $(1-a)^2 - 4b > 0$: 異なる二つの実根
- $(1-a)^2 - 4b = 0$: 実重根
- $(1-a)^2 - 4b < 0$: 共役複素根

## 補助方程式の判別式の符号による一般解の形
### I. 異なる二つの実根 $m_1$と $m_2$
この場合、任意の区間で方程式 ($\ref{eqn:euler_cauchy_eqn}$)の解の基底は

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

であり、これに対応する一般解は

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

である。

### II. 実重根 $m = \cfrac{1-a}{2}$
$(1-a)^2 - 4b = 0$、つまり $b=\cfrac{(1-a)^2}{4}$の場合、二次方程式 ($\ref{eqn:auxiliary_eqn}$)は一つの解 $m = m_1 = m_2 = \cfrac{1-a}{2}$のみを持ち、したがってこれから得られる $y = x^m$ 形式の一つの解は

$$ y_1 = x^{(1-a)/2} $$

であり、オイラー・コーシー方程式 ($\ref{eqn:euler_cauchy_eqn}$)は

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

の形になる。ここで線形独立なもう一つの解 $y_2$を[階数低下法](/posts/homogeneous-linear-odes-of-second-order/#次数低下法-reduction-of-order)を用いて求めよう。

求めたい二番目の解を $y_2=uy_1$とすると

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

を得る。

$\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$なので、

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

となり、積分すると $u = \ln x$を得る。

したがって $y_2 = uy_1 = y_1 \ln x$であり、$y_1$と $y_2$はその商が定数でないため線形独立である。基底 $y_1$と $y_2$に対応する一般解は

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

である。

### III. 共役複素根
この場合、補助方程式 ($\ref{eqn:auxiliary_eqn}$)の解は $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$となり、これに対応する方程式 ($\ref{eqn:euler_cauchy_eqn}$)の二つの複素解は $x=e^{\ln x}$を利用して次のように書くことができる。

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

$t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$とおき、オイラーの公式 $e^{it} = \cos{t} + i\sin{t}$を用いると

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

であることがわかり、これから次の二つの実数解

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

を得る。

これらの商 $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$が定数でないため、上記の二つの解は線形独立であり、したがって[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)によりオイラー・コーシー方程式 ($\ref{eqn:euler_cauchy_eqn}$)の基底を形成する。これから次の実数一般解を得る。

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

ただし、オイラー・コーシー方程式において補助方程式が共役複素根を持つ場合は、実質的な重要性はそれほど大きくない。
