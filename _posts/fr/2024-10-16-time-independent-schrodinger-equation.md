---
title: Équation de Schrödinger indépendante du temps
description: Nous dérivons l'équation de Schrödinger indépendante du temps ψ(x) en
  appliquant la méthode de séparation des variables à la forme originale de l'équation
  de Schrödinger (dépendante du temps) Ψ(x,t). Nous examinons la signification et
  l'importance mathématique et physique de la solution à variables séparées ainsi
  obtenue. Enfin, nous étudions comment obtenir la solution générale de l'équation
  de Schrödinger par combinaison linéaire des solutions à variables séparées.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - Solution à variables séparées : $ \Psi(x,t) = \psi(x)\phi(t)$
> - Dépendance temporelle ("facteur d'oscillation") : $ \phi(t) = e^{-iEt/\hbar} $
> - Opérateur hamiltonien : $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - Équation de Schrödinger indépendante du temps : $ \hat H\psi = E\psi $
> - Signification physique et mathématique et importance de la solution à variables séparées :
>   1. États stationnaires
>   2. Valeur d'énergie totale $E$ bien définie
>   3. La solution générale de l'équation de Schrödinger est une combinaison linéaire des solutions à variables séparées
> - Solution générale de l'équation de Schrödinger dépendante du temps : $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Prérequis
- Distributions de probabilité continues et densité de probabilité
- [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/)
- [Théorème d'Ehrenfest](/posts/ehrenfest-theorem/)
- [Méthode de séparation des variables](/posts/Separation-of-Variables/)

## Dérivation utilisant la méthode de séparation des variables
Dans le [post sur le théorème d'Ehrenfest](/posts/ehrenfest-theorem/), nous avons examiné comment calculer diverses quantités physiques à l'aide de la fonction d'onde $\Psi$. La question importante est alors de savoir comment obtenir cette fonction d'onde $\Psi(x,t)$. Généralement, il faut résoudre [l'équation de Schrödinger](/posts/schrodinger-equation-and-the-wave-function/), qui est une équation aux dérivées partielles en position $x$ et en temps $t$ pour un potentiel donné $V(x,t)$.

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

Si le potentiel $V$ est indépendant du temps $t$, on peut résoudre l'équation de Schrödinger ci-dessus en utilisant la [méthode de séparation des variables](/posts/Separation-of-Variables/). Considérons une solution de la forme du produit d'une fonction $\psi$ de $x$ seul et d'une fonction $\phi$ de $t$ seul :

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

À première vue, cela peut sembler être une expression excessivement restrictive qui ne permettrait d'obtenir qu'un petit sous-ensemble de la solution complète, mais en réalité, la solution ainsi obtenue a une signification importante et on peut obtenir la solution générale en additionnant ces solutions séparables d'une manière spécifique.

Pour une solution séparable, on a

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

En substituant cela dans l'équation ($\ref{eqn:schrodinger_eqn}$), on peut écrire l'équation de Schrödinger comme suit :

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

En divisant les deux côtés par $\psi\phi$, on obtient

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

où le côté gauche est une fonction de $t$ seul et le côté droit est une fonction de $x$ seul.

Pour que cette équation ait une solution, les deux côtés doivent être constants. Sinon, si on maintenait une des variables $t$ ou $x$ constante tout en faisant varier l'autre, un seul côté de l'équation changerait, rendant l'égalité fausse. On peut donc poser le côté gauche égal à une constante de séparation $E$.

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

On obtient alors deux équations différentielles ordinaires, l'une étant

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

pour la partie temporelle, et l'autre étant

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

pour la partie spatiale.

L'équation différentielle ordinaire ($\ref{eqn:ode_t}$) en $t$ peut être facilement résolue. La solution générale de cette équation est $ce^{-iEt/\hbar}$, mais comme on s'intéresse au produit $\psi\phi$ plutôt qu'à $\phi$ lui-même, on peut inclure la constante $c$ dans $\psi$. On obtient alors

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

L'équation différentielle ordinaire ($\ref{eqn:t_independent_schrodinger_eqn}$) en $x$ est appelée **équation de Schrödinger indépendante du temps**. On ne peut résoudre cette équation que si on connaît le potentiel $V(x)$.

## Signification physique et mathématique
Nous avons précédemment obtenu la fonction $\phi(t)$ dépendante uniquement du temps et l'équation de Schrödinger indépendante du temps ($\ref{eqn:t_independent_schrodinger_eqn}$) en utilisant la méthode de séparation des variables. Bien que la plupart des solutions de l'**équation de Schrödinger dépendante du temps** originale ($\ref{eqn:schrodinger_eqn}$) ne puissent pas être exprimées sous la forme $\psi(x)\phi(t)$, la forme de l'équation de Schrödinger indépendante du temps reste importante en raison des trois propriétés suivantes de sa solution.

### 1. Ce sont des états stationnaires.
Bien que la fonction d'onde elle-même

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

dépende de $t$, la densité de probabilité

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

est constante dans le temps car la dépendance temporelle s'annule.

> Pour une solution normalisable, la constante de séparation $E$ doit être réelle.
>
> Si on pose $E$ dans l'équation ($\ref{eqn:separation_of_variables}$) comme un nombre complexe $E_0+i\Gamma$ (où $E_0$ et $\Gamma$ sont réels), alors
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty}|\Psi|^2dx &= \int_{-\infty}^{\infty}\Psi^*\Psi dx \\
> &= \int_{-\infty}^{\infty} \left(\psi e^{-iEt/\hbar}\right)^*\left(\psi e^{-iEt/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right)^*\left(\psi e^{-i(E_0+i\Gamma)t/\hbar}\right) dx \\
> &= \int_{-\infty}^{\infty}\psi^* e^{(\Gamma-iE_0)t/\hbar}\psi e^{(\Gamma+iE_0)t/\hbar}dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} \psi^*\psi dx \\
> &= e^{2\Gamma t/\hbar} \int_{-\infty}^{\infty} |\psi|^2 dx
> \end{align*} $$
>
> Comme nous l'avons vu précédemment dans [Équation de Schrödinger et fonction d'onde](/posts/schrodinger-equation-and-the-wave-function/#normalisation-de-la-fonction-donde-normalization), $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ doit être une constante indépendante du temps, donc $\Gamma=0$. $\blacksquare$
{: .prompt-info }

Le même phénomène se produit lors du calcul de la valeur attendue de toute quantité physique, de sorte que l'équation (8) du [théorème d'Ehrenfest](/posts/ehrenfest-theorem/) devient

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

Ainsi, toutes les valeurs attendues sont constantes par rapport au temps. En particulier, comme $\langle x \rangle$ est constant, $\langle p \rangle=0$.

### 2. Ils ont une valeur d'énergie totale définie e pas une distribution de probabilité sur une plage
En mécanique classique, l'énergie totale (énergie cinétique plus énergie potentielle) est appelée **hamiltonien** et est définie comme

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

Donc, en remplaçant $p$ par $-i\hbar(\partial/\partial x)$, l'opérateur hamiltonien correspondant en mécanique quantique est

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

Ainsi, l'équation de Schrödinger indépendante du temps ($\ref{eqn:t_independent_schrodinger_eqn}$) peut s'écrire

$$ \hat H \psi = E\psi \tag{15}$$

et la valeur attendue de l'hamiltonien est

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

De plus,

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

est vrai, donc

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

Par conséquent, la variance de l'hamiltonien $H$ est

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

En d'autres termes, la solution à variables séparées donne toujours une mesure constante $E$ lorsque l'énergie totale est mesurée.

### 3. La solution générale de l'équation de Schrödinger dépendante du temps est une combinaison linéaire des solutions à variables séparées.

L'équation de Schrödinger indépendante du temps ($\ref{eqn:t_independent_schrodinger_eqn}$) a une infinité de solutions $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$. Appelons-les \{$\psi_n(x)$\}. Pour chacune d'entre elles, il existe des constantes de séparation $E_1,E_2,E_3,\dots=$\{$E_n$\}, donc pour chaque **niveau d'énergie possible**, il y a une fonction d'onde correspondante.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

L'équation de Schrödinger dépendante du temps ($\ref{eqn:schrodinger_eqn}$) a la propriété que la combinaison linéaire de deux solutions quelconques est également une solution, donc une fois que nous avons trouvé les solutions à variables séparées, nous pouvons immédiatement obtenir une forme plus générale de solution :

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

Toute solution de l'équation de Schrödinger dépendante du temps peut être écrite sous cette forme, et il ne reste plus qu'à trouver les constantes appropriées $c_1, c_2, \dots$ pour satisfaire les conditions initiales données dans le problème afin de trouver la solution particulière souhaitée. En d'autres termes, si nous pouvons résoudre l'équation de Schrödinger indépendante du temps, nous pouvons ensuite facilement trouver la solution générale de l'équation de Schrödinger dépendante du temps.

> Notez que bien que la solution à variables séparées 
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> soit un état stationnaire où toutes les probabilités et valeurs attendues sont indépendantes du temps, la solution générale de l'équation ($\ref{eqn:general_solution}$) n'a pas cette propriété.
{: .prompt-warning }

## Conservation de l'énergie
Dans la solution générale ($\ref{eqn:general_solution}$), le carré du module des coefficients \{$c_n$\}, $\|c_n\|^2$, représente physiquement la probabilité de mesurer la valeur $E_n$ lors de la mesure de l'énergie d'une particule dans cet état ($\Psi$). Par conséquent, la somme de ces probabilités doit être

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

égale à 1, et la valeur attendue de l'hamiltonien est

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

Comme les niveaux d'énergie $E_n$ de chaque état stationnaire et les coefficients \{$c_n$\} sont indépendants du temps, la probabilité de mesurer une énergie spécifique $E_n$ ou la valeur attendue de l'hamiltonien $H$ reste également constante, indépendamment du temps.
