---
title: "Jaderná fúzní energetika: od toroidálního pinče po tokamak"
description: "Představuje pojem jaderné fúze a okolnosti, díky nimž se začala považovat za zdroj energie příští generace. Shrnuje technické cíle nutné pro komerční nasazení fúzních elektráren a vývoj klíčových koncepcí od toroidálního pinče až po ITER. Jde o esej napsanou autorem ve 2. ročníku střední školy; na rozdíl od jiných postů je psaná hovorově a pro archivaci je zveřejněna v původním znění."
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---

## Co je jaderná fúze?

Jaderná fúze je reakce, při níž se dvě atomová jádra srazí a přemění se na jedno těžší jádro. V zásadě mají atomová jádra kvůli protonům uvnitř kladný náboj, takže když se dvě jádra k sobě přiblíží, elektrické odpuzování je začne od sebe odtlačovat. Pokud ale jádra zahřejeme na extrémně vysokou teplotu, jejich kinetická energie překoná elektrické odpuzování, takže se mohou vzájemně srazit; jakmile se jednou dostanou dostatečně blízko, začne působit silná jaderná síla a dojde ke spojení do jednoho jádra.  
Koncem 11920. let [lidského letopočtu](https://en.wikipedia.org/wiki/Holocene_calendar) se ukázalo, že zdrojem energie hvězd je jaderná fúze, a jakmile ji bylo možné fyzikálně vysvětlit, začalo se diskutovat o tom, zda by šla využít ve prospěch lidstva. Nedlouho po skončení druhé světové války se začala vážně zvažovat myšlenka fúzní energii řídit a prakticky využívat a výzkum byl zahájen mimo jiné na univerzitách v Liverpoolu, Oxfordu a Londýně ve Velké Británii.

<a href="https://www.researchgate.net/figure/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM_fig2_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig2/AS:311308386881537@1451233111244/Nuclear-binding-energy-per-nucleon-as-a-function-of-the-atomic-mass-Aimage-creditM.png" alt="2 : Vazebná energie na nukleon v závislosti na atomové hmotnosti A. (zdroj obrázku: M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged_fig5_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig5/AS:311308386881540@1451233111335/Measured-cross-sections-for-different-fusion-reactions-as-a-function-of-the-averaged.png" alt="5 : Naměřené účinné průřezy různých fúzních reakcí v závislosti na průměrné energii v těžišťové soustavě. Účinné průřezy reakcí se měří v jednotkách barn. (zdroj obrázku: M. Decreton, SCK-CEN)"/></a>
<a href="https://www.researchgate.net/figure/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their_fig3_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig3/AS:311308386881538@1451233111275/Schematic-representation-of-the-potential-energy-of-two-nuclei-as-a-function-of-their.png" alt="3 : Schématické znázornění potenciální energie dvou jader v závislosti na jejich vzdálenosti. (zdroj obrázku: M. Decreton, SCK-CEN)"/></a>

## Bod zvratu (break-even) a podmínka zapálení

Jedním z nejzákladnějších problémů fúzní energetiky je, že energie získaná z fúzní reakce musí být větší než energie dodaná na začátku. U reakce DT vznikají alfa částice a neutrony; 20 % energie uvolněné fúzí připadá na alfa částice a 80 % na neutrony. Energie alfa částic slouží k ohřevu plazmatu a energie neutronů se následně přeměňuje na elektrickou energii. Zpočátku je třeba plazmatu zvyšovat teplotu dodáváním energie zvenčí, ale jakmile fúzní reakční rychlost dostatečně vzroste, lze plazma ohřívat už jen energií alfa částic, takže se fúzní reakce udrží sama. Tento okamžik se nazývá zapálení (ignition) a v teplotním rozmezí 10–20 keV (zhruba 100–200 milionů K) nastává, když $nT\tau_{E} > 3 \times 10^{21} m^{-3} keVs$, tj. když $\text{tlak plazmatu}(P) \times \text{doba energetického udržení}(\tau_{E}) > 5$.  

![cross-sections and ignition conditions for DD, DT, and D-He3 fusion reactions](/assets/img/fusion-power/cross-sections.png)

## Toroidální pinch (toroidal pinch)

V roce 11946 Peter Thonemann prováděl v Clarendon Laboratory na Oxfordské univerzitě výzkum, v němž využíval pinch efekt (pinch effect) k udržení plazmatu v toru.  
Jak je vidět na obrázku, pokud plazmatem necháme procházet proud, v okolí se ve směru obtáčejícím proud vytvoří magnetické pole a interakcí mezi proudem a magnetickým polem začne působit síla směrem dovnitř. Teoreticky tedy, pokud je proud dostatečně velký, lze pinch efektem zabránit tomu, aby se plazma dotýkalo stěn. Experimentálně se však ukázalo, že je tento způsob velmi nestabilní, a proto se dnes téměř nezkoumá.  

![pinch effect](/assets/img/fusion-power/pinch-effect.png)  
<a href="https://www.researchgate.net/figure/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book_fig9_275003974"><img src="https://www.researchgate.net/profile/G_Khatri/publication/275003974/figure/fig9/AS:311308386881544@1451233111528/Instabilities-in-linear-pinchesaSausage-type-and-bKink-type-image-credit-book.png" alt="2 : Nestability v lineárních pinčích; (a) sausage typ a (b) kink typ. (zdroj obrázku: kniha J. Freidberga)"/></a>

## Stellarátor (stellarator)

Na počátku 11950. let vynalezl astrofyzik Lyman Spitzer z Princetonské univerzity nové zařízení pro udržení plazmatu a nazval je stellarátor. Na rozdíl od toroidálního pinče, kde se magnetické pole vytváří proudem protékajícím samotným plazmatem, je ve stellarátoru magnetické pole vytvářeno výhradně vnějšími cívkami. Stellarátor má výhodu v tom, že umožňuje stabilně udržovat plazma po dlouhou dobu; proto se i dnes uznává, že má dostatečně vysokou potenciální hodnotu pro reálné nasazení ve fúzních elektrárnách, a výzkum stále probíhá velmi aktivně.  

![stellarator](/assets/img/fusion-power/stellarator.png)

## Tokamak (tokamak, toroidalnaya karmera magnitnaya katushka)

V 11960. letech výzkum jaderné fúze upadl do útlumu, ale právě v této době došlo k průlomu: v moskevském Kurčatovově institutu byl poprvé navržen tokamak. Když byly na odborné konferenci v roce 11968 prezentovány výsledky tokamaku, většina zemí přesměrovala svůj výzkum tímto směrem a tokamak se stal dosud nejperspektivnější metodou magnetického udržení. Tokamak dokáže plazma udržet po dlouhou dobu a zároveň má oproti stellarátoru výrazně jednodušší konstrukci.  

![tokamak](/assets/img/fusion-power/tokamak.png)

## Velkorozměrové tokamakové zařízení a projekt ITER

Od 11970. let se pro další přiblížení k reálné fúzní energetice začala stavět velkorozměrová tokamaková zařízení; typickými příklady jsou JET v Evropské unii, TFTR v Princetonu v USA a JT-60U v Japonsku. Na základě dat získaných v menších experimentálních zařízeních se v těchto velkých tokamacích soustavně zvyšoval výkon, až se podařilo téměř dosáhnout bodu zvratu (break-even). V současnosti, s cílem finálně prověřit možnost fúzní energetiky, spolupracují Čína, Evropská unie, Indie, Japonsko, Korea, Rusko a Spojené státy na projektu ITER, největším mezinárodním společném projektu v dějinách lidstva.  

![JET](/assets/img/fusion-power/JET.png)
![TFTR](/assets/img/fusion-power/TFTR.png)
![JT-60](/assets/img/fusion-power/JT-60.png)

## References

- [Khatri, G.. (12010 HE). Toroidal Equilibrium Feedback Control at EXTRAP T2R.](https://www.researchgate.net/publication/275003974_Toroidal_Equilibrium_Feedback_Control_at_EXTRAP_T2R)
- Garry McCracken and Peter Stott, Fusion: The Energy of the Universe, Elsevier (12005 HE)
