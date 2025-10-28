---
title: "ベクトル空間、部分空間、そして行列"
description: "ベクトル空間と部分空間の定義を押さえ、行列空間や関数空間などの代表例を解説。とくに行列空間に焦点を当て、任意サイズで重要な部分空間を成す対称・反対称行列、上三角・下三角・対角行列を整理します。"
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **行列（matrix）**
>   - 行列 $A$ の $i$ 行 $j$ 列の成分を $A\_{ij}$ または $a\_{ij}$ と表す
>   - **対角成分（diagonal entry）**: $i=j$ の成分 $a\_{ij}$
>   - 成分 $a\_{i1}, a\_{i2}, \dots, a\_{in}$ をこの行列の $i$ 番目の**行（row）**という
>     - 行列の各行は $F^n$ のベクトルで表せる
>     - さらに、$F^n$ の行ベクトルは $1 \times n$ の別の行列として表せる
>   - 成分 $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ をこの行列の $j$ 番目の**列（column）**という
>     - 行列の各列は $F^m$ のベクトルで表せる
>     - さらに、$F^m$ の列ベクトルは $m \times 1$ の別の行列として表せる
>   - **零行列（zero matrix）**: すべての成分が $0$ の行列。$O$ と表す
>   - **正方行列（square matrix）**: 行数と列数が等しい行列
>   - 2 つの $m \times n$ 行列 $A, B$ について、すべての $1 \leq i \leq m$, $1 \leq j \leq n$ に対して $A\_{ij} = B\_{ij}$（すなわち対応する成分がすべて一致）なら、2 つの行列は**等しい**（$A=B$）と定義する
>   - **転置行列（transpose matrix）**: $m \times n$ 行列 $A$ に対し、$A$ の行と列を入れ替えた $n \times m$ 行列 $A^T$
>   - **対称行列（symmetric matrix）**: $A^T = A$ を満たす正方行列 $A$
>   - **反対称行列（skew-symmetric matrix）**: $B^T = -B$ を満たす正方行列 $B$
>   - **三角行列（triangular matrix）**
>     - **上三角行列（upper triangular matrix）**: 対角成分の下のすべての成分が $0$（すなわち $i>j \Rightarrow A\_{ij}=0$）の行列。通常 $U$ と表す
>     - **下三角行列（lower triangular matrix）**: 対角成分の上のすべての成分が $0$（すなわち $i<j \Rightarrow A\_{ij}=0$）の行列。通常 $L$ と表す
>   - **対角行列（diagonal matrix）**: 対角成分以外のすべての成分が $0$ の正方行列（すなわち $i \neq j \Rightarrow M\_{ij}=0$ の $n \times n$ 行列）。通常 $D$ と表す
> - 代表的なベクトル空間
>   - **$n$ 個の順序組 $F^n$**:
>     - 体 $F$ の成分からなるすべての $n$ 個の順序組の集合
>     - $F^n$ と表し、$F$-ベクトル空間である
>   - **行列空間（matrix space）**:
>     - 成分が体 $F$ の元であるすべての $m \times n$ 行列の集合
>     - $\mathcal{M}\_{m \times n}(F)$ と表し、ベクトル空間である
>   - **関数空間（function space）**:
>     - 体 $F$ の空でない集合 $S$ に対し、$S$ から $F$ へのすべての関数の集合
>     - $\mathcal{F}(S,F)$ と表し、ベクトル空間である
> - **部分空間（subspace）**
>   - $F$-ベクトル空間 $\mathbb{V}$ の部分集合 $\mathbb{W}$ が、$\mathbb{V}$ で定義した和とスカラー乗法を同一に備える $F$-ベクトル空間であるとき、$\mathbb{W}$ を $\mathbb{V}$ の**部分空間（subspace）**という
>   - あらゆるベクトル空間 $\mathbb{V}$ に対し、$\mathbb{V}$ 自身と $\\{0\\}$ は部分空間であり、とくに $\\{0\\}$ は**零部分空間（zero subspace）**という
>   - ベクトル空間のある部分集合が零ベクトルを元に持ち、[線形結合](/posts/vectors-and-linear-combinations/#ベクトルの線形結合)について閉じていれば（$\mathrm{span}(\mathbb{W})=\mathbb{W}$ なら）、その集合は部分空間である
{: .prompt-info }

## Prerequisites
- [ベクトルと線形結合](/posts/vectors-and-linear-combinations/)

## ベクトル空間

[ベクトルと線形結合](/posts/vectors-and-linear-combinations/#広い意味のベクトルベクトル空間の元)でも少し見たように、代数的構造としてのベクトルとベクトル空間の定義は次のとおりである。

> **定義**  
> 体 $F$ 上の**ベクトル空間（vector space）**または**線形空間（linear space）** $\mathbb{V}$ は、次の 8 条件を満たす 2 つの演算、**和**と**スカラー乗法**を持つ集合である。体 $F$ の元を**スカラー（scalar）**、ベクトル空間 $\mathbb{V}$ の元を**ベクトル（vector）**という。
>
> - **和（sum）**: $\mathbb{V}$ の 2 つの元 $\mathbf{x}, \mathbf{y}$ に対し、一意の元 $\mathbf{x} + \mathbf{y} \in \mathbb{V}$ を対応させる演算。このとき $\mathbf{x} + \mathbf{y}$ を $\mathbf{x}$ と $\mathbf{y}$ の**和**という。
> - **スカラー乗法（scalar multiplication）**: 体 $F$ の元 $a$ とベクトル空間 $\mathbb{V}$ の元 $\mathbf{x}$ ごとに一意の元 $a\mathbf{x} \in \mathbb{V}$ を対応させる演算。このとき $a\mathbf{x}$ を $\mathbf{x}$ の**スカラー倍（scalar multiple）**という。
>
> 1. すべての $\mathbf{x},\mathbf{y} \in \mathbb{V}$ に対して $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$（加法の交換法則）
> 2. すべての $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$ に対して $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$（加法の結合法則）
> 3. すべての $\mathbf{x} \in \mathbb{V}$ に対して $\mathbf{x} + \mathbf{0} = \mathbf{x}$ となる $\mathbf{0} \in \mathbb{V}$ が存在する（零ベクトル、加法に関する単位元）
> 4. 各 $\mathbf{x} \in \mathbb{V}$ について、$\mathbf{x}+\mathbf{y}=\mathbf{0}$ を満たす $\mathbf{y} \in \mathbb{V}$ が存在する（加法に関する逆元）
> 5. 各 $\mathbf{x} \in \mathbb{V}$ に対して $1\mathbf{x} = \mathbf{x}$（乗法に関する単位元）
> 6. すべての $a,b \in F$ とすべての $\mathbf{x} \in \mathbb{V}$ に対して $(ab)\mathbf{x} = a(b\mathbf{x})$（スカラー乗法の結合法則）
> 7. すべての $a \in F$ とすべての $\mathbf{x},\mathbf{y} \in \mathbb{V}$ に対して $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$（加法に関するスカラー乗法の分配法則 1）
> 8. すべての $a,b \in F$ とすべての $\mathbf{x},\mathbf{y} \in \mathbb{V}$ に対して $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$（加法に関するスカラー乗法の分配法則 2）
{: .prompt-info }

ベクトル空間は本来「$F$-ベクトル空間 $\mathbb{V}$」と表記すべきだが、ベクトル空間を扱う際、体は大きな争点ではないので混乱の恐れがなければ体 $F$ は省略し「ベクトル空間 $\mathbb{V}$」と書く。

### 行列空間

#### 行ベクトルと列ベクトル

体 $F$ の成分からなるすべての $n$ 個の順序組の集合を $F^n$ と表す。$u = (a_1, a_2, \dots, a_n) \in F^n$, $v = (b_1, b_2, \dots, b_n) \in F^n$ のとき、和とスカラー積を次のように定義すれば $F^n$ は $F$-ベクトル空間である。

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

$F^n$ のベクトルは、単独で書くときは通常**行ベクトル（row vector）** $(a_1, a_2, \dots, a_n)$ よりも **列ベクトル（column vector）**

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

で表す。

> ただし列ベクトル表記は紙幅を取りがちなので、[転置](#転置行列対称行列反対称行列)を用いて $(a_1, a_2, \dots, a_n)^T$ と表すこともある。
{: .prompt-tip }

#### 行列と行列空間

一方、$F$ の成分からなる $m \times n$ の**行列（matrix）**は次のような長方形の配列で、イタリック体の大文字（$A, B, C$ など）で表す。

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- 行列 $A$ の $i$ 行 $j$ 列の成分を $A\_{ij}$ または $a\_{ij}$ と表す。
- すべての $a\_{ij}$（$1 \leq i \leq m$, $1 \leq j \leq n$）は $F$ の元である。
- $i=j$ の成分 $a\_{ij}$ をこの行列の**対角成分（diagonal entry）**という。
- 成分 $a\_{i1}, a\_{i2}, \dots, a\_{in}$ をこの行列の $i$ 番目の**行（row）**という。行列の各行は $F^n$ のベクトルで表せ、さらに $F^n$ の行ベクトルは $1 \times n$ の別の行列で表せる。
- 成分 $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ をこの行列の $j$ 番目の**列（column）**という。行列の各列は $F^m$ のベクトルで表せ、さらに $F^m$ の列ベクトルは $m \times 1$ の別の行列で表せる。
- すべての成分が $0$ の $m \times n$ 行列を**零行列（zero matrix）**といい、$O$ と表す。
- 行数と列数が等しい行列を**正方行列（square matrix）**という。
- 2 つの $m \times n$ 行列 $A, B$ について、すべての $1 \leq i \leq m$, $1 \leq j \leq n$ に対し $A\_{ij} = B\_{ij}$ なら（すなわち対応する成分がすべて一致するなら）、2 つの行列は**等しい**（$A=B$）と定義する。

成分が体 $F$ の元であるすべての $m \times n$ 行列の集合を $\mathcal{M}\_{m \times n}(F)$ と表す。$\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F),\ c \in F$ のとき、和とスカラー乗法を次のように定義すれば $\mathcal{M}\_{m \times n}(F)$ はベクトル空間であり、これを**行列空間（matrix space）**という。

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{（ただし }1 \leq i \leq &m, 1 \leq j \leq n \text{）}
\end{align*} $$

これは $F^n$ と $F^m$ で定義した演算の自然な拡張である。

### 関数空間

体 $F$ の空でない集合 $S$ に対し、$\mathcal{F}(S,F)$ を $S$ から $F$ へのすべての関数の集合という。$\mathcal{F}(S,F)$ において、すべての $s \in S$ について $f(s) = g(s)$ なら 2 つの関数 $f, g$ は**等しい**（$f=g$）という。

$f,g \in \mathcal{F}(S,F),\ c \in F,\ s \in S$ のとき、和とスカラー乗法を次のように定義すれば $\mathcal{F}(S,F)$ はベクトル空間であり、これを**関数空間（function space）**という。

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## 部分空間

> **定義**  
> $F$-ベクトル空間 $\mathbb{V}$ の部分集合 $\mathbb{W}$ が、$\mathbb{V}$ で定義した和とスカラー乗法を同一に備える $F$-ベクトル空間であるとき、$\mathbb{W}$ を $\mathbb{V}$ の**部分空間（subspace）**という。
{: .prompt-info }

任意のベクトル空間 $\mathbb{V}$ に対し、$\mathbb{V}$ 自身と $\\{0\\}$ は部分空間であり、とくに $\{0\}$ は**零部分空間（zero subspace）**という。

ある部分集合が部分空間であるかどうかは、次の定理で確認できる。

> **定理 1**  
> ベクトル空間 $\mathbb{V}$ と部分集合 $\mathbb{W}$ について、$\mathbb{W}$ が $\mathbb{V}$ の部分空間であるための必要十分条件は、次の 3 条件を満たすことである。このとき演算は $\mathbb{V}$ で定義したものと同じである。
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> つまり、零ベクトルを元に持ち、[線形結合](/posts/vectors-and-linear-combinations/#ベクトルの線形結合)について閉じていれば（$\mathrm{span}(\mathbb{W})=\mathbb{W}$ であれば）部分空間である。
{: .prompt-info }

また、次の定理が成り立つ。

> **定理 2**  
> - ベクトル空間 $\mathbb{V}$ の任意の部分集合 $S$ の生成空間 $\mathrm{span}(S)$ は、$S$ を含む $\mathbb{V}$ の部分空間である。
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - $S$ を含む $\mathbb{V}$ の部分空間は、必ず $S$ の生成空間を含む。
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **定理 3**  
> ベクトル空間 $\mathbb{V}$ の部分空間について、それらの任意の共通部分（交わり）は同様に $\mathbb{V}$ の部分空間である。
{: .prompt-info }

### 転置行列、対称行列、反対称行列

$m \times n$ 行列 $A$ の**転置行列（transpose matrix）** $A^T$ は、$A$ の行と列を入れ替えた $n \times m$ 行列である。

$$ (A^T)_{ij} = A_{ji} $$

$$ \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}^T
= \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 
\end{pmatrix} $$

$A^T = A$ を満たす行列 $A$ を**対称行列（symmetric matrix）**、$B^T = -B$ を満たす行列 $B$ を**反対称行列（skew-symmetric matrix）**という。対称行列と反対称行列はいずれも正方行列でなければならない。

それぞれ $\mathcal{M}\_{n \times n}(F)$ のすべての対称行列、反対称行列を元とする 2 つの集合 $\mathbb{W}\_1, \mathbb{W}\_2$ は、$\mathcal{M}\_{n \times n}(F)$ の部分空間である。すなわち、$\mathbb{W}\_1, \mathbb{W}\_2$ は和とスカラー積について閉じている。

### 三角行列、対角行列

この 2 種類の行列もとくに重要である。

まず、次の 2 種類の行列をまとめて**三角行列（triangular matrix）**という。
- **上三角行列（upper triangular matrix）**: 対角成分の下のすべての成分が $0$ の行列（すなわち $i>j \Rightarrow A\_{ij}=0$ の行列）。通常 $U$ と表す
- **下三角行列（lower triangular matrix）**: 対角成分の上のすべての成分が $0$ の行列（すなわち $i<j \Rightarrow A\_{ij}=0$ の行列）。通常 $L$ と表す

対角成分以外のすべての成分が $0$ の正方行列、すなわち $i \neq j \Rightarrow M\_{ij}=0$ の $n \times n$ 行列を**対角行列（diagonal matrix）**といい、通常 $D$ と表す。対角行列は上三角行列であると同時に下三角行列でもある。

上三角行列の集合、下三角行列の集合、対角行列の集合はいずれも $\mathcal{M}\_{m \times n}(F)$ の部分空間である。
