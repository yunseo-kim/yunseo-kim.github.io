---
title: "선형변환, 영공간, 상"
description: "선형변환의 정의를 살펴보고, 이와 관련하여 중요한 두 부분공간인 영공간과 상, 그리고 그 둘의 차원(nullity, rank)과 관련한 정리들에 대해 알아본다."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [벡터와 선형결합](/posts/vectors-and-linear-combinations/)
- [벡터공간, 부분공간, 그리고 행렬](/posts/vector-spaces-subspaces-and-matrices/)
- [선형 종속과 선형 독립, 기저와 차원](posts/linear-dependence-and-independence-basis-and-dimension/)
- 일대일함수, 전사함수

## 선형변환

벡터공간의 구조를 보존하는 특별한 함수를 **선형변환(linear transformation)**이라 하며, 이는 순수수학, 응용수학, 사회과학, 자연과학, 그리고 공학을 통틀어 매우 자주 등장하는 중요한 개념이다.

> **정의**  
> $\mathbb{V}$와 $\mathbb{W}$가 $F$-벡터공간이라 하자. 모든 $\mathbf{x}, \mathbf{y} \in \mathbb{V},\ c \in F$에 대하여 다음의 두 조건을 만족하는 함수 $T: \mathbb{V} \to \mathbb{W}$를 $\mathbb{V}$에서 $\mathbb{W}$로 가는 **선형변환(linear transformation)**이라 한다.
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

$T$가 선형변환이라는 말을 간단히 줄여 $T$는 **선형(linear)**이라고도 표현한다. 선형변환 $T: \mathbb{V} \to \mathbb{W}$는 다음의 네 성질을 만족한다.

> 1. $T$가 선형 $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$가 선형 $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$가 선형 $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$가 선형 $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> 어떤 함수가 선형임을 보일 때 보통 2번째 성질을 사용하면 편리하다.
{: .prompt-tip }

> 선형대수학은 기하학에서도 폭넓고 다양하게 사용할 수 있는데, 그 이유는 많은 중요한 기하 변환들이 선형이기 때문이다. 특히 주요한 세 가지 기하 변환인 **회전**, **대칭**, **사영**이 선형변환에 해당한다.
{: .prompt-tip }

다음의 두 가지 선형변환이 특히 자주 등장한다.

> **항등변환과 영변환**  
> $F$-벡터공간 $\mathbb{V}, \mathbb{W}$에 대하여
> - **항등변환(identity transformation)**: 모든 $\mathbf{x} \in \mathbb{V}$에 대하여 $I_\mathbb{V}(\mathbf{x}) = \mathbf{x}$라 정의되는 함수 $I_\mathbb{V}: \mathbb{V} \to \mathbb{V}$
> - **영변환(zero transformation)**: 모든 $\mathbf{x} \in \mathbb{V}$에 대하여 $T_0(\mathbf{x}) = \mathbf{0}$이라 정의되는 함수 $T_0: \mathbb{V} \to \mathbb{W}$
{: .prompt-info }

이 외에도 다양한 개념들이 선형변환에 해당한다.

> **선형변환의 예시**  
> - 회전
> - 대칭
> - 사영
> - [전치](/posts/vector-spaces-subspaces-and-matrices/#전치행렬-대칭행렬-반대칭행렬)
> - 미분가능한 함수의 미분
> - 연속함수의 적분
{: .prompt-tip }

## 영공간과 상

### 영공간과 상의 정의

> **정의**  
> 벡터공간 $\mathbb{V}, \mathbb{W}$와 선형변환 $T: \mathbb{V} \to \mathbb{W}$에 대하여
> - **영공간(null space)** 또는 **핵(kernel)**: $T(\mathbf{x}) = \mathbf{0}$인 $\mathbf{x} \in \mathbb{V}$를 원소로 가지는 집합, $\mathrm{N}(T)$라 표기함
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **치역(range)** 또는 **상(image)**: $T$의 함숫값을 원소로 가지는 $\mathbb{W}$의 부분집합, $\mathrm{R}(T)$라 표기함
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **e.g.** 벡터공간 $\mathbb{V}, \mathbb{W}$와 항등변환 $I: \mathbb{V} \to \mathbb{V}$, 영변환 $T_0: \mathbb{V} \to \mathbb{W}$에 대해 다음이 성립한다.
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T_0) = \mathbb{V}$
> - $\mathrm{R}(T_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

앞으로 계속해서 중요하게 나올 내용인데, 선형변환의 영공간과 상은 벡터공간의 [부분공간](/posts/vector-spaces-subspaces-and-matrices/#부분공간)이다.

> **정리 1**  
> 벡터공간 $\mathbb{V}, \mathbb{W}$와 선형변환 $T: \mathbb{V} \to \mathbb{W}$에 대하여 $\mathrm{N}(T), \mathrm{R}(T)$는 각각 $\mathbb{V}, \mathbb{W}$의 부분공간이다.
>
> **증명**  
> $\mathbb{V}, \mathbb{W}$의 영벡터를 각각 $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$라 표기하자.
>
> $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$이므로 $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$이며, 또한 $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T),\ c \in F$에 대하여 다음이 성립한다.
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}_\mathbb{V} \in \mathrm{N}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{N}(T),\ c\mathbf{x} \in \mathrm{N}(T)$이므로 $\mathrm{N}(T)$는 $\mathbb{V}$의 부분공간이다](/posts/vector-spaces-subspaces-and-matrices/#부분공간).
>
> 마찬가지로, $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$이므로 $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$이며, $\forall \mathbf{x}, \mathbf{y} \in \mathrm{R}(T),\ c \in F \ (\exists \mathbf{v}, \mathbf{w} \in \mathbb{V} \ (T(\mathbf{v}) = \mathbf{x}\ \wedge \ T(\mathbf{w}) = \mathbf{y}))$이므로
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}_\mathbb{W} \in \mathrm{R}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{R}(T),\ c\mathbf{x} \in \mathrm{R}(T)$이므로 $\mathrm{R}(T)$는 $\mathbb{W}$의 부분공간이다](/posts/vector-spaces-subspaces-and-matrices/#부분공간). $\blacksquare$
{: .prompt-info }

한편, 벡터공간 $\mathbb{V}, \mathbb{W}$와 선형변환 $T: \mathbb{V} \to \mathbb{W}$에 대하여 $\mathbb{V}$의 [기저](/posts/linear-dependence-and-independence-basis-and-dimension/#기저) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$을 알 경우, 상 $\mathrm{R}(T)$의 [생성집합](/posts/vectors-and-linear-combinations/#생성)을 다음과 같이 찾을 수 있다.

> **정리 2**  
> 벡터공간 $\mathbb{V}, \mathbb{W}$와 선형변환 $T: \mathbb{V} \to \mathbb{W}$, $\mathbb{V}$의 [기저](/posts/linear-dependence-and-independence-basis-and-dimension/#기저) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$에 대하여 다음이 성립한다.
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **증명**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> $\mathrm{R}(T)$가 부분공간이므로, [벡터공간, 부분공간, 그리고 행렬](/posts/vector-spaces-subspaces-and-matrices/#부분공간)의 **정리 2**에 의해
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> 또한,
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> $\beta$가 $\mathbb{V}$의 기저이므로
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(단, } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> $T$는 선형이므로
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$이고 동시에 $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$이므로, $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

이 정리는 기저 $\beta$가 무한집합일 때에도 성립한다.

### 차원정리

영공간과 상은 매우 중요한 부분공간이므로, [차원](/posts/linear-dependence-and-independence-basis-and-dimension/#차원)에도 이름을 붙여 특별하게 다룬다.

> 벡터공간 $\mathbb{V}, \mathbb{W}$와 선형변환 $T: \mathbb{V} \to \mathbb{W}$에 대하여 $\mathrm{N}(T), \mathrm{R}(T)$가 유한차원이라 하자.
> - **영공간의 차원(nullity)**: $\mathrm{N}(T)$의 차원, $\mathrm{nullity}(T)$라 표기함
> - **계수(rank)**: $\mathrm{R}(T)$의 차원, $\mathrm{rank}(T)$라 표기함
{: .prompt-info }

선형변환에서 영공간의 차원이 커질수록 계수는 작아지고, 반대로 계수가 커질수록 영공간의 차원은 작아진다.

> **정리 3: 차원정리(dimension theorem)**  
> 벡터공간 $\mathbb{V}, \mathbb{W}$와 선형변환 $T: \mathbb{V}\to \mathbb{W}$에 대하여 $\mathbb{V}$가 유한차원이면 다음이 성립한다.
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### 증명

$\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$라 하고, $\mathrm{N}(T)$의 기저를 $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$라 하자.

["선형 종속과 선형 독립, 기저와 차원"의 **따름정리 6-1**](/posts/linear-dependence-and-independence-basis-and-dimension/#부분공간의-차원)에 따라, $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$를 확장하여 $\mathbb{V}$의 기저 $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$을 얻을 수 있다.

이제, $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$이 $\mathrm{R}(T)$의 기저임을 보일 것이다. 우선 $1 \leq i \leq k$일 때 $T(\mathbf{v}_i) = 0$이므로, [**정리 2**](#영공간과-상의-정의)에 의해

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

즉, $S$는 $\mathrm{R}(T)$의 생성집합이다. 이제 [**대체정리의 따름정리 5-2**](/posts/linear-dependence-and-independence-basis-and-dimension/#차원)에 따라, $S$가 선형독립임을 보이면 $S$가 $\mathrm{R}(T)$의 기저임을 증명할 수 있다.

$\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (단, $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$)라 하면, $T$가 선형이므로

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

따라서,

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

$\beta$가 $\mathbb{V}$의 기저이니, $\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$의 유일한 해는

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

이고, 이로부터

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

즉, $S$는 선형독립이며, $\mathrm{R}(T)$의 기저이다.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### 선형변환과 일대일함수, 전사함수

선형변환에서 일대일함수(injection)와 전사함수(surjection)는 계수, 영공간의 차원과 밀접한 관련이 있다.

> **정리 4**  
> 벡터공간 $\mathbb{V}, \mathbb{W}$와 선형변환 $T: \mathbb{V} \to \mathbb{W}$에 대하여
>
> $$ T\text{는 일대일함수이다.} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **정리 5**  
> 유한차원 벡터공간 $\mathbb{V}, \mathbb{W}$의 차원이 같을 때, 선형변환 $T: \mathbb{V} \to \mathbb{W}$에 대하여 다음 네 명제는 동치이다.
> 1. $T$는 일대일함수이다.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$는 전사함수이다.
{: .prompt-info }

[차원정리](#차원정리)와 [선형변환의 성질 1, 3](#선형변환), 그리고 ["선형 종속과 선형 독립, 기저와 차원"의 **정리 6**](/posts/linear-dependence-and-independence-basis-and-dimension/#부분공간의-차원)을 이용하여 **정리 4**와 **정리 5**를 증명할 수 있다.

이 두 정리는 주어진 선형변환이 일대일함수 또는 전사함수인지 판별할 때 유용하다.

> 무한차원 벡터공간 $\mathbb{V}$와 선형변환 $T: \mathbb{V} \to \mathbb{V}$에 대해서는, 단사와 전사는 동치가 아니다.
{: .prompt-warning }

또한 어떤 선형변환이 일대일함수라면, 경우에 따라선 주어진 벡터공간의 부분집합이 선형독립인지를 판별할 때 다음의 정리가 유용할 수 있다.

> **정리 6**  
> 벡터공간 $\mathbb{V}, \mathbb{W}$와 일대일함수인 선형변환 $T: \mathbb{V} \to \mathbb{W}$, 그리고 $\mathbb{V}$의 부분집합 $S$에 대하여 다음이 성립한다.
>
> $$ S\text{가 선형독립이다.} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \}\text{가 선형독립이다.} $$
>
{: .prompt-info }

## 선형변환과 기저

선형변환의 중요한 특성은, 기저에 따라 선형변환이 어떻게 행동하는지가 결정된다는 것이다.

> **정리 7**  
> $F$-벡터공간 $\mathbb{V}, \mathbb{W}$와 $\mathbb{V}$의 기저 $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$, 그리고 벡터 $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$에 대하여 다음 조건을 만족하는 선형변환 $T: \mathbb{V} \to \mathbb{W}$가 유일하게 존재한다.
>
> $$ i = 1, 2, \dots, n \text{에 대하여 } T(\mathbf{v}_i) = \mathbf{w}_i $$
>
> **증명**  
> $\mathbf{x} \in \mathbb{V}$에 대하여 다음 선형결합 표현은 유일하다.
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ (}a_1, a_2, \dots, a_n \in F \text{)} $$
>
> 선형변환 $T: \mathbb{V} \to \mathbb{W}$를
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> 로 놓자.
>
> i) $i = 1, 2, \dots, n$에 대하여 $T(\mathbf{v}_i) = \mathbf{w}_i$.
>
> ii)
>
> 또다른 선형변환 $U: \mathbb{V} \to \mathbb{W}$가 $i = 1, 2, \dots, n$에 대하여 $U(\mathbf{v}\_i) = \mathbf{w}\_i$를 만족한다고 가정하면, $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$에 대하여
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i) $$
>
> $$ \therefore U = T. $$
>
> i), ii)에 의해, $i = 1, 2, \dots, n$에 대하여 $T(\mathbf{v}\_i) = \mathbf{w}\_i$인 선형변환은
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> 로 유일하다. $\blacksquare$
>
> **따름정리 7-1**  
> 두 벡터공간 $\mathbb{V}, \mathbb{W}$에 대하여 $\mathbb{V}$가 유한집합인 기저 $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$을 포함한다고 할 때, 두 선형변환 $U, T: \mathbb{V} \to \mathbf{W}$가 $i = 1, 2, \dots, n$에 대해 $U(\mathbf{v}_i) = T(\mathbf{v}_i)$를 만족하면 $U = T$이다.  
> 즉, <u>기저에서 함숫값이 같으면 같은 선형변환이다.</u>
{: .prompt-info }
