---
title: Comment traduire automatiquement des articles avec l'API Claude 3.5 Sonnet (1)
description: >-
  Présentation brève du modèle Claude 3.5 Sonnet récemment publié, partage du processus de conception du prompt pour l'appliquer à la traduction multilingue des articles de ce blog, et présentation du résultat final du prompt.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introduction
J'ai récemment introduit l'API Claude 3.5 Sonnet d'Anthropic pour la traduction multilingue des articles de blog. Je souhaite aborder les raisons pour lesquelles j'ai choisi l'API Claude 3.5 Sonnet, la méthode de conception du prompt, ainsi que la méthode d'implémentation de l'API et d'automatisation via un script Python. Étant donné l'étendue du contenu à couvrir, il s'agira d'une série plutôt que d'un seul article, et ceci est le premier article de la série.

## À propos de Claude 3.5 Sonnet
Les modèles de la série Claude 3 sont disponibles en versions Haiku, Sonnet et Opus selon la taille du modèle.  
![Distinction des niveaux de modèles Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Source de l'image : [Page officielle de l'API Claude d'Anthropic](https://www.anthropic.com/api)

Et le 21 juin 2024 à l'heure coréenne, Anthropic a dévoilé son dernier modèle de langage, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Selon l'annonce d'Anthropic, il surpasse les performances d'inférence de Claude 3 Opus avec le même coût et la même vitesse que Claude 3 Sonnet existant, et il est généralement considéré comme ayant un avantage par rapport à son concurrent GPT-4 dans les domaines de la rédaction, du raisonnement linguistique, de la compréhension multilingue et de la traduction.  
![Image de présentation de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Résultats des tests de performance de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Source des images : [Site web d'Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

## Pourquoi j'ai adopté Claude 3.5 pour la traduction d'articles
Même sans utiliser des modèles de langage comme Claude 3.5 ou GPT-4, il existe des API de traduction commerciales existantes comme Google Translate ou DeepL. Malgré cela, j'ai décidé d'utiliser un LLM à des fins de traduction car, contrairement aux autres services de traduction commerciaux, l'utilisateur peut fournir des informations contextuelles supplémentaires ou des exigences au-delà du texte principal, telles que l'objectif de rédaction ou les principaux sujets de l'article, grâce à la conception du prompt, et le modèle peut fournir une traduction qui tient compte du contexte en conséquence. Bien que DeepL et Google Translate offrent généralement une excellente qualité de traduction, ils ont tendance à produire des résultats relativement peu naturels lors de la traduction de longs textes sur des sujets spécialisés plutôt que des conversations quotidiennes, en raison de leur limitation à bien saisir le sujet et le contexte global de l'article. En particulier, comme mentionné précédemment, Claude est considéré comme supérieur à son concurrent GPT-4 dans les domaines de la rédaction, du raisonnement linguistique, de la compréhension multilingue et de la traduction, j'ai donc jugé qu'il était approprié pour la tâche de traduire les articles d'ingénierie publiés sur ce blog en plusieurs langues.

## Conception du prompt
### Principes de base de la conception du prompt
Pour obtenir des résultats satisfaisants et conformes à l'objectif d'un modèle de langage, il est nécessaire de fournir un prompt approprié. Bien que la conception de prompt puisse sembler intimidante, en réalité, "la méthode pour bien faire une demande" n'est pas très différente, que l'interlocuteur soit un modèle de langage ou une personne, donc l'aborder de ce point de vue n'est pas si difficile. Il est bon d'expliquer clairement la situation actuelle et les demandes selon les six questions de base (qui, quoi, où, quand, pourquoi, comment), et d'ajouter quelques exemples spécifiques si nécessaire. Il existe de nombreux conseils et techniques pour la conception de prompt, mais la plupart découlent des principes de base mentionnés ci-dessus.

### Attribution de rôle et explication de la situation (qui, pourquoi)
Tout d'abord, j'ai attribué à Claude 3.5 le rôle de "traducteur technique professionnel" et fourni des informations contextuelles sur l'utilisateur en tant que "blogueur en ingénierie qui écrit principalement sur les mathématiques, la physique et la science des données".
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Transmission de la demande générale (quoi)
Ensuite, j'ai demandé de traduire le texte au format markdown fourni par l'utilisateur de {source_lang} vers {target_lang} tout en préservant le format.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Lors de l'appel à l'API Claude, les emplacements {source_lang} et {target_lang} dans le prompt sont remplacés respectivement par les variables de langue source et cible via la fonctionnalité f-string du script Python.
{: .prompt-info }

### Spécification des exigences et exemples (comment)
Jusqu'à l'étape précédente, il est parfois suffisant pour obtenir le résultat souhaité, mais pour des tâches plus complexes, des explications supplémentaires peuvent être nécessaires. Dans ce cas, j'ai ajouté les conditions suivantes.

#### Traitement lorsque le texte source contient une langue autre que la langue de départ
Lors de la rédaction du texte original en coréen, il est fréquent d'inclure l'expression anglaise entre parenthèses lorsqu'on introduit pour la première fois la définition d'un concept ou qu'on utilise certains termes techniques, comme dans "*중성자 감쇠 (Neutron Attenuation)*". Lors de la traduction de telles expressions, il y avait un problème d'incohérence dans la méthode de traduction, parfois en conservant les parenthèses et parfois en omettant l'anglais entre parenthèses, j'ai donc ajouté la phrase suivante au prompt.
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Traitement des liens vers d'autres articles
Certains articles contiennent des liens vers d'autres articles, et il y avait souvent un problème où la partie du chemin de l'URL était interprétée comme devant être traduite, ce qui brisait les liens internes. Ce problème a été résolu en ajoutant cette phrase au prompt.
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Ne produire que le résultat de la traduction comme réponse
Enfin, pour s'assurer que seul le résultat de la traduction est produit comme réponse sans ajouter d'autres commentaires, la phrase suivante est présentée.
> The output should only contain the translated text.

### Prompt finalisé
Le résultat de la conception du prompt après ces étapes est le suivant :
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.