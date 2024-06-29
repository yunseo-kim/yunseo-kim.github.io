---
title: "핵안정성 및 방사성 붕괴"
description: >-
	세그레표와 방사성 붕괴 유형, 그리고 이성체 천이에 대해 알아본다.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Radioactive Decay]
math: true
---

## 세그레표(Segre Chart) 또는 핵종 도표 
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *이미지 출처*
> - 저작자: 위키미디어 유저 [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - 라이선스: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- 원자번호 $Z$가 20보다 큰 핵종들의 경우, 안정화를 위해 양성자 수보다 더 많은 중성자들이 필요
- 중성자들은 양성자들 간의 전기적 반발력을 이기고 핵을 묶어 두는 역할을 함

## 방사성 붕괴(Radioactive Decay)를 하는 이유
- 특정한 중성자와 양성자의 조합만이 안정한 핵종을 이룸
- 양성자 수 대비 중성자 수가 너무 많거나 적으면 해당 핵종은 불안정하여 *방사성 붕괴(radioactive decay)* 를 일으킴
- 붕괴 이후 생성된 핵은 대부분 들뜬 상태이므로, 감마선이나 엑스선의 형태로 에너지를 방출

## 베타붕괴($\beta$-decay)
### 양의 베타붕괴($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- 중성자 수가 상대적으로 부족한 경우 일어남
- 양성자($p$)가 중성자($n$)로 바뀌며 양전자($\beta^+$)와 전자 중성미자($\nu_e$)를 방출
- 원자번호는 1 감소, 질량수는 변화 없음

예) $^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### 음의 베타붕괴($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- 중성자 수가 상대적으로 과도한 경우 일어남
- 중성자($n$)가 양성자($p$)로 바뀌며 전자($\beta^-$)와 전자 반중성미자($\overline{\nu}_e$)를 방출
- 원자번호는 1 증가, 질량수는 변화 없음

예) $^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### 방출되는 전자(양전자)의 에너지 스펙트럼
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *이미지 출처*
> - 저작자: 독일 위키피디아 유저 [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - 라이선스: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- 베타붕괴에서 방출되는 전자 또는 양전자는 위와 같은 연속 에너지 스펙트럼을 보인다.
- $\beta^-$ 붕괴: $\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$ 붕괴: $\overline{E}\approx 0.4E_{\text{max}}$

### 붕괴 사슬(Decay Chain)
종종 베타붕괴를 통해 형성된 *딸핵종(daughter nuclide)* 도 불안정하여 연달아 베타붕괴가 일어나곤 한다. 이는 다음과 같은 *붕괴 사슬(decay chain)* 로 이어진다.

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (stable)} $$ 

## 전자포획(Electron Capture) 또는 K-포획(K-capture)
~~Korea-capture가 아니다~~

$$ p + e \to n + \nu_e $$

- 중성자 수가 상대적으로 부족한 경우 일어남
- 최내각(K-껍질)의 전자를 포획하여 원자핵 내의 양성자를 중성자로 전환
- 원자번호는 1 감소, 질량수는 변화 없음
- 전자포획 후에는 전자구름에 빈 공간이 형성되어 추후 바깥쪽의 다른 전자가 이동함으로써 채워지는데, 이때 엑스선이나 오제 전자(Auger electron)를 방출
- 전자포획에 의해 생겨난 딸핵종(daughter nuclide)은 $\beta^+$붕괴에 의해 생성된 핵과 동일하므로, 이 두 과정은 서로 경쟁한다.

## 알파붕괴($\alpha$-decay)
- 알파입자($\alpha$, $^4_2\text{He}$)를 방출
- 원자번호는 2만큼 감소하고, 질량수는 4만큼 감소
- 납보다 무거운 핵들에서 흔히 일어남
- 베타붕괴와 달리, 알파붕괴 시 방출되는 알파입자의 에너지는 양자화되어 있다.

예) $^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## 자발 핵분열(Spontaneous Fission)
- 매우 무겁고 불안정한 핵종은 중성자를 흡수하지 않고도 스스로 핵분열하기도 함
- 넓은 의미로 방사성 붕괴에 포함함

## 양성자 방출(Proton Emission)
- 양성자가 극도로 많은 불안정한 핵종의 경우, 양성자 1개를 단독으로 방출하기도 함
- 원자번호와 질량수가 1만큼 감소
- 매우 드물게 일어남

## 붕괴도와 이성체 천이
### 붕괴도(Decay Scheme)
*붕괴도(decay scheme)*: 방사성 물질의 모든 붕괴 경로를 시각적으로 나타낸 도표

### 이성체 천이(Isomeric Transition)
- 방사성 붕괴에 의해 형성된 핵은 변환 후에도 들뜬 상태인 경우가 있는데, 이 경우 감마선의 형태로 에너지를 방출한다(감마선 방출 시 핵종이 바뀌지는 않으므로 엄밀히는 붕괴가 아니지만, 관습적으로 감마붕괴라는 표현을 사용하기도 한다). 
- 들뜬 상태의 핵은 대부분 아주 짧은 시간 내에 감마선을 방출하며 바닥 상태로 천이하지만, 특정한 경우에는 감마선 방출이 지연되어 준안정상태처럼 보이기도 한다. 이러한 지연상태를 해당 핵의 *이성체 상태(isomeric transition)* 라 한다.
- 이성체 상태에서 감마선을 방출하며 바닥 상태로 천이하는 것을 *이성체 천이(isomeric transition)* 라 하고 IT로 표시한다.
![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *이미지 출처*
> - 저작자: 영국 위키미디어 유저 [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - 라이선스: 법에 저촉되지 않는 한, 어떠한 목적으로든 제한조건 없이 자유롭게 사용 가능