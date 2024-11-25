---
title: Cómo implementar soporte multilingüe en un blog Jekyll con Polyglot (1) - Aplicación del plugin Polyglot e implementación de etiquetas hreflang alt, sitemap y botón de selección de idioma
description: >-
  Se presenta el proceso de implementación de soporte multilingüe utilizando el plugin Polyglot en un blog Jekyll basado en 'jekyll-theme-chirpy'.
  Este post es el primero de la serie y cubre la aplicación del plugin Polyglot y la modificación del encabezado html y el sitemap.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
---
## Resumen
Hace aproximadamente 4 meses, a principios de julio de 2024, implementé soporte multilingüe en este blog basado en Jekyll y alojado a través de Github Pages aplicando el plugin [Polyglot](https://github.com/untra/polyglot).
Esta serie comparte los errores encontrados durante el proceso de aplicación del plugin Polyglot al tema Chirpy, sus soluciones, y cómo escribir el encabezado html y sitemap.xml considerando el SEO.
La serie consta de 2 posts, y este que estás leyendo es el primero de ellos.
- Parte 1: Aplicación del plugin Polyglot e implementación de etiquetas hreflang alt, sitemap y botón de selección de idioma (este post)
- Parte 2: [Solución de problemas de fallo de compilación del tema Chirpy y errores en la función de búsqueda](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)

## Requisitos
- [x] Debe ser posible proporcionar el resultado de la compilación (páginas web) separado por rutas de idioma (ej. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar el tiempo y esfuerzo adicional requerido para el soporte multilingüe, debe ser posible reconocer automáticamente el idioma según la ruta local donde se encuentra el archivo markdown original (ej. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante la compilación, sin tener que especificar manualmente las etiquetas 'lang' y 'permalink' en el YAML front matter de cada archivo markdown escrito.
- [x] El encabezado de cada página del sitio debe incluir las etiquetas meta Content-Language y hreflang alternativas apropiadas para cumplir con las pautas de SEO para la búsqueda multilingüe de Google.
- [x] Debe ser posible proporcionar enlaces a todas las páginas que soportan cada idioma en el sitio sin omisiones en `sitemap.xml`, y el propio `sitemap.xml` debe existir solo uno en la ruta raíz sin duplicados.
- [x] Todas las funciones proporcionadas por el [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) deben funcionar normalmente en las páginas de cada idioma, y si no es así, deben modificarse para que funcionen correctamente.
  - [x] Funcionamiento normal de las funciones 'Recently Updated' y 'Trending Tags'
  - [x] No deben ocurrir errores durante el proceso de compilación utilizando GitHub Actions
  - [x] Funcionamiento normal de la función de búsqueda de posts en la esquina superior derecha del blog

## Aplicación del plugin Polyglot
Como Jekyll no admite blogs multilingües de forma nativa, se debe utilizar un plugin externo para implementar un blog multilingüe que cumpla con los requisitos anteriores. Después de investigar, encontré que [Polyglot](https://github.com/untra/polyglot) se usa ampliamente para implementar sitios web multilingües y puede satisfacer la mayoría de los requisitos anteriores, por lo que adopté este plugin.

### Instalación del plugin
Como estoy usando Bundler, agregué el siguiente contenido a `Gemfile`.

```ruby
group :jekyll_plugins do
   gem "jekyll-polyglot"
end
```
{: file='Gemfile'}

Luego, ejecutar `bundle update` en la terminal completará automáticamente la instalación.

Si no estás usando Bundler, puedes instalar la gema directamente con el comando `gem install jekyll-polyglot` en la terminal y luego agregar el plugin a `_config.yml` de la siguiente manera:

```yml
plugins:
  - jekyll-polyglot
```
{: file='_config.yml'}

### Configuración
A continuación, abre el archivo `_config.yml` y agrega el siguiente contenido:

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Lista de idiomas que deseas soportar
- default_lang: Idioma predeterminado de fallback
- exclude_from_localization: Especifica expresiones regulares de cadenas de ruta de archivos/carpetas raíz que se excluirán de la localización
- parallel_localization: Valor booleano que especifica si se debe paralelizar el procesamiento multilingüe durante la compilación
- lang_from_path: Valor booleano, si se establece en 'true', reconocerá y utilizará automáticamente el código de idioma si la cadena de ruta del archivo markdown contiene el código de idioma, incluso si no se especifica explícitamente el atributo 'lang' en el YAML front matter dentro del archivo markdown del post

> La [documentación oficial del protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) establece lo siguiente:
>
>> "La ubicación de un archivo Sitemap determina el conjunto de URLs que se pueden incluir en ese Sitemap. Un archivo Sitemap ubicado en http://example.com/catalog/sitemap.xml puede incluir cualquier URL que comience con http://example.com/catalog/ pero no puede incluir URLs que comiencen con http://example.com/images/."
>
>> "Se recomienda encarecidamente que coloque su Sitemap en el directorio raíz de su servidor web."
>
> Para cumplir con esto, debes agregar 'sitemap' a la lista 'exclude_from_localization' para asegurarte de que solo exista un archivo `sitemap.xml` con el mismo contenido en el directorio raíz, y no se creen por idioma como en el siguiente ejemplo incorrecto.
>
> Ejemplo incorrecto (el contenido de cada archivo es idéntico, no diferente por idioma):
> - /sitemap.xml
> - /ko/sitemap.xml
> - /es/sitemap.xml
> - /pt-BR/sitemap.xml
> - /ja/sitemap.xml
> - /fr/sitemap.xml
> - /de/sitemap.xml
{: .prompt-tip }

> Establecer 'parallel_localization' en 'true' tiene la ventaja de reducir significativamente el tiempo de compilación, pero a julio de 2024, cuando se activó esta función para este blog, había un error donde los títulos de los enlaces en las secciones 'Recently Updated' y 'Trending Tags' de la barra lateral derecha de la página no se procesaban correctamente y se mezclaban con otros idiomas. Parece que aún no está completamente estabilizado, así que es necesario probar previamente si funciona correctamente antes de aplicarlo al sitio. Además, [esta función no es compatible con Windows, por lo que debe desactivarse si se usa Windows](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
{: .prompt-warning }

Además, [en Jekyll 4.0, debes desactivar la generación de sourcemaps CSS de la siguiente manera](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).

```yml
sass:
  sourcemap: never # En Jekyll 4.0, los mapas de origen SCSS se generarán incorrectamente debido a cómo opera Polyglot
```
{: file='_config.yml'}

### Consideraciones al escribir posts
Los puntos a tener en cuenta al escribir posts multilingües son los siguientes:
- Especificación del código de idioma apropiado: Se debe especificar el código de idioma ISO apropiado utilizando la ruta del archivo (ej. `/_posts/ko/example-post.md`{: .filepath}) o el atributo 'lang' en el YAML front matter (ej. `lang: ko`). Consulta los ejemplos en la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales).

> Sin embargo, aunque la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) muestra los códigos de región en formato 'pt_BR', en realidad debes usar '-' en lugar de '_', como 'pt-BR', para que funcione correctamente al agregar etiquetas hreflang alternativas al encabezado html más adelante.

- La ruta y el nombre del archivo deben ser consistentes.

Para más detalles, consulta el [README del repositorio GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Modificación del encabezado html y sitemap
Ahora debemos insertar etiquetas meta Content-Language y etiquetas hreflang alternativas en el encabezado html de cada página del blog para SEO.

### Encabezado html
A partir de la versión 1.8.1, la más reciente a noviembre de 2024, Polyglot tiene una función que realiza automáticamente esta tarea cuando se llama a la etiqueta Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} en la sección del encabezado de la página.
Sin embargo, esto asume que se ha especificado el atributo 'permalink' en la página, y no funcionará correctamente si no es así.

Por lo tanto, tomé el [head.html del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) y agregué directamente el siguiente contenido.
Me basé en la [página SEO Recipes del blog oficial de Polyglot](https://polyglot.untra.io/seo/), pero modifiqué para usar el atributo `page.url` en lugar de `page.permalink` si este último no está presente.
Además, siguiendo la [documentación oficial de Google Search Central](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault), especifiqué `x-default` en lugar de `site.default_lang` como valor del atributo hreflang para la página del idioma predeterminado del sitio, para que se reconozca ese enlace de página como fallback cuando el idioma preferido del visitante no esté en la lista de idiomas soportados por el sitio o no se pueda reconocer el idioma preferido del visitante.

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
Como el sitemap generado automáticamente por Jekyll durante la compilación no admite correctamente las páginas multilingües, crea un archivo `sitemap.xml` en el directorio raíz e ingresa el siguiente contenido:

{% raw %}
```liquid
---
layout: content
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{% for lang in site.languages %}

    {% for node in site.pages %}
        {% comment %}<!-- verificación muy perezosa para ver si la página está en la lista de exclusión - esto significa que las páginas excluidas no estarán en el sitemap en absoluto, escriba excepciones según sea necesario -->{% endcomment %}
        {% unless site.exclude_from_localization contains node.path %}
            {% comment %}<!-- asumiendo que si no hay diseño asignado, entonces no incluya la página en el sitemap, es posible que desee cambiar esto -->{% endcomment %}
            {% if node.layout %}
                <url>
                    <loc>{% if lang == site.default_lang %}{{ node.url | absolute_url }}{% else %}{{ node.url | prepend: lang | prepend: '/' | absolute_url }}{% endif %}</loc>
                    {% if node.last_modified_at and node.last_modified_at != node.date %}<lastmod>{{ node.last_modified_at | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% elsif node.date %}<lastmod>{{ node.date | date: '%Y-%m-%dT%H:%M:%S%:z' }}</lastmod>{% endif %}
                </url>
            {% endif %}
        {% endunless %}
    {% endfor %}

    {% comment %}<!-- Esto recorre todas las colecciones del sitio, incluidos los posts -->{% endcomment %}
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
Creé el archivo `_includes/lang-selector.html` e ingresé el siguiente contenido:

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

Luego, agregué las siguientes tres líneas a la sección de clase "sidebar-bottom" en [`_includes/sidebar.html` del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) para que Jekyll cargue el contenido de `_includes/lang-selector.html` durante la compilación de la página:

{% raw %}
```liquid
    <div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Lectura adicional
Continúa en la [Parte 2](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-2)
