---
title: 자유입자(The Free Particle)
description: V(x)=0인 자유 입자의 경우 변수분리한 해를 규격화할 수 없다는 사실과 이것이 의미하는 바를 알아보며, 일반해에 대한 위치-운동량
  불확정성 관계를 정성적으로 보이고 Ψ(x,t)의 위상속도와 무리속도를 구하여 물리적으로 해석한다.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - 자유 입자: $V(x)=0$, 경계조건 없음(임의의 에너지)
> - 변수분리한 해 $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$는 제곱적분했을 때 무한대로 발산하므로 규격화할 수 없으며, 이는 다음을 시사함
>   - 자유입자는 정상상태로 존재할 수 없음
>   - 자유입자는 에너지를 정확한 하나의 값으로 정의할 수 없음(에너지 불확실성 존재)
> - 그럼에도 불구하고, 시간에 의존하는 슈뢰딩거 방정식의 일반해는 변수분리한 해의 선형결합이므로 변수분리한 해는 여전히 수학적으로는 중요한 의미 가짐. 단 이 경우 제한조건이 없으므로 일반해는 불연속변수 $n$에 대한 합($\sum$)이 아닌 연속변수 $k$에 대한 적분($\int$) 형태임.
> - 슈뢰딩거 방정식의 일반해:
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{이때 }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - 위치 불확실성과 운동량 불확실성의 관계:
>   - 위치 불확실성이 작아지면 운동량 불확실성은 커지며, 역으로 운동량 불확실성이 작아지면 위치 불확실성이 커짐
>   - 즉, 양자역학적으로 자유 입자의 위치와 운동량을 동시에 정확하게 아는 것은 불가능함
> - 파동함수 $\Psi(x,t)$의 위상속도와 무리속도:
>   - 위상속도: $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - 무리속도: $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - 무리속도의 물리적 의미 및 고전역학과의 비교:
>   - 물리적으로 무리속도는 곧 해당 입자의 운동 속력을 의미함
>   - $\phi(k)$가 어떤 값 $k_0$ 근처에서 매우 뾰족한 형태라고 가정할 때(운동량 불확실성이 충분히 작을 때), 
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Prerequisites
- 오일러 공식
- 푸리에 변환(Fourier transform) & 플랑쉐렐 정리(Plancherel's theorem)
- [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/)
- [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/)
- [1차원 무한 사각 우물](/posts/the-infinite-square-well/)

## 모델 설정
가장 단순한 경우인 자유입자($V(x)=0$)를 살펴보자. 고전적으로 이는 단지 등속도 운동일 뿐이지만, 양자역학에서 이 문제는 좀 더 흥미롭다.  
자유 입자에 대한 [시간에 무관한 슈뢰딩거 방정식](/posts/time-independent-schrodinger-equation/)은

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

즉

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, 여기서 }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

이다. [여기까지는 퍼텐셜이 $0$인 무한 사각 우물 내부와 같다](/posts/the-infinite-square-well/#모델-및-경계조건-설정). 다만 이번에는 일반해를 다음의 지수함수 형태로 쓰자.

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$와 $C\cos{kx}+D\sin{kx}$는 같은 $x$의 함수를 쓰는 동등한 방법이다. 오일러 공식 $e^{ix}=\cos{x}+i\sin{x}$에 의해
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> 즉, $C=A+B$, $D=i(A-B)$로 놓으면 
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> 역으로 $A$와 $B$를 $C$와 $D$로 나타내면 $A=\cfrac{C-iD}{2}$, $B=\cfrac{C+iD}{2}$이다.
>
> 양자역학에서 $V=0$일 때 지수함수는 움직이는 파동을 나타내며, 자유입자를 다룰 때 가장 편리하다. 반면 사인과 코사인 함수는 정상파를 나타내기 용이하며, 무한 사각 우물의 경우에 자연스럽게 나타난다.
{: .prompt-info }

무한한 사각형 우물과는 달리 이번에는 $k$와 $E$를 제한하는 경계조건이 없다. 즉 자유입자는 임의의 양의 에너지를 가질 수 있다. 

## 변수분리한 해와 위상속도
$\psi(x)$에 시간 의존성 $e^{-iEt/\hbar}$을 붙이면

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

를 얻는다.

이처럼 특별한 형태 $(x\pm vt)$에 의존하는 $x$와 $t$에 대한 임의의 함수는, 모양이 변하지 않고 속력 $v$로 $\mp x$ 방향으로 움직이는 파동을 나타낸다. 따라서 식 ($\ref{eqn:Psi_seperated_solution}$)의 첫 항은 오른쪽으로 움직이는 파동을 나타내고, 두 번째 항은 같은 파장과 진행속력을 갖고 진폭만 다른 파동이 왼쪽으로 움직이는 것을 나타낸다. 이들은 $k$ 앞의 부호만 다르므로

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

로 쓸 수 있고, 이때 $k$의 부호에 따른 파동의 진행 방향은 다음과 같다.

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{오른쪽으로 이동}, \\
k<0 \Rightarrow & \text{왼쪽으로 이동}.
\end{cases} \tag{6}$$

자유입자의 '정상상태'는 명백히 진행하는 파동으로*, 그 파장은 $\lambda = 2\pi/\|k\|$이고 드보로이 공식(de Broglie formula)에 의해

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

의 운동량을 가진다.

> *'정상상태'인데 진행하는 파동이라니 물리적으로는 당연히 모순이다. 이유는 곧 나온다.
{: .prompt-info }

또한 이 파동의 속력은 다음과 같다.

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(여기서 $\omega$는 $t$ 앞의 계수 $\cfrac{\hbar k^2}{2m}$이다.)

그러나, 이 파동함수는 제곱적분했을 때 무한대로 발산하기에 규격화할 수 없다.

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

즉, <u>자유입자의 경우 변수분리한 해는 물리적으로 가능한 상태가 아니다.</u> 자유입자는 [정상상태](/posts/time-independent-schrodinger-equation/#1-정상상태stationary-states이다)로 존재할 수 없으며, [어떤 특정한 에너지 값](/posts/time-independent-schrodinger-equation/#2-어떤-범위를-갖는-확률분포가-아닌-하나의-명확한-전체에너지-값-e를-갖는-상태이다)을 가질 수도 없다. 사실 직관적으로 생각해 봐도 양쪽 끝에 경계조건이 전혀 없는데 정상파가 형성되는 게 더 이상하다.

## 시간에 의존하는 슈뢰딩거 방정식의 일반해 $\Psi(x,t)$ 구하기
그럼에도 불구하고 이 변수분리한 해는 여전히 중요한 의미를 갖는데, 물리적인 해석과 별개로 [시간에 의존하는 슈뢰딩거 방정식의 일반해는 변수분리한 해의 선형결합](/posts/time-independent-schrodinger-equation/#3-시간에-의존하는-슈뢰딩거-방정식의-일반해는-변수분리한-해의-선형결합이다)이라는 수학적인 의미를 가지기 때문이다. 다만 이 경우 제한조건이 없기 때문에 일반해는 불연속변수 $n$에 대한 합($\sum$) 대신 연속변수 $k$에 대한 적분($\int$)의 형태를 가진다.

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> 여기서는 $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$가 ['시간에 무관한 슈뢰딩거 방정식' 포스트의 식 (21)](/posts/time-independent-schrodinger-equation/#3-시간에-의존하는-슈뢰딩거-방정식의-일반해는-변수분리한-해의-선형결합이다)에서의 $c_n$과 같은 역할을 한다.
{: .prompt-info }

이 파동함수는 적절한 $\phi(k)$에 대해 규격화할 수 있지만, 반드시 $k$의 영역이 있어야 하고 따라서 에너지와 속력의 범위를 가진다. 이것을 **파동묶음(wave packet)**이라고 한다.

> 사인함수는 공간적으로 무한히 퍼져 있기에 규격화할 수 없다. 그러나 이러한 파동을 여러 개 중첩시키면 간섭에 의해 국소화되고 규격화할 수 있다.
{: .prompt-info }

## 플랑쉐렐 정리(Plancherel theorem)를 이용한 $\phi(k)$ 구하기

이제 $\Psi(x,t)$의 형태(식 [$\ref{eqn:Psi_general_solution}$])를 알고 있으므로, 처음 파동함수

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

를 만족하는 $\phi(k)$를 결정하기만 하면 된다. 이는 푸리에 분석(Fourier analysis)의 전형적인 문제인데, **플랑쉐렐 정리(Plancherel's theorem)**로 답을 얻을 수 있다.

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$를 $f(x)$의 **푸리에 변환(Fourier transform)**이라고 하고, $f(x)$는 $F(k)$의 **역 푸리에 변환(inverse Fourier transform)**이라고 한다. 둘의 차이는 지수의 부호뿐임을 식 ($\ref{eqn:plancherel_theorem}$)에서 쉽게 확인할 수 있다. 물론 적분이 존재하는 함수만 허용된다는 제한 조건이 존재한다.

> $f(x)$가 존재하기 위한 필요충분조건은 $\int_{-\infty}^{\infty}\|f(x)\|^2dx$가 유한해야 한다는 것이다. 이 경우 $\int_{-\infty}^{\infty}\|F(k)\|^2dk$도 유한하며, 
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> 이다. 사람에 따라서는 식 ($\ref{eqn:plancherel_theorem}$)가 아니라 위 식을 플랑쉐렐 정리(Plancherel's theorem)라고 하기도 한다([위키피디아](https://en.wikipedia.org/wiki/Plancherel_theorem)에서도 이렇게 기술하고 있다.).
{: .prompt-info }

지금 이 경우에는 $\Psi(x,0)$이 규격화되어야 한다는 물리적인 조건에 의해 반드시 적분이 존재한다. 따라서 자유입자에 대한 양자역학적 해는 식 ($\ref{eqn:Psi_general_solution}$)이고, 여기서

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

이다.

> 다만, 실제로는 식 ($\ref{eqn:Psi_general_solution}$)의 적분을 해석적으로 풀 수 있는 경우는 거의 없다. 보통은 컴퓨터로 수치분석을 이용하여 값을 구한다.
{: .prompt-tip }

## 파동묶음의 무리속도 계산 및 물리적 해석

본질적으로 파동묶음은 $\phi$에 의해 진폭이 결정되는 수많은 사인함수들의 중첩이다. 즉, 파동묶음을 이루는 '포락선(envelope)' 안에 '잔물결(ripples)'이 있다.

![A wave packet with the group velocity larger(5x) than phase velocity](https://raw.githubusercontent.com/yunseo-kim/physics-visualizations/refs/heads/main/figs/wave_packet.gif)
> *이미지 라이선스 및 원작 출처 고지*
> - 이미지 생성 소스코드(gnuplot): [yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/wave_packet.plt)
> - 라이선스: [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)
> - 원작자: [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - 원 라이선스 고지: [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

물리적으로 입자의 속도에 해당하는 것은 앞서 식 ($\ref{eqn:phase_velocity}$)로 구한 개별 잔물결의 속도(**위상속도, phase velocity**)가 아니라 바깥쪽 포락선의 속도(**무리속도, group velocity**)이다.

### 위치 불확실성과 운동량 불확실성의 관계
식 ($\ref{eqn:Psi_at_t_0}$)의 피적분항 $\int\phi(k)e^{ikx}dk$와, 식 ($\ref{eqn:phi}$)의 피적분항 $\int\Psi(x,0)e^{-ikx}dx$ 부분만을 따로 떼어 위치 불확실성과 운동량 불확실성 사이의 관계를 살펴보자.

#### 위치 불확실성이 작을 때
위치 공간에서 $\Psi$가 어떤 값 $x_0$ 주변의 매우 좁은 영역 $[x_0-\delta, x_0+\delta]$에 분포하고 그 밖의 영역에서는 0에 가까운 형태일 때(<u>위치 불확실성이 작을 때</u>), $e^{-ikx} \approx e^{-ikx_0}$로 $x$에 대해 거의 상수이므로

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{eqn. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

이다. 정적분 항은 $p$에 대해 상수이므로 앞의 $e^{-ipx_0/\hbar}$ 항에 의해 $\phi$는 운동량 공간에서 $p$에 대한 사인파 형태를 갖게 되며, 즉 넓은 운동량 구간에 분포한다(<u>운동량 불확실성이 크다</u>).

#### 운동량 불확실성이 작을 때
마찬가지로 운동량 공간에서 $\phi$가 어떤 값 $p_0$ 주변의 매우 좁은 영역 $[p_0-\delta, p_0+\delta]$에 분포하고 그 밖의 영역에서는 0에 가까운 형태일 때(<u>운동량 불확실성이 작을 때</u>), 식 ($\ref{eqn:de_broglie_formula}$)에 의해 $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$로 $p$에 대해 거의 상수이고 $dk=\frac{1}{\hbar}dp$이므로

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

이다. 앞의 $e^{ip_0x/\hbar}$ 항에 의해 $\Psi$는 위치 공간에서 $x$에 대한 사인파 형태를 갖게 되며, 즉 넓은 위치 구간에 분포한다(<u>위치 불확실성이 크다</u>).

#### 결론
위치 불확실성이 작아지면 운동량 불확실성은 커지며, 역으로 운동량 불확실성이 작아지면 위치 불확실성이 커진다. 따라서 양자역학적으로 자유 입자의 위치와 운동량을 동시에 정확하게 아는 것은 불가능하다.

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *이미지 출처*
> - 저작자: 영문 위키피디아 유저 [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - 라이선스: public domain

> 사실, 불확정성 원리(uncertainty principle)에 의해 이는 자유 입자뿐만 아니라 모든 경우에 적용된다. 불확정성 원리는 추후 별도의 포스트로 다루도록 하겠다.
{: .prompt-info }

### 파동묶음의 무리속도
식 ($\ref{eqn:Psi_general_solution}$)의 일반해를 식 ($\ref{eqn:phase_velocity}$)에서와 같이 $\omega \equiv \cfrac{\hbar k^2}{2m}$으로 다시 쓰면

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

이다.

> $\omega = \cfrac{\hbar k^2}{2m}$와 같이 $\omega$를 $k$에 대한 함수로 나타낸 식을 **분산관계(dispersion relation)**라고 한다. 후술할 내용은 분산관계에 상관없이 모든 파동묶음에 대해 일반적으로 적용된다.
{: .prompt-info }

이제 $\phi(k)$가 적절한 값 $k_0$ 근처에서 매우 뾰족한 형태라고 가정하자. ($k$에 대해 넓게 퍼져도 괜찮긴 하지만, 이러한 파동묶음의 형태는 매우 빠르게 어그러지며 다른 형태로 바뀐다. 서로 다른 $k$에 대한 성분들은 제각기 다른 속력으로 움직이기 때문에, 잘 정의된 속도를 갖는 전체 '무리'라는 의미를 잃는다. 즉, <u>운동량의 불확실성이 커진다.</u>)  
적분되는 함수는 $k_0$ 근처를 제외하고 무시할 수 있으므로 이 점 근처에서 함수 $\omega(k)$를 테일러 전개할 수 있으며, 일차항까지만 쓰면

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

를 얻는다. 이제 $s=k-k_0$로 치환하여 $k_0$을 중심으로 적분하면

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

앞에 있는 항 $e^{i(k_0x-\omega_0t)}$은 속력 $\omega_0/k_0$로 움직이는 사인파동('잔물결')을 의미하고, 이 사인파동의 진폭을 결정하는 적분항('포락선')은 $e^{is(x-\omega_0^\prime t)}$ 부분에 의해 속력 $\omega_0^\prime$으로 움직인다. 따라서 $k=k_0$에서의 위상속도는

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

로 식 ($\ref{eqn:phase_velocity}$)에서의 값과 같음을 다시 한 번 확인할 수 있으며, 무리속도는

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

로 위상속도의 2배가 된다.

## 고전역학과의 비교

거시적인 규모에서 고전역학이 성립함을 알고 있으므로, 양자역학을 통해 얻은 결과는 양자론적인 불확정성이 충분히 작을 때 고전역학에서의 계산 결과로 근사할 수 있어야 한다. 지금 다루고 있는 자유 입자의 경우에는, 앞서 가정한 것과 같이 $\phi(k)$가 적절한 값 $k_0$ 근처에서 매우 뾰족한 형태일 때(즉, <u>운동량 불확실성이 충분히 작을 때</u>) 양자역학에서 입자의 속력에 해당하는 무리속도 $v_\text{group}$가 동일한 $k$와 그에 따른 에너지 값 $E$에 대하여 고전역학에서 구한 입자의 속력 $v_\text{classical}$와 같아야 한다.

방금 구한 무리속도(식 [$\ref{eqn:group_velocity}$])에 식 ($\ref{eqn:t_independent_schrodinger_eqn}$)의 $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$를 대입하면

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

이고, 고전역학에서 운동에너지 $E$를 갖는 자유 입자의 속력은 마찬가지로

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

이다. 따라서 $v_\text{quantum}=v_\text{classical}$이므로 양자역학을 적용하여 얻은 결과가 물리적으로 타당한 해임을 확인할 수 있다.
