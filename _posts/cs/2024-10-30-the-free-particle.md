---
title: Volná částice (The Free Particle)
description: Pro volnou částici s V(x)=0 ukážeme, proč separované řešení nelze normalizovat a co to fyzikálně znamená; kvalitativně odvodíme vztah neurčitostí poloha–hybnost pro obecné řešení a spočítáme fázovou i grupovou rychlost Ψ(x,t) včetně interpretace.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Volná částice: $V(x)=0$, bez okrajových podmínek (libovolná energie)
> - Separované řešení $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ při kvadratické integraci diverguje do nekonečna, a tedy jej nelze normalizovat; to naznačuje:
>   - volná částice nemůže existovat jako stacionární stav
>   - volná částice nemůže mít energii přesně definovanou jedinou hodnotou (existuje energetická neurčitost)
> - Přesto je obecné řešení časově závislé Schrödingerovy rovnice lineární kombinací separovaných řešení, takže separované řešení má stále významný matematický smysl. V tomto případě však neexistují omezující podmínky, takže obecné řešení není součtem ($\sum$) přes diskrétní proměnnou $n$, ale integrálem ($\int$) přes spojitou proměnnou $k$.
> - Obecné řešení Schrödingerovy rovnice:
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{kde }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - Vztah mezi neurčitostí polohy a neurčitostí hybnosti:
>   - když se zmenšuje neurčitost polohy, roste neurčitost hybnosti; a naopak, když se zmenšuje neurčitost hybnosti, roste neurčitost polohy
>   - tj. v kvantové mechanice není možné znát současně přesně polohu i hybnost volné částice
> - Fázová a grupová rychlost vlnové funkce $\Psi(x,t)$:
>   - fázová rychlost: $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - grupová rychlost: $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - Fyzikální význam grupové rychlosti a srovnání s klasickou mechanikou:
>   - fyzikálně grupová rychlost přímo odpovídá rychlosti pohybu dané částice
>   - pokud předpokládáme, že $\phi(k)$ je velmi špičatá kolem nějaké hodnoty $k_0$ (tj. neurčitost hybnosti je dostatečně malá),
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Prerequisites
- Eulerův vzorec
- Fourierova transformace (Fourier transform) a Plancherelova věta (Plancherel's theorem)
- [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/)
- [Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/)
- [Jednorozměrná nekonečná čtvercová jáma](/posts/the-infinite-square-well/)

## Nastavení modelu
Podívejme se na nejjednodušší případ, volnou částici ($V(x)=0$). Klasicky je to pouze rovnoměrný přímočarý pohyb, ale v kvantové mechanice je tato úloha zajímavější.  
[Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/) pro volnou částici má tvar

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

tj.

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, kde }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

To je stejné jako „uvnitř“ nekonečné čtvercové jámy s potenciálem $0$ [až po tuto část](/posts/the-infinite-square-well/#nastaveni-modelu-a-okrajovych-podminek). Jenže tentokrát zapíšeme obecné řešení v exponenciálním tvaru

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> Zápisy $Ae^{ikx} + Be^{-ikx}$ a $C\cos{kx}+D\sin{kx}$ jsou ekvivalentní způsoby, jak popsat tutéž funkci proměnné $x$. Z Eulerova vzorce $e^{ix}=\cos{x}+i\sin{x}$ plyne
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> Tedy při volbě $C=A+B$, $D=i(A-B)$ dostaneme
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> Naopak lze $A$ a $B$ vyjádřit pomocí $C$ a $D$ jako $A=\cfrac{C-iD}{2}$, $B=\cfrac{C+iD}{2}$.
>
> V kvantové mechanice pro $V=0$ exponenciální funkce popisují postupující vlny, a při práci s volnou částicí jsou nejpohodlnější. Naopak funkce sinus a kosinus se snadno interpretují jako stojaté vlny a v případě nekonečné čtvercové jámy se objevují přirozeně.
{: .prompt-info }

Na rozdíl od nekonečné čtvercové jámy zde neexistují žádné okrajové podmínky, které by omezovaly $k$ a $E$. Volná částice tedy může mít libovolnou kladnou energii.

## Separované řešení a fázová rychlost
Pokud k $\psi(x)$ připojíme časovou závislost $e^{-iEt/\hbar}$, dostaneme

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

Obecně platí, že libovolná funkce proměnných $x$ a $t$, která závisí na speciálním tvaru $(x\pm vt)$, popisuje vlnu, jejíž tvar se nemění a která se pohybuje rychlostí $v$ ve směru $\mp x$. Proto první člen v ($\ref{eqn:Psi_seperated_solution}$) popisuje vlnu postupující doprava a druhý člen vlnu se stejnou vlnovou délkou i rychlostí šíření, ale s jinou amplitudou, která postupuje doleva. Protože se liší pouze znaménkem před $k$, lze psát

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

a směr šíření vlny podle znaménka $k$ je

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{pohyb doprava}, \\
k<0 \Rightarrow & \text{pohyb doleva}.
\end{cases} \tag{6}$$

„Stacionární stav“ volné částice je zjevně postupující vlnou*, s vlnovou délkou $\lambda = 2\pi/\|k\|$, a podle de Broglieho vztahu (de Broglie formula)

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

má hybnost $p$.

> *Že je to „stacionární stav“, a přitom postupující vlna, je fyzikálně zjevný rozpor. Důvod uvidíme hned.
{: .prompt-info }

Rychlost této vlny je

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(kde $\omega$ je koeficient u $t$, tj. $\cfrac{\hbar k^2}{2m}$).

Tuto vlnovou funkci však nelze normalizovat, protože její kvadratický integrál diverguje do nekonečna:

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

Tedy <u>v případě volné částice separované řešení nepředstavuje fyzikálně realizovatelný stav.</u> Volná částice nemůže existovat jako [stacionární stav](/posts/time-independent-schrodinger-equation/#1-jsou-to-stacionarni-stavy-stationary-states) ani nemůže mít [nějakou konkrétní hodnotu energie](/posts/time-independent-schrodinger-equation/#2-nejde-o-pravdepodobnostni-rozdeleni-s-rozsahem-ale-o-stav-s-jednoznacnou-celkovou-energii-e). Ostatně i intuitivně: pokud nejsou na obou koncích žádné okrajové podmínky, je ještě divnější očekávat vznik stojaté vlny.

## Nalezení obecného řešení časově závislé Schrödingerovy rovnice $\Psi(x,t)$
Přesto má toto separované řešení stále důležitý význam: nezávisle na fyzikální interpretaci má totiž matematický význam, že [obecné řešení časově závislé Schrödingerovy rovnice je lineární kombinací separovaných řešení](/posts/time-independent-schrodinger-equation/#3-obecne-reseni-casove-zavisle-schrodingerovy-rovnice-je-linearni-kombinace-reseni-ziskanych-separaci-promennych). Jelikož zde ale nejsou žádná omezení, má obecné řešení místo součtu ($\sum$) přes diskrétní proměnnou $n$ tvar integrálu ($\int$) přes spojitou proměnnou $k$.

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> Zde $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ hraje stejnou roli jako $c_n$ ve [vzorci (21) v příspěvku „Časově nezávislá Schrödingerova rovnice“](/posts/time-independent-schrodinger-equation/#3-obecne-reseni-casove-zavisle-schrodingerovy-rovnice-je-linearni-kombinace-reseni-ziskanych-separaci-promennych).
{: .prompt-info }

Tuto vlnovou funkci lze pro vhodné $\phi(k)$ normalizovat, ale nutně musí mít nenulový rozsah v $k$, a tedy i rozsah energií a rychlostí. Tomu se říká **vlnový balík (wave packet)**.

> Sinusová vlna je prostorově rozprostřená do nekonečna, a proto ji nelze normalizovat. Když ale takové vlny složíme (superponujeme) ve větším počtu, interference je zlokalizuje a výslednou funkci lze normalizovat.
{: .prompt-info }

## Určení $\phi(k)$ pomocí Plancherelovy věty (Plancherel theorem)

Jelikož známe tvar $\Psi(x,t)$ (rovnice [$\ref{eqn:Psi_general_solution}$]), stačí už jen určit $\phi(k)$ tak, aby byla splněna počáteční podmínka

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

To je typická úloha Fourierovy analýzy (Fourier analysis) a odpověď dává **Plancherelova věta (Plancherel's theorem)**:

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$ se nazývá **Fourierova transformace (Fourier transform)** funkce $f(x)$ a $f(x)$ se nazývá **inverzní Fourierova transformace (inverse Fourier transform)** funkce $F(k)$. Z ($\ref{eqn:plancherel_theorem}$) je snadno vidět, že se liší pouze znaménkem v exponentu. Samozřejmě existuje omezující podmínka, že jsou dovoleny jen funkce, pro které integrál existuje.

> Nutná a postačující podmínka pro existenci $f(x)$ je, aby $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ bylo konečné. V tom případě je konečné i $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ a platí
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> Podle některých autorů se „Plancherelovou větou“ nenazývá rovnice ($\ref{eqn:plancherel_theorem}$), ale právě vztah výše (takto je to uvedeno i na [Wikipedii](https://en.wikipedia.org/wiki/Plancherel_theorem)).
{: .prompt-info }

V našem případě musí být $\Psi(x,0)$ z fyzikálních důvodů normalizovatelná, takže integrál určitě existuje. Kvantově-mechanické řešení pro volnou částici je tedy rovnice ($\ref{eqn:Psi_general_solution}$), kde

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> V praxi však téměř nikdy nelze analyticky vypočítat integrál v ($\ref{eqn:Psi_general_solution}$). Obvykle se hodnoty získávají numericky na počítači.
{: .prompt-tip }

## Výpočet grupové rychlosti vlnového balíku a fyzikální interpretace

Vlnový balík je v podstatě superpozice velkého množství sinusových vln, jejichž amplitudy určuje $\phi$. Tj. uvnitř „obalu (envelope)“ vlnového balíku jsou „vlnky (ripples)“.

![Vlnový balík s grupovou rychlostí větší (5×) než fázová rychlost](/physics-visualizations/figs/wave_packet.webp)
> *Oznámení o licenci obrázku a zdroji originálu*
> - zdrojový kód pro generování obrázku (Python3): [yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/wave_packet.py)
> - zdrojový kód pro generování obrázku (gnuplot): [yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/wave_packet.plt)
> - licence: [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)
> - původní autor: [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - původní oznámení licence: [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

Fyzikálně rychlosti částice neodpovídá rychlost jednotlivých „vlnkových“ složek (tj. **fázová rychlost, phase velocity**) vypočtená dříve ve ($\ref{eqn:phase_velocity}$), ale rychlost vnějšího obalu, tj. **grupová rychlost, group velocity**.

### Vztah mezi neurčitostí polohy a neurčitostí hybnosti
Podívejme se zvlášť jen na integrand $\int\phi(k)e^{ikx}dk$ ve ($\ref{eqn:Psi_at_t_0}$) a na integrand $\int\Psi(x,0)e^{-ikx}dx$ ve ($\ref{eqn:phi}$), abychom kvalitativně pochopili vztah mezi neurčitostí polohy a neurčitostí hybnosti.

#### Když je neurčitost polohy malá
Když je $\Psi$ v prostoru poloh rozložena v velmi úzké oblasti $[x_0-\delta, x_0+\delta]$ kolem nějaké hodnoty $x_0$ a mimo tuto oblast je blízká nule (<u>neurčitost polohy je malá</u>), pak $e^{-ikx} \approx e^{-ikx_0}$ je vůči $x$ téměř konstantní, a proto

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{eqn. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

Určitý integrál je vůči $p$ konstantní, takže díky členu $e^{-ipx_0/\hbar}$ nabývá $\phi$ v prostoru hybností tvaru sinusové vlny v proměnné $p$, tj. je rozprostřena přes široký interval hybností (<u>neurčitost hybnosti je velká</u>).

#### Když je neurčitost hybnosti malá
Analogicky, když je v prostoru hybností $\phi$ soustředěna do velmi úzké oblasti $[p_0-\delta, p_0+\delta]$ kolem nějaké hodnoty $p_0$ a mimo ni je blízká nule (<u>neurčitost hybnosti je malá</u>), pak z ($\ref{eqn:de_broglie_formula}$) plyne $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ (tj. vůči $p$ je to téměř konstanta) a protože $dk=\frac{1}{\hbar}dp$, dostáváme

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

Díky členu $e^{ip_0x/\hbar}$ má $\Psi$ v prostoru poloh tvar sinusové vlny v proměnné $x$, tj. je rozprostřena přes široký interval poloh (<u>neurčitost polohy je velká</u>).

#### Závěr
Když se zmenšuje neurčitost polohy, roste neurčitost hybnosti; a naopak, když se zmenšuje neurčitost hybnosti, roste neurčitost polohy. Proto v kvantové mechanice není možné znát současně přesně polohu i hybnost volné částice.

![ Postupující vlnové funkce v kvantové mechanice](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *Zdroj obrázku*
> - autor: uživatel anglické Wikipedie [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - licence: public domain

> Ve skutečnosti se to díky principu neurčitosti (uncertainty principle) netýká jen volné částice, ale všech případů. Princip neurčitosti proberu později v samostatném příspěvku.
{: .prompt-info }

### Grupová rychlost vlnového balíku
Když obecné řešení ($\ref{eqn:Psi_general_solution}$) přepíšeme stejně jako ve ($\ref{eqn:phase_velocity}$) pomocí $\omega \equiv \cfrac{\hbar k^2}{2m}$, dostaneme

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> Vztah typu $\omega = \cfrac{\hbar k^2}{2m}$, kde je $\omega$ vyjádřeno jako funkce $k$, se nazývá **disperzní relace (dispersion relation)**. Následující úvaha platí obecně pro všechny vlnové balíky bez ohledu na konkrétní disperzní relaci.
{: .prompt-info }

Předpokládejme nyní, že $\phi(k)$ je velmi špičatá kolem vhodné hodnoty $k_0$. (I kdyby byla v $k$ rozprostřena široce, takový vlnový balík se velmi rychle „rozpadá“ a mění tvar: složky s různými $k$ se pohybují různými rychlostmi, takže celek přestává mít smysl jako dobře definovaná „grupa“ s jednou rychlostí. Jinými slovy, <u>neurčitost hybnosti roste</u>.)  
Protože mimo okolí $k_0$ lze integrand zanedbat, můžeme v tomto okolí rozvinout $\omega(k)$ do Taylorovy řady; při ponechání jen lineárního členu dostaneme

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

Zavedeme substituci $s=k-k_0$ a integrujeme kolem $k_0$:

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

Přední člen $e^{i(k_0x-\omega_0t)}$ odpovídá sinusové vlně („vlnky“) pohybující se rychlostí $\omega_0/k_0$, zatímco integrální člen, který určuje amplitudu této sinusové vlny („obal“), se díky $e^{is(x-\omega_0^\prime t)}$ pohybuje rychlostí $\omega_0^\prime$. Tedy fázová rychlost v bodě $k=k_0$ je

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

což znovu potvrzuje hodnotu z ($\ref{eqn:phase_velocity}$), a grupová rychlost je

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

tedy dvojnásobek fázové rychlosti.

## Srovnání s klasickou mechanikou

Protože víme, že na makroskopických škálách platí klasická mechanika, výsledky získané z kvantové mechaniky se musí v limitě dostatečně malé kvantové neurčitosti aproximovat klasickým výsledkem. V případě volné částice, kterou zde řešíme, platí při našem předpokladu, že $\phi(k)$ je velmi špičatá kolem vhodné hodnoty $k_0$ (tj. <u>neurčitost hybnosti je dostatečně malá</u>), že grupová rychlost $v_\text{group}$ odpovídající rychlosti částice v kvantové mechanice musí být pro stejné $k$ a odpovídající energii $E$ rovna klasické rychlosti $v_\text{classical}$.

Dosadíme-li do právě získané grupové rychlosti (rovnice [$\ref{eqn:group_velocity}$]) vztah $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ z ($\ref{eqn:t_independent_schrodinger_eqn}$), dostaneme

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

a v klasické mechanice je rychlost volné částice s kinetickou energií $E$ rovněž

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

Tedy $v_\text{quantum}=v_\text{classical}$, a tím ověřujeme, že výsledek získaný aplikací kvantové mechaniky je fyzikálně konzistentní.
