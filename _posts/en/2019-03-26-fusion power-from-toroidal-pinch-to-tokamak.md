---
title: "Fusion Power: From Toroidal Pinch to Tokamak"
description: >-
  This post covers the concept of nuclear fusion, its background as a promising next-generation power source, the technical goals for commercializing fusion power, and the evolution of fusion power technology from toroidal pinch to ITER.
  The author notes that this essay was originally written for a high school science club activity when they were in their second year of high school. Unlike other posts, it is written in a colloquial style, but has been uploaded in its original form for archival purposes.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
---

## What is Nuclear Fusion?
Nuclear fusion refers to the reaction where two atomic nuclei collide and merge to form a single heavier nucleus. Fundamentally, atomic nuclei have a positive charge due to the protons inside, so when two nuclei approach each other, they repel due to electrostatic repulsion. However, if the nuclei are heated to extremely high temperatures, their kinetic energy can overcome the electrical repulsion, allowing the nuclei to collide. Once the nuclei are close enough, the strong nuclear force takes over, binding them into a single nucleus.

In the late 1920s, when it was discovered that nuclear fusion was the energy source of stars and it became possible to physically explain fusion, discussions began on whether fusion could be used for human benefit. Shortly after World War II, the idea of controlling and utilizing fusion energy was seriously considered, and research began at universities in the UK such as the University of Liverpool, Oxford University, and the University of London.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## Break-even Point and Ignition Condition
One of the most fundamental issues for fusion power is that the energy produced from the fusion reaction must be greater than the initial input energy. In the DT reaction, alpha particles and neutrons are produced, with 20% of the energy released by fusion carried by alpha particles and 80% by neutrons. The energy of the alpha particles is used to heat the plasma, while the neutron energy is converted into electrical energy. Initially, external energy must be applied to raise the plasma temperature, but once the fusion reaction rate increases sufficiently, the plasma can be heated solely by the energy of the alpha particles, allowing the fusion reaction to sustain itself. This point is called ignition, and it occurs when $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, or when $\text{plasma pressure}(P) \times \text{energy confinement time}(\tau_{E}) > 5$ in the temperature range of 10-20keV (approximately 100-200 million K).

![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## Toroidal Pinch
In 1946, Peter Thonemann conducted research at Oxford University's Clarendon Laboratory on confining plasma within a torus using the pinch effect.

As shown in the figure, when current is passed through the plasma, a magnetic field forms around the current, and the interaction between the current and the magnetic field creates an inward force. Theoretically, if the current is large enough, the pinch effect could prevent the plasma from touching the walls. However, experimental results showed that this method was highly unstable, and therefore it is rarely studied today.

![pinch effect](/assets/img/fusion-power/pinch-effect.png)

<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## Stellarator
In the early 1950s, astrophysicist Lyman Spitzer at Princeton University invented a new plasma confinement device and named it the stellarator. Unlike the toroidal pinch where the magnetic field is created by the current flowing through the plasma itself, in a stellarator, the magnetic field is formed solely by external coils. Stellarators have the advantage of being able to maintain plasma stably for long periods, and are still considered to have sufficient potential for practical application in fusion power plants. Research on stellarators continues actively to this day.

![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (toroidalnaya karmera magnitnaya katushka)
By the 1960s, fusion research had entered a period of stagnation. It was during this time that the Kurchatov Institute in Moscow first devised the tokamak, providing a breakthrough. When the results of the tokamak were presented at a scientific conference in 1968, most countries shifted their research direction towards tokamaks, making it the most promising magnetic confinement method today. Tokamaks have the advantage of being able to maintain plasma for long periods while having a much simpler structure than stellarators.

![tokamak](/assets/img/fusion-power/tokamak.png)

## Large Tokamak Devices and the ITER Project
Since the 1970s, large-scale tokamak devices have been constructed to move closer to actual fusion power generation. Notable examples include the European Union's JET, Princeton's TFTR in the United States, and Japan's JT-60U. By consistently conducting research to increase output in these large tokamaks based on data obtained from small-scale experimental devices, they have nearly reached the break-even point. Currently, to make a final assessment of the feasibility of fusion power, China, the European Union, India, Japan, Korea, Russia, and the United States are collaborating on the ITER project, humanity's largest international joint project.

![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## References
- [Khatri, G.. (2010). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (2005)
