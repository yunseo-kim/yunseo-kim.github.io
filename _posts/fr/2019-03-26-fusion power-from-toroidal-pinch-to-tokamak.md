---
title: 'La fusion nucléaire : des pincements toroïdaux aux tokamaks'
description: Ce texte aborde le concept de fusion nucléaire, les raisons pour lesquelles
  elle est considérée comme une source d'énergie prometteuse pour l'avenir, les objectifs
  techniques à atteindre pour commercialiser l'énergie de fusion, ainsi que l'évolution
  des technologies de fusion, des pincements toroïdaux (toroidal pinch) à ITER.  L'auteur
  précise que cet essai a été rédigé pour une activité de club scientifique lorsqu'il
  était en deuxième année de lycée. Contrairement à ses autres articles, celui-ci
  est écrit dans un style plus familier, mais il a été téléchargé tel quel à des fins
  d'archivage.
categories: [Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## Qu'est-ce que la fusion nucléaire ?
La fusion nucléaire est une réaction dans laquelle deux noyaux atomiques entrent en collision pour former un noyau plus lourd. Fondamentalement, les noyaux atomiques ont une charge positive en raison des protons qu'ils contiennent, donc lorsque deux noyaux s'approchent l'un de l'autre, ils se repoussent en raison de la force électrostatique répulsive. Cependant, si les noyaux sont chauffés à des températures extrêmement élevées, leur énergie cinétique peut surmonter la répulsion électrique, permettant aux deux noyaux d'entrer en collision. Une fois que les deux noyaux sont suffisamment proches, l'interaction nucléaire forte entre en jeu et les fusionne en un seul noyau.

À la fin des années 1920, lorsqu'il a été découvert que la fusion nucléaire était la source d'énergie des étoiles et qu'elle pouvait être expliquée physiquement, des discussions ont commencé sur la possibilité d'utiliser la fusion nucléaire au profit de l'humanité. Peu après la fin de la Seconde Guerre mondiale, l'idée de contrôler et d'utiliser l'énergie de fusion a été sérieusement envisagée, et des recherches ont débuté dans des universités britanniques telles que l'Université de Liverpool, l'Université d'Oxford et l'Université de Londres.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## Le seuil de rentabilité et les conditions d'allumage
L'un des problèmes fondamentaux de la production d'énergie par fusion est que l'énergie produite par la réaction de fusion doit être supérieure à l'énergie initialement investie. Dans la réaction DT, des particules alpha et des neutrons sont produits, avec 20% de l'énergie libérée par la fusion portée par les particules alpha et 80% par les neutrons. L'énergie des particules alpha est utilisée pour chauffer le plasma, tandis que l'énergie des neutrons est convertie en énergie électrique. Au début, il faut fournir de l'énergie externe pour augmenter la température du plasma, mais une fois que le taux de réaction de fusion est suffisamment élevé, l'énergie des particules alpha seule peut maintenir le chauffage du plasma, permettant à la réaction de fusion de s'auto-entretenir. Ce point est appelé allumage, et il se produit dans une plage de température de 10 à 20 keV (environ 100 à 200 millions de K) lorsque $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, c'est-à-dire lorsque $\text{pression du plasma}(P) \times \text{temps de confinement de l'énergie}(\tau_{E}) > 5$.

![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## Le pincement toroïdal (toroidal pinch)
En 1946, Peter Thonemann a mené des recherches au laboratoire Clarendon de l'Université d'Oxford sur le confinement du plasma dans un tore en utilisant l'effet de pincement (pinch effect).

Comme le montre la figure, lorsqu'un courant est appliqué au plasma, un champ magnétique se forme autour du courant, et l'interaction entre le courant et le champ magnétique crée une force dirigée vers l'intérieur. Théoriquement, si le courant est suffisamment élevé, l'effet de pincement pourrait empêcher le plasma de toucher les parois. Cependant, les expériences ont montré que cette méthode était très instable, et elle n'est donc presque plus étudiée aujourd'hui.

![pinch effect](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## Le stellarator
Au début des années 1950, Lyman Spitzer, un astrophysicien de l'Université de Princeton, a inventé un nouveau dispositif de confinement du plasma qu'il a nommé stellarator. Contrairement au pincement toroïdal où le champ magnétique est créé par le courant circulant dans le plasma lui-même, dans un stellarator, le champ magnétique est uniquement généré par des bobines externes. Le stellarator présente l'avantage de pouvoir maintenir le plasma de manière stable sur de longues périodes, ce qui lui confère encore aujourd'hui un potentiel d'application réelle dans les centrales à fusion. Les recherches sur ce dispositif se poursuivent activement.

![stellarator](/assets/img/fusion-power/stellarator.png)

## Le tokamak (toroidalnaya karmera magnitnaya katushka)
Dans les années 1960, la recherche sur la fusion est entrée dans une période de stagnation. C'est à ce moment-là que l'Institut Kurchatov de Moscou a conçu le premier tokamak, ouvrant ainsi une nouvelle voie. Lors d'une conférence scientifique en 1968, les résultats du tokamak ont été présentés, ce qui a conduit la plupart des pays à réorienter leurs recherches vers cette technologie, devenue depuis la méthode de confinement magnétique la plus prometteuse. Le tokamak présente l'avantage de pouvoir maintenir le plasma sur de longues périodes tout en ayant une structure beaucoup plus simple que le stellarator.

![tokamak](/assets/img/fusion-power/tokamak.png)

## Les grands dispositifs tokamak et le projet ITER
Depuis les années 1970, de grands dispositifs tokamak ont été construits pour se rapprocher davantage de la production d'énergie par fusion nucléaire. Les plus représentatifs sont le JET de l'Union européenne, le TFTR de Princeton aux États-Unis, et le JT-60U au Japon. En augmentant constamment la puissance de ces grands tokamaks sur la base des données obtenues à partir de dispositifs expérimentaux à petite échelle, on a presque atteint le seuil de rentabilité. Actuellement, pour vérifier définitivement la faisabilité de la production d'énergie par fusion, la Chine, l'Union européenne, l'Inde, le Japon, la Corée, la Russie et les États-Unis collaborent au projet ITER, le plus grand projet international conjoint de l'humanité.

![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## Références
- [Khatri, G.. (2010). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken et Peter Stott, Fusion: The Energy of the Universe, Elsevier (2005)
