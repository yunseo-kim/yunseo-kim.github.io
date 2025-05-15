---
title: Masse et énergie, particules et ondes
description: Explorons le principe d'équivalence masse-énergie de la théorie de la relativité et calculons l'énergie d'un électron en mouvement en tenant compte des effets relativistes.
categories: [Nuclear Engineering, Basis]
tags: [Nuclear Physics, Theory of Relativity]
math: true
image: /assets/img/atoms.webp
---
## Principe d'équivalence masse-énergie
La masse et l'énergie sont identiques et peuvent être converties l'une en l'autre.

$$ E=mc^2 $$

où $c$ est la vitesse de la lumière, $2.9979 \times 10^{10}\ \text{cm/sec}$.

## Électron-volt (Electron Volt, eV)
*Électron-volt (electron volt, eV)* : l'énergie cinétique acquise par un électron lorsqu'il traverse une différence de potentiel de 1V

$$
\begin{align*} 
1 \text{eV} &= 1.60219 \times 10^{-19}\ \text{C}\cdot \text{V}
\\ &= 1.60219 \times 10^{-19}\ \text{J}
\end{align*}
$$

## Masse et énergie d'un objet en mouvement
Selon la théorie de la relativité, la masse d'un objet en mouvement augmente relativement du point de vue de l'observateur, et l'équation reliant la vitesse et la masse d'un objet en mouvement est définie comme suit :

$$ m=\frac {m_0}{\sqrt{1-v^2/c^2}} \tag{1} $$

$m_0$ : masse au repos, $v$ : vitesse

L'*énergie totale* d'une particule est la somme de l'*énergie de masse au repos* et de l'*énergie cinétique*, donc :

$$ E_{\text{total}} = E_{\text{repos}}+E_{\text{cinétique}} = mc^2$$

$$
\begin{align*}
E_{\text{cinétique}} &= E_{\text{total}}-E_{\text{repos}}
\\ &= mc^2 - m_0c^2
\\ &= m_0c^2\left[\frac {1}{\sqrt{1-v^2/c^2}} - 1\right] \tag{2}
\end{align*}
$$

En particulier, lorsque $v\ll c$, en posant $\cfrac{v^2}{c^2} = \epsilon$ et en approximant par un développement de Taylor autour de $\epsilon = 0$ (c'est-à-dire un développement de Maclaurin) :

$$
\begin{align*}
E_{\text{cinétique}} &= m_0c^2\left[\frac {1}{\sqrt{1-\epsilon}} - 1\right] \\
&= m_0c^2\left[ (1-\epsilon)^{-\frac{1}{2}} - 1 \right] \\
&= m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon + O(\epsilon^2) \right) - 1 \right] \\
&\approx m_0c^2\left[ \left( 1 + \frac{1}{2}\epsilon \right) - 1 \right] \\
&= \frac{1}{2}m_0c^2\epsilon \\
&= \frac {1}{2}m_0v^2 \tag{3}
\end{align*}
$$

ce qui correspond à la formule de l'énergie cinétique en mécanique classique. En pratique, lorsque $v\leq 0.2c$ ou $E_{\text{cinétique}} \leq 0.02E_{\text{repos}}$, on peut considérer que $v\ll c$ et utiliser cette approximation (c'est-à-dire négliger les effets relativistes) tout en obtenant des valeurs suffisamment précises.

### Électron
L'énergie de masse au repos de l'électron étant $E_{\text{repos}}=m_ec^2=0.511 \text{MeV}$, il faut appliquer la formule relativiste de l'énergie cinétique lorsque l'énergie cinétique de l'électron dépasse $0.02\times 0.511 \text{MeV}=0.010 \text{MeV}=10 \text{keV}$. En génie nucléaire, l'énergie des électrons dépasse souvent 10 keV, donc l'équation (2) doit généralement être appliquée.

### Neutron
L'énergie de masse au repos du neutron est d'environ 1000 MeV, donc $0.02E_{repos}=20\text{MeV}$. En génie nucléaire, il est rare de traiter des situations où l'énergie cinétique des neutrons dépasse 20 MeV, donc on utilise généralement l'équation (3) pour calculer l'énergie cinétique des neutrons.

### Photon
Les équations (2) et (3) ne sont valables que lorsque la masse au repos n'est pas nulle, donc elles ne s'appliquent pas aux photons dont la masse au repos est nulle. L'énergie totale d'un photon est calculée par l'équation suivante :

$$ E = h\nu \tag{4} $$

$h$ : constante de Planck ($4.316 \times 10^{-15} \text{eV}\cdot\text{s}$), $\nu$ : fréquence de l'onde électromagnétique

## Onde de matière
Tout élément dans la nature est à la fois particule et onde. Ainsi, toutes les particules possèdent une longueur d'onde correspondante (*longueur d'onde de de Broglie*). Cette longueur d'onde $\lambda$ est fonction de la quantité de mouvement $p$ et de la constante de Planck $h$.

$$ \lambda = \frac {h}{p} \tag{5}$$

De plus, la quantité de mouvement $p$ est définie par l'équation suivante :

$$ p = mv \tag{6} $$

### En négligeant les effets relativistes (ex. : neutron)
Comme l'énergie cinétique est $E=1/2 mv^2$, l'expression de la quantité de mouvement en fonction de l'énergie est :

$$ p=\sqrt{2mE} \tag{7} $$

En substituant dans l'équation (5), la longueur d'onde de la particule devient :

$$ \lambda = \frac {h}{\sqrt{2mE}} \tag{8} $$

Cette équation est utilisée en génie nucléaire pour calculer la longueur d'onde de de Broglie des neutrons. En substituant la masse au repos du neutron, on obtient :

$$ \lambda = \frac {2.860 \times 10^{-9}}{\sqrt{E}} \tag{9}$$

où $\lambda$ est exprimé en cm et $E$ est l'énergie cinétique du neutron en eV.

### En tenant compte des effets relativistes (ex. : électron)
On calcule directement la quantité de mouvement $p$ en utilisant les équations relativistes précédentes :

$$ p=\frac {1}{c} \sqrt{E^2_{\text{total}}-E^2_{\text{repos}}} \tag{10}$$

La longueur d'onde de de Broglie est alors :

$$ \lambda = \frac {hc}{\sqrt{E_{\text{total}}-E_{\text{repos}}}} \tag{11} $$

### Particules de masse au repos nulle (ex. : photon)
Pour les particules de masse au repos nulle, la quantité de mouvement ne peut pas être calculée par l'équation (6), mais s'exprime par :

$$ p=\frac {E}{c} \tag{12} $$

En substituant l'équation (12) dans l'équation (5) :

$$ \lambda = \frac {hc}{E} \tag{13}$$

En substituant les valeurs de $h$ et $c$, l'équation finale pour la longueur d'onde est :

$$ \lambda = \frac {1.240 \times 10^{-6}}{E} \tag{14}$$

où $\lambda$ est exprimé en m et $E$ en eV.
