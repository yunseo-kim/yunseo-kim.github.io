---
title: "2階非同次線形常微分方程式（Nonhomogeneous Linear ODEs of Second Order）"
description: "2階非同次線形常微分方程式の一般解の構造と特性について学び、対応する同次方程式との関係を理解する。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 2階非同次線形常微分方程式 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$の**一般解**:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: 同次常微分方程式 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$の一般解 $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: 該当非同次常微分方程式の特殊解
> - 応答項 $y_p$は入力 $r(x)$によってのみ決定され、同じ非同次常微分方程式に対しては初期条件が異なっても $y_p$は変わらない。非同次常微分方程式の二つの特殊解の差は対応する同次常微分方程式の解となる。
> - **一般解の存在**: 非同次常微分方程式の係数 $p(x)$、$q(x)$と入力関数 $r(x)$が連続であれば一般解は常に存在する
> - **特異解の非存在**: 一般解は方程式のすべての解を含む（つまり、特異解は存在しない）
{: .prompt-info }

## Prerequisites
- [2階同次線形常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [ロンスキアン（Wronskian）、解の存在と一意性](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## 2階非同次線形常微分方程式の一般解と特殊解
2階非同次線形常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

を考えよう。ここで $r(x) \not\equiv 0$である。開区間 $I$で方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の**一般解**はこの非同次常微分方程式に対応する同次常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

の一般解 $y_h = c_1y_1 + c_2y_2$と式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の特殊解 $y_p$の和

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

の形である。また区間 $I$で方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の**特殊解**は $y_h$の任意定数 $c_1$と $c_2$に特定の値を指定して式 ($\ref{eqn:general_sol}$)から得られる解である。

つまり、同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)に独立変数 $x$のみに依存する入力 $r(x)$を追加すると、それに対応する項 $y_p$が応答に追加され、この追加された応答項 $y_p$は初期条件に関係なく入力 $r(x)$のみによって決定される。後で見るように、式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の任意の二つの解 $y_1$と $y_2$の差を求めると（つまり、異なる二つの初期条件に対するそれぞれの特殊解の差を求めると）初期条件に無関係な $y_p$部分は消え、${y_h}_1$と ${y_h}_2$の差だけが残り、これは[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)により式 ($\ref{eqn:homogeneous_linear_ode}$)の解となる。

## 非同次常微分方程式の解と、それに対応する同次常微分方程式の解の関係
> **定理1: 非同次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の解と同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)の解の関係**  
> **(a)** ある開区間 $I$で非同次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の解 $y$と同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)の解 $\tilde{y}$の和は区間 $I$で方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の解である。特に式 ($\ref{eqn:general_sol}$)は区間 $I$で方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の解である。  
> **(b)** 区間 $I$で非同次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の二つの解の差は区間 $I$で同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)の解である。
{: .prompt-info }

### 証明
#### (a)
方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)と ($\ref{eqn:homogeneous_linear_ode}$)の左辺を $L[y]$と表記しよう。すると区間 $I$で式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の任意の解 $y$と式 ($\ref{eqn:homogeneous_linear_ode}$)の任意の解 $\tilde{y}$に対しても次を満たす。

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
区間 $I$で式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の任意の二つの解 $y$と $y^\*$に対して次を満たす。

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## 非同次常微分方程式の一般解はすべての解を含む
同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)について[一般解がすべての解を含むことを知っている](/posts/wronskian-existence-and-uniqueness-of-solutions/#一般解はすべての解を含む)。非同次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)についても同じことが成り立つことを示そう。

> **定理2: 非同次常微分方程式の一般解はすべての解を含む**  
> 方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の係数 $p(x)$、$q(x)$と入力関数 $r(x)$がある開区間 $I$で連続ならば、区間 $I$で式 ($\ref{eqn:nonhomogeneous_linear_ode}$)のすべての解は区間 $I$で式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の一般解 ($\ref{eqn:general_sol}$)の $y_h$の任意定数 $c_1$と $c_2$に適当な値を指定することによって得ることができる。
{: .prompt-info }

### 証明
$y^\*$を $I$で方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)のある解とし、$x_0$を区間 $I$内のある $x$とする。[連続な変数係数を持つ同次常微分方程式の一般解の存在定理](/posts/wronskian-existence-and-uniqueness-of-solutions/#一般解の存在)により $y_h = c_1y_1 + c_2y_2$が存在し、後で学ぶ**パラメータ変化法（method of variation of parameters）**により $y_p$も存在するため、区間 $I$で方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の一般解 ($\ref{eqn:general_sol}$)は存在する。ここで先に証明した定理[1(b)](#非同次常微分方程式の解とそれに対応する同次常微分方程式の解の関係)により $Y = y^\* - y_p$は区間 $I$で同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)の解であり、$x_0$で

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

である。[初期値問題の解の存在性と一意性の定理](/posts/wronskian-existence-and-uniqueness-of-solutions/#初期値問題の解の存在性と一意性の定理)によれば、区間 $I$で上記の初期条件に対して $y_h$の $c_1$、$c_2$に適当な値を指定して得られる同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)の特殊解 $Y$が唯一存在する。$y^\* = Y + y_p$であるため、非同次常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の任意の特殊解 $y^\*$を一般解 ($\ref{eqn:general_sol}$)から得られることを示した。$\blacksquare$
