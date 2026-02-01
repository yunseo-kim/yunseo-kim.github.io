---
title: Reakcje jądrowe i energia wiązania
description: Omawiamy zapis reakcji jądrowych i definicję wartości Q, a także pojęcia ubytku masy oraz energii wiązania jądra.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Nuclear Reaction, Nuclear Radiation]
math: true
image: /assets/img/atoms.webp
---
## Reakcja jądrowa (Nuclear Reaction)
### Podstawowe prawa w reakcji jądrowej
*Reakcja jądrowa (nuclear reaction)*: reakcja, w której dwa różne jądra atomowe lub jądro atomowe i nukleon zderzają się, wytwarzając co najmniej dwa nowe cząstki jądrowe lub promieniowanie gamma.

Jeśli dwa jądra atomowe $a$, $b$ reagują i w produktach powstają jądra (lub promieniowanie gamma) $c$, $d$, to reakcję tę zapisuje się następująco:

$$ a + b \rightarrow c + d \tag{1} \label{nuclear_reaction}$$

W reakcjach jądrowych spełnione są cztery podstawowe prawa:

- *Prawo zachowania liczby nukleonów (conservation of nucleon)*: całkowita liczba nukleonów przed i po reakcji jest taka sama. Ponieważ typ nukleonu może się zmieniać, liczba protonów i liczba neutronów nie muszą być zachowane osobno.
- *Prawo zachowania ładunku (conservation of charge)*: suma ładunków cząstek przed i po reakcji jest taka sama.
- *Prawo zachowania pędu (conservation of momentum)*: suma pędów cząstek przed i po reakcji jest taka sama.
- *Prawo zachowania energii (conservation of energy)*: całkowita energia, <u>włącznie z energią spoczynkową masy</u>, jest taka sama przed i po reakcji.

### Reakcja egzotermiczna (exothermic reaction) i endotermiczna (endothermic reaction)
W reakcji jądrowej z równania ($\ref{nuclear_reaction}$) całkowita energia przed reakcją jest sumą energii spoczynkowej i energii kinetycznej $a$ oraz $b$, a całkowita energia po reakcji jest sumą energii spoczynkowej i energii kinetycznej $c$ oraz $d$. Zatem z prawa zachowania energii wynika:

$$ E_a + E_b + M_a c^2 + M_b c^2 = E_c + E_d + M_c c^2 + M_d c^2. $$

Po przekształceniu otrzymujemy:

$$ (E_c + E_d) - (E_a + E_b) = [(M_a + M_b) - (M_c + M_d)]c^2. $$

Innymi słowy, różnica energii kinetycznych przed i po reakcji jest równa różnicy mas spoczynkowych przed i po reakcji. Prawą stronę ostatniego równania nazywa się *wartością Q (Q-value)* reakcji jądrowej i definiuje następująco:

$$ Q = [(M_a + M_b) - (M_c + M_d)]c^2 \ \text{MeV}.\tag{2} \label{Q_value} $$

Wartość Q zawsze podaje się w MeV; ponieważ energia spoczynkowa odpowiadająca masie 1 amu wynosi zwykle 931 MeV, wartość Q można też zapisać jako:

$$ Q = [(M_a + M_b) - (M_c + M_d)]\cdot 931 \ \text{MeV}.\tag{3} $$

- *Reakcja egzotermiczna (exothermic reaction)*: reakcja jądrowa z $Q>0$; część masy zamienia się na energię kinetyczną, więc po reakcji energia kinetyczna rośnie.
- *Reakcja endotermiczna (endothermic reaction)*: reakcja jądrowa z $Q<0$; część energii kinetycznej zamienia się na masę, więc po reakcji energia kinetyczna maleje.

| Rodzaj reakcji jądrowej | Wartość Q | Zmiana masy przed/po | Zmiana energii kinetycznej przed/po |
| :---: | :---: | :---: | :---: |
| Reakcja egzotermiczna | $Q>0$ | $\Delta m<0$ (spadek) | $\Delta E>0$ (wzrost) |
| Reakcja endotermiczna | $Q<0$ | $\Delta m>0$ (wzrost) | $\Delta E<0$ (spadek) |

### Skrócony zapis reakcji jądrowej
Reakcję jądrową z równania ($\ref{nuclear_reaction}$) można skrótowo zapisać jako:

$$ a(b, c)d $$

Oznacza to reakcję, w której w jądro $a$ pada cząstka $b$, emitowana jest cząstka $c$, a $a$ ulega przemianie w $d$.

#### np.)
- $^{16} \text{O}(n,p)^{16}\text{N}$
- $^{14} \text{N}(n,p)^{14}\text{C}$
- $^{3} \text{H}(d,n)^{4}\text{He}$
- $p(n,\gamma)d$

## Energia wiązania (Binding Energy)
### Ubytek masy (Mass Defect)
Masa każdego jądra jest nieco mniejsza niż suma mas neutronów i protonów, z których to jądro się składa. Tę różnicę nazywa się *ubytkiem masy (mass defect)*.

Jeśli masę jądra oznaczymy przez $M_A$, to ubytek masy $\Delta$ dla dowolnego jądra można obliczyć jako:

$$ \Delta = ZM_p + NM_n - M_A. $$

Gdy ubytek masy $\Delta$ wyrazi się w jednostkach energii, otrzymuje się energię potrzebną do rozbicia danego jądra na jego nukleony składowe. Ponieważ jest to energia „wiązania” nukleonów w jądrze, nazywa się ją *energią wiązania (binding energy)*. Odwrotnie, gdy z $A$ nukleonów tworzy się jądro atomowe, poziom energii obniża się o energię wiązania $\Delta$, więc w trakcie reakcji jądrowej taka ilość energii zostaje wypromieniowana do otoczenia.

### Średnia energia wiązania na nukleon
Całkowita energia wiązania jądra rośnie wraz ze wzrostem liczby masowej $A$, ale nachylenie tej zależności nie jest stałe.  
![the average binding energy per nucleon for a varied number of neutrons](https://upload.wikimedia.org/wikipedia/commons/5/53/Binding_energy_curve_-_common_isotopes.svg)  
Średnia energia wiązania na nukleon $\Delta/A$ w obszarze małych liczb masowych rośnie stromo, natomiast dla ciężkich jąder o $A\geq56$ maleje łagodnie, co można potwierdzić na powyższym wykresie.

### Związek między wartością Q reakcji jądrowej a energią wiązania
W reakcji jądrowej z równania ($\ref{nuclear_reaction}$) energia wiązania jądra $a$ wynosi

$$ \text{BE}(a) = Z_a M_p + N_a M_n - M_a $$

a masa jądra $a$ jest równa

$$ M_a = Z_a M_p + N_a M_n - \text{BE}(a) $$

W ten sam sposób dla jąder $b$, $c$, $d$:

$$ \begin{align*}
M_b &= Z_b M_p + N_b M_n - \text{BE}(b) \\
M_c &= Z_c M_p + N_c M_n - \text{BE}(c) \\
M_d &= Z_d M_p + N_d M_n - \text{BE}(d) \\
\end{align*} $$

Zakładając, że

$$ \begin{align*}
Z_a + Z_b &= Z_c + Z_d\, , \\
N_a + N_b &= N_c + N_d
\end{align*}$$

i podstawiając powyższe zależności do równania ($\ref{Q_value}$), otrzymujemy:

$$ Q = [\text{BE}(c) + \text{BE}(d)] - [\text{BE}(a) + \text{BE}(b)] $$

Oznacza to, że gdy w wyniku reakcji jądrowej dwa mniej stabilne jądra łączą się, tworząc jądro bardziej stabilne, zawsze następuje wydzielenie energii.

### Synteza jądrowa (Nuclear Fusion) i rozszczepienie jądrowe (Nuclear Fission)
W przypadku reakcji, w której deuter o energii wiązania $2.23\text{MeV}$ oraz tryt o energii wiązania $8.48\text{MeV}$ łączą się, tworząc $^4\text{He}$ o energii wiązania $28.3\text{MeV}$ i emitując jeden neutron:

$$ ^2\text{H} + {^3\text{H}} \rightarrow {^4\text{He}} + n \tag{4} \label{nuclear_fusion}$$

uwalniana jest energia równa różnicy energii wiązań przed i po reakcji, tj. $28.3-(2.23+8.48)=17.6\text{MeV}$ (czyli $3.52\text{MeV}$ na nukleon), w postaci energii kinetycznej jądra helu i neutronu.

Reakcję, w której — jak w ($\ref{nuclear_fusion}$) — dwa lekkie jądra o małej liczbie masowej łączą się, tworząc cięższe jądro o większej liczbie masowej niż przed reakcją, nazywa się *syntezą jądrową (nuclear fusion)*. Jest ona źródłem energii Słońca i wszystkich gwiazd, a w przyszłości ludzkość będzie mogła wykorzystać ją bezpośrednio jako źródło napędu.

Z kolei w przypadku reakcji, w której $^{235}\text{U}$ o energii wiązania około $1780\text{MeV}$ po pochłonięciu neutronu rozdziela się na $^{92}\text{Kr}$ o energii wiązania $783\text{MeV}$ oraz $^{141}\text{Ba}$ o energii wiązania około $1170\text{MeV}$, emitując trzy neutrony:

$$ {^{235}\text{U}} + n \rightarrow {^{92}\text{Kr}} + {^{141}\text{Ba}} + 3n \tag{5} \label{nuclear_fission}$$

uwalniana jest energia odpowiadająca różnicy energii wiązania przed i po reakcji: $783+1170-1780=173\text{MeV}$ (czyli $0.733\text{MeV}$ na nukleon).

Reakcję, w której — jak w ($\ref{nuclear_fission}$) — ciężkie jądro rozpada się na lżejsze jądra, nazywa się *rozszczepieniem jądrowym (nuclear fission)*; od przemówienia „Pokojowe wykorzystanie energii atomowej (Atoms for Peace)” 34. prezydenta USA Dwighta D. Eisenhowera oraz od uruchomienia radzieckiej elektrowni jądrowej w Obnińsku jest ono szeroko wykorzystywane jako źródło energii elektrycznej.

## Liczby magiczne
Gdy liczba neutronów lub liczba protonów w jądrze wynosi 2, 6, 8, 14, 20, 28, 50, 82 lub 126, jądro wykazuje szczególnie dużą stabilność. Taką liczbę nukleonów nazywa się *liczbą magiczną (magic number)*. Są to liczby neutronów i protonów potrzebne do zapełnienia powłok nukleonowych w jądrze, analogicznie do zapełniania powłok elektronowych poza jądrem.

Nuklidy odpowiadające liczbom magicznym bywają w inżynierii jądrowej wykorzystywane praktycznie. Typowym przykładem jest cyrkon-90 ($^{90}_{40} \mathrm{Zr}$) mający 50 neutronów: jest stabilny i ma własność słabego pochłaniania neutronów, dzięki czemu jest szeroko stosowany m.in. jako materiał koszulek (płaszcz) prętów paliwowych w rdzeniu reaktora.
