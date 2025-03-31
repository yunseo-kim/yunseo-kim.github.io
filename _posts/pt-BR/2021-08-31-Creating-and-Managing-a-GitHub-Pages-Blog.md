---
title: Criando e gerenciando um blog no GitHub Pages
description: Vamos aprender sobre as características e diferenças entre páginas web estáticas e dinâmicas, geradores de sites estáticos (Static Site Generator) e hospedar um blog Jekyll no GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---
Comecei a hospedar um blog no GitHub Pages usando Jekyll no início do ano 12021 da [Era Humana](https://en.wikipedia.org/wiki/Holocene_calendar). No entanto, como não documentei adequadamente o processo de instalação na época da criação do blog, tive algumas dificuldades na manutenção posterior. Então, decidi fazer um breve resumo do processo de instalação e dos métodos de manutenção.

(+ Atualizado em 12024.12)

## 1. Gerador de sites estáticos & hospedagem web
### 1-1. Página web estática vs página web dinâmica
#### Página web estática (Static Web Page)
- Uma página web que entrega dados armazenados no servidor diretamente ao usuário
- O servidor web entrega uma página pré-armazenada correspondente à solicitação do usuário
- O usuário vê a mesma página web, a menos que os dados armazenados no servidor sejam alterados
- Geralmente, a resposta é rápida, pois apenas o arquivo correspondente à solicitação precisa ser enviado, sem necessidade de processamento adicional
- Como consiste apenas de arquivos simples, só é necessário configurar um servidor web, tornando o custo de implementação baixo
- O serviço é limitado, pois mostra apenas informações pré-armazenadas
- Adições, modificações e exclusões de dados devem ser feitas manualmente pelo administrador
- Estrutura mais fácil para os mecanismos de busca rastrearem, sendo relativamente mais vantajosa para otimização de mecanismos de busca (SEO)

#### Página web dinâmica (Dynamic Web Page)
- Uma página web que processa dados armazenados no servidor com scripts antes de entregá-los
- O servidor web interpreta a solicitação do usuário, processa os dados e então entrega a página web gerada
- O usuário vê páginas web que variam de acordo com a situação, hora, solicitação, etc.
- A resposta é relativamente mais lenta, pois os scripts precisam ser processados antes da entrega da página web
- Custos adicionais são incorridos na implementação, pois um servidor de aplicação é necessário além do servidor web
- Diversos serviços são possíveis, pois informações variadas podem ser combinadas e fornecidas dinamicamente
- Dependendo da estrutura da página web, os usuários podem adicionar, modificar e excluir dados diretamente no navegador
 
### 1-2. Gerador de sites estáticos (SSG, Static Site Generator)
- Uma ferramenta que gera páginas web estáticas baseadas em dados brutos (geralmente arquivos de texto em formato markdown) e templates predefinidos
- Automatiza o processo de construção e publicação de páginas web sem a necessidade de escrever páginas HTML individuais, bastando escrever posts em markdown
- Ex: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Um serviço de hospedagem de páginas web estáticas gratuito fornecido pelo GitHub
- Permite hospedar uma página web pessoal principal por conta e um número ilimitado de páginas de documentação de projetos por repositório
- Após criar um repositório com o nome no formato '{username}.github.io' correspondente ao seu nome de usuário do GitHub, você pode fazer push diretamente das páginas HTML construídas para o repositório ou usar o GitHub Actions para realizar a construção e implantação
- Se você possui um domínio próprio, pode conectá-lo nas configurações para usar um endereço de domínio diferente do formato padrão '{username}.github.io'

## 2. Escolhendo o SSG e o tema a serem usados

### 2-1. Razões para escolher o Jekyll
Existem vários SSGs como Jekyll, Hugo, Gatsby, etc., mas decidi usar o Jekyll. Os critérios considerados ao escolher o SSG e as razões para escolher o Jekyll são os seguintes:
- É possível minimizar tentativas e erros desnecessários e focar na escrita e operação do blog?
  - Jekyll é o gerador de sites estáticos oficialmente suportado pelo GitHub Pages. Embora outros SSGs como Hugo e Gatsby também possam ser hospedados no GitHub Pages sem problemas, e haja a opção de usar outros serviços de hospedagem como Netlify, na verdade, para operar um blog pessoal deste tamanho, não é tão importante tecnicamente qual SSG foi usado para construí-lo, nem a velocidade de construção ou desempenho. Portanto, decidi que seria melhor usar algo que fosse um pouco mais simples de manter e tivesse mais documentação de referência.
  - Além disso, Jekyll tem o período de desenvolvimento mais longo em comparação com seus concorrentes como Hugo e Gatsby. Isso significa que sua documentação é bem feita e há uma quantidade esmagadora de recursos de referência disponíveis quando surgem problemas.
- Há uma variedade de temas e plugins disponíveis?
  - Mesmo usando um SSG em vez de escrever HTML diretamente, criar vários templates por conta própria é trabalhoso, demorado e desnecessário. Há muitos temas excelentes já disponíveis na web, então basta adotar um que você goste e usá-lo.
  - Além disso, como eu originalmente uso principalmente C e Python, não conheço bem Ruby do Jekyll ou Go do Hugo, então queria usar ativamente temas e plugins já desenvolvidos.
  - Com Jekyll, pude encontrar rapidamente um tema que gostei à primeira vista, enquanto Hugo e Gatsby pareciam não ter tantos temas adequados para blogs pessoais em comparação. Isso provavelmente se deve à compatibilidade com o GitHub Pages, que muitos desenvolvedores usam para hospedar blogs pessoais, e ao período de desenvolvimento, como mencionado anteriormente.

### 2-2. Escolha do tema
#### Minimal Mistakes (12021.01 - 12022.04)
- Repositório GitHub: <https://github.com/mmistakes/minimal-mistakes>
- Página de demonstração: <https://mmistakes.github.io/minimal-mistakes/>
- Tema que usei por cerca de 1 ano e 3 meses quando criei o blog pela primeira vez
- Suporte a funcionalidade de comentários através de Disqus, Discourse, utterances, etc.
- Suporte a funcionalidade de classificação por categorias e tags
- Suporte nativo ao Google Analytics
- Possibilidade de escolher entre skins predefinidas
- Embora eu tenha mudado posteriormente para o tema Chirpy, que achei ter um design mais elegante e agradável, o Minimal Mistakes tinha um design razoavelmente limpo, mesmo que não fosse bonito, considerando que é um blog de engenharia.

#### Chirpy Jekyll Theme (12022.04 - presente)
- Repositório GitHub: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Página de demonstração: <https://chirpy.cotes.page/>
- Tema que estou usando desde que mudei o tema do blog em abril de 12022
- Suporte a classificação por múltiplas categorias e funcionalidade de tags
- Suporte nativo a expressões matemáticas usando sintaxe LaTeX baseada em MathJax
- Suporte nativo a funcionalidade de diagramas baseada em Mermaid
- Suporte a funcionalidade de comentários através de Disqus, Giscus, etc.
- Suporte ao Google Analytics, GoatCounter
- Suporte a temas claro e escuro
- No momento da mudança de tema, recursos como MathJax e Mermaid não eram suportados nativamente no tema Minimal Mistakes e precisavam ser adicionados através de customização, mas o tema Chirpy os suporta nativamente. Embora a customização não fosse muito complicada, ainda assim é uma pequena vantagem.
- Acima de tudo, o design é bonito. Enquanto o tema Minimal Mistakes é limpo, tem uma certa rigidez que parece mais adequada para documentação técnica oficial de projetos ou páginas de portfólio do que para blogs. O tema Chirpy tem a vantagem de um design que não fica atrás de plataformas de blog comerciais como Tistory, Medium ou velog.

## 3. Criando o repositório GitHub, construindo e implantando
Descreverei com base no Chirpy Jekyll Theme que estou usando atualmente (12024.06), assumindo que o Git já está instalado.  
Referência: [Guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/) e [Página oficial do Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalando Ruby & Jekyll
Instale Ruby e Jekyll de acordo com o [Guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/), adequado ao seu ambiente de sistema operacional.

### 3-2. Criando o repositório GitHub
A [página oficial do Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) apresenta dois métodos:
1. Método de importar os arquivos principais usando a gem "jekyll-theme-chirpy" e obter os recursos restantes do template [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Vantagem: Facilita a aplicação de atualizações de versão, como será explicado posteriormente.
  - Desvantagem: A customização é limitada.
2. Método de fazer fork do repositório [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) para o repositório do seu blog
  - Vantagem: Como você gerencia diretamente todos os arquivos dentro do repositório, pode customizar livremente modificando o código, mesmo para funcionalidades não suportadas pelo tema.
  - Desvantagem: Para aplicar atualizações de versão, é necessário fazer merge da [tag upstream mais recente do repositório original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), o que pode resultar em conflitos com o código customizado, que precisarão ser resolvidos manualmente.

Eu escolhi o método 1. No caso do tema Chirpy, ele já tem um alto nível de completude, então a maioria dos usuários não tem muito a customizar. Além disso, como o desenvolvimento e melhoria de funcionalidades continuam ativamente até 12024, a menos que você planeje fazer modificações extensas, as vantagens de acompanhar o upstream original superam as vantagens de aplicar customizações diretas. O guia oficial do tema Chirpy também recomenda o método 1 para a maioria dos usuários.

### 3-3. Configurações principais
Aplique as configurações necessárias nos arquivos `_config.yml`{: .filepath} no diretório raiz e `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. As configurações são bem comentadas e intuitivas, então podem ser aplicadas sem muita dificuldade. As configurações que podem requerer trabalho externo incluem o registro do código de autenticação para integração com o Google Search Console e a integração de ferramentas de webmaster como Google Analytics ou GoatCounter, mas esses procedimentos não são muito complicados e não são o foco principal deste post, então omitiremos detalhes.

### 3-4. Construindo localmente
Embora não seja um procedimento obrigatório, você pode querer verificar se um novo post ou modificações no site serão exibidos corretamente na web antes de publicar. Nesse caso, abra um terminal no diretório raiz do repositório local e execute o seguinte comando:
```console
$ bundle exec jekyll s
```
Após alguns segundos, o site será construído localmente e você poderá verificar o resultado no endereço <http://127.0.0.1:4000>.

### 3-5. Implantando
Existem dois métodos:
1. Usando GitHub Actions (ao hospedar no GitHub Pages)
  - Se você estiver usando o plano gratuito do GitHub, o repositório deve ser mantido público
  - Na página web do GitHub, selecione a aba *Settings* do repositório, clique em *Code and automation > Pages* na barra de navegação à esquerda e selecione a opção **GitHub Actions** na seção **Source**
  - Após a configuração, o fluxo de trabalho *Build and Deploy* será executado automaticamente sempre que um novo commit for feito push
2. Construindo e implantando manualmente (ao usar outro serviço de hospedagem ou auto-hospedagem)
  - Execute o comando abaixo para construir o site manualmente
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Faça upload do resultado da construção no diretório `_site` para o servidor

## 4. Escrevendo posts
O [guia de escrita de posts](https://chirpy.cotes.page/posts/write-a-new-post/) do tema Chirpy documenta bem o método de escrita de posts e as opções disponíveis. Ele fornece várias funcionalidades além das descritas neste post, e contém informações úteis para referência. Aqui, resumiremos os principais pontos a serem lembrados ao fazer posts regularmente.

### Criando o arquivo markdown
- Formato do nome: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Localização: diretório `_posts`{: .filepath}

### Escrevendo o Front Matter
O Front Matter deve ser escrito adequadamente no início do arquivo markdown.
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
- **description**: Resumo. Se não for escrito, uma parte do início do conteúdo principal será usada automaticamente, mas recomenda-se escrever a meta tag de descrição diretamente para otimização de mecanismos de busca (SEO). Um comprimento de 135~160 caracteres em alfabeto romano ou 80~110 caracteres em coreano é apropriado.
- **date**: Data e hora exatas de escrita do post e fuso horário (opcional, se omitido, a data de criação ou modificação do arquivo será reconhecida e usada automaticamente)
- **categories**: Classificação de categoria do post
- **tags**: Classificação de tags a serem aplicadas ao post
- **image**: Inserção de imagem de pré-visualização no topo do post
  - **path**: Caminho do arquivo de imagem
  - **alt**: Texto alternativo (opcional)
- **toc**: Uso da funcionalidade de índice na barra lateral direita, o valor padrão é `true`
- **comments**: Usado para especificar explicitamente o uso de comentários para posts individuais, independentemente da configuração padrão do site
- **math**: Ativa a funcionalidade de expressão matemática baseada em [MathJax](https://www.mathjax.org/) embutido, o valor padrão é desativado (`false`) para desempenho da página
- **mermaid**: Ativa a funcionalidade de expressão de diagramas baseada em [Mermaid](https://github.com/mermaid-js/mermaid) embutido, o valor padrão é desativado (`false`)

## 5. Atualização

Assumindo que o método 1 foi escolhido em [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-criando-o-repositório-github). Se o método 2 foi escolhido, como mencionado anteriormente, você precisará fazer merge da tag upstream mais recente manualmente.

1. Edite o `Gemfile`{: .filepath} para especificar a nova versão da gem "jekyll-theme-chirpy".
2. No caso de atualizações maiores, arquivos principais não incluídos na gem "jekyll-theme-chirpy" e opções de configuração também podem ter sido alterados. Nesse caso, você precisa verificar as alterações usando a API do GitHub abaixo e aplicá-las manualmente:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
