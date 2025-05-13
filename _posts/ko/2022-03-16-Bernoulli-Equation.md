---
title: 베르누이 방정식(Bernoulli Equation)
description: 베르누이 방정식과, 베르누이 방정식의 특수한 형태인 로지스틱 방정식의 풀이법을 알아본다.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## 베르누이 방정식(Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{는 임의의 실수)}  \tag{1} $$

베르누이 방정식 (1)은 $a=0$ 또는 $a=1$이면 선형이고, 그 밖의 경우에는 비선형이다. 그러나 아래의 과정을 거쳐 선형으로 변환할 수 있다.

$$ u(x)=[y(x)]^{1-a} $$

로 놓고, 미분한 뒤 식 (1)로부터 $y'$을 대입하면

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

를 얻는다. 우변에서 $y^{1-a}=u$이므로 다음의 선형 상미분방정식을 얻는다.

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## 예제: 로지스틱 방정식(Logistic Equation)
로지스틱 방정식(베르누이 방정식의 특수한 형태)을 풀어라.

$$ y'=Ay-By^2 \tag{3} $$

### 풀이
식 (3)을 식 (1)의 형태로 쓰면

$$ y'-Ay=-By^2 $$

이다. $a=2$이므로 $u=y^{1-a}=y^{-1}$이다. 이 u를 미분하고 식 (3)으로부터 $y'$을 대입하면

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

이다. 마지막 항은 $-Ay^{-1}=-Au$이므로, 다음의 선형상미분방정식을 얻는다.

$$ u'+Au=B $$

[비동차 선형 상미분방정식](/posts/Solution-of-First-Order-Linear-ODE/#비동차-선형-상미분방정식)의 해 공식에 의해 다음의 일반해를 구할 수 있다.

$$ u=ce^{-At}+B/A $$

$u=1/y$이므로, 이로부터 식 (3)의 일반해

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$

를 얻는다.
