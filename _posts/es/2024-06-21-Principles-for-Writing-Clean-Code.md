---
title: "Principios para escribir buen código"
description: >-
  Exploramos la necesidad de escribir buen código y los principios generales para hacerlo.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.jpg
---
## La necesidad de escribir buen código
Si nos apresuramos a escribir código rápidamente solo para la implementación inmediata, la [deuda técnica](/posts/Technical-debt/) puede crecer a niveles inmanejables, causando problemas de mantenimiento en el futuro. Por lo tanto, es innegablemente importante escribir código legible y fácil de mantener desde el principio cuando se lleva a cabo un proyecto de desarrollo.

En el caso de la resolución de problemas algorítmicos (PS, Problem Solving) o la programación competitiva (CP, Competitive Programming), generalmente no se reutiliza el código utilizado para resolver el problema después de que termina la resolución del problema o la competencia. Especialmente en CP, debido a las limitaciones de tiempo, algunos argumentan que la implementación rápida es más importante que escribir buen código. Para responder a esta pregunta, es necesario considerar para qué se hace PS/CP y qué dirección se busca.

En mi opinión personal, los puntos que se pueden aprender a través de PS/CP son los siguientes:
- Se pueden usar y aprender diversos algoritmos y estructuras de datos en el proceso de resolver problemas dentro de las condiciones dadas, como límites de tiempo de ejecución y memoria, y a través de esto, se puede desarrollar una intuición sobre qué algoritmos y estructuras de datos usar en situaciones específicas cuando se lleva a cabo un proyecto real
- Después de escribir y enviar el código, se puede recibir retroalimentación objetiva inmediata sobre si es correcto/incorrecto, el tiempo de ejecución y el uso de memoria, por lo que se puede practicar escribir código preciso rápida y hábilmente sin perder ningún detalle
- Se puede ver el código escrito por otros expertos, compararlo con el propio código y encontrar áreas de mejora
- En comparación con los proyectos de desarrollo reales, se escribe repetidamente código de escala más pequeña que realiza funciones similares, por lo que (especialmente cuando se practica PS solo) se puede practicar escribir código conciso y bueno prestando atención a los detalles sin estar atado a plazos de entrega, etc.

Aunque por supuesto puede haber casos en los que PS/CP se disfrute simplemente como un pasatiempo, si se hace PS/CP indirectamente para mejorar las habilidades de programación, la "práctica de escribir buen código" mencionada al final es una gran ventaja no menos importante que las tres anteriores. Esto se debe a que escribir buen código no es algo que ocurra naturalmente desde el principio, sino que requiere práctica constante y repetida para dominarlo. Además, el código complejo y difícil de leer es difícil de depurar y no es fácil de escribir correctamente de una vez incluso para uno mismo, por lo que si se pierde tiempo en depuración ineficiente, a menudo no se logra una implementación tan rápida. Aunque PS/CP es, por supuesto, muy diferente del trabajo real, por las razones mencionadas anteriormente, ignorar completamente la escritura de buen código y apresurarse solo por la implementación inmediata es invertir las prioridades, por lo que personalmente pienso que es mejor escribir código conciso y eficiente incluso en PS/CP.

> Comentario añadido en diciembre de 2024:  
> Dado el ambiente actual, a menos que se esté especializando en ingeniería informática y se vaya a dedicar al desarrollo en sí, si se planea usar la programación como una herramienta para análisis numérico o interpretación de datos experimentales, parece mejor usar activamente IA como GitHub Copilot, Cursor, Windsurf, etc. para ahorrar tiempo y usar ese tiempo ahorrado para estudiar otras cosas. Si se disfruta PS/CP como pasatiempo, nadie lo va a impedir, pero dedicar tiempo y esfuerzo a PS/CP para practicar la escritura de código parece tener una baja relación costo-beneficio ahora. Incluso para puestos de desarrollo, se espera que la importancia de las pruebas de codificación como examen de ingreso probablemente disminuya considerablemente en comparación con antes.
{: .prompt-warning }

## Principios para escribir buen código
Ya sea código escrito en competencias o código escrito en el trabajo real, las condiciones para considerarlo buen código no son muy diferentes. Este artículo trata los principales principios para escribir buen código en general. Sin embargo, en PS/CP puede haber áreas donde se compromete relativamente en comparación con el trabajo real para una implementación rápida, y estos casos se mencionarán por separado en el artículo.

### Escribir código conciso
> "KISS (Keep It Simple, Stupid)"

- Cuanto más corto y conciso sea el código, naturalmente hay menos preocupación por errores tipográficos o errores simples, y la depuración es más fácil
- Escribir de manera que se pueda interpretar fácilmente sin comentarios adicionales siempre que sea posible, y agregar explicaciones detalladas con comentarios solo cuando sea realmente necesario. Es preferible mantener la estructura del código concisa en lugar de depender de comentarios.
- Si se escriben comentarios, hacerlo de manera clara y concisa
- Limitar los argumentos pasados a una función a 3 o menos, y si se necesitan más argumentos, agruparlos en un solo objeto para pasarlos
- La profundidad (depth) de las declaraciones condicionales que se vuelven dobles o triples reduce la legibilidad, por lo que se debe evitar aumentar la profundidad de las declaraciones condicionales tanto como sea posible. 
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
- Sin embargo, en PS/CP, a veces se usa el truco de usar macros de C/C++ para reducir aún más la longitud del código y escribirlo rápidamente. Es útil usarlo ocasionalmente limitado a competencias con tiempo limitado, pero es un método que solo funciona en PS/CP y generalmente se debe evitar el uso de macros en C++.  
  ej)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularización del código
> "DRY (Don't Repeat Yourself)"

- Si se usa el mismo código repetidamente, separar esa parte en una función o clase para reutilizarla
- La reutilización activa del código a través de la modularización mejora la legibilidad y facilita el mantenimiento, ya que solo se necesita modificar la función o clase correspondiente si es necesario modificar el código en el futuro
- En principio, lo ideal es que una función realice solo una funcionalidad y no haga dos o más cosas. Sin embargo, el código escrito en PS/CP generalmente es un programa de pequeña escala que realiza funciones simples, por lo que hay límites en la reutilización, y debido a las limitaciones de tiempo, puede ser difícil seguir los principios tan estrictamente como en el trabajo real.

### Utilización de bibliotecas estándar
> "Don't reinvent the wheel"

- En la etapa de estudio de algoritmos o estructuras de datos, es útil implementar directamente estructuras de datos como colas o pilas, algoritmos de ordenamiento, etc. para entender los principios, pero si no es ese el caso, es mejor utilizar activamente las bibliotecas estándar
- Las bibliotecas estándar ya han sido utilizadas y verificadas innumerables veces, y están bien optimizadas, por lo que son más eficientes que implementarlas directamente de nuevo
- Como se pueden usar bibliotecas ya existentes, no es necesario perder tiempo implementando innecesariamente código que realiza la misma función, y es más fácil para otros miembros del equipo entender el código escrito durante la colaboración

### Uso de nomenclatura consistente y clara
> "Follow standard conventions"

- Usar nombres de variables y funciones que no sean ambiguos
- Generalmente, cada lenguaje de programación tiene sus propias convenciones de nomenclatura, así que es mejor aprender las convenciones de nomenclatura utilizadas en la biblioteca estándar del lenguaje que se está usando y aplicarlas consistentemente al declarar clases, funciones, variables, etc.
- Nombrar de manera que quede claro qué función realiza cada variable, función y clase, y en el caso de tipos booleanos, en qué condiciones devuelve verdadero (True)

### Normalizar todos los datos antes de almacenarlos
- Procesar todos los datos normalizándolos en un formato consistente
- Si los mismos datos tienen dos o más formatos, pueden ocurrir errores sutiles difíciles de detectar, como ligeras diferencias en la representación de cadenas o diferencias en los valores hash
- Al almacenar y procesar datos como zonas horarias, cadenas, etc., se deben convertir a un formato estándar único como UTC, codificación UTF-8, etc. tan pronto como se reciban o calculen. Es mejor realizar la normalización desde el principio en el constructor de la clase que representa los datos o realizar la normalización inmediatamente en la función que recibe los datos.

### Separar la lógica del código y los datos
- No incluir directamente en las declaraciones condicionales los datos que no están relacionados con la lógica del código, sino separarlos en una tabla aparte  
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
