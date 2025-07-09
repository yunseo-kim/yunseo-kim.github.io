---
title: "2階斉次線形常微分方程式（Homogeneous Linear ODEs of Second Order）"
description: "2階線形常微分方程式の定義と特徴を解説します。特に、斉次線形常微分方程式における重要な定理である重ね合わせの原理と、それに伴う基底（basis）の概念について理解を深めます。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 2階線形常微分方程式の**標準形**: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **係数（coefficients）**: 関数 $p$, $q$
>   - **入力（input）**: $r(x)$
>   - **出力（output）** または **応答（response）**: $y(x)$
> - 斉次と非斉次
>   - **斉次（homogeneous）**: 標準形で表したとき $r(x)\equiv0$ の場合
>   - **非斉次（nonhomogeneous）**: 標準形で表したとき $r(x)\not\equiv 0$ の場合
> - **重ね合わせの原理（superposition principle）**: <u>斉次</u>線形常微分方程式 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$ について、開区間 $I$ での任意の二つの解の線形結合は、同様に与えられた方程式の解となる。つまり、与えられた斉次線形常微分方程式に対する任意の解の和と定数倍もまた、その方程式の解となる。
> - **基底（basis）** または **基本系（fundamental system）**: 区間 $I$ で線形独立な斉次線形常微分方程式の解の組 $(y_1, y_2)$
> - **階数低下（reduction of order）**: 2階斉次常微分方程式について、ある一つの解を見つけることができれば、この解と線形独立な第二の解、すなわち基底を1階常微分方程式を解くことによって見つけ出すことができ、このような方法を階数低下という。
> - 階数低下の応用: 一般的な2階常微分方程式 $F(x, y, y^\prime, y^{\prime\prime})=0$ は、線形か非線形かに関わらず、次の場合に階数低下を用いて1階に下げることができる。
>   - $y$が陽に現れない場合
>   - $x$が陽に現れない場合
>   - 斉次線形であり、一つの解が既知の場合
{: .prompt-info }

## 前提知識
- [モデリング（Modeling）の基本概念](/posts/Basic-Concepts-of-Modeling/)
- [変数分離法（Separation of Variables）](/posts/Separation-of-Variables/)
- [1階線形常微分方程式の解法](/posts/Solution-of-First-Order-Linear-ODE/)

## 2階線形常微分方程式
2階常微分方程式を

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

の形で書ける場合、**線形（linear）**であるといい、そうでない場合は**非線形（nonlinear）**であるという。

$p$、$q$、$r$が任意の$x$についての関数であるとき、この方程式は$y$とその導関数に対して線形である。

式($\ref{eqn:standard_form}$)のような形を2階線形常微分方程式の**標準形（standard form）**といい、もし与えられた2階線形常微分方程式の最初の項が$f(x)y^{\prime\prime}$であれば、方程式の両辺を$f(x)$で割ることで標準形を得ることができる。

関数$p$、$q$を**係数（coefficients）**、$r(x)$を**入力（input）**、$y(x)$を**出力（output）**または入力と初期条件に対する**応答（response）**という。

### 斉次2階線形常微分方程式
式($\ref{eqn:standard_form}$)を解こうとするある区間 $a<x<b$を$J$としよう。式($\ref{eqn:standard_form}$)で区間$J$に対して$r(x)\equiv 0$であれば

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

となり、これを**斉次（homogeneous）**という。

## 非斉次線形常微分方程式
区間$J$で$r(x)\not\equiv 0$の場合、**非斉次（nonhomogeneous）**という。

## 重ね合わせの原理

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{は任意の定数)}\tag{3}$$

の形の関数を$y_1$と$y_2$の**線形結合（linear combination）**と呼ぶ。

このとき、次が成り立つ。

> **重ね合わせの原理（superposition principle）**  
> 斉次線形常微分方程式($\ref{eqn:homogeneous_linear_ode}$)について、開区間$I$での任意の二つの解の線形結合は、同様に式($\ref{eqn:homogeneous_linear_ode}$)の解となる。つまり、与えられた斉次線形常微分方程式に対する任意の解の和と定数倍もまた、その方程式の解となる。
{: .prompt-info }

### 証明
$y_1$と$y_2$が区間$I$で方程式($\ref{eqn:homogeneous_linear_ode}$)の解であるとしよう。$y=c_1y_1+c_2y_2$を式($\ref{eqn:homogeneous_linear_ode}$)に代入すると

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

となり、恒等式となる。したがって、$y$は区間$I$で方程式($\ref{eqn:homogeneous_linear_ode}$)の解である。$\blacksquare$

> 重ね合わせの原理は斉次線形常微分方程式に対してのみ成り立ち、非斉次線形常微分方程式や非線形常微分方程式では成り立たないことに注意してください。
{: .prompt-warning }

## 基底と一般解
### 1階常微分方程式における主要概念の復習
以前に[モデリング（Modeling）の基本概念](/posts/Basic-Concepts-of-Modeling/)で見たように、1階常微分方程式に対する初期値問題（Initial Value Problem）は、常微分方程式と初期条件（initial condition）$y(x_0)=y_0$で構成される。初期条件は、与えられた常微分方程式の一般解の任意定数$c$を決定するために必要であり、このようにして決定した解を特殊解という。さて、これらの概念を2階常微分方程式に拡張しよう。

### 初期値問題と初期条件
2階斉次常微分方程式($\ref{eqn:homogeneous_linear_ode}$)に対する**初期値問題（initial value problem）**は、与えられた常微分方程式($\ref{eqn:homogeneous_linear_ode}$)と2つの**初期条件（initial conditions）**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

で構成される。この条件は、常微分方程式の**一般解（general solution）**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

の2つの任意定数$c_1$と$c_2$を決定するために必要である。

### 線形独立と線形従属
ここで少し、線形独立と線形従属の概念について見てみよう。後で基底を定義するためには、これを理解する必要がある。  
二つの関数$y_1$と$y_2$が定義された区間$I$のすべての点で

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{かつ}k_2=0 \label{eqn:linearly_independent}\tag{6}$$

であれば、この二つの関数$y_1$と$y_2$は区間$I$で**線形独立（linearly independent）**であるといい、そうでない場合、$y_1$と$y_2$は**線形従属（linearly dependent）**であるという。

もし$y_1$と$y_2$が線形従属であれば（つまり、命題($\ref{eqn:linearly_independent}$)が真でなければ）、$k_1 \neq 0$または$k_2 \neq 0$で($\ref{eqn:linearly_independent}$)の方程式の両辺を割って

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{または} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

のように書けるので、$y_1$と$y_2$が比例関係にあることがわかる。

### 基底、一般解、特殊解
話を戻すと、式($\ref{eqn:general_sol}$)が一般解となるためには、$y_1$と$y_2$は方程式($\ref{eqn:homogeneous_linear_ode}$)の解であると同時に、区間$I$で互いに比例せず線形独立（linearly independent）でなければならない。このような条件を満たす、区間$I$で線形独立な方程式($\ref{eqn:homogeneous_linear_ode}$)の解の組（pair）$(y_1, y_2)$を、区間$I$における式($\ref{eqn:homogeneous_linear_ode}$)の解の**基底（basis）**または**基本系（fundamental system）**という。

初期条件を活用して一般解($\ref{eqn:general_sol}$)の二つの定数$c_1$と$c_2$を決定することにより、点$(x_0, K_0)$を通り、その点での接線の傾きが$K_1$である唯一の解を得る。これを常微分方程式($\ref{eqn:homogeneous_linear_ode}$)の**特殊解（particular solution）**という。

式($\ref{eqn:homogeneous_linear_ode}$)が開区間$I$で連続であれば、必ず一般解を持ち、この一般解は可能なすべての特殊解を含む。つまり、この場合、方程式($\ref{eqn:homogeneous_linear_ode}$)は一般解から得られない**特異解（singular solution）**を持たない。

## 階数低下 (reduction of order)
2階斉次常微分方程式について、ある一つの解を見つけることができれば、この解と線形独立な第二の解、すなわち基底を、次のように1階常微分方程式を解くことによって見つけ出すことができる。このような方法を**階数低下（reduction of order）**という。

<u>$f(x)y^{\prime\prime}$ではなく$y^{\prime\prime}$を持つ標準形の</u>2階斉次常微分方程式

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

について、開区間$I$でこの方程式の一つの解$y_1$を知っているとしよう。

ここで、求めたい第二の解を$y_2 = uy_1$と置き、

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

を方程式に代入すると

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

を得る。$u^{\prime\prime}$、$u^{\prime}$、$u$の各項でまとめて整理すると

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

となる。しかし、$y_1$は与えられた方程式の解であるため、最後の括弧内の式は$0$となり、$u$の項が消え、$u^{\prime}$と$u^{\prime\prime}$に関する常微分方程式が残る。この残った常微分方程式の両辺を$y_1$で割り、$u^{\prime}=U$、$u^{\prime\prime}=U^{\prime}$と置くと、次のような1階常微分方程式を得る。

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

[変数分離](/posts/Separation-of-Variables/)して積分すると

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

となり、両辺に指数関数を適用すると、最終的に

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

を得る。先に$U=u^{\prime}$と置いたので、$u=\int U dx$となり、求めたい第二の解$y_2$は

$$ y_2 = uy_1 = y_1 \int U dx $$

である。$\cfrac{y_2}{y_1} = u = \int U dx$は$U>0$である限り定数にはなり得ないので、$y_1$と$y_2$は解の基底を形成する。

### 階数低下の応用
一般的な2階常微分方程式$F(x, y, y^\prime, y^{\prime\prime})=0$は、線形か非線形かに関わらず、$y$が陽に現れないか、$x$が陽に現れないか、または前述のように斉次線形であり一つの解が既知である場合に、階数低下を用いて1階に下げることができる。

#### $y$が陽に現れない場合
$F(x, y^\prime, y^{\prime\prime})=0$で$z=y^{\prime}$と置くと、$z$に関する1階常微分方程式$F(x, z, z^{\prime})$に下げることができる。

#### $x$が陽に現れない場合
$F(y, y^\prime, y^{\prime\prime})=0$で$z=y^{\prime}$と置くと、$y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$となるので、$y$が独立変数$x$の役割を代行する$z$に関する1階常微分方程式$F(y,z,z^\prime)$に下げることができる。
