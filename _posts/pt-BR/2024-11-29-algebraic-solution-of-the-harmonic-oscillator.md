---
title: Solução algébrica do Oscilador Harmônico (The Harmonic Oscillator)
description: Estabelecemos a equação de Schrödinger para o oscilador harmônico na
  mecânica quântica e examinamos o método de solução algébrica para essa equação.
  Obtemos a função de onda e os níveis de energia para qualquer estado estacionário
  a partir dos comutadores, relações de comutação canônicas e operadores escada.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.png
---
## TL;DR
> - Qualquer oscilação pode ser aproximada como uma oscilação harmônica simples se a amplitude for suficientemente pequena, o que torna a oscilação harmônica simples importante na física
> - Oscilador harmônico: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Comutador (commutator)**:
>   - Operação binária que indica o quanto dois operadores não comutam
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Relação de comutação canônica (canonical commutation relation)**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Operadores escada (ladder operators)**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ é chamado de **operador de criação (raising operator)**, $\hat{a}\_-$ é chamado de **operador de aniquilação (lowering operator)**
>   - Podem aumentar ou diminuir o nível de energia para qualquer estado estacionário, permitindo encontrar todas as outras soluções da equação de Schrödinger independente do tempo uma vez que uma solução é encontrada
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Função de onda e níveis de energia do $n$-ésimo estado estacionário:
>   - Estado fundamental ($0$-ésimo estado estacionário):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$-ésimo estado estacionário:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ é o **conjugado hermitiano (hermitian conjugate)** e o **operador adjunto (adjoint operator)** de $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - A partir disso, podemos derivar as seguintes propriedades:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Método para calcular o valor esperado de quantidades físicas que incluem potências de $\hat{x}$ e $\hat{p}$:
>   1. Expressar $\hat{x}$ e $\hat{p}$ em termos dos operadores de criação e aniquilação usando a definição dos operadores escada
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. Expressar a quantidade física cujo valor esperado se deseja calcular usando as expressões acima para $\hat{x}$ e $\hat{p}$
>   3. Usar o fato de que $\left(\hat{a}\_\pm \right)^m$ é proporcional a $\psi\_{n\pm m}$ e, portanto, ortogonal a $\psi_n$, resultando em $0$
>   4. Calcular a integral usando as propriedades dos operadores escada
{: .prompt-info }

## Pré-requisitos
- [Método de separação de variáveis](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Equação de Schrödinger e função de onda](/posts/schrodinger-equation-and-the-wave-function/)
- [Teorema de Ehrenfest](/posts/ehrenfest-theorem/)
- [Equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/)
- [Poço quadrado infinito unidimensional](/posts/the-infinite-square-well/)
- Conjugado hermitiano (hermitian conjugate), operador adjunto (adjoint operator)

## Configuração do modelo
### Oscilador harmônico na mecânica clássica
Um exemplo típico de oscilador harmônico clássico é o movimento de uma massa $m$ pendurada em uma mola com constante elástica $k$ (ignorando o atrito).
Este movimento segue a **Lei de Hooke**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

A solução desta equação é

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

onde

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

é a frequência angular da oscilação. A energia potencial em função da posição $x$ tem a forma parabólica

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

Na realidade, não existem osciladores harmônicos perfeitos. Mesmo no caso da mola que usamos como exemplo, se puxarmos a mola além do seu limite elástico, ela se romperá ou sofrerá deformação permanente, e na verdade, mesmo antes de chegar a esse ponto, ela já não segue exatamente a Lei de Hooke. No entanto, a razão pela qual o oscilador harmônico é importante na física é que qualquer potencial arbitrário pode ser aproximado por uma forma parabólica perto de um mínimo local. Se expandirmos um potencial arbitrário $V(x)$ em série de Taylor próximo a um mínimo local, obtemos

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Agora, como adicionar uma constante arbitrária a $V(x)$ não afeta a força de forma alguma, podemos subtrair $V(x_0)$ aqui, e usando o fato de que $V^\prime(x_0)=0$ porque $x_0$ é um mínimo, e ignorando os termos de ordem superior assumindo que $(x-x_0)$ é suficientemente pequeno, obtemos

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

Isso coincide com o movimento de um oscilador harmônico com constante elástica efetiva $k=V^{\prime\prime}(x_0)$ próximo ao ponto $x_0$\*. Em outras palavras, qualquer oscilação pode ser aproximada como uma oscilação harmônica simples (simple harmonic oscillation) se a amplitude for suficientemente pequena.

> \* Assumimos que $V(x)$ tem um mínimo em $x_0$, portanto, $V^{\prime\prime}(x_0) \geq 0$ aqui. Em casos muito raros, pode ocorrer $V^{\prime\prime}(x_0)=0$, e tais movimentos não podem ser aproximados como oscilações harmônicas simples.
{: .prompt-info }

### Oscilador harmônico na mecânica quântica
O problema do oscilador harmônico quântico consiste em resolver a equação de Schrödinger para o potencial

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

A [equação de Schrödinger independente do tempo](/posts/time-independent-schrodinger-equation/) para o oscilador harmônico é

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

Existem duas abordagens completamente diferentes para resolver este problema. Uma é o método analítico usando **séries de potências (power series method)**, e a outra é o método algébrico usando **operadores escada (ladder operators)**. O método algébrico é mais rápido e simples, mas também é necessário estudar a solução analítica usando séries de potências. Aqui, abordaremos o método de solução algébrica, e para o método de solução analítica, consulte [este artigo](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Comutadores e relação de comutação canônica
Podemos reescrever a equação ($\ref{eqn:t_independent_schrodinger_eqn}$) usando o operador de momento $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$ da seguinte forma:

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Agora, vamos fatorar o Hamiltoniano (Hamiltonian)

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

Se $p$ e $x$ fossem números, poderíamos facilmente fatorar como

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

mas aqui $\hat{p}$ e $\hat{x}$ são operadores, e geralmente a **propriedade comutativa (commutative property)** não se aplica a operadores ($\hat{p}\hat{x}\neq \hat{x}\hat{p}$), então não é tão simples. No entanto, isso ainda pode servir como um ponto de referência, então vamos começar examinando a seguinte quantidade:

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

Para os operadores $\hat{a}_\pm$ definidos acima, $\hat{a}\_-\hat{a}\_+$ é

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Aqui, o termo $(\hat{x}\hat{p}-\hat{p}\hat{x})$ é chamado de **comutador (commutator)** de $\hat{x}$ e $\hat{p}$, e indica o quanto os dois operadores não comutam. Geralmente, o comutador de dois operadores $\hat{A}$ e $\hat{B}$ é representado usando colchetes da seguinte forma:

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

Usando essa notação, podemos reescrever a equação ($\ref{eqn:a_m_times_a_p_without_commutator}$) como:

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Agora precisamos descobrir o comutador de $\hat{x}$ e $\hat{p}$.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

e removendo a função de teste $f(x)$, obtemos:

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

Isso é chamado de **relação de comutação canônica (canonical commutation relation)**.

## Operadores escada (ladder operators)
Pela relação de comutação canônica, a equação ($\ref{eqn:a_m_times_a_p}$) se torna

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

ou seja,

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Aqui, a ordem de $\hat{a_-}$ e $\hat{a_+}$ é importante; se colocarmos $\hat{a_+}$ à esquerda, temos

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

e satisfaz

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

Neste caso, o Hamiltoniano também pode ser escrito como

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Portanto, a equação de Schrödinger independente do tempo ($\hat{H}\psi=E\psi$) expressa em termos de $\hat{a}_\pm$ é

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(sinais superiores e inferiores correspondentes).

Agora podemos descobrir a seguinte propriedade importante:

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Prova:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> Da mesma forma,
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Portanto, se pudermos encontrar uma solução da equação de Schrödinger independente do tempo, podemos encontrar todas as outras soluções. Como podemos aumentar ou diminuir o nível de energia para qualquer estado estacionário, $\hat{a}\_\pm$ são chamados de **operadores escada (ladder operators)**, onde $\hat{a}\_+$ é o **operador de criação (raising operator)** e $\hat{a}\_-$ é o **operador de aniquilação (lowering operator)**.

## Estados estacionários do oscilador harmônico
### Estados estacionários $\psi_n$ e níveis de energia $E_n$
Se continuarmos aplicando o operador de aniquilação, eventualmente obteremos um estado de energia menor que 0, que não pode existir fisicamente. Matematicamente, se $\psi$ é uma solução da equação de Schrödinger, $\hat{a}_-\psi$ também é uma solução da equação de Schrödinger, mas não há garantia de que essa nova solução seja sempre normalizada (ou seja, um estado fisicamente possível). Continuando a aplicar o operador de aniquilação, eventualmente obteremos a solução trivial $\psi=0$.

Portanto, para os estados estacionários $\psi$ do oscilador harmônico, existe um "nível mais baixo" $\psi_0$ que satisfaz

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

(não existe um nível de energia mais baixo). Este $\psi_0$ satisfaz

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

portanto,

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

Esta é uma [equação diferencial ordinária separável](/posts/Separation-of-Variables/), que pode ser facilmente resolvida da seguinte forma:

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

Além disso, esta função pode ser normalizada da seguinte forma:

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Aqui, $A^2 = \sqrt{m\omega / \pi\hbar}$, portanto

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Agora, substituindo esta solução na equação de Schrödinger ($\ref{eqn:schrodinger_eqn_with_ladder}$) que encontramos anteriormente e usando o fato de que $\hat{a}_-\psi_0=0$, obtemos:

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

Começando com este **estado fundamental (ground state)** e continuando a aplicar o operador de criação, podemos obter estados excitados (excited states) onde a energia aumenta em $\hbar\omega$ cada vez que o operador de criação é aplicado.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

Aqui, $A_n$ é a constante de normalização. Dessa forma, podemos determinar todos os estados estacionários e níveis de energia permitidos do oscilador harmônico aplicando o operador de criação após encontrar o estado fundamental.

### Normalização
A constante de normalização também pode ser determinada algebricamente. Sabemos que $\hat{a}\_{\pm}\psi_n$ é proporcional a $\psi\_{n\pm 1}$, então podemos escrever

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Agora, observe que para quaisquer funções $f(x)$ e $g(x)$ integráveis, a seguinte relação é válida:

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ é o **conjugado hermitiano (hermitian conjugate)** e o **operador adjunto (adjoint operator)** de $\hat{a}\_\pm$.

> **Prova:**
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

Portanto, fazendo $f=\hat{a}_\pm \psi_n$, $g=\psi_n$, temos

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Então, das equações ($\ref{eqn:schrodinger_eqn_with_ladder}$) e ($\ref{eqn:psi_n_and_E_n}$),

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

Portanto, das equações ($\ref{eqn:norm_const}$) e ($\ref{eqn:norm_const_2}$), obtemos:

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

E como $\psi_n$ e $\psi_{n\pm1}$ são todos normalizados, temos $\|c_n\|^2=n+1,\ \|d_n\|^2=n$, e portanto

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

A partir disso, podemos obter qualquer estado estacionário normalizado $\psi_n$ da seguinte forma:

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

Ou seja, na equação ($\ref{eqn:psi_n_and_E_n}$), a constante de normalização é $A_n=\cfrac{1}{\sqrt{n!}}$.

### Ortogonalidade dos estados estacionários
Assim como no [poço quadrado infinito unidimensional](/posts/the-infinite-square-well/#3-esses-estados-possuem-ortogonalidade), os estados estacionários do oscilador harmônico são ortogonais.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Prova
Podemos provar isso usando as equações ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$) e ($\ref{eqn:norm_const_3}$) que mostramos anteriormente. Na equação ($\ref{eqn:hermitian_conjugate}$), colocamos $f=\hat{a}_-\psi_m,\ g=\psi_n$ e usamos o fato de que

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

Usando a ortogonalidade, podemos [como fizemos na equação (19) do poço quadrado infinito unidimensional](/posts/the-infinite-square-well/#encontrando-a-solu%C3%A7%C3%A3o-geral-psixt-da-equa%C3%A7%C3%A3o-de-schr%C3%B6dinger-dependente-do-tempo), expandir $\Psi(x,0)$ como uma combinação linear de estados estacionários $\sum c_n\psi_n(x)$ e encontrar os coeficientes $c_n$ usando o [método de Fourier](/posts/the-infinite-square-well/#encontrando-os-coeficientes-c_n-usando-o-m%C3%A9todo-de-fourier).

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Aqui também, $\|c_n\|^2$ é a probabilidade de obter o valor $E_n$ ao medir a energia.

## Valor esperado da energia potencial $\langle V \rangle$ em qualquer estado estacionário $\psi_n$
Para encontrar $\langle V \rangle$, precisamos calcular a seguinte integral:

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

O seguinte método é útil para calcular integrais deste tipo que incluem potências de $\hat{x}$ e $\hat{p}$.

Primeiro, usamos a definição dos operadores de escada na equação ($\ref{eqn:ladder_operators}$) para expressar $\hat{x}$ e $\hat{p}$ em termos dos operadores de criação e aniquilação.

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Agora, expressamos a quantidade física cujo valor esperado queremos calcular usando as expressões acima para $\hat{x}$ e $\hat{p}$. Aqui, estamos interessados em $x^2$, então podemos expressá-lo como:

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

A partir disso, obtemos:

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

E aqui, como $\left(\hat{a}\_\pm \right)^2$ é proporcional a $\psi\_{n\pm2}$, é ortogonal a $\psi\_n$, e portanto os dois termos $\left(\hat{a}\_+ \right)^2$ e $\left(\hat{a}\_- \right)^2$ se tornam 0. Finalmente, usando a equação ($\ref{eqn:norm_const_2}$) para calcular os dois termos restantes, obtemos

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

Referindo-se à equação ($\ref{eqn:psi_n_and_E_n}$), podemos ver que o valor esperado da energia potencial é exatamente metade da energia total, e a outra metade é, naturalmente, a energia cinética $T$. Esta é uma característica única do oscilador harmônico.
