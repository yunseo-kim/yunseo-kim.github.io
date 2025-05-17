---
title: 中性子減衰(Neutron Attenuation)と平均自由行程(Mean Free Path)
description: 単一エネルギー中性子ビームを標的に照射した際の標的透過距離に応じた中性子ビームの強度を計算し、これから中性子の平均自由行程を導出する。また、二種類以上の核種が混合した均質混合物と分子の巨視的断面積を計算する方法を示す。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---

## 中性子減衰(Neutron Attenuation)
強度 $I_0$の単一エネルギー中性子ビームを厚さ $X$の標的に照射しており、標的の後方にある距離に中性子検出器が置かれている。標的と検出器はどちらも非常に小さく、検出器は標的を通過して出てくる中性子の一部だけを検出できる小さな立体角を持つと仮定しよう。そうすると標的に衝突するすべての中性子は吸収されるか散乱されて別の方向に逸脱するため、標的と反応しなかった中性子だけが検出器に入射する。

標的内で距離 $x$だけ進行する間に衝突せずに残っている中性子ビームの強度を $I(x)$とする。中性子ビームが十分に薄い厚さ $\tau$の標的を通過するとき、単位面積当たりの衝突数は $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$([中性子相互作用と反応断面積](/posts/Neutron-Interactions-and-Cross-sections/)の式 [(1)](/posts/Neutron-Interactions-and-Cross-sections/#mjx-eqn:eqn:microscopic_cross_section)と [(8)](/posts/Neutron-Interactions-and-Cross-sections/#mjx-eqn:eqn:reaction_rate) 参照)となるため、標的内で $dx$だけ進行する間の中性子ビーム強度の減少量は次のようになる。

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

上記の式を積分すると次のような結果が得られる。

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

したがって中性子ビームの強度は標的透過距離が長くなるにつれて指数関数的に減少することがわかる。

## 平均自由行程 (Mean Free Path)
- 中性子が原子核と一度衝突した後、続いて別の原子核と衝突するまでの平均移動距離
- つまり、中性子が衝突なしに進行する平均距離
- 記号 $\lambda$で表記

$I(x)/I_0=e^{-\Sigma_t x}$は中性子が媒質内で距離 $x$だけ進行する間に原子核と衝突しない確率を意味する。したがって、ある中性子が媒質内で距離 $x$まで衝突なしに進行した後、距離 $dx$ 以内で衝突する確率 $p(x)dx$は次のようになる。

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

これから*平均自由行程(mean free path)* $\lambda$を次のように求めることができる。

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## 均質混合物(Homogeneous Mixture)の巨視的断面積
二種類の核種 $X$と $Y$が均一に混合している混合物を考えてみよう。各核種の原子密度はそれぞれ $N_X$と $N_Y$ $\text{atom/cm}^3$であり、中性子とこれらの核との特定反応に対する反応断面積はそれぞれ $\sigma_X$、$\sigma_Y$とする。

すると中性子が原子核 $X$、$Y$と単位長さあたり衝突する確率はそれぞれ $\Sigma_X=N_X\sigma_X$、$\Sigma_Y=N_Y\sigma_Y$となるため([マクロ断面積](/posts/Neutron-Interactions-and-Cross-sections/#マクロ断面積macroscopic-cross-section) 参照)、中性子がこの二種類の原子核と単位長さあたり反応する総確率は次のようになる。

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## 分子の等価断面積(Equivalent Cross-section)
上で検討した核が分子形態で存在する場合、式 ($\ref{eqn:cross_section_of_mixture}$)で求めた混合物の巨視的断面積を単位体積当たりの分子数で割ることによって、その分子の等価断面積(equivalent cross-section)を定義することができる。

単位体積当たり分子 $X_mY_n$が $N$個ある場合、$N_X=mN$、$N_Y=nN$となり、式 ($\ref{eqn:cross_section_of_mixture}$)からこの分子の断面積を次のように求めることができる。

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> 式 ($\ref{eqn:cross_section_of_mixture}$)と ($\ref{eqn:equivalent_cross_section}$)は核 $X$と $Y$が互いに独立して中性子と反応するという仮定の下で成立し、[弾性散乱](/posts/Neutron-Interactions-and-Cross-sections/#弾性散乱elastic-scattering)を除くすべての種類の中性子反応に対して有効である。
> 分子と固体による中性子の弾性散乱（特に低エネルギー領域）には上記の仮定を適用できないため、実験を通じて散乱断面積を調べる必要がある。
{: .prompt-warning }
