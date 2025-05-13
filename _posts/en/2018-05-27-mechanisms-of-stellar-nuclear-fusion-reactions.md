---
title: Nuclear Fusion Reaction Mechanisms in Stars
description: This article introduces the nuclear fusion reactions occurring in stellar cores, specifically the proton-proton chain reaction and the carbon-nitrogen-oxygen cycle (CNO cycle). This essay was originally written for a high school science club activity when I was a first-year high school student, and unlike other posts, it is written in a conversational style. It has been uploaded in its original form for archiving purposes.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## Proton-Proton Chain Reaction
This is the most commonly known nuclear fusion reaction in stars. The nucleus of deuterium, called a deuteron, is formed by combining one proton (p) and one neutron (n). Therefore, for two protons to combine and form a deuterium nucleus, one of the protons must transform into a neutron. So how can a proton change into a neutron?

- When a neutron ($n$) changes into a proton ($p$) while emitting an electron ($e⁻$) and an antineutrino ($\nu_e$), it's called '[beta decay](/posts/Nuclear-Stability-and-Radioactive-Decay/#negative-beta-decay-beta--decay)'. The reaction equation is $n \rightarrow p + e^{-} + \overline{\nu_e}$.
- The process of a proton ($p$) changing into a neutron ($n$) corresponds to the reverse of beta decay. This is called '[inverse beta decay](/posts/Nuclear-Stability-and-Radioactive-Decay/#positive-beta-decay-beta-decay)'. What does the inverse beta decay reaction equation look like? There's nothing special about nuclear reaction equations. You just swap the positions of the proton and neutron, change the electron to a positron, and the antineutrino to a neutrino. Expressed as an equation: $p \rightarrow n + e^{+} + \nu_e$.

After a deuterium nucleus is formed through the above process, a helium-3 nucleus is created through $^2_1D + p \rightarrow {^3_2He}$, and finally, two helium-3 nuclei collide to form one helium-4 nucleus and two protons.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

In fact, there isn't just one reaction pathway for the proton-proton chain reaction. The above case is the most representative, but there are several other pathways as well. However, the other pathways don't account for a significant proportion in stars with masses less than that of the Sun, and in stars with masses more than 1.5 times that of the Sun, the CNO cycle (which we'll discuss later) plays a much more significant role than the proton-proton chain reaction, so I won't cover them separately here.

This proton-proton chain reaction predominantly occurs at temperatures of approximately 10-14 million K. In the case of the Sun, with a core temperature of about 15 million K, the pp chain reaction accounts for 98.3% of energy production (the remaining 1.3% comes from the CNO cycle).

## Carbon-Nitrogen-Oxygen Cycle (CNO Cycle)
The CNO cycle is a reaction where carbon accepts a proton and changes into nitrogen, then nitrogen accepts a proton and changes into oxygen, and so on. Ultimately, it accepts four protons, releases one helium nucleus, and returns to carbon. The characteristic of this CNO cycle is that carbon, nitrogen, and oxygen act as catalysts. Theoretically, this CNO cycle predominantly operates in stars with masses greater than 1.5 times that of the Sun. The difference in reactions according to stellar mass lies in the temperature dependence of the proton-proton chain reaction versus the CNO cycle. The former begins at relatively low temperatures around 4 million K, and its reaction rate is proportional to the fourth power of temperature. The latter, on the other hand, begins at around 15 million K but is very sensitive to temperature (reaction rate proportional to the 16th power of temperature), so at temperatures above 17 million K, the CNO cycle becomes more dominant.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Image source*
> - Author: Wikimedia user [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

The CNO cycle also has various pathways. It is broadly divided into the cold CNO cycle (stellar interior) and the hot CNO cycle (nova, supernova), and each case has three or four reaction pathways. I would like to cover all CNO cycle reactions, but that would require more than this amount of content, so I will only cover the most basic CN cycle*, that is, CNO-I.

> *The reason it's called the CN cycle without the O is because there is no stable isotope of oxygen in this reaction process.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

As shown in the figure above, carbon, nitrogen, and oxygen cycle and act as catalysts. However, regardless of the reaction pathway, the overall reaction equation and the total amount of energy generated are the same.

## More Readings
- Inkyu Park (Professor of Physics, University of Seoul), [Naver Cast Physics Walk: How many neutrinos are produced in the Sun?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
