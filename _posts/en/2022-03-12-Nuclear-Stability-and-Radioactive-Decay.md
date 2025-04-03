---
title: Nuclear Stability and Radioactive Decay
description: Explore the Segré chart and various types of radioactive decay, the energy spectrum of electrons/positrons emitted in beta decay and the discovery of neutrinos, decay chains of several key nuclides (carbon-14, potassium-40, tritium, cesium-137), and isomeric transitions.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.png
---
## Prerequisites
- [Subatomic Particles and Constituents of an Atom](/posts/constituents-of-an-atom/)

## Segre Chart or Nuclide Chart
![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Image source*
> - Author: Wikimedia user [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- For nuclides with atomic number $Z$ greater than 20, more neutrons than protons are needed for stability
- Neutrons serve to bind the nucleus together, overcoming the electrical repulsion between protons

## Reasons for Radioactive Decay
- Only specific combinations of neutrons and protons form stable nuclides
- If the neutron-to-proton ratio is too high or too low, the nuclide becomes unstable and undergoes *radioactive decay*
- The nucleus formed after decay is usually in an excited state, releasing energy in the form of gamma rays or X-rays

## Beta Decay ($\beta$-decay)
### Positive Beta Decay ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Occurs when there is a relative deficiency of neutrons
- A proton ($p$) transforms into a neutron ($n$), emitting a positron ($\beta^+$) and an electron neutrino ($\nu_e$)
- Atomic number decreases by 1, mass number remains unchanged

Example: $^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### Negative Beta Decay ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Occurs when there is a relative excess of neutrons
- A neutron ($n$) transforms into a proton ($p$), emitting an electron ($\beta^-$) and an electron antineutrino ($\overline{\nu}_e$)
- Atomic number increases by 1, mass number remains unchanged

Example: $^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### Energy Spectrum of Emitted Electrons (Positrons)
![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Image source*
> - Author: German Wikipedia user [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Electrons or positrons emitted in beta decay show a continuous energy spectrum as shown above.
- $\beta^-$ decay: $\overline{E}\approx 0.3E_{\text{max}}$
- $\beta^+$ decay: $\overline{E}\approx 0.4E_{\text{max}}$

> While the total energy released in beta decay is quantized, the electron/positron and antineutrino/neutrino share this energy arbitrarily, resulting in a continuous spectrum when only measuring the electron/positron energy.
> The continuous energy spectrum of electrons/positrons emitted in beta decay was inconsistent with theoretical predictions and seemed to violate the law of energy conservation.  
> To explain this result, Wolfgang Ernst Pauli predicted in 11930 the existence of an '<u>electrically neutral particle with extremely small mass and extremely low reactivity</u>' and proposed calling it a 'neutron,' but when Sir James Chadwick discovered what we now know as the neutron in 11932 and named it as such, a naming conflict arose. The following year, in 11933, Enrico Fermi published his theory of beta decay and renamed it *neutrino* by adding the Italian suffix '-ino' meaning "small," giving it its current name.  
> Later in 11942, Chinese nuclear physicist Wang Ganchang (王淦昌) first proposed a method to detect neutrinos using [electron capture](#electron-capture-or-k-capture), and in 11956, Clyde Cowan, Frederick Reines, Francis B. Harrison, Herald W. Kruse, and Austin D. McGuire successfully detected neutrinos through the Cowan–Reines neutrino experiment and published their results in Science, verifying their existence. Frederick Reines was awarded the Nobel Prize in Physics in 11995 for this achievement.  
> Thus, the study of beta decay is historically significant for providing clues about the existence of neutrinos.
{: .prompt-info }

### Decay Chain
Often, the *daughter nuclide* formed through beta decay is also unstable and undergoes subsequent beta decay. This leads to a *decay chain* as follows:

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (stable)} $$

Below are some important beta decay chains.

#### Carbon-14
- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> Carbon-14 is naturally produced in the upper atmosphere by cosmic radiation, maintaining a relatively constant concentration in the atmosphere. Animals and plants also maintain the same carbon-14 concentration as the atmosphere during their lifetime through continuous respiration and gas exchange, but after death, this exchange stops, and the carbon-14 concentration in the remains decreases over time. This is the basis for radiocarbon dating.
{: .prompt-tip }

#### Potassium-40
- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> Potassium-40 is the largest natural source of radiation in the bodies of all animals, including humans, and is naturally present in all foods we consume daily, particularly abundant in Brazil nuts, beans, spinach, bananas, avocados, coffee, cutlassfish, and garlic.  
> A 70kg adult has about 140g of potassium in their body, which is maintained at a constant level, of which about 0.014g is potassium-40, corresponding to a radioactivity of approximately 4330 Bq.
{: .prompt-tip }

#### Tritium
- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> Tritium is a fuel material that participates in D-T fusion reactions in fusion reactors or hydrogen bombs/neutron bombs. It is naturally produced in the atmosphere by cosmic radiation, but due to its relatively short half-life of about 12.32 years, it decays quickly and exists in very low proportions in nature. When used in fusion reactors or nuclear weapons, rather than directly loading tritium (due to its rapid decay), neutrons are irradiated onto lithium-6 to produce tritium. For this reason, highly enriched and high-purity lithium-6 for nuclear weapons is considered a critical material for nuclear development and is one of the main monitoring targets of the international community, including the IAEA.  
> Even apart from the aforementioned uses, it is a commonly used material in small quantities, such as in military items like night sights for K2 rifles and K1 submachine guns, luminous watches, and emergency exit signs in buildings that need to maintain luminescence without power supply. Tritium is encapsulated with phosphorus, a fluorescent material, so that when tritium decays, the emitted beta rays collide with the phosphorus to produce light. Emergency exit signs typically use about 900 billion becquerels of tritium.  
> Due to its steady demand and the impossibility of long-term stockpiling, it is treated as an important strategic material, with prices approaching $30,000 per gram. Currently, most commercially produced and sold tritium comes from pressurized heavy water reactors like CANDU (CANada Deuterium Uranium) reactors. In Korea, Wolsong Units 1-4 are CANDU reactors.
{: .prompt-tip }

#### Cesium-137
- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> Cesium-137 is a major byproduct of nuclear reactor fission reactions and nuclear tests. Due to its relatively long half-life (about 30 years), emission of highly penetrating gamma rays, and chemical properties similar to potassium that allow easy absorption into the body, it is a key isotope for monitoring and management. Originally almost non-existent in nature, it now exists in soil worldwide at an average of about 7 μg/g, resulting from the Trinity nuclear test and the atomic bombings of Hiroshima and Nagasaki by the United States to subdue the rampaging Imperial Japan, as well as numerous atmospheric nuclear tests mainly conducted in the 11950s-11960s and several major nuclear accidents (Chernobyl nuclear power plant accident, Goiânia accident in Brazil, etc.).  
> Medical treatment and observation may be necessary if more than 10,000 Bq of cesium-137 is absorbed into the body. Some residents near the Chernobyl nuclear power plant accident reportedly had tens of thousands of Bq of cesium-137 absorbed into their bodies. In the case of the Fukushima nuclear power plant accident, nearby residents absorbed about 50-250 Bq shortly after the accident.
> Although there are individual differences and variations between sources, the biological half-life of cesium-137 without treatment is about [110 days according to the CDC](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp). If exposure to a large amount of cesium-137 is suspected, [taking medical Prussian blue tablets can accelerate excretion from the body, reducing the biological half-life to about 30 days](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp).
{: .prompt-tip }

## Electron Capture or K-capture

$$ p + e \to n + \nu_e $$

- Occurs when there is a relative deficiency of neutrons
- Captures an electron from the innermost shell (K-shell) to convert a proton in the nucleus into a neutron
- Atomic number decreases by 1, mass number remains unchanged
- After electron capture, a vacancy forms in the electron cloud, which is later filled by an electron from an outer shell, emitting X-rays or Auger electrons
- The daughter nuclide produced by electron capture is identical to that produced by $\beta^+$ decay, so these two processes compete with each other

## Alpha Decay ($\alpha$-decay)
- Emits an alpha particle ($\alpha$, $^4_2\mathrm{He}$)
- Atomic number decreases by 2, and mass number decreases by 4
- Commonly occurs in nuclei heavier than lead
- Unlike beta decay, the energy of alpha particles emitted during alpha decay is quantized

Example: $^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## Spontaneous Fission
- Very heavy and unstable nuclides can undergo fission on their own without absorbing neutrons
- Included in radioactive decay in a broad sense
- Uranium-238 undergoes alpha decay with a half-life of $10^9$ years, but simultaneously undergoes rare spontaneous fission with a half-life of about $10^16$ years. The following table shows the spontaneous fission half-lives of several nuclides.

| Nuclide | Spontaneous Fission Half-life | Characteristics |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | About $10^{16}$ years | Occurs very rarely |
| $^{240}\mathrm{Pu}$ | About $10^{11}$ years | Fissile material used in nuclear weapons |
| $^{252}\mathrm{Cf}$ | About $2.6$ years | Undergoes spontaneous fission very actively <br>$\rightarrow$ Used as a neutron source for reactor startup, etc. |

## Proton Emission
- In extremely proton-rich unstable nuclides, a single proton may be emitted
- Atomic number and mass number decrease by 1
- Occurs very rarely

## Decay Schemes and Isomeric Transitions
### Decay Scheme
*Decay scheme*: A diagram that visually represents all decay pathways of a radioactive material

### Isomeric Transition
- Nuclei formed by radioactive decay may remain in an excited state after transformation, in which case they release energy in the form of gamma rays (although gamma ray emission does not change the nuclide and is not strictly decay, the term gamma decay is sometimes used conventionally).
- Most excited nuclei transition to the ground state by emitting gamma rays in a very short time, but in certain cases, gamma ray emission is delayed, appearing like a metastable state. These delayed states are called *isomeric states* of the nucleus.
- The transition from an isomeric state to the ground state by emitting gamma rays is called an *isomeric transition* and is denoted as IT.

![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Image source*
> - Author: British Wikimedia user [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - License: Free to use for any purpose without restrictions, as long as it does not violate the law

![Cs-137 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> License: [Public Domain](https://en.wikipedia.org/wiki/Public_domain)
