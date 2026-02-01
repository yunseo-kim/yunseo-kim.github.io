---
title: Jednorozměrná nekonečná čtvercová jáma (The 1D Infinite Square Well)
description: Probereme 1D nekonečnou potenciálovou jámu: vlastní funkce ψ_n(x), energie E_n, 4 klíčové matematické vlastnosti ψ(x) a obecné řešení Ψ(x,t).
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Úloha jednorozměrné nekonečné čtvercové jámy: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{jinak}
>   \end{cases}$$
> - Okrajové podmínky: $ \psi(0) = \psi(a) = 0 $
> - Energetické hladiny $n$-tého stacionárního stavu: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - Řešení časově nezávislé Schrödingerovy rovnice uvnitř jámy:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Fyzikální interpretace jednotlivých stacionárních stavů $\psi_n$: 
>   - tvar stojaté vlny na struně délky $a$
>   - **základní stav (ground state)**: stacionární stav $\psi_1$ s nejnižší energií
>   - **excitované stavy (excited states)**: zbývající stavy s $n\geq 2$, jejichž energie roste úměrně $n^2$
> - Čtyři důležité matematické vlastnosti $\psi_n$:
>   1. Pokud má potenciál $V(x)$ symetrii, pak se vzhledem ke středu jámy střídají sudé a liché funkce
>   2. S rostoucí energií má každý následující stav o jeden **uzel (node)** více
>   3. Platí **ortonormalita (orthonormality)**
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. Platí **úplnost (completeness)**
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - Obecné řešení Schrödingerovy rovnice (lineární kombinace stacionárních stavů):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{kde koeficienty }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## Prerequisites
- spojité rozdělení pravděpodobnosti a hustota pravděpodobnosti
- ortogonalita a normalizace (lineární algebra)
- Fourierovy řady a úplnost (lineární algebra)
- [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfestova věta](/posts/ehrenfest-theorem/)
- [Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/)

## Zadané podmínky pro potenciál
Je-li potenciál

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{jinak}
\end{cases} \tag{1}$$

pak je částice uvnitř tohoto potenciálu v oblasti $0<x<a$ volná částice a na obou koncích ($x=0$ a $x=a$) na ni působí nekonečně velká síla, takže nemůže uniknout. V klasickém modelu se to interpretuje jako nekonečný vratný pohyb tam a zpět, při němž se opakují dokonale pružné srážky a nepůsobí žádné neuchovávající síly. Ačkoli je takový potenciál krajně umělý a jednoduchý, právě proto může při pozdějším studiu kvantové mechaniky sloužit jako užitečný referenční příklad při zkoumání jiných fyzikálních situací, a je tedy třeba jej pečlivě projít.

![Infinite Potential Well](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## Nastavení modelu a okrajových podmínek
Mimo jámu je pravděpodobnost nalezení částice $0$, takže $\psi(x)=0$. Uvnitř jámy je $V(x)=0$, a proto [časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/) má tvar

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

tj.

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ kde } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

> Zde předpokládáme $E\geq 0$.
{: .prompt-info }

To je rovnice popisující klasický **jednoduchý harmonický oscilátor (simple harmonic oscillator)** a její obecné řešení je

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

kde $A$ a $B$ jsou libovolné konstanty. Při hledání konkrétního řešení odpovídajícího zadání se tyto konstanty typicky určují pomocí **okrajových podmínek**. <u>V případě $\psi(x)$ bývá okrajovou podmínkou obvykle spojitost jak $\psi$, tak $d\psi/dx$, avšak v místech, kde jde potenciál do nekonečna, je spojitá pouze $\psi$.</u>

## Nalezení řešení časově nezávislé Schrödingerovy rovnice

Protože $\psi(x)$ je spojitá,

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

a musí navazovat na řešení vně jámy. Z rovnice ($\ref{eqn:psi_general_solution}$) pro $x=0$ dostaneme

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

takže po dosazení ($\ref{eqn:boundary_conditions}$) musí platit $B=0$.

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

Pak $\psi(a)=A\sin{ka}$, a aby byla splněna podmínka $\psi(a)=0$ z ($\ref{eqn:boundary_conditions}$), musí být buď $A=0$ (triviální řešení), nebo $\sin{ka}=0$. Tedy

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

Stejně jako předtím je $k=0$ triviální řešení, protože vede na $\psi(x)=0$, které nelze normalizovat, a proto to není řešení, které v této úloze hledáme. Dále platí $\sin(-\theta)=-\sin(\theta)$, takže záporné znaménko lze absorbovat do konstanty $A$ v ($\ref{eqn:psi_without_B}$); proto neztrácíme obecnost, budeme-li uvažovat pouze případ $ka>0$. Možná řešení pro $k$ jsou tedy

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

Pak $\psi_n=A\sin{k_n x}$ a $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$, takže po dosazení do ($\ref{eqn:t_independent_schrodinger_eqn}$) vyjdou přípustné hodnoty $E$ takto:

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

V ostrém kontrastu s klasickým případem kvantová částice v nekonečné čtvercové jámě nemůže mít libovolnou energii, ale musí nabývat jedné z povolených hodnot.

> Okrajové podmínky aplikované na řešení časově nezávislé Schrödingerovy rovnice vedou ke kvantování energie.
{: .prompt-info }

Nyní můžeme $\psi$ znormalizovat a určit $A$.

> Původně se normalizuje $\Psi(x,t)$, ale podle rovnice (11) v příspěvku [Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/#1-jsou-to-stacionarni-stavy-stationary-states) to odpovídá normalizaci $\psi(x)$.
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

Tím je striktně určena pouze velikost $A$, ale fáze $A$ nemá žádný fyzikální význam, takže můžeme jednoduše vzít kladnou reálnou odmocninu jako $A$. Řešení uvnitř jámy tedy je

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

## Fyzikální interpretace jednotlivých stacionárních stavů $\psi_n$
Z časově nezávislé Schrödingerovy rovnice jsme, jak ukazuje ($\ref{eqn:psi_n}$), získali nekonečně mnoho řešení pro každou energetickou hladinu $n$. Když prvních několik z nich vykreslíme, dostaneme obrázek níže.

![Initial wavefunctions for the lowest four quantum states](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Tyto stavy mají tvar stojaté vlny na struně délky $a$. Stav $\psi_1$ s nejnižší energií se nazývá **základní stav (ground state)** a zbývající stavy s $n\geq 2$, jejichž energie roste úměrně $n^2$, se nazývají **excitované stavy (excited states)**.

## Čtyři důležité matematické vlastnosti $\psi_n$
Všechny funkce $\psi_n(x)$ mají následující čtyři důležité vlastnosti. Tyto čtyři vlastnosti jsou velmi silné a nejsou omezené pouze na nekonečnou čtvercovou jámu. První vlastnost platí vždy, pokud má samotný potenciál symetrii; druhá, třetí a čtvrtá vlastnost jsou obecné a objevují se bez ohledu na tvar potenciálu.

### 1. Vzhledem ke středu jámy se střídají sudé a liché funkce.
Pro kladná celá $n$ je $\psi_{2n-1}$ sudá funkce a $\psi_{2n}$ lichá funkce.

### 2. S rostoucí energií má každý následující stav o jeden uzel více.
Pro kladná celá $n$ má $\psi_n$ právě $(n-1)$ **uzlů (node)**.

### 3. Tyto stavy mají ortogonalitu (orthogonality).

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

v tom smyslu, že jsou navzájem **ortogonální (orthogonal)**.

> V nekonečné čtvercové jámě, kterou právě probíráme, je $\psi$ reálná, takže není nutné brát komplexní sdružení ($^*$) u $\psi_m$, ale kvůli případům, kdy tomu tak není, je dobré zvyknout si jej psát vždy.
{: .prompt-tip }

#### Důkaz
Pro $m\neq n$:

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

Pro $m=n$ je tento integrál díky normalizaci roven $1$. Pomocí **Kroneckerova delta (Kronecker delta)** $\delta_{mn}$ lze ortogonalitu i normalizaci vyjádřit společně jako

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

V takovém případě říkáme, že $\psi$ je **ortonormovaná (orthonormal)**.

### 4. Tyto funkce mají úplnost (completeness).
V tom smyslu, že libovolnou jinou funkci $f(x)$ lze zapsat jako lineární kombinaci

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

jsou tyto funkce **úplné (complete)**. Rovnice ($\ref{eqn:fourier_series}$) je **Fourierova řada (Fourier series)** funkce $f(x)$ a tvrzení, že libovolnou funkci lze takto rozvinout, se nazývá **Dirichletova věta (Dirichlet's theorem)**.

## Určení koeficientů $c_n$ pomocí Fourierovy metody (Fourier's trick)
Je-li dána funkce $f(x)$, pak pomocí výše uvedené úplnosti (completeness) a ortonormality (orthonormality) lze koeficienty $c_n$ určit následujícím postupem, kterému se říká **Fourierova metoda (Fourier's trick)**. Vynásobíme-li obě strany ($\ref{eqn:fourier_series}$) výrazem $\psi_m(x)^*$ a zintegrujeme, pak díky ($\ref{eqn:orthonomality}$) a ($\ref{eqn:kronecker_delta}$) dostaneme

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

> Všimněte si, že díky Kroneckerovu deltu v sumě zmizí všechny členy kromě členu s $n=m$.
{: .prompt-info }

Proto je $n$-tý koeficient při rozvoji $f(x)$

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

## Nalezení obecného řešení časově závislé Schrödingerovy rovnice $\Psi(x,t)$
Každý stacionární stav nekonečné čtvercové jámy je podle [rovnice (10) v příspěvku „Časově nezávislá Schrödingerova rovnice“](/posts/time-independent-schrodinger-equation/#1-jsou-to-stacionarni-stavy-stationary-states) a podle dříve odvozené rovnice ($\ref{eqn:psi_n}$)

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

Dále jsme v příspěvku [Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/#3-obecne-reseni-casove-zavisle-schrodingerovy-rovnice-je-linearni-kombinace-reseni-ziskanych-separaci-promennych) viděli, že obecné řešení Schrödingerovy rovnice lze vyjádřit jako lineární kombinaci stacionárních stavů. Tedy

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

Zbývá už jen najít koeficienty $c_n$, které splňují

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

Díky úplnosti funkcí $\psi$ koeficienty $c_n$ splňující tuto rovnost vždy existují a lze je získat dosazením $\Psi(x,0)$ za $f(x)$ v ($\ref{eqn:coefficients_n}$):

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

Je-li dána počáteční podmínka $\Psi(x,0)$, určíme pomocí ($\ref{eqn:calc_of_cn}$) rozvojové koeficienty $c_n$ a po dosazení do ($\ref{eqn:general_solution}$ získáme $\Psi(x,t)$. Poté lze podle postupu z příspěvku [Ehrenfestova věta](/posts/ehrenfest-theorem/) vypočítat libovolnou fyzikální veličinu, která nás zajímá. Tato metoda se dá použít nejen pro nekonečnou čtvercovou jámu, ale i pro libovolný potenciál; změní se pouze tvar funkce $\psi$ a vztahy pro povolené energetické hladiny.

## Odvození zákona zachování energie ($\langle H \rangle=\sum\|c_n\|^2E_n$)
Pomocí ortonormality $\psi(x)$ (rovnice [$\ref{eqn:orthonomality}$]–[$\ref{eqn:kronecker_delta}$]) odvoďme zákon zachování energie, který jsme stručně zmínili v příspěvku [Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/#zachovani-energie). Protože $c_n$ jsou na čase nezávislé, stačí ukázat platnost pro případ $t=0$.

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

Dále, protože

$$ \hat{H}\psi_n = E_n\psi_n $$

dostáváme:

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
