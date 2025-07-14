---
title: Atténuation des neutrons (Neutron Attenuation) et libre parcours moyen (Mean Free Path)
description: Calcul de l'intensité d'un faisceau de neutrons monoénergétique en fonction de la distance traversée dans une cible, dérivation du libre parcours moyen des neutrons, et détermination des sections efficaces macroscopiques pour les mélanges homogènes et les molécules.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
redirect_from:
  - /posts/Homogeneous-Mixtures-and-Molecular-Cross-sections/
---

## Atténuation des neutrons (Neutron Attenuation)
Un faisceau de neutrons d'intensité $I_0$ et d'énergie unique est dirigé sur une cible d'épaisseur $X$, avec un détecteur de neutrons placé à une certaine distance derrière la cible. Supposons que la cible et le détecteur soient tous deux très petits, et que le détecteur ne couvre qu'un angle solide réduit, ne pouvant détecter qu'une partie des neutrons sortant de la cible. Dans ces conditions, tous les neutrons qui entrent en collision avec la cible seront soit absorbés, soit diffusés dans d'autres directions, et seuls les neutrons n'ayant pas interagi avec la cible atteindront le détecteur.

Soit $I(x)$ l'intensité du faisceau de neutrons après avoir parcouru une distance $x$ dans la cible sans collision. Lorsque le faisceau de neutrons traverse une fine couche de cible d'épaisseur $\tau$, le nombre de collisions par unité de surface est $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (voir l'équation [(1)](/posts/Neutron-Interactions-and-Cross-sections/#section-efficace-cross-section-ou-section-efficace-microscopique-microscopic-cross-section) et [(8)](/posts/Neutron-Interactions-and-Cross-sections/#densité-de-collision-collision-density-ou-taux-de-réaction-reaction-rate) dans l'article sur les interactions des neutrons et les sections efficaces). Par conséquent, la diminution de l'intensité du faisceau sur une distance $dx$ est donnée par :

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

En intégrant cette équation, on obtient :

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

On constate donc que l'intensité du faisceau de neutrons diminue exponentiellement avec la distance parcourue dans la cible.

## Libre parcours moyen (Mean Free Path)
- Distance moyenne parcourue par un neutron entre deux collisions successives avec des noyaux
- Représente la distance moyenne qu'un neutron parcourt sans collision
- Noté par le symbole $\lambda$

Le rapport $I(x)/I_0=e^{-\Sigma_t x}$ représente la probabilité qu'un neutron traverse une distance $x$ dans le milieu sans subir de collision. Par conséquent, la probabilité qu'un neutron parcoure une distance $x$ sans collision puis subisse une collision dans l'intervalle $dx$ est donnée par $p(x)dx$ :

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

À partir de cette expression, on peut calculer le *libre parcours moyen (mean free path)* $\lambda$ :

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## Section efficace macroscopique d'un mélange homogène (Homogeneous Mixture)
Considérons un mélange homogène de deux nucléides $X$ et $Y$. Si les densités atomiques sont respectivement $N_X$ et $N_Y$ $\text{atom/cm}^3$, et que les sections efficaces pour une réaction particulière sont $\sigma_X$ et $\sigma_Y$, alors :

La probabilité de collision par unité de longueur pour chaque nucléide est $\Sigma_X=N_X\sigma_X$ et $\Sigma_Y=N_Y\sigma_Y$ (voir la section sur la [section efficace macroscopique](/posts/Neutron-Interactions-and-Cross-sections/#section-efficace-macroscopique-macroscopic-cross-section)). La probabilité totale de collision par unité de longueur est donc :

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## Section efficace équivalente d'une molécule (Equivalent Cross-section)
Si les nucléides considérés ci-dessus font partie d'une molécule, on peut définir une section efficace équivalente (equivalent cross-section) pour cette molécule en divisant la section efficace macroscopique du mélange par le nombre de molécules par unité de volume.

Si une molécule $X_mY_n$ est présente à raison de $N$ molécules par unité de volume, alors $N_X=mN$ et $N_Y=nN$. À partir de l'équation ($\ref{eqn:cross_section_of_mixture}$), on peut calculer la section efficace de cette molécule :

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> Les équations ($\ref{eqn:cross_section_of_mixture}$) et ($\ref{eqn:equivalent_cross_section}$) sont valables sous l'hypothèse que les nucléides $X$ et $Y$ interagissent indépendamment avec les neutrons. Cette hypothèse est valide pour tous les types d'interactions neutroniques, à l'exception de la [diffusion élastique](/posts/Neutron-Interactions-and-Cross-sections/#diffusion-élastique-elastic-scattering).
> Pour la diffusion élastique des neutrons par des molécules et des solides (particulièrement à basse énergie), cette hypothèse n'est pas applicable, et les sections efficaces de diffusion doivent être déterminées expérimentalement.
{: .prompt-warning }
