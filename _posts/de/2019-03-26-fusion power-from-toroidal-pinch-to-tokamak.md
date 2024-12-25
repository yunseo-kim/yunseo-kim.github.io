---
title: 'Kernfusion: Von der toroidalen Einschnürung bis zum Tokamak'
description: Dieser Beitrag behandelt das Konzept der Kernfusion, die Gründe für ihr
  Interesse als zukünftige Energiequelle, die technischen Ziele für die kommerzielle
  Nutzung der Kernfusion und die Geschichte der Fusionsreaktortechnologie von der
  toroidalen Einschnürung bis zum ITER-Projekt. Der Autor weist darauf hin, dass dieser
  Essay ursprünglich für eine Schulaktivität in der 11. Klasse geschrieben wurde und
  daher in einem eher umgangssprachlichen Stil verfasst ist, der sich von anderen
  Beiträgen unterscheidet. Er wurde zu Archivierungszwecken unverändert hochgeladen.
categories: [Engineering Physics, Nuclear Engineering]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.png
---
## Was ist Kernfusion?

Kernfusion bezeichnet die Reaktion, bei der zwei Atomkerne zusammenstoßen und zu einem schwereren Atomkern verschmelzen. Grundsätzlich tragen Atomkerne aufgrund der Protonen in ihrem Inneren eine positive Ladung, sodass sich zwei Atomkerne bei Annäherung durch die elektrische Abstoßung gegenseitig abstoßen. Wenn die Atomkerne jedoch auf extrem hohe Temperaturen erhitzt werden, kann ihre kinetische Energie die elektrische Abstoßung überwinden, sodass die beiden Atomkerne kollidieren können. Sobald sich zwei Atomkerne ausreichend angenähert haben, wirkt die starke Kernkraft und verbindet sie zu einem einzigen Atomkern.

Ende der 1920er Jahre wurde bekannt, dass Kernfusion die Energiequelle der Sterne ist und physikalisch erklärt werden konnte. Daraufhin wurde diskutiert, ob Kernfusion zum Nutzen der Menschheit eingesetzt werden könnte. Kurz nach dem Ende des Zweiten Weltkriegs wurde ernsthaft in Betracht gezogen, Fusionsenergie zu kontrollieren und zu nutzen. Die Forschung begann an britischen Universitäten wie der Universität Liverpool, der Universität Oxford und der Universität London.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## Break-even-Punkt und Zündbedingung

Eine der grundlegendsten Herausforderungen bei der Kernfusion zur Energiegewinnung ist, dass die aus der Fusionsreaktion gewonnene Energie größer sein muss als die anfänglich zugeführte Energie. Bei der DT-Reaktion werden Alpha-Teilchen und Neutronen erzeugt, wobei 20% der durch Fusion freigesetzten Energie von den Alpha-Teilchen und 80% von den Neutronen getragen werden. Die Energie der Alpha-Teilchen wird zur Aufheizung des Plasmas verwendet, während die Energie der Neutronen in elektrische Energie umgewandelt wird. Anfangs muss von außen Energie zugeführt werden, um die Plasmatemperatur zu erhöhen, aber wenn die Fusionsreaktionsrate ausreichend ansteigt, kann das Plasma allein durch die Energie der Alpha-Teilchen aufgeheizt werden, sodass die Fusionsreaktion sich selbst aufrechterhält. Dieser Punkt wird als Zündung bezeichnet und tritt im Temperaturbereich von 10-20 keV (etwa 100-200 Millionen K) auf, wenn $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, d.h. wenn $\text{Plasmadruck}(P) \times \text{Energieeinschlusszeit}(\tau_{E}) > 5$ ist.

![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## Toroidale Einschnürung (Toroidal Pinch)

1946 führte Peter Thonemann am Clarendon Laboratory der Universität Oxford Forschungen durch, um Plasma in einem Torus unter Verwendung des Pinch-Effekts einzuschließen.

Wie in der Abbildung gezeigt, bildet sich ein Magnetfeld um den Strom herum, wenn Strom durch das Plasma fließt, und durch die Wechselwirkung zwischen Strom und Magnetfeld wirkt eine Kraft nach innen. Theoretisch könnte bei ausreichend hohem Strom der Pinch-Effekt das Plasma daran hindern, die Wände zu berühren. Experimente zeigten jedoch, dass diese Methode sehr instabil war und wird daher heute kaum noch erforscht.

![pinch effect](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## Stellarator

Anfang der 1950er Jahre erfand der Astrophysiker Lyman Spitzer von der Princeton University eine neue Plasmaeinschlussvorrichtung, die er Stellarator nannte. Im Gegensatz zur toroidalen Einschnürung, bei der das Magnetfeld durch den im Plasma selbst fließenden Strom erzeugt wird, wird das Magnetfeld im Stellarator ausschließlich durch externe Spulen erzeugt. Stellaratoren haben den Vorteil, dass sie das Plasma über lange Zeit stabil halten können. Sie werden immer noch als potenziell wertvoll für den praktischen Einsatz in Fusionskraftwerken angesehen und sind weiterhin Gegenstand aktiver Forschung.

![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (toroidalnaya karmera magnitnaya katushka)

In den 1960er Jahren geriet die Fusionsforschung in eine Sackgasse, bis das Kurtschatow-Institut in Moskau den ersten Tokamak entwickelte und damit einen Durchbruch erzielte. Nach der Präsentation der Tokamak-Ergebnisse auf einer Konferenz im Jahr 1968 richteten die meisten Länder ihre Forschung auf Tokamaks aus, die heute als vielversprechendste Methode des magnetischen Einschlusses gelten. Tokamaks haben den Vorteil, dass sie das Plasma über lange Zeit aufrechterhalten können und gleichzeitig eine viel einfachere Struktur als Stellaratoren aufweisen.

![tokamak](/assets/img/fusion-power/tokamak.png)

## Große Tokamak-Anlagen und das ITER-Projekt

Seit den 1970er Jahren wurden große Tokamak-Anlagen gebaut, um der praktischen Fusionsenergieerzeugung näher zu kommen. Die bekanntesten sind JET der Europäischen Union, TFTR in Princeton, USA, und JT-60U in Japan. Durch kontinuierliche Forschung zur Leistungssteigerung in diesen großen Tokamaks, basierend auf Daten aus kleineren Versuchsanlagen, wurde der Break-even-Punkt fast erreicht. Derzeit wird das ITER-Projekt, das größte internationale Gemeinschaftsprojekt der Menschheit, von China, der Europäischen Union, Indien, Japan, Korea, Russland und den USA durchgeführt, um die Machbarkeit der Fusionsenergie endgültig zu überprüfen.

![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## Literaturverzeichnis

- [Khatri, G.. (2010). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (2005)
