---
title: "Mechanismus termojaderných fúzních reakcí ve hvězdách"
description: "Představení fúze ve hvězdných jádrech: proton-protonový řetězec a CNO cyklus. Esej z 1. ročníku střední školy, zveřejněná pro archivaci."
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics, Nuclear Reaction, Fusion Power]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---

## Proton-protonový řetězec (proton-proton chain reaction)

Jde o nejznámější termojadernou fúzní reakci probíhající ve hvězdách. Jádro deuteria, deuteron (deuteron), vzniká spojením jednoho protonu (p) a jednoho neutronu (n). Aby se tedy proton a proton spojily a vytvořily deuteron, musí se jeden z těchto protonů změnit na neutron. Jak se ale může proton změnit na neutron?

- Proces, při němž se neutron ($n$) mění na proton ($p$) a vyzáří elektron ($e⁻$) a elektronové antineutrino ($\nu_e$), se nazývá „[β⁻ rozpad](/posts/Nuclear-Stability-and-Radioactive-Decay/#zaporny-beta-rozpadbeta--decay)“. Reakční rovnice je $n \rightarrow p + e^{-} + \overline{\nu_e}$. 
- Proces, při němž se proton ($p$) mění na neutron ($n$), odpovídá opačnému procesu k beta rozpadu. Proto se mu říká „[inverzní beta rozpad](/posts/Nuclear-Stability-and-Radioactive-Decay/#kladny-beta-rozpadbeta-decay)“. Jak pak vypadá rovnice inverzního beta rozpadu? Na jaderné reakční rovnici není nic zvláštního. Stačí prohodit role protonu a neutronu, elektron nahradit pozitronem a antineutrino neutrinem. Zapsáno jako $p \rightarrow n + e^{+} + \nu_e$.

Po vzniku deuteronového jádra uvedeným procesem vzniká z reakcí $^2_1D + p \rightarrow {^3_2He}$ jádro helia-3 a nakonec srážkou dvou jader helia-3 vzniká jádro helia-4 a dva protony.  
![p-p chain reaction](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)

Ve skutečnosti není reakční cesta proton-protonového řetězce jen jedna. Výše uvedený případ je nejtypičtější, ale existuje i několik dalších cest. Ostatní cesty však netvoří u hvězd s hmotností menší než Slunce příliš významný podíl a u hvězd s hmotností alespoň 1,5násobku Slunce naopak zaujímá mnohem větší podíl CNO cyklus, kterému se budu věnovat níže; proto je zde samostatně rozebírat nebudu.

Tento proton-protonový řetězec probíhá dominantně při teplotách zhruba 10–14 milionů K. V případě Slunce je teplota v centru přibližně 15 milionů K a pp řetězec tvoří 98,3 % (zbývajících 1,3 % připadá na CNO cyklus).

## Cyklická reakce uhlík–dusík–kyslík (CNO Cycle)

CNO cyklus je reakce, při níž uhlík zachytává proton a mění se na dusík, dusík následně zachytává proton a mění se na kyslík atd.; celkově se nakonec zachytí čtyři protony, uvolní se jedno helium a reakce se vrátí zpět k uhlíku. Charakteristické je, že uhlík, dusík a kyslík zde hrají roli podobnou katalyzátoru. Tento CNO cyklus teoreticky dominuje u hvězd s hmotností alespoň 1,5násobku hmotnosti Slunce. Rozdíl v převaze reakcí v závislosti na hmotnosti hvězdy souvisí s rozdílnou teplotní závislostí proton-protonového řetězce a CNO cyklu. První začíná už při relativně nízkých teplotách kolem 4 milionů K a rychlost reakce je úměrná čtvrté mocnině teploty. Druhý sice začíná kolem 15 milionů K, ale je na teplotě velmi citlivý (rychlost reakce je úměrná 16. mocnině teploty), takže při teplotách nad 17 milionů K začne převažovat CNO cyklus.

![Stellar Nuclear Energy Generation](https://upload.wikimedia.org/wikipedia/commons/5/5b/Nuclear_energy_generation.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [RJHall](https://commons.wikimedia.org/wiki/User:RJHall)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Také CNO cyklus má různé reakční cesty. Ve velkém se dělí na nízkoteplotní CNO cyklus (uvnitř hvězd) a vysokoteplotní CNO cyklus (novy, supernovy) a v každém případě pak existují další tři až čtyři reakční větve. Rád bych pokryl všechny CNO cykly, ale na takový rozsah by tento text nestačil, takže se zaměřím pouze na nejzákladnější CN cyklus*, tedy CNO-I.

> *Důvod, proč se používá označení CN cyklus (bez O), je ten, že v daném reakčním procesu neexistuje stabilní izotop kyslíku.
{: .prompt-info }

![CN Cycle](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

Jak je vidět na obrázku výše, uhlík, dusík a kyslík cyklují a fungují jako katalyzátor. Nezávisle na konkrétní reakční větvi je však celková reakční rovnice i celkové uvolněné množství energie stejné.

## Další čtení

- 박인규(Inkyu Park, profesor katedry fyziky na University of Seoul), [Naver Cast Fyzikální procházky: Kolik neutrin vzniká na Slunci?](https://terms.naver.com/entry.naver?docId=4125519&cid=58941&categoryId=58960)
- Wikipedie, [Proton-proton chain](https://en.wikipedia.org/wiki/Proton%E2%80%93proton_chain)
- Wikipedie, [CNO cycle](https://en.wikipedia.org/wiki/CNO_cycle)
