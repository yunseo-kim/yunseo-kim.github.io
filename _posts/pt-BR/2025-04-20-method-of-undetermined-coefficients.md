---
title: "Método dos Coeficientes a Determinar"
description: "Aprenda o método dos coeficientes a determinar, uma técnica útil em engenharia para resolver problemas de valor inicial em EDOs lineares não homogêneas com coeficientes constantes, aplicável a sistemas vibratórios, circuitos RLC e mais."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Aplicação do Método dos Coeficientes a Determinar**:
>   - Possui **coeficientes constantes $a$ e $b$**
>   - A entrada $r(x)$ é composta por funções exponenciais, potências de $x$, $\cos$ ou $\sin$, ou somas e produtos dessas funções
>   - Equação diferencial ordinária linear $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Regras de Escolha para o Método dos Coeficientes a Determinar**  
>   - **(a) Regra básica (basic rule)**: Se $r(x)$ na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha e determine os coeficientes a determinar substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regra de modificação (modification rule)**: Se um termo escolhido para $y_p$ for uma solução da equação diferencial ordinária homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da EDO homogênea).  
>   - **(c) Regra da soma (sum rule)**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções das linhas correspondentes na segunda coluna.
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
- Espaço vetorial, combinação linear (álgebra linear)

## Método dos Coeficientes a Determinar
Considere uma equação diferencial ordinária linear não homogênea de segunda ordem com $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

e a equação diferencial ordinária homogênea correspondente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Como vimos anteriormente em [EDOs Lineares Não Homogêneas de Segunda Ordem](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver um problema de valor inicial para a equação diferencial ordinária linear não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$), precisamos resolver a equação diferencial ordinária homogênea ($\ref{eqn:homogeneous_linear_ode}$) para encontrar $y_h$ e, em seguida, encontrar uma solução particular $y_p$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) para obter a solução geral

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Então, como podemos encontrar $y_p$? Um método geral para encontrar $y_p$ é o **método da variação de parâmetros**, mas em alguns casos, um método muito mais simples, o **método dos coeficientes a determinar**, pode ser aplicado. Em particular, é um método frequentemente usado em engenharia, pois pode ser aplicado a sistemas vibratórios e modelos de circuitos elétricos RLC.

O método dos coeficientes a determinar é adequado para equações diferenciais ordinárias lineares com **coeficientes constantes $a$ e $b$**, e onde a entrada $r(x)$ é uma função exponencial, uma potência de $x$, $\cos$ ou $\sin$, ou uma soma e produto de tais funções.

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

A chave do método dos coeficientes a determinar é que $r(x)$ deste tipo tem derivadas de forma semelhante a si mesma. Para aplicar o método dos coeficientes a determinar, escolhemos um $y_p$ que tenha uma forma semelhante a $r(x)$, mas com coeficientes indeterminados que são determinados substituindo a si mesmo e suas derivadas na equação diferencial ordinária dada. As regras para escolher um $y_p$ apropriado para formas de $r(x)$ que são importantes na prática da engenharia são as seguintes.

> **Regras de Escolha para o Método dos Coeficientes a Determinar**  
> **(a) Regra básica (basic rule)**: Se $r(x)$ na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha e determine os coeficientes a determinar substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regra de modificação (modification rule)**: Se um termo escolhido para $y_p$ for uma solução da equação diferencial ordinária homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da EDO homogênea).  
> **(c) Regra da soma (sum rule)**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções das linhas correspondentes na segunda coluna.
>
> | Termo em $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método não é apenas simples, mas também tem a vantagem de ser autocorretivo. Se você escolher o $y_p$ errado ou com poucos termos, chegará a uma contradição, e se escolher muitos termos, os coeficientes dos termos desnecessários se tornarão $0$, levando ao resultado correto. Mesmo que algo dê errado ao aplicar o método dos coeficientes a determinar, você naturalmente perceberá isso durante o processo de solução, então, se você escolheu um $y_p$ razoavelmente apropriado de acordo com as regras de escolha acima, pode tentar sem hesitação.

### Prova da Regra da Soma
Considere a equação diferencial ordinária linear não homogênea da forma $r(x) = r_1(x) + r_2(x)$

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Agora, considere as duas equações seguintes com o mesmo lado esquerdo, mas com entradas $r_1$ e $r_2$.

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Suponha que elas tenham soluções ${y_p}_1$ e ${y_p}_2$, respectivamente. Se denotarmos o lado esquerdo da equação dada como $L[y]$, então, pela linearidade de $L[y]$, para $y_p = {y_p}_1 + {y_p}_2$, a seguinte relação é satisfeita, provando a regra da soma.

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Exemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
De acordo com a regra básica (a), definimos $y_p = Ce^{\gamma x}$ e substituímos na equação dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Caso em que $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar o coeficiente a determinar $C$ e encontrar $y_p$ da seguinte forma:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Caso em que $\gamma^2 + a\gamma + b = 0$
Neste caso, a regra de modificação (b) deve ser aplicada. Primeiro, vamos encontrar as raízes da equação característica da EDO homogênea $y^{\prime\prime} + ay^{\prime} + by = 0$ usando o fato de que $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$.

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

A partir disso, obtemos a base da EDO homogênea

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Caso em que $\gamma \neq -a-\gamma$
Como o $Ce^{\gamma x}$ que escolhemos para $y_p$ é uma solução que não é uma raiz dupla da EDO homogênea correspondente, de acordo com a regra de modificação (b), multiplicamos este termo por $x$ e definimos $y_p = Cxe^{\gamma x}$.

Agora, substituindo o $y_p$ modificado de volta na equação dada $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Caso em que $\gamma = -a-\gamma$
Neste caso, o $Ce^{\gamma x}$ que escolhemos para $y_p$ é uma raiz dupla da EDO homogênea correspondente, então, de acordo com a regra de modificação (b), multiplicamos este termo por $x^2$ e definimos $y_p = Cx^2 e^{\gamma x}$.

Agora, substituindo o $y_p$ modificado de volta na equação dada $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extensão do Método dos Coeficientes a Determinar: $r(x)$ na Forma de Produto de Funções
Considere a equação diferencial ordinária linear não homogênea da forma $r(x) = k x^n e^{\alpha x}\cos(\omega x)$

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Se $r(x)$ for um produto e soma de funções como a função exponencial $e^{\alpha x}$, a potência de $x$, $x^m$, e $\cos{\omega x}$ ou $\sin{\omega x}$ (aqui assumimos $\cos$ sem perda de generalidade), ou seja, se puder ser expresso como uma soma e produto das funções na primeira coluna da tabela anterior, mostraremos que existe uma solução da equação $y_p$ que é uma soma e produto das funções na segunda coluna da mesma tabela.

> Para uma prova rigorosa, algumas partes são descritas usando álgebra linear e marcadas com um \*. Você pode pular essas partes e ainda assim ter uma compreensão geral do conteúdo.
{: .prompt-tip }

### Definição do Espaço Vetorial $V$*
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

Para um $r(x)$ como este, podemos definir um espaço vetorial $V$ tal que $r(x) \in V$ da seguinte forma:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forma das Derivadas de Funções Exponenciais, Polinomiais e Trigonométricas
As formas das derivadas das funções básicas apresentadas na primeira coluna da tabela anterior são as seguintes:
- Função exponencial: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Função polinomial: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Função trigonométrica: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

A derivada obtida pela diferenciação dessas funções também é expressa como uma <u>soma de funções do mesmo tipo</u>.

Portanto, se as funções $f$ e $g$ são as funções acima ou suas somas, aplicando a regra do produto para $r(x) = f(x)g(x)$, temos

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

e aqui $f$, $f^{\prime}$, $f^{\prime\prime}$ e $g$, $g^{\prime}$, $g^{\prime\prime}$ podem todos ser escritos como somas ou múltiplos escalares de funções exponenciais, polinomiais e trigonométricas. Portanto, $r^{\prime}(x) = (fg)^{\prime}$ e $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ também podem ser expressos como somas e produtos dessas funções, assim como $r(x)$.

### Invariância de $V$ sob o Operador Diferencial $D$ e a Transformação Linear $L$*
Ou seja, não apenas $r(x)$ em si, mas também $r^{\prime}(x)$ e $r^{\prime\prime}(x)$ são combinações lineares de termos da forma $x^k e^{\alpha x}\cos(\omega x)$ e $x^k e^{\alpha x}\sin(\omega x)$, portanto

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Não se limitando a $r(x)$, se introduzirmos o operador diferencial $D$ para todos os elementos do espaço vetorial $V$ definido anteriormente e o expressarmos de forma mais geral, *o espaço vetorial $V$ é fechado sob o operador diferencial $D$*. Portanto, se denotarmos o lado esquerdo da equação dada $y^{\prime\prime} + ay^{\prime} + by$ como $L[y]$, então *$V$ é invariante sob $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Como $r(x) \in V$ e $V$ é invariante sob $L$, existe outro elemento $y_p$ de $V$ que satisfaz $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Portanto, se escolhermos um $y_p$ apropriado para ser a soma de todos os termos de produto possíveis usando os coeficientes a determinar $A_0, A_1, \dots, A_n$ e $K$, $M$ da seguinte forma, podemos determinar os coeficientes a determinar substituindo $y_p$ (ou $xy_p$, $x^2y_p$) e suas derivadas na equação dada, de acordo com a regra básica (a) e a regra de modificação (b). Aqui, $n$ pode ser determinado de acordo com o grau de $x$ em $r(x)$.

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

$\blacksquare$

> Se a entrada $r(x)$ dada incluir múltiplos valores distintos de $\alpha_i$ e $\omega_j$, então $y_p$ deve ser escolhido para incluir todos os termos possíveis da forma $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ e $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ para cada valor de $\alpha_i$ e $\omega_j$.  
> A vantagem do método dos coeficientes a determinar é a sua simplicidade, portanto, se a solução de teste (ansatz) se tornar muito complicada e essa vantagem desaparecer, pode ser melhor aplicar o método da variação de parâmetros, que será discutido posteriormente.
{: .prompt-warning }

## Extensão do Método dos Coeficientes a Determinar: Equação de Euler-Cauchy
Além das [EDOs lineares homogêneas de segunda ordem com coeficientes constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), o método dos coeficientes a determinar também pode ser utilizado para a [equação de Euler-Cauchy](/posts/euler-cauchy-equation/)

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Substituição de Variáveis
Fazendo a [substituição $x = e^t$ para transformá-la em uma EDO linear homogênea de segunda ordem com coeficientes constantes](/posts/euler-cauchy-equation/#transformacao-para-uma-edo-linear-homogenea-de-segunda-ordem-com-coeficientes-constantes), temos

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

e, como vimos anteriormente, a equação de Euler-Cauchy pode ser transformada na seguinte EDO linear homogênea com coeficientes constantes em termos de $t$.

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Agora, podemos aplicar o mesmo [método dos coeficientes a determinar que vimos anteriormente](#metodo-dos-coeficientes-a-determinar) à equação ($\ref{eqn:substituted}$) para resolver em termos de $t$ e, no final, usar $t = \ln x$ para encontrar a solução em termos de $x$.

### Caso em que $r(x)$ é uma Potência de $x$, Logaritmo Natural, ou Somas e Produtos Dessas Funções
Em particular, se a entrada $r(x)$ for composta por potências de $x$, logaritmos naturais, ou somas e produtos de tais funções, podemos escolher diretamente um $y_p$ apropriado de acordo com as seguintes regras de escolha para a equação de Euler-Cauchy.

> **Regras de Escolha para o Método dos Coeficientes a Determinar: Versão para a Equação de Euler-Cauchy**  
> **(a) Regra básica (basic rule)**: Se $r(x)$ na equação ($\ref{eqn:euler_cauchy}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha e determine os coeficientes a determinar substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:euler_cauchy}$).  
> **(b) Regra de modificação (modification rule)**: Se um termo escolhido para $y_p$ for uma solução da equação diferencial ordinária homogênea correspondente $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiplique este termo por $\ln{x}$ (ou por $(\ln{x})^2$ se esta solução corresponder a uma raiz dupla da equação característica da EDO homogênea).  
> **(c) Regra da soma (sum rule)**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções das linhas correspondentes na segunda coluna.
>
> | Termo em $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Desta forma, para formas de entrada $r(x)$ que são importantes na prática, podemos encontrar o mesmo $y_p$ que seria obtido pela [substituição de variáveis](#substituicao-de-variaveis) de forma mais rápida e simples. Podemos derivar estas regras de escolha para a equação de Euler-Cauchy substituindo $\ln{x}$ no lugar de $x$ nas [regras de escolha originais](#metodo-dos-coeficientes-a-determinar) que vimos anteriormente.
