---
title: Przekazywanie energii wskutek zderzeń w plazmie
description: Wyznaczamy tempo przekazywania energii w zderzeniach cząstek w plazmie, rozdzielając je na zderzenia sprężyste i niesprężyste, a następnie porównujemy jego wielkość dla przypadków, gdy masy zderzających się cząstek są zbliżone oraz gdy znacznie się różnią.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
redirect_from:
  - /posts/energy-transfer-by-collisions/
---
## TL;DR
> - Podczas zderzenia całkowita energia i pęd są zachowane
> - Jony, które utraciły wszystkie elektrony i pozostało w nich tylko jądro, oraz elektrony mają wyłącznie energię kinetyczną ruchu
> - Atomy obojętne oraz jony, które utraciły tylko część elektronów, posiadają energię wewnętrzną; w zależności od zmiany energii potencjalnej może zachodzić wzbudzenie (excitation), odwzbudzenie (deexcitation) lub jonizacja (ionization)
> - Klasyfikacja typów zderzeń według zmiany energii kinetycznej przed i po zderzeniu:
>   - zderzenie sprężyste (elastic collision): suma energii kinetycznej przed i po zderzeniu jest stała
>   - zderzenie niesprężyste (inelastic collision): w trakcie zderzenia energia kinetyczna ulega stracie
>     - wzbudzenie (excitation)
>     - jonizacja (ionization)
>   - zderzenie supersprężyste (superelastic collision): w trakcie zderzenia energia kinetyczna wzrasta
>     - odwzbudzenie (deexcitation)
> - Tempo przekazywania energii w zderzeniu sprężystym:
>   - tempo przekazywania energii w pojedynczym zderzeniu: $\zeta_L = \cfrac{4m_1m_2}{(m_1+m_2)^2}\cos^2\theta_2$
>   - średnie tempo przekazywania energii na zderzenie: $\overline{\zeta_L} = \cfrac{4m_1m_2}{(m_1+m_2)^2}\overline{\cos^2\theta_2} = \cfrac{2m_1m_2}{(m_1+m_2)^2}$
>     - gdy $m_1 \approx m_2$: $\overline{\zeta_L} \approx \cfrac{1}{2}$, więc zachodzi efektywne przekazywanie energii i szybko osiąga się równowagę termiczną
>     - gdy $m_1 \ll m_2$ lub $m_1 \gg m_2$: $\overline{\zeta_L} \approx 10^{-5}\sim 10^{-4}$, więc sprawność przekazywania energii jest bardzo mała i trudno osiągnąć równowagę termiczną. To wyjaśnia, dlaczego w słabo zjonizowanej plazmie zachodzi $T_e \gg T_i \approx T_n$, tj. temperatura elektronów znacznie różni się od temperatury jonów i atomów obojętnych.
>
> - Tempo przekazywania energii w zderzeniu niesprężystym:
>   - maksymalny udział konwersji na energię wewnętrzną w pojedynczym zderzeniu: $\zeta_L = \cfrac{\Delta U_\text{max}}{\cfrac{1}{2}m_1v_1^2} = \cfrac{m_2}{m_1+m_2}\cos^2\theta_2$
>   - średni maksymalny udział konwersji na energię wewnętrzną: $\overline{\zeta_L} = \cfrac{m_2}{m_1+m_2}\overline{\cos^2\theta_2} = \cfrac{m_2}{2(m_1+m_2)}$
>     - gdy $m_1 \approx m_2$: $\overline{\zeta_L} \approx \cfrac{1}{4}$
>     - gdy $m_1 \gg m_2$: $\overline{\zeta_L} \approx 10^{-5}\sim 10^{-4}$
>     - gdy $m_1 \ll m_2$: $\overline{\zeta_L} = \cfrac{1}{2}$, czyli najefektywniej można podnieść energię wewnętrzną obiektu zderzenia (jonu lub atomu obojętnego) i wprowadzić go w stan wzbudzony. To wyjaśnia, dlaczego łatwo zachodzą m.in. jonizacja przez elektrony (powstawanie plazmy), wzbudzenie (emisja światła) oraz dysocjacja (dissociation) cząsteczek (powstawanie rodników).
{: .prompt-info }

## Wymagania wstępne
- [Cząstki subatomowe i składniki atomu](/posts/constituents-of-an-atom/)

## Zderzenia między cząstkami w plazmie
- Podczas zderzenia całkowita energia i pęd są zachowane
- Jony, które utraciły wszystkie elektrony i pozostało w nich tylko jądro, oraz elektrony mają wyłącznie energię kinetyczną ruchu
- Atomy obojętne oraz jony, które utraciły tylko część elektronów, posiadają energię wewnętrzną; w zależności od zmiany energii potencjalnej może zachodzić wzbudzenie (excitation), odwzbudzenie (deexcitation) lub jonizacja (ionization)
- Klasyfikacja typów zderzeń według zmiany energii kinetycznej przed i po zderzeniu:
  - zderzenie sprężyste (elastic collision): suma energii kinetycznej przed i po zderzeniu jest stała
  - zderzenie niesprężyste (inelastic collision): w trakcie zderzenia energia kinetyczna ulega stracie
    - wzbudzenie (excitation)
    - jonizacja (ionization)
  - zderzenie supersprężyste (superelastic collision): w trakcie zderzenia energia kinetyczna wzrasta
    - odwzbudzenie (deexcitation)

## Przekazywanie energii w zderzeniu sprężystym

![Elastic collision](/assets/img/energy-transfer-by-collisions/elastic-collision.png)

### Tempo przekazywania energii w pojedynczym zderzeniu
W zderzeniu sprężystym pęd i energia kinetyczna są zachowane przed i po zderzeniu.

Zapisując równania zachowania pędu względem osi $x$ oraz $y$, otrzymujemy

$$ \begin{gather*}
m_1v_1 = m_1v_1^{\prime}\cos\theta_1 + m_2v_2^{\prime}\cos\theta_2, \label{eqn:momentum_conservation_x}\tag{1} \\
m_1v_1^{\prime}\sin\theta_1 = m_2v_2^{\prime}\sin\theta_2 \label{eqn:momentum_conservation_y}\tag{2}
\end{gather*} $$

oraz z zachowania energii

$$ \frac{1}{2}m_1v_1^2 = \frac{1}{2}m_1{v_1^{\prime}}^2 + \frac{1}{2}m_2{v_2^{\prime}}^2 $$

$$ v_1^2 = {v_1^{\prime}}^2 + \frac{m_2}{m_1}{v_2^{\prime}}^2 \label{eqn:energy_conservation}\tag{3}$$

Z równania ($\ref{eqn:momentum_conservation_x}$) mamy

$$ m_1 v_1^{\prime} \cos \theta_1  = m_1v_1 - m_2v_2^{\prime} \cos \theta_2 \label{eqn:momentum_conservation_x_2}\tag{4} $$

a po podniesieniu do kwadratu obu stron równań ($\ref{eqn:momentum_conservation_y}$) i ($\ref{eqn:momentum_conservation_x_2}$) oraz ich zsumowaniu

$$ \begin{align*}
(m_1v_1^{\prime})^2 &= (m_2 v_2^\prime \sin \theta_2)^2 + (m_1 v_1 - m_2 v_2^\prime \cos \theta_2)^2 \\
&= m_1^2 v_1^2 - 2 m_1 m_2 v_1 v_2^\prime \cos \theta_2 + m_2^2 {v_2^\prime}^2 \tag{5}
\end{align*} $$

Dzieląc obie strony przez $m_1^2$, dostajemy

$$ {v_1^{\prime}}^2 = v_1^2 - 2 \frac{m_2}{m_1} v_1 v_2^\prime \cos \theta_2 + \left(\frac{m_2}{m_1}\right)^2 {v_2^\prime}^2 \label{eqn:momentum_conservation}\tag{6}$$

Po podstawieniu do tego równania wyrażenia ($\ref{eqn:energy_conservation}$) można je uporządkować do postaci

$$ \begin{gather*}
\left( \frac{m_2}{m_1} \right) {v_2^\prime}^2 = 2 \left( \frac{m_2}{m_1} \right) v_1 v_2^\prime \cos \theta_2 - \left( \frac{m_2}{m_1} \right)^2 {v_2^\prime}^2 \\
2v_1 \cos \theta_2 = \left(\frac{m_1 + m_2}{m_1} \right) v_2^\prime \\
v_2^{\prime} = \frac{2m_1v_1\cos\theta_2}{m_1 + m_2}. \label{eqn:v_2_prime}\tag{7}
\end{gather*} $$

Stąd otrzymujemy tempo przekazywania energii $\zeta_L$:

$$ \begin{align*}
\therefore \zeta_L &= \frac{\cfrac{1}{2}m_2{v_2^\prime}^2}{\cfrac{1}{2}m_1v_1^2}  
= \frac{m_2}{m_1v_1^2} {\left(\frac{2m_1v_1\cos\theta_2}{m_1 + m_2} \right)}^2 \\
&= \frac{4m_1m_2}{(m_1+m_2)^2}\cos^2\theta_2. \quad \blacksquare \label{eqn:elastic_E_transfer_rate}\tag{8}
\end{align*} $$

### Średnie tempo przekazywania energii na zderzenie
Dla kątów od $0$ do $2\pi$ zachodzi $\sin^2{\theta_2}+\cos^2{\theta_2}=1$ oraz $\overline{\sin^2{\theta_2}}=\overline{\cos^2{\theta_2}}$, zatem

$$ \begin{align*}
\overline{\cos^2{\theta_2}} &= \overline{(1-\sin^2{\theta_2})} = 1 - \overline{\sin^2{\theta_2}} \\
&= 1 - \overline{\cos^2{\theta_2}} 
\end{align*} $$

$$ \begin{gather*}
2 \cdot \overline{\cos^2{\theta_2}} = 1 \\
\overline{\cos^2{\theta_2}} = \frac{1}{2}.
\end{gather*} $$

Podstawiając to do wcześniej uzyskanego wyrażenia ($\ref{eqn:elastic_E_transfer_rate}$), dostajemy

$$ \overline{\zeta_L} = \frac{4m_1m_2}{(m_1+m_2)^2}\overline{\cos^2\theta_2} = \frac{2m_1m_2}{(m_1+m_2)^2}. \quad \blacksquare \label{eqn:elastic_E_mean_transfer_rate}\tag{9} $$

#### Gdy $m_1 \approx m_2$
Dotyczy to zderzeń elektron–elektron, jon–jon, atom obojętny–atom obojętny oraz jon–atom obojętny. W takim przypadku

$$ \overline{\zeta_L} = \frac{2m_1m_2}{(m_1+m_2)^2} \approx \frac{1}{2} \label{eqn:elastic_similar_m}\tag{10}$$

czyli zachodzi efektywne przekazywanie energii i szybko osiąga się równowagę termiczną.

#### Gdy $m_1 \ll m_2$ lub $m_1 \gg m_2$
Dotyczy to zderzeń elektron–jon, elektron–atom obojętny, jon–elektron oraz atom obojętny–elektron. Wtedy

$$ \overline{\zeta_L} = \frac{2m_1m_2}{(m_1+m_2)^2} \approx \frac{2m_1}{m_2}\text{ (dla }m_1 \ll m_2\text{)} \approx 10^{-5}\sim 10^{-4} \label{eqn:elastic_different_m}\tag{11}$$

a więc sprawność przekazywania energii jest bardzo niska i niełatwo osiągnąć równowagę termiczną. To jest powód, dla którego w słabo zjonizowanej plazmie występuje $T_e \gg T_i \approx T_n$, tzn. temperatura elektronów znacząco różni się od temperatury jonów i atomów obojętnych.

## Przekazywanie energii w zderzeniu niesprężystym
![Inelastic collision](/assets/img/energy-transfer-by-collisions/inelastic-collision.png)

### Maksymalny udział konwersji na energię wewnętrzną w pojedynczym zderzeniu
Zachowanie pędu (równanie [$\ref{eqn:momentum_conservation}$]) pozostaje w tym przypadku takie samo, jednak ponieważ jest to zderzenie niesprężyste, energia kinetyczna nie jest zachowana. Utracona w zderzeniu niesprężystym energia kinetyczna zostaje przekształcona w energię wewnętrzną $\Delta U$, więc

$$ \Delta U = \frac{1}{2} m_1 v_1^2 - \left( \frac{1}{2} m_1 {v_1^{\prime}}^2 + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right) \label{eqn:delta_U}\tag{12} $$

Po podstawieniu tutaj równania ($\ref{eqn:momentum_conservation}$) i uporządkowaniu otrzymujemy

$$\begin{align*}
\Delta U &= \frac{1}{2} m_1 v_1^2 - \left[ \frac{1}{2} m_1 \left( v_1^2 - 2 \frac{m_2}{m_1} v_1 v_2^{\prime} \cos \theta_2 + \left( \frac{m_2}{m_1} v_2^{\prime} \right)^2 \right) + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right] \\
&= \frac{1}{2} m_1 v_1^2 - \left[ \frac{1}{2} m_1 v_1^2 - m_2 v_1 v_2^{\prime} \cos \theta_2 + \frac{1}{2} \frac{m_2^2}{m_1} {v_2^{\prime}}^2 + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right] \\
&= m_2 v_1 v_2^{\prime} \cos \theta_2 - \frac{1}{2}m_2{v_2^{\prime}}^2\left(\frac{m_1 + m_2}{m_1}\right) \label{eqn:delta_U_2}\tag{13}
\end{align*}$$.

Różniczkując $\Delta U$ względem $v_2^\prime$ i wyznaczając ekstremum, dla którego pochodna wynosi $0$, oraz wartość maksymalną w tym punkcie, dostajemy

$$ \cfrac{d \Delta U}{d v_2^{\prime}} = m_2 v_1 \cos \theta_2 - m_2 v_2^{\prime} \left( \frac{m_1 + m_2}{m_1} \right) = 0 \tag{14}$$

$$ \begin{gather*} 
v_2^{\prime} \left( \frac{m_1 + m_2}{m_1} \right) = v_1 \cos \theta_2 \\
v_2^\prime = \frac{m_1v_1\cos\theta_2}{m_1+m_2}.
\end{gather*} $$

$$ \therefore v_2^{\prime} = \frac{m_1v_1\cos\theta_2}{m_1+m_2}
\text{ gdy } \Delta U_\text{max} = \frac{1}{2}\frac{m_1m_2 v_1^2 \cos^2\theta_2}{m_1 + m_2}. \label{eqn:delta_U_max}\tag{15}$$

Stąd maksymalny możliwy udział konwersji energii kinetycznej na energię wewnętrzną w pojedynczym zderzeniu niesprężystym, $\zeta_L$, wynosi

$$ \zeta_L = \frac{\Delta U_\text{max}}{\cfrac{1}{2}m_1v_1^2} = \frac{m_2}{m_1+m_2}\cos^2\theta_2. \quad \blacksquare \label{eqn:inelastic_E_transfer_rate}\tag{16}$$

### Średni maksymalny udział konwersji na energię wewnętrzną
Analogicznie, podstawiając $\overline{\cos^2{\theta_2}} = \cfrac{1}{2}$ do ($\ref{eqn:inelastic_E_transfer_rate}$), otrzymujemy

$$ \overline{\zeta_L} = \frac{m_2}{m_1+m_2}\overline{\cos^2\theta_2} = \frac{m_2}{2(m_1+m_2)}. \label{eqn:inelastic_E_mean_transfer_rate}\tag{17}$$

#### Gdy $m_1 \approx m_2$
Dotyczy to zderzeń jon–jon, jon–atom obojętny oraz atom obojętny–atom obojętny.

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} = \frac{1}{4}. \label{eqn:inelastic_similar_m}\tag{18}$$

#### Gdy $m_1 \gg m_2$
Dotyczy to zderzeń jon–elektron oraz atom obojętny–elektron.

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} \approx \frac{m_2}{2m_1} \approx 10^{-5}\sim 10^{-4}. \label{eqn:inelastic_ion_electron}\tag{19}$$

#### Gdy $m_1 \ll m_2$
Dotyczy to zderzeń elektron–jon oraz elektron–atom obojętny. Dwa poprzednie przypadki nie różniły się zasadniczo od sytuacji w zderzeniu sprężystym, natomiast ten trzeci przypadek wykazuje istotną różnicę. Wtedy

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} \approx \frac{m_2}{2m_2} = \frac{1}{2} \label{eqn:inelastic_electron_ion}\tag{20}$$

czyli można najefektywniej podnieść energię wewnętrzną obiektu zderzenia (jonu lub atomu obojętnego) i wprowadzić go w stan wzbudzony. Jak zostanie omówione później, to właśnie dlatego łatwo zachodzą m.in. jonizacja przez elektrony (powstawanie plazmy), wzbudzenie (emisja światła) oraz dysocjacja (dissociation) cząsteczek (powstawanie rodników).
