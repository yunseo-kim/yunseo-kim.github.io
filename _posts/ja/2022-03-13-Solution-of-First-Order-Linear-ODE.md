---
title: "1階線形常微分方程式の解法"
description: "1階線形常微分方程式の解法を学びましょう。"
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## 1階線形常微分方程式
1階常微分方程式を代数的に

$$ y'+p(x)y=r(x) \tag{1} $$

の形に持っていくことができれば**線形(linear)**と呼び、そうでなければ**非線形(nonlinear)**と呼びます。

式(1)のような形を1階線形常微分方程式の**標準形(standard form)**と呼びます。もし与えられた1階線形常微分方程式の第一項が$f(x)y'$であれば、方程式の両辺を$f(x)$で割ることで標準形を得ることができます。

工学では、しばしば$r(x)$を**入力(input)**、$y(x)$を**出力(output)**または入力（と初期条件）に対する**応答(response)**と呼びます。

## 同次線形常微分方程式
式(1)を解きたい区間$a<x<b$を$J$とします。式(1)において区間$J$で$r(x)\equiv 0$であれば

$$ y'+p(x)y=0 \tag{2}$$

となり、これを**同次(homogeneous)**と呼びます。この場合、[変数分離法](/posts/Separation-of-Variables/)を使用できます。

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

$c=0$の場合、**自明な解(trivial solution)**$y(x)=0$を得ます。

## 非同次線形常微分方程式
区間$J$で$r(x)\not\equiv 0$の場合、**非同次(nonhomogeneous)**と呼びます。非同次線形常微分方程式(1)は$x$にのみ依存する積分因子を持つことが知られています。この積分因子$F(x)$は[積分因子を求める方法](/posts/Exact-Differential-Equation-and-Integrating-Factor/#積分因子を求める方法)の式(11)で求めることもできますし、以下のように直接求めることもできます。

式(1)に$F(x)$をかけると

$$ Fy'+pFy=rF \tag{1*} $$

を得ます。もし

$$ pF=F' $$

であれば、式(1*)の左辺は導関数$(Fy)'=F'y+Fy'$となります。$pF=F'$を変数分離すると$dF/F=p\ dx$となり、積分して$h=\int p\ dx$とすると

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

となります。式(1*)に代入すると

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

となります。積分すると

$$ e^hy=\int e^hr\ dx + c $$
となり、$e^h$で割ると求める解の公式を得ます。

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

このとき$h$における積分定数は問題になりません。

式(4)において与えられた初期条件に依存する唯一の値は$c$なので、式(4)を2つの項の和

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

と書くと、次のことがわかります。

$$ \text{全体の出力}=\text{入力 }r\text{に対する応答}+\text{初期条件に対する応答} \tag{5} $$

## 例題：RL回路
ある$RL$回路が起電力$E=48\textrm{V}$の電池、抵抗$R=11\mathrm{\Omega}$、インダクタンス$L=0.1\text{H}$で構成されており、初期電流は0であるとします。この$RL$回路のモデルを構築し、結果として得られる常微分方程式を電流$I(t)$について解いてください。

> **オームの法則(Ohm's law)**  
> 回路の電流$I$は抵抗の両端で電圧降下(voltage drop) $RI$を引き起こします。
{: .prompt-info }

> **ファラデーの電磁誘導の法則(Faraday's law of electromagnetic induction)**  
> 回路の電流$I$はインダクタの両端で電圧降下$LI'=L\ dI/dt$を引き起こします。
{: .prompt-info }

> **キルヒホッフの電圧法則(Kirchhoff's Voltage Law;KVL)**  
> 閉回路に加えられた起電力は、回路の他のすべての要素の両端の電圧降下の和に等しいです。
{: .prompt-info }

### 解答
上記の法則に従うと、$RL$回路のモデルは$LI'+RI=E(t)$となり、標準形で書くと

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

となります。式(4)において$x=t, y=I, p=R/L, h=(R/L)t$とおくと、この線形常微分方程式を解くことができます。

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

このとき$R/L=11/0.1=110$で$E(t)=48$なので

$$ I=\frac{48}{11}+ce^{-110t} $$

となります。

初期条件$I(0)=0$から$I(0)=E/R+c=0$、$c=-E/R$を得ます。これにより次の特殊解を求めることができます。

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
