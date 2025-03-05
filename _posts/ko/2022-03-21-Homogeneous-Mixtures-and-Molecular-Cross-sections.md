---
title: 균일혼합물과 분자의 단면적
description: 두 가지 이상의 핵종이 섞여 있는 균일혼합물의 거시적 단면적을 계산해 보자.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## 균일혼합물(Homogeneous Mixture)의 거시적 단면적
두 가지 핵종 $X$와 $Y$가 균일하게 섞여 있는 혼합물을 생각해 보자. 각 핵종의 원자 밀도는 각각 $N_X$와 $N_Y$ $\text{atom/cm}^3$이며, 중성자와 이 핵과의 특정 반응에 대한 반응단면적은 각각 $\sigma_X$, $\sigma_Y$라 하자. 

그러면 중성자가 원자핵 $X$, $Y$와 단위길이당 충돌할 확률은 각각 $\Sigma_X=N_X\sigma_X$, $\Sigma_Y=N_Y\sigma_Y$이므로([거시적 단면적](/posts/Neutron-Interactions-and-Cross-sections/#거시적-단면적macroscopic-cross-section) 참고), 중성자가 이 두 가지 원자핵과 단위길이당 반응할 총 확률은 다음과 같다.

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## 분자의 등가 단면적(Equivalent Cross-section)
위에서 살펴본 핵들이 분자 형태로 존재한다면, 식 (1)로 구한 혼합물의 거시적 단면적을 단위부피당 분자 수로 나눔으로써 그 분자의 등가 단면적(equivalent cross-section)을 정의할 수 있다.

단위부피당 분자 $X_mY_n$이 $N$개 있다면 $N_X=mN$, $N_Y=nN$이고, 식 (1)로부터 이 분자의 단면적을 다음과 같이 구할 수 있다.

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> 식 (1)과 (2)는 핵 $X$와 $Y$가 서로 독립적으로 중성자와 반응한다는 가정 하에 성립하므로, 분자와 고체에 의한 탄성산란에는 적용할 수 없다.
> 분자와 고체에 의한 낮은 중성자 에너지에서의 산란 단면적은 실험을 통해 알아내야 한다.
{: .prompt-warning }
