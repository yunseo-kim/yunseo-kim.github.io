---
title: Comment traduire automatiquement des articles avec l'API Claude 3.5 Sonnet (1) - Conception du prompt
description: >-
  Cet article traite de la conception d'un prompt pour la traduction multilingue de fichiers texte en markdown, et du processus d'automatisation en Python en utilisant la clé API fournie par Anthropic et le prompt créé. Ce post est le premier d'une série et présente la méthode et le processus de conception du prompt.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introduction
J'ai récemment adopté l'API Claude 3.5 Sonnet d'Anthropic pour la traduction multilingue des articles du blog. Dans cette série, nous aborderons les raisons du choix de l'API Claude 3.5 Sonnet, la méthode de conception du prompt, ainsi que la mise en œuvre de l'automatisation via l'API avec un script Python.  
La série se compose de deux articles, et celui-ci est le premier.
- Partie 1 : Présentation du modèle Claude 3.5 Sonnet, raisons de sa sélection et ingénierie des prompts (cet article)
- Partie 2 : [Création et application d'un script d'automatisation Python utilisant l'API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## À propos de Claude 3.5 Sonnet
Les modèles de la série Claude 3 sont disponibles en trois versions selon leur taille : Haiku, Sonnet et Opus.  
![Classification des niveaux de modèles Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Source de l'image : [Site officiel de l'API Anthropic Claude](https://www.anthropic.com/api)

Le 21 juin 2024 (heure coréenne), Anthropic a dévoilé son dernier modèle de langage, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Selon Anthropic, il surpasse les performances de raisonnement de Claude 3 Opus avec les mêmes coûts et vitesses que Claude 3 Sonnet, et il est généralement considéré comme supérieur à son concurrent GPT-4 en matière de rédaction, de raisonnement linguistique, de compréhension multilingue et de traduction.  
![Image de présentation de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Résultats des tests de performance de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Source des images : [Site web d'Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Ajout du 31.10.2024) Le 22 octobre 2024, Anthropic a annoncé une version améliorée de l'API Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") et Claude 3.5 Haiku. Cependant, en raison du [problème mentionné plus loin](#prévention-de-la-paresse-patch-halloween-31102024), ce blog utilise toujours l'API "claude-3-5-sonnet-20240620" d'origine.

## Pourquoi adopter Claude 3.5 pour la traduction d'articles
Il existe déjà des API de traduction commerciales comme Google Translate ou DeepL, sans nécessairement recourir à des modèles de langage comme Claude 3.5 ou GPT-4. La raison pour laquelle j'ai choisi d'utiliser un LLM pour la traduction est que, contrairement aux autres services de traduction commerciaux, l'utilisateur peut fournir des informations contextuelles supplémentaires et des exigences spécifiques au modèle via la conception du prompt, comme l'objectif de rédaction ou les thèmes principaux, et le modèle peut adapter sa traduction en conséquence. Bien que DeepL et Google Translate offrent généralement une excellente qualité de traduction, ils peuvent produire des résultats moins naturels lors de la traduction de longs textes sur des sujets spécialisés, en raison de leur difficulté à bien saisir le sujet et le contexte global. Claude, en particulier, est souvent considéré comme supérieur à son concurrent GPT-4 en matière de rédaction, de raisonnement linguistique, de compréhension multilingue et de traduction, et mes tests simples ont également montré une qualité de traduction plus fluide que GPT-4, ce qui m'a fait penser qu'il serait approprié pour la traduction des articles d'ingénierie publiés sur ce blog.

## Conception du prompt
### Principes de base pour faire une demande
Pour obtenir des résultats satisfaisants d'un modèle de langage, il faut fournir un prompt approprié. La conception de prompts peut sembler intimidante, mais en réalité, "la façon de bien faire une demande" n'est pas très différente, que ce soit à un modèle de langage ou à un humain. Il suffit d'expliquer clairement la situation actuelle et les demandes selon les 5W1H, et d'ajouter quelques exemples concrets si nécessaire. Il existe de nombreux conseils et techniques pour la conception de prompts, mais la plupart découlent des principes de base décrits ci-après.

#### Ton général
De nombreux rapports indiquent que le modèle de langage produit des réponses de meilleure qualité lorsque le prompt est rédigé sur un ton poli plutôt qu'autoritaire. De même que dans la société, les gens sont plus susceptibles d'effectuer une tâche avec soin lorsqu'on la leur demande poliment plutôt que sur un ton autoritaire, les modèles de langage semblent avoir appris et imiter ces schémas de réponse humaine.

#### Attribution des rôles et explication du contexte (qui, pourquoi)
Tout d'abord, j'ai attribué à Claude 3.5 le rôle de "traducteur technique professionnel" et fourni des informations contextuelles sur l'utilisateur en tant que "blogueur en ingénierie qui écrit principalement sur les mathématiques, la physique et la science des données".

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Communication des demandes générales (quoi)
Ensuite, j'ai demandé de traduire le texte au format markdown fourni de {source_lang} vers {target_lang} tout en préservant le format.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Lors de l'appel à l'API Claude, les variables de langue source et cible sont insérées respectivement aux emplacements {source_lang} et {target_lang} via la fonctionnalité f-string du script Python.
{: .prompt-info }

#### Spécification des exigences et exemples (comment)
Pour les tâches simples, les étapes précédentes peuvent suffire pour obtenir les résultats souhaités, mais pour les tâches plus complexes, des explications supplémentaires peuvent être nécessaires.

Lorsque les exigences sont complexes et multiples, il est plus lisible et compréhensible (tant pour les humains que pour les modèles de langage) de les présenter sous forme de liste plutôt que de les décrire en détail. De plus, fournir des exemples peut être utile si nécessaire.
Dans ce cas, j'ai ajouté les conditions suivantes.

##### Traitement du YAML front matter
Le YAML front matter au début des articles markdown rédigés pour le blog Jekyll contient les informations 'title', 'description', 'categories' et 'tags'. Par exemple, le YAML front matter de cet article est le suivant :

```yaml
---
title: Claude 3.5 Sonnet API로 포스트 자동 번역하는 법
description: \>-
  최근 공개된 Claude 3.5 Sonnet 모델을 간략히 소개하고, 본 블로그 포스트의 다국어 번역 작업에 적용하기 위해 프롬프트를 디자인한 과정과 완성한 프롬프트 결과물을 공유한다.
  그리고 Anthropic으로부터 발급받은 API 키와 앞서 작성한 프롬프트를 적용하여 Python으로 번역 자동화 스크립트를 작성하고 활용하는 방법을 소개한다.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
```

Lors de la traduction d'un article, bien que le titre (title) et la description (description) doivent être traduits dans différentes langues, il est préférable de maintenir les noms des catégories (categories) et des tags (tags) en anglais pour la cohérence des URL et la facilité de maintenance. J'ai donc ajouté l'instruction suivante pour ne pas traduire les tags autres que 'title' et 'description'.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> J'ai ajouté la phrase "under any circumstances, regardless of the language you are translating to" pour souligner que les autres tags du YAML front matter ne doivent **en aucun cas** être modifiés.
{: .prompt-tip }

##### Traitement du texte source contenant d'autres langues
Lors de la rédaction en coréen, il est courant d'inclure l'expression anglaise entre parenthèses lors de l'introduction d'un concept ou de l'utilisation de termes techniques, comme dans "중성자 감쇠 (Neutron Attenuation)". Pour traiter ces expressions de manière cohérente, j'ai établi les directives détaillées suivantes :
- Pour les termes techniques :
  - Pour les langues non basées sur l'alphabet romain comme le japonais, maintenir le format 'expression traduite(expression anglaise)'.
  - Pour les langues basées sur l'alphabet romain comme l'espagnol, le portugais ou le français, permettre soit l'expression traduite seule, soit le format combiné 'expression traduite(expression anglaise)', laissant Claude choisir l'option la plus appropriée.
- Pour les noms propres, l'orthographe originale doit être préservée d'une manière ou d'une autre dans la traduction.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
  2. it may be a proper noun such as a person's name or a place name. \n\
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
  <if>it is the first case, and the target language is not a Roman alphabet-based language, \
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
      You can choose whichever you think is more appropriate.</example>\n\
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
      French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Traitement des liens vers d'autres articles
Certains articles contiennent des liens vers d'autres articles, et pendant la phase de test, sans directives spécifiques à ce sujet, le modèle interprétait souvent la partie chemin de l'URL comme devant être traduite, ce qui cassait les liens internes. Ce problème a été résolu en ajoutant cette instruction au prompt.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Ne produire que le résultat de la traduction
Enfin, j'ai ajouté cette phrase pour que seul le résultat de la traduction soit produit, sans autres commentaires.

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Techniques supplémentaires de conception de prompts
Cependant, il existe des techniques supplémentaires spécifiques aux modèles de langage, différentes de celles utilisées pour faire des demandes aux humains.
Bien qu'il existe de nombreuses ressources utiles sur le web à ce sujet, voici quelques conseils représentatifs qui peuvent être utilisés de manière générale.  
Ces informations sont principalement basées sur le [guide d'ingénierie des prompts de la documentation officielle d'Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Structuration avec des balises XML
En fait, nous avons déjà utilisé cette technique jusqu'à présent. Pour les prompts complexes contenant divers contextes, instructions, formats et exemples, l'utilisation appropriée de balises XML comme `<instructions>`, `<example>`, `<format>` aide grandement le modèle de langage à interpréter correctement le prompt et à produire des résultats de haute qualité conformes aux intentions. Le dépôt GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) contient une bonne compilation de balises XML utiles pour la rédaction de prompts.

#### Technique du raisonnement par étapes (CoT, chain of thinking)
Pour les tâches nécessitant un niveau significatif de raisonnement, comme la résolution de problèmes mathématiques ou la rédaction de documents complexes, guider le modèle de langage à penser par étapes peut grandement améliorer ses performances. Cependant, cela peut augmenter le temps de réponse, et cette technique n'est pas toujours utile pour toutes les tâches.

#### Technique du chaînage de prompts (prompt chaining)
Pour les tâches complexes, un seul prompt peut avoir ses limites. Dans ce cas, on peut envisager de diviser dès le départ l'ensemble du flux de travail en plusieurs étapes, en présentant des prompts spécialisés pour chaque étape et en utilisant la réponse de l'étape précédente comme entrée pour l'étape suivante. Cette technique est appelée chaînage de prompts (prompt chaining).

#### Pré-remplissage du début de la réponse
Lors de la saisie du prompt, on peut pré-remplir le début de la réponse attendue pour éviter les salutations inutiles ou forcer une réponse dans un format spécifique comme XML ou JSON. [Dans le cas de l'API Claude, cette technique peut être utilisée en soumettant un message `Assistant` en plus du message `User` lors de l'appel.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prévention de la paresse (Patch Halloween 31.10.2024)
Bien que j'aie apporté quelques améliorations mineures au prompt et précisé certaines instructions depuis la rédaction initiale de cet article, le système d'automatisation a fonctionné sans problèmes majeurs pendant 4 mois.

Cependant, à partir d'environ 18h00 (heure coréenne) le 31.10.2024, lors de la traduction de nouveaux articles, une anomalie persistante est apparue où seule la partie 'TL;DR' initiale de l'article était traduite avant que la traduction ne soit arbitrairement interrompue.

Les causes probables de ce problème et ses solutions sont traitées dans [un article séparé](/posts/does-ai-hate-to-work-on-halloween), veuillez vous y référer.

### Le prompt finalisé
Voici le résultat de la conception du prompt après avoir suivi les étapes ci-dessus.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role> The customer's request is as follows:\n\n \
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task> \
In the provided markdown format text, \n\
  - <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
  - <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases. \n\
    1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it. \n\
    2. it may be a proper noun such as a person's name or a place name. \n\
    After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:\n\
    <if>it is the first case, and the target language is not a Roman alphabet-based language, \
    please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>\n\
      - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>\n\
      - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>\n\
    <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>\n\
      - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'. \
        You can choose whichever you think is more appropriate.</example>\n\
      - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable \
        French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>\n\
    <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
      - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as 'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
        In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
        redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
    </condition>\n\n\
  - <condition><if>the provided text contains links in markdown format, \
    please translate the link text and the fragment part of the URL into {target_lang}, \
    but keep the path part of the URL intact.</if> \n\
    - <example> the German translation of '[중성자 상호작용과 반응단면적]\
      (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
      would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
      #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

## Pour aller plus loin
Suite dans la [Partie 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
