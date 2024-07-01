---
title: "Criando e Gerenciando um Blog no GitHub Pages"
description: >-
  Vamos aprender sobre as características e diferenças entre páginas web estáticas e dinâmicas, geradores de sites estáticos (Static Site Generators) e como hospedar um blog Jekyll no GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
---

Comecei a hospedar meu blog no GitHub Pages usando Jekyll no início de 2021. No entanto, como não documentei adequadamente o processo de instalação na época, tive algumas dificuldades na manutenção posterior. Então, decidi fazer um breve resumo do processo de instalação e métodos de manutenção.  
~~Na verdade, o maior problema é que ainda não estou muito familiarizado com a hospedagem de sites estáticos.~~
(Conteúdo atualizado em junho de 2024)

## 1. Gerador de Sites Estáticos & Hospedagem Web
### 1-1. Páginas Web Estáticas vs Páginas Web Dinâmicas
#### Páginas Web Estáticas (Static Web Page)
- Páginas web que entregam dados armazenados no servidor diretamente ao usuário
- O servidor web entrega a página pré-armazenada correspondente à solicitação do usuário
- Os usuários veem a mesma página web, a menos que os dados armazenados no servidor sejam alterados
- Geralmente, a resposta é rápida, pois apenas o arquivo correspondente à solicitação precisa ser enviado, sem necessidade de processamento adicional
- Como consiste apenas de arquivos simples, só é necessário configurar um servidor web, tornando o custo de implementação baixo
- O serviço é limitado, pois mostra apenas informações pré-armazenadas
- Adições, modificações e exclusões de dados devem ser feitas manualmente pelo administrador
- Estrutura mais fácil para os mecanismos de busca rastrearem, sendo relativamente mais vantajosa para otimização de mecanismos de busca (SEO)

#### Páginas Web Dinâmicas (Dynamic Web Page)
- Páginas web que processam dados armazenados no servidor com scripts antes de entregá-los
- O servidor web interpreta a solicitação do usuário, processa os dados e então entrega a página web gerada
- Os usuários veem páginas web que variam de acordo com a situação, hora, solicitação, etc.
- A resposta é relativamente mais lenta, pois os scripts precisam ser processados para entregar a página web
- Custos adicionais são incorridos na implementação, pois um servidor de aplicação é necessário além do servidor web
- Diversos serviços são possíveis, pois informações variadas podem ser combinadas e fornecidas dinamicamente
- Dependendo da estrutura da página web, os usuários podem adicionar, modificar e excluir dados diretamente no navegador

### 1-2. Gerador de Sites Estáticos (SSG, Static Site Generator)
- Uma ferramenta que gera páginas web estáticas baseadas em dados brutos (geralmente arquivos de texto em formato markdown) e templates predefinidos
- Automatiza o processo de construção e publicação de páginas web sem a necessidade de escrever páginas HTML individuais, bastando escrever os posts em markdown
- ex) Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Um serviço de hospedagem de páginas web estáticas gratuito fornecido pelo GitHub
- Cada conta pode hospedar 1 página web pessoal representativa e criar e hospedar um número ilimitado de páginas de documentação de projetos por repositório.
- Após criar um repositório com o nome no formato '{username}.github.io' correspondente ao seu nome de usuário do GitHub, você pode fazer push diretamente das páginas HTML construídas para esse repositório ou usar GitHub Actions para realizar a construção e implantação.
- Se você possui um domínio próprio, pode conectá-lo nas configurações para usar um endereço de domínio diferente em vez do domínio padrão no formato '{username}.github.io'.

## 2. Escolhendo o SSG e o Tema a Serem Usados

### Por que escolhi Jekyll
Existem vários SSGs como Jekyll, Hugo, Gatsby, etc., mas decidi usar Jekyll. Os critérios que considerei ao escolher o SSG e as razões para escolher Jekyll são os seguintes:
- É possível minimizar tentativas e erros desnecessários e focar na escrita e operação do blog?
  - Jekyll é o gerador de sites estáticos oficialmente suportado pelo Github Pages. Claro, outros SSGs como Hugo, Gatsby, etc. também podem ser hospedados no Github Pages, e há a opção de usar outros serviços de hospedagem como Netlify, mas na verdade, para operar um blog pessoal deste tamanho, não é tão importante tecnicamente qual SSG foi usado para construí-lo, nem a velocidade de construção ou desempenho, então julguei que seria melhor usar algo que fosse um pouco mais simples de manter e tivesse mais documentação de referência.
  - Jekyll também tem o período de desenvolvimento mais longo em comparação com seus concorrentes como Hugo e Gatsby. Isso significa que está bem documentado e há uma quantidade esmagadora de recursos de referência disponíveis quando surgem problemas.
- Há uma variedade de temas e plugins disponíveis?
  - Mesmo que você não esteja escrevendo HTML diretamente, mas usando um SSG, criar vários templates por conta própria é trabalhoso, demorado e nem é necessário. Há muitos temas excelentes já disponíveis na web, então basta adotar um que você goste e usá-lo.
  - Além disso, como eu originalmente uso principalmente C e Python, não conheço bem Ruby do Jekyll ou Go do Hugo, então queria usar ativamente temas e plugins já desenvolvidos.
  - Com Jekyll, pude encontrar rapidamente um tema que gostei à primeira vista, enquanto Hugo e Gatsby pareciam não ter tantos temas adequados para blogs pessoais em comparação. Parece que a compatibilidade com o Github Pages, que muitos desenvolvedores usam para hospedar blogs pessoais, e o período de desenvolvimento mencionado acima também tiveram um grande impacto aqui.

### Escolha do Tema
#### Minimal Mistakes (Jan 2021 ~ Abr 2022)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Página de Demonstração: <https://mmistakes.github.io/minimal-mistakes/>
- Tema que usei por cerca de 1 ano e 3 meses quando criei o blog pela primeira vez
- Suporte a funcionalidade de comentários através de Disqus, Discourse, utterances, etc.
- Suporte a funcionalidade de classificação por categorias e tags
- Suporte nativo ao Google Analytics
- Possibilidade de escolher skins predefinidas
- Embora eu tenha mudado posteriormente para o tema Chirpy, que tem um design mais elegante e agradável, considerando que é um blog de engenharia de qualquer maneira, acho que foi bastante utilizável com seu design limpo, mesmo que não fosse bonito.

### Tema Chirpy Jekyll (Abr 2022~)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Página de Demonstração: <https://chirpy.cotes.page/>
- Tema que estou usando desde que mudei o tema do blog em abril de 2022
- Suporte a classificação por múltiplas categorias e funcionalidade de tags
- Suporte nativo a expressões matemáticas em sintaxe LaTeX baseado em MathJax
- Suporte nativo a funcionalidade de diagramas baseado em Mermaid
- Suporte a funcionalidade de comentários através de Disqus, Giscus, etc.
- Suporte ao Google Analytics, GoatCounter
- Suporte a temas claro e escuro
- No momento da mudança de tema, recursos como MathJax ou Mermaid não eram suportados nativamente no tema Minimal Mistakes e precisavam ser adicionados através de customização manual, mas o tema Chirpy os suporta nativamente. Claro, a customização não era grande coisa, mas ainda assim é uma pequena vantagem.
- Acima de tudo, o design é bonito. Enquanto o tema Minimal Mistakes é limpo, tem uma rigidez característica que parece mais adequada para documentação técnica oficial de projetos ou páginas de portfólio do que para blogs, o tema Chirpy tem a vantagem de um design que não fica atrás de plataformas de blog comerciais como Tistory, Medium, velog, etc.

## 3. Criando o Repositório GitHub, Construindo e Implantando
Isso é baseado no Tema Chirpy Jekyll que estou usando atualmente (junho de 2024), e assume que o Git já está instalado.  
Referência ao [Guia de Instalação Oficial do Jekyll](https://jekyllrb.com/docs/installation/) e à [Página Oficial do Tema Chirpy Jekyll](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalando Ruby & Jekyll
Instale Ruby e Jekyll de acordo com o seu ambiente de sistema operacional, seguindo o [Guia de Instalação Oficial do Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Criando o Repositório GitHub
A [página oficial do Tema Chirpy Jekyll](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) apresenta dois métodos:
1. Método de importar os arquivos principais com a gem "jekyll-theme-chirpy" e obter os recursos restantes do template [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Vantagem: Facilita a aplicação de atualizações de versão, como será mencionado posteriormente.
  - Desvantagem: A customização é limitada.
2. Método de fazer fork do repositório [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) para o repositório do seu próprio blog
  - Vantagem: Como você gerencia diretamente todos os arquivos dentro do repositório, pode customizar livremente modificando o código, mesmo para funcionalidades não suportadas pelo tema.
  - Desvantagem: Para aplicar atualizações de versão, você precisa fazer merge da [tag upstream mais recente do repositório original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), o que pode resultar em conflitos com o código que você customizou diretamente. Nesse caso, você precisa resolver esses conflitos manualmente.

Eu escolhi o método 1. No caso do tema Chirpy, ele já tem um alto nível de completude, então para a maioria dos usuários não há muito a customizar, e como o desenvolvimento e melhoria de funcionalidades continuam bastante ativos até 2024, a menos que você planeje fazer modificações extensivas, as vantagens de seguir o upstream original em tempo hábil superam as vantagens de aplicar customizações diretas. O guia oficial do tema Chirpy também recomenda o método 1 para a maioria dos usuários.

### 3-3. Configurações Principais
Aplique as configurações necessárias nos arquivos `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} e `_data/share.yml`{: .filepath} no diretório raiz. Os comentários são bem escritos e as configurações são intuitivas, então você pode aplicá-las sem muita dificuldade. As únicas configurações que podem requerer trabalho externo separado são o registro do código de autenticação para integração com o Google Search Console e a integração de ferramentas de webmaster como Google Analytics ou GoatCounter, mas mesmo isso não é um procedimento muito complicado e não é o tema principal que pretendo abordar neste post, então omito uma descrição detalhada.

### 3-4. Construindo Localmente
Embora não seja um procedimento obrigatório, você pode querer verificar antecipadamente se algo que você escreveu ou modificou no site será exibido corretamente na web. Nesse caso, você pode abrir um terminal no diretório raiz do repositório local e executar o seguinte comando:
```console
$ bundle exec jekyll s
```
Após alguns segundos, o site será construído localmente e você poderá verificar o resultado no endereço <http://127.0.0.1:4000>.

### 3-5. Implantando
Existem dois métodos:
1. Usando GitHub Actions (ao hospedar no GitHub Pages)
  - Se você estiver usando o GitHub Free Plan, precisa manter o repositório público
  - Na página web do GitHub, selecione a aba *Settings* do repositório, clique em *Code and automation > Pages* na barra de navegação à esquerda e selecione a opção **GitHub Actions** na seção **Source**
  - Após a configuração, o fluxo de trabalho *Build and Deploy* será executado automaticamente sempre que você fizer push de um novo commit
2. Construindo e implantando diretamente (ao usar outro serviço de hospedagem ou auto-hospedagem)
  - Execute o seguinte comando para construir o site diretamente
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Faça upload do resultado da construção no diretório `_site` para o servidor

## 4. Escrevendo Posts
O [guia de escrita de posts](https://chirpy.cotes.page/posts/write-a-new-post/) do tema Chirpy documenta bem o método de escrita de posts e as opções disponíveis. Ele fornece várias funcionalidades além do que é descrito neste post, e contém informações úteis para referência, então consulte a documentação oficial se necessário. Aqui, resumiremos os principais pontos a serem lembrados toda vez que você fizer um post.

### Criando o Arquivo Markdown
- Formato do nome: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Localização: diretório `_posts`{: .filepath}

### Escrevendo o Front Matter
Você deve escrever adequadamente o Front Matter na primeira parte do arquivo markdown.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]     # TAG names should always be lowercase
---
```
- **title**: Título do post
- **description**: Resumo. Se não for escrito, uma parte do início do conteúdo principal será usada automaticamente, mas é recomendado escrever diretamente a meta tag de descrição para otimização de mecanismos de busca (SEO). Um comprimento de cerca de 135~160 caracteres para o alfabeto romano ou 80~110 caracteres para o coreano é apropriado.
- **date**: Data e hora exatas de escrita do post e fuso horário (opcional, se omitido, as informações de data de escrita no título do arquivo serão reconhecidas e usadas automaticamente)
- **categories**: Classificação de categoria do post
- **tags**: Classificação de tags a serem aplicadas ao post

## 5. Atualizando

Isso é descrito assumindo que você escolheu o método 1 em [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#