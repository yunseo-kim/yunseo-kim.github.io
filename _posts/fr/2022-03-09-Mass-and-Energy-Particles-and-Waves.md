---
title: Masse et énergie, particules et ondes
description: Explorons le principe d'équivalence masse-énergie de la théorie de la
  relativité et calculons l'énergie d'un électron en mouvement en tenant compte des
  effets relativistes.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## Principe d'équivalence masse-énergie
La masse et l'énergie sont identiques et peuvent être mutuellement converties.

$$ E=mc^2 $$

Où $c$ est la vitesse de la lumière $2,9979 \times 10^{10}\ \text{cm/sec}$.

## Électron-volt (eV)
*Électron-volt (eV)* : L'énergie cinétique acquise par un électron lorsqu'il traverse une différence de potentiel de 1V

$$
\begin{align*} 
1 \text{eV} &= 1,60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1,60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Masse et énergie d'un objet en mouvement
Selon la théorie de la relativité, du point de vue de l'observateur, la masse d'un objet en mouvement augmente relativement, et l'équation reliant la vitesse et la masse d'un objet en mouvement est définie comme suit :

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$ : masse au repos, $v$ : vitesse

L'*énergie totale* d'une particule est la somme de son *énergie de masse au repos* et de son *énergie cinétique*, donc ce qui suit est vrai :

$$ E_{\text{totale}} = E_{\text{repos}}+E_{\text{cinétique}} = mc^2$$

$$
\begin{align*}
E_{\text{cinétique}} &= E_{\text{totale}}-E_{\text{repos}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

En particulier, lorsque $v\ll c$, en utilisant le développement binomial pour l'approximation :

$$
\begin{align*}
E_{cinétique} &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right]
\\ &= m_0c^2\left[\left(1+\frac{1}{2}v^2/c^2\right)-1\right]
\\ &= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

Ce qui devient identique à la formule de l'énergie cinétique en mécanique classique. En pratique, lorsque $v\leq 0,2c$ ou $E_{\text{cinétique}} \leq 0,02E_{\text{repos}}$, on peut considérer que $v\ll c$ et utiliser cette approximation (c'est-à-dire ignorer les effets relativistes) pour obtenir une valeur suffisamment précise.

### Électron
Comme l'énergie de masse au repos de l'électron est $E_{\text{repos}}=m_ec^2=0,511 \text{MeV}$, la formule relativiste de l'énergie cinétique doit être appliquée lorsque l'énergie cinétique de l'électron dépasse $0,02\times 0,511 \text{MeV}=0,010 \text{MeV}=10 \text{keV}$. Dans le génie nucléaire, l'énergie des électrons est souvent supérieure à 10 keV, donc l'équation (2) doit être appliquée dans la plupart des cas.

### Neutron
L'énergie de masse au repos du neutron est d'environ 1000 MeV, donc $0,02E_{repos}=20\text{MeV}$. Dans le génie nucléaire, il est rare de traiter des situations où l'énergie cinétique des neutrons dépasse 20 MeV, donc on utilise généralement l'équation (3) pour calculer l'énergie cinétique des neutrons.

### Photon
Les équations (2) et (3) ne sont valables que lorsque la masse au repos n'est pas nulle, donc elles ne peuvent pas être appliquées aux photons dont la masse au repos est nulle. L'énergie totale d'un photon est calculée par l'équation suivante :

$$ E = h\nu \tag{4} $$

$h$ : constante de Planck ($4,316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$ : fréquence de l'onde électromagnétique

## Onde de matière
Toute matière dans la nature est à la fois une particule et une onde. C'est-à-dire que toutes les particules ont une longueur d'onde correspondante (*longueur d'onde de de Broglie*). La longueur d'onde $\lambda$ est une fonction de la quantité de mouvement $p$ et de la constante de Planck $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

De plus, la quantité de mouvement $p$ est définie par l'équation suivante :

$$ p = mv \tag{6} $$

### En négligeant les effets relativistes (par exemple, pour les neutrons)
Comme l'énergie cinétique est $E=1/2 mv^2$, l'équation (6) exprimée en fonction de l'énergie devient :

$$ p=\sqrt{2mE} \tag{7} $$

En substituant cela dans l'équation (5), la longueur d'onde de la particule devient :

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

Cette équation est utilisée en génie nucléaire pour calculer la longueur d'onde de de Broglie des neutrons. En substituant la masse au repos du neutron, on obtient :

$$ \lambda = \frac {2,860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

Où $\lambda$ est en cm et $E$ est l'énergie cinétique du neutron exprimée en eV.

### En tenant compte des effets relativistes (par exemple, pour les électrons)
On calcule directement la quantité de mouvement $p$ en utilisant les équations relativistes précédentes.

$$ p=\frac {1}{c} \sqrt{E^2_{totale}-E^2_{repos}} \tag{10}$$

Alors la longueur d'onde de de Broglie devient :

$$ \lambda = \frac {hc}{\sqrt{E_{totale}-E_{repos}}} \tag{11} $$

### Pour les particules de masse au repos nulle (par exemple, les photons)
Pour les particules de masse au repos nulle, la quantité de mouvement ne peut pas être calculée par l'équation (6), donc on l'exprime comme :

$$ p=\frac {E}{c} \tag{12} $$

En substituant l'équation (12) dans l'équation (5), on obtient :

$$ \lambda = \frac {hc}{E} \tag{13}$$

En substituant les valeurs de $h$ et $c$, l'équation finale pour la longueur d'onde devient :

$$ \lambda = \frac {1,240 \times 10^{-6}}{E} \tag{14}$$

Où $\lambda$ est en m et $E$ est en eV.
