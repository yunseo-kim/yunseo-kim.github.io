---
title: Principe de relativité et transformation de Lorentz
description: Nous explorons le concept de référentiel et la transformation de Galilée largement utilisée en mécanique classique. Nous examinons également brièvement les équations de Maxwell et l'expérience de Michelson-Morley qui ont conduit à l'émergence de la transformation de Lorentz, puis nous dérivons la matrice de transformation de Lorentz.
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Principe de relativité** : Principe selon lequel toutes les lois physiques doivent être identiques dans différents référentiels se déplaçant à vitesse constante les uns par rapport aux autres
{: .prompt-info }

> **Facteur de Lorentz $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **Transformation de Lorentz**
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

> **Transformation de Lorentz inverse**
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

## Référentiels et principe de relativité
### Référentiel (frame of reference)
- **Référentiel (frame of reference)** : Dire qu'un objet se déplace signifie que sa position change relativement à un autre objet. Comme tout mouvement est relatif, il est nécessaire d'établir un référentiel pour décrire un mouvement.
- **Référentiel inertiel (inertial frames of reference)** : Référentiel dans lequel la première loi de Newton ("L'état de mouvement d'un corps reste inchangé tant que la somme des forces qui s'exercent sur lui est nulle") est valide. Tout référentiel se déplaçant à vitesse constante par rapport à un référentiel inertiel est également un référentiel inertiel.

### Principe de relativité (Principle of Relativity)
C'est l'un des concepts fondamentaux de la physique, qui stipule que toutes les lois physiques doivent être identiques dans différents référentiels se déplaçant à vitesse constante les uns par rapport aux autres. Si les lois physiques étaient différentes pour des observateurs en mouvement relatif, cette différence pourrait être utilisée pour établir un référentiel absolu et déterminer qui est immobile et qui se déplace. Cependant, selon le principe de relativité, une telle distinction n'existe pas, donc il n'y a pas de référentiel absolu ni de mouvement absolu dans l'univers, et tous les référentiels inertiels sont équivalents.

## Limites de la transformation de Galilée
### Transformation de Galilée (Galilean transformation)
Supposons qu'il existe deux référentiels inertiels $S$ et $S^{\prime}$, où $S^{\prime}$ se déplace par rapport à $S$ à une vitesse constante $\vec{v}$ dans la direction $+x$. Un même événement est observé dans $S$ aux coordonnées $(x, y, z)$ au temps $t$, et dans $S^{\prime}$ aux coordonnées $(x^{\prime}, y^{\prime}, z^{\prime})$ au temps $t^{\prime}$.

Dans ce cas, la valeur du mouvement dans la direction $x$ mesurée dans $S^{\prime}$ sera supérieure à celle mesurée dans $S$ d'une distance $\vec{v}t$ correspondant au déplacement de $S^{\prime}$ par rapport à $S$ dans la direction $x$, donc :

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

Et comme il n'y a pas de mouvement relatif dans les directions $y$ et $z$ :

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

Intuitivement, on peut supposer que :

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

Cette transformation de coordonnées entre différents référentiels inertiels, représentée par les équations ($\ref{eqn:galilean_transform_x}$) à ($\ref{eqn:galilean_transform_t}$), est appelée **transformation de Galilée (Galilean transformation)**. Elle est simple et intuitive, et fonctionne dans la plupart des situations quotidiennes. Cependant, comme nous le verrons plus loin, elle est en contradiction avec les équations de Maxwell.

### Équations de Maxwell
À la fin des années 11800, Maxwell a étendu les idées et les résultats de recherche antérieurs proposés par d'autres scientifiques comme Faraday et Ampère, révélant que l'électricité et le magnétisme sont en réalité une seule force, et a dérivé les quatre équations suivantes qui décrivent le champ électromagnétique :

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: Le flux électrique traversant une surface fermée quelconque est égal à la charge nette à l'intérieur (loi de Gauss).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: Il n'existe pas de monopôle magnétique.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: La variation du champ magnétique crée un champ électrique (loi de Faraday).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: La variation du champ électrique et le courant créent un champ magnétique (loi d'Ampère-Maxwell).}
\end{gather*}$$

Les équations de Maxwell expliquaient avec succès tous les phénomènes électriques et magnétiques connus jusqu'alors, prédisaient l'existence des ondes électromagnétiques et démontraient que la vitesse de ces ondes dans le vide, $c$, est une constante invariante, devenant ainsi les formules fondamentales de l'électromagnétisme.

### Contradiction entre la transformation de Galilée et les équations de Maxwell
La mécanique newtonienne utilisant la transformation de Galilée a été le fondement de la physique pendant plus de 200 ans, et les équations de Maxwell sont, comme mentionné précédemment, les équations fondamentales décrivant les phénomènes électriques et magnétiques. Cependant, il existe une contradiction entre les deux :

- Selon le principe de relativité, on s'attendrait à ce que les équations de Maxwell aient la même forme dans tous les référentiels inertiels, mais lorsqu'on applique la transformation de Galilée pour convertir les mesures d'un référentiel inertiel à un autre, les équations de Maxwell prennent une forme très différente.
- Les équations de Maxwell permettent de calculer la vitesse de la lumière $c$, qui est une constante invariante, mais selon la mécanique newtonienne et la transformation de Galilée, la vitesse de la lumière $c$ devrait être mesurée différemment selon le référentiel inertiel.

Par conséquent, les équations de Maxwell et la transformation de Galilée sont incompatibles, et au moins l'une des deux devait être modifiée. Cela a conduit à l'émergence de la **transformation de Lorentz (Lorentz transformation)** que nous aborderons plus loin.

## Théorie de l'éther (aether) et expérience de Michelson-Morley
Par ailleurs, la physique du 19ème siècle considérait que la lumière, comme les autres ondes telles que les vagues à la surface de l'eau ou les ondes sonores, était transmise par un milieu hypothétique appelé *éther (aether)*, et des efforts ont été déployés pour découvrir l'existence de cet éther.

Selon la théorie de l'éther, l'espace, même vide, était rempli d'éther, et on pensait que la révolution de la Terre autour du Soleil à une vitesse d'environ 30 km/s créerait un vent d'éther traversant la Terre.  
![Vent d'éther](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Source de l'image*
> - Auteur : utilisateur Wikimedia [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - Licence : [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Pour vérifier cette hypothèse, en 11887 de l'ère humaine, Michelson, en collaboration avec Morley, a réalisé l'*expérience de Michelson-Morley (Michelson-Morley Experiment)* en utilisant l'interféromètre ci-dessous.  
![Interféromètre de Michelson-Morley](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Source de l'image*
> - Auteur : Albert Abraham Michelson avec Edward Morley
> - Licence : domaine public

Dans cette expérience, un rayon lumineux est divisé en deux par un miroir semi-réfléchissant, puis chaque rayon parcourt environ 11 mètres en faisant un aller-retour le long des deux bras perpendiculaires de l'interféromètre avant de se rencontrer au point central, créant des franges d'interférence constructive ou destructive selon leur différence de phase. Selon la théorie de l'éther, la vitesse de la lumière varierait en fonction de la vitesse relative par rapport à l'éther, ce qui entraînerait un changement de cette différence de phase et donc un déplacement des franges d'interférence. Cependant, aucun déplacement des franges n'a été observé. Pour expliquer ce résultat, plusieurs tentatives ont été faites, dont celle de FitzGerald et Lorentz qui ont proposé la *contraction de Lorentz-FitzGerald (Lorentz–FitzGerald contraction)* ou *contraction des longueurs (length contraction)*, selon laquelle un objet se contracte lorsqu'il <u>se déplace relativement à l'éther</u>, ce qui a conduit à la transformation de Lorentz.

> À cette époque, Lorentz croyait en l'existence de l'éther et pensait que la contraction des longueurs était due au mouvement relatif par rapport à l'éther. Plus tard, Einstein a interprété la véritable signification physique de la transformation de Lorentz avec sa *théorie de la relativité restreinte (Theory of Special Relativity)*, expliquant la contraction des longueurs en termes d'espace-temps plutôt que d'éther, et il a également été démontré par la suite que l'éther n'existe pas.
{: .prompt-info }

## Transformation de Lorentz (Lorentz transformation)
### Dérivation de la transformation de Lorentz
Dans la même situation que celle décrite pour la transformation de Galilée (équations [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]), supposons que la relation de transformation correcte entre $x$ et $x^{\prime}$, qui ne contredit pas les équations de Maxwell, soit la suivante :

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Ici, $\gamma$ est indépendant de $x$ et $t$, mais peut être une fonction de $\vec{v}$. Cette hypothèse peut être justifiée pour les raisons suivantes :

- Pour qu'il y ait une correspondance biunivoque entre les événements dans $S$ et $S^{\prime}$, $x$ et $x^{\prime}$ doivent avoir une relation linéaire.
- Comme on sait que la transformation de Galilée est correcte pour la mécanique dans les situations ordinaires, l'équation ($\ref{eqn:lorentz_transform_x}$) doit pouvoir s'approximer à celle-ci.
- La forme doit être aussi simple que possible.

Puisque les formules physiques doivent avoir la même forme dans les référentiels $S$ et $S^{\prime}$, pour exprimer $x$ en fonction de $x^{\prime}$ et $t$, il suffit de changer le signe de $\vec{v}$ (la direction du mouvement relatif), et comme il ne doit y avoir aucune différence entre les deux référentiels à part le signe de $\vec{v}$, $\gamma$ doit être le même.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Comme pour la transformation de Galilée, il n'y a aucune raison pour que les composantes perpendiculaires à la direction de $\vec{v}$, c'est-à-dire $y$ et $y^{\prime}$, ainsi que $z$ et $z^{\prime}$, soient différentes, donc :

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

En substituant l'équation ($\ref{eqn:lorentz_transform_x}$) dans ($\ref{eqn:lorentz_transform_x_inverse}$), on obtient :

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

En réarrangeant pour $t^{\prime}$, on obtient :

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

De plus, pour ne pas contredire les équations de Maxwell, la vitesse de la lumière doit être la même, $c$, dans les deux référentiels, ce qui nous permet de déterminer $\gamma$. Si à $t=0$, les origines des deux référentiels sont au même endroit, alors par cette condition initiale, $t^\prime = 0$. Supposons maintenant qu'à $t=t^\prime=0$, il y ait un flash lumineux à l'origine commune de $S$ et $S^\prime$, et que les observateurs dans chaque référentiel mesurent la vitesse de cette lumière. Dans ce cas, dans le référentiel $S$ :

$$ x = ct \label{eqn:ct_S}\tag{9}$$

et dans le référentiel $S^\prime$ :

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

En utilisant les équations ($\ref{eqn:lorentz_transform_x}$) et ($\ref{eqn:lorentz_transform_t}$) pour substituer $x$ et $t$ dans l'équation ci-dessus, on obtient :

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

En résolvant pour $x$, on obtient :

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Mais d'après l'équation ($\ref{eqn:ct_S}$), $x=ct$, donc :

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

Par conséquent :

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

En substituant cette expression de $\gamma$ en fonction de $\vec{v}$ dans les équations ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$) et ($\ref{eqn:lorentz_transform_t}$), on obtient les équations de transformation finales du référentiel $S$ au référentiel $S^\prime$.

### Matrice de transformation de Lorentz

Les équations de transformation finales obtenues précédemment sont les suivantes :

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

Ces équations constituent la **transformation de Lorentz (Lorentz transformation)**. En posant $\vec{\beta}=\vec{v}/c$, on peut les exprimer sous forme matricielle comme suit :

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

Lorentz a montré qu'en utilisant cette transformation, les formules fondamentales de l'électromagnétisme ont la même forme dans tous les référentiels inertiels. On peut également vérifier que lorsque la vitesse $v$ est très petite par rapport à la vitesse de la lumière $c$, $\gamma \to 1$, et la transformation de Lorentz peut être approximée par la transformation de Galilée.

### Transformation de Lorentz inverse (inverse Lorentz transformation)
Parfois, il est plus pratique de transformer les mesures du référentiel en mouvement $S^\prime$ en mesures du référentiel au repos $S$, plutôt que l'inverse.
Dans ce cas, on peut utiliser la **transformation de Lorentz inverse (inverse Lorentz transformation)**.  
En calculant l'inverse de la matrice ($\ref{lorentz_transform_matrix}$), on obtient la matrice de transformation de Lorentz inverse suivante :

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

Cela revient à échanger les grandeurs physiques avec et sans prime dans les équations ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) et à remplacer $v$ par $-v$ (c'est-à-dire $\beta$ par $-\beta$).

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
