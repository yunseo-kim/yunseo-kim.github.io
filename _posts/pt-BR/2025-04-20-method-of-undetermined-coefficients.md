---
title: Método dos Coeficientes Indeterminados
description: Vamos explorar o método dos coeficientes indeterminados, uma técnica que permite resolver facilmente problemas de valor inicial para equações diferenciais ordinárias lineares não homogêneas com coeficientes constantes, frequentemente utilizada em engenharia para sistemas vibratórios e circuitos elétricos RLC.
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> - **Método dos Coeficientes Indeterminados** se aplica a:
>   - Equações diferenciais lineares com **coeficientes constantes $a$ e $b$**
>   - Onde a entrada $r(x)$ consiste em funções exponenciais, potências de $x$, $\cos$ ou $\sin$, ou combinações dessas funções
>   - Equação diferencial da forma $y^{\prime\prime} + ay^{\prime} + by = r(x)$
> - **Regras de seleção para o método dos coeficientes indeterminados**  
>   - **(a) Regra básica**: Se $r(x)$ na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha o $y_p$ correspondente na mesma linha e determine os coeficientes indeterminados substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
>   - **(b) Regra de modificação**: Se o termo escolhido para $y_p$ for uma solução da equação diferencial homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da equação diferencial homogênea).  
>   - **(c) Regra da soma**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções correspondentes na segunda coluna.
>
> | Termo de $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

## Pré-requisitos
- [Equações Diferenciais Ordinárias Lineares Homogêneas de Segunda Ordem](/posts/homogeneous-linear-odes-of-second-order/)
- [Wronskiano, Existência e Unicidade de Soluções](/posts/wronskian-existence-and-uniqueness-of-solutions/)
- [Equações Diferenciais Ordinárias Lineares Não Homogêneas de Segunda Ordem](/posts/nonhomogeneous-linear-odes-of-second-order/)

## Método dos Coeficientes Indeterminados
Consideremos uma equação diferencial ordinária linear não homogênea de segunda ordem com $r(x) \not\equiv 0$

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r(x) \label{eqn:nonhomogeneous_linear_ode}\tag{1}$$

e a equação diferencial homogênea correspondente

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode}\tag{2} $$

Conforme vimos anteriormente em [Equações Diferenciais Ordinárias Lineares Não Homogêneas de Segunda Ordem](/posts/nonhomogeneous-linear-odes-of-second-order/), para resolver um problema de valor inicial para a equação diferencial não homogênea ($\ref{eqn:nonhomogeneous_linear_ode}$), precisamos encontrar $y_h$ resolvendo a equação homogênea ($\ref{eqn:homogeneous_linear_ode}$) e depois encontrar uma solução particular $y_p$ da equação ($\ref{eqn:nonhomogeneous_linear_ode}$) para obter a solução geral

$$ y(x) = y_h(x) + y_p(x) \label{eqn:general_sol}\tag{3}$$

Como encontramos $y_p$? O método geral para encontrar $y_p$ é o **método da variação de parâmetros**, mas em certos casos podemos aplicar o **método dos coeficientes indeterminados**, que é muito mais simples. Este método é particularmente útil em engenharia para sistemas vibratórios e modelos de circuitos elétricos RLC.

O método dos coeficientes indeterminados é adequado para equações diferenciais lineares com **coeficientes constantes $a$ e $b$** onde a entrada $r(x)$ consiste em funções exponenciais, potências de $x$, $\cos$ ou $\sin$, ou combinações dessas funções:

$$ y^{\prime\prime} + ay^{\prime} + by = r(x) \label{eqn:linear_ode_with_constant_coefficients}\tag{4} $$

O aspecto fundamental do método é que estas formas de $r(x)$ possuem derivadas com estruturas semelhantes a si mesmas. Para aplicar o método, escolhemos um $y_p$ com forma semelhante a $r(x)$, mas com coeficientes indeterminados que serão definidos substituindo $y_p$ e suas derivadas na equação diferencial dada. As regras para escolher o $y_p$ apropriado para formas de $r(x)$ importantes na prática são as seguintes:

> **Regras de seleção para o método dos coeficientes indeterminados**  
> **(a) Regra básica**: Se $r(x)$ na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$) for uma das funções na primeira coluna da tabela, escolha o $y_p$ correspondente na mesma linha e determine os coeficientes indeterminados substituindo $y_p$ e suas derivadas na equação ($\ref{eqn:linear_ode_with_constant_coefficients}$).  
> **(b) Regra de modificação**: Se o termo escolhido para $y_p$ for uma solução da equação diferencial homogênea correspondente $y^{\prime\prime} + ay^{\prime} + by = 0$, multiplique este termo por $x$ (ou por $x^2$ se esta solução corresponder a uma raiz dupla da equação característica da equação diferencial homogênea).  
> **(c) Regra da soma**: Se $r(x)$ for uma soma de funções da primeira coluna da tabela, escolha para $y_p$ a soma das funções correspondentes na segunda coluna.
>
> | Termo de $r(x)$ | Escolha para $y_p(x)$ |
> | :--- | :--- |
> | $ke^{\gamma x}$ | $Ce^{\gamma x}$ |
> | $kx^n\ (n=0,1,\cdots)$ | $K_nx^n + K_{n-1}x^{n-1} + \cdots + K_1x + K_0$ |
> | $k\cos{\omega x}$<br>$k\sin{\omega x}$ | $K\cos{\omega x} + M\sin{\omega x}$ |
> | $ke^{\alpha x}\cos{\omega x}$<br>$ke^{\alpha x}\sin{\omega x}$ | $e^{\alpha x}(K\cos{\omega x} + M\sin{\omega x})$ |
{: .prompt-info }

Este método tem a vantagem de ser não apenas simples, mas também autocorretivo. Se escolhermos incorretamente $y_p$ ou selecionarmos poucos termos, chegaremos a uma contradição; se selecionarmos termos em excesso, os coeficientes dos termos desnecessários serão zero, levando ao resultado correto. Mesmo que algo dê errado ao aplicar o método, perceberemos naturalmente durante o processo de resolução, então podemos tentar sem preocupação, desde que sigamos as regras de seleção acima.

### Prova da regra da soma
Consideremos uma equação diferencial linear não homogênea da forma

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) + r_2(x) $$

Agora, consideremos duas equações com o mesmo lado esquerdo, mas com entradas $r_1$ e $r_2$:

$$ \begin{gather*}
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_1(x) \\
y^{\prime\prime} + p(x)y^{\prime} + q(x)y = r_2(x)
\end{gather*} $$

Suponhamos que estas equações tenham soluções ${y_p}_1$ e ${y_p}_2$, respectivamente. Denotando o lado esquerdo da equação por $L[y]$, pela linearidade de $L[y]$, temos que para $y_p = {y_p}_1 + {y_p}_2$:

$$ L[y_p] = L[{y_p}_1 + {y_p}_2] = L[{y_p}_1] + L[{y_p}_2] = r_1 + r_2 = r. \ \blacksquare $$

### Exemplo: $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$
De acordo com a regra básica (a), escolhemos $y_p = Ce^{\gamma x}$ e substituímos na equação dada $y^{\prime\prime} + ay^{\prime} + by = ke^{\gamma x}$:

$$ \gamma^2 Ce^{\gamma x} + \gamma aCe^{\gamma x} + bCe^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b)e^{\gamma x} = ke^{\gamma x} $$

$$ C(\gamma^2 + a\gamma + b) = k. $$

#### Caso $\gamma^2 + a\gamma + b \neq 0$
Podemos determinar o coeficiente indeterminado $C$ e encontrar $y_p$ da seguinte forma:

$$ C = \frac{k}{\gamma^2 + a\gamma + b} $$

$$ y_p = Ce^{\gamma x} = \frac{k}{\gamma^2 + a\gamma + b} e^{\gamma x}. $$

#### Caso $\gamma^2 + a\gamma + b = 0$
Neste caso, devemos aplicar a regra de modificação (b). Primeiro, usando $b = -\gamma^2 - a\gamma = -\gamma(a + \gamma)$, encontramos as raízes da equação característica da equação diferencial homogênea $y^{\prime\prime} + ay^{\prime} + by = 0$:

$$ y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = 0 $$

$$ \lambda^2 + a\lambda - \gamma(a + \gamma) = 0 $$

$$ (\lambda + (a + \gamma))(\lambda - \gamma) = 0 $$

$$ \lambda = \gamma, -a -\gamma. $$

Isso nos dá a base da equação diferencial homogênea:

$$ y_1 = e^{\gamma x}, \quad y_2 = e^{(-a - \gamma)x} $$

##### Caso $\gamma \neq -a-\gamma$
Como o $y_p$ que escolhemos, $Ce^{\gamma x}$, é uma solução da equação diferencial homogênea correspondente, mas não corresponde a uma raiz dupla, pela regra de modificação (b), multiplicamos este termo por $x$ e escolhemos $y_p = Cxe^{\gamma x}$.

Agora, substituímos este $y_p$ modificado na equação dada $y^{\prime\prime} + ay^{\prime} - \gamma(a + \gamma)y = ke^{\gamma x}$:

$$ C(2\gamma + \gamma^2 x)e^{\gamma x} + aC(1 + \gamma x)e^{\gamma x} - \gamma(a + \gamma)Cxe^{\gamma x} = ke^{\gamma x} $$

$$ C \left[\left\{\gamma^2 + a\gamma -\gamma(a + \gamma)\right\}x + 2\gamma + a \right]e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a)e^{\gamma x} = ke^{\gamma x} $$

$$ C(2\gamma + a) = k $$

$$ \therefore C = \frac{k}{2\gamma + a}, \quad y_p = Cxe^{\gamma x} = \frac{k}{2\gamma + a}xe^{\gamma x}. $$

##### Caso $\gamma = -a-\gamma$
Neste caso, o $y_p$ que escolhemos, $Ce^{\gamma x}$, corresponde a uma raiz dupla da equação característica da equação diferencial homogênea. Pela regra de modificação (b), multiplicamos este termo por $x^2$ e escolhemos $y_p = Cx^2 e^{\gamma x}$.

Agora, substituímos este $y_p$ modificado na equação dada $y^{\prime\prime} - 2\gamma y^{\prime} + \gamma^2 y = ke^{\gamma x}$:

$$ C(2 + 4\gamma x + \gamma^2 x^2)e^{\gamma x} + C(-4\gamma x - 2\gamma^2 x^2)e^{\gamma x} + C(\gamma^2 x^2)e^{\gamma x} = ke^{\gamma x} $$

$$ 2Ce^{\gamma x} = ke^{\gamma x} $$

$$ 2C = k $$

$$ \therefore C = \frac{k}{2}, \quad y_p = Cx^2 e^{\gamma x} = \frac{k}{2}x^2 e^{\gamma x}. $$
