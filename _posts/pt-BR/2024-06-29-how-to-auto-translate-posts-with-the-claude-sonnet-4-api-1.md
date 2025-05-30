---
title: Como traduzir posts automaticamente com a API do Claude Sonnet 4 (1) - Design de Prompt
description: "Aborda o processo de design de prompts para tradução multilíngue de arquivos de texto markdown e automação do trabalho com Python aplicando a chave API obtida da Anthropic e o prompt criado. Este post é o primeiro da série, apresentando métodos e processos de design de prompt."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---

## Introdução
Desde a introdução da API do Claude 3.5 Sonnet da Anthropic em junho de 12024 para tradução multilíngue de posts do blog, após várias melhorias de prompt e script de automação, além de atualizações de versão do modelo, venho operando esse sistema de tradução de forma satisfatória por quase um ano. Nesta série, pretendo abordar as razões para escolher o modelo Claude Sonnet no processo de introdução, métodos de design de prompt e métodos de implementação de integração de API e automação através de scripts Python.  
A série consiste em 2 artigos, e este artigo que você está lendo é o primeiro da série.
- Parte 1: Introdução ao modelo Claude Sonnet e razões para seleção, engenharia de prompt (texto atual)
- Parte 2: [Criação e aplicação de script de automação Python usando API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## Sobre o Claude Sonnet
Os modelos da série Claude são fornecidos nas versões Haiku, Sonnet e Opus de acordo com o tamanho do modelo.  
![Classificação de níveis do modelo Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)  
> Fonte da imagem: [Página oficial da API Anthropic Claude](https://www.anthropic.com/api)

> (Adicionado em 12025.05.29.)  
> Como a imagem foi capturada há um ano, as tarifas por token são baseadas na versão antiga Claude 3, mas a classificação Haiku, Sonnet, Opus por tamanho de modelo ainda é válida. Com base no final de maio de 12025, a precificação para cada modelo fornecido pela Anthropic é a seguinte.
>
> | Model | Base Input <br>Tokens | 5m Cache <br>Writes | 1h Cache <br>Writes | Cache Hits &<br> Refreshes | Output <br>Tokens |
> | :--- | :--- | :--- | :--- | :--- | :--- |
> | Claude Opus 4 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Sonnet 4 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.7 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Sonnet 3.5 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
> | Claude Haiku 3.5 | $0.80 / MTok | $1 / MTok | $1.6 / MTok | $0.08 / MTok | $4 / MTok |
> | Claude Opus 3 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
> | Claude Haiku 3 | $0.25 / MTok | $0.30 / MTok | $0.50 / MTok | $0.03 / MTok | $1.25 / MTok |
>
> Fonte: [Documentação do desenvolvedor Anthropic](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-pricing)
{: .prompt-tip }

E o modelo de linguagem [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) lançado pela Anthropic em 21 de junho de 12024 no horário da Coreia (calendário holoceno) mostra desempenho de raciocínio que supera o Claude 3 Opus com o mesmo custo e velocidade do Claude 3 Sonnet existente, e geralmente é avaliado como tendo vantagens sobre o modelo concorrente GPT-4 nas áreas de escrita, raciocínio linguístico, compreensão multilíngue e tradução.  
![Imagem de introdução do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)  
![Resultados de benchmark de desempenho do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)  
> Fonte da imagem: [Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## Razões para introduzir o Claude 3.5 para tradução de posts
Mesmo sem modelos de linguagem como Claude 3.5 ou GPT-4, existem APIs de tradução comerciais como Google Translate ou DeepL. Ainda assim, a razão para decidir usar LLM para fins de tradução é que, diferentemente de outros serviços de tradução comerciais, os usuários podem fornecer informações de contexto adicionais ou requisitos além do texto principal, como o propósito da escrita ou tópicos principais do texto através do design de prompt, e o modelo pode fornecer tradução considerando o contexto de acordo.

Embora DeepL ou Google Translate também mostrem qualidade de tradução geralmente excelente, eles têm limitações por não conseguirem compreender bem o tópico ou contexto geral do texto e não poderem transmitir requisitos complexos separadamente. Por isso, quando solicitados a traduzir textos longos sobre tópicos especializados que não sejam conversas cotidianas, os resultados de tradução podem ser relativamente não naturais e há dificuldades em produzir saídas que correspondam exatamente aos formatos específicos necessários (markdown, YAML frontmatter, etc.).

Especialmente, como mencionado acima, Claude tinha muitas avaliações de ser relativamente superior ao modelo concorrente GPT-4 nas áreas de escrita, raciocínio linguístico, compreensão multilíngue e tradução, e quando testei diretamente de forma simples, também mostrou qualidade de tradução mais suave que o GPT-4, então julguei adequado para o trabalho de traduzir artigos relacionados à engenharia registrados neste blog para várias línguas quando estava considerando a introdução em junho de 12024.

## Histórico de adoção de modelos e situação atual
### 12024.07.01.
Como organizado em [artigo separado](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/), [completei o trabalho inicial de aplicar o plugin Polyglot e modificar `_config.yml`{: .filepath}, cabeçalho html e sitemap de acordo.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Em seguida, [adotei o modelo Claude 3.5 Sonnet para fins de tradução e apliquei após completar a implementação inicial e verificação do script Python de integração de API que está sendo abordado nesta série.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
Em 22 de outubro de 12024, a Anthropic anunciou a versão atualizada da API do Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") e Claude 3.5 Haiku. No entanto, devido ao [problema mencionado posteriormente](#prevenção-de-preguiça-patch-de-halloween-120241031), ainda estou aplicando a API "claude-3-5-sonnet-20240620" existente neste blog.

### 12025.04.02.
[Mudei o modelo aplicado de "claude-3-5-sonnet-20240620" para "claude-3-7-sonnet-20250219".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[Mudei o modelo aplicado de "claude-3-7-sonnet-20250219" para "claude-sonnet-4-20250514".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Resultados de benchmark de desempenho do Claude 4](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)  
> Fonte da imagem: [Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

Embora possa haver diferenças dependendo das condições de uso, geralmente desde o lançamento do modelo Claude 3.7 Sonnet, há pouca discordância de que Claude é o modelo mais poderoso para programação. A própria Anthropic também está promovendo ativamente o desempenho superior de programação em comparação com modelos concorrentes como OpenAI ou Google como uma das principais vantagens de seus modelos. Neste anúncio do Claude Opus 4 e Claude Sonnet 4, também podemos confirmar que continuam a tendência de visar desenvolvedores como principal grupo de clientes, enfatizando o desempenho de programação.

Claro, olhando os resultados de benchmark divulgados, houve melhorias gerais em itens além de programação também, e para o trabalho de tradução abordado neste artigo, as melhorias de desempenho em perguntas e respostas multilíngues (MMMLU) ou resolução de problemas matemáticos (AIME 2025) parecem ser particularmente eficazes. Testando diretamente de forma simples, pude confirmar que os resultados de tradução do Claude Sonnet 4 são superiores ao modelo anterior Claude 3.7 Sonnet em naturalidade de expressão, especialização e consistência no uso de terminologia.

> No momento atual, pelo menos para o trabalho de traduzir textos escritos em coreano de natureza técnica como os abordados neste blog para múltiplas línguas, acredito que o modelo Claude ainda é o melhor. No entanto, recentemente o desempenho do modelo Gemini do Google tem melhorado visivelmente, e em maio deste ano até lançaram o modelo Gemini 2.5, embora ainda esteja em fase Preview.  
> Quando comparei os modelos Gemini 2.0 Flash com Claude 3.7 Sonnet e Claude Sonnet 4, julguei que o desempenho de tradução do Claude era superior, mas o desempenho multilíngue do Gemini também é bastante excelente, e a capacidade de resolução e descrição de problemas de matemática e física é na verdade superior no Gemini 2.5 Preview 05-06 até mesmo ao Claude Opus 4, então não posso garantir como será quando esse modelo for oficialmente lançado e comparado novamente.  
> Considerando as tarifas de API consideravelmente mais baratas do Gemini em comparação ao Claude, a competitividade de preço do Gemini é muito superior, então se o desempenho for equivalente, o Gemini pode se tornar uma alternativa razoável. Como o Gemini 2.5 ainda está em fase Preview, julgo que é cedo para aplicar em automação real, então não estou considerando no momento, mas planejo testá-lo quando a versão oficial for lançada.
{: .prompt-tip }

## Design de Prompt
### Princípios básicos ao solicitar algo
Para obter resultados satisfatórios que atendam ao propósito de um modelo de linguagem, é necessário fornecer um prompt apropriado. O design de prompt pode parecer intimidante, mas na verdade 'como solicitar algo bem' não é muito diferente se a contraparte é um modelo de linguagem ou uma pessoa, então se abordarmos dessa perspectiva, não é muito difícil. Explicar claramente a situação atual e solicitações de acordo com os princípios das cinco perguntas (quem, o quê, quando, onde, por que, como) e, se necessário, adicionar alguns exemplos específicos também é bom. Existem inúmeras dicas e técnicas sobre design de prompt, mas a maioria deriva dos princípios básicos que serão mencionados posteriormente.

#### Tom geral
Há muitos relatos de que quando prompts são escritos e inseridos em tom de solicitação educada em vez de tom de comando autoritário, modelos de linguagem produzem respostas de maior qualidade. Geralmente na sociedade, quando solicitamos algo a outras pessoas, a probabilidade da contraparte realizar o trabalho solicitado com mais sinceridade aumenta quando solicitamos educadamente em vez de comandar autoritariamente, e modelos de linguagem parecem aprender e imitar esses padrões de resposta das pessoas.

#### Atribuição de papel e explicação da situação (quem, por que)
Primeiro, atribuí ao Claude 4 o papel de *'tradutor profissional especializado em campos técnicos (professional technical translator)'* e forneci informações contextuais sobre o usuário como *"blogueiro de engenharia que escreve principalmente sobre matemática, física e ciência de dados"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Transmissão de solicitações no quadro geral (o quê)
Em seguida, solicitei traduzir o texto em formato markdown fornecido pelo usuário de {source_lang} para {target_lang} mantendo o formato.

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Ao chamar a API Claude, as variáveis de idioma de origem e destino da tradução são inseridas nas posições {source_lang} e {target_lang} do prompt através da funcionalidade f-string do script Python.
{: .prompt-info }

#### Especificação de requisitos e exemplos (como)
Se for um trabalho simples, até os passos anteriores podem ser suficientes para obter os resultados desejados, mas para trabalhos complexos, explicações adicionais podem ser necessárias.

Quando as condições de requisito são complexas e múltiplas, em vez de descrever cada item separadamente, listá-los de forma organizada melhora a legibilidade e facilita a compreensão para quem lê (seja humano ou modelo de linguagem). Além disso, fornecer exemplos quando necessário também é útil.
Neste caso, adicionei as seguintes condições.

##### Processamento do YAML front matter
O YAML front matter localizado na primeira parte de posts escritos em markdown para upload no blog Jekyll registra informações de 'title', 'description', 'categories' e 'tags'. Por exemplo, o YAML front matter deste artigo atual é o seguinte.

```yaml
---
title: Claude Sonnet 4 API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인
description: >-
  마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic으로부터 발급받은
  API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 
  이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

No entanto, ao traduzir posts, as tags de título (title) e descrição (description) devem ser traduzidas para múltiplas línguas, mas para consistência de URLs de posts, é conveniente para manutenção deixar os nomes de categorias (categories) e tags (tags) em inglês sem traduzir. Portanto, dei a seguinte instrução para não traduzir tags além de 'title' e 'description'. Como Claude já deve ter aprendido e conhecer informações sobre YAML front matter, essa explicação é suficiente na maioria dos casos.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> Adicionei a frase "under any circumstances, regardless of the language you are translating to" para enfatizar que **sem exceção** outras tags do YAML front matter não devem ser modificadas arbitrariamente.
{: .prompt-tip }

(Atualizado em 12025.04.02.)  
Além disso, instruí para escrever o conteúdo da tag description em quantidade apropriada considerando SEO da seguinte forma.

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Processamento quando o texto original fornecido inclui outras línguas além do idioma de origem
Ao escrever o texto original em coreano, ao introduzir pela primeira vez a definição de algum conceito ou usar alguns termos especializados, frequentemente registro expressões em inglês entre parênteses como '*atenuação de nêutrons (Neutron Attenuation)*'. Ao traduzir essas expressões, havia o problema de métodos de tradução inconsistentes, às vezes mantendo os parênteses e outras vezes omitindo o inglês registrado entre parênteses, então estabeleci as seguintes diretrizes detalhadas.
- Para termos especializados,
  - Ao traduzir para línguas não baseadas em alfabeto romano como japonês, manter o formato 'expressão traduzida(expressão em inglês)'.
  - Ao traduzir para línguas baseadas em alfabeto romano como espanhol, português, francês, permitir tanto notação única 'expressão traduzida' quanto notação combinada 'expressão traduzida(expressão em inglês)', deixando Claude escolher autonomamente a mais apropriada entre as duas.
- Para nomes próprios, a grafia original deve ser preservada no resultado da tradução de alguma forma.

```xml
- <condition>The original text provided may contain parts written in languages other than {source_lang}. This is one of two cases.
  1. The term may be a technical term used in a specific field with a specific meaning, so a standard English expression is written along with it.
  2. it may be a proper noun such as a person's name or a place name.
  After carefully considering which of the two cases the given expression corresponds to, please proceed as follows:
  <if>it is the first case, and the target language is not a Roman alphabet-based language,
  please maintain the <format>[target language expression(original English expression)]</format> in the translation result as well.</if>
    - <example>'중성자 감쇠(Neutron Attenuation)' translates to '中性子減衰（Neutron Attenuation）' in Japanese.</example>
    - <example>'삼각함수의 합성(Harmonic Addition Theorem)' translates to '三角関数の合成（調和加法定理, Harmonic Addition Theorem）' </example>
  <if>the target language is a Roman alphabet-based language, you can omit the parentheses if you deem them unnecessary.</if>
    - <example>Both 'Röntgenstrahlung' and 'Röntgenstrahlung(X-ray)' are acceptable German translations for 'X선(X-ray)'.
      You can choose whichever you think is more appropriate.</example>
    - <example>Both 'Le puits carré infini 1D' and 'Le puits carré infini 1D(The 1D Infinite Square Well)' are acceptable French translations for '1차원 무한 사각 우물(The 1D Infinite Square Well)'. You can choose whichever you think is more appropriate.</example>
  <else>In the second case, the original spelling of the proper noun in parentheses must be preserved in the translation output in some form.</else> \n\
    - <example> '패러데이(Faraday)', '맥스웰(Maxwell)', '아인슈타인(Einstein)' should be translated into Japanese as \
      'ファラデー(Faraday)', 'マクスウェル(Maxwell)', and 'アインシュタイン(Einstein)'.\
      In languages ​​such as Spanish or Portuguese, they can be translated as 'Faraday', 'Maxwell', 'Einstein', in which case, \
      redundant expressions such as 'Faraday(Faraday)', 'Maxwell(Maxwell)', 'Einstein(Einstein)' would be highly inappropriate.</example>\
  </condition>\n\n
```

##### Processamento de links conectados a outros posts
Alguns posts incluem links conectados a outros posts, e na fase de teste, quando não forneci diretrizes separadas sobre isso, frequentemente ocorria o problema de links internos quebrarem porque interpretava até a parte do caminho da URL como alvo de tradução e a modificava. Esse problema foi resolvido adicionando esta frase ao prompt.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(Atualizado em 12025.04.06.)  
Embora fornecer as diretrizes acima faça com que a parte do caminho dos links seja processada corretamente durante a tradução, reduzindo consideravelmente a frequência de links quebrados, para links que incluem identificadores de fragmento (Fragment identifier), ainda havia a limitação de que o modelo de linguagem tinha que preencher aproximadamente a parte do identificador de fragmento, a menos que conhecesse o conteúdo do artigo alvo do link, tornando impossível a resolução fundamental do problema. Assim, melhorei o script Python e o prompt para fornecer informações contextuais sobre outros posts conectados por links dentro da tag XML `<reference_context>` do prompt do usuário e processar a tradução de links de acordo com esse contexto. Como resultado da aplicação desta atualização, foi possível prevenir a maioria dos problemas de quebra de links, e para artigos de série intimamente conectados, também se tornou possível esperar o efeito de fornecer tradução mais consistente através de múltiplos posts.

Apresento a seguinte diretriz no prompt do sistema.
```xml
- <condition><if><![CDATA[<reference_context>]]> is provided in the prompt, \
  it contains the full content of posts that are linked with hash fragments from the original post.
  Use this context to accurately translate link texts and hash fragments \
  while maintaining proper references to the specific sections in those posts. 
  This ensures that cross-references between posts maintain their semantic meaning \
  and accurate linking after translation.</if></condition>
```

E a parte `<reference_context>` do prompt do usuário é composta pelo seguinte formato e conteúdo, fornecida adicionalmente após o conteúdo do texto principal a ser traduzido.
```xml
<reference_context>
The following are contents of posts linked with hash fragments in the original post. 
Use these for context when translating links and references:

<referenced_post path="{post_1_path}" hash="{hash_fragment_1}">
{post_content}
</referenced_post>

<referenced_post path="{post__2_path}" hash="{hash_fragment_2}">
{post_content}
</referenced_post>

...

</reference_context>
```

> Para como isso foi implementado especificamente, consulte a [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2) desta série e o conteúdo do [script Python](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/tools/prompt.py) no repositório GitHub.
{: .prompt-tip }

##### Produzir apenas resultados de tradução como resposta
Finalmente, apresento a seguinte frase para produzir apenas resultados de tradução sem adicionar outras palavras na resposta.

```xml
<important>In any case, without exception, the output should contain only the translation results, without any text such as \
"Here is the translation of the text provided, preserving the markdown format:" or something of that nature!!</important>
```

### Técnicas adicionais de design de prompt
No entanto, diferentemente de solicitar trabalho a humanos, no caso de modelos de linguagem, também existem técnicas adicionais que se aplicam especialmente.
Embora existam muitos materiais úteis sobre isso na web, resumindo algumas dicas representativas que podem ser usadas de forma universal:  
Referi-me principalmente ao [guia de engenharia de prompt da documentação oficial da Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Estruturação usando tags XML
Na verdade, isso já vinha sendo usado anteriormente. Para prompts complexos que incluem vários contextos, instruções, formatos e exemplos, usar apropriadamente tags XML como `<instructions>`, `<example>`, `<format>` ajuda o modelo de linguagem a interpretar o prompt com precisão e produzir saídas de alta qualidade que atendem à intenção. Recomendo consultar o repositório GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) onde tags XML úteis para escrita de prompts estão bem organizadas.

#### Técnica de raciocínio passo a passo (CoT, chain of thinking)
Para trabalhos que requerem um nível considerável de raciocínio, como resolução de problemas matemáticos ou escrita de documentos complexos, induzir o modelo de linguagem a pensar sobre o problema passo a passo pode melhorar significativamente o desempenho. No entanto, neste caso, o tempo de atraso de resposta pode aumentar, e essa técnica nem sempre é útil para todos os trabalhos, então tenha cuidado.

#### Técnica de encadeamento de prompts (prompt chaining)
Para trabalhos complexos, pode haver limitações em lidar com um único prompt. Neste caso, também pode ser considerado dividir todo o fluxo de trabalho em várias etapas desde o início, apresentar prompts especializados para cada etapa e usar o método de transmitir a resposta obtida na etapa anterior como entrada para a próxima etapa. Essa técnica é chamada de encadeamento de prompts (prompt chaining).

#### Pré-preenchimento da primeira parte da resposta
Ao inserir um prompt, fornecendo antecipadamente a primeira parte do conteúdo a ser respondido e fazendo com que escreva a resposta que seguirá, é possível pular preâmbulos desnecessários como cumprimentos ou forçar respostas em formatos específicos como XML, JSON. [No caso da API Claude, essa técnica pode ser usada submetendo mensagens `Assistant` junto com mensagens `User` ao fazer a chamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevenção de preguiça (Patch de Halloween 12024.10.31.)
Após escrever este artigo pela primeira vez, embora tenha passado por algumas melhorias de prompt e especificação de instruções adicionais uma ou duas vezes no meio, de qualquer forma, não houve grandes problemas ao aplicar este sistema de automação por 4 meses.

No entanto, a partir de cerca das 18h do horário da Coreia em 12024.10.31., quando solicitei trabalho de tradução de posts recém-escritos, continuou ocorrendo o fenômeno anômalo de traduzir apenas a primeira parte 'TL;DR' do post e depois interromper arbitrariamente a tradução.

Como abordei as causas prováveis e métodos de solução desse problema em [post separado](/posts/does-ai-hate-to-work-on-halloween), consulte esse artigo.

### Prompt do sistema completo
O resultado do design de prompt após passar pelas etapas acima pode ser verificado na [próxima parte](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2).

## Leitura Adicional
Continua na [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
