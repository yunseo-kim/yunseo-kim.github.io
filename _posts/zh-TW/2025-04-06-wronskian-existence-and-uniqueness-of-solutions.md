---
title: 朗斯基行列式（Wronskian）、解的存在與唯一性
description: 對於具有連續任意變數係數的二階齊次線性常微分方程，我們將探討初值問題解的存在性與唯一性定理、使用朗斯基行列式（Wronskian）判斷解的線性相依/線性獨立的方法。此外，我們還將證明這類方程式總是具有通解，且此通解包含方程式的所有解。
categories: [Mathematics, Differential Equation]
tags: [ODE, Second-Order ODEs, Linear ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---

## TL;DR
> 在區間 $I$ 上具有連續任意變數係數 $p$ 和 $q$ 的二階齊次線性常微分方程
>
> $$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 $$
>
> 與初始條件
>
> $$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 $$
>
> 對於以下四個定理成立：
> 1. **初值問題解的存在性與唯一性定理**：給定的方程式及初始條件所構成的初值問題在區間 $I$ 上具有唯一解 $y(x)$。
> 2. **使用朗斯基行列式（Wronskian）判斷解的線性相依/線性獨立**：對於方程式的兩個解 $y_1$ 和 $y_2$，若在區間 $I$ 內存在 $x_0$ 使得**朗斯基行列式（Wronskian）** $W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime}$ 的值為 $0$，則這兩個解是線性相依的。此外，若在區間 $I$ 內存在 $x_1$ 使得 $W\neq 0$，則這兩個解是線性獨立的。
> 3. **通解的存在**：給定的方程式在區間 $I$ 上具有通解。
> 4. **奇解的不存在**：此通解包含方程式的所有解（即不存在奇解）。
{: .prompt-info }

## Prerequisites
- [一階線性常微分方程的解法](/posts/Solution-of-First-Order-Linear-ODE/)
- [二階齊次線性常微分方程 (Homogeneous Linear ODEs of Second Order)](/posts/homogeneous-linear-odes-of-second-order/)
- [具有常數係數的二階齊次線性常微分方程](/posts/homogeneous-linear-odes-with-constant-coefficients/)
- [歐拉-柯西方程](/posts/euler-cauchy-equation/)
- 逆矩陣與奇異矩陣、行列式

## 具有連續任意變數係數的齊次線性常微分方程
在先前我們探討了[具有常數係數的二階齊次線性常微分方程](/posts/homogeneous-linear-odes-with-constant-coefficients/)和[歐拉-柯西方程](/posts/euler-cauchy-equation/)的通解。
在本文中，我們將討論更一般的情況，即具有連續任意**變數係數(variable coefficient)** $p$ 和 $q$ 的二階齊次線性常微分方程

$$ y^{\prime\prime} + p(x)y^{\prime} + q(x)y = 0 \label{eqn:homogeneous_linear_ode_with_var_coefficients}\tag{1} $$

的通解存在性與形式。此外，我們還將探討由常微分方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 和以下兩個初始條件

$$ y(x_0)=K_0, \qquad y^{\prime}(x_0)=K_1 \label{eqn:initial_conditions}\tag{2} $$

所構成的[初值問題](/posts/homogeneous-linear-odes-of-second-order/#初值問題和初始條件)的唯一性。

先說結論，具有連續係數的<u>線性</u>常微分方程不具有*奇解(singular solution)*（無法從通解得到的解）是本文討論的核心。

## 初值問題解的存在性與唯一性定理
> **初值問題解的存在性與唯一性定理(Existence and Uniqueness Theorem for Initial Value Problems)**  
> 若 $p(x)$ 和 $q(x)$ 在某開區間 $I$ 上為連續函數，且 $x_0$ 在區間 $I$ 內，則由式 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 和 ($\ref{eqn:initial_conditions}$) 所構成的初值問題在區間 $I$ 上具有唯一解 $y(x)$。
{: .prompt-info }

在此我們不討論存在性的證明，僅探討唯一性的證明。通常來說，證明唯一性比證明存在性簡單。  
若對證明不感興趣，可以跳過這部分直接閱讀[解的線性相依與線性獨立](#解的線性相依與線性獨立)。

### 唯一性的證明
假設常微分方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 和初始條件 ($\ref{eqn:initial_conditions}$) 所構成的初值問題在區間 $I$ 上有兩個解 $y_1(x)$ 和 $y_2(x)$。若能證明這兩個解的差

$$ y(x) = y_1(x) - y_2(x) $$

在區間 $I$ 上恆等於 $0$，則表示在區間 $I$ 上 $y_1 \equiv y_2$，即解具有唯一性。

由於方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 是齊次線性常微分方程，$y_1$ 和 $y_2$ 的線性組合 $y$ 在 $I$ 上也是方程的解。由於 $y_1$ 和 $y_2$ 滿足相同的初始條件 ($\ref{eqn:initial_conditions}$)，$y$ 滿足條件

$$ \begin{align*}
& y(x_0) = y_1(x_0) - y_1(x_0) = 0, \\
& y^{\prime}(x_0) = y_1^{\prime}(x_0) - y_2^{\prime}(x_0) = 0 
\end{align*} \label{eqn:initial_conditions_*}\tag{3}$$

現在考慮函數

$$ z(x) = y(x)^2 + y^{\prime}(x)^2 $$

及其導數

$$ z^{\prime} = 2yy^{\prime} + 2y^{\prime}y^{\prime\prime} $$

從常微分方程可得

$$ y^{\prime\prime} = -py^{\prime} - qy $$

將此代入 $z^{\prime}$ 的表達式，得到

$$ z^{\prime} = 2yy^{\prime} - 2p{y^{\prime}}^2 - 2qyy^{\prime} \label{eqn:z_prime}\tag{4} $$

由於 $y$ 和 $y^{\prime}$ 是實數，因此

$$ (y\pm y^{\prime})^2 = y^2 \pm 2yy^{\prime} + {y^{\prime}}^2 \geq 0 $$

從這裡和 $z$ 的定義可得兩個不等式

$$ (a)\ 2yy^{\prime} \leq y^2 + {y^{\prime}}^2 = z, \qquad (b)\ 2yy^{\prime} \geq -(y^2 + {y^{\prime}}^2) = -z \label{eqn:inequalities}\tag{5} $$

從這兩個不等式可知 $\|2yy^{\prime}\|\leq z$，因此對於式 ($\ref{eqn:z_prime}$) 的最後一項，有以下不等式成立：

$$ \pm2qyy^{\prime} \leq |\pm 2qyy^{\prime}| = |q||2yy^{\prime}| \leq |q|z. $$

利用這個結果和 $-p \leq \|p\|$，並將式 ($\ref{eqn:inequalities}$a) 應用於式 ($\ref{eqn:z_prime}$) 中的項 $2yy^{\prime}$，得到

$$ z^{\prime} \leq z + 2|p|{y^{\prime}}^2 + |q|z $$

由於 ${y^{\prime}}^2 \leq y^2 + {y^{\prime}}^2 = z$，因此

$$ z^{\prime} \leq (1 + 2|p| + |q|)z $$

令括號內的函數為 $h = 1 + 2\|p\| + \|q\|$，則

$$ z^{\prime} \leq hz \quad \forall x \in I \label{eqn:inequality_6a}\tag{6a}$$

同樣地，從式 ($\ref{eqn:z_prime}$) 和 ($\ref{eqn:inequalities}$) 可得

$$ \begin{align*}
-z^{\prime} &= -2yy^{\prime} + 2p{y^{\prime}}^2 + 2qyy^{\prime} \\
&\leq z + 2|p|z + |q|z = hz
\end{align*} \label{eqn:inequality_6b}\tag{6b} $$

這兩個不等式 ($\ref{eqn:inequality_6a}$)、($\ref{eqn:inequality_6b}$) 等價於以下不等式

$$ z^{\prime} - hz \leq 0, \qquad z^{\prime} + hz \geq 0 \label{eqn:inequalities_7}\tag{7} $$

這兩個式子左邊的[積分因子](/posts/Solution-of-First-Order-Linear-ODE/#非齊次線性常微分方程)為

$$ F_1 = e^{-\int h(x)\ dx} \qquad \text{和} \qquad F_2 = e^{\int h(x)\ dx} $$

由於 $h$ 是連續的，因此不定積分 $\int h(x)\ dx$ 存在，且 $F_1$ 和 $F_2$ 為正數，所以從式 ($\ref{eqn:inequalities_7}$) 可得

$$ F_1(z^{\prime} - hz) = (F_1 z)^{\prime} \leq 0, \qquad F_2(z^{\prime} + hz) = (F_2 z)^{\prime} \geq 0 $$

這表示在區間 $I$ 上 $F_1 z$ 不增加且 $F_2 z$ 不減少。由於式 ($\ref{eqn:initial_conditions_*}$) 表明 $z(x_0) = 0$，因此

$$ \begin{cases}
\left(F_1 z \geq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \leq (F_2 z)_{x_0} = 0\right) & (x \leq x_0) \\
\left(F_1 z \leq (F_1 z)_{x_0} = 0\right)\ \& \ \left(F_2 z \geq (F_2 z)_{x_0} = 0\right) & (x \geq x_0)
\end{cases} $$

最後，將不等式兩邊除以正數 $F_1$ 和 $F_2$，可以證明解的唯一性：

$$ (z \leq 0) \ \& \ (z \geq 0) \quad \forall x \in I $$

$$ z = y^2 + {y^{\prime}}^2 = 0 \quad \forall x \in I $$

$$ \therefore y \equiv y_1 - y_2 \equiv 0 \quad \forall x \in I. \ \blacksquare $$

## 解的線性相依與線性獨立
讓我們回顧一下在[二階齊次線性常微分方程](/posts/homogeneous-linear-odes-of-second-order/#基底和通解)中討論的內容。開區間 $I$ 上的通解是由 $I$ 上的**基底(basis)** $y_1$、$y_2$，即線性獨立的解對所構成。這裡 $y_1$ 和 $y_2$ 在區間 $I$ 上**線性獨立(linearly independent)**意味著對於區間內的所有 $x$，滿足：

$$ k_1y_1(x) + k_2y_2(x) = 0 \Leftrightarrow k_1=0\text{且 }k_2=0 \label{eqn:linearly_independent}\tag{8} $$

若不滿足上述條件，且存在至少一組非零的 $k_1$、$k_2$ 使得 $k_1y_1(x) + k_2y_2(x) = 0$，則 $y_1$ 和 $y_2$ 在區間 $I$ 上**線性相依(linearly dependent)**。在這種情況下，對於區間 $I$ 上的所有 $x$，有

$$ \text{(a) } y_1 = ky_2 \quad \text{或} \quad \text{(b) } y_2 = ly_1 \label{eqn:linearly_dependent}\tag{9}$$

即 $y_1$ 和 $y_2$ 成比例。

現在讓我們了解以下判斷解的線性獨立/線性相依的方法：

> **使用朗斯基行列式（Wronskian）判斷解的線性相依/線性獨立**  
> **i.** 若常微分方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在開區間 $I$ 上具有連續係數 $p(x)$ 和 $q(x)$，則區間 $I$ 上方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的兩個解 $y_1$ 和 $y_2$ 線性相依的充分必要條件是這些解的*朗斯基行列式(Wronski determinant)*，簡稱**朗斯基行列式（Wronskian）**
>
> $$ W(y_1, y_2) = 
\begin{vmatrix}
y_1 & y_2 \\
y_1^{\prime} & y_2^{\prime} \\
\end{vmatrix}
= y_1y_2^{\prime} - y_2y_1^{\prime} \label{eqn:wronskian}\tag{10} $$
>
> 在區間 $I$ 內的某點 $x_0$ 處為 $0$。
>
> $$ \exists x_0 \in I: W(x_0)=0 \iff y_1 \text{和 } y_2 \text{是線性相依的} $$
>
> **ii.** 若在區間 $I$ 內的一點 $x=x_0$ 處 $W=0$，則在區間 $I$ 內的所有 $x$ 處 $W=0$。
>
> $$ \exists x_0 \in I: W(x_0)=0 \implies \forall x \in I: W(x)=0 $$
>
> 換句話說，若存在 $x_1 \in I$ 使得 $W\neq 0$，則在區間 $I$ 上 $y_1$、$y_2$ 是線性獨立的。
>
> $$\begin{align*}
> \exists x_1 \in I: W(x_0)\neq 0 &\implies \forall x \in I: W(x)\neq 0 \\
> &\implies y_1 \text{和 } y_2 \text{是線性獨立的}
> \end{align*}$$
>
{: .prompt-info }

> 朗斯基行列式是由波蘭數學家約瑟夫·馬里亞·霍埃內-朗斯基（Józef Maria Hoene-Wroński）首先引入，並在他去世後的11882 HE由蘇格蘭數學家托馬斯·繆爾（Sir Thomas Muir）命名為現在的名稱。
{: .prompt-tip }

### 證明
#### i. (a)
假設在區間 $I$ 上 $y_1$ 和 $y_2$ 是線性相依的。則在區間 $I$ 上式 ($\ref{eqn:linearly_dependent}$a) 或 ($\ref{eqn:linearly_dependent}$b) 成立。若式 ($\ref{eqn:linearly_dependent}$a) 成立，則

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = ky_2ky_2^{\prime} - y_2ky_2^{\prime} = 0 $$

同樣地，若式 ($\ref{eqn:linearly_dependent}$b) 成立，則

$$ W(y_1, y_2) = y_1y_2^{\prime} - y_2y_1^{\prime} = y_1ly_1^{\prime} - ly_1y_1^{\prime} = 0 $$

因此，<u>對於區間 $I$ 內的所有 $x$</u>，朗斯基行列式 $W(y_1, y_2)=0$。

#### i. (b)
反過來，假設在某點 $x = x_0$ 處 $W(y_1, y_2)=0$，我們將證明在區間 $I$ 上 $y_1$ 和 $y_2$ 是線性相依的。考慮關於未知數 $k_1$、$k_2$ 的線性聯立方程

$$ \begin{gather*}
k_1y_1(x_0) + k_2y_2(x_0) = 0 \\
k_1y_1^{\prime}(x_0) + k_2y_2^{\prime}(x_0) = 0
\end{gather*} \label{eqn:linear_system}\tag{11}$$

這可以表示為以下向量方程：

$$ 
\left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right]
\left[\begin{matrix} k_1 \\ k_2 \end{matrix}\right]
= 0
\label{eqn:vector_equation}\tag{12}$$

這個向量方程的係數矩陣是

$$ A = \left[\begin{matrix}
y_1(x_0) & y_2(x_0) \\
y_1^{\prime}(x_0) & y_2^{\prime}(x_0)
\end{matrix}\right] $$

且這個矩陣的行列式就是 $W(y_1(x_0), y_2(x_0))$。由於 $\det(A) = W=0$，$A$ 是一個沒有**逆矩陣(inverse matrix)**的**奇異矩陣(singular matrix)**，因此聯立方程 ($\ref{eqn:linear_system}$) 有非零解 $(c_1, c_2)$，其中 $k_1$ 和 $k_2$ 中至少有一個不為 $0$。現在考慮函數 

$$ y(x) = c_1y_1(x) + c_2y_2(x) $$

由於方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 是齊次線性的，根據[疊加原理](/posts/homogeneous-linear-odes-of-second-order/#疊加原理)，這個函數在區間 $I$ 上是方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的解。從式 ($\ref{eqn:linear_system}$) 可知，這個解滿足初始條件 $y(x_0)=0$、$y^{\prime}(x_0)=0$。

另一方面，平凡解 $y^* \equiv 0$ 也滿足相同的初始條件 $y^*(x_0)=0$、${y^*}^{\prime}(x_0)=0$。由於方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的係數 $p$ 和 $q$ 是連續的，根據[初值問題解的存在性與唯一性定理](#初值問題解的存在性與唯一性定理)，解具有唯一性，因此 $y \equiv y^*$。即在區間 $I$ 上

$$ c_1y_1 + c_2y_2 \equiv 0 $$

由於 $c_1$ 和 $c_2$ 中至少有一個不為 $0$，因此不滿足 ($\ref{eqn:linearly_independent}$)，這表示在區間 $I$ 上 $y_1$、$y_2$ 是線性相依的。

#### ii.
若在區間 $I$ 內的某點 $x_0$ 處 $W(x_0)=0$，則根據 [i.(b)](#i-b)，在區間 $I$ 上 $y_1$、$y_2$ 是線性相依的，且根據 [i.(a)](#i-a)，$W\equiv 0$。因此，若在區間 $I$ 內存在 $x_1$ 使得 $W(x_1)\neq 0$，則 $y_1$ 和 $y_2$ 是線性獨立的。$\blacksquare$

## 通解包含所有解
### 通解的存在
> 若 $p(x)$ 和 $q(x)$ 在開區間 $I$ 上連續，則方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在區間 $I$ 上具有通解。
{: .prompt-info }

#### 證明
根據[初值問題解的存在性與唯一性定理](#初值問題解的存在性與唯一性定理)，常微分方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在區間 $I$ 上有滿足初始條件

$$ y_1(x_0) = 1, \qquad y_1^{\prime}(x_0) = 0 $$

的解 $y_1(x)$ 和滿足初始條件

$$ y_2(x_0) = 0, \qquad y_2^{\prime}(x_0) = 1 $$

的解 $y_2(x)$。這兩個解的朗斯基行列式在 $x=x_0$ 處的值為非零

$$ W(y_1(x_0), y_2(x_0)) = y_1(x_0)y_2^{\prime}(x_0) - y_2(x_0)y_1^{\prime}(x_0) = 1\cdot 1 - 0\cdot 0 = 1 $$

因此，根據[使用朗斯基行列式（Wronskian）判斷解的線性相依/線性獨立](#解的線性相依與線性獨立)，在區間 $I$ 上 $y_1$ 和 $y_2$ 是線性獨立的。因此，這兩個解在區間 $I$ 上形成方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 解的基底，且具有任意常數 $c_1$、$c_2$ 的通解 $y = c_1y_1 + c_2y_2$ 在區間 $I$ 上必定存在。$\blacksquare$

### 奇解的不存在
> 若常微分方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在某開區間 $I$ 上具有連續係數 $p(x)$ 和 $q(x)$，則區間 $I$ 上方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的所有解 $y=Y(x)$ 都具有
>
> $$ Y(x) = C_1y_1(x) + C_2y_2(x) \label{eqn:particular_solution}\tag{13}$$
>
> 的形式，其中 $y_1$、$y_2$ 是區間 $I$ 上方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 解的基底，$C_1$、$C_2$ 是適當的常數。  
> 也就是說，方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 不具有無法從通解得到的解，即**奇解(singular solution)**。
{: .prompt-info }

#### 證明
設 $y=Y(x)$ 是區間 $I$ 上方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 的某個解。根據[通解存在定理](#通解的存在)，常微分方程 ($\ref{eqn:homogeneous_linear_ode_with_var_coefficients}$) 在區間 $I$ 上具有通解

$$ y(x) = c_1y_1(x) + c_2y_2(x) \label{eqn:general_solution}\tag{14}$$

現在我們需要證明對於任意的 $Y(x)$，存在常數 $c_1$、$c_2$ 使得在區間 $I$ 上 $y(x)=Y(x)$。首先，我們證明可以找到 $c_1$、$c_2$ 的值，使得在區間 $I$ 上任意選擇的 $x_0$ 處有 $y(x_0)=Y(x_0)$ 且 $y^{\prime}(x_0)=Y^{\prime}(x_0)$。從式 ($\ref{eqn:general_solution}$) 得到

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

由於 $y_1$ 和 $y_2$ 是基底，係數矩陣的行列式 $W(y_1(x_0), y_2(x_0))\neq 0$，因此方程 ($\ref{eqn:vector_equation_2}$) 可以解出 $c_1$ 和 $c_2$。設其解為 $(c_1, c_2) = (C_1, C_2)$。將這個解代入式 ($\ref{eqn:general_solution}$)，得到特解

$$ y^*(x) = C_1y_1(x) + C_2y_2(x). $$

由於 $C_1$、$C_2$ 是方程 ($\ref{eqn:vector_equation_2}$) 的解，因此

$$ y^*(x_0) = Y(x_0), \qquad {y^*}^{\prime}(x_0) = Y^{\prime}(x_0) $$

根據[初值問題解的存在性與唯一性定理](#初值問題解的存在性與唯一性定理)的唯一性，對於區間 $I$ 內的所有 $x$，$y^* \equiv Y$。$\blacksquare$
