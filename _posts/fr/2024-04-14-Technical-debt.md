---
title: "Dette technique (Technical debt)"
description: >-
  Découvrons le concept de dette technique, les raisons de son apparition, et les méthodes pour la minimiser.
categories: [Programming]
tags: [Coding]
---

## Dette technique (Technical debt)
Dette technique : le prix à payer ultérieurement pour avoir choisi des raccourcis permettant de terminer plus rapidement un projet immédiat afin de répondre aux exigences immédiates dans le processus de développement.

Tout comme emprunter de l'argent en assumant une dette comptable permet d'investir rapidement là où c'est nécessaire dans l'immédiat, mais entraîne une pression financière et le remboursement du principal avec intérêts, le fait de développer rapidement, même de manière un peu désordonnée, pour résoudre les exigences immédiates, rend le code complexe et redondant, ce qui complique la mise en œuvre ou l'extension de nouvelles fonctionnalités par la suite.

Tout comme une entreprise peut réaliser davantage d'investissements en temps opportun grâce à la dette pour développer de nouveaux produits et augmenter sa part de marché, ou comme un individu peut acheter une maison grâce à un prêt, assumer une dette technique pour implémenter rapidement de nouvelles fonctionnalités n'est pas nécessairement une mauvaise chose. Cependant, il est souhaitable de réduire l'accumulation de dette technique et de la gérer à un niveau supportable.

## Raisons de l'apparition de la dette technique
Même si les compétences du développeur sont suffisantes, la dette technique survient inévitablement dans le processus de création de logiciels et il est impossible de l'empêcher complètement.
Lorsque le service évolue et que le code conçu à l'origine atteint ses limites, il peut être nécessaire de modifier la conception existante, même si le code était à l'origine lisible et fonctionnel.
De plus, à mesure que la technologie elle-même évolue, on peut décider de changer de pile technologique pour passer à une autre bibliothèque/framework lorsque celle qui était autrefois dominante n'est plus beaucoup utilisée, et dans ce cas, le code écrit précédemment devient une sorte de dette technique.

La dette technique peut également survenir pour les raisons suivantes :
- Ne pas documenter la conception en temps réel pendant le projet, ce qui rend difficile l'interprétation du code pour les autres ou pour soi-même après un certain temps
- Ne pas supprimer les variables ou les éléments de base de données qui ne sont plus utilisés
- Ne pas automatiser les tâches répétitives (déploiement/construction, etc.), ce qui nécessite du temps et des efforts supplémentaires à chaque fois
- Changements de spécifications urgents

## Méthodes pour minimiser la dette technique
### Établir des conventions entre développeurs
- S'il ne s'agit pas d'un développement en solo, il est nécessaire de s'accorder sur le langage ou la pile technologique à utiliser, la structure des répertoires du projet, le style de développement, etc. pour une collaboration efficace
- Il faut décider jusqu'où unifier les méthodes de développement et à partir de quand laisser l'autonomie individuelle
- Il est nécessaire d'échanger des opinions et de vérifier mutuellement les styles de développement à travers des revues de code

### Écriture de code propre (Clean Code) & Refactorisation (Refactoring)
- Si le code existant est désordonné et entrave le développement, on peut rembourser la dette technique en restructurant proprement le code par le biais de la refactorisation
- Bien sûr, plus le code existant est un code spaghetti désordonné, plus la difficulté de refactorisation augmente
- Il faut s'efforcer d'écrire dès le départ un code lisible et facile à maintenir