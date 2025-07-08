---
title: 一階線性常微分方程的解法
description: 探討一階線性常微分方程的解法，包括齊次與非齊次方程，並以RL電路為例說明。
categories: [Mathematics, Differential Equation]
tags: [ODE, First-Order ODEs]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## 一階線性常微分方程
如果一個一階常微分方程可以代數地表示為

$$ y'+p(x)y=r(x) \tag{1} $$

的形式，則稱其為**線性(linear)**，否則稱為**非線性(nonlinear)**。

式 (1) 這樣的形式稱為一階線性常微分方程的**標準型(standard form)**。如果給定的一階線性常微分方程首項為 $f(x)y'$，則可將方程式兩邊同除以 $f(x)$ 來得到標準型。

在工程學中，$r(x)$ 常被稱為**輸入(input)**，$y(x)$ 則被稱為**輸出(output)**或對輸入（及初始條件）的**響應(response)**。

## 齊次線性常微分方程
假設我們要在某個區間 $a<x<b$（稱之為 $J$）上解式 (1)。若在區間 $J$ 上 $r(x)\equiv 0$，則方程式為

$$ y'+p(x)y=0 \tag{2}$$

我們稱之為**齊次(homogeneous)**。這種情況下，可以使用[變數分離法](/posts/Separation-of-Variables/)。

$$ \frac{dy}{y} = -p(x)dx $$

$$ \log |y| = -\int p(x)dx + c^* $$

$$ y(x) = ce^{-\int p(x)dx} \tag{3}$$

當 $c=0$ 時，我們得到**平凡解(trivial solution)** $y(x)=0$。

## 非齊次線性常微分方程
在區間 $J$ 上，若 $r(x)\not\equiv 0$，則稱為**非齊次(nonhomogeneous)**。非齊次線性常微分方程 (1) 已知具有一個僅依賴於 $x$ 的積分因子。這個積分因子 $F(x)$ 可以透過[求積分因子的方法](/posts/Exact-Differential-Equation-and-Integrating-Factor/#求積分因子的方法)中的式 (11) 求得，也可以如下直接推導。

將式 (1) 乘以 $F(x)$，得到

$$ Fy'+pFy=rF \tag{1*} $$

如果

$$ pF=F' $$

則式 (1*) 的左邊就成為導數 $(Fy)'=F'y+Fy'$。對 $pF=F'$ 進行變數分離，可得 $dF/F=p\ dx$，積分後若令 $h=\int p\ dx$，則

$$ \log |F|=h=\int p\ dx $$

$$ F = e^h $$

將此代入式 (1*)：

$$ e^hy'+h'e^hy=e^hy'+(e^h)'=(e^hy)'=re^h $$

積分後得到

$$ e^hy=\int e^hr\ dx + c $$
再同除以 $e^h$ 即可得到所求的解公式。

$$ y(x)=e^{-h}\left(\int e^hr\ dx + c\right),\qquad h=\int p(x)\ dx \tag{4} $$

此處 $h$ 的積分常數不影響結果。

在式 (4) 中，唯一依賴於給定初始條件的值是 $c$，因此，若將式 (4) 寫成兩個項的和

$$ y(x)=e^{-h}\int e^hr\ dx + ce^{-h} \tag{4*} $$

我們可以得到以下結論：

$$ \text{總輸出}=\text{對輸入 }r\text{ 的響應}+\text{對初始條件的響應} \tag{5} $$

## 範例：RL 電路
假設一個 $RL$ 電路由一個電動勢 $E=48\textrm{V}$ 的電池、一個 $R=11\mathrm{\Omega}$ 的電阻和一個 $L=0.1\text{H}$ 的電感器串聯而成，且初始電流為零。請建立此 $RL$ 電路的模型，並解出關於電流 $I(t)$ 的常微分方程。
> **歐姆定律(Ohm's law)**  
> 電路中的電流 $I$ 會在電阻兩端產生電壓降(voltage drop) $RI$。
{: .prompt-info }

> **法拉第電磁感應定律(Faraday's law of electromagnetic induction)**  
> 電路中的電流 $I$ 會在電感器兩端產生電壓降 $LI'=L\ dI/dt$。
{: .prompt-info }

> **克希荷夫電壓定律(Kirchhoff's Voltage Law; KVL)**  
> 在一個封閉迴路中，所施加的電動勢等於迴路中所有其他元件兩端的電壓降總和。
{: .prompt-info }

### 解法
根據上述定律，$RL$ 電路的模型為 $LI'+RI=E(t)$，寫成標準型即為

$$ I'+\frac{R}{L}I=\frac{E(t)}{L} \tag{6}$$

在式 (4) 中，令 $x=t, y=I, p=R/L, h=(R/L)t$，即可解此線性常微分方程。

$$ I=e^{-(R/L)t}\left(\int e^{(R/L)t} \frac{E(t)}{L}dt+c\right) $$

$$ I=e^{-(R/L)t}\left(\frac{E}{L}\frac{e^{(R/L)t}}{R/L}+c\right)=\frac{E}{R}+ce^{-(R/L)t} \tag{7} $$

此時 $R/L=11/0.1=110$ 且 $E(t)=48$，因此

$$ I=\frac{48}{11}+ce^{-110t} $$

根據初始條件 $I(0)=0$，可得 $I(0)=E/R+c=0$，即 $c=-E/R$。由此可求得特解如下：

$$ I=\frac{E}{R}(1-e^{-(R/L)t}) \tag{8} $$

$$ \therefore I=\frac{48}{11}(1-e^{-110t}) $$
