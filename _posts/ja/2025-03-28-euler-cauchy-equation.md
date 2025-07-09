---
title: "オイラー・コーシー方程式"
description: "補助方程式の判別式の符号によって、オイラー・コーシー方程式の一般解がどのような形をとるか、各場合について考察します。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - オイラー・コーシー方程式: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **補助方程式（auxiliary equation）**: $m^2 + (a-1)m + b = 0$
> - 補助方程式の判別式 $(1-a)^2 - 4b$の符号によって、一般解の形を下の表のように3つの場合に分けることができます。
>
> | 場合 | 補助方程式の解 | オイラー・コーシー方程式の解の基底 | オイラー・コーシー方程式の一般解 |
> | :---: | :---: | :---: | :---: |
> | I | 異なる実数解<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | 実数の重解<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | 共役複素数解<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## 前提知識
- [2階斉次線形常微分方程式（Homogeneous Linear ODEs of Second Order）](/posts/homogeneous-linear-odes-of-second-order/)
- [定数係数を持つ2階斉次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- オイラーの公式

## 補助方程式（auxiliary equation）
**オイラー・コーシー方程式（Euler-Cauchy equation）**は、与えられた定数$a$と$b$、そして未知の関数$y(x)$を持つ

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

形の常微分方程式です。式($\ref{eqn:euler_cauchy_eqn}$)に

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

を代入すると

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

すなわち

$$ [m(m-1) + am + b]x^m = 0 $$

を得ます。これから補助方程式

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

を得て、$y=x^m$がオイラー・コーシー方程式($\ref{eqn:euler_cauchy_eqn}$)の解となるための必要十分条件は、$m$が補助方程式($\ref{eqn:auxiliary_eqn}$)の解となることです。

二次方程式($\ref{eqn:auxiliary_eqn}$)の解を求めると

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

であり、これから2つの関数

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

が方程式($\ref{eqn:euler_cauchy_eqn}$)の解となります。

[定数係数を持つ2階斉次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)と同様に、補助方程式($\ref{eqn:auxiliary_eqn}$)の判別式$(1-a)^2 - 4b$の符号によって、場合を3つに分けることができます。
- $(1-a)^2 - 4b > 0$: 異なる2つの実数解
- $(1-a)^2 - 4b = 0$: 実数の重解
- $(1-a)^2 - 4b < 0$: 共役複素数解

## 補助方程式の判別式の符号による一般解の形
### I. 異なる2つの実数解 $m_1$と$m_2$
この場合、任意の区間で方程式($\ref{eqn:euler_cauchy_eqn}$)の解の基底は

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

であり、これによる一般解は

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

です。

### II. 実数の重解 $m = \cfrac{1-a}{2}$
$(1-a)^2 - 4b = 0$、すなわち$b=\cfrac{(1-a)^2}{4}$の場合、二次方程式($\ref{eqn:auxiliary_eqn}$)は一つの解$m = m_1 = m_2 = \cfrac{1-a}{2}$のみを得ることになり、したがってこれから得られる$y = x^m$形の解の一つは

$$ y_1 = x^{(1-a)/2} $$

であり、オイラー・コーシー方程式($\ref{eqn:euler_cauchy_eqn}$)は

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

の形になります。ここで、線形独立なもう一つの解$y_2$を[階数低下](/posts/homogeneous-linear-odes-of-second-order/#階数低下-reduction-of-order)を用いて求めましょう。

求めたい第二の解を$y_2=uy_1$と置くと

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

を得ます。

$\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$なので、

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

であり、積分すると$u = \ln x$を得ます。

したがって、$y_2 = uy_1 = y_1 \ln x$であり、$y_1$と$y_2$はその商が定数ではないため線形独立です。基底$y_1$と$y_2$に対応する一般解は

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

です。

### III. 共役複素数解
この場合、補助方程式($\ref{eqn:auxiliary_eqn}$)の解は$m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$となり、これに対応する方程式($\ref{eqn:euler_cauchy_eqn}$)の2つの複素解は、$x=e^{\ln x}$であることを利用して次のように書くことができます。

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

$t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$と置き、オイラーの公式$e^{it} = \cos{t} + i\sin{t}$を利用すると

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

であることがわかり、これから次の2つの実数解

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

を得ます。

これらの商 $\tan\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$が定数ではないため、上記の2つの解は線形独立であり、したがって[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)によりオイラー・コーシー方程式($\ref{eqn:euler_cauchy_eqn}$)の基底を形成します。これから次の実数一般解を得ます。

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

ただし、オイラー・コーシー方程式で補助方程式が共役複素数解を持つ場合は、実質的な重要性はそれほど高くありません。

## 定数係数を持つ2階斉次線形常微分方程式への変換
オイラー・コーシー方程式は、変数置換を通じて[定数係数を持つ2階斉次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)に変換することができます。

$x = e^t$と置換すると

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

となり、オイラー・コーシー方程式($\ref{eqn:euler_cauchy_eqn}$)は次のように$t$に関する定数係数斉次線形常微分方程式に変わります。

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

方程式($\ref{eqn:substituted}$)を[定数係数を持つ2階斉次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)の解法を適用して$t$について解き、そうして得られた解を$t = \ln{x}$であることを利用して再び$x$に関する解に変換すると、[先ほど見たものと同じ結果](#補助方程式の判別式の符号による一般解の形)を得ます。
