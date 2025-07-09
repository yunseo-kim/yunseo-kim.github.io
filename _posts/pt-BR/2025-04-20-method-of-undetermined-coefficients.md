---
title: "Método dos Coeficientes a Determinar"
description: "Vamos explorar o método dos coeficientes a determinar, uma solução útil e frequentemente usada em engenharia para resolver problemas de valor inicial para EDOs lineares não homogêneas com coeficientes constantes e termos de entrada específicos, como em sistemas de vibração e circuitos RLC."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **O método dos coeficientes a determinar se aplica a:**
>   - EDOs com **coeficientes constantes $a$ e $b$**
>   - cujo termo de entrada $r(x)$ é uma função exponencial, uma potência de $x$, $\cos$ ou $\sin$, ou somas e produtos dessas funções
>   - EDOs lineares da forma $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Regras de Escolha para o Método dos Coeficientes a Determinar**  
>   - **(a) Regra Básica**: Se $r(x)$ na Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha e determine seus coeficientes substituindo $y_p$ e suas derivadas na Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regra de Modificação**: Se um termo em sua escolha para $y_p$ for uma solução da EDO homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da EDO homogênea).  
>   - **(c) Regra da Soma**: Se $r(x)$ for uma soma de funções listadas na primeira coluna da tabela, então escolha para $y_p$ a soma das funções nas linhas correspondentes da segunda coluna.
>
> | Termo em $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Pré-requisitos
- [EDOs Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [EDOs Lineares Homogêneas com Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [Equação de Euler-Cauchy](/posts/euler-cauchy-equation/)
- [Wronskiano, Existência e Unicidade de Soluções](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [EDOs Lineares Não Homogêneas de Segunda Ordem](/posts/nonhomogeneous-linear-odes-of-second-order/)
- Espaços vetoriais, combinação linear (álgebra linear)

## O Método dos Coeficientes a Determinar
Considere a equação diferencial ordinária linear não homogênea de segunda ordem com $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

e a EDO homogênea correspondente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Como vimos anteriormente em [EDOs Lineares Não Homogêneas de Segunda Ordem](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver um problema de valor inicial para a EDO linear não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$), precisamos primeiro resolver a EDO homogênea ($\ref{eqn:homogeneous_linear_ode}$) para encontrar $y_h$, e depois encontrar uma solução particular $y_p$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) para obter a solução geral

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Então, como podemos encontrar $y_p$? Um método geral para encontrar $y_p$ é o **método da variação de parâmetros**, mas em alguns casos, um método muito mais simples, o **método dos coeficientes a determinar**, pode ser aplicado. É um método frequentemente usado em engenharia, especialmente aplicável a modelos de sistemas de vibração e circuitos elétricos RLC.

O método dos coeficientes a determinar é adequado para equações diferenciais ordinárias lineares com **coeficientes constantes $a$ e $b$**, e cujo termo de entrada $r(x)$ consiste em funções exponenciais, potências de $x$, $\cos$ ou $\sin$, ou somas e produtos de tais funções:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

A chave para o método dos coeficientes a determinar é que $r(x)$ dessa forma tem derivadas que são semelhantes a si mesma. Para aplicar o método, escolhemos uma $y_p$ que tenha uma forma semelhante a $r(x)$, mas com coeficientes desconhecidos que são determinados substituindo $y_p$ e suas derivadas na EDO dada. As regras para escolher uma $y_p$ apropriada para formas de $r(x)$ que são importantes na prática da engenharia são as seguintes.

> **Regras de Escolha para o Método dos Coeficientes a Determinar**  
> **(a) Regra Básica**: Se $r(x)$ na Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha e determine seus coeficientes substituindo $y_p$ e suas derivadas na Eq. ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regra de Modificação**: Se um termo em sua escolha para $y_p$ for uma solução da EDO homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da EDO homogênea).  
> **(c) Regra da Soma**: Se $r(x)$ for uma soma de funções listadas na primeira coluna da tabela, então escolha para $y_p$ a soma das funções nas linhas correspondentes da segunda coluna.
>
> | Termo em $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método tem a vantagem de não ser apenas simples, mas também autocorretivo. Se você escolher a $y_p$ errada ou com poucos termos, chegará a uma contradição. Se escolher termos demais, os coeficientes dos termos desnecessários se tornarão $0$, levando ao resultado correto. Mesmo que algo dê errado ao aplicar o método dos coeficientes a determinar, você naturalmente perceberá isso durante o processo de solução. Portanto, se você escolheu uma $y_p$ razoavelmente apropriada de acordo com as regras de escolha acima, pode tentar sem hesitação.

### Prova da Regra da Soma
Considere a EDO linear não homogênea da forma $r(x) = r_1(x) + r_2(x)$

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Agora, suponha que as duas equações a seguir, com o mesmo lado esquerdo, mas com entradas $r_1$ e $r_2$, tenham soluções ${y_p}_1$ e ${y_p}_2$, respectivamente.

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Se denotarmos o lado esquerdo da equação dada como $L[y]$, então, pela linearidade de $L[y]$, para $y_p = {y_p}_1 + {y_p}_2$, temos o seguinte, o que prova a regra da soma.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Exemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
De acordo com a Regra Básica (a), definimos $y_p = Ce^{\gamma x}$ e substituímos na equação dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Caso em que $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar o coeficiente $C$ e encontrar $y_p$ da seguinte forma.

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Caso em que $\gamma^2 + a\gamma + b = 0$
Neste caso, a Regra de Modificação (b) deve ser aplicada. Primeiro, vamos encontrar as raízes da equação característica da EDO homogênea $y^{\prime\prime} + ay^{\prime} + by = 0$ usando o fato de que $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

A partir disso, obtemos a base da EDO homogênea

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Caso em que $\gamma \neq -a-\gamma$
Como a nossa escolha para $y_p$, $Ce^{\gamma x}$, é uma solução da EDO homogênea correspondente, mas não uma raiz dupla, multiplicamos este termo por $x$ de acordo com a Regra de Modificação (b), resultando em $y_p = Cxe^{\gamma x}$.

Agora, substituindo a $y_p$ modificada de volta na equação dada $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Caso em que $\gamma = -a-\gamma$
Neste caso, nossa escolha para $y_p$, $Ce^{\gamma x}$, corresponde a uma raiz dupla da EDO homogênea correspondente. Portanto, de acordo com a Regra de Modificação (b), multiplicamos este termo por $x^2$, resultando em $y_p = Cx^2 e^{\gamma x}$.

Agora, substituindo a $y_p$ modificada de volta na equação dada $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extensão do Método: $r(x)$ como um Produto de Funções
Considere a EDO linear não homogênea onde $r(x)$ tem a forma $r(x) = k x^n e^{\alpha x}\cos(\omega x)$

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Se $r(x)$ é um produto de funções como a exponencial $e^{\alpha x}$, uma potência de $x$ ($x^m$), $\cos{\omega x}$ ou $\sin{\omega x}$ (aqui assumimos $\cos$ sem perda de generalidade), ou uma soma de tais produtos (ou seja, pode ser expresso como uma soma e produto das funções na primeira coluna da tabela anterior), mostraremos que existe uma solução $y_p$ que é uma soma e produto das funções na segunda coluna da mesma tabela.

> Há partes descritas usando álgebra linear para uma prova rigorosa, que são marcadas com um *. Você pode pular essas partes e ainda ter uma compreensão geral.
{: .prompt-tip }

### Definição do Espaço Vetorial $V$*
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

Para um $r(x)$ como este, podemos definir um espaço vetorial $V$ tal que $r(x) \in V$ da seguinte forma:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forma das Derivadas de Funções Exponenciais, Polinomiais e Trigonométricas
A forma das derivadas das funções básicas apresentadas na primeira coluna da tabela anterior é a seguinte.
- Função exponencial: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Função polinomial: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Função trigonométrica: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

As derivadas obtidas pela diferenciação dessas funções também são expressas como <u>somas do mesmo tipo de funções</u>.

Portanto, se as funções $f$ e $g$ são as funções acima ou suas somas, aplicando a regra do produto a $r(x) = f(x)g(x)$, temos

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

e aqui, $f$, $f^{\prime}$, $f^{\prime\prime}$ e $g$, $g^{\prime}$, $g^{\prime\prime}$ podem todos ser escritos como somas ou múltiplos escalares de funções exponenciais, polinomiais e trigonométricas. Portanto, $r^{\prime}(x) = (fg)^{\prime}$ e $r^{\prime\prime}(x) = (fg)^{\prime\prime}$, assim como $r(x)$, também podem ser expressos como somas e produtos dessas funções.

### Invariância de $V$ sob o Operador Diferencial $D$ e a Transformação Linear $L$*
Ou seja, não apenas $r(x)$ em si, mas também $r^{\prime}(x)$ e $r^{\prime\prime}(x)$ são combinações lineares de termos da forma $x^k e^{\alpha x}\cos(\omega x)$ e $x^k e^{\alpha x}\sin(\omega x)$, portanto

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Sem nos limitarmos a $r(x)$, se introduzirmos o operador diferencial $D$ para todos os elementos do espaço vetorial $V$ definido anteriormente e o expressarmos de forma mais geral, *o espaço vetorial $V$ é fechado sob o operador diferencial $D$*. Portanto, se denotarmos o lado esquerdo da equação dada, $y^{\prime\prime} + ay^{\prime} + by$, como $L[y]$, então *$V$ é invariante sob $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Como $r(x) \in V$ e $V$ é invariante sob $L$, existe outro elemento $y_p$ em $V$ que satisfaz $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Portanto, se escolhermos uma $y_p$ apropriada como uma soma de todos os termos de produto possíveis usando coeficientes a determinar $A_0, A_1, \dots, A_n$ e $K, M$ como segue, podemos determinar os coeficientes substituindo $y_p$ (ou $xy_p$, $x^2y_p$) e suas derivadas na equação dada, de acordo com a Regra Básica (a) e a Regra de Modificação (b). Aqui, $n$ é determinado pelo grau de $x$ em $r(x)$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Se a entrada dada $r(x)$ incluir vários valores diferentes de $\alpha_i$ e $\omega_j$, a escolha de $y_p$ deve incluir todos os termos possíveis da forma $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ e $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ para cada valor de $\alpha_i$ e $\omega_j$.  
> A vantagem do método dos coeficientes a determinar é a sua simplicidade. Se o ansatz se tornar tão complexo que essa vantagem se perca, pode ser melhor aplicar o método da variação de parâmetros, que será discutido posteriormente.
{: .prompt-warning }

## Extensão do Método: Equação de Euler-Cauchy
O método dos coeficientes a determinar pode ser utilizado não apenas para [EDOs lineares homogêneas com coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), mas também para a [equação de Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Substituição de Variáveis
Como vimos anteriormente, ao [substituir $x = e^t$ para transformar em uma EDO linear homogênea de segunda ordem com coeficientes constantes](/posts/euler-cauchy-equation/#transformacao-para-uma-edo-linear-homogenea-de-segunda-ordem-com-coeficientes-constantes), temos

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

e vimos que a equação de Euler-Cauchy pode ser transformada na seguinte EDO linear homogênea com coeficientes constantes em termos de $t$.

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Agora, podemos aplicar o mesmo [método dos coeficientes a determinar discutido anteriormente](#o-metodo-dos-coeficientes-a-determinar) à Eq. ($\ref{eqn:substituted}$) para resolver em termos de $t$, e finalmente, usar $t = \ln x$ para encontrar a solução em termos de $x$.

### Caso em que $r(x)$ é uma potência de $x$, um logaritmo natural, ou uma soma e produto de tais funções
Em particular, se a entrada $r(x)$ consiste em potências de $x$, logaritmos naturais, ou somas e produtos de tais funções, uma $y_p$ apropriada pode ser escolhida diretamente de acordo com as seguintes regras de escolha para a equação de Euler-Cauchy.

> **Regras de Escolha para o Método dos Coeficientes a Determinar: Versão para a Equação de Euler-Cauchy**  
> **(a) Regra Básica**: Se $r(x)$ na Eq. ($\ref{eqn:euler_cauchy}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha e determine seus coeficientes substituindo $y_p$ e suas derivadas na Eq. ($\ref{eqn:euler_cauchy}$).  
> **(b) Regra de Modificação**: Se um termo em sua escolha para $y_p$ for uma solução da EDO homogênea correspondente $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiplique este termo por $\ln{x}$ (ou por $(\ln{x})^2$ se esta solução corresponder a uma raiz dupla da equação característica da EDO homogênea).  
> **(c) Regra da Soma**: Se $r(x)$ for uma soma de funções listadas na primeira coluna da tabela, então escolha para $y_p$ a soma das funções nas linhas correspondentes da segunda coluna.
>
> | Termo em $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Desta forma, para formas de entrada $r(x)$ que são importantes na prática, podemos encontrar a mesma $y_p$ que seria obtida através da [substituição de variáveis](#substituicao-de-variaveis) de uma maneira mais rápida e simples. Podemos derivar estas regras de escolha para a equação de Euler-Cauchy substituindo $x$ por $\ln{x}$ nas [regras de escolha originais](#o-metodo-dos-coeficientes-a-determinar) que vimos anteriormente.
