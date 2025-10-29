---
title: "線性變換、零空間與像"
description: "探討線性變換（linear transformation）的定義，並介紹兩個關鍵子空間——零空間（null space）與像（image）——以及它們的維度（nullity、rank）與相關定理（維度定理、單射與滿射的判別等）。"
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [向量與線性組合](/posts/vectors-and-linear-combinations/)
- [向量空間、子空間，以及矩陣](/posts/vector-spaces-subspaces-and-matrices/)
- [線性相依與線性獨立、基底與維度](posts/linear-dependence-and-independence-basis-and-dimension/)
- 單射、滿射

## 線性變換

保留向量空間結構的特殊函數稱為**線性變換（linear transformation）**，此概念在純數學、應用數學、社會科學、自然科學與工程中極為常見且重要。

> **定義**  
> 設 $\mathbb{V}$ 與 $\mathbb{W}$ 為 $F$-向量空間。對所有 $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ 與 $c \in F$，若函數 $T: \mathbb{V} \to \mathbb{W}$ 滿足下列兩條件，則稱 $T$ 為由 $\mathbb{V}$ 到 $\mathbb{W}$ 的**線性變換（linear transformation）**。
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

稱 $T$ 是線性變換時，亦簡稱 $T$ 是**線性（linear）**。線性變換 $T: \mathbb{V} \to \mathbb{W}$ 具有下列四個性質。

> 1. $T$ 線性 $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ 線性 $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ 線性 $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ 線性 $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> 要證明一個函數為線性時，通常使用第 2 點性質最為便利。
{: .prompt-tip }

> 線性代數在幾何中的應用極廣，原因在於許多重要的幾何變換都是線性的。特別是三大典型幾何變換：**旋轉**、**對稱**、**投影**皆屬線性變換。
{: .prompt-tip }

以下兩個線性變換尤為常見。

> **恆等變換與零變換**  
> 對 $F$-向量空間 $\mathbb{V}, \mathbb{W}$：
> - **恆等變換（identity transformation）**：對所有 $\mathbf{x} \in \mathbb{V}$ 定義 $I_\mathbb{V}(\mathbf{x}) = \mathbf{x}$ 的函數 $I_\mathbb{V}: \mathbb{V} \to \mathbb{V}$
> - **零變換（zero transformation）**：對所有 $\mathbf{x} \in \mathbb{V}$ 定義 $T_0(\mathbf{x}) = \mathbf{0}$ 的函數 $T_0: \mathbb{V} \to \mathbb{W}$
{: .prompt-info }

除此之外，還有許多概念可表為線性變換。

> **線性變換的例子**  
> - 旋轉
> - 對稱
> - 投影
> - [轉置](/posts/vector-spaces-subspaces-and-matrices/#轉置矩陣對稱矩陣斜對稱矩陣)
> - 可微函數的微分
> - 連續函數的積分
{: .prompt-tip }

## 零空間與像

### 零空間與像的定義

> **定義**  
> 對向量空間 $\mathbb{V}, \mathbb{W}$ 與線性變換 $T: \mathbb{V} \to \mathbb{W}$：
> - **零空間（null space）**或**核（kernel）**：由滿足 $T(\mathbf{x}) = \mathbf{0}$ 的 $\mathbf{x} \in \mathbb{V}$ 所成的集合，記作 $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **值域（range）**或**像（image）**：$T$ 的所有函數值所成的 $\mathbb{W}$ 的子集，記作 $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **e.g.** 對向量空間 $\mathbb{V}, \mathbb{W}$、恆等變換 $I: \mathbb{V} \to \mathbb{V}$ 與零變換 $T_0: \mathbb{V} \to \mathbb{W}$，有：
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T_0) = \mathbb{V}$
> - $\mathrm{R}(T_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

以下將反覆用到：線性變換的零空間與像是向量空間的[子空間](/posts/vector-spaces-subspaces-and-matrices/#子空間)。

> **定理 1**  
> 對向量空間 $\mathbb{V}, \mathbb{W}$ 與線性變換 $T: \mathbb{V} \to \mathbb{W}$，$\mathrm{N}(T), \mathrm{R}(T)$ 分別為 $\mathbb{V}, \mathbb{W}$ 的子空間。
>
> **證明**  
> 記 $\mathbb{V}, \mathbb{W}$ 的零向量分別為 $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$。
>
> 因 $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$，故 $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$。又對 $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T),\ c \in F$ 有
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [由於 $\mathbf{0}_\mathbb{V} \in \mathrm{N}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{N}(T),\ c\mathbf{x} \in \mathrm{N}(T)$，$\mathrm{N}(T)$ 為 $\mathbb{V}$ 的子空間](/posts/vector-spaces-subspaces-and-matrices/#子空間)。
>
> 同理，因 $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$，故 $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$；且對所有 $\mathbf{x}, \mathbf{y} \in \mathrm{R}(T),\ c \in F$，存在 $\mathbf{v}, \mathbf{w} \in \mathbb{V}$ 使得 $(T(\mathbf{v}) = \mathbf{x}\ \wedge \ T(\mathbf{w}) = \mathbf{y})$，因此
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [由於 $\mathbf{0}_\mathbb{W} \in \mathrm{R}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{R}(T),\ c\mathbf{x} \in \mathrm{R}(T)$，$\mathrm{R}(T)$ 為 $\mathbb{W}$ 的子空間](/posts/vector-spaces-subspaces-and-matrices/#子空間)。$\blacksquare$
{: .prompt-info }

另一方面，對向量空間 $\mathbb{V}, \mathbb{W}$ 與線性變換 $T: \mathbb{V} \to \mathbb{W}$，若知 $\mathbb{V}$ 的[基底](/posts/linear-dependence-and-independence-basis-and-dimension/#基底) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$，可如下找出像 $\mathrm{R}(T)$ 的[生成集](/posts/vectors-and-linear-combinations/#生成)。

> **定理 2**  
> 對向量空間 $\mathbb{V}, \mathbb{W}$ 與線性變換 $T: \mathbb{V} \to \mathbb{W}$、以及 $\mathbb{V}$ 的[基底](/posts/linear-dependence-and-independence-basis-and-dimension/#基底) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$，有
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **證明**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> 由於 $\mathrm{R}(T)$ 為子空間，依[向量空間、子空間，以及矩陣](/posts/vector-spaces-subspaces-and-matrices/#子空間)的**定理 2**可得
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> 且
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> 由 $\beta$ 為 $\mathbb{V}$ 的基底，得
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{（其中 } a_1, a_2, \dots, a_n \in F \text{）}. $$
>
> 因 $T$ 為線性，故
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ 由 $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ 且同時 $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$，得 $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$。$\blacksquare$
{: .prompt-info }

此定理在基底 $\beta$ 為無限集時亦成立。

### 維度定理

零空間與像是非常重要的子空間，因此也特別為其[維度](/posts/linear-dependence-and-independence-basis-and-dimension/#維度)命名。

> 對向量空間 $\mathbb{V}, \mathbb{W}$ 與線性變換 $T: \mathbb{V} \to \mathbb{W}$，若 $\mathrm{N}(T), \mathrm{R}(T)$ 為有限維，則
> - **零空間的維度（nullity）**：$\mathrm{N}(T)$ 的維度，記作 $\mathrm{nullity}(T)$
> - **秩（rank）**：$\mathrm{R}(T)$ 的維度，記作 $\mathrm{rank}(T)$
{: .prompt-info }

在線性變換中，零空間的維度越大，秩越小；反之亦然。

> **定理 3：維度定理（dimension theorem）**  
> 對向量空間 $\mathbb{V}, \mathbb{W}$ 與線性變換 $T: \mathbb{V}\to \mathbb{W}$，若 $\mathbb{V}$ 為有限維，則
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### 證明

設 $\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$，並令 $\mathrm{N}(T)$ 的基底為 $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$。

依[「線性相依與線性獨立、基底與維度」的**推論 6-1**](/posts/linear-dependence-and-independence-basis-and-dimension/#子空間的維度)，可將 $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ 擴張為 $\mathbb{V}$ 的基底 $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$。

以下將證明 $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ 是 $\mathrm{R}(T)$ 的基底。首先，當 $1 \leq i \leq k$ 時有 $T(\mathbf{v}_i) = 0$，故依[**定理 2**](#零空間與像的定義)
 
$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

亦即 $S$ 為 $\mathrm{R}(T)$ 的生成集。現依[**替換定理的推論 5-2**](/posts/linear-dependence-and-independence-basis-and-dimension/#維度)，只要證明 $S$ 線性獨立，即可得 $S$ 為 $\mathrm{R}(T)$ 的基底。

若 $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$（其中 $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$），因 $T$ 線性，有

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

因此，

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

由 $\beta$ 為 $\mathbb{V}$ 的基底，$\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ 的唯一解為

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

據此可得

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

故 $S$ 線性獨立，亦即為 $\mathrm{R}(T)$ 的基底。

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### 線性變換與單射、滿射

在線性變換中，單射（injection）與滿射（surjection）與秩、零空間的維度密切相關。

> **定理 4**  
> 對向量空間 $\mathbb{V}, \mathbb{W}$ 與線性變換 $T: \mathbb{V} \to \mathbb{W}$，
>
> $$ T\text{ 為單射} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **定理 5**  
> 當有限維向量空間 $\mathbb{V}, \mathbb{W}$ 的維度相同，對線性變換 $T: \mathbb{V} \to \mathbb{W}$，以下四命題互為同值。
> 1. $T$ 為單射。
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ 為滿射。
{: .prompt-info }

可利用[維度定理](#維度定理)、[線性變換的性質 1、3](#線性變換)、以及[「線性相依與線性獨立、基底與維度」的**定理 6**](/posts/linear-dependence-and-independence-basis-and-dimension/#子空間的維度)證明**定理 4**與**定理 5**。

此二定理有助於判斷給定的線性變換是否為單射或滿射。

> 對無限維向量空間 $\mathbb{V}$ 與線性變換 $T: \mathbb{V} \to \mathbb{V}$ 而言，單射與滿射並不等價。
{: .prompt-warning }

當某線性變換為單射時，有時下述定理可用來判斷給定向量空間的子集是否線性獨立。

> **定理 6**  
> 對向量空間 $\mathbb{V}, \mathbb{W}$、單射的線性變換 $T: \mathbb{V} \to \mathbb{W}$ 與 $\mathbb{V}$ 的子集 $S$，有
>
> $$ S\text{ 線性獨立} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \}\text{ 線性獨立。} $$
>
{: .prompt-info }

## 線性變換與基底

線性變換的一項關鍵特徵是：其在基底上的作用決定了變換的全部行為。

> **定理 7**  
> 對 $F$-向量空間 $\mathbb{V}, \mathbb{W}$、$\mathbb{V}$ 的基底 $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$，以及向量 $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$，存在且僅存在一個線性變換 $T: \mathbb{V} \to \mathbb{W}$ 滿足
>
> $$ i = 1, 2, \dots, n \text{ 時 } T(\mathbf{v}_i) = \mathbf{w}_i $$
>
> **證明**  
> 對 $\mathbf{x} \in \mathbb{V}$，其線性組合表示唯一：
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ （}a_1, a_2, \dots, a_n \in F \text{）} $$
>
> 定義線性變換 $T: \mathbb{V} \to \mathbb{W}$ 為
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> 則有
>
> i) 對 $i = 1, 2, \dots, n$，$T(\mathbf{v}_i) = \mathbf{w}_i$。
>
> ii)
>
> 若另一線性變換 $U: \mathbb{V} \to \mathbb{W}$ 亦滿足對 $i = 1, 2, \dots, n$ 有 $U(\mathbf{v}\_i) = \mathbf{w}\_i$，則對 $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$，
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i) $$
>
> $$ \therefore U = T. $$
>
> 由 i)、ii) 得知，滿足 $i = 1, 2, \dots, n$ 且 $T(\mathbf{v}\_i) = \mathbf{w}\_i$ 的線性變換唯一定義為
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i 。\ \blacksquare $$
>
> **推論 7-1**  
> 對兩向量空間 $\mathbb{V}, \mathbb{W}$，若 $\mathbb{V}$ 含有限基底 $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$，且兩線性變換 $U, T: \mathbb{V} \to \mathbf{W}$ 對 $i = 1, 2, \dots, n$ 皆滿足 $U(\mathbf{v}_i) = T(\mathbf{v}_i)$，則 $U = T$。  
> 亦即，<u>在基底上的函數值相同，則為同一個線性變換</u>。
{: .prompt-info }
