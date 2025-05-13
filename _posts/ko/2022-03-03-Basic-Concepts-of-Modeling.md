---
title: 모델링(Modeling) 기본 개념
description: '수학적 모델링과 상미분방정식, 편미분방정식, 초기값 문제의 개념을 알아본다. '
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
mermaid: true
image: /assets/img/math-and-physics-cropped.webp
---
## 모델링(Modeling)
- **모델(model)**: 풀고자 하는 공학문제를 변수, 함수, 방정식 등을 통하여 수학적 식으로 공식화한 것
- **수학적 모델링(mathematical modeling)** 또는 **모델링(modeling)**: 모델을 세우고, 그것을 수학적으로 풀고, 그 결과를 해석하는 과정

```mermaid
flowchart LR
	title([모델링])
	A[물리시스템] --> B[수학적 모델]
	B[수학적 모델] --> C[수학적 풀이]
	C[수학적 풀이] --> D[물리적 해석]
```

속도나 가속도와 같은 많은 물리적 개념들이 도함수이므로 모델은 미지함수의 도함수를 포함하는 방정식, 곧 **미분방정식(differential equation)** 꼴인 경우가 많음.

## 상미분방정식(ODE)와 편미분방정식(PDE)
### 상미분방정식(ODE)
**상미분방정식(ordinary differential equation; ODE)**: 미지함수의 $n$계 도함수를 포함하는 방정식

예)

$$y' = \cos x$$

$$ y'' + 9y = e^{-2x} $$

$$ y'y''' - \frac{3}{2}y'^{2} = 0 $$


### 편미분방정식(PDE)
**편미분방정식(partial differential equation; PDE)**: 두 개 이상의 변수를 가진 미지함수의 편도함수를 포함하는 방정식

예)

$$ \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0 $$

## 해(Solution)
함수 $h(x)$가 어떤 열린 구간 $(a, b)$에서 정의되고 미분 가능하며 $y$와 $y'$을 각각 $h$와 $h'$으로 대체할 때 주어진 상미분방정식이 항등식이 되는 경우, 함수

$$ y = h(x) $$

를 구간 $(a, b)$에서 주어진 상미분방정식의 **해(solution)**, $h$의 곡선을 **해곡선(solution curve)** 이라 부른다.

예)

$$ y'=\cos x \Leftrightarrow y=\sin x+c $$

$$ y'=0.2y \Leftrightarrow y=ce^{0.2t} $$

이처럼 임의의 상수 $c$를 포함하는 해를 상미분방정식의 **일반해(general solution)** 라고 부른다.

기하학적으로 상미분방정식의 일반해는 무한히 많은 해곡선의 모임이며, 상수 $c$의 각각의 값마다 한 개의 곡선이 대응한다. 특정한 상수 $c$를 선택하면 상미분방정식의 **특수해(particular solution)** 를 얻는다.

## 초기값 문제(Initial Value Problem)
주어진 문제의 특수해를 얻기 위해서는 임의의 상수 $c$의 값을 결정해야 하는데, 많은 경우 $y(x_{0})=y_{0}$ 또는 $y(t_{0})=y_{0}$와 같은 **초기조건(initial condition)** 을 통해 알아낼 수 있다(독립변수가 시간이 아니거나 $t_{0}\neq0$이라 해도 초기조건이라고 부른다). 초기조건을 갖는 상미분방정식을 **초기값 문제(initial value problem)** 라고 한다.

예)

$$ y'=f(x,y),\qquad y(x_{0})=y_{0} $$

## 모델링 예제: 방사성 물질의 지수적 감쇠
방사성 물질의 양이 0.5g으로 주어졌을 때, 이후의 시간에 남은 양을 구하라.
> 실험에 의하면 방사능 물질은 매 순간 남아있는 물질의 양에 비례하는 속도로 분해되고, 따라서 시간에 따라 감쇠한다.
{: .prompt-info }

### 1. 수학적 모델 설정
시간 $t$에서 남아 있는 물질의 양을 $y(t)$로 나타내자. $y'(t)$ 는 $y(t)$에 비례하므로 **1계 상미분방정식** 

$$ \frac {dy}{dt} = -ky$$ 

를 얻는다(상수 $k>0$).

또한 **초기조건** $y(0)=0.5$를 알고 있다. 따라서 수학적 모델을 다음과 같은 **초기값 문제**로 설정할 수 있다.

$$ \frac {dy}{dt} = -ky, \qquad y(0)=0.5 $$

### 2. 수학적 풀이
앞서 세운 상미분방정식의 일반해는 다음과 같다([변수분리법](/posts/Separation-of-Variables/#모델링-예제-방사성-탄소-연대측정법-radiocarbon-dating) 참고).

$$ y(t)=ce^{-kt} $$

$y(0)=c$이므로 초기조건으로부터 $y(0)=c=0.5$를 얻는다. 따라서 구하고자 하는 특수해는 

$$ y(t)=0.5e^{-kt} \quad(k>0)$$

이 된다.

### 3. 해의 물리적 해석
앞서 구한 해는 임의의 시간 $t$에서 방사성 물질의 양을 나타낸다. 방사성 물질의 양은 초기값 0.5(g)에서 시작하여 시간에 따라 감소하며, $t \to \infty$ 일 때 $y$의 극한값은 $0$이다.
