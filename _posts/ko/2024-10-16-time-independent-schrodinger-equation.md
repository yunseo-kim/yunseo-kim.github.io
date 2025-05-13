---
title: 시간에 무관한 슈뢰딩거 방정식(Time-independent Schrödinger Equation)
description: 슈뢰딩거 방정식의 원래 형태(시간에 의존하는 슈뢰딩거 방정식) Ψ(x,t)에 변수분리법을 적용하여 시간에 무관한 슈뢰딩거 방정식
  ψ(x)를 유도하고, 이렇게 얻은 변수분리한 해가 수학적, 물리적으로 갖는 의미와 중요성을 알아본다. 그리고 변수분리한 해들의 선형결합으로 슈뢰딩거
  방정식의 일반해를 구하는 방법을 살펴본다.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 변수분리한 해: $ \Psi(x,t) = \psi(x)\phi(t)$
> - 시간의존성("wiggle factor"): $ \phi(t) = e^{-iEt/\hbar} $
> - 해밀토니언(Hamiltonian) 연산자: $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - 시간에 무관한 슈뢰딩거 방정식: $ \hat H\psi = E\psi $
> - 변수분리한 해가 갖는 물리적, 수학적 의미와 중요성:
>   1. 정상상태(stationary states)
>   2. 명확한 전체에너지 값 $E$를 가짐
>   3. 슈뢰딩거 방정식의 일반해는 변수분리한 해들의 선형결합
> - 시간에 의존하는 슈뢰딩거 방정식의 일반해: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Prerequisites
- 연속확률분포와 확률밀도
- [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/)
- [에렌페스트 정리](/posts/ehrenfest-theorem/)
- [변수분리법](/posts/Separation-of-Variables/)

## 변수분리법을 이용한 유도
[에렌페스트 정리에 관한 포스트](/posts/ehrenfest-theorem/)에서 파동함수 $\Psi$를 이용하여 알고자 하는 여러 물리량을 어떻게 계산하는지 살펴보았다. 그렇다면 중요한 것은 그 파동함수 $\Psi(x,t)$를 어떻게 얻냐는 것인데, 보통은 주어진 퍼텐셜 $V(x,t)$에 대하여 위치 $x$와 시간 $t$에 대한 편미분방정식인 [슈뢰딩거 방정식](/posts/schrodinger-equation-and-the-wave-function/)을 풀어야 한다.

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

만약 퍼텐셜 $V$가 시간 $t$에 무관할 경우, 위의 슈뢰딩거 방정식을 [변수분리법](/posts/Separation-of-Variables/)을 이용해 풀 수 있다. 다음과 같이 $x$만의 함수 $\psi$와 $t$만의 함수 $\phi$의 곱의 형태로 표현되는 해를 생각해 보자.

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

얼핏 보면 이는 터무니없이 제한적인 표현이고 전체 해의 작은 부분집합만을 구할 수 있을 것 같아 보이지만, 사실 이렇게 얻은 해가 중요한 의미를 지닐 뿐 아니라 이 분리 가능한 해들을 특정한 방식으로 더하여 일반해를 구할 수 있다.

분리 가능한 해에 대해

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

를 만족하므로, 이를 식 ($\ref{eqn:schrodinger_eqn}$)에 대입하면 슈뢰딩거 방정식을 다음과 같이 쓸 수 있다.

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

양변을 $\psi\phi$로 나누면 좌변은 $t$만의 함수이고 우변은 $x$만의 함수인

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

를 얻는다. 이 식이 해를 갖기 위해서는 양변이 상수이어야 하는데, 만약 그렇지 않다면 변수 $t$와 $x$ 중 하나는 일정하게 유지하면서 다른 한 변수만 변화시켰을 때 위 식의 한쪽 변만 바뀌게 되어 등식이 더 이상 참이 아니게 되기 때문이다. 따라서 좌변을 분리상수 $E$로 놓을 수 있다.

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

그러면 다음의 2개의 상미분방정식을 얻는데, 하나는 

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

로 시간 $t$에 대한 부분이고, 다른 하나는

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

로 공간 $x$에 대한 부분이다.

$t$에 관한 상미분방정식 ($\ref{eqn:ode_t}$)은 쉽게 풀 수 있다. 원래 이 방정식의 일반해는 $ce^{-iEt/\hbar}$이지만, 어차피 관심 있는 양은 $\phi$ 자체보다는 곱 $\psi\phi$이므로 상수 $c$는 $\psi$에 포함시킬 수 있다. 그러면

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

을 얻는다.

$x$에 관한 상미분방정식 ($\ref{eqn:t_independent_schrodinger_eqn}$)을 **시간에 무관한 슈뢰딩거 방정식(time-independent Schrödinger equation)**이라고 한다. 퍼텐셜 $V(x)$를 알아야만 이 식을 풀 수 있다.

## 물리적, 수학적 의미
앞서 변수분리법을 이용해 시간 $t$만의 함수 $\phi(t)$와 시간에 무관한 슈뢰딩거 방정식 ($\ref{eqn:t_independent_schrodinger_eqn}$)을 얻었다. 비록 원래의 **시간에 의존하는 슈뢰딩거 방정식(time-dependant Schrödinger equation)** ($\ref{eqn:schrodinger_eqn}$)의 대부분의 해는 $\psi(x)\phi(t)$의 형태로 나타낼 수 없지만, 그럼에도 불구하고 시간에 무관한 슈뢰딩거 방정식 형태가 중요한 이유는 그 해가 갖는 다음의 3가지 속성 때문이다.

### 1. 정상상태(stationary states)이다.
파동함수

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

자체는 $t$에 의존하지만, 확률밀도

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

은 시간 의존성이 상쇄되어 시간에 무관하게 일정하다. 

> 규격화할 수 있는 해에 대해서 분리상수 $E$는 실수여야 한다.
>
> 식 ($\ref{eqn:separation_of_variables}$)의 $E$를 복소수 $E_0+i\Gamma$($E_0$, $\Gamma$는 실수)로 놓으면
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> 인데, 앞서 [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/#파동함수의-규격화normalization)에서 살펴보았듯 $\int_{-\infty}^{\infty}\|\Psi\|^2dx$는 시간에 무관한 상수이어야 하므로 $\Gamma=0$이다. $\blacksquare$
{: .prompt-info }

임의의 물리량의 기댓값을 계산할 때에도 같은 일이 일어나, [에렌페스트 정리](/posts/ehrenfest-theorem/)의 식 (8)은

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

가 되므로 모든 기댓값은 시간에 대해 상수이다. 특히 $\langle x \rangle$가 상수이므로, $\langle p \rangle=0$이다.

### 2. 어떤 범위를 갖는 확률분포가 아닌, 하나의 명확한 전체에너지 값 $E$를 갖는 상태이다.
고전역학에서 전체에너지(운동에너지와 퍼텐셜에너지)를 **해밀토니언(Hamiltonian)**이라 부르고

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

로 정의하는데, 따라서 $p$를 $-i\hbar(\partial/\partial x)$로 바꾸면 양자역학에서의 해밀토니언(Hamiltonian) 연산자에는

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

가 대응한다. 따라서 시간에 무관한 슈뢰딩거 방정식 ($\ref{eqn:t_independent_schrodinger_eqn}$)은

$$ \hat H \psi = E\psi \tag{15}$$

로 쓸 수 있고, 해밀토니언의 기댓값은 다음과 같다.

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

또한

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

가 성립하므로

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

이고, 따라서 해밀토니언 $H$의 분산은

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

이다. 즉, 변수분리한 해는 전체에너지를 측정했을 때 항상 일정한 값인 $E$로 측정된다.

### 3. 시간에 의존하는 슈뢰딩거 방정식의 일반해는 변수분리한 해의 선형결합이다.

시간에 무관한 슈뢰딩거 방정식 ($\ref{eqn:t_independent_schrodinger_eqn}$)은 무한히 많은 해$[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$를 갖는다. 이를 \{$\psi_n(x)$\}라 하자. 이들 각각에 대하여 분리상수 $E_1,E_2,E_3,\dots=$\{$E_n$\}이 존재하므로, 각각의 **가능한 에너지 준위**에 대해 그에 대응하는 파동함수가 있다.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

시간에 의존하는 슈뢰딩거 방정식 ($\ref{eqn:schrodinger_eqn}$)은 임의의 두 해를 선형결합했을 때 역시 해가 된다는 성질이 있으므로, 일단 변수분리한 해를 찾으면 바로 더 일반적인 형태의 해인

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

를 얻을 수 있다. 모든 시간에 의존하는 슈뢰딩거 방정식의 해를 위의 형태로 쓸 수 있으며, 이제 남은 일은 문제에서 주어진 초기조건을 만족하도록 적절한 상수 $c_1, c_2, \dots$를 구하여 알고자 하는 특수해를 찾는 것뿐이다. 즉, 일단 시간에 무관한 슈뢰딩거 방정식을 풀 수만 있다면, 그 다음에 시간에 의존하는 슈뢰딩거 방정식의 일반해를 구하는 것은 간단하게 할 수 있다.

> 변수분리된 해 
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> 은 모든 확률과 기댓값이 시간에 무관한 정상상태이지만, 식 ($\ref{eqn:general_solution}$)의 일반해는 이러한 성질을 갖지 않음에 유의한다.
{: .prompt-warning }

## 에너지 보존
일반해 ($\ref{eqn:general_solution}$)에서 계수 \{$c_n$\}의 절댓값의 제곱 $\|c_n\|^2$은 물리적으로 해당 상태($\Psi$)를 갖는 입자의 에너지를 측정했을 때 $E_n$값이 나올 확률을 의미한다. 따라서 이 확률의 합은

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

로 1이 되어야 하며, 해밀토니언의 기댓값은

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

이다. 여기서 각 정상상태의 에너지 준위 $E_n$과 계수 \{$c_n$\}이 시간에 무관하므로, 특정한 에너지 $E_n$이 측정될 확률이나 해밀토니언 $H$의 기댓값 역시 시간에 무관하게 일정한 값을 가진다.
