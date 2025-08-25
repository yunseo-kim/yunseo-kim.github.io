---
title: Crear y gestionar un blog en GitHub Pages
description: Características y diferencias entre páginas web estáticas y dinámicas, qué es un generador de sitios estáticos y cómo alojar un blog Jekyll en GitHub Pages.
categories: [Dev, Web Dev]
tags: [Jekyll, Markdown, Static Site]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Creating-and-Managing-a-GitHub-Pages-Blog/
---

Empecé a alojar mi blog en GitHub Pages con Jekyll a inicios de 12021. Como no dejé bien documentado el proceso de instalación al montar el blog, luego tuve algunos inconvenientes en el mantenimiento. Así que he decidido resumir, aunque sea de forma breve, el proceso de instalación y cómo mantenerlo.  

(+ Actualización de contenido 12024.12)

## 1. Generador de sitios estáticos y web hosting
### 1-1. Página web estática vs página web dinámica
#### Página web estática
- Página que entrega al usuario exactamente los datos almacenados en el servidor
- El servidor web entrega páginas previamente guardadas según la solicitud del usuario
- El usuario ve la misma página a menos que se modifiquen los datos almacenados en el servidor
- Como solo hay que enviar el archivo solicitado, no se requieren tareas adicionales y, por lo general, la respuesta es rápida
- Al estar compuesta por archivos simples, basta con montar un servidor web, por lo que es más barata de implementar
- Muestra únicamente la información almacenada, por lo que el servicio es limitado
- La adición, modificación y eliminación de datos debe hacerla el administrador manualmente
- Estructura favorable para el rastreo por motores de búsqueda, por lo que suele ser mejor para SEO

#### Página web dinámica
- Página que procesa los datos almacenados en el servidor mediante scripts antes de entregarlos
- El servidor web interpreta la petición del usuario, procesa los datos y entrega la página generada
- El usuario ve páginas que cambian según la situación, el momento o la solicitud
- Al tener que ejecutar scripts para entregar la página, la respuesta es relativamente más lenta
- Además del servidor web, se necesita un servidor de aplicaciones, lo que añade costes de implementación
- Al combinar información de forma dinámica, permite ofrecer servicios variados
- Según la arquitectura, el usuario puede añadir, modificar o eliminar datos desde el navegador

### 1-2. Generador de sitios estáticos (SSG, Static Site Generator)
- Herramienta que genera páginas web estáticas a partir de datos en bruto (normalmente archivos de texto en formato Markdown) y plantillas predefinidas
- Sin escribir cada HTML a mano: escribes la entrada en Markdown y automatiza la construcción y el despliegue en la web
- p. ej.: Jekyll, Hugo, Gatsby, Eleventy

### 1-3. GitHub Pages
- Servicio gratuito de alojamiento de páginas web estáticas de GitHub
- Permite alojar una página principal por cuenta y crear/alojar documentación de proyectos por repositorio sin límite
- Creas un repositorio con el nombre '{username}.github.io' acorde a tu usuario de GitHub y haces Push de las páginas HTML ya construidas, o bien usas GitHub Actions para construir y desplegar
- Si tienes un dominio propio, puedes enlazarlo en la configuración y usarlo en lugar del dominio por defecto '{username}.github.io'

## 2. Elección del SSG y del tema

### 2-1. Por qué elegí Jekyll
Existen varios SSG como Jekyll, Hugo y Gatsby, pero decidí usar Jekyll. Los criterios y las razones fueron:
- ¿Minimiza pruebas y errores innecesarios para centrarme en escribir y operar el blog?
  - Jekyll es el generador de sitios estáticos oficialmente soportado por GitHub Pages. Por supuesto, también se pueden alojar Hugo, Gatsby u otros SSG en GitHub Pages, o elegir Netlify u otros hostings. Pero para un blog personal de este tamaño, la elección del SSG, la velocidad de build o el rendimiento no son críticos; preferí algo con mantenimiento sencillo y abundante documentación.
  - Jekyll además tiene un ciclo de desarrollo más largo que competidores como Hugo o Gatsby. La documentación es mejor y, cuando surgen problemas, hay muchos más recursos a consultar.
- ¿Dispone de temas y plugins variados?
  - Aunque uses un SSG, crear todas las plantillas a mano es engorroso y consume tiempo; no hace falta reinventar la rueda. Hay excelentes temas públicos: adopta el que te guste y aprovecha.
  - Como suelo usar C o Python, no domino Ruby (Jekyll) ni Go (Hugo), así que preferí apoyarme en temas y plugins ya existentes.
  - En Jekyll encontré pronto temas que me gustaban, mientras que en Hugo o Gatsby me pareció que había menos temas adecuados para blogs personales. Probablemente influye la integración con GitHub Pages, popular entre desarrolladores, y el tiempo de maduración del proyecto.
  
### 2-2. Elección del tema
#### Minimal Mistakes (12021.01 - 12022.04)
- Github Repo: <https://github.com/mmistakes/minimal-mistakes>
- Demo Page: <https://mmistakes.github.io/minimal-mistakes/>
- Tema que usé durante aproximadamente 1 año y 3 meses al inicio del blog
- Soporte de comentarios vía Disqus, Discourse, utterances, etc.
- Soporte de categorías y etiquetas
- Soporte nativo de Google Analytics
- Skins predefinidos
- Aunque luego pasé a Chirpy por su diseño más atractivo, considerando que es un blog de corte técnico, a pesar de no ser “bonito”, su diseño limpio lo hace perfectamente usable.

#### Chirpy Jekyll Theme (12022.04 - presente)
- Github Repo: <https://github.com/cotes2020/jekyll-theme-chirpy/>
- Demo Page: <https://chirpy.cotes.page/>
- Tema que uso desde el cambio realizado en abril de 12022 hasta hoy
- Soporte de categorías múltiples y etiquetas
- Soporte nativo de notación LaTeX con MathJax
- Soporte nativo de diagramas basados en Mermaid
- Soporte de comentarios vía Disqus, Giscus, etc.
- Soporte para Google Analytics y GoatCounter
- Soporte de tema claro y oscuro
- En el momento del cambio, Minimal Mistakes no soportaba de serie MathJax ni Mermaid y había que añadirlos con personalización; Chirpy los soporta de forma nativa. Aunque la personalización no era compleja, esto es una ventaja.
- Y, sobre todo, el diseño es bonito. Minimal Mistakes es limpio pero rígido, más propio de documentación técnica oficial o un portfolio. Chirpy, en cambio, no desmerece frente a plataformas comerciales como Tistory, Medium o velog.

## 3. Crear el repositorio de GitHub, compilar y desplegar
Documento esto en base al tema Chirpy Jekyll que uso actualmente (12024.06), asumiendo que Git ya está instalado.  
Consulta la [guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/) y la [página oficial de Chirpy Jekyll Theme](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### 3-1. Instalar Ruby y Jekyll
Instala Ruby y Jekyll según tu sistema operativo siguiendo la [guía oficial de instalación de Jekyll](https://jekyllrb.com/docs/installation/).

### 3-2. Crear el repositorio de GitHub
En la [página oficial de Chirpy Jekyll Theme](https://chirpy.cotes.page/posts/getting-started/#creating-a-new-site) se proponen dos métodos:
1. Importar los archivos núcleo mediante el gem "jekyll-theme-chirpy" y obtener el resto de recursos desde la plantilla [Chirpy Starter](https://github.com/cotes2020/chirpy-starter)
  - Ventaja: como veremos, aplicar upgrades de versión es sencillo.
  - Desventaja: para personalizaciones muy grandes puede resultar incómodo.
2. Hacer fork del repositorio [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) y usarlo como repositorio de tu blog
  - Ventaja: gestionas todos los archivos dentro del repositorio; es cómodo añadir funciones no soportadas por el tema ajustando el código.
  - Desventaja: para aplicar upgrades hay que hacer merge con las [etiquetas de upstream más recientes](https://github.com/cotes2020/jekyll-theme-chirpy/tags) del repositorio original; tu código personalizado puede entrar en conflicto con los cambios y tendrás que resolverlos.

Yo elegí el método 1. Chirpy es un tema muy completo: para la mayoría de usuarios apenas requiere personalización y, a 12024, sigue desarrollándose activamente. Si no vas a hacer modificaciones profundas, es más ventajoso seguir puntualmente el upstream que mantener un fork pesado. La guía oficial de Chirpy también recomienda el método 1 para la mayoría.

### 3-3. Ajustes principales
Aplica la configuración necesaria en el archivo `_config.yml`{: .filepath} del directorio raíz y en `_data/contact.yml`{: .filepath}, `_data/share.yml`{: .filepath}. Están bien comentados y las opciones son intuitivas, así que no debería haber dificultades. Como ajustes externos, quizá necesites registrar el código de verificación para vincular Google Search Console y conectar herramientas como Google Analytics o GoatCounter; no es un proceso complejo y no es el foco de esta entrada, así que omito los detalles.

### 3-4. Compilar en local
No es obligatorio, pero al escribir una nueva entrada o modificar algo quizá quieras comprobar cómo se verá. Abre una terminal en el directorio raíz del repositorio local y ejecuta:
```console
$ bundle exec jekyll s
```
Tras esperar, el sitio se compilará localmente y podrás ver el resultado en <http://127.0.0.1:4000>.

### 3-5. Desplegar
Hay dos métodos:
1. Usar GitHub Actions (si hospedas en GitHub Pages)
  - Si usas el plan gratuito de GitHub, el repositorio debe ser público
  - En la web de GitHub, ve a la pestaña *Settings* del repositorio, haz clic en *Code and automation > Pages* en la barra lateral y, en la sección **Source**, elige **GitHub Actions**
  - Tras configurar, cada nuevo Push ejecutará automáticamente el workflow de *Build and Deploy*
2. Compilar y desplegar manualmente (si usas otro hosting o autoalojamiento)
  - Compila el sitio con:
  ```console
  $ JEKYLL_ENV=production bundle exec jekyll b
  ```
  - Sube el resultado compilado del directorio `_site` al servidor

## 4. Escribir entradas
La [guía de escritura de entradas de Chirpy](https://chirpy.cotes.page/posts/write-a-new-post/) documenta bien cómo crear entradas y las opciones disponibles. Además de lo aquí descrito, ofrece muchas funciones útiles; consulta la documentación oficial cuando lo necesites. También resumí la sintaxis básica de GitHub Flavored Markdown en [otra entrada](/posts/github-markdown-syntax-summary/). Aquí dejo los puntos clave a tener en cuenta en cada publicación.

### Crear el archivo Markdown
- Formato del nombre: `YYYY-MM-DD-TITLE.md`{: .filepath}
- Ubicación: directorio `_posts`{: .filepath}

### Escribir el Front Matter
Al comienzo del archivo Markdown debes redactar un Front Matter adecuado.
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
- **title**: título de la entrada
- **description**: resumen. Si no lo escribes, se toma automáticamente el inicio del cuerpo, pero para SEO se recomienda redactar este metatag manualmente. Aproximadamente 135–160 caracteres en alfabeto latino; en coreano, 80–110.
- **date**: fecha y hora exactas de la entrada y zona horaria (opcional; si se omite, se usa la fecha de creación o modificación del archivo)
- **categories**: categorías de la entrada
- **tags**: etiquetas de la entrada
- **image**: imagen de vista previa en la parte superior
  - **path**: ruta de la imagen
  - **alt**: texto alternativo (opcional)
- **toc**: activar el índice en la barra lateral derecha; por defecto `true`
- **comments**: para forzar el uso o no de comentarios en una entrada concreta, independientemente de la configuración global
- **math**: habilitar las ecuaciones basadas en [MathJax](https://www.mathjax.org/); desactivado por defecto (`false`) por rendimiento
- **mermaid**: habilitar los diagramas basados en [Mermaid](https://github.com/mermaid-js/mermaid); desactivado por defecto (`false`)

## 5. Actualización

Asumo que elegiste el método 1 en la [3-2](#3-2-crear-el-repositorio-de-github). Si elegiste el 2, como se dijo, deberás hacer merge manual con la etiqueta upstream más reciente.

1. Edita el `Gemfile`{: .filepath} para fijar la nueva versión del gem "jekyll-theme-chirpy".
2. En upgrades mayores, pueden haber cambiado archivos núcleo y opciones de configuración no incluidas en el gem. En ese caso, revisa los cambios con la siguiente URL de la API de GitHub y aplícalos manualmente:
  ```
  https://github.com/cotes2020/chirpy-starter/compare/<older_version>...<newer_version>
  ```
