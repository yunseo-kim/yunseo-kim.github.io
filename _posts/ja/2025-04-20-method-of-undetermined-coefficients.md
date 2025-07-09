---
title: "未定係数法"
description: "工学の振動系やRLC回路モデルで頻繁に用いられる、特定の形の定数係数非斉次線形常微分方程式を簡単に解くための未定係数法について解説します。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **未定係数法**の適用対象：
>   - **定数係数 $a$ と $b$** を持ち
>   - 入力 $r(x)$ が指数関数、$x$のべき乗、$\cos$ または $\sin$、あるいはこれらの関数の和と積で構成される
>   - 線形常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **未定係数法における選択規則**  
>   - **(a) 基本規則（basic rule）**: 式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)において、$r(x)$が表の最初の列にある関数のいずれかである場合、同じ行の$y_p$を選択し、$y_p$とその導関数を式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に代入することで未定係数を決定する。  
>   - **(b) 修正規則（modification rule）**: $y_p$として選択した項が、式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に対応する斉次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$の解となる場合、この項に$x$（または、もしこの解が斉次常微分方程式の特性方程式の重解に該当する場合は$x^2$）を掛ける。  
>   - **(c) 重ね合わせの規則（sum rule）**: $r(x)$が表の最初の列にある関数の和である場合、2番目の列の対応する行にある関数の和を$y_p$として選択する。
>
> | $r(x)$の項 | $y_p(x)$の選択 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## 前提知識
- [2階斉次線形常微分方程式（Homogeneous Linear ODEs of Second Order）](/posts/homogeneous-linear-odes-of-second-order/)
- [定数係数を持つ2階斉次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [オイラー・コーシー方程式](/posts/euler-cauchy-equation/)
- [ロンスキアン（Wronskian）、解の存在と一意性](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [2階非斉次線形常微分方程式（Nonhomogeneous Linear ODEs of Second Order）](/posts/nonhomogeneous-linear-odes-of-second-order/)
- ベクトル空間、線形スパン（線形代数学）

## 未定係数法
$r(x) \not\equiv 0$である2階非斉次線形常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

と、この非斉次常微分方程式に対応する斉次常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

を考えます。

以前、[2階非斉次線形常微分方程式（Nonhomogeneous Linear ODEs of Second Order）](/posts/nonhomogeneous-linear-odes-of-second-order/)で見たように、非斉次線形常微分方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の初期値問題を解くためには、斉次常微分方程式 ($\ref{eqn:homogeneous_linear_ode}$)を解いて$y_h$を求め、その後、方程式 ($\ref{eqn:nonhomogeneous_linear_ode}$)の一つの解$y_p$を見つけて一般解

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

を得る必要があります。では、$y_p$はどのように見つけることができるのでしょうか？$y_p$を見つける一般的な方法は**定数変化法（method of variation of parameters）**ですが、場合によってはそれよりもはるかに簡単な**未定係数法（method of undetermined coefficients）**を適用することができます。特に、振動系やRLC電気回路モデルに適用できるため、工学で頻繁に使用される方法です。

未定係数法は、**定数係数 $a$ と $b$** を持ち、入力 $r(x)$ が指数関数、$x$のべき乗、$\cos$ または $\sin$、あるいはこれらの関数の和と積で構成される線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

に適しています。このような形の$r(x)$は、それ自体と類似した形の導関数を持つという点が未定係数法の核心です。未定係数法を適用するためには、$r(x)$と類似した形でありながら、それ自体とその導関数を与えられた常微分方程式に代入することで決定される未知の係数を持つ$y_p$を選択します。工学で実用的に重要な形の$r(x)$に対して、適切な$y_p$を選択するための規則は次のとおりです。

> **未定係数法における選択規則**  
> **(a) 基本規則（basic rule）**: 式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)において、$r(x)$が表の最初の列にある関数のいずれかである場合、同じ行の$y_p$を選択し、$y_p$とその導関数を式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に代入することで未定係数を決定する。  
> **(b) 修正規則（modification rule）**: $y_p$として選択した項が、式 ($\ref{eqn:linear_ode_with_constant_coefficients}$)に対応する斉次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$の解となる場合、この項に$x$（または、もしこの解が斉次常微分方程式の特性方程式の重解に該当する場合は$x^2$）を掛ける。  
> **(c) 重ね合わせの規則（sum rule）**: $r(x)$が表の最初の列にある関数の和である場合、2番目の列の対応する行にある関数の和を$y_p$として選択する。
>
> | $r(x)$の項 | $y_p(x)$の選択 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

この方法は、手軽であるだけでなく、自己修正性を持つという利点があります。$y_p$を誤って選択したり、項の数が少なすぎたりすると矛盾に至り、多すぎる項を選択した場合は不要な項の係数が$0$となり、正しい結果を得ます。未定係数法を適用して何か問題が生じても、解法の過程で自然に気づくことができるため、上記の選択規則に従ってある程度適切な$y_p$を選択したならば、気軽に試すことができます。

### 重ね合わせの規則の証明
$r(x) = r_1(x) + r_2(x)$ の形である非斉次線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

を考えます。ここで、同じ左辺に入力として$r_1$、$r_2$を持つ次の2つの方程式

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

がそれぞれ${y_p}_1$、${y_p}_2$を解として持つとします。与えられた方程式の左辺を$L[y]$と表記すると、$L[y]$の線形性により、$y_p = {y_p}_1 + {y_p}_2$に対して次を満たすため、重ね合わせの規則が成り立ちます。

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## 例題: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
基本規則 (a) に従い、$y_p = Ce^{\gamma x}$と置いて与えられた方程式 $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$に代入すると

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### $\gamma^2 + a\gamma + b \neq 0$の場合
次のように未定係数$C$を決定し、$y_p$を求めることができます。

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### $\gamma^2 + a\gamma + b = 0$の場合
この場合、修正規則 (b) を適用する必要があります。まず、$b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$であることを利用して、斉次常微分方程式 $y^{\prime\prime} + ay^{\prime} + by = 0$の特性方程式の根を求めましょう。

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

これにより、斉次常微分方程式の基底

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

を得ます。

#### $\gamma \neq -a-\gamma$の場合
$y_p$として選択した$Ce^{\gamma x}$が、与えられた方程式に対応する斉次常微分方程式の重解ではない解であるため、修正規則 (b) に従い、この項に$x$を掛けて$y_p = Cxe^{\gamma x}$と置きます。

ここで、修正した$y_p$を再び与えられた方程式 $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$に代入すると

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### $\gamma = -a-\gamma$の場合
この場合、$y_p$として選択した$Ce^{\gamma x}$が、与えられた方程式に対応する斉次常微分方程式の重解であるため、修正規則 (b) に従い、この項に$x^2$を掛けて$y_p = Cx^2 e^{\gamma x}$と置きます。

ここで、修正した$y_p$を再び与えられた方程式 $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$に代入すると

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## 未定係数法の拡張：関数の積の形の$r(x)$
$r(x) = k x^n e^{\alpha x}\cos(\omega x)$ の形である非斉次線形常微分方程式

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

を考えます。$r(x)$をこのように指数関数 $e^{\alpha x}$、$x$のべき乗 $x^m$、$\cos{\omega x}$ または $\sin{\omega x}$（ここでは$\cos$と仮定し、これにより一般性を失いません）、あるいはこれらの関数の和と積であるとすると（つまり、先の表の最初の列にある関数の和と積で表現できるとすると）、同じ表の2番目の列にある関数の和と積である方程式の解$y_p$が存在することを示します。

> 厳密な証明のために線形代数学を用いて記述した部分がありますが、そのような部分は*で示しています。該当部分を飛ばして残りの部分だけを読んでも、概略的な理解には問題ありません。
{: .prompt-tip }

### ベクトル空間 $V$ の定義*
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

である$r(x)$に対して、$r(x) \in V$であるベクトル空間$V$を次のように定義できます。

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### 指数関数、多項式関数、三角関数の導関数の形
先の表の最初の列で提示された基本関数の導関数の形は次のとおりです。
- 指数関数: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- 多項式関数: $\cfrac{d}{dx}x^m = mx^{m-1}$
- 三角関数: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

これらの関数を微分して得られる導関数もまた、<u>同じ種類の関数の和</u>で表現されます。

したがって、関数$f$と$g$が上記の関数またはそれらの和であるとき、$r(x) = f(x)g(x)$に対して積の微分法を適用すると

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

となり、ここで$f$、$f^{\prime}$、$f^{\prime\prime}$と$g$、$g^{\prime}$、$g^{\prime\prime}$はすべて指数関数、多項式関数、三角関数の和または定数倍の形で書くことができます。したがって、$r^{\prime}(x) = (fg)^{\prime}$、$r^{\prime\prime}(x) = (fg)^{\prime\prime}$も$r(x)$と同様に、これらの関数の和と積で表現できます。

### $V$の微分演算$D$、線形変換$L$に対する不変性*
つまり、$r(x)$自体だけでなく、$r^{\prime}(x)$、$r^{\prime\prime}(x)$も$x^k e^{\alpha x}\cos(\omega x)$形の項と$x^k e^{\alpha x}\sin(\omega x)$形の項の線形結合であるため

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

$r(x)$に限定せず、先に定義したベクトル空間$V$のすべての元に対して微分演算子$D$を導入してより一般的に表現すると、*ベクトル空間$V$は微分演算$D$に対して閉じている*と言えます。したがって、与えられた方程式の左辺$y^{\prime\prime} + ay^{\prime} + by$を$L[y]$と表記すると、*$V$は$L$に対して不変（invariant）です*。

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

$r(x) \in V$であり、$V$が$L$に対して不変であるため、$L[y_p] = r$を満たす$V$の別の元$y_p$が存在します。

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
したがって、すべての可能な積の形の項の和となるように、適切な$y_p$を未定係数$A_0, A_1, \dots, A_n$と$K$, $M$を用いて次のように選択すれば、基本規則 (a) と修正規則 (b) に従って、$y_p$（または$xy_p$, $x^2y_p$）とその導関数を与えられた方程式に代入することで未定係数を決定できます。このとき、$n$は$r(x)$の$x$に対する次数に応じて決定すればよいです。

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> もし与えられた入力$r(x)$が互いに異なる複数の$\alpha_i$、$\omega_j$の値を含む場合、各$\alpha_i$と$\omega_j$の値に対しても、可能なすべての$x^{k}e^{\alpha_i x}\cos(\omega_j x)$、$x^{k}e^{\alpha_i x}\sin(\omega_j x)$形の項を漏れなく含めるように$y_p$を選択する必要があります。  
> 未定係数法の利点は手軽さにあるため、仮設解（ansatz）が複雑になりすぎてこの利点が薄れる場合は、むしろ後で扱う定数変化法を適用する方が良いかもしれません。
{: .prompt-warning }

## 未定係数法の拡張：オイラー・コーシー方程式
[定数係数を持つ2階斉次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)だけでなく、[オイラー・コーシー方程式](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

に対しても未定係数法を活用することができます。

### 変数置換
[$x = e^t$と置換して定数係数を持つ2階斉次線形常微分方程式に変換](/posts/euler-cauchy-equation/#定数係数を持つ2階斉次線形常微分方程式への変換)すると

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

となり、オイラー・コーシー方程式を次のように$t$に関する定数係数斉次線形常微分方程式に変えることができることを以前に学びました。

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

ここで、式 ($\ref{eqn:substituted}$)に対して[先に見た未定係数法](#未定係数法)を同様に適用して$t$について解き、最後に$t = \ln x$であることを利用して$x$に関する解を求めればよいです。

### $r(x)$が$x$のべき乗、自然対数、またはこれらの関数の和と積である場合
特に入力$r(x)$が$x$のべき乗、自然対数、またはこれらの関数の和と積で構成される場合、次のオイラー・コーシー方程式用の選択規則に従って適切な$y_p$を直ちに選択することができます。

> **未定係数法における選択規則：オイラー・コーシー方程式用**  
> **(a) 基本規則（basic rule）**: 式 ($\ref{eqn:euler_cauchy}$)において、$r(x)$が表の最初の列にある関数のいずれかである場合、同じ行の$y_p$を選択し、$y_p$とその導関数を式 ($\ref{eqn:euler_cauchy}$)に代入することで未定係数を決定する。  
> **(b) 修正規則（modification rule）**: $y_p$として選択した項が、式 ($\ref{eqn:euler_cauchy}$)に対応する斉次常微分方程式 $x^2y^{\prime\prime} + axy^{\prime} + by = 0$の解となる場合、この項に$\ln{x}$（または、もしこの解が斉次常微分方程式の特性方程式の重解に該当する場合は$(\ln{x})^2$）を掛ける。  
> **(c) 重ね合わせの規則（sum rule）**: $r(x)$が表の最初の列にある関数の和である場合、2番目の列の対応する行にある関数の和を$y_p$として選択する。
>
> | $r(x)$の項 | $y_p(x)$の選択 |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

こうすることで、実用的に重要な形の入力$r(x)$に対して、[変数置換](#変数置換)で得られるものと同じ$y_p$を、より迅速かつ手軽に見つけることができます。先に見た[元の選択規則](#未定係数法)で、$x$の代わりに$\ln{x}$を代入すると、このオイラー・コーシー方程式用の選択規則を導出できます。
