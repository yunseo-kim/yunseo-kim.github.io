---
title: የብዙ-አንግል·የግማሽ-አንግል ቀመሮች(Multiple-Angle and Half-Angle Formulas)
description: የ2-እጥፍ እና የ3-እጥፍ አንግል ቀመሮችን እንመለከታለን፣ እነዚህንም ከትሪጎኖሜትሪ መደመር ቀመሮች እንዴት እንደሚመነጩ እናሳያለን። እንዲሁም ከ2-እጥፍ አንግል ቀመሮች የግማሽ-አንግል ቀመሮችን እንወጣለን።
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Multiple-Angle Formulas, Half-Angle Formulas]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **የ2-እጥፍ አንግል ቀመሮች (Double-Angle Formulas)**
>
> - $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
> - $$ \begin{align*} 
> \cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
> &= 2\cos^{2}\alpha - 1 \\
> &= 1 - 2\sin^{2}\alpha \end{align*} $$
> - $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$
{: .prompt-info }

> **የ3-እጥፍ አንግል ቀመሮች (Triple-Angle Formulas)**
>
> - $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
> - $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$
{: .prompt-info }

> **የግማሽ-አንግል ቀመሮች (Half-Angle Formulas)**
>
> - $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
> - $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
> - $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
> - $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$
{: .prompt-info }

## ቅድመ ዝግጅቶች
- [የትሪጎኖሜትሪ መደመር ቀመሮች](/posts/trigonometric-addition-formulas)

## የብዙ-አንግል ቀመሮች
### የ2-እጥፍ አንግል ቀመሮች
- $$ \sin 2\alpha = 2\sin \alpha \cos \alpha $$
- $$ \begin{align*} 
\cos 2\alpha &= \cos^{2}\alpha - \sin^{2}\alpha \\ 
&= 2\cos^{2}\alpha - 1 \\
&= 1 - 2\sin^{2}\alpha \end{align*} $$
- $$\tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2}\alpha}$$

#### ማስመንጨት
ከ[የትሪጎኖሜትሪ መደመር ቀመሮች](/posts/trigonometric-addition-formulas) የ2-እጥፍ አንግል ቀመሮችን ማስመንጨት ይቻላል።

$$ \begin{gather} \sin ( \alpha + \beta ) = \sin \alpha \cos \beta + \cos \alpha \sin \beta \label{eqn:sin_add} \\
\cos ( \alpha + \beta ) = \cos \alpha \cos \beta - \sin \alpha \sin \beta \label{eqn:cos_add} \\
\tan ( \alpha + \beta ) = \frac { \tan \alpha + \tan \beta } { 1 - \tan \alpha \tan \beta } \label{eqn:tan_add} \end{gather} $$

በ$\beta$ ቦታ $\alpha$ን ብንተካ

በስሌት ($\ref{eqn:sin_add}$)

$$\sin 2\alpha = 2\sin \alpha \cos \alpha$$

በስሌት ($\ref{eqn:cos_add}$)

$$\begin{align*} \cos 2 \alpha &= \cos ^ { 2 } \alpha - \sin ^ { 2 } \alpha \\ &= 2 \cos ^ { 2 } \alpha - 1 \\ &= 1 - 2 \sin ^ { 2 } \alpha \end{align*}$$

በስሌት ($\ref{eqn:tan_add}$)

$$ \tan 2\alpha = \frac{2\tan \alpha}{1 - \tan^{2} \alpha} $$

### የ3-እጥፍ አንግል ቀመሮች
- $$\sin 3\alpha = 3\sin \alpha - 4\sin^{3}\alpha$$
- $$\cos 3\alpha = 4\cos^{3}\alpha - 3\cos \alpha$$

#### ማስመንጨት
$\sin 2\alpha = 2\sin\alpha \cos\alpha$, $\cos 2 \alpha = 1 - 2\sin^{2}\alpha$ን በመጠቀም

$$ \begin{align*} \sin 3 \alpha &= \sin ( \alpha + 2 \alpha ) = \sin \alpha \cos 2 \alpha + \cos \alpha \sin 2 \alpha \\ &= \sin \alpha ( 1 - 2 \sin ^ { 2 } \alpha ) + \cos \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \sin a ( 1 - 2 \sin ^ { 2 } \alpha ) + 2 \sin \alpha ( 1 - \sin ^ { 2 } \alpha ) \\ &= 3 \sin \alpha - 4 \sin ^ { 3 } \alpha . \end{align*} $$

በተመሳሳይ መንገድ፣ $\sin 2\alpha = 2\sin\alpha \cos\alpha$, $\cos 2 \alpha = 2\cos^{2}\alpha - 1$ን በመጠቀም

$$ \begin{align*} \cos 3 \alpha &= \cos ( \alpha + 2 \alpha ) = \cos \alpha \cos 2 \alpha - \sin \alpha \sin 2 \alpha \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - \sin \alpha ( 2 \sin \alpha \cos \alpha ) \\ &= \cos \alpha ( 2 \cos ^ { 2 } \alpha - 1 ) - 2 \cos \alpha ( 1 - \cos ^ { 2 } \alpha ) \\ &= 4 \cos ^ { 3 } \alpha - 3 \cos \alpha \end{align*} $$

## የግማሽ-አንግል ቀመሮች
- $$\sin^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{2}$$
- $$\cos^{2}\frac{\alpha}{2} = \frac{1 + \cos \alpha}{2}$$
- $$\tan^{2}\frac{\alpha}{2} = \frac{1 - \cos \alpha}{1 + \cos\alpha}$$
- $$\tan \frac{\alpha}{2} = \frac{\sin \alpha}{1 + \cos \alpha}$$

#### ማስመንጨት
በ2-እጥፍ አንግል ቀመር $\cos 2\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha$ ውስጥ በ$\alpha$ ቦታ $\frac{\alpha}{2}$ን ብንተካ

$$ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} = 2 \cos^{2}\frac{\alpha}{2} - 1 .$$

ከ$ \cos \alpha = 1 - 2\sin^{2}\frac{\alpha}{2} $ ይከተላል

$$ \sin^{2}\frac{\alpha}{2}=\frac{1-\cos \alpha}{2} .$$

ከ$ \cos \alpha = 2 \cos^{2}\frac{\alpha}{2} - 1 $ ይከተላል

$$ \cos^{2}\frac{\alpha}{2}=\frac{1+\cos \alpha}{2} .$$

ከዚህም

$$ \tan ^ { 2 } \frac { \alpha } { 2 } = \left . \left( \sin ^ { 2 } \frac{\alpha}{2}\right) \middle/ \left( \cos ^ { 2 } \frac { \alpha } { 2 } \right) \right . = \frac { 1 - \cos \alpha } { 1 + \cos \alpha } $$

መሆኑን ማሳየት ይቻላል፣ እንዲሁም

$$ \tan \frac { \alpha } { 2 } = \frac { \sin \frac { \alpha } { 2 } } { \cos \frac { \alpha } { 2 } } = \frac { 2 \sin \frac { \alpha } { 2 } \cos \frac { \alpha } { 2 } } { 2 \cos ^ { 2 } \frac { \alpha } { 2 } } = \frac { \sin \alpha } { 1 + \cos \alpha } $$

ደግሞ ይሠራል።
