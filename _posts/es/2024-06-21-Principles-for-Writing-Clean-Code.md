---
title: Principios para escribir buen código
description: Exploramos la necesidad de escribir buen código y los principios generales para lograrlo.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
---
## La necesidad de escribir buen código
Si nos centramos únicamente en escribir código rápidamente para la implementación inmediata, la [deuda técnica](/posts/Technical-debt/) puede crecer hasta niveles inmanejables, causando problemas de mantenimiento en el futuro. Por lo tanto, es indiscutiblemente importante escribir código legible y fácil de mantener desde el principio cuando se desarrolla un proyecto.

En el caso de la resolución de problemas algorítmicos (PS, Problem Solving) o la programación competitiva (CP, Competitive Programming), generalmente no se reutiliza el código después de resolver el problema o terminar la competencia. Especialmente en CP, donde hay límites de tiempo, algunos argumentan que la implementación rápida es más importante que escribir buen código. Para responder a esta cuestión, es necesario reflexionar sobre por qué uno practica PS/CP y qué dirección busca.

En mi opinión, los beneficios que se pueden obtener a través de PS/CP son los siguientes:
- Se pueden aprender y practicar diversos algoritmos y estructuras de datos al resolver problemas dentro de los límites de tiempo de ejecución y memoria establecidos, lo que ayuda a desarrollar intuición sobre qué algoritmos y estructuras de datos utilizar en situaciones específicas en proyectos reales
- Al escribir y enviar código, se recibe retroalimentación objetiva inmediata sobre si es correcto o no, el tiempo de ejecución y el uso de memoria, lo que permite practicar la escritura de código preciso de manera rápida y competente
- Se puede comparar el código propio con el de programadores más experimentados para encontrar áreas de mejora
- A diferencia de los proyectos de desarrollo reales, se escribe repetidamente código de funcionalidad similar pero de menor escala, lo que permite (especialmente cuando se practica PS individualmente) practicar la escritura de código conciso y de calidad prestando atención a los detalles sin la presión de plazos

Aunque algunas personas disfrutan de PS/CP simplemente como hobby, si se practica indirectamente para mejorar las habilidades de programación, el "ejercicio de escribir buen código" es una ventaja tan importante como las tres anteriores. Escribir buen código no es algo que surja naturalmente desde el principio, sino que requiere práctica constante. Además, el código complejo y difícil de leer es difícil de depurar y no es fácil escribirlo correctamente a la primera, lo que puede llevar a perder tiempo en depuración ineficiente sin lograr una implementación rápida. Aunque PS/CP difiere significativamente del trabajo profesional, ignorar completamente la escritura de buen código y centrarse solo en la implementación inmediata es contraproducente por las razones mencionadas, por lo que personalmente creo que es mejor escribir código conciso y eficiente incluso en PS/CP.

> Comentario añadido en 12024.12:  
> Viendo la tendencia actual, a menos que se estudie informática y se dedique al desarrollo como profesión, para quienes usan la programación como herramienta para análisis numérico o interpretación de datos experimentales, probablemente sea mejor utilizar activamente herramientas de IA como GitHub Copilot, Cursor o Windsurf para ahorrar tiempo y dedicarlo a estudiar otras cosas. Si se disfruta de PS/CP como hobby, no hay razón para desalentarlo, pero invertir tiempo y esfuerzo en PS/CP para practicar la escritura de código parece tener ahora una relación costo-beneficio mucho menor. Incluso en profesiones de desarrollo, preveo que la importancia de las pruebas de codificación como examen de ingreso probablemente disminuirá considerablemente.
{: .prompt-warning }

## Principios para escribir buen código
Ya sea código escrito para competencias o para trabajo profesional, las condiciones que definen un buen código no son muy diferentes. Este artículo aborda los principios fundamentales para escribir buen código en general. Sin embargo, en PS/CP puede haber áreas donde se hacen compromisos relativos para lograr una implementación rápida en comparación con el entorno profesional; estos casos se mencionarán específicamente.

### Escribir código conciso
> "KISS (Keep It Simple, Stupid)"

- Cuanto más corto y conciso sea el código, naturalmente hay menos preocupación por errores tipográficos o bugs simples, y la depuración es más fácil
- Escribir código que pueda interpretarse fácilmente sin comentarios adicionales y añadir comentarios solo cuando sea realmente necesario para explicaciones detalladas. Es preferible mantener la estructura del código concisa en lugar de depender de comentarios
- Si se escriben comentarios, hacerlos claros y concisos
- Limitar los argumentos de una función a tres o menos, y si se necesitan más, agruparlos en un solo objeto
- La profundidad (depth) de las declaraciones condicionales que se vuelven dobles o triples reduce la legibilidad, por lo que se debe evitar aumentar la profundidad de las condicionales cuando sea posible.  
  Por ejemplo: El código siguiente que utiliza cláusulas de guarda (Guard Clause) es más legible que el anterior

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
- Sin embargo, en PS/CP, a veces se utilizan trucos como las macros de C/C++ para reducir aún más la longitud del código y escribirlo más rápido. Esto puede ser útil en competencias con tiempo limitado, pero es un método que solo funciona en PS/CP y generalmente se debe evitar el uso de macros en C++.  
  Por ejemplo:  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularización del código
> "DRY (Don't Repeat Yourself)"

- Cuando se usa el mismo código repetidamente, separar esa parte en funciones o clases para reutilización
- La modularización para reutilizar activamente el código mejora la legibilidad y facilita el mantenimiento, ya que solo se necesita modificar la función o clase una vez cuando se requieren cambios
- En principio, lo ideal es que una función realice una sola tarea y no más de una. Sin embargo, en PS/CP, el código suele ser de pequeña escala que realiza funciones simples, por lo que hay límites en la reutilización, y debido a las restricciones de tiempo, puede ser difícil seguir los principios tan estrictamente como en el entorno profesional.

### Utilización de bibliotecas estándar
> "Don't reinvent the wheel"

- Aunque es útil implementar estructuras de datos como colas y pilas, o algoritmos de ordenación para entender sus principios durante la fase de estudio, es mejor utilizar activamente las bibliotecas estándar en otros casos
- Las bibliotecas estándar ya han sido ampliamente utilizadas y verificadas, y están bien optimizadas, lo que las hace más eficientes que implementarlas desde cero
- Usar bibliotecas existentes evita perder tiempo implementando código con la misma funcionalidad, y facilita que otros miembros del equipo entiendan el código durante la colaboración

### Uso de nomenclatura coherente y clara
> "Follow standard conventions"

- Usar nombres de variables y funciones que no sean ambiguos
- Cada lenguaje de programación suele tener sus propias convenciones de nomenclatura, por lo que es importante aprender y aplicar consistentemente las convenciones utilizadas en la biblioteca estándar del lenguaje al declarar clases, funciones y variables
- Nombrar de manera que quede claro qué función realiza cada variable, función y clase, y en el caso de tipos booleanos, bajo qué condiciones devuelven verdadero (True)

### Normalizar todos los datos al almacenarlos
- Procesar todos los datos en un formato consistente y normalizado
- Si los mismos datos tienen más de un formato, pueden surgir errores sutiles difíciles de detectar, como ligeras diferencias en la representación de cadenas o valores hash diferentes
- Al almacenar y procesar datos como zonas horarias o cadenas, se deben convertir a un formato estándar como UTC o codificación UTF-8 inmediatamente después de recibirlos o calcularlos. Es mejor realizar la normalización desde el principio en el constructor de la clase que representa los datos o en la función que recibe los datos.

### Separar la lógica del código y los datos
- Los datos que no están relacionados con la lógica del código no deben incluirse directamente en declaraciones condicionales, sino separarse en tablas independientes  
  Por ejemplo: Es preferible escribir código como el siguiente en lugar del anterior.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ~~~c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ~~~
