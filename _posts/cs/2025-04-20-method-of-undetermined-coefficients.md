---
title: "Metoda neurčených koeficientů"
description: "Metoda neurčených koeficientů umožňuje jednoduše řešit úlohy s počátečními podmínkami pro určité typy nehomogenních lineárních ODR s konstantními koeficienty; v praxi je užitečná např. pro kmitavé soustavy a modely obvodů RLC."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Oblast použití **metody neurčených koeficientů**:
>   - má **konstantní koeficienty $a$ a $b$**
>   - vstup $r(x)$ je tvořen exponenciální funkcí, mocninami $x$, $\cos$ nebo $\sin$, případně součty a součiny těchto funkcí
>   - lineární ODR $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Výběrová pravidla pro metodu neurčených koeficientů**  
>   - **(a) základní pravidlo (basic rule)**: Pokud je v rovnici ($\ref{eqn:linear_ode_with_constant_coefficients}$) $r(x)$ jednou z funkcí v prvním sloupci tabulky, zvolíme $y_p$ ze stejného řádku a neznámé koeficienty určíme dosazením $y_p$ a jeho derivací do ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) modifikační pravidlo (modification rule)**: Pokud zvolený člen $y_p$ je řešením odpovídající homogenní rovnice $y^{\prime\prime} + ay^{\prime} + by = 0$, vynásobíme tento člen $x$ (nebo $x^2$, pokud odpovídá dvojnásobnému kořeni charakteristické rovnice homogenní ODR).  
>   - **(c) pravidlo součtu (sum rule)**: Je-li $r(x)$ součtem funkcí z prvního sloupce tabulky, zvolíme $y_p$ jako součet odpovídajících funkcí z druhého sloupce.
>
> | člen v $r(x)$ | volba pro $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Předpoklady
- [Homogenní lineární ODR 2. řádu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Homogenní lineární ODR 2. řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Eulerova–Cauchyho rovnice](/posts/euler-cauchy-equation/)
- [Wronskián (Wronskian), existence a jednoznačnost řešení](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Nehomogenní lineární ODR 2. řádu (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)
- vektorový prostor, lineární obal (lineární algebra)

## Metoda neurčených koeficientů
Uvažujme nehomogenní lineární ODR 2. řádu s $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

a odpovídající homogenní rovnici

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Jak jsme již viděli v článku [Nehomogenní lineární ODR 2. řádu (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/), pro vyřešení úlohy s počátečními podmínkami k nehomogenní lineární ODR ($\ref{eqn:nonhomogeneous_linear_ode}$) je potřeba nejprve vyřešit homogenní ODR ($\ref{eqn:homogeneous_linear_ode}$), získat $y_h$, poté najít partikulární řešení $y_p$ rovnice ($\ref{eqn:nonhomogeneous_linear_ode}$) a dostat obecné řešení

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Jak tedy $y_p$ najít? Obecnou metodou je **metoda variace parametrů (method of variation of parameters)**, ale v některých případech lze použít výrazně jednodušší **metodu neurčených koeficientů (method of undetermined coefficients)**. Ta je obzvlášť často využívaná v inženýrské praxi, protože se hodí pro kmitavé soustavy a modely elektrických obvodů RLC.

Metoda neurčených koeficientů je vhodná pro lineární ODR se **stálými koeficienty $a$ a $b$**, kde vstup $r(x)$ je tvořen exponenciální funkcí, mocninami $x$, $\cos$ nebo $\sin$, případně součty a součiny těchto funkcí:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

Klíč je v tom, že takové $r(x)$ má derivace podobného tvaru. Pro použití metody neurčených koeficientů zvolíme $y_p$ podobného tvaru jako $r(x)$, avšak s neznámými koeficienty, které určíme dosazením $y_p$ a jeho derivací do dané ODR. Pravidla pro volbu vhodného $y_p$ pro prakticky důležité tvary $r(x)$ jsou následující.

> **Výběrová pravidla pro metodu neurčených koeficientů**  
> **(a) základní pravidlo (basic rule)**: Pokud je v rovnici ($\ref{eqn:linear_ode_with_constant_coefficients}$) $r(x)$ jednou z funkcí v prvním sloupci tabulky, zvolíme $y_p$ ze stejného řádku a neznámé koeficienty určíme dosazením $y_p$ a jeho derivací do ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) modifikační pravidlo (modification rule)**: Pokud zvolený člen $y_p$ je řešením odpovídající homogenní rovnice $y^{\prime\prime} + ay^{\prime} + by = 0$, vynásobíme tento člen $x$ (nebo $x^2$, pokud odpovídá dvojnásobnému kořeni charakteristické rovnice homogenní ODR).  
> **(c) pravidlo součtu (sum rule)**: Je-li $r(x)$ součtem funkcí z prvního sloupce tabulky, zvolíme $y_p$ jako součet odpovídajících funkcí z druhého sloupce.
>
> | člen v $r(x)$ | volba pro $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Tato metoda je nejen jednoduchá, ale má i výhodu určité „samokontrolovatelnosti“. Pokud $y_p$ zvolíme špatně nebo zvolíme příliš málo členů, narazíme na rozpor; pokud naopak zvolíme členů příliš mnoho, koeficienty nadbytečných členů vyjdou jako $0$ a dostaneme správný výsledek. I když se při použití metody neurčených koeficientů něco pokazí, obvykle to během výpočtu přirozeně odhalíme, takže pokud podle výše uvedených pravidel zvolíte rozumné $y_p$, můžete metodu bez obav vyzkoušet.

### Důkaz pravidla součtu
Uvažujme nehomogenní lineární ODR tvaru $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Nyní uvažujme následující dvě rovnice se stejnou levou stranou a vstupy $r_1$, $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Nechť mají řešení ${y_p}_1$, ${y_p}_2$. Označme levou stranu jako $L[y]$. Díky linearitě $L[y]$ pak pro $y_p = {y_p}_1 + {y_p}_2$ platí následující, čímž je pravidlo součtu dokázáno:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Příklad: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Podle základního pravidla (a) položíme $y_p = Ce^{\gamma x}$ a dosadíme do dané rovnice $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Případ, kdy $\gamma^2 + a\gamma + b \neq 0$
Neurčený koeficient $C$ lze určit následovně a dostaneme $y_p$:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Případ, kdy $\gamma^2 + a\gamma + b = 0$
V tomto případě musíme použít modifikační pravidlo (b). Nejprve využijeme $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$ a určeme kořeny charakteristické rovnice homogenní ODR $y^{\prime\prime} + ay^{\prime} + by = 0$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Odtud získáme bázi řešení homogenní ODR:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Případ, kdy $\gamma \neq -a-\gamma$
Protože zvolené $Ce^{\gamma x}$ odpovídá kořeni, který není dvojnásobný, použijeme podle modifikačního pravidla (b) násobení $x$ a položíme $y_p = Cxe^{\gamma x}$.

Dosadíme takto upravené $y_p$ zpět do dané rovnice $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Případ, kdy $\gamma = -a-\gamma$
V tomto případě je $Ce^{\gamma x}$ dvojnásobným kořenem pro odpovídající homogenní ODR, takže podle modifikačního pravidla (b) násobíme $x^2$ a položíme $y_p = Cx^2 e^{\gamma x}$.

Dosadíme takto upravené $y_p$ zpět do dané rovnice $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Rozšíření metody neurčených koeficientů: $r(x)$ jako součin funkcí
Uvažujme nehomogenní lineární ODR, kde $r(x) = k x^n e^{\alpha x}\cos(\omega x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Ukážeme, že pokud je $r(x)$ součinem a součtem exponenciálních funkcí $e^{\alpha x}$, mocnin $x^m$, $\cos{\omega x}$ nebo $\sin{\omega x}$ (zde pro jednoduchost předpokládáme $\cos$, aniž bychom ztratili obecnost), tj. lze jej vyjádřit jako součet a součin funkcí z prvního sloupce předchozí tabulky, pak existuje partikulární řešení $y_p$ jako součet a součin odpovídajících funkcí z druhého sloupce téže tabulky.

> Pro striktní důkaz je část textu napsána s využitím lineární algebry; takové pasáže jsou označeny \* . Tyto části můžete přeskočit a pro přibližné pochopení stačí číst zbytek.
{: .prompt-tip }

### Definice vektorového prostoru $V$\*
Pro $r(x)$ tvaru

$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

lze zvolit vektorový prostor $V$ tak, aby $r(x) \in V$, například takto:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Tvary derivací exponenciálních, polynomiálních a goniometrických funkcí
Tvary derivací základních funkcí uvedených v prvním sloupci tabulky jsou následující:
- exponenciální funkce: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- polynomiální funkce: $\cfrac{d}{dx}x^m = mx^{m-1}$
- goniometrické funkce: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Derivace získané derivováním těchto funkcí lze opět vyjádřit jako <u>součet funkcí stejného typu</u>.

Proto, jsou-li $f$ a $g$ výše uvedené funkce nebo jejich součty, pak pro $r(x) = f(x)g(x)$ platí (pravidlo pro derivaci součinu):

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

a zde jsou $f$, $f^{\prime}$, $f^{\prime\prime}$ i $g$, $g^{\prime}$, $g^{\prime\prime}$ vždy součty či konstantní násobky exponenciálních, polynomiálních a goniometrických funkcí. Tedy také $r^{\prime}(x) = (fg)^{\prime}$ a $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ lze stejně jako $r(x)$ vyjádřit jako součty a součiny těchto funkcí.

### Invariance $V$ vůči derivačnímu operátoru $D$ a lineárnímu zobrazení $L$\*
Jinými slovy, nejen $r(x)$ samotné, ale i $r^{\prime}(x)$ a $r^{\prime\prime}(x)$ jsou lineární kombinace členů tvaru $x^k e^{\alpha x}\cos(\omega x)$ a $x^k e^{\alpha x}\sin(\omega x)$, takže

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Zavedeme-li derivační operátor $D$ obecně pro všechny prvky $V$, dostaneme: *vektorový prostor $V$ je uzavřený vůči derivaci $D$*. Označíme-li levou stranu dané rovnice $y^{\prime\prime} + ay^{\prime} + by$ jako $L[y]$, pak *$V$ je invariantní vůči $L$ (invariant)*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Protože $r(x) \in V$ a $V$ je invariantní vůči $L$, existuje další prvek $y_p \in V$ splňující $L[y_p] = r$:

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Proto, zvolíme-li vhodné $y_p$ s neurčenými koeficienty $A_0, A_1, \dots, A_n$ a $K$, $M$ tak, aby tvořilo součet všech možných členů součinového typu, můžeme podle základního pravidla (a) a modifikačního pravidla (b) určit neurčené koeficienty dosazením $y_p$ (nebo $xy_p$, $x^2y_p$) a jeho derivací do dané rovnice. Číslo $n$ se zvolí podle stupně $r(x)$ vzhledem k $x$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Pokud daný vstup $r(x)$ obsahuje více různých hodnot $\alpha_i$ a $\omega_j$, je potřeba zvolit $y_p$ tak, aby pro každou kombinaci $\alpha_i$, $\omega_j$ zahrnovalo všechny možné členy tvaru $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ a $x^{k}e^{\alpha_i x}\sin(\omega_j x)$, bez výjimek.  
> Výhodou metody neurčených koeficientů je její jednoduchost; pokud se ansatz příliš zkomplikuje a tato výhoda se vytrácí, může být lepší použít (později probíranou) metodu variace parametrů.
{: .prompt-warning }

## Rozšíření metody neurčených koeficientů: Eulerova–Cauchyho rovnice
Metodu neurčených koeficientů lze použít nejen pro [homogenní lineární ODR 2. řádu s konstantními koeficienty](/posts/homogeneous-linear-odes-with-constant-coefficients/), ale také pro [Eulerovu–Cauchyho rovnici](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Substituce proměnné
Pokud provedeme [substituci $x = e^t$ a převedeme na homogenní lineární ODR 2. řádu s konstantními koeficienty](/posts/euler-cauchy-equation/#transformace-na-homogenni-linearni-odr-2-radu-s-konstantnimi-koeficienty),

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

a jak jsme si již ukázali, Eulerova–Cauchyho rovnice se dá přepsat na lineární ODR s konstantními koeficienty v proměnné $t$:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Nyní stačí na rovnici ($\ref{eqn:substituted}$) aplikovat stejným způsobem [dříve probíranou metodu neurčených koeficientů](#metoda-neurcenych-koeficientu), vyřešit ji pro $t$ a nakonec s využitím $t = \ln x$ získat řešení v proměnné $x$.

### Případ, kdy je $r(x)$ mocnina $x$, přirozený logaritmus nebo součet/součin takových funkcí
Zejména pokud je vstup $r(x)$ tvořen mocninami $x$, přirozeným logaritmem nebo součty a součiny takových funkcí, lze podle následujících výběrových pravidel (pro Eulerovu–Cauchyho rovnici) přímo zvolit vhodné $y_p$.

> **Výběrová pravidla pro metodu neurčených koeficientů: Eulerova–Cauchyho rovnice**  
> **(a) základní pravidlo (basic rule)**: Pokud je v rovnici ($\ref{eqn:euler_cauchy}$) $r(x)$ jednou z funkcí v prvním sloupci tabulky, zvolíme $y_p$ ze stejného řádku a neznámé koeficienty určíme dosazením $y_p$ a jeho derivací do ($\ref{eqn:euler_cauchy}$).  
> **(b) modifikační pravidlo (modification rule)**: Pokud zvolený člen $y_p$ je řešením odpovídající homogenní rovnice $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, vynásobíme tento člen $\ln{x}$ (nebo $(\ln{x})^2$, pokud odpovídá dvojnásobnému kořeni charakteristické rovnice homogenní ODR).  
> **(c) pravidlo součtu (sum rule)**: Je-li $r(x)$ součtem funkcí z prvního sloupce tabulky, zvolíme $y_p$ jako součet odpovídajících funkcí z druhého sloupce.
>
> | člen v $r(x)$ | volba pro $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Tímto způsobem lze pro prakticky důležité tvary vstupu $r(x)$ najít stejné $y_p$ jako při použití [substituce proměnné](#substituce-promenne), ale rychleji a pohodlněji. Tato pravidla pro Eulerovu–Cauchyho rovnici lze odvodit tak, že v [původních výběrových pravidlech](#metoda-neurcenych-koeficientu) nahradíme $x$ výrazem $\ln{x}$.
