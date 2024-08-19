---
title: "Teorema da Adição Harmônica"
description: >-
  Aprenda como encontrar uma única função trigonométrica r sin(θ+α) ou r cos(θ-β) correspondente a uma soma de funções trigonométricas da forma f(θ) = a cos θ + b sin θ.
categories: [Matemática]
tags: [Trigonometria]
math: true
---

## TL;DR
> **Teorema da Adição Harmônica**
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \sin(\theta+\alpha) $$
>
> $$ (onde,\ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}) $$
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \cos(\theta-\beta) $$
>
> $$ (onde,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}) $$
{: .prompt-info }

## Pré-requisitos
- [Fórmulas de adição trigonométrica](/posts/trigonometric-addition-formulas)

## Teorema da Adição Harmônica
Para uma função f(θ) na forma de uma soma de funções trigonométricas, como f(θ) = a cos θ + b sin θ, sempre existem números reais α e β que satisfazem f(θ)=√(a²+b²) sin(θ+α) = √(a²+b²) cos(θ-β).

![Derivação Geométrica do Teorema da Adição Harmônica](/assets/img/trigonometry/harmonic-addition.png)

Como mostrado na figura, se tomarmos um ponto P(a,b) no plano coordenado e chamarmos de α o ângulo formado entre o segmento OP e a direção positiva do eixo x, temos:

$$ \overline{OP} = \sqrt{a^2+b^2} $$

e

$$ \cos \alpha = \frac{a}{\sqrt{a^{2} + b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2} + b^{2}}} \tag{1} $$

Então,

$$ \begin{align*}
a \sin \theta + b \cos \theta &= \sqrt{a^{2}+b^{2}} \left(\frac{a}{\sqrt{a^{2}+b^{2}}}\sin \theta + \frac{b}{\sqrt{a^{2}+b^{2}}}\cos \theta \right) \\
&= \sqrt{a^{2}+b^{2}}(\cos \alpha \sin \theta + \sin \alpha \cos \theta) \\
&= \sqrt{a^{2}+b^{2}} \sin(\theta + \alpha). \tag{2}
\end{align*} $$

Da mesma forma, se tomarmos um ponto P'(b,a) e chamarmos de β o ângulo formado entre o segmento OP e a direção positiva do eixo x, obtemos:

$$ a \sin \theta + b \cos \theta = \sqrt{a^{2}+b^{2}}\cos(\theta-\beta). \tag{3} $$

$$ onde,\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}. $$

A transformação de uma função trigonométrica da forma a sin θ + b sin θ em r sin(θ+α) ou r cos(θ-β) é chamada de Adição Harmônica.

## Exemplo
Dada a função f(θ)=-√3 sin θ + cos(θ - π/3), encontre os valores máximo e mínimo da função f(θ) no intervalo [0, 2π].

### 1. Transformar para a forma a sin θ + b cos θ
Usando as [fórmulas de adição trigonométrica](/posts/trigonometric-addition-formulas), transformamos a função dada:

$$ \begin{align*}
f(\theta) &= -\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right) \\
&= -\sqrt{3}\sin \theta + \left( \cos\theta \cos\frac{\pi}{3} + \sin\theta \sin\frac{\pi}{3} \right) \\
&= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta .
\end{align*} $$

### 2. Transformar para a forma r sin(θ+α)
Fazendo a=-√3/2 e b=1/2, temos:

$$ r = \sqrt{a^2+b^2} = \sqrt{\frac{3}{4}+\frac{1}{4}} = 1 $$

Além disso, existe um único valor real α tal que 0 ≤ α < 2π, cos α = a e sin α = b. A partir dos valores trigonométricos para ângulos especiais, podemos determinar que α = 5π/6.

Portanto, transformando a função dada f(θ) para a forma r sin(θ+α), obtemos:

$$ f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right). $$

### 3. Encontrar os valores máximo e mínimo no intervalo dado
![Gráfico da função dada](/assets/img/trigonometry/harmonic-addition-ex-graph.png)

A função f(θ) = sin(θ + 5π/6) é uma função periódica com período 2π, e no intervalo dado, ela tem um valor máximo de 1 e um valor mínimo de -1.

$$ \therefore M=1,\ m=-1$$