---
title: "Crear y gestionar un blog en GitHub Pages"
description: >-
  Exploremos las características y diferencias entre páginas web estáticas y dinámicas, los generadores de sitios estáticos (Static Site Generator) y alojemos un blog Jekyll en GitHub Pages.
categories:
  - Blogging
tags:
  - Jekyll
---

Comencé a alojar un blog en GitHub Pages usando Jekyll a principios de 2021. Sin embargo, como no documenté adecuadamente el proceso de instalación en ese momento, tuve algunas dificultades con el mantenimiento posterior, así que decidí hacer un breve resumen del proceso de instalación y los métodos de mantenimiento.  
~~En realidad, la razón principal es que aún no estoy muy familiarizado con el alojamiento de sitios estáticos.~~
(Actualización de contenido en junio de 2024)

## 1. Generador de sitios estáticos y alojamiento web
### 1-1. Página web estática vs página web dinámica
#### Página web estática (Static Web Page)
- Una página web que entrega datos almacenados en el servidor directamente al usuario
- El servidor web entrega una página previamente almacenada en respuesta a la solicitud del usuario
- El usuario ve la misma página web a menos que se cambien los datos almacenados en el servidor
- Generalmente, la respuesta es rápida ya que solo se necesita enviar el archivo correspondiente a la solicitud, sin necesidad de procesamiento adicional
- Como solo consiste en archivos simples, solo se necesita configurar un servidor web, por lo que los costos de configuración son bajos
- El servicio es limitado ya que solo muestra información almacenada
- El administrador debe agregar, modificar y eliminar datos manualmente
- Estructura favorable para el rastreo por parte de los motores de búsqueda, relativamente más ventajosa para la optimización de motores de búsqueda (SEO)

#### Página web dinámica (Dynamic Web Page)
- Una página web que procesa los datos almacenados en el servidor con scripts antes de entregarlos
- El servidor web interpreta la solicitud del usuario, procesa los datos y luego entrega una página web generada
- El usuario ve páginas web que cambian según la situación, el tiempo, la solicitud, etc.
- La respuesta es relativamente lenta ya que se necesita procesar scripts para entregar la página web
- Se incurre en costos adicionales de configuración ya que se necesita un servidor de aplicaciones además del servidor web
- Es posible ofrecer diversos servicios combinando dinámicamente varias informaciones
- Dependiendo de la estructura de la página web, los usuarios pueden agregar, modificar y eliminar datos desde el navegador

### 1-2. Generador de sitios web estáticos (SSG, Static Site Generator)
- Una herramienta que genera páginas web estáticas basadas en datos sin procesar (generalmente archivos de texto en formato markdown) y plantillas predefinidas
- Automatiza el proceso de construir y desplegar páginas web sin necesidad de escribir páginas HTML individuales, simplemente escribiendo publicaciones en markdown
- Ejemplos: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Un servicio de alojamiento de páginas web estáticas gratuito proporcionado por GitHub
- Permite alojar una página web personal representativa por cuenta y crear y alojar páginas de documentación de proyectos ilimitadas por repositorio.
- Después de crear un repositorio con el nombre en el formato '{username}.github.io' que coincida con tu nombre de usuario de GitHub, puedes hacer push directamente de las páginas HTML construidas a ese repositorio o usar GitHub Actions para realizar la construcción y el despliegue.
- Si tienes un dominio propio, puedes conectarlo en la configuración para usar una dirección de dominio diferente en lugar del dominio predeterminado en formato '{username}.github.io'.

## 2. Elección del SSG y el tema a utilizar

### 2-1. Razones para elegir Jekyll
Aunque existen varios SSG como Jekyll, Hugo, Gatsby, etc., decidí usar Jekyll. Los criterios que consideré al elegir el SSG y las razones por las que elegí Jekyll son las siguientes:
- ¿Puedo minimizar pruebas y errores innecesarios y concentrarme en escribir y administrar el blog?
  - Jekyll es el generador de sitios web estáticos oficialmente soportado por Github Pages. Por supuesto, otros SSG como Hugo, Gatsby, etc. también se pueden alojar en Github Pages, y existe la opción de usar otros servicios de alojamiento como Netlify, pero en realidad, para operar un blog personal de este tamaño, no es muy importante qué SSG se usó técnicamente para construirlo o la velocidad de construcción y rendimiento, así que decidí que sería mejor usar algo que sea un poco más fácil de mantener y tenga más documentación de referencia.
  - Además, Jekyll tiene el período de desarrollo más largo en comparación con otros competidores como Hugo y Gatsby. Como resultado, está bien documentado y hay una cantidad abrumadora de recursos de referencia disponibles cuando surgen problemas.
- ¿Hay una variedad de temas y plugins disponibles?
  - Incluso si no se escribe HTML directamente y se usa un SSG, crear varias plantillas por uno mismo es engorroso, lleva mucho tiempo y realmente no es necesario. Hay muchos temas excelentes ya disponibles en la web, así que se puede adoptar y utilizar uno que te guste.
  - Además, como originalmente uso principalmente C y Python, no conozco bien Ruby de Jekyll o Go de Hugo, así que quería utilizar activamente los temas y plugins existentes.
  - Con Jekyll, pude encontrar rápidamente un tema que me gustó a primera vista, mientras que Hugo y Gatsby parecían tener relativamente pocos temas adecuados para blogs personales. Supongo que la compatibilidad con Github Pages, que muchos desarrolladores usan para alojar blogs personales como se mencionó anteriormente, y el período de desarrollo también tuvieron un gran impacto aquí.

### 2-2. Selección del tema
#### Minimal Mistakes (enero 2021 ~ abril 2022)
- Repositorio de Github: <https://github.com/mmistakes/minimal-mistakes>
- Página de demostración: <https://mmistakes.github.io/minimal-mistakes/>
- El tema que utilicé durante aproximadamente 1 año y 3 meses cuando creé el blog por primera vez
- Soporte para funciones de comentarios a través de Disqus, Discourse, utterances, etc.
- Soporte para funciones de clasificación de categorías y etiquetas
- Soporte integrado para Google Analytics
- Posibilidad de seleccionar pieles predefinidas
- Aunque luego descubrí el tema Chirpy que tiene un diseño más elegante y me gustó más, considerando que de todos modos es un blog de ingeniería, creo que fue bastante utilizable con un diseño limpio aunque no fuera hermoso.

#### Chirpy Jekyll Theme (abril 2022~)
- Repositorio de Github: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Página de demostración: <https://chirpy.cotes.page/>
- El tema que he estado usando desde que cambié el tema del blog en abril de 2022 hasta ahora
- Soporte para clasificación de múltiples categorías y funciones de etiquetas
- Soporte integrado para expresiones matemáticas con sintaxis LaTex basado en MathJax
- Soporte integrado para funciones de diagrama basadas en Mermaid
- Soporte para funciones de comentarios a través de Disqus, Giscus, etc.
- Soporte para Google Analytics, GoatCounter
- Soporte para temas claro y oscuro
- En el momento del cambio de tema, MathJax y Mermaid no eran compatibles de forma nativa con el tema Minimal Mistakes y tenían que agregarse mediante personalización, pero el tema Chirpy los admite de forma nativa. Por supuesto, la personalización no era gran cosa, pero aun así es una pequeña ventaja.
- Sobre todo, el diseño es bonito. Aunque el tema Minimal Mistakes es limpio, tiene una rigidez característica que parece más adecuada para documentación técnica oficial de proyectos o páginas de portafolio que para blogs, mientras que el tema Chirpy tiene la ventaja de un diseño que no se queda atrás en comparación con plataformas de blogs comerciales como Tistory, Medium o velog.

## 3. Crear repositorio de GitHub, construir y desplegar
Esto se describe basándose en el Chirpy Jekyll Theme que estoy usando actualmente (junio de 2024), y se asume que Git ya está instalado.  
Consulta la [Guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/) y la [Página oficial del tema Chirpy Jekyll](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalar Ruby y Jekyll
Instala Ruby y Jekyll según tu entorno de sistema operativo siguiendo la [Guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Crear repositorio de GitHub
La [página oficial del tema Chirpy Jekyll](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) introduce los siguientes dos métodos:
1. Método que obtiene los archivos principales con la gema "jekyll-theme-chirpy" y obtiene los recursos restantes de la plantilla [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Ventaja: Como se mencionará más adelante, es fácil aplicar actualizaciones de versión.
  - Desventaja: La personalización está limitada.
2. Método de bifurcar el repositorio [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) como repositorio de tu propio blog
  - Ventaja: Como gestionas directamente todos los archivos dentro del repositorio, puedes personalizar libremente modificando el código directamente incluso para funciones no soportadas por el tema.
  - Desventaja: Para aplicar actualizaciones de versión, debes fusionar [la última etiqueta upstream del repositorio original](https://github.com/cotes2020/jekyll-theme-chirpy/tags), lo que puede causar conflictos con el código personalizado en algunos casos. En este caso, debes resolver el conflicto manualmente.

Yo adopté el método 1. En el caso del tema Chirpy, tiene una alta integridad básica, por lo que no hay mucho que personalizar desde el punto de vista de la mayoría de los usuarios, y hasta 2024 todavía se está desarrollando y mejorando activamente, por lo que a menos que hagas modificaciones importantes, las ventajas de seguir el upstream original a tiempo superan las ventajas de aplicar personalizaciones directas. La guía oficial del tema Chirpy también recomienda el método 1 para la mayoría de los usuarios.

### 3-3. Configuraciones principales
Aplica las configuraciones necesarias en los archivos `_config.yml`{: .filepath} en el directorio raíz y `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. Están bien comentados y las configuraciones son intuitivas, por lo que se pueden aplicar sin dificultad. Las únicas configuraciones que requieren trabajo adicional externo son el registro del código de autenticación para la integración con Google Search Console y la integración de herramientas de webmaster como Google Analytics o GoatCounter, pero en realidad no es un procedimiento muy complicado y no es el tema principal que quiero abordar en este artículo, así que omito la descripción detallada.

### 3-4. Construir localmente
No es un procedimiento esencial, pero es posible que quieras verificar previamente si se mostrará correctamente en la web cuando escribas una nueva publicación o hagas alguna modificación en el sitio. En estos casos, puedes abrir una terminal en el directorio raíz del repositorio local y ejecutar el siguiente comando:
```console
$ bundle exec jekyll s
```
Después de esperar unos segundos, el sitio se construirá localmente y podrás ver el resultado en la dirección <http://127.0.0.1:4000>.

### 3-5. Desplegar
Hay dos métodos:
1. Usar GitHub Actions (en caso de alojar en GitHub Pages)
  - Si estás usando el plan gratuito de GitHub, debes mantener el repositorio público
  - En la página web de GitHub, selecciona la pestaña *Settings* del repositorio, luego haz clic en *Code and automation > Pages* en la barra de navegación izquierda y selecciona la opción **GitHub Actions** en la sección **Source**
  - Después de completar la configuración, el flujo de trabajo *Build and Deploy* se ejecutará automáticamente cada vez que hagas push de un nuevo commit
2. Construir y desplegar manualmente (en caso de usar otro servicio de alojamiento o autoalojamiento)
  - Ejecuta el siguiente comando para construir el sitio manualmente
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Sube el resultado de la construcción en el directorio `_site` al servidor

## 4. Escribir publicaciones
La [guía de escritura de publicaciones](https://chirpy.cotes.page/posts/write-a-new-post/) del tema Chirpy documenta bien el método de escritura de publicaciones y las opciones disponibles. Proporciona varias funciones además de las descritas en este artículo, y contiene información útil para referencia, así que consulta la documentación oficial si es necesario. Aquí resumimos los puntos principales que deben tenerse en cuenta cada vez que se publica.

### Crear archivo markdown
- Formato del nombre: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Ubicación: directorio `_posts`{: .filepath}

### Escribir Front Matter
En la primera parte del archivo markdown, debes escribir adecuadamente el Front Matter.
```YAML
---
title: TITLE
description: >-
  DESCRIPTION
date: YYYY-MM-DD HH:MM:SS +/-TTTT
categories: [TOP_CATEGORIE, SUB_CATEGORIE]
tags: [TAG]     # TAG names should always be lowercase
---
```
- **title**: Título de la publicación
- **description**: Resumen. Si no se escribe, se usa automáticamente una parte del contenido del cuerpo, pero se recomienda escribir directamente la etiqueta meta de descripción para la optimización de motores de búsqueda (SEO). Una longitud apropiada es de 135~160 caracteres en alfabeto romano, o 80~110 caracteres en coreano.
- **date**: Fecha y hora exacta de escritura de la publicación y zona horaria (opcional, si se omite, se reconoce y usa automáticamente la información de fecha de escritura del título del archivo)
- **categories**: Clasificación de categorías de la publicación
- **tags**: Clasificación de etiquetas para aplicar a la publicación

## 5. Actualización

Esto se describe asumiendo que se adoptó el método 1 en [3-2](/posts/Creating-and-Managing-a-GitHub-Pages-Blog/#3-2-crear-repositorio-de-github). Si adoptaste el método 2, como se mencionó anteriormente, debes fusionar manualmente la última etiqueta upstream.

1. Edita `Gemfile`{: .filepath} para espec