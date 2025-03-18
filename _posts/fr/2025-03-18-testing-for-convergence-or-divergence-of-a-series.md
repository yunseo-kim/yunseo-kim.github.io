---
title: Test de convergence/divergence des séries (Testing for Convergence or Divergence of a Series)
description: On examine diverses méthodes pour déterminer la convergence ou la divergence des séries.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Test du terme général (n-ième test pour la divergence)** : $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la série }\sum a_n \text{ diverge}$
> - **Convergence/divergence de la série géométrique** : La série géométrique $\sum ar^{n-1}$ 
>   - converge si $\|r\| < 1$
>   - diverge si $\|r\| \geq 1$
> - **Convergence/divergence de la série p** : La série p $\sum \cfrac{1}{n^p}$
>   - converge si $p>1$
>   - diverge si $p\leq 1$
> - **Test de comparaison (Comparison Test)** : Si $0 \leq a_n \leq b_n$, alors  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Test de comparaison limite (Limit Comparison Test)** : Si $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ est un nombre positif fini)}$, alors les deux séries $\sum a_n$ et $\sum b_n$ convergent toutes les deux ou divergent toutes les deux
> - Pour une série à termes positifs $\sum a_n$ et un nombre positif $\epsilon < 1$  
>   - Si $\sqrt[n]{a_n}< 1-\epsilon$ pour tout $n$, alors la série $\sum a_n$ converge
>   - Si $\sqrt[n]{a_n}> 1+\epsilon$ pour tout $n$, alors la série $\sum a_n$ diverge
> - **Test de la racine (Root Test)** : Pour une série à termes positifs $\sum a_n$, si la limite $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ existe,
>   - la série $\sum a_n$ converge si $r<1$
>   - la série $\sum a_n$ diverge si $r>1$
> - **Test du rapport (Ratio Test)** : Pour une suite de nombres positifs $(a_n)$ et $0 < r < 1$
>   - Si $a_{n+1}/a_n \leq r$ pour tout $n$, alors la série $\sum a_n$ converge
>   - Si $a_{n+1}/a_n \geq 1$ pour tout $n$, alors la série $\sum a_n$ diverge
> - Pour une suite de nombres positifs $(a_n)$, si la limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existe,
>   - la série $\sum a_n$ converge si $\rho < 1$
>   - la série $\sum a_n$ diverge si $\rho > 1$
> - **Test de l'intégrale (Integral Test)** : Pour une fonction continue et décroissante $f: [1,\infty) \rightarrow \mathbb{R}$ avec $f(x)>0$ pour tout $x$, la série $\sum f(n)$ converge si et seulement si l'intégrale $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ converge
> - **Test des séries alternées (Alternating Series Test)** : Une série alternée $\sum a_n$ converge si les conditions suivantes sont satisfaites :
>   1. $a_n$ et $a_{n+1}$ ont des signes opposés pour tout $n$
>   2. $\|a_n\| \geq \|a_{n+1}\|$ pour tout $n$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Une série qui converge absolument converge. La réciproque n'est pas vraie.
{: .prompt-info }

## Prérequis
- [Suites et séries](/posts/sequences-and-series/)

## Introduction
Dans [Suites et séries](/posts/sequences-and-series/#convergence-et-divergence-des-séries), nous avons vu la définition de la convergence et de la divergence des séries. Dans cet article, nous allons résumer diverses méthodes qui peuvent être utilisées pour déterminer la convergence ou la divergence des séries. En général, il est beaucoup plus facile de déterminer la convergence/divergence d'une série que de calculer sa somme exacte.

## Test du terme général
Pour une série $\sum a_n$, $a_n$ est appelé le **terme général** de cette série.

Le théorème suivant permet de déterminer facilement que certaines séries divergent manifestement, et il est donc sage de le vérifier en premier lieu lors de l'évaluation de la convergence/divergence d'une série afin d'éviter de perdre du temps.

> **Test du terme général (n-ième test pour la divergence)**  
> Si la série $\sum a_n$ converge, alors
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> C'est-à-dire,
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la série }\sum a_n \text{ diverge} $$
{: .prompt-info }

### Démonstration
Soit $l$ la somme d'une série convergente $\sum a_n$ et soit $s_n$ la somme des $n$ premiers termes :

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Alors,

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Donc, pour $n$ suffisamment grand ($>N$),

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Par conséquent, de la définition de la convergence d'une suite,

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Attention
La réciproque de ce théorème n'est généralement pas vraie. Un exemple typique qui le démontre est la **série harmonique**.

La série harmonique est une série obtenue à partir d'une suite dont chaque terme est l'inverse d'une **suite arithmétique**, c'est-à-dire une **suite harmonique**. La série harmonique typique est

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

On peut montrer que cette série diverge comme suit :

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Comme on peut le voir, bien que la série $H_n$ diverge, son terme général $1/n$ converge vers 0.

> Si $\lim_{n\to\infty} a_n \neq 0$, alors la série $\sum a_n$ diverge nécessairement, mais il est dangereux de penser que la série $\sum a_n$ convergera si $\lim_{n\to\infty} a_n = 0$, et dans ce cas, d'autres méthodes doivent être utilisées pour déterminer la convergence/divergence.
{: .prompt-danger }

## Série géométrique
La **série géométrique** obtenue à partir d'une suite géométrique avec le premier terme égal à 1 et une **raison** $r$

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

est <u>la série la plus importante et fondamentale</u>. De l'égalité

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

on obtient

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

D'autre part,

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

donc on sait que la condition nécessaire et suffisante pour que la série géométrique ($\ref{eqn:geometric_series}$) converge est $\|r\| < 1$.

> **Convergence/divergence de la série géométrique**  
> La série géométrique $\sum ar^{n-1}$
> - converge si $\|r\| < 1$
> - diverge si $\|r\| \geq 1$
{: .prompt-info }

De là, on obtient

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Série géométrique et valeur approchée
L'identité ($\ref{eqn:sum_of_geometric_series}$) est utile pour trouver une valeur approchée de $\cfrac{1}{1-r}$ lorsque $|r| < 1$.

En substituant $r=-\epsilon$ et $n=2$ dans cette équation, on obtient

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Donc, si $0 < \epsilon < 1$,

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

Par conséquent,

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

De là, on peut voir que pour un nombre positif $\epsilon$ suffisamment petit, $\cfrac{1}{1 + \epsilon}$ peut être approximé par $1 - \epsilon$.

## Test de la série p (p-Series Test)  
Pour un nombre réel positif $p$, une série de la forme suivante est appelée **série p** :

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Convergence/divergence de la série p**  
> La série p $\sum \cfrac{1}{n^p}$
> - converge si $p>1$
> - diverge si $p\leq 1$
{: .prompt-info }

Dans la série p, le cas où $p=1$ devient la série harmonique, qui, comme nous l'avons vu précédemment, diverge.  
Le problème de trouver la valeur de la série p lorsque $p=2$, c'est-à-dire $\sum \cfrac{1}{n^2}$, est appelé le problème de Bâle, du nom de la ville d'origine de la famille Bernoulli, qui a produit plusieurs mathématiciens célèbres sur plusieurs générations et qui a été la première à montrer que cette série converge. On sait que la réponse à ce problème est $\cfrac{\pi^2}{6}$.

Plus généralement, la série p avec $p>1$ est appelée **fonction zêta**. Il s'agit d'une fonction spéciale introduite par Leonhard Euler en 1740 et nommée plus tard par Riemann, définie comme

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Ce sujet s'éloigne un peu du thème de cet article, et pour être honnête, comme je suis un étudiant en ingénierie et non un mathématicien, je ne le connais pas bien non plus, donc je ne vais pas l'aborder ici. Cependant, Leonhard Euler a montré que la fonction zêta peut également être exprimée sous forme d'un produit infini de nombres premiers appelé **produit d'Euler**, et par la suite, la fonction zêta occupe une position centrale dans plusieurs domaines de la théorie analytique des nombres. La **fonction zêta de Riemann**, qui étend le domaine de définition de la fonction zêta aux nombres complexes, et l'important problème non résolu qui lui est associé, l'**hypothèse de Riemann**, en font partie.

Pour revenir au sujet initial, la démonstration du test de la série p nécessite le [test de comparaison](#test-de-comparaison) et le [test de l'intégrale](#test-de-lintégrale) qui seront abordés plus loin. Cependant, la convergence/divergence de la série p peut être utilisée efficacement dans le [test de comparaison](#test-de-comparaison) qui suit immédiatement, c'est pourquoi elle a été intentionnellement placée plus tôt.

### Démonstration
#### i) Lorsque $p>1$
L'intégrale

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

converge, donc par le [test de l'intégrale](#test-de-lintégrale), on sait que la série $\sum \cfrac{1}{n^p}$ converge également.

#### ii) Lorsque $p\leq 1$
Dans ce cas,

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Ici, nous savons que la série harmonique $\sum \cfrac{1}{n}$ diverge, donc par le [test de comparaison](#test-de-comparaison), on sait que $\sum \cfrac{1}{n^p}$ diverge également.

#### Conclusion
Par i) et ii), la série p $\sum \cfrac{1}{n^p}$ converge si $p>1$ et diverge si $p \leq 1$. $\blacksquare$

## Test de comparaison
Le **test de comparaison** de Jakob Bernoulli est utile pour déterminer la convergence/divergence d'une **série à termes positifs**, c'est-à-dire une série dont le terme général est composé de nombres réels non négatifs.

Comme une série à termes positifs $\sum a_n$ est une suite croissante, elle converge nécessairement si elle ne diverge pas vers l'infini ($\sum a_n = \infty$). Donc, dans une série à termes positifs, l'expression

$$ \sum a_n < \infty $$

signifie que <u>la série converge</u>.

> **Test de comparaison (Comparison Test)**  
> Si $0 \leq a_n \leq b_n$, alors  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

En particulier, pour les séries à termes positifs qui ont une forme similaire à la série géométrique $\sum ar^{n-1}$ ou à la série p $\sum \cfrac{1}{n^p}$ que nous avons vues précédemment, comme $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, etc., il est bon d'essayer activement le test de comparaison pour déterminer leur convergence/divergence.

Toutes les autres méthodes de détermination de la convergence/divergence mentionnées ci-après peuvent être dérivées de ce **test de comparaison**, et en ce sens, on peut dire que le test de comparaison est le plus important.

### Test de comparaison limite
Pour les séries à termes positifs $\sum a_n$ et $\sum b_n$, supposons que le rapport des termes généraux des deux séries $a_n/b_n$ ait une limite $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ est un nombre positif fini)}$ où les termes dominants du numérateur et du dénominateur s'annulent. Dans ce cas, si on connaît la convergence/divergence de la série $\sum b_n$, on peut utiliser le **test de comparaison limite** suivant.

> **Test de comparaison limite (Limit Comparison Test)**  
> Si
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ est un nombre positif fini)}$$
>
> alors les deux séries $\sum a_n$ et $\sum b_n$ convergent toutes les deux ou divergent toutes les deux. C'est-à-dire, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Test de la racine
> **Théorème**  
> Pour une série à termes positifs $\sum a_n$ et un nombre positif $\epsilon < 1$  
> - Si $\sqrt[n]{a_n}< 1-\epsilon$ pour tout $n$, alors la série $\sum a_n$ converge
> - Si $\sqrt[n]{a_n}> 1+\epsilon$ pour tout $n$, alors la série $\sum a_n$ diverge
{: .prompt-info }

> **Corollaire : Test de la racine (Root Test)**  
> Pour une série à termes positifs $\sum a_n$, supposons que la limite
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> existe. Alors,
> - la série $\sum a_n$ converge si $r<1$
> - la série $\sum a_n$ diverge si $r>1$
{: .prompt-info }

> Dans le corollaire ci-dessus, si $r=1$, on ne peut pas déterminer la convergence/divergence, il faut donc utiliser une autre méthode.
{: .prompt-warning }

## Test du rapport
> **Test du rapport (Ratio Test)**  
> Pour une suite de nombres positifs $(a_n)$ et $0 < r < 1$
> - Si $a_{n+1}/a_n \leq r$ pour tout $n$, alors la série $\sum a_n$ converge
> - Si $a_{n+1}/a_n \geq 1$ pour tout $n$, alors la série $\sum a_n$ diverge
{: .prompt-info }

> **Corollaire**  
> Pour une suite de nombres positifs $(a_n)$, supposons que la limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existe. Alors,
> - la série $\sum a_n$ converge si $\rho < 1$
> - la série $\sum a_n$ diverge si $\rho > 1$
{: .prompt-info }

## Test de l'intégrale
Le calcul intégral peut être utilisé pour déterminer la convergence/divergence d'une série composée d'une suite décroissante de nombres positifs.

> **Test de l'intégrale (Integral Test)**  
> Pour une fonction continue et décroissante $f: [1,\infty) \rightarrow \mathbb{R}$ avec $f(x)>0$ pour tout $x$, la série $\sum f(n)$ converge si et seulement si l'intégrale
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> converge.
{: .prompt-info }

### Démonstration
Si la fonction $f(x)$ est continue, décroissante et toujours positive, alors l'inégalité

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

est vraie. En additionnant les termes de cette inégalité de $n=1$ jusqu'au terme général, on obtient l'inégalité

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Maintenant, en appliquant le [test de comparaison](#test-de-comparaison), on obtient le résultat souhaité. $\blacksquare$

## Série alternée
Une série $\sum a_n$ dont le terme général $a_n$ est non nul et de signe opposé à celui du terme suivant $a_{n+1}$, c'est-à-dire une série où les termes positifs et négatifs apparaissent alternativement, est appelée **série alternée**.

Pour les séries alternées, le théorème suivant, découvert par le mathématicien allemand Gottfried Wilhelm Leibniz, peut être utilisé efficacement pour déterminer la convergence/divergence.

> **Test des séries alternées (Alternating Series Test)**  
> Une série alternée $\sum a_n$ converge si les conditions suivantes sont satisfaites :
> 1. $a_n$ et $a_{n+1}$ ont des signes opposés pour tout $n$,
> 2. $\|a_n\| \geq \|a_{n+1}\|$ pour tout $n$, et
> 3. $\lim_{n\to\infty} a_n = 0$.
{: .prompt-info }

## Série absolument convergente
Pour une série $\sum a_n$, si la série $\sum \|a_n\|$ converge, on dit que "la série $\sum a_n$ **converge absolument**".

Dans ce cas, le théorème suivant est vrai.

> **Théorème**  
> Une série qui converge absolument converge.
{: .prompt-info }

> La réciproque du théorème ci-dessus n'est pas vraie.  
> Lorsqu'une série converge mais ne converge pas absolument, on dit qu'elle "**converge conditionnellement**".
{: .prompt-warning }

### Démonstration
Pour un nombre réel $a$, posons

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Alors,

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Comme $0 \leq a^\pm \leq \|a\|$, par le [test de comparaison](#test-de-comparaison), si la série $\sum \|a_n\|$ converge, alors les séries $\sum a_n^+$ et $\sum a_n^-$ convergent également, et donc par la [propriétés fondamentales des séries convergentes](/posts/sequences-and-series/#propriétés-fondamentales-des-séries-convergentes),

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

converge également. $\blacksquare$
