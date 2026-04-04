---
title: "የሃርሞኒክ ኦሲሌተር(The Harmonic Oscillator) ትንታኔያዊ መፍትሔ"
description: "በኳንተም መካኒክስ ውስጥ ለሃርሞኒክ ኦሲሌተር የሽሮዲንገር ስሌትን እንመሰርታለን፣ እና ትንታኔያዊ መፍትሔውን እንመለከታለን። መጠን-አልባ ተለዋዋጭ 𝜉ን በማስገባት ስሌቱን እንፈታለን፣ እና ማንኛውንም ኖርማላይዝ የተደረገ ቋሚ ሁኔታ በኤርሚት ፖሊኖሚያሎች እንገልጻለን።"
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hermite Polynomials]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---

## TL;DR

> - አምፕሊቱዱ(amplitude) በበቂ ሁኔታ ትንሽ ከሆነ፣ ማንኛውም ንዝረት እንደ ቀላል ሃርሞኒክ ንዝረት(simple harmonic oscillation) ሊጠጋገም ይችላል፤ በዚህም ምክንያት ቀላል ሃርሞኒክ ንዝረት በፊዚክስ ውስጥ ጠቃሚ ትርጉም አለው
> - ሃርሞኒክ ኦሲሌተር: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - መጠን-አልባ ተለዋዋጭ $\xi$ እና በ $\cfrac{1}{2}\hbar\omega$ አሃድ የተገለጸ ኃይል $K$ ማስገባት:
>   - $\xi \equiv \sqrt{\cfrac{m\omega}{\hbar}}x$
>   - $K \equiv \cfrac{2E}{\hbar\omega}$
>   - $ \cfrac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi $
> - $\|\xi\|^2 \to \infty$ ሲሆን በአካላዊ ሁኔታ የሚፈቀደው አሰምፕቶቲክ መፍትሔ(asymptotic solution) $\psi(\xi) \to Ae^{-\xi^2/2}$ ስለሆነ፣
>
> $$ \begin{gather*}
> \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(ነገር ግን }\lim_{\xi\to\infty}h(\xi)=A\text{)}, \\
> \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0
> \end{gather*} $$
>
> - የላይኛውን ስሌት መፍትሔ በተከታታይ ቅርጽ $ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j$ እንደሚከተለው ብንገልጸው፣
>
> $$ a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j $$
>
> - ይህ መፍትሔ ኖርማላይዝ ለመሆን ተከታታዩ $\sum a_j$ ውስን መሆን አለበት፤ ማለትም አንድ ‘ከፍተኛው’ $j$ እሴት $n\in \mathbb{N}$ መኖር አለበት እና $j>n$ ሲሆን $a_j=0$ መሆን አለበት፣ ስለዚህ
>   - $ K = 2n + 1 $
>   - $ E_n = \left(n+\cfrac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots $
> - በአጠቃላይ $h_n(\xi)$ በ $\xi$ ላይ የ $n$ ኛ ደረጃ ፖሊኖሚያል ሲሆን፣ ከፊት ያለውን ኮፊሺየንት($a_0$ ወይም $a_1$) ሲያስወግዱ የቀረውን **ኤርሚት ፖሊኖሚያሎች(Hermite polynomials)** $H_n(\xi)$ ብለን እንጠራዋለን
>
> $$ h_n(\xi) = 
> \begin{cases}
> a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
> a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
> \end{cases} $$
>
> - የሃርሞኒክ ኦሲሌተሩ ኖርማላይዝ የተደረጉ ቋሚ ሁኔታዎች:
>
> $$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2} $$
>
> - የኳንተም ኦሲሌተሩ ባህሪያት
>   - እንደ ኢገንፋንክሽን(eigenfunction) ጥንድ ፋንክሽኖች እና ነጠላ ፋንክሽኖች ተፈራርቀው ይታያሉ
>   - በክላሲካል መካኒክስ መኖር የማይችል ክልል ውስጥም(ለተሰጠው $E$ ከክላሲካል አምፕሊቱድ የሚበልጥ $x$) የመገኘት እድሉ $0$ አይደለም፣ ዝቅተኛ እድል ቢሆንም ነጠላ ቅንጣቱ ሊኖር ይችላል
>   - $n$ ነጠላ ለሆነ ሁሉም ቋሚ ሁኔታዎች ላይ ቅንጣቱን በመሃል የማግኘት እድል $0$ ነው
>   - $n$ በበለጠ መጠን ሲጨምር ከክላሲካል ኦሲሌተር ጋር ይመሳሰላል
{: .prompt-info }

## ቅድመ እውቀቶች

- [የተለዋዋጮች መለያየት ዘዴ](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [የሽሮዲንገር(Schrödinger) ስሌት እና የሞገድ ፋንክሽን](/posts/schrodinger-equation-and-the-wave-function/)
- [የኤረንፌስት(Ehrenfest) ቲዮረም](/posts/ehrenfest-theorem/)
- [ከጊዜ ጋር የማይዛመድ የሽሮዲንገር(Schrödinger) ስሌት](/posts/time-independent-schrodinger-equation/)
- [1-ልኬት ያለ ወሰን ካሬ ጉድጓድ(The 1D Infinite Square Well)](/posts/the-infinite-square-well/)
- [የሃርሞኒክ ኦሲሌተር(The Harmonic Oscillator) አልጀብራዊ መፍትሔ](/posts/algebraic-solution-of-the-harmonic-oscillator/)

## የሞዴሉ ቅንብር

በክላሲካል መካኒክስ ውስጥ የሃርሞኒክ ኦሲሌተርን እንዴት እንደሚገልጹ እና የሃርሞኒክ ኦሲሌተር ችግኝ ያለውን አስፈላጊነት በተመለከተ [ቀደም ባለው ጽሑፍ](/posts/algebraic-solution-of-the-harmonic-oscillator/) ይመልከቱ።

### በኳንተም መካኒክስ ውስጥ ያለ ሃርሞኒክ ኦሲሌተር

በኳንተም መካኒክስ ያለው የሃርሞኒክ ኦሲሌተር ችግኝ ፖቴንሺያሉ

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{1}$$

የሆነበትን የሽሮዲንገር ስሌት መፍታት ነው። ለሃርሞኒክ ኦሲሌተር [ከጊዜ ጋር የማይዛመድ የሽሮዲንገር ስሌት](/posts/time-independent-schrodinger-equation/) የሚከተለው ነው።

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

ይህን ችግኝ ለመፍታት ፍጹም የተለያዩ ሁለት አቀራረቦች አሉ። አንዱ **የኃይል ተከታታይ ዘዴ(power series method)**ን የሚጠቀም ትንታኔያዊ ዘዴ(analytic method) ሲሆን፣ ሌላው ደግሞ **ላደር ኦፕሬተሮች(ladder operators)**ን የሚጠቀም አልጀብራዊ ዘዴ(algebraic method) ነው። አልጀብራዊ ዘዴው ፈጣንና ቀላል ቢሆንም፣ የኃይል ተከታታይ በመጠቀም የሚሰጠውን ትንታኔያዊ መፍትሔም ማጥናት ያስፈልጋል። [ከዚህ በፊት አልጀብራዊውን የመፍትሔ ዘዴ አይተናል](/posts/algebraic-solution-of-the-harmonic-oscillator/)፣ እዚህ ግን ትንታኔያዊውን የመፍትሔ ዘዴ እንመለከታለን።

## የሽሮዲንገር ስሌቱን መለወጥ

መጠን-አልባው ተለዋዋጭ

$$ \xi \equiv \sqrt{\frac{m\omega}{\hbar}}x \label{eqn:xi}\tag{3}$$

እንደሚከተለው ከገባን፣ ከጊዜ ጋር የማይዛመደውን የሽሮዲንገር ስሌት ($\ref{eqn:t_independent_schrodinger_eqn}$) በቀላሉ እንዲህ ማድረግ እንችላለን።

$$ \frac{d^2\psi}{d\xi^2} = \left(\xi^2-K \right)\psi. \label{eqn:schrodinger_eqn_with_xi}\tag{4}$$

እዚህ $K$ በ $\cfrac{1}{2}\hbar\omega$ አሃድ የተገለጸ ኃይል ነው።

$$ K \equiv \frac{2E}{\hbar\omega}. \label{eqn:K}\tag{5}$$

አሁን ይህን እንደገና የተጻፈውን ስሌት ($\ref{eqn:schrodinger_eqn_with_xi}$) መፍታት ነው። በመጀመሪያ ለበጣም ትልቅ $\xi$ (ማለትም ለበጣም ትልቅ $x$) $\xi^2 \gg K$ ስለሆነ፣

$$ \frac{d^2\psi}{d\xi^2} \approx \xi^2\psi \label{eqn:schrodinger_eqn_approx}\tag{6}$$

ይሆናል፣ እና ይህ የሚኖረው ግምታዊ መፍትሔ

$$ \psi(\xi) \approx Ae^{-\xi^2/2} + Be^{\xi^2/2} \label{eqn:psi_approx}\tag{7}$$

ነው። ነገር ግን እዚህ $B$ ተርሙ $\|x\|\to \infty$ ሲሆን ይፈነዳል እና ኖርማላይዝ ማድረግ አይቻልም፤ ስለዚህ በአካላዊ ሁኔታ የሚፈቀደው አሰምፕቶቲክ መፍትሔ

$$ \psi(\xi) \to Ae^{-\xi^2/2} \label{eqn:psi_asymp}\tag{8}$$

ነው። አሁን እዚህ ኤክስፖነንሻል ክፍሉን ለይተን

$$ \psi(\xi) = h(\xi)e^{-\xi^2/2} \quad \text{(ነገር ግን }\lim_{\xi\to\infty}h(\xi)=A\text{)} \label{eqn:psi_and_h}\tag{9}$$

ብለን እንጻፍ።

> ኤክስፖነንሻሉን $e^{-\xi^2/2}$ ለማግኘት በየአመጣጡ ሂደት ውስጥ የተጠቀምነው ግምታዊ ዘዴ የአሰምፕቶቲክ መፍትሔውን ቅርጽ ለማግኘት ብቻ ነበር፤ ነገር ግን በዚህ መንገድ ያገኘነው ስሌት ($\ref{eqn:psi_and_h}$) ግምታዊ ሳይሆን ትክክለኛ ስሌት ነው። እንደዚህ ያለ አሰምፕቶቲክ ቅርጽ ማለየት የዲፈረንሻል ስሌቶችን በኃይል ተከታታይ ቅርጽ ሲፈቱ የሚጠቀሙት መደበኛ የመጀመሪያ ደረጃ ነው።
{: .prompt-info }

ስሌት ($\ref{eqn:psi_and_h}$) ን በመድፈር $\cfrac{d\psi}{d\xi}$ እና $\cfrac{d^2\psi}{d\xi^2}$ ን ካገኘን፣

$$ \begin{gather*}
\frac{d\psi}{d\xi} = \left(\frac{dh}{d\xi}-\xi h \right)e^{-\xi^2/2}, \\
\frac{d^2\psi}{d\xi^2} = \left(\frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(\xi^2-1)h \right)e^{-\xi^2/2}
\end{gather*} $$

ስለሆነ የሽሮዲንገር ስሌቱ ($\ref{eqn:schrodinger_eqn_with_xi}$) አሁን

$$ \frac{d^2h}{d\xi^2}-2\xi\frac{dh}{d\xi}+(K-1)h = 0 \label{eqn:schrodinger_eqn_with_h}\tag{10}$$

ይሆናል።

## የኃይል ተከታታይ ዝርጋታ

በቴይለር ቲዎረም(Taylor's theorem) መሠረት ማንኛውም ለስላሳ የሆነ ፋንክሽን በኃይል ተከታታይ ሊገለጽ ስለሚችል፣ የስሌት ($\ref{eqn:schrodinger_eqn_with_h}$) መፍትሔን በ $\xi$ ላይ ያለ ተከታታይ

$$ h(\xi) = a_0 + a_1\xi + a_2\xi^2 + \cdots = \sum_{j=0}^{\infty}a_j\xi^j \label{eqn:h_series_exp}\tag{11}$$

ቅርጽ እንፈልግ። የዚህን ተከታታይ እያንዳንዱን ተርም ከደፈርን በኋላ የሚከተሉትን ሁለት ስሌቶች እናገኛለን።

$$ \begin{gather*}
\frac{dh}{d\xi} = a_1 + 2a_2\xi + 3a_3\xi^2 + \cdots = \sum_{j=0}^{\infty}ja_j\xi^{j-1}, \\
\frac{d^2 h}{d\xi^2} = 2a_2 + 2\cdot3a_3\xi + 3\cdot4a_4\xi^2 + \cdots = \sum_{j=0}^{\infty} (j+1)(j+2)a_{j+2}\xi^j.
\end{gather*} $$

እነዚህን ሁለት ስሌቶች ወደ የሽሮዲንገር ስሌቱ(ስሌት [$\ref{eqn:schrodinger_eqn_with_h}$]) እንደገና ብናስገባ የሚከተለውን እናገኛለን።

$$ \sum_{j=0}^{\infty}[(j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j]\xi^j = 0. \label{eqn:schrodinger_eqn_power_series}\tag{12}$$

በኃይል ተከታታይ ዝርጋታ ልዩነት ምክንያት ለእያንዳንዱ የ $\xi$ ደረጃ ያለው ኮፊሺየንት $0$ መሆን አለበት፣ ስለዚህ

$$ (j+1)(j+2)a_{j+2} - 2ja_j + (K-1)a_j = 0 $$

$$ \therefore a_{j+2} = \frac{(2j+1-K)}{(j+1)(j+2)}a_j. \label{eqn:recursion_formula}\tag{13}$$

ይሆናል። ይህ **የተደጋጋሚ ግንኙነት(recursion formula)** ከየሽሮዲንገር ስሌቱ ጋር እኩል ነው። ሁለት የዘፈቀደ ቋሚዎች $a_0$ እና $a_1$ ከተሰጡ፣ የመፍትሔውን $h(\xi)$ ሁሉንም ተርሞች ኮፊሺየንቶች ማግኘት እንችላለን።

ነገር ግን በዚህ የተገኘው መፍትሔ ሁልጊዜ ኖርማላይዝ ሊደረግ ይችላል ማለት አይደለም። ተከታታዩ $\sum a_j$ ወሰን የሌለው ተከታታይ ከሆነ($\lim_{j\to\infty} a_j\neq0$ ከሆነ)፣ ለበጣም ትልቅ $j$ ከላይ ያለው የተደጋጋሚ ግንኙነት በግምት

$$ a_{j+2} \approx \frac{2}{j}a_j $$

ይሆናል፣ እና ለዚህ ያለው ግምታዊ መፍትሔ

$$ a_j \approx \frac{C}{(j/2)!} \quad \text{(}C\text{ የዘፈቀደ ቋሚ ነው)}$$

ነው። በዚህ ሁኔታ ከፍተኛ ደረጃ ተርሞች የሚቆጣጠሩባቸው ትልቅ $\xi$ እሴቶች ላይ

$$ h(\xi) \approx C\sum\frac{1}{(j/2)!}\xi^j \approx C\sum\frac{1}{j!}\xi^{2j} \approx Ce^{\xi^2} $$

ዓይነት ቅርጽ ይኖረዋል፣ እንዲሁም $h(\xi)$ የ $Ce^{\xi^2}$ ቅርጽ ከሆነ በስሌት ($\ref{eqn:psi_and_h}$) ውስጥ ያለው $\psi(\xi)$ የ $Ce^{\xi^2/2}$ ቅርጽ ይወስዳል እና $\xi \to \infty$ ሲሆን ይፈነዳል። ይህ በስሌት ($\ref{eqn:psi_approx}$) ውስጥ $A=0, B\neq0$ የሆነውን ኖርማላይዝ ሊደረግ የማይችል መፍትሔ ይወክላል።

ስለዚህ ተከታታዩ $\sum a_j$ ውስን መሆን አለበት። አንድ ‘ከፍተኛው’ $j$ እሴት $n\in \mathbb{N}$ መኖር አለበት እና $j>n$ ሲሆን $a_j=0$ መሆን አለበት፤ ይህም እንዲሆን ለ $0$ ያልሆነ $a_n$ የ $a_{n+2}=0$ መሆን አለበት፣ ስለዚህ ከስሌት ($\ref{eqn:recursion_formula}$) 

$$ K = 2n + 1 $$

መሆን አለበት። ይህን ወደ ስሌት ($\ref{eqn:K}$) ብንተካ፣ በአካላዊ ሁኔታ የሚፈቀዱ ኃይሎች

$$ E_n = \left(n+\frac{1}{2} \right)\hbar\omega, \quad n=0,1,2,\dots \label{eqn:E_n}\tag{14}$$

እናገኛለን። በዚህም [የሃርሞኒክ ኦሲሌተር ቋሚ ሁኔታዎች $\psi_n$ እና የኃይል ደረጃ $E_n$](/posts/algebraic-solution-of-the-harmonic-oscillator/#%E1%89%8B%E1%88%9A-%E1%88%81%E1%8A%94%E1%89%B3-%24%5Cpsi_n%24-%E1%8A%A5%E1%8A%93-%E1%8B%A8%E1%8A%83%E1%8B%AD%E1%88%8D-%E1%8B%B0%E1%88%A8%E1%8C%83-%24E_n%24) በሚለው ክፍል ውስጥ ያለውን ስሌት (21) የኃይል መጠን-ተከፋፈል ሁኔታ ሙሉ በሙሉ በተለየ መንገድ ተጠቅመን እንደገና አግኝተናል።

## ኤርሚት ፖሊኖሚያሎች (Hermite polynomials) $H_n(\xi)$ እና ቋሚ ሁኔታዎች $\psi_n(x)$

### ኤርሚት ፖሊኖሚያሎች $H_n$

በአጠቃላይ $h_n(\xi)$ በ $\xi$ ላይ የ $n$ ኛ ደረጃ ፖሊኖሚያል ነው፣ እና $n$ ጥንድ ከሆነ ጥንድ ደረጃዎችን ብቻ፣ $n$ ነጠላ ከሆነ ደግሞ ነጠላ ደረጃዎችን ብቻ ያካትታል። እዚህ ከፊት ያለውን ኮፊሺየንት($a_0$ ወይም $a_1$) ካስወገድን የቀረውን **ኤርሚት ፖሊኖሚያሎች(Hermite polynomials)** $H_n(\xi)$ ብለን እንጠራዋለን።

$$ h_n(\xi) = 
\begin{cases}
a_0 H_n(\xi), & n=2k & (k=0,1,2,\dots) \\
a_1 H_n(\xi), & n=2k+1 & (k=0,1,2,\dots)
\end{cases} $$

በባህላዊ መንገድ $H_n$ ውስጥ ያለው ከፍተኛ ደረጃ ተርም ኮፊሺየንት $2^n$ እንዲሆን ኮፊሺየንቱን በዘፈቀደ ይመርጣሉ።

የሚከተሉት የመጀመሪያ ጥቂት ኤርሚት ፖሊኖሚያሎች ናቸው።

$$ \begin{align*}
H_0 &= 1 \\
H_1 &= 2\xi \\
H_2 &= 4\xi^2 - 2 \\
H_3 &= 8\xi^3 - 12\xi \\
H_4 &= 16\xi^4 - 48\xi^2 + 12 \\
H_5 &= 32\xi^5 - 160\xi^3 + 120\xi \\
&\qquad\vdots
\end{align*} $$

### ቋሚ ሁኔታዎች $\psi_n(x)$

ለሃርሞኒክ ኦሲሌተር ያሉት ኖርማላይዝ የተደረጉ ቋሚ ሁኔታዎች እንደሚከተለው ናቸው።

$$ \psi_n(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4} \frac{1}{\sqrt{2^n n!}}H_n(\xi)e^{-\xi^2/2}. $$

ይህ በ [የሃርሞኒክ ኦሲሌተር አልጀብራዊ መፍትሔ](/posts/algebraic-solution-of-the-harmonic-oscillator/#%E1%8A%96%E1%88%AD%E1%88%9B%E1%88%8B%E1%8B%AD%E1%8B%9C%E1%88%BD%E1%8A%95) ውስጥ ያገኘነው ውጤት(ስሌት [27]) ጋር ይጣጣማል።

የሚከተለው ምስል ለመጀመሪያዎቹ 8 የ $n$ እሴቶች ቋሚ ሁኔታዎች $\psi_n(x)$ እና የፕሮባቢሊቲ ዴንሲቲ(probability density) $\|\psi_n(x)\|^2$ ን ያሳያል። የኳንተም ኦሲሌተሩ ኢገንፋንክሽኖች እንደ ጥንድ ፋንክሽን እና ነጠላ ፋንክሽን ተፈራርቀው እንደሚታዩ ማየት ይቻላል።

![Wavefunction representations for the first eight bound eigenstates, n = 0 to 7. The horizontal axis shows the position x.](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png)
> *የምስል ምንጭ*
> - ደራሲ: የዊኪሚዲያ ተጠቃሚ [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - ፈቃድ: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)

![Corresponding probability densities.](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)
> *የምስል ምንጭ*
> - ደራሲ: የዊኪሚዲያ ተጠቃሚ [AllenMcC](https://commons.wikimedia.org/wiki/User:AllenMcC.)
> - ፈቃድ: Public Domain

የኳንተም ኦሲሌተሩ ከእርሱ ጋር የሚመሳሰለው ክላሲካል ኦሲሌተር በጣም የተለየ ሲሆን፣ ኃይሉ መጠን-ተከፋፈል መሆኑ ብቻ ሳይሆን የቦታ $x$ ፕሮባቢሊቲ ስርጭቱም እንግዳ የሆኑ ባህሪያትን ያሳያል።
- በክላሲካል መካኒክስ መኖር የማይችል ክልል ውስጥም(ለተሰጠው $E$ ከክላሲካል አምፕሊቱድ የሚበልጥ $x$) የመገኘት እድሉ $0$ አይደለም፣ ዝቅተኛ እድል ቢሆንም ቅንጣቱ ሊኖር ይችላል
- $n$ ነጠላ ለሆነ ሁሉም ቋሚ ሁኔታዎች ላይ ቅንጣቱን በመሃል የማግኘት እድል $0$ ነው

$n$ እየጨመረ ሲሄድ የኳንተም ኦሲሌተሩ ከክላሲካል ኦሲሌተሩ ጋር የሚመሳሰል ገጽታ ያሳያል። ከታች ያለው ምስል የቦታ $x$ ክላሲካል ፕሮባቢሊቲ ስርጭት(ተቋረጠ መስመር) እና $n=30$ ሲሆን ያለው የኳንተም ሁኔታ $\|\psi_{30}\|^2$(ቀጥታ መስመር) ን ያሳያል። የተንቀጠቀጡትን ክፍሎች ለስላሳ ካደረግናቸው ሁለቱ ግራፎች በግምት ተመሳሳይ ቅርጽ እንዳላቸው ማየት ይቻላል።

![Quantum (solid) and classical (dashed) probability distributions of the n = 30 excited state of the quantum harmonic oscillator. The vertical dashed lines represent the classical turning points.](https://upload.wikimedia.org/wikipedia/commons/6/69/QHOn30pdf.svg)
> *የምስል ምንጭ*
> - ደራሲ: የዊኪሚዲያ ተጠቃሚ [AkanoToE](https://commons.wikimedia.org/wiki/User:AkanoToE)
> - ፈቃድ: Public Domain

### የኳንተም ኦሲሌተር ፕሮባቢሊቲ ስርጭቶች መስተጋብራዊ ማሳያ

የሚከተለው እኔ ራሴ የጻፍኩት በ Plotly.js ላይ የተመሠረተ ምላሽ-ሰጪ ምስላዊ ማሳያ ነው። በስላይደሩ የ $n$ እሴትን እያስተካከሉ ለቦታ $x$ ያለውን ክላሲካል ፕሮባቢሊቲ ስርጭት እና $\|\psi_n\|^2$ ያለውን ቅርጽ ማየት ይችላሉ።

<div class="plotly-iframe-container" style="position: relative; height: 850px; overflow: hidden;">
    <iframe id="plotly-iframe"
            src="/physics-visualizations/quantum-harmonic-oscillator.html"
            title="Quantum Harmonic Oscillator: Probability Density"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; overflow:hidden" 
            allow="fullscreen"
            scrolling="no"
            loading="lazy">
    </iframe>
</div>

> - የመጀመሪያው ምስላዊ ማሳያ ገጽ: <a {% static_href %}href="{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html"{% endstatic_href %}>{{site.url}}/physics-visualizations/quantum-harmonic-oscillator.html</a>
> - ምንጭ ኮድ: [የ yunseo-kim/physics-visualizations ሪፖዚቶሪ](https://github.com/yunseo-kim/physics-visualizations/blob/main/quantum-harmonic-oscillator.html)
> - ፈቃድ: [እዚህ ይመልከቱ](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

በተጨማሪም፣ በራስዎ ኮምፒውተር ላይ Python መጠቀም የሚችሉ ከሆነ እና Numpy, Plotly, Dash ቤተ-መጻሕፍት የተጫኑበት አካባቢ ካለ፣ በዚያው ሪፖዚቶሪ ውስጥ ያለውን [`/src/quantum_oscillator.py`{: .filepath}](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/quantum_oscillator.py) የ Python ስክሪፕት በማስኬድ ውጤቱን ማየት ይችላሉ።
