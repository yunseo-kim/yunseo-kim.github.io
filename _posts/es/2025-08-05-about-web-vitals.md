번역문 1입니다.

---
title: Métricas de rendimiento web (Web Vitals)
description: Resumen de las Web Vitals y de cómo Lighthouse las mide y puntúa; explicación de qué significan métricas como LCP, INP, CLS, TBT, FCP y SI y cómo optimizarlas.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Factores que determinan el rendimiento web
Al optimizar el rendimiento web, los factores que lo determinan pueden agruparse, a grandes rasgos, en dos categorías: rendimiento de carga y rendimiento de renderizado.

### Rendimiento de carga de HTML
- Tiempo desde que se solicita por primera vez la página al servidor a través de la red hasta que el navegador recibe el documento HTML y comienza a renderizar
- Determina con qué rapidez empieza a mostrarse la página
- Se optimiza minimizando redirecciones, almacenando en caché la respuesta HTML, comprimiendo recursos y usando una CDN adecuada, entre otros métodos

### Rendimiento de renderizado
- Tiempo que tarda el navegador en dibujar lo que ve el usuario y dejarlo listo para la interacción
- Determina cuán fluida y rápida es la representación visual
- Se optimiza eliminando CSS y JS innecesarios, evitando la carga diferida de fuentes y miniaturas, separando operaciones pesadas en un Web Worker para minimizar la ocupación del hilo principal, y optimizando animaciones, entre otros métodos

## Métricas de rendimiento web (Web Vitals)
Se describe con base en [web.dev de Google](https://web.dev/performance?hl={{ site.active_lang }}) y la [documentación para desarrolladores de Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Salvo que haya una razón especial, es mejor apuntar a mejoras generales que centrarse en una sola métrica, e identificar qué parte de la página actúa como cuello de botella. Si dispones de estadísticas de usuarios reales, conviene fijarse en valores del cuartil inferior (Q1) en lugar de los mejores o promedio, y verificar y mejorar para que también cumplan el objetivo en esos casos.

### Métricas esenciales de la web (Core Web Vitals)
Como veremos enseguida, existen varias Web Vitals. Entre ellas, Google considera especialmente importantes tres que se relacionan estrechamente con la experiencia de usuario y que se pueden medir en condiciones reales (no solo de laboratorio); a estas se las denomina [Métricas esenciales de la web (Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Google tiene en cuenta estas métricas en el orden de resultados de su buscador, por lo que para los operadores de sitios también son relevantes desde la perspectiva del SEO.
- [Pintura con contenido más grande (LCP)](#lcp-pintura-con-contenido-mas-grande): refleja el rendimiento de carga; debe ser ≤ 2,5 s
- [Interacción hasta la siguiente pintura (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): refleja la capacidad de respuesta; debe ser ≤ 200 ms
- [Cambio de diseño acumulado (CLS)](#cls-cambio-de-diseno-acumulado): refleja la estabilidad visual; debe mantenerse ≤ 0,1

Aunque las Core Web Vitals se concibieron para medirse en el entorno real, dos de ellas (salvo INP) también pueden medirse en entornos de laboratorio como las DevTools de Chrome o Lighthouse. INP requiere entradas reales de usuarios, por lo que no se puede medir en laboratorio; en estos casos, [TBT](#tbt-tiempo-de-bloqueo-total) está muy correlacionada con INP y es una métrica similar a la que se puede recurrir, y [normalmente al mejorar TBT también mejora INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Ponderación de la puntuación de rendimiento en Lighthouse 10
[La puntuación de rendimiento de Lighthouse es un promedio ponderado de cada métrica, siguiendo los pesos de la tabla siguiente](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Métrica | Peso |
| --- | --- |
| [Pintura con contenido inicial](#fcp-pintura-con-contenido-inicial) | 10% |
| [Índice de velocidad](#si-indice-de-velocidad) | 10% |
| [Pintura con contenido más grande](#lcp-pintura-con-contenido-mas-grande) | 25% |
| [Tiempo de bloqueo total](#tbt-tiempo-de-bloqueo-total) | 30% |
| [Cambio de diseño acumulado](#cls-cambio-de-diseno-acumulado) | 25% |

### FCP (First Contentful Paint) {#fcp-pintura-con-contenido-inicial}
- Mide el tiempo hasta que, tras solicitar la página, se renderiza el primer contenido del DOM
- Se consideran contenido del DOM las imágenes de la página, elementos `<canvas>` que no sean en blanco, SVG, etc.; no se considera el contenido dentro de `iframe`

> Uno de los factores que más inciden en FCP es el tiempo de carga de las fuentes. En la [documentación de Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recomiendan consultar esta [entrada relacionada](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) para su optimización.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación de Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Nivel de color | FCP móvil (s) | FCP de escritorio (s) |
| --- | --- | --- |
| Verde (rápido) | 0-1,8 | 0-0,9 |
| Naranja (medio) | 1,8-3 | 0,9-1,6 |
| Rojo (lento) | Más de 3 | Más de 1,6 |

### LCP (Largest Contentful Paint) {#lcp-pintura-con-contenido-mas-grande}
- Toma como referencia el área visible inicial (viewport) al abrir por primera vez la página, y mide el tiempo hasta renderizar el elemento (imagen, bloque de texto, vídeo, etc.) más grande dentro de esa área
- Cuanto mayor sea el área que ocupa en pantalla, más probable es que el usuario lo perciba como contenido principal
- Si el LCP es una imagen, el tiempo puede dividirse en 4 subintervalos; es importante identificar dónde se produce el cuello de botella:
  1. Time to first byte (TTFB): tiempo desde el inicio de la carga de la página hasta recibir el primer byte de la respuesta del documento HTML
  2. Retraso de carga (Load delay): diferencia entre el momento en que el navegador empieza a cargar el recurso LCP y el TTFB
  3. Tiempo de carga (Load time): tiempo necesario para cargar el recurso LCP como tal
  4. Retraso de renderizado (Render delay): tiempo desde que finaliza la carga del recurso LCP hasta que el elemento LCP se renderiza por completo

#### Criterios de evaluación de Lighthouse
Según la [documentación de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Nivel de color | FCP móvil (s) | FCP de escritorio (s) |
| --- | --- | --- |
| Verde (rápido) | 0-2,5 | 0-1,2 |
| Naranja (medio) | 2,5-4 | 1,2-2,4 |
| Rojo (lento) | Más de 4 | Más de 2,4 |

### TBT (Total Blocking Time) {#tbt-tiempo-de-bloqueo-total}
- Mide el tiempo total durante el cual la página no puede responder a entradas del usuario como clics de ratón, toques táctiles o teclado
- Entre FCP y [TTI (Time to Interactive, inicio de la interactividad)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, se consideran [tareas largas](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}) aquellas que tardan más de 50 ms; de cada una se resta 50 ms y la parte restante se denomina porción de bloqueo. La suma de todas estas porciones se define como TBT

> \* El propio TTI es demasiado sensible a valores atípicos de la red y a tareas largas, lo que reduce su consistencia y aumenta su variabilidad; por ello, [a partir de Lighthouse 10 se excluyó de las métricas de evaluación](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Las causas más comunes de tareas largas suelen ser la carga, el análisis y la ejecución de JavaScript innecesario o ineficiente. La [documentación de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) y [web.dev de Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recomiendan reducir el payload de JavaScript mediante [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) para que cada parte se ejecute en ≤ 50 ms y, si es necesario, separar tareas fuera del hilo principal, por ejemplo en un Service Worker, para ejecutarlas en multihilo.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación de Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Nivel de color | FCP móvil (ms) | FCP de escritorio (ms) |
| --- | --- | --- |
| Verde (rápido) | 0-200 | 0-150 |
| Naranja (medio) | 200-600 | 150-350 |
| Rojo (lento) | Más de 600 | Más de 350 |

### CLS (Cumulative Layout Shift) {#cls-cambio-de-diseno-acumulado}
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Ejemplo de cambio de diseño inesperado" autoplay=true loop=true %}
> Fuente del video: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Se percibe una profunda rabia en el movimiento del cursor~~

- Los cambios de diseño inesperados perjudican la experiencia de usuario de múltiples formas: el texto puede moverse de repente y hacer que se pierda la línea, o se puede hacer clic por error en un enlace o botón, etc.
- La forma exacta de calcular la puntuación CLS está descrita en [web.dev de Google](https://web.dev/articles/cls)
- Como puede verse en la imagen inferior, el objetivo debe ser ≤ 0,1

![¿Cuál es un buen valor de CLS?](/assets/img/about-web-vitals/good-cls-values.svg)
> Fuente de la imagen: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index) {#si-indice-de-velocidad}
- Mide cuán rápido se muestra visualmente el contenido durante la carga de la página
- Lighthouse graba en vídeo el proceso de carga del navegador, analiza el vídeo para calcular el progreso entre fotogramas y usa el [módulo Speedline para Node.js](https://github.com/paulirish/speedline) para calcular la puntuación de SI

> Además de lo mencionado al resumir [FCP](#fcp-pintura-con-contenido-inicial), [LCP](#lcp-pintura-con-contenido-mas-grande) y [TBT](#tbt-tiempo-de-bloqueo-total), cualquier medida que acelere la carga de la página suele mejorar también la puntuación de SI. Más que representar una única fase de carga, es una métrica que refleja el proceso de carga global en cierto grado.
{: .prompt-tip }

#### Criterios de evaluación de Lighthouse
Según la [documentación de Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), los criterios de Lighthouse son los siguientes.

| Nivel de color | SI móvil (s) | SI de escritorio (s) |
| --- | --- | --- |
| Verde (rápido) | 0-3,4 | 0-1,3 |
| Naranja (medio) | 3,4-5,8 | 1,3-2,3 |
| Rojo (lento) | Más de 5,8 | Más de 2,3 |
