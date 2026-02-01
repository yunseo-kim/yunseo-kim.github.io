---
title: Spojité a charakteristické X záření (Continuous and Characteristic X Rays)
description: Dvěma způsoby vzniku atomového X záření a tomu odpovídajícími vlastnostmi brzdného (bremsstrahlung) a charakteristického X záření.
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Atomic Radiation, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## TL;DR
> - **bremsstrahlung (brzdné záření, braking radiation)**: spojité spektrum X záření vyzařované při průletu nabité částice (např. elektronu) v blízkosti atomového jádra, kdy je částice urychlována elektrickou přitažlivostí
> - minimální vlnová délka: $\lambda_\text{min} = \cfrac{hc}{E_\text{max}} = \cfrac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}$
> - **charakteristické X záření (characteristic X-ray)**: nespojité spektrum X záření, které vzniká, když dopadající elektron ionizuje atom vyražením elektronu z vnitřní slupky; následně elektron z vnější slupky přejde na uvolněné místo a vyzáří foton s energií rovnou rozdílu dvou energetických hladin
{: .prompt-info }

## Prerequisites
- [Subatomární částice a složky atomu](/posts/constituents-of-an-atom/)

## Objev X záření
Röntgen objevil, že při ozáření terče elektronovým svazkem vzniká X záření. V době objevu ještě nebylo známo, že jde o elektromagnetické vlnění, a proto bylo pojmenováno **X záření (X-ray)** ve smyslu „neznámé“ povahy; také se mu říká **Röntgenovo záření (Röntgen radiation)** podle jména objevitele.

![X-ray Tube](https://upload.wikimedia.org/wikipedia/commons/7/72/WaterCooledXrayTube.svg)

Výše uvedený obrázek schematicky ukazuje typickou konstrukci rentgenky (X-ray tube). Uvnitř rentgenky jsou ve vakuu hermeticky uzavřeny katoda tvořená wolframovým vláknem a anoda, na níž je upevněn terč. Při přiložení vysokého napětí řádu desítek kV mezi elektrody jsou z katody emitovány elektrony, které dopadají na terč anody, a z něj se vyzařuje X záření. Účinnost přeměny energie na X záření je však obvykle pod 1 % a zbývajících více než 99 % energie se mění na teplo, takže je třeba přidat samostatné zařízení pro chlazení.

## bremsstrahlung (brzdné záření, braking radiation)
Když nabitá částice, například elektron, proletí v blízkosti atomového jádra, její trajektorie se vlivem elektrické přitažlivosti mezi částicí a jádrem prudce zakřiví a částice se současně zpomalí; přitom vyzáří energii ve formě X záření. Protože přeměna energie v tomto procesu není kvantována, má vyzářené X záření spojité spektrum; tento jev se nazývá **bremsstrahlung** neboli **brzdné záření (braking radiation)**.

![Bremsstrahlung](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bremsstrahlung.svg)

Energie fotonu X záření vyzářeného bremsstrahlungem samozřejmě nemůže překročit kinetickou energii dopadajícího elektronu. Proto existuje minimální vlnová délka vyzářeného X záření, kterou lze jednoduše získat ze vztahu

$$ \lambda_\text{min} = \frac{hc}{E}. \tag{1}$$

Protože Planckova konstanta $h$ i rychlost světla $c$ jsou konstanty, je tato minimální vlnová délka určena pouze energií dopadajícího elektronu. Vlnová délka $\lambda$ odpovídající energii $1\text{eV}$ je přibližně $1.24 \mu\text{m}=12400\text{Å}$. Proto minimální vlnová délka $\lambda_\text{min}$ při přiložení napětí $V$ voltů na rentgenku vychází takto; v praxi se často používá právě tento tvar:

$$ \lambda_\text{min} \text{[Å]} = \frac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}. \label{eqn:lambda_min}\tag{2}$$

Následující graf ukazuje spojité spektrum X záření při změně napětí za současného udržení konstantního proudu rentgenkou. S rostoucím napětím se minimální vlnová délka $\lambda_{\text{min}}$ zkracuje a celková intenzita X záření roste.

![Typical continuous X-ray spectra from tube operating
at three different peak voltages with the same current](/assets/img/continuous-and-characteristic-x-rays/bremsstrahlung.png)

## Charakteristické X záření (characteristic X-ray)
Je-li napětí na rentgence dostatečně vysoké, může dopadající elektron při srážce s elektronem ve vnitřní slupce atomu terče tento atom ionizovat. Elektron z vnější slupky pak rychle vyzáří energii a zaplní vzniklé volné místo ve vnitřní slupce; přitom vznikne foton X záření s energií rovnou rozdílu těchto dvou energetických hladin. Spektrum X záření vyzářeného tímto procesem je nespojité, je určeno vlastními energetickými hladinami atomu terče a je nezávislé na energii či intenzitě dopadajícího elektronového svazku. Tomuto záření se říká **charakteristické X záření (characteristic X-ray)**.

### Siegbahnovo značení (Siegbahn notation)

![Siegbahn notation of electron transitions between shells](https://upload.wikimedia.org/wikipedia/commons/f/f6/CharacteristicRadiation.svg)
> *Zdroj obrázku*
> - autor: uživatel anglické Wikipedie [HenrikMidtiby](https://en.wikipedia.org/wiki/User:HenrikMidtiby)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Podle Siegbahnova značení se X záření vyzařované při zaplnění vakance ve slupce K elektronem ze slupky L, M, ... označuje, jak je ukázáno na obrázku, jako $K_\alpha$, $K_\beta$, ... . Po zavedení moderního atomového modelu se však ukázalo, že u víceelektronových atomů se energetické hladiny liší i uvnitř jedné „slupky“ Bohrůvova modelu (tj. v rámci hladin se stejným hlavním kvantovým číslem) v závislosti na dalších kvantových číslech. Proto se i pro $K_\alpha$, $K_\beta$, ... zavedly jemnější podtřídy jako $K_{\alpha_1}$, $K_{\alpha_2}$, ... . 

![Siegbahn notation](/assets/img/continuous-and-characteristic-x-rays/siegbahn-notation.png)

Toto tradiční značení se dodnes ve spektroskopii stále široce používá. Protože však není systematické a často vede k nejasnostem, doporučuje *Mezinárodní unie pro čistou a užitou chemii (IUPAC)* používat následující alternativní značení.

### Značení IUPAC (IUPAC notation)
Standardní značení atomových orbitalů a charakteristického X záření doporučované IUPAC je následující. Nejprve se jednotlivým atomovým orbitalům přiřadí názvy podle tabulky níže.

| $n$(hlavní kvantové číslo) | $l$(orbitalové kvantové číslo) | $s$(spinové kvantové číslo) | $j$(kvantové číslo celkového momentu hybnosti) | atomový orbital | značení X záření |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $0$ | $\pm1/2$ | $1/2$ | $1s_{1/2}$ | $K_{(1)}$ |
| $2$ | $0$ | $\pm1/2$ | $1/2$ | $2s_{1/2}$ | $L_1$ |
| $2$ | $1$ | $-1/2$ | $1/2$ | $2p_{1/2}$ | $L_2$ |
| $2$ | $1$ | $+1/2$ | $3/2$ | $2p_{3/2}$ | $L_3$ |
| $3$ | $0$ | $\pm1/2$ | $1/2$ | $3s_{1/2}$ | $M_1$ |
| $3$ | $1$ | $-1/2$ | $1/2$ | $3p_{1/2}$ | $M_2$ |
| $3$ | $1$ | $+1/2$ | $3/2$ | $3p_{3/2}$ | $M_3$ |
| $3$ | $2$ | $-1/2$ | $3/2$ | $3d_{3/2}$ | $M_4$ |
| $3$ | $2$ | $+1/2$ | $5/2$ | $3d_{5/2}$ | $M_5$ |
| $4$ | $0$ | $\pm1/2$ | $1/2$ | $4s_{1/2}$ | $N_1$ |
| $4$ | $1$ | $-1/2$ | $1/2$ | $4p_{1/2}$ | $N_2$ |
| $4$ | $1$ | $+1/2$ | $3/2$ | $4p_{3/2}$ | $N_3$ |
| $4$ | $2$ | $-1/2$ | $3/2$ | $4d_{3/2}$ | $N_4$ |
| $4$ | $2$ | $+1/2$ | $5/2$ | $4d_{5/2}$ | $N_5$ |
| $4$ | $3$ | $-1/2$ | $5/2$ | $4f_{5/2}$ | $N_6$ |
| $4$ | $3$ | $+1/2$ | $7/2$ | $4f_{7/2}$ | $N_7$ |

> Celkové kvantové číslo momentu hybnosti $j=\|l+s\|$.
{: .prompt-info }

A charakteristické X záření vyzářené při přechodu elektronu z určité energetické hladiny na nižší hladinu se označuje podle následujícího pravidla:

$$ \text{(značení X záření pozdější hladiny)-(značení X záření původní hladiny)} $$

Například charakteristické X záření vyzářené při přechodu elektronu z orbitalu $2p_{1/2}$ do $1s_{1/2}$ lze označit jako $\text{K-L}_2$.

## Spektrum X záření

![Spectrum of the X-rays emitted by an X-ray tube with a rhodium target, operated at 60 kV](https://upload.wikimedia.org/wikipedia/commons/2/23/TubeSpectrum-en.svg)

Výše je spektrum X záření vyzařovaného při ozáření terče z rhodia (Rh) elektronovým svazkem urychleným na 60 kV. Je patrná hladká spojitá křivka odpovídající bremsstrahlungu a podle vztahu ($\ref{eqn:lambda_min}$) lze ověřit, že X záření je vyzařováno pouze pro vlnové délky přibližně $\ge 0.207\text{Å} = 20.7\text{pm}$. Ostré „špičky“ v grafu jsou způsobeny charakteristickým X zářením slupky K atomu rhodia. Jak bylo zmíněno, protože každý terčový prvek má vlastní charakteristické spektrum, lze z měření vlnových délek, na nichž se ve spektru objevují spiky, určit, z jakých prvků se terč skládá.

> Kromě $K_\alpha, K_\beta, \dots$ se samozřejmě vyzařuje i X záření nižších energií, jako $L_\alpha, L_\beta, \dots$. Ta však mají mnohem nižší energii a obvykle jsou pohlcena v krytu (housing) rentgenky, takže se nedostanou až k detektoru.
{: .prompt-info }
