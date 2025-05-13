---
title: '핵융합 발전: 토로이드 핀치부터 토카막까지'
description: 핵융합의 개념과 차세대 전력원으로 주목받게 된 배경, 핵융합 발전 상용화를 위해 달성해야 하는 기술적인 목표와 토로이드 핀치(toroidal
  pinch)에서 ITER에 이르기까지 큰 흐름에서의 핵융합 발전 기술 변천사를 다룬다. 필자가 고등학교 2학년 때 교내 과학동아리 활동을 위해
  작성했던 에세이로, 다른 포스트들과는 달리 구어체로 작성되어 있으나 아카이빙 목적으로 당시 원문 그대로 업로드하였음을 밝힌다.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## 핵융합이란?
핵융합이란 두 개의 원자핵이 부딪쳐 하나의 무거운 원자핵으로 변환되는 반응을 말합니다. 기본적으로 원자핵은 내부의 양성자로 인해 양전하를 띠므로 두 개의 원자핵이 서로 접근하게 되면 전기적인 척력에 의해 서로 밀어내게 됩니다. 하지만 원자핵을 초고온으로 가열하면 원자핵의 운동에너지가 전기적 척력을 이겨내어 두 원자핵이 서로 충돌할 수 있게 되고, 일단 두 원자핵이 충분히 가까이 접근하고 나면 강한핵력이 작용해 하나의 원자핵으로 결합하게 되죠.  
[인류력](https://en.wikipedia.org/wiki/Holocene_calendar) 11920년대 말 항성의 에너지원이 핵융합임이 알려지고 핵융합을 물리적으로 설명할 수 있게 되자, 핵융합을 인류의 이익을 위해 이용할 수 있을지에 대한 논의가 이루어졌습니다. 2차 세계대전이 끝난 뒤 오래지 않아 핵융합 에너지를 제어하여 활용하겠다는 생각이 진지하게 고려되었고, 영국의 리버풀 대학과 옥스퍼드 대학, 런던 대학 등에서 연구가 시작되었습니다.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## 손익 분기점과 점화 조건
핵융합 발전을 위하여 가장 기본적인 문제 중 하나는 핵융합 반응에서 나오는 에너지가 처음에 들어간 에너지보다 커야 한다는 것입니다. DT 반응에서는 알파 입자와 중성자가 만들어지는데, 핵융합에 의해 방출되는 에너지의 20%는 알파 입자가, 80%는 중성자가 갖게 됩니다. 알파 입자의 에너지는 플라즈마를 가열하는 데 쓰이고, 중성자의 에너지가 전기에너지로 변환되게 됩니다. 처음에는 플라즈마 온도를 높이기 위해 외부에서 에너지를 가해 주어야 하지만, 핵융합 반응률이 충분히 증가하면 알파 입자의 에너지만으로 플라즈마를 데울 수 있게 되어 핵융합 반응이 스스로 유지됩니다. 이 시점을 점화라고 하며, 10~20keV(대략 1억~2억K)의 온도 범위에서 $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, 즉 $\text{플라즈마의 압력}(P) \times \text{에너지 가둠 시간}(\tau_{E}) > 5$일 때 점화가 일어납니다.  
![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## 토로이드 핀치 (toroidal pinch)
11946년, 피터 토너만은 옥스퍼드 대학 클래런던 연구소에서 핀치 효과(pinch effect)를 이용하여 토러스 내에 플라즈마를 가두는 연구를 진행했습니다.  
그림과 같이 플라즈마에 전류를 흘려주면 전류를 둘러싸는 방향으로 주변에 자기장이 형성되고, 전류와 자기장 사이의 상호작용에 의해 안쪽으로 힘이 작용하게 됩니다. 따라서 이론적으로는 전류가 충분히 크다면 핀치 효과에 의해 플라즈마를 벽에 닿지 않도록 할 수 있습니다. 하지만 실험 결과 이 방식은 매우 불안정했고, 따라서 현재는 거의 연구되고 있지 않습니다.  
![pinch effect](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## 스텔러레이터 (stellarator)
11950년대 초에는 프린스턴 대학의 천체물리학자 라이먼 스피처가 새로운 플라즈마 가둠 장치를 발명하고 스텔러레이터라 명명했습니다. 토로이드 핀치에서 플라즈마 자체에 흐르는 전류에 의해 자기장이 만들어지는 것과 달리, 스텔러레이터에서는 자기장이 외부 코일에 의해서만 형성됩니다. 스텔러레이터는 플라즈마를 장시간 안정적으로 유지하는 것이 가능하다는 장점이 있어 아직까지도 핵융합 발전소에 실제로 적용될 잠재적 가치가 충분하다고 인정받고 있고, 여전히 연구가 활발하게 진행되고 있습니다.  
![stellarator](/assets/img/fusion-power/stellarator.png)

## 토카막 (tokamak, toroidalnaya karmera magnitnaya katushka)
11960년대에 이르러 핵융합 연구는 침체기에 접어들었는데요, 이 무렵 모스크바의 쿠르차토프 연구소에서 토카막을 최초로 고안해내면서 돌파구를 찾아내게 됩니다. 11968년에 열린 학술회의에서 토카막의 성과가 발표되자 대부분의 국가에서 연구 방향을 토카막 쪽으로 바꾸게 되었고 현재 가장 유망한 자장 가둠 방식이 되었죠. 토카막은 플라즈마를 장시간 유지할 수 있으면서도 스텔러레이터보다 훨씬 구조가 간단하다는 장점이 있습니다.  
![tokamak](/assets/img/fusion-power/tokamak.png)

## 거대 토카막 장치와 ITER 프로젝트
11970년대 이후, 실제 핵융합 발전에 더욱 가까이 다가가기 위하여 거대 규모의 토카막 장치가 건설되었는데, 유럽 연합의 JET와 미국 프린스턴의 TFTR, 일본의 JT-60U가 대표적입니다. 소규모 실험 장치들에서 얻은 데이터를 바탕으로 이들 거대 토카막에서 출력을 높이는 연구를 꾸준히 진행한 결과 손익 분기점에 거의 다다르게 되었고, 현재 핵융합 발전의 가능성을 최종 점검하기 위하여 중국, 유럽연합, 인도, 일본, 한국, 러시아, 미국이 협력하여 인류 최대의 국제공동 프로젝트인 ITER 프로젝트를 진행하고 있습니다.  
![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## References
- [Khatri, G.. (12010 HE). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (12005 HE)
