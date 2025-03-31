---
title: Como suportar múltiplos idiomas em um blog Jekyll com Polyglot (1) - Aplicando o plugin Polyglot e implementando tags hreflang alt, sitemap e botão de seleção de idioma
description: 'Apresentamos o processo de implementação de suporte multilíngue usando o plugin Polyglot em um blog Jekyll baseado no tema "jekyll-theme-chirpy". Este post é o primeiro da série e aborda a aplicação do plugin Polyglot e a modificação do cabeçalho HTML e do sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---

## Visão geral

No início de julho do ano 12024 do [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), há cerca de 4 meses, adicionei suporte multilíngue a este blog baseado em Jekyll e hospedado via GitHub Pages, aplicando o plugin [Polyglot](https://github.com/untra/polyglot).

Esta série compartilha os bugs encontrados durante o processo de aplicação do plugin Polyglot ao tema Chirpy, seus processos de resolução e métodos para escrever cabeçalhos HTML e sitemap.xml considerando SEO.

A série consiste em dois posts, e este que você está lendo é o primeiro da série.

- Parte 1: Aplicando o plugin Polyglot e implementando tags hreflang alt, sitemap e botão de seleção de idioma (este post)
- Parte 2: [Solucionando problemas de falha na compilação do tema Chirpy e erros na função de pesquisa](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requisitos

- [x] Deve ser possível fornecer o resultado da compilação (páginas web) separado por caminhos de idioma (ex. `/posts/pt-BR/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar o tempo e esforço adicionais necessários para o suporte multilíngue, deve ser possível reconhecer automaticamente o idioma com base no caminho local onde o arquivo está localizado (ex. `/_posts/pt-BR/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante a compilação, sem a necessidade de especificar manualmente as tags 'lang' e 'permalink' no YAML front matter do arquivo markdown original.
- [x] O cabeçalho de cada página do site deve incluir meta tags Content-Language apropriadas e tags alternativas hreflang para atender às diretrizes de SEO para pesquisa multilíngue do Google.
- [x] Deve ser possível fornecer links para todas as páginas que suportam cada idioma no site, sem omissões, no `sitemap.xml`{: .filepath}, e o próprio `sitemap.xml`{: .filepath} deve existir apenas uma vez no caminho raiz, sem duplicações.
- [x] Todas as funcionalidades fornecidas pelo [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) devem funcionar normalmente em cada página de idioma, e caso contrário, devem ser modificadas para funcionar corretamente.
  - [x] Funcionamento normal das funcionalidades 'Recently Updated' e 'Trending Tags'
  - [x] Sem erros durante o processo de compilação usando GitHub Actions
  - [x] Funcionamento normal da função de pesquisa de posts no canto superior direito do blog

## Aplicando o plugin Polyglot

Como o Jekyll não suporta nativamente blogs multilíngues, é necessário utilizar um plugin externo para implementar um blog multilíngue que atenda aos requisitos acima. Após pesquisar, descobri que o [Polyglot](https://github.com/untra/polyglot) é amplamente utilizado para implementação de sites multilíngues e pode satisfazer a maioria dos requisitos acima, então adotei esse plugin.

### Instalação do plugin

Como estou usando o Bundler, adicionei o seguinte conteúdo ao `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Em seguida, executar `bundle update` no terminal completará a instalação automaticamente.

Se você não estiver usando o Bundler, você pode instalar a gem diretamente com o comando `gem install jekyll-polyglot` no terminal e então adicionar o plugin ao `_config.yml`{: .filepath} da seguinte forma:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuração

Em seguida, abra o arquivo `_config.yml`{: .filepath} e adicione o seguinte conteúdo:

```yml
# Configurações do Polyglot
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Lista de idiomas que você deseja suportar
- default_lang: Idioma padrão de fallback
- exclude_from_localization: Especifica expressões regulares de strings de caminhos de arquivos/pastas raiz a serem excluídos da localização
- parallel_localization: Valor booleano que especifica se o processamento multilíngue deve ser paralelizado durante a compilação
- lang_from_path: Valor booleano que, quando definido como 'true', reconhece e usa automaticamente o código de idioma se a string do caminho do arquivo markdown contiver o código de idioma, mesmo que o atributo 'lang' não seja especificado explicitamente no YAML front matter dentro do arquivo markdown

> A [documentação oficial do protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) afirma o seguinte:
>
>> "A localização de um arquivo Sitemap determina o conjunto de URLs que podem ser incluídos nesse Sitemap. Um arquivo Sitemap localizado em http://example.com/catalog/sitemap.xml pode incluir quaisquer URLs começando com http://example.com/catalog/ mas não pode incluir URLs começando com http://example.com/images/."
>
>> "É fortemente recomendado que você coloque seu Sitemap no diretório raiz do seu servidor web."
>
> Para cumprir isso, é necessário adicionar 'sitemap' à lista 'exclude_from_localization' para garantir que apenas um arquivo `sitemap.xml`{: .filepath} exista no diretório raiz, e não seja criado para cada idioma com o mesmo conteúdo, como no exemplo incorreto abaixo.
>
> Exemplo incorreto (o conteúdo de cada arquivo é idêntico, não diferindo por idioma):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Atualização de 14.01.12025) Com a aceitação do [Pull Request que submeti reforçando o conteúdo mencionado acima no README](https://github.com/untra/polyglot/pull/230), agora a mesma orientação pode ser encontrada na [documentação oficial do Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Definir 'parallel_localization' como 'true' tem a vantagem de reduzir significativamente o tempo de compilação, mas a partir de julho de 12024, quando essa funcionalidade foi ativada para este blog, havia um bug onde os títulos dos links nas seções 'Recently Updated' e 'Trending Tags' na barra lateral direita da página não eram processados corretamente e se misturavam com outros idiomas. Parece que ainda não está totalmente estabilizado, então é necessário testar previamente se funciona normalmente antes de aplicar ao site. Além disso, [a funcionalidade também não é suportada ao usar Windows, então deve ser desativada](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Além disso, [no Jekyll 4.0, é necessário desativar a geração de sourcemaps CSS da seguinte forma](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # No Jekyll 4.0, os mapas de origem SCSS serão gerados incorretamente devido à forma como o Polyglot opera
```
{: file='_config.yml'}

### Pontos a considerar ao escrever posts

Ao escrever posts multilíngues, é necessário considerar os seguintes pontos:
- Especificação adequada do código de idioma: É necessário especificar o código de idioma ISO apropriado usando o caminho do arquivo (ex. `/_posts/pt-BR/example-post.md`{: .filepath}) ou o atributo 'lang' no YAML front matter (ex. `lang: pt-BR`). Consulte os exemplos na [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> No entanto, embora a [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) use o formato 'pt_BR' para códigos regionais, na prática, deve-se usar 'pt-BR' com um hífen (-) em vez de um sublinhado (_) para que funcione corretamente ao adicionar tags alternativas hreflang ao cabeçalho HTML posteriormente.

- O caminho e o nome do arquivo devem ser consistentes.

Para mais detalhes, consulte o [README do repositório GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modificação do cabeçalho HTML e sitemap

Agora, para SEO, é necessário inserir meta tags Content-Language e tags alternativas hreflang no cabeçalho HTML de cada página do blog.

### Cabeçalho HTML

Com base na versão 1.8.1, a mais recente até novembro de 12024, o Polyglot tem uma funcionalidade que realiza automaticamente as tarefas acima quando a tag Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} é chamada na seção de cabeçalho da página.
No entanto, isso assume que o atributo 'permalink' foi especificado explicitamente para a página em questão, e não funcionará corretamente se não for o caso.

Portanto, eu trouxe o [head.html do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) e adicionei diretamente o seguinte conteúdo.
Trabalhei com referência à [página SEO Recipes do blog oficial do Polyglot](https://polyglot.untra.io/seo/), mas modifiquei para usar o atributo `page.url` em vez de `page.permalink` quando este não estiver disponível.

{% raw %}
```liquid
  <meta http-equiv="Content-Language" content="{{site.active_lang}}">

  {% if site.default_lang %}<link rel="alternate" hreflang="{{site.default_lang}}" href="{{site.url}}{{page.url}}" />{% endif %}
  {% for lang in site.languages %}{% if lang == site.default_lang %}{% continue %}{% endif %}
  <link rel="alternate" hreflang="{{lang}}" href="{{site.url}}/{{lang}}{{page.url}}" />
  {% endfor %}
```
{: file='/_includes/head.html'}
{% endraw %}

### Sitemap

Como o sitemap gerado automaticamente pelo Jekyll durante a compilação não suporta corretamente páginas multilíngues, crie um arquivo `sitemap.xml`{: .filepath} no diretório raiz e insira o seguinte conteúdo:

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

(Atualização de 05.02.12025) Melhorei o botão de seleção de idioma para um formato de lista suspensa.
Criei o arquivo `_includes/lang-selector.html`{: .filepath} e inseri o seguinte conteúdo:

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Selecionar Idioma">
    {%- for lang in site.languages -%}
        <option value="{% if lang == site.default_lang %}{{ page.url }}{% else %}/{{ lang }}{{ page.url }}{% endif %}"
                {% if lang == site.active_lang %}selected{% endif %}>
            {% case lang %}
            {% when 'ko' %}🇰🇷 한국어
            {% when 'en' %}🇺🇸 English
            {% when 'ja' %}🇯🇵 日本語
            {% when 'zh-TW' %}🇹🇼 正體中文
            {% when 'es' %}🇪🇸 Español
            {% when 'pt-BR' %}🇧🇷 Português
            {% when 'fr' %}🇫🇷 Français
            {% when 'de' %}🇩🇪 Deutsch
            {% else %}{{ lang }}
            {% endcase %}
        </option>
    {%- endfor -%}
    </select>
</div>

<script>
function changeLang(url) {
    window.location.href = url;
}
</script>
```
{: file='_includes/lang-selector.html'}
{% endraw %}

Além disso, criei o arquivo `assets/css/lang-selector.css`{: .filepath} e inseri o seguinte conteúdo:

```css
/**
 * Estilo do seletor de idioma
 * 
 * Define o estilo do dropdown de seleção de idioma localizado na barra lateral.
 * Suporta o modo escuro do tema e é otimizado para ambientes móveis.
 */

/* Container do seletor de idioma */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Container do dropdown */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Elemento de entrada de seleção */
.lang-select {
    /* Estilo básico */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Fonte e cor */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Forma e interação */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Adição do ícone de seta */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Estilo dos emojis de bandeira */
.lang-select option {
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
    padding: 0.35rem;
    font-size: 1rem;
}

.lang-flag {
    display: inline-block;
    margin-right: 0.5rem;
    font-family: "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji", sans-serif;
}

/* Estado de hover */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* Estado de foco */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Suporte para o navegador Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Suporte para o navegador IE */
.lang-select::-ms-expand {
    display: none;
}

/* Suporte para o modo escuro */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Otimização para ambiente móvel */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Área de toque maior */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Área de seleção mais ampla em dispositivos móveis */
    }
}
```
{: file='assets/css/lang-selector.css'}

Em seguida, adicionei as seguintes três linhas logo antes da classe "sidebar-bottom" no [`_includes/sidebar.html`{: .filepath} do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) para que o Jekyll carregue o conteúdo do `_includes/lang-selector.html`{: .filepath} criado anteriormente durante a compilação da página:

{% raw %}
```liquid
  (início)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(fim)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Leitura adicional

Continua na [Parte 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
