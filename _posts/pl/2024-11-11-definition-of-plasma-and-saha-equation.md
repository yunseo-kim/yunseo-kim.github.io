---
title: Definicja plazmy i pojęcie temperatury oraz równanie Sahy (Saha equation)
description: Wyjaśniamy, co oznacza „zachowanie kolektywne” w definicji plazmy, omawiamy równanie Sahy i porządkujemy pojęcie temperatury w fizyce plazmy.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
---
## TL;DR
> - **Plazma (plasma)**: quasineutralny gaz złożony z cząstek naładowanych i neutralnych, wykazujący zachowanie kolektywne (collective behavior)
> - **„Zachowanie kolektywne (collective behavior)” plazmy**:
>   - Siła elektryczna między dwoma obszarami plazmy $A$ i $B$ maleje wraz z odległością jak $1/r^2$
>   - Jednak przy danym (stałym) kącie bryłowym ($\Delta r/r$) objętość obszaru plazmy $B$, który może oddziaływać na $A$, rośnie jak $r^3$
>   - Zatem elementy składowe plazmy mogą wywierać na siebie istotne siły nawet na dużych odległościach
> - **Równanie Sahy (Saha equation)**: zależność między stopniem jonizacji gazu w stanie równowagi termicznej a temperaturą i ciśnieniem
+>
> $$ \frac{n_{i+1}n_e}{n_i} = \frac{2}{\lambda_{\text{th}}^3}\frac{g_{i+1}}{g_i}\exp{\left[-\frac{\epsilon_{i+1}-\epsilon_i}{k_B T}\right]}$$
>
> - Pojęcie temperatury w fizyce plazmy:
>   - W gazie i w plazmie średnia energia kinetyczna na cząstkę jest ściśle związana z temperaturą; wielkości te są w praktyce „wymienne”
>   - W fizyce plazmy przyjęło się wyrażać temperaturę poprzez wartość $kT$ w jednostkach energii, tj. w $\mathrm{eV}$
>     - $1\mathrm{eV}=11600\mathrm{K}$
>   - Plazma może jednocześnie mieć kilka różnych temperatur; w szczególności temperatura elektronów ($T_e$) i jonów ($T_i$) mogą się znacznie różnić
> - Plazma niskotemperaturowa vs. wysokotemperaturowa:
>   - Temperatura plazmy:
>     - plazma niskotemperaturowa: $T_e \text{(>10,000℃)} \gg T_i \approx T_g \text{(}\sim\text{100℃)}$ $\rightarrow$ plazma nierównowagowa (non-equilibrium plasma)
>     - plazma wysokotemperaturowa (termiczna): $T_e \approx T_i \approx T_g \text{(>10,000℃)}$ $\rightarrow$ plazma równowagowa (equilibrium plasma)
>   - Gęstość plazmy:
>     - plazma niskotemperaturowa: $n_g \gg n_i \approx n_e$ $\rightarrow$ mały stopień jonizacji, większość występuje jako cząstki neutralne
>     - plazma wysokotemperaturowa (termiczna): $n_g \approx n_i \approx n_e $ $\rightarrow$ duży stopień jonizacji
>   - Pojemność cieplna plazmy:
>     - plazma niskotemperaturowa: temperatura elektronów jest wysoka, ale gęstość jest niska, a większość stanowią względnie chłodne cząstki neutralne, więc pojemność cieplna jest mała i „nie jest gorąca”
>     - plazma wysokotemperaturowa (termiczna): elektrony, jony i cząstki neutralne mają wysoką temperaturę, więc pojemność cieplna jest duża i plazma jest gorąca
{: .prompt-info }

## Wymagania wstępne
- [Cząstki subatomowe i składniki atomu](/posts/constituents-of-an-atom/)
- rozkład Maxwella–Boltzmanna (mechanika statystyczna)
- [Masa i energia, cząstki i fale](/posts/Mass-and-Energy-Particles-and-Waves/)
- symetrie i prawa zachowania (mechanika kwantowa), degeneracja (degeneracy)

## Definicja plazmy
Zazwyczaj w tekstach wyjaśniających plazmę osobom spoza danej dziedziny plazmę definiuje się następująco:

> Czwarty stan skupienia materii po ciele stałym, cieczy i gazie, otrzymywany przez ogrzanie gazu do ultrawysokiej temperatury tak, aby atomy składowe rozdzieliły się na elektrony i dodatnie jony, aż do jonizacji

Nie jest to stwierdzenie błędne; także na stronie [Korea Institute of Fusion Energy](https://www.kfe.re.kr/menu.es;jsessionid=BD5BB81782954634B90FEE221A82583E?mid=a10201010000) przedstawia się plazmę w podobny sposób. To również popularna, „encyklopedyczna” definicja, na którą łatwo trafić przy wyszukiwaniu informacji o plazmie.

Jednak powyższe sformułowanie, mimo że zasadniczo prawdziwe, nie jest definicją ścisłą. Gaz w warunkach otoczenia (temperatura pokojowa i ciśnienie atmosferyczne) także ulega w pewnym *skrajnie małym* stopniu jonizacji, ale nie nazywa się go przez to plazmą. Jeśli rozpuścić w wodzie substancję o wiązaniu jonowym (np. chlorek sodu), to rozdzieli się ona na naładowane jony, ale taki roztwór również nie jest plazmą.  
Innymi słowy: plazma faktycznie jest stanem zjonizowanym, lecz nie każdy zjonizowany ośrodek jest plazmą.

Bardziej ściśle plazmę można zdefiniować tak:

> *Plazma jest quasineutralnym gazem złożonym z cząstek naładowanych i neutralnych, który wykazuje zachowanie kolektywne.*  
> *A plasma is a quasineutral gas of charged and neutral particles which exhibits collective behavior.*
>
> by Fransis F. Chen

Tym, co oznacza „quasineutralność (quasineutrality)”, zajmiemy się później przy okazji **ekranowania Debye’a (Debye shielding)**. Tutaj zobaczmy, co znaczy „zachowanie kolektywne (collective behavior)” w kontekście plazmy.

## Zachowanie kolektywne plazmy
W przypadku niezjonizowanego gazu złożonego z cząstek neutralnych, każda cząsteczka jest elektrycznie obojętna, więc wypadkowa siła elektromagnetyczna wynosi $0$, a wpływ grawitacji można pominąć. Cząsteczki poruszają się swobodnie aż do zderzenia z innymi cząsteczkami, a to właśnie zderzenia determinują ruch cząstek. Nawet jeśli pewna część cząstek ulegnie jonizacji i nabierze ładunku, to udział zjonizowanych cząstek w całym gazie jest na tyle mały, że oddziaływanie elektryczne tych nośników ładunku słabnie z odległością jak $1/r^2$ i nie sięga daleko.

Natomiast w plazmie, która zawiera wiele cząstek naładowanych, sytuacja jest zupełnie inna. Wskutek ruchu cząstek naładowanych może lokalnie dochodzić do nagromadzenia ładunku dodatniego lub ujemnego, co wytwarza pole elektryczne. Ponadto ruch ładunków tworzy prąd, a prąd wytwarza pole magnetyczne. Takie pola elektryczne i magnetyczne mogą wpływać na cząstki położone daleko, nawet bez zderzeń międzycząsteczkowych.

![Siły elektryczne działające na odległość w plazmie](/assets/img/definition-of-plasma/electric-forces-acting-at-a-distance-in-a-plasma.png)

Przeanalizujmy, jak zmienia się natężenie siły elektrycznej działającej między dwoma obszarami plazmy $A$ i $B$, które mają niewielki ładunek netto. Siła elektryczna zgodna z prawem Coulomba (Coulomb force) między $A$ i $B$ maleje wraz ze wzrostem odległości jak $1/r^2$. Jednak przy stałym kącie bryłowym ($\Delta r/r$) objętość obszaru plazmy $B$, który może oddziaływać na $A$, rośnie jak $r^3$. Zatem części składowe plazmy mogą wywierać na siebie istotne siły nawet na dużych odległościach. Oddziaływania elektryczne sięgające daleko sprawiają, że plazma może wykazywać bardzo różnorodne formy dynamiki; jest to też jeden z powodów, dla których istnieje odrębna dziedzina nauki: fizyka plazmy (plasma physics). „Zachowanie kolektywne (collective behavior)” oznacza, że <u>ruch w danym obszarze zależy nie tylko od warunków lokalnych w tym obszarze, lecz także od stanu plazmy w innych, odległych obszarach</u>.

## Równanie Sahy (Saha equation)
**Równanie Sahy (Saha equation)** jest zależnością opisującą związek między stanem jonizacji gazu znajdującego się w równowadze termicznej a temperaturą i ciśnieniem. Zostało zaproponowane przez indyjskiego astrofizyka Meghnada Sahę.

$$ \frac{n_{i+1}n_e}{n_i} = \frac{2}{\lambda_{\text{th}}^3}\frac{g_{i+1}}{g_i}\exp{\left[-\frac{\epsilon_{i+1}-\epsilon_i}{k_B T}\right]} \label{eqn:saha_eqn}\tag{1}$$

- $n_i$: gęstość jonów $i$-krotnie dodatnich (kationów, które utraciły $i$ elektronów)
- $g_i$: degeneracja stanu jonu $i$-krotnie dodatniego
- $\epsilon_i$: energia potrzebna do oderwania $i$ elektronów od atomu obojętnego i wytworzenia jonu $i$-krotnie dodatniego
  - $\epsilon_{i+1}-\epsilon_i$: $(i+1)$-ta energia jonizacji
- $n_e$: gęstość elektronów
- $k_B$: stała Boltzmanna
- $\lambda_{\text{th}}$: termiczna długość fali de Broglie’a (średnia [długość fali de Broglie’a](/posts/Mass-and-Energy-Particles-and-Waves/#fale-materii) elektronu w gazie dla danej temperatury)

$$ \lambda_{\text{th}} \equiv \frac{h}{\sqrt{2\pi m_e k_B T}} \quad \text{ (}h\text{: stała Plancka)} \label{eqn:lambda_th}\tag{2}$$

- $m_e$: masa elektronu
- $T$: temperatura gazu

Jeśli istotna jest tylko jonizacja jednokrotna, a wytwarzanie jonów o ładunku $2+$ i większym można pominąć, to kładąc $n_1=n_i=n_e$, $n_0=n_n$, $U_i = \epsilon = \epsilon_1$, $i=0$, można uprościć równanie do postaci:

$$ \begin{align*}
\frac{n_i^2}{n_n} &= \frac{2}{\lambda_{th}^3}\frac{g_1}{g_0}\exp{\left[-\frac{\epsilon}{k_B T} \right]} \label{eqn:saha_eqn_approx}\tag{3}\\
&= 2\left(\frac{2\pi m_e k_B T}{h^2}\right)^{3/2}\frac{g_1}{g_0}e^{-U_i/{k_B T}} \\
&= 2\frac{g_1}{g_0}\left(\frac{2\pi m_e k_B}{h^2}\right)^{3/2}T^{3/2}e^{-U_i/{k_B T}}. \label{eqn:saha_eqn_approx_2}\tag{4}
\end{align*}$$

### Stopień jonizacji powietrza (azotu) w warunkach pokojowych i przy ciśnieniu atmosferycznym
W powyższym wzorze wartość $2 \cfrac{g_1}{g_0}$ zależy od składu gazu, ale w wielu przypadkach jego **rząd wielkości (order of magnitude)** wynosi $1$. Można więc w przybliżeniu zapisać:

$$ \frac{n_i^2}{n_n} \approx \left(\frac{2\pi m_e k_B}{h^2}\right)^{3/2} T^{3/2} e^{-U_i/{k_B T}}.$$

W układzie SI wartości stałych podstawowych $m_e$, $k_B$, $h$ wynoszą odpowiednio:

- $m_e \approx 9.11 \times 10^{-31} \mathrm{kg}$
- $k_B \approx 1.38 \times 10^{-23} \mathrm{J/K}$
- $h \approx 6.63 \times 10^{-34} \mathrm{J \cdot s}$

a po podstawieniu do wzoru otrzymujemy:

$$ \frac{n_i^2}{n_n} \approx 2.4 \times 10^{21}\ T^{3/2} e^{-U_i/{k_B T}}. \label{eqn:fractional_ionization}\tag{5}$$

Stąd, dla azotu w warunkach pokojowych i przy ciśnieniu atmosferycznym ($n_n \approx 3 \times 10^{25} \mathrm{m^{-3}}$, $T\approx 300\mathrm{K}$; $U_i \approx 14.5\mathrm{eV} \approx 2.32 \times 10^{-18}\mathrm{J}$), przybliżony stopień jonizacji $n_i/(n_n + n_i) \approx n_i/n_n$ wynosi:

$$ \frac{n_i}{n_n} \approx 10^{-122} $$

czyli jest ekstremalnie mały. To dlatego, w odróżnieniu od warunków kosmicznych, w atmosferze przy powierzchni Ziemi (w pobliżu poziomu lądu i morza) naturalnie niemal nie spotyka się plazmy.

## Pojęcie temperatury w fizyce plazmy
Prędkości cząstek gazu w równowadze termicznej z grubsza podlegają rozkładowi Maxwella–Boltzmanna (Maxwell–Boltzmann distribution):

$$ f(v) = \left(\frac{m}{2\pi k_B T} \right)^{3/2} 4\pi v^2 \exp{\left(-\frac{mv^2}{2k_B T} \right)} \label{eqn:maxwell_boltzmann_dist}\tag{6}$$

![Rozkład Maxwella–Boltzmanna](https://tikz.net/files/maxwell-boltzmann-001.png)
> *Źródło obrazu*
> - autor: TikZ.net author [Izaak Neutelings](https://tikz.net/author/izaak/)
> - licencja: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

- prędkość najbardziej prawdopodobna (most probable speed): $v_p = \sqrt{\cfrac{2k_B T}{m}}$
- prędkość średnia (mean speed): $\langle v \rangle = \sqrt{\cfrac{8k_B T}{\pi m}}$
- prędkość skuteczna (RMS speed): $v_{rms} = \sqrt{\langle v^2 \rangle} = \sqrt{\cfrac{3k_B T}{m}}$

Średnia energia kinetyczna przypadająca na jedną cząstkę w temperaturze $T$ wynosi $\cfrac{1}{2}m\langle v^2 \rangle = \cfrac{1}{2}mv_{rms}^2 = \cfrac{3}{2}k_B T$ (dla $3$ stopni swobody) i jest wyznaczona wyłącznie przez temperaturę. W ten sposób w gazie i w plazmie średnia energia kinetyczna na cząstkę jest ściśle związana z temperaturą; ponieważ są to wielkości w praktyce wymienne, w fizyce plazmy przyjęło się wyrażać temperaturę w jednostkach energii $\mathrm{eV}$. Aby uniknąć niejasności wymiarowych, zamiast średniej energii kinetycznej $\langle E_k \rangle$ temperaturę zapisuje się przez wartość $kT$.

Temperatura $T$ odpowiadająca $kT=1\mathrm{eV}$ wynosi:

$$ \begin{align*}
T\mathrm{[K]} &= \frac{1.6 \times 10^{-19}\mathrm{[J]}}{1.38 \times 10^{-23}\mathrm{[J/K]}} \\
&= 11600\mathrm{[K]}
\end{align*} \label{eqn:temp_conv_factor}\tag{7}$$

Zatem w fizyce plazmy zapis $1\mathrm{eV}=11600\mathrm{K}$ oznacza przeliczenie temperatury w tym sensie.  
Np.) dla plazmy o temperaturze $2\mathrm{eV}$ wartość $kT$ wynosi $2\mathrm{eV}$, a średnia energia kinetyczna na cząstkę to $\cfrac{3}{2}kT=3\mathrm{eV}$.

Plazma może też jednocześnie mieć kilka temperatur. W plazmie częstości zderzeń jon–jon lub elektron–elektron są większe niż częstość zderzeń elektron–jon, przez co elektrony i jony mogą osobno osiągać równowagę termiczną przy różnych temperaturach (temperatura elektronów $T_e$ i temperatura jonów $T_i$), tworząc osobne rozkłady Maxwella–Boltzmanna; w zależności od warunków $T_e$ i $T_i$ mogą się znacznie różnić. Co więcej, jeśli z zewnątrz przyłożone jest pole magnetyczne $\vec{B}$, to nawet dla cząstek tego samego rodzaju (np. jonów) siła Lorentza (Lorentz force) ma inną wartość w zależności od tego, czy składowa ruchu jest równoległa czy prostopadła do pola magnetycznego, więc mogą wystąpić różne temperatury $T_\perp$ oraz $T_\parallel$.

## Zależność między temperaturą, ciśnieniem i gęstością
Z prawa gazu doskonałego:

$$ PV = \left(\frac{N}{N_A}\right)RT = NkT \label{eqn:ideal_gas_law}\tag{8}$$

stąd:

$$ \begin{gather*}
P = \frac{NkT}{V} = nkT, \\
n = \frac{P}{kT} 
\end{gather*} \label{eqn:relation_between_T_P_n}\tag{9}$$

Czyli gęstość plazmy jest odwrotnie proporcjonalna do temperatury ($kT$) i proporcjonalna do ciśnienia ($P$).

## Klasyfikacja plazmy: plazma niskotemperaturowa vs. wysokotemperaturowa

| Low-temperature<br> non-thermal cold plasma | Low-temperature thermal<br> cold plasma | High-temperature<br> hot plasma |
| --- | --- | --- |
| $T_i \approx T \approx 300 \mathrm{K}$<br>$T_i \ll T_e \leqslant 10^5 \mathrm{K}$ | $T_i \approx T_e \approx T < 2 \times 10^4 \mathrm{K}$ | $T_i \approx T_e > 10^6 \mathrm{K}$ |
| Low pressure($\sim 100\mathrm{Pa}$)<br> glow and arc | Arcs at $100\mathrm{kPa}$ ($1\mathrm{atm}$) | Kinetic plasma, fusion plasma |

### Temperatura plazmy
Niech temperatura elektronów będzie $T_e$, jonów $T_i$, a cząstek neutralnych $T_g$. Wtedy:

- plazma niskotemperaturowa: $T_e \mathrm{(>10,000 K)} \gg T_i \approx T_g \mathrm{(\sim 100 K)}$ $\rightarrow$ plazma nierównowagowa (non-equilibrium plasma)
- plazma wysokotemperaturowa (termiczna): $T_e \approx T_i \approx T_g \mathrm{(>10,000 K)}$ $\rightarrow$ plazma równowagowa (equilibrium plasma)

### Gęstość plazmy
Niech gęstość elektronów będzie $n_e$, jonów $n_i$, a cząstek neutralnych $n_g$. Wtedy:

- plazma niskotemperaturowa: $n_g \gg n_i \approx n_e$ $\rightarrow$ mały stopień jonizacji, większość występuje jako cząstki neutralne
- plazma wysokotemperaturowa (termiczna): $n_g \approx n_i \approx n_e $ $\rightarrow$ duży stopień jonizacji

### Pojemność cieplna plazmy (jak bardzo jest „gorąca”?)
- plazma niskotemperaturowa: temperatura elektronów jest wysoka, ale gęstość jest niska, a większość stanowią względnie chłodne cząstki neutralne, więc pojemność cieplna jest mała i plazma nie jest „gorąca”
- plazma wysokotemperaturowa (termiczna): elektrony, jony i cząstki neutralne mają wysoką temperaturę, więc pojemność cieplna jest duża i plazma jest gorąca
