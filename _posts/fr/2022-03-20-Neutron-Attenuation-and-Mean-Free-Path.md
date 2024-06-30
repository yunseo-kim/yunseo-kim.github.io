---
title: "Atténuation des neutrons et libre parcours moyen"
description: >-
  Calcul de l'intensité d'un faisceau de neutrons monoénergétique en fonction de la distance de pénétration dans une cible, et dérivation du libre parcours moyen des neutrons à partir de ces résultats.
categories: [Physique de l'ingénieur, Génie nucléaire]
tags: [Physique nucléaire, Interaction du rayonnement avec la matière]
math: true
---

## Atténuation des neutrons (Neutron Attenuation)
Un faisceau de neutrons monoénergétique d'intensité $I_0$ est irradié sur une cible d'épaisseur $X$, et un détecteur de neutrons est placé à une certaine distance derrière la cible. Supposons que la cible et le détecteur soient tous deux très petits, et que le détecteur n'ait qu'un petit angle solide capable de détecter seulement une partie des neutrons traversant la cible. Ainsi, tous les neutrons entrant en collision avec la cible seront soit absorbés, soit diffusés dans d'autres directions, et seuls les neutrons n'ayant pas interagi avec la cible atteindront le détecteur.

Soit $I(x)$ l'intensité du faisceau de neutrons restant sans collision après avoir parcouru une distance $x$ dans la cible. Lorsque le faisceau de neutrons traverse une cible d'épaisseur suffisamment fine $\tau$, le nombre de collisions par unité de surface est $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (voir les équations (1) et (4) dans [Interactions des neutrons et sections efficaces](/posts/Neutron-Interactions-and-Cross-sections/#section-efficacecross-section-ou-section-efficace-microscopiquemicroscopic-cross-section)). Par conséquent, la diminution de l'intensité du faisceau de neutrons lors de la progression de $dx$ dans la cible est donnée par :

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

En intégrant cette équation, on obtient le résultat suivant :

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

On peut donc constater que l'intensité du faisceau de neutrons diminue exponentiellement avec la distance parcourue dans la cible.

## Libre parcours moyen (Mean Free Path)
- Distance moyenne parcourue par un neutron entre deux collisions successives avec des noyaux
- C'est-à-dire la distance moyenne parcourue par un neutron sans collision
- Noté par le symbole $\lambda$

$I(x)/I_0=e^{-\Sigma_t x}$ représente la probabilité qu'un neutron ne subisse pas de collision en parcourant une distance $x$ dans le milieu. Par conséquent, la probabilité $p(x)dx$ qu'un neutron parcoure une distance $x$ sans collision dans le milieu, puis entre en collision dans l'intervalle $dx$, est donnée par :

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

À partir de cela, on peut calculer le *libre parcours moyen* $\lambda$ comme suit :

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$