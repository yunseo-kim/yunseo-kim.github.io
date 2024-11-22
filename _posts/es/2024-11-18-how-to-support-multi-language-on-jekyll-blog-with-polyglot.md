---
title: Cómo implementar soporte multilingüe en un blog Jekyll con Polyglot
description: >-
  Se presenta el proceso de implementación de soporte multilingüe utilizando el plugin Polyglot en un blog Jekyll basado en 'jekyll-theme-chirpy'.
categories:
- Blogging
tags:
- Jekyll
- Polyglot
- RegExp
---
## Introducción
Hace aproximadamente 4 meses, a principios de julio de 2024, implementé el soporte multilingüe en este blog basado en Jekyll y alojado a través de Github Pages aplicando el plugin [Polyglot](https://github.com/untra/polyglot).
En este artículo, compartiré los errores que surgieron durante el proceso de aplicación del plugin Polyglot, cómo los resolví, y cómo escribir el encabezado html y sitemap.xml considerando el SEO.

## Requisitos
- [x] Debe ser posible proporcionar el resultado de la compilación (páginas web) separado por rutas de idioma (ej. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar el tiempo y esfuerzo adicionales requeridos para el soporte multilingüe, debe ser posible reconocer automáticamente el idioma según la ruta local donde se encuentra el archivo (ej. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante la compilación, sin tener que especificar manualmente las etiquetas 'lang' y 'permalink' en el YAML front matter del archivo markdown original.
- [x] El encabezado de cada página del sitio debe incluir las etiquetas meta Content-Language y hreflang alternativas apropiadas para cumplir con las pautas de SEO para la búsqueda multilingüe de Google.
- [x] Debe ser posible proporcionar enlaces a todas las páginas que admiten cada idioma en el sitio sin omisiones en `sitemap.xml`, y el propio `sitemap.xml` debe existir solo uno en la ruta raíz sin duplicados.
- [ ] Todas las funciones proporcionadas por el [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) deben funcionar normalmente en cada página de idioma, y si no es así, deben modificarse para que funcionen correctamente.

## Aplicación del plugin Polyglot
Como Jekyll no admite blogs multilingües de forma nativa, se debe utilizar un plugin externo para implementar un blog multilingüe que cumpla con los requisitos anteriores. Después de buscar, encontré que [Polyglot](https://github.com/untra/polyglot) se usa ampliamente para implementar sitios web multilingües y puede satisfacer la mayoría de los requisitos anteriores, por lo que adopté este plugin.

### Instalación del plugin
Como estoy usando Bundler, agregué lo siguiente a mi `Gemfile`:

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
A continuación, abre el archivo `_config.yml` y agrega lo siguiente:

```yml
# Polyglot Settings
languages: ["en", "ko", "es", "pt-BR", "ja", "fr", "de"]
default_lang: "en"
exclude_from_localization: ["javascript", "images", "css", "public", "assets", "sitemap"]
parallel_localization: false
lang_from_path: true
```
{: file='_config.yml'}

- languages: Lista de idiomas que deseas admitir
- default_lang: Idioma predeterminado de fallback
- exclude_from_localization: Especifica expresiones regulares de cadenas de ruta de archivos/carpetas raíz para excluir de la localización
- parallel_localization: Valor booleano que especifica si paralelizar el procesamiento multilingüe durante la compilación
- lang_from_path: Valor booleano, si se establece en 'true', reconocerá y utilizará automáticamente el código de idioma si la cadena de ruta del archivo markdown contiene el código de idioma, incluso si no se especifica explícitamente el atributo 'lang' en el YAML front matter dentro del archivo markdown del post

> La [documentación oficial del protocolo Sitemap](https://www.sitemaps.org/protocol.html#location) establece lo siguiente:
>
>> "La ubicación de un archivo Sitemap determina el conjunto de URL que se pueden incluir en ese Sitemap. Un archivo Sitemap ubicado en http://example.com/catalog/sitemap.xml puede incluir cualquier URL que comience con http://example.com/catalog/ pero no puede incluir URL que comiencen con http://example.com/images/."
>
>> "Se recomienda encarecidamente que coloque su Sitemap en el directorio raíz de su servidor web."
>
> Para cumplir con esto, debes agregar 'sitemap.xml' a la lista 'exclude_from_localization' para asegurarte de que solo exista un archivo `sitemap.xml` con el mismo contenido en el directorio raíz y no se creen por idioma, evitando el siguiente ejemplo incorrecto.
>
> Ejemplo incorrecto (el contenido de cada archivo es idéntico, no diferente por idioma):
> - https://www.yunseo.kim/sitemap.xml
> - https://www.yunseo.kim/ko/sitemap.xml
> - https://www.yunseo.kim/es/sitemap.xml
> - https://www.yunseo.kim/pt-BR/sitemap.xml
> - https://www.yunseo.kim/ja/sitemap.xml
> - https://www.yunseo.kim/fr/sitemap.xml
> - https://www.yunseo.kim/de/sitemap.xml
{: .prompt-tip }

> Establecer 'parallel_localization' en 'true' puede reducir significativamente el tiempo de compilación, pero a partir de julio de 2024, cuando activé esta función para este blog, había un error donde los títulos de los enlaces en las secciones 'Recently Updated' y 'Trending Tags' de la barra lateral derecha de la página no se procesaban correctamente y se mezclaban con otros idiomas. Parece que aún no está completamente estabilizado, así que es necesario probar si funciona correctamente antes de aplicarlo al sitio. Además, [esta función no es compatible cuando se usa Windows, por lo que debe desactivarse](https://github.com/untra/polyglot?tab=readme-ov-file#compatibility).
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

> Sin embargo, aunque la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/extensions/reference/api/i18n#locales) muestra los códigos de región en el formato 'pt_BR', en realidad debes usar '-' en lugar de '_', como 'pt-BR', para que funcione correctamente al agregar etiquetas alternativas hreflang al encabezado html más adelante.

- La ruta y el nombre del archivo deben ser consistentes.

Para más detalles, consulta el [README del repositorio GitHub untra/polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#how-to-use-it).

## Solución de problemas ('relative_url_regex': target of repeat operator is not specified)
Después de completar los pasos anteriores, ejecuté el comando `bundle exec jekyll serve` para probar la compilación, pero falló con el error `'relative_url_regex': target of repeat operator is not specified`.

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

Después de buscar si se había informado de un problema similar, encontré que [exactamente el mismo problema](https://github.com/untra/polyglot/issues/204) ya estaba registrado en el repositorio de Polyglot y también existía una solución.

El archivo `_config.yml` del [tema Chirpy que estoy aplicando a este blog](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_config.yml) contiene la siguiente cláusula:

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

La causa del problema está en que las expresiones regulares en las dos funciones siguientes incluidas en el archivo [`site.rb` de Polyglot](https://github.com/untra/polyglot/blob/master/lib/jekyll/polyglot/patches/jekyll/site.rb) no pueden procesar correctamente los patrones de globbing que incluyen comodines como `"*.gem"`, `"*.gemspec"`, `"*.config.js"`.

{% raw %}
```ruby
    # una expresión regular que coincide con urls relativas en un documento html
    # coincide con href="baseurl/foo/bar-baz" href="/foo/bar-baz" y otros similares
    # evita coincidir con archivos excluidos. prepare se asegura
    # de que todos los directorios @exclude tengan una barra diagonal al final.
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

    # una expresión regular que coincide con urls absolutas en un documento html
    # coincide con href="http://baseurl/foo/bar-baz" y otros similares
    # evita coincidir con archivos excluidos. prepare se asegura
    # de que todos los directorios @exclude tengan una barra diagonal al final.
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
{: file='(ruta raíz de polyglot)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

Hay dos formas de resolver este problema.

### 1. Hacer un fork de Polyglot, modificar la parte problemática y usarlo
En el momento de escribir este artículo (noviembre de 2024), la [documentación oficial de Jekyll](https://jekyllrb.com/docs/configuration/options/#global-configuration) establece que la configuración `exclude` admite el uso de patrones de globbing de nombres de archivo.

>"Esta opción de configuración admite los patrones de globbing de nombres de archivo de Ruby's File.fnmatch para hacer coincidir múltiples entradas a excluir."

Es decir, la causa del problema no está en el tema Chirpy, sino en las dos funciones `relative_url_regex()` y `absolute_url_regex()` de Polyglot, por lo que modificarlas para que no causen problemas es la solución fundamental.

Como este error aún no se ha resuelto en Polyglot, puedes hacer un fork del repositorio de Polyglot y modificar la parte problemática como se muestra a continuación, refiriéndote a [esta publicación de blog](https://hionpu.com/en/posts/github_blog_4#4-polyglot-dependency-issue) y [la respuesta al problema de GitHub mencionado anteriormente](https://github.com/untra/polyglot/issues/204#issuecomment-2143270322), y luego usar esto en lugar del Polyglot original.

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
{: file='(ruta raíz de polyglot)/lib/jekyll/polyglot/patches/jekyll/site.rb'}
{% endraw %}

### 2. Reemplazar los patrones de globbing en el archivo de configuración `_config.yml` del tema Chirpy con nombres de archivo exactos
En realidad, el método ideal y correcto sería que el parche anterior se incorporara al flujo principal de Polyglot. Sin embargo, hasta entonces, se debe usar la versión bifurcada en su lugar, pero en este caso, puede ser engorroso seguir y reflejar las actualizaciones cada vez que la versión upstream de Polyglot se actualice, así que usé un método diferente.

Si revisas los archivos en la ruta raíz del proyecto en el [repositorio del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) que corresponden a los patrones `"*.gem"`, `"*.gemspec"`, `"*.config.js"`, de todos modos solo hay estos 3:
- `jekyll-theme-chirpy.gemspec`
- `purgecss.config.js`
- `rollup.config.js`

Por lo tanto, si eliminas los patrones de globbing en la cláusula `exclude` del archivo `_config.yml` y los reescribes como se muestra a continuación, Polyglot podrá procesarlos sin problemas.

```yml
exclude: # Modificado consultando el problema https://github.com/untra/polyglot/issues/204.
  # - "*.gem"
  - jekyll-theme-chirpy.gemspec # - "*.gemspec"
  - tools
  - README.md
  - LICENSE
  - purgecss.config.js # - "*.config.js"
  - rollup.config.js
  - package*.json
```

## Modificación del encabezado html y sitemap
Ahora, para SEO, necesitamos insertar etiquetas meta Content-Language y etiquetas alternativas hreflang en el encabezado html de cada página del blog.

### Encabezado html
A partir de la versión 1.8.1, la última versión a noviembre de 2024, Polyglot tiene una función que realiza automáticamente esta tarea cuando se llama a la etiqueta Liquid {% raw %}`{% I18n_Headers %}`{% endraw %} en la parte del encabezado de la página.
Sin embargo, esto asume que se ha especificado el atributo 'permalink' en la página, y no funcionará correctamente si no es así.

Por lo tanto, tomé el [head.html del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/head.html) y agregué directamente el siguiente contenido.
Me referí a la [página SEO Recipes del blog oficial de Polyglot](https://polyglot.untra.io/seo/) para el trabajo, pero lo modifiqué para usar el atributo `page.url` en lugar de `page.permalink` si este último no está presente.
Además, refiriéndome a la [documentación oficial de Google Search Central](https://developers.google.com/search/docs/specialty/international/localized-versions#xdefault), especifiqué `x-default` en lugar de `site.default_lang` como valor del atributo hreflang para la página del idioma predeterminado del sitio, para que se reconozca el enlace de esa página como fallback cuando el idioma preferido del visitante no está en la lista de idiomas admitidos por el sitio o cuando no se puede reconocer el idioma preferido del visitante.

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

## Agregar botón de selección de idioma en la barra lateral
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

Luego, agregué las siguientes tres líneas a la parte de la clase "sidebar-bottom" en el [`_includes/sidebar.html` del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html) para que Jekyll cargue el contenido de `_includes/lang-selector.html` al construir la página:

{% raw %}
```liquid
<div class="lang-selector">
      {%- include lang-selector.html -%}
    </div>
```
{% endraw %}

## Problema de indexación incorrecta de páginas multilingües al usar la función de búsqueda
Después de completar los pasos anteriores, casi todas las funciones del sitio funcionaban satisfactoriamente como se pretendía. Sin embargo, descubrí tardíamente que había un problema: la barra de búsqueda ubicada en la esquina superior derecha de la página con el tema Chirpy no indexaba las páginas en idiomas distintos al `site.default_lang` (en el caso de este blog, inglés), y al buscar en idiomas distintos al inglés, también mostraba páginas en inglés como resultados de búsqueda.

Esto ocurre porque la biblioteca JavaScript [Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search) utilizada por el tema Chirpy depende de la variable `site.posts` proporcionada por Jekyll para realizar la indexación, y por lo tanto no reconoce las páginas multilingües construidas usando Polyglot que no sean del idioma predeterminado.

La estructura simple de Simple-Jekyll-Search, que realiza la indexación dependiendo solo de las variables proporcionadas por Jekyll con una única plantilla liquid llamada [`search.json`](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/assets/js/data/search.json), es una ventaja, pero en este caso actúa como una desventaja crítica y una limitación, por lo que no es adecuada para aplicar a este blog. A menos que Jekyll admita páginas multilingües de forma nativa y Polyglot proporcione alguna variable alternativa que pueda reemplazar a `site.posts`, Simple-Jekyll-Search no podrá realizar correctamente la indexación de páginas multilingües requerida por este blog. Por lo tanto, es necesario buscar y aplicar una alternativa que pueda reemplazar a Simple-Jekyll-Search, lo cual dejaré como una tarea pendiente y un tema para una publicación futura.
