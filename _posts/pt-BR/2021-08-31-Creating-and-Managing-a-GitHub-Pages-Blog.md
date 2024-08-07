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
#### Páginas Web Estáticas
- Páginas web que entregam dados armazenados no servidor diretamente ao usuário
- O servidor web entrega a página pré-armazenada correspondente à solicitação do usuário
- Os usuários veem a mesma página web, a menos que os dados armazenados no servidor sejam alterados
- Geralmente, a resposta é rápida, pois apenas o arquivo correspondente à solicitação precisa ser enviado, sem necessidade de processamento adicional
- Como consiste apenas de arquivos simples, só é necessário configurar um servidor web, tornando o custo de implementação baixo
- O serviço é limitado, pois mostra apenas informações pré-armazenadas
- Adições, modificações e exclusões de dados devem ser feitas manualmente pelo administrador
- Estrutura mais fácil para os mecanismos de busca rastrearem, sendo relativamente mais vantajosa para otimização de mecanismos de busca (SEO)

#### Páginas Web Dinâmicas
- Páginas web que processam dados armazenados no servidor com scripts antes de entregá-los
- O servidor web interpreta a solicitação do usuário, processa os dados e então entrega a página web gerada
- Os usuários veem páginas web que variam de acordo com a situação, hora, solicitação, etc.
- A resposta é relativamente mais lenta, pois os scripts precisam ser processados para entregar a página web
- Custos adicionais são incorridos na implementação, pois um servidor de aplicação é necessário além do servidor web
- Diversos serviços são possíveis, pois informações variadas podem ser combinadas e fornecidas dinamicamente
- Dependendo da estrutura da página web, os usuários podem adicionar, modificar e excluir dados diretamente no navegador

### 1-2. Gerador de Sites Estáticos (SSG, Static Site Generator)
- Uma ferramenta que gera páginas web estáticas baseadas em dados brutos (geralmente arquivos de texto em formato markdown) e templates predefinidos
- Automatiza o processo de construção e implantação de páginas web, eliminando a necessidade de escrever páginas HTML individuais manualmente, bastando escrever os posts em markdown
- ex) Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Um serviço de hospedagem de páginas web estáticas gratuito fornecido pelo GitHub
- Cada conta pode hospedar 1 página web pessoal representativa e um número ilimitado de páginas de documentação de projetos por repositório
- Após criar um repositório com o nome no formato '{username}.github.io' correspondente ao seu nome de usuário do GitHub, você pode fazer push diretamente das páginas HTML construídas para esse repositório ou usar GitHub Actions para realizar a construção e implantação
- Se você possui um domínio próprio, pode conectá-lo nas configurações para usar um endereço de domínio diferente em vez do domínio padrão no formato '{username}.github.io'

## 2. Escolhendo o SSG e o Tema a Serem Usados

### 2-1. Por que escolhi Jekyll
Existem vários SSGs como Jekyll, Hugo, Gatsby, etc., mas decidi usar Jekyll. Os critérios que considerei ao escolher o SSG e as razões para escolher Jekyll são os seguintes:
- É possível minimizar tentativas e erros desnecessários e focar na escrita e operação do blog?
  - Jekyll é o gerador de sites estáticos oficialmente suportado pelo GitHub Pages. Claro, outros SSGs como Hugo e Gatsby também podem ser hospedados no GitHub Pages, e há a opção de usar serviços de hospedagem completamente diferentes como Netlify, mas na verdade, para operar um blog pessoal deste tamanho, não é tão importante qual SSG foi usado tecnicamente para construí-lo, nem a velocidade de construção ou desempenho. Então, julguei que seria melhor usar algo que fosse um pouco mais simples de manter e tivesse mais documentação de referência.
  - Jekyll também tem o período de desenvolvimento mais longo em comparação com seus concorrentes como Hugo e Gatsby. Isso significa que está bem documentado e há uma quantidade esmagadora de recursos de referência disponíveis quando surgem problemas.
- Há uma variedade de temas e plugins disponíveis?
  - Mesmo que você não esteja escrevendo HTML diretamente, mas usando um SSG, criar vários templates por conta própria é trabalhoso, demorado e nem é necessário. Há muitos temas excelentes já disponíveis na web, então você pode simplesmente adotar e usar um que goste.
  - Além disso, como eu originalmente uso principalmente C e Python, não conheço bem Ruby do Jekyll ou Go do Hugo, então queria usar ativamente temas e plugins existentes.
  - Com Jekyll, pude encontrar rapidamente um tema que gostei à primeira vista, enquanto Hugo e Gatsby pareciam ter relativamente menos temas adequados para blogs pessoais. Parece que a conectividade com o GitHub Pages, que muitos desenvolvedores usam para hospedar blogs pessoais, e o período de desenvolvimento mencionado acima também tiveram um grande impacto aqui.

### 2-2. Escolha do Tema
#### Minimal Mistakes (Janeiro de 2021 ~ Abril de 2022)
- Repositório GitHub: <https://github.com/mmistakes/minimal-mistakes>
- Página de Demonstração: <https://mmistakes.github.io/minimal-mistakes/>
- Tema que usei por cerca de 1 ano e 3 meses quando criei o blog pela primeira vez
- Suporte a funcionalidade de comentários através de Disqus, Discourse, utterances, etc.
- Suporte a funcionalidade de classificação por categorias e tags
- Suporte nativo ao Google Analytics
- Possibilidade de escolher entre skins predefinidas
- Embora eu tenha mudado posteriormente para o tema Chirpy, que tem um design mais elegante e agradável, considerando que é um blog de engenharia de qualquer maneira, o design do Minimal Mistakes, embora não seja bonito, é bastante limpo e foi adequado para uso.

#### Tema Jekyll Chirpy (Abril de 2022~)
- Repositório GitHub: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Página de Demonstração: <https://chirpy.cotes.page/>
- Tema que estou usando desde que mudei o tema do blog em abril de 2022
- Suporte a classificação por múltiplas categorias e funcionalidade de tags
- Suporte nativo a expressões matemáticas com sintaxe LaTeX baseada em MathJax
- Suporte nativo a funcionalidade de diagramas baseada em Mermaid
- Suporte a funcionalidade de comentários através de Disqus, Giscus, etc.
- Suporte ao Google Analytics, GoatCounter
- Suporte a temas claro e escuro
- No momento da mudança de tema, recursos como MathJax ou Mermaid não eram suportados nativamente no tema Minimal Mistakes e precisavam ser adicionados através de customização manual, mas o tema Chirpy os suporta nativamente. Claro, a customização não era grande coisa, mas ainda assim é uma pequena vantagem.
- Acima de tudo, o design é bonito. Enquanto o tema Minimal Mistakes é limpo, tem uma rigidez característica que parece mais adequada para documentação técnica oficial de projetos ou páginas de portfólio do que para blogs, o tema Chirpy tem a vantagem de um design que não fica atrás de plataformas de blog comerciais como Tistory, Medium ou velog.

## 3. Criando o Repositório GitHub, Construindo e Implantando
Descreverei com base no Tema Jekyll Chirpy que estou usando atualmente (junho de 2024), assumindo que o Git já está instalado.  
Referência: [Guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/) e [Página oficial do Tema Jekyll Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalando Ruby & Jekyll
Instale Ruby e Jekyll de acordo com o [Guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/), adequado ao seu ambiente de sistema operacional.

### 3-2. Criando o Repositório GitHub
A [página oficial do Tema Jekyll Chirpy](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) apresenta dois métodos:
1. Método de importar os arquivos principais com a gem "jekyll-theme-chirpy" e obter os recursos restantes do template [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Vantagem: Facilita a aplicação de atualizações de versão, como será mencionado posteriormente.
  - Desvantagem: A customização é limitada.
2. Método de fazer fork do repositório [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) para o repositório do seu blog
  - Vantagem: Como você gerencia diretamente todos os arquivos dentro do repositório, pode customizar livremente modificando o código, mesmo para funcionalidades não suportadas pelo tema.
  - Desvantagem: Para aplicar atualizações de versão, você precisa fazer merge da [tag upstream mais recente do repositório original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), o que pode resultar em conflitos com o código que você customizou diretamente. Nesse caso, você precisa resolver esses conflitos manualmente.

Eu adotei o método 1. No caso do tema Chirpy, ele já tem um alto nível de completude, então para a maioria dos usuários não há muito a customizar. Além disso, até 2024, o desenvolvimento e melhoria de funcionalidades continuam muito ativos, então, a menos que você planeje fazer modificações extensivas, as vantagens de seguir o upstream original superam as vantagens de aplicar customizações diretas. O guia oficial do tema Chirpy também recomenda o método 1 para a maioria dos usuários.

### 3-3. Configurações Principais
Aplique as configurações necessárias nos arquivos `_config.yml`{: .filepath} no diretório raiz e `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. Os comentários são bem escritos e as configurações são intuitivas, então você pode aplicá-las sem muita dificuldade. As únicas configurações que podem requerer trabalho externo separado são o registro do código de autenticação para integração com o Google Search Console e a integração de ferramentas de webmaster como Google Analytics ou GoatCounter, mas mesmo esses processos não são muito complicados e não são o foco principal deste post, então omito descrições detalhadas.

### 3-4. Construindo Localmente
Embora não seja um procedimento obrigatório, você pode querer verificar antecipadamente se algo que escreveu ou modificou no site será exibido corretamente na web. Nesse caso, abra um terminal no diretório raiz do repositório local e execute o seguinte comando:
```console
$ bundle exec jekyll s
```
Após alguns segundos, o site será construído localmente e você poderá verificar o resultado no endereço <http://127.0.0.1:4000>.

### 3-5. Implantando
Existem dois métodos:
1. Usando GitHub Actions (ao hospedar no GitHub Pages)
  - Se você estiver usando o GitHub Free Plan, precisa manter o repositório público
  - Na página web do GitHub, selecione a aba *Settings* do repositório, clique em *Code and automation > Pages* na barra de navegação à esquerda e selecione a opção **GitHub Actions** na seção **Source**
  - Após a configuração, o fluxo de trabalho *Build and Deploy* será executado automaticamente sempre que um novo commit for feito push
2. Construindo e implantando diretamente (ao usar outro serviço de hospedagem ou auto-hospedagem)
  - Execute o comando abaixo para construir o site diretamente
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
Na primeira parte do arquivo markdown, você deve escrever o Front Matter apropriadamente.
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
- **description**: Resumo. Se não for escrito, uma parte do início do conteúdo principal será usada automaticamente, mas para otimização de mecanismos de busca (SEO), recomenda-se escrever diretamente a meta tag de descrição apropriadamente. Um volume de cerca de 135~160 caracteres em alfabeto romano ou 80~110 caracteres em coreano é apropriado.
- **date**: Data e hora exatas de escrita do post e fuso horário (opcional, se omitido, as informações de data e hora de escrita no título do arquivo serão reconhecidas e usadas automaticamente)
- **categories**: Classificação de categoria do post
- **tags**: Classificação de tags a serem aplicadas ao post

## 5. Atualizando

Assumindo que você adotou o método 1 em [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-criando-o-repositório-github).