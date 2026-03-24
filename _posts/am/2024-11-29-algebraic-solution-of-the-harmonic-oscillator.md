---
title: የሃርሞኒክ ኦሲሌተር(The Harmonic Oscillator) አልጀብራዊ መፍትሔ
description: በኳንተም መካኒክስ ውስጥ ለሃርሞኒክ ኦሲሌተር የሽሮዲንገር ስሌትን እንመሰርታለን፣ ከዚያም አልጀብራዊ የመፍትሔ ዘዴውን እንመለከታለን። ከኮሚውቴተር(commutator)፣ ካኖኒካል ኮሚውቴሽን ግንኙነት እና ከላደር ኦፕሬተሮች በመነሳት የቋሚ ሁኔታ የሞገድ ፋንክሽንና የኃይል ደረጃዎችን እናገኛለን።
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - አምፕሊቱዱ(amplitude) በበቂ ሁኔታ ትንሽ ከሆነ፣ ማንኛውም ንዝረት እንደ ቀላል ሃርሞኒክ ንዝረት(simple harmonic oscillation) ሊጠጋገም ይችላል፤ ስለዚህም ቀላል ሃርሞኒክ ንዝረት በፊዚክስ ውስጥ አስፈላጊ ትርጉም አለው
> - ሃርሞኒክ ኦሲሌተር: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **ኮሚውቴተር(commutator)**:
>   - ሁለት ኦፕሬተሮች ምን ያህል በቀያይሮ(commute) እንደማይሰሩ የሚያመለክት ሁለት-ግቤት ኦፕሬሽን
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **ካኖኒካል ኮሚውቴሽን ግንኙነት(canonical commutation relation)**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **ላደር ኦፕሬተሮች(ladder operators)**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ን **ከፍ የሚያደርግ ኦፕሬተር(raising operator)**፣ $\hat{a}\_-$ን **ዝቅ የሚያደርግ ኦፕሬተር(lowering operator)** ብለን እንጠራዋለን
>   - ለማንኛውም ቋሚ ሁኔታ የኃይል ደረጃውን ማሳደግ ወይም ማሳነስ ስለሚቻል፣ ከጊዜ ጋር የማይዛመድ የሽሮዲንገር ስሌት አንድ መፍትሔ ብቻ ካገኘን ሌሎቹንም ሁሉ ማግኘት እንችላለን
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - የ$n$ኛው ቋሚ ሁኔታ የሞገድ ፋንክሽን እና የኃይል ደረጃ:
>   - የመሬት ሁኔታ($0$ኛው ቋሚ ሁኔታ):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - $n$ኛው ቋሚ ሁኔታ:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ የ $\hat{a}\_\pm$ **ኤርሚቲያን ኮንጁጌት(hermitian conjugate)** እና **አድጆይንት ኦፕሬተር(adjoint operator)** ነው
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - ከዚህ የሚከተሉትን ባህሪያት ማውጣት ይቻላል:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - $\hat{x}$ እና $\hat{p}$ የሚያካትቱ የኃይላቸው ቁጥሮች ያሉበትን የአካላዊ መጠኖች ጠበቃ ዋጋ(expectation value) የማስላት ዘዴ:
>   1. የላደር ኦፕሬተሮችን ትርጉም በመጠቀም $\hat{x}$ እና $\hat{p}$ን በከፍ የሚያደርግ እና በዝቅ የሚያደርግ ኦፕሬተሮች መግለጽ
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. ጠበቃ ዋጋውን ማግኘት የምንፈልገውን አካላዊ መጠን ከላይ ባሉት $\hat{x}$ እና $\hat{p}$ መግለጫዎች በመጠቀም መፃፍ
>   3. $\left(\hat{a}\_\pm \right)^m$ ከ $\psi\_{n\pm m}$ ጋር ተመጣጣኝ ስለሆነ ከ $\psi_n$ ጋር ኦርቶጎናል ሆኖ $0$ እንደሚሆን መጠቀም
>   4. የላደር ኦፕሬተሮችን ባህሪ በመጠቀም ኢንቴግራሉን ማስላት
{: .prompt-info }

## ቅድመ እውቀቶች
- [የተለዋዋጮች መለያየት ዘዴ](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [የሽሮዲንገር(Schrödinger) ስሌት እና የሞገድ ፋንክሽን](/posts/schrodinger-equation-and-the-wave-function/)
- [የኤረንፌስት(Ehrenfest) ቲዮረም](/posts/ehrenfest-theorem/)
- [ከጊዜ ጋር የማይዛመድ የሽሮዲንገር(Schrödinger) ስሌት](/posts/time-independent-schrodinger-equation/)
- [1-ልኬት ያለ ወሰን ካሬ ጉድጓድ(The 1D Infinite Square Well)](/posts/the-infinite-square-well/)
- ኤርሚቲያን ኮንጁጌት(hermitian conjugate), አድጆይንት ኦፕሬተር(adjoint operator)

## የሞዴሉ ቅንብር
### በክላሲካል መካኒክስ ውስጥ ያለ ሃርሞኒክ ኦሲሌተር
ክላሲካል ሃርሞኒክ ኦሲሌተር የሚወክለው ተወላጅ ምሳሌ የጅምላው $m$ እና የስፕሪንግ ቋሚው $k$ በሆነ ስፕሪንግ ላይ የተንጠለጠለ እቃ እንቅስቃሴ ነው(ግጭት እንደሌለ እንቆጥራለን)።
ይህ እንቅስቃሴ **የሁክ(Hooke) ሕግ(Hooke's law)**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

ይከተላል። የዚህ ስሌት መፍትሔ

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

ነው፣ እና እዚህ

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

የንዝረቱ አንግላር ፍሪክዌንሲ(angular frequency) ነው። ከቦታ $x$ ጋር የተያያዘ ፖቴንሺያል ኃይል(potential energy)

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

የፓራቦላ ቅርጽ አለው።

በእውነተኛ ዓለም ፍጹም ሃርሞኒክ ኦሲሌተር የለም። አሁን በምሳሌ የወሰድነውን ስፕሪንግ ብቻ ብንመለከት፣ በጣም ከፍ አድርገን ካጠነከርነው የኤላስቲክነት ገደቡን አልፎ ሊቆረጥ ወይም የቋሚ ቅርጽ ለውጥ ሊፈጠርበት ይችላል፤ እንዲያውም ወደዚያ ከመድረሳችን በፊት እንኳን የሁክን ሕግ በትክክል መከተሉን ያቆማል። ነገር ግን ሃርሞኒክ ኦሲሌተር በፊዚክስ ውስጥ አስፈላጊ የሆነው ምክንያት ማንኛውም ፖቴንሺያል በአካባቢያዊ ዝቅተኛ(local minimum) አካባቢ በፓራቦላ ሊጠጋገም ስለሚችል ነው። የትኛውንም ፖቴንሺያል $V(x)$ በዝቅተኛ ነጥብ አቅራቢያ በቴይለር ተከታታይ(Taylor expansion) ብንስፋፋው

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

እናገኛለን። አሁን $V(x)$ ላይ ማንኛውንም ቋሚ ቁጥር መጨመር በኃይል ላይ ምንም ተጽእኖ ስለማይኖረው፣ እዚህ $V(x_0)$ን እንቀንሳለን፤ እንዲሁም $x_0$ ዝቅተኛ ነጥብ ስለሆነ $V^\prime(x_0)=0$ መሆኑን እንጠቀማለን፤ በተጨማሪም $(x-x_0)$ በበቂ ሁኔታ ትንሽ ነው ብለን በማሰብ ከፍተኛ ደረጃ ቃላትን ብንተው

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

እናገኛለን\*። ይህ በ $x_0$ አቅራቢያ ውጤታማ የስፕሪንግ ቋሚ $k=V^{\prime\prime}(x_0)$ ያለው ሃርሞኒክ ኦሲሌተር እንቅስቃሴ ጋር ይጣጣማል። ማለትም፣ አምፕሊቱዱ(amplitude) በበቂ ሁኔታ ትንሽ ከሆነ ማንኛውም ንዝረት እንደ ቀላል ሃርሞኒክ ንዝረት(simple harmonic oscillation) ሊጠጋገም ይችላል።

> \* $V(x)$ በ $x_0$ ላይ አካባቢያዊ ዝቅተኛ እንዳለው አስበናል፤ ስለዚህ $V^{\prime\prime}(x_0) \geq 0$ ነው። እጅግ አልፎ አልፎ $V^{\prime\prime}(x_0)=0$ የሚሆን ሁኔታ አለ፣ እነዚህም እንቅስቃሴዎች እንደ ቀላል ሃርሞኒክ ንዝረት ሊጠጋገሙ አይችሉም።
{: .prompt-info }

### በኳንተም መካኒክስ ውስጥ ያለ ሃርሞኒክ ኦሲሌተር
በኳንተም መካኒክስ ያለው የሃርሞኒክ ኦሲሌተር ችግኝ ፖቴንሺያሉ

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

የሆነበትን የሽሮዲንገር ስሌት መፍታት ነው። ለሃርሞኒክ ኦሲሌተር [ከጊዜ ጋር የማይዛመድ የሽሮዲንገር ስሌት](/posts/time-independent-schrodinger-equation/) የሚከተለው ነው።

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

ይህን ችግኝ ለመፍታት ፍጹም የተለያዩ ሁለት አቀራረቦች አሉ። አንዱ **የኃይል ተከታታይ ዘዴ(power series method)** የሚጠቀም ትንታኔያዊ ዘዴ(analytic method) ሲሆን፣ ሌላው ደግሞ **ላደር ኦፕሬተሮች(ladder operators)**ን የሚጠቀም አልጀብራዊ ዘዴ(algebraic method) ነው። አልጀብራዊ ዘዴው ፈጣንና ቀላል ቢሆንም፣ የኃይል ተከታታይ በመጠቀም የሚሰጠውን ትንታኔያዊ መፍትሔም ማጥናት ያስፈልጋል። እዚህ አልጀብራዊውን የመፍትሔ ዘዴ እንመለከታለን፤ ትንታኔያዊውን ዘዴ ግን [በዚህ ጽሑፍ](/posts/analytic-solution-of-the-harmonic-oscillator/) ማየት ይችላሉ።

## ኮሚውቴተር እና ካኖኒካል ኮሚውቴሽን ግንኙነት
ስሌት ($\ref{eqn:t_independent_schrodinger_eqn}$) የግፊት ኦፕሬተር $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$ን በመጠቀም እንዲህ ሊጻፍ ይችላል።

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

አሁን ሃሚልቶኒያኑን(Hamiltonian)

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

እንፋክተር እናድርግ።

$ p $ እና $ x $ ቁጥሮች(numbers) ቢሆኑ ኖሮ

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

በሚል መልኩ ቀላል ፋክተር ማድረግ እንችል ነበር፤ ነገር ግን እዚህ $\hat{p}$ እና $\hat{x}$ ኦፕሬተሮች ናቸው፣ እና ለኦፕሬተሮች በአጠቃላይ **የመቀያየር ባህሪ(commutative property)** አይሠራም($\hat{p}\hat{x}\neq \hat{x}\hat{p}$)፣ ስለዚህ ነገሩ እንዲያው ቀላል አይደለም። ሆኖም ግን ይህ አንድ መመሪያ ነጥብ ሊሆን ይችላል፣ ስለዚህ ከመጀመሪያ የሚከተለውን መጠን እንመልከት።

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

ከላይ ለተገለጹት $\hat{a_\pm}$ ኦፕሬተሮች፣ $\hat{a}\_-\hat{a}\_+$ የሚከተለው ነው።

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

ነው። እዚህ $(\hat{x}\hat{p}-\hat{p}\hat{x})$ ቃልን የ $\hat{x}$ እና $\hat{p}$ **ኮሚውቴተር(commutator)** ብለን እንጠራዋለን፤ ይህም ሁለት ኦፕሬተሮች ምን ያህል በቀያይሮ(commute) እንደማይሰሩ ያሳያል። በአጠቃላይ የ $\hat{A}$ እና $\hat{B}$ ኦፕሬተሮች ኮሚውቴተር በካሬ ቅንፎች እንዲህ ይገለጻል።

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

ይህን ምልክት በመጠቀም ስሌት ($\ref{eqn:a_m_times_a_p_without_commutator}$) እንዲህ ብለን እንደገና ልንጽፈው እንችላለን።

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

አሁን $\hat{x}$ እና $\hat{p}$ ያላቸውን ኮሚውቴተር ማወቅ ያስፈልጋል።

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

ሲሆን፣ የሙከራ ፋንክሽን(test function) $f(x)$ን ካስወገድን በኋላ የሚከተለውን እናገኛለን።

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

ይህንን **ካኖኒካል ኮሚውቴሽን ግንኙነት(canonical commutation relation)** ብለን እንጠራዋለን።

## ላደር ኦፕሬተሮች (ladder operators)
በካኖኒካል ኮሚውቴሽን ግንኙነት ምክንያት ስሌት ($\ref{eqn:a_m_times_a_p}$) እንዲህ ይሆናል።

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

ማለትም

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

ነው። እዚህ $\hat{a}\_-$ እና $\hat{a}\_+$ ያላቸው ቅደም ተከተል አስፈላጊ ነው፤ $\hat{a}\_+$ን በግራ ብናስቀምጠው

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

ይሆናል፣ እና

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

ያሟላል። በዚህ ሁኔታ ሃሚልቶኒያኑ

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

ብለንም ልንጽፈው እንችላለን። ስለዚህ ከጊዜ ጋር የማይዛመደውን የሽሮዲንገር ስሌት($\hat{H}\psi=E\psi$) በ $\hat{a}_\pm$ ብንገልጸው

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

ይሆናል(የ± ምልክቶቹ በተዛማጅ ሁኔታ ይመረጣሉ)።

አሁን የሚከተለውን አስፈላጊ ባህሪ ማውጣት እንችላለን።

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> ማረጋገጫ:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> በተመሳሳይ፣
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

ስለዚህ፣ ከጊዜ ጋር የማይዛመድ የሽሮዲንገር ስሌት አንድ መፍትሔ ብቻ ካገኘን ሌሎቹን ሁሉ ማግኘት እንችላለን። ለማንኛውም ቋሚ ሁኔታ የኃይል ደረጃውን ማሳደግ ወይም ማሳነስ ስለሚቻል $\hat{a}\_\pm$ን **ላደር ኦፕሬተሮች(ladder operators)** ብለን እንጠራቸዋለን፤ $\hat{a}\_+$ ደግሞ **ከፍ የሚያደርግ ኦፕሬተር(raising operator)** ሲሆን $\hat{a}\_-$ ደግሞ **ዝቅ የሚያደርግ ኦፕሬተር(lowering operator)** ነው።

## የሃርሞኒክ ኦሲሌተር ቋሚ ሁኔታዎች
### ቋሚ ሁኔታ $\psi_n$ እና የኃይል ደረጃ $E_n$
ዝቅ የሚያደርገውን ኦፕሬተር በተከታታይ ብንተገብር አንድ ጊዜ ከ $0$ በታች ያለ የኃይል ሁኔታ እናገኛለን፤ እንዲህ ያሉ ሁኔታዎች ግን በአካላዊ ዓለም ሊኖሩ አይችሉም። በሂሳብ ቋንቋ ለመናገር፣ $\psi$ የሽሮዲንገር ስሌት መፍትሔ ከሆነ $\hat{a}_-\psi$ ደግሞ የሽሮዲንገር ስሌት መፍትሔ ነው፤ ነገር ግን ይህ አዲስ መፍትሔ ሁልጊዜ ኖርማላይዝ(normalized) ይሆናል ብለን መደምደም አንችልም(ማለትም በአካላዊ ሁኔታ የሚቻል ሁኔታ መሆኑ አይረጋገጥም)። ዝቅ የሚያደርገውን ኦፕሬተር በተከታታይ ብንጠቀም በመጨረሻ ትሪቪያል መፍትሔ $\psi=0$ እናገኛለን።

ስለዚህ ለሃርሞኒክ ኦሲሌተር ቋሚ ሁኔታ $\psi$፣

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

የሚያሟላ(ከዚያ በታች ያለ የኃይል ደረጃ የሌለው) “ዝቅተኛው ደረጃ” $\psi_0$ መኖሩ ይኖርበታል። ይህ $\psi_0$

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

ያሟላል፣ ስለዚህ

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

ነው። ይህ [መለያየት የሚችል ተራ ዲፈረንሻል ስሌት](/posts/Separation-of-Variables/) ስለሆነ ቀላል በሆነ መንገድ እንዲህ ማፍታት ይቻላል።

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

በተጨማሪም ይህን ፋንክሽን እንዲህ ብለን ኖርማላይዝ(normalize) ማድረግ እንችላለን።

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

እዚህ $A^2 = \sqrt{m\omega / \pi\hbar}$ ስለሆነ

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

ነው። አሁን ይህን መፍትሔ ከዚህ በፊት ያገኘነው የሽሮዲንገር ስሌት ($\ref{eqn:schrodinger_eqn_with_ladder}$) ውስጥ በመተካት እና $\hat{a}_-\psi_0$ መሆኑን በመጠቀም የሚከተለውን እናገኛለን።

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

ከዚህ **የመሬት ሁኔታ(ground state)** ጀምሮ ከፍ የሚያደርገውን ኦፕሬተር በተከታታይ ብንተገብር፣ ከፍ የሚያደርገው ኦፕሬተር አንድ ጊዜ በሚሰራ ቁጥር ኃይሉ $\hbar\omega$ በሚጨምር መልኩ የሚገኙ እንቅስቃሴ ሁኔታዎችን **የተነሱ ሁኔታዎች(excited states)** ማግኘት እንችላለን።

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

እዚህ $A_n$ የኖርማላይዜሽን ቋሚ ነው። እንዲህ ሆኖ የመሬት ሁኔታን ካገኘን በኋላ ከፍ የሚያደርገውን ኦፕሬተር በመተግበር የሃርሞኒክ ኦሲሌተር ሁሉንም ቋሚ ሁኔታዎችና የሚፈቀዱ የኃይል ደረጃዎች መወሰን እንችላለን።

### ኖርማላይዜሽን
የኖርማላይዜሽን ቋሚውንም በአልጀብራዊ መንገድ ማግኘት ይቻላል። እኛ $\hat{a}\_{\pm}\psi_n$ ከ $\psi\_{n\pm 1}$ ጋር ተመጣጣኝ መሆኑን እናውቃለን፣ ስለዚህ

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

ብለን ልንጽፈው እንችላለን። 

አሁን ለማንኛውም ኢንቴግራብል ፋንክሽኖች $f(x)$ እና $g(x)$ የሚከተለው እንደሚሠራ እንገንዘብ።

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ የ $\hat{a}\_\pm$ **ኤርሚቲያን ኮንጁጌት(hermitian conjugate)** እና **አድጆይንት ኦፕሬተር(adjoint operator)** ነው።

> **ማረጋገጫ:**
>
> $$ \begin{align*}
> \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g) dx &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} f^*\left(\mp \hbar\frac{d}{dx}+m\omega x \right)g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\int_{-\infty}^{\infty} \left(\mp\hbar  f^* \frac{d}{dx}g + m\omega x f^*g\right)dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left(\mp\hbar\int_{-\infty}^{\infty} f^*\frac{dg}{dx}\ dx + \int_{-\infty}^{\infty}m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left[\mp\hbar\left(f^*g\bigg|^{\infty}_{-\infty} -\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx \right) + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right] \\
> &= \frac{1}{\sqrt{2\hbar m\omega}}\left( \pm\hbar\int_{-\infty}^{\infty} \frac{df^*}{dx}g\ dx + \int_{-\infty}^{\infty} m\omega x f^*g\ dx \right) \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f^* \right] g\ dx \\
> &= \frac{1}{\sqrt{2\hbar m\omega}} \int_{-\infty}^{\infty} \left[\left(\pm\hbar\frac{d}{dx} + m\omega x \right)f \right]^* g\ dx \\
> &= \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx.\ \blacksquare
> \end{align*} $$
>
{: .prompt-info }

ስለዚህ፣ $f=\hat{a}_\pm \psi_n$, $g=\psi_n$ ብለን ብናስቀምጥ

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

ይሆናል። እንግዲህ ከስሌቶች ($\ref{eqn:schrodinger_eqn_with_ladder}$) እና ($\ref{eqn:psi_n_and_E_n}$)

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

ስለሆነ፣ ከስሌቶች ($\ref{eqn:norm_const}$) እና ($\ref{eqn:norm_const_2}$) የሚከተለውን እናገኛለን።

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

እና እዚህ $\psi_n$ እና $\psi_{n\pm1}$ ሁለቱም ኖርማላይዝ ስለሆኑ $\|c_n\|^2=n+1,\ \|d_n\|^2=n$ ነው፣ ስለዚህ

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

ነው። ከዚህም ኖርማላይዝ የተደረገ ማንኛውም ቋሚ ሁኔታ $\psi_n$ እንዲህ ብለን ማግኘት እንችላለን።

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

ማለትም፣ በስሌት ($\ref{eqn:psi_n_and_E_n}$) ውስጥ የኖርማላይዜሽን ቋሚ $A_n=\cfrac{1}{\sqrt{n!}}$ ነው።

### የቋሚ ሁኔታዎች ኦርቶጎናልነት
[1-ልኬት ያለ ወሰን ካሬ ጉድጓድ(The 1D Infinite Square Well)](/posts/the-infinite-square-well/#3-ይህ-ሁኔታ-ኦርቶጎናልነትorthogonality-አለው) ውስጥ እንደነበረው በተመሳሳይ፣ የሃርሞኒክ ኦሲሌተር ቋሚ ሁኔታዎች እርስ በርሳቸው ኦርቶጎናል ናቸው።

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### ማረጋገጫ
ከዚህ በፊት ያሳየነውን ስሌቶች ($\ref{eqn:hermitian_conjugate}$)፣ ($\ref{eqn:norm_const_2}$) እና ($\ref{eqn:norm_const_3}$) በመጠቀም ማረጋገጥ ይቻላል። በስሌት ($\ref{eqn:hermitian_conjugate}$) ውስጥ $f=\hat{a}_-\psi_m,\ g=\psi_n$ ብለን ካስቀመጥን

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

መሆኑን እንጠቀማለን።

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

ኦርቶጎናልነትን በመጠቀም፣ [በ1-ልኬት ያለ ወሰን ካሬ ጉድጓድ ጽሑፍ ውስጥ በስሌት (19) እንደተደረገው](/posts/the-infinite-square-well/#ጊዜ-ላይ-የሚወሰን-የሽሮዲንገር-ስሌት-አጠቃላይ-መፍትሔ-psixt-ማግኘት) $\Psi(x,0)$ን እንደ ቋሚ ሁኔታዎች መስመራዊ ድምር $\sum c_n\psi_n(x)$ ስንዘርጋ፣ ኮፊሺየንቶቹን $c_n$ [በፉሪዬ(Fourier) ዘዴ](/posts/the-infinite-square-well/#በፉሪዬ-ዘዴfouriers-trick-የ-ኮፊሺየንት-c_n-ማግኘት) ማግኘት እንችላለን።

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

እዚህም እንደዚያው $\|c_n\|^2$ ኃይልን ሲለካ $E_n$ ዋጋን የማግኘት እድል ነው።

## በማንኛውም ቋሚ ሁኔታ $\psi_n$ ውስጥ ያለ የፖቴንሺያል ኃይል ጠበቃ ዋጋ $\langle V \rangle$
$\langle V \rangle$ን ለማግኘት የሚከተለውን ኢንቴግራል ማስላት አለብን።

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

$\hat{x}$ እና $\hat{p}$ የኃይል ቁጥሮች ያላቸውን ቅርጾች የሚያካትቱ እንደዚህ ያሉ ኢንቴግራሎችን ሲያስሉ የሚከተለው ዘዴ ጠቃሚ ነው።

መጀመሪያ ስሌት ($\ref{eqn:ladder_operators}$) ውስጥ ያለውን የላደር ኦፕሬተሮች ትርጉም በመጠቀም $\hat{x}$ እና $\hat{p}$ን በከፍ የሚያደርግ እና በዝቅ የሚያደርግ ኦፕሬተሮች መግለጽ እንችላለን።

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

አሁን ጠበቃ ዋጋውን ማግኘት የምንፈልገውን አካላዊ መጠን ከላይ ባሉት $\hat{x}$ እና $\hat{p}$ መግለጫዎች በመጠቀም እንጽፋለን። እዚህ $x^2$ ላይ ፍላጎት ስላለን፣

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

በሚል መልኩ መጻፍ እንችላለን። ከዚህም የሚከተለውን እናገኛለን።

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

እዚህ $\left(\hat{a}\_\pm \right)^2$ ከ $\psi\_{n\pm2}$ ጋር ተመጣጣኝ ስለሆነ ከ $\psi\_n$ ጋር ኦርቶጎናል ነው፣ ስለዚህ $\left(\hat{a}\_+ \right)^2$ እና $\left(\hat{a}\_- \right)^2$ የሆኑት ሁለቱ ቃላት $0$ ይሆናሉ። ከዚያም በመጨረሻ ስሌት ($\ref{eqn:norm_const_2}$) በመጠቀም የቀሩትን ሁለት ቃላት ካሰላን

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

እናገኛለን። ስሌት ($\ref{eqn:psi_n_and_E_n}$)ን ብንመለከት የፖቴንሺያል ኃይል ጠበቃ ዋጋ ከጠቅላላ ኃይል ትክክለኛ ግማሽ መሆኑን እናያለን፤ የቀረው ግማሽ ደግሞ በእርግጥ ኪኔቲክ ኃይል $T$ ነው። ይህ የሃርሞኒክ ኦሲሌተር ልዩ ባህሪ ነው።
