---
title: Teoremu ya Ehrenfest (Ehrenfest theorem)
description: Katika mekanika ya kwanta, tunaangalia jinsi ya kupata thamani za matarajio za nafasi na msukumo kutoka kwa kazi ya wimbi, kisha tunapanua hilo hadi kwenye fomula ya kukokotoa thamani ya matarajio ya kigeu chochote cha kimitambo Q(x,p). Kutokana na hilo, tunatoa teoremu ya Ehrenfest.
categories: [Physics, Modern Physics]
tags: [Quantum Mechanics, Schrödinger Equation, Wave Function]
math: true
image: /assets/img/schrodinger-cat-cropped.webp
---
## TL;DR
> - $$ \hat x \equiv x,\ \hat p \equiv -i\hbar\nabla$$
> - $$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx $$
> - $$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} $$
> - $$ \frac{d\langle p \rangle}{dt} = \left\langle -\frac{\partial V}{\partial x} \right\rangle $$
{: .prompt-info }

## Yanayohitajika kabla
- Mgawanyo endelevu wa uwezekano na msongamano wa uwezekano
- [Mlinganyo wa Schrödinger na kazi ya wimbi](/posts/schrodinger-equation-and-the-wave-function/)

## Kukokotoa thamani ya matarajio kutoka kwa kazi ya wimbi
### Thamani ya matarajio ya nafasi $x$
Thamani ya matarajio (expectation value) ya nafasi $x$ kwa chembe iliyo katika hali ya $\Psi$ ni

$$ \langle x \rangle = \int_{-\infty}^{\infty}x|\Psi(x,t)|^2 dx \label{eqn:x_exp}\tag{1}$$

ni. Tukipima nafasi za chembe nyingi vya kutosha zilizo katika hali ileile $\Psi$ na kisha kuchukua wastani wa matokeo ya vipimo hivyo, tutapata $\langle x \rangle$ iliyokokotolewa kwa kutumia fomula hapo juu.

> Kumbuka kwamba thamani ya matarajio inayozungumziwa hapa si wastani unaopatikana kwa kumpima chembe moja mara kwa mara, bali ni wastani wa matokeo ya vipimo kwa **mkusanyiko wa mifumo (ensemble)** yenye hali ileile. Ikiwa chembe ileile itapimwa mara nyingi kwa vipindi vifupi vya muda, katika kipimo cha kwanza [kazi ya wimbi huanguka (collapse)](/posts/schrodinger-equation-and-the-wave-function/#kipimo-na-kuanguka-kwa-kazi-ya-wimbi), kwa hiyo vipimo vinavyofuata vitatoa thamani ileile tu.
{: .prompt-warning }

### Thamani ya matarajio ya msukumo $p$
Kwa kuwa $\Psi$ hutegemea muda, $\langle x \rangle$ itabadilika kadiri muda unavyopita. Hapa, kutokana na mlinganyo (8) wa [Mlinganyo wa Schrödinger na kazi ya wimbi](/posts/schrodinger-equation-and-the-wave-function/) pamoja na mlinganyo hapo juu ($\ref{eqn:x_exp}$), yafuatayo yanashikamana.

$$ \begin{align*}
\frac{d\langle x \rangle}{dt} &= \int_{-\infty}^{\infty} x\frac{\partial}{\partial t}|\Psi|^2 dx \\
&= \frac{i\hbar}{2m}\int_{-\infty}^{\infty} x\frac{\partial}{\partial x}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_1}\tag{2}\\
&= \frac{i\hbar}{2m}\left[x\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)\Bigg|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \right]\\
&= -\frac{i\hbar}{2m}\int_{-\infty}^{\infty}\left(\Psi^*\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^*}{\partial x}\Psi \right)dx \label{eqn:dx/dt_2}\tag{3}\\
&= -\frac{i\hbar}{2m}\left[\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx-\left(\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\Psi^*\frac{\partial\Psi}{\partial x}dx \right) \right] \\
&= -\frac{i\hbar}{m}\int_{-\infty}^{\infty} \Psi^*\frac{\partial\Psi}{\partial x}dx. \label{eqn:dx/dt_3}\tag{4}
\end{align*} $$

> Katika hatua kutoka mlinganyo ($\ref{eqn:dx/dt_1}$) hadi ($\ref{eqn:dx/dt_2}$) na kutoka ($\ref{eqn:dx/dt_2}$) hadi ($\ref{eqn:dx/dt_3}$), ujumuishaji kwa sehemu ulitumika mara mbili, na kwa kuwa $\lim_{x\rightarrow\pm\infty}\Psi=0$, neno la mpakani (boundary term) liliondolewa.
{: .prompt-tip }

Kwa hiyo, thamani ya matarajio ya **msukumo** hupatikana kama ifuatavyo.

$$ \langle p \rangle = m\frac{d\langle x \rangle}{dt} = -i\hbar\int\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)dx. \label{eqn:p_exp}\tag{5} $$

### Thamani ya matarajio kwa kiasi chochote cha kimwili $Q(x,p)$
Misemo ya $\langle x \rangle$ na $\langle p \rangle$ tuliyopata hapo juu inaweza kuandikwa katika umbo lifuatalo.

$$ \begin{gather*}
\langle x \rangle = \int\Psi^*[x]\Psi dx \label{eqn:x_op}\tag{6},\\
\langle p \rangle = \int\Psi^*[-i\hbar(\partial/\partial x)]\Psi dx \label{eqn:p_op}\tag{7}.
\end{gather*} $$

Oparesheni $\hat x \equiv x$ huwakilisha nafasi, na oparesheni $\hat p \equiv -i\hbar(\partial/\partial x)$ huwakilisha msukumo. Kwa oparesheni ya msukumo $\hat p$, tukipanua hadi katika nafasi ya vipimo vitatu, tunaweza kufafanua $\hat p \equiv -i\hbar\nabla$.

Kwa kuwa kila kigeu cha mekanika ya klasiki kinaweza kuandikwa kwa nafasi na msukumo, tunaweza kupanua hili hadi kwenye thamani ya matarajio ya kiasi chochote cha kimwili. Ili kukokotoa thamani ya matarajio ya kiasi cha kiholela $Q(x,p)$, badilisha kila $p$ kuwa $-i\hbar\nabla$, kisha weka oparesheni inayopatikana kati ya $\Psi^\*$ na $\Psi$ na ufanye ujumuishaji.

$$ \langle Q(x,p) \rangle = \int \Psi^*[Q(x, -i\hbar\nabla)]\Psi dx. \label{eqn:Q_exp}\tag{8}$$

Kwa mfano, kwa kuwa nishati ya mwendo ni $T=\cfrac{p^2}{2m}$,

$$ \langle T \rangle = \frac{\langle p^2 \rangle}{2m} = -\frac{\hbar^2}{2m}\int\Psi^*\frac{\partial^2\Psi}{\partial x^2}dx \label{eqn:T_exp}\tag{9}$$

ni.

Kupitia mlinganyo ($\ref{eqn:Q_exp}$), tunaweza kukokotoa thamani ya matarajio ya kiasi chochote cha kimwili kwa chembe iliyo katika hali ya $\Psi$.

## Teoremu ya Ehrenfest (Ehrenfest theorem)
### Kukokotoa $d\langle p \rangle/dt$
Tuchukue tofauti kwa muda $t$ ya pande zote mbili za mlinganyo ($\ref{eqn:p_op}$) ili kupata tofauti ya wakati ya thamani ya matarajio ya msukumo, $\cfrac{d\langle p \rangle}{dt}$.

$$ \begin{align*}
\frac{d\langle p \rangle}{dt} &= -i\hbar\frac{d}{dt}\int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\Psi dx \tag{10}\\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}\Psi^*\frac{\partial}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{11} \\
&= -i\hbar\left(\int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx - \int_{-\infty}^{\infty}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \right) \tag{12}\\
&= \int_{-\infty}^{\infty}-i\hbar\frac{\partial \Psi^*}{\partial t}\frac{\partial}{\partial x}\Psi dx + \int_{-\infty}^{\infty}i\hbar\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial t}dx \label{eqn:dp/dt_1}\tag{13}\\
&= \int_{-\infty}^{\infty}\left[\left(-\frac{\hbar^2}{2m}\frac{\partial^2\Psi^*}{\partial x^2}+V\Psi^*\right)\frac{\partial \Psi}{\partial x}+\frac{\partial \Psi^*}{\partial x}\left(-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi \right)\right]dx \label{eqn:dp/dt_2}\tag{14}\\
&= -\frac{\hbar^2}{2m}\int_{-\infty}^{\infty}\frac{\partial}{\partial x}\left(\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\right)dx + \int_{-\infty}^{\infty}V\frac{\partial}{\partial x}(\Psi^*\Psi)dx \label{eqn:dp/dt_3}\tag{15}\\
&= -\frac{\hbar^2}{2m}\frac{\partial \Psi^*}{\partial x}\frac{\partial \Psi}{\partial x}\Biggr|^{\infty}_{-\infty} + V\Psi^*\Psi\biggr|^{\infty}_{-\infty}-\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \\
&= -\int_{-\infty}^{\infty}\frac{\partial V}{\partial x}\Psi^*\Psi dx \label{eqn:dp/dt_4}\tag{16}\\
&= -\left\langle \frac{\partial V}{\partial x} \right\rangle.
\end{align*} $$

> Mlinganyo ($\ref{eqn:dp/dt_2}$) unaweza kupatikana kwa kuweka mlinganyo (6) na (7) kutoka [Mlinganyo wa Schrödinger na kazi ya wimbi](/posts/schrodinger-equation-and-the-wave-function/) ndani ya mlinganyo ($\ref{eqn:dp/dt_1}$). Katika hatua kutoka mlinganyo ($\ref{eqn:dp/dt_3}$) hadi ($\ref{eqn:dp/dt_4}$), ujumuishaji kwa sehemu ulitumika, na kama hapo awali, kwa kuwa $\lim_{x\rightarrow\pm\infty}\Psi=0$, neno la mpakani (boundary term) liliondolewa.
{: .prompt-tip }

$$ \therefore \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle. \label{eqn:ehrenfest_theorem_2nd}\tag{17}$$

### Uhusiano kati ya teoremu ya Ehrenfest na sheria ya pili ya Newton ya mwendo
Milinganyo miwili ifuatayo tuliyopata hapo juu huitwa teoremu ya Ehrenfest (Ehrenfest theorem).

$$ \begin{gather*}
\langle p \rangle = m\frac{d\langle x \rangle}{dt} \\
\frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle 
\end{gather*} \label{eqn:ehrenfest_theorem}\tag{18}$$

Teoremu ya Ehrenfest ina umbo linalofanana sana na uhusiano kati ya nishati ya potensheli na nguvu ya kihafidhina katika mekanika ya klasiki, $F=\cfrac{dp}{dt}=-\nabla V$.  
Tukiweka milinganyo hiyo miwili sambamba kwa kulinganisha, tunapata yafuatayo.

- $$ \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V(x)}{\partial x} \right\rangle \text{ [Ehrenfest Theorem]} $$
- $$ \frac{d\langle p \rangle}{dt} = -\frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} \text{ [Newton's Second Law of Motion]}$$

Tukipanua upande wa kulia wa mlinganyo wa pili wa teoremu ya Ehrenfest, $\cfrac{d\langle p \rangle}{dt} = -\left\langle \cfrac{\partial V(x)}{\partial x} \right\rangle$ (mlinganyo [$\ref{eqn:ehrenfest_theorem_2nd}$]), kwa mfululizo wa Taylor kwa $x$ karibu na $\langle x \rangle$, tunapata

$$ \frac{\partial V(x)}{\partial x} = \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} + \frac{\partial^2 V(\langle x \rangle)}{\partial \langle x \rangle^2}(x-\langle x \rangle) + \frac{\partial^3 V(\langle x \rangle)}{\partial \langle x \rangle^3}(x-\langle x \rangle)^2 + \cdots $$

ni. Hapa, ikiwa $x-\langle x \rangle$ ni ndogo vya kutosha, tunaweza kupuuza viteremu vyote vya daraja la juu isipokuwa kile cha kwanza, na kukadiria kwamba

$$ \frac{\partial V(x)}{\partial x} \approx \frac{\partial V(\langle x \rangle)}{\partial \langle x \rangle} $$

yaani.

Kwa maneno mengine, **ikiwa kazi ya wimbi ya chembe fulani ina umbo kali lililojikusanya karibu sana na nukta moja katika nafasi (ikiwa mtawanyiko wa $\|\Psi\|^2$ kwa $x$ ni mdogo sana), basi teoremu ya Ehrenfest inaweza kukadiriwa na sheria ya pili ya Newton ya mwendo katika mekanika ya klasiki.** Katika mizani ya makroskopiki, kiwango ambacho kazi ya wimbi imesambaa katika nafasi kinaweza kupuuzwa na nafasi ya chembe kuchukuliwa kivitendo kama nukta moja, hivyo sheria ya pili ya Newton ya mwendo hutimia. Lakini katika mizani ya mikroskopiki, athari za kwanta haziwezi kupuuzwa, kwa hiyo sheria ya pili ya Newton ya mwendo haitimizi tena, na teoremu ya Ehrenfest ndiyo inayopaswa kutumika.
