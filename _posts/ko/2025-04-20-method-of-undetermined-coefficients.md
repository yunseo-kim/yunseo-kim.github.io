---
title: 미정계수법
description: 특정한 형태의 상수계수 비동차 선형 상미분방정식에 대한 초기값 문제를 간단하게 풀 수 있어, 공학에서 진동계, RLC 전기회로 모델 등에 대해 유용하게 자주 사용하는 해법인 미정계수법을 알아보자.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **미정계수법**의 적용 대상:
>   - **상수 계수 $a$와 $b$**를 갖고
>   - 입력 $r(x)$가 지수함수, $x$의 거듭제곱, $\cos$ 또는 $\sin$, 또는 이와 같은 함수들의 합과 곱으로 이루어진
>   - 선형 상미분방정식 $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **미정계수법에 대한 선택 규칙**  
>   - **(a) 기본규칙(basic rule)**: 식 ($\ref{eqn:linear_ode_with_constant_coefficients}$)에서 $r(x)$가 표의 첫 번째 열에 있는 함수들 중 하나라면 같은 행의 $y_p$를 선택하고, $y_p$와 그 도함수들을 식 ($\ref{eqn:linear_ode_with_constant_coefficients}$)에 대입함으로써 미정계수를 결정한다.  
>   - **(b) 변형규칙(modification rule)**: $y_p$로 선택한 항이 식 ($\ref{eqn:linear_ode_with_constant_coefficients}$)에 대응하는 동차 상미분방정식 $y^{\prime\prime} + ay^{\prime} + by = 0$의 해가 된다면, 이 항에 $x$(또는 만약 이 해가 동차 상미분방정식의 특성방정식의 이중근에 해당한다면 $x^2$)를 곱한다.  
>   - **(c) 합규칙(sum rule)**: $r(x)$가 표의 첫 번째 열에 있는 함수들의 합이라면, 두 번째 열의 대응하는 행에 있는 함수들의 합을 $y_p$로 선택한다.
>
> | $r(x)$의 항 | $y_p(x)$에 대한 선택 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [2계 동차 선형 상미분방정식 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [브론스키언(Wronskian), 해의 존재와 유일성](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [2계 비동차 선형 상미분방정식 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)

## 미정계수법
$r(x) \not\equiv 0$인 2계 비동차 선형 상미분방정식

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

와 이 비동차 상미분방정식에 대응하는 동차 상미분방정식

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

을 생각하자.

앞서 [2계 비동차 선형 상미분방정식 (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)에서 살펴본 바에 따르면, 비동차 선형 상미분방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)에 대한 초기값 문제를 풀기 위해서는 동차 상미분방정식 ($\ref{eqn:homogeneous_linear_ode}$)를 풀어 $y_h$를 구한 후 방정식 ($\ref{eqn:nonhomogeneous_linear_ode}$)의 한 해 $y_p$를 찾아서 일반해

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

를 얻어야 한다. 그렇다면 $y_p$는 어떻게 찾을 수 있는가? $y_p$를 찾는 일반적인 방법은 **매개변수변환법(method of variation of parameters)**이지만, 경우에 따라선 그보다 훨씬 간단한 **미정계수법(method of undetermined coefficients)**을 적용할 수 있다. 특히, 진동계와 RLC 전기회로 모델에 적용할 수 있어 공학에서 자주 사용하는 방법이다.

미정계수법은 **상수 계수 $a$와 $b$**를 갖고, 입력 $r(x)$가 지수함수, $x$의 거듭제곱, $\cos$ 또는 $\sin$, 또는 이와 같은 함수들의 합과 곱으로 이루어진 선형 상미분방정식

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

에 적합하다. 이와 같은 형태의 $r(x)$는 자기 자신과 유사한 형태의 도함수들을 갖는다는 점이 미정계수법의 핵심이다. 미정계수법을 적용하기 위해서는 $r(x)$와 유사한 형태이되, 자기 자신과 그 도함수들을 주어진 상미분방정식에 대입함으로써 결정되는 미지의 계수를 갖는 $y_p$를 선택한다. 공학에서 실용적으로 중요한 형태의 $r(x)$에 대하여 적절한 $y_p$를 선택하기 위한 규칙은 다음과 같다.

> **미정계수법에 대한 선택 규칙**  
> **(a) 기본규칙(basic rule)**: 식 ($\ref{eqn:linear_ode_with_constant_coefficients}$)에서 $r(x)$가 표의 첫 번째 열에 있는 함수들 중 하나라면 같은 행의 $y_p$를 선택하고, $y_p$와 그 도함수들을 식 ($\ref{eqn:linear_ode_with_constant_coefficients}$)에 대입함으로써 미정계수를 결정한다.  
> **(b) 변형규칙(modification rule)**: $y_p$로 선택한 항이 식 ($\ref{eqn:linear_ode_with_constant_coefficients}$)에 대응하는 동차 상미분방정식 $y^{\prime\prime} + ay^{\prime} + by = 0$의 해가 된다면, 이 항에 $x$(또는 만약 이 해가 동차 상미분방정식의 특성방정식의 이중근에 해당한다면 $x^2$)를 곱한다.  
> **(c) 합규칙(sum rule)**: $r(x)$가 표의 첫 번째 열에 있는 함수들의 합이라면, 두 번째 열의 대응하는 행에 있는 함수들의 합을 $y_p$로 선택한다.
>
> | $r(x)$의 항 | $y_p(x)$에 대한 선택 |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

이 방법은 간편할 뿐만 아니라 자기교정성을 지닌다는 장점이 있다. $y_p$를 잘못 선택하거나 너무 적은 수의 항들을 선택하면 모순에 이르게 되며, 너무 많은 항을 선택할 경우 불필요한 항들의 계수는 $0$이 되어 옳은 결과를 얻는다. 미정계수법을 적용했다가 뭔가가 잘못되더라도 풀이 과정에서 자연스럽게 알아차리게 되므로, 위의 선택 규칙에 따라 어느 정도 적당한 $y_p$를 선택했다면 부담 없이 시도해 볼 수 있다.

### 합규칙의 증명
$r(x) = r_1(x) + r_2(x)$ 꼴인 비동차 선형 상미분방정식

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

를 생각하자. 이제 동일한 좌변에 입력으로는 $r_1$, $r_2$를 갖는 다음의 두 방정식

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

가 각각 ${y_p}_1$, ${y_p}_2$를 해로 가진다고 하자. 주어진 방정식의 좌변을 $L[y]$로 표기하면, $L[y]$의 선형성에 의해 $y_p = {y_p}_1 + {y_p}_2$에 대해 다음을 만족하므로 합규칙이 성립한다.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

### 예제: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
기본규칙 (a)에 따라 $y_p = Ce^{\gamma x}$으로 놓고 주어진 방정식 $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$에 대입하면

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### $\gamma^2 + a\gamma + b \neq 0$인 경우
다음과 같이 미정계수 $C$를 결정하고 $y_p$를 구할 수 있다.

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### $\gamma^2 + a\gamma + b = 0$인 경우
이 경우 변형규칙 (b)를 적용해야 한다. 우선 $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$임을 이용하여 동차 상미분방정식 $y^{\prime\prime} + ay^{\prime} + by = 0$의 특성방정식의 근을 구하자.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

이로부터 동차 상미분방정식의 기저

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

을 얻는다.

##### $\gamma \neq -a-\gamma$인 경우
$y_p$로 선택했던 $Ce^{\gamma x}$이 주어진 방정식에 대응하는 동차 상미분방정식의 이중근이 아닌 해이므로, 변형규칙 (b)에 따라 이 항에 $x$를 곱하여 $y_p = Cxe^{\gamma x}$으로 놓는다.

이제 변형한 $y_p$를 다시 주어진 방정식 $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$에 대입하면

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### $\gamma = -a-\gamma$인 경우
이 경우 $y_p$로 선택했던 $Ce^{\gamma x}$이 주어진 방정식에 대응하는 동차 상미분방정식의 이중근이므로, 변형규칙 (b)에 따라 이 항에 $x^2$을 곱하여 $y_p = Cx^2 e^{\gamma x}$으로 놓는다.

이제 변형한 $y_p$를 다시 주어진 방정식 $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$에 대입하면

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
