---
title: Cząstka swobodna (The Free Particle)
description: Dla cząstki swobodnej z V(x)=0 nie da się znormalizować rozwiązań z rozdzielenia zmiennych. Omawiamy sens fizyczny, relację nieoznaczoności x–p oraz prędkości fazową i grupową Ψ(x,t).
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Cząstka swobodna: $V(x)=0$, brak warunków brzegowych (dowolna energia)
> - Rozwiązanie z rozdzielenia zmiennych $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ po scałkowaniu kwadratu rozbiega do nieskończoności, więc nie da się go znormalizować, co sugeruje:
>   - cząstka swobodna nie może istnieć jako stan stacjonarny
>   - cząstka swobodna nie może mieć energii zdefiniowanej dokładnie jedną wartością (istnieje nieoznaczoność energii)
> - Mimo to rozwiązanie ogólne zależnego od czasu równania Schrödingera jest kombinacją liniową rozwiązań z rozdzielenia zmiennych, więc te rozwiązania nadal mają istotne znaczenie matematyczne. Ponieważ nie ma tu ograniczeń, rozwiązanie ogólne ma postać całki ($\int$) po zmiennej ciągłej $k$, a nie sumy ($\sum$) po zmiennej dyskretnej $n$.
> - Rozwiązanie ogólne równania Schrödingera:
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{gdzie }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - Zależność między nieoznaczonością położenia i pędu:
>   - gdy nieoznaczoność położenia maleje, nieoznaczoność pędu rośnie; odwrotnie, gdy nieoznaczoność pędu maleje, nieoznaczoność położenia rośnie
>   - tzn. w mechanice kwantowej nie da się jednocześnie znać dokładnie położenia i pędu cząstki swobodnej
> - Prędkość fazowa i grupowa funkcji falowej $\Psi(x,t)$:
>   - prędkość fazowa: $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - prędkość grupowa: $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - Sens fizyczny prędkości grupowej i porównanie z mechaniką klasyczną:
>   - fizycznie prędkość grupowa odpowiada prędkości ruchu cząstki
>   - gdy $\phi(k)$ jest bardzo „ostra” w pobliżu pewnej wartości $k_0$ (gdy nieoznaczoność pędu jest dostatecznie mała),
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Wymagania wstępne
- wzór Eulera
- transformata Fouriera (Fourier transform) i twierdzenie Plancherela (Plancherel's theorem)
- [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/)
- [Równanie Schrödingera niezależne od czasu](/posts/time-independent-schrodinger-equation/)
- [1-wymiarowa nieskończona studnia potencjału](/posts/the-infinite-square-well/)

## Ustawienie modelu
Rozważmy najprostszy przypadek: cząstkę swobodną ($V(x)=0$). Klasycznie jest to po prostu ruch jednostajny, ale w mechanice kwantowej problem robi się ciekawszy.  
[Równanie Schrödingera niezależne od czasu](/posts/time-independent-schrodinger-equation/) dla cząstki swobodnej ma postać

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

czyli

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, gdzie }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[Do tego miejsca jest to identyczne jak wnętrze nieskończonej studni kwadratowej o potencjale $0$](/posts/the-infinite-square-well/#model-i-warunki-brzegowe). Tyle że tym razem zapiszmy rozwiązanie ogólne w postaci wykładniczej:

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ oraz $C\cos{kx}+D\sin{kx}$ to równoważne sposoby zapisu tej samej funkcji zmiennej $x$. Z wzoru Eulera $e^{ix}=\cos{x}+i\sin{x}$ wynika
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> Zatem, gdy przyjmiemy $C=A+B$ oraz $D=i(A-B)$, to
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> Odwrotnie, wyrażając $A$ i $B$ przez $C$ i $D$, dostajemy $A=\cfrac{C-iD}{2}$, $B=\cfrac{C+iD}{2}$.
>
> W mechanice kwantowej przy $V=0$ funkcje wykładnicze opisują falę biegnącą i są najwygodniejsze przy analizie cząstki swobodnej. Z kolei funkcje sinus i cosinus łatwo opisują falę stojącą i naturalnie pojawiają się w nieskończonej studni kwadratowej.
{: .prompt-info }

W odróżnieniu od nieskończonej studni kwadratowej, tym razem nie ma warunków brzegowych ograniczających $k$ i $E$. To znaczy: cząstka swobodna może mieć dowolną dodatnią energię.

## Rozwiązanie z rozdzielenia zmiennych i prędkość fazowa
Jeśli do $\psi(x)$ dołączymy zależność czasową $e^{-iEt/\hbar}$, to dostajemy

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

W ogólności dowolna funkcja $x$ i $t$ zależna od szczególnej postaci $(x\pm vt)$ opisuje falę, która nie zmienia kształtu i porusza się z prędkością $v$ w kierunku $\mp x$. Zatem pierwszy wyraz w ($\ref{eqn:Psi_seperated_solution}$) opisuje falę biegnącą w prawo, a drugi — falę o tej samej długości i prędkości fazowej, lecz o innej amplitudzie, biegnącą w lewo. Ponieważ różnią się jedynie znakiem przy $k$, możemy pisać

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

a kierunek propagacji w zależności od znaku $k$ jest następujący:

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{ruch w prawo}, \\
k<0 \Rightarrow & \text{ruch w lewo}.
\end{cases} \tag{6}$$

„Stan stacjonarny” cząstki swobodnej jest ewidentnie falą biegnącą*, o długości $\lambda = 2\pi/\|k\|$, a ze wzoru de Broglie’a (de Broglie formula) wynika, że ma pęd

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

> *„Stan stacjonarny”, a jednak fala biegnąca — fizycznie to oczywista sprzeczność. Powód zaraz się pojawi.
{: .prompt-info }

Ponadto prędkość tej fali wynosi

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(tutaj $\omega$ to współczynnik przy $t$, czyli $\cfrac{\hbar k^2}{2m}$.)

Jednak tej funkcji falowej nie da się znormalizować, bo po scałkowaniu kwadratu rozbiega do nieskończoności:

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

Czyli <u>dla cząstki swobodnej rozwiązanie z rozdzielenia zmiennych nie jest fizycznie dopuszczalnym stanem.</u> Cząstka swobodna nie może istnieć jako [stan stacjonarny](/posts/time-independent-schrodinger-equation/#1-stany-stacjonarne-stationary-states) ani nie może mieć [jednej, ściśle określonej wartości energii](/posts/time-independent-schrodinger-equation/#2-stan-majacy-jedna-jednoznacznie-okreslona-wartosc-calkowitej-energii-e-a-nie-rozklad-prawdopodobienstwa-o-pewnym-zakresie). Zresztą intuicyjnie: skoro na obu końcach nie ma żadnych warunków brzegowych, to bardziej „dziwne” byłoby właśnie to, gdyby powstawała fala stojąca.

## Wyznaczenie rozwiązania ogólnego $\Psi(x,t)$ dla zależnego od czasu równania Schrödingera
Mimo to to rozwiązanie z rozdzielenia zmiennych nadal ma ważne znaczenie: niezależnie od interpretacji fizycznej, [rozwiązanie ogólne zależnego od czasu równania Schrödingera jest kombinacją liniową rozwiązań z rozdzielenia zmiennych](/posts/time-independent-schrodinger-equation/#3-ogolne-rozwiazanie-rownania-schrodingera-zaleznego-od-czasu-jest-kombinacja-liniowa-rozwiazan-z-metody-rozdzielenia-zmiennych). Ponieważ w tym przypadku nie ma ograniczeń, rozwiązanie ogólne ma postać całki ($\int$) po zmiennej ciągłej $k$, zamiast sumy ($\sum$) po zmiennej dyskretnej $n$:

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> Tutaj $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ pełni tę samą rolę co $c_n$ w [równaniu (21) z posta „Równanie Schrödingera niezależne od czasu”](/posts/time-independent-schrodinger-equation/#3-ogolne-rozwiazanie-rownania-schrodingera-zaleznego-od-czasu-jest-kombinacja-liniowa-rozwiazan-z-metody-rozdzielenia-zmiennych).
{: .prompt-info }

Tę funkcję falową można znormalizować dla odpowiedniego $\phi(k)$, ale wtedy musi istnieć pewien zakres wartości $k$, a więc i zakres energii oraz prędkości. Nazywa się to **pakietem falowym (wave packet)**.

> Fala sinusoidalna jest nieskończenie rozciągnięta w przestrzeni, więc nie da się jej znormalizować. Jednak superpozycja wielu takich fal może — na skutek interferencji — ulec lokalizacji i stać się normalizowalna.
{: .prompt-info }

## Wyznaczenie $\phi(k)$ z twierdzenia Plancherela (Plancherel theorem)

Skoro znamy postać $\Psi(x,t)$ (równanie [$\ref{eqn:Psi_general_solution}$]), to pozostaje jedynie wyznaczyć $\phi(k)$ spełniające warunek na początkową funkcję falową:

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

Jest to typowy problem analizy Fouriera (Fourier analysis), a odpowiedź daje **twierdzenie Plancherela (Plancherel's theorem)**:

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

$F(k)$ nazywa się **transformatą Fouriera (Fourier transform)** funkcji $f(x)$, a $f(x)$ — **odwrotną transformatą Fouriera (inverse Fourier transform)** funkcji $F(k)$. Z ($\ref{eqn:plancherel_theorem}$) łatwo widać, że różnią się tylko znakiem w wykładniku. Oczywiście istnieje ograniczenie: dopuszczalne są tylko takie funkcje, dla których całka istnieje.

> Warunkiem koniecznym i wystarczającym istnienia $f(x)$ jest to, aby $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ było skończone. Wtedy $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ także jest skończone oraz zachodzi
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> Czasem to właśnie powyższe równanie (a nie ($\ref{eqn:plancherel_theorem}$)) nazywa się twierdzeniem Plancherela (tak jest to opisane również w [Wikipedii](https://en.wikipedia.org/wiki/Plancherel_theorem)).
{: .prompt-info }

W naszym przypadku z fizycznego warunku normalizacji $\Psi(x,0)$ wynika, że odpowiednia całka musi istnieć. Zatem kwantowomechaniczne rozwiązanie dla cząstki swobodnej to ($\ref{eqn:Psi_general_solution}$), gdzie

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> W praktyce jednak rzadko da się analitycznie obliczyć całkę w ($\ref{eqn:Psi_general_solution}$). Zwykle wartości wyznacza się numerycznie na komputerze.
{: .prompt-tip }

## Obliczenie prędkości grupowej pakietu falowego i interpretacja fizyczna

W swej istocie pakiet falowy jest superpozycją bardzo wielu fal sinusoidalnych, których amplitudy wyznacza $\phi$. Innymi słowy: wewnątrz „obwiedni (envelope)” pakietu znajdują się „zmarszczki (ripples)”.

![A wave packet with the group velocity larger(5x) than phase velocity](/physics-visualizations/figs/wave_packet.webp)
> *Informacja o licencji obrazu i źródle oryginału*
> - kod źródłowy generowania obrazu (Python3): [yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/wave_packet.py)
> - kod źródłowy generowania obrazu (gnuplot): [yunseo-kim/physics-visualizations](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/wave_packet.plt)
> - licencja: [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)
> - autor oryginału: [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - oryginalna informacja o licencji: [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

Fizycznie prędkością cząstki nie jest prędkość pojedynczych „zmarszczek”, którą wyznaczyliśmy wcześniej w ($\ref{eqn:phase_velocity}$) (**prędkość fazowa, phase velocity**), lecz prędkość zewnętrznej obwiedni (**prędkość grupowa, group velocity**).

### Zależność między nieoznaczonością położenia i pędu
Spójrzmy na związek między nieoznaczonością położenia i nieoznaczonością pędu, wyodrębniając same części całkowe: $\int\phi(k)e^{ikx}dk$ z ($\ref{eqn:Psi_at_t_0}$) oraz $\int\Psi(x,0)e^{-ikx}dx$ z ($\ref{eqn:phi}$).

#### Gdy nieoznaczoność położenia jest mała
Jeśli w przestrzeni położeń $\Psi$ jest skupiona w bardzo wąskim obszarze wokół pewnej wartości $x_0$, tj. w przedziale $[x_0-\delta, x_0+\delta]$, a poza nim jest bliska 0 (<u>gdy nieoznaczoność położenia jest mała</u>), to $e^{-ikx} \approx e^{-ikx_0}$ jest prawie stałe względem $x$, zatem

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{eqn. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

Wyraz z całką oznaczoną jest stały względem $p$, więc przez czynnik $e^{-ipx_0/\hbar}$ funkcja $\phi$ przyjmuje w przestrzeni pędów postać sinusoidalną względem $p$, czyli rozkłada się na szeroki zakres pędów (<u>nieoznaczoność pędu jest duża</u>).

#### Gdy nieoznaczoność pędu jest mała
Analogicznie, jeśli w przestrzeni pędów $\phi$ jest skupiona w bardzo wąskim obszarze wokół pewnej wartości $p_0$, tj. w przedziale $[p_0-\delta, p_0+\delta]$, a poza nim jest bliska 0 (<u>gdy nieoznaczoność pędu jest mała</u>), to na mocy ($\ref{eqn:de_broglie_formula}$) mamy $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ (prawie stałe względem $p$), oraz $dk=\frac{1}{\hbar}dp$, więc

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

Przez czynnik $e^{ip_0x/\hbar}$ funkcja $\Psi$ w przestrzeni położeń przyjmuje postać sinusoidalną względem $x$, czyli rozkłada się na szeroki zakres położeń (<u>nieoznaczoność położenia jest duża</u>).

#### Wniosek
Gdy nieoznaczoność położenia maleje, nieoznaczoność pędu rośnie; odwrotnie, gdy nieoznaczoność pędu maleje, nieoznaczoność położenia rośnie. Dlatego w mechanice kwantowej nie jest możliwe jednoczesne dokładne poznanie położenia i pędu cząstki swobodnej.

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *Źródło obrazu*
> - autor: użytkownik anglojęzycznej Wikipedii [Maschen](https://en.wikipedia.org/wiki/User:Maschen)
> - licencja: public domain

> W rzeczywistości, na mocy zasady nieoznaczoności (uncertainty principle), dotyczy to nie tylko cząstki swobodnej, ale wszystkich przypadków. Zasadę nieoznaczoności omówię w osobnym poście.
{: .prompt-info }

### Prędkość grupowa pakietu falowego
Jeśli w ($\ref{eqn:Psi_general_solution}$) podstawimy — jak w ($\ref{eqn:phase_velocity}$) — $\omega \equiv \cfrac{\hbar k^2}{2m}$, to

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> Zapis $\omega = \cfrac{\hbar k^2}{2m}$, czyli $\omega$ jako funkcja $k$, nazywa się **relacją dyspersji (dispersion relation)**. Poniższe rozumowanie stosuje się ogólnie do wszystkich pakietów falowych, niezależnie od konkretnej relacji dyspersji.
{: .prompt-info }

Załóżmy teraz, że $\phi(k)$ ma bardzo ostry kształt w pobliżu pewnej wartości $k_0$. (Można dopuścić też szeroki rozkład po $k$, ale wtedy pakiet bardzo szybko się „rozmywa” i zmienia postać. Składowe o różnych $k$ poruszają się z różnymi prędkościami, więc cała „grupa” przestaje mieć dobrze zdefiniowaną prędkość; tzn. <u>rośnie nieoznaczoność pędu</u>.)  
Ponieważ wkład spoza okolic $k_0$ można zaniedbać, możemy rozwinąć $\omega(k)$ w szereg Taylora wokół $k_0$ i zatrzymać się na wyrazie liniowym:

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

Podstawiając $s=k-k_0$ i całkując względem środka $k_0$, dostajemy

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

Czynnik $e^{i(k_0x-\omega_0t)}$ z przodu opisuje falę sinusoidalną („zmarszczki”) poruszającą się z prędkością $\omega_0/k_0$, natomiast całka (opisująca „obwiednię”, czyli amplitudę tej fali) porusza się — przez składnik $e^{is(x-\omega_0^\prime t)}$ — z prędkością $\omega_0^\prime$. Zatem prędkość fazowa w punkcie $k=k_0$ wynosi

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

co zgadza się z ($\ref{eqn:phase_velocity}$), a prędkość grupowa to

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

czyli jest dwukrotnie większa od prędkości fazowej.

## Porównanie z mechaniką klasyczną

Wiemy, że w skali makro obowiązuje mechanika klasyczna, więc wynik z mechaniki kwantowej powinien przechodzić w wynik klasyczny, gdy nieoznaczoności kwantowe są dostatecznie małe. Dla cząstki swobodnej oznacza to, że gdy $\phi(k)$ jest bardzo ostra w pobliżu pewnego $k_0$ (tzn. <u>gdy nieoznaczoność pędu jest dostatecznie mała</u>), to prędkość grupowa $v_\text{group}$ (odpowiadająca prędkości cząstki w opisie kwantowym) powinna być równa prędkości klasycznej $v_\text{classical}$ dla tej samej wartości $k$ i odpowiadającej jej energii $E$.

Podstawiając $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ z ($\ref{eqn:t_independent_schrodinger_eqn}$) do wyznaczonej przed chwilą prędkości grupowej (równanie [$\ref{eqn:group_velocity}$]), dostajemy

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

a w mechanice klasycznej prędkość cząstki swobodnej o energii kinetycznej $E$ również wynosi

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

Zatem $v_\text{quantum}=v_\text{classical}$, co potwierdza, że otrzymany wynik jest fizycznie sensowny.
