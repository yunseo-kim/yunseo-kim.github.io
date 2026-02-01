---
title: Gravitační pole a gravitační potenciál
description: "Definice vektoru gravitačního pole a gravitačního potenciálu podle Newtonova zákona gravitace; klíčové příklady: věta o kulové slupce a rotační křivky galaxií."
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Newtonův zákon všeobecné gravitace: $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - Pro spojité rozložení hmoty a tělesa konečné velikosti: $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$: hustota hmoty v bodě s polohovým vektorem $\mathbf{r^{\prime}}$ vzhledem k libovolně zvolenému počátku
>   - $dv^{\prime}$: objemový element v bodě s polohovým vektorem $\mathbf{r^{\prime}}$ vzhledem k libovolně zvolenému počátku
> - **Vektor gravitačního pole (gravitational field vector)**:
>   - vektor vyjadřující sílu na jednotkovou hmotnost, kterou v daném poli vyvolaném tělesem o hmotnosti $M$ pociťuje částice
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - má rozměr *síly na jednotku hmotnosti* neboli *zrychlení*
> - **Gravitační potenciál (gravitational potential)**:
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - má rozměr $($*síla na jednotku hmotnosti* $) \times ($*vzdálenost* $)$ neboli *energie na jednotku hmotnosti*
>   - $\Phi = -G\cfrac{M}{r}$
>   - gravitační potenciál má význam jen přes své relativní rozdíly; konkrétní absolutní hodnota sama o sobě význam nemá
>   - obvykle se pro odstranění neurčitosti (ambiguity) volí podmínka $\Phi \to 0$ pro $r \to \infty$
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **Gravitační potenciál uvnitř a vně kulové slupky (věta o kulové slupce)**
>   - pro $R>a$:
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - při výpočtu gravitačního potenciálu v libovolném vnějším bodě od kulově symetrického rozložení hmoty (spherical symmetric distribution) lze celé těleso považovat za hmotný bod (point mass)
>   - pro $R<b$:
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - uvnitř kulově symetrické hmotné slupky je gravitační potenciál konstantní nezávisle na poloze a působící gravitace je $0$
>   - pro $b<R<a$: $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## Gravitační pole
### Newtonův zákon všeobecné gravitace
Newton již před 11666 HE zákon všeobecné gravitace systematizoval a také jej numericky ověřil. Přesto mu trvalo dalších 20 let, než své výsledky vydal roku 11687 HE v díle *Principia*—důvodem bylo, že nedokázal ospravedlnit výpočetní postup, v němž Zemi a Měsíc považoval za hmotné body (point mass) bez rozměrů. Naštěstí platí, že [s použitím kalkulu, který Newton sám později vynalezl, můžeme problém, jenž pro Newtona v 11600. letech nebyl snadný, dokázat mnohem jednodušeji](#kdyz-ra).

Podle Newtonova zákona všeobecné gravitace (Newton's law of universal gravitation) *každá hmotná částice přitahuje všechny ostatní částice ve vesmíru silou, která je úměrná součinu jejich hmotností a nepřímo úměrná druhé mocnině vzdálenosti mezi nimi.* Matematicky:

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - licence: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

Jednotkový vektor $\mathbf{e}_r$ míří od $M$ směrem k $m$ a záporné znaménko vyjadřuje, že jde o přitažlivou sílu. Tj. $m$ je přitahováno k $M$.

### Cavendishův experiment
Experimentální ověření tohoto zákona a určení hodnoty $G$ provedl roku 11798 HE britský fyzik Henry Cavendish. Cavendishův experiment používá torzní váhy tvořené lehkou tyčí, na jejíchž koncích jsou upevněny dvě malé koule. Tyto dvě koule jsou přitahovány ke dvěma jiným velkým koulím umístěným poblíž. Dosud udávaná oficiální hodnota $G$ je $6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$.

> Přestože je $G$ jednou z nejdéle známých fundamentálních konstant, známe ji jen s nižší přesností (precision) než většinu ostatních konstant, jako jsou $e$, $c$, $\hbar$. I dnes probíhá mnoho výzkumů, jejichž cílem je zjistit $G$ s vyšší přesností.
{: .prompt-tip }

### Případ těles konečné velikosti
Zákon ve tvaru ($\ref{eqn:law_of_gravitation}$) lze přísně vzato aplikovat pouze na *bodové částice (point particle)*. Pokud je jedno nebo obě tělesa objekt konečné velikosti, je třeba pro výpočet síly navíc předpokládat, že gravitační pole (gravitational force field) je *lineární pole (linear field)*. Tj. předpokládáme, že celková gravitace působící na jednu částici o hmotnosti $m$ od mnoha dalších částic se získá vektorovým součtem jednotlivých sil. Pro těleso se spojitým rozložením hmoty se součet přepíše jako integrál:

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$: hustota hmoty v bodě s polohovým vektorem $\mathbf{r^{\prime}}$ vzhledem k libovolně zvolenému počátku
- $dv^{\prime}$: objemový element v bodě s polohovým vektorem $\mathbf{r^{\prime}}$ vzhledem k libovolně zvolenému počátku

Pokud mají konečnou velikost jak těleso o hmotnosti $M$, tak těleso o hmotnosti $m$, je pro určení celkové gravitace potřeba ještě druhý objemový integrál i přes objem tělesa $m$.

### Vektor gravitačního pole
**Vektor gravitačního pole (gravitational field vector)** $\mathbf{g}$ definujeme jako vektor síly na jednotku hmotnosti, kterou v poli vytvořeném tělesem o hmotnosti $M$ pociťuje částice:

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

nebo

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

kde se směr $\mathbf{e}_r$ mění v závislosti na $\mathbf{r^\prime}$.

Tato veličina $\mathbf{g}$ má rozměr *síly na jednotku hmotnosti* neboli *zrychlení*. Velikost vektoru gravitačního pole $\mathbf{g}$ poblíž zemského povrchu je rovna tomu, čemu říkáme **konstanta tíhového zrychlení (gravitational acceleration constant)**, a platí $\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$.

## Gravitační potenciál
### Definice
Vektor gravitačního pole $\mathbf{g}$ se mění jako $1/r^2$, a proto splňuje podmínku ($\nabla \times \mathbf{g} \equiv 0$), aby mohl být vyjádřen jako gradient nějaké skalární funkce (potenciálu). Můžeme tedy psát:

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

kde $\Phi$ nazýváme **gravitační potenciál (gravitational potential)**; má rozměr $($*síla na jednotku hmotnosti* $) \times ($*vzdálenost* $)$ neboli *energie na jednotku hmotnosti*.

Protože $\mathbf{g}$ závisí pouze na poloměru, závisí na $r$ i $\Phi$. Ze vztahů ($\ref{eqn:g_vector}$) a ($\ref{eqn:gradient_phi}$) plyne

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

a integrací dostaneme

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

Gravitační potenciál má smysl pouze přes relativní rozdíly; velikost absolutní hodnoty smysl nemá, proto lze integrační konstantu vynechat. Obvykle se pro odstranění neurčitosti (ambiguity) volí podmínka $\Phi \to 0$ pro $r \to \infty$ a vztah ($\ref{eqn:g_potential}$) ji také splňuje.

Pro spojité rozložení hmoty je gravitační potenciál

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

Je-li hmota povrchově rozložena na tenké slupce, pak

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

A pro lineární zdroj hmoty s lineární hustotou $\rho_l$ lze psát

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### Fyzikální význam
Uvažujme práci na jednotku hmotnosti $dW^\prime$, kterou těleso vykoná při posunu o $d\mathbf{r}$ v gravitačním poli.

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

V tomto vztahu je $\Phi$ funkcí pouze polohových souřadnic, tj. $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$. Z toho plyne, že při přesunu tělesa z jednoho bodu do druhého je práce na jednotku hmotnosti rovna rozdílu potenciálů mezi těmito dvěma body.

Definujeme-li gravitační potenciál v nekonečně vzdáleném bodě jako $0$, lze $\Phi$ v libovolném bodě interpretovat jako práci na jednotku hmotnosti potřebnou k přesunu tělesa z nekonečna do daného bodu. Potenciální energie tělesa je rovna součinu jeho hmotnosti a gravitačního potenciálu $\Phi$, takže pro potenciální energii $U$ platí

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

Proto gravitační sílu působící na těleso získáme jako záporný gradient jeho potenciální energie:

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

Je-li těleso umístěno do gravitačního pole vytvořeného nějakou hmotností, vždy vzniká určitá potenciální energie. Přísně vzato patří poli jako takovému, ale zvyklostí se o ní mluví jako o potenciální energii tělesa.

## Příklad: gravitační potenciál uvnitř a vně kulové slupky (věta o kulové slupce)
### Volba souřadnic & vyjádření gravitačního potenciálu integrálem
Spočítejme gravitační potenciál uvnitř a vně homogenní kulové slupky (spherical shell) s vnitřním poloměrem $b$ a vnějším poloměrem $a$. Gravitační sílu od slupky lze získat i přímým výpočtem složek síly působících na jednotkovou hmotnost v poli, ale potenciálová metoda je jednodušší.

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

Vypočtěme potenciál v bodě $P$, který je ve vzdálenosti $R$ od středu. Při předpokladu homogenního rozložení hmoty ve slupce platí $\rho(r^\prime)=\rho$ a vzhledem k symetrii podle azimutu $\phi$ kolem přímky spojující střed koule s bodem $P$ dostaneme

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

Z kosinové věty plyne

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

a protože $R$ je konstanta, diferenciací podle $r^\prime$ dostaneme

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

tedy

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

Po dosazení do ($\ref{eqn:spherical_shell_1}$) vyjde

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

kde $r_\mathrm{max}$ a $r_\mathrm{min}$ závisí na poloze bodu $P$.

### Když $R>a$

$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

Hmotnost kulové slupky $M$ je

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

a tedy potenciál je

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> Porovnáme-li vztah pro gravitační potenciál od hmotného bodu o hmotnosti $M$, tj. ($\ref{eqn:g_potential}$), s právě získaným výsledkem ($\ref{eqn:spherical_shell_outside_2}$), vidíme, že jsou totožné. To znamená, že při výpočtu gravitačního potenciálu v libovolném vnějším bodě od kulově symetrického rozložení hmoty (spherical symmetric distribution) lze bez újmy považovat veškerou hmotnost za soustředěnou ve středu. Patří sem většina kulových těles alespoň určité velikosti, jako je Země či Měsíc; lze je považovat za překryv nesčetně mnoha kulových slupek se stejným středem a různými průměry, podobně jako [matrjoška](https://en.wikipedia.org/wiki/Matryoshka_doll). To je také [oprávnění pro předpoklad, že je výpočet správný i tehdy, když tělesa jako Země nebo Měsíc považujeme za hmotné body bez rozměrů](#newtonuv-zakon-vseobecne-gravitace), jak bylo zmíněno v první části tohoto článku.
{: .prompt-info }

### Když $R<b$

$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> Uvnitř kulově symetrické hmotné slupky je gravitační potenciál konstantní nezávisle na poloze a působící gravitace je $0$.
{: .prompt-info }

> A právě to je také jeden z hlavních důvodů, proč je „teorie duté Země“—typický příklad pseudovědy—nesmysl. Pokud by Země opravdu měla tvar kulové slupky a byla uvnitř prázdná, jak tato teorie tvrdí, pak by na všechny objekty uvnitř dutiny nepůsobila zemská gravitace. Když vezmeme v úvahu hmotnost a objem Země, je dutina takového rozsahu sama o sobě nereálná; a i kdyby existovala, případné organismy by nežily „na vnitřní stěně“ jako na zemi, ale volně by se vznášely v beztížném stavu jako na kosmické stanici.  
> Je sice možné, že [v hloubce několika kilometrů pod povrchem mohou žít mikroorganismy](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3), ale určitě ne v podobě, jakou předpokládá teorie duté Země. Román Julese Verna 《Cesta do středu Země (Voyage au centre de la Terre)》 i film „Cesta do středu Země (Journey to the Center of the Earth)“ mám také moc rád, ale fikce je fikce—neberme ji smrtelně vážně.
{: .prompt-tip }

### Když $b<R<a$

$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### Výsledek
Gravitační potenciál $\Phi$ ve třech oblastech, a odpovídající velikost vektoru gravitačního pole $\|\mathbf{g}\|$, jako funkce vzdálenosti $R$:

![Gravitational Potential as a Function of R](/physics-visualizations/figs/shell-theorem-gravitational-potential.png)  
![Magnitude of the Field Vector as a Function of R](/physics-visualizations/figs/shell-theorem-field-vector.png)  
> - Kód vizualizace v Pythonu: [repozitář yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/shell_theorem.py)
> - licence: [See here](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

Je vidět, že gravitační potenciál i velikost vektoru gravitačního pole jsou spojité. Kdyby byl gravitační potenciál v nějakém bodě nespojitý, pak by v tomto bodě byl gradient potenciálu, tedy velikost gravitační síly, nekonečný; to není fyzikálně smysluplné, a proto musí být potenciálová funkce všude spojitá. Nicméně *derivace* vektoru gravitačního pole je na vnitřním a vnějším povrchu slupky nespojitá.

## Příklad: rotační křivky galaxií
Astronomická pozorování ukazují, že ve spirálních galaxiích rotujících kolem svého středu—například v Mléčné dráze nebo v galaxii Andromeda—je většina pozorovatelné hmoty soustředěna poblíž centrální oblasti. Přesto jsou oběžné rychlosti pozorovatelné hmoty ve spirálních galaxiích ve výrazném nesouladu s hodnotami teoreticky předpovězenými z pozorovatelného rozložení hmoty, a jak je vidět na následujícím grafu, ve větších vzdálenostech jsou téměř konstantní.

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *Zdroj obrázku*
> - autor: uživatel Wikipedie [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - licence: Public Domain

{% 
  include embed/video.html 
  src='https://cdn.jsdelivr.net/gh/yunseo-kim/yunseo-kim.github.io/assets/video/gravitational-field-and-potential/Galaxy_rotation_under_the_influence_of_dark_matter.webm' 
  title="Vlevo: rotace galaxie předpovězená z pozorovatelné hmoty | vpravo: skutečně pozorovaná rotace galaxie." 
  types='ogg'
  autoplay=true 
  loop=true 
%}
> *Zdroj videa*
> - odkaz na původní soubor (Ogg Theora video): <https://commons.wikimedia.org/wiki/File:Galaxy_rotation_under_the_influence_of_dark_matter.ogv>
> - autor: [Ingo Berg](https://beltoforion.de/en/index.php)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
> - použitá simulační metoda a kód: <https://beltoforion.de/en/spiral_galaxy_renderer/>

> Dříve vložený obrázek `Rotation curve of spiral galaxy Messier 33 (Triangulum).png` byl smazán z Wikimedia Commons poté, co se ukázalo, že uživatel Wikimedia [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama) jej [vytvořil jako odvozené dílo plagiující nevolně licencované dílo profesora Marka Whittlea z University of Virginia bez řádné citace](https://commons.wikimedia.org/wiki/Commons:Deletion_requests/File:Rotation_curve_of_spiral_galaxy_Messier_33_(Triangulum).png). Z tohoto důvodu byl odstraněn i z této stránky.
{: .prompt-danger }

Ověřme, že pokud je hmotnost galaxie soustředěna do středu, teoreticky předpovězená oběžná rychlost jako funkce vzdálenosti neodpovídá pozorování, a ukažme, že k vysvětlení pozorování musí hmotnost $M(R)$ rozložená uvnitř vzdálenosti $R$ od středu růst úměrně $R$.

Nejprve: je-li hmotnost galaxie $M$ soustředěna ve středu, oběžnou rychlost ve vzdálenosti $R$ dostaneme z

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

V tomto případě bychom (podle tečkované čáry v předchozích grafech) očekávali oběžnou rychlost klesající jako $1/\sqrt{R}$. Pozorování však ukazují, že oběžná rychlost $v$ je téměř konstantní nezávisle na vzdálenosti $R$, takže teorie a pozorování se neshodují. Tento výsledek lze vysvětlit pouze tehdy, když $M(R)\propto R$.

Zavedeme-li konstantu úměrnosti $k$ a položíme $M(R) = kR$, pak

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(konstanta)}. $$

Z toho astrofyzikové vyvozují, že v mnoha galaxiích musí existovat dosud neobjevená „temná hmota (dark matter)“ a že tato temná hmota musí tvořit více než 90 % hmoty ve vesmíru. Povaha temné hmoty však zatím nebyla jednoznačně objasněna; existují také pokusy (byť nejde o hlavní proud) vysvětlit pozorování bez předpokladu temné hmoty, například pomocí modifikované newtonovské dynamiky (Modified Newtonian Dynamics, MOND). Dnes se tento výzkum nachází na samé špičce astrofyziky.
