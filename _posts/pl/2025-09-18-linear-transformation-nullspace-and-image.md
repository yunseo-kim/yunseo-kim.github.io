---
title: "Przekształcenia liniowe, jądro i obraz"
description: "Omawiamy definicję przekształcenia liniowego, dwa kluczowe podprzestrzenie: jądro i obraz, oraz twierdzenia o rządzie i defekcie (nullity, rank)."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Linear Transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [Wektory i kombinacje liniowe](/posts/vectors-and-linear-combinations/)
- [Przestrzenie wektorowe, podprzestrzenie i macierze](/posts/vector-spaces-subspaces-and-matrices/)
- [Zależność liniowa i niezależność liniowa, baza i wymiar](posts/linear-dependence-and-independence-basis-and-dimension/)
- funkcja injektywna, funkcja surjektywna

## Przekształcenia liniowe

Szczególną funkcję, która zachowuje strukturę przestrzeni wektorowej, nazywamy **przekształceniem liniowym (linear transformation)**. Jest to kluczowe pojęcie, bardzo często pojawiające się w czystej matematyce, matematyce stosowanej, naukach społecznych, przyrodniczych oraz w inżynierii.

> **Definicja**  
> Niech $\mathbb{V}$ oraz $\mathbb{W}$ będą $F$-przestrzeniami wektorowymi. Funkcję $T: \mathbb{V} \to \mathbb{W}$ nazywamy **przekształceniem liniowym (linear transformation)** z $\mathbb{V}$ do $\mathbb{W}$, jeśli dla wszystkich $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ oraz $c \in F$ spełnione są dwa warunki:
> 1. $T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x}) + T(\mathbf{y})$
> 2. $T(c\mathbf{x}) = cT(\mathbf{x})$
{: .prompt-info }

Stwierdzenie, że $T$ jest przekształceniem liniowym, skraca się często do „$T$ jest **liniowe (linear)**”. Przekształcenie liniowe $T: \mathbb{V} \to \mathbb{W}$ spełnia następujące cztery własności.

> 1. $T$ jest liniowe $\quad \Rightarrow \quad $ $T(\mathbf{0}) = \mathbf{0}$
> 2. $T$ jest liniowe $\quad \Leftrightarrow \quad $ $T(c\mathbf{x} + \mathbf{y}) = cT(\mathbf{x}) + T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V},\, c \in F$
> 3. $T$ jest liniowe $\quad \Rightarrow \quad $ $T(\mathbf{x} - \mathbf{y}) = T(\mathbf{x}) - T(\mathbf{y}) \; \forall \, \mathbf{x}, \mathbf{y} \in \mathbb{V}$
> 4. $T$ jest liniowe $\quad \Leftrightarrow \quad $ $T\left( \sum\_{i=1}^n a\_i \mathbf{x}\_i \right) = \sum\_{i=1}^n a\_i T(\mathbf{x}\_i)$
{: .prompt-info }

> Przy wykazywaniu liniowości danej funkcji zazwyczaj najwygodniej jest użyć własności 2.
{: .prompt-tip }

> Algebrę liniową można szeroko i różnorodnie stosować także w geometrii, ponieważ wiele ważnych przekształceń geometrycznych jest liniowych. W szczególności trzy kluczowe przekształcenia geometryczne — **obrót**, **symetria**, **rzut** — są przekształceniami liniowymi.
{: .prompt-tip }

Szczególnie często pojawiają się dwa następujące przekształcenia liniowe.

> **Przekształcenie identycznościowe i przekształcenie zerowe**  
> Dla $F$-przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$:
> - **przekształcenie identycznościowe (identity transformation)**: funkcja $I_\mathbb{V}: \mathbb{V} \to \mathbb{V}$ zdefiniowana przez $I_\mathbb{V}(\mathbf{x}) = \mathbf{x}$ dla wszystkich $\mathbf{x} \in \mathbb{V}$
> - **przekształcenie zerowe (zero transformation)**: funkcja $T_0: \mathbb{V} \to \mathbb{W}$ zdefiniowana przez $T_0(\mathbf{x}) = \mathbf{0}$ dla wszystkich $\mathbf{x} \in \mathbb{V}$
{: .prompt-info }

Poza tym wiele innych pojęć również jest przykładami przekształceń liniowych.

> **Przykłady przekształceń liniowych**  
> - obrót
> - symetria
> - rzut
> - [transpozycja](/posts/vector-spaces-subspaces-and-matrices/#macierz-transponowana-macierz-symetryczna-macierz-antysymetryczna)
> - pochodna funkcji różniczkowalnej
> - całka funkcji ciągłej
{: .prompt-tip }

## Jądro i obraz

### Definicje jądra i obrazu

> **Definicja**  
> Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$:
> - **jądro (kernel)**, czyli **przestrzeń zerowa (null space)**: zbiór tych $\mathbf{x} \in \mathbb{V}$, dla których $T(\mathbf{x}) = \mathbf{0}$; oznaczamy $\mathrm{N}(T)$
>
>   $$ \mathrm{N}(T) = \{ \mathbf{x} \in \mathbb{V}: T(\mathbf{x}) = \mathbf{0} \} $$
>
> - **zbiór wartości (range)**, czyli **obraz (image)**: podzbiór $\mathbb{W}$ złożony z wartości funkcji $T$; oznaczamy $\mathrm{R}(T)$
>
>   $$ \mathrm{R}(T) = \{ T(\mathbf{x}): \mathbf{x} \in \mathbb{V} \}$$
>
{: .prompt-info }

> **e.g.** Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz przekształcenia identycznościowego $I: \mathbb{V} \to \mathbb{V}$ i przekształcenia zerowego $T_0: \mathbb{V} \to \mathbb{W}$ zachodzi:
> - $\mathrm{N}(I) = \\{\mathbf{0}\\}$
> - $\mathrm{R}(I) = \mathbb{V}$
> - $\mathrm{N}(T_0) = \mathbb{V}$
> - $\mathrm{R}(T_0) = \\{\mathbf{0}\\}$
{: .prompt-tip }

To będzie pojawiać się dalej wielokrotnie: jądro i obraz przekształcenia liniowego są [podprzestrzeniami](/posts/vector-spaces-subspaces-and-matrices/#podprzestrzen) przestrzeni wektorowej.

> **Twierdzenie 1**  
> Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$ zbiory $\mathrm{N}(T)$ i $\mathrm{R}(T)$ są odpowiednio podprzestrzeniami $\mathbb{V}$ i $\mathbb{W}$.
>
> **Dowód**  
> Oznaczmy wektory zerowe $\mathbb{V}$ oraz $\mathbb{W}$ odpowiednio przez $\mathbf{0}\_\mathbb{V}, \mathbf{0}\_\mathbb{W}$.
>
> Ponieważ $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, mamy $\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T)$. Ponadto dla $\mathbf{x}, \mathbf{y} \in \mathrm{N}(T)$ oraz $c \in F$ zachodzi:
>
> $$ \begin{align*}
> T(\mathbf{x} + \mathbf{y}) &= T(\mathbf{x}) + T(\mathbf{y}) = \mathbf{0}_\mathbb{W} + \mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}, \\
> T(c\mathbf{x}) &= cT(\mathbf{x}) = c\mathbf{0}_\mathbb{W} = \mathbf{0}_\mathbb{W}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}\_\mathbb{V} \in \mathrm{N}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{N}(T),\ c\mathbf{x} \in \mathrm{N}(T)$, więc $\mathrm{N}(T)$ jest podprzestrzenią $\mathbb{V}$](/posts/vector-spaces-subspaces-and-matrices/#podprzestrzen).
>
> Analogicznie, ponieważ $T(\mathbf{0}\_\mathbb{V}) = \mathbf{0}\_\mathbb{W}$, mamy $\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T)$ oraz $\forall \mathbf{x}, \mathbf{y} \in \mathrm{R}(T),\ c \in F \ (\exists \mathbf{v}, \mathbf{w} \in \mathbb{V} \ (T(\mathbf{v}) = \mathbf{x}\ \wedge \ T(\mathbf{w}) = \mathbf{y}))$, więc
>
> $$ \begin{align*}
> T(\mathbf{v} + \mathbf{w}) &= T(\mathbf{v}) + T(\mathbf{w}) = \mathbf{x} + \mathbf{y}, \\
> T(c\mathbf{v}) &= cT(\mathbf{v}) = c\mathbf{x}.
> \end{align*} $$
>
> $\therefore$ [$\mathbf{0}\_\mathbb{W} \in \mathrm{R}(T),\ \mathbf{x} + \mathbf{y} \in \mathrm{R}(T),\ c\mathbf{x} \in \mathrm{R}(T)$, więc $\mathrm{R}(T)$ jest podprzestrzenią $\mathbb{W}$](/posts/vector-spaces-subspaces-and-matrices/#podprzestrzen). $\blacksquare$
{: .prompt-info }

Z kolei dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ i przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$, jeśli znamy [bazę](/posts/linear-dependence-and-independence-basis-and-dimension/#baza) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ przestrzeni $\mathbb{V}$, to [zbiór generujący](/posts/vectors-and-linear-combinations/#rozpinanie) obrazu $\mathrm{R}(T)$ można znaleźć następująco.

> **Twierdzenie 2**  
> Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$ i [bazy](/posts/linear-dependence-and-independence-basis-and-dimension/#baza) $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ przestrzeni $\mathbb{V}$ zachodzi:
>
> $$ \mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), 
\dots, T(\mathbf{v}_n) \}) $$
>
> **Dowód**  
>
> $$ T(\mathbf{v}_i) \in \mathrm{R}(T) \quad \forall \mathbf{v}_i \in \beta. $$
>
> Ponieważ $\mathrm{R}(T)$ jest podprzestrzenią, na mocy **Twierdzenia 2** z tekstu [Przestrzenie wektorowe, podprzestrzenie i macierze](/posts/vector-spaces-subspaces-and-matrices/#podprzestrzen) mamy
>
> $$ \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) = \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) \subseteq \mathrm{R}(T). $$
>
> Ponadto,
>
> $$ \forall \mathbf{w} \in \mathrm{R}(T) \ (\exists \mathbf{v} \in \mathbb{V} \ (\mathbf{w} = T(\mathbf{v}))). $$
>
> Ponieważ $\beta$ jest bazą $\mathbb{V}$,
>
> $$ \mathbf{v} = \sum_{i=1}^n a_i \mathbf{v}_i \quad \text{(gdzie } a_1, a_2, \dots, a_n \in F \text{)}. $$
>
> A ponieważ $T$ jest liniowe,
>
> $$ \mathbf{w} = T(\mathbf{v}) = \sum_{i=1}^n a_i T(\mathbf{v}_i) \in \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) $$
>
> $$ \mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \}) = \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}). $$
>
> $\therefore$ $\mathrm{R}(T) \supseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$ i jednocześnie $\mathrm{R}(T) \subseteq \mathrm{span}(\{T(\mathbf{v}_i): \mathbf{v}_i \in \beta \})$, zatem $\mathrm{R}(T) = \mathrm{span}(\{T(\mathbf{v}): \mathbf{v} \in \beta \})$. $\blacksquare$
{: .prompt-info }

Twierdzenie to pozostaje prawdziwe także wtedy, gdy baza $\beta$ jest zbiorem nieskończonym.

### Twierdzenie o rządzie i defekcie

Ponieważ jądro i obraz są bardzo ważnymi podprzestrzeniami, wyróżnia się także ich [wymiary](/posts/linear-dependence-and-independence-basis-and-dimension/#wymiar) specjalnymi nazwami.

> Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$ załóżmy, że $\mathrm{N}(T)$ i $\mathrm{R}(T)$ są skończenie wymiarowe.
> - **wymiar jądra (nullity)**: wymiar $\mathrm{N}(T)$, oznaczany $\mathrm{nullity}(T)$
> - **rząd (rank)**: wymiar $\mathrm{R}(T)$, oznaczany $\mathrm{rank}(T)$
{: .prompt-info }

W przekształceniu liniowym, im większy jest wymiar jądra, tym mniejszy jest rząd; i odwrotnie, im większy jest rząd, tym mniejszy jest wymiar jądra.

> **Twierdzenie 3: twierdzenie o wymiarze (dimension theorem)**  
> Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz przekształcenia liniowego $T: \mathbb{V}\to \mathbb{W}$, jeśli $\mathbb{V}$ jest skończenie wymiarowa, to zachodzi:
>
> $$ \mathrm{nullity}(T) + \mathrm{rank}(T) = \dim(\mathbb{V}) $$
>
{: .prompt-info }

#### Dowód

Niech $\dim(\mathbb{V}) = n$, $\mathrm{nullity}(T) = \dim(\mathrm{N}(T)) = k$ oraz niech bazą $\mathrm{N}(T)$ będzie $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$.

Zgodnie z [Wnioskiem 6-1 z tekstu „Zależność liniowa i niezależność liniowa, baza i wymiar”](/posts/linear-dependence-and-independence-basis-and-dimension/#wymiar-podprzestrzeni), zbiór $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \\}$ można rozszerzyć do bazy $\mathbb{V}$, tj. otrzymać bazę $\beta = \\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$.

Pokażemy teraz, że $S = \\{T(\mathbf{v}\_{k+1}), T(\mathbf{v}\_{k+2}), \dots, T(\mathbf{v}\_n) \\}$ jest bazą $\mathrm{R}(T)$. Ponieważ dla $1 \leq i \leq k$ mamy $T(\mathbf{v}_i) = 0$, z [**Twierdzenia 2**](#definicje-jadra-i-obrazu) wynika:

$$ \begin{align*}
\mathrm{R}(T) &= \mathrm{span}(\{T(\mathbf{v}_1), T(\mathbf{v}_2), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(\{T(\mathbf{v}_{k+1}), T(\mathbf{v}_{k+2}), \dots, T(\mathbf{v}_n) \}) \\
&= \mathrm{span}(S).
\end{align*} $$

Zatem $S$ jest zbiorem generującym $\mathrm{R}(T)$. Teraz, na mocy [Wniosku 5-2 z twierdzenia o zastępowaniu](/posts/linear-dependence-and-independence-basis-and-dimension/#wymiar), jeśli pokażemy, że $S$ jest liniowo niezależny, to udowodnimy, że $S$ jest bazą $\mathrm{R}(T)$.

Załóżmy, że $\sum\_{i=k+1}^n b\_i T(\mathbf{v}\_i) = 0$ (gdzie $b\_{k+1}, b\_{k+2}, \dots, b\_n \in F$). Ponieważ $T$ jest liniowe,

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \Leftrightarrow T\left(\sum_{i=k+1}^n b_i \mathbf{v}_i \right) = 0 \Leftrightarrow \sum_{i=k+1}^n b_i \mathbf{v}_i \in \mathrm{N}(T). $$

Stąd

$$ \begin{align*}
&\exists c_1, c_2, \dots, c_k \in F, \\
&\sum_{i=k+1}^n b_i \mathbf{v}_i = \sum_{i=1}^k c_i \mathbf{v}_i \\
\Leftrightarrow &\sum_{i=1}^k (-c_i)\mathbf{v}_i + \sum_{i=k+1}^n b_i \mathbf{v}_i = 0.
\end{align*} $$

Ponieważ $\beta$ jest bazą $\mathbb{V}$, jedynym rozwiązaniem równania $\sum\_{i=1}^k (-c\_i)\mathbf{v}\_i + \sum\_{i=k+1}^n b\_i \mathbf{v}\_i = 0$ jest

$$ c_1 = c_2 = \cdots = c_k = b_{k+1} = b_{k+2} = \cdots = b_n = 0 $$

a zatem

$$ \sum_{i=k+1}^n b_i T(\mathbf{v}_i) = 0 \quad \Rightarrow \quad b_i = 0. $$

Czyli $S$ jest liniowo niezależny i jest bazą $\mathrm{R}(T)$.

$$ \therefore \mathrm{rank}(T) = n - k = \dim{\mathbb{V}} - \mathrm{nullity}(T). \blacksquare $$

### Przekształcenia liniowe a iniekcje i surjekcje

W przypadku przekształceń liniowych własności bycia iniekcją (injection) i surjekcją (surjection) są ściśle powiązane z rzędem i wymiarem jądra.

> **Twierdzenie 4**  
> Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$:
>
> $$ T\text{ jest iniekcją.} \quad \Leftrightarrow \quad \mathrm{N}(T) = \{\mathbf{0}\}. $$
>
{: .prompt-info }

> **Twierdzenie 5**  
> Jeżeli skończenie wymiarowe przestrzenie wektorowe $\mathbb{V}, \mathbb{W}$ mają ten sam wymiar, to dla przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$ następujące cztery zdania są równoważne:
> 1. $T$ jest iniekcją.
> 2. $\mathrm{nullity}(T) = 0$
> 3. $\mathrm{rank}(T) = \dim(\mathbb{V})$
> 4. $T$ jest surjekcją.
{: .prompt-info }

Korzystając z [twierdzenia o wymiarze](#twierdzenie-o-rzadzie-i-defekcie), [własności 1 i 3 przekształceń liniowych](#przeksztalcenia-liniowe) oraz [Twierdzenia 6 z tekstu „Zależność liniowa i niezależność liniowa, baza i wymiar”](/posts/linear-dependence-and-independence-basis-and-dimension/#wymiar-podprzestrzeni), można udowodnić **Twierdzenie 4** i **Twierdzenie 5**.

Te dwa twierdzenia są przydatne przy rozstrzyganiu, czy dane przekształcenie liniowe jest iniekcją albo surjekcją.

> Dla nieskończenie wymiarowej przestrzeni wektorowej $\mathbb{V}$ i przekształcenia liniowego $T: \mathbb{V} \to \mathbb{V}$ iniektywność i surjektywność nie są równoważne.
{: .prompt-warning }

Ponadto, jeśli pewne przekształcenie liniowe jest iniekcją, to w zależności od sytuacji przydatne może być następujące twierdzenie do sprawdzania, czy dany podzbiór przestrzeni jest liniowo niezależny.

> **Twierdzenie 6**  
> Dla przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ oraz iniektywnego przekształcenia liniowego $T: \mathbb{V} \to \mathbb{W}$ i podzbioru $S \subseteq \mathbb{V}$ zachodzi:
>
> $$ S\text{ jest liniowo niezależny.} \quad \Leftrightarrow \quad \{T(\mathbf{v}): \mathbf{v} \in S \}\text{ jest liniowo niezależny.} $$
>
{: .prompt-info }

## Przekształcenia liniowe a baza

Ważną cechą przekształceń liniowych jest to, że ich „zachowanie” jest wyznaczone przez wartości na bazie.

> **Twierdzenie 7**  
> Dla $F$-przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$, bazy $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$ przestrzeni $\mathbb{V}$ oraz wektorów $\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n \in \mathbb{W}$ istnieje dokładnie jedno przekształcenie liniowe $T: \mathbb{V} \to \mathbb{W}$ spełniające warunek:
>
> $$ i = 1, 2, \dots, n \text{ oraz } T(\mathbf{v}_i) = \mathbf{w}_i $$
>
> **Dowód**  
> Dla $\mathbf{x} \in \mathbb{V}$ następujące przedstawienie jako kombinacja liniowa jest jednoznaczne:
>
> $$ \mathbf{x} = \sum_{i=1}^n a_i \mathbf{v}_i \text{ (}a_1, a_2, \dots, a_n \in F \text{)} $$
>
> Zdefiniujmy przekształcenie liniowe $T: \mathbb{V} \to \mathbb{W}$ przez
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. $$
>
> i) Dla $i = 1, 2, \dots, n$ mamy $T(\mathbf{v}_i) = \mathbf{w}_i$.
>
> ii)
>
> Jeśli założymy, że inne przekształcenie liniowe $U: \mathbb{V} \to \mathbb{W}$ spełnia $U(\mathbf{v}\_i) = \mathbf{w}\_i$ dla $i = 1, 2, \dots, n$, to dla $\mathbf{x} = \sum\_{i=1}^n a\_i \mathbf{v}\_i \in \mathbb{V}$ zachodzi
>
> $$ U(\mathbf{x}) = \sum_{i=1}^n a_i U(\mathbf{v}_i) = \sum_{i=1}^n a_i \mathbf{w}_i = T(\mathbf{x}_i). $$
>
> $$ \therefore U = T. $$
>
> Z punktów i), ii) wynika, że przekształcenie liniowe spełniające $T(\mathbf{v}\_i) = \mathbf{w}\_i$ dla $i = 1, 2, \dots, n$ jest jedyne i ma postać
>
> $$T(\mathbf{x}) = T\left( \sum_{i=1}^n a_i \mathbf{v}_i \right) = \sum_{i=1}^n a_i \mathbf{w}_i. $$
>
> $\blacksquare$
>
> **Wniosek 7-1**  
> Dla dwóch przestrzeni wektorowych $\mathbb{V}, \mathbb{W}$ załóżmy, że $\mathbb{V}$ zawiera skończoną bazę $\\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_n \\}$. Jeśli dwa przekształcenia liniowe $U, T: \mathbb{V} \to \mathbf{W}$ spełniają $U(\mathbf{v}_i) = T(\mathbf{v}_i)$ dla $i = 1, 2, \dots, n$, to $U = T$.  
> Innymi słowy, <u>jeśli wartości funkcji są takie same na bazie, to jest to to samo przekształcenie liniowe.</u>
{: .prompt-info }
