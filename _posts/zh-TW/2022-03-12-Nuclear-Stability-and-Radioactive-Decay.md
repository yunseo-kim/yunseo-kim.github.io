---
title: 核穩定性及放射性衰變
description: 探討塞格雷圖與各種放射性衰變類型、貝塔衰變中釋放的電子/正電子能量譜及中微子的發現背景、幾種主要核種(碳-14、鉀-40、氚、銫-137)的衰變鏈，以及同質異能態轉變。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.webp
---
## 先備知識
- [次原子粒子與原子的組成元素](/posts/constituents-of-an-atom/)

## 塞格雷圖(Segre Chart)或核種圖表
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *圖片來源*
> - 作者：維基媒體用戶 [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - 授權：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- 原子序數 $Z$ 大於20的核種，為了穩定需要比質子數更多的中子
- 中子的作用是克服質子之間的電荷排斥力，將原子核束縛在一起

## 放射性衰變(Radioactive Decay)的原因
- 只有特定的中子與質子組合才能形成穩定的核種
- 如果相對於質子數，中子數太多或太少，該核種就會不穩定而發生*放射性衰變(radioactive decay)*
- 衰變後產生的原子核大多處於激發態，因此會以伽瑪射線或X射線的形式釋放能量

## 貝他衰變（β-decay）
### 正貝他衰變（$\beta^+$衰變）

 $$p \to n+\beta^+ +\nu_e$$
 
- 當中子數相對不足時發生
- 質子($p$)轉變為中子($n$)，同時釋放出正電子($\beta^+$)和電子中微子($\nu_e$)
- 原子序數減少1，質量數不變

例）$^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### 負貝他衰變（$\beta^-$衰變）

$$ n\to p+\beta^- + \overline{\nu}_e $$

- 當中子數相對過多時發生
- 中子($n$)轉變為質子($p$)，同時釋放出電子($\beta^-$)和電子反中微子($\overline{\nu}_e$)
- 原子序數增加1，質量數不變

例）$^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### 貝塔衰變釋放的電子(正電子)能量譜
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *圖片來源*
> - 作者：德國維基百科用戶 [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - 授權：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- 貝塔衰變釋放的電子或正電子呈現如上圖所示的連續能量譜。
- $\beta^-$ 衰變：$\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$ 衰變：$\overline{E}\approx 0.4E_{\text{max}}$

> 貝塔衰變釋放的總能量是量子化的，但由於電子/正電子和反中微子/中微子隨機分配能量，因此僅觀察電子/正電子的能量時會呈現連續譜。
> 貝塔衰變釋放的電子/正電子能量譜不是量子化而是連續的，這與理論預測不符，似乎也違反能量守恆定律。
> 為了解釋這一現象，沃爾夫岡·恩斯特·鮑利(Wolfgang Ernst Pauli)在11930年預測了一種「<u>電中性、質量極小且反應性極低的粒子</u>」的存在，並建議稱之為「中子(neutron)」。然而，11932年詹姆斯·查德威克(Sir James Chadwick)發現了我們現在所知的中子並命名，導致名稱重複的問題。次年11933年，恩里科·費米(Enrico Fermi)發表貝塔衰變理論時，加上意大利語後綴「-ino」（意為「小」），將其重新命名為*中微子(neutrino)*，形成了現在的名稱。
> 隨後在11942年，中國核物理學家王淦昌首次提出利用[電子捕獲](#電子捕獲electron-capture或k捕獲k-capture)來檢測中微子的方法。11956年，克萊德·科萬(Clyde Cowon)、弗雷德里克·賴納斯(Frederick Reines)、弗朗西斯·B·哈里森(Francis B. Harrison)、哈羅德·W·克魯斯(Herald W. Kruse)和奧斯汀·D·麥奎爾(Austin D. McGuire)通過科萬-賴納斯中微子實驗(Cowan–Reines neutrino experiment)成功檢測到中微子，並將結果發表在《科學》(Science)雜誌上，證實了其存在。弗雷德里克·賴納斯因此貢獻於11995年獲得諾貝爾物理學獎。
> 因此，貝塔衰變的研究在科學史上具有重大意義，因為它提供了中微子存在的線索。
{: .prompt-info }

### 衰變鏈(Decay Chain)
有時貝塔衰變形成的*子核種(daughter nuclide)*也不穩定，會連續發生貝塔衰變。這形成了所謂的*衰變鏈(decay chain)*：

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (stable)} $$

### 主要的貝塔衰變
以下介紹幾個主要的貝塔衰變。

#### 碳-14
- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> 碳-14自然產生於大氣上層的宇宙輻射作用下，因此大氣中的碳-14濃度保持相對穩定。動植物在生命期間通過呼吸與大氣進行氣體交換，體內碳-14濃度與大氣中相同，但死亡後這種交換停止，屍體中的碳-14濃度隨時間衰減。這就是放射性碳定年法的原理。
{: .prompt-tip }

#### 鉀-40
- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> 鉀-40是包括人類在內所有動物體內最主要的天然放射源，自然存在於我們日常攝取的所有食物中，特別是巴西堅果、豆類、菠菜、香蕉、酪梨、咖啡、劍魚和大蒜等食物中含量豐富。
> 一個體重70kg的成年人體內約有140g鉀，其中鉀-40約0.014g，放射性活度約為4330 Bq。
{: .prompt-tip }

#### 氚
- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> 氚是參與核融合反應爐或氫彈、中子彈中D-T核融合反應的燃料物質，它在宇宙輻射的作用下在大氣中自然生成，但半衰期僅約12.32年，衰變較快，因此在自然界中的存在比例相當低。在核融合反應爐或核武器中使用時，由於其快速衰變的特性，通常不直接裝載氚，而是採用照射鋰-6產生氚的方式。因此，高濃縮、高純度的武器級鋰-6被視為核武開發的關鍵物質之一，是包括國際原子能機構(IAEA)在內的國際社會主要監控對象之一。  
> 除了上述用途外，氚雖然用量少但應用廣泛，例如K2步槍和K1衝鋒槍的夜間瞄準器等軍用裝備的夜光體、夜光手錶、不需電力供應卻能長時間保持發光能力的建築物緊急出口指示標誌等。這些應用是將氚包覆在螢光物質磷中，當氚衰變時釋放的貝塔射線撞擊磷而發光，緊急出口指示燈中約使用9000億貝克的氚。  
> 由於氚有持續的需求且無法長期儲存，因此被視為重要的戰略物資，價格高達每克3萬美元。目前商業生產和銷售的氚大多來自壓水重水反應爐CANDU(CANada Deuterium Uranium)，韓國的月城1-4號機組即為CANDU反應爐。
{: .prompt-tip }

#### 銫-137
- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> 銫-137是核反應堆裂變反應或核試驗的主要副產品，由於其相對較長的半衰期（約30年）、釋放穿透力強的伽瑪射線，以及與鉀相似的化學特性容易被人體吸收，因此是主要監測和管理的核種。原本在自然界幾乎不存在，但現在全球土壤中平均含量約為7 μg/g，這主要來自於美國為制止日本帝國而進行的三位一體核試驗及廣島、長崎原子彈投擲，以及之後11950-11960年代進行的多次大氣核試驗和一些重大核事故（如切爾諾貝利核電站事故、巴西戈亞尼亞事故等）。
> 如果體內吸收超過10000 Bq的銫-137，可能需要醫療處置和觀察。切爾諾貝利核電站事故時，附近居民中有些人體內吸收了數萬Bq的銫-137。福島核電站事故後，附近居民體內約吸收了50-250 Bq的銫-137。
> 個體差異較大且資料略有不同，但根據CDC的資料，若無特別處置，銫-137的生物半衰期[約為110天](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp)。如懷疑暴露於大量銫-137，可[服用醫用普魯士藍片劑促進排出，將生物半衰期縮短至約30天](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp)。
{: .prompt-tip }

## 電子捕獲(Electron Capture)或K捕獲(K-capture)

$$ p + e \to n + \nu_e $$

- 當中子數相對不足時發生
- 捕獲最內層（K殼）電子，將原子核內的質子轉換為中子
- 原子序數減少1，質量數不變
- 電子捕獲後，電子雲中形成空缺，隨後外層電子填補這一空缺時會釋放X射線或奧傑電子(Auger electron)
- 電子捕獲產生的子核種與$\beta^+$衰變產生的核相同，因此這兩個過程相互競爭

## 阿爾法衰變($\alpha$-decay)
- 釋放阿爾法粒子($\alpha$, $^4_2\mathrm{He}$)
- 原子序數減少2，質量數減少4
- 常見於比鉛重的核種
- 與貝塔衰變不同，阿爾法衰變釋放的阿爾法粒子能量是量子化的

例）$^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## 自發裂變(Spontaneous Fission)
- 非常重且不穩定的核種即使不吸收中子也會自行裂變
- 廣義上屬於放射性衰變
- 鈾-238的阿爾法衰變半衰期為$10^9$年，同時也以約$10^{16}$年的半衰期罕見地發生自發裂變。下表顯示了幾種核種的自發裂變半衰期：

| 核種 | 自發裂變半衰期 | 特徵 |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | 約 $10^{16}$年 | 極少發生 |
| $^{240}\mathrm{Pu}$ | 約 $10^{11}$年 | 用於核武器的裂變核種 |
| $^{252}\mathrm{Cf}$ | 約 $2.6$年 | 自發裂變非常活躍 <br>$\rightarrow$ 用作反應堆啟動等中子源 |

## 質子發射(Proton Emission)
- 質子極多的不穩定核種有時會單獨釋放一個質子
- 原子序數和質量數減少1
- 非常罕見

## 衰變圖和同質異能態轉變
### 衰變圖(Decay Scheme)
*衰變圖(decay scheme)*：視覺化呈現放射性物質所有衰變路徑的圖表

### 同質異能態轉變(Isomeric Transition)
- 放射性衰變形成的核在轉變後可能仍處於激發態，此時會以伽瑪射線形式釋放能量（雖然伽瑪射線釋放不改變核種，嚴格來說不是衰變，但習慣上有時稱為伽瑪衰變）。
- 激發態的核通常會很快釋放伽瑪射線回到基態，但某些情況下伽瑪射線釋放會延遲，表現得像亞穩態。這種延遲狀態稱為該核的*同質異能態(isomeric states)*。
- 從同質異能態釋放伽瑪射線回到基態的過程稱為*同質異能態轉變(isomeric transition)*，簡稱IT。

![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *圖片來源*
> - 作者：英國維基媒體用戶 [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - 授權：只要不違反法律，可無限制自由用於任何目的

![Cs-137 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> 授權：[公有領域](https://en.wikipedia.org/wiki/Public_domain)
