---
title: የስበት መስክ እና የስበት ፖቴንሻል
description: "በኒውተን የአጽናፈ ስበት ሕግ መሠረት የስበት መስክ ቬክተርና የስበት ፖቴንሻል ትርጓሜዎችን እንመለከታለን፣ እና በሁለት አስፈላጊ ምሳሌዎች የቅርፊት ቲዎሬምንና የጋላክሲ ዞር ከርቭን እንወያያለን።"
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Gravitation]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR
> - የኒውተን የአጽናፈ ስበት ሕግ: $\mathbf{F} = -G\cfrac{mM}{r^2}\mathbf{e}_r$
> - ቀጣይ የብዛት ስርጭት እና መጠን ላላቸው አካላት ሲሆን: $\mathbf{F} = -Gm\int_V \cfrac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime}$
>   - $\rho(\mathbf{r^{\prime}})$: ከማንኛውም መነሻ ነጥብ የቦታ ቬክተሩ $\mathbf{r^{\prime}}$ በሆነ ነጥብ ላይ ያለ የብዛት እፍጋት
>   - $dv^{\prime}$: ከማንኛውም መነሻ ነጥብ የቦታ ቬክተሩ $\mathbf{r^{\prime}}$ በሆነ ነጥብ ላይ ያለ የመጠን አካል
> - **የስበት መስክ ቬክተር(gravitational field vector)**:
>   - ብዛቱ $M$ በሆነ አካል የተፈጠረ መስክ ውስጥ አንድ ቅንጣት በአንድ ክፍል ብዛት የሚቀበለውን ኃይል የሚወክል ቬክተር
>   - $\mathbf{g} = \cfrac{\mathbf{F}}{m} = - G \cfrac{M}{r^2}\mathbf{e}_r = - G \int_V \cfrac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime$
>   - *በአንድ ክፍል ብዛት ኃይል* ወይም *ፍጥነት ለውጥ(acceleration)* ልኬት አለው
> - **የስበት ፖቴንሻል(gravitational potential)**:
>   - $\mathbf{g} \equiv -\nabla \Phi$
>   - $($*በአንድ ክፍል ብዛት ኃይል* $) \times ($*ርቀት* $)$ ወይም *በአንድ ክፍል ብዛት ኃይል ኃይል(energy)* ልኬት አለው
>   - $\Phi = -G\cfrac{M}{r}$
>   - የስበት ፖቴንሻል ከነዚህ ውስጥ የሚያስፈልገው አንጻራዊ ልዩነቱ ብቻ ነው፤ ራሱ የተወሰነ እሴት ግን ትርጉም የለውም
>   - ብዙውን ጊዜ $r \to \infty$ ሲሆን $\Phi \to 0$ ብለን በፈቃድ እንወስናለን፣ ይህም የማይወሰንነት(ambiguity) ያስወግዳል
>   - $U = m\Phi, \quad \mathbf{F} = -\nabla U$
> - **በጎላ ቅርፊት ውስጥና ውጭ ያለ የስበት ፖቴንሻል(የቅርፊት ቲዎሬም)**
>   - $R>a$ ሲሆን:
>     - $\Phi(R>a) = -\cfrac{GM}{R}$
>     - ከቁስ የጎላዊ ሲምሜትሪ ስርጭት(spherical symmetric distribution) የተነሳ በውጭ ያለ ማንኛውም ነጥብ የስበት ፖቴንሻልን ለማግኘት ይህን አካል እንደ ነጥብ ብዛት(point mass) ቆጥረን መለካት እንችላለን
>   - $R<b$ ሲሆን:
>     - $\Phi(R<b) = -2\pi\rho G(a^2 - b^2)$
>     - በጎላዊ ሲምሜትሪ ያለው የብዛት ቅርፊት ውስጥ የስበት ፖቴንሻል ቦታን ሳይመለከት ቋሚ ነው፣ የሚሰራው የስበት ኃይል ግን $0$
>   - $b<R<a$ ሲሆን: $\Phi(b<R<a) = -4\pi\rho G \left( \cfrac{a^2}{2} - \cfrac{b^3}{3R} - \cfrac{R^2}{6} \right)$
{: .prompt-info }

## የስበት መስክ
### የኒውተን የአጽናፈ ስበት ሕግ
ኒውተን ከ11666 HE በፊትም ቢሆን የአጽናፈ ስበት ሕጉን በሥርዓት አዘጋጅቶ በቁጥርም አረጋግጦ ነበር። ቢሆንም በ11687 HE በ*Principia* ውስጥ የራሱን ውጤት እስኪያትም ድረስ ተጨማሪ 20 ዓመታት ፈጅቶበታል፤ ምክንያቱም ምድርንና ጨረቃን መጠን የሌላቸው ነጥብ ብዛቶች(point mass) ብሎ ያደረገውን ስሌት ማጽደቅ አልቻለም ነበር። ደግሞ ሆኖ [ኒውተን ራሱ በኋላ የፈጠረውን ካልኩለስ(calculus) ብንጠቀም፣ በ11600 ዎቹ ለኒውተን ቀላል ያልነበረውን ያ ችግኝ እኛ በጣም በቀላሉ ማረጋገጥ እንችላለን](#ra-ሲሆን)።

የኒውተን የአጽናፈ ስበት ሕግ(Newton's law of universal gravitation) እንደሚል፣ *እያንዳንዱ የብዛት ቅንጣት በአጽናፈ ዓለም ያሉ ሌሎች ሁሉንም ቅንጣቶች ይስባል፣ እና ይህ ኃይል ከሁለቱ ብዛቶች ምርት ጋር ተመጣጣኝ ሲሆን በመካከላቸው ያለው ርቀት ካሬ ጋር ተቃራኒ ተመጣጣኝ ነው።* በሂሳብ ማለት ይህን ይሆናል።

$$ \mathbf{F} = -G\frac{mM}{r^2}\mathbf{e}_r \label{eqn:law_of_gravitation}\tag{1} $$

![Newton's law of universal gravitation](https://upload.wikimedia.org/wikipedia/commons/0/0e/NewtonsLawOfUniversalGravitation.svg)
> *የምስል ምንጭ*
> - ደራሲ: የዊኪሚዲያ ተጠቃሚ [Dennis Nilsson](https://commons.wikimedia.org/wiki/User:Dna-webmaster)
> - ፈቃድ: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

አንድነት ቬክተሩ $\mathbf{e}_r$ ከ$M$ ወደ $m$ አቅጣጫ ይመራል፣ እና ያለው አሉታዊ ምልክት ኃይሉ መሳብ መሆኑን ያሳያል። ማለትም $m$ ወደ $M$ ይሳባል።

### የካቨንዲሽ ሙከራ
ይህ ሕግ በሙከራ መረጋገጡና የ$G$ እሴት መወሰኑ በ11798 HE በእንግሊዝ ፊዚሺስት ሄንሪ ካቨንዲሽ(Henry Cavendish) ተፈጽሟል። የካቨንዲሽ ሙከራ በቀላል ዘንግ ሁለቱ ጫፎች ላይ የተጣበቁ ሁለት ትንሽ ኳሶች ያሉበት የጥለት ሚዛን(torsion balance) ይጠቀማል። እነዚህ ሁለት ኳሶች እያንዳንዳቸው በአቅራቢያቸው ያሉ ሌሎች ሁለት ትልቅ ኳሶች አቅጣጫ ይሳባሉ። እስካሁን ድረስ የተገኘው የ$G$ ይፋዊ እሴት $6.673 \pm 0.010 \times 10^{-11} \mathrm{N\cdot m^2/kg^2}$ ነው።

> $G$ ከጥንት ጀምሮ የታወቀ መሠረታዊ ቋሚ ቢሆንም፣ $e$, $c$, $\hbar$ እንደሚባሉት አብዛኞቹ ሌሎች መሠረታዊ ቋሚዎች ከሚታወቁበት ያነሰ ትክክለኛነት(precision) ብቻ ነው የምናውቀው። ዛሬም ቢሆን $G$ እሴቱን በከፍተኛ ትክክለኛነት ለማወቅ ብዙ ምርምሮች እየተካሄዱ ናቸው።
{: .prompt-tip }

### መጠን ላላቸው አካላት ሲሆን
በጥብቅ አነጋገር የእኩልታ ($\ref{eqn:law_of_gravitation}$) ሕግ *ለነጥብ ቅንጣት(point particle)* ብቻ ነው የሚተገበረው። ከሁለቱ አንዱ ወይም ሁለቱም መጠን ያላቸው አካላት ከሆኑ ግን ኃይሉን ለማስላት የስበት መስክ(gravitational force field) *መስመራዊ መስክ(linear field)* ነው የሚለውን ተጨማሪ ግምት ማድረግ ያስፈልጋል። ማለትም ብዛቱ $m$ የሆነ አንድ ቅንጣት ከብዙ ሌሎች ቅንጣቶች የሚቀበለው ጠቅላላ የስበት ኃይል እያንዳንዱን ኃይል ቬክተር በመደመር ማግኘት እንደሚቻል እንገምታለን። ንጥረ ነገር በቀጣይ ሁኔታ የተሰራጨበት አካል ሲሆን ድምርን እንዲህ ባለ ኢንቲግራል እንቀይራለን።

$$ \mathbf{F} = -Gm\int_V \frac{dM}{r^2}\mathbf{e}_r = -Gm\int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2} dv^{\prime} \label{eqn:integral_form}\tag{2}$$

- $\rho(\mathbf{r^{\prime}})$: ከማንኛውም መነሻ ነጥብ የቦታ ቬክተሩ $\mathbf{r^{\prime}}$ በሆነ ነጥብ ላይ ያለ የብዛት እፍጋት
- $dv^{\prime}$: ከማንኛውም መነሻ ነጥብ የቦታ ቬክተሩ $\mathbf{r^{\prime}}$ በሆነ ነጥብ ላይ ያለ የመጠን አካል

ብዛቱ $M$ የሆነ አካልና ብዛቱ $m$ የሆነ አካል ሁለቱም መጠን ካላቸው ግን ጠቅላላ የስበት ኃይሉን ለማግኘት በ$m$ ላይ ሁለተኛ የመጠን ኢንቲግራልም ያስፈልጋል።

### የስበት መስክ ቬክተር
**የስበት መስክ ቬክተር(gravitational field vector)** $\mathbf{g}$ ብዛቱ $M$ በሆነ አካል የተፈጠረ መስክ ውስጥ አንድ ቅንጣት በአንድ ክፍል ብዛት የሚቀበለውን ኃይል የሚወክል ቬክተር ብለን እንገልጸዋለን፤ ስለዚህ

$$ \mathbf{g} = \frac{\mathbf{F}}{m} = - G \frac{M}{r^2}\mathbf{e}_r \label{eqn:g_vector}\tag{3} $$

ወይም

$$ \boxed{\mathbf{g} = - G \int_V \frac{\rho(\mathbf{r^\prime})\mathbf{e}_r}{r^2}dv^\prime} \tag{4} $$

ብለን እንጻፈዋለን። እዚህ $\mathbf{e}_r$ አቅጣጫ በ$\mathbf{r^\prime}$ መሠረት ይለዋወጣል።

ይህ መጠን $\mathbf{g}$ *በአንድ ክፍል ብዛት ኃይል* ወይም *ፍጥነት ለውጥ(acceleration)* ልኬት አለው። በምድር ፊት አቅራቢያ ያለው የስበት መስክ ቬክተር $\mathbf{g}$ መጠን እኛ **የስበት ፍጥነት ቋሚ(gravitational acceleration constant)** ብለን ከምንጠራው መጠን ጋር እኩል ሲሆን፣ $\|\mathbf{g}\| \approx 9.80\mathrm{m/s^2}$ ነው።

## የስበት ፖቴንሻል
### ትርጓሜ
የስበት መስክ ቬክተር $\mathbf{g}$ እንደ $1/r^2$ ይለዋወጣል፣ ስለዚህ ደግሞ ይህ አንድ ስካላር ፋንክሽን(ፖቴንሻል) ግራዲየንት(gradient) ሆኖ እንዲገለጽ የሚያስፈልገውን ሁኔታ ($\nabla \times \mathbf{g} \equiv 0$) ያሟላል። ስለዚህ እንዲህ ማለት እንችላለን።

$$ \mathbf{g} \equiv -\nabla \Phi \label{eqn:gradient_phi}\tag{5}$$

እዚህ $\Phi$ን **የስበት ፖቴንሻል(gravitational potential)** እንለዋለን፣ እና ይህ $($*በአንድ ክፍል ብዛት ኃይል* $) \times ($*ርቀት* $)$ ወይም *በአንድ ክፍል ብዛት ኃይል ኃይል(energy)* ልኬት አለው።

$\mathbf{g}$ በራዲየስ ብቻ ስለሚመሠረት፣ $\Phi$ም በ$r$ መሠረት ይለዋወጣል። ከእኩልታዎች ($\ref{eqn:g_vector}$) እና ($\ref{eqn:gradient_phi}$)

$$ \nabla\Phi = \frac{d\Phi}{dr}\mathbf{e}_r = G\frac{M}{r^2}\mathbf{e}_r $$

ይሆናል፣ ይህንንም ሲንቲግሬት ካደረግን

$$ \boxed{\Phi = -G\frac{M}{r}} \label{eqn:g_potential}\tag{6}$$

እናገኛለን። የስበት ፖቴንሻል አንጻራዊ ልዩነቱ ብቻ ትርጉም ስላለው ፍጹም እሴቱ ግን ትርጉም የለውም፣ ስለዚህ የኢንቲግሬሽን ቋሚውን መተው እንችላለን። ብዙውን ጊዜ $r \to \infty$ ሲሆን $\Phi \to 0$ ብለን በፈቃድ እንወስናለን፣ ይህም የማይወሰንነት(ambiguity) ያስወግዳል፤ እኩልታ ($\ref{eqn:g_potential}$) ደግሞ ይህን ሁኔታ ያሟላል።

ንጥረ ነገር በቀጣይ ሁኔታ የተሰራጨ ከሆነ የስበት ፖቴንሻሉ እንዲህ ነው።

$$ \Phi = -G\int_V \frac{\rho(\mathbf{r\prime})}{r}dv^\prime \label{eqn:g_potential_v}\tag{7}$$

ብዛት በቀጭን ቅርፊት ላይ በወለል ስርጭት የተከፋፈለ ከሆነ

$$ \Phi = -G\int_S \frac{\rho_s}{r}da^\prime. \label{eqn:g_potential_s}\tag{8}$$

እና መስመራዊ እፍጋቱ $\rho_l$ የሆነ የመስመር ብዛት ምንጭ ከሆነ ደግሞ እንዲህ ማለት እንችላለን።

$$ \Phi = -G\int_\Gamma \frac{\rho_l}{r}ds^\prime. \label{eqn:g_potential_l}\tag{9}$$

### አካላዊ ትርጉም
አንድ አካል በስበት መስክ ውስጥ $d\mathbf{r}$ መጠን ሲንቀሳቀስ፣ ያ አካል በአንድ ክፍል ብዛት የሚያደርገውን ሥራ $dW^\prime$ እንመልከት።

$$ \begin{align*}
dW^\prime &= -\mathbf{g}\cdot d\mathbf{r} = (\nabla \Phi)\cdot d\mathbf{r} \\
&= \sum_i \frac{\partial \Phi}{\partial x_i}dx_i = d\Phi \label{eqn:work}\tag{10}
\end{align*} $$

በዚህ እኩልታ ውስጥ $\Phi$ የቦታ ኮኦርዲኔቶች ብቻ ተግባር ሲሆን፣ $\Phi=\Phi(x_1, x_2, x_3) = \Phi(x_i)$ ብለን እንጽፈዋለን። ስለዚህ በስበት መስክ ውስጥ አንድ አካልን ከአንድ ነጥብ ወደ ሌላ ነጥብ ሲንቀሳቀስ፣ ያ አካል በአንድ ክፍል ብዛት የሚያደርገው ሥራ መጠን በእነዚያ ሁለት ነጥቦች መካከል ካለው የፖቴንሻል ልዩነት ጋር እኩል መሆኑን እናውቃለን።

ማያልቅ ርቀት ላይ ያለውን የስበት ፖቴንሻል $0$ ብለን ከገለጽነው፣ በማንኛውም ነጥብ ያለው $\Phi$ እቃውን ከማያልቅ ርቀት ጀምሮ እስከዚያ ነጥብ ለማምጣት የሚያስፈልገው በአንድ ክፍል ብዛት ሥራ ተብሎ ሊተረጎም ይችላል። የአካሉ ፖቴንሻል ኃይል ከአካሉ ብዛትና ከየስበት ፖቴንሻል $\Phi$ ምርት ጋር እኩል ስለሆነ፣ $U$ን ፖቴንሻል ኃይል ብለን ካለን

$$ U = m\Phi. \label{eqn:potential_e}\tag{11} $$

ስለዚህ አካሉ የሚቀበለው የስበት ኃይል ከፖቴንሻል ኃይሉ ግራዲየንት ላይ አሉታዊ ምልክት በመጨመር ይገኛል።

$$ \mathbf{F} = -\nabla U \label{eqn:force_and_potential}\tag{12} $$

አንድ አካል በአንድ ብዛት የተፈጠረ የስበት መስክ ውስጥ ሲኖር ሁልጊዜ የተወሰነ ፖቴንሻል ኃይል ይፈጠራል። ይህ ፖቴንሻል ኃይል በጥብቅ አነጋገር በመስኩ ራሱ ውስጥ ያለ ቢሆንም፣ በተለምዶ የእቃው ፖቴንሻል ኃይል ብለን እንጠራዋለን።

## ምሳሌ፡ በጎላ ቅርፊት ውስጥና ውጭ ያለ የስበት ፖቴንሻል (የቅርፊት ቲዎሬም)
### ኮኦርዲኔት ማቀናበር እና የስበት ፖቴንሻሉን በኢንቲግራል መግለጽ
ውስጣዊ ራዲየሱ $b$ እና ውጫዊ ራዲየሱ $a$ የሆነ አንድ አንደኛ ወጥ የጎላ ቅርፊት(spherical shell) በውስጡና በውጩ ያለውን የስበት ፖቴንሻል እንፈልግ። በጎላ ቅርፊቱ የሚፈጠረውን የስበት ኃይል በመስክ ውስጥ ባለ አንድ ክፍል ብዛት ላይ የሚሰሩ የኃይል ክፍሎችን በቀጥታ በመቁጠር ማግኘት ቢቻልም፣ የፖቴንሻል ዘዴ መጠቀም ከዚህ ይልቅ ቀላል ነው።

![Spherical shell](/assets/img/gravitational-field-and-potential/spherical-shell.png)

ከላይ ባለው ስዕል ውስጥ ከማዕከሉ ርቀቱ $R$ በሆነው $P$ ነጥብ ላይ ያለውን ፖቴንሻል እንቁጠር። የቅርፊቱ ወጥ የብዛት ስርጭት ካለ እንደምንገምት $\rho(r^\prime)=\rho$ ይሆናል፣ እና የጎላውን ማዕከል ከ$P$ ነጥብ ጋር የሚያገናኘውን መስመር መሠረት አድርገን በአዚሙት ማእዘን $\phi$ ላይ ሲምሜትሪ ስለሚኖር

$$\begin{align*}
\Phi &= -G\int_V \frac{\rho(r^\prime)}{r}dv^\prime \\
&= -\rho G \int_0^{2\pi} \int_0^\pi \int_b^a \frac{1}{r}(dr^\prime)(r^\prime d\theta)(r^\prime \sin\theta\, d\phi) \\
&= -\rho G \int_0^{2\pi} d\phi \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta \\
&= -2\pi\rho G \int_b^a {r^\prime}^2 dr^\prime \int_0^\pi \frac{\sin\theta}{r}d\theta. \label{eqn:spherical_shell_1}\tag{13}
\end{align*}$$

የኮሳይን ሕግ መሠረት

$$ r^2 = {r^\prime}^2 + R^2 - 2r^\prime R \cos\theta \label{eqn:law_of_cosines}\tag{14}$$

ሲሆን $R$ ቋሚ ነው፤ ስለዚህ ይህንን እኩልታ በ$r^\prime$ ላይ ሳይሆን በ$\theta$ ላይ እንደሚገባ በመለየት

$$ 2rdr = 2r^\prime R \sin\theta d\theta $$

$$ \frac{\sin\theta}{r}d\theta = \frac{dr}{r^\prime R} \tag{15}$$

እናገኛለን። ይህንን በእኩልታ ($\ref{eqn:spherical_shell_1}$) ውስጥ በመተካት

$$ \Phi = -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r_\mathrm{min}}^{r_\mathrm{max}} dr. \label{eqn:spherical_shell_2}\tag{16} $$

እዚህ $r_\mathrm{max}$ እና $r_\mathrm{min}$ በ$P$ ነጥብ ቦታ መሠረት ይወሰናሉ።

### $R>a$ ሲሆን

$$ \begin{align*}
\Phi(R>a) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{R-r^\prime}^{R+r^\prime} dr \\
&= - \frac{4\pi\rho G}{R} \int_b^a {r^\prime}^2 dr^\prime \\
&= - \frac{4}{3}\frac{\pi\rho G}{R}(a^3 - b^3). \label{eqn:spherical_shell_outside_1}\tag{17}
\end{align*} $$

የጎላ ቅርፊቱ ጠቅላላ ብዛት $M$ እንዲህ ይሰጣል።

$$ M = \frac{4}{3}\pi\rho(a^3 - b^3) \label{eqn:mass_of_shell}\tag{18}$$

ስለዚህ ፖቴንሻሉ እንዲህ ይሆናል።

$$ \boxed{\Phi(R>a) = -\frac{GM}{R}} \label{eqn:spherical_shell_outside_2}\tag{19}$$

> በብዛቱ $M$ የሆነ ነጥብ ብዛት የሚፈጥረውን የስበት ፖቴንሻል እኩልታ ($\ref{eqn:g_potential}$) እና አሁን ያገኘነውን ውጤት ($\ref{eqn:spherical_shell_outside_2}$) ብንነጻጸር አንድ መሆናቸውን እናያለን። ይህ ማለት ደግሞ ከቁስ የጎላዊ ሲምሜትሪ ስርጭት(spherical symmetric distribution) የተነሳ በውጭ ያለ ማንኛውም ነጥብ የስበት ፖቴንሻልን ለማግኘት ሁሉም ብዛት በማዕከሉ ላይ ተከማችቷል ብለን መቆጠር እንደሚቻል ነው። ምድር ወይም ጨረቃ እንደሚመስሉ ከተወሰነ መጠን በላይ ያሉ አብዛኞቹ የጎላ ሰማያዊ አካላት በዚህ ውስጥ ይገባሉ፤ እነሱም እንደ [ማትሪዮሽካ(Matryoshka)](https://en.wikipedia.org/wiki/Matryoshka_doll) በአንድ ማዕከል የተዛመዱና የተለያዩ ዲያሜትሮች ያላቸው በብዙ ቁጥር የተደራረቡ የጎላ ቅርፊቶች እንዳሉባቸው ማሰብ ይቻላል። ይህም በዚህ ጽሑፍ መጀመሪያ ላይ የተጠቀሰው [እንደ ምድር ወይም ጨረቃ ያሉ ሰማያዊ አካላትን መጠን የሌላቸው ነጥብ ብዛቶች ብለን ቆጥረን ማስላት ለምን ትክክል እንደሆነ የሚያሳይ መሠረት](#የኒውተን-የአጽናፈ-ስበት-ሕግ) ይሆናል።
{: .prompt-info }

### $R<b$ ሲሆን

$$\begin{align*}
\Phi(R<b) &= -\frac{2\pi\rho G}{R} \int_b^a r^\prime dr^\prime \int_{r^\prime - R}^{r^\prime + R}dr \\
&= -4\pi\rho G \int_b^a r^\prime dr^\prime \\
&= -2\pi\rho G(a^2 - b^2). \label{eqn:spherical_shell_inside}\tag{20}
\end{align*}$$

> በጎላዊ ሲምሜትሪ ያለው የብዛት ቅርፊት ውስጥ የስበት ፖቴንሻል ቦታን ሳይመለከት ቋሚ ነው፣ እና የሚሰራው የስበት ኃይል $0$ ነው።
{: .prompt-info }

> እንዲሁም ይህ ከተለመዱ የውሸት ሳይንስ እምነቶች አንዱ የሆነው ‘ባዶ ውስጥ ያለች ምድር(Hollow Earth)’ የማይረባ ነገር መሆኑን የሚያሳይ ዋና ማስረጃ ነው። እንደ ዚያ ሀሳብ የሚነገረው ሁሉ ምድር የጎላ ቅርፊት ቅርጽ ኖራ ውስጧም ባዶ ብትሆን፣ በዚያ ጉድጓድ ውስጥ ላሉ ሁሉም ነገሮች የምድር ስበት አይሰራም። የምድርን ብዛትና መጠን ብናስብ እንኳን እንደዚህ ያለ ባዶ ክፍተት ሊኖር አይችልም፤ እንኳን ቢኖር በዚያ ያሉ ሕይወት ያላቸው ፍጥረታት የጎላ ቅርፊቱን ውስጠኛ ገጽ መሬት አድርገው አይኖሩም፣ እንደ ስፔስ ስቴሽን በክብደት አልባ ሁኔታ ይንሳፈፋሉ።  
> [በመሬት ሥር ጥቂት ኪ.ሜ. ጥልቀት ውስጥ ያሉ የአፈር ንብርብሮች ውስጥ ማይክሮኦርጋኒዝሞች ሊኖሩ ይችላሉ](https://youtu.be/VD6xJq8NguY?si=szgtuLkuk6rPJag3)፣ ግን ቢያንስ በ‘ባዶ ውስጥ ያለች ምድር’ እምነት የሚነገረው ዓይነት መልክ ግን አይቻልም። የጁል ቨርን(Jules Verne) ልቦለድ 《ወደ ምድር ማዕከል ጉዞ(Voyage au centre de la Terre)》 እና ፊልሙ ‘ወደ የጠፋው ዓለም ፍለጋ(Journey to the Center of the Earth)’ እኔም እወዳቸዋለሁ፣ ግን ፈጠራ ሥራዎችን እንደ ፈጠራ ሥራ ብቻ መደሰት ነው ያለብን፤ በቁም ነገር መመን አይገባም።
{: .prompt-tip }

### $b<R<a$ ሲሆን

$$\begin{align*}
\Phi(b<R<a) &= -\frac{4\pi\rho G}{3R}(R^3 - b^3) - 2\pi\rho G(a^2 - R^2) \\
&= -4\pi\rho G \left( \frac{a^2}{2} - \frac{b^3}{3R} - \frac{R^2}{6} \right) \label{eqn:within_spherical_shell}\tag{21}
\end{align*}$$

### ውጤት
ከዚህ በፊት በሶስቱ ክልሎች ያገኘነውን የስበት ፖቴንሻል $\Phi$፣ እና ከእሱ የሚመጣውን የስበት መስክ ቬክተር መጠን $\|\mathbf{g}\|$ እንደ ርቀት $R$ ተግባር በግራፍ ብናሳይ እንዲህ ይሆናል።

![Gravitational Potential as a Function of R](/physics-visualizations/figs/shell-theorem-gravitational-potential.png)  
![Magnitude of the Field Vector as a Function of R](/physics-visualizations/figs/shell-theorem-field-vector.png)  
> - የPython ቪዥዋላይዜሽን ኮድ: [yunseo-kim/physics-visualizations ሪፖዚቶሪ](https://github.com/yunseo-kim/physics-visualizations/blob/main/src/shell_theorem.py)
> - ፈቃድ: [See here](https://github.com/yunseo-kim/physics-visualizations?tab=readme-ov-file#license)

የስበት ፖቴንሻሉና የስበት መስክ ቬክተር መጠኑ ቀጣይ መሆናቸውን ማየት እንችላለን። እንደ ሆነ የስበት ፖቴንሻል በአንድ ነጥብ ላይ የተቋረጠ ከሆነ፣ በዚያ ነጥብ የፖቴንሻሉ ግራዲየንት፣ ማለትም የስበቱ መጠን ማያልቅ ይሆናል፤ ይህ በአካላዊ እውነታ የማይታመን ስለሆነ የፖቴንሻል ተግባሩ በሁሉም ነጥቦች ላይ ቀጣይ መሆን አለበት። ነገር ግን የስበት መስክ ቬክተር *የልዩነት ኮኤፊሺየንት* በቅርፊቱ ውስጠኛና ውጫዊ ገጾች ላይ የተቋረጠ ነው።

## ምሳሌ፡ የጋላክሲ ዞር ከርቭ
በአስትሮኖሚ ምልከታዎች መሠረት፣ እንደ እኛ ጋላክሲ ወይም አንድሮመዳ ጋላክሲ ያሉ በማዕከሉ ዙሪያ የሚዞሩ ብዙ ስፓይረል ጋላክሲዎች ውስጥ የሚታየው ብዛት አብዛኛው በማዕከላዊ ክፍል አቅራቢያ ተከማችቶ ይገኛል። ነገር ግን በእነዚህ ስፓይረል ጋላክሲዎች ውስጥ ያሉ ብዛቶች የኦርቢት ፍጥነቶች፣ ከሚታየው የብዛት ስርጭት በመነሳት በቲዎሪ የተተነበዩት እሴቶች ጋር እጅግ እንደማይጣጣሙ እና ከተወሰነ ርቀት በኋላ በቅርብ ቋሚ እንደሚሆኑ በሚከተለው ግራፍ ማየት ይቻላል።

![Galactic Rotation](https://upload.wikimedia.org/wikipedia/commons/b/b9/GalacticRotation2.svg){: width="972" }
> *የምስል ምንጭ*
> - ደራሲ: የዊኪፔዲያ ተጠቃሚ [PhilHibbs](https://en.wikipedia.org/wiki/User:PhilHibbs)
> - ፈቃድ: Public Domain

{% 
  include embed/video.html 
  src='https://cdn.jsdelivr.net/gh/yunseo-kim/yunseo-kim.github.io/assets/video/gravitational-field-and-potential/Galaxy_rotation_under_the_influence_of_dark_matter.webm' 
  title="ግራ: ከሚታየው ብዛት የተነሳ የተተነበየ የጋላክሲ ዞር | ቀኝ: በእውነት የታየ የጋላክሲ ዞር።" 
  types='ogg'
  autoplay=true 
  loop=true 
%}
> *የቪዲዮ ምንጭ*
> - የመነሻ ፋይል(Ogg Theora video) አገናኝ: <https://commons.wikimedia.org/wiki/File:Galaxy_rotation_under_the_influence_of_dark_matter.ogv>
> - ደራሲ: [Ingo Berg](https://beltoforion.de/en/index.php)
> - ፈቃድ: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en)
> - የተጠቀሙት የሲሙሌሽን ዘዴና ኮድ: <https://beltoforion.de/en/spiral_galaxy_renderer/>

> ቀደም ሲል በዚህ ገጽ ውስጥ የተካተተው `Rotation curve of spiral galaxy Messier 33 (Triangulum).png` ምስል ፋይል፣ [የቨርጂኒያ ዩኒቨርሲቲ ፕሮፌሰር Mark Whittle](https://markwhittle.uvacreate.virginia.edu/) ያለነፃ ፈቃድ ሥራን የዊኪሚዲያ ተጠቃሚ [Mario De Leo](https://commons.wikimedia.org/wiki/User:Accrama) [አግባብ ያለው ጥቅስ ሳይሰጥ የተቀዳ ተዋጽኦ ሥራ መሆኑ ከተረጋገጠ በኋላ ከዊኪሚዲያ ኮመንስ ተሰርዟል](https://commons.wikimedia.org/wiki/Commons:Deletion_requests/File:Rotation_curve_of_spiral_galaxy_Messier_33_(Triangulum).png)፣ ስለዚህ ከዚህ ገጽም እንዲሁ እንደተወገደ እገልጻለሁ።
{: .prompt-danger }

የጋላክሲው ብዛት በማዕከላዊ ክፍል ተከማችቶ ካለ ከርቀት ጋር የሚለዋወጠውን የኦርቢት ፍጥነት እንተነብይ፣ ይህ ትንበያ ከእነዚህ ምልከታ ውጤቶች ጋር እንደማይጣጣም እና ከጋላክሲው ማዕከል እስከ ርቀት $R$ ድረስ የተሰራጨው ብዛት $M(R)$ ከ$R$ ጋር ተመጣጣኝ መሆን እንዳለበት እንሳይ።

መጀመሪያ የጋላክሲ ብዛት $M$ በማዕከላዊ ክፍል ተከማችቶ ካለ፣ በርቀት $R$ ያለው የኦርቢት ፍጥነት እንዲህ ይሆናል።

$$ \frac{GMm}{R^2} = \frac{mv^2}{R} $$

$$ v = \sqrt{\frac{GM}{R}} \propto \frac{1}{\sqrt{R}}. $$

በዚህ ሁኔታ በላይ ባሉት ሁለት ግራፎች ላይ በቁልቁል መስመር እንደታየው $1/\sqrt{R}$ የሚቀንስ የኦርቢት ፍጥነት እንደሚገመት ይገኛል፣ ነገር ግን በምልከታ ውጤቶች መሠረት የኦርቢት ፍጥነቱ $v$ ከርቀት $R$ ጋር በቅርብ ቋሚ ነው፣ ስለዚህ ትንበያውና ምልከታው አይጣጣሙም። እነዚህ ምልከታዎች ሊተረጎሙ የሚችሉት $M(R)\propto R$ ሲሆን ብቻ ነው።

የተመጣጣኝነት ቋሚውን $k$ ብለን $M(R) = kR$ ካስቀመጥን፣

$$ v = \sqrt{\frac{GM(R)}{R}} = \sqrt{Gk}\ \text{(ቋሚ)}. $$

ከዚህ በመነሳት አስትሮፊዚሲስቶች ብዙ ጋላክሲዎች ውስጥ እስካሁን ያልተገኘ ‘ጨለማ ቁስ(dark matter)’ እንዲኖር አስፈላጊ እንደሆነ እና ይህ ጨለማ ቁስ ከአጽናፈ ዓለም ጠቅላላ ብዛት 90% በላይ መሆን እንዳለበት ድምዳሜ ይደርሳሉ። ሆኖም የጨለማ ቁስ ትክክለኛ ማንነት እስካሁን ግልጽ ሆኖ አልተገለጸም፣ እና ዋና ፅንሰ ሀሳብ ባይሆንም የጨለማ ቁስ መኖሩን ሳይገምቱ ምልከታ ውጤቶቹን ለማብራራት እንደ ተሻሻለ የኒውተን ዳይናሚክስ(Modified Newtonian Dynamics, MOND) ያሉ ሙከራዎችም አሉ። ዛሬ ይህ የምርምር መስክ በአስትሮፊዚክስ የፊት መስመር ላይ ይገኛል።
