---
title: "Como Traduzir Posts Automaticamente com a API do Claude Sonnet 4 (1) - Design de Prompt"
description: "Aborda o processo de design de prompts para tradução multilíngue de arquivos de texto markdown e automação do trabalho com Python aplicando chaves de API da Anthropic/Gemini e os prompts criados. Este post é o primeiro da série, apresentando métodos e processos de design de prompt."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/
  - /posts/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api-1/
---

## Introdução
Desde a introdução da API do Claude 3.5 Sonnet da Anthropic para tradução multilíngue de posts do blog em junho de 12024, após várias melhorias de prompt e script de automação, além de atualizações de versão do modelo, tenho operado satisfatoriamente esse sistema de tradução por quase um ano. Nesta série, pretendo abordar as razões para escolher o modelo Claude Sonnet no processo de introdução e posteriormente adicionar o Gemini 2.5 Pro, métodos de design de prompt, e implementação de integração de API e automação através de scripts Python.
A série consiste em 2 artigos, e este que você está lendo é o primeiro da série.
- Parte 1: Introdução aos modelos Claude Sonnet/Gemini 2.5 e razões para seleção, engenharia de prompt (texto atual)
- Parte 2: [Criação e aplicação de script de automação Python utilizando API](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)

## Sobre o Claude Sonnet
Os modelos da série Claude são fornecidos nas versões Haiku, Sonnet e Opus de acordo com o tamanho do modelo.
![Classificação de níveis do modelo Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-pricing.png)
> Fonte da imagem: [Página oficial da API Anthropic Claude](https://www.anthropic.com/api)

> (Adicionado em 12025.05.29.)
> A imagem foi capturada há um ano, então as tarifas por token são baseadas na versão antiga Claude 3, mas a classificação Haiku, Sonnet, Opus por tamanho de modelo ainda é válida. Com base no final de maio de 12025, a precificação de cada modelo fornecido pela Anthropic é a seguinte.
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

E o modelo de linguagem [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) lançado pela Anthropic no horário da Coreia em 21 de junho do [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar) 12024 mostra desempenho de raciocínio superior ao Claude 3 Opus com o mesmo custo e velocidade do Claude 3 Sonnet existente, e a avaliação dominante é que geralmente mostra vantagens em escrita, raciocínio linguístico, compreensão multilíngue e tradução em comparação com o modelo concorrente GPT-4.
![Imagem de introdução do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/Claude-3-5-Sonnet.webp)
![Resultados de benchmark de desempenho do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-3-5-benchmark.webp)
> Fonte da imagem: [Anthropic Newsroom](https://www.anthropic.com/news/claude-3-5-sonnet)

## Razões para Introduzir o Claude 3.5 para Tradução de Posts
Mesmo sem modelos de linguagem como Claude 3.5 ou GPT-4, existem APIs de tradução comerciais como Google Translate ou DeepL. Ainda assim, a razão para decidir usar LLM para fins de tradução é que, diferentemente de outros serviços de tradução comerciais, os usuários podem fornecer informações de contexto adicionais ou requisitos além do texto principal, como o propósito de escrita ou tópicos principais do texto através do design de prompt, e o modelo pode fornecer traduções considerando o contexto de acordo.

Embora DeepL ou Google Translate também mostrem qualidade de tradução geralmente excelente, eles têm limitações de não compreender bem o tópico ou contexto geral do texto e não conseguir transmitir requisitos complexos separadamente. Por isso, quando solicitados a traduzir textos longos sobre tópicos especializados que não são conversas cotidianas, os resultados de tradução podem ser relativamente não naturais, e há o problema de ser difícil produzir saídas que correspondam exatamente ao formato específico necessário (markdown, YAML frontmatter, etc.).

Especialmente, como mencionado acima, Claude tinha muitas avaliações de ser relativamente superior em escrita, raciocínio linguístico, compreensão multilíngue e tradução em comparação com o modelo concorrente GPT-4, e quando testei diretamente de forma simples, também mostrou qualidade de tradução mais suave que o GPT-4, então julguei adequado para o trabalho de traduzir artigos relacionados à engenharia registrados neste blog para várias línguas quando estava considerando a introdução em junho de 12024.

## Histórico de Atualizações
### 12024.07.01.
Como resumido em [artigo separado](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/), [completei o trabalho inicial de aplicar o plugin Polyglot e modificar `_config.yml`{: .filepath}, cabeçalho html e sitemap de acordo.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/44afc4f9bac0d689842d9373c9daa7e0220659e7) Em seguida, [adotei o modelo Claude 3.5 Sonnet para fins de tradução e apliquei após completar a implementação inicial e verificação do script Python de integração de API abordado nesta série.](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3cadd28fd72bb2a6e1b64addfe000d99ca5ab51b)

### 12024.10.31.
Em 22 de outubro de 12024, a Anthropic anunciou a versão atualizada da API do Claude 3.5 Sonnet ("claude-3-5-sonnet-20241022") e Claude 3.5 Haiku. No entanto, devido ao [problema mencionado posteriormente](#prevenção-de-preguiça-patch-de-halloween-120241031), ainda estou aplicando a API "claude-3-5-sonnet-20240620" existente neste blog.

### 12025.04.02.
[Mudei o modelo aplicado de "claude-3-5-sonnet-20240620" para "claude-3-7-sonnet-20250219".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/aa281979ad360081116348ef8240887ecb50e953)

### 12025.05.29.
[Mudei o modelo aplicado de "claude-3-7-sonnet-20250219" para "claude-sonnet-4-20250514".](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/68c67d8c7e94edb884fa3206d0c78eeef67d8a65)

![Resultados de benchmark de desempenho do Claude 4](/assets/img/how-to-auto-translate-posts-with-the-claude-sonnet-4-api/claude-4-benchmark.webp)
> Fonte da imagem: [Anthropic Newsroom](https://www.anthropic.com/news/claude-4)

Embora possa haver diferenças dependendo das condições de uso, geralmente desde o lançamento do modelo Claude 3.7 Sonnet, há pouca discordância de que Claude é o modelo mais poderoso em codificação. A própria Anthropic também está promovendo ativamente o desempenho superior de codificação em comparação com modelos concorrentes como OpenAI ou Google como uma das principais vantagens de seus modelos. No anúncio do Claude Opus 4 e Claude Sonnet 4 desta vez, também se pode confirmar que continuam a tendência de visar desenvolvedores como principal grupo de clientes, enfatizando o desempenho de codificação.

Claro, olhando os resultados de benchmark divulgados, houve melhorias gerais em itens além de codificação, e para o trabalho de tradução abordado neste artigo, as melhorias de desempenho em perguntas e respostas multilíngues (MMMLU) ou resolução de problemas matemáticos (AIME 2025) parecem ser particularmente eficazes. Como resultado de testes simples diretos, pude confirmar que os resultados de tradução do Claude Sonnet 4 são superiores ao modelo anterior Claude 3.7 Sonnet em naturalidade de expressão, especialização e consistência no uso de terminologia.

> No momento atual, pelo menos para o trabalho de traduzir textos escritos em coreano de natureza técnica como os abordados neste blog para múltiplas línguas, acredito que os modelos Claude ainda são os melhores. No entanto, recentemente o desempenho dos modelos Gemini do Google tem melhorado visivelmente, e em maio deste ano até lançaram o modelo Gemini 2.5, embora ainda esteja em estágio Preview.
> Quando comparei os modelos Gemini 2.0 Flash com Claude 3.7 Sonnet e Claude Sonnet 4, julguei que o desempenho de tradução do Claude era superior, mas o desempenho multilíngue do Gemini também é bastante excelente, e apesar de estar em estágio Preview, a capacidade de resolução de problemas matemáticos e físicos e habilidade descritiva do Gemini 2.5 Preview 05-06 é na verdade superior até mesmo ao Claude Opus 4, então não posso garantir como será quando esse modelo for oficialmente lançado e comparado novamente.
> Considerando que é possível usar até uma certa quantidade de uso como [nível gratuito (Free Tier)](https://ai.google.dev/gemini-api/docs/rate-limits#current-rate-limits) e as tarifas de API mais baratas que Claude mesmo no nível pago (Paid Tier), a competitividade de preço do Gemini é muito superior, então se o desempenho for equivalente, o Gemini pode se tornar uma alternativa razoável. Como o Gemini 2.5 ainda está em estágio Preview, julgo que é cedo para aplicar na automação real, então não estou considerando no momento, mas planejo testar quando a versão oficial for lançada no futuro.
{: .prompt-tip }

### 12025.07.04.
- [Adição de funcionalidade de tradução incremental](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/978032f52c7d85ecb6b213233d5404d844402965)
- Dualização de modelo aplicado por idioma de destino da tradução ([Commit 3890c82](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/3890c820c1f3df34f8e4686b8903ca4ee770ba15), [Commit fe0fc63](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/fe0fc63ae4e2764f3dfe24ff259b4477f120b9ed))
  - Uso de "gemini-2.5-pro" para tradução para inglês, chinês taiwanês e alemão
  - Continuação do uso do "claude-sonnet-4-20250514" existente para tradução para japonês, espanhol, português e francês
- Considerou-se aumentar o valor de `temperature` de `0.0` para `0.2`, mas foi revertido ao original

Em 4 de julho de 12025, finalmente os modelos Gemini 2.5 Pro e Gemini 2.5 Flash foram oficialmente lançados, saindo do estágio Preview. Embora o número de exemplos usados seja limitado, quando testei pessoalmente, baseado na tradução para inglês, até mesmo o Gemini 2.5 Flash processava algumas partes de forma mais natural que o Claude Sonnet 4 existente. Considerando que as tarifas por token de saída dos modelos Gemini 2.5 Pro e Flash são 1,5 vezes e 6 vezes mais baratas que o Claude Sonnet 4, respectivamente, mesmo no nível pago, pode-se dizer que é o modelo mais competitivo no momento atual de julho de 12025 para inglês. No entanto, no caso do modelo Gemini 2.5 Flash, talvez devido às limitações de um modelo pequeno, embora os resultados de saída sejam geralmente excelentes, havia problemas como quebra de alguns formatos de documentos markdown ou links internos, tornando-o inadequado para trabalhos complexos de tradução e processamento de documentos. Além disso, embora o Gemini 2.5 Pro mostre desempenho claramente superior para inglês, **a maioria dos posts em português (pt-BR)** e alguns posts em espanhol mostraram dificuldades de processamento, talvez devido à quantidade insuficiente de dados de treinamento. Examinando os erros ocorridos, a maioria eram problemas causados pela confusão entre caracteres similares como 'í' e 'i', 'ó' e 'o', 'ç' e 'c', e 'ã' e 'a'. Além disso, para francês, embora não houvesse problemas como os mencionados acima, às vezes as frases eram excessivamente prolixas, resultando em legibilidade inferior comparada ao Claude Sonnet 4.

Como não conheço bem idiomas além do inglês, é difícil fazer uma comparação detalhada e precisa, mas comparando a qualidade de resposta aproximada por idioma, foi o seguinte:
- Inglês, alemão, chinês taiwanês: Gemini superior
- Japonês, francês, espanhol, português: Claude superior

Além disso, adicionei funcionalidade de tradução incremental (Incremental Translation) ao script de tradução de posts. Embora me esforce para revisar cuidadosamente ao escrever inicialmente, ainda assim às vezes descubro erros menores como erros de digitação após publicar o artigo, ou me ocorrem conteúdos que seria bom adicionar/modificar. No entanto, nesses casos, embora a quantidade modificada seja limitada em relação ao artigo inteiro, o script existente tinha que traduzir e produzir todo o artigo do início ao fim novamente, o que era um pouco ineficiente em termos de uso de API. Por isso, adicionei uma funcionalidade que se integra com git para realizar comparação de versões do texto original em coreano, extrair as partes alteradas do texto original em formato diff, inserir como prompt junto com o texto completo da tradução anterior às alterações, e receber um patch diff para a tradução como saída para modificar seletivamente apenas as partes necessárias. Como a tarifa por token de entrada é significativamente mais barata que a tarifa por token de saída, pode-se esperar um efeito significativo de redução de custos, e portanto, no futuro, mesmo quando modificar apenas uma parte do artigo, será possível aplicar o script de tradução automática sem hesitação, sem modificar diretamente as traduções para cada idioma.

Enquanto isso, `temperature` é um parâmetro que ajusta quanta aleatoriedade dar ao modelo de linguagem ao selecionar a próxima palavra no processo de gerar uma resposta para cada palavra. Tem um valor de número real não negativo (\*como mencionarei posteriormente, geralmente na faixa de $[0,1]$ ou $[0,2]$), onde valores pequenos próximos a 0 geram respostas mais determinísticas e consistentes, e valores maiores geram respostas mais diversas e criativas.
O propósito da tradução é transmitir o significado e tom do texto original para outro idioma de forma mais precisa e consistente possível, não criar criativamente novo conteúdo, então para garantir precisão, consistência e previsibilidade da tradução, deve-se usar um valor baixo de `temperature`. No entanto, definir `temperature` como `0.0` faz com que o modelo sempre selecione apenas a palavra com maior probabilidade, o que em alguns casos pode tornar a tradução muito próxima da tradução literal ou gerar frases não naturais e rígidas, então para evitar que a resposta seja excessivamente rígida e dar alguma flexibilidade, considerou-se aumentar ligeiramente o valor de `temperature` para `0.2`, mas devido ao problema de redução drástica na precisão de processamento de links complexos incluindo identificadores de fragmento (Fragment identifier), decidiu-se não aplicar.

> \* Na maioria dos casos, o valor de `temperature` usado praticamente está na faixa de 0 a 1, e a faixa permitida na API Anthropic também é $[0,1]$. As APIs OpenAI ou Gemini permitem valores de `temperature` na faixa mais ampla de $[0,2]$, mas mesmo que a faixa de `temperature` seja expandida para $[0,2]$, a escala não dobra, e o significado de $T=1$ é o mesmo que modelos que usam a faixa $[0,1]$.
>
> Quando modelos de linguagem geram saídas, internamente funcionam como uma espécie de função que recebe o prompt e tokens de saída anteriores como entrada e responde com a distribuição de probabilidade do próximo token, e o resultado do experimento de acordo com essa distribuição de probabilidade é determinado como o próximo token e produzido. O valor de referência que usa essa distribuição de probabilidade como está é $T=1$, onde quando $T<1$, a distribuição de probabilidade se torna estreita e pontiaguda, fazendo escolhas mais consistentes focando principalmente nas palavras com maior probabilidade, enquanto quando $T>1$, ao contrário, nivela a distribuição de probabilidade para artificialmente aumentar a probabilidade de seleção de palavras com baixa probabilidade de ocorrência que normalmente quase não seriam selecionadas.
>
> Na região $T>1$, a qualidade de saída pode se deteriorar e se tornar imprevisível, incluindo tokens que saem do contexto na resposta ou gerando frases gramaticalmente incorretas que não fazem sentido. Para a maioria das tarefas, especialmente em ambientes de produção, é bom definir o valor de `temperature` dentro da faixa $[0,1]$, e valores maiores que 1 devem ser usados experimentalmente para fins como brainstorming, assistência criativa (geração de rascunhos de cenários, etc.) quando se deseja saídas diversas, mas como o risco de alucinação ou erros gramaticais e lógicos também aumenta, é desejável pressupor intervenção e revisão humana em vez de automação.
>
> Para conteúdo mais detalhado sobre `temperature` de modelos de linguagem, é bom consultar os seguintes artigos.
> - [Tamanna, *Understanding LLM Temperature* (2025).](https://medium.com/@tam.tamanna18/understanding-llm-temperature-7d838277a7d9)
> - [Tickr Data, *The Impact of Temperature on LLM Performance* (2023).](https://www.tickr.com/blog/posts/impact-of-temperature-on-llms/)
> - [Anik Das, *Temperature in Prompt Engineering* (2025).](https://peerlist.io/anikdas/articles/temperature-in-prompt-engineering)
> - [Peeperkorn et al., *Is Temperature the Creativity Parameter of LLMs?*, arXiv:2405.00492 (2024).](https://arxiv.org/abs/2405.00492)
> - [Colt Steele, *Understanding OpenAI's Temperature Parameter* (2023).](https://www.coltsteele.com/tips/understanding-openai-s-temperature-parameter)
> - [Damon Garn, *Understanding the role of temperature settings in AI output*, TechTarget (2025).](https://www.techtarget.com/searchenterpriseai/tip/Understanding-the-role-of-temperature-settings-in-AI-output)
{: .prompt-info }

## Design de Prompt
### Princípios Básicos ao Solicitar Algo
Para obter resultados satisfatórios que atendam ao propósito de um modelo de linguagem, é necessário fornecer um prompt apropriado. Embora o design de prompt possa parecer intimidante, na verdade, o 'método de solicitar algo bem' não é muito diferente, seja o interlocutor um modelo de linguagem ou uma pessoa, então se abordarmos dessa perspectiva, não é muito difícil. Explicar claramente a situação atual e solicitações de acordo com os princípios das cinco perguntas (quem, o quê, quando, onde, por quê) e, se necessário, adicionar alguns exemplos específicos também é bom. Existem inúmeras dicas e técnicas sobre design de prompt, mas a maioria deriva dos princípios básicos que serão mencionados posteriormente.

#### Tom Geral
Há muitos relatos de que quando prompts são escritos e inseridos em tom de solicitação educada em vez de tom de comando autoritário, modelos de linguagem produzem respostas de maior qualidade. Geralmente na sociedade, quando solicitamos algo a outras pessoas, a probabilidade de a outra pessoa realizar a tarefa solicitada com mais sinceridade aumenta quando solicitamos educadamente em vez de comandar autoritariamente, e os modelos de linguagem parecem aprender e imitar esses padrões de resposta das pessoas.

#### Atribuição de Papel e Explicação da Situação (Quem, Por quê)
Primeiro, atribuí o papel de *'tradutor técnico profissional (professional technical translator)'* e forneci informações contextuais sobre o usuário como *"blogueiro de engenharia que escreve principalmente sobre matemática, física e ciência de dados"*.

```xml
<role>You are a professional translator specializing in technical and scientific fields. 
Your client is an engineering blogger who writes mainly about math, physics \
(especially nuclear physics, electromagnetism, quantum mechanics, \
and quantum information theory), and data science for his Jekyll blog.</role>
```

#### Transmissão de Solicitações no Quadro Geral (O quê)
Em seguida, solicitei traduzir o texto em formato markdown fornecido pelo usuário de {source_lang} para {target_lang} mantendo o formato.

```xml
<task>Please translate the provided <format>markdown</format> text \
from <lang>{source_lang}</lang> to <lang>{target_lang}</lang> \
while preserving the format.</task> 
```

> Ao chamar a API Claude, as variáveis de idioma de origem e destino da tradução são inseridas nos lugares {source_lang} e {target_lang} do prompt através da funcionalidade f-string do script Python.
{: .prompt-info }

#### Especificação de Requisitos e Exemplos (Como)
Para tarefas simples, os passos anteriores podem ser suficientes para obter os resultados desejados, mas para tarefas complexas, explicações adicionais podem ser necessárias.

Quando as condições de requisito são complexas e múltiplas, em vez de descrever cada item separadamente, listá-los de forma concisa melhora a legibilidade e facilita a compreensão para quem lê (seja humano ou modelo de linguagem). Além disso, fornecer exemplos junto quando necessário também é útil.
Neste caso, adicionei as seguintes condições.

##### Processamento do YAML front matter
No YAML front matter localizado na primeira parte de posts escritos em markdown para upload no blog Jekyll, são registradas informações de 'title', 'description', 'categories' e 'tags'. Por exemplo, o YAML front matter deste artigo atual é o seguinte.

```yaml
---
title: "Claude Sonnet 4 API로 포스트 자동 번역하는 법 (1) - 프롬프트 디자인"
description: "마크다운 텍스트 파일의 다국어 번역을 위한 프롬프트를 디자인하고, Anthropic/Gemini API 키와 작성한 프롬프트를 적용하여 Python으로 작업을 자동화하는 과정을 다룬다. 이 포스트는 해당 시리즈의 첫 번째 글로, 프롬프트 디자인 방법과 과정을 소개한다."
categories: [AI & Data, GenAI]
tags: [Jekyll, Markdown, LLM]
image: /assets/img/technology.webp
---
```

No entanto, ao traduzir posts, as tags de título (title) e descrição (description) devem ser traduzidas para múltiplos idiomas, mas para consistência de URL de posts, é conveniente para manutenção deixar os nomes de categorias (categories) e tags (tags) em inglês sem traduzir. Portanto, dei a seguinte instrução para não traduzir tags além de 'title' e 'description'. Como o modelo já deve ter aprendido e conhecer informações sobre YAML front matter, essa explicação é suficiente na maioria dos casos.

```xml
- <condition>please do not modify the YAML front matter except for the 'title' and 'description' tags, \
  under any circumstances, regardless of the language you are translating to.</condition>
```

> Adicionei a frase "under any circumstances, regardless of the language you are translating to" para enfatizar que outras tags do YAML front matter não devem ser modificadas **sem exceção**.
{: .prompt-tip }

(Atualização em 12025.04.02.)
Além disso, instruí para escrever o conteúdo da tag description em quantidade apropriada considerando SEO da seguinte forma.

```xml
- <condition>For the description tag, this is a meta tag that directly impacts SEO. 
  Keep it broadly consistent with the original description tag content and body content, 
  but adjust the character count appropriately considering SEO.</condition>
```

##### Processamento quando o texto original fornecido contém idiomas diferentes do idioma de origem
Ao escrever o texto original em coreano, ao introduzir a definição de algum conceito pela primeira vez ou usar alguns termos técnicos, frequentemente registro expressões em inglês entre parênteses como '*감쇠 중성자 (Neutron Attenuation)*'. Ao traduzir essas expressões, havia o problema de métodos de tradução inconsistentes, às vezes mantendo os parênteses e outras vezes omitindo o inglês registrado nos parênteses, então estabeleci as seguintes diretrizes detalhadas.
- Para termos técnicos,
  - Ao traduzir para idiomas não baseados em alfabeto romano como japonês, manter o formato 'expressão traduzida(expressão em inglês)'.
  - Ao traduzir para idiomas baseados em alfabeto romano como espanhol, português, francês, permitir tanto notação única 'expressão traduzida' quanto notação combinada 'expressão traduzida(expressão em inglês)', deixando o modelo escolher autonomamente o mais apropriado entre os dois.
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

##### Processamento de Links para Outros Posts
Alguns posts contêm links para outros posts, mas na fase de teste, quando não forneci diretrizes separadas sobre isso, frequentemente interpretava até a parte do caminho da URL como alvo de tradução e a modificava, causando quebra de links internos. Esse problema foi resolvido adicionando esta cláusula ao prompt.

```xml
- <condition><if>the provided text contains links in markdown format, \
  please translate the link text and the fragment part of the URL into {target_lang}, \
  but keep the path part of the URL intact.</if></condition>
```

(Atualização em 12025.04.06.)
Fornecer as diretrizes acima faz com que a parte do caminho dos links seja processada corretamente durante a tradução, reduzindo consideravelmente a frequência de quebra de links, mas para links que incluem identificadores de fragmento (Fragment identifier), ainda havia a limitação de que o modelo de linguagem tinha que preencher a parte do identificador de fragmento por inferência aproximada, a menos que conhecesse o conteúdo do artigo de destino do link, tornando impossível a resolução fundamental do problema. Por isso, melhorei o script Python e o prompt para fornecer informações contextuais sobre outros posts vinculados por links na tag XML `<reference_context>` do prompt do usuário e processar a tradução de links de acordo com esse contexto. Como resultado da aplicação dessa atualização, foi possível prevenir a maioria dos problemas de quebra de links, e para artigos de série intimamente conectados, também se pode esperar o efeito de fornecer traduções mais consistentes em vários posts.

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
Finalmente, apresento a seguinte frase para produzir apenas os resultados de tradução como saída sem adicionar outras palavras na resposta.

```xml
<important>In any case, without exception, the output should contain only the translation results, \
without any text such as "Here is the translation of the text provided, preserving the markdown format:" \
or "```markdown" or something of that nature!!</important>
```

### Técnicas Adicionais de Design de Prompt
No entanto, diferentemente de solicitar trabalho a humanos, no caso de modelos de linguagem, também existem técnicas adicionais que se aplicam especialmente.
Embora existam muitos materiais úteis sobre isso na web, resumindo algumas dicas representativas que podem ser usadas de forma universalmente útil:
Referi-me principalmente ao [guia de engenharia de prompt da documentação oficial da Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).

#### Estruturação Utilizando Tags XML
Na verdade, isso já vinha sendo usado anteriormente. Para prompts complexos que incluem vários contextos, instruções, formatos e exemplos, usar apropriadamente tags XML como `<instructions>`, `<example>`, `<format>` ajuda o modelo de linguagem a interpretar o prompt com precisão e produzir saídas de alta qualidade que atendem à intenção. O repositório GitHub [GENEXIS-AI/prompt-gallery](https://github.com/GENEXIS-AI/prompt-gallery/blob/main/prompt_xml.md) tem tags XML úteis para escrever prompts bem organizadas, então recomendo consultá-lo.

#### Técnica de Raciocínio Passo a Passo (CoT, Chain-of-Thought)
Para tarefas que requerem um nível considerável de raciocínio, como resolução de problemas matemáticos ou escrita de documentos complexos, induzir o modelo de linguagem a pensar no problema dividindo-o em etapas pode melhorar significativamente o desempenho. No entanto, neste caso, o tempo de atraso de resposta pode aumentar, e essa técnica nem sempre é útil para todas as tarefas, então tenha cuidado.

#### Técnica de Encadeamento de Prompts (prompt chaining)
Para realizar tarefas complexas, pode haver limitações em responder com um único prompt. Neste caso, também se pode considerar usar o método de dividir todo o fluxo de trabalho em várias etapas desde o início, apresentar prompts especializados para cada etapa e transmitir a resposta obtida na etapa anterior como entrada para a próxima etapa. Essa técnica é chamada de encadeamento de prompts (prompt chaining).

#### Pré-preenchimento do Início da Resposta
Ao inserir um prompt, fornecendo antecipadamente a primeira parte do conteúdo a ser respondido e fazendo com que escreva a resposta que seguirá, é possível pular saudações desnecessárias ou forçar respostas em formatos específicos como XML, JSON. [No caso da API Anthropic, essa técnica pode ser usada submetendo não apenas mensagens `User` mas também mensagens `Assistant` ao fazer a chamada.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)

#### Prevenção de Preguiça (Patch de Halloween 12024.10.31.)
Embora tenha passado por algumas melhorias de prompt e especificação de instruções adicionais uma ou duas vezes após escrever este artigo inicialmente, de qualquer forma, não houve grandes problemas ao aplicar este sistema de automação por 4 meses.

No entanto, a partir de cerca das 18h do horário da Coreia em 12024.10.31., quando atribuí o trabalho de tradução de posts recém-escritos, continuou ocorrendo o fenômeno anômalo de traduzir apenas a primeira parte 'TL;DR' do post e depois interromper arbitrariamente a tradução.

As causas prováveis desse problema e métodos de solução foram abordados em [post separado](/posts/does-ai-hate-to-work-on-halloween), então consulte esse artigo.

### Prompt do Sistema Completo
O resultado do design de prompt após passar pelas etapas acima pode ser verificado na [próxima parte](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2).

## Leitura Adicional
Continuado na [Parte 2](/posts/how-to-auto-translate-posts-with-the-claude-sonnet-4-api-2)
