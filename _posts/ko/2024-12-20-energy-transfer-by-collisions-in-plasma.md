---
title: 플라즈마에서의 충돌에 의한 에너지 전달
description: 플라즈마 내 입자 간 충돌에 의한 에너지 전달률을 탄성 충돌과 비탄성 충돌 두 가지로 나누어 구하고, 이로부터 충돌하는 두 입자의 질량이 비슷할 때와 크게 다를 때 각각의 경우에 대하여 에너지 전달률의 크기를 비교한다.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
redirect_from:
  - /posts/energy-transfer-by-collisions/
---
## TL;DR
> - 충돌 시 총 에너지와 운동량은 보존됨
> - 모든 전자를 잃고 원자핵만 남은 이온과 전자는 운동에너지만을 가짐
> - 중성 원자 및 일부 전자만을 잃은 이온은 내부 에너지를 가지며, 퍼텐셜 에너지의 변화에 따라 들뜸(excitation), 탈들뜸(deexcitation), 혹은 이온화(ionization)가 일어날 수 있음
> - 충돌 전후의 운동에너지 변화에 따른 충돌 유형 분류:
>   - 탄성 충돌(elastic collision): 충돌 전후의 운동에너지 총량이 일정함
>   - 비탄성 충돌(inelastic collision): 충돌 과정에서 운동에너지가 손실됨
>     - 들뜸(excitation)
>     - 이온화(ionization)
>   - 초탄성 충돌(superelastic collision): 충돌 과정에서 운동에너지가 증가함
>     - 탈들뜸(deexcitation)
> - 탄성 충돌에 의한 에너지 전달률:
>   - 개별 충돌에 의한 에너지 전달률: $\zeta_L = \cfrac{4m_1m_2}{(m_1+m_2)^2}\cos^2\theta_2$
>   - 충돌당 평균 에너지 전달률: $\overline{\zeta_L} = \cfrac{4m_1m_2}{(m_1+m_2)^2}\overline{\cos^2\theta_2} = \cfrac{2m_1m_2}{(m_1+m_2)^2}$
>     - $m_1 \approx m_2$일 때: $\overline{\zeta_L} \approx \cfrac{1}{2}$로, 효과적인 에너지 전달이 일어나 빠르게 열평형에 도달함
>     - $m_1 \ll m_2$ 또는 $m_1 \gg m_2$일 때: $\overline{\zeta_L} \approx 10^{-5}\sim 10^{-4}$로, 에너지 전달 효율이 매우 낮아 열평형에 도달하기 쉽지 않음. 이는 약하게 이온화된 플라즈마에서 $T_e \gg T_i \approx T_n$으로 전자 온도와 이온 온도 및 중성 원자 온도가 크게 다른 이유임.
>
> - 비탄성 충돌에 의한 에너지 전달률:
>   - 단일 충돌에 의한 최대 내부 에너지 전환률: $\zeta_L = \cfrac{\Delta U_\text{max}}{\cfrac{1}{2}m_1v_1^2} = \cfrac{m_2}{m_1+m_2}\cos^2\theta_2$
>   - 평균 최대 내부 에너지 전환률: $\overline{\zeta_L} = \cfrac{m_2}{m_1+m_2}\overline{\cos^2\theta_2} = \cfrac{m_2}{2(m_1+m_2)}$
>     - $m_1 \approx m_2$일 때: $\overline{\zeta_L} \approx \cfrac{1}{4}$
>     - $m_1 \gg m_2$일 때: $\overline{\zeta_L} \approx 10^{-5}\sim 10^{-4}$
>     - $m_1 \ll m_2$일 때: $\overline{\zeta_L} = \cfrac{1}{2}$로, 가장 효율적으로 충돌 대상(이온 또는 중성원자)의 내부 에너지를 상승시켜 들뜬 상태로 만들 수 있음. 이는 전자에 의한 이온화(플라즈마 생성), 들뜸(발광), 분자의 해리(dissociation)(라디칼 생성) 등이 잘 일어나는 이유임.
{: .prompt-info }

## Prerequisites
- [아원자 입자와 원자의 구성 요소](/posts/constituents-of-an-atom/)

## 플라즈마에서의 입자 간 충돌
- 충돌 시 총 에너지와 운동량은 보존됨
- 모든 전자를 잃고 원자핵만 남은 이온과 전자는 운동에너지만을 가짐
- 중성 원자 및 일부 전자만을 잃은 이온은 내부 에너지를 가지며, 퍼텐셜 에너지의 변화에 따라 들뜸(excitation), 탈들뜸(deexcitation), 혹은 이온화(ionization)가 일어날 수 있음
- 충돌 전후의 운동에너지 변화에 따른 충돌 유형 분류:
  - 탄성 충돌(elastic collision): 충돌 전후의 운동에너지 총량이 일정함
  - 비탄성 충돌(inelastic collision): 충돌 과정에서 운동에너지가 손실됨
    - 들뜸(excitation)
    - 이온화(ionization)
  - 초탄성 충돌(superelastic collision): 충돌 과정에서 운동에너지가 증가함
    - 탈들뜸(deexcitation)

## 탄성 충돌에 의한 에너지 전달

![Elastic collision](/assets/img/energy-transfer-by-collisions/elastic-collision.png)

### 개별 충돌에 의한 에너지 전달률
탄성 충돌에서는 충돌 전후 운동량과 운동에너지가 보존된다.

$x$축과 $y$축에 대해 각각 운동량 보존 식을 세우면

$$ \begin{gather*}
m_1v_1 = m_1v_1^{\prime}\cos\theta_1 + m_2v_2^{\prime}\cos\theta_2, \label{eqn:momentum_conservation_x}\tag{1} \\
m_1v_1^{\prime}\sin\theta_1 = m_2v_2^{\prime}\sin\theta_2 \label{eqn:momentum_conservation_y}\tag{2}
\end{gather*} $$

이며, 또한 에너지 보존에 의해

$$ \frac{1}{2}m_1v_1^2 = \frac{1}{2}m_1{v_1^{\prime}}^2 + \frac{1}{2}m_2{v_2^{\prime}}^2 $$

$$ v_1^2 = {v_1^{\prime}}^2 + \frac{m_2}{m_1}{v_2^{\prime}}^2 \label{eqn:energy_conservation}\tag{3}$$

이다.

식 ($\ref{eqn:momentum_conservation_x}$)에서

$$ m_1 v_1^{\prime} \cos \theta_1  = m_1v_1 - m_2v_2^{\prime} \cos \theta_2 \label{eqn:momentum_conservation_x_2}\tag{4} $$

이고, 식 ($\ref{eqn:momentum_conservation_y}$)와 ($\ref{eqn:momentum_conservation_x_2}$)의 양변을 제곱하여 더하면

$$ \begin{align*}
(m_1v_1^{\prime})^2 &= (m_2 v_2^\prime \sin \theta_2)^2 + (m_1 v_1 - m_2 v_2^\prime \cos \theta_2)^2 \\
&= m_1^2 v_1^2 - 2 m_1 m_2 v_1 v_2^\prime \cos \theta_2 + m_2^2 {v_2^\prime}^2 \tag{5}
\end{align*} $$

이다. 이제 양변을 $m_1^2$으로 나누면

$$ {v_1^{\prime}}^2 = v_1^2 - 2 \frac{m_2}{m_1} v_1 v_2^\prime \cos \theta_2 + \left(\frac{m_2}{m_1}\right)^2 {v_2^\prime}^2 \label{eqn:momentum_conservation}\tag{6}$$

이 된다.
여기에 식 ($\ref{eqn:energy_conservation}$)을 대입하면 다음과 같이 정리할 수 있다.

$$ \begin{gather*}
\left( \frac{m_2}{m_1} \right) {v_2^\prime}^2 = 2 \left( \frac{m_2}{m_1} \right) v_1 v_2^\prime \cos \theta_2 - \left( \frac{m_2}{m_1} \right)^2 {v_2^\prime}^2 \\
2v_1 \cos \theta_2 = \left(\frac{m_1 + m_2}{m_1} \right) v_2^\prime \\
v_2^{\prime} = \frac{2m_1v_1\cos\theta_2}{m_1 + m_2}. \label{eqn:v_2_prime}\tag{7}
\end{gather*} $$

이로부터 에너지 전달률 $\zeta_L$을 다음과 같이 얻는다.

$$ \begin{align*}
\therefore \zeta_L &= \frac{\cfrac{1}{2}m_2{v_2^\prime}^2}{\cfrac{1}{2}m_1v_1^2}  
= \frac{m_2}{m_1v_1^2} {\left(\frac{2m_1v_1\cos\theta_2}{m_1 + m_2} \right)}^2 \\
&= \frac{4m_1m_2}{(m_1+m_2)^2}\cos^2\theta_2. \quad \blacksquare \label{eqn:elastic_E_transfer_rate}\tag{8}
\end{align*} $$

### 충돌당 평균 에너지 전달률
$0$부터 $2\pi$까지의 각에 대해 $\sin^2{\theta_2}+\cos^2{\theta_2}=1$이고 $\overline{\sin^2{\theta_2}}=\overline{\cos^2{\theta_2}}$이므로,

$$ \begin{align*}
\overline{\cos^2{\theta_2}} &= \overline{(1-\sin^2{\theta_2})} = 1 - \overline{\sin^2{\theta_2}} \\
&= 1 - \overline{\cos^2{\theta_2}} 
\end{align*} $$

$$ \begin{gather*}
2 \cdot \overline{\cos^2{\theta_2}} = 1 \\
\overline{\cos^2{\theta_2}} = \frac{1}{2}.
\end{gather*} $$

이를 앞서 구한 식 ($\ref{eqn:elastic_E_transfer_rate}$)에 대입하면

$$ \overline{\zeta_L} = \frac{4m_1m_2}{(m_1+m_2)^2}\overline{\cos^2\theta_2} = \frac{2m_1m_2}{(m_1+m_2)^2}. \quad \blacksquare \label{eqn:elastic_E_mean_transfer_rate}\tag{9} $$

#### $m_1 \approx m_2$일 때
전자-전자, 이온-이온, 중성원자-중성원자, 이온-중성원자 충돌이 이에 해당한다. 이러한 경우

$$ \overline{\zeta_L} = \frac{2m_1m_2}{(m_1+m_2)^2} \approx \frac{1}{2} \label{eqn:elastic_similar_m}\tag{10}$$

로, 효과적인 에너지 전달이 일어나 빠르게 열평형에 도달한다.

#### $m_1 \ll m_2$ 또는 $m_1 \gg m_2$일 때
전자-이온, 전자-중성원자, 이온-전자, 중성원자-전자 충돌이 이에 해당한다. 이러한 경우에는

$$ \overline{\zeta_L} = \frac{2m_1m_2}{(m_1+m_2)^2} \approx \frac{2m_1}{m_2}\text{ (}m_1 \ll m_2 \text{일 때 기준)} \approx 10^{-5}\sim 10^{-4} \label{eqn:elastic_different_m}\tag{11}$$

로, 에너지 전달 효율이 매우 낮아 열평형에 도달하기가 쉽지 않다. 이는 약하게 이온화된 플라즈마에서 $T_e \gg T_i \approx T_n$으로 전자 온도와 이온 온도 및 중성 원자 온도가 크게 다른 이유이다.

## 비탄성 충돌에 의한 에너지 전달
![Inelastic collision](/assets/img/energy-transfer-by-collisions/inelastic-collision.png)

### 단일 충돌에 의한 최대 내부 에너지 전환률
운동량 보존(식 [$\ref{eqn:momentum_conservation}$])은 이 경우에도 동일하게 성립하나, 비탄성 충돌이므로 운동에너지는 보존되지 않는다. 이때 비탄성 충돌에 의해 손실된 운동에너지는 $\Delta U$의 내부에너지로 전환되므로

$$ \Delta U = \frac{1}{2} m_1 v_1^2 - \left( \frac{1}{2} m_1 {v_1^{\prime}}^2 + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right) \label{eqn:delta_U}\tag{12} $$

이다. 이제 여기에 식 ($\ref{eqn:momentum_conservation}$)을 대입하여 정리하면 다음을 얻는다.

$$\begin{align*}
\Delta U &= \frac{1}{2} m_1 v_1^2 - \left[ \frac{1}{2} m_1 \left( v_1^2 - 2 \frac{m_2}{m_1} v_1 v_2^{\prime} \cos \theta_2 + \left( \frac{m_2}{m_1} v_2^{\prime} \right)^2 \right) + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right] \\
&= \frac{1}{2} m_1 v_1^2 - \left[ \frac{1}{2} m_1 v_1^2 - m_2 v_1 v_2^{\prime} \cos \theta_2 + \frac{1}{2} \frac{m_2^2}{m_1} {v_2^{\prime}}^2 + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right] \\
&= m_2 v_1 v_2^{\prime} \cos \theta_2 - \frac{1}{2}m_2{v_2^{\prime}}^2\left(\frac{m_1 + m_2}{m_1}\right) \label{eqn:delta_U_2}\tag{13}
\end{align*}$$.

$\Delta U$를 $v_2^\prime$에 대해 미분하여, 해당 도함수의 값이 $0$이 되는 극점과 그 점에서의 최댓값을 구하면

$$ \cfrac{d \Delta U}{d v_2^{\prime}} = m_2 v_1 \cos \theta_2 - m_2 v_2^{\prime} \left( \frac{m_1 + m_2}{m_1} \right) = 0 \tag{14}$$

$$ \begin{gather*} 
v_2^{\prime} \left( \frac{m_1 + m_2}{m_1} \right) = v_1 \cos \theta_2 \\
v_2^\prime = \frac{m_1v_1\cos\theta_2}{m_1+m_2}.
\end{gather*} $$

$$ \therefore v_2^{\prime} = \frac{m_1v_1\cos\theta_2}{m_1+m_2}
\text{일 때 } \Delta U_\text{max} = \frac{1}{2}\frac{m_1m_2 v_1^2 \cos^2\theta_2}{m_1 + m_2}. \label{eqn:delta_U_max}\tag{15}$$

이로부터, 단일 비탄성 충돌에 의해 가능한 운동에너지에서 내부에너지로의 최대 전환율 $\zeta_L$은 다음과 같다.

$$ \zeta_L = \frac{\Delta U_\text{max}}{\cfrac{1}{2}m_1v_1^2} = \frac{m_2}{m_1+m_2}\cos^2\theta_2. \quad \blacksquare \label{eqn:inelastic_E_transfer_rate}\tag{16}$$

### 평균 최대 내부 에너지 전환률
마찬가지로, 식 ($\ref{eqn:inelastic_E_transfer_rate}$)에 $\overline{\cos^2{\theta_2}} = \cfrac{1}{2}$을 대입하면 다음을 얻는다.

$$ \overline{\zeta_L} = \frac{m_2}{m_1+m_2}\overline{\cos^2\theta_2} = \frac{m_2}{2(m_1+m_2)}. \label{eqn:inelastic_E_mean_transfer_rate}\tag{17}$$

#### $m_1 \approx m_2$일 때
이온-이온, 이온-중성원자, 중성원자-중성원자 충돌이 이에 해당한다.

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} = \frac{1}{4}. \label{eqn:inelastic_similar_m}\tag{18}$$

#### $m_1 \gg m_2$일 때
이온-전자, 중성원자-전자 충돌이 이에 해당한다.

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} \approx \frac{m_2}{2m_1} \approx 10^{-5}\sim 10^{-4}. \label{eqn:inelastic_ion_electron}\tag{19}$$

#### $m_1 \ll m_2$일 때
전자-이온, 전자-중성원자 충돌이 이에 해당한다. 앞선 두 경우는 탄성 충돌에서와 크게 다르지는 않은 양상이었으나, 이 세 번째 경우는 중요한 차이를 보인다. 이 경우

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} \approx \frac{m_2}{2m_2} = \frac{1}{2} \label{eqn:inelastic_electron_ion}\tag{20}$$

로, 가장 효율적으로 충돌 대상(이온 또는 중성원자)의 내부 에너지를 상승시켜 들뜬 상태로 만들 수 있다. 이는 추후 다루겠지만 전자에 의한 이온화(플라즈마 생성), 들뜸(발광), 분자의 해리(dissociation)(라디칼 생성) 등이 잘 일어나는 이유이다.
