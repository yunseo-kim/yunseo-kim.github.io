---
title: Definice plazmatu a pojem teploty, a také Sahova rovnice (Saha equation)
description: Vysvětlíme, co v definici plazmatu znamená kolektivní chování, představíme Sahovu rovnici a ujasníme pojem teploty v plazmové fyzice.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## TL;DR
> - **Plazma (plasma)**: kvazineutrální (quasineutral) plyn tvořený nabitými i neutrálními částicemi, který vykazuje kolektivní chování (collective behavior)
> - **„Kolektivní chování (collective behavior)”** plazmatu:
>   - Elektrická síla mezi dvěma oblastmi plazmatu $A$ a $B$ klesá se vzdáleností jako $1/r^2$
>   - Avšak při daném prostorovém úhlu ($\Delta r/r$) roste objem oblasti plazmatu $B$, která může ovlivnit $A$, jako $r^3$
>   - Proto mohou části plazmatu působit jedna na druhou smysluplnou silou i na velké vzdálenosti
> - **Sahova rovnice (Saha equation)**: vztah mezi stupněm ionizace plynu v tepelné rovnováze a jeho teplotou a tlakem
>
> $$ \frac{n_{i+1}n_e}{n_i} = \frac{2}{\lambda_{\text{th}}^3}\frac{g_{i+1}}{g_i}\exp{\left[-\frac{\epsilon_{i+1}-\epsilon_i}{k_B T}\right]}$$
>
> - Pojem teploty v plazmové fyzice:
>   - V plynu i plazmatu úzce souvisí průměrná kinetická energie na částici s teplotou; jde o vzájemně zaměnitelné fyzikální veličiny
>   - V plazmové fyzice je zvykem vyjadřovat teplotu v energetických jednotkách $\mathrm{eV}$ jako hodnotu $kT$
>     - $1\mathrm{eV}=11600\mathrm{K}$
>   - Plazma může mít současně několik různých teplot; zejména elektronová teplota ($T_e$) a iontová teplota ($T_i$) se mohou v některých případech výrazně lišit
> - Nízkoteplotní plazma vs. vysokoteplotní plazma:
>   - Teplota plazmatu:
>     - nízkoteplotní plazma: $T_e \text{(>10,000℃)} \gg T_i \approx T_g \text{(}\sim\text{100℃)}$ $\rightarrow$ nerovnovážné plazma (non-equilibrium plasma)
>     - vysokoteplotní (tepelné) plazma: $T_e \approx T_i \approx T_g \text{(>10,000℃)}$ $\rightarrow$ rovnovážné plazma (equilibrium plasma)
>   - Hustota plazmatu:
>     - nízkoteplotní plazma: $n_g \gg n_i \approx n_e$ $\rightarrow$ malý stupeň ionizace, většina částic je neutrálních
>     - vysokoteplotní (tepelné) plazma: $n_g \approx n_i \approx n_e $ $\rightarrow$ velký stupeň ionizace
>   - Tepelná kapacita plazmatu:
>     - nízkoteplotní plazma: elektronová teplota je vysoká, ale hustota nízká a většina částic jsou relativně chladné neutrály, takže tepelná kapacita je malá a plazma „nepálí”
>     - vysokoteplotní (tepelné) plazma: elektrony, ionty i neutrály mají vysokou teplotu, tepelná kapacita je velká a plazma je horké
{: .prompt-info }

## Prerequisites
- [Subatomární částice a stavební prvky atomu](/posts/constituents-of-an-atom/)
- Maxwellovo–Boltzmannovo rozdělení (statistická mechanika)
- [Hmotnost a energie, částice a vlny](/posts/Mass-and-Energy-Particles-and-Waves/)
- Symetrie a zákony zachování (kvantová mechanika), degenerace (degeneracy)

## Definice plazmatu
V textech, které vysvětlují plazma laikům, se plazma obvykle definuje následovně:

> Zahřátím plynu na extrémně vysokou teplotu až do stavu, kdy se jeho atomy oddělí na elektrony a kladné ionty a dojde k ionizaci, získáme čtvrté skupenství hmoty po pevném, kapalném a plynném

Není to vyloženě špatně a stejně to uvádí i [web Korea Institute of Fusion Energy](https://www.kfe.re.kr/menu.es;jsessionid=BD5BB81782954634B90FEE221A82583E?mid=a10201010000).
Jde také o populární definici, se kterou se snadno setkáte při vyhledávání „plazma“.

Jenže: i když je toto tvrzení obecně správné, nelze ho považovat za striktně přesnou definici. Plyn v běžných podmínkách okolního prostředí (pokojová teplota a atmosférický tlak) je sice ionizovaný jen v extrémně malé míře, ale přesto je částečně ionizovaný; a stejně mu plazma neříkáme. Pokud ve vodě rozpustíme iontovou sloučeninu, jako je chlorid sodný, rozpadne se na nabité ionty, ale ani takový roztok není plazma.  
Jinými slovy: plazma je sice ionizovaný stav hmoty, ale ne vše, co je ionizované, je automaticky plazma.

Přesněji lze plazma definovat takto:

> *Plazma je kvazineutrální plyn složený z nabitých a neutrálních částic, který vykazuje kolektivní chování.*  
> *A plasma is a quasineutral gas of charged and neutral particles which exhibits collective behavior.*
>
> by Fransis F. Chen

Co přesně znamená „kvazineutralita (quasineutrality)“, si ukážeme později při probírání **Debyeho stínění (Debye shielding)**. Tady se zaměřme na to, co znamená „kolektivní chování (collective behavior)“ plazmatu.

## Kolektivní chování plazmatu
U neionizovaného plynu složeného z neutrálních částic je každá molekula elektricky neutrální, takže výsledná elektromagnetická síla je $0$ a gravitační vliv lze také zanedbat. Molekuly se pohybují nerušeně až do srážky s jinou molekulou a právě srážky určují jejich pohyb. I kdyby se část částic ionizovala a nesla náboj, podíl ionizovaných částic v celém plynu je velmi malý, takže elektrický vliv těchto nabitých částic se se vzdáleností tlumí jako $1/r^2$ a nedosahuje do velkých vzdáleností.

V plazmatu, které obsahuje velké množství nabitých částic, je však situace zcela jiná. Pohyb nabitých částic může vyvolat lokální akumulaci kladného nebo záporného náboje, a tím vznik elektrického pole. Pohyb náboje navíc vytváří elektrický proud a proud vytváří magnetické pole. Taková elektrická a magnetická pole mohou ovlivňovat i vzdálené částice bez nutnosti přímých srážek.

![Elektrické síly působící na dálku v plazmatu](/assets/img/definition-of-plasma/electric-forces-acting-at-a-distance-in-a-plasma.png)

Podívejme se, jak se mění velikost elektrické síly působící mezi dvěma oblastmi plazmatu $A$ a $B$, které nesou malé množství náboje, v závislosti na vzdálenosti $r$. Elektrická síla (Coulomb force) podle Coulombova zákona mezi $A$ a $B$ klesá s rostoucí vzdáleností jako $1/r^2$. Pokud však při daném prostorovém úhlu ($\Delta r/r$) zůstává geometrie stejná, objem oblasti plazmatu $B$, která může ovlivnit $A$, roste jako $r^3$. Proto mohou části plazmatu působit jedna na druhou smysluplnou silou i na velké vzdálenosti. Elektrické síly působící na dálku umožňují plazmatu vykazovat velmi rozmanité druhy pohybu a jsou jedním z důvodů, proč existuje samostatný obor plazmová fyzika (plasma physics). „Kolektivní chování (collective behavior)“ znamená, že <u>pohyb v určité oblasti není určen pouze lokálními podmínkami v této oblasti, ale je ovlivněn i stavem plazmatu ve vzdálených oblastech</u>. 

## Sahova rovnice (Saha equation)
**Sahova rovnice (Saha equation)** je vztah mezi ionizačním stavem plynu v tepelné rovnováze a jeho teplotou a tlakem; zavedl ji indický astrofyzik Meghnad Saha.

$$ \frac{n_{i+1}n_e}{n_i} = \frac{2}{\lambda_{\text{th}}^3}\frac{g_{i+1}}{g_i}\exp{\left[-\frac{\epsilon_{i+1}-\epsilon_i}{k_B T}\right]} \label{eqn:saha_eqn}\tag{1}$$

- $n_i$: hustota $i$-tého kladného iontu (kationtu, který ztratil $i$ elektronů)
- $g_i$: degenerace (degeneracy) stavů $i$-tého kationtu
- $\epsilon_i$: energie potřebná k odtržení $i$ elektronů z neutrálního atomu a vytvoření $i$-tého kationtu
  - $\epsilon_{i+1}-\epsilon_i$: ionizační energie $(i+1)$-tého stupně
- $n_e$: elektronová hustota
- $k_B$: Boltzmannova konstanta
- $\lambda_{\text{th}}$: tepelná de Broglieho vlnová délka (průměrná [de Broglieho vlnová délka](/posts/Mass-and-Energy-Particles-and-Waves/#hmotnostni-vlny) elektronu v plynu při dané teplotě)

$$ \lambda_{\text{th}} \equiv \frac{h}{\sqrt{2\pi m_e k_B T}} \quad \text{ (}h\text{: Planckova konstanta)} \label{eqn:lambda_th}\tag{2}$$

- $m_e$: hmotnost elektronu
- $T$: teplota plynu

Pokud je důležitá pouze ionizace o jeden stupeň a vznik kationtů s nábojem $2+$ a vyšším lze zanedbat, můžeme položit $n_1=n_i=n_e$, $n_0=n_n$, $U_i = \epsilon = \epsilon_1$, $i=0$ a rovnici zjednodušit následovně:

$$ \begin{align*}
\frac{n_i^2}{n_n} &= \frac{2}{\lambda_{th}^3}\frac{g_1}{g_0}\exp{\left[-\frac{\epsilon}{k_B T} \right]} \label{eqn:saha_eqn_approx}\tag{3}\\
&= 2\left(\frac{2\pi m_e k_B T}{h^2}\right)^{3/2}\frac{g_1}{g_0}e^{-U_i/{k_B T}} \\
&= 2\frac{g_1}{g_0}\left(\frac{2\pi m_e k_B}{h^2}\right)^{3/2}T^{3/2}e^{-U_i/{k_B T}}. \label{eqn:saha_eqn_approx_2}\tag{4}
\end{align*}$$

### Míra ionizace vzduchu (dusíku) při pokojové teplotě a atmosférickém tlaku
Ve výše uvedeném vztahu se hodnota $2 \cfrac{g_1}{g_0}$ liší podle složení plynu, ale v mnoha případech je její **řád (order of magnitude)** přibližně $1$. Lze tedy zhruba aproximovat:

$$ \frac{n_i^2}{n_n} \approx \left(\frac{2\pi m_e k_B}{h^2}\right)^{3/2} T^{3/2} e^{-U_i/{k_B T}}.$$

V soustavě SI mají základní konstanty $m_e$, $k_B$, $h$ hodnoty

- $m_e \approx 9.11 \times 10^{-31} \mathrm{kg}$
- $k_B \approx 1.38 \times 10^{-23} \mathrm{J/K}$
- $h \approx 6.63 \times 10^{-34} \mathrm{J \cdot s}$

a po dosazení do rovnice dostaneme:

$$ \frac{n_i^2}{n_n} \approx 2.4 \times 10^{21}\ T^{3/2} e^{-U_i/{k_B T}}. \label{eqn:fractional_ionization}\tag{5}$$

Z toho pro dusík v podmínkách pokojové teploty a atmosférického tlaku ($n_n \approx 3 \times 10^{25} \mathrm{m^{-3}}$, $T\approx 300\mathrm{K}$; $U_i \approx 14.5\mathrm{eV} \approx 2.32 \times 10^{-18}\mathrm{J}$) vyjde přibližná míra ionizace $n_i/(n_n + n_i) \approx n_i/n_n$:

$$ \frac{n_i}{n_n} \approx 10^{-122} $$

Tedy extrémně nízká. To je důvod, proč na rozdíl od kosmického prostředí na zemském povrchu a v blízkosti hladiny moře přirozeně téměř nepřicházíme do styku s plazmatem.

## Pojem teploty v plazmové fyzice
Rychlosti částic v plynu v tepelné rovnováze se obecně řídí Maxwellovým–Boltzmannovým rozdělením (Maxwell–Boltzmann distribution):

$$ f(v) = \left(\frac{m}{2\pi k_B T} \right)^{3/2} 4\pi v^2 \exp{\left(-\frac{mv^2}{2k_B T} \right)} \label{eqn:maxwell_boltzmann_dist}\tag{6}$$

![Maxwellovo–Boltzmannovo rozdělení](https://tikz.net/files/maxwell-boltzmann-001.png)
> *Zdroj obrázku*
> - Autor: TikZ.net author [Izaak Neutelings](https://tikz.net/author/izaak/)
> - Licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

- nejpravděpodobnější rychlost (most probable speed): $v_p = \sqrt{\cfrac{2k_B T}{m}}$
- střední rychlost (mean speed): $\langle v \rangle = \sqrt{\cfrac{8k_B T}{\pi m}}$
- efektivní (RMS) rychlost (RMS speed): $v_{rms} = \sqrt{\langle v^2 \rangle} = \sqrt{\cfrac{3k_B T}{m}}$

Průměrná kinetická energie na jednu částici při teplotě $T$ je $\cfrac{1}{2}m\langle v^2 \rangle = \cfrac{1}{2}mv_{rms}^2 = \cfrac{3}{2}k_B T$ (pro $3$ stupně volnosti) a je určena pouze teplotou. Protože v plynu i plazmatu průměrná kinetická energie na částici úzce souvisí s teplotou a jde o vzájemně zaměnitelné veličiny, je v plazmové fyzice zvykem vyjadřovat teplotu v energetických jednotkách $\mathrm{eV}$. Aby se předešlo záměně rozměrů, místo průměrné kinetické energie $\langle E_k \rangle$ se teplota zapisuje jako hodnota $kT$.

Teplota $T$ odpovídající $kT=1\mathrm{eV}$ je:

$$ \begin{align*}
T\mathrm{[K]} &= \frac{1.6 \times 10^{-19}\mathrm{[J]}}{1.38 \times 10^{-23}\mathrm{[J/K]}} \\
&= 11600\mathrm{[K]}
\end{align*} \label{eqn:temp_conv_factor}\tag{7}$$

Takže v plazmové fyzice při vyjadřování teploty platí $1\mathrm{eV}=11600\mathrm{K}$.  
Např.) plazma o teplotě $2\mathrm{eV}$ má $kT=2\mathrm{eV}$ a průměrná kinetická energie na částici je $\cfrac{3}{2}kT=3\mathrm{eV}$.

Plazma navíc může mít současně několik různých teplot. V plazmatu je četnost srážek ion–ion nebo elektron–elektron větší než četnost srážek mezi elektrony a ionty; proto mohou elektrony a ionty dosáhnout tepelné rovnováhy každé zvlášť, při odlišných teplotách (elektronová teplota $T_e$ a iontová teplota $T_i$), a mohou vytvářet samostatná Maxwellova–Boltzmannova rozdělení. V některých situacích se $T_e$ a $T_i$ mohou výrazně lišit. Dokonce i při působení vnějšího magnetického pole $\vec{B}$ může mít tentýž druh částic (např. ionty) různé teploty $T_\perp$ a $T_\parallel$, protože velikost Lorentzovy síly (Lorentz force) závisí na tom, zda je směr pohybu rovnoběžný, nebo kolmý k magnetickému poli.

## Vztah mezi teplotou, tlakem a hustotou
Podle stavové rovnice ideálního plynu platí

$$ PV = \left(\frac{N}{N_A}\right)RT = NkT \label{eqn:ideal_gas_law}\tag{8}$$

a z toho

$$ \begin{gather*}
P = \frac{NkT}{V} = nkT, \\
n = \frac{P}{kT} 
\end{gather*} \label{eqn:relation_between_T_P_n}\tag{9}$$

tedy hustota plazmatu je nepřímo úměrná teplotě ($kT$) a přímo úměrná tlaku ($P$).

## Klasifikace plazmatu: nízkoteplotní plazma vs. vysokoteplotní plazma

| Nízkoteplotní<br> netepelné (studené) plazma | Nízkoteplotní tepelné<br> (studené) plazma | Vysokoteplotní<br> (horké) plazma |
| --- | --- | --- |
| $T_i \approx T \approx 300 \mathrm{K}$<br>$T_i \ll T_e \leqslant 10^5 \mathrm{K}$ | $T_i \approx T_e \approx T < 2 \times 10^4 \mathrm{K}$ | $T_i \approx T_e > 10^6 \mathrm{K}$ |
| Nízký tlak ($\sim 100\mathrm{Pa}$)<br> doutnavý výboj a oblouk | Oblouky při $100\mathrm{kPa}$ ($1\mathrm{atm}$) | Kinetické plazma, fúzní plazma |

### Teplota plazmatu
Označme elektronovou teplotu $T_e$, iontovou teplotu $T_i$ a teplotu neutrálních částic $T_g$. Pak:

- nízkoteplotní plazma: $T_e \mathrm{(>10,000 K)} \gg T_i \approx T_g \mathrm{(\sim 100 K)}$ $\rightarrow$ nerovnovážné plazma (non-equilibrium plasma)
- vysokoteplotní (tepelné) plazma: $T_e \approx T_i \approx T_g \mathrm{(>10,000 K)}$ $\rightarrow$ rovnovážné plazma (equilibrium plasma)

### Hustota plazmatu
Označme elektronovou hustotu $n_e$, iontovou hustotu $n_i$ a hustotu neutrálních částic $n_g$. Pak:

- nízkoteplotní plazma: $n_g \gg n_i \approx n_e$ $\rightarrow$ malý stupeň ionizace, většina částic je neutrálních
- vysokoteplotní (tepelné) plazma: $n_g \approx n_i \approx n_e $ $\rightarrow$ velký stupeň ionizace

### Tepelná kapacita plazmatu (jak moc je „horké“?)
- nízkoteplotní plazma: elektronová teplota je vysoká, ale hustota nízká a většina částic jsou relativně chladné neutrály, takže tepelná kapacita je malá a plazma není „horké“
- vysokoteplotní (tepelné) plazma: elektrony, ionty i neutrály mají vysokou teplotu, takže tepelná kapacita je velká a plazma je horké
