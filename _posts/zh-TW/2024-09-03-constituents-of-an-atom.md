---
title: 亞原子粒子與原子的組成元素
description: 簡要探討電子、質子、中子、光子、中微子等原子核工程中重要的基本粒子，並了解原子及原子核的結構。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## 亞原子粒子 (subatomic particle)
**亞原子粒子(subatomic particle)**是指比原子更小的粒子。亞原子粒子中有些是由更小單位的組成粒子構成的複合粒子，也有被認為不能再分解的基本粒子。
在原子核工程中，特別重視以下基本粒子：

- 強子(hadron)
  - 重子(baryon)
    - 核子(nucleon)
      - 質子(proton)
      - 中子(neutron)
- 輕子(lepton)
  - 電子(electron)
  - 正電子(positron)
  - 中微子(neutrino)

> *「輕子(lepton)」*這個名稱源自希臘語*「λεπτός」*，意為小而薄。命名當時是因為相較於其他類型的基本粒子，它的質量較小，但在[人類紀年](https://en.wikipedia.org/wiki/Holocene_calendar) 11970年代發現的*陶子(tauon)*雖然是輕子，但質量卻接近質子、中子的1.9倍，所以實際上並非所有輕子都是輕的。
{: .prompt-info }

### 電子(electron) & 正電子(positron)
- 靜止質量：$m_e = 9.10939 \times 10^{-31} \text{kg}$
- 電荷量：$e = 1.60219 \times 10^{-19} \text{C}$

電子有帶負電荷的$e^-$(*負電子*, *negatron*)和帶正電荷的$e^+$(*正電子*, *positron*)兩種，這兩者除了電荷的正負不同外，其他特性都相同。通常不特別說明時，電子指的是負電子。

在特定條件下，當正電子與負電子相撞時，這兩個電子會湮滅並釋放出兩個光子。這個過程稱為*電子湮滅(electron annihilation)*，而產生的光子稱為*湮滅輻射(annihilation radiation)*。  
![electron-positron annihilation](https://upload.wikimedia.org/wikipedia/commons/0/0a/ElectronPositronAnnihilation.svg)
> *圖片來源*
> - 作者：Dirk Hünniger, Joel Holdsworth
> - 授權：[GFDLv1.2](https://www.gnu.org/licenses/old-licenses/fdl-1.2.html)

### 質子(proton)
- 靜止質量：$m_p = 1.6726 \times 10^{-27} \text{kg}$
- 電荷量：+ $e = 1.60219 \times 10^{-19} \text{C}$

帶有與電子相同大小但正電荷的粒子。

### 中子(neutron)
- 靜止質量：$m_n = 1.674929 \times 10^{-27} \text{kg}$
- 電荷量：$0$ 

質量略大於質子，電性中性。在原子核外不穩定，會釋放電子和電子反中微子而衰變成質子，這個過程平均需要約12分鐘。

### 中微子(neutrino)
- 靜止質量：非常小（確切值未知）
- 電荷：$0$

原本被認為靜止質量為0，但在11998年，日本超級神岡探測器研究團隊證實它具有極小但非零的質量。中微子有多種類型，在核反應中主要考慮*電子中微子(electron neutrino)*和*電子反中微子(electron anti-neutrino)*，通常不區分這兩者而視為同一種類。

## 原子和原子核的結構

$$ ^A_Z X \ (\text{A: 質量數, Z: 原子序數, X: 元素符號})$$

- 原子由電子雲和位於中心的原子核組成
- 未電離的中性原子有與質子數量相同的電子圍繞原子核旋轉
- 電子決定原子的化學特性和元素種類
- 原子核由核子（質子和中子）組成，核子間通過強核力(Nuclear Force)克服電荷排斥而結合
- *原子序數(atomic number)*：原子核中質子的數量，用$Z$表示
- 原子核的總電荷：+$Ze$
- *中子數(neutron number)*：原子核中中子的數量，用$N$表示
- *質量數(atomic mass number)*或*核子數(nucleon number)*：原子核中質子數和中子數的總和。$A=Z+N.$
- *核素(nuclide)*：具有特定質子數和中子數的原子核

## 同位素(isotope)、同質異位素(isobar)、同中子素(isotone)、同質異能素(isomer)

| 類型 | 定義 |
| --- | --- |
| 同位素(isotope) | 原子序數相同但中子數不同的核素 |
| 同質異位素(isobar) | 質量數相同但質子數和中子數不同的核素 |
| 同中子素(isotone) | 中子數相同但原子序數不同的核素 |
| 同質異能素(isomer) | 相同核素但因一個或多個核子處於激發態(excitation)而呈準穩定狀態的原子核 |
