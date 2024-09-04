---
title: "Dette technique (Technical debt)"
description: >-
  Examinons le concept de dette technique, les raisons de son apparition, et les moyens de la minimiser.
categories: [Programming]
tags: [Coding]
---

## Dette technique (Technical debt)
Dette technique : le prix à payer ultérieurement pour avoir choisi des raccourcis permettant de terminer plus rapidement un projet immédiat afin de répondre aux exigences immédiates dans le processus de développement.

Tout comme emprunter de l'argent en assumant une dette comptable permet d'investir rapidement là où c'est nécessaire dans l'immédiat, mais entraîne une pression financière et le remboursement du principal avec intérêts, procéder à un développement rapide, même un peu désordonné, pour résoudre les exigences immédiates rend le code complexe et redondant, ce qui complique la mise en œuvre ou l'extension de nouvelles fonctionnalités par la suite.

Il n'est pas nécessairement mauvais d'assumer une dette technique pour implémenter rapidement de nouvelles fonctionnalités, tout comme une entreprise peut réaliser plus d'investissements en temps opportun pour développer de nouveaux produits et augmenter sa part de marché grâce à la dette, ou comme un individu peut contracter un prêt pour acheter une maison. Cependant, il est souhaitable de réduire l'accumulation de la dette technique et de la gérer à un niveau supportable.

## Raisons de l'apparition de la dette technique
Même si les compétences du développeur sont suffisantes, la dette technique survient inévitablement dans le processus de création de logiciels et il est impossible de l'empêcher complètement.
Lorsqu'un service évolue et que le code conçu à l'origine atteint ses limites, il peut être nécessaire de modifier la conception existante, même si le code était à l'origine lisible et fonctionnait bien.
De plus, à mesure que la technologie elle-même évolue, on peut décider de changer de pile technologique pour passer à une autre bibliothèque/framework si celle qui était autrefois dominante n'est plus beaucoup utilisée, et dans ce cas, le code écrit précédemment devient une sorte de dette technique.

La dette technique peut également survenir pour les raisons suivantes :
- Ne pas documenter la conception en temps réel pendant le projet, ce qui rend difficile l'interprétation du code pour les autres ou pour soi-même après un certain temps
- Ne pas supprimer les variables ou les éléments de base de données qui ne sont plus utilisés
- Ne pas automatiser les tâches répétitives (déploiement/construction, etc.), ce qui nécessite du temps et des efforts supplémentaires à chaque fois
- Changements de spécifications urgents

## Méthodes pour minimiser la dette technique
### Établir des conventions entre développeurs
- S'il ne s'agit pas d'un développement en solo, il est nécessaire de s'accorder sur le langage ou la pile technologique à utiliser, la structure des répertoires du projet, le style de développement, etc. pour une collaboration efficace
- Il faut décider jusqu'où unifier les méthodes de développement et à partir de quand laisser l'autonomie individuelle
- Il est nécessaire d'examiner et de discuter des styles de développement de chacun à travers des revues de code

### Écriture de code propre (Clean Code) & Refactorisation (Refactoring)
- Si le code existant est désordonné et entrave le développement, on peut rembourser la dette technique en restructurant le code de manière plus propre par la refactorisation
- Naturellement, plus le code existant est un code spaghetti désordonné, plus la difficulté de refactorisation est élevée
- Il faut s'efforcer d'écrire dès le départ un code lisible et facile à maintenir