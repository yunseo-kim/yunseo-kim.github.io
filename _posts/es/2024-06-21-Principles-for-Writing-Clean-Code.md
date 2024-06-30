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
Si nos apresuramos a escribir código rápidamente solo para la implementación inmediata, la deuda técnica puede crecer a niveles inmanejables, causando problemas de mantenimiento en el futuro. Por lo tanto, es innecesario decir que es importante escribir código legible y fácil de mantener desde el principio al desarrollar un proyecto.

En el caso de la resolución de problemas algorítmicos (PS, Problem Solving) o la programación competitiva (CP, Competitive Programming), generalmente no se reutiliza el código utilizado para resolver problemas después de que termina la resolución o la competencia. Especialmente en CP, debido a las limitaciones de tiempo, algunos argumentan que la implementación rápida es más importante que escribir buen código. Para responder a esta pregunta, es necesario considerar para qué se hace PS/CP y qué dirección se busca.

Personalmente, creo que los puntos que se pueden aprender a través de PS/CP son los siguientes:
- Se pueden usar y aprender diversos algoritmos y estructuras de datos en el proceso de resolver problemas dentro de los límites de tiempo de ejecución y memoria dados, lo que ayuda a desarrollar intuición sobre qué algoritmos y estructuras de datos usar en situaciones específicas en proyectos reales.
- Se puede recibir retroalimentación objetiva inmediata sobre la corrección/incorrección, el tiempo de ejecución y el uso de memoria después de escribir y enviar código, lo que permite practicar la escritura de código preciso de manera rápida y competente sin omitir nada.
- Se puede comparar el código propio con el de otros expertos y encontrar áreas de mejora.
- Al escribir repetidamente código de escala más pequeña que realiza funciones similares en comparación con proyectos de desarrollo reales, se puede practicar la escritura de código conciso y bueno prestando atención a los detalles sin estar atado a plazos (especialmente cuando se practica PS solo).

Aunque puede haber casos en los que PS/CP se disfrute simplemente como un pasatiempo, si, como yo, se hace PS/CP para mejorar indirectamente las habilidades de programación, la "práctica de escribir buen código" es una ventaja tan grande como las tres anteriores. Esto se debe a que escribir buen código no es algo que ocurra naturalmente desde el principio, sino que requiere práctica constante y repetida. Además, el código complejo y difícil de leer es difícil de depurar y no es fácil de escribir correctamente de una vez, por lo que a menudo se pierde tiempo en depuración ineficiente y no se logra una implementación tan rápida. Aunque PS/CP es muy diferente del trabajo real, por las razones mencionadas anteriormente, ignorar completamente la escritura de buen código y apresurarse solo por la implementación inmediata es contraproducente, por lo que personalmente trato de escribir código conciso y eficiente incluso en PS/CP.

## Principios para escribir buen código
Ya sea código escrito en competencias o en el trabajo real, las condiciones para considerarlo buen código no son muy diferentes. Este artículo trata sobre los principales principios para escribir buen código en general. Sin embargo, puede haber áreas donde se hagan compromisos en PS/CP para una implementación rápida en comparación con el trabajo real, y estos casos se mencionarán específicamente en el artículo.

### Escribir código conciso
> "KISS (Keep It Simple, Stupid)"
- Cuanto más corto y conciso sea el código, naturalmente habrá menos preocupaciones por errores tipográficos o errores simples, y la depuración será más fácil.
- Escribir de manera que se pueda interpretar fácilmente sin comentarios adicionales siempre que sea posible, y agregar explicaciones detalladas con comentarios solo cuando sea realmente necesario. Es preferible mantener la estructura del código concisa en lugar de depender de comentarios.
- Si se escriben comentarios, hacerlo de manera clara y concisa.
- Limitar el número de argumentos pasados a una función a tres o menos, y si se necesitan más argumentos, agruparlos en un solo objeto para pasarlos.
- La profundidad de las declaraciones condicionales que se vuelven dobles o triples reduce la legibilidad, por lo que se debe evitar aumentar la profundidad de las declaraciones condicionales tanto como sea posible.
  ej) El código de abajo que utiliza la cláusula de guarda (Guard Clause) es más favorable en términos de legibilidad que el código de arriba.

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
- Sin embargo, en PS/CP, a veces se usa el truco de utilizar macros de C/C++ para reducir aún más la longitud del código y escribirlo rápidamente. Aunque es útil usarlo ocasionalmente en competencias con tiempo limitado, es un método que solo funciona en PS/CP y generalmente se debe evitar el uso de macros en C++.
  ej)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularización del código
> "DRY (Don't Repeat Yourself)"
- Si se usa el mismo código repetidamente, separar esa parte en funciones o clases para reutilizarla.
- La reutilización activa del código a través de la modularización mejora la legibilidad y facilita el mantenimiento, ya que solo se necesita modificar la función o clase correspondiente si es necesario realizar cambios en el código en el futuro.
- En principio, es ideal que una función realice solo una tarea y no más de dos. Sin embargo, el código escrito en PS/CP suele ser un programa de pequeña escala que realiza funciones simples, por lo que hay limitaciones en la reutilización, y debido a las restricciones de tiempo, puede ser difícil seguir los principios tan estrictamente como en el trabajo real.

### Utilización de bibliotecas estándar
> "Don't reinvent the wheel"
- En la etapa de estudio de algoritmos o estructuras de datos, es útil implementar directamente estructuras de datos como colas o pilas y algoritmos de ordenamiento para entender los principios, pero si ese no es el caso, es mejor utilizar activamente las bibliotecas estándar.
- Las bibliotecas estándar ya han sido utilizadas y verificadas innumerables veces, y están bien optimizadas, por lo que son más eficientes que implementarlas directamente nuevamente.
- Como se pueden usar bibliotecas existentes, no es necesario perder tiempo implementando directamente código con la misma funcionalidad innecesariamente, y es más fácil para otros miembros del equipo entender el código escrito durante la colaboración.

### Uso de nomenclatura consistente y clara
> "Follow standard conventions"
- Usar nombres de variables y funciones que no sean ambiguos.
- Generalmente, cada lenguaje de programación tiene sus propias convenciones de nomenclatura, así que es importante familiarizarse con las convenciones de nomenclatura utilizadas en la biblioteca estándar del lenguaje que se está utilizando y aplicarlas consistentemente al declarar clases, funciones, variables, etc.
- Nombrar de manera que quede claro qué función realiza cada variable, función y clase, y en el caso de tipos booleanos, en qué condiciones devuelven verdadero (True).

### Normalizar todos los datos antes de almacenarlos
- Procesar todos los datos normalizándolos en un formato consistente.
- Si los mismos datos tienen más de un formato, pueden ocurrir errores sutiles difíciles de detectar, como ligeras diferencias en la representación de cadenas o valores hash diferentes.
- Al almacenar y procesar datos como zonas horarias, cadenas, etc., se deben convertir a un formato estándar único como UTC, codificación UTF-8, etc., tan pronto como se reciban o calculen. Es mejor realizar la normalización desde el principio en el constructor de la clase que representa los datos o en la función que recibe los datos.

### Separar la lógica del código y los datos
- No incluir datos no relacionados con la lógica del código directamente en las declaraciones condicionales, sino separarlos en tablas separadas.
  ej) Es preferible escribir el código como el de abajo en lugar del de arriba.

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