---
title: Indicateurs de performance web (Web Vitals)
description: Découvrez les indicateurs de performance web (Web Vitals), les critères de mesure et d'évaluation de Lighthouse, et comprenez ce que signifie chaque indicateur de performance.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Facteurs déterminant les performances web
Les facteurs déterminant les performances web à considérer lors de l'optimisation peuvent être largement classés en deux catégories : les performances de chargement et les performances de rendu.

### Performances de chargement HTML
- Temps nécessaire depuis la première requête d'une page web au serveur via le réseau jusqu'à ce que le navigateur commence le rendu après avoir reçu le document HTML
- Détermine la rapidité avec laquelle la page commence à s'afficher
- Optimisé par des méthodes telles que la minimisation des redirections, la mise en cache des réponses HTML, la compression des ressources, et l'utilisation appropriée de CDN

### Performances de rendu
- Temps nécessaire au navigateur pour dessiner l'écran visible par l'utilisateur et le rendre interactif
- Détermine la fluidité et la rapidité avec laquelle l'écran est dessiné
- Optimisé par des méthodes telles que la suppression de CSS et JS inutiles, la prévention du chargement différé des polices et vignettes, la séparation des calculs lourds vers des Web Workers séparés pour minimiser l'occupation du thread principal, et l'optimisation des animations

## Indicateurs de performance web (Web Vitals)
Cette description se base sur [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) de Google et la [documentation développeur Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Sauf raison particulière, il est préférable de viser une amélioration globale plutôt que de se concentrer sur un seul indicateur de performance, et il est important d'identifier quelles parties de la page web à optimiser constituent un goulot d'étranglement pour les performances. De plus, lorsque des statistiques de données utilisateur réelles sont disponibles, il est recommandé de se concentrer sur les valeurs du premier quartile (Q1) plutôt que sur les valeurs moyennes ou du quartile supérieur, et de vérifier et améliorer si les critères cibles sont atteints même dans ces cas.

### Indicateurs de performance web essentiels (Core Web Vitals)
Comme nous le verrons bientôt, il existe plusieurs indicateurs de performance web (Web Vitals). Cependant, parmi ceux-ci, Google considère comme particulièrement importants les 3 indicateurs suivants qui sont étroitement liés à l'expérience utilisateur et peuvent être mesurés dans des environnements réels plutôt que simulés, appelés [Indicateurs de performance web essentiels (Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Comme Google reflète également les indicateurs de performance web essentiels des sites cibles dans l'ordre des résultats de recherche de son moteur de recherche, les opérateurs de sites doivent également examiner attentivement ces indicateurs du point de vue de l'optimisation pour les moteurs de recherche (SEO).
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint) : reflète les *performances de chargement*, doit être inférieur à 2,5 secondes
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}) : reflète la *réactivité*, doit être inférieur à 200ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift) : reflète la *stabilité visuelle*, doit être maintenu à 0,1 ou moins

Les indicateurs de performance web essentiels sont fondamentalement destinés à être mesurés dans des environnements réels, mais les deux autres à l'exception d'INP peuvent également être mesurés dans des environnements simulés comme les outils de développement Chrome ou Lighthouse. Dans le cas d'INP, comme il nécessite une entrée utilisateur réelle pour être mesuré, il ne peut pas être mesuré dans des environnements simulés, mais dans ce cas, [TBT](#tbt-total-blocking-time) peut être utilisé comme référence car il a une très forte corrélation avec INP et est un indicateur de performance similaire, et [généralement l'amélioration de TBT améliore également INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Pondération du score de performance de Lighthouse 10
[Le score de performance de Lighthouse est calculé comme une moyenne pondérée des scores de chaque métrique, suivant les pondérations du tableau suivant](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Métrique | Pondération |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Mesure le temps nécessaire pour rendre le premier contenu DOM après la requête de page
- Considère les images, les éléments `<canvas>` non blancs, les SVG, etc. comme contenu DOM dans la page, mais ne considère pas le contenu dans les `iframe`

> L'un des facteurs qui influence particulièrement le FCP est le temps de chargement des polices. Pour l'optimisation à ce sujet, la [documentation développeur Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recommande de consulter le [post associé](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Critères d'évaluation Lighthouse
Selon la [documentation développeur Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), les critères d'évaluation de Lighthouse sont les suivants :

| Grade de couleur | FCP mobile (secondes) | FCP bureau (secondes) |
| --- | --- | --- |
| Vert (rapide) | 0-1,8 | 0-0,9 |
| Orange (moyen) | 1,8-3 | 0,9-1,6 |
| Rouge (lent) | Plus de 3 | Plus de 1,6 |

### LCP (Largest Contentful Paint)
- Mesure le temps nécessaire pour rendre l'élément le plus grand (images, blocs de texte, vidéos, etc.) dans la zone d'affichage (viewport) visible en premier lors de l'ouverture initiale d'une page web
- Plus la surface occupée à l'écran est grande, plus il est probable que l'utilisateur la perçoive comme contenu principal
- Lorsque le LCP est une image, le temps nécessaire peut être divisé en 4 sous-intervalles, et il est important d'identifier où se produit le goulot d'étranglement
  1. Time to first byte (TTFB) : temps depuis le début du chargement de la page jusqu'à la réception du premier octet de la réponse du document HTML
  2. Délai de chargement (Load delay) : différence entre le moment où le navigateur commence à charger la ressource LCP et le TTFB
  3. Temps de chargement (Load time) : temps nécessaire pour charger la ressource LCP elle-même
  4. Délai de rendu (Render delay) : temps depuis la fin du chargement de la ressource LCP jusqu'à la fin complète du rendu de l'élément LCP

#### Critères d'évaluation Lighthouse
Selon la [documentation développeur Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), les critères d'évaluation de Lighthouse sont les suivants :

| Grade de couleur | FCP mobile (secondes) | FCP bureau (secondes) |
| --- | --- | --- |
| Vert (rapide) | 0-2,5 | 0-1,2 |
| Orange (moyen) | 2,5-4 | 1,2-2,4 |
| Rouge (lent) | Plus de 4 | Plus de 2,4 |

### TBT (Total Blocking Time)
- Mesure le temps total pendant lequel une page web ne peut pas répondre aux entrées utilisateur comme les clics de souris, les touches d'écran, les entrées clavier
- Parmi les tâches entre FCP et [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, celles qui s'exécutent pendant 50ms ou plus sont considérées comme [tâches longues](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}), et pour chacune de ces tâches longues, la partie excédentaire obtenue en soustrayant 50ms du temps nécessaire est appelée *partie bloquante (blocking portion)*, et la somme de toutes les parties bloquantes est définie comme TBT

> \* TTI lui-même est trop sensible aux valeurs aberrantes de réponse réseau et aux tâches longues, manquant de cohérence et ayant une forte variabilité, et par conséquent [a été exclu des éléments d'évaluation de performance depuis Lighthouse 10](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> En général, la cause la plus courante des tâches longues est le chargement, l'analyse et l'exécution de JavaScript inutiles ou inefficaces. La [documentation développeur Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) et [web.dev de Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recommandent de réduire la taille de la charge utile JavaScript grâce à la [division de code](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) pour que chacune puisse s'exécuter en moins de 50ms, et si nécessaire, de considérer l'exécution multithread en séparant vers un service worker séparé plutôt que le thread principal.
{: .prompt-tip }

#### Critères d'évaluation Lighthouse
Selon la [documentation développeur Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), les critères d'évaluation de Lighthouse sont les suivants :

| Grade de couleur | FCP mobile (millisecondes) | FCP bureau (millisecondes) |
| --- | --- | --- |
| Vert (rapide) | 0-200 | 0-150 |
| Orange (moyen) | 200-600 | 150-350 |
| Rouge (lent) | Plus de 600 | Plus de 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Exemple de changement soudain de mise en page" autoplay=true loop=true %}
> Source de la vidéo : [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Une profonde colère se ressent dans le mouvement du curseur~~

- Les changements de mise en page inattendus nuisent à l'expérience utilisateur de diverses manières, comme faire perdre la position de lecture en déplaçant soudainement le texte, ou faire cliquer par erreur sur des liens ou boutons
- La méthode spécifique de calcul du score CLS est décrite dans [web.dev de Google](https://web.dev/articles/cls)
- Comme on peut le voir dans l'image ci-dessous, l'objectif doit être de 0,1 ou moins

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> Source de l'image : [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Mesure la rapidité avec laquelle le contenu s'affiche visuellement pendant le chargement de la page
- Lighthouse enregistre en vidéo le processus de chargement de la page dans le navigateur, analyse cette vidéo pour calculer la progression entre les images, puis utilise le [module Node.js Speedline](https://github.com/paulirish/speedline) pour calculer le score SI

> Toutes les mesures d'amélioration de la vitesse de chargement des pages, y compris celles mentionnées précédemment pour [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint), [TBT](#tbt-total-blocking-time), ont également un effet positif sur le score SI. On peut considérer cet indicateur comme reflétant l'ensemble du processus de chargement à un certain niveau plutôt que de représenter seulement un processus particulier du chargement de page.
{: .prompt-tip }

#### Critères d'évaluation Lighthouse
Selon la [documentation développeur Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), les critères d'évaluation de Lighthouse sont les suivants :

| Grade de couleur | SI mobile (secondes) | SI bureau (secondes) |
| --- | --- | --- |
| Vert (rapide) | 0-3,4 | 0-1,3 |
| Orange (moyen) | 3,4-5,8 | 1,3-2,3 |
| Rouge (lent) | Plus de 5,8 | Plus de 2,3 |
