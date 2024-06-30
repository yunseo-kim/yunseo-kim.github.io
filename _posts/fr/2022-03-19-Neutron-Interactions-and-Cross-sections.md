---
title: "Interactions des neutrons et sections efficaces"
description: >-
  Les neutrons étant électriquement neutres, ils peuvent traverser le nuage électronique des atomes sans subir d'influence électrique et interagir directement avec le noyau atomique. Nous examinerons les types d'interactions des neutrons et le concept de section efficace des noyaux atomiques.
categories: [Physique de l'ingénieur, Génie nucléaire]
tags: [Physique nucléaire, Interaction du rayonnement avec la matière]
math: true
mermaid: true
---

## Interactions des neutrons
Les neutrons étant électriquement neutres, ils ne sont pas affectés par l'influence électrique des électrons dans l'atome ou par la charge positive du noyau atomique. Par conséquent, les neutrons peuvent traverser le nuage électronique de l'atome et interagir directement avec le noyau atomique.

### Diffusion élastique (elastic scattering)
- Le neutron rebondit après avoir heurté le noyau atomique
- Le noyau atomique reste dans son état fondamental sans changement d'énergie
- Noté (n, n)

### Diffusion inélastique (inelastic scattering)
- Le neutron rebondit après avoir heurté le noyau atomique
- Contrairement à la diffusion élastique, le noyau atomique absorbe une partie de l'énergie du neutron et passe à un état excité (réaction endothermique)
- Noté (n, n′)
- Le noyau excité retourne à son état fondamental en émettant un rayonnement gamma, appelé *rayon gamma inélastique (inelastic $\gamma$-ray)*

### Capture radiative (radiative capture)
- Le noyau atomique capture le neutron et émet un ou plusieurs rayons gamma (réaction exothermique)
- Noté (n, $\gamma$)
- Le rayonnement gamma émis est appelé *rayon gamma de capture (capture $\gamma$-ray)*

### Réactions avec particules chargées
- Le noyau atomique capture le neutron et émet des particules chargées comme des particules alpha ($\alpha$) ou des protons (p)
- Noté (n, $\alpha$), (n, p), etc.
- Peut être une réaction exothermique ou endothermique selon le cas

### Réactions de production de neutrons
- Un neutron de haute énergie entre en collision avec un noyau atomique, produisant deux neutrons ou plus (réaction endothermique)
- Noté (n, 2n), (n, 3n), etc.
- La réaction (n, 2n) est particulièrement importante dans les réacteurs contenant de l'eau lourde ou du béryllium, car les neutrons de $^2\text{H}$ et $^9\text{Be}$ ont une faible énergie de liaison et peuvent être facilement libérés même lors de collisions avec des neutrons de faible énergie

### Fission (fission)
- Un neutron entre en collision avec un certain noyau atomique, le divisant en deux noyaux filles ou plus

## Section efficace (cross-section) ou section efficace microscopique (microscopic cross-section)
Supposons qu'un faisceau de neutrons monoénergétiques frappe une cible d'épaisseur (très fine) $\tau$ et de surface $A$, et que le nombre de neutrons incidents par unité de surface et par seconde sur la cible soit $I\ \text{neutrons/cm}^2\cdot \text{s}$. La proportion du volume occupé par le noyau atomique dans l'atome est très faible, et comme nous avons supposé que la cible est très mince, la plupart des neutrons traversent la cible sans interagir avec les noyaux atomiques. Alors, le nombre de neutrons entrant en collision avec les noyaux atomiques par unité de surface et par seconde est proportionnel à l'intensité du faisceau de neutrons $I$, à l'épaisseur de la cible $\tau$, et à la densité atomique de la cible $N$.

$$ \Delta I \propto I\tau N $$

En introduisant une constante de proportionnalité $\sigma$, on peut l'exprimer comme suit :

$$ \Delta I = \sigma I\tau N\ \text{[neutrons/cm}^2\cdot\text{s]} \tag{1} $$

Le rapport des neutrons entrant en collision avec les noyaux atomiques par rapport aux neutrons incidents sur la cible est donné par :

$$ p = \frac {\Delta I}{I} = \sigma\tau N = \frac {\sigma}{A} A\tau N = \frac {\sigma}{A} N_t \tag{2} $$

($N_t$ : nombre total d'atomes dans la cible)

On peut voir dans cette équation que $\sigma$ a les dimensions d'une surface. Cette constante de proportionnalité $\sigma$ est appelée *section efficace (cross-section)* ou *section efficace microscopique (microscopic cross-section)*. Physiquement, la section efficace représente la surface effective avec laquelle un noyau atomique peut interagir avec un neutron.

## Unité de la section efficace microscopique
cm$^2$ étant une unité trop grande pour exprimer la section efficace microscopique, on utilise généralement l'unité *barn* (b).

$$ 1\ \text{b} = 10^{-24}\ \text{cm}^2 $$

## Types de sections efficaces microscopiques
- Section efficace totale : $\sigma_t$
  - Section efficace de diffusion : $\sigma_s$
    - Section efficace de diffusion élastique : $\sigma_e$
    - Section efficace de diffusion inélastique : $\sigma_i$
  - Section efficace d'absorption : $\sigma_a$
    - Section efficace de capture radiative : $\sigma_\gamma$
    - Section efficace de fission : $\sigma_f$
    - Section efficace de réaction avec particules chargées : $\sigma_p, \sigma_\alpha, \cdots$
    - Section efficace de réaction de production de neutrons : $\sigma_{2n}, \sigma_{3n}, \cdots$

```mermaid
flowchart LR
	total["Section efficace totale t"] --- s["Section efficace de diffusion s"]
	total --- a["Section efficace d'absorption a"]

	s --- e["Section efficace de diffusion élastique e"]
	s --- i["Section efficace de diffusion inélastique i"]

	a --- gamma["Section efficace de capture radiative γ"]
	a --- f["Section efficace de fission f"]
	a --- p["Section efficace de réaction avec particules chargées p, α, ..."]
	a --- n["Section efficace de réaction de production de neutrons 2n, 3n, ..."]
```

## Section efficace macroscopique (macroscopic cross-section)
À partir de l'équation (2), on peut calculer le taux de collision par unité de distance du faisceau de neutrons comme suit :

$$ \frac {p}{\tau} = \frac {1}{\tau} \frac {\Delta I}{I} = \sigma N \equiv \Sigma\ \text{[cm}^{-1}\text{]} \tag{3}$$

La *section efficace macroscopique (macroscopic cross-section)* est définie comme le produit de la densité atomique $N$ et de la section efficace. Physiquement, la section efficace macroscopique représente le taux de collision par unité de distance parcourue par un neutron dans une cible donnée. Comme pour la section efficace microscopique, elle peut être subdivisée comme suit :

- Section efficace macroscopique totale $\Sigma_t=N\sigma_t$
  - Section efficace macroscopique de diffusion $\Sigma_s=N\sigma_s$
  - Section efficace macroscopique d'absorption $\Sigma_a=N\sigma_a$

En général, pour une réaction donnée, la section efficace macroscopique est $\Sigma_{reaction}=N\sigma_{reaction}$.

## Densité de collision (collision density), c'est-à-dire taux de réaction (reaction rate)
La *densité de collision (collision density)*, ou *taux de réaction (reaction rate)*, représente le nombre de collisions par unité de temps et par unité de volume dans la cible. À partir des équations (1) et (3), on peut la définir comme suit :

$$ F = \frac {\Delta I}{\tau} = I\sigma N = I\Sigma \tag{4} $$