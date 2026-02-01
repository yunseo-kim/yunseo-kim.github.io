---
title: Tłumienie neutronów (Neutron Attenuation) i średnia droga swobodna (Mean Free Path)
description: Obliczamy osłabienie monoenergetycznej wiązki neutronów w materiale, wyprowadzamy średnią drogę swobodną oraz makroskopowe przekroje mieszanin i cząsteczek.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Interaction of Radiation with Matter]
math: true
image: /assets/img/atoms.webp
redirect_from:
  - /posts/Homogeneous-Mixtures-and-Molecular-Cross-sections/
---

## Tłumienie neutronów (Neutron Attenuation)
Rozważmy monoenergetyczną wiązkę neutronów o natężeniu $I_0$, padającą na tarczę (materiał) o grubości $X$, a w pewnej odległości za tarczą znajduje się detektor neutronów. Załóżmy, że zarówno tarcza, jak i detektor są bardzo małe, a detektor ma mały kąt bryłowy, przez co może zarejestrować jedynie część neutronów wychodzących z tarczy. Wówczas wszystkie neutrony, które zderzą się w tarczy, zostaną pochłonięte albo rozproszone i odchylą się w innym kierunku, więc do detektora docierają tylko neutrony, które nie weszły w reakcję w tarczy.

Niech $I(x)$ oznacza natężenie wiązki neutronów, które pozostaje po przejściu przez odcinek $x$ w tarczy bez zderzenia. Gdy wiązka przechodzi przez bardzo cienką warstwę tarczy o grubości $\tau$, liczba zderzeń na jednostkę powierzchni wynosi $\Delta I = \sigma_t I\tau N = \Sigma_t I\tau \ \text{[neutrons/cm}^2\cdot\text{s]}$ (zob. wzory [(1)](/posts/Neutron-Interactions-and-Cross-sections/#przekr%C3%B3j-czynny-cross-section-lub-mikroskopowy-przekr%C3%B3j-czynny-microscopic-cross-section) i [(8)](/posts/Neutron-Interactions-and-Cross-sections/#g%C4%99sto%C5%9B%C4%87-zderze%C5%84-collision-density-tj-szybko%C5%9B%C4%87-reakcji-reaction-rate) we wpisie [Oddziaływania neutronów i przekroje czynne reakcji](/posts/Neutron-Interactions-and-Cross-sections/)), zatem ubytek natężenia wiązki podczas przejścia przez $dx$ w tarczy spełnia:

$$ -dI = \sigma_t IN dx = \Sigma_t I dx \tag{1} $$

Po scałkowaniu otrzymujemy:

$$ \frac{dI}{I} = -\Sigma_t dx $$

$$ I(x) = I_0e^{-\Sigma_t x} \tag{2} $$

Widać więc, że natężenie wiązki neutronów maleje wykładniczo wraz ze wzrostem drogi przebytej w tarczy.

## Średnia droga swobodna (Mean Free Path)
- średnia droga, jaką neutron przebywa od zderzenia z jednym jądrem do kolejnego zderzenia z innym jądrem
- czyli średnia odległość, jaką neutron pokonuje bez zderzeń
- oznaczana symbolem $\lambda$

Wyrażenie $I(x)/I_0=e^{-\Sigma_t x}$ oznacza prawdopodobieństwo, że neutron nie zderzy się z jądrem podczas przebycia w ośrodku drogi $x$. Zatem prawdopodobieństwo $p(x)dx$, że neutron dotrze bez zderzeń do odległości $x$, a następnie zderzy się w przedziale $dx$, wynosi:

$$ \begin{align*}
p(x)dx &= \frac{I(x)}{I_0} \Sigma_t dx
\\ &= e^{-\Sigma_t x}\times \Sigma_t dx
\\ &= \Sigma_t e^{-\Sigma_t x}dx
\end{align*}
$$

Stąd *średnią drogę swobodną (mean free path)* $\lambda$ można obliczyć następująco:

$$ \begin{align*}
\lambda &= \int_0^\infty xp(x)dx
\\ &= \Sigma_t \int_0^\infty xe^{-\Sigma_t x}dx
\\ &= \Sigma_t \left(\left[-\frac{1}{\Sigma_t}xe^{-\Sigma_t x} \right]_0^\infty +\int_0^\infty \frac{1}{\Sigma_t}e^{-\Sigma_t x} \right)
\\ &= \left[-\frac{1}{\Sigma_t}e^{-\Sigma_t x} \right]_0^\infty
\\ &= 1/\Sigma_t \label{eqn:mean_free_pass}\tag{3}
\end{align*}
$$

## Makroskopowy przekrój czynny jednorodnej mieszaniny (Homogeneous Mixture)
Rozważmy mieszaninę, w której dwa nuklidy $X$ i $Y$ są równomiernie wymieszane. Niech gęstości atomowe tych nuklidów wynoszą odpowiednio $N_X$ i $N_Y$ $\text{atom/cm}^3$, a mikroskopowe przekroje czynne dla pewnej reakcji neutron–jądro niech będą odpowiednio $\sigma_X$, $\sigma_Y$.

Wtedy prawdopodobieństwa zderzenia neutronu z jądrami $X$ i $Y$ na jednostkę długości wynoszą odpowiednio $\Sigma_X=N_X\sigma_X$, $\Sigma_Y=N_Y\sigma_Y$ (zob. [Makroskopowy przekrój czynny](/posts/Neutron-Interactions-and-Cross-sections/#makroskopowy-przekr%C3%B3j-czynny-macroscopic-cross-section)), więc całkowite prawdopodobieństwo reakcji na jednostkę długości z tymi dwoma jądrami jest równe:

$$ \Sigma = \Sigma_X + \Sigma_Y = N_X\sigma_X + N_Y\sigma_Y \label{eqn:cross_section_of_mixture}\tag{4}$$

## Równoważny przekrój czynny cząsteczki (Equivalent Cross-section)
Jeśli rozważane wyżej jądra występują w postaci cząsteczek, to dzieląc makroskopowy przekrój czynny mieszaniny wyznaczony ze wzoru ($\ref{eqn:cross_section_of_mixture}$) przez liczbę cząsteczek w jednostce objętości, można zdefiniować równoważny przekrój czynny (equivalent cross-section) danej cząsteczki.

Jeśli w jednostce objętości znajduje się $N$ cząsteczek $X_mY_n$, to $N_X=mN$, $N_Y=nN$, a z równania ($\ref{eqn:cross_section_of_mixture}$) przekrój czynny tej cząsteczki można wyznaczyć jako:

$$ \sigma = \frac{\Sigma}{N}=m\sigma_X + n\sigma_Y \label{eqn:equivalent_cross_section}\tag{5} $$

> Równania ($\ref{eqn:cross_section_of_mixture}$) i ($\ref{eqn:equivalent_cross_section}$) są prawdziwe przy założeniu, że jądra $X$ i $Y$ reagują z neutronami niezależnie od siebie, i są poprawne dla wszystkich typów reakcji neutronowych z wyjątkiem [rozpraszania sprężystego](/posts/Neutron-Interactions-and-Cross-sections/#rozpraszanie-spr%C4%99%C5%BCyste-elastic-scattering).
> Ponieważ w rozpraszaniu sprężystym neutronów na cząsteczkach i ciałach stałych (zwłaszcza w zakresie niskich energii) nie można zastosować powyższego założenia, przekrój rozpraszania trzeba wyznaczyć doświadczalnie.
{: .prompt-warning }
