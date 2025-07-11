---
title: "브론스키언(Wronskian), 해의 존재와 유일성"
description: "연속인 임의의 변수계수를 갖는 2계 동차 선형 상미분방정식에 대하여, 초기값 문제의 해의 존재성과 유일성의 정리, 브론스키언(Wronskian)을 이용한 해의 선형종속/선형독립 판별법을 알아본다. 또한 이를 이용하여 이러한 형태의 방정식은 항상 일반해를 가지며, 이 일반해는 방정식의 모든 해를 포함함을 보인다."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> 구간 $I$에서 연속인 임의의 변수계수 $p$와 $q$를 갖는 2계 동차 선형 상미분방정식
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> 과 초기조건
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> 에 대하여, 다음 4개의 정리가 성립한다.
> 1. **초기값 문제의 해의 존재성과 유일성의 정리**: 주어진 방정식 및 초기조건으로 구성되는 초기값 문제는 구간 $I$에서 유일한 해 $y(x)$를 갖는다.
> 2. **브론스키언(Wronskian)을 이용한 해의 선형종속/선형독립 판별**: 방정식의 두 해 $y_1$과 $y_2$에 대하여, 구간 $I$ 내에 **브론스키언(Wronskian)** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$의 값이 $0$이 되는 $x_0$가 존재한다면 두 해는 선형종속이다. 또한, 구간 $I$ 내에 $W\neq 0$이 되는 $x_1$이 존재한다면 두 해는 선형독립이다.
> 3. **일반해의 존재**: 주어진 방정식은 구간 $I$에서 일반해를 가진다.
> 4. **특이해의 비존재**: 이 일반해는 방정식의 모든 해를 포함한다(즉, 특이해가 존재하지 않는다).
{: .prompt-info }

## Prerequisites
- [1계 선형 상미분방정식의 풀이](/posts/Solution-of-First-Order-Linear-ODE/)
- [2계 동차 선형 상미분방정식 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [상수계수를 갖는 2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [오일러-코시 방정식](/posts/euler-cauchy-equation/)
- 역행렬과 특이행렬, 행렬식

## 연속인 임의의 변수계수를 갖는 동차 선형 상미분방정식
앞서 [상수계수를 갖는 2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-with-constant-coefficients/)과 [오일러-코시 방정식](/posts/euler-cauchy-equation/)의 일반해를 알아보았다.
이 글에서는 논의를 보다 일반적인 경우로 확장하여, 연속인 임의의 **변수계수(variable coefficient)** $p$와 $q$를 갖는 2계 동차 선형 상미분방정식

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

의 일반해의 존재성과 형태를 알아본다. 또한 이에 더하여, 상미분방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)과 다음의 두 가지 초기조건

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

로 구성된 [초기값 문제](/posts/homogeneous-linear-odes-of-second-order/#초기값-문제와-초기조건)의 유일성도 알아볼 것이다. 

미리 결론부터 이야기하자면, 연속인 계수를 갖는 <u>선형</u>상미분방정식은 *특이해(singular solution)*(일반해로부터 얻을 수 없는 해)를 갖지 않는다는 것이 여기서 다루는 내용의 핵심이다.

## 초기값 문제의 해의 존재성과 유일성의 정리
> **초기값 문제의 해의 존재성과 유일성의 정리(Existence and Uniqueness Theorem for Initial Value Problems)**  
> 만약 $p(x)$와 $q(x)$가 어떤 열린 구간 $I$에서 연속함수이고, $x_0$가 구간 $I$ 내에 있다면, 식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)과 ($\ref{eqn:initial_conditions}$)로 구성되는 초기값 문제는 구간 $I$에서 유일한 해 $y(x)$를 갖는다.
{: .prompt-info }

존재성에 대한 증명은 여기서는 다루지 않으며, 유일성의 증명만 살펴볼 것이다. 통상적으로 유일성을 증명하는 것이 존재성을 증명하는 것보다 간단하다.  
증명에 관심이 없다면 이 부분은 건너뛰고 [해의 선형종속과 선형독립](#해의-선형종속과-선형독립)으로 넘어가도 좋다.

### 유일성의 증명
상미분방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)과 초기조건 ($\ref{eqn:initial_conditions}$)로 구성된 초기값 문제가 구간 $I$에서 두 개의 해 $y_1(x)$와 $y_2(x)$를 가진다고 가정하자. 이 두 해의 차

$$ y(x) = y_1(x) - y_2(x) $$

가 구간 $I$에서 항등적으로 $0$이 됨을 보일 수 있다면, 이는 곧 구간 $I$에서 $y_1 \equiv y_2$라는 것이므로 해의 유일성을 의미한다.

방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)이 동차 선형 상미분방정식이므로, $y_1$과 $y_2$의 선형결합인 $y$는 $I$에서 방정식의 해가 된다. $y_1$과 $y_2$가 동일한 초기조건 ($\ref{eqn:initial_conditions}$)를 만족하므로, $y$는 조건

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

을 만족한다. 이제 함수

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

과 그 도함수

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

을 생각하자. 상미분방정식으로부터

$$ y^{\prime\prime} = -py^{\prime} - qy $$

를 얻으며, 이를 $z^{\prime}$에 대한 식에 대입하면

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

을 얻는다. 이제 $y$와 $y^{\prime}$이 실수이므로

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

이 된다. 이것과 $z$의 정의로부터 두 개의 부등식

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

를 얻을 수 있다. 이 두 부등식으로부터 $\|2yy^{\prime}\|\leq z$임을 알 수 있고, 그렇다면 식 ($\ref{eqn:z_prime}$)의 마지막 항에 대해서는 다음 부등식이 성립한다.

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

이 결과와 함께 $-p \leq \|p\|$임을 이용하고, 식 ($\ref{eqn:z_prime}$)의 항 $2yy^{\prime}$에 식 ($\ref{eqn:inequalities}$a)를 적용하면

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

가 된다. ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$이므로 이로부터

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

를 얻으며, 괄호 안의 함수를 $h = 1 + 2\|p\| + \|q\|$로 놓으면

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

이다. 같은 방법으로, 식 ($\ref{eqn:z_prime}$)와 ($\ref{eqn:inequalities}$)로부터

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

를 얻는다. 이 두 부등식 ($\ref{eqn:inequality_6a}$), ($\ref{eqn:inequality_6b}$)는 다음 부등식

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

과 동등하며, 두 식의 좌변에 대한 [적분인자](/posts/Solution-of-First-Order-Linear-ODE/#비동차-선형-상미분방정식)는

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{와} \qquad F_2 = e^{\int h(x)\ dx} $$

이다. $h$가 연속이므로 부정적분 $\int h(x)\ dx$는 존재하며, $F_1$과 $F_2$가 양수이므로 식 ($\ref{eqn:inequalities_7}$)로부터

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

을 얻는다. 이는 구간 $I$에서 $F_1 z$가 증가하지 않으며 $F_2 z$가 감소하지 않음을 의미한다. 식 ($\ref{eqn:initial_conditions_*}$)에 의해 $z(x_0) = 0$이므로,

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

이다. 마지막으로 부등식의 양변을 양수 $F_1$과 $F_2$로 나누면 다음과 같이 해의 유일성을 보일 수 있다.

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## 해의 선형종속과 선형독립
[2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-of-second-order/#기저와-일반해)에서 다뤘던 내용을 잠시 다시 떠올려보자. 열린 구간 $I$에서의 일반해는 $I$에서의 **기저(basis)** $y_1$, $y_2$, 즉 선형독립인 해들의 쌍으로부터 만들어진다. 여기서 $y_1$과 $y_2$가 구간 $I$에서 **선형 독립(linearly independent)**이라는 것은 곧 구간 내 모든 $x$에 대하여 다음을 만족함을 의미한다.

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{이고 }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

만약 위를 만족하지 않고, 적어도 하나의 $0$이 아닌 $k_1$, $k_2$에 대하여 $k_1y_1(x) + k_2y_2(x) = 0$이 성립할 경우 $y_1$과 $y_2$는 구간 $I$에서 **선형 종속(linearly dependent)**이다. 이 경우 구간 $I$의 모든 $x$에 대해

$$ \text{(a) } y_1 = ky_2 \quad \text{또는} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

이 되어 $y_1$과 $y_2$는 비례한다.

이제 다음의 해의 선형독립/선형종속 판별법을 알아보자.

> **브론스키언(Wronskian)을 이용한 해의 선형종속/선형독립 판별**  
> **i.** 상미분방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)이 열린 구간 $I$에서 연속인 계수 $p(x)$와 $q(x)$를 갖는다면, 구간 $I$에서 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)의 두 해 $y_1$과 $y_2$가 선형종속이 되기 위한 필요충분조건은 이 해들의 *브론스키 행렬식(Wronski determinant)*, 줄여서 **브론스키언(Wronskian)**이라고 부르는 다음의 행렬식
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> 이 구간 $I$ 내의 어떤 $x_0$에서 $0$이 되는 것이다.
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{과 } y_2 \text{는 선형종속} $$
>
> **ii.** 구간 $I$ 내의 한 점 $x=x_0$에서 $W=0$이라면 구간 $I$ 안의 모든 $x$에서 $W=0$이다.
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> 다시 말해, $W\neq 0$인 $x_1$이 구간 $I$에 존재한다면 해당 구간 $I$에서는 $y_1$, $y_2$는 선형독립이다.
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_1)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{과 } y_2 \text{는 선형독립}
> \end{align*}$$
>
{: .prompt-info }

> 브론스키언은 폴란드의 수학자 유제프 마리아 호에네-브론스키(Józef Maria Hoene-Wroński)가 처음 도입하였고, 그의 사후인 11882 HE에 스코틀랜드 수학자 토머스 뮤어(Sir Thomas Muir)에 의해 지금의 이름이 붙었다.
{: .prompt-tip }

### 증명
#### i. (a)
구간 $I$에서 $y_1$과 $y_2$가 선형종속이라 하자. 그러면 구간 $I$에서 식 ($\ref{eqn:linearly_dependent}$a) 또는 ($\ref{eqn:linearly_dependent}$b)가 성립한다. 만약 식 ($\ref{eqn:linearly_dependent}$a)가 성립한다면

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

이며, 마찬가지로 식 ($\ref{eqn:linearly_dependent}$b)가 성립하는 경우에도

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

이므로 <u>구간 $I$ 내의 모든 $x$에 대해</u> 브론스키언 $W(y_1, y_2)=0$임을 확인할 수 있다.

#### i. (b)
역으로 어떤 $x = x_0$에 대해 $W(y_1, y_2)=0$이라 할 때, 구간 $I$에서 $y_1$과 $y_2$가 선형종속이 됨을 보일 것이다. 미지수 $k_1$, $k_2$에 대한 선형연립방정식

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

을 생각하자. 이는 다음과 같은 벡터방정식 꼴로 표현할 수 있다.

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

이 벡터방정식의 계수행렬은

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

이고, 이 행렬의 행렬식은 곧 $W(y_1(x_0), y_2(x_0))$이다. $\det(A) = W=0$이므로 $A$는 **역행렬(inverse matrix)**이 존재하지 않는 **특이행렬(singular matrix)**이고, 따라서 연립방정식 ($\ref{eqn:linear_system}$)은 $k_1$과 $k_2$ 중 적어도 하나는 $0$이 아닌 영벡터 $(0,0)$ 이외의 해 $(c_1, c_2)$를 가진다. 이제 함수 

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

를 도입하자. 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)이 동차 선형이므로 [중첩의 원리](/posts/homogeneous-linear-odes-of-second-order/#중첩의-원리)에 의해 이 함수는 구간 $I$에서 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)의 해가 된다. 식 ($\ref{eqn:linear_system}$)로부터 이 해는 초기조건 $y(x_0)=0$, $y^{\prime}(x_0)=0$을 만족함을 알 수 있다.

한편, 동일한 초기조건 $y^\*(x_0)=0$, ${y^\*}^{\prime}(x_0)=0$을 만족하는 자명해 $y^\* \equiv 0$이 존재한다. 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)의 계수 $p$와 $q$가 연속이기 때문에 [초기값 문제의 해의 존재성과 유일성의 정리](#초기값-문제의-해의-존재성과-유일성의-정리)에 의해 해의 유일성이 보장되며, 따라서 $y \equiv y^\*$이다. 즉, 구간 $I$에서

$$ c_1y_1 + c_2y_2 \equiv 0 $$

이다. $c_1$과 $c_2$ 둘 중 적어도 하나는 $0$이 아니기 때문에 ($\ref{eqn:linearly_independent}$)을 만족하지 않으므로, 이는 구간 $I$에서 $y_1$, $y_2$가 선형종속임을 의미한다.

#### ii.
만약 구간 $I$ 내의 어떤 한 점 $x_0$에서 $W(x_0)=0$라면, [i.(b)](#i-b)에 의해 구간 $I$에서 $y_1$, $y_2$는 선형종속이고, 그러면 [i.(a)](#i-a)에 의해 $W\equiv 0$이다. 그러므로 $W(x_1)\neq 0$인 $x_1$이 구간 $I$ 내에 하나라도 존재한다면 $y_1$과 $y_2$는 선형독립이다. $\blacksquare$

## 일반해는 모든 해를 포함한다
### 일반해의 존재
> 만약 $p(x)$와 $q(x)$가 열린 구간 $I$에서 연속이라면, 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)은 구간 $I$에서 일반해를 가진다.
{: .prompt-info }

#### 증명
[초기값 문제의 해의 존재성과 유일성의 정리](#초기값-문제의-해의-존재성과-유일성의-정리)에 의해, 상미분방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)은 구간 $I$에서 초기조건

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

을 만족하는 해 $y_1(x)$와 구간 $I$에서 초기조건

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

을 만족하는 해 $y_2(x)$를 가진다. 이 두 해의 브론스키언은 $x=x_0$에서 0이 아닌 값

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

을 가지므로, [브론스키언(Wronskian)을 이용한 해의 선형종속/선형독립 판별](#해의-선형종속과-선형독립)에 의해 구간 $I$에서 $y_1$과 $y_2$는 선형독립이다. 따라서 이 두 해는 구간 $I$에서 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)의 해의 기저를 형성하며, 임의의 상수 $c_1$, $c_2$를 갖는 일반해 $y = c_1y_1 + c_2y_2$가 구간 $I$에서 반드시 존재한다. $\blacksquare$

### 특이해의 부존재
> 상미분방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)이 어떤 열린 구간 $I$에서 연속인 계수 $p(x)$와 $q(x)$를 갖는다면, 구간 $I$에서 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)의 모든 해 $y=Y(x)$는
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> 의 형태이며, 여기서 $y_1$, $y_2$는 구간 $I$에서 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)의 해의 기저이고 $C_1$, $C_2$는 적당한 상수이다.  
> 즉, 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)은 일반해로부터 얻을 수 없는 해인 **특이해(singular solution)**를 갖지 않는다.
{: .prompt-info }

#### 증명
$y=Y(x)$를 구간 $I$에서 방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)의 어떤 해라고 하자. 이제 [일반해의 존재 정리](#일반해의-존재)에 의해서 상미분방정식 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$)은 구간 $I$에서 일반해

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

를 갖는다. 이제 임의의 $Y(x)$에 대하여 구간 $I$에서 $y(x)=Y(x)$가 되게 하는 상수 $c_1$, $c_2$가 존재함을 보여야 한다. 구간 $I$에서 임의의 $x_0$를 선택했을 때 $y(x_0)=Y(x_0)$이고 $y^{\prime}(x_0)=Y^{\prime}(x_0)$가 되게 하는 $c_1$, $c_2$의 값을 찾을 수 있음을 먼저 보이자. 식 ($\ref{eqn:general_solution}$)로부터

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

가 된다. $y_1$과 $y_2$가 기저이므로 계수행렬의 행렬식인 $W(y_1(x_0), y_2(x_0))\neq 0$이고, 따라서 방정식 ($\ref{eqn:vector_equation_2}$)는 $c_1$과 $c_2$에 대해 풀 수 있다. 그 해를 $(c_1, c_2) = (C_1, C_2)$라고 하자. 이를 식 ($\ref{eqn:general_solution}$)에 대입하면 다음의 특수해를 얻는다.

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

$C_1$, $C_2$가 방정식 ($\ref{eqn:vector_equation_2}$)의 해이므로,

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

이다. [초기값 문제의 해의 존재성과 유일성의 정리](#초기값-문제의-해의-존재성과-유일성의-정리)의 유일성에 의헤, 구간 $I$ 내의 모든 $x$에 대하여 $y^\* \equiv Y$이다. $\blacksquare$
