---
title: "Przestrzenie wektorowe, podprzestrzenie i macierze"
description: "Omawiamy definicje przestrzeni wektorowej i podprzestrzeni oraz typowe przykłady: $F^n$, przestrzenie macierzy i funkcji. Skupiamy się na przestrzeniach macierzy i ważnych podprzestrzeniach: macierzach symetrycznych/antysymetrycznych oraz trójkątnych i diagonalnych."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **macierz (matrix)**
>   - element w $i$-tym wierszu i $j$-tej kolumnie macierzy $A$ zapisujemy jako $A\_{ij}$ lub $a\_{ij}$
>   - **element diagonalny (diagonal entry)**: element $a\_{ij}$ taki, że $i=j$
>   - elementy $a\_{i1}, a\_{i2}, \dots, a\_{in}$ nazywamy $i$-tym **wierszem (row)** tej macierzy
>     - każdy wiersz macierzy można przedstawić jako wektor z $F^n$
>     - ponadto, wektor wierszowy z $F^n$ można przedstawić jako inną macierz rozmiaru $1 \times n$
>   - elementy $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ nazywamy $j$-tą **kolumną (column)** tej macierzy
>     - każdą kolumnę macierzy można przedstawić jako wektor z $F^m$
>     - ponadto, wektor kolumnowy z $F^m$ można przedstawić jako inną macierz rozmiaru $m \times 1$
>   - **macierz zerowa (zero matrix)**: macierz, której wszystkie elementy są równe $0$; oznaczamy ją przez $O$
>   - **macierz kwadratowa (square matrix)**: macierz, w której liczba wierszy jest równa liczbie kolumn
>   - dla dwóch macierzy $m \times n$ $A, B$: jeśli dla wszystkich $1 \leq i \leq m$, $1 \leq j \leq n$ zachodzi $A\_{ij} = B_{ij}$ (tj. wszystkie odpowiadające sobie elementy są identyczne), to definiujemy, że macierze są **równe** ($A=B$)
>   - **macierz transponowana (transpose matrix)**: dla macierzy $m \times n$ $A$ macierzą transponowaną nazywamy macierz $A^T$ rozmiaru $n \times m$, otrzymaną przez zamianę wierszy z kolumnami
>   - **macierz symetryczna (symmetric matrix)**: macierz kwadratowa $A$ taka, że $A^T = A$
>   - **macierz antysymetryczna (skew-symmetric matrix)**: macierz kwadratowa $B$ taka, że $B^T = -B$
>   - **macierz trójkątna (triangular matrix)**
>     - **macierz górnotrójkątna (upper triangular matrix)**: macierz, w której wszystkie elementy pod przekątną są równe $0$ (tj. $i>j \Rightarrow A\_{ij}=0$); zwykle oznaczana przez $U$
>     - **macierz dolnotrójkątna (lower triangular matrix)**: macierz, w której wszystkie elementy nad przekątną są równe $0$ (tj. $i<j \Rightarrow A\_{ij}=0$); zwykle oznaczana przez $L$
>   - **macierz diagonalna (diagonal matrix)**: macierz kwadratowa, w której wszystkie elementy poza przekątną są równe $0$ (tj. $i \neq j \Rightarrow M\_{ij}=0$ dla macierzy $n \times n$); zwykle oznaczana przez $D$
> - reprezentatywne przestrzenie wektorowe
>   - **$n$-tki $F^n$**:
>     - zbiór wszystkich $n$-tek, których składowe należą do ciała $F$
>     - oznaczamy przez $F^n$; jest to przestrzeń wektorowa nad $F$
>   - **przestrzeń macierzy (matrix space)**:
>     - zbiór wszystkich macierzy $m \times n$, których elementy należą do ciała $F$
>     - oznaczamy przez $\mathcal{M}\_{m \times n}(F)$; jest to przestrzeń wektorowa
>   - **przestrzeń funkcji (function space)**:
>     - dla niepustego zbioru $S$ oraz ciała $F$: zbiór wszystkich funkcji z $S$ do $F$
>     - oznaczamy przez $\mathcal{F}(S,F)$; jest to przestrzeń wektorowa
> - **podprzestrzeń (subspace)**
>   - jeśli podzbiór $\mathbb{W}$ przestrzeni wektorowej nad $F$, $\mathbb{V}$, jest przestrzenią wektorową nad $F$ z tym samym dodawaniem i mnożeniem przez skalar co w $\mathbb{V}$, to $\mathbb{W}$ nazywamy **podprzestrzenią (subspace)** $\mathbb{V}$
>   - dla każdej przestrzeni wektorowej $\mathbb{V}$: sama $\mathbb{V}$ oraz $\\{0\\}$ są podprzestrzeniami; w szczególności $\\{0\\}$ nazywamy **podprzestrzenią zerową (zero subspace)**
>   - jeśli pewien podzbiór przestrzeni wektorowej zawiera wektor zerowy i jest domknięty na [kombinacje liniowe](/posts/vectors-and-linear-combinations/#kombinacje-liniowe-wektorow) (tj. $\mathrm{span}(\mathbb{W})=\mathbb{W}$), to jest on podprzestrzenią
{: .prompt-info }

## Prerequisites
- [Wektory i kombinacje liniowe](/posts/vectors-and-linear-combinations/)

## Przestrzeń wektorowa

Jak krótko widzieliśmy już w tekście [Wektory i kombinacje liniowe](/posts/vectors-and-linear-combinations/#wektor-w-szerokim-sensie-element-przestrzeni-wektorowej), definicje wektora i przestrzeni wektorowej jako struktury algebraicznej są następujące.

> **Definicja**  
> **Przestrzeń wektorowa (vector space)** lub **przestrzeń liniowa (linear space)** $\mathbb{V}$ nad ciałem $F$ jest zbiorem wyposażonym w dwa działania, **dodawanie** oraz **mnożenie przez skalar**, spełniające poniższe 8 warunków. Elementy ciała $F$ nazywamy **skalarami (scalar)**, a elementy przestrzeni $\mathbb{V}$ — **wektorami (vector)**.
>
> - **Suma (sum)**: dla dwóch elementów $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ jest to działanie przyporządkowujące jednoznacznie element $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. Element $\mathbf{x} + \mathbf{y}$ nazywamy **sumą** $\mathbf{x}$ i $\mathbf{y}$.
> - **Mnożenie przez skalar (scalar multiplication)**: dla elementu $a \in F$ i elementu $\mathbf{x} \in \mathbb{V}$ jest to działanie przyporządkowujące jednoznacznie element $a\mathbf{x} \in \mathbb{V}$. Element $a\mathbf{x}$ nazywamy **wielokrotnością skalarną (scalar multiple)** wektora $\mathbf{x}$.
>
> 1. Dla wszystkich $\mathbf{x},\mathbf{y} \in \mathbb{V}$ zachodzi $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (przemienność dodawania)
> 2. Dla wszystkich $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$ zachodzi $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (łączność dodawania)
> 3. Dla każdego $\mathbf{x} \in \mathbb{V}$ istnieje $\mathbf{0} \in \mathbb{V}$ takie, że $\mathbf{x} + \mathbf{0} = \mathbf{x}$. (wektor zerowy, element neutralny dodawania)
> 4. Dla każdego $\mathbf{x} \in \mathbb{V}$ istnieje $\mathbf{y} \in \mathbb{V}$ takie, że $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (element przeciwny względem dodawania)
> 5. Dla każdego $\mathbf{x} \in \mathbb{V}$ zachodzi $1\mathbf{x} = \mathbf{x}$. (element neutralny mnożenia)
> 6. Dla wszystkich $a,b \in F$ oraz wszystkich $\mathbf{x} \in \mathbb{V}$ zachodzi $(ab)\mathbf{x} = a(b\mathbf{x})$. (łączność mnożenia przez skalar)
> 7. Dla wszystkich $a \in F$ oraz wszystkich $\mathbf{x},\mathbf{y} \in \mathbb{V}$ zachodzi $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (rozdzielność 1 mnożenia przez skalar względem dodawania)
> 8. Dla wszystkich $a,b \in F$ oraz wszystkich $\mathbf{x},\mathbf{y} \in \mathbb{V}$ zachodzi $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (rozdzielność 2 mnożenia przez skalar względem dodawania)
{: .prompt-info }

Ściśle mówiąc, należy pisać „przestrzeń wektorowa $\mathbb{V}$ nad $F$”, jednak przy omawianiu przestrzeni wektorowych ciało zwykle nie jest kluczowym elementem, więc jeśli nie ma ryzyka nieporozumienia, pomijamy ciało $F$ i piszemy po prostu „przestrzeń wektorowa $\mathbb{V}$”.

### Przestrzeń macierzy

#### Wektory wierszowe i wektory kolumnowe

Zbiór wszystkich $n$-tek o elementach z ciała $F$ oznaczamy przez $F^n$. Dla $u = (a_1, a_2, \dots, a_n) \in F^n$, $v = (b_1, b_2, \dots, b_n) \in F^n$ definiujemy dodawanie i mnożenie przez skalar następująco; wtedy $F^n$ jest przestrzenią wektorową nad $F$.

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

Wektory z $F^n$ zapisuje się zwykle nie jako **wektory wierszowe (row vector)** $(a_1, a_2, \dots, a_n)$, lecz jako **wektory kolumnowe (column vector)**

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

.

> Ponieważ taki zapis kolumnowy zajmuje dużo miejsca, czasem stosuje się [transpozycję](#macierz-transponowana-macierz-symetryczna-macierz-antysymetryczna) i zapisuje jako $(a_1, a_2, \dots, a_n)^T$.
{: .prompt-tip }

#### Macierze i przestrzeń macierzy

Z kolei macierz $m \times n$ o elementach z ciała $F$ to prostokątna tablica postaci poniżej; zapisujemy ją kursywą wielką literą ($A, B, C$ itd.).

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- element w $i$-tym wierszu i $j$-tej kolumnie macierzy $A$ zapisujemy jako $A\_{ij}$ lub $a\_{ij}$.
- wszystkie $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) są elementami $F$.
- element $a\_{ij}$ taki, że $i=j$, nazywamy **elementem diagonalnym (diagonal entry)** tej macierzy.
- elementy $a\_{i1}, a\_{i2}, \dots, a\_{in}$ nazywamy $i$-tym **wierszem (row)** tej macierzy. Każdy wiersz macierzy można przedstawić jako wektor z $F^n$; ponadto wektor wierszowy z $F^n$ można przedstawić jako inną macierz rozmiaru $1 \times n$.
- elementy $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ nazywamy $j$-tą **kolumną (column)** tej macierzy. Każdą kolumnę macierzy można przedstawić jako wektor z $F^m$; ponadto wektor kolumnowy z $F^m$ można przedstawić jako inną macierz rozmiaru $m \times 1$.
- macierz $m \times n$, której wszystkie elementy są równe $0$, nazywamy **macierzą zerową (zero matrix)** i oznaczamy przez $O$.
- macierz, w której liczba wierszy jest równa liczbie kolumn, nazywamy **macierzą kwadratową (square matrix)**.
- dla dwóch macierzy $m \times n$ $A, B$: jeśli dla wszystkich $1 \leq i \leq m$, $1 \leq j \leq n$ zachodzi $A\_{ij} = B_{ij}$ (tj. wszystkie odpowiadające sobie elementy są identyczne), to definiujemy, że macierze są **równe** ($A=B$).

Zbiór wszystkich macierzy $m \times n$ o elementach z ciała $F$ oznaczamy przez $\mathcal{M}\_{m \times n}(F)$. Dla $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F)$ oraz $c \in F$, jeśli dodawanie i mnożenie przez skalar zdefiniujemy następująco, to $\mathcal{M}\_{m \times n}(F)$ jest przestrzenią wektorową; nazywamy ją **przestrzenią macierzy (matrix space)**.

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(przy czym }1 \leq i \leq &m, 1 \leq j \leq n \text{)}
\end{align*} $$

Jest to naturalne rozszerzenie działań zdefiniowanych w $F^n$ oraz $F^m$.

### Przestrzeń funkcji

Dla niepustego zbioru $S$ oraz ciała $F$, $\mathcal{F}(S,F)$ jest zbiorem wszystkich funkcji z $S$ do $F$. W $\mathcal{F}(S,F)$, jeśli dla każdego $s \in S$ zachodzi $f(s) = g(s)$, to mówimy, że funkcje $f, g$ są **równe** ($f=g$).

Dla $f,g \in \mathcal{F}(S,F)$, $c \in F$, $s \in S$ definiujemy dodawanie i mnożenie przez skalar następująco; wtedy $\mathcal{F}(S,F)$ jest przestrzenią wektorową i nazywamy ją **przestrzenią funkcji (function space)**.

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## Podprzestrzeń

> **Definicja**  
> Jeśli podzbiór $\mathbb{W}$ przestrzeni wektorowej nad $F$, $\mathbb{V}$, jest przestrzenią wektorową nad $F$ z tym samym dodawaniem i mnożeniem przez skalar co w $\mathbb{V}$, to $\mathbb{W}$ nazywamy **podprzestrzenią (subspace)** $\mathbb{V}$.
{: .prompt-info }

Dla każdej przestrzeni wektorowej $\mathbb{V}$: sama $\mathbb{V}$ oraz $\\{0\\}$ są podprzestrzeniami; w szczególności $\\{0\\}$ nazywamy **podprzestrzenią zerową (zero subspace)**.

To, czy dany podzbiór jest podprzestrzenią, można sprawdzić za pomocą następującego twierdzenia.

> **Twierdzenie 1**  
> Dla przestrzeni wektorowej $\mathbb{V}$ i jej podzbioru $\mathbb{W}$ warunkiem koniecznym i wystarczającym na to, by $\mathbb{W}$ była podprzestrzenią $\mathbb{V}$, jest spełnienie poniższych 3 warunków. Działania są takie same jak te zdefiniowane w $\mathbb{V}$.
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> Krótko mówiąc: jeśli zbiór zawiera wektor zerowy i jest domknięty na [kombinacje liniowe](/posts/vectors-and-linear-combinations/#kombinacje-liniowe-wektorow) (tj. $\mathrm{span}(\mathbb{W})=\mathbb{W}$), to jest podprzestrzenią.
{: .prompt-info }

Ponadto zachodzą następujące twierdzenia.

> **Twierdzenie 2**  
> - Rozpiętość $\mathrm{span}(S)$ dowolnego podzbioru $S$ przestrzeni wektorowej $\mathbb{V}$ jest podprzestrzenią $\mathbb{V}$ zawierającą $S$.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - Każda podprzestrzeń $\mathbb{V}$ zawierająca $S$ musi zawierać rozpiętość $S$.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **Twierdzenie 3**  
> Dla dowolnej rodziny podprzestrzeni przestrzeni wektorowej $\mathbb{V}$ ich dowolne przecięcie jest również podprzestrzenią $\mathbb{V}$.
{: .prompt-info }

### Macierz transponowana, macierz symetryczna, macierz antysymetryczna

Dla macierzy $m \times n$ $A$ jej **macierz transponowana (transpose matrix)** $A^T$ jest macierzą $n \times m$ otrzymaną przez zamianę wierszy z kolumnami.

$$ (A^T)_{ij} = A_{ji} $$

$$ \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}^T
= \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 
\end{pmatrix} $$

Macierz $A$ spełniającą $A^T = A$ nazywamy **macierzą symetryczną (symmetric matrix)**, a macierz $B$ spełniającą $B^T = -B$ — **macierzą antysymetryczną (skew-symmetric matrix)**. Macierze symetryczne i antysymetryczne muszą być macierzami kwadratowymi.

Dwa zbiory $\mathbb{W}\_1, \mathbb{W}\_2$, których elementami są odpowiednio wszystkie macierze symetryczne oraz wszystkie macierze antysymetryczne z $\mathcal{M}\_{n \times n}(F)$, są podprzestrzeniami $\mathcal{M}\_{n \times n}(F)$. To znaczy: $\mathbb{W}\_1, \mathbb{W}\_2$ są domknięte względem dodawania i mnożenia przez skalar.

### Macierze trójkątne, macierze diagonalne

Te dwa typy macierzy są również szczególnie ważne.

Najpierw następujące dwa typy macierzy łącznie nazywamy **macierzami trójkątnymi (triangular matrix)**.
- **macierz górnotrójkątna (upper triangular matrix)**: macierz, w której wszystkie elementy pod przekątną są równe $0$ (tj. $i>j \Rightarrow A\_{ij}=0$); zwykle oznaczana przez $U$
- **macierz dolnotrójkątna (lower triangular matrix)**: macierz, w której wszystkie elementy nad przekątną są równe $0$ (tj. $i<j \Rightarrow A\_{ij}=0$); zwykle oznaczana przez $L$

Macierz kwadratową, w której wszystkie elementy poza przekątną są równe $0$, tzn. macierz $n \times n$ spełniającą $i \neq j \Rightarrow M\_{ij}=0$, nazywamy **macierzą diagonalną (diagonal matrix)** i zwykle oznaczamy przez $D$. Macierz diagonalna jest jednocześnie macierzą górnotrójkątną i dolnotrójkątną.

Zbiór macierzy górnotrójkątnych, zbiór macierzy dolnotrójkątnych oraz zbiór macierzy diagonalnych są podprzestrzeniami $\mathcal{M}\_{m \times n}(F)$.
