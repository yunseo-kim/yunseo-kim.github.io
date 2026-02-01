---
title: Přenos energie při srážkách v plazmatu
description: Odvodíme rychlost přenosu energie při srážkách částic v plazmatu zvlášť pro pružné a nepružné srážky a porovnáme její velikost pro případy, kdy jsou hmotnosti částic podobné, a kdy se výrazně liší.
categories: [Nuclear Engineering, Plasma Physics]
tags: [Nuclear Physics]
math: true
image: /assets/img/tokamak-plasma-cropped.webp
redirect_from:
  - /posts/energy-transfer-by-collisions/
---
## TL;DR
> - Při srážce se zachovává celková energie a hybnost
> - Ionty, které ztratily všechny elektrony a zůstalo jen atomové jádro, a elektrony mají pouze kinetickou energii
> - Neutrální atomy a ionty, které ztratily jen část elektronů, mají vnitřní energii; v závislosti na změně potenciální energie může docházet k excitaci (excitation), deexcitaci (deexcitation) nebo ionizaci (ionization)
> - Klasifikace typů srážek podle změny kinetické energie před a po srážce:
>   - pružná srážka (elastic collision): celková kinetická energie před a po srážce je konstantní
>   - nepružná srážka (inelastic collision): během srážky dochází ke ztrátě kinetické energie
>     - excitace (excitation)
>     - ionizace (ionization)
>   - superelastická srážka (superelastic collision): během srážky kinetická energie roste
>     - deexcitace (deexcitation)
> - Rychlost přenosu energie při pružných srážkách:
>   - rychlost přenosu energie při jednotlivé srážce: $\zeta_L = \cfrac{4m_1m_2}{(m_1+m_2)^2}\cos^2\theta_2$
>   - průměrná rychlost přenosu energie na srážku: $\overline{\zeta_L} = \cfrac{4m_1m_2}{(m_1+m_2)^2}\overline{\cos^2\theta_2} = \cfrac{2m_1m_2}{(m_1+m_2)^2}$
>     - když $m_1 \approx m_2$: $\overline{\zeta_L} \approx \cfrac{1}{2}$, takže dochází k efektivnímu přenosu energie a rychle se dosáhne tepelné rovnováhy
>     - když $m_1 \ll m_2$ nebo $m_1 \gg m_2$: $\overline{\zeta_L} \approx 10^{-5}\sim 10^{-4}$, takže účinnost přenosu energie je velmi nízká a tepelné rovnováhy se dosahuje obtížně. To je důvod, proč je ve slabě ionizovaném plazmatu $T_e \gg T_i \approx T_n$ a elektronová teplota se výrazně liší od teploty iontů i neutrálních atomů.
>
> - Rychlost přenosu energie při nepružných srážkách:
>   - maximální míra převodu do vnitřní energie při jedné srážce: $\zeta_L = \cfrac{\Delta U_\text{max}}{\cfrac{1}{2}m_1v_1^2} = \cfrac{m_2}{m_1+m_2}\cos^2\theta_2$
>   - průměrná maximální míra převodu do vnitřní energie: $\overline{\zeta_L} = \cfrac{m_2}{m_1+m_2}\overline{\cos^2\theta_2} = \cfrac{m_2}{2(m_1+m_2)}$
>     - když $m_1 \approx m_2$: $\overline{\zeta_L} \approx \cfrac{1}{4}$
>     - když $m_1 \gg m_2$: $\overline{\zeta_L} \approx 10^{-5}\sim 10^{-4}$
>     - když $m_1 \ll m_2$: $\overline{\zeta_L} = \cfrac{1}{2}$, takže lze nejefektivněji zvýšit vnitřní energii sráženého objektu (iontu nebo neutrálního atomu) a uvést jej do excitovaného stavu. To je důvod, proč snadno probíhá ionizace elektrony (vznik plazmatu), excitace (emise světla), disociace (dissociation) molekul (tvorba radikálů) apod.
{: .prompt-info }

## Předpoklady
- [Subatomární částice a stavební složky atomu](/posts/constituents-of-an-atom/)

## Srážky částic v plazmatu
- Při srážce se zachovává celková energie a hybnost
- Ionty, které ztratily všechny elektrony a zůstalo jen atomové jádro, a elektrony mají pouze kinetickou energii
- Neutrální atomy a ionty, které ztratily jen část elektronů, mají vnitřní energii; v závislosti na změně potenciální energie může docházet k excitaci (excitation), deexcitaci (deexcitation) nebo ionizaci (ionization)
- Klasifikace typů srážek podle změny kinetické energie před a po srážce:
  - pružná srážka (elastic collision): celková kinetická energie před a po srážce je konstantní
  - nepružná srážka (inelastic collision): během srážky dochází ke ztrátě kinetické energie
    - excitace (excitation)
    - ionizace (ionization)
  - superelastická srážka (superelastic collision): během srážky kinetická energie roste
    - deexcitace (deexcitation)

## Přenos energie při pružných srážkách

![Elastic collision](/assets/img/energy-transfer-by-collisions/elastic-collision.png)

### Rychlost přenosu energie při jednotlivé srážce
U pružné srážky se zachovává hybnost i kinetická energie před a po srážce.

Sestavíme-li rovnice zachování hybnosti pro osy $x$ a $y$, dostaneme

$$ \begin{gather*}
m_1v_1 = m_1v_1^{\prime}\cos\theta_1 + m_2v_2^{\prime}\cos\theta_2, \label{eqn:momentum_conservation_x}\tag{1} \\
m_1v_1^{\prime}\sin\theta_1 = m_2v_2^{\prime}\sin\theta_2 \label{eqn:momentum_conservation_y}\tag{2}
\end{gather*} $$

a dále ze zákona zachování energie

$$ \frac{1}{2}m_1v_1^2 = \frac{1}{2}m_1{v_1^{\prime}}^2 + \frac{1}{2}m_2{v_2^{\prime}}^2 $$

$$ v_1^2 = {v_1^{\prime}}^2 + \frac{m_2}{m_1}{v_2^{\prime}}^2 \label{eqn:energy_conservation}\tag{3}$$

Platí tedy.

Z rovnice ($\ref{eqn:momentum_conservation_x}$) plyne

$$ m_1 v_1^{\prime} \cos \theta_1  = m_1v_1 - m_2v_2^{\prime} \cos \theta_2 \label{eqn:momentum_conservation_x_2}\tag{4} $$

a po umocnění obou stran rovnic ($\ref{eqn:momentum_conservation_y}$) a ($\ref{eqn:momentum_conservation_x_2}$) na druhou a jejich sečtení dostaneme

$$ \begin{align*}
(m_1v_1^{\prime})^2 &= (m_2 v_2^\prime \sin \theta_2)^2 + (m_1 v_1 - m_2 v_2^\prime \cos \theta_2)^2 \\
&= m_1^2 v_1^2 - 2 m_1 m_2 v_1 v_2^\prime \cos \theta_2 + m_2^2 {v_2^\prime}^2 \tag{5}
\end{align*} $$

Nyní vydělíme obě strany $m_1^2$:

$$ {v_1^{\prime}}^2 = v_1^2 - 2 \frac{m_2}{m_1} v_1 v_2^\prime \cos \theta_2 + \left(\frac{m_2}{m_1}\right)^2 {v_2^\prime}^2 \label{eqn:momentum_conservation}\tag{6}$$

Dosadíme-li sem ($\ref{eqn:energy_conservation}$), lze to upravit takto:

$$ \begin{gather*}
\left( \frac{m_2}{m_1} \right) {v_2^\prime}^2 = 2 \left( \frac{m_2}{m_1} \right) v_1 v_2^\prime \cos \theta_2 - \left( \frac{m_2}{m_1} \right)^2 {v_2^\prime}^2 \\
2v_1 \cos \theta_2 = \left(\frac{m_1 + m_2}{m_1} \right) v_2^\prime \\
v_2^{\prime} = \frac{2m_1v_1\cos\theta_2}{m_1 + m_2}. \label{eqn:v_2_prime}\tag{7}
\end{gather*} $$

Odtud získáme rychlost přenosu energie $\zeta_L$ následovně:

$$ \begin{align*}
\therefore \zeta_L &= \frac{\cfrac{1}{2}m_2{v_2^\prime}^2}{\cfrac{1}{2}m_1v_1^2}  
= \frac{m_2}{m_1v_1^2} {\left(\frac{2m_1v_1\cos\theta_2}{m_1 + m_2} \right)}^2 \\
&= \frac{4m_1m_2}{(m_1+m_2)^2}\cos^2\theta_2. \quad \blacksquare \label{eqn:elastic_E_transfer_rate}\tag{8}
\end{align*} $$

### Průměrná rychlost přenosu energie na srážku
Protože pro úhly od $0$ do $2\pi$ platí $\sin^2{\theta_2}+\cos^2{\theta_2}=1$ a $\overline{\sin^2{\theta_2}}=\overline{\cos^2{\theta_2}}$, dostáváme

$$ \begin{align*}
\overline{\cos^2{\theta_2}} &= \overline{(1-\sin^2{\theta_2})} = 1 - \overline{\sin^2{\theta_2}} \\
&= 1 - \overline{\cos^2{\theta_2}} 
\end{align*} $$

$$ \begin{gather*}
2 \cdot \overline{\cos^2{\theta_2}} = 1 \\
\overline{\cos^2{\theta_2}} = \frac{1}{2}.
\end{gather*} $$

Dosazením do ($\ref{eqn:elastic_E_transfer_rate}$) dostaneme

$$ \overline{\zeta_L} = \frac{4m_1m_2}{(m_1+m_2)^2}\overline{\cos^2\theta_2} = \frac{2m_1m_2}{(m_1+m_2)^2}. \quad \blacksquare \label{eqn:elastic_E_mean_transfer_rate}\tag{9} $$

#### Když $m_1 \approx m_2$
Sem patří srážky elektron–elektron, ion–ion, neutrální atom–neutrální atom a ion–neutrální atom. V takovém případě

$$ \overline{\zeta_L} = \frac{2m_1m_2}{(m_1+m_2)^2} \approx \frac{1}{2} \label{eqn:elastic_similar_m}\tag{10}$$

tj. dochází k efektivnímu přenosu energie a rychle se dosáhne tepelné rovnováhy.

#### Když $m_1 \ll m_2$ nebo $m_1 \gg m_2$
Sem patří srážky elektron–ion, elektron–neutrální atom, ion–elektron a neutrální atom–elektron. V takovém případě

$$ \overline{\zeta_L} = \frac{2m_1m_2}{(m_1+m_2)^2} \approx \frac{2m_1}{m_2}\text{ (pro případ }m_1 \ll m_2 \text{)} \approx 10^{-5}\sim 10^{-4} \label{eqn:elastic_different_m}\tag{11}$$

takže účinnost přenosu energie je velmi nízká a tepelné rovnováhy se dosahuje obtížně. To je důvod, proč je ve slabě ionizovaném plazmatu $T_e \gg T_i \approx T_n$ a elektronová teplota se výrazně liší od teploty iontů i neutrálních atomů.

## Přenos energie při nepružných srážkách
![Inelastic collision](/assets/img/energy-transfer-by-collisions/inelastic-collision.png)

### Maximální míra převodu do vnitřní energie při jedné srážce
Zachování hybnosti (rovnice [$\ref{eqn:momentum_conservation}$]) platí i zde stejně, ale protože jde o nepružnou srážku, kinetická energie se nezachovává. Kinetická energie ztracená při nepružné srážce se převede na vnitřní energii $\Delta U$, takže

$$ \Delta U = \frac{1}{2} m_1 v_1^2 - \left( \frac{1}{2} m_1 {v_1^{\prime}}^2 + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right) \label{eqn:delta_U}\tag{12} $$

Dosadíme-li sem ($\ref{eqn:momentum_conservation}$) a upravíme, dostaneme

$$\begin{align*}
\Delta U &= \frac{1}{2} m_1 v_1^2 - \left[ \frac{1}{2} m_1 \left( v_1^2 - 2 \frac{m_2}{m_1} v_1 v_2^{\prime} \cos \theta_2 + \left( \frac{m_2}{m_1} v_2^{\prime} \right)^2 \right) + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right] \\
&= \frac{1}{2} m_1 v_1^2 - \left[ \frac{1}{2} m_1 v_1^2 - m_2 v_1 v_2^{\prime} \cos \theta_2 + \frac{1}{2} \frac{m_2^2}{m_1} {v_2^{\prime}}^2 + \frac{1}{2} m_2 {v_2^{\prime}}^2 \right] \\
&= m_2 v_1 v_2^{\prime} \cos \theta_2 - \frac{1}{2}m_2{v_2^{\prime}}^2\left(\frac{m_1 + m_2}{m_1}\right) \label{eqn:delta_U_2}\tag{13}
\end{align*}$$.

Zderivujeme-li $\Delta U$ podle $v_2^\prime$ a najdeme extrém, kde je derivace rovna $0$, a maximum v tomto bodě, dostaneme

$$ \cfrac{d \Delta U}{d v_2^{\prime}} = m_2 v_1 \cos \theta_2 - m_2 v_2^{\prime} \left( \frac{m_1 + m_2}{m_1} \right) = 0 \tag{14}$$

$$ \begin{gather*} 
v_2^{\prime} \left( \frac{m_1 + m_2}{m_1} \right) = v_1 \cos \theta_2 \\
v_2^\prime = \frac{m_1v_1\cos\theta_2}{m_1+m_2}.
\end{gather*} $$

$$ \therefore v_2^{\prime} = \frac{m_1v_1\cos\theta_2}{m_1+m_2}
\text{ když } \Delta U_\text{max} = \frac{1}{2}\frac{m_1m_2 v_1^2 \cos^2\theta_2}{m_1 + m_2}. \label{eqn:delta_U_max}\tag{15}$$

Odtud plyne, že maximální možná míra převodu kinetické energie na vnitřní energii při jedné nepružné srážce je

$$ \zeta_L = \frac{\Delta U_\text{max}}{\cfrac{1}{2}m_1v_1^2} = \frac{m_2}{m_1+m_2}\cos^2\theta_2. \quad \blacksquare \label{eqn:inelastic_E_transfer_rate}\tag{16}$$

### Průměrná maximální míra převodu do vnitřní energie
Analogicky dosadíme do ($\ref{eqn:inelastic_E_transfer_rate}$) $\overline{\cos^2{\theta_2}} = \cfrac{1}{2}$ a dostaneme

$$ \overline{\zeta_L} = \frac{m_2}{m_1+m_2}\overline{\cos^2\theta_2} = \frac{m_2}{2(m_1+m_2)}. \label{eqn:inelastic_E_mean_transfer_rate}\tag{17}$$

#### Když $m_1 \approx m_2$
Sem patří srážky ion–ion, ion–neutrální atom a neutrální atom–neutrální atom.

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} = \frac{1}{4}. \label{eqn:inelastic_similar_m}\tag{18}$$

#### Když $m_1 \gg m_2$
Sem patří srážky ion–elektron a neutrální atom–elektron.

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} \approx \frac{m_2}{2m_1} \approx 10^{-5}\sim 10^{-4}. \label{eqn:inelastic_ion_electron}\tag{19}$$

#### Když $m_1 \ll m_2$
Sem patří srážky elektron–ion a elektron–neutrální atom. Předchozí dva případy se příliš nelišily od chování u pružných srážek, ale tento třetí případ vykazuje důležitý rozdíl. V tomto případě

$$ \overline{\zeta_L} = \frac{m_2}{2(m_1+m_2)} \approx \frac{m_2}{2m_2} = \frac{1}{2} \label{eqn:inelastic_electron_ion}\tag{20}$$

tj. lze nejefektivněji zvýšit vnitřní energii sráženého objektu (iontu nebo neutrálního atomu) a uvést jej do excitovaného stavu. Jak bude probráno později, je to důvod, proč snadno probíhá ionizace elektrony (vznik plazmatu), excitace (emise světla), disociace (dissociation) molekul (tvorba radikálů) apod.
