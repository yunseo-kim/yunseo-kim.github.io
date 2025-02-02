---
title: 中子衰減和平均自由程（Mean Free Path）
description: 計算單一能量中子束照射目標物時，中子束強度隨目標物穿透距離的變化，並由此推導中子的平均自由程。
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## 中子衰減（Neutron Attenuation）
假設我們將強度為 $I_0$ 的單一能量中子束照射到厚度為 $X$ 的目標物上，並在目標物後方的一定距離放置一個中子探測器。我們假設目標物和探測器都非常小，且探測器具有很小的立體角，只能探測到穿過目標物的部分中子。在這種情況下，所有與目標物發生碰撞的中子要麼被吸收，要麼被散射到其他方向，因此只有未與目標物發生反應的中子才能進入探測器。

讓我們用 $I(x)$ 表示中子束在目標物內行進距離 $x$ 後，未發生碰撞而保留下來的中子束強度。當中子束通過一個足夠薄的厚度為 $\tau$ 的目標物時，每單位面積的碰撞數為 $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$（參考[中子相互作用和反應截面](/posts/Neutron-Interactions-and-Cross-sections/#截面cross-section-或微觀截面microscopic-cross-section)中的公式 (1) 和 (4)）。因此，中子束在目標物內行進 $dx$ 距離時，其強度的減少量可表示為：

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

對上述方程進行積分，我們得到：

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

由此可見，中子束的強度隨著穿過目標物的距離增加而呈指數衰減。

## 平均自由程（Mean Free Path）
- 中子與一個原子核發生碰撞後，到下一次與另一個原子核發生碰撞之前的平均移動距離
- 即中子在不發生碰撞的情況下行進的平均距離
- 用符號 $\lambda$ 表示

$I(x)/I_0=e^{-\Sigma_t x}$ 表示中子在介質中行進距離 $x$ 而不與原子核發生碰撞的概率。因此，某個中子在介質中無碰撞地行進到距離 $x$，然後在 $dx$ 距離內發生碰撞的概率 $p(x)dx$ 可以表示為：

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

由此，我們可以計算出*平均自由程（mean free path）* $\lambda$ 如下：

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
