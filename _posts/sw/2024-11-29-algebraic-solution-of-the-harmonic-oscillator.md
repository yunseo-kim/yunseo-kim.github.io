---
title: "Suluhisho la kialjebra la osileta harmoniki (The Harmonic Oscillator)"
description: "Mwongozo wa suluhisho la kialjebra la osileta harmoniki katika mekaniki ya kwanta: commutator, uhusiano wa ubadilishanaji kanoniki, opereta za ngazi, kazi za mawimbi, na viwango vya nishati."
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function, Commutator, Ladder
    Operators]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## Kwa kifupi
> - Iwapo amplitudo ni ndogo vya kutosha, mtetemo wowote unaweza kukaribiwa kama mtetemo harmoniki sahili (simple harmonic oscillation), na kwa sababu hiyo mtetemo harmoniki sahili una umuhimu mkubwa katika fizikia
> - Osileta harmoniki: $V(x) = \cfrac{1}{2}kx^2 = \cfrac{1}{2}m\omega^2 x^2$
> - **Komuteta (commutator)**:
>   - Operesheni ya kibinari inayoonyesha kwa kiwango gani opereta mbili hazibadilishani vizuri
>   - $\left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}$
> - **Uhusiano wa ubadilishanaji kanoniki (canonical commutation relation)**: $\left[\hat{x},\hat{p}\right] = i\hbar$
> - **Opereta za ngazi (ladder operators)**:
>   - $\hat{a}_\pm \equiv \cfrac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x})$
>   - $\hat{a}\_+$ huitwa **opereta ya kuinua (raising operator)**, na $\hat{a}\_-$ huitwa **opereta ya kushusha (lowering operator)**
>   - Kwa hali tuli yoyote, zinaweza kuinua au kushusha kiwango cha nishati; hivyo ukipata suluhisho moja tu la mlinganyo wa Schrödinger usiotegemea muda, unaweza kupata suluhisho nyingine zote pia
>
> $$\hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right) $$
>
> - Kazi ya mawimbi na kiwango cha nishati cha hali tuli ya $n$:
>   - Hali ya msingi (hali tuli ya $0$):
>     - $\psi_0(x) = \left(\cfrac{m\omega}{\pi\hbar} \right)^{1/4}\exp\left(-\cfrac{m\omega}{2\hbar}x^2\right)$
>     - $E_0 = \cfrac{1}{2}\hbar\omega$
>   - Hali tuli ya $n$:
>     - $\psi_n(x) = \cfrac{1}{\sqrt{n!}}(\hat{a}_+)^n \psi_0(x)$
>     - $E_n = \left(n + \cfrac{1}{2} \right)\hbar\omega$
> - $\hat{a}\_\mp$ ni **konjugati ya Hermite (hermitian conjugate)** na pia **opereta adjointi (adjoint operator)** ya $\hat{a}\_\pm$
>
> $$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx $$
>
> - Kutokana na hili, tunaweza kupata sifa zifuatazo:
>   - $\hat{a}\_+\hat{a}\_-\psi_n = n\psi_n$
>   - $\hat{a}\_-\hat{a}\_+\psi_n = (n+1)\psi_n$
> - Jinsi ya kukokotoa thamani za matarajio za viwango vya kimwili vinavyohusisha nguvu za $\hat{x}$ na $\hat{p}$:
>   1. Tumia fasili ya opereta za ngazi kuandika $\hat{x}$ na $\hat{p}$ kwa kutumia opereta ya kuinua na ya kushusha
>      - $\hat{x} = \sqrt{\cfrac{\hbar}{2m\omega}}\left(\hat{a}\_+ + \hat{a}\_- \right)$
>      - $\hat{p} = i\sqrt{\cfrac{\hbar m\omega}{2}}\left(\hat{a}\_+ - \hat{a}\_- \right)$
>   2. Andika kiasi cha kimwili unachotaka kupata thamani yake ya matarajio kwa kutumia fomula za juu za $\hat{x}$ na $\hat{p}$
>   3. Tumia ukweli kwamba $\left(\hat{a}\_\pm \right)^m$ ni sawia na $\psi\_{n\pm m}$, kwa hiyo ni ortogonali kwa $\psi_n$ na hivyo kuwa $0$
>   4. Tumia sifa za opereta za ngazi kufanya ukokotoaji wa kiintegrali
{: .prompt-info }

## Maarifa ya Awali
- [Mbinu ya utenganishaji wa vigeu](https://www.yunseo.kim/ko/posts/Separation-of-Variables/)
- [Mlinganyo wa Schrödinger na kazi ya mawimbi](/posts/schrodinger-equation-and-the-wave-function/)
- [Nadharia ya Ehrenfest](/posts/ehrenfest-theorem/)
- [Mlinganyo wa Schrödinger usiotegemea muda](/posts/time-independent-schrodinger-equation/)
- [Kisanduku kisicho na kikomo cha mraba cha 1D](/posts/the-infinite-square-well/)
- konjugati ya Hermite (hermitian conjugate), opereta adjointi (adjoint operator)

## Uwekaji wa modeli
### Osileta harmoniki katika mekaniki ya klasiki
Mfano wa kawaida wa osileta harmoniki ya klasiki ni mwendo wa kiwambo chenye uzani $m$ kilichoning’inizwa kwenye chemchemi yenye thamani ya konstant ya chemchemi $k$ (tunasahau msuguano).
Mwendo huu unatii **sheria ya Hooke (Hooke's law)**

$$ F = -kx = m\frac{d^2x}{dt^2} $$

Suluhisho la mlinganyo huu ni

$$ x(t) = A\sin(\omega t) + B\cos(\omega t) $$

na hapa

$$ \omega \equiv \sqrt{\frac{k}{m}} \label{eqn: angular_freq}\tag{1}$$

ni masafa ya pembe ya mtetemo. Nishati potensi kulingana na nafasi $x$ ina umbo la parabola

$$ V(x)=\frac{1}{2}kx^2 \label{eqn: potential_k}\tag{2}$$

Katika hali halisi, hakuna osileta harmoniki kamili. Hata kwa mfano huu wa chemchemi, ukiivuta kupita kiasi itazidi mpaka wa uelastiki na kukatika au kupata mgeuko wa kudumu; kwa kweli, hata kabla ya kufika hapo tayari haitafuata tena sheria ya Hooke kwa usahihi. Hata hivyo, sababu inayofanya osileta harmoniki kuwa muhimu sana katika fizikia ni kwamba potensia yoyote ya kiholela inaweza kukaribiwa kwa parabola karibu na kiwango chake cha chini cha ndani (local minimum). Tukipanua potensia yoyote $V(x)$ kwa mfululizo wa Taylor karibu na kiwango cha chini, tunapata

$$ V(x) = V(x_0) + V^\prime(x_0)(x-x_0) + \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 + \cdots $$

Sasa, kwa kuwa kuongeza konstanti yoyote kwa $V(x)$ hakuathiri kabisa nguvu, tunaweza kuondoa $V(x_0)$; na kwa kuwa $x_0$ ni kiwango cha chini, tunatumia kwamba $V^\prime(x_0)=0$; kisha chini ya dhana kwamba $(x-x_0)$ ni ndogo vya kutosha, tunapuuza viwango vya juu zaidi na kupata

$$ V(x) \approx \frac{1}{2}V^{\prime\prime}(x_0)(x-x_0)^2 $$

\* Hili linafanana na mwendo wa osileta harmoniki yenye konstant ya chemchemi inayofaa $k=V^{\prime\prime}(x_0)$ karibu na nukta $x_0$. Yaani, amplitudo ikiwa ndogo vya kutosha, mtetemo wowote unaweza kukaribiwa kama mtetemo harmoniki sahili (simple harmonic oscillation).

> \* Kwa kuwa tumedhani $V(x)$ ina kiwango cha chini katika $x_0$, hapa $V^{\prime\prime}(x_0) \geq 0$. Kwa nadra sana inaweza kutokea kwamba $V^{\prime\prime}(x_0)=0$, na katika hali hiyo mwendo huu hauwezi kukaribiwa kama mtetemo harmoniki sahili.
{: .prompt-info }

### Osileta harmoniki katika mekaniki ya kwanta
Tatizo la osileta harmoniki ya kwanta ni kutatua mlinganyo wa Schrödinger kwa potensia

$$ V(x) = \frac{1}{2}m\omega^2 x^2 \label{eqn: potential_omega}\tag{3}$$

Mlinganyo wa Schrödinger usiotegemea muda kwa osileta harmoniki ni

$$ -\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \frac{1}{2}m\omega^2x^2\psi = E\psi \label{eqn:t_independent_schrodinger_eqn}\tag{4}$$

Kuna njia mbili tofauti kabisa za kutatua tatizo hili. Moja ni njia ya kianalitiki (analytic method) inayotumia **mbinu ya mfululizo wa nguvu (power series method)**, na nyingine ni njia ya kialjebra (algebraic method) inayotumia **opereta za ngazi (ladder operators)**. Njia ya kialjebra ni ya haraka na rahisi zaidi, lakini bado ni muhimu kujifunza suluhisho la kianalitiki linalotumia mfululizo wa nguvu. Hapa tutashughulikia njia ya kialjebra, na kwa suluhisho la kianalitiki tafadhali rejea [makala hii](/posts/analytic-solution-of-the-harmonic-oscillator/).

## Komuteta na uhusiano wa ubadilishanaji kanoniki
Tukitumia opereta ya momentum $\hat{p}\equiv -i\hbar \cfrac{d}{dx}$, mlinganyo ($\ref{eqn:t_independent_schrodinger_eqn}$) unaweza kuandikwa kama ifuatavyo.

$$ \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right]\psi = E\psi. \tag{5}$$

Sasa tufanye ufaktorishaji wa Hamiltonian

$$ \hat{H} = \frac{1}{2m}\left[\hat{p}^2 + (m\omega \hat{x})^2 \right] \label{eqn:hamiltonian}\tag{6}$$

Kama $p$ na $x$ zingekuwa namba za kawaida (numbers), basi tungeweza kufanya ufaktorishaji kwa urahisi kama

$$ p^2 + (m\omega x)^2 = (ip + m\omega x)(-ip + m\omega x) $$

lakini hapa $\hat{p}$ na $\hat{x}$ ni opereta, na kwa opereta **sifa ya kubadilishana (commutative property)** kwa ujumla haitimiziwi ($\hat{p}\hat{x}\neq \hat{x}\hat{p}$), kwa hiyo si rahisi hivyo. Hata hivyo, kwa kuwa hiyo inaweza kutupa mwongozo, tuanze kwa kuangalia kiasi kifuatacho.

$$ \hat{a}_\pm \equiv \frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat{p}+m\omega\hat{x}). \label{eqn:ladder_operators}\tag{7}$$

Kwa opereta $\hat{a_\pm}$ iliyofafanuliwa hapo juu, $\hat{a}\_-\hat{a}\_+$ ni

$$ \begin{align*}
\hat{a}_-\hat{a}_+ &= \frac{1}{2\hbar m\omega}(i\hat{p}+m\omega\hat{x})(-i\hat{p}+m\omega\hat{x}) \\
&= \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 - im\omega(\hat{x}\hat{p}-\hat{p}\hat{x})\right]
\end{align*} \label{eqn:a_m_times_a_p_without_commutator}\tag{8}$$

Hapa kipengele cha $(\hat{x}\hat{p}-\hat{p}\hat{x})$ huitwa **komuteta (commutator)** ya $\hat{x}$ na $\hat{p}$, na kinaonyesha kwa kiwango gani opereta hizo mbili hazibadilishani. Kwa ujumla, komuteta ya opereta $\hat{A}$ na $\hat{B}$ huandikwa kwa mabano ya mraba kama ifuatavyo.

$$ \left[\hat{A},\hat{B} \right] \equiv \hat{A}\hat{B} - \hat{B}\hat{A}. \label{eqn:commutator}\tag{9} $$

Kwa kutumia noteshani hiyo, mlinganyo ($\ref{eqn:a_m_times_a_p_without_commutator}$) unaweza kuandikwa tena kama

$$ \hat{a}_-\hat{a}_+ = \frac{1}{2\hbar m\omega}\left[\hat{p}^2 + (m\omega x)^2 \right] - \frac{i}{2\hbar}\left[\hat{x},\hat{p} \right]. \label{eqn:a_m_times_a_p}\tag{10} $$

Sasa tunahitaji kupata komuteta ya $\hat{x}$ na $\hat{p}$.

$$ \begin{align*}
\left[\hat{x},\hat{p} \right]f(x) &= \left[x(-i\hbar)\frac{d}{dx}(f) - (-i\hbar)\frac{d}{dx}(xf) \right] \\
&= -i\hbar \left[x\frac{df}{dx} - f - x\frac{df}{dx} \right] \\
&= i\hbar f(x)
\end{align*}\tag{11}$$

na tukiondoa kazi ya majaribio $f(x)$, tunapata

$$ \left[\hat{x},\hat{p}\right] = i\hbar. \label{eqn:canonical_commutation_rel}\tag{12}$$

Huu huitwa **uhusiano wa ubadilishanaji kanoniki (canonical commutation relation)**.

## Opereta za ngazi (ladder operators)
Kutokana na uhusiano wa ubadilishanaji kanoniki, mlinganyo ($\ref{eqn:a_m_times_a_p}$) unakuwa

$$ \hat{a}_-\hat{a}_+ = \frac{1}{\hbar\omega}\hat{H} + \frac{1}{2}, \tag{13}$$

yaani

$$ \hat{H} = \hbar\omega\left(\hat{a}_-\hat{a}_+ - \frac{1}{2} \right) \tag{14} $$

Hapa mpangilio wa $\hat{a}\_-$ na $\hat{a}\_+$ ni muhimu. Tukiiweka $\hat{a}\_+$ kushoto, tunapata

$$ \hat{a}_+\hat{a}_- = \frac{1}{\hbar\omega}\hat{H} - \frac{1}{2}, \tag{15}$$

na hii hutimiza

$$ \left[\hat{a}_-,\hat{a}_+ \right] = 1 \tag{16}$$

Katika hali hiyo Hamiltonian inaweza pia kuandikwa kama

$$ \hat{H} = \hbar\omega\left(\hat{a}_+\hat{a}_- + \frac{1}{2} \right) \tag{17} $$

Kwa hiyo, tukiandika mlinganyo wa Schrödinger usiotegemea muda ($\hat{H}\psi=E\psi$) kwa kutumia $\hat{a}_\pm$, tunapata

$$ \hbar\omega \left(\hat{a}_{\pm}\hat{a}_{\mp} \pm \frac{1}{2} \right)\psi = E\psi \label{eqn:schrodinger_eqn_with_ladder}\tag{18}$$

(ishara zinazolingana huchaguliwa pamoja).

Sasa tunaweza kupata sifa muhimu ifuatayo.

$$ \hat{H}\psi = E\psi \quad \Rightarrow \quad \hat{H}\left(\hat{a}_{\pm}\psi \right)=(E \pm \hbar\omega)\left(\hat{a}_{\pm}\psi \right). $$

> Uthibitisho:
> 
> $$ \begin{align*}
> \hat{H}(\hat{a}_{+}\psi) &= \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+\frac{1}{2} \right)(\hat{a}_{+}\psi) = \hbar\omega \left(\hat{a}_{+}\hat{a}_{-}\hat{a}_{+} + \frac{1}{2}\hat{a}_{+} \right)\psi \\
&= \hbar\omega\hat{a}_{+} \left(\hat{a}_{-}\hat{a}_{+} + \frac{1}{2} \right)\psi = \hat{a}_{+}\left[\hbar\omega \left(\hat{a}_{+}\hat{a}_{-}+1+\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{+}\left(\hat{H}+\hbar\omega \right)\psi = \hat{a}_{+}(E+\hbar\omega)\psi = (E+\hbar\omega)\left(\hat{a}_{+}\psi \right). \blacksquare
> \end{align*} $$
>
> Vivyo hivyo,
>
> $$ \begin{align*}
> \hat{H}(\hat{a}_{-}\psi) &= \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-\frac{1}{2} \right)(\hat{a}_{-}\psi) = \hbar\omega \left(\hat{a}_{-}\hat{a}_{+}\hat{a}_{-} - \frac{1}{2}\hat{a}_{-} \right)\psi \\
&= \hbar\omega\hat{a}_{-} \left(\hat{a}_{+}\hat{a}_{-} - \frac{1}{2} \right)\psi = \hat{a}_{-}\left[\hbar\omega \left(\hat{a}_{-}\hat{a}_{+}-1-\frac{1}{2} \right)\psi \right] \\
&= \hat{a}_{-}\left(\hat{H}-\hbar\omega \right)\psi = \hat{a}_{-}(E-\hbar\omega)\psi = (E-\hbar\omega)\left(\hat{a}_{-}\psi \right). \blacksquare
> \end{align*} $$
{: .prompt-info }

Kwa hiyo, ukipata suluhisho moja la mlinganyo wa Schrödinger usiotegemea muda, unaweza kupata suluhisho nyingine zote. Kwa kuwa kwa hali tuli yoyote tunaweza kuinua au kushusha kiwango chake cha nishati, $\hat{a}\_\pm$ huitwa **opereta za ngazi (ladder operators)**; $\hat{a}\_+$ ni **opereta ya kuinua (raising operator)** na $\hat{a}\_-$ ni **opereta ya kushusha (lowering operator)**.

## Hali tuli za osileta harmoniki
### Hali tuli $\psi_n$ na viwango vya nishati $E_n$
Ukiendelea kutumia opereta ya kushusha, mwishowe utapata hali yenye nishati ndogo kuliko $0$, na hali kama hiyo haiwezi kuwepo kimwili. Kihisabati, kama $\psi$ ni suluhisho la mlinganyo wa Schrödinger basi $\hat{a}_-\psi$ pia ni suluhisho la mlinganyo wa Schrödinger, lakini hakuna hakikisho kwamba suluhisho hili jipya daima litakuwa limenormishwa (yaani, hali inayowezekana kimwili). Ukiendelea kutumia opereta ya kushusha, mwishowe utapata suluhisho trivi $\psi=0$.

Kwa hiyo, kwa hali tuli $\psi$ ya osileta harmoniki, kuna “ngazi ya chini kabisa” $\psi_0$ inayotimiza

$$ \hat{a}_-\psi_0 = 0 \tag{19}$$

(yaani hakuna kiwango cha nishati cha chini zaidi kinachoweza kuwepo). $\psi_0$ hii hutimiza

$$ \frac{1}{\sqrt{2\hbar m\omega}}\left(\hbar\frac{d}{dx} + m\omega x \right)\psi_0 = 0 $$

hivyo,

$$ \frac{d\psi_0}{dx} = -\frac{m\omega}{\hbar}x\psi_0 $$

Huu ni [mlinganyo wa kawaida wa diferenshali unaotenganishika](/posts/Separation-of-Variables/), kwa hiyo unaweza kutatuliwa kwa urahisi kama ifuatavyo.

$$ \begin{gather*}
\int \frac{d\psi_0}{\psi_0} = -\frac{m\omega}{\hbar}\int x\ dx \\
\ln\psi_0 = -\frac{m\omega}{2\hbar}x^2 + C
\end{gather*}$$

$$ \therefore \psi_0(x) = Ae^{-\frac{m\omega}{2\hbar}x^2}. $$

Zaidi ya hayo, kazi hii inaweza kunormishwa kama ifuatavyo.

$$ 1 = |A|^2 \int_\infty^\infty e^{-m\omega x^2/\hbar} dx = |A|^2\sqrt{\frac{\pi\hbar}{m\omega}}. $$

Hapa $A^2 = \sqrt{m\omega / \pi\hbar}$, kwa hiyo

$$ \psi_0(x) = \left(\frac{m\omega}{\pi\hbar} \right)^{1/4}e^{-\frac{m\omega}{2\hbar}x^2} $$

Sasa tukiweka suluhisho hili katika mlinganyo wa Schrödinger ($\ref{eqn:schrodinger_eqn_with_ladder}$) uliopatikana hapo juu, na tukitumia kwamba $\hat{a}_-\psi_0=0$, tunapata

$$ E_0 = \frac{1}{2}\hbar\omega \label{eqn:E_ground}\tag{20}$$

Kuanzia kwenye **hali ya msingi (ground state)** hii, tukitumia tena na tena opereta ya kuinua, tunapata **hali zilizochochewa (excited states)** ambazo nishati yake huongezeka kwa $\hbar\omega$ kila opereta ya kuinua inapofanya kazi mara moja.

$$ \psi_n(x) = A_n(\hat{a}_+)^n \psi_0(x),\quad E_n = \left(n + \frac{1}{2} \right)\hbar\omega \label{eqn:psi_n_and_E_n}\tag{21}$$

Hapa $A_n$ ni konstanti ya kunormisha. Kwa njia hii, baada ya kujua hali ya msingi, tunaweza kutumia opereta ya kuinua kuamua hali zote tuli za osileta harmoniki pamoja na viwango vyake vyote vya nishati vinavyoruhusiwa.

### Unormishaji
Konstanti ya unormishaji pia inaweza kupatikana kwa njia ya kialjebra. Tunajua kwamba $\hat{a}\_{\pm}\psi_n$ ni sawia na $\psi\_{n\pm 1}$, kwa hiyo tunaweza kuandika

$$ \hat{a}_+\psi_n = c_n\psi_{n+1}, \quad \hat{a}_-\psi_n = d_n\psi_{n-1} \label{eqn:norm_const}\tag{22}$$

Sasa zingatia kwamba kwa kazi zozote mbili zinazoweza kuunganishwa $f(x)$ na $g(x)$, yafuatayo hutimia.

$$ \int_{-\infty}^{\infty} f^*(\hat{a}_\pm g)dx = \int_{-\infty}^{\infty} (\hat{a}_\mp f)^* g\ dx. \label{eqn:hermitian_conjugate}\tag{23}$$

$\hat{a}\_\mp$ ni **konjugati ya Hermite (hermitian conjugate)** na pia **opereta adjointi (adjoint operator)** ya $\hat{a}\_\pm$.

> **Uthibitisho:**
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

Kwa hiyo, tukiweka $f=\hat{a}_\pm \psi_n$, $g=\psi_n$, tunapata

$$ \int_{-\infty}^{\infty} \left(\hat{a}_\pm \psi_n \right)^*\left(\hat{a}_\pm \psi_n \right)\ dx = \int_{-\infty}^{\infty} \left( \hat{a}_\mp\hat{a}_\pm \psi_n \right)^* \psi_n\ dx $$

Basi kutoka kwa mlinganyo ($\ref{eqn:schrodinger_eqn_with_ladder}$) na ($\ref{eqn:psi_n_and_E_n}$),

$$ \begin{gather*}
\hat{a}_+\hat{a}_-\psi_n = \left(\frac{E}{\hbar\omega} - \frac{1}{2}\right)\psi_n = n\psi_n, \\
\hat{a}_-\hat{a}_+\psi_n = \left(\frac{E}{\hbar\omega} + \frac{1}{2}\right)\psi_n = (n+1)\psi_n
\end{gather*} \label{eqn:norm_const_2}\tag{24}$$

kwa hiyo, kutoka kwa mlinganyo ($\ref{eqn:norm_const}$) na ($\ref{eqn:norm_const_2}$), tunapata yafuatayo.

$$ \begin{align*}
\int_{-\infty}^{\infty} \left(\hat{a}_+\psi_n \right)^* \left(\hat{a}_+\psi_n \right) &= |c_n|^2 \int |\psi_{n+1}|^2 dx = (n+1)\int |\psi_n|^2 dx,\\
\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_n \right)^* \left(\hat{a}_-\psi_n \right) &= |d_n|^2 \int |\psi_{n-1}|^2 dx = n\int |\psi_n|^2 dx.
\end{align*} \label{eqn:norm_const_3}\tag{25}$$

Na kwa kuwa hapa $\psi_n$ na $\psi_{n\pm1}$ zote zimenormishwa, tuna $\|c_n\|^2=n+1,\ \|d_n\|^2=n$, na hivyo

$$ \hat{a}_+\psi_n = \sqrt{n+1}\psi_{n+1}, \quad \hat{a}_-\psi_n = \sqrt{n}\psi_{n-1} \label{eqn:norm_const_4}\tag{26}$$

Kutokana na hili, hali tuli yoyote iliyonormishwa $\psi_n$ inaweza kupatikana kama ifuatavyo.

$$ \psi_n = \frac{1}{\sqrt{n!}}\left(\hat{a}_+ \right)^n \psi_0. \tag{27}$$

Yaani, katika mlinganyo ($\ref{eqn:psi_n_and_E_n}$), konstanti ya unormishaji ni $A_n=\cfrac{1}{\sqrt{n!}}$.

### Uorthogonali wa hali tuli
Kama ilivyo kwa [kisanduku kisicho na kikomo cha mraba cha 1D](/posts/the-infinite-square-well/#3-hali-hizi-zina-sifa-ya-orthogonality), hali tuli za osileta harmoniki ni ortogonali.

$$ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = \delta_{mn}. \tag{28}$$

#### Uthibitisho
Hili linaweza kuthibitishwa kwa kutumia mlinganyo ($\ref{eqn:hermitian_conjugate}$), ($\ref{eqn:norm_const_2}$), na ($\ref{eqn:norm_const_3}$) tulizoonyesha hapo awali. Katika mlinganyo ($\ref{eqn:hermitian_conjugate}$), tukiweka $f=\hat{a}_-\psi_m,\ g=\psi_n$, tunatumia kwamba

$$\int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^*\left(\hat{a}_-\psi_n \right)\ dx = \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx$$

$$ \begin{align*}
n\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx &= \int_{-\infty}^{\infty} \psi_m^* \left(\hat{a}_+\hat{a}_- \right)\psi_n\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_-\psi_m \right)^* \left(\hat{a}_-\psi_n \right)\ dx \\
&= \int_{-\infty}^{\infty} \left(\hat{a}_+\hat{a}_-\psi_m \right)^*\psi_n\ dx \\
&= m\int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx.
\end{align*} $$

$$ \therefore \ (m \neq n) \ \Rightarrow \ \int_{-\infty}^{\infty} \psi_m^*\psi_n\ dx = 0.\ \blacksquare $$

Kwa kutumia uorthogonali, [kama tulivyofanya katika fomula (19) ya kisanduku kisicho na kikomo cha mraba cha 1D](/posts/the-infinite-square-well/#kupata-suluhisho-la-jumla-la-mlinganyo-wa-schrodinger-unaotegemea-muda-psixt), tunapopanua $\Psi(x,0)$ kama mchanganyiko wa mstari wa hali tuli $\sum c_n\psi_n(x)$, migawo $c_n$ inaweza kupatikana kwa [mbinu ya Fourier](/posts/the-infinite-square-well/#kupata-mgawo-c_n-kwa-kutumia-mbinu-ya-fourier-fouriers-trick).

$$ c_n = \int \psi_n^*\Psi(x,0)\ dx. $$

Hapa pia, $\|c_n\|^2$ ni uwezekano wa kupata thamani ya $E_n$ unapopima nishati.

## Thamani ya matarajio ya nishati potensi $\langle V \rangle$ katika hali tuli yoyote $\psi_n$
Ili kupata $\langle V \rangle$, tunahitaji kukokotoa kiintegrali kifuatacho.

$$ \langle V \rangle = \left\langle \frac{1}{2}m\omega^2x^2 \right\rangle = \frac{1}{2}m\omega^2\int_{-\infty}^{\infty}\psi_n^*x^2\psi_n\ dx. $$

Wakati wa kukokotoa integrali za aina hii zinazohusisha nguvu za $\hat{x}$ na $\hat{p}$, njia ifuatayo huwa muhimu.

Kwanza, kwa kutumia fasili ya opereta za ngazi katika mlinganyo ($\ref{eqn:ladder_operators}$), tunaandika $\hat{x}$ na $\hat{p}$ kwa kutumia opereta ya kuinua na ya kushusha.

$$ \hat{x} = \sqrt{\frac{\hbar}{2m\omega}}\left(\hat{a}_+ + \hat{a}_- \right); \quad \hat{p} = i\sqrt{\frac{\hbar m\omega}{2}}\left(\hat{a}_+ - \hat{a}_- \right). $$

Sasa tunaandika kiasi cha kimwili tunachotaka kupata thamani ya matarajio kwa kutumia fomula za juu za $\hat{x}$ na $\hat{p}$. Hapa tunavutiwa na $x^2$, kwa hiyo tunaweza kuandika

$$ x^2 = \frac{\hbar}{2m\omega}\left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right] $$

Kutokana na hili, tunapata

$$ \langle V \rangle = \frac{\hbar\omega}{4}\int_{-\infty}^{\infty} \psi_n^* \left[\left(\hat{a}_+ \right)^2 + \left(\hat{a}_+\hat{a}_- \right) + \left(\hat{a}_-\hat{a}_+ \right) + \left(\hat{a}_- \right)^2 \right]\psi_n\ dx. $$

Na hapa $\left(\hat{a}\_\pm \right)^2$ ni sawia na $\psi\_{n\pm2}$, kwa hiyo ni ortogonali kwa $\psi\_n$; hivyo vipengele hivi viwili, $\left(\hat{a}\_+ \right)^2$ na $\left(\hat{a}\_- \right)^2$, vinakuwa $0$. Mwishowe, tukitumia mlinganyo ($\ref{eqn:norm_const_2}$) kukokotoa vipengele viwili vilivyobaki, tunapata

$$ \langle V \rangle = \frac{\hbar\omega}{4}\{n+(n+1)\} = \frac{1}{2}\hbar\omega\left(n+\frac{1}{2} \right) $$

Ukiangalia mlinganyo ($\ref{eqn:psi_n_and_E_n}$), utaona kwamba thamani ya matarajio ya nishati potensi ni nusu kamili ya nishati yote, na nusu iliyobaki bila shaka ni nishati ya mwendo $T$. Hii ni sifa mahsusi ya osileta harmoniki.
