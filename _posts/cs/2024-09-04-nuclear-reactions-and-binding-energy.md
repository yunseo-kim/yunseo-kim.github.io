---
title: "Jaderné reakce a vazebná energie"
description: "Seznámíme se se zápisem jaderných reakcí a definicí Q-hodnoty (Q-value), pojmy hmotnostní defekt (mass defect) a vazebná energie (binding energy)."
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---

## Jaderná reakce (Nuclear Reaction)

### Základní zákony v jaderných reakcích

*Jaderná reakce (nuclear reaction)*: reakce, při níž se srazí dvě různá atomová jádra nebo atomové jádro s nukleonem a vzniknou dva či více nových jaderných částic a/nebo gama záření

Předpokládejme, že dvě atomová jádra $a$, $b$ zareagují a jako produkty vzniknou atomová jádra nebo gama záření $c$, $d$. Tuto reakci vyjádříme následovně:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

V jaderných reakcích platí následující čtyři základní zákony:

- *Zákon zachování nukleonového čísla (conservation of nucleon)*: celkový počet nukleonů je před i po reakci stejný. Druh nukleonů se může měnit, takže počet protonů a neutronů se nezachovává každý zvlášť.
- *Zákon zachování elektrického náboje (conservation of charge)*: celkový elektrický náboj částic je před i po reakci stejný.
- *Zákon zachování hybnosti (conservation of momentum)*: celková hybnost částic je před i po reakci stejná.
- *Zákon zachování energie (conservation of energy)*: celková energie včetně <u>energie klidové hmotnosti</u> je před i po reakci stejná.

### Exotermická reakce (exothermic reaction) & endotermická reakce (endothermic reaction)

V jaderné reakci ve tvaru ($\ref{nuclear_reaction}$) je celková energie před reakcí součtem klidových hmotnostních energií a kinetických energií $a$ a $b$ a celková energie po reakci je součtem klidových hmotnostních energií a kinetických energií $c$ a $d$. Proto ze zákona zachování energie plyne:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Po úpravě dostaneme:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Tedy rozdíl kinetických energií před a po jaderné reakci je roven rozdílu klidových hmotností před a po reakci. Pravá strana posledního vztahu se nazývá *Q-hodnota (Q-value)* jaderné reakce a definuje se takto:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

Q-hodnota se vždy uvádí v jednotkách MeV; protože klidová hmotnostní energie odpovídající 1 amu je obvykle 931 MeV, lze Q-hodnotu zapsat také:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Exotermická reakce (exothermic reaction)*: jaderná reakce s $Q>0$; část hmotnosti se přemění na kinetickou energii, takže kinetická energie po reakci vzroste.
- *Endotermická reakce (endothermic reaction)*: jaderná reakce s $Q<0$; část kinetické energie se přemění na hmotnost, takže kinetická energie po reakci klesne.

| Typ jaderné reakce | Q-hodnota | Změna hmotnosti před/po | Změna kinetické energie před/po |
| :---: | :---: | :---: | :---: |
| exotermická | $Q>0$ | $\Delta m<0$ (pokles) | $\Delta E>0$ (nárůst) |
| endotermická | $Q<0$ | $\Delta m>0$ (nárůst) | $\Delta E<0$ (pokles) |

### Zjednodušený zápis jaderné reakce

Jadernou reakci ve tvaru ($\ref{nuclear_reaction}$) lze zjednodušeně zapsat:

$$ a(b, c)d $$

což znamená jadernou reakci, v níž do $a$ dopadá $b$, je vyzářeno $c$ a $a$ se přemění na $d$.

#### ex)

- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Vazebná energie (Binding Energy)

### Hmotnostní defekt (Mass Defect)

Hmotnost každého jádra je o něco menší než součet hmotností neutronů a protonů, které ho tvoří. Tento rozdíl se nazývá *hmotnostní defekt (mass defect)*.

Označíme-li hmotnost jádra jako $M_A$, pak hmotnostní defekt $\Delta$ libovolného jádra lze spočítat:

$$ \Delta = ZM_p + NM_n - M_A. $$

Vyjádříme-li hmotnostní defekt $\Delta$ v jednotkách energie, získáme energii potřebnou k rozštěpení daného jádra na jeho nukleony. V tom smyslu, že jde o energii „držíci“ nukleony pohromadě, se tato energie nazývá *vazebná energie (bindig energy)*. Naopak, vzniká-li atomové jádro z $A$ nukleonů, energetická hladina se o vazebnou energii $\Delta$ sníží, a v průběhu jaderné reakce se odpovídající energie vyzáří do okolí.

### Průměrná vazebná energie na nukleon

Celková vazebná energie jádra s rostoucím hmotnostním číslem $A$ roste, avšak její sklon není konstantní.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
Průměrná vazebná energie na nukleon $\Delta/A$ u malých hmotnostních čísel prudce roste, avšak u těžkých jader s $A\geq56$ podle obrázku klesá pozvolným sklonem.

### Vztah mezi Q-hodnotou reakce a vazebnou energií

V jaderné reakci ($\ref{nuclear_reaction}$) je vazebná energie jádra $a$

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

a hmotnost $a$ je

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

Stejným způsobem pro jádra $b$, $c$, $d$ platí:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Dále uvažujme, že

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

a po dosazení výše uvedených vztahů do ($\ref{Q_value}$) dostaneme:

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

To znamená, že když se v důsledku jaderné reakce spojí dvě méně stabilní jádra a vznikne stabilnější jádro, vždy se uvolní energie.

### Jaderná fúze (Nuclear Fusion) a jaderné štěpení (Nuclear Fission)

U jaderné reakce, v níž se deuterium s vazebnou energií $2.23\text{MeV}$ a tritium s vazebnou energií $8.48\text{MeV}$ spojí za vzniku $^4\text{He}$ s vazebnou energií $28.3\text{MeV}$ a uvolní se jeden neutron:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

se energie odpovídající rozdílu vazebných energií $28.3-(2.23+8.48)=17.6\text{MeV}$ (tj. $3.52\text{MeV}$ na nukleon) uvolní ve formě kinetické energie jádra helia a neutronu.

Reakce, při níž se jako ve ($\ref{nuclear_fusion}$) spojí dvě lehká jádra s malým hmotnostním číslem a vytvoří těžší jádro s větším hmotnostním číslem než před reakcí, se nazývá *jaderná fúze (nuclear fusion)*. Jde o zdroj energie Slunce i všech hvězd a jednou přijde den, kdy ji lidstvo bude schopno využívat přímo jako zdroj výkonu.

Na druhé straně, u jaderné reakce, v níž $^{235}\text{U}$ s vazebnou energií přibližně $1780\text{MeV}$ po pohlcení neutronu přejde na $^{92}\text{Kr}$ s vazebnou energií $783\text{MeV}$ a $^{141}\text{Ba}$ s vazebnou energií přibližně $1170\text{MeV}$ a uvolní tři neutrony:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

se uvolní energie odpovídající rozdílu vazebných energií $783+1170-1780=173\text{MeV}$ (tj. $0.733\text{MeV}$ na nukleon).

Reakce, při níž se jako ve ($\ref{nuclear_fission}$) těžké jádro rozdělí na lehčí jádra, se nazývá *jaderné štěpení (nuclear fission)* a od projevu 34. prezidenta USA Dwighta D. Eisenhowera „Mírové využití atomu (Atoms for Peace)“ a od sovětské jaderné elektrárny Obninsk se široce využívá jako zdroj elektrické energie.

## Magická čísla

Pokud je počet neutronů nebo počet protonů v jádře roven 2, 6, 8, 14, 20, 28, 50, 82 nebo 126, má takové jádro tendenci být obzvlášť stabilní. Taková nukleonová čísla se nazývají *magická čísla (magic number)*. Odpovídají počtu neutronů a protonů potřebných k zaplnění nukleonových slupek v jádře a jsou analogická zaplňování elektronových slupek mimo jádro.

Nuklidy odpovídající magickým číslům se v jaderném inženýrství někdy prakticky využívají. Typickým příkladem je zirkonium-90 s 50 neutrony ($^{90}_{40} \mathrm{Zr}$), které je stabilní a má vlastnost málo pohlcovat neutrony, takže se široce používá například jako materiál pokrytí (cladding) palivových proutků v aktivní zóně reaktoru.
