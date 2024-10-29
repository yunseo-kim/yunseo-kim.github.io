---
title: "サブアトミック粒子と原子の構成要素"
description: >-
  電子、陽子、中性子、光子、ニュートリノなど、原子核工学で重要に扱われる素粒子を簡単に概観し、原子および原子核の構造を理解する。
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Atomic Structure]
math: true
---

## サブアトミック粒子 (subatomic particle)
**サブアトミック粒子（subatomic particle）**とは、原子よりも小さいサイズの粒子を指す。サブアトミック粒子には、より小さな単位の構成粒子からなる複合粒子もあれば、これ以上分解されないと考えられる基本粒子もある。
原子核工学では、特に以下の素粒子が重要に扱われる。

- ハドロン（hadron）
  - バリオン（baryon）
    - 核子（nucleon）
      - 陽子（proton）
      - 中性子（neutron）
- レプトン（lepton）
  - 電子（electron）
  - 陽電子（positron）
  - ニュートリノ（neutrino）

> *'レプトン（lepton）'*という名前は、小さく薄いという意味のギリシャ語*'λεπτός'*に由来する。命名当時、他の種類の素粒子に比べて質量が小さいとされていたが、その後1970年代に発見された*タウオン（tauon）*の場合、レプトンであるにもかかわらず質量が陽子、中性子の1.9倍に近い水準であるため、実際にはレプトンだからといって必ずしも軽いわけではない。
{: .prompt-info }

### 電子（electron）& 陽電子（positron）
- 静止質量：$m_e = 9.10939 \times 10^{-31} \text{kg}$
- 電荷量：$e = 1.60219 \times 10^{-19} \text{C}$

電子には負電荷を持つ$e^-$（*陰電子*、*negatron*）と正電荷を持つ$e^+$（*陽電子*、*positron*）の2種類があり、この2つは電荷量の符号だけが異なり、他の性質は同じである。通常、特に言及がない場合、電子は陰電子を指す。

特定の条件下で陽電子と陰電子が衝突すると、これら2つの電子が消滅し、2つの光子が放出される。このプロセスを*電子消滅（electron annihilation）*と呼び、このとき発生する光子を*消滅放射線（annihilation radiation）*という。  
![electron-positron annihilation](https://upload.wikimedia.org/wikipedia/commons/0/0a/ElectronPositronAnnihilation.svg)
> *画像出典*
> - 作者：Dirk Hünniger, Joel Holdsworth
> - ライセンス：[GFDLv1.2](https://www.gnu.org/licenses/old-licenses/fdl-1.2.html)

### 陽子（proton）
- 静止質量：$m_p = 1.6726 \times 10^{-27} \text{kg}$
- 電荷量：+ $e = 1.60219 \times 10^{-19} \text{C}$

電子と同じ大きさの正電荷を持つ。

### 中性子（neutron）
- 静止質量：$m_n = 1.674929 \times 10^{-27} \text{kg}$
- 電荷量：$0$ 

陽子よりわずかに大きい質量を持ち、電気的に中性である。原子核の外では安定ではないため、電子と電子反ニュートリノを放出しながら崩壊して陽子になり、このプロセスは平均12分ほどかかる。

### ニュートリノ（neutrino）
- 静止質量：非常に小さい（正確な値は不明）
- 電荷：$0$

元々は静止質量が0だと考えられていたが、1998年に日本のスーパーカミオカンデ研究チームによって、非常に小さいが質量を持つことが明らかになった。いくつかの種類があるが、核反応ではそのうち*電子ニュートリノ（electron neutrino）*と*電子反ニュートリノ（electron anti-neutrino）*が重要に考慮され、通常はこの2つを区別せず1種類として扱う。

## 原子と原子核の構造

$$ ^A_Z X \ (\text{A: 質量数, Z: 原子番号, X: 元素記号})$$

- 原子は電子雲と中心に位置する原子核で構成される
- イオン化されていない中性原子は、陽子と同じ数の電子が原子核の周りを回転する
- 電子は原子の化学的特性と元素の種類を決定する
- 原子核は核子である陽子と中性子で構成され、核子は強い核力（Nuclear Force）によって電気的反発に打ち勝って結合する
- *原子番号（atomic number）*：原子核に含まれる陽子の数を意味し、$Z$で表示する
- 原子核の総電荷：+$Ze$
- *中性子数（neutron number）*：原子核に含まれる中性子の数を意味し、$N$で表示する
- *質量数（atomic mass number）*または*核子数（nucleon number）*：原子核の陽子数と中性子数の和。$A=Z+N.$
- *核種（nuclide）*：特定の陽子数と中性子数を持つ原子核

## 同位体（isotope）、同重体（isobar）、同中性子体（isotone）、核異性体（isomer）

| 区分 | 定義 |
| --- | --- |
| 同位体（isotope） | 原子番号が同じだが中性子数が異なる核種 |
| 同重体（isobar） | 質量数が同じだが陽子数と中性子数が異なる核種 |
| 同中性子体（isotone） | 中性子数が同じだが原子番号が異なる核種 |
| 核異性体（isomer） | 同じ核種だが、1つ以上の核子の励起（excitation）により準安定状態にある原子核 |
