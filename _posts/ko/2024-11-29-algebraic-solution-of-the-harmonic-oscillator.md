---
title: 조화진동자(The Harmonic Oscillator)의 대수적 풀이
description: 양자역학에서의 조화진동자에 대한 슈뢰딩거 방정식을 세우고, 해당 방정식의 대수적인 풀이법을 알아본다. 교환자와 정준교환관계
  및 사다리연산자로부터 임의의 정상상태의 파동함수와 에너지 준위를 구한다.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 진폭이 충분히 작다면 어떠한 진동도 단순조화진동(simple harmonic oscillation)으로 근사할 수 있으며, 이 덕에 단순조화진동은 물리학에서 중요한 의미 가짐
> - 조화진동자: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **교환자(commutator)**:
>   - 두 연산자가 얼마나 잘 교환(commute)되지 않는지를 나타내는 이항 연산
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **정준교환관계(canonical commutation relation)**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **사다리연산자(ladder operators)**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$를 **올림연산자(raising operator)**, $\hat{a}\_-$를 **내림연산자(lowering operator)**라고 부름
>   - 임의의 정상상태에 대해 에너지 준위를 올리거나 내릴 수 있으며, 따라서 시간에 무관한 슈뢰딩거 방정식의 한 해만 찾으면 다른 해도 모두 찾을 수 있음
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - $n$번째 정상상태의 파동함수와 에너지 준위:
>   - 바닥상태($0$번째 정상상태):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$번째 정상상태:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$는 $\hat{a}\_\pm$의 **에르미트 켤레(hermitian conjugate)**이자 **수반연산자(adjoint operator)**임
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - 이로부터 다음의 성질을 유도할 수 있음:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - $\hat{x}$와 $\hat{p}$의 거듭제곱을 포함하는 물리량의 기댓값 계산 방법:
>   1. 사다리연산자의 정의를 이용하여 $\hat{x}$와 $\hat{p}$를 올림연산자와 내림연산자로 표현
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. 기댓값을 구하고자 하는 물리량을 위의 $\hat{x}$와 $\hat{p}$의 식을 이용하여 표현
>   3. $\left(\hat{a}\_\pm \right)^m$은 $\psi\_{n\pm m}$에 비례하므로 $\psi_n$과는 직교하여 $0$이 됨을 이용
>   4. 사다리연산자의 성질을 이용하여 적분 계산
{: .prompt-info }

## Prerequisites
- [변수분리법](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/)
- [에렌페스트 정리](/posts/ehrenfest-theorem/)
- [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/)
- [1차원 무한 사각 우물](/posts/the-infinite-square-well/)
- 에르미트 켤레(hermitian conjugate), 수반 연산자(adjoint operator)

## 모델 설정
### 고전역학에서의 조화진동자
고전적인 조화진동자의 대표적인 예시는 질량 $m$이 용수철 상수 $k$인 용수철에 매달려 있는 경우의 운동(마찰은 무시한다)이다.
이 운동은 **훅의 법칙(Hooke's law)**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

을 따른다. 이 식의 해는

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

이고, 여기서

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

는 진동의 각진동수이다. 위치 $x$에 따른 퍼텐셜에너지는

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

의 포물선 형태이다.

현실에서는 완벽한 조화진동자는 존재하지 않는다. 지금 예시로 든 용수철의 경우만 해도, 용수철을 지나치게 잡아당기면 탄성 한계를 초과하여 끊어지거나 영구적인 변형이 발생하며, 사실 그 지점까지 가기도 전에 이미 훅의 법칙을 정확하게 따르지는 않게 된다. 그럼에도 불구하고 물리학에서 조화진동자가 중요한 이유는 어떠한 임의의 퍼텐셜도 극솟값(local minimum) 근처에서는 포물선 형태로 근사할 수 있기 때문이다. 임의의 퍼텐셜 $V(x)$를 극소점 근처에서 테일러 전개하면

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

을 얻는다. 이제 $V(x)$에 임의의 상수를 더해도 힘에는 전혀 영향을 미치지 않으므로 여기서 $V(x_0)$를 빼고, $x_0$가 극소점이므로 $V^\prime(x_0)=0$임을 이용하고, $(x-x_0)$가 충분히 작다는 가정 하에 고차항을 무시하면

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

을 얻는다\*. 이는 점 $x_0$ 근처에서 유효 용수철상수 $k=V^{\prime\prime}(x_0)$인 조화진동자의 운동과 일치한다. 즉, 진폭이 충분히 작다면 어떠한 진동도 단순조화진동(simple harmonic oscillation)으로 근사할 수 있다.

> \* $V(x)$가 $x_0$에서 극솟값을 가진다고 가정했으므로, 여기서 $V^{\prime\prime}(x_0) \geq 0$이다. 아주 드물게 $V^{\prime\prime}(x_0)=0$인 경우가 있으며, 이러한 운동은 단순조화진동으로 근사할 수 없다.
{: .prompt-info }

### 양자역학에서의 조화진동자
양자역학적 조화진동자 문제는 퍼텐셜

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

에 대한 슈뢰딩거 방정식을 푸는 것이다. 조화진동자에 대한 [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/)은

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

이다.

이 문제를 푸는 데에는 완전히 다른 두 가지 접근 방식이 있다. 하나는 **거듭제곱급수(power series method)**를 이용한 해석적인 방법(analytic method)이고, 다른 하나는 **사다리연산자(ladder operators)**를 이용한 대수적인 방법(algebraic method)이다. 대수적인 방법이 더 빠르고 간단하지만, 거듭제곱급수를 이용한 해석적인 풀이 또한 공부할 필요가 있다. 여기서는 대수적인 풀이 방법을 다룰 것이며, 해석적인 풀이 방법은 [이 글](/posts/analytic-solution-of-the-harmonic-oscillator/)을 참고하기 바란다.

## 교환자와 정준교환관계
식 ($\ref{eqn:t_independent_schrodinger_eqn}$)를 운동량 연산자 $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$를 활용하여 다음과 같이 쓸 수 있다.

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

이제 해밀토니언(Hamiltonian)

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

을 인수분해하자.

만약 $p$와 $x$가 수(numbers)였다면

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

와 같이 간단하게 인수분해할 수 있지만, 여기서 $\hat{p}$와 $\hat{x}$는 연산자이고 연산자에 대해서는 일반적으로 **교환법칙(commutative property)**이 성립하지 않으므로($\hat{p}\hat{x}\neq \hat{x}\hat{p}$) 그렇게 간단하지는 않다. 하지만 어쨌든 기준점이 되어줄 수는 있으므로, 일단 다음 양을 살펴보는 것에서 출발하자.

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

위에서 정의한 연산자 $\hat{a_\pm}$에 대해, $\hat{a}\_-\hat{a}\_+$는

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

이다. 여기서 $(\hat{x}\hat{p}-\hat{p}\hat{x})$ 항을 $\hat{x}$와 $\hat{p}$의 **교환자(commutator)**라고 하며, 두 연산자가 얼마나 잘 교환(commute)되지 않는지를 나타낸다. 일반적으로 연산자 $\hat{A}$와 $\hat{B}$의 교환자를 사각 괄호를 써 다음과 같이 나타낸다.

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

이러한 표기법을 이용하면 식 ($\ref{eqn:a_m_times_a_p_without_commutator}$)를 다음과 같이 다시 쓸 수 있다.

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

이제 $\hat{x}$와 $\hat{p}$의 교환자를 알아낼 필요가 있다.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

이고, 시험함수 $f(x)$를 떼어내면 다음을 얻는다.

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

이를 **정준교환관계(canonical commutation relation)**라고 한다.

## 사다리연산자 (ladder operators)
정준교환관계에 의해 식 ($\ref{eqn:a_m_times_a_p}$)는

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

즉

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

이다. 여기서 $\hat{a}\_-$와 $\hat{a}\_+$의 순서가 중요한데, $\hat{a}\_+$를 왼쪽에 놓으면

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

이 되며

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

을 만족한다. 이 경우 해밀토니언은

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

로도 쓸 수 있다. 따라서 시간에 무관한 슈뢰딩거 방정식($\hat{H}\psi=E\psi$)을 $\hat{a}_\pm$로 표현하면

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

이다(복부호동순).

이제 다음의 중요한 성질을 알아낼 수 있다.

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> 증명:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> 마찬가지로,
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

따라서, 시간에 무관한 슈뢰딩거 방정식의 한 해를 찾을 수 있다면 다른 해를 모두 찾을 수 있다. 임의의 정상상태에 대해 에너지 준위를 올리거나 내릴 수 있으므로 $\hat{a}\_\pm$를 **사다리연산자(ladder operators)**라고 부르며, $\hat{a}\_+$는 **올림연산자(raising operator)**이고 $\hat{a}\_-$는 **내림연산자(lowering operator)**이다.

## 조화진동자의 정상상태
### 정상상태 $\psi_n$과 에너지 준위 $E_n$
내림연산자를 계속 적용하면 언젠가는 $0$보다 작은 에너지 상태를 얻게 되며, 이러한 상태는 물리적으로 존재할 수 없다. 수학적으로는 $\psi$가 슈뢰딩거 방정식의 해라면 $\hat{a}_-\psi$ 역시 슈뢰딩거 방정식의 해이지만, 이 새로운 해가 항상 규격화된다는(즉 물리적으로 가능한 상태라는) 보장은 없다. 내림연산자를 계속 적용하다 보면 결국에는 자명해 $\psi=0$을 얻는다.

따라서 조화진동자의 정상상태 $\psi$에 대하여,

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

을 만족하는(더 낮은 에너지 준위가 존재하지 않는) '가장 낮은 단계' $\psi_0$가 존재한다. 이 $\psi_0$은

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

을 만족하므로,

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

이다. 이는 [분리 가능한 상미분방정식](/posts/Separation-of-Variables/)이므로 다음과 같이 쉽게 풀 수 있다.

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

또한 이 함수는 다음과 같이 규격화할 수 있다.

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

여기서 $A^2 = \sqrt{m\omega / \pi\hbar}$이므로

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

이다. 이제 이 해를 앞서 구한 슈뢰딩거 방정식 ($\ref{eqn:schrodinger_eqn_with_ladder}$)에 대입하고, $\hat{a}_-\psi_0$임을 이용하면 다음을 얻는다.

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

이 **바닥상태(ground state)**에서 시작하여 올림연산자를 계속 적용하면, 올림연산자가 한 번 작용할 때마다 에너지가 $\hbar\omega$씩 증가하는 들뜬 상태들(excited states)을 얻을 수 있다.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

여기서 $A_n$은 규격화 상수이다. 이처럼 바닥상태를 알아낸 뒤에 올림연산자를 적용하여 조화진동자의 모든 정상상태와 허용된 에너지 준위를 결정할 수 있다.

### 규격화
규격화 상수 또한 대수적으로 구할 수 있다. 우리는 $\hat{a}\_{\pm}\psi_n$이 $\psi\_{n\pm 1}$에 비례함을 알고 있으므로,

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

로 쓸 수 있다. 

이제 임의의 정적분 가능한 함수 $f(x)$와 $g(x)$에 대해 다음이 성립함에 주목하자.

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$는 $\hat{a}\_\pm$의 **에르미트 켤레(hermitian conjugate)**이자 **수반연산자(adjoint operator)**이다.

> **증명:**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

따라서, $f=\hat{a}_\pm \psi_n$, $g=\psi_n$으로 놓으면

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

가 성립한다. 그렇다면 식 ($\ref{eqn:schrodinger_eqn_with_ladder}$)과 ($\ref{eqn:psi_n_and_E_n}$)에서

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

이므로, 식 ($\ref{eqn:norm_const}$)와 ($\ref{eqn:norm_const_2}$)로부터 다음을 얻는다.

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

그리고 여기서 $\psi_n$과 $\psi_{n\pm1}$은 모두 규격화되어 있으므로 $\|c_n\|^2=n+1,\ \|d_n\|^2=n$이고, 따라서

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

이다. 이로부터 규격화된 임의의 정상상태 $\psi_n$을 다음과 같이 구할 수 있다.

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

즉, 식 ($\ref{eqn:psi_n_and_E_n}$)에서 규격화 상수 $A_n=\cfrac{1}{\sqrt{n!}}$이다.

### 정상상태의 직교성
[1차원 무한 사각 우물](/posts/the-infinite-square-well/#3-이-상태는-직교성orthogonality을-갖는다)에서와 마찬가지로, 조화진동자의 정상상태는 직교한다.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### 증명
앞서 보인 식 ($\ref{eqn:hermitian_conjugate}$)과 ($\ref{eqn:norm_const_2}$), ($\ref{eqn:norm_const_3}$)를 사용하여 증명할 수 있다. 식 ($\ref{eqn:hermitian_conjugate}$)에서 $f=\hat{a}_-\psi_m,\ g=\psi_n$으로 놓으면

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

임을 이용한다.

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

직교성을 이용하면, [1차원 무한 사각 우물의 식 (19)에서 했던 것처럼](/posts/the-infinite-square-well/#시간에-의존하는-슈뢰딩거-방정식의-일반해-psixt-구하기) $\Psi(x,0)$을 정상상태의 선형결합 $\sum c_n\psi_n(x)$으로 전개할 때 그 계수 $c_n$을 [Fourier 방법](/posts/the-infinite-square-well/#푸리에-방법fouriers-trick을-이용한-계수-c_n-구하기)으로 구할 수 있다.

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

여기서도 마찬가지로 $\|c_n\|^2$은 에너지를 측정하여 $E_n$값을 얻을 확률이다.

## 임의의 정상상태 $\psi_n$에서 퍼텐셜에너지의 기댓값 $\langle V \rangle$
$\langle V \rangle$를 구하기 위해서는 다음의 적분을 계산해야 한다.

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

$\hat{x}$와 $\hat{p}$의 거듭제곱을 포함하는 이러한 형태의 적분을 계산할 때는 아래의 방법이 유용하게 쓰인다.

먼저 식 ($\ref{eqn:ladder_operators}$)의 사다리연산자의 정의를 이용하여 $\hat{x}$와 $\hat{p}$를 올림연산자와 내림연산자로 나타낸다.

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

이제 기댓값을 구하고자 하는 물리량을 위의 $\hat{x}$와 $\hat{p}$의 식을 이용하여 나타낸다. 여기서는 $x^2$에 관심이 있으므로,

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

와 같이 나타낼 수 있다. 이로부터 다음을 얻는다.

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

그리고 여기서 $\left(\hat{a}\_\pm \right)^2$은 $\psi\_{n\pm2}$에 비례하므로 $\psi\_n$과는 직교하며, 따라서 $\left(\hat{a}\_+ \right)^2$과 $\left(\hat{a}\_- \right)^2$ 이 두 항은 $0$이 된다. 이제 마지막으로 식 ($\ref{eqn:norm_const_2}$)을 이용하여 남은 두 항을 계산하면

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

을 얻는다. 식 ($\ref{eqn:psi_n_and_E_n}$)을 참고하면 퍼텐셜에너지의 기댓값은 전체 에너지의 정확히 절반임을 알 수 있고, 나머지 절반은 당연히 운동에너지 $T$이다. 이것은 조화진동자의 고유한 특성이다.
