---
title: 連續X射線與特性X射線(Continuous and Characteristic X Rays)
description: 探討原子輻射中X射線的兩種產生原理，以及相應的制動輻射和特性X射線的各自特徵。
categories: [Nuclear Engineering, Radiation]
tags: [Nuclear Physics, Atomic Radiation, Atomic Structure]
math: true
image: /assets/img/atoms.webp
---
## TL;DR
> - **制動輻射（bremsstrahlung）**：帶電粒子（如電子）在原子核附近通過時，由於電力作用而加速，從而發射出連續光譜的X射線
> - 最小波長：$\lambda_\text{min} = \cfrac{hc}{E_\text{max}} = \cfrac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}$
> - **特性X射線（characteristic X-ray）**：入射電子與內層電子殼的電子碰撞，使原子電離後，外層電子殼的電子填補內層空缺時所釋放的能量，其能量等於兩個能級之間的差異，形成不連續光譜的X射線
{: .prompt-info }

## 先備知識
- [亞原子粒子與原子的組成元素](/posts/constituents-of-an-atom/)

## X射線的發現
倫琴（Röntgen）發現當電子束照射到靶材時會產生X射線。由於發現當時還不知道X射線是電磁波，因此以"X"命名，表示未知的意思。此外，也以發現者的名字稱為**倫琴射線（Röntgen radiation）**。

![X-ray Tube](https://upload.wikimedia.org/wikipedia/commons/7/72/WaterCooledXrayTube.svg)

上圖簡單地展示了典型X射線管（X-ray tube）的結構。X射線管內部由鎢絲燈絲構成的陰極和固定靶材的陽極在真空狀態下密封。在兩極之間施加數十kV的高電壓，陰極會釋放電子並照射到陽極的靶材上，從而產生X射線。然而，能量轉換為X射線的效率通常低於1%，超過99%的能量會轉換為熱，因此需要額外的冷卻裝置。

## 制動輻射（bremsstrahlung）
當帶電粒子（如電子）經過原子核附近時，由於粒子與原子核之間的電力作用，其運動路徑會急劇彎曲並減速，同時以X射線的形式釋放能量。這個過程中的能量轉換並非量子化的，因此產生的X射線呈現連續光譜，這種現象稱為**制動輻射（bremsstrahlung）**。

![Bremsstrahlung](https://upload.wikimedia.org/wikipedia/commons/1/1e/Bremsstrahlung.svg)

然而，由制動輻射產生的X射線光子的能量顯然不能超過入射電子的動能。因此，發射的X射線存在最小波長，可以用以下簡單的公式計算：

$$ \lambda_\text{min} = \frac{hc}{E}. \tag{1}$$

由於普朗克常數$h$和光速$c$是常數，這個最小波長只取決於入射電子的能量。對應於$1\text{eV}$能量的波長$\lambda$約為$1.24 \mu\text{m}=12400\text{Å}$。因此，當X射線管施加$V$伏特電壓時的最小波長$\lambda_\text{min}$為：

$$ \lambda_\text{min} \text{[Å]} = \frac{12400 \text{[Å}\cdot\text{eV]}}{V\text{[eV]}}. \label{eqn:lambda_min}\tag{2}$$

實際上，這個公式被廣泛使用。

下圖顯示了在保持X射線管電流恆定的情況下，改變電壓時的連續X射線光譜。可以看到，隨著電壓的增加，最小波長$\lambda_{\text{min}}$變短，整體X射線強度也增加。

![典型的連續X射線光譜，顯示在相同電流下三種不同峰值電壓下的運作情況](/assets/img/continuous-and-characteristic-x-rays/bremsstrahlung.png)

## 特性X射線（characteristic X-ray）
如果X射線管施加的電壓足夠大，入射電子可能會與靶原子內層電子殼的電子碰撞，使該原子電離。在這種情況下，外層電子殼的電子會迅速釋放能量並填補內層的空缺，在這個過程中會產生能量等於兩個能級差的X射線光子。通過這個過程產生的X射線光譜是不連續的，由靶原子的特定能級決定，與入射電子束的能量或強度無關。這種X射線被稱為**特性X射線（characteristic X-ray）**。

### Siegbahn符號

![Siegbahn符號表示電子在殼層間躍遷](https://upload.wikimedia.org/wikipedia/commons/f/f6/CharacteristicRadiation.svg)
> *圖片來源*
> - 作者：英文維基百科用戶 [HenrikMidtiby](https://en.wikipedia.org/wiki/User:HenrikMidtiby)
> - 授權：[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

根據Siegbahn符號，當L殼、M殼等的電子填補K殼的空缺時釋放的X射線，如上圖所示，分別稱為$K_\alpha$、$K_\beta$等。然而，在Siegbahn符號提出後，隨著現代原子模型的出現，人們發現對於多電子原子，在玻爾原子模型的每個殼層（具有相同主量子數的能級）內，能級還會因其他量子數而有所不同。因此，對於每個$K_\alpha$、$K_\beta$等，又進一步細分為$K_{\alpha_1}$、$K_{\alpha_2}$等。

![Siegbahn符號](/assets/img/continuous-and-characteristic-x-rays/siegbahn-notation.png)

這種傳統的符號系統在光譜學領域仍被廣泛使用。然而，由於命名不夠系統化且容易引起混淆，國際純粹與應用化學聯合會（IUPAC）建議使用另一種符號系統。

### IUPAC符號
IUPAC建議的原子軌道和特性X射線的標準符號如下：
首先，為每個原子軌道分配以下表格中的名稱：

| $n$（主量子數） | $l$（角量子數） | $s$（自旋量子數） | $j$（總角動量量子數） | 原子軌道 | X射線符號 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $1$ | $0$ | $\pm1/2$ | $1/2$ | $1s_{1/2}$ | $K_{(1)}$ |
| $2$ | $0$ | $\pm1/2$ | $1/2$ | $2s_{1/2}$ | $L_1$ |
| $2$ | $1$ | $-1/2$ | $1/2$ | $2p_{1/2}$ | $L_2$ |
| $2$ | $1$ | $+1/2$ | $3/2$ | $2p_{3/2}$ | $L_3$ |
| $3$ | $0$ | $\pm1/2$ | $1/2$ | $3s_{1/2}$ | $M_1$ |
| $3$ | $1$ | $-1/2$ | $1/2$ | $3p_{1/2}$ | $M_2$ |
| $3$ | $1$ | $+1/2$ | $3/2$ | $3p_{3/2}$ | $M_3$ |
| $3$ | $2$ | $-1/2$ | $3/2$ | $3d_{3/2}$ | $M_4$ |
| $3$ | $2$ | $+1/2$ | $5/2$ | $3d_{5/2}$ | $M_5$ |
| $4$ | $0$ | $\pm1/2$ | $1/2$ | $4s_{1/2}$ | $N_1$ |
| $4$ | $1$ | $-1/2$ | $1/2$ | $4p_{1/2}$ | $N_2$ |
| $4$ | $1$ | $+1/2$ | $3/2$ | $4p_{3/2}$ | $N_3$ |
| $4$ | $2$ | $-1/2$ | $3/2$ | $4d_{3/2}$ | $N_4$ |
| $4$ | $2$ | $+1/2$ | $5/2$ | $4d_{5/2}$ | $N_5$ |
| $4$ | $3$ | $-1/2$ | $5/2$ | $4f_{5/2}$ | $N_6$ |
| $4$ | $3$ | $+1/2$ | $7/2$ | $4f_{7/2}$ | $N_7$ |

> 總角動量量子數 $j=\|l+s\|$。
{: .prompt-info }

然後，當原子中的電子從一個能級躍遷到較低能級時釋放的特性X射線，按照以下規則命名：

$$ \text{（終態能級的X射線符號）-（初態能級的X射線符號）} $$

例如，$2p_{1/2}$軌道的電子躍遷到$1s_{1/2}$時釋放的特性X射線可以稱為$\text{K-L}_2$。

## X射線光譜

![使用銠靶、60 kV操作電壓的X射線管所發射的X射線光譜](https://upload.wikimedia.org/wikipedia/commons/2/23/TubeSpectrum-en.svg)

上圖顯示了當60kV加速的電子束照射到銠（Rh）靶時產生的X射線光譜。可以看到由制動輻射產生的平滑連續曲線，根據公式（$\ref{eqn:lambda_min}$），只有波長大於約$0.207\text{Å} = 20.7\text{pm}$的X射線被發射。此外，圖中的尖峰是由銠原子特有的K殼X射線產生的。如前所述，由於不同靶原子具有獨特的特性X射線光譜，通過觀察某個靶材在電子束照射下產生的X射線光譜中出現尖峰的波長，可以確定該靶材的組成元素。

> 除了$K_\alpha、K_\beta$等之外，$L_\alpha、L_\beta$等更低能量的X射線當然也會被發射。然而，這些X射線的能量要低得多，通常會被X射線管的外殼吸收，無法到達檢測器。
{: .prompt-info }
