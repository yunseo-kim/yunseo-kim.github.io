---
title: Cómo implementar soporte multilingüe en un blog Jekyll con Polyglot (1) - Aplicación del plugin Polyglot e implementación de etiquetas hreflang alt, sitemap y botón de selección de idioma
description: 'Se presenta el proceso de implementación de soporte multilingüe utilizando el plugin Polyglot en un blog Jekyll basado en "jekyll-theme-chirpy". Este post es el primero de la serie y cubre la aplicación del plugin Polyglot y la modificación del encabezado html y el sitemap.'
categories: [AI & Data, Blogging]
tags: [Jekyll, Polyglot, Markdown]
image: /assets/img/technology.jpg
---

## Resumen
Hace unos 4 meses, a principios de julio del año 12024 del [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), implementé soporte multilingüe en este blog basado en Jekyll y alojado a través de Github Pages aplicando el plugin [Polyglot](https://github.com/untra/polyglot).
Esta serie comparte los errores encontrados durante el proceso de aplicar el plugin Polyglot al tema Chirpy, cómo se resolvieron, y cómo escribir el encabezado html y sitemap.xml considerando el SEO.
La serie consta de 2 posts, y este que estás leyendo es el primero de ellos.
- Parte 1: Aplicación del plugin Polyglot e implementación de etiquetas hreflang alt, sitemap y botón de selección de idioma (este post)
- Parte 2: [Solución de problemas de fallo de compilación del tema Chirpy y errores en la función de búsqueda](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requisitos
- [x] Debe ser posible proporcionar el resultado de la compilación (páginas web) separado por rutas de idioma (ej. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar el tiempo y esfuerzo adicional requerido para el soporte multilingüe, debe ser posible reconocer automáticamente el idioma según la ruta local donde se encuentra el archivo markdown original (ej. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante la compilación, sin tener que especificar manualmente las etiquetas 'lang' y 'permalink' en el YAML front matter de cada archivo markdown escrito.
- [x] El encabezado de cada página del sitio debe incluir las etiquetas meta Content-Language y hreflang alternativas apropiadas para cumplir con las pautas de SEO para la búsqueda multilingüe de Google.
- [x] Debe ser posible proporcionar enlaces a todas las páginas que soportan cada idioma en el sitio sin omisiones en `sitemap.xml`{: .filepath}, y el propio `sitemap.xml`{: .filepath} debe existir solo uno en la ruta raíz sin duplicados.
- [x] Todas las funciones proporcionadas por el [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) deben funcionar normalmente en las páginas de cada idioma, y si no es así, deben modificarse para que funcionen correctamente.
  - [x] Funcionamiento normal de 'Recently Updated', 'Trending Tags'
  - [x] No deben ocurrir errores durante el proceso de compilación utilizando GitHub Actions
  - [x] Funcionamiento normal de la función de búsqueda de posts en la esquina superior derecha del blog

## Aplicación del plugin Polyglot
Como Jekyll no soporta blogs multilingües de forma nativa, se debe utilizar un plugin externo para implementar un blog multilingüe que cumpla con los requisitos anteriores. Después de investigar, encontré que [Polyglot](https://github.com/untra/polyglot) se usa ampliamente para implementar sitios web multilingües y puede satisfacer la mayoría de los requisitos anteriores, así que adopté este plugin.

### Instalación del plugin
Como estoy usando Bundler, agregué lo siguiente al `Gemfile`:

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Luego, ejecutar `bundle update` en la terminal completará automáticamente la instalación.

Si no estás usando Bundler, también puedes instalar la gema directamente con el comando `gem install jekyll-polyglot` en la terminal y luego agregar el plugin a `_config.yml`{: .filepath} de la siguiente manera:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuración
A continuación, abre el archivo `_config.yml`{: .filepath} y agrega lo siguiente:

```yml
# Polyglot Settings
languages: ["en", "ko", "ja", "zh-TW", "es", "pt-BR", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Lista de idiomas que deseas soportar
- default_lang: Idioma predeterminado de fallback
- exclude_from_localization: Especifica expresiones regulares de cadenas de ruta de archivos/carpetas raíz a excluir de la localización
- parallel_localization: Valor booleano que especifica si paralelizar el procesamiento multilingüe durante la compilación
- lang_from_path: Valor booleano, si se establece en 'true', reconocerá y usará automáticamente el código de idioma incluido en la cadena de ruta del archivo markdown si no se especifica explícitamente el atributo 'lang' en el YAML front matter dentro del archivo markdown

> La [documentación oficial del protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) establece lo siguiente:
>
>> "La ubicación de un archivo Sitemap determina el conjunto de URLs que se pueden incluir en ese Sitemap. Un archivo Sitemap ubicado en http://example.com/catalog/sitemap.xml puede incluir cualquier URL que comience con http://example.com/catalog/ pero no puede incluir URLs que comiencen con http://example.com/images/."
>
>> "Se recomienda encarecidamente que coloque su Sitemap en el directorio raíz de su servidor web."
>
> Para cumplir con esto, se debe agregar 'sitemap' a la lista 'exclude_from_localization' para asegurar que solo exista un único archivo `sitemap.xml`{: .filepath} en el directorio raíz con el mismo contenido, y evitar que se cree como en el siguiente ejemplo incorrecto.
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
> (Actualización 14.01.12025) Tras la aceptación de [una Pull Request que presenté para complementar el contenido mencionado anteriormente en el README](https://github.com/untra/polyglot/pull/230), ahora se puede encontrar la misma guía en la [documentación oficial de Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#sitemap-generation).
{: .prompt-tip }

> Establecer 'parallel_localization' en 'true' tiene la ventaja de reducir significativamente el tiempo de compilación, pero a julio de 12024, cuando activé esta función para este blog, había un error donde los títulos de los enlaces en las secciones 'Recently Updated' y 'Trending Tags' de la barra lateral derecha de la página no se procesaban correctamente y se mezclaban con otros idiomas. Parece que aún no está completamente estabilizado, así que si planeas aplicarlo a tu sitio, es necesario probarlo previamente para asegurarte de que funcione correctamente. Además, [esta función no es compatible con Windows, por lo que debe desactivarse si se usa Windows](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Además, [en Jekyll 4.0, debes desactivar la generación de sourcemaps CSS de la siguiente manera](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility):

```yml
sass:
  sourcemap: never # En Jekyll 4.0, los mapas de origen SCSS se generarán incorrectamente debido a cómo opera Polyglot
```
{: file='_config.yml'}

### Precauciones al escribir posts
Los puntos a tener en cuenta al escribir posts multilingües son los siguientes:
- Especificación adecuada del código de idioma: Se debe especificar el código de idioma ISO apropiado utilizando la ruta del archivo (ej. `/_posts/ko/example-post.md`{: .filepath}) o el atributo 'lang' en el YAML front matter (ej. `lang: ko`). Consulta los ejemplos en la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Sin embargo, aunque la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) muestra los códigos de región en formato 'pt_BR', en realidad debes usar '-' en lugar de '_', como 'pt-BR', para que funcione correctamente al agregar etiquetas hreflang alternativas al encabezado html más adelante.

- Las rutas y nombres de los archivos deben ser consistentes.

Para más detalles, consulta el [README del repositorio GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modificación del encabezado html y sitemap
Ahora debemos insertar etiquetas meta Content-Language y etiquetas hreflang alternativas en el encabezado html de cada página del blog para SEO.

### Encabezado html
A partir de la versión 1.8.1, la más reciente a noviembre de 12024, Polyglot tiene una función que realiza automáticamente esta tarea cuando se llama a la etiqueta Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} en la sección del encabezado de la página.
Sin embargo, esto asume que se ha especificado explícitamente el atributo 'permalink' en la página, y no funcionará correctamente si no es así.

Por lo tanto, tomé el [head.html del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) y agregué directamente el siguiente contenido.
Me basé en la [página SEO Recipes del blog oficial de Polyglot](https://polyglot.untra.io/seo/), pero lo modifiqué para usar el atributo `page.url` en lugar de `page.permalink` cuando este último no está disponible.

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
Como el sitemap generado automáticamente por Jekyll durante la compilación no soporta correctamente las páginas multilingües, crea un archivo `sitemap.xml`{: .filepath} en el directorio raíz e ingresa el siguiente contenido:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- verificación muy perezosa para ver si la página está en la lista de exclusión - esto significa que las páginas excluidas no estarán en el sitemap en absoluto, escribe excepciones según sea necesario -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- asumiendo que si no hay diseño asignado, entonces no incluir la página en el sitemap, es posible que desees cambiar esto -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- Esto recorre todas las colecciones del sitio, incluyendo posts -->{% endcomment %}
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

## Agregar botón de selección de idioma a la barra lateral
(Actualización 05.02.12025) He mejorado el botón de selección de idioma a un formato de lista desplegable.
Crea el archivo `_includes/lang-selector.html`{: .filepath} e ingresa el siguiente contenido:

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

Además, crea el archivo `assets/css/lang-selector.css`{: .filepath} e ingresa el siguiente contenido:

```css
/**
 * Estilos del selector de idioma
 * 
 * Define los estilos para el desplegable de selección de idioma ubicado en la barra lateral.
 * Soporta el modo oscuro del tema y está optimizado para entornos móviles.
 */

/* Contenedor del selector de idioma */
.lang-selector-wrapper {
    padding: 0.35rem;
    margin: 0.15rem 0;
    text-align: center;
}

/* Contenedor del desplegable */
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

/* Estilos de emojis de banderas */
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

/* Compatibilidad con Firefox */
.lang-select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 var(--sidebar-muted);
}

/* Compatibilidad con IE */
.lang-select::-ms-expand {
    display: none;
}

/* Compatibilidad con modo oscuro */
[data-mode="dark"] .lang-select {
    background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

/* Optimización para entornos móviles */
@media (max-width: 768px) {
    .lang-select {
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Área táctil más grande */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Área de selección más amplia en móviles */
    }
}
```
{: file='assets/css/lang-selector.css'}

Luego, agrega las siguientes tres líneas justo antes de la clase "sidebar-bottom" en el [`_includes/sidebar.html`{: .filepath} del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) para que Jekyll cargue el contenido de `_includes/lang-selector.html`{: .filepath} que escribimos anteriormente durante la compilación de la página:

{% raw %}
```liquid
  (estrategia previa)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(estrategia posterior)
```
{: file='_includes/sidebar.html'}
{% endraw %}

## Lectura adicional
Continúa en la [Parte 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
