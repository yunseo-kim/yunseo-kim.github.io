---
title: Comment traduire automatiquement des articles avec l'API Claude 3.5 Sonnet (1) - Conception du prompt
description: Cet article traite de la conception d'un prompt pour la traduction multilingue de fichiers texte Markdown, et du processus d'automatisation en Python en utilisant une clé API obtenue auprès d'Anthropic et le prompt créé. Il s'agit du premier article de cette série, qui présente la méthode et le processus de conception du prompt.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introduction
J'ai récemment adopté l'API Claude 3.5 Sonnet d'Anthropic pour la traduction multilingue des articles de mon blog. Dans cette série, je vais expliquer pourquoi j'ai choisi l'API Claude 3.5 Sonnet, comment j'ai conçu le prompt, et comment j'ai implémenté l'automatisation via un script Python connecté à l'API.  
Cette série se compose de deux articles, et celui que vous lisez est le premier.
- Partie 1 : Introduction au modèle Claude 3.5 Sonnet, raisons de sa sélection, et ingénierie de prompt (cet article)
- Partie 2 : [Écriture et application d'un script d'automatisation Python utilisant l'API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## À propos de Claude 3.5 Sonnet
La série de modèles Claude 3 est disponible en trois versions selon leur taille : Haiku, Sonnet et Opus.  
![Classification des modèles Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Source de l'image : [Site officiel de l'API Anthropic Claude](https://www.anthropic.com/api)

Le 21 juin 12024 (selon le [calendrier holocène](https://en.wikipedia.org/wiki/Holocene_calendar)), Anthropic a dévoilé son dernier modèle de langage, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Selon Anthropic, il surpasse Claude 3 Opus en termes de capacités de raisonnement, tout en conservant le même coût et la même vitesse que Claude 3 Sonnet. Il est généralement considéré comme supérieur à GPT-4 dans les domaines de la rédaction, du raisonnement linguistique, de la compréhension multilingue et de la traduction.  
![Image de présentation de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Résultats des benchmarks de performance de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Source des images : [Site d'Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Ajout du 12024.10.31) Le 22 octobre 12024, Anthropic a annoncé une version améliorée de l'API Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") ainsi que Claude 3.5 Haiku. Cependant, en raison du [problème mentionné plus loin](#prévention-de-la-paresse-patch-halloween-120241031), ce blog utilise toujours l'API "claude-3-5-sonnet-20240620" d'origine.

## Pourquoi adopter Claude 3.5 pour la traduction d'articles
Il existe déjà des API de traduction commerciales comme Google Translate ou DeepL. Cependant, j'ai choisi d'utiliser un LLM pour la traduction car, contrairement aux services de traduction traditionnels, les modèles de langage permettent de fournir un contexte supplémentaire et des exigences spécifiques via la conception du prompt, comme l'objectif de l'article ou le sujet principal. Le modèle peut ainsi produire une traduction qui tient compte du contexte. Bien que DeepL et Google Translate offrent généralement d'excellentes qualités de traduction, ils peuvent produire des résultats moins naturels pour des textes longs sur des sujets spécialisés, car ils ne saisissent pas toujours bien le sujet ou le contexte global. Comme mentionné précédemment, Claude est considéré comme supérieur à GPT-4 en matière de rédaction, de raisonnement linguistique, de compréhension multilingue et de traduction. Mes propres tests ont confirmé que Claude produisait des traductions plus fluides que GPT-4o, ce qui le rend particulièrement adapté à la traduction d'articles techniques pour ce blog.

## Conception du prompt
### Principes de base pour formuler une demande
Pour obtenir des résultats satisfaisants d'un modèle de langage, il faut lui fournir un prompt approprié. La conception de prompt peut sembler intimidante, mais en réalité, "bien formuler une demande" suit les mêmes principes, que l'on s'adresse à un modèle de langage ou à un humain. Il suffit d'expliquer clairement la situation et la demande selon les principes journalistiques (qui, quoi, où, quand, pourquoi, comment), et d'ajouter des exemples concrets si nécessaire. Il existe de nombreux conseils et techniques pour la conception de prompt, mais la plupart découlent des principes fondamentaux décrits ci-dessous.

#### Ton général
De nombreux rapports indiquent que les modèles de langage produisent des réponses de meilleure qualité lorsque les prompts sont rédigés sur un ton poli plutôt qu'impératif. Comme dans les interactions sociales normales, où les gens sont plus susceptibles de répondre favorablement à des demandes polies qu'à des ordres autoritaires, les modèles de langage semblent imiter ce schéma de réponse humaine.

#### Attribution de rôle et explication du contexte (qui, pourquoi)
J'ai d'abord attribué à Claude 3.5 le rôle de "traducteur professionnel spécialisé dans les domaines techniques", et fourni des informations contextuelles sur l'utilisateur en tant que "blogueur en ingénierie qui écrit principalement sur les mathématiques, la physique et la science des données".

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Communication de la demande principale (quoi)
Ensuite, j'ai demandé de traduire le texte au format markdown fourni par l'utilisateur de {source_lang} vers {target_lang} tout en préservant le format.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Lors de l'appel à l'API Claude, les variables {source_lang} et {target_lang} dans le prompt sont remplacées par les langues source et cible via la fonctionnalité f-string de Python.
{: .prompt-info }

#### Spécification des exigences et exemples (comment)
Pour des tâches simples, les étapes précédentes peuvent suffire, mais pour des tâches complexes, des explications supplémentaires sont nécessaires.

Lorsque les exigences sont complexes et multiples, il est préférable de les présenter sous forme de liste pour améliorer la lisibilité et faciliter la compréhension. Fournir des exemples est également utile.
Dans ce cas, j'ai ajouté les conditions suivantes :

##### Traitement du YAML front matter
Les articles de blog Jekyll en markdown commencent par un YAML front matter qui contient des informations comme 'title', 'description', 'categories' et 'tags'. Par exemple, le YAML front matter de cet article est le suivant :

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

Lors de la traduction d'un article, les balises 'title' et 'description' doivent être traduites, mais pour maintenir la cohérence des URL, les noms des 'categories' et 'tags' doivent rester en anglais. J'ai donc ajouté l'instruction suivante pour que seuls 'title' et 'description' soient traduits :

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> J'ai ajouté la phrase "under any circumstances, regardless of the language you are translating to" pour souligner qu'**aucune exception** n'est permise concernant la modification des autres balises du YAML front matter.
{: .prompt-tip }

##### Traitement des parties du texte original écrites dans d'autres langues
Lorsque je rédige en coréen, j'inclus parfois l'expression anglaise entre parenthèses pour les termes techniques, comme '*중성자 감쇠 (Neutron Attenuation)*'. Pour assurer une cohérence dans la traduction de ces expressions, j'ai établi les directives suivantes :
- Pour les termes techniques :
  - Lors de la traduction vers des langues non basées sur l'alphabet romain comme le japonais, maintenir le format 'expression traduite(expression anglaise)'.
  - Lors de la traduction vers des langues basées sur l'alphabet romain comme l'espagnol, le portugais ou le français, permettre soit l'expression traduite seule, soit le format 'expression traduite(expression anglaise)', laissant Claude choisir l'option la plus appropriée.
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
Certains articles contiennent des liens vers d'autres articles. Pendant la phase de test, sans directive spécifique, le modèle traduisait parfois la partie chemin de l'URL, ce qui cassait les liens internes. J'ai résolu ce problème en ajoutant cette instruction :

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Produire uniquement le résultat de la traduction
Enfin, j'ai demandé que la réponse contienne uniquement le résultat de la traduction, sans texte supplémentaire :

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Techniques supplémentaires de conception de prompt
Contrairement aux demandes adressées à des humains, il existe des techniques spécifiques qui s'appliquent aux modèles de langage.
Voici quelques conseils généralement utiles, principalement tirés du [guide officiel d'ingénierie de prompt d'Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) :

#### Structuration avec des balises XML
J'ai déjà utilisé cette technique tout au long du prompt. Pour les prompts complexes contenant divers contextes, instructions, formats et exemples, l'utilisation de balises XML comme `<instructions>`, `<example>`, `<format>` aide le modèle à interpréter correctement le prompt et à produire une sortie de haute qualité. Le dépôt GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) contient une bonne liste de balises XML utiles pour la rédaction de prompts.

#### Technique de raisonnement par étapes (CoT, Chain of Thinking)
Pour les tâches nécessitant un raisonnement substantiel, comme la résolution de problèmes mathématiques ou la rédaction de documents complexes, guider le modèle pour qu'il décompose le problème en étapes peut considérablement améliorer ses performances. Cependant, cela peut augmenter le temps de réponse et n'est pas toujours utile pour toutes les tâches.

#### Technique de chaînage de prompts (prompt chaining)
Pour les tâches complexes, un seul prompt peut être insuffisant. Dans ce cas, on peut diviser le flux de travail en plusieurs étapes, chacune avec un prompt spécialisé, et utiliser la réponse d'une étape comme entrée pour l'étape suivante. Cette technique s'appelle le chaînage de prompts.

#### Pré-remplissage de la première partie de la réponse
En fournissant le début de la réponse attendue dans le prompt, on peut éviter les salutations inutiles ou forcer une réponse dans un format spécifique comme XML ou JSON. [Pour l'API Claude, on peut utiliser cette technique en soumettant un message `Assistant` avec le message `User` lors de l'appel.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prévention de la paresse (Patch Halloween 12024.10.31)
Bien que j'aie apporté quelques améliorations mineures au prompt après la rédaction initiale de cet article, le système d'automatisation a fonctionné sans problème majeur pendant 4 mois.

Cependant, à partir du 31 octobre 12024 vers 18h (heure coréenne), un problème étrange est apparu : lors de la traduction de nouveaux articles, le modèle ne traduisait que la partie "TL;DR" initiale puis arrêtait arbitrairement la traduction.

J'ai traité les causes probables de ce problème et sa solution dans [un article séparé](/posts/does-ai-hate-to-work-on-halloween), que je vous invite à consulter.

### Prompt final
Voici le résultat final de la conception du prompt :

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
