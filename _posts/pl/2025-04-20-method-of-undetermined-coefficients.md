---
title: "Metoda nieoznaczonych współczynników"
description: "Metoda nieoznaczonych współczynników pozwala prosto rozwiązywać zagadnienia początkowe dla pewnej klasy liniowych niejednorodnych równań różniczkowych o stałych współczynnikach, często używana w inżynierii (układy drgające, modele obwodów RLC)."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Zastosowanie **metody nieoznaczonych współczynników**:
>   - dla **stałych współczynników $a$ i $b$**
>   - gdy wymuszenie $r(x)$ jest funkcją wykładniczą, potęgą $x$, $\cos$ lub $\sin$, albo sumą i/lub iloczynem takich funkcji
>   - dla liniowego równania różniczkowego zwyczajnego $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Reguły wyboru w metodzie nieoznaczonych współczynników**  
>   - **(a) reguła podstawowa (basic rule)**: w równaniu ($\ref{eqn:linear_ode_with_constant_coefficients}$), jeśli $r(x)$ jest jedną z funkcji z pierwszej kolumny tabeli, wybierz $y_p$ z tej samej linii, a następnie wyznacz nieoznaczone współczynniki, podstawiając $y_p$ i jego pochodne do ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) reguła modyfikacji (modification rule)**: jeśli składnik wybrany jako $y_p$ jest rozwiązaniem odpowiadającego mu jednorodnego równania $y^{\prime\prime} + ay^{\prime} + by = 0$, pomnóż go przez $x$ (albo przez $x^2$, jeśli odpowiada on pierwiastkowi podwójnemu równania charakterystycznego).  
>   - **(c) reguła sumy (sum rule)**: jeśli $r(x)$ jest sumą funkcji z pierwszej kolumny tabeli, wybierz jako $y_p$ sumę odpowiadających funkcji z drugiej kolumny.
>
> | Składnik w $r(x)$ | Wybór dla $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Wymagania wstępne
- [Jednorodne liniowe RRO drugiego rzędu (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [Jednorodne liniowe RRO drugiego rzędu o stałych współczynnikach](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Równanie Eulera–Cauchy’ego](/posts/euler-cauchy-equation/)
- [Wronskian, istnienie i jednoznaczność rozwiązań](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Niejednorodne liniowe RRO drugiego rzędu (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/)
- przestrzenie wektorowe, rozpiętość liniowa (algebra liniowa)

## Metoda nieoznaczonych współczynników
Rozważmy niejednorodne liniowe równanie różniczkowe zwyczajne drugiego rzędu z $r(x) \not\equiv 0$:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

oraz odpowiadające mu jednorodne równanie różniczkowe:

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Jak omówiono wcześniej w tekście [Niejednorodne liniowe RRO drugiego rzędu (Nonhomogeneous Linear ODEs of Second Order)](/posts/nonhomogeneous-linear-odes-of-second-order/), aby rozwiązać zagadnienie początkowe dla niejednorodnego liniowego RRO ($\ref{eqn:nonhomogeneous_linear_ode}$), należy najpierw rozwiązać jednorodne RRO ($\ref{eqn:homogeneous_linear_ode}$) i znaleźć $y_h$, a następnie znaleźć jedno rozwiązanie szczególne $y_p$ równania ($\ref{eqn:nonhomogeneous_linear_ode}$), aby otrzymać rozwiązanie ogólne

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Jak zatem znaleźć $y_p$? Ogólną metodą wyznaczania $y_p$ jest **metoda wariacji stałych (method of variation of parameters)**, jednak w pewnych przypadkach można zastosować znacznie prostszą **metodę nieoznaczonych współczynników (method of undetermined coefficients)**. Jest ona szczególnie użyteczna w inżynierii, bo stosuje się ją m.in. do układów drgających oraz modeli obwodów elektrycznych RLC.

Metoda nieoznaczonych współczynników nadaje się do liniowych równań różniczkowych o **stałych współczynnikach $a$ i $b$**, w których wymuszenie $r(x)$ jest funkcją wykładniczą, potęgą $x$, $\cos$ lub $\sin$, albo sumą i/lub iloczynem takich funkcji:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

Istotą metody jest to, że $r(x)$ tego typu ma pochodne o podobnej postaci. Aby zastosować metodę nieoznaczonych współczynników, wybiera się $y_p$ o postaci podobnej do $r(x)$, lecz zawierające niewiadome współczynniki, które wyznacza się poprzez podstawienie $y_p$ oraz jego pochodnych do danego równania różniczkowego. Reguły wyboru odpowiedniego $y_p$ dla praktycznie ważnych postaci $r(x)$ są następujące.

> **Reguły wyboru w metodzie nieoznaczonych współczynników**  
> **(a) reguła podstawowa (basic rule)**: w równaniu ($\ref{eqn:linear_ode_with_constant_coefficients}$), jeśli $r(x)$ jest jedną z funkcji z pierwszej kolumny tabeli, wybierz $y_p$ z tej samej linii, a następnie wyznacz nieoznaczone współczynniki, podstawiając $y_p$ i jego pochodne do ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) reguła modyfikacji (modification rule)**: jeśli składnik wybrany jako $y_p$ jest rozwiązaniem odpowiadającego mu jednorodnego równania różniczkowego $y^{\prime\prime} + ay^{\prime} + by = 0$, pomnóż go przez $x$ (albo przez $x^2$, jeśli odpowiada on pierwiastkowi podwójnemu równania charakterystycznego).  
> **(c) reguła sumy (sum rule)**: jeśli $r(x)$ jest sumą funkcji z pierwszej kolumny tabeli, wybierz jako $y_p$ sumę odpowiadających funkcji z drugiej kolumny.
>
> | Składnik w $r(x)$ | Wybór dla $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Metoda ta jest nie tylko prosta, ale ma też zaletę „samokorygującą”. Jeśli wybierzesz błędne $y_p$ lub zbyt małą liczbę składników, w obliczeniach pojawi się sprzeczność; jeśli zaś wybierzesz zbyt wiele składników, współczynniki zbędnych składników wyjdą równe $0$, co i tak prowadzi do poprawnego wyniku. Nawet jeśli coś pójdzie nie tak, zwykle w naturalny sposób zauważysz to w trakcie rachunków, więc gdy wybierzesz w miarę sensowne $y_p$ zgodnie z powyższymi regułami, warto po prostu spróbować.

### Dowód reguły sumy
Rozważmy niejednorodne liniowe RRO postaci $r(x) = r_1(x) + r_2(x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Teraz rozważmy dwa równania o tej samej lewej stronie, lecz z wymuszeniami odpowiednio $r_1$, $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Niech ich rozwiązaniami szczególnymi będą odpowiednio ${y_p}_1$, ${y_p}_2$. Oznaczmy lewą stronę danego równania przez $L[y]$. Wówczas z liniowości operatora $L$ wynika, że dla $y_p = {y_p}_1 + {y_p}_2$ zachodzi:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Przykład: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
Zgodnie z regułą podstawową (a) przyjmujemy $y_p = Ce^{\gamma x}$ i podstawiamy do danego równania $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Przypadek $\gamma^2 + a\gamma + b \neq 0$
Możemy wyznaczyć nieoznaczony współczynnik $C$ i znaleźć $y_p$:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Przypadek $\gamma^2 + a\gamma + b = 0$
W tym przypadku należy zastosować regułę modyfikacji (b). Najpierw, korzystając z $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, znajdźmy pierwiastki równania charakterystycznego jednorodnego RRO $y^{\prime\prime} + ay^{\prime} + by = 0$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Stąd otrzymujemy bazę rozwiązań jednorodnego równania:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Przypadek $\gamma \neq -a-\gamma$
Ponieważ $Ce^{\gamma x}$, wybrane jako $y_p$, jest rozwiązaniem jednorodnego równania, ale nie odpowiada pierwiastkowi podwójnemu, zgodnie z regułą modyfikacji (b) mnożymy przez $x$ i przyjmujemy $y_p = Cxe^{\gamma x}$.

Podstawiając zmodyfikowane $y_p$ do równania $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$ otrzymujemy:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Przypadek $\gamma = -a-\gamma$
W tym przypadku $Ce^{\gamma x}$ odpowiada pierwiastkowi podwójnemu równania charakterystycznego, więc zgodnie z regułą modyfikacji (b) mnożymy przez $x^2$ i przyjmujemy $y_p = Cx^2 e^{\gamma x}$.

Podstawiając do równania $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$ otrzymujemy:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Rozszerzenie metody nieoznaczonych współczynników: $r(x)$ jako iloczyn funkcji
Rozważmy niejednorodne liniowe RRO, w którym $r(x)$ ma postać $r(x) = k x^n e^{\alpha x}\cos(\omega x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Załóżmy, że $r(x)$ jest iloczynem wykładniczej $e^{\alpha x}$, potęgi $x^m$, $\cos{\omega x}$ lub $\sin{\omega x}$ (tu zakładamy $\cos$ — bez straty ogólności), ewentualnie sumą i/lub iloczynem takich funkcji (tj. da się go zapisać jako sumę i iloczyn funkcji z pierwszej kolumny wcześniejszej tabeli). Pokażemy, że istnieje rozwiązanie $y_p$ będące sumą i iloczynem funkcji z drugiej kolumny tej samej tabeli.

> Dla ścisłości w pewnym miejscu użyto aparatu algebry liniowej — te fragmenty oznaczono znakiem \*. Można je pominąć i czytać dalej; do ogólnego zrozumienia nie są konieczne.
{: .prompt-tip }

### Definicja przestrzeni wektorowej $V$\*
Dla $r(x)$ postaci

$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

możemy zdefiniować przestrzeń wektorową $V$ tak, aby $r(x) \in V$, w następujący sposób:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Postacie pochodnych funkcji wykładniczej, wielomianu i funkcji trygonometrycznych
Postacie pochodnych funkcji bazowych z pierwszej kolumny tabeli są następujące:
- funkcja wykładnicza: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- wielomian: $\cfrac{d}{dx}x^m = mx^{m-1}$
- funkcje trygonometryczne: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Pochodne otrzymywane przez różniczkowanie tych funkcji również dają się zapisać jako <u>suma funkcji tego samego typu</u>.

Zatem jeśli $f$ i $g$ są jedną z powyższych funkcji lub ich sumą, to dla $r(x) = f(x)g(x)$, stosując regułę iloczynu, mamy

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

przy czym $f$, $f^{\prime}$, $f^{\prime\prime}$ oraz $g$, $g^{\prime}$, $g^{\prime\prime}$ można wszystkie zapisać jako sumy (lub stałe wielokrotności) funkcji wykładniczych, wielomianów i funkcji trygonometrycznych. W konsekwencji $r^{\prime}(x) = (fg)^{\prime}$ i $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ również, podobnie jak $r(x)$, dają się wyrazić jako sumy i iloczyny tych funkcji.

### Niezmienniczość $V$ względem różniczkowania $D$ i przekształcenia liniowego $L$\*
To znaczy: nie tylko samo $r(x)$, ale też $r^{\prime}(x)$ i $r^{\prime\prime}(x)$ są kombinacjami liniowymi składników postaci $x^k e^{\alpha x}\cos(\omega x)$ oraz $x^k e^{\alpha x}\sin(\omega x)$, więc

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Nie ograniczając się do $r(x)$, wprowadzamy operator różniczkowania $D$ dla wszystkich elementów przestrzeni $V$. Wtedy *przestrzeń $V$ jest domknięta ze względu na operator różniczkowania $D$*. Jeśli oznaczymy lewą stronę równania jako $L[y] = y^{\prime\prime} + ay^{\prime} + by$, to *$V$ jest niezmiennicza (invariant) względem $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Ponieważ $r(x) \in V$ i $V$ jest niezmiennicza względem $L$, istnieje pewien element $y_p \in V$ taki, że $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Zatem, jeśli wybierzemy odpowiednie $y_p$ jako sumę wszystkich możliwych składników iloczynowych, używając nieoznaczonych współczynników $A_0, A_1, \dots, A_n$ oraz $K$, $M$, w postaci

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}), $$

to zgodnie z regułą podstawową (a) i regułą modyfikacji (b) można wyznaczyć nieoznaczone współczynniki, podstawiając $y_p$ (lub $xy_p$, $x^2y_p$) i jego pochodne do danego równania. Wartość $n$ dobiera się zgodnie ze stopniem wielomianowym w $x$ występującym w $r(x)$.

$\blacksquare$

> Jeśli dane wymuszenie $r(x)$ zawiera kilka różnych wartości $\alpha_i$ oraz $\omega_j$, to dla każdej z nich trzeba dobrać $y_p$ tak, by zawierało wszystkie możliwe składniki postaci $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ oraz $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ (bez pominięć).  
> Zaletą metody nieoznaczonych współczynników jest prostota; jeśli ansatz robi się zbyt złożony i ta zaleta zanika, rozsądniej może być zastosować (omawianą później) metodę wariacji stałych.
{: .prompt-warning }

## Rozszerzenie metody nieoznaczonych współczynników: równanie Eulera–Cauchy’ego
Metodę nieoznaczonych współczynników można wykorzystać nie tylko dla [jednorodnych liniowych RRO drugiego rzędu o stałych współczynnikach](/posts/homogeneous-linear-odes-with-constant-coefficients/), ale także dla [równania Eulera–Cauchy’ego](/posts/euler-cauchy-equation/):

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Podstawienie zmiennej
Jeśli wykonamy podstawienie [$x = e^t$ i sprowadzimy do jednorodnego liniowego RRO drugiego rzędu o stałych współczynnikach](/posts/euler-cauchy-equation/#przeksztalcenie-do-jednorodnego-liniowego-rro-drugiego-rzedu-o-stalych-wspolczynnikach), to

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

i — jak już wcześniej ustaliliśmy — równanie Eulera–Cauchy’ego można przekształcić do liniowego RRO o stałych współczynnikach względem $t$:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Teraz wystarczy zastosować dokładnie tak samo [metodę nieoznaczonych współczynników omówioną wcześniej](#metoda-nieoznaczonych-wspolczynnikow), rozwiązać równanie względem $t$, a na końcu użyć faktu, że $t = \ln x$, aby otrzymać rozwiązanie względem $x$.

### Gdy $r(x)$ jest potęgą $x$, logarytmem naturalnym lub sumą/iloczynem takich funkcji
W szczególności, gdy wymuszenie $r(x)$ składa się z potęg $x$, logarytmów naturalnych, lub sum i/lub iloczynów takich funkcji, można od razu dobrać odpowiednie $y_p$ według poniższych reguł dla równania Eulera–Cauchy’ego.

> **Reguły wyboru w metodzie nieoznaczonych współczynników: dla równania Eulera–Cauchy’ego**  
> **(a) reguła podstawowa (basic rule)**: w równaniu ($\ref{eqn:euler_cauchy}$), jeśli $r(x)$ jest jedną z funkcji z pierwszej kolumny tabeli, wybierz $y_p$ z tej samej linii, a następnie wyznacz nieoznaczone współczynniki, podstawiając $y_p$ i jego pochodne do ($\ref{eqn:euler_cauchy}$).  
> **(b) reguła modyfikacji (modification rule)**: jeśli składnik wybrany jako $y_p$ jest rozwiązaniem odpowiadającego mu jednorodnego równania $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, pomnóż go przez $\ln{x}$ (albo przez $(\ln{x})^2$, jeśli odpowiada on pierwiastkowi podwójnemu równania charakterystycznego).  
> **(c) reguła sumy (sum rule)**: jeśli $r(x)$ jest sumą funkcji z pierwszej kolumny tabeli, wybierz jako $y_p$ sumę odpowiadających funkcji z drugiej kolumny.
>
> | Składnik w $r(x)$ | Wybór dla $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Dzięki temu dla praktycznie ważnych postaci wymuszenia $r(x)$ można znaleźć $y_p$ szybciej i wygodniej — otrzymując to samo, co metodą [podstawienia zmiennej](#podstawienie-zmiennej). Wystarczy wziąć [oryginalne reguły wyboru](#metoda-nieoznaczonych-wspolczynnikow) i w miejsce $x$ podstawić $\ln{x}$, aby wyprowadzić te reguły dla równania Eulera–Cauchy’ego.
