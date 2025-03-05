---
title: 均一混合物と分子の断面積
description: 二種類以上の核種が混ざっている均一混合物の巨視的断面積を計算してみよう。
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## 均一混合物（Homogeneous Mixture）の巨視的断面積
二種類の核種 $X$ と $Y$ が均一に混ざっている混合物を考えてみよう。各核種の原子密度はそれぞれ $N_X$ と $N_Y$ $\text{atom/cm}^3$であり、中性子とこの核との特定の反応に対する反応断面積はそれぞれ $\sigma_X$、$\sigma_Y$ とする。

すると、中性子が原子核 $X$、$Y$ と単位長さあたり衝突する確率はそれぞれ $\Sigma_X=N_X\sigma_X$、$\Sigma_Y=N_Y\sigma_Y$ となるので（[巨視的断面積](/posts/Neutron-Interactions-and-Cross-sections/#巨視的断面積macroscopic-cross-section) 参照）、中性子がこの二種類の原子核と単位長さあたり反応する総確率は次のようになる。

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## 分子の等価断面積（Equivalent Cross-section）
上で見た核が分子形態で存在する場合、式 (1) で求めた混合物の巨視的断面積を単位体積あたりの分子数で割ることで、その分子の等価断面積（equivalent cross-section）を定義することができる。

単位体積あたりの分子 $X_mY_n$ が $N$ 個ある場合、$N_X=mN$、$N_Y=nN$ となり、式 (1) からこの分子の断面積を次のように求めることができる。

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> 式 (1) と (2) は核 $X$ と $Y$ が互いに独立して中性子と反応するという仮定の下で成り立つため、分子と固体による弾性散乱には適用できない。
> 分子と固体による低い中性子エネルギーでの散乱断面積は実験を通じて調べる必要がある。
{: .prompt-warning }
