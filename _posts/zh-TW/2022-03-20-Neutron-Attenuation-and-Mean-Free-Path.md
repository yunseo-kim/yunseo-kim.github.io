---
title: 中子衰減(Neutron Attenuation)與平均自由路徑(Mean Free Path)
description: 計算單一能量中子束照射目標物時隨穿透距離的強度變化，並由此推導中子平均自由路徑。同時說明如何計算混合物與分子的巨觀截面。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
redirect_from:
  - /posts/Homogeneous-Mixtures-and-Molecular-Cross-sections/
---

## 中子衰減(Neutron Attenuation)
強度為 $I_0$ 的單一能量中子束正照射在厚度為 $X$ 的目標物上，目標物後方一定距離處放置了中子探測器。假設目標物和探測器都非常小，且探測器具有很小的立體角，只能探測到穿過目標物的部分中子。在這種情況下，所有與目標物碰撞的中子都會被吸收或散射到其他方向，只有未與目標物發生反應的中子才會進入探測器。

假設中子束在目標物內部行進距離 $x$ 後，未發生碰撞而保留下來的中子束強度為 $I(x)$。當中子束通過厚度為 $\tau$ 的薄目標物時，每單位面積的碰撞數為 $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$（參考[中子交互作用與反應截面](/posts/Neutron-Interactions-and-Cross-sections/)中的式 [(1)](/posts/Neutron-Interactions-and-Cross-sections/#截面cross-section或微觀截面microscopic-cross-section)和 [(8)](/posts/Neutron-Interactions-and-Cross-sections/#碰撞密度collision-density即反應率reaction-rate)），因此中子束在目標物內行進距離 $dx$ 時，強度的減少量為：

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

對上式進行積分，得到：

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

由此可知，中子束的強度隨著穿過目標物的距離增加而呈指數衰減。

## 平均自由路徑 (Mean Free Path)
- 中子與一個原子核碰撞後，到下一次與另一個原子核碰撞之前的平均移動距離
- 即中子無碰撞前進的平均距離
- 用符號 $\lambda$ 表示

$I(x)/I_0=e^{-\Sigma_t x}$ 表示中子在介質中行進距離 $x$ 而不與原子核碰撞的機率。因此，中子在介質中無碰撞行進距離 $x$ 後，在距離 $dx$ 內發生碰撞的機率 $p(x)dx$ 為：

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

由此可計算*平均自由路徑(mean free path)* $\lambda$：

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## 均勻混合物(Homogeneous Mixture)的巨觀截面
考慮兩種核種 $X$ 和 $Y$ 均勻混合的混合物。假設這兩種核種的原子密度分別為 $N_X$ 和 $N_Y$ $\text{atom/cm}^3$，中子與這些核種發生特定反應的反應截面分別為 $\sigma_X$ 和 $\sigma_Y$。

中子與原子核 $X$、$Y$ 每單位長度的碰撞機率分別為 $\Sigma_X=N_X\sigma_X$ 和 $\Sigma_Y=N_Y\sigma_Y$（參考[巨觀截面](/posts/Neutron-Interactions-and-Cross-sections/#宏觀截面macroscopic-cross-section)），因此中子與這兩種原子核每單位長度的總反應機率為：

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## 分子的等效截面(Equivalent Cross-section)
若上述核種以分子形式存在，可以通過將混合物的巨觀截面除以單位體積內的分子數，來定義該分子的等效截面(equivalent cross-section)。

若單位體積內有 $N$ 個分子 $X_mY_n$，則 $N_X=mN$、$N_Y=nN$，由式 ($\ref{eqn:cross_section_of_mixture}$) 可得該分子的截面為：

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> 式 ($\ref{eqn:cross_section_of_mixture}$) 和 ($\ref{eqn:equivalent_cross_section}$) 是基於核種 $X$ 和 $Y$ 獨立與中子反應的假設，適用於除[彈性散射](/posts/Neutron-Interactions-and-Cross-sections/#彈性散射elastic-scattering)外的所有類型的中子反應。
> 對於分子和固體引起的中子彈性散射（特別是低能區），上述假設不適用，需要通過實驗測定散射截面。
{: .prompt-warning }
