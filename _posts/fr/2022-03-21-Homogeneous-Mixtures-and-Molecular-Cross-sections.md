---
title: "Mélanges homogènes et sections efficaces moléculaires"
description: >-
  Calculons la section efficace macroscopique d'un mélange homogène contenant deux types de noyaux ou plus.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
---
## Section efficace macroscopique d'un mélange homogène (Homogeneous Mixture)
Considérons un mélange homogène de deux types de noyaux $X$ et $Y$. Les densités atomiques de chaque noyau sont respectivement $N_X$ et $N_Y$ $\text{atome/cm}^3$, et les sections efficaces pour une réaction spécifique avec les neutrons sont respectivement $\sigma_X$ et $\sigma_Y$. 

Alors, la probabilité de collision par unité de longueur d'un neutron avec les noyaux $X$ et $Y$ est respectivement $\Sigma_X=N_X\sigma_X$ et $\Sigma_Y=N_Y\sigma_Y$ (voir [Section efficace macroscopique](/posts/Neutron-Interactions-and-Cross-sections/#section-efficace-macroscopique-macroscopic-cross-section)). La probabilité totale de réaction d'un neutron avec ces deux types de noyaux par unité de longueur est donc :

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## Section efficace équivalente d'une molécule (Equivalent Cross-section)
Si les noyaux examinés ci-dessus existent sous forme moléculaire, nous pouvons définir la section efficace équivalente de cette molécule en divisant la section efficace macroscopique du mélange calculée par l'équation (1) par le nombre de molécules par unité de volume.

S'il y a $N$ molécules $X_mY_n$ par unité de volume, alors $N_X=mN$, $N_Y=nN$, et à partir de l'équation (1), nous pouvons calculer la section efficace de cette molécule comme suit :

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> Les équations (1) et (2) sont valables sous l'hypothèse que les noyaux $X$ et $Y$ réagissent indépendamment avec les neutrons, donc elles ne peuvent pas être appliquées à la diffusion élastique par des molécules et des solides.
> Les sections efficaces de diffusion pour les neutrons de faible énergie par des molécules et des solides doivent être déterminées expérimentalement.
{: .prompt-warning }