---
title: '核融合発電: トロイダルピンチからトカマクまで'
description: 核融合の概念と次世代電力源として注目されるようになった背景、核融合発電の商用化に向けて達成すべき技術的目標、そしてトロイダルピンチ(toroidal
  pinch)からITERに至るまでの核融合発電技術の変遷を大きな流れで扱う。 筆者が高校2年生の時に校内の科学部活動のために作成したエッセイで、他の投稿とは異なり口語体で書かれているが、アーカイブ目的で当時の原文をそのままアップロードしたことを明記する。
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## 核融合とは？
核融合とは、2つの原子核が衝突して1つの重い原子核に変換される反応のことを言います。基本的に原子核は内部の陽子によって正電荷を帯びているため、2つの原子核が接近すると電気的な斥力によってお互いに押し合います。しかし、原子核を超高温に加熱すると、原子核の運動エネルギーが電気的斥力に打ち勝ち、2つの原子核が衝突できるようになります。一旦2つの原子核が十分に近づくと、強い核力が作用して1つの原子核に結合するのです。

1920年代末に恒星のエネルギー源が核融合であることが知られ、核融合を物理的に説明できるようになると、核融合を人類の利益のために利用できるかどうかについての議論が行われました。第二次世界大戦が終わってまもなく、核融合エネルギーを制御して活用しようという考えが真剣に検討され、イギリスのリバプール大学やオックスフォード大学、ロンドン大学などで研究が始まりました。

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## 損益分岐点と点火条件
核融合発電において最も基本的な問題の一つは、核融合反応から出るエネルギーが最初に投入されたエネルギーよりも大きくなければならないということです。DT反応ではアルファ粒子と中性子が生成されますが、核融合によって放出されるエネルギーの20%はアルファ粒子が、80%は中性子が持つことになります。アルファ粒子のエネルギーはプラズマの加熱に使われ、中性子のエネルギーが電気エネルギーに変換されます。最初はプラズマの温度を上げるために外部からエネルギーを加える必要がありますが、核融合反応率が十分に増加すると、アルファ粒子のエネルギーだけでプラズマを加熱できるようになり、核融合反応が自己維持されます。この時点を点火と呼び、10〜20keV（約1億〜2億K）の温度範囲で $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$、つまり $\text{プラズマの圧力}(P) \times \text{エネルギー閉じ込め時間}(\tau_{E}) > 5$ のとき点火が起こります。

![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## トロイダルピンチ（toroidal pinch）
1946年、ピーター・トーネマンはオックスフォード大学クラレンドン研究所でピンチ効果（pinch effect）を利用してトーラス内にプラズマを閉じ込める研究を行いました。

図のようにプラズマに電流を流すと、電流を取り囲む方向に周囲に磁場が形成され、電流と磁場の相互作用により内側に力が作用します。したがって理論的には、電流が十分に大きければ、ピンチ効果によってプラズマが壁に触れないようにすることができます。しかし、実験の結果、この方式は非常に不安定であることがわかり、現在ではほとんど研究されていません。

![pinch effect](/assets/img/fusion-power/pinch-effect.png)

<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## ステラレーター（stellarator）
1950年代初頭、プリンストン大学の天体物理学者ライマン・スピッツァーが新しいプラズマ閉じ込め装置を発明し、ステラレーターと名付けました。トロイダルピンチではプラズマ自体に流れる電流によって磁場が作られるのに対し、ステラレーターでは磁場が外部コイルによってのみ形成されます。ステラレーターはプラズマを長時間安定的に維持できるという利点があり、現在でも核融合発電所に実際に適用される潜在的価値が十分にあると認められており、依然として活発に研究が進められています。

![stellarator](/assets/img/fusion-power/stellarator.png)

## トカマク（tokamak, toroidalnaya karmera magnitnaya katushka）
1960年代に入ると核融合研究は停滞期に入りましたが、この頃、モスクワのクルチャトフ研究所でトカマクが初めて考案され、突破口が見出されました。1968年に開催された学術会議でトカマクの成果が発表されると、ほとんどの国で研究の方向性がトカマクへと変わり、現在最も有望な磁場閉じ込め方式となりました。トカマクはプラズマを長時間維持できるうえ、ステラレーターよりもはるかに構造が単純であるという利点があります。

![tokamak](/assets/img/fusion-power/tokamak.png)

## 巨大トカマク装置とITERプロジェクト
1970年代以降、実際の核融合発電にさらに近づくために、巨大規模のトカマク装置が建設されました。欧州連合のJET、アメリカのプリンストンのTFTR、日本のJT-60Uが代表的です。小規模実験装置で得られたデータをもとに、これらの巨大トカマクで出力を高める研究を着実に進めた結果、損益分岐点にほぼ到達しました。現在、核融合発電の可能性を最終的に確認するために、中国、欧州連合、インド、日本、韓国、ロシア、アメリカが協力して、人類最大の国際共同プロジェクトであるITERプロジェクトを進めています。

![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## References
- [Khatri, G.. (2010). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (2005)
