---
title: 항성의 핵융합 반응 메커니즘
description: 이 글에서는 항성의 핵에서 일어나는 핵융합 반응 중 양성자-양성자 연쇄 반응(proton-proton chain reaction)과
  탄소-질소-산소 순환 반응(CNO cycle)을 소개한다. 필자가 고등학교 1학년 때 교내 과학동아리 활동을 위해 작성했던 에세이로, 다른 포스트들과는
  달리 구어체로 작성되어 있으나 아카이빙 목적으로 당시 원문 그대로 업로드하였음을 밝힌다.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## 양성자-양성자 연쇄반응 (proton-proton chain reaction)
사람들에게 가장 흔히 알려져 있는 항성의 핵융합 반응입니다. 중수소의 핵인 중양성자(deuteron)는 양성자(p) 하나와 중성자(n) 하나가 결합하여 만들어집니다. 따라서 양성자와 양성자가 결합하여 중수소의 핵이 되려면 둘 중에 한 양성자는 중성자로 바뀌어야 합니다. 그렇다면 어떻게 양성자가 중성자로 바뀔 수 있을까요?

- 중성자($n$)가 양성자($p$)로 바뀌면서 전자($e⁻$)와 반중성미자($\nu_e$)를 내놓는 것이 ‘[베타붕괴](/posts/Nuclear-Stability-and-Radioactive-Decay/#음의-베타붕괴beta--decay)’입니다. 이를 반응식으로 쓰면 $n \rightarrow p + e^{-} + \overline{\nu_e}$입니다. 
- 양성자($p$)가 중성자($n$)로 바뀌는 과정은 베타붕괴의 반대과정에 해당합니다. 그래서 이를 ‘[역베타붕괴](/posts/Nuclear-Stability-and-Radioactive-Decay/#양의-베타붕괴beta-decay)’라 부릅니다. 그러면 역베타붕괴 반응식은 어떻게 생겼을까요? 핵반응식이라고 해서 특별한 건 없습니다. 양성자와 중성자의 위치를 바꾸고 전자를 양전자로, 반중성미자를 중성미자로 바꿔 주면 됩니다. 식으로 표현하면 $p \rightarrow n + e^{+} + \nu_e$입니다.

위의 과정을 거쳐 중수소 원자핵이 만들어진 후에는 $^2_1D + p \rightarrow {^3_2He}$으로 헬륨-3 원자핵이 만들어지고, 마지막으로 헬륨-3 원자핵 2개가 충돌하여 헬륨-4 원자핵과 양성자 2개가 만들어지게 됩니다.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

사실 양성자-양성자 연쇄반응의 반응 경로는 한 가지가 아닙니다. 위의 경우가 가장 대표적이지만, 이것 외에도 몇 가지 경로가 더 있습니다. 하지만 나머지 경로들은 질량이 태양 이하인 별에서 차지하는 비중이 그리 높지 않고, 질량이 태양의 1.5배 이상인 별에서는 양성자-양성자 연쇄반응보다 뒤에서 다룰 CNO사이클이 훨씬 큰 비중을 차지하기 때문에 여기서는 따로 다루지 않겠습니다.

이 양성자-양성자 연쇄반응은 대략 1000만K~1400만K 정도의 온도에서 지배적으로 일어납니다. 태양의 경우 중심부 온도가 약 1500만K 정도로, pp 연쇄반응이 98.3%를 차지합니다.(나머지 1.3%는 CNO 사이클이 차지)

## 탄소-질소-산소 순환 반응 (CNO Cycle)
CNO순환반응은 탄소가 양성자를 받아들이면서 질소로 바뀌고, 또 질소가 양성자를 받아들여 산소로 바뀌는 과정 등을 겪으면서, 최종적으로는 양성자 4개를 받아들여 헬륨 1개를 내놓고 다시 탄소로 돌아가는 반응입니다. 탄소, 질소, 산소가 촉매와 같은 역할을 한다는 것이 특징입니다. 이 CNO 사이클은 이론적으로 태양 질량의 1.5배 이상인 항성에서 우세하게 작용합니다. 항성 질량에 따른 반응 차이는 양성자-양성자 연쇄반응과 CNO 사이클의 온도 의존성 차이에 있습니다. 전자는 400만K 언저리의 비교적 낮은 온도에서 시작되며, 반응속도는 온도의 4제곱에 비례한다고 합니다. 반면 후자는 1500만K 정도에서 시작되지만 온도에 매우 민감하여(반응속도가 온도의 16제곱에 비례), 1700만K 이상의 온도에서는 CNO 사이클이 더 큰 비중을 차지하게 됩니다.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *이미지 출처*
> - 저작자: 위키미디어 유저 [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

CNO 사이클 역시 다양한 경로가 존재합니다. 저온 CNO사이클(항성 내부)과 고온 CNO사이클(신성, 초신성)으로 크게 나뉘고, 각각의 경우 또다시 서너 개의 반응 경로가 존재합니다. 모든 CNO 사이클 반응을 다루고 싶지만 그러려면 이 정도 분량으로는 부족하므로, 가장 기본적인 CN사이클*, 즉 CNO-I에 대해서만 다루겠습니다.

> *O가 빠진 CN사이클이란 명칭이 붙은 이유는, 해당 반응 과정에서 산소의 안정한 동위원소가 존재하지 않기 때문이다.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

위의 그림과 같이 탄소, 질소, 산소가 순환하며 촉매 역할을 하게 됩니다. 하지만 반응 경로와 상관없이 전체 반응식과 발생하는 에너지의 총량은 같습니다.

## More Readings
- 박인규(Inkyu Park, 서울시립대학교 물리학과 교수), [네이버캐스트 물리산책: 태양에선 얼마나 많은 중성미자가 만들어지는가?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- 위키피디아, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- 위키피디아, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
