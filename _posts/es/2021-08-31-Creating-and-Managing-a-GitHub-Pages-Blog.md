---
title: Crear y gestionar un blog en GitHub Pages
description: Exploremos las características y diferencias entre páginas web estáticas y dinámicas, los generadores de sitios estáticos, y cómo alojar un blog Jekyll en GitHub Pages.
categories: [AI & Data, Blogging]
tags: [Jekyll, Markdown]
image: /assets/img/technology.jpg
---
Empecé a alojar un blog en GitHub Pages usando Jekyll a principios del año 12021 de la [era humana](https://es.wikipedia.org/wiki/Calendario_holoceno). Sin embargo, como no documenté adecuadamente el proceso de instalación en ese momento, tuve algunas dificultades con el mantenimiento posterior. Por lo tanto, decidí hacer un breve resumen del proceso de instalación y los métodos de mantenimiento.

(+ Actualizado en 12024.12)

## 1. Generador de sitios estáticos y alojamiento web
### 1-1. Páginas web estáticas vs páginas web dinámicas
#### Páginas web estáticas (Static Web Page)
- Páginas web que entregan datos almacenados en el servidor directamente al usuario
- El servidor web entrega páginas previamente almacenadas en respuesta a las solicitudes del usuario
- Los usuarios ven la misma página web a menos que se cambien los datos almacenados en el servidor
- Generalmente, la respuesta es rápida ya que solo se necesita enviar el archivo correspondiente a la solicitud, sin necesidad de trabajo adicional
- Como solo consisten en archivos simples, solo se necesita configurar un servidor web, por lo que los costos de configuración son bajos
- El servicio es limitado ya que solo muestra información almacenada
- El administrador debe agregar, modificar y eliminar datos manualmente
- Estructura favorable para el rastreo por parte de los motores de búsqueda, relativamente más ventajosa para la optimización de motores de búsqueda (SEO)

#### Páginas web dinámicas (Dynamic Web Page)
- Páginas web que procesan datos almacenados en el servidor con scripts antes de entregarlos
- El servidor web interpreta la solicitud del usuario, procesa los datos y luego entrega la página web generada
- Los usuarios ven páginas web que cambian según la situación, el tiempo, la solicitud, etc.
- La respuesta es relativamente lenta ya que se necesita procesar scripts para entregar la página web
- Se incurren en costos adicionales de configuración ya que se necesita un servidor de aplicaciones además del servidor web
- Es posible proporcionar diversos servicios combinando dinámicamente varias informaciones
- Dependiendo de la estructura de la página web, los usuarios pueden agregar, modificar y eliminar datos desde el navegador
- 
### 1-2. Generador de sitios web estáticos (SSG, Static Site Generator)
- Herramienta que genera páginas web estáticas basadas en datos sin procesar (generalmente archivos de texto en formato markdown) y plantillas predefinidas
- Automatiza el proceso de construir y desplegar páginas web sin necesidad de escribir páginas HTML individuales, simplemente escribiendo posts en markdown
- Ejemplos: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Servicio de alojamiento de páginas web estáticas gratuito proporcionado por GitHub
- Se puede alojar 1 página web personal representativa por cuenta y un número ilimitado de páginas de documentación de proyectos por repositorio
- Después de crear un repositorio con el nombre '{username}.github.io' que coincida con tu nombre de usuario de GitHub, puedes hacer push directamente de las páginas HTML construidas a ese repositorio o usar GitHub Actions para realizar la construcción y el despliegue
- Si tienes un dominio propio, puedes conectarlo en la configuración para usar una dirección de dominio diferente en lugar del dominio predeterminado '{username}.github.io'

## 2. Elección del SSG y tema a utilizar

### 2-1. Razones para elegir Jekyll
Aunque existen varios SSG como Jekyll, Hugo, Gatsby, etc., decidí usar Jekyll. Los criterios que consideré al elegir el SSG y las razones por las que elegí Jekyll son las siguientes:
- ¿Puedo minimizar pruebas y errores innecesarios y concentrarme en escribir y administrar el blog?
  - Jekyll es el generador de sitios web estáticos oficialmente soportado por Github Pages. Aunque otros SSG como Hugo, Gatsby, etc. también se pueden alojar en Github Pages sin problemas, e incluso existe la opción de usar otros servicios de alojamiento como Netlify, la verdad es que para un blog personal de este tamaño, no es muy importante técnicamente qué SSG se usó para construirlo o su velocidad de construcción y rendimiento. Así que decidí que sería mejor usar algo que sea un poco más fácil de mantener y tenga más documentación de referencia.
  - Además, Jekyll tiene el período de desarrollo más largo en comparación con sus competidores como Hugo y Gatsby. Esto significa que está bien documentado y hay una cantidad abrumadora de recursos de referencia disponibles cuando surgen problemas.
- ¿Hay una variedad de temas y plugins disponibles?
  - Incluso si no se escribe HTML directamente y se usa un SSG, crear varias plantillas por uno mismo es engorroso, lleva mucho tiempo y realmente no es necesario. Hay muchos temas excelentes ya disponibles en la web, así que se puede adoptar y utilizar uno que te guste.
  - Además, como originalmente uso principalmente C o Python, no conozco bien Ruby de Jekyll o Go de Hugo, así que quería utilizar activamente los temas y plugins existentes.
  - Con Jekyll, pude encontrar rápidamente un tema que me gustó a primera vista, mientras que Hugo y Gatsby parecían tener relativamente pocos temas adecuados para blogs personales. Parece que la compatibilidad con Github Pages, que muchos desarrolladores usan para alojar blogs personales, y el período de desarrollo mencionado anteriormente también tuvieron un gran impacto aquí.

### 2-2. Selección del tema
#### Minimal Mistakes (12021.01 - 12022.04)
- Repositorio de Github: <https://github.com/mmistakes/minimal-mistakes>
- Página de demostración: <https://mmistakes.github.io/minimal-mistakes/>
- Tema que utilicé durante aproximadamente 1 año y 3 meses cuando creé el blog por primera vez
- Soporte para funciones de comentarios a través de Disqus, Discourse, utterances, etc.
- Soporte para funciones de clasificación de categorías y etiquetas
- Soporte integrado para Google Analytics
- Posibilidad de seleccionar pieles predefinidas
- Aunque luego descubrí el tema Chirpy que tiene un diseño más elegante y me gusta más, considerando que es un blog de ingeniería, creo que fue bastante útil con un diseño limpio aunque no sea bonito.

#### Chirpy Jekyll Theme (12022.04 - presente)
- Repositorio de Github: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Página de demostración: <https://chirpy.cotes.page/>
- Tema que he estado usando desde que cambié el tema del blog en abril de 12022
- Soporte para clasificación de múltiples categorías y función de etiquetas
- Soporte integrado para expresiones de fórmulas con sintaxis LaTex basado en MathJax
- Soporte integrado para funciones de diagrama basadas en Mermaid
- Soporte para funciones de comentarios a través de Disqus, Giscus, etc.
- Soporte para Google Analytics, GoatCounter
- Soporte para temas claro y oscuro
- En el momento del cambio de tema, MathJax y Mermaid no estaban soportados nativamente en el tema Minimal Mistakes y tenían que agregarse mediante personalización, pero el tema Chirpy los soporta de forma nativa. Por supuesto, la personalización no era gran cosa, pero aún así es una pequeña ventaja.
- Sobre todo, el diseño es bonito. Aunque el tema Minimal Mistakes es limpio, tiene una rigidez característica que parece más adecuada para documentación técnica oficial de proyectos o páginas de portafolio que para blogs. El tema Chirpy tiene la ventaja de un diseño que no se queda atrás incluso en comparación con plataformas de blogs comerciales como Tistory, Medium o velog.

## 3. Crear repositorio de GitHub, construir y desplegar
Esto se describe basándose en el Chirpy Jekyll Theme que estoy usando actualmente (12024.06), y se asume que Git ya está instalado básicamente.  
Referencia a la [guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/) y la [página oficial del tema Chirpy Jekyll](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalar Ruby y Jekyll
Instala Ruby y Jekyll según tu entorno de sistema operativo siguiendo la [guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Crear repositorio de GitHub
La [página oficial del tema Chirpy Jekyll](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) introduce los siguientes dos métodos:
1. Método de importar los archivos principales con la gema "jekyll-theme-chirpy" y obtener los recursos restantes de la plantilla [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Ventaja: Como se mencionará más adelante, es fácil aplicar actualizaciones de versión.
  - Desventaja: La personalización está limitada.
2. Método de bifurcar el repositorio [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) como repositorio de tu propio blog
  - Ventaja: Como gestionas directamente todos los archivos dentro del repositorio, puedes personalizar libremente incluso funciones no soportadas por el tema modificando directamente el código.
  - Desventaja: Para aplicar actualizaciones de versión, debes fusionar [la última etiqueta upstream del repositorio original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), lo que puede causar conflictos con el código personalizado en algunos casos. En este caso, debes resolver el conflicto manualmente.

Yo adopté el método 1. En el caso del tema Chirpy, ya tiene una alta integridad básica, por lo que la mayoría de los usuarios no tienen mucho que personalizar. Además, hasta 12024, el desarrollo y la mejora de funciones siguen siendo bastante activos, por lo que a menos que hagas modificaciones extensas, las ventajas de seguir el upstream original superan las ventajas de aplicar personalizaciones directas. La guía oficial del tema Chirpy también recomienda el método 1 para la mayoría de los usuarios.

### 3-3. Configuraciones principales
Aplica las configuraciones necesarias en los archivos `_config.yml`{: .filepath} en el directorio raíz y `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. Los comentarios están bien escritos y las configuraciones son intuitivas, por lo que se pueden aplicar sin dificultad. Las configuraciones que requieren trabajo adicional externo incluyen el registro del código de autenticación para la integración con Google Search Console y la integración de herramientas de webmaster como Google Analytics o GoatCounter, pero estos procedimientos no son realmente complicados y no son el tema principal que quiero abordar en este artículo, así que omito la descripción detallada.

### 3-4. Construir localmente
Aunque no es un procedimiento esencial, es posible que quieras verificar previamente si algo se mostrará correctamente en la web cuando escribas un nuevo post o hagas alguna modificación en el sitio. En estos casos, puedes abrir una terminal en el directorio raíz del repositorio local y ejecutar el siguiente comando:
```console
$ bundle exec jekyll s
```
Después de esperar unos segundos, el sitio se construirá localmente y podrás verificar el resultado en la dirección <http://127.0.0.1:4000>.

### 3-5. Desplegar
Hay dos métodos:
1. Utilizar GitHub Actions (en caso de alojamiento en GitHub Pages)
  - Si estás usando el plan gratuito de GitHub, debes mantener el repositorio público
  - En la página web de GitHub, selecciona la pestaña *Settings* del repositorio, luego haz clic en *Code and automation > Pages* en la barra de navegación izquierda y selecciona la opción **GitHub Actions** en la sección **Source**
  - Después de completar la configuración, el flujo de trabajo *Build and Deploy* se ejecutará automáticamente cada vez que hagas push de un nuevo commit
2. Construir y desplegar directamente (en caso de utilizar otro servicio de alojamiento o autoalojamiento)
  - Ejecuta el siguiente comando para construir el sitio directamente
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Sube el resultado de la construcción en el directorio `_site` al servidor

## 4. Escribir posts
La [guía de escritura de posts](https://chirpy.cotes.page/posts/write-a-new-post/) del tema Chirpy documenta bien el método de escritura de posts y las opciones disponibles. Proporciona varias funciones además de las descritas en este artículo, y contiene información útil para referencia, así que consulta la documentación oficial si es necesario. Aquí resumiré los puntos principales que deben tenerse en cuenta cada vez que se publica un post.

### Crear archivo markdown
- Formato del nombre: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Ubicación: directorio `_posts`{: .filepath}

### Escribir Front Matter
En la primera parte del archivo markdown, se debe escribir adecuadamente el Front Matter.
```YAML
---
title: TÍTULO
description: >-
  DESCRIPCIÓN
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [CATEGORÍA_PRINCIPAL, SUBCATEGORÍA]
tags: [ETIQUETA]
image:
  path: /ruta/a/imagen
  alt: texto alternativo de la imagen
toc: true
comments: false
math: true
mermaid: true
---
```
- **title**: Título del post
- **description**: Resumen. Si no se escribe, se utilizará automáticamente una parte del contenido del cuerpo, pero se recomienda escribir directamente la etiqueta meta de descripción para la optimización de motores de búsqueda (SEO). Una longitud apropiada es de 135~160 caracteres en alfabeto latino, o 80~110 caracteres en coreano.
- **date**: Fecha y hora exacta de escritura del post y zona horaria (opcional, si se omite, se utilizará automáticamente la información de fecha de creación o modificación del archivo)
- **categories**: Clasificación de categorías del post
- **tags**: Clasificación de etiquetas a aplicar al post
- **image**: Insertar imagen de vista previa en la parte superior del post
  - **path**: Ruta del archivo de imagen
  - **alt**: Texto alternativo (opcional)
- **toc**: Uso de la función de tabla de contenidos en la barra lateral derecha, el valor predeterminado es `true`
- **comments**: Se usa cuando se quiere especificar explícitamente el uso de comentarios para posts individuales, independientemente de la configuración predeterminada del sitio
- **math**: Activa la función de expresión de fórmulas basada en [MathJax](https://www.mathjax.org/) incorporado, el valor predeterminado es desactivado (`false`) para el rendimiento de la página
- **mermaid**: Activa la función de expresión de diagramas basada en [Mermaid](https://github.com/mermaid-js/mermaid) incorporado, el valor predeterminado es desactivado (`false`)

## 5. Actualización

Esto se describe asumiendo que se adoptó el método 1 en [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-crear-repositorio-de-github). Si se adoptó el método 2, como se mencionó anteriormente, se debe fusionar directamente la última etiqueta upstream.

1. Edita `Gemfile`{: .filepath} para especificar la nueva versión de la gema "jekyll-theme-chirpy".
2. En el caso de actualizaciones mayores, es posible que también se hayan cambiado los archivos principales no incluidos en la gema "jekyll-theme-chirpy" y las opciones de configuración. En este caso, debes verificar los cambios con la siguiente API de GitHub y reflejarlos directamente:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<versión_anterior>...<versión_nueva>
  ```
