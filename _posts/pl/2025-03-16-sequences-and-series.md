---
title: "Ciągi i szeregi"
description: "Omawiamy podstawowe pojęcia analizy matematycznej: definicje ciągów i szeregów, zbieżność i rozbieżność ciągów oraz szeregów, a także definicję liczby e jako podstawy logarytmu naturalnego."
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Ciągi
W analizie matematycznej **ciąg (sequence)** oznacza najczęściej ciąg nieskończony. Innymi słowy, ciąg to funkcja określona na zbiorze wszystkich **liczb naturalnych (natural number)**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

.* Jeśli wartościami tej funkcji są liczby rzeczywiste (real number), mówimy o „ciągu rzeczywistym”, jeśli zespolone (complex number) — o „ciągu zespolonym”, jeśli punkty (point) — o „ciągu punktów”, jeśli macierze (matrix) — o „ciągu macierzy”, jeśli funkcje (function) — o „ciągu funkcji”, jeśli zbiory (set) — o „ciągu zbiorów” itd.; wszystkie te przypadki można jednak zbiorczo nazywać po prostu „ciągiem”.

Zwykle, dla **ciała liczb rzeczywistych (the field of real numbers)** $\mathbb{R}$, dla ciągu $\mathbf{a}: \mathbb{N} \to \mathbb{R}$ przyjmuje się oznaczenia

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

itd., a sam ciąg zapisuje się jako

$$ a_1,\, a_2,\, a_3,\, \dots $$

albo

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

itd.

> *W procesie definiowania ciągu, zamiast dziedziny będącej zbiorem wszystkich liczb naturalnych $\mathbb{N}$, można przyjąć zbiór liczb całkowitych nieujemnych
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> albo
>
> $$\{2,3,4,\dots \}$$
>
> itd. Na przykład w teorii szeregów potęgowych bardziej naturalne jest, by dziedziną było $\mathbb{N}_0$.
{: .prompt-info }

## Zbieżność i rozbieżność
Jeśli ciąg $(a_n)$ jest zbieżny do liczby rzeczywistej $l$, to piszemy

$$ \lim_{n\to \infty} a_n = l $$

a liczbę $l$ nazywamy **granicą** ciągu $(a_n)$.

> Ścisła definicja z użyciem **argumentu epsilon-delta (epsilon-delta argument)** jest następująca.
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> To znaczy: dla dowolnie małego dodatniego $\epsilon$, jeśli zawsze istnieje taka liczba naturalna $N$, że dla $n>N$ zachodzi $|a_n-l|<\epsilon$, to dla dostatecznie dużych $n$ różnica między $a_n$ i $l$ staje się dowolnie mała; wówczas definiujemy, że ciąg $(a_n)$ jest zbieżny do liczby rzeczywistej $l$.
{: .prompt-info }

Ciąg, który nie jest zbieżny, nazywamy **rozbieżnym**. *Zbieżność lub rozbieżność ciągu nie zmienia się, nawet jeśli zmienimy skończoną liczbę jego wyrazów.*

Jeśli kolejne wyrazy ciągu $(a_n)$ rosną bez ograniczeń, to piszemy

$$ \lim_{n\to \infty} a_n = \infty $$

i mówimy, że *ciąg jest rozbieżny do dodatniej nieskończoności*. Analogicznie, jeśli wyrazy ciągu $(a_n)$ maleją bez ograniczeń, to piszemy

$$ \lim_{n\to \infty} a_n = -\infty $$

i mówimy, że *ciąg jest rozbieżny do ujemnej nieskończoności*.

## Podstawowe własności ciągów zbieżnych
Jeśli ciągi $(a_n)$ oraz $(b_n)$ są zbieżne (tj. mają granice), to ciągi $(a_n + b_n)$ oraz $(a_n \cdot b_n)$ również są zbieżne, przy czym

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Ponadto dla dowolnej liczby rzeczywistej $t$ zachodzi

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Własności te nazywa się **podstawowymi własnościami ciągów zbieżnych** albo **podstawowymi własnościami granic**.

## Podstawa logarytmu naturalnego $e$
**Podstawę logarytmu naturalnego** definiuje się jako

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

Jest to jedna z najważniejszych stałych w matematyce.

> Co ciekawe, praktycznie tylko w Korei dość szeroko używa się określenia „stała naturalna”, jednak nie jest to termin standardowy. Oficjalnym terminem, umieszczonym w słowniku terminów matematycznych Koreańskiego Towarzystwa Matematycznego, jest ['podstawa logarytmu naturalnego'](https://www.kms.or.kr/mathdict/list.html?key=kname&keyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98+%EB%B0%91), natomiast określenia „stała naturalna” nie da się w tym słowniku znaleźć. Co więcej, nawet w standardowym słowniku Narodowego Instytutu Języka Koreańskiego nie występuje hasło „stała naturalna”; w [definicji słownikowej „logarytmu naturalnego”](https://stdict.korean.go.kr/search/searchView.do?pageSize=10&searchKeyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8) wspomina się jedynie o „pewnej liczbie, którą często oznacza się przez e”.  
> W krajach anglojęzycznych i w Japonii również nie funkcjonuje odpowiadający temu termin; po angielsku najczęściej mówi się „the base of the natural logarithm”, w skrócie „natural base”, albo „Euler's number” czy po prostu „the number $e$”.  
> Ponieważ jest to określenie o niejasnym pochodzeniu, nigdy nieuznane za termin oficjalny przez Koreańskie Towarzystwo Matematyczne i nieużywane nigdzie na świecie poza Koreą, nie ma żadnego powodu, by się go upierać; dlatego także tutaj będę odtąd używać określenia „podstawa logarytmu naturalnego” lub po prostu zapisywać $e$.
{: .prompt-tip }

## Szeregi
Dla ciągu

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

definiujemy inny ciąg, złożony z sum częściowych tego ciągu:

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

Nazywa się go **szeregiem** ciągu $\mathbf{a}$. Szereg ciągu $(a_n)$ zapisuje się jako

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

itd.

## Zbieżność i rozbieżność szeregów
Jeśli szereg otrzymany z ciągu $(a_n)$

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

jest zbieżny do pewnej liczby rzeczywistej $l$, to zapisujemy

$$ \sum_{n=1}^{\infty} a_n = l $$

Wówczas granicę $l$ nazywa się **sumą** szeregu $\sum a_n$. Symbol

$$ \sum a_n $$

w zależności od kontekstu może oznaczać zarówno <u>szereg</u>, jak i <u>sumę tego szeregu</u>.

Szereg, który nie jest zbieżny, nazywamy **rozbieżnym**.

## Podstawowe własności szeregów zbieżnych
Z [podstawowych własności ciągów zbieżnych](#podstawowe-własności-ciągów-zbieżnych) wynikają następujące podstawowe własności szeregów zbieżnych. Dla liczby rzeczywistej $t$ oraz dwóch zbieżnych szeregów $\sum a_n$, $\sum b_n$ zachodzi

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n \tag{4}$$

Zbieżność szeregu nie zależy od zmiany skończonej liczby wyrazów. To znaczy: jeśli dla dwóch ciągów $(a_n)$ oraz $(b_n)$ zachodzi $a_n=b_n$ dla wszystkich $n$ z wyjątkiem skończonej ich liczby, to warunkiem koniecznym i wystarczającym zbieżności szeregu $\sum a_n$ jest zbieżność szeregu $\sum b_n$.
