---
title: "Mistura Homogênea e Seção Transversal de Moléculas"
description: >-
  Vamos calcular a seção transversal macroscópica de uma mistura homogênea contendo dois ou mais nuclídeos.
categories: [Engenharia Física, Engenharia Nuclear]
tags: [Física Nuclear, Interação da Radiação com a Matéria]
math: true
---
## Seção Transversal Macroscópica de uma Mistura Homogênea

Considere uma mistura homogênea contendo dois nuclídeos, $X$ e $Y$. As densidades atômicas de cada nuclídeo são $N_X$ e $N_Y$ $\text{átomo/cm}^3$, respectivamente, e as seções transversais para uma reação específica de nêutrons com esses núcleos são $\sigma_X$ e $\sigma_Y$, respectivamente.

Então, as probabilidades de colisão de nêutrons por unidade de comprimento com os núcleos $X$ e $Y$ são $\Sigma_X=N_X\sigma_X$ e $\Sigma_Y=N_Y\sigma_Y$, respectivamente (consulte [Seção Transversal Macroscópica](/posts/Neutron-Interactions-and-Cross-sections/#seção-transversal-macroscópica)). A probabilidade total de um nêutron reagir com esses dois tipos de núcleos por unidade de comprimento é dada por:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## Seção Transversal Equivalente de Moléculas

Se os núcleos mencionados acima existirem na forma de moléculas, podemos definir a seção transversal equivalente dessa molécula dividindo a seção transversal macroscópica da mistura, calculada pela equação (1), pelo número de moléculas por unidade de volume.

Se houver $N$ moléculas de $X_mY_n$ por unidade de volume, então $N_X=mN$ e $N_Y=nN$, e podemos calcular a seção transversal dessa molécula a partir da equação (1) da seguinte forma:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> As equações (1) e (2) são válidas sob a suposição de que os núcleos $X$ e $Y$ reagem independentemente com os nêutrons, portanto, não podem ser aplicadas ao espalhamento elástico por moléculas e sólidos.
> As seções transversais de espalhamento para nêutrons de baixa energia por moléculas e sólidos devem ser determinadas experimentalmente.
{: .prompt-warning }