---
title: Testování konvergence/divergence řady (Testing for Convergence or Divergence of a Series)
description: Přehled metod pro testování konvergence a divergence nekonečných řad, včetně srovnávacích, integrálních, podílových a odmocninových testů.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Test n-tého členu (test divergence; $n$th-term test for divergence)**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{řada }\sum a_n \text{ diverguje}$
> - **Konvergence/divergence geometrické řady**: geometrická řada $\sum ar^{n-1}$:
>   - konverguje, pokud $\|r\| < 1$
>   - diverguje, pokud $\|r\| \geq 1$
> - **Konvergence/divergence $p$-řady**: $p$-řada $\sum \cfrac{1}{n^p}$:
>   - konverguje, pokud $p>1$
>   - diverguje, pokud $p\leq 1$
> - **Srovnávací test (Comparison Test)**: když $0 \leq a_n \leq b_n$, pak  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Limitní srovnávací test (Limit Comparison Test)**: pokud $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ je konečné kladné číslo)}$, pak obě řady $\sum a_n$ a $\sum b_n$ buď obě konvergují, nebo obě divergují
> - Pro řadu s kladnými členy $\sum a_n$ a kladné $\epsilon < 1$ platí:  
>   - jestliže pro všechna $n$ platí $\sqrt[n]{a_n}< 1-\epsilon$, pak řada $\sum a_n$ konverguje
>   - jestliže pro všechna $n$ platí $\sqrt[n]{a_n}> 1+\epsilon$, pak řada $\sum a_n$ diverguje
> - **Odmocninový test (Root Test)**: je-li u řady s kladnými členy $\sum a_n$ definována limita $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$, pak:
>   - pokud $r<1$, řada $\sum a_n$ konverguje
>   - pokud $r>1$, řada $\sum a_n$ diverguje
> - **Podílový test (Ratio Test)**: pro kladnou posloupnost $(a_n)$ a $0 < r < 1$:
>   - jestliže pro všechna $n$ platí $a_{n+1}/a_n \leq r$, pak řada $\sum a_n$ konverguje
>   - jestliže pro všechna $n$ platí $a_{n+1}/a_n \geq 1$, pak řada $\sum a_n$ diverguje
> - Existuje-li u kladné posloupnosti $(a_n)$ limita $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$, pak:
>   - pokud $\rho < 1$, řada $\sum a_n$ konverguje
>   - pokud $\rho > 1$, řada $\sum a_n$ diverguje
> - **Integrální test (Integral Test)**: je-li spojitá funkce $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ klesající a pro všechna $x$ platí $f(x)>0$, pak řada $\sum f(n)$ konverguje právě tehdy, když konverguje integrál $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$
> - **Test střídavé řady (Alternating Series Test)**: střídavá řada $\sum a_n$ konverguje, pokud platí:
>   1. pro všechna $n$ mají $a_n$ a $a_{n+1}$ opačné znaménko
>   2. pro všechna $n$ platí $\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Absolutně konvergentní řada je konvergentní. Obráceně to neplatí.
{: .prompt-info }

## Prerequisites
- [Posloupnosti a řady](/posts/sequences-and-series/)

## Úvod
V článku [Posloupnosti a řady](/posts/sequences-and-series/#konvergence-a-divergence-rady) jsme si definovali konvergenci a divergenci řad. V tomto textu shrnu různé metody, které lze použít při testování konvergence/divergence řady. Obecně je testování konvergence/divergence řady mnohem snazší než přesné určení jejího součtu.

## Test n-tého členu
Pro řadu $\sum a_n$ nazýváme $a_n$ jejím **obecným členem**.

Následující věta umožňuje snadno zjistit, že některé řady zjevně divergují; proto je rozumné při testování konvergence/divergence řady nejprve ověřit právě tuto podmínku, aby se předešlo zbytečné ztrátě času.

> **Test n-tého členu (test divergence; $n$th-term test for divergence)**  
> Jestliže řada $\sum a_n$ konverguje, pak
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> Tedy:
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{řada }\sum a_n \text{ diverguje} $$
>
> .
{: .prompt-info }

### Důkaz
Označme součet konvergentní řady $\sum a_n$ jako $l$ a její $n$-tý částečný součet jako

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Pak platí

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Proto pro dostatečně velké ($>N$) $n$:

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

a tedy z definice konvergence posloupnosti:

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Poznámka
Obrácení této věty obecně neplatí. Typickým příkladem je **harmonická řada (harmonic series)**.

Harmonická řada je řada získaná z posloupnosti, jejíž členy jsou převrácené hodnoty členů **aritmetické posloupnosti** (tj. z **harmonické posloupnosti**). Klasickým příkladem je:

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Tato řada diverguje, což lze ukázat následovně:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

I když tedy řada $H_n$ diverguje, její obecný člen $1/n$ zjevně konverguje k nule.

> Jestliže $\lim_{n\to\infty} a_n \neq 0$, pak řada $\sum a_n$ nutně diverguje. Avšak z $\lim_{n\to\infty} a_n = 0$ ještě neplyne, že řada $\sum a_n$ konverguje — v takovém případě je třeba použít jiné metody testování konvergence/divergence.
{: .prompt-danger }

## Geometrická řada
**Geometrická řada (geometric series)** získaná z geometrické posloupnosti s prvním členem 1 a **kvocientem** $r$:

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

je <u>nejdůležitější a nejzákladnější řada</u>. Z identity

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

dostaneme

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Dále platí

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

a proto je nutnou a postačující podmínkou konvergence geometrické řady ($\ref{eqn:geometric_series}$) nerovnost $\|r\| < 1$.

> **Konvergence/divergence geometrické řady**  
> Geometrická řada $\sum ar^{n-1}$:
> - konverguje, pokud $\|r\| < 1$
> - diverguje, pokud $\|r\| \geq 1$
{: .prompt-info }

Odtud plyne

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Geometrická řada a aproximace
Identita ($\ref{eqn:sum_of_geometric_series}$) je pro $\|r\| < 1$ užitečná k získání aproximace hodnoty $\cfrac{1}{1-r}$.

Dosadíme-li do ní $r=-\epsilon$, $n=2$, dostaneme

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Tedy pro $0 < \epsilon < 1$ platí

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

a proto

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

Z toho plyne, že pro dostatečně malé kladné $\epsilon$ lze $\cfrac{1}{1 + \epsilon}$ aproximovat výrazem $1 - \epsilon$.

## Test $p$-řady ($p$-Series Test)  
Pro kladné reálné $p$ nazýváme řadu tvaru

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

**$p$-řadou**.

> **Konvergence/divergence $p$-řady**  
> $p$-řada $\sum \cfrac{1}{n^p}$:
> - konverguje, pokud $p>1$
> - diverguje, pokud $p\leq 1$
{: .prompt-info }

Pro $p=1$ dostaneme harmonickou řadu, u níž jsme výše ukázali divergenci.  
Pro $p=2$ se problém určení hodnoty $p$-řady $\sum \cfrac{1}{n^2}$ nazývá „bazilejský (Basel) problém“ podle místa spojeného s rodinou Bernoulliů, která dala světu několik slavných matematiků a která jako první prokázala konvergenci této řady. Je známo, že odpověď je $\cfrac{\pi^2}{6}$.

Obecněji se pro $p$-řadu s $p>1$ používá označení **zeta funkce (zeta function)**. Jde o speciální funkci zavedenou Leonhardem Eulerem (Leonhard Euler) v roce 11740 [holocenního kalendáře](https://en.wikipedia.org/wiki/Holocene_calendar) a později pojmenovanou Riemannem; definuje se jako

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

To už s tématem tohoto článku příliš nesouvisí a upřímně: jsem spíš „inženýrský typ“ než matematik, takže se tomu zde věnovat nebudu. Euler však ukázal, že zeta funkci lze vyjádřit také jako nekonečný součin přes prvočísla (prime number) — tzv. **Eulerův součin (Euler Product)** — a zeta funkce pak zaujímá klíčové místo v řadě oblastí analytické teorie čísel. Patří sem i **Riemannova zeta funkce (Riemann zeta function)**, tj. rozšíření definičního oboru na komplexní čísla, a s ní související slavný nevyřešený problém **Riemannova hypotéza (Riemann hypothesis)**.

Zpět k původnímu tématu: k důkazu testu $p$-řady budeme potřebovat níže uvedený [srovnávací test](#srovnavaci-test) a [integrální test](#integralni-test). Konvergenci/divergenci $p$-řady jsem však záměrně zařadil dopředu, protože se společně s geometrickou řadou hodí hned v [srovnávacím testu](#srovnavaci-test), který následuje.

### Důkaz
#### i) Pro $p>1$
Protože integrál

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

konverguje, plyne z [integrálního testu](#integralni-test), že konverguje i řada $\sum \cfrac{1}{n^p}$.

#### ii) Pro $p\leq 1$
V tomto případě platí

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Protože víme, že harmonická řada $\sum \cfrac{1}{n}$ diverguje, dostaneme ze [srovnávacího testu](#srovnavaci-test), že $\sum \cfrac{1}{n^p}$ také diverguje.

#### Závěr
Z i) a ii) plyne: $p$-řada $\sum \cfrac{1}{n^p}$ konverguje pro $p>1$ a diverguje pro $p \leq 1$. $\blacksquare$

## Srovnávací test
Při testování konvergence/divergence řad s nezápornými reálnými členy, tj. **řad s kladnými členy (series of positive terms)**, je užitečný **srovnávací test (Comparison Test)** Jakoba Bernoulliho (Jakob Bernoulli).

Řada s kladnými členy $\sum a_n$ má rostoucí částečné součty, takže pokud nediverguje do nekonečna ($\sum a_n = \infty$), musí konvergovat. Proto výraz typu

$$ \sum a_n < \infty $$

znamená <u>konverguje</u>.

> **Srovnávací test (Comparison Test)**  
> Když $0 \leq a_n \leq b_n$, pak:
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

Zejména u řad s kladnými členy jako $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$ apod., které mají podobný tvar jako geometrická řada $\sum ar^{n-1}$ či $p$-řada $\sum \cfrac{1}{n^p}$, je vhodné srovnávací test aktivně vyzkoušet.

Všechny další testy konvergence/divergence uvedené níže lze odvodit právě ze **srovnávacího testu**; v tomto smyslu jej lze považovat za nejdůležitější.

### Limitní srovnávací test
Pro dvě řady s kladnými členy $\sum a_n$ a $\sum b_n$ předpokládejme, že v podílu obecných členů $a_n/b_n$ se dominantní členy v čitateli a jmenovateli vyruší a že platí $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ je konečné kladné číslo)}$. Známe-li konvergenci/divergenci řady $\sum b_n$, můžeme použít následující **limitní srovnávací test (Limit Comparison Test)**.

> **Limitní srovnávací test (Limit Comparison Test)**  
> Jestliže
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ je konečné kladné číslo)}$$
>
> pak řady $\sum a_n$ a $\sum b_n$ buď obě konvergují, nebo obě divergují. Tj. $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Odmocninový test
> **Věta**  
> Pro řadu s kladnými členy $\sum a_n$ a kladné $\epsilon < 1$ platí:  
> - jestliže pro všechna $n$ platí $\sqrt[n]{a_n}< 1-\epsilon$, pak řada $\sum a_n$ konverguje
> - jestliže pro všechna $n$ platí $\sqrt[n]{a_n}> 1+\epsilon$, pak řada $\sum a_n$ diverguje
{: .prompt-info }

> **Důsledek: odmocninový test (Root Test)**  
> Nechť u řady s kladnými členy $\sum a_n$ existuje limita
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> Pak:
> - pokud $r<1$, řada $\sum a_n$ konverguje
> - pokud $r>1$, řada $\sum a_n$ diverguje
{: .prompt-info }

> Pokud je v uvedeném důsledku $r=1$, nelze rozhodnout o konvergenci/divergenci, a je třeba použít jiné metody.
{: .prompt-warning }

## Podílový test
> **Podílový test (Ratio Test)**  
> Pro kladnou posloupnost $(a_n)$ a $0 < r < 1$:
> - jestliže pro všechna $n$ platí $a_{n+1}/a_n \leq r$, pak řada $\sum a_n$ konverguje
> - jestliže pro všechna $n$ platí $a_{n+1}/a_n \geq 1$, pak řada $\sum a_n$ diverguje
{: .prompt-info }

> **Důsledek**  
> Nechť u kladné posloupnosti $(a_n)$ existuje limita $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$. Pak:
> - pokud $\rho < 1$, řada $\sum a_n$ konverguje
> - pokud $\rho > 1$, řada $\sum a_n$ diverguje
{: .prompt-info }

## Integrální test
Pomocí integrálu lze testovat konvergenci/divergenci řad složených z klesající kladné posloupnosti.

> **Integrální test (Integral Test)**  
> Nechť je spojitá funkce $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ klesající a pro všechna $x$ platí $f(x)>0$. Pak řada $\sum f(n)$ konverguje právě tehdy, když konverguje integrál
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> .
{: .prompt-info }

### Důkaz
Protože $f(x)$ je spojitá, klesající a všude kladná, platí nerovnost

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

Sečteme-li tyto nerovnosti pro $n=1$ až po obecné $n$, dostaneme

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Aplikací [srovnávacího testu](#srovnavaci-test) získáme požadovaný výsledek. $\blacksquare$

## Střídavé řady
Řadu $\sum a_n$, v níž je obecný člen nenulový a znaménko každého členu $a_n$ je opačné než znaménko následujícího členu $a_{n+1}$ (tj. kladné a záporné členy se střídají), nazýváme **střídavou řadou (alternating series)**.

Pro střídavé řady lze pro testování konvergence/divergence užitečně využít následující větu, kterou objevil německý matematik Gottfried Wilhelm Leibniz (Gottfried Wilhelm Leibniz).

> **Test střídavé řady (Alternating Series Test)**  
> Jestliže:
> 1. pro všechna $n$ mají $a_n$ a $a_{n+1}$ opačné znaménko,
> 2. pro všechna $n$ platí $\|a_n\| \geq \|a_{n+1}\|$,
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> pak střídavá řada $\sum a_n$ konverguje.
{: .prompt-info }

## Absolutně konvergentní řady
Pro řadu $\sum a_n$ říkáme, že **konverguje absolutně (converge absolutely)**, jestliže konverguje řada $\sum \|a_n\|$.

Pak platí následující věta.

> **Věta**  
> Absolutně konvergentní řada je konvergentní.
{: .prompt-info }

> Obrácení předchozí věty neplatí.  
> Pokud řada konverguje, ale není absolutně konvergentní, říkáme, že konverguje **podmíněně (converge conditionally)**.
{: .prompt-warning }

### Důkaz
Pro reálné $a$ definujme

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Pak platí

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Protože $0 \leq a^\pm \leq \|a\|$, plyne ze [srovnávacího testu](#srovnavaci-test), že pokud řada $\sum \|a_n\|$ konverguje, pak konvergují i řady $\sum a_n^+$ a $\sum a_n^-$. Následně ze [základních vlastností konvergentních řad](/posts/sequences-and-series/#zakladni-vlastnosti-konvergentnich-rad) dostaneme

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

a tedy $\sum a_n$ konverguje. $\blacksquare$
