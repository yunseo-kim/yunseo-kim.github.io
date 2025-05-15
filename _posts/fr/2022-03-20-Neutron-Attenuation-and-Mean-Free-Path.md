---
title: Atténuation des neutrons (Neutron Attenuation) et libre parcours moyen (Mean Free Path)
description: Calcul de l'intensité d'un faisceau de neutrons monoénergétique en fonction de la distance de pénétration dans une cible, et dérivation du libre parcours moyen des neutrons.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---
## Atténuation des neutrons (Neutron Attenuation)
Supposons qu'un faisceau de neutrons monoénergétique d'intensité $I_0$ soit dirigé vers une cible d'épaisseur $X$, avec un détecteur de neutrons placé à une certaine distance derrière la cible. Supposons que la cible et le détecteur sont tous deux très petits, et que le détecteur ne couvre qu'un angle solide réduit, ne lui permettant de détecter qu'une partie des neutrons traversant la cible. Dans ce cas, tous les neutrons qui entrent en collision avec la cible seront soit absorbés, soit diffusés dans d'autres directions, et seuls les neutrons n'ayant pas interagi avec la cible atteindront le détecteur.

Soit $I(x)$ l'intensité du faisceau de neutrons qui reste après avoir parcouru une distance $x$ dans la cible sans collision. Lorsqu'un faisceau de neutrons traverse une cible d'épaisseur très fine $\tau$, le nombre de collisions par unité de surface est $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (voir équations (1) et (4) dans [Interactions des neutrons et sections efficaces](/posts/Neutron-Interactions-and-Cross-sections/#section-efficace-cross-section-ou-section-efficace-microscopique-microscopic-cross-section)). Par conséquent, la diminution de l'intensité du faisceau de neutrons lors de la traversée d'une distance $dx$ dans la cible est donnée par :

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

En intégrant cette équation, on obtient :

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

On constate donc que l'intensité du faisceau de neutrons diminue exponentiellement avec la distance parcourue dans la cible.

## Libre parcours moyen (Mean Free Path)
- Distance moyenne parcourue par un neutron entre deux collisions successives avec des noyaux
- C'est-à-dire la distance moyenne qu'un neutron parcourt sans collision
- Noté par le symbole $\lambda$

Le rapport $I(x)/I_0=e^{-\Sigma_t x}$ représente la probabilité qu'un neutron parcoure une distance $x$ dans le milieu sans subir de collision. Par conséquent, la probabilité $p(x)dx$ qu'un neutron parcoure une distance $x$ sans collision puis subisse une collision dans l'intervalle $dx$ est donnée par :

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

À partir de cette expression, on peut calculer le *libre parcours moyen (mean free path)* $\lambda$ comme suit :

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
