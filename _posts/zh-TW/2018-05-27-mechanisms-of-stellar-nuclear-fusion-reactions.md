---
title: 恆星的核融合反應機制
description: 本文介紹恆星核心中發生的核融合反應，包括質子-質子鏈反應(proton-proton chain reaction)和碳-氮-氧循環反應(CNO cycle)。這是作者在高中一年級時為校內科學社團活動所撰寫的文章，與其他文章不同，採用口語化的寫作風格，為了存檔目的而原文上傳。
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## 質子-質子鏈反應 (proton-proton chain reaction)
這是人們最常知道的恆星核融合反應。重氫的原子核，即氘核（deuteron），是由一個質子（p）和一個中子（n）結合而成的。因此，要使兩個質子結合成重氫的原子核，其中一個質子必須變成中子。那麼，質子是如何變成中子的呢？

- 中子（$n$）變成質子（$p$）並釋放出電子（$e⁻$）和反電子中微子（$\nu_e$）的過程稱為「[β衰變](/posts/Nuclear-Stability-and-Radioactive-Decay/#負貝他衰變beta-衰變)」。其反應方程式為 $n \rightarrow p + e^{-} + \overline{\nu_e}$。
- 質子（$p$）變成中子（$n$）的過程是β衰變的反過程。因此，這被稱為「[逆β衰變](/posts/Nuclear-Stability-and-Radioactive-Decay/#正貝他衰變beta衰變)」。那麼，逆β衰變的反應方程式是什麼樣的呢？核反應方程式並沒有什麼特別之處。只需將質子和中子的位置互換，將電子改為正電子，將反電子中微子改為電子中微子即可。用方程式表示為 $p \rightarrow n + e^{+} + \nu_e$。

通過上述過程形成重氫原子核後，接著進行 $^2_1D + p \rightarrow {^3_2He}$ 反應生成氦-3原子核，最後兩個氦-3原子核碰撞形成一個氦-4原子核和兩個質子。  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

事實上，質子-質子鏈反應的反應路徑不只一種。上述情況是最典型的，但除此之外還有幾種路徑。然而，其他路徑在質量小於太陽的恆星中所占比例不高，而在質量大於太陽1.5倍的恆星中，後面將討論的CNO循環比質子-質子鏈反應占更大比例，因此這裡不再詳細討論。

這種質子-質子鏈反應主要發生在大約1000萬K到1400萬K的溫度範圍內。以太陽為例，其核心溫度約為1500萬K，pp鏈反應占98.3%（剩餘1.3%為CNO循環）。

## 碳-氮-氧循環反應 (CNO Cycle)
CNO循環反應是碳接受質子變成氮，然後氮再接受質子變成氧等過程，最終接受4個質子產生1個氦，然後又回到碳的反應。其特點是碳、氮、氧起到類似催化劑的作用。理論上，這種CNO循環在質量大於太陽1.5倍的恆星中占主導地位。不同恆星質量下反應的差異在於質子-質子鏈反應和CNO循環對溫度的依賴性不同。前者在相對較低的400萬K左右開始，反應速率與溫度的4次方成正比。而後者在1500萬K左右開始，但對溫度非常敏感（反應速率與溫度的16次方成正比），在1700萬K以上的溫度下，CNO循環占更大比例。

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *圖片來源*
> - 作者：維基媒體用戶 [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - 授權：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

CNO循環也存在多種路徑。大致可分為低溫CNO循環（恆星內部）和高溫CNO循環（新星、超新星），每種情況又有三四種反應路徑。雖然想介紹所有CNO循環反應，但這樣的篇幅不夠，所以只討論最基本的CN循環*，即CNO-I。

> *之所以稱為CN循環而不包括O，是因為在該反應過程中不存在氧的穩定同位素。
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

如上圖所示，碳、氮、氧循環並起到催化劑的作用。但無論反應路徑如何，整體反應方程式和產生的能量總量都是相同的。

## 更多閱讀
- 朴仁奎（首爾市立大學物理系教授），[Naver Cast 物理漫步：太陽中產生多少中微子？](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- 維基百科，[Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- 維基百科，[CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
