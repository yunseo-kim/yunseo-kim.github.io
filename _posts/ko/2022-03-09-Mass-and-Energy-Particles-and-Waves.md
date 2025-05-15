---
title: 질량과 에너지, 입자와 파동
description: 상대성이론의 질량-에너지 등가 원리를 탐구하고, 운동하는 전자의 에너지를 상대론적 효과를 고려하여 계산해 보자.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## 질량-에너지 등가 원리
질량과 에너지는 서로 동일하며 상호 변환할 수 있다.

$$ E=mc^2 $$

여기서 $c$는 빛의 속도 $2.9979 \times 10^{10}\ \text{cm/sec}$이다.

## 전자볼트(Electron Volt, eV)
*전자볼트(electron volt, eV)*: 1개의 전자가 1V의 전압을 통과할 때 얻는 운동에너지

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## 운동하는 물체의 질량과 에너지
상대성이론에 따르면 관찰자 입장에서 운동하는 물체의 질량은 상대적으로 증가하며, 운동하는 물체의 속력과 질량에 관한 식은 다음과 같이 정의된다.

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: 정지질량, $v$: 속력

입자의 *총 에너지(total energy)* 는 *정지질량 에너지(rest-mass energy)* 와 *운동에너지(kinetic energy)* 의 합이므로 다음이 성립한다.

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

특히 $v\ll c$일 경우, $\cfrac{v^2}{c^2} = \epsilon$으로 놓고 $\epsilon = 0$ 근처에서 테일러 전개하여(즉, 매클로린 전개하여) 근사하면

$$
\begin{align*}
E_{\text{kinetic}} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

으로 고전역학에서의 운동에너지 공식과 같아진다. 실질적으로, $v\leq 0.2c$ 또는 $E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$인 경우 $v\ll c$로 간주하고 이 근사식을 사용해도(즉, 상대성이론에 따른 효과를 무시해도) 충분히 정확한 값을 얻는다.

### 전자
전자의 정지질량 에너지 $E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$이므로, 전자의 운동에너지가 $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$ 초과일 경우 상대론적 운동에너지 공식을 적용해야 한다. 원자핵공학에서 다루는 전자들의 에너지는 많은 경우 10keV보다 크므로 대부분 식 (2)를 적용해야 한다.

### 중성자
중성자의 정지질량 에너지는 대략 1000MeV에 달하므로 $0.02E_{rest}=20\text{MeV}$이다. 원자핵공학에서 중성자의 운동에너지가 20MeV 초과인 상황을 다루는 경우는 희박하므로, 보통 중성자의 운동에너지 계산은 식 (3)을 이용한다.

### 광자
식 (2), (3)은 정지질량이 0이 아닐 경우에 유효하므로 정지질량이 0인 광자에는 적용할 수 없다. 광자의 총 에너지는 아래의 식으로 구한다.

$$ E = h\nu \tag{4} $$

$h$: 플랑크상수($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: 전자기파의 진동수

## 물질파
자연계의 모든 물질은 입자이면서 동시에 파동이다. 즉 모든 입자들은 그에 상응하는 파장(*드보로이 파장, de Broglie wavelength*)을 가진다. 이때 파장 $\lambda$는 운동량 $p$와 플랑크 상수 $h$의 함수이다.

$$ \lambda = \frac {h}{p} \tag{5}$$

또한 운동량 $p$는 다음의 식으로 정의된다.

$$ p = mv \tag{6} $$

### 상대론적 효과를 무시할 경우(e.g., 중성자)
운동에너지 $E=1/2 mv^2$이므로 식 (6)을 에너지의 함수로 표현하면 다음과 같다.

$$ p=\sqrt{2mE} \tag{7} $$

이를 식 (5)에 대입하면 입자의 파장은 

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

이 된다. 원자핵공학에서는 중성자의 드보로이 파장을 구할 때 위 식을 적용한다. 중성자의 정지질량을 대입하면 다음과 같이 표현된다.

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

여기서 $\lambda$의 단위는 cm이며 $E$는 eV로 표현된 중성자의 운동에너지이다.

### 상대론적 효과를 고려할 경우(e.g., 전자)
앞의 상대성이론 식들을 직접 풀어 운동량 $p$를 계산한다.

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{rest}}} \tag{10}$$

그러면 드보로이 파장은 다음과 같다.

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{rest}}}} \tag{11} $$

### 정지질량이 0인 입자(e.g., 광자)
정지질량이 0인 입자의 운동량은 식 (6)으로 구할 수 없으므로 

$$ p=\frac {E}{c} \tag{12} $$

으로 표현한다. 식 (12)를 식 (5)에 대입하면 

$$ \lambda = \frac {hc}{E} \tag{13}$$

이 된다. 여기에 $h$와 $c$ 값을 대입하면 최종적으로 파장에 대한 식은 

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

이 된다. 여기서 $\lambda$의 단위는 m, $E$의 단위는 eV이다.
