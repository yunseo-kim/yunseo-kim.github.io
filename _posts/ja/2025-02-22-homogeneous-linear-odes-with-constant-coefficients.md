---
title: "定数係数を持つ2階同次線形常微分方程式"
description: "特性方程式の判別式の符号によって、それぞれの場合に定数係数同次線形常微分方程式の一般解がどのような形になるかを考察する。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 定数係数を持つ2階同次線形常微分方程式: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **特性方程式(characteristic equation)**: $\lambda^2 + a\lambda + b = 0$
> - 特性方程式の判別式 $a^2 - 4b$の符号によって一般解の形を表のように三つの場合に分けることができる
>
> | 場合 | 特性方程式の解 | 常微分方程式の解の基底 | 常微分方程式の一般解 |
> | :---: | :---: | :---: | :---: |
> | I | 異なる実根<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | 実重根<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | 共役複素根<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [ベルヌーイ方程式(Bernoulli Equation)](/posts/Bernoulli-Equation/)
- [2階同次線形常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- オイラーの公式

## 特性方程式 (characteristic equation)
係数 $a$と $b$が定数である2階同次線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

を考えよう。この形の方程式は機械的、電気的振動において重要な応用がある。

先に[ベルヌーイ方程式(Bernoulli Equation)](/posts/Bernoulli-Equation/)でロジスティック方程式の一般解を求めたが、それによると定数係数 $k$を持つ1階線形常微分方程式

$$ y^\prime + ky = 0 $$

の解は指数関数 $y = ce^{-kx}$である。（その記事の式(4)で $A=-k$, $B=0$の場合）

したがって、同様の形の方程式である($\ref{eqn:ode_with_constant_coefficients}$)に対しても

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

形の解をまず試してみることができる。

> もちろんこれはあくまで推測に過ぎず、実際に一般解がこのような形であるという保証は全くない。しかし何であれ線形独立な二つの解さえ求めることができれば、[2階同次線形常微分方程式](/posts/homogeneous-linear-odes-of-second-order/#基底と一般解)で見たように[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)によって一般解を求めることができる。  
> 後で見るように、[別の形の解を求める必要がある場合](#ii-実重根-lambda---cfraca2)もある。
{: .prompt-info }

式($\ref{eqn:general_sol}$)とその導関数

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

を式($\ref{eqn:ode_with_constant_coefficients}$)に代入すると

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

を得る。したがって、もし $\lambda$が**特性方程式(characteristic equation)**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

の解であれば、指数関数($\ref{eqn:general_sol}$)は常微分方程式($\ref{eqn:ode_with_constant_coefficients}$)の解である。二次方程式($\ref{eqn:characteristic_eqn}$)の解を求めると

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 + 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

となり、これから二つの関数

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

が方程式($\ref{eqn:ode_with_constant_coefficients}$)の解となる。

> **特性方程式(characteristic equation)**と**補助方程式(auxiliary equation)**という二つの用語がよく混用されるが、両者は全く同じ意味である。どちらで呼んでも構わない。
{: .prompt-tip }

ここで、特性方程式($\ref{eqn:characteristic_eqn}$)の判別式 $a^2 - 4b$の符号によって場合を三つに分けることができる。
- $a^2 - 4b > 0$: 異なる二つの実根
- $a^2 - 4b = 0$: 実重根
- $a^2 - 4b < 0$: 共役複素根

## 特性方程式の判別式の符号による一般解の形
### I. 異なる二つの実根 $\lambda_1$と $\lambda_2$
この場合、任意の区間で方程式($\ref{eqn:ode_with_constant_coefficients}$)の解の基底は

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

であり、これに対応する一般解は

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

である。

### II. 実重根 $\lambda = -\cfrac{a}{2}$
$a^2 - 4b = 0$の場合、二次方程式($\ref{eqn:characteristic_eqn}$)は一つの解 $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$しか得られず、したがってこれから得られる $y = e^{\lambda x}$ 形の解は

$$ y_1 = e^{-(a/2)x} $$

の一つだけである。基底を得るためには $y_1$と独立した別の形の二番目の解 $y_2$を見つける必要がある。

このような状況で活用できるのが、先に学んだ[次数低下法](/posts/homogeneous-linear-odes-of-second-order/#次数低下法-reduction-of-order)である。求めたい二番目の解を $y_2=uy_1$とおき、

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

を方程式($\ref{eqn:ode_with_constant_coefficients}$)に代入すると

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

を得る。$u^{\prime\prime}$, $u^\prime$, $u$ の各項ごとにまとめて整理すると

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

となる。ここで $y_1$が方程式($\ref{eqn:ode_with_constant_coefficients}$)の解であるため、最後の括弧内の式は $0$であり、

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

なので最初の括弧内の式も $0$である。したがって $u^{\prime\prime}y_1 = 0$だけが残り、これから $u^{\prime\prime}=0$となる。二回積分すると $u = c_1x + c_2$となり、積分定数 $c_1$と $c_2$はどんな値でもよいので、単純に $c_1=1$, $c_2=0$を選んで $u=x$とすることができる。すると $y_2 = uy_1 = xy_1$となり、$y_1$と $y_2$は線形独立なのでこの二つは基底を形成する。したがって特性方程式($\ref{eqn:characteristic_eqn}$)が重根を持つ場合、任意の区間での方程式($\ref{eqn:ode_with_constant_coefficients}$)の解の基底は

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

であり、これに対応する一般解は

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

である。

### III. 共役複素根 $-\cfrac{1}{2}a + i\omega$と $-\cfrac{1}{2}a - i\omega$
この場合 $a^2 - 4b < 0$であり $\sqrt{-1} = i$なので、式($\ref{eqn:lambdas}$)から

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

となり、ここで実数 $\sqrt{b-\cfrac{1}{4}a^2} = \omega$と定義しよう。

$\omega$を上のように定義すると特性方程式($\ref{eqn:characteristic_eqn}$)の解は共役複素根 $\lambda = -\cfrac{1}{2}a \pm i\omega$となり、これに対応する方程式($\ref{eqn:ode_with_constant_coefficients}$)の二つの複素解

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

を得る。ただしこの場合も虚数ではなく実数解の基底を次のように得ることができる。

オイラーの公式(Euler formula)

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

と、上の式で $t$ の代わりに $-t$を代入して得られる

$$ e^{-it} = \cos t - i\sin t $$

の二つの式を辺ごとに足したり引いたりすると次を得る。

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

実部 $r$と虚部 $it$を持つ複素変数 $z = r + it$の複素指数関数 $e^z$は実関数 $e^r$、$\cos t$と $\sin t$を使って次のように定義できる。

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

ここで $r=-\cfrac{1}{2}ax$, $t=\omega x$とおくと次のように書ける。

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)により、上の複素解の和と定数倍もまた解となる。したがって二つの等式を辺ごとに足して両辺に $\cfrac{1}{2}$をかけると、最初の実数解 $y_1$を次のように得ることができる。

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

同様に、最初の等式から二番目の等式を辺ごとに引いて両辺に $\cfrac{1}{2i}$をかけることで、二番目の実数解 $y_2$を得ることができる。

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

$\cfrac{y_1}{y_2} = \cot{\omega x}$であり、これは定数ではないので、$y_1$と $y_2$はすべての区間で線形独立であり、したがって方程式($\ref{eqn:ode_with_constant_coefficients}$)の実数解の基底をなす。これから一般解

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{は任意の定数)} \label{eqn:general_sol_3}\tag{13}$$

を得る。
