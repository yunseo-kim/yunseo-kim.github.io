---
title: Homogeneous Mixtures and Molecular Cross-sections
description: Let's calculate the macroscopic cross-section of a homogeneous mixture
  containing two or more nuclides.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.png
---
## Macroscopic Cross-section of a Homogeneous Mixture
Let's consider a homogeneous mixture of two nuclides $X$ and $Y$. The atomic densities of each nuclide are $N_X$ and $N_Y$ $\text{atom/cm}^3$ respectively, and the cross-sections for a specific reaction between neutrons and these nuclei are $\sigma_X$ and $\sigma_Y$ respectively.

Then, the probability of a neutron colliding with nuclei $X$ and $Y$ per unit length is $\Sigma_X=N_X\sigma_X$ and $\Sigma_Y=N_Y\sigma_Y$ respectively (refer to [Macroscopic Cross-section](/posts/Neutron-Interactions-and-Cross-sections/#macroscopic-cross-section)). The total probability of a neutron reacting with these two types of nuclei per unit length is as follows:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \tag{1}$$

## Equivalent Cross-section of a Molecule
If the nuclei we examined above exist in molecular form, we can define the equivalent cross-section of that molecule by dividing the macroscopic cross-section of the mixture obtained from equation (1) by the number of molecules per unit volume.

If there are $N$ molecules of $X_mY_n$ per unit volume, then $N_X=mN$, $N_Y=nN$, and from equation (1), we can calculate the cross-section of this molecule as follows:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \tag{2} $$

> Equations (1) and (2) are valid under the assumption that nuclei $X$ and $Y$ react independently with neutrons, so they cannot be applied to elastic scattering by molecules and solids.
> The scattering cross-sections of molecules and solids at low neutron energies must be determined through experiments.
{: .prompt-warning }
