---
title: 아원자 입자와 원자의 구성 요소
description: 전자, 양성자, 중성자, 광자, 중성미자 등 원자핵공학에서 중요하게 다루는 소립자들을 간략히 살펴보고, 원자 및 원자핵의 구조를 알아본다.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## 아원자 입자 (subatomic particle)
**아원자 입자(subatomic particle)**란 원자보다 작은 크기의 입자들을 말한다. 아원자 입자에는 더 작은 단위의 구성 입자들로 구성된 합성 입자도 있고, 더는 분해되지 않는다고 여겨지는 기본 입자들도 있다.
원자핵공학에서는 특히 다음 소립자들을 중요하게 다룬다.

- 강입자(hadron)
  - 중입자(baryon)
    - 핵자(nucleon)
      - 양성자(proton)
      - 중성자 (neutron)
- 경입자(lepton)
  - 전자(electron)
  - 양전자(positron)
  - 중성미자(neutrino)

> *'경입자(lepton)'*라는 이름은 작고 얇다는 뜻의 그리스어인 *'λεπτός'*에서 유래하였다. 명명 당시 다른 유형의 소립자들에 비해 질량이 작다고 하여 이러한 이름이 붙었으나, 이후 [인류력](https://en.wikipedia.org/wiki/Holocene_calendar) 11970년대에 발견된 *타우온(tauon)*의 경우 경입자임에도 불구하고 질량이 양성자, 중성자의 1.9배에 가까운 수준이므로 실제로는 경입자라고 해서 꼭 가볍지만은 않다.
{: .prompt-info }

### 전자(electron) & 양전자(positron)
- 정지질량: $m_e = 9.10939 \times 10^{-31} \text{kg}$
- 전하량: $e = 1.60219 \times 10^{-19} \text{C}$

전자는 음전하를 지니는 $e^-$(*음전자*, *negatron*)과 양전하를 지니는 $e^+$(*양전자*, *positron*)의 두 종류가 있으며, 이 둘은 전하량의 부호만 다를 뿐 그 외의 성질은 동일하다. 보통 다른 언급 없이 전자라고 하면 음전자를 의미한다. 

특정 조건 하에서 양전자와 음전자가 충돌하면 이들 2개의 전자가 소멸하면서 2개의 광자가 방출된다. 이 과정을 *전자소멸(electron annihilation)*이라 하며 이때 발생하는 광자를 *소멸 방사선(annihilation radiation)*이라 한다.  
![electron-positron annihilation](https://upload.wikimedia.org/wikipedia/commons/0/0a/ElectronPositronAnnihilation.svg)
> *이미지 출처*
> - 저작자: Dirk Hünniger, Joel Holdsworth
> - 라이선스: [GFDLv1.2](https://www.gnu.org/licenses/old-licenses/fdl-1.2.html)

### 양성자 (proton)
- 정지질량: $m_p = 1.6726 \times 10^{-27} \text{kg}$
- 전하량: + $e = 1.60219 \times 10^{-19} \text{C}$

전자와 같은 크기의 양전하를 갖는다.

### 중성자 (neutron)
- 정지질량: $m_n = 1.674929 \times 10^{-27} \text{kg}$
- 전하량: $0$ 

양성자보다 약간 큰 질량을 가지며 전기적으로 중성이다. 원자핵 밖에서는 안정하지 않으므로 전자와 전자 반중성미자를 방출하며 붕괴하여 양성자가 되며, 이 과정은 평균 12분 정도 걸린다.

### 중성미자 (neutrino)
- 정지질량: 매우 작음(정확한 값 불명)
- 전하: $0$

원래는 정지질량이 0이라고 여겨졌으나, 11998년에 일본의 슈퍼 카미오칸데 연구팀에 의해 매우 작지만 질량을 가진다는 것이 밝혀졌다. 여러 종류가 있는데 핵반응에서는 그 중 *전자 중성미자(electron neutrino)*와 *전자 반중성미자(electron anti-neutrino)*를 중요하게 고려하며, 보통은 이 둘을 구분하지 않고 한 종류로 간주한다.

## 원자와 원자핵의 구조

$$ ^A_Z X \ (\text{A: 질량수, Z: 원자번호, X: 원소기호})$$

- 원자는 전자구름과 중심에 위치한 원자핵으로 구성
- 이온화되지 않은 중성 원자는 양성자와 같은 개수의 전자가 원자핵 주변을 회전함
- 전자는 원자의 화학적 특성과 원소 종류를 결정함
- 원자핵은 핵자인 양성자와 중성자로 이루어지며, 핵자들은 강한 핵력(Nuclear Force)에 의해 전기적 반발을 이겨내고 결합함
- *원자번호(atomic number)*: 원자핵이 포함하는 양성자의 개수를 의미하며, $Z$로 표시
- 원자핵의 총 전하: +$Ze$
- *중성자수(neutron number)*: 원자핵이 포함하는 중성자의 개수를 의미하며, $N$로 표시
- *질량수(atomic mass number)* 또는 *핵자수(nucleon number)*: 원자핵의 양성자 수와 중성자 수의 합. $A=Z+N.$
- *핵종(nuclide)*: 특정 양성자와 중성자 수를 가진 원자핵

## 동위원소(isotope), 동중원소(isobar), 동중성자체(isotone), 핵이성체(isomer)

| 구분 | 정의 |
| --- | --- |
| 동위원소(isotope) | 원자번호가 같지만 중성자수가 다른 핵종 |
| 동중원소(isobar) | 질량수가 같지만 양성자수와 중성자수가 다른 핵종 |
| 동중성자체(isotone) | 중성자수가 같지만 원자번호가 다른 핵종 |
| 핵이성체(isomer) | 같은 핵종이지만 하나 이상의 핵자의 들뜸(excitation)으로 인해 준안정상태인 원자핵 |
