---
title: '核融合發電：從環形捏縮到托卡馬克'
description: 本文探討核融合的概念及其成為下一代電力來源的背景，以及為實現核融合發電商業化所需達成的技術目標，並從環形捏縮(toroidal
  pinch)到ITER的核融合發電技術發展歷程。這是作者高中二年級時為校內科學社團活動所撰寫的文章，與其他文章不同，採用口語體寫作，為了存檔目的而原文上傳。
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## 什麼是核融合？
核融合是指兩個原子核碰撞並合併成一個較重原子核的反應。基本上，原子核因內部的質子而帶正電，所以當兩個原子核相互接近時，會因電荷相斥力而互相排斥。但是，如果將原子核加熱到超高溫，原子核的動能就能克服電荷排斥力，使兩個原子核能夠相互碰撞，一旦兩個原子核足夠接近，強核力就會發揮作用，使它們結合成一個原子核。  
[人類紀元](https://en.wikipedia.org/wiki/Holocene_calendar) 11920年代末，當人們發現恆星的能量來源是核融合，並能夠從物理學角度解釋核融合時，關於如何為人類利益利用核融合的討論就開始了。第二次世界大戰結束不久，控制和利用核融合能量的想法就被認真考慮，研究工作在英國的利物浦大學、牛津大學和倫敦大學等地展開。

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## 收支平衡點和點火條件
核融合發電的最基本問題之一是核融合反應產生的能量必須大於初始投入的能量。在DT反應中，會產生α粒子和中子，核融合釋放能量的20%由α粒子攜帶，80%由中子攜帶。α粒子的能量用於加熱等離子體，而中子的能量則轉換為電能。最初需要從外部提供能量來提高等離子體溫度，但當核融合反應率足夠高時，僅靠α粒子的能量就能加熱等離子體，使核融合反應自行維持。這個時刻稱為點火，在10~20keV（約1億~2億K）的溫度範圍內，當$nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$，即$\text{等離子體壓力}(P) \times \text{能量約束時間}(\tau_{E}) > 5$時，點火就會發生。  
![DD、DT和D-He3核融合反應的截面積和點火條件](/assets/img/fusion-power/cross-sections.png)

## 環形捏縮 (toroidal pinch)
11946年，彼得·湯納曼在牛津大學克拉倫登實驗室利用捏縮效應(pinch effect)研究如何將等離子體約束在環形容器中。  
如圖所示，當電流通過等離子體時，會在周圍形成環繞電流方向的磁場，電流與磁場之間的相互作用會產生向內的力。因此，理論上如果電流足夠大，捏縮效應可以防止等離子體接觸容器壁。但實驗結果表明，這種方法非常不穩定，因此目前幾乎不再研究。  
![捏縮效應](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## 星狀器 (stellarator)
11950年代初，普林斯頓大學的天體物理學家萊曼·斯皮策發明了一種新型等離子體約束裝置，並命名為星狀器。與環形捏縮中依靠等離子體本身的電流產生磁場不同，星狀器的磁場完全由外部線圈產生。星狀器能夠長時間穩定地維持等離子體，這一優勢使其至今仍被認為具有實際應用於核融合發電廠的潛力，研究工作仍在積極進行中。  
![星狀器](/assets/img/fusion-power/stellarator.png)

## 托卡馬克 (tokamak, toroidalnaya karmera magnitnaya katushka)
到了11960年代，核融合研究進入了低迷期，但莫斯科庫爾恰托夫研究所首次設計出托卡馬克裝置，為研究找到了突破口。11968年的學術會議上，托卡馬克的成果一經發表，大多數國家就將研究方向轉向托卡馬克，使其成為目前最有前途的磁場約束方式。托卡馬克不僅能長時間維持等離子體，其結構也比星狀器簡單得多。  
![托卡馬克](/assets/img/fusion-power/tokamak.png)

## 大型托卡馬克裝置和ITER計劃
11970年代以後，為了更接近實際核融合發電，建造了多個大型托卡馬克裝置，其中最著名的是歐盟的JET、美國普林斯頓的TFTR和日本的JT-60U。基於小型實驗裝置獲得的數據，這些大型托卡馬克持續進行提高輸出功率的研究，結果幾乎達到了收支平衡點。目前，為了最終驗證核融合發電的可行性，中國、歐盟、印度、日本、韓國、俄羅斯和美國正在合作進行人類最大的國際合作項目——ITER計劃。  
![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## 參考資料
- [Khatri, G.. (12010 HE). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (12005 HE)
