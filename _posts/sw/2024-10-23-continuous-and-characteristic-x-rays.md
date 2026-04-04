---
title: Miale-X Endelevu na Miale-X Tabia (Continuous and Characteristic X Rays)
description: Tunachunguza kanuni mbili za kuzalishwa kwa miale-X inayohusiana na mionzi ya atomiki, pamoja na sifa za bremsstrahlung na miale-X tabia zinazotokana nazo.
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Atomic Radiation, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## TL;DR
> - **bremsstrahlung (mionzi ya kusimama, braking radiation)**: miale-X yenye spektra endelevu inayotolewa wakati chembe yenye chaji kama elektroni inapopita karibu na kiini cha atomu na kuharakishwa na mvuto wa umeme
> - Urefu mdogo kabisa wa wimbi: $\lambda_\text{min} = \cfrac{hc}{E_\text{max}} = \cfrac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}$
> - **miale-X tabia (characteristic X-ray)**: miale-X yenye spektra isiyo endelevu inayotolewa wakati elektroni iliyoingia inapogongana na elektroni ya gamba la ndani la atomu na kuifanya atomu hiyo kuwa ioni, kisha elektroni nyingine kutoka gamba la nje huhamia kwenye nafasi tupu ya ndani huku ikitoa nishati iliyo sawa na tofauti kati ya viwango viwili vya nishati
{: .prompt-info }

## Mambo ya Kujua Kabla
- [Chembe ndogo za atomu na vipengele vya atomu](/posts/constituents-of-an-atom/)

## Ugunduzi wa miale-X
Röntgen aligundua kwamba miale-X huzalishwa wakati boriti ya elektroni inapopigwa kwenye lengo. Wakati wa ugunduzi huo, haikujulikana kwamba miale-X ni mawimbi ya sumakuumeme, hivyo ikapewa jina la **X-ray** kwa maana ya kitu kisichojulikana asili yake. Pia huitwa **mionzi ya Röntgen (Röntgen radiation)** kwa heshima ya mgunduzi wake.

![X-ray Tube](https://upload.wikimedia.org/wikipedia/commons/7/72/WaterCooledXrayTube.svg)

Picha iliyo juu inaonyesha kwa ufupi muundo wa kawaida wa bomba la miale-X (X-ray tube). Ndani ya bomba la miale-X kuna kathodi iliyoundwa kwa filament ya tungsteni na anodi yenye lengo lililowekwa, vyote vikiwa vimefungwa katika hali ya ombwe. Wakati volti kubwa ya makumi ya kV inapowekwa kati ya elektrodi hizi, elektroni hutolewa kutoka kathodi na kuelekezwa kwenye lengo la anodi, na kutoka hapo miale-X hutolewa. Hata hivyo, ufanisi wa ubadilishaji wa nishati kuwa miale-X kwa kawaida huwa chini ya 1%, na zaidi ya 99% ya nishati iliyobaki hubadilishwa kuwa joto, hivyo kifaa cha ziada cha kupooza huhitajika.

## bremsstrahlung (mionzi ya kusimama, braking radiation)
Wakati chembe yenye chaji kama elektroni inapopita karibu na kiini cha atomu, njia yake hupindishwa ghafla na pia kupunguzwa kasi kutokana na mvuto wa umeme kati ya chembe hiyo na kiini, na hivyo kutoa nishati katika umbo la miale-X. Kwa kuwa ubadilishaji huu wa nishati haujakwantishwa, miale-X inayotolewa huwa na spektra endelevu, na hii huitwa **bremsstrahlung** au **mionzi ya kusimama (braking radiation)**.

![Bremsstrahlung](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bremsstrahlung.svg)

Hata hivyo, nishati ya fotoni ya miale-X inayotolewa kwa bremsstrahlung haiwezi, bila shaka, kuzidi nishati ya mwendo ya elektroni iliyoingia. Kwa hiyo, kuna urefu mdogo kabisa wa wimbi kwa miale-X inayotolewa, na huu unaweza kupatikana kwa urahisi kwa kutumia fomula ifuatayo.

$$ \lambda_\text{min} = \frac{hc}{E}. \tag{1}$$

Kwa kuwa konstanti ya Planck $h$ na kasi ya mwanga $c$ ni konstanti, urefu huu mdogo kabisa wa wimbi huamuliwa tu na nishati ya elektroni inayoingia. Urefu wa wimbi $\lambda$ unaolingana na nishati ya $1\text{eV}$ ni takriban $1.24 \mu\text{m}=12400\text{Å}$. Kwa hiyo, urefu mdogo kabisa wa wimbi $\lambda_\text{min}$ wakati volti ya $V$ inatumiwa kwenye bomba la miale-X ni kama ifuatavyo. Kivitendo, fomula hii hutumiwa mara nyingi zaidi.

$$ \lambda_\text{min} \text{[Å]} = \frac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}. \label{eqn:lambda_min}\tag{2}$$

Grafu ifuatayo inaonyesha spektra endelevu ya miale-X wakati volti inabadilishwa huku mkondo unaopita kwenye bomba la miale-X ukiwekwa thabiti. Tunaweza kuona kwamba kadiri volti inavyoongezeka, urefu mdogo kabisa wa wimbi $\lambda_{\text{min}}$ unakuwa mfupi zaidi, na ukubwa wa jumla wa miale-X huongezeka.

![Typical continuous X-ray spectra from tube operating
at three different peak voltages with the same current](/assets/img/continuous-and-characteristic-x-rays/bremsstrahlung.png)

## Miale-X tabia (characteristic X-ray)
Ikiwa volti iliyowekwa kwenye bomba la miale-X ni kubwa vya kutosha, elektroni iliyoingia inaweza kugongana na elektroni katika gamba la ndani la atomu ya lengo na kuifanya atomu hiyo kuwa ioni. Katika hali hii, elektroni ya gamba la nje hutoa nishati haraka na kujaza nafasi tupu katika gamba la ndani, na katika mchakato huo fotoni ya miale-X yenye nishati sawa na tofauti ya viwango hivyo viwili vya nishati huzalishwa. Spektra ya miale-X inayotolewa kwa mchakato huu si endelevu, na huamuliwa na viwango vya nishati vya kipekee vya atomu ya lengo, bila kutegemea nishati au ukubwa wa boriti ya elektroni inayoingia. Hii huitwa **miale-X tabia (characteristic X-ray)**.

### Uandishi wa Siegbahn

![Siegbahn notation of electron transitions between shells](https://upload.wikimedia.org/wikipedia/commons/f/f6/CharacteristicRadiation.svg)
> *Chanzo cha picha*
> - Mwandishi: mtumiaji wa Wikipedia ya Kiingereza [HenrikMidtiby](https://en.wikipedia.org/wiki/User:HenrikMidtiby)
> - Leseni: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Kulingana na uandishi wa Siegbahn, wakati nafasi tupu katika gamba la K inajazwa na elektroni kutoka gamba la L, gamba la M, ... miale-X inayotolewa hujulikana kama $K_\alpha$, $K_\beta$, ... kama inavyoonyeshwa kwenye picha iliyo juu. Hata hivyo, baada ya uandishi wa Siegbahn, modeli za kisasa za atomu zilipojitokeza, iligunduliwa kwamba kwa atomu zenye elektroni nyingi, hata ndani ya kila gamba la modeli ya atomu ya Bohr (yaani, viwango vya nishati vyenye namba kuu ya kwanta sawa), viwango vya nishati hutofautiana kulingana na namba nyingine za kwanta. Kwa hiyo, kwa kila $K_\alpha$, $K_\beta$, ... pia likawekwa uainishaji wa kina zaidi kama $K_{\alpha_1}$, $K_{\alpha_2}$, ... 

![Siegbahn notation](/assets/img/continuous-and-characteristic-x-rays/siegbahn-notation.png)

Uandishi huu wa jadi bado unatumiwa sana katika nyanja ya spektroskopia. Hata hivyo, kwa kuwa majina yake si ya kimfumo na mara nyingi husababisha mkanganyiko, *Muungano wa Kimataifa wa Kemia Safi na Inayotumika (IUPAC)* unapendekeza kutumia uandishi mwingine kama ulivyo hapa chini.

### Uandishi wa IUPAC
Uandishi wa kawaida wa obitali za atomu na miale-X tabia unaopendekezwa na IUPAC ni kama ifuatavyo.
Kwanza, kwa kila obitali ya atomu, jina hutolewa kama katika jedwali lifuatalo.

| $n$(namba kuu ya kwanta) | $l$(namba ya kwanta ya azimuthi) | $s$(namba ya kwanta ya spin) | $j$(namba ya kwanta ya momenti ya angulari) | Obitali ya atomu | Uandishi wa miale-X |
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

> Namba ya kwanta ya jumla ya momenti ya angulari ni $j=\|l+s\|$.
{: .prompt-info }

Kisha miale-X tabia inayotolewa wakati elektroni ya atomu inapohama kutoka kiwango fulani cha nishati kwenda kiwango cha chini zaidi cha nishati hutajwa kwa kufuata kanuni ifuatayo.

$$ \text{(uandishi wa miale-X wa kiwango cha nishati cha baadaye)-(uandishi wa miale-X wa kiwango cha nishati cha awali)} $$

Kwa mfano, miale-X tabia inayotolewa wakati elektroni ya obitali ya $2p_{1/2}$ inapohama kwenda $1s_{1/2}$ inaweza kuitwa $\text{K-L}_2$.

## Spektra ya miale-X

![Spectrum of the X-rays emitted by an X-ray tube with a rhodium target, operated at 60 kV](https://upload.wikimedia.org/wikipedia/commons/2/23/TubeSpectrum-en.svg)

Hapo juu ni spektra ya miale-X inayotolewa wakati boriti ya elektroni iliyoharakishwa kwa 60 kV inapopigwa kwenye lengo la rodiamu (Rh). Mviringo laini na endelevu unaotokana na bremsstrahlung unaonekana, na kwa mujibu wa fomula ($\ref{eqn:lambda_min}$) tunaweza kuthibitisha kwamba miale-X hutolewa tu kwa urefu wa wimbi wa takriban $0.207\text{Å} = 20.7\text{pm} $ au zaidi. Aidha, sehemu zenye ncha kali zinazoonekana katikati ya grafu zinatokana na miale-X ya kipekee ya gamba la K ya atomu ya rodiamu. Kama ilivyotajwa awali, kwa kuwa kila atomu ya lengo ina spektra ya kipekee ya miale-X tabia kulingana na aina ya atomu hiyo, tunaweza kutambua elementi zinazounda lengo kwa kuchunguza urefu wa mawimbi ambamo miiba hiyo inaonekana katika spektra ya miale-X inayotolewa wakati boriti ya elektroni inapolipiga lengo hilo.

> Si tu $K_\alpha, K_\beta, \dots$ bali pia miale-X ya nishati ya chini zaidi kama $L_\alpha, L_\beta, \dots$ hutolewa bila shaka. Hata hivyo, hizi zina nishati ndogo zaidi na kwa kawaida hufyonzwa na housing ya bomba la miale-X, hivyo hazifiki kwenye kigunduzi.
{: .prompt-info }
