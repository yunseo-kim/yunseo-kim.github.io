---
title: "Como implementar suporte multilíngue em blog Jekyll com Polyglot (1) - Aplicação do plugin Polyglot & modificação do cabeçalho html e sitemap"
description: "Apresenta o processo de implementação de suporte multilíngue aplicando o plugin Polyglot em um blog Jekyll baseado no tema 'jekyll-theme-chirpy'. Este post é o primeiro da série, abordando a aplicação do plugin Polyglot e a modificação do cabeçalho html e sitemap."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---

## Visão Geral
No início de julho de 12024, implementei suporte multilíngue neste blog hospedado no Github Pages baseado em Jekyll aplicando o plugin [Polyglot](https://github.com/untra/polyglot).
Esta série compartilha os bugs que ocorreram durante o processo de aplicação do plugin Polyglot ao tema Chirpy e seus processos de resolução, além de como escrever cabeçalhos html e sitemap.xml considerando SEO.
A série consiste em 3 posts, e este post que você está lendo é o primeiro da série.
- Parte 1: Aplicação do plugin Polyglot & modificação do cabeçalho html e sitemap (este post)
- Parte 2: [Implementação do botão de seleção de idioma & localização do idioma do layout](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
- Parte 3: [Solução de problemas de falha de build do tema Chirpy e erro na função de busca](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> Originalmente foi composta por 2 partes, mas posteriormente foi reorganizada em 3 partes devido ao aumento significativo do conteúdo após várias melhorias.
{: .prompt-info }

## Requisitos
- [x] Deve ser possível fornecer o resultado do build (páginas web) separado por caminhos de idioma (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar o tempo e esforço adicionais necessários para suporte multilíngue, deve ser possível reconhecer automaticamente o idioma durante o build com base no caminho local onde o arquivo está localizado (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) sem especificar manualmente as tags 'lang' e 'permalink' no YAML front matter do arquivo markdown original.
- [x] A seção de cabeçalho de cada página do site deve incluir tags meta Content-Language apropriadas, tags alternativas hreflang e links canônicos para atender às diretrizes de SEO do Google para busca multilíngue.
- [x] Deve ser possível fornecer links de páginas para cada versão de idioma no site sem omissões através do `sitemap.xml`{: .filepath}, e o próprio `sitemap.xml`{: .filepath} deve existir apenas um no caminho raiz sem duplicação.
- [x] Todas as funcionalidades fornecidas pelo [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) devem funcionar normalmente em cada página de idioma, caso contrário, devem ser corrigidas para funcionar normalmente.
  - [x] Funcionamento normal das funcionalidades 'Recently Updated' e 'Trending Tags'
  - [x] Não deve ocorrer erros durante o processo de build usando GitHub Actions
  - [x] Funcionamento normal da função de busca de posts no canto superior direito do blog

## Aplicação do plugin Polyglot
Como o Jekyll não suporta blogs multilíngues nativamente, é necessário usar plugins externos para implementar um blog multilíngue que satisfaça os requisitos acima. Após pesquisar, descobri que o [Polyglot](https://github.com/untra/polyglot) é amplamente usado para implementação de sites multilíngues e pode satisfazer a maioria dos requisitos acima, então adotei esse plugin.

### Instalação do plugin
Como estou usando o Bundler, adicionei o seguinte conteúdo ao `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Depois, execute `bundle update` no terminal para completar a instalação automaticamente.

Se não estiver usando o Bundler, você pode instalar a gem diretamente com o comando `gem install jekyll-polyglot` no terminal e depois adicionar o plugin ao `_config.yml`{: .filepath} da seguinte forma.

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuração
Em seguida, abra o arquivo `_config.yml`{: .filepath} e adicione o conteúdo abaixo.

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- `languages`: Lista de idiomas que você deseja suportar
- `default_lang`: Idioma padrão de fallback
- `exclude_from_localization`: Especifica expressões regulares de strings de caminho de arquivos/pastas raiz para excluir da localização de idioma
- `parallel_localization`: Valor booleano que especifica se deve paralelizar o processamento multilíngue durante o build
- `lang_from_path`: Valor booleano, quando definido como 'true', reconhece e usa automaticamente se a string do caminho do arquivo markdown contém um código de idioma, mesmo sem especificar separadamente a propriedade 'lang' como YAML front matter no arquivo markdown do post

> A [documentação oficial do protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) especifica o seguinte:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Para cumprir isso, o arquivo `sitemap.xml`{: .filepath} com o mesmo conteúdo não deve ser criado por idioma, mas deve existir apenas um no diretório raiz, adicionando à lista 'exclude_from_localization' para evitar o exemplo incorreto abaixo.
>
> Exemplo incorreto (o conteúdo de cada arquivo não difere por idioma e é todo idêntico):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Atualização em 14.01.12025) Como o [Pull Request que enviei reforçando o conteúdo mencionado acima no README](https://github.com/untra/polyglot/pull/230) foi aceito, agora você pode encontrar a mesma orientação na [documentação oficial do Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Especificar 'parallel_localization' como 'true' tem a vantagem de reduzir significativamente o tempo de build, mas no momento de julho de 12024, quando ativei essa funcionalidade para este blog, havia um bug onde os títulos dos links das seções 'Recently Updated' e 'Trending Tags' na barra lateral direita da página não eram processados normalmente e se misturavam com outros idiomas. Como parece que ainda não está estabilizado, é necessário testar se funciona normalmente antes de aplicar ao site. Além disso, [se você estiver usando Windows, essa funcionalidade também não é suportada, então deve ser desabilitada](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Além disso, [no Jekyll 4.0, você deve desabilitar a geração de sourcemaps CSS da seguinte forma](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Precauções ao escrever posts
Os pontos a serem observados ao escrever posts multilíngues são os seguintes:
- Especificação apropriada do código de idioma: Você deve especificar o código de idioma ISO apropriado usando o caminho do arquivo (ex. `/_posts/ko/example-post.md`{: .filepath}) ou a propriedade 'lang' do YAML front matter (ex. `lang: ko`). Consulte os exemplos na [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> No entanto, embora a [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) represente códigos de região no formato 'pt_BR', na prática você deve usar - em vez de _ como 'pt-BR' para que funcione normalmente ao adicionar tags alternativas hreflang ao cabeçalho html posteriormente.
{: .prompt-tip }

- Os caminhos e nomes dos arquivos devem ser consistentes.

Para detalhes, consulte o [README do repositório GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modificação do cabeçalho html e sitemap
Agora precisamos inserir tags meta Content-Language e tags alternativas hreflang no cabeçalho html de cada página do blog para SEO, e especificar apropriadamente a URL canônica.

### Cabeçalho html
Com base na versão mais recente 1.8.1 em novembro de 12024, o Polyglot tem uma funcionalidade que executa automaticamente o trabalho acima ao chamar a tag Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} na seção de cabeçalho da página.
No entanto, isso pressupõe que a propriedade 'permalink' foi especificada para essa página, e não funciona normalmente caso contrário.

Portanto, peguei o [head.html do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) e adicionei diretamente o conteúdo abaixo.
Trabalhei consultando a [página SEO Recipes do blog oficial do Polyglot](https://polyglot.untra.io/seo/), mas modifiquei para usar a propriedade `page.url` em vez de `page.permalink` para adequar ao meu ambiente de uso e requisitos.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">
  
  {% if site.default_lang -%}
  <link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />
  {%- endif -%}
  {% for lang in site.languages -%}
    {% if lang == site.default_lang -%}
      {%- continue -%}
    {%- endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {%- endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

(Adicionado em 29.07.12025) Além disso, o tema Chirpy tem o plugin [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag) integrado por padrão, e confirmei que os metadados [Open Graph](https://ogp.me/) `og:locale`, `og:url` gerados automaticamente pelo Jekyll SEO Tag e a [URL canônica](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (elemento `link` `rel="canonical"`) são baseados no idioma padrão do site (`site.lang`, `site.default_lang`), necessitando processamento adicional.  
Portanto, adicionei a seguinte declaração antes de {% raw %}`{{ seo_tags }}`{% endraw %}.

{% raw %}
```liquid
(전략)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(중략)...

  {%- capture old_og_locale -%}
    <meta property="og:locale" content="{{site.lang}}" />
  {%- endcapture -%}
  {%- capture new_og_locale -%}
    <meta property="og:locale" content="{{site.active_lang}}" />
    {% for lang in site.languages -%}
      {%- if lang == site.active_lang -%}
        {%- continue -%}
      {%- endif %}
    <meta property="og:locale:alternate" content="{{lang}}" />
    {%- endfor %}
  {%- endcapture -%}
  {% assign seo_tags = seo_tags | replace: old_og_locale, new_og_locale %}
  
  {% unless site.active_lang == site.default_lang -%}
    {%- capture old_canonical_link -%}
      <link rel="canonical" href="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture old_og_url -%}
      <meta property="og:url" content="{{site.url}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_canonical_link -%}
      <link rel="canonical" href="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {%- capture new_og_url -%}
      <meta property="og:url" content="{{site.url}}/{{site.active_lang}}{{page.url}}" />
    {%- endcapture -%}
    {% assign seo_tags = seo_tags | replace: old_canonical_link, new_canonical_link %}
    {% assign seo_tags = seo_tags | replace: old_og_url, new_og_url %}
  {%- endunless %}

  {{ seo_tags }}

  ...(후략)
```
{: file='/_includes/head.html'}
{% endraw %}

> De acordo com a [documentação do desenvolvedor Google](https://developers.google.com/search/docs/crawling-indexing/canonicalization), quando uma página tem várias versões de idioma, elas são consideradas duplicatas apenas quando o idioma do conteúdo principal é o mesmo, ou seja, quando apenas cabeçalhos, rodapés e outros textos não importantes são traduzidos e o corpo principal é idêntico. Portanto, no caso de fornecer texto do corpo principal em vários idiomas como este blog, todas as versões de idioma são consideradas páginas independentes, não duplicatas, então você deve especificar URLs canônicas diferentes de acordo com o idioma.  
> Por exemplo, para a versão em português desta página, a URL canônica é "{{site.url}}/pt-BR{{page.url}}", não "{{site.url}}{{page.url}}".
{: .prompt-tip }

### sitemap
Como o sitemap gerado automaticamente pelo Jekyll durante o build não suporta normalmente páginas multilíngues quando nenhum template é especificado, crie um arquivo `sitemap.xml`{: .filepath} no diretório raiz e insira o seguinte conteúdo.

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages -%}

  {% for node in site.pages %}
    {%- comment -%}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{%- endcomment -%}
    {%- comment -%}<!-- Exclude redirects from sitemap -->{%- endcomment -%}
    {%- if node.redirect.to -%}
      {%- continue -%}
    {%- endif -%}
    {%- unless site.exclude_from_localization contains node.path -%}
      {%- comment -%}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{%- endcomment -%}
      {% if node.layout %}
        <url>
          <loc>
            {%- if lang == site.default_lang -%}
              {{ node.url | absolute_url }}
            {%- else -%}
              {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
            {%- endif -%}
          </loc>
          {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
          {% endif -%}
          {% if site.default_lang -%}
          <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
          {%- endif -%}
          {% for lang in site.languages -%}
            {% if lang == site.default_lang -%}
              {%- continue -%}
            {%- endif %}
          <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
          {%- endfor %}
        </url>
      {% endif %}
    {%- elsif site.default_lang -%}
        <url>
          <loc>{{ node.url | absolute_url }}</loc>
      {% if node.last_modified_at and node.last_modified_at != node.date -%}
          <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {%- elsif node.date -%}
          <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
      {% endif -%}
        </url>
    {%- endunless -%}
  {% endfor %}

  {%- comment -%}<!-- This loops through all site collections including posts -->{%- endcomment -%}
  {% for collection in site.collections %}
    {% for node in site[collection.label] %}
      <url>
        <loc>
          {%- if lang == site.default_lang -%}
            {{ node.url | absolute_url }}
          {%- else -%}
            {{ node.url | prepend: lang | prepend: '/' | absolute_url }}
          {%- endif -%}
        </loc>
        {% if node.last_modified_at and node.last_modified_at != node.date -%}
        <lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- elsif node.date -%}
        <lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>
        {%- endif %}
        {% if site.default_lang -%}
        <xhtml:link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{node.url}}" />
        {%- endif -%}
        {% for lang in site.languages -%}
          {% if lang == site.default_lang -%}
            {%- continue -%}
          {%- endif %}
        <xhtml:link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{node.url}}" />
        {%- endfor %}
      </url>
    {% endfor %}
  {% endfor %}

{%- endfor %}
</urlset>
```
{: file='sitemap.xml'}
{% endraw %}

## Leitura Adicional
Continuação na [Parte 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
