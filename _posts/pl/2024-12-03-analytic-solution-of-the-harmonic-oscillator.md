---
title: Analityczne rozwiązanie oscylatora harmonicznego (The Harmonic Oscillator)
description: Wyprowadzamy równanie Schrödingera dla kwantowego oscylatora harmonicznego i przedstawiamy analityczną metodę rozwiązania z bezwymiarową zmienną ξ oraz wielomianami Hermite’a.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hermite Polynomials]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Jeśli amplituda jest dostatecznie mała, dowolne drgania można przybliżyć jako drgania harmoniczne proste (simple harmonic oscillation); dlatego drgania harmoniczne proste mają w fizyce duże znaczenie
> - Oscylator harmoniczny: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - Wprowadzamy bezwymiarową zmienną $\xi$ oraz energię $K$ wyrażoną w jednostkach $\cfrac{1}{2}\hbar\omega$:
>   - $\xi \equiv \sqrt{\cfrac{m\omega}{\hbar}}x$
>   - $K \equiv \cfrac{2E}{\hbar\omega}$
>   - $ \cfrac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi $
> - Gdy $\|\xi\|^2 \to \infty$, fizycznie dopuszczalne rozwiązanie asymptotyczne ma postać $\psi(\xi) \to Ae^{-\xi^2/2}$, zatem
>
> $$ \begin{gather*}
> \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(przy czym }\lim_{\xi\to\infty}h(\xi)=A\text{)}, \\
> \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0
> \end{gather*} $$
>
> - Jeśli rozwiązanie powyższego równania zapiszemy w postaci szeregu $ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j$, to
>
> $$ a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j $$
>
> - Aby rozwiązanie było znormalizowane, szereg $\sum a_j$ musi być skończony, tj. musi istnieć pewna „największa” wartość $j$ równa $n\in \mathbb{N}$, taka że dla $j>n$ mamy $a_j=0$, więc
>   - $ K = 2n + 1 $
>   - $ E_n = \left(n+\cfrac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots $
> - Ogólnie $h_n(\xi)$ jest wielomianem $n$-tego stopnia w $\xi$, a część poza współczynnikiem wiodącym ($a_0$ lub $a_1$) nazywa się **wielomianem Hermite’a (Hermite polynomials)** $H_n(\xi)$
>
> $$ h_n(\xi) = 
> \begin{cases}
> a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
> a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
> \end{cases} $$
>
> - Znormalizowane stany stacjonarne oscylatora harmonicznego:
>
> $$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2} $$
>
> - Cechy oscylatora kwantowego
>   - Funkcje własne na przemian są parzyste i nieparzyste
>   - Prawdopodobieństwo znalezienia cząstki nie jest równe $0$ nawet w obszarach klasycznie niedostępnych (tj. dla $x$ większych niż klasyczna amplituda dla danego $E$); jest ono małe, ale niezerowe
>   - Dla wszystkich stanów stacjonarnych o nieparzystym $n$ prawdopodobieństwo znalezienia cząstki w centrum wynosi $0$
>   - Im większe $n$, tym zachowanie bardziej przypomina klasyczny oscylator
{: .prompt-info }

## Wymagania wstępne
- [Metoda rozdzielenia zmiennych](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/)
- [Twierdzenie Ehrenfesta](/posts/ehrenfest-theorem/)
- [Niezależne od czasu równanie Schrödingera](/posts/time-independent-schrodinger-equation/)
- [Jednowymiarowa nieskończona studnia kwadratowa](/posts/the-infinite-square-well/)
- [Algebraiczne rozwiązanie oscylatora harmonicznego](/posts/algebraic-solution-of-the-harmonic-oscillator/)

## Ustalenie modelu
Sposób opisu oscylatora harmonicznego w mechanice klasycznej oraz znaczenie tego zagadnienia omówiono w [poprzednim wpisie](/posts/algebraic-solution-of-the-harmonic-oscillator/).

### Oscylator harmoniczny w mechanice kwantowej
Zagadnienie kwantowego oscylatora harmonicznego polega na rozwiązaniu równania Schrödingera dla potencjału

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{1}$$

[Równanie Schrödingera niezależne od czasu](/posts/time-independent-schrodinger-equation/) dla oscylatora harmonicznego ma postać

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

Istnieją dwa zupełnie różne podejścia do rozwiązania tego problemu. Pierwsze to analityczna metoda (analytic method) wykorzystująca **szereg potęgowy (power series)**, drugie to metoda algebraiczna (algebraic method) wykorzystująca **operatory drabinkowe (ladder operators)**. Metoda algebraiczna jest szybsza i prostsza, jednak warto też przestudiować rozwiązanie analityczne oparte o szereg potęgowy. [Wcześniej omówiliśmy metodę algebraiczną](/posts/algebraic-solution-of-the-harmonic-oscillator/); tutaj zajmiemy się metodą analityczną.

## Przekształcenie równania Schrödingera
Wprowadzając bezwymiarową zmienną

$$ \xi \equiv \sqrt{\frac{m\omega}{\hbar}}x \label{eqn:xi}\tag{3}$$

możemy zapisać niezależne od czasu równanie Schrödingera ($\ref{eqn:t_independent_schrodinger_eqn}$) w prostszej postaci

$$ \frac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi. \label{eqn:schrodinger_eqn_with_xi}\tag{4}$$

gdzie $K$ jest energią wyrażoną w jednostkach $\cfrac{1}{2}\hbar\omega$:

$$ K \equiv \frac{2E}{\hbar\omega}. \label{eqn:K}\tag{5}$$

Teraz wystarczy rozwiązać równanie przepisane w tej postaci ($\ref{eqn:schrodinger_eqn_with_xi}$). Dla bardzo dużych $\xi$ (tj. bardzo dużych $x$) mamy $\xi^2 \gg K$, więc

$$ \frac{d^2\psi}{d\xi^2} \approx \xi^2\psi \label{eqn:schrodinger_eqn_approx}\tag{6}$$

a przybliżone rozwiązanie ma postać

$$ \psi(\xi) \approx Ae^{-\xi^2/2} + Be^{\xi^2/2} \label{eqn:psi_approx}\tag{7}$$

Jednak składnik z $B$ rozbiega się przy $\|x\|\to \infty$ i nie da się go znormalizować, więc fizycznie dopuszczalne rozwiązanie asymptotyczne to

$$ \psi(\xi) \to Ae^{-\xi^2/2} \label{eqn:psi_asymp}\tag{8}$$

Wydzielmy teraz część wykładniczą i zapiszmy

$$ \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(przy czym }\lim_{\xi\to\infty}h(\xi)=A\text{)} \label{eqn:psi_and_h}\tag{9}$$

> Aby znaleźć czynnik wykładniczy $e^{-\xi^2/2}$, w trakcie wyprowadzenia użyliśmy przybliżeń, by odgadnąć postać rozwiązania asymptotycznego. Jednak otrzymany w ten sposób zapis ($\ref{eqn:psi_and_h}$) nie jest przybliżeniem, tylko dokładną postacią rozwiązania. Tego typu wydzielenie zachowania asymptotycznego jest standardowym pierwszym krokiem przy rozwiązywaniu równań różniczkowych metodą szeregu potęgowego.
{: .prompt-info }

Różniczkując ($\ref{eqn:psi_and_h}$) i wyznaczając $\cfrac{d\psi}{d\xi}$ oraz $\cfrac{d^2\psi}{d\xi^2}$, otrzymujemy

$$ \begin{gather*}
\frac{d\psi}{d\xi} = \left(\frac{dh}{d\xi}-\xi h \right)e^{-\xi^2/2}, \\
\frac{d^2\psi}{d\xi^2} = \left(\frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(\xi^2-1)h \right)e^{-\xi^2/2}
\end{gather*} $$

Zatem równanie Schrödingera ($\ref{eqn:schrodinger_eqn_with_xi}$) przyjmuje postać

$$ \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0 \label{eqn:schrodinger_eqn_with_h}\tag{10}$$

## Rozwinięcie w szereg potęgowy
Z twierdzenia Taylora (Taylor's theorem) wynika, że dowolną gładką funkcję można przedstawić jako szereg potęgowy, więc poszukajmy rozwiązania równania ($\ref{eqn:schrodinger_eqn_with_h}$) w postaci szeregu względem $\xi$:

$$ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j \label{eqn:h_series_exp}\tag{11}$$

Różniczkując kolejne wyrazy tego szeregu, dostajemy:

$$ \begin{gather*}
\frac{dh}{d\xi} = a_1 + 2a_2\xi + 3a_3\xi^2 + \cdots = \sum_{j=0}^{\infty}ja_j\xi^{j-1}, \\
\frac{d^2 h}{d\xi^2} = 2a_2 + 2\cdot3a_3\xi + 3\cdot4a_4\xi^2 + \cdots = \sum_{j=0}^{\infty} (j+1)(j+2)a_{j+2}\xi^j.
\end{gather*} $$

Podstawiając te wyrażenia do równania Schrödingera (równanie [$\ref{eqn:schrodinger_eqn_with_h}$]), otrzymujemy

$$ \sum_{j=0}^{\infty}[(j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j]\xi^j = 0. \label{eqn:schrodinger_eqn_power_series}\tag{12}$$

Z jednoznaczności rozwinięcia w szereg potęgowy wynika, że współczynnik przy każdej potędze $\xi$ musi być równy $0$, więc

$$ (j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j = 0 $$

$$ \therefore a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j. \label{eqn:recursion_formula}\tag{13}$$

Ta **formuła rekurencyjna (recursion formula)** jest równoważna równaniu Schrödingera. Gdy dane są dwie dowolne stałe $a_0$ oraz $a_1$, można wyznaczyć współczynniki wszystkich wyrazów rozwiązania $h(\xi)$.

Jednak nie zawsze da się znormalizować rozwiązanie otrzymane w ten sposób. Jeśli szereg $\sum a_j$ jest nieskończony (tj. gdy $\lim_{j\to\infty} a_j\neq0$), to dla bardzo dużych $j$ formuła rekurencyjna w przybliżeniu daje

$$ a_{j+2} \approx \frac{2}{j}a_j $$

a przybliżone rozwiązanie ma postać

$$ a_j \approx \frac{C}{(j/2)!} \quad \text{(}C\text{ jest dowolną stałą)}$$

Wtedy dla dużych wartości $\xi$, gdzie dominują wyrazy wysokiego rzędu,

$$ h(\xi) \approx C\sum\frac{1}{(j/2)!}\xi^j \approx C\sum\frac{1}{j!}\xi^{2j} \approx Ce^{\xi^2} $$

Zatem jeśli $h(\xi)$ zachowuje się jak $Ce^{\xi^2}$, to z ($\ref{eqn:psi_and_h}$) wynika, że $\psi(\xi)$ ma postać $Ce^{\xi^2/2}$ i rozbiega się dla $\xi \to \infty$. Odpowiada to nienormalizowalnemu rozwiązaniu z ($\ref{eqn:psi_approx}$) o własnościach $A=0, B\neq0$.

Dlatego szereg $\sum a_j$ musi być skończony. Musi istnieć pewna „największa” wartość $j$ równa $n\in \mathbb{N}$ taka, że dla $j>n$ mamy $a_j=0$. Aby tak było, dla niezerowego $a_n$ musi zachodzić $a_{n+2}=0$, więc z ($\ref{eqn:recursion_formula}$) wynika warunek

$$ K = 2n + 1 $$

Podstawiając to do ($\ref{eqn:K}$), otrzymujemy fizycznie dopuszczalne energie

$$ E_n = \left(n+\frac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots \label{eqn:E_n}\tag{14}$$

W ten sposób, stosując zupełnie inną metodę, uzyskaliśmy dokładnie ten sam warunek kwantyzacji energii co w równaniu (21) we wpisie [Algebraiczne rozwiązanie oscylatora harmonicznego](/posts/algebraic-solution-of-the-harmonic-oscillator/#stany-stacjonarne-psi_n-i-poziomy-energii-e_n).

## Wielomiany Hermite’a (Hermite polynomials) $H_n(\xi)$ i stany stacjonarne $\psi_n(x)$
### Wielomiany Hermite’a $H_n$
Ogólnie $h_n(\xi)$ jest wielomianem $n$-tego stopnia w $\xi$; jeśli $n$ jest parzyste, zawiera tylko parzyste potęgi, a jeśli $n$ jest nieparzyste, tylko nieparzyste. Część poza współczynnikiem wiodącym ($a_0$ lub $a_1$) nazywamy **wielomianem Hermite’a (Hermite polynomials)** $H_n(\xi)$.

$$ h_n(\xi) = 
\begin{cases}
a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
\end{cases} $$

Tradycyjnie współczynniki dobiera się tak, aby współczynnik przy najwyższej potędze w $H_n$ był równy $2^n$.

Poniżej podano kilka pierwszych wielomianów Hermite’a:

$$ \begin{align*}
H_0 &= 1 \\
H_1 &= 2\xi \\
H_2 &= 4\xi^2 - 2 \\
H_3 &= 8\xi^3 - 12\xi \\
H_4 &= 16\xi^4 - 48\xi^2 + 12 \\
H_5 &= 32\xi^5 - 160\xi^3 + 120\xi \\
&\qquad\vdots
\end{align*} $$

### Stany stacjonarne $\psi_n(x)$
Znormalizowane stany stacjonarne oscylatora harmonicznego mają postać

$$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2}. $$

Jest to zgodne z wynikiem uzyskanym we wpisie [Algebraiczne rozwiązanie oscylatora harmonicznego](/posts/algebraic-solution-of-the-harmonic-oscillator/#normalizacja) (równanie [27]).

Poniższa ilustracja przedstawia stany stacjonarne $\psi_n(x)$ oraz gęstości prawdopodobieństwa $\|\psi_n(x)\|^2$ dla pierwszych ośmiu wartości $n$. Widać, że funkcje własne oscylatora kwantowego na przemian są parzyste i nieparzyste.

![Wavefunction representations for the first eight bound eigenstates, n = 0 to 7. The horizontal axis shows the position x.](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)
> *Źródło obrazu*
> - Autor: użytkownik Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)

![Corresponding probability densities.](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)
> *Źródło obrazu*
> - Autor: użytkownik Wikimedia [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - Licencja: Public Domain

Oscylator kwantowy istotnie różni się od odpowiadającego mu oscylatora klasycznego: nie tylko energia jest skwantowana, ale również rozkład prawdopodobieństwa położenia $x$ wykazuje osobliwe własności.
- Prawdopodobieństwo znalezienia cząstki nie jest równe $0$ nawet w obszarach klasycznie niedostępnych (tj. dla $x$ większych niż klasyczna amplituda dla danego $E$); jest ono małe, ale niezerowe
- Dla wszystkich stanów stacjonarnych o nieparzystym $n$ prawdopodobieństwo znalezienia cząstki w centrum wynosi $0$

Im większe $n$, tym oscylator kwantowy upodabnia się do oscylatora klasycznego. Poniższy rysunek przedstawia klasyczny rozkład prawdopodobieństwa położenia $x$ (linia przerywana) oraz stan kwantowy $\|\psi_{30}\|^2$ (linia ciągła) dla $n=30$. Jeśli „wygładzimy” pofalowane fragmenty, oba wykresy są w przybliżeniu zgodne.

![Quantum (solid) and classical (dashed) probability distributions of the n = 30 excited state of the quantum harmonic oscillator. The vertical dashed lines represent the classical turning points.](https://upload.wikimedia.org/wikipedia/commons/6/69/QHOn30pdf.svg)
> *Źródło obrazu*
> - Autor: użytkownik Wikimedia [AkanoToE](https://commons.wikimedia.org/wiki/User:AkanoToE)
> - Licencja: Public Domain

### Interaktywna wizualizacja rozkładów prawdopodobieństwa oscylatora kwantowego
Poniżej znajduje się responsywna wizualizacja oparta o Plotly.js, którą przygotowałem. Za pomocą suwaka można zmieniać wartość $n$ i obserwować kształt klasycznego rozkładu prawdopodobieństwa położenia $x$ oraz $\|\psi_n\|^2$.

<div class="plotly-iframe-container" style="position: relative; height: 850px; overflow: hidden;">
    <iframe id="plotly-iframe"
            src="/physics-visualizations/quantum-harmonic-oscillator.html"
            title="Kwantowy oscylator harmoniczny: gęstość prawdopodobieństwa"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; overflow:hidden" 
            allow="fullscreen"
            scrolling="no"
            loading="lazy">
    </iframe>
</div>

> - Strona oryginalnej wizualizacji: <a {% static_href %}href="{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html"{% endstatic_href %}>{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html</a>
> - Kod źródłowy: repozytorium [yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/quantum-harmonic-oscillator.html)
> - Licencja: [See here](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

Dodatkowo, jeśli możesz uruchamiać Pythona na swoim komputerze i masz zainstalowane biblioteki Numpy, Plotly oraz Dash, to możesz też uruchomić skrypt Pythona [`/src/quantum_oscillator.py`{: .filepath}](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/quantum_oscillator.py) w tym samym repozytorium, aby zobaczyć wyniki.
