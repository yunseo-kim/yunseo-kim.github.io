---
title: Kryteria zbieżności/rozbieżności szeregu (Testing for Convergence or Divergence of a Series)
description: Przegląd najważniejszych metod badania zbieżności i rozbieżności szeregów.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Kryterium wyrazu ogólnego ($n$th-term test for divergence)**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{szereg }\sum a_n \text{ jest rozbieżny}$
> - **Zbieżność/rozbieżność szeregu geometrycznego**: szereg geometryczny $\sum ar^{n-1}$ jest
>   - zbieżny, gdy $\|r\| < 1$
>   - rozbieżny, gdy $\|r\| \geq 1$
> - **Zbieżność/rozbieżność $p$-szeregu**: $p$-szereg $\sum \cfrac{1}{n^p}$ jest
>   - zbieżny, gdy $p>1$
>   - rozbieżny, gdy $p\leq 1$
> - **Test porównawczy (Comparison Test)**: gdy $0 \leq a_n \leq b_n$,  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Test porównawczy graniczny (Limit Comparison Test)**: jeśli $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ jest skończoną liczbą dodatnią)}$, to oba szeregi $\sum a_n$ i $\sum b_n$ albo są zbieżne, albo oba są rozbieżne
> - Dla szeregu o wyrazach dodatnich $\sum a_n$ i dodatniej liczby $\epsilon < 1$  
>   - jeśli dla każdego $n$ zachodzi $\sqrt[n]{a_n}< 1-\epsilon$, to szereg $\sum a_n$ jest zbieżny
>   - jeśli dla każdego $n$ zachodzi $\sqrt[n]{a_n}> 1+\epsilon$, to szereg $\sum a_n$ jest rozbieżny
> - **Kryterium pierwiastkowe (Root Test)**: dla szeregu o wyrazach dodatnich $\sum a_n$, gdy istnieje granica $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$,
>   - jeśli $r<1$, to szereg $\sum a_n$ jest zbieżny
>   - jeśli $r>1$, to szereg $\sum a_n$ jest rozbieżny
> - **Kryterium ilorazowe (Ratio Test)**: dla dodatniego ciągu $(a_n)$ i $0 < r < 1$
>   - jeśli dla każdego $n$ zachodzi $a_{n+1}/a_n \leq r$, to szereg $\sum a_n$ jest zbieżny
>   - jeśli dla każdego $n$ zachodzi $a_{n+1}/a_n \geq 1$, to szereg $\sum a_n$ jest rozbieżny
> - Jeśli dla dodatniego ciągu $(a_n)$ istnieje granica $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$, to
>   - gdy $\rho < 1$, szereg $\sum a_n$ jest zbieżny
>   - gdy $\rho > 1$, szereg $\sum a_n$ jest rozbieżny
> - **Kryterium całkowe (Integral Test)**: gdy funkcja ciągła $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ jest malejąca i zawsze $f(x)>0$, warunkiem koniecznym i wystarczającym zbieżności szeregu $\sum f(n)$ jest zbieżność całki $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$
> - **Kryterium Leibniza dla szeregu naprzemiennego (Alternating Series Test)**: jeśli spełnione są warunki:
>   1. dla każdego $n$ wyrazy $a_n$ i $a_{n+1}$ mają różne znaki,
>   2. dla każdego $n$ zachodzi $\|a_n\| \geq \|a_{n+1}\|$,
>   3. $\lim_{n\to\infty} a_n = 0$,
>
>   to szereg naprzemienny $\sum a_n$ jest zbieżny
> - Szereg zbieżny bezwzględnie jest zbieżny. Odwrotność nie zachodzi.
{: .prompt-info }

## Wymagania wstępne
- [Ciągi i szeregi](/posts/sequences-and-series/)

## Wprowadzenie
Wcześniej, w tekście [Ciągi i szeregi](/posts/sequences-and-series/#zbieznosc-i-rozbieznosc-szeregu), omówiliśmy definicje zbieżności i rozbieżności szeregu. W tym wpisie porządkuję różne metody, których można użyć do rozstrzygania o zbieżności/rozbieżności szeregów. Zwykle sprawdzenie zbieżności/rozbieżności jest dużo łatwiejsze niż dokładne wyznaczenie sumy szeregu.

## Kryterium wyrazu ogólnego
Dla szeregu $\sum a_n$ wyraz $a_n$ nazywa się **wyrazem ogólnym** tego szeregu.

Z poniższego twierdzenia wynika, że dla pewnych szeregów bardzo łatwo stwierdzić ich rozbieżność. Dlatego, oceniając zbieżność/rozbieżność danego szeregu, rozsądnie jest zacząć właśnie od tego sprawdzenia — pozwala to uniknąć marnowania czasu.

> **Kryterium wyrazu ogólnego ($n$th-term test for divergence)**  
> Jeśli szereg $\sum a_n$ jest zbieżny, to
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> czyli
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{szereg }\sum a_n \text{ jest rozbieżny} $$
>
> .
{: .prompt-info }

### Dowód
Niech suma pewnego zbieżnego szeregu $\sum a_n$ wynosi $l$, a suma częściowa do $n$-tego wyrazu będzie równa

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Wtedy

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Zatem dla dostatecznie dużego ($>N$) $n$ zachodzi

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

a więc, z definicji zbieżności ciągu,

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Uwaga
Odwrotność tego twierdzenia na ogół nie jest prawdziwa. Klasycznym przykładem jest **szereg harmoniczny (harmonic series)**.

Szereg harmoniczny jest szeregiem otrzymanym z **ciągu harmonicznego**, tj. z ciągu, którego wyrazy są odwrotnościami wyrazów **ciągu arytmetycznego**. Reprezentatywny przykład to

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Można pokazać, że jest to szereg rozbieżny, np. tak:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Widzimy więc, że mimo iż szereg $H_n$ jest rozbieżny, jego wyraz ogólny $1/n$ dąży do $0$.

> Jeśli $\lim_{n\to\infty} a_n \neq 0$, to szereg $\sum a_n$ na pewno jest rozbieżny, ale samo $\lim_{n\to\infty} a_n = 0$ nie gwarantuje zbieżności szeregu $\sum a_n$. W takim przypadku należy użyć innych metod oceny zbieżności/rozbieżności.
{: .prompt-danger }

## Szereg geometryczny
**Szereg geometryczny (geometric series)** otrzymany z ciągu geometrycznego o pierwszym wyrazie równym 1 i **ilorazie** $r$:

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

jest <u>najważniejszym i najbardziej podstawowym szeregiem</u>. Z tożsamości

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

wynika

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Ponieważ

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

to warunkiem koniecznym i wystarczającym zbieżności szeregu geometrycznego ($\ref{eqn:geometric_series}$) jest $\|r\| < 1$.

> **Zbieżność/rozbieżność szeregu geometrycznego**  
> Szereg geometryczny $\sum ar^{n-1}$ jest
> - zbieżny, gdy $\|r\| < 1$
> - rozbieżny, gdy $\|r\| \geq 1$
{: .prompt-info }

Stąd otrzymujemy

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Szereg geometryczny i wartości przybliżone
Tożsamość ($\ref{eqn:sum_of_geometric_series}$) jest użyteczna do znajdowania przybliżeń $\cfrac{1}{1-r}$, gdy $\|r\| < 1$.

Podstawiając $r=-\epsilon$, $n=2$, otrzymujemy

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Zatem dla $0 < \epsilon < 1$ zachodzi

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

a więc

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

Wynika z tego, że dla dostatecznie małego dodatniego $\epsilon$ można przybliżać $\cfrac{1}{1 + \epsilon}$ przez $1 - \epsilon$.

## Kryterium $p$-szeregu ($p$-Series Test)  
Dla dodatniej liczby rzeczywistej $p$ szereg postaci

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

nazywa się **$p$-szeregiem**.

> **Zbieżność/rozbieżność $p$-szeregu**  
> $p$-szereg $\sum \cfrac{1}{n^p}$ jest
> - zbieżny, gdy $p>1$
> - rozbieżny, gdy $p\leq 1$
{: .prompt-info }

Dla $p=1$ otrzymujemy szereg harmoniczny, o którym już pokazaliśmy, że jest rozbieżny.  
Problem obliczenia wartości $p$-szeregu dla $p=2$, tj. $\sum \cfrac{1}{n^2}$, nazywa się „problemem bazylejskim” (Bazylea, Basel) — od nazwy miejsca związanego z rodziną Bernoullich, która odegrała znaczącą rolę w historii tego zagadnienia. Wiadomo, że odpowiedź wynosi $\cfrac{\pi^2}{6}$.

Co więcej, w ujęciu ogólniejszym, dla $p$-szeregu z $p>1$ mówi się o **funkcji dzeta (zeta function)**. Jest to jedna z funkcji szczególnych wprowadzona przez Leonharda Eulera w [erze holoceńskiej](https://en.wikipedia.org/wiki/Holocene_calendar) w roku 11740 HE, a później nazwana przez Riemanna:

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Temat ten nieco odbiega od głównego wątku, a poza tym — szczerze mówiąc — jestem studentem kierunku inżynierskiego, nie matematykiem, więc sam też nie znam go dobrze i nie będę go tu rozwijał. Warto jednak wspomnieć, że Euler pokazał możliwość przedstawienia funkcji dzeta jako nieskończonego iloczynu po liczbach pierwszych, znanego jako **iloczyn Eulera (Euler Product)**, a sama funkcja dzeta zajmuje dziś kluczowe miejsce w wielu działach analitycznej teorii liczb. Jednym z najsłynniejszych przykładów jest **funkcja dzeta Riemanna (Riemann zeta function)** (rozszerzenie dziedziny na liczby zespolone) oraz ważny nierozwiązany problem: **hipoteza Riemanna (Riemann hypothesis)**.

Wracając do tematu: do dowodu kryterium $p$-szeregu potrzebujemy omówionego niżej [testu porównawczego](#test-porownawczy) i [kryterium całkowego](#test-calkowy). Jednak zbieżność/rozbieżność $p$-szeregu jest (obok szeregu geometrycznego) szczególnie użyteczna w samym [teście porównawczym](#test-porownawczy), dlatego celowo umieszczam ją wcześniej.

### Dowód
#### i) Gdy $p>1$
Całka

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

jest zbieżna, więc na mocy [kryterium całkowego](#test-calkowy) szereg $\sum \cfrac{1}{n^p}$ także jest zbieżny.

#### ii) Gdy $p\leq 1$
W tym przypadku

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Ponieważ wiemy, że szereg harmoniczny $\sum \cfrac{1}{n}$ jest rozbieżny, to z [testu porównawczego](#test-porownawczy) wynika, że $\sum \cfrac{1}{n^p}$ również jest rozbieżny.

#### Wniosek
Z punktów i), ii) wynika, że $p$-szereg $\sum \cfrac{1}{n^p}$ jest zbieżny dla $p>1$ i rozbieżny dla $p \leq 1$. $\blacksquare$

## Test porównawczy
Przy rozstrzyganiu zbieżności/rozbieżności szeregu o wyrazach nieujemnych, czyli **szeregu o wyrazach dodatnich (series of positive terms)**, użyteczny jest **test porównawczy (Comparison Test)** autorstwa Jakoba Bernoulliego.

Ponieważ szereg o wyrazach dodatnich $\sum a_n$ ma sumy częściowe tworzące ciąg rosnący, to jeśli nie jest rozbieżny do nieskończoności ($\sum a_n = \infty$), musi być zbieżny. Dlatego w przypadku szeregu o wyrazach dodatnich zapis

$$ \sum a_n < \infty $$

oznacza po prostu, że jest on <u>zbieżny</u>.

> **Test porównawczy (Comparison Test)**  
> Gdy $0 \leq a_n \leq b_n$,  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

W szczególności, wśród szeregów o wyrazach dodatnich takich jak $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$ itp. — czyli mających postać podobną do omawianych wcześniej szeregu geometrycznego $\sum ar^{n-1}$ lub $p$-szeregu $\sum \cfrac{1}{n^p}$ — warto aktywnie próbować właśnie testu porównawczego.

Wiele innych kryteriów zbieżności/rozbieżności można wyprowadzić z **testu porównawczego**; w tym sensie jest to najważniejsze z nich.

### Test porównawczy graniczny
Dla szeregów o wyrazach dodatnich $\sum a_n$ i $\sum b_n$ załóżmy, że w ilorazie $a_n/b_n$ dominujące składniki (dominant term) w liczniku i mianowniku się redukują, tak że $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ jest skończoną liczbą dodatnią)}$. Jeśli znamy zbieżność/rozbieżność szeregu $\sum b_n$, możemy zastosować poniższy **test porównawczy graniczny (Limit Comparison Test)**.

> **Test porównawczy graniczny (Limit Comparison Test)**  
> Jeśli
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ jest skończoną liczbą dodatnią)}$$
>
> to oba szeregi $\sum a_n$ i $\sum b_n$ albo są zbieżne, albo oba są rozbieżne. Tzn. $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Kryterium pierwiastkowe
> **Twierdzenie**  
> Dla szeregu o wyrazach dodatnich $\sum a_n$ oraz dodatniej liczby $\epsilon < 1$  
> - jeśli dla każdego $n$ zachodzi $\sqrt[n]{a_n}< 1-\epsilon$, to szereg $\sum a_n$ jest zbieżny
> - jeśli dla każdego $n$ zachodzi $\sqrt[n]{a_n}> 1+\epsilon$, to szereg $\sum a_n$ jest rozbieżny
{: .prompt-info }

> **Wniosek: kryterium pierwiastkowe (Root Test)**  
> Załóżmy, że dla szeregu o wyrazach dodatnich $\sum a_n$ istnieje granica
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> Wtedy
> - jeśli $r<1$, to szereg $\sum a_n$ jest zbieżny
> - jeśli $r>1$, to szereg $\sum a_n$ jest rozbieżny
{: .prompt-info }

> W powyższym wniosku przypadek $r=1$ nie pozwala rozstrzygnąć zbieżności/rozbieżności, więc trzeba użyć innych metod.
{: .prompt-warning }

## Kryterium ilorazowe
> **Kryterium ilorazowe (Ratio Test)**  
> Dla dodatniego ciągu $(a_n)$ oraz $0 < r < 1$
> - jeśli dla każdego $n$ zachodzi $a_{n+1}/a_n \leq r$, to szereg $\sum a_n$ jest zbieżny
> - jeśli dla każdego $n$ zachodzi $a_{n+1}/a_n \geq 1$, to szereg $\sum a_n$ jest rozbieżny
{: .prompt-info }

> **Wniosek**  
> Załóżmy, że dla dodatniego ciągu $(a_n)$ istnieje granica $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$. Wtedy
> - jeśli $\rho < 1$, to szereg $\sum a_n$ jest zbieżny
> - jeśli $\rho > 1$, to szereg $\sum a_n$ jest rozbieżny
{: .prompt-info }

## Kryterium całkowe
Za pomocą całek można rozstrzygać zbieżność/rozbieżność szeregu utworzonego z dodatnich wyrazów ciągu malejącego.

> **Kryterium całkowe (Integral Test)**  
> Gdy funkcja ciągła $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ jest malejąca i zawsze $f(x)>0$, to warunkiem koniecznym i wystarczającym zbieżności szeregu $\sum f(n)$ jest zbieżność całki
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> .
{: .prompt-info }

### Dowód
Ponieważ $f(x)$ jest funkcją ciągłą i malejącą oraz zawsze dodatnią, zachodzi nierówność

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

Sumując stronami tę nierówność od $n=1$ do dowolnego wyrazu, otrzymujemy

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Teraz, stosując [test porównawczy](#test-porownawczy), dostajemy żądany wynik. $\blacksquare$

## Szereg naprzemienny
Szereg $\sum a_n$, w którym wyraz ogólny jest niezerowy, a znaki kolejnych wyrazów $a_n$ i $a_{n+1}$ są różne (tzn. wyrazy dodatnie i ujemne występują na przemian), nazywa się **szeregiem naprzemiennym (alternating series)**.

Dla szeregu naprzemiennego można z pożytkiem użyć następującego twierdzenia odkrytego przez niemieckiego matematyka Gottfrieda Wilhelma Leibniza.

> **Kryterium Leibniza dla szeregu naprzemiennego (Alternating Series Test)**  
> Jeśli
> 1. dla każdego $n$ wyrazy $a_n$ i $a_{n+1}$ mają różne znaki,
> 2. dla każdego $n$ zachodzi $\|a_n\| \geq \|a_{n+1}\|$,
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> to szereg naprzemienny $\sum a_n$ jest zbieżny.
{: .prompt-info }

## Szeregi zbieżne bezwzględnie
Dla szeregu $\sum a_n$ mówimy, że „szereg $\sum a_n$ jest **zbieżny bezwzględnie** (converge absolutely)”, jeśli szereg $\sum \|a_n\|$ jest zbieżny.

Wtedy zachodzi następujące twierdzenie.

> **Twierdzenie**  
> Szereg zbieżny bezwzględnie jest zbieżny.
{: .prompt-info }

> Odwrotność powyższego twierdzenia nie zachodzi.  
> Jeśli szereg jest zbieżny, ale nie jest zbieżny bezwzględnie, to mówimy, że jest „**zbieżny warunkowo** (converge conditionally)”.
{: .prompt-warning }

### Dowód
Dla liczby rzeczywistej $a$ zdefiniujmy

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Wtedy

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Ponieważ $0 \leq a^\pm \leq \|a\|$, to na mocy [testu porównawczego](#test-porownawczy), jeżeli szereg $\sum \|a_n\|$ jest zbieżny, to oba szeregi $\sum a_n^+$ oraz $\sum a_n^-$ również są zbieżne. W konsekwencji, na mocy [podstawowych własności szeregów zbieżnych](/posts/sequences-and-series/#podstawowe-wlasnosci-zbieznych-szeregow),

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

też jest zbieżny. $\blacksquare$
