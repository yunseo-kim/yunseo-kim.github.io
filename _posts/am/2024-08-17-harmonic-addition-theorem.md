---
title: የትሪጎኖሜትሪ ፋንክሽኖች ውህደት(Harmonic Addition Theorem)
description: ስለ እንደ f(θ) = a cos θ + b sin θ ያለ የትሪጎኖሜትሪ ፋንክሽኖች ድምር፣ ከእሱ ጋር የሚመጣውን ነጠላ የትሪጎኖሜትሪ ፋንክሽን r sin(θ+α) ወይም r cos(θ-β) እንዴት እንደሚገኝ እንመለከታለን።
categories: [Mathematics, Trigonometry]
tags: [Trigonometric Addition Formulas, Harmonic Addition Theorem]
math: true
image: /assets/img/math-and-physics-cropped.webp
---
## TL;DR
> **የትሪጎኖሜትሪ ፋንክሽኖች ውህደት (Harmonic Addition Theorem)**
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \sin(\theta+\alpha) $$
>
> $$ (እዚህ፣\ \cos \alpha = \frac{a}{\sqrt{a^{2}+b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2}+b^{2}}}) $$
>
> - $$ a\sin \theta + b\cos \theta = \sqrt{a^{2}+b^{2}} \cos(\theta-\beta) $$
>
> $$ (እዚህ፣\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}) $$
{: .prompt-info }

## ቅድመ ዕውቀት
- [የትሪጎኖሜትሪ ድምር መለያዎች](/posts/trigonometric-addition-formulas)

## የትሪጎኖሜትሪ ፋንክሽኖች ውህደት (Harmonic Addition Theorem)
$f(\theta) = a \cos \theta + b \sin \theta$ እንደሚሆን በትሪጎኖሜትሪ ፋንክሽኖች ድምር መልክ ለተሰጠ ፋንክሽን $f(\theta)$፣ $f(\theta)=\sqrt{a^2+b^2} \sin(\theta+\alpha) = \sqrt{a^2+b^2} \cos(\theta-\beta)$ እንዲሆን የሚያደርጉ እውነተኛ ቁጥሮች $\alpha$, $\beta$ ሁልጊዜ ይኖራሉ።

![Geometric Derivation of the Harmonic Addition Theorem](/assets/img/trigonometry/harmonic-addition.png)

በስዕሉ ውስጥ እንደሚታየው፣ በመጋጠሚያ አውታረ ሰሌዳው ላይ $P(a,b)$ የሚለውን ነጥብ እንወስድ፣ እና መስመር ክፍሉ $\overline{OP}$ ከ$x$-ዘንግ አዎንታዊ አቅጣጫ ጋር የሚፈጥረውን ማዕዘን $\alpha$ ብለን እንሰይም፤

$$ \overline{OP} = \sqrt{a^2+b^2} $$

እና

$$ \cos \alpha = \frac{a}{\sqrt{a^{2} + b^{2}}},\ \sin \alpha = \frac{b}{\sqrt{a^{2} + b^{2}}} \tag{1} $$

ይሆናል። በዚህ ጊዜ፣

$$ \begin{align*}
a \sin \theta + b \cos \theta &= \sqrt{a^{2}+b^{2}} \left(\frac{a}{\sqrt{a^{2}+b^{2}}}\sin \theta + \frac{b}{\sqrt{a^{2}+b^{2}}}\cos \theta \right) \\
&= \sqrt{a^{2}+b^{2}}(\cos \alpha \sin \theta + \sin \alpha \cos \theta) \\
&= \sqrt{a^{2}+b^{2}} \sin(\theta + \alpha). \tag{2}
\end{align*} $$

በተመሳሳይ መንገድ፣ ነጥብ $P^{\prime}(b,a)$ እንወስድ እና መስመር ክፍሉ $\overline{OP^{\prime}}$ ከ$x$-ዘንግ አዎንታዊ አቅጣጫ ጋር የሚፈጥረውን ማዕዘን $\beta$ ብለን ከሰየምነው፣ የሚከተለውን እናገኛለን።

$$ a \sin \theta + b \cos \theta = \sqrt{a^{2}+b^{2}}\cos(\theta-\beta). \tag{3} $$

$$ እዚህ፣\ \cos \beta = \frac{b}{\sqrt{a^{2}+b^{2}}},\ \sin \beta = \frac{a}{\sqrt{a^{2}+b^{2}}}. $$

እንዲህ በማድረግ $a \sin \theta + b \sin \theta$ ቅርጽ ያለውን የትሪጎኖሜትሪ ፋንክሽን ወደ $r\sin(\theta+\alpha)$ ወይም $r\cos(\theta-\beta)$ ቅርጽ መቀየር የትሪጎኖሜትሪ ፋንክሽኖች ውህደት(Harmonic Addition) ተብሎ ይጠራል።

## ምሳሌ
ፋንክሽኑ $f(\theta)=-\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right)$ ተሰጥቶ ከሆነ፣ በክልሉ $[0, 2\pi]$ ላይ ያለውን የፋንክሽኑ $f(\theta)$ ከፍተኛ እና ዝቅተኛ እሴት ፈልጉ።

### 1. ወደ $a\sin\theta + b\cos\theta$ ቅርጽ መቀየር
[የትሪጎኖሜትሪ ድምር መለያዎች](/posts/trigonometric-addition-formulas)ን በመጠቀም የተሰጠውን የፋንክሽን አገላለጽ እንቀይራለን፤

$$ \begin{align*}
f(\theta) &= -\sqrt{3}\sin \theta + \cos \left(\theta - \frac{\pi}{3} \right) \\
&= -\sqrt{3}\sin \theta + \left( \cos\theta \cos\frac{\pi}{3} + \sin\theta \sin\frac{\pi}{3} \right) \\
&= -\frac{\sqrt{3}}{2}\sin\theta + \frac{1}{2}\cos\theta .
\end{align*} $$

### 2. ወደ $r\sin(\theta+\alpha)$ ቅርጽ መቀየር
$a=-\frac{\sqrt{3}}{2}$, $b=\frac{1}{2}$ ብለን ካስቀመጥን፣

$$ r = \sqrt{a^2+b^2} = \sqrt{\frac{3}{4}+\frac{1}{4}} = 1 $$

ይሆናል።

እንዲሁም፣ $0 \leq \alpha<2\pi$ እና $\cos\alpha = a$, $\sin\alpha = b$ የሚያሟላ እውነተኛ ቁጥር $\alpha$ አንድ ብቻ አለ። ከልዩ ማዕዘኖች የትሪጎኖሜትሪ ሬሾ እሴቶች በመጠቀም፣ $\alpha = \frac{5}{6}\pi$ መሆኑን እናውቃለን። 

ስለዚህ፣ የተሰጠውን ፋንክሽን $f(\theta)$ ወደ $r\sin(\theta+\alpha)$ ቅርጽ ስንቀይረው የሚከተለውን እናገኛለን።

$$ f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right). $$

### 3. በተሰጠው ክልል ውስጥ ከፍተኛ እና ዝቅተኛ እሴቶችን ማግኘት
![Graph of the given function](/assets/img/trigonometry/harmonic-addition-ex-graph.png)

ፋንክሽኑ $f(\theta) = \sin \left(\theta + \frac{5\pi}{6} \right)$ ወቅቱ $2\pi$ የሆነ ወቅታዊ ፋንክሽን ሲሆን፣ በተሰጠው ክልል ውስጥ ከፍተኛ እሴቱ $1$ እና ዝቅተኛ እሴቱ $-1$ ነው።

$$ \therefore M=1,\ m=-1$$
