---
title: 1D ወሰን የሌለው ካሬ ጉድጓድ(The 1D Infinite Square Well)
description: የኳንተም መካኒክስ መሠረታዊ ሀሳቦችን በግልጽ የሚያሳይ ቀላል ነገር ግን አስፈላጊ የሆነውን የ1D ወሰን የሌለው ካሬ ጉድጓድ ችግኝ እንመለከታለን።
  በዚህ ሁኔታ nኛውን ቋሚ ሁኔታ ψ(x)፣ ኃይል E፣ የψ(x) 4 አስፈላጊ ሂሳባዊ ባህሪያትን እና ከዚህ የሚከተለውን አጠቃላይ Ψ(x,t) እናገኛለን።
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Hamiltonian]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## አጭር ማጠቃለያ
> - የ1D ወሰን የሌለው ካሬ ጉድጓድ ችግኝ: 
>   $$V(x) = \begin{cases}
>   0, & 0 \leq x \leq a,\\
>   \infty, & \text{ከዚህ ውጭ}
>   \end{cases}$$
> - የድንበር ሁኔታዎች: $ \psi(0) = \psi(a) = 0 $
> - የ$n$ኛው ቋሚ ሁኔታ የኃይል ደረጃ: $E_n = \cfrac{n^2\pi^2\hbar^2}{2ma^2}$
> - በጉድጓዱ ውስጥ የጊዜ-ነጻ የሽሮዲንገር ስሌት መፍትሔ:
>
>   $$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) $$
>
> - የእያንዳንዱ ቋሚ ሁኔታ $\psi_n$ ፊዚካዊ ትርጓሜ: 
>   - ርዝመቱ $a$ በሆነ ገመድ ላይ የሚታይ የቆመ ማዕበል ቅርጽ
>   - **የመሬት ሁኔታ(ground state)**: ከሁሉ ዝቅተኛ ኃይል ያለው ቋሚ ሁኔታ $\psi_1$
>   - **የተነሱ ሁኔታዎች(exited states)**: ኃይላቸው ከ$n^2$ ጋር በተመጣጣኝ የሚጨምር ሌሎች $n\geq 2$ ሁኔታዎች
> - የ$\psi_n$ 4 አስፈላጊ ሂሳባዊ ባህሪያት:
>   1. ፖቴንሻል $V(x)$ ሲመጣጠን በጉድጓዱ መሃል አንፃር ጥንድ ተግባርና ነጠላ ተግባር በተራ ይታያሉ
>   2. ኃይል እየጨመረ ሲሄድ እያንዳንዱ ተከታታይ ሁኔታ **ኖድ(node)** አንድ በአንድ ይጨምራል
>   3. **ኦርቶኖርማሊቲ(orthonomality)** አለው
>
>      $$ \begin{gather*}
>      \int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \\
>      \delta_{mn} = \begin{cases}
>      0, & m\neq n \\
>      1, & m=n
>      \end{cases} 
>      \end{gather*} $$
>
>   4. **ሙሉነት(completeness)** አለው
>
>      $$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) $$
>
> - የሽሮዲንገር ስሌት አጠቃላይ መፍትሔ(የቋሚ ሁኔታዎች መስመራዊ ጥምረት):
>
>   $$ \begin{gather*}
>   \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t}, \\
>   \text{በዚህ ጊዜ ግቤት }c_n = \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
>   \end{gather*}$$
{: .prompt-info }

## ቅድመ እውቀቶች
- ቀጣይ የእድል ስርጭት እና የእድል ጥግግት
- ኦርቶጎናሊቲ እና መደበኛ ማድረግ(መስመራዊ አልጀብራ)
- የፉሪየ(Fourier) ተከታታይ እና ሙሉነት(መስመራዊ አልጀብራ)
- [የሽሮዲንገር ስሌት እና የሞገድ ተግባር](/posts/schrodinger-equation-and-the-wave-function/)
- [የኤረንፌስት ቲዎረም](/posts/ehrenfest-theorem/)
- [የጊዜ-ነጻ የሽሮዲንገር ስሌት](/posts/time-independent-schrodinger-equation/)

## የተሰጠው የፖቴንሻል ሁኔታ
ፖቴንሻሉ

$$ V(x) = \begin{cases}
0, & 0 \leq x \leq a,\\
\infty, & \text{ከዚህ ውጭ}
\end{cases} \tag{1}$$

ከሆነ፣ በዚህ ፖቴንሻል ውስጥ ያለ ቅንጣት በክልሉ $0<x<a$ ውስጥ ነፃ ቅንጣት ሲሆን በሁለቱም ጫፎች($x=0$ እና $x=a$) ላይ ወሰን የሌለው ኃይል ስለሚሠራበት ማምለጥ አይችልም። በክላሲካል ሞዴል ይህ በፊትና በኋላ ፍጹም የኤላስቲክ ግጭት እየደገመ እና ያልተጠበቀ ኃይል ሳይሠራ የሚፈጠር ወሰን የሌለው የመመላለስ እንቅስቃሴ ተብሎ ይተረጎማል። ምንም እንኳን እንዲህ ያለ ፖቴንሻል እጅግ ሰው ሠራሽ እና ቀላል ቢሆንም፣ በኋላ ኳንተም መካኒክስን ሲማሩ ሌሎች ፊዚካዊ ሁኔታዎችን ለመመልከት ጠቃሚ የማጣቀሻ ምሳሌ ሊሆን ስለሚችል በጥንቃቄ ማየት ያስፈልጋል።

![ወሰን የሌለው ፖቴንሻል ጉድጓድ](https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Infinite_potential_well-en.svg/615px-Infinite_potential_well-en.svg.png)
> *የምስል ምንጭ*
> - ደራሲ: የዊኪሚዲያ ተጠቃሚ [Benjamin ESHAM](https://commons.wikimedia.org/wiki/User:Bdesham)
> - ፈቃድ: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

## ሞዴሉን እና የድንበር ሁኔታዎችን ማዘጋጀት
ከጉድጓዱ ውጭ ቅንጣቱን የማግኘት እድል $0$ ስለሆነ $\psi(x)=0$ ነው። በጉድጓዱ ውስጥ $V(x)=0$ ስለሆነ [የጊዜ-ነጻ የሽሮዲንገር ስሌት](/posts/time-independent-schrodinger-equation/) እንዲህ ይሆናል።

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{2}$$

ማለትም

$$ \frac{d^2\psi}{dx^2} = -k^2\psi,\text{ እዚህ } k\equiv \frac{\sqrt{2mE}}{\hbar} \tag{3}$$

በሚለው ቅርጽ ሊጻፍ ይችላል።

> እዚህ $E\geq 0$ ብለን እንገምታለን።
{: .prompt-info }

ይህ ክላሲካል **ቀላል ሐርሞኒክ ኦሲሌተር(simple harmonic oscillator)** የሚገልጽ ስሌት ሲሆን፣ አጠቃላይ መፍትሔው

$$ \psi(x) = A\sin{kx} + B\cos{kx} \label{eqn:psi_general_solution}\tag{4}$$

ነው። እዚህ $A$ እና $B$ የፈለጉ ቋሚዎች ሲሆኑ፣ ከችግኙ ሁኔታ ጋር የሚስማማ ልዩ መፍትሔ ሲፈለግ ብዙ ጊዜ እነዚህ ቋሚዎች በችግኙ የተሰጡ **የድንበር ሁኔታዎች** ይወሰናሉ። <u>በአብዛኛው $\psi(x)$ ለሚሆን ጉዳይ $\psi$ እና $d\psi/dx$ ሁለቱም ቀጣይ መሆናቸው የድንበር ሁኔታ ይሆናል፤ ነገር ግን ፖቴንሻሉ ወደ ወሰን የሌለው ሲሄድ $\psi$ ብቻ ቀጣይ ነው።</u>

## የጊዜ-ነጻ የሽሮዲንገር ስሌት መፍትሔን ማግኘት

$\psi(x)$ ቀጣይ ስለሆነ

$$ \psi(0) = \psi(a) = 0 \label{eqn:boundary_conditions}\tag{5}$$

መሆን አለበት፣ እናም ከጉድጓዱ ውጭ ካለው መፍትሔ ጋር መገናኘት አለበት። በስሌት ($\ref{eqn:psi_general_solution}$) ውስጥ $x=0$ ሲሆን

$$ \psi(0) = A\sin{0} + B\cos{0} = B $$

ስለሚሆን፣ ($\ref{eqn:boundary_conditions}$) ሲተካ $B=0$ መሆን አለበት።

$$ \therefore \psi(x)=A\sin{kx} \label{eqn:psi_without_B}. \tag{6}$$

ከዚያ $\psi(a)=A\sin{ka}$ ስለሆነ፣ በስሌት ($\ref{eqn:boundary_conditions}$) ውስጥ ያለውን $\psi(a)=0$ ለማሟላት $A=0$(ትሪቪያል መፍትሔ) ወይም $\sin{ka}=0$ መሆን አለበት። ስለዚህ

$$ ka = 0,\, \pm\pi,\, \pm 2\pi,\, \pm 3\pi,\, \dots \tag{7}$$

ነው። እዚህም እንደተመሳሰለው $k=0$ ትሪቪያል መፍትሔ ሲሆን $\psi(x)=0$ ይሆናል እና ስለዚህ መደበኛ ማድረግ አይቻልም፤ ስለዚህ በዚህ ችግኝ ውስጥ የምንፈልገው መፍትሔ አይደለም። እንዲሁም $\sin(-\theta)=-\sin(\theta)$ ስለሆነ የአሉታዊ ምልክቱ ተጽእኖ በስሌት ($\ref{eqn:psi_without_B}$) ውስጥ ባለው $A$ ውስጥ ሊውል ይችላል፤ ስለዚህ $ka>0$ የሆኑ ጉዳዮችን ብቻ መመልከት አጠቃላይነትን አያጣም። ስለዚህ $k$ ላይ የሚቻሉ መፍትሔዎች

$$ k_n = \frac{n\pi}{a},\ n\in\mathbb{N} \tag{8}$$

ናቸው።

ከዚያ $\psi_n=A\sin{k_n x}$ ሲሆን $\cfrac{d^2\psi}{dx^2}=-Ak^2\sin{kx}$ ስለሚሆን፣ ይህን በስሌት ($\ref{eqn:t_independent_schrodinger_eqn}$) ውስጥ በመተካት የሚቻሉ የ$E$ እሴቶች እንዲህ ይሆናሉ።

$$ A\frac{\hbar^2}{2m}k_n^2\sin{k_n x} = AE_n\sin{k_n x} $$

$$ E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}. \tag{9}$$

ከክላሲካል ጉዳይ ጋር በጣም የሚለይ በሆነ መንገድ፣ በወሰን የሌለው ካሬ ጉድጓድ ውስጥ ያለ የኳንተም ቅንጣት ማንኛውንም ኃይል ሊኖረው አይችልም፤ ከተፈቀዱት እሴቶች አንዱን ብቻ ሊይዝ ይችላል።

> በየጊዜ-ነጻ የሽሮዲንገር ስሌት መፍትሔ ላይ የሚተገቡ የድንበር ሁኔታዎች ምክንያት ኃይሉ ኳንታይዝ ይደረጋል።
{: .prompt-info }

አሁን $\psi$ ን መደበኛ በማድረግ $A$ ን ማግኘት እንችላለን።

> በመሠረቱ መደበኛ ማድረግ የሚገባው $\Psi(x,t)$ ነው፤ ነገር ግን [የጊዜ-ነጻ የሽሮዲንገር ስሌት](/posts/time-independent-schrodinger-equation/#1-ቋሚ-ሁኔታዎችstationary-states-ናቸው) ውስጥ ባለው ስሌት (11) መሠረት ይህ ከ$\psi(x)$ መደበኛ ማድረግ ጋር እኩል ነው።
{: .prompt-tip }

$$ \int_0^a |A|^2 \sin^2(kx)dx = |A|^2\frac{a}{2} = 1 $$

$$ \therefore |A|^2 = \frac{2}{a}. $$

ይህ በትክክል የሚወስነው የ$A$ መጠንን ብቻ ነው፤ ነገር ግን የ$A$ ፌዝ ምንም ፊዚካዊ ትርጉም ስለሌለው አዎንታዊውን እውነተኛ ስኩዌር ሩት በቀጥታ $A$ እንደሆነ መውሰድ ይቻላል። ስለዚህ በጉድጓዱ ውስጥ ያለው መፍትሔ

$$ \psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) \label{eqn:psi_n}\tag{10}$$

ነው።

## የእያንዳንዱ ቋሚ ሁኔታ $\psi_n$ ፊዚካዊ ትርጓሜ
በስሌት ($\ref{eqn:psi_n}$) እንደተገለጸው፣ ከየጊዜ-ነጻ የሽሮዲንገር ስሌት ለእያንዳንዱ የኃይል ደረጃ $n$ የሚዛመዱ ወሰን የሌላቸው መፍትሔዎችን አግኝተናል። ከእነዚህ መካከል የመጀመሪያዎቹን ጥቂቶች በስዕል ካሳየን ከታች እንደሚታየው ይሆናል።

![የዝቅተኛዎቹ አራት የኳንተም ሁኔታዎች የመጀመሪያ ሞገድ ተግባሮች](https://upload.wikimedia.org/wikipedia/commons/4/47/Particle_in_a_box_wavefunctions_2.svg)
> *የምስል ምንጭ*
> - ደራሲ: የዊኪሚዲያ ተጠቃሚ [Papa November](https://commons.wikimedia.org/wiki/User:Papa_November)
> - ፈቃድ: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)

እነዚህ ሁኔታዎች ርዝመቱ $a$ በሆነ ገመድ ላይ የሚታዩ የቆመ ማዕበል ቅርጾችን ይይዛሉ፤ በጣም ዝቅተኛ ኃይል ያለው $\psi_1$ ን **የመሬት ሁኔታ(ground state)** ብለው ይጠራሉ፣ እና ኃይላቸው ከ$n^2$ ጋር በተመጣጣኝ የሚጨምር ቀሪዎቹ $n\geq 2$ ሁኔታዎች **የተነሱ ሁኔታዎች(exited states)** ተብለው ይጠራሉ።

## የ$\psi_n$ 4 አስፈላጊ ሂሳባዊ ባህሪያት
ሁሉም የ$\psi_n(x)$ ተግባሮች የሚከተሉትን 4 አስፈላጊ ባህሪያት ይይዛሉ። እነዚህ አራቱ ባህሪያት በጣም ኃይለኛ ሲሆኑ በወሰን የሌለው ካሬ ጉድጓድ ብቻ አይገደቡም። የመጀመሪያው ባህሪ ፖቴንሻሉ ራሱ ሲምሜትሪ ያለው ተግባር ከሆነ ሁልጊዜ ይፈጸማል፤ ሁለተኛው፣ ሦስተኛው እና አራተኛው ባህሪ ግን የፖቴንሻሉ ቅርጽ ምንም ይሁን ምን የሚታዩ አጠቃላይ ባህሪያት ናቸው።

### 1. በጉድጓዱ መሃል አንፃር ጥንድ ተግባርና ነጠላ ተግባር በተራ ይታያሉ።
ለአዎንታዊ ፍፁም ቁጥር $n$፣ $\psi_{2n-1}$ ጥንድ ተግባር ሲሆን $\psi_{2n}$ ደግሞ ነጠላ ተግባር ነው።

### 2. ኃይሉ እየጨመረ ሲሄድ እያንዳንዱ ተከታታይ ሁኔታ አንድ ኖድ ይጨምራል።
ለአዎንታዊ ፍፁም ቁጥር $n$፣ $\psi_n$ $(n-1)$ **ኖዶች(node)** አሉት።

### 3. እነዚህ ሁኔታዎች ኦርቶጎናሊቲ(orthogonality) አላቸው።

$$ \int \psi_m(x)^*\psi_n(x)dx=0, \quad (m\neq n) \tag{11}$$

በሚለው ትርጉም እርስ በርሳቸው **ኦርቶጎናል(orthogonal)** ናቸው።

> አሁን እየተመለከትነው ባለው የወሰን የሌለው ካሬ ጉድጓድ ጉዳይ $\psi$ እውነተኛ እሴት ስለሆነ የ$\psi_m$ ኮንጁጌት ኮምፕሌክስ($^*$) መውሰድ አያስፈልግም፤ ነገር ግን ሌሎች ጉዳዮችን ለመቀበል ሁልጊዜ ማስያዝ የሚጠቅም ልምድ ነው።
{: .prompt-tip }

#### ማረጋገጫ
$m\neq n$ ሲሆን፣

$$ \begin{align*}
\int \psi_m(x)^*\psi_n(x)dx &= \frac{2}{a}\int_0^a \sin{\left(\frac{m\pi}{a}x\right)}\sin(\frac{n\pi}{a}x)dx \\
&= \frac{1}{a}\int_0^a \left[\cos{\left(\frac{m-n}{a}\pi x\right)-\cos{\left(\frac{m+n}{a}\pi x \right)}} \right]dx \\
&= \left\{\frac{1}{(m-n)\pi}\sin{\left(\frac{m-n}{a}\pi x \right)} - \frac{1}{(m+n)\pi}\sin{\left(\frac{m+n}{a}\pi x \right)} \right\}\Bigg|^a_0 \\
&= \frac{1}{\pi}\left\{\frac{\sin[(m-n)\pi]}{m-n}-\frac{\sin[(m+n)\pi]}{m+n} \right\} \\
&= 0.
\end{align*} $$

$m=n$ ሲሆን ይህ ኢንተግራል በመደበኛ ማድረግ ምክንያት $1$ ይሆናል፤ እና **ክሮኔከር(Kronecker) ዴልታ** $\delta_{mn}$ በመጠቀም ኦርቶጎናሊቲን እና መደበኛ ማድረግን

$$ \begin{gather*}
\int \psi_m(x)^*\psi_n(x)dx=\delta_{mn} \label{eqn:orthonomality}\tag{12}\\
\delta_{mn} = \begin{cases}
0, & m\neq n \\
1, & m=n
\end{cases} \label{eqn:kronecker_delta}\tag{13}
\end{gather*}$$

በአንድ መግለጫ ላይ በአንድነት ማሳየትም ይቻላል። በዚህ ጊዜ $\psi$ ዎቹ **ኦርቶኖርማል(orthonormal)** ናቸው ተብለው ይጠራሉ።

### 4. እነዚህ ተግባሮች ሙሉነት(completeness) አላቸው።
ማንኛውም ሌላ ተግባር $f(x)$ እንደ መስመራዊ ጥምረት

$$ f(x) = \sum_{n=1}^{\infty}c_n\psi_n(x) = \sqrt{\frac{2}{a}}\sum_{n=1}^{\infty} c_n\sin\left(\frac{n\pi}{a}x\right) \label{eqn:fourier_series}\tag{14}$$

ሊጻፍ ይችላል በሚለው ትርጉም እነዚህ ተግባሮች **ሙሉ(complete)** ናቸው። ስሌት ($\ref{eqn:fourier_series}$) የ$f(x)$ **የፉሪየ(Fourier) ተከታታይ** ሲሆን፣ ማንኛውም ተግባር በዚህ መልክ ሊዘረጋ ይችላል የሚለውን **የዲሪክሌ(Dirichlet) ቲዎረም** ብለን እንጠራዋለን።

## የፉሪየ(Fourier) ብልሃትን በመጠቀም የ$c_n$ ግቤቶችን ማግኘት
$f(x)$ ሲሰጥ፣ ከላይ ያየነውን ሙሉነት(completeness) እና ኦርቶኖርማሊቲ(orthonormality) በመጠቀም **የፉሪየ(Fourier) ብልሃት** ተብሎ በሚጠራው የሚከተለው ዘዴ የ$c_n$ ግቤቶችን ማግኘት ይቻላል። በስሌት ($\ref{eqn:fourier_series}$) ሁለቱንም ወገኖች በ$\psi_m(x)^*$ በማባዛት እና በማካተት፣ በስሌቶች ($\ref{eqn:orthonomality}$) እና ($\ref{eqn:kronecker_delta}$) መሠረት

$$ \int \psi_m(x)^*f(x)dx = \sum_{n=1}^{\infty} c_n\int\psi_m(x)^*\psi_n(x)dx = \sum_{n=1}^{\infty} c_n\delta_{mn} = c_m \tag{15}$$

እናገኛለን።

> በክሮኔከር ዴልታ ምክንያት በድምሩ ውስጥ $n=m$ የሆነውን ክፍል ብቻ ቀርቶ ሌሎቹ ሁሉ እንደሚጠፉ ያስተውሉ።
{: .prompt-info }

ስለዚህ $f(x)$ ን ሲዘረጋ የ$n$ኛው ግቤት

$$ c_n = \int \psi_n(x)^*f(x)dx \label{eqn:coefficients_n}\tag{16}$$

ነው።

## የጊዜ-ጥገኛ የሽሮዲንገር ስሌት አጠቃላይ መፍትሔ $\Psi(x,t)$ ማግኘት
በወሰን የሌለው ካሬ ጉድጓድ ውስጥ ያለው እያንዳንዱ ቋሚ ሁኔታ፣ ['የጊዜ-ነጻ የሽሮዲንገር ስሌት' ፖስት ውስጥ ያለው ስሌት (10)](/posts/time-independent-schrodinger-equation/#1-ቋሚ-ሁኔታዎችstationary-states-ናቸው) እና ቀደም ብለን ባገኘነው ስሌት ($\ref{eqn:psi_n}$) መሠረት

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \tag{17}$$

ነው። እንዲሁም [የጊዜ-ነጻ የሽሮዲንገር ስሌት](/posts/time-independent-schrodinger-equation/#3-የጊዜ-ጥገኛ-የሽሮዲንገር-ስሌት-አጠቃላይ-መፍትሔ-ተለዋዋጮችን-በመለየት-የተገኙ-መፍትሔዎች-መስመራዊ-ጥምረት-ነው) ውስጥ የሽሮዲንገር ስሌት አጠቃላይ መፍትሔ የቋሚ ሁኔታዎች መስመራዊ ጥምረት መሆኑን ቀደም ብለን አይተናል። ስለዚህ

$$ \Psi(x,t) = \sum_{n=1}^{\infty} c_n\sqrt{\frac{2}{a}}\sin{\left(\frac{n\pi}{a}x \right)}e^{-i(n^2\pi^2\hbar/2ma^2)t} \label{eqn:general_solution}\tag{18}$$

በሚለው መልክ ሊጻፍ ይችላል። አሁን ማድረግ ያለብን የሚከተለውን ሁኔታ የሚያሟሉ የ$c_n$ ግቤቶችን ማግኘት ብቻ ነው።

$$ \Psi(x,0) = \sum_{n=1}^{\infty} c_n\psi_n(x). $$

ቀደም ብለን ባየነው የ$\psi$ ሙሉነት መሠረት ይህን የሚያሟሉ $c_n$ ሁልጊዜ አሉ፣ እና በስሌት ($\ref{eqn:coefficients_n}$) ውስጥ ባለው $f(x)$ ምትክ $\Psi(x,0)$ ን በማስገባት ሊገኙ ይችላሉ።

$$ \begin{align*}
c_n &= \int \psi_n(x)^*\Psi(x,0)dx \\
&= \sqrt{\frac{2}{a}}\int_0^a \sin{\left(\frac{n\pi}{a}x \right)}\Psi(x,0) dx.
\end{align*} \label{eqn:calc_of_cn}\tag{19}$$

መጀመሪያ ሁኔታ $\Psi(x,0)$ ከተሰጠ፣ በስሌት ($\ref{eqn:calc_of_cn}$) በመጠቀም የዝርግ ግቤቶች $c_n$ ይገኛሉ፣ ከዚያም እነሱን በስሌት ($\ref{eqn:general_solution}$) ውስጥ በመተካት $\Psi(x,t)$ ይገኛል። ከዚያ በኋላ [የኤረንፌስት ቲዎረም](/posts/ehrenfest-theorem/) ሂደት መሠረት የሚፈለገው ማንኛውም ፊዚካዊ መጠን ሊሰላ ይችላል። ይህ ዘዴ በወሰን የሌለው ካሬ ጉድጓድ ብቻ ሳይሆን ለማንኛውም ፖቴንሻል ሊተገበር ይችላል፤ የሚለወጡት ግን የ$\psi$ ተግባሮች ቅርጽ እና የተፈቀዱ የኃይል ደረጃዎችን የሚገልጹ ስሌቶች ብቻ ናቸው።

## የኃይል ጥበቃ($\langle H \rangle=\sum\|c_n\|^2E_n$) ማውጣት
የ$\psi(x)$ ኦርቶኖርማሊቲ(ስሌቶች [$\ref{eqn:orthonomality}$]-[$\ref{eqn:kronecker_delta}$]) በመጠቀም ቀደም ብለን [የጊዜ-ነጻ የሽሮዲንገር ስሌት](/posts/time-independent-schrodinger-equation/#የኃይል-ጥበቃ) ውስጥ በአጭሩ ያየነውን የኃይል ጥበቃ እናውጣ። $c_n$ በጊዜ ላይ የማይመሠረት ስለሆነ፣ $t=0$ ላይ ብቻ እውነት መሆኑን ማሳየት ይበቃል።

$$ \begin{align*}
\int|\Psi|^2dx &= \int \left(\sum_{m=1}^{\infty}c_m\psi_m(x)\right)^*\left(\sum_{n=1}^{\infty}c_n\psi_n(x)\right)dx \\
&= \sum_{m=1}^{\infty}\sum_{n=1}^{\infty}c_m^*c_n\int\psi_m(x)^*\psi_n(x)dx \\
&= \sum_{n=1}^{\infty}\sum_{m=1}^{\infty}c_m^*c_n\delta_{mn} \\
&= \sum_{n=1}^{\infty}|c_n|^2
\end{align*} $$

$$ \therefore \sum_{n=1}^{\infty}|c_n|^2 = 1. \quad (\because \int|\Psi|^2dx=1) $$

በተጨማሪም

$$ \hat{H}\psi_n = E_n\psi_n $$

ስለሆነ የሚከተለውን እናገኛለን።

$$ \begin{align*}
\langle H \rangle &= \int \Psi^*\hat{H}\Psi dx = \int \left(\sum c_m\psi_m \right)^*\hat{H}\left(\sum c_n\psi_n \right) dx \\
&= \sum\sum c_m c_n E_n\int \psi_m^*\psi_n dx \\
&= \sum\sum c_m c_n E_n\delta_{mn} \\
&= \sum|c_n|^2E_n. \ \blacksquare
\end{align*} $$
