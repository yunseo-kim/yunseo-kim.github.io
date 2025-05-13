---
title: 恆星的核融合反應機制
description: 本文介紹恆星核心中發生的核融合反應，包括質子-質子鏈式反應(proton-proton chain reaction)和碳-氮-氧循環反應(CNO cycle)。這是作者高中一年級時為校內科學社團活動所撰寫的文章，與其他文章不同，採用口語體寫作，為了存檔目的而原文上傳。
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## 質子-質子鏈式反應 (proton-proton chain reaction)
這是人們最常知道的恆星核融合反應。重氫的原子核即氘核(deuteron)是由一個質子(p)和一個中子(n)結合而成。因此，當兩個質子結合形成重氫原子核時，其中一個質子必須轉變為中子。那麼，質子是如何變成中子的呢？

- 中子($n$)變成質子($p$)的同時釋放出電子($e⁻$)和反電子中微子($\nu_e$)，這個過程稱為「[β衰變](/posts/Nuclear-Stability-and-Radioactive-Decay/#負貝他衰變beta-衰變)」。反應式為 $n \rightarrow p + e^{-} + \overline{\nu_e}$。
- 質子($p$)變成中子($n$)的過程則是β衰變的反向過程，因此稱為「[逆β衰變](/posts/Nuclear-Stability-and-Radioactive-Decay/#正貝他衰變beta衰變)」。逆β衰變的反應式是什麼樣子呢？核反應式並沒有什麼特別之處。只需將質子和中子的位置互換，將電子換成正電子，將反電子中微子換成電子中微子即可。表示為 $p \rightarrow n + e^{+} + \nu_e$。

通過上述過程形成重氫原子核後，接著進行 $^2_1D + p \rightarrow {^3_2He}$ 反應生成氦-3原子核，最後兩個氦-3原子核碰撞，產生一個氦-4原子核和兩個質子。  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

實際上，質子-質子鏈式反應的反應路徑不只一種。上述情況是最具代表性的，但除此之外還有幾種路徑。不過，其他路徑在質量小於太陽的恆星中所占比例不高，而在質量大於太陽1.5倍的恆星中，後面將介紹的CNO循環比質子-質子鏈式反應占更大比重，因此這裡不再詳述。

這種質子-質子鏈式反應主要發生在約1000萬K至1400萬K的溫度下。太陽的核心溫度約為1500萬K，其中pp鏈式反應占98.3%（其餘1.3%為CNO循環）。

## 碳-氮-氧循環反應 (CNO Cycle)
CNO循環反應是碳接收質子變成氮，然後氮再接收質子變成氧等過程，最終接收4個質子產生1個氦，並回到碳的反應。其特點是碳、氮、氧起到類似催化劑的作用。理論上，這種CNO循環在質量超過太陽1.5倍的恆星中占主導地位。恆星質量導致反應差異的原因在於質子-質子鏈式反應和CNO循環對溫度依賴性的不同。前者在較低溫度（約400萬K）就能開始，反應速率與溫度的4次方成正比。而後者需要約1500萬K才能開始，但對溫度極為敏感（反應速率與溫度的16次方成正比），因此在溫度超過1700萬K時，CNO循環會占更大比重。

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *圖片來源*
> - 作者：維基媒體用戶 [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - 授權：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

CNO循環同樣存在多種路徑。大致可分為低溫CNO循環（恆星內部）和高溫CNO循環（新星、超新星），每種情況又有三四種反應路徑。由於篇幅有限，無法介紹所有CNO循環反應，因此僅討論最基本的CN循環*，即CNO-I。

> *之所以稱為CN循環（省略O），是因為在該反應過程中不存在氧的穩定同位素。
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

如上圖所示，碳、氮、氧循環作為催化劑。但無論反應路徑如何，整體反應式和產生的能量總量都是相同的。

## 延伸閱讀
- 朴仁奎(Inkyu Park，首爾市立大學物理系教授)，[Naver Cast 物理散步：太陽產生多少中微子？](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- 維基百科，[Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- 維基百科，[CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
