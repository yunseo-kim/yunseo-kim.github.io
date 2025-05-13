---
title: 1계 선형 상미분방정식의 풀이
description: 1계 선형 상미분방정식의 풀이법을 알아보자.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## 1계 선형 상미분방정식
1계 상미분방정식을 대수적으로

$$ y'+p(x)y=r(x) \tag{1} $$

의 형태로 가져갈 수 있으면 **선형(linear)** 이라고 하고, 그렇지 않으면 **비선형(nonlinear)** 이라고 한다.

식 (1)과 같은 형태를 1계 선형 상미분방정식의 **표준형(standard form)** 이라고 하며, 만약 주어진 1계 선형 상미분방정식의 첫 항이 $f(x)y'$이면 방정식의 양변을 $f(x)$로 나누어 표준형을 얻을 수 있다.

공학에서는 종종 $r(x)$를 **입력(input)**, $y(x)$를 **출력(output)** 또는 입력(과 초기조건)에 대한 **응답(response)** 이라고 부른다.

## 동차 선형 상미분방정식
식 (1)을 풀고자 하는 어떤 구간 $a<x<b$를 $J$ 라고 하자. 식 (1)에서 구간 $J$에 대해 $r(x)\equiv 0$이면

$$ y'+p(x)y=0 \tag{2}$$

이고, 이를 **동차(homogeneous)** 라 한다. 이 경우 [변수분리법](/posts/Separation-of-Variables/)을 사용할 수 있다.

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

$c=0$일 경우 **자명한 해(trivial solution)** $y(x)=0$을 얻는다.

## 비동차 선형 상미분방정식
구간 $J$에서 $r(x)\not\equiv 0$인 경우 **비동차(nonhomogeneous)** 라고 한다. 비동차 선형상미분방정식 (1)은 $x$에만 의존하는 적분인자를 가짐이 알려져 있다. 이 적분인자 $F(x)$는 [적분인자를 구하는 방법](/posts/Exact-Differential-Equation-and-Integrating-Factor/#적분인자를-구하는-방법)의 식 (11)로 구할 수도 있고, 다음과 같이 직접 구할 수도 있다.

식 (1)에 $F(x)$를 곱하면

$$ Fy'+pFy=rF \tag{1*} $$

를 얻는다. 만약

$$ pF=F' $$

이면 식 (1*)의 좌변은 도함수 $(Fy)'=F'y+Fy'$가 된다. $pF=F'$을 변수분리하면 $dF/F=p\ dx$이고, 적분해서 $h=\int p\ dx$라 쓰면

$$ \log |F|=h=\inf p\ dx $$

$$ F = e^h $$

이다. 식 (1*)에 대입하면

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

이 된다. 적분하면

$$ e^hy=\int e^hr\ dx + c $$
가 되고, $e^h$로 나누면 원하는 해 공식을 얻는다.

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

이때 $h$에서 적분상수는 문제가 되지 않는다.

식 (4)에서 주어진 초기조건에 의존하는 유일한 값은 $c$이므로, 식 (4)를 두 개의 항의 합

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

으로 쓰면 다음을 알 수 있다.

$$ \text{전체 출력}=\text{입력 }r\text{에 대한 응답}+\text{초기조건에 대한 응답} \tag{5} $$

## 예제: RL 회로
어떤 $RL$ 회로가 기전력 $E=48\textrm{V}$인 전지, $R=11\mathrm{\Omega}$인 저항, $L=0.1\text{H}$인 인덕터로 구성되어 있고, 초기 전류는 0이라고 하자. 이 $RL$ 회로의 모델을 구하고, 결과로 얻는 상미분방정식을 전류 $I(t)$에 대해 풀어라.
> **옴의 법칙(Ohm's law)**  
> 회로의 전류 $I$는 저항의 양단에서 전압강하(voltage drop) $RI$을 야기한다.
{: .prompt-info }

> **패러데이 전자기 유도 법칙(Faraday's law of electromagnetic induction)**  
> 회로의 전류 $I$는 인덕터의 양단에서 전압강하 $LI'=L\ dI/dt$를 야기한다.
{: .prompt-info }

> **키르히호프의 전압법칙(Kirchhoff's Voltage Law;KVL)**  
> 닫힌 회로에 가해진 기전력은 회로의 모든 다른 원소들 양단의 전압강하의 합과 같다.
{: .prompt-info }

### 풀이
위의 법칙들에 따르면 $RL$ 회로의 모델은 $LI'+RI=E(t)$이고, 표준형으로 쓰면

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

이다. 식 (4)에서 $x=t, y=I, p=R/L, h=(R/L)t$로 놓으면 이 선형상미분방정식을 풀 수 있다.

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

이때 $R/L=11/0.1=110$이고 $E(t)=48$이므로

$$ I=\frac{48}{11}+ce^{-110t} $$

이다.

초기조건 $I(0)=0$으로부터 $I(0)=E/R+c=0$, $c=-E/R$를 얻는다. 이로부터 다음의 특수해를 구할 수 있다.

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
