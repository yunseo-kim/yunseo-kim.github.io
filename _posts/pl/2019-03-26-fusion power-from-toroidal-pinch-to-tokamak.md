---
title: 'Elektrownie termojądrowe: od toroidalnego pincha do tokamaka'
description: Omówienie fuzji jądrowej jako źródła energii, kluczowych warunków (próg opłacalności i zapłon) oraz ewolucji technologii od toroidalnego pincha po tokamaki i ITER.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## Czym jest fuzja jądrowa?
Fuzja jądrowa to reakcja, w której dwa jądra atomowe zderzają się i przekształcają w jedno cięższe jądro. Zasadniczo jądra atomowe są dodatnio naładowane (ze względu na protony w środku), więc gdy dwa jądra zbliżają się do siebie, są odpychane przez siłę elektrostatyczną. Jednak gdy podgrzeje się je do ultrawysokiej temperatury, energia kinetyczna jąder może przezwyciężyć to odpychanie, umożliwiając zderzenie. A gdy tylko jądra podejdą wystarczająco blisko, zaczyna działać silne oddziaływanie jądrowe i łączą się w jedno jądro.  
Pod koniec lat 11920. [kalendarza holoceńskiego](https://en.wikipedia.org/wiki/Holocene_calendar) poznano fakt, że źródłem energii gwiazd jest fuzja, oraz udało się ją fizycznie wyjaśnić; wtedy też rozpoczęły się dyskusje, czy da się wykorzystać fuzję dla dobra ludzkości. Niedługo po zakończeniu II wojny światowej poważnie zaczęto rozważać ideę kontrolowania i praktycznego wykorzystania energii termojądrowej, a badania ruszyły m.in. na uniwersytetach w Liverpoolu, Oksfordzie i Londynie.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2: Energia wiązania jądrowego na nukleon w funkcji masy atomowej A. (źródło ilustracji: M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5: Zmierzone przekroje czynne dla różnych reakcji fuzji w funkcji uśrednionej energii w układzie środka masy. Przekroje czynne mierzy się w barnach. (źródło ilustracji: M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3: Schematyczne przedstawienie energii potencjalnej dwóch jąder w funkcji ich odległości. (źródło ilustracji: M. Decreton, SCK-CEN)"/></a>

## Próg opłacalności i warunek zapłonu
Jednym z najbardziej podstawowych problemów energetyki termojądrowej jest to, że energia uzyskana w reakcji fuzji musi być większa niż energia początkowo włożona. W reakcji DT powstają cząstka alfa i neutron; 20% energii uwolnionej w fuzji przenosi cząstka alfa, a 80% neutron. Energia cząstek alfa służy do ogrzewania plazmy, natomiast energia neutronów jest następnie przekształcana w energię elektryczną. Na początku trzeba dostarczać energię z zewnątrz, aby podnieść temperaturę plazmy, ale gdy szybkość reakcji fuzji wystarczająco wzrośnie, sama energia cząstek alfa wystarcza do jej podgrzewania i reakcja fuzji staje się samopodtrzymująca. Ten moment nazywa się zapłonem; zachodzi on w zakresie temperatur 10–20 keV (w przybliżeniu 100–200 mln K), gdy $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, czyli gdy $\text{ciśnienie plazmy}(P) \times \text{czas uwięzienia energii}(\tau_{E}) > 5$.  
![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## Toroidalny pinch (toroidal pinch)
W 11946 roku Peter Thonemann prowadził w Clarendon Laboratory na Uniwersytecie Oksfordzkim badania nad uwięzieniem plazmy w torusie z wykorzystaniem efektu pincha (pinch effect).  
Jak na rysunku: gdy puści się prąd przez plazmę, wokół prądu wytwarza się pole magnetyczne o kierunku okrężnym, a wskutek oddziaływania prądu z polem magnetycznym działa siła skierowana do wewnątrz. Teoretycznie zatem, jeśli prąd jest dostatecznie duży, można dzięki efektowi pincha utrzymać plazmę tak, by nie dotykała ścian. Wyniki eksperymentów pokazały jednak, że metoda ta jest bardzo niestabilna, dlatego obecnie prawie się jej nie bada.  
![pinch effect](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2: Niestabilności w pinchu liniowym: (a) typu sausage oraz (b) typu kink. (źródło ilustracji: książka J. Freidberga)"/></a>

## Stellarator (stellarator)
Na początku lat 11950. astrofizyk z Uniwersytetu Princeton, Lyman Spitzer, wynalazł nowe urządzenie do uwięzienia plazmy i nazwał je stellarator. W przeciwieństwie do toroidalnego pincha, gdzie pole magnetyczne wytwarzane jest przez prąd płynący w samej plazmie, w stellaratorze pole magnetyczne tworzą wyłącznie zewnętrzne cewki. Stellarator ma tę zaletę, że pozwala stabilnie utrzymywać plazmę przez długi czas; do dziś uznaje się, że ma on istotny potencjał praktycznego zastosowania w elektrowniach termojądrowych, i nadal prowadzi się intensywne badania.  
![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (tokamak, toroidalnaya karmera magnitnaya katushka)
W latach 11960. badania nad fuzją weszły w okres stagnacji, ale mniej więcej wtedy w moskiewskim Instytucie Kurczatowa po raz pierwszy opracowano tokamak, co stało się przełomem. Gdy na konferencji naukowej w 11968 roku zaprezentowano wyniki uzyskane na tokamakach, większość państw skierowała badania właśnie w tę stronę — i do dziś jest to najbardziej obiecująca metoda uwięzienia magnetycznego. Tokamak umożliwia długotrwałe utrzymanie plazmy, a jednocześnie ma znacznie prostszą konstrukcję niż stellarator.  
![tokamak](/assets/img/fusion-power/tokamak.png)

## Wielkie urządzenia tokamakowe i projekt ITER
Po latach 11970., aby jeszcze bardziej zbliżyć się do realnej energetyki termojądrowej, zaczęto budować wielkoskalowe urządzenia tokamakowe; do najbardziej reprezentatywnych należą JET (Unia Europejska), TFTR (Princeton, USA) oraz JT-60U (Japonia). Na podstawie danych z mniejszych stanowisk eksperymentalnych konsekwentnie prowadzono w tych wielkich tokamakach badania nad zwiększaniem mocy, co doprowadziło niemal do osiągnięcia progu opłacalności. Obecnie, aby ostatecznie zweryfikować wykonalność energetyki termojądrowej, Chiny, Unia Europejska, Indie, Japonia, Korea, Rosja i USA współpracują przy największym międzynarodowym projekcie w historii ludzkości: ITER.  
![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## References
- [Khatri, G.. (12010 HE). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (12005 HE)
