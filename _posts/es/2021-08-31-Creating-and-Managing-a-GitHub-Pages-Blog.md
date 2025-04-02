---
title: Crear y gestionar un blog en GitHub Pages
description: Exploremos las características y diferencias entre páginas web estáticas y dinámicas, generadores de sitios estáticos (Static Site Generator) y cómo alojar un blog Jekyll en GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---
Desde principios del año 12021 de la [era holocena](https://en.wikipedia.org/wiki/Holocene_calendar), comencé a alojar un blog en GitHub Pages utilizando Jekyll. Sin embargo, como no documenté adecuadamente el proceso de instalación en ese momento, tuve algunas dificultades con el mantenimiento posterior, así que decidí documentar brevemente el proceso de instalación y los métodos de mantenimiento.

(+ Actualización 12024.12)

## 1. Generador de sitios estáticos y alojamiento web
### 1-1. Páginas web estáticas vs páginas web dinámicas
#### Páginas web estáticas (Static Web Page)
- Páginas web que entregan datos almacenados en el servidor directamente al usuario
- El servidor web entrega páginas previamente almacenadas en respuesta a las solicitudes del usuario
- Los usuarios ven la misma página web a menos que se modifiquen los datos almacenados en el servidor
- Como solo se necesita transferir el archivo correspondiente a la solicitud, no se requiere trabajo adicional, por lo que generalmente la respuesta es rápida
- Consisten solo en archivos simples, por lo que solo se necesita configurar un servidor web, lo que hace que los costos de implementación sean económicos
- Como solo muestran información almacenada, los servicios son limitados
- El administrador debe agregar, modificar y eliminar datos manualmente
- Estructura fácil de rastrear para los motores de búsqueda, lo que es relativamente más ventajoso para la optimización de motores de búsqueda (SEO)

#### Páginas web dinámicas (Dynamic Web Page)
- Páginas web que procesan datos almacenados en el servidor mediante scripts antes de entregarlos
- El servidor web interpreta la solicitud del usuario, procesa los datos y luego entrega la página web generada
- Los usuarios ven páginas web que varían según la situación, el tiempo, la solicitud, etc.
- La respuesta es relativamente más lenta porque se debe procesar el script para entregar la página web
- Se requiere un servidor de aplicaciones además del servidor web, lo que genera costos adicionales durante la implementación
- Es posible ofrecer diversos servicios al combinar y proporcionar dinámicamente diferentes tipos de información
- Según la estructura de la página web, los usuarios pueden agregar, modificar y eliminar datos desde el navegador

### 1-2. Generador de sitios estáticos (SSG, Static Site Generator)
- Herramienta que genera páginas web estáticas basadas en datos sin procesar (generalmente archivos de texto en formato markdown) y plantillas predefinidas
- Automatiza el proceso de crear y desplegar páginas web sin necesidad de escribir páginas HTML individuales, simplemente escribiendo publicaciones en markdown
- Ejemplos: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Servicio de alojamiento de páginas web estáticas gratuito proporcionado por GitHub
- Cada cuenta puede alojar 1 página web personal representativa y crear y alojar un número ilimitado de páginas de documentación de proyectos por repositorio
- Después de crear un repositorio con el nombre '{username}.github.io' que coincida con tu nombre de usuario de GitHub, puedes enviar directamente páginas HTML compiladas a ese repositorio o utilizar GitHub Actions para compilar y desplegar
- Si tienes un dominio propio, puedes conectarlo en la configuración para usar una dirección de dominio diferente en lugar del dominio predeterminado '{username}.github.io'

## 2. Selección del SSG y tema a utilizar

### 2-1. Por qué elegí Jekyll
Aunque existen varios SSG como Jekyll, Hugo, Gatsby, etc., decidí usar Jekyll. Los criterios que consideré al elegir un SSG y las razones por las que elegí Jekyll son los siguientes:
- ¿Puedo minimizar pruebas y errores innecesarios y concentrarme en escribir y administrar el blog?
  - Jekyll es el generador de sitios web estáticos oficialmente compatible con GitHub Pages. Por supuesto, otros SSG como Hugo, Gatsby, etc. también se pueden alojar en GitHub Pages, e incluso existe la opción de utilizar otros servicios de alojamiento como Netlify, pero en realidad, para administrar un blog personal de este tamaño, no importa mucho qué SSG se utilizó técnicamente para construirlo, ni la velocidad de compilación o el rendimiento, así que decidí que sería mejor usar algo que fuera más simple de mantener y tuviera más documentación de referencia.
  - Además, Jekyll tiene el período de desarrollo más largo en comparación con otros competidores como Hugo y Gatsby. Esto significa que está bien documentado y hay una cantidad abrumadora de recursos disponibles cuando surgen problemas.
- ¿Hay una variedad de temas y plugins disponibles?
  - Incluso si usas un SSG en lugar de escribir HTML directamente, crear varias plantillas desde cero es tedioso, lleva mucho tiempo y realmente no es necesario. Hay muchos temas excelentes ya disponibles en línea, así que puedes adoptar y utilizar uno que te guste.
  - Además, como principalmente uso C y Python, no conozco bien Ruby (Jekyll) o Go (Hugo), así que quería aprovechar al máximo los temas y plugins existentes.
  - Con Jekyll, pude encontrar rápidamente un tema que me gustó a primera vista, mientras que Hugo y Gatsby parecían tener relativamente menos temas adecuados para blogs personales. Supongo que la compatibilidad con GitHub Pages, que muchos desarrolladores usan para alojar blogs personales, y el período de desarrollo más largo también tuvieron un gran impacto aquí.

### 2-2. Selección de tema
#### Minimal Mistakes (12021.01 - 12022.04)
- GitHub Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- Tema que utilicé durante aproximadamente 1 año y 3 meses cuando creé el blog por primera vez
- Soporte para comentarios a través de Disqus, Discourse, utterances, etc.
- Soporte para funciones de clasificación de categorías y etiquetas
- Soporte integrado para Google Analytics
- Posibilidad de elegir entre pieles predefinidas
- Aunque más tarde descubrí el tema Chirpy, que tiene un diseño más elegante y me gustó más, considerando que es un blog de ingeniería, creo que Minimal Mistakes tenía un diseño bastante limpio aunque no fuera tan bonito.

#### Chirpy Jekyll Theme (12022.04 - presente)
- GitHub Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- Tema que he estado usando desde que cambié el tema del blog en abril de 12022
- Soporte para clasificación de múltiples categorías y funciones de etiquetas
- Soporte integrado para expresiones matemáticas con sintaxis LaTeX basado en MathJax
- Soporte integrado para funciones de diagramas basado en Mermaid
- Soporte para comentarios a través de Disqus, Giscus, etc.
- Soporte para Google Analytics, GoatCounter
- Soporte para temas claro y oscuro
- En el momento del cambio de tema, MathJax y Mermaid no estaban integrados en el tema Minimal Mistakes y tenían que agregarse mediante personalización, mientras que el tema Chirpy los admite de forma nativa. Por supuesto, la personalización no era gran cosa, pero sigue siendo una pequeña ventaja.
- Sobre todo, el diseño es bonito. Aunque Minimal Mistakes es limpio, tiene una rigidez característica que parece más adecuada para documentación técnica oficial de proyectos o páginas de portafolio que para un blog, mientras que el tema Chirpy tiene la ventaja de un diseño que no se queda atrás en comparación con plataformas de blogs comerciales como Tistory, Medium, velog, etc.

## 3. Crear un repositorio de GitHub, compilar y desplegar
Esto se basa en el Chirpy Jekyll Theme que estoy usando actualmente (12024.06), y asume que Git ya está instalado.  
Consulta la [Guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/) y la [Página oficial de Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalar Ruby y Jekyll
Instala Ruby y Jekyll según la [Guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/) de acuerdo con tu entorno de sistema operativo.

### 3-2. Crear un repositorio de GitHub
La [página oficial de Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) presenta los siguientes dos métodos:
1. Usar la gema "jekyll-theme-chirpy" para importar los archivos principales y obtener el resto de los recursos de la plantilla [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Ventaja: Como se mencionará más adelante, es fácil aplicar actualizaciones de versión.
  - Desventaja: La personalización es limitada.
2. Bifurcar (fork) el repositorio [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) como repositorio de tu blog
  - Ventaja: Como administras todos los archivos directamente dentro del repositorio, puedes personalizar libremente modificando el código directamente, incluso para funciones no admitidas por el tema.
  - Desventaja: Para aplicar actualizaciones de versión, debes fusionar la [última etiqueta upstream del repositorio original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), y en algunos casos, el código que has personalizado directamente puede entrar en conflicto con el código de la versión actualizada. En este caso, debes resolver el conflicto manualmente.

Yo adopté el método 1. En el caso del tema Chirpy, tiene un alto nivel de integridad por defecto, por lo que la mayoría de los usuarios no tienen mucho que personalizar, y dado que el desarrollo y la mejora de funciones continúan activamente hasta 12024, a menos que planees hacer modificaciones extensas, las ventajas de seguir el upstream original superan las ventajas de aplicar personalizaciones directas. La guía oficial del tema Chirpy también recomienda el método 1 para la mayoría de los usuarios.

### 3-3. Configuraciones principales
Aplica las configuraciones necesarias en los archivos `_config.yml`{: .filepath}, `_data/contact.yml`{: .filepath} y `_data/share.yml`{: .filepath} en el directorio raíz. Están bien comentados y las configuraciones son intuitivas, por lo que se pueden aplicar sin dificultad. Las configuraciones que requieren trabajo adicional externo incluyen el registro del código de autenticación para la integración con Google Search Console y la integración con herramientas de webmaster como Google Analytics o GoatCounter, pero estos procedimientos no son realmente complicados y no son el tema principal de este artículo, así que omito la descripción detallada.

### 3-4. Compilar localmente
Aunque no es un procedimiento obligatorio, es posible que desees verificar previamente si algo se mostrará correctamente en la web cuando escribas una nueva publicación o hagas alguna modificación en el sitio. En este caso, abre una terminal en el directorio raíz del repositorio local y ejecuta el siguiente comando:
```console
$ bundle exec jekyll s
```
Después de esperar unos segundos, el sitio se compilará localmente y podrás ver el resultado en la dirección <http://127.0.0.1:4000>.

### 3-5. Desplegar
Hay dos métodos:
1. Usar GitHub Actions (cuando se aloja en GitHub Pages)
  - Si estás usando el plan gratuito de GitHub, debes mantener el repositorio público
  - En la página web de GitHub, selecciona la pestaña *Settings* del repositorio, luego haz clic en *Code and automation > Pages* en la barra de navegación izquierda y selecciona la opción **GitHub Actions** en la sección **Source**
  - Una vez completada la configuración, el flujo de trabajo *Build and Deploy* se ejecutará automáticamente cada vez que envíes un nuevo commit
2. Compilar y desplegar manualmente (cuando utilizas otro servicio de alojamiento o autoalojamiento)
  - Ejecuta el siguiente comando para compilar el sitio directamente
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Sube los resultados de la compilación en el directorio `_site` al servidor

## 4. Escribir publicaciones
La [guía de escritura de publicaciones](https://chirpy.cotes.page/posts/write-a-new-post/) del tema Chirpy documenta bien el método de escritura de publicaciones y las opciones disponibles. Proporciona varias funciones además de las descritas en este artículo, y es un buen contenido de referencia, así que consulta la documentación oficial si es necesario. Aquí resumo los puntos principales que deben tenerse en cuenta cada vez que se publica.

### Crear un archivo markdown
- Formato del nombre: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Ubicación: directorio `_posts`{: .filepath}

### Escribir el Front Matter
En la primera parte del archivo markdown, debes escribir adecuadamente el Front Matter.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]
image:
  path: /path/to/image
  alt: image alternative text
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: Título de la publicación
- **description**: Resumen. Si no se escribe, automáticamente se utilizará parte del contenido del texto principal, pero se recomienda escribir directamente la etiqueta meta description para la optimización de motores de búsqueda (SEO). Una cantidad adecuada es de aproximadamente 135-160 caracteres en alfabeto romano, o 80-110 caracteres en coreano.
- **date**: Fecha y hora exactas de la publicación y zona horaria (opcional, si se omite, se utilizará automáticamente la fecha de creación o modificación del archivo)
- **categories**: Clasificación de categorías de la publicación
- **tags**: Clasificación de etiquetas para aplicar a la publicación
- **image**: Insertar imagen de vista previa en la parte superior de la publicación
  - **path**: Ruta del archivo de imagen
  - **alt**: Texto alternativo (opcional)
- **toc**: Si se usa la función de tabla de contenidos en la barra lateral derecha, el valor predeterminado es `true`
- **comments**: Se usa cuando se desea especificar explícitamente si se permiten comentarios para publicaciones individuales, independientemente de la configuración predeterminada del sitio
- **math**: Activa la función de expresión matemática basada en [MathJax](https://www.mathjax.org/) incorporado, el valor predeterminado está desactivado (`false`) para el rendimiento de la página
- **mermaid**: Activa la función de expresión de diagrama basada en [Mermaid](https://github.com/mermaid-js/mermaid) incorporado, el valor predeterminado está desactivado (`false`)

## 5. Actualización

Esto asume que adoptaste el método 1 en [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-crear-un-repositorio-de-github). Si adoptaste el método 2, como se mencionó anteriormente, deberás fusionar directamente la última etiqueta upstream.

1. Edita `Gemfile`{: .filepath} para especificar la nueva versión de la gema "jekyll-theme-chirpy".
2. En el caso de actualizaciones mayores, es posible que también se hayan cambiado los archivos principales no incluidos en la gema "jekyll-theme-chirpy" y las opciones de configuración. En este caso, debes verificar los cambios con la siguiente API de GitHub y reflejarlos directamente:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
