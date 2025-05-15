---
title: Nuclear Reactions and Binding Energy
description: Learn about nuclear reaction expressions, Q-value definitions, and the concepts of mass defect and binding energy.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Nuclear Reaction
### Basic Laws in Nuclear Reactions
*Nuclear reaction*: A reaction where two different nuclei, or a nucleus and a nucleon, collide to produce two or more new nuclear particles or gamma rays

When two nuclei $a$ and $b$ react to produce nuclei or gamma rays $c$ and $d$, this reaction is expressed as:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

The following four basic laws apply in nuclear reactions:

- *Conservation of nucleons*: The total number of nucleons remains the same before and after the reaction. The type of nucleons may change, so protons and neutrons are not individually conserved.
- *Conservation of charge*: The total charge of the particles remains the same before and after the reaction.
- *Conservation of momentum*: The total momentum of the particles remains the same before and after the reaction.
- *Conservation of energy*: The total energy, <u>including rest mass energy</u>, remains the same before and after the reaction.

### Exothermic Reaction & Endothermic Reaction
In the nuclear reaction shown in equation ($\ref{nuclear_reaction}$), the total energy before the reaction is the sum of the rest mass energies and kinetic energies of $a$ and $b$, and the total energy after the reaction is the sum of the rest mass energies and kinetic energies of $c$ and $d$. Therefore, by the law of conservation of energy:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Rearranging this equation:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

This shows that the difference in kinetic energy before and after the nuclear reaction equals the difference in rest mass.
The right side of the last equation is called the *Q-value* of the nuclear reaction and is defined as:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

The Q-value is always expressed in MeV units. Since the rest mass energy of 1 amu is typically 931 MeV, the Q-value can also be written as:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Exothermic reaction*: Nuclear reaction where $Q>0$, part of the mass is converted to kinetic energy, increasing kinetic energy after the reaction
- *Endothermic reaction*: Nuclear reaction where $Q<0$, part of the kinetic energy is converted to mass, decreasing kinetic energy after the reaction

| Reaction Type | Q-value | Mass Change Before and After | Kinetic Energy Change Before and After |
| :---: | :---: | :---: | :---: |
| Exothermic reaction | $Q>0$ | $\Delta m<0$ (decrease) | $\Delta E>0$ (increase) |
| Endothermic reaction | $Q<0$ | $\Delta m>0$ (increase) | $\Delta E<0$ (decrease) |

### Abbreviated Notation for Nuclear Reactions
The nuclear reaction in equation ($\ref{nuclear_reaction}$) can be abbreviated as:

$$ a(b, c)d $$

This means that $b$ is incident on $a$, emitting $c$ and transforming into $d$.

#### Examples:
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Binding Energy
### Mass Defect
The mass of any nucleus is slightly less than the sum of the masses of the neutrons and protons that constitute it. This difference is called the *mass defect*.

If the mass of a nucleus is $M_A$, the mass defect $\Delta$ of any nucleus can be calculated as:

$$ \Delta = ZM_p + NM_n - M_A. $$

When the mass defect $\Delta$ is expressed in energy units, it represents the energy required to break a nucleus into its constituent nucleons. This is called the *binding energy* because it is the energy that holds the nucleons together. Conversely, when a nucleus is formed from A nucleons, the energy level decreases by the binding energy $\Delta$, and this amount of energy is released to the surroundings during the nuclear reaction.

### Average Binding Energy per Nucleon
The total binding energy of a nucleus increases with mass number $A$, but the rate of increase is not constant.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
As shown in the image above, the average binding energy per nucleon $\Delta/A$ increases steeply at low mass numbers but decreases with a gentle slope for heavy nuclei with $A\geq56$.

### Relationship Between Q-value and Binding Energy in Nuclear Reactions
In the nuclear reaction of equation ($\ref{nuclear_reaction}$), the binding energy of nucleus $a$ is:

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

and the mass of $a$ is:

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

Similarly, for nuclei $b$, $c$, and $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Considering that:

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

and substituting these equations into equation ($\ref{Q_value}$):

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

This means that energy is always released when two less stable nuclei combine to form a more stable nucleus through a nuclear reaction process.

### Nuclear Fusion and Nuclear Fission
In the case of a nuclear reaction where deuterium with a binding energy of $2.23\text{MeV}$ and tritium with a binding energy of $8.48\text{MeV}$ combine to produce $^4\text{He}$ with a binding energy of $28.3\text{MeV}$ and release one neutron:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

The difference in binding energy before and after the reaction, $28.3-(2.23+8.48)=17.6\text{MeV}$ (or $3.52\text{MeV}$ per nucleon), is released as kinetic energy of the helium nucleus and neutron.

Reactions like equation ($\ref{nuclear_fusion}$), where two light nuclei with small mass numbers combine to form a heavier nucleus with a larger mass number, are called *nuclear fusion*. This is the energy source of the sun and all stars, and someday humans may directly use it as a power source.

On the other hand, in a nuclear reaction where $^{235}\text{U}$ with a binding energy of about $1780\text{MeV}$ absorbs a neutron and then splits into $^{92}\text{Kr}$ with a binding energy of $783\text{MeV}$ and $^{141}\text{Ba}$ with about $1170\text{MeV}$, releasing three neutrons:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

The difference in binding energy before and after the reaction, $783+1170-1780=173\text{MeV}$ (or $0.733\text{MeV}$ per nucleon), is released.

Reactions like equation ($\ref{nuclear_fission}$), where a heavy nucleus splits into lighter nuclei, are called *nuclear fission*. Since President Eisenhower's "Atoms for Peace" speech and the Soviet Union's Obninsk Nuclear Power Plant, nuclear fission has been widely used as a power source.

## Magic Numbers
Nuclei tend to be particularly stable when the number of neutrons or protons is 2, 6, 8, 14, 20, 28, 50, 82, or 126. These numbers are called *magic numbers*. They correspond to the number of neutrons and protons needed to fill the nuclear shells, similar to how electron shells are filled outside the atom.

Isotopes with magic numbers are practically useful in nuclear engineering. A notable example is zirconium-90 ($^{90}_{40} \mathrm{Zr}$), which has 50 neutrons. Due to its stability, it does not readily absorb neutrons, making it widely used as fuel rod cladding material in reactor cores.
