---
title: Atenuación de neutrones (Neutron Attenuation) y camino libre medio (Mean Free Path)
description: Calculamos la intensidad de un haz de neutrones monoenergético al atravesar un material en función de la distancia de penetración, derivamos el camino libre medio de los neutrones, y analizamos cómo calcular la sección eficaz macroscópica para mezclas homogéneas y moléculas.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---

## Atenuación de neutrones (Neutron Attenuation)
Consideremos un haz de neutrones monoenergético de intensidad $I_0$ que incide sobre un blanco de espesor $X$, con un detector de neutrones colocado a cierta distancia detrás del blanco. Supongamos que tanto el blanco como el detector son muy pequeños, y que el detector tiene un ángulo sólido pequeño que le permite detectar solo una parte de los neutrones que salen del blanco. Entonces, todos los neutrones que colisionan con el blanco serán absorbidos o dispersados en otras direcciones, por lo que solo los neutrones que no interactúan con el blanco llegarán al detector.

Sea $I(x)$ la intensidad del haz de neutrones que permanece sin colisionar después de recorrer una distancia $x$ dentro del blanco. Cuando el haz de neutrones atraviesa un espesor muy delgado $\tau$ del blanco, el número de colisiones por unidad de área es $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (ver ecuación [(1)](/posts/Neutron-Interactions-and-Cross-sections/#sección-eficaz-cross-section-o-sección-eficaz-microscópica-microscopic-cross-section) y [(8)](/posts/Neutron-Interactions-and-Cross-sections/#densidad-de-colisión-collision-density-es-decir-tasa-de-reacción-reaction-rate) en [Interacciones de neutrones y sección eficaz](/posts/Neutron-Interactions-and-Cross-sections/)). Por lo tanto, la disminución en la intensidad del haz de neutrones al recorrer una distancia $dx$ dentro del blanco es:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Integrando esta ecuación, obtenemos:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Por lo tanto, la intensidad del haz de neutrones disminuye exponencialmente con la distancia recorrida dentro del blanco.

## Camino libre medio (Mean Free Path)
- La distancia promedio que un neutrón recorre entre colisiones sucesivas con núcleos
- Es decir, la distancia promedio que un neutrón viaja sin colisionar
- Se denota con el símbolo $\lambda$

La relación $I(x)/I_0=e^{-\Sigma_t x}$ representa la probabilidad de que un neutrón recorra una distancia $x$ dentro del material sin colisionar con ningún núcleo. Por lo tanto, la probabilidad $p(x)dx$ de que un neutrón recorra una distancia $x$ sin colisionar y luego colisione dentro de un intervalo $dx$ es:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

A partir de esto, podemos calcular el *camino libre medio (mean free path)* $\lambda$ como:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## Sección eficaz macroscópica de una mezcla homogénea (Homogeneous Mixture)
Consideremos una mezcla homogénea de dos tipos de núcleos $X$ e $Y$. Si las densidades atómicas son $N_X$ y $N_Y$ $\text{atom/cm}^3$ respectivamente, y las secciones eficaces para una reacción específica con neutrones son $\sigma_X$ y $\sigma_Y$, entonces:

La probabilidad de colisión por unidad de longitud para los núcleos $X$ e $Y$ son $\Sigma_X=N_X\sigma_X$ y $\Sigma_Y=N_Y\sigma_Y$ respectivamente (ver [sección eficaz macroscópica](/posts/Neutron-Interactions-and-Cross-sections/#sección-eficaz-macroscópica-macroscopic-cross-section)). Por lo tanto, la probabilidad total de colisión por unidad de longitud es:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## Sección eficaz equivalente (Equivalent Cross-section) de una molécula
Si los núcleos mencionados anteriormente existen en forma molecular, podemos definir la sección eficaz equivalente (equivalent cross-section) de la molécula dividiendo la sección eficaz macroscópica de la mezcla por el número de moléculas por unidad de volumen.

Si hay $N$ moléculas de $X_mY_n$ por unidad de volumen, entonces $N_X=mN$ y $N_Y=nN$. A partir de la ecuación ($\ref{eqn:cross_section_of_mixture}$), podemos calcular la sección eficaz de esta molécula como:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> Las ecuaciones ($\ref{eqn:cross_section_of_mixture}$) y ($\ref{eqn:equivalent_cross_section}$) son válidas bajo la suposición de que los núcleos $X$ e $Y$ interactúan independientemente con los neutrones, y son aplicables a todos los tipos de reacciones neutrónicas excepto la [dispersión elástica](/posts/Neutron-Interactions-and-Cross-sections/#dispersión-elástica-elastic-scattering).
> Para la dispersión elástica de neutrones por moléculas y sólidos (especialmente en el rango de baja energía), esta suposición no es válida, y la sección eficaz de dispersión debe determinarse experimentalmente.
{: .prompt-warning }
