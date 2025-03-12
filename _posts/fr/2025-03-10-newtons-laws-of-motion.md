---
title: Les lois du mouvement de Newton
description: Examinons les lois du mouvement de Newton, la signification de ces trois lois, les définitions de la masse inertielle et de la masse gravitationnelle, ainsi que le principe d'équivalence, qui a une importance significative non seulement en mécanique classique mais aussi dans la théorie de la relativité générale ultérieure.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Les lois du mouvement de Newton**
> 1. Tout corps persévère dans l'état de repos ou de mouvement uniforme en ligne droite dans lequel il se trouve, à moins que quelque force n'agisse sur lui, et ne le contraigne à changer d'état.
> 2. Le changement de mouvement est proportionnel à la force motrice imprimée, et il se fait suivant la ligne droite dans laquelle cette force a été imprimée.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. L'action est toujours égale et opposée à la réaction ; c'est-à-dire que les actions de deux corps l'un sur l'autre sont toujours égales et dans des directions contraires.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Le principe d'équivalence**
> - Masse inertielle : la masse qui détermine l'accélération d'un corps soumis à une force donnée
> - Masse gravitationnelle : la masse qui détermine la force gravitationnelle entre un corps et un autre
> - Il est actuellement connu que la masse inertielle et la masse gravitationnelle sont clairement identiques avec une marge d'erreur de l'ordre de $10^{-12}$
> - L'affirmation selon laquelle la masse inertielle et la masse gravitationnelle sont exactement égales est appelée le **principe d'équivalence**
{: .prompt-info }

## Les lois du mouvement de Newton
Les lois du mouvement de Newton sont trois lois publiées par Isaac Newton en 1687 dans son ouvrage Philosophiæ Naturalis Principia Mathematica (Principes mathématiques de la philosophie naturelle, abrégé en 'Principia'), qui forment la base de la mécanique newtonienne.

1. Tout corps persévère dans l'état de repos ou de mouvement uniforme en ligne droite dans lequel il se trouve, à moins que quelque force n'agisse sur lui, et ne le contraigne à changer d'état.
2. Le changement de mouvement est proportionnel à la force motrice imprimée, et il se fait suivant la ligne droite dans laquelle cette force a été imprimée.
3. L'action est toujours égale et opposée à la réaction ; c'est-à-dire que les actions de deux corps l'un sur l'autre sont toujours égales et dans des directions contraires.

### Première loi de Newton
> I. Tout corps persévère dans l'état de repos ou de mouvement uniforme en ligne droite dans lequel il se trouve, à moins que quelque force n'agisse sur lui, et ne le contraigne à changer d'état.

Un corps dans cet état, sans force extérieure agissant sur lui, est appelé un **corps libre** ou une **particule libre**.
Cependant, la première loi seule ne donne qu'un concept qualitatif de la force.

### Deuxième loi de Newton
> II. Le changement de mouvement est proportionnel à la force motrice imprimée, et il se fait suivant la ligne droite dans laquelle cette force a été imprimée.

Newton a défini la **quantité de mouvement (momentum)** comme le produit de la masse et de la vitesse

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

À partir de cela, la deuxième loi de Newton peut être exprimée comme suit :

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Les première et deuxième lois de Newton, malgré leur nom, sont en réalité plus proches d'une 'définition' de la force que d'une 'loi'. On peut également voir que la définition de la force dépend de la définition de la 'masse'.

### Troisième loi de Newton
> III. L'action est toujours égale et opposée à la réaction ; c'est-à-dire que les actions de deux corps l'un sur l'autre sont toujours égales et dans des directions contraires.

Cette loi physique est également connue sous le nom de 'loi de l'action et de la réaction', et s'applique lorsque la force qu'un corps exerce sur un autre est dirigée le long de la ligne droite reliant les deux points d'action. Une telle force est appelée **force centrale**, et la troisième loi s'applique que la force centrale soit attractive ou répulsive. La gravité ou la force électrostatique entre deux corps au repos, ainsi que la force élastique, sont des exemples de telles forces centrales. En revanche, la force entre des charges en mouvement, la gravité entre des corps en mouvement, et d'autres forces qui dépendent de la vitesse des deux corps en interaction sont des forces non centrales, et dans ces cas, la troisième loi ne peut pas être appliquée.

En tenant compte de la définition de la masse que nous avons examinée précédemment, la troisième loi peut être reformulée comme suit :

> III$^\prime$. Si deux corps forment un système isolé idéal, les accélérations de ces deux corps sont de directions opposées et le rapport de leurs magnitudes est égal à l'inverse du rapport de leurs masses.

Selon la troisième loi de Newton,

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

et en y appliquant la deuxième loi ($\ref{eqn:2nd_law}$) que nous avons vue précédemment,

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

De cela, on peut déduire que la quantité de mouvement est conservée dans l'interaction isolée entre deux particules.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

De plus, dans l'équation ($\ref{eqn:3rd-1_law}$), comme $\vec{p}=m\vec{v}$ et la masse $m$ est constante,

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

ce qui donne :

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Cependant, bien que la troisième loi de Newton décrive le cas où deux corps forment un système isolé, il est en réalité impossible de réaliser de telles conditions idéales, donc l'affirmation de Newton dans la troisième loi pourrait être considérée comme assez audacieuse. Malgré le fait que cette conclusion soit tirée d'observations limitées, grâce à la profonde intuition physique de Newton, la mécanique newtonienne a maintenu une position solide pendant près de 300 ans sans qu'aucune erreur ne soit découverte lors de diverses expériences de vérification. Ce n'est qu'au 20e siècle que des mesures suffisamment précises pour montrer des différences entre les prédictions de la théorie de Newton et la réalité sont devenues possibles, donnant naissance à la théorie de la relativité et à la mécanique quantique.

## Masse inertielle et masse gravitationnelle
Une méthode pour déterminer la masse d'un objet consiste à comparer son poids à un poids standard à l'aide d'un instrument tel qu'une balance. Cette méthode utilise le fait que le poids d'un objet dans un champ gravitationnel est égal à la magnitude de la force gravitationnelle agissant sur cet objet. Dans ce cas, la deuxième loi $\vec{F}=m\vec{a}$ prend la forme $\vec{W}=m\vec{g}$. Cette méthode repose sur l'hypothèse fondamentale que la masse $m$ définie dans III$^\prime$ est la même que la masse $m$ apparaissant dans l'équation gravitationnelle. Ces deux masses sont appelées respectivement **masse inertielle** et **masse gravitationnelle**, et sont définies comme suit :

- Masse inertielle : la masse qui détermine l'accélération d'un corps soumis à une force donnée
- Masse gravitationnelle : la masse qui détermine la force gravitationnelle entre un corps et un autre

Bien qu'il s'agisse d'une histoire inventée plus tard sans lien avec Galileo Galilei, l'expérience de chute de la tour de Pise est la première expérience de pensée montrant que la masse inertielle et la masse gravitationnelle seraient égales. Newton a également tenté de montrer qu'il n'y avait pas de différence entre les deux masses en mesurant les périodes de pendules de même longueur mais avec des masses différentes, mais sa méthode expérimentale et sa précision étaient rudimentaires, donc il n'a pas réussi à le prouver avec précision.

Plus tard, à la fin du 19e siècle, le physicien hongrois Loránd Eötvös a réalisé l'expérience d'Eötvös pour mesurer précisément la différence entre la masse inertielle et la masse gravitationnelle, prouvant leur identité avec une précision considérable (à l'intérieur d'une marge d'erreur de 1 sur 20 millions).

Des expériences plus récentes menées par Robert Henry Dicke et d'autres ont encore amélioré la précision, et il est maintenant connu que la masse inertielle et la masse gravitationnelle sont clairement identiques avec une marge d'erreur de l'ordre de $10^{-12}$. Ce résultat a une signification extrêmement importante dans la théorie de la relativité générale, et l'affirmation selon laquelle la masse inertielle et la masse gravitationnelle sont exactement égales est appelée le **principe d'équivalence**.
