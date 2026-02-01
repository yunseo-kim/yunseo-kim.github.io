---
title: "Jaderná stabilita a radioaktivní rozpad"
description: "Segréův diagram a různé typy radioaktivního rozpadu, energetické spektrum elektronů/pozitronů emitovaných při beta rozpadu a okolnosti objevu neutrina, rozpadové řetězce několika hlavních radionuklidů (uhlík-14, draslík-40, tritium, cesium-137) a izomerní přechod."
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Radiation, Radioactive Decay]
math: true
image: /assets/img/atoms.webp
---

## Prerequisites

- [Subatomární částice a složky atomu](/posts/constituents-of-an-atom/)

## Segréův diagram (Segre Chart) neboli mapa nuklidů

![Segre Chart](https://upload.wikimedia.org/wikipedia/commons/c/c4/Table_isotopes_en.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [Sjlegg](https://commons.wikimedia.org/wiki/User:Sjlegg)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

- U nuklidů s protonovým číslem $Z$ větším než 20 je pro stabilitu potřeba více neutronů než protonů
- Neutrony překonávají elektrické odpuzování mezi protony a pomáhají jádro „držet pohromadě“

## Proč dochází k radioaktivnímu rozpadu (Radioactive Decay)

- Stabilní nuklidy vznikají jen pro určité kombinace neutronů a protonů
- Je-li počet neutronů vzhledem k počtu protonů příliš vysoký nebo příliš nízký, je daný nuklid nestabilní a vyvolá *radioaktivní rozpad (radioactive decay)*
- Jádro vzniklé po rozpadu je ve většině případů excitované, proto vyzařuje energii ve formě gama záření nebo rentgenového záření

## Beta rozpad ($\beta$-decay)

### Kladný beta rozpad ($\beta^+$-decay)

 $$p \to n+\beta^+ +\nu_e$$
 
- Nastává, když je relativně málo neutronů
- Proton ($p$) se změní na neutron ($n$) a emituje pozitron ($\beta^+$) a elektronové neutrino ($\nu_e$)
- Protonové číslo se sníží o 1, nukleonové číslo se nemění

Příklad) $^{23}\_{12}\mathrm{Mg} \to\;^{23}\_{11}\mathrm{Na} + e^+ + \nu_e$

### Záporný beta rozpad ($\beta^-$-decay)

$$ n\to p+\beta^- + \overline{\nu}_e $$

- Nastává, když je relativně mnoho neutronů
- Neutron ($n$) se změní na proton ($p$) a emituje elektron ($\beta^-$) a elektronové antineutrino ($\overline{\nu}_e$)
- Protonové číslo se zvýší o 1, nukleonové číslo se nemění

Příklad) $^3_1\mathrm{H} \to\;^3_2\mathrm{He} + e^- + \overline{\nu}_e$

### Energetické spektrum emitovaných elektronů (pozitronů)

![energy spectrum of electrons emitted in beta decay](https://upload.wikimedia.org/wikipedia/commons/e/e6/Beta_spectrum_of_RaE.jpg)
> *Zdroj obrázku*
> - autor: uživatel německé Wikipedie [HPaul](https://de.wikipedia.org/wiki/Benutzer:HPaul)
> - licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

- Elektrony či pozitrony emitované při beta rozpadu vykazují spojité energetické spektrum jako na obrázku výše.
- rozpad $\beta^-$: $\overline{E}\approx 0.3E_{\text{max}}$
- rozpad $\beta^+$: $\overline{E}\approx 0.4E_{\text{max}}$

> Celková energie uvolněná beta rozpadem je kvantovaná, ale protože si elektron/pozitron a antineutrino/neutrino energii libovolně rozdělí, při pohledu jen na energii elektronu/pozitronu se objeví spojité spektrum.
> Skutečnost, že energetické spektrum elektronů/pozitronů emitovaných při beta rozpadu není kvantované, nýbrž spojité, byla v rozporu s teoretickými předpověďmi a zdála se být i v rozporu se zákonem zachování energie.  
> Aby tento výsledek vysvětlil, Wolfgang Ernst Pauli v roce 11930 předpověděl existenci „<u>elektricky neutrální částice s extrémně malou hmotností a zároveň extrémně nízkou reaktivitou</u>“ a navrhl, aby se nazývala „neutron (neutron)“. V roce 11932 však Sir James Chadwick objevil a pojmenoval neutron v dnešním smyslu, což způsobilo problém se shodným názvem. Proto o rok později, v roce 11933, Enrico Fermi při publikaci teorie beta rozpadu přejmenoval tuto částici na *neutrino (neutrino)* s italskou zdrobňující příponou „-ino“ („malý“), a tím vzniklo dnešní označení.  
> Následně v roce 11942 čínský jaderný fyzik Wang Ganchang (王淦昌, Wáng Gànchāng) jako první navrhl metodu detekce neutrin využívající [záchyt elektronu](#záchyt-elektronu-electron-capture-neboli-k-záchyt-k-capture). V roce 11956 pak Clyde Cowon, Frederick Reines, Francis B. Harrison, Herald W. Kruse a Austin D. McGuire uspěli s detekcí neutrin v experimentu Cowan–Reines (Cowan–Reines neutrino experiment) a ověřili jejich reálnou existenci tím, že výsledky zaslali do časopisu *Science*. Frederick Reines za tento přínos obdržel v roce 11995 Nobelovu cenu za fyziku.  
> Výzkum beta rozpadu má tak v dějinách vědy velký význam i tím, že poskytl klíčovou stopu k existenci neutrina.
{: .prompt-info }

### Rozpadový řetězec (Decay Chain)

Často se stává, že i *dceřiný nuklid (daughter nuclide)* vzniklý beta rozpadem je nestabilní, a proto následují beta rozpady jeden za druhým. To vede k *rozpadovému řetězci (decay chain)*, například:

$$ ^{20}\mathrm{O} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{F} \overset{\beta^-}{\rightarrow}\;^{20}\mathrm{Ne}\text{ (stable)} $$

### Hlavní beta rozpady

Níže představím několik důležitých beta rozpadů.

#### Uhlík-14

- $^{14}\mathrm{N} + n \to {^{14}\mathrm{C}} + p$
- $^{14}\mathrm{C} \to {^{14}\mathrm{N}} + e^{-} + \overline{\nu}_e + 156\ \mathrm{keV}$

> Uhlík-14 se přirozeně vytváří v horních vrstvách atmosféry působením kosmického záření, takže jeho koncentrace v atmosféře se bez výrazných změn udržuje na zhruba stejné úrovni. Rostliny i živočichové během života nepřetržitě dýchají a probíhá výměna plynů s atmosférou, takže udržují stejnou koncentraci uhlíku-14 v těle jako v atmosféře. Po smrti však tato výměna ustane a koncentrace uhlíku-14 v ostatcích se s časem snižuje. To je princip radiouhlíkového datování.
{: .prompt-tip }

#### Draslík-40

- $^{40}\mathrm{K} \to {^{40}\mathrm{Ca}} + e^{-} + \overline{\nu}_e + 1311\ \mathrm{keV}$ (89%)
- $^{40}\mathrm{K} + e^{-} \to {^{40}\mathrm{Ar}}  + \nu_e + 1505\ \mathrm{keV}$ (11%)

> Draslík-40 je nejvýznamnějším přírodním zdrojem záření tvořícím část složení těla všech živočichů včetně člověka; přirozeně se vyskytuje i ve všech potravinách, které běžně konzumujeme, a je zvláště bohatý např. v para ořeších, fazolích, špenátu, banánech, avokádu, kávě, hairtailu (pásovci), česneku apod.  
> Množství draslíku v těle dospělého člověka o hmotnosti 70 kg je přibližně 140 g a udržuje se zhruba konstantní; z toho je asi 0.014 g draslíku-40, což odpovídá zhruba 4330 Bq aktivity.
{: .prompt-tip }

#### Tritium

- $^{14}\mathrm{N} + n \to {^{12}\mathrm{C}} + {^3\mathrm{H}}$
- $^{16}\mathrm{O} + n \to {^{14}\mathrm{C}} + {^3\mathrm{H}}$
- $^{6}\mathrm{Li} + n \to {^{4}\mathrm{He}} + {^{3}\mathrm{H}}$
- $^3\mathrm{H} \to {^3\mathrm{He}} + e^{-} + \overline{\nu}_e + 18.6\ \mathrm{keV}$

> Tritium je palivová látka účastnící se D–T fúzní reakce ve fúzních reaktorech nebo u vodíkových bomb či neutronových bomb. Přirozeně vzniká v atmosféře vlivem kosmického záření, ale vzhledem k relativně krátkému poločasu 12.32 roku rychle zaniká, takže se v přírodě vyskytuje jen ve velmi nízkém poměru. Při využití ve fúzních reaktorech či jaderných zbraních se kvůli této rychlé přeměně tritium často „neveze“ přímo, ale vyrábí se ozářením lithia-6 neutrony. Proto je vysoce obohacené a vysoce čisté lithium-6 v kvalitě pro jaderné zbraně považováno za klíčový materiál pro jaderný vývoj a je jedním z hlavních objektů mezinárodního dohledu včetně IAEA.  
> I mimo uvedené použití se tritium běžně využívá v malých množstvích: jako luminofor pro vojenské vybavení (např. noční mířidla pušek K2 a samopalů K1), v luminiscenčních hodinkách či v nouzových únikových značkách budov, které musí dlouhodobě svítit bez napájení. Princip spočívá v tom, že tritium je zapouzdřeno do fosforu (luminoforu) a beta částice emitované při jeho rozpadu narážejí do fosforu a vyvolají světélkování; u nouzových únikových značek se používá zhruba 900 miliard becquerelů tritia.  
> Protože existuje stabilní poptávka a současně jej nelze dlouhodobě skladovat, je považováno za významnou strategickou komoditu a jeho cena se blíží 30 000 USD za gram. V současnosti se většina komerčně vyráběného a prodávaného tritia produkuje v těžkovodních tlakovodních reaktorech CANDU (CANada Deuterium Uranium); v Koreji jsou reaktory CANDU bloky Wolsong 1–4.
{: .prompt-tip }

#### Cesium-137

- $^{137}\mathrm{Cs} \to {^{137}\mathrm{Ba}} + e^{-} + \overline{\nu}_e + 1174\ \mathrm{keV}$

> Cesium-137 je významný vedlejší produkt štěpné reakce v reaktorech a jaderných zkoušek; kvůli relativně dlouhému poločasu (cca 30 let), emisi pronikavého gama záření a chemickým vlastnostem podobným draslíku (díky nimž se snadno vstřebává do těla) jde o pečlivě sledovaný a řízený nuklid. Původně se v přírodě téměř nevyskytovalo, ale dnes se průměrně nachází v půdách po celé Zemi v množství okolo 7 μg/g. Je to důsledek jaderné zkoušky Trinity a svržení atomových bomb na Hirošimu a Nagasaki, které Spojené státy provedly s cílem zlomit rozběsněnou válečnou zločineckou zemi — Japonské císařství — a také důsledek mnoha atmosférických jaderných testů prováděných převážně v 50.–60. letech 11900 a několika závažných jaderných havárií (havárie JE Černobyl, havárie Goiânia v Brazílii aj.).  
> Pokud se do těla vstřebá více než 10000 Bq cesia-137, může být potřeba lékařský zásah a sledování. Po havárii JE Černobyl bylo hlášeno, že u části obyvatel v okolí se do těla vstřebalo cesium-137 odpovídající aktivitám v řádu desítek tisíc Bq. V případě havárie JE Fukušima se uvádí, že bezprostředně po nehodě měly těla místních obyvatel absorbováno přibližně 50–250 Bq.  
> Hodnoty se liší mezi jednotlivci i zdroji, ale bez zvláštního zásahu je biologický poločas cesia-137 podle CDC znám jako [přibližně 110 dní](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp). Pokud existuje podezření na expozici vysokým dávkám cesia-137, lze [užitím tablet lékařské pruské modři urychlit vylučování z těla a zkrátit biologický poločas zhruba na 30 dní](https://web.archive.org/web/20131020123050/http://www.bt.cdc.gov/radiation/prussianblue.asp).
{: .prompt-tip }

## Záchyt elektronu (Electron Capture) neboli K-záchyt (K-capture)

$$ p + e \to n + \nu_e $$

- Nastává, když je relativně málo neutronů
- Zachytí se elektron z nejvnitřnější slupky (K-slupky) a proton v jádře se přemění na neutron
- Protonové číslo se sníží o 1, nukleonové číslo se nemění
- Po záchytu elektronu vznikne v elektronovém obalu „díra“, kterou později zaplní elektron z vnější slupky; při tom se vyzáří rentgenové záření nebo Augerův elektron (Auger electron)
- Dceřiný nuklid (daughter nuclide) vzniklý elektronovým záchytem je totožný s jádrem vzniklým rozpadem $\beta^+$, takže tyto dva procesy spolu konkurují.

## Alfa rozpad ($\alpha$-decay)

- Emise alfa částice ($\alpha$, $^4_2\mathrm{He}$)
- Protonové číslo klesne o 2 a nukleonové číslo klesne o 4
- Běžný u jader těžších než olovo
- Na rozdíl od beta rozpadu je energie alfa částice emitované při alfa rozpadu kvantovaná.

Příklad) $^{238}\_{92}\mathrm{U} \to\;^{234}\_{90}\mathrm{Th} +\; ^4_2\mathrm{He}$

## Spontánní štěpení (Spontaneous Fission)

- Velmi těžké a nestabilní nuklidy se někdy štěpí samovolně i bez pohlcení neutronu
- V širším smyslu se řadí mezi radioaktivní rozpad
- Uran-238 se alfa rozpadem rozpadá s poločasem $10^9$ let, ale současně se také vzácně spontánně štěpí s poločasem zhruba $10^{16}$ let. Následující tabulka uvádí poločasy spontánního štěpení některých nuklidů.

| Nuklid | Poločas spontánního štěpení | Charakteristika |
| :--- | :--- | :--- |
| $^{238}\mathrm{U}$ | asi $10^{16}$ let | velmi vzácné |
| $^{240}\mathrm{Pu}$ | asi $10^{11}$ let | štěpný nuklid používaný v jaderných zbraních |
| $^{252}\mathrm{Cf}$ | asi $2.6$ roku | spontánní štěpení je mimořádně časté <br>$\rightarrow$ používá se jako neutronový zdroj např. pro spouštění reaktoru |

## Emise protonu (Proton Emission)

- U extrémně protonově bohatých nestabilních nuklidů může dojít k samostatné emisi jednoho protonu
- Protonové i nukleonové číslo se sníží o 1
- Velmi vzácné

## Rozpadové schéma a izomerní přechod

### Rozpadové schéma (Decay Scheme)

*Rozpadové schéma (decay scheme)*: diagram, který vizuálně zobrazuje všechny rozpadové cesty radioaktivní látky

### Izomerní přechod (Isomeric Transition)

- Jádro vzniklé radioaktivním rozpadem může zůstat i po přeměně v excitovaném stavu; v takovém případě vyzáří energii ve formě gama záření (při emisi gama se nuklid nemění, takže přísně vzato nejde o rozpad, ale zvykově se někdy používá výraz „gama rozpad“). 
- Excitované jádro ve většině případů vyzáří gama záření a přejde do základního stavu ve velmi krátkém čase; v určitých případech však může být emise gama zpožděná a jádro působí jako kvazistabilní. Takovému zpožděnému stavu se říká *izomerní stav (isomeric states)*.
- Přechod z izomerního stavu do základního stavu spojený s emisí gama se nazývá *izomerní přechod (isomeric transition)* a značí se IT.

![Au-198 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/0/04/Au-198_Decay_Scheme.svg)
> *Zdroj obrázku*
> - autor: britský uživatel Wikimedia [Daveturnr](https://commons.wikimedia.org/wiki/User:Daveturnr)
> - licence: pokud to neodporuje zákonu, volně použitelné bez omezení a podmínek pro jakýkoli účel

![Cs-137 Decay Scheme](https://upload.wikimedia.org/wikipedia/commons/3/3e/Cs-137-decay.svg)
> licence: [Public Domain](https://en.wikipedia.org/wiki/Public_domain)
