---
title: "Wektory i kombinacje liniowe"
description: "Czym jest wektor oraz jakie są jego podstawowe operacje (mnożenie przez skalar, dodawanie); na tej podstawie wyjaśniamy kombinacje liniowe wektorów i pojęcie rozpiętości (span)."
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Definicja wektora**
>   - **Wektor w wąskim sensie (wektor euklidesowy)**: wielkość fizyczna mająca jednocześnie moduł i kierunek
>   - **Wektor w szerokim sensie, w algebrze liniowej**: element przestrzeni wektorowej
> - **Sposoby zapisu wektora**
>   - **Zapis strzałkowy**: moduł wektora przedstawia długość strzałki, a kierunek wektora — kierunek strzałki. Zaletą jest łatwa wizualizacja i intuicyjność, jednak trudno w ten sposób przedstawiać wektory wysokowymiarowe (≥4) lub nieeuklidesowe.
>   - **Zapis współrzędnych (składowych)**: ustawiamy początek wektora w początku układu współrzędnych i opisujemy wektor współrzędnymi punktu końcowego.
> - **Podstawowe działania na wektorach**
>   - **Suma**: $(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **Iloczyn przez skalar**: $c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **Kombinacja liniowa wektorów**
>   - Dla skończonej liczby wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ oraz skalarów $a_1, a_2, \dots, a_n$ wektor $\mathbf{v}$ spełniający $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$ nazywamy **kombinacją liniową (linear combination)** wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$
>   - Wtedy $a_1, a_2, \dots, a_n$ nazywamy **współczynnikami (coefficient)** tej kombinacji liniowej
> - **Rozpiętość**
>   - Dla niepustego podzbioru $S$ przestrzeni wektorowej $\mathbb{V}$: zbiór wszystkich kombinacji liniowych utworzonych z wektorów z $S$, oznaczany $\mathrm{span}(S)$
>   - Definiujemy $\mathrm{span}(\emptyset) = \\{0\\}$
>   - Jeśli dla podzbioru $S \subset \mathbb{V}$ zachodzi $\mathrm{span}(S) = \mathbb{V}$, to mówimy, że $S$ generuje (generate lub span) przestrzeń $\mathbb{V}$
{: .prompt-info }

## Prerequisites
- płaszczyzna/ przestrzeń współrzędnych
- ciało (field)

## Czym jest wektor?

### Wektor w wąskim sensie: wektor euklidesowy

> Siła, prędkość, przyspieszenie i wiele innych wielkości fizycznych ma nie tylko moduł, lecz także informację o kierunku. Taką wielkość fizyczną mającą zarówno moduł, jak i kierunek nazywa się **wektorem (vector)**.
{: .prompt-info }

Powyższa definicja to definicja wektora znana z mechaniki w fizyce lub z matematyki na poziomie szkoły średniej. Wektor w wąskim sensie — mający geometryczne znaczenie „długości i kierunku zorientowanego odcinka” oraz oparty na fizycznej intuicji — nazywa się ściślej **wektorem euklidesowym (Euclidean vector)**.

### Wektor w szerokim sensie: element przestrzeni wektorowej

W algebrze liniowej wektor definiuje się jako bardziej abstrakcyjną strukturę algebraiczną o szerszym znaczeniu niż powyższy wektor euklidesowy:

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

Taka definicja wektora w algebrze liniowej jest definicją o szerszym zakresie, obejmującą również wspomniany wcześniej [wektor euklidesowy](#wektor-w-wąskim-sensie-wektor-euklidesowy). Można sprawdzić, że [wektor euklidesowy](#wektor-w-wąskim-sensie-wektor-euklidesowy) także spełnia powyższe 8 własności.

Geneza i rozwój pojęcia wektora są ściśle związane z różnymi praktycznymi problemami stawianymi przez fizykę — próbami ilościowego opisu takich pojęć jak siła, ruch ciała, obrót czy pole. Z potrzeby fizycznej, by matematycznie opisywać zjawiska przyrodnicze, początkowo zaproponowano pojęcie wektora jako [wektora euklidesowego](#wektor-w-wąskim-sensie-wektor-euklidesowy). Następnie matematyka uogólniała i formalizowała te idee, ustanawiając struktury takie jak przestrzenie wektorowe, iloczyn skalarny i wektorowy, co doprowadziło do współczesnej definicji wektora. Innymi słowy, wektor to pojęcie „wymagane przez fizykę i ugruntowane przez matematykę” — produkt interdyscyplinarny rozwijany przez ścisłą współpracę matematyków i fizyków, a nie wyłącznie wytwór czystej matematyki.

[Wektory euklidesowe](#wektor-w-wąskim-sensie-wektor-euklidesowy) używane w klasycznej mechanice można matematycznie opisać w [bardziej uogólnionych ramach](#wektor-w-szerokim-sensie-element-przestrzeni-wektorowej). Współczesna fizyka aktywnie wykorzystuje nie tylko [wektory euklidesowe](#wektor-w-wąskim-sensie-wektor-euklidesowy), lecz także bardziej abstrakcyjne pojęcia zdefiniowane w matematyce, takie jak przestrzenie wektorowe czy przestrzenie funkcji, nadając im interpretację fizyczną. Dlatego niewłaściwe jest rozumienie tych dwóch definicji wyłącznie jako „definicji fizycznej” i „definicji matematycznej”.

O przestrzeniach wektorowych powiemy więcej później; na razie skupimy się na wąskim sensie wektora — wektorach euklidesowych, które da się geometrycznie przedstawić w przestrzeni współrzędnych. Najpierw warto zobaczyć intuicyjne przykłady wektorów euklidesowych, bo ułatwia to późniejsze uogólnienia na inne rodzaje wektorów.

## Sposoby zapisu wektora
### Zapis strzałkowy

To najczęściej spotykany zapis, najlepiej oddający intuicję geometryczną. Moduł wektora przedstawia się jako długość strzałki, a kierunek wektora — jako kierunek strzałki.

![Euclidean Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *Źródło obrazu*
> - autor: użytkownik Wikipedii [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

Taki zapis jest intuicyjny, jednak dla wektorów wysokowymiarowych (co najmniej 4-wymiarowych) ma oczywiste ograniczenia. Co więcej, później trzeba będzie rozważać także wektory nieeuklidesowe, których nie da się wygodnie przedstawić geometrycznie, dlatego warto oswoić się z omówionym niżej zapisem współrzędnych.

### Zapis współrzędnych (składowych)

Wektory o takim samym module i kierunku uznaje się za identyczne, niezależnie od tego, gdzie „leżą”. Zatem, gdy dana jest przestrzeń współrzędnych, jeśli umocujemy początek wektora w początku układu, to <u>wektor $n$-wymiarowy odpowiada dowolnemu punktowi w przestrzeni $n$-wymiarowej</u>, a wtedy wektor można opisać współrzędnymi punktu końcowego. Taki zapis nazywamy **zapisem współrzędnych (składowych)** wektora.

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ lub } \mathbb{C}^n $$

![Position vector](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Podstawowe działania na wektorach

Podstawowe działania na wektorach to dwa: **suma** oraz **mnożenie przez skalar**. Wszystkie operacje wektorowe da się wyrazić jako złożenie tych dwóch podstawowych działań.

### Suma wektorów

Suma dwóch wektorów jest również wektorem, a składowe wektora wynikowego są sumami odpowiednich składowych.

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### Mnożenie wektora przez skalar

Wektor można „powiększać” lub „pomniejszać”; opisuje to działanie mnożenia wektora przez stałą (skalar). Wynik mnożenia przez skalar odpowiada mnożeniu każdej składowej przez ten skalar.

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Scalar multiplication of vectors](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikipedii [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## Kombinacje liniowe wektorów

Tak jak analiza matematyczna startuje od liczby $x$ i funkcji $f(x)$, tak algebra liniowa startuje od wektorów $\mathbf{v}, \mathbf{w}, \dots$ oraz kombinacji liniowych postaci $c\mathbf{v} + d\mathbf{w} + \cdots$. Wszystkie kombinacje liniowe wektorów są zbudowane jako złożenie dwóch podstawowych działań: [sumy](#suma-wektorów) i [mnożenia przez skalar](#mnożenie-wektora-przez-skalar).

> Dla skończonej liczby wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ oraz skalarów $a_1, a_2, \dots, a_n$ wektor $\mathbf{v}$ spełniający
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> nazywamy **kombinacją liniową (linear combination)** wektorów $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$.
> 
> Wtedy $a_1, a_2, \dots, a_n$ nazywamy **współczynnikami (coefficient)** tej kombinacji liniowej.
{: .prompt-info }

Dlaczego takie kombinacje liniowe są ważne? Rozważmy sytuację, w której **$n$ wektorów w $m$-wymiarowej przestrzeni tworzy $n$ kolumn macierzy $m \times n$**.

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

Kluczowe są tu dwa punkty:

1. **Opisz wszystkie możliwe kombinacje liniowe $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots x_n\mathbf{v}_n$.** Co tworzą?
2. Znajdź **liczby $x_1, x_2, \dots, x_n$**, które wytworzą żądany wektor wyjściowy $Ax = b$.

Do odpowiedzi na drugie pytanie wrócimy później, a teraz skupmy się na pierwszym. Aby uprościć rozważania, rozpatrzmy przykład dwóch niezerowych wektorów dwuwymiarowych ($m=2$) w liczbie dwóch ($n=2$).

### Kombinacja liniowa $c\mathbf{v} + d\mathbf{w}$

Wektor $\mathbf{v}$ w przestrzeni 2D ma dwie składowe. Dla każdego skalara $c$ <u>wektor $c\mathbf{v}$ jest równoległy do $\mathbf{v}$ i wyznacza w płaszczyźnie $xy$ nieskończenie długą prostą przechodzącą przez początek układu.</u>

Jeżeli drugi dany wektor $\mathbf{w}$ nie leży na tej prostej (tj. wektory $\mathbf{v}$ i $\mathbf{w}$ nie są równoległe), to wektor $d\mathbf{w}$ wyznacza drugą prostą. Gdy połączymy te dwie proste, widać, że **kombinacja liniowa $c\mathbf{v} + d\mathbf{w}$ wyznacza pewną płaszczyznę zawierającą początek układu**.

![Linear combinations of two vectors](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - licencja: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

### Rozpinanie

W ten sposób kombinacje liniowe wektorów tworzą przestrzeń wektorową; nazywa się to **rozpinaniem (span)**.

> **Definicja**  
> Dla niepustego podzbioru $S$ przestrzeni wektorowej $\mathbb{V}$ zbiór wszystkich kombinacji liniowych utworzonych z wektorów z $S$ nazywamy **rozpiętością (span)** zbioru $S$ i oznaczamy $\mathrm{span}(S)$. Ponadto definiujemy $\mathrm{span}(\emptyset) = \\{0\\}$.
{: .prompt-info }

> **Definicja**  
> Dla podzbioru $S$ przestrzeni wektorowej $\mathbb{V}$, jeśli $\mathrm{span}(S) = \mathbb{V}$, to mówimy, że $S$ generuje (generate lub span) przestrzeń $\mathbb{V}$.
{: .prompt-info }

Nie omawialiśmy jeszcze pojęć takich jak podprzestrzeń czy baza, jednak przywołanie tego przykładu pomaga w zrozumieniu samej idei przestrzeni wektorowej.
