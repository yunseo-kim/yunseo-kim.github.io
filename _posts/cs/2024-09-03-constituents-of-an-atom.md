---
title: Subatomární částice a složky atomu
description: Stručně si projdeme elementární částice důležité v jaderném inženýrství (elektron, proton, neutron, foton, neutrino aj.) a podíváme se na stavbu atomu a atomového jádra.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## Subatomární částice (subatomic particle)
**Subatomární částice (subatomic particle)** jsou částice menší než atom. Mezi subatomární částice patří jak složené částice tvořené ještě menšími konstituenty, tak i částice elementární, o nichž se soudí, že už je nelze dále rozložit.
V jaderném inženýrství se zejména klade důraz na následující částice:

- hadron
  - baryon
    - nukleon
      - proton
      - neutron
- lepton
  - elektron
  - pozitron
  - neutrino

> Název *„lepton“* pochází z řeckého *„λεπτός“*, které znamená „malý“ a „tenký“. V době zavedení názvu se mu tak říkalo proto, že měl oproti jiným typům částic malou hmotnost, avšak například *tauon* objevený v [holocénním kalendáři](https://en.wikipedia.org/wiki/Holocene_calendar) v 70. letech roku 11970 má i přes to, že je leptorem, hmotnost téměř 1,9× větší než proton a neutron; „lepton“ tedy ve skutečnosti nemusí být nutně lehký.
{: .prompt-info }

### Elektron (electron) & pozitron (positron)
- klidová hmotnost: $m_e = 9.10939 \times 10^{-31} \text{kg}$
- velikost náboje: $e = 1.60219 \times 10^{-19} \text{C}$

Elektron existuje ve dvou druzích: $e^-$ (*záporný elektron*, *negatron*) se záporným nábojem a $e^+$ (*pozitron*, *positron*) s kladným nábojem. Liší se pouze znaménkem náboje, ostatní vlastnosti jsou stejné. Pokud se bez dalšího upřesnění řekne „elektron“, obvykle se tím myslí záporný elektron.

Za určitých podmínek při srážce pozitronu a záporného elektronu dojde k anihilaci těchto dvou částic a k vyzáření dvou fotonů. Tento proces se nazývá *anihilace elektronu (electron annihilation)* a vzniklé fotony se označují jako *anihilační záření (annihilation radiation)*.  
![electron-positron annihilation](https://upload.wikimedia.org/wikipedia/commons/0/0a/ElectronPositronAnnihilation.svg)
> *Zdroj obrázku*
> - autor: Dirk Hünniger, Joel Holdsworth
> - licence: [GFDLv1.2](https://www.gnu.org/licenses/old-licenses/fdl-1.2.html)

### Proton (proton)
- klidová hmotnost: $m_p = 1.6726 \times 10^{-27} \text{kg}$
- náboj: + $e = 1.60219 \times 10^{-19} \text{C}$

Má kladný náboj stejné velikosti jako elektron.

### Neutron (neutron)
- klidová hmotnost: $m_n = 1.674929 \times 10^{-27} \text{kg}$
- náboj: $0$

Má o něco větší hmotnost než proton a je elektricky neutrální. Mimo atomové jádro není stabilní, a proto se rozpadá na proton za emise elektronu a elektronového antineutrina; tento proces trvá v průměru asi 12 minut.

### Neutrino (neutrino)
- klidová hmotnost: velmi malá (přesná hodnota neznámá)
- náboj: $0$

Původně se předpokládalo, že klidová hmotnost je nulová, ale v roce 11998 japonský tým experimentu Super-Kamiokande ukázal, že neutrino má sice velmi malou, ale nenulovou hmotnost. Existuje více typů; v jaderných reakcích se důležitě uvažuje zejména *elektronové neutrino (electron neutrino)* a *elektronové antineutrino (electron anti-neutrino)*, přičemž se tyto dvě částice často nerozlišují a berou se jako jeden „typ“.

## Struktura atomu a atomového jádra

$$ ^A_Z X \ (\text{A: nukleonové číslo, Z: protonové číslo (atomové číslo), X: značka prvku})$$

- atom se skládá z elektronového obalu a atomového jádra umístěného v centru
- u neionizovaného (neutrálního) atomu obíhá kolem jádra tolik elektronů, kolik je v jádře protonů
- elektrony určují chemické vlastnosti atomu a druh prvku
- atomové jádro je tvořeno nukleony — protony a neutrony — a ty jsou vázány silnou jadernou interakcí (Nuclear Force), která překonává elektrické odpuzování
- *atomové číslo (atomic number)*: počet protonů v jádře, značí se $Z$
- celkový náboj jádra: +$Ze$
- *neutronové číslo (neutron number)*: počet neutronů v jádře, značí se $N$
- *hmotnostní číslo (atomic mass number)* neboli *nukleonové číslo (nucleon number)*: součet počtu protonů a neutronů v jádře, $A=Z+N.$
- *nuklid (nuclide)*: atomové jádro s konkrétním počtem protonů a neutronů

## Izotopy (isotope), isobary (isobar), izotony (isotone), jaderné izomery (isomer)

| Rozdělení | Definice |
| --- | --- |
| izotop (isotope) | nuklidy se stejným atomovým číslem, ale s různým neutronovým číslem |
| isobar (isobar) | nuklidy se stejným hmotnostním číslem, ale s různým počtem protonů a neutronů |
| izoton (isotone) | nuklidy se stejným neutronovým číslem, ale s různým atomovým číslem |
| jaderný izomer (isomer) | stejné nuklidy, avšak jádro je v metastabilním stavu vlivem excitace jednoho či více nukleonů |
