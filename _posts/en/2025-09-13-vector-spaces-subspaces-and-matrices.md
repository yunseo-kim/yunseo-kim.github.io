---
title: "Vector Spaces, Subspaces, and Matrices"
description: "Define vector spaces and subspaces with canonical examples (R^n, matrix, and function spaces). Focus on matrix spaces: symmetric/skew, triangular, and diagonal subspaces."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Matrix**
>   - The entry of a matrix $A$ in the $i$-th row and $j$-th column is denoted $A\_{ij}$ or $a\_{ij}$
>   - **Diagonal entry**: an entry $a\_{ij}$ with $i=j$
>   - The components $a\_{i1}, a\_{i2}, \dots, a\_{in}$ are the $i$-th **row** of the matrix
>     - Each row of a matrix can be regarded as a vector in $F^n$
>     - Moreover, a row vector in $F^n$ can be viewed as another matrix of size $1 \times n$
>   - The components $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ are the $j$-th **column** of the matrix
>     - Each column of a matrix can be regarded as a vector in $F^m$
>     - Moreover, a column vector in $F^m$ can be viewed as another matrix of size $m \times 1$
>   - **Zero matrix**: a matrix all of whose entries are $0$, denoted by $O$
>   - **Square matrix**: a matrix with the same number of rows and columns
>   - For two $m \times n$ matrices $A, B$, if $A\_{ij} = B\_{ij}$ for all $1 \leq i \leq m$, $1 \leq j \leq n$ (i.e., every corresponding entry agrees), then the two matrices are defined to be **equal** ($A=B$)
>   - **Transpose (transpose matrix)**: for an $m \times n$ matrix $A$, the $n \times m$ matrix $A^T$ obtained by swapping rows and columns of $A$
>   - **Symmetric matrix**: a square matrix $A$ with $A^T = A$
>   - **Skew-symmetric matrix**: a square matrix $B$ with $B^T = -B$
>   - **Triangular matrix**
>     - **Upper triangular matrix**: a matrix whose entries below the diagonal are all $0$ (i.e., $i>j \Rightarrow A\_{ij}=0$), usually denoted by $U$
>     - **Lower triangular matrix**: a matrix whose entries above the diagonal are all $0$ (i.e., $i<j \Rightarrow A\_{ij}=0$), usually denoted by $L$
>   - **Diagonal matrix**: an $n \times n$ square matrix whose off-diagonal entries are all $0$ (i.e., $i \neq j \Rightarrow M\_{ij}=0$), usually denoted by $D$
> - Representative vector spaces
>   - **The $n$-tuples $F^n$**:
>     - The set of all $n$-tuples with entries in a field $F$
>     - Denoted $F^n$; an $F$-vector space
>   - **Matrix space**:
>     - The set of all $m \times n$ matrices with entries in a field $F$
>     - Denoted $\mathcal{M}\_{m \times n}(F)$; a vector space
>   - **Function space**:
>     - For a nonempty set $S$ over a field $F$, the set of all functions from $S$ to $F$
>     - Denoted $\mathcal{F}(S,F)$; a vector space
> - **Subspace**
>   - A subset $\mathbb{W}$ of an $F$-vector space $\mathbb{V}$ is called a **subspace** of $\mathbb{V}$ if it is an $F$-vector space under the same addition and scalar multiplication as defined on $\mathbb{V}$
>   - For every vector space $\mathbb{V}$, both $\mathbb{V}$ itself and $\\{0\\}$ are subspaces; in particular, $\\{0\\}$ is called the **zero subspace**
>   - If a subset of a vector space contains the zero vector and is closed under [linear combinations](/posts/vectors-and-linear-combinations/#linear-combinations-of-vectors) (i.e., if $\mathrm{span}(\mathbb{W})=\mathbb{W}$), then it is a subspace
{: .prompt-info }

## Prerequisites
- [Vectors and Linear Combinations](/posts/vectors-and-linear-combinations/)

## Vector spaces

As briefly noted in [Vectors and Linear Combinations](/posts/vectors-and-linear-combinations/#vector-in-the-broad-sense-an-element-of-a-vector-space), the definitions of vectors and vector spaces as algebraic structures are as follows.

> **Definition**  
> A **vector space** (or **linear space**) $\mathbb{V}$ over a field $F$ is a set equipped with two operations, **sum** and **scalar multiplication**, satisfying the following eight axioms. Elements of the field $F$ are called **scalars**, and elements of the vector space $\mathbb{V}$ are called **vectors**.
>
> - **Sum**: For $\mathbf{x}, \mathbf{y} \in \mathbb{V}$, there exists a unique element $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. We call $\mathbf{x} + \mathbf{y}$ the **sum** of $\mathbf{x}$ and $\mathbf{y}$.
> - **Scalar multiplication**: For $a \in F$ and $\mathbf{x} \in \mathbb{V}$, there exists a unique element $a\mathbf{x} \in \mathbb{V}$. We call $a\mathbf{x}$ a **scalar multiple** of $\mathbf{x}$.
>
> 1. For all $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (commutativity of addition)
> 2. For all $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$, $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (associativity of addition)
> 3. There exists $\mathbf{0} \in \mathbb{V}$ such that $\mathbf{x} + \mathbf{0} = \mathbf{x}$ for all $\mathbf{x} \in \mathbb{V}$. (zero vector, additive identity)
> 4. For each $\mathbf{x} \in \mathbb{V}$, there exists $\mathbf{y} \in \mathbb{V}$ such that $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (additive inverse)
> 5. For each $\mathbf{x} \in \mathbb{V}$, $1\mathbf{x} = \mathbf{x}$. (multiplicative identity)
> 6. For all $a,b \in F$ and $\mathbf{x} \in \mathbb{V}$, $(ab)\mathbf{x} = a(b\mathbf{x})$. (associativity of scalar multiplication)
> 7. For all $a \in F$ and $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (distributivity of scalar multiplication over vector addition)
> 8. For all $a,b \in F$ and $\mathbf{x},\mathbf{y} \in \mathbb{V}$, $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (distributivity of scalar multiplication over field addition)
{: .prompt-info }

Strictly speaking, one should write “the $F$-vector space $\mathbb{V}$,” but when discussing vector spaces the specific field is often not essential; thus, when there is no risk of confusion, we omit $F$ and simply write “the vector space $\mathbb{V}$.”

### Matrix spaces

#### Row and column vectors

The set of all $n$-tuples with entries in a field $F$ is denoted $F^n$. For $u = (a_1, a_2, \dots, a_n) \in F^n$ and $v = (b_1, b_2, \dots, b_n) \in F^n$, defining addition and scalar multiplication by

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

makes $F^n$ into an $F$-vector space.

Vectors in $F^n$ are usually written as **column vectors** rather than standalone **row vectors** $(a_1, a_2, \dots, a_n)$:

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

> Because column-vector notation takes more vertical space, one often uses the [transpose](#transpose-symmetric-and-skew-symmetric-matrices) to write $(a_1, a_2, \dots, a_n)^T$ instead.
{: .prompt-tip }

#### Matrices and matrix spaces

An $m \times n$ **matrix** with entries in $F$ is a rectangular array, typically denoted by italic capitals ($A, B, C$, etc.):

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- The entry of a matrix $A$ in the $i$-th row and $j$-th column is denoted $A\_{ij}$ or $a\_{ij}$.
- Each $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) belongs to $F$.
- An entry $a\_{ij}$ with $i=j$ is called a **diagonal entry**.
- The components $a\_{i1}, a\_{i2}, \dots, a\_{in}$ form the $i$-th **row** of the matrix. Each row can be regarded as a vector in $F^n$, and, furthermore, a row vector in $F^n$ can be viewed as another matrix of size $1 \times n$.
- The components $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ form the $j$-th **column** of the matrix. Each column can be regarded as a vector in $F^m$, and, furthermore, a column vector in $F^m$ can be viewed as another matrix of size $m \times 1$.
- An $m \times n$ matrix whose entries are all $0$ is called the **zero matrix**, denoted $O$.
- A matrix with the same number of rows and columns is called a **square matrix**.
- For two $m \times n$ matrices $A, B$, if $A\_{ij} = B\_{ij}$ for all $1 \leq i \leq m$, $1 \leq j \leq n$ (i.e., every corresponding entry agrees), we define the matrices to be **equal** ($A=B$).

The set of all $m \times n$ matrices with entries in $F$ is denoted $\mathcal{M}\_{m \times n}(F)$. For $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F)$ and $c \in F$, defining addition and scalar multiplication by

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(for }1 \leq i \leq &m, 1 \leq j \leq n \text{)}
\end{align*} $$

makes $\mathcal{M}\_{m \times n}(F)$ a vector space, called a **matrix space**.

This naturally extends the operations defined on $F^n$ and $F^m$.

### Function spaces

For a nonempty set $S$ over a field $F$, $\mathcal{F}(S,F)$ denotes the set of all functions from $S$ to $F$. For $f,g \in \mathcal{F}(S,F)$, we declare $f$ and $g$ **equal** ($f=g$) if $f(s) = g(s)$ for all $s \in S$.

For $f,g \in \mathcal{F}(S,F)$, $c \in F$, and $s \in S$, defining addition and scalar multiplication by

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

makes $\mathcal{F}(S,F)$ a vector space, called a **function space**.

## Subspaces

> **Definition**  
> A subset $\mathbb{W}$ of an $F$-vector space $\mathbb{V}$ is called a **subspace** of $\mathbb{V}$ if it is an $F$-vector space under the same addition and scalar multiplication as those defined on $\mathbb{V}$.
{: .prompt-info }

For every vector space $\mathbb{V}$, both $\mathbb{V}$ itself and $\\{0\\}$ are subspaces; in particular, $\\{0\\}$ is called the **zero subspace**.

Whether a subset is a subspace can be checked using the following theorem.

> **Theorem**  
> For a vector space $\mathbb{V}$ and a subset $\mathbb{W}$, $\mathbb{W}$ is a subspace of $\mathbb{V}$ if and only if the following three conditions hold (with the operations inherited from $\mathbb{V}$):
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> In short, if it contains the zero vector and is closed under [linear combinations](/posts/vectors-and-linear-combinations/#linear-combinations-of-vectors) (i.e., if $\mathrm{span}(\mathbb{W})=\mathbb{W}$), then it is a subspace.
{: .prompt-info }

The following theorems also hold.

> **Theorem**  
> - For any subset $S$ of a vector space $\mathbb{V}$, the span $\mathrm{span}(S)$ is a subspace of $\mathbb{V}$ containing $S$.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - Any subspace of $\mathbb{V}$ that contains $S$ must contain the span of $S$.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **Theorem**  
> For subspaces of a vector space $\mathbb{V}$, the intersection of any collection of such subspaces is again a subspace of $\mathbb{V}$.
{: .prompt-info }

### Transpose, symmetric, and skew-symmetric matrices

The **transpose** $A^T$ of an $m \times n$ matrix $A$ is the $n \times m$ matrix obtained by swapping the rows and columns of $A$:

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

A matrix $A$ with $A^T = A$ is called **symmetric**, and a matrix $B$ with $B^T = -B$ is called **skew-symmetric**. Symmetric and skew-symmetric matrices must be square.

Let $\mathbb{W}\_1$ and $\mathbb{W}\_2$ be the sets of all symmetric and all skew-symmetric matrices in $\mathcal{M}\_{n \times n}(F)$, respectively. Then $\mathbb{W}\_1$ and $\mathbb{W}\_2$ are subspaces of $\mathcal{M}\_{n \times n}(F)$; that is, they are closed under addition and scalar multiplication.

### Triangular and diagonal matrices

These two classes of matrices are also particularly important.

First, we collectively call the following two types of matrices **triangular matrices**:
- **Upper triangular matrix**: a matrix whose entries below the diagonal are all $0$ (i.e., $i>j \Rightarrow A\_{ij}=0$), usually denoted by $U$
- **Lower triangular matrix**: a matrix whose entries above the diagonal are all $0$ (i.e., $i<j \Rightarrow A\_{ij}=0$), usually denoted by $L$

An $n \times n$ square matrix in which all off-diagonal entries are $0$—that is, $i \neq j \Rightarrow M\_{ij}=0$—is called a **diagonal matrix**, usually denoted by $D$. A diagonal matrix is both upper and lower triangular.

The sets of upper triangular matrices, lower triangular matrices, and diagonal matrices are all subspaces of $\mathcal{M}\_{m \times n}(F)$.
