---
title: ロンスキアン(Wronskian)、解の存在と一意性
description: 連続な任意の変数係数を持つ2階同次線形常微分方程式について、初期値問題の解の存在性と一意性の定理、ロンスキアン(Wronskian)を用いた解の線形従属/線形独立の判別法を学ぶ。また、これを用いてこのような形の方程式は常に一般解を持ち、この一般解は方程式のすべての解を含むことを示す。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> 区間 $I$で連続な任意の変数係数 $p$と $q$を持つ2階同次線形常微分方程式
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> と初期条件
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> について、次の4つの定理が成り立つ。
> 1. **初期値問題の解の存在性と一意性の定理**: 与えられた方程式および初期条件で構成される初期値問題は区間 $I$で唯一の解 $y(x)$を持つ。
> 2. **ロンスキアン(Wronskian)を用いた解の線形従属/線形独立の判別**: 方程式の二つの解 $y_1$と $y_2$について、区間 $I$内に**ロンスキアン(Wronskian)** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$の値が $0$となる $x_0$が存在するならば、二つの解は線形従属である。また、区間 $I$内に $W\neq 0$となる $x_1$が存在するならば、二つの解は線形独立である。
> 3. **一般解の存在**: 与えられた方程式は区間 $I$で一般解を持つ。
> 4. **特異解の非存在**: この一般解は方程式のすべての解を含む（つまり、特異解は存在しない）。
{: .prompt-info }

## Prerequisites
- [1階線形常微分方程式の解法](/posts/Solution-of-First-Order-Linear-ODE/)
- [2階同次線形常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [定数係数を持つ2階同次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [オイラー・コーシー方程式](/posts/euler-cauchy-equation/)
- 逆行列と特異行列、行列式

## 連続な任意の変数係数を持つ同次線形常微分方程式
前回[定数係数を持つ2階同次線形常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)と[オイラー・コーシー方程式](/posts/euler-cauchy-equation/)の一般解を学びました。
この記事では議論をより一般的な場合に拡張し、連続な任意の**変数係数(variable coefficient)** $p$と $q$を持つ2階同次線形常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

の一般解の存在性と形態を調べます。さらに、常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)と次の二つの初期条件

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

で構成される[初期値問題](/posts/homogeneous-linear-odes-of-second-order/#初期値問題と初期条件)の一意性も調べます。

結論から先に言えば、連続な係数を持つ<u>線形</u>常微分方程式は*特異解(singular solution)*（一般解から得られない解）を持たないということがここで扱う内容の核心です。

## 初期値問題の解の存在性と一意性の定理
> **初期値問題の解の存在性と一意性の定理(Existence and Uniqueness Theorem for Initial Value Problems)**  
> もし $p(x)$と $q(x)$がある開区間 $I$で連続関数であり、$x_0$が区間 $I$内にあるならば、式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)と ($\ref{eqn:initial_conditions}$)で構成される初期値問題は区間 $I$で唯一の解 $y(x)$を持つ。
{: .prompt-info }

存在性に関する証明はここでは扱わず、一意性の証明のみを見ていきます。通常、一意性を証明する方が存在性を証明するよりも簡単です。  
証明に興味がない場合は、この部分をスキップして[解の線形従属と線形独立](#解の線形従属と線形独立)に進んでも構いません。

### 一意性の証明
常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)と初期条件 ($\ref{eqn:initial_conditions}$)で構成される初期値問題が区間 $I$で二つの解 $y_1(x)$と $y_2(x)$を持つと仮定します。これら二つの解の差

$$ y(x) = y_1(x) - y_2(x) $$

が区間 $I$で恒等的に $0$となることを示せれば、区間 $I$で $y_1 \equiv y_2$ということになり、解の一意性を意味します。

方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)が同次線形常微分方程式であるため、$y_1$と $y_2$の線形結合である $y$は $I$で方程式の解となります。$y_1$と $y_2$が同じ初期条件 ($\ref{eqn:initial_conditions}$)を満たすので、$y$は条件

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_1(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

を満たします。ここで関数

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

とその導関数

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

を考えます。常微分方程式から

$$ y^{\prime\prime} = -py^{\prime} - qy $$

を得て、これを $z^{\prime}$に関する式に代入すると

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

を得ます。ここで $y$と $y^{\prime}$が実数であるため

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

となります。これと $z$の定義から二つの不等式

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

を得ることができます。これら二つの不等式から $\|2yy^{\prime}\|\leq z$であることがわかり、式 ($\ref{eqn:z_prime}$)の最後の項については次の不等式が成り立ちます。

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

この結果と $-p \leq \|p\|$を用いて、式 ($\ref{eqn:z_prime}$)の項 $2yy^{\prime}$に式 ($\ref{eqn:inequalities}$a)を適用すると

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

となります。${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$であるため、これから

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

を得て、括弧内の関数を $h = 1 + 2\|p\| + \|q\|$とすると

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

となります。同様の方法で、式 ($\ref{eqn:z_prime}$)と ($\ref{eqn:inequalities}$)から

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

を得ます。これら二つの不等式 ($\ref{eqn:inequality_6a}$)、($\ref{eqn:inequality_6b}$)は次の不等式

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

と同等であり、二つの式の左辺に対する[積分因子](/posts/Solution-of-First-Order-Linear-ODE/#非同次線形常微分方程式)は

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{と} \qquad F_2 = e^{\int h(x)\ dx} $$

です。$h$が連続であるため不定積分 $\int h(x)\ dx$は存在し、$F_1$と $F_2$が正であるため式 ($\ref{eqn:inequalities_7}$)から

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

を得ます。これは区間 $I$で $F_1 z$が増加せず、$F_2 z$が減少しないことを意味します。式 ($\ref{eqn:initial_conditions_*}$)により $z(x_0) = 0$であるため、

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

となります。最後に不等式の両辺を正の値 $F_1$と $F_2$で割ると、次のように解の一意性を示すことができます。

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## 解の線形従属と線形独立
[2階同次線形常微分方程式](/posts/homogeneous-linear-odes-of-second-order/#基底と一般解)で扱った内容を少し思い出しましょう。開区間 $I$での一般解は $I$での**基底(basis)** $y_1$、$y_2$、つまり線形独立な解のペアから作られます。ここで $y_1$と $y_2$が区間 $I$で**線形独立(linearly independent)**であるとは、区間内のすべての $x$について次を満たすことを意味します。

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{かつ }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

もし上記を満たさず、少なくとも一つの $0$でない $k_1$、$k_2$について $k_1y_1(x) + k_2y_2(x) = 0$が成り立つ場合、$y_1$と $y_2$は区間 $I$で**線形従属(linearly dependent)**です。この場合、区間 $I$のすべての $x$について

$$ \text{(a) } y_1 = ky_2 \quad \text{または} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

となり、$y_1$と $y_2$は比例します。

ここで次の解の線形独立/線形従属の判別法を見ていきましょう。

> **ロンスキアン(Wronskian)を用いた解の線形従属/線形独立の判別**  
> **i.** 常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)が開区間 $I$で連続な係数 $p(x)$と $q(x)$を持つならば、区間 $I$で方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)の二つの解 $y_1$と $y_2$が線形従属となるための必要十分条件は、これらの解の*ロンスキー行列式(Wronski determinant)*、略して**ロンスキアン(Wronskian)**と呼ばれる次の行列式
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> が区間 $I$内のある $x_0$で $0$となることである。
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{と } y_2 \text{は線形従属} $$
>
> **ii.** 区間 $I$内の一点 $x=x_0$で $W=0$ならば、区間 $I$内のすべての $x$で $W=0$である。
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> つまり、$W\neq 0$となる $x_1$が区間 $I$に存在するならば、その区間 $I$では $y_1$、$y_2$は線形独立である。
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{と } y_2 \text{は線形独立}
> \end{align*}$$
>
{: .prompt-info }

> ロンスキアンはポーランドの数学者ユゼフ・マリア・ホエネ＝ヴロンスキ(Józef Maria Hoene-Wroński)によって初めて導入され、彼の死後の12024 HE（11882年）にスコットランドの数学者トーマス・ミュア(Sir Thomas Muir)によって現在の名前が付けられました。
{: .prompt-tip }

### 証明
#### i. (a)
区間 $I$で $y_1$と $y_2$が線形従属であるとします。すると区間 $I$で式 ($\ref{eqn:linearly_dependent}$a)または($\ref{eqn:linearly_dependent}$b)が成り立ちます。もし式 ($\ref{eqn:linearly_dependent}$a)が成り立つならば

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

となり、同様に式 ($\ref{eqn:linearly_dependent}$b)が成り立つ場合も

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

となるため、<u>区間 $I$内のすべての $x$について</u>ロンスキアン $W(y_1, y_2)=0$であることが確認できます。

#### i. (b)
逆に、ある $x = x_0$で $W(y_1, y_2)=0$である場合、区間 $I$で $y_1$と $y_2$が線形従属となることを示します。未知数 $k_1$、$k_2$に関する線形連立方程式

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

を考えます。これは次のようなベクトル方程式の形で表現できます。

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

このベクトル方程式の係数行列は

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

であり、この行列の行列式はすなわち $W(y_1(x_0), y_2(x_0))$です。$\det(A) = W=0$であるため、$A$は**逆行列(inverse matrix)**が存在しない**特異行列(singular matrix)**であり、したがって連立方程式 ($\ref{eqn:linear_system}$)は $k_1$と $k_2$の少なくとも一方は $0$でないゼロベクトル $(0,0)$以外の解 $(c_1, c_2)$を持ちます。ここで関数

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

を導入します。方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)が同次線形であるため、[重ね合わせの原理](/posts/homogeneous-linear-odes-of-second-order/#重ね合わせの原理)によりこの関数は区間 $I$で ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)の解となります。式 ($\ref{eqn:linear_system}$)からこの解は初期条件 $y(x_0)=0$、$y^{\prime}(x_0)=0$を満たすことがわかります。

一方、同じ初期条件 $y^\*(x_0)=0$、${y^\*}^{\prime}(x_0)=0$を満たす自明解 $y^* \equiv 0$が存在します。方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)の係数 $p$と $q$が連続であるため、[初期値問題の解の存在性と一意性の定理](#初期値問題の解の存在性と一意性の定理)により解の一意性が保証され、したがって $y \equiv y^\*$です。つまり、区間 $I$で

$$ c_1y_1 + c_2y_2 \equiv 0 $$

となります。$c_1$と $c_2$の少なくとも一方は $0$でないため ($\ref{eqn:linearly_independent}$)を満たさず、これは区間 $I$で $y_1$、$y_2$が線形従属であることを意味します。

#### ii.
もし区間 $I$内のある一点 $x_0$で $W(x_0)=0$ならば、[i.(b)](#i-b)により区間 $I$で $y_1$、$y_2$は線形従属であり、そうすると[i.(a)](#i-a)により $W\equiv 0$です。したがって $W(x_1)\neq 0$となる $x_1$が区間 $I$内に一つでも存在するならば、$y_1$と $y_2$は線形独立です。$\blacksquare$

## 一般解はすべての解を含む
### 一般解の存在
> もし $p(x)$と $q(x)$が開区間 $I$で連続ならば、方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)は区間 $I$で一般解を持つ。
{: .prompt-info }

#### 証明
[初期値問題の解の存在性と一意性の定理](#初期値問題の解の存在性と一意性の定理)により、常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)は区間 $I$で初期条件

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

を満たす解 $y_1(x)$と区間 $I$で初期条件

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

を満たす解 $y_2(x)$を持ちます。これら二つの解のロンスキアンは $x=x_0$で0でない値

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

を持つため、[ロンスキアン(Wronskian)を用いた解の線形従属/線形独立の判別](#解の線形従属と線形独立)により区間 $I$で $y_1$と $y_2$は線形独立です。したがって、これら二つの解は区間 $I$で方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)の解の基底を形成し、任意の定数 $c_1$、$c_2$を持つ一般解 $y = c_1y_1 + c_2y_2$が区間 $I$で必ず存在します。$\blacksquare$

### 特異解の非存在
> 常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)がある開区間 $I$で連続な係数 $p(x)$と $q(x)$を持つならば、区間 $I$での方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)のすべての解 $y=Y(x)$は
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> の形であり、ここで $y_1$、$y_2$は区間 $I$での方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)の解の基底であり、$C_1$、$C_2$は適当な定数である。  
> つまり、方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)は一般解から得られない解である**特異解(singular solution)**を持たない。
{: .prompt-info }

#### 証明
$y=Y(x)$を区間 $I$での方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)のある解とします。[一般解の存在定理](#一般解の存在)により常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)は区間 $I$で一般解

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

を持ちます。ここで任意の $Y(x)$について区間 $I$で $y(x)=Y(x)$となるような定数 $c_1$、$c_2$が存在することを示す必要があります。区間 $I$で任意の $x_0$を選んだとき、$y(x_0)=Y(x_0)$かつ $y^{\prime}(x_0)=Y^{\prime}(x_0)$となるような $c_1$、$c_2$の値を見つけられることをまず示しましょう。式 ($\ref{eqn:general_solution}$)から

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

が得られます。$y_1$と $y_2$が基底であるため、係数行列の行列式である $W(y_1(x_0), y_2(x_0))\neq 0$であり、したがって方程式 ($\ref{eqn:vector_equation_2}$)は $c_1$と $c_2$について解くことができます。その解を $(c_1, c_2) = (C_1, C_2)$とします。これを式 ($\ref{eqn:general_solution}$)に代入すると次の特殊解が得られます。

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

$C_1$、$C_2$が方程式 ($\ref{eqn:vector_equation_2}$)の解であるため、

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

となります。[初期値問題の解の存在性と一意性の定理](#初期値問題の解の存在性と一意性の定理)の一意性により、区間 $I$内のすべての $x$について $y^\* \equiv Y$です。$\blacksquare$
