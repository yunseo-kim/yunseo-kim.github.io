---
title: Princip relativity a Lorentzova transformace
description: Probereme pojem vztažné soustavy a Galileiho transformaci, která se široce používala v klasické mechanice. Stručně se také podíváme na Maxwellovy rovnice a Michelsonův–Morleyův experiment, jež vedly k zavedení Lorentzovy transformace, a odvodíme její transformační matici.
categories: [Physics, Modern Physics]
tags: [Theory of Relativity, Linear Transformation, Lorentz transformation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **Princip relativity**: princip, podle něhož musí být všechny fyzikální zákony stejné ve všech vztažných soustavách pohybujících se vůči sobě rovnoměrným přímočarým pohybem
{: .prompt-info }

> **Lorentzův faktor $\gamma$**
>
> $$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} $$
{: .prompt-info }

> **Lorentzova transformace**
>
> $$ \begin{pmatrix}
> \vec{x}^\prime \\ ct^\prime
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & -\gamma\vec{\beta} \\
> -\gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}. $$
>
> - $ \vec{x^\prime} = \gamma\vec{x}-\gamma\vec{\beta}ct $
> - $ ct^\prime = \gamma ct - \gamma \vec{\beta}\cdot\vec{x} $
{: .prompt-info }

> **Inverzní Lorentzova transformace**
>
> $$ \begin{pmatrix}
> \vec{x} \\ ct
> \end{pmatrix}
> = \begin{pmatrix}
> \gamma & \gamma\vec{\beta} \\
> \gamma\vec{\beta} & \gamma
> \end{pmatrix}
> \begin{pmatrix}
> \vec{x^\prime} \\ ct^\prime
> \end{pmatrix}. $$
>
> - $ \vec{x} = \gamma\vec{x^\prime}+\gamma\vec{\beta}ct^\prime $
> - $ ct = \gamma ct^\prime + \gamma \vec{\beta}\cdot\vec{x^\prime} $
{: .prompt-info }

## Vztažná soustava a princip relativity
### Vztažná soustava (frame of reference)
- **Vztažná soustava (frame of reference)**: skutečnost, že se nějaké těleso „pohybuje“, znamená, že se jeho poloha relativně mění vůči jinému tělesu. Jelikož je veškerý pohyb relativní, je pro popis pohybu nutné zvolit vztažnou soustavu, která slouží jako referenční rámec.
- **Inerciální vztažná soustava (inertial frames of reference)**: soustava, ve které platí Newtonův (Newton) 1. zákon pohybu („Pokud je výsledná síla působící na těleso nulová, jeho pohybový stav se nemění.“). Každá vztažná soustava, která se vůči nějaké inerciální soustavě pohybuje rovnoměrně, je také inerciální.

### Princip relativity (Principle of Relativity)
Jde o jeden z klíčových pojmů fyziky a základní předpoklad: všechny fyzikální zákony musí mít stejnou podobu ve všech vztažných soustavách, které se vůči sobě pohybují rovnoměrně. Pokud by se fyzikální zákony pro pozorovatele v relativním pohybu lišily, bylo by možné tento rozdíl využít k zavedení jedné absolutní vztažné soustavy a určit, kdo je v klidu a kdo v pohybu. Podle principu relativity však takové rozlišení neexistuje: neexistuje absolutní vztažná soustava pro celý vesmír ani absolutní pohyb a všechny inerciální soustavy jsou rovnocenné.

## Omezení Galileiho transformace
### Galileiho transformace (Galilean transformation)
Uvažujme dvě inerciální soustavy $S$ a $S^{\prime}$. Nechť se $S^{\prime}$ vzhledem k $S$ pohybuje konstantní rychlostí $\vec{v}$ ve směru $+x$ a tentýž jev (událost) je v $S$ pozorován v čase $t$ v souřadnicích $(x, y, z)$, zatímco v $S^{\prime}$ v čase $t^{\prime}$ v souřadnicích $(x^{\prime}, y^{\prime}, z^{\prime})$.

Protože hodnota souřadnice v ose $x$ měřená v $S^{\prime}$ bude o dráhu $\vec{v}t$, kterou se $S^{\prime}$ vůči $S$ posunula ve směru $x$, menší než hodnota měřená v $S$, platí

$$ x^{\prime} = x - \vec{v}t \label{eqn:galilean_transform_x} \tag{1} $$

a jelikož ve směrech $y$ a $z$ nedochází k relativnímu pohybu,

$$ \begin{align*}
y^{\prime} = y \label{eqn:galilean_transform_y} \tag{2} \\
z^{\prime} = z \label{eqn:galilean_transform_z} \tag{3}
\end{align*} $$

a intuitivně lze předpokládat

$$ t^{\prime} = t \tag{4} \label{eqn:galilean_transform_t}$$

Souřadnicová transformace mezi dvěma inerciálními soustavami, která se v klasické fyzice tradičně používala ve tvaru od ($\ref{eqn:galilean_transform_x}$) do ($\ref{eqn:galilean_transform_t}$), se nazývá **Galileiho transformace (Galilean transformation)**. Je jednoduchá a intuitivní, protože ve většině každodenních situací funguje. Jak ale uvidíme dále, je v rozporu s Maxwellovými rovnicemi.

### Maxwellovy rovnice
Maxwell (Maxwell) koncem 11800. let rozšířil myšlenky a výsledky předchozích výzkumů dalších vědců, jako byli Faraday (Faraday) a Ampere (Ampere), a ukázal, že elektřina a magnetismus jsou ve skutečnosti projevy téže interakce. Odvodil následující čtyři rovnice popisující elektromagnetické pole.

1. $$\begin{gather*}\nabla\cdot{E}=\frac{q}{\epsilon_0} \\
 \text{: Elektrický tok libovolnou uzavřenou plochou se rovná celkovému náboji uvnitř (Gaussův zákon).}
 \end{gather*}$$
2. $$\begin{gather*}\nabla\cdot{B}=0 \\
\text{: Magnetické monopóly (magnetický náboj) neexistují.}
\end{gather*}$$
3. $$\begin{gather*}\nabla\times{E}=-\frac{\partial B}{\partial t} \\
\text{: Změna magnetického pole vytváří elektrické pole (Faradayův zákon).}
\end{gather*}$$
4. $$\begin{gather*}\nabla\times{B}=\mu_0\left(J+\epsilon_0\frac{\partial E}{\partial t}\right) \\
\text{: Změna elektrického pole a elektrický proud vytvářejí magnetické pole (Ampèrův–Maxwellův zákon).}
\end{gather*}$$

Maxwellovy rovnice dokázaly úspěšně vysvětlit všechny tehdy známé elektrické a magnetické jevy, předpověděly existenci elektromagnetických vln a zároveň odvodily, že rychlost elektromagnetických vln ve vakuu $c$ je neměnná konstanta. Staly se tak klíčovým vztahem elektromagnetismu.

### Rozpor mezi Galileiho transformací a Maxwellovými rovnicemi
Newtonovská mechanika používající Galileiho transformaci byla více než 200 let základem fyziky a Maxwellovy rovnice jsou, jak bylo uvedeno, základními rovnicemi popisujícími elektrické a magnetické jevy. Mezi těmito dvěma teoriemi však vzniká následující rozpor:

- Podle principu relativity bychom očekávali, že i Maxwellovy rovnice budou mít ve všech inerciálních soustavách stejný tvar, ale pokud veličiny naměřené v jedné inerciální soustavě převedeme pomocí Galileiho transformace na veličiny v jiné soustavě, Maxwellovy rovnice získají velmi odlišnou podobu.
- Z Maxwellových rovnic lze spočítat velikost rychlosti světla $c$ a ta je neměnnou konstantou, avšak podle Newtonovy mechaniky a Galileiho transformace se rychlost světla $c$ mění v závislosti na vztažné soustavě.

Proto si Maxwellovy rovnice a Galileiho transformace navzájem neodpovídají a alespoň jednu z nich bylo nutné upravit. To se stalo motivací pro zavedení **Lorentzovy transformace (Lorentz transformation)**, o níž bude řeč dále.

## Teorie éteru (aether) a Michelsonův–Morleyův experiment
Ve fyzice 11800. let se mezitím předpokládalo, že i světlo se—podobně jako vlny na hladině či zvuk—šíří prostřednictvím hypotetického média zvaného *éter (aether)*, a fyzikové se snažili jeho existenci prokázat.

Podle éterové teorie je vesmírný prostor i ve vakuu vyplněn éterem, takže díky oběhu Země kolem Slunce rychlostí asi 30 km/s měl vznikat „éterový vítr“ vanoucí napříč Zemí.  
![Aether Wind](https://upload.wikimedia.org/wikipedia/commons/f/fc/AetherWind.svg)
> *Zdroj obrázku*
> - autor: uživatel Wikimedia [Cronholm144](https://commons.wikimedia.org/wiki/User:Cronholm144)
> - licence: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

Aby tuto hypotézu ověřil, provedl Michelson (Michelson) v roce 11887 [Holocénního kalendáře](https://en.wikipedia.org/wiki/Holocene_calendar) ve spolupráci s Morleyem (Morley) *Michelsonův–Morleyův experiment (Michelson-Morley Experiment)* s použitím níže uvedeného interferometru.  
![Michelsonův–Morleyův interferometr](https://upload.wikimedia.org/wikipedia/commons/f/fb/On_the_Relative_Motion_of_the_Earth_and_the_Luminiferous_Ether_-_Fig_4.png)
> *Zdroj obrázku*
> - autor: Albert Abraham Michelson with Edward Morley
> - licence: public domain

V tomto experimentu prochází světelný paprsek polopropustným zrcadlem, kde se rozdělí na dva paprsky. Každý z nich se odráží tam a zpět ve dvou na sebe kolmých ramenech interferometru, celkem urazí zhruba 11 m, a poté se znovu setkají ve středním bodě. Podle fázového rozdílu obou paprsků se objeví buď konstruktivní, nebo destruktivní interferenční obrazec. Éterová teorie předpovídala, že v závislosti na rychlosti vůči éteru se rychlost světla bude lišit, a tím se změní i fázový rozdíl, takže bude možné pozorovat posun interferenčních proužků. Ve skutečnosti však žádnou změnu interferenčního obrazce pozorovat nešlo. Pro vysvětlení výsledku se objevilo více pokusů; mimo jiné FitzGerald (FitzGerald) a Lorentz (Lorentz) navrhli, že pokud se těleso <u>relativně pohybuje vůči éteru</u>, zkracuje se jeho délka — tzv. *Lorentzovo–FitzGeraldovo zkrácení (Lorentz–FitzGerald contraction)* neboli *délková kontrakce (length contraction)*. Tato myšlenka vedla k Lorentzově transformaci.

> Lorentz v té době věřil, že éter existuje, a domníval se, že ke kontrakci délky dochází v důsledku relativního pohybu vůči éteru. Později Einstein (Einstein) v *teorii speciální relativity (Theory of Special Relativity)* vyložil skutečný fyzikální význam Lorentzovy transformace: délkovou kontrakci vysvětlil nikoli éterem, ale pojmem časoprostoru; zároveň se později ukázalo, že éter neexistuje.
{: .prompt-info }

## Lorentzova transformace (Lorentz transformation)
### Odvození Lorentzovy transformace
Uvažujme stejnou situaci jako u Galileiho transformace (rovnice [$\ref{eqn:galilean_transform_x}$]-[$\ref{eqn:galilean_transform_t}$]) a předpokládejme, že správný transformační vztah mezi $x$ a $x^{\prime}$, který není v rozporu s Maxwellovými rovnicemi, má tvar

$$ x^{\prime} = \gamma(x-\vec{v}t). \label{eqn:lorentz_transform_x}\tag{5}$$

Zde $\gamma$ nezávisí na $x$ ani $t$, může však být funkcí $\vec{v}$. Důvody pro tento předpoklad jsou následující:

- Aby události v $S$ a $S^{\prime}$ odpovídaly jednoznačně jedna druhé, musí být $x$ a $x^{\prime}$ v lineárním vztahu.
- Je známo, že Galileiho transformace je správná pro mechaniku v běžných situacích, takže musí být možné ji aproximovat rovnicí ($\ref{eqn:galilean_transform_x}$).
- Tvar by měl být pokud možno jednoduchý.

Fyzikální vztahy musí mít v soustavách $S$ a $S^{\prime}$ stejnou formu, takže pokud chceme vyjádřit $x$ pomocí $x^{\prime}$ a $t$, stačí změnit znaménko $\vec{v}$ (směr relativního pohybu). Jelikož mezi oběma soustavami nesmí být žádný jiný rozdíl než znaménko $\vec{v}$, musí být $\gamma$ stejné.

$$ x = \gamma(x^{\prime}+\vec{v}t^{\prime}). \label{eqn:lorentz_transform_x_inverse}\tag{6}$$

Stejně jako u Galileiho transformace není důvod, aby se lišily složky kolmé na směr $\vec{v}$, tedy $y$ a $y^{\prime}$, resp. $z$ a $z^{\prime}$, proto položíme

$$ \begin{align*}
y^{\prime} &= y \\
z^{\prime} &= z
\end{align*} \label{eqn:lorentz_transform_yz} \tag{7}$$

Nyní dosadíme ($\ref{eqn:lorentz_transform_x}$) do ($\ref{eqn:lorentz_transform_x_inverse}$):

$$ x = \gamma^2 x - \gamma^2 \vec{v}t + \gamma \vec{v}t^{\prime} $$

a po úpravě na $t^{\prime}$ dostaneme

$$ t^{\prime} = \gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)x \label{eqn:lorentz_transform_t} \tag{8} $$

Abychom nebyli v rozporu s Maxwellovými rovnicemi, musí být rychlost světla v obou soustavách stejná, tj. $c$; toho využijeme k určení $\gamma$. Předpokládejme, že v čase $t=0$ byly počátky obou soustav na stejném místě; z této počáteční podmínky plyne $t^\prime = 0$. Nyní si představme, že v okamžiku $t=t^\prime=0$ došlo ve společném počátku soustav $S$ a $S^\prime$ k záblesku a pozorovatelé v obou soustavách měří rychlost tohoto světla. V soustavě $S$ pak platí

$$ x = ct \label{eqn:ct_S}\tag{9}$$

a v soustavě $S^\prime$

$$ x^\prime = ct^\prime \label{eqn:ct_S_prime}\tag{10}$$

Pomocí ($\ref{eqn:lorentz_transform_x}$) a ($\ref{eqn:lorentz_transform_t}$) dosadíme za $x$ a $t$:

$$ \gamma (x-\vec{v}t) = c\gamma t + \left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)cx $$

Tuto rovnici vyřešíme pro $x$:

$$ \left[\gamma-\left(\frac{1-\gamma^2}{\gamma \vec{v}}\right)c \right]x = c\gamma t + \vec{v}\gamma t$$

$$ \begin{align*}
x &= \cfrac{c\gamma t + \vec{v}\gamma}{\gamma-\left(\cfrac{1-\gamma^2}{\gamma \vec{v}}\right)c} \\
&= ct\left[ \cfrac{\gamma + \cfrac{\vec{v}}{c}\gamma}{\gamma - \left( \cfrac{1-\gamma^2}{\gamma \vec{v}} \right)c} \right] \\
&= ct\left[ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} \right]
\end{align*} $$

Protože ale v ($\ref{eqn:ct_S}$) platí $x=ct$, musí být

$$ \cfrac{1 + \cfrac{\vec{v}}{c}}{1 - \left( \cfrac{1}{\gamma^2}-1 \right)\cfrac{c}{\vec{v}}} = 1 $$

a tedy

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}} \label{lorentz_factor}\tag{11} $$

Dosazením tohoto vztahu pro $\gamma(\vec{v})$ do ($\ref{eqn:lorentz_transform_x}$), ($\ref{eqn:lorentz_transform_yz}$) a ($\ref{eqn:lorentz_transform_t}$) nakonec získáme transformační rovnice z $S$ do $S^\prime$.

### Transformační matice Lorentzovy transformace

Konečné transformační vztahy získané výše jsou následující:

- $$ x^\prime = \frac{x-\vec{v}t}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_x_fin}\tag{12}$$
- $$ y^\prime = y \label{eqn:lorentz_transform_y_fin}\tag{13}$$
- $$ z^\prime = z \label{eqn:lorentz_transform_z_fin}\tag{14}$$
- $$ t^\prime = \frac{t-\cfrac{\vec{v}x}{c^2}}{\sqrt{1-v^2/c^2}} \label{eqn:lorentz_transform_t_fin}\tag{15}$$

Tyto rovnice tvoří **Lorentzovu transformaci (Lorentz transformation)**. Položíme-li $\vec{\beta}=\vec{v}/c$, lze ji zapsat maticově takto:

$$ \begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix} 
= \begin{pmatrix}
\gamma & 0 & 0 & -\gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}. \label{lorentz_transform_matrix}\tag{16}$$

Lorentz (Lorentz) ukázal, že při použití této transformace mají základní rovnice elektromagnetismu ve všech inerciálních soustavách stejný tvar. Zároveň lze ověřit, že pokud je rychlost $v$ ve srovnání s rychlostí světla $c$ velmi malá, pak $\gamma \to 1$ a Lorentzova transformace se aproximuje Galileiho transformací.

### Inverzní Lorentzova transformace (inverse Lorentz transformation)
Někdy je výhodnější převádět měření v pohybující se soustavě $S^\prime$ na měření v klidové soustavě $S$ (na rozdíl od převodu z $S$ do $S^\prime$).
V takovém případě lze použít **inverzní Lorentzovu transformaci (inverse Lorentz transformation)**.  
Vypočtením inverzní matice k ($\ref{lorentz_transform_matrix}$) získáme následující matici inverzní Lorentzovy transformace:

$$ \begin{pmatrix}
x_1 \\ x_2 \\ x_3 \\ ct
\end{pmatrix}
= \begin{pmatrix}
\gamma & 0 & 0 & \gamma\vec{\beta} \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\gamma\vec{\beta} & 0 & 0 & \gamma
\end{pmatrix}
\begin{pmatrix}
x_1^\prime \\ x_2^\prime \\ x_3^\prime \\ ct^\prime
\end{pmatrix}. \tag{17}
$$

Je to totéž jako v rovnicích ($\ref{eqn:lorentz_transform_x_fin}$)-($\ref{eqn:lorentz_transform_t_fin}$) prohodit veličiny s primem a bez prima a nahradit $v$ hodnotou $-v$ (tj. $\beta$ hodnotou $-\beta$).

- $$ x = \frac{x^\prime+\vec{v}t^\prime}{\sqrt{1-v^2/c^2}} \tag{18}$$
- $$ y = y^\prime \tag{19}$$
- $$ z = z^\prime \tag{20}$$
- $$ t = \frac{t^\prime+\cfrac{\vec{v}x^\prime}{c^2}}{\sqrt{1-v^2/c^2}} \tag{21}$$
