---
title: Como suportar múltiplos idiomas em um blog Jekyll usando Polyglot
description: >-
  Apresento o processo de implementação de suporte multilíngue aplicando o plugin Polyglot a um blog Jekyll baseado no tema 'jekyll-theme-chirpy'.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
- RegExp
---
## Introdução
Há cerca de 4 meses, no início de julho de 2024, adicionei suporte multilíngue ao meu blog hospedado no GitHub Pages baseado em Jekyll, aplicando o plugin [Polyglot](https://github.com/untra/polyglot).
Neste post, compartilho os bugs encontrados durante a aplicação do plugin Polyglot, o processo de resolução, e como escrever cabeçalhos HTML e sitemap.xml considerando SEO.

## Requisitos
- [x] Deve ser possível fornecer o resultado da compilação (páginas web) separado por caminhos de idioma (ex. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar o tempo e esforço adicionais necessários para o suporte multilíngue, deve ser possível reconhecer automaticamente o idioma com base no caminho local onde o arquivo está localizado (ex. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante a compilação, sem ter que especificar manualmente as tags 'lang' e 'permalink' no YAML front matter do arquivo markdown original.
- [x] O cabeçalho de cada página do site deve incluir meta tags Content-Language apropriadas e tags alternativas hreflang para atender às diretrizes de SEO para pesquisa multilíngue do Google.
- [x] Deve ser possível fornecer links para todas as páginas que suportam cada idioma no site sem omissões no `sitemap.xml`, e o próprio `sitemap.xml` deve existir apenas uma vez no caminho raiz, sem duplicações.
- [ ] Todas as funcionalidades fornecidas pelo [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) devem funcionar normalmente em cada página de idioma, e caso contrário, devem ser modificadas para funcionar corretamente.

## Aplicando o plugin Polyglot
Como o Jekyll não suporta nativamente blogs multilíngues, é necessário usar um plugin externo para implementar um blog multilíngue que atenda aos requisitos acima. Após pesquisar, descobri que o [Polyglot](https://github.com/untra/polyglot) é amplamente usado para implementação de sites multilíngues e pode atender à maioria dos requisitos acima, então adotei esse plugin.

### Instalação do plugin
Como estou usando o Bundler, adicionei o seguinte conteúdo ao `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Em seguida, executar `bundle update` no terminal completa a instalação automaticamente.

Se você não estiver usando o Bundler, também pode instalar a gem diretamente com o comando `gem install jekyll-polyglot` no terminal e então adicionar o plugin ao `_config.yml` da seguinte forma:

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
- lang_from_path: Valor booleano, se definido como 'true', reconhece e usa automaticamente o código de idioma se a string do caminho do arquivo markdown incluir o código de idioma, mesmo que a propriedade 'lang' não seja especificada explicitamente no YAML front matter dentro do arquivo markdown do post

> O [documento oficial do protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) afirma o seguinte:
>
>> "A localização de um arquivo Sitemap determina o conjunto de URLs que podem ser incluídos nesse Sitemap. Um arquivo Sitemap localizado em http://example.com/catalog/sitemap.xml pode incluir quaisquer URLs começando com http://example.com/catalog/ mas não pode incluir URLs começando com http://example.com/images/."
>
>> "É fortemente recomendado que você coloque seu Sitemap no diretório raiz do seu servidor web."
>
> Para cumprir isso, deve-se adicionar 'sitemap.xml' à lista 'exclude_from_localization' para garantir que apenas um arquivo `sitemap.xml` com o mesmo conteúdo exista no diretório raiz, e não seja criado para cada idioma, evitando o exemplo incorreto abaixo.
>
> Exemplo incorreto (o conteúdo de cada arquivo é o mesmo para todos os idiomas):
> - https://www.yunseo.kim/sitemap.xml
> - https://www.yunseo.kim/ko/sitemap.xml
> - https://www.yunseo.kim/es/sitemap.xml
> - https://www.yunseo.kim/pt-BR/sitemap.xml
> - https://www.yunseo.kim/ja/sitemap.xml
> - https://www.yunseo.kim/fr/sitemap.xml
> - https://www.yunseo.kim/de/sitemap.xml
{: .prompt-tip }

> Definir 'parallel_localization' como 'true' tem a vantagem de reduzir significativamente o tempo de compilação, mas em julho de 2024, quando essa funcionalidade foi ativada para este blog, havia um bug onde os links de título nas seções 'Recently Updated' e 'Trending Tags' na barra lateral direita da página não eram processados corretamente e se misturavam com outros idiomas. Parece que ainda não está totalmente estabilizado, então é necessário testar previamente se funciona normalmente antes de aplicar ao site. Além disso, [a funcionalidade também não é suportada ao usar Windows, então deve ser desativada](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Além disso, [no Jekyll 4.0, é necessário desativar a geração de sourcemaps CSS da seguinte forma](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # No Jekyll 4.0, os mapas de origem SCSS serão gerados incorretamente devido à forma como o Polyglot opera
```
{: file='_config.yml'}

### Pontos a considerar ao escrever posts
Ao escrever posts multilíngues, deve-se considerar o seguinte:
- Especificação apropriada do código de idioma: Deve-se especificar o código de idioma ISO apropriado usando o caminho do arquivo (ex. `/_posts/ko/example-post.md`{: .filepath}) ou a propriedade 'lang' no YAML front matter (ex. `lang: ko`). Consulte os exemplos na [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> No entanto, embora a [documentação do desenvolvedor do Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) use o formato 'pt_BR' para códigos regionais, na prática deve-se usar 'pt-BR' com - em vez de _ para que funcione corretamente ao adicionar tags alternativas hreflang ao cabeçalho HTML posteriormente.

- O caminho e o nome do arquivo devem ser consistentes.

Para mais detalhes, consulte o [README do repositório GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Solução de problemas ('relative_url_regex': target of repeat operator is not specified)
Após concluir as etapas anteriores, ao executar o comando `bundle exec jekyll serve` para testar a compilação, ocorreu um erro dizendo `'relative_url_regex': target of repeat operator is not specified` e a compilação falhou.

```shell
...(omitido)
                    ------------------------------------------------
      Jekyll 4.3.4   Please append `--trace` to the `serve` command 
                     for any additional information or backtrace. 
                    ------------------------------------------------
/Users/yunseo/.gem/ruby/3.2.2/gems/jekyll-polyglot-1.8.1/lib/jekyll/polyglot/
patches/jekyll/site.rb:234:in `relative_url_regex': target of repeat operator 
is not specified: /href="?\/((?:(?!*.gem)(?!*.gemspec)(?!tools)(?!README.md)(
?!LICENSE)(?!*.config.js)(?!rollup.config.js)(?!package*.json)(?!.sass-cache)
(?!.jekyll-cache)(?!gemfiles)(?!Gemfile)(?!Gemfile.lock)(?!node_modules)(?!ve
ndor\/bundle\/)(?!vendor\/cache\/)(?!vendor\/gems\/)(?!vendor\/ruby\/)(?!en\/
)(?!ko\/)(?!es\/)(?!pt-BR\/)(?!ja\/)(?!fr\/)(?!de\/)[^,'"\s\/?.]+\.?)*(?:\/[^
\]\[)("'\s]*)?)"/ (RegexpError)

...(omitido)
```

Após pesquisar se um problema semelhante havia sido relatado, encontrei [exatamente o mesmo problema](https://github.com/untra/polyglot/issues/204) já registrado no repositório do Polyglot, e também havia uma solução.

O arquivo `_config.yml` do [tema Chirpy aplicado a este blog](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml) contém a seguinte sintaxe:

```yml
exclude:
  - "*.gem"
  - "*.gemspec"
  - docs
  - tools
  - README.md
  - LICENSE
  - "*.config.js"
  - package*.json
```
{: file='_config.yml'}

A causa do problema está nas expressões regulares das duas funções incluídas no arquivo [`site.rb` do Polyglot](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb) que não processam corretamente padrões de globbing contendo curingas como `"*.gem"`, `"*.gemspec"`, `"*.config.js"`.

{% raw %}
```ruby
    # uma regex que corresponde a urls relativas em um documento html
    # corresponde a href="baseurl/foo/bar-baz" href="/foo/bar-baz" e outros semelhantes
    # evita corresponder a arquivos excluídos. prepare garante
    # que todos os diretórios @exclude tenham uma barra no final.
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    # uma regex que corresponde a urls absolutas em um documento html
    # corresponde a href="http://baseurl/foo/bar-baz" e outros semelhantes
    # evita corresponder a arquivos excluídos. prepare garante
    # que todos os diretórios @exclude tenham uma barra no final.
    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          regex += "(?!#{x})"
        end
        @languages.each do |x|
          regex += "(?!#{x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(caminho raiz do polyglot)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

Existem duas maneiras de resolver este problema.

### 1. Fazer um fork do Polyglot, modificar a parte problemática e usar
No momento da escrita deste post (novembro de 2024), a [documentação oficial do Jekyll](https://jekyllrb.com/docs/configuration/options/#global-configuration) afirma que a configuração `exclude` suporta o uso de padrões de globbing de nomes de arquivo.

>"Esta opção de configuração suporta padrões de globbing de nomes de arquivo do Ruby File.fnmatch para corresponder a várias entradas a serem excluídas."

Ou seja, a causa do problema não está no tema Chirpy, mas nas duas funções `relative_url_regex()` e `absolute_url_regex()` do Polyglot, então a solução fundamental é modificá-las para que o problema não ocorra.

Como o bug ainda não foi resolvido no Polyglot, você pode fazer um fork do repositório do Polyglot e modificar a parte problemática conforme a seguir, referindo-se a [este post de blog](https://hionpu.com/en/posts/github_blog_4#4-polyglot-dependency-issue) e [a resposta dada ao problema do GitHub mencionado anteriormente](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322), e usar isso em vez do Polyglot original.

{% raw %}
```ruby
    def relative_url_regex(disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{#{start}="?#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end

    def absolute_url_regex(url, disabled = false)
      regex = ''
      unless disabled
        @exclude.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x})"
        end
        @languages.each do |x|
          escaped_x = Regexp.escape(x)
          regex += "(?!#{escaped_x}\/)"
        end
      end
      start = disabled ? 'ferh' : 'href'
      %r{(?<!hreflang="#{@default_lang}" )#{start}="?#{url}#{@baseurl}/((?:#{regex}[^,'"\s/?.]+\.?)*(?:/[^\]\[)("'\s]*)?)"}
    end
```
{: file='(caminho raiz do polyglot)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

### 2. Substituir padrões de globbing por nomes de arquivo exatos no arquivo de configuração `_config.yml` do tema Chirpy
Na verdade, o método ideal e correto seria incorporar o patch acima no mainstream do Polyglot. No entanto, até lá, seria necessário usar a versão bifurcada, o que seria inconveniente para acompanhar e refletir as atualizações do upstream do Polyglot cada vez que ele for atualizado, então eu usei um método diferente.

Se você verificar os arquivos localizados no caminho raiz do projeto no [repositório do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) que correspondem aos padrões `"*.gem"`, `"*.gemspec"`, `"*.config.js"`, há apenas 3 deles:
- `jekyll-theme-chirpy.gemspec`
- `purgecss.config.js`
- `rollup.config.js`

Portanto, se você remover os padrões de globbing da cláusula `exclude` no arquivo `_config.yml` e substituí-los como abaixo, o Polyglot poderá processá-los sem problemas.

```yml
exclude: # Modificado referindo-se ao problema https://github.com/untra/polyglot/issues/204.
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```

## Modificação do cabeçalho HTML e sitemap
Agora, para SEO, é necessário inserir meta tags Content-Language e tags alternativas hreflang no cabeçalho HTML de cada página do blog.

### Cabeçalho HTML
Na versão 1.8.1, a mais recente em novembro de 2024, o Polyglot tem uma funcionalidade que realiza automaticamente o trabalho acima quando a tag Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} é chamada na parte do cabeçalho da página.
No entanto, isso assume que a tag de atributo 'permalink' foi especificada explicitamente naquela página, e não funcionará corretamente se não for o caso.

Portanto, eu peguei o [head.html do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) e adicionei diretamente o seguinte conteúdo.
Eu me referi à [página SEO Recipes do blog oficial do Polyglot](https://polyglot.untra.io/seo/) para o trabalho, mas modifiquei para usar o atributo `page.url` em vez de `page.permalink` quando `page.permalink` não está presente.
Além disso, referindo-me à [documentação oficial do Google Search Central](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault), especifiquei `x-default` em vez de `site.default_lang` como o valor do atributo hreflang para a página do idioma padrão do site, para que o link da página seja reconhecido como fallback quando o idioma preferido do visitante não está na lista de idiomas suportados pelo site ou quando o idioma preferido do visitante não pode ser reconhecido.

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

Em seguida, adicione as seguintes três linhas à parte da classe "sidebar-bottom" no [_includes/sidebar.html do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) para que o Jekyll carregue o conteúdo do `_includes/lang-selector.html` criado anteriormente ao construir a página:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Problema de não indexar corretamente páginas multilíngues ao usar a funcionalidade de pesquisa
Quando as etapas anteriores foram concluídas, quase todas as funcionalidades do site funcionavam satisfatoriamente como pretendido. No entanto, descobri tardiamente que havia um problema onde a barra de pesquisa localizada no canto superior direito da página com o tema Chirpy aplicado não indexava páginas em idiomas diferentes de `site.default_lang` (inglês no caso deste blog), e ao pesquisar em outros idiomas que não o inglês, ainda exibia páginas em inglês nos resultados da pesquisa.

Isso ocorre porque a biblioteca JavaScript [Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search) utilizada pelo tema Chirpy depende da variável `site.posts` fornecida pelo Jekyll para realizar a indexação, e portanto não reconhece páginas multilíngues construídas usando o Polyglot além do idioma padrão.

A estrutura simples do Simple-Jekyll-Search, que realiza a indexação dependendo apenas das variáveis padrão fornecidas pelo Jekyll com um único template liquid chamado [`search.json`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/assets/js/data/search.json), é uma vantagem, mas neste caso, atua como uma desvantagem crítica e uma limitação, tornando-o inadequado para aplicação neste blog. A menos que o Jekyll suporte nativamente páginas multilíngues e o Polyglot forneça alguma variável alternativa que possa substituir `site.posts`, julgo que o Simple-Jekyll-Search não poderá realizar adequadamente a indexação de páginas multilíngues exigida por este blog. Portanto, é necessário explorar e aplicar uma alternativa que possa substituir o Simple-Jekyll-Search, o que deixarei como uma tarefa subsequente e um tópico para um post futuro.
