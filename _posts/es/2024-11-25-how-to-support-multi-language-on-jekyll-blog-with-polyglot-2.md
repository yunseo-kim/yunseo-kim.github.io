---
title: "Cómo implementar soporte multilingüe en un blog Jekyll con Polyglot (2) - Implementación del botón de selección de idioma y localización del idioma del layout"
description: "Presenta el proceso de implementación de soporte multilingüe aplicando el plugin Polyglot a un blog Jekyll basado en 'jekyll-theme-chirpy'. Este post es el segundo de la serie, cubriendo la implementación del botón de selección de idioma y la localización del idioma del layout."
categories: [Dev, Web Dev]
tags: [Static Site, Jekyll, Polyglot, Markdown]
image: /assets/img/technology.webp
---

## Introducción
A principios de julio de 12024, implementé soporte multilingüe en este blog basado en Jekyll y alojado en GitHub Pages aplicando el plugin [Polyglot](https://github.com/untra/polyglot).
Esta serie comparte los bugs encontrados durante el proceso de aplicación del plugin Polyglot al tema Chirpy y su proceso de resolución, así como métodos para escribir headers HTML y sitemap.xml considerando SEO.
La serie consta de 3 artículos, y este artículo que estás leyendo es el segundo de la serie.
- Parte 1: [Aplicación del plugin Polyglot y modificación del header HTML y sitemap](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1)
- Parte 2: Implementación del botón de selección de idioma y localización del idioma del layout (este artículo)
- Parte 3: [Solución de problemas de fallo de compilación del tema Chirpy y errores en la función de búsqueda](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)

> Originalmente se componía de 2 partes en total, pero posteriormente se reestructuró a 3 partes debido al considerable aumento de contenido tras varias mejoras.
{: .prompt-info }

## Requisitos
- [x] Debe poder proporcionar el resultado de la compilación (páginas web) separado por rutas de idioma (ej. `/posts/ko/`{: .filepath}, `/posts/ja/`{: .filepath}).
- [x] Para minimizar el tiempo y esfuerzo adicional requerido para el soporte multiidioma, debe poder reconocer automáticamente el idioma según la ruta local donde se encuentra el archivo (ej. `/_posts/ko/`{: .filepath}, `/_posts/ja/`{: .filepath}) durante la compilación, sin necesidad de especificar manualmente las etiquetas 'lang' y 'permalink' en el YAML front matter de cada archivo markdown original.
- [x] La sección header de cada página del sitio debe incluir etiquetas meta Content-Language apropiadas, etiquetas alternativas hreflang y enlaces canónicos para cumplir con las directrices SEO de Google para búsquedas multiidioma.
- [x] Debe poder proporcionar enlaces de páginas para cada versión de idioma del sitio sin omisiones en `sitemap.xml`{: .filepath}, y el propio `sitemap.xml`{: .filepath} debe existir solo uno en la ruta raíz sin duplicados.
- [x] Todas las funciones proporcionadas por el [tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) deben funcionar normalmente en cada página de idioma, y si no es así, deben ser corregidas para funcionar normalmente.
  - [x] Funcionamiento normal de las funciones 'Recently Updated' y 'Trending Tags'
  - [x] No debe ocurrir errores durante el proceso de compilación usando GitHub Actions
  - [x] Funcionamiento normal de la función de búsqueda de posts en la esquina superior derecha del blog

## Antes de comenzar
Este artículo es una continuación de la [Parte 1](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1), por lo que si aún no lo has leído, se recomienda leer primero el artículo anterior.

## Agregar botón de selección de idioma en la barra lateral
> (Actualización del 12025.02.05.) Se mejoró el botón de selección de idioma en formato de lista desplegable.
{: .prompt-info }

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
{: file='\_includes/lang-selector.html'}
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
        padding: 0.75rem 2rem 0.75rem 1rem;  /* Área de toque más grande */
    }
    
    .lang-dropdown {
        min-width: 140px;  /* Área de selección más amplia en móvil */
    }
}
```
{: file='assets/css/lang-selector.css'}

Luego, en el [`_includes/sidebar.html`{: .filepath} del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy/blob/v7.1.1/_includes/sidebar.html), agregué las siguientes tres líneas de la clase `lang-selector-wrapper` justo antes de la clase `sidebar-bottom` para que Jekyll cargue el contenido del archivo `_includes/lang-selector.html`{: .filepath} creado anteriormente durante la compilación de la página.

{% raw %}
```liquid
  (anterior)...
  <div class="lang-selector-wrapper w-100">
    {%- include lang-selector.html -%}
  </div>

  <div class="sidebar-bottom d-flex flex-wrap align-items-center w-100">
    ...(posterior)
```
{: file='\_includes/sidebar.html'}
{% endraw %}

## (Función agregada el 12025.07.31.) Localización del idioma del layout
Anteriormente, solo se aplicaba la localización de idioma al contenido principal como títulos de página y contenido, mientras que el idioma del layout como nombres de pestañas en la barra lateral izquierda, sitio superior e inferior y panel derecho se mantenía fijo en inglés, que es el valor predeterminado del sitio. Personalmente, eso era suficiente para mí, por lo que no sentía mucha necesidad de trabajar adicionalmente. Sin embargo, recientemente, mientras trabajaba en el [parche de metadatos Open Graph y URL canónica mencionado anteriormente](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#header-html), descubrí que la localización del idioma del layout era posible de manera muy simple con solo unas pequeñas modificaciones. Si hubiera requerido una modificación de código compleja y tediosa, habría sido diferente, pero como era [un trabajo simple que no tomó ni 10 minutos](https://github.com/yunseo-kim/yunseo-kim.github.io/commit/6f231437f7ba16f669fcb60b504f024ea1cf83cb), lo apliqué adicionalmente.

### Agregar locales
Para proporcionar simultáneamente múltiples versiones de idioma para cada página del sitio y cambiar entre versiones según la selección del usuario, aunque no existe tal función, [el rango de idiomas que soporta el tema Chirpy en sí es bastante amplio](https://github.com/cotes2020/jekyll-theme-chirpy/tree/master/_data/locales). Por lo tanto, solo necesitas descargar selectivamente los archivos de locale necesarios de los que proporciona el tema Chirpy, agregarlos y, si es necesario, modificar apropiadamente solo los nombres de archivo. El nombre del archivo de locale debe coincidir con los elementos en la lista `languages` definida previamente en el archivo `_config.yml`{: .filepath} durante el paso de [configuración](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuración).

> De hecho, los archivos en el directorio `_data`{: .filepath} se proporcionan básicamente a través del [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy) incluso sin agregarlos directamente.
>
> Sin embargo, en mi caso, era difícil usar los locales proporcionados por el tema Chirpy tal como están debido a las siguientes razones, por lo que necesitaba algunas modificaciones por separado.
> - El formato de nombres de los archivos de locale proporcionados básicamente por el tema Chirpy incluye códigos de región como `ko-KR`, `ja-JP`, que no coinciden con el formato usado en este sitio (`ko`, `ja`, etc.)
> - Necesidad de modificar el texto de aviso de licencia del valor predeterminado [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) al [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) de este blog
> - Los locales en [coreano](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ko.yml) o [japonés](https://github.com/yunseo-kim/yunseo-kim.github.io/blob/main/_data/locales/ja.yml) me parecían un poco extraños o no adecuados para este blog desde mi perspectiva como coreano, por lo que existen partes que modifiqué personalmente
> - Como se describe a continuación, por varias razones no me gusta mucho la era cristiana, y en este blog adopto el [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar) como formato de fecha, por lo que necesitaba modificar el locale en consecuencia
>   - Fundamentalmente tiene un fuerte color religioso de una religión específica y es sesgado hacia Occidente
>     - Aunque no niego que Jesús fue un gran santo, y respeto la posición de esa religión, si dijeran que usarían la era cristiana solo internamente dentro de esa religión como el calendario budista, no habría problema alguno. Pero no es así, por eso planteo el problema. Hubo muchos otros santos como Confucio, Buda, Sócrates, etc., pero desde la perspectiva de no religiosos o personas que creen en otras religiones, y desde la perspectiva de otras culturas fuera de Europa, ¿cuál es la razón por la que el año de origen del sistema de años usado por todo el mundo deba ser específicamente el año de nacimiento de Jesús?
>     - Y si preguntas si ese 'año de origen' es realmente el año de nacimiento de Jesús, de hecho no es así, y la teoría establecida es que nació varios años antes
>   - Como es un sistema de años concebido antes de la aparición del concepto de '0', el año siguiente al año 1 a.C. (-1) es directamente el año 1 d.C. (1), lo que hace que el cálculo de años no sea intuitivo
>   - Los 10,000 años desde la entrada de la humanidad en el período neolítico y la sociedad agrícola hasta el nacimiento de Jesús, o incluso considerando solo después de la invención de la escritura, los 3000-4000 años de historia se agrupan como 'antes de Cristo', lo que causa distorsión cognitiva en la historia mundial, especialmente en la historia antigua
> 
> Por eso aquí agregué directamente archivos de locale en el directorio `_data/locales`{: .filepath} y los apliqué después de modificarlos apropiadamente.  
> Por lo tanto, si no aplica y desea aplicar los locales proporcionados por el tema Chirpy sin modificaciones, puede omitir este paso.
{: .prompt-tip }

### Integración con Polyglot
Ahora solo necesitas modificar ligeramente los siguientes dos archivos para integrar suavemente con Polyglot.

> Si inicialmente creaste el repositorio usando [Chirpy Starter](https://chirpy.cotes.page/posts/getting-started/#option-1-using-the-starter-recommended) en lugar de hacer fork directo del repositorio del tema, es posible que los archivos correspondientes no existan en el repositorio de tu sitio. Esto se debe a que son archivos proporcionados básicamente a través del [gem jekyll-theme-chirpy](https://rubygems.org/gems/jekyll-theme-chirpy), por lo que en ese caso, primero descarga los archivos originales correspondientes del [repositorio del tema Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) y colócalos en la misma ubicación dentro de tu repositorio antes de trabajar. Cuando Jekyll compila el sitio, si ya existe un archivo con el mismo nombre en el repositorio, se aplica con prioridad sobre el archivo proporcionado por el gem externo (jekyll-theme-chirpy).
{: .prompt-tip }

#### '\_includes/lang.html'
Como se muestra a continuación, agrega dos líneas de código en el medio del archivo [`_includes/lang.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_includes/lang.html) para que, cuando no se especifica por separado la variable `lang` en el YAML front matter de la página, reconozca prioritariamente la [variable `site.active_lang` de Polyglot](https://github.com/untra/polyglot?tab=readme-ov-file#features) sobre el idioma predeterminado del sitio (`site.lang`) o inglés (`'en'`) definido en `_config.yml`{: .filepath}. Este archivo es llamado comúnmente por todas las páginas del sitio que aplica el tema Chirpy ([`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html)) para declarar la variable `lang` durante la compilación, y utiliza esta variable `lang` declarada aquí para ejecutar la localización del idioma del layout.

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

Prioridad al declarar la variable `lang`:
- Antes de la modificación:
  1. `page.lang` (cuando se define en el YAML front matter de la página individual)
  2. `site.lang` (cuando se define en `_config.yml`{: .filepath})
  3. `'en'`
- Después de la modificación:
  1. `page.lang` (cuando se define en el YAML front matter de la página individual)
  2. **`site.active_lang`** (cuando se está aplicando Polyglot)
  3. `site.lang` (cuando se define en `_config.yml`{: .filepath})
  4. `'en'`

#### '\_layouts/default.html'
De manera similar, modifica el contenido del archivo [`_layouts/default.html`{: .filepath}](https://github.com/cotes2020/jekyll-theme-chirpy/blob/master/_layouts/default.html) para especificar correctamente el atributo `lang` en la etiqueta `<html>`, que es el elemento de nivel superior del documento HTML.

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

Prioridad al especificar el atributo `lang` de la etiqueta `<html>`:
- Antes de la modificación:
  1. `page.lang` (cuando se define en el YAML front matter de la página individual)
  2. `site.alt_lang` (cuando se define en `_config.yml`{: .filepath})
  3. `site.lang` (cuando se define en `_config.yml`{: .filepath})
  4. `unknown` (cadena vacía, `lang=""`)
- Después de la modificación:
  1. `page.lang` (cuando se define en el YAML front matter de la página individual)
  2. **`site.active_lang`** (cuando se está aplicando Polyglot)
  3. `site.alt_lang` (cuando se define en `_config.yml`{: .filepath})
  4. `site.lang` (cuando se define en `_config.yml`{: .filepath})
  5. `unknown` (cadena vacía, `lang=""`)

> No se recomienda dejar el idioma de la página web (atributo `lang`) sin especificar como `unknown`, y debe especificarse con un valor apropiado siempre que sea posible. Como se puede ver, se usa el valor del atributo `lang` en `_config.yml`{: .filepath} como respaldo, por lo que ya sea que uses Polyglot o no, es bueno definir apropiadamente este valor, y normalmente ya debería estar definido en casos normales. Si aplicas Polyglot o un plugin i18n similar como se trata en este artículo, sería apropiado especificarlo con el mismo valor que [`site.default_lang`](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-1/#configuración).
{: .prompt-tip }

## Lectura adicional
Continúa en la [Parte 3](/posts/how-to-support-multi-language-on-jekyll-blog-with-polyglot-3)
