---
title: "벡터와 선형결합"
description: "벡터란 무엇인지와 기본 연산(상수배, 덧셈)을 알아보고, 이를 바탕으로 벡터의 선형 결합을 이해한다."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **벡터의 정의**
>   - **좁은 의미의 벡터(유클리드 벡터)**: 크기와 방향을 함께 갖는 물리량
>   - **넓은 의미의, 선형대수학에서의 벡터**: 벡터공간의 원소
> - **벡터의 표현법**
>   - **화살표 표현법**: 벡터의 크기는 화살표의 길이로, 벡터의 방향은 화살표의 방향으로 나타냄. 시각화하기 용이하고 직관적이라는 장점이 있으나, 4차원 이상의 고차원 벡터나 비유클리드 벡터는 표현하기 곤란함.
>   - **성분 표현법**: 벡터의 시점을 좌표공간의 원점으로 놓고, 종점의 좌표로 벡터를 표현하는 방법.
> - **벡터의 기본 연산**
>   - **합**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **스칼라 곱**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **벡터의 선형 결합**
>   - 유한 개의 벡터 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$과 스칼라 $a_1, a_2, \dots, a_n$에 대하여, $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$인 벡터 $\mathbf{v}$를 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$의 **선형 결합(linear combination)**이라고 함
>   - 이때 $a_1, a_2, \dots, a_n$을 이 선형 결합의 **계수(coefficient)**라고 함
{: .prompt-info }

## Prerequisites
- 좌표평면/좌표공간
- 체(field)

## 벡터란 무엇인가?

### 좁은 의미의 벡터: 유클리드 벡터

> 힘, 속도, 가속도 등 많은 물리량은 크기뿐만 아니라 방향 정보를 함께 가진다. 이처럼 크기와 방향을 모두 가진 물리량을 **벡터(vector)**라고 한다.
{: .prompt-info }

위의 정의가 물리학의 역학이나 고등학교 수준 수학에서 다루던 벡터의 정의이다. 이와 같이 '유향선분의 크기와 방향'이라는 기하학적인 의미를 지닌, 물리적 직관에 기반한 좁은 의미의 벡터를 엄밀히는 **유클리드 벡터(Euclidean vector)**라고 한다.

### 넓은 의미의 벡터: 벡터 공간의 원소

선형대수학에서는 위의 유클리드 벡터의 정의보다 넓은 의미를 지닌, 보다 추상적인 대수적 구조로서 벡터를 다음과 같이 정의한다.

> **정의**  
> 체 $F$에서의 **벡터공간(vector space)** 또는 **선형공간(linear space)** $V$는 다음 8가지 조건을 만족하는 두 연산, **합**과 **스칼라 곱**을 가지는 집합이다. 체 $F$의 원소를 **스칼라(scalar)**, 벡터공간 $V$의 원소를 **벡터(vector)**라 한다.
>
> - **합(sum)**: $V$의 두 원소 $x, y$에 대하여 유일한 원소 $x + y \in V$를 대응하는 연산이다. 이때 $x + y$를 $x$와 $y$의 **합**이라 한다.
> - **스칼라 곱(scalar multiplication)**: 체 $F$의 원소 $a$와 벡터공간 $V$의 원소 $x$마다 유일한 원소 $ax \in V$를 대응하는 연산이다. 이때 $ax$를 $a$와 $x$의 스칼라 **곱(product)**이라 한다.
>
> 1. 모든 $x,y \in V$에 대하여 $x + y = y + x$이다. (덧셈에 대한 교환법칙)
> 2. 모든 $x,y,z \in V$에 대하여 $(x+y)+z = x+(y+z)$이다. (덧셈에 대한 결합법칙)
> 3. 모든 $x \in V$에 대하여 $x + 0 = x$인 $0 \in V$가 존재한다. (영벡터, 덧셈에 대한 항등원)
> 4. 각 $x \in V$마다 $x+y=0$인 $y \in V$가 존재한다. (덧셈에 대한 역원)
> 5. 각 $x \in V$에 대하여 $1x = x$이다. (곱셈에 대한 항등원)
> 6. 모든 $a,b \in F$와 모든 $x \in V$에 대하여 $(ab)x = a(bx)$이다. (스칼라 곱에 대한 결합법칙)
> 7. 모든 $a \in F$와 모든 $x,y \in V$에 대하여 $a(x+y) = ax + ay$이다. (덧셈에 대한 스칼라 곱의 분배법칙 1)
> 8. 모든 $a,b \in F$와 모든 $x,y \in V$에 대하여 $(a+b)x = ax + bx$이다. (덧셈에 대한 스칼라 곱의 분배법칙 2)
{: .prompt-info }

이러한 선형대수학에서의 벡터의 정의는 앞서 언급한 [유클리드 벡터](#좁은-의미의-벡터-유클리드-벡터)까지 포괄하는 보다 넓은 범위의 정의이다. [유클리드 벡터](#좁은-의미의-벡터-유클리드-벡터)도 위의 8가지 성질을 만족함을 확인할 수 있다.

벡터의 기원과 발전 과정은 물리학에서 제기한 여러 실용적인 문제들, 가령 힘이나 물체의 운동, 회전, 장과 같은 개념들을 정량적으로 기술하려는 시도와 밀접하게 연관되어 있다. 자연현상을 수학적으로 표현하기 위한 물리학적 필요에 의해 처음에 [유클리드 벡터](#좁은-의미의-벡터-유클리드-벡터)로 벡터의 개념이 처음 제시되었고, 이후 수학이 이러한 물리적 개념을 일반화하고 이론화하는 과정에서 벡터 공간, 내적, 외적 등의 형식적 구조를 정립하여 지금의 벡터의 정의를 이루게 된다. 즉 벡터는 물리학이 요구하고 수학이 정립한 개념으로, 순수 수학만의 산물이라기보다는 수학계와 물리학계가 긴밀히 교류하며 발전시켜 온 학제 간 산물이라 할 수 있다.

고전적인 역학에서 다루던 [유클리드 벡터](#좁은-의미의-벡터-유클리드-벡터)는 수학적으로 [보다 일반화된 틀](#넓은-의미의-벡터-벡터-공간의-원소)로 표현할 수 있으며, 오늘날 물리학에서는 [유클리드 벡터](#좁은-의미의-벡터-유클리드-벡터)뿐만 아니라 벡터 공간, 함수 공간 등 수학에서 정의한 보다 추상적인 개념들도 적극적으로 활용하여 물리적인 의미를 부여한다. 따라서 벡터에 대한 두 정의를 단순히 '물리학적 정의', '수학적 정의'로 이해하는 것은 부적절하다.

벡터공간에 대해서는 나중에 더 알아보기로 하고, 우선은 좌표공간 상에서 기하학적으로 표현 가능한 좁은 의미의 벡터, 유클리드 벡터에 집중한다. 직관적인 유클리드 벡터의 예시를 먼저 살펴보는 것은 추후 그 외의 다른 벡터들로 일반화할 때에도 이해에 도움이 된다.

## 벡터의 표현법
### 화살표 표현법

기하학적인 직관을 가장 잘 살린, 흔히 볼 수 있는 표현법이다. 벡터의 크기는 화살표의 길이로, 벡터의 방향은 화살표의 방향으로 나타낸다.

![Euclidean Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *이미지 출처*
> - 저작자: 위키피디아 유저 [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

이러한 표현법은 직관적이긴 하나, 4차원 이상의 고차원 벡터에 대해서는 이러한 화살표 표현법은 한계가 명확하다. 뿐만 아니라, 나중에 가서는 애초에 기하학적으로 표현하기 곤란한 비유클리드 벡터들도 다뤄야 하기 때문에 후술할 성분 표현법에 익숙해질 필요가 있다.

### 성분 표현법

벡터가 어디에 위치했는지와 무관하게 크기와 방향이 같으면 동일한 벡터로 생각한다. 따라서 어떤 좌표공간이 주어졌을 때, 벡터의 시점을 해당 좌표공간의 원점으로 고정하면 <u>$n$차원 벡터는 $n$차원 공간상의 임의의 점에 대응</u>하며, 이 경우 종점의 좌표로 벡터를 표현할 수 있다. 이와 같은 표현법을 벡터의 **성분 표현법**이라고 한다.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ or } \mathbb{C}^n $$

![Position vector](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *이미지 출처*
> - 저작자: 위키미디어 유저 [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## 벡터의 기본 연산

벡터의 기본 연산은 **합**과 **스칼라곱** 두 가지이다. 모든 벡터 연산은 이 두 가지 기본 연산의 조합으로 표현할 수 있다.

### 벡터의 합

두 벡터의 합은 마찬가지로 벡터이며, 이때 합성벡터의 성분들은 두 벡터의 성분들끼리 각각 더한 것과 같다.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### 벡터의 스칼라곱

벡터는 크기를 확대하거나 축소할 수 있으며, 이를 벡터에 상수(스칼라)를 곱하는 스칼라 곱이라는 연산으로 나타낸다. 어떤 벡터에 상수배를 한 결과물은 각각의 성분에 상수배를 한 것과 같다.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Scalar multiplication of vectors](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *이미지 출처*
> - 저작자: 위키피디아 유저 [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## 벡터의 선형 결합

미적분학이 수 $x$와 함수 $f(x)$로부터 출발하듯, 선형대수학은 벡터 $\mathbf{v}, \mathbf{w}, \dots$와 선형 결합 $c\mathbf{v} + d\mathbf{w} + \cdots$로부터 출발한다. 그리고 벡터들의 모든 선형 결합은 위의 두 기본 연산, [합](#벡터의-합)과 [스칼라곱](#벡터의-스칼라곱)의 조합으로 구성된다.

> 유한 개의 벡터 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$과 스칼라 $a_1, a_2, \dots, a_n$에 대하여 다음을 만족하는 벡터 $\mathbf{v}$는 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$의 **선형 결합(linear combination)**이라 한다.
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> 이때, $a_1, a_2, \dots, a_n$을 이 선형 결합의 **계수(coefficient)**라고 한다.
{: .prompt-info }

그렇다면 이러한 선형 결합이 왜 중요한가? 다음과 같이 **$m$차원 공간 상의 벡터 $n$개가 $m \times n$ 행렬의 $n$개 열을 이루는 상황**을 생각해 보자.

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

여기서 핵심은 다음의 두 가지이다.

1. **모든 가능한 선형 결합 $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots x_n\mathbf{v}_n$을 표현해 보라.** 무엇을 이루는가?
2. 원하는 출력 벡터 $Ax = b$를 만들어 내는 **수 $x_1, x_2, \dots, x_n$을 찾아라.**

두 번째 질문에 대한 답은 나중에 다시 알아볼 것이며, 일단 지금은 첫 번째 질문에 집중하자. 논의를 간단하게 하기 위해, $0$벡터가 아닌 2차원($m=2$) 벡터 2개($n=2$)의 경우를 예시로 살펴보자. 

### 선형 결합 $c\mathbf{v} + d\mathbf{w}$

2차원 공간 상의 벡터 $\mathbf{v}$는 2개의 성분을 가진다. 모든 스칼라 $c$에 대하여, <u>벡터 $c\mathbf{v}$는 원래의 벡터 $\mathbf{v}$와 평행하고 원점을 지나는 $xy$ 평면 상의 무한히 긴 직선을 이룬다.</u>

여기서 주어진 두 번째 벡터 $\mathbf{w}$가 이 직선 위에 있지 않다면(벡터 $\mathbf{v}$와 $\mathbf{w}$가 평행하지 않다면), 벡터 $d\mathbf{w}$는 또다른 두 번째 직선을 이룬다. 이제 이 두 직선을 조합해 보면, **선형 결합 $c\mathbf{v} + d\mathbf{w}$는 원점을 포함하는 하나의 평면을 이룬다**는 것을 알 수 있다.

![Linear combinations of two vectors](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *이미지 출처*
> - 저작자: 위키미디어 유저 [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - 라이선스: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

이처럼 벡터들의 선형 결합은 곧 벡터공간을 이루며, 이를 공간 **생성(span)**이라고 한다. 아직 벡터공간의 개념을 정확히 알아보지는 않았으나, 지금의 이 예시를 떠올리면 추후 벡터공간의 개념을 이해하는 데도 도움이 된다.
