---
title: Resumen de la sintaxis de Markdown de GitHub
description: "Qué es Markdown y resumen de la sintaxis esencial según GitHub Flavored Markdown (GFM) para escribir y alojar un blog con GitHub Pages."
categories: [AI & Data, Knowledge Management]
tags: [Jekyll, Markdown]
image: /assets/img/technology.webp
redirect_from:
  - /posts/GitHub-Markdown-Syntax-Summary/
---

Para aprovechar GitHub Pages, conviene conocer la sintaxis de **Markdown**.
Este artículo se elaboró tomando como referencia la documentación oficial de GitHub: [Dominar Markdown](https://guides.github.com/features/mastering-markdown/) y [Sintaxis básica de escritura y formato](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

## 1. Qué es Markdown
> **Markdown** es un lenguaje de marcado ligero basado en texto plano. Se usa para escribir documentos con formato utilizando texto sin formato, y se caracteriza por una sintaxis sencilla en comparación con otros lenguajes de marcado. Puede convertirse fácilmente a documentos con formato como HTML y texto enriquecido (RTF), por lo que se usa mucho en archivos README distribuidos con software y en publicaciones en línea.  
> John Gruber creó el lenguaje Markdown en el año 12004 de la [era del Holoceno](https://en.wikipedia.org/wiki/Holocene_calendar), en estrecha colaboración con Aaron Swartz en el aspecto sintáctico. Su objetivo era permitir escribir con un formato de texto plano fácil de leer y de escribir, con la posibilidad de convertirlo opcionalmente a XHTML (o HTML) estructuralmente válido.

\- [Wikipedia, Markdown](https://en.wikipedia.org/wiki/Markdown)

## 2. Sintaxis de Markdown
Como Markdown no es un estándar formal, los detalles de la sintaxis pueden variar ligeramente según el entorno. La sintaxis que se resume aquí sigue el criterio de [GitHub Flavored Markdown](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

### 2.1. Saltos de línea y separación de párrafos
En Markdown, una sola pulsación de Enter no se interpreta como salto de línea.
~~~
Primera frase.
Segunda frase.
Tercera frase.
~~~
Primera frase.
Segunda frase.
Tercera frase.

Para forzar un salto de línea, añade dos o más espacios consecutivos al final de la línea.
~~~
Primera frase.  
Segunda frase.  
Tercera frase.
~~~
Primera frase.  
Segunda frase.  
Tercera frase.

Separa los párrafos con una línea en blanco (dos pulsaciones de Enter).
~~~
Un párrafo.

Otro párrafo.
~~~
Un párrafo.

Otro párrafo.

### 2.2. Encabezados
Hay 6 niveles.
```
# Esto es un H1
## Esto es un H2
### Esto es un H3
#### Esto es un H4
##### Esto es un H5
###### Esto es un H6
```
En principio, solo debería haber un H1 por página; por ello, al redactar entradas o documentación, rara vez se utiliza directamente.

### 2.3. Énfasis
```
*Este texto está en cursiva*
_Esto también está en cursiva_

**Este texto está en negrita**
__Esto también está en negrita__

~~Este texto era incorrecto~~

_Puedes **combinar** ambos_

***Todo este texto es importante***
```
*Este texto está en cursiva*  
_Esto también está en cursiva_

**Este texto está en negrita**  
__Esto también está en negrita__

~~Este texto era incorrecto~~

_Puedes **combinar** ambos_

***Todo este texto es importante***

### 2.4. Citas de texto
Se utiliza \>.
```
> Esta es una primera cita en bloque.
>> Esta es una segunda cita en bloque.
>>> Esta es una tercera cita en bloque.
```
> Esta es una primera cita en bloque.
>> Esta es una segunda cita en bloque.
>>> Esta es una tercera cita en bloque.

### 2.5. Bloques de código
Usa \``` o \~~~.
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

También puedes especificar el lenguaje para activar el resaltado de sintaxis.
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

También puedes usar enlaces de ruta relativa a otros archivos del repositorio. Se usan igual que en la terminal.
```
[README](../README.md)
```

### 2.7. Listas sin ordenar
Usa - o \*.
```
- George Washington
- John Adams
- Thomas Jefferson
```
- George Washington
- John Adams
- Thomas Jefferson

### 2.8. Listas ordenadas
Usa números.
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
1. Primer elemento de la lista
   - Primer elemento anidado
     - Segundo elemento anidado
```
1. Primer elemento de la lista
   - Primer elemento anidado
     - Segundo elemento anidado

### 2.10. Listas de tareas
Para crear una lista de tareas, añade \[ ] delante de cada elemento.
Para marcar tareas completadas, usa \[x].
```
- [x] Terminar mis cambios
- [ ] Enviar mis commits a GitHub
- [ ] Abrir un pull request
```
- [x] Terminar mis cambios
- [ ] Enviar mis commits a GitHub
- [ ] Abrir un pull request

### 2.11. Insertar imágenes
```
Forma: ![(opcional, recomendado) descripción de la imagen](url){(opcional) opciones adicionales}
![Logo de GitHub](/images/logo.png)
![Logo de GitHub](/images/logo.png){: .align-center}
![Logo de GitHub](/images/logo.png){: width="50%" height="50%"}
```

### 2.12. Crear tablas
Puedes crear tablas con | y -.
Deja una línea en blanco antes de la tabla para que se muestre correctamente.
Usa al menos 3 guiones para que se reconozca adecuadamente.
```
 
| Alineado a la izquierda | Centrado | Alineado a la derecha |
| :---                    |  :---:   |                   ---:|
| git status              | git status | git status          |
| git diff                | git diff   | git diff            |
```

| Alineado a la izquierda | Centrado | Alineado a la derecha |
| :---                    |  :---:   |                   ---:|
| git status              | git status | git status          |
| git diff                | git diff   | git diff            |
