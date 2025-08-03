---
title: "Como implementar suporte multilíngue em blog Jekyll com Polyglot (2) - Implementação do botão de seleção de idioma & localização do idioma do layout"
description: "Apresenta o processo de implementação de suporte multilíngue aplicando o plugin Polyglot em um blog Jekyll baseado no tema 'jekyll-theme-chirpy'. Este post é o primeiro da série, abordando a aplicação do plugin Polyglot e a modificação do cabeçalho html e sitemap."
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Visão Geral
No início de julho de 12024, implementei suporte multilíngue neste blog hospedado no Github Pages baseado em Jekyll aplicando o plugin [Polyglot](https://github.com/untra/polyglot).
Esta série compartilha os bugs que ocorreram durante o processo de aplicação do plugin Polyglot ao tema Chirpy e seus processos de resolução, além de como escrever cabeçalhos html e sitemap.xml considerando SEO.
A série consiste em 3 posts, e este post que você está lendo é o segundo da série.
- Parte 1: [Aplicação do plugin Polyglot & modificação do cabeçalho html e sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Parte 2: Implementação do botão de seleção de idioma & localização do idioma do layout (este post)
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

## Antes de Começar
Este post é uma continuação da [Parte 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1), então se você ainda não leu, recomendo ler o post anterior primeiro.

## Adicionando Botão de Seleção de Idioma na Barra Lateral
> (Atualização em 05.02.12025) O botão de seleção de idioma foi melhorado para o formato de lista suspensa.
{: .prompt-info }

Criei o arquivo `_includes/lang-selector.html`{: .filepath} e inseri o seguinte conteúdo.

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
{: file='\_includes/lang-selector.html'}
{% endraw %}

Também criei o arquivo `assets/css/lang-selector.css`{: .filepath} e inseri o seguinte conteúdo.

```css
/**
 * Estilos do seletor de idioma
 * 
 * Define os estilos do dropdown de seleção de idioma localizado na barra lateral.
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
    
    /* Adicionar ícone de seta */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Estilos dos emojis de bandeira */
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

/* Estado hover */
.lang-select:hover {
    color: var(--sidebar-active);
    background-color: var(--sidebar-hover);
}

/* Estado focus */
.lang-select:focus {
    outline: 2px solid var(--sidebar-active);
    outline-offset: 2px;
    color: var(--sidebar-active);
}

/* Suporte ao navegador Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Suporte ao navegador IE */
.lang-select::-ms-expand {
    display: none;
}

/* Suporte ao modo escuro */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Otimização para ambiente móvel */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Área de toque maior */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Área de seleção mais ampla no móvel */
    }
}
```
{: file='assets/css/lang-selector.css'}

Em seguida, no [`_includes/sidebar.html`{: .filepath} do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html), adicionei as três linhas da classe `lang-selector-wrapper` logo antes da classe `sidebar-bottom` para que o Jekyll carregue o conteúdo do `_includes/lang-selector.html`{: .filepath} criado anteriormente durante o build da página.

{% raw %}
```liquid
  (전략)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(후략)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (Funcionalidade adicionada em 31.07.12025) Localização do Idioma do Layout
Anteriormente, a localização de idioma era aplicada apenas ao conteúdo principal como títulos de páginas e conteúdo, enquanto o idioma do layout como nomes de abas na barra lateral esquerda e seções superior, inferior e painel direito do site permaneciam fixos em inglês, que é o padrão do site. Pessoalmente, isso era suficiente para mim, então não sentia grande necessidade de trabalho adicional, mas recentemente, durante o trabalho no [patch de propriedades de metadados Open Graph e URL canônica mencionado acima](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#cabeçalho-html), descobri que a localização do idioma do layout era possível de forma muito simples com apenas pequenas modificações. Se fosse necessário um trabalho de modificação de código extenso e complicado, seria diferente, mas como era [um trabalho simples que levou menos de 10 minutos](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb), apliquei adicionalmente.

### Adicionando Locales
Para fornecer simultaneamente várias versões de idioma para cada página do site e alternar entre versões conforme a seleção do usuário, embora não haja essa funcionalidade, [o próprio escopo de idiomas suportado pelo tema Chirpy já é bastante amplo](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales). Portanto, basta selecionar e baixar os arquivos de locale necessários entre os fornecidos pelo tema Chirpy e, se necessário, apenas modificar adequadamente os nomes dos arquivos. O nome do arquivo de locale deve corresponder aos itens na lista `languages` definida no arquivo `_config.yml`{: .filepath} durante a etapa de [configuração](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuração).

> Na verdade, os arquivos no diretório `_data`{: .filepath} são fornecidos por padrão através da [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy) mesmo sem adição direta.
>
> No entanto, no meu caso, era difícil usar os locales fornecidos pelo tema Chirpy como estão devido às seguintes razões, necessitando algumas modificações separadas.
> - O formato dos nomes dos arquivos de locale fornecidos por padrão pelo tema Chirpy inclui códigos de região como `ko-KR`, `ja-JP`, não correspondendo ao formato usado neste site (`ko`, `ja`, etc.)
> - Necessidade de modificar o texto de orientação de licença do padrão [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) para [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) deste blog
> - Os locales de [coreano](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) ou [japonês](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) pareciam um pouco estranhos ou inadequados para este blog na minha perspectiva como coreano, então existem partes que modifiquei pessoalmente
> - Como descrito abaixo, por várias razões não gosto muito da era cristã e adotei o [calendário holoceno](https://en.wikipedia.org/wiki/Holocene_calendar) como formato de data neste blog, então precisei modificar os locales adequadamente
>   - Fundamentalmente tem forte coloração religiosa de uma religião específica e é tendencioso ao Ocidente
>     - Embora não negue que Jesus foi um grande santo e respeite a posição dessa religião, se fosse para usar apenas internamente como a era budista do budismo, não haveria problema algum, mas como não é esse o caso, levanto a questão. Confúcio, Buda, Sócrates e muitos outros santos existiram, então qual é a razão para que não religiosos ou pessoas de outras religiões, e pessoas de outras culturas fora da Europa, tenham que usar um sistema de anos cuja origem é o ano de nascimento de Jesus?
>     - E se perguntarmos se essa 'origem' é realmente o ano de nascimento de Jesus, na verdade não é, e a teoria estabelecida é que ele nasceu alguns anos antes
>   - Como é um sistema de anos concebido antes do surgimento do conceito de '0', o ano seguinte ao ano 1 a.C. (-1) é imediatamente o ano 1 d.C. (1), tornando o cálculo de anos não intuitivo
>   - Trata os 10.000 anos desde a entrada da humanidade na era neolítica e sociedade agrícola até o nascimento de Jesus, ou mesmo os 3.000-4.000 anos desde a invenção da escrita, como 'antes de Cristo', causando distorção cognitiva na história mundial, especialmente na história antiga
> 
> Por isso, aqui adicionei arquivos de locale diretamente no diretório `_data/locales`{: .filepath} e os apliquei após modificações adequadas.  
> Portanto, se isso não se aplica e você deseja aplicar os locales fornecidos por padrão pelo tema Chirpy sem modificações, pode pular esta etapa.
{: .prompt-tip }

### Integração com Polyglot
Agora, modificando apenas os dois arquivos a seguir ligeiramente, é possível integrar suavemente com o Polyglot.

> Se você criou o repositório inicialmente usando o [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended) em vez de fazer fork direto do repositório do tema, os arquivos correspondentes podem não existir no repositório do seu site. Isso ocorre porque são arquivos fornecidos por padrão através da [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy), então nesse caso, primeiro baixe o arquivo original correspondente do [repositório do tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) e coloque-o na mesma posição no seu repositório antes de trabalhar. Quando o Jekyll constrói o site, se já existe um arquivo com o mesmo nome no repositório, ele é aplicado com prioridade sobre o arquivo fornecido pela [gem externa (jekyll-theme-chirpy)](https://rubygems.org/gems/jekyll-theme-chirpy).
{: .prompt-tip }

#### '\_includes/lang.html'
Adicione duas linhas de código no meio do arquivo [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) como mostrado abaixo, para que quando a variável `lang` não for especificada separadamente no YAML front matter da página, a [variável `site.active_lang` do Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#features) seja reconhecida com prioridade sobre o idioma padrão do site definido em `_config.yml`{: .filepath} (`site.lang`) ou inglês (`'en'`). Este arquivo é chamado comumente por todas as páginas do site que aplicam o tema Chirpy ([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) durante o build para declarar a variável `lang`, e usa essa variável `lang` para executar a localização do idioma do layout.

{% raw %}
```diff
@@ -1,10 +1,12 @@
 {% comment %}
   Detect appearance language and return it through variable "lang"
 {% endcomment %}
 {% if site.data.locales[page.lang] %}
   {% assign lang = page.lang %}
+{% elsif site.data.locales[site.active_lang] %}
+  {% assign lang = site.active_lang %}
 {% elsif site.data.locales[site.lang] %}
   {% assign lang = site.lang %}
 {% else %}
   {% assign lang = 'en' %}
 {% endif %}
```
{: file='\_includes/lang.html'}
{% endraw %}

Prioridade na declaração da variável `lang`:
- Antes da modificação:
  1. `page.lang` (quando definido no YAML front matter da página individual)
  2. `site.lang` (quando definido em `_config.yml`{: .filepath})
  3. `'en'`
- Após a modificação:
  1. `page.lang` (quando definido no YAML front matter da página individual)
  2. **`site.active_lang`** (quando Polyglot está sendo aplicado)
  3. `site.lang` (quando definido em `_config.yml`{: .filepath})
  4. `'en'`

#### '\_layouts/default.html'
Da mesma forma, modifique o conteúdo do arquivo [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) para especificar corretamente o atributo `lang` na tag `<html>`, que é o elemento de nível superior do documento HTML.

{% raw %}
```diff
@@ -1,19 +1,19 @@
 ---
 layout: compress
 ---
 
 <!doctype html>
 
 {% include origin-type.html %}
 
 {% include lang.html %}
 
 {% if site.theme_mode %}
   {% capture prefer_mode %}data-mode="{{ site.theme_mode }}"{% endcapture %}
 {% endif %}
 
 <!-- `site.alt_lang` can specify a language different from the UI -->
-<html lang="{{ page.lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
+<html lang="{{ page.lang | default: site.active_lang | default: site.alt_lang | default: site.lang }}" {{ prefer_mode }}>
   {% include head.html %}
```
{: file='\_layouts/default.html'}
{% endraw %}

Prioridade na especificação do atributo `lang` da tag `<html>`:
- Antes da modificação:
  1. `page.lang` (quando definido no YAML front matter da página individual)
  2. `site.alt_lang` (quando definido em `_config.yml`{: .filepath})
  3. `site.lang` (quando definido em `_config.yml`{: .filepath})
  4. `unknown` (string vazia, `lang=""`)
- Após a modificação:
  1. `page.lang` (quando definido no YAML front matter da página individual)
  2. **`site.active_lang`** (quando Polyglot está sendo aplicado)
  3. `site.alt_lang` (quando definido em `_config.yml`{: .filepath})
  4. `site.lang` (quando definido em `_config.yml`{: .filepath})
  5. `unknown` (string vazia, `lang=""`)

> Não especificar o idioma da página web (atributo `lang`) e deixá-lo como `unknown` não é recomendado, e deve ser especificado com um valor apropriado sempre que possível. Como você pode ver, o valor do atributo `lang` em `_config.yml`{: .filepath} é usado como fallback, então seja usando Polyglot ou não, é bom definir esse valor adequadamente, e normalmente já estará definido em casos normais. Se você aplicar Polyglot ou um plugin i18n similar como abordado neste post, seria seguro especificar o mesmo valor que [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuração).
{: .prompt-tip }

## Leitura Adicional
Continuação na [Parte 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
