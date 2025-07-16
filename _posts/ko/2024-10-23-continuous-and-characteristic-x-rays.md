---
title: 연속 X선과 특성 X선(Continuous and Characteristic X Rays)
description: 원자 방사선에 해당하는 X선의 2가지 발생 원리와, 그에 따른 bremsstrahlung 및 특성 X선의 각각의 특징에 대해 알아본다.
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Atomic Radiation, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## TL;DR
> - **bremsstrahlung(제동 복사, breaking radiation)**: 전자와 같은 하전 입자가 원자핵 근처를 지날 때, 전기적 인력에 의해 가속되면서 방출하는 연속 스펙트럼의 X선
> - 최소 파장: $\lambda_\text{min} = \cfrac{hc}{E_\text{max}} = \cfrac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}$
> - **특성 X선(characteristic X-ray)**: 입사한 전자가 안쪽 원자껍질의 전자와 충돌하여 해당 원자를 이온화시켰을 때 바깥쪽 전자껍질에 있던 다른 전자가 안쪽의 빈 자리로 전이하면서 방출하는, 두 에너지 준위 간 차이만큼의 에너지를 갖는 불연속적인 스펙트럼의 X선
{: .prompt-info }

## Prerequisites
- [아원자 입자와 원자의 구성 요소](/posts/constituents-of-an-atom/)

## X선의 발견
뢴트겐(Röntgen)은 전자 빔을 표적에 조사하였을 때 X선이 발생한다는 것을 발견하였다. 발견 당시에는 X선이 전자기파라는 사실을 알지 못했기에 정체를 알 수 없다는 의미에서 **X선(X-ray)**로 명명되었으며, 또한 발견자의 이름을 따서 **뢴트겐선(Röntgen radiation)**이라고도 부른다.

![X-ray Tube](https://upload.wikimedia.org/wikipedia/commons/7/72/WaterCooledXrayTube.svg)

위 이미지는 전형적인 X선관(X-ray tube)의 구조를 간단히 나타낸 것이다. X선관 내부에는 텅스텐 필라멘트로 구성된 음극과 표적이 고정된 양극이 진공 상태로 밀봉되어 있다. 양극 사이에 수십 kV의 고전압을 걸면 음극에서 전자가 방출되어 양극의 표적으로 조사되고, 이로부터 X선이 방출된다. 단 이때 X선으로의 에너지 변환 효율은 보통 1% 이하로 상당히 낮으며, 나머지 99% 이상의 에너지는 열로 변환되므로 냉각을 위한 별도의 장치가 추가로 필요하다.

## bremsstrahlung (제동 복사, braking radiation)
전자와 같은 하전 입자가 원자핵 근처를 지날 때, 해당 입자와 원자핵 사이에 작용하는 전기적 인력에 의해 급격하게 진행 경로가 휘어지고 또 감속되면서 X선의 형태로 에너지를 방출한다. 이 과정에서의 에너지 전환은 양자화되어 있지 않으므로 방출되는 X선은 연속 스펙트럼을 띄며, 이를 **bremsstrahlung** 또는 **제동 복사(braking radiation)**라고 한다.

![Bremsstrahlung](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bremsstrahlung.svg)

다만, bremsstrahlung에 의해 방출되는 X선의 광자가 갖는 에너지는 당연히 입사한 전자의 운동에너지를 넘을 수는 없다. 따라서 방출되는 X선의 최소 파장이 존재하며, 이는 다음의 식으로 간단히 구할 수 있다.

$$ \lambda_\text{min} = \frac{hc}{E}. \tag{1}$$

플랑크 상수 $h$와 광속 $c$는 상수이므로 이 최소 파장은 오직 입사하는 전자의 에너지에 의해서만 결정된다. $1\text{eV}$의 에너지에 대응하는 파장 $\lambda$는 약 $1.24 \mu\text{m}=12400\text{Å}$이다. 따라서 X선관에 $V$볼트의 전압을 걸었을 때의 최소 파장 $\lambda_\text{min}$은 다음과 같다. 실질적으로는 이 공식을 많이 사용한다.

$$ \lambda_\text{min} \text{[Å]} = \frac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}. \label{eqn:lambda_min}\tag{2}$$

다음 그래프는 X선관에 흐르는 전류량을 일정하게 유지하면서 전압을 달리할 때의 연속 X선 스펙트럼을 나타낸 것이다. 전압이 높아질수록 최소 파장 $\lambda_{\text{min}}$이 짧아지며, 전체적인 X선의 세기는 증가하는 것을 확인할 수 있다.

![Typical continuous X-ray spectra from tube operating
at three different peak voltages with the same current](/assets/img/continuous-and-characteristic-x-rays/bremsstrahlung.png)

## 특성 X선 (characteristic X-ray)
만약 X선관에 걸은 전압이 충분히 크다면, 입사한 전자가 표적 원자의 안쪽 전자껍질에 있는 전자와 충돌하여 해당 원자를 이온화시킬 수 있다. 이 경우 바깥쪽 전자껍질의 전자가 빠르게 에너지를 방출하며 그 안쪽 전자껍질의 빈 자리를 채우는데, 그 과정에서 두 에너지 준위의 차이와 같은 에너지를 갖는 X선 광자가 발생한다. 이 과정으로 방출되는 X선의 스펙트럼은 불연속적이며, 표적 원자의 고유한 에너지 준위에 의해 결정되고 입사하는 전자 빔의 에너지나 세기와는 무관하다. 이를 **특성 X선(characteristic X-ray)**이라고 한다.

### Siegbahn notation

![Siegbahn notation of electron transitions between shells](https://upload.wikimedia.org/wikipedia/commons/f/f6/CharacteristicRadiation.svg)
> *이미지 출처*
> - 저작자: 영문 위키피디아 유저 [HenrikMidtiby](https://en.wikipedia.org/wiki/User:HenrikMidtiby)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Siegbahn 표기법에 따르면, K껍질의 빈 자리를 L껍질, M껍질, ...의 전자가 채울 때 방출하는 X선을 위 이미지와 같이 $K_\alpha$, $K_\beta$, ...와 같이 지칭한다. 다만 Siegbahn 표기법 이후에 현대 원자 모형이 등장하면서 다전자 원자의 경우 보어 원자 모형의 각 껍질(같은 주양자수를 갖는 에너지 준위) 안에서도 다른 양자수들에 따라 에너지 준위가 달라진다는 것을 알게 됨에 따라, 각 $K_\alpha$, $K_\beta$, ...에 대해서도 또다시 $K_{\alpha_1}$, $K_{\alpha_2}$, ...와 같은 세부 분류를 두게 되었다. 

![Siegbahn notation](/assets/img/continuous-and-characteristic-x-rays/siegbahn-notation.png)

이러한 전통적인 표기법은 지금도 분광학 분야에서 여전히 널리 쓰인다. 그러나 명칭이 체계적이지 않고 종종 혼동을 야기한다는 문제점이 있기에, *국제 순수 및 응용 화학 연맹(IUPAC)*에서는 아래와 같은 다른 표기법을 사용할 것을 권장하고 있다.

### IUPAC notation
IUPAC에서 권장하는 원자 오비탈 및 특성 X선의 표준 표기법은 다음과 같다.
우선, 각각의 원자 오비탈에 아래의 표와 같이 이름을 할당한다.

| $n$(주 양자수) | $l$(방위 양자수) | $s$(스핀 양자수) | $j$(각운동량 양자수) | 원자 오비탈 | X선 표기 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $0$ | $\pm1/2$ | $1/2$ | $1s_{1/2}$ | $K_{(1)}$ |
| $2$ | $0$ | $\pm1/2$ | $1/2$ | $2s_{1/2}$ | $L_1$ |
| $2$ | $1$ | $-1/2$ | $1/2$ | $2p_{1/2}$ | $L_2$ |
| $2$ | $1$ | $+1/2$ | $3/2$ | $2p_{3/2}$ | $L_3$ |
| $3$ | $0$ | $\pm1/2$ | $1/2$ | $3s_{1/2}$ | $M_1$ |
| $3$ | $1$ | $-1/2$ | $1/2$ | $3p_{1/2}$ | $M_2$ |
| $3$ | $1$ | $+1/2$ | $3/2$ | $3p_{3/2}$ | $M_3$ |
| $3$ | $2$ | $-1/2$ | $3/2$ | $3d_{3/2}$ | $M_4$ |
| $3$ | $2$ | $+1/2$ | $5/2$ | $3d_{5/2}$ | $M_5$ |
| $4$ | $0$ | $\pm1/2$ | $1/2$ | $4s_{1/2}$ | $N_1$ |
| $4$ | $1$ | $-1/2$ | $1/2$ | $4p_{1/2}$ | $N_2$ |
| $4$ | $1$ | $+1/2$ | $3/2$ | $4p_{3/2}$ | $N_3$ |
| $4$ | $2$ | $-1/2$ | $3/2$ | $4d_{3/2}$ | $N_4$ |
| $4$ | $2$ | $+1/2$ | $5/2$ | $4d_{5/2}$ | $N_5$ |
| $4$ | $3$ | $-1/2$ | $5/2$ | $4f_{5/2}$ | $N_6$ |
| $4$ | $3$ | $+1/2$ | $7/2$ | $4f_{7/2}$ | $N_7$ |

> 총 각운동량 양자수 $j=\|l+s\|$.
{: .prompt-info }

그리고 원자를 구성하는 전자가 어느 한 에너지 준위에서 그보다 낮은 에너지 준위로 전이하면서 방출하는 특성 X선을 다음 규칙을 따라 지칭한다.

$$ \text{(나중 에너지 준위의 X선 표기)-(기존 에너지 준위의 X선 표기)} $$

예를 들어, $2p_{1/2}$ 오비탈의 전자가 $1s_{1/2}$로 전이하면서 방출하는 특성 X선은 $\text{K-L}_2$로 부를 수 있다.

## X선 스펙트럼

![Spectrum of the X-rays emitted by an X-ray tube with a rhodium target, operated at 60 kV](https://upload.wikimedia.org/wikipedia/commons/2/23/TubeSpectrum-en.svg)

위는 로듐(Rh) 표적에 60kV로 가속된 전자 빔을 조사했을 때 방출되는 X선 스펙트럼이다. bremsstrahlung에 의한 매끄럽고 연속적인 형태의 곡선이 나타나며 식 ($\ref{eqn:lambda_min}$)에 따라 약 $0.207\text{Å} = 20.7\text{pm} $ 이상의 파장에 대해서만 X선이 방출됨을 확인할 수 있다. 또한 그래프 중간중간에 나타난 뾰족한 부분은 로듐 원자의 고유한 K껍질 X선에 의한 것이다. 앞서 언급했듯 표적 원자의 종류에 따라 고유한 특성 X선 스펙트럼을 갖기 때문에, 어떤 표적에 전자 빔을 조사하여 나오는 X선 스펙트럼에서 스파이크가 관찰되는 파장을 조사하면 해당 표적의 구성 원소를 알아낼 수 있다.

> $K_\alpha, K_\beta, \dots$ 뿐만 아니라 $L_\alpha, L_\beta, \dots$와 같은 더 낮은 에너지의 X선도 물론 방출된다. 그러나 이들은 훨씬 낮은 에너지를 가지며 대개 X선관의 하우징(housing)에서 흡수되어 검출기까지 도달하지 못한다.
{: .prompt-info }
