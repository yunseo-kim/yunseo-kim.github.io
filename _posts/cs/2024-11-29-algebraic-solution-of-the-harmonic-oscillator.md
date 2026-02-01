---
title: Algebraické řešení harmonického oscilátoru (The Harmonic Oscillator)
description: V kvantové mechanice sestavíme Schrödingerovu rovnici pro harmonický oscilátor a projdeme algebraické řešení. Z komutátorů, kanonické komutační relace a žebříčkových operátorů odvodíme vlnové funkce stacionárních stavů i energetické hladiny.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Pokud je amplituda dostatečně malá, lze libovolné kmitání aproximovat jako jednoduché harmonické kmitání (simple harmonic oscillation); proto má v fyzice zásadní význam
> - Harmonický oscilátor: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Komutátor (commutator)**:
>   - binární operace vyjadřující, jak moc se dva operátory „nevyměňují“ (commute)
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Kanonická komutační relace (canonical commutation relation)**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Žebříčkové operátory (ladder operators)**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ se nazývá **zvyšovací operátor (raising operator)**, $\hat{a}\_-$ **snižovací operátor (lowering operator)**
>   - pro libovolný stacionární stav lze energetickou hladinu zvyšovat nebo snižovat, takže stačí najít jedno řešení časově nezávislé Schrödingerovy rovnice a všechna ostatní z něj získáme
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Vlnová funkce a energetická hladina $n$-tého stacionárního stavu:
>   - základní stav ($0$-tý stacionární stav):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$-tý stacionární stav:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ je **Hermitovsky sdružený (hermitian conjugate)** a zároveň **adjungovaný operátor (adjoint operator)** k $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - Z toho lze odvodit následující vlastnosti:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Jak počítat střední hodnoty veličin obsahujících mocniny $\hat{x}$ a $\hat{p}$:
>   1. pomocí definice žebříčkových operátorů vyjádřit $\hat{x}$ a $\hat{p}$ přes zvyšovací a snižovací operátor
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. vyjádřit hledanou veličinu pomocí výše uvedených vztahů pro $\hat{x}$ a $\hat{p}$
>   3. využít, že $\left(\hat{a}\_\pm \right)^m$ je úměrné $\psi\_{n\pm m}$, které je s $\psi_n$ ortogonální, takže příspěvek je $0$
>   4. dopočítat integrály s využitím vlastností žebříčkových operátorů
{: .prompt-info }

## Předpoklady
- [Metoda separace proměnných](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Schrödingerova rovnice a vlnová funkce](/posts/schrodinger-equation-and-the-wave-function/)
- [Ehrenfestova věta](/posts/ehrenfest-theorem/)
- [Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/)
- [1D nekonečná potenciálová jáma](/posts/the-infinite-square-well/)
- Hermitovsky sdružený (hermitian conjugate), adjungovaný operátor (adjoint operator)

## Nastavení modelu
### Harmonický oscilátor v klasické mechanice
Typickým příkladem klasického harmonického oscilátoru je pohyb tělesa o hmotnosti $m$ zavěšeného na pružině s tuhostí $k$ (tření zanedbáme).
Tento pohyb se řídí **Hookeovým zákonem (Hooke's law)**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

Řešením této rovnice je

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

kde

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

je úhlová frekvence kmitání. Potenciální energie v závislosti na poloze $x$ má tvar

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

tj. paraboly.

V realitě neexistuje dokonale harmonický oscilátor. I v příkladu s pružinou: pokud ji natáhneme příliš, překročí se mez pružnosti a pružina se přetrhne nebo dojde k trvalé deformaci; a ve skutečnosti už před tímto bodem přestane přesně platit Hookeův zákon. Přesto je harmonický oscilátor ve fyzice důležitý, protože libovolný potenciál lze v okolí lokálního minima aproximovat parabolou. Provedeme-li Taylorův rozvoj potenciálu $V(x)$ v okolí bodu minima, dostaneme

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Protože přičtení libovolné konstanty k $V(x)$ nijak neovlivní sílu, odečteme $V(x_0)$. Jelikož $x_0$ je minimum, platí $V^\prime(x_0)=0$. A pokud předpokládáme, že $(x-x_0)$ je dostatečně malé, zanedbáme vyšší členy a získáme

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

\*. To odpovídá pohybu harmonického oscilátoru s efektivní tuhostí pružiny $k=V^{\prime\prime}(x_0)$ v okolí bodu $x_0$. Jinými slovy: je-li amplituda dostatečně malá, lze libovolné kmitání aproximovat jako jednoduché harmonické kmitání (simple harmonic oscillation).

> \* Protože předpokládáme, že $V(x)$ má v $x_0$ lokální minimum, platí zde $V^{\prime\prime}(x_0) \geq 0$. Ve velmi vzácných případech může nastat $V^{\prime\prime}(x_0)=0$ a takový pohyb nelze aproximovat jednoduchým harmonickým kmitáním.
{: .prompt-info }

### Harmonický oscilátor v kvantové mechanice
Úloha kvantově-mechanického harmonického oscilátoru spočívá v řešení Schrödingerovy rovnice pro potenciál

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

[Časově nezávislá Schrödingerova rovnice](/posts/time-independent-schrodinger-equation/) pro harmonický oscilátor má tvar

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

K řešení této úlohy existují dvě zcela odlišné metody. Jedna je analytická metoda využívající **mocninnou řadu (power series method)**, druhá je algebraická metoda využívající **žebříčkové operátory (ladder operators)**. Algebraická metoda je rychlejší a jednodušší, ale i analytické řešení pomocí mocninných řad je potřeba studovat. Zde budeme probírat algebraický postup; analytický postup viz [tento článek](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Komutátor a kanonická komutační relace
Rovnici ($\ref{eqn:t_independent_schrodinger_eqn}$) lze s využitím operátoru hybnosti $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$ přepsat takto:

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Nyní zaveďme hamiltonián (Hamiltonian)

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

a zkusme ho rozložit na součin.

Kdyby $p$ a $x$ byly čísla, mohli bychom napsat jednoduchý rozklad

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

Jenže zde jsou $\hat{p}$ a $\hat{x}$ operátory a pro operátory obecně neplatí **komutativita (commutative property)** (tj. $\hat{p}\hat{x}\neq \hat{x}\hat{p}$), takže to není tak přímočaré. Přesto nám to může sloužit jako vodítko, a proto začněme tím, že se podíváme na následující veličiny:

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

Pro operátory $\hat{a_\pm}$ definované výše je

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Zde se člen $(\hat{x}\hat{p}-\hat{p}\hat{x})$ nazývá **komutátor (commutator)** operátorů $\hat{x}$ a $\hat{p}$ a vyjadřuje, jak moc se tyto dva operátory „nevyměňují“ (commute). Obecně se komutátor operátorů $\hat{A}$ a $\hat{B}$ zapisuje pomocí hranatých závorek takto:

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

S touto notací lze rovnici ($\ref{eqn:a_m_times_a_p_without_commutator}$) přepsat na

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Nyní potřebujeme zjistit komutátor $\hat{x}$ a $\hat{p}$.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

Po vykrácení testovací funkce $f(x)$ dostaneme

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

Tomu se říká **kanonická komutační relace (canonical commutation relation)**.

## Žebříčkové operátory (ladder operators)
Díky kanonické komutační relaci se ($\ref{eqn:a_m_times_a_p}$) zjednoduší na

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

tj.

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Pořadí $\hat{a}\_-$ a $\hat{a}\_+$ je přitom důležité. Pokud dáme $\hat{a}\_+$ vlevo, dostaneme

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

a platí

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

V tomto případě lze hamiltonián psát také jako

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Proto lze časově nezávislou Schrödingerovu rovnici ($\hat{H}\psi=E\psi$) vyjádřit pomocí $\hat{a}_\pm$ takto:

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(„dvojité znaménko ve stejném pořadí“).

Nyní můžeme odvodit následující důležitou vlastnost:

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Důkaz:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> Podobně
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Tedy: pokud najdeme jedno řešení časově nezávislé Schrödingerovy rovnice, můžeme najít všechna ostatní. Jelikož pro libovolný stacionární stav můžeme energetickou hladinu zvyšovat či snižovat, nazýváme $\hat{a}\_\pm$ **žebříčkové operátory (ladder operators)**; $\hat{a}\_+$ je **zvyšovací operátor (raising operator)** a $\hat{a}\_-$ **snižovací operátor (lowering operator)**.

## Stacionární stavy harmonického oscilátoru
### Stacionární stav $\psi_n$ a energetická hladina $E_n$
Pokud budeme snižovací operátor aplikovat opakovaně, dříve či později bychom dostali stav se zápornou energií, který fyzikálně nemůže existovat. Matematicky platí, že je-li $\psi$ řešením Schrödingerovy rovnice, pak i $\hat{a}_-\psi$ je řešením, ale není zaručeno, že toto nové řešení bude vždy normované (tj. fyzikálně přípustné). Při opakované aplikaci snižovacího operátoru nakonec dostaneme triviální řešení $\psi=0$.

Proto pro stacionární stav $\psi$ harmonického oscilátoru existuje „nejnižší stupeň“ $\psi_0$, který splňuje

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

(tj. neexistuje už nižší energetická hladina). Tento stav $\psi_0$ splňuje

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

takže

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

Jde o [separovatelnou obyčejnou diferenciální rovnici](/posts/Separation-of-Variables/), takže ji snadno vyřešíme:

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

Tuto funkci lze znormalizovat následovně:

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Protože $A^2 = \sqrt{m\omega / \pi\hbar}$, dostáváme

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Nyní tento výsledek dosadíme do Schrödingerovy rovnice ($\ref{eqn:schrodinger_eqn_with_ladder}$) a využijeme $\hat{a}_-\psi_0=0$, čímž získáme

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

Počínaje tímto **základním stavem (ground state)** můžeme opakovaně aplikovat zvyšovací operátor a získáme excitované stavy (excited states), přičemž při každé aplikaci zvyšovacího operátoru energie vzroste o $\hbar\omega$.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

kde $A_n$ je normalizační konstanta. Tímto způsobem po určení základního stavu a aplikaci zvyšovacího operátoru určíme všechny stacionární stavy harmonického oscilátoru i povolené energetické hladiny.

### Normalizace
Normalizační konstantu lze rovněž určit algebraicky. Víme, že $\hat{a}\_{\pm}\psi_n$ je úměrné $\psi\_{n\pm 1}$, takže můžeme psát

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Nyní si všimněme, že pro libovolné integrovatelné funkce $f(x)$ a $g(x)$ platí

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ je tedy **Hermitovsky sdružený (hermitian conjugate)** a zároveň **adjungovaný operátor (adjoint operator)** k $\hat{a}\_\pm$.

> **Důkaz:**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

Tedy položíme-li $f=\hat{a}_\pm \psi_n$ a $g=\psi_n$, platí

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Z rovnic ($\ref{eqn:schrodinger_eqn_with_ladder}$) a ($\ref{eqn:psi_n_and_E_n}$) plyne, že

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

a tedy z ($\ref{eqn:norm_const}$) a ($\ref{eqn:norm_const_2}$) dostaneme

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

Protože $\psi_n$ i $\psi_{n\pm1}$ jsou všechny normované, vychází $\|c_n\|^2=n+1,\ \|d_n\|^2=n$, a tedy

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

Odtud získáme normovaný libovolný stacionární stav $\psi_n$ ve tvaru

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

Tj. v ($\ref{eqn:psi_n_and_E_n}$) je normalizační konstanta $A_n=\cfrac{1}{\sqrt{n!}}$.

### Ortogonalita stacionárních stavů
Stejně jako u [1D nekonečné potenciálové jámy](/posts/the-infinite-square-well/#3-tento-stav-ma-ortogonalitu-orthogonality) jsou stacionární stavy harmonického oscilátoru ortogonální:

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Důkaz
Lze jej dokázat pomocí dříve uvedených vztahů ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$), ($\ref{eqn:norm_const_3}$). Ve vztahu ($\ref{eqn:hermitian_conjugate}$) položíme $f=\hat{a}_-\psi_m,\ g=\psi_n$ a využijeme, že

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

Pak

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

S využitím ortogonality můžeme (stejně jako v [rovnici (19) u 1D nekonečné potenciálové jámy](/posts/the-infinite-square-well/#obecne-reseni-casove-zavisle-schrodingerovy-rovnice-psixt)) při rozvoji $\Psi(x,0)$ do lineární kombinace stacionárních stavů $\sum c_n\psi_n(x)$ určit koeficienty $c_n$ pomocí [Fourierovy metody](/posts/the-infinite-square-well/#urceni-koeficientu-c_n-pomoci-fourierova-triku-fouriers-trick):

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Také zde platí, že $\|c_n\|^2$ je pravděpodobnost, že při měření energie získáme hodnotu $E_n$.

## Střední hodnota potenciální energie $\langle V \rangle$ ve stacionárním stavu $\psi_n$
Pro výpočet $\langle V \rangle$ musíme spočítat integrál

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

Při výpočtu integrálů tohoto typu, které obsahují mocniny $\hat{x}$ a $\hat{p}$, je užitečný následující postup.

Nejprve pomocí definice žebříčkových operátorů z rovnice ($\ref{eqn:ladder_operators}$) vyjádříme $\hat{x}$ a $\hat{p}$ pomocí zvyšovacího a snižovacího operátoru:

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Pak pomocí těchto vztahů vyjádříme veličinu, jejíž střední hodnotu chceme spočítat. Zde nás zajímá $x^2$, takže můžeme psát

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

Odtud

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

Protože $\left(\hat{a}\_\pm \right)^2$ je úměrné $\psi\_{n\pm2}$, je s $\psi\_n$ ortogonální; tedy členy $\left(\hat{a}\_+ \right)^2$ a $\left(\hat{a}\_- \right)^2$ dávají $0$. Nakonec použijeme ($\ref{eqn:norm_const_2}$) na zbývající dva členy a dostaneme

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

Z rovnice ($\ref{eqn:psi_n_and_E_n}$) pak vidíme, že střední hodnota potenciální energie je přesně polovina celkové energie a druhá polovina je (samozřejmě) kinetická energie $T$. To je charakteristická vlastnost harmonického oscilátoru.
