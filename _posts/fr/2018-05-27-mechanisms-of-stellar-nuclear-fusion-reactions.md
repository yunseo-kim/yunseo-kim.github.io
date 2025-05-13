---
title: Mécanismes de réaction de fusion nucléaire dans les étoiles
description: Cet article présente les réactions de fusion nucléaire qui se produisent dans le cœur des étoiles, notamment la chaîne proton-proton et le cycle carbone-azote-oxygène (CNO). Il s'agit d'un essai que j'ai rédigé en première année de lycée pour une activité de club scientifique, écrit dans un style plus conversationnel que mes autres articles et conservé tel quel à des fins d'archivage.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## La chaîne de réaction proton-proton (proton-proton chain reaction)
C'est la réaction de fusion nucléaire stellaire la plus connue du grand public. Le noyau du deutérium, appelé deutéron, est formé par la combinaison d'un proton (p) et d'un neutron (n). Par conséquent, pour que deux protons se combinent pour former un noyau de deutérium, l'un des protons doit se transformer en neutron. Comment un proton peut-il alors se transformer en neutron?

- La ‘[désintégration bêta](/posts/Nuclear-Stability-and-Radioactive-Decay/#d%C3%A9sint%C3%A9gration-b%C3%AAta-moins-beta--decay)’ est le processus par lequel un neutron ($n$) se transforme en proton ($p$) en émettant un électron ($e^{-}$) et un antineutrino électronique ($\overline{\nu_e}$). L'équation de réaction s'écrit : $n \rightarrow p + e^{-} + \overline{\nu_e}$.
- Le processus par lequel un proton ($p$) se transforme en neutron ($n$) est l'inverse de la désintégration bêta. On l'appelle donc ‘[désintégration bêta inverse](/posts/Nuclear-Stability-and-Radioactive-Decay/#d%C3%A9sint%C3%A9gration-b%C3%AAta-plus-beta-decay)’. À quoi ressemble l'équation de cette réaction? Il n'y a rien de spécial dans cette équation nucléaire. Il suffit d'échanger les positions du proton et du neutron, de remplacer l'électron par un positron et l'antineutrino par un neutrino. En équation, cela donne $p \rightarrow n + e^{+} + \nu_e$.

Après la formation du noyau de deutérium par ce processus, la réaction $^2_1D + p \rightarrow {^3_2He}$ produit un noyau d'hélium-3, puis finalement, deux noyaux d'hélium-3 entrent en collision pour former un noyau d'hélium-4 et deux protons.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

En réalité, il existe plusieurs voies de réaction pour la chaîne proton-proton. Le cas ci-dessus est le plus représentatif, mais il existe d'autres voies. Cependant, ces autres voies ne représentent pas une proportion significative dans les étoiles de masse inférieure à celle du Soleil, et dans les étoiles dont la masse est supérieure à 1,5 fois celle du Soleil, le cycle CNO que nous aborderons plus tard joue un rôle beaucoup plus important que la chaîne proton-proton, donc nous ne les traiterons pas séparément ici.

Cette chaîne de réaction proton-proton se produit principalement à des températures d'environ 10 à 14 millions de kelvins. Dans le cas du Soleil, dont la température centrale est d'environ 15 millions de kelvins, la chaîne pp représente 98,3% des réactions (le cycle CNO représentant les 1,3% restants).

## Le cycle carbone-azote-oxygène (CNO Cycle)
Le cycle CNO est une réaction où le carbone se transforme en azote en absorbant un proton, puis l'azote se transforme en oxygène en absorbant un autre proton, et ainsi de suite. Au final, après avoir absorbé 4 protons et produit un noyau d'hélium, le cycle revient au carbone. La caractéristique de ce cycle CNO est que le carbone, l'azote et l'oxygène jouent un rôle catalytique. Théoriquement, ce cycle CNO prédomine dans les étoiles dont la masse est supérieure à 1,5 fois celle du Soleil. La différence de réaction selon la masse stellaire réside dans la différence de dépendance à la température entre la chaîne proton-proton et le cycle CNO. La première commence à des températures relativement basses d'environ 4 millions de kelvins, et sa vitesse de réaction est proportionnelle à la puissance 4 de la température. En revanche, le second commence à environ 15 millions de kelvins mais est très sensible à la température (la vitesse de réaction est proportionnelle à la puissance 16 de la température), de sorte qu'à des températures supérieures à 17 millions de kelvins, le cycle CNO devient prédominant.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Source de l'image*
> - Auteur: Utilisateur Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - Licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Le cycle CNO présente également diverses voies. Il se divise principalement en cycle CNO à basse température (intérieur stellaire) et cycle CNO à haute température (novae, supernovae), et dans chaque cas, il existe encore trois ou quatre voies de réaction. J'aimerais traiter toutes les réactions du cycle CNO, mais cela nécessiterait plus d'espace que ce dont nous disposons ici, donc je ne traiterai que du cycle CN* le plus fondamental, c'est-à-dire le CNO-I.

> *La raison pour laquelle il est appelé cycle CN, sans le O, est qu'il n'existe pas d'isotope stable de l'oxygène dans ce processus de réaction.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Comme le montre l'image ci-dessus, le carbone, l'azote et l'oxygène circulent et jouent un rôle de catalyseur. Cependant, quelle que soit la voie de réaction, l'équation de réaction globale et la quantité totale d'énergie produite sont les mêmes.

## Pour aller plus loin
- Park Inkyu (Professeur de physique à l'Université de Séoul), [Naver Cast Physics Walk: Combien de neutrinos sont produits dans le Soleil?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipédia, [Chaîne proton-proton](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipédia, [Cycle CNO](https://en.wikipedia.org/wiki/CNO_cycle)
