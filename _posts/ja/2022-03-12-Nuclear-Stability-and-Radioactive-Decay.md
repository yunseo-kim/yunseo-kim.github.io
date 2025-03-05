---
title: 核安定性と放射性崩壊
description: セグレ図と放射性崩壊の種類、そして異性体遷移について学ぶ。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## セグレ図（Segre Chart）または核種図表
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *画像出典*
> - 作者：ウィキメディアユーザー [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - ライセンス：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- 原子番号 $Z$ が20より大きい核種の場合、安定化のために陽子数よりも多くの中性子が必要
- 中性子は陽子間の電気的反発力に打ち勝ち、核を束ねる役割を果たす

## 放射性崩壊（Radioactive Decay）が起こる理由
- 特定の中性子と陽子の組み合わせのみが安定な核種を形成する
- 陽子数に対して中性子数が多すぎるか少なすぎると、その核種は不安定となり、*放射性崩壊（radioactive decay）* を起こす
- 崩壊後に生成された核はほとんどの場合励起状態にあるため、ガンマ線やX線の形でエネルギーを放出する

## ベータ崩壊（$\beta$-decay）
### 陽電子崩壊（$\beta^+$-decay）

 $$p \to n+\beta^+ +\nu_e$$
 
- 中性子数が相対的に不足している場合に起こる
- 陽子（$p$）が中性子（$n$）に変わり、陽電子（$\beta^+$）と電子ニュートリノ（$\nu_e$）を放出する
- 原子番号は1減少し、質量数は変化しない

例）$^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### 電子崩壊（$\beta^-$-decay）

$$ n\to p+\beta^- + \overline{\nu}_e $$

- 中性子数が相対的に過剰な場合に起こる
- 中性子（$n$）が陽子（$p$）に変わり、電子（$\beta^-$）と電子反ニュートリノ（$\overline{\nu}_e$）を放出する
- 原子番号は1増加し、質量数は変化しない

例）$^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### 放出される電子（陽電子）のエネルギースペクトル
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *画像出典*
> - 作者：ドイツウィキペディアユーザー [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - ライセンス：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- ベータ崩壊で放出される電子または陽電子は、上記のような連続エネルギースペクトルを示す。
- $\beta^-$ 崩壊：$\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$ 崩壊：$\overline{E}\approx 0.4E_{\text{max}}$

### 崩壊連鎖（Decay Chain）
しばしばベータ崩壊によって形成された *娘核種（daughter nuclide）* も不安定で、連続してベータ崩壊が起こることがある。これは次のような *崩壊連鎖（decay chain）* につながる。

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (stable)} $$ 

## 電子捕獲（Electron Capture）またはK捕獲（K-capture）

$$ p + e \to n + \nu_e $$

- 中性子数が相対的に不足している場合に起こる
- 最内殻（K殻）の電子を捕獲し、原子核内の陽子を中性子に変換する
- 原子番号は1減少し、質量数は変化しない
- 電子捕獲後は電子雲に空隙が形成され、その後外側の他の電子が移動して埋められる際にX線やオージェ電子（Auger electron）を放出する
- 電子捕獲によって生じた娘核種（daughter nuclide）は $\beta^+$ 崩壊によって生成された核と同一であるため、これら二つの過程は互いに競合する

## アルファ崩壊（$\alpha$-decay）
- アルファ粒子（$\alpha$、$^4_2\text{He}$）を放出する
- 原子番号は2だけ減少し、質量数は4だけ減少する
- 鉛より重い核でよく起こる
- ベータ崩壊とは異なり、アルファ崩壊時に放出されるアルファ粒子のエネルギーは量子化されている

例）$^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## 自発核分裂（Spontaneous Fission）
- 非常に重く不安定な核種は、中性子を吸収しなくても自発的に核分裂することがある
- 広義では放射性崩壊に含まれる

## 陽子放出（Proton Emission）
- 陽子が極端に多い不安定な核種の場合、陽子1個を単独で放出することがある
- 原子番号と質量数が1だけ減少する
- 非常にまれに起こる

## 崩壊図と異性体遷移
### 崩壊図（Decay Scheme）
*崩壊図（decay scheme）*：放射性物質のすべての崩壊経路を視覚的に表した図表

### 異性体遷移（Isomeric Transition）
- 放射性崩壊によって形成された核は、変換後も励起状態にある場合があり、この場合ガンマ線の形でエネルギーを放出する（ガンマ線放出時に核種は変化しないため、厳密には崩壊ではないが、慣習的にガンマ崩壊という表現を使用することもある）。
- 励起状態の核はほとんどの場合、非常に短時間でガンマ線を放出して基底状態に遷移するが、特定の場合にはガンマ線放出が遅延し、準安定状態のように見えることがある。このような遅延状態をその核の *異性体状態（isomeric transition）* と呼ぶ。
- 異性体状態からガンマ線を放出して基底状態に遷移することを *異性体遷移（isomeric transition）* と呼び、ITと表記する。
![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *画像出典*
> - 作者：イギリスウィキメディアユーザー [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - ライセンス：法に抵触しない限り、いかなる目的でも制限条件なく自由に使用可能
