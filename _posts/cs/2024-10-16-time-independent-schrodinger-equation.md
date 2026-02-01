---
title: Časově nezávislá Schrödingerova rovnice (Time-independent Schrödinger Equation)
description: Aplikujeme separaci proměnných na původní (časově závislou) Schrödingerovu rovnici pro Ψ(x,t), odvodíme časově nezávislou rovnici pro ψ(x) a vysvětlíme matematický i fyzikální význam takto získaných řešení. Ukážeme také, jak z lineární kombinace separovatelných řešení sestavit obecné řešení.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Separované řešení: $ \Psi(x,t) = \psi(x)\phi(t)$
> - Časová závislost („wiggle factor“): $ \phi(t) = e^{-iEt/\hbar} $
> - Hamiltonián (Hamiltonian), operátor: $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - Časově nezávislá Schrödingerova rovnice: $ \hat H\psi = E\psi $
> - Fyzikální a matematický význam a důležitost separovaných řešení:
>   1. stacionární stavy (stationary states)
>   2. mají jednoznačnou hodnotu celkové energie $E$
>   3. obecné řešení Schrödingerovy rovnice je lineární kombinací separovaných řešení
> - Obecné řešení časově závislé Schrödingerovy rovnice: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Prerequisites
- spojité rozdělení pravděpodobnosti a hustota pravděpodobnosti
- [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfestova věta](/posts/ehrenfest-theorem/)
- [metoda separace proměnných](/posts/Separation-of-Variables/)

## Odvození pomocí separace proměnných
V [postu o Ehrenfestově větě](/posts/ehrenfest-theorem/) jsme si ukázali, jak pomocí vlnové funkce $\Psi$ počítat různé fyzikální veličiny, které nás zajímají. Klíčové tedy je, jak takovou vlnovou funkci $\Psi(x,t)$ získat; obvykle je třeba pro daný potenciál $V(x,t)$ vyřešit parciální diferenciální rovnici v proměnných poloha $x$ a čas $t$, tj. [Schrödingerovu rovnici](/posts/schrodinger-equation-and-the-wave-function/).

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

Pokud je potenciál $V$ nezávislý na čase $t$, lze výše uvedenou Schrödingerovu rovnici řešit pomocí [separace proměnných](/posts/Separation-of-Variables/). Uvažujme řešení vyjádřené jako součin funkce pouze proměnné $x$, tj. $\psi$, a funkce pouze proměnné $t$, tj. $\phi$:

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

Na první pohled jde o nepřiměřeně omezující tvar, takže by se mohlo zdát, že takto najdeme jen malou podmnožinu všech řešení. Ve skutečnosti však takto získaná řešení mají důležitý význam a navíc lze z těchto separovatelných řešení vhodným způsobem složit obecné řešení.

Pro separovatelná řešení platí

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

a po dosazení do rovnice ($\ref{eqn:schrodinger_eqn}$) lze Schrödingerovu rovnici psát jako

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

Po vydělení obou stran výrazem $\psi\phi$ dostaneme rovnici, jejíž levá strana je funkcí pouze $t$ a pravá strana je funkcí pouze $x$:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

Aby měla tato rovnice řešení, musejí být obě strany konstantní. Kdyby tomu tak nebylo, pak při fixaci jedné z proměnných ($t$ nebo $x$) a změně druhé by se změnila pouze jedna strana rovnosti, takže by rovnost přestala platit. Proto můžeme levou stranu položit rovnou separační konstantě $E$:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

Tím získáme dvě obyčejné diferenciální rovnice: jedna je pro čas $t$

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

a druhá je pro prostor $x$

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

Rovnice ($\ref{eqn:ode_t}$) pro $t$ se snadno vyřeší. Obecné řešení má tvar $ce^{-iEt/\hbar}$, ale protože nás ve výsledku zajímá součin $\psi\phi$ spíše než samotná $\phi$, můžeme konstantu $c$ zahrnout do $\psi$. Dostaneme tedy

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

Rovnice ($\ref{eqn:t_independent_schrodinger_eqn}$) pro $x$ se nazývá **časově nezávislá Schrödingerova rovnice (time-independent Schrödinger equation)**. K jejímu řešení je nutné znát potenciál $V(x)$.

## Fyzikální a matematický význam
Pomocí separace proměnných jsme výše získali funkci času $\phi(t)$ a časově nezávislou Schrödingerovu rovnici ($\ref{eqn:t_independent_schrodinger_eqn}$). Ačkoliv většinu řešení původní **časově závislé Schrödingerovy rovnice (time-dependent Schrödinger equation)** ($\ref{eqn:schrodinger_eqn}$) nelze zapsat ve tvaru $\psi(x)\phi(t)$, tvar časově nezávislé rovnice je přesto důležitý, protože její řešení mají následující tři vlastnosti.

### 1. Jsou to stacionární stavy (stationary states).
Samotná vlnová funkce

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

závisí na čase $t$, ale hustota pravděpodobnosti

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

má časová závislost vykrácenou, takže je v čase konstantní.

> Pro normalizovatelná řešení musí být separační konstanta $E$ reálná.
>
> Položíme-li v ($\ref{eqn:separation_of_variables}$) $E$ jako komplexní číslo $E_0+i\Gamma$ (kde $E_0$, $\Gamma$ jsou reálná),
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> Jak jsme viděli v části o [normalizaci vlnové funkce (normalization)](/posts/schrodinger-equation-and-the-wave-function/#normalizace-vlnove-funkce-normalization), $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ musí být konstanta nezávislá na čase, takže musí platit $\Gamma=0$. $\blacksquare$
{: .prompt-info }

Totéž nastává i při výpočtu střední hodnoty libovolné fyzikální veličiny: rovnice (8) z [Ehrenfestovy věty](/posts/ehrenfest-theorem/) přejde na

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

takže všechny střední hodnoty jsou v čase konstantní. Zejména je-li $\langle x \rangle$ konstanta, pak $\langle p \rangle=0$.

### 2. Jde o stav s jednou jednoznačnou hodnotou celkové energie $E$, nikoli o pravděpodobnostní rozdělení s určitým rozsahem.
V klasické mechanice se celková energie (kinetická plus potenciální) nazývá **Hamiltonián (Hamiltonian)** a definuje se jako

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

Nahradíme-li tedy $p$ výrazem $-i\hbar(\partial/\partial x)$, odpovídá tomu v kvantové mechanice Hamiltoniánový operátor

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

Časově nezávislou Schrödingerovu rovnici ($\ref{eqn:t_independent_schrodinger_eqn}$) pak lze psát jako

$$ \hat H \psi = E\psi \tag{15}$$

a střední hodnota Hamiltoniánu je

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

Dále platí

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

tedy

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

a rozptyl Hamiltoniánu $H$ je

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

To znamená, že při měření celkové energie separovaného řešení vždy vyjde stejná hodnota $E$.

### 3. Obecné řešení časově závislé Schrödingerovy rovnice je lineární kombinací separovaných řešení.

Časově nezávislá Schrödingerova rovnice ($\ref{eqn:t_independent_schrodinger_eqn}$) má nekonečně mnoho řešení $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$. Označme je \{$\psi_n(x)$\}. Pro každé z nich existuje separační konstanta $E_1,E_2,E_3,\dots=$\{$E_n$\}, takže každé **možné energetické hladině** odpovídá příslušná vlnová funkce.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

Časově závislá Schrödingerova rovnice ($\ref{eqn:schrodinger_eqn}$) má vlastnost, že lineární kombinace libovolných dvou řešení je opět řešením. Jakmile tedy najdeme separovaná řešení, můžeme rovnou získat obecnější tvar řešení

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

Všechna řešení časově závislé Schrödingerovy rovnice lze zapsat ve výše uvedeném tvaru; zbývá už jen najít vhodné konstanty $c_1, c_2, \dots$ tak, aby byla splněna počáteční podmínka daná v zadání, a tím určit konkrétní řešení, které nás zajímá. Jinými slovy: jakmile dokážeme vyřešit časově nezávislou Schrödingerovu rovnici, získání obecného řešení časově závislé Schrödingerovy rovnice je už jednoduché.

> Separované řešení
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> je stacionární stav, v němž jsou všechny pravděpodobnosti i střední hodnoty nezávislé na čase, ale všimněte si, že obecné řešení ($\ref{eqn:general_solution}$) tuto vlastnost obecně nemá.
{: .prompt-warning }

## Zákon zachování energie
V obecném řešení ($\ref{eqn:general_solution}$) má druhá mocnina absolutní hodnoty koeficientu $\|c_n\|^2$ fyzikální význam: je to pravděpodobnost, že při měření energie částice ve stavu ($\Psi$) naměříme hodnotu $E_n$. Součet těchto pravděpodobností tedy musí být

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

a střední hodnota Hamiltoniánu je

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

Protože energetické hladiny $E_n$ jednotlivých stacionárních stavů i koeficienty \{$c_n$\} jsou nezávislé na čase, je nezávislá na čase a konstantní i pravděpodobnost naměření konkrétní energie $E_n$ a rovněž střední hodnota Hamiltoniánu $H$.
