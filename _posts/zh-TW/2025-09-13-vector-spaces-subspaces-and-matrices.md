---
title: "向量空間、子空間，以及矩陣"
description: "以向量空間與子空間的定義為核心，介紹典型例子：矩陣空間與函數空間。並特別聚焦於矩陣空間，系統整理能構成重要子空間的對稱／斜對稱矩陣、上／下三角矩陣與對角矩陣。"
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **矩陣（matrix）**
>   - 矩陣 $A$ 的第 $i$ 行第 $j$ 列元素記為 $A\_{ij}$ 或 $a\_{ij}$
>   - **對角元素（diagonal entry）**：滿足 $i=j$ 的元素 $a\_{ij}$
>   - 元素 $a\_{i1}, a\_{i2}, \dots, a\_{in}$ 稱為此矩陣的第 $i$ 個**行（row）**
>     - 矩陣的每一行可視為 $F^n$ 的向量
>     - 進一步地，$F^n$ 的行向量也可視為一個 $1 \times n$ 的矩陣
>   - 元素 $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ 稱為此矩陣的第 $j$ 個**列（column）**
>     - 矩陣的每一列可視為 $F^m$ 的向量
>     - 進一步地，$F^m$ 的列向量也可視為一個 $m \times 1$ 的矩陣
>   - **零矩陣（zero matrix）**：所有元素皆為 $0$ 的矩陣，記作 $O$
>   - **方陣（square matrix）**：行數與列數相同的矩陣
>   - 對兩個 $m \times n$ 矩陣 $A, B$，若對所有 $1 \leq i \leq m$, $1 \leq j \leq n$ 皆有 $A\_{ij} = B\_{ij}$（即對應元素逐一相等），則定義兩矩陣**相等**（$A=B$）
>   - **轉置矩陣（transpose matrix）**：對 $m \times n$ 矩陣 $A$，將其行與列互換所得的 $n \times m$ 矩陣 $A^T$
>   - **對稱矩陣（symmetric matrix）**：滿足 $A^T = A$ 的方陣 $A$
>   - **斜對稱矩陣（skew-symmetric matrix）**：滿足 $B^T = -B$ 的方陣 $B$
>   - **三角矩陣（triangular matrix）**
>     - **上三角矩陣（upper triangular matrix）**：對角線以下元素全為 $0$（即 $i>j \Rightarrow A\_{ij}=0$），常記作 $U$
>     - **下三角矩陣（lower triangular matrix）**：對角線以上元素全為 $0$（即 $i<j \Rightarrow A\_{ij}=0$），常記作 $L$
>   - **對角矩陣（diagonal matrix）**：除對角線元素外，其餘皆為 $0$ 的方陣（即 $i \neq j \Rightarrow M\_{ij}=0$ 的 $n \times n$ 矩陣），常記作 $D$
> - 代表性的向量空間
>   - **$n$ 維有序組 $F^n$**：
>     - 由體 $F$ 的元素作為分量之所有 $n$ 維有序組的集合
>     - 記作 $F^n$，是 $F$-向量空間
>   - **矩陣空間（matrix space）**：
>     - 所有分量屬於體 $F$ 的 $m \times n$ 矩陣之集合
>     - 記作 $\mathcal{M}\_{m \times n}(F)$，為向量空間
>   - **函數空間（function space）**：
>     - 對體 $F$ 上的非空集合 $S$，由 $S$ 到 $F$ 的所有函數之集合
>     - 記作 $\mathcal{F}(S,F)$，為向量空間
> - **子空間（subspace）**
>   - 當 $F$-向量空間 $\mathbb{V}$ 的子集 $\mathbb{W}$，在沿用 $\mathbb{V}$ 的加法與純量乘法之下仍構成 $F$-向量空間，則稱 $\mathbb{W}$ 為 $\mathbb{V}$ 的**子空間（subspace）**
>   - 對任意向量空間 $\mathbb{V}$，$\mathbb{V}$ 本身與 $\\{0\\}$ 皆為其子空間，特別地，$\\{0\\}$ 稱為**零子空間（zero subspace）**
>   - 若某子集含有零向量，且對[線性組合](/posts/vectors-and-linear-combinations/#向量的線性組合)封閉（即 $\mathrm{span}(\mathbb{W})=\mathbb{W}$），則該集合為子空間
{: .prompt-info }

## Prerequisites
- [向量與線性組合](/posts/vectors-and-linear-combinations/)

## 向量空間

如同在[向量與線性組合](/posts/vectors-and-linear-combinations/#廣義的向量向量空間的元素)中稍作提及，作為代數結構之向量與向量空間的定義如下。

> **定義**  
> 定義在體 $F$ 上的**向量空間（vector space）**或**線性空間（linear space）** $\mathbb{V}$，是配備兩種運算——**加法**與**純量乘法**——且滿足下列八項公理的集合。體 $F$ 的元素稱為**純量（scalar）**，向量空間 $\mathbb{V}$ 的元素稱為**向量（vector）**。
>
> - **加法（sum）**：對 $\mathbb{V}$ 的任意兩元素 $\mathbf{x}, \mathbf{y}$，對應到唯一元素 $\mathbf{x} + \mathbf{y} \in \mathbb{V}$。此時 $\mathbf{x} + \mathbf{y}$ 稱為 $\mathbf{x}$ 與 $\mathbf{y}$ 的**和**。
> - **純量乘法（scalar multiplication）**：對體 $F$ 的元素 $a$ 與向量空間 $\mathbb{V}$ 的元素 $\mathbf{x}$，對應到唯一元素 $a\mathbf{x} \in \mathbb{V}$。此時 $a\mathbf{x}$ 稱為 $\mathbf{x}$ 的**純量倍（scalar multiple）**。
>
> 1. 對所有 $\mathbf{x},\mathbf{y} \in \mathbb{V}$，有 $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$。（加法的交換律）
> 2. 對所有 $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$，有 $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$。（加法的結合律）
> 3. 對所有 $\mathbf{x} \in \mathbb{V}$，存在 $\mathbf{0} \in \mathbb{V}$ 使得 $\mathbf{x} + \mathbf{0} = \mathbf{x}$。（零向量，加法的單位元）
> 4. 對每個 $\mathbf{x} \in \mathbb{V}$，存在 $\mathbf{y} \in \mathbb{V}$ 使得 $\mathbf{x}+\mathbf{y}=\mathbf{0}$。（加法的逆元）
> 5. 對每個 $\mathbf{x} \in \mathbb{V}$，有 $1\mathbf{x} = \mathbf{x}$。（乘法的單位元）
> 6. 對所有 $a,b \in F$ 與所有 $\mathbf{x} \in \mathbb{V}$，有 $(ab)\mathbf{x} = a(b\mathbf{x})$。（純量乘法的結合律）
> 7. 對所有 $a \in F$ 與所有 $\mathbf{x},\mathbf{y} \in \mathbb{V}$，有 $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$。（對加法的純量乘法分配律 1）
> 8. 對所有 $a,b \in F$ 與所有 $\mathbf{x},\mathbf{y} \in \mathbb{V}$，有 $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$。（對加法的純量乘法分配律 2）
{: .prompt-info }

嚴格而言應寫作「$F$-向量空間 $\mathbb{V}$」，但在討論向量空間時，體 $F$ 通常不是重點；若不致混淆，便省略 $F$ 而直接稱作「向量空間 $\mathbb{V}$」。

### 矩陣空間

#### 行向量與列向量

由體 $F$ 的元素作為分量之所有 $n$ 維有序組的集合，記作 $F^n$。令 $u = (a_1, a_2, \dots, a_n) \in F^n$, $v = (b_1, b_2, \dots, b_n) \in F^n$，若定義加法與純量乘法如下，則 $F^n$ 為 $F$-向量空間。

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

$F^n$ 的向量在單獨書寫時，通常不寫作**行向量（row vector）** $(a_1, a_2, \dots, a_n)$，而更常寫作**列向量（column vector）**

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

> 但此種列向量表示較佔版面，故亦常利用[轉置](#轉置矩陣對稱矩陣斜對稱矩陣)寫作 $(a_1, a_2, \dots, a_n)^T$。
{: .prompt-tip }

#### 矩陣與矩陣空間

另一方面，分量屬於 $F$ 的 $m \times n$ **矩陣（matrix）**是一個如下的長方形陣列，通常以斜體大寫字母（$A, B, C$ 等）表示。

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- 矩陣 $A$ 的第 $i$ 行第 $j$ 列元素記為 $A\_{ij}$ 或 $a\_{ij}$。
- 所有 $a\_{ij}$（$1 \leq i \leq m$, $1 \leq j \leq n$）皆為 $F$ 的元素。
- 滿足 $i=j$ 的元素 $a\_{ij}$ 稱為此矩陣的**對角元素（diagonal entry）**。
- 元素 $a\_{i1}, a\_{i2}, \dots, a\_{in}$ 稱為此矩陣的第 $i$ 個**行（row）**。矩陣的每一行可視為 $F^n$ 的向量；進一步地，$F^n$ 的行向量也可視為 $1 \times n$ 的另一個矩陣。
- 元素 $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ 稱為此矩陣的第 $j$ 個**列（column）**。矩陣的每一列可視為 $F^m$ 的向量；進一步地，$F^m$ 的列向量也可視為 $m \times 1$ 的另一個矩陣。
- 所有元素皆為 $0$ 的 $m \times n$ 矩陣稱為**零矩陣（zero matrix）**，記作 $O$。
- 行數與列數相同的矩陣稱為**方陣（square matrix）**。
- 對兩個 $m \times n$ 矩陣 $A, B$，若對所有 $1 \leq i \leq m$, $1 \leq j \leq n$ 皆有 $A\_{ij} = B\_{ij}$（即對應元素逐一相等），則定義兩矩陣**相等**（$A=B$）。

分量屬於體 $F$ 的所有 $m \times n$ 矩陣的集合記作 $\mathcal{M}\_{m \times n}(F)$。對 $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F)$ 與 $c \in F$，若定義加法與純量乘法如下，則 $\mathcal{M}\_{m \times n}(F)$ 構成向量空間，稱為**矩陣空間（matrix space）**。

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{（其中 }1 \leq i \leq &m, 1 \leq j \leq n \text{）}
\end{align*} $$

此即將在 $F^n$ 與 $F^m$ 上定義的運算，自然地擴張至矩陣的情形。

### 函數空間

對體 $F$ 的非空集合 $S$，$\mathcal{F}(S,F)$ 表示所有由 $S$ 到 $F$ 的函數之集合。在 $\mathcal{F}(S,F)$ 中，若對所有 $s \in S$ 皆有 $f(s) = g(s)$，則稱兩函數 $f, g$ **相等**（$f=g$）。

對 $f,g \in \mathcal{F}(S,F)$、$c \in F$、$s \in S$，若定義加法與純量乘法如下，則 $\mathcal{F}(S,F)$ 構成向量空間，稱為**函數空間（function space）**。

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## 子空間

> **定義**  
> 若 $F$-向量空間 $\mathbb{V}$ 的子集 $\mathbb{W}$，在沿用 $\mathbb{V}$ 的加法與純量乘法之下仍構成 $F$-向量空間，則稱 $\mathbb{W}$ 為 $\mathbb{V}$ 的**子空間（subspace）**。
{: .prompt-info }

對任意向量空間 $\mathbb{V}$，$\mathbb{V}$ 本身與 $\\{0\\}$ 皆為其子空間，特別地，$\\{0\\}$ 稱為**零子空間（zero subspace）**。

判別某子集是否為子空間，可用下述定理。

> **定理**  
> 對向量空間 $\mathbb{V}$ 與其子集 $\mathbb{W}$，$\mathbb{W}$ 為 $\mathbb{V}$ 的子空間之必要且充分條件，是滿足下列三項（運算沿用 $\mathbb{V}$ 的定義）：
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> 簡言之，若其包含零向量，且對[線性組合](/posts/vectors-and-linear-combinations/#向量的線性組合)封閉（$\mathrm{span}(\mathbb{W})=\mathbb{W}$），則為子空間。
{: .prompt-info }

此外，下列定理亦成立。

> **定理**  
> - 對向量空間 $\mathbb{V}$ 的任意子集 $S$，其生成空間 $\mathrm{span}(S)$ 是包含 $S$ 的 $\mathbb{V}$ 的子空間。
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - 任何包含 $S$ 的 $\mathbb{V}$ 的子空間，必然包含 $S$ 的生成空間。
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **定理**  
> 對向量空間 $\mathbb{V}$ 的諸子空間，其任意交集仍為 $\mathbb{V}$ 的子空間。
{: .prompt-info }

### 轉置矩陣、對稱矩陣、斜對稱矩陣

$m \times n$ 矩陣 $A$ 的**轉置矩陣（transpose matrix）** $A^T$，是將 $A$ 的行與列互換所得之 $n \times m$ 矩陣。

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

滿足 $A^T = A$ 的矩陣 $A$ 稱為**對稱矩陣（symmetric matrix）**；滿足 $B^T = -B$ 的矩陣 $B$ 稱為**斜對稱矩陣（skew-symmetric matrix）**。對稱與斜對稱矩陣必為方陣。

分別以 $\mathbb{W}\_1, \mathbb{W}\_2$ 表示 $\mathcal{M}\_{n \times n}(F)$ 中所有對稱矩陣、斜對稱矩陣所成之集合，則 $\mathbb{W}\_1, \mathbb{W}\_2$ 皆為 $\mathcal{M}\_{n \times n}(F)$ 的子空間。亦即，對加法與純量乘法封閉。

### 三角矩陣、對角矩陣

下述兩類矩陣尤為重要，合稱為**三角矩陣（triangular matrix）**。
- **上三角矩陣（upper triangular matrix）**：對角線以下元素全為 $0$（即 $i>j \Rightarrow A\_{ij}=0$），常記作 $U$
- **下三角矩陣（lower triangular matrix）**：對角線以上元素全為 $0$（即 $i<j \Rightarrow A\_{ij}=0$），常記作 $L$

除對角線元素外，其餘皆為 $0$ 的方陣，即滿足 $i \neq j \Rightarrow M\_{ij}=0$ 的 $n \times n$ 矩陣，稱為**對角矩陣（diagonal matrix）**，常記作 $D$。對角矩陣同時屬於上三角與下三角。

上三角矩陣的集合、下三角矩陣的集合、對角矩陣的集合，皆為 $\mathcal{M}\_{m \times n}(F)$ 的子空間。
