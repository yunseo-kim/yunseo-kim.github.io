---
title: "Vektorové prostory, podprostory a matice"
description: "Definice vektorových prostorů a podprostorů s příklady (F^n, prostor matic, prostor funkcí) a přehled symetrických, antisymetrických, trojúhelníkových a diagonálních matic."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations, Matrix]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **matice (matrix)**
>   - Prvek v $i$-tém řádku a $j$-tém sloupci matice $A$ značíme $A\_{ij}$ nebo $a\_{ij}$
>   - **diagonální prvek (diagonal entry)**: prvek $a\_{ij}$ pro $i=j$
>   - Prvky $a\_{i1}, a\_{i2}, \dots, a\_{in}$ nazýváme $i$-tý **řádek (row)** této matice
>     - Každý řádek matice lze vyjádřit jako vektor z $F^n$
>     - A navíc lze řádkový vektor z $F^n$ chápat jako další matici rozměru $1 \times n$
>   - Prvky $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ nazýváme $j$-tý **sloupec (column)** této matice
>     - Každý sloupec matice lze vyjádřit jako vektor z $F^m$
>     - A navíc lze sloupcový vektor z $F^m$ chápat jako další matici rozměru $m \times 1$
>   - **nulová matice (zero matrix)**: matice, jejíž všechny prvky jsou $0$, značí se $O$
>   - **čtvercová matice (square matrix)**: matice se stejným počtem řádků a sloupců
>   - Pro dvě matice $A, B$ typu $m \times n$ definujeme, že jsou **stejné** ($A=B$), pokud pro všechna $1 \leq i \leq m$, $1 \leq j \leq n$ platí $A\_{ij} = B_{ij}$ (tj. všechny odpovídající prvky se shodují)
>   - **transponovaná matice (transpose matrix)**: pro matici $A$ typu $m \times n$ je transpozice $A^T$ matice typu $n \times m$, která vznikne prohozením řádků a sloupců
>   - **symetrická matice (symmetric matrix)**: čtvercová matice $A$ splňující $A^T = A$
>   - **antisymetrická matice (skew-symmetric matrix)**: čtvercová matice $B$ splňující $B^T = -B$
>   - **trojúhelníková matice (triangular matrix)**
>     - **horní trojúhelníková matice (upper triangular matrix)**: všechny prvky pod diagonálou jsou $0$ (tj. $i>j \Rightarrow A\_{ij}=0$), obvykle se značí $U$
>     - **dolní trojúhelníková matice (lower triangular matrix)**: všechny prvky nad diagonálou jsou $0$ (tj. $i<j \Rightarrow A\_{ij}=0$), obvykle se značí $L$
>   - **diagonální matice (diagonal matrix)**: čtvercová matice, jejíž všechny nediagonální prvky jsou $0$ (tj. $i \neq j \Rightarrow M\_{ij}=0$ pro matici $n \times n$), obvykle se značí $D$
> - Typické vektorové prostory
>   - **$n$-tice $F^n$**:
>     - množina všech uspořádaných $n$-tic s prvky z tělesa $F$
>     - značí se $F^n$ a je to $F$-vektorový prostor
>   - **prostor matic (matrix space)**:
>     - množina všech matic typu $m \times n$ s prvky z tělesa $F$
>     - značí se $\mathcal{M}\_{m \times n}(F)$ a je to vektorový prostor
>   - **prostor funkcí (function space)**:
>     - pro neprázdnou množinu $S$ a těleso $F$ je to množina všech funkcí ze $S$ do $F$
>     - značí se $\mathcal{F}(S,F)$ a je to vektorový prostor
> - **podprostor (subspace)**
>   - Je-li $\mathbb{W}$ podmnožina $F$-vektorového prostoru $\mathbb{V}$ a zároveň je $F$-vektorovým prostorem se stejnými operacemi sčítání a násobení skalárem, jaké jsou definovány na $\mathbb{V}$, pak $\mathbb{W}$ nazýváme **podprostorem (subspace)** prostoru $\mathbb{V}$
>   - Pro každý vektorový prostor $\mathbb{V}$ jsou $\mathbb{V}$ samotný i $\\{0\\}$ podprostory; zejména $\\{0\\}$ se nazývá **nulový podprostor (zero subspace)**
>   - Pokud nějaká podmnožina vektorového prostoru obsahuje nulový vektor a je uzavřená na [lineární kombinace](/posts/vectors-and-linear-combinations/#lineární-kombinace-vektorů) (tj. $\mathrm{span}(\mathbb{W})=\mathbb{W}$), pak je to podprostor
{: .prompt-info }

## Prerequisites
- [Vektory a lineární kombinace](/posts/vectors-and-linear-combinations/)

## Vektorový prostor

Jak jsme krátce viděli i v článku [Vektory a lineární kombinace](/posts/vectors-and-linear-combinations/#vektor-v-širším-smyslu-prvek-vektorového-prostoru), definice vektoru a vektorového prostoru jako algebraické struktury je následující.

> **Definice**  
> **Vektorový prostor (vector space)** neboli **lineární prostor (linear space)** $\mathbb{V}$ nad tělesem $F$ je množina vybavená dvěma operacemi, **sčítáním** a **násobením skalárem**, které splňují následujících 8 podmínek. Prvky tělesa $F$ nazýváme **skaláry (scalar)** a prvky vektorového prostoru $\mathbb{V}$ nazýváme **vektory (vector)**.
>
> - **Součet (sum)**: pro dva prvky $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ je přiřazen jednoznačný prvek $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. Tomuto $\mathbf{x} + \mathbf{y}$ říkáme **součet** prvků $\mathbf{x}$ a $\mathbf{y}$.
> - **Násobení skalárem (scalar multiplication)**: každému prvku $a \in F$ a každému prvku $\mathbf{x} \in \mathbb{V}$ je přiřazen jednoznačný prvek $a\mathbf{x} \in \mathbb{V}$. Tomuto $a\mathbf{x}$ říkáme **skalární násobek (scalar multiple)** vektoru $\mathbf{x}$.
>
> 1. Pro všechna $\mathbf{x},\mathbf{y} \in \mathbb{V}$ platí $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$. (komutativita sčítání)
> 2. Pro všechna $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$ platí $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$. (asociativita sčítání)
> 3. Pro každé $\mathbf{x} \in \mathbb{V}$ existuje $\mathbf{0} \in \mathbb{V}$ takové, že $\mathbf{x} + \mathbf{0} = \mathbf{x}$. (nulový vektor, neutrální prvek pro sčítání)
> 4. Ke každému $\mathbf{x} \in \mathbb{V}$ existuje $\mathbf{y} \in \mathbb{V}$ takové, že $\mathbf{x}+\mathbf{y}=\mathbf{0}$. (inverzní prvek pro sčítání)
> 5. Pro každé $\mathbf{x} \in \mathbb{V}$ platí $1\mathbf{x} = \mathbf{x}$. (neutrální prvek pro násobení)
> 6. Pro všechna $a,b \in F$ a všechna $\mathbf{x} \in \mathbb{V}$ platí $(ab)\mathbf{x} = a(b\mathbf{x})$. (asociativita násobení skalárem)
> 7. Pro všechna $a \in F$ a všechna $\mathbf{x},\mathbf{y} \in \mathbb{V}$ platí $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$. (distributivita násobení skalárem vůči sčítání 1)
> 8. Pro všechna $a,b \in F$ a všechna $\mathbf{x},\mathbf{y} \in \mathbb{V}$ platí $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$. (distributivita násobení skalárem vůči sčítání 2)
{: .prompt-info }

Přesněji bychom měli psát „$F$-vektorový prostor $\mathbb{V}$“, ale při práci s vektorovými prostory obvykle těleso není zásadní a nehrozí-li záměna, těleso $F$ vynecháváme a píšeme jen „vektorový prostor $\mathbb{V}$“.

### Prostor matic

#### Řádkové a sloupcové vektory

Množinu všech uspořádaných $n$-tic s prvky z tělesa $F$ značíme $F^n$. Pro $u = (a_1, a_2, \dots, a_n) \in F^n$, $v = (b_1, b_2, \dots, b_n) \in F^n$ definujeme součet a násobení skalárem následovně; pak je $F^n$ $F$-vektorový prostor.

$$ \begin{align*}
u + v &= (a_1+b_1, a_2+b_2, \dots, a_n+b_n), \\
cu &= (ca_1, ca_2, \dots, ca_n)
\end{align*} $$

Vektor z $F^n$ se při samostatném zápisu obvykle vyjadřuje spíše jako **sloupcový vektor (column vector)** než jako **řádkový vektor (row vector)** $(a_1, a_2, \dots, a_n)$, tj.

$$\begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$$

> Protože zápis sloupcovým vektorem zabírá hodně místa, někdy se používá [transpozice](#transponovaná-matice-symetrická-matice-antisymetrická-matice) a zapisuje se $(a_1, a_2, \dots, a_n)^T$.
{: .prompt-tip }

#### Matice a prostor matic

Na druhé straně, $m \times n$ **matice (matrix)** s prvky z $F$ je obdélníkové uspořádání prvků následujícího tvaru; značí se kurzívními velkými písmeny ($A, B, C$ apod.).

$$ \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix} $$

- Prvek v $i$-tém řádku a $j$-tém sloupci matice $A$ značíme $A\_{ij}$ nebo $a\_{ij}$.
- Všechny $a\_{ij}$ ($1 \leq i \leq m$, $1 \leq j \leq n$) jsou prvky tělesa $F$.
- Prvek $a\_{ij}$ pro $i=j$ nazýváme **diagonální prvek (diagonal entry)**.
- Prvky $a\_{i1}, a\_{i2}, \dots, a\_{in}$ nazýváme $i$-tý **řádek (row)** této matice. Každý řádek matice lze vyjádřit jako vektor z $F^n$, a navíc lze řádkový vektor z $F^n$ vyjádřit jako další matici rozměru $1 \times n$.
- Prvky $a\_{1j}, a\_{2j}, \dots, a\_{mj}$ nazýváme $j$-tý **sloupec (column)** této matice. Každý sloupec matice lze vyjádřit jako vektor z $F^m$, a navíc lze sloupcový vektor z $F^m$ vyjádřit jako další matici rozměru $m \times 1$.
- Matici typu $m \times n$, jejíž všechny prvky jsou $0$, nazýváme **nulová matice (zero matrix)** a značíme ji $O$.
- Matici se stejným počtem řádků a sloupců nazýváme **čtvercová matice (square matrix)**.
- Pro dvě matice $A, B$ typu $m \times n$ definujeme, že jsou **stejné** ($A=B$), pokud pro všechna $1 \leq i \leq m$, $1 \leq j \leq n$ platí $A\_{ij} = B_{ij}$ (tj. všechny odpovídající prvky se shodují).

Množinu všech matic typu $m \times n$ s prvky z tělesa $F$ značíme $\mathcal{M}\_{m \times n}(F)$. Pro $\mathbf{A},\mathbf{B} \in \mathcal{M}\_{m \times n}(F)$ a $c \in F$ definujeme součet a násobení skalárem takto; pak je $\mathcal{M}\_{m \times n}(F)$ vektorový prostor a nazývá se **prostor matic (matrix space)**.

$$ \begin{align*}
(\mathbf{A}+\mathbf{B})_{ij} &= \mathbf{A}_{ij} + \mathbf{B}_{ij}, \\
(c\mathbf{A})_{ij} &= c\mathbf{A}_{ij} \\
\text{(kde }1 \leq i \leq &m, 1 \leq j \leq n \text{)}
\end{align*} $$

Jde o přirozené rozšíření operací definovaných na $F^n$ a $F^m$.

### Prostor funkcí

Pro neprázdnou množinu $S$ a těleso $F$ je $\mathcal{F}(S,F)$ množina všech funkcí ze $S$ do $F$. Řekneme, že dvě funkce $f, g$ jsou **stejné** ($f=g$), pokud pro všechna $s \in S$ platí $f(s) = g(s)$.

Pro $f,g \in \mathcal{F}(S,F)$, $c \in F$, $s \in S$ definujeme součet a násobení skalárem následovně; pak je $\mathcal{F}(S,F)$ vektorový prostor a nazývá se **prostor funkcí (function space)**.

$$ \begin{align*}
(f + g)(s) &= f(s) + g(s), \\
(cf)(s) &= c[f(s)]
\end{align*} $$

## Podprostor

> **Definice**  
> Je-li $\mathbb{W}$ podmnožina $F$-vektorového prostoru $\mathbb{V}$ a zároveň je $F$-vektorovým prostorem se stejnými operacemi sčítání a násobení skalárem, jaké jsou definovány na $\mathbb{V}$, pak $\mathbb{W}$ nazýváme **podprostorem (subspace)** prostoru $\mathbb{V}$.
{: .prompt-info }

Pro každý vektorový prostor $\mathbb{V}$ jsou $\mathbb{V}$ samotný i $\\{0\\}$ podprostory; zejména $\\{0\\}$ se nazývá **nulový podprostor (zero subspace)**.

Zda je daná podmnožina podprostorem, lze ověřit pomocí následující věty.

> **Věta 1**  
> Pro vektorový prostor $\mathbb{V}$ a jeho podmnožinu $\mathbb{W}$ je nutná a postačující podmínka pro to, aby $\mathbb{W}$ byla podprostorem $\mathbb{V}$, splnění následujících tří podmínek. Operace jsou stejné jako ty, které jsou definovány na $\mathbb{V}$.
> 1. $\mathbf{0} \in \mathbb{W}$
> 2. $\mathbf{x}+\mathbf{y} \in \mathbb{W} \quad \forall\ \mathbf{x} \in \mathbb{W},\ \mathbf{y} \in \mathbb{W}$
> 3. $c\mathbf{x} \in \mathbb{W} \quad \forall\ c \in F,\ \mathbf{x} \in \mathbb{W}$
>
> Stručně: pokud množina obsahuje nulový vektor a je uzavřená na [lineární kombinace](/posts/vectors-and-linear-combinations/#lineární-kombinace-vektorů) (tj. $\mathrm{span}(\mathbb{W})=\mathbb{W}$), pak je to podprostor.
{: .prompt-info }

Dále platí následující tvrzení.

> **Věta 2**  
> - Generovaný podprostor $\mathrm{span}(S)$ libovolné podmnožiny $S$ vektorového prostoru $\mathbb{V}$ je podprostor $\mathbb{V}$, který obsahuje $S$.
>
>   $$ S \subset \mathrm{span}(S) \leq \mathbb{V} \quad \forall\ S \subset \mathbb{V}. $$
>
> - Každý podprostor $\mathbb{V}$, který obsahuje $S$, musí nutně obsahovat i generovaný podprostor $S$.
>
>   $$ \mathbb{W}\supset \mathrm{span}(S) \quad \forall\ S \subset \mathbb{W} \leq \mathbb{V}. $$
>
{: .prompt-info }

> **Věta 3**  
> Pro podprostory vektorového prostoru $\mathbb{V}$ platí, že libovolný průnik těchto podprostorů je opět podprostorem $\mathbb{V}$.
{: .prompt-info }

### Transponovaná matice, symetrická matice, antisymetrická matice

Pro matici $A$ typu $m \times n$ je její **transponovaná matice (transpose matrix)** $A^T$ matice typu $n \times m$, která vznikne prohozením řádků a sloupců matice $A$.

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

Matici $A$ splňující $A^T = A$ nazýváme **symetrická matice (symmetric matrix)** a matici $B$ splňující $B^T = -B$ nazýváme **antisymetrická matice (skew-symmetric matrix)**. Symetrická i antisymetrická matice musí být nutně čtvercové.

Dvě množiny $\mathbb{W}\_1, \mathbb{W}\_2$ tvořené všemi symetrickými, resp. antisymetrickými maticemi z $\mathcal{M}\_{n \times n}(F)$ jsou podprostory $\mathcal{M}\_{n \times n}(F)$. Jinými slovy, $\mathbb{W}\_1, \mathbb{W}\_2$ jsou uzavřené na součet a násobení skalárem.

### Trojúhelníkové matice, diagonální matice

Tyto dva typy matic jsou také zvlášť důležité.

Nejprve sjednotíme následující dva typy matic pod označení **trojúhelníková matice (triangular matrix)**.
- **horní trojúhelníková matice (upper triangular matrix)**: všechny prvky pod diagonálou jsou $0$ (tj. $i>j \Rightarrow A\_{ij}=0$), obvykle se značí $U$
- **dolní trojúhelníková matice (lower triangular matrix)**: všechny prvky nad diagonálou jsou $0$ (tj. $i<j \Rightarrow A\_{ij}=0$), obvykle se značí $L$

Čtvercovou matici, jejíž všechny nediagonální prvky jsou $0$, tj. matici $n \times n$ splňující $i \neq j \Rightarrow M\_{ij}=0$, nazýváme **diagonální matice (diagonal matrix)** a obvykle ji značíme $D$. Diagonální matice je současně horní i dolní trojúhelníková matice.

Množina horních trojúhelníkových matic, množina dolních trojúhelníkových matic i množina diagonálních matic jsou všechny podprostory $\mathcal{M}\_{m \times n}(F)$.
