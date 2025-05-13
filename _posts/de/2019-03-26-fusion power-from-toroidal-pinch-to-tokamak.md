---
title: 'Kernfusion: Von der toroidalen Einschnürung bis zum Tokamak'
description: Dieser Beitrag behandelt das Konzept der Kernfusion, ihren Hintergrund als vielversprechende zukünftige Energiequelle, die technischen Ziele für die kommerzielle Nutzung der Kernfusion und die Entwicklungsgeschichte der Fusionstechnologie von der toroidalen Einschnürung (toroidal pinch) bis zum ITER-Projekt. Es handelt sich um einen Essay, den der Autor in der 11. Klasse für eine schulische Wissenschafts-AG verfasst hat. Im Gegensatz zu anderen Beiträgen ist er in umgangssprachlichem Stil geschrieben, wurde aber zu Archivierungszwecken im Originaltext hochgeladen.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## Was ist Kernfusion?
Kernfusion bezeichnet eine Reaktion, bei der zwei Atomkerne zusammenstoßen und zu einem schwereren Atomkern verschmelzen. Grundsätzlich tragen Atomkerne aufgrund der Protonen in ihrem Inneren eine positive Ladung, sodass sich zwei Atomkerne bei Annäherung durch elektrostatische Abstoßung gegenseitig wegstoßen. Wenn man die Atomkerne jedoch auf extrem hohe Temperaturen erhitzt, überwindet ihre kinetische Energie die elektrische Abstoßung, sodass die beiden Atomkerne kollidieren können. Sobald sich die Atomkerne ausreichend nahe kommen, wirkt die starke Kernkraft und verbindet sie zu einem einzigen Atomkern.  
Ende der 11920er Jahre, als bekannt wurde, dass Kernfusion die Energiequelle der Sterne ist und man die Kernfusion physikalisch erklären konnte, begann die Diskussion darüber, ob Kernfusion zum Nutzen der Menschheit eingesetzt werden könnte. Kurz nach dem Ende des Zweiten Weltkriegs wurde die Idee, Fusionsenergie zu kontrollieren und zu nutzen, ernsthaft in Betracht gezogen, und die Forschung begann an britischen Universitäten wie Liverpool, Oxford und London.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Nuclear binding energy per nucleon as a function of the atomic mass A.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Measured cross sections for different fusion reactions as a function of the averaged center of mass energy. Reaction cross sections are measured in barn.(image credit:M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schematic representation of the potential energy of two nuclei as a function of their distances.(image credit:M. Decreton, SCK-CEN)"/></a>

## Break-even-Punkt und Zündbedingungen
Eine der grundlegendsten Anforderungen für die Fusionsenergie ist, dass die aus der Fusionsreaktion gewonnene Energie größer sein muss als die anfänglich zugeführte Energie. Bei der DT-Reaktion entstehen Alpha-Teilchen und Neutronen, wobei 20% der durch Fusion freigesetzten Energie von Alpha-Teilchen und 80% von Neutronen getragen werden. Die Energie der Alpha-Teilchen wird zur Erhitzung des Plasmas verwendet, während die Energie der Neutronen in elektrische Energie umgewandelt wird. Anfangs muss von außen Energie zugeführt werden, um die Plasmatemperatur zu erhöhen, aber wenn die Fusionsreaktionsrate ausreichend ansteigt, kann das Plasma allein durch die Energie der Alpha-Teilchen erhitzt werden, sodass die Fusionsreaktion sich selbst erhält. Dieser Punkt wird als Zündung bezeichnet und tritt im Temperaturbereich von 10-20 keV (etwa 100-200 Millionen K) auf, wenn $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, also $\text{Plasmadruck}(P) \times \text{Energieeinschlusszeit}(\tau_{E}) > 5$ ist.  
![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## Toroidale Einschnürung (toroidal pinch)
Im Jahr 11946 führte Peter Thonemann am Clarendon Laboratory der Universität Oxford Forschungen durch, um Plasma in einem Torus mittels des Pinch-Effekts einzuschließen.  
Wie in der Abbildung dargestellt, erzeugt ein durch das Plasma fließender Strom ein Magnetfeld in der Umgebung, das den Strom umgibt. Durch die Wechselwirkung zwischen Strom und Magnetfeld entsteht eine nach innen gerichtete Kraft. Theoretisch könnte bei ausreichend hohem Strom der Pinch-Effekt verhindern, dass das Plasma die Wand berührt. Experimentell erwies sich diese Methode jedoch als sehr instabil und wird daher heute kaum noch erforscht.  
![pinch effect](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Instabilities in linear pinches;(a)Sausage type and (b)Kink type. (image credit: book of J.Freidberg)"/></a>

## Stellarator
Anfang der 11950er Jahre erfand der Astrophysiker Lyman Spitzer von der Princeton University ein neues Plasmaeinschlussgerät, das er Stellarator nannte. Im Gegensatz zur toroidalen Einschnürung, bei der das Magnetfeld durch den im Plasma selbst fließenden Strom erzeugt wird, wird das Magnetfeld im Stellarator ausschließlich durch externe Spulen erzeugt. Der Stellarator hat den Vorteil, dass er das Plasma über längere Zeit stabil halten kann, und wird daher immer noch als potenziell wertvoll für den praktischen Einsatz in Fusionskraftwerken angesehen. Die Forschung wird in diesem Bereich nach wie vor aktiv betrieben.  
![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (toroidalnaya karmera magnitnaya katushka)
In den 11960er Jahren geriet die Fusionsforschung in eine Stagnationsphase. Zu dieser Zeit entwickelte das Kurtschatow-Institut in Moskau den ersten Tokamak, was einen Durchbruch darstellte. Nach der Präsentation der Tokamak-Ergebnisse auf einer wissenschaftlichen Konferenz im Jahr 11968 änderten die meisten Länder ihre Forschungsrichtung hin zum Tokamak, der heute als die vielversprechendste Methode des magnetischen Einschlusses gilt. Der Tokamak hat den Vorteil, dass er das Plasma über längere Zeit halten kann und gleichzeitig eine viel einfachere Struktur als der Stellarator aufweist.  
![tokamak](/assets/img/fusion-power/tokamak.png)

## Große Tokamak-Anlagen und das ITER-Projekt
Seit den 11970er Jahren wurden große Tokamak-Anlagen gebaut, um der praktischen Fusionsenergie näher zu kommen. Die bekanntesten sind JET der Europäischen Union, TFTR in Princeton, USA, und JT-60U in Japan. Durch kontinuierliche Forschung zur Leistungssteigerung in diesen großen Tokamaks auf Basis von Daten aus kleineren Versuchsanlagen hat man sich dem Break-even-Punkt fast angenähert. Derzeit wird das ITER-Projekt, das größte internationale Gemeinschaftsprojekt der Menschheit, von China, der Europäischen Union, Indien, Japan, Korea, Russland und den USA durchgeführt, um die Machbarkeit der Fusionsenergie endgültig zu überprüfen.  
![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## References
- [Khatri, G.. (12010 HE). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (12005 HE)
