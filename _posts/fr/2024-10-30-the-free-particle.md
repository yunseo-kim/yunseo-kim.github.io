---
title: La particule libre
description: Nous examinons le fait que la solution à variables séparées pour une
  particule libre avec V(x)=0 ne peut pas être normalisée et ce que cela signifie,
  nous démontrons qualitativement la relation d'incertitude position-impulsion pour
  la solution générale, et nous calculons et interprétons physiquement la vitesse
  de phase et la vitesse de groupe de Ψ(x,t).
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, The Uncertainty Principle]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Particule libre : $V(x)=0$, pas de conditions aux limites (énergie arbitraire)
> - La solution à variables séparées $\Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)}$ diverge à l'infini lorsqu'on l'intègre au carré, donc elle ne peut pas être normalisée, ce qui implique que :
>   - Une particule libre ne peut pas exister dans un état stationnaire
>   - On ne peut pas définir l'énergie d'une particule libre comme une valeur unique et précise (il existe une incertitude sur l'énergie)
> - Néanmoins, la solution générale de l'équation de Schrödinger dépendante du temps est une combinaison linéaire de solutions à variables séparées, donc ces dernières conservent une signification mathématique importante. Cependant, dans ce cas, en l'absence de conditions restrictives, la solution générale prend la forme d'une intégrale ($\int$) sur la variable continue $k$ plutôt que d'une somme ($\sum$) sur une variable discrète $n$.
> - Solution générale de l'équation de Schrödinger :
>
> $$ \begin{gather*}
> \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk, \\
> \text{où }\phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx
> \end{gather*}$$
>
> - Relation entre l'incertitude sur la position et l'incertitude sur l'impulsion :
>   - Si l'incertitude sur la position diminue, l'incertitude sur l'impulsion augmente, et inversement
>   - En d'autres termes, il est impossible en mécanique quantique de connaître simultanément et avec précision la position et l'impulsion d'une particule libre
> - Vitesse de phase et vitesse de groupe de la fonction d'onde $\Psi(x,t)$ :
>   - Vitesse de phase : $v_\text{phase} = \cfrac{\omega}{k} = \cfrac{\hbar k}{2m}$
>   - Vitesse de groupe : $v_\text{group} = \cfrac{d\omega}{dk} = \cfrac{\hbar k}{m}$
> - Signification physique de la vitesse de groupe et comparaison avec la mécanique classique :
>   - Physiquement, la vitesse de groupe représente la vitesse de déplacement de la particule
>   - En supposant que $\phi(k)$ ait une forme très pointue autour d'une certaine valeur $k_0$ (lorsque l'incertitude sur l'impulsion est suffisamment faible), 
> 
> $$v_\text{group} = v_\text{classical} = \sqrt{\cfrac{2E}{m}}$$
{: .prompt-info }

## Prérequis
- Formule d'Euler
- Transformée de Fourier & Théorème de Plancherel
- [L'équation de Schrödinger et la fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/)
- [L'équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/)
- [Le puits carré infini unidimensionnel](/posts/the-infinite-square-well/)

## Configuration du modèle
Examinons le cas le plus simple, celui de la particule libre ($V(x)=0$). Classiquement, il s'agit simplement d'un mouvement à vitesse constante, mais en mécanique quantique, ce problème est plus intéressant.  
L'[équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/) pour une particule libre est

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}=E\psi \tag{1}$$

c'est-à-dire

$$ \frac{d^2\psi}{dx^2} = -k^2\psi \text{, où }k\equiv \frac{\sqrt{2mE}}{\hbar} \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

[Jusqu'ici, c'est identique à l'intérieur d'un puits carré infini avec un potentiel nul](/posts/the-infinite-square-well/#établissement-du-modèle-et-des-conditions-aux-limites). Cependant, cette fois, écrivons la solution générale sous la forme exponentielle suivante :

$$ \psi(x) = Ae^{ikx} + Be^{-ikx}. \tag{3}$$

> $Ae^{ikx} + Be^{-ikx}$ et $C\cos{kx}+D\sin{kx}$ sont des méthodes équivalentes pour écrire la même fonction de $x$. Par la formule d'Euler $e^{ix}=\cos{x}+i\sin{x}$,
>
> $$\begin{align*}
> Ae^{ikx}+Be^{-ikx} &= A[\cos{kx}+i\sin{kx}] + B[\cos{(-kx)}+i\sin{(-kx)}] \\
&= A(\cos{kx}+i\sin{kx}) + B(\cos{kx}-i\sin{kx}) \\
&= (A+B)\cos{kx} + i(A-B)\sin{kx}.
> \end{align*}$$
>
> C'est-à-dire, en posant $C=A+B$, $D=i(A-B)$, 
>
> $$Ae^{ikx} + Be^{-ikx} = C\cos{kx}+D\sin{kx}. \blacksquare$$
>
> Inversement, en exprimant $A$ et $B$ en termes de $C$ et $D$, on obtient $A=\cfrac{C-iD}{2}$, $B=\cfrac{C+iD}{2}$.
>
> En mécanique quantique, lorsque $V=0$, la fonction exponentielle représente une onde en mouvement et est la plus pratique pour traiter les particules libres. En revanche, les fonctions sinus et cosinus sont plus adaptées pour représenter les ondes stationnaires et apparaissent naturellement dans le cas du puits carré infini.
{: .prompt-info }

Contrairement au puits carré infini, il n'y a pas de conditions aux limites qui restreignent $k$ et $E$ cette fois-ci. En d'autres termes, une particule libre peut avoir n'importe quelle énergie positive.

## Solution à variables séparées et vitesse de phase
En ajoutant la dépendance temporelle $e^{-iEt/\hbar}$ à $\psi(x)$, on obtient

$$ \Psi(x,t) = Ae^{ik\left(x-\frac{\hbar k}{2m}t \right)} + Be^{-ik\left(x+\frac{\hbar k}{2m}t \right)} \label{eqn:Psi_seperated_solution}\tag{4}$$

Toute fonction de $x$ et $t$ dépendant d'une forme particulière $(x\pm vt)$ représente une onde se déplaçant à la vitesse $v$ dans la direction $\mp x$ sans changer de forme. Par conséquent, le premier terme de l'équation ($\ref{eqn:Psi_seperated_solution}$) représente une onde se déplaçant vers la droite, et le second terme représente une onde de même longueur d'onde et vitesse de propagation, mais d'amplitude différente, se déplaçant vers la gauche. Comme ils ne diffèrent que par le signe devant $k$, on peut écrire

$$ \Psi_k(x,t) = Ae^{i\left(kx-\frac{\hbar k^2}{2m}t \right)} \tag{5}$$

où la direction de propagation de l'onde en fonction du signe de $k$ est la suivante :

$$ k \equiv \pm\frac{\sqrt{2mE}}{\hbar},\quad
\begin{cases}
k>0 \Rightarrow & \text{déplacement vers la droite}, \\
k<0 \Rightarrow & \text{déplacement vers la gauche}.
\end{cases} \tag{6}$$

L'"état stationnaire" d'une particule libre est clairement une onde progressive*, dont la longueur d'onde est $\lambda = 2\pi/\|k\|$ et qui, selon la formule de de Broglie, possède une quantité de mouvement

$$ p = \frac{2\pi\hbar}{\lambda} = \hbar k \label{eqn:de_broglie_formula}\tag{7}$$

> *Physiquement, il est évidemment contradictoire d'avoir un "état stationnaire" qui soit une onde progressive. La raison en sera bientôt expliquée.
{: .prompt-info }

De plus, la vitesse de cette onde est la suivante :

$$ v_{\text{phase}} = \left|\frac{\omega}{k}\right| = \frac{\hbar|k|}{2m} = \sqrt{\frac{E}{2m}}. \label{eqn:phase_velocity}\tag{8}$$

(Ici, $\omega$ est le coefficient devant $t$, soit $\cfrac{\hbar k^2}{2m}$.)

Cependant, cette fonction d'onde ne peut pas être normalisée car elle diverge à l'infini lorsqu'on l'intègre au carré.

$$ \int_{-\infty}^{\infty}\Psi_k^*\Psi_k dx = |A|^2\int_{-\infty}^{\infty}dx = \infty. \tag{9}$$

En d'autres termes, <u>dans le cas d'une particule libre, la solution à variables séparées n'est pas un état physiquement possible.</u> Une particule libre ne peut pas exister dans un [état stationnaire](/posts/time-independent-schrodinger-equation/#1-ce-sont-des-états-stationnaires) et ne peut pas non plus avoir [une valeur d'énergie spécifique](/posts/time-independent-schrodinger-equation/#2-ils-ont-une-valeur-dénergie-totale-définie-e-pas-une-distribution-de-probabilité-sur-une-plage). En fait, intuitivement, il serait plus étrange qu'une onde stationnaire se forme sans aucune condition aux limites aux deux extrémités.

## Calcul de la solution générale $\Psi(x,t)$ de l'équation de Schrödinger dépendante du temps
Néanmoins, cette solution à variables séparées conserve une signification importante car, indépendamment de l'interprétation physique, elle a une signification mathématique en tant que [combinaison linéaire de solutions à variables séparées qui forme la solution générale de l'équation de Schrödinger dépendante du temps](/posts/time-independent-schrodinger-equation/#3-la-solution-générale-de-léquation-de-schrödinger-dépendante-du-temps-est-une-combinaison-linéaire-des-solutions-à-variables-séparées). Cependant, dans ce cas, en l'absence de conditions restrictives, la solution générale prend la forme d'une intégrale ($\int$) sur la variable continue $k$ plutôt que d'une somme ($\sum$) sur une variable discrète $n$.

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\frac{\hbar k^2}{2m}t)}dk. \label{eqn:Psi_general_solution}\tag{10}$$

> Ici, $\cfrac{1}{\sqrt{2\pi}}\phi(k)dk$ joue le même rôle que $c_n$ dans [l'équation (21) du post sur 'L'équation de Schrödinger indépendante du temps'](/posts/time-independent-schrodinger-equation/#3-la-solution-générale-de-léquation-de-schrödinger-dépendante-du-temps-est-une-combinaison-linéaire-des-solutions-à-variables-séparées).
{: .prompt-info }

Cette fonction d'onde peut être normalisée pour un $\phi(k)$ approprié, mais elle doit nécessairement avoir une plage de $k$, et donc une plage d'énergies et de vitesses. On appelle cela un **paquet d'ondes**.

> Une fonction sinus est spatialement étendue à l'infini et ne peut donc pas être normalisée. Cependant, en superposant plusieurs de ces ondes, elles peuvent être localisées par interférence et devenir normalisables.
{: .prompt-info }

## Calcul de $\phi(k)$ en utilisant le théorème de Plancherel

Maintenant que nous connaissons la forme de $\Psi(x,t)$ (équation [$\ref{eqn:Psi_general_solution}$]), il nous suffit de déterminer $\phi(k)$ qui satisfait la fonction d'onde initiale

$$ \Psi(x,0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk \label{eqn:Psi_at_t_0}\tag{11}$$

C'est un problème typique d'analyse de Fourier, et nous pouvons obtenir la réponse grâce au **théorème de Plancherel**.

$$ f(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} F(k)e^{ikx}dk \Longleftrightarrow F(k)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-ikx}dx. \label{eqn:plancherel_theorem}\tag{12}$$

On appelle $F(k)$ la **transformée de Fourier** de $f(x)$, et $f(x)$ est la **transformée de Fourier inverse** de $F(k)$. On peut facilement voir dans l'équation ($\ref{eqn:plancherel_theorem}$) que la seule différence entre les deux est le signe de l'exposant. Bien sûr, il existe une condition restrictive selon laquelle seules les fonctions pour lesquelles l'intégrale existe sont autorisées.

> La condition nécessaire et suffisante pour que $f(x)$ existe est que $\int_{-\infty}^{\infty}\|f(x)\|^2dx$ soit finie. Dans ce cas, $\int_{-\infty}^{\infty}\|F(k)\|^2dk$ est également finie, et 
>
> $$ \int_{-\infty}^{\infty}|f(x)|^2 dx = \int_{-\infty}^{\infty}|F(k)|^2 dk $$
>
> Certains appellent cette équation le théorème de Plancherel plutôt que l'équation ($\ref{eqn:plancherel_theorem}$) (c'est ainsi que [Wikipedia](https://en.wikipedia.org/wiki/Plancherel_theorem) le décrit également).
{: .prompt-info }

Dans ce cas, l'intégrale existe nécessairement en raison de la condition physique selon laquelle $\Psi(x,0)$ doit être normalisée. Par conséquent, la solution quantique pour une particule libre est donnée par l'équation ($\ref{eqn:Psi_general_solution}$), où

$$ \phi(k) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\Psi(x,0)e^{-ikx}dx \label{eqn:phi}\tag{13}$$

> Cependant, en pratique, il est rare de pouvoir résoudre analytiquement l'intégrale de l'équation ($\ref{eqn:Psi_general_solution}$). Généralement, on utilise l'analyse numérique par ordinateur pour obtenir les valeurs.
{: .prompt-tip }

## Calcul de la vitesse de groupe du paquet d'ondes et interprétation physique

Essentiellement, un paquet d'ondes est une superposition de nombreuses fonctions sinusoïdales dont l'amplitude est déterminée par $\phi$. En d'autres termes, il y a des "ondulations" à l'intérieur d'une "enveloppe" qui forme le paquet d'ondes.

![A wave packet with the group velocity larger(5x) than phase velocity](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/wave_packet.gif)
> *Mention de la licence de l'image et de la source originale*
> - Code source de génération de l'image (gnuplot) : [yunseo-kim/physics-visualization](https://github.com/yunseo-kim/physics-visualization/blob/main/src/wave_packet.plt)
> - Licence : [Mozilla Public License 2.0](https://github.com/yunseo-kim/physics-visualization/blob/main/LICENSE)
> - Auteur original : [Ph.D. Youjun Hu](https://github.com/youjunhu)
> - Mention de la licence originale : [MIT License](https://github.com/Youjunhu/Youjunhu.github.io/blob/main/LICENSE.txt)

Physiquement, ce qui correspond à la vitesse de la particule n'est pas la vitesse des ondulations individuelles (**vitesse de phase**) calculée précédemment par l'équation ($\ref{eqn:phase_velocity}$), mais la vitesse de l'enveloppe extérieure (**vitesse de groupe**).

### Relation entre l'incertitude sur la position et l'incertitude sur l'impulsion
Examinons la relation entre l'incertitude sur la position et l'incertitude sur l'impulsion en isolant les termes intégrands $\int\phi(k)e^{ikx}dk$ de l'équation ($\ref{eqn:Psi_at_t_0}$) et $\int\Psi(x,0)e^{-ikx}dx$ de l'équation ($\ref{eqn:phi}$).

#### Lorsque l'incertitude sur la position est faible
Lorsque $\Psi$ est distribuée dans une région très étroite $[x_0-\delta, x_0+\delta]$ autour d'une certaine valeur $x_0$ dans l'espace des positions et est proche de zéro ailleurs (<u>lorsque l'incertitude sur la position est faible</u>), $e^{-ikx} \approx e^{-ikx_0}$ est presque constant par rapport à $x$, donc

$$\begin{align*} 
\int_{-\infty}^{\infty} \Psi(x,0)e^{-ikx}dx &\approx \int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)e^{-ikx_0}dx \\
&= e^{-ikx_0}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \\
&= e^{-ipx_0/\hbar}\int_{x_0-\delta}^{x_0+\delta} \Psi(x,0)dx \quad (\because \text{éqn. }\ref{eqn:de_broglie_formula})
\end{align*}\tag{14}$$

Le terme d'intégrale définie est constant par rapport à $p$, donc en raison du terme $e^{-ipx_0/\hbar}$ devant, $\phi$ prend la forme d'une onde sinusoïdale en $p$ dans l'espace des impulsions, c'est-à-dire qu'elle est distribuée sur une large plage d'impulsions (<u>l'incertitude sur l'impulsion est grande</u>).

#### Lorsque l'incertitude sur l'impulsion est faible
De même, lorsque $\phi$ est distribuée dans une région très étroite $[p_0-\delta, p_0+\delta]$ autour d'une certaine valeur $p_0$ dans l'espace des impulsions et est proche de zéro ailleurs (<u>lorsque l'incertitude sur l'impulsion est faible</u>), d'après l'équation ($\ref{eqn:de_broglie_formula}$), $e^{ikx}=e^{ipx/\hbar} \approx e^{ip_0x/\hbar}$ est presque constant par rapport à $p$ et $dk=\frac{1}{\hbar}dp$, donc

$$\begin{align*}
\int_{-\infty}^{\infty} \phi(k)e^{ikx}dk &= \frac{1}{\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)e^{ip_0x/\hbar}dp \\
&= \frac{1}{\hbar}e^{ip_0x/\hbar}\int_{p_0-\delta}^{p_0+\delta} \phi(p)dp
\end{align*}\tag{15}$$

En raison du terme $e^{ip_0x/\hbar}$ devant, $\Psi$ prend la forme d'une onde sinusoïdale en $x$ dans l'espace des positions, c'est-à-dire qu'elle est distribuée sur une large plage de positions (<u>l'incertitude sur la position est grande</u>).

#### Conclusion
Lorsque l'incertitude sur la position diminue, l'incertitude sur l'impulsion augmente, et inversement, lorsque l'incertitude sur l'impulsion diminue, l'incertitude sur la position augmente. Par conséquent, il est impossible en mécanique quantique de connaître simultanément et avec précision la position et l'impulsion d'une particule libre.

![ Quantum mechanics travelling wavefunctions](https://upload.wikimedia.org/wikipedia/commons/3/3e/Quantum_mechanics_travelling_wavefunctions.svg)
> *Source de l'image*
> - Auteur : Utilisateur [Maschen](https://en.wikipedia.org/wiki/User:Maschen) de Wikipédia en anglais
> - Licence : domaine public

> En fait, en raison du principe d'incertitude (uncertainty principle), cela s'applique non seulement aux particules libres, mais à tous les cas. Le principe d'incertitude sera traité dans un post ultérieur séparé.
{: .prompt-info }

### Vitesse de groupe du paquet d'ondes
Si nous réécrivons la solution générale de l'équation ($\ref{eqn:Psi_general_solution}$) comme dans l'équation ($\ref{eqn:phase_velocity}$) avec $\omega \equiv \cfrac{\hbar k^2}{2m}$, nous obtenons

$$ \Psi(x,t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} \phi(k)e^{i(kx-\omega t)}dk \tag{16}$$

> On appelle **relation de dispersion** une équation qui exprime $\omega$ en fonction de $k$, comme $\omega = \cfrac{\hbar k^2}{2m}$. Le contenu qui suit s'applique généralement à tous les paquets d'ondes, indépendamment de la relation de dispersion.
{: .prompt-info }

Supposons maintenant que $\phi(k)$ ait une forme très pointue autour d'une valeur appropriée $k_0$. (Il peut être largement étalé en $k$, mais une telle forme de paquet d'ondes se déforme très rapidement et change de forme. Comme les composantes pour différents $k$ se déplacent chacune à des vitesses différentes, elles perdent le sens d'un "groupe" global bien défini avec une vitesse. En d'autres termes, <u>l'incertitude sur l'impulsion augmente.</u>)  
La fonction intégrée peut être négligée sauf autour de $k_0$, donc nous pouvons développer la fonction $\omega(k)$ en série de Taylor autour de ce point, et en ne gardant que le terme du premier ordre, nous obtenons

$$ \omega(k) \approx \omega_0 + \omega_0^\prime(k-k_0) $$

Maintenant, en substituant $s=k-k_0$ et en intégrant autour de $k_0$, nous obtenons

$$\begin{align*}
\Psi(x,t) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\phi(k_0+s)e^{i[(k_0+s)x-(\omega_0+\omega_0^\prime s)t]}ds \\
&= \frac{1}{\sqrt{2\pi}}e^{i(k_0x-\omega_0t)}\int_{-\infty}^{\infty}\phi(k_0+s)e^{is(x-\omega_0^\prime t)}ds.
\end{align*}\tag{17}$$

Le terme $e^{i(k_0x-\omega_0t)}$ à l'avant représente une onde sinusoïdale ("ondulation") se déplaçant à la vitesse $\omega_0/k_0$, et le terme intégral qui détermine l'amplitude de cette onde sinusoïdale ("enveloppe") se déplace à la vitesse $\omega_0^\prime$ en raison de la partie $e^{is(x-\omega_0^\prime t)}$. Par conséquent, la vitesse de phase à $k=k_0$ est

$$ v_\text{phase} = \frac{\omega_0}{k_0} = \frac{\omega}{k} = \frac{\hbar k}{2m} \tag{18}$$

ce qui confirme à nouveau la valeur de l'équation ($\ref{eqn:phase_velocity}$), et la vitesse de groupe est

$$ v_\text{group} = \omega_0^\prime = \frac{d\omega}{dk} = \frac{\hbar k}{m} \label{eqn:group_velocity}\tag{19}$$

soit le double de la vitesse de phase.

## Comparaison avec la mécanique classique

Sachant que la mécanique classique s'applique à l'échelle macroscopique, les résultats obtenus par la mécanique quantique devraient se rapprocher des calculs de la mécanique classique lorsque l'incertitude quantique est suffisamment faible. Dans le cas de la particule libre que nous traitons actuellement, lorsque $\phi(k)$ a une forme très pointue autour d'une valeur appropriée $k_0$ comme supposé précédemment (c'est-à-dire, <u>lorsque l'incertitude sur l'impulsion est suffisamment faible</u>), la vitesse de groupe $v_\text{group}$ qui correspond à la vitesse de la particule en mécanique quantique devrait être égale à la vitesse de la particule $v_\text{classical}$ calculée en mécanique classique pour les mêmes valeurs de $k$ et d'énergie $E$ correspondante.

En substituant $k\equiv \cfrac{\sqrt{2mE}}{\hbar}$ de l'équation ($\ref{eqn:t_independent_schrodinger_eqn}$) dans la vitesse de groupe que nous venons de calculer (équation [$\ref{eqn:group_velocity}$]), nous obtenons

$$ v_\text{quantum} = \sqrt{\frac{2E}{m}} \tag{20}$$

et la vitesse d'une particule libre ayant une énergie cinétique $E$ en mécanique classique est également

$$ v_\text{classical} = \sqrt{\frac{2E}{m}} \tag{21}$$

Par conséquent, comme $v_\text{quantum}=v_\text{classical}$, nous pouvons confirmer que le résultat obtenu en appliquant la mécanique quantique est une solution physiquement valable.
