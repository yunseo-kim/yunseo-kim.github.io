---
title: "線性相依與線性獨立、基底與維度"
description: "整理線性相依與線性獨立，並系統介紹向量空間的基底、標準基底與維度（替換定理與推論）等核心觀念。"
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Prerequisites
- [向量與線性組合](/posts/vectors-and-linear-combinations/)
- [向量空間、子空間，以及矩陣](/posts/vector-spaces-subspaces-and-matrices/)

## 線性相依與線性獨立

對某個[向量空間](/posts/vector-spaces-subspaces-and-matrices/#向量空間) $\mathbb{V}$ 與其[子空間](/posts/vector-spaces-subspaces-and-matrices/#子空間) $\mathbb{W}$，想要找到生成[生成](/posts/vectors-and-linear-combinations/#線性組合-cmathbfv--dmathbfw) $\mathbb{W}$ 的可能最小有限子集 $S$。

設 $S = \\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3, \mathbf{u}_4 \\}$ 且 $\mathrm{span}(S) = \mathbb{W}$。要判斷是否存在生成 $\mathbb{W}$ 的 $S$ 的真子集，等價於判斷 $S$ 中某向量是否可由其餘向量的[線性組合](/posts/vectors-and-linear-combinations/#向量的線性組合)表出。例：欲以其餘三向量線性組合表出 $\mathbf{u}_4$ 的充要條件，是存在純量 $a_1, a_2, a_3$ 使下式成立：
$$ \mathbf{u}_4 = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 $$

然而對 $\mathbf{u}_1$, $\mathbf{u}_2$, $\mathbf{u}_3$, $\mathbf{u}_4$ 各自重複此聯立一次方程的判斷相當繁瑣，不妨改寫為
$$ a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + a_3\mathbf{u}_3 + a_4\mathbf{u}_4 = \mathbf{0} $$

若 $S$ 中某向量可由其他向量線性組合得到，則上式存在至少一個係數 $a_1, a_2, a_3, a_4$ 非零的表示法。其逆亦真：若存在至少一個係數非零，卻能將零向量表為 $S$ 的線性組合，則 $S$ 中有向量可由其餘向量線性組合。

推而廣之，定義如下的**線性相依**與**線性獨立**。

> **定義**  
> 對向量空間 $\mathbb{V}$ 的子集 $S$，若存在有限多個彼此不同的向量 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in S$ 與至少一個不為 $0$ 的純量 $a_1, a_2, \dots, a_n$，使 $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$，則稱集合 $S$ 與其中向量**線性相依（linearly dependent）**。否則稱為**線性獨立（linearly independent）**。
{: .prompt-info }

對任意向量 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$，當 $a_1 = a_2 = \cdots = a_n = 0$ 時，必有 $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n = \mathbf{0}$。此稱為**零向量的平凡表示（trivial representation of $\mathbf{0}$）**。

關於線性獨立的集合，以下三個命題在所有向量空間中恆為真，尤其是**命題 3**對判斷有限集合是否線性獨立非常實用。

> - **命題 1**：空集合為線性獨立。要使某集合線性相依，該集合必須非空。
> - **命題 2**：由一個非零向量組成的集合是線性獨立的。
> - **命題 3**：某集合線性獨立的充要條件是，將 $\mathbf{0}$ 表為該集合線性組合的方式僅有平凡表示一種。
{: .prompt-info }

此外，以下定理亦很重要。

> **定理 1**  
> 設 $\mathbb{V}$ 為向量空間且 $S_1 \subseteq S_2 \subseteq \mathbb{V}$。若 $S_1$ 線性相依，則 $S_2$ 亦線性相依。
>
> **推論 1-1**  
> 設 $\mathbb{V}$ 為向量空間且 $S_1 \subseteq S_2 \subseteq \mathbb{V}$。若 $S_2$ 線性獨立，則 $S_1$ 亦線性獨立。
{: .prompt-info }

> **定理 2**  
> 設 $\mathbb{V}$ 為向量空間，$S$ 為其中線性獨立的子集。對不屬於 $S$ 的向量 $\mathbf{v} \in \mathbb{V}$，$S \cup \\{\mathbf{v}\\}$ 線性相依的充要條件為 $\mathbf{v} \in \mathrm{span}(S)$。
>
> 換言之，**若 $S$ 的任一真子集都無法生成與 $S$ 相同的空間，則 $S$ 線性獨立。**
{: .prompt-info }

## 基底與維度

### 基底

對[線性獨立](#線性相依與線性獨立)的 $\mathbb{W}$ 的生成集 $S$，有一個特別的性質：$\mathbb{W}$ 中的每個向量都必可表示為 $S$ 的線性組合，且此表示是唯一的（**定理 3**）。因此，對某向量空間的線性獨立生成集，特別定義為**基底（basis）**如下。

> **基底的定義**  
> 對向量空間 $\mathbb{V}$ 與其子集 $\beta$，若 $\beta$ 線性獨立且能生成 $\mathbb{V}$，則稱 $\beta$ 為 $\mathbb{V}$ 的**基底（basis）**。此時，$\beta$ 中的向量形成 $\mathbb{V}$ 的基底。
{: .prompt-info }

> 因為 $\mathrm{span}(\emptyset) = \\{\mathbf{0}\\}$ 且 $\emptyset$ 線性獨立，因此 $\emptyset$ 為點空間的基底。
{: .prompt-tip }

特別地，下述 $F^n$ 的特殊基底稱為 $F^n$ 的**標準基底（standard basis）**。

> **標準基底的定義**  
> 對向量空間 $F^n$，考慮下列向量：
>
> $$ \mathbf{e}_1 = (1,0,0,\dots,0),\ \mathbf{e}_2 = (0,1,0,\dots,0),\ \dots, \mathbf{e}_n = (0,0,0,\dots,1) $$
>
> 則集合 $\\{\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\}$ 是 $F^n$ 的基底，稱為 $F^n$ 的**標準基底（standard basis）**。
{: .prompt-info }

> **定理 3**  
> 設 $\mathbb{V}$ 為向量空間，$\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \in \mathbb{V}$ 彼此不同。集合 $\beta = \\{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n \\}$ 成為 $\mathbb{V}$ 的基底的充要條件是：「任意向量 $\mathbf{v} \in \mathbb{V}$ 可且僅可唯一地表示為 $\beta$ 中向量的線性組合」。亦即，存在唯一的純量 $n$-有序組 $(a_1, a_2, \dots, a_n)$ 使得
>
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
>
{: .prompt-info }

依據**定理 3**，若互異的 $n$ 個向量 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ 形成向量空間 $\mathbb{V}$ 的基底，則在該空間中，給定向量 $\mathbf{v}$ 便唯一對應到純量 $n$-有序組 $(a_1, a_2, \dots, a_n)$；反之，給定純量 $n$-有序組也唯一決定對應的向量 $\mathbf{v}$。日後在學習**可逆性**與**同構**時會再整理；在此情形下，向量空間 $\mathbb{V}$ 與 $F^n$ <u>本質上相同</u>。

> **定理 4**  
> 若有限集合 $S$ 滿足 $\mathrm{span}(S) = \mathbb{V}$，則 $S$ 的某個子集是 $\mathbb{V}$ 的基底。亦即，此時 $\mathbb{V}$ 的基底為有限集。
{: .prompt-info }

> 許多向量空間屬於**定理 4**的適用對象，但未必一概如此。<u>基底也可能不是有限集</u>。{: .prompt-tip }

### 維度

> **定理 5：替換定理（replacement theorem）**  
> 設集合 $G$ 含 $n$ 個向量且 $\mathrm{span}(G) = \mathbb{V}$。若 $L$ 是由 $m$ 個線性獨立向量所成的 $\mathbb{V}$ 的子集，則 $m \leq n$。此外，存在 $H \subseteq G$，其含有 $n-m$ 個向量，並滿足 $\mathrm{span}(L \cup H) = \mathbb{V}$。
{: .prompt-info }

由此可得兩個極為重要的推論。

> **替換定理的推論 5-1**  
> 假設向量空間 $\mathbb{V}$ 含有有限集基底，則 $\mathbb{V}$ 的所有基底皆為有限集，且含有相同數目的向量。
{: .prompt-info }

因此，構成 $\mathbb{V}$ 基底的向量個數是 $\mathbb{V}$ 不隨改變的本質性質，稱為**維度（dimension）**。

> **維度的定義**  
> 具有有限集基底的向量空間稱為**有限維（finite dimension）**；此時基底元素個數 $n$ 稱為該向量空間的**維度（dimension）**，記作 $\dim(\mathbb{V})$。非有限維的向量空間稱為**無限維（infinite dimension）**。
{: .prompt-info }

> - $\dim(\\{\mathbf{0}\\}) = 0$
> - $\dim(F^n) = n$
> - $\dim(\mathcal{M}_{m \times n}(F)) = mn$
{: .prompt-tip }

> 向量空間的維度會因所處的體而異。
> - 在複數體 $\mathbb{C}$ 上，複數向量空間的維度為 1，基底為 $\\{1\\}$
> - 在實數體 $\mathbb{R}$ 上，複數向量空間的維度為 2，基底為 $\\{1,i\\}$
{: .prompt-tip }

在有限維向量空間 $\mathbb{V}$ 中，含有比 $\dim(\mathbb{V})$ 更多向量的子集不可能是線性獨立的。

> **替換定理的推論 5-2**  
> 設 $\mathbb{V}$ 為維度為 $n$ 的向量空間。
> 1. 任何生成 $\mathbb{V}$ 的有限集合必含至少 $n$ 個向量，而由 $n$ 個向量組成的 $\mathbb{V}$ 的生成集即為 $\mathbb{V}$ 的基底。
> 2. 線性獨立且含 $n$ 個向量的 $\mathbb{V}$ 子集是 $\mathbb{V}$ 的基底。
        3. 可將線性獨立的 $\mathbb{V}$ 子集擴張為基底。亦即，若 $L \subseteq \mathbb{V}$ 線性獨立，則存在 $\mathbb{V}$ 的基底 $\beta$ 使得 $\beta \supseteq L$。
{: .prompt-info }

### 子空間的維度

> **定理 6**  
> 對有限維向量空間 $\mathbb{V}$，其子空間 $\mathbb{W}$ 亦為有限維，且 $\dim(\mathbb{W}) \leq \dim(\mathbb{V})$。特別地，若 $\dim(\mathbb{W}) = \dim(\mathbb{V}) \quad \Rightarrow \quad \mathbb{V} = \mathbb{W}.$
>
> **推論 6-1**  
> 對有限維向量空間 $\mathbb{V}$ 的子空間 $\mathbb{W}$，可將 $\mathbb{W}$ 的任一基底擴張為 $\mathbb{V}$ 的基底。
{: .prompt-info }

依**定理 6**，$\mathbb{R}^3$ 的子空間之維度可能為 $0,1,2,3$。
- 0 維：僅包含原點（$\mathbf{0}$）的點空間 $\\{\mathbf{0}\\}$
- 1 維：通過原點（$\mathbf{0}$）的直線
- 2 維：包含原點（$\mathbf{0}$）的平面
- 3 維：整個三維歐幾里得空間
