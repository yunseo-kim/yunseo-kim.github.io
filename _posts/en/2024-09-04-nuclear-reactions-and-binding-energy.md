---
title: Nuclear Reactions and Binding Energy
description: Learn about the expression of nuclear reactions, the definition of Q-value,
  and the concepts of mass defect and binding energy.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.png
---
## Nuclear Reaction
### Basic Laws in Nuclear Reactions
*Nuclear reaction*: A reaction where two different atomic nuclei or an atomic nucleus and a nucleon collide to produce two or more new nuclear particles or gamma rays.

When two atomic nuclei $a$ and $b$ react to produce atomic nuclei or gamma rays $c$ and $d$, this reaction is expressed as follows:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

Four basic laws apply in nuclear reactions:

- *Conservation of nucleons*: The total number of nucleons remains the same before and after the reaction. The type of nucleons may change, so protons and neutrons are not individually conserved.
- *Conservation of charge*: The sum of the charges of the particles remains the same before and after the reaction.
- *Conservation of momentum*: The sum of the momenta of the particles remains the same before and after the reaction.
- *Conservation of energy*: The total energy, <u>including rest mass energy</u>, remains the same before and after the reaction.

### Exothermic Reaction & Endothermic Reaction
In the nuclear reaction of equation ($\ref{nuclear_reaction}$), the total energy before the reaction is the sum of the rest mass energies and kinetic energies of $a$ and $b$, and the total energy after the reaction is the sum of the rest mass energies and kinetic energies of $c$ and $d$. Therefore, by the law of conservation of energy, the following holds:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Rearranging this equation gives:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

This shows that the difference in kinetic energy before and after the nuclear reaction is equal to the difference in rest mass before and after the reaction.
The right side of the last equation is called the *Q-value* of the nuclear reaction and is defined as:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

The Q-value is always expressed in MeV units, and since the rest mass energy for 1 amu of mass is typically 931MeV, the Q-value can also be written as:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Exothermic reaction*: Nuclear reaction where $Q>0$, part of the mass is converted to kinetic energy, increasing kinetic energy after the reaction
- *Endothermic reaction*: Nuclear reaction where $Q<0$, part of the kinetic energy is converted to mass, decreasing kinetic energy after the reaction

| Type of Nuclear <br>Reaction | Q-value | Mass Change Before <br>and After Reaction | Kinetic Energy Change <br>Before and After Reaction |
| :---: | :---: | :---: | :---: |
| Exothermic reaction | $Q>0$ | $\Delta m<0$ (decrease) | $\Delta E>0$ (increase) |
| Endothermic reaction | $Q<0$ | $\Delta m>0$ (increase) | $\Delta E<0$ (decrease) |

### Simplified Expression of Nuclear Reactions
The nuclear reaction in equation ($\ref{nuclear_reaction}$) can be briefly expressed as:

$$ a(b, c)d $$

This means a nuclear reaction where $b$ is incident on $a$, emitting $c$ and transforming into $d$.

#### ex)
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Binding Energy
### Mass Defect
The mass of any nucleus is slightly less than the sum of the masses of the neutrons and protons that compose it. This difference is called the *mass defect*.

If we denote the mass of a nucleus as $M_A$, the mass defect $\Delta$ of any nucleus can be calculated as follows:

$$ \Delta = ZM_p + NM_n - M_A. $$

When the mass defect $\Delta$ is expressed in energy units, it represents the energy required to break a nucleus into its constituent nucleons. This is called the *binding energy* as it's the energy that holds the nucleons together. Conversely, when a nucleus is formed from A nucleons, the energy level decreases by the binding energy $\Delta$, so this amount of energy is released to the surroundings during the nuclear reaction process.

### Average Binding Energy per Nucleon
While the total binding energy of an atomic nucleus increases with increasing mass number $A$, the rate of increase is not constant.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
As can be seen in the image above, the average binding energy per nucleon $\Delta/A$ increases sharply at low mass numbers but decreases with a gentle slope for heavy atomic nuclei with $A\geq56$.

### Relationship between Q-value of Nuclear Reactions and Binding Energy
In the nuclear reaction of equation ($\ref{nuclear_reaction}$), the binding energy of nucleus $a$ is 

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

and the mass of $a$ is

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

Similarly, for nuclei $b$, $c$, and $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Assuming

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

and substituting these equations into equation ($\ref{Q_value}$), we get:

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

This means that energy is always released when two less stable nuclei combine to form a more stable nucleus through a nuclear reaction process.

### Nuclear Fusion and Nuclear Fission
In the case of a nuclear reaction where deuterium with a binding energy of $2.23\text{MeV}$ and tritium with a binding energy of $8.48\text{MeV}$ combine to produce $^4\text{He}$ with a binding energy of $28.3\text{MeV}$ and emit one neutron:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

The energy corresponding to the difference in binding energies before and after the reaction, $28.3-(2.23+8.48)=17.6\text{MeV}$ (or $3.52\text{MeV}$ per nucleon), is released in the form of kinetic energy of the helium nucleus and neutron.

A reaction like equation ($\ref{nuclear_fusion}$), where two light atomic nuclei with small mass numbers combine to form a heavier atomic nucleus with a larger mass number than before the reaction, is called *nuclear fusion*. This is the energy source of all stars, including the Sun, and someday humans may directly use it as a power source.

On the other hand, in the case of a nuclear reaction where $^{235}\text{U}$ with a binding energy of about $1780\text{MeV}$ absorbs a neutron and then separates into $^{92}\text{Kr}$ with a binding energy of $783\text{MeV}$ and $^{141}\text{Ba}$ with about $1170\text{MeV}$, emitting 3 neutrons:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

The energy corresponding to the difference in binding energies before and after the reaction, $783+1170-1780=173\text{MeV}$ (or $0.733\text{MeV}$ per nucleon), is released.

A reaction like equation ($\ref{nuclear_fission}$), where a heavy atomic nucleus separates into lighter atomic nuclei, is called *nuclear fission*. Since President Eisenhower's "Atoms for Peace" speech and the Soviet Union's Obninsk Nuclear Power Plant, it has been widely used as a power source.
