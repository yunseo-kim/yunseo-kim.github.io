---
title: Nuclear Fusion Reaction Mechanisms in Stars
description: This article introduces the proton-proton chain reaction and the carbon-nitrogen-oxygen
  cycle, which are nuclear fusion reactions occurring in the cores of stars. This
  essay was written by the author for a high school science club activity when they
  were in the first year of high school. Unlike other posts, it is written in a colloquial
  style, but it has been uploaded as it was originally written for archiving purposes.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## Proton-Proton Chain Reaction
This is the most commonly known nuclear fusion reaction in stars. The nucleus of deuterium, called a deuteron, is formed by the combination of one proton (p) and one neutron (n). Therefore, for two protons to combine and form a deuterium nucleus, one of the protons must change into a neutron. So how can a proton change into a neutron?

- When a neutron ($n$) changes into a proton ($p$) while emitting an electron ($e⁻$) and an antineutrino ($\nu_e$), it's called '[Beta decay](/posts/Nuclear-Stability-and-Radioactive-Decay/#negative-beta-decay-beta--decay)'. The reaction equation is $n \rightarrow p + e^{-} + \overline{\nu_e}$.
- The process of a proton ($p$) changing into a neutron ($n$) corresponds to the reverse of beta decay. So we call this '[inverse beta decay](/posts/Nuclear-Stability-and-Radioactive-Decay/#positive-beta-decay-beta-decay)'. What does the inverse beta decay reaction equation look like? There's nothing special about nuclear reaction equations. You just need to swap the positions of proton and neutron, change the electron to a positron, and the antineutrino to a neutrino. Expressed as an equation, it's $p \rightarrow n + e^{+} + \nu_e$.

After the deuterium nucleus is formed through the above process, a helium-3 nucleus is created through $^2_1D + p \rightarrow {^3_2He}$, and finally, two helium-3 nuclei collide to form a helium-4 nucleus and two protons.
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

In fact, there isn't just one reaction path for the proton-proton chain reaction. While the above case is the most representative, there are a few other paths as well. However, the other paths don't account for a significant proportion in stars with masses less than the Sun, and in stars with masses 1.5 times or more than the Sun, the CNO cycle, which we'll discuss later, plays a much larger role than the proton-proton chain reaction, so we won't cover them separately here.

This proton-proton chain reaction predominantly occurs at temperatures around 10-14 million K. In the case of the Sun, with a core temperature of about 15 million K, the pp chain reaction accounts for 98.3% (the remaining 1.3% is accounted for by the CNO cycle).

## Carbon-Nitrogen-Oxygen Cycle (CNO Cycle)
The CNO cycle is a reaction where carbon accepts a proton and changes to nitrogen, then nitrogen accepts a proton and changes to oxygen, and so on, ultimately accepting four protons to produce one helium and returning to carbon. A characteristic of this CNO cycle is that carbon, nitrogen, and oxygen act as catalysts. Theoretically, this CNO cycle predominantly operates in stars with masses 1.5 times or more than the Sun. The difference in reactions according to stellar mass lies in the temperature dependence of the proton-proton chain reaction and the CNO cycle. The former starts at relatively low temperatures around 4 million K, and its reaction rate is proportional to the fourth power of temperature. On the other hand, the latter starts at about 15 million K but is very sensitive to temperature (reaction rate is proportional to the 16th power of temperature), so at temperatures above 17 million K, the CNO cycle accounts for a larger proportion.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Image Source*
> - Author: Wikimedia user [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - License: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

The CNO cycle also has various paths. It is broadly divided into cold CNO cycles (stellar interiors) and hot CNO cycles (novae, supernovae), and each case has three or four reaction paths. I'd like to cover all CNO cycle reactions, but that would require more than this amount of content, so I'll only cover the most basic CN cycle*, that is, CNO-I.

> *The reason it's called the CN cycle without O is that there are no stable oxygen isotopes in this reaction process.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

As shown in the figure above, carbon, nitrogen, and oxygen circulate and act as catalysts. However, regardless of the reaction path, the overall reaction equation and the total amount of energy generated are the same.

## More Readings
- Inkyu Park (Professor of Physics, University of Seoul), [Naver Cast Physics Walk: How many neutrinos are produced in the Sun?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedia, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedia, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
