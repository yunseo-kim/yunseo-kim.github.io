---
title: Neutron Attenuation and Mean Free Path
description: Calculating the intensity of a neutron beam as it passes through a target material based on penetration distance, and deriving the mean free path of neutrons from this relationship.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
---
## Neutron Attenuation
Consider a monoenergetic neutron beam with intensity $I_0$ irradiating a target with thickness $X$, with a neutron detector placed at some distance behind the target. Let's assume that both the target and detector are very small, and the detector has a small solid angle that allows it to detect only a portion of the neutrons passing through the target. Under these conditions, all neutrons that interact with the target will either be absorbed or scattered away in different directions, so only neutrons that don't interact with the target will reach the detector.

Let $I(x)$ be the intensity of the neutron beam that remains uncollided after traveling a distance $x$ within the target. When a neutron beam passes through a very thin target of thickness $\tau$, the number of collisions per unit area is $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (refer to equations (1) and (4) in [Neutron Interactions and Cross-sections](/posts/Neutron-Interactions-and-Cross-sections/#cross-section-or-microscopic-cross-section)). Therefore, the decrease in neutron beam intensity while traveling a distance $dx$ within the target is:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Integrating this equation yields:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

This shows that the neutron beam intensity decreases exponentially with the distance traveled through the target.

## Mean Free Path
- The average distance a neutron travels between successive collisions with nuclei
- In other words, the average distance a neutron travels without collision
- Denoted by the symbol $\lambda$

The ratio $I(x)/I_0=e^{-\Sigma_t x}$ represents the probability that a neutron will travel a distance $x$ within the medium without colliding with any nuclei. Therefore, the probability $p(x)dx$ that a neutron travels a distance $x$ without collision and then collides within a distance $dx$ is:

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
\\ &= 1/\Sigma_t \tag{3}
\end{align*}
$$
