---
title: 中子衰減(Neutron Attenuation)與平均自由路徑(Mean Free Path)
description: 計算單一能量中子束照射目標物時，隨著穿透距離變化的中子束強度，並從中推導中子的平均自由路徑。
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---
## 中子衰減(Neutron Attenuation)
假設有強度為 $I_0$ 的單一能量中子束正照射在厚度為 $X$ 的目標物上，且在目標物後方的某處放置了一個中子探測器。假設目標物和探測器都非常小，且探測器具有很小的立體角，只能探測到穿過目標物的部分中子。在這種情況下，所有與目標物碰撞的中子都會被吸收或散射到其他方向，因此只有未與目標物發生反應的中子才會進入探測器。

讓我們用 $I(x)$ 表示中子束在目標物內部行進距離 $x$ 後，仍未發生碰撞的中子束強度。當中子束通過厚度為 $\tau$ 的薄目標物時，每單位面積的碰撞數為 $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$（參考[中子交互作用與反應截面](/posts/Neutron-Interactions-and-Cross-sections/#截面cross-section或微觀截面microscopic-cross-section)中的式 (1) 和 (4)），因此中子束在目標物內行進距離 $dx$ 時的強度減少量為：

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

對上式進行積分，可得：

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

因此，我們可以看出中子束的強度會隨著穿過目標物的距離增加而呈指數衰減。

## 平均自由路徑 (Mean Free Path)
- 中子與一個原子核碰撞後，到下一次與另一個原子核碰撞之前的平均移動距離
- 即中子在無碰撞情況下行進的平均距離
- 用符號 $\lambda$ 表示

$I(x)/I_0=e^{-\Sigma_t x}$ 表示中子在介質中行進距離 $x$ 而不與原子核碰撞的機率。因此，某個中子在介質中無碰撞地行進距離 $x$ 後，在距離 $dx$ 內發生碰撞的機率 $p(x)dx$ 為：

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

從這個機率分布，我們可以計算*平均自由路徑(mean free path)* $\lambda$ 如下：

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
