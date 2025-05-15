---
title: Atenuación de neutrones (Neutron Attenuation) y camino libre medio (Mean Free Path)
description: Calculamos la intensidad del haz de neutrones en función de la distancia de penetración al irradiar un objetivo con un haz de neutrones monoenergético, y derivamos el camino libre medio de los neutrones.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---
## Atenuación de neutrones (Neutron Attenuation)
Un haz de neutrones monoenergético de intensidad $I_0$ está irradiando un objetivo de espesor $X$, y a cierta distancia detrás del objetivo se encuentra un detector de neutrones. Supongamos que tanto el objetivo como el detector son muy pequeños, y que el detector tiene un ángulo sólido pequeño que solo puede detectar una parte de los neutrones que salen del objetivo. Entonces, todos los neutrones que colisionan con el objetivo serán absorbidos o dispersados en otras direcciones, por lo que solo los neutrones que no interactúan con el objetivo incidirán en el detector.

Sea $I(x)$ la intensidad del haz de neutrones que permanece sin colisionar después de recorrer una distancia $x$ dentro del objetivo. Cuando el haz de neutrones atraviesa un objetivo de espesor muy delgado $\tau$, el número de colisiones por unidad de área es $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (consultar ecuaciones (1) y (4) en [Interacciones de neutrones y secciones eficaces](/posts/Neutron-Interactions-and-Cross-sections/#sección-eficazcross-section-o-sección-eficaz-microscópicamicroscopic-cross-section)), por lo que la disminución en la intensidad del haz de neutrones al avanzar una distancia $dx$ dentro del objetivo es:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Integrando esta ecuación, obtenemos el siguiente resultado:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Por lo tanto, podemos ver que la intensidad del haz de neutrones disminuye exponencialmente a medida que aumenta la distancia de penetración en el objetivo.

## Camino libre medio (Mean Free Path)
- La distancia media que recorre un neutrón después de colisionar con un núcleo hasta colisionar con otro núcleo
- Es decir, la distancia media que recorre un neutrón sin colisiones
- Se denota con el símbolo $\lambda$

$I(x)/I_0=e^{-\Sigma_t x}$ representa la probabilidad de que un neutrón viaje una distancia $x$ dentro del medio sin colisionar con ningún núcleo. Por lo tanto, la probabilidad $p(x)dx$ de que un neutrón viaje sin colisiones hasta una distancia $x$ y luego colisione dentro de una distancia $dx$ es:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

A partir de esto, podemos calcular el *camino libre medio (mean free path)* $\lambda$ de la siguiente manera:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
