---
title: Cómo implementar soporte multilingüe en un blog Jekyll con Polyglot (1) - Aplicación del plugin Polyglot e implementación de etiquetas alt hreflang, sitemap y botón de selección de idioma
description: 'Presenta el proceso de implementación de soporte multilingüe aplicando el plugin Polyglot a un blog Jekyll basado en ''jekyll-theme-chirpy''. Este post es el primero de la serie, cubriendo la aplicación del plugin Polyglot y la modificación del header HTML y sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot/
---
## Introducción
Hace aproximadamente 4 meses, a principios de julio de 12024, implementé soporte multilingüe en este blog basado en Jekyll y alojado en GitHub Pages aplicando el plugin [Polyglot](https://github.com/untra/polyglot).
Esta serie comparte los bugs encontrados durante el proceso de aplicación del plugin Polyglot al tema Chirpy y su proceso de resolución, así como métodos para escribir headers HTML y sitemap.xml considerando SEO.
La serie consta de 2 artículos, y este artículo que estás leyendo es el primero de la serie.
- Parte 1: Aplicación del plugin Polyglot e implementación de etiquetas alt hreflang, sitemap y botón de selección de idioma (este artículo)
- Parte 2: [Solución de problemas de fallo de compilación del tema Chirpy y errores en la función de búsqueda](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requisitos
- [x] Debe poder proporcionar el resultado de la compilación (páginas web) separado por rutas de idioma (ej. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar el tiempo y esfuerzo adicional requerido para el soporte multiidioma, debe poder reconocer automáticamente el idioma según la ruta local donde se encuentra el archivo (ej. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante la compilación, sin necesidad de especificar manualmente las etiquetas 'lang' y 'permalink' en el YAML front matter de cada archivo markdown original.
- [x] La sección header de cada página del sitio debe incluir etiquetas meta Content-Language apropiadas, etiquetas alternativas hreflang y enlaces canónicos para cumplir con las directrices SEO de Google para búsquedas multiidioma.
- [x] Debe poder proporcionar enlaces de páginas para cada versión de idioma del sitio sin omisiones en `sitemap.xml`{: .filepath}, y el propio `sitemap.xml`{: .filepath} debe existir solo uno en la ruta raíz sin duplicados.
- [x] Todas las funciones proporcionadas por el [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) deben funcionar normalmente en cada página de idioma, y si no es así, deben ser corregidas para funcionar normalmente.
  - [x] Funcionamiento normal de las funciones 'Recently Updated' y 'Trending Tags'
  - [x] No debe ocurrir errores durante el proceso de compilación usando GitHub Actions
  - [x] Funcionamiento normal de la función de búsqueda de posts en la esquina superior derecha del blog

## Aplicación del plugin Polyglot
Jekyll no soporta blogs multiidioma de forma nativa, por lo que para implementar un blog multiidioma que satisfaga los requisitos anteriores, es necesario utilizar plugins externos. Tras investigar, encontré que [Polyglot](https://github.com/untra/polyglot) se usa ampliamente para implementar sitios web multiidioma y puede satisfacer la mayoría de los requisitos anteriores, por lo que adopté este plugin.

### Instalación del plugin
Como estoy usando Bundler, agregué el siguiente contenido al `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Después, ejecutando `bundle update` en la terminal se completa la instalación automáticamente.

Si no usas Bundler, puedes instalar la gem directamente con el comando `gem install jekyll-polyglot` en la terminal y luego agregar el plugin al `_config.yml`{: .filepath} de la siguiente manera.

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuración
A continuación, abre el archivo `_config.yml`{: .filepath} y agrega el siguiente contenido.

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap.xml"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Lista de idiomas que se desea soportar
- default_lang: Idioma de respaldo predeterminado
- exclude_from_localization: Especifica expresiones regulares de cadenas de rutas de archivos/carpetas raíz a excluir de la localización de idiomas
- parallel_localization: Valor booleano que especifica si paralelizar el procesamiento multiidioma durante la compilación
- lang_from_path: Valor booleano, cuando se establece en 'true', reconoce y usa automáticamente el código de idioma si la cadena de ruta del archivo markdown contiene un código de idioma, incluso sin especificar por separado el atributo 'lang' como YAML front matter dentro del archivo markdown del post

> El [documento oficial del protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) establece lo siguiente:
>
>> "The location of a Sitemap file determines the set of URLs that can be included in that Sitemap. A Sitemap file located at http://example.com/catalog/sitemap.xml can include any URLs starting with http://example.com/catalog/ but can not include URLs starting with http://example.com/images/."
>
>> "It is strongly recommended that you place your Sitemap at the root directory of your web server."
>
> Para cumplir con esto, se debe agregar a la lista 'exclude_from_localization' para que no se creen archivos `sitemap.xml`{: .filepath} con el mismo contenido por idioma, sino que exista solo uno en el directorio raíz, evitando el siguiente ejemplo incorrecto.
>
> Ejemplo incorrecto (el contenido de cada archivo es idéntico, no diferente por idioma):
> - `/sitemap.xml`{: .filepath}
> - `/ko/sitemap.xml`{: .filepath}
> - `/es/sitemap.xml`{: .filepath}
> - `/pt-BR/sitemap.xml`{: .filepath}
> - `/ja/sitemap.xml`{: .filepath}
> - `/fr/sitemap.xml`{: .filepath}
> - `/de/sitemap.xml`{: .filepath}
>
> (Actualización del 12025.01.14.) Como el [Pull Request que envié para reforzar el contenido mencionado anteriormente en el README](https://github.com/untra/polyglot/pull/230) fue aceptado, ahora se puede confirmar la misma guía en la [documentación oficial de Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Aunque especificar 'parallel_localization' como 'true' tiene la ventaja de reducir considerablemente el tiempo de compilación, a partir de julio de 12024, cuando activé esta función para este blog, había un bug donde los títulos de enlaces en las secciones 'Recently Updated' y 'Trending Tags' de la barra lateral derecha no se procesaban normalmente y se mezclaban con otros idiomas. Parece que aún no está suficientemente estabilizado, por lo que es necesario probar si funciona normalmente antes de aplicarlo al sitio. Además, [si usas Windows, esta función tampoco es compatible, por lo que debe desactivarse](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

También, [en Jekyll 4.0, se debe desactivar la generación de sourcemaps CSS de la siguiente manera](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # In Jekyll 4.0 , SCSS source maps will generate improperly due to how Polyglot operates
```
{: file='_config.yml'}

### Consideraciones al escribir posts
Los puntos a considerar al escribir posts multiidioma son los siguientes:
- Especificación apropiada del código de idioma: Se debe especificar el código de idioma ISO apropiado usando la ruta del archivo (ej. `/_posts/ko/example-post.md`{: .filepath}) o el atributo 'lang' del YAML front matter (ej. `lang: ko`). Consulta los ejemplos en la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Sin embargo, aunque la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) muestra códigos de región en formato 'pt_BR', en realidad se debe usar - en lugar de _ como 'pt-BR' para que funcione normalmente al agregar etiquetas alternativas hreflang al header HTML posteriormente.
{: .prompt-tip }

- Las rutas y nombres de archivos deben ser consistentes.

Para más detalles, consulta el [README del repositorio untra/polyglot en GitHub](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modificación del header HTML y sitemap
Ahora necesitamos insertar etiquetas meta Content-Language y etiquetas alternativas hreflang en el header HTML de cada página del blog para SEO, y especificar apropiadamente la URL canónica.

### Header HTML
Basado en la versión 1.8.1, que es la más reciente a partir de 12024.11., Polyglot tiene una función que realiza automáticamente el trabajo anterior cuando se llama la etiqueta Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} en la sección header de la página.
Sin embargo, esto asume que se ha especificado el atributo 'permalink' en esa página, y no funciona normalmente si no es así.

Por lo tanto, tomé el [head.html del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) y agregué directamente el contenido como se muestra a continuación.
Trabajé consultando la [página SEO Recipes del blog oficial de Polyglot](https://polyglot.untra.io/seo/), pero modifiqué para usar el atributo `page.url` en lugar de `page.permalink` para adaptarse a mi entorno de uso y requisitos.

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

(Agregado el 12025.07.29.) Además, el tema Chirpy incluye por defecto el plugin [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag), y confirmé que los metadatos [Open Graph](https://ogp.me/) `og:locale`, `og:url` generados automáticamente por Jekyll SEO Tag y la [URL canónica](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) (elemento `link` con `rel="canonical"`) están basados en el idioma predeterminado del sitio (`site.lang`, `site.default_lang`), por lo que se necesita procesamiento adicional.  
Por lo tanto, agregué la siguiente declaración antes de {% raw %}`{{ seo_tags }}`{% endraw %}.

{% raw %}
```liquid
(anterior)...

  {% capture seo_tags -%}
    {% seo title=false %}
  {%- endcapture %}

  ...(medio)...

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

  ...(posterior)
```
{: file='/_includes/head.html'}
{% endraw %}

> Según la [documentación para desarrolladores de Google](https://developers.google.com/search/docs/crawling-indexing/canonicalization), cuando una página tiene múltiples versiones de idioma, se considera duplicado solo cuando el idioma del contenido principal es el mismo, es decir, cuando solo se han traducido encabezados, pies de página y otros textos no importantes, pero el cuerpo principal es idéntico. Por lo tanto, en casos como este blog donde se proporciona texto del cuerpo principal en múltiples idiomas, todas las versiones de idioma se consideran páginas independientes, no duplicados, por lo que se debe especificar una URL canónica diferente según el idioma.  
> Por ejemplo, para la versión en coreano de esta página, la URL canónica no es "{{site.url}}{{page.url}}" sino "{{site.url}}/ko{{page.url}}".
{: .prompt-tip }

### Sitemap
Como el sitemap generado automáticamente por Jekyll durante la compilación no soporta normalmente páginas multiidioma si no se especifica una plantilla por separado, crea un archivo `sitemap.xml`{: .filepath} en el directorio raíz e ingresa el siguiente contenido.

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

## Agregar botón de selección de idioma a la barra lateral
(Actualización del 12025.02.05.) Mejoré el botón de selección de idioma en formato de lista desplegable.  
Creé el archivo `_includes/lang-selector.html`{: .filepath} e ingresé el siguiente contenido.

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

También creé el archivo `assets/css/lang-selector.css`{: .filepath} e ingresé el siguiente contenido.

```css
/**
 * Estilos del selector de idioma
 * 
 * Define los estilos del dropdown de selección de idioma ubicado en la barra lateral.
 * Soporta el modo oscuro del tema y está optimizado para entornos móviles.
 */

/* Contenedor del selector de idioma */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Contenedor del dropdown */
.lang-dropdown {
    position: relative;
    display: inline-block;
    width: auto;
    min-width: 120px;
    max-width: 80%;
}

/* Elemento de entrada de selección */
.lang-select {
    /* Estilos básicos */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 100%;
    padding: 0.5rem 2rem 0.5rem 1rem;
    
    /* Fuente y color */
    font-family: Lato, "Pretendard JP Variable", "Pretendard Variable", sans-serif;
    font-size: 0.95rem;
    color: var(--sidebar-muted);
    background-color: var(--sidebar-bg);
    
    /* Forma e interacción */
    border-radius: var(--bs-border-radius, 0.375rem);
    cursor: pointer;
    transition: all 0.2s ease;
    
    /* Agregar icono de flecha */
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: right 0.75rem center;
    background-size: 1rem;
}

/* Estilos de emoji de bandera */
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

/* Compatibilidad con navegador Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Compatibilidad con navegador IE */
.lang-select::-ms-expand {
    display: none;
}

/* Compatibilidad con modo oscuro */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Optimización para entorno móvil */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Área táctil más grande */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Área de selección más amplia en móvil */
    }
}
```
{: file='assets/css/lang-selector.css'}

Luego, en el [`_includes/sidebar.html`{: .filepath} del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html), agregué las siguientes tres líneas justo antes de la clase "sidebar-bottom" para que Jekyll cargue el contenido del `_includes/lang-selector.html`{: .filepath} que escribí anteriormente durante la compilación de la página.

{% raw %}
```liquid
  (anterior)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(posterior)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Lectura adicional
Continúa en la [Parte 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
