---
title: "線形変換、零空間、像"
description: "線形変換の定義を概観し、関連する2つの重要な部分空間である零空間（null space）と像（image）、それらの次元（ヌルティとランク）、次元定理や単射・全射との同値条件、基底との関係まで解説します。"
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [ベクトルと線形結合](/posts/vectors-and-linear-combinations/)
- [ベクトル空間、部分空間、そして行列](/posts/vector-spaces-subspaces-and-matrices/)
- [線形従属と線形独立、基底と次元](posts/linear-dependence-and-independence-basis-and-dimension/)
- 単射、全射

## 線形変換

ベクトル空間の構造を保存する特別な関数を**線形変換（linear transformation）**といい、これは純粋数学、応用数学、社会科学、自然科学、そして工学を通じて非常に頻出する重要な概念である。

> **定義**  
> $\mathbb{V}$ と $\mathbb{W}$ が $F$-ベクトル空間とする。すべての $\mathbf{x}, \mathbf{y} \in \mathbb{V},\ c \in F$ に対して次の 2 条件を満たす関数 $T: \mathbb{V} \to \mathbb{W}$ を、$\mathbb{V}$ から $\mathbb{W}$ への**線形変換（linear transformation）**という。
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

$T$ が線形変換であることを簡潔に「$T$ は**線形（linear）**である」ともいう。線形変換 $T: \mathbb{V} \to \mathbb{W}$ は次の 4 性質を満たす。

> 1. $T$ が線形 $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ が線形 $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ が線形 $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ が線形 $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> ある関数が線形であることを示す際は、通常 2 番目の性質を用いると便利である。
{: .prompt-tip }

> 線形代数は幾何でも広く多様に使える。その理由は、多くの重要な幾何変換が線形だからである。とくに主要な 3 つの幾何変換である**回転**、**反射**、**射影**は線形変換に当たる。
{: .prompt-tip }

次の 2 種類の線形変換はとくに頻出である。

> **恒等変換と零変換**  
> $F$-ベクトル空間 $\mathbb{V}, \mathbb{W}$ について
> - **恒等変換（identity transformation）**: すべての $\mathbf{x} \in \mathbb{V}$ に対し $I\_\mathbb{V}(\mathbf{x}) = \mathbf{x}$ と定義される関数 $I\_\mathbb{V}: \mathbb{V} \to \mathbb{V}$
> - **零変換（zero transformation）**: すべての $\mathbf{x} \in \mathbb{V}$ に対し $T\_0(\mathbf{x}) = \mathbf{0}$ と定義される関数 $T\_0: \mathbb{V} \to \mathbb{W}$
{: .prompt-info }

このほかにも多様な概念が線形変換に該当する。

> **線形変換の例**  
> - 回転
> - 反射
> - 射影
> - [転置](/posts/vector-spaces-subspaces-and-matrices/#転置行列対称行列反対称行列)
> - 微分可能な関数の微分
> - 連続関数の積分
{: .prompt-tip }

## 零空間と像

### 零空間と像の定義

> **定義**  
> ベクトル空間 $\mathbb{V}, \mathbb{W}$ と線形変換 $T: \mathbb{V} \to \mathbb{W}$ に対して
> - **零空間（null space）**または**核（kernel）**: $T(\mathbf{x}) = \mathbf{0}$ を満たす $\mathbf{x} \in \mathbb{V}$ を元とする集合。$\mathrm{N}(T)$ と表記
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **値域（range）**または**像（image）**: $T$ の値を元とする $\mathbb{W}$ の部分集合。$\mathrm{R}(T)$ と表記
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **例** ベクトル空間 $\mathbb{V}, \mathbb{W}$ と恒等変換 $I: \mathbb{V} \to \mathbb{V}$、零変換 $T\_0: \mathbb{V} \to \mathbb{W}$ について次が成り立つ。
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T\_0) = \mathbb{V}$
> - $\mathrm{R}(T\_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

今後繰り返し重要になるが、線形変換の零空間と像はベクトル空間の[部分空間](/posts/vector-spaces-subspaces-and-matrices/#部分空間)である。

> **定理 1**  
> ベクトル空間 $\mathbb{V}, \mathbb{W}$ と線形変換 $T: \mathbb{V} \to \mathbb{W}$ に対して、$\mathrm{N}(T), \mathrm{R}(T)$ はそれぞれ $\mathbb{V}, \mathbb{W}$ の部分空間である。
>
> **証明**  
> $\mathbb{V}, \mathbb{W}$ の零ベクトルをそれぞれ $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$ と表す。
>
> $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$ なので $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$ であり、また $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T),\ c \in F$ に対し次が成り立つ。
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}_\mathbb{V} \in \mathrm{N}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{N}(T),\ c\mathbf{x} \in \mathrm{N}(T)$ なので $\mathrm{N}(T)$ は $\mathbb{V}$ の部分空間である](/posts/vector-spaces-subspaces-and-matrices/#部分空間)。
>
> 同様に、$T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$ なので $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$ であり、$\forall \mathbf{x}, \mathbf{y} \in \mathrm{R}(T),\ c \in F \ (\exists \mathbf{v}, \mathbf{w} \in \mathbb{V} \ (T(\mathbf{v}) = \mathbf{x}\ \wedge \ T(\mathbf{w}) = \mathbf{y}))$ より
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}_\mathbb{W} \in \mathrm{R}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{R}(T),\ c\mathbf{x} \in \mathrm{R}(T)$ なので $\mathrm{R}(T)$ は $\mathbb{W}$ の部分空間である](/posts/vector-spaces-subspaces-and-matrices/#部分空間)。$\blacksquare$
{: .prompt-info }

一方、ベクトル空間 $\mathbb{V}, \mathbb{W}$ と線形変換 $T: \mathbb{V} \to \mathbb{W}$ に対し、$\mathbb{V}$ の[基底](/posts/linear-dependence-and-independence-basis-and-dimension/#基底) $\beta = \\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_n \\}$ が分かっているとき、像 $\mathrm{R}(T)$ の[生成集合](/posts/vectors-and-linear-combinations/#生成)を次のように求められる。

> **定理 2**  
> ベクトル空間 $\mathbb{V}, \mathbb{W}$ と線形変換 $T: \mathbb{V} \to \mathbb{W}$、$\mathbb{V}$ の[基底](/posts/linear-dependence-and-independence-basis-and-dimension/#基底) $\beta = \\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_n \\}$ に対し次が成り立つ。
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **証明**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> $\mathrm{R}(T)$ は部分空間なので、[ベクトル空間、部分空間、そして行列](/posts/vector-spaces-subspaces-and-matrices/#部分空間)の**定理 2**により
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> また、
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> $\beta$ は $\mathbb{V}$ の基底なので
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(ただし } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> $T$ は線形なので
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ かつ $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ なので、$\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$。$\blacksquare$
{: .prompt-info }

この定理は基底 $\beta$ が無限集合の場合にも成り立つ。

### 次元定理

零空間と像は非常に重要な部分空間なので、[次元](/posts/linear-dependence-and-independence-basis-and-dimension/#次元)にも特別な名称を与える。

> ベクトル空間 $\mathbb{V}, \mathbb{W}$ と線形変換 $T: \mathbb{V} \to \mathbb{W}$ に対し、$\mathrm{N}(T), \mathrm{R}(T)$ が有限次元とする。
> - **零空間の次元（nullity）**: $\mathrm{N}(T)$ の次元。$\mathrm{nullity}(T)$ と表記
> - **階数（rank）**: $\mathrm{R}(T)$ の次元。$\mathrm{rank}(T)$ と表記
{: .prompt-info }

線形変換では零空間の次元が大きくなるほど階数は小さくなり、逆に階数が大きくなるほど零空間の次元は小さくなる。

> **定理 3: 次元定理（dimension theorem）**  
> ベクトル空間 $\mathbb{V}, \mathbb{W}$ と線形変換 $T: \mathbb{V}\to \mathbb{W}$ に対して、$\mathbb{V}$ が有限次元なら次が成り立つ。
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### 証明

$\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$ とし、$\mathrm{N}(T)$ の基底を $\\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_k \\}$ とする。

[「線形従属と線形独立、基底と次元」の**系 6-1**](/posts/linear-dependence-and-independence-basis-and-dimension/#部分空間の次元)により、$\\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_k \\}$ を拡張して $\mathbb{V}$ の基底 $\beta = \\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_n \\}$ を得ることができる。

いま、$S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ が $\mathrm{R}(T)$ の基底であることを示す。まず $1 \leq i \leq k$ では $T(\mathbf{v}\_i) = 0$ なので、[**定理 2**](#零空間と像の定義) により

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

すなわち $S$ は $\mathrm{R}(T)$ の生成集合である。ここで[**交換定理の系 5-2**](/posts/linear-dependence-and-independence-basis-and-dimension/#次元) により、$S$ が線形独立であることを示せば $S$ が $\mathrm{R}(T)$ の基底であることが分かる。

$\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$（ただし $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$）とすると、$T$ が線形なので

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

したがって、

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

$\beta$ は $\mathbb{V}$ の基底であるから、$\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ の唯一の解は

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

であり、これより

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

すなわち $S$ は線形独立であり、$\mathrm{R}(T)$ の基底である。

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### 線形変換と単射・全射

線形変換において単射（injection）と全射（surjection）は階数や零空間の次元と密接に関係する。

> **定理 4**  
> ベクトル空間 $\mathbb{V}, \mathbb{W}$ と線形変換 $T: \mathbb{V} \to \mathbb{W}$ に対して
>
> $$ T\text{ は単射である} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **定理 5**  
> 有限次元ベクトル空間 $\mathbb{V}, \mathbb{W}$ の次元が等しいとき、線形変換 $T: \mathbb{V} \to \mathbb{W}$ について次の 4 命題は同値である。
> 1. $T$ は単射である。
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ は全射である。
{: .prompt-info }

[次元定理](#次元定理)と[線形変換の性質 1, 3](#線形変換)、そして[「線形従属と線形独立、基底と次元」の**定理 6**](/posts/linear-dependence-and-independence-basis-and-dimension/#部分空間の次元)を用いて、**定理 4** と **定理 5** を証明できる。

これら 2 つの定理は、与えられた線形変換が単射または全射かどうかを判定する際に有用である。

> 無限次元ベクトル空間 $\mathbb{V}$ と線形変換 $T: \mathbb{V} \to \mathbb{V}$ については、単射と全射は同値ではない。
{: .prompt-warning }

また、ある線形変換が単射であれば、場合によっては与えられたベクトル空間の部分集合が線形独立かどうかを判定する際に、次の定理が有用である。

> **定理 6**  
> ベクトル空間 $\mathbb{V}, \mathbb{W}$ と単射な線形変換 $T: \mathbb{V} \to \mathbb{W}$、および $\mathbb{V}$ の部分集合 $S$ に対して次が成り立つ。
>
> $$ S\text{ が線形独立} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \}\text{ が線形独立}. $$
>
{: .prompt-info }

## 線形変換と基底

線形変換の重要な特徴は、基底に対してどのように作用するかで線形変換が決まる、という点にある。

> **定理 7**  
> $F$-ベクトル空間 $\mathbb{V}, \mathbb{W}$ と $\mathbb{V}$ の基底 $\\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_n \\}$、およびベクトル $\mathbf{w}\_1, \mathbf{w}\_2, \dots, \mathbf{w}\_n \in \mathbb{W}$ に対して、次の条件を満たす線形変換 $T: \mathbb{V} \to \mathbb{W}$ が一意に存在する。
>
> $$ i = 1, 2, \dots, n \text{ に対して } T(\mathbf{v}_i) = \mathbf{w}_i $$
>
> **証明**  
> $\mathbf{x} \in \mathbb{V}$ に対して次の線形結合表現は一意である。
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ (}a_1, a_2, \dots, a_n \in F \text{)} $$
>
> 線形変換 $T: \mathbb{V} \to \mathbb{W}$ を
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> とおく。
>
> i) $i = 1, 2, \dots, n$ に対して $T(\mathbf{v}_i) = \mathbf{w}_i$。
>
> ii)
>
> もう一つの線形変換 $U: \mathbb{V} \to \mathbb{W}$ が $i = 1, 2, \dots, n$ に対して $U(\mathbf{v}\_i) = \mathbf{w}\_i$ を満たすと仮定すると、$\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$ に対して
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i) $$
>
> $$ \therefore U = T. $$
>
> i), ii) により、$i = 1, 2, \dots, n$ に対して $T(\mathbf{v}\_i) = \mathbf{w}\_i$ となる線形変換は
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> の形で一意である。$\blacksquare$
>
> **系 7-1**  
> 2 つのベクトル空間 $\mathbb{V}, \mathbb{W}$ に対し、$\mathbb{V}$ が有限集合の基底 $\\{\mathbf{v}\_1, \mathbf{v}\_2, \dots, \mathbf{v}\_n \\}$ をもつとする。2 つの線形変換 $U, T: \mathbb{V} \to \mathbf{W}$ が $i = 1, 2, \dots, n$ について $U(\mathbf{v}\_i) = T(\mathbf{v}\_i)$ を満たせば $U = T$ である。  
> すなわち、<u>基底での値が等しければ同じ線形変換である。</u>
{: .prompt-info }
