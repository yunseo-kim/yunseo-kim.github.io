---
title: "向量與線性組合"
description: "認識什麼是向量與其基本運算（純量乘法、加法），並在此基礎上理解向量的線性組合與生成空間（span）的概念。"
categories: [Mathematics, Linear Algebra]
tags: [Vector, Vector Operations, Linear Combinations]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **向量的定義**
>   - **狹義的向量（歐幾里得向量）**：同時具有大小與方向的物理量
>   - **廣義、線性代數中的向量**：向量空間的元素
> - **向量的表示法**
>   - **箭號表示法**：以箭頭長度表示大小、箭頭方向表示方向。易於視覺化且直觀，但對四維以上的高維向量或非歐幾里得向量不易表達。
>   - **分量表示法**：將向量的起點置於座標空間的原點，以終點的座標來表示向量。
> - **向量的基本運算**
>   - **加法**：$(a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n)$
>   - **純量乘法**：$c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n)$
> - **向量的線性組合**
>   - 對有限個向量 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ 與純量 $a_1, a_2, \dots, a_n$，若 $\mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n$，則稱向量 $\mathbf{v}$ 為 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ 的**線性組合（linear combination）**
>   - 此時 $a_1, a_2, \dots, a_n$ 稱為此線性組合的**係數（coefficient）**
{: .prompt-info }
> - **生成空間（span）**
>   - 對向量空間 $\mathbb{V}$ 的非空子集 $S$，由 $S$ 中的向量所作的所有線性組合所成的集合 $\mathrm{span}(S)$
>   - 定義 $\mathrm{span}(\emptyset) = \{ \mathbf{0} \}$
>   - 若向量空間 $\mathbb{V}$ 的子集 $S$ 滿足 $\mathrm{span}(S) = \mathbb{V}$，則稱 $S$ 生成（generate 或 span）$\mathbb{V}$

## Prerequisites
- 座標平面／座標空間
- 體（field）

## 什麼是向量？

### 狹義的向量：歐幾里得向量

> 力、速度、加速度等許多物理量不僅具有大小，還包含方向資訊。如此同時擁有大小與方向的物理量稱為**向量（vector）**。
{: .prompt-info }

上述定義是物理學的力學或高中程度數學所處理的向量定義。如此強調「有向線段的大小與方向」之幾何意涵，基於物理直覺的狹義向量，嚴格地稱為**歐幾里得向量（Euclidean vector）**。

### 廣義的向量：向量空間的元素

在線性代數中，向量被定義為較上述歐幾里得向量更廣、更抽象的代數結構，如下所示。

> **定義**  
> 定義在體 $F$ 上的**向量空間（vector space）**或**線性空間（linear space）** $\mathbb{V}$ 是一個集合，配備兩種運算：**加法**與**純量乘法**，並滿足下列八個條件。體 $F$ 的元素稱為**純量（scalar）**，向量空間 $\mathbb{V}$ 的元素稱為**向量（vector）**。
>
> - **加法（sum）**：對 $\mathbb{V}$ 的任意兩元素 $\mathbf{x}, \mathbf{y}$，對應到唯一的元素 $\mathbf{x} + \mathbf{y} \in \mathbb{V}$。此時 $\mathbf{x} + \mathbf{y}$ 稱為 $\mathbf{x}$ 與 $\mathbf{y}$ 的**和**。
> - **純量乘法（scalar multiplication）**：對體 $F$ 的元素 $a$ 與向量空間 $\mathbb{V}$ 的元素 $\mathbf{x}$，對應到唯一的元素 $a\mathbf{x} \in \mathbb{V}$。此時 $a\mathbf{x}$ 稱為 $\mathbf{x}$ 的**純量倍（scalar multiple）**。
>
> 1. 對所有 $\mathbf{x},\mathbf{y} \in \mathbb{V}$，有 $\mathbf{x} + \mathbf{y} = \mathbf{y} + \mathbf{x}$。（加法的交換律）
> 2. 對所有 $\mathbf{x},\mathbf{y},\mathbf{z} \in \mathbb{V}$，有 $(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$。（加法的結合律）
> 3. 對所有 $\mathbf{x} \in \mathbb{V}$，存在 $\mathbf{0} \in \mathbb{V}$ 使得 $\mathbf{x} + \mathbf{0} = \mathbf{x}$。（零向量，加法的單位元）
> 4. 對每個 $\mathbf{x} \in \mathbb{V}$，存在 $\mathbf{y} \in \mathbb{V}$ 使得 $\mathbf{x}+\mathbf{y}=\mathbf{0}$。（加法的逆元）
> 5. 對每個 $\mathbf{x} \in \mathbb{V}$，有 $1\mathbf{x} = \mathbf{x}$。（乘法的單位元）
> 6. 對所有 $a,b \in F$ 與所有 $\mathbf{x} \in \mathbb{V}$，有 $(ab)\mathbf{x} = a(b\mathbf{x})$。（純量乘法的結合律）
> 7. 對所有 $a \in F$ 與所有 $\mathbf{x},\mathbf{y} \in \mathbb{V}$，有 $a(\mathbf{x}+\mathbf{y}) = a\mathbf{x} + a\mathbf{y}$。（對加法的純量乘法分配律 1）
> 8. 對所有 $a,b \in F$ 與所有 $\mathbf{x},\mathbf{y} \in \mathbb{V}$，有 $(a+b)\mathbf{x} = a\mathbf{x} + b\mathbf{x}$。（對加法的純量乘法分配律 2）
{: .prompt-info }

此線性代數中的向量定義涵蓋了先前提及的[歐幾里得向量](#狹義的向量-歐幾里得向量)，屬於更廣的範疇。[歐幾里得向量](#狹義的向量-歐幾里得向量)亦可驗證滿足上述八項性質。

向量的起源與發展，與物理學中一系列實用問題密切相關，例如對力、物體運動、轉動、場等概念的定量描述。為了以數學方式表述自然現象，最初提出了[歐幾里得向量](#狹義的向量-歐幾里得向量)的概念；其後數學在將這些物理概念一般化與理論化的過程中，建立了向量空間、內積、外積等形式結構，形成今日的向量定義。換言之，向量是物理學的需求與數學的建構所共同促成的概念，與其說是純數學的產物，不如說是數學界與物理學界密切交流下的跨領域成果。

經典力學處理的[歐幾里得向量](#狹義的向量-歐幾里得向量)，可以用數學上[更一般化的框架](#廣義的向量-向量空間的元素)來表達；而在今日的物理學中，不僅[歐幾里得向量](#狹義的向量-歐幾里得向量)，連同向量空間、函數空間等更抽象的數學概念也被廣泛運用並賦予物理意義。因此，將兩種定義簡單對應為「物理學的定義」與「數學的定義」並不恰當。

關於向量空間我們之後再深入，先聚焦於在座標空間中可幾何表徵的狹義向量——歐幾里得向量。先熟悉直觀的歐幾里得向量例子，對日後推廣到其他類型的向量也有幫助。

## 向量的表示法
### 箭號表示法

這是最能保留幾何直觀、也最常見的表示法。向量的大小用箭頭的長度表示，向量的方向用箭頭的方向表示。

![Euclidean Vector from A to B](https://upload.wikimedia.org/wikipedia/commons/9/95/Vector_from_A_to_B.svg){: width="972" }
> *圖片來源*
> - 作者：維基百科用戶 [Nguyenthephuc](https://en.wikipedia.org/wiki/User:Nguyenthephuc)
> - 授權條款：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

此表示法雖直觀，但對四維以上的高維向量，其箭號表示法的侷限明顯。此外，日後我們還會處理原本就難以以幾何圖形表達的非歐幾里得向量，因此有必要熟悉下述的分量表示法。

### 分量表示法

不論向量位於何處，只要大小與方向相同，便視為相同的向量。因此當給定一個座標空間時，若將向量的起點固定在該座標空間的原點，則<u>$n$ 維向量對應到 $n$ 維空間中的任意一個點</u>；此時即可用終點的座標來表示向量。這種方法稱為向量的**分量表示法**。

$$ (a_1, a_2, \cdots, a_n) \in \mathbb{R}^n \text{ or } \mathbb{C}^n $$

![Position vector](https://upload.wikimedia.org/wikipedia/commons/5/5d/Position_vector.svg)
> *圖片來源*
> - 作者：維基共享資源用戶 [Acdx](https://commons.wikimedia.org/wiki/User:Acdx)
> - 授權條款：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## 向量的基本運算

向量的基本運算有兩種：**加法**與**純量乘法**。所有向量運算皆可由此二者的組合來表達。

### 向量的加法

兩個向量的和仍為向量，而其分量等於兩向量的對應分量逐一相加。

$$ (a_1, a_2, \cdots, a_n) + (b_1, b_2, \cdots, b_n) := (a_1+b_1, a_2+b_2, \cdots, a_n+b_n) $$

### 向量的純量乘法

向量可以被放大或縮小，這以在向量上乘以常數（純量）的純量乘法來表示。對任一向量做常數倍，其結果等同於對每個分量皆做相同的常數倍。

$$ c(a_1, a_2, \cdots, a_n) := (ca_1, ca_2, \cdots, ca_n) $$

![Scalar multiplication of vectors](https://upload.wikimedia.org/wikipedia/commons/1/1b/Scalar_multiplication_of_vectors2.svg)
> *圖片來源*
> - 作者：維基百科用戶 [Silly rabbit](https://en.wikipedia.org/wiki/User:Silly_rabbit)
> - 授權條款：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)

## 向量的線性組合

如同微積分從數 $x$ 與函數 $f(x)$ 出發，線性代數則從向量 $\mathbf{v}, \mathbf{w}, \dots$ 與線性組合 $c\mathbf{v} + d\mathbf{w} + \cdots$ 出發。而所有向量的線性組合皆由上述兩種基本運算——[加法](#向量的加法)與[純量乘法](#向量的純量乘法)——的組合構成。

> 對有限個向量 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ 與純量 $a_1, a_2, \dots, a_n$，若下式成立，則稱向量 $\mathbf{v}$ 為 $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ 的**線性組合（linear combination）**。
> 
> $$ \mathbf{v} = a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \cdots + a_n\mathbf{u}_n $$
> 
> 此時，$a_1, a_2, \dots, a_n$ 稱為此線性組合的**係數（coefficient）**。
{: .prompt-info }

那麼，線性組合為何重要？請考慮如下情形：**在 $m$ 維空間上的 $n$ 個向量，構成一個 $m \times n$ 矩陣的 $n$ 個列**。

$$ \begin{gather*}
\mathbf{v}_1 = (a_{11}, a_{21}, \dots, a_{m1}), \\
\mathbf{v}_2 = (a_{12}, a_{22}, \dots, a_{m2}), \\
\vdots \\
\mathbf{v}_n = (a_{1n}, a_{2n}, \dots, a_{mn}) \\
\\
A = \Bigg[ \mathbf{v}_1 \quad \mathbf{v}_2 \quad \cdots \quad \mathbf{v}_n \Bigg]
\end{gather*} $$

此處的關鍵有兩點：

1. **寫出所有可能的線性組合 $Ax = x_1\mathbf{v}_1 + x_2\mathbf{v}_2 + \cdots + x_n\mathbf{v}_n$。** 它構成了什麼？
2. 找出能產生期望輸出向量 $Ax = b$ 的**數 $x_1, x_2, \dots, x_n$**。

第二個問題的答案我們稍後再談；先專注於第一個問題。為了簡化討論，先以非零的二維（$m=2$）向量兩個（$n=2$）為例。

### 線性組合 $c\mathbf{v} + d\mathbf{w}$

二維空間中的向量 $\mathbf{v}$ 具有兩個分量。對所有純量 $c$，<u>向量 $c\mathbf{v}$ 與原先的 $\mathbf{v}$ 平行，並在通過原點的 $xy$ 平面上形成一條無限長的直線。</u>

若第二個給定向量 $\mathbf{w}$ 不在這條直線上（亦即 $\mathbf{v}$ 與 $\mathbf{w}$ 不平行），那麼向量 $d\mathbf{w}$ 又形成另一條直線。將這兩條直線加以組合，可知**線性組合 $c\mathbf{v} + d\mathbf{w}$ 形成一個包含原點的平面**。

![Linear combinations of two vectors](https://upload.wikimedia.org/wikipedia/commons/6/6f/Linjcomb.png)
> *圖片來源*
> - 作者：維基共享資源用戶 [Svjo](https://commons.wikimedia.org/wiki/User:Svjo)
> - 授權條款：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

### 生成

如此，向量們的線性組合便構成向量空間，這稱為空間的**生成（span）**。

> **定義**  
> 對於向量空間 $\mathbb{V}$ 的非空子集 $S$，由 $S$ 中向量所有線性組合所成的集合稱為 $S$ 的**生成空間（span）**，記為 $\mathrm{span}(S)$。但定義 $\mathrm{span}(\emptyset) = \{ \mathbf{0} \}$。
{: .prompt-info }

> **定義**  
> 若向量空間 $\mathbb{V}$ 的子集 $S$ 滿足 $\mathrm{span}(S) = \mathbb{V}$，則稱 $S$**生成（generate 或 span）**$\mathbb{V}$。
{: .prompt-info }

雖然我們尚未探討子空間、基底等概念，但記住此例，有助於理解向量空間的概念。
