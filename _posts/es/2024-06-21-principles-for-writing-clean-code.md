---
title: Principios para escribir buen código
description: "Por qué es importante escribir buen código y los principios clave para lograrlo: simplicidad, modularidad, convenciones de nombres, librerías y más."
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## Por qué es necesario escribir buen código
Si te centras solo en escribir código rápido para la implementación inmediata, la [deuda técnica](/posts/Technical-debt/) puede crecer hasta niveles inmanejables y causar problemas de mantenimiento a futuro. Por lo tanto, al llevar a cabo un proyecto de desarrollo, es fundamental desde el inicio escribir buen código, legible y fácil de mantener.

En algoritmia para resolución de problemas (PS, Problem Solving) o en programación competitiva (CP, Competitive Programming), suele decirse que el código utilizado para resolver un problema rara vez se reutiliza una vez finalizados el problema o la competición, y que, especialmente en CP, debido a los límites de tiempo, la implementación rápida importa más que escribir buen código. Para responder a esta cuestión, conviene reflexionar sobre por qué haces PS/CP y qué objetivos persigues.

En mi opinión, dejando de lado el desarrollo de habilidades generales de resolución de problemas y centrándome en el aspecto relacionado con la programación, a través de PS/CP se pueden aprender, entre otras, las siguientes cosas:
- Al resolver problemas bajo restricciones de tiempo de ejecución y memoria, puedes usar y familiarizarte con diversos algoritmos y estructuras de datos; esto te ayuda a intuir qué algoritmos y estructuras de datos conviene usar en situaciones concretas de proyectos reales.
- Al escribir y enviar código, recibes retroalimentación objetiva e inmediata sobre si es correcto o no, y sobre el tiempo de ejecución y el uso de memoria; así puedes practicar escribir código correcto con rapidez y destreza, sin pasar por alto detalles.
- Puedes comparar tu código con el de personas más expertas y encontrar puntos de mejora.
- A diferencia de los proyectos reales, sueles escribir repetidamente código de pequeña escala con funcionalidades similares y, (especialmente si practicas PS por tu cuenta) sin la presión de plazos, puedes prestar atención a los detalles y practicar escribir código conciso y de calidad.

Por supuesto, puede haber quien disfrute de PS/CP simplemente como afición; pero si lo haces para mejorar tus habilidades de programación, el “entrenamiento para escribir buen código” del último punto es tan valioso como los tres anteriores. Escribir buen código no sale de forma natural desde el principio; requiere práctica repetida y mejora constante. Además, el código complejo y difícil de leer es más complicado de depurar y, para uno mismo, también es más difícil escribirlo correctamente a la primera; si terminas dedicando tiempo a una depuración ineficiente, a menudo ni siquiera implementas tan rápido como pretendías. Aunque PS/CP difiera bastante del trabajo en el mundo real, por estas razones no tiene sentido ignorar por completo escribir buen código para centrarse solo en implementar “como sea”. Personalmente, incluso en PS/CP, creo que conviene escribir código conciso y eficiente. 

> 12024.12 Comentario adicional:  
> A la vista del panorama actual, seguir adquiriendo bases como algoritmos y estructuras de datos para escribir programas eficientes y desarrollar capacidad de resolución de problemas seguirá teniendo sentido; pero, en la fase de llevarlo a código funcional, quizá no haga falta insistir en escribir cada línea a mano. Puede ser mejor aprovechar activamente herramientas de IA como GitHub Copilot, Cursor o Windsurf, ahorrar tiempo y dedicarlo a otras tareas o estudio. Si haces PS/CP para entrenar la resolución de problemas general o estudiar algoritmos/estructuras de datos, o porque te gusta como afición, perfecto; pero dedicar tiempo y esfuerzo a PS/CP exclusivamente para practicar la escritura de código ahora parece ofrecer un rendimiento mucho menor en relación con el coste. Incluso en empleos de desarrollo, estimo que, al menos como prueba de ingreso, la importancia de los coding tests bajará bastante respecto a antes.
{: .prompt-warning }

## Principios para escribir buen código
Ya sea código para concursos o para el trabajo, las condiciones que definen “buen código” no difieren mucho. En esta entrada trato los principios clave para escribir buen código en general. Eso sí, en PS/CP puede haber concesiones en pos de la velocidad de implementación; cuando proceda, lo mencionaré explícitamente.

### Escribe código conciso
> "KISS (Keep It Simple, Stupid)"

- Cuanto más corto y conciso sea el código, menor será el riesgo de typos o bugs triviales, y más fácil será depurarlo.
- Procura que pueda interpretarse fácilmente incluso sin comentarios; añade comentarios solo cuando sean realmente necesarios. Es preferible depender menos de comentarios y mantener la estructura del código simple y clara.
- Si escribes comentarios, que sean claros y concisos.
- Pasa como máximo 3 argumentos a una función; si necesitas pasar más, encapsúlalos en un solo objeto.
- La anidación profunda de condicionales perjudica la legibilidad; evita aumentar la profundidad.  
  p. ej.) Usar cláusulas de guarda (guard clauses) como en el siguiente código suele mejorar la legibilidad frente al ejemplo superior.  

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
- En PS/CP, a veces se recurre a atajos como macros de C/C++ para reducir aún más el tamaño del código y escribir más rápido. En concursos con tiempo limitado pueden ser útiles, pero es una práctica que solo “funciona” en PS/CP; en general, en C++ conviene evitar los macros.  
  p. ej.)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modulariza el código
> "DRY (Don't Repeat Yourself)"

- Si repites el mismo código, extrae esa parte en una función o clase para reutilizarla.
- La modularización fomenta la reutilización, mejora la legibilidad y facilita el mantenimiento, pues basta con modificar la función o clase en un solo lugar.
- En principio, es ideal que cada función haga solo una cosa. Sin embargo, el código de PS/CP suele ser de pequeña escala, con funciones simples, la reutilización es limitada y el tiempo es escaso; por ello, puede ser difícil aplicar el principio con el mismo rigor que en el entorno profesional.

### Aprovecha la biblioteca estándar
> "No reinventes la rueda"

- En la fase de aprendizaje de algoritmos y estructuras de datos, es útil implementar por tu cuenta estructuras como colas o pilas, o algoritmos de ordenación, para entender sus principios; fuera de ese contexto, conviene aprovechar activamente la biblioteca estándar.
- Las bibliotecas estándar han sido ampliamente usadas y verificadas, y están bien optimizadas; reimplementarlas suele ser menos eficiente.
- Reutilizar lo que ya existe evita perder tiempo implementando funcionalidades duplicadas y facilita que tus compañeros entiendan el código en colaboración.

### Usa una nomenclatura clara y consistente
> "Sigue las convenciones estándar"

- Usa nombres de variables y funciones no ambiguos.
- Cada lenguaje suele tener sus propias convenciones de nombres; aprende las que usa la biblioteca estándar del lenguaje y aplícalas de forma consistente al declarar clases, funciones y variables.
- Nombra de modo que quede claro qué hace cada variable, función o clase; si es de tipo booleano, que se entienda en qué condiciones devuelve 'True'.

### Normaliza todos los datos antes de almacenarlos
- Procesa todos los datos en un formato uniforme y coherente.
- Si el mismo dato existe en dos o más formatos, pueden surgir bugs sutiles y difíciles de detectar, como pequeñas diferencias en su representación en cadena o en los valores hash.
- Al almacenar y procesar datos como zonas horarias o cadenas, conviértelos a un formato estándar único (por ejemplo, UTC, codificación UTF-8) tan pronto como se reciban o se calculen. Es buena práctica normalizar en el constructor de la clase que representa esos datos o inmediatamente en la función que los recibe.

### Separa la lógica del código y los datos
- No incrustes en condicionales datos que no formen parte de la lógica; sepáralos en una tabla aparte.  
  p. ej.) Es preferible escribirlo como en el siguiente ejemplo que como en el anterior.

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
