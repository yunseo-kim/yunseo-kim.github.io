---
title: "벡터공간, 부분공간, 그리고 행렬"
description: "벡터공간과 부분공간의 정의를 중심으로 행렬공간과 함수공간 등 대표적인 벡터공간의 예시들을 다룬다. 특히 행렬공간에 집중하여, 임의의 크기의 행렬공간에 대해 중요한 유형의 부분공간을 이루는 대칭·반대칭행렬, 상삼각·하삼각·대각행렬을 정리한다."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **행렬(matrix)**
>   - 행렬 $A$의 $i$행 $j$열 성분을 $A\_{ij}$ 또는 $a\_{ij}$로 표기함
>   - **대각성분(diagonal entry)**: $i=j$인 성분 $a\_{ij}$
>   - 성분 $a\_{i1}, a\_{i2}, \dots, a\_{in}$을 이 행렬의 $i$번째 **행(row)**이라 함
>     - 행렬의 각 행은 $F^n$의 벡터로 나타낼 수 있음
>     - 더 나아가, $F^n$의 행벡터를 $1 \times n$의 또다른 행렬로 나타낼 수 있음
>   - 성분 $a\_{1j}, a\_{2j}, \dots, a\_{mj}$를 이 행렬의 $j$번째 **열(column)**이라 함
>     - 행렬의 각 열은 $F^m$의 벡터로 나타낼 수 있음
>     - 더 나아가, $F^m$의 열벡터를 $m \times 1$의 또다른 행렬로 나타낼 수 있음
>   - **영행렬(zero matrix)**: 모든 성분이 $0$인 행렬, $O$로 표기함
>   - **정사각행렬(square matrix)**: 행의 개수와 열의 개수가 같은 행렬
>   - 두 $m \times n$ 행렬 $A, B$에서 모든 $1 \leq i \leq m$, $1 \leq j \leq n$에 대하여 $A\_{ij} = B_{ij}$이면(즉, 대응하는 성분이 모두 일치하면) 두 행렬이 **같다**($A=B$)고 정의함
>   - **전치행렬(transpose matrix)**: $m \times n$ 행렬 $A$에 대해, $A$의 행과 열을 뒤바꾼 $n \times m$ 행렬 $A^T$을 전치행렬이라고 함
>   - **대칭행렬(symmetric matrix)**: $A^T = A$인 정사각행렬 $A$
>   - **반대칭행렬(skew-symmetric matrix)**: $B^T = -B$인 정사각행렬 $B$
>   - **삼각행렬(triangular matrix)**
>     - **상삼각행렬(upper triangular matrix)**: 대각성분 아래의 모든 성분이 $0$인 행렬(즉, $i>j \Rightarrow A\_{ij}=0$인 행렬), 보통 $U$로 표기
>     - **하삼각행렬(lower triangular matrix)**: 대각성분 위의 모든 성분이 $0$인 행렬(즉, $i<j \Rightarrow A\_{ij}=0$인 행렬), 보통 $L$로 표기
>   - **대각행렬(diagonal matrix)**: 대각성분을 제외한 모든 성분이 $0$인 정사각행렬(즉, $i \neq j \Rightarrow M\_{ij}=0$인 $n \times n$ 행렬), 보통 $D$로 표기
> - 대표적인 벡터공간들
>   - **n 순서쌍 $F^n$**:
>     - 체 $F$에서 성분을 가져온 모든 $n$ 순서쌍의 집합
>     - $F^n$이라 표기하며, $F$-벡터공간임
>   - **행렬공간(matrix space)**:
>     - 성분이 체 $F$의 원소인 모든 $m \times n$ 행렬의 집합
>     - $\mathcal{M}\_{m \times n}(F)$라 표기하며, 벡터공간임
>   - **함수공간(function space)**:
>     - 체 $F$의 공집합이 아닌 집합 $S$에 대해, $S$에서 $F$로 가는 모든 함수의 집합
>     - $\mathcal{F}(S,F)$라 표기하며, 벡터공간임
> - **부분공간(subspace)**
>   - $F$-벡터공간 $\mathbb{V}$의 부분집합 $\mathbb{W}$가 $\mathbb{V}$에서 정의한 합과 스칼라배를 동일하게 가지는 $F$-벡터공간일 때, $\mathbb{W}$는 $\mathbb{V}$의 **부분공간(subspace)**이라 정의함
>   - 모든 벡터공간 $\mathbb{V}$에 대해 $\mathbb{V}$ 자기 자신과 $\\{0\\}$은 부분공간이며, 특히 $\\{0\\}$은 **점 부분공간(zero subspace)**이라 함
>   - 벡터공간의 어떤 부분집합이 영벡터를 원소로 가지며 [선형결합](/posts/vectors-and-linear-combinations/#벡터의-선형-결합)에 대해 닫혀 있으면($\mathrm{span}(\mathbb{W})=\mathbb{W}$이면), 그 집합은 부분공간임
{: .prompt-info }

## Prerequisites
- [벡터와 선형결합](/posts/vectors-and-linear-combinations/)

## 벡터공간

[벡터와 선형결합](/posts/vectors-and-linear-combinations/#넓은-의미의-벡터-벡터-공간의-원소)에서도 잠깐 보았듯, 대수적 구조로서의 벡터와 벡터공간의 정의는 다음과 같다.

> **정의**  
> 체 $F$에서의 **벡터공간(vector space)** 또는 **선형공간(linear space)** $\mathbb{V}$는 다음 8가지 조건을 만족하는 두 연산, **합**과 **스칼라배**를 가지는 집합이다. 체 $F$의 원소를 **스칼라(scalar)**, 벡터공간 $\mathbb{V}$의 원소를 **벡터(vector)**라 한다.
>
> - **합(sum)**: $\mathbb{V}$의 두 원소 $\mathbf{x}, \mathbf{y}$에 대하여 유일한 원소 $\mathbf{x} + \mathbf{y} \in \mathbb{V}$를 대응하는 연산이다. 이때 $\mathbf{x} + \mathbf{y}$를 $\mathbf{x}$와 $\mathbf{y}$의 **합**이라 한다.
> - **스칼라배(scalar multiplication)**: 체 $F$의 원소 $a$와 벡터공간 $\mathbb{V}$의 원소 $\mathbf{x}$마다 유일한 원소 $a\mathbf{x} \in \mathbb{V}$를 대응하는 연산이다. 이때 $a\mathbf{x}$를 $\mathbf{x}$의 **스칼라배(scalar multiple)**라 한다.
>
> 1. 모든 $\mathbf{x},\mathbf{y} \in \mathbb{V}$에 대하여 $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$이다. (덧셈에 대한 교환법칙)
> 2. 모든 $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$에 대하여 $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$이다. (덧셈에 대한 결합법칙)
> 3. 모든 $\mathbf{x} \in \mathbb{V}$에 대하여 $\mathbf{x} + \mathbf{0} = \mathbf{x}$인 $\mathbf{0} \in \mathbb{V}$가 존재한다. (영벡터, 덧셈에 대한 항등원)
> 4. 각 $\mathbf{x} \in \mathbb{V}$마다 $\mathbf{x}+\mathbf{y}=\mathbf{0}$인 $\mathbf{y} \in \mathbb{V}$가 존재한다. (덧셈에 대한 역원)
> 5. 각 $\mathbf{x} \in \mathbb{V}$에 대하여 $1\mathbf{x} = \mathbf{x}$이다. (곱셈에 대한 항등원)
> 6. 모든 $a,b \in F$와 모든 $\mathbf{x} \in \mathbb{V}$에 대하여 $(ab)\mathbf{x} = a(b\mathbf{x})$이다. (스칼라배에 대한 결합법칙)
> 7. 모든 $a \in F$와 모든 $\mathbf{x},\mathbf{y} \in \mathbb{V}$에 대하여 $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$이다. (덧셈에 대한 스칼라배의 분배법칙 1)
> 8. 모든 $a,b \in F$와 모든 $\mathbf{x},\mathbf{y} \in \mathbb{V}$에 대하여 $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$이다. (덧셈에 대한 스칼라배의 분배법칙 2)
{: .prompt-info }

벡터공간은 정확하게는 '$F$-벡터공간 $\mathbb{V}$'라 표기해야 하나, 벡터공간을 다룰 때 체는 크게 중요한 요소는 아니므로 혼란의 여지가 없으면 체 $F$는 생략하고 '벡터공간 $\mathbb{V}$'라 적는다.

### 행렬공간

#### 행벡터와 열벡터

체 $F$에서 성분을 가져온 모든 $n$ 순서쌍의 집합을 $F^n$이라 표기한다. $u = (a_1, a_2, \dots, a_n) \in F^n$, $v = (b_1, b_2, \dots, b_n) \in F^n$일 때, 합과 스칼라곱을 다음과 같이 정의하면 $F^n$은 $F$-벡터공간이다.

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

$F^n$의 벡터는 단독으로 쓸 때는 보통 **행벡터(row vector)** $(a_1, a_2, \dots, a_n)$보다는 **열벡터(column vector)**

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

로 표현한다.

> 다만 이렇게 열벡터로 표기할 때 공간을 많이 차지하다 보니, [전치](#전치행렬-대칭행렬-반대칭행렬)를 써서 $(a_1, a_2, \dots, a_n)^T$로 나타내기도 한다.
{: .prompt-tip }

#### 행렬과 행렬공간

한편, $F$에서 성분을 가져온 $m \times n$ **행렬(matrix)**은 다음과 같은 직사각형 모양의 배열로, 이탤릭 대문자($A, B, C$ 등)로 나타낸다.

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- 행렬 $A$의 $i$행 $j$열 성분을 $A\_{ij}$ 또는 $a\_{ij}$로 표기한다.
- 모든 $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$)는 $F$의 원소이다.
- $i=j$인 성분 $a\_{ij}$를 이 행렬의 **대각성분(diagonal entry)**이라 한다.
- 성분 $a\_{i1}, a\_{i2}, \dots, a\_{in}$을 이 행렬의 $i$번째 **행(row)**이라 한다. 행렬의 각 행은 $F^n$의 벡터로 나타낼 수 있으며, 더 나아가 $F^n$의 행벡터를 $1 \times n$의 또다른 행렬로 나타낼 수 있다.
- 성분 $a\_{1j}, a\_{2j}, \dots, a\_{mj}$를 이 행렬의 $j$번째 **열(column)**이라 한다. 행렬의 각 열은 $F^m$의 벡터로 나타낼 수 있으며, 더 나아가 $F^m$의 열벡터를 $m \times 1$의 또다른 행렬로 나타낼 수 있다.
- 모든 성분이 $0$인 $m \times n$ 행렬을 **영행렬(zero matrix)**이라 하며 $O$로 표기한다.
- 행의 개수와 열의 개수가 같은 행렬을 **정사각행렬(square matrix)**이라 한다.
- 두 $m \times n$ 행렬 $A, B$에서 모든 $1 \leq i \leq m$, $1 \leq j \leq n$에 대하여 $A\_{ij} = B_{ij}$이면(즉, 대응하는 성분이 모두 일치하면) 두 행렬이 **같다**($A=B$)고 정의한다.

성분이 체 $F$의 원소인 모든 $m \times n$ 행렬의 집합을 $\mathcal{M}\_{m \times n}(F)$라 표기한다. $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F),\ c \in F$일 때, 합과 스칼라배를 다음과 같이 정의하면 $\mathcal{M}\_{m \times n}(F)$는 벡터공간이며, 이를 **행렬공간(matrix space)**이라고 한다.

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(단, }1 \leq i \leq &m, 1 \leq j \leq n \text{)}
\end{align*} $$

이는 $F^n$과 $F^m$에서 정의한 연산을 자연스럽게 확장한 것이다.

### 함수공간

체 $F$의 공집합이 아닌 집합 $S$에 대해, $\mathcal{F}(S,F)$는 $S$에서 $F$로 가는 모든 함수의 집합이다. $\mathcal{F}(S,F)$에서 모든 $s \in S$에 대하여 $f(s) = g(s)$일 때 두 함수 $f, g$는 **같다**($f=g$)고 한다.

$f,g \in \mathcal{F}(S,F),\ c \in F,\ s \in S$일 때, 합과 스칼라배를 다음과 같이 정의하면 $\mathcal{F}(S,F)$는 벡터공간이며, 이를 **함수공간(function space)**이라고 한다.

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## 부분공간

> **정의**  
> $F$-벡터공간 $\mathbb{V}$의 부분집합 $\mathbb{W}$가 $\mathbb{V}$에서 정의한 합과 스칼라배를 동일하게 가지는 $F$-벡터공간일 때, $\mathbb{W}$는 $\mathbb{V}$의 **부분공간(subspace)**이라 한다.
{: .prompt-info }

모든 벡터공간 $\mathbb{V}$에 대해 $\mathbb{V}$ 자기 자신과 $\\{0\\}$은 부분공간이며, 특히 $\\{0\\}$은 **점 부분공간(zero subspace)**이라 한다.

어떤 부분집합이 부분공간인지는 다음 정리를 이용해 확인할 수 있다.

> **정리**  
> 벡터공간 $\mathbb{V}$와 부분집합 $\mathbb{W}$에 대해, $\mathbb{W}$가 $\mathbb{V}$의 부분공간이기 위한 필요충분조건은 다음 3가지 조건을 만족하는 것이다. 이때 연산은 $\mathbb{V}$에서 정의한 것과 같다.
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> 간단히 말해, 영벡터를 원소로 가지며 [선형결합](/posts/vectors-and-linear-combinations/#벡터의-선형-결합)에 대해 닫혀 있으면($\mathrm{span}(\mathbb{W})=\mathbb{W}$이면) 부분공간이다.
{: .prompt-info }

또한 다음의 정리들이 성립한다.

> **정리**  
> - 벡터공간 $\mathbb{V}$의 임의의 부분집합 $S$의 생성공간 $\mathrm{span}(S)$는 $S$를 포함하는 $\mathbb{V}$의 부분공간이다.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - $S$를 포함하는 $\mathbb{V}$의 부분공간은 반드시 $S$의 생성공간을 포함한다.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **정리**  
> 벡터공간 $\mathbb{V}$의 부분공간들에 대해, 이 부분공간들의 임의의 교집합은 마찬가지로 $\mathbb{V}$의 부분공간이다.
{: .prompt-info }

### 전치행렬, 대칭행렬, 반대칭행렬

$m \times n$ 행렬 $A$의 **전치행렬(transpose matrix)** $A^T$는 $A$의 행과 열을 뒤바꾼 $n \times m$ 행렬이다.

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

$A^T = A$인 행렬 $A$를 **대칭행렬(symmetric matrix)**, $B^T = -B$인 행렬 $B$를 **반대칭행렬(skew-symmetric matrix)**이라 한다. 대칭행렬과 반대칭행렬은 반드시 정사각행렬이어야 한다.

각각 $\mathcal{M}\_{n \times n}(F)$의 모든 대칭행렬, 반대칭행렬을 원소로 하는 두 집합 $\mathbb{W}\_1, \mathbb{W}\_2$는 $\mathcal{M}\_{n \times n}(F)$의 부분공간이다. 즉, $\mathbb{W}\_1, \mathbb{W}\_2$는 합과 스칼라곱에 대해 닫혀 있다.

### 삼각행렬, 대각행렬

이 두 종류의 행렬도 특히 중요하다. 

우선, 다음 두 종류의 행렬을 묶어 **삼각행렬(triangular matrix)**이라 한다.
- **상삼각행렬(upper triangular matrix)**: 대각성분 아래의 모든 성분이 $0$인 행렬(즉, $i>j \Rightarrow A\_{ij}=0$인 행렬), 보통 $U$로 표기
- **하삼각행렬(lower triangular matrix)**: 대각성분 위의 모든 성분이 $0$인 행렬(즉, $i<j \Rightarrow A\_{ij}=0$인 행렬), 보통 $L$로 표기

대각성분을 제외한 모든 성분이 $0$인 정사각행렬, 즉 $i \neq j \Rightarrow M\_{ij}=0$인 $n \times n$ 행렬을 **대각행렬(diagonal matrix)**이라 하며 보통 $D$로 표기한다. 대각행렬은 상삼각행렬인 동시에 하삼각행렬이다.

상삼각행렬의 집합, 하삼각행렬의 집합, 대각행렬의 집합은 모두 $\mathcal{M}\_{m \times n}(F)$의 부분공간이다.
