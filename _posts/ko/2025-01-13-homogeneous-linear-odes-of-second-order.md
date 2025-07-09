---
title: "2계 동차 선형 상미분방정식 (Homogeneous Linear ODEs of Second Order)"
description: "2계 선형 상미분방정식의 정의와 특징을 알아보고, 특히 동차 선형 상미분방정식에서 성립하는 중요한 정리인 중첩의 원리와 이에 따른 기저(basis)의 개념을 이해한다."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 2계 선형 상미분방정식의 **표준형**: $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x)$
>   - **계수(coefficients)**: 함수 $p$, $q$
>   - **입력(input)**: $r(x)$
>   - **출력(output)** 또는 **응답(response)**: $y(x)$
> - 동차와 비동차
>   - **동차(homogeneous)**: 표준형으로 나타냈을 때 $r(x)\equiv0$인 경우
>   - **비동차(nonhomogeneous)**: 표준형으로 나타냈을 때 $r(x)\not\equiv 0$인 경우
> - **중첩의 원리(superposition principle)**: <u>동차</u> 선형 상미분방정식 $y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0$에 대하여, 열린 구간 $I$에서 임의의 두 해의 선형 결합은 마찬가지로 주어진 방정식의 해가 된다. 즉, 주어진 동차 선형 상미분방정식에 대한 임의의 해들의 합과 상수곱 역시 해당 방정식의 해가 된다.
> - **기저(basis)** 또는 **기본계(fundamental system)**: 구간 $I$에서 선형 독립인 동차 선형 상미분방정식의 해의 쌍 $(y_1, y_2)$
> - **계수내림(reduction of order)**: 2계 동차 상미분방정식에 대하여 어떤 한 해를 찾을 수 있다면, 이 해와 선형독립인 두 번째 해, 즉 기저를 1계 상미분방정식을 풀어서 알아낼 수 있으며 이러한 방법을 계수내림이라고 함
> - 계수내림의 응용: 일반적인 2계 상미분방정식 $F(x, y, y^\prime, y^{\prime\prime})=0$은 선형이든 비선형이든 상관없이 다음의 경우에 계수내림을 이용하여 1계로 내릴 수 있음
>   - $y$가 명시적으로 나타나지 않는 경우
>   - $x$가 명시적으로 나타나지 않는 경우
>   - 동차 선형이고 한 개의 해를 이미 알고 있을 경우
{: .prompt-info }

## Prerequisites
- [모델링(Modeling) 기본 개념](/posts/Basic-Concepts-of-Modeling/)
- [변수분리법(Separation of Variables)](/posts/Separation-of-Variables/)
- [1계 선형 상미분방정식의 풀이](/posts/Solution-of-First-Order-Linear-ODE/)

## 2계 선형 상미분방정식
2계 상미분방정식을

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:standard_form}\tag{1} $$

의 형태로 쓸 수 있으면 **선형(linear)**이라고 하고, 그렇지 않으면 **비선형(nonlinear)**이라고 한다.

$p$, $q$, $r$이 임의의 $x$에 대한 함수일 때, 이 방정식은 $y$와 그 도함수들에 대하여 선형이다.

식 ($\ref{eqn:standard_form}$)과 같은 형태를 2계 선형 상미분방정식의 **표준형(standard form)**이라고 하며, 만약 주어진 2계 선형 상미분방정식의 첫 항이 $f(x)y^{\prime\prime}$이면 방정식의 양변을 $f(x)$로 나누어 표준형을 얻을 수 있다.

함수 $p$, $q$를 **계수(coefficients)**, $r(x)$를 **입력(input)**, $y(x)$를 **출력(output)** 또는 입력과 초기조건에 대한 **응답(response)**이라고 한다.

### 동차 2계 선형 상미분방정식
식 ($\ref{eqn:standard_form}$)을 풀고자 하는 어떤 구간 $a<x<b$를 $J$ 라고 하자. 식 ($\ref{eqn:standard_form}$)에서 구간 $J$에 대해 $r(x)\equiv 0$이면

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2}$$

이고, 이를 **동차(homogeneous)**라 한다.

## 비동차 선형 상미분방정식
구간 $J$에서 $r(x)\not\equiv 0$인 경우 **비동차(nonhomogeneous)** 라고 한다.

## 중첩의 원리

$$ y = c_1y_1 + c_2y_2 \quad \text{(}c_1, c_2\text{는 임의의 상수)}\tag{3}$$

형태의 함수를 $y_1$과 $y_2$의 **선형 결합(linear combination)**이라고 부른다. 

이때 다음이 성립한다.

> **중첩의 원리(superposition principle)**  
> 동차 선형 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)에 대하여 열린 구간 $I$에서 임의의 두 해의 선형 결합은 마찬가지로 식 ($\ref{eqn:homogeneous_linear_ode}$)의 해가 된다. 즉, 주어진 동차 선형 상미분방정식에 대한 임의의 해들의 합과 상수곱 역시 해당 방정식의 해가 된다.
{: .prompt-info }

### 증명
$y_1$과 $y_2$가 구간 $I$에서 방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해라 하자. $y=c_1y_1+c_2y_2$를 식 ($\ref{eqn:homogeneous_linear_ode}$)에 대입하면

$$ \begin{align*}
y^{\prime\prime} + py^{\prime} + qy &= (c_1y_1+c_2y_2)^{\prime\prime} + p(c_1y_1+c_2y_2)^{\prime} + q(c_1y_1+c_2y_2) \\
&= c_1y_1^{\prime\prime} + c_2y_2^{\prime\prime} + p(c_1y_1^{\prime} + c_2y_2^{\prime}) + q(c_1y_1+c_2y_2) \\
&= c_1(y_1^{\prime\prime} + py_1^{\prime} + qy_1) + c_2(y_2^{\prime\prime} + py_2^{\prime} + qy_2) \\
&= 0
\end{align*} $$

으로 항등식이 된다. 따라서 $y$는 구간 $I$에서 방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해이다. $\blacksquare$

> 중첩의 원리는 동차 선형 상미분방정식에 대해서만 성립하며, 비동차 선형 상미분방정식 또는 비선형 상미분방정식에서는 성립하지 않음에 유의한다.
{: .prompt-warning }

## 기저와 일반해
### 1계 상미분방정식에서의 주요 개념 복기
이전에 [모델링(Modeling) 기본 개념](/posts/Basic-Concepts-of-Modeling/)에서 살펴본 것처럼, 1계 상미분방정식에 대한 초기값 문제(Initial Value Problem)는 상미분방정식과 초기조건(initial condition) $y(x_0)=y_0$로 구성된다. 초기조건은 주어진 상미분방정식의 일반해의 임의의 상수 $c$를 결정하기 위하여 필요하며, 이렇게 결정한 해를 특수해라고 한다. 이제 이 개념들을 2계 상미분방정식으로 확장하자.

### 초기값 문제와 초기조건
2계 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)에 대한 **초기값 문제(initial value problem)**는, 주어진 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)와 2개의 **초기조건(initial conditions)**

$$ y(x_0) = K_0, \quad y^{\prime}(x_0)=K_1 \label{eqn:init_conditions}\tag{4}$$

으로 구성된다. 이 조건은 상미분방정식의 **일반해(general solution)**

$$ y = c_1y_1 + c_2y_2 \label{eqn:general_sol}\tag{5}$$

의 2개의 임의의 상수 $c_1$과 $c_2$를 결정하기 위해 필요하다.

### 선형 독립과 선형 종속
여기서 잠시 선형 독립과 선형 종속의 개념을 알아보자. 뒤에서 기저를 정의하려면 이를 이해할 필요가 있다.  
두 함수 $y_1$과 $y_2$가 정의된 구간 $I$의 모든 점에서

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{이고 }k_2=0 \label{eqn:linearly_independent}\tag{6}$$

이면 이 두 함수 $y_1$과 $y_2$는 구간 $I$에서 **선형 독립(linearly independent)**이라고 하며, 그렇지 않은 경우 $y_1$과 $y_2$는 **선형 종속(linearly dependent)**이라고 한다.

만약 $y_1$과 $y_2$가 선형 종속이라면(즉, 명제 ($\ref{eqn:linearly_independent}$)이 참이 아니라면), $k_1 \neq 0$ 또는 $k_2 \neq 0$으로 ($\ref{eqn:linearly_independent}$)의 방정식의 양변을 나누어

$$ y_1 = - \frac{k_2}{k_1}y_2 \quad \text{또는} \quad y_2 = - \frac{k_1}{k_2}y_2 $$

와 같이 쓸 수 있으므로 $y_1$과 $y_2$가 비례함을 알 수 있다.

### 기저, 일반해, 특수해
다시 돌아와서, 식 ($\ref{eqn:general_sol}$)가 일반해가 되려면 $y_1$과 $y_2$는 방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해이면서 동시에 구간 $I$에서 서로 비례하지 않고 선형 독립(linearly independent)이어야 한다. 이러한 조건을 만족하는, 구간 $I$에서 선형 독립인 방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 해의 쌍(pair) $(y_1, y_2)$를 구간 $I$에서 식 ($\ref{eqn:homogeneous_linear_ode}$)의 해의 **기저(basis)** 또는 **기본계(fundamental system)**라고 한다.

초기조건을 활용하여 일반해 ($\ref{eqn:general_sol}$)의 두 상수 $c_1$과 $c_2$를 결정함으로써, 점 $(x_0, K_0)$를 지나고 그 점에서의 접선의 기울기는 $K_1$인 유일한 해를 얻는다. 이를 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)의 **특수해(particular solution)**라고 한다.

식 ($\ref{eqn:homogeneous_linear_ode}$)가 열린 구간 $I$에서 연속이라면 반드시 일반해를 가지며, 이 일반해는 가능한 모든 특수해를 포함한다. 즉, 이 경우 방정식 ($\ref{eqn:homogeneous_linear_ode}$)는 일반해로부터 얻을 수 없는 특이해(singular solution)를 갖지 않는다.

## 계수내림 (reduction of order)
2계 동차 상미분방정식에 대하여 어떤 한 해를 찾을 수 있다면, 이 해와 선형독립인 두 번째 해, 즉 기저를 다음과 같이 1계 상미분방정식을 풀어서 알아낼 수 있다. 이러한 방법을 **계수내림(reduction of order)**이라고 한다.

<u>$f(x)y^{\prime\prime}$이 아닌 $y^{\prime\prime}$을 갖는 표준형의</u> 2계 동차 상미분방정식

$$ y^{\prime\prime} + p(x)y^\prime + q(x)y = 0 $$

에 대하여, 열린 구간 $I$에서 이 방정식의 한 해 $y_1$을 알고 있다고 하자.

이제 찾고자 하는 두 번째 해를 $y_2 = uy_1$으로 놓고,

$$ \begin{align*}
y &= y_2 = uy_1, \\
y^{\prime} &= y_2^{\prime} = u^{\prime}y_1 + uy_1^{\prime}, \\
y^{\prime\prime} &= y_2^{\prime\prime} = u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

을 방정식에 대입하면

$$ (u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}) + p(u^{\prime}y_1 + uy_1^{\prime}) + quy_1 = 0 \tag{7} $$

을 얻는다. $u^{\prime\prime}$, $u^{\prime}$, $u$ 각 항끼리 모아서 정리하면

$$ y_1u^{\prime\prime} + (py_1+2y_1^{\prime})u^{\prime} + (y_1^{\prime\prime} + py_1^{\prime} + qy_1)u = 0 $$

이 된다. 그런데 $y_1$은 주어진 방정식의 해이기 때문에, 마지막 괄호 안의 식은 $0$이므로 $u$의 항이 사라지고 $u^{\prime}$과 $u^{\prime\prime}$에 대한 상미분방정식이 남는다. 이 남은 상미분방정식의 양변을 $y_1$으로 나누고, $u^{\prime}=U$, $u^{\prime\prime}=U^{\prime}$으로 놓으면 다음과 같은 1계 상미분방정식을 얻는다.

$$ U^{\prime} + \left(\frac{2y_1^{\prime}}{y_1} + p \right) U = 0. $$

[변수분리](/posts/Separation-of-Variables/)하고 적분하면

$$ \begin{align*}
\frac{dU}{U} &= - \left(\frac{2y_1^{\prime}}{y_1} + p \right) dx \\
\ln|U| &= -2\ln|y_1| - \int p dx
\end{align*} $$

이고, 양변에 지수함수를 취하면 최종적으로

$$ U = \frac{1}{y_1^2}e^{-\int p dx} \tag{8}$$

를 얻는다. 앞서 $U=u^{\prime}$으로 놓았으므로 $u=\int U dx$가 되어, 구하고자 하는 두 번째 해 $y_2$는

$$ y_2 = uy_1 = y_1 \int U dx $$

이다. $\cfrac{y_2}{y_1} = u = \int U dx$는 $U>0$인 이상 상수가 될 수 없으므로, $y_1$과 $y_2$는 해의 기저를 형성한다.

### 계수내림의 응용
일반적인 2계 상미분방정식 $F(x, y, y^\prime, y^{\prime\prime})=0$은, 선형이든 비선형이든 상관없이 $y$가 명시적으로 나타나지 않거나, $x$가 명시적으로 나타나지 않거나, 또는 앞서 본 것과 같이 동차 선형이고 한 개의 해를 이미 알고 있을 때 계수내림을 이용하여 1계로 내릴 수 있다.

#### $y$가 명시적으로 나타나지 않을 경우
$F(x, y^\prime, y^{\prime\prime})=0$에서 $z=y^{\prime}$으로 놓으면, $z$에 대한 1계 상미분방정식 $F(x, z, z^{\prime})$으로 내릴 수 있다.

#### $x$가 명시적으로 나타나지 않을 경우
$F(y, y^\prime, y^{\prime\prime})=0$에서 $z=y^{\prime}$으로 놓으면, $y^{\prime\prime} = \cfrac{d y^{\prime}}{dx} = \cfrac{d y^{\prime}}{dy}\cfrac{dy}{dx} = \cfrac{dz}{dy}z$가 되므로 $y$가 독립변수 $x$의 역할을 대신하는 $z$에 대한 1계 상미분방정식 $F(y,z,z^\prime)$으로 내릴 수 있다.
