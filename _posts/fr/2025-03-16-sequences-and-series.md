---
title: Suites et séries
description: Nous examinons les concepts fondamentaux du calcul différentiel et intégral, tels que la définition des suites et séries, la convergence et la divergence des suites, la convergence et la divergence des séries, et la définition du nombre e.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## Suites
En calcul différentiel et intégral, une **suite (sequence)** fait généralement référence à une suite infinie. En d'autres termes, une suite est une fonction définie sur l'ensemble des **nombres naturels (natural numbers)**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

Si les valeurs de cette fonction sont des nombres réels, on parle de 'suite réelle', si ce sont des nombres complexes, de 'suite complexe', si ce sont des points, de 'suite de points', si ce sont des matrices, de 'suite de matrices', si ce sont des fonctions, de 'suite de fonctions', si ce sont des ensembles, de 'suite d'ensembles', mais tous ces termes peuvent être simplement désignés par 'suite' ou 'séquence'.

Généralement, pour le **corps des nombres réels (the field of real numbers)** $\mathbb{R}$, dans une suite $\mathbf{a}: \mathbb{N} \to \mathbb{R}$, on pose

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

et cette suite est représentée par

$$ a_1,\, a_2,\, a_3,\, \dots $$

ou

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

> *Dans le processus de définition d'une suite, au lieu de l'ensemble complet des nombres naturels $\mathbb{N}$, on peut choisir comme domaine de définition l'ensemble des entiers non négatifs
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> ou
>
> $$\{2,3,4,\dots \}$$
>
> Par exemple, lors de l'étude de la théorie des séries entières, il est plus naturel d'avoir $\mathbb{N}_0$ comme domaine de définition.
{: .prompt-info }

## Convergence et divergence
Si une suite $(a_n)$ converge vers un nombre réel $l$, on écrit

$$ \lim_{n\to \infty} a_n = l $$

et $l$ est appelé la **valeur limite** de la suite $(a_n)$.

> La définition rigoureuse utilisant l'**argument epsilon-delta (epsilon-delta argument)** est la suivante :
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> En d'autres termes, si pour tout nombre positif $\epsilon$, aussi petit soit-il, il existe toujours un nombre naturel $N$ tel que $\|a_n - l \| < \epsilon$ pour $n>N$, cela signifie que la différence entre $a_n$ et $l$ devient infiniment petite pour $n$ suffisamment grand, et donc on définit que la suite $(a_n)$ converge vers le nombre réel $l$.
{: .prompt-info }

Une suite qui ne converge pas est dite **divergente**. *La convergence ou la divergence d'une suite ne change pas si un nombre fini de ses termes est modifié.*

Si chaque terme de la suite $(a_n)$ devient infiniment grand, on écrit

$$ \lim_{n\to \infty} a_n = \infty $$

et on dit que la suite *diverge vers plus l'infini*. De même, si chaque terme de la suite $(a_n)$ devient infiniment petit, on écrit

$$ \lim_{n\to \infty} a_n = -\infty $$

et on dit que la suite *diverge vers moins l'infini*.

## Propriétés fondamentales des suites convergentes
Si les suites $(a_n)$ et $(b_n)$ convergent toutes les deux (c'est-à-dire qu'elles ont des valeurs limites), alors les suites $(a_n + b_n)$ et $(a_n \cdot b_n)$ convergent également, et dans ce cas

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

De plus, pour tout nombre réel $t$,

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Ces propriétés sont appelées **propriétés fondamentales des suites convergentes** ou **propriétés fondamentales des limites**.

## Nombre e
Le **nombre e** est défini par

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

C'est l'une des constantes les plus importantes en mathématiques.

## Séries
Pour une suite

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

la nouvelle suite formée par les sommes partielles de cette suite

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

est appelée la **série** de la suite $\mathbf{a}$. La série de la suite $(a_n)$ est notée

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

## Convergence et divergence des séries
Si la série obtenue à partir de la suite $(a_n)$

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

converge vers un nombre réel $l$, on écrit

$$ \sum_{n=1}^{\infty} a_n = l $$

Dans ce cas, la valeur limite $l$ est appelée la **somme** de la série $\sum a_n$. Le symbole

$$ \sum a_n $$

peut représenter soit la <u>série</u>, soit la <u>somme de la série</u>, selon le contexte.

Une série qui ne converge pas est dite **divergente**.

## Propriétés fondamentales des séries convergentes
À partir des [propriétés fondamentales des suites convergentes](#propriétés-fondamentales-des-suites-convergentes), on obtient les propriétés fondamentales suivantes pour les séries convergentes. Pour un nombre réel $t$ et deux séries convergentes $\sum a_n$ et $\sum b_n$,

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n $$

La convergence d'une série n'est pas affectée par le changement d'un nombre fini de termes. En d'autres termes, si pour deux suites $(a_n)$ et $(b_n)$, $a_n=b_n$ sauf pour un nombre fini de $n$, alors la série $\sum a_n$ converge si et seulement si la série $\sum b_n$ converge.
