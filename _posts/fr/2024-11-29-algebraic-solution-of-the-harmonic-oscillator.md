---
title: "Solution algébrique de l'oscillateur harmonique"
description: >-
  On établit l'équation de Schrödinger pour l'oscillateur harmonique en mécanique quantique et on examine sa résolution algébrique.
  On détermine les fonctions d'onde et les niveaux d'énergie de tout état stationnaire à partir des commutateurs, des relations de commutation canoniques et des opérateurs d'échelle.
categories: [Physique de l'ingénieur, Physique moderne]
tags: [Mécanique quantique, Équation de Schrödinger, Fonction d'onde, Commutateur, Opérateurs d'échelle]
math: true
---

## TL;DR
> - Toute oscillation peut être approximée par une oscillation harmonique simple si l'amplitude est suffisamment petite, ce qui donne à l'oscillation harmonique simple une signification importante en physique
> - Oscillateur harmonique : $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Commutateur** :
>   - Opération binaire indiquant à quel point deux opérateurs ne commutent pas
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Relation de commutation canonique** : $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Opérateurs d'échelle** :
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ est appelé **opérateur de montée**, $\hat{a}\_-$ est appelé **opérateur de descente**
>   - Ils peuvent augmenter ou diminuer le niveau d'énergie pour tout état stationnaire, donc si on trouve une solution de l'équation de Schrödinger indépendante du temps, on peut trouver toutes les autres solutions
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Fonction d'onde et niveau d'énergie du $n$-ième état stationnaire :
>   - État fondamental ($0$-ième état stationnaire) :
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$-ième état stationnaire :
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ est le **conjugué hermitien** et l'**opérateur adjoint** de $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - On peut en déduire les propriétés suivantes :
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Méthode de calcul de la valeur attendue des quantités physiques incluant des puissances de $\hat{x}$ et $\hat{p}$ :
>   1. Exprimer $\hat{x}$ et $\hat{p}$ en termes d'opérateurs de montée et de descente en utilisant la définition des opérateurs d'échelle
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. Exprimer la quantité physique dont on veut calculer la valeur attendue en utilisant les expressions ci-dessus pour $\hat{x}$ et $\hat{p}$
>   3. Utiliser le fait que $\left(\hat{a}\_\pm \right)^m$ est proportionnel à $\psi\_{n\pm m}$ et donc orthogonal à $\psi\_n$, ce qui donne $0$
>   4. Utiliser les propriétés des opérateurs d'échelle pour effectuer le calcul de l'intégrale
{: .prompt-info }

## Prérequis
- [Méthode de séparation des variables](https://www.yunseo.kim/fr/posts/Separation-of-Variables/)
- [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/)
- [Théorème d'Ehrenfest](/posts/ehrenfest-theorem/)
- [Équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/)
- [Le puits carré infini 1D](/posts/the-infinite-square-well/)
- Conjugué hermitien, opérateur adjoint

## Configuration du modèle
### L'oscillateur harmonique en mécanique classique
Un exemple typique d'oscillateur harmonique classique est le mouvement d'une masse $m$ suspendue à un ressort de constante de raideur $k$ (en négligeant le frottement).
Ce mouvement suit la **loi de Hooke** :

$$ F = -kx = m\frac{d^2x}{dt^2} $$

La solution de cette équation est :

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

où

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

est la pulsation de l'oscillation. L'énergie potentielle en fonction de la position $x$ est :

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

qui a une forme parabolique.

Dans la réalité, il n'existe pas d'oscillateur harmonique parfait. Même pour le ressort que nous avons pris comme exemple, si on le tire trop fort, il dépassera sa limite d'élasticité et se cassera ou subira une déformation permanente, et en fait, même avant d'atteindre ce point, il ne suivra déjà plus exactement la loi de Hooke. Néanmoins, la raison pour laquelle l'oscillateur harmonique est important en physique est que tout potentiel arbitraire peut être approximé par une forme parabolique près d'un minimum local. Si on développe un potentiel arbitraire $V(x)$ en série de Taylor autour d'un point minimum, on obtient :

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Maintenant, comme l'ajout d'une constante arbitraire à $V(x)$ n'a aucun effet sur la force, on peut soustraire $V(x_0)$ ici, et en utilisant le fait que $V^\prime(x_0)=0$ puisque $x_0$ est un point minimum, et en négligeant les termes d'ordre supérieur en supposant que $(x-x_0)$ est suffisamment petit, on obtient :

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

Ceci correspond au mouvement d'un oscillateur harmonique avec une constante de ressort effective $k=V^{\prime\prime}(x_0)$ au voisinage du point $x_0$. En d'autres termes, toute oscillation peut être approximée par une oscillation harmonique simple si l'amplitude est suffisamment petite.

> \* Comme on a supposé que $V(x)$ a un minimum en $x_0$, on a $V^{\prime\prime}(x_0) \geq 0$. Dans de rares cas, on peut avoir $V^{\prime\prime}(x_0)=0$, et un tel mouvement ne peut pas être approximé par une oscillation harmonique simple.
{: .prompt-info }

### L'oscillateur harmonique en mécanique quantique
Le problème de l'oscillateur harmonique quantique consiste à résoudre l'équation de Schrödinger pour le potentiel

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

L'[équation de Schrödinger indépendante du temps](/posts/time-independent-schrodinger-equation/) pour l'oscillateur harmonique est :

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

Il existe deux approches complètement différentes pour résoudre ce problème. L'une est une méthode analytique utilisant les **séries de puissances**, et l'autre est une méthode algébrique utilisant les **opérateurs d'échelle**. La méthode algébrique est plus rapide et plus simple, mais il est également nécessaire d'étudier la solution analytique utilisant les séries de puissances. Ici, nous traiterons de la méthode de résolution algébrique, et pour la méthode de résolution analytique, veuillez vous référer à [cet article](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Commutateurs et relation de commutation canonique
On peut réécrire l'équation ($\ref{eqn:t_independent_schrodinger_eqn}$) en utilisant l'opérateur d'impulsion $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$ comme suit :

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Maintenant, factorisons l'hamiltonien (Hamiltonian)

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

Si $p$ et $x$ étaient des nombres, on pourrait facilement factoriser comme suit :

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

mais ici, $\hat{p}$ et $\hat{x}$ sont des opérateurs, et pour les opérateurs, la **propriété commutative** ne s'applique généralement pas ($\hat{p}\hat{x}\neq \hat{x}\hat{p}$), donc ce n'est pas si simple. Cependant, cela peut quand même servir de point de départ, alors commençons par examiner la quantité suivante :

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

Pour les opérateurs $\hat{a}_\pm$ définis ci-dessus, $\hat{a}\_-\hat{a}\_+$ est :

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Ici, le terme $(\hat{x}\hat{p}-\hat{p}\hat{x})$ est appelé le **commutateur** de $\hat{x}$ et $\hat{p}$, et il indique à quel point les deux opérateurs ne commutent pas. En général, le commutateur des opérateurs $\hat{A}$ et $\hat{B}$ est représenté avec des crochets comme suit :

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

En utilisant cette notation, on peut réécrire l'équation ($\ref{eqn:a_m_times_a_p_without_commutator}$) comme suit :

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Maintenant, nous devons déterminer le commutateur de $\hat{x}$ et $\hat{p}$.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

et en enlevant la fonction test $f(x)$, on obtient :

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

C'est ce qu'on appelle la **relation de commutation canonique**.

## Opérateurs d'échelle (ladder operators)
Grâce à la relation de commutation canonique, l'équation ($\ref{eqn:a_m_times_a_p}$) devient :

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

c'est-à-dire

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Ici, l'ordre de $\hat{a}\_-$ et $\hat{a}\_+$ est important, si on place $\hat{a}\_+$ à gauche, on obtient :

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

et

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

est satisfait. Dans ce cas, l'hamiltonien peut aussi s'écrire :

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Donc, si on exprime l'équation de Schrödinger indépendante du temps ($\hat{H}\psi=E\psi$) en termes de $\hat{a}_\pm$, on obtient :

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(le double signe suit l'ordre).

Maintenant, on peut découvrir la propriété importante suivante :

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Preuve :
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> De même,
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Ainsi, si on peut trouver une solution de l'équation de Schrödinger indépendante du temps, on peut trouver toutes les autres solutions. Comme on peut augmenter ou diminuer le niveau d'énergie pour tout état stationnaire, $\hat{a}\_\pm$ sont appelés **opérateurs d'échelle**, $\hat{a}\_+$ étant l'**opérateur de montée** et $\hat{a}\_-$ l'**opérateur de descente**.

## États stationnaires de l'oscillateur harmonique
### États stationnaires $\psi_n$ et niveaux d'énergie $E_n$
Si on continue d'appliquer l'opérateur de descente, on finira par obtenir un état d'énergie inférieure à 0, ce qui est physiquement impossible. Mathématiquement, si $\psi$ est une solution de l'équation de Schrödinger, $\hat{a}_-\psi$ est aussi une solution de l'équation de Schrödinger, mais il n'y a aucune garantie que cette nouvelle solution soit toujours normalisée (c'est-à-dire qu'elle représente un état physiquement possible). Si on continue d'appliquer l'opérateur de descente, on finira par obtenir la solution triviale $\psi=0$.

Donc, pour un état stationnaire $\psi$ de l'oscillateur harmonique, il existe un "niveau le plus bas" $\psi_0$ qui satisfait

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

(il n'existe pas de niveau d'énergie inférieur). Ce $\psi_0$ satisfait

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

donc,

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

C'est une [équation différentielle ordinaire séparable](/posts/Separation-of-Variables/), donc on peut la résoudre facilement comme suit :

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

De plus, cette fonction peut être normalisée comme suit :

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Ici, $A^2 = \sqrt{m\omega / \pi\hbar}$, donc

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Maintenant, si on substitue cette solution dans l'équation de Schrödinger ($\ref{eqn:schrodinger_eqn_with_ladder}$) qu'on a trouvée précédemment, et en utilisant le fait que $\hat{a}_-\psi_0=0$, on obtient :

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

En partant de cet **état fondamental**, et en appliquant continuellement l'opérateur de montée, on peut obtenir des états excités dont l'énergie augmente de $\hbar\omega$ à chaque application de l'opérateur de montée.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

où $A_n$ est une constante de normalisation. Ainsi, après avoir trouvé l'état fondamental, on peut déterminer tous les états stationnaires et les niveaux d'énergie permis de l'oscillateur harmonique en appliquant l'opérateur de montée.

### Normalisation
La constante de normalisation peut également être déterminée algébriquement. Nous savons que $\hat{a}\_{\pm}\psi_n$ est proportionnel à $\psi\_{n\pm 1}$, donc on peut écrire

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Maintenant, notons que pour toutes fonctions intégrables $f(x)$ et $g(x)$, la relation suivante est vraie :

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ est le **conjugué hermitien (hermitian conjugate)** et l'**opérateur adjoint (adjoint operator)** de $\hat{a}\_\pm$.

> **Preuve :**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

Donc, si on pose $f=\hat{a}_\pm \psi_n$, $g=\psi_n$, on obtient

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Alors, à partir des équations ($\ref{eqn:schrodinger_eqn_with_ladder}$) et ($\ref{eqn:psi_n_and_E_n}$), on a

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

Donc, à partir des équations ($\ref{eqn:norm_const}$) et ($\ref{eqn:norm_const_2}$), on obtient

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

Et comme $\psi_n$ et $\psi_{n\pm1}$ sont tous normalisés, on a $\|c_n\|^2=n+1,\ \|d_n\|^2=n$, donc

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

À partir de cela, on peut obtenir n'importe quel état stationnaire normalisé $\psi_n$ comme suit :

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

C'est-à-dire que dans l'équation ($\ref{eqn:psi_n_and_E_n}$), la constante de normalisation est $A_n=\cfrac{1}{\sqrt{n!}}$.

### Orthogonalité des états stationnaires
Comme dans le cas du [puits carré infini 1D](/posts/the-infinite-square-well/#3-ces-états-possèdent-lorthogonalité-orthogonality), les états stationnaires de l'oscillateur harmonique sont orthogonaux.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Preuve
On peut le prouver en utilisant les équations ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$), et ($\ref{eqn:norm_const_3}$) que nous avons montrées précédemment. Dans l'équation ($\ref{eqn:hermitian_conjugate}$), on pose $f=\hat{a}_-\psi_m,\ g=\psi_n$, et on utilise le fait que

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

En utilisant l'orthogonalité, comme nous l'avons fait dans [l'équation (19) du puits carré infini 1D](/posts/the-infinite-square-well/#trouver-la-solution-g%C3%A9n%C3%A9rale-psixt-de-l%C3%A9quation-de-schr%C3%B6dinger-d%C3%A9pendante-du-temps), lorsqu'on développe $\Psi(x,0)$ en combinaison linéaire d'états stationnaires $\sum c_n\psi_n(x)$, on peut trouver les coefficients $c_n$ en utilisant la [méthode de Fourier](/posts/the-infinite-square-well/#calcul-des-coefficients-c_n-en-utilisant-la-m%C3%A9thode-de-fourier-fouriers-trick).

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Ici aussi, $\|c_n\|^2$ est la probabilité d'obtenir la valeur $E_n$ lors de la mesure de l'énergie.

## Valeur attendue de l'énergie potentielle $\langle V \rangle$ dans un état stationnaire arbitraire $\psi_n$
Pour trouver $\langle V \rangle$, nous devons calculer l'intégrale suivante :

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

La méthode suivante est utile pour calculer ce type d'intégrale impliquant des puissances de $\hat{x}$ et $\hat{p}$.

Tout d'abord, on utilise la définition des opérateurs d'échelle de l'équation ($\ref{eqn:ladder_operators}$) pour exprimer $\hat{x}$ et $\hat{p}$ en termes d'opérateurs de montée et de descente.

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Ensuite, on exprime la quantité physique dont on veut calculer la valeur attendue en utilisant ces expressions pour $\hat{x}$ et $\hat{p}$. Ici, nous nous intéressons à $x^2$, donc

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

À partir de cela, on obtient :

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

Et ici, comme $\left(\hat{a}\_\pm \right)^2$ est proportionnel à $\psi\_{n\pm2}$, il est orthogonal à $\psi\_n$, donc les deux termes $\left(\hat{a}\_+ \right)^2$ et $\left(\hat{a}\_- \right)^2$ deviennent $0$. Enfin, en utilisant l'équation ($\ref{eqn:norm_const_2}$) pour calculer les deux termes restants, on obtient

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

En se référant à l'équation ($\ref{eqn:psi_n_and_E_n}$), on peut voir que la valeur attendue de l'énergie potentielle est exactement la moitié de l'énergie totale, et l'autre moitié est naturellement l'énergie cinétique $T$. C'est une caractéristique propre à l'oscillateur harmonique.
