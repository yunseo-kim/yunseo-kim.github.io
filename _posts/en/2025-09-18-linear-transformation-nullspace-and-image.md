---
title: "Linear Transformations, Null Space, and Image"
description: "Define linear transformations and study their null space (kernel) and image (range). Prove rank–nullity, relate injectivity/surjectivity to rank and nullity, and show how bases determine linear maps."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [Vectors and Linear Combinations](/posts/vectors-and-linear-combinations/)
- [Vector Spaces, Subspaces, and Matrices](/posts/vector-spaces-subspaces-and-matrices/)
- [Linear Dependence and Independence, Bases and Dimension](posts/linear-dependence-and-independence-basis-and-dimension/)
- Injection, surjection

## Linear transformations

A special class of functions that preserve the structure of vector spaces are called **linear transformations**. They are fundamental across pure and applied mathematics, social and natural sciences, and engineering.

> **Definition**  
> Let $\mathbb{V}$ and $\mathbb{W}$ be $F$-vector spaces. A function $T: \mathbb{V} \to \mathbb{W}$ is called a **linear transformation** from $\mathbb{V}$ to $\mathbb{W}$ if, for all $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ and $c \in F$, the following hold:
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

When $T$ is a linear transformation, we also simply say that $T$ is **linear**. A linear transformation $T: \mathbb{V} \to \mathbb{W}$ satisfies the following four properties.

> 1. $T$ linear $\quad \Rightarrow \quad T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ linear $\quad \Leftrightarrow \quad T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ linear $\quad \Rightarrow \quad T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ linear $\quad \Leftrightarrow \quad T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> When proving that a function is linear, it is often convenient to use Property 2.
{: .prompt-tip }

> Linear algebra has wide and varied applications in geometry because many important geometric maps are linear. In particular, the three principal geometric transformations—**rotation**, **reflection**, and **projection**—are linear transformations.
{: .prompt-tip }

Two linear transformations occur especially often:

> **Identity and zero transformations**  
> For $F$-vector spaces $\mathbb{V}, \mathbb{W}$:
> - **Identity transformation**: the function $I\_\mathbb{V}: \mathbb{V} \to \mathbb{V}$ defined by $I\_\mathbb{V}(\mathbf{x}) = \mathbf{x}$ for all $\mathbf{x} \in \mathbb{V}$
> - **Zero transformation**: the function $T\_0: \mathbb{V} \to \mathbb{W}$ defined by $T\_0(\mathbf{x}) = \mathbf{0}$ for all $\mathbf{x} \in \mathbb{V}$
{: .prompt-info }

Many other familiar operations are linear transformations.

> **Examples of linear transformations**  
> - Rotation
> - Reflection
> - Projection
> - [Transpose](/posts/vector-spaces-subspaces-and-matrices/#transpose-symmetric-and-skew-symmetric-matrices)
> - Differentiation of a differentiable function
> - Integration of a continuous function
{: .prompt-tip }

## Null space and image

### Definitions of the null space and the image

> **Definition**  
> For vector spaces $\mathbb{V}, \mathbb{W}$ and a linear transformation $T: \mathbb{V} \to \mathbb{W}$:
> - **Null space** (or **kernel**): the set of vectors $\mathbf{x} \in \mathbb{V}$ such that $T(\mathbf{x}) = \mathbf{0}$, denoted $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **Range** (or **image**): the subset of $\mathbb{W}$ consisting of all values of $T$, denoted $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **e.g.** For vector spaces $\mathbb{V}, \mathbb{W}$, the identity $I: \mathbb{V} \to \mathbb{V}$ and the zero map $T\_0: \mathbb{V} \to \mathbb{W}$ satisfy:
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T\_0) = \mathbb{V}$
> - $\mathrm{R}(T\_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

A key point going forward is that the null space and the image of a linear transformation are [subspaces](/posts/vector-spaces-subspaces-and-matrices/#subspaces) of the corresponding vector spaces.

> **Theorem 1**  
> For vector spaces $\mathbb{V}, \mathbb{W}$ and a linear transformation $T: \mathbb{V} \to \mathbb{W}$, the sets $\mathrm{N}(T)$ and $\mathrm{R}(T)$ are subspaces of $\mathbb{V}$ and $\mathbb{W}$, respectively.
>
> **Proof**  
> Denote the zero vectors of $\mathbb{V}$ and $\mathbb{W}$ by $\mathbf{0}\_\mathbb{V}$ and $\mathbf{0}\_\mathbb{W}$, respectively.
>
> Since $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, we have $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$. Moreover, for $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T)$ and $c \in F$,
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [Since $\mathbf{0}_\mathbb{V} \in \mathrm{N}(T)$ and $\mathrm{N}(T)$ is closed under addition and scalar multiplication, $\mathrm{N}(T)$ is a subspace of $\mathbb{V}$](/posts/vector-spaces-subspaces-and-matrices/#subspaces).
>
> Similarly, $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$ implies $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$. For all $\mathbf{x}, \mathbf{y} \in \mathrm{R}(T)$ and $c \in F$ (there exist $\mathbf{v}, \mathbf{w} \in \mathbb{V}$ with $T(\mathbf{v}) = \mathbf{x}$ and $T(\mathbf{w}) = \mathbf{y}$), we have
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [Since $\mathbf{0}_\mathbb{W} \in \mathrm{R}(T)$ and $\mathrm{R}(T)$ is closed under addition and scalar multiplication, $\mathrm{R}(T)$ is a subspace of $\mathbb{W}$](/posts/vector-spaces-subspaces-and-matrices/#subspaces). $\blacksquare$
{: .prompt-info }

Furthermore, given a basis $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ of $\mathbb{V}$, we can find a generating set of the image $\mathrm{R}(T)$ as follows.

> **Theorem 2**  
> For vector spaces $\mathbb{V}, \mathbb{W}$, a linear transformation $T: \mathbb{V} \to \mathbb{W}$, and a [basis](/posts/linear-dependence-and-independence-basis-and-dimension/#basis) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ of $\mathbb{V}$, we have
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **Proof**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> Since $\mathrm{R}(T)$ is a subspace, by **Theorem 2** of [Vector Spaces, Subspaces, and Matrices](/posts/vector-spaces-subspaces-and-matrices/#subspaces),
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> Also,
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> Because $\beta$ is a basis of $\mathbb{V}$,
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(where } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> Since $T$ is linear,
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ Since both contain each other, $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

This theorem remains valid even when the basis $\beta$ is infinite.

### Dimension theorem

Because the null space and image are especially important subspaces, we give special names to their [dimensions](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension).

> For vector spaces $\mathbb{V}, \mathbb{W}$ and a linear transformation $T: \mathbb{V} \to \mathbb{W}$, assume $\mathrm{N}(T)$ and $\mathrm{R}(T)$ are finite-dimensional.
> - **Nullity**: the dimension of $\mathrm{N}(T)$, denoted $\mathrm{nullity}(T)$
> - **Rank**: the dimension of $\mathrm{R}(T)$, denoted $\mathrm{rank}(T)$
{: .prompt-info }

For a linear transformation, the larger the nullity, the smaller the rank, and vice versa.

> **Theorem 3: Dimension theorem**  
> For vector spaces $\mathbb{V}, \mathbb{W}$ and a linear transformation $T: \mathbb{V}\to \mathbb{W}$, if $\mathbb{V}$ is finite-dimensional, then
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### Proof

Let $\dim(\mathbb{V}) = n$ and $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$, and let a basis of $\mathrm{N}(T)$ be $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$.

By [“Linear Dependence and Independence, Bases and Dimension” — **Corollary 6-1**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension-of-subspaces), we can extend $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ to a basis $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ of $\mathbb{V}$.

We now show that $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ is a basis of $\mathrm{R}(T)$. First, for $1 \leq i \leq k$, $T(\mathbf{v}_i) = 0$, so by [**Theorem 2**](#definitions-of-the-null-space-and-the-image),

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

Thus $S$ generates $\mathrm{R}(T)$. By [**Corollary 5-2 of the replacement theorem**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension), it suffices to show that $S$ is linearly independent.

Suppose $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (with $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$). Since $T$ is linear,

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

Therefore,

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

Since $\beta$ is a basis of $\mathbb{V}$, the unique solution of $\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ is

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

and hence

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

Thus $S$ is linearly independent and is a basis of $\mathrm{R}(T)$.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### Linear transformations and injections/surjections

For linear transformations, injectivity and surjectivity are closely tied to rank and nullity.

> **Theorem 4**  
> For vector spaces $\mathbb{V}, \mathbb{W}$ and a linear transformation $T: \mathbb{V} \to \mathbb{W}$,
>
> $$ T \text{ is injective} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **Theorem 5**  
> If finite-dimensional vector spaces $\mathbb{V}, \mathbb{W}$ have the same dimension and $T: \mathbb{V} \to \mathbb{W}$ is linear, then the following four statements are equivalent.
> 1. $T$ is injective.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ is surjective.
{: .prompt-info }

Using the [dimension theorem](#dimension-theorem), [Properties 1 and 3 of linear transformations](#linear-transformations), and [“Linear Dependence and Independence, Bases and Dimension” — **Theorem 6**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimension-of-subspaces), one can prove **Theorem 4** and **Theorem 5**.

These two theorems are useful when deciding whether a given linear transformation is injective or surjective.

> For an infinite-dimensional vector space $\mathbb{V}$ and a linear transformation $T: \mathbb{V} \to \mathbb{V}$, injectivity and surjectivity are not equivalent.
{: .prompt-warning }

If a linear transformation is injective, the following theorem can be useful in some cases for testing whether a subset of the domain is linearly independent.

> **Theorem 6**  
> For vector spaces $\mathbb{V}, \mathbb{W}$, an injective linear transformation $T: \mathbb{V} \to \mathbb{W}$, and a subset $S \subseteq \mathbb{V}$,
>
> $$ S \text{ is linearly independent} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \} \text{ is linearly independent.} $$
>
{: .prompt-info }

## Linear transformations and bases

A key feature of linear transformations is that their action is determined by their values on a basis.

> **Theorem 7**  
> Let $\mathbb{V}, \mathbb{W}$ be $F$-vector spaces, let $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ be a basis of $\mathbb{V}$, and let $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$. Then there exists a unique linear transformation $T: \mathbb{V} \to \mathbb{W}$ such that
>
> $$ T(\mathbf{v}_i) = \mathbf{w}_i \quad (i = 1, 2, \dots, n). $$
>
> **Proof**  
> For $\mathbf{x} \in \mathbb{V}$, the representation
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ (}a_1, a_2, \dots, a_n \in F \text{)} $$
>
> is unique. Define a linear transformation $T: \mathbb{V} \to \mathbb{W}$ by
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. $$
>
> i) For $i = 1, 2, \dots, n$, $T(\mathbf{v}_i) = \mathbf{w}_i$.
>
> ii) Suppose another linear transformation $U: \mathbb{V} \to \mathbb{W}$ satisfies $U(\mathbf{v}\_i) = \mathbf{w}\_i$ for $i = 1, 2, \dots, n$. Then for $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$,
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i) $$
>
> $$ \therefore U = T. $$
>
> From i) and ii), the linear transformation satisfying $T(\mathbf{v}\_i) = \mathbf{w}\_i$ for $i = 1, 2, \dots, n$ is unique and given by
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. \ \blacksquare$$
>
> **Corollary 7-1**  
> Let $\mathbb{V}, \mathbb{W}$ be vector spaces and suppose $\mathbb{V}$ has a finite basis $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$. If two linear transformations $U, T: \mathbb{V} \to \mathbf{W}$ satisfy $U(\mathbf{v}_i) = T(\mathbf{v}_i)$ for $i = 1, 2, \dots, n$, then $U = T$.  
> In other words, <u>if two linear transformations agree on a basis, they are equal.</u>
{: .prompt-info }
