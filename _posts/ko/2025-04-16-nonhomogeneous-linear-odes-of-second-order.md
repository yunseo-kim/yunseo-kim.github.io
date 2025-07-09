---
title: "2계 비동차 선형 상미분방정식 (Nonhomogeneous Linear ODEs of Second Order)"
description: "2계 비동차 선형 상미분방정식의 일반해의 형태를 대응하는 동차 선형 상미분방정식의 해와의 관계를 중심으로 살펴보고, 일반해의 존재와 특이해의 비존재를 보인다."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 2계 비동차 선형 상미분방정식 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$의 **일반해**:
>   - $y(x) = y_h(x) + y_p(x)$
>   - $y_h$: 동차 상미분방정식 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$의 일반해 $y_h = c_1y_1 + c_2y_2$
>   - $y_p$: 해당 비동차 상미분방정식의 특수해
> - 응답 항 $y_p$는 입력 $r(x)$에 의해서만 결정되며, 동일한 비동차 상미분방정식에 대해서는 초기조건이 달라져도 $y_p$는 달라지지 않음. 비동차 상미분방정식의 두 특수해의 차는 대응하는 동차 상미분방정식의 해가 됨.
> - **일반해의 존재**: 비동차 상미분방정식의 계수 $p(x)$, $q(x)$와 입력 함수 $r(x)$가 연속이면 일반해가 항상 존재함
> - **특이해의 비존재**: 일반해는 방정식의 모든 해를 포함함(즉, 특이해가 존재하지 않음)
{: .prompt-info }

## Prerequisites
- [2계 동차 선형 상미분방정식 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [브론스키언(Wronskian), 해의 존재와 유일성](/posts/wronskian-existence-and-uniqueness-of-solutions/)

## 2계 비동차 선형 상미분방정식의 일반해와 특수해
2계 비동차 선형 상미분방정식

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

를 생각하자. 여기서 $r(x) \not\equiv 0$이다. 열린 구간 $I$에서 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 **일반해**는 이 비동차 상미분방정식에 대응하는 동차 상미분방정식

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

의 일반해 $y_h = c_1y_1 + c_2y_2$와 식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 특수해 $y_p$의 합

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

의 형태이다. 또한 구간 $I$에서 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 **특수해**는 $y_h$의 임의의 상수 $c_1$과 $c_2$에 특정한 값을 지정하여 식 ($\ref{eqn:general_sol}$)으로부터 얻는 해이다.

즉, 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)에 독립변수 $x$에만 의존하는 입력 $r(x)$를 추가하면 그에 대응하는 항 $y_p$가 응답에 추가되며, 이 추가된 응답 항 $y_p$는 초기조건과 무관하게 오직 입력 $r(x)$에 의해 결정된다. 뒤에서 보겠지만 식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 임의의 두 해 $y_1$과 $y_2$의 차를 구하면(즉, 서로 다른 두 초기조건에 대한 각각의 특수해의 차를 구하면) 초기조건에 무관한 $y_p$ 부분은 지워져 ${y_h}_1$과 ${y_h}_2$의 차만 남으며, 이는 [중첩의 원리](/posts/homogeneous-linear-odes-of-second-order/#중첩의-원리)에 의해 식 ($\ref{eqn:homogeneous_linear_ode}$)의 해가 된다.

## 비동차 상미분방정식의 해와, 그에 대응하는 동차 상미분방정식의 해의 관계
> **정리 1: 비동차 상미분방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 해와 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해의 관계**  
> **(a)** 어떤 열린 구간 $I$에서 비동차 상미분방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 해 $y$와 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해 $\tilde{y}$의 합은 구간 $I$에서 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 해이다. 특히 식 ($\ref{eqn:general_sol}$)은 구간 $I$에서 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 해이다.  
> **(b)** 구간 $I$에서 비동차 상미분방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 두 해의 차는 구간 $I$에서 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해이다.
{: .prompt-info }

### 증명
#### (a)
방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)과 ($\ref{eqn:homogeneous_linear_ode}$)의 좌변을 $L[y]$라고 표기하자. 그러면 구간 $I$에서 식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 임의의 해 $y$와 식 ($\ref{eqn:homogeneous_linear_ode}$)의 임의의 해 $\tilde{y}$에 대해서도 다음을 만족한다.

$$ L[y + \tilde{y}] = L[y] + L[\tilde{y}] = r + 0 = r. $$

#### (b)
구간 $I$에서 식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 임의의 두 해 $y$와 $y^\*$에 대하여 다음을 만족한다.

$$ L[y - y^*] = L[y] - L[y^*] = r - r = 0.\ \blacksquare $$

## 비동차 상미분방정식의 일반해는 모든 해를 포함한다
동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)에 대하여 [일반해가 모든 해를 포함한다는 것을 알고 있다](/posts/wronskian-existence-and-uniqueness-of-solutions/#일반해는-모든-해를-포함한다). 비동차 상미분방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)에 대해서도 같은 것이 성립함을 보이자.

> **정리 2: 비동차 상미분방정식의 일반해는 모든 해를 포함한다**  
> 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 계수 $p(x)$, $q(x)$와 입력 함수 $r(x)$가 어떤 열린 구간 $I$에서 연속이라면, 구간 $I$에서 식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 모든 해는 구간 $I$에서 식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 일반해 ($\ref{eqn:general_sol}$)의 $y_h$의 임의의 상수 $c_1$과 $c_2$에 적당한 값을 지정함으로써 얻을 수 있다.
{: .prompt-info }

### 증명
$y^\*$을 $I$에서 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 어떤 해라고 하고, $x_0$를 구간 $I$ 내의 어떤 $x$라 하자. [연속인 변수계수를 갖는 동차 상미분방정식의 일반해의 존재 정리](/posts/wronskian-existence-and-uniqueness-of-solutions/#일반해의-존재)에 의해 $y_h = c_1y_1 + c_2y_2$가 존재하고, 추후 알아볼 **매개변수변환법(method of variation of parameters)**에 의해 $y_p$ 또한 존재하기에 구간 $I$에서 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 일반해 ($\ref{eqn:general_sol}$)은 존재한다. 이제 앞서 증명한 정리 [1(b)](#비동차-상미분방정식의-해와-그에-대응하는-동차-상미분방정식의-해의-관계)에 의해 $Y = y^\* - y_p$는 구간 $I$에서 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해이며, $x_0$에서

$$ \begin{gather*}
Y(x_0) = y^*(x_0) - y_p(x_0) \\
Y^{\prime}(x_0) = {y^*}^{\prime}(x_0) - y_p^{\prime}(x_0)
\end{gather*} $$

이다. [초기값 문제의 해의 존재성과 유일성의 정리](/posts/wronskian-existence-and-uniqueness-of-solutions/#초기값-문제의-해의-존재성과-유일성의-정리)에 의하면 구간 $I$에서 위의 초기조건에 대하여 $y_h$의 $c_1$, $c_2$에 적당한 값을 지정하여 얻을 수 있는 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 특수해 $Y$가 유일하게 존재한다. $y^\* = Y + y_p$이므로 비동차 상미분방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 임의의 특수해 $y^\*$을 일반해 ($\ref{eqn:general_sol}$)으로부터 얻을 수 있음을 보였다. $\blacksquare$
