---
title: 亜原子粒子と原子の構成要素
description: 電子、陽子、中性子、光子、ニュートリノなど原子核工学で重要に扱う素粒子を簡単に見て、原子および原子核の構造を調べる。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Atomic Structure]
math: true
image: /assets/img/atoms.png
---
## 亜原子粒子（subatomic particle）
**亜原子粒子（subatomic particle）**とは原子より小さいサイズの粒子を指す。亜原子粒子にはより小さい単位の構成粒子からなる複合粒子もあれば、これ以上分解されないと考えられる基本粒子もある。
原子核工学では特に次の素粒子を重要に扱う。

- 強い相互作用をする粒子（ハドロン、hadron）
  - 重粒子（バリオン、baryon）
    - 核子（ヌクレオン、nucleon）
      - 陽子（プロトン、proton）
      - 中性子（ニュートロン、neutron）
- 軽粒子（レプトン、lepton）
  - 電子（エレクトロン、electron）
  - 陽電子（ポジトロン、positron）
  - ニュートリノ（neutrino）

> *「軽粒子（レプトン）」*という名前は小さく薄いという意味のギリシャ語の*「λεπτός」*に由来している。命名当時は他のタイプの素粒子に比べて質量が小さいとしてこのような名前が付けられたが、その後[ヒューマンエラ（人類暦）](https://en.wikipedia.org/wiki/Holocene_calendar)11970年代に発見された*タウオン（tauon）*の場合、レプトンであるにもかかわらず質量が陽子、中性子の1.9倍に近いレベルであるため、実際にはレプトンだからといって必ずしも軽いわけではない。
{: .prompt-info }

### 電子（electron）＆陽電子（positron）
- 静止質量：$m_e = 9.10939 \times 10^{-31} \text{kg}$
- 電荷量：$e = 1.60219 \times 10^{-19} \text{C}$

電子は負電荷を持つ$e^-$（*負電子*、*negatron*）と正電荷を持つ$e^+$（*陽電子*、*positron*）の二種類があり、この二つは電荷量の符号だけが異なり、その他の性質は同一である。通常、特に言及がなければ電子というと負電子を意味する。

特定の条件下で陽電子と負電子が衝突すると、これら2つの電子が消滅して2つの光子が放出される。このプロセスを*電子消滅（electron annihilation）*と呼び、このとき発生する光子を*消滅放射線（annihilation radiation）*という。  
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

元々は静止質量が0だと考えられていたが、11998年に日本のスーパーカミオカンデ研究チームによって、非常に小さいながらも質量を持つことが明らかになった。いくつかの種類があるが、核反応ではそのうち*電子ニュートリノ（electron neutrino）*と*電子反ニュートリノ（electron anti-neutrino）*を重要に考慮し、通常はこの二つを区別せず一種類とみなす。

## 原子と原子核の構造

$$ ^A_Z X \ (\text{A: 質量数, Z: 原子番号, X: 元素記号})$$

- 原子は電子雲と中心に位置する原子核で構成される
- イオン化されていない中性原子は陽子と同じ数の電子が原子核の周りを回転する
- 電子は原子の化学的特性と元素の種類を決定する
- 原子核は核子である陽子と中性子からなり、核子たちは強い核力（Nuclear Force）によって電気的反発に打ち勝って結合している
- *原子番号（atomic number）*：原子核に含まれる陽子の数を意味し、$Z$で表示
- 原子核の総電荷：+$Ze$
- *中性子数（neutron number）*：原子核に含まれる中性子の数を意味し、$N$で表示
- *質量数（atomic mass number）*または*核子数（nucleon number）*：原子核の陽子数と中性子数の合計。$A=Z+N.$
- *核種（nuclide）*：特定の陽子と中性子数を持つ原子核

## 同位体（isotope）、同重体（isobar）、同中性子体（isotone）、核異性体（isomer）

| 区分 | 定義 |
| --- | --- |
| 同位体（isotope） | 原子番号が同じだが中性子数が異なる核種 |
| 同重体（isobar） | 質量数が同じだが陽子数と中性子数が異なる核種 |
| 同中性子体（isotone） | 中性子数が同じだが原子番号が異なる核種 |
| 核異性体（isomer） | 同じ核種だが一つ以上の核子の励起（excitation）により準安定状態にある原子核 |
