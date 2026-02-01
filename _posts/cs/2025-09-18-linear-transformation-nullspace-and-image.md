---
title: "Lineární transformace, jádrový prostor a obraz"
description: "Projdeme definici lineární transformace a dva klíčové podprostory: jádro (nulový prostor) a obraz. Ukážeme také věty o jejich dimenzích (nulita, hodnost)."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Předpoklady
- [Vektory a lineární kombinace](/posts/vectors-and-linear-combinations/)
- [Vektorové prostory, podprostory a matice](/posts/vector-spaces-subspaces-and-matrices/)
- [Lineární závislost a lineární nezávislost, báze a dimenze](posts/linear-dependence-and-independence-basis-and-dimension/)
- injektivní funkce, surjektivní funkce

## Lineární transformace

Speciální funkci, která zachovává strukturu vektorového prostoru, nazýváme **lineární transformací (linear transformation)**. Jde o důležitý pojem, který se velmi často objevuje napříč čistou matematikou, aplikovanou matematikou, společenskými vědami, přírodními vědami i inženýrstvím.

> **Definice**  
> Nechť $\mathbb{V}$ a $\mathbb{W}$ jsou $F$-vektorové prostory. Funkci $T: \mathbb{V} \to \mathbb{W}$ nazveme **lineární transformací (linear transformation)** z $\mathbb{V}$ do $\mathbb{W}$, pokud pro všechna $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ a $c \in F$ platí následující dvě podmínky.
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

Tvrzení „$T$ je lineární transformace“ se zkráceně vyjadřuje také jako „$T$ je **lineární (linear)**“. Lineární transformace $T: \mathbb{V} \to \mathbb{W}$ splňuje následující čtyři vlastnosti.

> 1. $T$ je lineární $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ je lineární $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ je lineární $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ je lineární $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> Při dokazování linearity nějaké funkce je obvykle výhodné použít 2. vlastnost.
{: .prompt-tip }

> Lineární algebra má široké a rozmanité využití také v geometrii, protože mnoho důležitých geometrických transformací je lineárních. Zejména tři hlavní geometrické transformace — **rotace**, **symetrie** a **projekce** — jsou lineárními transformacemi.
{: .prompt-tip }

Následující dvě lineární transformace se objevují obzvlášť často.

> **Identita a nulová transformace**  
> Pro $F$-vektorové prostory $\mathbb{V}, \mathbb{W}$:
> - **identita (identity transformation)**: funkce $I_\mathbb{V}: \mathbb{V} \to \mathbb{V}$ definovaná tak, že pro všechna $\mathbf{x} \in \mathbb{V}$ platí $I_\mathbb{V}(\mathbf{x}) = \mathbf{x}$
> - **nulová transformace (zero transformation)**: funkce $T_0: \mathbb{V} \to \mathbb{W}$ definovaná tak, že pro všechna $\mathbf{x} \in \mathbb{V}$ platí $T_0(\mathbf{x}) = \mathbf{0}$
{: .prompt-info }

Kromě toho spadá pod lineární transformace řada dalších pojmů.

> **Příklady lineárních transformací**  
> - rotace
> - symetrie
> - projekce
> - [transpozice](/posts/vector-spaces-subspaces-and-matrices/#transponovaná-matice-symetrická-matice-antisymetrická-matice)
> - derivace diferencovatelné funkce
> - integrál spojité funkce
{: .prompt-tip }

## Jádrový prostor a obraz

### Definice jádrového prostoru a obrazu

> **Definice**  
> Pro vektorové prostory $\mathbb{V}, \mathbb{W}$ a lineární transformaci $T: \mathbb{V} \to \mathbb{W}$:
> - **nulový prostor (null space)** neboli **jádro (kernel)**: množina všech $\mathbf{x} \in \mathbb{V}$ takových, že $T(\mathbf{x}) = \mathbf{0}$; značíme $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **obor hodnot (range)** neboli **obraz (image)**: podmnožina $\mathbb{W}$ tvořená všemi hodnotami funkce $T$; značíme $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **e.g.** Pro vektorové prostory $\mathbb{V}, \mathbb{W}$, identitu $I: \mathbb{V} \to \mathbb{V}$ a nulovou transformaci $T_0: \mathbb{V} \to \mathbb{W}$ platí:
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T_0) = \mathbb{V}$
> - $\mathrm{R}(T_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

Dále je to klíčový fakt, ke kterému se budeme opakovaně vracet: nulový prostor a obraz lineární transformace jsou [podprostory](/posts/vector-spaces-subspaces-and-matrices/#podprostor).

> **Věta 1**  
> Pro vektorové prostory $\mathbb{V}, \mathbb{W}$ a lineární transformaci $T: \mathbb{V} \to \mathbb{W}$ jsou $\mathrm{N}(T)$ a $\mathrm{R}(T)$ podprostory prostorů $\mathbb{V}$, resp. $\mathbb{W}$.
>
> **Důkaz**  
> Nulové vektory prostorů $\mathbb{V}, \mathbb{W}$ označme $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$.
>
> Jelikož $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, platí $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$. Dále pro $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T),\ c \in F$ platí:
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{N}(T),\ c\mathbf{x} \in \mathrm{N}(T)$, a tedy $\mathrm{N}(T)$ je podprostor $\mathbb{V}$](/posts/vector-spaces-subspaces-and-matrices/#podprostor).
>
> Podobně, protože $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, máme $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$. A jelikož $\forall \mathbf{x}, \mathbf{y} \in \mathrm{R}(T),\ c \in F \ (\exists \mathbf{v}, \mathbf{w} \in \mathbb{V} \ (T(\mathbf{v}) = \mathbf{x}\ \wedge \ T(\mathbf{w}) = \mathbf{y}))$, platí
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{R}(T),\ c\mathbf{x} \in \mathrm{R}(T)$, a tedy $\mathrm{R}(T)$ je podprostor $\mathbb{W}$](/posts/vector-spaces-subspaces-and-matrices/#podprostor). $\blacksquare$
{: .prompt-info }

Na druhé straně, pro vektorové prostory $\mathbb{V}, \mathbb{W}$ a lineární transformaci $T: \mathbb{V} \to \mathbb{W}$, známe-li [bázi](/posts/linear-dependence-and-independence-basis-and-dimension/#báze) prostoru $\mathbb{V}$, $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$, můžeme [generující množinu](/posts/vectors-and-linear-combinations/#generovani-span-linearni-kombinace-cmathbfv--dmathbfw) obrazu $\mathrm{R}(T)$ najít následovně.

> **Věta 2**  
> Pro vektorové prostory $\mathbb{V}, \mathbb{W}$, lineární transformaci $T: \mathbb{V} \to \mathbb{W}$ a [bázi](/posts/linear-dependence-and-independence-basis-and-dimension/#báze) prostoru $\mathbb{V}$, $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$, platí:
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **Důkaz**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> Protože $\mathrm{R}(T)$ je podprostor, podle **Věty 2** v článku [Vektorové prostory, podprostory a matice](/posts/vector-spaces-subspaces-and-matrices/#podprostor) platí:
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> Dále:
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> Jelikož $\beta$ je báze $\mathbb{V}$, platí:
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(kde } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> Protože $T$ je lineární:
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ platí zároveň $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ i $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$, tedy $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

Tato věta platí i tehdy, když je báze $\beta$ nekonečná.

### Dimenzní věta

Protože nulový prostor i obraz jsou velmi důležité podprostory, zavádí se pro jejich [dimenzi](/posts/linear-dependence-and-independence-basis-and-dimension/#dimenze) speciální názvy.

> Pro vektorové prostory $\mathbb{V}, \mathbb{W}$ a lineární transformaci $T: \mathbb{V} \to \mathbb{W}$ předpokládejme, že $\mathrm{N}(T)$ a $\mathrm{R}(T)$ jsou konečněrozměrné.
> - **dimenze nulového prostoru (nullity)**: dimenze $\mathrm{N}(T)$; značí se $\mathrm{nullity}(T)$
> - **hodnost (rank)**: dimenze $\mathrm{R}(T)$; značí se $\mathrm{rank}(T)$
{: .prompt-info }

U lineárních transformací platí: čím větší je dimenze nulového prostoru, tím menší je hodnost, a naopak.

> **Věta 3: dimenzní věta (dimension theorem)**  
> Pro vektorové prostory $\mathbb{V}, \mathbb{W}$ a lineární transformaci $T: \mathbb{V}\to \mathbb{W}$ platí, že pokud je $\mathbb{V}$ konečněrozměrný, pak:
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### Důkaz

Nechť $\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$ a báze $\mathrm{N}(T)$ je $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$.

Podle [**Důsledku 6-1** z článku „Lineární závislost a lineární nezávislost, báze a dimenze“](/posts/linear-dependence-and-independence-basis-and-dimension/#dimenze-podprostoru) lze $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ rozšířit na bázi $\mathbb{V}$, tj. získáme bázi $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$.

Nyní ukážeme, že $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ je bází $\mathrm{R}(T)$. Nejprve, protože pro $1 \leq i \leq k$ platí $T(\mathbf{v}_i) = 0$, dostaneme z [**Věty 2**](#definice-jádrového-prostoru-a-obrazu):

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

Tedy $S$ je generující množina $\mathrm{R}(T)$. Podle [**Důsledku 5-2 věty o nahrazení**](/posts/linear-dependence-and-independence-basis-and-dimension/#dimenze) stačí ukázat, že $S$ je lineárně nezávislá, a tím bude $S$ bází $\mathrm{R}(T)$.

Nechť $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (kde $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$). Protože $T$ je lineární,

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

Proto:

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

Protože $\beta$ je báze $\mathbb{V}$, jediné řešení rovnice $\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ je

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

a z toho plyne

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

Tedy $S$ je lineárně nezávislá a je bází $\mathrm{R}(T)$.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### Lineární transformace a injekce, surjekce

U lineárních transformací souvisí injekce (injection) a surjekce (surjection) úzce s hodností a dimenzí nulového prostoru.

> **Věta 4**  
> Pro vektorové prostory $\mathbb{V}, \mathbb{W}$ a lineární transformaci $T: \mathbb{V} \to \mathbb{W}$ platí:
>
> $$ T\text{ je injektivní.} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **Věta 5**  
> Nechť mají konečněrozměrné vektorové prostory $\mathbb{V}, \mathbb{W}$ stejnou dimenzi. Pak jsou pro lineární transformaci $T: \mathbb{V} \to \mathbb{W}$ následující čtyři tvrzení ekvivalentní.
> 1. $T$ je injektivní.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ je surjektivní.
{: .prompt-info }

Pomocí [dimenzní věty](#dimenzní-věta), [vlastností 1 a 3 lineární transformace](#lineární-transformace) a [**Věty 6** z článku „Lineární závislost a lineární nezávislost, báze a dimenze“](/posts/linear-dependence-and-independence-basis-and-dimension/#dimenze-podprostoru) lze dokázat **Větu 4** a **Větu 5**.

Tyto dvě věty jsou užitečné při rozhodování, zda je daná lineární transformace injektivní nebo surjektivní.

> Pro nekonečněrozměrný vektorový prostor $\mathbb{V}$ a lineární transformaci $T: \mathbb{V} \to \mathbb{V}$ neplatí, že injektivita a surjektivita jsou ekvivalentní.
{: .prompt-warning }

Navíc, je-li nějaká lineární transformace injektivní, může být v některých situacích užitečná následující věta pro rozhodování, zda je daná podmnožina vektorového prostoru lineárně nezávislá.

> **Věta 6**  
> Pro vektorové prostory $\mathbb{V}, \mathbb{W}$, injektivní lineární transformaci $T: \mathbb{V} \to \mathbb{W}$ a podmnožinu $S \subseteq \mathbb{V}$ platí:
>
> $$ S\text{ je lineárně nezávislá.} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \}\text{ je lineárně nezávislá.} $$
>
{: .prompt-info }

## Lineární transformace a báze

Důležitou vlastností lineárních transformací je, že jejich chování je určeno tím, jak působí na bázi.

> **Věta 7**  
> Nechť $\mathbb{V}, \mathbb{W}$ jsou $F$-vektorové prostory, $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ je báze $\mathbb{V}$ a $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$ jsou vektory. Pak existuje právě jedna lineární transformace $T: \mathbb{V} \to \mathbb{W}$ splňující:
>
> $$ i = 1, 2, \dots, n \text{ a } T(\mathbf{v}_i) = \mathbf{w}_i $$
>
> **Důkaz**  
> Pro $\mathbf{x} \in \mathbb{V}$ je následující vyjádření jako lineární kombinace jednoznačné:
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ (}a_1, a_2, \dots, a_n \in F \text{)} $$
>
> Definujme lineární transformaci $T: \mathbb{V} \to \mathbb{W}$ takto:
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> i) Pro $i = 1, 2, \dots, n$ platí $T(\mathbf{v}_i) = \mathbf{w}_i$.
>
> ii)
>
> Předpokládejme, že jiná lineární transformace $U: \mathbb{V} \to \mathbb{W}$ splňuje pro $i = 1, 2, \dots, n$ rovněž $U(\mathbf{v}\_i) = \mathbf{w}\_i$. Pak pro $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$ platí:
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i) $$
>
> $$ \therefore U = T. $$
>
> Z i), ii) plyne, že lineární transformace splňující $T(\mathbf{v}\_i) = \mathbf{w}\_i$ pro $i = 1, 2, \dots, n$ je jednoznačně dána předpisem:
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i $$
>
> $\blacksquare$
>
> **Důsledek 7-1**  
> Nechť vektorový prostor $\mathbb{V}$ obsahuje konečnou bázi $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$. Pokud dvě lineární transformace $U, T: \mathbb{V} \to \mathbf{W}$ splňují pro $i = 1, 2, \dots, n$ rovnost $U(\mathbf{v}_i) = T(\mathbf{v}_i)$, pak $U = T$.  
> Tj. <u>pokud se dvě lineární transformace shodují na bázi, jsou totožné.</u>
{: .prompt-info }
