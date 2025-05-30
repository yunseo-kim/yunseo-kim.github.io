---
title: Mass and Energy, Particles and Waves
description: Explore the mass-energy equivalence principle of relativity theory and calculate the energy of moving electrons considering relativistic effects.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## Mass-Energy Equivalence Principle
Mass and energy are identical and can be converted into each other.

$$ E=mc^2 $$

where $c$ is the speed of light, $2.9979 \times 10^{10}\ \text{cm/sec}$.

## Electron Volt (eV)
*Electron volt (eV)*: The kinetic energy gained by an electron passing through a potential difference of 1 volt

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Mass and Energy of Moving Objects
According to the theory of relativity, the mass of a moving object increases relative to an observer, and the equation relating the speed and mass of a moving object is defined as follows:

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$: rest mass, $v$: speed

The *total energy* of a particle is the sum of its *rest-mass energy* and *kinetic energy*, so the following holds:

$$ E_{\text{total}} = E_{\text{rest}}+E_{\text{kinetic}} = mc^2$$

$$
\begin{align*}
E_{\text{kinetic}} &= E_{\text{total}}-E_{\text{rest}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

Particularly when $v\ll c$, if we set $\cfrac{v^2}{c^2} = \epsilon$ and approximate using Taylor expansion around $\epsilon = 0$ (i.e., Maclaurin expansion):

$$
\begin{align*}
E_{\text{kinetic}} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

This becomes the same as the kinetic energy formula in classical mechanics. Practically, when $v\leq 0.2c$ or $E_{\text{kinetic}} \leq 0.02E_{\text{rest}}$, we can consider $v\ll c$ and use this approximation (i.e., ignore relativistic effects) to obtain sufficiently accurate values.

### Electrons
Since the rest-mass energy of an electron is $E_{\text{rest}}=m_ec^2=0.511 \text{MeV}$, the relativistic kinetic energy formula should be applied when the electron's kinetic energy exceeds $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$. In nuclear engineering, the energy of electrons often exceeds 10 keV, so equation (2) must be applied in most cases.

### Neutrons
The rest-mass energy of a neutron is approximately 1000 MeV, so $0.02E_{rest}=20\text{MeV}$. Since it is rare to deal with neutron kinetic energies exceeding 20 MeV in nuclear engineering, equation (3) is typically used to calculate neutron kinetic energy.

### Photons
Equations (2) and (3) are valid only when the rest mass is not zero, so they cannot be applied to photons with zero rest mass. The total energy of a photon is calculated using the following equation:

$$ E = h\nu \tag{4} $$

$h$: Planck's constant ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$: frequency of the electromagnetic wave

## Matter Waves
Everything in nature is both a particle and a wave simultaneously. That is, all particles have a corresponding wavelength (*de Broglie wavelength*). The wavelength $\lambda$ is a function of momentum $p$ and Planck's constant $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

Also, momentum $p$ is defined by the following equation:

$$ p = mv \tag{6} $$

### Neglecting Relativistic Effects (e.g., Neutrons)
Since kinetic energy is $E=1/2 mv^2$, expressing equation (6) as a function of energy gives:

$$ p=\sqrt{2mE} \tag{7} $$

Substituting this into equation (5), the particle's wavelength becomes:

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

This equation is applied when calculating the de Broglie wavelength of neutrons in nuclear engineering. Substituting the rest mass of a neutron gives:

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

where $\lambda$ is in cm and $E$ is the neutron's kinetic energy expressed in eV.

### Considering Relativistic Effects (e.g., Electrons)
Calculate momentum $p$ by directly solving the relativistic equations:

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{rest}}} \tag{10}$$

Then the de Broglie wavelength is:

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{rest}}}} \tag{11} $$

### Particles with Zero Rest Mass (e.g., Photons)
For particles with zero rest mass, momentum cannot be calculated using equation (6), so it is expressed as:

$$ p=\frac {E}{c} \tag{12} $$

Substituting equation (12) into equation (5):

$$ \lambda = \frac {hc}{E} \tag{13}$$

Substituting the values of $h$ and $c$, the final equation for wavelength is:

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

where $\lambda$ is in meters and $E$ is in eV.
