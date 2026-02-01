---
title: Twierdzenie Ehrenfesta (Ehrenfest theorem)
description: W quantum mechanice pokazuję, jak z funkcji falowej wyznaczać wartości oczekiwane położenia i pędu, a następnie uogólniam to na dowolną wielkość Q(x,p) i wyprowadzam twierdzenie Ehrenfesta.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Wymagania wstępne
- ciągły rozkład prawdopodobieństwa i gęstość prawdopodobieństwa
- [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/)

## Obliczanie wartości oczekiwanych z funkcji falowej
### Wartość oczekiwana położenia $x$
Wartość oczekiwana (expectation value) położenia $x$ dla cząstki w stanie $\Psi$ wynosi

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

Jeżeli dla dostatecznie dużej liczby cząstek znajdujących się w tym samym stanie $\Psi$ zmierzymy położenie każdej z nich, a następnie uśrednimy wyniki pomiarów, to otrzymamy $\langle x \rangle$ obliczone z powyższego wzoru.

> Zwróć uwagę, że „wartość oczekiwana” nie oznacza średniej z wielokrotnych pomiarów *tej samej* cząstki, lecz średnią wyników pomiarów dla **zespołu (ensemble)** układów w identycznym stanie. Jeśli wielokrotnie mierzyć tę samą cząstkę w krótkich odstępach czasu, to po pierwszym pomiarze następuje [kolaps funkcji falowej (collapse)](/posts/schrodinger-equation-and-the-wave-function/#pomiar-i-kolaps-funkcji-falowej), więc kolejne pomiary będą wciąż dawały tę samą wartość.
{: .prompt-warning }

### Wartość oczekiwana pędu $p$
Ponieważ $\Psi$ zależy od czasu, wraz z upływem czasu będzie się zmieniać także $\langle x \rangle$. Wówczas, na mocy równania (8) z wpisu [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/) oraz powyższego wzoru ($\ref{eqn:x_exp}$), zachodzi:

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> W przejściu od ($\ref{eqn:dx/dt_1}$) do ($\ref{eqn:dx/dt_2}$) oraz od ($\ref{eqn:dx/dt_2}$) do ($\ref{eqn:dx/dt_3}$) dwukrotnie zastosowano całkowanie przez części, a ponieważ $\lim_{x\rightarrow\pm\infty}\Psi=0$, pominięto wyrazy brzegowe (boundary term).
{: .prompt-tip }

Stąd wartość oczekiwana **pędu** wynosi

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Wartość oczekiwana dowolnej wielkości fizycznej $Q(x,p)$
Wyrażenia na $\langle x \rangle$ i $\langle p \rangle$ można zapisać w postaci

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

Operator $\hat x \equiv x$ opisuje położenie, a operator $\hat p \equiv -i\hbar(\partial/\partial x)$ opisuje pęd. W przypadku operatora pędu $\hat p$, po uogólnieniu na przestrzeń trójwymiarową można go zdefiniować jako $\hat p \equiv -i\hbar\nabla$.

Ponieważ wszystkie klasyczne zmienne mechaniczne można wyrazić przez położenie i pęd, da się to uogólnić na wartość oczekiwaną dowolnej wielkości fizycznej. Aby obliczyć wartość oczekiwaną dowolnej wielkości $Q(x,p)$, należy w $Q$ zastąpić wszystkie $p$ przez $-i\hbar\nabla$, a następnie wstawić otrzymany operator pomiędzy $\Psi^\*$ i $\Psi$ oraz scałkować.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

Na przykład, ponieważ energia kinetyczna wynosi $T=\cfrac{p^2}{2m}$, mamy

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

Zatem, korzystając z ($\ref{eqn:Q_exp}$), można obliczać wartości oczekiwane dowolnych wielkości fizycznych dla cząstki w stanie $\Psi$.

## Twierdzenie Ehrenfesta (Ehrenfest theorem)
### Obliczenie $d\langle p \rangle/dt$
Zróżniczkujmy obustronnie równanie ($\ref{eqn:p_op}$) względem czasu $t$, aby otrzymać pochodną czasową wartości oczekiwanej pędu $\cfrac{d\langle p \rangle}{dt}$.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> Do ($\ref{eqn:dp/dt_1}$) można podstawić równania (6) i (7) z wpisu [Równanie Schrödingera i funkcja falowa](/posts/schrodinger-equation-and-the-wave-function/), otrzymując ($\ref{eqn:dp/dt_2}$). W przejściu od ($\ref{eqn:dp/dt_3}$) do ($\ref{eqn:dp/dt_4}$) zastosowano całkowanie przez części, a jak wcześniej, ponieważ $\lim_{x\rightarrow\pm\infty}\Psi=0$, pominięto wyrazy brzegowe (boundary term).
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Związek twierdzenia Ehrenfesta z drugą zasadą dynamiki Newtona
Następujące dwa równania, które otrzymaliśmy, nazywa się twierdzeniem Ehrenfesta (Ehrenfest theorem).

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

Twierdzenie Ehrenfesta ma postać bardzo podobną do klasycznego związku między energią potencjalną a siłą zachowawczą: $F=\cfrac{dp}{dt}=-\nabla V$.  
Jeśli zestawić oba równania, otrzymujemy:

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newton's Second Law of Motion]}$$

Jeżeli prawą stronę drugiego równania twierdzenia Ehrenfesta $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (równanie [$\ref{eqn:ehrenfest_theorem_2nd}$]) rozwinąć w szereg Taylora względem $x$ w pobliżu $\langle x \rangle$, to

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

Jeśli wówczas $x-\langle x \rangle$ jest dostatecznie małe, można pominąć wszystkie wyrazy wyższych rzędów poza pierwszym i przybliżyć

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

Czyli: **jeśli funkcja falowa cząstki jest przestrzennie bardzo silnie skoncentrowana w pobliżu jednego punktu (tj. dyspersja $\|\Psi\|^2$ względem $x$ jest bardzo mała), to twierdzenie Ehrenfesta można przybliżyć drugą zasadą dynamiki Newtona z mechaniki klasycznej.** W skali makroskopowej można zaniedbać rozmycie funkcji falowej w przestrzeni i w praktyce traktować położenie cząstki jako punkt, więc druga zasada Newtona jest spełniona; natomiast w skali mikroskopowej nie da się pominąć efektów kwantowych, dlatego druga zasada Newtona przestaje obowiązywać i należy posługiwać się twierdzeniem Ehrenfesta.
