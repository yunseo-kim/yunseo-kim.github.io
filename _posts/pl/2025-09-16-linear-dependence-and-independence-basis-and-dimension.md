---
title: "Zależność liniowa i niezależność liniowa, baza i wymiar"
description: "Porządkujemy pojęcia zależności i niezależności liniowej oraz bazy i wymiaru przestrzeni wektorowej."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Wymagania wstępne
- [Wektory i kombinacje liniowe](/posts/vectors-and-linear-combinations/)
- [Przestrzenie wektorowe, podprzestrzenie i macierze](/posts/vector-spaces-subspaces-and-matrices/)

## Zależność liniowa i niezależność liniowa

Dla pewnej [przestrzeni wektorowej](/posts/vector-spaces-subspaces-and-matrices/#przestrzen-wektorowa) $\mathbb{V}$ oraz [podprzestrzeni](/posts/vector-spaces-subspaces-and-matrices/#podprzestrzen) $\mathbb{W}$ załóżmy, że chcemy znaleźć możliwie mały skończony podzbiór $S$, który generuje (rozpina) $\mathbb{W}$.

Jeśli dla zbioru $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ zachodzi $\mathrm{span}(S) = \mathbb{W}$, to jak rozstrzygnąć, czy nie istnieje właściwy podzbiór $S$, który również generuje $\mathbb{W}$? Jest to to samo, co problem sprawdzenia, czy jeden z wektorów wybranych z $S$ da się wyrazić jako [kombinację liniową](/posts/vectors-and-linear-combinations/#kombinacja-liniowa-wektorow) pozostałych. Na przykład, warunkiem koniecznym i wystarczającym, aby wyrazić $\mathbf{u}_4$ jako kombinację liniową pozostałych trzech wektorów, jest istnienie skalarów $a_1, a_2, a_3$ spełniających:

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

Jednak za każdym razem konstruowanie układu równań liniowych osobno dla $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ i sprawdzanie, czy istnieje rozwiązanie, jest uciążliwe, więc nieco przekształćmy równanie.

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

Jeżeli pewien wektor z $S$ jest kombinacją liniową pozostałych wektorów, to wówczas przy zapisie wektora zerowego jako kombinacji liniowej elementów $S$ istnieje reprezentacja, w której co najmniej jeden współczynnik spośród $a_1, a_2, a_3, a_4$ jest różny od $0$. Odwrotność tego stwierdzenia również jest prawdziwa: jeśli istnieje sposób wyrażenia wektora zerowego jako kombinacji liniowej wektorów należących do $S$, w którym co najmniej jeden ze współczynników $a_1, a_2, a_3, a_4$ jest różny od $0$, to pewien wektor z $S$ jest kombinacją liniową pozostałych.

Uogólniając, definiujemy następująco **zależność liniową** i **niezależność liniową**.

> **Definicja**  
> Dla podzbioru $S$ przestrzeni wektorowej $\mathbb{V}$, jeżeli istnieje skończona liczba parami różnych wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ oraz skalary $a_1, a_2, \dots, a_n$, z których co najmniej jeden jest różny od $0$, takie że $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$, to zbiór $S$ (i jego wektory) nazywa się **liniowo zależnym (linearly dependent)**. W przeciwnym razie nazywa się go **liniowo niezależnym (linearly independent)**.
{: .prompt-info }

Dla dowolnych wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$, jeśli $a_1 = a_2 = \cdots = a_n = 0$, to $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$; nazywamy to **trywialnym przedstawieniem (trivial representation of $\mathbf{0}$)** wektora zerowego.

Poniższe trzy stwierdzenia o zbiorach liniowo niezależnych są zawsze prawdziwe w każdej przestrzeni wektorowej. W szczególności **Stwierdzenie 3**, jak widzieliśmy, jest bardzo użyteczne przy sprawdzaniu, czy dany zbiór skończony jest liniowo niezależny.

> - **Stwierdzenie 1**: Zbiór pusty jest liniowo niezależny. Aby zbiór był liniowo zależny, nie może być pusty.
> - **Stwierdzenie 2**: Zbiór złożony z jednego niezerowego wektora jest liniowo niezależny.
> - **Stwierdzenie 3**: Warunkiem koniecznym i wystarczającym, aby dany zbiór był liniowo niezależny, jest to, że jedynym sposobem wyrażenia $\mathbf{0}$ jako kombinacji liniowej tego zbioru jest przedstawienie trywialne.
{: .prompt-info }

Ważne są również następujące twierdzenia.

> **Twierdzenie 1**  
> Niech $\mathbb{V}$ będzie przestrzenią wektorową oraz $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Jeśli $S_1$ jest liniowo zależny, to $S_2$ również jest liniowo zależny.
>
> **Wniosek 1-1**  
> Niech $\mathbb{V}$ będzie przestrzenią wektorową oraz $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Jeśli $S_2$ jest liniowo niezależny, to $S_1$ również jest liniowo niezależny.
{: .prompt-info }

> **Twierdzenie 2**  
> Rozważmy przestrzeń wektorową $\mathbb{V}$ oraz liniowo niezależny podzbiór $S$. Dla wektora $\mathbf{v} \in \mathbb{V}$, który nie należy do $S$, warunkiem koniecznym i wystarczającym, aby $S \cup \\{\mathbf{v}\\}$ było liniowo zależne, jest $\mathbf{v} \in \mathrm{span}(S)$.
>
> Innymi słowy, **jeśli żaden właściwy podzbiór $S$ nie jest w stanie wygenerować tej samej przestrzeni co $S$, to $S$ jest liniowo niezależny.**
{: .prompt-info }

## Baza i wymiar

### Baza

Zbiór generujący $S$ podprzestrzeni $\mathbb{W}$, który jest [liniowo niezależny](#zaleznosc-liniowa-i-niezaleznosc-liniowa), ma szczególną własność: każdy wektor należący do $\mathbb{W}$ można koniecznie wyrazić jako kombinację liniową wektorów z $S$, a ponadto to przedstawienie jest jednoznaczne (**Twierdzenie 3**). Dlatego liniowo niezależny zbiór generujący danej przestrzeni wektorowej definiuje się szczególnie jako **bazę (basis)**.

> **Definicja bazy**  
> Dla przestrzeni wektorowej $\mathbb{V}$ i jej podzbioru $\beta$, jeśli $\beta$ jest liniowo niezależny i generuje $\mathbb{V}$, to $\beta$ nazywa się **bazą (basis)** przestrzeni $\mathbb{V}$. Mówimy wtedy, że wektory z $\beta$ tworzą bazę $\mathbb{V}$.
{: .prompt-info }

> $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$, a $\emptyset$ jest liniowo niezależny. Zatem $\emptyset$ jest bazą przestrzeni punktowej.
{: .prompt-tip }

W szczególności następującą szczególną bazę przestrzeni $F^n$ nazywa się **bazą standardową (standard basis)**.

> **Definicja bazy standardowej**  
> Dla przestrzeni wektorowej $F^n$ rozważmy następujące wektory.
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> Wtedy zbiór $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ jest bazą $F^n$ i nazywa się go **bazą standardową (standard basis)** przestrzeni $F^n$.
{: .prompt-info }

> **Twierdzenie 3**  
> Dla przestrzeni wektorowej $\mathbb{V}$ oraz $n$ parami różnych wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$, zbiór $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ jest bazą $\mathbb{V}$ wtedy i tylko wtedy, gdy „dowolny wektor $\mathbf{v} \in \mathbb{V}$ można przedstawić jako kombinację liniową wektorów z $\beta$, a przedstawienie to jest jednoznaczne”. To znaczy, dla jedynej uporządkowanej $n$-ki skalarów $(a_1, a_2, \dots, a_n)$ wektor $\mathbf{v}$ musi spełniać:
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

Z **Twierdzenia 3** wynika, że jeśli $n$ parami różnych wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ tworzy bazę przestrzeni wektorowej $\mathbb{V}$, to w tej przestrzeni, dla danego wektora $\mathbf{v}$, jednoznacznie wyznaczona jest odpowiadająca mu uporządkowana $n$-ka skalarów $(a_1, a_2, \dots, a_n)$; i odwrotnie, jeśli dana jest uporządkowana $n$-ka skalarów, można odzyskać odpowiadający jej wektor $\mathbf{v}$. Później uporządkujemy to ponownie przy nauce o **odwracalności** i **izomorfizmach**, ale w tym przypadku przestrzenie $\mathbb{V}$ oraz $F^n$ są <u>w istocie takie same</u>.

> **Twierdzenie 4**  
> Jeśli dla zbioru skończonego $S$ zachodzi $\mathrm{span}(S) = \mathbb{V}$, to wśród podzbiorów $S$ istnieje baza przestrzeni $\mathbb{V}$. To znaczy, w tym przypadku baza $\mathbb{V}$ jest zbiorem skończonym.
{: .prompt-info }

> Wiele przestrzeni wektorowych spełnia założenia **Twierdzenia 4**, ale nie jest to konieczne. <u>Baza nie musi być zbiorem skończonym</u>.
{: .prompt-tip }

### Wymiar

> **Twierdzenie 5: twierdzenie o zastępowaniu (replacement theorem)**  
> Niech $G$ będzie zbiorem złożonym z $n$ wektorów oraz $\mathrm{span}(G) = \mathbb{V}$. Jeśli $L$ jest podzbiorem $\mathbb{V}$ złożonym z $m$ liniowo niezależnych wektorów, to $m\leq n$. Ponadto istnieje zbiór $H \subseteq G$ mający $n-m$ wektorów taki, że $\mathrm{span}(L \cup H) = \mathbb{V}$.
{: .prompt-info }

Stąd otrzymujemy dwa bardzo ważne wnioski.

> **Wniosek 5-1 z twierdzenia o zastępowaniu**  
> Zakładając, że przestrzeń wektorowa $\mathbb{V}$ zawiera bazę będącą zbiorem skończonym, każda baza $\mathbb{V}$ jest zbiorem skończonym i wszystkie bazy mają tę samą liczbę wektorów.
{: .prompt-info }

Zatem liczba wektorów tworzących bazę $\mathbb{V}$ jest niezmienną, istotną własnością $\mathbb{V}$ i nazywa się ją **wymiarem (dimension)**.

> **Definicja wymiaru**  
> Przestrzeń wektorową, której baza jest zbiorem skończonym, nazywa się **skończenie wymiarową (finite dimension)**. Wtedy liczbę elementów bazy $n$ nazywa się **wymiarem (dimension)** danej przestrzeni wektorowej i oznacza $\dim(\mathbb{V})$. Przestrzeń wektorowa, która nie jest skończenie wymiarowa, jest **nieskończenie wymiarowa (infinite dimension)**.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> Wymiar przestrzeni wektorowej może zależeć od tego, nad jakim ciałem jest rozważana.
> - Nad ciałem liczb zespolonych $\mathbb{C}$ wymiar przestrzeni wektorowej liczb zespolonych wynosi $1$, a bazą jest $\\{1\\}$
> - Nad ciałem liczb rzeczywistych $\mathbb{R}$ wymiar przestrzeni wektorowej liczb zespolonych wynosi $2$, a bazą jest $\\{1,i\\}$
{: .prompt-tip }

W skończenie wymiarowej przestrzeni wektorowej $\mathbb{V}$ każdy podzbiór zawierający więcej wektorów niż $\dim(\mathbb{V})$ nie może być liniowo niezależny.

> **Wniosek 5-2 z twierdzenia o zastępowaniu**  
> Niech $\mathbb{V}$ będzie przestrzenią wektorową o wymiarze $n$.
> 1. Każdy skończony zbiór generujący $\mathbb{V}$ musi zawierać co najmniej $n$ wektorów, a zbiór generujący $\mathbb{V}$ składający się z $n$ wektorów jest bazą $\mathbb{V}$.
> 2. Podzbiór $\mathbb{V}$ złożony z $n$ wektorów, który jest liniowo niezależny, jest bazą $\mathbb{V}$.
> 3. Każdy liniowo niezależny podzbiór $\mathbb{V}$ można rozszerzyć do bazy. To znaczy, jeśli $L \subseteq \mathbb{V}$ jest liniowo niezależny, to istnieje baza $\beta$ przestrzeni $\mathbb{V}$ taka, że $\beta \supseteq L$.
{: .prompt-info }

### Wymiar podprzestrzeni

> **Twierdzenie 6**  
> Dla skończenie wymiarowej przestrzeni wektorowej $\mathbb{V}$ podprzestrzeń $\mathbb{W}$ jest skończenie wymiarowa oraz $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$. W szczególności, $\dim(\mathbb{W}) = \dim(\mathbb{V}) \quad \Rightarrow \quad \mathbb{V} = \mathbb{W}.$
>
> **Wniosek 6-1**  
> Dla podprzestrzeni $\mathbb{W}$ skończenie wymiarowej przestrzeni wektorowej $\mathbb{V}$ dowolną bazę $\mathbb{W}$ można rozszerzyć do bazy $\mathbb{V}$.
{: .prompt-info }

Z **Twierdzenia 6** wynika, że wymiar podprzestrzeni $\mathbb{R}^3$ może wynosić $0,1,2,3$.
- wymiar 0: przestrzeń punktowa $\\{\mathbf{0}\\}$ zawierająca wyłącznie początek układu współrzędnych ($\mathbf{0}$)
- wymiar 1: prosta przechodząca przez początek układu współrzędnych ($\mathbf{0}$)
- wymiar 2: płaszczyzna zawierająca początek układu współrzędnych ($\mathbf{0}$)
- wymiar 3: cała euklidesowa przestrzeń trójwymiarowa
