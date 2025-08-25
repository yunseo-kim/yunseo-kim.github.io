---
title: Criando e gerenciando um blog no GitHub Pages
description: Conheça diferenças entre páginas estáticas e dinâmicas, o que é um Static Site Generator, e hospede um blog Jekyll no GitHub Pages passo a passo.
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

Desde o início de 12021, passei a hospedar meu blog no GitHub Pages usando Jekyll. Como não documentei direito o processo de instalação na época da criação, tive algumas dificuldades na manutenção; então resolvi registrar, de forma breve, o processo de instalação e as práticas de manutenção.  

(+ Atualização de conteúdo em 12024.12)

## 1. Gerador de site estático e hospedagem na Web
### 1-1. Página da Web estática vs página da Web dinâmica
#### Página da Web estática
- Página que entrega ao usuário exatamente os dados armazenados no servidor
- O servidor envia uma página previamente armazenada correspondente à requisição
- O usuário vê a mesma página enquanto os dados no servidor não mudarem
- Como basta enviar o arquivo solicitado, não há processamento extra; em geral a resposta é mais rápida
- Por ser composta apenas de arquivos simples, basta montar um servidor web; o custo de implantação é baixo
- Como exibe apenas informações armazenadas, o serviço é limitado
- Inclusões, alterações e exclusões de dados são feitas manualmente pelo administrador
- Estrutura fácil de rastrear pelos mecanismos de busca; relativamente mais favorável a SEO

#### Página da Web dinâmica
- Página que processa dados armazenados no servidor via scripts antes de entregá-los
- O servidor interpreta a solicitação do usuário, processa os dados e envia a página gerada
- O usuário vê páginas que variam conforme contexto, horário e tipo de solicitação
- Como há processamento de scripts, a resposta tende a ser mais lenta
- Além do servidor web, é necessário um servidor de aplicação; há custo extra de implantação
- Por combinar e fornecer informações de forma dinâmica, permite serviços variados
- Dependendo da estrutura da página, o usuário pode adicionar, editar e excluir dados no próprio navegador

### 1-2. Gerador de site estático (SSG, Static Site Generator)
- Ferramenta que gera páginas estáticas a partir de dados brutos (geralmente arquivos de texto em Markdown) e templates predefinidos
- Em vez de escrever cada página HTML manualmente, você escreve posts em Markdown e o processo de build e distribuição é automatizado
- Ex.: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Serviço gratuito do GitHub para hospedar páginas estáticas
- Por conta, é possível hospedar 1 página pessoal principal e, sem limite, páginas de documentação por repositório de projetos
- Crie um repositório com o nome no formato '{username}.github.io' correspondente ao seu usuário do GitHub e envie as páginas HTML já buildadas, ou use GitHub Actions para construir e implantar automaticamente
- Se você possui um domínio próprio, pode configurá-lo para usar no lugar do domínio padrão '{username}.github.io'

## 2. Escolha do SSG e do tema

### 2-1. Por que escolhi o Jekyll
Há vários SSGs como Jekyll, Hugo e Gatsby, mas decidi usar o Jekyll. Os critérios considerados e os motivos foram:
- É possível minimizar tentativas e erros desnecessários e focar na escrita e na operação do blog?
  - O Jekyll é oficialmente suportado pelo GitHub Pages. Claro que Hugo, Gatsby etc. também funcionam no GitHub Pages e há alternativas como Netlify, mas para um blog pessoal deste porte, a escolha do SSG, velocidade de build e desempenho não são cruciais; preferi algo com manutenção simples e abundância de documentação.
  - O Jekyll também está em desenvolvimento há mais tempo que concorrentes como Hugo e Gatsby. Isso se traduz em documentação mais madura e um volume muito maior de material de referência para solucionar problemas reais.
- Há variedade de temas e plugins disponíveis?
  - Mesmo usando um SSG, criar todos os templates do zero é trabalhoso e desnecessário. Há muitos temas excelentes já públicos; basta adotar um que agrade e aproveitar.
  - Como venho de C e Python, e não domino Ruby (Jekyll) nem Go (Hugo), quis aproveitar ao máximo temas e plugins prontos.
  - No Jekyll encontrei rapidamente temas que me agradaram; no Hugo e no Gatsby, a oferta de temas adequados para blogs pessoais me pareceu menor. A integração com o GitHub Pages, muito usado por devs para blogs pessoais, e o tempo de maturação também devem influenciar.

### 2-2. Escolha do tema
#### Minimal Mistakes (12021.01 - 12022.04)
- Repositório no GitHub: <https://github.com/mmistakes/minimal-mistakes>
- Página de demonstração: <https://mmistakes.github.io/minimal-mistakes/>
- Tema usado no primeiro ano e três meses do blog
- Suporte a comentários via Disqus, Discourse, utterances etc.
- Suporte a categorias e tags
- Suporte nativo ao Google Analytics
- Skins predefinidos selecionáveis
- Depois migrei para o Chirpy, cujo design me agradou mais; ainda assim, considerando a proposta “engenheirística” do blog, embora não seja o mais bonito, tem um design limpo e utilizável sem sustos.

#### Chirpy Jekyll Theme (12022.04 - presente)
- Repositório no GitHub: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Página de demonstração: <https://chirpy.cotes.page/>
- Tema em uso desde a migração em 12022.04
- Suporte a múltiplas categorias e a tags
- Suporte nativo a fórmulas com sintaxe LaTeX via MathJax
- Suporte nativo a diagramas via Mermaid
- Suporte a comentários via Disqus, Giscus etc.
- Suporte a Google Analytics e GoatCounter
- Suporte a tema claro e escuro
- Na época da migração, MathJax e Mermaid não eram suportados nativamente pelo Minimal Mistakes e exigiam customização; no Chirpy, já vêm de fábrica. Não é uma customização difícil, mas é um bom ganho de conveniência.
- E, acima de tudo, o design é bonito. O Minimal Mistakes é limpo, porém passa uma sensação mais “documentação técnica/portfólio”; o Chirpy, em termos de visual, não fica devendo a plataformas como Tistory, Medium ou velog.

## 3. Criar repositório do GitHub, fazer build e implantar
Com base no Chirpy Jekyll Theme em uso no momento (12024.06), assumindo que o Git já está instalado.  
Consulte o [guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/) e a [página oficial do Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalar Ruby e Jekyll
Instale Ruby e Jekyll conforme seu sistema operacional, seguindo o [guia oficial de instalação do Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Criar repositório do GitHub
A [página oficial do Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) apresenta dois caminhos:
1. Usar o gem "jekyll-theme-chirpy" para importar os arquivos centrais e trazer os demais recursos a partir do template [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Vantagem: como veremos adiante, é mais fácil aplicar upgrades de versão.
  - Desvantagem: pode ser menos prático para customizações muito extensas.
2. Fazer fork do repositório [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) para o repositório do seu blog
  - Vantagem: você gerencia todos os arquivos no seu repositório, facilitando customizações que exigem alterar código e adicionar recursos não suportados pelo tema.
  - Desvantagem: para aplicar upgrades, é preciso fazer merge com a [tag upstream mais recente](https://github.com/cotes2020/jekyll-theme-chirpy/tags) do repositório original; dependendo do caso, as alterações locais podem conflitar com o código da nova versão, e você terá de resolver os conflitos.

Adotei a opção 1. O Chirpy é bastante maduro e, para a maioria dos usuários, há pouco a customizar; além disso, até 12024 segue em desenvolvimento ativo, com melhorias frequentes. A menos que você pretenda modificá-lo a fundo, acompanhar o upstream traz mais benefícios do que manter um fork altamente customizado. O próprio guia do Chirpy recomenda a opção 1 para a maioria.

### 3-3. Configurações principais
Aplique as configurações necessárias nos arquivos `_config.yml`{: .filepath} (na raiz), `_data/contact.yml`{: .filepath} e `_data/share.yml`{: .filepath}. Os comentários são claros e as opções, intuitivas. Entre os ajustes externos, destacam-se o código de verificação para o Google Search Console e a integração com ferramentas como Google Analytics ou GoatCounter; não são processos complexos e não são o foco deste texto, então vou poupar os detalhes.

### 3-4. Fazer build localmente
Não é obrigatório, mas ao escrever um novo post ou alterar algo no site, pode ser útil conferir previamente o resultado. No diretório raiz do repositório local, abra o terminal e execute:
```console
$ bundle exec jekyll s
```
Após a conclusão do build local, acesse o resultado em <http://127.0.0.1:4000>.

### 3-5. Implantar
Há duas formas:
1. Usar GitHub Actions (quando hospedado no GitHub Pages)
  - Se estiver no plano gratuito do GitHub, mantenha o repositório como público
  - Na interface do GitHub, abra a aba *Settings* do repositório, clique em *Code and automation > Pages* na barra lateral e, na seção **Source**, selecione a opção **GitHub Actions**
  - Após configurar, a cada novo push o workflow de *Build and Deploy* será executado automaticamente
2. Fazer o build local e enviar (para outro provedor de hospedagem ou self-hosting)
  - Execute o comando abaixo para construir o site:
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Envie o conteúdo gerado no diretório `_site` para o servidor

## 4. Escrevendo posts
O guia de escrita do Chirpy está bem documentado: [Chirpy Jekyll Theme — Write a new post](https://chirpy.cotes.page/posts/write-a-new-post/). Além do que menciono aqui, há muitos recursos úteis — consulte a documentação quando necessário. O básico do GitHub Flavored Markdown eu resumi em [um post à parte](/posts/github-markdown-syntax-summary/). Abaixo, pontos que costumo considerar em todo post.

### Criar o arquivo Markdown
- Formato do nome: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Local: diretório `_posts`{: .filepath}

### Escrever o Front Matter
Na primeira parte do arquivo Markdown, escreva um Front Matter apropriado.
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
- **title**: título do post
- **description**: resumo. Se omitido, um trecho inicial do corpo é usado automaticamente, mas para SEO é recomendável escrever uma descrição adequada manualmente. Em caracteres latinos, cerca de 135–160; em coreano, 80–110.
- **date**: data/hora exata do post e timezone (opcional; se omitido, usa a data de criação/edição do arquivo)
- **categories**: categorias do post
- **tags**: tags do post
- **image**: insere uma imagem de destaque no topo
  - **path**: caminho do arquivo da imagem
  - **alt**: texto alternativo (opcional)
- **toc**: ativa a tabela de conteúdo na barra lateral direita; padrão `true`
- **comments**: para habilitar/desabilitar comentários neste post, independentemente da configuração global do site
- **math**: ativa fórmulas via [MathJax](https://www.mathjax.org/); por desempenho, o padrão é desativado (`false`)
- **mermaid**: ativa diagramas via [Mermaid](https://github.com/mermaid-js/mermaid); padrão desativado (`false`)

## 5. Atualização

Parto do princípio de que você escolheu a opção 1 em [3-2](#3-2-criar-repositorio-do-github). Se tiver escolhido a 2, como dito, será preciso fazer merge com a tag upstream mais recente.

1. Edite o `Gemfile`{: .filepath} e defina a nova versão do gem "jekyll-theme-chirpy".
2. Em upgrades maiores, arquivos centrais e opções de configuração fora do gem "jekyll-theme-chirpy" podem ter mudado. Nesse caso, verifique as diferenças pela API do GitHub abaixo e aplique-as manualmente:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
