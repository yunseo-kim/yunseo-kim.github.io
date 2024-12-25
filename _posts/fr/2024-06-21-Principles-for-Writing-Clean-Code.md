---
title: Principes pour écrire du bon code
description: Découvrez la nécessité d'écrire du bon code et les principaux principes
  généralement appliqués pour y parvenir.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.jpg
---
## La nécessité d'écrire du bon code
Si l'on se contente d'écrire rapidement du code pour une implémentation immédiate, la [dette technique](/posts/Technical-debt/) peut s'accumuler à un niveau ingérable, ce qui peut poser des problèmes de maintenance ultérieurement. Par conséquent, il est inutile de souligner l'importance d'écrire dès le départ un code lisible et facile à maintenir lors de la réalisation d'un projet de développement.

Dans le cas de la résolution de problèmes algorithmiques (PS, Problem Solving) ou de la programmation compétitive (CP, Competitive Programming), on dit souvent que le code utilisé pour résoudre le problème n'est généralement pas réutilisé après la fin du problème ou de la compétition, et en particulier dans le cas de la CP, qu'une implémentation rapide est plus importante que l'écriture d'un bon code en raison des contraintes de temps. Pour répondre à cette question, il est nécessaire de réfléchir à ce pour quoi on fait du PS/CP et quelle direction on souhaite prendre.

Personnellement, je pense que les points que l'on peut apprendre à travers le PS/CP sont les suivants :
- On peut utiliser et maîtriser divers algorithmes et structures de données dans le processus de résolution de problèmes dans les limites de temps d'exécution et de mémoire données, ce qui permet d'acquérir une intuition sur les algorithmes et structures de données à utiliser dans certaines situations lors de la réalisation de projets réels.
- Après avoir écrit et soumis le code, on peut recevoir immédiatement un retour objectif sur la justesse/l'erreur, le temps d'exécution et l'utilisation de la mémoire, ce qui permet de s'entraîner à écrire rapidement et habilement un code précis sans rien manquer.
- On peut voir le code écrit par d'autres experts, le comparer avec son propre code et trouver des points d'amélioration.
- Comme on écrit de manière répétitive du code de petite taille et aux fonctionnalités similaires par rapport aux projets de développement réels, on peut s'entraîner à écrire un code concis et de qualité en prêtant attention aux détails sans être contraint par des délais (surtout si on s'entraîne seul au PS).

Bien qu'il puisse y avoir des cas où l'on pratique le PS/CP simplement comme un passe-temps, si on le fait indirectement pour améliorer ses compétences en programmation, le dernier point "s'entraîner à écrire du bon code" est un avantage tout aussi important que les trois premiers. Écrire du bon code ne vient pas naturellement dès le début, mais nécessite une pratique répétée et constante. De plus, un code complexe et difficile à lire est difficile à déboguer et n'est pas facile à écrire correctement du premier coup, même pour soi-même. Par conséquent, si l'on perd du temps dans un débogage inefficace, on finit souvent par ne pas implémenter si rapidement que ça. Bien que le PS/CP soit bien sûr très différent du travail réel, ne pas du tout se soucier d'écrire du bon code et se précipiter sur l'implémentation immédiate est, pour les raisons mentionnées ci-dessus, une inversion des priorités. C'est pourquoi je pense personnellement qu'il est préférable d'écrire un code concis et efficace même en PS/CP.

> Commentaire ajouté en décembre 2024 :  
> Vu l'ambiance actuelle, à moins d'être spécialisé en informatique et de faire du développement son métier, si on veut utiliser la programmation comme un outil pour l'analyse numérique ou l'interprétation de données expérimentales, il serait peut-être préférable d'utiliser activement l'IA comme GitHub Copilot, Cursor, Windsurf, etc. pour gagner du temps et consacrer ce temps gagné à étudier autre chose. Si on apprécie le PS/CP comme un passe-temps en soi, personne ne va l'en empêcher, mais consacrer du temps et des efforts au PS/CP pour s'entraîner à l'écriture de code semble maintenant avoir un rapport coût-bénéfice assez faible. Même dans le cas des métiers du développement, je m'attends à ce que l'importance des tests de codage en tant qu'examen d'embauche diminue probablement considérablement par rapport à avant.
{: .prompt-warning }

## Principes pour écrire du bon code
Que ce soit pour le code écrit en compétition ou dans la pratique professionnelle, les conditions pour qu'un code soit considéré comme bon ne sont pas très différentes. Cet article traite des principaux principes généralement appliqués pour écrire du bon code. Cependant, en PS/CP, il peut y avoir des compromis relatifs par rapport à la pratique professionnelle pour une implémentation rapide, et ces cas seront mentionnés séparément dans l'article.

### Écrire un code concis
> "KISS (Keep It Simple, Stupid)"

- Plus le code est court et concis, moins il y a de risques de fautes de frappe ou de bugs simples, et plus le débogage est facile.
- Écrire autant que possible de manière à ce que le code puisse être facilement interprété sans commentaires supplémentaires, et n'ajouter des commentaires que lorsque c'est vraiment nécessaire pour des explications détaillées. Il est préférable de maintenir la structure du code elle-même concise plutôt que de s'appuyer sur des commentaires.
- Si des commentaires sont écrits, ils doivent être clairs et concis.
- Limiter le nombre d'arguments passés à une fonction à 3 ou moins, et si plus d'arguments doivent être passés ensemble, les regrouper en un seul objet.
- La profondeur (depth) des instructions conditionnelles qui s'emboîtent en double ou triple diminue la lisibilité, donc il faut éviter autant que possible d'augmenter la profondeur des instructions conditionnelles.
  ex) Le code ci-dessous utilisant la clause de garde (Guard Clause) est plus avantageux en termes de lisibilité que le code ci-dessus.

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
- Cependant, en PS/CP, pour aller plus loin et réduire la longueur du code afin de l'écrire rapidement, on utilise parfois l'astuce des macros en C/C++. C'est utile à utiliser occasionnellement pour les compétitions où le temps est limité, mais c'est une méthode qui ne fonctionne que pour le PS/CP, et en général, l'utilisation de macros en C++ doit être évitée.
  ex)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularisation du code
> "DRY (Don't Repeat Yourself)"

- Si le même code est utilisé de manière répétée, séparer cette partie en fonction ou en classe pour la réutiliser.
- La modularisation pour réutiliser activement le code améliore la lisibilité, et s'il est nécessaire de modifier le code ultérieurement, il suffit de modifier la fonction ou la classe concernée une seule fois, ce qui facilite la maintenance.
- En principe, l'idéal est qu'une fonction n'effectue qu'une seule tâche et non deux ou plus. Cependant, le code écrit en PS/CP est généralement un programme de petite taille effectuant des fonctions simples, donc il y a des limites à la réutilisation, et comme le temps est limité, il peut être difficile de suivre strictement ce principe comme dans la pratique professionnelle.

### Utilisation des bibliothèques standard
> "Don't reinvent the wheel"

- Lors de l'étude des algorithmes ou des structures de données, il est utile d'implémenter directement des structures de données comme les files ou les piles, ou des algorithmes de tri pour comprendre leurs principes, mais sinon, il est préférable d'utiliser activement les bibliothèques standard.
- Les bibliothèques standard ont déjà été utilisées et vérifiées d'innombrables fois, et sont bien optimisées, ce qui les rend plus efficaces que de les réimplémenter soi-même.
- Comme on peut utiliser des bibliothèques existantes, il n'est pas nécessaire de perdre du temps à implémenter directement du code ayant la même fonctionnalité, et lors de la collaboration, il est plus facile pour les autres membres de l'équipe de comprendre le code écrit.

### Utilisation d'une nomenclature cohérente et claire
> "Follow standard conventions"

- Utiliser des noms de variables et de fonctions non ambigus.
- Généralement, chaque langage de programmation a ses propres conventions de nommage, donc il faut apprendre les conventions de nommage utilisées dans la bibliothèque standard du langage utilisé et les appliquer de manière cohérente lors de la déclaration de classes, fonctions, variables, etc.
- Nommer de manière à ce que la fonction de chaque variable, fonction et classe soit clairement visible, et si c'est un type booléen, dans quelles conditions il renvoie vrai (True).

### Normaliser toutes les données avant de les stocker
- Traiter toutes les données sous une forme cohérente et normalisée.
- Si les mêmes données ont plus d'une forme, des bugs subtils et difficiles à détecter peuvent survenir, comme de légères différences dans la représentation des chaînes de caractères ou des valeurs de hachage différentes.
- Lors du stockage et du traitement de données telles que les fuseaux horaires, les chaînes de caractères, etc., il faut les convertir dans un format standard unique comme UTC, encodage UTF-8, etc. dès qu'elles sont reçues ou calculées. Il est préférable d'effectuer la normalisation dès le début dans le constructeur de la classe représentant ces données, ou dans la fonction qui reçoit les données.

### Séparer la logique du code et les données
- Ne pas mettre directement dans les instructions conditionnelles les données qui n'ont rien à voir avec la logique du code, mais les séparer dans un tableau distinct.
  ex) Il est préférable d'écrire comme dans le code ci-dessous plutôt que dans celui du dessus.

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
