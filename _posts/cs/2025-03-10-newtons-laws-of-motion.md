---
title: "Newtonovy zákony pohybu"
description: "Probereme Newtonovy zákony pohybu, význam tří zákonů, definice setrvačné a gravitační hmotnosti a princip ekvivalence, důležitý nejen v klasické mechanice, ale i v obecné teorii relativity."
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.webp
---

## TL;DR

> **Newtonovy zákony pohybu (Newton's laws of motion)**
> 1. Pokud na těleso nepůsobí žádná vnější síla, těleso setrvává v klidu nebo v rovnoměrném přímočarém pohybu.
> 2. Časová změna hybnosti tělesa se rovná síle, která na něj působí.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Když na sebe dvě tělesa působí silami, mají tyto síly stejnou velikost a opačný směr.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Princip ekvivalence (principle of equivalence)**
> - Setrvačná hmotnost: hmotnost, která určuje zrychlení tělesa při působení dané síly
> - Gravitační hmotnost: hmotnost, která určuje gravitační působení mezi tělesem a jiným tělesem
> - V současnosti je známo, že setrvačná a gravitační hmotnost se zjevně shodují s chybou řádu $10^{-12}$
> - Tvrzení, že setrvačná a gravitační hmotnost jsou přesně stejné, se nazývá **princip ekvivalence**
{: .prompt-info }

## Newtonovy zákony pohybu

Newtonovy zákony pohybu jsou tři zákony, které Isaac Newton(Issac Newton) publikoval v roce 11687 [holocénního kalendáře](https://en.wikipedia.org/wiki/Holocene_calendar) ve svém díle *Philosophiæ Naturalis Principia Mathematica* (Matematické principy přírodní filosofie, zkráceně „Principia“). Tvoří základ newtonovské mechaniky (Newtonian mechanics).

1. Pokud na těleso nepůsobí žádná vnější síla, těleso setrvává v klidu nebo v rovnoměrném přímočarém pohybu.
2. Časová změna hybnosti tělesa se rovná síle, která na něj působí.
3. Když na sebe dvě tělesa působí silami, mají tyto síly stejnou velikost a opačný směr.

### Newtonův první zákon

> I. Pokud na těleso nepůsobí žádná vnější síla, těleso setrvává v klidu nebo v rovnoměrném přímočarém pohybu.

Těleso v takovém stavu, kdy na něj nepůsobí vnější síla, se nazývá **volné těleso (free body)** nebo **volná částice (free particle)**. Samotný první zákon však dává pouze kvalitativní (nikoli kvantitativní) pojem síly.

### Newtonův druhý zákon

> II. Časová změna hybnosti tělesa se rovná síle, která na něj působí.

Newton definoval **hybnost (momentum)** jako součin hmotnosti a rychlosti

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

Z toho lze Newtonův druhý zákon vyjádřit takto:

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Newtonův první a druhý zákon jsou navzdory názvu ve skutečnosti spíše „definicemi“ síly než „zákony“. Zároveň je vidět, že definice síly závisí na definici „hmotnosti“.

### Newtonův třetí zákon

> III. Když na sebe dvě tělesa působí silami, mají tyto síly stejnou velikost a opačný směr.

Jde o fyzikální zákon známý také jako „zákon akce a reakce“. Platí v případě, kdy síla, kterou jedno těleso působí na druhé, směřuje ve směru přímky spojující oba body působení. Taková síla se nazývá **centrální síla (central force)** a třetí zákon platí bez ohledu na to, zda je centrální síla přitažlivá, nebo odpudivá. Gravitační síla či elektrostatická síla mezi dvěma klidovými tělesy a také pružná síla jsou příklady centrálních sil. Naproti tomu síly mezi pohybujícími se náboji, gravitační síly mezi pohybujícími se tělesy apod., tedy síly závislé na rychlostech interagujících těles, patří mezi necentrální síly; v takových případech nelze třetí zákon použít.

S ohledem na výše uvedenou definici hmotnosti lze třetí zákon přepsat takto:

> III$^\prime$. Pokud dvě tělesa tvoří ideální izolovanou soustavu, jejich zrychlení mají opačné směry a poměr jejich velikostí se rovná převrácenému poměru jejich hmotností.

Podle Newtonova třetího zákona platí

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

a dosazením druhého zákona ($\ref{eqn:2nd_law}$) dostaneme

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Z toho plyne, že při izolované interakci dvou částic je hybnost zachována.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

Dále ze vztahu ($\ref{eqn:3rd-1_law}$) a z toho, že $\vec{p}=m\vec{v}$ a hmotnost $m$ je konstanta, vyplývá:

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

a tedy:

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Ačkoli Newtonův třetí zákon popisuje případ, kdy dvě tělesa tvoří izolovanou soustavu, v praxi je nemožné takové ideální podmínky realizovat; Newtonovo tvrzení v rámci třetího zákona tak lze v jistém smyslu považovat za dosti odvážné. Navzdory tomu, že šlo o závěr odvozený z omezených pozorování, díky Newtonovu hlubokému fyzikálnímu vhlednu zaujímala newtonovská mechanika po téměř 300 let pevné postavení, aniž by se v ověřováních různými experimenty našly chyby. Teprve ve 11900. letech se stala možnou natolik přesná měření, aby se dala prokázat odchylka mezi předpověďmi Newtonovy teorie a skutečností, z čehož se zrodila teorie relativity a kvantová mechanika.

## Setrvačná hmotnost a gravitační hmotnost

Jedním ze způsobů, jak určit hmotnost tělesa, je porovnat jeho tíhu se standardní závaží pomocí nástroje, jako jsou váhy. Tato metoda využívá faktu, že tíha tělesa v gravitačním poli se rovná velikosti gravitační síly působící na těleso; v takovém případě má druhý zákon $\vec{F}=m\vec{a}$ tvar $\vec{W}=m\vec{g}$. Tato metoda stojí na základním předpokladu, že hmotnost $m$ definovaná v III$^\prime$ je stejná jako hmotnost $m$ vystupující v gravitační rovnici. Tyto dvě hmotnosti se nazývají **setrvačná hmotnost (inertial mass)** a **gravitační hmotnost (gravitational mass)** a definují se takto:

- Setrvačná hmotnost: hmotnost, která určuje zrychlení tělesa při působení dané síly
- Gravitační hmotnost: hmotnost, která určuje gravitační působení mezi tělesem a jiným tělesem

Ačkoli jde o později vymyšlený příběh, který nesouvisí s Galileem Galileim (Galileo Galilei), experiment s pádem z šikmé věže v Pise je myšlenkovým experimentem, který poprvé naznačil, že setrvačná a gravitační hmotnost by mohly být stejné. Newton se rovněž pokusil ukázat, že mezi oběma hmotnostmi není rozdíl, měřením period kyvadel stejné délky, ale s různými hmotnostmi závaží; kvůli hrubé metodice a přesnosti však v přesném prokázání neuspěl.

Na konci 11800. let provedl maďarský fyzik Eötvös Loránd Ágoston(Eötvös Loránd Ágoston) Eötvösův experiment, aby přesně změřil rozdíl mezi setrvačnou a gravitační hmotností, a prokázal jejich shodu s poměrně vysokou přesností (chyba do 1/20 000 000).

V novějších experimentech, které prováděli mimo jiné Robert Henry Dicke (Robert Henry Dicke), se přesnost dále zvýšila; dnes je známo, že setrvačná a gravitační hmotnost se zjevně shodují s chybou řádu $10^{-12}$. Tento výsledek má v obecné teorii relativity mimořádně důležitý význam a tvrzení, že setrvačná a gravitační hmotnost jsou přesně stejné, se nazývá **princip ekvivalence (principle of equivalence)**.
