---
title: Équation de Bernoulli
description: Nous examinons l'équation de Bernoulli et la méthode de résolution de
  l'équation logistique, qui est une forme spéciale de l'équation de Bernoulli.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## Équation de Bernoulli

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ est un nombre réel quelconque)}  \tag{1} $$

L'équation de Bernoulli (1) est linéaire si $a=0$ ou $a=1$, et non linéaire dans les autres cas. Cependant, elle peut être transformée en une équation linéaire par le processus suivant.

Posons $$ u(x)=[y(x)]^{1-a} $$

et différencions, puis substituons $y'$ de l'équation (1) pour obtenir

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

Dans le membre de droite, $y^{1-a}=u$, donc nous obtenons l'équation différentielle linéaire suivante :

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Exemple : Équation logistique
Résolvez l'équation logistique (une forme spéciale de l'équation de Bernoulli).

$$ y'=Ay-By^2 \tag{3} $$

### Solution
Si nous écrivons l'équation (3) sous la forme de l'équation (1), nous obtenons

$$ y'-Ay=-By^2 $$

Ici, $a=2$, donc $u=y^{1-a}=y^{-1}$. Si nous différencions ce u et substituons $y'$ de l'équation (3), nous obtenons

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

Le dernier terme est $-Ay^{-1}=-Au$, donc nous obtenons l'équation différentielle linéaire suivante :

$$ u'+Au=B $$

Selon la formule de solution pour [l'équation différentielle linéaire non homogène](/posts/Solution-of-First-Order-Linear-ODE/#équation-différentielle-ordinaire-linéaire-non-homogène), nous pouvons obtenir la solution générale suivante :

$$ u=ce^{-At}+B/A $$

Comme $u=1/y$, nous obtenons de là la solution générale de l'équation (3)

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$
