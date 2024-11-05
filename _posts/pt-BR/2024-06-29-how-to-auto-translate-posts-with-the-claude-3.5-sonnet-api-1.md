---
title: Como traduzir posts automaticamente com a API do Claude 3.5 Sonnet (1) - Design do prompt
description: >-
  Aborda o processo de design do prompt para aplicar na tradução multilíngue dos posts deste blog, e a automatização do trabalho em Python usando a chave API obtida da Anthropic e o prompt desenvolvido. Este post é o primeiro da série e apresenta o método e processo de design do prompt.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introdução
Recentemente, implementei a API do Claude 3.5 Sonnet da Anthropic para tradução multilíngue dos posts do blog. Nesta série, vou abordar os motivos para escolher a API do Claude 3.5 Sonnet, o método de design do prompt, e como implementar a automação através da integração da API com scripts Python.  
A série consiste em 2 posts, e este que você está lendo é o primeiro deles.
- Parte 1: Introdução ao modelo Claude 3.5 Sonnet, motivos da seleção e engenharia de prompt (este post)
- Parte 2: [Desenvolvimento e aplicação do script de automação Python usando a API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Sobre o Claude 3.5 Sonnet
Os modelos da série Claude 3 são oferecidos em três versões de acordo com o tamanho do modelo: Haiku, Sonnet e Opus.  
![Diferenciação dos níveis de modelo do Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fonte da imagem: [Página oficial da API Anthropic Claude](https://www.anthropic.com/api)

Em 21 de junho de 2024 (horário coreano), a Anthropic lançou seu mais recente modelo de linguagem, o [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Segundo o anúncio da Anthropic, ele oferece desempenho de inferência superior ao Claude 3 Opus com o mesmo custo e velocidade do Claude 3 Sonnet original, e é geralmente considerado superior ao seu concorrente GPT-4 em áreas como redação, raciocínio linguístico, compreensão multilíngue e tradução.  
![Imagem de introdução do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados do benchmark de desempenho do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fonte das imagens: [Site da Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Adicionado em 31.10.2024) Em 22 de outubro de 2024, a Anthropic anunciou uma versão atualizada da API do Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") e o Claude 3.5 Haiku. No entanto, devido ao [problema que será discutido posteriormente](#prevenção-de-preguiça-patch-halloween-31102024), este blog ainda está usando a API "claude-3-5-sonnet-20240620" original.

## Por que implementei o Claude 3.5 para tradução de posts
Mesmo sem usar modelos de linguagem como Claude 3.5 ou GPT-4, existem APIs de tradução comerciais estabelecidas como Google Translate ou DeepL. A razão para decidir usar um LLM para fins de tradução é que, diferentemente de outros serviços de tradução comerciais, os usuários podem fornecer informações contextuais adicionais ou requisitos através do design do prompt, como o propósito da escrita ou os principais tópicos do texto, e o modelo pode fornecer traduções que consideram esse contexto. Embora DeepL e Google Translate geralmente mostrem excelente qualidade de tradução, eles têm limitações em compreender o tema e o contexto geral do texto, resultando em traduções relativamente não naturais quando solicitados a traduzir textos longos sobre tópicos especializados, em vez de conversas cotidianas. Em particular, como mencionado anteriormente, o Claude é frequentemente considerado superior ao seu concorrente GPT-4 em áreas como redação, raciocínio linguístico, compreensão multilíngue e tradução, e quando testado brevemente, mostrou qualidade de tradução mais fluida que o GPT-4o, então julguei que seria adequado para traduzir os textos de engenharia publicados neste blog para vários idiomas.

## Design do Prompt
### Princípios básicos ao fazer solicitações
Para obter resultados satisfatórios que atendam aos objetivos de um modelo de linguagem, é necessário fornecer um prompt apropriado. Embora o design de prompt possa parecer intimidante, na verdade não é muito difícil se abordado do ponto de vista de "como fazer boas solicitações", pois não é muito diferente seja o destinatário um modelo de linguagem ou uma pessoa. É bom explicar claramente a situação atual e os requisitos seguindo os princípios básicos de comunicação (quem, o quê, quando, onde, por que e como), e adicionar alguns exemplos específicos se necessário. Existem muitas dicas e técnicas para design de prompt, mas a maioria deriva dos princípios básicos que serão discutidos a seguir.

#### Tom geral
Há muitos relatos de que os modelos de linguagem produzem respostas de maior qualidade quando os prompts são escritos e inseridos em um tom educado de solicitação, em vez de um tom autoritário de comando. Normalmente, na sociedade, quando pedimos algo a outra pessoa, a probabilidade de a pessoa realizar a tarefa solicitada com mais sinceridade aumenta quando usamos o último tom em vez do primeiro, e parece que os modelos de linguagem aprendem e imitam esses padrões de resposta humana.

#### Atribuição de papel e explicação da situação (quem, por quê)
Primeiro, atribuí ao Claude 3.5 o papel de "tradutor técnico profissional" e forneci informações contextuais sobre o usuário como "um blogueiro de engenharia que contribui principalmente com textos sobre matemática, física e ciência de dados".

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Comunicação dos requisitos gerais (o quê)
Em seguida, solicitei a tradução do texto em formato markdown fornecido de {source_lang} para {target_lang}, mantendo o formato.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Ao chamar a API do Claude, as variáveis de idioma de origem e destino são inseridas respectivamente nos lugares de {source_lang} e {target_lang} através da funcionalidade f-string do script Python.
{: .prompt-info }

#### Especificação de requisitos e exemplos (como)
Para tarefas simples, as etapas anteriores podem ser suficientes para obter os resultados desejados, mas para tarefas que exigem requisitos complexos, podem ser necessárias explicações adicionais.

Quando os requisitos são complexos e múltiplos, é mais fácil de entender (seja para humanos ou modelos de linguagem) se eles forem apresentados em forma de lista concisa em vez de explicados detalhadamente. Além disso, fornecer exemplos quando necessário pode ser útil.
Neste caso, foram adicionadas as seguintes condições:

##### Processamento do YAML front matter
O YAML front matter localizado no início dos posts escritos em markdown para upload no blog Jekyll registra informações de 'title', 'description', 'categories' e 'tags'. Por exemplo, o YAML front matter deste post é o seguinte:

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

Ao traduzir os posts, as tags de título (title) e descrição (description) devem ser traduzidas para vários idiomas, mas para manter a consistência das URLs dos posts, é mais conveniente para a manutenção manter os nomes das categorias (categories) e tags em inglês. Portanto, adicionei a seguinte instrução para não traduzir outras tags além de 'title' e 'description':

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Enfatizei que outras tags do YAML front matter não devem ser modificadas **sem exceção** adicionando a frase "under any circumstances, regardless of the language you are translating to".
{: .prompt-tip }

##### Processamento quando o texto original inclui outros idiomas além do idioma de origem
Ao escrever o texto original em coreano, frequentemente incluímos expressões em inglês entre parênteses ao introduzir a definição de um conceito ou usar certos termos técnicos, como '*중성자 감쇠 (Neutron Attenuation)*'. Para resolver o problema de inconsistência na tradução dessas expressões, onde às vezes os parênteses são mantidos e outras vezes a expressão em inglês entre parênteses é omitida, estabeleci as seguintes diretrizes detalhadas:
- Para termos técnicos:
  - Ao traduzir para idiomas não baseados no alfabeto romano, como japonês, manter o formato 'expressão traduzida(expressão em inglês)'.
  - Ao traduzir para idiomas baseados no alfabeto romano, como espanhol, português ou francês, permitir tanto a notação única 'expressão traduzida' quanto a notação combinada 'expressão traduzida(expressão em inglês)', deixando o Claude escolher autonomamente a mais apropriada.
- Para nomes próprios, a grafia original deve ser preservada de alguma forma no resultado da tradução.

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

##### Processamento de links para outros posts
Alguns posts incluem links para outros posts, e durante a fase de teste, quando não foram fornecidas diretrizes específicas sobre isso, frequentemente ocorria o problema dos links internos quebrarem porque o modelo interpretava que a parte do caminho da URL também deveria ser traduzida. Este problema foi resolvido adicionando a seguinte frase ao prompt:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Produzir apenas o resultado da tradução como resposta
Por fim, a seguinte frase é apresentada para garantir que apenas o resultado da tradução seja produzido na resposta, sem adicionar outros comentários:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Técnicas adicionais de design de prompt
No entanto, existem técnicas adicionais que se aplicam especificamente aos modelos de linguagem, diferentemente de quando se faz solicitações a humanos.
Existem muitos recursos úteis sobre isso na web, mas aqui estão algumas dicas representativas que podem ser úteis de forma geral:  
[Referência principal: Guia de engenharia de prompt da documentação oficial da Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

#### Estruturação usando tags XML
Na verdade, isso já vinha sendo usado até agora. Para prompts complexos que incluem vários contextos, instruções, formatos e exemplos, o uso apropriado de tags XML como `<instructions>`, `<example>`, `<format>` pode ajudar muito o modelo de linguagem a interpretar o prompt com precisão e produzir saídas de alta qualidade que atendam à intenção. O repositório GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) tem uma boa compilação de tags XML úteis para escrita de prompts, então recomendo consultá-lo.

#### Técnica de raciocínio passo a passo (CoT, chain of thinking)
Para tarefas que requerem um nível significativo de raciocínio, como resolução de problemas matemáticos ou criação de documentos complexos, o desempenho pode ser significativamente melhorado guiando o modelo de linguagem a pensar no problema em etapas. No entanto, isso pode aumentar o tempo de resposta, e essa técnica não é sempre útil para todas as tarefas, então é preciso ter cuidado.

#### Técnica de encadeamento de prompts (prompt chaining)
Para tarefas complexas, pode haver limitações ao tentar lidar com um único prompt. Nestes casos, pode-se considerar dividir todo o fluxo de trabalho em várias etapas desde o início, apresentar prompts especializados para cada etapa e passar a resposta obtida em uma etapa como entrada para a próxima. Esta técnica é chamada de encadeamento de prompts (prompt chaining).

#### Preenchimento prévio do início da resposta
Ao inserir um prompt, pode-se pular saudações desnecessárias ou forçar uma resposta em um formato específico, como XML ou JSON, fornecendo previamente a primeira parte do conteúdo da resposta e solicitando a continuação. [No caso da API do Claude, esta técnica pode ser usada submetendo uma mensagem 'Assistant' junto com a mensagem 'User' ao fazer a chamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevenção de preguiça (Patch Halloween 31.10.2024)
Embora tenha havido algumas pequenas melhorias no prompt e especificações mais detalhadas das instruções desde que este post foi escrito inicialmente, o sistema de automação funcionou sem grandes problemas durante 4 meses.

No entanto, por volta das 18h (horário coreano) de 31.10.2024, começou a ocorrer continuamente um comportamento anormal onde, ao solicitar a tradução de novos posts, apenas a primeira parte 'TL;DR' do post era traduzida antes de interromper arbitrariamente a tradução.

As causas suspeitas deste problema e os métodos de solução são discutidos em um [post separado](/posts/does-ai-hate-to-work-on-halloween), então por favor consulte esse post.

### Prompt finalizado
O resultado do design do prompt após passar por essas etapas é o seguinte:

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

## Leitura Adicional
Continua na [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)
