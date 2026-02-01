---
title: "Lineární závislost a lineární nezávislost, báze a dimenze"
description: "Shrnutí pojmů lineární závislosti a nezávislosti a definice báze a dimenze vektorového prostoru."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Předpoklady
- [Vektory a lineární kombinace](/posts/vectors-and-linear-combinations/)
- [Vektorové prostory, podprostory a matice](/posts/vector-spaces-subspaces-and-matrices/)

## Lineární závislost a lineární nezávislost

Uvažujme nějaký [vektorový prostor](/posts/vector-spaces-subspaces-and-matrices/#vektorovy-prostor) $\mathbb{V}$ a [podprostor](/posts/vector-spaces-subspaces-and-matrices/#podprostor) $\mathbb{W}$. Řekněme, že chceme najít co nejmenší konečnou podmnožinu $S$, která $\mathbb{W}$ [generuje](/posts/vectors-and-linear-combinations/#generovani-span-linearni-kombinace-cmathbfv--dmathbfw).

Je-li pro množinu $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ splněno $\mathrm{span}(S) = \mathbb{W}$, jak rozhodnout, zda neexistuje vlastní podmnožina $S$, která stále generuje $\mathbb{W}$? Je to totéž jako rozhodnout, zda lze některý vektor vybraný ze $S$ vyjádřit jako [lineární kombinaci](/posts/vectors-and-linear-combinations/#linearni-kombinace-vektoru) ostatních vektorů. Například nutná a postačující podmínka pro vyjádření $\mathbf{u}_4$ jako lineární kombinace zbývajících tří vektorů je existence skalárů $a_1, a_2, a_3$, které splňují

$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

Protože je ale nepohodlné pokaždé pro $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ sestavovat soustavu lineárních rovnic a zjišťovat, zda má řešení, trochu výraz upravme:

$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

Pokud je některý vektor z $S$ lineární kombinací ostatních, pak při vyjádření nulového vektoru jako lineární kombinace vektorů z $S$ existuje takové vyjádření, v němž je alespoň jeden z koeficientů $a_1, a_2, a_3, a_4$ nenulový. Obrácené tvrzení je rovněž pravdivé: existuje-li vyjádření nulového vektoru jako lineární kombinace prvků $S$ s tím, že alespoň jeden z koeficientů $a_1, a_2, a_3, a_4$ je nenulový, pak je některý vektor z $S$ lineární kombinací ostatních.

Zobecněním toho definujeme **lineární závislost** a **lineární nezávislost** následovně.

> **Definice**  
> Pro podmnožinu $S$ vektorového prostoru $\mathbb{V}$ říkáme, že množina $S$ (a její vektory) je **lineárně závislá (linearly dependent)**, existují-li konečně mnohé navzájem různé vektory $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ a skaláry $a_1, a_2, \dots, a_n$, z nichž alespoň jeden je nenulový, takové, že $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$. V opačném případě je **lineárně nezávislá (linearly independent)**.
{: .prompt-info }

Pro libovolné vektory $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ platí, že když $a_1 = a_2 = \cdots = a_n = 0$, pak $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$; tomu se říká **triviální vyjádření nulového vektoru (trivial representation of $\mathbf{0}$)**.

Následující tři tvrzení o lineárně nezávislých množinách platí ve všech vektorových prostorech vždy. Zejména **tvrzení 3** je, jak jsme viděli, velmi užitečné při rozhodování, zda je nějaká konečná množina lineárně nezávislá.

> - **Tvrzení 1**: Prázdná množina je lineárně nezávislá. Aby byla množina lineárně závislá, nesmí být prázdná.
> - **Tvrzení 2**: Množina tvořená jediným nenulovým vektorem je lineárně nezávislá.
> - **Tvrzení 3**: Nutnou a postačující podmínkou, aby byla množina lineárně nezávislá, je, že jediným způsobem, jak vyjádřit $\mathbf{0}$ jako lineární kombinaci dané množiny, je triviální vyjádření.
{: .prompt-info }

Důležité jsou také následující věty.

> **Věta 1**  
> Nechť $\mathbb{V}$ je vektorový prostor a $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Je-li $S_1$ lineárně závislá, pak je lineárně závislá i $S_2$.
>
> **Důsledek 1-1**  
> Nechť $\mathbb{V}$ je vektorový prostor a $S_1 \subseteq S_2 \subseteq \mathbb{V}$. Je-li $S_2$ lineárně nezávislá, pak je lineárně nezávislá i $S_1$.
{: .prompt-info }

> **Věta 2**  
> Uvažujme vektorový prostor $\mathbb{V}$ a lineárně nezávislou podmnožinu $S$. Pro vektor $\mathbf{v} \in \mathbb{V}$, který nepatří do $S$, je nutná a postačující podmínka pro to, aby $S \cup \\{\mathbf{v}\\}$ byla lineárně závislá, že $\mathbf{v} \in \mathrm{span}(S)$.
>
> Jinými slovy: **pokud žádná vlastní podmnožina $S$ nedokáže generovat stejný prostor jako $S$, pak je $S$ lineárně nezávislá.**
{: .prompt-info }

## Báze a dimenze

### Báze

Generující množina $S$ pro $\mathbb{W}$, která je [lineárně nezávislá](#linearni-zavislost-a-linearni-nezavislost), má zvláštní vlastnost: každý vektor z $\mathbb{W}$ lze nutně vyjádřit jako lineární kombinaci prvků $S$ a toto vyjádření je jediné (**Věta 3**). Proto se lineárně nezávislá generující množina pro nějaký vektorový prostor speciálně definuje jako **báze (basis)**.

> **Definice báze**  
> Nechť $\mathbb{V}$ je vektorový prostor a $\beta$ je jeho podmnožina. Pokud je $\beta$ lineárně nezávislá a generuje $\mathbb{V}$, pak se $\beta$ nazývá **báze (basis)** prostoru $\mathbb{V}$. Říkáme také, že vektory v $\beta$ tvoří bázi prostoru $\mathbb{V}$.
{: .prompt-info }

> $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ a $\emptyset$ je lineárně nezávislá. Proto je $\emptyset$ bází bodového prostoru.
{: .prompt-tip }

Zejména následující speciální báze pro $F^n$ se nazývá **standardní báze (standard basis)** prostoru $F^n$.

> **Definice standardní báze**  
> Pro vektorový prostor $F^n$ uvažujme následující vektory.
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> Pak množina $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ je bází $F^n$ a nazývá se **standardní báze (standard basis)** prostoru $F^n$.
{: .prompt-info }

> **Věta 3**  
> Nechť $\mathbb{V}$ je vektorový prostor a $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$ jsou navzájem různé vektory. Nutnou a postačující podmínkou, aby množina $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ byla bází $\mathbb{V}$, je: „libovolný vektor $\mathbf{v} \in \mathbb{V}$ lze vyjádřit jako lineární kombinaci vektorů z $\beta$ a toto vyjádření je jediné“. Tj. pro jediné skalární $n$-tice $(a_1, a_2, \dots, a_n)$ musí platit
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

Podle **Věty 3**, pokud $n$ navzájem různých vektorů $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ tvoří bázi vektorového prostoru $\mathbb{V}$, pak uvnitř tohoto prostoru je pro daný vektor $\mathbf{v}$ určena odpovídající skalární $n$-tice $(a_1, a_2, \dots, a_n)$ a naopak, je-li dána skalární $n$-tice, lze získat odpovídající vektor $\mathbf{v}$. Později to znovu shrnu při studiu **invertibility** a **izomorfismů**, ale v tomto případě jsou vektorové prostory $\mathbb{V}$ a $F^n$ <u>v podstatě totéž</u>.

> **Věta 4**  
> Je-li pro konečnou množinu $S$ splněno $\mathrm{span}(S) = \mathbb{V}$, pak existuje podmnožina $S$, která je bází $\mathbb{V}$. Tedy v tomto případě je báze $\mathbb{V}$ konečná.
{: .prompt-info }

> Velká část vektorových prostorů spadá pod **Větu 4**, ale ne nutně všechny. <u>Báze nemusí být konečná množina</u>.
{: .prompt-tip }

### Dimenze

> **Věta 5: věta o nahrazení (replacement theorem)**  
> Nechť $G$ je množina $n$ vektorů taková, že $\mathrm{span}(G) = \mathbb{V}$. Pokud je $L$ podmnožina $\mathbb{V}$ tvořená $m$ lineárně nezávislými vektory, pak $m\leq n$. Dále existuje množina $H \subseteq G$ s $n-m$ prvky taková, že $\mathrm{span}(L \cup H) = \mathbb{V}$.
{: .prompt-info }

Z toho získáme dvě velmi důležitá důsledková tvrzení.

> **Důsledek 5-1 věty o nahrazení**  
> Předpokládejme, že vektorový prostor $\mathbb{V}$ obsahuje konečnou bázi. Pak každá báze $\mathbb{V}$ je konečná a všechny báze mají stejný počet vektorů.
{: .prompt-info }

Podle toho je počet vektorů tvořících bázi $\mathbb{V}$ neměnnou, podstatnou vlastností prostoru $\mathbb{V}$; této vlastnosti se říká **dimenze (dimension)**.

> **Definice dimenze**  
> Vektorový prostor, který má konečnou bázi, se nazývá **konečněrozměrný (finite-dimensional)**. V tomto případě se počet prvků báze $n$ nazývá **dimenze (dimension)** daného vektorového prostoru a značí se $\dim(\mathbb{V})$. Vektorový prostor, který není konečněrozměrný, je **nekonečněrozměrný (infinite-dimensional)**.
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> Dimenze vektorového prostoru se může lišit podle toho, nad jakým tělesem je uvažován.
> - Nad tělesem komplexních čísel $\mathbb{C}$ má komplexní vektorový prostor dimenzi $1$ a bázi $\\{1\\}$.
> - Nad tělesem reálných čísel $\mathbb{R}$ má komplexní vektorový prostor dimenzi $2$ a bázi $\\{1,i\\}$.
{: .prompt-tip }

V konečněrozměrném vektorovém prostoru $\mathbb{V}$ nemůže být žádná podmnožina s více než $\dim(\mathbb{V})$ vektory lineárně nezávislá.

> **Důsledek 5-2 věty o nahrazení**  
> Nechť $\mathbb{V}$ je vektorový prostor dimenze $n$.
> 1. Každá konečná generující množina $\mathbb{V}$ musí obsahovat alespoň $n$ vektorů a generující množina $\mathbb{V}$ tvořená $n$ vektory je bází $\mathbb{V}$.
> 2. Lineárně nezávislá podmnožina $\mathbb{V}$ tvořená $n$ vektory je bází $\mathbb{V}$.
> 3. Každou lineárně nezávislou podmnožinu $\mathbb{V}$ lze rozšířit na bázi. Tj. je-li $L \subseteq \mathbb{V}$ lineárně nezávislá, pak existuje báze $\beta$ prostoru $\mathbb{V}$ taková, že $\beta \supseteq L$.
{: .prompt-info }

### Dimenze podprostoru

> **Věta 6**  
> Pro konečněrozměrný vektorový prostor $\mathbb{V}$ je každý jeho podprostor $\mathbb{W}$ konečněrozměrný a platí $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$. Zejména
>
> $$ \dim(\mathbb{W}) = \dim(\mathbb{V}) \quad \Rightarrow \quad \mathbb{V} = \mathbb{W}.$$
>
> **Důsledek 6-1**  
> Pro podprostor $\mathbb{W}$ konečněrozměrného vektorového prostoru $\mathbb{V}$ lze libovolnou bázi $\mathbb{W}$ rozšířit na bázi $\mathbb{V}$.
{: .prompt-info }

Podle **Věty 6** může mít podprostor $\mathbb{R}^3$ dimenzi $0,1,2,3$.
- 0 rozměrů: bodový prostor $\\{\mathbf{0}\\}$ obsahující pouze počátek ($\mathbf{0}$)
- 1 rozměr: přímka procházející počátkem ($\mathbf{0}$)
- 2 rozměry: rovina obsahující počátek ($\mathbf{0}$)
- 3 rozměry: celý eukleidovský trojrozměrný prostor
