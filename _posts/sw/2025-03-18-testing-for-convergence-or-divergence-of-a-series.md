---
title: Vigezo vya Kukagua Ukonverjensia/Utofautikaji wa Msururu
description: Muhtasari wa mbinu mbalimbali za kukagua kama msururu unakonverjia au unatofautika.
categories: [Mathematics, Calculus]
tags: [Sequence, Series, Convergence, Divergence, Limit]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - **Kigezo cha neno la jumla ($n$th-term test for divergence)**: $\lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{msururu }\sum a_n \text{ unatofautika}$
> - **Ukonverjensia/utofautikaji wa mfululizo wa kijiometri**: mfululizo wa kijiometri $\sum ar^{n-1}$:
>   - ukiwa na $\|r\| < 1$ unakonverjia
>   - ukiwa na $\|r\| \geq 1$ unatofautika
> - **Ukonverjensia/utofautikaji wa $p$-msururu**: $p$-msururu $\sum \cfrac{1}{n^p}$:
>   - ikiwa $p>1$ unakonverjia
>   - ikiwa $p\leq 1$ unatofautika
> - **Kigezo cha ulinganishi (Comparison Test)**: wakati $0 \leq a_n \leq b_n$,  
>   - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
>   - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
> - **Kigezo cha ulinganishi wa kikomo (Limit Comparison Test)**: ikiwa $\lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ ni namba chanya yenye kikomo)}$, basi misururu miwili $\sum a_n$ na $\sum b_n$ aidha yote miwili inakonverjia au yote miwili inatofautika
> - Kwa msururu wa viungo chanya $\sum a_n$ na namba chanya $\epsilon < 1$,  
>   - ikiwa kwa kila $n$, $\sqrt[n]{a_n}< 1-\epsilon$, basi msururu $\sum a_n$ unakonverjia
>   - ikiwa kwa kila $n$, $\sqrt[n]{a_n}> 1+\epsilon$, basi msururu $\sum a_n$ unatofautika
> - **Kigezo cha mzizi (Root Test)**: kwa msururu wa viungo chanya $\sum a_n$, ikiwa kikomo $\lim_{n\to\infty} \sqrt[n]{a_n} =: r$ kipo,
>   - ikiwa $r<1$, msururu $\sum a_n$ unakonverjia
>   - ikiwa $r>1$, msururu $\sum a_n$ unatofautika
> - **Kigezo cha uwiano (Ratio Test)**: kwa mfuatano chanya $(a_n)$ na $0 < r < 1$
>   - ikiwa kwa kila $n$, $a_{n+1}/a_n \leq r$, basi msururu $\sum a_n$ unakonverjia
>   - ikiwa kwa kila $n$, $a_{n+1}/a_n \geq 1$, basi msururu $\sum a_n$ unatofautika
> - Katika mfuatano chanya $(a_n)$, tukidhania kuwa kikomo $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ kipo,
>   - ikiwa $\rho < 1$, basi msururu $\sum a_n$ unakonverjia
>   - ikiwa $\rho > 1$, basi msururu $\sum a_n$ unatofautika
> - **Kigezo cha jumuisho (Integral Test)**: ikiwa funksi endelevu $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ inapungua na daima $f(x)>0$, basi sharti la lazima na la kutosha kwa msururu $\sum f(n)$ kukonverjia ni kwamba jumuisho $\int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx$ likonverjie
> - **Kigezo cha msururu mbadala (Alternating Series Test)**: msururu mbadala $\sum a_n$ unakonverjia iwapo masharti yafuatayo yanatimizwa
>   1. Kwa kila $n$, $a_n$ na $a_{n+1}$ zina alama tofauti
>   2. Kwa kila $n$, $\|a_n\| \geq \|a_{n+1}\|$
>   3. $\lim_{n\to\infty} a_n = 0$
> - Msururu unaokonverjia kiabsolute unakonverjia. Kinyume chake si kweli.
{: .prompt-info }

## Yanayohitajika kabla
- [Mfuatano na Misururu](/posts/sequences-and-series/)

## Utangulizi
Hapo awali katika [Mfuatano na Misururu](/posts/sequences-and-series/#ukonverjensia-na-utofautikaji-wa-misururu), tuliangalia ufafanuzi wa ukonverjensia na utofautikaji wa misururu. Katika makala hii, tunapanga mbinu mbalimbali zinazoweza kutumika kukagua ukonverjensia/utofautikaji wa msururu. Kwa jumla, kukagua ukonverjensia/utofautikaji wa msururu ni rahisi zaidi kuliko kupata kwa usahihi jumla ya msururu huo.

## Kigezo cha neno la jumla
Kwa msururu $\sum a_n$, tunaita $a_n$ **neno la jumla** la msururu huo.

Kwa nadharia ifuatayo, tunaweza kujua kwa urahisi kuwa baadhi ya misururu hutofautika kwa dhahiri; kwa hiyo, unapokagua ukonverjensia/utofautikaji wa msururu wowote, ni jambo la busara kuangalia hili kwanza ili kuepuka kupoteza muda.

> **Kigezo cha neno la jumla ($n$th-term test for divergence)**  
> Ikiwa msururu $\sum a_n$ unakonverjia, basi
>
> $$ \lim_{n\to\infty} a_n=0 $$
>
> yaani,
>
> $$ \lim_{n\to\infty} a_n \neq 0 \Rightarrow \text{msururu }\sum a_n \text{ unatofautika} $$
>
> ni kweli.
{: .prompt-info }

### Uthibitisho
Tuchukulie jumla ya msururu unaokonverjia $\sum a_n$ kuwa $l$, na jumla ya viungo vya kwanza hadi la $n$ iwe

$$ s_n := a_1 + a_2 + \cdots + a_n $$

basi

$$ \forall \epsilon > 0,\, \exists N \in \mathbb{N}\ (n > N \Rightarrow |s_n - l| < \epsilon). $$

Kwa hiyo, kwa $n$ kubwa vya kutosha ($>N$),

$$ |a_n| = |s_n - s_{n-1}| = |(s_n - l) - (s_{n-1} - l)| \leq |s_n - l| + |s_{n-1} - l| \leq \epsilon + \epsilon = 2\epsilon $$

na hivyo, kutokana na ufafanuzi wa ukonverjensia wa mfuatano,

$$ \lim_{n\to\infty} |a_n| = 0. \quad \blacksquare $$

### Tahadhari
Kinyume cha nadharia hii kwa ujumla si kweli. Mfano mashuhuri unaoonyesha hili ni **msururu wa harmoniki (harmonic series)**.

Msururu wa harmoniki ni msururu unaotokana na mfuatano ambao viungo vyake ni vipatanishi vya **mfuatano wa hesabu**; yaani, **mfuatano wa harmoniki**. Mfano maarufu wa msururu wa harmoniki ni

$$ H_n := 1 + \frac{1}{2} + \cdots + \frac{1}{n} \quad (n=1,2,3,\dots) $$

Msururu huu unaweza kuonyeshwa kutofautika kama ifuatavyo:

$$ \begin{align*}
\lim_{n\to\infty} H_n &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \frac{1}{9} + \cdots + \frac{1}{16} + \cdots \\
&> 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{16} + \cdots + \frac{1}{16} + \cdots \\
&= 1 + \frac{1}{2} \qquad\, + \frac{1}{2} \qquad\qquad\qquad\ \ + \frac{1}{2} \qquad\qquad\quad + \frac{1}{2} + \cdots \\
&= \infty.
\end{align*} $$

Hivyo, ingawa msururu $H_n$ unatofautika, tunaona kwamba neno lake la jumla $1/n$ linakonverjia kwenda $0$.

> Ikiwa $\lim_{n\to\infty} a_n \neq 0$, basi msururu $\sum a_n$ lazima utatofautika. Lakini ni hatari kudhani kwamba $\lim_{n\to\infty} a_n = 0$ inamaanisha moja kwa moja kuwa msururu $\sum a_n$ unakonverjia; katika hali hiyo lazima tutumie mbinu nyingine kukagua ukonverjensia/utofautikaji.
{: .prompt-danger }

## Mfululizo wa kijiometri
**Mfululizo wa kijiometri (geometric series)** unaotokana na mfuatano wa kijiometri wenye kiungo cha kwanza 1 na **uwiano wa pamoja** $r$,

$$ 1 + r + r^2 + r^3 + \cdots \label{eqn:geometric_series}\tag{5}$$

ni <u>miongoni mwa misururu muhimu zaidi na ya msingi kabisa</u>. Kutoka kwenye usawa

$$ (1-r)(1+r+\cdots + r^{n-1}) = 1 - r^n $$

tunapata

$$ 1 + r + \cdots + r^{n-1} = \frac{1-r^n}{1-r} = \frac{1}{1-r} - \frac{r^n}{1-r} \qquad (r \neq 1) \label{eqn:sum_of_geometric_series}\tag{6}$$

Wakati huohuo,

$$ \lim_{n\to\infty} r^n = 0 \quad \Leftrightarrow \quad |r| < 1 $$

kwa hiyo tunajua kuwa sharti la lazima na la kutosha kwa mfululizo wa kijiometri ($\ref{eqn:geometric_series}$) kukonverjia ni $\|r\| < 1$.

> **Ukonverjensia/utofautikaji wa mfululizo wa kijiometri**  
> Mfululizo wa kijiometri $\sum ar^{n-1}$:
> - ukiwa na $\|r\| < 1$ unakonverjia
> - ukiwa na $\|r\| \geq 1$ unatofautika
{: .prompt-info }

Kutokana na hili tunapata

$$ 1 + r + r^2 + r^3 + \cdots = \frac{1}{1-r} \qquad (|r| < 1) \label{eqn:sum_of_inf_geometric_series}\tag{7}$$

### Mfululizo wa kijiometri na thamani za kukadiria
Utambulisho ($\ref{eqn:sum_of_geometric_series}$) ni muhimu katika kupata thamani ya kukadiria ya $\cfrac{1}{1-r}$ wakati $\|r\| < 1$.

Tukiweka $r=-\epsilon$, $n=2$ katika fomula hii, tunapata

$$ \frac{1}{1+\epsilon} - (1 - \epsilon) = \frac{\epsilon^2}{1 + \epsilon} $$

Kwa hiyo, ikiwa $0 < \epsilon < 1$,

$$ 0 < \frac{1}{1 + \epsilon} - (1 - \epsilon) < \epsilon^2 $$

na hivyo tunapata

$$ \frac{1}{1 + \epsilon} \approx (1 - \epsilon) \pm \epsilon^2 \qquad (0 < \epsilon < 1) $$

Kutokana na hili, tunaona kuwa kwa $\epsilon$ ndogo ya kutosha iliyo chanya, $\cfrac{1}{1 + \epsilon}$ inaweza kukadiriwa kwa $1 - \epsilon$.

## Kigezo cha $p$-msururu ($p$-Series Test)  
Kwa namba halisi chanya $p$, msururu wa umbo lifuatalo huitwa **$p$-msururu**.

$$ \sum_{n=1}^{\infty} \frac{1}{n^p} $$

> **Ukonverjensia/utofautikaji wa $p$-msururu**  
> $p$-msururu $\sum \cfrac{1}{n^p}$:
> - ikiwa $p>1$ unakonverjia
> - ikiwa $p\leq 1$ unatofautika
{: .prompt-info }

Katika $p$-msururu, hali ya $p=1$ ndiyo msururu wa harmoniki, na tayari tumeona kuwa unatofautika.  
Kwa $p=2$, tatizo la kupata thamani ya $p$-msururu $\sum \cfrac{1}{n^2}$ liliitwa “tatizo la Basel” kwa jina la eneo la familia ya Bernoulli, ambayo pia ni familia iliyotoa wanahisabati kadhaa mashuhuri kwa vizazi vingi na ambayo ilionyesha kwanza kuwa msururu huu unakonverjia. Inajulikana kuwa jibu la tatizo hili ni $\cfrac{\pi^2}{6}$.

Kwa upana zaidi, hali ya $p>1$ katika $p$-msururu huitwa **funksi ya zeta (zeta function)**. Hii ni mojawapo ya funksi maalumu iliyoletwa na Leonhard Euler katika mwaka 11740 wa [Kalenda ya Holocene](https://en.wikipedia.org/wiki/Holocene_calendar), na baadaye ikapewa jina na Riemann, nayo hufafanuliwa kwa

$$ \zeta(s) := \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s>1) $$

Kwa kuwa hili linatoka kidogo nje ya mada ya makala hii na, kusema kweli, mimi ni mwanafunzi wa uhandisi wala si mtaalamu wa hisabati, sitaingia zaidi hapa. Hata hivyo, Leonhard Euler alionyesha kuwa funksi ya zeta inaweza pia kuandikwa kama bidhaa isiyo na mwisho ya namba za kwanza, iitwayo **Euler Product**, na tangu hapo funksi ya zeta imekuwa na nafasi ya msingi katika maeneo mbalimbali ndani ya nadharia ya namba ya kianalisi. Miongoni mwa hayo ni **funksi ya zeta ya Riemann (Riemann zeta function)**, ambayo hupanua eneo la ufafanuzi la funksi ya zeta hadi namba changamano, pamoja na tatizo muhimu lisilotatuliwa linaloitwa **dhana ya Riemann (Riemann hypothesis)**.

Tukirudi kwenye mada ya awali, ili kuthibitisha kigezo cha $p$-msururu tunahitaji [kigezo cha ulinganishi](#kigezo-cha-ulinganishi) na [kigezo cha jumuisho](#kigezo-cha-jumuisho) ambavyo vitaelezwa baadaye. Hata hivyo, kwa kuwa ukonverjensia/utofautikaji wa $p$-msururu unaweza kutumika kwa manufaa katika [kigezo cha ulinganishi](#kigezo-cha-ulinganishi) kitakachofuata mara moja baada ya mfululizo wa kijiometri, nimekiweka kimakusudi mapema.

### Uthibitisho
#### i) Wakati $p>1$
Kwa kuwa jumuisho

$$ \int_1^\infty \frac{1}{x^p}\ dx = \left[\frac{1}{-p+1}\frac{1}{x^{p-1}} \right]^\infty_1 = \frac{1}{p-1} $$

linakonverjia, basi kwa [kigezo cha jumuisho](#kigezo-cha-jumuisho) tunajua kuwa msururu $\sum \cfrac{1}{n^p}$ pia unakonverjia.

#### ii) Wakati $p\leq 1$
Katika hali hii,

$$ 0 \leq \frac{1}{n} \leq \frac{1}{n^p} $$

Hapa tunajua kuwa msururu wa harmoniki $\sum \cfrac{1}{n}$ unatofautika, kwa hiyo kwa [kigezo cha ulinganishi](#kigezo-cha-ulinganishi) tunajua kuwa $\sum \cfrac{1}{n^p}$ pia unatofautika.

#### Hitimisho
Kutokana na i), ii), $p$-msururu $\sum \cfrac{1}{n^p}$ unakonverjia ikiwa $p>1$, na unatofautika ikiwa $p \leq 1$. $\blacksquare$

## Kigezo cha ulinganishi
Wakati wa kukagua ukonverjensia/utofautikaji wa **msururu wa viungo chanya (series of positive terms)**, yaani msururu wenye maneno ya jumla yaliyo namba halisi zisizo chini ya $0$, ni muhimu kutumia **kigezo cha ulinganishi (Comparison Test)** cha Jakob Bernoulli.

Kwa kuwa msururu wa viungo chanya ni mfuatano unaoongezeka, basi isipokuwa tu katika hali ya kutofautika kuelekea $\infty$ ($\sum a_n = \infty$), lazima ukonverjie. Kwa hiyo, katika msururu wa viungo chanya, andiko kama

$$ \sum a_n < \infty $$

linamaanisha <u>unakonverjia</u>.

> **Kigezo cha ulinganishi (Comparison Test)**  
> Wakati $0 \leq a_n \leq b_n$,  
> - $\sum b_n < \infty \ \Rightarrow \ \sum a_n < \infty$
> - $\sum a_n = \infty \ \Rightarrow \ \sum b_n = \infty$
{: .prompt-info }

Hususan, miongoni mwa misururu ya viungo chanya kama vile $\sum \cfrac{1}{n^2 + n}$, $\sum \cfrac{\log n}{n^3}$, $\sum \cfrac{1}{2^n + 3^n}$, $\sum \cfrac{1}{\sqrt{n}}$, $\sum \sin{\cfrac{1}{n}}$, n.k., pale tunapotaka kukagua ukonverjensia/utofautikaji wa misururu yenye umbo linalofanana na mfululizo wa kijiometri $\sum ar^{n-1}$ au $p$-msururu $\sum \cfrac{1}{n^p}$ tuliyoona mapema, ni vizuri kujaribu kwa bidii kigezo cha ulinganishi.

Vigezo vingine vingi vya ukonverjensia/utofautikaji vitakavyoelezwa baadaye vinaweza vyote kutolewa kutoka kwenye **kigezo hiki cha ulinganishi**, na kwa maana hiyo tunaweza kusema ndicho kilicho muhimu zaidi.

### Kigezo cha ulinganishi wa kikomo
Kwa misururu ya viungo chanya $\sum a_n$ na $\sum b_n$, tuseme katika uwiano wa maneno ya jumla $a_n/b_n$, viungo tawala vya juu katika hesabu na mahisabu vinafutana na kupata $\lim_{n\to\infty} \cfrac{a_n}{b_n}=c \text{ (}c\text{ ni namba chanya yenye kikomo)}$. Katika hali hii, ikiwa tunajua tayari ukonverjensia/utofautikaji wa msururu $\sum b_n$, tunaweza kutumia **kigezo cha ulinganishi wa kikomo (Limit Comparison Test)** kifuatacho.

> **Kigezo cha ulinganishi wa kikomo (Limit Comparison Test)**  
> Ikiwa
>
> $$ \lim_{n\to\infty} \frac{a_n}{b_n} = c \text{ (}c\text{ ni namba chanya yenye kikomo)}$$
>
> basi misururu $\sum a_n$ na $\sum b_n$ aidha yote miwili inakonverjia au yote miwili inatofautika. Yaani, $ \sum a_n < \infty \ \Leftrightarrow \ \sum b_n < \infty$.
{: .prompt-info }

## Kigezo cha mzizi
> **Nadharia**  
> Kwa msururu wa viungo chanya $\sum a_n$ na namba chanya $\epsilon < 1$,  
> - ikiwa kwa kila $n$, $\sqrt[n]{a_n}< 1-\epsilon$, basi msururu $\sum a_n$ unakonverjia
> - ikiwa kwa kila $n$, $\sqrt[n]{a_n}> 1+\epsilon$, basi msururu $\sum a_n$ unatofautika
{: .prompt-info }

> **Nadharia tokezi: Kigezo cha mzizi (Root Test)**  
> Katika msururu wa viungo chanya $\sum a_n$, tuseme kikomo
>
> $$ \lim_{n\to\infty} \sqrt[n]{a_n} =: r $$
>
> kipo. Hapo
> - ikiwa $r<1$, msururu $\sum a_n$ unakonverjia
> - ikiwa $r>1$, msururu $\sum a_n$ unatofautika
{: .prompt-info }

> Katika nadharia tokezi hapo juu, ikiwa $r=1$, hatuwezi kukagua ukonverjensia/utofautikaji, hivyo ni lazima kutumia mbinu nyingine.
{: .prompt-warning }

## Kigezo cha uwiano
> **Kigezo cha uwiano (Ratio Test)**  
> Kwa mfuatano chanya $(a_n)$ na $0 < r < 1$
> - ikiwa kwa kila $n$, $a_{n+1}/a_n \leq r$, basi msururu $\sum a_n$ unakonverjia
> - ikiwa kwa kila $n$, $a_{n+1}/a_n \geq 1$, basi msururu $\sum a_n$ unatofautika
{: .prompt-info }

> **Nadharia tokezi**  
> Katika mfuatano chanya $(a_n)$, tuseme kikomo $\rho := \lim_{n\to\infty} \cfrac{a_{n+1}}{a_n}$ kipo. Hapo
> - ikiwa $\rho < 1$, basi msururu $\sum a_n$ unakonverjia
> - ikiwa $\rho > 1$, basi msururu $\sum a_n$ unatofautika
{: .prompt-info }

## Kigezo cha jumuisho
Kwa kutumia mbinu ya jumuisho, tunaweza kukagua ukonverjensia/utofautikaji wa msururu ulioundwa na mfuatano chanya unaopungua.

> **Kigezo cha jumuisho (Integral Test)**  
> Ikiwa funksi endelevu $f: \left[1,\infty \right) \rightarrow \mathbb{R}$ inapungua na daima $f(x)>0$, basi sharti la lazima na la kutosha kwa msururu $\sum f(n)$ kukonverjia ni kwamba jumuisho
>
> $$ \int_1^\infty f(x)\ dx := \lim_{b\to\infty} \int_1^b f(x)\ dx $$
>
> likonverjie.
{: .prompt-info }

### Uthibitisho
Kwa kuwa funksi $f(x)$ ni endelevu, inapungua, na daima ni chanya, basi ukosefu wa usawa

$$ f(n+1) \leq \int_n^{n+1} f(x)\ dx \leq f(n) $$

unatimia. Tukijumlisha ukosefu huu wa usawa kutoka $n=1$ hadi neno la jumla, tunapata

$$ f(2) + \cdots + f(n+1) \leq \int_1^{n+1} f(x)\ dx \leq f(1) + \cdots + f(n) $$

Sasa tukitumia [kigezo cha ulinganishi](#kigezo-cha-ulinganishi), tunapata matokeo tuliyokusudia. $\blacksquare$

## Misururu mbadala
Msururu $\sum a_n$ ambao neno lake la jumla si $0$ na ambapo alama ya kila neno $a_n$ ni tofauti na alama ya neno linalofuata $a_{n+1}$, yaani viungo chanya na hasi vinajitokeza kwa kupokezana, huitwa **msururu mbadala (alternating series)**.

Kwa misururu mbadala, nadharia ifuatayo iliyogunduliwa na mwanahisabati Mjerumani Gottfried Wilhelm Leibniz inaweza kutumika kwa manufaa kukagua ukonverjensia/utofautikaji.

> **Kigezo cha msururu mbadala (Alternating Series Test)**  
> 1. Kwa kila $n$, $a_n$ na $a_{n+1}$ zina alama tofauti,
> 2. Kwa kila $n$, $\|a_n\| \geq \|a_{n+1}\|$, na
> 3. $\lim_{n\to\infty} a_n = 0$,
>
> basi msururu mbadala $\sum a_n$ unakonverjia.
{: .prompt-info }

## Misururu inayokonverjia kiabsolute
Kwa msururu $\sum a_n$, ikiwa msururu $\sum \|a_n\|$ unakonverjia, basi tunasema kwamba “msururu $\sum a_n$ **unakonverjia kiabsolute** (**converge absolutely**)”.

Katika hali hii, nadharia ifuatayo inatimia.

> **Nadharia**  
> Msururu unaokonverjia kiabsolute unakonverjia.
{: .prompt-info }

> Kinyume cha nadharia hapo juu si kweli.  
> Ikiwa msururu unakonverjia lakini haukonverjii kiabsolute, tunasema kuwa "**unakonverjia kimasharti** (**converge conditionally**)".
{: .prompt-warning }

### Uthibitisho
Kwa namba halisi $a$, tukifafanua

$$ \begin{align*}
a^+ &:= \max\{a,0\} = \frac{1}{2}(|a| + a), \\
a^- &:= -\min\{a,0\} = \frac{1}{2}(|a| - a)
\end{align*} $$

basi tunapata

$$ a = a^+ - a^-, \qquad |a| = a^+ + a^- $$

Kwa hiyo $0 \leq a^\pm \leq \|a\|$, na hivyo kwa [kigezo cha ulinganishi](#kigezo-cha-ulinganishi), ikiwa msururu $\sum \|a_n\|$ unakonverjia, basi misururu $\sum a_n^+$ na $\sum a_n^-$ pia yote miwili inakonverjia; kwa hiyo, kwa [sifa za msingi za misururu inayokonverjia](/posts/sequences-and-series/#sifa-za-msingi-za-misururu-inayokonverjia),

$$ \sum a_n = \sum (a_n^+ - a_n^-) = \sum a_n^+ - \sum a_n^- $$

pia unakonverjia. $\blacksquare$
