---
title: Criando e Gerenciando um Blog no GitHub Pages
description: Conheça as características e diferenças entre páginas web estáticas e dinâmicas, aprenda sobre Geradores de Sites Estáticos (Static Site Generator) e hospede seu blog Jekyll no GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
---
Comecei a hospedar meu blog no GitHub Pages usando Jekyll no início de 12021 do [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar). No entanto, como não documentei adequadamente o processo de instalação na época, tive algumas dificuldades na manutenção posterior. Por isso, decidi registrar brevemente o processo de instalação e os métodos de manutenção.

(+ Atualizado em 12024.12)

## 1. Geradores de Sites Estáticos & Hospedagem Web
### 1-1. Páginas Web Estáticas vs Páginas Web Dinâmicas
#### Páginas Web Estáticas (Static Web Page)
- Páginas web que entregam dados armazenados no servidor diretamente ao usuário
- O servidor web entrega páginas pré-armazenadas em resposta às solicitações do usuário
- Os usuários veem a mesma página web, a menos que os dados armazenados no servidor sejam alterados
- Como apenas os arquivos solicitados são enviados, não há necessidade de processamento adicional, resultando em respostas geralmente mais rápidas
- Consistem apenas de arquivos simples, então apenas um servidor web é necessário, tornando os custos de implementação mais baixos
- Os serviços são limitados porque mostram apenas informações pré-armazenadas
- Adições, modificações e exclusões de dados devem ser feitas manualmente pelo administrador
- Estrutura mais fácil para os mecanismos de busca rastrearem, sendo relativamente mais vantajosa para otimização de mecanismos de busca (SEO)

#### Páginas Web Dinâmicas (Dynamic Web Page)
- Páginas web que processam dados armazenados no servidor com scripts antes de entregá-los
- O servidor web interpreta as solicitações do usuário, processa os dados e entrega a página web gerada
- Os usuários veem páginas web que variam de acordo com a situação, hora, solicitação, etc.
- As respostas são relativamente mais lentas porque os scripts precisam ser processados antes da entrega da página
- Custos adicionais de implementação são incorridos porque um servidor de aplicativos é necessário além do servidor web
- Diversos serviços são possíveis porque as informações podem ser combinadas e fornecidas dinamicamente
- Dependendo da estrutura da página web, os usuários podem adicionar, modificar e excluir dados através do navegador
  
### 1-2. Geradores de Sites Estáticos (SSG, Static Site Generator)
- Ferramentas que geram páginas web estáticas com base em dados brutos (geralmente arquivos de texto em formato markdown) e modelos predefinidos
- Automatizam o processo de construção e publicação de páginas web sem a necessidade de escrever páginas HTML individuais, bastando escrever posts em markdown
- Ex: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Serviço de hospedagem de páginas web estáticas gratuito fornecido pelo GitHub
- Cada conta pode hospedar 1 página web pessoal representativa e um número ilimitado de páginas de documentação de projetos por repositório
- Após criar um repositório com o nome no formato '{username}.github.io' correspondente ao seu nome de usuário do GitHub, você pode enviar diretamente páginas HTML construídas para o repositório ou usar o GitHub Actions para construção e implantação
- Se você possui um domínio próprio, pode conectá-lo nas configurações para usar um endereço de domínio diferente em vez do domínio padrão '{username}.github.io'

## 2. Escolhendo um SSG e um tema

### 2-1. Por que escolhi o Jekyll
Existem vários SSGs como Jekyll, Hugo, Gatsby, etc., mas decidi usar o Jekyll. Os critérios que considerei ao escolher um SSG e as razões para escolher o Jekyll são os seguintes:
- Posso minimizar tentativas e erros desnecessários e me concentrar na escrita e operação do blog?
  - Jekyll é o gerador de sites estáticos oficialmente suportado pelo GitHub Pages. Claro, outros SSGs como Hugo e Gatsby também podem ser hospedados no GitHub Pages, e há a opção de usar serviços de hospedagem completamente diferentes como o Netlify, mas na verdade, para operar um blog pessoal deste tamanho, não importa muito tecnicamente qual SSG foi usado para construí-lo, nem a velocidade de construção ou desempenho, então decidi que seria melhor usar algo com manutenção mais simples e com mais documentação de referência.
  - Jekyll também tem o período de desenvolvimento mais longo em comparação com outros concorrentes como Hugo e Gatsby. Isso significa que está bem documentado e há uma quantidade esmagadora de recursos disponíveis para referência quando surgem problemas.
- Existe uma variedade de temas e plugins disponíveis?
  - Mesmo usando um SSG em vez de escrever HTML diretamente, criar vários modelos por conta própria é complicado, demorado e desnecessário. Há muitos temas excelentes já disponíveis online, então basta adotar um que você goste.
  - Além disso, como uso principalmente C e Python, não conheço bem Ruby (Jekyll) ou Go (Hugo), então queria aproveitar ao máximo os temas e plugins já desenvolvidos.
  - Encontrei rapidamente um tema que gostei no Jekyll, enquanto Hugo e Gatsby pareciam ter relativamente menos temas adequados para blogs pessoais. Como mencionado acima, a compatibilidade com o GitHub Pages, que muitos desenvolvedores usam para hospedar blogs pessoais, e o período de desenvolvimento parecem ter tido um grande impacto aqui também.

### 2-2. Escolha do tema
#### Minimal Mistakes (12021.01 - 12022.04)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- Tema que usei por cerca de 1 ano e 3 meses quando criei o blog pela primeira vez
- Suporte a comentários via Disqus, Discourse, utterances, etc.
- Suporte a categorização e tags
- Suporte nativo ao Google Analytics
- Possibilidade de escolher entre skins predefinidas
- Embora tenha mudado posteriormente para o tema Chirpy, que tem um design mais elegante e agradável, considerando que é um blog de engenharia, o design do Minimal Mistakes, embora não seja bonito, é bastante limpo e foi adequado para uso.

#### Chirpy Jekyll Theme (12022.04 - presente)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- Tema que estou usando desde abril de 12022, quando migrei o tema do blog
- Suporte a múltiplas categorias, funcionalidade de tags
- Suporte nativo a expressões matemáticas com sintaxe LaTeX baseado em MathJax
- Suporte nativo a diagramas baseados em Mermaid
- Suporte a comentários via Disqus, Giscus, etc.
- Suporte ao Google Analytics, GoatCounter
- Suporte a temas claro e escuro
- No momento da transição de tema, recursos como MathJax e Mermaid não eram suportados nativamente pelo tema Minimal Mistakes e precisavam ser adicionados através de personalização, enquanto o tema Chirpy os suporta nativamente. Claro, a personalização não era nada complicada, mas ainda assim é uma pequena vantagem.
- Acima de tudo, o design é bonito. O tema Minimal Mistakes é limpo, mas tem uma rigidez característica que parece mais adequada para documentação técnica oficial de projetos ou páginas de portfólio do que para blogs. O tema Chirpy tem a vantagem de um design que não fica atrás de plataformas de blogs comerciais como Tistory, Medium, velog, etc.

## 3. Criando um repositório GitHub, construindo e implantando
Descrito com base no Chirpy Jekyll Theme atualmente em uso (12024.06), assumindo que o Git já está instalado.  
Referência: [Guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/) e [Página oficial do Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalando Ruby & Jekyll
Instale Ruby e Jekyll de acordo com o [Guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/), adaptando para seu sistema operacional.

### 3-2. Criando um repositório GitHub
A [página oficial do Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) apresenta dois métodos:
1. Usar a gem "jekyll-theme-chirpy" para importar arquivos principais e obter recursos restantes do modelo [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Vantagem: Facilita a aplicação de atualizações de versão, como será explicado posteriormente.
  - Desvantagem: Personalização limitada.
2. Fazer fork do repositório [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) para seu próprio repositório de blog
  - Vantagem: Como você gerencia todos os arquivos diretamente no repositório, pode personalizar livremente modificando o código, mesmo para recursos não suportados pelo tema.
  - Desvantagem: Para aplicar atualizações de versão, você precisa mesclar a [tag upstream mais recente do repositório original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), o que pode causar conflitos com código personalizado. Nesses casos, você precisa resolver os conflitos manualmente.

Escolhi o método 1. No caso do tema Chirpy, ele já tem alta qualidade, então a maioria dos usuários não precisa de muita personalização. Além disso, como o desenvolvimento e melhorias de recursos continuam ativamente até 12024, a menos que você planeje modificações extensivas, as vantagens de acompanhar o upstream original superam as vantagens da personalização direta. O guia oficial do tema Chirpy também recomenda o método 1 para a maioria dos usuários.

### 3-3. Configurações principais
Aplique as configurações necessárias nos arquivos `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} e `_data/share.yml`{: .filepath} no diretório raiz. As configurações são bem comentadas e intuitivas, facilitando a aplicação. As configurações que podem exigir trabalho externo incluem o registro de códigos de autenticação para integração com o Google Search Console e ferramentas como Google Analytics ou GoatCounter, mas esses procedimentos não são muito complicados e não são o foco principal deste artigo, então omito descrições detalhadas.

### 3-4. Construindo localmente
Embora não seja um procedimento obrigatório, você pode querer verificar se um novo post ou modificação será exibido corretamente na web. Para isso, abra um terminal no diretório raiz do repositório local e execute o seguinte comando:
```console
$ bundle exec jekyll s
```
Após alguns segundos, o site será construído localmente e você poderá verificar o resultado em <http://127.0.0.1:4000>.

### 3-5. Implantando
Existem dois métodos:
1. Usando GitHub Actions (para hospedagem no GitHub Pages)
  - Se você estiver usando o GitHub Free Plan, o repositório deve ser público
  - Na página web do GitHub, selecione a aba *Settings* do repositório, clique em *Code and automation > Pages* na barra de navegação à esquerda e selecione a opção **GitHub Actions** na seção **Source**
  - Após a configuração, o fluxo de trabalho *Build and Deploy* será executado automaticamente sempre que um novo commit for enviado
2. Construção e implantação manual (para outros serviços de hospedagem ou auto-hospedagem)
  - Execute o comando abaixo para construir o site manualmente
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Faça upload do resultado da construção no diretório `_site` para o servidor

## 4. Escrevendo posts
O [guia de escrita de posts](https://chirpy.cotes.page/posts/write-a-new-post/) do tema Chirpy documenta bem os métodos e opções disponíveis. Além do que é descrito neste artigo, ele oferece várias funcionalidades, e é um bom material de referência quando necessário. Aqui, resumo os principais pontos a considerar ao criar cada post.

### Criando o arquivo markdown
- Formato do nome: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Localização: diretório `_posts`{: .filepath}

### Escrevendo o Front Matter
O Front Matter deve ser escrito adequadamente no início do arquivo markdown:
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: Título do post
- **description**: Resumo. Se não for fornecido, parte do conteúdo do texto será usado automaticamente, mas recomenda-se escrever a meta tag description diretamente para otimização de mecanismos de busca (SEO). Um comprimento adequado é de 135-160 caracteres para alfabeto romano, ou 80-110 caracteres para idiomas como o coreano.
- **date**: Data e hora exatas de criação do post e fuso horário (opcional; se omitido, a data de criação ou modificação do arquivo será reconhecida automaticamente)
- **categories**: Categorização do post
- **tags**: Tags a serem aplicadas ao post
- **image**: Inserção de imagem de pré-visualização no topo do post
  - **path**: Caminho do arquivo de imagem
  - **alt**: Texto alternativo (opcional)
- **toc**: Uso da funcionalidade de índice na barra lateral direita, valor padrão é `true`
- **comments**: Use para especificar explicitamente se deseja ativar comentários para posts individuais, independentemente da configuração padrão do site
- **math**: Ativa a funcionalidade de expressão matemática baseada em [MathJax](https://www.mathjax.org/), desativada por padrão (`false`) para melhor desempenho da página
- **mermaid**: Ativa a funcionalidade de diagrama baseada em [Mermaid](https://github.com/mermaid-js/mermaid), desativada por padrão (`false`)

## 5. Atualizações

Assumindo que você escolheu o método 1 em [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-criando-um-repositório-github). Se você escolheu o método 2, precisará mesclar manualmente a tag upstream mais recente, como mencionado anteriormente.

1. Edite o arquivo `Gemfile`{: .filepath} para especificar a nova versão da gem "jekyll-theme-chirpy".
2. Para atualizações de versão principal, arquivos essenciais não incluídos na gem "jekyll-theme-chirpy" e opções de configuração também podem ter mudado. Nesse caso, verifique as alterações usando a API do GitHub abaixo e aplique-as manualmente:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
