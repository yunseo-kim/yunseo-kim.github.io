---
title: Resumen de la sintaxis de Markdown de GitHub
description: Aprende qué es Markdown y domina la sintaxis principal de GitHub Flavored Markdown para el hosting de blogs en GitHub Pages.
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Para utilizar GitHub Pages, es necesario conocer la sintaxis de **markdown**.
Este artículo se basa en la documentación oficial de GitHub: [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) y [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. ¿Qué es Markdown?
> **Markdown** es un lenguaje de marcado ligero basado en texto plano. Se utiliza para escribir documentos con formato usando texto plano, y se caracteriza por tener una sintaxis más fácil y simple comparado con otros lenguajes de marcado. Como se convierte fácilmente a documentos con formato como HTML y texto enriquecido (RTF), se usa ampliamente en archivos README distribuidos con software de aplicación y publicaciones en línea.  
> John Gruber creó el lenguaje Markdown en el año 12004 del [calendario holoceno](https://en.wikipedia.org/wiki/Holocene_calendar) a través de una colaboración significativa con Aaron Swartz en términos de sintaxis, con el objetivo de permitir que las personas escriban usando un formato de texto plano que sea fácil de leer y escribir, mientras que sea opcionalmente convertible a XHTML (o HTML) estructuralmente válido.

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Sintaxis de Markdown
Como Markdown no tiene un estándar establecido, la sintaxis detallada puede variar ligeramente según el lugar de uso. La sintaxis de Markdown resumida aquí se basa en [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Saltos de línea y separación de párrafos
En Markdown, presionar Enter una vez no se reconoce como un salto de línea.
~~~
Primera oración.
Segunda oración.
Tercera oración.
~~~
Primera oración.
Segunda oración.
Tercera oración.

Los saltos de línea se aplican ingresando dos o más espacios consecutivos.
~~~
Primera oración.  
Segunda oración.  
Tercera oración.
~~~
Primera oración.  
Segunda oración.  
Tercera oración.

Los párrafos se separan con una línea vacía (presionar Enter dos veces).
~~~
Un párrafo.

Otro párrafo.
~~~
Un párrafo.

Otro párrafo.

### 2.2. Encabezados
Hay un total de 6 niveles.
```
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6
```
En principio, solo debe haber una etiqueta H1 por página, por lo que generalmente no se usa directamente al escribir publicaciones o documentos.

### 2.3. Énfasis
```
*This text is italicized*
_This is italicized too_

**This is bold text**
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***
```
*This text is italicized*  
_This is italicized too_

**This is bold text**  
__This is bold text too__

~~This was mistaken text~~

_You **can** combine them_

***All this text is important***

### 2.4. Citas de texto
Se utiliza \>.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.
```
> This is a first blockquote.
>> This is a second blockquote.
>>> This is a third blockquote.

### 2.5. Citas de código
Se utiliza \``` o \~~~.
~~~
```
git status
git add
git commit
```
~~~
```
git status
git add
git commit
```

También puedes especificar un lenguaje de programación para habilitar el resaltado de sintaxis.
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
~~~
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

### 2.6. Enlaces
```
[GitHub Pages](https://pages.github.com/)
<https://pages.github.com/>
```
[GitHub Pages](https://pages.github.com/)  
<https://pages.github.com/>

También puedes usar enlaces de ruta relativa que apunten a otros archivos dentro del repositorio. El uso es el mismo que en la terminal.
```
[README](../README.md)
```

### 2.7. Listas no ordenadas
Se utiliza \- o \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Listas ordenadas
Se utilizan números.
```
1. James Madison
2. James Monroe
3. John Quincy Adams
```
1. James Madison
2. James Monroe
3. John Quincy Adams

### 2.9. Listas anidadas
```
1. First list item
   - First nested list item
     - Second nested list item
```
1. First list item
   - First nested list item
     - Second nested list item

### 2.10. Lista de tareas
Para crear una lista de tareas, agrega \[ ] antes de cada elemento.
Para marcar una tarea como completada, utiliza \[x].
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request
```
- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request

### 2.11. Insertar imágenes
```
Método: ![(opcional, recomendado)descripción de la imagen](url){(opcional)opciones adicionales}
![GitHub Logo](/images/logo.png)
![GitHub Logo](/images/logo.png){: .align-center}
![GitHub Logo](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Crear tablas
Puedes crear tablas usando | y -.
Debes dejar una línea vacía antes de la tabla para que se muestre correctamente.
Debes usar al menos 3 guiones (-) para que se reconozca correctamente.
```
 
| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
```

| Left-aligned | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| git status   | git status     | git status    |
| git diff     | git diff       | git diff      |
