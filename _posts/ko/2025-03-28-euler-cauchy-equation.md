---
title: "오일러-코시 방정식"
description: "보조방정식의 판별식의 부호에 따라, 각각의 경우에 오일러-코시 방정식의 일반해가 어떤 형태를 띄는지 살펴본다."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 오일러-코시 방정식: $x^2y^{\prime\prime} + axy^{\prime} + by = 0$
> - **보조방정식(auxiliary equation)**: $m^2 + (a-1)m + b = 0$
> - 보조방정식의 판별식 $(1-a)^2 - 4b$의 부호에 따라 일반해의 형태를 표와 같이 세 가지 경우로 나눌 수 있음
>
> | 경우 | 보조방정식의 해 | 오일러-코시 방정식의 해의 기저 | 오일러-코시 방정식의 일반해 |
> | :---: | :---: | :---: | :---: |
> | I | 서로 다른 실근<br>$m_1$, $m_2$ | $x^{m_1}$, $x^{m_2}$ | $y = c_1 x^{m_1} + c_2 x^{m_2}$ |
> | II | 실이중근<br> $m = \cfrac{1-a}{2}$ | $x^{(1-a)/2}$, $x^{(1-a)/2}\ln{x}$ | $y = (c_1 + c_2 \ln x)x^m$ |
> | III | 켤레복소근<br> $m_1 = \cfrac{1}{2}(1-a) + i\omega$, <br> $m_2 = \cfrac{1}{2}(1-a) - i\omega$ | $x^{(1-a)/2}\cos{(\omega \ln{x})}$, <br> $x^{(1-a)/2}\sin{(\omega \ln{x})}$ | $y = x^{(1-a)/2}[A\cos{(\omega \ln{x})} + B\sin{(\omega \ln{x})}]$ |
{: .prompt-info }

## Prerequisites
- [2계 동차 선형 상미분방정식 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [상수계수를 갖는 2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- 오일러 공식

## 보조방정식 (auxiliary equation)
**오일러-코시 방정식(Euler-Cauchy equation)**은 주어진 상수 $a$와 $b$, 그리고 미지의 함수 $y(x)$를 갖는

$$ x^2y^{\prime\prime} + axy^{\prime} + by = 0 \label{eqn:euler_cauchy_eqn}\tag{1} $$

형태의 상미분방정식이다. 식 ($\ref{eqn:euler_cauchy_eqn}$)에

$$ y=x^m, \qquad y^{\prime}=mx^{m-1}, \qquad y^{\prime\prime}=m(m-1)x^{m-2} $$

을 대입하면

$$ x^2m(m-1)x^{m-2} + axmx^{m-1} + bx^m = 0, $$

즉

$$ [m(m-1) + am + b]x^m = 0 $$

을 얻는다. 이로부터 보조방정식

$$ m^2 + (a-1)m + b = 0 \label{eqn:auxiliary_eqn}\tag{2} $$

을 얻으며, $y=x^m$이 오일러-코시 방정식 ($\ref{eqn:euler_cauchy_eqn}$)의 해가 되기 위한 필요충분조건은 $m$이 보조방정식 ($\ref{eqn:auxiliary_eqn}$)의 해가 되는 것이다.

이차방정식 ($\ref{eqn:auxiliary_eqn}$)의 해를 구하면

$$ \begin{align*}
m_1 &= \frac{1}{2}\left[(1-a) + \sqrt{(1-a)^2 - 4b} \right], \\
m_2 &= \frac{1}{2}\left[(1-a) - \sqrt{(1-a)^2 - 4b} \right]
\end{align*}\label{eqn:m1_and_m2}\tag{3} $$

이고, 이로부터 두 함수

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2}$$

이 방정식 ($\ref{eqn:euler_cauchy_eqn}$)의 해가 된다.

[상수계수를 갖는 2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-with-constant-coefficients/)에서와 마찬가지로, 보조방정식 ($\ref{eqn:auxiliary_eqn}$)의 판별식 $(1-a)^2 - 4b$의 부호에 따라 경우를 세 가지로 나눌 수 있다.
- $(1-a)^2 - 4b > 0$: 서로 다른 두 실근
- $(1-a)^2 - 4b = 0$: 실이중근
- $(1-a)^2 - 4b < 0$: 켤레복소근

## 보조방정식의 판별식의 부호에 따른 일반해의 형태
### I. 서로 다른 두 실근 $m_1$과 $m_2$
이 경우 임의의 구간에서 방정식 ($\ref{eqn:euler_cauchy_eqn}$)의 해의 기저는

$$ y_1 = x^{m_1}, \quad y_2 = x^{m_2} $$

이며, 이에 따른 일반해는

$$ y = c_1 x^{m_1} + c_2 x^{m_2} \label{eqn:general_sol_1}\tag{4}$$

이다.

### II. 실이중근 $m = \cfrac{1-a}{2}$
$(1-a)^2 - 4b = 0$, 즉 $b=\cfrac{(1-a)^2}{4}$일 경우 이차방정식 ($\ref{eqn:auxiliary_eqn}$)는 한 개의 해 $m = m_1 = m_2 = \cfrac{1-a}{2}$만을 얻게 되며, 따라서 이로부터 얻을 수 있는 $y = x^m$ 형태의 한 해는

$$ y_1 = x^{(1-a)/2} $$

이고, 오일러-코시 방정식 ($\ref{eqn:euler_cauchy_eqn}$)은

$$ y^{\prime\prime} + \frac{a}{x}y^{\prime} + \frac{(1-a)^2}{4x^2}y = 0 \label{eqn:standard_form}\tag{5} $$

의 형태가 된다. 이제 선형독립인 또다른 해 $y_2$를 [계수내림](/posts/homogeneous-linear-odes-of-second-order/#계수내림-reduction-of-order)을 이용하여 구하자.

찾고자 하는 두 번째 해를 $y_2=uy_1$으로 놓으면

$$ u = \int U, \qquad U = \frac{1}{y_1^2}\exp\left(-\int \frac{a}{x}\ dx \right) $$

를 얻는다.

$\exp \left(-\int \cfrac{a}{x}\ dx \right) = \exp (-a\ln x) = \exp(\ln{x^{-a}}) = x^{-a}$이므로,

$$ U = \frac{x^{-a}}{y_1^2} = \frac{x^{-a}}{x^{(1-a)}} = \frac{1}{x} $$

이고 적분하면 $u = \ln x$를 얻는다.

따라서 $y_2 = uy_1 = y_1 \ln x$이고, $y_1$과 $y_2$는 그 몫이 상수가 아니므로 선형독립이다. 기저 $y_1$과 $y_2$에 대응하는 일반해는

$$ y = (c_1 + c_2 \ln x)x^m \label{eqn:general_sol_2}\tag{6}$$

이다.

### III. 켤레복소근
이 경우 보조방정식 ($\ref{eqn:auxiliary_eqn}$)의 해는 $m = \cfrac{1}{2}(1-a) \pm i\sqrt{b - \frac{1}{4}(1-a)^2}$이 되며, 이에 대응하는 방정식 ($\ref{eqn:euler_cauchy_eqn}$)의 두 복소해는 $x=e^{\ln x}$임을 이용하여 다음과 같이 쓸 수 있다.

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2 + i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}, \\
x^{m_2} &= x^{(1-a)/2 - i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}(e^{\ln x})^{-i\sqrt{b - \frac{1}{4}(1-a)^2}} \\
&= x^{(1-a)/2}e^{i(-\sqrt{b - \frac{1}{4}(1-a)^2}\ln x)}.
\end{align*} \tag{7}$$

$t=\sqrt{b - \frac{1}{4}(1-a)^2}\ln x$로 놓고 오일러 공식 $e^{it} = \cos{t} + i\sin{t}$를 이용하면

$$ \begin{align*}
x^{m_1} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right], \\
x^{m_2} &= x^{(1-a)/2}\left[\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) - i\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]
\end{align*} \tag{8}$$

임을 알 수 있고, 이로부터 다음의 두 실수해

$$ \begin{align*}
\frac{x^{m_1} + x^{m_2}}{2} &= x^{(1-a)/2}\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right), \\
\frac{x^{m_1} - x^{m_2}}{2i} &= x^{(1-a)/2}\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right)
\end{align*} \tag{9}$$

를 얻는다.

이들의 몫 $\cos\left(\sqrt{b - \frac{1}{4}(1-a)^2}\ln x \right)$가 상수가 아니므로 위의 두 해는 선형독립이며, 따라서 [중첩의 원리](/posts/homogeneous-linear-odes-of-second-order/#중첩의-원리)에 의해 오일러-코시 방정식 ($\ref{eqn:euler_cauchy_eqn}$)의 기저를 형성한다. 이로부터 다음의 실수 일반해를 얻는다.

$$ y = x^{(1-a)/2} \left[ A\cos\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) + B\sin\left(\sqrt{b - \tfrac{1}{4}(1-a)^2}\ln x \right) \right]. \label{eqn:general_sol_3}\tag{10}$$

다만, 오일러-코시 방정식에서 보조방정식이 켤레복소근을 갖는 경우는 실질적인 중요성이 그리 크진 않다.

## 상수계수를 갖는 2계 동차 선형 상미분방정식으로의 변환
오일러-코시 방정식은 변수 치환을 통해 [상수계수를 갖는 2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-with-constant-coefficients/)으로 변환할 수 있다.

$x = e^t$으로 치환하면

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

가 되어, 오일러-코시 방정식 ($\ref{eqn:euler_cauchy_eqn}$)은 다음과 같이 $t$에 대한 상수계수 동차 선형 상미분방정식으로 바뀐다.

$$ y^{\prime\prime}(t) + (a-1)y^{\prime}(t) + by(t) = 0. \label{eqn:substituted}\tag{11} $$

방정식 ($\ref{eqn:substituted}$)을 [상수계수를 갖는 2계 동차 선형 상미분방정식](/posts/homogeneous-linear-odes-with-constant-coefficients/)의 해법을 적용하여 $t$에 대해 풀고, 그렇게 얻은 해를 $t = \ln{x}$임을 이용하여 다시 $x$에 대한 해로 변환하면 [앞서 살펴본 것과 동일한 결과](#보조방정식의-판별식의-부호에-따른-일반해의-형태)를 얻는다.
