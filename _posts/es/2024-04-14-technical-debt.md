---
title: Deuda técnica
description: "Concepto de deuda técnica, por qué surge y cómo minimizarla en el desarrollo de software mediante convenciones de equipo, código limpio y refactorización."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Deuda técnica
> **Deuda técnica**  
> El coste que se debe pagar después por tomar atajos para terminar más rápido un proyecto y satisfacer necesidades inmediatas durante el desarrollo
{: .prompt-info }

Igual que asumir deuda financiera permite invertir rápidamente donde hace falta, a costa de presión financiera y de devolver principal e intereses, avanzar deprisa para atender requisitos urgentes —aunque el código quede algo desordenado— puede complicar y duplicar el código, dificultando la implementación o ampliación de nuevas funciones más adelante.

Del mismo modo que una empresa puede usar deuda para invertir a tiempo, desarrollar nuevos productos y ganar cuota de mercado, o una persona puede firmar una hipoteca para comprar una casa, asumir cierta deuda técnica para lanzar antes una funcionalidad no es intrínsecamente malo. Lo deseable es reducir su acumulación y gestionarla en un nivel asumible.

## Por qué surge la deuda técnica
Incluso con desarrolladores competentes, la deuda técnica es, en cierta medida, inevitable durante el desarrollo; prevenirla por completo es imposible. A medida que el servicio evoluciona y el diseño original alcanza sus límites, puede ser necesario modificarlo, aunque el código fuera legible y funcionara bien. Además, con la evolución de la tecnología, librerías o frameworks que antes eran estándar pueden dejar de usarse; al migrar el stack tecnológico, el código previo se convierte también en una forma de deuda técnica.

Además, puede aparecer por motivos como los siguientes:
- No documentar a tiempo lo diseñado durante el proyecto, lo que dificulta la comprensión para otras personas o para uno mismo con el paso del tiempo.
- No eliminar variables o elementos de BD que ya no se utilizan.
- No automatizar tareas repetitivas (despliegue/compilación, etc.), añadiendo tiempo y esfuerzo en cada ocasión.
- Cambios urgentes de requisitos.

## Cómo minimizar la deuda técnica
### Establecer convenciones entre desarrolladores
- Si no se desarrolla en solitario, es necesario acordar lenguaje, stack tecnológico, estructura de directorios del proyecto, estilo de desarrollo, etc., para colaborar con fluidez.
- Decidir hasta dónde estandarizar y a partir de qué punto dejar libertad individual.
- Realizar revisiones de código para alinear estilos y compartir opiniones.

### Escribir código limpio (Clean Code) y refactorizar (Refactoring)
- Si el código existente está desordenado y entorpece el desarrollo, se puede amortizar la deuda técnica refactorizando para mejorar su estructura.
- Cuanto más spaghetti sea el código, mayor será la dificultad de refactorizar; en casos extremos, puede ser preferible abandonarlo y reescribir desde cero.
- En lo posible, esforzarse por escribir desde el principio código legible y fácil de mantener.
