---
title: "中性子減衰と平均自由行程（Mean Free Path）"
description: >-
  単一エネルギーの中性子ビームを標的に照射した際の、標的透過距離に応じた中性子ビームの強度を計算し、これから中性子の平均自由行程を導出する。
categories: [工学物理学, 原子力工学]
tags: [原子核物理学, 放射線と物質の相互作用]
math: true
---

## 中性子減衰（Neutron Attenuation）
強度 $I_0$ の単一エネルギー中性子ビームを厚さ $X$ の標的に照射しており、標的の後方にある程度離れた距離に中性子検出器が置かれている。標的と検出器は両方とも非常に小さく、検出器は標的を通過して出てくる中性子の一部のみを検出できる小さな立体角を持つと仮定しよう。そうすると、標的に衝突するすべての中性子は吸収されるか散乱されて別の方向に逸脱するため、標的と反応しなかった中性子のみが検出器に入射する。

標的内で距離 $x$ だけ進行する間に衝突せずに残っている中性子ビームの強度を $I(x)$ とする。中性子ビームが十分に薄い厚さ $\tau$ の標的を通過する際、単位面積当たりの衝突数は $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$（[中性子相互作用と反応断面積](/posts/Neutron-Interactions-and-Cross-sections/#断面積cross-section-または微視的断面積microscopic-cross-section)の式（1）と（4）参照）であるため、標的内で $dx$ だけ進行する間の中性子ビーム強度の減少量は次のようになる。

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

上記の式を積分すると、次のような結果が得られる。

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

したがって、中性子ビームの強度は標的透過距離が長くなるにつれて指数関数的に減少することがわかる。

## 平均自由行程（Mean Free Path）
- 中性子が原子核と1回衝突した後、続いて別の原子核と衝突するまでの平均移動距離
- つまり、中性子が衝突なしで進行する平均距離
- 記号 $\lambda$ で表記

$I(x)/I_0=e^{-\Sigma_t x}$ は中性子が媒質内で距離 $x$ だけ進行する間に原子核と衝突しない確率を意味する。したがって、ある中性子が媒質内で距離 $x$ まで衝突なしで進行した後、距離 $dx$ 以内に衝突する確率 $p(x)dx$ は次のようになる。

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

これから*平均自由行程（mean free path）* $\lambda$ を次のように求めることができる。

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$