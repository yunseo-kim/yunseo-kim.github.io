---
title: "Posloupnosti a řady"
description: "Probereme základní pojmy z kalkulu: definici posloupností a řad, jejich konvergenci a divergenci, a také definici čísla e jako základu přirozeného logaritmu."
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## Posloupnosti
**Posloupnost (sequence)**, se kterou se v kalkulu pracuje, obvykle znamená nekonečnou posloupnost. Jinými slovy, posloupnost je funkce definovaná na množině všech **přirozených čísel (natural number)**

$$ \mathbb{N} := \{1,2,3,\dots\} $$

.* Pokud jsou hodnoty této funkce reálná čísla (real number), mluvíme o „reálné posloupnosti“, pokud jsou to komplexní čísla (complex number), o „komplexní posloupnosti“, pokud jsou to body (point), o „posloupnosti bodů“, pokud jsou to matice (matrix), o „posloupnosti matic“, pokud jsou to funkce (function), o „posloupnosti funkcí“, pokud jsou to množiny (set), o „posloupnosti množin“ atd. Všechna tato označení však lze zjednodušeně shrnout jako „posloupnost“.

Obvykle pro **těleso reálných čísel (the field of real numbers)** $\mathbb{R}$, u posloupnosti $\mathbf{a}: \mathbb{N} \to \mathbb{R}$ klademe

$$ a_1 := \mathbf{a}(1), \quad a_2 := \mathbf{a}(2), \quad a_3 := \mathbf{a}(3) $$

apod. a tuto posloupnost zapisujeme jako

$$ a_1,\, a_2,\, a_3,\, \dots $$

nebo

$$ \begin{gather*}
(a_1,a_2,a_3,\dots), \\
(a_n: n=1,2,3,\dots), \\
(a_n)_{n=1}^{\infty}, \qquad (a_n)
\end{gather*} $$

atd.

> *Při definování posloupnosti lze místo oboru přirozených čísel $\mathbb{N}$ vzít množinu celých čísel nezáporných
>
> $$ \mathbb{N}_0 := \{0\} \cup \mathbb{N} = \{0,1,2,\dots\} $$
>
> nebo
>
> $$\{2,3,4,\dots \}$$
>
> apod. Například při studiu teorie mocninných řad je přirozenější, když je oborem definice $\mathbb{N}_0$.
{: .prompt-info }

## Konvergence a divergence
Jestliže posloupnost $(a_n)$ konverguje k reálnému číslu $l$, píšeme

$$ \lim_{n\to \infty} a_n = l $$

a číslo $l$ se nazývá **limita** posloupnosti $(a_n)$.

> Přísná definice pomocí **epsilon-delta argumentu (epsilon-delta argument)** je následující.
>
> $$ \lim_{n\to \infty} a_n = l \overset{def}\Longleftrightarrow \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |a_n - l| < \epsilon) $$
>
> Tj. pro libovolně malé kladné $\epsilon$ vždy existuje přirozené číslo $N$ takové, že pro $n>N$ platí $\|a_n - l \| < \epsilon$. To znamená, že pro dostatečně velká $n$ se rozdíl mezi $a_n$ a $l$ stává libovolně malým; posloupnost $(a_n)$ pak podle definice konverguje k reálnému číslu $l$.
{: .prompt-info }

Posloupnost, která nekonverguje, se nazývá **divergentní**. *Konvergence či divergence posloupnosti se nezmění, i když změníme konečný počet jejích členů.*

Pokud jednotlivé členy posloupnosti $(a_n)$ rostou bez omezení, píšeme

$$ \lim_{n\to \infty} a_n = \infty $$

a říkáme, že *diverguje k plus nekonečnu*. Podobně, pokud členy posloupnosti $(a_n)$ klesají bez omezení, píšeme

$$ \lim_{n\to \infty} a_n = -\infty $$

a říkáme, že *diverguje k minus nekonečnu*.

## Základní vlastnosti konvergentních posloupností
Jestliže posloupnosti $(a_n)$ a $(b_n)$ obě konvergují (tj. mají limitu), potom posloupnosti $(a_n + b_n)$ a $(a_n \cdot b_n)$ také konvergují a platí

$$ \lim_{n\to \infty} (a_n + b_n) = \lim_{n\to \infty} a_n + \lim_{n\to \infty} b_n \label{eqn:props_of_conv_series_1}\tag{1}$$

$$ \lim_{n\to \infty} (a_n \cdot b_n) = \left(\lim_{n\to \infty} a_n \right) \cdot \left(\lim_{n\to \infty} b_n \right) \label{eqn:props_of_conv_series_2}\tag{2}$$

Dále pro libovolné reálné číslo $t$ platí

$$ \lim_{n\to \infty} (t a_n) = t\left(\lim_{n\to \infty} a_n \right) \label{eqn:props_of_conv_series_3}\tag{3}$$

Tyto vlastnosti se nazývají **základní vlastnosti konvergentních posloupností** nebo také **základní vlastnosti limity**.

## Základ přirozeného logaritmu $e$
**Základ přirozeného logaritmu** je definován jako

$$ e := \lim_{n\to \infty} \left(1+\frac{1}{n} \right)^n \approx 2.718 $$

Jde o jednu z nejdůležitějších konstant v matematice.

> Zvláštností je, že prakticky jen v Koreji se poměrně často používá výraz „přirozená konstanta“, avšak nejde o standardní termín. Korejská matematická společnost uvádí v oficiálním slovníku jako termín ['základ přirozeného logaritmu'](https://www.kms.or.kr/mathdict/list.html?key=kname&keyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8%EC%9D%98+%EB%B0%91) a výraz „přirozená konstanta“ se v něm vůbec nevyskytuje. Dokonce ani ve standardním slovníku Národního institutu korejského jazyka nelze heslo „přirozená konstanta“ najít; ve [slovníkovém výkladu k „přirozenému logaritmu“](https://stdict.korean.go.kr/search/searchView.do?pageSize=10&searchKeyword=%EC%9E%90%EC%97%B0%EB%A1%9C%EA%B7%B8) se pouze uvádí „určité číslo, které se často značí e“.  
> Ani v anglicky mluvících zemích a v Japonsku pro to neexistuje přímý odpovídající termín; v angličtině se obvykle používá „the base of the natural logarithm“, zkráceně „natural base“, případně „Euler's number“ nebo „the number $e$“.  
> Jelikož původ je nejasný, Korejská matematická společnost to nikdy neuznala jako oficiální termín a mimo Koreu se to prakticky nikde nepoužívá, není žádný důvod na takovém názvu trvat. Proto zde dál budu používat označení „základ přirozeného logaritmu“, případně prostě $e$.
{: .prompt-tip }

## Řady
Pro posloupnost

$$ \mathbf{a} = (a_1, a_2, a_3, \dots) $$

nazveme **řadou** posloupnosti $\mathbf{a}$ jinou posloupnost tvořenou jejími částečnými součty

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

Řadu posloupnosti $(a_n)$ zapisujeme například jako

$$ \begin{gather*}
a_1 + a_2 + a_3 + \cdots, \qquad \sum_{n=1}^{\infty}a_n, \\
\sum_{n\geq 1} a_n, \qquad \sum_n a_n, \qquad \sum a_n 
\end{gather*} $$

atd.

## Konvergence a divergence řad
Řada získaná z posloupnosti $(a_n)$,

$$ a_1, \quad a_1 + a_2, \quad a_1 + a_2 + a_3, \quad \dots $$

konverguje k nějakému reálnému číslu $l$, jestliže

$$ \sum_{n=1}^{\infty} a_n = l $$

V tomto případě se limita $l$ nazývá **součet** řady $\sum a_n$. Symbol

$$ \sum a_n $$

může podle kontextu označovat buď <u>řadu</u>, nebo její <u>součet</u>.

Řada, která nekonverguje, se nazývá **divergentní**.

## Základní vlastnosti konvergentních řad
Ze [základních vlastností konvergentních posloupností](#základní-vlastnosti-konvergentních-posloupností) plyne následující: pro reálné číslo $t$ a dvě konvergentní řady $\sum a_n$, $\sum b_n$ platí

$$ \sum(a_n + b_n) = \sum a_n + \sum b_n, \qquad \sum ta_n = t\sum a_n \tag{4}$$

Konvergence řady není ovlivněna změnou konečného počtu členů. Tj. pro dvě posloupnosti $(a_n)$, $(b_n)$: pokud pro všechna $n$ až na konečně mnoho výjimek platí $a_n=b_n$, pak řada $\sum a_n$ konverguje právě tehdy, když konverguje řada $\sum b_n$.
