---
title: Atenuação de Nêutrons e Livre Caminho Médio (Mean Free Path)
description: Calcula-se a intensidade de um feixe de nêutrons de energia única quando
  irradiado em um alvo em função da distância de penetração no alvo, e a partir disso,
  deriva-se o livre caminho médio dos nêutrons.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## Atenuação de Nêutrons (Neutron Attenuation)
Um feixe de nêutrons de energia única com intensidade $I_0$ está sendo irradiado em um alvo de espessura $X$, e um detector de nêutrons está posicionado a uma certa distância atrás do alvo. Vamos assumir que tanto o alvo quanto o detector são muito pequenos, e que o detector tem um ângulo sólido pequeno que pode detectar apenas uma parte dos nêutrons que passam pelo alvo. Então, todos os nêutrons que colidem com o alvo serão absorvidos ou espalhados em outras direções, e apenas os nêutrons que não interagiram com o alvo incidirão no detector.

Vamos chamar de $I(x)$ a intensidade do feixe de nêutrons que permanece sem colidir após percorrer uma distância $x$ dentro do alvo. Quando o feixe de nêutrons passa por uma espessura suficientemente fina $\tau$ do alvo, o número de colisões por unidade de área é $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[nêutrons/cm}^2\cdot\text{s]}$ (consulte as equações (1) e (4) em [Interações de Nêutrons e Seções de Choque](/posts/Neutron-Interactions-and-Cross-sections/#seção-de-choque-cross-section-ou-seção-de-choque-microscópica-microscopic-cross-section)). Portanto, a diminuição na intensidade do feixe de nêutrons ao percorrer uma distância $dx$ dentro do alvo é dada por:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Integrando esta equação, obtemos o seguinte resultado:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Assim, podemos ver que a intensidade do feixe de nêutrons diminui exponencialmente à medida que a distância de penetração no alvo aumenta.

## Livre Caminho Médio (Mean Free Path)
- A distância média que um nêutron percorre após colidir com um núcleo até colidir com outro núcleo
- Ou seja, a distância média que um nêutron percorre sem colisões
- Representado pelo símbolo $\lambda$

$I(x)/I_0=e^{-\Sigma_t x}$ representa a probabilidade de um nêutron não colidir com um núcleo ao percorrer uma distância $x$ dentro do meio. Portanto, a probabilidade $p(x)dx$ de um nêutron percorrer uma distância $x$ sem colisões e então colidir dentro de uma distância $dx$ é dada por:

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
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
