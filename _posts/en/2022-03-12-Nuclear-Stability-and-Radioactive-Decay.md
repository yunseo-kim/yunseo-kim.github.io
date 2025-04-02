---
title: Nuclear Stability and Radioactive Decay
description: Learn about the Segre Chart, types of radioactive decay, and isomeric
  transitions.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## Segre Chart or Nuclide Chart
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Image source*
> - Author: Wikimedia user [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- For nuclides with atomic number $Z$ greater than 20, more neutrons than protons are needed for stability
- Neutrons play a role in binding the nucleus together, overcoming the electrical repulsion between protons

## Reasons for Radioactive Decay
- Only specific combinations of neutrons and protons form stable nuclides
- If the number of neutrons relative to protons is too high or too low, the nuclide becomes unstable and undergoes *radioactive decay*
- The nucleus formed after decay is usually in an excited state, so it releases energy in the form of gamma rays or X-rays

## Beta Decay ($\beta$-decay)
### Positive Beta Decay ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Occurs when there is a relative shortage of neutrons
- A proton ($p$) changes into a neutron ($n$) and emits a positron ($\beta^+$) and an electron neutrino ($\nu_e$)
- The atomic number decreases by 1, while the mass number remains unchanged

Example) $^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### Negative Beta Decay ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Occurs when there is a relative excess of neutrons
- A neutron ($n$) changes into a proton ($p$) and emits an electron ($\beta^-$) and an electron antineutrino ($\overline{\nu}_e$)
- The atomic number increases by 1, while the mass number remains unchanged

Example) $^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### Energy Spectrum of Emitted Electrons (Positrons)
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Image source*
> - Author: German Wikipedia user [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Electrons or positrons emitted in beta decay show a continuous energy spectrum as shown above.
- $\beta^-$ decay: $\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$ decay: $\overline{E}\approx 0.4E_{\text{max}}$

### Decay Chain
Often, the *daughter nuclide* formed through beta decay is also unstable and undergoes successive beta decays. This leads to a *decay chain* as follows:

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (stable)} $$ 

## Electron Capture or K-capture

$$ p + e \to n + \nu_e $$

- Occurs when there is a relative shortage of neutrons
- Captures an electron from the innermost shell (K-shell) and converts a proton in the nucleus into a neutron
- The atomic number decreases by 1, while the mass number remains unchanged
- After electron capture, a vacancy is formed in the electron cloud, which is later filled by an outer electron, emitting X-rays or Auger electrons
- The daughter nuclide produced by electron capture is identical to that produced by $\beta^+$ decay, so these two processes compete with each other.

## Alpha Decay ($\alpha$-decay)
- Emits an alpha particle ($\alpha$, $^4_2\text{He}$)
- The atomic number decreases by 2, and the mass number decreases by 4
- Commonly occurs in nuclei heavier than lead
- Unlike beta decay, the energy of alpha particles emitted during alpha decay is quantized.

Example) $^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## Spontaneous Fission
- Very heavy and unstable nuclides can undergo fission without absorbing neutrons
- Included in radioactive decay in a broad sense

## Proton Emission
- In extremely proton-rich unstable nuclides, a single proton can be emitted
- The atomic number and mass number decrease by 1
- Occurs very rarely

## Decay Scheme and Isomeric Transition
### Decay Scheme
*Decay scheme*: A diagram that visually represents all decay paths of a radioactive material

### Isomeric Transition
- Nuclei formed by radioactive decay may remain in an excited state after transformation, in which case they release energy in the form of gamma rays (although not strictly decay, the term gamma decay is conventionally used when gamma rays are emitted without changing the nuclide).
- Most excited nuclei emit gamma rays and transition to the ground state in a very short time, but in certain cases, gamma ray emission is delayed, appearing like a metastable state. This delayed state is called the *isomeric state* of the nucleus.
- The transition from an isomeric state to the ground state by emitting gamma rays is called an *isomeric transition* and is denoted as IT.
![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Image source*
> - Author: British Wikimedia user [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - License: Free to use for any purpose without any conditions, unless such conditions are required by law
