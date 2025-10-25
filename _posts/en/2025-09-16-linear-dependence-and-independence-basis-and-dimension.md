---
title: "Linear Dependence and Independence, Bases and Dimension"
description: "A concise guide to linear dependence and independence, and to bases and dimension of vector spaces: definitions, key propositions, replacement theorem, and subspace dimension."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [Vectors and Linear Combinations](/posts/vectors-and-linear-combinations/)
- [Vector Spaces, Subspaces, and Matrices](/posts/vector-spaces-subspaces-and-matrices/)

## Linear dependence and linear independence

Given a [vector space](/posts/vector-spaces-subspaces-and-matrices/#vector-spaces) $\mathbb{V}$ and a [subspace](/posts/vector-spaces-subspaces-and-matrices/#subspaces) $\mathbb{W}$, suppose we wish to find a minimal finite subset $S$ that [spans](/posts/vectors-and-linear-combinations/#the-linear-combination-cmathbfv--dmathbfw) $\mathbb{W}$.

Let $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ with $\mathrm{span}(S) = \mathbb{W}$. How can we decide whether there exists a proper subset of $S$ that still spans $\mathbb{W}$? This is equivalent to asking whether some vector in $S$ can be written as a [linear combination](/posts/vectors-and-linear-combinations/#linear-combinations-of-vectors) of the others. For example, a necessary and sufficient condition for expressing $\mathbf{u}_4$ as a linear combination of the remaining three vectors is the existence of scalars $a_1, a_2, a_3$ satisfying

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

However, solving a new linear system each time for $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ is tedious. Instead, consider

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

If some vector in $S$ is a linear combination of the others, then there exists a representation of the zero vector as a linear combination of elements of $S$ in which at least one among $a_1, a_2, a_3, a_4$ is nonzero. The converse is also true: if there is a nontrivial linear combination of vectors in $S$ that equals the zero vector (i.e., at least one of $a_1, a_2, a_3, a_4$ is nonzero), then some vector in $S$ is a linear combination of the others.

Generalizing this, we define **linear dependence** and **linear independence** as follows.

> **Definition**  
> For a subset $S$ of a vector space $\mathbb{V}$, if there exist finitely many distinct vectors $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ and scalars $a_1, a_2, \dots, a_n$, not all $0$, such that $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$, then the set $S$ (and those vectors) is called **linearly dependent**. Otherwise, it is called **linearly independent**.
{: .prompt-info }

For any vectors $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$, if $a_1 = a_2 = \cdots = a_n = 0$ then $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$; this is called the **trivial representation of the zero vector**.

The following three propositions about linearly independent sets hold in every vector space. In particular, **Proposition 3** is very useful for testing whether a finite set is linearly independent.

> - **Proposition 1**: The empty set is linearly independent. A set must be nonempty to be linearly dependent.
> - **Proposition 2**: A set consisting of a single nonzero vector is linearly independent.
> - **Proposition 3**: A set is linearly independent if and only if the only way to express $\mathbf{0}$ as a linear combination of its vectors is the trivial one.
{: .prompt-info }

The following theorems are also important.

> **Theorem 1**  
> If $\mathbb{V}$ is a vector space and $S_1 \subseteq S_2 \subseteq \mathbb{V}$, then $S_2$ is linearly dependent whenever $S_1$ is linearly dependent.
>
> **Corollary 1-1**  
> If $\mathbb{V}$ is a vector space and $S_1 \subseteq S_2 \subseteq \mathbb{V}$, then $S_1$ is linearly independent whenever $S_2$ is linearly independent.
{: .prompt-info }

> **Theorem 2**  
> Let $\mathbb{V}$ be a vector space and $S$ a linearly independent subset. For a vector $\mathbf{v} \in \mathbb{V}\setminus S$, $S \cup \\{\mathbf{v}\\}$ is linearly dependent if and only if $\mathbf{v} \in \mathrm{span}(S)$.
>
> In other words, **if no proper subset of $S$ spans the same space as $S$, then $S$ is linearly independent.**
{: .prompt-info }

## Bases and dimension

### Basis

A spanning set $S$ of $\mathbb{W}$ that is [linearly independent](#linear-dependence-and-linear-independence) has a special property: every vector in $\mathbb{W}$ can be expressed as a linear combination of $S$, and that expression is unique (**Theorem 3**). Thus, we define a linearly independent spanning set of a vector space to be a **basis**.

> **Definition of a basis**  
> For a vector space $\mathbb{V}$ and a subset $\beta$, if $\beta$ is linearly independent and spans $\mathbb{V}$, then $\beta$ is called a **basis** of $\mathbb{V}$. In this case, the vectors in $\beta$ are said to form a basis of $\mathbb{V}$.
{: .prompt-info }

> $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ and $\emptyset$ is linearly independent. Therefore, $\emptyset$ is a basis of the zero space.
{: .prompt-tip }

In particular, the following distinguished basis of $F^n$ is called the **standard basis** of $F^n$.

> **Definition of the standard basis**  
> For the vector space $F^n$, consider
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> Then the set $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ is a basis of $F^n$, called the **standard basis**.
{: .prompt-info }

> **Theorem 3**  
> Let $\mathbb{V}$ be a vector space and $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$ be distinct vectors. A necessary and sufficient condition for $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ to be a basis of $\mathbb{V}$ is that every vector $\mathbf{v} \in \mathbb{V}$ can be expressed as a linear combination of vectors in $\beta$, and that this expression is unique. That is, there exist unique scalars $(a_1, a_2, \dots, a_n)$ such that
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

By **Theorem 3**, if the distinct vectors $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ form a basis of a vector space $\mathbb{V}$, then within $\mathbb{V}$, a vector $\mathbf{v}$ uniquely determines the scalar $n$-tuple $(a_1, a_2, \dots, a_n)$, and conversely a scalar $n$-tuple uniquely determines the corresponding vector $\mathbf{v}$. We will revisit this when studying **invertibility** and **isomorphisms**; in this case, $\mathbb{V}$ and $F^n$ are <u>essentially the same</u>.

> **Theorem 4**  
> If $S$ is a finite set with $\mathrm{span}(S) = \mathbb{V}$, then some subset of $S$ is a basis of $\mathbb{V}$. In particular, in this case every basis of $\mathbb{V}$ is finite.
{: .prompt-info }

> Many vector spaces fall under the scope of **Theorem 4**, but not all do. <u>A basis need not be finite</u>.{: .prompt-tip }

### Dimension

> **Theorem 5: Replacement theorem**  
> Let $G$ be a set of $n$ vectors with $\mathrm{span}(G) = \mathbb{V}$. If $L$ is a subset of $\mathbb{V}$ consisting of $m$ linearly independent vectors, then $m \le n$. Moreover, there exists a set $H \subseteq G$ with $n-m$ vectors such that $\mathrm{span}(L \cup H) = \mathbb{V}$.
{: .prompt-info }

From this we obtain two very important corollaries.

> **Corollary 5-1 of the replacement theorem**  
> If a vector space $\mathbb{V}$ has a finite basis, then every basis of $\mathbb{V}$ is finite and all bases have the same number of vectors.
{: .prompt-info }

Hence the number of vectors in a basis of $\mathbb{V}$ is an invariant, intrinsic property of $\mathbb{V}$, called its **dimension**.

> **Definition of dimension**  
> A vector space that has a finite basis is called **finite-dimensional**; in this case, the number $n$ of basis elements is the **dimension** of the vector space, denoted $\dim(\mathbb{V})$. A vector space that is not finite-dimensional is called **infinite-dimensional**.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> The dimension of a vector space depends on the underlying field.
> - Over the complex field $\mathbb{C}$, the complex numbers form a 1-dimensional vector space with basis $\\{1\\}$
> - Over the real field $\mathbb{R}$, the complex numbers form a 2-dimensional vector space with basis $\\{1,i\\}$
{: .prompt-tip }

In a finite-dimensional vector space $\mathbb{V}$, any subset with more than $\dim(\mathbb{V})$ vectors can never be linearly independent.

> **Corollary 5-2 of the replacement theorem**  
> Let $\mathbb{V}$ be a vector space of dimension $n$.
> 1. Any finite spanning set of $\mathbb{V}$ has at least $n$ vectors, and any spanning set of $\mathbb{V}$ with exactly $n$ vectors is a basis.
> 2. Any linearly independent subset of $\mathbb{V}$ with exactly $n$ vectors is a basis of $\mathbb{V}$.
        3. Any linearly independent subset of $\mathbb{V}$ can be extended to a basis. That is, if $L \subseteq \mathbb{V}$ is linearly independent, there exists a basis $\beta \supseteq L$ of $\mathbb{V}$.
{: .prompt-info }

### Dimension of subspaces

> **Theorem 6**  
> In a finite-dimensional vector space $\mathbb{V}$, every subspace $\mathbb{W}$ is finite-dimensional and satisfies $\dim(\mathbb{W}) \le \dim(\mathbb{V})$. In particular, if $\dim(\mathbb{W}) = \dim(\mathbb{V})$, then $\mathbb{V} = \mathbb{W}$.
>
> **Corollary 6-1**  
> For a subspace $\mathbb{W}$ of a finite-dimensional vector space $\mathbb{V}$, any basis of $\mathbb{W}$ can be extended to a basis of $\mathbb{V}$.
{: .prompt-info }

By **Theorem 6**, the dimension of a subspace of $\mathbb{R}^3$ can be $0,1,2,$ or $3$.
- 0-dimensional: the zero space $\\{\mathbf{0}\\}$ containing only the origin ($\mathbf{0}$)
- 1-dimensional: a line through the origin ($\mathbf{0}$)
- 2-dimensional: a plane containing the origin ($\mathbf{0}$)
- 3-dimensional: the entire 3D Euclidean space
