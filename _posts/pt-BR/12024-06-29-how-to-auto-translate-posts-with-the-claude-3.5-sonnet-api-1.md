---
title: Como traduzir posts automaticamente com a API Claude 3.5 Sonnet (1) - Design de prompt
description: Aborda o processo de projetar prompts para tradução multilíngue de arquivos de texto markdown e automatizar o trabalho em Python usando a chave de API emitida pela Anthropic e os prompts criados. Este post é o primeiro da série e introduz métodos e processos de design de prompts.
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.jpg
---
## Introdução
Recentemente, implementei a API Claude 3.5 Sonnet da Anthropic para tradução multilíngue dos posts do blog. Nesta série, abordarei os motivos para escolher a API Claude 3.5 Sonnet, métodos de design de prompts e como implementar a automação através de scripts Python conectados à API.  
A série consiste em dois artigos, e este é o primeiro deles.
- Parte 1: Introdução ao modelo Claude 3.5 Sonnet, razões para seleção e engenharia de prompts (este artigo)
- Parte 2: [Escrevendo e aplicando scripts de automação Python usando a API](/posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-2)

## Sobre o Claude 3.5 Sonnet
A série de modelos Claude 3 é oferecida em três versões de acordo com o tamanho: Haiku, Sonnet e Opus.  
![Diferenciação de níveis dos modelos Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fonte da imagem: [Página oficial da API Anthropic Claude](https://www.anthropic.com/api)

Em 21 de junho de 12024 (calendário holocene), a Anthropic lançou seu mais recente modelo de linguagem, o [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). Segundo a Anthropic, ele oferece desempenho de raciocínio superior ao Claude 3 Opus com o mesmo custo e velocidade do Claude 3 Sonnet original. É geralmente considerado superior ao GPT-4 em composição, raciocínio linguístico, compreensão multilíngue e tradução.  
![Imagem de introdução do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados de benchmark de desempenho do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fonte das imagens: [Site da Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

(Adicionado em 31.10.12024) Em 22 de outubro de 12024, a Anthropic anunciou uma versão atualizada da API Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") e o Claude 3.5 Haiku. No entanto, devido ao [problema mencionado posteriormente](#prevenção-de-preguiça-patch-de-halloween-311012024), este blog ainda utiliza a API "claude-3-5-sonnet-20240620" original.

## Por que implementar o Claude 3.5 para tradução de posts
Existem APIs de tradução comerciais como Google Translate e DeepL que poderiam ser usadas em vez de modelos de linguagem como Claude 3.5 ou GPT-4. No entanto, decidi usar um LLM para tradução porque, diferentemente de outros serviços de tradução comerciais, os usuários podem fornecer informações contextuais adicionais ou requisitos através do design de prompts, como o propósito do texto ou tópicos principais, e o modelo pode fornecer traduções que consideram esse contexto. Embora DeepL e Google Translate geralmente ofereçam excelente qualidade de tradução, eles têm limitações na compreensão do tema ou contexto geral, resultando em traduções menos naturais para textos longos sobre tópicos especializados. Como mencionado anteriormente, o Claude é considerado superior ao GPT-4 em composição, raciocínio linguístico, compreensão multilíngue e tradução, e em testes simples, demonstrou traduções mais fluidas que o GPT-4o, tornando-o adequado para traduzir artigos de engenharia deste blog para vários idiomas.

## Design de Prompt
### Princípios básicos para fazer solicitações
Para obter resultados satisfatórios de um modelo de linguagem, é necessário fornecer prompts apropriados. O design de prompts pode parecer intimidador, mas na verdade não é muito diferente de "como fazer boas solicitações" a pessoas ou modelos de linguagem. É útil explicar claramente a situação atual e os requisitos seguindo os princípios básicos de comunicação (quem, o quê, quando, onde, por quê e como), e adicionar exemplos específicos quando necessário. Existem muitas dicas e técnicas para design de prompts, mas a maioria deriva dos princípios básicos descritos a seguir.

#### Tom geral
Há muitos relatos de que os modelos de linguagem produzem respostas de maior qualidade quando os prompts são escritos em um tom educado de solicitação, em vez de comandos autoritários. Assim como na sociedade, onde as pessoas tendem a realizar tarefas com mais dedicação quando solicitadas educadamente em vez de receberem ordens, os modelos de linguagem parecem imitar esses padrões de resposta humana.

#### Atribuição de papel e explicação da situação (quem, por quê)
Primeiro, atribuí ao Claude 3.5 o papel de *'tradutor técnico profissional'* e forneci informações contextuais sobre o usuário como *"um blogueiro de engenharia que escreve principalmente sobre matemática, física e ciência de dados"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. \
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, and quantum information theory), \
and data science for his Jekyll blog.</role>
```

#### Comunicação dos requisitos gerais (o quê)
Em seguida, solicitei a tradução do texto em formato markdown de {source_lang} para {target_lang}, mantendo o formato.

```xml
<task>Please translate the provided <format>markdown</format> text from <lang>{source_lang}</lang> \
to <lang>{target_lang}</lang> while preserving the format.</task>
```

> Ao chamar a API Claude, as variáveis {source_lang} e {target_lang} no prompt são substituídas pelos idiomas de origem e destino através da funcionalidade f-string do Python.
{: .prompt-info }

#### Especificação de requisitos e exemplos (como)
Para tarefas simples, as etapas anteriores podem ser suficientes, mas tarefas complexas podem exigir explicações adicionais.

Quando os requisitos são complexos e numerosos, é melhor listá-los de forma organizada para melhorar a legibilidade e facilitar a compreensão. Fornecer exemplos também pode ser útil.
Neste caso, adicionei as seguintes condições:

##### Tratamento do YAML front matter
Os posts em markdown para o blog Jekyll começam com um YAML front matter que contém informações como 'title', 'description', 'categories' e 'tags'. Por exemplo, o YAML front matter deste post é:

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

Ao traduzir posts, as tags 'title' e 'description' devem ser traduzidas, mas para manter a consistência das URLs, os nomes de 'categories' e 'tags' devem permanecer em inglês. Portanto, adicionei a seguinte instrução:

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition> \n\n\
```

> Adicionei a frase "under any circumstances, regardless of the language you are translating to" para enfatizar que **sem exceções** as outras tags do YAML front matter não devem ser modificadas.
{: .prompt-tip }

##### Tratamento de texto em idiomas diferentes do idioma de origem
Ao escrever em coreano, frequentemente incluo expressões em inglês entre parênteses ao introduzir conceitos ou termos técnicos, como '*중성자 감쇠 (Neutron Attenuation)*'. Para garantir consistência na tradução dessas expressões, estabeleci as seguintes diretrizes:
- Para termos técnicos:
  - Ao traduzir para idiomas não baseados no alfabeto romano (como japonês), manter o formato 'expressão traduzida(expressão em inglês)'.
  - Ao traduzir para idiomas baseados no alfabeto romano (como espanhol, português ou francês), permitir tanto a forma 'expressão traduzida' quanto 'expressão traduzida(expressão em inglês)', deixando Claude escolher a mais apropriada.
- Para nomes próprios, a grafia original deve ser preservada de alguma forma na tradução.

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

##### Tratamento de links para outros posts
Alguns posts contêm links para outros posts, e durante os testes, sem instruções específicas, o modelo frequentemente traduzia até mesmo o caminho da URL, quebrando os links internos. Resolvi esse problema adicionando esta instrução:

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if> \n\
  - <example> the German translation of '[중성자 상호작용과 반응단면적]\
    (/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section)' \
    would be '[Neutronenwechselwirkungen und Wirkungsquerschnitte](/posts/Neutron-Interactions-and-Cross-sections/\
    #wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section)'.</example></condition> \n\n\
```

##### Saída apenas do resultado da tradução
Por fim, instruí o modelo a fornecer apenas o resultado da tradução, sem texto adicional:

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Técnicas adicionais de design de prompt
Além das técnicas aplicáveis à comunicação humana, existem técnicas específicas para modelos de linguagem.
Há muitos recursos úteis disponíveis online, mas aqui estão algumas dicas representativas que podem ser aplicadas universalmente:  
As informações a seguir foram principalmente baseadas no [guia oficial de engenharia de prompts da Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Estruturação com tags XML
Na verdade, já vínhamos usando essa técnica. Para prompts complexos que incluem vários contextos, instruções, formatos e exemplos, o uso adequado de tags XML como `<instructions>`, `<example>`, `<format>` ajuda o modelo a interpretar o prompt corretamente e produzir saídas de alta qualidade. O repositório GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) contém uma boa compilação de tags XML úteis para escrita de prompts.

#### Técnica de raciocínio passo a passo (CoT, Chain of Thinking)
Para tarefas que requerem raciocínio substancial, como resolução de problemas matemáticos ou criação de documentos complexos, orientar o modelo a dividir o problema em etapas pode melhorar significativamente o desempenho. No entanto, isso pode aumentar o tempo de resposta e não é útil para todas as tarefas.

#### Técnica de encadeamento de prompts (prompt chaining)
Para tarefas complexas, um único prompt pode ser limitado. Nesse caso, pode-se considerar dividir o fluxo de trabalho em várias etapas, fornecendo prompts especializados para cada etapa e usando a resposta de uma etapa como entrada para a próxima. Esta técnica é conhecida como encadeamento de prompts.

#### Preenchimento prévio do início da resposta
Ao fornecer a parte inicial da resposta esperada no prompt, pode-se fazer com que o modelo pule saudações desnecessárias ou forçá-lo a responder em um formato específico como XML ou JSON. [Na API Claude, isso pode ser feito incluindo uma mensagem `Assistant` junto com a mensagem `User` ao fazer a chamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevenção de preguiça (Patch de Halloween 31.10.12024)
Embora tenha feito algumas pequenas melhorias no prompt e especificações mais detalhadas após escrever este artigo inicialmente, o sistema de automação funcionou sem grandes problemas por 4 meses.

No entanto, a partir das 18h (horário coreano) de 31.10.12024, começou a ocorrer um fenômeno estranho: ao solicitar a tradução de novos posts, o modelo traduzia apenas a parte inicial "TL;DR" e interrompia arbitrariamente a tradução.

As causas prováveis deste problema e suas soluções são discutidas em [um post separado](/posts/does-ai-hate-to-work-on-halloween), que recomendo consultar.

### Prompt finalizado
O resultado final do design de prompt é o seguinte:

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
