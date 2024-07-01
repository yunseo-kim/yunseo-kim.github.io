---
title: "Principios para escribir buen código"
description: >-
  Exploramos la necesidad de escribir buen código y los principios generales para hacerlo.
categories:
  - Programming
tags:
  - Coding
  - PS/CP
---
## La necesidad de escribir buen código
Si nos apresuramos a escribir código rápidamente solo para la implementación inmediata, la [deuda técnica](/posts/Technical-debt/) puede crecer a niveles inmanejables y causar problemas de mantenimiento en el futuro. Por lo tanto, al llevar a cabo un proyecto de desarrollo, es innecesario decir que es importante escribir buen código que sea legible y fácil de mantener desde el principio.

En el caso de la resolución de problemas algorítmicos (PS, Problem Solving) o la programación competitiva (CP, Competitive Programming), generalmente no se reutiliza el código utilizado para resolver problemas después de que termina la resolución del problema o la competencia, y especialmente en el caso de CP, hay un límite de tiempo, por lo que algunos argumentan que la implementación rápida es más importante que escribir buen código. Para responder a esta pregunta, es necesario pensar en por qué haces PS/CP y qué dirección buscas.

Personalmente, creo que los puntos que se pueden aprender a través de PS/CP son los siguientes:
- Se pueden usar y aprender diversos algoritmos y estructuras de datos en el proceso de resolver problemas dentro de los límites de tiempo de ejecución y memoria dados, y a través de esto, se puede desarrollar una intuición sobre qué algoritmos y estructuras de datos usar en situaciones específicas cuando se lleva a cabo un proyecto real
- Después de escribir y enviar el código, se puede recibir retroalimentación objetiva inmediata sobre si es correcto/incorrecto, el tiempo de ejecución y el uso de memoria, por lo que se puede practicar escribir código preciso rápida y hábilmente sin perder nada
- Se puede ver el código escrito por otros expertos y compararlo con el propio código para encontrar áreas de mejora
- En comparación con los proyectos de desarrollo reales, se escribe repetidamente código de escala más pequeña que realiza funciones similares, por lo que (especialmente cuando se practica PS solo) se puede practicar escribir código conciso y bueno prestando atención a los detalles sin estar atado a plazos de entrega, etc.

Por supuesto, puede haber casos en los que PS/CP se disfrute simplemente como un pasatiempo, pero si, como yo, haces PS/CP para mejorar indirectamente tus habilidades de programación, la "práctica de escribir buen código" mencionada al final es una gran ventaja, no menos importante que las tres anteriores. Esto se debe a que escribir buen código no es algo que ocurra naturalmente desde el principio, sino que requiere práctica constante a través de repetición. Además, el código complejo y difícil de leer es difícil de depurar y no es fácil de escribir con precisión de una sola vez, por lo que si se pierde tiempo en depuración ineficiente, a menudo no se puede implementar tan rápidamente. Aunque PS/CP es muy diferente del trabajo real, por las razones mencionadas anteriormente, ignorar completamente la escritura de buen código y apresurarse solo por la implementación inmediata es poner el carro delante de los bueyes, por lo que personalmente trato de escribir código conciso y eficiente incluso en PS/CP.

## Principios para escribir buen código
Ya sea código escrito en competencias o código escrito en el trabajo real, las condiciones para considerarlo buen código no son muy diferentes. En este artículo, trataremos los principales principios para escribir buen código en general. Sin embargo, en PS/CP puede haber áreas donde se comprometa relativamente en comparación con el trabajo real para una implementación rápida, y en estos casos se mencionará por separado en el artículo.

### Escribir código conciso
> "KISS (Keep It Simple, Stupid)"
- Cuanto más corto y conciso sea el código, naturalmente habrá menos preocupación por errores tipográficos o errores simples, y la depuración será más fácil
- Escribir de manera que se pueda interpretar fácilmente sin comentarios adicionales siempre que sea posible, y agregar explicaciones detalladas con comentarios solo cuando sea realmente necesario. Es preferible mantener la estructura del código concisa en lugar de depender de comentarios.
- Si se escriben comentarios, hacerlo de manera clara y concisa
- Limitar el número de argumentos pasados a una función a tres o menos, y si se necesitan más argumentos para pasar juntos, agruparlos en un solo objeto para pasarlos
- Si la profundidad (depth) de las declaraciones condicionales se vuelve doble o triple, disminuye la legibilidad, por lo que se debe evitar aumentar la profundidad de las declaraciones condicionales tanto como sea posible.
  ej) El código de abajo que utiliza la cláusula de guarda (Guard Clause) es más favorable en términos de legibilidad que el código de arriba

  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if user:
          token = await user_service.get_token(user)
  
          if token :
              if token.purpose == 'reset':
                  return True
      return False
  ```
  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if not user:
          return False
    
      token = await user_service.get_token(user)
  
      if not token or token.purpose != 'reset':
          return False
    
    return True
  ```
- Sin embargo, en PS/CP, a veces se usa el truco de usar macros de C/C++ para reducir aún más la longitud del código y escribirlo rápidamente. Aunque es útil usarlo ocasionalmente en competencias con tiempo limitado, es un método que solo funciona en PS/CP y generalmente se debe evitar el uso de macros en C++.
  ej)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularización del código
> "DRY (Don't Repeat Yourself)"
- Si se usa el mismo código repetidamente, separar esa parte en una función o clase para reutilizarla
- La reutilización activa del código a través de la modularización mejora la legibilidad y facilita el mantenimiento cuando es necesario modificar el código más adelante, ya que solo se necesita modificar la función o clase correspondiente una vez
- En principio, lo ideal es que una función realice solo una funcionalidad y no haga dos o más cosas. Sin embargo, el código escrito en PS/CP suele ser un programa de pequeña escala que realiza funciones simples, por lo que hay límites en la reutilización, y debido a las limitaciones de tiempo, puede ser difícil seguir los principios tan estrictamente como en el trabajo real.

### Utilización de bibliotecas estándar
> "Don't reinvent the wheel"
- En la etapa de estudio de algoritmos o estructuras de datos, es útil implementar directamente estructuras de datos como colas o pilas, algoritmos de ordenación, etc., para entender los principios, pero si no es así, es mejor utilizar activamente las bibliotecas estándar
- Las bibliotecas estándar ya han sido utilizadas y verificadas innumerables veces, y están bien optimizadas, por lo que son más eficientes que implementarlas directamente de nuevo
- Como se pueden usar bibliotecas ya existentes, no es necesario perder tiempo implementando directamente código que realiza la misma función innecesariamente, y es fácil para otros miembros del equipo entender el código escrito durante la colaboración

### Uso de nomenclatura consistente y clara
> "Follow standard conventions"
- Usar nombres de variables y funciones que no sean ambiguos
- Generalmente, cada lenguaje de programación tiene sus propias convenciones de nomenclatura, así que aprende las convenciones de nomenclatura utilizadas en la biblioteca estándar del lenguaje que estás usando y aplícalas consistentemente al declarar clases, funciones, variables, etc.
- Nombrar de manera que quede claro qué función realiza cada variable, función y clase, y si es de tipo booleano, en qué condición devuelve verdadero (True)

### Almacenar todos los datos normalizados
- Procesar todos los datos en un formato consistente y normalizado
- Si los mismos datos tienen dos o más formatos, pueden ocurrir errores sutiles difíciles de detectar, como ligeras diferencias en la representación de cadenas o diferencias en los valores hash
- Al almacenar y procesar datos como zonas horarias, cadenas, etc., se deben convertir a un formato estándar único como UTC, codificación UTF-8, etc., tan pronto como se reciban o calculen. Es mejor realizar la normalización desde el principio en el constructor de la clase que representa los datos o realizar la normalización inmediatamente en la función que recibe los datos.

### Separar la lógica del código y los datos
- No poner datos que no estén relacionados con la lógica del código directamente en las declaraciones condicionales, sino separarlos en una tabla separada
  ej) Es preferible escribir como el código de abajo en lugar del código de arriba.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ```c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ```