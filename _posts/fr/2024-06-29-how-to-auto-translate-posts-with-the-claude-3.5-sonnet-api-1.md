---
title: Comment traduire automatiquement des articles avec l'API Claude 3.5 Sonnet (1) - Conception du prompt
description: Cet article aborde la conception d'un prompt pour la traduction multilingue de fichiers texte en markdown, ainsi que le processus d'automatisation du travail en Python en utilisant une clé API obtenue auprès d'Anthropic et le prompt créé. Il s'agit du premier article de cette série, qui présente la méthode et le processus de conception du prompt.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introduction
J'ai récemment adopté l'API Claude 3.5 Sonnet d'Anthropic pour la traduction multilingue des articles de blog. Dans cette série, je vais expliquer les raisons du choix de l'API Claude 3.5 Sonnet, la méthode de conception du prompt, ainsi que la mise en œuvre de l'automatisation via l'API et un script Python.  
La série se compose de deux articles, et celui-ci est le premier de la série.
- Partie 1 : Présentation du modèle Claude 3.5 Sonnet, raisons de sa sélection, et ingénierie du prompt (cet article)
- Partie 2 : [Rédaction et application d'un script d'automatisation Python utilisant l'API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## À propos de Claude 3.5 Sonnet
Les modèles de la série Claude 3 sont disponibles en versions Haiku, Sonnet et Opus, selon la taille du modèle.  
![Différenciation des niveaux de modèles Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Source de l'image : [Page officielle de l'API Claude d'Anthropic](https://www.anthropic.com/api)

Le 21 juin 12024 (selon le [calendrier holocène](https://fr.wikipedia.org/wiki/Calendrier_holoc%C3%A8ne)), heure coréenne, Anthropic a dévoilé son dernier modèle de langage, [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Selon l'annonce d'Anthropic, il surpasse les performances d'inférence de Claude 3 Opus avec le même coût et la même vitesse que Claude 3 Sonnet. Il est généralement considéré comme ayant un avantage par rapport à son concurrent GPT-4 dans les domaines de la rédaction, du raisonnement linguistique, de la compréhension multilingue et de la traduction.  
![Image de présentation de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Résultats des tests de performance de Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Source des images : [Site web d'Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Ajout du 31.10.12024) Le 22 octobre 12024, Anthropic a annoncé une version améliorée de l'API Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") et Claude 3.5 Haiku. Cependant, en raison du [problème mentionné plus loin](#prévention-de-la-paresse-patch-halloween-du-31102024), ce blog utilise toujours l'API "claude-3-5-sonnet-20240620" existante.

## Pourquoi j'ai adopté Claude 3.5 pour la traduction d'articles
Même sans utiliser des modèles de langage comme Claude 3.5 ou GPT-4, il existe déjà des API de traduction commerciales comme Google Translate ou DeepL. Malgré cela, j'ai décidé d'utiliser un LLM pour la traduction car, contrairement aux autres services de traduction commerciaux, l'utilisateur peut fournir au modèle des informations contextuelles supplémentaires ou des exigences spécifiques, telles que l'objectif de rédaction ou les principaux sujets de l'article, grâce à la conception du prompt. Le modèle peut ensuite fournir une traduction qui tient compte de ce contexte. Bien que DeepL et Google Translate offrent généralement une excellente qualité de traduction, ils ont tendance à produire des résultats moins naturels lors de la traduction de longs textes sur des sujets spécialisés, plutôt que des conversations quotidiennes, en raison de leur difficulté à bien saisir le sujet et le contexte global de l'article. En particulier, comme mentionné précédemment, Claude est généralement considéré comme supérieur à son concurrent GPT-4 dans les domaines de la rédaction, du raisonnement linguistique, de la compréhension multilingue et de la traduction. Lors de tests simples, j'ai constaté que Claude produisait des traductions plus fluides que GPT-4. J'ai donc jugé qu'il était approprié pour la traduction en plusieurs langues des articles d'ingénierie publiés sur ce blog.

## Conception du prompt
### Principes de base pour faire une demande
Pour obtenir des résultats satisfaisants et conformes à l'objectif d'un modèle de langage, il faut lui fournir un prompt approprié. La conception de prompts peut sembler intimidante, mais en réalité, "la façon de bien faire une demande" n'est pas très différente, que l'on s'adresse à un modèle de langage ou à un être humain. Il n'est donc pas si difficile d'aborder la question sous cet angle. Il est bon d'expliquer clairement la situation actuelle et les demandes selon les cinq W (qui, quoi, où, quand, pourquoi) et le H (comment), et d'ajouter quelques exemples concrets si nécessaire. Il existe de nombreux conseils et techniques pour la conception de prompts, mais la plupart découlent des principes de base qui seront expliqués ci-après.

#### Ton général
De nombreux rapports indiquent que le modèle de langage produit des réponses de meilleure qualité lorsque le prompt est rédigé et saisi sur un ton poli de demande plutôt que sur un ton autoritaire. En général, dans la société, lorsqu'on demande quelque chose à quelqu'un d'autre, la probabilité que l'autre personne effectue la tâche demandée avec soin est plus élevée lorsqu'on utilise le premier ton plutôt que le second. Il semble que les modèles de langage aient appris et imitent ce schéma de réponse humaine.

#### Attribution de rôle et explication de la situation (qui, pourquoi)
Tout d'abord, j'ai attribué à Claude 3.5 le rôle de "traducteur professionnel spécialisé dans les domaines techniques" et fourni des informations contextuelles sur l'utilisateur en tant que "blogueur en ingénierie qui écrit principalement sur les mathématiques, la physique et la science des données".

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Transmission de la demande générale (quoi)
Ensuite, j'ai demandé de traduire le texte au format markdown fourni par l'utilisateur de {source_lang} vers {target_lang} tout en préservant le format.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Lors de l'appel à l'API Claude, les variables de langue source et cible sont respectivement insérées à la place de {source_lang} et {target_lang} dans le prompt grâce à la fonction f-string du script Python.
{: .prompt-info }

#### Spécification des exigences et exemples (comment)
Pour des tâches simples, les étapes précédentes peuvent suffire pour obtenir le résultat souhaité, mais pour des tâches plus complexes, des explications supplémentaires peuvent être nécessaires.

Lorsque les exigences sont complexes et multiples, il est préférable de les présenter sous forme de liste plutôt que de les décrire en détail, ce qui améliore la lisibilité et facilite la compréhension (que ce soit pour un humain ou un modèle de langage). Il peut également être utile de fournir des exemples si nécessaire.
Dans ce cas, j'ai ajouté les conditions suivantes :

##### Traitement du YAML front matter
Le YAML front matter situé au début des articles rédigés en markdown pour être téléchargés sur le blog Jekyll contient les informations 'title', 'description', 'categories' et 'tags'. Par exemple, le YAML front matter de cet article est le suivant :

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

Cependant, lors de la traduction d'un article, les balises de titre (title) et de description (description) doivent être traduites en plusieurs langues, mais pour maintenir la cohérence des URL des articles, il est préférable de laisser les noms des catégories (categories) et des tags (tags) en anglais sans les traduire, ce qui facilite la maintenance. J'ai donc ajouté l'instruction suivante pour éviter la traduction des balises autres que 'title' et 'description'. Comme Claude a probablement déjà appris et connaît les informations sur le YAML front matter, cette explication devrait suffire dans la plupart des cas.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> J'ai ajouté la phrase "under any circumstances, regardless of the language you are translating to" pour souligner que les autres balises du YAML front matter ne doivent **en aucun cas** être modifiées arbitrairement.
{: .prompt-tip }

##### Traitement des cas où le texte original contient des langues autres que la langue source
Lors de la rédaction du texte original en coréen, il arrive souvent que l'on inclue l'expression anglaise entre parenthèses, comme dans "*중성자 감쇠 (Neutron Attenuation)*", lorsqu'on introduit la définition d'un concept pour la première fois ou qu'on utilise certains termes techniques. Lors de la traduction de telles expressions, il y avait un problème d'incohérence dans la méthode de traduction, parfois en conservant les parenthèses, parfois en omettant l'anglais entre parenthèses. J'ai donc établi les directives détaillées suivantes :
- Pour les termes techniques,
  - Lors de la traduction vers des langues non basées sur l'alphabet romain comme le japonais, conserver le format 'expression traduite(expression anglaise)'.
  - Lors de la traduction vers des langues basées sur l'alphabet romain comme l'espagnol, le portugais ou le français, autoriser à la fois la notation unique 'expression traduite' et la notation combinée 'expression traduite(expression anglaise)', en laissant Claude choisir de manière autonome celle qui lui semble la plus appropriée.
- Pour les noms propres, l'orthographe originale doit être préservée dans le résultat de la traduction sous une forme ou une autre.

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
Certains articles contiennent des liens vers d'autres articles. Lors de la phase de test, lorsqu'aucune directive spécifique n'était fournie à ce sujet, le modèle interprétait souvent la partie du chemin de l'URL comme devant être traduite, ce qui entraînait la rupture des liens internes. Ce problème a été résolu en ajoutant la phrase suivante au prompt :

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Ne produire que le résultat de la traduction comme réponse
Enfin, la phrase suivante est présentée pour demander de ne produire que le résultat de la traduction sans ajouter d'autres commentaires dans la réponse.

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Techniques supplémentaires de conception de prompts
Cependant, contrairement à la demande de travail à un être humain, il existe des techniques supplémentaires qui s'appliquent spécifiquement aux modèles de langage.
Il existe de nombreuses ressources utiles à ce sujet sur le web, mais voici un résumé de quelques conseils représentatifs qui peuvent être utilisés de manière générale et utile.  
Je me suis principalement référé au [guide d'ingénierie des prompts de la documentation officielle d'Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Structuration à l'aide de balises XML
En fait, nous avons déjà utilisé cette technique jusqu'à présent. Pour les prompts complexes incluant divers contextes, instructions, formats et exemples, l'utilisation appropriée de balises XML telles que `<instructions>`, `<example>`, `<format>`, etc., peut grandement aider le modèle de langage à interpréter correctement le prompt et à produire une sortie de haute qualité conforme à l'intention. Le dépôt GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) contient une bonne liste de balises XML utiles pour la rédaction de prompts, je recommande de s'y référer.

#### Technique de raisonnement par étapes (CoT, chain of thinking)
Pour les tâches nécessitant un niveau considérable de raisonnement, comme la résolution de problèmes mathématiques ou la rédaction de documents complexes, on peut grandement améliorer les performances en guidant le modèle de langage pour qu'il réfléchisse au problème étape par étape. Cependant, cela peut augmenter le temps de réponse, et cette technique n'est pas toujours utile pour toutes les tâches, il faut donc être prudent.

#### Technique de chaînage de prompts (prompt chaining)
Pour les tâches complexes, un seul prompt peut avoir ses limites. Dans ce cas, on peut envisager de diviser dès le départ l'ensemble du flux de travail en plusieurs étapes, en présentant un prompt spécialisé pour chaque étape et en transmettant la réponse obtenue à l'étape précédente comme entrée pour l'étape suivante. Cette technique est appelée chaînage de prompts (prompt chaining).

#### Pré-remplissage du début de la réponse
Lors de la saisie du prompt, on peut présenter à l'avance le début du contenu de la réponse et demander de continuer la réponse à partir de là, ce qui permet d'éviter les salutations inutiles ou d'autres introductions, ou de forcer une réponse dans un format spécifique comme XML ou JSON. [Dans le cas de l'API Claude, on peut utiliser cette technique en soumettant un message `Assistant` en plus du message `User` lors de l'appel.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prévention de la paresse (Patch Halloween du 31.10.12024)
Bien que j'aie apporté quelques améliorations mineures au prompt et précisé certaines instructions une ou deux fois depuis la rédaction initiale de cet article, le système d'automatisation a fonctionné sans problème majeur pendant 4 mois.

Cependant, à partir d'environ 18h00 heure coréenne le 31.10.12024, un phénomène anormal s'est produit de manière persistante : lors de la traduction de nouveaux articles, seule la partie "TL;DR" au début de l'article était traduite, puis la traduction s'arrêtait arbitrairement.

Les causes probables de ce problème et les méthodes de résolution sont traitées dans [un article séparé](/posts/does-ai-hate-to-work-on-halloween), veuillez vous y référer.

### Prompt finalisé
Voici le résultat de la conception du prompt après avoir suivi les étapes ci-dessus :

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
