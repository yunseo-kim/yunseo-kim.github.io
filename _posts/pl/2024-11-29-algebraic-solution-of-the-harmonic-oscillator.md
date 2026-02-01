---
title: Algebraiczne rozwiązanie oscylatora harmonicznego (The Harmonic Oscillator)
description: Wyprowadzamy równanie Schrödingera dla oscylatora harmonicznego w mechanice kwantowej i omawiamy jego algebraiczną metodę rozwiązania. Z komutatorów, kanonicznych relacji komutacyjnych oraz operatorów drabinkowych wyznaczamy funkcje falowe i poziomy energii dowolnych stanów stacjonarnych.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Jeśli amplituda jest dostatecznie mała, dowolne drgania można przybliżyć jako drgania harmoniczne proste (simple harmonic oscillation); dlatego drgania harmoniczne proste mają w fizyce duże znaczenie
> - Oscylator harmoniczny: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Komutator (commutator)**:
>   - Dwuargumentowa operacja opisująca, jak bardzo dwa operatory nie komutują (commute)
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Kanoniczna relacja komutacyjna (canonical commutation relation)**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Operatory drabinkowe (ladder operators)**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ nazywa się **operatorem podnoszącym (raising operator)**, a $\hat{a}\_-$ **operatorem opuszczającym (lowering operator)**
>   - Dla dowolnego stanu stacjonarnego można podnosić lub obniżać poziom energii; zatem wystarczy znaleźć jedno rozwiązanie niezależnego od czasu równania Schrödingera, aby otrzymać wszystkie pozostałe
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Funkcja falowa i poziom energii $n$-tego stanu stacjonarnego:
>   - Stan podstawowy (0-ty stan stacjonarny):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$-ty stan stacjonarny:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ jest **sprzężeniem hermitowskim (hermitian conjugate)** oraz **operatorem sprzężonym (adjoint operator)** do $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - Z tego można wyprowadzić następujące własności:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Metoda obliczania wartości oczekiwanych wielkości fizycznych zawierających potęgi $\hat{x}$ i $\hat{p}$:
>   1. Korzystając z definicji operatorów drabinkowych, wyrazić $\hat{x}$ i $\hat{p}$ przez operator podnoszący i opuszczający
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. Wyrazić interesującą wielkość fizyczną za pomocą powyższych wzorów na $\hat{x}$ i $\hat{p}$
>   3. Skorzystać z faktu, że $\left(\hat{a}\_\pm \right)^m$ jest proporcjonalne do $\psi\_{n\pm m}$, więc jest ortogonalne do $\psi_n$ i daje $0$
>   4. Wykonać obliczenia całkowe, korzystając z własności operatorów drabinkowych
{: .prompt-info }

## Wymagania wstępne
- [Metoda rozdzielenia zmiennych](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/)
- [Twierdzenie Ehrenfesta](/posts/ehrenfest-theorem/)
- [Niezależne od czasu równanie Schrödingera](/posts/time-independent-schrodinger-equation/)
- [Jednowymiarowa nieskończona studnia kwadratowa](/posts/the-infinite-square-well/)
- sprzężenie hermitowskie (hermitian conjugate), operator sprzężony (adjoint operator)

## Ustalenie modelu
### Oscylator harmoniczny w mechanice klasycznej
Typowym przykładem klasycznego oscylatora harmonicznego jest ruch (pomijamy tarcie) masy $m$ zawieszonej na sprężynie o stałej sprężystości $k$.
Ruch ten spełnia **prawo Hooke’a (Hooke's law)**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

Rozwiązaniem tego równania jest

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

gdzie

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

to częstość kołowa drgań. Energia potencjalna jako funkcja położenia $x$ ma postać paraboli

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

W rzeczywistości idealny oscylator harmoniczny nie istnieje. Nawet w przypadku sprężyny: jeśli rozciągnąć ją zbyt mocno, przekroczy granicę sprężystości i pęknie albo ulegnie trwałej deformacji; w praktyce jeszcze zanim do tego dojdzie, przestaje ona dokładnie spełniać prawo Hooke’a. Mimo to oscylator harmoniczny jest w fizyce ważny, ponieważ dowolny potencjał w pobliżu minimum lokalnego (local minimum) można przybliżyć paraboloidą. Rozwijając dowolny potencjał $V(x)$ w szereg Taylora w pobliżu minimum, otrzymujemy

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Ponieważ dodanie stałej do $V(x)$ nie wpływa w ogóle na siłę, odejmujemy $V(x_0)$. Ponadto, ponieważ $x_0$ jest punktem minimum, mamy $V^\prime(x_0)=0$. Zakładając, że $(x-x_0)$ jest dostatecznie małe i pomijając wyrazy wyższego rzędu, dostajemy

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

\*. Jest to równoważne ruchowi oscylatora harmonicznego o efektywnej stałej sprężystości $k=V^{\prime\prime}(x_0)$ w pobliżu punktu $x_0$. Innymi słowy, jeśli amplituda jest dostatecznie mała, dowolne drgania można przybliżyć jako drgania harmoniczne proste (simple harmonic oscillation).

> \* Ponieważ założyliśmy, że $V(x)$ ma w $x_0$ minimum lokalne, zachodzi tu $V^{\prime\prime}(x_0) \geq 0$. Bardzo rzadko może się zdarzyć, że $V^{\prime\prime}(x_0)=0$; w takim przypadku ruchu nie da się przybliżyć jako drgań harmonicznych prostych.
{: .prompt-info }

### Oscylator harmoniczny w mechanice kwantowej
Problem kwantowego oscylatora harmonicznego polega na rozwiązaniu równania Schrödingera dla potencjału

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

[Niezależne od czasu równanie Schrödingera](/posts/time-independent-schrodinger-equation/) dla oscylatora harmonicznego ma postać

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

Do rozwiązania tego problemu istnieją dwa zupełnie różne podejścia. Pierwsze to metoda analityczna (analytic method) oparta o **metodę szeregu potęgowego (power series method)**, drugie to metoda algebraiczna (algebraic method) oparta o **operatory drabinkowe (ladder operators)**. Metoda algebraiczna jest szybsza i prostsza, jednak warto również przestudiować rozwiązanie analityczne z użyciem szeregu potęgowego. Tutaj omówimy metodę algebraiczną; rozwiązanie analityczne opisano w [tym wpisie](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Komutator i kanoniczna relacja komutacyjna
Korzystając z operatora pędu $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$, równanie ($\ref{eqn:t_independent_schrodinger_eqn}$) można zapisać jako

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Teraz rozłóżmy na czynniki hamiltonian (Hamiltonian)

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

Gdyby $p$ i $x$ były liczbami (numbers), to

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

dałoby się łatwo rozłożyć. Jednak tutaj $\hat{p}$ i $\hat{x}$ są operatorami, a dla operatorów na ogół nie zachodzi **własność przemienności (commutative property)** (tj. $\hat{p}\hat{x}\neq \hat{x}\hat{p}$), więc sytuacja nie jest tak prosta. Mimo to powyższy rozkład może stanowić punkt odniesienia, więc zacznijmy od rozważenia następującej wielkości:

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

Dla operatorów $\hat{a_\pm}$ zdefiniowanych powyżej, iloczyn $\hat{a}\_-\hat{a}\_+$ wynosi

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Wyraz $(\hat{x}\hat{p}-\hat{p}\hat{x})$ nazywa się **komutatorem (commutator)** operatorów $\hat{x}$ i $\hat{p}$; opisuje on, jak bardzo te dwa operatory nie komutują (commute). Ogólnie komutator operatorów $\hat{A}$ i $\hat{B}$ zapisuje się w nawiasach kwadratowych:

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

Korzystając z tej notacji, równanie ($\ref{eqn:a_m_times_a_p_without_commutator}$) można przepisać jako

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Musimy teraz wyznaczyć komutator $\hat{x}$ i $\hat{p}$.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

a po „odłączeniu” funkcji testowej $f(x)$ otrzymujemy

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

Jest to **kanoniczna relacja komutacyjna (canonical commutation relation)**.

## Operatory drabinkowe (ladder operators)
Na mocy kanonicznej relacji komutacyjnej równanie ($\ref{eqn:a_m_times_a_p}$) przyjmuje postać

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

czyli

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Kolejność $\hat{a}\_-$ i $\hat{a}\_+$ jest tu istotna: jeśli umieścimy $\hat{a}\_+$ po lewej, dostajemy

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

i spełnione jest

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

Wtedy hamiltonian można też zapisać jako

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Zatem niezależne od czasu równanie Schrödingera ($\hat{H}\psi=E\psi$) zapisane przy użyciu $\hat{a}_\pm$ ma postać

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(znaki skorelowane).

Teraz można wykazać następującą kluczową własność:

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Dowód:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> Analogicznie,
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Zatem jeśli znajdziemy jedno rozwiązanie niezależnego od czasu równania Schrödingera, to możemy znaleźć wszystkie pozostałe. Ponieważ dla dowolnego stanu stacjonarnego można podnosić lub obniżać poziom energii, operatory $\hat{a}\_\pm$ nazywa się **operatorami drabinkowymi (ladder operators)**; $\hat{a}\_+$ jest **operatorem podnoszącym (raising operator)**, a $\hat{a}\_-$ **operatorem opuszczającym (lowering operator)**.

## Stany stacjonarne oscylatora harmonicznego
### Stany stacjonarne $\psi_n$ i poziomy energii $E_n$
Jeśli będziemy wciąż stosować operator opuszczający, to w pewnym momencie otrzymamy stan o energii mniejszej niż $0$, a taki stan nie może istnieć fizycznie. Matematycznie: jeśli $\psi$ jest rozwiązaniem równania Schrödingera, to $\hat{a}_-\psi$ także jest rozwiązaniem, ale nie ma gwarancji, że to nowe rozwiązanie zawsze będzie znormalizowane (czyli będzie stanem fizycznie dopuszczalnym). Stosując operator opuszczający dostatecznie wiele razy, ostatecznie otrzymamy rozwiązanie trywialne $\psi=0$.

Dlatego dla stanu stacjonarnego $\psi$ oscylatora harmonicznego istnieje „najniższy poziom” $\psi_0$ (taki, dla którego nie ma już niższej energii), spełniający

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

Ponieważ $\psi_0$ spełnia

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

to

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

Jest to [równanie różniczkowe zwyczajne o rozdzielnych zmiennych](/posts/Separation-of-Variables/), więc łatwo je rozwiązać:

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

Funkcję tę można następnie znormalizować:

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Ponieważ $A^2 = \sqrt{m\omega / \pi\hbar}$, mamy

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Podstawiając to rozwiązanie do wcześniej otrzymanego równania Schrödingera ($\ref{eqn:schrodinger_eqn_with_ladder}$) i korzystając z faktu, że $\hat{a}_-\psi_0=0$, dostajemy

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

Zaczynając od tego **stanu podstawowego (ground state)** i wielokrotnie stosując operator podnoszący, otrzymujemy stany wzbudzone (excited states), przy czym każdorazowe zadziałanie operatora podnoszącego zwiększa energię o $\hbar\omega$.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

gdzie $A_n$ jest stałą normalizacji. W ten sposób, znając stan podstawowy i stosując operator podnoszący, można wyznaczyć wszystkie stany stacjonarne oscylatora harmonicznego oraz dozwolone poziomy energii.

### Normalizacja
Stałe normalizacji można również wyznaczyć metodą algebraiczną. Ponieważ wiemy, że $\hat{a}\_{\pm}\psi_n$ jest proporcjonalne do $\psi\_{n\pm 1}$, możemy zapisać

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Zwróćmy uwagę, że dla dowolnych funkcji całkowalnych $f(x)$ i $g(x)$ zachodzi

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

czyli $\hat{a}\_\mp$ jest **sprzężeniem hermitowskim (hermitian conjugate)** oraz **operatorem sprzężonym (adjoint operator)** do $\hat{a}\_\pm$.

> **Dowód:**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

Zatem, podstawiając $f=\hat{a}_\pm \psi_n$ i $g=\psi_n$, otrzymujemy

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Z równań ($\ref{eqn:schrodinger_eqn_with_ladder}$) i ($\ref{eqn:psi_n_and_E_n}$) wynika, że

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

Zatem z ($\ref{eqn:norm_const}$) i ($\ref{eqn:norm_const_2}$) dostajemy

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

Ponieważ $\psi_n$ oraz $\psi_{n\pm1}$ są znormalizowane, mamy $\|c_n\|^2=n+1$ i $\|d_n\|^2=n$, a więc

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

Stąd dowolny znormalizowany stan stacjonarny $\psi_n$ można zapisać jako

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

Czyli w równaniu ($\ref{eqn:psi_n_and_E_n}$) stała normalizacji wynosi $A_n=\cfrac{1}{\sqrt{n!}}$.

### Ortogonalność stanów stacjonarnych
Podobnie jak w przypadku [jednowymiarowej nieskończonej studni kwadratowej](/posts/the-infinite-square-well/#3-ten-stan-jest-ortogonalny-orthogonality), stany stacjonarne oscylatora harmonicznego są ortogonalne.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Dowód
Można to wykazać, korzystając z równań ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$) i ($\ref{eqn:norm_const_3}$). W ($\ref{eqn:hermitian_conjugate}$) podstawmy $f=\hat{a}_-\psi_m$, $g=\psi_n$:

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

Wówczas

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

Korzystając z ortogonalności, tak jak [w przypadku wzoru (19) dla jednowymiarowej nieskończonej studni kwadratowej](/posts/the-infinite-square-well/#wyznaczenie-ogolnego-rozwiazania-rownania-schrodingera-zaleznego-od-czasu-psixt), przy rozwinięciu $\Psi(x,0)$ w kombinację liniową stanów stacjonarnych $\sum c_n\psi_n(x)$ współczynniki $c_n$ można wyznaczyć [metodą Fouriera](/posts/the-infinite-square-well/#wyznaczenie-wspolczynnikow-c_n-metoda-fouriera-fouriers-trick).

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Tak samo jak wcześniej, $\|c_n\|^2$ jest prawdopodobieństwem otrzymania wartości $E_n$ przy pomiarze energii.

## Wartość oczekiwana energii potencjalnej $\langle V \rangle$ w dowolnym stanie stacjonarnym $\psi_n$
Aby obliczyć $\langle V \rangle$, trzeba policzyć całkę

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

Przy obliczaniu całek tego typu, zawierających potęgi $\hat{x}$ i $\hat{p}$, przydatna jest następująca metoda.

Najpierw, korzystając z definicji operatorów drabinkowych z ($\ref{eqn:ladder_operators}$), wyrażamy $\hat{x}$ i $\hat{p}$ przez operator podnoszący i opuszczający:

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Następnie interesującą wielkość fizyczną zapisujemy za pomocą tych wyrażeń na $\hat{x}$ i $\hat{p}$. Ponieważ tutaj interesuje nas $x^2$, można napisać

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

Stąd

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

Ponieważ $\left(\hat{a}\_\pm \right)^2$ jest proporcjonalne do $\psi\_{n\pm2}$, jest ono ortogonalne do $\psi\_n$; zatem dwa wyrazy $\left(\hat{a}\_+ \right)^2$ oraz $\left(\hat{a}\_- \right)^2$ dają $0$. Na koniec, korzystając z ($\ref{eqn:norm_const_2}$) do obliczenia pozostałych dwóch składników, otrzymujemy

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

Z równania ($\ref{eqn:psi_n_and_E_n}$) widać, że wartość oczekiwana energii potencjalnej jest dokładnie połową całkowitej energii, a druga połowa to oczywiście energia kinetyczna $T$. Jest to charakterystyczna własność oscylatora harmonicznego.
