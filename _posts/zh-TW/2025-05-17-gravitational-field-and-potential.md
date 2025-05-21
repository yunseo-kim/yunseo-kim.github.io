---
title: 重力場與重力勢能
description: 探討牛頓萬有引力定律下的重力場向量和重力勢能的定義，並通過兩個重要例子：球殼定理和星系旋轉曲線來說明相關概念。
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - 牛頓萬有引力定律：$\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - 連續質量分佈和具有體積的物體情況：$\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$：從任意原點到位置向量 $\mathbf{r^{\prime}}$ 處的質量密度
>   - $dv^{\prime}$：從任意原點到位置向量 $\mathbf{r^{\prime}}$ 處的體積元素
> - **重力場向量(gravitational field vector)**：
>   - 表示質量 $M$ 物體產生的場中，一個粒子所受到的單位質量力的向量
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - 具有*單位質量力*或*加速度*的維度
> - **重力勢能(gravitational potential)**：
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - 具有 $($*單位質量力* $) \times ($*距離* $)$ 或 *單位質量能量*的維度
>   - $\Phi = -G\cfrac{M}{r}$
>   - 重力勢能只有相對差值有意義，特定值本身沒有意義
>   - 通常設定 $r \to \infty$ 時 $\Phi \to 0$ 的條件來消除不確定性
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **球殼內部和外部的重力勢能(球殼定理)**
>   - 當 $R>a$ 時：
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - 計算球對稱分佈物質在外部某點的重力勢能時，可以將該物體視為質點計算
>   - 當 $R<b$ 時：
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - 在球對稱質量殼內部，重力勢能與位置無關且恆定，作用的重力為 $0$
>   - 當 $b<R<a$ 時：$\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## 重力場
### 牛頓萬有引力定律
牛頓在11666 HE之前就已經系統化萬有引力定律並進行數值驗證。儘管如此，他直到11687 HE才在著作*Principia*中發表自己的成果，這中間相隔了20多年，原因是他無法證明將地球和月球視為無體積質點(point mass)的計算方法是合理的。幸運的是，[利用牛頓後來發明的微積分，我們現在可以比11600年代的牛頓更容易地證明這個問題](#ra時)。

根據牛頓萬有引力定律(Newton's law of universal gravitation)，*每個質量粒子都會吸引宇宙中的所有其他粒子，這種力與兩個質量的乘積成正比，與它們之間距離的平方成反比。* 數學表示如下：

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *圖片來源*
> - 作者：維基媒體用戶 [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - 授權：[CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

單位向量 $\mathbf{e}_r$ 指向從 $M$ 到 $m$ 的方向，負號表示力是吸引力。也就是說，$m$ 被拉向 $M$。

### 卡文迪許實驗
這個定律的實驗驗證和 $G$ 值的確定是在11798 HE由英國物理學家亨利·卡文迪許(Henry Cavendish)完成的。卡文迪許實驗使用一個扭轉天平，由輕桿兩端固定的兩個小球組成。這兩個球分別被附近的另外兩個大球吸引。目前確定的官方 $G$ 值為 $6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$。

> 儘管 $G$ 是最早被發現的基本常數之一，但它的精確度比大多數其他基本常數如 $e$、$c$、$\hbar$ 等要低。即使在今天，仍有許多研究致力於更精確地測量 $G$ 值。
{: .prompt-tip }

### 具有體積的物體情況
方程式 ($\ref{eqn:law_of_gravitation}$) 嚴格來說只適用於*點粒子(point particle)*。如果一方或雙方是具有體積的物體，則需要額外假設重力場(gravitational force field)是*線性場(linear field)*來計算力。也就是說，假設質量為 $m$ 的一個粒子受到其他多個粒子的總重力可以通過向量加法得到。對於連續分佈的物質，總和可以轉換為以下積分：

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$：從任意原點到位置向量 $\mathbf{r^{\prime}}$ 處的質量密度
- $dv^{\prime}$：從任意原點到位置向量 $\mathbf{r^{\prime}}$ 處的體積元素

如果質量為 $M$ 和質量為 $m$ 的物體都具有體積，要計算總重力，還需要對 $m$ 進行第二次體積積分。

### 重力場向量
**重力場向量(gravitational field vector)** $\mathbf{g}$ 定義為質量 $M$ 物體產生的場中，一個粒子所受到的單位質量力的向量：

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

或

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

這裡 $\mathbf{e}_r$ 的方向隨 $\mathbf{r^\prime}$ 變化。

量 $\mathbf{g}$ 具有*單位質量力*或*加速度*的維度。在地球表面附近，重力場向量 $\mathbf{g}$ 的大小就是我們稱為**重力加速度常數(gravitational acceleration constant)**的量，約為 $\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$。

## 重力勢能
### 定義
重力場向量 $\mathbf{g}$ 隨 $1/r^2$ 變化，因此滿足可以表示為某個標量函數(勢能)梯度的條件($\nabla \times \mathbf{g} \equiv 0$)。因此可以寫成：

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

這裡 $\Phi$ 稱為**重力勢能(gravitational potential)**，具有 $($*單位質量力* $) \times ($*距離* $)$ 或 *單位質量能量*的維度。

由於 $\mathbf{g}$ 只依賴於半徑，$\Phi$ 也只隨 $r$ 變化。從方程式 ($\ref{eqn:g_vector}$) 和 ($\ref{eqn:gradient_phi}$)，我們得到：

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

積分後得到：

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

重力勢能只有相對差值有意義，特定值本身沒有意義，因此可以省略積分常數。通常設定 $r \to \infty$ 時 $\Phi \to 0$ 的條件來消除不確定性，方程式 ($\ref{eqn:g_potential}$) 也滿足這個條件。

對於連續分佈的物質，重力勢能為：

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

對於質量分佈在薄殼表面的情況：

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

對於線密度為 $\rho_l$ 的線性質量源：

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### 物理意義
考慮物體在重力場中移動 $d\mathbf{r}$ 時所做的單位質量功 $dW^\prime$：

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

在這個方程中，$\Phi$ 是位置坐標的函數，表示為 $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$。因此，物體在重力場中從一點移動到另一點所做的單位質量功等於這兩點的勢能差。

如果將無限遠處的重力勢能定義為 $0$，則任意點的 $\Phi$ 可以解釋為將物體從無限遠處移動到該點所需的單位質量功。物體的勢能等於其質量與重力勢能 $\Phi$ 的乘積：

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

因此，物體受到的重力等於其勢能梯度的負值：

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

當物體處於由某質量產生的重力場中時，總會產生勢能。嚴格來說，這個勢能存在於場本身，但習慣上我們稱之為該物體的勢能。

## 例子：球殼內部和外部的重力勢能（球殼定理）
### 座標設定與勢能積分表示
讓我們計算內半徑為 $b$、外半徑為 $a$ 的均勻球殼(spherical shell)內部和外部的重力勢能。雖然可以通過直接計算場中單位質量受力分量來獲得球殼產生的重力，但使用勢能方法更簡單。

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

在上圖中，我們計算距離中心 $R$ 處 $P$ 點的勢能。假設殼體質量均勻分佈，則 $\rho(r^\prime)=\rho$，且關於連接球心和點 $P$ 的線的方位角 $\phi$ 具有對稱性：

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

根據餘弦定理：

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

由於 $R$ 是常數，對 $r^\prime$ 微分得到：

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

將此代入方程式 ($\ref{eqn:spherical_shell_1}$)：

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

這裡 $r_\mathrm{max}$ 和 $r_\mathrm{min}$ 由點 $P$ 的位置決定。

### 當 $R>a$ 時
$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

球殼的質量 $M$ 為：

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

因此，勢能為：

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> 比較質量為 $M$ 的質點產生的重力勢能方程式 ($\ref{eqn:g_potential}$) 和我們剛得到的結果 ($\ref{eqn:spherical_shell_outside_2}$)，可以看出它們是相同的。這意味著，計算球對稱分佈物質在外部某點的重力勢能時，可以假設所有質量都集中在中心。地球或月球等大多數球形天體都屬於這種情況，它們可以視為像俄羅斯套娃一樣，由無數個同心但直徑不同的球殼疊加而成。這就是[為什麼將地球或月球等天體視為無體積質點進行計算是合理的](#牛頓萬有引力定律)。
{: .prompt-info }

### 當 $R<b$ 時
$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> 在球對稱質量殼內部，重力勢能與位置無關且恆定，作用的重力為 $0$。
{: .prompt-info }

> 這也是為什麼「地球空心說」是偽科學的主要證據之一。如果地球如地球空心說所聲稱的那樣是一個球殼且內部是空的，那麼在該空腔內的所有物體都不會受到地球重力的作用。考慮到地球的質量和體積，地球不可能是空心的，即使有空腔，那裡的生命體也不會以球殼內側為地面生活，而是像在國際太空站一樣處於失重狀態漂浮。  
> [雖然在地下數公里深的地層中可能有微生物生存](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3)，但至少不可能以地球空心說所聲稱的形式存在。我也很喜歡儒勒·凡爾納的小說《地心遊記》(Voyage au centre de la Terre)和電影《地心冒險》(Journey to the Center of the Earth)，但創作就是創作，不應該當真。
{: .prompt-tip }

### 當 $b<R<a$ 時
$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### 結果
以下是我們計算的三個區域中重力勢能 $\Phi$ 和重力場向量大小 $\|\mathbf{g}\|$ 隨距離 $R$ 變化的圖表：

![Gravitational Potential as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-gravitational-potential.png)
![Magnitude of the Field Vector as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-field-vector.png)
> - Python 視覺化代碼：[yunseo-kim/physics-visualization 倉庫](https://github.com/yunseo-kim/physics-visualization/blob/main/src/shell_theorem.py)
> - 授權：[查看這裡](https://github.com/yunseo-kim/physics-visualization?tab=readme-ov-file#license)

可以看出重力勢能和重力場向量的大小是連續的。如果重力勢能在某點不連續，那麼在該點勢能的梯度（即重力大小）將變為無窮大，這在物理上是不合理的，因此勢能函數必須在所有點上連續。然而，重力場向量的*微分係數*在殼體的內表面和外表面是不連續的。

## 例子：星系旋轉曲線
根據天文觀測，在像銀河系或仙女座星系這樣圍繞中心旋轉的許多螺旋星系中，可觀測到的質量大多集中在中心區域附近。然而，這些螺旋星系中物質的軌道速度與從可觀測質量分佈理論預測的值有很大差異，如下圖所示，在一定距離以外幾乎保持恆定。

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *圖片來源*
> - 作者：維基百科用戶 [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - 授權：公共領域

![Rotation Curve of Spiral Galaxy M33](https://upload.wikimedia.org/wikipedia/commons/c/cd/Rotation_curve_of_spiral_galaxy_Messier_33_%28Triangulum%29.png)
> **螺旋星系M33（三角座星系）的旋轉曲線**
> - 作者：維基媒體用戶 [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama)
> - 授權：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

讓我們預測星系質量集中在中心時距離對軌道速度的影響，並確認這種預測與觀測結果不符，然後證明星系中心距離 $R$ 內分佈的質量 $M(R)$ 必須與 $R$ 成正比才能解釋觀測結果。

首先，如果星系質量 $M$ 集中在中心，則距離 $R$ 處的軌道速度為：

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

在這種情況下，預測軌道速度會按 $1/\sqrt{R}$ 減小，如上圖中的虛線所示，但觀測結果表明軌道速度 $v$ 與距離 $R$ 無關且幾乎恆定，因此預測與觀測不符。這種觀測結果只有在 $M(R)\propto R$ 時才能解釋。

設比例常數為 $k$，則 $M(R) = kR$，

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(常數)}. $$

基於此，天體物理學家得出結論：許多星系中必定存在未被發現的「暗物質(dark matter)」，且這種暗物質必須佔宇宙質量的90%以上。不過，暗物質的本質至今尚未明確揭示，雖然不是主流理論，但也有像修正牛頓動力學(Modified Newtonian Dynamics, MOND)這樣不假設暗物質存在而試圖解釋觀測結果的嘗試。如今，這類研究領域處於天體物理學的最前沿。
