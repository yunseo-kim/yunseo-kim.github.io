---
title: "Vektory a lineární kombinace"
description: "Vysvětlíme, co je vektor a jaké jsou jeho základní operace (násobení skalárem, sčítání). Na tomto základě pochopíme lineární kombinace vektorů a pojem generovaného podprostoru (span)."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Definice vektoru**
>   - **Vektor v užším smyslu (eukleidovský vektor)**: fyzikální veličina, která má zároveň velikost i směr
>   - **Vektor v širším smyslu, v lineární algebře**: prvek vektorového prostoru
> - **Způsoby reprezentace vektoru**
>   - **Šipková reprezentace**: velikost vektoru je dána délkou šipky a směr vektoru směrem šipky. Výhodou je snadná vizualizace a intuitivnost, nevýhodou však to, že je obtížné takto vyjadřovat vektory ve 4 a více dimenzích nebo neeukleidovské vektory.
>   - **Složková reprezentace**: počátek vektoru se položí do počátku souřadného prostoru a vektor se vyjádří souřadnicemi koncového bodu.
> - **Základní operace s vektory**
>   - **Součet**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **Násobení skalárem**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **Lineární kombinace vektorů**
>   - Pro konečně mnoho vektorů $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ a skalárů $a_1, a_2, \dots, a_n$ se vektor $\mathbf{v}$ splňující $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$ nazývá **lineární kombinací (linear combination)** vektorů $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$
>   - Čísla $a_1, a_2, \dots, a_n$ se nazývají **koeficienty (coefficient)** této lineární kombinace
> - **Generovaný podprostor**
>   - Pro neprázdnou podmnožinu $S$ vektorového prostoru $\mathbb{V}$ je $\mathrm{span}(S)$ množina všech lineárních kombinací vytvořených z vektorů v $S$
>   - Definuje se $\mathrm{span}(\emptyset) = \\{0\\}$
>   - Pro podmnožinu $S$ vektorového prostoru $\mathbb{V}$, platí-li $\mathrm{span}(S) = \mathbb{V}$, říkáme, že $S$ generuje (generate nebo span) prostor $\mathbb{V}$
{: .prompt-info }

## Prerequisites
- souřadná rovina / souřadný prostor
- těleso (field)

## Co je to vektor?

### Vektor v užším smyslu: eukleidovský vektor

> Mnoho fyzikálních veličin, jako je síla, rychlost či zrychlení, má kromě velikosti také informaci o směru. Takové fyzikální veličiny, které mají velikost i směr, se nazývají **vektory (vector)**.
{: .prompt-info }

Výše uvedená definice je definice vektoru, se kterou se setkáváme v klasické mechanice nebo na středoškolské úrovni matematiky. Takový vektor v užším smyslu, založený na fyzikální intuici a nesoucí geometrický význam „velikosti a směru orientované úsečky“, se přesněji nazývá **eukleidovský vektor (Euclidean vector)**.

### Vektor v širším smyslu: prvek vektorového prostoru

V lineární algebře se vektor definuje v širším smyslu než výše uvedený eukleidovský vektor, jako abstraktnější algebraická struktura, následovně.

> **Definice**  
> **Vektorový prostor (vector space)** neboli **lineární prostor (linear space)** $\mathbb{V}$ nad tělesem $F$ je množina vybavená dvěma operacemi, **sčítáním** a **násobením skalárem**, které splňují následujících 8 podmínek. Prvky tělesa $F$ nazýváme **skaláry (scalar)** a prvky vektorového prostoru $\mathbb{V}$ nazýváme **vektory (vector)**.
>
> - **Sčítání (sum)**: pro dva prvky $\mathbf{x}, \mathbf{y} \in \mathbb{V}$ je přiřazena jednoznačná hodnota $\mathbf{x} + \mathbf{y} \in \mathbb{V}$. Tomuto $\mathbf{x} + \mathbf{y}$ říkáme **součet** vektorů $\mathbf{x}$ a $\mathbf{y}$.
> - **Násobení skalárem (scalar multiplication)**: každému prvku $a \in F$ a každému prvku $\mathbf{x} \in \mathbb{V}$ je přiřazena jednoznačná hodnota $a\mathbf{x} \in \mathbb{V}$. Tomuto $a\mathbf{x}$ říkáme **skalární násobek (scalar multiple)** vektoru $\mathbf{x}$.
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

Tato definice vektoru v lineární algebře je širší než dříve uvedený [eukleidovský vektor](#vektor-v-užším-smyslu-eukleidovský-vektor) a zahrnuje jej. Lze ověřit, že i [eukleidovské vektory](#vektor-v-užším-smyslu-eukleidovský-vektor) splňují všech osm výše uvedených vlastností.

Původ a vývoj vektorů úzce souvisí s řadou praktických problémů, které vyvstaly ve fyzice — například se snahou kvantitativně popsat sílu, pohyb těles, rotaci či pojmy jako pole. Potřeba matematicky vyjadřovat přírodní jevy vedla k tomu, že byl nejprve zaveden pojem vektoru jako [eukleidovského vektoru](#vektor-v-užším-smyslu-eukleidovský-vektor). Následně matematika tyto fyzikální koncepty zobecnila a teoreticky zformulovala: ustavila formální struktury, jako jsou vektorové prostory, skalární součin, vektorový součin apod., čímž vznikla dnešní definice vektoru. Jinými slovy, vektor je pojem, který si vyžádala fyzika a zformulovala matematika; nejde tedy o výhradní produkt čisté matematiky, ale spíše o interdisciplinární výsledek, který se rozvíjel díky úzké výměně mezi matematikou a fyzikou.

[Eukleidovské vektory](#vektor-v-užším-smyslu-eukleidovský-vektor), se kterými pracuje klasická mechanika, lze matematicky vyjádřit v [obecnějším rámci](#vektor-v-širším-smyslu-prvek-vektorového-prostoru). V současné fyzice se aktivně používají nejen [eukleidovské vektory](#vektor-v-užším-smyslu-eukleidovský-vektor), ale i abstraktnější pojmy definované matematikou, jako jsou vektorové prostory či prostory funkcí, kterým se následně přiřazuje fyzikální význam. Proto není vhodné chápat dvě definice vektoru jednoduše jako „fyzikální definici“ a „matematickou definici“.

Vektorové prostory si podrobněji probereme později; nyní se zaměříme na eukleidovské vektory v užším smyslu, které lze geometricky vyjádřit v souřadném prostoru. Nejprve si ukážeme intuitivní příklady eukleidovských vektorů, protože to pomůže i při pozdějším zobecnění na jiné typy vektorů.

## Způsoby reprezentace vektoru
### Šipková reprezentace

Jde o nejběžnější způsob, který nejlépe zachovává geometrickou intuici. Velikost vektoru se vyjadřuje délkou šipky a směr vektoru směrem šipky.

![Euclidean Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *Zdroj obrázku*
> - autor: uživatel Wikipedie [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

Tato reprezentace je sice intuitivní, ale u vektorů ve 4 a více dimenzích má zjevná omezení. Navíc později budeme pracovat i s neeukleidovskými vektory, které jsou už z principu obtížně geometricky znázornitelné, takže je potřeba si zvyknout na složkovou reprezentaci popsanou níže.

### Složková reprezentace

Vektor považujeme za stejný bez ohledu na to, kde je umístěn, pokud má stejnou velikost i směr. Proto, je-li dán souřadný prostor, můžeme počátek vektoru zafixovat do počátku tohoto prostoru; pak <u>$n$-rozměrný vektor odpovídá libovolnému bodu v $n$-rozměrném prostoru</u> a vektor lze vyjádřit souřadnicemi koncového bodu. Tomuto způsobu říkáme **složková reprezentace** vektoru.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ or } \mathbb{C}^n $$

![Position vector](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Základní operace s vektory

Základní operace s vektory jsou dvě: **součet** a **násobení skalárem**. Všechny vektorové operace lze vyjádřit jako kombinaci těchto dvou základních operací.

### Součet vektorů

Součet dvou vektorů je opět vektor a složky výsledného vektoru jsou rovny součtům odpovídajících složek obou vektorů.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### Násobení vektoru skalárem

Vektor lze zvětšovat či zmenšovat; to se popisuje operací násobení skalárem, tj. vynásobením vektoru konstantou (skalárem). Výsledek násobení vektoru skalárem odpovídá vynásobení každé složky vektoru stejným skalárem.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Scalar multiplication of vectors](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikipedie [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Lineární kombinace vektorů

Stejně jako kalkulus začíná číslem $x$ a funkcí $f(x)$, lineární algebra začíná vektory $\mathbf{v}, \mathbf{w}, \dots$ a lineárními kombinacemi $c\mathbf{v} + d\mathbf{w} + \cdots$. A všechny lineární kombinace vektorů se skládají z kombinací dvou výše uvedených základních operací: [součtu](#součet-vektorů) a [násobení skalárem](#násobení-vektoru-skalárem).

> Pro konečně mnoho vektorů $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ a skalárů $a_1, a_2, \dots, a_n$ se vektor $\mathbf{v}$, který splňuje následující, nazývá **lineární kombinací (linear combination)** vektorů $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$.
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> V tomto případě se $a_1, a_2, \dots, a_n$ nazývají **koeficienty (coefficient)** této lineární kombinace.
{: .prompt-info }

Proč je ale lineární kombinace tak důležitá? Uvažujme následující situaci: **$n$ vektorů v $m$-rozměrném prostoru tvoří $n$ sloupců matice typu $m \times n$**.

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

Klíčové jsou zde následující dvě věci.

1. **Vyjádřete všechny možné lineární kombinace $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots x_n\mathbf{v}_n$.** Co tvoří?
2. Najděte **čísla $x_1, x_2, \dots, x_n$**, která vytvoří požadovaný výstupní vektor $Ax = b$.

Odpověď na druhou otázku si rozebereme později; zatím se soustřeďme na první. Pro zjednodušení uvažujme jako příklad případ dvou nenulových 2D vektorů ($m=2$) a dvou vektorů celkem ($n=2$).

### Lineární kombinace $c\mathbf{v} + d\mathbf{w}$

Vektor $\mathbf{v}$ v dvojrozměrném prostoru má dvě složky. Pro libovolný skalár $c$ platí, že <u>vektor $c\mathbf{v}$ je rovnoběžný s původním vektorem $\mathbf{v}$ a tvoří nekonečně dlouhou přímku v rovině $xy$, která prochází počátkem.</u>

Pokud druhý daný vektor $\mathbf{w}$ neleží na této přímce (tj. vektory $\mathbf{v}$ a $\mathbf{w}$ nejsou rovnoběžné), pak i $d\mathbf{w}$ tvoří další, druhou přímku. Když nyní tyto dvě přímky zkombinujeme, zjistíme, že **lineární kombinace $c\mathbf{v} + d\mathbf{w}$ tvoří rovinu obsahující počátek**.

![Linear combinations of two vectors](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - licence: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

### Generování

Takové lineární kombinace vektorů tedy vytvářejí (vyplňují) vektorový prostor; tomuto se říká **generování (span)** prostoru.

> **Definice**  
> Pro neprázdnou podmnožinu $S$ vektorového prostoru $\mathbb{V}$ se množina všech lineárních kombinací vytvořených z vektorů v $S$ nazývá **generovaný podprostor (span)** množiny $S$ a značí se $\mathrm{span}(S)$. Dále se definuje $\mathrm{span}(\emptyset) = \\{0\\}$.
{: .prompt-info }

> **Definice**  
> Pro podmnožinu $S$ vektorového prostoru $\mathbb{V}$, platí-li $\mathrm{span}(S) = \mathbb{V}$, říkáme, že $S$ generuje (generate nebo span) prostor $\mathbb{V}$.
{: .prompt-info }

Zatím jsme neprobírali pojmy jako podprostor či báze, ale když si vybavíte tento příklad, pomůže vám to pochopit pojem vektorového prostoru.
