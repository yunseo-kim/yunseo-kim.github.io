---
title: 未定係数法
description: 特定の形の定数係数非同次線形常微分方程式に対する初期値問題を簡単に解くことができ、工学において振動系、RLC電気回路モデルなどに対して有用によく使われる解法である未定係数法について学びましょう。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **未定係数法**の適用対象:
>   - **定数係数 $a$と $b$**を持ち
>   - 入力 $r(x)$が指数関数、$x$の累乗、$\cos$または$\sin$、あるいはこれらの関数の和と積で構成される
>   - 線形常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **未定係数法に対する選択規則**  
>   - **(a) 基本規則(basic rule)**: 式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)で $r(x)$が表の最初の列にある関数のうちの一つであれば、同じ行の $y_p$を選択し、$y_p$とその導関数を式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に代入することによって未定係数を決定する。  
>   - **(b) 変形規則(modification rule)**: $y_p$として選択した項が式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に対応する同次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$の解になる場合、この項に $x$（またはもしこの解が同次常微分方程式の特性方程式の重根に対応する場合は $x^2$）を掛ける。  
>   - **(c) 和規則(sum rule)**: $r(x)$が表の最初の列にある関数の和である場合、二番目の列の対応する行にある関数の和を $y_p$として選択する。
>
> | $r(x)$の項 | $y_p(x)$に対する選択 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [2階同次線形常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [ロンスキアン(Wronskian)、解の存在と一意性](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [2階非同次線形常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)

## 未定係数法
$r(x) \not\equiv 0$である2階非同次線形常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

とこの非同次常微分方程式に対応する同次常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

を考えよう。

先に[2階非同次線形常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)で見たように、非同次線形常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)に対する初期値問題を解くためには、同次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)を解いて $y_h$を求めた後、方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の一つの解 $y_p$を見つけて一般解

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

を得る必要がある。それでは $y_p$はどのように見つけることができるのか？$y_p$を見つける一般的な方法は**パラメータ変換法(method of variation of parameters)**だが、場合によってはそれよりもはるかに簡単な**未定係数法(method of undetermined coefficients)**を適用することができる。特に、振動系とRLC電気回路モデルに適用できるため、工学でよく使用される方法である。

未定係数法は**定数係数 $a$と $b$**を持ち、入力 $r(x)$が指数関数、$x$の累乗、$\cos$または$\sin$、あるいはこれらの関数の和と積で構成される線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

に適している。このような形の $r(x)$は自分自身と類似した形の導関数を持つという点が未定係数法の核心である。未定係数法を適用するためには、$r(x)$と類似した形でありながら、自分自身とその導関数を与えられた常微分方程式に代入することによって決定される未知の係数を持つ $y_p$を選択する。工学で実用的に重要な形の $r(x)$に対して適切な $y_p$を選択するための規則は次のとおりである。

> **未定係数法に対する選択規則**  
> **(a) 基本規則(basic rule)**: 式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)で $r(x)$が表の最初の列にある関数のうちの一つであれば、同じ行の $y_p$を選択し、$y_p$とその導関数を式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に代入することによって未定係数を決定する。  
> **(b) 変形規則(modification rule)**: $y_p$として選択した項が式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に対応する同次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$の解になる場合、この項に $x$（またはもしこの解が同次常微分方程式の特性方程式の重根に対応する場合は $x^2$）を掛ける。  
> **(c) 和規則(sum rule)**: $r(x)$が表の最初の列にある関数の和である場合、二番目の列の対応する行にある関数の和を $y_p$として選択する。
>
> | $r(x)$の項 | $y_p(x)$に対する選択 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

この方法は簡便であるだけでなく、自己修正性を持つという利点がある。$y_p$を間違って選択したり、あまりにも少ない数の項を選択すると矛盾に至り、あまりにも多くの項を選択した場合、不必要な項の係数は$0$になって正しい結果を得る。未定係数法を適用して何かが間違っていても、解法の過程で自然に気づくことになるので、上記の選択規則に従ってある程度適当な$y_p$を選択したら、気軽に試してみることができる。

### 和規則の証明
$r(x) = r_1(x) + r_2(x)$の形の非同次線形常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

を考えよう。ここで同じ左辺に入力として$r_1$、$r_2$を持つ次の二つの方程式

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

がそれぞれ${y_p}_1$、${y_p}_2$を解として持つとしよう。与えられた方程式の左辺を$L[y]$と表記すると、$L[y]$の線形性により$y_p = {y_p}_1 + {y_p}_2$に対して次を満たすので和規則が成立する。

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

### 例題: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
基本規則 (a)に従って $y_p = Ce^{\gamma x}$とおき、与えられた方程式 $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$に代入すると

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### $\gamma^2 + a\gamma + b \neq 0$の場合
次のように未定係数 $C$を決定し $y_p$を求めることができる。

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### $\gamma^2 + a\gamma + b = 0$の場合
この場合、変形規則 (b)を適用する必要がある。まず $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$を利用して同次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$の特性方程式の根を求めよう。

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

これより同次常微分方程式の基底

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

を得る。

##### $\gamma \neq -a-\gamma$の場合
$y_p$として選択した $Ce^{\gamma x}$が与えられた方程式に対応する同次常微分方程式の重根ではない解であるため、変形規則 (b)に従ってこの項に $x$を掛けて $y_p = Cxe^{\gamma x}$とおく。

ここで変形した $y_p$を再び与えられた方程式 $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$に代入すると

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### $\gamma = -a-\gamma$の場合
この場合、$y_p$として選択した $Ce^{\gamma x}$が与えられた方程式に対応する同次常微分方程式の重根であるため、変形規則 (b)に従ってこの項に $x^2$を掛けて $y_p = Cx^2 e^{\gamma x}$とおく。

ここで変形した $y_p$を再び与えられた方程式 $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$に代入すると

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
