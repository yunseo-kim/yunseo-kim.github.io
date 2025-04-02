---
title: Como suportar múltiplos idiomas em um blog Jekyll com Polyglot (1) - Aplicando o plugin Polyglot & implementando tags hreflang alt, sitemap e botão de seleção de idioma
description: 'Apresento o processo de implementação de suporte multilíngue em um blog Jekyll baseado no ''jekyll-theme-chirpy'' usando o plugin Polyglot. Este post é o primeiro da série e aborda a aplicação do plugin Polyglot e a modificação do cabeçalho html e sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---
## Visão geral
Cerca de 4 meses atrás, no início de julho do [calendário holocene](https://en.wikipedia.org/wiki/Holocene_calendar) 12024, adicionei suporte multilíngue ao meu blog baseado em Jekyll hospedado no Github Pages aplicando o plugin [Polyglot](https://github.com/untra/polyglot).
Esta série compartilha o processo de aplicação do plugin Polyglot ao tema Chirpy, os bugs encontrados e suas soluções, além de como escrever cabeçalhos html e sitemap.xml considerando SEO.
A série consiste em 2 posts, e este é o primeiro.
- Parte 1: Aplicando o plugin Polyglot & implementando tags hreflang alt, sitemap e botão de seleção de idioma (este post)
- Parte 2: [Solucionando problemas de falha na compilação do tema Chirpy e erros na função de busca](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requisitos
- [x] O resultado da compilação (páginas web) deve ser fornecido em caminhos separados por idioma (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar o tempo e esforço adicionais necessários para o suporte multilíngue, o sistema deve reconhecer automaticamente o idioma com base no caminho local do arquivo markdown original (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante a compilação, sem precisar especificar manualmente as tags 'lang' e 'permalink' no YAML front matter.
- [x] O cabeçalho de cada página do site deve incluir meta tags Content-Language apropriadas e tags alternativas hreflang para atender às diretrizes de SEO para busca multilíngue do Google.
- [x] O `sitemap.xml`{: .filepath} deve fornecer links para todas as páginas em todos os idiomas suportados sem omissões, e o próprio `sitemap.xml`{: .filepath} deve existir apenas uma vez no caminho raiz, sem duplicações.
- [x] Todas as funcionalidades fornecidas pelo [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) devem funcionar normalmente em cada página de idioma, ou devem ser modificadas para funcionar corretamente.
  - [x] Funcionamento normal das funcionalidades 'Recently Updated' e 'Trending Tags'
  - [x] Sem erros durante o processo de compilação usando GitHub Actions
  - [x] Funcionamento normal da função de busca de posts no canto superior direito do blog

## Aplicando o plugin Polyglot
Como o Jekyll não suporta blogs multilíngues nativamente, é necessário usar um plugin externo para implementar um blog multilíngue que atenda aos requisitos acima. Após pesquisar, descobri que o [Polyglot](https://github.com/untra/polyglot) é amplamente usado para implementação de sites multilíngues e pode satisfazer a maioria dos requisitos acima, então adotei este plugin.

### Instalação do plugin
Como estou usando o Bundler, adicionei o seguinte ao meu `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Em seguida, execute `bundle update` no terminal para completar a instalação automaticamente.

Se você não estiver usando o Bundler, pode instalar a gem diretamente com o comando `gem install jekyll-polyglot` no terminal e depois adicionar o plugin ao seu `_config.yml`{: .filepath} da seguinte forma:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuração
Em seguida, abra o arquivo `_config.yml`{: .filepath} e adicione o seguinte conteúdo:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Lista de idiomas que você deseja suportar
- default_lang: Idioma padrão de fallback
- exclude_from_localization: Expressões regulares de strings de caminhos de arquivos/pastas raiz a serem excluídos da localização
- parallel_localization: Valor booleano que especifica se o processamento multilíngue deve ser paralelizado durante a compilação
- lang_from_path: Valor booleano que, quando definido como 'true', reconhece e usa automaticamente o código de idioma incluído na string de caminho do arquivo markdown, mesmo que o atributo 'lang' não seja especificado explicitamente no YAML front matter do arquivo markdown

> A [documentação oficial do protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) especifica o seguinte:
>
>> "A localização de um arquivo Sitemap determina o conjunto de URLs que podem ser incluídos nesse Sitemap. Um arquivo Sitemap localizado em http://example.com/catalog/sitemap.xml pode incluir quaisquer URLs começando com http://example.com/catalog/ mas não pode incluir URLs começando com http://example.com/images/."
>
>> "É fortemente recomendado que você coloque seu Sitemap no diretório raiz do seu servidor web."
>
> Para cumprir isso, você deve adicionar 'sitemap' à lista 'exclude_from_localization' para garantir que o arquivo `sitemap.xml`{: .filepath} exista apenas uma vez no diretório raiz e não seja criado para cada idioma, evitando o exemplo incorreto abaixo.
>
> Exemplo incorreto (o conteúdo de cada arquivo é idêntico, não diferente por idioma):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Atualização 14.01.12025) O [Pull Request que submeti com o conteúdo acima adicionado ao README](https://github.com/untra/polyglot/pull/230) foi aceito, então agora você pode verificar a mesma orientação na [documentação oficial do Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Definir 'parallel_localization' como 'true' pode reduzir significativamente o tempo de compilação, mas em julho de 12024, quando ativei esse recurso para este blog, havia um bug onde os links de título nas seções 'Recently Updated' e 'Trending Tags' na barra lateral direita da página não eram processados corretamente e se misturavam com outros idiomas. Parece que ainda não está totalmente estabilizado, então é necessário testar previamente se funciona normalmente antes de aplicar ao site. Além disso, [se você estiver usando Windows, esse recurso não é suportado e deve ser desativado](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Além disso, [no Jekyll 4.0, você deve desativar a geração de sourcemaps CSS da seguinte forma](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Considerações ao escrever posts
Ao escrever posts multilíngues, observe o seguinte:
- Especificação adequada do código de idioma: Você deve especificar o código ISO de idioma apropriado usando o caminho do arquivo (ex. `/_posts/ko/example-post.md`{: .filepath}) ou o atributo 'lang' no YAML front matter (ex. `lang: ko`). Consulte os exemplos na [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> No entanto, embora a [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) mostre códigos de região no formato 'pt_BR', você deve usar 'pt-BR' com um hífen em vez de sublinhado para que as tags alternativas hreflang funcionem corretamente quando adicionadas ao cabeçalho html posteriormente.

- Os caminhos e nomes dos arquivos devem ser consistentes.

Para mais detalhes, consulte o [README do repositório GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modificando o cabeçalho html e o sitemap
Agora, para SEO, precisamos inserir meta tags Content-Language e tags alternativas hreflang no cabeçalho html de cada página do blog.

### Cabeçalho html
Na versão 1.8.1, a mais recente em novembro de 12024, o Polyglot tem uma funcionalidade que realiza automaticamente essa tarefa quando a tag Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} é chamada na seção de cabeçalho da página.
No entanto, isso pressupõe que a tag de atributo 'permalink' foi especificada para essa página, e não funcionará corretamente se não for o caso.

Portanto, peguei o [head.html do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) e adicionei diretamente o seguinte conteúdo:
Baseei-me na [página SEO Recipes do blog oficial do Polyglot](https://polyglot.untra.io/seo/), mas modifiquei para usar o atributo `page.url` em vez de `page.permalink` quando este não estiver disponível.

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
        {% comment %}<!-- very lazy check to see if page is in the exclude list - this means excluded pages are not gonna be in the sitemap at all, write exceptions as necessary -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- assuming if there's not layout assigned, then not include the page in the sitemap, you may want to change this -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- This loops through all site collections including posts -->{% endcomment %}
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
(Atualização 05.02.12025) Melhorei o botão de seleção de idioma para um formato de lista suspensa.  
Crie o arquivo `_includes/lang-selector.html`{: .filepath} e insira o seguinte conteúdo:

{% raw %}
```liquid
<link rel="stylesheet" href="{{ '/assets/css/lang-selector.css' | relative_url }}">

<div class="lang-dropdown">
    <select class="lang-select" onchange="changeLang(this.value)" aria-label="Select Language">
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

Além disso, crie o arquivo `assets/css/lang-selector.css`{: .filepath} e insira o seguinte conteúdo:

```css
/**
 * Estilos do seletor de idioma
 * 
 * Define os estilos para o dropdown de seleção de idioma localizado na barra lateral.
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
    /* Estilos básicos */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Fonte e cores */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Forma e interação */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Adicionando ícone de seta */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Estilos para emojis de bandeiras */
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

/* Compatibilidade com Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Compatibilidade com IE */
.lang-select::-ms-expand {
    display: none;
}

/* Compatibilidade com modo escuro */
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

Em seguida, adicione as três linhas a seguir logo antes da classe "sidebar-bottom" no [arquivo `_includes/sidebar.html`{: .filepath} do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) para que o Jekyll carregue o conteúdo do `_includes/lang-selector.html`{: .filepath} durante a compilação da página:

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

## Leitura Adicional
Continua na [Parte 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
