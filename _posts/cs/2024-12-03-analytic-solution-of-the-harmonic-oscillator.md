---
title: Analytické řešení harmonického oscilátoru (The Harmonic Oscillator)
description: V kvantové mechanice sestavíme Schrödingerovu rovnici pro harmonický oscilátor a projdeme její analytické řešení. Zavedeme bezrozměrnou proměnnou 𝜉 a stacionární stavy vyjádříme pomocí Hermitových polynomů.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hermite Polynomials]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Pokud je amplituda dostatečně malá, lze libovolné kmitání aproximovat jako jednoduché harmonické kmitání (simple harmonic oscillation); díky tomu má v fyzice zásadní význam
> - Harmonický oscilátor: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - Zavedeme bezrozměrnou proměnnou $\xi$ a energii $K$ vyjádřenou v jednotkách $\cfrac{1}{2}\hbar\omega$:
>   - $\xi \equiv \sqrt{\cfrac{m\omega}{\hbar}}x$
>   - $K \equiv \cfrac{2E}{\hbar\omega}$
>   - $ \cfrac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi $
> - Pro $\|\xi\|^2 \to \infty$ je fyzikálně přípustné asymptotické řešení $\psi(\xi) \to Ae^{-\xi^2/2}$, takže
>
> $$ \begin{gather*}
> \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(kde }\lim_{\xi\to\infty}h(\xi)=A\text{)}, \\
> \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0
> \end{gather*} $$
>
> - Vyjádříme-li řešení této rovnice ve tvaru řady $ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j$, dostaneme
>
> $$ a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j $$
>
> - Aby bylo řešení normovatelné, musí být řada $\sum a_j$ konečná; tj. existuje nějaké „největší“ $j$ s hodnotou $n\in \mathbb{N}$ tak, že pro $j>n$ je $a_j=0$, a tedy
>   - $ K = 2n + 1 $
>   - $ E_n = \left(n+\cfrac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots $
> - Obecně je $h_n(\xi)$ polynom $n$-tého stupně v $\xi$; po odfiltrování předního koeficientu ($a_0$ nebo $a_1$) se zbytek nazývá **Hermitovy polynomy (Hermite polynomials)** $H_n(\xi)$
>
> $$ h_n(\xi) = 
> \begin{cases}
> a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
> a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
> \end{cases} $$
>
> - Normované stacionární stavy harmonického oscilátoru:
>
> $$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2} $$
>
> - Vlastnosti kvantového oscilátoru
>   - jako vlastní funkce se střídají sudé a liché funkce
>   - i v oblastech klasicky zakázaných (tj. pro $x$ větší než klasická amplituda odpovídající dané energii $E$) není pravděpodobnost nalezení nulová; sice malá, ale částice se tam může nacházet
>   - pro všechny stacionární stavy s lichým $n$ je pravděpodobnost nalezení částice v centru nulová
>   - s rostoucím $n$ se chování blíží klasickému oscilátoru
{: .prompt-info }

## Předpoklady
- [Metoda separace proměnných](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfestova věta](/posts/ehrenfest-theorem/)
- [Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/)
- [1D nekonečná potenciálová jáma](/posts/the-infinite-square-well/)
- [Algebraické řešení harmonického oscilátoru](/posts/algebraic-solution-of-the-harmonic-oscillator/)

## Nastavení modelu
Způsob popisu harmonického oscilátoru v klasické mechanice a význam této úlohy viz [předchozí článek](/posts/algebraic-solution-of-the-harmonic-oscillator/).

### Harmonický oscilátor v kvantové mechanice
Úloha kvantově-mechanického harmonického oscilátoru spočívá v řešení Schrödingerovy rovnice pro potenciál

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{1}$$

[Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/) pro harmonický oscilátor má tvar

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

K řešení tohoto problému existují dva zcela odlišné přístupy. Jeden je analytická metoda (analytic method) využívající **mocninnou řadu (power series)**, druhý je algebraická metoda (algebraic method) využívající **žebříčkové operátory (ladder operators)**. Algebraická metoda je rychlejší a jednodušší, ale i analytické řešení pomocí mocninných řad má smysl studovat. [Algebraický postup jsme už probrali](/posts/algebraic-solution-of-the-harmonic-oscillator/) a zde se zaměříme na analytické řešení.

## Úprava Schrödingerovy rovnice
Zaveďme bezrozměrnou proměnnou

$$ \xi \equiv \sqrt{\frac{m\omega}{\hbar}}x \label{eqn:xi}\tag{3}$$

Pak lze časově nezávislou Schrödingerovu rovnici ($\ref{eqn:t_independent_schrodinger_eqn}$) jednoduše přepsat do tvaru

$$ \frac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi. \label{eqn:schrodinger_eqn_with_xi}\tag{4}$$

kde $K$ je energie vyjádřená v jednotkách $\cfrac{1}{2}\hbar\omega$:

$$ K \equiv \frac{2E}{\hbar\omega}. \label{eqn:K}\tag{5}$$

Nyní stačí vyřešit takto přepsanou rovnici ($\ref{eqn:schrodinger_eqn_with_xi}$). Nejprve si všimněme, že pro velmi velké $\xi$ (tj. pro velmi velké $x$) platí $\xi^2 \gg K$, takže

$$ \frac{d^2\psi}{d\xi^2} \approx \xi^2\psi \label{eqn:schrodinger_eqn_approx}\tag{6}$$

a její přibližné řešení je

$$ \psi(\xi) \approx Ae^{-\xi^2/2} + Be^{\xi^2/2} \label{eqn:psi_approx}\tag{7}$$

Jenže člen s $B$ diverguje pro $\|x\|\to \infty$, takže jej nelze normovat; fyzikálně přípustné asymptotické řešení je proto

$$ \psi(\xi) \to Ae^{-\xi^2/2} \label{eqn:psi_asymp}\tag{8}$$

Nyní oddělme exponenciální část a pišme

$$ \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(kde }\lim_{\xi\to\infty}h(\xi)=A\text{)} \label{eqn:psi_and_h}\tag{9}$$

> Exponenciální člen $e^{-\xi^2/2}$ jsme odhalili tak, že jsme v průběhu odvození použili aproximaci k nalezení tvaru asymptotického řešení; výsledný vztah ($\ref{eqn:psi_and_h}$) však není přibližný, ale přesný. Takové oddělení asymptotického tvaru je standardní první krok při řešení diferenciálních rovnic pomocí mocninných řad.
{: .prompt-info }

Zderivujeme-li ($\ref{eqn:psi_and_h}$) a určíme $\cfrac{d\psi}{d\xi}$ a $\cfrac{d^2\psi}{d\xi^2}$, dostaneme

$$ \begin{gather*}
\frac{d\psi}{d\xi} = \left(\frac{dh}{d\xi}-\xi h \right)e^{-\xi^2/2}, \\
\frac{d^2\psi}{d\xi^2} = \left(\frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(\xi^2-1)h \right)e^{-\xi^2/2}
\end{gather*} $$

a tedy Schrödingerova rovnice ($\ref{eqn:schrodinger_eqn_with_xi}$) přejde na

$$ \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0 \label{eqn:schrodinger_eqn_with_h}\tag{10}$$

## Rozvoj do mocninné řady
Podle Taylorovy věty (Taylor's theorem) lze libovolnou hladkou funkci vyjádřit jako mocninnou řadu, takže zkusme hledat řešení rovnice ($\ref{eqn:schrodinger_eqn_with_h}$) ve tvaru řady v $\xi$:

$$ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j \label{eqn:h_series_exp}\tag{11}$$

Zderivováním jednotlivých členů této řady dostaneme

$$ \begin{gather*}
\frac{dh}{d\xi} = a_1 + 2a_2\xi + 3a_3\xi^2 + \cdots = \sum_{j=0}^{\infty}ja_j\xi^{j-1}, \\
\frac{d^2 h}{d\xi^2} = 2a_2 + 2\cdot3a_3\xi + 3\cdot4a_4\xi^2 + \cdots = \sum_{j=0}^{\infty} (j+1)(j+2)a_{j+2}\xi^j.
\end{gather*} $$

Dosadíme-li tyto výrazy zpět do Schrödingerovy rovnice (rovnice [$\ref{eqn:schrodinger_eqn_with_h}$]), získáme

$$ \sum_{j=0}^{\infty}[(j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j]\xi^j = 0. \label{eqn:schrodinger_eqn_power_series}\tag{12}$$

Z jednoznačnosti rozvoje do mocninné řady musí být koeficient u každé mocniny $\xi$ roven $0$, tedy

$$ (j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j = 0 $$

$$ \therefore a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j. \label{eqn:recursion_formula}\tag{13}$$

Tento **rekurzní vztah (recursion formula)** je ekvivalentní Schrödingerově rovnici. Jsou-li dány dvě libovolné konstanty $a_0$ a $a_1$, lze určit všechny koeficienty řešení $h(\xi)$.

Ne každé takto získané řešení však lze normovat. Pokud je řada $\sum a_j$ nekonečná (tj. $\lim_{j\to\infty} a_j\neq0$), pak pro velmi velké $j$ lze výše uvedený rekurzní vztah aproximovat jako

$$ a_{j+2} \approx \frac{2}{j}a_j $$

a přibližné řešení je

$$ a_j \approx \frac{C}{(j/2)!} \quad \text{(}C\text{ je libovolná konstanta)}$$

V takovém případě pro velké $\xi$, kde dominují vyšší členy, vychází

$$ h(\xi) \approx C\sum\frac{1}{(j/2)!}\xi^j \approx C\sum\frac{1}{j!}\xi^{2j} \approx Ce^{\xi^2} $$

a pak je podle ($\ref{eqn:psi_and_h}$) $\psi(\xi)$ tvaru $Ce^{\xi^2/2}$, takže diverguje pro $\xi \to \infty$. To odpovídá nenormovatelnému řešení v ($\ref{eqn:psi_approx}$) s $A=0, B\neq0$.

Proto musí být řada $\sum a_j$ konečná. Musí existovat nějaké „největší“ $j$ s hodnotou $n\in \mathbb{N}$ tak, že pro $j>n$ je $a_j=0$. Aby k tomu došlo, musí pro nenulové $a_n$ platit $a_{n+2}=0$, a z ($\ref{eqn:recursion_formula}$) tedy plyne, že

$$ K = 2n + 1 $$

Dosadíme-li to do ($\ref{eqn:K}$), získáme fyzikálně přípustné energie

$$ E_n = \left(n+\frac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots \label{eqn:E_n}\tag{14}$$

Tím jsme úplně jinou metodou znovu odvodili kvantizační podmínku energie z rovnice (21) v části [Algebraické řešení harmonického oscilátoru](/posts/algebraic-solution-of-the-harmonic-oscillator/#stacionární-stav-psi_n-a-energetická-hladina-e_n).

## Hermitovy polynomy (Hermite polynomials) $H_n(\xi)$ a stacionární stavy $\psi_n(x)$
### Hermitovy polynomy $H_n$
Obecně je $h_n(\xi)$ polynom $n$-tého stupně v $\xi$; pokud je $n$ sudé, obsahuje pouze sudé mocniny, a pokud je $n$ liché, obsahuje pouze liché mocniny. Po odfiltrování předního koeficientu ($a_0$ nebo $a_1$) se zbytek nazývá **Hermitovy polynomy (Hermite polynomials)** $H_n(\xi)$.

$$ h_n(\xi) = 
\begin{cases}
a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
\end{cases} $$

Tradičně se koeficienty volí tak, aby koeficient u nejvyšší mocniny v $H_n$ byl $2^n$.

Následují první Hermitovy polynomy:

$$ \begin{align*}
H_0 &= 1 \\
H_1 &= 2\xi \\
H_2 &= 4\xi^2 - 2 \\
H_3 &= 8\xi^3 - 12\xi \\
H_4 &= 16\xi^4 - 48\xi^2 + 12 \\
H_5 &= 32\xi^5 - 160\xi^3 + 120\xi \\
&\qquad\vdots
\end{align*} $$

### Stacionární stavy $\psi_n(x)$
Normované stacionární stavy harmonického oscilátoru mají tvar

$$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2}. $$

To souhlasí s výsledkem získaným v části [Algebraické řešení harmonického oscilátoru](/posts/algebraic-solution-of-the-harmonic-oscillator/#normalizace) (rovnice [27]).

Následující obrázek ukazuje stacionární stavy $\psi_n(x)$ a pravděpodobnostní hustoty $\|\psi_n(x)\|^2$ pro prvních osm hodnot $n$. Je vidět, že jako vlastní funkce kvantového oscilátoru se střídají sudé a liché funkce.

![Reprezentace vlnové funkce pro prvních osm vázaných vlastních stavů, n = 0 až 7. Vodorovná osa značí polohu x.](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)

![Odpovídající pravděpodobnostní hustoty.](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - licence: Public Domain

Kvantový oscilátor se od odpovídajícího klasického oscilátoru výrazně liší: nejenže je energie kvantovaná, ale i pravděpodobnostní rozdělení polohy $x$ vykazuje podivuhodné vlastnosti.
- i v oblastech klasicky zakázaných (tj. pro $x$ větší než klasická amplituda odpovídající dané energii $E$) není pravděpodobnost nalezení nulová; sice malá, ale částice se tam může nacházet
- pro všechny stacionární stavy s lichým $n$ je pravděpodobnost nalezení částice v centru nulová

S rostoucím $n$ se kvantový oscilátor začíná chovat podobně jako oscilátor klasický. Následující obrázek ukazuje klasické pravděpodobnostní rozdělení polohy $x$ (čárkovaně) a kvantový stav $\|\psi_{30}\|^2$ pro $n=30$ (plná čára). Pokud „zubaté“ oscilace vhodně vyhladíme, oba grafy se zhruba shodují.

![Kvantové (plná čára) a klasické (čárkovaná čára) pravděpodobnostní rozdělení excitovaného stavu n = 30 kvantového harmonického oscilátoru. Svislé čárkované čáry označují klasické body obratu.](https://upload.wikimedia.org/wikipedia/commons/6/69/QHOn30pdf.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [AkanoToE](https://commons.wikimedia.org/wiki/User:AkanoToE)
> - licence: Public Domain

### Interaktivní vizualizace pravděpodobnostních rozdělení kvantového oscilátoru
Následuje responzivní vizualizace založená na Plotly.js, kterou jsem sám vytvořil. Pomocí posuvníku lze měnit hodnotu $n$ a sledovat tvar klasického pravděpodobnostního rozdělení polohy $x$ a také $\|\psi_n\|^2$.

<div class="plotly-iframe-container" style="position: relative; height: 850px; overflow: hidden;">
    <iframe id="plotly-iframe"
            src="/physics-visualizations/quantum-harmonic-oscillator.html"
            title="Kvantový harmonický oscilátor: hustota pravděpodobnosti"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; overflow:hidden" 
            allow="fullscreen"
            scrolling="no"
            loading="lazy">
    </iframe>
</div>

> - Původní stránka vizualizace: <a {% static_href %}href="{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html"{% endstatic_href %}>{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html</a>
> - Zdrojový kód: [repozitář yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/quantum-harmonic-oscillator.html)
> - Licence: [See here](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

Dále, pokud můžete na svém počítači používat Python a máte nainstalované knihovny Numpy, Plotly a Dash, můžete spustit Python skript [`/src/quantum_oscillator.py`{: .filepath}](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/quantum_oscillator.py) ve stejném repozitáři a zobrazit výsledky i takto.
