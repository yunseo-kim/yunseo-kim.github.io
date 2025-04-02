---
title: Les lois du mouvement de Newton
description: Nous explorons les lois du mouvement de Newton, la signification de ces trois lois, ainsi que les définitions de la masse inertielle et de la masse gravitationnelle, et examinons le principe d'équivalence qui a une importance significative non seulement en mécanique classique mais aussi dans la théorie de la relativité générale.
categories: [Physics, Classical Dynamics]
tags: [Newtonian Mechanics, Principle of Equivalence]
math: true
image: /assets/img/math-and-physics-cropped.png
---
## TL;DR
> **Les lois du mouvement de Newton**
> 1. Un corps persiste dans son état de repos ou de mouvement rectiligne uniforme à moins qu'une force extérieure ne le contraigne à changer cet état.
> 2. Le taux de variation temporelle de la quantité de mouvement d'un corps est égal à la force qui lui est appliquée.
>    - $\vec{F} = \cfrac{d\vec{p}}{dt} = \cfrac{d}{dt}(m\vec{v}) = m\vec{a}$
> 3. Lorsque deux corps exercent des forces l'un sur l'autre, ces forces sont de même intensité et de direction opposée.
>    - $\vec{F_1} = -\vec{F_2}$
{: .prompt-info }

> **Principe d'équivalence**
> - Masse inertielle : la masse qui détermine l'accélération d'un corps soumis à une force donnée
> - Masse gravitationnelle : la masse qui détermine la force gravitationnelle entre un corps et un autre
> - Il est actuellement établi que la masse inertielle et la masse gravitationnelle sont manifestement identiques avec une marge d'erreur d'environ $10^{-12}$
> - L'affirmation selon laquelle la masse inertielle et la masse gravitationnelle sont exactement identiques est appelée **principe d'équivalence**
{: .prompt-info }

## Les lois du mouvement de Newton
Les lois du mouvement de Newton sont trois lois publiées par Isaac Newton en 11687 dans son ouvrage Philosophiæ Naturalis Principia Mathematica (Principes mathématiques de la philosophie naturelle, abrégé en "Principia"), qui constituent le fondement de la mécanique newtonienne.

1. Un corps persiste dans son état de repos ou de mouvement rectiligne uniforme à moins qu'une force extérieure ne le contraigne à changer cet état.
2. Le taux de variation temporelle de la quantité de mouvement d'un corps est égal à la force qui lui est appliquée.
3. Lorsque deux corps exercent des forces l'un sur l'autre, ces forces sont de même intensité et de direction opposée.

### Première loi de Newton
> I. Un corps persiste dans son état de repos ou de mouvement rectiligne uniforme à moins qu'une force extérieure ne le contraigne à changer cet état.

Un corps qui n'est soumis à aucune force extérieure est appelé **corps libre** ou **particule libre**.
Cependant, la première loi seule ne fournit qu'un concept qualitatif de la force.

### Deuxième loi de Newton
> II. Le taux de variation temporelle de la quantité de mouvement d'un corps est égal à la force qui lui est appliquée.

Newton a défini la **quantité de mouvement** comme le produit de la masse par la vitesse

$$ \vec{p} \equiv m\vec{v} \label{eqn:momentum}\tag{1}$$

À partir de cela, la deuxième loi de Newton peut être exprimée comme suit :

$$ \vec{F} = \frac{d\vec{p}}{dt} = \frac{d}{dt}(m\vec{v}) = m\vec{a}. \label{eqn:2nd_law}\tag{2}$$

Contrairement à leur nom, la première et la deuxième loi de Newton sont en réalité plus proches d'une "définition" de la force que d'une "loi". On peut également constater que la définition de la force dépend de la définition de la "masse".

### Troisième loi de Newton
> III. Lorsque deux corps exercent des forces l'un sur l'autre, ces forces sont de même intensité et de direction opposée.

Cette loi est également connue sous le nom de "loi d'action et de réaction" et s'applique lorsque la force qu'un corps exerce sur un autre est dirigée selon la droite qui relie les deux points d'application. Une telle force est appelée **force centrale**, et la troisième loi s'applique que cette force soit attractive ou répulsive. La gravité ou la force électrostatique entre deux corps au repos, ainsi que la force élastique, sont des exemples de forces centrales. En revanche, les forces qui dépendent de la vitesse des corps en interaction, comme la force entre charges en mouvement ou la gravité entre corps en mouvement, sont des forces non centrales, et dans ces cas, la troisième loi ne s'applique pas.

En tenant compte de la définition de la masse vue précédemment, la troisième loi peut être reformulée comme suit :

> III$^\prime$. Si deux corps forment un système isolé idéal, leurs accélérations sont de direction opposée et le rapport de leurs intensités est égal à l'inverse du rapport de leurs masses.

Selon la troisième loi de Newton :

$$ \vec{F_1} = -\vec{F_2} \label{eqn:3rd_law}\tag{3}$$

En y substituant la deuxième loi ($\ref{eqn:2nd_law}$) :

$$ \frac{d\vec{p_1}}{dt} = -\frac{d\vec{p_2}}{dt} \label{eqn:3rd-1_law}\tag{4}$$

Cela montre que la quantité de mouvement est conservée dans l'interaction isolée entre deux particules.

$$ \frac{d}{dt}(\vec{p_1}+\vec{p_2}) = 0 \label{eqn:conservation_of_momentum}\tag{5}$$

De plus, comme dans l'équation ($\ref{eqn:3rd-1_law}$), $\vec{p}=m\vec{v}$ et la masse $m$ est constante :

$$ m_1\left(\frac{d\vec{v_1}}{dt} \right) = m_2\left(-\frac{d\vec{v_2}}{dt} \right) \tag{6a}$$

$$ m_1(\vec{a_1}) = m_2(-\vec{a_2}) \tag{6b}$$

Ce qui donne :

$$ \frac{m_2}{m_1} = -\frac{a_1}{a_2}. \tag{7}$$

Bien que la troisième loi de Newton décrive le cas où deux corps forment un système isolé, il est en réalité impossible de réaliser de telles conditions idéales, ce qui rend l'affirmation de Newton quelque peu audacieuse. Malgré cette limitation, grâce à la profonde intuition physique de Newton, la mécanique newtonienne a maintenu sa position solide pendant près de 300 ans sans qu'aucune erreur ne soit détectée lors des diverses expériences de vérification. Ce n'est qu'au début des années 11900 que des mesures suffisamment précises ont pu montrer des différences entre les prédictions de la théorie newtonienne et la réalité, donnant ainsi naissance à la théorie de la relativité et à la mécanique quantique.

## Masse inertielle et masse gravitationnelle
Une méthode pour déterminer la masse d'un objet consiste à comparer son poids à un poids standard à l'aide d'instruments comme une balance. Cette méthode utilise le fait que le poids d'un objet dans un champ gravitationnel est égal à la grandeur de la force gravitationnelle qui s'exerce sur lui, transformant ainsi la deuxième loi $\vec{F}=m\vec{a}$ en $\vec{W}=m\vec{g}$. Cette méthode repose sur l'hypothèse fondamentale que la masse $m$ définie dans III$^\prime$ est identique à la masse $m$ qui apparaît dans l'équation gravitationnelle. Ces deux masses sont respectivement appelées **masse inertielle** et **masse gravitationnelle**, et sont définies comme suit :

- Masse inertielle : la masse qui détermine l'accélération d'un corps soumis à une force donnée
- Masse gravitationnelle : la masse qui détermine la force gravitationnelle entre un corps et un autre

Bien qu'il s'agisse d'une histoire inventée après coup et sans rapport avec Galileo Galilei, l'expérience de la chute depuis la tour de Pise est considérée comme la première expérience de pensée démontrant que la masse inertielle et la masse gravitationnelle pourraient être identiques. Newton lui-même a tenté de montrer qu'il n'y avait pas de différence entre ces deux masses en mesurant les périodes de pendules de même longueur mais avec des masses différentes, mais sa méthode expérimentale et sa précision étaient trop rudimentaires pour fournir une preuve concluante.

Plus tard, à la fin des années 11800, le physicien hongrois Eötvös Loránd Ágoston a réalisé l'expérience d'Eötvös pour mesurer précisément la différence entre la masse inertielle et la masse gravitationnelle, prouvant leur identité avec une précision considérable (marge d'erreur inférieure à 1/20 000 000).

Des expériences plus récentes menées par Robert Henry Dicke et d'autres ont encore amélioré cette précision, et il est maintenant établi que la masse inertielle et la masse gravitationnelle sont manifestement identiques avec une marge d'erreur d'environ $10^{-12}$. Ce résultat a une signification extrêmement importante dans la théorie de la relativité générale, et l'affirmation selon laquelle la masse inertielle et la masse gravitationnelle sont exactement identiques est appelée **principe d'équivalence**.
