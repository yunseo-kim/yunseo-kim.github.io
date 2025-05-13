---
title: 수열과 급수
description: 수열과 급수의 정의, 수열의 수렴과 발산, 급수의 수렴과 발산, 자연로그의 밑 e의 정의 등 미적분학의 기초 개념들을 살펴본다.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## 수열
미적분학에서 다루는 **수열(sequence)**은 주로 무한수열을 뜻한다. 즉, 수열이란 **자연수(natural number)** 전체집합

$$ \mathbb{N} := \{1,2,3,\dots\} $$

에서 정의된 함수이다.* 이 함수의 값들이 실수(real number)이면 '실수열', 복소수(complex number)이면 '복소수열', 점(point)이면 '점렬', 행렬(matrix)이면 '행렬렬', 함수(function)이면 '함수열', 집합(set)이면 '집합렬' 등으로 부를 수 있지만, 이들 모두를 간단하게 '열' 또는 '수열'로 지칭할 수 있다.

보통 **실수체(the field of real numbers)** $\mathbb{R}$에 대하여, 수열 $\mathbf{a}: \mathbb{N} \to \mathbb{R}$에서

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

등으로 두고, 이 수열을

$$ a_1,\, a_2,\, a_3,\, \dots $$

또는

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

등으로 나타낸다.

> *수열을 정의하는 과정에서 정의역을 자연수 전체집합 $\mathbb{N}$ 대신 $0$ 이상의 정수 집합
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> 또는
>
> $$\{2,3,4,\dots \}$$
>
> 등으로 잡을 수도 있다. 예를 들어, 거듭제곱급수 이론을 다룰 때는 정의역이 $\mathbb{N}_0$인 것이 더 자연스럽다.
{: .prompt-info }

## 수렴과 발산
수열 $(a_n)$이 실수 $l$에 수렴하면

$$ \lim_{n\to \infty} a_n = l $$

로 쓰고, 이때 $l$을 수열 $(a_n)$의 **극한값**이라 한다.

> **엡실론-델타 논법(epsilon-delta argument)**을 이용한 엄밀한 정의는 다음과 같다.
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> 즉, 아무리 작은 양수 $\epsilon$에 대해서도 $n>N$일 때 $\|a_n - l \| < \epsilon$을 만족하는 자연수 $N$이 항상 존재한다면, 충분히 큰 $n$에 대하여 $a_n$과 $l$의 차가 한없이 작아진다는 의미이므로 이를 만족하는 수열 $(a_n)$은 실수 $l$로 수렴한다고 정의한다.
{: .prompt-info }

수렴하지 않는 수열은 **발산**한다고 한다. *수열의 수렴 혹은 발산 여부는 그 수열의 유한 개의 항이 바뀌어도 변하지 않는다.*

만약 수열 $(a_n)$의 각 항이 한없이 커지면

$$ \lim_{n\to \infty} a_n = \infty $$

라고 쓰고 *양의 무한대로 발산한다*고 한다. 마찬가지로, 수열 $(a_n)$의 각 항이 한없이 작아지면

$$ \lim_{n\to \infty} a_n = -\infty $$

라고 쓰고 *음의 무한대로 발산한다*고 한다.

## 수렴하는 수열의 기본 성질
수열 $(a_n)$과 $(b_n)$이 모두 수렴하면(즉 극한값을 가지면), 수열 $(a_n + b_n)$과 $(a_n \cdot b_n)$도 마찬가지로 수렴하며, 이때

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

이다. 또한 임의의 실수 $t$에 대하여

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

이다. 이러한 성질을 **수렴하는 수열의 기본 성질** 또는 **극한의 기본 성질**이라 한다.

## 자연로그의 밑 $e$
**자연로그의 밑**은

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

로 정의한다. 이는 수학에서 가장 중요한 상수 중 하나라고 할 수 있다.

> 유독 한국에서만 '자연상수'라는 표현이 꽤 널리 쓰이고 있으나, 이는 표준 용어가 아니다. 대한수학회에서 수학용어집에 등재한 공식 용어는 ['자연로그의 밑'](https://www.kms.or.kr/mathdict/list.html?key=kname&keyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98+%EB%B0%91)이며, '자연상수'라는 표현은 해당 용어집에서 찾아볼 수 없다. 심지어 국립국어원 표준국어대사전에서도 '자연상수'라는 단어는 찾아볼 수 없으며, ['자연로그'에 대한 사전 풀이](https://stdict.korean.go.kr/search/searchView.do?pageSize=10&searchKeyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8)에서 "흔히 e로 표시하는 특정한 수"라고만 언급하고 있다.  
> 영어권과 일본에서도 이에 대응하는 용어는 존재하지 않으며, 영어 기준으로 'the base of the natural logarithm'이나 줄여서 'natural base', 혹은 'Euler's number'나 'the number $e$' 정도로 주로 지칭하는 듯 하다.  
> 출처도 불분명하고 대한수학회에서 공식 용어로 인정한 적도 없을 뿐더러, 한국을 제외하면 전 세계 어디에서도 쓰지 않는 이러한 용어를 고집할 이유가 전혀 없으므로, 앞으로 여기서는 나도 '자연로그의 밑'이라고 지칭하거나 그냥 $e$라고 표기하겠다.
{: .prompt-tip }

## 급수
수열

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

에 대하여, 이 수열의 부분합들로 이루어진 또다른 수열

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

를 수열 $\mathbf{a}$의 **급수**라고 한다. 수열 $(a_n)$의 급수는

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

등으로 나타낸다.

## 급수의 수렴과 발산
수열 $(a_n)$에서 얻은 급수

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

가 어떤 실수 $l$에 수렴하면

$$ \sum_{n=1}^{\infty} a_n = l $$

로 나타낸다. 이때 극한값 $l$을 급수 $\sum a_n$의 **합**이라고 부른다. 기호

$$ \sum a_n $$

은 상황에 따라서 <u>급수</u>를 나타내기도 하고, 그 <u>급수의 합</u>을 나타내기도 한다.

수렴하지 않는 급수는 **발산**한다고 한다.

## 수렴하는 급수의 기본 성질
[수렴하는 수열의 기본 성질](#수렴하는-수열의-기본-성질)로부터 다음과 같이 수렴하는 급수의 기본 성질을 얻는다. 실수 $t$와 수렴하는 두 급수 $\sum a_n$, $\sum b_n$에 대하여

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n \tag{4}$$

이 성립한다.

급수의 수렴성은 유한개의 항의 변화에 영향을 받지 않는다. 즉, 두 수열 $(a_n)$, $(b_n)$에서 유한 개의 $n$을 제외하고 $a_n=b_n$이면, 급수 $\sum a_n$이 수렴할 필요충분조건은 급수 $\sum b_n$이 수렴하는 것이다.
