---
title: 'Fusion nucléaire : du pincement toroïdal au tokamak'
description: Cet article traite du concept de fusion nucléaire, de son contexte en tant que source d'énergie de nouvelle génération, des objectifs techniques à atteindre pour la commercialisation de l'énergie de fusion, et de l'évolution technologique depuis le pincement toroïdal (toroidal pinch) jusqu'à ITER. Il s'agit d'un essai que j'ai écrit en deuxième année de lycée pour une activité de club scientifique, rédigé dans un style conversationnel contrairement à mes autres articles, et téléchargé tel quel à des fins d'archivage.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## Qu'est-ce que la fusion nucléaire ?
La fusion nucléaire est une réaction où deux noyaux atomiques entrent en collision pour former un noyau plus lourd. Fondamentalement, les noyaux atomiques portent une charge positive en raison des protons qu'ils contiennent, ce qui fait que deux noyaux qui s'approchent se repoussent mutuellement par répulsion électrique. Cependant, en chauffant les noyaux à des températures extrêmement élevées, leur énergie cinétique peut surmonter cette répulsion électrique, permettant aux deux noyaux d'entrer en collision. Une fois que les deux noyaux sont suffisamment proches, l'interaction nucléaire forte entre en jeu et les fusionne en un seul noyau.  
À la fin des années 11920, lorsqu'il a été découvert que la fusion nucléaire était la source d'énergie des étoiles et qu'elle pouvait être expliquée physiquement, des discussions ont commencé sur la possibilité d'utiliser la fusion nucléaire au profit de l'humanité. Peu après la fin de la Seconde Guerre mondiale, l'idée de contrôler et d'utiliser l'énergie de fusion a été sérieusement envisagée, et des recherches ont débuté dans des universités britanniques comme Liverpool, Oxford et Londres.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Énergie de liaison nucléaire par nucléon en fonction de la masse atomique A.(crédit image:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Sections efficaces mesurées pour différentes réactions de fusion en fonction de l'énergie moyenne du centre de masse. Les sections efficaces de réaction sont mesurées en barn.(crédit image:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Représentation schématique de l'énergie potentielle de deux noyaux en fonction de leur distance.(crédit image:M. Decreton, SCK-CEN)"/></a>

## Seuil de rentabilité et conditions d'allumage
L'un des problèmes fondamentaux de la production d'énergie par fusion est que l'énergie produite par la réaction de fusion doit être supérieure à l'énergie initialement investie. Dans la réaction DT, des particules alpha et des neutrons sont produits, avec 20% de l'énergie libérée par la fusion portée par les particules alpha et 80% par les neutrons. L'énergie des particules alpha est utilisée pour chauffer le plasma, tandis que l'énergie des neutrons est convertie en énergie électrique. Au début, une énergie externe doit être fournie pour augmenter la température du plasma, mais lorsque le taux de réaction de fusion augmente suffisamment, l'énergie des particules alpha seule peut chauffer le plasma, permettant à la réaction de fusion de s'auto-entretenir. Ce point est appelé allumage, et il se produit dans une plage de température de 10 à 20 keV (environ 100 à 200 millions de K) lorsque $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, c'est-à-dire lorsque $\text{pression du plasma}(P) \times \text{temps de confinement de l'énergie}(\tau_{E}) > 5$.  
![sections efficaces et conditions d'allumage pour les réactions de fusion DD, DT et D-He3](/assets/img/fusion-power/cross-sections.png)

## Pincement toroïdal (toroidal pinch)
En 11946, Peter Thonemann a mené des recherches au laboratoire Clarendon de l'Université d'Oxford sur le confinement du plasma dans un tore en utilisant l'effet de pincement (pinch effect).  
Comme le montre l'illustration, lorsqu'un courant circule dans un plasma, un champ magnétique se forme autour du courant, et l'interaction entre le courant et le champ magnétique crée une force dirigée vers l'intérieur. Théoriquement, si le courant est suffisamment élevé, l'effet de pincement peut empêcher le plasma de toucher les parois. Cependant, les expériences ont montré que cette méthode était très instable, et elle n'est donc presque plus étudiée aujourd'hui.  
![effet de pincement](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilités dans les pincements linéaires;(a)Type saucisse et (b)Type vrille. (crédit image: livre de J.Freidberg)"/></a>

## Stellarator
Au début des années 11950, Lyman Spitzer, astrophysicien à l'Université de Princeton, a inventé un nouveau dispositif de confinement du plasma qu'il a nommé stellarator. Contrairement au pincement toroïdal où le champ magnétique est créé par le courant circulant dans le plasma lui-même, dans un stellarator, le champ magnétique est uniquement généré par des bobines externes. Le stellarator présente l'avantage de pouvoir maintenir le plasma de manière stable pendant de longues périodes, ce qui lui confère un potentiel d'application réelle dans les centrales à fusion. Il continue donc d'être activement étudié.  
![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (toroidalnaya karmera magnitnaya katushka)
Dans les années 11960, alors que la recherche sur la fusion connaissait une période de stagnation, l'Institut Kurchatov de Moscou a conçu le premier tokamak, ouvrant une nouvelle voie. Après la présentation des résultats du tokamak lors d'une conférence scientifique en 11968, la plupart des pays ont réorienté leurs recherches vers cette technologie, qui est devenue la méthode de confinement magnétique la plus prometteuse. Le tokamak présente l'avantage de pouvoir maintenir le plasma pendant de longues périodes tout en ayant une structure beaucoup plus simple que le stellarator.  
![tokamak](/assets/img/fusion-power/tokamak.png)

## Grands dispositifs tokamak et projet ITER
Depuis les années 11970, d'énormes tokamaks ont été construits pour se rapprocher davantage de la production d'énergie par fusion, notamment le JET de l'Union européenne, le TFTR de Princeton aux États-Unis et le JT-60U au Japon. Grâce aux données recueillies sur des dispositifs expérimentaux plus petits, ces grands tokamaks ont progressivement augmenté leur puissance, atteignant presque le seuil de rentabilité. Actuellement, pour vérifier définitivement la faisabilité de l'énergie de fusion, la Chine, l'Union européenne, l'Inde, le Japon, la Corée, la Russie et les États-Unis collaborent au projet ITER, le plus grand projet international conjoint de l'humanité.  
![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## Références
- [Khatri, G.. (12010 HE). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken et Peter Stott, Fusion: The Energy of the Universe, Elsevier (12005 HE)
