---
title: Test de convergence/divergence d'une série (Testing for Convergence or Divergence of a Series)
description: Examen des différentes méthodes pour déterminer la convergence ou la divergence d'une série.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Test du terme général ($n$th-term test for divergence)** : $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la série }\sum a_n \text{ diverge}$
> - **Convergence/divergence des séries géométriques** : La série géométrique $\sum ar^{n-1}$ :
>   - converge si $\|r\| < 1$
>   - diverge si $\|r\| \geq 1$
> - **Convergence/divergence des séries $p$** : La série $p$ $\sum \cfrac{1}{n^p}$ :
>   - converge si $p>1$
>   - diverge si $p\leq 1$
> - **Test de comparaison (Comparison Test)** : Si $0 \leq a_n \leq b_n$, alors :  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Test de comparaison limite (Limit Comparison Test)** : Si $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (où }c\text{ est un nombre positif fini)}$, alors les deux séries $\sum a_n$ et $\sum b_n$ convergent toutes les deux ou divergent toutes les deux
> - Pour une série à termes positifs $\sum a_n$ et un nombre positif $\epsilon < 1$ :  
>   - Si pour tout $n$, $\sqrt[n]{a_n}< 1-\epsilon$, alors la série $\sum a_n$ converge
>   - Si pour tout $n$, $\sqrt[n]{a_n}> 1+\epsilon$, alors la série $\sum a_n$ diverge
> - **Test de la racine (Root Test)** : Pour une série à termes positifs $\sum a_n$, si la limite $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ existe :
>   - Si $r<1$, alors la série $\sum a_n$ converge
>   - Si $r>1$, alors la série $\sum a_n$ diverge
> - **Test du rapport (Ratio Test)** : Pour une suite de nombres positifs $(a_n)$ et $0 < r < 1$ :
>   - Si pour tout $n$, $a_{n+1}/a_n \leq r$, alors la série $\sum a_n$ converge
>   - Si pour tout $n$, $a_{n+1}/a_n \geq 1$, alors la série $\sum a_n$ diverge
> - Pour une suite de nombres positifs $(a_n)$, si la limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existe :
>   - Si $\rho < 1$, alors la série $\sum a_n$ converge
>   - Si $\rho > 1$, alors la série $\sum a_n$ diverge
> - **Test de l'intégrale (Integral Test)** : Si $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ est une fonction continue, décroissante et toujours positive, alors la série $\sum f(n)$ converge si et seulement si l'intégrale $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ converge
> - **Test des séries alternées (Alternating Series Test)** : Une série alternée $\sum a_n$ converge si les conditions suivantes sont satisfaites :
>   1. Pour tout $n$, $a_n$ et $a_{n+1}$ ont des signes opposés
>   2. Pour tout $n$, $\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Une série qui converge absolument converge. La réciproque n'est pas vraie.
{: .prompt-info }

## Prérequis
- [Suites et séries](/posts/sequences-and-series/)

## Introduction
Dans l'article précédent sur [les suites et séries](/posts/sequences-and-series/#convergence-et-divergence-des-séries), nous avons vu les définitions de convergence et divergence des séries. Dans cet article, nous allons résumer les différentes méthodes pour déterminer si une série converge ou diverge. En général, déterminer la convergence ou la divergence d'une série est beaucoup plus facile que de calculer sa somme exacte.

## Test du terme général
Pour une série $\sum a_n$, on appelle $a_n$ le **terme général** de cette série.

Le théorème suivant permet de déterminer facilement la divergence de certaines séries, et il est donc judicieux de le vérifier en premier lieu pour éviter de perdre du temps.

> **Test du terme général ($n$th-term test for divergence)**  
> Si une série $\sum a_n$ converge, alors :
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> C'est-à-dire :
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{la série }\sum a_n \text{ diverge} $$
{: .prompt-info }

### Démonstration
Soit $\sum a_n$ une série convergente de somme $l$, et soit $s_n$ la somme des $n$ premiers termes :

$$ s_n := a_1 + a_2 + \cdots + a_n $$

Alors :

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Donc pour $n$ suffisamment grand ($>N$) :

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

Par la définition de la convergence d'une suite :

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Mise en garde
La réciproque de ce théorème n'est généralement pas vraie. Un exemple classique est la **série harmonique (harmonic series)**.

La série harmonique est une série dont les termes sont les inverses d'une **suite arithmétique**, c'est-à-dire une **suite harmonique**. La série harmonique la plus connue est :

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

On peut montrer que cette série diverge comme suit :

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Ainsi, bien que la série $H_n$ diverge, son terme général $1/n$ converge vers $0$.

> Si $\lim_{n\to\infty} a_n \neq 0$, alors la série $\sum a_n$ diverge nécessairement, mais si $\lim_{n\to\infty} a_n = 0$, il est risqué de supposer que la série $\sum a_n$ converge. Dans ce cas, il faut utiliser d'autres méthodes pour déterminer la convergence ou la divergence.
{: .prompt-danger }

## Séries géométriques
La **série géométrique (geometric series)** dont le premier terme est 1 et la **raison** est $r$ :

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

est <u>la série la plus importante et fondamentale</u>. De l'égalité :

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

on obtient :

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

D'autre part :

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

Donc, la condition nécessaire et suffisante pour que la série géométrique ($\ref{eqn:geometric_series}$) converge est $\|r\| < 1$.

> **Convergence/divergence des séries géométriques**  
> La série géométrique $\sum ar^{n-1}$ :
> - converge si $\|r\| < 1$
> - diverge si $\|r\| \geq 1$
{: .prompt-info }

On en déduit :

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Séries géométriques et approximations
L'identité ($\ref{eqn:sum_of_geometric_series}$) est utile pour calculer des approximations de $\cfrac{1}{1-r}$ lorsque $\|r\| < 1$.

En substituant $r=-\epsilon$ et $n=2$ dans cette formule, on obtient :

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Donc, si $0 < \epsilon < 1$ :

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

Ce qui donne :

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

On en déduit que pour un petit $\epsilon$ positif, $\cfrac{1}{1 + \epsilon}$ peut être approximé par $1 - \epsilon$.

## Test des séries $p$ ($p$-Series Test)  
Pour un nombre réel positif $p$, une série de la forme suivante est appelée **série $p$** :

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Convergence/divergence des séries $p$**  
> La série $p$ $\sum \cfrac{1}{n^p}$ :
> - converge si $p>1$
> - diverge si $p\leq 1$
{: .prompt-info }

Dans le cas où $p=1$, la série $p$ devient la série harmonique, dont nous avons déjà montré la divergence.  
Pour $p=2$, le calcul de la valeur de $\sum \cfrac{1}{n^2}$ est connu sous le nom de "problème de Bâle (Basel problem)", du nom de la ville d'origine de la famille Bernoulli, qui a produit plusieurs mathématiciens célèbres sur plusieurs générations et qui a été la première à démontrer la convergence de cette série. La réponse à ce problème est $\cfrac{\pi^2}{6}$.

Plus généralement, la série $p$ pour $p>1$ est appelée **fonction zêta (zeta function)**. Elle a été introduite par Leonhard Euler en 11740 [HE](https://en.wikipedia.org/wiki/Holocene_calendar) et nommée plus tard par Riemann. C'est une fonction spéciale définie par :

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Ce sujet s'éloigne un peu de notre thème principal et, pour être franc, étant ingénieur et non mathématicien, je ne le maîtrise pas parfaitement. Je ne l'aborderai donc pas ici. Cependant, il est intéressant de noter que Leonhard Euler a montré que la fonction zêta peut également être exprimée sous forme d'un produit infini de nombres premiers, appelé **produit d'Euler (Euler Product)**. La fonction zêta occupe depuis une place centrale dans plusieurs domaines de la théorie analytique des nombres. La **fonction zêta de Riemann (Riemann zeta function)**, qui étend le domaine de définition aux nombres complexes, et la célèbre conjecture non résolue, l'**hypothèse de Riemann (Riemann hypothesis)**, en sont des exemples.

Pour revenir à notre sujet, la démonstration du test des séries $p$ nécessite le [test de comparaison](#test-de-comparaison) et le [test de l'intégrale](#test-de-lintégrale) que nous verrons plus loin. Cependant, la convergence/divergence des séries $p$ peut être utilisée efficacement avec les séries géométriques dans le [test de comparaison](#test-de-comparaison) que nous allons voir juste après, c'est pourquoi je l'ai intentionnellement placée ici.

### Démonstration
#### i) Lorsque $p>1$
L'intégrale :

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

converge, donc par le [test de l'intégrale](#test-de-lintégrale), la série $\sum \cfrac{1}{n^p}$ converge également.

#### ii) Lorsque $p\leq 1$
Dans ce cas :

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Comme nous savons que la série harmonique $\sum \cfrac{1}{n}$ diverge, par le [test de comparaison](#test-de-comparaison), $\sum \cfrac{1}{n^p}$ diverge également.

#### Conclusion
D'après i) et ii), la série $p$ $\sum \cfrac{1}{n^p}$ converge si $p>1$ et diverge si $p \leq 1$. $\blacksquare$

## Test de comparaison
Le **test de comparaison (Comparison Test)** de Jakob Bernoulli est utile pour déterminer la convergence ou la divergence des **séries à termes positifs (series of positive terms)**, c'est-à-dire des séries dont les termes généraux sont des nombres réels positifs ou nuls.

Une série à termes positifs $\sum a_n$ forme une suite croissante, donc si elle ne diverge pas vers l'infini ($\sum a_n = \infty$), elle converge nécessairement. Ainsi, dans le contexte des séries à termes positifs, l'expression :

$$ \sum a_n < \infty $$

signifie que <u>la série converge</u>.

> **Test de comparaison (Comparison Test)**  
> Si $0 \leq a_n \leq b_n$, alors :  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

En particulier, pour les séries à termes positifs comme $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, qui ont une forme similaire aux séries géométriques $\sum ar^{n-1}$ ou aux séries $p$ $\sum \cfrac{1}{n^p}$ que nous avons vues précédemment, il est recommandé d'essayer activement le test de comparaison.

Plusieurs autres tests de convergence/divergence que nous verrons par la suite peuvent tous être dérivés de ce **test de comparaison**, ce qui en fait l'un des tests les plus importants.

### Test de comparaison limite
Pour deux séries à termes positifs $\sum a_n$ et $\sum b_n$, si le rapport des termes généraux $a_n/b_n$ est tel que les termes dominants du numérateur et du dénominateur s'annulent, donnant $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (où }c\text{ est un nombre positif fini)}$, alors on peut utiliser le **test de comparaison limite (Limit Comparison Test)** si l'on connaît la convergence ou la divergence de la série $\sum b_n$.

> **Test de comparaison limite (Limit Comparison Test)**  
> Si :
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (où }c\text{ est un nombre positif fini)}$$
>
> alors les deux séries $\sum a_n$ et $\sum b_n$ convergent toutes les deux ou divergent toutes les deux. C'est-à-dire, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Test de la racine
> **Théorème**  
> Pour une série à termes positifs $\sum a_n$ et un nombre positif $\epsilon < 1$ :  
> - Si pour tout $n$, $\sqrt[n]{a_n}< 1-\epsilon$, alors la série $\sum a_n$ converge
> - Si pour tout $n$, $\sqrt[n]{a_n}> 1+\epsilon$, alors la série $\sum a_n$ diverge
{: .prompt-info }

> **Corollaire : Test de la racine (Root Test)**  
> Pour une série à termes positifs $\sum a_n$, si la limite :
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> existe, alors :
> - Si $r<1$, la série $\sum a_n$ converge
> - Si $r>1$, la série $\sum a_n$ diverge
{: .prompt-info }

> Dans le corollaire ci-dessus, si $r=1$, le test ne permet pas de déterminer la convergence ou la divergence, et il faut utiliser une autre méthode.
{: .prompt-warning }

## Test du rapport
> **Test du rapport (Ratio Test)**  
> Pour une suite de nombres positifs $(a_n)$ et $0 < r < 1$ :
> - Si pour tout $n$, $a_{n+1}/a_n \leq r$, alors la série $\sum a_n$ converge
> - Si pour tout $n$, $a_{n+1}/a_n \geq 1$, alors la série $\sum a_n$ diverge
{: .prompt-info }

> **Corollaire**  
> Pour une suite de nombres positifs $(a_n)$, si la limite $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ existe, alors :
> - Si $\rho < 1$, la série $\sum a_n$ converge
> - Si $\rho > 1$, la série $\sum a_n$ diverge
{: .prompt-info }

## Test de l'intégrale
Le calcul intégral peut être utilisé pour déterminer la convergence ou la divergence d'une série à termes positifs décroissants.

> **Test de l'intégrale (Integral Test)**  
> Si $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ est une fonction continue, décroissante et toujours positive, alors la série $\sum f(n)$ converge si et seulement si l'intégrale :
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> converge.
{: .prompt-info }

### Démonstration
Si la fonction $f(x)$ est continue, décroissante et toujours positive, alors l'inégalité :

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

est vérifiée. En additionnant cette inégalité de $n=1$ jusqu'au terme général, on obtient :

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

En appliquant le [test de comparaison](#test-de-comparaison), on obtient le résultat souhaité. $\blacksquare$

## Séries alternées
Une **série alternée (alternating series)** est une série $\sum a_n$ dont les termes $a_n$ sont non nuls et dont le signe de chaque terme est différent de celui du terme suivant $a_{n+1}$, c'est-à-dire que les termes positifs et négatifs apparaissent alternativement.

Pour les séries alternées, le théorème suivant, découvert par le mathématicien allemand Gottfried Wilhelm Leibniz, est très utile pour déterminer la convergence ou la divergence.

> **Test des séries alternées (Alternating Series Test)**  
> Si :
> 1. Pour tout $n$, $a_n$ et $a_{n+1}$ ont des signes opposés,
> 2. Pour tout $n$, $\|a_n\| \geq \|a_{n+1}\|$, et
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> alors la série alternée $\sum a_n$ converge.
{: .prompt-info }

## Convergence absolue
On dit qu'une série $\sum a_n$ **converge absolument (converge absolutely)** si la série $\sum \|a_n\|$ converge.

Le théorème suivant est alors vérifié :

> **Théorème**  
> Une série qui converge absolument converge.
{: .prompt-info }

> La réciproque de ce théorème n'est pas vraie.  
> Si une série converge mais ne converge pas absolument, on dit qu'elle **converge conditionnellement (converge conditionally)**.
{: .prompt-warning }

### Démonstration
Pour un nombre réel $a$, définissons :

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

Alors :

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Comme $0 \leq a^\pm \leq \|a\|$, par le [test de comparaison](#test-de-comparaison), si la série $\sum \|a_n\|$ converge, alors les séries $\sum a_n^+$ et $\sum a_n^-$ convergent également. Par conséquent, d'après les [propriétés fondamentales des séries convergentes](/posts/sequences-and-series/#propriétés-fondamentales-des-séries-convergentes) :

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

converge également. $\blacksquare$
