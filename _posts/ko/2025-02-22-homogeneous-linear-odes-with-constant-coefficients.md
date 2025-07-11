---
title: "상수계수를 갖는 2계 동차 선형 상미분방정식"
description: "특성방정식의 판별식의 부호에 따라, 각각의 경우에 상수계수 동차 선형 상미분방정식의 일반해가 어떤 형태를 띄는지 살펴본다."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 상수계수를 갖는 2계 동차 선형 상미분방정식: $y^{\prime\prime} + ay^{\prime} + by = 0$
> - **특성방정식(characteristic equation)**: $\lambda^2 + a\lambda + b = 0$
> - 특성방정식의 판별식 $a^2 - 4b$의 부호에 따라 일반해의 형태를 표와 같이 세 가지 경우로 나눌 수 있음
>
> | 경우 | 특성방정식의 해 | 상미분방정식의 해의 기저 | 상미분방정식의 일반해 |
> | :---: | :---: | :---: | :---: |
> | I | 서로 다른 실근<br>$\lambda_1$, $\lambda_2$ | $e^{\lambda_1 x}$, $e^{\lambda_2 x}$ | $y = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$ |
> | II | 실이중근<br> $\lambda = -\cfrac{1}{2}a$ | $e^{-ax/2}$, $xe^{-ax/2}$ | $y = (c_1 + c_2 x)e^{-ax/2}$ |
> | III | 켤레복소근<br> $\lambda_1 = -\cfrac{1}{2}a + i\omega$, <br> $\lambda_2 = -\cfrac{1}{2}a - i\omega$ | $e^{-ax/2}\cos{\omega x}$, <br> $e^{-ax/2}\sin{\omega x}$ | $y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x})$ |
{: .prompt-info }

## Prerequisites
- [베르누이 방정식(Bernoulli Equation)](/posts/Bernoulli-Equation/)
- [2계 동차 선형 상미분방정식 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- 오일러 공식

## 특성방정식 (characteristic equation)
계수 $a$와 $b$가 상수인 2계 동차 선형 상미분방정식

$$ y^{\prime\prime} + ay^{\prime} + by = 0 \label{eqn:ode_with_constant_coefficients}\tag{1} $$

을 살펴보자. 이러한 형태의 방정식은 기계적, 전기적 진동에서 중요하게 응용된다.

앞서 [베르누이 방정식(Bernoulli Equation)](/posts/Bernoulli-Equation/)에서 로지스틱 방정식의 일반해를 구한 바 있으며, 그에 따르면 상수계수 $k$를 갖는 1계 선형 상미분방정식

$$ y^\prime + ky = 0 $$

의 해는 지수함수 $y = ce^{-kx}$이다. (해당 글의 식 (4)에서 $A=-k$, $B=0$인 경우)

따라서, 비슷한 형태의 방정식인 ($\ref{eqn:ode_with_constant_coefficients}$)에 대해서도

$$y=e^{\lambda x}\label{eqn:general_sol}\tag{2}$$

형태의 해를 우선 시도해 볼 수 있다.

> 물론 이는 어디까지나 추측에 불과하며, 정말로 일반해가 이런 형태일 거라는 보장은 전혀 없다. 하지만 뭐가 되었든 선형 독립인 두 해를 일단 구하기만 한다면, [2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-of-second-order/#기저와-일반해)에서 살펴봤다시피 [중첩의 원리](/posts/homogeneous-linear-odes-of-second-order/#중첩의-원리)에 의해 일반해를 구할 수 있다.  
> 잠시 뒤에 보겠지만, [다른 형태의 해를 구해야 하는 경우](#ii-실이중근-lambda---cfraca2)도 있다.
{: .prompt-info }

식 ($\ref{eqn:general_sol}$)와 그 도함수

$$ y^\prime = \lambda e^{\lambda x}, \quad y^{\prime\prime} = \lambda^2 e^{\lambda x} $$

을 식 ($\ref{eqn:ode_with_constant_coefficients}$)에 대입하면

$$ (\lambda^2 + a\lambda + b)e^{\lambda x} = 0 $$

을 얻는다. 따라서, 만약 $\lambda$가 **특성방정식(characteristic equation)**

$$ \lambda^2 + a\lambda + b = 0 \label{eqn:characteristic_eqn}\tag{3}$$

의 해라면 지수함수 ($\ref{eqn:general_sol}$)는 상미분방정식 ($\ref{eqn:ode_with_constant_coefficients}$)의 해이다. 이차방정식 ($\ref{eqn:characteristic_eqn}$)의 해를 구하면

$$ \begin{align*}
\lambda_1 &= \frac{1}{2}\left(-a + \sqrt{a^2 - 4b}\right), \\
\lambda_2 &= \frac{1}{2}\left(-a - \sqrt{a^2 - 4b}\right)
\end{align*}\label{eqn:lambdas}\tag{4} $$

이고, 이로부터 두 함수

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} \tag{5}$$

이 방정식 ($\ref{eqn:ode_with_constant_coefficients}$)의 해가 된다.

> **특성방정식(characteristic equation)**과 **보조방정식(auxiliary equation)** 두 용어가 자주 혼용되곤 하는데, 둘은 완전히 같은 의미이다. 어느 쪽으로 지칭해도 상관없다.
{: .prompt-tip }

이제, 특성방정식 ($\ref{eqn:characteristic_eqn}$)의 판별식 $a^2 - 4b$의 부호에 따라 경우를 세 가지로 나눌 수 있다.
- $a^2 - 4b > 0$: 서로 다른 두 실근
- $a^2 - 4b = 0$: 실이중근
- $a^2 - 4b < 0$: 켤레복소근

## 특성방정식의 판별식의 부호에 따른 일반해의 형태
### I. 서로 다른 두 실근 $\lambda_1$과 $\lambda_2$
이 경우 임의의 구간에서 방정식 ($\ref{eqn:ode_with_constant_coefficients}$)의 해의 기저는

$$ y_1 = e^{\lambda_1 x}, \quad y_2 = e^{\lambda_2 x} $$

이며, 이에 따른 일반해는

$$ y = c_1 e^{\lambda_1 x} + c_2 e^{\lambda_2 x} \label{eqn:general_sol_1}\tag{6}$$

이다.

### II. 실이중근 $\lambda = -\cfrac{a}{2}$
$a^2 - 4b = 0$일 경우 이차방정식 ($\ref{eqn:characteristic_eqn}$)은 한 개의 해 $\lambda = \lambda_1 = \lambda_2 = -\cfrac{a}{2}$만을 얻게 되며, 따라서 이로부터 얻을 수 있는 $y = e^{\lambda x}$ 형태의 해는

$$ y_1 = e^{-(a/2)x} $$

의 한 개뿐이다. 기저를 얻기 위해서는 $y_1$과 독립적인 다른 형태의 두 번째 해 $y_2$를 알아내야 한다. 

이러한 상황에서 활용할 수 있는 것이 앞서 알아보았던 [계수내림](/posts/homogeneous-linear-odes-of-second-order/#계수내림-reduction-of-order)이다. 찾고자 하는 두 번째 해를 $y_2=uy_1$으로 놓고, 

$$ \begin{align*}
y_2 &= uy_1, \\
y_2^{\prime} &= u^{\prime}y_1 + uy_1^{\prime}, \\
y_2^{\prime\prime} &= u^{\prime\prime}y_1 + 2u^{\prime}y_1^{\prime} + uy_1^{\prime\prime}
\end{align*} $$

을 방정식 ($\ref{eqn:ode_with_constant_coefficients}$)에 대입하면

$$ (u^{\prime\prime}y_1 + 2u^\prime y_1^\prime + uy_1^{\prime\prime}) + a(u^\prime y_1 + uy_1^\prime) + buy_1 = 0 $$

을 얻는다. $u^{\prime\prime}$, $u^\prime$, $u$ 각 항끼리 모아서 정리하면

$$ y_1u^{\prime\prime} + (2y_1^\prime + ay_1)u^\prime + (y_1^{\prime\prime} + ay_1^\prime + by_1)u = 0 $$

이다. 여기서 $y_1$이 방정식 ($\ref{eqn:ode_with_constant_coefficients}$)의 해이기 때문에 마지막 괄호 안의 식은 $0$이며,

$$ 2y_1^\prime = -ae^{-ax/2} = -ay_1 $$

이므로 첫 번째 괄호 안의 식 역시 $0$이다. 따라서 $u^{\prime\prime}y_1 = 0$만 남게 되며, 이로부터 $u^{\prime\prime}=0$이다. 두 번 적분하면 $u = c_1x + c_2$가 되며, 적분상수 $c_1$과 $c_2$는 어떤 값이든 될 수 있으므로 단순히 $c_1=1$, $c_2=0$을 선택하여 $u=x$로 놓을 수 있다. 그러면 $y_2 = uy_1 = xy_1$이 되며, $y_1$과 $y_2$는 선형 독립이므로 이 둘은 기저를 형성한다. 따라서 특성방정식 ($\ref{eqn:characteristic_eqn}$)이 중근을 갖는 경우에 임의의 구간에서의 방정식 ($\ref{eqn:ode_with_constant_coefficients}$)의 해의 기저는

$$ e^{-ax/2}, \quad xe^{-ax/2} $$

이고, 이에 대응하는 일반해는

$$ y = (c_1 + c_2x)e^{-ax/2} \label{eqn:general_sol_2}\tag{7}$$

이다.

### III. 켤레복소근 $-\cfrac{1}{2}a + i\omega$와 $-\cfrac{1}{2}a - i\omega$
이 경우 $a^2 - 4b < 0$이고 $\sqrt{-1} = i$이므로 식 ($\ref{eqn:lambdas}$)에서

$$ \cfrac{1}{2}\sqrt{a^2 - 4b} = \cfrac{1}{2}\sqrt{-(4b - a^2)} = \sqrt{-(b-\frac{1}{4}a^2)} = i\sqrt{b - \frac{1}{4}a^2} $$

이며, 여기서 실수 $\sqrt{b-\cfrac{1}{4}a^2} = \omega$로 정의하자.

$\omega$를 위와 같이 정의하면 특성방정식 ($\ref{eqn:characteristic_eqn}$)의 해는 켤레복소근 $\lambda = -\cfrac{1}{2}a \pm i\omega$가 되며, 이에 대응하는 방정식 ($\ref{eqn:ode_with_constant_coefficients}$)의 두 복소해

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x}, \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x}
\end{align*} $$

를 얻는다. 다만 이 경우에도 허수가 아닌 실수해의 기저를 다음과 같이 얻을 수 있다.

오일러 공식(Euler formula)

$$ e^{it} = \cos t + i\sin t \label{eqn:euler_formula}\tag{8}$$

와, 위 식에서 $t$ 자리에 $-t$를 대입하여 얻는

$$ e^{-it} = \cos t - i\sin t $$

의 두 식을 변끼리 더하고 빼면 다음을 얻는다.

$$ \begin{align*}
\cos t &= \frac{1}{2}(e^{it} + e^{-it}), \\
\sin t &= \frac{1}{2i}(e^{it} - e^{-it}).
\end{align*} \label{eqn:cos_and_sin}\tag{9}$$

실수부 $r$과 허수부 $it$를 갖는 복소변수 $z = r + it$의 복소지수함수 $e^z$는 실함수 $e^r$, $\cos t$와 $\sin t$를 사용하여 다음과 같이 정의할 수 있다.

$$ e^z = e^{r + it} = e^r e^{it} = e^r(\cos t + i\sin t) \label{eqn:complex_exp}\tag{10}$$

여기서 $r=-\cfrac{1}{2}ax$, $t=\omega x$로 놓으면 다음과 같이 쓸 수 있다.

$$ \begin{align*}
e^{\lambda_1 x} &= e^{-(a/2)x + i\omega x} = e^{-(a/2)x}(\cos{\omega x} + i\sin{\omega x}) \\
e^{\lambda_2 x} &= e^{-(a/2)x - i\omega x} = e^{-(a/2)x}(\cos{\omega x} - i\sin{\omega x})
\end{align*} $$

[중첩의 원리](/posts/homogeneous-linear-odes-of-second-order/#중첩의-원리)에 의해 위의 복소해들의 합과 상수곱 또한 해가 된다. 따라서 두 등식을 변끼리 더하고 양변에 $\cfrac{1}{2}$을 곱하면 첫 번째 실수해 $y_1$을 다음과 같이 얻을 수 있다.

$$ y_1 = e^{-(a/2)x} \cos{\omega x}. \label{eqn:basis_1}\tag{11} $$

같은 방법으로, 첫 번째 등식에서 두 번째 등식을 변끼리 빼고 양변에 $\cfrac{1}{2i}$를 곱하여 두 번째 실수해 $y_2$를 얻을 수 있다.

$$ y_2 = e^{-(a/2)x} \sin{\omega x}. \label{eqn:basis_2}\tag{12}$$

$\cfrac{y_1}{y_2} = \cot{\omega x}$이고 이는 상수가 아니므로, $y_1$과 $y_2$는 모든 구간에서 선형 독립이며 따라서 방정식 ($\ref{eqn:ode_with_constant_coefficients}$)의 실수해의 기저를 이룬다. 이로부터 일반해

$$ y = e^{-ax/2}(A\cos{\omega x} + B\sin{\omega x}) \quad \text{(}A,\, B\text{는 임의의 상수)} \label{eqn:general_sol_3}\tag{13}$$

를 얻는다.
