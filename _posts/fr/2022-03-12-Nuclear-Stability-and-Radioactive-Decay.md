---
title: "Stabilité nucléaire et désintégration radioactive"
description: >-
  Découvrez le tableau de Segré, les types de désintégration radioactive et la transition isomère.
categories: [Physique de l'ingénieur, Génie nucléaire]
tags: [Physique nucléaire, Désintégration radioactive]
math: true
---

## Tableau de Segré (Segre Chart) ou Carte des nucléides
![Tableau de Segré](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Source de l'image*
> - Auteur : Utilisateur Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - Licence : [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- Pour les nucléides avec un numéro atomique $Z$ supérieur à 20, plus de neutrons que de protons sont nécessaires pour la stabilisation
- Les neutrons jouent un rôle dans la liaison du noyau en surmontant la répulsion électrique entre les protons

## Raisons de la désintégration radioactive (Radioactive Decay)
- Seules certaines combinaisons de neutrons et de protons forment des nucléides stables
- Si le nombre de neutrons par rapport au nombre de protons est trop élevé ou trop faible, le nucléide est instable et subit une *désintégration radioactive (radioactive decay)*
- Le noyau formé après la désintégration est généralement dans un état excité et libère de l'énergie sous forme de rayons gamma ou de rayons X

## Désintégration bêta ($\beta$-decay)
### Désintégration bêta plus ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Se produit lorsque le nombre de neutrons est relativement insuffisant
- Un proton ($p$) se transforme en neutron ($n$) en émettant un positron ($\beta^+$) et un neutrino électronique ($\nu_e$)
- Le numéro atomique diminue de 1, le nombre de masse reste inchangé

Exemple : $^{23}\_{12}\text{Mg} \to\;^{23}\_{11}\text{Na} + e^+ + \nu_e$

### Désintégration bêta moins ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Se produit lorsque le nombre de neutrons est relativement excessif
- Un neutron ($n$) se transforme en proton ($p$) en émettant un électron ($\beta^-$) et un antineutrino électronique ($\overline{\nu}_e$)
- Le numéro atomique augmente de 1, le nombre de masse reste inchangé

Exemple : $^3_1\text{H} \to\;^3_2\text{He} + e^- + \overline{\nu}_e$

### Spectre d'énergie des électrons (positrons) émis
![Spectre d'énergie des électrons émis lors de la désintégration bêta](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Source de l'image*
> - Auteur : Utilisateur Wikipédia allemand [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - Licence : [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Les électrons ou positrons émis lors de la désintégration bêta présentent un spectre d'énergie continu comme ci-dessus.
- Désintégration $\beta^-$ : $\overline{E}\approx 0.3E_{\text{max}}$
- Désintégration $\beta^+$ : $\overline{E}\approx 0.4E_{\text{max}}$

### Chaîne de désintégration (Decay Chain)
Souvent, le *nucléide fils (daughter nuclide)* formé par désintégration bêta est également instable et subit une désintégration bêta consécutive. Cela conduit à une *chaîne de désintégration (decay chain)* comme suit :

$$ ^{20}\text{O} \overset{\beta^-}{\rightarrow}\;^{20}\text{F} \overset{\beta^-}{\rightarrow}\;^{20}\text{Ne (stable)} $$ 

## Capture électronique (Electron Capture) ou Capture K (K-capture)
~~Ce n'est pas une capture coréenne~~

$$ p + e \to n + \nu_e $$

- Se produit lorsque le nombre de neutrons est relativement insuffisant
- Capture un électron de la couche la plus interne (couche K) pour convertir un proton du noyau en neutron
- Le numéro atomique diminue de 1, le nombre de masse reste inchangé
- Après la capture électronique, un espace vide se forme dans le nuage électronique, qui est ensuite rempli par le déplacement d'un autre électron extérieur, émettant des rayons X ou des électrons Auger
- Le nucléide fils (daughter nuclide) créé par capture électronique est identique à celui créé par désintégration $\beta^+$, donc ces deux processus sont en compétition.

## Désintégration alpha ($\alpha$-decay)
- Émission d'une particule alpha ($\alpha$, $^4_2\text{He}$)
- Le numéro atomique diminue de 2 et le nombre de masse diminue de 4
- Courante dans les noyaux plus lourds que le plomb
- Contrairement à la désintégration bêta, l'énergie des particules alpha émises lors de la désintégration alpha est quantifiée.

Exemple : $^{238}\_{92}\text{U} \to\;^{234}\_{90}\text{Th} +\; ^4_2\text{He}$

## Fission spontanée (Spontaneous Fission)
- Les nucléides très lourds et instables peuvent subir une fission nucléaire spontanée sans absorption de neutrons
- Incluse dans la désintégration radioactive au sens large

## Émission de protons (Proton Emission)
- Dans le cas de nucléides extrêmement instables avec un excès de protons, un seul proton peut être émis
- Le numéro atomique et le nombre de masse diminuent de 1
- Se produit très rarement

## Schéma de désintégration et transition isomère
### Schéma de désintégration (Decay Scheme)
*Schéma de désintégration (decay scheme)* : Diagramme visuel représentant toutes les voies de désintégration d'une substance radioactive

### Transition isomère (Isomeric Transition)
- Le noyau formé par désintégration radioactive peut rester dans un état excité après la transformation, auquel cas il libère de l'énergie sous forme de rayons gamma (bien que l'émission de rayons gamma ne change pas le nucléide, on utilise parfois le terme de désintégration gamma par convention).
- La plupart des noyaux excités transitent vers l'état fondamental en émettant des rayons gamma en très peu de temps, mais dans certains cas, l'émission de rayons gamma est retardée, apparaissant comme un état métastable. Cet état retardé est appelé *état isomère (isomeric state)* du noyau.
- La transition de l'état isomère à l'état fondamental par émission de rayons gamma est appelée *transition isomère (isomeric transition)* et est notée IT.
![Schéma de désintégration de Au-198](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Source de l'image*
> - Auteur : Utilisateur Wikimedia britannique [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - Licence : Libre d'utilisation sans restriction pour tout usage, dans la mesure où cela ne contrevient pas à la loi