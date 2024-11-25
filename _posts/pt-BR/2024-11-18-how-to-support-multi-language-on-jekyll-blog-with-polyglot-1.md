---
title: Como suportar múltiplos idiomas em um blog Jekyll com Polyglot (1) - Aplicando o plugin Polyglot e implementando tags hreflang alt, sitemap e botão de seleção de idioma
description: >-
  Apresenta o processo de implementação de suporte multilíngue em um blog Jekyll baseado no tema 'jekyll-theme-chirpy' usando o plugin Polyglot.
  Este post é o primeiro da série, cobrindo a aplicação do plugin Polyglot e a modificação do cabeçalho HTML e do sitemap.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
---
## Visão geral
Há cerca de 4 meses, no início de julho de 2024, adicionei suporte multilíngue a este blog baseado em Jekyll, hospedado via Github Pages, aplicando o plugin [Polyglot](https://github.com/untra/polyglot).
Esta série compartilha os bugs encontrados durante o processo de aplicação do plugin Polyglot ao tema Chirpy, suas soluções, e métodos para escrever cabeçalhos HTML e sitemap.xml considerando SEO.
A série consiste em dois posts, e este é o primeiro deles.
- Parte 1: Aplicando o plugin Polyglot e implementando tags hreflang alt, sitemap e botão de seleção de idioma (este post)
- Parte 2: [Solucionando problemas de falha na compilação do tema Chirpy e erros na função de busca](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requisitos
- [x] Deve ser capaz de fornecer o resultado da compilação (páginas web) separado por caminhos de idioma (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar o tempo e esforço adicionais necessários para o suporte multilíngue, deve ser capaz de reconhecer automaticamente o idioma com base no caminho local onde o arquivo markdown original está localizado (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante a compilação, sem a necessidade de especificar manualmente as tags 'lang' e 'permalink' no YAML front matter de cada arquivo markdown escrito.
- [x] O cabeçalho de cada página do site deve incluir meta tags Content-Language apropriadas e tags alternativas hreflang para atender às diretrizes de SEO para busca multilíngue do Google.
- [x] Deve ser capaz de fornecer links para todas as páginas que suportam cada idioma no site, sem omissões, no `sitemap.xml`, e o próprio `sitemap.xml` deve existir apenas uma vez no caminho raiz, sem duplicações.
- [x] Todas as funcionalidades fornecidas pelo [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) devem funcionar normalmente em cada página de idioma, e caso contrário, devem ser modificadas para funcionar corretamente.
  - [x] Funcionamento normal das funcionalidades 'Recently Updated' e 'Trending Tags'
  - [x] Sem erros durante o processo de compilação usando GitHub Actions
  - [x] Funcionamento normal da função de busca de posts no canto superior direito do blog

## Aplicando o plugin Polyglot
Como o Jekyll não suporta nativamente blogs multilíngues, é necessário utilizar um plugin externo para implementar um blog multilíngue que atenda aos requisitos acima. Após pesquisar, descobri que o [Polyglot](https://github.com/untra/polyglot) é amplamente utilizado para implementação de sites multilíngues e pode satisfazer a maioria dos requisitos acima, então adotei este plugin.

### Instalação do plugin
Como estou usando o Bundler, adicionei o seguinte conteúdo ao `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Depois, executar `bundle update` no terminal completa automaticamente a instalação.

Se você não estiver usando o Bundler, pode instalar a gem diretamente com o comando `gem install jekyll-polyglot` no terminal e então adicionar o plugin ao `_config.yml` da seguinte forma:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuração
Em seguida, abra o arquivo `_config.yml` e adicione o seguinte conteúdo:

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Lista de idiomas que você deseja suportar
- default_lang: Idioma padrão de fallback
- exclude_from_localization: Especifica expressões regulares de strings de caminhos de arquivos/pastas raiz a serem excluídos da localização
- parallel_localization: Valor booleano que especifica se deve paralelizar o processamento multilíngue durante a compilação
- lang_from_path: Valor booleano, se definido como 'true', reconhece e usa automaticamente o código de idioma se a string do caminho do arquivo markdown contiver o código de idioma, mesmo que o atributo 'lang' não seja especificado explicitamente no YAML front matter dentro do arquivo markdown do post

> A [documentação oficial do protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) afirma o seguinte:
>
>> "A localização de um arquivo Sitemap determina o conjunto de URLs que podem ser incluídos nesse Sitemap. Um arquivo Sitemap localizado em http://example.com/catalog/sitemap.xml pode incluir quaisquer URLs começando com http://example.com/catalog/ mas não pode incluir URLs começando com http://example.com/images/."
>
>> "É fortemente recomendado que você coloque seu Sitemap no diretório raiz do seu servidor web."
>
> Para cumprir isso, deve-se adicionar 'sitemap' à lista 'exclude_from_localization' para garantir que apenas um arquivo `sitemap.xml` com o mesmo conteúdo exista no diretório raiz, e não seja criado para cada idioma, evitando o seguinte exemplo incorreto.
>
> Exemplo incorreto (o conteúdo de cada arquivo é idêntico, não diferindo por idioma):
> - /sitemap.xml
> - /ko/sitemap.xml
> - /es/sitemap.xml
> - /pt-BR/sitemap.xml
> - /ja/sitemap.xml
> - /fr/sitemap.xml
> - /de/sitemap.xml
{: .prompt-tip }

> Definir 'parallel_localization' como 'true' pode reduzir significativamente o tempo de compilação, mas a partir de julho de 2024, quando essa funcionalidade foi ativada para este blog, havia um bug onde os títulos dos links nas seções 'Recently Updated' e 'Trending Tags' na barra lateral direita da página não eram processados corretamente e se misturavam com outros idiomas. Parece que ainda não está totalmente estabilizado, então é necessário testar previamente se funciona normalmente antes de aplicar ao site. Além disso, [essa funcionalidade não é suportada ao usar Windows, então deve ser desativada](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Além disso, [no Jekyll 4.0, é necessário desativar a geração de sourcemaps CSS da seguinte forma](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # No Jekyll 4.0, os mapas de origem SCSS serão gerados incorretamente devido à forma como o Polyglot opera
```
{: file='_config.yml'}

### Pontos a considerar ao escrever posts
Ao escrever posts multilíngues, deve-se considerar o seguinte:
- Especificação apropriada do código de idioma: Deve-se especificar o código de idioma ISO apropriado usando o caminho do arquivo (ex. `/_posts/ko/example-post.md`{: .filepath}) ou o atributo 'lang' no YAML front matter (ex. `lang: ko`). Consulte os exemplos na [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> No entanto, embora a [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) use o formato 'pt_BR' para códigos regionais, na prática, deve-se usar '-' em vez de '_', como em 'pt-BR', para que funcione corretamente ao adicionar tags alternativas hreflang ao cabeçalho HTML posteriormente.

- O caminho e o nome do arquivo devem ser consistentes.

Para mais detalhes, consulte o [README do repositório GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modificando o cabeçalho HTML e o sitemap
Agora, para SEO, precisamos inserir meta tags Content-Language e tags alternativas hreflang no cabeçalho HTML de cada página do blog.

### Cabeçalho HTML
A partir da versão 1.8.1, a mais recente em novembro de 2024, o Polyglot tem uma funcionalidade que realiza automaticamente as tarefas acima quando a tag Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} é chamada na parte do cabeçalho da página.
No entanto, isso pressupõe que a tag de atributo 'permalink' foi especificada explicitamente para aquela página, e não funcionará corretamente se não for o caso.

Portanto, eu peguei o [head.html do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) e adicionei diretamente o seguinte conteúdo.
Trabalhei com referência à [página SEO Recipes do blog oficial do Polyglot](https://polyglot.untra.io/seo/), mas modifiquei para usar o atributo `page.url` em vez de `page.permalink` quando `page.permalink` não está disponível.
Além disso, referenciando a [documentação oficial do Google Search Central](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault), especifiquei `x-default` em vez de `site.default_lang` como o valor do atributo hreflang para a página do idioma padrão do site, para que o link dessa página seja reconhecido como fallback quando o idioma preferido do visitante não está na lista de idiomas suportados pelo site ou quando o idioma preferido do visitante não pode ser reconhecido.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="x-default" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### Sitemap
Como o sitemap gerado automaticamente pelo Jekyll durante a compilação não suporta corretamente páginas multilíngues, crie um arquivo `sitemap.xml` no diretório raiz e insira o seguinte conteúdo:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- verificação muito preguiçosa para ver se a página está na lista de exclusão - isso significa que as páginas excluídas não estarão no sitemap de forma alguma, escreva exceções conforme necessário -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- assumindo que se não houver layout atribuído, então não inclua a página no sitemap, você pode querer mudar isso -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- Isso percorre todas as coleções do site, incluindo posts -->{% endcomment %}
    {% for collection in site.collections %}
        {% for node in site[collection.label] %}
            <url>
                <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
            </url>
        {% endfor %}
    {% endfor %}

{% endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## Adicionando botão de seleção de idioma na barra lateral
Crie um arquivo `_includes/lang-selector.html` e insira o seguinte conteúdo:

{% raw %}
```liquid
<p>
{%- for lang in site.languages -%}
  {%- if lang == site.default_lang -%}
<a ferh="{{ page.url }}" style="display:inline-block; white-space:nowrap;">
    {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- else -%}
<a href="/{{ lang }}{{ page.url }}" style="display:inline-block; white-space:nowrap;">
  {%- if lang == site.active_lang -%}
      <b>{{ lang }}</b>
    {%- else -%}
      {{ lang }}
    {%- endif -%}
</a>
  {%- endif -%}
{%- endfor -%}
</p>
```
{: file='_includes/lang-selector.html'}
{% endraw %}

Em seguida, adicione as seguintes três linhas à parte da classe "sidebar-bottom" no [`_includes/sidebar.html` do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) para que o Jekyll carregue o conteúdo do `_includes/lang-selector.html` criado anteriormente durante a compilação da página:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Leitura Adicional
Continuado na [Parte 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
