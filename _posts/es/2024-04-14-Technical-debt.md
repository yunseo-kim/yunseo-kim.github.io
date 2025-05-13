---
title: Deuda técnica (Technical debt)
description: Exploremos el concepto de deuda técnica, las razones por las que ocurre
  y cómo minimizarla.
categories: [Programming]
tags: [Coding]
image: /assets/img/technology.webp
---
## Deuda técnica (Technical debt)
Deuda técnica: El precio que se paga posteriormente por elegir atajos que permiten completar un proyecto más rápidamente para satisfacer requisitos inmediatos durante el proceso de desarrollo.

Al igual que asumir una deuda financiera permite invertir rápidamente en necesidades inmediatas pero conlleva presión financiera y el pago del principal más intereses, avanzar rápidamente en el desarrollo, aunque sea un poco desordenado, para resolver requisitos inmediatos hace que el código se vuelva complejo y redundante, dificultando la implementación o expansión de nuevas funciones en el futuro.

Asumir deuda técnica para implementar rápidamente nuevas funciones no es necesariamente malo, al igual que las empresas utilizan deudas para realizar más inversiones oportunas, desarrollar nuevos productos y aumentar la cuota de mercado, o los individuos obtienen préstamos para comprar casas. Sin embargo, es deseable reducir la acumulación de deuda técnica y gestionarla a un nivel manejable.

## Razones por las que ocurre la deuda técnica
La deuda técnica surge inevitablemente en el proceso de creación de software, incluso si la capacidad del desarrollador es suficiente, y es imposible prevenirla por completo.
A medida que un servicio evoluciona, puede llegar a los límites del código diseñado originalmente, y puede ser necesario modificar el diseño existente incluso si el código era originalmente legible y funcionaba bien.
Además, a medida que la tecnología misma avanza, se puede tomar la decisión de cambiar la pila tecnológica a otras bibliotecas/frameworks si las que antes eran tendencia ya no se usan mucho, y en este caso, el código escrito previamente también se convierte en una especie de deuda técnica.

Además de estas, la deuda técnica puede ocurrir por las siguientes razones:
- Cuando no se documenta el diseño a tiempo durante el proyecto, lo que dificulta la interpretación del código cuando otra persona o incluso uno mismo lo revisa después de un tiempo
- Cuando no se eliminan variables o elementos de la base de datos que ya no se utilizan
- Cuando no se automatizan tareas repetitivas (despliegue/compilación, etc.), lo que requiere tiempo y esfuerzo adicionales cada vez
- Cambios urgentes en las especificaciones

## Cómo minimizar la deuda técnica
### Establecer convenciones entre desarrolladores
- Si no se está desarrollando solo, es necesario llegar a un acuerdo sobre el lenguaje o la pila tecnológica a utilizar, la estructura de directorios del proyecto, el estilo de desarrollo, etc., para una colaboración fluida
- Se debe decidir hasta qué punto unificar los métodos y a partir de dónde dejar autonomía individual
- Es necesario verificar los estilos de desarrollo de cada uno y compartir opiniones a través de revisiones de código

### Escribir código limpio (Clean Code) y refactorizar (Refactoring)
- Si el código existente es desordenado y obstaculiza el desarrollo, se puede liquidar la deuda técnica mediante la refactorización, que modifica la estructura del código para hacerlo más limpio
- Naturalmente, cuanto más desordenado sea el código existente, más difícil será la refactorización
- Se debe hacer un esfuerzo por escribir código legible y fácil de mantener desde el principio en la medida de lo posible
