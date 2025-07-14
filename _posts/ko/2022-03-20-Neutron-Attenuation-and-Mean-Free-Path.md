---
title: 중성자 감쇠(Neutron Attenuation)와 평균 자유 거리(Mean Free Path)
description: 단일 에너지 중성자 빔을 목표물에 조사했을 때 목표물 투과 거리에 따른 중성자 빔의 강도를 계산하고, 이로부터 중성자의 평균 자유 거리를 유도한다. 또한 두 가지 이상의 핵종이 섞여 있는 균일혼합물과 분자의 거시적 단면적을 계산할 수 있다.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
redirect_from:
  - /posts/Homogeneous-Mixtures-and-Molecular-Cross-sections/
---

## 중성자 감쇠(Neutron Attenuation)
강도 $I_0$의 단일 에너지 중성자 빔을 두께 $X$인 목표물에 조사하고 있으며, 목표물 뒤 얼마 떨어진 거리에 중성자 감지기가 놓여 있다. 목표물과 감지기는 둘 다 매우 작고, 감지기는 목표물을 통과하여 나오는 중성자의 일부만 감지할 수 있는 작은 입체각을 가진다고 가정하자. 그러면 목표물에 충돌하는 모든 중성자는 흡수되거나 산란되어 다른 방향으로 이탈할 것이므로, 목표물과 반응하지 않은 중성자들만 감지기로 입사한다.

목표물 내에서 거리 $x$만큼 진행할 동안 충돌하지 않고 남아 있는 중성자 빔의 세기를 $I(x)$라 하자. 중성자 빔이 충분히 얇은 두께 $\tau$의 목표물을 통과할 때 단위면적당 충돌 수는 $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$([중성자 상호작용과 반응단면적](/posts/Neutron-Interactions-and-Cross-sections/)의 식 [(1)](/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)과 [(8)](/posts/Neutron-Interactions-and-Cross-sections/#충돌밀도collision-density-ie-반응률reaction-rate) 참고)이므로, 목표물 내에서 $dx$만큼 진행하는 동안 중성자 빔 세기의 감소량은 다음과 같다.

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

위 식을 적분하면 다음과 같은 결과를 얻는다.

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

따라서 중성자 빔의 강도는 목표물 통과 거리가 길어질수록 지수적으로 감소함을 알 수 있다.

## 평균 자유 거리 (Mean Free Path)
- 중성자가 핵과 한 번 충돌한 후 뒤이어 또 다른 핵과 충돌할 때까지의 평균 이동거리
- 즉, 중성자가 충돌 없이 진행하는 평균 거리
- 기호 $\lambda$로 표기

$I(x)/I_0=e^{-\Sigma_t x}$는  중성자가 매질 내에서 거리 $x$만큼 진행하는 동안 핵과 충돌하지 않을 확률을 의미한다. 따라서 어떤 중성자가 매질 내에서 거리 $x$까지 충돌 없이 진행한 다음, 거리 $dx$ 이내에 충돌할 확률 $p(x)dx$는 다음과 같다.

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

이로부터 *평균 자유 거리(mean free path)* $\lambda$를 다음과 같이 구할 수 있다.

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## 균일혼합물(Homogeneous Mixture)의 거시적 단면적
두 가지 핵종 $X$와 $Y$가 균일하게 섞여 있는 혼합물을 생각해 보자. 각 핵종의 원자 밀도는 각각 $N_X$와 $N_Y$ $\text{atom/cm}^3$이며, 중성자와 이 핵과의 특정 반응에 대한 반응단면적은 각각 $\sigma_X$, $\sigma_Y$라 하자. 

그러면 중성자가 원자핵 $X$, $Y$와 단위길이당 충돌할 확률은 각각 $\Sigma_X=N_X\sigma_X$, $\Sigma_Y=N_Y\sigma_Y$이므로([거시적 단면적](/posts/Neutron-Interactions-and-Cross-sections/#거시적-단면적macroscopic-cross-section) 참고), 중성자가 이 두 가지 원자핵과 단위길이당 반응할 총 확률은 다음과 같다.

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## 분자의 등가 단면적(Equivalent Cross-section)
위에서 살펴본 핵들이 분자 형태로 존재한다면, 식 ($\ref{eqn:cross_section_of_mixture}$)로 구한 혼합물의 거시적 단면적을 단위부피당 분자 수로 나눔으로써 그 분자의 등가 단면적(equivalent cross-section)을 정의할 수 있다.

단위부피당 분자 $X_mY_n$이 $N$개 있다면 $N_X=mN$, $N_Y=nN$이고, 식 ($\ref{eqn:cross_section_of_mixture}$)로부터 이 분자의 단면적을 다음과 같이 구할 수 있다.

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> 식 ($\ref{eqn:cross_section_of_mixture}$)와 ($\ref{eqn:equivalent_cross_section}$)는 핵 $X$와 $Y$가 서로 독립적으로 중성자와 반응한다는 가정 하에 성립하며, [탄성산란](/posts/Neutron-Interactions-and-Cross-sections/#탄성산란elastic-scattering)을 제외한 모든 종류의 중성자 반응에 대해 유효하다.
> 분자와 고체에 의한 중성자의 탄성산란(특히 낮은 에너지 영역)에는 위의 가정을 적용할 수 없으므로, 실험을 통해 산란 단면적을 알아내야 한다.
{: .prompt-warning }
