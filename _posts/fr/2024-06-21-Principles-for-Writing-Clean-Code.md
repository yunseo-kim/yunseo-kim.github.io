---
title: "Principes pour écrire du bon code"
description: >-
  Nous examinons la nécessité d'écrire du bon code et les principes généraux pour écrire du bon code.
categories:
  - Programming
tags:
  - Coding
  - PS/CP
---
## La nécessité d'écrire du bon code
Si l'on se contente d'écrire rapidement du code pour une implémentation immédiate, la dette technique peut augmenter à un niveau ingérable, ce qui peut poser des problèmes de maintenance ultérieurement. Par conséquent, il est inutile de dire qu'il est important d'écrire dès le début un bon code lisible et facile à maintenir lors de la réalisation d'un projet de développement.

Dans le cas de la résolution de problèmes algorithmiques (PS, Problem Solving) ou des compétitions de programmation (CP, Competitive Programming), on dit généralement qu'il n'y a pas besoin de réutiliser le code utilisé pour résoudre le problème une fois le problème résolu ou la compétition terminée, et en particulier dans le cas du CP, il y a une limite de temps, donc on pourrait penser que l'implémentation rapide est plus importante que l'écriture de bon code. Pour répondre à cette question, il faut réfléchir à ce pour quoi on fait du PS/CP et quelle direction on veut prendre.

Personnellement, je pense que les points que l'on peut apprendre à travers le PS/CP sont les suivants :
- On peut utiliser et maîtriser divers algorithmes et structures de données dans le processus de résolution de problèmes dans les limites de temps d'exécution et de mémoire données, et ainsi acquérir une intuition sur les algorithmes et structures de données à utiliser dans certaines situations lors de la réalisation de projets réels
- Après avoir écrit et soumis le code, on peut recevoir immédiatement un retour objectif sur la justesse/l'erreur, le temps d'exécution et l'utilisation de la mémoire, ce qui permet de s'entraîner à écrire rapidement et habilement un code précis sans rien manquer
- On peut voir le code écrit par d'autres experts, le comparer avec son propre code et trouver des points d'amélioration
- Comme on écrit de manière répétitive du code de petite taille et de fonctionnalité similaire par rapport à un projet de développement réel, (en particulier lorsqu'on s'entraîne seul au PS) on peut s'exercer à écrire un code concis et de qualité en prêtant attention aux détails sans être lié à des délais

Bien qu'il puisse y avoir des cas où l'on pratique le PS/CP simplement comme un passe-temps, si, comme moi, on le fait indirectement pour améliorer ses compétences en programmation, le dernier point "s'exercer à écrire du bon code" est un avantage tout aussi important que les trois premiers. Écrire du bon code ne vient pas naturellement dès le début, mais nécessite une pratique répétée et constante. De plus, un code complexe et difficile à lire est difficile à déboguer et n'est pas facile à écrire correctement du premier coup, donc si l'on perd du temps dans un débogage inefficace, on finit par ne pas implémenter si rapidement. Bien que le PS/CP soit bien sûr très différent du travail réel, ne pas du tout se soucier d'écrire du bon code et se précipiter sur l'implémentation immédiate est, pour les raisons mentionnées ci-dessus, une inversion des priorités, donc personnellement, j'essaie d'écrire un code concis et efficace même en PS/CP.

## Principes pour écrire du bon code
Que ce soit pour le code écrit en compétition ou le code écrit en pratique, les conditions pour qu'un code soit considéré comme bon ne sont pas très différentes. Dans cet article, nous abordons les principaux principes pour écrire généralement du bon code. Cependant, en PS/CP, il peut y avoir des compromis relatifs par rapport à la pratique pour une implémentation rapide, et dans ces cas, je le mentionnerai séparément dans l'article.

### Écrire un code concis
> "KISS (Keep It Simple, Stupid)"
- Plus le code est court et concis, moins il y a de risques de fautes de frappe ou de bugs simples, et plus le débogage est facile
- Écrire autant que possible de manière à ce qu'il soit facile à interpréter sans commentaires séparés, et n'ajouter des commentaires que lorsque c'est vraiment nécessaire pour des explications détaillées. Il est préférable de maintenir la structure du code elle-même concise plutôt que de s'appuyer sur des commentaires.
- Lorsque vous écrivez des commentaires, faites-le de manière claire et concise
- Limiter le nombre d'arguments passés à une fonction à 3 ou moins, et si plus d'arguments doivent être passés ensemble, les regrouper en un seul objet
- La profondeur (depth) des instructions conditionnelles qui s'emboîtent doublement ou triplement réduit la lisibilité, donc il faut éviter autant que possible d'augmenter la profondeur des instructions conditionnelles. 
  ex) Le code ci-dessous utilisant la clause de garde (Guard Clause) est plus avantageux en termes de lisibilité que le code ci-dessus  

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
- Cependant, en PS/CP, pour aller plus loin et réduire la longueur du code pour l'écrire rapidement, on utilise parfois l'astuce des macros en C/C++. C'est utile à utiliser occasionnellement pour les compétitions où le temps est limité, mais c'est une méthode qui ne fonctionne que pour le PS/CP, et en général, l'utilisation de macros en C++ doit être évitée.  
  ex)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularisation du code
> "DRY (Don't Repeat Yourself)"
- Lorsque le même code est utilisé de manière répétée, séparer cette partie en fonction ou en classe pour la réutiliser
- La modularisation pour réutiliser activement le code améliore la lisibilité, et s'il est nécessaire de modifier le code ultérieurement, il suffit de modifier une seule fois la fonction ou la classe concernée, ce qui facilite la maintenance
- En principe, l'idéal est qu'une fonction n'effectue qu'une seule tâche et non deux ou plus. Cependant, le code écrit en PS/CP est généralement un programme de petite taille effectuant des fonctions simples, donc il y a des limites à la réutilisation, et comme le temps est limité, il peut être difficile de suivre strictement ce principe comme dans la pratique.

### Utilisation de la bibliothèque standard
> "Don't reinvent the wheel"
- Lors de l'étude des algorithmes ou des structures de données, il est utile d'implémenter directement des structures de données comme les files ou les piles, ou des algorithmes de tri pour en comprendre les principes, mais sinon, il est préférable d'utiliser activement la bibliothèque standard
- La bibliothèque standard a déjà été utilisée et vérifiée d'innombrables fois, et elle est bien optimisée, donc elle est plus efficace que de l'implémenter soi-même
- Comme on peut utiliser une bibliothèque déjà existante, il n'est pas nécessaire de perdre du temps à implémenter directement un code ayant la même fonctionnalité, et il est également plus facile pour les autres membres de l'équipe de comprendre le code écrit lors de la collaboration

### Utilisation d'une nomenclature cohérente et claire
> "Follow standard conventions"
- Utiliser des noms de variables et de fonctions non ambigus
- Généralement, chaque langage de programmation a sa propre convention de nommage, donc il faut apprendre la convention de nommage utilisée dans la bibliothèque standard du langage utilisé et l'appliquer de manière cohérente lors de la déclaration de classes, fonctions, variables, etc.
- Nommer de manière à ce que la fonction de chaque variable, fonction et classe soit clairement visible, et si c'est un type booléen, dans quelles conditions il renvoie vrai (True)

### Normaliser toutes les données avant de les stocker
- Traiter toutes les données sous une forme cohérente et normalisée
- Si les mêmes données ont plus d'une forme, des bugs subtils difficiles à détecter peuvent se produire, comme de légères différences dans la représentation des chaînes de caractères ou des valeurs de hachage différentes
- Lors du stockage et du traitement de données telles que les fuseaux horaires, les chaînes de caractères, etc., il faut les convertir dans un format standard unique comme UTC, encodage UTF-8, etc. dès qu'elles sont reçues ou calculées. Il est préférable d'effectuer la normalisation dès le début dans le constructeur de la classe représentant ces données, ou d'effectuer immédiatement la normalisation dans la fonction qui reçoit les données.

### Séparer la logique du code et les données
- Ne pas mettre directement dans les instructions conditionnelles les données sans rapport avec la logique du code, mais les séparer dans un tableau distinct  
  ex) Il est préférable d'écrire comme dans le code ci-dessous plutôt que dans le code ci-dessus.

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