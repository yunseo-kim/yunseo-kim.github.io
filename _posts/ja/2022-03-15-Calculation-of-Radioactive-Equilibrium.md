---
title: 放射平衡計算
description: 放射性核種の崩壊定数と半減期、平均寿命の相関関係について学び、与えられた崩壊連鎖における任意の時間tでの放射性核種の放射能を計算してみる。
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Radioactive Decay]
math: true
mermaid: true
image: /assets/img/atoms.png
---
## TL;DR
> **任意の時間tでの放射能**
>
> $$\begin{align*}
> \alpha (t) &= \lambda n(t)
> \\ &= \alpha_0 e^{-\lambda t}
> \\ &= \alpha_0 e^{-0.693t/T_{1/2}}
> \end{align*}$$
{: .prompt-info }

> **崩壊定数と半減期、平均寿命の関係**
>
> $$ \begin{align*}
> T_{1/2}&=\frac {\ln 2}{\lambda} = \frac {0.693}{\lambda}
> \\
> \\ \overline{t}&=\frac {1}{\lambda}
> \\ &=\frac {T_{1/2}}{0.693}=1.44T_{1/2}
> \end{align*} $$
{: .prompt-info }

## 崩壊定数(Decay Constant)
- ある核が単位時間当たりに崩壊する確率
- 時間に関係なく一定で、核種によってのみ決定される定数
- 記号 $\lambda$ で表記

## 放射能(Radioactivity)
時間 $t$ でまだ崩壊していない核の数を n(t) とすると、時間 $t$ と $t+dt$ の間の間隔 $dt$ の間に平均的に $\lambda n(t)$ 個の核が崩壊する。この崩壊率をそのサンプルの *放射能(radioactivity)* と呼び、記号 $\alpha$ で表記する。したがって、ある時間 $t$ での放射能は次のようになる。

$$ \alpha (t)=\lambda n(t) \tag{1}$$

## 放射能の単位
### キュリー(Curie, Ci)
- ベクレル単位を使用する前に伝統的に使用された単位
- ラジウム-226 1gが持つ放射能
- 毎秒 $3.7\times 10^{10}$ 回の核崩壊($3.7\times 10^{10}\text{Bq}$)

### ベクレル(Becquerel, Bq)
- 国際標準(SI)単位
- 毎秒1回の核崩壊
- $1 \text{Bq} = 2.703\times 10^{-11}\text{Ci} = 27\text{pCi}$

## 時間に伴う放射能変化の計算
時間 $dt$ の間に $\lambda n(t)$ 個の核が崩壊するので、$dt$ の間にサンプル内で崩壊せずに残っている核の減少量は次のように表現できる。

$$ -dn(t)=\lambda n(t)dt $$

これを積分すると

$$ n(t)=n_0e^{-\lambda t} \tag{2} $$

となる。両辺に $\lambda$ を掛けると放射能は

$$ \alpha (t)=\alpha_0e^{-\lambda t} \tag{3} $$

となる。

放射能は *半減期(half-life)* の間に半分に減少するので

$$ \alpha (T_{1/2})=\alpha_0/2 $$

これを式 (3) に代入すると

$$ \alpha_0/2=\alpha_0e^{-\lambda T_{1/2}} $$

となる。両辺に対数をとり、半減期 $T_{1/2}$ について解くと

$$ T_{1/2}=\frac {\ln 2}{\lambda}=\frac {0.693}{\lambda} \tag{4}$$

上の式を $\lambda$ について解いて式 (3) に代入すると

$$ \alpha (t)=\alpha_0e^{-0.693t/T_{1/2}} \tag{5} $$

式 (5) が式 (3) よりも放射性崩壊の計算に使用しやすい場合が多いが、これは崩壊定数よりも半減期の値が与えられることが多いためである。

放射性核の *平均寿命(mean-life)* $\overline{t}$ は崩壊定数の逆数である。

$$ \overline{t}=1/\lambda $$

式 (3) から、1回の平均寿命の間に放射能は初期値の $1/e$ に落ちることがわかる。式 (4) から平均寿命と半減期は以下のような関係が成り立つ。

$$ \overline{t}=\frac {T_{1/2}}{0.693}=1.44T_{1/2} \tag{6} $$

### ※ 平均寿命 $\overline{t}$ の導出

$$ \begin{align*}
\overline{t}&=\frac {\int_0^\infty t\alpha(t)}{\int_0^\infty t} = \frac {\int_0^\infty t\alpha(t)}{n_0}
\\ &= \frac {\int_0^\infty n_0 \lambda te^{-\lambda t}}{n_0}
\\ &= \int_0^\infty \lambda te^{-\lambda t}
\\ &= \left[-te^{-\lambda t}\right]_0^\infty +\int_0^\infty e^{-\lambda t}
\\ &=\left[-\frac {1}{\lambda} e^{-\lambda t}\right]_0^\infty
\\ &=\frac {1}{\lambda}
\end{align*}$$

## 例題：放射性崩壊連鎖 1
ある放射性核種が $R$ atom/s の速度で生成されると仮定する。この核は生成されるとすぐに放射性崩壊が起こる。任意の時刻 t でのこの核種の放射能を求めよ。
```mermaid
flowchart LR
	Start[?] -- R --> A[数学的モデル]
	A -- α --> End[?]
```

### 1. モデル設定

$$ \text{時間に伴う核種変化率} = \text{生成率}-\text{損失率} $$

数学記号で表現すると

$$ dn/dt = -\lambda n + R $$

となる。

### 2. 一般解
$n$ に関する項をすべて左辺に移項し、両辺に $e^{\lambda t}$ を掛ける。

$$ \frac {dn}{dt} + \lambda n = R $$

$$ e^{\lambda t}\frac {dn}{dt} + \lambda e^{\lambda t}n = Re^{\lambda t} $$

$\lambda e^{\lambda t}=\frac {d}{dt} e^{\lambda t}$ なので、次のように整理できる。

$$ e^{\lambda t}\frac {dn}{dt}+\left(\frac {d}{dt} e^{\lambda t}\right)n = Re^{\lambda t} $$

両辺を積分すると次の一般解を得る。

$$ e^{\lambda t}n=\frac {R}{\lambda}e^{\lambda t}+c $$

$$ n=ce^{-\lambda t}+\frac {R}{\lambda} $$

### 3. 特殊解
$t=0$ のときにこの核種の数が $n_0$ であるとし、定数 $c$ の値を求める。

$$ n(0)=c+\frac {R}{\lambda}=n_0 $$

$$ c=n_0-\frac {R}{\lambda} $$

したがって、与えられた状況に合う特殊解は次のようになる。

$$ n = n_0e^{-\lambda t}+\frac {R}{\lambda}(1-e^{-\lambda t}) \tag{7} $$

である。上の式の両辺に $\lambda$ を掛けてこの核種の放射能を求めることができる。

$$ \alpha = \alpha_0e^{-\lambda t}+R(1-e^{-\lambda t}) \tag{8} $$

つまり、$t\to\infty$ のとき $\alpha_{\text{max}}=R$, $n_{\text{max}}=R/\lambda$ に収束する。

## 例題：放射性崩壊連鎖 2
以下のような崩壊連鎖において放射性核種 B の放射能を計算せよ。
```mermaid
flowchart LR
	A --> B
	B --> C
```

### 1. モデル設定

$$ \text{B 核の数の変化率}=\text{A の崩壊による生成率}-\text{B の C への崩壊率} $$

$$ \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_A $$

$n_A$ について式 (2) を代入すると、$n_B$ に関する次の微分方程式を得る。

$$  \frac {dn_B}{dt} = -\lambda_B n_B + \lambda_A n_{A0}e^{-\lambda_A t} \tag{9}$$ 

### 2. 一般解
微分方程式を解くために、$n_B$ に関する項をすべて左辺に移項し、両辺に $e^{\lambda_B t}$ を掛ける。

$$ \frac {dn_B}{dt} + \lambda_B n_B = n_{A0}\lambda_A e^{-\lambda_A t} $$

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \lambda_B e^{\lambda_B t}n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

$\lambda_B e^{\lambda_B t}=\frac {d}{dt} e^{\lambda_b t}$ なので、次のように整理できる。

$$ e^{\lambda_B t}\frac {dn_B}{dt} + \left(\frac {d}{dt} e^{\lambda_B t}\right)n_B = n_{A0}\lambda_A e^{(\lambda_B-\lambda_A)t} $$

両辺を積分すると

$$ e^{\lambda_B t}n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{(\lambda_B-\lambda_A)t}+c $$

となる。両辺を $e^{\lambda_B t}$ で割ると次の一般解を得る。

$$ n_B = \frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}e^{-\lambda_A t}+ce^{-\lambda_B t} $$

### 3. 特殊解
$t=0$ のとき B 元素の数が $n_{B0}$ であるとし、定数 $c$ の値を求める。

$$ n_B(0)=\frac {n_{A0}\lambda_A}{\lambda_B-\lambda_A}+c=n_{B0} $$

$$ c=n_{B0}-\frac{n_{A0}\lambda_A}{\lambda_B-\lambda_A} $$

したがって、与えられた状況に合う特殊解は次のようになる。

$$ n_B = n_{B0}e^{-\lambda_B t} + \frac {n_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{10}$$

$$ \therefore \alpha_B = \alpha_{B0} e^{-\lambda_B t} + \frac {\alpha_{A0}\lambda_A}{\lambda_B - \lambda_A} (e^{-\lambda_A t} - e^{-\lambda_B t}) \tag{11}$$
