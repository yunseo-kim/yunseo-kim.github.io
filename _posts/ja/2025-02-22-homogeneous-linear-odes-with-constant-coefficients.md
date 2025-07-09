---
title: "定数係数を持つ2階斉次線形常微分方程式"
description: "特性方程式の判別式の符号に応じて、定数係数を持つ斉次線形常微分方程式の一般解がどのような形をとるかを各ケースごとに考察します。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 定数係数を持つ2階斉次線形常微分方程式: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **特性方程式（characteristic equation）**: $\lambda^2 + a\lambda + b = 0$
> - 特性方程式の判別式 $a^2 - 4b$の符号によって、一般解の形を次表のように3つの場合に分けることができます。
>
> | 場合 | 特性方程式の解 | 常微分方程式の解の基底 | 常微分方程式の一般解 |
> | :---: | :---: | :---: | :---: |
> | I | 互いに異なる実数解<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | 実数の重根<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | 共役複素数解<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## 前提知識
- [ベルヌーイ方程式（Bernoulli Equation）](/posts/Bernoulli-Equation/)
- [2階斉次線形常微分方程式（Homogeneous Linear ODEs of Second Order）](/posts/homogeneous-linear-odes-of-second-order/)
- オイラーの公式

## 特性方程式（characteristic equation）
係数$a$と$b$が定数である2階斉次線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

を考えてみましょう。このような形の式は、機械的、電気的振動において重要に応用されます。

以前、[ベルヌーイ方程式（Bernoulli Equation）](/posts/Bernoulli-Equation/)でロジスティック方程式の一般解を求めたことがありますが、それによると定数係数$k$を持つ1階線形常微分方程式

$$ y^\prime + ky = 0 $$

の解は指数関数$y = ce^{-kx}$です。（該当記事の式(4)で$A=-k$、$B=0$の場合）

したがって、似た形の式である($\ref{eqn:ode_with_constant_coefficients}$)に対しても

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

形の解をまず試みることができます。

> もちろん、これはあくまで推測に過ぎず、本当に一般解がこのような形であるという保証は全くありません。しかし、何であれ線形独立な2つの解を求めさえすれば、[2階斉次線形常微分方程式](/posts/homogeneous-linear-odes-of-second-order/#基底と一般解)で見たように、[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)によって一般解を求めることができます。  
> 後ほど見ますが、[異なる形の解を求める必要がある場合](#ii-実数の重根-lambda---cfraca2)もあります。
{: .prompt-info }

式($\ref{eqn:general_sol}$)とその導関数

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

を式($\ref{eqn:ode_with_constant_coefficients}$)に代入すると

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

を得ます。したがって、もし$\lambda$が**特性方程式（characteristic equation）**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

の解であれば、指数関数($\ref{eqn:general_sol}$)は常微分方程式($\ref{eqn:ode_with_constant_coefficients}$)の解です。二次方程式($\ref{eqn:characteristic_eqn}$)の解を求めると

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

であり、これから2つの関数

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

が方程式($\ref{eqn:ode_with_constant_coefficients}$)の解となります。

> **特性方程式（characteristic equation）**と**補助方程式（auxiliary equation）**という2つの用語はしばしば混用されますが、両者は完全に同じ意味です。どちらで呼んでも構いません。
{: .prompt-tip }

さて、特性方程式($\ref{eqn:characteristic_eqn}$)の判別式$a^2 - 4b$の符号によって、場合を3つに分けることができます。
- $a^2 - 4b > 0$: 互いに異なる2つの実数解
- $a^2 - 4b = 0$: 実数の重根
- $a^2 - 4b < 0$: 共役複素数解

## 特性方程式の判別式の符号による一般解の形
### I. 互いに異なる2つの実数解 $\lambda_1$と$\lambda_2$
この場合、任意の区間で方程式($\ref{eqn:ode_with_constant_coefficients}$)の解の基底は

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

であり、これによる一般解は

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

です。

### II. 実数の重根 $\lambda = -\cfrac{a}{2}$
$a^2 - 4b = 0$の場合、二次方程式($\ref{eqn:characteristic_eqn}$)は一つの解$\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$のみを得ることになり、したがってこれから得られる$y = e^{\lambda x}$形の解は

$$ y_1 = e^{-(a/2)x} $$

の一つだけです。基底を得るためには、$y_1$と独立な異なる形の第二の解$y_2$を見つけ出す必要があります。

このような状況で活用できるのが、先に調べた[階数低下](/posts/homogeneous-linear-odes-of-second-order/#階数低下-reduction-of-order)です。求めたい第二の解を$y_2=uy_1$と置き、

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

を方程式($\ref{eqn:ode_with_constant_coefficients}$)に代入すると

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

を得ます。$u^{\prime\prime}$、$u^\prime$、$u$の各項でまとめて整理すると

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

です。ここで、$y_1$は方程式($\ref{eqn:ode_with_constant_coefficients}$)の解であるため、最後の括弧内の式は$0$であり、

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

なので、最初の括弧内の式も$0$です。したがって、$u^{\prime\prime}y_1 = 0$だけが残り、これから$u^{\prime\prime}=0$です。2回積分すると$u = c_1x + c_2$となり、積分定数$c_1$と$c_2$は任意の値を取りうるので、単純に$c_1=1$、$c_2=0$を選択して$u=x$と置くことができます。すると$y_2 = uy_1 = xy_1$となり、$y_1$と$y_2$は線形独立なので、これらは基底を形成します。したがって、特性方程式($\ref{eqn:characteristic_eqn}$)が重根を持つ場合に、任意の区間における方程式($\ref{eqn:ode_with_constant_coefficients}$)の解の基底は

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

であり、これに対応する一般解は

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

です。

### III. 共役複素数解 $-\cfrac{1}{2}a + i\omega$と$-\cfrac{1}{2}a - i\omega$
この場合、$a^2 - 4b < 0$であり、$\sqrt{-1} = i$なので、式($\ref{eqn:lambdas}$)から

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

であり、ここで実数$\sqrt{b-\cfrac{1}{4}a^2} = \omega$と定義しましょう。

$\omega$を上記のように定義すると、特性方程式($\ref{eqn:characteristic_eqn}$)の解は共役複素数解$\lambda = -\cfrac{1}{2}a \pm i\omega$となり、これに対応する方程式($\ref{eqn:ode_with_constant_coefficients}$)の2つの複素解

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

を得ます。ただし、この場合でも虚数ではない実数解の基底を次のように得ることができます。

オイラーの公式（Euler's formula）

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

と、上の式で$t$の位置に$-t$を代入して得られる

$$ e^{-it} = \cos t - i\sin t $$

の2つの式を辺々足したり引いたりすると、次を得ます。

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

実部$r$と虚部$it$を持つ複素変数$z = r + it$の複素指数関数$e^z$は、実関数$e^r$、$\cos t$、$\sin t$を用いて次のように定義できます。

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

ここで、$r=-\cfrac{1}{2}ax$、$t=\omega x$と置くと、次のように書くことができます。

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)により、上記の複素解の和と定数倍もまた解となります。したがって、2つの等式を辺々足し、両辺に$\cfrac{1}{2}$を掛けると、最初の実数解$y_1$を次のように得ることができます。

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

同様に、最初の等式から2番目の等式を辺々引き、両辺に$\cfrac{1}{2i}$を掛けることで、2番目の実数解$y_2$を得ることができます。

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

$\cfrac{y_1}{y_2} = \cot{\omega x}$であり、これは定数ではないため、$y_1$と$y_2$はすべての区間で線形独立であり、したがって方程式($\ref{eqn:ode_with_constant_coefficients}$)の実数解の基底をなします。これから一般解

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{は任意の定数)} \label{eqn:general_sol_3}\tag{13}$$

を得ます。
