---
title: 一階線性常微分方程的解法
description: 讓我們來了解一階線性常微分方程的解法。
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## 一階線性常微分方程
如果一階常微分方程可以代數地表示為

$$ y'+p(x)y=r(x) \tag{1} $$

的形式，我們稱之為**線性(linear)**，否則稱為**非線性(nonlinear)**。

式(1)的形式被稱為一階線性常微分方程的**標準形式(standard form)**。如果給定的一階線性常微分方程的第一項是$f(x)y'$，我們可以通過將方程的兩邊除以$f(x)$來得到標準形式。

在工程中，$r(x)$通常被稱為**輸入(input)**，$y(x)$被稱為**輸出(output)**或對輸入（和初始條件）的**響應(response)**。

## 齊次線性常微分方程
假設我們要在某個區間$a<x<b$上解方程(1)，我們將這個區間稱為$J$。如果在式(1)中，對於區間$J$，$r(x)\equiv 0$，則我們有

$$ y'+p(x)y=0 \tag{2}$$

這被稱為**齊次(homogeneous)**方程。在這種情況下，我們可以使用[變數分離法](/posts/Separation-of-Variables/)。

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

當$c=0$時，我們得到**平凡解(trivial solution)** $y(x)=0$。

## 非齊次線性常微分方程
如果在區間$J$上$r(x)\not\equiv 0$，我們稱之為**非齊次(nonhomogeneous)**。已知非齊次線性常微分方程(1)具有只依賴於$x$的積分因子。這個積分因子$F(x)$可以通過[求積分因子的方法](/posts/Exact-Differential-Equation-and-Integrating-Factor/#求積分因子的方法)的式(11)來求得，也可以直接求得如下：

將式(1)乘以$F(x)$，我們得到

$$ Fy'+pFy=rF \tag{1*} $$

如果

$$ pF=F' $$

則式(1*)的左邊成為導數$(Fy)'=F'y+Fy'$。將$pF=F'$進行變數分離，我們得到$dF/F=p\ dx$，積分後寫為$h=\int p\ dx$，則

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

將此代入式(1*)，我們得到

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

積分後得到

$$ e^hy=\int e^hr\ dx + c $$
除以$e^h$，我們得到所需的解公式。

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

這裡$h$中的積分常數並不重要。

在式(4)中，唯一依賴於給定初始條件的值是$c$，因此我們可以將式(4)寫成兩項之和的形式

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

從這裡我們可以得知：

$$ \text{總輸出}=\text{對輸入}r\text{的響應}+\text{對初始條件的響應} \tag{5} $$

## 例題：RL電路
假設一個RL電路由一個電動勢為$E=48\textrm{V}$的電池、一個電阻為$R=11\mathrm{\Omega}$的電阻器和一個電感為$L=0.1\text{H}$的電感器組成，初始電流為0。求這個RL電路的模型，並解出得到的常微分方程以求電流$I(t)$。
> **歐姆定律(Ohm's law)**  
> 電路中的電流$I$會在電阻兩端產生電壓降(voltage drop) $RI$。
{: .prompt-info }

> **法拉第電磁感應定律(Faraday's law of electromagnetic induction)**  
> 電路中的電流$I$會在電感兩端產生電壓降$LI'=L\ dI/dt$。
{: .prompt-info }

> **基爾霍夫電壓定律(Kirchhoff's Voltage Law;KVL)**  
> 閉合電路中施加的電動勢等於電路中所有其他元件兩端電壓降的總和。
{: .prompt-info }

### 解答
根據上述定律，RL電路的模型為$LI'+RI=E(t)$，寫成標準形式為

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

在式(4)中，令$x=t, y=I, p=R/L, h=(R/L)t$，我們可以解這個線性常微分方程。

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

這裡$R/L=11/0.1=110$且$E(t)=48$，所以

$$ I=\frac{48}{11}+ce^{-110t} $$

從初始條件$I(0)=0$，我們得到$I(0)=E/R+c=0$，$c=-E/R$。由此我們可以得到以下特解：

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
