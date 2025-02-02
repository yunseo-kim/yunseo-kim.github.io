---
title: 均勻混合物與分子的截面積
description: 讓我們計算含有兩種或更多核種的均勻混合物的巨觀截面積。
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## 均勻混合物（Homogeneous Mixture）的巨觀截面積
讓我們考慮一個由兩種核種 $X$ 和 $Y$ 均勻混合的混合物。假設每種核種的原子密度分別為 $N_X$ 和 $N_Y$ $\text{atom/cm}^3$，而中子與這些核的特定反應的反應截面積分別為 $\sigma_X$ 和 $\sigma_Y$。

那麼，中子與原子核 $X$ 和 $Y$ 每單位長度發生碰撞的機率分別為 $\Sigma_X=N_X\sigma_X$ 和 $\Sigma_Y=N_Y\sigma_Y$（參考[巨觀截面積](/posts/Neutron-Interactions-and-Cross-sections/#巨觀截面積macroscopic-cross-section)）。因此，中子與這兩種原子核每單位長度發生反應的總機率如下：

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## 分子的等效截面積（Equivalent Cross-section）
如果上述核以分子形式存在，我們可以通過將混合物的巨觀截面積（由公式（1）計算得出）除以單位體積內的分子數，來定義該分子的等效截面積。

假設單位體積內有 $N$ 個分子 $X_mY_n$，則 $N_X=mN$，$N_Y=nN$。根據公式（1），我們可以計算出這個分子的截面積如下：

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> 公式（1）和（2）是基於核 $X$ 和 $Y$ 獨立地與中子反應的假設而成立的，因此不適用於分子和固體的彈性散射。
> 分子和固體在低中子能量下的散射截面積必須通過實驗來確定。
{: .prompt-warning }
