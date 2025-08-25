---
title: Dette technique
description: "Définition de la dette technique, ses causes fréquentes et des pratiques concrètes pour la prévenir, la réduire et la gérer dans un projet logiciel."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Dette technique
> **Dette technique**  
> Le coût différé que l’on devra payer plus tard lorsqu’on prend des raccourcis pour livrer un projet plus vite afin de satisfaire des besoins immédiats
{: .prompt-info }

Comme contracter une dette financière permet d’investir rapidement là où c’est nécessaire, au prix d’une pression financière et du remboursement du principal avec intérêts, accélérer le développement pour répondre à des exigences immédiates — même avec un code un peu brouillon — complexifie et duplique le code, ce qui rend ensuite plus difficile l’ajout de nouvelles fonctionnalités ou la montée en charge.

Tout comme une entreprise peut s’endetter pour investir à temps, développer de nouveaux produits et gagner des parts de marché, ou comme un particulier finance l’achat d’un logement par un crédit, accepter une certaine dette technique pour livrer rapidement des fonctionnalités n’est pas intrinsèquement mauvais. L’essentiel est d’en limiter l’accumulation et de la gérer à un niveau soutenable.

## Pourquoi la dette technique apparaît
Même avec des développeurs très compétents, la dette technique survient inévitablement au cours du développement, et l’empêcher totalement est impossible. À mesure qu’un service évolue, l’architecture initiale peut atteindre ses limites; du code qui était lisible et fonctionnel peut alors nécessiter des ajustements de conception. De plus, quand les technologies évoluent et que les bibliothèques ou frameworks autrefois dominants deviennent moins utilisés, on peut décider de migrer la pile technique; dans ce cas, le code existant devient lui aussi une forme de dette technique.

En outre, elle peut surgir pour les raisons suivantes:
- Ne pas documenter à temps les décisions de conception, rendant l’interprétation du code difficile pour d’autres, ou pour soi-même après un certain temps
- Ne pas supprimer les variables ou éléments de base de données devenus inutiles
- Ne pas automatiser les tâches répétitives (déploiement, build, etc.), ce qui engendre à chaque fois du temps et des efforts supplémentaires
- Modifications urgentes des spécifications

## Comment minimiser la dette technique
### Définir des conventions entre développeurs
- Si l’on ne développe pas seul, il faut s’accorder, pour une collaboration fluide, sur la langue, la pile technologique, la structure des répertoires du projet, le style de développement, etc.
- Décider ce qui doit être standardisé et ce qui peut relever de l’autonomie individuelle
- Procéder à des revues de code pour confronter les styles et échanger des avis

### Code propre et refactorisation
- Si le code existant est désordonné au point de gêner le développement, on peut apurer la dette technique en nettoyant l’architecture via la refactorisation
- Plus le code est un « spaghetti », plus la refactorisation est difficile; dans les cas extrêmes, on renonce à refactoriser et on jette l’ancien code pour réécrire depuis zéro
- Dans la mesure du possible, viser dès le départ un code lisible et facile à maintenir
