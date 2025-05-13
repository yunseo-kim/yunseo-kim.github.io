---
title: Resumen del curso Kaggle-Pandas
description: Se resume el contenido del mini curso de Pandas de los cursos abiertos de Kaggle.
categories: [AI & Data, Machine Learning]
tags: [Kaggle Courses, Pandas]
image: /assets/img/technology.webp
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
Un DataFrame es una tabla. Contiene una matriz de entradas individuales, cada una con un valor específico y correspondiente a una fila y columna. Las entradas de un DataFrame no tienen que ser necesariamente números enteros.
```python
pd.DataFrame({'Bob': ['Me gustó.', 'Fue horrible.'], 'Sue': ['Bastante bueno.', 'Insípido.']})
```
Los DataFrames se declaran en formato de diccionario de Python. Las claves son los nombres de las columnas y los valores son listas con los elementos a incluir.

Normalmente, al declarar un DataFrame se asignan etiquetas a las columnas, pero a las filas se les asignan enteros 0, 1, 2... Si es necesario, se pueden especificar manualmente las etiquetas de las filas. La lista de etiquetas de filas en un DataFrame se llama **Índice** y se puede especificar usando el parámetro ```index```.
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
Una Series es esencialmente como una sola columna de un DataFrame. Por lo tanto, también se puede especificar un índice. La diferencia es que tiene un "nombre" (```name```) en lugar de un "nombre de columna".
```python
pd.Series([30, 35, 40], index=['Ventas 12015', 'Ventas 12016', 'Ventas 12017'], name='Producto A')
```
Las Series y los DataFrames están estrechamente relacionados. Puede ser útil pensar en un DataFrame simplemente como un conjunto de Series.

### Leer archivos de datos
En muchos casos, en lugar de crear datos directamente, se importan datos existentes. Los datos pueden estar almacenados en varios formatos, siendo el más básico el archivo CSV. El contenido de un archivo CSV suele ser así:
```
Producto A,Producto B,Producto C,
30,21,9,
35,34,1,
41,11,11
```
Es decir, un archivo CSV es una tabla que separa cada valor con comas (de ahí el nombre "Comma-Separated Values", CSV).

Para cargar datos en formato CSV como un DataFrame, se usa la función ```pd.read_csv()```.

Se puede verificar el tamaño de un DataFrame usando el atributo ```shape```.

Se pueden ver las primeras cinco filas de un DataFrame usando el comando ```head()```.

La función ```pd.read_csv()``` tiene más de 30 parámetros. Por ejemplo, si el archivo CSV que se quiere cargar incluye su propio índice, se puede especificar el valor del parámetro ```index_col``` para usar esa columna como índice en lugar de que pandas asigne automáticamente uno.

### Escribir datos
Se puede exportar un DataFrame a un archivo CSV usando el método ```to_csv()```. Se usa de la siguiente manera:
```python
(nombre del DataFrame).to_csv("(ruta del archivo CSV)")
```

## Lección 2. Indexación, Selección y Asignación
Seleccionar valores específicos para usar de un DataFrame o Series de pandas es un paso que se da en casi todas las operaciones que utilizan datos.
