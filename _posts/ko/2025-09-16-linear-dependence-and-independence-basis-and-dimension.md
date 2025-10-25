---
title: "선형 종속과 선형 독립, 기저와 차원"
description: "선형 종속과 선형 독립, 그리고 벡터공간의 기저와 차원의 개념을 정리한다."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [벡터와 선형결합](/posts/vectors-and-linear-combinations/)
- [벡터공간, 부분공간, 그리고 행렬](/posts/vector-spaces-subspaces-and-matrices/)

## 선형 종속과 선형 독립

어떤 [벡터공간](/posts/vector-spaces-subspaces-and-matrices/#벡터공간) $\mathbb{V}$와 [부분공간](/posts/vector-spaces-subspaces-and-matrices/#부분공간) $\mathbb{W}$에 대해, $\mathbb{W}$를 [생성](/posts/vectors-and-linear-combinations/#선형-결합-cmathbfv--dmathbfw)하는 가능한 작은 유한 부분집합 $S$를 찾고 싶다고 하자.

집합 $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$에 대하여 $\mathrm{span}(S) = \mathbb{W}$라 할 때, $\mathbb{W}$를 생성하는 $S$의 진부분집합이 존재하지는 않는지 판별하려면 어떻게 해야 할까? 이는 $S$에서 꺼낸 한 벡터가 다른 벡터들의 [선형결합](/posts/vectors-and-linear-combinations/#벡터의-선형-결합)으로 표현 가능한지 판별하는 문제와 같다. 예를 들어, $\mathbf{u}_4$를 나머지 세 벡터의 선형결합으로 표현하기 위한 필요충분조건은 다음 조건을 만족하는 스칼라 $a_1, a_2, a_3$가 존재하는 것이다.

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

하지만 $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ 각각에 대해 매번 이런 식으로 연립일차방정식을 세워서 해가 존재하는지 확인하려면 번거로우므로, 식을 살짝 변경해 보자.

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

만약 $S$의 어떤 벡터가 다른 벡터들의 선형결합이면, 위와 같이 영벡터를 $S$의 선형결합으로 표현할 때 계수 $a_1, a_2, a_3, a_4$ 중 하나 이상이 $0$이 아닌 표현이 존재한다. 이 명제의 역 또한 참으로, 계수 $a_1, a_2, a_3, a_4$ 중 하나 이상이 $0$이 아니면서 영벡터를 $S$의 원소 벡터들의 선형결합으로 표현하는 방법이 존재한다면 $S$의 어떤 벡터는 다른 벡터들의 선형결합이다.

이를 일반화하여, 다음과 같이 **선형종속**과 **선형독립**을 정의한다.

> **정의**  
> 벡터공간 $\mathbb{V}$의 부분집합 $S$에 대하여 $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$을 만족하는 유한개의 서로 다른 벡터 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$와 적어도 하나가 $0$이 아닌 스칼라 $a_1, a_2, \dots, a_n$이 존재하면 집합 $S$ 및 그 벡터들은 **선형종속(linearly dependent)**이라 한다. 그렇지 않은 경우는 **선형독립(linearly independent)**이라 한다.
{: .prompt-info }

임의의 벡터 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$에 대하여 $a_1 = a_2 = \cdots = a_n = 0$이면 $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$이며, 이를 **영벡터의 자명한 표현(trivial representation of $\mathbf{0}$)**이라 한다.

선형독립인 집합에 대한 다음의 세 명제가 모든 벡터공간에서 항상 참이다. 특히 **명제 3**은 앞서 본 것처럼 어떤 유한집합이 선형독립인지 판정할 때 매우 유용하다.

> - **명제 1**: 공집합은 선형독립이다. 어떤 집합이 선형종속이기 위해서는 공집합이 아니어야 한다.
> - **명제 2**: 영이 아닌 벡터 하나로 이루어진 집합은 선형독립이다.
> - **명제 3**: 어떤 집합이 선형독립이기 위한 필요충분조건은 $\mathbf{0}$을 주어진 집합에 대한 선형결합으로 표현하는 방법이 자명한 표현뿐인 것이다.
{: .prompt-info }

또한 다음의 정리들도 중요하다.

> **정리 1**  
> $\mathbb{V}$가 벡터공간이고 $S_1 \subseteq S_2 \subseteq \mathbb{V}$일 때, $S_1$이 선형종속이면 $S_2$도 선형종속이다.
>
> **따름정리 1-1**  
> $\mathbb{V}$가 벡터공간이고 $S_1 \subseteq S_2 \subseteq \mathbb{V}$일 때, $S_2$가 선형독립이면 $S_1$도 선형독립이다.
{: .prompt-info }

> **정리 2**  
> 벡터공간 $\mathbb{V}$ 그리고 선형독립인 부분집합 $S$를 생각하자. $S$에 포함되지 않는 벡터 $\mathbf{v} \in \mathbb{V}$에 대해, $S \cup \\{\mathbf{v}\\}$가 선형종속이기 위한 필요충분조건은 $\mathbf{v} \in \mathrm{span}(S)$이다.
>
> 바꿔 말해, **$S$의 어떤 진부분집합도 $S$와 같은 공간을 생성하지 못한다면 $S$는 선형독립이다.**
{: .prompt-info }

## 기저와 차원

### 기저

[선형독립](#선형-종속과-선형-독립)인 $\mathbb{W}$의 생성집합 $S$에는 특별한 성질이 있는데, $\mathbb{W}$에 속한 모든 벡터는 반드시 $S$의 선형결합으로 표현할 수 있고, 그 표현은 유일하다(**정리 3**). 따라서, 어떤 벡터공간에 대한 선형독립인 생성집합을 특별히 다음과 같이 **기저(basis)**라고 정의한다.

> **기저의 정의**  
> 벡터공간 $\mathbb{V}$와 부분집합 $\beta$에 대하여, $\beta$가 선형독립이고 $\mathbb{V}$를 생성하면 $\beta$를 $\mathbb{V}$의 **기저(basis)**라고 한다. 이때, $\beta$의 벡터는 $\mathbb{V}$의 기저를 형성한다고 한다.
{: .prompt-info }

> $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$이고, $\emptyset$은 선형독립이다. 따라서 $\emptyset$은 점공간의 기저이다.
{: .prompt-tip }

특히, $F^n$에 대한 다음의 특별한 기저를 $F^n$의 **표준기저(standard basis)**라 한다.

> **표준기저의 정의**  
> 벡터공간 $F^n$에 대하여 다음 벡터들을 생각하자.
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> 이때, 집합 $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$은 $F^n$의 기저이며, 이를 $F^n$의 **표준기저(standard basis)**라 한다.
{: .prompt-info }

> **정리 3**  
> 벡터공간 $\mathbb{V}$와 서로 다른 $n$개의 벡터 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$에 대하여, 집합 $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$이 $\mathbb{V}$의 기저가 되기 위한 필요충분조건은 '임의의 벡터 $\mathbf{v} \in \mathbb{V}$를 $\beta$에 속한 벡터의 선형결합으로 나타낼 수 있고, 그 표현이 유일할 것'이다. 즉, 유일한 스칼라 $n$순서쌍 $(a_1, a_2, \dots, a_n)$에 대하여 벡터 $\mathbf{v}$는 다음과 같아야 한다.
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

**정리 3**에 따르면, 서로 다른 $n$개의 벡터 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$가 벡터공간 $\mathbb{V}$의 기저를 형성할 경우 해당 벡터공간 안에서는 벡터 $\mathbf{v}$가 주어지면 그에 대응하는 스칼라 $n$순서쌍 $(a_1, a_2, \dots, a_n)$이 결정되고, 반대로 스칼라 $n$순서쌍이 주어지면 그에 대응하는 벡터 $\mathbf{v}$를 얻을 수 있다. 나중에 **가역성**과 **동형사상**에 대해 공부할 때 다시 정리하겠지만, 이 경우 벡터공간 $\mathbb{V}$와 $F^n$은 <u>본질적으로 같다</u>.

> **정리 4**  
> 유한집합 $S$에 대해 $\mathrm{span}(S) = \mathbb{V}$이면, $S$의 부분집합 중 $\mathbb{V}$의 기저가 존재한다. 즉, 이 경우 $\mathbb{V}$의 기저는 유한집합이다.
{: .prompt-info }

> 벡터공간의 상당수가 **정리 4**의 적용 대상에 해당하지만, 반드시 그런 것은 아니다. <u>기저는 유한집합이 아닐 수도 있다</u>.
{: .prompt-tip }

### 차원

> **정리 5: 대체정리(replacement theorem)**  
> $n$개의 벡터로 이루어진 집합 $G$에 대해 $\mathrm{span}(G) = \mathbb{V}$라 하자. $L$이 $m$개의 선형독립인 벡터들로 이루어진 $\mathbb{V}$의 부분집합이면, $m\leq n$이다. 또한, $n-m$개의 벡터를 원소로 가지며 $\mathrm{span}(L \cup H) = \mathbb{V}$인 집합 $H \subseteq G$가 존재한다.
{: .prompt-info }

이로부터, 매우 중요한 2개의 따름정리를 얻는다.

> **대체정리의 따름정리 5-1**  
> 벡터공간 $\mathbb{V}$가 유한집합인 기저를 포함한다고 가정할 때, $\mathbb{V}$의 모든 기저는 유한집합이며 같은 개수의 벡터로 이루어져 있다.
{: .prompt-info }

이에 따르면 $\mathbb{V}$의 기저를 형성하는 벡터의 개수는 $\mathbb{V}$의 변치 않는 본질적인 성질이며, 이를 **차원(dimension)**이라 한다.

> **차원의 정의**  
> 기저가 유한집합인 벡터공간을 **유한차원(finite dimension)**이라 하며, 이때 기저의 원소 개수 $n$을 주어진 벡터공간의 **차원(dimension)**이라 하고 $\dim(\mathbb{V})$라 표기한다. 유한차원이 아닌 벡터공간은 **무한차원(infinite dimension)**이다.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> 벡터공간은 어느 체 위에 있는지에 따라 차원이 달라질 수 있다.
> - 복소수체 $\mathbb{C}$에서 복소수 벡터공간의 차원은 $1$, 기저는 $\\{1\\}$
> - 실수체 $\mathbb{R}$에서 복소수 벡터공간의 차원은 $2$, 기저는 $\\{1,i\\}$
{: .prompt-tip }

유한차원 벡터공간 $\mathbb{V}$에서 $\dim(\mathbb{V})$보다 더 많은 개수의 벡터를 가지는 부분집합은 절대 선형독립일 수 없다.

> **대체정리의 따름정리 5-2**  
> $\mathbb{V}$가 차원이 $n$인 벡터공간이라 하자.
> 1. $\mathbb{V}$의 유한 생성집합에는 반드시 $n$개 이상의 벡터가 있으며, $n$개의 벡터로 이루어진 $\mathbb{V}$의 생성집합은 $\mathbb{V}$의 기저이다.
> 2. 선형독립이고 $n$개의 벡터로 이루어진 $\mathbb{V}$의 부분집합은 $\mathbb{V}$의 기저이다.
> 3. 선형독립인 $\mathbb{V}$의 부분집합을 확장하여 기저를 만들 수 있다. 즉, $L \subseteq \mathbb{V}$이 선형독립이면 $\beta \supseteq L$인 $\mathbb{V}$의 기저 $\beta$가 존재한다.
{: .prompt-info }

### 부분공간의 차원

> **정리 6**  
> 유한차원 벡터공간 $\mathbb{V}$에 대하여 부분공간 $\mathbb{W}$는 유한차원이고, $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$이다. 특히, $\dim(\mathbb{W}) = \dim(\mathbb{V}) \quad \Rightarrow \quad \mathbb{V} = \mathbb{W}.$
>
> **따름정리 6-1**  
> 유한차원 벡터공간 $\mathbb{V}$의 부분공간 $\mathbb{W}$에 대해, $\mathbb{W}$의 임의의 기저를 확장하여 $\mathbb{V}$의 기저를 얻을 수 있다.
{: .prompt-info }

**정리 6**에 따라, $\mathbb{R}^3$의 부분공간의 차원은 $0,1,2,3$이 될 수 있다.
- 0차원: 원점($\mathbf{0}$)만을 포함하는 점공간 $\\{\mathbf{0}\\}$
- 1차원: 원점($\mathbf{0}$)을 지나는 직선
- 2차원: 원점($\mathbf{0}$)을 포함하는 평면
- 3차원: 유클리드 3차원 공간 전체
