---
title: Champ gravitationnel et potentiel gravitationnel
description: Découvrez les définitions du vecteur champ gravitationnel et du potentiel gravitationnel selon la loi de la gravitation universelle de Newton, et explorez deux exemples importants liés à ces concepts : le théorème de la coquille sphérique et les courbes de rotation galactique.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - Loi de la gravitation universelle de Newton : $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - Pour les objets avec une distribution de masse continue et une taille : $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$ : densité de masse au point situé au vecteur position $\mathbf{r^{\prime}}$ depuis une origine arbitraire
>   - $dv^{\prime}$ : élément de volume au point situé au vecteur position $\mathbf{r^{\prime}}$ depuis une origine arbitraire
> - **Vecteur champ gravitationnel (gravitational field vector)** :
>   - Vecteur représentant la force par unité de masse exercée sur une particule dans un champ créé par un objet de masse $M$
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - Possède la dimension d'une *force par unité de masse* ou d'une *accélération*
> - **Potentiel gravitationnel (gravitational potential)** :
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - Possède la dimension d'une *force par unité de masse* $\times$ *distance* ou d'une *énergie par unité de masse*
>   - $\Phi = -G\cfrac{M}{r}$
>   - Seules les différences relatives de potentiel gravitationnel ont une signification, pas les valeurs absolues
>   - On élimine généralement l'ambiguïté en fixant arbitrairement la condition $\Phi \to 0$ quand $r \to \infty$
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **Potentiel gravitationnel à l'intérieur et à l'extérieur d'une coquille sphérique (théorème de la coquille)**
>   - Pour $R>a$ :
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - Pour calculer le potentiel gravitationnel en un point extérieur à une distribution sphérique symétrique de matière, on peut considérer l'objet comme une masse ponctuelle
>   - Pour $R<b$ :
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - À l'intérieur d'une coquille de masse à symétrie sphérique, le potentiel gravitationnel est constant indépendamment de la position, et la gravité exercée est nulle
>   - Pour $b<R<a$ : $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## Champ gravitationnel
### Loi de la gravitation universelle de Newton
Newton avait déjà systématisé et vérifié numériquement la loi de la gravitation universelle avant 11666 HE. Pourtant, il lui fallut encore 20 ans pour publier ses résultats dans son ouvrage *Principia* en 11687 HE, car il ne pouvait pas justifier sa méthode de calcul qui considérait la Terre et la Lune comme des masses ponctuelles sans dimension. Heureusement, [grâce au calcul différentiel et intégral que Newton lui-même a inventé plus tard, nous pouvons démontrer ce problème beaucoup plus facilement que Newton ne le pouvait à l'époque](#pour-ra).

Selon la loi de la gravitation universelle de Newton, *chaque particule de matière attire toutes les autres particules de l'univers avec une force proportionnelle au produit de leurs masses et inversement proportionnelle au carré de la distance qui les sépare*. Mathématiquement, cela s'exprime comme suit :

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *Source de l'image*
> - Auteur : utilisateur Wikimedia [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - Licence : [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

Le vecteur unitaire $\mathbf{e}_r$ est dirigé de $M$ vers $m$, et le signe négatif indique que la force est attractive. Ainsi, $m$ est attiré vers $M$.

### L'expérience de Cavendish
La vérification expérimentale de cette loi et la détermination de la valeur de $G$ ont été réalisées en 11798 HE par le physicien britannique Henry Cavendish. L'expérience de Cavendish utilise une balance de torsion composée de deux petites sphères fixées aux extrémités d'une tige légère. Ces deux sphères sont attirées par deux autres sphères plus grandes placées à proximité. La valeur officielle actuelle de $G$ est de $6,673 \pm 0,010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$.

> Bien que $G$ soit l'une des constantes fondamentales connues depuis le plus longtemps, elle est connue avec une précision inférieure à celle de la plupart des autres constantes fondamentales comme $e$, $c$ ou $\hbar$. De nombreuses recherches sont encore menées aujourd'hui pour déterminer la valeur de $G$ avec une plus grande précision.
{: .prompt-tip }

### Pour les objets ayant une taille
La loi exprimée par l'équation ($\ref{eqn:law_of_gravitation}$) ne s'applique strictement qu'aux *particules ponctuelles*. Si l'un ou les deux objets ont une certaine taille, il faut ajouter l'hypothèse que le champ gravitationnel est un *champ linéaire* pour calculer la force. C'est-à-dire qu'on suppose que la gravité totale exercée sur une particule de masse $m$ par plusieurs autres particules peut être obtenue en additionnant vectoriellement chaque force. Pour un objet avec une distribution continue de matière, la somme devient une intégrale :

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$ : densité de masse au point situé au vecteur position $\mathbf{r^{\prime}}$ depuis une origine arbitraire
- $dv^{\prime}$ : élément de volume au point situé au vecteur position $\mathbf{r^{\prime}}$ depuis une origine arbitraire

Si les deux objets de masses $M$ et $m$ ont tous deux une taille, une seconde intégrale volumique sur $m$ est nécessaire pour calculer la force gravitationnelle totale.

### Vecteur champ gravitationnel
Le **vecteur champ gravitationnel (gravitational field vector)** $\mathbf{g}$ est défini comme la force par unité de masse exercée sur une particule dans un champ créé par un objet de masse $M$ :

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

ou

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

où la direction de $\mathbf{e}_r$ varie selon $\mathbf{r^\prime}$.

Cette grandeur $\mathbf{g}$ a la dimension d'une *force par unité de masse* ou d'une *accélération*. Près de la surface terrestre, la magnitude du vecteur champ gravitationnel $\mathbf{g}$ correspond à ce que nous appelons la **constante d'accélération gravitationnelle**, avec $\|\mathbf{g}\| \approx 9,80\mathrm{m/s^2}$.

## Potentiel gravitationnel
### Définition
Le vecteur champ gravitationnel $\mathbf{g}$ varie en $1/r^2$, et satisfait donc la condition ($\nabla \times \mathbf{g} \equiv 0$) permettant de l'exprimer comme le gradient d'une fonction scalaire (potentiel). On peut donc écrire :

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

où $\Phi$ est le **potentiel gravitationnel**, qui a la dimension d'une (*force par unité de masse*) $\times$ (*distance*) ou d'une *énergie par unité de masse*.

Puisque $\mathbf{g}$ ne dépend que du rayon, $\Phi$ varie également uniquement en fonction de $r$. À partir des équations ($\ref{eqn:g_vector}$) et ($\ref{eqn:gradient_phi}$), on obtient :

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

En intégrant, on trouve :

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

La constante d'intégration peut être omise car seules les différences relatives de potentiel gravitationnel ont une signification, pas les valeurs absolues. On élimine généralement l'ambiguïté en fixant arbitrairement la condition $\Phi \to 0$ quand $r \to \infty$, condition que l'équation ($\ref{eqn:g_potential}$) satisfait.

Pour une distribution continue de matière, le potentiel gravitationnel s'écrit :

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

Pour une masse distribuée sur une fine coquille de surface :

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

Et pour une source de masse linéaire de densité $\rho_l$ :

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### Signification physique
Considérons le travail par unité de masse $dW^\prime$ effectué lorsqu'un objet se déplace d'une distance $d\mathbf{r}$ dans un champ gravitationnel.

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

Dans cette équation, $\Phi$ est une fonction des coordonnées de position uniquement, exprimée comme $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$. Par conséquent, le travail par unité de masse effectué pour déplacer un objet d'un point à un autre dans un champ gravitationnel est égal à la différence de potentiel entre ces deux points.

Si l'on définit le potentiel gravitationnel comme étant nul à l'infini, alors $\Phi$ en un point quelconque peut être interprété comme le travail par unité de masse nécessaire pour déplacer l'objet depuis l'infini jusqu'à ce point. L'énergie potentielle d'un objet est égale au produit de sa masse par le potentiel gravitationnel $\Phi$, donc si $U$ est l'énergie potentielle :

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

Par conséquent, la force gravitationnelle exercée sur un objet est égale au gradient négatif de son énergie potentielle.

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

Lorsqu'un objet est placé dans un champ gravitationnel créé par une masse, il possède toujours une certaine énergie potentielle. Cette énergie potentielle réside strictement dans le champ lui-même, mais par convention, on l'attribue souvent à l'objet.

## Exemple : Potentiel gravitationnel à l'intérieur et à l'extérieur d'une coquille sphérique (théorème de la coquille)
### Configuration des coordonnées et expression du potentiel gravitationnel sous forme d'intégrale
Calculons le potentiel gravitationnel à l'intérieur et à l'extérieur d'une coquille sphérique uniforme de rayon intérieur $b$ et de rayon extérieur $a$. La gravité due à la coquille sphérique peut être obtenue en calculant directement les composantes de la force agissant sur une unité de masse dans le champ, mais l'approche par le potentiel est plus simple.

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

Calculons le potentiel au point $P$ situé à une distance $R$ du centre. En supposant une distribution de masse uniforme dans la coquille, $\rho(r^\prime)=\rho$, et comme il y a symétrie par rapport à l'angle azimutal $\phi$ autour de la ligne reliant le centre de la sphère et le point $P$ :

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

D'après la loi des cosinus :

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

et comme $R$ est constant, en différenciant cette équation par rapport à $r^\prime$ :

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

En substituant dans l'équation ($\ref{eqn:spherical_shell_1}$) :

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

où $r_\mathrm{max}$ et $r_\mathrm{min}$ sont déterminés par la position du point $P$.

### Pour $R>a$
$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

La masse $M$ de la coquille sphérique est donnée par :

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

donc le potentiel est :

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> En comparant le résultat que nous venons d'obtenir ($\ref{eqn:spherical_shell_outside_2}$) avec l'équation du potentiel gravitationnel dû à une masse ponctuelle $M$ ($\ref{eqn:g_potential}$), on constate qu'ils sont identiques. Cela signifie que pour calculer le potentiel gravitationnel en un point extérieur à une distribution sphérique symétrique de matière, on peut considérer que toute la masse est concentrée au centre. La plupart des corps célestes sphériques comme la Terre ou la Lune entrent dans cette catégorie, car ils peuvent être considérés comme composés d'innombrables coquilles sphériques concentriques de diamètres différents, comme des [poupées russes](https://en.wikipedia.org/wiki/Matryoshka_doll). Cela justifie [l'hypothèse mentionnée au début de cet article](#loi-de-la-gravitation-universelle-de-newton) selon laquelle des corps célestes comme la Terre ou la Lune peuvent être traités comme des masses ponctuelles sans dimension pour les calculs.
{: .prompt-info }

### Pour $R<b$
$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> À l'intérieur d'une coquille de masse à symétrie sphérique, le potentiel gravitationnel est constant indépendamment de la position, et la gravité exercée est nulle.
{: .prompt-info }

> C'est aussi l'une des principales raisons pour lesquelles la "théorie de la Terre creuse", une pseudoscience notoire, est absurde. Si la Terre était une coquille sphérique avec un intérieur vide comme le prétend cette théorie, la gravité terrestre n'agirait pas sur tous les objets à l'intérieur de cette cavité. Compte tenu de la masse et du volume de la Terre, non seulement une telle cavité ne pourrait pas exister, mais même si elle existait, les êtres vivants qui s'y trouveraient ne marcheraient pas sur la surface intérieure de la coquille, mais flotteraient en apesanteur comme dans une station spatiale.  
> [Des microorganismes peuvent vivre à plusieurs kilomètres sous la surface terrestre](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3), mais certainement pas de la manière décrite par la théorie de la Terre creuse. J'apprécie beaucoup le roman de Jules Verne *Voyage au centre de la Terre* et le film *Journey to the Center of the Earth*, mais il faut apprécier ces œuvres de fiction pour ce qu'elles sont, sans les prendre au sérieux.
{: .prompt-tip }

### Pour $b<R<a$
$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### Résultats
Les graphiques suivants montrent le potentiel gravitationnel $\Phi$ et la magnitude du vecteur champ gravitationnel $\|\mathbf{g}\|$ en fonction de la distance $R$ pour les trois régions que nous avons calculées.

![Gravitational Potential as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-gravitational-potential.png)
![Magnitude of the Field Vector as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-field-vector.png)
> - Code Python de visualisation : [Dépôt yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/shell_theorem.py)
> - Licence : [Voir ici](https://github.com/yunseo-kim/physics-visualization?tab=readme-ov-file#license)

On peut observer que le potentiel gravitationnel et la magnitude du vecteur champ sont continus. Si le potentiel gravitationnel était discontinu en un point, le gradient du potentiel, c'est-à-dire la magnitude de la gravité, serait infini en ce point, ce qui n'est pas physiquement plausible. Cependant, la *dérivée* du vecteur champ gravitationnel est discontinue aux surfaces intérieure et extérieure de la coquille.

## Exemple : Courbes de rotation galactique
Selon les observations astronomiques, la masse observable de nombreuses galaxies spirales en rotation, comme notre Voie lactée ou la galaxie d'Andromède, est principalement concentrée près du centre. Cependant, comme on peut le voir sur le graphique suivant, la vitesse orbitale des masses dans ces galaxies spirales diffère considérablement des prédictions théoriques basées sur la distribution de masse observable, et reste presque constante au-delà d'une certaine distance.

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *Source de l'image*
> - Auteur : utilisateur Wikipédia [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - Licence : Domaine public

![Rotation Curve of Spiral Galaxy M33](https://upload.wikimedia.org/wikipedia/commons/c/cd/Rotation_curve_of_spiral_galaxy_Messier_33_%28Triangulum%29.png)
> **Courbe de rotation de la galaxie spirale M33 (galaxie du Triangle)**
> - Auteur : utilisateur Wikimedia [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama)
> - Licence : [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

Montrons que la prédiction de la vitesse orbitale en fonction de la distance lorsque la masse galactique est concentrée au centre ne correspond pas à ces observations, et que pour expliquer les résultats observés, la masse $M(R)$ distribuée à l'intérieur d'une distance $R$ du centre galactique doit être proportionnelle à $R$.

D'abord, si la masse galactique $M$ est concentrée au centre, la vitesse orbitale à une distance $R$ est donnée par :

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

Dans ce cas, on prédit une vitesse orbitale qui diminue en $1/\sqrt{R}$ comme indiqué par la ligne pointillée sur les deux graphiques ci-dessus, mais selon les observations, la vitesse orbitale $v$ reste presque constante quelle que soit la distance $R$. Ces observations ne peuvent s'expliquer que si $M(R)\propto R$.

En posant $M(R) = kR$ avec une constante de proportionnalité $k$ :

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(constante)}. $$

À partir de ces résultats, les astrophysiciens concluent qu'il doit exister dans de nombreuses galaxies une "matière noire" (dark matter) non détectée, et que cette matière noire doit constituer plus de 90% de la masse de l'univers. Cependant, la nature exacte de la matière noire n'a pas encore été clairement identifiée, et il existe également des tentatives, bien que non majoritaires, comme la dynamique newtonienne modifiée (Modified Newtonian Dynamics, MOND), qui cherchent à expliquer les observations sans supposer l'existence de matière noire. Aujourd'hui, ces domaines de recherche sont à la pointe de l'astrophysique.
