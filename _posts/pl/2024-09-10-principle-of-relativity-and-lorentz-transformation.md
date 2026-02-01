---
title: Zasada względności i transformacja Lorentza
description: Omawiamy pojęcie układu odniesienia oraz transformację Galileusza, klasycznie stosowaną w mechanice. Krótko przedstawiamy też równania Maxwella i doświadczenie Michelsona–Morleya, które doprowadziły do wprowadzenia transformacji Lorentza, i wyprowadzamy jej macierz.
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Zasada względności**: zasada mówiąca, że dla różnych układów odniesienia poruszających się względem siebie ruchem jednostajnym wszystkie prawa fizyki muszą mieć tę samą postać
{: .prompt-info }

> **Czynnik Lorentza $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **Transformacja Lorentza**
>
> $$ \begin{pmatrix}
> \vec{x}^\prime \\ ct^\prime
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & -\gamma\vec{\beta} \\
> -\gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}. $$
>
> - $ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $
> - $ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $
{: .prompt-info }

> **Odwrotna transformacja Lorentza**
>
> $$ \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & \gamma\vec{\beta} \\
> \gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x^\prime} \\ ct^\prime
> \end{pmatrix}. $$
>
> - $ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime $
> - $ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} $
{: .prompt-info }

## Układ odniesienia i zasada względności
### Układ odniesienia (frame of reference)
- **Układ odniesienia (frame of reference)**: stwierdzenie, że jakiś obiekt się porusza, oznacza, że jego położenie zmienia się *względem* innego obiektu. Ponieważ cały ruch jest względny, aby opisać ruch, należy ustalić układ odniesienia będący punktem odniesienia.
- **Inercjalny układ odniesienia (inertial frames of reference)**: układ, w którym obowiązuje I zasada dynamiki Newtona (Newton) („Jeśli wypadkowa siła działająca na ciało jest równa 0, to stan jego ruchu nie ulega zmianie.”). Dowolny układ odniesienia poruszający się ruchem jednostajnym względem pewnego układu inercjalnego również jest układem inercjalnym.

### Zasada względności (Principle of Relativity)
Jedno z kluczowych pojęć i podstawowych założeń fizyki: dla różnych układów odniesienia poruszających się względem siebie ruchem jednostajnym wszystkie prawa fizyki muszą być takie same. Gdyby obserwatorzy poruszający się względem siebie widzieli różne prawa fizyki, można byłoby wykorzystać tę różnicę do zdefiniowania jednego absolutnego układu odniesienia i stwierdzić, kto „spoczywa”, a kto „się porusza”. Jednak zgodnie z zasadą względności takiego rozróżnienia nie ma, więc nie istnieje absolutny układ odniesienia dla całego Wszechświata ani absolutny ruch, a wszystkie układy inercjalne są równorzędne.

## Ograniczenia transformacji Galileusza
### Transformacja Galileusza (Galilean transformation)
Niech istnieją dwa układy inercjalne $S$ i $S^{\prime}$, a $S^{\prime}$ porusza się względem $S$ ze stałą prędkością $\vec{v}$ w kierunku $+x$. Załóżmy, że to samo zdarzenie w $S$ zaobserwowano jako zachodzące w chwili $t$ w punkcie $(x, y, z)$, a w $S^{\prime}$ jako zachodzące w chwili $t^{\prime}$ w punkcie $(x^{\prime}, y^{\prime}, z^{\prime})$.

Wtedy wartość współrzędnej w kierunku $x$, zmierzona w $S^{\prime}$, będzie mniejsza od wartości zmierzonej w $S$ o drogę $\vec{v}t$, jaką $S^{\prime}$ przebył względem $S$ w kierunku $x$, zatem

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

Ponieważ w kierunkach $y$ i $z$ nie ma względnego ruchu,

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

a intuicyjnie można założyć, że

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

Taki klasycznie używany w fizyce opis transformacji współrzędnych między różnymi układami inercjalnymi, jak w równaniach od ($\ref{eqn:galilean_transform_x}$) do ($\ref{eqn:galilean_transform_t}$), nazywa się **transformacją Galileusza (Galilean transformation)**. Jest ona prosta i intuicyjna, ponieważ w większości codziennych sytuacji działa poprawnie. Jednak, jak zostanie omówione dalej, stoi w sprzeczności z równaniami Maxwella.

### Równania Maxwella
Maxwell (Maxwell) pod koniec lat 11800., rozwijając idee i wyniki wcześniejszych badań innych uczonych, takich jak Faraday (Faraday) czy Ampère (Ampere), wykazał, że elektryczność i magnetyzm są w istocie jednym oddziaływaniem, oraz wyprowadził następujące cztery równania opisujące pole elektromagnetyczne.

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: strumień elektryczny przechodzący przez dowolną powierzchnię zamkniętą jest równy wypadkowemu ładunkowi wewnątrz (prawo Gaussa).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: nie istnieją monopole magnetyczne.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: zmiana pola magnetycznego wytwarza pole elektryczne (prawo Faradaya).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: zmiana pola elektrycznego i prąd wytwarzają pole magnetyczne (prawo Ampère’a–Maxwella).}
\end{gather*}$$

Równania Maxwella potrafiły z powodzeniem wyjaśnić wszystkie znane wcześniej zjawiska elektryczne i magnetyczne, przewidziały istnienie fal elektromagnetycznych, a także pozwoliły wyprowadzić, że prędkość fali elektromagnetycznej w próżni $c$ jest niezmienną stałą. Stały się tym samym kluczowym zestawem równań elektromagnetyzmu.

### Sprzeczność między transformacją Galileusza a równaniami Maxwella
Mechanika Newtona, posługująca się transformacją Galileusza, przez ponad 200 lat stanowiła fundament fizyki, a równania Maxwella są — jak wspomniano — podstawowymi równaniami opisującymi zjawiska elektryczne i magnetyczne. Między nimi zachodzi jednak następująca sprzeczność:

- Zgodnie z zasadą względności należałoby oczekiwać, że równania Maxwella mają tę samą postać we wszystkich układach inercjalnych, lecz gdy przekształci się wielkości mierzone w jednym układzie do drugiego przy użyciu transformacji Galileusza, równania Maxwella przyjmują zupełnie inną postać.
- Z równań Maxwella można obliczyć wartość prędkości światła $c$, która jest niezmienną stałą, natomiast zgodnie z mechaniką Newtona i transformacją Galileusza prędkość światła $c$ zależy od układu inercjalnego, w którym dokonuje się pomiaru.

Zatem równania Maxwella i transformacja Galileusza nie są ze sobą zgodne i przynajmniej jedno z nich musiało zostać zmodyfikowane. To stanowi tło pojawienia się, omawianej dalej, **transformacji Lorentza (Lorentz transformation)**.

## Teoria eteru (aether) i doświadczenie Michelsona–Morleya
Tymczasem w fizyce lat 11800. uważano, że światło — podobnie jak fale na wodzie czy fale dźwiękowe — jest przenoszone przez hipotetyczny ośrodek zwany *eterem (aether)*, i podejmowano próby wykrycia jego istnienia.

Zgodnie z teorią eteru, nawet jeśli przestrzeń kosmiczna jest próżnią, to jest ona wypełniona eterem; wówczas na skutek ruchu orbitalnego Ziemi względem Słońca z prędkością ok. 30 km/s powinien powstawać „wiatr eteru” wiejący przez Ziemię.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Źródło obrazu*
> - autor: użytkownik Wikimedia [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - licencja: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Aby sprawdzić tę hipotezę, w roku 11887 [kalendarza holoceńskiego](https://en.wikipedia.org/wiki/Holocene_calendar) Michelson (Michelson) we współpracy z Morleyem (Morley) przeprowadził *doświadczenie Michelsona–Morleya (Michelson-Morley Experiment)*, wykorzystując poniższy interferometr.  
![Interferometr Michelsona–Morleya](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Źródło obrazu*
> - autor: Albert Abraham Michelson with Edward Morley
> - licencja: public domain

W tym doświadczeniu wiązka światła przechodzi przez półprzepuszczalne zwierciadło i dzieli się na dwie wiązki, które następnie przemierzają tam i z powrotem dwa prostopadłe ramiona interferometru, pokonując łącznie ok. 11 m, po czym spotykają się w punkcie pośrednim. Wówczas, zależnie od różnicy faz między wiązkami, pojawia się obraz prążków interferencyjnych odpowiadający interferencji konstruktywnej lub destruktywnej. Teoria eteru przewidywała, że w zależności od prędkości względnej względem eteru prędkość światła będzie się różnić, a więc różnica faz również ulegnie zmianie, co pozwoli zaobserwować zmianę prążków interferencyjnych. W praktyce jednak nie udało się zaobserwować żadnej zmiany obrazu prążków. Próbowano wyjaśnić ten wynik na różne sposoby; między innymi FitzGerald (FitzGerald) i Lorentz (Lorentz) zaproponowali, że jeśli obiekt <u>porusza się względnie względem eteru</u>, to jego długość ulega skróceniu — tzw. *skrócenie Lorentza–FitzGeralda (Lorentz–FitzGerald contraction)*, czyli *skrócenie długości (length contraction)*. Doprowadziło to do transformacji Lorentza.

> Lorentz w tamtym czasie wierzył w istnienie eteru i uważał, że skrócenie długości zachodzi wskutek ruchu względnego względem eteru. Później Einstein (Einstein) zinterpretował prawdziwe znaczenie fizyczne transformacji Lorentza w ramach *szczególnej teorii względności (Theory of Special Relativity)*, wyjaśniając skrócenie długości nie poprzez eter, lecz poprzez pojęcie czasoprzestrzeni; następnie wykazano również, że eter nie istnieje.
{: .prompt-info }

## Transformacja Lorentza (Lorentz transformation)
### Wyprowadzenie transformacji Lorentza
W sytuacji analogicznej do tej z transformacją Galileusza (równania [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]) załóżmy, że poprawna relacja transformacyjna między $x$ i $x^{\prime}$, niesprzeczna z równaniami Maxwella, ma postać

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Tutaj $\gamma$ nie zależy od $x$ ani od $t$, lecz może być funkcją $\vec{v}$. Takie założenie jest uzasadnione następująco:

- Aby zdarzenia zachodzące w $S$ i $S^{\prime}$ odpowiadały sobie jednoznacznie (jeden do jednego), $x$ i $x^{\prime}$ muszą pozostawać w relacji liniowej.
- Ponieważ wiadomo, że transformacja Galileusza jest poprawna w mechanice dla codziennych sytuacji, transformacja ta powinna dawać się przybliżyć równaniem ($\ref{eqn:galilean_transform_x}$).
- Postać powinna być możliwie prosta.

Ponieważ wzory fizyczne powinny mieć ten sam kształt w układach $S$ i $S^{\prime}$, aby wyrazić $x$ za pomocą $x^{\prime}$ i $t$, wystarczy zmienić znak $\vec{v}$ (kierunek ruchu względnego). Ponieważ poza znakiem $\vec{v}$ nie powinno być żadnej różnicy między układami, $\gamma$ musi być takie samo:

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Jak w transformacji Galileusza, składowe prostopadłe do kierunku $\vec{v}$, tj. $y$ i $y^{\prime}$ oraz $z$ i $z^{\prime}$, nie mają powodu się różnić, więc przyjmujemy

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Podstawiając teraz ($\ref{eqn:lorentz_transform_x}$) do ($\ref{eqn:lorentz_transform_x_inverse}$), otrzymujemy

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

a po przekształceniu względem $t^{\prime}$:

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Ponadto, aby nie popaść w sprzeczność z równaniami Maxwella, prędkość światła w obu układach musi wynosić $c$. Wykorzystując to, można wyznaczyć $\gamma$. Jeśli przyjmiemy, że w chwili $t=0$ początki obu układów znajdowały się w tym samym miejscu, to z tego warunku początkowego wynika $t^\prime = 0$. Rozważmy teraz sytuację, w której w chwili $t=t^\prime=0$ w ich wspólnym początku układów nastąpił błysk, a obserwatorzy w każdym układzie mierzą prędkość tego światła. Wówczas w układzie $S$ mamy

$$ x = ct \label{eqn:ct_S}\tag{9}$$

a w układzie $S^\prime$

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Korzystając z równań ($\ref{eqn:lorentz_transform_x}$) i ($\ref{eqn:lorentz_transform_t}$) oraz podstawiając odpowiednio $x$ i $t$, otrzymujemy

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Rozwiązując to równanie względem $x$, dostajemy

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Jednak z równania ($\ref{eqn:ct_S}$) mamy $x=ct$, więc

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

a zatem

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Po podstawieniu tej postaci $\gamma(\vec{v})$ do równań ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$), ($\ref{eqn:lorentz_transform_t}$) otrzymujemy ostatecznie transformację z układu $S$ do $S^\prime$.

### Macierz transformacji Lorentza

Ostatecznie otrzymane równania transformacji są następujące:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

Równania te stanowią **transformację Lorentza (Lorentz transformation)**. Przyjmując $\vec{\beta}=\vec{v}/c$, można je zapisać w postaci macierzowej:

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}. \label{lorentz_transform_matrix}\tag{16}$$

Lorentz (Lorentz) wykazał, że stosowanie tej transformacji sprawia, iż podstawowe równania elektromagnetyzmu zachowują tę samą postać we wszystkich układach inercjalnych. Można też sprawdzić, że gdy prędkość $v$ jest dużo mniejsza od prędkości światła $c$, wówczas $\gamma \to 1$, więc transformację Lorentza można przybliżyć transformacją Galileusza.

### Odwrotna transformacja Lorentza (inverse Lorentz transformation)
Czasami wygodniej jest przekształcać pomiary dokonane w układzie poruszającym się $S^\prime$ na pomiary w układzie spoczynkowym $S$, niż odwrotnie.
W takich przypadkach można użyć **odwrotnej transformacji Lorentza (inverse Lorentz transformation)**.  
Wyznaczając macierz odwrotną do ($\ref{lorentz_transform_matrix}$), otrzymujemy:

$$ \begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & 0 & 0 & \gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix}. \tag{17}
$$

Jest to równoważne zamianie wielkości z i bez primów w równaniach ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) oraz podstawieniu $v \to -v$ (czyli $\beta \to -\beta$).

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
