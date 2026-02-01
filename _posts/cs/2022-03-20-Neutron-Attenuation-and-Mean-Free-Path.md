---
title: Útlum neutronů (Neutron Attenuation) a střední volná dráha (Mean Free Path)
description: Vypočítá intenzitu monoenergetického neutronového svazku v závislosti na dráze v materiálu, odvodí střední volnou dráhu neutronu a ukáže, jak určit makroskopické účinné průřezy homogenních směsí a ekvivalentní účinný průřez molekul.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
redirect_from:
  - /posts/Homogeneous-Mixtures-and-Molecular-Cross-sections/
---

## Útlum neutronů (Neutron Attenuation)
Uvažujme monoenergetický neutronový svazek o intenzitě $I_0$, který dopadá na terč o tloušťce $X$, a ve vzdálenosti za terčem je umístěn detektor neutronů. Předpokládejme, že jak terč, tak detektor jsou velmi malé, a že detektor má malý prostorový úhel, takže dokáže zachytit jen část neutronů vycházejících z terče. Pak budou všechny neutrony, které do terče narazí, buď pohlceny, nebo rozptýleny a odkloněny jiným směrem; do detektoru tedy vstupují pouze neutrony, které s terčem nereagovaly.

Označme $I(x)$ intenzitu neutronového svazku, která zůstává po průchodu vzdáleností $x$ uvnitř terče bez srážky. Když neutronový svazek prochází terčem o dostatečně malé tloušťce $\tau$, počet srážek na jednotku plochy je $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (viz rovnice [(1)](/posts/Neutron-Interactions-and-Cross-sections/#ucinny-prurez-cross-section-neboli-mikroskopicky-ucinny-prurez-microscopic-cross-section) a [(8)](/posts/Neutron-Interactions-and-Cross-sections/#hustota-srazek-collision-density-tj-reakcni-rychlost-reaction-rate) v článku [Interakce neutronů a reakční účinné průřezy](/posts/Neutron-Interactions-and-Cross-sections/)). Proto je pokles intenzity neutronového svazku při postupu o $dx$ uvnitř terče dán:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Integrací dostaneme:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Intenzita neutronového svazku tedy s rostoucí dráhou v terči exponenciálně klesá.

## Střední volná dráha (Mean Free Path)
- průměrná vzdálenost, kterou neutron urazí od jedné srážky s jádrem do následující srážky s jiným jádrem
- tj. průměrná vzdálenost, kterou neutron urazí bez srážky
- značí se $\lambda$

$I(x)/I_0=e^{-\Sigma_t x}$ vyjadřuje pravděpodobnost, že neutron při postupu o vzdálenost $x$ v prostředí nenarazí na jádro. Pravděpodobnost, že neutron dojde bez srážky až do vzdálenosti $x$ a poté se srazí v intervalu $dx$, tedy $p(x)dx$, je:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

Odtud lze *střední volnou dráhu (mean free path)* $\lambda$ určit následovně:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## Makroskopický účinný průřez homogenní směsi (Homogeneous Mixture)
Uvažujme směs, v níž jsou rovnoměrně promíchány dva nuklidy $X$ a $Y$. Nechť jsou atomové hustoty jednotlivých nuklidů $N_X$ a $N_Y$ v jednotkách $\text{atom/cm}^3$ a mikroskopické účinné průřezy pro jistou konkrétní reakci neutronu s těmito jádry jsou $\sigma_X$, $\sigma_Y$.

Protože pravděpodobnosti srážky neutronu na jednotku délky s jádry $X$ a $Y$ jsou $\Sigma_X=N_X\sigma_X$, $\Sigma_Y=N_Y\sigma_Y$ (viz [Makroskopický účinný průřez](/posts/Neutron-Interactions-and-Cross-sections/#makroskopicky-ucinny-prurez-macroscopic-cross-section)), celková pravděpodobnost reakce na jednotku délky s oběma typy jader je:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## Ekvivalentní účinný průřez molekuly (Equivalent Cross-section)
Pokud se výše uvažovaná jádra vyskytují ve formě molekul, lze ekvivalentní účinný průřez (equivalent cross-section) dané molekuly definovat tak, že makroskopický účinný průřez směsi vypočtený ze vztahu ($\ref{eqn:cross_section_of_mixture}$) vydělíme počtem molekul na jednotku objemu.

Je-li v jednotkovém objemu $N$ molekul $X_mY_n$, pak $N_X=mN$, $N_Y=nN$ a ze vztahu ($\ref{eqn:cross_section_of_mixture}$) dostaneme účinný průřez této molekuly:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> Vztahy ($\ref{eqn:cross_section_of_mixture}$) a ($\ref{eqn:equivalent_cross_section}$) platí za předpokladu, že jádra $X$ a $Y$ reagují s neutrony vzájemně nezávisle; jsou použitelné pro všechny typy neutronových reakcí kromě [elastického rozptylu](/posts/Neutron-Interactions-and-Cross-sections/#elasticky-rozptyl-elastic-scattering).
> U elastického rozptylu neutronů na molekulách a pevných látkách (zejména v oblasti nízkých energií) tento předpoklad nelze použít, a proto je třeba rozptylový účinný průřez určit experimentálně.
{: .prompt-warning }
