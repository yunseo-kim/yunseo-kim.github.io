---
title: 중성자 감쇠와 평균 자유행정(Mean Free Path)
description: 단일 에너지 중성자 빔을 목표물에 조사했을 때 목표물 투과 거리에 따른 중성자 빔의 강도를 계산하고, 이로부터 중성자의 평균
  자유행정을 유도한다.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## 중성자 감쇠(Neutron Attenuation)
강도 $I_0$의 단일 에너지 중성자 빔을 두께 $X$인 목표물에 조사하고 있으며, 목표물 뒤 얼마 떨어진 거리에 중성자 감지기가 놓여 있다. 목표물과 감지기는 둘 다 매우 작고, 감지기는 목표물을 통과하여 나오는 중성자의 일부만 감지할 수 있는 작은 입체각을 가진다고 가정하자. 그러면 목표물에 충돌하는 모든 중성자는 흡수되거나 산란되어 다른 방향으로 이탈할 것이므로, 목표물과 반응하지 않은 중성자들만 감지기로 입사한다.

목표물 내에서 거리 $x$만큼 진행할 동안 충돌하지 않고 남아 있는 중성자 빔의 세기를 $I(x)$라 하자. 중성자 빔이 충분히 얇은 두께 $\tau$의 목표물을 통과할 때 단위면적당 충돌 수는 $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$([중성자 상호작용과 반응단면적](/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)의 식 (1)과 (4) 참고)이므로, 목표물 내에서 $dx$만큼 진행하는 동안 중성자 빔 세기의 감소량은 다음과 같다.

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

위 식을 적분하면 다음과 같은 결과를 얻는다.

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

따라서 중성자 빔의 강도는 목표물 통과 거리가 길어질수록 지수적으로 감소함을 알 수 있다.

## 평균 자유행정(Mean Free Path)
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

이로부터 *평균 자유행정(mean free path)* $\lambda$를 다음과 같이 구할 수 있다.

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
