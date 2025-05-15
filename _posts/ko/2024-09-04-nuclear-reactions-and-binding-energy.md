---
title: 핵반응과 결합에너지
description: 핵반응의 표현식과 Q값(Q-value)의 정의, 질량 결손(mass defect)와 결합에너지(binding energy)의 개념을 알아본다.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## 핵반응 (Nuclear Reaction)
### 핵반응에서의 기본 법칙
*핵반응(nuclear reaction)*: 2개의 서로 다른 원자핵끼리 혹은 원자핵과 핵자가 충돌하여 2개 이상의 새로운 핵 입자들이나 또는 감마선을 생성하는 반응

두 원자핵 $a$, $b$가 반응하여 생성물로 원자핵 또는 감마선 $c$, $d$가 생성된다고 하면, 이 반응은 아래와 같이 표현한다.

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

핵반응에서는 아래의 네 가지 기본 법칙이 성립한다.

- *핵자수 보존법칙(conservation of nucleon)*: 총 핵자수는 반응 전후 동일하다. 핵자의 종류는 바뀔 수 있으므로, 양성자와 중성자 각각이 보존되지는 않는다.
- *전하량 보존법칙(conservation of charge)*: 입자들의 전하량의 총합은 반응 전후 동일하다.
- *운동량 보존법칙(conservation of momentum)*: 입자들의 운동량의 총합은 반응 전후 동일하다.
- *에너지 보존법칙(conservation of energy)*: <u>정지질량 에너지를 포함한</u> 총 에너지는 반응 전후 동일하다.

### 발열반응(exothermic reaction) & 흡열반응(endothermic reaction)
식 ($\ref{nuclear_reaction}$)의 핵반응에서 반응 전의 총 에너지는 $a$와 $b$의 정지질량 에너지와 운동에너지의 합이며, 반응 이후의 총 에너지는 $c$와 $d$의 정지질량 에너지와 운동에너지의 합이다. 따라서 에너지 보존법칙에 의해 다음이 성립한다.

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

위 식을 정리하면 아래와 같다.

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

즉, 핵반응 전후 운동에너지의 차이는 핵반응 전후 정지질량의 차이와 같다는 것을 알 수 있다.
마지막 식의 우변을 핵반응의 *Q값(Q-value)*이라고 하며 아래와 같이 정의한다.

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

Q값은 항상 MeV 단위로 나타내며, 1 amu의 질량에 대한 정지질량 에너지가 보통 931MeV이므로 Q값을 아래와 같이 쓸 수도 있다.

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *발열반응(exothermic reaction)*: $Q>0$인 핵반응, 질량 일부가 운동에너지로 전환되어 반응 후 운동에너지 증가
- *흡열반응(endothermic reaction)*: $Q<0$인 핵반응, 운동에너지 일부가 질량으로 전환되어 반응 후 운동에너지 감소

| 핵반응 종류 | Q값 | 반응 전후 질량 변화 | 반응 전후 운동에너지 변화 |
| :---: | :---: | :---: | :---: |
| 발열반응 | $Q>0$ | $\Delta m<0$ (감소) | $\Delta E>0$ (증가) |
| 흡열반응 | $Q<0$ | $\Delta m>0$ (증가) | $\Delta E<0$ (감소) |

### 핵반응의 간략한 표현
식 ($\ref{nuclear_reaction}$)의 핵반응은 아래와 같이 간략히 표현할 수 있다.

$$ a(b, c)d $$

이는 $a$에 $b$가 입사되어 $c$를 방출하고 $d$로 변환되는 핵반응을 의미한다.

#### ex)
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## 결합에너지 (Binding Energy)
### 질량 결손 (Mass Defect)
모든 핵의 질량은 그 핵을 구성하는 중성자 및 양성자의 질량 합보다 약간 작다. 이 차이를 *질량 결손(mass defect)*이라고 한다.

핵의 질량을 $M_A$라고 하면, 임의의 핵의 질량 결손 $\Delta$는 다음과 같이 계산할 수 있다.

$$ \Delta = ZM_p + NM_n - M_A. $$

질량 결손 $\Delta$를 에너지 단위로 표현하면 임의의 핵을 그 구성 핵자들로 쪼개는 데 필요한 에너지가 된다. 핵자들을 붙잡아 두는 에너지라는 의미에서 이를 *결합에너지(bindig energy)*라고 한다. 거꾸로 A개의 핵자들로부터 원자핵이 생성되는 경우, 결합에너지 $\Delta$만큼 에너지 준위가 낮아지므로 핵반응 과정에서 그만큼의 에너지를 주변으로 방출한다.

### 핵자당 평균 결합에너지
원자핵의 총 결합에너지는 질량수 $A$가 증가할수록 증가하지만, 그 기울기가 일정하지는 않다.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
핵자당 평균 결합에너지 $\Delta/A$는 낮은 질량수에서는 가파르게 증가하나, $A\geq56$인 무거운 원자핵에서는 완만한 기울기로 감소함을 위 이미지에서 확인할 수 있다.

### 핵반응의 Q값과 결합에너지의 관계
식 ($\ref{nuclear_reaction}$)의 핵반응에서 $a$ 핵의 결합에너지는 

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

이고, $a$의 질량은

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

가 된다. 같은 방법으로 $b$, $c$, $d$ 핵에 대해서도

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

이다.

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

라고 간주하고 위의 식들을 식 ($\ref{Q_value}$)에 대입하면

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

이다. 이는 어떤 핵반응 과정에 의해 덜 안정한 두 핵이 결합하여 더 안정한 핵이 만들어질 때는 항상 에너지가 방출됨을 의미한다.

### 핵융합(Nuclear Fusion)과 핵분열(Nuclear Fission)
$2.23\text{MeV}$의 결합에너지를 가지는 중수소와 $8.48\text{MeV}$의 결합에너지를 가지는 삼중수소가 결합하여 $28.3\text{MeV}$의 결합에너지를 가지는 $^4\text{He}$를 생성하고 중성자 1개를 방출하는 핵반응의 경우

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

반응 전후의 결합에너지 차이에 해당하는 $28.3-(2.23+8.48)=17.6\text{MeV}$의 에너지(핵자당 $3.52\text{MeV}$)를 헬륨 원자핵과 중성자의 운동에너지의 형태로 방출한다.

식 ($\ref{nuclear_fusion}$)와 같이 질량수가 작은 2개의 가벼운 원자핵이 결합하여 반응 전보다 질량수가 큰 무거운 원자핵을 형성하는 반응을 *핵융합(nuclear fusion)*이라 한다. 이는 태양을 비롯한 모든 항성의 에너지원이며, 언젠가는 인류가 직접 동력원으로 이용할 날이 올 것이다.

한편, 결합에너지가 약 $1780\text{MeV}$인 $^{235}\text{U}$가 중성자를 흡수한 뒤 결합에너지가 $783\text{MeV}$인 $^{92}\text{Kr}$과 약 $1170\text{MeV}$인 $^{141}\text{Ba}$로 분리되며 3개의 중성자를 방출하는 핵반응의 경우

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

반응 전후의 결합에너지 차이에 해당하는 $783+1170-1780=173\text{MeV}$의 에너지(핵자당 $0.733\text{MeV}$)를 방출한다.

식 ($\ref{nuclear_fission}$)와 같이 무거운 원자핵이 가벼운 원자핵들로 분리되는 반응을 *핵분열(nuclear fission)*이라 하며, 아이젠하워 제34대 미국 대통령의 '원자력의 평화적 이용(Atoms for Peace)' 연설과 소련의 오브닌스크 원자력 발전소 이래로 전력원으로 널리 활용되고 있다.

## 마법수
어떤 핵을 이루는 중성자 수 혹은 양성자 수가 2, 6, 8, 14, 20, 28, 50, 82, 126개일 때 그 핵은 특히 안정한 경향이 있다. 이러한 핵자수를 *마법수(magic number)*라고 한다. 이 수는 핵 안의 핵자 껍질을 채우기 위해 필요한 중성자 및 양성자 수에 해당하며, 원자 바깥쪽의 전자 껍질이 채워지는 것과 유사하다.

마법수에 해당하는 핵종은 핵공학에서 실질적으로 유용하게 활용하기도 한다. 대표적인 예시가 50개의 중성자를 갖는 지르코늄-90($^{90}_{40} \mathrm{Zr}$)인데, 안정적이어서 중성자를 잘 흡수하지 않는 성질이 있어 원자로 노심 내의 연료봉 피복재 등으로 널리 사용한다.
