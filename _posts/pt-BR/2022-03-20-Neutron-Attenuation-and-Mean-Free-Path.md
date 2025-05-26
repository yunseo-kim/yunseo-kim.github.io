---
title: Atenuação de Nêutrons (Neutron Attenuation) e Livre Caminho Médio (Mean Free Path)
description: Calculamos a intensidade de um feixe de nêutrons monoenergético ao atravessar um alvo em função da distância percorrida, e derivamos o livre caminho médio dos nêutrons. Também analisamos como calcular a seção de choque macroscópica de misturas homogêneas e a seção de choque equivalente de moléculas.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---

## Atenuação de Nêutrons (Neutron Attenuation)
Um feixe de nêutrons monoenergético com intensidade $I_0$ está sendo irradiado em um alvo de espessura $X$, e um detector de nêutrons está posicionado a uma certa distância atrás do alvo. Vamos supor que tanto o alvo quanto o detector são muito pequenos, e que o detector possui um ângulo sólido pequeno, capaz de detectar apenas uma parte dos nêutrons que saem do alvo. Nesse caso, todos os nêutrons que colidem com o alvo serão absorvidos ou espalhados em outras direções, e apenas os nêutrons que não interagiram com o alvo chegarão ao detector.

Seja $I(x)$ a intensidade do feixe de nêutrons que permanece sem colisões após percorrer uma distância $x$ dentro do alvo. Quando o feixe de nêutrons atravessa uma espessura muito fina $\tau$ do alvo, o número de colisões por unidade de área é $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (conforme a equação [(1)](/posts/Neutron-Interactions-and-Cross-sections/#seção-de-choque-cross-section-ou-seção-de-choque-microscópica-microscopic-cross-section) e [(8)](/posts/Neutron-Interactions-and-Cross-sections/#densidade-de-colisão-collision-density-ou-taxa-de-reação-reaction-rate) em [Interações de Nêutrons e Seção de Choque](/posts/Neutron-Interactions-and-Cross-sections/)). Portanto, a diminuição na intensidade do feixe de nêutrons ao percorrer uma distância $dx$ dentro do alvo é:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Integrando esta equação, obtemos:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Assim, podemos concluir que a intensidade do feixe de nêutrons diminui exponencialmente com a distância percorrida no alvo.

## Livre Caminho Médio (Mean Free Path)
- A distância média que um nêutron percorre entre colisões sucessivas com núcleos
- Ou seja, a distância média que um nêutron viaja sem sofrer colisões
- Representado pelo símbolo $\lambda$

A razão $I(x)/I_0=e^{-\Sigma_t x}$ representa a probabilidade de um nêutron percorrer uma distância $x$ dentro do meio sem colidir com nenhum núcleo. Portanto, a probabilidade $p(x)dx$ de um nêutron percorrer uma distância $x$ sem colisões e então colidir dentro de uma distância $dx$ é:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

A partir disso, podemos calcular o *livre caminho médio (mean free path)* $\lambda$ da seguinte forma:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## Seção de Choque Macroscópica de Misturas Homogêneas (Homogeneous Mixture)
Consideremos uma mistura homogênea de dois tipos de núcleos, $X$ e $Y$. As densidades atômicas desses núcleos são $N_X$ e $N_Y$ $\text{atom/cm}^3$, respectivamente, e as seções de choque para uma determinada reação com nêutrons são $\sigma_X$ e $\sigma_Y$.

A probabilidade de um nêutron colidir com núcleos $X$ ou $Y$ por unidade de comprimento percorrido é $\Sigma_X=N_X\sigma_X$ e $\Sigma_Y=N_Y\sigma_Y$, respectivamente (conforme [Seção de Choque Macroscópica](/posts/Neutron-Interactions-and-Cross-sections/#seção-de-choque-macroscópica-macroscopic-cross-section)). Portanto, a probabilidade total de um nêutron reagir com qualquer um desses núcleos por unidade de comprimento é:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## Seção de Choque Equivalente de Moléculas (Equivalent Cross-section)
Se os núcleos mencionados acima existirem na forma de moléculas, podemos definir a seção de choque equivalente (equivalent cross-section) da molécula dividindo a seção de choque macroscópica da mistura, calculada pela equação ($\ref{eqn:cross_section_of_mixture}$), pelo número de moléculas por unidade de volume.

Se houver $N$ moléculas de $X_mY_n$ por unidade de volume, então $N_X=mN$ e $N_Y=nN$. A partir da equação ($\ref{eqn:cross_section_of_mixture}$), podemos calcular a seção de choque desta molécula como:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> As equações ($\ref{eqn:cross_section_of_mixture}$) e ($\ref{eqn:equivalent_cross_section}$) são válidas sob a suposição de que os núcleos $X$ e $Y$ interagem independentemente com os nêutrons, e são aplicáveis a todos os tipos de reações de nêutrons, exceto o [espalhamento elástico](/posts/Neutron-Interactions-and-Cross-sections/#espalhamento-elástico-elastic-scattering).
> Para o espalhamento elástico de nêutrons por moléculas e sólidos (especialmente em baixas energias), esta suposição não é válida, e a seção de choque de espalhamento deve ser determinada experimentalmente.
{: .prompt-warning }
