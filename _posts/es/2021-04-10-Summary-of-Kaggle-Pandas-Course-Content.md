---
title: "Resumen del curso Kaggle-Pandas"
description: >-
  He resumido el contenido del mini curso de Pandas de los cursos públicos de Kaggle.
categories: [Ciencia de Datos, Aprendizaje Automático]
tags: [Cursos de Kaggle, Pandas]
toc: true
toc_sticky: true
---

# Pandas
Resuelve breves desafíos prácticos para perfeccionar tus habilidades de manipulación de datos.

## Lección 1. Crear, Leer y Escribir
### Importar pandas
```python
import pandas as pd
```
Pandas tiene dos objetos centrales: **DataFrame** y **Series**.

### DataFrame
Un DataFrame es una tabla. Contiene una matriz de entradas individuales, cada una de las cuales tiene un valor específico y corresponde a una fila y una columna. Las entradas de un DataFrame no tienen que ser necesariamente números enteros.
```python
pd.DataFrame({'Bob': ['Me gustó.', 'Fue horrible.'], 'Sue': ['Bastante bueno.', 'Insípido.']})
```
La declaración de un DataFrame se hace en formato de diccionario de Python. Las claves son los nombres de las columnas y los valores son listas de elementos a incluir.

Normalmente, al declarar un DataFrame, las etiquetas de las columnas se asignan al nombre de esa columna, pero a las etiquetas de las filas se les asignan enteros 0, 1, 2... Si es necesario, se pueden especificar manualmente las etiquetas de las filas. La lista de etiquetas de filas en un DataFrame se llama **Index**, y se puede especificar usando el parámetro ```index```.
```python
pd.DataFrame({'Bob': ['Me gustó.', 'Fue horrible.'], 
              'Sue': ['Bastante bueno.', 'Insípido.']},
             index=['Producto A', 'Producto B'])
```

### Series
Una Series es una secuencia de valores de datos.
```python
pd.Series([1, 2, 3, 4, 5])
```
Una Series es esencialmente una columna única de un DataFrame. Por lo tanto, también se puede especificar un índice. Sin embargo, la diferencia es que tiene un 'nombre', ```name```, en lugar de un 'nombre de columna'.
```python
pd.Series([30, 35, 40], index=['Ventas 2015', 'Ventas 2016', 'Ventas 2017'], name='Producto A')
```
Las Series y los DataFrames están estrechamente relacionados. Puede ser útil pensar en un DataFrame simplemente como un conjunto de Series.

### Leer archivos de datos
En muchos casos, en lugar de crear datos directamente, se utilizan datos existentes. Los datos pueden estar almacenados en varios formatos, pero el más básico es el archivo CSV. El contenido de un archivo CSV suele ser así:
```
Producto A,Producto B,Producto C,
30,21,9,
35,34,1,
41,11,11
```
Es decir, un archivo CSV es una tabla donde cada valor está separado por comas (comma). Por eso se llama "Comma-Separated Values", CSV.

Para cargar datos en formato CSV en un DataFrame, se utiliza la función ```pd.read_csv()```.

Se puede usar el atributo ```shape``` para verificar el tamaño del DataFrame.

Se puede usar el comando ```head()``` para ver las primeras cinco filas del DataFrame.

La función ```pd.read_csv()``` tiene más de 30 parámetros. Por ejemplo, si el archivo CSV que se quiere cargar incluye su propio índice, se puede especificar el valor del parámetro ```index_col``` para usar esa columna como índice en lugar de que pandas asigne automáticamente un índice.

### Escribir datos
Se puede exportar un DataFrame a un archivo CSV usando el método ```to_csv()```. Se usa de la siguiente manera:
```python
(nombre del DataFrame).to_csv("(ruta del archivo CSV)")
```

## Lección 2. Indexación, Selección y Asignación
Seleccionar valores específicos para usar de un DataFrame o Series de pandas es un paso que se da en casi todas las tareas que involucran datos.