---
title: 重力場と重力ポテンシャル
description: ニュートンの万有引力の法則に基づく重力場ベクトルと重力ポテンシャルの定義を学び、関連する重要な二つの例として球殻定理と銀河回転曲線を扱う。
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - ニュートンの万有引力の法則：$\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - 連続的な質量分布と大きさを持つ物体の場合：$\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$：任意の原点から位置ベクトル$\mathbf{r^{\prime}}$にある点での質量密度
>   - $dv^{\prime}$：任意の原点から位置ベクトル$\mathbf{r^{\prime}}$にある点での体積要素
> - **重力場ベクトル（gravitational field vector）**：
>   - 質量$M$の物体によって生じた場の中で、ある一つの粒子が単位質量当たりに受ける力を表すベクトル
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - *単位質量当たりの力*または*加速度*の次元を持つ
> - **重力ポテンシャル（gravitational potential）**：
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - $($*単位質量当たりの力* $) \times ($*距離* $)$または*単位質量当たりのエネルギー*の次元を持つ
>   - $\Phi = -G\cfrac{M}{r}$
>   - 重力ポテンシャルはその相対的な差のみが意味を持ち、特定の値自体は意味がない
>   - 通常$r \to \infty$のとき$\Phi \to 0$という条件を任意に設定して不確実性（ambiguity）を除去する
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **球殻内部と外部の重力ポテンシャル（球殻定理）**
>   - $R>a$のとき：
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - 物質の球対称分布（spherical symmetric distribution）による外部のある点での重力ポテンシャルを求める際、その物体を質点（point mass）とみなして計算できる
>   - $R<b$のとき：
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - 球対称な質量殻の内側では重力ポテンシャルは位置に関係なく一定であり、作用する重力は$0$
>   - $b<R<a$のとき：$\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## 重力場
### ニュートンの万有引力の法則
ニュートンは11666 HE以前にすでに万有引力の法則を体系化し、数値的にも検証していた。それにもかかわらず、11687 HEに著書*Principia*で自分の結果を出版するまでには20年もかかった。その理由は、地球と月を大きさを持たない質点（point mass）と仮定して行った計算法を正当化することができなかったからである。幸いにも、[ニュートン自身がその後に発明した微積分学を使えば、11600年代当時のニュートンには簡単ではなかったその問題を私たちははるかに簡単に証明できる](#raのとき)。

ニュートンの万有引力の法則（Newton's law of universal gravitation）によれば、*各質量粒子は宇宙内の他のすべての粒子を引き寄せ、その力は二つの質量の積に比例し、その間の距離の二乗に反比例する。*数学的に表すと次のようになる。

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *画像出典*
> - 作者：ウィキメディアユーザー [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - ライセンス：[CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

単位ベクトル$\mathbf{e}_r$は$M$から$m$の方向を向き、マイナス記号は力が引力であることを示す。つまり、$m$は$M$の方向に引かれる。

### キャベンディッシュの実験
この法則の実験的な検証と$G$値の決定は、11798 HEにイギリスの物理学者ヘンリー・キャベンディッシュ（Henry Cavendish）によって行われた。キャベンディッシュの実験は、軽い棒の両端に固定された二つの小さな球からなるねじれ天秤を使用する。その二つの球はそれぞれ、その近くに位置する他の二つの大きな球の方向に引かれる。現在までに求められた公式の$G$値は$6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$である。

> $G$は最も古くから知られていた基本定数であるにもかかわらず、$e$、$c$、$\hbar$などの他のほとんどの基本定数よりも低い精度（precision）でしか知られていない。今日でも$G$値をより高い精度で求めようとする多くの研究が行われている。
{: .prompt-tip }

### 大きさを持つ物体の場合
式（$\ref{eqn:law_of_gravitation}$）の法則は厳密には*点粒子（point particle）*に対してのみ適用できる。もしどちらか一方または両方がある大きさを持つ物体である場合には、力を計算するために重力場（gravitational force field）が*線形場（linear field）*であるという仮定を追加する必要がある。つまり、質量が$m$である一つの粒子が他の複数の粒子から受ける総重力は、各力のベクトルを合計することによって求めることができると仮定する。物質が連続的に分布する物体の場合には、合計を次のように積分に置き換える。

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$：任意の原点から位置ベクトル$\mathbf{r^{\prime}}$にある点での質量密度
- $dv^{\prime}$：任意の原点から位置ベクトル$\mathbf{r^{\prime}}$にある点での体積要素

もし質量$M$の物体と質量$m$の物体がともに大きさを持つ場合に全体の重力を求めようとする場合、$m$に対する二番目の体積積分も必要となる。

### 重力場ベクトル
**重力場ベクトル（gravitational field vector）** $\mathbf{g}$は、質量$M$の物体によって生じた場の中で、ある一つの粒子が単位質量当たりに受ける力を表すベクトルと定義して

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

または

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

と表す。ここで$\mathbf{e}_r$の方向は$\mathbf{r^\prime}$によって異なる。

この量$\mathbf{g}$は*単位質量当たりの力*または*加速度*の次元を持つ。地球表面付近での重力場ベクトル$\mathbf{g}$の大きさはすなわち我々が**重力加速度定数（gravitational acceleration constant）**と呼ぶ量と同じであり、$\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$である。

## 重力ポテンシャル
### 定義
重力場ベクトル$\mathbf{g}$は$1/r^2$で変化し、したがってあるスカラー関数（ポテンシャル）の勾配（gradient）として表現するための条件（$\nabla \times \mathbf{g} \equiv 0$）を満たす。そのため、次のように書くことができる。

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

ここで$\Phi$を**重力ポテンシャル（gravitational potential）**と呼び、$($*単位質量当たりの力* $) \times ($*距離* $)$または*単位質量当たりのエネルギー*の次元を持つ。

$\mathbf{g}$は半径のみに依存するため、$\Phi$も$r$に従って変化する。式（$\ref{eqn:g_vector}$）と（$\ref{eqn:gradient_phi}$）から

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

となり、これを積分すると

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

を得る。重力ポテンシャルはその相対的な差のみが意味を持ち、特定の値自体は意味がないため、積分定数は省略できる。通常$r \to \infty$のとき$\Phi \to 0$という条件を任意に設定して不確実性（ambiguity）を除去し、式（$\ref{eqn:g_potential}$）もこの条件を満たす。

物質が連続的に分布する場合の重力ポテンシャルは次のようになる。

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

質量が薄い殻に表面分布する場合には

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

そして線密度$\rho_l$の線形質量源の場合には次のように書くことができる。

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### 物理的意味
物体が重力場の中で$d\mathbf{r}$だけ移動するとき、その物体が行う単位質量当たりの仕事$dW^\prime$を考えてみよう。

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

この式で$\Phi$は位置座標のみの関数で、$\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$と表される。したがって、重力場の中で物体をある一点から別の一点まで移動させるとき、その物体が行う単位質量当たりの仕事の量はその二点のポテンシャルの差と等しいことがわかる。

無限に遠い場所での重力ポテンシャルを$0$と定義すると、任意の点での$\Phi$はその物体を無限に遠い場所からその点まで移動させるのに必要な単位質量当たりの仕事として解釈できる。物体のポテンシャルエネルギーはその物体の質量と重力ポテンシャル$\Phi$の積に等しいので、$U$をポテンシャルエネルギーとすると

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

したがって、物体が受ける重力はその物体のポテンシャルエネルギーの勾配にマイナス記号を付けて得られる。

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

物体がある質量によって生じた重力場の中に置かれているときは、常にあるポテンシャルエネルギーが生じる。このポテンシャルエネルギーは厳密には場自体にあるものだが、慣例的にこれをその物体のポテンシャルエネルギーと表現することがある。

## 例題：球殻内部と外部の重力ポテンシャル（球殻定理）
### 座標設定＆積分式で重力ポテンシャルを表現する
内側半径が$b$、外側半径が$a$の均一な球殻（spherical shell）の内部と外部の重力ポテンシャルを求めてみよう。球殻による重力は場の中の単位質量に作用する力の成分を直接計算して得ることもできるが、ポテンシャル法を使う方が簡単である。

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

上の図で中心からの距離$R$にある$P$点でのポテンシャルを計算しよう。殻の均一質量分布を仮定すると$\rho(r^\prime)=\rho$であり、球の中心と点$P$を結ぶ線を基準として方位角$\phi$に関して対称なので

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

余弦定理によれば

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

であり、$R$は一定なので、$r^\prime$についてこの式を微分すると

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

を得る。これを式（$\ref{eqn:spherical_shell_1}$）に代入すると

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

ここで$r_\mathrm{max}$と$r_\mathrm{min}$は点$P$の位置によって決まる。

### $R>a$のとき
$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

球殻の質量$M$は

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

で与えられるので、ポテンシャルは次のようになる。

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> 質量が$M$の質点による重力ポテンシャル式（$\ref{eqn:g_potential}$）と今得られた結果（$\ref{eqn:spherical_shell_outside_2}$）を比較してみると同一であることがわかる。これはすなわち、物質の球対称分布（spherical symmetric distribution）による外部のある点での重力ポテンシャルを求めるとき、すべての質量が中心に集中していると考えても構わないということである。地球や月のような一定の大きさ以上の球形天体のほとんどがこれに該当するが、これらは[マトリョーシカ](https://en.wikipedia.org/wiki/Matryoshka_doll)のように中心が同じで互いに異なる直径を持つ無数の球殻が重なっているものとみなすことができる。これはこの記事の冒頭で言及した[地球や月のような天体を大きさを持たない質点と仮定して計算しても妥当な根拠](#ニュートンの万有引力の法則)となる。
{: .prompt-info }

### $R<b$のとき
$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> 球対称な質量殻の内側では重力ポテンシャルは位置に関係なく一定であり、作用する重力は$0$である。
{: .prompt-info }

> そしてこれは代表的な疑似科学の一つである「地球空洞説」がデタラメである主な根拠でもある。地球空洞説で主張されているように地球が球殻の形をしていて内部が空洞であれば、その空洞内部にあるすべての物体に対して地球の重力は作用しない。地球の質量と体積を考えると地球空洞があり得ないのはもちろん、仮にあったとしてもそこの生命体は球殻の内側を地面として生活するのではなく、宇宙ステーションのように無重力状態で漂うことになる。  
> [地下数km程度の地層の奥深くに微生物が生息している可能性はあるが](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3)、少なくとも地球空洞説で主張されているような形では不可能である。ジュール・ヴェルヌの小説《地底旅行（Voyage au centre de la Terre）》と映画「センター・オブ・ジ・アース（Journey to the Center of the Earth）」は私も大好きだが、創作物は創作物として楽しむべきで、それを真剣に信じるべきではない。
{: .prompt-tip }

### $b<R<a$のとき
$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### 結果
先ほど求めた三つの領域での重力ポテンシャル$\Phi$、そしてそれに伴う重力場ベクトルの大きさ$\|\mathbf{g}\|$を距離$R$の関数としてグラフで表すと次のようになる。

![Gravitational Potential as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-gravitational-potential.png)
![Magnitude of the Field Vector as a Function of R](https://raw.githubusercontent.com/yunseo-kim/physics-visualization/refs/heads/main/figs/shell-theorem-field-vector.png)
> - Python可視化コード：[yunseo-kim/physics-visualization リポジトリ](https://github.com/yunseo-kim/physics-visualization/blob/main/src/shell_theorem.py)
> - ライセンス：[こちらを参照](https://github.com/yunseo-kim/physics-visualization?tab=readme-ov-file#license)

重力ポテンシャルと重力場ベクトルの大きさは連続的であることがわかる。もし重力ポテンシャルがある点で不連続であれば、その点でのポテンシャルの勾配、つまり重力の大きさがその点で無限大になるが、これは物理的に妥当ではないためポテンシャル関数はすべての点で連続でなければならない。しかし、重力場ベクトルの*微分係数*は殻の内側面と外側面で不連続である。

## 例題：銀河回転曲線
天文学的観測によれば、我々の銀河やアンドロメダ銀河のように中心に対して回転する多くの渦巻銀河内の観測可能な質量のほとんどは中心部付近に集中的に分布している。しかし、このような渦巻銀河内の質量の軌道速度は、次のグラフで確認できるように観測可能な質量分布から理論的に予測した値と大きく一致せず、一定距離以上ではほぼ一定である。

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *画像出典*
> - 作者：ウィキペディアユーザー [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - ライセンス：Public Domain

![Rotation Curve of Spiral Galaxy M33](https://upload.wikimedia.org/wikipedia/commons/c/cd/Rotation_curve_of_spiral_galaxy_Messier_33_%28Triangulum%29.png)
> **渦巻銀河M33（さんかく座銀河）の回転曲線**
> - 作者：ウィキメディアユーザー [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama)
> - ライセンス：[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)

銀河の質量が中心部に集中している場合の距離に応じた軌道速度を予測し、その予測値がこのような観測結果と一致しないことを確認し、銀河中心からの距離$R$以内に分布する質量$M(R)$が$R$に比例しなければならないことを示そう。

まず銀河質量$M$が中心部に集中している場合、距離$R$での軌道速度を求めると次のようになる。

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

この場合、上の二つのグラフに示されている点線のように$1/\sqrt{R}$で減少する軌道速度が予測されるが、観測結果によれば軌道速度$v$は距離$R$に関係なくほぼ一定であるため、予測と観測結果が一致しない。このような観測結果は$M(R)\propto R$でなければ説明できない。

比例定数$k$を用いて$M(R) = kR$とおくと、

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{（定数）}. $$

これから天体物理学者たちは、多くの銀河には発見されていない「暗黒物質（dark matter）」が必ず存在し、このような暗黒物質が宇宙質量の90％以上を占めなければならないという結論を導く。ただし暗黒物質の正体はまだ明確に解明されておらず、主流の理論ではないが、暗黒物質の存在を仮定せずに観測結果を説明しようとする修正ニュートン力学（Modified Newtonian Dynamics, MOND）のような試みも存在する。今日、このような研究分野は天体物理学の最前線に接している。
