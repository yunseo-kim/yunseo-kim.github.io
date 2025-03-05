---
title: Atténuation des neutrons et libre parcours moyen (Mean Free Path)
description: Calcul de l'intensité d'un faisceau de neutrons mono-énergétique lors
  de sa pénétration dans une cible, et déduction du libre parcours moyen des neutrons.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## Atténuation des neutrons (Neutron Attenuation)
Un faisceau de neutrons mono-énergétique d'intensité $I_0$ est irradié sur une cible d'épaisseur $X$, et un détecteur de neutrons est placé à une certaine distance derrière la cible. Supposons que la cible et le détecteur soient tous deux très petits, et que le détecteur ait un angle solide suffisamment petit pour ne détecter qu'une partie des neutrons traversant la cible. Ainsi, tous les neutrons entrant en collision avec la cible seront soit absorbés, soit diffusés dans une autre direction, et seuls les neutrons n'ayant pas interagi avec la cible atteindront le détecteur.

Soit $I(x)$ l'intensité du faisceau de neutrons restant après avoir parcouru une distance $x$ dans la cible sans collision. Lorsque le faisceau de neutrons traverse une cible d'épaisseur $\tau$ suffisamment fine, le nombre de collisions par unité de surface est $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (voir les équations (1) et (4) dans [Interactions des neutrons et sections efficaces](/posts/Neutron-Interactions-and-Cross-sections/#section-efficace-cross-section-ou-section-efficace-microscopique-microscopic-cross-section)). Par conséquent, la diminution de l'intensité du faisceau de neutrons lors de sa progression sur une distance $dx$ dans la cible est donnée par :

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

En intégrant cette équation, on obtient le résultat suivant :

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

On constate donc que l'intensité du faisceau de neutrons diminue exponentiellement avec la distance parcourue dans la cible.

## Libre parcours moyen (Mean Free Path)
- Distance moyenne parcourue par un neutron entre deux collisions successives avec des noyaux
- C'est-à-dire la distance moyenne parcourue par un neutron sans collision
- Noté par le symbole $\lambda$

$I(x)/I_0=e^{-\Sigma_t x}$ représente la probabilité qu'un neutron ne subisse pas de collision en parcourant une distance $x$ dans le milieu. Par conséquent, la probabilité $p(x)dx$ qu'un neutron parcoure une distance $x$ sans collision dans le milieu, puis entre en collision dans un intervalle $dx$, est donnée par :

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

À partir de cela, on peut calculer le *libre parcours moyen (mean free path)* $\lambda$ comme suit :

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
