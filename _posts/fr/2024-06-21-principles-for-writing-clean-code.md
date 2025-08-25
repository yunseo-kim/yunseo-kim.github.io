---
title: Principes pour écrire un code de qualité
description: "Pourquoi écrire du code de qualité et comment y parvenir: principes KISS/DRY, modularisation, conventions de nommage, normalisation des données, exemples PS/CP et projets."
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## Pourquoi il est nécessaire d’écrire du bon code
Si l’on se contente d’écrire du code à la va-vite pour l’implémentation immédiate, la [Dette technique](/posts/Technical-debt/) peut enfler jusqu’à devenir ingérable et poser des problèmes de maintenance ultérieure. Ainsi, lors d’un projet de développement, écrire dès le départ un code lisible et facile à maintenir est évidemment essentiel.

Dans le cas de la résolution de problèmes algorithmiques (PS, Problem Solving) ou des concours de programmation (CP, Competitive Programming), on n’a généralement plus besoin de réutiliser le code une fois le problème ou la compétition terminés, et en CP il y a une contrainte de temps; d’aucuns avancent donc que la vitesse d’implémentation importe plus que la qualité du code. Pour répondre à cette question, il faut se demander pourquoi vous faites du PS/CP et quelle direction vous visez.

À mon sens, si l’on se limite aux aspects liés à la programmation (en dehors du développement de compétences générales en résolution de problèmes), PS/CP permet d’apprendre notamment:
- à expérimenter et assimiler divers algorithmes et structures de données sous des contraintes de temps d’exécution et de mémoire; ainsi, lors de projets réels, on développe une intuition sur l’algorithme/la structure adaptés à une situation donnée;
- à s’entraîner à écrire rapidement un code précis et robuste grâce à un retour objectif et immédiat sur l’exactitude, le temps d’exécution et l’usage mémoire après soumission;
- à comparer son code avec celui de programmeurs chevronnés et à en tirer des pistes d’amélioration;
- à écrire de manière répétée de petits programmes aux fonctionnalités semblables; surtout en s’exerçant seul, sans pression d’échéance, on peut soigner les détails et s’entraîner à écrire un code concis et de qualité.

On peut bien sûr pratiquer PS/CP par simple loisir, mais si l’objectif est d’améliorer ses compétences en programmation, alors «s’entraîner à écrire du bon code» constitue un avantage aussi important que les trois points précédents. Écrire un bon code ne vient pas naturellement: il faut s’y exercer de manière répétée. De plus, un code complexe et difficile à lire se débogue mal et est plus difficile à écrire correctement du premier coup; on finit souvent par perdre du temps en débogage inefficace et, au final, on n’implémente même pas si vite. Bien que PS/CP diffère du monde professionnel, négliger totalement la qualité au profit de l’implémentation immédiate me semble contre-productif pour les raisons évoquées; je préfère donc aussi en PS/CP viser un code concis et efficace. 

> Commentaire ajouté en 12024.12:  
> Vu la tendance actuelle, accumuler des bases en algorithmes et structures de données pour écrire des programmes efficaces et développer ses capacités de résolution de problèmes restera pertinent, mais au stade de l’implémentation, mieux vaut ne pas s’acharner à tout coder soi-même: exploitez activement l’IA (GitHub Copilot, Cursor, Windsurf, etc.) pour gagner du temps et consacrer l’économie à d’autres tâches ou à l’étude. Que l’on fasse du PS/CP pour développer des compétences générales ou pour le plaisir, personne n’y verra d’inconvénient; en revanche, investir du temps et des efforts uniquement pour s’exercer à taper du code via PS/CP me paraît désormais peu rentable. J’anticipe même que, dans les métiers du développement, l’importance des tests de codage comme épreuves d’embauche devrait sensiblement diminuer.
{: .prompt-warning }

## Principes pour écrire du bon code
Que le code soit écrit pour un concours ou pour le travail, les critères d’un bon code ne diffèrent pas tant que cela. Cet article présente les principaux principes généralement reconnus pour écrire du bon code. Toutefois, en PS/CP, certaines concessions peuvent être faites pour aller plus vite qu’en contexte professionnel; lorsque c’est le cas, je le préciserai.

### Écrire du code concis
> "KISS(Keep It Simple, Stupid)"

- Plus le code est court et concis, moins il risque de contenir des fautes de frappe ou des bugs simples, et plus le débogage est facile.
- Rédigez le code de manière à être compréhensible sans commentaires lorsque c’est possible; n’ajoutez des commentaires que lorsque c’est réellement nécessaire. Il vaut mieux compter sur une structure de code simple que sur des commentaires.
- Lorsque vous commentez, soyez clair et concis.
- Limitez à trois le nombre de paramètres d’une fonction; au-delà, regroupez-les dans un objet.
- Une forte imbrication des conditions dégrade la lisibilité; évitez d’augmenter la profondeur des conditionnelles.  
  ex) Par rapport au code ci-dessus, l’utilisation d’une clause de garde (Guard Clause) comme ci-dessous est plus lisible.  

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
- En PS/CP, on emploie parfois des astuces comme des macros C/C++ pour raccourcir le code et aller plus vite. C’est utile ponctuellement dans des concours serrés, mais cela reste spécifique à PS/CP; en règle générale, l’usage des macros en C++ est à éviter.  
  ex)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularisation du code
> "DRY(Don't Repeat Yourself)"

- Si vous répétez le même code, factorisez-le dans une fonction ou une classe pour le réutiliser.
- La modularisation améliore la lisibilité et facilite la maintenance: si une modification est nécessaire, il suffit d’ajuster la fonction ou la classe concernée.
- Idéalement, une fonction ne doit faire qu’une seule chose. Cependant, le code écrit en PS/CP étant de petite taille et à fonctionnalité simple, la réutilisation est limitée et le temps contraint; il peut être difficile d’appliquer les principes aussi strictement qu’en production.

### Utiliser la bibliothèque standard
> "Don't reinvent the wheel"

- Lors de l’apprentissage des algorithmes et structures de données, implémenter soi-même des structures comme les files/piles ou des tris pour comprendre les principes est utile; sinon, privilégiez la bibliothèque standard.
- Les bibliothèques standard sont largement utilisées et éprouvées, et bien optimisées; elles sont plus efficaces que des ré-implémentations maison.
- En réutilisant des bibliothèques existantes, vous évitez d’écrire inutilement du code redondant, gagnez du temps et facilitez la compréhension par vos coéquipiers.

### Utiliser des conventions de nommage cohérentes et explicites
> "Follow standard conventions"

- Employez des noms de variables et de fonctions non ambigus.
- Chaque langage a ses conventions de nommage; inspirez-vous de celles de sa bibliothèque standard et appliquez-les de manière cohérente pour les classes, fonctions et variables.
- Nommez de sorte qu’on comprenne clairement le rôle de chaque variable, fonction et classe; pour un type booléen, indiquez sans équivoque dans quelles conditions il vaut True.

### Normaliser toutes les données
- Traitez toutes les données dans un format unique et cohérent.
- Si une même donnée existe sous plusieurs formats, des bugs subtils et difficiles à traquer peuvent survenir (représentations textuelles légèrement différentes, valeurs de hachage distinctes, etc.).
- Pour les fuseaux horaires, les chaînes de caractères, etc., convertissez immédiatement à un format standard (UTC, encodage UTF-8, …). Réalisez la normalisation dès le constructeur de la classe représentant ces données, ou directement dans la fonction qui les reçoit.

### Séparer la logique du code et les données
- N’insérez pas dans des conditions des données étrangères à la logique; isolez-les dans une table dédiée.  
  ex) Il est préférable d’écrire comme ci-dessous plutôt que comme ci-dessus.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ~~~c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ~~~
