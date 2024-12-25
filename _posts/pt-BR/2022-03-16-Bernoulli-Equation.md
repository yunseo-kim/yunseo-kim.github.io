---
title: Equação de Bernoulli (Bernoulli Equation)
description: Exploramos a equação de Bernoulli e o método de resolução da equação
  logística, uma forma especial da equação de Bernoulli.
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## Equação de Bernoulli (Bernoulli Equation)

$$ y'+p(x)y=g(x)y^a\quad \text{(}a\text{ é um número real arbitrário)}  \tag{1} $$

A equação de Bernoulli (1) é linear se $a=0$ ou $a=1$, e não linear nos outros casos. No entanto, pode ser transformada em linear através do seguinte processo.

Definindo $$ u(x)=[y(x)]^{1-a} $$

e diferenciando, então substituindo $y'$ da equação (1), obtemos:

$$ \begin{align*}
u'&=(1-a)y^{-a}y'
\\&=(1-a)y^{-a}(gy^a-py) 
\\&=(1-a)(g-py^{1-a})
\end{align*} $$

No lado direito, $y^{1-a}=u$, então obtemos a seguinte equação diferencial ordinária linear:

$$ u'+(1-a)pu=(1-a)g \tag{2} $$

## Exemplo: Equação Logística (Logistic Equation)
Resolva a equação logística (uma forma especial da equação de Bernoulli).

$$ y'=Ay-By^2 \tag{3} $$

### Solução
Escrevendo a equação (3) na forma da equação (1):

$$ y'-Ay=-By^2 $$

Aqui, $a=2$, então $u=y^{1-a}=y^{-1}$. Diferenciando este u e substituindo $y'$ da equação (3):

$$ u'=-y^{-2}y'=-y^{-2}(Ay-By^2)=B-Ay^{-1} $$

O último termo é $-Ay^{-1}=-Au$, então obtemos a seguinte equação diferencial ordinária linear:

$$ u'+Au=B $$

Pela fórmula de solução para [equações diferenciais ordinárias lineares não homogêneas](/posts/Solution-of-First-Order-Linear-ODE/#equação-diferencial-ordinária-linear-não-homogênea), podemos obter a seguinte solução geral:

$$ u=ce^{-At}+B/A $$

Como $u=1/y$, a partir disso obtemos a solução geral da equação (3):

$$ y=\frac{1}{u}=\frac{1}{ce^{-At}+B/A} \tag{4}$$
