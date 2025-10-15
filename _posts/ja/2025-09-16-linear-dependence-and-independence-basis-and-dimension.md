---
title: "線形従属と線形独立、基底と次元"
description: "線形従属と線形独立、さらにベクトル空間の基底と次元の定義・性質をまとめて解説します。"
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [ベクトルと線形結合](/posts/vectors-and-linear-combinations/)
- [ベクトル空間、部分空間、そして行列](/posts/vector-spaces-subspaces-and-matrices/)

## 線形従属と線形独立

ある[ベクトル空間](/posts/vector-spaces-subspaces-and-matrices/#ベクトル空間) $\mathbb{V}$ と[部分空間](/posts/vector-spaces-subspaces-and-matrices/#部分空間) $\mathbb{W}$ について、$\mathbb{W}$ を[生成](/posts/vectors-and-linear-combinations/#線形結合-cmathbfv--dmathbfw)する可能な限り小さい有限部分集合 $S$ を見つけたいとしよう。

集合 $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ に対し $\mathrm{span}(S) = \mathbb{W}$ であるとき、$\mathbb{W}$ を生成する $S$ の真部分集合が存在しないかどうかを判定するにはどうすればよいだろうか。これは、$S$ から取り出したあるベクトルが他のベクトルの[線形結合](/posts/vectors-and-linear-combinations/#ベクトルの線形結合)で表せるかどうかを判定する問題に等しい。たとえば、$\mathbf{u}_4$ を残り 3 本のベクトルの線形結合で表すための必要十分条件は、次の条件を満たすスカラー $a_1, a_2, a_3$ が存在することである。

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

しかし $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ のそれぞれについて毎回このように連立一次方程式を立てて解の存在を確かめるのは煩雑なので、式を少し変形してみよう。

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

もし $S$ のあるベクトルが他のベクトルの線形結合であれば、上のように零ベクトルを $S$ の線形結合で表すとき、係数 $a_1, a_2, a_3, a_4$ のうち少なくとも 1 つが $0$ ではない表し方が存在する。この命題の逆もまた成り立ち、係数 $a_1, a_2, a_3, a_4$ のうち少なくとも 1 つが $0$ でないまま零ベクトルを $S$ の元ベクトルの線形結合として表す方法が存在するなら、$S$ のあるベクトルは他のベクトルの線形結合である。

これを一般化して、次のように**線形従属**と**線形独立**を定義する。

> **定義**  
> ベクトル空間 $\mathbb{V}$ の部分集合 $S$ について、$a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$ を満たす有限個の互いに異なるベクトル $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ と、少なくとも 1 つが 0 でないスカラー $a_1, a_2, \dots, a_n$ が存在すれば、集合 $S$ およびそのベクトルは**線形従属（linearly dependent）**であるという。そうでない場合は**線形独立（linearly independent）**という。
{: .prompt-info }

任意のベクトル $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ に対し $a_1 = a_2 = \cdots = a_n = 0$ なら $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$ であり、これを**零ベクトルの自明な表現（trivial representation of $\mathbf{0}$）**という。

線形独立な集合に関して、次の 3 つの命題はすべてのベクトル空間で常に真である。とくに**命題 3**は前述のとおり、ある有限集合が線形独立かどうかを判定する際に非常に有用である。

> - **命題 1**: 空集合は線形独立である。ある集合が線形従属であるためには空集合であってはならない。
> - **命題 2**: 0 でないベクトル 1 本からなる集合は線形独立である。
> - **命題 3**: ある集合が線形独立であるための必要十分条件は、$\mathbf{0}$ をその集合に関する線形結合で表す方法が自明な表現しかないことである。
{: .prompt-info }

また、次の定理も重要である。

> **定理 1**  
> $\mathbb{V}$ をベクトル空間とし、$S_1 \subseteq S_2 \subseteq \mathbb{V}$ とする。$S_1$ が線形従属なら $S_2$ も線形従属である。
>
> **系 1-1**  
> $\mathbb{V}$ をベクトル空間とし、$S_1 \subseteq S_2 \subseteq \mathbb{V}$ とする。$S_2$ が線形独立なら $S_1$ も線形独立である。
{: .prompt-info }

> **定理 2**  
> ベクトル空間 $\mathbb{V}$ と線形独立な部分集合 $S$ を考える。$S$ に含まれないベクトル $\mathbf{v} \in \mathbb{V}$ に対し、$S \cup \\{\mathbf{v}\\}$ が線形従属であるための必要十分条件は $\mathbf{v} \in \mathrm{span}(S)$ である。
>
> 言い換えると、**$S$ のどの真部分集合も $S$ と同じ空間を生成できないなら $S$ は線形独立である。**
{: .prompt-info }

## 基底と次元

### 基底

[線形独立](#線形従属と線形独立)な $\mathbb{W}$ の生成集合 $S$ には特別な性質がある。すなわち、$\mathbb{W}$ に属するすべてのベクトルは必ず $S$ の線形結合で表せ、その表現は一意である（**定理 3**）。したがって、あるベクトル空間に対する線形独立な生成集合を特に次のように**基底（basis）**と定義する。

> **基底の定義**  
> ベクトル空間 $\mathbb{V}$ と部分集合 $\beta$ に対し、$\beta$ が線形独立でかつ $\mathbb{V}$ を生成するなら、$\beta$ を $\mathbb{V}$ の**基底（basis）**という。このとき、$\beta$ のベクトルは $\mathbb{V}$ の基底を成すという。
{: .prompt-info }

> $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ であり、$\emptyset$ は線形独立である。したがって $\emptyset$ は点空間の基底である。
{: .prompt-tip }

とくに、$F^n$ に対する次の特別な基底を $F^n$ の**標準基底（standard basis）**という。

> **標準基底の定義**  
> ベクトル空間 $F^n$ について次のベクトルを考える。
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> このとき、集合 $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ は $F^n$ の基底であり、これを $F^n$ の**標準基底（standard basis）**という。
{: .prompt-info }

> **定理 3**  
> ベクトル空間 $\mathbb{V}$ と互いに異なる $n$ 個のベクトル $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$ に対し、集合 $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ が $\mathbb{V}$ の基底であるための必要十分条件は「任意のベクトル $\mathbf{v} \in \mathbb{V}$ を $\beta$ に属するベクトルの線形結合で表せ、しかもその表現が一意であること」である。すなわち、一意なスカラーの $n$ 順序組 $(a_1, a_2, \dots, a_n)$ に対し、ベクトル $\mathbf{v}$ は次を満たす。
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

**定理 3**によれば、互いに異なる $n$ 個のベクトル $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ がベクトル空間 $\mathbb{V}$ の基底を成す場合、そのベクトル空間の中ではベクトル $\mathbf{v}$ が与えられると、それに対応するスカラーの $n$ 順序組 $(a_1, a_2, \dots, a_n)$ が定まり、逆にスカラーの $n$ 順序組が与えられると、それに対応するベクトル $\mathbf{v}$ を得ることができる。後で**可逆性**と**同型写像**について学ぶ際に改めて整理するが、この場合ベクトル空間 $\mathbb{V}$ と $F^n$ は<u>本質的に同じ</u>である。

> **定理 4**  
> 有限集合 $S$ について $\mathrm{span}(S) = \mathbb{V}$ なら、$S$ の部分集合の中に $\mathbb{V}$ の基底が存在する。すなわち、この場合 $\mathbb{V}$ の基底は有限集合である。
{: .prompt-info }

> 多くのベクトル空間が**定理 4**に当てはまるが、必ずしもそうとは限らない。<u>基底は有限集合でない場合もある</u>。
{: .prompt-tip }

### 次元

> **定理 5: 交換定理（replacement theorem）**  
> $n$ 個のベクトルからなる集合 $G$ に対し $\mathrm{span}(G) = \mathbb{V}$ とする。$L$ が $m$ 個の線形独立なベクトルからなる $\mathbb{V}$ の部分集合であれば、$m \leq n$ である。さらに、$n-m$ 個のベクトルを要素とし $\mathrm{span}(L \cup H) = \mathbb{V}$ を満たす集合 $H \subseteq G$ が存在する。
{: .prompt-info }

これより、きわめて重要な 2 つの系が得られる。

> **交換定理の系 5-1**  
> ベクトル空間 $\mathbb{V}$ が有限集合の基底を含むと仮定すると、$\mathbb{V}$ のすべての基底は有限集合であり、同じ本数のベクトルから成る。
{: .prompt-info }

これによれば、$\mathbb{V}$ の基底を成すベクトルの本数は $\mathbb{V}$ の不変な本質的性質であり、これを**次元（dimension）**という。

> **次元の定義**  
> 基底が有限集合であるベクトル空間を**有限次元（finite dimension）**といい、このとき基底の要素数 $n$ を当該ベクトル空間の**次元（dimension）**とし、$\dim(\mathbb{V})$ と表す。有限次元でないベクトル空間は**無限次元（infinite dimension）**である。
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> ベクトル空間の次元は、どの体の上にあるかによって変わり得る。
> - 複素数体 $\mathbb{C}$ 上では、複素数ベクトル空間の次元は 1、基底は $\\{1\\}$
> - 実数体 $\mathbb{R}$ 上では、複素数ベクトル空間の次元は 2、基底は $\\{1,i\\}$
{: .prompt-tip }

有限次元ベクトル空間 $\mathbb{V}$ では、$\dim(\mathbb{V})$ より多い本数のベクトルを持つ部分集合は決して線形独立ではあり得ない。

> **交換定理の系 5-2**  
> $\mathbb{V}$ が次元 $n$ のベクトル空間とする。
> 1. $\mathbb{V}$ の有限生成集合には必ず $n$ 本以上のベクトルが含まれ、$n$ 本のベクトルからなる $\mathbb{V}$ の生成集合は $\mathbb{V}$ の基底である。
> 2. 線形独立で $n$ 本のベクトルからなる $\mathbb{V}$ の部分集合は $\mathbb{V}$ の基底である。
> 3. 線形独立な $\mathbb{V}$ の部分集合は拡張して基底にできる。すなわち、$L \subseteq \mathbb{V}$ が線形独立なら、$\beta \supseteq L$ を満たす $\mathbb{V}$ の基底 $\beta$ が存在する。
{: .prompt-info }

### 部分空間の次元

> **定理 6**  
> 有限次元ベクトル空間 $\mathbb{V}$ に対し、部分空間 $\mathbb{W}$ は有限次元であり、$\dim(\mathbb{W}) \leq \dim(\mathbb{V})$ である。とくに、$\dim(\mathbb{W}) = \dim(\mathbb{V}) \quad \Rightarrow \quad \mathbb{V} = \mathbb{W}.$
>
> **系 6-1**  
> 有限次元ベクトル空間 $\mathbb{V}$ の部分空間 $\mathbb{W}$ に対し、$\mathbb{W}$ の任意の基底を拡張して $\mathbb{V}$ の基底を得ることができる。
{: .prompt-info }

**定理 6**より、$\mathbb{R}^3$ の部分空間の次元は $0,1,2,3$ になり得る。
- 0 次元: 原点（$\mathbf{0}$）のみを含む点空間 $\\{\mathbf{0}\\}$
- 1 次元: 原点（$\mathbf{0}$）を通る直線
- 2 次元: 原点（$\mathbf{0}$）を含む平面
- 3 次元: ユークリッド 3 次元空間全体
