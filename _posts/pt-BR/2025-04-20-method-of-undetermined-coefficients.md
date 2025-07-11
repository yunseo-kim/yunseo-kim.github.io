---
title: "Método dos Coeficientes Indeterminados"
description: "Vamos explorar o método dos coeficientes indeterminados, uma técnica que permite resolver facilmente problemas de valor inicial para certos tipos de EDOs lineares não homogêneas com coeficientes constantes, frequentemente utilizada em engenharia para sistemas vibratórios e circuitos RLC."
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - O **método dos coeficientes indeterminados** se aplica a:
>   - EDOs lineares com **coeficientes constantes $a$ e $b$**
>   - Onde a entrada $r(x)$ consiste de funções exponenciais, potências de $x$, $\cos$ ou $\sin$, ou somas e produtos dessas funções
>   - Equação da forma $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Regras de seleção para o método dos coeficientes indeterminados**  
>   - **(a) Regra básica**: Se $r(x)$ na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha na segunda coluna e determine os coeficientes indeterminados substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regra de modificação**: Se o termo escolhido para $y_p$ for uma solução da EDO homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da EDO homogênea).  
>   - **(c) Regra da soma**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções correspondentes na segunda coluna.
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
- Espaços vetoriais, geração linear (álgebra linear)

## Método dos Coeficientes Indeterminados
Consideremos uma equação diferencial ordinária linear não homogênea de segunda ordem

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

onde $r(x) \not\equiv 0$, e a equação diferencial homogênea correspondente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

De acordo com o que vimos em [EDOs Lineares Não Homogêneas de Segunda Ordem](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver um problema de valor inicial para a equação diferencial não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$), precisamos encontrar $y_h$ resolvendo a equação homogênea ($\ref{eqn:homogeneous_linear_ode}$) e depois encontrar uma solução particular $y_p$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) para obter a solução geral

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Então, como encontramos $y_p$? O método geral para encontrar $y_p$ é o **método da variação de parâmetros**, mas em certos casos podemos aplicar o **método dos coeficientes indeterminados**, que é muito mais simples. Este método é particularmente útil na engenharia para sistemas vibratórios e modelos de circuitos RLC.

O método dos coeficientes indeterminados é adequado para equações diferenciais lineares com **coeficientes constantes $a$ e $b$** e onde a entrada $r(x)$ consiste de funções exponenciais, potências de $x$, $\cos$ ou $\sin$, ou somas e produtos dessas funções:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

A ideia central do método dos coeficientes indeterminados é que essas formas de $r(x)$ têm derivadas que mantêm uma forma similar. Para aplicar o método, escolhemos um $y_p$ com forma similar a $r(x)$, mas com coeficientes indeterminados que serão determinados substituindo $y_p$ e suas derivadas na equação diferencial dada. As regras para escolher a forma apropriada de $y_p$ são as seguintes:

> **Regras de seleção para o método dos coeficientes indeterminados**  
> **(a) Regra básica**: Se $r(x)$ na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha na segunda coluna e determine os coeficientes indeterminados substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regra de modificação**: Se o termo escolhido para $y_p$ for uma solução da EDO homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da equação homogênea).  
> **(c) Regra da soma**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções correspondentes na segunda coluna.
>
> | Termo em $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método tem a vantagem de ser não apenas simples, mas também autocorretivo. Se você escolher $y_p$ incorretamente ou com poucos termos, chegará a uma contradição; se escolher muitos termos, os coeficientes dos termos desnecessários serão zero, levando ao resultado correto. Mesmo que algo dê errado ao aplicar o método, você perceberá naturalmente durante o processo de resolução, então pode tentar com confiança seguindo as regras de seleção acima.

### Prova da regra da soma
Considere uma equação diferencial linear não homogênea da forma

$$ y^{\prime\prime} + ay^{\prime} + by = r_1(x) + r_2(x) $$

Agora, considere as duas equações com o mesmo lado esquerdo, mas com entradas $r_1$ e $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + ay^{\prime} + by = r_1(x) \\
y^{\prime\prime} + ay^{\prime} + by = r_2(x)
\end{gather*} $$

Suponha que estas equações tenham soluções ${y_p}_1$ e ${y_p}_2$, respectivamente. Denotando o lado esquerdo da equação por $L[y]$, pela linearidade de $L[y]$, temos que $y_p = {y_p}_1 + {y_p}_2$ satisfaz:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

## Exemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
De acordo com a regra básica (a), escolhemos $y_p = Ce^{\gamma x}$ e substituímos na equação dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

### Caso em que $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar o coeficiente indeterminado $C$ e encontrar $y_p$ da seguinte forma:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

### Caso em que $\gamma^2 + a\gamma + b = 0$
Neste caso, precisamos aplicar a regra de modificação (b). Primeiro, usando $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, encontramos as raízes da equação característica da equação homogênea $y^{\prime\prime} + ay^{\prime} + by = 0$:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Isso nos dá a base da equação homogênea:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

#### Caso em que $\gamma \neq -a-\gamma$
Como $Ce^{\gamma x}$ é uma solução da equação homogênea correspondente (mas não corresponde a uma raiz dupla), pela regra de modificação (b), multiplicamos por $x$ e escolhemos $y_p = Cxe^{\gamma x}$.

Substituindo esta nova forma de $y_p$ na equação original $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

#### Caso em que $\gamma = -a-\gamma$
Neste caso, $Ce^{\gamma x}$ corresponde a uma raiz dupla da equação característica da equação homogênea, então pela regra de modificação (b), multiplicamos por $x^2$ e escolhemos $y_p = Cx^2 e^{\gamma x}$.

Substituindo na equação original $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$

## Extensão do método dos coeficientes indeterminados: $r(x)$ na forma de produtos de funções
Considere uma EDO linear não homogênea com $r(x) = k x^n e^{\alpha x}\cos(\omega x)$:

$$ y^{\prime\prime} + ay^{\prime} + by = C x^n e^{\alpha x}\cos(\omega x) $$

Se $r(x)$ puder ser expresso como produtos de funções exponenciais $e^{\alpha x}$, potências de $x$ como $x^m$, e funções trigonométricas como $\cos{\omega x}$ ou $\sin{\omega x}$ (aqui assumimos $\cos$ sem perda de generalidade), ou somas e produtos dessas funções (ou seja, se puder ser expresso como somas e produtos das funções na primeira coluna da tabela anterior), então existe uma solução particular $y_p$ que é uma soma e produto das funções na segunda coluna da tabela.

> Para uma prova rigorosa, usamos álgebra linear em algumas partes, que estão marcadas com \*. Você pode pular essas partes e ainda compreender a ideia geral.
{: .prompt-tip }

### Definição do espaço vetorial $V$\*
Para $r(x)$ da forma
$$ \begin{align*}
r(x) &= C_1x^{n_1}e^{\alpha_1 x} \times C_2x^{n_2}e^{\alpha_2 x}\cos(\omega x) \times \cdots \\
&= C x^n e^{\alpha x}\cos(\omega x)
\end{align*} $$

podemos definir um espaço vetorial $V$ tal que $r(x) \in V$:

$$ V = \mathrm{span}\left\{x^k e^{\alpha x}\cos(\omega x), \; x^k e^{\alpha x}\sin(\omega x) \bigm| k=0,1,\dots,n \right\}$$

### Forma das derivadas de funções exponenciais, polinomiais e trigonométricas
As derivadas das funções básicas apresentadas na primeira coluna da tabela têm as seguintes formas:
- Função exponencial: $\cfrac{d}{dx}e^{\alpha x} = \alpha e^{\alpha x}$
- Função polinomial: $\cfrac{d}{dx}x^m = mx^{m-1}$
- Funções trigonométricas: $\cfrac{d}{dx}\cos\omega x = -\omega\sin\omega x, \quad \cfrac{d}{dx}\sin\omega x = \omega\cos\omega x$

Observe que as derivadas dessas funções também podem ser expressas como <u>somas de funções do mesmo tipo</u>.

Portanto, se $f$ e $g$ são funções do tipo acima ou somas delas, e $r(x) = f(x)g(x)$, aplicando a regra do produto para derivadas:

$$ \begin{align*}
(fg)^{\prime} &= f^{\prime}g + fg^{\prime}, \\
(fg)^{\prime\prime} &= f^{\prime\prime}g + 2f^{\prime}g^{\prime} + fg^{\prime\prime}
\end{align*} $$

onde $f$, $f^{\prime}$, $f^{\prime\prime}$ e $g$, $g^{\prime}$, $g^{\prime\prime}$ podem todos ser escritos como somas ou múltiplos constantes de funções exponenciais, polinomiais e trigonométricas. Portanto, $r^{\prime}(x) = (fg)^{\prime}$ e $r^{\prime\prime}(x) = (fg)^{\prime\prime}$ também podem ser expressos como somas e produtos dessas funções, assim como $r(x)$.

### Invariância de $V$ sob o operador de diferenciação $D$ e a transformação linear $L$\*
Ou seja, não apenas $r(x)$, mas também $r^{\prime}(x)$ e $r^{\prime\prime}(x)$ são combinações lineares de termos da forma $x^k e^{\alpha x}\cos(\omega x)$ e $x^k e^{\alpha x}\sin(\omega x)$, então:

$$ r(x) \in V \implies r^{\prime}(x) \in V,\ r^{\prime\prime}(x) \in V. $$

Generalizando para todos os elementos do espaço vetorial $V$ definido anteriormente e introduzindo o operador de diferenciação $D$, podemos dizer que *o espaço vetorial $V$ é fechado sob a operação de diferenciação $D$*. Portanto, se denotarmos o lado esquerdo da equação $y^{\prime\prime} + ay^{\prime} + by$ como $L[y]$, então *$V$ é invariante sob $L$*.

$$ D^2(V)\subseteq V,\quad aD(V)\subseteq V,\quad b\,V\subseteq V \implies L(V)\subseteq V. $$

Como $r(x) \in V$ e $V$ é invariante sob $L$, existe outro elemento $y_p \in V$ tal que $L[y_p] = r$.

$$ \exists y_p \in V: L[y_p] = r $$

### Ansatz
Portanto, podemos escolher um $y_p$ apropriado usando coeficientes indeterminados $A_0, A_1, \dots, A_n$ e $K$, $M$ da seguinte forma, que inclui a soma de todos os possíveis termos produto:

$$ y_p = e^{\alpha x}(A_nx^n + A_{n-1}x^{n-1} + \cdots + A_1x + A_0)(K\cos{\omega x} + M \sin{\omega x}). $$

Aqui, $n$ é determinado pelo grau de $x$ em $r(x)$. Seguindo as regras básica (a) e de modificação (b), podemos determinar os coeficientes indeterminados substituindo $y_p$ (ou $xy_p$, $x^2y_p$ conforme necessário) e suas derivadas na equação dada.

$\blacksquare$

> Se a entrada dada $r(x)$ contiver diferentes valores de $\alpha_i$ e $\omega_j$, você deve incluir todos os possíveis termos da forma $x^{k}e^{\alpha_i x}\cos(\omega_j x)$ e $x^{k}e^{\alpha_i x}\sin(\omega_j x)$ para cada valor de $\alpha_i$ e $\omega_j$ ao escolher $y_p$.  
> A vantagem do método dos coeficientes indeterminados é sua simplicidade, mas se o ansatz se tornar muito complicado, perdendo essa vantagem, pode ser melhor aplicar o método da variação de parâmetros, que discutiremos posteriormente.
{: .prompt-warning }

## Extensão do método dos coeficientes indeterminados: equação de Euler-Cauchy
O método dos coeficientes indeterminados pode ser aplicado não apenas a [EDOs Lineares Homogêneas de Segunda Ordem com Coeficientes Constantes](/posts/homogeneous-linear-odes-with-constant-coefficients/), mas também à [Equação de Euler-Cauchy](/posts/euler-cauchy-equation/):

$$ x^2y^{\prime\prime} + axy^{\prime} + by = r(x) \label{eqn:euler_cauchy}\tag{5}$$

### Substituição de variável
Como vimos em [transformação para uma EDO linear homogênea de segunda ordem com coeficientes constantes](/posts/euler-cauchy-equation/#transformação-para-uma-edo-linear-homogênea-de-segunda-ordem-com-coeficientes-constantes), fazendo a substituição $x = e^t$, temos:

$$ \frac{d}{dx} = \frac{1}{x}\frac{d}{dt}, \quad \frac{d^2}{dx^2} = \frac{1}{x^2}\left(\frac{d^2}{dt^2} - \frac{d}{dt} \right) $$

e a equação de Euler-Cauchy pode ser transformada em uma EDO linear homogênea com coeficientes constantes em termos de $t$:

$$ y^{\prime\prime} + (a-1)y^{\prime} + by = r(e^t). \label{eqn:substituted}\tag{6} $$

Podemos então aplicar o [método dos coeficientes indeterminados](#método-dos-coeficientes-indeterminados) à equação ($\ref{eqn:substituted}$) em termos de $t$ e, finalmente, substituir $t = \ln x$ para obter a solução em termos de $x$.

### Caso em que $r(x)$ é uma potência de $x$, logaritmo natural, ou somas e produtos dessas funções
Especialmente quando a entrada $r(x)$ consiste de potências de $x$, logaritmos naturais, ou somas e produtos dessas funções, podemos selecionar diretamente um $y_p$ apropriado seguindo as regras de seleção para a equação de Euler-Cauchy:

> **Regras de seleção para o método dos coeficientes indeterminados: versão para a equação de Euler-Cauchy**  
> **(a) Regra básica**: Se $r(x)$ na equação ($\ref{eqn:euler_cauchy}$) for uma das funções na primeira coluna da tabela, escolha $y_p$ da mesma linha na segunda coluna e determine os coeficientes indeterminados substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:euler_cauchy}$).  
> **(b) Regra de modificação**: Se o termo escolhido para $y_p$ for uma solução da EDO homogênea correspondente $x^2y^{\prime\prime} + axy^{\prime} + by = 0$, multiplique este termo por $\ln{x}$ (ou por $(\ln{x})^2$ se esta solução corresponder a uma raiz dupla da equação característica da equação homogênea).  
> **(c) Regra da soma**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções correspondentes na segunda coluna.
>
> | Termo em $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $kx^m\ (m=0,1,\cdots)$ | $Ax^m$ |
> | $kx^m \ln{x}\ (m=0,1,\cdots)$ | $x^m(B\ln x + C)$ |
> | $k(\ln{x})^s\ (s=0,1,\cdots)$ | $D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s$ |
> | $kx^m (\ln{x})^s$<br>$(m=0,1,\cdots ;\; s=0,1,\cdots)$ | $x^m \left( D_0 + D_1\ln{x} + \cdots + D_{s-1}(\ln{x})^{s-1} + D_s(\ln{x})^s \right)$ |
{: .prompt-info }

Isso nos permite encontrar $y_p$ de forma mais rápida e simples para formas práticas importantes de entrada $r(x)$, sem precisar fazer a [substituição de variável](#substituição-de-variável). Estas regras de seleção para a equação de Euler-Cauchy podem ser derivadas das [regras de seleção originais](#método-dos-coeficientes-indeterminados) substituindo $x$ por $\ln{x}$.
