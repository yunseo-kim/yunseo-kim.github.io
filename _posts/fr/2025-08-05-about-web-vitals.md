---
title: Indicateurs de performance web (Web Vitals)
description: "Aperçu des Web Vitals et des critères Lighthouse: définitions, seuils et conseils pour comprendre chaque indicateur et optimiser les performances."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Facteurs qui déterminent les performances web
Lors de l’optimisation des performances, on peut regrouper les facteurs déterminants en deux grandes catégories: performances de chargement et performances de rendu.

### Performances de chargement HTML
- Temps écoulé entre la première requête de page au serveur via le réseau et le moment où le navigateur commence à rendre le document HTML
- Détermine la rapidité avec laquelle la page commence à s’afficher
- Optimisation par la réduction des redirections, la mise en cache des réponses HTML, la compression des ressources, l’usage approprié d’un CDN, etc.

### Performances de rendu
- Temps nécessaire au navigateur pour dessiner l’interface visible et la rendre interactive
- Détermine la fluidité et la vitesse d’affichage
- Optimisation via la suppression du CSS/JS inutile, la prévention des retards de chargement des polices et miniatures, la délégation des tâches lourdes à des Web Workers pour minimiser l’occupation du thread principal, l’optimisation des animations, etc.

## Indicateurs de performance web (Web Vitals)
La description s’appuie sur [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) de Google et la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Sauf raison particulière, il vaut mieux viser une amélioration globale plutôt que de se focaliser sur un seul indicateur, et identifier les véritables goulots d’étranglement de la page à optimiser. Lorsque des données réelles d’utilisateurs sont disponibles, il est préférable de se concentrer sur le premier quartile (Q1) plutôt que sur la moyenne ou le haut du panier, et de vérifier que les objectifs sont atteints même dans ces cas moins favorables.

### Indicateurs clés de performance web (Core Web Vitals)
Comme nous le verrons, il existe plusieurs Web Vitals. Parmi eux, trois indicateurs, étroitement liés à l’expérience utilisateur et mesurables en conditions réelles, sont considérés comme particulièrement importants par Google: ce sont les [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Google les prend en compte dans le classement de son moteur de recherche; ils sont donc cruciaux pour l’optimisation pour les moteurs de recherche (SEO) du site.
- [Largest Contentful Paint (LCP)](#lcp-largest-contentful-paint): reflète les *performances de chargement*, doit être ≤ 2,5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): reflète la *réactivité*, doit être ≤ 200 ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): reflète la *stabilité visuelle*, doit rester ≤ 0,1

Les Core Web Vitals sont conçus pour être mesurés en conditions réelles. Toutefois, à l’exception de l’INP, les deux autres peuvent aussi être mesurés en environnement simulé (Chrome DevTools, Lighthouse). L’INP exige de vraies interactions utilisateur et ne peut donc pas être mesuré en laboratoire; dans ce cas, le [TBT](#tbt-total-blocking-time), fortement corrélé à l’INP et de nature similaire, peut servir de référence, et [améliorer le TBT améliore généralement aussi l’INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Pondération du score de performance dans Lighthouse 10
[Le score de performance de Lighthouse est la moyenne pondérée des métriques, avec les pondérations suivantes](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Métrique | Pondération |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Mesure le temps nécessaire pour rendre le premier contenu DOM après la requête de page
- Considère comme contenu DOM les images, les éléments `<canvas>` non blancs, les SVG, etc.; le contenu des `iframe` n’est pas pris en compte

> Parmi les facteurs influençant fortement le FCP figure le temps de chargement des polices; la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recommande de consulter [l’article associé](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) pour l’optimiser.
{: .prompt-tip }

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), les critères sont les suivants.

| Couleur | FCP mobile (s) | FCP ordinateur (s) |
| --- | --- | --- |
| Vert (rapide) | 0-1,8 | 0-0,9 |
| Orange (moyen) | 1,8-3 | 0,9-1,6 |
| Rouge (lent) | supérieur à 3 | supérieur à 1,6 |

### LCP (Largest Contentful Paint)
- Mesure, au premier affichage de la page, le temps nécessaire pour rendre dans la fenêtre d’affichage (viewport) l’élément le plus volumineux (image, bloc de texte, vidéo, etc.) situé dans cette zone
- Plus l’élément occupe de surface à l’écran, plus l’utilisateur est susceptible de le percevoir comme un contenu principal
- Si le LCP est une image, on peut décomposer la durée en quatre sous-étapes; identifier le goulet d’étranglement est essentiel:
  1. Time to First Byte (TTFB): temps entre le début du chargement de la page et la réception du premier octet de la réponse HTML
  2. Délai de chargement (Load delay): écart entre le TTFB et le moment où le navigateur commence à charger la ressource LCP
  3. Temps de chargement (Load time): temps nécessaire pour charger la ressource LCP
  4. Délai de rendu (Render delay): temps entre la fin du chargement de la ressource LCP et l’achèvement du rendu de l’élément LCP

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), les critères sont les suivants.

| Couleur | LCP mobile (s) | LCP ordinateur (s) |
| --- | --- | --- |
| Vert (rapide) | 0-2,5 | 0-1,2 |
| Orange (moyen) | 2,5-4 | 1,2-2,4 |
| Rouge (lent) | supérieur à 4 | supérieur à 2,4 |

### TBT (Total Blocking Time)
- Mesure le temps total pendant lequel la page ne répond pas aux interactions utilisateur (clics, taps, saisie clavier, etc.)
- Parmi les tâches exécutées entre le FCP et le [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, on considère comme [long tasks](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) celles qui durent ≥ 50 ms; pour chacune, la portion excédant 50 ms constitue la *partie bloquante (blocking portion)* et la somme de ces portions correspond au TBT

> \* Le TTI lui-même est trop sensible aux anomalies réseau et aux long tasks, avec une faible cohérence et une grande variabilité; en conséquence, [il a été retiré du score de performance à partir de Lighthouse 10](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Les causes les plus fréquentes des long tasks sont le chargement, l’analyse et l’exécution JavaScript inutiles ou inefficaces. La [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) et [web.dev de Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recommandent de recourir au [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) pour réduire la taille du payload et faire en sorte que chaque module s’exécute en moins de 50 ms, et si nécessaire de déplacer leur exécution en multithread via un Service Worker distinct plutôt que sur le thread principal.
{: .prompt-tip }

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), les critères sont les suivants.

| Couleur | TBT mobile (ms) | TBT ordinateur (ms) |
| --- | --- | --- |
| Vert (rapide) | 0-200 | 0-150 |
| Orange (moyen) | 200-600 | 150-350 |
| Rouge (lent) | supérieur à 600 | supérieur à 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Exemple de changement de mise en page soudain" autoplay=true loop=true %}
> Source de la vidéo: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~On sent une profonde colère dans le mouvement du curseur~~

- Les changements de mise en page inattendus nuisent à l’expérience: le texte se déplace, on perd sa ligne de lecture, on clique sur le mauvais lien/bouton, etc.
- La méthode détaillée de calcul du score CLS est décrite sur [web.dev de Google](https://web.dev/articles/cls)
- Comme l’illustre l’image ci-dessous, il faut viser ≤ 0,1

![Quel est un bon score CLS ?](/assets/img/about-web-vitals/good-cls-values.svg)
> Source de l’image: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Mesure la vitesse à laquelle le contenu devient visuellement disponible pendant le chargement de la page
- Lighthouse enregistre le chargement sous forme de vidéo, analyse la progression des frames, puis utilise le [module Node.js Speedline](https://github.com/paulirish/speedline) pour calculer le score SI

> En plus de ce qui a été évoqué pour [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) et [TBT](#tbt-total-blocking-time), toute action qui accélère le chargement de la page profite aussi au SI. Celui-ci reflète non pas une étape unique, mais l’ensemble du processus de chargement.
{: .prompt-tip }

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), les critères sont les suivants.

| Couleur | SI mobile (s) | SI ordinateur (s) |
| --- | --- | --- |
| Vert (rapide) | 0-3,4 | 0-1,3 |
| Orange (moyen) | 3,4-5,8 | 1,3-2,3 |
| Rouge (lent) | supérieur à 5,8 | supérieur à 2,3 |
