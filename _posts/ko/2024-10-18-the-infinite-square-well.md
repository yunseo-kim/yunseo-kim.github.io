---
title: 1차원 무한 사각 우물(The 1D Infinite Square Well)
description: 양자역학의 기본 개념들을 잘 보여주는 간단하면서도 중요한 대표 문제, 1차원 무한 사각 우물 문제를 살펴본다. 이러한 이상적인
  상황에서 입자의 n번째 정상상태 ψ(x)와 에너지 E를 구하고, ψ(x)가 갖는 중요한 수학적 성질 4가지를 알아본다. 그리고 이로부터 일반해
  Ψ(x,t)을 구한다.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 1차원 무한 사각 우물 문제: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{이외의 경우}
>   \end{cases}$$
> - 경계조건: $ \psi(0) = \psi(a) = 0 $
> - $n$번째 정상상태의 에너지 준위: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - 우물 안에서의 시간에 무관한 슈뢰딩거 방정식의 해:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - 각 정상상태 $\psi_n$의 물리적 해석: 
>   - 길이 $a$인 줄에서 나타나는 정상파 형태
>   - **바닥상태(ground state)**: 가장 낮은 에너지를 갖는 정상상태 $\psi_1$
>   - **들뜬 상태(exited states)**: $n^2$에 비례하여 에너지가 증가하는 나머지 $n\geq 2$인 상태들
> - $\psi_n$의 중요한 4가지 수학적 성질:
>   1. 퍼텐셜 $V(x)$가 대칭성을 갖는다면, 우물 중심에 대해 짝함수, 홀함수가 교대로 나타남
>   2. 에너지가 커질수록 각 연속된 상태는 **마디(node)**가 하나씩 증가함
>   3. **직교규격성(orthonomality)**을 가짐
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. **완전성(completeness)**을 가짐
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - 슈뢰딩거 방정식의 일반해(정상상태들의 선형결합):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{이때 계수 }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Prerequisites
- 연속확률분포와 확률밀도
- 직교성과 규격화(선형대수학)
- 푸리에 급수와 완전성(선형대수학)
- [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/)
- [에렌페스트 정리](/posts/ehrenfest-theorem/)
- [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/)

## 주어진 퍼텐셜 조건
퍼텐셜이

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{이외의 경우}
\end{cases} \tag{1}$$

라고 하면, 이 퍼텐셜 안의 입자는 범위 $0<x<a$ 내에서는 자유입자이며 양쪽 끝($x=0$과 $x=a$)에서는 무한한 힘이 작용하여 탈출하지 못한다. 고전적인 모형에서는 이를 앞뒤로 완전탄성충돌을 반복하며 비보존력이 작용하지 않는 무한 왕복 운동으로 해석한다. 비록 이러한 퍼텐셜은 지극히 인위적이고 단순하지만, 오히려 그렇기에 추후 양자역학을 공부하면서 다른 물리적인 상황들을 살펴볼 때 유용한 참고 사례가 되어줄 수 있으므로 주의깊게 확인할 필요가 있다.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *이미지 출처*
> - 저작자: 위키미디어 유저 [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## 모델 및 경계조건 설정
우물 바깥쪽에서는 입자를 발견할 확률이 $0$이므로 $\psi(x)=0$이다. 우물 안에서는 $V(x)=0$이므로 [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/)은

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

이고, 즉

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ 여기서 } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

의 형태로 쓸 수 있다.

> 여기서 $E\geq 0$이라고 가정한다.
{: .prompt-info }

이것은 고전적인 **단순조화진동자(simple harmonic oscillator)**를 기술하는 식이며, 일반해는

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

이다. 여기서 $A$와 $B$는 임의의 상수이며, 문제 상황에 맞는 특수해를 구할 때 전형적으로 이 상수는 문제에서 주어진 **경계조건**으로 결정된다. <u>$\psi(x)$의 경우 보통은 $\psi$와 $d\psi/dx$가 모두 연속이라는 것이 경계조건이 되나, 퍼텐셜이 무한대가 되는 곳은 $\psi$만 연속이다.</u>

## 시간에 무관한 슈뢰딩거 방정식의 해 구하기

$\psi(x)$가 연속이므로

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

이 되어 우물 바깥쪽의 해와 연결되어야 한다. 식 ($\ref{eqn:psi_general_solution}$)에서 $x=0$일 때

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

이므로, ($\ref{eqn:boundary_conditions}$)를 대입하면 $B=0$이어야 한다.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

그러면 $\psi(a)=A\sin{ka}$이므로, 식 ($\ref{eqn:boundary_conditions}$)의 $\psi(a)=0$을 만족하려면 $A=0$(자명해)이거나 $\sin{ka}=0$이다. 따라서

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

이다. 여기서도 마찬가지로 $k=0$은 자명해이며, $\psi(x)=0$이 되어 규격화할 수 없으므로 이 문제에서 찾고자 하는 해는 아니다. 또한 $\sin(-\theta)=-\sin(\theta)$이어서 음의 부호는 식 ($\ref{eqn:psi_without_B}$)의 $A$에 흡수시킬 수 있으므로, $ka>0$인 경우만 고려하여도 일반성을 잃지 않는다. 그러므로 $k$에 대하여 가능한 해는

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

이다.

그러면 $\psi_n=A\sin{k_n x}$이고 $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$이므로, 식 ($\ref{eqn:t_independent_schrodinger_eqn}$)에 대입하면 가능한 $E$값은 다음과 같다.

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

고전적인 경우와는 대단히 대조적으로, 무한 사각 우물 안의 양자 입자는 임의의 에너지를 가질 수 없고 허용된 값들 중 하나를 가져야 한다.

> 시간에 무관한 슈뢰딩거 방정식의 해에 적용되는 경계조건에 의해 에너지가 양자화된다.
{: .prompt-info }

이제 $\psi$를 규격화하여 $A$를 구할 수 있다.

> 원래는 $\Psi(x,t)$를 규격화하는 것이지만, [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/#1-정상상태stationary-states이다)의 식 (11)에 의해 이것은 $\psi(x)$를 규격화하는 것에 해당한다.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

이것은 엄밀히는 $A$의 크기만을 결정하지만, $A$의 위상은 아무런 물리적 의미를 갖지 않으므로 그냥 양의 실수 제곱근을 $A$로 사용해도 된다. 따라서 우물 안에서의 해는

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

이다.

## 각 정상상태 $\psi_n$의 물리적 해석
식 ($\ref{eqn:psi_n}$)과 같이 시간에 무관한 슈뢰딩거 방정식으로부터 각 에너지 준위 $n$에 대한 무한 개의 해를 구했다. 이들 중 처음 몇 개를 그림으로 그리면 아래 이미지와 같다.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *이미지 출처*
> - 저작자: 위키미디어 유저 [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

이 상태들은 길이 $a$인 줄에서 나타나는 정상파 형태를 띄며, 가장 낮은 에너지를 갖는 $\psi_1$을 **바닥상태(ground state)**라고 하고, $n^2$에 비례하여 에너지가 증가하는 나머지 $n\geq 2$인 상태들을 **들뜬 상태(exited states)**라고 한다.

## $\psi_n$의 중요한 4가지 수학적 성질
모든 함수 $\psi_n(x)$는 다음의 중요한 4가지 성질을 가진다. 이 네 성질은 매우 강력하며, 무한한 사각형 우물에만 국한되지 않는다. 첫 번째 성질은 퍼텐셜 자체가 대칭성이 있는 함수라면 언제나 성립하며, 두 번째, 세 번째, 네 번째 성질은 퍼텐셜 모양에 상관 없이 나타나는 일반적 성질이다.

### 1. 우물 중심에 대해 짝함수, 홀함수가 교대로 나타난다.
양의 정수 $n$에 대하여 $\psi_{2n-1}$은 짝함수, $\psi_{2n}$은 홀함수이다.

### 2. 에너지가 커질수록 각 연속된 상태는 마디가 하나씩 증가한다.
양의 정수 $n$에 대하여 $\psi_n$은 $(n-1)$개의 **마디(node)**를 가진다.

### 3. 이 상태는 직교성(orthogonality)을 갖는다.

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

인 의미로 서로 **직교(orthogonal)**한다.

> 지금 살펴보고 있는 무한 사각 우물의 경우 $\psi$는 실수이므로 $\psi_m$의 켤레복소수($^*$)를 취하지 않아도 되지만, 그렇지 않은 경우를 위해 항상 붙이는 습관을 들이는 것이 좋다.
{: .prompt-tip }

#### 증명
$m\neq n$일 때,

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

$m=n$일 때는 규격화에 의하여 이 적분은 $1$이 되며, **크로네커 델타(Kronecker delta)** $\delta_{mn}$을 쓰면 직교성과 규격화를

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

의 한 표현으로 함께 나타낼 수도 있다. 이때 $\psi$는 **직교규격화(orthonormal)**되어 있다고 한다.

### 4. 이 함수들은 완전성(completeness)을 갖는다.
임의의 다른 함수 $f(x)$를 선형결합

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

로 쓸 수 있다는 의미에서 이 함수들은 **완전(complete)**하다. 식 ($\ref{eqn:fourier_series}$)는 $f(x)$의 **푸리에 급수(Fourier series)**이고, 임의의 함수를 이렇게 전개할 수 있다는 것을 **디리클레 정리(Dirichlet's theorem)**라고 부른다.

## 푸리에 방법(Fourier's trick)을 이용한 계수 $c_n$ 구하기
$f(x)$가 주어졌을 때, 위의 완전성(completeness)과 직교규격성(orthonormality)을 이용하면 **푸리에 방법(Fourier's trick)**이라 불리는 다음 방법으로 계수 $c_n$을 구할 수 있다. 식 ($\ref{eqn:fourier_series}$)의 양변에 $\psi_m(x)^*$를 곱하고 적분하면, 식 ($\ref{eqn:orthonomality}$)와 ($\ref{eqn:kronecker_delta}$)에 의해

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

을 얻는다.

> 크로네커 델타로 인해 합에서 $n=m$인 항을 제외한 다른 모든 항이 없어지는 것을 주목한다.
{: .prompt-info }

따라서 $f(x)$를 전개할 때 $n$차 계수는

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

이다.

## 시간에 의존하는 슈뢰딩거 방정식의 일반해 $\Psi(x,t)$ 구하기
무한 사각 우물의 각 정상상태는 ['시간에 무관한 슈뢰딩거 방정식' 포스트의 식 (10)](/posts/time-independent-schrodinger-equation/#1-정상상태stationary-states이다)과 앞서 구한 식 ($\ref{eqn:psi_n}$)에 의해

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

이다. 또한 [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/#3-시간에-의존하는-슈뢰딩거-방정식의-일반해는-변수분리한-해의-선형결합이다)에서 슈뢰딩거 방정식의 일반해를 정상상태들의 선형결합으로 표현할 수 있음을 앞서 살펴보았다. 따라서

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

로 쓸 수 있다. 이제 다음 조건을 만족하는 계수 $c_n$을 찾아내기만 하면 된다.

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

앞서 살펴본 $\psi$의 완전성에 의해 위를 만족하는 $c_n$이 항상 존재하며, 식 ($\ref{eqn:coefficients_n}$)의 $f(x)$에 $\Psi(x,0)$을 대입하여 구할 수 있다.

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

초기조건으로 $\Psi(x,0)$이 주어지면 식 ($\ref{eqn:calc_of_cn}$)을 이용하여 전개 계수 $c_n$을 구하고, 이를 식 ($\ref{eqn:general_solution}$)에 대입하여 $\Psi(x,t)$를 구한다. 그러고 나서는 [에렌페스트 정리](/posts/ehrenfest-theorem/)의 과정에 따라 관심 있는 임의의 물리량을 계산할 수 있다. 이 방법은 무한 사각 우물뿐만 아니라 임의의 퍼텐셜에 적용할 수 있으며, 다만 $\psi$ 함수의 형태와 허용된 에너지 준위에 관한 식만 달라질 뿐이다.

## 에너지 보존($\langle H \rangle=\sum\|c_n\|^2E_n$) 유도
$\psi(x)$의 직교규격성(식 [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$])을 이용하여 앞서 [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/#에너지-보존)에서 간략히 살펴봤던 에너지 보존을 유도하자. $c_n$은 시간에 무관하므로 $t=0$일 경우에 대해 참임을 보이기만 하면 된다.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

또한

$$ \hat{H}\psi_n = E_n\psi_n $$

이므로 다음을 얻는다.

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
