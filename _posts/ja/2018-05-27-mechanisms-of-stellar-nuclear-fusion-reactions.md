---
title: 恒星の核融合反応メカニズム
description: この記事では、恒星の核で起こる核融合反応のうち、陽子-陽子連鎖反応(proton-proton chain reaction)と
  炭素-窒素-酸素循環反応(CNO cycle)を紹介する。筆者が高校1年生の時に校内科学サークル活動のために作成したエッセイで、他の投稿とは
  異なり口語体で書かれているが、アーカイブ目的で当時の原文そのままアップロードしたことを明記する。
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## 陽子-陽子連鎖反応 (proton-proton chain reaction)
人々に最も広く知られている恒星の核融合反応です。重水素の核である重陽子(deuteron)は陽子(p)一つと中性子(n)一つが結合して作られます。したがって、陽子と陽子が結合して重水素の核になるためには、どちらか一方の陽子が中性子に変わらなければなりません。では、どのようにして陽子が中性子に変わることができるのでしょうか？

- 中性子($n$)が陽子($p$)に変わりながら電子($e⁻$)と反ニュートリノ($\nu_e$)を放出するのが「[ベータ崩壊](/posts/Nuclear-Stability-and-Radioactive-Decay/#負のベータ崩壊beta--decay)」です。これを反応式で書くと$n \rightarrow p + e^{-} + \overline{\nu_e}$です。
- 陽子($p$)が中性子($n$)に変わる過程はベータ崩壊の逆過程に相当します。そのため、これを「[逆ベータ崩壊](/posts/Nuclear-Stability-and-Radioactive-Decay/#正のベータ崩壊beta-decay)」と呼びます。では逆ベータ崩壊の反応式はどのようになるでしょうか？核反応式だからといって特別なものではありません。陽子と中性子の位置を入れ替え、電子を陽電子に、反ニュートリノをニュートリノに変えればいいのです。式で表すと$p \rightarrow n + e^{+} + \nu_e$です。

上記の過程を経て重水素原子核が作られた後は、$^2_1D + p \rightarrow {^3_2He}$でヘリウム-3原子核が作られ、最後にヘリウム-3原子核2つが衝突してヘリウム-4原子核と陽子2つが作られることになります。  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

実は陽子-陽子連鎖反応の反応経路は一つだけではありません。上記の場合が最も代表的ですが、これ以外にもいくつかの経路があります。しかし、残りの経路は質量が太陽以下の星で占める割合がそれほど高くなく、質量が太陽の1.5倍以上の星では陽子-陽子連鎖反応よりも後述するCNOサイクルがはるかに大きな割合を占めるため、ここでは別途扱いません。

この陽子-陽子連鎖反応は約1000万K〜1400万K程度の温度で支配的に起こります。太陽の場合、中心部の温度が約1500万K程度で、pp連鎖反応が98.3%を占めます（残りの1.3%はCNOサイクルが占めます）。

## 炭素-窒素-酸素循環反応 (CNO Cycle)
CNO循環反応は、炭素が陽子を受け入れて窒素に変わり、また窒素が陽子を受け入れて酸素に変わる過程などを経て、最終的には陽子4つを受け入れてヘリウム1つを放出し、再び炭素に戻る反応です。炭素、窒素、酸素が触媒のような役割をするのが特徴です。このCNOサイクルは理論的に太陽質量の1.5倍以上の恒星で優勢に作用します。恒星質量による反応の違いは、陽子-陽子連鎖反応とCNOサイクルの温度依存性の違いにあります。前者は400万K付近の比較的低い温度で始まり、反応速度は温度の4乗に比例するといわれています。一方、後者は1500万K程度で始まりますが、温度に非常に敏感で（反応速度が温度の16乗に比例）、1700万K以上の温度ではCNOサイクルがより大きな割合を占めるようになります。

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *画像出典*
> - 作者：ウィキメディアユーザー [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - ライセンス：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

CNOサイクルにも様々な経路が存在します。低温CNOサイクル（恒星内部）と高温CNOサイクル（新星、超新星）に大きく分かれ、それぞれの場合にさらに3〜4つの反応経路が存在します。すべてのCNOサイクル反応を扱いたいところですが、この程度の分量では不足するため、最も基本的なCNサイクル*、つまりCNO-Iについてのみ扱います。

> *Oが抜けたCNサイクルという名称が付いた理由は、該当する反応過程で酸素の安定同位体が存在しないためである。
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

上の図のように炭素、窒素、酸素が循環しながら触媒の役割をします。しかし、反応経路に関係なく、全体の反応式と発生するエネルギーの総量は同じです。

## More Readings
- 朴仁奎（Inkyu Park、ソウル市立大学物理学科教授）、[ネイバーキャスト物理散歩：太陽ではどれだけ多くのニュートリノが作られるのか？](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- ウィキペディア、[Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- ウィキペディア、[CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
