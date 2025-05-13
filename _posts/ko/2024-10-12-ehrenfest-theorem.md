---
title: 에렌페스트 정리(Ehrenfest theorem)
description: 양자역학에서 파동함수로부터 위치와 운동량의 기댓값을 구하는 방법을 알아보고, 이를 임의의 역학적 변수 Q(x,p)에 대한 기댓값의
  계산식으로 확장한다. 그리고 이로부터 에렌페스트 정리(Ehrenfest theorem)를 유도한다.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Prerequisites
- 연속확률분포와 확률밀도
- [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/)

## 파동함수로부터의 기댓값 계산
### 위치 $x$의 기댓값
$\Psi$ 상태에 있는 입자에 대한 위치 $x$의 기댓값(expectation value)은

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

이다. 동일한 상태 $\Psi$에 있는 충분히 많은 수의 입자들에 대해 각각 위치를 측정한 후 측정 결과의 평균을 내면 위의 식을 통해 계산한 $\langle x \rangle$를 얻는다.

> 여기서 말하는 기댓값이란 한 입자를 반복해서 측정하여 얻은 평균값이 아니라, 동일한 상태를 갖는 계들의 **앙상블(ensemble)**에 대한 측정 결과의 평균임에 유의한다. 만약 같은 입자를 짧은 시간 간격으로 여러 번 반복 측정하면, 첫 번째 측정에서 [파동함수가 붕괴(collapse)](/posts/schrodinger-equation-and-the-wave-function/#측정과-파동함수의-붕괴)하므로 이후의 측정에서는 계속 같은 값만을 얻을 것이다.
{: .prompt-warning }

### 운동량 $p$의 기댓값
$\Psi$가 시간에 의존하므로 시간이 지남에 따라 $\langle x \rangle$는 변할 것이다. 이때 [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/)의 식 (8)과 위의 식 ($\ref{eqn:x_exp}$)에 의해 다음이 성립한다.

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> 식 ($\ref{eqn:dx/dt_1}$)에서 ($\ref{eqn:dx/dt_2}$)으로의 과정과 ($\ref{eqn:dx/dt_2}$)에서 ($\ref{eqn:dx/dt_3}$)로의 과정에서 두 차례 부분적분을 적용하였으며, $\lim_{x\rightarrow\pm\infty}\Psi=0$이므로 경계값(boundary term)을 버렸다.
{: .prompt-tip }

따라서 **운동량**의 기댓값을 다음과 같이 얻는다.

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### 임의의 물리량 $Q(x,p)$에 대한 기댓값
앞에서 구한 $\langle x \rangle$와 $\langle p \rangle$의 표현식을 다음의 형태로 쓸 수 있다.

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

연산자 $\hat x \equiv x$는 위치를 표현하고, 연산자 $\hat p \equiv -i\hbar(\partial/\partial x)$는 운동량을 표현한다. 운동량 연산자 $\hat p$의 경우 3차원 공간으로 확장하면 $\hat p \equiv -i\hbar\nabla$로 정의할 수 있다.

모든 고전역학적 변수는 위치와 운동량으로 나타낼 수 있으므로, 이를 임의의 물리량에 대한 기댓값으로 확장할 수 있다. 임의의 양 $Q(x,p)$에 대한 기댓값을 계산하려면, 모든 $p$를 $-i\hbar\nabla$로 바꾸고 이렇게 얻은 연산자를 $\Psi^\*$와 $\Psi$ 사이에 넣어 적분하면 된다.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

예를 들어, 운동에너지 $T=\cfrac{p^2}{2m}$이므로

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

이다.

식 ($\ref{eqn:Q_exp}$)을 통해 상태 $\Psi$에 있는 입자에 대한 임의의 물리량의 기댓값을 계산할 수 있다.

## 에렌페스트 정리 (Ehrenfest theorem)
### $d\langle p \rangle/dt$의 계산
식 ($\ref{eqn:p_op}$)의 양변을 시간 $t$에 대해 미분하여 운동량의 기댓값의 시간 미분 $\cfrac{d\langle p \rangle}{dt}$를 구하자.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> 식 ($\ref{eqn:dp/dt_1}$)에 [슈뢰딩거 방정식과 파동함수](/posts/schrodinger-equation-and-the-wave-function/)의 식 (6)과 (7)을 대입하여 식 ($\ref{eqn:dp/dt_2}$)를 얻을 수 있다. 식 ($\ref{eqn:dp/dt_3}$)에서 ($\ref{eqn:dp/dt_4}$)으로의 과정에서는 부분적분을 적용하였고, 앞에서와 마찬가지로 $\lim_{x\rightarrow\pm\infty}\Psi=0$이므로 경계값(boundary term)을 버렸다.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### 에렌페스트 정리와 뉴턴의 운동 제2법칙 간의 관계
앞서 얻은 다음의 두 식을 에렌페스트 정리(Ehrenfest theorem)라고 한다.

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

에렌페스트 정리는 고전역학에서의 퍼텐셜에너지와 보존력 사이의 관계식 $F=\cfrac{dp}{dt}=-\nabla V$와 상당히 유사한 형태를 지닌다.  
두 식을 나란히 놓고 비교해보면 아래와 같다.

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newton's Second Law of Motion]}$$

에렌페스트 정리의 두 번째 식 $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$(식 [$\ref{eqn:ehrenfest_theorem_2nd}$])의 우항을 $\langle x \rangle$ 근처에서 $x$에 대해 테일러 전개하면

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

이다. 여기서 만약 $x-\langle x \rangle$가 충분히 작다면, 첫 번째 항 이외의 모든 고차항을 무시하고

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

로 근사할 수 있다.

즉, **어떤 입자의 파동함수가 공간적으로 어느 한 점에 매우 가깝게 분포하는 뾰족한 형태를 띈다면($\|\Psi\|^2$의 $x$에 대한 산포도가 매우 작다면), 에렌페스트 정리를 고전역학의 뉴턴 운동 제2법칙으로 근사할 수 있다.** 거시적인 규모에서는 파동함수가 공간적으로 퍼진 정도를 무시하고 입자의 위치를 사실상 한 점으로 간주할 수 있으므로 뉴턴의 운동 제2법칙이 성립하나, 미시적인 규모에서는 양자역학적 효과를 무시할 수 없으므로 뉴턴의 운동 제2법칙은 더 이상 성립하지 않아 에렌페스트 정리를 활용하여야 한다.
