---
title: Principes pour écrire du bon code
description: Découvrez la nécessité d'écrire du bon code et les principes généraux pour y parvenir.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
---
## La nécessité d'écrire du bon code
Si l'on se contente d'écrire rapidement du code pour une implémentation immédiate, la [dette technique](/posts/Technical-debt/) peut s'accumuler à un niveau ingérable et causer des problèmes de maintenance ultérieurs. Par conséquent, il est indiscutablement important d'écrire dès le départ un code lisible et facile à maintenir lors du développement d'un projet.

Dans le cas de la résolution de problèmes algorithmiques (PS, Problem Solving) ou de la programmation compétitive (CP, Competitive Programming), on pourrait penser que l'écriture de bon code est moins importante que l'implémentation rapide, puisque le code utilisé n'est généralement pas réutilisé après la résolution du problème ou la fin du concours, et que les compétitions imposent des contraintes de temps. Pour répondre à cette question, il faut réfléchir à ce que l'on cherche à accomplir à travers le PS/CP et quelle direction on souhaite prendre.

Personnellement, je pense que les avantages du PS/CP sont les suivants :
- On peut utiliser et maîtriser divers algorithmes et structures de données pour résoudre des problèmes dans les limites de temps d'exécution et de mémoire imposées, ce qui permet de développer une intuition sur les algorithmes et structures de données à utiliser dans des situations spécifiques lors de projets réels
- On reçoit immédiatement des retours objectifs sur la justesse de la solution, le temps d'exécution et l'utilisation de la mémoire après avoir soumis son code, ce qui permet de s'entraîner à écrire du code précis rapidement et avec compétence
- On peut comparer son code avec celui d'experts et identifier des points d'amélioration
- Comparé aux projets de développement réels, on écrit de manière répétitive du code de petite taille ayant des fonctionnalités similaires, ce qui permet (surtout lorsqu'on pratique le PS seul) de s'exercer à écrire du code concis et de qualité en prêtant attention aux détails sans être contraint par des délais

Bien que certains pratiquent le PS/CP simplement comme un loisir, si on le fait pour améliorer indirectement ses compétences en programmation, le dernier point concernant "l'entraînement à écrire du bon code" est un avantage tout aussi important que les trois premiers. Écrire du bon code ne vient pas naturellement dès le début, mais nécessite une pratique constante. De plus, un code complexe et difficile à lire est difficile à déboguer et même difficile à écrire correctement du premier coup, ce qui peut entraîner une perte de temps en débogage inefficace et finalement ralentir l'implémentation. Bien que le PS/CP diffère considérablement du travail professionnel, négliger complètement l'écriture de bon code au profit d'une implémentation rapide serait, pour les raisons mentionnées, une inversion des priorités. C'est pourquoi je pense personnellement qu'il est préférable d'écrire un code concis et efficace même en PS/CP.

> Commentaire ajouté en 12024.12 :  
> Vu la tendance actuelle, à moins d'être spécialisé en informatique et de faire du développement son métier, pour ceux qui utilisent la programmation comme un outil pour l'analyse numérique ou le traitement de données expérimentales, il serait probablement plus judicieux d'utiliser activement des outils d'IA comme GitHub Copilot, Cursor ou Windsurf pour gagner du temps et consacrer ce temps économisé à d'autres apprentissages. Si le PS/CP est pratiqué comme un loisir, personne ne vous en dissuadera, mais investir du temps et des efforts dans le PS/CP pour s'entraîner à l'écriture de code semble désormais avoir un rapport coût-bénéfice assez faible. Même pour les métiers du développement, je prévois que l'importance des tests de codage comme critère d'embauche diminuera probablement considérablement par rapport à avant.
{: .prompt-warning }

## Principes pour écrire du bon code
Que ce soit pour du code écrit en compétition ou en milieu professionnel, les critères qui définissent un bon code ne sont pas fondamentalement différents. Cet article traite des principes généraux pour écrire du bon code. Cependant, en PS/CP, certains compromis peuvent être faits pour une implémentation rapide par rapport au milieu professionnel, et ces cas seront mentionnés spécifiquement dans l'article.

### Écrire du code concis
> "KISS (Keep It Simple, Stupid)"

- Plus le code est court et concis, moins il y a de risques de fautes de frappe ou de bugs simples, et plus le débogage est facile
- Écrire le code de manière à ce qu'il soit facilement interprétable sans commentaires supplémentaires, et n'ajouter des commentaires que lorsque c'est vraiment nécessaire pour des explications détaillées. Il est préférable de maintenir une structure de code concise plutôt que de s'appuyer sur des commentaires
- Si des commentaires sont nécessaires, les rédiger de manière claire et concise
- Limiter le nombre d'arguments passés à une fonction à trois maximum, et si plus d'arguments doivent être transmis ensemble, les regrouper en un seul objet
- La profondeur des instructions conditionnelles (imbrication de conditions) réduit la lisibilité, il faut donc éviter autant que possible d'augmenter cette profondeur.
  Ex) Le code ci-dessous utilisant des clauses de garde (Guard Clause) est plus lisible que le code au-dessus

  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if user:
          token = await user_service.get_token(user)
  
          if token :
              if token.purpose == 'reset':
                  return True
      return False
  ```
  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if not user:
          return False
    
      token = await user_service.get_token(user)
  
      if not token or token.purpose != 'reset':
          return False
    
    return True
  ```
- Cependant, en PS/CP, on utilise parfois des astuces comme les macros en C/C++ pour réduire davantage la longueur du code et l'écrire plus rapidement. C'est utile dans les compétitions où le temps est limité, mais c'est une pratique spécifique au PS/CP et l'utilisation de macros en C++ devrait généralement être évitée.
  Ex)

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularisation du code
> "DRY (Don't Repeat Yourself)"

- Séparer les parties de code répétitives en fonctions ou classes pour les réutiliser
- La modularisation pour une réutilisation active du code améliore la lisibilité et facilite la maintenance, car il suffit de modifier la fonction ou la classe concernée une seule fois en cas de besoin
- En principe, une fonction ne devrait idéalement accomplir qu'une seule tâche. Cependant, en PS/CP, les programmes sont généralement de petite taille avec des fonctionnalités simples, ce qui limite les possibilités de réutilisation, et les contraintes de temps rendent difficile le respect strict de ce principe comme en milieu professionnel.

### Utilisation des bibliothèques standard
> "Don't reinvent the wheel"

- Lors de l'apprentissage des algorithmes ou des structures de données, il est utile d'implémenter soi-même des structures comme les files ou les piles, ou des algorithmes de tri pour en comprendre les principes, mais sinon, il est préférable d'utiliser activement les bibliothèques standard
- Les bibliothèques standard ont été largement utilisées et validées, et sont bien optimisées, ce qui les rend plus efficaces qu'une implémentation personnelle
- L'utilisation de bibliothèques existantes évite de perdre du temps à réimplémenter des fonctionnalités identiques, et facilite la compréhension du code par les autres membres de l'équipe lors de collaborations

### Utilisation de conventions de nommage cohérentes et claires
> "Follow standard conventions"

- Utiliser des noms de variables et de fonctions non ambigus
- Chaque langage de programmation a généralement ses propres conventions de nommage, il est donc important de se familiariser avec celles utilisées dans la bibliothèque standard du langage et de les appliquer de manière cohérente lors de la déclaration de classes, fonctions, variables, etc.
- Nommer clairement chaque variable, fonction et classe pour refléter sa fonctionnalité, et pour les types booléens, indiquer clairement dans quelles conditions ils renvoient vrai (True)

### Normaliser toutes les données lors du stockage
- Traiter toutes les données dans un format cohérent et normalisé
- Si les mêmes données existent sous plusieurs formats, des bugs subtils et difficiles à détecter peuvent survenir, comme des différences mineures dans la représentation des chaînes de caractères ou des valeurs de hachage différentes
- Lors du stockage et du traitement de données comme les fuseaux horaires ou les chaînes de caractères, il faut les convertir dès leur réception ou calcul dans un format standard unique comme UTC ou l'encodage UTF-8. Il est préférable d'effectuer cette normalisation dès le constructeur de la classe qui représente ces données ou dès la fonction qui les reçoit.

### Séparer la logique du code et les données
- Séparer les données qui n'ont pas de rapport avec la logique du code en les plaçant dans des tables distinctes plutôt que directement dans les instructions conditionnelles
  Ex) Le code ci-dessous est préférable au code au-dessus.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ```c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ```
