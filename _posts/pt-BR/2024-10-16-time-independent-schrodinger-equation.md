---
title: "Equação de Schrödinger independente do tempo (Time-independent Schrödinger Equation)"
description: >-
  Derivamos a equação de Schrödinger independente do tempo ψ(x) aplicando o método de separação de variáveis
  à forma original da equação de Schrödinger (equação de Schrödinger dependente do tempo) Ψ(x,t).
  Examinamos o significado e a importância matemática e física da solução separada obtida desta forma.
  Também exploramos o método de obter a solução geral da equação de Schrödinger através da combinação linear de soluções separadas.
categories: [Engineering Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
---

## TL;DR
> - Solução separada: $ \Psi(x,t) = \psi(x)\phi(t)$
> - Dependência temporal ("fator de oscilação"): $ \phi(t) = e^{-iEt/\hbar} $
> - Operador Hamiltoniano: $ \hat H = -\cfrac{h^2}{2m}\cfrac{\partial^2}{\partial x^2} + V(x) $
> - Equação de Schrödinger independente do tempo: $ \hat H\psi = E\psi $
> - Significado físico e matemático e importância da solução separada:
>   1. Estados estacionários
>   2. Possui um valor de energia total claro $E$
>   3. A solução geral da equação de Schrödinger é uma combinação linear de soluções separadas
> - Solução geral da equação de Schrödinger dependente do tempo: $\Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)\phi_n(t) = \sum_{n=1}^\infty c_n\Psi_n(x,t)$
{: .prompt-info }

## Pré-requisitos
- Distribuição de probabilidade contínua e densidade de probabilidade
- [Equação de Schrödinger e função de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Teorema de Ehrenfest](/posts/ehrenfest-theorem/)
- [Método de separação de variáveis](/posts/separation-of-variables/)

## Derivação usando o método de separação de variáveis
No [post sobre o teorema de Ehrenfest](/posts/ehrenfest-theorem/), vimos como calcular várias quantidades físicas usando a função de onda $\Psi$. Então, o importante é como obter essa função de onda $\Psi(x,t)$, e geralmente é necessário resolver a [equação de Schrödinger](/posts/schrodinger-equation-and-the-wave-function/), que é uma equação diferencial parcial em relação à posição $x$ e ao tempo $t$ para um dado potencial $V(x,t)$.

$$ i\hbar \frac{\partial \Psi}{\partial t} = - \frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi. \label{eqn:schrodinger_eqn}\tag{1}$$

Se o potencial $V$ for independente do tempo $t$, podemos resolver a equação de Schrödinger acima usando o [método de separação de variáveis](/posts/Separation-of-Variables/). Vamos considerar uma solução na forma do produto de uma função $\psi$ apenas de $x$ e uma função $\phi$ apenas de $t$:

$$ \Psi(x,t) = \psi(x)\phi(t). \tag{2}$$

À primeira vista, isso pode parecer uma expressão excessivamente restritiva e capaz de encontrar apenas um pequeno subconjunto da solução completa, mas na verdade, a solução obtida dessa forma tem um significado importante, e podemos obter a solução geral somando essas soluções separáveis de uma maneira específica.

Para a solução separável,

$$ \frac{\partial \Psi}{\partial t}=\psi\frac{d\phi}{dt},\quad \frac{\partial^2 \Psi}{\partial x^2}=\frac{d^2\psi}{dx^2}\phi \tag{3} $$

Substituindo isso na equação ($\ref{eqn:schrodinger_eqn}$), podemos escrever a equação de Schrödinger como:

$$ i\hbar\psi\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2}\phi + V\psi\phi. \tag{4}$$

Dividindo ambos os lados por $\psi\phi$, obtemos

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = -\frac{\hbar^2}{2m}\frac{1}{\psi}\frac{d^2\psi}{dx^2} + V \tag{5}$$

onde o lado esquerdo é uma função apenas de $t$ e o lado direito é uma função apenas de $x$.

Para que esta equação tenha uma solução, ambos os lados devem ser iguais a uma constante, que chamaremos de $E$:

$$ i\hbar\frac{1}{\phi}\frac{d\phi}{dt} = E. \tag{6}$$

Isso nos dá duas equações diferenciais ordinárias, uma para a parte temporal:

$$ \frac{d\phi}{dt} = -\frac{iE}{\hbar}\phi \label{eqn:ode_t}\tag{7}$$

e outra para a parte espacial:

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{8}$$

A equação diferencial ordinária ($\ref{eqn:ode_t}$) para $t$ pode ser facilmente resolvida. A solução geral é $ce^{-iEt/\hbar}$, mas como estamos interessados no produto $\psi\phi$ e não em $\phi$ por si só, podemos incluir a constante $c$ em $\psi$. Assim, obtemos:

$$ \phi(t) = e^{-iEt/\hbar} \tag{9}$$

A equação diferencial ordinária ($\ref{eqn:t_independent_schrodinger_eqn}$) para $x$ é chamada de **equação de Schrödinger independente do tempo**. Para resolver esta equação, precisamos conhecer o potencial $V(x)$.

## Significado físico e matemático
Anteriormente, usando o método de separação de variáveis, obtivemos a função $\phi(t)$ apenas do tempo e a equação de Schrödinger independente do tempo ($\ref{eqn:t_independent_schrodinger_eqn}$). Embora a maioria das soluções da **equação de Schrödinger dependente do tempo** original ($\ref{eqn:schrodinger_eqn}$) não possa ser expressa na forma $\psi(x)\phi(t)$, a forma da equação de Schrödinger independente do tempo ainda é importante devido às seguintes três propriedades de sua solução:

### 1. São estados estacionários.
Embora a própria função de onda

$$ \Psi(x,t)=\psi(x)e^{-iEt/\hbar} \label{eqn:separation_of_variables}\tag{10}$$

dependa de $t$, a densidade de probabilidade

$$ \begin{align*}
|\Psi(x,t)|^2 &= \Psi^*\Psi \\
&= \psi^*e^{iEt/\hbar}\psi e^{-iEt/\hbar} \\
&= |\psi(x)|^2 
\end{align*} \tag{11}$$

é constante e independente do tempo, pois a dependência temporal se cancela.

> Para soluções normalizáveis, a constante de separação $E$ deve ser real.
>
> Se considerarmos $E$ na equação ($\ref{eqn:separation_of_variables}$) como um número complexo $E_0+i\Gamma$ (onde $E_0$ e $\Gamma$ são reais),
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
> Como vimos anteriormente em [Equação de Schrödinger e função de onda](/posts/schrodinger-equation-and-the-wave-function/#normalização-da-função-de-onda), $\int_{-\infty}^{\infty}\|\Psi\|^2dx$ deve ser uma constante independente do tempo, portanto $\Gamma=0$. $\blacksquare$
{: .prompt-info }

O mesmo acontece ao calcular o valor esperado de qualquer quantidade física, e a equação (8) do [teorema de Ehrenfest](/posts/ehrenfest-theorem/) se torna:

$$ \langle Q(x,p) \rangle = \int \psi^*[Q(x, -i\hbar\nabla)]\psi dx \tag{12}$$

Portanto, todos os valores esperados são constantes em relação ao tempo. Em particular, como $\langle x \rangle$ é constante, $\langle p \rangle=0$.

### 2. É um estado com um valor de energia total claro $E$, não uma distribuição de probabilidade com um intervalo.
Na mecânica clássica, a energia total (energia cinética e energia potencial) é chamada de **Hamiltoniano** e é definida como:

$$ H(x,p)=\frac{p^2}{2m}+V(x) \tag{13}$$

Portanto, substituindo $p$ por $-i\hbar(\partial/\partial x)$, o operador Hamiltoniano na mecânica quântica corresponde a:

$$ \hat H = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x) \label{eqn:hamiltonian_op}\tag{14}$$

Assim, a equação de Schrödinger independente do tempo ($\ref{eqn:t_independent_schrodinger_eqn}$) pode ser escrita como:

$$ \hat H \psi = E\psi \tag{15}$$

e o valor esperado do Hamiltoniano é:

$$ \langle H \rangle = \int \psi^* \hat H \psi dx = E\int|\psi|^2dx = E\int|\Psi|^2dx = E. \tag{16}$$

Além disso,

$$ {\hat H}^2\psi = \hat H(\hat H\psi) = \hat H(E\psi) = E(\hat H\psi) = E^2\psi \tag{17}$$

então

$$ \langle H^2 \rangle = \int \psi^*{\hat H}^2\psi dx = E^2\int|\psi|^2dx = E^2 \tag{18}$$

Portanto, a variância do Hamiltoniano $H$ é:

$$ \sigma_H^2 = \langle H^2 \rangle - {\langle H \rangle}^2 = E^2 - E^2 = 0 \tag{19}$$

Ou seja, a solução separada sempre mede um valor constante $E$ quando a energia total é medida.

### 3. A solução geral da equação de Schrödinger dependente do tempo é uma combinação linear de soluções separadas.

A equação de Schrödinger independente do tempo ($\ref{eqn:t_independent_schrodinger_eqn}$) tem infinitas soluções $[\psi_1(x),\psi_2(x),\psi_3(x),\dots]$. Vamos chamá-las de \{$\psi_n(x)$\}. Para cada uma delas, existe uma constante de separação $E_1,E_2,E_3,\dots=$\{$E_n$\}, então para cada **nível de energia possível**, há uma função de onda correspondente.

$$ \Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar},\quad \Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar},\ \dots \tag{20}$$

A equação de Schrödinger dependente do tempo ($\ref{eqn:schrodinger_eqn}$) tem a propriedade de que a combinação linear de quaisquer duas soluções também é uma solução, então uma vez que encontramos as soluções separadas, podemos imediatamente obter uma forma mais geral de solução:

$$ \Psi(x,t) = \sum_{n=1}^\infty c_n\psi_n(x)e^{-iE_nt/\hbar} = \sum_{n=1}^\infty c_n\Psi_n(x,t) \label{eqn:general_solution}\tag{21}$$

Todas as soluções da equação de Schrödinger dependente do tempo podem ser escritas na forma acima, e agora a única tarefa restante é encontrar as constantes apropriadas $c_1, c_2, \dots$ para satisfazer as condições iniciais dadas no problema e encontrar a solução particular desejada. Em outras palavras, uma vez que podemos resolver a equação de Schrödinger independente do tempo, encontrar a solução geral da equação de Schrödinger dependente do tempo se torna simples.

> Note que enquanto a solução separada 
>
> $$ \Psi_n(x,t) = \psi_n(x)e^{-iEt/\hbar} $$
>
> é um estado estacionário onde todas as probabilidades e valores esperados são independentes do tempo, a solução geral na equação ($\ref{eqn:general_solution}$) não possui essa propriedade.
{: .prompt-warning }

## Conservação de energia
Na solução geral ($\ref{eqn:general_solution}$), o quadrado do valor absoluto dos coeficientes \{$c_n$\}, $\|c_n\|^2$, representa fisicamente a probabilidade de medir o valor de energia $E_n$ quando a energia de uma partícula no estado $\Psi$ é medida. Portanto, a soma dessas probabilidades deve ser

$$ \sum_{n=1}^\infty |c_n|^2=1 \tag{22}$$

e o valor esperado do Hamiltoniano é

$$ \langle H \rangle = \sum_{n=1}^\infty |c_n|^2E_n \tag{23}$$

Como os níveis de energia $E_n$ de cada estado estacionário e os coeficientes \{$c_n$\} são independentes do tempo, a probabilidade de medir uma energia específica $E_n$ e o valor esperado do Hamiltoniano $H$ também permanecem constantes, independentes do tempo.
