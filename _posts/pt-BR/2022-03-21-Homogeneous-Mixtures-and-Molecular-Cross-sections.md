---
title: Mistura Homogênea e Seção de Choque de Moléculas
description: Vamos calcular a seção de choque macroscópica de uma mistura homogênea
  contendo dois ou mais nuclídeos.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## Seção de Choque Macroscópica de uma Mistura Homogênea
Considere uma mistura homogênea contendo dois nuclídeos, $X$ e $Y$. As densidades atômicas de cada nuclídeo são $N_X$ e $N_Y$ $\text{átomo/cm}^3$, respectivamente, e as seções de choque para uma reação específica de nêutrons com esses núcleos são $\sigma_X$ e $\sigma_Y$, respectivamente.

Então, as probabilidades de colisão por unidade de comprimento de um nêutron com os núcleos $X$ e $Y$ são $\Sigma_X=N_X\sigma_X$ e $\Sigma_Y=N_Y\sigma_Y$, respectivamente (consulte [Seção de Choque Macroscópica](/posts/Neutron-Interactions-and-Cross-sections/#seção-de-choque-macroscópica-macroscopic-cross-section)). A probabilidade total de um nêutron reagir com esses dois tipos de núcleos por unidade de comprimento é dada por:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## Seção de Choque Equivalente de Moléculas
Se os núcleos mencionados acima existirem na forma de moléculas, podemos definir a seção de choque equivalente (equivalent cross-section) dessa molécula dividindo a seção de choque macroscópica da mistura, calculada pela equação (1), pelo número de moléculas por unidade de volume.

Se houver $N$ moléculas de $X_mY_n$ por unidade de volume, então $N_X=mN$ e $N_Y=nN$, e podemos calcular a seção de choque dessa molécula a partir da equação (1) da seguinte forma:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> As equações (1) e (2) são válidas sob a suposição de que os núcleos $X$ e $Y$ reagem independentemente com os nêutrons, portanto, não podem ser aplicadas ao espalhamento elástico por moléculas e sólidos.
> As seções de choque de espalhamento para nêutrons de baixa energia por moléculas e sólidos devem ser determinadas experimentalmente.
{: .prompt-warning }
