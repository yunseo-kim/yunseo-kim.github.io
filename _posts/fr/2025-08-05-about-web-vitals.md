---
title: Indicateurs de performance Web (Web Vitals)
description: Synthèse des Web Vitals et des critères de mesure et de notation Lighthouse, avec l’explication de chaque indicateur (LCP, INP, CLS, TBT, FCP, SI) et des seuils à viser pour le SEO.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Facteurs qui déterminent la performance Web
Lors de l’optimisation des performances Web, on peut regrouper les facteurs déterminants en deux grandes catégories: performance de chargement et performance de rendu.

### Performance de chargement HTML
- Temps écoulé entre la première requête de page au serveur via le réseau et le moment où le navigateur commence à effectuer le rendu du document HTML reçu
- Détermine la rapidité avec laquelle l’affichage de la page commence
- Optimisations possibles: réduction des redirections, mise en cache de la réponse HTML, compression des ressources, utilisation appropriée d’un CDN, etc.

### Performance de rendu
- Temps nécessaire pour que le navigateur dessine l’interface visible par l’utilisateur et la rende interactive
- Détermine à quel point l’affichage est fluide et rapide
- Optimisations possibles: élimination du CSS et du JS superflus, éviter de retarder le chargement des polices et des miniatures, déléguer les calculs lourds à un Web Worker distinct afin de minimiser l’occupation du thread principal, optimisation des animations, etc.

## Indicateurs de performance Web (Web Vitals)
La description qui suit s’appuie sur [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) de Google et la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Sauf raison particulière, il est préférable de viser une amélioration globale plutôt que de se focaliser sur un seul indicateur, et d’identifier les véritables goulets d’étranglement de la page à optimiser. Si vous disposez de données réelles d’utilisateurs, concentrez-vous plutôt sur les valeurs du premier quartile (Q1) que sur les moyennes ou les meilleures, et vérifiez que l’objectif est atteint même dans ces cas.

### Indicateurs Web essentiels (Core Web Vitals)
Il existe de nombreux Web Vitals, que nous aborderons plus loin. Parmi eux, Google considère comme particulièrement importants les trois indicateurs suivants, étroitement liés à l’expérience utilisateur et mesurables sur le terrain (et pas seulement en laboratoire): ce sont les [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Google prenant en compte ces indicateurs dans le classement des résultats de son moteur de recherche, ils doivent également être suivis de près du point de vue du référencement (SEO).
- [Largest Contentful Paint (LCP)](#lcp-largest-contentful-paint): reflète la performance de chargement; doit être ≤ 2,5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): reflète la réactivité; doit être ≤ 200 ms
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): reflète la stabilité visuelle; doit rester ≤ 0,1

Les Core Web Vitals sont conçus pour être mesurés en conditions réelles; toutefois, à l’exception de l’INP, les deux autres peuvent aussi être mesurés en environnement simulé (DevTools Chrome, Lighthouse). L’INP exige des interactions réelles de l’utilisateur et n’est donc pas mesurable en laboratoire; dans ce cas, [le TBT](#tbt-total-blocking-time) est fortement corrélé à l’INP et peut servir de substitut, [l’amélioration du TBT entraînant généralement celle de l’INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Pondération du score de performance dans Lighthouse 10
[Le score de performance Lighthouse est une moyenne pondérée des sous-scores, avec les pondérations suivantes](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Mesure | Pondération |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Mesure le temps nécessaire pour rendre le premier contenu DOM après la requête de page
- Sont considérés comme contenu DOM: images de la page, éléments `<canvas>` non blancs, SVG, etc.; le contenu à l’intérieur d’un `iframe` n’est pas pris en compte

> Parmi les facteurs influençant fortement le FCP figure le temps de chargement des polices. La [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recommande de consulter ce [billet connexe](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) pour des optimisations à ce sujet.
{: .prompt-tip }

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), les seuils Lighthouse sont les suivants.

| Code couleur | FCP mobile (s) | FCP ordinateur (s) |
| --- | --- | --- |
| Vert (rapide) | 0-1.8 | 0-0.9 |
| Orange (moyen) | 1.8-3 | 0.9-1.6 |
| Rouge (lent) | > 3 | > 1.6 |

### LCP (Largest Contentful Paint)
- À l’ouverture de la page, mesure le temps nécessaire pour rendre, dans la zone d’affichage initiale (viewport), l’élément le plus grand (image, bloc de texte, vidéo, etc.)
- Plus la surface occupée à l’écran est grande, plus il est probable que l’utilisateur la perçoive comme un contenu principal
- Si le LCP est une image, on peut décomposer le temps en 4 sous-parties; identifier le goulot d’étranglement est crucial:
  1. Time to First Byte (TTFB): temps entre le début du chargement de la page et la réception du premier octet de la réponse HTML
  2. Délai de chargement (Load delay): différence entre le moment où le navigateur commence à charger la ressource LCP et le TTFB
  3. Temps de chargement (Load time): temps nécessaire pour charger la ressource LCP elle-même
  4. Délai de rendu (Render delay): temps entre la fin du chargement de la ressource LCP et l’achèvement du rendu de l’élément LCP

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), les seuils Lighthouse sont les suivants.

| Code couleur | LCP mobile (s) | LCP ordinateur (s) |
| --- | --- | --- |
| Vert (rapide) | 0-2.5 | 0-1.2 |
| Orange (moyen) | 2.5-4 | 1.2-2.4 |
| Rouge (lent) | > 4 | > 2.4 |

### TBT (Total Blocking Time)
- Mesure le temps total pendant lequel la page ne peut pas répondre aux interactions de l’utilisateur (clics, touchers, saisies clavier)
- Entre le FCP et le [TTI (Time to Interactive, début de l’interaction)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }}), les tâches durant ≥ 50 ms sont considérées comme des [tâches longues](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}). Pour chacune, la partie au-delà de 50 ms est appelée portion de blocage (blocking portion). Le TBT est la somme de ces portions de blocage.

> Le TTI lui-même est trop sensible aux anomalies réseau et aux tâches longues, avec une faible cohérence et une grande variabilité; en conséquence, [depuis Lighthouse 10 il a été retiré du scoring](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Les causes les plus fréquentes des tâches longues sont le chargement, l’analyse et l’exécution JavaScript inutiles ou inefficaces. La [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) et [web.dev de Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recommandent de recourir au [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) pour réduire la taille du payload afin que chaque chunk s’exécute en ≤ 50 ms et, si nécessaire, d’exécuter hors thread principal (p. ex. dans un service worker) pour du multi-threading.
{: .prompt-tip }

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), les seuils Lighthouse sont les suivants.

| Code couleur | TBT mobile (ms) | TBT ordinateur (ms) |
| --- | --- | --- |
| Vert (rapide) | 0-200 | 0-150 |
| Orange (moyen) | 200-600 | 150-350 |
| Rouge (lent) | > 600 | > 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Exemple de changement soudain de mise en page" autoplay=true loop=true %}
> Source de la vidéo: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~On ressent une colère profonde dans le mouvement du curseur~~

- Les changements de mise en page inattendus dégradent l’expérience utilisateur de multiples façons: déplacement soudain du texte faisant perdre la ligne, clics erronés sur un lien ou un bouton, etc.
- La méthode de calcul détaillée du score CLS est décrite sur [web.dev de Google](https://web.dev/articles/cls)
- Comme l’illustre l’image ci-dessous, l’objectif doit être ≤ 0,1

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> Source de l’image: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Mesure la vitesse à laquelle le contenu devient visuellement visible pendant le chargement de la page
- Lighthouse enregistre le processus de chargement sous forme de vidéo, l’analyse pour calculer la progression image par image, puis utilise le [module Node.js Speedline](https://github.com/paulirish/speedline) pour déterminer le score SI

> Toutes les optimisations qui améliorent la vitesse de chargement — y compris celles évoquées pour le [FCP](#fcp-first-contentful-paint), le [LCP](#lcp-largest-contentful-paint) et le [TBT](#tbt-total-blocking-time) — ont en général un effet positif sur le SI. On peut voir cet indicateur comme reflétant, non pas une seule étape, mais l’ensemble du processus de chargement.
{: .prompt-tip }

#### Critères d’évaluation Lighthouse
Selon la [documentation des développeurs Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), les seuils Lighthouse sont les suivants.

| Code couleur | SI mobile (s) | SI ordinateur (s) |
| --- | --- | --- |
| Vert (rapide) | 0-3.4 | 0-1.3 |
| Orange (moyen) | 3.4-5.8 | 1.3-2.3 |
| Rouge (lent) | > 5.8 | > 2.3 |
