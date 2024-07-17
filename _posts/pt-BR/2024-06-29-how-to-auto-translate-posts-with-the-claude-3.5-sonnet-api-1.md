---
title: Como traduzir automaticamente postagens com a API Claude 3.5 Sonnet (1)
description: >-
  Apresento brevemente o modelo Claude 3.5 Sonnet recentemente lançado, compartilho o processo de design do prompt para aplicá-lo à tradução multilíngue das postagens deste blog e o resultado final do prompt concluído.
categories:
- Blogging
tags:
- Jekyll
- LLM
---
## Introdução
Recentemente, introduzi a API Claude 3.5 Sonnet da Anthropic para tradução multilíngue das postagens do blog. Gostaria de abordar as razões para escolher a API Claude 3.5 Sonnet, o método de design do prompt e a implementação da automação através da integração da API com um script Python. Como o conteúdo que pretendo cobrir é bastante extenso, não será uma única postagem, mas uma série, e esta é a primeira postagem da série.

## Sobre o Claude 3.5 Sonnet
Os modelos da série Claude 3 são fornecidos em versões Haiku, Sonnet e Opus, de acordo com o tamanho do modelo.  
![Distinção de níveis do modelo Claude 3](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-pricing.png)  
> Fonte da imagem: [Página oficial da API Claude da Anthropic](https://www.anthropic.com/api)

E no horário da Coreia, em 21 de junho de 2024, a Anthropic lançou seu mais recente modelo de linguagem, o [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet). De acordo com o anúncio da Anthropic, ele demonstra um desempenho de inferência que supera o Claude 3 Opus com o mesmo custo e velocidade do Claude 3 Sonnet existente, e geralmente é considerado superior ao modelo concorrente GPT-4 em áreas de composição, raciocínio linguístico, compreensão multilíngue e tradução.  
![Imagem de introdução do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/Claude-3-5-Sonnet.webp)  
![Resultados do benchmark de desempenho do Claude 3.5 Sonnet](/assets/img/how-to-auto-translate-posts-with-the-claude-3.5-sonnet-api/LLM-benchmark.webp)  
> Fonte das imagens: [Site da Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet)

## Razões para adotar o Claude 3.5 para tradução de postagens
Mesmo sem necessariamente usar modelos de linguagem como Claude 3.5 ou GPT-4, existem APIs de tradução comerciais existentes como Google Translate ou DeepL. A razão pela qual decidi usar um LLM para fins de tradução é que, diferentemente de outros serviços de tradução comerciais, o usuário pode fornecer informações contextuais adicionais ou requisitos além do texto principal, como o propósito de escrita do texto ou os principais tópicos, através do design do prompt, e o modelo pode fornecer uma tradução que considera o contexto de acordo com isso. Embora o DeepL e o Google Translate geralmente mostrem uma excelente qualidade de tradução, devido à limitação de não compreenderem bem o tema ou o contexto geral do texto, quando solicitados a traduzir textos longos sobre tópicos especializados, em vez de conversas cotidianas, os resultados da tradução tendem a ser relativamente pouco naturais. Em particular, como mencionado anteriormente, o Claude é considerado relativamente superior em áreas de composição, raciocínio linguístico, compreensão multilíngue e tradução em comparação com seu modelo concorrente GPT-4, então julguei que seria adequado para a tarefa de traduzir os textos relacionados à engenharia publicados neste blog para vários idiomas.

## Design do Prompt
### Princípios básicos do design do prompt
Para obter resultados satisfatórios que atendam ao propósito de um modelo de linguagem, é necessário fornecer um prompt apropriado. Embora o design do prompt possa parecer intimidante, na verdade, "como fazer um bom pedido" não é muito diferente se o interlocutor for um modelo de linguagem ou uma pessoa, então não é tão difícil se abordado desse ponto de vista. É bom explicar claramente a situação atual e os requisitos de acordo com os cinco Ws e um H, e adicionar alguns exemplos específicos, se necessário. Existem inúmeras dicas e técnicas para o design de prompts, mas a maioria delas deriva dos princípios básicos mencionados acima.

### Atribuição de papel e explicação da situação (quem, por quê)
Primeiro, atribuí ao Claude 3.5 o papel de "tradutor técnico profissional" e forneci informações contextuais sobre o usuário como "um blogueiro de engenharia que escreve principalmente sobre matemática, física e ciência de dados".
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. 

### Transmissão de requisitos gerais (o quê)
Em seguida, solicitei a tradução do texto formatado em markdown fornecido pelo usuário de {source_lang} para {target_lang}, mantendo o formato.
> Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format.

> Ao chamar a API Claude, as posições {source_lang} e {target_lang} no prompt são preenchidas com as variáveis de idioma de origem e destino, respectivamente, através da funcionalidade f-string do script Python.
{: .prompt-info }

### Especificação de requisitos e exemplos (como)
Até as etapas anteriores, às vezes é suficiente para obter os resultados desejados, mas para tarefas mais complexas, podem ser necessárias explicações adicionais. Neste caso, adicionei as seguintes condições:

#### Tratamento quando o texto original inclui idiomas diferentes do idioma de origem
Ao escrever o texto original em coreano, ao introduzir a definição de um conceito pela primeira vez ou ao usar alguns termos técnicos, muitas vezes incluo a expressão em inglês entre parênteses, como '*중성자 감쇠 (Neutron Attenuation)*'. Ao traduzir tais expressões, havia um problema de inconsistência no método de tradução, às vezes mantendo os parênteses e outras vezes omitindo o inglês entre parênteses, então adicionei a seguinte frase ao prompt:
> If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French.

#### Tratamento de links para outras postagens
Algumas postagens incluem links para outras postagens, e frequentemente ocorria o problema de interpretar a parte do caminho da URL como algo que precisava ser traduzido, quebrando os links internos. Esse problema foi resolvido adicionando esta frase ao prompt:
> Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'.

#### Saída apenas do resultado da tradução como resposta
Por fim, apresenta-se a seguinte frase para produzir apenas o resultado da tradução como saída, sem adicionar outras palavras na resposta:
> The output should only contain the translated text.

### Prompt finalizado
O resultado do design do prompt após passar pelas etapas acima é o seguinte:
> You are a professional technical translator. Your client is an engineering blogger who writes mainly about math, physics (especially nuclear physics, quantum mechanics, and quantum information theory), and data science. Translate the markdown-formatted text provided by the user from {source_lang} to {target_lang} while preserving the format. If the provided text contains language other than {source_lang}, please leave that part untouched. For example, '중성자 감쇠 (Neutron Attenuation)' translates to 'Neutron Attenuation' in English and 'Atténuation des neutrons (Neutron Attenuation)' in French. Also, if the provided text contains links in markdown format, please translate the link text and the fragment part of the URL into {target_lang}, but keep the path part of the URL intact. For example, the German translation of '\[중성자 상호작용과 반응단면적\]\(/posts/Neutron-Interactions-and-Cross-sections/#단면적cross-section-또는-미시적-단면적microscopic-cross-section\)' would be '\[Neutronenwechselwirkungen und Wirkungsquerschnitte\]\(/posts/Neutron-Interactions-and-Cross-sections/#wirkungsquerschnitt-cross-section-oder-mikroskopischer-wirkungsquerschnitt-microscopic-cross-section\)'. The output should only contain the translated text.