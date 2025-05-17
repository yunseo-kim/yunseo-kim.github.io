---
title: Neutron Attenuation and Mean Free Path
description: Calculate the intensity of a neutron beam as it penetrates a target material, derive the mean free path of neutrons, and determine macroscopic cross-sections for homogeneous mixtures and molecules containing multiple nuclides.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---

## Neutron Attenuation
Consider a monoenergetic neutron beam with intensity $I_0$ irradiating a target of thickness $X$, with a neutron detector placed at some distance behind the target. Assume both the target and detector are very small, and the detector has a small solid angle that allows it to detect only a portion of the neutrons emerging from the target. All neutrons that collide with the target will either be absorbed or scattered away in different directions, so only neutrons that do not interact with the target will reach the detector.

Let $I(x)$ be the intensity of the neutron beam that remains uncollided after traveling a distance $x$ within the target. When neutrons pass through a thin target of thickness $\tau$, the number of collisions per unit area is $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (refer to equation [(1)](/posts/Neutron-Interactions-and-Cross-sections/#mjx-eqn:eqn:microscopic_cross_section) and [(8)](/posts/Neutron-Interactions-and-Cross-sections/#mjx-eqn:eqn:reaction_rate) in [Neutron Interactions and Cross-sections](/posts/Neutron-Interactions-and-Cross-sections/)). Therefore, the decrease in neutron beam intensity while traveling a distance $dx$ within the target is:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Integrating this equation yields:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

This shows that the neutron beam intensity decreases exponentially with distance traveled through the target.

## Mean Free Path
- The average distance a neutron travels between successive collisions with nuclei
- In other words, the average distance a neutron travels without collision
- Denoted by the symbol $\lambda$

The ratio $I(x)/I_0=e^{-\Sigma_t x}$ represents the probability that a neutron will travel a distance $x$ through the medium without colliding with any nuclei. Therefore, the probability $p(x)dx$ that a neutron travels a distance $x$ without collision and then collides within a distance $dx$ is:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

From this, we can calculate the *mean free path* $\lambda$ as follows:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## Macroscopic Cross-Section of a Homogeneous Mixture
Consider a homogeneous mixture containing two nuclides $X$ and $Y$ with atomic densities $N_X$ and $N_Y$ $\text{atom/cm}^3$, respectively. If the microscopic cross-sections for a specific neutron reaction with these nuclei are $\sigma_X$ and $\sigma_Y$, then:

The probabilities of neutron collision per unit path length with nuclei $X$ and $Y$ are $\Sigma_X=N_X\sigma_X$ and $\Sigma_Y=N_Y\sigma_Y$, respectively (see [Macroscopic Cross-section](/posts/Neutron-Interactions-and-Cross-sections/#macroscopic-cross-section)). Therefore, the total probability of neutron reaction per unit path length is:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## Equivalent Cross-Section of a Molecule
If the nuclei discussed above exist in molecular form, we can define an equivalent cross-section for the molecule by dividing the macroscopic cross-section of the mixture (calculated using equation ($\ref{eqn:cross_section_of_mixture}$)) by the number of molecules per unit volume.

If there are $N$ molecules of $X_mY_n$ per unit volume, then $N_X=mN$ and $N_Y=nN$. From equation ($\ref{eqn:cross_section_of_mixture}$), we can determine the equivalent cross-section of this molecule as:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> Equations ($\ref{eqn:cross_section_of_mixture}$) and ($\ref{eqn:equivalent_cross_section}$) are valid under the assumption that nuclei $X$ and $Y$ interact independently with neutrons. This assumption holds for all types of neutron reactions except for elastic scattering.
> For elastic scattering by molecules and solids (especially in the low-energy region), this assumption cannot be applied, and scattering cross-sections must be determined experimentally.
{: .prompt-warning }
