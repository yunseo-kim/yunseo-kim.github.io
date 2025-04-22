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
>   - **定数係数$a$と$b$**を持ち
>   - 入力$r(x)$が指数関数、$x$の累乗、$\cos$または$\sin$、あるいはこれらの関数の和と積からなる
>   - 線形常微分方程式$y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **未定係数法における選択規則**  
>   - **(a) 基本規則(basic rule)**: 式($\ref{eqn:linear_ode_with_constant_coefficients}$)において$r(x)$が表の最初の列にある関数のうちの一つであれば、同じ行の$y_p$を選び、$y_p$とその導関数を式($\ref{eqn:linear_ode_with_constant_coefficients}$)に代入することによって未定係数を決定する。  
>   - **(b) 変形規則(modification rule)**: $y_p$として選んだ項が式($\ref{eqn:linear_ode_with_constant_coefficients}$)に対応する同次常微分方程式$y^{\prime\prime} + ay^{\prime} + by = 0$の解になる場合、この項に$x$(またはこの解が同次常微分方程式の特性方程式の重根に対応する場合は$x^2$)を掛ける。  
>   - **(c) 和規則(sum rule)**: $r(x)$が表の最初の列にある関数の和である場合、2列目の対応する行にある関数の和を$y_p$として選ぶ。
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
- [定数係数を持つ2階同次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [オイラー・コーシー方程式](/posts/euler-cauchy-equation/)
- [ロンスキアン(Wronskian)、解の存在と一意性](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [2階非同次線形常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)
- ベクトル空間、線形生成（線形代数学）

## 未定係数法
$r(x) \not\equiv 0$である2階非同次線形常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

とこの非同次常微分方程式に対応する同次常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

を考えよう。

先に[2階非同次線形常微分方程式 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)で見たように、非同次線形常微分方程式($\ref{eqn:nonhomogeneous_linear_ode}$)の初期値問題を解くためには、同次常微分方程式($\ref{eqn:homogeneous_linear_ode}$)を解いて$y_h$を求めた後、方程式($\ref{eqn:nonhomogeneous_linear_ode}$)の一つの解$y_p$を見つけて一般解

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

を得る必要がある。では$y_p$はどのように見つけることができるだろうか？$y_p$を見つける一般的な方法は**パラメータ変換法(method of variation of parameters)**だが、場合によってはそれよりもはるかに簡単な**未定係数法(method of undetermined coefficients)**を適用することができる。特に、振動系とRLC電気回路モデルに適用できるため、工学でよく使われる方法である。

未定係数法は**定数係数$a$と$b$**を持ち、入力$r(x)$が指数関数、$x$の累乗、$\cos$または$\sin$、あるいはこれらの関数の和と積からなる線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

に適している。このような形の$r(x)$は自分自身と類似した形の導関数を持つという点が未定係数法の核心である。未定係数法を適用するためには、$r(x)$と類似した形でありながら、自分自身とその導関数を与えられた常微分方程式に代入することによって決定される未知の係数を持つ$y_p$を選ぶ。工学で実用的に重要な形の$r(x)$に対して適切な$y_p$を選ぶための規則は次のとおりである。

> **未定係数法における選択規則**  
> **(a) 基本規則(basic rule)**: 式($\ref{eqn:linear_ode_with_constant_coefficients}$)において$r(x)$が表の最初の列にある関数のうちの一つであれば、同じ行の$y_p$を選び、$y_p$とその導関数を式($\ref{eqn:linear_ode_with_constant_coefficients}$)に代入することによって未定係数を決定する。  
> **(b) 変形規則(modification rule)**: $y_p$として選んだ項が式($\ref{eqn:linear_ode_with_constant_coefficients}$)に対応する同次常微分方程式$y^{\prime\prime} + ay^{\prime} + by = 0$の解になる場合、この項に$x$(またはこの解が同次常微分方程式の特性方程式の重根に対応する場合は$x^2$)を掛ける。  
> **(c) 和規則(sum rule)**: $r(x)$が表の最初の列にある関数の和である場合、2列目の対応する行にある関数の和を$y_p$として選ぶ。
>
> | $r(x)$の項 | $y_p(x)$に対する選択 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

この方法は簡便であるだけでなく、自己修正性を持つという利点がある。$y_p$を誤って選択したり、少なすぎる項を選択したりすると矛盾に至り、多すぎる項を選択した場合は不要な項の係数が$0$になって正しい結果が得られる。未定係数法を適用して何かがうまくいかなくても、解法の過程で自然に気づくことができるので、上記の選択規則に従ってある程度適切な$y_p$を選択したなら、気軽に試してみることができる。

### 和規則の証明
$r(x) = r_1(x) + r_2(x)$の形の非同次線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

を考えよう。ここで同じ左辺に入力として$r_1$、$r_2$を持つ次の二つの方程式

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

がそれぞれ${y_p}_1$、${y_p}_2$を解として持つとする。与えられた方程式の左辺を$L[y]$と表記すると、$L[y]$の線形性により$y_p = {y_p}_1 + {y_p}_2$に対して次を満たすので和規則が成立する。

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## 例題: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
基本規則(a)に従って$y_p = Ce^{\gamma x}$とおき、与えられた方程式$y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$に代入すると

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### $\gamma^2 + a\gamma + b \neq 0$の場合
次のように未定係数$C$を決定し、$y_p$を求めることができる。

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### $\gamma^2 + a\gamma + b = 0$の場合
この場合、変形規則(b)を適用する必要がある。まず$b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$を利用して同次常微分方程式$y^{\prime\prime} + ay^{\prime} + by = 0$の特性方程式の根を求めよう。

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

これより同次常微分方程式の基底

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

を得る。

#### $\gamma \neq -a-\gamma$の場合
$y_p$として選んだ$Ce^{\gamma x}$が与えられた方程式に対応する同次常微分方程式の重根ではない解であるため、変形規則(b)に従ってこの項に$x$を掛けて$y_p = Cxe^{\gamma x}$とおく。

この変形した$y_p$を再び与えられた方程式$y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$に代入すると

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### $\gamma = -a-\gamma$の場合
この場合、$y_p$として選んだ$Ce^{\gamma x}$が与えられた方程式に対応する同次常微分方程式の重根であるため、変形規則(b)に従ってこの項に$x^2$を掛けて$y_p = Cx^2 e^{\gamma x}$とおく。

この変形した$y_p$を再び与えられた方程式$y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$に代入すると

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## 未定係数法の拡張: 関数の積形式の$r(x)$
$r(x) = k x^n e^{\alpha x}\cos(\omega x)$の形の非同次線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

を考えよう。$r(x)$をこのように指数関数$e^{\alpha x}$、$x$の累乗$x^m$、$\cos{\omega x}$または$\sin{\omega x}$(ここでは$\cos$と仮定し、これでも一般性を失わない)、あるいはこれらの関数の和と積とすると(つまり、先の表の最初の列にある関数の和と積で表現できるとすると)、同じ表の2列目にある関数の和と積である方程式の解$y_p$が存在することを示す。

> 厳密な証明のために線形代数学を使用して記述した部分があり、そのような部分は\*で示している。該当部分をスキップして残りの部分だけ読んでも概略的な理解には問題ない。
{: .prompt-tip }

### ベクトル空間$V$の定義\*
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

である$r(x)$に対して、$r(x) \in V$であるベクトル空間$V$を次のように取ることができる。

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### 指数関数、多項式関数、三角関数の導関数の形
先の表の最初の列に示された基本関数の導関数の形は次のとおりである。
- 指数関数: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- 多項式関数: $\cfrac{d}{dx}x^m = mx^{m-1}$
- 三角関数: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

これらの関数を微分して得られる導関数もまた<u>同じ種類の関数の和</u>として表現される。

したがって、関数$f$と$g$が上記の関数またはそれらの和であるとき、$r(x) = f(x)g(x)$に対して積の微分法を適用すると

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

となり、ここで$f$、$f^{\prime}$、$f^{\prime\prime}$と$g$、$g^{\prime}$、$g^{\prime\prime}$はすべて指数関数、多項式関数、三角関数の和または定数倍の形で書くことができる。したがって$r^{\prime}(x) = (fg)^{\prime}$、$r^{\prime\prime}(x) = (fg)^{\prime\prime}$も$r(x)$と同様にこれらの関数の和と積として表現できる。

### $V$の微分演算$D$、線形変換$L$に対する不変\*
つまり、$r(x)$自体だけでなく$r^{\prime}(x)$、$r^{\prime\prime}(x)$も$x^k e^{\alpha x}\cos(\omega x)$形の項と$x^k e^{\alpha x}\sin(\omega x)$形の項の線形結合であるため

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

$r(x)$に限定せず、先に定義したベクトル空間$V$のすべての要素に対して微分演算子$D$を導入してより一般的に表現すると、*ベクトル空間$V$は微分演算$D$に対して閉じている*。したがって与えられた方程式の左辺$y^{\prime\prime} + ay^{\prime} + by$を$L[y]$と表記すると、*$V$は$L$に対して不変(invariant)である*。

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

$r(x) \in V$であり$V$が$L$に対して不変であるため、$L[y_p] = r$を満たす$V$の別の要素$y_p$が存在する。

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
したがって、すべての可能な積形式の項の和になるように適切な$y_p$を未定係数$A_0, A_1, \dots, A_n$と$K$、$M$を用いて次のように選べば、基本規則(a)と変形規則(b)に従って$y_p$(または$xy_p$、$x^2y_p$)とその導関数を与えられた方程式に代入することによって未定係数を決定できる。このとき$n$は$r(x)$の$x$に関する次数に応じて決定すればよい。

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> もし与えられた入力$r(x)$が異なる複数の$\alpha_i$、$\omega_j$値を含む場合、各$\alpha_i$と$\omega_j$値に対しても可能なすべての$x^{k}e^{\alpha_i x}\cos(\omega_j x)$、$x^{k}e^{\alpha_i x}\sin(\omega_j x)$形の項を漏れなく含めるように$y_p$を選ぶ必要がある。  
> 未定係数法の利点は簡便であることなので、仮説解(ansatz)が複雑になりすぎてこの利点が薄れる場合は、むしろ後で扱うパラメータ変換法を適用する方が良いかもしれない。
{: .prompt-warning }

## 未定係数法の拡張: オイラー・コーシー方程式
[定数係数を持つ2階同次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)だけでなく、[オイラー・コーシー方程式](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

に対しても未定係数法を活用できる。

### 変数変換
[$x = e^t$と変換して定数係数を持つ2階同次線形常微分方程式に変換](/posts/euler-cauchy-equation/#定数係数を持つ2階同次線形常微分方程式への変換)すると

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

となり、オイラー・コーシー方程式を次のように$t$に関する定数係数同次線形常微分方程式に変えることができることを先に学んだ。

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

ここで式($\ref{eqn:substituted}$)に対して[先ほど見た未定係数法](#未定係数法)を同様に適用して$t$について解き、最後に$t = \ln x$であることを利用して$x$に関する解を求めればよい。

### $r(x)$が$x$の累乗、自然対数、またはこれらの関数の和と積である場合
特に入力$r(x)$が$x$の累乗、自然対数、またはこれらの関数の和と積からなる場合、次のオイラー・コーシー方程式用選択規則に従って適切な$y_p$を直接選ぶことができる。

> **未定係数法における選択規則: オイラー・コーシー方程式用**  
> **(a) 基本規則(basic rule)**: 式($\ref{eqn:euler_cauchy}$)において$r(x)$が表の最初の列にある関数のうちの一つであれば、同じ行の$y_p$を選び、$y_p$とその導関数を式($\ref{eqn:euler_cauchy}$)に代入することによって未定係数を決定する。  
> **(b) 変形規則(modification rule)**: $y_p$として選んだ項が式($\ref{eqn:euler_cauchy}$)に対応する同次常微分方程式$x^2y^{\prime\prime} + axy^{\prime} + by = 0$の解になる場合、この項に$\ln{x}$(またはこの解が同次常微分方程式の特性方程式の重根に対応する場合は$(\ln{x})^2$)を掛ける。  
> **(c) 和規則(sum rule)**: $r(x)$が表の最初の列にある関数の和である場合、2列目の対応する行にある関数の和を$y_p$として選ぶ。
>
> | $r(x)$の項 | $y_p(x)$に対する選択 |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

このようにすれば、実用的に重要な形の入力$r(x)$に対して[変数変換](#変数変換)で得るのと同じ$y_p$をより速く簡単に見つけることができる。先に見た[元の選択規則](#未定係数法)で$x$の代わりに$\ln{x}$を入れると、このオイラー・コーシー方程式用選択規則を導くことができる。
