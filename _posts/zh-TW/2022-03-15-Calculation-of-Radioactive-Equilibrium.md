---
title: 輻射平衡計算
description: 探討放射性核種的衰變常數、半衰期和平均壽命之間的關係，並計算給定衰變鏈中任意時間 t 的放射性核種的放射性活度。
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Radioactive Decay]
math: true
mermaid: true
image: /assets/img/atoms.png
---
## TL;DR
> **任意時間 t 的放射性活度**
>
> $$\begin{align*}
> \alpha (t) &= \lambda n(t)
> \\ &= \alpha_0 e^{-\lambda t}
> \\ &= \alpha_0 e^{-0.693t/T_{1/2}}
> \end{align*}$$
{: .prompt-info }

> **衰變常數、半衰期和平均壽命的關係**
>
> $$ \begin{align*}
> T_{1/2}&=\frac {\ln 2}{\lambda} = \frac {0.693}{\lambda}
> \\
> \\ \overline{t}&=\frac {1}{\lambda}
> \\ &=\frac {T_{1/2}}{0.693}=1.44T_{1/2}
> \end{align*} $$
{: .prompt-info }

## 衰變常數（Decay Constant）
- 某個原子核在單位時間內衰變的機率
- 與時間無關，只由核種決定的常數
- 用符號 $\lambda$ 表示

## 放射性活度（Radioactivity）
在時間 $t$ 時尚未衰變的原子核數量為 n(t)，則在時間 $t$ 和 $t+dt$ 之間的間隔 $dt$ 內，平均有 $\lambda n(t)$ 個原子核衰變。這種衰變率稱為該樣品的*放射性活度（radioactivity）*，用符號 $\alpha$ 表示。因此，在任何時間 $t$ 的放射性活度為：

$$ \alpha (t)=\lambda n(t) \tag{1}$$

## 放射性活度的單位
### 居里（Curie, Ci）
- 在使用貝克勒爾單位之前傳統使用的單位
- 1克鐳-226的放射性活度
- 每秒 $3.7\times 10^{10}$ 次核衰變（$3.7\times 10^{10}\text{Bq}$）

### 貝克勒爾（Becquerel, Bq）
- 國際標準（SI）單位
- 每秒1次核衰變
- $1 \text{Bq} = 2.703\times 10^{-11}\text{Ci} = 27\text{pCi}$

## 計算放射性活度隨時間的變化
在時間 $dt$ 內有 $\lambda n(t)$ 個原子核衰變，因此在 $dt$ 內樣品中未衰變而剩餘的原子核數量減少量可以表示為：

$$ -dn(t)=\lambda n(t)dt $$

積分後得到：

$$ n(t)=n_0e^{-\lambda t} \tag{2} $$

兩邊乘以 $\lambda$，則放射性活度為：

$$ \alpha (t)=\alpha_0e^{-\lambda t} \tag{3} $$

放射性活度在*半衰期（half-life）*內減半，因此：

$$ \alpha (T_{1/2})=\alpha_0/2 $$

將此代入式 (3)：

$$ \alpha_0/2=\alpha_0e^{-\lambda T_{1/2}} $$

兩邊取對數並解出半衰期 $T_{1/2}$：

$$ T_{1/2}=\frac {\ln 2}{\lambda}=\frac {0.693}{\lambda} \tag{4}$$

將上式解出 $\lambda$ 並代入式 (3)：

$$ \alpha (t)=\alpha_0e^{-0.693t/T_{1/2}} \tag{5} $$

式 (5) 在放射性衰變計算中通常比式 (3) 更實用，因為半衰期值比衰變常數更常被給出。

放射性原子核的*平均壽命（mean-life）* $\overline{t}$ 是衰變常數的倒數：

$$ \overline{t}=1/\lambda $$

從式 (3) 可以看出，在一個平均壽命內，放射性活度下降到初始值的 $1/e$。從式 (4) 可以得出平均壽命和半衰期之間的關係：

$$ \overline{t}=\frac {T_{1/2}}{0.693}=1.44T_{1/2} \tag{6} $$

### ※ 平均壽命 $\overline{t}$ 的推導

$$ \begin{align*}
\overline{t}&=\frac {\int_0^\infty t\alpha(t)}{\int_0^\infty t} = \frac {\int_0^\infty t\alpha(t)}{n_0}
\\ &= \frac {\int_0^\infty n_0 \lambda te^{-\lambda t}}{n_0}
\\ &= \int_0^\infty \lambda te^{-\lambda t}
\\ &= \left[-te^{-\lambda t}\right]_0^\infty +\int_0^\infty e^{-\lambda t}
\\ &=\left[-\frac {1}{\lambda} e^{-\lambda t}\right]_0^\infty
\\ &=\frac {1}{\lambda}
\end{align*}$$

## 例題：放射性衰變鏈 1
假設某放射性核種以 $R$ atom/s 的速率產生。這些原子核一產生就立即開始放射性衰變。求任意時刻 t 時該核種的放射性活度。
```mermaid
flowchart LR
	Start[?] -- R --> A[數學模型]
	A -- α --> End[?]
```

### 1. 建立模型

$$ \text{核種隨時間的變化率} = \text{產生率}-\text{損失率} $$

用數學符號表示為：

$$ dn/dt = -\lambda n + R $$

### 2. 一般解
將 $n$ 的項全部移到左邊，兩邊乘以 $e^{\lambda t}$：

$$ \frac {dn}{dt} + \lambda n = R $$

$$ e^{\lambda t}\frac {dn}{dt} + \lambda e^{\lambda t}n = Re^{\lambda t} $$

因為 $\lambda e^{\lambda t}=\frac {d}{dt} e^{\lambda t}$，所以可以整理為：

$$ e^{\lambda t}\frac {dn}{dt}+\left(\frac {d}{dt} e^{\lambda t}\right)n = Re^{\lambda t} $$

兩邊積分得到一般解：

$$ e^{\lambda t}n=\frac {R}{\lambda}e^{\lambda t}+c $$

$$ n=ce^{-\lambda t}+\frac {R}{\lambda} $$

### 3. 特解
假設在 $t=0$ 時，這個核種的數量為 $n_0$，求常數 $c$ 的值：

$$ n(0)=c+\frac {R}{\lambda}=n_0 $$

$$ c=n_0-\frac {R}{\lambda} $$

因此，符合給定情況的特解為：

$$ n = n_0e^{-\lambda t}+\frac {R}{\lambda}(1-e^{-\lambda t}) \tag{7} $$

兩邊乘以 $\lambda$ 可得到這個核種的放射性活度：

$$ \alpha = \alpha_0e^{-\lambda t}+R(1-e^{-\lambda t}) \tag{8} $$

也就是說，當 $t\to\infty$ 時，$\alpha_{\text{max}}=R$，$n_{\text{max}}=R/\lambda$。

## 例題：放射性衰變鏈 2
在下面的衰變鏈中，計算放射性核種 B 的放射性活度。
```mermaid
flowchart LR
	A --> B
	B --> C
```

### 1. 建立模型

$$ \text{B 核的數量變化率}=\text{A 衰變產生的速率}-\text{B 衰變為 C 的速率} $$

$$ \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_A $$

將 $n_A$ 代入式 (2)，得到關於 $n_B$ 的微分方程：

$$  \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_{A0}e^{-\lambda_A t} \tag{9}$$ 

### 2. 一般解
為了解微分方程，將 $n_B$ 的項全部移到左邊，兩邊乘以 $e^{\lambda_B t}$：

$$ \frac {dn_B}{dt} + \lambda_B n_B = n_{A0}\lambda_A e^{-\lambda_A t} $$

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \lambda_B e^{\lambda_B t}n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

因為 $\lambda_B e^{\lambda_B t}=\frac {d}{dt} e^{\lambda_b t}$，所以可以整理為：

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \left(\frac {d}{dt} e^{\lambda_B t}\right)n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

兩邊積分：

$$ e^{\lambda_B t}n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{(\lambda_B-\lambda_A)t}+c $$

兩邊除以 $e^{\lambda_B t}$ 得到一般解：

$$ n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{-\lambda_A t}+ce^{-\lambda_B t} $$

### 3. 特解
假設在 $t=0$ 時，B 元素的數量為 $n_{B0}$，求常數 $c$ 的值：

$$ n_B(0)=\frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}+c=n_{B0} $$

$$ c=n_{B0}-\frac{n_{A0}\lambda_A}{\lambda_B-\lambda_A} $$

因此，符合給定情況的特解為：

$$ n_B = n_{B0}e^{-\lambda_B t} + \frac {n_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{10}$$

$$ \therefore \alpha_B = \alpha_{B0} e^{-\lambda_B t} + \frac {\alpha_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{11}$$
