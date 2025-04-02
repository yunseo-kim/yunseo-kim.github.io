---
title: 核穩定性及放射性衰變
description: 探討塞格雷圖、放射性衰變類型以及同質異能態轉變。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## 塞格雷圖（Segre Chart）或核素圖表
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *圖片來源*
> - 作者：維基媒體用戶 [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - 授權：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- 對於原子序數 $Z$ 大於20的核素，為了穩定需要比質子數更多的中子
- 中子的作用是克服質子之間的電力排斥，將原子核束縛在一起

## 發生放射性衰變（Radioactive Decay）的原因
- 只有特定的中子和質子組合才能形成穩定的核素
- 如果中子數相對於質子數過多或過少，該核素就會不穩定，進而發生*放射性衰變（radioactive decay）*
- 衰變後產生的原子核大多處於激發態，因此會以伽瑪射線或X射線的形式釋放能量

## 貝他衰變（β-decay）
### 正貝他衰變（$\beta^+$衰變）

 $$p \to n+\beta^+ +\nu_e$$
 
- 當中子數相對不足時發生
- 質子（$p$）變成中子（$n$），同時釋放出正電子（$\beta^+$）和電子中微子（$\nu_e$）
- 原子序數減少1，質量數不變

例）$^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### 負貝他衰變（$\beta^-$衰變）

$$ n\to p+\beta^- + \overline{\nu}_e $$

- 當中子數相對過多時發生
- 中子（$n$）變成質子（$p$），同時釋放出電子（$\beta^-$）和電子反中微子（$\overline{\nu}_e$）
- 原子序數增加1，質量數不變

例）$^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### 釋放的電子（正電子）能量譜
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *圖片來源*
> - 作者：德國維基百科用戶 [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - 授權：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- 貝他衰變中釋放的電子或正電子呈現如上圖所示的連續能量譜。
- $\beta^-$ 衰變：$\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$ 衰變：$\overline{E}\approx 0.4E_{\text{max}}$

### 衰變鏈（Decay Chain）
有時通過貝他衰變形成的*子核素（daughter nuclide）*也不穩定，會連續發生貝他衰變。這形成了所謂的*衰變鏈（decay chain）*。

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (stable)} $$ 

## 電子捕獲（Electron Capture）或K-捕獲（K-capture）

$$ p + e \to n + \nu_e $$

- 當中子數相對不足時發生
- 捕獲最內層（K殼）的電子，將原子核內的質子轉換為中子
- 原子序數減少1，質量數不變
- 電子捕獲後，電子雲中會形成空缺，隨後外層的其他電子會移動填補這個空缺，這時會釋放X射線或奧傑電子（Auger electron）
- 電子捕獲產生的子核素（daughter nuclide）與 $\beta^+$ 衰變產生的核相同，因此這兩個過程相互競爭。

## 阿爾法衰變（α-decay）
- 釋放阿爾法粒子（$\alpha$, $^4_2\text{He}$）
- 原子序數減少2，質量數減少4
- 常見於比鉛更重的核
- 與貝他衰變不同，阿爾法衰變時釋放的阿爾法粒子能量是量子化的。

例）$^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## 自發裂變（Spontaneous Fission）
- 非常重且不穩定的核素可能在不吸收中子的情況下自行發生核裂變
- 廣義上也被歸類為放射性衰變

## 質子發射（Proton Emission）
- 對於質子極度過多的不穩定核素，有時會單獨釋放一個質子
- 原子序數和質量數都減少1
- 非常罕見

## 衰變圖和同質異能態轉變
### 衰變圖（Decay Scheme）
*衰變圖（decay scheme）*：視覺化呈現放射性物質所有衰變路徑的圖表

### 同質異能態轉變（Isomeric Transition）
- 放射性衰變產生的核在轉換後可能仍處於激發態，這種情況下會以伽瑪射線的形式釋放能量（雖然伽瑪射線釋放並不改變核素，嚴格來說不算是衰變，但習慣上有時也稱為伽瑪衰變）。
- 大多數激發態的核會在極短時間內釋放伽瑪射線並回到基態，但在某些特殊情況下，伽瑪射線的釋放會被延遲，看起來像是準穩態。這種延遲狀態被稱為該核的*同質異能態（isomeric transition）*。
- 從同質異能態釋放伽瑪射線並回到基態的過程稱為*同質異能態轉變（isomeric transition）*，用IT表示。
![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *圖片來源*
> - 作者：英國維基媒體用戶 [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - 授權：在不違反法律的情況下，可以無限制地自由使用於任何目的
