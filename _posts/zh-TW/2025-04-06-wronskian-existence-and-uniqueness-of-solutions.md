---
title: "朗斯基行列式(Wronskian)，解的存在性與唯一性"
description: "針對具有任意連續變數係數的二階齊次線性常微分方程式，本文將探討其初始值問題解的存在性與唯一性定理，以及利用朗斯基行列式(Wronskian)判斷解的線性相依/線性獨立的方法。此外，我們將證明此類方程式恆有通解，且此通解包含方程式的所有解。"
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> 對於在區間 $I$ 上具有連續的任意變數係數 $p$ 與 $q$ 的二階齊次線性常微分方程式
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> 與初始條件
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> ，以下四個定理成立。
> 1. **初始值問題解的存在性與唯一性定理**：由給定方程式及初始條件構成的初始值問題，在區間 $I$ 上有唯一的解 $y(x)$。
> 2. **利用朗斯基行列式(Wronskian)判斷解的線性相依/線性獨立**：對於方程式的兩個解 $y_1$ 和 $y_2$，若在區間 $I$ 內存在一點 $x_0$ 使得**朗斯基行列式(Wronskian)** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ 的值為 $0$，則兩解為線性相依。此外，若在區間 $I$ 內存在一點 $x_1$ 使得 $W\neq 0$，則兩解為線性獨立。
> 3. **通解的存在性**：給定的方程式在區間 $I$ 上有通解。
> 4. **奇異解的不存在**：此通解包含方程式的所有解（即不存在奇異解）。
{: .prompt-info }

## 先備知識
- [一階線性常微分方程的解法](/posts/Solution-of-First-Order-Linear-ODE/)
- [二階齊次線性常微分方程式 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [常數係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [歐拉-柯西方程式](/posts/euler-cauchy-equation/)
- 反矩陣與奇異矩陣、行列式

## 具有連續任意變數係數的齊次線性常微分方程式
先前我們已探討過[常數係數二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-with-constant-coefficients/)與[歐拉-柯西方程式](/posts/euler-cauchy-equation/)的通解。
本文將把討論擴展到更一般的情況，探討具有任意連續**變數係數(variable coefficient)** $p$ 與 $q$ 的二階齊次線性常微分方程式

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

的通解之存在性與形式。此外，我們還將探討由常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 與下列兩個初始條件

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

所構成的[初始值問題](/posts/homogeneous-linear-odes-of-second-order/#初始值問題與初始條件)的唯一性。

若先說結論，本文的核心內容是：具有連續係數的<u>線性</u>常微分方程式，不會有*奇異解(singular solution)*（無法從通解中得到的解）。

## 初始值問題解的存在性與唯一性定理
> **初始值問題解的存在性與唯一性定理(Existence and Uniqueness Theorem for Initial Value Problems)**  
> 若 $p(x)$ 與 $q(x)$ 在某個開放區間 $I$ 上是連續函數，且 $x_0$ 位於區間 $I$ 內，則由方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 與 ($\ref{eqn:initial_conditions}$) 構成的初始值問題，在區間 $I$ 上有唯一的解 $y(x)$。
{: .prompt-info }

關於存在性的證明，本文不予討論，僅探討唯一性的證明。一般而言，證明唯一性比證明存在性來得簡單。
若對證明不感興趣，可跳過此部分，直接前往[解的線性相依與線性獨立](#解的線性相依與線性獨立)。

### 唯一性的證明
假設由常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 與初始條件 ($\ref{eqn:initial_conditions}$) 構成的初始值問題，在區間 $I$ 上有兩個解 $y_1(x)$ 與 $y_2(x)$。若能證明這兩個解的差

$$ y(x) = y_1(x) - y_2(x) $$

在區間 $I$ 上恆為 $0$，即表示在區間 $I$ 上 $y_1 \equiv y_2$，從而證明解的唯一性。

由於方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 是齊次線性常微分方程式，因此 $y_1$ 與 $y_2$ 的線性組合 $y$ 也是在 $I$ 上的解。$y_1$ 與 $y_2$ 滿足相同的初始條件 ($\ref{eqn:initial_conditions}$)，因此 $y$ 滿足條件

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_2(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

。現在考慮函數

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

及其導數

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

。從常微分方程式可得

$$ y^{\prime\prime} = -py^{\prime} - qy $$

，將其代入關於 $z^{\prime}$ 的式子中，可得

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

。由於 $y$ 與 $y^{\prime}$ 為實數，因此

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

。從此式與 $z$ 的定義，可得到兩個不等式

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

。從這兩個不等式可知 $\|2yy^{\prime}\|\leq z$，那麼對於式 ($\ref{eqn:z_prime}$) 的最後一項，下列不等式成立。

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

利用此結果以及 $-p \leq \|p\|$，並將式 ($\ref{eqn:inequalities}$a) 應用於式 ($\ref{eqn:z_prime}$) 的 $2yy^{\prime}$ 項，可得

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

。因為 ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$，由此可得

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

，若令括號內的函數為 $h = 1 + 2\|p\| + \|q\|$，則

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

。同理，從式 ($\ref{eqn:z_prime}$) 與 ($\ref{eqn:inequalities}$) 可得

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

。這兩個不等式 ($\ref{eqn:inequality_6a}$)、($\ref{eqn:inequality_6b}$) 與下列不等式

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

等價，兩式左邊的[積分因子](/posts/Solution-of-First-Order-Linear-ODE/#非齊次線性常微分方程)為

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{與} \qquad F_2 = e^{\int h(x)\ dx} $$

。因為 $h$ 是連續的，不定積分 $\int h(x)\ dx$ 存在，且 $F_1$ 與 $F_2$ 為正數，故從式 ($\ref{eqn:inequalities_7}$) 可得

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

。這表示在區間 $I$ 上，$F_1 z$ 不遞增，而 $F_2 z$ 不遞減。根據式 ($\ref{eqn:initial_conditions_*}$)，$z(x_0) = 0$，因此，

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

。最後，將不等式兩邊同除以正數 $F_1$ 與 $F_2$，即可如下證明解的唯一性。

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## 解的線性相依與線性獨立
讓我們回顧一下在[二階齊次線性常微分方程式](/posts/homogeneous-linear-odes-of-second-order/#基底與通解)中探討過的內容。在開放區間 $I$ 上的通解，是由 $I$ 上的**基底(basis)** $y_1$、$y_2$，即一對線性獨立的解所構成。此處，稱 $y_1$ 與 $y_2$ 在區間 $I$ 上為**線性獨立(linearly independent)**，意指對於區間內所有的 $x$，滿足下列條件。

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{且 }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

若不滿足上述條件，而是對於至少一個不為 $0$ 的 $k_1$、$k_2$ 使得 $k_1y_1(x) + k_2y_2(x) = 0$ 成立，則 $y_1$ 與 $y_2$ 在區間 $I$ 上為**線性相依(linearly dependent)**。此時，對於區間 $I$ 內的所有 $x$，

$$ \text{(a) } y_1 = ky_2 \quad \text{或} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

，因此 $y_1$ 與 $y_2$ 成比例。

現在，讓我們來看看以下判斷解的線性獨立/線性相依的方法。

> **利用朗斯基行列式(Wronskian)判斷解的線性相依/線性獨立**  
> **i.** 若常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在開放區間 $I$ 上具有連續係數 $p(x)$ 與 $q(x)$，則在區間 $I$ 上，方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的兩個解 $y_1$ 與 $y_2$ 為線性相依的充要條件是，這兩個解的*朗斯基行列式(Wronski determinant)*，簡稱**朗斯基行列式(Wronskian)** 的下列行列式
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> 在區間 $I$ 內的某點 $x_0$ 為 $0$。
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{與 } y_2 \text{為線性相依} $$
>
> **ii.** 若在區間 $I$ 內的一點 $x=x_0$ 上 $W=0$，則在區間 $I$ 內的所有 $x$ 上 $W=0$。
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> 換言之，若在區間 $I$ 中存在一點 $x_1$ 使得 $W\neq 0$，則在該區間 $I$ 上 $y_1$、$y_2$ 為線性獨立。
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_1)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{與 } y_2 \text{為線性獨立}
> \end{align*}$$
>
{: .prompt-info }

> 朗斯基行列式最初由波蘭數學家約瑟夫·瑪麗亞·赫內-朗斯基(Józef Maria Hoene-Wroński)引入，在他去世後的 11882 HE，由蘇格兰數學家托馬斯·繆爾(Sir Thomas Muir)命名為現在的名稱。
{: .prompt-tip }

### 證明
#### i. (a)
假設在區間 $I$ 上 $y_1$ 與 $y_2$ 為線性相依。則在區間 $I$ 上，式 ($\ref{eqn:linearly_dependent}$a) 或 ($\ref{eqn:linearly_dependent}$b) 成立。若式 ($\ref{eqn:linearly_dependent}$a) 成立，則

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

；同理，若式 ($\ref{eqn:linearly_dependent}$b) 成立，則

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

，因此可以確認<u>在區間 $I$ 內的所有 $x$</u>，朗斯基行列式 $W(y_1, y_2)=0$。

#### i. (b)
反之，假設在某點 $x = x_0$ 上 $W(y_1, y_2)=0$，我們將證明在區間 $I$ 上 $y_1$ 與 $y_2$ 為線性相依。考慮關於未知數 $k_1$、$k_2$ 的線性聯立方程式

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

。這可以表示為如下的向量方程式形式。

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

此向量方程式的係數矩陣為

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

，而此矩陣的行列式即為 $W(y_1(x_0), y_2(x_0))$。因為 $\det(A) = W=0$，所以 $A$ 是不存在**反矩陣(inverse matrix)**的**奇異矩陣(singular matrix)**，因此聯立方程式 ($\ref{eqn:linear_system}$) 除了零向量 $(0,0)$ 之外，還有一個解 $(c_1, c_2)$，其中 $k_1$ 與 $k_2$ 至少有一個不為 $0$。現在引入函數

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

。由於方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 是齊次線性的，根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，此函數在區間 $I$ 上是 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的解。從式 ($\ref{eqn:linear_system}$) 可知，此解滿足初始條件 $y(x_0)=0$、$y^{\prime}(x_0)=0$。

另一方面，存在一個滿足相同初始條件 $y^\*(x_0)=0$、${y^\*}^{\prime}(x_0)=0$ 的自明解 $y^\* \equiv 0$。由於方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的係數 $p$ 與 $q$ 是連續的，根據[初始值問題解的存在性與唯一性定理](#初始值問題解的存在性與唯一性定理)，解的唯一性得到保證，因此 $y \equiv y^\*$。也就是說，在區間 $I$ 上

$$ c_1y_1 + c_2y_2 \equiv 0 $$

。因為 $c_1$ 與 $c_2$ 至少有一個不為 $0$，所以不滿足 ($\ref{eqn:linearly_independent}$)，這表示在區間 $I$ 上 $y_1$、$y_2$ 為線性相依。

#### ii.
若在區間 $I$ 內的某點 $x_0$ 上 $W(x_0)=0$，則根據 [i.(b)](#i-b)，在區間 $I$ 上 $y_1$、$y_2$ 為線性相依，那麼根據 [i.(a)](#i-a)，$W\equiv 0$。因此，若在區間 $I$ 內存在任何一點 $x_1$ 使得 $W(x_1)\neq 0$，則 $y_1$ 與 $y_2$ 為線性獨立。 $\blacksquare$

## 通解包含所有解
### 通解的存在性
> 若 $p(x)$ 與 $q(x)$ 在開放區間 $I$ 上連續，則方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在區間 $I$ 上有通解。
{: .prompt-info }

#### 證明
根據[初始值問題解的存在性與唯一性定理](#初始值問題解的存在性與唯一性定理)，常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在區間 $I$ 上有一個滿足初始條件

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

的解 $y_1(x)$，以及一個在區間 $I$ 上滿足初始條件

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

的解 $y_2(x)$。這兩個解的朗斯基行列式在 $x=x_0$ 處的值不為零

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

，因此根據[利用朗斯基行列式(Wronskian)判斷解的線性相依/線性獨立](#解的線性相依與線性獨立)，在區間 $I$ 上 $y_1$ 與 $y_2$ 為線性獨立。因此，這兩個解在區間 $I$ 上構成了方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的解的基底，且帶有任意常數 $c_1$、$c_2$ 的通解 $y = c_1y_1 + c_2y_2$ 必然在區間 $I$ 上存在。 $\blacksquare$

### 奇異解的不存在
> 若常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在某個開放區間 $I$ 上具有連續係數 $p(x)$ 與 $q(x)$，則在區間 $I$ 上，方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的所有解 $y=Y(x)$ 均為
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> 的形式，其中 $y_1$、$y_2$ 是在區間 $I$ 上方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的解的基底，而 $C_1$、$C_2$ 為適當的常數。  
> 也就是說，方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 不具有無法從通解中得到的解，即**奇異解(singular solution)**。
{: .prompt-info }

#### 證明
令 $y=Y(x)$ 為在區間 $I$ 上方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的任意一個解。現在，根據[通解的存在性](#通解的存在性)，常微分方程式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在區間 $I$ 上有通解

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

。現在，我們必須證明對於任意的 $Y(x)$，存在常數 $c_1$、$c_2$ 使得在區間 $I$ 上 $y(x)=Y(x)$。首先，我們證明可以找到 $c_1$、$c_2$ 的值，使得在區間 $I$ 中任選一點 $x_0$，滿足 $y(x_0)=Y(x_0)$ 且 $y^{\prime}(x_0)=Y^{\prime}(x_0)$。從式 ($\ref{eqn:general_solution}$) 可得

$$ \begin{gather*}
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix}
c_1 \\ c_2
\end{matrix}\right]
= \left[\begin{matrix}
Y(x_0) \\ Y^{\prime}(x_0)
\end{matrix}\right]
\end{gather*} \label{eqn:vector_equation_2}\tag{15} $$

。因為 $y_1$ 與 $y_2$ 是基底，所以係數矩陣的行列式 $W(y_1(x_0), y_2(x_0))\neq 0$，因此方程式 ($\ref{eqn:vector_equation_2}$) 可以對 $c_1$ 與 $c_2$ 求解。令其解為 $(c_1, c_2) = (C_1, C_2)$。將此代入式 ($\ref{eqn:general_solution}$) 可得以下的特解。

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

因為 $C_1$、$C_2$ 是方程式 ($\ref{eqn:vector_equation_2}$) 的解，所以，

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

。根據[初始值問題解的存在性與唯一性定理](#初始值問題解的存在性與唯一性定理)的唯一性，在區間 $I$ 內的所有 $x$ 上，$y^\* \equiv Y$。 $\blacksquare$
